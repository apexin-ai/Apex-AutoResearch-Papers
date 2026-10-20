# Research conversation: I'm working on a research proposal about active annotation disagreement resolution. I need to find any recent papers (20

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 122
- **Recorded user turns:** 1
- **Tool calls:** 58
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a353a15cb7baef652.jsonl`
- **Structured JSON:** [`cc60d5e440e424345a97.json`](../../sessions/cc/cc60d5e440e424345a97.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

122 recorded events

### User

_source line 1 · 2026-05-10T07:58:14.780Z_

I'm working on a research proposal about active annotation disagreement resolution. I need to find any recent papers (2025-2026) that might overlap with the following core approach:

The proposal (called DART) involves:
1. Classifying annotation disagreements into types (conceptual ambiguity, value divergence, borderline threshold)
2. Generating type-specific clarification probes for disagreeing annotators
3. Using probe responses to update soft-label training distributions

Please search for papers about:
1. "active annotation" + "disagreement" + "probing" or "clarification" (2024-2026)
2. "type-conditioned" annotation disagreement resolution
3. "annotation disagreement taxonomy" + "probe generation" or "clarification questions"
4. Recent papers (2025-2026) that combine disagreement typing with active learning or probe generation
5. Any papers that specifically address the "borderline threshold" vs "conceptual ambiguity" distinction in annotation

Use WebSearch and fetch abstracts of any relevant papers you find. Also check:
- Recent EMNLP 2025, ACL 2025, EACL 2026 proceedings for annotation disagreement papers
- arXiv cs.CL from Jan 2026 onwards for relevant work

Report paper titles, venues, and a 2-3 sentence summary of what each does, focusing on overlap with DART's approach.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "4ca74ac7-0732-4e62-bccb-b31d025970d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T07:58:14.783Z_

```json
{
  "parentUuid": "4ca74ac7-0732-4e62-bccb-b31d025970d9",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
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
  "uuid": "3dcce2fb-62ed-40e9-a3b6-063d4f4cf660",
  "timestamp": "2026-05-10T07:58:14.783Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T07:58:16.537Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QV8zHqHu9yj6a5ycNaib93`</summary>

```json
{
  "query": "select:WebSearch,WebFetch"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dcce2fb-62ed-40e9-a3b6-063d4f4cf660",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXsVWqmj6oLkVvvJEen",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "36cf0d90-b0be-48b8-9a27-f7c5016b2fe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PjwvHg6feCqUmBaXSTKa4c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 8088,
      "output_tokens": 61,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 867
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 61,
          "cache_read_input_tokens": 8088,
          "cache_creation_input_tokens": 867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 867,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-10T07:58:16.539Z_

<details><summary>↩ Tool result · `toolu_01QV8zHqHu9yj6a5ycNaib93`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

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
  "parentUuid": "36cf0d90-b0be-48b8-9a27-f7c5016b2fe0",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "e39edd1a-c388-4446-9a49-a90c9f7711d7",
  "sourceToolAssistantUUID": "36cf0d90-b0be-48b8-9a27-f7c5016b2fe0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-10T07:58:18.697Z_

I'll run multiple searches in parallel to cover all the angles you've outlined for DART.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e39edd1a-c388-4446-9a49-a90c9f7711d7",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXsdFS2kauAoaqYum3C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8379a3a3-43ee-4cea-9930-5130720bb43c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XgNUiJdto3ZU9QQCpj6bsQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1869,
      "cache_read_input_tokens": 8955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1869,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T07:58:19.085Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EbbfNLhhctdnhdXwDtWPdv`</summary>

```json
{
  "query": "active annotation disagreement probing clarification 2025 2026 NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8379a3a3-43ee-4cea-9930-5130720bb43c",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXsdFS2kauAoaqYum3C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fd6cc41c-6f01-40ae-8749-5910fe483474",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XgNUiJdto3ZU9QQCpj6bsQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1869,
      "cache_read_input_tokens": 8955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1869,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T07:58:19.467Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FYYD9p9YXb36RjoU4CpdZG`</summary>

```json
{
  "query": "annotation disagreement taxonomy classification types NLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd6cc41c-6f01-40ae-8749-5910fe483474",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXsdFS2kauAoaqYum3C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2f42898e-f045-4985-b612-cb474b22d9e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XgNUiJdto3ZU9QQCpj6bsQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1869,
      "cache_read_input_tokens": 8955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1869,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T07:58:19.702Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017QcEXbJXpeRGaWjBsbYnPS`</summary>

```json
{
  "query": "type-conditioned annotation disagreement resolution soft labels 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f42898e-f045-4985-b612-cb474b22d9e8",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXsdFS2kauAoaqYum3C",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "05ed4316-e5ab-4925-89d9-bfa0ea16424e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XgNUiJdto3ZU9QQCpj6bsQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1869,
      "cache_read_input_tokens": 8955,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1869
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 180,
          "cache_read_input_tokens": 8955,
          "cache_creation_input_tokens": 1869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1869,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T07:58:26.354Z_

<details><summary>↩ Tool result · `toolu_01FYYD9p9YXb36RjoU4CpdZG`</summary>

```text
Web search results for query: "annotation disagreement taxonomy classification types NLP 2025"

Links: [{"title":"The Case for Ambiguity Detection in NLI","url":"https://aclanthology.org/2025.nlperspectives-1.4.pdf"},{"title":"A Comprehensive Taxonomy of Negation for NLP and Neural Retrievers","url":"https://arxiv.org/html/2507.22337"},{"title":"DEALING WITH ANNOTATOR DISAGREEMENT IN HATE SPEECH CLASSIFICATION A PREPRINT","url":"https://arxiv.org/pdf/2502.08266"},{"title":"Beyond Black-Box Labels: Interpretable Criteria for Diagnosing Subjective NLP Tasks","url":"https://arxiv.org/html/2604.17022"},{"title":"Weak Ensemble Learning from Multiple Annotators for ...","url":"https://aclanthology.org/2025.nlperspectives-1.8.pdf"},{"title":"CARE: A Disagreement Detection Framework with Concept ...","url":"https://aclanthology.org/2025.emnlp-main.671.pdf"},{"title":"A Comprehensive Taxonomy of Negation for NLP and Neural Retrievers","url":"https://staff.fnwi.uva.nl/m.derijke/wp-content/papercite-data/pdf/petcu-2025-comprehensive-arxiv.pdf"},{"title":"Enriching Subjective Data Annotation through Qualitative ...","url":"https://aclanthology.org/2025.hcinlp-1.20.pdf"},{"title":"Modeling Annotator Disagreement with Demographic-Aware Experts and","url":"https://arxiv.org/pdf/2508.02853"},{"title":"Investigating Reasons for Disagreement in Natural Language Inference | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00523/114372/Investigating-Reasons-for-Disagreement-in-Natural"}]

Based on the search results, I found several recent works on annotation disagreement taxonomy and classification types in NLP from 2025 and related work:

## Key Findings on Annotation Disagreement Taxonomies

**Disagreement Sources and Classification Types:**

Recent research investigates how disagreement in natural language inference (NLI) annotation arises, with a taxonomy of disagreement sources containing 10 categories spanning 3 high-level classes. Some disagreements are due to uncertainty in the sentence meaning, while others stem from annotator biases and task artifacts, leading to different interpretations of the label distribution.

**Task-Specific Taxonomies:**

In the context of NLI tasks, Liu et al. (2023) introduced a taxonomy, and Li et al. (2024) refined the classification by proposing finer-grained types such as Type/Token and Collective/Distributive.

**Subjective Task Disagreement:**

Disagreement among annotators is common in subjective NLP tasks like toxicity classification, misinformation detection, and stance analysis. Annotator disagreement often stems not only from individual differences but also from ambiguities in the data and context, and rather than removing such disagreement as noise, recent work advocates for embracing it as a signal.

**Disagreement Detection Framework:**

Recent 2025 work includes a framework that constructs stance taxonomy serving as task instruction for zero-shot learning, and performs data synthesis and taxonomy-based counterfactual augmentation for curriculum learning.

The research emphasizes treating disagreement as meaningful signal rather than noise, particularly in subjective classification tasks in NLP.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f42898e-f045-4985-b612-cb474b22d9e8",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "46e6f10f-56d2-4d2f-ac5f-6264d1129517",
  "sourceToolAssistantUUID": "2f42898e-f045-4985-b612-cb474b22d9e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T07:58:27.129Z_

<details><summary>↩ Tool result · `toolu_01EbbfNLhhctdnhdXwDtWPdv`</summary>

```text
Web search results for query: "active annotation disagreement probing clarification 2025 2026 NLP"

Links: [{"title":"Can Large Language Models Capture Human Annotator Disagreements? by Jingwei Ni, Yu Fan, Vilém Zouhar, Donya Rooein, Alexander Hoyle, Mrinmaya Sachan, Markus Leippold, Dirk Hovy, Elliott Ash :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/5319936.pdf?abstractid=5319936"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Text Annotation Tool: A 2026 Guide for ML and NLP Teams | Label Your Data","url":"https://labelyourdata.com/articles/data-annotation/text-annotation-tool"},{"title":"Active Learning Machine Learning: How It Reduces Labeling Costs in 2026 | Label Your Data","url":"https://labelyourdata.com/articles/active-learning-machine-learning"},{"title":"Another Approach to Agreement Measurement and Prediction with Emotion Annotations - ACL Anthology","url":"https://aclanthology.org/2025.law-1.7/"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP","url":"https://arxiv.org/html/2601.09065"},{"title":"Counting on Consensus: Selecting the Right Inter-annotator Agreement Metric for NLP Annotation and Evaluation","url":"https://arxiv.org/html/2603.06865"},{"title":"Will Annotators Disagree? Identifying Subjectivity in Value-Laden Arguments","url":"https://arxiv.org/html/2509.06704"},{"title":"Automating Annotation Guideline Improvements using LLMs: A Case Study - ACL Anthology","url":"https://aclanthology.org/2025.comedi-1.13/"}]

Based on the search results, I found several recent papers and resources on active annotation, disagreement, probing, and clarification in NLP from 2025-2026:

## Key Recent Work

**Large Language Models and Annotator Disagreement:**
Human annotation variation (i.e., annotation disagreements) is common in NLP and often reflects important information such as task subjectivity and sample ambiguity, and recent work extensively evaluates LLMs' ability to predict annotation disagreements without access to repeated human labels. LLMs struggle with modeling disagreements, which can be overlooked by majority label-based evaluations.

**Perspectivist Approaches:**
Mixture-of-experts approaches capture feature-level heterogeneity, while Jury Learning combines content, annotator, and demographic embeddings to predict individual votes and compose configurable juries.

**Disagreement Prediction Methods:**
An AAD-based RMSE variant for predicting annotation disagreement was proposed, with experiments on the large-scale DynaSent corpus demonstrating significant improvements in disagreement prediction accuracy, rising from 41.71% to 51.64% and outperforming existing methods.

**Guideline Improvement:**
LLMs can help produce guidelines of high quality (inter-annotator agreement going from 0.593 to 0.84 when improving WNUT-17's guidelines), while being faster and cheaper than crowdsource workers.

**Upcoming Workshop Focus:**
The 20th Linguistic Annotation Workshop (LAW XX) at ACL 2026 is specifically inviting submissions on addressing annotations which are objectively incorrect, distinct from annotator disagreement, and the role of error analysis in improving data quality for both human-annotated and LLM-generated datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd6cc41c-6f01-40ae-8749-5910fe483474",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "75777de8-97ed-4fff-b425-a730b54a59f0",
  "sourceToolAssistantUUID": "fd6cc41c-6f01-40ae-8749-5910fe483474",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T07:58:28.522Z_

<details><summary>↩ Tool result · `toolu_017QcEXbJXpeRGaWjBsbYnPS`</summary>

```text
Web search results for query: "type-conditioned annotation disagreement resolution soft labels 2025"

Links: [{"title":"STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems","url":"https://arxiv.org/html/2605.02122"},{"title":"Leveraging Annotator Disagreement via Soft-Label Multi- ...","url":"https://aclanthology.org/2021.naacl-main.204.pdf"},{"title":"Counting on Consensus: Selecting the Right Inter-annotator Agreement Metric for NLP Annotation and Evaluation","url":"https://arxiv.org/html/2603.06865"},{"title":"Soft-Label Training Preserves Epistemic Uncertainty","url":"https://arxiv.org/html/2511.14117"},{"title":"Rubric-conditioned large language model labeling: Agreement, uncertainty, and label consistency in subjective text annotation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0747563226000853"},{"title":"Quantifying and Predicting Disagreement in Graded Human Ratings","url":"https://arxiv.org/html/2605.01168"},{"title":"Learning with Annotator Disagreement in STS","url":"https://aclanthology.org/2025.emnlp-main.1800.pdf"},{"title":"Handling Disagreement in Hate Speech Modelling | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-08974-9_54"},{"title":"Leveraging Annotator Disagreement for Text Classification","url":"https://arxiv.org/html/2409.17577v1"},{"title":"The Case for Ambiguity Detection in NLI","url":"https://aclanthology.org/2025.nlperspectives-1.4.pdf"}]

I found several relevant results for your search query on type-conditioned annotation disagreement resolution with soft labels in 2025. Here's a summary of what the search revealed:

## Key Research Areas

**Recent Work on Disagreement-Aware Evaluation (2025):**

STABLEVAL is a disagreement-aware evaluation framework that models latent item correctness and annotator-specific confusion patterns to compute posterior expected item credit and calibrated agent-level scores. Rather than treating disagreement as noise to suppress, this research argues that disagreement is signal to model, and that the central challenge in AI evaluation is not merely recovering a denoised label, but producing stable and uncertainty-aware system comparisons under realistic annotator variability.

**Soft Label Training and Epistemic Uncertainty:**

Soft-label predictions mirror the spread of human annotations, while hard-label predictions collapse to single peaks despite genuine annotator disagreement. On average, soft-label models show 61% stronger correlation with data entropy.

**Rubric-Conditioned Approaches:**

Recent research explores evaluating LLM-based labeling not only by concordance with human reference constructions, but also by whether the resulting supervision is stable and learnable, where hard labels correspond to learning a single decision rule, whereas soft labels provide a distributional supervisory signal that can retain ambiguity and disagreement.

**Methods for Handling Disagreement:**

Recent machine learning approaches include soft-label training, incorporating socio-demographic features for group perspective simulation, multi-task learning with each task corresponding to a specific annotator, and using an annotator embedding layer to learn annotator-specific labels.

These works represent the cutting edge of research on leveraging annotator disagreement as informative signal rather than noise.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05ed4316-e5ab-4925-89d9-bfa0ea16424e",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "7eba8fc3-3e26-4aa1-b642-e84c61567c6a",
  "sourceToolAssistantUUID": "05ed4316-e5ab-4925-89d9-bfa0ea16424e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T07:58:30.589Z_

Good initial results. Now let me fetch the most directly relevant papers and run more targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eba8fc3-3e26-4aa1-b642-e84c61567c6a",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXtWD3YhB2o3dtU3wVn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fbb2d1a0-da9d-4c64-9fd5-51af7f47af8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DppDUrxnrhWYuLfp5Mn65f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3008,
      "cache_read_input_tokens": 10824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3008,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-10T07:58:31.742Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016h8e7CgCTE1kpJD91toDmG`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-main.671.pdf",
  "prompt": "Extract the title, authors, venue, abstract, and key methods of this paper. Focus on how it classifies disagreement types and whether it uses probing or clarification questions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbb2d1a0-da9d-4c64-9fd5-51af7f47af8e",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXtWD3YhB2o3dtU3wVn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53d20aa7-c49a-4db3-ac0d-cec9e28fb622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DppDUrxnrhWYuLfp5Mn65f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3008,
      "cache_read_input_tokens": 10824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3008,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-10T07:58:32.504Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Go4ZWX6iNPDphgy9qtypBQ`</summary>

```json
{
  "query": "annotation disagreement \"clarification questions\" OR \"clarification probes\" active learning 2025 2026 NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53d20aa7-c49a-4db3-ac0d-cec9e28fb622",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXtWD3YhB2o3dtU3wVn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e2358f6-2998-4310-9872-e158c5534d53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DppDUrxnrhWYuLfp5Mn65f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3008,
      "cache_read_input_tokens": 10824,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3008,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-10T07:58:32.780Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R2ufxEkyAFksf6r5cRR5Zc`</summary>

```json
{
  "query": "\"borderline\" \"conceptual ambiguity\" annotation disagreement NLP 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e2358f6-2998-4310-9872-e158c5534d53",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXtWD3YhB2o3dtU3wVn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "703068ed-d3b9-4163-977e-6b3af638e358",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DppDUrxnrhWYuLfp5Mn65f",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3008,
      "cache_read_input_tokens": 10824,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3008
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 262,
          "cache_read_input_tokens": 10824,
          "cache_creation_input_tokens": 3008,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3008,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T07:58:37.359Z_

<details><summary>↩ Tool result · `toolu_016h8e7CgCTE1kpJD91toDmG`</summary>

```text
I appreciate your request, but I'm unable to extract the requested information from the provided content. The text appears to be a PDF file encoded in binary format containing compressed stream data, which makes it unreadable in plain text form.

To properly extract the title, authors, venue, abstract, and key methods from this academic paper, I would need:

1. A properly decoded or converted version of the PDF (such as plain text or HTML)
2. The actual document content rather than the raw PDF structure

**Recommendation:** Please provide either:
- A text version of the paper
- A link to the paper's abstract page
- The paper content in a readable format (HTML, markdown, or plain text)

Once you share the paper in a readable format, I'll be happy to extract the specific information about how the paper classifies disagreement types and whether it employs probing or clarification questions, while adhering to your character limits and quotation requirements.

[Binary content (application/pdf, 2.2MB) also saved to /home/ubuntu/.claude-account-1/projects/-/7ac167d0-b69c-4418-a1b0-da73321aa61d/tool-results/webfetch-1778399913712-rnlkjc.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53d20aa7-c49a-4db3-ac0d-cec9e28fb622",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "1d2fe0e0-597a-445b-b8e5-a0049a6707f4",
  "sourceToolAssistantUUID": "53d20aa7-c49a-4db3-ac0d-cec9e28fb622",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T07:58:39.990Z_

<details><summary>↩ Tool result · `toolu_01R2ufxEkyAFksf6r5cRR5Zc`</summary>

```text
Web search results for query: ""borderline" "conceptual ambiguity" annotation disagreement NLP 2024 2025"

Links: [{"title":"Navigating Disagreements in NLP Annotation","url":"https://aclanthology.org/2025.comedi-1.pdf"},{"title":"The Case for Ambiguity Detection in NLI","url":"https://aclanthology.org/2025.nlperspectives-1.4.pdf"},{"title":"Ambiguity and Disagreement in Abstract Meaning Representation - ACL Anthology","url":"https://aclanthology.org/2025.comedi-1.14/"},{"title":"Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP","url":"https://arxiv.org/html/2601.09065v1"},{"title":"Can Large Language Models Capture Human Annotator Disagreements? by Jingwei Ni, Yu Fan, Vilém Zouhar, Donya Rooein, Alexander Hoyle, Mrinmaya Sachan, Markus Leippold, Dirk Hovy, Elliott Ash :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/5319936.pdf?abstractid=5319936"},{"title":"Conflicts in Texts: Data, Implications and Challenges","url":"https://arxiv.org/html/2504.19472"},{"title":"Redirecting to BlackboxNLP 2025","url":"https://blackboxnlp.github.io/"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"[2506.19467] Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?","url":"https://arxiv.org/abs/2506.19467"},{"title":"(PDF) Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP","url":"https://www.researchgate.net/publication/399776954_Beyond_Consensus_Perspectivist_Modeling_and_Evaluation_of_Annotator_Disagreement_in_NLP"}]

Based on the search results, I found several relevant recent papers and resources on annotation disagreement, conceptual ambiguity, and NLP from 2024-2025:

## Key Findings

**Recent Workshop & Conference Coverage:**

A workshop on "Context and Meaning: Navigating Disagreements in NLP Annotation" is taking place for the first time and explores causes of disagreements in NLP annotations as well as strategies for effective handling or resolution. This workshop includes research on representing ambiguity in meaning representations, annotating implicit discourse relations, analyzing disagreement in politeness annotations, and predicting disagreement in tasks about word sense.

**Research on Ambiguity and Disagreement:**

A paper on "Ambiguity and Disagreement in Abstract Meaning Representation" quantifies the impact of ambiguity on AMR using disambiguating paraphrases at a larger scale, and compares this to the measurable impact of ambiguity in vector semantics.

**Sources of Disagreement:**

In NLP, disagreements arise from linguistic ambiguity, annotator backgrounds, task design, and dataset curation practices, with subjective ambiguity and annotator diversity identified as key contributors.

**LLM Performance on Disagreement:**

Human annotation variation (i.e., annotation disagreements) is common in NLP and often reflects important information such as task subjectivity and sample ambiguity. Recent findings show that LLMs struggle with modeling disagreements, which can be overlooked by majority label-based evaluations.

The search results indicate this is an active research area with multiple 2025 publications addressing these topics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "703068ed-d3b9-4163-977e-6b3af638e358",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "f6d88aa6-3252-4857-8ae7-b4f7f38dcaf0",
  "sourceToolAssistantUUID": "703068ed-d3b9-4163-977e-6b3af638e358",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T07:58:40.606Z_

<details><summary>↩ Tool result · `toolu_01Go4ZWX6iNPDphgy9qtypBQ`</summary>

```text
Web search results for query: "annotation disagreement "clarification questions" OR "clarification probes" active learning 2025 2026 NLP"

Links: [{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"Active Learning Machine Learning: How It Reduces Labeling Costs in 2026 | Label Your Data","url":"https://labelyourdata.com/articles/active-learning-machine-learning"},{"title":"Text Annotation Tool: A 2026 Guide for ML and NLP Teams | Label Your Data","url":"https://labelyourdata.com/articles/data-annotation/text-annotation-tool"},{"title":"Enhancing the Interpretability of NLI Models Using LLMs and Active Learning Algorithms","url":"https://www.mdpi.com/2078-2489/17/2/119"},{"title":"Navigating Disagreements in NLP Annotation","url":"https://aclanthology.org/2025.comedi-1.pdf"},{"title":"Can Large Language Models Capture Human Annotator Disagreements? by Jingwei Ni, Yu Fan, Vilém Zouhar, Donya Rooein, Alexander Hoyle, Mrinmaya Sachan, Markus Leippold, Dirk Hovy, Elliott Ash :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/5319936.pdf?abstractid=5319936"},{"title":"Active learning for data streams: a survey | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10994-023-06454-2"},{"title":"Reassessing Active Learning Adoption in Contemporary NLP","url":"https://aclanthology.org/2026.eacl-long.120.pdf"},{"title":"Annotator-Centric Active Learning for Subjective NLP Tasks","url":"https://aclanthology.org/2024.emnlp-main.1031.pdf"},{"title":"Active Learning in Machine Learning: Guide & Strategies [2025]","url":"https://encord.com/blog/active-learning-machine-learning-guide/"}]

I've completed the web search for your query about annotation disagreement, clarification questions/probes, active learning, and NLP research from 2025-2026. Here's a summary of the most relevant findings:

## Key Research Areas Found:

**Workshop and Conference Activity:**
A new workshop called CoMeDi is taking place for the first time and explores causes of disagreements in NLP annotations as well as strategies for effective handling or resolution.

**Recent Studies on Annotation Disagreement:**

Human annotation variation (i.e., annotation disagreements) is common in NLP and often reflects important information such as task subjectivity and sample ambiguity. While Large Language Models (LLMs) are increasingly used for automatic annotation to reduce human effort, their evaluation often focuses on predicting the majority-voted "ground truth" labels. It is still unclear whether these models also capture informative human annotation variation, which researchers are addressing by extensively evaluating LLMs' ability to predict annotation disagreements.

**Active Learning and Disagreement-Based Strategies:**

Disagreement-based query strategies focus on selecting data points where there is disagreement among multiple models or experts. Additionally, recent research includes work leveraging variation theory in counterfactual data augmentation for optimized active learning.

**Annotation Quality and Conflict Resolution:**

Text data annotation tools need built-in conflict resolution that surfaces disagreements before they poison the dataset. If tools just average confidence scores without flagging semantic conflicts, they are training models on low-quality data.

The search results indicate active research into handling annotation disagreement in NLP, though specific work focused on "clarification questions" or "clarification probes" within active learning wasn't prominently featured in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e2358f6-2998-4310-9872-e158c5534d53",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "e53ff3ae-8c15-4725-8dbf-ac62467a6d05",
  "sourceToolAssistantUUID": "0e2358f6-2998-4310-9872-e158c5534d53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-10T07:58:46.665Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PeZANDbnB72hiBaChKJRMh`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-main.671/",
  "prompt": "Extract the title, authors, venue/year, abstract, and key methods. Focus especially on how it classifies or taxonomizes disagreement, and any probing or clarification mechanisms."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e53ff3ae-8c15-4725-8dbf-ac62467a6d05",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXuQ8CoP86zbittnmW8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8a795a97-e8ee-493e-a7f6-8bee383aeda3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S1nXbEvVt7tGYPX6Cv7TxC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 958,
      "cache_creation_input_tokens": 1539,
      "cache_read_input_tokens": 13832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1539,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-10T07:58:48.884Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Q7jgoStU4bVV81N3bkYQmF`</summary>

```json
{
  "url": "https://aclanthology.org/2025.comedi-1.pdf",
  "prompt": "List all paper titles in this proceedings volume along with authors. I'm looking for papers about: disagreement typing/taxonomy, clarification probes, active annotation, soft labels, borderline cases, or value divergence."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a795a97-e8ee-493e-a7f6-8bee383aeda3",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXuQ8CoP86zbittnmW8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e6a64ec-1275-487a-841d-b582ea47dae2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S1nXbEvVt7tGYPX6Cv7TxC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 958,
      "cache_creation_input_tokens": 1539,
      "cache_read_input_tokens": 13832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1539,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-10T07:58:49.188Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dv5p33gKBUAkQpQhu16RAW`</summary>

```json
{
  "query": "EMNLP 2025 annotation disagreement resolution active learning probe generation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e6a64ec-1275-487a-841d-b582ea47dae2",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXuQ8CoP86zbittnmW8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33a9fd1b-4caf-4370-bb2c-c0a0a5b58cac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01S1nXbEvVt7tGYPX6Cv7TxC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 958,
      "cache_creation_input_tokens": 1539,
      "cache_read_input_tokens": 13832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1539,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T07:58:50.316Z_

<details><summary>↩ Tool result · `toolu_01PeZANDbnB72hiBaChKJRMh`</summary>

```text
# CARE: Disagreement Detection Framework

**Title:** CARE: A Disagreement Detection Framework with Concept Alignment and Reasoning Enhancement

**Authors:** Jiyuan Liu, Jielin Song, Yunhe Pang, Zhiyu Shen, Yanghui Rao

**Venue/Year:** EMNLP 2025 (November, Suzhou, China)

**Abstract Summary:**
The paper addresses disagreement detection in online discussions by tackling two limitations in LLM performance: conceptual gaps and reasoning gaps. The framework operates in two stages to improve model comprehension and inferential capability.

**Key Methods:**

1. **Concept Alignment Stage:** Performs "sub-concept taxonomy extraction" to align model understanding with expert knowledge, bridging the gap between how experts and models understand disagreement concepts.

2. **Reasoning Enhancement Stage:** Implements curriculum learning with two components:
   - "Rationale to critique" - generating explanatory reasoning
   - "Counterfactual to detection" - reducing spurious correlations through synthetic variations

**Performance:** The approach demonstrates effectiveness in both zero-shot and supervised settings, with consistent improvements across different domains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a795a97-e8ee-493e-a7f6-8bee383aeda3",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "d07f1af0-0fc0-4a0d-a9bc-ca2099ed2864",
  "sourceToolAssistantUUID": "8a795a97-e8ee-493e-a7f6-8bee383aeda3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T07:58:53.853Z_

<details><summary>↩ Tool result · `toolu_01Q7jgoStU4bVV81N3bkYQmF`</summary>

```text
I apologize, but I cannot provide the requested information. The content you've provided is a raw PDF file in binary/compressed format that contains embedded streams and objects rather than readable text. While I can see this is a proceedings document with multiple pages, the actual paper titles and author information are not accessible in a human-readable form within this data.

To help you find papers on disagreement typing, clarification probes, active annotation, soft labels, borderline cases, or value divergence, I would need:

1. A plain text version of the table of contents
2. An HTML or plain text rendering of the proceedings
3. A list of paper titles and authors in a structured format

If you can provide the proceedings in one of these alternative formats, I'd be happy to identify papers matching your research interests.

[Binary content (application/pdf, 2.7MB) also saved to /home/ubuntu/.claude-account-1/projects/-/7ac167d0-b69c-4418-a1b0-da73321aa61d/tool-results/webfetch-1778399930590-ncdgdq.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e6a64ec-1275-487a-841d-b582ea47dae2",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "c93cf8ab-9ab8-43a4-afbd-a45132cfa51f",
  "sourceToolAssistantUUID": "8e6a64ec-1275-487a-841d-b582ea47dae2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T07:58:57.102Z_

<details><summary>↩ Tool result · `toolu_01Dv5p33gKBUAkQpQhu16RAW`</summary>

```text
Web search results for query: "EMNLP 2025 annotation disagreement resolution active learning probe generation"

Links: [{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Eighteen papers by CSE researchers at EMNLP 2025","url":"https://cse.engin.umich.edu/stories/eighteen-papers-by-cse-researchers-at-emnlp-2025"},{"title":"LINGUIST List 36.1369 Confs: EMNLP Workshop: Perspectivist Approaches to NLP (China)","url":"https://linguistlist.org/issues/36/1369/"},{"title":"CARE: A Disagreement Detection Framework with Concept ...","url":"https://aclanthology.org/2025.emnlp-main.671.pdf"},{"title":"Learning with Annotator Disagreement in STS","url":"https://aclanthology.org/2025.emnlp-main.1800.pdf"},{"title":"EMNLP.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/EMNLP.2025"},{"title":"Empirical Methods in Natural Language Processing (EMNLP) 2025 - Apple Machine Learning Research","url":"https://machinelearning.apple.com/updates/apple-at-emnlp-2025"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"Debating for Better Reasoning in Vision-Language Models","url":"https://aclanthology.org/2025.findings-emnlp.853.pdf"},{"title":"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track - ACL Anthology","url":"https://aclanthology.org/volumes/2025.emnlp-industry/"}]

Based on the search results, I found relevant information about EMNLP 2025 papers. Here are the key findings related to your query:

## Annotation Disagreement Resolution

NUTMEG: Separating Signal From Noise in Annotator Disagreement by Jonathan Ivey, Susan Gauch, and David Jurgens is a notable paper at EMNLP 2025. NUTMEG is a new Bayesian model that incorporates information about annotator backgrounds to remove noisy annotations from human-labeled training data while preserving systematic disagreements. Using synthetic and real-world data, NUTMEG is more effective at recovering ground-truth from annotations with systematic disagreement than traditional aggregation methods, and downstream models trained on NUTMEG-aggregated data significantly outperform models trained on data from traditional aggregation methods.

## Related Work on Disagreement

There is also work titled "When Annotators Disagree, Topology Explains: Mapper, a Topological Tool for Exploring Text Embedding Geometry and Ambiguity" by Nisrine Rair, Alban Goupil, Valeriu Vrabie, and Emmanuel Chochoy.

## Workshop on Disagreement

The NLPerspectives workshop hosts the new edition of Learning with Disagreement (Le-Wi-Di) shared task, which explores new approaches to modeling and evaluation of Perspectivist benchmarks, challenging participants to leverage both instance-level disagreement and annotator-level information in classification.

The search results did not reveal specific papers combining all elements of annotation disagreement resolution, active learning, and probe generation together at EMNLP 2025. The most directly relevant work appears to be NUTMEG for disagreement resolution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33a9fd1b-4caf-4370-bb2c-c0a0a5b58cac",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "50d851dd-5b9a-47f3-998c-8617064bdd74",
  "sourceToolAssistantUUID": "33a9fd1b-4caf-4370-bb2c-c0a0a5b58cac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-10T07:59:00.676Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EP5JW1HVYUK4aRYhDAVkVM`</summary>

```json
{
  "url": "https://aclanthology.org/2025.comedi-1/",
  "prompt": "List all paper titles and authors in this proceedings volume. I am looking for papers about disagreement typing/taxonomy, active annotation, clarification probes or questions, soft labels, borderline cases, value divergence, or probe generation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50d851dd-5b9a-47f3-998c-8617064bdd74",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXvcQunziJPcnsfRhBP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8095fdbf-6f82-42fe-b1b1-69d98483e826",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01H8TnYrbEfR1gaAjnugRNzJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2875,
      "cache_read_input_tokens": 15371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2875,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-10T07:59:01.874Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CXdeYsvFEjhEKyM7g23Ci8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.09065",
  "prompt": "Extract the title, authors, year/venue, abstract, and key methods. Does this paper classify types of annotation disagreement? Does it involve probing annotators or generating clarification questions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8095fdbf-6f82-42fe-b1b1-69d98483e826",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXvcQunziJPcnsfRhBP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8bfc7f4c-7b27-4419-967d-28223b5ff143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01H8TnYrbEfR1gaAjnugRNzJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2875,
      "cache_read_input_tokens": 15371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2875,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-10T07:59:02.436Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DXVChWEToNd5EDVNrRm2KL`</summary>

```json
{
  "query": "ACL 2025 annotation disagreement types ambiguity value divergence soft label probe"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bfc7f4c-7b27-4419-967d-28223b5ff143",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXvcQunziJPcnsfRhBP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9ddd075-86b4-4a65-9303-c7cbfa954ed7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01H8TnYrbEfR1gaAjnugRNzJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2875,
      "cache_read_input_tokens": 15371,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2875
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 289,
          "cache_read_input_tokens": 15371,
          "cache_creation_input_tokens": 2875,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2875,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-10T07:59:05.569Z_

<details><summary>↩ Tool result · `toolu_01CXdeYsvFEjhEKyM7g23Ci8`</summary>

```text
# Paper Summary

**Title:** Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP

**Authors:** Yinuo Xu, David Jurgens

**Year/Venue:** arXiv:2601.09065 (submitted January 14, 2026; revised January 17, 2026)

**Abstract:** The work surveys disagreement-aware NLP methods, presenting "a domain-agnostic taxonomy of the sources of disagreement spanning data, task, and annotator factors." It synthesizes modeling approaches and evaluation metrics, noting a shift from treating disagreement as noise toward explicitly capturing it as meaningful signal reflecting interpretation variation.

## Classification of Disagreement Types

**Yes.** The paper presents a taxonomy categorizing disagreement sources across three dimensions: data factors, task factors, and annotator factors.

## Annotator Probing or Clarification Questions

**No evidence provided.** The abstract and page content do not indicate whether the paper involves directly probing annotators or generating clarification questions. The material focuses on surveying existing methods for modeling disagreement rather than describing novel data collection techniques.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bfc7f4c-7b27-4419-967d-28223b5ff143",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "7451cbbb-7b34-41ad-ac2f-a5c3ea5de96b",
  "sourceToolAssistantUUID": "8bfc7f4c-7b27-4419-967d-28223b5ff143",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T07:59:05.710Z_

<details><summary>↩ Tool result · `toolu_01EP5JW1HVYUK4aRYhDAVkVM`</summary>

```text
# Papers on Disagreement, Annotation Methods, and Related Topics

Based on the proceedings content, here are papers matching your interests:

## Direct Matches

**"Ambiguity and Disagreement in Abstract Meaning Representation"** by Shira Wein
- Examines ambiguity types affecting AMR annotation and their measurable impact on parser performance.

**"Disagreement in Metaphor Annotation of Mexican Spanish Science Tweets"** by Alec Sánchez-Montero, Gemma Bel-Enguix, Sergio-Luis Ojeda-Trueba, and Gerardo Sierra
- Studies inter-annotator disagreement in figurative language detection, proposing adoption of "a learning-from-disagreement approach for capturing diverse annotation perspectives."

**"Sources of Disagreement in Data for LLM Instruction Tuning"** by Russel Dsouza and Venelin Kovatchev
- Investigates whether disagreement stems from data points, annotators, or task design by comparing conditions with different formats.

**"On Crowdsourcing Task Design for Discourse Relation Annotation"** by Frances Yung and Vera Demberg
- Compares annotation methodologies (free-choice versus forced-choice) and their impact on annotation diversity.

## Potentially Relevant Papers

**"Is a bunch of words enough to detect disagreement in hateful content?"** by Giulia Rizzi, Paolo Rosso, and Elisabetta Fersini
- Addresses detecting ambiguous textual constituents that cause disagreement in content classification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8095fdbf-6f82-42fe-b1b1-69d98483e826",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "c81d82b2-c525-4a82-b537-b0da67a4beb7",
  "sourceToolAssistantUUID": "8095fdbf-6f82-42fe-b1b1-69d98483e826",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T07:59:10.473Z_

<details><summary>↩ Tool result · `toolu_01DXVChWEToNd5EDVNrRm2KL`</summary>

```text
Web search results for query: "ACL 2025 annotation disagreement types ambiguity value divergence soft label probe"

Links: [{"title":"Predicting Median, Disagreement and Noise Label in Ordinal Word-in-Context Data - ACL Anthology","url":"https://aclanthology.org/2025.comedi-1.6/"},{"title":"The Case for Ambiguity Detection in NLI","url":"https://aclanthology.org/2025.nlperspectives-1.4.pdf"},{"title":"Learning with Annotator Disagreement in STS","url":"https://aclanthology.org/2025.emnlp-main.1800.pdf"},{"title":"Ambiguity and Disagreement in Abstract Meaning Representation - ACL Anthology","url":"https://aclanthology.org/2025.comedi-1.14/"},{"title":"Measuring Label Ambiguity in Subjective Tasks using ...","url":"https://aclanthology.org/2025.law-1.2.pdf"},{"title":"Sources of Disagreement in Data for LLM Instruction Tuning - ACL Anthology","url":"https://aclanthology.org/2025.comedi-1.3/"},{"title":"COLING 2025 Proceedings of CoMeDi: Context and Meaning—Navigating","url":"https://aclanthology.org/2025.comedi-1.pdf"},{"title":"Consistency is Key: Disentangling Label Variation in ...","url":"https://aclanthology.org/2025.nlperspectives-1.6.pdf"},{"title":"Your Model is Overconfident, and Other Lies We Tell ...","url":"https://aclanthology.org/2025.acl-long.269.pdf"},{"title":"Leveraging Annotator Disagreement via Soft-Label Multi- ...","url":"https://aclanthology.org/2021.naacl-main.204.pdf"}]

I've completed a web search for your query. Here are the key findings related to ACL 2025 research on annotation disagreement, ambiguity, value divergence, soft labels, and probe techniques:

## Key Research Areas Found

**Annotation Disagreement and Ambiguity:**

The CoMeDi workshop at ACL 2025 explores causes of disagreements in NLP annotations as well as strategies for handling or resolution, including research on representing ambiguity in meaning representations and analyzing disagreement in tasks about word sense.

Research examines the role of ambiguity in AMR graph structure by employing a taxonomy of ambiguity types and producing AMRs affected by each type.

**Disagreement Sources:**

One study found there are very few "universally ambiguous" instances, and that label disagreement depends largely on task formulation and the choice of annotators, with changes in task formulation and annotators impacting resulting instance-level labels.

**Soft Labels and Training:**

Soft-label training plus distance-aware temperature scaling (Soft-Cal) yields the best overall calibration and lowest average RMSE on semantic textual similarity tasks.

**Shared Task:**

The CoMeDi shared task included subtasks where participants predicted the median of annotator judgments and the mean of pairwise absolute judgment differences between annotators.

The search results show active research at ACL 2025 addressing how to model, predict, and leverage annotator disagreement in NLP annotation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9ddd075-86b4-4a65-9303-c7cbfa954ed7",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "88d9e72e-0efe-4e95-afd3-ad4703e2286b",
  "sourceToolAssistantUUID": "e9ddd075-86b4-4a65-9303-c7cbfa954ed7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-10T07:59:13.415Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BT54ukCaDsCw6mzeSdetNm`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-main.1800/",
  "prompt": "Extract title, authors, abstract, and key methods. Does this paper classify types of disagreement? Does it involve probing annotators, generating clarification questions, or updating soft labels based on annotator responses?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88d9e72e-0efe-4e95-afd3-ad4703e2286b",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXwbcKKcC6qx5wBrtHS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60a6d176-cb26-414c-8b3c-1899789a3335",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ce67DpqLCcvYeYHd2vhrtg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1814,
      "cache_read_input_tokens": 18246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1814,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-10T07:59:14.573Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014GxvPsa5RN3Sv3uMxwiyH9`</summary>

```json
{
  "url": "https://aclanthology.org/2024.emnlp-main.1031/",
  "prompt": "Extract title, authors, venue, abstract, and key methods. Focus on: does this paper classify types of disagreement, use probes or clarification questions, do active learning with disagreement, or update soft labels?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60a6d176-cb26-414c-8b3c-1899789a3335",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXwbcKKcC6qx5wBrtHS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a1cd111-6900-4c68-bda3-cfdb788517d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ce67DpqLCcvYeYHd2vhrtg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1814,
      "cache_read_input_tokens": 18246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1814,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-10T07:59:15.112Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Nog6RCfP5goS6nMkek3rD`</summary>

```json
{
  "query": "arXiv 2025 2026 annotation disagreement \"probe\" OR \"probing\" \"soft label\" active learning clarification NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a1cd111-6900-4c68-bda3-cfdb788517d0",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXwbcKKcC6qx5wBrtHS",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6833870d-2fa6-4ee3-97d7-48148c70b540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ce67DpqLCcvYeYHd2vhrtg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1814,
      "cache_read_input_tokens": 18246,
      "output_tokens": 316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1814
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 316,
          "cache_read_input_tokens": 18246,
          "cache_creation_input_tokens": 1814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1814,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-10T07:59:16.964Z_

<details><summary>↩ Tool result · `toolu_01BT54ukCaDsCw6mzeSdetNm`</summary>

```text
# Paper Summary

**Title:** "Beyond Averages: Learning with Annotator Disagreement in STS"

**Authors:** Alejandro Benito-Santos, Adrian Ghajari

**Abstract:** The work addresses disagreement in Semantic Textual Similarity by treating it as "an ordinal distribution prediction problem" rather than averaging scores. Two strategies are proposed: a truncated Gaussian head for regression models and a calibrated cross-encoder with temperature scaling.

## Key Methods

The paper employs two main approaches:
1. A lightweight truncated Gaussian head for standard regression
2. A distance-aware cross-encoder refined with temperature scaling

## Classification & Engagement Questions

**No**, this paper does not classify types of disagreement or involve annotator engagement. It focuses solely on modeling disagreement distributions rather than understanding disagreement sources or generating clarification questions. The approach treats disagreement as label dispersion to preserve through probabilistic prediction, not as something requiring annotator interaction or probing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60a6d176-cb26-414c-8b3c-1899789a3335",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "94bd9752-4d5e-4839-ba12-1c7d2e1421e9",
  "sourceToolAssistantUUID": "60a6d176-cb26-414c-8b3c-1899789a3335",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-10T07:59:18.084Z_

<details><summary>↩ Tool result · `toolu_014GxvPsa5RN3Sv3uMxwiyH9`</summary>

```text
# Paper Analysis: Annotator-Centric Active Learning for Subjective NLP Tasks

**Title:** Annotator-Centric Active Learning for Subjective NLP Tasks

**Authors:** Michiel van der Meer, Neele Falk, Pradeep K. Murukannaiah, Enrico Liscio

**Venue:** EMNLP 2024 (Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing)

**Abstract Summary:**
The paper addresses annotation costs by proposing ACAL, which combines data sampling with annotator selection. Key objectives include capturing diversity in human judgments and using metrics that treat minority and majority perspectives equally across seven subjective NLP tasks.

## Key Methods Assessment:

**Disagreement Classification:** Not mentioned in the abstract or metadata.

**Probes/Clarification Questions:** Not indicated in provided content.

**Active Learning with Disagreement:** Yes—ACAL incorporates "an annotator selection strategy following data sampling" to capture "the variability in human judgments" and improve "data efficiency."

**Soft Label Updates:** Not explicitly discussed in the available materials.

**Primary Innovation:** The approach uniquely combines active learning's sample selection with strategic annotator selection, employing "annotator-centric metrics, which value minority and majority perspectives equally" rather than traditional consensus-based evaluation methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a1cd111-6900-4c68-bda3-cfdb788517d0",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "cc7dd3df-89af-4c71-b94c-92547dee17f8",
  "sourceToolAssistantUUID": "1a1cd111-6900-4c68-bda3-cfdb788517d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-10T07:59:24.335Z_

<details><summary>↩ Tool result · `toolu_011Nog6RCfP5goS6nMkek3rD`</summary>

```text
Web search results for query: "arXiv 2025 2026 annotation disagreement "probe" OR "probing" "soft label" active learning clarification NLP"

Links: [{"title":"Do We Still Need Humans in the Loop? Comparing Human and LLM Annotation in Active Learning for Hostility Detection","url":"https://arxiv.org/html/2604.13899"},{"title":"STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems","url":"https://arxiv.org/html/2605.02122v1"},{"title":"Revisiting Active Learning under (Human) Label Variation","url":"https://arxiv.org/pdf/2507.02593"},{"title":"[2507.02593] Revisiting Active Learning under (Human) Label Variation","url":"https://arxiv.org/abs/2507.02593"},{"title":"Enhancing Text Classification through LLM-Driven Active Learning and Human Annotation","url":"https://arxiv.org/html/2406.12114v1"},{"title":"Active Learning Machine Learning: How It Reduces Labeling Costs in 2026 | Label Your Data","url":"https://labelyourdata.com/articles/active-learning-machine-learning"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"[2406.12114] Enhancing Text Classification through LLM-Driven Active Learning and Human Annotation","url":"https://arxiv.org/abs/2406.12114"},{"title":"A Survey on Large Language Model Benchmarks","url":"https://arxiv.org/html/2508.15361v1"},{"title":"[2406.12114v1] Enhancing Text Classification through LLM-Driven Active Learning and Human Annotation","url":"https://arxiv.org/abs/2406.12114v1"}]

I've completed the web search for your query. Here are the relevant results I found:

## Key Papers Found

**1. STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems (2025)**
This paper clarifies the distinction between label denoising and evaluation stability, showing that recovering latent labels does not guarantee robust system rankings. There is growing interest in treating annotator disagreement as a meaningful signal rather than noise, with surveys highlighting the need to model structured disagreement, especially for subjective tasks like toxicity detection and stance annotation.

**2. Revisiting Active Learning under (Human) Label Variation (2025)**
While label variation is common in natural language processing, annotation frameworks often still rest on the assumption of a single ground truth, overlooking human label variation (HLV), the occurrence of plausible differences in annotations, as an informative signal.

**3. Do We Still Need Humans in the Loop? (2025)**
This paper compares human and LLM annotation in active learning for hostility detection and discusses recent work on whether large language models can capture human annotator disagreements, finding that models often fail to model disagreement patterns, particularly on tasks requiring emotional intelligence or contextual understanding.

**4. Soft Labels and Uncertainty**
Large-scale empirical studies show that aggregating soft labels from crowd annotations improves uncertainty estimation compared to hard majority labels.

These papers address your search terms around annotation disagreement, active learning, soft labels, and probing approaches in NLP for 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6833870d-2fa6-4ee3-97d7-48148c70b540",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "ed95d1db-0f5d-4776-ada7-4a7e3a6acfa9",
  "sourceToolAssistantUUID": "6833870d-2fa6-4ee3-97d7-48148c70b540",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-10T07:59:26.846Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Vi5eThDLMhLnNUTk1SKXii`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.02593",
  "prompt": "Extract the full title, authors, abstract, and key methods. Does this paper classify types of disagreement? Does it involve probing annotators, generating clarification questions, or doing type-conditioned resolution of disagreements?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed95d1db-0f5d-4776-ada7-4a7e3a6acfa9",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXxcsVyh5Sd4HWRJZMr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e619857f-b0bd-491f-80eb-3c661bfabfbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SjnNHaXTjhFeSm9JiUpg7V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1739,
      "cache_read_input_tokens": 20060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1739,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-10T07:59:27.811Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VQQqiC5Apm1vXQYMAvKbpQ`</summary>

```json
{
  "query": "\"annotation disagreement\" \"taxonomy\" \"value\" \"ambiguity\" NLP paper 2025 2026 ACL EMNLP EACL arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e619857f-b0bd-491f-80eb-3c661bfabfbe",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXxcsVyh5Sd4HWRJZMr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0597000-6a9e-4534-99ad-390d79cc3e3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SjnNHaXTjhFeSm9JiUpg7V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1739,
      "cache_read_input_tokens": 20060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1739,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-10T07:59:27.990Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AYqrEZaRw6arW4wjVUD9xt`</summary>

```json
{
  "query": "EACL 2026 annotation disagreement typing resolution active learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0597000-6a9e-4534-99ad-390d79cc3e3b",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXxcsVyh5Sd4HWRJZMr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f8b40ee-8d8c-48de-952a-c8dd67a17ead",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SjnNHaXTjhFeSm9JiUpg7V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1739,
      "cache_read_input_tokens": 20060,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1739
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 251,
          "cache_read_input_tokens": 20060,
          "cache_creation_input_tokens": 1739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1739,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T07:59:31.834Z_

<details><summary>↩ Tool result · `toolu_01Vi5eThDLMhLnNUTk1SKXii`</summary>

```text
# Paper Summary

**Full Title:** "Revisiting Active Learning under (Human) Label Variation"

**Authors:** Cornelia Gruber, Helen Alber, Bernd Bischl, Göran Kauermann, Barbara Plank, Matthias Aßenmacher

**Abstract:** The paper addresses how supervised learning systems can better leverage high-quality labeled data. It emphasizes that "label variation (LV), i.e., differing labels for the same instance, is common, especially in natural language processing." The work examines how to distinguish human label variation (plausible annotation differences) from noise, proposing a framework for incorporating HLV throughout active learning workflows.

**Key Methods:** The paper proposes a conceptual framework addressing:
- Instance selection strategies
- Annotator selection
- Label representation approaches
- Integration of large language models as annotators

**Classification of Disagreement Types:** The paper does conceptually decompose observed label variation into "signal (e.g., HLV) and noise (e.g., annotation error)," distinguishing between legitimate human disagreement and annotation errors.

**Probing/Clarification/Conditional Resolution:** The provided content does not detail whether the paper includes probing annotators, generating clarification questions, or employing type-conditioned disagreement resolution. These specifics would require examining the full paper text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e619857f-b0bd-491f-80eb-3c661bfabfbe",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "a779fa78-a431-48d1-82e6-b129894fe8cf",
  "sourceToolAssistantUUID": "e619857f-b0bd-491f-80eb-3c661bfabfbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T07:59:37.823Z_

<details><summary>↩ Tool result · `toolu_01VQQqiC5Apm1vXQYMAvKbpQ`</summary>

```text
Web search results for query: ""annotation disagreement" "taxonomy" "value" "ambiguity" NLP paper 2025 2026 ACL EMNLP EACL arXiv"

Links: [{"title":"Ambiguity and Disagreement in Abstract Meaning Representation - ACL Anthology","url":"https://aclanthology.org/2025.comedi-1.14/"},{"title":"The Case for Ambiguity Detection in NLI","url":"https://aclanthology.org/2025.nlperspectives-1.4.pdf"},{"title":"[2506.19467] Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?","url":"https://arxiv.org/abs/2506.19467"},{"title":"Navigating Disagreements in NLP Annotation","url":"https://aclanthology.org/2025.comedi-1.pdf"},{"title":"Conflicts in Texts: Data, Implications and Challenges","url":"https://arxiv.org/html/2504.19472"},{"title":"From Disagreement to Understanding: The Case for Ambiguity Detection in NLI - ACL Anthology","url":"https://aclanthology.org/2025.nlperspectives-1.4/"},{"title":"Will Annotators Disagree? Identifying Subjectivity in Value- ...","url":"https://aclanthology.org/2025.findings-emnlp.824.pdf"},{"title":"Beyond Black-Box Labels: Interpretable Criteria for Diagnosing Subjective NLP Tasks","url":"https://arxiv.org/html/2604.17022v1"},{"title":"Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP","url":"https://arxiv.org/html/2601.09065"},{"title":"Can Large Language Models Capture Human Annotator Disagreements? by Jingwei Ni, Yu Fan, Vilém Zouhar, Donya Rooein, Alexander Hoyle, Mrinmaya Sachan, Markus Leippold, Dirk Hovy, Elliott Ash :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/5319936.pdf?abstractid=5319936"}]

Great! I found several highly relevant papers on annotation disagreement, taxonomy, and ambiguity in NLP from 2025-2026. Here's a summary of the key results:

## Key Papers Found:

**1. Ambiguity and Disagreement in Abstract Meaning Representation (2025)**
This paper examines the role of ambiguity in AMR graph structure by employing a taxonomy of ambiguity types, investigating to what extent and in what ways ambiguity affects AMR graphs and causes disagreement in AMR annotation. Published in the CoMeDi 2025 workshop.

**2. From Disagreement to Understanding: The Case for Ambiguity Detection in NLI (2025)**
This paper calls for a shift toward ambiguity-aware NLI that first identifies ambiguous input pairs, classifies their types, and presents a unified taxonomy that synthesizes existing taxonomies and illustrates key subtypes with examples. Published in NLPerspectives 2025.

**3. Will Annotators Disagree? Identifying Subjectivity in Value-... (2025)**
This EMNLP 2025 findings paper addresses identifying subjectivity in value-related annotations.

**4. Can Reasoning Help Large Language Models Capture Human Annotator Disagreement? (2025-2026)**
This arXiv paper examines variation in human annotation (disagreements), noting that they are common in NLP and often reflect important information like task subjectivity and sample ambiguity. Latest version from January 2026.

**5. Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP (2026)**
This survey presents a domain-agnostic taxonomy of the sources of disagreement spanning data, task, and annotator factors, and synthesizes modeling approaches using a common framework, highlighting a shift from consensus learning toward explicitly modeling disagreement.

**6. Beyond Black-Box Labels: Interpretable Criteria for Diagnosing Subjective NLP Tasks (2025)**
This paper distinguishes sources of disagreement: specification gaps where criteria underspecify expert intent, forcing annotators to implicitly supply missing decision policies; and cases where criteria are individually crisp but multiple simultaneously valid persuasive dimensions lack explicit resolution rules.

**7. Conflicts in Texts: Data, Implications and Challenges (2026)**
This paper notes that in NLP, disagreements arise from linguistic ambiguity, annotator backgrounds, task design, and dataset curation practices, and categorizes disagreements into inherent ambiguity, annotation errors, or contextual gaps, as well as linguistic uncertainty, annotator bias, and task design.

These papers represent current research from major NLP conferences (ACL, EMNLP) and workshops focusing specifically on the relationship between annotation disagreement, ambiguity, taxonomies, and value-related judgments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0597000-6a9e-4534-99ad-390d79cc3e3b",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "7214e1e6-245b-4d2c-a187-f109b3e66ffa",
  "sourceToolAssistantUUID": "f0597000-6a9e-4534-99ad-390d79cc3e3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-10T07:59:39.360Z_

<details><summary>↩ Tool result · `toolu_01AYqrEZaRw6arW4wjVUD9xt`</summary>

```text
Web search results for query: "EACL 2026 annotation disagreement typing resolution active learning"

Links: [{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"},{"title":"Findings Accepted Papers -","url":"https://2026.eacl.org/program/findings-accepted/"},{"title":"Student Research Workshop (SRW) Accepted Papers -","url":"https://2026.eacl.org/program/srw-accepted/"},{"title":"Can Reasoning Help Large Language Models Capture Human Annotator Disagreement? - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.3/"},{"title":"Language Model-Driven Data Pruning Enables Efficient Active Learning - ACL Anthology","url":"https://aclanthology.org/2026.findings-eacl.229/"},{"title":"Call for System Demonstrations -","url":"https://2026.eacl.org/calls/demos/"},{"title":"an annotation tool based on active and proactive learning","url":"https://aclanthology.org/2021.eacl-demos.28.pdf"},{"title":"EACL 2026 | OpenReview","url":"https://openreview.net/group?id=eacl.org/EACL/2026"},{"title":"Aggregating Crowd of LLMs for Cost-Effective Data ...","url":"https://aclanthology.org/2026.findings-eacl.125.pdf"},{"title":"Conference Overview -","url":"https://2026.eacl.org/program/"}]

Based on the search results, I found several relevant papers at EACL 2026 related to your query about annotation disagreement, active learning, and related topics:

## Key Papers Found:

**Annotation Disagreement:**
A main conference paper titled "Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?" explores whether reasoning enables LLMs to capture informative variation in human annotation and evaluates the influence of different reasoning settings on LLM disagreement modeling.

**Active Learning:**
A Student Research Workshop paper on "Active Learning for Corpus Refinement: Cost-Effective Preprocessing to Improve Validity of Applied Quantitative Text Analysis" was accepted to EACL 2026.

Additionally, a Findings paper titled "Language Model-Driven Data Pruning Enables Efficient Active Learning" addresses how active learning optimizes data labeling efficiency by selecting the most informative instances for annotation. The paper presents ActivePrune, which uses a two-stage pruning process and includes a novel perplexity reweighting method to enhance diversity in the unlabeled pool.

**Data Annotation:**
A Findings paper on "Aggregating Crowd of LLMs for Cost-Effective Data Annotation" was also accepted.

These papers collectively address aspects of annotation disagreement, active learning strategies, and efficient data annotation approaches presented at EACL 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f8b40ee-8d8c-48de-952a-c8dd67a17ead",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "2bc8abaf-d73b-4e71-add0-18d273c7b886",
  "sourceToolAssistantUUID": "8f8b40ee-8d8c-48de-952a-c8dd67a17ead",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-10T07:59:42.400Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016WUdZLgf4yg4kd773dLQUc`</summary>

```json
{
  "url": "https://aclanthology.org/2026.eacl-long.3/",
  "prompt": "Extract title, authors, abstract, and key methods. Does this paper classify types of annotation disagreement? Does it involve probing annotators or generating clarification questions? What is novel about it?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bc8abaf-d73b-4e71-add0-18d273c7b886",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXyj7KgiQAbPP3g28Qq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "32d835e1-06fd-4613-b270-49f36ae1d0dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LRrwD3hENxuYpwuuCuRdPN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2585,
      "cache_read_input_tokens": 21799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2585,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-10T07:59:43.865Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JbDvmDPY6432TjNuree3g1`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.17022",
  "prompt": "Extract full title, authors, year/venue, abstract, and key methods. This seems to be about interpretable criteria for subjective NLP tasks - does it classify types of disagreement, use probes or clarification questions, or generate type-specific questions for annotators?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32d835e1-06fd-4613-b270-49f36ae1d0dc",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXyj7KgiQAbPP3g28Qq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9962f1a9-e571-4975-b127-ed868bb4e861",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LRrwD3hENxuYpwuuCuRdPN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2585,
      "cache_read_input_tokens": 21799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2585,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-10T07:59:44.354Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HZxisic764YeAWDKFrRnZQ`</summary>

```json
{
  "query": "arXiv 2025 2026 \"disagree\" OR \"disagreement\" \"clarification\" OR \"probing\" annotation labeling NLP active"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9962f1a9-e571-4975-b127-ed868bb4e861",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXyj7KgiQAbPP3g28Qq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3d0e2690-9feb-43d8-a21c-974a7ae3b83c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LRrwD3hENxuYpwuuCuRdPN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2585,
      "cache_read_input_tokens": 21799,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2585
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 318,
          "cache_read_input_tokens": 21799,
          "cache_creation_input_tokens": 2585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2585,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-10T07:59:46.456Z_

<details><summary>↩ Tool result · `toolu_016WUdZLgf4yg4kd773dLQUc`</summary>

```text
# Paper Summary

**Title:** "Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?"

**Authors:** Jingwei Ni, Yu Fan, Vilém Zouhar, Donya Rooein, Alexander Miserlis Hoyle, Mrinmaya Sachan, Markus Leippold, Dirk Hovy, Elliott Ash

**Abstract:** The paper investigates whether different reasoning approaches help LLMs model "variation in human annotation (i.e., disagreements)" which reflects "task subjectivity and sample ambiguity." The researchers test 60 experimental configurations across 3 tasks, varying model sizes, distribution expression methods, and steering approaches.

## Key Findings

**Methods Evaluated:**
- RLVR-style reasoning (Reinforcement Learning with Verifiable Rewards)
- Chain-of-Thought (CoT) reasoning
- RLHF LLMs (Reinforcement Learning from Human Feedback)

**Main Discovery:** Surprisingly, "RLVR-style reasoning degrades performance in disagreement modeling, while naive Chain-of-Thought (CoT) reasoning improves the performance of RLHF LLMs."

## Notable Aspects

**Does not classify disagreement types:** The paper focuses on modeling disagreement variation rather than categorizing different types of annotator disagreement.

**No annotator probing or clarification questions:** This is an empirical study evaluating existing reasoning techniques, not generating clarification questions or directly interviewing annotators.

**Novel contribution:** The counterintuitive finding that advanced reasoning techniques harm disagreement modeling represents the paper's primary novelty, challenging assumptions about reasoning-enhanced LLMs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32d835e1-06fd-4613-b270-49f36ae1d0dc",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "19797fb2-de38-4408-b498-17b9bd716e27",
  "sourceToolAssistantUUID": "32d835e1-06fd-4613-b270-49f36ae1d0dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-10T07:59:48.314Z_

<details><summary>↩ Tool result · `toolu_01JbDvmDPY6432TjNuree3g1`</summary>

```text
# Paper Summary

**Full Title:** Beyond Black-Box Labels: Interpretable Criteria for Diagnosing Subjective NLP Tasks

**Authors:** Nisrine Rair, Alban Goupil, Valeriu Vrabie, Emmanuel Chochoy

**Venue/Year:** ACL Findings 2026

**Abstract:** The researchers address how subjective NLP datasets handle annotator disagreement. Rather than immediately committing to gold labels, they propose "a schema-level diagnostic for auditing expert-designed annotation schemas" using multi-annotator criterion judgments. Their approach distinguishes between two failure modes: unstable criteria with unclear boundaries and systematic overlap between categories. Applied to persuasive value extraction in commercial documents, they identify that "disagreement is not diffuse: instability concentrates in a few criteria, while nearly half of covered sentences activate multiple categories."

**Key Methods:** The diagnostic operates at the schema level *before* gold-label creation, examining criterion-level judgments across multiple annotators rather than treating disagreement as monolithic. This framework identifies specific problematic criteria and category overlaps rather than just measuring overall agreement rates, providing actionable guidance for refining annotation guidelines or restructuring categories.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9962f1a9-e571-4975-b127-ed868bb4e861",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "1fdf3e43-cb28-45b8-a346-ac56ec0a5f35",
  "sourceToolAssistantUUID": "9962f1a9-e571-4975-b127-ed868bb4e861",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-10T07:59:52.382Z_

<details><summary>↩ Tool result · `toolu_01HZxisic764YeAWDKFrRnZQ`</summary>

```text
Web search results for query: "arXiv 2025 2026 "disagree" OR "disagreement" "clarification" OR "probing" annotation labeling NLP active"

Links: [{"title":"STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems","url":"https://arxiv.org/html/2605.02122v1"},{"title":"Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP","url":"https://arxiv.org/html/2601.09065v1"},{"title":"Beyond Black-Box Labels: Interpretable Criteria for Diagnosing Subjective NLP Tasks","url":"https://arxiv.org/html/2604.17022v1"},{"title":"Dealing with Annotator Disagreement in Hate Speech Classification","url":"https://arxiv.org/html/2502.08266v2"},{"title":"DEALING WITH ANNOTATOR DISAGREEMENT IN HATE SPEECH CLASSIFICATION A PREPRINT","url":"https://arxiv.org/pdf/2502.08266"},{"title":"Counting on Consensus: Selecting the Right Inter-annotator Agreement Metric for NLP Annotation and Evaluation","url":"https://arxiv.org/html/2603.06865"},{"title":"How does Disagreement Help Generalization against Label Corruption?","url":"https://arxiv.org/pdf/1901.04215"},{"title":"Large Language Models in Argument Mining: A Survey","url":"https://arxiv.org/html/2506.16383v3"},{"title":"Do LLMs Adhere to Label Definitions? Examining Their ...","url":"https://aclanthology.org/2025.emnlp-main.1648.pdf"},{"title":"Are LLMs Better than Reported? Detecting Label Errors ...","url":"https://aclanthology.org/2025.emnlp-main.1360.pdf"}]

I've found several highly relevant arXiv papers from 2025-2026 that match your search query. Here are the key results:

## Main Findings:

1. **STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems** (arXiv 2605.02122, 5 days ago)
   - Clarifies the distinction between label denoising and evaluation stability, showing that recovering latent labels does not guarantee robust system rankings
   - Addresses annotator disagreement as a meaningful signal

2. **Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP** (arXiv 2601.09065, January 14, 2026)
   - Examines how annotation task design strongly shapes disagreement, and how interface design affects agreement through unclear guidelines and ambiguity surfacing
   - Covers perspectivist approaches to modeling disagreement

3. **Beyond Black-Box Labels: Interpretable Criteria for Diagnosing Subjective NLP Tasks** (arXiv 2604.17022, 3 weeks ago)
   - Addresses how subjective NLP datasets aggregate annotator judgments into single gold labels, and proposes a schema-level diagnostic for auditing expert-designed annotation schemas using multi-annotator criterion judgments

4. **Dealing with Annotator Disagreement in Hate Speech Classification** (arXiv 2502.08266, August 17, 2025)
   - Describes iteratively refining guidelines to resolve ambiguities by adding more examples and clarifying guidelines about ambiguous situations

5. **Counting on Consensus: Selecting the Right Inter-annotator Agreement Metric for NLP Annotation and Evaluation** (arXiv 2603.06865, April 1, 2026)
   - Comprehensive guide on inter-annotator agreement metrics across different NLP tasks

These papers collectively address disagreement, clarification strategies, and annotation practices in NLP from multiple perspectives.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d0e2690-9feb-43d8-a21c-974a7ae3b83c",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "d51d28d3-bd97-4468-8029-7586b7d055b5",
  "sourceToolAssistantUUID": "3d0e2690-9feb-43d8-a21c-974a7ae3b83c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-10T07:59:56.180Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014Tu4PrSmZVuSvanfCWLHV3`</summary>

```json
{
  "url": "https://aclanthology.org/2025.nlperspectives-1.4/",
  "prompt": "Extract title, authors, abstract, and key methods. This paper is about ambiguity detection in NLI - does it propose a taxonomy of ambiguity types? Does it distinguish between different causes of disagreement like conceptual ambiguity vs borderline cases? Does it involve probing annotators or generating clarification questions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d51d28d3-bd97-4468-8029-7586b7d055b5",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXzgoSdSe1yG5GBSk83",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8e8bf90-5d18-4c3e-b8be-5170aedfeec4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HbMwW4ef4s2KLngcdQYuAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2094,
      "cache_read_input_tokens": 24384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2094,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-10T07:59:57.117Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0122K6pLaKSQ9o5CdjVBAAGt`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.08266",
  "prompt": "Extract title, authors, abstract, and key methods. Does this paper classify types of annotation disagreement? Does it generate clarification probes or questions for annotators? Does it distinguish between value divergence, conceptual ambiguity, and borderline cases?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8e8bf90-5d18-4c3e-b8be-5170aedfeec4",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXzgoSdSe1yG5GBSk83",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f018fe8a-c2b4-4240-8486-e7ba190938f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HbMwW4ef4s2KLngcdQYuAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2094,
      "cache_read_input_tokens": 24384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2094,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-10T07:59:57.547Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UzKV1oEvBwYAdewLrqL75A`</summary>

```json
{
  "query": "\"annotation disagreement\" \"probe generation\" OR \"question generation\" \"resolve\" disagreement NLP 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f018fe8a-c2b4-4240-8486-e7ba190938f4",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatXzgoSdSe1yG5GBSk83",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0cece68a-8d96-4dea-8abc-12989494f1bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HbMwW4ef4s2KLngcdQYuAd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2094,
      "cache_read_input_tokens": 24384,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2094
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 336,
          "cache_read_input_tokens": 24384,
          "cache_creation_input_tokens": 2094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2094,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-10T08:00:00.241Z_

<details><summary>↩ Tool result · `toolu_014Tu4PrSmZVuSvanfCWLHV3`</summary>

```text
# Paper Summary: Ambiguity Detection in NLI

**Title:** From Disagreement to Understanding: The Case for Ambiguity Detection in NLI

**Authors:** Chathuri Jayaweera, Bonnie J. Dorr

**Key Finding:** This position paper argues that "annotation disagreement in Natural Language Inference (NLI) is not mere noise but often" signals meaningful variation from ambiguity rather than just annotator error.

## Does it propose a taxonomy?
Yes. The authors present "a unified taxonomy that synthesizes existing taxonomies, illustrates key subtypes with examples" to organize different ambiguity types systematically.

## Does it distinguish causes of disagreement?
The paper acknowledges multiple sources: underspecified guidelines, annotator behavior, and "content-based ambiguity provides a process-independent signal of divergent human perspectives." This suggests it recognizes both procedural factors and genuine semantic ambiguity as distinct causes.

## Does it involve annotator probing or clarification questions?
The abstract does not mention these approaches. Instead, it emphasizes developing "new annotated resources and exploring unsupervised approaches to ambiguity detection" as future work, suggesting the current position paper doesn't employ those methods.

**Publication:** 4th Workshop on Perspectivist Approaches to NLP, November 2025, Suzhou, China
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8e8bf90-5d18-4c3e-b8be-5170aedfeec4",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "0dd3a513-8e62-421c-a1db-e8eaccfabf30",
  "sourceToolAssistantUUID": "e8e8bf90-5d18-4c3e-b8be-5170aedfeec4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-10T08:00:05.578Z_

<details><summary>↩ Tool result · `toolu_01UzKV1oEvBwYAdewLrqL75A`</summary>

```text
Web search results for query: ""annotation disagreement" "probe generation" OR "question generation" "resolve" disagreement NLP 2025 2026"

Links: [{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Quantifying and Predicting Disagreement in Graded Human Ratings","url":"https://arxiv.org/html/2605.01168"},{"title":"Can Large Language Models Capture Human Annotator Disagreements? by Jingwei Ni, Yu Fan, Vilém Zouhar, Donya Rooein, Alexander Hoyle, Mrinmaya Sachan, Markus Leippold, Dirk Hovy, Elliott Ash :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/5319936.pdf?abstractid=5319936"},{"title":"Navigating Disagreements in NLP Annotation","url":"https://aclanthology.org/2025.comedi-1.pdf"},{"title":"Learning Who Disagrees: Demographic Importance Weighting for Modeling Annotator Distributions with DiADEM","url":"https://arxiv.org/html/2604.08425"},{"title":"[2506.19467] Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?","url":"https://arxiv.org/abs/2506.19467"},{"title":"Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP","url":"https://arxiv.org/html/2601.09065v1"},{"title":"GitHub - llm-as-a-judge/Awesome-LLM-as-a-judge · GitHub","url":"https://github.com/llm-as-a-judge/Awesome-LLM-as-a-judge"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Agreeing to Disagree: Annotating Offensive Language Datasets with Annotators' Disagreement | Request PDF","url":"https://www.researchgate.net/publication/354922371_Agreeing_to_Disagree_Annotating_Offensive_Language_Datasets_with_Annotators'_Disagreement"}]

Based on the search results, I found several relevant papers and resources about annotation disagreement in NLP from 2025-2026:

## Key Recent Work on Annotation Disagreement

**Recent Publications:**

1. NUTMEG: Separating Signal From Noise in Annotator Disagreement by Jonathan Ivey, Susan Gauch, and David Jurgens was accepted at EMNLP 2025.

2. A workshop titled "Navigating Disagreements in NLP Annotation" is taking place for the first time and explores causes of disagreements in NLP annotations as well as strategies for effective handling or resolution.

3. Recent literature on annotation variation focuses on analyzing human annotation and human interpretation variation, investigating types or causes of variation across annotators, disentangling noise from genuine disagreement, and analyzing cultural background influence.

**Modeling Approaches:**

Work addresses the gap by extensively evaluating LLMs' ability to predict annotation disagreements without access to repeated human labels, with results showing that LLMs struggle with modeling disagreements, which can be overlooked by majority label-based evaluations.

The LeWiDi shared task series (Leonardelli et al., 2026) requires systems to predict soft label distributions over annotators, simulate individual annotator responses, and remain faithful to item-level disagreement patterns.

**Methods for Resolution:**

Research includes representing ambiguity in meaning representations, annotating implicit discourse relations, analyzing disagreement in politeness annotations, and predicting disagreement in tasks about word sense. The workshop hosted a shared task on ordinal word-in-context judgments where participants were asked to predict the median of annotator judgments and the mean of pairwise absolute judgment differences between annotators.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cece68a-8d96-4dea-8abc-12989494f1bb",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "0710b1af-5bfa-499c-97dd-646e843d60e5",
  "sourceToolAssistantUUID": "0cece68a-8d96-4dea-8abc-12989494f1bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-10T08:00:34.058Z_

<details><summary>↩ Tool result · `toolu_0122K6pLaKSQ9o5CdjVBAAGt`</summary>

```text
# Paper Analysis

**Title:** "Dealing with Annotator Disagreement in Hate Speech Classification"

**Authors:** Somaiyeh Dehghan, Mehmet Umut Sen, Berrin Yanikoglu

**Abstract Summary:** The paper addresses disagreement among annotators when labeling hate speech, particularly in Turkish tweets. It examines "automatic approaches for aggregating multiple annotations" to improve dataset quality for machine learning models.

## Key Findings

**Does it classify types of annotation disagreement?**
No clear evidence in the provided content. The abstract mentions the "diverse and often subjective nature" causing disagreements but doesn't detail specific disagreement categories.

**Does it generate clarification probes or questions for annotators?**
Not indicated in the available metadata or abstract.

**Does it distinguish between value divergence, conceptual ambiguity, and borderline cases?**
The abstract notes disagreements stem from "varying interpretations" but doesn't explicitly differentiate between these three specific phenomena.

**Key Methods:** The paper evaluates "various automatic approaches for aggregating multiple annotations" rather than preventing or classifying disagreement types.

**Note:** The full paper (20 pages) likely contains more detailed analysis. This extraction is limited to information visible on the arXiv abstract page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f018fe8a-c2b4-4240-8486-e7ba190938f4",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "091d9bc1-b04f-4e86-a212-f390a570a56d",
  "sourceToolAssistantUUID": "f018fe8a-c2b4-4240-8486-e7ba190938f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-10T08:00:36.663Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011x9cBGM9rKUHCotn76ktHK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.08425",
  "prompt": "Extract title, authors, abstract, and key methods. Does this paper classify types of annotation disagreement? Does it involve probing annotators or generating clarification questions? What is its core contribution?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "091d9bc1-b04f-4e86-a212-f390a570a56d",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY3m22vmvG6LQDdfxVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b8cd7653-28fc-4864-bcb1-00380ddb341b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TNKtufVpk9tf1zr777ESYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1060,
      "cache_creation_input_tokens": 977,
      "cache_read_input_tokens": 26478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 977,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-10T08:00:37.421Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01C737427Ag5G4PxYei3pYZD`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.01168",
  "prompt": "Extract title, authors, abstract, and key methods. Does this paper classify types of annotation disagreement, specifically distinguishing between value divergence, conceptual ambiguity, and borderline cases? Does it involve probing or clarification questions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8cd7653-28fc-4864-bcb1-00380ddb341b",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY3m22vmvG6LQDdfxVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "232ccf8a-c406-4945-90c0-604f21787a93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TNKtufVpk9tf1zr777ESYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1060,
      "cache_creation_input_tokens": 977,
      "cache_read_input_tokens": 26478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 977,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-10T08:00:38.116Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AKUdoQxyWivLHwbMbnGX5v`</summary>

```json
{
  "query": "\"will annotators disagree\" \"value-laden\" subjectivity disagreement prediction 2025 EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "232ccf8a-c406-4945-90c0-604f21787a93",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY3m22vmvG6LQDdfxVy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76a0c65a-b411-4a67-b1e6-f17fec000c5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TNKtufVpk9tf1zr777ESYt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1060,
      "cache_creation_input_tokens": 977,
      "cache_read_input_tokens": 26478,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 977
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1060,
          "output_tokens": 298,
          "cache_read_input_tokens": 26478,
          "cache_creation_input_tokens": 977,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 977,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-10T08:00:42.626Z_

<details><summary>↩ Tool result · `toolu_01C737427Ag5G4PxYei3pYZD`</summary>

```text
# Paper Analysis

**Title:** Quantifying and Predicting Disagreement in Graded Human Ratings

**Authors:** Leixin Zhang, Çağrı Çöltekin (University of Tübingen, Germany)

**Abstract Summary:**
The paper investigates whether annotation disagreement patterns can be predicted from textual features using Likert-scale ratings for inappropriate language detection tasks. It proposes the Opposition Index metric to quantify perspective opposition and examines two aspects: annotation variance and opposing stances.

## Key Methods

1. **Variance Prediction:** Two approaches—direct regression on variance values and distribution-based prediction computing variance from predicted Likert distributions

2. **Opposition Index:** A novel metric measuring polarization where "index ranges from 0 to 1, with 1 indicating maximal polarization"

3. **Loss Functions:** Earth Mover's Distance, EMD with mean regularization, ordinal cumulative cross-entropy, and KL divergence

4. **Datasets:** Three inappropriate language datasets (offensive language, hate speech, toxicity) with 3-5 point Likert scales

## Does It Classify Types of Disagreement?

**No.** The paper does not distinguish between value divergence, conceptual ambiguity, and borderline cases. Instead, it focuses on predicting the magnitude and structure of disagreement through variance estimation and opposition detection.

## Does It Use Probing/Clarification Questions?

**No.** The approach relies solely on textual features encoded via Sentence-Transformer embeddings without interactive clarification mechanisms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "232ccf8a-c406-4945-90c0-604f21787a93",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "851c29f3-3c0c-4627-82d8-8a521edd5645",
  "sourceToolAssistantUUID": "232ccf8a-c406-4945-90c0-604f21787a93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-10T08:00:43.480Z_

<details><summary>↩ Tool result · `toolu_01AKUdoQxyWivLHwbMbnGX5v`</summary>

```text
Web search results for query: ""will annotators disagree" "value-laden" subjectivity disagreement prediction 2025 EMNLP"

Links: [{"title":"Will Annotators Disagree? Identifying Subjectivity in Value-Laden Arguments - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.824/"},{"title":"Will Annotators Disagree? Identifying Subjectivity in Value- ...","url":"https://aclanthology.org/2025.findings-emnlp.824.pdf"},{"title":"[2509.06704] Will Annotators Disagree? Identifying Subjectivity in Value-Laden Arguments","url":"https://arxiv.org/abs/2509.06704"},{"title":"Will Annotators Disagree? Identifying Subjectivity in Value-Laden Arguments","url":"https://arxiv.org/html/2509.06704"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"LeWiDi 2025 - 3rd edition | LeWiDi","url":"https://le-wi-di.github.io/"},{"title":"When Annotators Disagree, Topology Explains: Mapper, a Topological Tool for Exploring Text Embedding Geometry and Ambiguity - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.426/"},{"title":"Modeling Annotator Disagreement for Subjective Tasks","url":"https://aclanthology.org/2023.emnlp-main.415.pdf"},{"title":"Agreeing to Disagree: Annotating Offensive Language Datasets with Annotators’ Disagreement - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.822/"},{"title":"Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP","url":"https://arxiv.org/html/2601.09065"}]

Based on the search results, I found the paper you're looking for:

"Will Annotators Disagree? Identifying Subjectivity in Value-Laden Arguments" was published in the Findings of the Association for Computational Linguistics: EMNLP 2025, held in Suzhou, China.

The paper is authored by Amir Homayounirad, Enrico Liscio, Tong Wang, Catholijn M Jonker, and Luciano Cavalcante Siebert.

The work explores methods for identifying subjectivity in recognizing the human values that motivate arguments, evaluating two main approaches: inferring subjectivity through value prediction vs. directly identifying subjectivity. Their experiments show that direct subjectivity identification significantly improves the model performance of flagging subjective arguments.

The paper is available through the ACL Anthology at: https://aclanthology.org/2025.findings-emnlp.824/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76a0c65a-b411-4a67-b1e6-f17fec000c5f",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "95b0c48a-bf50-4ca2-a24b-6486b649ce73",
  "sourceToolAssistantUUID": "76a0c65a-b411-4a67-b1e6-f17fec000c5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-10T08:00:44.286Z_

<details><summary>↩ Tool result · `toolu_011x9cBGM9rKUHCotn76ktHK`</summary>

```text
# Paper Analysis: DiADEM

**Title:** "Learning Who Disagrees: Demographic Importance Weighting for Modeling Annotator Distributions with DiADEM"

**Authors:** Samay U. Shetty, Tharindu Cyril Weerasooriya, Deepak Pandita, Christopher M. Homan

**Abstract Summary:**
The paper addresses how human annotators disagree on subjective content labeling tasks. Rather than collapsing judgments into majority labels, the authors propose modeling disagreement as reflecting "genuine differences in perspective shaped by annotators' social identities."

## Does it classify types of annotation disagreement?
No. The paper focuses on *predicting disagreement patterns* based on annotator demographics rather than categorizing different disagreement types.

## Does it involve probing annotators or generating clarification questions?
No. It works with existing annotated datasets (DICES and VOICED benchmarks) without interactive querying.

## Core Contribution:
DiADEM is a neural architecture that learns "how much each demographic axis matters" for predicting disagreement. Key innovations include:

- Per-demographic projections with learned importance weights (α vector)
- Specialized item-level disagreement loss measuring annotation variance prediction
- Empirical finding: race and age emerge as most influential demographic factors driving disagreement across datasets

The approach substantially outperforms LLM baselines on disagreement tracking metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8cd7653-28fc-4864-bcb1-00380ddb341b",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "281a3ef9-fa3d-45dc-b584-0c084f0d2385",
  "sourceToolAssistantUUID": "b8cd7653-28fc-4864-bcb1-00380ddb341b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-10T08:00:46.857Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016zcJVpSrzppkBiQu8Zqevv`</summary>

```json
{
  "url": "https://aclanthology.org/2025.findings-emnlp.824/",
  "prompt": "Extract the title, authors, abstract, and key methods. Does this paper classify types of annotation disagreement - especially distinguishing value divergence from ambiguity or borderline cases? Does it involve probing annotators or generating clarification questions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "281a3ef9-fa3d-45dc-b584-0c084f0d2385",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY4X2ghTjV1kWRdGSFw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "28ef188a-fc55-4196-8959-d47777ecccc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01V8wxKGnTt59EsXNvVvdSPz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1161,
      "cache_creation_input_tokens": 1707,
      "cache_read_input_tokens": 27455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1707,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-10T08:00:48.042Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Nuec82Tm6165ygWaJyZUhZ`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-main.426/",
  "prompt": "Extract title, authors, abstract, and key methods. Does this paper classify types of annotation disagreement? Does it distinguish between ambiguity types like conceptual vs borderline? Does it probe annotators or generate clarification questions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28ef188a-fc55-4196-8959-d47777ecccc8",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY4X2ghTjV1kWRdGSFw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1fbbe2d-b286-40c3-8ef2-f1db5a8458f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01V8wxKGnTt59EsXNvVvdSPz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1161,
      "cache_creation_input_tokens": 1707,
      "cache_read_input_tokens": 27455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1707,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-10T08:00:48.742Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WwFNBL7ppMB44oQFLAaPsu`</summary>

```json
{
  "query": "arXiv 2025 2026 \"disagreement type\" OR \"types of disagreement\" annotation NLP classification active resolution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1fbbe2d-b286-40c3-8ef2-f1db5a8458f7",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY4X2ghTjV1kWRdGSFw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0d1d215-4056-4e6e-8a84-fdfcb87dda24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01V8wxKGnTt59EsXNvVvdSPz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1161,
      "cache_creation_input_tokens": 1707,
      "cache_read_input_tokens": 27455,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1707
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1161,
          "output_tokens": 320,
          "cache_read_input_tokens": 27455,
          "cache_creation_input_tokens": 1707,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1707,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-10T08:00:51.277Z_

<details><summary>↩ Tool result · `toolu_016zcJVpSrzppkBiQu8Zqevv`</summary>

```text
# Paper Analysis

**Title:** "Will Annotators Disagree? Identifying Subjectivity in Value-Laden Arguments"

**Authors:** Amir Homayounirad, Enrico Liscio, Tong Wang, Catholijn M Jonker, Luciano Cavalcante Siebert

**Abstract Summary:** The paper addresses how aggregating annotations into single labels can obscure valuable disagreement insights. It examines methods for detecting subjectivity when identifying human values in arguments, comparing "inferring subjectivity through value prediction vs. directly identifying subjectivity."

## Does it classify annotation disagreement types?

The available content does not indicate the paper classifies distinct disagreement sources (value divergence versus ambiguity/borderline cases). The abstract focuses on "identifying subjectivity" and developing models to "flag subjective arguments," but doesn't describe typological distinctions among disagreement sources.

## Does it involve annotator probing or clarification questions?

No evidence appears in this page content of annotator interviews, clarification question generation, or probing methods. The work centers on computational approaches—using "contrastive loss with binary cross-entropy loss"—rather than direct annotator engagement or explanation-generation techniques.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28ef188a-fc55-4196-8959-d47777ecccc8",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "a1714ecf-6cd1-47d3-8dcb-e45dc47fa49d",
  "sourceToolAssistantUUID": "28ef188a-fc55-4196-8959-d47777ecccc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-10T08:00:51.906Z_

<details><summary>↩ Tool result · `toolu_01Nuec82Tm6165ygWaJyZUhZ`</summary>

```text
# Paper Analysis

**Title:** "When Annotators Disagree, Topology Explains: Mapper, a Topological Tool for Exploring Text Embedding Geometry and Ambiguity"

**Authors:** Nisrine Rair, Alban Goupil, Valeriu Vrabie, Emmanuel Chochoy

**Abstract Summary:** The paper proposes a topological approach using Mapper to examine how fine-tuned language models represent ambiguity in embedding space. Applied to RoBERTa-Large on the MD-Offense dataset, it reveals that models create "modular, non-convex regions aligned with model predictions" while showing tension between structural confidence and label alignment in ambiguous cases.

**Key Methods:**
- Topological data analysis via Mapper tool
- Analysis of embedding space geometry using connected components
- Prediction purity measurement (≥90% threshold)
- Comparison against traditional dimensionality reduction (PCA, UMAP)

---

## Does the paper address annotation disagreement classification?

**No.** The abstract does not indicate classification of disagreement types or investigation into annotator behavior itself.

## Does it distinguish ambiguity types?

**No.** The paper references "ambiguous cases" and "ambiguous data" generally but shows no evidence of distinguishing conceptual versus borderline ambiguity categories.

## Does it probe annotators or generate clarification questions?

**No.** The work focuses on analyzing model representations rather than engaging with annotators or producing clarification mechanisms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1fbbe2d-b286-40c3-8ef2-f1db5a8458f7",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "a45e2192-85f2-4a82-9b92-fc94a82735fe",
  "sourceToolAssistantUUID": "b1fbbe2d-b286-40c3-8ef2-f1db5a8458f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-10T08:00:58.488Z_

<details><summary>↩ Tool result · `toolu_01WwFNBL7ppMB44oQFLAaPsu`</summary>

```text
Web search results for query: "arXiv 2025 2026 "disagreement type" OR "types of disagreement" annotation NLP classification active resolution"

No links found.

The search returned no results. This could mean there are no arXiv papers from 2025-2026 that match all of these specific terms together. Let me try a more targeted search:

Links: [{"title":"DEALING WITH ANNOTATOR DISAGREEMENT IN HATE SPEECH CLASSIFICATION A PREPRINT","url":"https://arxiv.org/pdf/2502.08266"},{"title":"Quantifying and Predicting Disagreement in Graded Human Ratings","url":"https://arxiv.org/html/2605.01168"},{"title":"Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP","url":"https://arxiv.org/html/2601.09065"},{"title":"Modeling Annotator Disagreement with Demographic-Aware Experts and","url":"https://arxiv.org/pdf/2508.02853"},{"title":"Leveraging Annotator Disagreement for Text Classification","url":"https://arxiv.org/html/2409.17577v1"},{"title":"Dealing with Annotator Disagreement in Hate Speech Classification","url":"https://arxiv.org/html/2502.08266v2"},{"title":"Structured Disagreement in Health-Literacy Annotation: Epistemic Stability, Conceptual Difficulty, and Agreement-Stratified Inference","url":"https://arxiv.org/html/2604.19943"},{"title":"Beyond Black-Box Labels: Interpretable Criteria for Diagnosing Subjective NLP Tasks","url":"https://arxiv.org/html/2604.17022"},{"title":"STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems","url":"https://arxiv.org/html/2605.02122"},{"title":"MSA at BEA 2025 Shared Task: Disagreement-Aware Instruction Tuning for Multi-Dimensional Evaluation of LLMs as Math Tutors","url":"https://arxiv.org/html/2505.18549"}]

Based on the search results, I found several relevant arXiv papers from 2025-2026 that address disagreement annotation, NLP classification, and related topics. Here are the key papers:

## Recent arXiv Papers on Disagreement in NLP

**1. "Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP"** (January 2026)
This paper by Xu et al. (2025) addresses modeling annotator disagreement with demographic-aware experts and synthetic perspectives.

**2. "Quantifying and Predicting Disagreement in Graded Human Ratings"** (May 2026)
This work investigates types or causes of variation across annotators and disentangles noise from genuine disagreement. The authors propose the Opposition Index, a metric that quantifies perspective opposition among annotators on a given item.

**3. "Structured Disagreement in Health-Literacy Annotation"** (3 weeks ago)
This paper treats disagreement as potentially informative rather than erroneous, showing that disagreement is structured by the task itself rather than driven by individual raters.

**4. "STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems"** (1 week ago)
This work introduces a disagreement-aware evaluation framework that models latent item correctness and annotator-specific confusion patterns.

**5. "Beyond Black-Box Labels: Interpretable Criteria for Diagnosing Subjective NLP Tasks"** (1 week ago)
This paper distinguishes sources of disagreement: instance ambiguity, annotator subjectivity, and task underspecification.

**6. "Dealing with Annotator Disagreement in Hate Speech Classification"** (February 2025)
This work highlights that annotator disagreement stems from individual differences and data ambiguities, and advocates for embracing disagreement as a signal in model training and evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0d1d215-4056-4e6e-8a84-fdfcb87dda24",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "2220d510-deb4-4d71-bd96-1cb9ac095939",
  "sourceToolAssistantUUID": "b0d1d215-4056-4e6e-8a84-fdfcb87dda24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-10T08:01:01.884Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015faaws9JMyr8J1jt5sxt1t`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.19943",
  "prompt": "Extract the full title, authors, abstract, and key methods. This paper seems highly relevant - does it classify types of annotation disagreement (epistemic stability, conceptual difficulty)? Does it use probing or clarification questions for annotators? How does it relate to the idea of borderline threshold cases vs conceptual ambiguity?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2220d510-deb4-4d71-bd96-1cb9ac095939",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY5ZiSXeHum1VNrit5M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1cb035c-812e-468f-9695-44cab69e165d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SM7RCu3ABviA6FHT5BfJdR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3153,
      "cache_read_input_tokens": 29162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3153,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-10T08:01:02.779Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01N6JApB6SAPA7q6Z3kchsRt`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.09065",
  "prompt": "Extract the full abstract, taxonomy of disagreement types, and key contributions. Does this paper distinguish between value divergence, conceptual ambiguity, and borderline threshold cases as distinct disagreement types? Does it involve generating probes or clarification questions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1cb035c-812e-468f-9695-44cab69e165d",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY5ZiSXeHum1VNrit5M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "859cb1bd-66e7-46ce-9466-a806bf1d4231",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SM7RCu3ABviA6FHT5BfJdR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3153,
      "cache_read_input_tokens": 29162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3153,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-10T08:01:03.313Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015NMvNR3KEFANENbepuN3CL`</summary>

```json
{
  "query": "\"structured disagreement\" annotation \"epistemic\" OR \"conceptual\" taxonomy types NLP 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "859cb1bd-66e7-46ce-9466-a806bf1d4231",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY5ZiSXeHum1VNrit5M",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0c16e32c-24c7-4a0f-983b-a713b5306c1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SM7RCu3ABviA6FHT5BfJdR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3153,
      "cache_read_input_tokens": 29162,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3153
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 327,
          "cache_read_input_tokens": 29162,
          "cache_creation_input_tokens": 3153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3153,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-10T08:01:07.650Z_

<details><summary>↩ Tool result · `toolu_015faaws9JMyr8J1jt5sxt1t`</summary>

```text
# Paper Summary

**Full Title:** "Structured Disagreement in Health-Literacy Annotation: Epistemic Stability, Conceptual Difficulty, and Agreement-Stratified Inference"

**Authors:** Olga Kellert, Sriya Kondury, Candice Koo, Nemika Tyagi, Steffen Eikenberry

## Abstract Overview

The research analyzes 6,323 COVID-19 responses from Ecuador and Peru using graded health-literacy annotations. Rather than collapsing disagreement into single labels, the team examined "the full distribution of judgments" across multiple independent annotators assigning proportional correctness scores.

## Key Finding on Disagreement Classification

Yes, the paper explicitly distinguishes between sources of disagreement. The variance decomposition reveals that "question-level conceptual difficulty accounts for substantially more variance than annotator identity," indicating structured, task-driven rather than rater-driven disagreement. This maps onto their distinction between **epistemically stable components** (where annotators reliably agree) and **unstable components** (where difficulty drives variance).

## Methods and Approach

The study does **not** appear to use clarification questions for annotators based on the abstract. Instead, it employs **agreement-stratified analysis**, examining how social-scientific effects (country, education, urbanicity) "vary in magnitude and in some cases reverse direction across levels of inter-annotator agreement."

## Relevance to Borderline Cases

The findings support modeling borderline threshold cases separately from conceptual ambiguity, as the paper argues that "aggregating across them can obscure important inferential differences" in graded interpretive tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1cb035c-812e-468f-9695-44cab69e165d",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "774fe4da-34e6-4628-8971-bb9ef8c7dc87",
  "sourceToolAssistantUUID": "a1cb035c-812e-468f-9695-44cab69e165d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-10T08:01:08.309Z_

<details><summary>↩ Tool result · `toolu_01N6JApB6SAPA7q6Z3kchsRt`</summary>

```text
# Analysis of arXiv:2601.09065

## Full Abstract

"Annotator disagreement is widespread in NLP, particularly for subjective and ambiguous tasks such as toxicity detection and stance analysis. While early approaches treated disagreement as noise to be removed, recent work increasingly models it as a meaningful signal reflecting variation in interpretation and perspective. This survey provides a unified view of disagreement-aware NLP methods. We first present a domain-agnostic taxonomy of the sources of disagreement spanning data, task, and annotator factors. We then synthesize modeling approaches using a common framework defined by prediction targets and pooling structure, highlighting a shift from consensus learning toward explicitly modeling disagreement, and toward capturing structured relationships among annotators. We review evaluation metrics for both predictive performance and annotator behavior, and noting that most fairness evaluations remain descriptive rather than normative. We conclude by identifying open challenges and future directions, including integrating multiple sources of variation, developing disagreement-aware interpretability frameworks, and grappling with the practical tradeoffs of perspectivist modeling."

## Taxonomy and Specific Disagreement Types

The provided content does **not** detail the specific disagreement taxonomy. The abstract only mentions a "domain-agnostic taxonomy of the sources of disagreement spanning data, task, and annotator factors" without elaborating on whether it distinguishes value divergence, conceptual ambiguity, or threshold cases as discrete categories.

## Probe/Clarification Question Generation

The webpage contains no information suggesting the paper involves generating probes or clarification questions.

**Note:** Full details on the taxonomy structure and methodology would require accessing the complete paper PDF.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "859cb1bd-66e7-46ce-9466-a806bf1d4231",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "d3c189b4-e9c9-4194-ac21-c2ab4ff5639b",
  "sourceToolAssistantUUID": "859cb1bd-66e7-46ce-9466-a806bf1d4231",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-10T08:01:17.197Z_

<details><summary>↩ Tool result · `toolu_015NMvNR3KEFANENbepuN3CL`</summary>

```text
Web search results for query: ""structured disagreement" annotation "epistemic" OR "conceptual" taxonomy types NLP 2025 2026"

Links: [{"title":"[2604.19943] Structured Disagreement in Health-Literacy Annotation: Epistemic Stability, Conceptual Difficulty, and Agreement-Stratified Inference","url":"https://arxiv.org/abs/2604.19943"},{"title":"Structured Disagreement in Health-Literacy Annotation: Epistemic Stability, Conceptual Difficulty, and Agreement-Stratified Inference","url":"https://arxiv.org/html/2604.19943"},{"title":"Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator","url":"https://arxiv.org/pdf/2601.09065"},{"title":"Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP","url":"https://arxiv.org/html/2601.09065"},{"title":"Learning from Disagreement: A Survey","url":"https://jair.org/index.php/jair/article/download/12752/26751/29240"},{"title":"The Case for Ambiguity Detection in NLI","url":"https://aclanthology.org/2025.nlperspectives-1.4.pdf"},{"title":"Building custom NLP tools to annotate discourse-functional features for second language writing research: A tutorial - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2772766124000594"},{"title":"Why Don't You Do It Right? Analysing Annotators' ...","url":"https://cris.fbk.eu/retrieve/085c1b8c-15ca-4103-bd30-8284636a91f9/2023.eacl-main.178.pdf"},{"title":"A Comprehensive Taxonomy of Negation for NLP and ...","url":"https://aclanthology.org/2025.findings-emnlp.839.pdf"},{"title":"Why do experts disagree? The development of a taxonomy - Kristine Deroover, Simon Knight, Paul F. Burke, Tamara Bucher, 2023","url":"https://journals.sagepub.com/doi/10.1177/09636625221110029"}]

I found highly relevant results for your search. Here's what the research shows:

## Key Finding: Recent Work on Structured Disagreement (2026)

The most directly relevant work is an arXiv paper from April 2026 titled "Structured Disagreement in Health-Literacy Annotation: Epistemic Stability, Conceptual Difficulty, and Agreement-Stratified Inference". This paper addresses your exact query terms:

### Epistemic and Conceptual Dimensions

The paper distinguishes that graded health-literacy evaluation contains both epistemically stable and unstable components, and that aggregating across them can obscure important inferential differences. 

The study found that question-level conceptual difficulty accounts for substantially more variance than annotator identity, indicating that disagreement is structured by the task itself rather than driven by individual raters.

### Taxonomy of Disagreement Sources

Another highly relevant recent survey (January 2026) provides a unified taxonomy of disagreement across data-, task-, and annotator-driven sources, along with a synthesis of disagreement-aware methods, mapping approaches to disagreement sources, prediction targets, and pooling structures.

### Sources of Disagreement

Prior work identifies three data-driven sources of disagreement: data quality issues, linguistic ambiguity, and epistemic uncertainty—cases with no single ground truth, such as subjective or culturally situated interpretations.

These papers provide the most current frameworks for understanding how "epistemic" and "conceptual" categories structure disagreement in NLP annotation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c16e32c-24c7-4a0f-983b-a713b5306c1e",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "57b15fbe-653c-44be-8561-af8ddbab423b",
  "sourceToolAssistantUUID": "0c16e32c-24c7-4a0f-983b-a713b5306c1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-10T08:01:20.529Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HGbULSfWbDGFZEjYozkdA4`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.19943",
  "prompt": "Extract the key sections: What are the specific disagreement categories/types discussed? How do they distinguish \"epistemic stability\" from \"conceptual difficulty\"? Do the authors propose any probing or clarification questions for annotators? What methods do they use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57b15fbe-653c-44be-8561-af8ddbab423b",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY6wNxSN1pDn2dutkaa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5a850e06-a537-43ca-b76b-97abd2bc3087",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019DeSNo6ujpMJp9tRv1ZdSt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2148,
      "cache_read_input_tokens": 32315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2148,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-10T08:01:21.223Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ftu4KVvKL3eMABYosyF6ZB`</summary>

```json
{
  "query": "\"active annotation\" disagreement \"type\" OR \"taxonomy\" labeler clarification question 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a850e06-a537-43ca-b76b-97abd2bc3087",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY6wNxSN1pDn2dutkaa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb17a95c-7005-4b3e-8a78-57d6f290eddf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019DeSNo6ujpMJp9tRv1ZdSt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2148,
      "cache_read_input_tokens": 32315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2148,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-10T08:01:21.688Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017n32NhywFdpsRhSP6rA75s`</summary>

```json
{
  "query": "EMNLP 2025 ACL 2025 disagreement \"soft label\" \"probe\" OR \"probing\" OR \"elicitation\" annotation NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb17a95c-7005-4b3e-8a78-57d6f290eddf",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY6wNxSN1pDn2dutkaa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "15069d34-6c21-4cff-ac0c-3e271023ba38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019DeSNo6ujpMJp9tRv1ZdSt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2148,
      "cache_read_input_tokens": 32315,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2148
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 268,
          "cache_read_input_tokens": 32315,
          "cache_creation_input_tokens": 2148,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2148,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-10T08:01:28.114Z_

<details><summary>↩ Tool result · `toolu_01HGbULSfWbDGFZEjYozkdA4`</summary>

```text
# Key Findings on Disagreement Structure and Epistemic Stability

## Disagreement Categories

The authors identify disagreement arising from three sources rather than discrete types:
- **Task-level conceptual difficulty**: Questions requiring biomedical mechanisms and implicit reasoning show higher variance
- **Socially structured knowledge differences**: Educational background and geographic location correlate with response variation
- **Interpretive ambiguity in graded assessment**: Partial correctness judgments create intermediate scoring zones

## Epistemic Stability vs. Conceptual Difficulty

The paper distinguishes these through variance decomposition:

**Epistemic Stability** refers to "responses that are consistently interpretable across raters," evident when inter-annotator agreement remains high (κ > 0.60).

**Conceptual Difficulty** describes inherent task complexity. The authors show "question-level conceptual difficulty accounts for substantially more variance than annotator identity" (33.73% vs. 1.14%), suggesting disagreement reflects the task itself rather than rater inconsistency.

Critically, they demonstrate that effects "vary in magnitude and in some cases reverse direction" across agreement strata, indicating medium-agreement items occupy unstable interpretive zones.

## Annotation Methods

The authors employed:
- **Proportional correctness scoring** on five-point scale {0, 0.25, 0.5, 0.75, 1.0}
- **Independent annotation** without inter-rater discussion
- **Blinded evaluation** to sociodemographic metadata
- **Pilot training** for consistency

However, they did **not propose clarification questions**. They acknowledge this limitation, noting annotators "were drawn from a single institutional context, which may introduce shared interpretive biases."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a850e06-a537-43ca-b76b-97abd2bc3087",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "5b3ea4a4-c1e7-498c-be6c-cbe80c70fbfe",
  "sourceToolAssistantUUID": "5a850e06-a537-43ca-b76b-97abd2bc3087",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-10T08:01:29.163Z_

<details><summary>↩ Tool result · `toolu_01Ftu4KVvKL3eMABYosyF6ZB`</summary>

```text
Web search results for query: ""active annotation" disagreement "type" OR "taxonomy" labeler clarification question 2024 2025 2026"

Links: [{"title":"Can Large Language Models Capture Human Annotator Disagreements?","url":"https://openreview.net/pdf?id=SfMoAphDly"},{"title":"Can Large Language Models Capture Human Annotator Disagreements? by Jingwei Ni, Yu Fan, Vilém Zouhar, Donya Rooein, Alexander Hoyle, Mrinmaya Sachan, Markus Leippold, Dirk Hovy, Elliott Ash :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/5319936.pdf?abstractid=5319936"},{"title":"Disambiguation in Conversational Question Answering in the Era of LLM: A Survey","url":"https://arxiv.org/html/2505.12543v1"},{"title":"Data Annotation Guide 2026: Complete Overview & Downloadable Checklist | Sama","url":"https://www.sama.com/blog/data-annotation-guide"},{"title":"Leveraging Annotator Disagreement for Text Classification - ACL Anthology","url":"https://aclanthology.org/2024.icnlsp-1.1/"},{"title":"Comparing Labeling Behaviour of Annotator Groups - Methods Hub - GESIS","url":"https://methodshub.gesis.org/library/tutorials/methodshub-perspective-annotation-comparison/1/"},{"title":"The Empirical Variability of Narrative Perceptions of Social ...","url":"https://aclanthology.org/2024.emnlp-main.1113.pdf"},{"title":"Leveraging Annotator Disagreement for Text Classification","url":"https://arxiv.org/html/2409.17577v1"},{"title":"A Survey on Asking Clarification Questions Datasets in ...","url":"https://aclanthology.org/2023.acl-long.152.pdf"},{"title":"Disambiguation in Conversational Question Answering in the Era of LLMs and Agents: A Survey","url":"https://arxiv.org/html/2505.12543v2"}]

I've performed the web search for your query. Here are the key results found:

## Research on Annotation Disagreement (2024-2025)

The search returned several relevant academic papers and resources addressing annotation disagreement, taxonomies, and clarification in recent publications:

**Recent Studies on Annotation Disagreement:**

LLMs' ability to predict annotation disagreements is being evaluated without access to repeated human labels, with results showing that LLMs struggle with modeling disagreements, which can be overlooked by majority label-based evaluations.

It is common practice in text classification to only use one majority label for model training even if a dataset has been annotated by multiple annotators, though doing so can remove valuable nuances and diverse perspectives inherent in the annotators' assessments.

**Handling Disagreement in Annotation Tasks:**

Researchers propose and compare different strategies to leverage annotator disagreement for text classification: a probability-based multi-label method, an ensemble system, and instruction tuning, all evaluated on tasks of hate speech and abusive conversation detection.

**Clarification Questions and Ambiguity Detection:**

A taxonomy of eight ambiguity types has been introduced in the CLAMBER benchmark for conversational question answering. Recent studies employ methods to detect multiple ambiguity types—syntactic, semantic, and contextual—demonstrating that explicit modeling of ambiguity categories can improve detection.

**Distinguishing Error from Valid Disagreement:**

Distinguishing errors from valid disagreement is an ongoing field of research in annotation studies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb17a95c-7005-4b3e-8a78-57d6f290eddf",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "dcbf0f65-ed3a-4f08-ab71-cf9f9be21d57",
  "sourceToolAssistantUUID": "cb17a95c-7005-4b3e-8a78-57d6f290eddf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-10T08:01:30.044Z_

<details><summary>↩ Tool result · `toolu_017n32NhywFdpsRhSP6rA75s`</summary>

```text
Web search results for query: "EMNLP 2025 ACL 2025 disagreement "soft label" "probe" OR "probing" OR "elicitation" annotation NLP"

Links: [{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"LINGUIST List 36.1369 Confs: EMNLP Workshop: Perspectivist Approaches to NLP (China)","url":"https://linguistlist.org/issues/36/1369/"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-emnlp/"},{"title":"LINGUIST List 36.1741 Calls: EMNLP Workshop: Perspectivist Approaches to NLP (China)","url":"https://linguistlist.org/issues/36/1741/"},{"title":"Layer-wise Minimal Pair Probing Reveals Contextual ...","url":"https://aclanthology.org/2025.emnlp-main.1790.pdf"},{"title":"Learning with Annotator Disagreement in STS","url":"https://aclanthology.org/2025.emnlp-main.1800.pdf"},{"title":"EMNLP 2025 to include Responsible NLP Checklists as Paper Appendices – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/responsible-nlp-checklist-appendices"},{"title":"EMNLP.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/EMNLP.2025"},{"title":"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track - ACL Anthology","url":"https://aclanthology.org/volumes/2025.emnlp-industry/"}]

Based on the search results, I found relevant information about EMNLP 2025 related to disagreement and annotation topics:

## Key Findings:

### NUTMEG Paper
NUTMEG: Separating Signal From Noise in Annotator Disagreement by Jonathan Ivey, Susan Gauch, and David Jurgens is an accepted main conference paper at EMNLP 2025.

### Soft-Label Learning in STS
There is a paper accepted at EMNLP 2025 titled "Beyond Averages: Learning with Annotator Disagreement in STS" that explores the trade-offs between training with a soft-label objective versus applying purely post-hoc calibration to a standard approach.

### Probing Research
An EMNLP 2025 paper on "Layer-wise Minimal Pair Probing Reveals Contextual Grammatical-Conceptual Hierarchy in Speech Representations" synthesizes speech minimal pairs from text-based benchmarks and probes speech models for contextual syntax and semantics.

### NLPerspectives Workshop and Le-Wi-Di Shared Task
The NLPerspectives workshop will host the new edition of Learning with Disagreement (Le-Wi-Di) shared task to explore new approaches to modelling and evaluation of Perspectivist benchmarks, co-located with EMNLP 2025 in Suzhou, China, in November 5-9, 2025. The proposed tasks feature datasets that address disagreement in both interpretation and labeling—with a dataset for Natural Language Inference (NLI) and another for paraphrase detection—as well as subjective tasks, including irony and sarcasm detection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15069d34-6c21-4cff-ac0c-3e271023ba38",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "acbf088e-12ba-443f-ac17-8044280d4b90",
  "sourceToolAssistantUUID": "15069d34-6c21-4cff-ac0c-3e271023ba38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-10T08:01:32.411Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GbvTr8WsXovVcd2TeVFm3b`</summary>

```json
{
  "query": "NUTMEG \"separating signal from noise\" annotator disagreement Ivey Jurgens EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "acbf088e-12ba-443f-ac17-8044280d4b90",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY7tQPpeKrMmdum3B2b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ef082b1a-92e7-4b45-9f43-afc7fc6c9bad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JCXWCGPWvbVWjtdQcHrG7L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2600,
      "cache_read_input_tokens": 34463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2600,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-10T08:01:34.441Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CQsTTczFg2mSJcueK8axC8`</summary>

```json
{
  "url": "https://2026.eacl.org/program/main-accepted/",
  "prompt": "Search this list of accepted papers for any papers related to: annotation disagreement, disagreement types/taxonomy, clarification probes, active annotation, soft labels, borderline cases, ambiguity resolution, or probe generation for disagreeing annotators. List any matches with authors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef082b1a-92e7-4b45-9f43-afc7fc6c9bad",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY7tQPpeKrMmdum3B2b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "40c3d07b-2b46-4203-b2ca-5a72562f236e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JCXWCGPWvbVWjtdQcHrG7L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2600,
      "cache_read_input_tokens": 34463,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2600,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 49,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-10T08:01:35.043Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XanYZinNtaSM3zvqzdBFov`</summary>

```json
{
  "query": "\"annotation disagreement\" \"resolve\" OR \"resolution\" LLM \"generate questions\" OR \"generate probes\" OR \"elicit\" annotator 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40c3d07b-2b46-4203-b2ca-5a72562f236e",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY7tQPpeKrMmdum3B2b",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f846cfee-78d9-4769-ab1e-0c4ae6c1a788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JCXWCGPWvbVWjtdQcHrG7L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2600,
      "cache_read_input_tokens": 34463,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2600
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 276,
          "cache_read_input_tokens": 34463,
          "cache_creation_input_tokens": 2600,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2600,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-10T08:01:39.111Z_

<details><summary>↩ Tool result · `toolu_01CQsTTczFg2mSJcueK8axC8`</summary>

```text
# Papers Related to Annotation Disagreement and Related Topics

Based on my search of the accepted papers list, I found **one directly relevant paper**:

**"Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?"**
- Authors: Jingwei Ni; Yu Fan; Vilém Zouhar; Donya Rooein; Alexander Miserlis Hoyle; Mrinmaya Sachan; Markus Leippold; Dirk Hovy; Elliott Ash

This paper explicitly addresses whether reasoning capabilities in LLMs can help capture variation among human annotators.

Additionally, one paper addresses **annotation practices** more broadly:

**"Gender and Politeness Perception: A Novel Approach for Exploring Annotations Disagreement"**
- Authors: Ahmad Aljanaideh

This work examines "Annotations Disagreement" as a focal point for understanding perception variation.

No other papers in the list explicitly mention disagreement types/taxonomy, clarification probes, active annotation, soft labels, borderline cases, ambiguity resolution, or probe generation for disagreeing annotators.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40c3d07b-2b46-4203-b2ca-5a72562f236e",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "3708fb62-1583-43a3-9e78-a0ab7bf92e7d",
  "sourceToolAssistantUUID": "40c3d07b-2b46-4203-b2ca-5a72562f236e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-10T08:01:40.205Z_

<details><summary>↩ Tool result · `toolu_01GbvTr8WsXovVcd2TeVFm3b`</summary>

```text
Web search results for query: "NUTMEG "separating signal from noise" annotator disagreement Ivey Jurgens EMNLP 2025"

Links: [{"title":"NUTMEG: Separating Signal From Noise in Annotator Disagreement - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.144/"},{"title":"[2507.18890] NUTMEG: Separating Signal From Noise in Annotator Disagreement","url":"https://arxiv.org/abs/2507.18890"},{"title":"\"NUTMEG: Separating Signal From Noise in Annotator Disagreement\" by Jonathan W. Ivey, Susan Gauch et al.","url":"https://scholarworks.uark.edu/dtscuht/14/"},{"title":"NUTMEG: Separating Signal From Noise in Annotator Disagreement","url":"https://arxiv.org/html/2507.18890v1"},{"title":"\"Separating Signal From Noise in Annotator Disagreement\" by Jonathan W. Ivey, Susan Gauch et al.","url":"https://scholarworks.uark.edu/hnrcsturpc25/5/"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"NUTMEG: Separating Signal From Noise in Annotator Disagreement Jonathan Ivey","url":"https://arxiv.org/pdf/2507.18890"},{"title":"oro.open.ac.uk How Reliable are Annotations via Crowdsourcing? A Study about Inter-annotator Agreement for Multi-label Image Annotation ABSTRACT | Request PDF","url":"https://www.researchgate.net/publication/48990441_oroopenacuk_How_Reliable_are_Annotations_via_Crowdsourcing_A_Study_about_Inter-annotator_Agreement_for_Multi-label_Image_Annotation_ABSTRACT"},{"title":"David Jurgens's research works | University of Michigan and other places","url":"https://www.researchgate.net/scientific-contributions/David-Jurgens-69708417"},{"title":"[2601.09065] Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP","url":"https://arxiv.org/abs/2601.09065"}]

I found the paper you're looking for! Here's what I found about NUTMEG:

## NUTMEG: Separating Signal From Noise in Annotator Disagreement

NUTMEG is a paper by Jonathan Ivey, Susan Gauch, and David Jurgens, published at EMNLP 2025. It was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 2874–2887, in Suzhou, China.

### Main Contribution

NUTMEG is a new Bayesian model that incorporates information about annotator backgrounds to remove noisy annotations from human-labeled training data while preserving systematic disagreements.

### Problem It Addresses

NLP models often rely on human-labeled data for training and evaluation. Many approaches crowdsource this data from a large number of annotators with varying skills, backgrounds, and motivations, resulting in conflicting annotations. These conflicts have traditionally been resolved by aggregation methods that assume disagreements are errors. Recent work has argued that for many tasks annotators may have genuine disagreements and that variation should be treated as signal rather than noise.

### Key Results

Using synthetic data, NUTMEG is more effective at recovering ground-truth from annotations with systematic disagreement than traditional aggregation methods. The results highlight the importance of accounting for both annotator competence and systematic disagreements when training on human-labeled data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef082b1a-92e7-4b45-9f43-afc7fc6c9bad",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "a40ee4ae-798b-4d7a-8ffb-ac4275ee3796",
  "sourceToolAssistantUUID": "ef082b1a-92e7-4b45-9f43-afc7fc6c9bad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-10T08:01:41.541Z_

<details><summary>↩ Tool result · `toolu_01XanYZinNtaSM3zvqzdBFov`</summary>

```text
Web search results for query: ""annotation disagreement" "resolve" OR "resolution" LLM "generate questions" OR "generate probes" OR "elicit" annotator 2025 2026"

Links: [{"title":"Learning Who Disagrees: Demographic Importance Weighting for Modeling Annotator Distributions with DiADEM","url":"https://arxiv.org/html/2604.08425"},{"title":"[Quick Review] Can Large Language Models Capture Human Annotator Disagreements?","url":"https://liner.com/review/can-large-language-models-capture-human-annotator-disagreements"},{"title":"Can Large Language Models Capture Human Annotator Disagreements? by Jingwei Ni, Yu Fan, Vilém Zouhar, Donya Rooein, Alexander Hoyle, Mrinmaya Sachan, Markus Leippold, Dirk Hovy, Elliott Ash :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/5319936.pdf?abstractid=5319936"},{"title":"GitHub - llm-as-a-judge/Awesome-LLM-as-a-judge · GitHub","url":"https://github.com/llm-as-a-judge/Awesome-LLM-as-a-judge"},{"title":"Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?","url":"https://arxiv.org/pdf/2506.19467"},{"title":"Can Reasoning Help Large Language Models Capture Human Annotator Disagreement? - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.3/"},{"title":"Federated Learning for Exploiting Annotators’ Disagreements in Natural Language Processing | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00664/121195/Federated-Learning-for-Exploiting-Annotators"},{"title":"Can Large Language Models Capture Human Annotator Disagreements?","url":"https://openreview.net/pdf?id=SfMoAphDly"},{"title":"On Integrating LLMs Into an Argument Annotation Workflow","url":"https://aclanthology.org/2025.argmining-1.8.pdf"},{"title":"[2506.19467] Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?","url":"https://arxiv.org/abs/2506.19467"}]

I found several relevant results about annotation disagreement and LLMs from 2025-2026. Here's a summary of the key research:

## Recent Research on Annotation Disagreement and LLMs

Variation in human annotation (disagreements) is common in NLP, often reflecting important information like task subjectivity and sample ambiguity, and modeling this variation is important for applications sensitive to such information.

### LLM Capabilities in Disagreement Modeling

Recent work evaluates LLMs' ability to predict annotation disagreements without access to repeated human labels, finding that LLMs struggle with modeling disagreements, which can be overlooked by majority label-based evaluations. More specifically, RLVR-style reasoning degrades performance in disagreement modeling, while naive Chain-of-Thought (CoT) reasoning improves the performance of RLHF LLMs.

### Disagreement-Aware Approaches

The LeWiDi shared task series requires systems to predict soft label distributions over annotators, simulate individual annotator responses, and remain faithful to item-level disagreement patterns. Additionally, DiADEM (Disagreement- and Demographic-Aware Distribution Modeling) is a demographic-aware annotator learning method that addresses modeling challenges through learnable per-demographic importance weights and improved annotator item mixing strategies.

The search results focus primarily on modeling and capturing disagreement with LLMs rather than using LLMs to resolve disagreements through question generation or elicitation. The papers emphasize that disagreement contains valuable information that shouldn't be treated as noise to be eliminated.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f846cfee-78d9-4769-ab1e-0c4ae6c1a788",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "163f461c-942e-46e7-a689-4d003594c0ab",
  "sourceToolAssistantUUID": "f846cfee-78d9-4769-ab1e-0c4ae6c1a788",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-10T08:01:44.618Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G7UAbSr9xTfAVW1vxKcWHw`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-main.144/",
  "prompt": "Extract the title, authors, abstract, and key methods for NUTMEG. Does this paper distinguish between types of annotation disagreement (systematic vs noise)? How does it separate signal from noise in disagreement?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "163f461c-942e-46e7-a689-4d003594c0ab",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY8jXsfyuffZ8yXQuzU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80521533-3782-498b-958d-3f07e1325b71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JomxNvPyPqj7ujxhKJ8njf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2533,
      "cache_read_input_tokens": 37063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2533,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-10T08:01:45.435Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019dgQHHj33QajZhAHe9GqkL`</summary>

```json
{
  "query": "\"annotation guideline\" OR \"annotation instructions\" clarification question generation disagreement NLP LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80521533-3782-498b-958d-3f07e1325b71",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY8jXsfyuffZ8yXQuzU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1a0750e-ec89-4e95-8600-69bcc3d1cad0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JomxNvPyPqj7ujxhKJ8njf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2533,
      "cache_read_input_tokens": 37063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2533,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-10T08:01:46.751Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FZs5c5K9R4sBUkrXiQb6tW`</summary>

```json
{
  "url": "https://aclanthology.org/2025.comedi-1.13/",
  "prompt": "Extract the title, authors, abstract, and key methods. This paper is about automating annotation guideline improvements with LLMs. Does it generate clarification questions for annotators? Does it classify types of disagreement? How does it relate to probing annotators on specific disagreement types?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1a0750e-ec89-4e95-8600-69bcc3d1cad0",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY8jXsfyuffZ8yXQuzU",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "46717b71-bd25-4e18-9ef5-9ed78deb0b51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JomxNvPyPqj7ujxhKJ8njf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2533,
      "cache_read_input_tokens": 37063,
      "output_tokens": 324,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2533
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 324,
          "cache_read_input_tokens": 37063,
          "cache_creation_input_tokens": 2533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2533,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-10T08:01:48.255Z_

<details><summary>↩ Tool result · `toolu_01G7UAbSr9xTfAVW1vxKcWHw`</summary>

```text
# NUTMEG: Paper Summary

**Title:** NUTMEG: Separating Signal From Noise in Annotator Disagreement

**Authors:** Jonathan Ivey, Susan Gauch, David Jurgens

**Publication:** EMNLP 2025, pages 2874–2887

## Key Distinction: Systematic vs. Noise Disagreement

Yes, the paper explicitly addresses this distinction. It acknowledges that "recent work has argued that for many tasks annotators may have genuine disagreements and that variation should be treated as signal rather than noise," contrasting this with traditional approaches that "assume disagreements are errors."

## How NUTMEG Separates Signal from Noise

The paper introduces "a new Bayesian model that incorporates information about annotator backgrounds to remove noisy annotations from human-labeled training data while preserving systematic disagreements."

**Key methodological features:**
- Leverages annotator background information to distinguish problematic from substantive disagreement
- Removes noise while retaining legitimate variations
- Accounts for both "annotator competence and systematic disagreements"
- Analyzes how subpopulation sizes, disagreement rates, and spam rates affect performance

The approach demonstrates that downstream models trained on NUTMEG-aggregated data "significantly outperform models trained on data from traditionally aggregation methods."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80521533-3782-498b-958d-3f07e1325b71",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "86a23ed1-f4d6-4cad-a306-5520a1c063e4",
  "sourceToolAssistantUUID": "80521533-3782-498b-958d-3f07e1325b71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-10T08:01:50.866Z_

<details><summary>↩ Tool result · `toolu_01FZs5c5K9R4sBUkrXiQb6tW`</summary>

```text
# Paper Summary

**Title:** "Automating Annotation Guideline Improvements using LLMs: A Case Study"

**Authors:** Adrien Bibal, Nathaniel Gerlek, Goran Muric, Elizabeth Boschee, Steven C. Fincke, Mike Ross, Steven N. Minton

**Abstract Overview:**
The paper addresses annotation challenges by leveraging language models to enhance guidelines. The study demonstrates that LLMs can improve inter-annotator agreement "from 0.593 to 0.84 when improving WNUT-17's guidelines," while being more efficient than crowdsourced approaches.

## Key Findings

**Methods:** The case study focuses on entity recognition, using LLMs to iteratively refine annotation guidelines rather than relying on traditional crowdsourced workflows.

**Regarding Your Questions:**

Based on the provided content, the abstract does **not explicitly indicate** whether the paper:
- Generates clarification questions for annotators
- Classifies disagreement types
- Probes annotators on specific disagreement patterns

The available metadata emphasizes speed and cost advantages of LLM-based improvements over human-driven workflows, but specific methodological details about disagreement analysis mechanisms are not disclosed in this excerpt. Consulting the full PDF would be necessary to determine whether these elements are addressed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46717b71-bd25-4e18-9ef5-9ed78deb0b51",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "d12be60a-96c1-4807-b55b-4f78cbc4b1d9",
  "sourceToolAssistantUUID": "46717b71-bd25-4e18-9ef5-9ed78deb0b51",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-10T08:01:56.065Z_

<details><summary>↩ Tool result · `toolu_019dgQHHj33QajZhAHe9GqkL`</summary>

```text
Web search results for query: ""annotation guideline" OR "annotation instructions" clarification question generation disagreement NLP LLM 2025 2026"

Links: [{"title":"A Methodological Guide on Using Large Language Models for Text Annotation in the Social Sciences and Humanities with Python and R","url":"https://arxiv.org/html/2604.09638v1"},{"title":"The use of LLMs to annotate data in management research: Foundational guidelines and warnings - Carlson - 2026 - Strategic Management Journal - Wiley Online Library","url":"https://sms.onlinelibrary.wiley.com/doi/full/10.1002/smj.70023"},{"title":"Automating Annotation Guideline Improvements using LLMs: A Case Study - ACL Anthology","url":"https://aclanthology.org/2025.comedi-1.13/"},{"title":"Text Annotation: 2026 Techniques to Label Data for NLP Projects | Label Your Data","url":"https://labelyourdata.com/articles/data-annotation/text-annotation"},{"title":"Using Large Language Models for Text Annotation in ...","url":"https://sodascience.github.io/workshop_llm_data_collection/llm_social_science_paper.pdf"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-emnlp/"},{"title":"NLP Annotation Project","url":"https://people.ischool.berkeley.edu/~dbamman/nlpap.html"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"GitHub - Zhen-Tan-dmml/LLM4Annotation · GitHub","url":"https://github.com/Zhen-Tan-dmml/LLM4Annotation"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"}]

I found several relevant sources on annotation guidelines, clarification questions, and disagreement in NLP and LLM research from 2025-2026. Here's what the search revealed:

## Key Findings:

### Annotation Guidelines and Disagreement Resolution

Poor agreement between LLM and human annotations often signals ambiguous instructions or unclear category boundaries, and identifying disagreement patterns can clarify whether issues stem from annotation ambiguity or model behavior. Common improvements to address disagreements include clarifying category definitions, adding boundary examples, and explicitly stating how to handle ambiguous cases.

### Automating Guideline Improvements

Research shows LLMs can help produce guidelines of high quality, with inter-annotator agreement improving from 0.593 to 0.84 when improving guidelines, while being faster and cheaper than crowdsource workers.

### Examining Disagreement for Insights

When examining disagreement patterns, systematic LLM tendencies (such as overestimating scores) reveal potential issues with scoring instructions in the prompt, and incorporating few-shot examples may help calibrate the model and reduce systematic estimation errors.

### Recent Workshop Focus

The 20th Linguistic Annotation Workshop (LAW XX) for 2026 has a special theme on errors in annotation, specifically inviting submissions on objectively incorrect annotations—distinct from annotator disagreement—and the role of error analysis in improving data quality for both human-annotated and LLM-generated datasets.

These recent sources highlight growing interest in using LLMs to improve annotation guidelines and better understand disagreement in annotation workflows.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1a0750e-ec89-4e95-8600-69bcc3d1cad0",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "62dbc18a-e526-40c1-9940-bc17f5c61c66",
  "sourceToolAssistantUUID": "c1a0750e-ec89-4e95-8600-69bcc3d1cad0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-10T08:01:58.960Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X88FUXWadCGeWdQTSSuAqR`</summary>

```json
{
  "query": "\"disagreement resolution\" annotation NLP \"ambiguity\" \"subjectivity\" \"borderline\" 2025 2026 machine learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62dbc18a-e526-40c1-9940-bc17f5c61c66",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY9oYkK6MewLkbX4ZNm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "51df3068-6d42-4c28-b91d-c0bb2a2e97ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01441we5TWM8nUPBgxtvr4Y4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 325,
      "cache_creation_input_tokens": 1595,
      "cache_read_input_tokens": 39596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1595,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-10T08:02:00.638Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LMpMC2iC3ZCwDPgnXLmZ8i`</summary>

```json
{
  "url": "https://2025.emnlp.org/program/main_papers/",
  "prompt": "Search this page for papers about: annotation disagreement, disagreement taxonomy or types, active annotation, clarification questions or probes for annotators, soft label distribution, borderline cases, ambiguity types in annotation. List matching paper titles and any available authors."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51df3068-6d42-4c28-b91d-c0bb2a2e97ec",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatY9oYkK6MewLkbX4ZNm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1af5bf90-1935-47c5-ad86-3b12a3d5ab1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01441we5TWM8nUPBgxtvr4Y4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 325,
      "cache_creation_input_tokens": 1595,
      "cache_read_input_tokens": 39596,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1595
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 325,
          "output_tokens": 204,
          "cache_read_input_tokens": 39596,
          "cache_creation_input_tokens": 1595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1595,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-10T08:02:05.835Z_

<details><summary>↩ Tool result · `toolu_01LMpMC2iC3ZCwDPgnXLmZ8i`</summary>

```text
# Papers on Annotation Disagreement and Related Topics

Based on my search of the EMNLP 2025 accepted papers, I found the following relevant work:

**NUTMEG: Separating Signal From Noise in Annotator Disagreement**
- Authors: Jonathan Ivey, Susan Gauch, David Jurgens
- Focus: Addressing disagreement patterns in annotation tasks

**When Annotators Disagree, Topology Explains: Mapper, a Topological Tool for Exploring Text Embedding Geometry and Ambiguity**
- Authors: Nisrine Rair, Alban Goupil, Valeriu Vrabie, Emmanuel Chochoy
- Focus: Using topological methods to understand disagreement and ambiguity in text annotation

These papers directly address annotation disagreement. While other papers in the list touch on related concepts (such as ambiguity in QA tasks or soft label distributions), these two specifically focus on "disagreement taxonomy, types, clarification of disagreement patterns, or related annotation quality issues" as requested.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1af5bf90-1935-47c5-ad86-3b12a3d5ab1b",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "cd423f82-e3c9-4d78-ae23-0e932845b952",
  "sourceToolAssistantUUID": "1af5bf90-1935-47c5-ad86-3b12a3d5ab1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-10T08:02:09.624Z_

<details><summary>↩ Tool result · `toolu_01X88FUXWadCGeWdQTSSuAqR`</summary>

```text
Web search results for query: ""disagreement resolution" annotation NLP "ambiguity" "subjectivity" "borderline" 2025 2026 machine learning"

Links: [{"title":"[2506.19467] Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?","url":"https://arxiv.org/abs/2506.19467"},{"title":"[2506.19467v1] Can Large Language Models Capture Human Annotator Disagreements?","url":"http://arxiv.org/abs/2506.19467v1"},{"title":"Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP","url":"https://arxiv.org/html/2601.09065v1"},{"title":"Can Large Language Models Capture Human Annotator Disagreements? by Jingwei Ni, Yu Fan, Vilém Zouhar, Donya Rooein, Alexander Hoyle, Mrinmaya Sachan, Markus Leippold, Dirk Hovy, Elliott Ash :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/5319936.pdf?abstractid=5319936"},{"title":"Quantifying and Predicting Disagreement in Graded Human Ratings","url":"https://arxiv.org/html/2605.01168"},{"title":"Conflicts in Texts: Data, Implications and Challenges","url":"https://arxiv.org/html/2504.19472v2"},{"title":"Navigating Disagreements in NLP Annotation","url":"https://aclanthology.org/2025.comedi-1.pdf"},{"title":"Ambiguity and Disagreement in Abstract Meaning Representation - ACL Anthology","url":"https://aclanthology.org/2025.comedi-1.14/"},{"title":"Counting on Consensus: Selecting the Right Inter-annotator Agreement Metric for NLP Annotation and Evaluation","url":"https://arxiv.org/html/2603.06865"},{"title":"Learning from Disagreement: A Survey","url":"https://jair.org/index.php/jair/article/download/12752/26751/29240"}]

I found several highly relevant results about disagreement resolution, annotation, NLP, ambiguity, and subjectivity from 2025-2026. Here's a summary of the key findings:

## Recent Research on Disagreement in NLP Annotation

### Core Problem
Variation in human annotation (i.e., disagreements) is common in NLP, often reflecting important information like task subjectivity and sample ambiguity.

### LLM Challenges with Disagreement Modeling
While Large Language Models (LLMs) are increasingly used for automatic annotation to reduce human effort, their evaluation often focuses on predicting the majority-voted "ground truth" labels. LLMs struggle with modeling disagreements, which can be overlooked by majority label-based evaluations. Notably, while RLVR-style (Reinforcement learning with verifiable rewards) reasoning generally boosts LLM performance, it degrades performance in disagreement prediction.

### Sources and Classification of Disagreement
In NLP, disagreements arise from linguistic ambiguity, annotator backgrounds, task design, and dataset curation practices. Subjective ambiguity and annotator diversity are key contributors. Furthermore, annotation variation can arise from item ambiguity or vagueness (e.g., insufficient context), language complexity (e.g., use of slang or jargon), or annotators' personal beliefs, values, expertise, or personality.

### Modeling Disagreement Distributions
Predicting how much people disagree is becoming as important as predicting what label they choose. There is a convergence toward distribution-level modeling in newer architectures (Fornaciari et al. (2021) as a task-based model, Parappan and Henao (2025); Weerasooriya et al. (2023) as embedding-based models).

### Workshop and Shared Tasks
A workshop on "Context and Meaning: Navigating Disagreements in NLP Annotation" explores causes of disagreements in NLP annotations as well as strategies for effective handling or resolution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51df3068-6d42-4c28-b91d-c0bb2a2e97ec",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "45ef3a82-16a0-486e-80d9-83803c11560d",
  "sourceToolAssistantUUID": "51df3068-6d42-4c28-b91d-c0bb2a2e97ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-10T08:02:13.073Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NmokuGSnQ3baAhvXerX7fX`</summary>

```json
{
  "query": "arXiv cs.CL 2026 annotation disagreement type-specific probing resolution soft label training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45ef3a82-16a0-486e-80d9-83803c11560d",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatYAoeEZQ8Qmsz6fRsNT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec9d9b40-80e4-405d-ac07-c11ed78b012f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QZVs97QCyec3ADbogLX41C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 269,
      "cache_creation_input_tokens": 1674,
      "cache_read_input_tokens": 41191,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1674,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-10T08:02:13.992Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01X8E61sRCQksGrBRLxUWCyn`</summary>

```json
{
  "url": "https://arxiv.org/html/2504.19472v2",
  "prompt": "Extract the paper title, authors, abstract, and key methods. Does this paper classify types of disagreement in text? Does it distinguish between conceptual ambiguity, value divergence, and borderline threshold cases? Does it involve probing or clarification questions for annotators?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec9d9b40-80e4-405d-ac07-c11ed78b012f",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatYAoeEZQ8Qmsz6fRsNT",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b0cffc8-f53c-4a5c-b52c-7dc5a829aca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QZVs97QCyec3ADbogLX41C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 269,
      "cache_creation_input_tokens": 1674,
      "cache_read_input_tokens": 41191,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1674
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 269,
          "output_tokens": 198,
          "cache_read_input_tokens": 41191,
          "cache_creation_input_tokens": 1674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1674,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-10T08:02:19.011Z_

<details><summary>↩ Tool result · `toolu_01X8E61sRCQksGrBRLxUWCyn`</summary>

```text
# Paper Analysis

**Title:** "Conflicts in Texts: Data, Implications and Challenges"

**Authors:** Siyi Liu and Dan Roth (University of Pennsylvania)

**Abstract:** The paper presents a unified framework for understanding conflicting information in NLP across three primary sources: natural web texts, human-annotated data, and model interactions. It analyzes origins, implications, and mitigation strategies for each conflict type.

## Classification of Disagreement Types

**Yes**, this paper classifies disagreement types. It distinguishes between:

1. **Annotation disagreement sources**: The paper identifies that disagreements arise from "linguistic ambiguity, annotator backgrounds, and task design."

2. **Categorization framework**: It separates disagreements into "linguistic uncertainty, annotator bias, and task design" per Jiang and de Marneffe (2022).

## Distinction Between Ambiguity Types

The paper **partially addresses** your specific categories:

- **Conceptual ambiguity**: Addressed as "semantic ambiguities" and "linguistic ambiguity"
- **Value divergence**: Covered through "annotator bias" and "ethical and societal biases"
- **Borderline cases**: Mentioned as disagreements reflecting "hard-to-classify content"

However, the paper does not explicitly distinguish these as separate threshold-based categories in the way you've framed them.

## Clarification Questions/Probing

**No**, the paper does not discuss probing or clarification questions for annotators during annotation collection. It focuses on analyzing existing disagreement patterns rather than eliciting clarifications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b0cffc8-f53c-4a5c-b52c-7dc5a829aca1",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "40763602-0e10-441e-afc6-53e2bebfcbe5",
  "sourceToolAssistantUUID": "7b0cffc8-f53c-4a5c-b52c-7dc5a829aca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-10T08:02:19.673Z_

<details><summary>↩ Tool result · `toolu_01NmokuGSnQ3baAhvXerX7fX`</summary>

```text
Web search results for query: "arXiv cs.CL 2026 annotation disagreement type-specific probing resolution soft label training"

Links: [{"title":"Leveraging Annotator Disagreement for Text Classification","url":"https://arxiv.org/html/2409.17577v1"},{"title":"CLS: Cross Labeling Supervision for Semi-Supervised Learning Yao Yao","url":"https://arxiv.org/pdf/2202.08502"},{"title":"STABLEVAL: Disagreement-Aware and Stable Evaluation of AI Systems","url":"https://arxiv.org/html/2605.02122v1"},{"title":"[2311.05265] Don't Waste a Single Annotation: Improving Single-Label Classifiers Through Soft Labels","url":"https://arxiv.org/abs/2311.05265"},{"title":"How does Disagreement Help Generalization against Label Corruption?","url":"https://arxiv.org/pdf/1901.04215"},{"title":"Computation and Language","url":"https://arxiv.org/list/cs.CL/recent"},{"title":"Computation and Language Apr 2026","url":"https://arxiv.org/list/cs.CL/current?skip=205&show=500"},{"title":"[2603.25450] Cross-Model Disagreement as a Label-Free Correctness Signal","url":"https://arxiv.org/abs/2603.25450"},{"title":"arXiv:2112.07475v2 [cs.CL] 29 Apr 2022","url":"https://arxiv.org/pdf/2112.07475"},{"title":"Computation and Language May 2026","url":"https://arxiv.org/list/cs.CL/current"}]

Based on the web search results, I found several relevant papers in the cs.CL field related to annotation disagreement, soft label training, and related techniques:

## Key Findings

**Recent Work on Annotation Disagreement:**

One paper proposes and compares three different strategies to leverage annotator disagreement for text classification: a probability-based multi-label method, an ensemble system, and instruction tuning.

Research shows that additional annotator information, such as confidence, secondary label and disagreement, can be used to effectively generate soft labels, and training classifiers with these soft labels leads to improved performance and calibration on the hard label test set.

**Broader Perspective on Disagreement:**

There is growing interest in treating annotator disagreement as a meaningful signal rather than noise, with surveys and frameworks highlighting the need to model structured disagreement, especially for subjective tasks like toxicity detection and stance annotation.

Methods that explicitly model annotator-specific behavior or group-level variation via demographic-aware experts and synthetic perspectives demonstrate improved representation of structured disagreement.

The search results show an active research area examining how to better utilize annotation disagreement through soft label training approaches, type-specific handling, and structured disagreement modeling in computational linguistics research from 2024-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec9d9b40-80e4-405d-ac07-c11ed78b012f",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "d3de9aa3-1bcd-410b-9c45-9fab7f35c16f",
  "sourceToolAssistantUUID": "ec9d9b40-80e4-405d-ac07-c11ed78b012f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-10T08:02:23.544Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PNnoJheqi7A9tBTmMymGWX`</summary>

```json
{
  "url": "https://arxiv.org/list/cs.CL/current",
  "prompt": "Search this listing of recent cs.CL papers. Find any papers related to: annotation disagreement types or taxonomy, active annotation with probing or clarification questions, disagreement resolution by type, soft label training from disagreement, or borderline vs ambiguous annotation cases. List matching paper titles, authors, and arXiv IDs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3de9aa3-1bcd-410b-9c45-9fab7f35c16f",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatYBYWRxcrEfdj9xq1Dd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d54dc62-eac3-4303-bf8b-b13750b2dfc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0128T1oHccV4WMotugGLYHm5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 387,
      "cache_creation_input_tokens": 1211,
      "cache_read_input_tokens": 42865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1211,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-10T08:02:23.935Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CEM77AuLc6LPvmi3PB9sUv`</summary>

```json
{
  "query": "\"disagreement\" \"annotation\" \"probing\" OR \"clarification\" \"type\" OR \"category\" NLP paper 2025 2026 cs.CL arXiv ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d54dc62-eac3-4303-bf8b-b13750b2dfc7",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatYBYWRxcrEfdj9xq1Dd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e307574-df9a-45e7-9dd1-4602c3d49584",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0128T1oHccV4WMotugGLYHm5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 387,
      "cache_creation_input_tokens": 1211,
      "cache_read_input_tokens": 42865,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1211
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 387,
          "output_tokens": 233,
          "cache_read_input_tokens": 42865,
          "cache_creation_input_tokens": 1211,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1211,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-10T08:02:27.078Z_

<details><summary>↩ Tool result · `toolu_01PNnoJheqi7A9tBTmMymGWX`</summary>

```text
# Search Results

Based on the provided arXiv listing for May 2026 Computation and Language papers, I found **no papers** that directly match your specified research interests.

The search covered 50 entries (of 502 total) and included papers on topics such as:
- LLM evaluation and safety
- Language model behavior and reasoning
- Retrieval-augmented generation
- Multilingual and domain-specific NLP
- Model interpretability and probing

However, **none addressed**:
- Annotation disagreement taxonomies or types
- Active annotation with clarification questions
- Disagreement resolution methodologies
- Soft label training approaches
- Borderline versus ambiguous case categorization

To locate relevant papers on these specific annotation and disagreement topics, you would need to:
1. Search earlier or later months on arXiv
2. Use the Advanced Search feature with targeted keywords like "annotation disagreement," "inter-annotator agreement," or "soft labels"
3. Review papers from recent ACL/EMNLP proceedings focused on data annotation methodologies
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4d54dc62-eac3-4303-bf8b-b13750b2dfc7",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "a2cf4263-6036-45b7-9c7d-f902db3ce6f8",
  "sourceToolAssistantUUID": "4d54dc62-eac3-4303-bf8b-b13750b2dfc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-10T08:02:32.950Z_

<details><summary>↩ Tool result · `toolu_01CEM77AuLc6LPvmi3PB9sUv`</summary>

```text
Web search results for query: ""disagreement" "annotation" "probing" OR "clarification" "type" OR "category" NLP paper 2025 2026 cs.CL arXiv ACL EMNLP"

Links: [{"title":"Quantifying and Predicting Disagreement in Graded Human Ratings","url":"https://arxiv.org/html/2605.01168"},{"title":"Can Large Language Models Capture Human Annotator Disagreements? by Jingwei Ni, Yu Fan, Vilém Zouhar, Donya Rooein, Alexander Hoyle, Mrinmaya Sachan, Markus Leippold, Dirk Hovy, Elliott Ash :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/5319936.pdf?abstractid=5319936"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Counting on Consensus: Selecting the Right Inter-annotator Agreement Metric for NLP Annotation and Evaluation","url":"https://arxiv.org/html/2603.06865"},{"title":"Predicting Median, Disagreement and Noise Label in Ordinal Word-in-Context Data - ACL Anthology","url":"https://aclanthology.org/2025.comedi-1.6/"},{"title":"Text Annotation Tool: A 2026 Guide for ML and NLP Teams | Label Your Data","url":"https://labelyourdata.com/articles/data-annotation/text-annotation-tool"},{"title":"Beyond Black-Box Labels: Interpretable Criteria for Diagnosing Subjective NLP Tasks","url":"https://arxiv.org/html/2604.17022"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"Modeling Annotator Disagreement with Demographic-Aware Experts and","url":"https://arxiv.org/pdf/2508.02853"},{"title":"NLP Annotation Project","url":"https://people.ischool.berkeley.edu/~dbamman/nlpap.html"}]

Based on the web search results, I found several relevant recent NLP papers on disagreement, annotation, and related topics from 2025-2026:

## Key Papers Found:

1. **"Quantifying and Predicting Disagreement in Graded Human Ratings"** (2025)
   This paper performs detailed analysis to model the full distribution of Likert-scale ratings and examines its effectiveness in inferring annotators' opinion divergence with item textual features, using datasets with Likert-scale ratings that capture fine-grained human perception differences.

2. **"Can Large Language Models Capture Human Annotator Disagreements?"** (June 2025)
   This work addresses the gap by extensively evaluating LLMs' ability to predict annotation disagreements without access to repeated human labels, finding that LLMs struggle with modeling disagreements.

3. **"Predicting Median, Disagreement and Noise Label in Ordinal Word-in-Context Data"** (CoMeDi 2025)
   This paper aims to model different aspects of ordinal Word-in-Context annotations necessary to build a more human-like model: (i) the aggregated label, (ii) the disagreement between annotators, and (iii) the aggregated noise label which annotators can choose to exclude data points from annotation.

4. **"Beyond Black-Box Labels: Interpretable Criteria for Diagnosing Subjective NLP Tasks"** (2025)
   This work demonstrates how disagreement can stress-test a schema and guide revision.

5. **"Counting on Consensus: Selecting the Right Inter-annotator Agreement Metric for NLP Annotation and Evaluation"** (April 2026)
   This paper outlines how inter-annotator agreement (IAA) has been conceptualized and applied across NLP and related disciplines, organizing agreement measures by task type and discussing how factors such as label imbalance and missing data influence reliability estimates.

These papers represent recent work on annotation disagreement and related methodological topics in NLP conferences like ACL 2025 and workshops focused on annotation challenges.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e307574-df9a-45e7-9dd1-4602c3d49584",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "01ed67c9-8077-48d7-ab73-839396181e1a",
  "sourceToolAssistantUUID": "8e307574-df9a-45e7-9dd1-4602c3d49584",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-10T08:02:36.400Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011ftcFV2wFAkSv26XLdqY4P`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.02853",
  "prompt": "Extract full title, authors, abstract, and key methods. Does this paper classify types of annotation disagreement? Does it involve probing annotators, generating clarification questions, or doing type-conditioned resolution? What is new about it?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01ed67c9-8077-48d7-ab73-839396181e1a",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatYCXJ2gpP89XNDG1Xbk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f654296-b7a2-45bd-8abb-fc8d495f2eef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HzTNi56hkmV1XqwQ8Py8qG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2004,
      "cache_read_input_tokens": 44076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2004,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-10T08:02:37.175Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014kuUvAYp3DkaM9RrU512Mo`</summary>

```json
{
  "query": "\"DART\" annotation disagreement resolution \"type\" NLP 2025 2026 proposal framework active"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f654296-b7a2-45bd-8abb-fc8d495f2eef",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatYCXJ2gpP89XNDG1Xbk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc1b8dd0-5084-4b9b-a3a0-e30871dbaf8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HzTNi56hkmV1XqwQ8Py8qG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2004,
      "cache_read_input_tokens": 44076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2004,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-10T08:02:37.452Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C9tLeFt8qLn8MDEYvzUK7H`</summary>

```json
{
  "query": "annotation disagreement \"interactive\" OR \"dialogue\" annotator clarification probing NLP 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc1b8dd0-5084-4b9b-a3a0-e30871dbaf8e",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatYCXJ2gpP89XNDG1Xbk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9817bde3-70a2-4132-8c88-13b3db925e48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01HzTNi56hkmV1XqwQ8Py8qG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2004,
      "cache_read_input_tokens": 44076,
      "output_tokens": 246,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2004
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 246,
          "cache_read_input_tokens": 44076,
          "cache_creation_input_tokens": 2004,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2004,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-10T08:02:41.874Z_

<details><summary>↩ Tool result · `toolu_011ftcFV2wFAkSv26XLdqY4P`</summary>

```text
# Paper Analysis

**Full Title:** "Modeling Annotator Disagreement with Demographic-Aware Experts and Synthetic Perspectives"

**Authors:** Yinuo Xu, Veronica Derricks, Allison Earl, David Jurgens

**Abstract Summary:** The researchers present an approach addressing disagreement in subjective NLP annotation tasks. They introduce DEM-MoE (Demographic-Aware Mixture of Experts), which "routes inputs to expert subnetworks based on annotator demographics" to represent group-level variation. The work also explores LLM-generated synthetic annotations via persona prompting for data imputation and tests blending strategies for real and synthetic data.

## Classification & Methodology

**Does it classify disagreement types?** No explicit disagreement typology is described in the abstract or metadata provided.

**Probing/clarification/type-conditioned resolution?** None of these approaches are mentioned. The focus is on architectural modeling and data augmentation rather than interactive annotation refinement.

## What's Novel

The paper's innovations include:

1. **Demographic routing mechanism** — Using mixture-of-experts architecture tailored to annotator demographics rather than standard disagreement aggregation
2. **Synthetic persona-based augmentation** — Leveraging LLMs to generate synthetic annotations that fill demographic coverage gaps
3. **Dataset-aware blending strategies** — Proposing multiple approaches for combining real and synthetic data based on dataset structure

The work addresses representation of diverse perspectives through both model architecture and data-centric solutions rather than disagreement classification or interactive methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f654296-b7a2-45bd-8abb-fc8d495f2eef",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "ee947b67-a02a-4038-ab12-e2f0d1d1e4cd",
  "sourceToolAssistantUUID": "8f654296-b7a2-45bd-8abb-fc8d495f2eef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-10T08:02:45.893Z_

<details><summary>↩ Tool result · `toolu_014kuUvAYp3DkaM9RrU512Mo`</summary>

```text
Web search results for query: ""DART" annotation disagreement resolution "type" NLP 2025 2026 proposal framework active"

Links: [{"title":"Navigating Disagreements in NLP Annotation","url":"https://aclanthology.org/2025.comedi-1.pdf"},{"title":"DART: Leveraging Multi-Agent Disagreement for Tool Recruitment in Multimodal Reasoning - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.253/"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"[2512.07132] DART: Leveraging Multi-Agent Disagreement for Tool Recruitment in Multimodal Reasoning","url":"https://arxiv.org/abs/2512.07132"},{"title":"DARC: Disagreement-Aware Alignment via Risk-Constrained Decoding","url":"https://arxiv.org/html/2603.08145"},{"title":"Can Large Language Models Capture Human Annotator Disagreements? by Jingwei Ni, Yu Fan, Vilém Zouhar, Donya Rooein, Alexander Hoyle, Mrinmaya Sachan, Markus Leippold, Dirk Hovy, Elliott Ash :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/5319936.pdf?abstractid=5319936"},{"title":"Quantifying and Predicting Disagreement in Graded Human Ratings","url":"https://arxiv.org/html/2605.01168"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"GitHub - karan/language.dart: :hibiscus: Natural language processing utilities for Dart","url":"https://github.com/karan/language.dart"},{"title":"I beg to differ: how disagreement is handled in the annotation of legal machine learning data sets | Artificial Intelligence and Law | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10506-023-09369-4"}]

Based on the search results, I found relevant information about DART and annotation disagreement resolution in NLP. Here are the key findings:

## DART: Multi-Agent Disagreement for Tool Recruitment

DART (Leveraging Multi-Agent Disagreement for Tool Recruitment in Multimodal Reasoning) is a framework presented at the 2026 European Chapter of the Association for Computational Linguistics conference. DART uses disagreements between multiple debating visual agents to identify useful visual tools (e.g., object detection, OCR, spatial reasoning) that can resolve inter-agent disagreement.

The approach improves over multi-agent debate and single agent tool-calling frameworks, beating the next-strongest baseline by 3.4% and 2.4% on A-OKVQA and MMMU respectively. DART adapts well to new tools in applied domains, with a 1.3% improvement on the M3D medical dataset.

## Related NLP Annotation Disagreement Research

The broader context of annotation disagreement resolution in NLP for 2025-2026 includes:

- A workshop exploring causes of disagreements in NLP annotations as well as strategies for effective handling or resolution
- Recent research evaluates whether large language models can capture human annotation disagreement, as LLMs struggle with modeling disagreements despite potential majority label-based evaluations
- Studies examining whether annotation disagreement degree can be predicted from textual features and proposing metrics like the Opposition Index to quantify perspective opposition among annotators


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc1b8dd0-5084-4b9b-a3a0-e30871dbaf8e",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "e075f2f7-6c49-4b70-95c2-06015dc40666",
  "sourceToolAssistantUUID": "dc1b8dd0-5084-4b9b-a3a0-e30871dbaf8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-10T08:02:47.696Z_

<details><summary>↩ Tool result · `toolu_01C9tLeFt8qLn8MDEYvzUK7H`</summary>

```text
Web search results for query: "annotation disagreement "interactive" OR "dialogue" annotator clarification probing NLP 2025 2026"

Links: [{"title":"Counting on Consensus: Selecting the Right Inter-annotator Agreement Metric for NLP Annotation and Evaluation","url":"https://arxiv.org/html/2603.06865"},{"title":"Full article: Inter-annotator Agreement Using the Conversation Analysis Modelling Schema, for Dialogue","url":"https://www.tandfonline.com/doi/full/10.1080/19312458.2021.2020229"},{"title":"(PDF) Inter-annotator Agreement Using the Conversation Analysis Modelling Schema, for Dialogue","url":"https://www.researchgate.net/publication/357895917_Inter-annotator_Agreement_Using_the_Conversation_Analysis_Modelling_Schema_for_Dialogue"},{"title":"Funzac at CoMeDi Shared Task: Modeling Annotator Disagreement from Word-In-Context Perspectives - ACL Anthology","url":"https://aclanthology.org/2025.comedi-1.8/"},{"title":"Can Large Language Models Capture Human Annotator Disagreements? by Jingwei Ni, Yu Fan, Vilém Zouhar, Donya Rooein, Alexander Hoyle, Mrinmaya Sachan, Markus Leippold, Dirk Hovy, Elliott Ash :: SSRN","url":"https://papers.ssrn.com/sol3/Delivery.cfm/5319936.pdf?abstractid=5319936"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Modeling Annotator Disagreement with Demographic-Aware Experts and","url":"https://arxiv.org/pdf/2508.02853"},{"title":"Inter-Annotator Agreement: a key metric in Labeling","url":"https://www.innovatiana.com/en/post/inter-annotator-agreement"},{"title":"Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP","url":"https://arxiv.org/html/2601.09065v1"},{"title":"Enriching Subjective Data Annotation through Qualitative ...","url":"https://aclanthology.org/2025.hcinlp-1.20.pdf"}]

I've found several relevant results on annotation disagreement in NLP from 2025-2026. Here's what the search uncovered:

## Recent Work on Annotation Disagreement in NLP (2025-2026)

**Annotation Disagreement as a Research Focus:**

Recent surveys show that the emergence of LLM-based evaluation has reshaped the methodological landscape of NLP, with significant attention to how disagreement among annotators is handled and modeled.

**Modeling Disagreement Approaches:**

NLP has shifted from treating disagreement as noise to modeling it as structured variation, with families of disagreement modeling that attribute disagreement to annotator reliability, bias, or task difficulty. Mixture-of-experts approaches capture feature-level heterogeneity, while multi-head Transformers preserve uncertainty aligned with empirical disagreement.

**Interactive and Dialogue-Based Research:**

Research presents the Conversation Analysis Modeling Schema (CAMS), a novel dialogue labeling schema that combines the Conversation Analysis concept of Adjacency Pairs with Dialogue Acts. Studies show that annotator disagreement in dialogue tasks can be driven by alternative interpretations of utterances and ambiguity in transcriptions.

**Recent Conference Activity (2025):**

Recent shared tasks on annotator disagreement incorporate Word-In-Context (WiC) to bridge the gap between sentence-level semantic representation and annotator judgment variability. Additionally, EMNLP 2025 featured work on separating signal from noise in annotator disagreement.

The search results emphasize how annotation disagreement is now recognized as valuable structured information rather than just noise to be resolved through consensus.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9817bde3-70a2-4132-8c88-13b3db925e48",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "05d2a75e-c969-4fb3-8411-86e3924621b3",
  "sourceToolAssistantUUID": "9817bde3-70a2-4132-8c88-13b3db925e48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-10T08:02:52.753Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SzqGWkW1WucSR4oei1vB8H`</summary>

```json
{
  "url": "https://aclanthology.org/2025.hcinlp-1.20/",
  "prompt": "Extract the title, authors, abstract, and key methods. Does this paper use qualitative methods to probe or clarify annotation disagreements? Does it classify types of disagreement? Does it involve generating questions for annotators to resolve disagreements?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05d2a75e-c969-4fb3-8411-86e3924621b3",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatYDcU7PsMqNg31naeUZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b5333cc7-34f4-4d1b-a5c1-bf05f51beb13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Jb8pkvYTGaEWMGwXBkDoBG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2597,
      "cache_read_input_tokens": 46080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2597,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-10T08:02:53.323Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pc6ypTtC75T1GYnMigChmW`</summary>

```json
{
  "query": "\"annotator disagreement\" \"resolve\" OR \"resolution\" \"question\" OR \"probe\" crowdsourcing NLP active learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5333cc7-34f4-4d1b-a5c1-bf05f51beb13",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatYDcU7PsMqNg31naeUZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "299a1397-2ec3-447a-bfff-e690f661181e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Jb8pkvYTGaEWMGwXBkDoBG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2597,
      "cache_read_input_tokens": 46080,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2597,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 57,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-10T08:02:57.200Z_

<details><summary>↩ Tool result · `toolu_01SzqGWkW1WucSR4oei1vB8H`</summary>

```text
# Paper Summary

**Title:** "From Noise to Nuance: Enriching Subjective Data Annotation through Qualitative Analysis"

**Authors:** Ruyuan Wan, Haonan Wang, Ting-Hao Kenneth Huang, Jie Gao

**Abstract:** The work examines how subjective data annotation in NLP tasks (sentiment analysis, toxicity detection, bias identification) can be improved by integrating qualitative data analysis methods. Rather than dismissing disagreement among annotators as problematic, the authors propose treating it as "a meaningful source of knowledge."

## Key Findings

**Use of Qualitative Methods:** Yes. The paper explicitly performs a "comparative analysis of SDA and QDA methodologies," bridging subjective data annotation practices with established qualitative research approaches.

**Classification of Disagreement Types:** The abstract does not indicate specific disagreement typologies. Instead, the work focuses on methodological comparisons regarding "annotation schema, annotation workflow, annotator selection, and evaluation."

**Question Generation for Annotators:** No evidence in the provided content suggests the paper involves generating targeted questions to help annotators resolve disagreements. Rather, it proposes "five practical recommendations" based on the SDA-QDA comparison and demonstrates these through a reinforcement learning case study.

The approach treats annotator diversity as epistemologically valuable rather than seeking consensus resolution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b5333cc7-34f4-4d1b-a5c1-bf05f51beb13",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "e6b502d2-0ab6-4384-99c7-be9cf5ae9779",
  "sourceToolAssistantUUID": "b5333cc7-34f4-4d1b-a5c1-bf05f51beb13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-10T08:03:01.412Z_

<details><summary>↩ Tool result · `toolu_01Pc6ypTtC75T1GYnMigChmW`</summary>

```text
Web search results for query: ""annotator disagreement" "resolve" OR "resolution" "question" OR "probe" crowdsourcing NLP active learning 2025"

Links: [{"title":"\"NUTMEG: Separating Signal From Noise in Annotator Disagreement\" by Jonathan W. Ivey, Susan Gauch et al.","url":"https://scholarworks.uark.edu/dtscuht/14/"},{"title":"Learning from Disagreement: A Survey","url":"https://jair.org/index.php/jair/article/download/12752/26751/29240"},{"title":"Truth in Disagreement - Anca Dumitrache","url":"http://ancad.ro/phd.pdf"},{"title":"Design Choices for Crowdsourcing Implicit Discourse Relations: Revealing the Biases Introduced by Task Design | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00586/117215/Design-Choices-for-Crowdsourcing-Implicit"},{"title":"CrowdAgent: Multi-Agent Managed Multi-Source Annotation System","url":"https://arxiv.org/html/2509.14030v1"},{"title":"COLING 2025 Proceedings of CoMeDi: Context and Meaning—Navigating","url":"https://aclanthology.org/2025.comedi-1.pdf"},{"title":"Weak Ensemble Learning from Multiple Annotators for ...","url":"https://aclanthology.org/2025.nlperspectives-1.8.pdf"},{"title":"Enriching Subjective Data Annotation through Qualitative ...","url":"https://aclanthology.org/2025.hcinlp-1.20.pdf"},{"title":"A review and experimental analysis of active learning over crowdsourced data | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-021-10021-3"},{"title":"Understanding Crowdsourcing Algorithms for Multi-Annotator Data | PGW’s notes","url":"https://pengwei715.github.io/2025/07/01/crowdsoucing.html"}]

I've successfully completed the web search for your query on annotator disagreement, resolution, questions/probes, crowdsourcing, NLP, and active learning from 2025. Here are the key findings:

## Recent Research Highlights (2025)

**NUTMEG Model**: A new Bayesian model that incorporates information about annotator backgrounds to remove noisy annotations from human-labeled training data while preserving systematic disagreements.

**Active Learning Integration**: Active Learning (AL) allows the model to select the most valuable data for annotation, thereby significantly reducing the expensive human effort for annotation work.

**Disagreement as Signal**: Recent work has argued that for many tasks annotators may have genuine disagreements and that variation should be treated as signal rather than noise.

**CoMeDi Workshop**: A workshop exploring causes of disagreements in NLP annotations as well as strategies for effective handling or resolution. Participants were asked to predict the median of annotator judgments in one subtask and needed to predict the mean of pairwise absolute judgment differences between annotators in another.

**Multi-Agent Crowdsourcing**: Multi-agent systems emerge as a natural and powerful solution to intelligently control crowdsourcing processes, in order to assign tasks to the most suitable annotators under evolving conditions.

**Qualitative Enrichment**: Deeper meanings that often underlie annotator disagreements can be captured through subjective data annotation approaches.

The research emphasizes moving away from simply treating disagreement as noise, instead focusing on methods to preserve and understand systematic disagreements while filtering out true errors in crowdsourced NLP datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "299a1397-2ec3-447a-bfff-e690f661181e",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "a75de852-f889-4a8f-8742-28e088866363",
  "sourceToolAssistantUUID": "299a1397-2ec3-447a-bfff-e690f661181e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 113 · 2026-05-10T08:03:03.851Z_

I now have a comprehensive picture of the landscape. Let me do a few final targeted searches to make sure I haven't missed the most directly relevant work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a75de852-f889-4a8f-8742-28e088866363",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatYEcyPoLx3pEkJfmNBP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0adbf782-b768-491b-a54a-66c5c98a450e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WakNDCA5mzLWNpWpyL3QA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1480,
      "cache_read_input_tokens": 48677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1480,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-10T08:03:05.286Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SDbHVj89LuwiGLQRA3Sn2Z`</summary>

```json
{
  "query": "\"Annotator-Centric Active Learning\" EMNLP 2024 van der Meer Falk disagreement probe type"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0adbf782-b768-491b-a54a-66c5c98a450e",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatYEcyPoLx3pEkJfmNBP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dc6d666d-fd23-4433-b731-8449b910c1a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WakNDCA5mzLWNpWpyL3QA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1480,
      "cache_read_input_tokens": 48677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1480,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-10T08:03:05.562Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AhRDxp9ZGTQ1bzG4VwzEe3`</summary>

```json
{
  "query": "ACL 2025 findings annotation subjectivity disagreement \"soft label\" OR \"label distribution\" active probing elicitation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc6d666d-fd23-4433-b731-8449b910c1a1",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatYEcyPoLx3pEkJfmNBP",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f831b25-2888-46b0-9dec-1c7453bfc90f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WakNDCA5mzLWNpWpyL3QA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1480,
      "cache_read_input_tokens": 48677,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1480,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-10T08:03:12.682Z_

<details><summary>↩ Tool result · `toolu_01AhRDxp9ZGTQ1bzG4VwzEe3`</summary>

```text
Web search results for query: "ACL 2025 findings annotation subjectivity disagreement "soft label" OR "label distribution" active probing elicitation"

Links: [{"title":"Will Annotators Disagree? Identifying Subjectivity in Value-Laden Arguments - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.824/"},{"title":"Will Annotators Disagree? Identifying Subjectivity in Value- ...","url":"https://aclanthology.org/2025.findings-emnlp.824.pdf"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"Proceedings of the 19th Linguistic Annotation Workshop (LAW-XIX-2025) - ACL Anthology","url":"https://aclanthology.org/volumes/2025.law-1/"},{"title":"Enriching Subjective Data Annotation through Qualitative ...","url":"https://aclanthology.org/2025.hcinlp-1.20.pdf"},{"title":"Analysis, Insights, and Modelling from an Annotation ...","url":"https://aclanthology.org/2025.findings-acl.922.pdf"},{"title":"Learning with Annotator Disagreement in STS","url":"https://aclanthology.org/2025.emnlp-main.1800.pdf"},{"title":"Disentangling Subjectivity and Uncertainty for Hate Speech ...","url":"https://aclanthology.org/2025.emnlp-main.1460.pdf"},{"title":"Consistency is Key: Disentangling Label Variation in ...","url":"https://aclanthology.org/2025.nlperspectives-1.6.pdf"},{"title":"Measuring Label Ambiguity in Subjective Tasks using ...","url":"https://aclanthology.org/2025.law-1.2.pdf"}]

Based on my web search, I found several relevant papers from ACL 2025 Findings and related venues addressing annotation subjectivity, disagreement, and related methods:

## Key Papers Found

**1. Will Annotators Disagree? Identifying Subjectivity in Value-Laden Arguments**
This paper explores how aggregating multiple annotations into a single ground truth label may hide valuable insights into annotator disagreement, particularly in subjective tasks, and investigates methods for identifying subjectivity in recognizing human values that motivate arguments.

**2. Beyond Averages: Learning with Annotator Disagreement in STS (EMNLP 2025)**
This work uses soft-label training combined with temperature scaling to improve calibration and explores trade-offs between training with soft-label objectives versus applying post-hoc calibration.

**3. Disentangling Subjectivity and Uncertainty for Hate Speech Detection**
This paper addresses modeling annotator disagreement for subjective tasks.

**4. Measuring Label Ambiguity in Subjective Tasks using Predictive Uncertainty Estimation**
This paper addresses label ambiguity especially prevalent in subjective tasks, defining label ambiguity score as the entropy of the empirical probability distribution.

**5. Consistency is Key: Disentangling Label Variation with Intra-Annotator Agreement**
This workshop paper examines label variation in NLP with a focus on intra-annotator agreement measures.

These papers collectively address annotation subjectivity, disagreement quantification, soft labels/label distributions, and related methods for handling human label variation in ACL 2025 proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f831b25-2888-46b0-9dec-1c7453bfc90f",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "8db23a57-39d2-409f-986c-67f9cef5ad9b",
  "sourceToolAssistantUUID": "8f831b25-2888-46b0-9dec-1c7453bfc90f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-10T08:03:13.537Z_

<details><summary>↩ Tool result · `toolu_01SDbHVj89LuwiGLQRA3Sn2Z`</summary>

```text
Web search results for query: ""Annotator-Centric Active Learning" EMNLP 2024 van der Meer Falk disagreement probe type"

Links: [{"title":"Annotator-Centric Active Learning for Subjective NLP Tasks - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.1031/"},{"title":"Annotator-Centric Active Learning for Subjective NLP Tasks","url":"https://aclanthology.org/2024.emnlp-main.1031.pdf"},{"title":"[Quick Review] Annotator-Centric Active Learning for Subjective NLP Tasks","url":"https://liner.com/review/annotatorcentric-active-learning-for-subjective-nlp-tasks"},{"title":"Annotator-Centric Active Learning for Subjective NLP Tasks | Request PDF","url":"https://www.researchgate.net/publication/386197718_Annotator-Centric_Active_Learning_for_Subjective_NLP_Tasks"},{"title":"Annotator-Centric Active Learning for Subjective NLP Tasks","url":"https://arxiv.org/html/2404.15720v1/"},{"title":"Annotator-Centric active learning for subjective NLP tasks","url":"https://scholarlypublications.universiteitleiden.nl/access/item:4176718/view"},{"title":"Annotator-Centric Active Learning","url":"https://www.emergentmind.com/topics/annotator-centric-active-learning-acal"},{"title":"[2404.15720] Annotator-Centric Active Learning for Subjective NLP Tasks","url":"https://arxiv.org/abs/2404.15720"},{"title":"The 2024 Conference on Empirical Methods in Natural Language Processing - EMNLP 2024","url":"https://2024.emnlp.org/"},{"title":"dblp: EMNLP (Findings) 2024","url":"https://dblp.org/db/conf/emnlp/emnlp2024f.html"}]

Based on the search results, I found comprehensive information about the paper "Annotator-Centric Active Learning for Subjective NLP Tasks" from EMNLP 2024.

## Key Information:

**Paper Details:**
The paper "Annotator-Centric Active Learning for Subjective NLP Tasks" by Michiel van der Meer, Neele Falk, Pradeep K. Murukannaiah, and Enrico Liscio was published in the Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 18537–18555, Miami, Florida, USA.

**Main Contribution:**
The paper introduces Annotator-Centric Active Learning (ACAL), which incorporates an annotator selection strategy following data sampling.

**Objectives:**
The objectives are two-fold: (1) to efficiently approximate the full diversity of human judgments, and (2) to assess model performance using annotator-centric metrics, which value minority and majority perspectives equally.

**Annotator Selection Strategies:**
ACAL incorporates three novel annotator selection strategies, including random, label minority, and semantic diversity, to collect a balanced distribution of annotations.

**Key Findings:**
ACAL improves data efficiency and excels in annotator-centric performance evaluations. However, its success depends on the availability of a sufficiently large and diverse pool of annotators to sample from.

**Experimental Scope:**
The study experiments with multiple annotator selection strategies across seven subjective NLP tasks, employing both traditional and novel, human-centered evaluation metrics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc6d666d-fd23-4433-b731-8449b910c1a1",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "cb69f644-8339-417e-86ce-0cb6ad5c7d68",
  "sourceToolAssistantUUID": "dc6d666d-fd23-4433-b731-8449b910c1a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-10T08:03:17.129Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01E3EiUEbQqEXReXcTkd8YEK`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-main.1460/",
  "prompt": "Extract the title, authors, abstract, and key methods. Does this paper classify types of annotation disagreement - specifically distinguishing subjectivity from uncertainty? Does it relate to value divergence vs borderline threshold vs conceptual ambiguity? Does it involve probing annotators or generating clarification questions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb69f644-8339-417e-86ce-0cb6ad5c7d68",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatYFWqpziQxb8JypHBmf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aa2db15d-0eb6-45fe-a2a4-0cf02c415507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MJcFmyRFG1vAkoz7Hn51uK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 900,
      "cache_creation_input_tokens": 1212,
      "cache_read_input_tokens": 50157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1212,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 58,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-10T08:03:17.971Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0117PXpEkLGBQjy59MKmLYzJ`</summary>

```json
{
  "url": "https://aclanthology.org/2025.law-1.2/",
  "prompt": "Extract the title, authors, abstract, and key methods. Does this paper propose a method for measuring label ambiguity or classifying disagreement types? Does it relate to borderline threshold cases vs conceptual ambiguity? Does it involve probing annotators?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa2db15d-0eb6-45fe-a2a4-0cf02c415507",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatYFWqpziQxb8JypHBmf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "202ac693-d4c8-42fa-9786-a49b5be8e822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MJcFmyRFG1vAkoz7Hn51uK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 900,
      "cache_creation_input_tokens": 1212,
      "cache_read_input_tokens": 50157,
      "output_tokens": 275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1212
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 900,
          "output_tokens": 275,
          "cache_read_input_tokens": 50157,
          "cache_creation_input_tokens": 1212,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1212,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-10T08:03:21.583Z_

<details><summary>↩ Tool result · `toolu_01E3EiUEbQqEXReXcTkd8YEK`</summary>

```text
# Paper Analysis

**Title:** "Disentangling Subjectivity and Uncertainty for Hate Speech Annotation and Modeling using Gaze"

**Authors:** Özge Alacam, Sanne Hoeken, Andreas Säuberli, Hannes Gröner, Diego Frassinelli, Sina Zarrieß, Barbara Plank

**Abstract Summary:** The paper examines variation in opinion-based annotation tasks, distinguishing between genuine disagreement and uncertainty using annotator confidence ratings.

## Classification of Annotation Disagreement

**Yes** — this paper explicitly addresses your core question. The authors state their goal is to "establish distinctive dimensions of variation which are often not clearly separated in existing work on modeling annotator variation." They differentiate between:
- **Subjectivity:** Genuine differences in opinion shaped by background, experience, and culture
- **Uncertainty:** Confusion or ambiguity affecting annotation decisions

## Key Methods

The research employs:
- **Confidence ratings** from annotators to disentangle subjective variation from uncertainty
- **Gaze tracking** to identify behavioral indicators of subjective evaluation and uncertainty
- **Hate speech detection task** as the empirical application domain

The authors demonstrate that "models are affected differently by instances of uncertainty and subjectivity," suggesting these dimensions have distinct modeling implications.

## Scope Limitations

The abstract does not indicate whether the work involves clarification question generation or direct annotator probing beyond confidence collection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa2db15d-0eb6-45fe-a2a4-0cf02c415507",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "9bc2f595-9c96-4a01-81db-5518c5991148",
  "sourceToolAssistantUUID": "aa2db15d-0eb6-45fe-a2a4-0cf02c415507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-10T08:03:21.880Z_

<details><summary>↩ Tool result · `toolu_0117PXpEkLGBQjy59MKmLYzJ`</summary>

```text
# Paper Summary

**Title:** "Measuring Label Ambiguity in Subjective Tasks using Predictive Uncertainty Estimation"

**Authors:** Richard Alies, Elena Merdjanovska, Alan Akbik

**Abstract:** The paper addresses how "Human annotations in natural language corpora vary due to differing human perspectives" particularly in subjective annotation tasks, focusing on identifying "data samples [that] are more prone to label variation."

## Analysis

**Method for measuring ambiguity:** Yes, the paper proposes using predictive uncertainty estimation as the core methodology for quantifying label ambiguity.

**Classifying disagreement types:** The provided content does not specify whether the approach distinguishes between different disagreement categories.

**Borderline vs. conceptual ambiguity:** The abstract does not differentiate between these ambiguity sources—it broadly addresses samples exhibiting "label variation."

**Annotator probing:** No evidence in the available content suggests the method involves directly probing or surveying annotators about their decision-making processes.

The paper appears to be a computational approach using model uncertainty to identify problematic annotations, rather than an annotation study examining why disagreement occurs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "202ac693-d4c8-42fa-9786-a49b5be8e822",
  "isSidechain": true,
  "promptId": "7c8dbae0-8255-45de-9522-53b207466c0d",
  "agentId": "a353a15cb7baef652",
  "type": "user",
  "uuid": "66c5cd6d-3bd3-4ed4-9f5d-099f70eba859",
  "sourceToolAssistantUUID": "202ac693-d4c8-42fa-9786-a49b5be8e822",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 122 · 2026-05-10T08:04:20.529Z_

I now have a thorough picture of the relevant literature. Let me compile the final report.

---

Here is a comprehensive survey of recent papers (2024-2026) with potential overlap with DART's core approach. I have organized them by degree of relevance.

---

## Papers with Direct Overlap with DART

### 1. "Disentangling Subjectivity and Uncertainty for Hate Speech Annotation and Modeling using Gaze"
**Authors:** Özge Alacam, Sanne Hoeken, Andreas Säuberli, Hannes Gröner, Diego Frassinelli, Sina Zarrieß, Barbara Plank
**Venue:** EMNLP 2025 (Main)
**Overlap with DART:** This paper is the closest match to DART's disagrement-typing component. It explicitly proposes distinguishing *subjectivity* (genuine value-based opinion differences across annotators) from *uncertainty* (confusion or ambiguity in the item itself), and demonstrates that models behave differently depending on which type is present. This directly parallels DART's distinction between value divergence and conceptual/borderline ambiguity. It uses annotator confidence ratings and gaze tracking rather than generated probes, and does not do active resolution, but the typological framing is highly overlapping.

---

### 2. "Structured Disagreement in Health-Literacy Annotation: Epistemic Stability, Conceptual Difficulty, and Agreement-Stratified Inference"
**Authors:** Olga Kellert, Sriya Kondury, Candice Koo, Nemika Tyagi, Steffen Eikenberry
**Venue:** arXiv:2604.19943 (April 2026; no venue listed, appears to be a preprint)
**Overlap with DART:** This paper argues for decomposing annotation disagreement into epistemically stable components (items that are reliably annotated) versus items exhibiting conceptual difficulty (task-level complexity that drives annotator variance). It finds that question-level conceptual difficulty accounts for 33% of rating variance while annotator identity accounts for only 1%, and shows that aggregating across these strata reverses scientific conclusions. This maps closely onto DART's borderline-threshold vs. conceptual-ambiguity distinction, though it does not involve active probe generation and instead uses variance decomposition post hoc.

---

### 3. "Beyond Black-Box Labels: Interpretable Criteria for Diagnosing Subjective NLP Tasks"
**Authors:** Nisrine Rair, Alban Goupil, Valeriu Vrabie, Emmanuel Chochoy
**Venue:** ACL Findings 2026 (arXiv:2604.17022)
**Overlap with DART:** This paper conducts schema-level diagnostics before gold-label creation, using multi-annotator criterion judgments to identify whether disagreement reflects *unstable criteria* (unclear decision boundaries, analogous to DART's borderline threshold type) or *category overlap* (criteria that are each clear but simultaneously applicable — closer to DART's conceptual ambiguity). It finds disagreement concentrates in a small number of criteria and shows nearly half of covered sentences activate multiple categories simultaneously. There is no probe generation or active resolution loop, but the diagnostic framing of "what type of criterion failure drives this disagreement" is a strong conceptual parallel.

---

### 4. "From Disagreement to Understanding: The Case for Ambiguity Detection in NLI"
**Authors:** Chathuri Jayaweera, Bonnie J. Dorr
**Venue:** 4th Workshop on Perspectivist Approaches to NLP (NLPerspectives), EMNLP 2025
**Overlap with DART:** A position paper arguing that NLI annotation disagreement is not noise but signals meaningful ambiguity types. The authors present a unified taxonomy synthesizing existing NLI ambiguity taxonomies and propose an ambiguity-first annotation pipeline in which ambiguity is detected and classified before labels are assigned. The call for new annotated resources and classifiers targeting specific ambiguity subtypes is very close in spirit to DART's type-conditioned clarification approach, though no probe generation system is implemented.

---

### 5. "NUTMEG: Separating Signal From Noise in Annotator Disagreement"
**Authors:** Jonathan Ivey, Susan Gauch, David Jurgens
**Venue:** EMNLP 2025 (Main), pages 2874–2887
**Overlap with DART:** NUTMEG is a Bayesian model that uses annotator background information to partition disagreements into *systematic signal* (genuine perspectival differences worth preserving) and *noise* (low-competence errors to discard). While it does not further classify the types of systematic disagreement (value divergence, conceptual ambiguity, borderline threshold), it directly addresses the foundational step that DART depends on — separating disagreements worth resolving from those worth preserving. It then re-trains on the filtered label distribution, which overlaps with DART's soft-label training update step.

---

### 6. "Beyond Consensus: Perspectivist Modeling and Evaluation of Annotator Disagreement in NLP" (Survey)
**Authors:** Yinuo Xu, David Jurgens
**Venue:** arXiv:2601.09065 (January 2026; survey paper)
**Overlap with DART:** This is a broad survey presenting a domain-agnostic taxonomy of disagreement sources organized across data factors, task factors, and annotator factors, and synthesizing modeling approaches. It explicitly advocates for a shift from consensus aggregation toward structured disagreement modeling. The taxonomy is less fine-grained than DART's three-type split (the survey categories are higher-level), and there is no discussion of probe generation. This is likely to be cited as a framing reference by DART reviewers and should be cited in the proposal.

---

## Papers with Partial Overlap

### 7. "Will Annotators Disagree? Identifying Subjectivity in Value-Laden Arguments"
**Authors:** Amir Homayounirad, Enrico Liscio, Tong Wang, Catholijn M Jonker, Luciano Cavalcante Siebert
**Venue:** Findings of EMNLP 2025 (arXiv:2509.06704)
**Overlap with DART:** Directly addresses DART's "value divergence" disagreement type by predicting whether annotation of arguments containing human values will be subjective. It contrasts value prediction (inferring subjectivity from the label itself) with direct subjectivity identification and finds the direct method works better. It does not classify other disagreement types, does not generate probes, and does not update training distributions, but it confirms that value-laden disagreements form a tractable detection target.

### 8. "Annotator-Centric Active Learning for Subjective NLP Tasks" (ACAL)
**Authors:** Michiel van der Meer, Neele Falk, Pradeep K. Murukannaiah, Enrico Liscio
**Venue:** EMNLP 2024 (Main), pages 18537–18555
**Overlap with DART:** ACAL is the closest existing work to DART's active learning component. It combines active data selection with active annotator selection, targeting diversity of perspectives rather than consensus, and evaluates using annotator-centric metrics that weight minority and majority views equally. However, it selects who to ask rather than what to ask — it does not generate type-conditioned probes or classify what kind of disagreement has occurred. DART's novelty over ACAL lies precisely in the probe-generation and type-conditioning steps.

### 9. "Revisiting Active Learning under (Human) Label Variation"
**Authors:** Cornelia Gruber, Helen Alber, Bernd Bischl, Göran Kauermann, Barbara Plank, Matthias Aßenmacher
**Venue:** arXiv:2507.02593 (July 2025)
**Overlap with DART:** A conceptual framework distinguishing human label variation (legitimate disagreement worth preserving as signal) from label noise (error to be discarded) within active learning workflows. It covers instance selection, annotator selection, label representation, and LLM integration. Like NUTMEG, it covers the signal/noise split foundational to DART but does not taxonomize types of signal disagreement or generate clarification probes.

### 10. "Automating Annotation Guideline Improvements using LLMs: A Case Study"
**Authors:** Adrien Bibal et al.
**Venue:** CoMeDi Workshop at COLING 2025
**Overlap with DART:** This paper uses LLMs to iteratively improve annotation guidelines and achieves substantial IAA gains (0.593 → 0.84 on WNUT-17). This is related to DART's probe generation step in that it uses an LLM to generate guideline clarifications in response to observed disagreements, but it targets guideline text rather than individual annotators, and it does not classify disagreement types before generating clarifications.

### 11. "Conflicts in Texts: Data, Implications and Challenges"
**Authors:** Siyi Liu and Dan Roth
**Venue:** arXiv:2504.19472 (April 2025)
**Overlap with DART:** Provides a taxonomy distinguishing disagreements rooted in linguistic ambiguity, annotator bias, and task design. The distinction between semantic/linguistic ambiguity (≈ DART's conceptual ambiguity) and value-driven annotator disagreement (≈ DART's value divergence) is present but not operationalized for active resolution or probe generation.

---

## Notable Absence: No Direct Precedent for DART's Full Pipeline

Across all searches covering EMNLP 2025, ACL 2025, EACL 2026, CoMeDi 2025, NLPerspectives 2025, and arXiv cs.CL through May 2026, **no paper was found that combines all three of DART's core steps**: (1) classifying a specific disagreement into a type (conceptual ambiguity vs. value divergence vs. borderline threshold), (2) generating type-conditioned clarification probes sent back to the original disagreeing annotators, and (3) using probe responses to update soft-label training distributions. Papers address one or two of these steps but not the full closed-loop pipeline.

The most important overlap risk for reviewers to flag is likely papers 1 (Alacam et al., EMNLP 2025) for the typing step and paper 8 (ACAL, EMNLP 2024) for the active loop step. DART should clearly differentiate itself from both.

---

Sources:
- [CARE: Disagreement Detection Framework – EMNLP 2025](https://aclanthology.org/2025.emnlp-main.671/)
- [Beyond Consensus: Perspectivist Modeling – arXiv:2601.09065](https://arxiv.org/abs/2601.09065)
- [From Disagreement to Understanding: NLI Ambiguity Detection – NLPerspectives 2025](https://aclanthology.org/2025.nlperspectives-1.4/)
- [NUTMEG: Separating Signal From Noise – EMNLP 2025](https://aclanthology.org/2025.emnlp-main.144/)
- [Will Annotators Disagree? Value-Laden Arguments – EMNLP Findings 2025](https://aclanthology.org/2025.findings-emnlp.824/)
- [Disentangling Subjectivity and Uncertainty – EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1460/)
- [Beyond Black-Box Labels: Interpretable Criteria – ACL Findings 2026](https://arxiv.org/abs/2604.17022)
- [Structured Disagreement in Health-Literacy Annotation – arXiv:2604.19943](https://arxiv.org/abs/2604.19943)
- [Annotator-Centric Active Learning – EMNLP 2024](https://aclanthology.org/2024.emnlp-main.1031/)
- [Revisiting Active Learning under Label Variation – arXiv:2507.02593](https://arxiv.org/abs/2507.02593)
- [Conflicts in Texts: Data, Implications and Challenges – arXiv:2504.19472](https://arxiv.org/abs/2504.19472)
- [Automating Annotation Guideline Improvements – CoMeDi 2025](https://aclanthology.org/2025.comedi-1.13/)
- [CoMeDi Workshop Proceedings – COLING 2025](https://aclanthology.org/2025.comedi-1/)
- [Can Reasoning Help LLMs Capture Annotator Disagreement? – EACL 2026](https://aclanthology.org/2026.eacl-long.3/)
- [Measuring Label Ambiguity using Predictive Uncertainty – LAW 2025](https://aclanthology.org/2025.law-1.2/)
- [Learning with Annotator Disagreement in STS – EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1800/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66c5cd6d-3bd3-4ed4-9f5d-099f70eba859",
  "isSidechain": true,
  "agentId": "a353a15cb7baef652",
  "requestId": "req_011CatYG8Ux7VuRgBAdAG2fg",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0b0a11a-520d-4040-8109-5719a304a19e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7ac167d0-b69c-4418-a1b0-da73321aa61d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015pCExrV2RrQHxRSohsTtnQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1817,
      "cache_read_input_tokens": 51369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1817,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---
