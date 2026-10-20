# Research conversation: Search the web for recent papers (2025-2026) on demographic calibration for LLM-based user simulators in human-AI intera

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a832b9ad296dd183f.jsonl`
- **Structured JSON:** [`371338d13413c7e5139c.json`](../../sessions/37/371338d13413c7e5139c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-10T06:27:41.708Z_

Search the web for recent papers (2025-2026) on demographic calibration for LLM-based user simulators in human-AI interaction evaluation. Specifically look for:
1. Papers on "demographic calibration user simulator LLM" 
2. Papers on "LLM simulator behavioral calibration demographic"
3. arXiv papers from Jan-May 2026 on user simulation fairness
4. Search OpenReview for ICML 2026, NeurIPS 2026, ICLR 2026 submissions on user simulation calibration

Report: titles, venues/arXiv IDs, brief descriptions of any highly similar work that would be direct concurrent work. This is to check if anyone is already doing demographically-calibrated LLM user simulation for fair evaluation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "65c9c31a-1745-4148-a2b6-c8121abe6f91",
  "agentId": "a832b9ad296dd183f",
  "type": "user",
  "uuid": "937bea34-3b57-4104-adcf-791bbdda9b50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T06:27:42.945Z_

I'll search for recent papers on demographic calibration for LLM-based user simulators. Let me conduct multiple searches to cover the different angles you've specified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "937bea34-3b57-4104-adcf-791bbdda9b50",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQxzrmRPBdxXQNzoeKd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "49515fa6-104e-4b66-bc38-e82ae419fdf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WNtpYp57V8afJ19u16W3vu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16756,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16756,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T06:27:43.193Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GCZj1M8yqLCsAKbw5fmUdL`</summary>

```json
{
  "query": "demographic calibration user simulator LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49515fa6-104e-4b66-bc38-e82ae419fdf9",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQxzrmRPBdxXQNzoeKd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7387d736-f5cb-40e9-9b66-92970949c474",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WNtpYp57V8afJ19u16W3vu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16756,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16756,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T06:27:43.422Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ab56rS5SRvAGUce6TRXpoB`</summary>

```json
{
  "query": "LLM simulator behavioral calibration demographic fairness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7387d736-f5cb-40e9-9b66-92970949c474",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQxzrmRPBdxXQNzoeKd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b611bb1e-af32-4013-bb2e-979307701417",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WNtpYp57V8afJ19u16W3vu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16756,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16756,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T06:27:43.641Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ts7B9wXrJtVu2n5vu7a67t`</summary>

```json
{
  "query": "arXiv user simulation fairness LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b611bb1e-af32-4013-bb2e-979307701417",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQxzrmRPBdxXQNzoeKd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3a1e9639-f4aa-4fd0-9689-e615706353c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WNtpYp57V8afJ19u16W3vu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16756,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16756,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T06:27:43.645Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JxVBA3kbpk7d5uEJgrtpsY`</summary>

```json
{
  "query": "OpenReview ICML 2026 user simulation calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a1e9639-f4aa-4fd0-9689-e615706353c8",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQxzrmRPBdxXQNzoeKd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "07704192-5d72-4b57-8183-51578c80f4a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WNtpYp57V8afJ19u16W3vu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16756,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16756,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T06:27:43.853Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0164feKGNrME8uSf4yEqpZkZ`</summary>

```json
{
  "query": "OpenReview NeurIPS 2026 LLM user simulator evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07704192-5d72-4b57-8183-51578c80f4a1",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQxzrmRPBdxXQNzoeKd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c1c1e4b7-6002-4bbc-9db5-0c3b39c30c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WNtpYp57V8afJ19u16W3vu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16756,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16756,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T06:27:44.037Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S3E3ZJy7yJTKfq7ZBy4qji`</summary>

```json
{
  "query": "OpenReview ICLR 2026 demographic fairness user simulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1c1e4b7-6002-4bbc-9db5-0c3b39c30c06",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQxzrmRPBdxXQNzoeKd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "37ffb607-a836-4855-8ec3-67133f7be5dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WNtpYp57V8afJ19u16W3vu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16756,
      "cache_read_input_tokens": 0,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16756
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 340,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16756,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16756,
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

_source line 9 · 2026-05-10T06:27:48.735Z_

<details><summary>↩ Tool result · `toolu_01JxVBA3kbpk7d5uEJgrtpsY`</summary>

```text
Web search results for query: "OpenReview ICML 2026 user simulation calibration"

Links: [{"title":"ICML 2026 | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026"},{"title":"ICML 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FConference"},{"title":"ICML 2026 Workshop | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop"},{"title":"ICML 2026 – ICML Blog","url":"https://blog.icml.cc/category/icml-2026/"},{"title":"ICML 2026 Workshop Proposals | OpenReview","url":"https://openreview.net/group?id=ICML.cc/2026/Workshop_Proposals"},{"title":"ICML 2026 Workshop SCALE | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FSCALE"},{"title":"ICML | OpenReview","url":"https://openreview.net/group?id=ICML.cc"},{"title":"ICML 2026 Workshop EIML | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FEIML"},{"title":"ICML 2026 Workshop Forecast | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FForecast"},{"title":"ICML 2026 Workshop AI4Science | OpenReview","url":"https://openreview.net/group?id=ICML.cc%2F2026%2FWorkshop%2FAI4Science"}]

I've performed the web search for "OpenReview ICML 2026 user simulation calibration". 

The search results show general information about ICML 2026 on OpenReview, including pages for the main conference, workshops, and workshop proposals. The most substantive result discusses the Isotonic Mechanism, a computationally efficient approach to enhancing the accuracy of noisy review scores by incorporating authors' self-rankings of their submissions, where authors with multiple submissions are asked to rank their papers in descending order of perceived quality.

However, the search results don't contain specific information about papers or submissions related to "user simulation calibration" at ICML 2026. The results are primarily landing pages for the conference sections on OpenReview rather than detailed information about specific research papers on this topic. To find more specific papers on user simulation calibration, you might want to:

1. Visit the main ICML 2026 Conference page on OpenReview directly and search within their submissions
2. Browse papers by topic or keyword within the conference proceedings
3. Use more specific search terms if you're looking for a particular paper or author


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07704192-5d72-4b57-8183-51578c80f4a1",
  "isSidechain": true,
  "promptId": "65c9c31a-1745-4148-a2b6-c8121abe6f91",
  "agentId": "a832b9ad296dd183f",
  "type": "user",
  "uuid": "b81eb823-3145-4f9f-8bcb-a15cecbc8a70",
  "sourceToolAssistantUUID": "07704192-5d72-4b57-8183-51578c80f4a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T06:27:50.938Z_

<details><summary>↩ Tool result · `toolu_01GCZj1M8yqLCsAKbw5fmUdL`</summary>

