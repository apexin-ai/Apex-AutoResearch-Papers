# Research conversation: You are helping build a related work section for a paper about "Embedding Alignment Gap" — where submodular-based divers

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-af5811deecee9942b.jsonl`
- **Structured JSON:** [`5d84761d05d8f7921a8a.json`](../../sessions/5d/5d84761d05d8f7921a8a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-13T18:32:28.142Z_

You are helping build a related work section for a paper about "Embedding Alignment Gap" — where submodular-based diversity selection on internal embeddings fails because the embedding space degrades during iterative self-training.

Your task: Search and verify papers in "Submodular Maximization for Data Selection".

**Seed papers to verify:**
1. Iyer & Bilmes (2013) - submodular optimization for data subset selection (search: "Iyer Bilmes 2013 submodular optimization")
2. Wei et al. (2015) - submodularity in data subset selection (search: "Wei Bilmes 2015 submodularity data subset selection machine learning")

For EACH, use WebSearch to find: exact title, all authors, year, venue.

Then search for 1-2 ADDITIONAL papers on submodular optimization for data selection, facility location for coreset selection, or submodular functions in active learning/data pruning (preferably 2018+). Verify each.

**Output format:**
PAPER: [Author et al. (Year)] "Exact Title" — Venue
VERIFIED: Yes/No
RELEVANCE: One sentence connecting to diversity-based data selection using embedding geometry

List all papers numbered.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "cb9d95fc-9c2d-4329-a2e0-19f7dffc3a15",
  "agentId": "af5811deecee9942b",
  "type": "user",
  "uuid": "0a9f8f9a-6fef-401d-8a8e-7d94ebcceba8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-13T18:32:28.145Z_

```json
{
  "parentUuid": "0a9f8f9a-6fef-401d-8a8e-7d94ebcceba8",
  "isSidechain": true,
  "agentId": "af5811deecee9942b",
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
      "mcp__agent-ml-research__append_idea",
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
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "66d5afaa-6ba0-4db1-bb10-5f805c5f17eb",
  "timestamp": "2026-05-13T18:32:28.145Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-13T18:32:30.790Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Nkpmd53Gy9enLuNjNCrRpE`</summary>

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
  "parentUuid": "66d5afaa-6ba0-4db1-bb10-5f805c5f17eb",
  "isSidechain": true,
  "agentId": "af5811deecee9942b",
  "requestId": "req_011Cb13fKMase9NNrNMKG7gB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9e278550-6f8b-46e6-8011-329d61cb1c26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016iU2FkrCamz28F7Xbqj2Gt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6087,
      "cache_read_input_tokens": 8112,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6087
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 76,
          "cache_read_input_tokens": 8112,
          "cache_creation_input_tokens": 6087,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6087,
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

_source line 4 · 2026-05-13T18:32:30.792Z_

<details><summary>↩ Tool result · `toolu_01Nkpmd53Gy9enLuNjNCrRpE`</summary>

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
  "parentUuid": "9e278550-6f8b-46e6-8011-329d61cb1c26",
  "isSidechain": true,
  "promptId": "cb9d95fc-9c2d-4329-a2e0-19f7dffc3a15",
  "agentId": "af5811deecee9942b",
  "type": "user",
  "uuid": "f9f99055-7e19-4ab4-a059-5b28607e8957",
  "sourceToolAssistantUUID": "9e278550-6f8b-46e6-8011-329d61cb1c26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-13T18:32:32.740Z_

I'll search for all four papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9f99055-7e19-4ab4-a059-5b28607e8957",
  "isSidechain": true,
  "agentId": "af5811deecee9942b",
  "requestId": "req_011Cb13fWyayod8RRu4kgGFc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "66697385-7309-48c3-a341-589ee37f513f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XnQteEywsJCtrNqBz2NHvV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 6 · 2026-05-13T18:32:33.190Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LAJmghjQTYwuifXft2dcdd`</summary>

```json
{
  "query": "Iyer Bilmes 2013 submodular optimization data subset selection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66697385-7309-48c3-a341-589ee37f513f",
  "isSidechain": true,
  "agentId": "af5811deecee9942b",
  "requestId": "req_011Cb13fWyayod8RRu4kgGFc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e3d03e71-3cd2-418c-b798-88b263578088",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XnQteEywsJCtrNqBz2NHvV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 7 · 2026-05-13T18:32:34.051Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015Ft24VkvQfCu7fheLgLjpX`</summary>

```json
{
  "query": "Wei Bilmes 2015 submodularity data subset selection machine learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3d03e71-3cd2-418c-b798-88b263578088",
  "isSidechain": true,
  "agentId": "af5811deecee9942b",
  "requestId": "req_011Cb13fWyayod8RRu4kgGFc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "306cd80a-7d8e-4170-a33a-25b39b7475da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XnQteEywsJCtrNqBz2NHvV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 8 · 2026-05-13T18:32:34.908Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QNE2PrtkooXqa59uJaxRPQ`</summary>

```json
{
  "query": "facility location coreset selection submodular 2018 2019 2020 data pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "306cd80a-7d8e-4170-a33a-25b39b7475da",
  "isSidechain": true,
  "agentId": "af5811deecee9942b",
  "requestId": "req_011Cb13fWyayod8RRu4kgGFc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ac53370-2cc7-4b90-a3fe-93a154ec3278",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XnQteEywsJCtrNqBz2NHvV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 9 · 2026-05-13T18:32:35.120Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S6NJnUdK2C3i6aj3uWvm88`</summary>

```json
{
  "query": "submodular active learning data selection embedding 2019 2020 2021 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ac53370-2cc7-4b90-a3fe-93a154ec3278",
  "isSidechain": true,
  "agentId": "af5811deecee9942b",
  "requestId": "req_011Cb13fWyayod8RRu4kgGFc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "294b00aa-97f5-4915-a2d9-0ba550459c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01XnQteEywsJCtrNqBz2NHvV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14199,
      "output_tokens": 239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1439
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 239,
          "cache_read_input_tokens": 14199,
          "cache_creation_input_tokens": 1439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1439,
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

_source line 10 · 2026-05-13T18:32:39.277Z_

<details><summary>↩ Tool result · `toolu_01LAJmghjQTYwuifXft2dcdd`</summary>

```text
Web search results for query: "Iyer Bilmes 2013 submodular optimization data subset selection"

Links: [{"title":"Rishabh Iyer - Research","url":"https://sites.google.com/view/rishabhiyer/research"},{"title":"Submodularity in data subset selection and active learning | Proceedings of the 32nd International Conference on Machine Learning - Volume 37","url":"https://dl.acm.org/doi/10.5555/3045118.3045326"},{"title":"Submodularity in Data Subset Selection and Active Learning","url":"https://proceedings.mlr.press/v37/wei15.html"},{"title":"[1311.2106] Submodular Optimization with Submodular Cover and Submodular Knapsack Constraints","url":"https://arxiv.org/abs/1311.2106"},{"title":"[PDF] Submodularity in Data Subset Selection and Active Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Submodularity-in-Data-Subset-Selection-and-Active-Wei-Iyer/afdb6b7a083e3b7304c354925a3f3528716cb44e"},{"title":"Bilmes and Iyer Win Best Paper at the 2013 Neural Information Processing Systems Conference | UW Department of Electrical & Computer Engineering","url":"https://www.ece.uw.edu/spotlight/bilmes-and-iyer-win-best-paper-at-the-2013-neural-information-processing-systems-conference/"},{"title":"On Fine-Tuning Submodular Functions for Data Subset Selection","url":"https://digital.lib.washington.edu/bitstreams/38c03838-ca8b-4ad2-a595-165fbe0155ee/download"},{"title":"Submodularity for Data Selection in Statistical Machine Translation","url":"https://people.ece.uw.edu/bilmes/p/mypubs/kirchhoff2014-submodmt.pdf"},{"title":"Submodularity in Data Subset Selection and Active Learning Kai Wei","url":"https://proceedings.mlr.press/v37/wei15.pdf"},{"title":"Submodular Optimization with Submodular Cover and Submodular Knapsack Constraints","url":"https://papers.nips.cc/paper/4911-submodular-optimization-with-submodular-cover-and-submodular-knapsack-constraints"}]

I've found relevant research related to your query. Here are the key findings:

## Iyer and Bilmes 2013 Work on Submodular Optimization

Rishabh Iyer and Jeff Bilmes published multiple papers in 2013 on submodular optimization topics including "Submodular optimization with submodular cover and submodular knapsack constraints" at NIPS 2013 (which won an Outstanding Paper Award).

This work investigated two optimization problems — minimizing a submodular function subject to a submodular lower bound constraint (submodular cover) and maximizing a submodular function subject to a submodular upper bound constraint (submodular knapsack), motivated by real-world applications including sensor placement and data subset selection.

## Data Subset Selection Applications

While the main 2013 papers focused on the optimization framework itself, subsequent work by Wei, Iyer, and Bilmes in 2015 addressed submodularity in data subset selection and active learning at ICML. This work showed the connection of submodularity to data likelihood functions for Naive Bayes and Nearest Neighbor classifiers, formulated data subset selection problems as constrained submodular maximization, and proposed a filtering active submodular selection (FASS) scheme combining uncertainty sampling with submodular data subset selection.

The research demonstrates how submodular optimization provides a principled framework for selecting representative data subsets while maintaining model performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e3d03e71-3cd2-418c-b798-88b263578088",
  "isSidechain": true,
  "promptId": "cb9d95fc-9c2d-4329-a2e0-19f7dffc3a15",
  "agentId": "af5811deecee9942b",
  "type": "user",
  "uuid": "3eb44862-2554-4d4f-bb8d-1a9a91708458",
  "sourceToolAssistantUUID": "e3d03e71-3cd2-418c-b798-88b263578088",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T18:32:39.331Z_

<details><summary>↩ Tool result · `toolu_015Ft24VkvQfCu7fheLgLjpX`</summary>

```text
Web search results for query: "Wei Bilmes 2015 submodularity data subset selection machine learning"

Links: [{"title":"Submodularity in Data Subset Selection and Active Learning","url":"https://proceedings.mlr.press/v37/wei15.html"},{"title":"Submodularity in data subset selection and active learning | Proceedings of the 32nd International Conference on Machine Learning - Volume 37","url":"https://dl.acm.org/doi/10.5555/3045118.3045326"},{"title":"Jeff A. Bilmes Homepage","url":"https://people.ece.uw.edu/bilmes/p/pgs/b2hd-wei2015-submodular-data-active.html"},{"title":"dblp: Submodularity in Data Subset Selection and Active Learning.","url":"https://dblp.org/rec/conf/icml/WeiIB15.html"},{"title":"[PDF] Submodularity in Data Subset Selection and Active Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Submodularity-in-Data-Subset-Selection-and-Active-Wei-Iyer/afdb6b7a083e3b7304c354925a3f3528716cb44e"},{"title":"Submodularity in Data Subset Selection and Active Learning Kai Wei","url":"https://proceedings.mlr.press/v37/wei15.pdf"},{"title":"Rishabh Iyer - Research","url":"https://sites.google.com/view/rishabhiyer/research"},{"title":"Submodularity in Data Subset Selection and Active Learning","url":"https://videolectures.net/videos/icml2015_wei_submodularity"},{"title":"CARAML Lab - Publications","url":"https://www.caraml-lab.com/publications/"},{"title":"Rishabh Iyer's Webpage","url":"https://rishabhk108.github.io/"}]

I found the paper you're looking for! Here's a summary of the search results:

The paper "Submodularity in Data Subset Selection and Active Learning" was authored by Kai Wei, Rishabh Iyer, and Jeff Bilmes and was published at the International Conference on Machine Learning (ICML) in Lille, France in 2015.

The paper shows the connection of submodularity to the data likelihood functions for Naive Bayes (NB) and Nearest Neighbor (NN) classifiers, and formulates the data subset selection problems for these classifiers as constrained submodular maximization.

Furthermore, the authors apply this framework to active learning and propose a novel scheme called filtering active submodular selection (FASS), where they combine the uncertainty sampling method with a submodular data subset selection framework.

The paper extensively evaluates the proposed framework on text categorization and handwritten digit recognition tasks with four different classifiers, including Deep Neural Network (DNN) based classifiers, with empirical results indicating significant improvement over state-of-the-art algorithms.

The paper is available at the Proceedings of Machine Learning Research (PMLR) website and has been widely cited in subsequent research on submodular optimization for machine learning applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "306cd80a-7d8e-4170-a33a-25b39b7475da",
  "isSidechain": true,
  "promptId": "cb9d95fc-9c2d-4329-a2e0-19f7dffc3a15",
  "agentId": "af5811deecee9942b",
  "type": "user",
  "uuid": "532d3c88-ba19-4883-9b3d-ac7b957fe79f",
  "sourceToolAssistantUUID": "306cd80a-7d8e-4170-a33a-25b39b7475da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T18:32:42.014Z_

<details><summary>↩ Tool result · `toolu_01QNE2PrtkooXqa59uJaxRPQ`</summary>

```text
Web search results for query: "facility location coreset selection submodular 2018 2019 2020 data pruning"

Links: [{"title":"A Coreset Selection of Coreset Selection Literature: Introduction and Recent Advances","url":"https://arxiv.org/html/2505.17799v1"},{"title":"SubZeroCore: A Submodular Approach with Zero Training for Coreset Selection","url":"https://arxiv.org/html/2509.21748"},{"title":"(PDF) SubZeroCore: A Submodular Approach with Zero Training for Coreset Selection","url":"https://www.researchgate.net/publication/395944227_SubZeroCore_A_Submodular_Approach_with_Zero_Training_for_Coreset_Selection"},{"title":"1 A Coreset Selection of Coreset Selection Literature:","url":"https://arxiv.org/pdf/2505.17799"},{"title":"Active Learning is a Strong Baseline for Data Subset Selection","url":"https://openreview.net/pdf?id=PAgpyQ5rGS"},{"title":"SubZeroCore: Unified Coreset Selection","url":"https://www.emergentmind.com/topics/core-reference-set"},{"title":"GLISTER: Generalization based Data Subset Selection for Efﬁcient and Robust","url":"https://www.cse.iitb.ac.in/~ganesh/papers/aaai2021.pdf"},{"title":"GitHub - PatrickZH/DeepCore: Code for coreset selection methods · GitHub","url":"https://github.com/PatrickZH/DeepCore"},{"title":"Coresets for Data-efﬁcient Training of Machine Learning Models","url":"https://cs.stanford.edu/people/jure/pubs/craig-icml20.pdf"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf/e791fa328e06b73e4668b27df0ca04c49e8b5cb4.pdf"}]

Here are the search results for your query on facility location, coreset selection, submodular functions, and data pruning from 2018-2020 and recent work:

## Key Findings:

**Core Concepts:**
Facility Location is a common submodular function used in coreset selection that maximizes coverage, along with other functions like Graph Cut and Log Determinant which measure the diversity of information.

**Notable Methods:**

1. **CRAIG (2020):** Uses a submodular facility location function for coreset selection. This gradient-matching approach formulates the problem as a facility location optimization problem.

2. **GLISTER:** Offers variants including F-GLISTER with Facility Location as a regularizer, and D-GLISTER with diversity regularization for active learning.

3. **Submodular Optimization:** Submodular functions can be efficiently maximized using a greedy algorithm, which provides a (1-1/e) ≈ 63% approximation guarantee for cardinality-constrained maximization.

**Recent Advances (2025):**

SubZeroCore is a training-free coreset selection method that integrates submodular coverage and density into a unified objective, and despite no training, matches training-based baselines and significantly outperforms them at high pruning rates.

**Data Pruning Context:**
Many attempts have been devoted to prune the training dataset to enable efficient learning, with data subset selection aiming to reduce the size of training sets by finding a core subset that generalizes on par with the full training set.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ac53370-2cc7-4b90-a3fe-93a154ec3278",
  "isSidechain": true,
  "promptId": "cb9d95fc-9c2d-4329-a2e0-19f7dffc3a15",
  "agentId": "af5811deecee9942b",
  "type": "user",
  "uuid": "0b7a763e-a53e-43f0-8e71-997b6fa1cd29",
  "sourceToolAssistantUUID": "9ac53370-2cc7-4b90-a3fe-93a154ec3278",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T18:32:42.398Z_

<details><summary>↩ Tool result · `toolu_01S6NJnUdK2C3i6aj3uWvm88`</summary>

```text
Web search results for query: "submodular active learning data selection embedding 2019 2020 2021 2022"

Links: [{"title":"Data Source Selection in Federated Learning: A Submodular Optimization Approach | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-00126-0_43"},{"title":"STENCIL: Submodular Mutual Information Based Weak Supervision for Cold-Start Active Learning","url":"https://arxiv.org/html/2402.13468"},{"title":"Active Learning is a Strong Baseline for Data Subset Selection","url":"https://openreview.net/pdf?id=PAgpyQ5rGS"},{"title":"Submodularity in Data Subset Selection and Active Learning Kai Wei","url":"https://proceedings.mlr.press/v37/wei15.pdf"},{"title":"Submodular Information Measures Based Active Learning ...","url":"https://arxiv.org/pdf/2107.00717"},{"title":"Learning From Less Data: A Unified Data Subset Selection and Active Learning Framework for Computer Vision | Request PDF","url":"https://www.researchgate.net/publication/331591266_Learning_From_Less_Data_A_Unified_Data_Subset_Selection_and_Active_Learning_Framework_for_Computer_Vision"},{"title":"[PDF] Submodularity in Data Subset Selection and Active Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Submodularity-in-Data-Subset-Selection-and-Active-Wei-Iyer/afdb6b7a083e3b7304c354925a3f3528716cb44e"},{"title":"(PDF) Submodularity-Inspired Data Selection for Goal-Oriented Chatbot Training Based on Sentence Embeddings","url":"https://www.researchgate.net/publication/322929407_Submodularity-inspired_Data_Selection_for_Goal-oriented_Chatbot_Training_based_on_Sentence_Embeddings"},{"title":"Submodularity in data subset selection and active learning | Proceedings of the 32nd International Conference on Machine Learning - Volume 37","url":"https://dl.acm.org/doi/10.5555/3045118.3045326"},{"title":"SIMILAR: Submodular Information Measures Based Active Learning In Realistic Scenarios | Request PDF","url":"https://www.researchgate.net/publication/353054510_SIMILAR_Submodular_Information_Measures_Based_Active_Learning_In_Realistic_Scenarios"}]

I've successfully retrieved search results for your query on submodular active learning and data selection with embeddings from 2019-2022. Here are the key findings:

## Recent Research Highlights

**Submodular Information Measures in Active Learning**

A notable 2019 work by Iyer & Bilmes presented a memoization framework for scaling submodular optimization to large scale problems at the 22nd International Conference on Artificial Intelligence and Statistics. Building on this foundation, Kothawade et al. (2021) introduced SIMILAR: Submodular Information Measures Based Active Learning in Realistic Scenarios.

**Cold-Start Active Learning with Weak Supervision**

STENCIL (2024) presents a submodular mutual information-based weak supervision approach for cold-start active learning that effectively utilizes prior knowledge through exemplar sets.

**Data Source Selection in Federated Learning**

Recent work (2022) proves that data source selection in federated learning is a monotone submodular maximization problem and proposes FDSS, an efficient algorithm with constant approximate ratio.

**General Framework Applications**

SIMILAR uses submodular information measures as acquisition functions and extends to realistic settings like class imbalance and out-of-distribution data, functioning as a scalable solution for active learning on large real-world datasets.

**Core Theory**

Submodular functions like facility location, log determinant, and graph cut are widely recognized for modeling diversity, with successful applications in summarization, curriculum learning, active learning, and subset selection.

The search results demonstrate significant progress in combining submodular optimization with active learning and embedding-based approaches between 2019-2022, particularly for handling realistic scenarios like class imbalance and noisy data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "294b00aa-97f5-4915-a2d9-0ba550459c44",
  "isSidechain": true,
  "promptId": "cb9d95fc-9c2d-4329-a2e0-19f7dffc3a15",
  "agentId": "af5811deecee9942b",
  "type": "user",
  "uuid": "5e848ec0-ce29-461c-ab10-c9ff4b8b9270",
  "sourceToolAssistantUUID": "294b00aa-97f5-4915-a2d9-0ba550459c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-13T18:32:45.760Z_

Now let me get more details on the CRAIG paper and SIMILAR paper as strong additional candidates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e848ec0-ce29-461c-ab10-c9ff4b8b9270",
  "isSidechain": true,
  "agentId": "af5811deecee9942b",
  "requestId": "req_011Cb13gNYrRHeUPEaDyChAn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db4d99b2-32d8-40b4-81ad-6c3ad0967551",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KJ4HHjUujsEf141wzztQYR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4006,
      "cache_read_input_tokens": 15638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4006,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 15 · 2026-05-13T18:32:46.640Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JosdeXZNHJmk8YVc6YywgG`</summary>

```json
{
  "query": "CRAIG coreset selection facility location submodular Mirzasoleiman 2020 ICML exact title authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db4d99b2-32d8-40b4-81ad-6c3ad0967551",
  "isSidechain": true,
  "agentId": "af5811deecee9942b",
  "requestId": "req_011Cb13gNYrRHeUPEaDyChAn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cb742e5d-663f-417f-ade6-695a670ee7ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KJ4HHjUujsEf141wzztQYR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4006,
      "cache_read_input_tokens": 15638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4006,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 16 · 2026-05-13T18:32:48.035Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D4i2FfDCwfUwcsvNiHaBqc`</summary>

```json
{
  "query": "SIMILAR submodular information measures active learning Kothawade 2021 NeurIPS exact title venue authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb742e5d-663f-417f-ade6-695a670ee7ee",
  "isSidechain": true,
  "agentId": "af5811deecee9942b",
  "requestId": "req_011Cb13gNYrRHeUPEaDyChAn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "370372e4-6e73-4e5c-b879-da6a2c1e74c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KJ4HHjUujsEf141wzztQYR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4006,
      "cache_read_input_tokens": 15638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4006,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 17 · 2026-05-13T18:32:48.203Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S4TCctfFsVG2vP43ZWjrFK`</summary>

```json
{
  "query": "Iyer Bilmes 2013 \"submodular optimization\" NeurIPS exact paper title best paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "370372e4-6e73-4e5c-b879-da6a2c1e74c6",
  "isSidechain": true,
  "agentId": "af5811deecee9942b",
  "requestId": "req_011Cb13gNYrRHeUPEaDyChAn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1189457c-a497-4e00-98e4-be39543386c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KJ4HHjUujsEf141wzztQYR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4006,
      "cache_read_input_tokens": 15638,
      "output_tokens": 217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4006
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 217,
          "cache_read_input_tokens": 15638,
          "cache_creation_input_tokens": 4006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4006,
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

_source line 18 · 2026-05-13T18:32:51.546Z_

<details><summary>↩ Tool result · `toolu_01S4TCctfFsVG2vP43ZWjrFK`</summary>

```text
Web search results for query: "Iyer Bilmes 2013 "submodular optimization" NeurIPS exact paper title best paper"

Links: [{"title":"Submodular Optimization with Submodular Cover and ...","url":"https://proceedings.neurips.cc/paper_files/paper/2013/file/a1d50185e7426cbb0acad1e6ca74b9aa-Paper.pdf"},{"title":"Submodular Optimization with Submodular Cover and Submodular Knapsack Constraints","url":"https://proceedings.neurips.cc/paper/2013/hash/a1d50185e7426cbb0acad1e6ca74b9aa-Abstract.html"},{"title":"Curvature and Optimal Algorithms for Learning and Minimizing Submodular Functions","url":"https://proceedings.neurips.cc/paper/2013/hash/c1e39d912d21c91dce811d6da9929ae8-Abstract.html"},{"title":"Bilmes and Iyer Win Best Paper at the 2013 Neural Information Processing Systems Conference | UW Department of Electrical & Computer Engineering","url":"https://www.ece.uw.edu/spotlight/bilmes-and-iyer-win-best-paper-at-the-2013-neural-information-processing-systems-conference/"},{"title":"Distributed Submodular Maximization:","url":"https://proceedings.neurips.cc/paper_files/paper/2013/file/84d2004bf28a2095230e8e14993d398d-Paper.pdf"},{"title":"Rishabh Iyer - Research","url":"https://sites.google.com/view/rishabhiyer/research"},{"title":"A Generalization of Submodular Cover via the","url":"https://proceedings.neurips.cc/paper/2015/file/7bcdf75ad237b8e02e301f4091fb6bc8-Paper.pdf"},{"title":"CARAML Lab - Publications","url":"https://www.caraml-lab.com/publications/"},{"title":"Rishabh Iyer's Webpage","url":"https://rishabhk108.github.io/"},{"title":"Rishabh Iyer - Publications","url":"https://sites.google.com/view/rishabhiyer/publications"}]

Based on the search results, I found the paper you're looking for:

The exact paper title is "Submodular Optimization with Submodular Cover and Submodular Knapsack Constraints" by Rishabh Iyer and Jeff Bilmes, which was published at NeurIPS 2013.

Importantly, this paper was one of three papers selected at the conference to receive the Outstanding Paper Award.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1189457c-a497-4e00-98e4-be39543386c1",
  "isSidechain": true,
  "promptId": "cb9d95fc-9c2d-4329-a2e0-19f7dffc3a15",
  "agentId": "af5811deecee9942b",
  "type": "user",
  "uuid": "bd82a70d-f1ee-419d-af3a-d4819e191fe7",
  "sourceToolAssistantUUID": "1189457c-a497-4e00-98e4-be39543386c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T18:32:51.652Z_

<details><summary>↩ Tool result · `toolu_01D4i2FfDCwfUwcsvNiHaBqc`</summary>

```text
Web search results for query: "SIMILAR submodular information measures active learning Kothawade 2021 NeurIPS exact title venue authors"

Links: [{"title":"SIMILAR: Submodular Information Measures Based Active Learning In Realistic Scenarios","url":"https://proceedings.neurips.cc/paper/2021/hash/9af08cda54faea9adf40a201794183cf-Abstract.html"},{"title":"SIMILAR: Submodular Information Measures Based Active Learning In Realistic Scenarios","url":"https://papers.nips.cc/paper/2021/hash/9af08cda54faea9adf40a201794183cf-Abstract.html"},{"title":"SIMILAR Submodular Information Measures Based","url":"https://nips.cc/media/neurips-2021/Slides/26574.pdf"},{"title":"SIMILAR Submodular Information Measures Based Active ...","url":"https://neurips.cc/media/neurips-2021/Slides/26574.pdf"},{"title":"SIMILAR: Submodular Information Measures Based Active ...","url":"https://proceedings.neurips.cc/paper/2021/file/9af08cda54faea9adf40a201794183cf-Paper.pdf"},{"title":"SIMILAR: Submodular Information Measures Based Active Learning In Realistic Scenarios | by CARAML Lab | Medium","url":"https://caraml-lab.medium.com/similar-submodular-information-measures-based-active-learning-in-realistic-scenarios-a9eb8c1d9047"},{"title":"SIMILAR: Submodular Information Measures Based Active Learning In Realistic Scenarios | OpenReview","url":"https://openreview.net/forum?id=VGDFaLNFFk"},{"title":"CARAML Lab - Publications","url":"https://www.caraml-lab.com/publications/"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=SIMILAR:+Submodular+Information+Measures+Based+Active+Learning+In+Realistic+Scenarios."},{"title":"[2107.00717] SIMILAR: Submodular Information Measures Based Active Learning In Realistic Scenarios","url":"https://arxiv.org/abs/2107.00717"}]

Based on the search results, here is the information you requested:

**Exact Title:** SIMILAR: Submodular Information Measures Based Active Learning In Realistic Scenarios

**Venue:** Advances in Neural Information Processing Systems 34 (NeurIPS 2021)

**Authors:** Suraj Kothawade, Nathan Beck, Krishnateja Killamsetty, Rishabh Iyer


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "370372e4-6e73-4e5c-b879-da6a2c1e74c6",
  "isSidechain": true,
  "promptId": "cb9d95fc-9c2d-4329-a2e0-19f7dffc3a15",
  "agentId": "af5811deecee9942b",
  "type": "user",
  "uuid": "f2f877b3-daba-4c52-be65-9c5dab901dc2",
  "sourceToolAssistantUUID": "370372e4-6e73-4e5c-b879-da6a2c1e74c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T18:32:51.686Z_

<details><summary>↩ Tool result · `toolu_01JosdeXZNHJmk8YVc6YywgG`</summary>

```text
Web search results for query: "CRAIG coreset selection facility location submodular Mirzasoleiman 2020 ICML exact title authors"

Links: [{"title":"Coresets for Data-efﬁcient Training of Machine Learning Models","url":"https://cs.stanford.edu/people/jure/pubs/craig-icml20.pdf"},{"title":"[1906.01827] Coresets for Data-efficient Training of Machine Learning Models","url":"https://arxiv.org/abs/1906.01827"},{"title":"Coresets for Data-efficient Training of Machine Learning Models","url":"https://proceedings.mlr.press/v119/mirzasoleiman20a.html"},{"title":"GitHub - PatrickZH/DeepCore: Code for coreset selection methods · GitHub","url":"https://github.com/PatrickZH/DeepCore"},{"title":"[PDF] Coresets for Data-efficient Training of Machine Learning Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Coresets-for-Data-efficient-Training-of-Machine-Mirzasoleiman-Bilmes/790985a4bee821046992ff3d5322ff11dd1b4262"},{"title":"GLISTER: Generalization based Data Subset Selection for Efﬁcient and Robust","url":"https://www.cse.iitb.ac.in/~ganesh/papers/aaai2021.pdf"},{"title":"Icml","url":"https://icml.cc/media/icml-2020/Slides/6325.pdf"},{"title":"Adversarial Coreset Selection for Efficient Robust Training | International Journal of Computer Vision | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11263-023-01860-4"},{"title":"Published as a conference paper at ICLR 2022 DIVERSE CLIENT SELECTION FOR","url":"https://openreview.net/pdf?id=nwKXyFvaUm"},{"title":"A Coreset Selection of Coreset Selection Literature: Introduction and Recent Advances","url":"https://arxiv.org/html/2505.17799v1"}]

Based on the search results, I found information about the paper you're looking for:

**Title:** "Coresets for Data-efficient Training of Machine Learning Models"

**Authors:** Baharan Mirzasoleiman, Jeff Bilmes, and Jure Leskovec

**Conference:** Proceedings of the 37th International Conference on Machine Learning (ICML)

**Key Details:** The paper develops CRAIG, a method to select a weighted subset (or coreset) of training data that closely estimates the full gradient by maximizing a submodular function. The authors prove that applying IG (incremental gradient) to this subset is guaranteed to converge to the (near)optimal solution with the same convergence rate as that of IG for convex optimization, and CRAIG achieves a speedup that is inversely proportional to the size of the subset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb742e5d-663f-417f-ade6-695a670ee7ee",
  "isSidechain": true,
  "promptId": "cb9d95fc-9c2d-4329-a2e0-19f7dffc3a15",
  "agentId": "af5811deecee9942b",
  "type": "user",
  "uuid": "c0f16226-6d02-4020-a54b-2c85e33291fa",
  "sourceToolAssistantUUID": "cb742e5d-663f-417f-ade6-695a670ee7ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-13T18:33:03.987Z_

All papers confirmed. Here are the verified results:

---

1. PAPER: [Iyer & Bilmes (2013)] "Submodular Optimization with Submodular Cover and Submodular Knapsack Constraints" — NeurIPS 2013 (Outstanding Paper Award)
VERIFIED: Yes
RELEVANCE: Establishes the constrained submodular maximization framework (budget constraints on subset size) that underpins diversity-based data selection methods operating over embedding spaces.

2. PAPER: [Wei et al. (2015)] "Submodularity in Data Subset Selection and Active Learning" — ICML 2015
AUTHORS: Kai Wei, Rishabh Iyer, Jeff Bilmes
VERIFIED: Yes
RELEVANCE: Directly formalizes data subset selection as submodular maximization using functions (facility location, graph cut) that measure coverage and diversity in feature/embedding space — the canonical framework attacked by the embedding alignment gap problem.

3. PAPER: [Mirzasoleiman et al. (2020)] "Coresets for Data-efficient Training of Machine Learning Models" — ICML 2020
AUTHORS: Baharan Mirzasoleiman, Jeff Bilmes, Jure Leskovec
VERIFIED: Yes
RELEVANCE: CRAIG uses facility location — a submodular function over gradient embeddings — to select coresets, making it directly susceptible to embedding space degradation when applied iteratively.

4. PAPER: [Kothawade et al. (2021)] "SIMILAR: Submodular Information Measures Based Active Learning In Realistic Scenarios" — NeurIPS 2021
AUTHORS: Suraj Kothawade, Nathan Beck, Krishnateja Killamsetty, Rishabh Iyer
VERIFIED: Yes
RELEVANCE: Applies submodular information measures (submodular mutual information, conditional gain) as acquisition functions over learned embeddings, making selection quality inherently tied to embedding representational fidelity.

Sources:
- [Iyer & Bilmes NeurIPS 2013](https://proceedings.neurips.cc/paper/2013/hash/a1d50185e7426cbb0acad1e6ca74b9aa-Abstract.html)
- [Wei et al. ICML 2015 – PMLR](https://proceedings.mlr.press/v37/wei15.html)
- [Mirzasoleiman et al. ICML 2020 – PMLR](https://proceedings.mlr.press/v119/mirzasoleiman20a.html)
- [Kothawade et al. NeurIPS 2021](https://proceedings.neurips.cc/paper/2021/hash/9af08cda54faea9adf40a201794183cf-Abstract.html)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0f16226-6d02-4020-a54b-2c85e33291fa",
  "isSidechain": true,
  "agentId": "af5811deecee9942b",
  "requestId": "req_011Cb13h3whKmoYKPBKGqsM7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "378a5163-70b1-45cf-86a0-1e33f675304a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/div_cal_verify",
  "sessionId": "be21bc6f-69d7-408f-96f6-62cd88f8b58c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01LvcsTWaU1n8ZxKQRLrDrbD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1402,
      "cache_creation_input_tokens": 1095,
      "cache_read_input_tokens": 19644,
      "output_tokens": 673,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1095
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1402,
          "output_tokens": 673,
          "cache_read_input_tokens": 19644,
          "cache_creation_input_tokens": 1095,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1095,
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
