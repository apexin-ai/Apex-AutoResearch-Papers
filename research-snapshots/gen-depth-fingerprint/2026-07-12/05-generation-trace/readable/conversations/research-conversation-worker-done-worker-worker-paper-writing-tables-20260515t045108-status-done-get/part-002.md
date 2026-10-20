# Research conversation: [WORKER DONE] Worker worker_paper_writing_tables_20260515T045108 已完成（status=done）。用 `get_worker_status('worker_paper_wri — Part 2 of 7

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-worker-done-worker-worker-paper-writing-tables-20260515t045108-status-done-get.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/79/79bb6a74a12c5dd6568f.json)

## Round 16

### Assistant

_source line 294 · 2026-05-15T05:05:04.331Z_

<details><summary>Logged reasoning block</summary>

```text
OK so the integrate-and-compile worker already fixed line 11 to 0.789 and line 47 caption to 0.789. But it didn't fix the per-generator table numbers or other issues.

Let me fix the remaining issues:

1. Line 12: 0.685 → 0.683, 0.855 → 0.856
2. Line 17: 0.685 → 0.683
3. Lines 36-44: per-generator F1s and averages
4. Lines 66-67: Spearman correlations
5. Line 71: F1=0.790 → 0.789


6. Line 72: importance values
7. Line 88: table values

Now I need to apply all these corrections to get the metrics consistent throughout the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "412bbbde-08ed-46e3-8451-4f6bd9d06149",
  "isSidechain": false,
  "requestId": "req_011Cb3mhYkCiVktoyoprsqwS",
  "type": "assistant",
  "uuid": "c5531924-37cc-499c-b206-34916eb41456",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJqjjrkDFKm5TQBkYrVPoD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4015,
      "cache_read_input_tokens": 100721,
      "output_tokens": 1213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4015,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1213,
          "cache_read_input_tokens": 100721,
          "cache_creation_input_tokens": 4015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4015
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


### Tool call

_source line 295 · 2026-05-15T05:05:05.020Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Gns2emnNfmkLi1z6VYYH2w`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
  "old_string": "Per-generator held-out F1 ranges from 0.685 (Qwen3-8B) to 0.855 (Pythia-1B).",
  "new_string": "Per-generator held-out F1 ranges from 0.683 (Qwen3-8B) to 0.856 (Pythia-1B)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5531924-37cc-499c-b206-34916eb41456",
  "isSidechain": false,
  "requestId": "req_011Cb3mhYkCiVktoyoprsqwS",
  "type": "assistant",
  "uuid": "d2b13cd7-acf3-4b4d-8583-819bb6e1171b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJqjjrkDFKm5TQBkYrVPoD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4015,
      "cache_read_input_tokens": 100721,
      "output_tokens": 1213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4015,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1213,
          "cache_read_input_tokens": 100721,
          "cache_creation_input_tokens": 4015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4015
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

_source line 296 · 2026-05-15T05:05:05.042Z_

<details><summary>↩ Tool result · `toolu_01Gns2emnNfmkLi1z6VYYH2w`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2b13cd7-acf3-4b4d-8583-819bb6e1171b",
  "isSidechain": false,
  "promptId": "0ffb5ebe-9671-48cd-98cf-674bf708f562",
  "type": "user",
  "uuid": "f25c4d3a-1952-45d5-9b8b-e12f59d38170",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
    "oldString": "Per-generator held-out F1 ranges from 0.685 (Qwen3-8B) to 0.855 (Pythia-1B).",
    "newString": "Per-generator held-out F1 ranges from 0.683 (Qwen3-8B) to 0.856 (Pythia-1B).",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " Table~\\ref{tab:logo-results} reports leave-one-generator-out (LOGO) macro-F1 for 3-class depth estimation (gen-0\\,/\\,gen-1\\,/\\,gen-2+) across six generators spanning three model families and parameter counts from 0.6B to 8.2B.",
          " ",
          " The 7-feature ensemble achieves LOGO F1\\,=\\,0.789, significantly outperforming all single-detector baselines ($p<0.001$; \\S\\ref{sec:results-baselines}).",
          "-Per-generator held-out F1 ranges from 0.685 (Qwen3-8B) to 0.855 (Pythia-1B).",
          "+Per-generator held-out F1 ranges from 0.683 (Qwen3-8B) to 0.856 (Pythia-1B).",
          " Gen-0 classification is near-perfect (per-class F1\\,$\\approx$\\,0.95); the primary difficulty lies in distinguishing gen-1 from gen-2+, where feature margins narrow.",
          " ",
          " \\paragraph{Cross-scale transfer.}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "d2b13cd7-acf3-4b4d-8583-819bb6e1171b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 297 · 2026-05-15T05:05:07.056Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01WtGMqyrLnWXZXoxyjJ4LzK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
  "old_string": "Qwen3-8B held-out F1\\,=\\,0.685 (CI [0.672, 0.698])",
  "new_string": "Qwen3-8B held-out F1\\,=\\,0.683 (CI [0.672, 0.698])"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f25c4d3a-1952-45d5-9b8b-e12f59d38170",
  "isSidechain": false,
  "requestId": "req_011Cb3mhYkCiVktoyoprsqwS",
  "type": "assistant",
  "uuid": "9ea7b439-37dc-4ed9-8ebb-7bf5376205cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJqjjrkDFKm5TQBkYrVPoD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4015,
      "cache_read_input_tokens": 100721,
      "output_tokens": 1213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4015,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1213,
          "cache_read_input_tokens": 100721,
          "cache_creation_input_tokens": 4015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4015
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

_source line 298 · 2026-05-15T05:05:07.069Z_

<details><summary>↩ Tool result · `toolu_01WtGMqyrLnWXZXoxyjJ4LzK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ea7b439-37dc-4ed9-8ebb-7bf5376205cb",
  "isSidechain": false,
  "promptId": "0ffb5ebe-9671-48cd-98cf-674bf708f562",
  "type": "user",
  "uuid": "6e774609-7b7d-45e9-89f5-027190b753bf",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
    "oldString": "Qwen3-8B held-out F1\\,=\\,0.685 (CI [0.672, 0.698])",
    "newString": "Qwen3-8B held-out F1\\,=\\,0.683 (CI [0.672, 0.698])",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 14,
        "oldLines": 7,
        "newStart": 14,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Cross-scale transfer.}",
          " The six-generator evaluation includes Qwen3-8B (8.2B parameters), confirming that depth signal persists at scales beyond the $\\leq$2.8B training generators.",
          "-However, cross-scale transfer incurs a moderate gap: Qwen3-8B held-out F1\\,=\\,0.685 (CI [0.672, 0.698]), compared to 0.76--0.86 for $\\leq$2.8B generators.",
          "+However, cross-scale transfer incurs a moderate gap: Qwen3-8B held-out F1\\,=\\,0.683 (CI [0.672, 0.698]), compared to 0.76--0.86 for $\\leq$2.8B generators.",
          " Text generated by larger models is more fluent, compressing feature margins and making depth distinctions harder.",
          " Notably, adding Qwen3-8B data \\emph{improves} classification on the original five generators (+0.9\\,pp to 0.809), indicating that cross-scale diversity benefits rather than dilutes the training signal.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "9ea7b439-37dc-4ed9-8ebb-7bf5376205cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 299 · 2026-05-15T05:05:11.506Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01EdsusTcUdBVw9Rx22RG9ys`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
  "old_string": "Pythia-1B       & Pythia & 1.0B & 0.855 \\\\\nPythia-2.8B     & Pythia & 2.8B & 0.804 \\\\\nOLMo-2-1B      & OLMo   & 1.5B & 0.762 \\\\\nQwen3-0.6B     & Qwen   & 0.6B & 0.823 \\\\\nQwen3-1.7B     & Qwen   & 1.7B & 0.809 \\\\\nQwen3-8B       & Qwen   & 8.2B & 0.685 \\\\\n\\midrule\n\\multicolumn{3}{l}{Average (6-gen LOGO)} & 0.790 \\\\\n\\multicolumn{3}{l}{Average (5-gen, $\\leq$2.8B)} & 0.804 \\\\",
  "new_string": "Pythia-1B       & Pythia & 1.0B & 0.856 \\\\\nPythia-2.8B     & Pythia & 2.8B & 0.804 \\\\\nOLMo-2-1B      & OLMo   & 1.5B & 0.764 \\\\\nQwen3-0.6B     & Qwen   & 0.6B & 0.824 \\\\\nQwen3-1.7B     & Qwen   & 1.7B & 0.805 \\\\\nQwen3-8B       & Qwen   & 8.2B & 0.683 \\\\\n\\midrule\n\\multicolumn{3}{l}{Average (6-gen LOGO)} & 0.789 \\\\\n\\multicolumn{3}{l}{Average (5-gen, $\\leq$2.8B)} & 0.800 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e774609-7b7d-45e9-89f5-027190b753bf",
  "isSidechain": false,
  "requestId": "req_011Cb3mhYkCiVktoyoprsqwS",
  "type": "assistant",
  "uuid": "295781df-73de-4098-addd-e9f9eb15a94f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJqjjrkDFKm5TQBkYrVPoD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4015,
      "cache_read_input_tokens": 100721,
      "output_tokens": 1213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4015,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1213,
          "cache_read_input_tokens": 100721,
          "cache_creation_input_tokens": 4015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4015
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

_source line 300 · 2026-05-15T05:05:11.523Z_

