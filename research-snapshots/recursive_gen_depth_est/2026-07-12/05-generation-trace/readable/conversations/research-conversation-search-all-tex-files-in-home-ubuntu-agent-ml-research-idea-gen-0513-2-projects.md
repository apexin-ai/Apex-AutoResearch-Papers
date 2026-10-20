# Research conversation: Search all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/ fo

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a6c7950c9417f13a3.jsonl`
- **Structured JSON:** [`49a14cabadbf29a87f6c.json`](../../sessions/49/49a14cabadbf29a87f6c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

52 recorded events

### User

_source line 1 · 2026-05-15T20:05:32.451Z_

Search all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/ for terminology inconsistencies. Report all matches with file and line numbers for each of these patterns:

1. "hand-crafted" or "handcrafted" (variant of "statistical features")
2. "statistical fingerprint" (as a noun, not "statistical fingerprints")
3. "sampling strategy" or "generation strategy" (vs "decoding strategy")
4. "feature-based method" or "statistical method" (check both)
5. EDD formatting: search for "\text{EDD}" (should be "\mathrm{EDD}")
6. "model family" vs just "model" or "architecture" when referring to Pythia/OLMo/GPT-2 XL groups
7. "statistical features" occurrences

Search breadth: very thorough

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "8fbdfbad-fb0a-4293-9402-3916c516a184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-15T20:05:34.950Z_

I'll conduct a thorough search of all .tex files in the paper directory for these terminology inconsistencies. Let me start by finding all .tex files and then search for each pattern.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fbdfbad-fb0a-4293-9402-3916c516a184",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xNnukF1t7cLgvWCr39",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "33479753-ca4d-4931-a60f-a519bb4eb8ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0162mBQ2HVzyfx9U9pWiM2tK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16948,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16948,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 3 · 2026-05-15T20:05:35.068Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Vfozms9ea2RYLzjC9wRj37`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33479753-ca4d-4931-a60f-a519bb4eb8ec",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xNnukF1t7cLgvWCr39",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "71ef2b68-c240-48ca-98ee-17b94aac4cf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0162mBQ2HVzyfx9U9pWiM2tK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16948,
      "cache_read_input_tokens": 0,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16948
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16948,
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

_source line 4 · 2026-05-15T20:05:35.087Z_

<details><summary>↩ Tool result · `toolu_01Vfozms9ea2RYLzjC9wRj37`</summary>

```text
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
docs/paper/abstract.tex
docs/paper/section_appendix.tex
docs/paper/atlas.tex
docs/paper/method.tex
docs/paper/conclusion.tex
docs/paper/generalization.tex
docs/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71ef2b68-c240-48ca-98ee-17b94aac4cf4",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "225ff6fa-c417-4463-950f-33c453ebdf97",
  "sourceToolAssistantUUID": "71ef2b68-c240-48ca-98ee-17b94aac4cf4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-15T20:05:36.457Z_

Now let me search for each pattern across all these .tex files. I'll do comprehensive searches for all the patterns you specified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "225ff6fa-c417-4463-950f-33c453ebdf97",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xNz3yBnezigfpUAkGs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c209cf3c-6b5e-4bf7-a861-2d0f37506019",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01P7cs2Ub2GqAVLJavMK9kbK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 16948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1059,
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

_source line 6 · 2026-05-15T20:05:37.150Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013vFRAuEU9LWjPMX7sBAdYa`</summary>

```json
{
  "pattern": "hand-crafted|handcrafted",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c209cf3c-6b5e-4bf7-a861-2d0f37506019",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xNz3yBnezigfpUAkGs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "14989223-937e-493a-a3ef-4eb29653a1b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01P7cs2Ub2GqAVLJavMK9kbK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 16948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1059,
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

_source line 7 · 2026-05-15T20:05:37.164Z_

<details><summary>↩ Tool result · `toolu_013vFRAuEU9LWjPMX7sBAdYa`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "14989223-937e-493a-a3ef-4eb29653a1b0",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "008d6e27-bc09-4c45-a115-e7908a3fb3e1",
  "sourceToolAssistantUUID": "14989223-937e-493a-a3ef-4eb29653a1b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T20:05:37.582Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01BDaT5mRQxHcZGjUuvffkni`</summary>

```json
{
  "pattern": "statistical fingerprint",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "008d6e27-bc09-4c45-a115-e7908a3fb3e1",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xNz3yBnezigfpUAkGs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9bfbae38-d752-4365-a66b-d288f6b8d6e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01P7cs2Ub2GqAVLJavMK9kbK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 16948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1059,
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

_source line 9 · 2026-05-15T20:05:37.601Z_

<details><summary>↩ Tool result · `toolu_01BDaT5mRQxHcZGjUuvffkni`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-3-
docs/paper/atlas.tex:4:We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
docs/paper/atlas.tex-5-The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-164-Unlike nucleus and top-$k$, which truncate the vocabulary, temperature uniformly scales logits, redistributing probability mass across all tokens.
docs/paper/atlas.tex:165:This accelerates convergence to an attractor distribution during recursive finetuning~\cite{shumailov2024_nature}, amplifying the statistical fingerprint at each depth step.
docs/paper/atlas.tex-166-The acceleration manifests as a systematic depth shift: temperature depth-$N$ features approximate nucleus/top-$k$ depth-$(N{+}1)$ features.
--
docs/paper/method.tex-98-EDD captures a natural question: \emph{how deep into the recursive chain can we reliably distinguish successive generations?}
docs/paper/method.tex:99:A high EDD indicates that the statistical fingerprints retain discriminative power across many recursion steps; a low EDD signals rapid convergence to an indistinguishable regime.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-100-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-13-
docs/paper/introduction.tex:14:Our key insight is that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are consistent across the three model families and three decoding strategies studied.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-15-Specifically, perplexity tail statistics---the 90th-percentile perplexity (\textsc{p90\_ppl}) and surprisal variance (\textsc{var\_surprisal})---emerge as dominant depth indicators, ranking in the top two features by importance in 9/9 and 8/9 model--strategy configurations, respectively.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bfbae38-d752-4365-a66b-d288f6b8d6e2",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "6b2b4890-ee45-4d9a-a6a4-859508bb36fc",
  "sourceToolAssistantUUID": "9bfbae38-d752-4365-a66b-d288f6b8d6e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T20:05:38.231Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01W1j7H2DdaK2EDK6XADQmtg`</summary>

```json
{
  "pattern": "sampling strategy|generation strategy",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b2b4890-ee45-4d9a-a6a4-859508bb36fc",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xNz3yBnezigfpUAkGs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "055a3f87-8d0d-40a9-adb7-5375d5b20116",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01P7cs2Ub2GqAVLJavMK9kbK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 16948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1059,
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

_source line 11 · 2026-05-15T20:05:38.247Z_

<details><summary>↩ Tool result · `toolu_01W1j7H2DdaK2EDK6XADQmtg`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "055a3f87-8d0d-40a9-adb7-5375d5b20116",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "5ca9d3aa-da21-4f4a-9a73-10befb40df40",
  "sourceToolAssistantUUID": "055a3f87-8d0d-40a9-adb7-5375d5b20116",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T20:05:38.862Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Ne1ggpYveeL2Y4Q7yjvo3f`</summary>

```json
{
  "pattern": "feature-based method|statistical method",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ca9d3aa-da21-4f4a-9a73-10befb40df40",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xNz3yBnezigfpUAkGs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "60dfc7da-af73-43bf-a6c5-d6b2d843cf11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01P7cs2Ub2GqAVLJavMK9kbK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 16948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1059,
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

_source line 13 · 2026-05-15T20:05:38.888Z_

<details><summary>↩ Tool result · `toolu_01Ne1ggpYveeL2Y4Q7yjvo3f`</summary>

```text
docs/paper/generalization.tex-9-Table~\ref{tab:baselines} compares classification methods on the Pythia-1.4B nucleus setting.
docs/paper/generalization.tex:10:Five feature-based methods spanning bagging (RF), gradient boosting (XGBoost, LightGBM), ordinal regression (CORAL \cite{coral2020}), and a detection-oriented ensemble (DivEye \cite{diveye2026}) all operate on the same 19 features and converge within $\leq$0.9pp (78.1--79.0\%; pairwise bootstrap $p>0.05$, Bonferroni-corrected), establishing a feature-determined accuracy ceiling.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-11-All five significantly outperform CE-MLP ($p<0.001$, $+$3.2pp).
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-16-\small
docs/paper/generalization.tex:17:\caption{Comparison of classification methods on Pythia-1.4B nucleus. Five feature-based methods (RF, XGBoost, LightGBM, CORAL, DivEye) all operate on the same 19 features and converge within $\leq$0.9pp (78.1--79.0\%). Chance = 25\%. 5-fold CV std: 0.2--0.9pp.}
docs/paper/generalization.tex-18-\label{tab:baselines}
--
docs/paper/generalization.tex-106-SHAP TreeExplainer shows perplexity and surprisal features account for 88.8\% of RF's contribution; three importance measures achieve strong concordance (Kendall's $W{=}0.90$, $p{<}0.005$; Appendix~\ref{app:permutation}), while linear probing from DeBERTa hidden states yields negative $R^2$ for \textsc{var\_surprisal} and \textsc{p90\_ppl} (Appendix~\ref{app:feature_overlap}).
docs/paper/generalization.tex:107:DCOL \cite{cloc2025} reached 64.5\% (Appendix~\ref{app:dcol_iterations}); all end-to-end approaches (58--65\%) underperform feature-based methods, suggesting depth estimation benefits from explicit tail statistics absent from PLM representations.
--
docs/paper/section_appendix.tex-24-Table~\ref{tab:dcol_iterations} summarizes all six DCOL iterations.
docs/paper/section_appendix.tex:25:DeBERTa-v3-large exhibited systematic numerical instability across five configurations; RoBERTa-large resolved stability but could not close the accuracy gap with feature-based methods.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-26-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60dfc7da-af73-43bf-a6c5-d6b2d843cf11",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "b754dd70-4767-4050-a2ed-87c8fcd6c01a",
  "sourceToolAssistantUUID": "60dfc7da-af73-43bf-a6c5-d6b2d843cf11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T20:05:39.519Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01XTN2fAZ93TQLxo41MyPuLe`</summary>

```json
{
  "pattern": "\\\\text\\{EDD\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b754dd70-4767-4050-a2ed-87c8fcd6c01a",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xNz3yBnezigfpUAkGs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f626f089-29a1-4646-b800-e5fa72a3f31d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01P7cs2Ub2GqAVLJavMK9kbK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 16948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1059,
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

_source line 15 · 2026-05-15T20:05:39.532Z_

<details><summary>↩ Tool result · `toolu_01XTN2fAZ93TQLxo41MyPuLe`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f626f089-29a1-4646-b800-e5fa72a3f31d",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "2e9e5393-28f6-4532-9ca0-824fc803f571",
  "sourceToolAssistantUUID": "f626f089-29a1-4646-b800-e5fa72a3f31d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T20:05:39.942Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01DrztosN59hPuXysc3oy7fE`</summary>

```json
{
  "pattern": "model family",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e9e5393-28f6-4532-9ca0-824fc803f571",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xNz3yBnezigfpUAkGs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8b03f050-235d-48cf-9c00-02d1b26c75ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01P7cs2Ub2GqAVLJavMK9kbK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 16948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1059,
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

_source line 17 · 2026-05-15T20:05:39.957Z_

<details><summary>↩ Tool result · `toolu_01DrztosN59hPuXysc3oy7fE`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-15-Top-$k$ sampling yields the lowest accuracy in every model.
docs/paper/atlas.tex:16:The mean within-model strategy gap is 8.4~pp, comparable to the 7.1~pp mean within-strategy model gap---decoding strategy and model family contribute roughly equally to performance variance.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-17-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-16-
docs/paper/method.tex:17:We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-18-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b03f050-235d-48cf-9c00-02d1b26c75ad",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "fd0bc8fc-e24d-4afc-a713-7ea0fdbe176f",
  "sourceToolAssistantUUID": "8b03f050-235d-48cf-9c00-02d1b26c75ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T20:05:40.320Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01AaecuvJQfhkYcZVinUGC83`</summary>

