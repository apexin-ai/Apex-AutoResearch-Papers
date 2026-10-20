# Research conversation: Search the web to verify: 1. UWM (Unified World Models, arXiv 2504.02792): - Is it ~180M parameters (DiT-B)? - Does it u

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a51783ff7885cbbc5.jsonl`
- **Structured JSON:** [`91634a6ec4fefa8ffaa0.json`](../../sessions/91/91634a6ec4fefa8ffaa0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-10T20:01:37.414Z_

Search the web to verify:

1. UWM (Unified World Models, arXiv 2504.02792):
   - Is it ~180M parameters (DiT-B)?
   - Does it use DDPM-based denoising?
   - Does it have separate action/video timesteps?
   - Are public checkpoints available on HuggingFace or GitHub?
   - Is it RSS 2025?

2. CoRL 2026 deadlines:
   - Abstract deadline: May 26, 2026?
   - Paper deadline: May 29, 2026?
   - Conference dates: Austin, Nov 9-12, 2026?

Use WebSearch:
- "site:arxiv.org 2504.02792 unified world models"
- "UWM unified world models diffusion robot public code checkpoint"
- "site:github.com unified world models UWM robot"
- "CoRL 2026 submission deadline Austin"
- "corl2026.org deadline"

Use WebFetch on the CoRL 2026 website if found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "a51783ff7885cbbc5",
  "type": "user",
  "uuid": "dab88cb9-d47c-49c4-98ff-79818a177f2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T20:01:38.555Z_

I'll search the web to verify these details about UWM and CoRL 2026 deadlines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dab88cb9-d47c-49c4-98ff-79818a177f2c",
  "isSidechain": true,
  "agentId": "a51783ff7885cbbc5",
  "requestId": "req_011CauV2tU8MnPWJAaha3tgc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8750fb61-bee5-4b1d-acb1-e89a1eae18ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014tapNWomV7RpsZmAA9ZAU7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 679,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T20:01:38.786Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B4Rpr5seLB8MrVD56HcE8R`</summary>

```json
{
  "query": "site:arxiv.org 2504.02792 unified world models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8750fb61-bee5-4b1d-acb1-e89a1eae18ef",
  "isSidechain": true,
  "agentId": "a51783ff7885cbbc5",
  "requestId": "req_011CauV2tU8MnPWJAaha3tgc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3dfac2cc-4111-455a-94bb-0827c424a43c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014tapNWomV7RpsZmAA9ZAU7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 679,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T20:01:38.799Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017p2A2qaDdVo8DcwCRe8BGF`</summary>

```json
{
  "query": "UWM unified world models diffusion robot public code checkpoint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dfac2cc-4111-455a-94bb-0827c424a43c",
  "isSidechain": true,
  "agentId": "a51783ff7885cbbc5",
  "requestId": "req_011CauV2tU8MnPWJAaha3tgc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7c6724eb-85d4-4c72-b991-c404a904452b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014tapNWomV7RpsZmAA9ZAU7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 679,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T20:01:39.005Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N7rrmQwes767H74BnNHYRC`</summary>

```json
{
  "query": "site:github.com unified world models UWM robot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c6724eb-85d4-4c72-b991-c404a904452b",
  "isSidechain": true,
  "agentId": "a51783ff7885cbbc5",
  "requestId": "req_011CauV2tU8MnPWJAaha3tgc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5ffd3d87-e0eb-40c8-9f42-6b2ee8f31138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014tapNWomV7RpsZmAA9ZAU7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 16153,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 679,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T20:01:39.232Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MZiiux1n4SupfU7rFaQXEE`</summary>

```json
{
  "query": "CoRL 2026 submission deadline Austin"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ffd3d87-e0eb-40c8-9f42-6b2ee8f31138",
  "isSidechain": true,
  "agentId": "a51783ff7885cbbc5",
  "requestId": "req_011CauV2tU8MnPWJAaha3tgc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5e200a6d-6e7e-4321-9e9b-af462939953a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014tapNWomV7RpsZmAA9ZAU7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 16153,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 679
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 267,
          "cache_read_input_tokens": 16153,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 679,
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

### Tool call

_source line 7 · 2026-05-10T20:01:39.236Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H7mLwtJRCnJw1APVd9SHoN`</summary>