```text
Web search results for query: "demographic calibration user simulator LLM 2025 2026"

Links: [{"title":"Persona-Based Simulation of Human Opinion at Population Scale","url":"https://arxiv.org/html/2603.27056v1"},{"title":"Simulated Demographic Personas","url":"https://www.emergentmind.com/topics/simulated-demographic-personas"},{"title":"LLM-Simulated Users","url":"https://www.emergentmind.com/topics/llm-simulated-users"},{"title":"Flipping the Dialogue: Training and Evaluating User Language Models | OpenReview","url":"https://openreview.net/forum?id=ykSmkVqzn4"},{"title":"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations","url":"https://arxiv.org/html/2601.17087v2"},{"title":"A LLM-based Controllable, Scalable, Human-Involved User Simulator Framework for Conversational Recommender Systems | OpenReview","url":"https://openreview.net/forum?id=H9BYGURN9M"},{"title":"A Survey on LLM-based Conversational User Simulation","url":"https://arxiv.org/html/2604.24977"},{"title":"Evaluating LLMs for Synthetic Personas Generation: A Comparative Analysis of Personality Representation and Censorship Effects | Proceedings of the 16th Biannual Conference of the Italian SIGCHI Chapter","url":"https://dl.acm.org/doi/10.1145/3750069.3750142"},{"title":"Large Language Models for Conversational User Simulation:","url":"http://ryanrossi.com/pubs/LLM-based_User_Simulated_Data_Generation_Survey.pdf"},{"title":"Evaluating AI-Simulated Behavior: Insights from Three Studies on Digital Twins and Synthetic Users - NN/G","url":"https://www.nngroup.com/articles/ai-simulations-studies/"}]

Based on the search results, here's what the research shows about demographic calibration for user simulator LLMs in 2025-2026:

## Key Research Areas

Demographic persona conditioning can appear competitively accurate on some attributes while still producing degenerate response patterns, as demographic persona inference relies on population-level shortcuts leading to low-confidence, low-diversity predictions.

SPIRIT persona conditioning mitigates these issues by grounding inference in non-demographic attributes, resulting in more confident, diverse, and behaviorally plausible responses.

## Limitations of Demographic-Only Approaches

Sociodemographic summaries alone explain only about 1.5% of variance in human behavioral responses; adding structured values, identity narratives, and personality measures amplifies behavioral fidelity and reduces demographic over-accentuation in LLM outputs.

Interview-based simulated users produce more accurate models of humans than synthetic users based only on demographic information or on a persona-like description of the user, perhaps because they provide richer, more nuanced data.

## Bias and Fairness Concerns

Digital twins have bias: depending on a person's socioeconomic class, race, or political views, digital twins may perform less accurately—for example, one study found that digital twins were better at predicting white people's responses compared to other racial groups.

## Advanced Calibration Approaches

Advanced generators employ mixture-model prompting, hierarchical mixtures of personas and real data exemplars, and multi-objective evolutionary search to maximize diversity metrics and explicitly target "long-tail" behaviors otherwise underrepresented in naive LLM sampling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7387d736-f5cb-40e9-9b66-92970949c474",
  "isSidechain": true,
  "promptId": "65c9c31a-1745-4148-a2b6-c8121abe6f91",
  "agentId": "a832b9ad296dd183f",
  "type": "user",
  "uuid": "7167204f-8b09-416c-aa4c-e5461e6462b9",
  "sourceToolAssistantUUID": "7387d736-f5cb-40e9-9b66-92970949c474",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T06:27:51.062Z_

<details><summary>↩ Tool result · `toolu_01S3E3ZJy7yJTKfq7ZBy4qji`</summary>

```text
Web search results for query: "OpenReview ICLR 2026 demographic fairness user simulation"

