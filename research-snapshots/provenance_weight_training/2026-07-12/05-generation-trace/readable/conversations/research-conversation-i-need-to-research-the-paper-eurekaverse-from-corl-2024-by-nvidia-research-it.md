# Research conversation: I need to research the paper "Eurekaverse" from CoRL 2024 by NVIDIA Research. It's about LLM-driven environment curricul

**When Does Detect-and-Reweight Work for Synthetic Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a213ef82cff7a045d.jsonl`
- **Structured JSON:** [`5e26c90c2919e1d65835.json`](../../sessions/5e/5e26c90c2919e1d65835.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-10T19:14:24.086Z_

I need to research the paper "Eurekaverse" from CoRL 2024 by NVIDIA Research. It's about LLM-driven environment curriculum generation with agent-environment co-evolution for RL training, targeting quadrupedal parkour.

Please:
1. Use WebSearch to find "Eurekaverse CoRL 2024 NVIDIA environment generation curriculum"
2. Use WebFetch to read the paper's abstract and method section from arXiv (likely arXiv:2406.01309 or similar)
3. Summarize: what exactly does Eurekaverse do? How does it generate environments? What's the co-evolution loop? What are its limitations?

Report back with detailed findings including the exact arXiv ID, key method details, and how it relates to compositional task generation for humanoid loco-manipulation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3f7b4726-baab-4e94-9aee-9793dc1dd145",
  "agentId": "a213ef82cff7a045d",
  "type": "user",
  "uuid": "ac6cfb59-2e4f-42aa-86c2-2ced046358ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-10T19:14:24.090Z_

```json
{
  "parentUuid": "ac6cfb59-2e4f-42aa-86c2-2ced046358ab",
  "isSidechain": true,
  "agentId": "a213ef82cff7a045d",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "3c6c79e7-a789-4549-b257-30b6a9c2a291",
  "timestamp": "2026-05-10T19:14:24.090Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-10T19:14:26.876Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01478nKQupQttrb6Y3Lgdhex`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c6c79e7-a789-4549-b257-30b6a9c2a291",
  "isSidechain": true,
  "agentId": "a213ef82cff7a045d",
  "requestId": "req_011CauRS2i9WiKi9yMm53yWi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "82403197-2036-40b5-9f38-6d634153b92c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LH2rAgerneh3AkktC63FQE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7874,
      "cache_read_input_tokens": 0,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7874
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 7874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7874,
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

_source line 4 · 2026-05-10T19:14:26.880Z_

<details><summary>↩ Tool result · `toolu_01478nKQupQttrb6Y3Lgdhex`</summary>

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
  "parentUuid": "82403197-2036-40b5-9f38-6d634153b92c",
  "isSidechain": true,
  "promptId": "3f7b4726-baab-4e94-9aee-9793dc1dd145",
  "agentId": "a213ef82cff7a045d",
  "type": "user",
  "uuid": "7564abf9-3c54-43d2-b3f2-5298d787a3be",
  "sourceToolAssistantUUID": "82403197-2036-40b5-9f38-6d634153b92c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T19:14:30.210Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HdQesujt95DU4a9ZoVbpV7`</summary>

```json
{
  "query": "Eurekaverse CoRL 2024 NVIDIA environment generation curriculum LLM quadrupedal parkour"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7564abf9-3c54-43d2-b3f2-5298d787a3be",
  "isSidechain": true,
  "agentId": "a213ef82cff7a045d",
  "requestId": "req_011CauRSEtPBo2wXwBpQhATj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "56329b1f-e7aa-4802-8565-fd5c9e345418",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHbzrhJxfkU3nXYQJwyZbG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1881,
      "cache_read_input_tokens": 7874,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1881
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 77,
          "cache_read_input_tokens": 7874,
          "cache_creation_input_tokens": 1881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1881,
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

_source line 6 · 2026-05-10T19:14:37.208Z_

<details><summary>↩ Tool result · `toolu_01HdQesujt95DU4a9ZoVbpV7`</summary>

```text
Web search results for query: "Eurekaverse CoRL 2024 NVIDIA environment generation curriculum LLM quadrupedal parkour"

Links: [{"title":"GitHub - eureka-research/eurekaverse: Official Repository for \"Eurekaverse: Environment Curriculum Generation via Large Language Models\" (CoRL 2024)","url":"https://github.com/eureka-research/eurekaverse"},{"title":"[2411.01775] Eurekaverse: Environment Curriculum Generation via Large Language Models","url":"https://arxiv.org/abs/2411.01775"},{"title":"Eurekaverse | Environment Curriculum Generation via Large Language Models","url":"https://eureka-research.github.io/eurekaverse/"},{"title":"Eurekaverse: Environment Curriculum Generation via Large Language Models | Dinesh Jayaraman","url":"https://www.seas.upenn.edu/~dineshj/publication/liang-2024-eurekaverse/"},{"title":"Environment Curriculum Generation via Large Language Models | OpenReview","url":"https://openreview.net/forum?id=F0rWEID2gb"},{"title":"eurekaverse/README.md at main · eureka-research/eurekaverse","url":"https://github.com/eureka-research/eurekaverse/blob/main/README.md"},{"title":"Environment Curriculum Generation via Large Language Models","url":"https://arxiv.org/html/2411.01775v1"},{"title":"Eurekaverse: Environment Curriculum Generation via Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241101775L/abstract"},{"title":"Eurekaverse: Environment Curriculum Generation via Large Language Models","url":"https://www.researchgate.net/publication/385529161_Eurekaverse_Environment_Curriculum_Generation_via_Large_Language_Models"},{"title":"[Literature Review] Eurekaverse: Environment Curriculum Generation via Large Language Models","url":"https://www.themoonlight.io/en/review/eurekaverse-environment-curriculum-generation-via-large-language-models"}]

I found comprehensive information about Eurekaverse. Here's a summary of the research:

## Overview

Eurekaverse is the official repository for "Eurekaverse: Environment Curriculum Generation via Large Language Models" (CoRL 2024). Eurekaverse is an unsupervised environment design algorithm that uses LLMs to sample progressively more challenging, diverse, and learnable environments for skill training.

## Key Concept

The key insight is that environments are often naturally represented as code, and the researchers probed whether effective environment curriculum design can be achieved and automated via code generation by large language models (LLM).

## Application Domain

Eurekaverse's effectiveness is validated in the domain of quadrupedal parkour learning, in which a quadruped robot must traverse through a variety of obstacle courses.

## Technical Approach

At a technical level, Eurekaverse instructs an LLM to generate novel environments to teach the target task, trains policies for each environment, and evaluates the best-performing policies to inform the LLM when it generates the next round of environments. The algorithm uses a process called agent-environment co-evolution, where it iteratively uses reinforcement learning (RL) to train agents on the current set of environments, followed by updating the set of environments so they continue to challenge the best current policy without being too difficult for learning.

## Results

The automatic curriculum designed by Eurekaverse enables gradual learning of complex parkour skills in simulation and can successfully transfer to the real-world, outperforming manual training courses designed by humans.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56329b1f-e7aa-4802-8565-fd5c9e345418",
  "isSidechain": true,
  "promptId": "3f7b4726-baab-4e94-9aee-9793dc1dd145",
  "agentId": "a213ef82cff7a045d",
  "type": "user",
  "uuid": "5c4f8c6f-32b6-4436-a729-3ba5889e72e6",
  "sourceToolAssistantUUID": "56329b1f-e7aa-4802-8565-fd5c9e345418",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T19:14:41.515Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Pthw8R62XnmPgqWDzwDf5n`</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.01775",
  "prompt": "Extract the full abstract, list of authors, and any information about the method, contributions, and key technical details of this paper. Include the exact arXiv ID."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c4f8c6f-32b6-4436-a729-3ba5889e72e6",
  "isSidechain": true,
  "agentId": "a213ef82cff7a045d",
  "requestId": "req_011CauRT14DBvBbLYgVJ3QYp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db212c46-3564-4090-b346-f1cbf75e375b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HspKRaFYVuk28e96JuLk6c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 9755,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 976,
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

_source line 8 · 2026-05-10T19:14:43.846Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EiZpW1CdumXnkNqiZZ4DMa`</summary>

```json
{
  "url": "https://arxiv.org/html/2411.01775v1",
  "prompt": "Extract detailed information about the method section of this paper. Specifically: 1) How does the LLM generate environments (what is the representation)? 2) What is the co-evolution loop in detail - how does the agent training feed back into environment generation? 3) What curriculum strategy is used? 4) What are the limitations discussed by the authors? 5) What environments/tasks were tested? 6) Any details about the reward function or training pipeline. Be as detailed as possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db212c46-3564-4090-b346-f1cbf75e375b",
  "isSidechain": true,
  "agentId": "a213ef82cff7a045d",
  "requestId": "req_011CauRT14DBvBbLYgVJ3QYp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c4d5d59-c5f2-4290-acf8-ad21904e4b8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HspKRaFYVuk28e96JuLk6c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 976,
      "cache_read_input_tokens": 9755,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 976
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 287,
          "cache_read_input_tokens": 9755,
          "cache_creation_input_tokens": 976,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 976,
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

_source line 9 · 2026-05-10T19:14:46.275Z_

<details><summary>↩ Tool result · `toolu_01Pthw8R62XnmPgqWDzwDf5n`</summary>

```text
# Eurekaverse: Environment Curriculum Generation via Large Language Models

**arXiv ID:** 2411.01775

## Authors
William Liang, Sam Wang, Hung-Ju Wang, Osbert Bastani, Dinesh Jayaraman, Yecheng Jason Ma

## Abstract
The paper addresses automated curriculum design for robot training. The authors propose that "environments are often naturally represented as code" and leverage this insight to automate curriculum development. Their key contribution is demonstrating that "effective environment curriculum design can be achieved and automated via code generation by large language models."

## Method & Contributions

**Core Approach:** Eurekaverse is an unsupervised algorithm using LLMs to "sample progressively more challenging, diverse, and learnable environments for skill training."

**Key Technical Details:**
- Applies environment curriculum generation to quadrupedal parkour learning
- Robots learn to traverse obstacle courses with increasing difficulty
- Curriculum transfers successfully from simulation to real-world robots

**Validation Results:** The automatically designed curriculum "outperforms manual training courses designed by humans" in both simulation and real-world deployment.

**Publication:** Conference on Robot Learning (CoRL), 2024

**Subjects:** Robotics (cs.RO), Artificial Intelligence (cs.AI), Machine Learning (cs.LG)

**Resources:** Project website and code available at the associated URL
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db212c46-3564-4090-b346-f1cbf75e375b",
  "isSidechain": true,
  "promptId": "3f7b4726-baab-4e94-9aee-9793dc1dd145",
  "agentId": "a213ef82cff7a045d",
  "type": "user",
  "uuid": "1f4d837e-9790-4596-b97b-c20a1065b9d5",
  "sourceToolAssistantUUID": "db212c46-3564-4090-b346-f1cbf75e375b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T19:14:55.188Z_

<details><summary>↩ Tool result · `toolu_01EiZpW1CdumXnkNqiZZ4DMa`</summary>

```text
# Eurekaverse: Method Details Extraction

## 1. Environment Representation

Environments are represented as **Python programs** that generate obstacle courses. Specifically, the method uses "a function set_terrain(length, width, field_resolution, difficulty)" that produces two outputs:
- A height_field: a 2D NumPy array representing ground heights
- A goals array: 8 (x,y) coordinate pairs marking sequential waypoints

For quadrupedal parkour, this translates terrain geometry into executable code using NumPy operations and loops.

## 2. Co-Evolution Loop Detail

The approach alternates between two phases:

**Policy Evolution:** N agents train independently on J environments each. All agents evaluate against a union of training environments (proxy set), and the best-performing policy is selected using "soft selection" (75% probability for best, 25% for second-best).

**Environment Evolution:** The LLM receives the best policy's training environments plus performance feedback: "environment statistics (e.g. maximum terrain height difference) and policy training statistics (e.g. reward terms and success rate)." New environments are generated as variations of successful ones via the evolution prompt. This iterates for 5 generations with 8 parallel policy runs per iteration.

## 3. Curriculum Strategy

Rather than predetermined difficulty progression, Eurekaverse creates implicit curriculum through **adaptive feedback**: environments evolve based on what the current policy struggles with. The prompt instructs the LLM to "balance difficulty and feasibility," increasing challenge if success exceeds 80%, simplifying if below 20%. Evolution prompt states: "if the robot is getting stuck on a certain obstacle...you should change it."

## 4. Author-Stated Limitations

The authors acknowledge: "Our system requires a moderate amount of LLM samples to consistently generate and select valuable environments; a important future direction necessary for scaling up is increasing sample efficiency." Additionally, evolution uses "only textual feedback" rather than visual information from environment renders.

## 5. Tested Environments/Tasks

Primary evaluation uses **quadrupedal parkour** on a Unitree Go1 robot. Testing includes:
- Simulation benchmark: 20 diverse tasks (box climbing, gap crossing, ramps, stairs, A-frames, stepping stones, etc.)
- Real-world deployment: box climbing, gap crossing, forward ramps, staircases, plus four unseen composite courses

## 6. Reward Function & Training Details

The paper states: "All methods and ablations use the same reward and training setup." Specific reward components tracked include torso orientation, but full formulation isn't detailed in main text. Training uses PPO with "privileged scandot sensing" during sim training, distilled into a depth-based student policy. One full run requires approximately 24 hours on 8 GPUs with $15 in API costs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c4d5d59-c5f2-4290-acf8-ad21904e4b8e",
  "isSidechain": true,
  "promptId": "3f7b4726-baab-4e94-9aee-9793dc1dd145",
  "agentId": "a213ef82cff7a045d",
  "type": "user",
  "uuid": "53bf8b45-5792-46b9-bd5e-dbf3a831f041",
  "sourceToolAssistantUUID": "5c4d5d59-c5f2-4290-acf8-ad21904e4b8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T19:15:05.291Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TsLc6qUspQk11unH81cL8M`</summary>

```json
{
  "url": "https://eureka-research.github.io/eurekaverse/",
  "prompt": "Extract any additional details about: 1) The relationship between Eurekaverse and Eureka (the reward generation paper), 2) Any discussion of limitations or failure modes, 3) How environments are parameterized and what the LLM prompt looks like, 4) Any mention of humanoid robots or loco-manipulation tasks, 5) Comparisons to baselines and quantitative results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53bf8b45-5792-46b9-bd5e-dbf3a831f041",
  "isSidechain": true,
  "agentId": "a213ef82cff7a045d",
  "requestId": "req_011CauRUKfgE8MCrNyViKkpq",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "41b6b4fa-d19a-4bfb-a892-dd59e2226bc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VyY5d9G1JXLLjqqB4giZju",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1292,
      "cache_read_input_tokens": 10731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1292,
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

### Tool result

_source line 12 · 2026-05-10T19:15:09.424Z_

<details><summary>↩ Tool result · `toolu_01TsLc6qUspQk11unH81cL8M`</summary>

```text
# Eurekaverse: Key Details Extraction

## 1. Relationship to Eureka
The website acknowledges borrowing its template from "Eureka" but provides no substantive discussion of the relationship between Eurekaverse and the prior Eureka reward generation work.

## 2. Limitations and Failure Modes
The paper explicitly addresses shortcomings: "our sim-to-real transfer still leaves a noticeable gap between simulated and real-world behavior." Additionally, they suggest that "future work can incorporate visual feedback during environment generation, potentially improving spatial reasoning and environment diversity." The authors also note "many ways to further improve performance."

## 3. Environment Parameterization and LLM Prompts
The content indicates that "environments are often naturally represented as code" and that the method uses "code generation by large language models." However, specific details about parameterization schemes and actual prompt formulations are not provided in this webpage—these would likely be in the full paper or code repository.

## 4. Humanoid Robots or Loco-Manipulation
Neither humanoid robots nor loco-manipulation tasks are mentioned. The work focuses exclusively on "quadrupedal parkour learning."

## 5. Baselines and Quantitative Results
Eurekaverse is compared against a "Human-Designed baseline from prior work." The results show that the human baseline "learns quickly but plateaus, whereas Ours continuously improves and nears the performance of an Oracle trained on the testing terrains." Real-world testing demonstrates superior performance "across four obstacle types."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41b6b4fa-d19a-4bfb-a892-dd59e2226bc7",
  "isSidechain": true,
  "promptId": "3f7b4726-baab-4e94-9aee-9793dc1dd145",
  "agentId": "a213ef82cff7a045d",
  "type": "user",
  "uuid": "164ae450-7fff-4b5d-b972-8664df235cb9",
  "sourceToolAssistantUUID": "41b6b4fa-d19a-4bfb-a892-dd59e2226bc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T19:15:41.078Z_

Here is my detailed research report on the Eurekaverse paper:

---

## Eurekaverse: Environment Curriculum Generation via Large Language Models

**arXiv ID:** 2411.01775  
**Venue:** CoRL 2024  
**Authors:** William Liang, Sam Wang, Hung-Ju Wang, Osbert Bastani, Dinesh Jayaraman, Yecheng Jason Ma  
**Affiliations:** NVIDIA Research, University of Pennsylvania

---

### What Eurekaverse Does

Eurekaverse is an unsupervised environment design algorithm that uses LLMs to automatically generate progressively more challenging, diverse, and learnable training environments for reinforcement learning. Its core insight is that physical environments are naturally representable as code (specifically Python programs), so LLM code-generation capabilities can be directly leveraged for environment curriculum design. The system was validated on quadrupedal parkour (Unitree Go1 robot traversing obstacle courses), where it outperformed human-designed training curricula both in simulation and real-world deployment.

---

### How It Generates Environments

Environments are represented as **Python functions** with the signature `set_terrain(length, width, field_resolution, difficulty)` that produce:
1. A **height_field** -- a 2D NumPy array representing ground elevations (the physical terrain geometry)
2. A **goals** array -- 8 sequential (x, y) waypoint coordinates the robot must reach

The LLM generates these terrain programs using NumPy operations and loops. This code-as-environment representation allows the LLM to reason about obstacle geometry (boxes, gaps, ramps, stairs, A-frames, stepping stones, etc.) in a structured, composable way.

---

### The Co-Evolution Loop (Detailed)

The method alternates between two phases:

**Phase 1 -- Policy Evolution:**
- N agents train independently, each on J environments
- All agents are evaluated against a union set of training environments (a proxy evaluation set)
- The best-performing policy is selected via "soft selection" (75% probability for top performer, 25% for second-best) to maintain diversity

**Phase 2 -- Environment Evolution:**
- The LLM receives the best policy's training environments plus performance feedback including: environment statistics (e.g., maximum terrain height difference) and policy training statistics (e.g., reward terms, success rate)
- The LLM generates new environment variations based on this feedback
- Adaptive difficulty: if success > 80%, difficulty increases; if success < 20%, the environment is simplified
- The prompt instructs the LLM to "balance difficulty and feasibility" and to modify obstacles the robot gets stuck on

This loop iterates for **5 generations** with **8 parallel policy runs per iteration**. A full run takes approximately 24 hours on 8 GPUs with ~$15 in LLM API costs.

Training uses PPO with privileged scandot sensing in simulation, later distilled into a depth-camera-based student policy for real-world deployment.

---

### Key Results

- Eurekaverse's automatic curriculum enables continuous improvement, whereas human-designed baselines learn quickly but plateau
- Performance approaches an Oracle policy trained directly on the test terrains
- Successful sim-to-real transfer demonstrated across box climbing, gap crossing, forward ramps, staircases, and four unseen composite courses

---

### Limitations (Author-Stated)

1. **Sample efficiency:** Requires a moderate number of LLM samples to consistently generate valuable environments; improving sample efficiency is critical for scaling up
2. **Text-only feedback:** Environment evolution uses only textual statistics, not visual renders -- incorporating visual feedback could improve spatial reasoning and diversity
3. **Sim-to-real gap:** Transfer still leaves a noticeable gap between simulated and real-world behavior
4. **Single domain validated:** Only demonstrated on quadrupedal parkour

---

### Relationship to Compositional Task Generation for Humanoid Loco-Manipulation

Eurekaverse does **not** address humanoid robots or loco-manipulation tasks -- it focuses exclusively on quadrupedal locomotion over terrain. However, its methodology is highly relevant to compositional humanoid task generation in the following ways:

1. **Code-as-environment paradigm:** The idea that environments/tasks can be represented as programs that an LLM generates is directly transferable. For humanoid loco-manipulation, one could represent manipulation scenes (object placements, furniture arrangements, tool configurations) as code.

2. **Curriculum via co-evolution:** The adaptive feedback loop (train agent -> evaluate -> generate harder environments) could extend to manipulation task curricula -- e.g., starting with simple pick-and-place, evolving toward multi-step tool use or coordinated locomotion+manipulation.

3. **Compositionality gap:** Eurekaverse generates monolithic terrain programs rather than composing modular sub-tasks. For humanoid loco-manipulation, a compositional approach (combining locomotion primitives with manipulation primitives) would likely require extending beyond Eurekaverse's flat terrain-generation paradigm.

4. **Key missing pieces for loco-manipulation:** Eurekaverse lacks object interaction semantics, multi-objective reward balancing (locomotion vs. manipulation), and articulated object modeling -- all essential for humanoid tasks.

---

### Sources

- [arXiv:2411.01775 -- Eurekaverse Paper](https://arxiv.org/abs/2411.01775)
- [Eurekaverse Project Website](https://eureka-research.github.io/eurekaverse/)
- [GitHub Repository](https://github.com/eureka-research/eurekaverse)
- [OpenReview (CoRL 2024)](https://openreview.net/forum?id=F0rWEID2gb)
- [Full HTML Version](https://arxiv.org/html/2411.01775v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "164ae450-7fff-4b5d-b972-8664df235cb9",
  "isSidechain": true,
  "agentId": "a213ef82cff7a045d",
  "requestId": "req_011CauRVNWMi7cyknKS8ZMxZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81679fc5-d1f0-4d17-85c9-c6169aea4aed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "0a642523-2dba-48d9-8830-07708276e46b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182i42AonCP371vsuGqcuW8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 528,
      "cache_read_input_tokens": 12023,
      "output_tokens": 1360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 528
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1360,
          "cache_read_input_tokens": 12023,
          "cache_creation_input_tokens": 528,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 528,
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