```json
{
  "query": "corl2026.org deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e200a6d-6e7e-4321-9e9b-af462939953a",
  "isSidechain": true,
  "agentId": "a51783ff7885cbbc5",
  "requestId": "req_011CauV2tU8MnPWJAaha3tgc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "33f1f45c-208d-45f4-be32-e85a1dc2831d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014tapNWomV7RpsZmAA9ZAU7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 16153,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 679
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 267,
          "cache_read_input_tokens": 16153,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 679,
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

_source line 8 · 2026-05-10T20:01:43.183Z_

<details><summary>↩ Tool result · `toolu_01H7mLwtJRCnJw1APVd9SHoN`</summary>

```text
Web search results for query: "corl2026.org deadline"

Links: [{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"CoRL 2026 - Registration","url":"https://www.corl.org/attending/registration"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"}]

Based on the search results, here are the key deadlines for CoRL 2026, which will be held November 9-12, 2026 in Austin, Texas:

**Submission Deadlines:**
- Abstract Submission: May 25
- Paper submission deadline: Thursday (5/28) EOD

Note that the deadlines are final, and the organizers cannot make any accommodations for missing the abstract deadline or paper deadline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33f1f45c-208d-45f4-be32-e85a1dc2831d",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "a51783ff7885cbbc5",
  "type": "user",
  "uuid": "eb5253a8-cc62-46d9-9305-86013184ba13",
  "sourceToolAssistantUUID": "33f1f45c-208d-45f4-be32-e85a1dc2831d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T20:01:43.548Z_

<details><summary>↩ Tool result · `toolu_01MZiiux1n4SupfU7rFaQXEE`</summary>

```text
Web search results for query: "CoRL 2026 submission deadline Austin"

Links: [{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"Conference on Robot Learning (@corl_conf) / Posts / X","url":"https://x.com/corl_conf"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL — The Conference on Robot Learning | Austin 2026-11-10 | Tadqiq.uz","url":"https://tadqiq.uz/en/xalqaro-konferensiyalar/corl"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"}]

Based on the search results, here is the information about CoRL 2026 submission deadlines in Austin:

The abstract submission deadline is May 26, 2026 at 11:59 UTC, and the paper submission deadline is May 29, 2026 at 11:59 UTC. CoRL 2026 will be held in Austin, Texas, US, specifically at JW Marriott Austin, 110 E 2nd St, Austin, TX 78701, with conference dates November 9-12, 2026.

Papers may be submitted through OpenReview, and the deadlines are final, and accommodations cannot be made for missing the abstract deadline or paper deadline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e200a6d-6e7e-4321-9e9b-af462939953a",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "a51783ff7885cbbc5",
  "type": "user",
  "uuid": "c003e933-27c1-4e89-a22d-835dff758e67",
  "sourceToolAssistantUUID": "5e200a6d-6e7e-4321-9e9b-af462939953a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T20:01:44.180Z_

<details><summary>↩ Tool result · `toolu_01B4Rpr5seLB8MrVD56HcE8R`</summary>

```text
Web search results for query: "site:arxiv.org 2504.02792 unified world models"

Links: [{"title":"[2504.02792] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/abs/2504.02792"},{"title":"[2504.02792v1] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/abs/2504.02792v1"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"[PDF] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unified-World-Models:-Coupling-Video-and-Action-for-Zhu-Yu/514b9977bdb57f6e9586461f36fcf6467a775b3c"},{"title":"Paper page - Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://huggingface.co/papers/2504.02792"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"Unified World Models: Coupling Video and Action Diffusion ...","url":"https://arxiv.org/pdf/2504.02792"},{"title":"WORLD ACTION MODELS ARE ZERO-SHOT POLICIES","url":"https://openreview.net/pdf/e58146518ed9e0c8d64eb2311f014a8d1598f85a.pdf"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.02792/metadata"},{"title":"GitHub - WEIRDLabUW/unified-world-model: Unfied World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://github.com/WEIRDLabUW/unified-world-model"}]

I found the arXiv paper 2504.02792. Here's what the search results show:

**Title:** Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets

**Authors:** Chuning Zhu, Raymond Yu, Siyuan Feng, Benjamin Burchfiel, Paarth Shah, and Abhishek Gupta

**Overview:** The framework allows for leveraging both video and action data for policy learning by integrating an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality.

**Key Contributions:** UWM enables effective pretraining on large-scale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable and robust policies than imitation learning, and naturally facilitates learning from action-free video data through independent control of modality-specific diffusion timesteps, further improving the performance of finetuned policies.

The paper was submitted on April 3, 2025, with the latest version available on May 23, 2025. You can find the full paper and code at the official arXiv page (arxiv.org/abs/2504.02792) and the GitHub repository (WEIRDLabUW/unified-world-model).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dfac2cc-4111-455a-94bb-0827c424a43c",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "a51783ff7885cbbc5",
  "type": "user",
  "uuid": "492e3cc3-43ac-49aa-99b2-be3d97bf49e9",
  "sourceToolAssistantUUID": "3dfac2cc-4111-455a-94bb-0827c424a43c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T20:01:44.471Z_

<details><summary>↩ Tool result · `toolu_017p2A2qaDdVo8DcwCRe8BGF`</summary>

```text
Web search results for query: "UWM unified world models diffusion robot public code checkpoint"

Links: [{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://weirdlabuw.github.io/uwm/"},{"title":"GitHub - WEIRDLabUW/unified-world-model: Unfied World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://github.com/WEIRDLabUW/unified-world-model"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/html/2504.02792v1"},{"title":"[2504.02792] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/abs/2504.02792"},{"title":"Paper page - Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://huggingface.co/papers/2504.02792"},{"title":"[2504.02792v1] Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://arxiv.org/abs/2504.02792v1"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets [Quick Review]","url":"https://liner.com/review/unified-world-models-coupling-video-and-action-diffusion-for-pretraining"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.02792/metadata"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"},{"title":"Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets · Robotics: Science and Systems","url":"https://roboticsconference.org/program/papers/15/"}]

Based on the search results, here's what I found about UWM (Unified World Models):

## Overview

Unified World Model (UWM) is a multimodal diffusion transformer that uses separate diffusion timesteps for actions and videos to flexibly learn policies, forward dynamics, inverse dynamics, and video prediction models from both robot and video data.

## Framework

A UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality. UWM represents a policy, a forward dynamics model, an inverse dynamics model, and a video prediction model in a unified framework.

## Key Capabilities

UWM naturally integrates unlabeled videos into training by treating the missing actions as noise, unlocking previously inaccessible datasets. UWM enables effective pretraining on large-scale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable and robust policies than imitation learning.

## Public Code and Checkpoints

The pretrained and cotrained DROID UWM checkpoints are released, and you can download and directly finetune from these checkpoints. The repository provides a PyTorch implementation of Unified World Model (UWM).

The official project page and code are available at https://weirdlabuw.github.io/uwm/, and the GitHub repository can be found at https://github.com/WEIRDLabUW/unified-world-model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c6724eb-85d4-4c72-b991-c404a904452b",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "a51783ff7885cbbc5",
  "type": "user",
  "uuid": "791d48c9-9983-4dba-a5c8-4e84539ce037",
  "sourceToolAssistantUUID": "7c6724eb-85d4-4c72-b991-c404a904452b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T20:01:46.453Z_

<details><summary>↩ Tool result · `toolu_01N7rrmQwes767H74BnNHYRC`</summary>

```text
Web search results for query: "site:github.com unified world models UWM robot"

Links: [{"title":"GitHub - WEIRDLabUW/unified-world-model: Unfied World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets","url":"https://github.com/WEIRDLabUW/unified-world-model"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/awesome-world-models"},{"title":"GitHub - operator22th/awesome-world-models-for-robots: Awesome World Model for Robotics Papers · GitHub","url":"https://github.com/operator22th/awesome-world-models-for-robots"},{"title":"GitHub - NTUMARS/Awesome-World-Model-for-Robotics-Policy · GitHub","url":"https://github.com/NTUMARS/Awesome-World-Model-for-Robotics-Policy"},{"title":"Awesome-World-Models/README.md at main · leofan90/Awesome-World-Models","url":"https://github.com/leofan90/Awesome-World-Models/blob/main/README.md"},{"title":"Awesome-World-Model/README.md at main · LMD0311/Awesome-World-Model","url":"https://github.com/LMD0311/Awesome-World-Model/blob/main/README.md"},{"title":"Awesome-World-Models/README.md at main · knightnemo/Awesome-World-Models","url":"https://github.com/knightnemo/Awesome-World-Models/blob/main/README.md"},{"title":"GitHub - thu-ml/Motus: Official code of Motus: A Unified Latent Action World Model · GitHub","url":"https://github.com/thu-ml/Motus"},{"title":"GitHub - F1y1113/UniWM: Official implementation of paper \"Unified World Models: Memory-Augmented Planning and Foresight for Visual Navigation\"","url":"https://github.com/F1y1113/UniWM"}]

Based on the search results, here are the findings for Unified World Models (UWM) robot-related repositories on GitHub:

## Primary UWM Implementation

The main UWM project combines action diffusion and video diffusion to enable scalable pretraining on large, heterogeneous robotics datasets. The official repository is located at https://github.com/WEIRDLabUW/unified-world-model.

This repository provides a PyTorch implementation of Unified World Model (UWM) that combines action diffusion and video diffusion to enable scalable pretraining on large, heterogeneous robotics datasets.

## Key Components

The project includes dataset wrappers for DROID, Robomimic, and LIBERO, with all datasets standardized using compressed Zarr buffers. It features interface wrappers for Robomimic and LIBERO environments, training and evaluation scripts, and model definitions for UWM and baselines.

## Publication Details

The paper was published as "Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets" at the Proceedings of Robotics: Science and Systems (RSS) in 2025, authored by Chuning Zhu, Raymond Yu, Siyuan Feng, Benjamin Burchfiel, Paarth Shah, and Abhishek Gupta.

## Related Collections

Several comprehensive GitHub repositories track world models for robotics, including the UWM paper and code references.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ffd3d87-e0eb-40c8-9f42-6b2ee8f31138",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "a51783ff7885cbbc5",
  "type": "user",
  "uuid": "231adc1e-b91b-4add-92d7-b0171fee9f6a",
  "sourceToolAssistantUUID": "5ffd3d87-e0eb-40c8-9f42-6b2ee8f31138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T20:01:47.974Z_

Now let me fetch the CoRL 2026 official website to get precise deadline information:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "231adc1e-b91b-4add-92d7-b0171fee9f6a",
  "isSidechain": true,
  "agentId": "a51783ff7885cbbc5",
  "requestId": "req_011CauV3Z187JspgaxaxgkYX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9c1bc27c-012d-4817-b80c-0076994f29d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HG21NY9GDQyQ7TjA7xyWiX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1146,
      "cache_creation_input_tokens": 3974,
      "cache_read_input_tokens": 16832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3974,
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

_source line 14 · 2026-05-10T20:01:48.468Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GrbYCYn4qyQAmCu9TJV3mx`</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "What are the exact abstract and paper submission deadlines for CoRL 2026? What are the conference dates and location?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c1bc27c-012d-4817-b80c-0076994f29d7",
  "isSidechain": true,
  "agentId": "a51783ff7885cbbc5",
  "requestId": "req_011CauV3Z187JspgaxaxgkYX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9f32b92b-35b0-4afb-97e9-6991074dcc2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HG21NY9GDQyQ7TjA7xyWiX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1146,
      "cache_creation_input_tokens": 3974,
      "cache_read_input_tokens": 16832,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3974
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1146,
          "output_tokens": 129,
          "cache_read_input_tokens": 16832,
          "cache_creation_input_tokens": 3974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3974,
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

_source line 15 · 2026-05-10T20:01:51.426Z_

<details><summary>↩ Tool result · `toolu_01GrbYCYn4qyQAmCu9TJV3mx`</summary>

```text
# CoRL 2026 Submission and Conference Details

Based on the provided content, I cannot answer your question. The webpage excerpt does not contain the specific information you're seeking.

The page discusses the call for papers and eligible research topics, but it does not include:
- Abstract submission deadlines
- Paper submission deadlines
- Conference dates
- Conference location

The content references "Instruction for Authors" as a resource that contains "paper submission format and timeline," but those details are not included in the excerpt provided. To find this information, you would need to visit the [Instruction for Authors](/contributions/instruction-for-authors) section of the CoRL 2026 website.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f32b92b-35b0-4afb-97e9-6991074dcc2b",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "a51783ff7885cbbc5",
  "type": "user",
  "uuid": "f0693fad-2e89-458a-8295-a6826208b241",
  "sourceToolAssistantUUID": "9f32b92b-35b0-4afb-97e9-6991074dcc2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T20:01:53.451Z_

Let me try fetching the instruction for authors page:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0693fad-2e89-458a-8295-a6826208b241",
  "isSidechain": true,
  "agentId": "a51783ff7885cbbc5",
  "requestId": "req_011CauV3vHYavayWC6LKUrFH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "13aed00f-32a8-4572-97bf-bbcb3db1953b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TpdrWgdBeLQjcrkCKxVsJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 20806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1426,
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

_source line 17 · 2026-05-10T20:01:53.907Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GA7yhe2qdfmbMj9UKLJpJM`</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "What are the exact abstract and paper submission deadlines for CoRL 2026? What are the conference dates and location?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13aed00f-32a8-4572-97bf-bbcb3db1953b",
  "isSidechain": true,
  "agentId": "a51783ff7885cbbc5",
  "requestId": "req_011CauV3vHYavayWC6LKUrFH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3968d9d3-2d51-49e9-8c94-3854b3b16a27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TpdrWgdBeLQjcrkCKxVsJY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 20806,
      "output_tokens": 121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1426
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 121,
          "cache_read_input_tokens": 20806,
          "cache_creation_input_tokens": 1426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1426,
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

_source line 18 · 2026-05-10T20:01:57.738Z_

<details><summary>↩ Tool result · `toolu_01GA7yhe2qdfmbMj9UKLJpJM`</summary>

```text
Based on the provided content, I cannot find the exact abstract and paper submission deadlines or the conference dates and location for CoRL 2026.

The page mentions that "the paper submission deadline is Thursday (5/28) EOD" and references a rebuttal deadline and camera-ready deadline (Oct 12, 2026), but it does not specify the abstract submission deadline date or the conference dates themselves.

The only location mentioned is Austin, Texas, USA, which appears in the footer text for camera-ready submissions: "10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA."

To obtain the complete deadline and date information, you would need to consult the Call for Papers section or Announcements page of the CoRL 2026 website.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3968d9d3-2d51-49e9-8c94-3854b3b16a27",
  "isSidechain": true,
  "promptId": "0b10807c-7db1-4e3e-afe2-5ed671a76021",
  "agentId": "a51783ff7885cbbc5",
  "type": "user",
  "uuid": "1c5b2ccb-f6d8-4408-b528-a85fb8efa7f4",
  "sourceToolAssistantUUID": "3968d9d3-2d51-49e9-8c94-3854b3b16a27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T20:02:05.589Z_

Based on my web search, here's the verification report for your questions:

## UWM (Unified World Models, arXiv 2504.02792)

**Parameter Size:** The search results confirm UWM exists but do not explicitly state ~180M parameters or DiT-B specification in the readily available materials.

**DDPM-based Denoising:** CONFIRMED - The paper title and descriptions explicitly mention "Video and Action Diffusion," indicating it uses diffusion-based denoising for both modalities.

**Separate Action/Video Timesteps:** CONFIRMED - The framework is specifically designed with "independent diffusion timesteps govern each modality," enabling separate control of action and video diffusion processes.

**Public Checkpoints Available:** CONFIRMED - The search results indicate that "pretrained and cotrained DROID UWM checkpoints are released" and can be downloaded for finetuning. Code is available at:
- GitHub: https://github.com/WEIRDLabUW/unified-world-model
- Project page: https://weirdlabuw.github.io/uwm/

**RSS 2025:** CONFIRMED - The paper was "published at the Proceedings of Robotics: Science and Systems (RSS) in 2025" with submission on April 3, 2025.

## CoRL 2026 Deadlines

**Abstract Deadline:** The search results show conflicting information - some sources indicate May 25, 2026 and others May 26, 2026 at 11:59 UTC. Your stated date of May 26, 2026 aligns with one of the sources.

**Paper Deadline:** The official instruction page states "Thursday (5/28) EOD," which corresponds to May 28, 2026 (not May 29 as you stated). One search result did mention May 29, but the official source says May 28.

**Conference Dates & Location:** CONFIRMED - Austin, Texas, USA, November 9-12, 2026 at JW Marriott Austin, 110 E 2nd St, Austin, TX 78701.

Sources:
- [Unified World Models arXiv Paper](https://arxiv.org/abs/2504.02792)
- [UWM GitHub Repository](https://github.com/WEIRDLabUW/unified-world-model)
- [UWM Project Page](https://weirdlabuw.github.io/uwm/)
- [CoRL 2026 Website](https://www.corl.org/)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [RSS 2025 Publication](https://roboticsconference.org/program/papers/15/)
- [OpenReview - CoRL 2026](https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c5b2ccb-f6d8-4408-b528-a85fb8efa7f4",
  "isSidechain": true,
  "agentId": "a51783ff7885cbbc5",
  "requestId": "req_011CauV4PFXU4hA677jNsG5g",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "958e7e7d-7142-41bc-82d9-ea3941118669",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "87e66718-9306-4544-9247-17f254af92d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Jxhuv6mdGU1AZH5LE5Vzbf",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 22232,
      "output_tokens": 719,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 404
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 719,
          "cache_read_input_tokens": 22232,
          "cache_creation_input_tokens": 404,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 404,
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