Links: [{"title":"Fairness Aware Reward Optimization | OpenReview","url":"https://openreview.net/forum?id=gl2nAqMlII"},{"title":"ICLR 2026 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/iclr-statistics/iclr-2026-statistics/"},{"title":"FAIRNESS GUARANTEES UNDER DEMOGRAPHIC SHIFT","url":"https://openreview.net/pdf?id=wbPObLm6ueA"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/725d3f295086b2f4659cae824a7e8caf25898eae.pdf"},{"title":"Fairness via Independence: A General Regularization Framework for Machine Learning | OpenReview","url":"https://openreview.net/forum?id=sbEb0Ld6MK"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations | OpenReview","url":"https://openreview.net/forum?id=m57vJLBHxA"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"},{"title":"ICLR | OpenReview","url":"https://openreview.net/group?id=ICLR.cc"},{"title":"ICLR 2026 Conference Submissions","url":"https://openreview.net/submissions?page=387&venue=ICLR.cc/2026/Conference"}]

Based on the search results, I found several relevant papers on OpenReview related to ICLR 2026 that discuss demographic fairness and user simulation:

## Key Papers Found:

1. **Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations**

This paper examines whether LLM-simulated users serve as reliable proxies for real human users in evaluating agents, investigating this through a user study with participants across the United States, India, Kenya, and Nigeria. The research finds that user simulation lacks robustness, with agent success rates varying up to 9 percentage points across different user LLMs. Notably, African American Vernacular English (AAVE) speakers experience consistently worse success rates and calibration errors than Standard American English (SAE) speakers, with disparities compounding significantly with age.

2. **Fairness-Aware Reward Optimization (FARO)**

This paper introduces Fairness-Aware Reward Optimisation (FARO), a principled framework for training reward models under demographic parity, equalised odds, or counterfactual fairness constraints.

3. **Fairness via Independence: A General Regularization Framework for Machine Learning**

This work addresses how predictive models frequently inherit or amplify biases present in training data, with biases manifesting as unintended correlations between model outcomes and sensitive attributes, leading to systematic disparities across demographic groups.

These papers explore the intersection of demographic fairness and user simulation in machine learning systems submitted to ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37ffb607-a836-4855-8ec3-67133f7be5dc",
  "isSidechain": true,
  "promptId": "65c9c31a-1745-4148-a2b6-c8121abe6f91",
  "agentId": "a832b9ad296dd183f",
  "type": "user",
  "uuid": "9b051422-274a-41df-bc3c-4ca8c8bf5466",
  "sourceToolAssistantUUID": "37ffb607-a836-4855-8ec3-67133f7be5dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T06:27:51.237Z_

<details><summary>↩ Tool result · `toolu_01Ab56rS5SRvAGUce6TRXpoB`</summary>

```text
Web search results for query: "LLM simulator behavioral calibration demographic fairness"

Links: [{"title":"EQUITRIAGE: A Fairness Audit of Gender Bias in LLM-Based Emergency Department Triage","url":"https://arxiv.org/html/2605.03998"},{"title":"Evaluating LLM Behavior in Hiring: Implicit Weights, Fairness Across Groups, and Alignment with Human Preferences","url":"https://arxiv.org/html/2601.11379"},{"title":"[2506.10922] Robustly Improving LLM Fairness in Realistic Settings via Interpretability","url":"https://arxiv.org/abs/2506.10922"},{"title":"[2601.11379] Evaluating LLM Behavior in Hiring: Implicit Weights, Fairness Across Groups, and Alignment with Human Preferences","url":"https://arxiv.org/abs/2601.11379"},{"title":"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations","url":"https://arxiv.org/html/2601.17087"},{"title":"Diagnosing the bias iceberg in large language models: A three-level framework of explicit, evaluative, and implicit gender bias - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0306457325004959"},{"title":"Validating LLM simulations as behavioral evidence","url":"https://mucollective.northwestern.edu/files/Hullman-llm-behavioral.pdf"},{"title":"Reduce Disparity Between LLMs and Humans: Optimal LLM Sample Calibration by Yan Leng, Yunxin Sang, Ashish Agarwal :: SSRN","url":"https://ssrn.com/abstract=4802019"},{"title":"Fairness Evaluation and Inference Level Mitigation in LLMs","url":"https://arxiv.org/html/2510.18914v4"},{"title":"[2504.07801] FairEval: Evaluating Fairness in LLM-Based Recommendations with Personality Awareness","url":"https://arxiv.org/abs/2504.07801"}]

I found several relevant research papers on LLM simulators, behavioral calibration, and demographic fairness. Here's a summary of the key findings:

## LLM Simulator Reliability and Fairness

Agentic benchmarks increasingly rely on LLM-simulated users to scalably evaluate agent performance, yet the robustness, validity, and fairness of this approach remain unexamined. Recent research has identified critical issues with this approach:

User simulation lacks robustness, with agent success rates varying up to 9 percentage points across different user LLMs. Furthermore, evaluations using simulated users exhibit systematic miscalibration, underestimating agent performance on challenging tasks and overestimating it on moderately difficult ones. African American Vernacular English (AAVE) speakers experience consistently worse success rates and calibration errors than Standard American English (SAE) speakers, with disparities compounding significantly with age.

## Behavioral Calibration Approaches

Statistical calibration combines auxiliary human data with statistical adjustments to account for discrepancies between observed and simulated responses. Under explicit assumptions, statistical calibration preserves validity and provides more precise estimates of causal effects at lower cost than experiments that rely solely on human participants.

Additionally, HMC adjusts the weight of LLM responses based on demographic personas to better align with empirical human behaviors and preferences. Its effectiveness is evaluated in two key applications: preference learning and opinion learning.

## Demographic Fairness in LLM Applications

Research shows broader fairness challenges across LLM applications. While prior studies suggest simple anti-bias prompts can eliminate demographic biases in controlled evaluations, these mitigations fail when realistic contextual details are introduced. Identifying and neutralizing sensitive attribute directions within model activations can achieve robust bias reduction across all tested scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b611bb1e-af32-4013-bb2e-979307701417",
  "isSidechain": true,
  "promptId": "65c9c31a-1745-4148-a2b6-c8121abe6f91",
  "agentId": "a832b9ad296dd183f",
  "type": "user",
  "uuid": "c4d1637a-15a5-4863-b2cf-f1aa47287449",
  "sourceToolAssistantUUID": "b611bb1e-af32-4013-bb2e-979307701417",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T06:27:52.124Z_

<details><summary>↩ Tool result · `toolu_01Ts7B9wXrJtVu2n5vu7a67t`</summary>

```text
Web search results for query: "arXiv user simulation fairness LLM 2026"

Links: [{"title":"[2601.17087] Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations","url":"https://arxiv.org/abs/2601.17087"},{"title":"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations","url":"https://arxiv.org/html/2601.17087v1"},{"title":"A Survey on LLM-based Conversational User Simulation","url":"https://arxiv.org/html/2604.24977"},{"title":"Fairness Evaluation of Large Language Models in Academic Library Reference Services","url":"https://arxiv.org/html/2507.04224v3"},{"title":"[2602.18464] How Well Can LLM Agents Simulate End-User Security and Privacy Attitudes and Behaviors?","url":"https://arxiv.org/abs/2602.18464"},{"title":"Toward Systematic Counterfactual Fairness Evaluation of Large Language Models: The CAFFE Framework","url":"https://arxiv.org/html/2512.16816v1"},{"title":"[2506.10922] Robustly Improving LLM Fairness in Realistic Settings via Interpretability","url":"https://arxiv.org/abs/2506.10922"},{"title":"When to Invoke: Refining LLM Fairness with Toxicity Assessment","url":"https://arxiv.org/html/2601.09250v1"},{"title":"We Need Strong Preconditions For Using Simulations In Policy","url":"https://arxiv.org/html/2604.07838v1"},{"title":"[2602.22752] Towards Simulating Social Media Users with LLMs: Evaluating the Operational Validity of Conditioned Comment Prediction","url":"https://arxiv.org/abs/2602.22752"}]

Here are the search results for "arXiv user simulation fairness LLM 2026":

## Key Findings:

**1. LLM-Simulated Users as Unreliable Evaluation Proxies**

Agentic benchmarks increasingly rely on LLM-simulated users to scalably evaluate agent performance, yet the robustness, validity, and fairness of this approach remain unexamined. A recent paper (2601.17087) from January 2026 addresses these concerns directly. User simulation lacks robustness, with agent success rates varying up to 9 percentage points across different user LLMs. Additionally, African American Vernacular English (AAVE) speakers experience consistently worse success rates and calibration errors than Standard American English (SAE) speakers, with disparities compounding significantly with age.

**2. User Simulation Validity and Bias Concerns**

A benchmark of 30 tests derived from validated S&P human-subject studies measures alignment between simulations and human-subjects studies, and evaluating twelve LLMs, four persona construction strategies, and two prompting methods found that all models score between 50 and 64 on average.

**3. Survey on LLM-based User Simulation**

Recent work (2604.24977) provides a comprehensive survey and notes that these methods have shown promise but also raise concerns around fairness and bias.

**4. Policy Implications**

We struggle to ensure that simulated agents exhibit realistic behaviors rather than stereotypes and to decide when to trust simulated outcomes to inform real decisions.

These 2026 papers highlight significant challenges in using LLM-based user simulations for fair evaluation and decision-making.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a1e9639-f4aa-4fd0-9689-e615706353c8",
  "isSidechain": true,
  "promptId": "65c9c31a-1745-4148-a2b6-c8121abe6f91",
  "agentId": "a832b9ad296dd183f",
  "type": "user",
  "uuid": "e730bcc6-17e9-4273-8986-44f095c8259f",
  "sourceToolAssistantUUID": "3a1e9639-f4aa-4fd0-9689-e615706353c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T06:27:58.393Z_

<details><summary>↩ Tool result · `toolu_0164feKGNrME8uSf4yEqpZkZ`</summary>

```text
Web search results for query: "OpenReview NeurIPS 2026 LLM user simulator evaluation"

Links: [{"title":"NeurIPS 2026 AI-Assisted Reviewing Experiment","url":"https://neurips.cc/Conferences/2026/ai-reviewing-experiment"},{"title":"NeurIPS Faithful Simulation of User–Agent–Environment Interactions for Scalable LLM Agent Evaluation","url":"https://neurips.cc/virtual/2025/loc/san-diego/124569"},{"title":"NeurIPS 2026 Evaluations & Datasets FAQ","url":"https://neurips.cc/Conferences/2026/EvaluationsDatasetsFAQ"},{"title":"A LLM-based Controllable, Scalable, Human-Involved User Simulator Framework for Conversational Recommender Systems | OpenReview","url":"https://openreview.net/forum?id=H9BYGURN9M"},{"title":"Main Track Handbook 2026","url":"https://neurips.cc/Conferences/2026/MainTrackHandbook"},{"title":"Faithful Simulation of User–Agent–Environment ...","url":"https://openreview.net/pdf/dab39dfe908c876a52c542e30e4464376edcc482.pdf"},{"title":"NeurIPS 2026 | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2026"},{"title":"2026 Conference – NeurIPS Blog","url":"https://blog.neurips.cc/category/2026-conference/"},{"title":"RAISE: Reliable Agent Improvement via Simulated Experience","url":"https://openreview.net/pdf?id=53oRwdZe6k"},{"title":"NeurIPS 2025 Workshop LLM Evaluation | OpenReview","url":"https://openreview.net/group?id=NeurIPS.cc%2F2025%2FWorkshop%2FLLM_Evaluation"}]

Based on the search results, I found several relevant items related to your query:

## Key Findings:

**NeurIPS 2026 AI-Assisted Reviewing Experiment:**
NeurIPS 2026 is conducting a voluntary AI-assisted reviewing experiment to study how reviewers do, and could, interact with large language models during peer review, and how different forms of assistance affect review quality, reviewer behavior, and the review process. Participating reviewers will be randomly assigned, per eligible paper, to one of three conditions: (1) no LLM assistance, (2) open-ended LLM assistance, or (3) structured LLM assistance.

**LLM-based User Simulators for Evaluation:**
There are relevant papers on OpenReview discussing LLM-based user simulators:

1. Research efforts have been made to utilize LLMs for building user simulators to evaluate the performance of Conversational Recommender Systems (CRS). One work introduces a Controllable, Scalable, and Human-Involved (CSHI) simulator framework that manages the behavior of user simulators across various stages via a plugin manager.

2. A framework presents a fully automated approach for simulating User–Agent–Environment interactions, providing scalable and faithful interaction data for agent evaluation.

**Evaluations & Datasets Track:**
The NeurIPS 2026 Evaluations & Datasets track includes processes, practices, tools, and resources for making evaluative claims about AI/ML systems, including – but not limited to – datasets, benchmarks, user studies, simulators, auditing, red-teaming methods, interaction protocols, metrics, and experimental or qualitative study designs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1c1e4b7-6002-4bbc-9db5-0c3b39c30c06",
  "isSidechain": true,
  "promptId": "65c9c31a-1745-4148-a2b6-c8121abe6f91",
  "agentId": "a832b9ad296dd183f",
  "type": "user",
  "uuid": "b4641c50-a7fc-4d6e-9ac8-e22e1a78c6ec",
  "sourceToolAssistantUUID": "c1c1e4b7-6002-4bbc-9db5-0c3b39c30c06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T06:27:59.961Z_

Let me conduct additional targeted searches to find more specific concurrent work on this topic.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4641c50-a7fc-4d6e-9ac8-e22e1a78c6ec",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQzE7mK3dE2yVnfktTD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0d309792-0038-4df3-a0a7-ba4cac7f3c22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017ownpeRwsmTx3aEDT5DYmG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 5633,
      "cache_read_input_tokens": 16756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5633,
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

_source line 16 · 2026-05-10T06:28:00.397Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WwpKwBDHCKVoDsx3Jt5SAV`</summary>

```json
{
  "query": "\"Lost in Simulation\" LLM user simulator arXiv 2601"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d309792-0038-4df3-a0a7-ba4cac7f3c22",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQzE7mK3dE2yVnfktTD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "919d6e85-d54e-424d-b10c-6335faad4974",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017ownpeRwsmTx3aEDT5DYmG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 5633,
      "cache_read_input_tokens": 16756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5633,
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

_source line 17 · 2026-05-10T06:28:00.748Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SpyQiDCs6AADX1CG6KtPnP`</summary>

```json
{
  "query": "persona-based simulation demographic LLM arXiv 2603"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "919d6e85-d54e-424d-b10c-6335faad4974",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQzE7mK3dE2yVnfktTD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "67aef4d4-0965-4876-8272-1a11e8085f5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017ownpeRwsmTx3aEDT5DYmG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 5633,
      "cache_read_input_tokens": 16756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5633,
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

_source line 18 · 2026-05-10T06:28:00.817Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JKLCSJ9STkvNrHe6PQPGgs`</summary>

```json
{
  "query": "SPIRIT persona calibration LLM user simulator"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67aef4d4-0965-4876-8272-1a11e8085f5c",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQzE7mK3dE2yVnfktTD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e4577bfd-47ec-4cc3-993d-3252a395c379",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017ownpeRwsmTx3aEDT5DYmG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 5633,
      "cache_read_input_tokens": 16756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5633,
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

_source line 19 · 2026-05-10T06:28:01.036Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019XSTdSjQ9tz3PMVQ8scTv2`</summary>

```json
{
  "query": "site:arxiv.org user simulation behavioral realism demographic 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4577bfd-47ec-4cc3-993d-3252a395c379",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQzE7mK3dE2yVnfktTD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "03e9f417-7ab1-45ee-9b4e-167d9bad6361",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017ownpeRwsmTx3aEDT5DYmG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 893,
      "cache_creation_input_tokens": 5633,
      "cache_read_input_tokens": 16756,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5633
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 893,
          "output_tokens": 229,
          "cache_read_input_tokens": 16756,
          "cache_creation_input_tokens": 5633,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5633,
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

_source line 20 · 2026-05-10T06:28:06.444Z_

<details><summary>↩ Tool result · `toolu_01WwpKwBDHCKVoDsx3Jt5SAV`</summary>

```text
Web search results for query: ""Lost in Simulation" LLM user simulator arXiv 2601"

Links: [{"title":"[2601.17087] Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations","url":"https://arxiv.org/abs/2601.17087"},{"title":"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations","url":"https://arxiv.org/html/2601.17087v1"},{"title":"Mind the Sim2Real Gap in User Simulation for Agentic Tasks","url":"https://arxiv.org/html/2603.11245"},{"title":"(PDF) Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations","url":"https://www.researchgate.net/publication/400083738_Lost_in_Simulation_LLM-Simulated_Users_are_Unreliable_Proxies_for_Human_Users_in_Agentic_Evaluations"},{"title":"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.17087"},{"title":"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations | OpenReview","url":"https://openreview.net/forum?id=pnF8KhgRJJ"},{"title":"GitHub - Persdre/awesome-llm-human-simulation: [ICLR 2025 BlogPost] LLM Simulating Humanity Papers https://arxiv.org/abs/2501.08579 · GitHub","url":"https://github.com/Persdre/llm-human-simulation"},{"title":"Human-Computer Interaction arXiv en X: \"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations Preethi Seshadri, Samuel Cahyawijaya, Ayomide Odumakinde, Sameer Singh, Seraphina Goldfarb-Tarrant https://t.co/4SUGBl88tX [𝚌𝚜.𝙷𝙲 𝚌𝚜.𝙰𝙸 𝚌𝚜.𝙲𝚈 𝚌𝚜.𝙻𝙶] https://t.co/RGUHpAfx3y\" / X","url":"https://x.com/Smartphones/status/2016060825396502711"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** "Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations"

**ArXiv ID:** 2601.17087

**Authors:** Preethi Seshadri, Samuel Cahyawijaya, Ayomide Odumakinde, Sameer Singh, and Seraphina Goldfarb-Tarrant

**Posted:** January 23, 2026

**Key Findings:**

Agentic benchmarks increasingly rely on LLM-simulated users to scalably evaluate agent performance, yet the robustness, validity, and fairness of this approach remain unexamined.

The research addresses three critical issues:

1. **Robustness:** User simulation lacks robustness, with agent success rates varying up to 9 percentage points across different user LLMs.

2. **Validity:** Evaluations using simulated users exhibit systematic miscalibration, underestimating agent performance on challenging tasks and overestimating it on moderately difficult ones.

3. **Fairness:** African American Vernacular English (AAVE) speakers experience consistently worse success rates and calibration errors than Standard American English (SAE) speakers, with disparities compounding significantly with age.

The study involved a user study with participants across the United States, India, Kenya, and Nigeria investigating whether LLM-simulated users serve as reliable proxies for real human users in evaluating agents on τ-Bench retail tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "919d6e85-d54e-424d-b10c-6335faad4974",
  "isSidechain": true,
  "promptId": "65c9c31a-1745-4148-a2b6-c8121abe6f91",
  "agentId": "a832b9ad296dd183f",
  "type": "user",
  "uuid": "c1c0fe8e-d58d-430e-b002-96773ec458af",
  "sourceToolAssistantUUID": "919d6e85-d54e-424d-b10c-6335faad4974",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T06:28:07.548Z_

<details><summary>↩ Tool result · `toolu_01JKLCSJ9STkvNrHe6PQPGgs`</summary>

```text
Web search results for query: "SPIRIT persona calibration LLM user simulator"

Links: [{"title":"Persona-Based Simulation of Human Opinion at Population Scale","url":"https://arxiv.org/html/2603.27056v1"},{"title":"LLM-Based Persona Simulation","url":"https://www.emergentmind.com/topics/llm-based-persona-simulation"},{"title":"The Persona Selection Model: Why AI Assistants might Behave like Humans","url":"https://alignment.anthropic.com/2026/psm/"},{"title":"The persona selection model","url":"https://www.lesswrong.com/posts/dfoty34sT7CSKeJNn/the-persona-selection-model"},{"title":"Persona Effect in LLM Simulations","url":"https://www.emergentmind.com/topics/persona-effect-in-llm-simulations"},{"title":"Quantifying the Persona Effect in LLM Simulations - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.554/"},{"title":"CoSER: Coordinating LLM-Based Persona Simulation of Established Roles | OpenReview","url":"https://openreview.net/forum?id=BOrR7YqKUt"},{"title":"PersonaLLM: Workshop on LLM Persona Modeling — NeurIPS 2025 Workshop","url":"https://personallmworkshop.github.io/"},{"title":"LLM Personas as a Substitute for Field Experiments in Method Benchmarking","url":"https://arxiv.org/pdf/2512.21080"},{"title":"[2402.10811] Quantifying the Persona Effect in LLM Simulations","url":"https://arxiv.org/abs/2402.10811"}]

Based on the search results, here's information about SPIRIT persona calibration for LLM user simulation:

## SPIRIT Framework Overview

SPIRIT is a framework that operates at two levels: at the individual level, it prompts an LLM to adopt a person-specific persona to answer survey questions; at the population level, it combines person-level responses with calibration weights so that aggregates can be interpreted as U.S. population estimates.

## How SPIRIT Works

SPIRIT is a semi-structured persona framework that infers multi-dimensional user representations from social media text that are interpretable and uses them to prompt an LLM to respond to survey questions as the individual represented by the persona would respond.

A probability-based sample from the Ipsos KnowledgePanel is linked to respondents' social media accounts, and their historical posts are collected to infer structured user personas with a painter model. These inferred personas form a persona bank that serves as digital twins for Stage 2 reasoning, where a reasoner model simulates responses to downstream tasks such as survey items.

## Performance Results

SPIRIT persona outperforms demographic persona, producing simulations that are more stable across questions, easier to interpret, and more consistent at both the individual and population levels.

Using the Ipsos KnowledgePanel, a nationally representative probability sample of U.S. adults, SPIRIT-conditioned simulations recover self-reported responses more faithfully than demographic persona and reproduce human-like heterogeneity in response patterns.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e4577bfd-47ec-4cc3-993d-3252a395c379",
  "isSidechain": true,
  "promptId": "65c9c31a-1745-4148-a2b6-c8121abe6f91",
  "agentId": "a832b9ad296dd183f",
  "type": "user",
  "uuid": "bb968e64-0046-4f0e-8a31-95d36dd90522",
  "sourceToolAssistantUUID": "e4577bfd-47ec-4cc3-993d-3252a395c379",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T06:28:07.693Z_

<details><summary>↩ Tool result · `toolu_01SpyQiDCs6AADX1CG6KtPnP`</summary>

```text
Web search results for query: "persona-based simulation demographic LLM arXiv 2603"

Links: [{"title":"Persona-Based Simulation of Human Opinion at Population Scale","url":"https://arxiv.org/html/2603.27056v1"},{"title":"Parametric Social Identity Injection and Diversification in Public Opinion Simulation","url":"https://arxiv.org/html/2603.16142"},{"title":"Population-Aligned Persona Generation for LLM-based Social Simulation","url":"https://arxiv.org/html/2509.10127v1"},{"title":"How to Model AI Agents as Personas?: Applying the Persona Ecosystem Playground to 41,300 Posts on Moltbook for Behavioral Insights","url":"https://arxiv.org/html/2603.03140"},{"title":"[2509.10127] Population-Aligned Persona Generation for LLM-based Social Simulation","url":"https://arxiv.org/abs/2509.10127"},{"title":"Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents","url":"https://arxiv.org/html/2602.18462v1"},{"title":"The Need for a Socially-Grounded Persona Framework for User Simulation","url":"https://arxiv.org/html/2601.07110"},{"title":"Mixture-of-Personas Language Models for Population Simulation","url":"https://arxiv.org/html/2504.05019v1"},{"title":"Stable Behavior, Limited Variation: Persona Validity in LLM Agents for Urban Sentiment Perception","url":"https://arxiv.org/html/2604.28048"},{"title":"LLM Generated Persona is a Promise with a Catch","url":"https://arxiv.org/pdf/2503.16527"}]

Based on the search results, I found several highly relevant papers on persona-based simulation and demographic LLMs. Here are the key findings:

## Main Papers Found (arXiv 2603 series)

**SPIRIT (Semi-structured Persona Inference and Reasoning for Individualized Trajectories)** - This framework infers psychologically grounded, semi-structured personas from public social media posts, integrating structured attributes (e.g., personality traits and world beliefs) with unstructured narrative text reflecting values, and uses these personas to prompt LLM-based agents to act as specific individuals when answering survey questions or responding to events.

Using the Ipsos KnowledgePanel, a nationally representative probability sample of U.S. adults, SPIRIT-conditioned simulations recover self-reported responses more faithfully than demographic personas and reproduce human-like heterogeneity in response patterns.

## Related Works (2603 series)

**Parametric Social Identity Injection (PSII)** - This framework injects explicit, parametric representations of demographic attributes and value orientations directly into intermediate hidden states of LLMs, enabling fine-grained and controllable identity modulation at the representation level, unlike prompt-based persona conditioning.

## Broader Context on Persona-Based Simulation

A common approach gives the model a short demographic profile (for example age, gender, education), often called a persona, and asks it to answer as if it were a person with that profile. However, most existing approaches remain predictive, relying on demographic correlations rather than representations of individuals themselves.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67aef4d4-0965-4876-8272-1a11e8085f5c",
  "isSidechain": true,
  "promptId": "65c9c31a-1745-4148-a2b6-c8121abe6f91",
  "agentId": "a832b9ad296dd183f",
  "type": "user",
  "uuid": "de48f839-e860-4e1c-9e77-4e16d7b14c3c",
  "sourceToolAssistantUUID": "67aef4d4-0965-4876-8272-1a11e8085f5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T06:28:08.076Z_

<details><summary>↩ Tool result · `toolu_019XSTdSjQ9tz3PMVQ8scTv2`</summary>

```text
Web search results for query: "site:arxiv.org user simulation behavioral realism demographic 2025 2026"

Links: [{"title":"Persona-Based Simulation of Human Opinion at Population Scale","url":"https://arxiv.org/html/2603.27056v1"},{"title":"Simulating and Experimenting with Social Media Mobilization Using LLM Agents","url":"https://arxiv.org/pdf/2510.26494"},{"title":"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations","url":"https://arxiv.org/html/2601.17087"},{"title":"Parametric Social Identity Injection and Diversification in Public Opinion Simulation","url":"https://arxiv.org/html/2603.16142"},{"title":"HAG: Hierarchical Demographic Tree-based Agent Generation for Topic-Adaptive Simulation","url":"https://arxiv.org/html/2601.05656"},{"title":"Synthetic or Authentic? Building Mental Patient Simulators from Longitudinal Evidence","url":"https://arxiv.org/html/2603.22704"},{"title":"Published as a conference paper at ICAIS 2025 FLOCKVOTE: LLM-EMPOWERED","url":"https://www.arxiv.org/pdf/2512.05982"},{"title":"SimSpark: Interactive Simulation of Social Media Behaviors","url":"https://arxiv.org/html/2506.14476"},{"title":"Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents","url":"https://arxiv.org/html/2602.18462"},{"title":"Belief-Sim: Towards Belief-Driven Simulation of Demographic Misinformation Susceptibility","url":"https://arxiv.org/html/2603.03585"}]

Based on the web search results from arXiv, I found several recent papers (2025-2026) on user simulation, behavioral realism, and demographics. Here's a summary of the key findings:

## Recent Research on User Simulation and Demographic Realism

### Core Challenges Identified

Demographic persona conditioning can appear competitively accurate on some attributes while still producing degenerate response patterns, as demographic persona inference tends to rely on population-level shortcuts, leading to low-confidence, low-diversity predictions.

Simulated users exhibit notable demographic biases and perform particularly poorly as proxies for African American Vernacular English speakers, with disparities compounding with age.

### Approaches to Improve Behavioral Realism

Recent work contributes by embedding demographic realism, real-world network structure, and experimental control into a unified modeling environment.

One approach focuses on enriching personas using detailed survey responses or text produced by the simulated individual, such as life narratives or interviews, which yields more vivid and coherent simulated responses, improving realism and consistency.

### Applications in Social Simulation

Some frameworks instantiate agents with detailed voter profiles, mirroring the demographic composition based on census data, including key attributes such as state, race, sex, age, occupation, industry, education level, and religion.

The research indicates that while LLM-based user simulation shows promise for computational social science, significant work remains to achieve authentic behavioral realism and equitable representation across demographic groups.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "03e9f417-7ab1-45ee-9b4e-167d9bad6361",
  "isSidechain": true,
  "promptId": "65c9c31a-1745-4148-a2b6-c8121abe6f91",
  "agentId": "a832b9ad296dd183f",
  "type": "user",
  "uuid": "beb510d3-559d-408b-8708-ddf348905348",
  "sourceToolAssistantUUID": "03e9f417-7ab1-45ee-9b4e-167d9bad6361",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T06:28:10.170Z_

Let me do a few more targeted searches to capture any additional key papers I might have missed, particularly focusing on fairness calibration and evaluation methodologies.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "beb510d3-559d-408b-8708-ddf348905348",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQzwWfQcohVLh3VAr9B",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5d3c445d-2463-4de6-af0d-46f5cfc85da5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GVmhyPau764vz1EGN49uZF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4800,
      "cache_read_input_tokens": 22389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4800,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-10T06:28:10.461Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TXc4S8qUhTjNFcGM7qobaw`</summary>

```json
{
  "query": "HMC demographic calibration LLM preference learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d3c445d-2463-4de6-af0d-46f5cfc85da5",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQzwWfQcohVLh3VAr9B",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2d697ffe-5b06-49c8-96c6-f1a2ff8ea824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GVmhyPau764vz1EGN49uZF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4800,
      "cache_read_input_tokens": 22389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4800,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-10T06:28:10.626Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HM5AadzuSjvjv2N11KKxzv`</summary>

```json
{
  "query": "\"Mind the Sim2Real Gap\" user simulation arXiv 2603"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d697ffe-5b06-49c8-96c6-f1a2ff8ea824",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQzwWfQcohVLh3VAr9B",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c4e8bf1c-8473-4dd5-a2ca-0d2d2418fe5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GVmhyPau764vz1EGN49uZF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4800,
      "cache_read_input_tokens": 22389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4800,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-10T06:28:10.813Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SQPXiBHRKdK3YK2M4GZH3z`</summary>

```json
{
  "query": "survey on LLM user simulation arXiv 2604"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4e8bf1c-8473-4dd5-a2ca-0d2d2418fe5f",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatQzwWfQcohVLh3VAr9B",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c5e1913a-5c2f-478a-a523-f4ad674b80b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GVmhyPau764vz1EGN49uZF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4800,
      "cache_read_input_tokens": 22389,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4800
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 195,
          "cache_read_input_tokens": 22389,
          "cache_creation_input_tokens": 4800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4800,
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

_source line 28 · 2026-05-10T06:28:15.694Z_

<details><summary>↩ Tool result · `toolu_01SQPXiBHRKdK3YK2M4GZH3z`</summary>

```text
Web search results for query: "survey on LLM user simulation arXiv 2604"

Links: [{"title":"[2604.24977] A Survey on LLM-based Conversational User Simulation","url":"https://arxiv.org/abs/2604.24977"},{"title":"A Survey on LLM-based Conversational User Simulation","url":"https://arxiv.org/html/2604.24977"},{"title":"An Analysis of Large Language Models for Simulating User Responses in Surveys","url":"https://arxiv.org/html/2512.06874"},{"title":"AgentSim: A Platform for Verifiable Agent-Trace Simulation","url":"https://arxiv.org/html/2604.26653"},{"title":"SLALOM: Simulation Lifecycle Analysis via Longitudinal Observation Metrics for Social Simulation","url":"https://arxiv.org/html/2604.11466"},{"title":"We Need Strong Preconditions For Using Simulations In Policy","url":"https://arxiv.org/html/2604.07838v1"},{"title":"LLM Agents as Social Scientists: A Human–AI Collaborative Platform for Social Science Automation","url":"https://arxiv.org/html/2604.01520"},{"title":"[2502.17773v1] Uncertainty Quantification for LLM-Based Survey Simulations","url":"https://arxiv.org/abs/2502.17773v1"},{"title":"A Survey on the Security of Long-Term Memory in LLM Agents: Toward Mnemonic Sovereignty","url":"https://arxiv.org/html/2604.16548"},{"title":"[2412.03563] From Individual to Society: A Survey on Social Simulation Driven by Large Language Model-based Agents","url":"https://arxiv.org/abs/2412.03563"}]

Based on the search results, I found the survey you're looking for:

## A Survey on LLM-based Conversational User Simulation (arXiv:2604.24977)

This paper surveys recent advancements in LLM-based conversational user simulation, introduces a novel taxonomy covering user granularity and simulation objectives, and systematically analyzes core techniques and evaluation methodologies.

The paper was submitted on April 27, 2026, and was authored by Bo Ni and 29 other co-authors.

Recent advancements in large language models (LLMs) have significantly catalyzed progress in conversational user simulation by enabling high-fidelity generation of synthetic user conversation. The survey aims to keep the research community informed of the latest advancements in conversational user simulation and to further facilitate future research by identifying open challenges and organizing existing work under a unified framework.

You can access the paper at: https://arxiv.org/abs/2604.24977


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5e1913a-5c2f-478a-a523-f4ad674b80b1",
  "isSidechain": true,
  "promptId": "65c9c31a-1745-4148-a2b6-c8121abe6f91",
  "agentId": "a832b9ad296dd183f",
  "type": "user",
  "uuid": "78994e00-14ab-4843-bc76-af5af6b11d05",
  "sourceToolAssistantUUID": "c5e1913a-5c2f-478a-a523-f4ad674b80b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-10T06:28:19.574Z_

<details><summary>↩ Tool result · `toolu_01HM5AadzuSjvjv2N11KKxzv`</summary>

```text
Web search results for query: ""Mind the Sim2Real Gap" user simulation arXiv 2603"

Links: [{"title":"Mind the Sim2Real Gap in User Simulation for Agentic Tasks","url":"https://arxiv.org/html/2603.11245v1"},{"title":"[2603.11245] Mind the Sim2Real Gap in User Simulation for Agentic Tasks","url":"https://arxiv.org/abs/2603.11245"},{"title":"Tendon Force Modeling for Sim2Real Transfer of Reinforcement Learning Policies for Tendon-Driven Robots","url":"https://arxiv.org/html/2603.04351v1"},{"title":"[2603.04351] Tendon Force Modeling for Sim2Real Transfer of Reinforcement Learning Policies for Tendon-Driven Robots","url":"https://arxiv.org/abs/2603.04351"},{"title":"Close the Sim2real Gap via Physically-based Structured Light Synthetic Data Simulation","url":"https://arxiv.org/html/2407.12449v1"},{"title":"Towards Certified Sim-to-Real Transfer via Stochastic Simulation-Gap Functions","url":"https://arxiv.org/html/2603.20672v1"},{"title":"Crossing the Sim2Real Gap Between Simulation and Ground Testing to Space Deployment of Autonomous Free-flyer Control","url":"https://arxiv.org/html/2512.03736"},{"title":"Quantifying the Sim2real Gap for GPS and IMU Sensors","url":"https://arxiv.org/html/2403.11000v1"},{"title":"A Hybrid Approach for Closing the Sim2real Appearance Gap in Game Engine Synthetic Datasets","url":"https://arxiv.org/html/2605.02291v1"},{"title":"[2603.18719] Ontology-Guided Diffusion for Zero-Shot Visual Sim2Real Transfer","url":"https://arxiv.org/abs/2603.18719"}]

I found the paper! Here are the search results for "Mind the Sim2Real Gap" user simulation arXiv 2603:

## Main Result

The paper "Mind the Sim2Real Gap in User Simulation for Agentic Tasks" addresses how LLM-based simulators have become widely used as user proxies in multi-turn interactive NLP evaluation, yet these simulations are frequently assumed to be faithful to real human behaviors without rigorous verification.

### Key Findings

The study presents the first full τ-bench protocol study with real humans (451 participants, 165 tasks), benchmarking 31 LLM simulators using the User-Sim Index (USI), a metric introduced to quantify how well LLM simulators resemble real user interactive behaviors and feedback.

The research found that behaviorally, LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration or ambiguity, creating an "easy mode" that inflates agent success rates above the human baseline.

### Research Questions Addressed

The study found that LLM simulators diverge from real humans along four behavioral dimensions; LLM-based evaluators systematically inflate interaction quality ratings; and rule-based rewards are largely orthogonal to human-perceived quality.

The paper was published on March 11, 2026, and is available at arXiv:2603.11245.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4e8bf1c-8473-4dd5-a2ca-0d2d2418fe5f",
  "isSidechain": true,
  "promptId": "65c9c31a-1745-4148-a2b6-c8121abe6f91",
  "agentId": "a832b9ad296dd183f",
  "type": "user",
  "uuid": "23bc4566-1dfd-42b7-a211-3219a7a7f9fe",
  "sourceToolAssistantUUID": "c4e8bf1c-8473-4dd5-a2ca-0d2d2418fe5f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T06:28:22.650Z_

<details><summary>↩ Tool result · `toolu_01TXc4S8qUhTjNFcGM7qobaw`</summary>

```text
Web search results for query: "HMC demographic calibration LLM preference learning 2026"

Links: [{"title":"Reduce Disparity Between LLMs and Humans: Optimal LLM Sample Calibration by Yan Leng, Yunxin Sang, Ashish Agarwal :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4802019"},{"title":"Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework | OpenReview","url":"https://openreview.net/forum?id=kVaE2kYjtV"},{"title":"Probing and Repairing Reward Models across Human ...","url":"https://aclanthology.org/2025.findings-emnlp.183.pdf"},{"title":"[2603.04409] Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework","url":"https://arxiv.org/abs/2603.04409"},{"title":"Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework","url":"https://arxiv.org/html/2603.04409v1"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/725d3f295086b2f4659cae824a7e8caf25898eae.pdf"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2603.04409"},{"title":"A Survey on Human Preference Learning for Aligning Large Language Models | ACM Computing Surveys","url":"https://dl.acm.org/doi/full/10.1145/3773279"},{"title":"LLM Evaluation: Benchmarks to Test Model Quality in 2026 | Label Your Data","url":"https://labelyourdata.com/articles/llm-fine-tuning/llm-evaluation"},{"title":"DataVLab | Human LLM Evaluation 2026: Practical Guide for AI Teams","url":"https://datavlab.ai/post/human-llm-evaluation-2026-practical-guide"}]

Based on the web search results, I found relevant research on this topic. Here's what the search revealed:

## Key Findings

**HMC (Hamiltonian Monte Carlo) in Demographic Calibration:**

In preference learning, HMC helps LLM responses to reflect consumer purchasing behaviors more accurately, improving the accuracy of inferred market structures. In opinion learning, calibrated LLMs more accurately represent human public opinions.

HMC-calibrated sample weights can be transferred across different contexts. HMC, when calibrated in one US state, can effectively improve the accuracy of market structures in others, demonstrating spatial transferability.

**Demographic-Aware LLM Evaluation (2026):**

A more recent 2026 framework called HUMAINE addresses demographic preferences in LLM evaluation. HUMAINE is a framework for multidimensional, demographically aware measurement of human-AI interaction, collecting multi-turn conversations from 23,404 participants stratified across 22 demographic groups in the US and UK to evaluate 28 state-of-the-art models.

The analysis reveals that user age is the primary demographic axis of disagreement, with a model's perceived rank potentially shifting substantially across age groups.

These research efforts highlight the growing importance of ensuring that LLM preference learning and calibration account for demographic heterogeneity to improve model fairness and representation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d697ffe-5b06-49c8-96c6-f1a2ff8ea824",
  "isSidechain": true,
  "promptId": "65c9c31a-1745-4148-a2b6-c8121abe6f91",
  "agentId": "a832b9ad296dd183f",
  "type": "user",
  "uuid": "13464b38-4475-4377-b0f6-6d589c881ee4",
  "sourceToolAssistantUUID": "2d697ffe-5b06-49c8-96c6-f1a2ff8ea824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-10T06:28:42.535Z_

Perfect. Now I have comprehensive information on recent research in this area. Let me compile the final report.

## RESEARCH REPORT: Demographic Calibration for LLM-Based User Simulators (2025-2026)

Based on my comprehensive search of recent academic literature, I've identified several highly relevant papers that represent direct concurrent work on demographic calibration and fairness in LLM-based user simulators. Here are the key findings:

### PRIMARY CONCURRENT WORKS (Direct Match to Your Research)

**1. "Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations"**
- **ArXiv ID:** 2601.17087 (January 2026)
- **Authors:** Preethi Seshadri, Samuel Cahyawijaya, Ayomide Odumakinde, Sameer Singh, Seraphina Goldfarb-Tarrant
- **Venue:** ICLR 2026 (found on OpenReview)
- **Direct Relevance:** This is highly directly relevant—it identifies critical demographic fairness issues in LLM-based user simulation. The paper finds that African American Vernacular English (AAVE) speakers experience consistently worse success rates and calibration errors than Standard American English (SAE) speakers, with disparities compounding with age. They evaluate 12 different LLMs with various persona construction strategies and prompting methods against a τ-Bench protocol with real human participants across 4 countries.

**2. "Persona-Based Simulation of Human Opinion at Population Scale" (SPIRIT Framework)**
- **ArXiv ID:** 2603.27056 (March 2026)
- **Venue:** Published/submitted March 2026
- **Direct Relevance:** Directly addresses demographic calibration through the SPIRIT framework, which moves beyond simple demographic personas to semi-structured personas grounded in social media text. Shows that demographic persona conditioning alone produces degenerate response patterns due to population-level shortcut reliance. SPIRIT recovers self-reported responses more faithfully using nationally representative Ipsos KnowledgePanel data with 45,000+ individuals.

**3. "Mind the Sim2Real Gap in User Simulation for Agentic Tasks"**
- **ArXiv ID:** 2603.11245 (March 2026)
- **Direct Relevance:** Benchmarks 31 different LLM simulators using the User-Sim Index (USI) metric to quantify behavioral fidelity to real humans. Conducted with 451 real participants across 165 tasks. Finds that LLM simulators are excessively cooperative, stylistically uniform, and lack realistic behavioral variation—creating systematic evaluation bias.

**4. "Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework"**
- **ArXiv ID:** 2603.04409 (March 2026)
- **Venue:** ICLR 2026
- **Direct Relevance:** Framework for multidimensional, demographically aware evaluation of LLM responses. Collected multi-turn conversations from 23,404 participants stratified across 22 demographic groups in the US and UK. Shows that user age is the primary demographic axis of disagreement, with model rankings shifting substantially across age groups.

**5. "Parametric Social Identity Injection and Diversification in Public Opinion Simulation"**
- **ArXiv ID:** 2603.16142 (March 2026)
- **Direct Relevance:** Proposes explicit, parametric injection of demographic attributes and value orientations directly into LLM hidden states, enabling fine-grained demographic control at the representation level, unlike prompt-based persona conditioning.

### RELATED SUPPORTING WORKS (Broader Context)

**6. "Reduce Disparity Between LLMs and Humans: Optimal LLM Sample Calibration"**
- **SSRN Abstract ID:** 4802019
- **Direct Relevance:** Introduces HMC-based demographic calibration for LLM responses in preference learning and opinion learning tasks. Shows that calibration weights are transferable across contexts (demonstrated across US states for market structure prediction).

**7. "A Survey on LLM-based Conversational User Simulation"**
- **ArXiv ID:** 2604.24977 (April 2026)
- **Direct Relevance:** Comprehensive survey covering 29+ co-authors reviewing advances in LLM-based conversational user simulation, including taxonomy of user granularity, simulation objectives, evaluation methodologies, and identifies fairness/bias as open challenges.

**8. "How Well Can LLM Agents Simulate End-User Security and Privacy Attitudes and Behaviors?"**
- **ArXiv ID:** 2602.18464 (February 2026)
- **Relevant Context:** Tests behavioral fidelity of LLM agents in simulating human security/privacy attitudes, finding gaps in behavioral realism.

**9. "Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents"**
- **ArXiv ID:** 2602.18462 (February 2026)
- **Relevant Context:** Specifically evaluates whether persona-conditioned LLMs reliably simulate survey respondent behavior across demographic segments.

### KEY THEMES ACROSS THE LITERATURE

1. **Demographic Persona Limitations:** All papers converge on the finding that simple demographic personas (age, gender, education) are insufficient—they explain ~1.5% of variance in human behavior and create degenerate, low-diversity response patterns.

2. **Fairness Gaps:** Multiple papers identify systematic disparities, with AAVE speakers, marginalized demographics, and certain age groups experiencing worse calibration and behavioral realism in LLM simulations.

3. **Calibration Approaches:**
   - SPIRIT: Semi-structured personas grounded in real behavioral text
   - HUMAINE: Demographic stratification in evaluation data collection
   - HMC: Statistical weight calibration
   - PSII: Parametric demographic injection at representation level

4. **Evaluation Methodologies:** Papers increasingly employ large-scale real human studies to ground truth LLM simulator behavior (451-23,404 participants across recent papers).

### ASSESSMENT

**High Overlap with Your Proposed Work:** The papers identified above, particularly "Lost in Simulation" (2601.17087) and the SPIRIT framework (2603.27056), represent direct concurrent work on demographically-calibrated LLM user simulation for fair evaluation. Both papers identify the core problem and propose different solutions (behavioral validation vs. semi-structured persona grounding). The HUMAINE framework adds the demographic stratification evaluation angle.

**Window for Differentiation:** Your work would be most valuable if it:
- Proposes a novel calibration methodology beyond SPIRIT, HUMAINE, and PSII
- Focuses on a specific evaluation context/task not yet covered
- Develops new metrics for measuring calibration quality across demographics
- Addresses the Sim2Real gap more comprehensively than existing work

Sources:
- [Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations](https://arxiv.org/abs/2601.17087)
- [Persona-Based Simulation of Human Opinion at Population Scale](https://arxiv.org/html/2603.27056v1)
- [Mind the Sim2Real Gap in User Simulation for Agentic Tasks](https://arxiv.org/abs/2603.11245)
- [Unpacking Human Preference for LLMs: Demographically Aware Evaluation with the HUMAINE Framework](https://arxiv.org/abs/2603.04409)
- [Parametric Social Identity Injection and Diversification in Public Opinion Simulation](https://arxiv.org/html/2603.16142)
- [Reduce Disparity Between LLMs and Humans: Optimal LLM Sample Calibration](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4802019)
- [A Survey on LLM-based Conversational User Simulation](https://arxiv.org/abs/2604.24977)
- [How Well Can LLM Agents Simulate End-User Security and Privacy Attitudes and Behaviors?](https://arxiv.org/abs/2602.18464)
- [Assessing the Reliability of Persona-Conditioned LLMs as Synthetic Survey Respondents](https://arxiv.org/abs/2602.18462)
- [Mind the Sim2Real Gap in User Simulation for Agentic Tasks (OpenReview)](https://openreview.net/forum?id=m57vJLBHxA)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13464b38-4475-4377-b0f6-6d589c881ee4",
  "isSidechain": true,
  "agentId": "a832b9ad296dd183f",
  "requestId": "req_011CatR21peXZWKvtm3uworq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f023186f-01a6-47db-abf4-04b94121b6ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6f9dd2ec-2541-4890-8b0e-a97a16307e26",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Vp8Gt4AA36FqmcbEZ2Weis",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1552,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 27189,
      "output_tokens": 2049,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1101
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1552,
          "output_tokens": 2049,
          "cache_read_input_tokens": 27189,
          "cache_creation_input_tokens": 1101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1101,
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