```json
{
  "pattern": "statistical features",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd0bc8fc-e24d-4afc-a713-7ea0fdbe176f",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xNz3yBnezigfpUAkGs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "85bef746-90ba-4f6f-892c-20b7fc3ee4fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01P7cs2Ub2GqAVLJavMK9kbK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 16948,
      "output_tokens": 1031,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1059
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1031,
          "cache_read_input_tokens": 16948,
          "cache_creation_input_tokens": 1059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1059,
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

_source line 19 · 2026-05-15T20:05:40.347Z_

<details><summary>↩ Tool result · `toolu_01AaecuvJQfhkYcZVinUGC83`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex-18-\citet{pu2026_generator_barrier} formalize a generator barrier bounding detection performance when the generator is unknown.
docs/paper/related_work.tex:19:Ghostbuster \cite{verma2024_ghostbuster} trains classifiers on statistical features (token probabilities, rank sequences) for binary detection, sharing our feature-engineering philosophy but not addressing depth.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex-20-The M4-SemEval shared task \cite{wang2024_m4_semeval} benchmarks multilingual machine-generated text detection across diverse generators, and DNA-GPT \cite{yang2024_dnagpt} uses divergent $n$-gram analysis to detect AI text without model access.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex-3-
docs/paper/discussion.tex:4:We formalized recursive generation depth estimation and showed that 19 statistical features achieve 70--85\% four-class accuracy ($\mathrm{EDD}_{0.75}{=}4$; cross-model 66.4\%, cross-strategy 59.1\%).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex-5-Predicted depth can serve as a quality proxy for graded curation; cross-strategy degradation motivates a two-stage strategy-conditioned pipeline as future work.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex-3-We formalize \emph{recursive generation depth estimation} as ordinal classification and construct a benchmark of 180K passages spanning 3 model families, 3 decoding strategies, and 4 generation depths.
docs/paper/abstract.tex:4:From each passage we extract 19 statistical features---perplexity percentiles, surprisal moments, and lexical diversity measures---computed against a fixed reference model (GPT-2 base, 124M).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex-5-A Random Forest classifier achieves 70--85\% four-class accuracy (chance = 25\%; 58.8--82.6\% when excluding the near-perfectly separable d0 class; a zero-shot LLM baseline reaches only 36.2\%), with 90th-percentile perplexity and surprisal variance emerging as consistent depth markers across the studied $3 \times 3$ grid (top-2 importance in 9/9 and 8/9 cells, respectively).
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-38-\paragraph{Reference model.}
docs/paper/method.tex:39:All statistical features (\S\ref{sec:method:features}) are computed using a fixed reference model---GPT-2 base (124M)---that is independent of the three generation models.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-40-The reference model computes per-token perplexity for each passage, providing a consistent measurement frame across model families.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-51-\small
docs/paper/method.tex:52:\caption{The 19 statistical features comprising $\mathbf{f}(x)$, grouped by category. All perplexity and surprisal features are computed from the reference model (GPT-2 base, 124M).}
docs/paper/method.tex-53-\label{tab:features}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-48-
docs/paper/section_appendix.tex:49:We probe whether end-to-end PLM representations capture the same depth signals as our statistical features.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-50-DeBERTa attention importance and RF permutation importance exhibit a significant negative correlation (Spearman $\rho{=}{-}0.484$, $p{=}0.036$; top-5 Jaccard overlap$\,{=}\,0$).
docs/paper/section_appendix.tex-51-PLM representations excel at surface lexical features (TTR: $R^2{=}0.85$, repeated bigrams) but fail to capture perplexity distribution statistics---\textsc{var\_surprisal} and \textsc{p90\_ppl} yield negative $R^2$ under linear probing.
docs/paper/section_appendix.tex:52:This confirms that the 19pp accuracy gap between feature-based and end-to-end methods (\S\ref{sec:gen:e2e}) stems from complementary---not redundant---representations: PLMs capture lexical patterns while the statistical features capture distributional tail properties that constitute the dominant depth markers.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-53-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85bef746-90ba-4f6f-892c-20b7fc3ee4fc",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "9cf71178-7646-4440-a805-c2d7efccd300",
  "sourceToolAssistantUUID": "85bef746-90ba-4f6f-892c-20b7fc3ee4fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-15T20:05:42.115Z_

Now let me search for more specific patterns related to decoding strategy vs generation/sampling strategy, and check for other terminology variations:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cf71178-7646-4440-a805-c2d7efccd300",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xPNgkMLAU3Da1zM6G8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "62e31711-4b52-45d6-bfaa-3e672e4ef551",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011n2hUKP3YRtyfBPSKLUvc2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4382,
      "cache_read_input_tokens": 18007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4382,
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

_source line 21 · 2026-05-15T20:05:42.540Z_

<details open><summary>🔧 Tool call — Grep · `toolu_011K1VoQR3C8op46gTeHCD9j`</summary>

```json
{
  "pattern": "decoding strategy",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62e31711-4b52-45d6-bfaa-3e672e4ef551",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xPNgkMLAU3Da1zM6G8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a4befc3c-fb08-43f9-967e-50765a4791f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011n2hUKP3YRtyfBPSKLUvc2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4382,
      "cache_read_input_tokens": 18007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4382,
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

_source line 22 · 2026-05-15T20:05:42.555Z_

<details><summary>↩ Tool result · `toolu_011K1VoQR3C8op46gTeHCD9j`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex-30-\paragraph{Decoding Strategy Effects.}
docs/paper/related_work.tex:31:The choice of decoding strategy shapes the statistical properties of generated text in ways that interact with generation depth signals.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex-32-\citet{holtzman2020_nucleus} show that unrestricted sampling produces degenerate repetitions and propose nucleus sampling to maintain output diversity.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-15-Top-$k$ sampling yields the lowest accuracy in every model.
docs/paper/atlas.tex:16:The mean within-model strategy gap is 8.4~pp, comparable to the 7.1~pp mean within-strategy model gap---decoding strategy and model family contribute roughly equally to performance variance.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-17-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-177-\paragraph{Strategy vs.\ model effect.}
docs/paper/atlas.tex:178:The strategy effect (8.4~pp range) exceeds the model effect (7.1~pp range) across the atlas, indicating that deployment-time knowledge of the decoding strategy is at least as important as knowledge of the generator model for accurate depth estimation.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-16-
docs/paper/method.tex:17:We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-18-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-32-\paragraph{Generation pipeline.}
docs/paper/method.tex:33:Starting from a Wikipedia subset as seed text ($\mathcal{D}_0$), each generation cycle proceeds in three steps: (1)~LoRA finetuning \cite{hu2022lora} with rank $r{=}16$, $\alpha{=}32$, learning rate $2{\times}10^{-4}$, batch size 8, for 3 epochs; (2)~generation of 5{,}000 passages (max 512 tokens) under the specified decoding strategy; (3)~the generated corpus becomes $\mathcal{D}_k$ and serves as training data for the next cycle.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-34-Each generation cycle samples unconditionally from the BOS token; there is no per-passage lineage across depths, ensuring that cross-validation splits do not introduce information leakage.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex-5-A Random Forest classifier achieves 70--85\% four-class accuracy (chance = 25\%; 58.8--82.6\% when excluding the near-perfectly separable d0 class; a zero-shot LLM baseline reaches only 36.2\%), with 90th-percentile perplexity and surprisal variance emerging as consistent depth markers across the studied $3 \times 3$ grid (top-2 importance in 9/9 and 8/9 cells, respectively).
docs/paper/abstract.tex:6:Our \emph{Depth Degradation Atlas} reveals that decoding strategy reshapes degradation trajectories rather than merely attenuating them, and we define the \emph{Effective Discriminable Depth} (EDD) metric, finding $\mathrm{EDD}_{0.75}{=}4$ for extended recursion chains.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex-7-Cross-model transfer reaches 66.4\% and cross-strategy transfer 59.1\%; temperature sampling induces a d1/d2 AUC inversion that we decompose into a correctable scale component and a residual structural component.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4befc3c-fb08-43f9-967e-50765a4791f2",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "d99d3aa8-747d-4aec-afb0-8fcfdc661261",
  "sourceToolAssistantUUID": "a4befc3c-fb08-43f9-967e-50765a4791f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T20:05:43.375Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01Ti5DUqjzpgcBAV39XPxAYu`</summary>

```json
{
  "pattern": "Pythia|OLMo|GPT-2 XL",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d99d3aa8-747d-4aec-afb0-8fcfdc661261",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xPNgkMLAU3Da1zM6G8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d71f6d60-6197-4a08-8af7-7eab4a15d7d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011n2hUKP3YRtyfBPSKLUvc2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4382,
      "cache_read_input_tokens": 18007,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4382,
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

_source line 24 · 2026-05-15T20:05:43.389Z_

<details><summary>↩ Tool result · `toolu_01Ti5DUqjzpgcBAV39XPxAYu`</summary>

```text
docs/paper/atlas.tex-11-Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
docs/paper/atlas.tex:12:Accuracy ranges from 69.6\% (Pythia, top-$k$) to 85.4\% (GPT-2~XL, temperature), all exceeding the 25\% chance baseline by a wide margin.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-13-Two axis effects emerge.
docs/paper/atlas.tex:14:GPT-2~XL achieves the highest accuracy under every strategy (76.6--85.4\%), followed by OLMo (74.2--82.0\%) and Pythia (69.6--78.2\%).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-15-Top-$k$ sampling yields the lowest accuracy in every model.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-26-\midrule
docs/paper/atlas.tex:27:Pythia-1.4B  & 78.2\,(71.2) & 76.3\,(70.6) & 69.6\,(58.8) \\
docs/paper/atlas.tex:28:OLMo-1B     & 78.8\,(75.0) & 82.0\,(76.3) & 74.2\,(66.1) \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-29-GPT-2~XL    & 83.3\,(79.0) & 85.4\,(82.6) & 76.6\,(69.5) \\
--
docs/paper/atlas.tex-105-Figure~\ref{fig:auc_decay} plots the binary pairwise AUC decay curves.
docs/paper/atlas.tex:106:For Pythia-1.4B (nucleus), AUC decays monotonically: d0-vs-d1 $= 0.999$, d1-vs-d2 $= 0.925$, d2-vs-d3 $= 0.823$, d3-vs-d4 $= 0.784$, d4-vs-d5 $= 0.683$.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-107-The steepest drop occurs between the d1-vs-d2 and d2-vs-d3 pairs; the curve then flattens as the system approaches an indistinguishable regime gradually rather than crossing a sharp boundary.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-110-All three models exhibit a consistent profile at the deep boundaries.
docs/paper/atlas.tex:111:The d3-vs-d4 AUC clusters near the $T{=}0.75$ threshold: Pythia $0.784$ (bootstrap 95\% CI $[0.765, 0.802]$, $p = 0.001$), OLMo $0.765$ ($[0.744, 0.785]$, $p = 0.091$), GPT-2~XL $0.750$ ($[0.728, 0.771]$, $p = 0.505$), where $p$ denotes the one-tailed bootstrap probability under $H_0\!: \mathrm{AUC} \leq 0.75$ (1{,}000 iterations).
docs/paper/atlas.tex:112:Only Pythia achieves significance at conventional levels; OLMo is marginal and GPT-2~XL falls on the threshold despite its higher in-distribution accuracy.
docs/paper/atlas.tex:113:The d4-vs-d5 AUC falls uniformly below 0.70 across all three models (Pythia $0.683$, OLMo $0.684$, GPT-2~XL $0.681$), confirming a model-independent signal saturation point at depth~5.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-114-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-120-At $T{=}0.65$, all 9 cells achieve $\mathrm{EDD} = 3$; at $T{=}0.75$, 7 of 9 cells maintain $\mathrm{EDD} \geq 3$; at $T{=}0.80$, the count drops to 5 of 9.
docs/paper/atlas.tex:121:The cells losing $\mathrm{EDD}{=}3$ first are consistently the top-$k$ configurations (Pythia top-$k$ at $T{=}0.70$, then OLMo top-$k$ at $T{=}0.75$), where the d2-vs-d3 pair is the consistent bottleneck across all 9 cells.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-122-
--
docs/paper/atlas.tex-146-EDD's binary-pair design is motivated by \emph{decision boundary dilution}: when a multi-class classifier must simultaneously separate $K$ depths, its decision boundaries are shared across all $\binom{K}{2}$ class pairs, diluting the capacity allocated to any single adjacent pair.
docs/paper/atlas.tex:147:Concretely, in the Pythia nucleus setting, the d2\,vs.\,d3 pairwise AUC degrades from 0.804 in a 4-class pipeline to 0.689 in a 6-class pipeline---a 14.3\% relative decline---despite identical underlying data.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-148-Mean classification accuracy likewise drops from 99.5\% (binary) to 78.3\% (4-class) to 62.9\% (6-class).
--
docs/paper/atlas.tex-162-\paragraph{Temperature ($\tau{=}0.9$): signal enhancement with boundary reversal.}
docs/paper/atlas.tex:163:Temperature sampling yields the highest accuracy in 2 of 3 models (GPT-2~XL $85.4\%$, OLMo $82.0\%$) and the second-highest in Pythia ($76.3\%$).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-164-Unlike nucleus and top-$k$, which truncate the vocabulary, temperature uniformly scales logits, redistributing probability mass across all tokens.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-5-Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
docs/paper/conclusion.tex:6:Per-strategy z-score normalization partially corrects the inversion (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but leaves a residual gap relative to within-strategy performance (${\sim}0.83$), indicating that a two-stage pipeline (strategy identification + strategy-conditioned classification) is needed for reliable cross-strategy deployment.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-7-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-9-Depth~0 (human-written text) is near-perfectly separable (recall $>$98\% across all settings), inflating headline accuracy.
docs/paper/conclusion.tex:10:Cross-model transfer accuracy of 66.4\% is substantially driven by d0; d2 recall drops to 26.8\% in the worst case (Pythia holdout).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-11-
--
docs/paper/conclusion.tex-14-While depth signal is the dominant classification factor (5-fold CV 59--82\%, 3.4$\times$ chance), a residual domain signal from seed-article stylistic differences exists (${\sim}$2$\times$ chance conditional on seed group; LOGO accuracy drops 8pp on average; Appendix~\ref{app:domain_bias}).
docs/paper/conclusion.tex:15:In the most affected cell (Pythia top-$k$), individual LOGO folds drop to 22.9\%, approaching chance.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-16-Transfer to mixed-domain corpora, instruction-tuned models, and larger scales (7B+) remains open.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-24-However, \citet{bakshi2026_collapse_improvement} show that early recursion can temporarily \emph{improve} model quality, which could produce non-monotonic AUC profiles (e.g., a dip at d1/d2 followed by recovery at d2/d3).
docs/paper/conclusion.tex:25:Our cross-strategy transfer results provide an empirical example: training on nucleus + top-$k$ and testing on temperature yields d1-vs-d2 AUC as low as 0.129 (GPT-2~XL) and 0.253 (OLMo), violating the monotonicity assumption.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-26-In such cases EDD would conservatively report a lower value than the deepest discriminable pair, potentially underestimating the true discriminable range; extending EDD to handle non-contiguous discriminable regions is future work.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-29-\paragraph{Reference model dependency.}
docs/paper/conclusion.tex:30:Surprisal-based features are computed relative to GPT-2 base (124M), introducing partial overlap when GPT-2~XL is held out, though GPT-2~XL holdout accuracy (67.6\%) does not exceed the unrelated OLMo (69.2\%).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-31-The choice of reference model affects feature values; a different reference model may shift absolute feature magnitudes and potentially alter discriminability at depth boundaries.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-38-
docs/paper/conclusion.tex:39:This work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2~XL) and Wikipedia text as seed data.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-40-No human subjects were involved, no private or sensitive data were collected, and no new models were released.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-19-\paragraph{Model families.}
docs/paper/method.tex:20:We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-21-Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-29-The primary benchmark covers depths d0--d3 across all $3 \times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K samples total).
docs/paper/method.tex:30:For depth extension experiments (\S\ref{sec:atlas}), we extend one pipeline (Pythia-1.4B, nucleus) to d0--d5.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-31-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-34-Each generation cycle samples unconditionally from the BOS token; there is no per-passage lineage across depths, ensuring that cross-validation splits do not introduce information leakage.
docs/paper/method.tex:35:LoRA targets are architecture-specific: \texttt{query\_key\_value} for Pythia (GPT-NeoX), \texttt{q\_proj}/\texttt{k\_proj}/\texttt{v\_proj} for OLMo, and \texttt{c\_attn}/\texttt{c\_proj} for GPT-2~XL.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-36-We adopt commonly used LoRA hyperparameters ($r{=}16$, $\alpha{=}32$, dropout$\,{=}\,0.05$) following \citet{hu2022lora}, applied uniformly across all models.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-8-
docs/paper/generalization.tex:9:Table~\ref{tab:baselines} compares classification methods on the Pythia-1.4B nucleus setting.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-10-Five feature-based methods spanning bagging (RF), gradient boosting (XGBoost, LightGBM), ordinal regression (CORAL \cite{coral2020}), and a detection-oriented ensemble (DivEye \cite{diveye2026}) all operate on the same 19 features and converge within $\leq$0.9pp (78.1--79.0\%; pairwise bootstrap $p>0.05$, Bonferroni-corrected), establishing a feature-determined accuracy ceiling.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-16-\small
docs/paper/generalization.tex:17:\caption{Comparison of classification methods on Pythia-1.4B nucleus. Five feature-based methods (RF, XGBoost, LightGBM, CORAL, DivEye) all operate on the same 19 features and converge within $\leq$0.9pp (78.1--79.0\%). Chance = 25\%. 5-fold CV std: 0.2--0.9pp.}
docs/paper/generalization.tex-18-\label{tab:baselines}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-33-\end{tabular}
docs/paper/generalization.tex:34:\footnotetext{Evaluated on 500 samples (125 per class) from the Pythia-1.4B nucleus cell only, due to API cost; 95\% CI: $[32.0\%, 40.4\%]$. All other methods use the full 20{,}000-sample set.}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-35-\end{table}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-42-\includegraphics[width=\columnwidth]{figures/fig_confusion_matrix.pdf}
docs/paper/generalization.tex:43:\caption{Confusion matrices for the best in-distribution setting (GPT-2 XL, temp $\tau{=}0.9$, 85.4\%) and the best cross-model leave-one-out transfer (OLMo holdout, 69.2\%). d0 recall exceeds 99\% in both; errors spread across the d1--d3 range under transfer.}
docs/paper/generalization.tex-44-\label{fig:confusion_matrix}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-54-\small
docs/paper/generalization.tex:55:\caption{Cross-model transfer (leave-one-out, nucleus only). Chance = 25\% / 33\% (d1--d3). d1--d3 bal.\ acc: Pythia 49.9\%, OLMo 59.2\%, GPT-2~XL 57.2\% (mean 55.4\%).}
docs/paper/generalization.tex-56-\label{tab:cross_model}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-61-\midrule
docs/paper/generalization.tex:62:Pythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\
docs/paper/generalization.tex:63:OLMo & \textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\
docs/paper/generalization.tex:64:GPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-65-\midrule
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-70-
docs/paper/generalization.tex:71:Mean transfer accuracy is 66.4\% (2.7$\times$ chance); d0 recall ($>$98\%) inflates the headline while d2 drops to 26.8\% (Pythia holdout).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-72-Excluding d0, d1--d3 balanced accuracy averages 55.4\% (chance = 33\%).
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-85-\toprule
docs/paper/generalization.tex:86:Holdout & Pythia & OLMo & GPT-2 XL \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex-87- & Acc (\%) & Acc (\%) & Acc (\%) \\
--
docs/paper/section_appendix.tex-15-To verify that the Gini-based importance rankings in \S\ref{sec:atlas:features} are not an artifact of the impurity measure, we compute permutation importance (5-fold CV, 10 repeats) for all 9 atlas cells.
docs/paper/section_appendix.tex:16:The top-2 features are stable across measures: \textsc{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \textsc{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \textsc{p75\_ppl} displaces \textsc{var\_surprisal} to rank 3).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-17-Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-29-\small
docs/paper/section_appendix.tex:30:\caption{DCOL iteration summary. All experiments use Pythia-1.4B nucleus data. RF baseline: 78.2\%.}
docs/paper/section_appendix.tex-31-\label{tab:dcol_iterations}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-60-LOGO accuracy drops 8pp on average relative to random-split CV, with substantial variance across cells.
docs/paper/section_appendix.tex:61:In the most affected configuration (Pythia-1.4B, top-$k$), individual LOGO folds drop as low as 22.9\%---approaching the 33.3\% chance level for d1--d3 classification---suggesting that in specific model--strategy combinations, the seed-article effect can nearly eliminate the depth signal for a held-out article group.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex-62-These results motivate future work on domain-robust features and cross-corpus evaluation.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-18-Given a text passage, we compute a 19-dimensional feature vector from reference-model perplexity statistics---capturing distributional location, spread, tail behavior, and lexical diversity---and classify it with a Random Forest into one of $K{+}1$ depth classes ($d{=}0$ for human text through $d{=}K$ for $K$-th generation text).
docs/paper/introduction.tex:19:To systematically characterize how recursive generation reshapes these features, we construct the \emph{Depth Degradation Atlas}: a $3 \times 3$ grid of model families (Pythia-1.4B, OLMo-1B, GPT-2~XL) and decoding strategies (nucleus $p{=}0.95$, temperature $\tau{=}0.9$, top-$k$ $k{=}50$), each spanning 4 generation depths, totaling 180K samples.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-20-The atlas reveals strategy-dependent degradation trajectories---temperature sampling accelerates convergence toward a low-entropy attractor, while top-$k$ attenuates the depth signal---and we introduce the \emph{Effective Discriminable Depth} (EDD) metric to quantify how far into the recursion chain adjacent depths remain distinguishable.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-26-
docs/paper/introduction.tex:27:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-28-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d71f6d60-6197-4a08-8af7-7eab4a15d7d1",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "0015a92b-f41f-4c2a-8172-8868c5617ea7",
  "sourceToolAssistantUUID": "d71f6d60-6197-4a08-8af7-7eab4a15d7d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T20:05:43.784Z_

<details open><summary>🔧 Tool call — Grep · `toolu_018LT4KiK7dtEw1piN8xMC61`</summary>

```json
{
  "pattern": "\\\\mathrm\\{EDD\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0015a92b-f41f-4c2a-8172-8868c5617ea7",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xPNgkMLAU3Da1zM6G8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bf7e9620-fcaf-4d42-a784-ef4d8e7fa1c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011n2hUKP3YRtyfBPSKLUvc2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4382,
      "cache_read_input_tokens": 18007,
      "output_tokens": 480,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4382
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 480,
          "cache_read_input_tokens": 18007,
          "cache_creation_input_tokens": 4382,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4382,
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

_source line 26 · 2026-05-15T20:05:43.802Z_

<details><summary>↩ Tool result · `toolu_018LT4KiK7dtEw1piN8xMC61`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-115-This pattern---directional consistency across models with graded statistical strength---supports interpreting the d3--d4 region as a \emph{transition zone} rather than a binary boundary.
docs/paper/atlas.tex:116:The continuous AUC decay curve provides a more informative characterization of depth discriminability than any single $\mathrm{EDD}_T$ value.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-117-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-118-\paragraph{EDD threshold sensitivity.}
docs/paper/atlas.tex:119:Table~\ref{tab:edd_sensitivity} reports $\mathrm{EDD}_T$ across the primary 9-cell benchmark (depths 0--3) at four threshold values.
docs/paper/atlas.tex:120:At $T{=}0.65$, all 9 cells achieve $\mathrm{EDD} = 3$; at $T{=}0.75$, 7 of 9 cells maintain $\mathrm{EDD} \geq 3$; at $T{=}0.80$, the count drops to 5 of 9.
docs/paper/atlas.tex:121:The cells losing $\mathrm{EDD}{=}3$ first are consistently the top-$k$ configurations (Pythia top-$k$ at $T{=}0.70$, then OLMo top-$k$ at $T{=}0.75$), where the d2-vs-d3 pair is the consistent bottleneck across all 9 cells.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-122-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-125-\small
docs/paper/atlas.tex:126:\caption{Number of atlas cells achieving $\mathrm{EDD} \geq 3$ at each threshold $T$, across 9 model--strategy cells (depths 0--3). The d2-vs-d3 boundary is the bottleneck; top-$k$ cells drop first.}
docs/paper/atlas.tex-127-\label{tab:edd_sensitivity}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-131-\midrule
docs/paper/atlas.tex:132:Cells with $\mathrm{EDD} \geq 3$ & 9/9 & 8/9 & 7/9 & 5/9 \\
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-133-\bottomrule
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex-3-
docs/paper/discussion.tex:4:We formalized recursive generation depth estimation and showed that 19 statistical features achieve 70--85\% four-class accuracy ($\mathrm{EDD}_{0.75}{=}4$; cross-model 66.4\%, cross-strategy 59.1\%).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex-5-Predicted depth can serve as a quality proxy for graded curation; cross-strategy degradation motivates a two-stage strategy-conditioned pipeline as future work.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-90-\begin{equation}
docs/paper/method.tex:91:\mathrm{EDD}_T = \max \bigl\{ d^*{+}1 : \forall\, d' \leq d^*,\; \mathrm{AUC}(d', d'{+}1) \geq T \bigr\}
docs/paper/method.tex-92-\label{eq:edd}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex-5-A Random Forest classifier achieves 70--85\% four-class accuracy (chance = 25\%; 58.8--82.6\% when excluding the near-perfectly separable d0 class; a zero-shot LLM baseline reaches only 36.2\%), with 90th-percentile perplexity and surprisal variance emerging as consistent depth markers across the studied $3 \times 3$ grid (top-2 importance in 9/9 and 8/9 cells, respectively).
docs/paper/abstract.tex:6:Our \emph{Depth Degradation Atlas} reveals that decoding strategy reshapes degradation trajectories rather than merely attenuating them, and we define the \emph{Effective Discriminable Depth} (EDD) metric, finding $\mathrm{EDD}_{0.75}{=}4$ for extended recursion chains.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex-7-Cross-model transfer reaches 66.4\% and cross-strategy transfer 59.1\%; temperature sampling induces a d1/d2 AUC inversion that we decompose into a correctable scale component and a residual structural component.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-26-
docs/paper/introduction.tex:27:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-28-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf7e9620-fcaf-4d42-a784-ef4d8e7fa1c8",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "f049bfe6-ddd8-4ae6-87ea-383fba534fa1",
  "sourceToolAssistantUUID": "bf7e9620-fcaf-4d42-a784-ef4d8e7fa1c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-15T20:05:45.211Z_

Perfect! Now let me search for more patterns related to "architecture" in the context of model families, and check for any remaining inconsistencies:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f049bfe6-ddd8-4ae6-87ea-383fba534fa1",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xPdN3nRsF7UxXBAp2Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "493b9a58-0f16-4149-b7a5-cce7fbabdd8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HcL5u9EzKuJa1Xuf4o4CmK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9767,
      "cache_read_input_tokens": 22389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9767,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 28 · 2026-05-15T20:05:46.085Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01UxGys39sP17i1Pw28SL97c`</summary>

```json
{
  "pattern": "Pythia.*architecture|OLMo.*architecture|GPT-2.*architecture",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "493b9a58-0f16-4149-b7a5-cce7fbabdd8c",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xPdN3nRsF7UxXBAp2Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a5b8daa1-ac1e-475b-aad8-c6587d9f1cf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HcL5u9EzKuJa1Xuf4o4CmK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9767,
      "cache_read_input_tokens": 22389,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9767,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 29 · 2026-05-15T20:05:46.115Z_

<details><summary>↩ Tool result · `toolu_01UxGys39sP17i1Pw28SL97c`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5b8daa1-ac1e-475b-aad8-c6587d9f1cf3",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "82c0adaf-7a66-42e1-91bc-d5a91aaf24d1",
  "sourceToolAssistantUUID": "a5b8daa1-ac1e-475b-aad8-c6587d9f1cf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T20:05:46.491Z_

<details open><summary>🔧 Tool call — Grep · `toolu_016agfRXZ4R3bx1cjFG16nKW`</summary>

```json
{
  "pattern": "fingerprints",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82c0adaf-7a66-42e1-91bc-d5a91aaf24d1",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xPdN3nRsF7UxXBAp2Q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0d9f1329-f872-4ef2-b11b-8c1f5d034f63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HcL5u9EzKuJa1Xuf4o4CmK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9767,
      "cache_read_input_tokens": 22389,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9767
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 342,
          "cache_read_input_tokens": 22389,
          "cache_creation_input_tokens": 9767,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9767,
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

_source line 31 · 2026-05-15T20:05:46.509Z_

<details><summary>↩ Tool result · `toolu_016agfRXZ4R3bx1cjFG16nKW`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-3-
docs/paper/atlas.tex:4:We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
docs/paper/atlas.tex-5-The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-34-Detection features degrade under domain shift \cite{pudasaini2026_detection_fails}; our depth features are likely susceptible.
docs/paper/conclusion.tex:35:\citet{falahati2026_curated} show that curated synthetic data need not trigger collapse, attenuating the fingerprints we exploit.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex-36-
--
docs/paper/method.tex-98-EDD captures a natural question: \emph{how deep into the recursive chain can we reliably distinguish successive generations?}
docs/paper/method.tex:99:A high EDD indicates that the statistical fingerprints retain discriminative power across many recursion steps; a low EDD signals rapid convergence to an indistinguishable regime.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-100-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-13-
docs/paper/introduction.tex:14:Our key insight is that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are consistent across the three model families and three decoding strategies studied.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-15-Specifically, perplexity tail statistics---the 90th-percentile perplexity (\textsc{p90\_ppl}) and surprisal variance (\textsc{var\_surprisal})---emerge as dominant depth indicators, ranking in the top two features by importance in 9/9 and 8/9 model--strategy configurations, respectively.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d9f1329-f872-4ef2-b11b-8c1f5d034f63",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "13218590-d83f-48d5-bd67-f9323d7fbd52",
  "sourceToolAssistantUUID": "0d9f1329-f872-4ef2-b11b-8c1f5d034f63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-15T20:05:47.966Z_

Now let me read the main files to check for any context around model references and identify any terminology issues I may have missed:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13218590-d83f-48d5-bd67-f9323d7fbd52",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xPpx4WC1KDUhxh84KR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b996edca-0871-4036-b4ba-db02eabca921",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CXRE3R8xuKK2QAUFaKAkgd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1074,
      "cache_read_input_tokens": 32156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1074,
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

_source line 33 · 2026-05-15T20:05:48.294Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WbifnZaUr9ejV1KuxroqQZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b996edca-0871-4036-b4ba-db02eabca921",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xPpx4WC1KDUhxh84KR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f413792f-fde6-47e0-ba8d-f3ccbfaffe32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CXRE3R8xuKK2QAUFaKAkgd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1074,
      "cache_read_input_tokens": 32156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1074,
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

_source line 34 · 2026-05-15T20:05:48.300Z_

<details><summary>↩ Tool result · `toolu_01WbifnZaUr9ejV1KuxroqQZ`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Definition}
5	\label{sec:method:problem}
6	
7	Let $f_\theta$ denote a language model and $\mathcal{D}_0$ a corpus of human-written seed text.
8	We define a \emph{recursive generation chain} of depth $K$ as the sequence $\mathcal{D}_0, \mathcal{D}_1, \dots, \mathcal{D}_K$, where each $\mathcal{D}_k$ ($k \geq 1$) is produced by finetuning $f_\theta$ on $\mathcal{D}_{k-1}$ and sampling from the resulting model.
9	Depth $d{=}0$ denotes human-written text; depth $d{=}k$ ($k \geq 1$) denotes text generated by a model trained on depth-$(k{-}1)$ data.
10	
11	Given a text passage $x$, the task is to estimate its recursive generation depth $d \in \{0, 1, \dots, K\}$.
12	This is an ordinal classification problem: depths carry a natural ordering, and $d{=}1$ is structurally closer to $d{=}0$ than $d{=}3$ is, since each generation step compounds distributional drift.
13	
14	\subsection{Multi-Generational Benchmark Construction}
15	\label{sec:method:benchmark}
16	
17	We construct a benchmark spanning three axes: model family, decoding strategy, and generation depth.
18	
19	\paragraph{Model families.}
20	We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
21	Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
22	
23	\paragraph{Decoding strategies.}
24	Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
25	These span the dominant modes of open-ended generation and induce qualitatively different entropy profiles.
26	Our findings on feature importance and discriminability are limited to this grid; transfer to untested models, scales, or strategies is not established.
27	
28	\paragraph{Depth and scale.}
29	The primary benchmark covers depths d0--d3 across all $3 \times 3 = 9$ model--strategy cells, with 5{,}000 samples per depth per cell (180K samples total).
30	For depth extension experiments (\S\ref{sec:atlas}), we extend one pipeline (Pythia-1.4B, nucleus) to d0--d5.
31	
32	\paragraph{Generation pipeline.}
33	Starting from a Wikipedia subset as seed text ($\mathcal{D}_0$), each generation cycle proceeds in three steps: (1)~LoRA finetuning \cite{hu2022lora} with rank $r{=}16$, $\alpha{=}32$, learning rate $2{\times}10^{-4}$, batch size 8, for 3 epochs; (2)~generation of 5{,}000 passages (max 512 tokens) under the specified decoding strategy; (3)~the generated corpus becomes $\mathcal{D}_k$ and serves as training data for the next cycle.
34	Each generation cycle samples unconditionally from the BOS token; there is no per-passage lineage across depths, ensuring that cross-validation splits do not introduce information leakage.
35	LoRA targets are architecture-specific: \texttt{query\_key\_value} for Pythia (GPT-NeoX), \texttt{q\_proj}/\texttt{k\_proj}/\texttt{v\_proj} for OLMo, and \texttt{c\_attn}/\texttt{c\_proj} for GPT-2~XL.
36	We adopt commonly used LoRA hyperparameters ($r{=}16$, $\alpha{=}32$, dropout$\,{=}\,0.05$) following \citet{hu2022lora}, applied uniformly across all models.
37	
38	\paragraph{Reference model.}
39	All statistical features (\S\ref{sec:method:features}) are computed using a fixed reference model---GPT-2 base (124M)---that is independent of the three generation models.
40	The reference model computes per-token perplexity for each passage, providing a consistent measurement frame across model families.
41	In cross-model leave-one-out evaluation (\S\ref{sec:generalization}), the reference model remains fixed even when GPT-2~XL is held out; the partial architectural overlap this introduces is discussed in Limitations.
42	
43	\subsection{Statistical Feature Design}
44	\label{sec:method:features}
45	
46	We extract a 19-dimensional feature vector $\mathbf{f}(x)$ from the reference-model perplexity distribution over each passage $x$.
47	The features fall into four categories (Table~\ref{tab:features}).
48	
49	\begin{table}[t]
50	\centering
51	\small
52	\caption{The 19 statistical features comprising $\mathbf{f}(x)$, grouped by category. All perplexity and surprisal features are computed from the reference model (GPT-2 base, 124M).}
53	\label{tab:features}
54	\begin{tabular}{@{}llr@{}}
55	\toprule
56	Category & Features & $n$ \\
57	\midrule
58	Perplexity & mean, var, skewness, kurtosis, & 9 \\
59	statistics & p10, p25, p50, p75, p90 & \\
60	\addlinespace
61	Surprisal & mean, var, entropy & 3 \\
62	statistics & & \\
63	\addlinespace
64	Lexical & type--token ratio, hapax ratio, & 4 \\
65	diversity & bigram entropy, trigram entropy & \\
66	\addlinespace
67	Repetition & repeated 2/3/4-gram fractions & 3 \\
68	\bottomrule
69	\end{tabular}
70	\end{table}
71	
72	\emph{Perplexity statistics} (9 features) capture the location, spread, and shape of the per-token perplexity distribution via its mean, variance, skewness, kurtosis, and five percentile quantiles (p10--p90).
73	The tail quantiles (p75, p90) prove especially informative: recursive finetuning erodes the high-perplexity tail, making these features monotonically decreasing with depth (\S\ref{sec:atlas}).
74	
75	\emph{Surprisal statistics} (3 features) operate on $-\log p(\text{token})$ and include mean surprisal, surprisal variance, and the entropy of the surprisal distribution.
76	While correlated with perplexity features, surprisal variance captures second-order structure---the variability of token predictability---that is not redundant with perplexity moments.
77	
78	\emph{Lexical diversity} (4 features) measures vocabulary usage through type--token ratio, hapax ratio (fraction of tokens appearing exactly once), and bigram/trigram entropy.
79	
80	\emph{Repetition} (3 features) quantifies the fraction of repeated $n$-grams for $n \in \{2, 3, 4\}$, capturing the increased self-repetition characteristic of recursive generation.
81	
82	\subsection{Effective Discriminable Depth}
83	\label{sec:method:edd}
84	
85	Aggregate classification accuracy over $K{+}1$ classes obscures whether discriminability degrades at specific depths.
86	We introduce the \emph{Effective Discriminable Depth} (EDD), a scalar metric that summarizes how far into a recursive chain adjacent depths remain distinguishable.
87	
88	For each adjacent depth pair $(d, d{+}1)$, we train a dedicated binary Random Forest (500 trees; increased from 200 in the multi-class setting to ensure convergence on the smaller per-pair samples) and compute the one-vs-one AUC.
89	Given a threshold $T$, we define:
90	\begin{equation}
91	\mathrm{EDD}_T = \max \bigl\{ d^*{+}1 : \forall\, d' \leq d^*,\; \mathrm{AUC}(d', d'{+}1) \geq T \bigr\}
92	\label{eq:edd}
93	\end{equation}
94	where $d^* \in \{0, 1, \dots, K{-}1\}$.\footnote{Our AUC profiles are monotonically decreasing, so the $\forall$ and pointwise $\max\{d^*{+}1 : \mathrm{AUC}(d^*,d^*{+}1) \geq T\}$ formulations coincide; the $\forall$ version is preferred as it guarantees a contiguous discriminable range (see Limitations).}
95	The default threshold is $T{=}0.75$; we report sensitivity analyses at $T \in \{0.65, 0.70, 0.75, 0.80\}$ in \S\ref{sec:atlas}.
96	Crucially, each AUC is obtained from an independent binary pairwise classifier (5-fold stratified CV) rather than extracted from a single multi-class model, avoiding decision boundary dilution (\S\ref{sec:atlas}).
97	
98	EDD captures a natural question: \emph{how deep into the recursive chain can we reliably distinguish successive generations?}
99	A high EDD indicates that the statistical fingerprints retain discriminative power across many recursion steps; a low EDD signals rapid convergence to an indistinguishable regime.
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f413792f-fde6-47e0-ba8d-f3ccbfaffe32",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "d2a16d45-febc-4cba-9eb8-fb85cbc143f8",
  "sourceToolAssistantUUID": "f413792f-fde6-47e0-ba8d-f3ccbfaffe32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T20:05:48.454Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NwJvpR5EFHVKkHoitGchbU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2a16d45-febc-4cba-9eb8-fb85cbc143f8",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xPpx4WC1KDUhxh84KR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ab7489e9-2177-420c-92e8-262f41b2e13a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CXRE3R8xuKK2QAUFaKAkgd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1074,
      "cache_read_input_tokens": 32156,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1074
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 204,
          "cache_read_input_tokens": 32156,
          "cache_creation_input_tokens": 1074,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1074,
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

_source line 36 · 2026-05-15T20:05:48.459Z_

<details><summary>↩ Tool result · `toolu_01NwJvpR5EFHVKkHoitGchbU`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	The text on which large language models are trained increasingly contains their own outputs.
5	As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
6	This model$\to$data$\to$model cycle is no longer hypothetical---it is already occurring in the wild---yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
7	
8	Existing tools address adjacent but distinct problems.
9	Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
10	Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
11	The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
12	No existing method estimates the ordinal recursive generation depth of a text passage from its content alone.
13	
14	Our key insight is that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are consistent across the three model families and three decoding strategies studied.
15	Specifically, perplexity tail statistics---the 90th-percentile perplexity (\textsc{p90\_ppl}) and surprisal variance (\textsc{var\_surprisal})---emerge as dominant depth indicators, ranking in the top two features by importance in 9/9 and 8/9 model--strategy configurations, respectively.
16	
17	We formalize recursive generation depth estimation as an ordinal classification task and introduce a lightweight pipeline to solve it.
18	Given a text passage, we compute a 19-dimensional feature vector from reference-model perplexity statistics---capturing distributional location, spread, tail behavior, and lexical diversity---and classify it with a Random Forest into one of $K{+}1$ depth classes ($d{=}0$ for human text through $d{=}K$ for $K$-th generation text).
19	To systematically characterize how recursive generation reshapes these features, we construct the \emph{Depth Degradation Atlas}: a $3 \times 3$ grid of model families (Pythia-1.4B, OLMo-1B, GPT-2~XL) and decoding strategies (nucleus $p{=}0.95$, temperature $\tau{=}0.9$, top-$k$ $k{=}50$), each spanning 4 generation depths, totaling 180K samples.
20	The atlas reveals strategy-dependent degradation trajectories---temperature sampling accelerates convergence toward a low-entropy attractor, while top-$k$ attenuates the depth signal---and we introduce the \emph{Effective Discriminable Depth} (EDD) metric to quantify how far into the recursion chain adjacent depths remain distinguishable.
21	
22	Our contributions are:
23	
24	\begin{itemize}
25	    \item \textbf{Task formalization.} We define recursive generation depth estimation as ordinal classification and introduce the EDD metric, which summarizes the maximum depth at which adjacent generations remain separable above a given AUC threshold.
26	
27	    \item \textbf{Depth Degradation Atlas.} We construct a systematic $3 \times 3$ map across model families and decoding strategies, revealing that \textsc{p90\_ppl} ranks in the top 2 in all 9 cells and \textsc{var\_surprisal} in 8/9, with a mean Spearman rank correlation of $\rho{=}0.868$ across importance vectors. The extended Pythia nucleus pipeline (d0--d5) yields $\mathrm{EDD}_{0.75}{=}4$, establishing that depth discrimination persists through four recursive steps before falling below threshold.
28	
29	    \item \textbf{Generalization analysis.} Cross-model leave-one-out transfer achieves 66.4\% and cross-strategy transfer 59.1\% (chance = 25\%). We decompose a temperature-induced d1/d2 AUC inversion into a scale component---partially correctable by per-strategy normalization---and a residual structural component that simple normalization cannot resolve.
30	
31	    \item \textbf{End-to-end learning.} Both DeBERTa-v3-base (58.3\%) and RoBERTa-base (59.5\%) achieve ${\sim}$59\% via end-to-end finetuning---19pp below feature-based classifiers (78.2\%)---with the architecture-invariant gap ruling out model selection bias. Linear probing confirms that PLM representations cannot recover perplexity tail features (negative $R^2$), while SHAP analysis shows these features account for 88.8\% of RF's contribution.
32	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab7489e9-2177-420c-92e8-262f41b2e13a",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "804e8cfe-6857-40fa-9d0d-a05b9cb1ad82",
  "sourceToolAssistantUUID": "ab7489e9-2177-420c-92e8-262f41b2e13a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-15T20:05:49.912Z_

Let me do one more comprehensive check for any instances of "architecture" when referring to the model groups and check for any contextual terminology issues:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "804e8cfe-6857-40fa-9d0d-a05b9cb1ad82",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xPyTmxbsPBiRFt9q3w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "caa7048e-6250-4f41-b69a-cea7c86c604e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J64H6Zs9LtfCy5JkEXdwDf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4208,
      "cache_read_input_tokens": 33230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4208,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 38 · 2026-05-15T20:05:51.236Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017ontQzch1gmVyddCMrARFc`</summary>

```json
{
  "pattern": "model.*architecture|architecture.*model|three models",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caa7048e-6250-4f41-b69a-cea7c86c604e",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xPyTmxbsPBiRFt9q3w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c93dce17-3cfc-43ea-9ba0-c53c79db4910",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J64H6Zs9LtfCy5JkEXdwDf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4208,
      "cache_read_input_tokens": 33230,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4208,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 39 · 2026-05-15T20:05:51.258Z_

<details><summary>↩ Tool result · `toolu_017ontQzch1gmVyddCMrARFc`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-41-
docs/paper/atlas.tex-42-Cross-model feature-rank Spearman correlation averages $\bar{\rho} = 0.868$ (range $[0.619, 0.954]$): models agree on which features carry depth information even when they differ in absolute accuracy.
docs/paper/atlas.tex:43:Among strategies, top-$k$ yields the highest cross-model rank correlation ($\rho = 0.811$)---the deterministic vocabulary truncation imposes a more uniform feature landscape across architectures, at the cost of weaker overall signal (\S\ref{sec:atlas:strategy}).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-44-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-45-Percentile-based features outperform their moment-based counterparts.
--
docs/paper/atlas.tex-98-\label{sec:atlas:edd}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-99-
docs/paper/atlas.tex:100:We extend the benchmark to depth $d{=}5$ for all three models under nucleus sampling.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-101-Each model's depth-3 LoRA checkpoint is used to finetune and generate depth-4 data, and the process repeats for depth~5; feature extraction uses the same reference model (GPT-2 base, 124M).
docs/paper/atlas.tex-102-We train dedicated binary RF classifiers (500 trees) for each adjacent pair, as defined in Eq.~\ref{eq:edd}.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-108-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-109-\paragraph{Cross-model convergence at depth 4--5.}
docs/paper/atlas.tex:110:All three models exhibit a consistent profile at the deep boundaries.
docs/paper/atlas.tex-111-The d3-vs-d4 AUC clusters near the $T{=}0.75$ threshold: Pythia $0.784$ (bootstrap 95\% CI $[0.765, 0.802]$, $p = 0.001$), OLMo $0.765$ ($[0.744, 0.785]$, $p = 0.091$), GPT-2~XL $0.750$ ($[0.728, 0.771]$, $p = 0.505$), where $p$ denotes the one-tailed bootstrap probability under $H_0\!: \mathrm{AUC} \leq 0.75$ (1{,}000 iterations).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-112-Only Pythia achieves significance at conventional levels; OLMo is marginal and GPT-2~XL falls on the threshold despite its higher in-distribution accuracy.
docs/paper/atlas.tex:113:The d4-vs-d5 AUC falls uniformly below 0.70 across all three models (Pythia $0.683$, OLMo $0.684$, GPT-2~XL $0.681$), confirming a model-independent signal saturation point at depth~5.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-114-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-115-This pattern---directional consistency across models with graded statistical strength---supports interpreting the d3--d4 region as a \emph{transition zone} rather than a binary boundary.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-138-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-139-% \includegraphics[width=\columnwidth]{figures/auc_decay.pdf}
docs/paper/atlas.tex:140:\caption{Binary pairwise AUC decay curves for three models (nucleus sampling, depths 0--5). Horizontal dashed lines mark $T \in \{0.65, 0.70, 0.75, 0.80\}$. All three curves converge below 0.70 at d4-vs-d5, while d3-vs-d4 AUC clusters in the range 0.750--0.784. Shaded bands: bootstrap 95\% CIs.}
docs/paper/atlas.tex-141-\label{fig:auc_decay}
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-142-\end{figure}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-18-
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-19-\paragraph{Model families.}
docs/paper/method.tex:20:We select three 1--1.5B-parameter models with diverse pretraining corpora and architectures: Pythia-1.4B (EleutherAI), OLMo-1B (AI2), and GPT-2~XL (OpenAI, 1.5B).
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-21-Restricting to a narrow parameter range isolates the effect of architecture and training data from scale.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-22-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-29-    \item \textbf{Generalization analysis.} Cross-model leave-one-out transfer achieves 66.4\% and cross-strategy transfer 59.1\% (chance = 25\%). We decompose a temperature-induced d1/d2 AUC inversion into a scale component---partially correctable by per-strategy normalization---and a residual structural component that simple normalization cannot resolve.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-30-
docs/paper/introduction.tex:31:    \item \textbf{End-to-end learning.} Both DeBERTa-v3-base (58.3\%) and RoBERTa-base (59.5\%) achieve ${\sim}$59\% via end-to-end finetuning---19pp below feature-based classifiers (78.2\%)---with the architecture-invariant gap ruling out model selection bias. Linear probing confirms that PLM representations cannot recover perplexity tail features (negative $R^2$), while SHAP analysis shows these features account for 88.8\% of RF's contribution.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-32-\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c93dce17-3cfc-43ea-9ba0-c53c79db4910",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "f4e6d9f6-5dc1-4f73-ac28-e976becb6d63",
  "sourceToolAssistantUUID": "c93dce17-3cfc-43ea-9ba0-c53c79db4910",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T20:05:51.733Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01X5NntMh35ecuHCrFiSR9GV`</summary>

```json
{
  "pattern": "these models|the three|all three",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4e6d9f6-5dc1-4f73-ac28-e976becb6d63",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xPyTmxbsPBiRFt9q3w",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d54e26b5-834d-45e3-9c4d-cce828ef56bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J64H6Zs9LtfCy5JkEXdwDf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 4208,
      "cache_read_input_tokens": 33230,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4208
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 337,
          "cache_read_input_tokens": 33230,
          "cache_creation_input_tokens": 4208,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4208,
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

_source line 41 · 2026-05-15T20:05:51.769Z_

<details><summary>↩ Tool result · `toolu_01X5NntMh35ecuHCrFiSR9GV`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-99-
docs/paper/atlas.tex:100:We extend the benchmark to depth $d{=}5$ for all three models under nucleus sampling.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-101-Each model's depth-3 LoRA checkpoint is used to finetune and generate depth-4 data, and the process repeats for depth~5; feature extraction uses the same reference model (GPT-2 base, 124M).
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-112-Only Pythia achieves significance at conventional levels; OLMo is marginal and GPT-2~XL falls on the threshold despite its higher in-distribution accuracy.
docs/paper/atlas.tex:113:The d4-vs-d5 AUC falls uniformly below 0.70 across all three models (Pythia $0.683$, OLMo $0.684$, GPT-2~XL $0.681$), confirming a model-independent signal saturation point at depth~5.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex-114-
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-38-\paragraph{Reference model.}
docs/paper/method.tex:39:All statistical features (\S\ref{sec:method:features}) are computed using a fixed reference model---GPT-2 base (124M)---that is independent of the three generation models.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex-40-The reference model computes per-token perplexity for each passage, providing a consistent measurement frame across model families.
--
docs/paper/section_appendix.tex-16-The top-2 features are stable across measures: \textsc{p90\_ppl} ranks in the top 2 in 9/9 cells under both Gini and permutation importance, and \textsc{var\_surprisal} in 8/9 (vs.\ 7/9 for Gini, with the additional cell being OLMo top-$k$; the single SHAP exception is GPT-2~XL top-$k$, where \textsc{p75\_ppl} displaces \textsc{var\_surprisal} to rank 3).
docs/paper/section_appendix.tex:17:Kendall's $W{=}0.90$ across all three methods (Gini, permutation, SHAP) indicates strong concordance ($p{<}0.005$).
docs/paper/section_appendix.tex-18-Pairwise Spearman correlations are: SHAP--Gini $\rho{=}0.93$, SHAP--permutation $\rho{=}0.84$, Gini--permutation $\rho{=}0.76$.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-13-
docs/paper/introduction.tex:14:Our key insight is that recursive generation leaves quantifiable statistical fingerprints in text, and these fingerprints are consistent across the three model families and three decoding strategies studied.
/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex-15-Specifically, perplexity tail statistics---the 90th-percentile perplexity (\textsc{p90\_ppl}) and surprisal variance (\textsc{var\_surprisal})---emerge as dominant depth indicators, ranking in the top two features by importance in 9/9 and 8/9 model--strategy configurations, respectively.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d54e26b5-834d-45e3-9c4d-cce828ef56bb",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "90c38b60-17d8-42ea-a420-a45b952e19b7",
  "sourceToolAssistantUUID": "d54e26b5-834d-45e3-9c4d-cce828ef56bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-15T20:05:53.143Z_

Now let me read the atlas and other files to look for any other terminology issues:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90c38b60-17d8-42ea-a420-a45b952e19b7",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xQDTtz2jJhri5tDCcV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0d6f8fd6-d510-486e-b4d0-a3b232dae32b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WbfdzMRuTGis81zVbyQx6r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3506,
      "cache_read_input_tokens": 37438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3506,
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

_source line 43 · 2026-05-15T20:05:53.606Z_

<details open><summary>🔧 Tool call — Read · `toolu_013v2Uwzn2HdETqofgn4eBRn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d6f8fd6-d510-486e-b4d0-a3b232dae32b",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xQDTtz2jJhri5tDCcV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f43690c5-7e81-4cc0-b96b-672eb20534cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WbfdzMRuTGis81zVbyQx6r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3506,
      "cache_read_input_tokens": 37438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3506,
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

_source line 44 · 2026-05-15T20:05:53.617Z_

<details><summary>↩ Tool result · `toolu_013v2Uwzn2HdETqofgn4eBRn`</summary>

```text
1	\section{The Depth Degradation Atlas}
2	\label{sec:atlas}
3	
4	We present the Depth Degradation Atlas: a systematic empirical map of how statistical fingerprints evolve across recursive generation depths, models, and decoding strategies.
5	The atlas spans $3 \times 3 = 9$ model--strategy cells evaluated at depths $d \in \{0, 1, 2, 3\}$, with depth extensions to $d{=}5$ for cross-model EDD validation (\S\ref{sec:atlas:edd}).
6	
7	%% ----------------------------------------------------------------
8	\subsection{In-Distribution Performance}
9	\label{sec:atlas:id}
10	
11	Table~\ref{tab:main_matrix} reports four-class Random Forest accuracy (5-fold CV, 200 trees) across all nine cells.
12	Accuracy ranges from 69.6\% (Pythia, top-$k$) to 85.4\% (GPT-2~XL, temperature), all exceeding the 25\% chance baseline by a wide margin.
13	Two axis effects emerge.
14	GPT-2~XL achieves the highest accuracy under every strategy (76.6--85.4\%), followed by OLMo (74.2--82.0\%) and Pythia (69.6--78.2\%).
15	Top-$k$ sampling yields the lowest accuracy in every model.
16	The mean within-model strategy gap is 8.4~pp, comparable to the 7.1~pp mean within-strategy model gap---decoding strategy and model family contribute roughly equally to performance variance.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Four-class RF accuracy (\%) across the $3 \times 3$ atlas, with d1--d3 three-class accuracy in parentheses (chance = 25\% / 33\%). Depth-0 recall exceeds 98\% in all cells.}
22	\label{tab:main_matrix}
23	\begin{tabular}{@{}lccc@{}}
24	\toprule
25	& Nucleus & Temp.\ $\tau{=}0.9$ & Top-$k$ \\
26	\midrule
27	Pythia-1.4B  & 78.2\,(71.2) & 76.3\,(70.6) & 69.6\,(58.8) \\
28	OLMo-1B     & 78.8\,(75.0) & 82.0\,(76.3) & 74.2\,(66.1) \\
29	GPT-2~XL    & 83.3\,(79.0) & 85.4\,(82.6) & 76.6\,(69.5) \\
30	\bottomrule
31	\end{tabular}
32	\end{table}
33	
34	%% ----------------------------------------------------------------
35	\subsection{Feature Universality}
36	\label{sec:atlas:features}
37	
38	Despite the 15.8~pp accuracy spread across cells, a small feature family dominates in every setting.
39	The 90th-percentile perplexity (\texttt{p90\_ppl}) ranks top-2 by Gini importance in all 9 cells; surprisal variance (\texttt{var\_surprisal}) in 7/9 (8/9 under SHAP; Appendix~\ref{app:permutation}).
40	Table~\ref{tab:feature_importance} shows the full per-cell ranking.
41	
42	Cross-model feature-rank Spearman correlation averages $\bar{\rho} = 0.868$ (range $[0.619, 0.954]$): models agree on which features carry depth information even when they differ in absolute accuracy.
43	Among strategies, top-$k$ yields the highest cross-model rank correlation ($\rho = 0.811$)---the deterministic vocabulary truncation imposes a more uniform feature landscape across architectures, at the cost of weaker overall signal (\S\ref{sec:atlas:strategy}).
44	
45	Percentile-based features outperform their moment-based counterparts.
46	Token-level perplexity distributions are heavy-tailed: individual outlier passages can dominate the arithmetic mean of their depth class, whereas \texttt{p90\_ppl} is robust to such extremes while still capturing the tail erosion that signals recursive depth.
47	
48	The feature hierarchy also shifts with depth.
49	At shallow boundaries (d1 vs.\ d2), \texttt{var\_surprisal} dominates importance; at deeper boundaries (d3 vs.\ d4, d4 vs.\ d5), tail perplexity statistics (\texttt{p90\_ppl}, \texttt{kurtosis\_ppl}) take over.
50	This transition aligns with model-collapse dynamics~\cite{shumailov2024_nature}: early recursion narrows the surprisal distribution (captured by its variance), while later steps erode the perplexity tail (captured by upper quantiles and kurtosis).
51	
52	\begin{table}[t]
53	\centering
54	\small
55	\caption{Top-5 features by Gini importance. \textbf{Bold}: top-2. \texttt{p90\_ppl} top-2 in 9/9; \texttt{var\_surprisal} 7/9 (8/9 under SHAP).}
56	\label{tab:feature_importance}
57	% [Populate with per-cell top-5 feature rankings from importance analysis.]
58	\begin{tabular}{@{}ll@{}}
59	\toprule
60	Cell & Top-5 features (ranked) \\
61	\midrule
62	\multicolumn{2}{@{}l}{\textit{[9-row table; see supplementary materials for importance scores]}} \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\begin{figure}[t]
68	\centering
69	% \includegraphics[width=\columnwidth]{figures/atlas_heatmap.pdf}
70	\caption{Atlas feature importance heatmap. Rows: 19 features grouped by category (\S\ref{sec:method:features}); columns: 9 model--strategy cells. Color intensity encodes RF Gini importance. The perplexity-tail and surprisal-variance blocks maintain high importance across all cells.}
71	\label{fig:atlas_heatmap}
72	\end{figure}
73	
74	%% ----------------------------------------------------------------
75	\subsection{Monotonicity and Inter-Depth Distances}
76	\label{sec:atlas:monotonicity}
77	
78	Depth features exhibit strong monotonic trends.
79	Spearman correlations between cell-level feature medians and depth $d$ range from $\rho = -0.82$ to $-0.89$ for perplexity-family features across all 9 cells.
80	Two complementary signal groups drive this structure.
81	Perplexity tail statistics (\texttt{p90\_ppl}, \texttt{mean\_surprisal}) decrease monotonically with depth ($\rho = -1.0$ across cell-level medians), reflecting the narrowing of the token-predictability distribution under recursive finetuning.
82	Repetition features (\texttt{rep\_2gram}, \texttt{rep\_3gram}, \texttt{rep\_4gram}) increase monotonically, capturing the growing self-repetition that accompanies distribution collapse.
83	
84	Inter-depth distances are non-uniform.
85	Binary d0-vs-d1 AUC exceeds 0.99 in all 9 cells, whereas d2-vs-d3 AUC ranges from 0.69 to 0.89.
86	The $d{=}0 \to d{=}1$ gap reflects the qualitative jump from human-written to machine-generated text; subsequent recursion steps produce progressively smaller distributional shifts.
87	This non-uniformity has practical implications: distinguishing real from first-generation synthetic text is near-trivial, but separating adjacent deep generations requires increasingly sensitive features---precisely the tail statistics identified in \S\ref{sec:atlas:features}.
88	
89	\begin{figure}[t]
90	\centering
91	% \includegraphics[width=\columnwidth]{figures/feature_trajectory.pdf}
92	\caption{Feature trajectories across depths $d{=}0$ to $d{=}3$, stratified by model (columns) and strategy (line style). Top row: \texttt{p90\_ppl} (monotonically decreasing). Middle: \texttt{var\_surprisal} (decreasing). Bottom: \texttt{rep\_3gram} (increasing). Shaded bands: interquartile range. The $d{=}0 \to d{=}1$ gap exceeds all subsequent inter-depth gaps.}
93	\label{fig:feature_trajectory}
94	\end{figure}
95	
96	%% ----------------------------------------------------------------
97	\subsection{EDD Analysis}
98	\label{sec:atlas:edd}
99	
100	We extend the benchmark to depth $d{=}5$ for all three models under nucleus sampling.
101	Each model's depth-3 LoRA checkpoint is used to finetune and generate depth-4 data, and the process repeats for depth~5; feature extraction uses the same reference model (GPT-2 base, 124M).
102	We train dedicated binary RF classifiers (500 trees) for each adjacent pair, as defined in Eq.~\ref{eq:edd}.
103	
104	\paragraph{AUC decay profile.}
105	Figure~\ref{fig:auc_decay} plots the binary pairwise AUC decay curves.
106	For Pythia-1.4B (nucleus), AUC decays monotonically: d0-vs-d1 $= 0.999$, d1-vs-d2 $= 0.925$, d2-vs-d3 $= 0.823$, d3-vs-d4 $= 0.784$, d4-vs-d5 $= 0.683$.
107	The steepest drop occurs between the d1-vs-d2 and d2-vs-d3 pairs; the curve then flattens as the system approaches an indistinguishable regime gradually rather than crossing a sharp boundary.
108	
109	\paragraph{Cross-model convergence at depth 4--5.}
110	All three models exhibit a consistent profile at the deep boundaries.
111	The d3-vs-d4 AUC clusters near the $T{=}0.75$ threshold: Pythia $0.784$ (bootstrap 95\% CI $[0.765, 0.802]$, $p = 0.001$), OLMo $0.765$ ($[0.744, 0.785]$, $p = 0.091$), GPT-2~XL $0.750$ ($[0.728, 0.771]$, $p = 0.505$), where $p$ denotes the one-tailed bootstrap probability under $H_0\!: \mathrm{AUC} \leq 0.75$ (1{,}000 iterations).
112	Only Pythia achieves significance at conventional levels; OLMo is marginal and GPT-2~XL falls on the threshold despite its higher in-distribution accuracy.
113	The d4-vs-d5 AUC falls uniformly below 0.70 across all three models (Pythia $0.683$, OLMo $0.684$, GPT-2~XL $0.681$), confirming a model-independent signal saturation point at depth~5.
114	
115	This pattern---directional consistency across models with graded statistical strength---supports interpreting the d3--d4 region as a \emph{transition zone} rather than a binary boundary.
116	The continuous AUC decay curve provides a more informative characterization of depth discriminability than any single $\mathrm{EDD}_T$ value.
117	
118	\paragraph{EDD threshold sensitivity.}
119	Table~\ref{tab:edd_sensitivity} reports $\mathrm{EDD}_T$ across the primary 9-cell benchmark (depths 0--3) at four threshold values.
120	At $T{=}0.65$, all 9 cells achieve $\mathrm{EDD} = 3$; at $T{=}0.75$, 7 of 9 cells maintain $\mathrm{EDD} \geq 3$; at $T{=}0.80$, the count drops to 5 of 9.
121	The cells losing $\mathrm{EDD}{=}3$ first are consistently the top-$k$ configurations (Pythia top-$k$ at $T{=}0.70$, then OLMo top-$k$ at $T{=}0.75$), where the d2-vs-d3 pair is the consistent bottleneck across all 9 cells.
122	
123	\begin{table}[t]
124	\centering
125	\small
126	\caption{Number of atlas cells achieving $\mathrm{EDD} \geq 3$ at each threshold $T$, across 9 model--strategy cells (depths 0--3). The d2-vs-d3 boundary is the bottleneck; top-$k$ cells drop first.}
127	\label{tab:edd_sensitivity}
128	\begin{tabular}{@{}lcccc@{}}
129	\toprule
130	& $T{=}0.65$ & $T{=}0.70$ & $T{=}0.75$ & $T{=}0.80$ \\
131	\midrule
132	Cells with $\mathrm{EDD} \geq 3$ & 9/9 & 8/9 & 7/9 & 5/9 \\
133	\bottomrule
134	\end{tabular}
135	\end{table}
136	
137	\begin{figure}[t]
138	\centering
139	% \includegraphics[width=\columnwidth]{figures/auc_decay.pdf}
140	\caption{Binary pairwise AUC decay curves for three models (nucleus sampling, depths 0--5). Horizontal dashed lines mark $T \in \{0.65, 0.70, 0.75, 0.80\}$. All three curves converge below 0.70 at d4-vs-d5, while d3-vs-d4 AUC clusters in the range 0.750--0.784. Shaded bands: bootstrap 95\% CIs.}
141	\label{fig:auc_decay}
142	\end{figure}
143	
144	\paragraph{Decision boundary dilution.}
145	\label{sec:atlas:edd:dilution}
146	EDD's binary-pair design is motivated by \emph{decision boundary dilution}: when a multi-class classifier must simultaneously separate $K$ depths, its decision boundaries are shared across all $\binom{K}{2}$ class pairs, diluting the capacity allocated to any single adjacent pair.
147	Concretely, in the Pythia nucleus setting, the d2\,vs.\,d3 pairwise AUC degrades from 0.804 in a 4-class pipeline to 0.689 in a 6-class pipeline---a 14.3\% relative decline---despite identical underlying data.
148	Mean classification accuracy likewise drops from 99.5\% (binary) to 78.3\% (4-class) to 62.9\% (6-class).
149	Because the pairwise signal between depths $d$ and $d{+}1$ does not change when unrelated depths are added, this degradation is entirely attributable to boundary dilution, not signal loss.
150	Binary pairwise classifiers eliminate this confound, isolating the true adjacent-pair discriminability that EDD is designed to measure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f43690c5-7e81-4cc0-b96b-672eb20534cb",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "ae9439d3-a446-46c1-8b86-df2a32a5dfbd",
  "sourceToolAssistantUUID": "f43690c5-7e81-4cc0-b96b-672eb20534cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T20:05:53.729Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UGBuERvTYa4XGBzeWbe2JF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae9439d3-a446-46c1-8b86-df2a32a5dfbd",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xQDTtz2jJhri5tDCcV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "be93cf60-f507-4af0-87c9-15b1cf4dd96f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WbfdzMRuTGis81zVbyQx6r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3506,
      "cache_read_input_tokens": 37438,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3506
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 214,
          "cache_read_input_tokens": 37438,
          "cache_creation_input_tokens": 3506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3506,
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

_source line 46 · 2026-05-15T20:05:53.734Z_

<details><summary>↩ Tool result · `toolu_01UGBuERvTYa4XGBzeWbe2JF`</summary>

```text
1	\section{Generalization and Robustness}
2	\label{sec:generalization}
3	
4	We test whether the atlas results (69.6--85.4\%) reflect genuine statistical regularities or training artifacts, evaluating four axes: classifier choice (\S\ref{sec:gen:baselines}), cross-model transfer (\S\ref{sec:gen:crossmodel}), cross-strategy transfer (\S\ref{sec:gen:crossstrategy}), and end-to-end learning (\S\ref{sec:gen:e2e}).
5	
6	\subsection{Baseline Comparison}
7	\label{sec:gen:baselines}
8	
9	Table~\ref{tab:baselines} compares classification methods on the Pythia-1.4B nucleus setting.
10	Five feature-based methods spanning bagging (RF), gradient boosting (XGBoost, LightGBM), ordinal regression (CORAL \cite{coral2020}), and a detection-oriented ensemble (DivEye \cite{diveye2026}) all operate on the same 19 features and converge within $\leq$0.9pp (78.1--79.0\%; pairwise bootstrap $p>0.05$, Bonferroni-corrected), establishing a feature-determined accuracy ceiling.
11	All five significantly outperform CE-MLP ($p<0.001$, $+$3.2pp).
12	Single-feature regression on mean perplexity performs at chance (25.1\%), confirming that depth estimation requires the multi-dimensional feature representation defined in \S\ref{sec:method}.
13	
14	\begin{table}[t]
15	\centering
16	\small
17	\caption{Comparison of classification methods on Pythia-1.4B nucleus. Five feature-based methods (RF, XGBoost, LightGBM, CORAL, DivEye) all operate on the same 19 features and converge within $\leq$0.9pp (78.1--79.0\%). Chance = 25\%. 5-fold CV std: 0.2--0.9pp.}
18	\label{tab:baselines}
19	\begin{tabular}{lc}
20	\toprule
21	Method & 4-class Acc (\%) \\
22	\midrule
23	RF (19 features) & 78.2 \\
24	XGBoost & 79.0 \\
25	LightGBM & 78.8 \\
26	CORAL & 78.1 \\
27	DivEye & 78.2 \\
28	CE-MLP & 74.9 \\
29	LR & 75.0 \\
30	DeepSeek V3.2 (zero-shot)\footnotemark & 36.2 \\
31	ppl-regression (single feature) & 25.1 \\
32	\bottomrule
33	\end{tabular}
34	\footnotetext{Evaluated on 500 samples (125 per class) from the Pythia-1.4B nucleus cell only, due to API cost; 95\% CI: $[32.0\%, 40.4\%]$. All other methods use the full 20{,}000-sample set.}
35	\end{table}
36	
37	Convergence across five structurally different classifiers---including both bagging and gradient-boosting families---confirms the signal resides in the features, not the learning algorithm; a zero-shot LLM (DeepSeek V3.2) reaches only 36.2\%.
38	Figure~\ref{fig:confusion_matrix} shows d0 near-perfectly identified; errors concentrate at d2/d3 in-distribution and spread across d1--d3 under transfer.
39	
40	\begin{figure}[t]
41	\centering
42	\includegraphics[width=\columnwidth]{figures/fig_confusion_matrix.pdf}
43	\caption{Confusion matrices for the best in-distribution setting (GPT-2 XL, temp $\tau{=}0.9$, 85.4\%) and the best cross-model leave-one-out transfer (OLMo holdout, 69.2\%). d0 recall exceeds 99\% in both; errors spread across the d1--d3 range under transfer.}
44	\label{fig:confusion_matrix}
45	\end{figure}
46	
47	\subsection{Cross-Model Transfer}
48	\label{sec:gen:crossmodel}
49	
50	We perform leave-one-model-family-out evaluation: train on two families (nucleus only), test on the held-out third (Table~\ref{tab:cross_model}).
51	
52	\begin{table}[t]
53	\centering
54	\small
55	\caption{Cross-model transfer (leave-one-out, nucleus only). Chance = 25\% / 33\% (d1--d3). d1--d3 bal.\ acc: Pythia 49.9\%, OLMo 59.2\%, GPT-2~XL 57.2\% (mean 55.4\%).}
56	\label{tab:cross_model}
57	\begin{tabular}{lccccc}
58	\toprule
59	Holdout & Acc & d0 & d1 & d2 & d3 \\
60	 & (\%) & Rec. & Rec. & Rec. & Rec. \\
61	\midrule
62	Pythia & 62.4 & 100.0 & 49.3 & 26.8 & 73.6 \\
63	OLMo & \textbf{69.2} & 99.3 & 75.5 & 43.3 & 58.8 \\
64	GPT-2 XL & 67.6 & 98.5 & 74.7 & 52.6 & 44.5 \\
65	\midrule
66	Mean & 66.4 & 99.3 & 66.5 & 40.9 & 59.0 \\
67	\bottomrule
68	\end{tabular}
69	\end{table}
70	
71	Mean transfer accuracy is 66.4\% (2.7$\times$ chance); d0 recall ($>$98\%) inflates the headline while d2 drops to 26.8\% (Pythia holdout).
72	Excluding d0, d1--d3 balanced accuracy averages 55.4\% (chance = 33\%).
73	
74	\subsection{Cross-Strategy Transfer}
75	\label{sec:gen:crossstrategy}
76	
77	We train on two decoding strategies and test on the held-out third (Table~\ref{tab:cross_strategy}).
78	
79	\begin{table}[t]
80	\centering
81	\small
82	\caption{Cross-strategy transfer (leave-one-out). Chance = 25\% / 33\% (d1--d3). d0 recall $\geq$89.5\% inflates headline; d1--d3 mean: 45.9\%.}
83	\label{tab:cross_strategy}
84	\begin{tabular}{lccc}
85	\toprule
86	Holdout & Pythia & OLMo & GPT-2 XL \\
87	 & Acc (\%) & Acc (\%) & Acc (\%) \\
88	\midrule
89	nucleus & \textbf{69.4} & \textbf{65.4} & \textbf{59.9} \\
90	temp ($\tau{=}0.9$) & 62.8 & 58.2 & 56.1 \\
91	top-$k$ ($k{=}50$) & 51.5 & 54.9 & 53.6 \\
92	\bottomrule
93	\end{tabular}
94	\end{table}
95	
96	Mean cross-strategy accuracy (59.1\%) falls 7pp below cross-model transfer (66.4\%); excluding d0, d1--d3 accuracy drops to 45.9\% (chance = 33\%), with d2 recall ranging from 3.7\% to 19\%---strategy-induced shifts pose a greater challenge than architectural differences.
97	
98	\paragraph{Temperature-induced boundary inversion.}
99	Training on nucleus + top-$k$ and testing on temperature inverts the d1/d2 boundary (d1v2 AUC $<$ 0.5; \S\ref{sec:atlas:strategy}).
100	Per-strategy z-score normalization partially recovers the boundary but leaves a residual gap to within-strategy performance (per-model details in Limitations).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be93cf60-f507-4af0-87c9-15b1cf4dd96f",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "7b6f2516-42f6-43e5-877b-7293afbb42f8",
  "sourceToolAssistantUUID": "be93cf60-f507-4af0-87c9-15b1cf4dd96f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-15T20:05:55.103Z_

Now let me check the related work and conclusion files for any additional terminology issues:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b6f2516-42f6-43e5-877b-7293afbb42f8",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xQMyrwU8oh7UhqYxEY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c6ad7ca8-d769-4eba-8bbe-d924c176bfa3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0168vX4szb7p3nEhXPDhCvqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6543,
      "cache_read_input_tokens": 40944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6543,
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

_source line 48 · 2026-05-15T20:05:56.026Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NDGH12ZiJyqM2W298fStTq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6ad7ca8-d769-4eba-8bbe-d924c176bfa3",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xQMyrwU8oh7UhqYxEY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c612f551-4b94-4678-9448-3e512115ee39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0168vX4szb7p3nEhXPDhCvqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6543,
      "cache_read_input_tokens": 40944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6543,
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

### Tool result

_source line 49 · 2026-05-15T20:05:56.031Z_

<details><summary>↩ Tool result · `toolu_01NDGH12ZiJyqM2W298fStTq`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	\citet{shumailov2024_nature} demonstrate that recursively training language models on their own outputs erodes distributional tails, eventually collapsing the output distribution to a narrow mode.
6	\citet{dohmatob2024_tale_of_tails} formalize this phenomenon through scaling laws that distinguish tail \emph{narrowing} (reduced variance) from tail \emph{cutting} (lost support), showing both accelerate with generation depth; \citet{dohmatob2024_strong_collapse} establish strong collapse guarantees, and \citet{dohmatob2024_demystified} analyze the regression case.
7	The MAD framework \cite{alemohammad2024_mad} extends this analysis to self-consuming generative models and quantifies the precision--recall tradeoff as synthetic data accumulates across generations.
8	Mitigation strategies include retaining real data \cite{gerstgrasser2024_accumulate} and filtering synthetic samples via detection \cite{drayson2025_detection_prevents_collapse}.
9	Recent work identifies non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, fixed-point convergence \cite{marchi2024_heat_death}, contamination bounds \cite{wang2026_contamination}, curated pipelines \cite{falahati2026_curated}, knowledge collapse \cite{knowledge_collapse2025}, spectral signatures \cite{sigma2026_spectral}, and self-improving loops \cite{synthetic_eggs2026}.
10	These works characterize degradation patterns but assume the generation depth is known a priori; our work addresses the inverse problem of estimating depth from text alone.
11	
12	\paragraph{AI Text Detection.}
13	DetectGPT \cite{mitchell2023_detectgpt} introduced probability curvature---the tendency of model-generated text to occupy local maxima of the log-probability surface---as a zero-shot detection signal.
14	\citet{fast_detectgpt2024} improve computational efficiency by replacing random perturbations with conditional probability curvature from a surrogate model.
15	Binoculars \cite{binoculars2024} exploits the perplexity ratio between two related models, achieving strong detection without training data.
16	DivEye \cite{diveye2026} leverages surprisal diversity patterns, while GLTR \cite{gehrmann2019_gltr} provides statistical visualization of per-token likelihood ranks for human inspection.
17	\citet{sadasivan2023_paraphrase} expose fundamental limits: paraphrasing attacks reduce detection accuracy to near chance, and \citet{pudasaini2026_detection_fails} show detection degrades under distribution shift between training and deployment domains.
18	\citet{pu2026_generator_barrier} formalize a generator barrier bounding detection performance when the generator is unknown.
19	Ghostbuster \cite{verma2024_ghostbuster} trains classifiers on statistical features (token probabilities, rank sequences) for binary detection, sharing our feature-engineering philosophy but not addressing depth.
20	The M4-SemEval shared task \cite{wang2024_m4_semeval} benchmarks multilingual machine-generated text detection across diverse generators, and DNA-GPT \cite{yang2024_dnagpt} uses divergent $n$-gram analysis to detect AI text without model access.
21	All these methods perform binary classification (human vs.\ machine), discarding the ordinal depth information that distinguishes first-generation from deeply recursive text.
22	Our approach outputs ordinal depth labels, complementing rather than replacing binary detection.
23	
24	\paragraph{Adjacent Tasks.}
25	EditLens \cite{editlens2026} estimates the \emph{extent} of editing applied to a passage---a continuous measure of how much a text has been modified in a single pass---but does not model recursive generation chains.
26	\citet{uchendu2020_attribution} formulate authorship attribution as multi-source classification, identifying \emph{which} model generated a text rather than \emph{how many} recursive steps it has undergone.
27	LOKI \cite{loki2025} provides a comprehensive benchmark spanning multiple synthetic data modalities but evaluates binary detection, not depth estimation.
28	\citet{mohamed2025_broken_telephone} study iterative generation as a ``broken telephone'' effect, quantifying information distortion across rounds; while their work measures forward degradation fidelity, our task performs the inverse: classifying generation depth from text alone, without access to the generation chain.
29	
30	\paragraph{Decoding Strategy Effects.}
31	The choice of decoding strategy shapes the statistical properties of generated text in ways that interact with generation depth signals.
32	\citet{holtzman2020_nucleus} show that unrestricted sampling produces degenerate repetitions and propose nucleus sampling to maintain output diversity.
33	\citet{finlayson2024_closing} demonstrate that decoding parameters affect downstream evaluation metrics in non-trivial ways.
34	\citet{garces_arias2025_decoding_decoded} find that the effect of decoding strategies on text quality is model-dependent, complicating universal quality claims.
35	\citet{wiher2022_decoding} provide a systematic comparison of decoding methods on surface-level text properties, and Mirostat \cite{basu2021_mirostat} introduces perplexity-controlled decoding that actively regulates output entropy.
36	Our Depth Degradation Atlas (\S\ref{sec:atlas}) reveals that these strategies induce qualitatively different degradation trajectories under recursive generation---temperature sampling accelerates convergence to a low-entropy attractor while top-$k$ attenuates the depth signal---effects that go beyond single-pass text quality to shape the discriminability of generation depth itself.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c612f551-4b94-4678-9448-3e512115ee39",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "fdf7c081-8974-49b0-ac34-a8e4ecdd6716",
  "sourceToolAssistantUUID": "c612f551-4b94-4678-9448-3e512115ee39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T20:05:56.153Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VScwR5HGn6kzFWhHB381Fd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdf7c081-8974-49b0-ac34-a8e4ecdd6716",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xQMyrwU8oh7UhqYxEY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9aff2ed4-0cec-4dc5-b999-8a254f574850",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0168vX4szb7p3nEhXPDhCvqm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6543,
      "cache_read_input_tokens": 40944,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6543
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 180,
          "cache_read_input_tokens": 40944,
          "cache_creation_input_tokens": 6543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6543,
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

_source line 51 · 2026-05-15T20:05:56.159Z_

<details><summary>↩ Tool result · `toolu_01VScwR5HGn6kzFWhHB381Fd`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Cross-strategy deployment constraint.}
5	Cross-strategy transfer induces a d1/d2 boundary inversion under temperature sampling.
6	Per-strategy z-score normalization partially corrects the inversion (GPT-2~XL d1v2 AUC $0.24{\to}0.56$, OLMo $0.19{\to}0.70$) but leaves a residual gap relative to within-strategy performance (${\sim}0.83$), indicating that a two-stage pipeline (strategy identification + strategy-conditioned classification) is needed for reliable cross-strategy deployment.
7	
8	\paragraph{d0 inflation of headline metrics.}
9	Depth~0 (human-written text) is near-perfectly separable (recall $>$98\% across all settings), inflating headline accuracy.
10	Cross-model transfer accuracy of 66.4\% is substantially driven by d0; d2 recall drops to 26.8\% in the worst case (Pythia holdout).
11	
12	\paragraph{Controlled vs.\ ecological setting.}
13	All experiments use Wikipedia seed text with controlled recursive generation (LoRA fine-tuning, 1--1.5B parameter models).
14	While depth signal is the dominant classification factor (5-fold CV 59--82\%, 3.4$\times$ chance), a residual domain signal from seed-article stylistic differences exists (${\sim}$2$\times$ chance conditional on seed group; LOGO accuracy drops 8pp on average; Appendix~\ref{app:domain_bias}).
15	In the most affected cell (Pythia top-$k$), individual LOGO folds drop to 22.9\%, approaching chance.
16	Transfer to mixed-domain corpora, instruction-tuned models, and larger scales (7B+) remains open.
17	Real-world documents may also interleave segments at different recursion depths; extending to segment-level estimation introduces a granularity--statistical-power tradeoff.
18	
19	\paragraph{Adversarial robustness.}
20	Adversarial paraphrasing \cite{sadasivan2023_paraphrase} could disrupt the perplexity tail features that drive classification; depth estimation's robustness under such attacks is untested.
21	
22	\paragraph{EDD monotonicity assumption.}
23	Our EDD definition (Eq.~\ref{eq:edd}) requires all pairwise AUCs up to depth $d^*$ to exceed $T$, which is well-behaved when AUC decays monotonically---as observed in all our configurations.
24	However, \citet{bakshi2026_collapse_improvement} show that early recursion can temporarily \emph{improve} model quality, which could produce non-monotonic AUC profiles (e.g., a dip at d1/d2 followed by recovery at d2/d3).
25	Our cross-strategy transfer results provide an empirical example: training on nucleus + top-$k$ and testing on temperature yields d1-vs-d2 AUC as low as 0.129 (GPT-2~XL) and 0.253 (OLMo), violating the monotonicity assumption.
26	In such cases EDD would conservatively report a lower value than the deepest discriminable pair, potentially underestimating the true discriminable range; extending EDD to handle non-contiguous discriminable regions is future work.
27	The choice of threshold $T$ is also application-dependent: at $T{=}0.80$, several cells lose one depth level relative to $T{=}0.75$.
28	
29	\paragraph{Reference model dependency.}
30	Surprisal-based features are computed relative to GPT-2 base (124M), introducing partial overlap when GPT-2~XL is held out, though GPT-2~XL holdout accuracy (67.6\%) does not exceed the unrelated OLMo (69.2\%).
31	The choice of reference model affects feature values; a different reference model may shift absolute feature magnitudes and potentially alter discriminability at depth boundaries.
32	
33	\paragraph{Additional caveats.}
34	Detection features degrade under domain shift \cite{pudasaini2026_detection_fails}; our depth features are likely susceptible.
35	\citet{falahati2026_curated} show that curated synthetic data need not trigger collapse, attenuating the fingerprints we exploit.
36	
37	\section*{Ethics Statement}
38	
39	This work uses publicly available pretrained language models (Pythia-1.4B, OLMo-1B, GPT-2~XL) and Wikipedia text as seed data.
40	No human subjects were involved, no private or sensitive data were collected, and no new models were released.
41	Our method is intended to support data provenance and training-data auditing; we acknowledge that depth estimation tools could in principle be misused to circumvent content moderation, though such risks are shared with all detection-oriented research.
42	Code and data will be released upon acceptance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9aff2ed4-0cec-4dc5-b999-8a254f574850",
  "isSidechain": true,
  "promptId": "122b271a-e3fe-4268-9664-b0c85727d227",
  "agentId": "a6c7950c9417f13a3",
  "type": "user",
  "uuid": "06fd2812-425c-4ca2-b4b0-8814f5cf9dfa",
  "sourceToolAssistantUUID": "9aff2ed4-0cec-4dc5-b999-8a254f574850",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-15T20:06:12.580Z_

Perfect! Now let me compile my comprehensive findings. Let me create a summary of all the terminology inconsistencies I found:

## Comprehensive Terminology Inconsistency Report

Based on a thorough search of all .tex files in `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/`, here are the findings:

### 1. "Hand-crafted" or "handcrafted" (variant of "statistical features")
**Result**: No matches found.

### 2. "Statistical fingerprint" (as a noun, not "statistical fingerprints")
**Findings**: Found multiple instances of "statistical fingerprints" (plural), but looking for singular usage:
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:4` - "statistical fingerprints" (plural - INCONSISTENT if singular is preferred)
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:165` - "statistical fingerprint" (singular - CORRECT)
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:99` - "statistical fingerprints" (plural)
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex:14` - "statistical fingerprints" (plural - appears twice)

**Inconsistency**: Inconsistent usage between singular and plural forms throughout the paper.

### 3. "Sampling strategy" or "generation strategy" (vs "decoding strategy")
**Result**: No matches found for "sampling strategy" or "generation strategy" - the paper consistently uses "decoding strategy" throughout, which is the preferred terminology.

### 4. "Feature-based method" or "statistical method"
**Findings**: Multiple consistent uses of "feature-based" (all correct):
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:10` - "Five feature-based methods" 
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:17` - "Five feature-based methods"
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/generalization.tex:107` - "feature-based methods"
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:25` - "feature-based methods"
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:52` - "feature-based and end-to-end methods"

**Inconsistency**: None detected - consistent use of "feature-based methods" throughout.

### 5. EDD formatting: "\text{EDD}" (should be "\mathrm{EDD}")
**Findings**: All instances use the CORRECT `\mathrm{EDD}` format:
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex:6` - `$\mathrm{EDD}_{0.75}{=}4$`
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:116` - `$\mathrm{EDD}_T$`
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:119` - `$\mathrm{EDD}_T$`
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:120` - `$\mathrm{EDD} = 3$`
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:121` - `$\mathrm{EDD}{=}3$`
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:126` - `$\mathrm{EDD} \geq 3$`
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:132` - `$\mathrm{EDD} \geq 3$`
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex:4` - `$\mathrm{EDD}_{0.75}{=}4$`
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:91` - `\mathrm{EDD}_T`

**Inconsistency**: None detected - all uses of EDD correctly employ `\mathrm{EDD}`.

### 6. "Model family" vs just "model" or "architecture" when referring to Pythia/OLMo/GPT-2 XL groups
**Findings**: Consistent usage of "model family" and "model families":
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:17` - "model family"
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:19` - "Model families"
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:40` - "model families"
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:16` - "model family"
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex:14` - "model families"
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex:19` - "model families"

However, instances of "architecture" used to refer to differences between model families appear sparingly:
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:20` - "architectures" (referring to the three models)
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:21` - "architecture" in context of isolating effects
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/introduction.tex:31` - "architecture-invariant gap"
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/atlas.tex:43` - "architectures" (referring to models in "across architectures")

**Inconsistency**: Minor inconsistency - "model family" is preferred and used predominantly, but "architecture" is occasionally used as a synonym when discussing the three model groups.

### 7. "Statistical features" occurrences
**Findings**: Multiple consistent uses throughout:
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex:19` - "statistical features"
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex:4` - "19 statistical features"
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/abstract.tex:4` - "19 statistical features"
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:39` - "All statistical features"
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/method.tex:52` - "19 statistical features"
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:49` - "statistical features"
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/section_appendix.tex:52` - "statistical features"

**Inconsistency**: None detected - consistent use of "statistical features" throughout.

---

## Summary of Issues Found

1. **Most Significant**: "Statistical fingerprints" vs "statistical fingerprint" - **plural/singular inconsistency** across the paper (lines in atlas.tex:4, atlas.tex:165, method.tex:99, introduction.tex:14)

2. **Minor**: Occasional use of "architectures" as a synonym for "model families" in atlas.tex:43 and method.tex:20-21, though "model family/families" is the dominant and preferred terminology.

3. **No Issues Found**: EDD formatting, feature-based methods terminology, decoding strategy naming, and statistical features usage are all consistent throughout the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06fd2812-425c-4ca2-b4b0-8814f5cf9dfa",
  "isSidechain": true,
  "agentId": "a6c7950c9417f13a3",
  "requestId": "req_011Cb4xQYFzfQ6eNkGhgBSJe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "98f7c99c-c994-4769-bed8-7707e3a7032f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "1666c4a0-8f6e-4585-b596-b002a261cef8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KNjk7qyXpXMref6skHKpsr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2873,
      "cache_read_input_tokens": 47487,
      "output_tokens": 2539,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2873
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2539,
          "cache_read_input_tokens": 47487,
          "cache_creation_input_tokens": 2873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2873,
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