<details><summary>↩ Tool result · `toolu_01EdsusTcUdBVw9Rx22RG9ys`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "295781df-73de-4098-addd-e9f9eb15a94f",
  "isSidechain": false,
  "promptId": "0ffb5ebe-9671-48cd-98cf-674bf708f562",
  "type": "user",
  "uuid": "54f63559-ba6c-4ab3-a2e0-63c22d3032d5",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
    "oldString": "Pythia-1B       & Pythia & 1.0B & 0.855 \\\\\nPythia-2.8B     & Pythia & 2.8B & 0.804 \\\\\nOLMo-2-1B      & OLMo   & 1.5B & 0.762 \\\\\nQwen3-0.6B     & Qwen   & 0.6B & 0.823 \\\\\nQwen3-1.7B     & Qwen   & 1.7B & 0.809 \\\\\nQwen3-8B       & Qwen   & 8.2B & 0.685 \\\\\n\\midrule\n\\multicolumn{3}{l}{Average (6-gen LOGO)} & 0.790 \\\\\n\\multicolumn{3}{l}{Average (5-gen, $\\leq$2.8B)} & 0.804 \\\\",
    "newString": "Pythia-1B       & Pythia & 1.0B & 0.856 \\\\\nPythia-2.8B     & Pythia & 2.8B & 0.804 \\\\\nOLMo-2-1B      & OLMo   & 1.5B & 0.764 \\\\\nQwen3-0.6B     & Qwen   & 0.6B & 0.824 \\\\\nQwen3-1.7B     & Qwen   & 1.7B & 0.805 \\\\\nQwen3-8B       & Qwen   & 8.2B & 0.683 \\\\\n\\midrule\n\\multicolumn{3}{l}{Average (6-gen LOGO)} & 0.789 \\\\\n\\multicolumn{3}{l}{Average (5-gen, $\\leq$2.8B)} & 0.800 \\\\",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 33,
        "oldLines": 15,
        "newStart": 33,
        "newLines": 15,
        "lines": [
          " \\toprule",
          " \\textbf{Generator} & \\textbf{Family} & \\textbf{Params} & \\textbf{Held-out F1} \\\\",
          " \\midrule",
          "-Pythia-1B       & Pythia & 1.0B & 0.855 \\\\",
          "+Pythia-1B       & Pythia & 1.0B & 0.856 \\\\",
          " Pythia-2.8B     & Pythia & 2.8B & 0.804 \\\\",
          "-OLMo-2-1B      & OLMo   & 1.5B & 0.762 \\\\",
          "-Qwen3-0.6B     & Qwen   & 0.6B & 0.823 \\\\",
          "-Qwen3-1.7B     & Qwen   & 1.7B & 0.809 \\\\",
          "-Qwen3-8B       & Qwen   & 8.2B & 0.685 \\\\",
          "+OLMo-2-1B      & OLMo   & 1.5B & 0.764 \\\\",
          "+Qwen3-0.6B     & Qwen   & 0.6B & 0.824 \\\\",
          "+Qwen3-1.7B     & Qwen   & 1.7B & 0.805 \\\\",
          "+Qwen3-8B       & Qwen   & 8.2B & 0.683 \\\\",
          " \\midrule",
          "-\\multicolumn{3}{l}{Average (6-gen LOGO)} & 0.790 \\\\",
          "-\\multicolumn{3}{l}{Average (5-gen, $\\leq$2.8B)} & 0.804 \\\\",
          "+\\multicolumn{3}{l}{Average (6-gen LOGO)} & 0.789 \\\\",
          "+\\multicolumn{3}{l}{Average (5-gen, $\\leq$2.8B)} & 0.800 \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\caption{Leave-one-generator-out macro-F1 for 3-class depth estimation using the 7-feature ensemble. Each row holds out one generator for testing and trains on the remaining five. The 6-gen LOGO average (0.789) includes Qwen3-8B, whose cross-scale transfer gap lowers the mean.}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "295781df-73de-4098-addd-e9f9eb15a94f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 301_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[WORKER DONE] Worker worker_paper_compile-and-audit_20260515T045634 已完成（status=done）。用 `get_worker_status('worker_paper_compile-and-audit_20260515T045634')` 读取结果，然后处理。  - worker_id: worker_paper_compi…",
  "leafUuid": "54f63559-ba6c-4ab3-a2e0-63c22d3032d5",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


### Runtime record

_source line 302_

```json
{
  "type": "ai-title",
  "aiTitle": "Process completed paper writing tables worker",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


### Tool call

_source line 303 · 2026-05-15T05:05:16.999Z_

<details open><summary>🔧 Tool call — Edit · `toolu_013gTraRTDHy4QJNHnUiN1eq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
  "old_string": "drifting features show strong monotonic trends (hapax ratio $\\rho = -0.558$, TTR $\\rho = -0.543$, entropy mean $\\rho = -0.476$),\nwhile shape features show weak or negligible correlations (entropy std $|\\rho| = 0.076$, tail decay $|\\rho| = 0.087$).",
  "new_string": "drifting features show strong monotonic trends (hapax ratio $\\rho = -0.558$, TTR $\\rho = -0.542$, entropy mean $\\rho = -0.475$),\nwhile shape features show weak or negligible correlations (entropy std $|\\rho| = 0.076$, tail decay $|\\rho| = 0.089$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54f63559-ba6c-4ab3-a2e0-63c22d3032d5",
  "isSidechain": false,
  "requestId": "req_011Cb3migCCSLkSWnAb15PVq",
  "type": "assistant",
  "uuid": "78068511-a576-415c-855d-dee6cdcf32b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fgB2Pp6mkbHjaJ4ZiVeR8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 104736,
      "output_tokens": 857,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 857,
          "cache_read_input_tokens": 104736,
          "cache_creation_input_tokens": 1427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1427
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

_source line 304 · 2026-05-15T05:05:17.009Z_

<details><summary>↩ Tool result · `toolu_013gTraRTDHy4QJNHnUiN1eq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78068511-a576-415c-855d-dee6cdcf32b8",
  "isSidechain": false,
  "promptId": "0ffb5ebe-9671-48cd-98cf-674bf708f562",
  "type": "user",
  "uuid": "0f239b0a-f195-4167-9f5a-17b832dcb69a",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
    "oldString": "drifting features show strong monotonic trends (hapax ratio $\\rho = -0.558$, TTR $\\rho = -0.543$, entropy mean $\\rho = -0.476$),\nwhile shape features show weak or negligible correlations (entropy std $|\\rho| = 0.076$, tail decay $|\\rho| = 0.087$).",
    "newString": "drifting features show strong monotonic trends (hapax ratio $\\rho = -0.558$, TTR $\\rho = -0.542$, entropy mean $\\rho = -0.475$),\nwhile shape features show weak or negligible correlations (entropy std $|\\rho| = 0.076$, tail decay $|\\rho| = 0.089$).",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 63,
        "oldLines": 8,
        "newStart": 63,
        "newLines": 8,
        "lines": [
          " \\end{figure}",
          " ",
          " Individual-level Spearman correlations with depth confirm the split (Figure~\\ref{fig:feature-drift}):",
          "-drifting features show strong monotonic trends (hapax ratio $\\rho = -0.558$, TTR $\\rho = -0.543$, entropy mean $\\rho = -0.476$),",
          "-while shape features show weak or negligible correlations (entropy std $|\\rho| = 0.076$, tail decay $|\\rho| = 0.087$).",
          "+drifting features show strong monotonic trends (hapax ratio $\\rho = -0.558$, TTR $\\rho = -0.542$, entropy mean $\\rho = -0.475$),",
          "+while shape features show weak or negligible correlations (entropy std $|\\rho| = 0.076$, tail decay $|\\rho| = 0.089$).",
          " ",
          " \\paragraph{Feature complementarity.}",
          " Table~\\ref{tab:ablation} reports ablation results."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "78068511-a576-415c-855d-dee6cdcf32b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 305 · 2026-05-15T05:05:19.336Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Tw89X6WADYqdrQVbaUwEQi`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
  "old_string": "The full 7-feature set (F1\\,=\\,0.790) significantly outperforms both surface-only features (TTR + hapax; F1\\,=\\,0.729) and reference-only features (entropy statistics + tail decay; F1\\,=\\,0.745; McNemar $p \\approx 0$).\nPermutation importance ranks hapax ratio highest (0.271), followed by TTR (0.165) and entropy mean (0.156).",
  "new_string": "The full 7-feature set (F1\\,=\\,0.789) significantly outperforms both surface-only features (TTR + hapax; F1\\,=\\,0.729) and reference-only features (entropy statistics + tail decay; F1\\,=\\,0.745; McNemar $p \\approx 0$).\nPermutation importance ranks hapax ratio highest (0.269), followed by entropy mean (0.164) and TTR (0.159)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f239b0a-f195-4167-9f5a-17b832dcb69a",
  "isSidechain": false,
  "requestId": "req_011Cb3migCCSLkSWnAb15PVq",
  "type": "assistant",
  "uuid": "fd6e3e99-43b0-43d0-98b5-3a94299bc84f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fgB2Pp6mkbHjaJ4ZiVeR8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 104736,
      "output_tokens": 857,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 857,
          "cache_read_input_tokens": 104736,
          "cache_creation_input_tokens": 1427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1427
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

_source line 306 · 2026-05-15T05:05:20.792Z_

<details><summary>↩ Tool result · `toolu_016muE77Fo3HowmNsAacKufV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d46164a7-4e68-4ffc-9773-1faff9eb7e91",
  "isSidechain": false,
  "promptId": "0ffb5ebe-9671-48cd-98cf-674bf708f562",
  "type": "user",
  "uuid": "cbc9b6dc-4c7a-45b3-a37e-2a7fe4be63f3",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
    "oldString": "Full (7 features)     & 0.790 & hapax\\_ratio (0.271) \\\\",
    "newString": "Full (7 features)     & 0.789 & hapax\\_ratio (0.269) \\\\",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 85,
        "oldLines": 7,
        "newStart": 85,
        "newLines": 7,
        "lines": [
          " \\toprule",
          " \\textbf{Feature set} & \\textbf{LOGO F1} & \\textbf{Top feature (importance)} \\\\",
          " \\midrule",
          "-Full (7 features)     & 0.790 & hapax\\_ratio (0.271) \\\\",
          "+Full (7 features)     & 0.789 & hapax\\_ratio (0.269) \\\\",
          " Surface only (2)      & 0.729 & hapax\\_ratio (0.320) \\\\",
          " Reference only (5)    & 0.745 & entropy\\_mean (0.218) \\\\",
          " \\bottomrule"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "d46164a7-4e68-4ffc-9773-1faff9eb7e91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-15T05:05:19.344Z_

<details><summary>↩ Tool result · `toolu_01Tw89X6WADYqdrQVbaUwEQi`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd6e3e99-43b0-43d0-98b5-3a94299bc84f",
  "isSidechain": false,
  "promptId": "0ffb5ebe-9671-48cd-98cf-674bf708f562",
  "type": "user",
  "uuid": "3aed5912-c05e-4a97-bdae-931f9d7a3f60",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
    "oldString": "The full 7-feature set (F1\\,=\\,0.790) significantly outperforms both surface-only features (TTR + hapax; F1\\,=\\,0.729) and reference-only features (entropy statistics + tail decay; F1\\,=\\,0.745; McNemar $p \\approx 0$).\nPermutation importance ranks hapax ratio highest (0.271), followed by TTR (0.165) and entropy mean (0.156).",
    "newString": "The full 7-feature set (F1\\,=\\,0.789) significantly outperforms both surface-only features (TTR + hapax; F1\\,=\\,0.729) and reference-only features (entropy statistics + tail decay; F1\\,=\\,0.745; McNemar $p \\approx 0$).\nPermutation importance ranks hapax ratio highest (0.269), followed by entropy mean (0.164) and TTR (0.159).",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 68,
        "oldLines": 8,
        "newStart": 68,
        "newLines": 8,
        "lines": [
          " ",
          " \\paragraph{Feature complementarity.}",
          " Table~\\ref{tab:ablation} reports ablation results.",
          "-The full 7-feature set (F1\\,=\\,0.790) significantly outperforms both surface-only features (TTR + hapax; F1\\,=\\,0.729) and reference-only features (entropy statistics + tail decay; F1\\,=\\,0.745; McNemar $p \\approx 0$).",
          "-Permutation importance ranks hapax ratio highest (0.271), followed by TTR (0.165) and entropy mean (0.156).",
          "+The full 7-feature set (F1\\,=\\,0.789) significantly outperforms both surface-only features (TTR + hapax; F1\\,=\\,0.729) and reference-only features (entropy statistics + tail decay; F1\\,=\\,0.745; McNemar $p \\approx 0$).",
          "+Permutation importance ranks hapax ratio highest (0.269), followed by entropy mean (0.164) and TTR (0.159).",
          " Surface features capture vocabulary impoverishment; reference features capture distributional shift---neither subsumes the other.",
          " ",
          " \\paragraph{Cross-family reference models.}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "fd6e3e99-43b0-43d0-98b5-3a94299bc84f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-15T05:05:20.755Z_

<details open><summary>🔧 Tool call — Edit · `toolu_016muE77Fo3HowmNsAacKufV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
  "old_string": "Full (7 features)     & 0.790 & hapax\\_ratio (0.271) \\\\",
  "new_string": "Full (7 features)     & 0.789 & hapax\\_ratio (0.269) \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3aed5912-c05e-4a97-bdae-931f9d7a3f60",
  "isSidechain": false,
  "requestId": "req_011Cb3migCCSLkSWnAb15PVq",
  "type": "assistant",
  "uuid": "d46164a7-4e68-4ffc-9773-1faff9eb7e91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fgB2Pp6mkbHjaJ4ZiVeR8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1427,
      "cache_read_input_tokens": 104736,
      "output_tokens": 857,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 857,
          "cache_read_input_tokens": 104736,
          "cache_creation_input_tokens": 1427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1427
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


### Assistant

_source line 309 · 2026-05-15T05:05:24.188Z_

修正 introduction.tex 的 per-generator range。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbc9b6dc-4c7a-45b3-a37e-2a7fe4be63f3",
  "isSidechain": false,
  "requestId": "req_011Cb3mjMwNVqdpCKfL4T5kD",
  "type": "assistant",
  "uuid": "0466b377-d737-406a-8163-9a9073a9236e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuYhnJweFDLW3XbeR5zDi9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 106163,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 106163,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1071
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


### Tool call

_source line 310 · 2026-05-15T05:05:24.680Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Konvds4QBJbdi7VurgbidV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
  "offset": 22,
  "limit": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0466b377-d737-406a-8163-9a9073a9236e",
  "isSidechain": false,
  "requestId": "req_011Cb3mjMwNVqdpCKfL4T5kD",
  "type": "assistant",
  "uuid": "f3d60b11-6977-4109-b791-979aead8a12b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuYhnJweFDLW3XbeR5zDi9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 106163,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1071,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 106163,
          "cache_creation_input_tokens": 1071,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1071
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

_source line 311 · 2026-05-15T05:05:24.688Z_

<details><summary>↩ Tool result · `toolu_01Konvds4QBJbdi7VurgbidV`</summary>

```text
22	This pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.
23	The combination of drifting and stationary features yields a 7-feature ensemble that achieves leave-one-generator-out (LOGO) macro-F1 of 0.79, with per-generator held-out F1 ranging from 0.68 to 0.86.
24	This ensemble maintains tight cross-generator consistency (CI width 1.3\,pp), whereas the best single detector spans over 20\,pp.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3d60b11-6977-4109-b791-979aead8a12b",
  "isSidechain": false,
  "promptId": "0ffb5ebe-9671-48cd-98cf-674bf708f562",
  "type": "user",
  "uuid": "f8b91e00-bae2-4fae-a42d-4cda001b39cb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
      "content": "This pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves leave-one-generator-out (LOGO) macro-F1 of 0.79, with per-generator held-out F1 ranging from 0.68 to 0.86.\nThis ensemble maintains tight cross-generator consistency (CI width 1.3\\,pp), whereas the best single detector spans over 20\\,pp.",
      "numLines": 3,
      "startLine": 22,
      "totalLines": 43
    }
  },
  "sourceToolAssistantUUID": "f3d60b11-6977-4109-b791-979aead8a12b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 312 · 2026-05-15T05:05:32.296Z_

<details><summary>Logged reasoning block</summary>

```text
Line 23 already says "0.68 to 0.86" — the integrate-and-compile worker must have fixed it. Previously the audit said it was "0.69 to 0.85". Let me check the rest of the file for any remaining issues. Let me also verify the introduction has correct numbers throughout.

Actually, let me also check line 23 more carefully: "macro-F1 of 0.79" — registry says 0.7893 which rounds to 0.79 at 2 decimal places. Good.

The introduction also references `\textit{plan-014}` and `\textit{plan-015}` and `\textit{plan-004-v2}` — these are internal experiment IDs that should NOT be in the final paper. 

That's something I need to flag separately, but let me scan through the rest of the document more carefully first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8b91e00-bae2-4fae-a42d-4cda001b39cb",
  "isSidechain": false,
  "requestId": "req_011Cb3mjejRTgozPr8k4RmnE",
  "type": "assistant",
  "uuid": "84a96114-4a68-419a-8af0-857ec5184a1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGAt8EuRd5Px8zSkH9RtUx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 107234,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 451,
          "cache_read_input_tokens": 107234,
          "cache_creation_input_tokens": 292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 292
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


### Assistant

_source line 313 · 2026-05-15T05:05:33.321Z_

Introduction 第23行已是 "0.68 to 0.86"（已被 integrate worker 修正）。但注意到 introduction 中有内部实验 ID 引用（plan-014, plan-015, plan-004-v2），这些需要在提交前移除。先检查还有哪些地方引用了内部 ID。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84a96114-4a68-419a-8af0-857ec5184a1a",
  "isSidechain": false,
  "requestId": "req_011Cb3mjejRTgozPr8k4RmnE",
  "type": "assistant",
  "uuid": "c5e844bd-a8b9-40b9-afc7-0faf2a82d91d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGAt8EuRd5Px8zSkH9RtUx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 107234,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 451,
          "cache_read_input_tokens": 107234,
          "cache_creation_input_tokens": 292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 292
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


### Tool call

_source line 314 · 2026-05-15T05:05:34.056Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01UHa3DsGhBFeMQkvJnapz8E`</summary>

```json
{
  "pattern": "plan-\\d+",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5e844bd-a8b9-40b9-afc7-0faf2a82d91d",
  "isSidechain": false,
  "requestId": "req_011Cb3mjejRTgozPr8k4RmnE",
  "type": "assistant",
  "uuid": "6e34588d-528c-4950-844b-40b4566b49b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CGAt8EuRd5Px8zSkH9RtUx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 107234,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 451,
          "cache_read_input_tokens": 107234,
          "cache_creation_input_tokens": 292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 292
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

_source line 315 · 2026-05-15T05:05:34.079Z_

<details><summary>↩ Tool result · `toolu_01UHa3DsGhBFeMQkvJnapz8E`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e34588d-528c-4950-844b-40b4566b49b2",
  "isSidechain": false,
  "promptId": "0ffb5ebe-9671-48cd-98cf-674bf708f562",
  "type": "user",
  "uuid": "30f32f46-e299-4844-85d2-2b7700ccb326",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "6e34588d-528c-4950-844b-40b4566b49b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 316 · 2026-05-15T05:05:34.109Z_

```json
{
  "parentUuid": "30f32f46-e299-4844-85d2-2b7700ccb326",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "167a3727-f876-49ed-8de4-741685d7e2f9",
  "timestamp": "2026-05-15T05:05:34.109Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 317 · 2026-05-15T05:05:37.998Z_

<details><summary>Logged reasoning block</summary>

```text
Good, no plan-* references in the .tex files. The integrate worker or consistency worker must have cleaned them up. Let me verify the introduction.tex doesn't have them either.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "167a3727-f876-49ed-8de4-741685d7e2f9",
  "isSidechain": false,
  "requestId": "req_011Cb3mkLkU61rA5mxZ7G4c1",
  "type": "assistant",
  "uuid": "c2055942-2511-45f0-ab9b-b522959d858d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVXodqZqmZSnaXwdJfS4SS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 569,
      "cache_read_input_tokens": 107526,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 107526,
          "cache_creation_input_tokens": 569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 569
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


### Tool call

_source line 318 · 2026-05-15T05:05:39.532Z_

<details open><summary>🔧 Tool call — Grep · `toolu_013aiCdjR9vXMumyr89a8Lbi`</summary>

```json
{
  "pattern": "plan[-_]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2055942-2511-45f0-ab9b-b522959d858d",
  "isSidechain": false,
  "requestId": "req_011Cb3mkLkU61rA5mxZ7G4c1",
  "type": "assistant",
  "uuid": "0806b061-761f-4f12-8df7-10f8c7f9390a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVXodqZqmZSnaXwdJfS4SS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 569,
      "cache_read_input_tokens": 107526,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 195,
          "cache_read_input_tokens": 107526,
          "cache_creation_input_tokens": 569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 569
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

_source line 319 · 2026-05-15T05:05:39.545Z_

<details><summary>↩ Tool result · `toolu_013aiCdjR9vXMumyr89a8Lbi`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0806b061-761f-4f12-8df7-10f8c7f9390a",
  "isSidechain": false,
  "promptId": "0ffb5ebe-9671-48cd-98cf-674bf708f562",
  "type": "user",
  "uuid": "0159fb4f-d037-4b69-8e43-4932ac6eafb5",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "0806b061-761f-4f12-8df7-10f8c7f9390a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 320 · 2026-05-15T05:05:43.454Z_

内部 ID 已被清除。向 Director 汇报审计修正结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0159fb4f-d037-4b69-8e43-4932ac6eafb5",
  "isSidechain": false,
  "requestId": "req_011Cb3mkkUE7VMiHx8izK2qh",
  "type": "assistant",
  "uuid": "2c4270e3-d0e1-4522-96d0-e7d6469b72e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JUq7XqY98eg319864wzYz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 210,
      "cache_read_input_tokens": 108095,
      "output_tokens": 565,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 210,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 565,
          "cache_read_input_tokens": 108095,
          "cache_creation_input_tokens": 210,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 210
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


### Tool call

_source line 321 · 2026-05-15T05:05:54.148Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director · `toolu_01BMNsZ1HrADeh5TZx2YtNmM`</summary>

```json
{
  "text": "[资源] GPU 分配 4 / 实际跑 3 (cuda:1-3 plan-005) | Worker 池 1 (GPU 0 / CPU 1: consistency-fixes)\n\n**数字审计 + 修正完成：**\n\n已修正 results.tex 中 8 处数字不一致（全部对齐到 registry plan-014）：\n- **LOGO 表**: Pythia-1B 0.855→0.856, OLMo 0.762→0.764, Qwen3-0.6B 0.823→0.824, Qwen3-1.7B 0.809→0.805, Qwen3-8B 0.685→0.683, avg 0.790→0.789, 5-gen 0.804→0.800\n- **Spearman**: TTR -0.543→-0.542, entropy_mean -0.476→-0.475, tail_decay 0.087→0.089\n- **Feature importance**: hapax 0.271→0.269, 排序修正 entropy_mean(0.164) > TTR(0.159)\n- **Ablation 文本+表**: Full F1 0.790→0.789\n\n其他 Worker 已完成的修正：\n- integrate worker: F1 0.790→0.789 (line 11), caption 修正, fig 环境添加, introduction range 已正确 (0.68-0.86)\n- 内部实验 ID (plan-*) 已从所有 .tex 文件中清除\n\n**编译状态**: 零错误、零 undefined refs, 11 页\n\n**仍在运行**: consistency-fixes worker (1), plan-005 cuda:1-3",
  "project": "gen-depth-fingerprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c4270e3-d0e1-4522-96d0-e7d6469b72e6",
  "isSidechain": false,
  "requestId": "req_011Cb3mkkUE7VMiHx8izK2qh",
  "type": "assistant",
  "uuid": "a6946392-f6b1-4a8a-b421-3ee81dcf862f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018JUq7XqY98eg319864wzYz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 210,
      "cache_read_input_tokens": 108095,
      "output_tokens": 565,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 210,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 565,
          "cache_read_input_tokens": 108095,
          "cache_creation_input_tokens": 210,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 210
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


### Runtime record

_source line 322_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[WORKER DONE] Worker worker_paper_compile-and-audit_20260515T045634 已完成（status=done）。用 `get_worker_status('worker_paper_compile-and-audit_20260515T045634')` 读取结果，然后处理。  - worker_id: worker_paper_compi…",
  "leafUuid": "a6946392-f6b1-4a8a-b421-3ee81dcf862f",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


### Runtime record

_source line 323_

```json
{
  "type": "ai-title",
  "aiTitle": "Process completed paper writing tables worker",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


### Tool result

_source line 324 · 2026-05-15T05:05:57.737Z_

<details><summary>↩ Tool result · `toolu_01BMNsZ1HrADeh5TZx2YtNmM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6946392-f6b1-4a8a-b421-3ee81dcf862f",
  "isSidechain": false,
  "promptId": "0ffb5ebe-9671-48cd-98cf-674bf708f562",
  "type": "user",
  "uuid": "b49e00e7-2ed3-4460-ae4f-b8e14f976ed2",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_dbd68d7879a81efc0c108e9844b15d0b:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "a6946392-f6b1-4a8a-b421-3ee81dcf862f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 325_

```json
{
  "type": "ai-title",
  "aiTitle": "Process completed paper writing tables worker",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


### Runtime record

_source line 326 · 2026-05-15T05:06:30.205Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T05:06:30.205Z",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "content": "[WORKER DONE] Worker worker_paper_consistency-fixes_20260515T045751 已完成（status=done）。用 `get_worker_status('worker_paper_consistency-fixes_20260515T045751')` 读取结果，然后处理。\n\n- worker_id: worker_paper_consistency-fixes_20260515T045751\n- project: gen-depth-fingerprint\n- status: done"
}
```

---


### Runtime record

_source line 327 · 2026-05-15T05:06:30.206Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T05:06:30.206Z",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


## Round 17

## Round 17

2 recorded events


### User

_source line 328 · 2026-05-15T05:06:30.194Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b49e00e7-2ed3-4460-ae4f-b8e14f976ed2",
  "isSidechain": false,
  "promptId": "d7663afc-402f-4d31-bc13-b0c432bd139f",
  "type": "user",
  "isMeta": true,
  "uuid": "6d0c2a89-fe48-4098-a207-bf46ab939cd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 329 · 2026-05-15T05:06:30.194Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d0c2a89-fe48-4098-a207-bf46ab939cd1",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "73626c97-a877-4860-9cc0-da413fcfac6a",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "b3bec4be-b7cd-42f6-b2e2-e18115270a76",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 18

## Round 18

40 recorded events


### User

_source line 330 · 2026-05-15T05:06:30.307Z_

[WORKER DONE] Worker worker_paper_consistency-fixes_20260515T045751 已完成（status=done）。用 `get_worker_status('worker_paper_consistency-fixes_20260515T045751')` 读取结果，然后处理。

- worker_id: worker_paper_consistency-fixes_20260515T045751
- project: gen-depth-fingerprint
- status: done

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73626c97-a877-4860-9cc0-da413fcfac6a",
  "isSidechain": false,
  "promptId": "d7663afc-402f-4d31-bc13-b0c432bd139f",
  "type": "user",
  "uuid": "d24d4d92-24a2-4abb-9f6c-8fabde3a4db1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 331 · 2026-05-15T05:06:35.619Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_016BMEupehmrSCufZdZJSyQP`</summary>

```json
{
  "worker_id": "worker_paper_consistency-fixes_20260515T045751"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d24d4d92-24a2-4abb-9f6c-8fabde3a4db1",
  "isSidechain": false,
  "requestId": "req_011Cb3mpeJ1p1gUQeriWXDzK",
  "type": "assistant",
  "uuid": "01f81315-e6ed-46a8-8ab0-0630c85dc80f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dear7TdcUqViLGwEEr2hDo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 122,
      "cache_read_input_tokens": 108945,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 122,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 108945,
          "cache_creation_input_tokens": 122,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 122
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

_source line 332 · 2026-05-15T05:06:35.660Z_

<details><summary>↩ Tool result · `toolu_016BMEupehmrSCufZdZJSyQP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_consistency-fixes_20260515T045751\", \"status\": \"done\", \"task_type\": \"paper:consistency-fixes\", \"project\": \"gen-depth-fingerprint\", \"started_at\": \"2026-05-15T04:57:51.551624+00:00\", \"ended_at\": \"2026-05-15T05:06:26.687462+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"全部修复完成。共修改 16 个文件，修复报告已写入 `consistency_fixes_report.md`。\\n\\n**修复总结：**\\n- **Fix 1 (CI 区间)**: 从所有 6-gen 上下文删除 [0.786, 0.799]，仅保留在 5-gen baselines 表格中（已标注 \\\"5-gen LOGO\\\"）\\n- **Fix 2 (实验 ID)**: 删除全部 `plan-014`、`plan-015`、`plan-004-v2` 共 16 处\\n- **Fix 3 (Binoculars)**: 5 个文件中 `0.59--0.82` → `0.41--0.82`\\n- **Fix 4 (6-gen 主线)**: ablation 句中 `macro-F1=0.80` → `0.79`，held-out 范围统一为 `0.68 to 0.86`\"}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01f81315-e6ed-46a8-8ab0-0630c85dc80f",
  "isSidechain": false,
  "promptId": "d7663afc-402f-4d31-bc13-b0c432bd139f",
  "type": "user",
  "uuid": "238ea940-8b80-456a-a7c5-b1da0d7b3706",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_consistency-fixes_20260515T045751\\\", \\\"status\\\": \\\"done\\\", \\\"task_type\\\": \\\"paper:consistency-fixes\\\", \\\"project\\\": \\\"gen-depth-fingerprint\\\", \\\"started_at\\\": \\\"2026-05-15T04:57:51.551624+00:00\\\", \\\"ended_at\\\": \\\"2026-05-15T05:06:26.687462+00:00\\\", \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}, \\\"result\\\": {\\\"raw\\\": \\\"全部修复完成。共修改 16 个文件，修复报告已写入 `consistency_fixes_report.md`。\\\\n\\\\n**修复总结：**\\\\n- **Fix 1 (CI 区间)**: 从所有 6-gen 上下文删除 [0.786, 0.799]，仅保留在 5-gen baselines 表格中（已标注 \\\\\\\"5-gen LOGO\\\\\\\"）\\\\n- **Fix 2 (实验 ID)**: 删除全部 `plan-014`、`plan-015`、`plan-004-v2` 共 16 处\\\\n- **Fix 3 (Binoculars)**: 5 个文件中 `0.59--0.82` → `0.41--0.82`\\\\n- **Fix 4 (6-gen 主线)**: ablation 句中 `macro-F1=0.80` → `0.79`，held-out 范围统一为 `0.68 to 0.86`\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_consistency-fixes_20260515T045751\", \"status\": \"done\", \"task_type\": \"paper:consistency-fixes\", \"project\": \"gen-depth-fingerprint\", \"started_at\": \"2026-05-15T04:57:51.551624+00:00\", \"ended_at\": \"2026-05-15T05:06:26.687462+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"全部修复完成。共修改 16 个文件，修复报告已写入 `consistency_fixes_report.md`。\\n\\n**修复总结：**\\n- **Fix 1 (CI 区间)**: 从所有 6-gen 上下文删除 [0.786, 0.799]，仅保留在 5-gen baselines 表格中（已标注 \\\"5-gen LOGO\\\"）\\n- **Fix 2 (实验 ID)**: 删除全部 `plan-014`、`plan-015`、`plan-004-v2` 共 16 处\\n- **Fix 3 (Binoculars)**: 5 个文件中 `0.59--0.82` → `0.41--0.82`\\n- **Fix 4 (6-gen 主线)**: ablation 句中 `macro-F1=0.80` → `0.79`，held-out 范围统一为 `0.68 to 0.86`\"}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "01f81315-e6ed-46a8-8ab0-0630c85dc80f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 333 · 2026-05-15T05:06:43.553Z_

<details><summary>Logged reasoning block</summary>

```text
The consistency-fixes worker completed with 16 file modifications. Key fixes:
1. CI interval [0.786, 0.799] removed from 6-gen contexts (only kept in 5-gen baselines table)
2. All internal experiment IDs removed (16 occurrences)
3. Binoculars CI range corrected: 0.59-0.82 → 0.41-0.82
4. 6-gen ablation F1 corrected: 0.80 → 0.79, held-out range unified to 0.68-0.86


5. Now I need to verify the compilation still works after these changes, check the worker pool status since nothing's currently running, and report back on the overall status.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "238ea940-8b80-456a-a7c5-b1da0d7b3706",
  "isSidechain": false,
  "requestId": "req_011Cb3mpt1mVS5UtwNtdR4iL",
  "type": "assistant",
  "uuid": "218d6453-076c-4cef-bc4d-a3da7dbd5100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QsFqBW7gr82T6vTgbVgqCF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 538,
      "cache_read_input_tokens": 109067,
      "output_tokens": 579,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 538,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 579,
          "cache_read_input_tokens": 109067,
          "cache_creation_input_tokens": 538,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 538
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


### Assistant

_source line 334 · 2026-05-15T05:06:43.558Z_

Consistency-fixes worker 完成了 16 处修复。验证编译是否仍然通过。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "218d6453-076c-4cef-bc4d-a3da7dbd5100",
  "isSidechain": false,
  "requestId": "req_011Cb3mpt1mVS5UtwNtdR4iL",
  "type": "assistant",
  "uuid": "f1dafe58-055d-4a91-95d4-a862f6408458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QsFqBW7gr82T6vTgbVgqCF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 538,
      "cache_read_input_tokens": 109067,
      "output_tokens": 579,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 538,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 579,
          "cache_read_input_tokens": 109067,
          "cache_creation_input_tokens": 538,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 538
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


### Tool call

_source line 335 · 2026-05-15T05:06:45.502Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012WHcg7nu6RyemkT7YNUHME`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"(Error|!|Output written)\" && bibtex main 2>&1 | grep -E \"(Error|Warning|Database)\" && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"(Error|Output written)\" && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"(Error|undefined|Output written)\"",
  "description": "Full LaTeX rebuild after consistency fixes",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1dafe58-055d-4a91-95d4-a862f6408458",
  "isSidechain": false,
  "requestId": "req_011Cb3mpt1mVS5UtwNtdR4iL",
  "type": "assistant",
  "uuid": "297238bd-be8e-4193-8974-0519e001fdd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QsFqBW7gr82T6vTgbVgqCF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 538,
      "cache_read_input_tokens": 109067,
      "output_tokens": 579,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 538,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 579,
          "cache_read_input_tokens": 109067,
          "cache_creation_input_tokens": 538,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 538
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


### Tool call

_source line 336 · 2026-05-15T05:06:45.672Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers · `toolu_0124hcEcTyEsQqhiLwUegxTG`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "297238bd-be8e-4193-8974-0519e001fdd7",
  "isSidechain": false,
  "requestId": "req_011Cb3mpt1mVS5UtwNtdR4iL",
  "type": "assistant",
  "uuid": "3b5cb471-78be-4b99-a8dd-f44be8854922",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QsFqBW7gr82T6vTgbVgqCF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 538,
      "cache_read_input_tokens": 109067,
      "output_tokens": 579,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 538,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 579,
          "cache_read_input_tokens": 109067,
          "cache_creation_input_tokens": 538,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 538
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

_source line 337 · 2026-05-15T05:06:47.920Z_

<details><summary>↩ Tool result · `toolu_012WHcg7nu6RyemkT7YNUHME`</summary>

```text
Output written on main.pdf (11 pages, 324698 bytes).
Database file #1: references.bib
Output written on main.pdf (11 pages, 324674 bytes).
Output written on main.pdf (11 pages, 324674 bytes).
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "297238bd-be8e-4193-8974-0519e001fdd7",
  "isSidechain": false,
  "promptId": "d7663afc-402f-4d31-bc13-b0c432bd139f",
  "type": "user",
  "uuid": "71e0b55f-670d-4db4-9334-0ecc10896865",
  "toolUseResult": {
    "stdout": "Output written on main.pdf (11 pages, 324698 bytes).\nDatabase file #1: references.bib\nOutput written on main.pdf (11 pages, 324674 bytes).\nOutput written on main.pdf (11 pages, 324674 bytes).",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "297238bd-be8e-4193-8974-0519e001fdd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 338 · 2026-05-15T05:06:47.959Z_

<details><summary>↩ Tool result · `toolu_0124hcEcTyEsQqhiLwUegxTG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b5cb471-78be-4b99-a8dd-f44be8854922",
  "isSidechain": false,
  "promptId": "d7663afc-402f-4d31-bc13-b0c432bd139f",
  "type": "user",
  "uuid": "e5c97556-7668-49a4-8671-06cb8129dfb5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"workers\\\": [], \\\"count\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "3b5cb471-78be-4b99-a8dd-f44be8854922",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 339 · 2026-05-15T05:06:53.574Z_

编译通过，零错误，11 页 PDF。Worker 池为 0，需要补充。

当前状态：plan-005 在 cuda:1-3 运行（~35%，ETA ~1.5h），论文初稿编译通过。可以派 Worker 做论文视觉审查（检查图表渲染质量、页面布局）和引用审计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5c97556-7668-49a4-8671-06cb8129dfb5",
  "isSidechain": false,
  "requestId": "req_011Cb3mqnZP1Hdfxay1hGhTw",
  "type": "assistant",
  "uuid": "e6d7ffd5-a7f2-4fb0-8e23-807cf9531375",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MvuZrQjoFNXgrqtyFZv8Jq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 109605,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 797,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 109605,
          "cache_creation_input_tokens": 797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 797
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


### Tool call

_source line 340 · 2026-05-15T05:06:53.899Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HpTEqPaMctXDXPxmW44dwC`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e6d7ffd5-a7f2-4fb0-8e23-807cf9531375",
  "isSidechain": false,
  "requestId": "req_011Cb3mqnZP1Hdfxay1hGhTw",
  "type": "assistant",
  "uuid": "b7214253-b599-42dc-b041-51742d3533fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MvuZrQjoFNXgrqtyFZv8Jq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 109605,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 797,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 109605,
          "cache_creation_input_tokens": 797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 797
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

_source line 341 · 2026-05-15T05:06:53.902Z_

<details><summary>↩ Tool result · `toolu_01HpTEqPaMctXDXPxmW44dwC`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__pdf_to_images"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7214253-b599-42dc-b041-51742d3533fc",
  "isSidechain": false,
  "promptId": "d7663afc-402f-4d31-bc13-b0c432bd139f",
  "type": "user",
  "uuid": "00309982-84f4-461b-bcfb-df4d38de2189",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__pdf_to_images"
    ],
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "total_deferred_tools": 79
  },
  "sourceToolAssistantUUID": "b7214253-b599-42dc-b041-51742d3533fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 342 · 2026-05-15T05:06:53.958Z_

```json
{
  "parentUuid": "00309982-84f4-461b-bcfb-df4d38de2189",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "b03e26b9-0ef8-461f-adce-618891e6bcdb",
  "timestamp": "2026-05-15T05:06:53.958Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 343 · 2026-05-15T05:07:01.759Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do a visual review of the PDF myself rather than spawning a worker for it, since I have the pdf_to_images tool available. I'll render the key pages and check the layout. Also, I should spawn workers for other tasks to keep the worker pool at ≥2.

Let me:
1. Render the PDF for visual inspection
2. Spawn a worker for reference audit (checking bib entries)

Actually, let me think about what tasks are worth spawning workers for right now:
- Reference/citation audit (bib integrity) - good CPU task
- Page count / format compliance check (EMNLP limit is 8 pages + unlimited refs/appendix)


I'll start by rendering the PDF pages to visually inspect the layout while spinning up a worker to audit the references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b03e26b9-0ef8-461f-adce-618891e6bcdb",
  "isSidechain": false,
  "requestId": "req_011Cb3mrE8md8saeaeeXsg92",
  "type": "assistant",
  "uuid": "7dfddbb8-2864-4d2c-89a1-fa8ea4288064",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GkfVutgT5JiPzSLM9hh7sg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 671,
      "cache_read_input_tokens": 110402,
      "output_tokens": 1005,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1005,
          "cache_read_input_tokens": 110402,
          "cache_creation_input_tokens": 671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 671
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


### Assistant

_source line 344 · 2026-05-15T05:07:01.760Z_

渲染 PDF 做视觉检查，同时派 Worker 做引用审计。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dfddbb8-2864-4d2c-89a1-fa8ea4288064",
  "isSidechain": false,
  "requestId": "req_011Cb3mrE8md8saeaeeXsg92",
  "type": "assistant",
  "uuid": "2ab84215-7d4b-4f9d-8d0c-4ab00101bad8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GkfVutgT5JiPzSLM9hh7sg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 671,
      "cache_read_input_tokens": 110402,
      "output_tokens": 1005,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1005,
          "cache_read_input_tokens": 110402,
          "cache_creation_input_tokens": 671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 671
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


### Tool call

_source line 345 · 2026-05-15T05:07:02.678Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01KNz1VGGyUMbEMMqy1mT1Fc`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf",
  "pages": "1-6",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ab84215-7d4b-4f9d-8d0c-4ab00101bad8",
  "isSidechain": false,
  "requestId": "req_011Cb3mrE8md8saeaeeXsg92",
  "type": "assistant",
  "uuid": "b313cd6c-4699-4524-b9df-7de31d599af2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GkfVutgT5JiPzSLM9hh7sg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 671,
      "cache_read_input_tokens": 110402,
      "output_tokens": 1005,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1005,
          "cache_read_input_tokens": 110402,
          "cache_creation_input_tokens": 671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 671
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

_source line 346 · 2026-05-15T05:07:04.430Z_

<details><summary>↩ Tool result · `toolu_01KNz1VGGyUMbEMMqy1mT1Fc`</summary>

```text
Error: result (3,930,294 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/cc34e79c-0750-433b-82e8-2f9b3761bd2e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821624409.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/cc34e79c-0750-433b-82e8-2f9b3761bd2e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821624409.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/cc34e79c-0750-433b-82e8-2f9b3761bd2e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821624409.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b313cd6c-4699-4524-b9df-7de31d599af2",
  "isSidechain": false,
  "promptId": "d7663afc-402f-4d31-bc13-b0c432bd139f",
  "type": "user",
  "uuid": "d8abba94-5b90-4c54-b669-e7f3e21d9480",
  "toolUseResult": "Error: result (3,930,294 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/cc34e79c-0750-433b-82e8-2f9b3761bd2e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821624409.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/cc34e79c-0750-433b-82e8-2f9b3761bd2e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821624409.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/cc34e79c-0750-433b-82e8-2f9b3761bd2e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821624409.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 346,
    "serialized_bytes": 3930331,
    "serialized_sha256": "5e7fd98beaf3aea86680cb8ede795035ad3622be6d5313968629e2ae8f69b485",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "b313cd6c-4699-4524-b9df-7de31d599af2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 347 · 2026-05-15T05:07:12.588Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker · `toolu_016CMzaj2iPJoH5mbX6LecbK`</summary>

````json
{
  "task_type": "paper:reference-audit",
  "project": "gen-depth-fingerprint",
  "task_prompt": "## 任务：引用审计\n\n### 目标\n检查论文的 references.bib 中所有条目的完整性和正确性。\n\n### 步骤\n\n1. 读取 `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib`\n2. 读取所有 .tex 文件中的 \\cite{} 引用键\n3. 检查：\n   - 所有 \\cite{} 引用的 key 是否都在 bib 中存在\n   - bib 中是否有未被引用的条目（orphan entries）\n   - 每个 bib 条目是否有完整字段（author, title, year, booktitle/journal/publisher）\n   - 是否有 \"placeholder\" 或明显不完整的条目\n   - author 名字格式是否一致\n   - year 是否合理（不应有未来年份除非是 2026 preprint）\n4. 用 WebSearch 抽查 5-10 个引用的真实性（确认论文确实存在，标题/作者匹配）\n\n### 产出\n写一份引用审计报告到：`/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/reference_audit.md`\n\n格式：\n```\n# Reference Audit Report\n\n## 统计\n- 总 bib 条目数: X\n- 被引用条目数: X\n- 未引用条目数: X\n\n## 完整性检查\n| Key | 缺失字段 | 问题 |\n|-----|---------|------|\n\n## 真实性抽查\n| Key | 标题 | 验证结果 |\n|-----|------|---------|\n\n## 问题汇总\n1. ...\n```\n\n用 `register_artifact` 注册报告。",
  "tool_groups": [
    "knowledge"
  ],
  "tools": [
    "WebSearch"
  ]
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8abba94-5b90-4c54-b669-e7f3e21d9480",
  "isSidechain": false,
  "requestId": "req_011Cb3mrE8md8saeaeeXsg92",
  "type": "assistant",
  "uuid": "35b34da7-1087-4a18-9268-6dae2fa98be1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GkfVutgT5JiPzSLM9hh7sg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 671,
      "cache_read_input_tokens": 110402,
      "output_tokens": 1005,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1005,
          "cache_read_input_tokens": 110402,
          "cache_creation_input_tokens": 671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 671
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


### Runtime record

_source line 348_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[WORKER DONE] Worker worker_paper_consistency-fixes_20260515T045751 已完成（status=done）。用 `get_worker_status('worker_paper_consistency-fixes_20260515T045751')` 读取结果，然后处理。  - worker_id: worker_paper_consi…",
  "leafUuid": "35b34da7-1087-4a18-9268-6dae2fa98be1",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


### Runtime record

_source line 349_

```json
{
  "type": "ai-title",
  "aiTitle": "Process completed paper writing tables worker",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


### Tool result

_source line 350 · 2026-05-15T05:07:18.432Z_

<details><summary>↩ Tool result · `toolu_016CMzaj2iPJoH5mbX6LecbK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_reference-audit_20260515T050713\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/workers/worker_paper_reference-audit_20260515T050713.log\", \"setup_data\": {}, \"message\": \"Worker worker_paper_reference-audit_20260515T050713 started. Use get_worker_status('worker_paper_reference-audit_20260515T050713') to check progress.\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35b34da7-1087-4a18-9268-6dae2fa98be1",
  "isSidechain": false,
  "promptId": "d7663afc-402f-4d31-bc13-b0c432bd139f",
  "type": "user",
  "uuid": "03b967ad-c5d8-440a-afec-031c450e012d",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_reference-audit_20260515T050713\\\", \\\"status\\\": \\\"running\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/workers/worker_paper_reference-audit_20260515T050713.log\\\", \\\"setup_data\\\": {}, \\\"message\\\": \\\"Worker worker_paper_reference-audit_20260515T050713 started. Use get_worker_status('worker_paper_reference-audit_20260515T050713') to check progress.\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_reference-audit_20260515T050713\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/workers/worker_paper_reference-audit_20260515T050713.log\", \"setup_data\": {}, \"message\": \"Worker worker_paper_reference-audit_20260515T050713 started. Use get_worker_status('worker_paper_reference-audit_20260515T050713') to check progress.\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "35b34da7-1087-4a18-9268-6dae2fa98be1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 351 · 2026-05-15T05:07:22.377Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF to images result is too large to load directly. Let me use a lower DPI or fewer pages. Or let me read the individual page images from the output directory.

Let me check what files were generated and read individual pages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03b967ad-c5d8-440a-afec-031c450e012d",
  "isSidechain": false,
  "requestId": "req_011Cb3mt2oSPpkMySH9H1DeH",
  "type": "assistant",
  "uuid": "aed11394-78a5-458b-bcdf-7a43014fdb29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXye94FhN5nm6uxTxMKUKY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1802,
      "cache_read_input_tokens": 111073,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 111073,
          "cache_creation_input_tokens": 1802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1802
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


### Assistant

_source line 352 · 2026-05-15T05:07:22.873Z_

PDF 渲染结果太大，逐页查看关键页面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aed11394-78a5-458b-bcdf-7a43014fdb29",
  "isSidechain": false,
  "requestId": "req_011Cb3mt2oSPpkMySH9H1DeH",
  "type": "assistant",
  "uuid": "47df4ff6-4f39-46cf-88a8-feed73224984",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXye94FhN5nm6uxTxMKUKY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1802,
      "cache_read_input_tokens": 111073,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 111073,
          "cache_creation_input_tokens": 1802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1802
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


### Tool call

_source line 353 · 2026-05-15T05:07:23.324Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01UFyKQn3yyk6FL5ieceQFXQ`</summary>

```json
{
  "pattern": "**/_pdf_images/*.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47df4ff6-4f39-46cf-88a8-feed73224984",
  "isSidechain": false,
  "requestId": "req_011Cb3mt2oSPpkMySH9H1DeH",
  "type": "assistant",
  "uuid": "a1dbef32-f567-4f51-b024-415e6cc9437b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXye94FhN5nm6uxTxMKUKY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1802,
      "cache_read_input_tokens": 111073,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1802,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 111073,
          "cache_creation_input_tokens": 1802,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1802
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

_source line 354 · 2026-05-15T05:07:23.335Z_

<details><summary>↩ Tool result · `toolu_01UFyKQn3yyk6FL5ieceQFXQ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p1.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p2.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p3.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p4.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p5.png
/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p6.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1dbef32-f567-4f51-b024-415e6cc9437b",
  "isSidechain": false,
  "promptId": "d7663afc-402f-4d31-bc13-b0c432bd139f",
  "type": "user",
  "uuid": "7471ab48-8e8d-4b96-9d48-14f92d7d8c1e",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p1.png",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p2.png",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p3.png",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p4.png",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p5.png",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p6.png"
    ],
    "durationMs": 6,
    "numFiles": 6,
    "truncated": false
  },
  "sourceToolAssistantUUID": "a1dbef32-f567-4f51-b024-415e6cc9437b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 355 · 2026-05-15T05:07:26.635Z_

<details open><summary>🔧 Tool call — Read · `toolu_018JJXd6G4QR9sXvRyqzFXQT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7471ab48-8e8d-4b96-9d48-14f92d7d8c1e",
  "isSidechain": false,
  "requestId": "req_011Cb3mtPxfeWgqCWzcoVSZw",
  "type": "assistant",
  "uuid": "dadea9e1-61e7-4844-8b05-e0649b89b43a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fm5kNTgZtHVJJpRoUB8JUX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 479,
      "cache_read_input_tokens": 112875,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 479,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 112875,
          "cache_creation_input_tokens": 479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 479
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


### Tool call

_source line 356 · 2026-05-15T05:07:27.151Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YFN9ypDJXaqZoMhNKmALBD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dadea9e1-61e7-4844-8b05-e0649b89b43a",
  "isSidechain": false,
  "requestId": "req_011Cb3mtPxfeWgqCWzcoVSZw",
  "type": "assistant",
  "uuid": "67aba14e-5d33-4c5e-93ef-5675dccbeb69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fm5kNTgZtHVJJpRoUB8JUX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 479,
      "cache_read_input_tokens": 112875,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 479,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 112875,
          "cache_creation_input_tokens": 479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 479
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

_source line 357 · 2026-05-15T05:07:27.269Z_

<details><summary>↩ Tool result · `toolu_018JJXd6G4QR9sXvRyqzFXQT`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dadea9e1-61e7-4844-8b05-e0649b89b43a",
  "isSidechain": false,
  "promptId": "d7663afc-402f-4d31-bc13-b0c432bd139f",
  "type": "user",
  "uuid": "b1a32b74-a868-4594-b5ba-953269f80b69",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 455358
    }
  },
  "sourceToolAssistantUUID": "dadea9e1-61e7-4844-8b05-e0649b89b43a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-15T05:07:27.618Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UmuVQQmwr2APgYJX9C5XPP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1a32b74-a868-4594-b5ba-953269f80b69",
  "isSidechain": false,
  "requestId": "req_011Cb3mtPxfeWgqCWzcoVSZw",
  "type": "assistant",
  "uuid": "ffbd7bf9-e9c6-4abf-87b8-7a4c9178986b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fm5kNTgZtHVJJpRoUB8JUX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 479,
      "cache_read_input_tokens": 112875,
      "output_tokens": 257,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 479,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 257,
          "cache_read_input_tokens": 112875,
          "cache_creation_input_tokens": 479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 479
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


### Runtime record

_source line 359_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[WORKER DONE] Worker worker_paper_consistency-fixes_20260515T045751 已完成（status=done）。用 `get_worker_status('worker_paper_consistency-fixes_20260515T045751')` 读取结果，然后处理。  - worker_id: worker_paper_consi…",
  "leafUuid": "f70f5766-26f6-41cb-ace4-9a7d643f1259",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


### Runtime record

_source line 360_

```json
{
  "type": "ai-title",
  "aiTitle": "Process completed paper writing tables worker",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


### Tool result

_source line 361 · 2026-05-15T05:07:27.837Z_

<details><summary>↩ Tool result · `toolu_01YFN9ypDJXaqZoMhNKmALBD`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67aba14e-5d33-4c5e-93ef-5675dccbeb69",
  "isSidechain": false,
  "promptId": "d7663afc-402f-4d31-bc13-b0c432bd139f",
  "type": "user",
  "uuid": "f70f5766-26f6-41cb-ace4-9a7d643f1259",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 498684
    }
  },
  "sourceToolAssistantUUID": "67aba14e-5d33-4c5e-93ef-5675dccbeb69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 362_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[WORKER DONE] Worker worker_paper_consistency-fixes_20260515T045751 已完成（status=done）。用 `get_worker_status('worker_paper_consistency-fixes_20260515T045751')` 读取结果，然后处理。  - worker_id: worker_paper_consi…",
  "leafUuid": "f70f5766-26f6-41cb-ace4-9a7d643f1259",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


### Runtime record

_source line 363_

```json
{
  "type": "ai-title",
  "aiTitle": "Process completed paper writing tables worker",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


### Tool result

_source line 364 · 2026-05-15T05:07:28.355Z_

<details><summary>↩ Tool result · `toolu_01UmuVQQmwr2APgYJX9C5XPP`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffbd7bf9-e9c6-4abf-87b8-7a4c9178986b",
  "isSidechain": false,
  "promptId": "d7663afc-402f-4d31-bc13-b0c432bd139f",
  "type": "user",
  "uuid": "652eba0c-a587-4c43-a3b5-dc34f19314c4",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 466225
    }
  },
  "sourceToolAssistantUUID": "ffbd7bf9-e9c6-4abf-87b8-7a4c9178986b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 365_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[WORKER DONE] Worker worker_paper_consistency-fixes_20260515T045751 已完成（status=done）。用 `get_worker_status('worker_paper_consistency-fixes_20260515T045751')` 读取结果，然后处理。  - worker_id: worker_paper_consi…",
  "leafUuid": "652eba0c-a587-4c43-a3b5-dc34f19314c4",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


### Runtime record

_source line 366_

```json
{
  "type": "ai-title",
  "aiTitle": "Process completed paper writing tables worker",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


### Runtime record

_source line 367_

```json
{
  "type": "ai-title",
  "aiTitle": "Process completed paper writing tables worker",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


### Runtime record

_source line 368 · 2026-05-15T05:07:37.760Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T05:07:37.760Z",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "content": "[Director 指令] **紧急修正（本地 .tex 文件编辑，不需要 SSH）：**\n\n在 `artifacts/_project/paper/` 目录下修正以下问题：\n\n1. **main.tex**: grep `0.786` → 删除所有 6-gen 行的 CI \"[0.786, 0.799]\"，只保留点估计 \"0.79\"\n2. **main.tex L25**: \"surface-only (0.75)\" → \"surface-only (0.73)\"\n3. **results.tex Table 1**: \"Average (5-gen, ≤2.8B)\" 值从 0.804 → 0.800\n4. **results.tex Table 1**: Qwen3-1.7B 从 0.809 → 0.805\n5. **results.tex Table 1**: caption 和 body 统一为 0.789\n6. **results.tex**: feature importance 排序 entropy_mean(0.164) > ttr(0.159)，修正文本\n7. **全文 grep `plan-`** 确认无内部 ID 残留\n\n修完后 pdflatex 编译验证。"
}
```

---


### Runtime record

_source line 369 · 2026-05-15T05:07:37.761Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T05:07:37.761Z",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e"
}
```

---


## Round 19

## Round 19

2 recorded events


### User

_source line 370 · 2026-05-15T05:07:37.750Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "652eba0c-a587-4c43-a3b5-dc34f19314c4",
  "isSidechain": false,
  "promptId": "b8b965ab-5323-4ba9-894e-bf6d3915911f",
  "type": "user",
  "isMeta": true,
  "uuid": "92556cf0-62ba-4c7d-b2ef-45ade91da931",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 371 · 2026-05-15T05:07:37.750Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92556cf0-62ba-4c7d-b2ef-45ade91da931",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "760f5f74-c4e8-42cf-8e91-16123efe1d0a",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "0a41067b-d75d-4302-ae33-a3776ef7e77e",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 20

## Round 20

38 recorded events


### User

_source line 372 · 2026-05-15T05:07:37.898Z_

[Director 指令] **紧急修正（本地 .tex 文件编辑，不需要 SSH）：**

在 `artifacts/_project/paper/` 目录下修正以下问题：

1. **main.tex**: grep `0.786` → 删除所有 6-gen 行的 CI "[0.786, 0.799]"，只保留点估计 "0.79"
2. **main.tex L25**: "surface-only (0.75)" → "surface-only (0.73)"
3. **results.tex Table 1**: "Average (5-gen, ≤2.8B)" 值从 0.804 → 0.800
4. **results.tex Table 1**: Qwen3-1.7B 从 0.809 → 0.805
5. **results.tex Table 1**: caption 和 body 统一为 0.789
6. **results.tex**: feature importance 排序 entropy_mean(0.164) > ttr(0.159)，修正文本
7. **全文 grep `plan-`** 确认无内部 ID 残留

修完后 pdflatex 编译验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "760f5f74-c4e8-42cf-8e91-16123efe1d0a",
  "isSidechain": false,
  "promptId": "b8b965ab-5323-4ba9-894e-bf6d3915911f",
  "type": "user",
  "uuid": "7167d65e-3ea4-4ff6-95af-2d39f259bb13",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 373 · 2026-05-15T05:07:42.390Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VMtY4PuW3wUCwkfEPRqtqk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7167d65e-3ea4-4ff6-95af-2d39f259bb13",
  "isSidechain": false,
  "requestId": "req_011Cb3muU2XJJE9gyLX9zsr8",
  "type": "assistant",
  "uuid": "93dd7c5b-f059-420d-b3cd-bd5587478f70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016RuG3RgH1FaB7ga2rSK3Ne",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1739,
      "cache_read_input_tokens": 113354,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 113354,
          "cache_creation_input_tokens": 1739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1739
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

_source line 374 · 2026-05-15T05:07:42.405Z_

<details><summary>↩ Tool result · `toolu_01VMtY4PuW3wUCwkfEPRqtqk`</summary>

```text
1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	
11	\graphicspath{{../chart/}}
12	
13	\title{Depth Fingerprinting: Ordinal Generation Depth Estimation\\in Non-Paraphrastic LLM Text Chains}
14	
15	\author{Anonymous}
16	
17	\begin{document}
18	\maketitle
19	
20	\begin{abstract}
21	As large language model (LLM) outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.
22	We formulate \emph{ordinal depth estimation}---classifying whether text is human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---a task that moves beyond binary real-versus-synthetic detection.
23	Existing detectors provide only binary scores and, when repurposed for ordinal prediction, exhibit high cross-generator variance (confidence intervals spanning 0.41--0.82), making them unreliable depth estimators.
24	We characterize a \emph{differential depth response} in distributional features computed under a held-out reference model: central-tendency and diversity features (entropy mean, type-token ratio, hapax ratio) drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay rate) remain near-stationary.
25	Combining both feature types into a 7-feature ensemble exploits this complementarity: the full set (macro-F1\,=\,0.79) outperforms surface-only (0.75) and reference-only (0.75) subsets.
26	In leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\ all single-detector baselines), with per-generator held-out F1 ranging from 0.68 to 0.86.
27	However, depth-aware data curation does not improve downstream language modeling quality compared to random subsampling---data quantity, not depth composition, is the primary determinant---positioning depth fingerprinting as a diagnostic tool for provenance characterization, not a curative tool for data selection.
28	\end{abstract}
29	
30	\input{introduction}
31	\input{related_work}
32	\input{method}
33	\input{results}
34	
35	\input{discussion}
36	\input{conclusion}
37	\input{limitations}
38	\input{ethics}
39	
40	\bibliography{references}
41	
42	\appendix
43	\section{Length Confound Analysis}
44	\label{app:length}
45	% Placeholder — full analysis to be added.
46	
47	\end{document}
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "93dd7c5b-f059-420d-b3cd-bd5587478f70",
  "isSidechain": false,
  "promptId": "b8b965ab-5323-4ba9-894e-bf6d3915911f",
  "type": "user",
  "uuid": "27ce1b4b-78d5-4226-a6be-78fc9050e5ce",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
      "content": "% EMNLP 2026 ARR Submission — ACL 2023 Template\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{amsmath}\n\n\\graphicspath{{../chart/}}\n\n\\title{Depth Fingerprinting: Ordinal Generation Depth Estimation\\\\in Non-Paraphrastic LLM Text Chains}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nAs large language model (LLM) outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.\nWe formulate \\emph{ordinal depth estimation}---classifying whether text is human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---a task that moves beyond binary real-versus-synthetic detection.\nExisting detectors provide only binary scores and, when repurposed for ordinal prediction, exhibit high cross-generator variance (confidence intervals spanning 0.41--0.82), making them unreliable depth estimators.\nWe characterize a \\emph{differential depth response} in distributional features computed under a held-out reference model: central-tendency and diversity features (entropy mean, type-token ratio, hapax ratio) drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay rate) remain near-stationary.\nCombining both feature types into a 7-feature ensemble exploits this complementarity: the full set (macro-F1\\,=\\,0.79) outperforms surface-only (0.75) and reference-only (0.75) subsets.\nIn leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\\ all single-detector baselines), with per-generator held-out F1 ranging from 0.68 to 0.86.\nHowever, depth-aware data curation does not improve downstream language modeling quality compared to random subsampling---data quantity, not depth composition, is the primary determinant---positioning depth fingerprinting as a diagnostic tool for provenance characterization, not a curative tool for data selection.\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{results}\n\n\\input{discussion}\n\\input{conclusion}\n\\input{limitations}\n\\input{ethics}\n\n\\bibliography{references}\n\n\\appendix\n\\section{Length Confound Analysis}\n\\label{app:length}\n% Placeholder — full analysis to be added.\n\n\\end{document}\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  },
  "sourceToolAssistantUUID": "93dd7c5b-f059-420d-b3cd-bd5587478f70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 375 · 2026-05-15T05:07:42.449Z_

```json
{
  "parentUuid": "27ce1b4b-78d5-4226-a6be-78fc9050e5ce",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "18ec451b-40c8-4a2a-be23-d616275d2609",
  "timestamp": "2026-05-15T05:07:42.449Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 376 · 2026-05-15T05:07:46.507Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze what I see in the PDF pages:

**Page 1**: Title, abstract, and beginning of introduction. Layout looks good, two-column format, ACL style. The abstract is visible and complete. The title is "Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains". Author is "Anonymous ACL submission". Good.

**Page 5**: Results section with Table 1 (LOGO classification results). The numbers look correct:
- Pythia-1B: 0.856 ✓
- Pythia-2.8B: 0.804 ✓


- OLMo-2-1B: 0.764, with average F1 scores of 0.789 for 6-generation LOGO and 0.800 for 5-generation ≤2.8B models. ✓

**Page 6**: Figure 1 showing differential depth response across four panels is rendered clearly on the left, and Table 2 with feature ablation results appears on the right.

There's a discrepancy I'm noticing — the caption for Figure 1 mentions "Spearman correlations between individual features and generation depth," but the actual figure displays feature value trends across depths 0-4 rather than correlation coefficients. The four panels show entropy_mean, hapax_ratio, entropy_std, and tail_decay as line plots trending downward across generation depth, which doesn't match what the caption describes.

Figure 2 appears to be a forest plot with error bars showing baseline comparisons, which looks appropriate. I should scan through the remaining pages to check the discussion, conclusion, and any limitations sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "652eba0c-a587-4c43-a3b5-dc34f19314c4",
  "isSidechain": false,
  "requestId": "req_011Cb3mtmC7XrFqNfvgKgYZB",
  "type": "assistant",
  "uuid": "8be6e142-e73f-48d6-a92f-619634a616fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Z9TAponmWgPToWtyVQWEr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 113354,
      "output_tokens": 832,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 832,
          "cache_read_input_tokens": 113354,
          "cache_creation_input_tokens": 1413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1413
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


### Assistant

_source line 377 · 2026-05-15T05:07:46.512Z_

Page 1/5/6 看起来不错：布局正确、两栏格式、表格数字已更新。检查后续页面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8be6e142-e73f-48d6-a92f-619634a616fe",
  "isSidechain": false,
  "requestId": "req_011Cb3mtmC7XrFqNfvgKgYZB",
  "type": "assistant",
  "uuid": "8c1d7743-05ed-4848-a4d6-71b831147a76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Z9TAponmWgPToWtyVQWEr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 113354,
      "output_tokens": 832,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 832,
          "cache_read_input_tokens": 113354,
          "cache_creation_input_tokens": 1413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1413
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


### Tool call

_source line 378 · 2026-05-15T05:07:47.435Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_011La3gVew67T7oaQ62xBHWL`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.pdf",
  "pages": "7-8",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c1d7743-05ed-4848-a4d6-71b831147a76",
  "isSidechain": false,
  "requestId": "req_011Cb3mtmC7XrFqNfvgKgYZB",
  "type": "assistant",
  "uuid": "a86294b6-db31-4d7c-89b7-379da4f37a7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/agent_113cd425",
  "sessionId": "cc34e79c-0750-433b-82e8-2f9b3761bd2e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Z9TAponmWgPToWtyVQWEr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1413,
      "cache_read_input_tokens": 113354,
      "output_tokens": 832,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1413,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 832,
          "cache_read_input_tokens": 113354,
          "cache_creation_input_tokens": 1413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1413
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


### Large event (continued)

````text
### Tool result

_source line 379 · 2026-05-15T05:07:48.035Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_011La3gVew67T7oaQ62xBHWL`&lt;/summary>

```text
Error: result (1,319,618 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/cc34e79c-0750-433b-82e8-2f9b3761bd2e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821668031.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/cc34e79c-0750-433b-82e8-2f9b3761bd2e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821668031.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/cc34e79c-0750-433b-82e8-2f9b3761bd2e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821668031.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a86294b6-db31-4d7c-89b7-379da4f37a7c",
  "isSidechain": false,
  "promptId": "d7663afc-402f-4d31-bc13-b0c432bd139f",
  "type": "user",
  "uuid": "95be38d7-38cc-4d3d-b8fc-6ba9a36f18d6",
  "toolUseResult": "Error: result (1,319,618 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/cc34e79c-0750-433b-82e8-2f9b3761bd2e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821668031.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/cc34e79c-0750-433b-82e8-2f9b3761bd2e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821668031.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-agent-113cd425/cc34e79c-0750-433b-82e8-2f9b3761bd2e/tool-results/mcp-agent-ml-research-pdf_to_images-1778821668031.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/_pdf_images/main_p7.png\", \"base64\": \"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VaW1a9d27tz58ccff+qpp6pWrapVvHLlyrjm4bfffmvTpk2DuGlj887GpEmTNBsJWSq+OnHihOp8bdu2ff75519++eWjR496+65atSrk22mpegdQrXHKlCkat0+fPocPH7ZCLeE33nijY8eO8ZyHM2fODB06tHz58vfdd59W1tNPP/3hhx9qZdWvX199P/7442effdbNQMOGDV955ZWL8dVx1dP+9d/LojoKJU+ePKFjxXNRXNjE42/dunWDBg26dNMHgAQhiyIBPvvss5hzlDFC+h47dixz5szWt2zZsvG5dUe15JYtW7rO5557zkbfsmXLv5nPf/75J1++fJrOTTfd9G+mA/PSSy/ZesmePbuiflyD7du374knntBgHTp00JpVyY4dO1TxypAhw3vvvRcy8Pr164sXL540aVLlQDe6sqt9kCptbsg///yze/fuyZIlu//++7WNBYIPHVWqVEnj6oNOnz4dcWY0BbsjTurUqaMMtmvXrsWLF9eqVUsl//vf/zSMolS/fv1uuOEGlWhq/24hXSr6ygUKFEiRIsWpU6eUQlOmTKlt2/srz4svvhjzf73zzjuur774gw8+qEKlx+HDh+vLWp6vXr16mjRpIv6iFO7HH38sUqRIbGzstGnTrEQjPvroo97ltnbtWjcD+qCLtwBwdftPZtH8+fNfuix6YROPJx0Qbr311oRezwRwtVCdYXUY1aO8wxw5csTKf/75Z1eoCsYPP/zwzTfffP311999912Uyt5FRxZFAmhLLVasWNq0aXVCvf76672BQYYNG6b6rlVGVT+OzwS7du2aLl061/nKK69clCwqVv8mi14Un376qa0XpcG4htHGoG1Dw5QuXdpbPm/ePBv3ww8/dIVKMhkzZlRh+/btvQMrwVqa9W5arVq1sgeTDh065ApVo1KUUnmTJk3imqXWrVvbR4dco6tfv76y6F9//fXqq6/OmDHDpnPFZtGOHTtq9vLmzWud5cqVU2fTpk3dAFrg93loHR08eND1bdSokYZXmrVLzY0bN1aSDwQXTt++feMzA7t379ZOqol069bNW64JVqtWzbvcdEywBU7bJPG0adOmb7/9Vv9olU2dOnX69OknTpywXtrCP//883HjxkX8vWD79u3Tpk0bPXr0ypUrw3/127hx4/r167U3ffzxx5rmP//843ppeI31ySef/P77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pYTYtm2b21m+/fZbVz5nzpzu3bsPGDDghx9+iGvc7du3h+9xS5YscQP8/PPP/fv3b9++/WuvvXbgwIGIE9H0e/fuPXDgwF9++SU+M6zpaGpdu3adMGHC8ePH4xpsxowZ4fN27Ngx67tv375hw4Z17Njx3XffPXz4sHfEM2fOvP/++507dx4yZIjm35UvW7bMTWfnzp3xmVUAAHBVI4sivv75559cuXLFhFm5cmWUsV5++eXBgwf//ffflStXLl68uG9ze/V67733MmXKlCdPnvBeqrgrJGiZK9r5P2MXZtq0aUmSJJk/f/7JkyezZMny5JNP/vXXX+GDtWjRInzTSpky5dGjR9W3fv366lywYIH+v+eee9KlS7dw4UIbsVevXur16quvBoL5J23atBkyZFD88+8bno+SleZw6tSpv/766x9//GGF+r5VqlTRt9u7d2/hwoUnT54ccVyl8fDFMmjQIOs7ffp0LY09e/bo/5kzZ2bLli3ki6uzRo0aFSpUOO8PRs7atWuzZ8+unKz9XWGydOnSLl6GTDl8xtKnT6+cqb46JhQsWHDz5s1nz54dMWLEbbfd5mbg4MGDJUuW1Fah/xcvXpwjR44vvvjCeh06dEiLSMNrUh999FE8ZxgAAFy9yKKIL1VPO3XqtHv37rPnzJ0796abbooyimreKVKk+PrrrwPBiyGWKxLqwIEDixYtusCZvjpVqlQpYhY111577dWSRXfu3Jk8efKkSZOePn1anVWrVlXMePfdd8OHLFGihHql81BnzZo11WvWrFkWdXbt2hU4Fz7z58+vTKv0Yr3c9cYHHnjARdMrhGVRl0IDwQypEneVUl8wNjY2PD8fPnz48ccfX79+vdvjVKJ87oZUaBw/frwbvnLlyu3atXOdWiaZM2du2bKlUmX857ZIkSKNGzd2ncqN3k6nZ8+eH374oebHzVu3bt3q16+vXlovStcvvfSSG1hh+P7777f/FcLvvPNO16tPnz5KsN6F89tvv5FFAQBIJMiiiC/v7YVG1coXX3wxyijffPONqpXLli274A9VvbZixYpjx4694ClcjR588MEoWfS66667WrJo3759tQFkyJDBOpVq1Fm0aNGQwZRkypcv770tc+nSpRry448/Dngume7bt0+d77zzjnXOmTPHBpNnn33WRixXrpw63377bT++XvyEZ1HNZMGC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Xo888oi3l/bNJk2afPHFF5dili6dq3S2ASCxIYviAo0aNcp+RL90H6Fq8aX7iBw5cmji7oa0b7/9NlmyZDlz5ryAS2r9+vUji0a0e/fulClTKoxZp5JY8uTJXadXnTp1VBs+ffr02XPKlCnz7rvvugFGjx4dGxsbMbM1bdpUMfXXc86cOXOJvs6FsSzqvfCuFKcSd5Vy1qxZ+mpxvWdl//79SuClSpUKv7qolKiMN2HChIjhTZt05syZW7ZsqVQZ/7ktUqRI48aNXWfJkiW9nV6KrOPHj3edlStXbteunf75+++/H3jgAft2+v/ll1/W7NWtWzee3/23335LPFm0ffv22rB9+7goWVTy5s3r+n766ae+zRUAIDEji+IClS5dunr16qq1eG87vLg2bNig6d93332XYuI33XSTN4uKXd5U5Tihk3rllVfIohH16tVLS0ZpypWULVtWyzlkMKXH7777zluiQHLNNdccPHjQOhctWqTpWNQJoSEV1a7khR+eRcuVK1ewYEHXeerUKUX0Dh06hI+rGFmxYsUMGTJEuWd17ty54eHtwIEDWbNmVYJNUDK35eydVPfu3VOkSOFWhHP48GEN6W1fR2u2adOmgeAVNm+S0VfIHWSd5/3uiSqLFi5c+JFHHnnhhRcGDx6shX+pG32NnkU7duzo+lapUkUlX3zxRR+PvXv3uoFXrlzZrFkzrc0nnnhi2LBh77777sSJE71T05odO3bsc889V758+Tp16rgHOkKmefLkSZV7S/r16+cmcvr0aS0ZnWg0kbZt206fPr158+bn7RtltgPBTVcz3KBBg4ceeqhTp04h9xro092Imv9A8Jp/zZo1K1SooNWkjfNfrQAAuMSOHTu2Osyff/7pHebIkSNW/vPPP3tH/P7773UGX7Zsmc+NkJNFcSEWLFigSoZSqGotqme48h07dowcOfLtt99+5513LIFs2rRJnSp0d/ppK1cFV2f6efPmnThxIsqnxDOLLl++XPWqzp07T5kyJWTn0fwMHDiwS5cuqtqGPM8WnkVVoVHJ119/rf/1V3WUX375RfOp6dsA27ZtUyVGNbbRo0d7p+ay6MKFC7t166bvG9dtjYnNww8/fOONN3pLXnzxxfjkdi1nZTDXedtttyVLluzQoUPhQ2q9W+351ltvHT58eIKuAfojPIumSZOmXr163mGKFi2a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8gxeunSferpkyZJOnTrpZDgh8MMPP1SpUuWuu+5q2rRpz549mzRpkilTplq1am3ZsiVBv3sL4aeffnr99dfvuOMOJM1xlnW4QJyefPLJgQMHRipviQ93TzQwCBeGixokLILGa/nnnDWPp3L48OFb7tTThIi4c3NG8fntt98im+DZs2cT4vgWko14mgYGDvz9998RT3PVqlUNGjTYtWtXRFJDl+bKlcvhAY8dOzYhuOioUaM6d+6s3+HyxRdflL9btGjBRzds2BDo57BQuKU3Fz1//vI994xo127x1KnbBg78plixkfwkVao+27efUO+sWbOmefPmCRefb+TIkWnSpKlbt+7p06fVzSNHjlStWhWy8eGHHybQd29F5MmT55577olnItQtkkNSEclSUsFvTzQwCB2GixokCM6dOzd48ODq1avnzJnT7wsbN258/fXX77///gceeCCR85YkGDhwYI8ePapUqZIpU6apU6cmdXaC48SJE717965QoQJeSKTSDCoVSYihQ4diShcvXhz/pHAv+vbtW61atZQpU0bwBBc83Q4dOhQqVIiOE6k0byrAImJiYvw+euyxx44fP57I+fmH4+mnn07qLATHQw895PCAV65cGXEuOm/evFKlSjkYYJ06dZRubNSo0Z133nn06FG/P582bVubNguDctG33141duwmdXnp0tVKlSbyq5YtbzhWqkuXLg5WHCmg/ag6jLJ76vXs2bMFChTgKWQ4IT59y2Hv3r3UhhqMCB2//fbbsWPH9DtTpkz56quvIpe1pIG7JxoYhA7DRQ0SBH///feBAwcyZsyIhfb7wsWLF7/55huU17/+9a9EzlviY/To0WhqyyZjlPeWWJCD44WBpIEeeeSRSKUZVCqSEAsXLixRokRE1qFdvnwZrzRv3rzUXgS5KF1mxIgRpHn7cdHr16+3b99+xYoVfp/u2LGDUnfv3j2Rc/VPxpgxY6jzpM5FcCQCF4U5ZM2addWqVY77b731li6WgeYqf/rp9xo1pvJ/UC765JOzHHc+/3w/vypZcrR+EzKTOXPm5cuXh1eMYDh//nz+/PkpUaDTuUeOHClM9ZZb2pMQkA4S7unTp0+fLlWq1G1J2AwXvXnw559/bnEBt8SyTe13333neORYEYYq27ZtG/e3b9+eaHm+BYyNwa0L7JY360iVKlWSc1G6aL9+/RL0E/fcc0+bNm0S9BORgsPjT548eQS5qCCoVMQBBw8e/OijjyKbZjxRs2bNyHJRgBUJnYtGULATmge+8cYbvXv3DvS0bdu2lDp79uyRrcybAXv37t24caNlE4x58+YtWLDgwoUL8ujs2bOffvrplClTTpw44f7hTz/9hB88ceLETZs2uWextm7dKutg9+/fP3ny5M8++8y9VhxGgasxderUmTNn7tmzR39ETlKmTEmdr7Ohb6O4ePHi2rVrx48fv2TJEsf0jmWPtS1cuJA/aKnPP/980qRJhw8fdrzDHfda1kuXLn355Zdjx4795JNPSMRdnI9s7Nixw/EoKBelftbFQkUYIg9y59Ch4MGEXnrpJbiom4D98ccf9913H9+Kjo6mWvz+9u+/r9WqNW3v3tNHjvzhzUXtHRzOtfeHDp3lVw8/PMlxv3nz5iVLlozs+v+BAwdSlmTJkgXqZcihz8Z///tfdTMUSYOALVq0aMKECbRFfPKcEIvG44ynnnqKugorVA9GCttXsGDBhMuVN6h/NAY9VAWjOn/+/DoNR2yoS12xbN68GWXFH3QiEqG3OtSOXy4qCmH06NHLli1zbC2B8CAtVCAigUJAPJAlR4Zp8S+++GLcuHFz5sxxaxKDQDh+/PiXLqBjLVszux85TAyNKPcTc7recFGDBERQ1nHHHXckORdt167dv//974RL/88//0RHP/vsswn3iUgBJyN9+vT6nVuCi+IIli5d+v33349gmvHHY489lrRcNFKC7ZaKyALykC9fPrGUbkCE7rnnnsaNG1NwfKCEy0YiAxJYpkwZCvX222+PGTPm3nvvLVeuHJf58+fHP3vvvfcKFSpUsWJF/N3cuXPriz9x71q3bt2wYcPly5dPmzYNTlK8eHG8THk6YsSIu+++m3Tw/zp37lygQIEsWbJw6RgLw9uoVKnSm2++icMxdOjQzJkzP/744+KRoK969+6dLl06ftXThvig1v9M033Ot8gtDiJCCF996623ZLj9+++/b9KkSerUqe+66y6klNckG5kyZRICCZeDwVapUoWbr7zyip4ZUsORJcNIQvXq1fkJRFce4b8++uijtD5pTp8+nUdvvPGG/tugXHT16tVoG+6QCHxJblLSZs2awSSh9N7NRG2nTZuWovl9ivcsyx/Kli2LE+9+oW/fNbLsNigX9YsNG37hVz16rHbc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IVTVdP+3psOGDQsbF71w4UKKFCkmTZrE/0uXLiHe6dOnx0VGTio1aNCgDz/80PnCYPXq1R9oLgrnfOmll3r27KlCoKOMUTdv3oy7TGvVqqW5qIZGQNBcVMMRfvvtN2V0GrcYNWrUaO3atfewYAKKVL9+fYqnuajGQ4Dt27e3b99e/lu5KGjWrBn8xHmCZ86cEZZow0VlTczIRYUJgLp163J54MABExe9ePGiKtv+/fsJwfKTS73x3gnGjh27YsWKIB6kHWNP0uAkkZGRsUkhrhGSarotcv7pp5/CxkVHjBhBXmGYJeOiUk2aNHmguejs2bMpf3D7toJGhw4dNBfV0AgImotqOAJkT7YAgTlz5kggpkzRokXl//nz53v06NG4cePSpUtXqlRpzJgx6tVjmzZtGnowefLkzZs316pV64MPPsCSxtKV8NGjR9snwlOQXol88ODBYcOGvfXWW2XLll22bJk8KEQUZMmShThLliwJq3Q0HjTcuHFDHYJCt3fs2IG9EnfnuAIFxbt06ZL898pFL1y4cOvWrQULFqD5dI2mTZseP35cbp0+fbpFixbvvfcegV26dPn222/pp2r/LR2WDnL48GFrplYuSgoS8sknn7i9cdETJ06osp08edKtuWgg2LhxY0RERHCnFkNC0qpXr16yZMnYpBDXCEk1rXIOJxdt1qyZ5qL3CpGRkZQ/zOddNRfVuLfAeNhgwfXr192enQKbNm0y3Tp79qw8ePHixS1btjB3r1y5kmjhdByguaiGU/Tr10+szHLlyknI2LFjv/vuO/n/8ssvi4WKGS0rMB9//LHcwkqWByGQuXLlkv9du3Y9evSo/Ied+k2E+BK5Zs2an3/+udxNkiSJ7FTE2kibNi0hJUqUYNb/999/wygYjQcMV65cadOmTY8ePVA8WGj79u1nzZrVv3//woULX7t27V6XzgyvXBR8//33hAwdOpT/5cuXT5cu3blz56DThQoVghDyhwerVq2KNUmlpk6dKim0bNmSDiK7f00wcVFSyJ8/P5eJEiWS46BWLjp9+nQJISMJ0VzUIbZv354pUyYENWTIEFpErXKfPn1aREfguHHjMA4k/MKFC4sXL1aPG0laVFTUsGHD4FpibYC///57rQcyPBK+9i7kmDGN265dO1J44YUXJFy9iDl8+PD69etNpaXLrF69esSIEXPmzFFv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qVdgUblyZR6m98gjjzz22GPIBv4HBQXhf5o0aeSovR07drRs2TI4OBj/wUgDmIH9+/d7fGDKlCl+H0+aetQwYd++fSEhIcmSJYPa+IqzadOmBg0aQJdQL7/99ltSZk9DQ0NDQ0NDI/GguejDj3///TdR069Spcpbb73F/927d+/du3divGX06NHNmzePjo6WkMOHD5u46K1bt9q2bdu/f//EyIBflClTpnr16seOHePlZ599huw988wzvLx27drIkSPJJW7fvp0tW7aAc9EuXbpkypTplVdeeV0BcgUOc/78eb+PJ0Y9JrbuPRy4cuWKMxc1vLqdPXt2zUUdoJVNQ0NDQ0PjgYPmog85pkyZEhoamnjph4eHwz7+/PPPE+8VvvDPP/+YuOi9RfHixc+ePSuXJi5K1KxZc//+/fiD8MBy0ZiYmFq1auHXFN6qVasXX3zR7+OJUY8HDhwYMWJEABN8iJE+fXpnLgq88MILmov6glY2DQ0NDQ2NBxGB56IwlXbdid9//523bty4cejQoS1btoAdbd++/fTp06btf0BkZCQeuXr1asAz9h/E7t27U6ZMmaj7J+fNm6e5KNGjRw/10paLzpgxA0azkQhc9M8//zx58qQpMDY2FiRnzJgxfh8PeD1euXKlQIEC92qO+oGD5qJ3A61sGhoaGhoaDygCz0W3bt368504fPiw4V1jFhYWxpBNmzbxj8mugkmxefNmhGv/HO7x77//rlu3bvz48fPnzz916pSEHzx4MGfOnDBex44d+8svv8iIgOFdL7ply5YJEyYsW7ZMncoToApQF1evXp08efK2bdts3xsVFYVke/fujVd06tTpFy8QyLt4dsmSJXj1ypUrkZTp2fDw8O3bt+PPpUuXFi5c+L///U8m9BB5+fLl06ZNA7kyPbVz587jx4/LpS0XRSDeCA6mBt64cYMiwi/KbkoW5BCvgyj++OMP60sTDFsuKhAuevPmTeg86oICMeHixYtLly6dOHHijh07rAM3fgFJ4i2nT592iONcj8CxY8dmz549c+bMiIgI07O+dA/leumll5Bgu3btkNr+/fuhfkwZask4e/bsYQj7B8GRI0cOHTqE7mLx4sVQDCm1cyX6AuQ2adIkqOKFCxdMt3bv3s1xAZRrypQpq1atMkkYb4FWQDfQBM6cOWNaAuogFrzrxx9/ZJ5/+umn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EThkyJD4pgYFe+utt/i/e/fuvXv3DmRe/xvgAIEbLkq89tprmos+HNBcVENDQ0ND4x6AthQhqy7//fffVKlSMbB8+fIuk9q0aVPCuOjOnTvxOhNXgVEOAjZ06NDbt2/HK7W7R9OmTVGKwHLRxo0bUzj169c33bp69eojjzyCW8mSJVMnonfs2EEiClg9afXp04e3XnnlFTUc9Ewq9LfffpNw/E+RIgXDR48enbBS/PHHHwngorb1e5cYO3Ys8qByUcNLwKpXr7548eIAvihRUa9ePZQC/EcNnDx5MgKTJ09+4sQJ90mFh4fjqc8//zzAWfyP4aOPPooXF/344481F304oLmohoaGhobGPYAtFwXy5cvHQNjELncGJoyL/vrrr48//jieCvi8WQIA3tu5c2eWIoBc9McffxQhz5o1yxqhbt26vFukSJHY2FgGli9fnoH58+e3PrJr1y5Jc86cORLui4sCsog6derUptlUl0gAF02M+p09e3ZwcLCViz5wqF+/vpWLyuTz999/7z6pefPmaS5699BcNCBA57DLAvRsV69etYYTHHNEnIMHD27x4sCBA7JUJwmguaiGhoaGhsY9gC8uyn1TQNasWU2PwEqAxVavXr333ntv8+bNEm7LRW/durV48eL27dvXrl27cePGPXv2VPf4wQThgbHAE088AUt69OjRf/311+cKTKwJFLFbt24w4pHU2rVrJRwWvPrUjRs3tm/fjnyC5n366afR0dF+RQFjqG3btiKN1q1bIx3kUCLs3r27f//+DRs27Nix44wZM9x7A0LZJVnbHZuc5SOmT5+OEGReQkCPbZPNkiULI+TNm1cCHbgoJ9yIzz77zGXmV69e3alTp1dffXXSpEkOXBRcCNEaNGjQp08f1AUDbetXHjlx4sSgQYOQcps2bWwp+oYNG2DrQ9NatmwJ/kmBT5kyJVmyZEyzUqVKSPN///vfvn37pOpHjBihJgJNQM7feustqB9KfejQIbm1ceNGeQrJIgS6+vbbbyMmZJUEE/K2XHTv3r0s3ZIlS0zxUZZ169aNHz8ev7InNioq6pdffunduzceQRX84gUC5aljx45BejNnzoyIiDAlCG1Es8UfPDJt2jRQBbm1Y8cOyA15MGkseolVq1ZdvnwZ8tm2bdvEiRPRLqxFQ1Z//vnnb7/9FiJVkyUuXry4dOlSPIu3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
```

---
