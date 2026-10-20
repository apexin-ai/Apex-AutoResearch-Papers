# Research conversation: [系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director  — Part 17 of 19

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

[← Part 16](part-016.md) · [Transcript overview](../research-conversation-director-main-agent-post-to-director-director-main-agent-post-to-director-copy-3.md) · [Part 18 →](part-018.md) · [Structured JSON](../../../sessions/a0/a047059c5dfdcca65e05.json)

## Round 80

### Assistant

_source line 2763 · 2026-05-19T13:34:19.861Z_

<details><summary>Logged reasoning block</summary>

```text
The "6 Conclusion" heading didn't appear in the search because pdftotext output might be on the boundary between pages 8 and 9. Since "7 Limitations" is on page 9, Conclusion must be on page 8 (or the boundary). Let me check page 8 more carefully.

Actually, looking at the results, Conclusion doesn't appear in the search at all now! This means it might be fully contained on page 8 without "Conclusion" being detected on its own line. Or the search just didn't pick it up. Let me look at the page image.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85dda4be-8772-4e04-b89f-95c68d36561a",
  "isSidechain": false,
  "requestId": "req_011CbC1mkUuwt6J3Re7QMWi1",
  "type": "assistant",
  "uuid": "983ba106-7c7a-4fa5-8a67-1129fdfb48c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011NQY2VAezB7Eon1p7hLUzs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 317,
      "cache_read_input_tokens": 143042,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 270,
          "cache_read_input_tokens": 143042,
          "cache_creation_input_tokens": 317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 317
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

_source line 2764 · 2026-05-19T13:34:20.412Z_

Limitations is on page 9, which means Conclusion should be on page 8. Let me verify visually.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "983ba106-7c7a-4fa5-8a67-1129fdfb48c7",
  "isSidechain": false,
  "requestId": "req_011CbC1mkUuwt6J3Re7QMWi1",
  "type": "assistant",
  "uuid": "0fab7c59-d816-471c-8cc4-522bafacaa57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011NQY2VAezB7Eon1p7hLUzs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 317,
      "cache_read_input_tokens": 143042,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 270,
          "cache_read_input_tokens": 143042,
          "cache_creation_input_tokens": 317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 317
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

_source line 2765 · 2026-05-19T13:34:21.175Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Eyfy7GYX57DvN2MaMKUjQx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fab7c59-d816-471c-8cc4-522bafacaa57",
  "isSidechain": false,
  "requestId": "req_011CbC1mkUuwt6J3Re7QMWi1",
  "type": "assistant",
  "uuid": "21920376-9b64-41ce-9166-5ce4dc0ab678",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011NQY2VAezB7Eon1p7hLUzs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 317,
      "cache_read_input_tokens": 143042,
      "output_tokens": 270,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 317,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 270,
          "cache_read_input_tokens": 143042,
          "cache_creation_input_tokens": 317,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 317
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

_source line 2766 · 2026-05-19T13:34:21.752Z_

<details><summary>↩ Tool result · `toolu_01Eyfy7GYX57DvN2MaMKUjQx`</summary>

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
  "parentUuid": "21920376-9b64-41ce-9166-5ce4dc0ab678",
  "isSidechain": false,
  "promptId": "bf44e86a-6a77-4d12-b438-d4d4b2ba2396",
  "type": "user",
  "uuid": "eddf402b-1358-4e02-80d7-f995bcf2fb5b",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 512741
    }
  },
  "sourceToolAssistantUUID": "21920376-9b64-41ce-9166-5ce4dc0ab678",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor"
}
```

</details>

---


### Runtime record

_source line 2767_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-19。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] [Patch] R18 审稿修订 — 16 项论文修改，0 实验  R18 Fresh Review Overall 3.0 (Findings)。以下修改全部需要在 DDL 5/25 前完…",
  "leafUuid": "eddf402b-1358-4e02-80d7-f995bcf2fb5b",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c"
}
```

---


### Runtime record

_source line 2768_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent response to director callback",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c"
}
```

---


### Assistant

_source line 2769 · 2026-05-19T13:34:27.931Z_

<details><summary>Logged reasoning block</summary>

```text
Looking at page 8 now:
- Left column: Forest plot at top, then Negative Results, then "5 Discussion"
- Right column: Discussion continues with Encoder-quality boundary, Guidance for future research, Generalizability, then "6 Conclusion" starts

At the very bottom right of page 8, I can see "6 Conclusion" and about 3-4 lines of text. The Conclusion continues onto page 9.


Moving to page 9 to see how the Conclusion section wraps up.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eddf402b-1358-4e02-80d7-f995bcf2fb5b",
  "isSidechain": false,
  "requestId": "req_011CbC1nL3mFKskR8Kye6cX9",
  "type": "assistant",
  "uuid": "c09ea87c-6831-4dc6-97fa-3601d2f4ed6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWx3Aunj7nYD94LXtcQsWi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 143359,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 648,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 143359,
          "cache_creation_input_tokens": 648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 648
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

_source line 2770 · 2026-05-19T13:34:28.051Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L9vchcSJhphrtjWAmtQ73G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c09ea87c-6831-4dc6-97fa-3601d2f4ed6c",
  "isSidechain": false,
  "requestId": "req_011CbC1nL3mFKskR8Kye6cX9",
  "type": "assistant",
  "uuid": "bd446df2-4501-4012-84bc-0538820a2c40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWx3Aunj7nYD94LXtcQsWi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 143359,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 648,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 143359,
          "cache_creation_input_tokens": 648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 648
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

_source line 2771 · 2026-05-19T13:34:28.645Z_

<details><summary>↩ Tool result · `toolu_01L9vchcSJhphrtjWAmtQ73G`</summary>

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
  "parentUuid": "bd446df2-4501-4012-84bc-0538820a2c40",
  "isSidechain": false,
  "promptId": "bf44e86a-6a77-4d12-b438-d4d4b2ba2396",
  "type": "user",
  "uuid": "64a73796-9fbc-45ef-a1ab-aabc2970397a",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 502391
    }
  },
  "sourceToolAssistantUUID": "bd446df2-4501-4012-84bc-0538820a2c40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor"
}
```

</details>

---


### Runtime record

_source line 2772_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-19。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] [Patch] R18 审稿修订 — 16 项论文修改，0 实验  R18 Fresh Review Overall 3.0 (Findings)。以下修改全部需要在 DDL 5/25 前完…",
  "leafUuid": "64a73796-9fbc-45ef-a1ab-aabc2970397a",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c"
}
```

---


### Runtime record

_source line 2773_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent response to director callback",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c"
}
```

---


### Assistant

_source line 2774 · 2026-05-19T13:34:48.904Z_

<details><summary>Logged reasoning block</summary>

```text
Looking at page 9:
- Left column starts with continuation of Guidance paragraph from page 8 (the audit protocol numbered items), then Generalizability, then "6 Conclusion" starts about 2/3 down the left column.
- Right column continues Conclusion text and then "7 Limitations" starts.

Wait, I'm confused again. Let me look at this more carefully. On page 8 right column, I saw the Discussion paragraphs. On page 9 left column, I see the audit protocol text, then Generalizability, then Conclusion.

So the Discussion text that was supposed to be on page 8 right column is actually flowing into page 9 left column. 

I'm realizing the Conclusion section actually begins on page 9's left column around the 2/3 mark, with Limitations following on the right column further down. The pdftotext output didn't catch these headings initially, but visually scanning the pages shows they're definitely there.

The real problem is that the Discussion is still overflowing into page 9 even after compression. I need to be more aggressive—either drastically cut the Discussion further or move the audit protocol entirely to the appendix. If I condense the protocol description to a single sentence that just references the appendix, I can reclaim significant space. The detailed methodology can live in the appendix instead of taking up valuable real estate in the main text. I should also look at trimming the "Layer selection" paragraph in the Discussion since it's running long.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64a73796-9fbc-45ef-a1ab-aabc2970397a",
  "isSidechain": false,
  "requestId": "req_011CbC1nqgj3kWCVrbE2W58z",
  "type": "assistant",
  "uuid": "4c1320b5-3f9a-4b92-a51a-100c9e19eb3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011GbTxUp5thpyxKW1Y1Xc5j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 599,
      "cache_read_input_tokens": 144007,
      "output_tokens": 1303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 599,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1303,
          "cache_read_input_tokens": 144007,
          "cache_creation_input_tokens": 599,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 599
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

_source line 2775 · 2026-05-19T13:34:48.906Z_

Conclusion still starts on page 9. Need to drastically compress the Guidance paragraph — move the audit protocol details to appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c1320b5-3f9a-4b92-a51a-100c9e19eb3f",
  "isSidechain": false,
  "requestId": "req_011CbC1nqgj3kWCVrbE2W58z",
  "type": "assistant",
  "uuid": "2bd981e3-1519-4f52-b8f8-1417790d13d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011GbTxUp5thpyxKW1Y1Xc5j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 599,
      "cache_read_input_tokens": 144007,
      "output_tokens": 1303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 599,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1303,
          "cache_read_input_tokens": 144007,
          "cache_creation_input_tokens": 599,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 599
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

_source line 2776 · 2026-05-19T13:35:02.579Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01QrjnxqJ8pcSzZHrQLbvrVs`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex",
  "old_string": "\\paragraph{Guidance for future research.}\nOracle analysis corroborates the evidence gradient (\\cref{sec:oracle}): OT-7B achieves 93.6\\% early detection vs.\\ R1-32B at 50\\%. Converging evidence supports genuine safety representations, but causal validation via DAS~\\citep{geiger2025causal} or ITI~\\citep{li2024iti} is needed. We propose---but have not validated---a multi-metric audit protocol: compute $\\geq$3 metrics (threshold-free and threshold-based) across all layers, flag disagreement when selections differ by $>$10\\% relative depth, report alternative layers for stability, and check cosine volatility at candidate layers (\\cref{app:cosine_volatility}). This protocol requires independent validation. Raising $K$ yields low-FPR operating points (e.g., $K{=}10$: 8\\% FPR at 21\\% coverage; \\cref{app:deployment_operating_points}). For production monitoring, deep layers with $W \\geq 3$ are most reliable.\n\n\\paragraph{Generalizability.}\nThree of four models share the Qwen architecture; only R1-8B (Llama) provides cross-architecture evidence. Layer selection sensitivity follows from representation geometry (architecture-general), but HS advantage magnitudes are specific to these models, HarmThoughts, and self-jailbreak; broader validation is needed before deployment.",
  "new_string": "\\paragraph{Guidance for future research.}\nConverging evidence (oracle analysis, PCA capacity control, control task selectivity, position residualization) supports genuine safety representations, but causal validation via DAS~\\citep{geiger2025causal} or ITI~\\citep{li2024iti} is needed. We propose---but have not validated---a multi-metric audit protocol for layer selection: compute $\\geq$3 metrics (threshold-free and threshold-based), flag metric disagreement, and verify cosine volatility at candidate layers; details and requirements in \\cref{app:cosine_volatility}. Raising $K$ yields low-FPR operating points ($K{=}10$: 8\\% FPR at 21\\% coverage; \\cref{app:deployment_operating_points}). Three of four models share the Qwen architecture; broader validation across architectures, datasets, and attack types is needed before deployment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2bd981e3-1519-4f52-b8f8-1417790d13d7",
  "isSidechain": false,
  "requestId": "req_011CbC1nqgj3kWCVrbE2W58z",
  "type": "assistant",
  "uuid": "0cbf7294-709c-46fc-af77-f6222f7cc8a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011GbTxUp5thpyxKW1Y1Xc5j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 599,
      "cache_read_input_tokens": 144007,
      "output_tokens": 1303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 599,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1303,
          "cache_read_input_tokens": 144007,
          "cache_creation_input_tokens": 599,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 599
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

_source line 2777 · 2026-05-19T13:35:02.595Z_

<details><summary>↩ Tool result · `toolu_01QrjnxqJ8pcSzZHrQLbvrVs`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cbf7294-709c-46fc-af77-f6222f7cc8a2",
  "isSidechain": false,
  "promptId": "bf44e86a-6a77-4d12-b438-d4d4b2ba2396",
  "type": "user",
  "uuid": "1c29652d-99f5-44a9-85e3-df7d2f18c7cc",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex",
    "oldString": "\\paragraph{Guidance for future research.}\nOracle analysis corroborates the evidence gradient (\\cref{sec:oracle}): OT-7B achieves 93.6\\% early detection vs.\\ R1-32B at 50\\%. Converging evidence supports genuine safety representations, but causal validation via DAS~\\citep{geiger2025causal} or ITI~\\citep{li2024iti} is needed. We propose---but have not validated---a multi-metric audit protocol: compute $\\geq$3 metrics (threshold-free and threshold-based) across all layers, flag disagreement when selections differ by $>$10\\% relative depth, report alternative layers for stability, and check cosine volatility at candidate layers (\\cref{app:cosine_volatility}). This protocol requires independent validation. Raising $K$ yields low-FPR operating points (e.g., $K{=}10$: 8\\% FPR at 21\\% coverage; \\cref{app:deployment_operating_points}). For production monitoring, deep layers with $W \\geq 3$ are most reliable.\n\n\\paragraph{Generalizability.}\nThree of four models share the Qwen architecture; only R1-8B (Llama) provides cross-architecture evidence. Layer selection sensitivity follows from representation geometry (architecture-general), but HS advantage magnitudes are specific to these models, HarmThoughts, and self-jailbreak; broader validation is needed before deployment.",
    "newString": "\\paragraph{Guidance for future research.}\nConverging evidence (oracle analysis, PCA capacity control, control task selectivity, position residualization) supports genuine safety representations, but causal validation via DAS~\\citep{geiger2025causal} or ITI~\\citep{li2024iti} is needed. We propose---but have not validated---a multi-metric audit protocol for layer selection: compute $\\geq$3 metrics (threshold-free and threshold-based), flag metric disagreement, and verify cosine volatility at candidate layers; details and requirements in \\cref{app:cosine_volatility}. Raising $K$ yields low-FPR operating points ($K{=}10$: 8\\% FPR at 21\\% coverage; \\cref{app:deployment_operating_points}). Three of four models share the Qwen architecture; broader validation across architectures, datasets, and attack types is needed before deployment.",
    "originalFile": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Layer selection as researcher degree of freedom.}\nOur five-metric ablation (\\cref{sec:layer-results}) shows that crossing rate reverses the central finding: at CR-composite layers, the HS advantage appears scale-dependent; at threshold-based layers, it is graded (confirmed at 7--8B, significant but position-competitive at QwQ-32B$^\\dagger$, exploratory at R1-32B$^\\dagger$). The mechanism---shallow-layer representation compression (\\cref{app:cosine_volatility}), confirmed as label-independent (\\cref{app:random_cp})---is likely generalizable to any threshold-based detection study. This robustness separates the two contributions: layer selection sensitivity (Contribution~1) follows from representation geometry regardless of sample size, while the empirical HS advantage (Contribution~2) is sample-dependent and requires larger-scale validation. The threshold-based layers are the deepest in the network (L63/64 for 32B), consistent with safety features concentrating in late layers~\\citep{wollschlager2025geometry}; however, R1-32B's residualized selectivity is only 3.0pp (\\cref{app:control}), below the 5pp threshold of \\citet{hewitt2019control}.\n\n\\paragraph{Encoder-quality boundary.}\nThe HS advantage is significant against 384d MiniLM (confirmed at 7--8B; descriptive at 32B) but attenuated against 1024d BGE-large (1/4 HB). PCA capacity matching preserves significance (+16.8 to +23.1pp), providing partial evidence against a pure capacity explanation. This boundary is itself a finding: the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference~\\citep{boxo2025linear_probes}. Whether stronger future encoders (e.g., LLM-based embeddings~\\citep{wang2024e5mistral}) could close the gap entirely bounds the shelf life of our HS advantage claims.\n\n\\paragraph{Guidance for future research.}\nOracle analysis corroborates the evidence gradient (\\cref{sec:oracle}): OT-7B achieves 93.6\\% early detection vs.\\ R1-32B at 50\\%. Converging evidence supports genuine safety representations, but causal validation via DAS~\\citep{geiger2025causal} or ITI~\\citep{li2024iti} is needed. We propose---but have not validated---a multi-metric audit protocol: compute $\\geq$3 metrics (threshold-free and threshold-based) across all layers, flag disagreement when selections differ by $>$10\\% relative depth, report alternative layers for stability, and check cosine volatility at candidate layers (\\cref{app:cosine_volatility}). This protocol requires independent validation. Raising $K$ yields low-FPR operating points (e.g., $K{=}10$: 8\\% FPR at 21\\% coverage; \\cref{app:deployment_operating_points}). For production monitoring, deep layers with $W \\geq 3$ are most reliable.\n\n\\paragraph{Generalizability.}\nThree of four models share the Qwen architecture; only R1-8B (Llama) provides cross-architecture evidence. Layer selection sensitivity follows from representation geometry (architecture-general), but HS advantage magnitudes are specific to these models, HarmThoughts, and self-jailbreak; broader validation is needed before deployment.\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 7,
        "newStart": 7,
        "newLines": 4,
        "lines": [
          " The HS advantage is significant against 384d MiniLM (confirmed at 7--8B; descriptive at 32B) but attenuated against 1024d BGE-large (1/4 HB). PCA capacity matching preserves significance (+16.8 to +23.1pp), providing partial evidence against a pure capacity explanation. This boundary is itself a finding: the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference~\\citep{boxo2025linear_probes}. Whether stronger future encoders (e.g., LLM-based embeddings~\\citep{wang2024e5mistral}) could close the gap entirely bounds the shelf life of our HS advantage claims.",
          " ",
          " \\paragraph{Guidance for future research.}",
          "-Oracle analysis corroborates the evidence gradient (\\cref{sec:oracle}): OT-7B achieves 93.6\\% early detection vs.\\ R1-32B at 50\\%. Converging evidence supports genuine safety representations, but causal validation via DAS~\\citep{geiger2025causal} or ITI~\\citep{li2024iti} is needed. We propose---but have not validated---a multi-metric audit protocol: compute $\\geq$3 metrics (threshold-free and threshold-based) across all layers, flag disagreement when selections differ by $>$10\\% relative depth, report alternative layers for stability, and check cosine volatility at candidate layers (\\cref{app:cosine_volatility}). This protocol requires independent validation. Raising $K$ yields low-FPR operating points (e.g., $K{=}10$: 8\\% FPR at 21\\% coverage; \\cref{app:deployment_operating_points}). For production monitoring, deep layers with $W \\geq 3$ are most reliable.",
          "-",
          "-\\paragraph{Generalizability.}",
          "-Three of four models share the Qwen architecture; only R1-8B (Llama) provides cross-architecture evidence. Layer selection sensitivity follows from representation geometry (architecture-general), but HS advantage magnitudes are specific to these models, HarmThoughts, and self-jailbreak; broader validation is needed before deployment.",
          "+Converging evidence (oracle analysis, PCA capacity control, control task selectivity, position residualization) supports genuine safety representations, but causal validation via DAS~\\citep{geiger2025causal} or ITI~\\citep{li2024iti} is needed. We propose---but have not validated---a multi-metric audit protocol for layer selection: compute $\\geq$3 metrics (threshold-free and threshold-based), flag metric disagreement, and verify cosine volatility at candidate layers; details and requirements in \\cref{app:cosine_volatility}. Raising $K$ yields low-FPR operating points ($K{=}10$: 8\\% FPR at 21\\% coverage; \\cref{app:deployment_operating_points}). Three of four models share the Qwen architecture; broader validation across architectures, datasets, and attack types is needed before deployment."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "0cbf7294-709c-46fc-af77-f6222f7cc8a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor"
}
```

</details>

---


### Runtime record

_source line 2778 · 2026-05-19T13:35:02.614Z_

```json
{
  "parentUuid": "1c29652d-99f5-44a9-85e3-df7d2f18c7cc",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [
      {
        "content": "P0#1: Abstract rewrite",
        "status": "completed",
        "activeForm": "Rewriting abstract"
      },
      {
        "content": "P0#2: Introduction framework shift",
        "status": "completed",
        "activeForm": "Updating introduction"
      },
      {
        "content": "P0#3: 32B descriptive reporting",
        "status": "completed",
        "activeForm": "Updating 32B descriptive wording"
      },
      {
        "content": "P0#4: Graded wording replacements",
        "status": "completed",
        "activeForm": "Replacing count-based claims"
      },
      {
        "content": "P0#5: Garden-of-forking-paths paragraph",
        "status": "completed",
        "activeForm": "Adding garden-of-forking-paths"
      },
      {
        "content": "P0#6: K=5 wording unification",
        "status": "completed",
        "activeForm": "Unifying K=5 wording"
      },
      {
        "content": "P0#7: Five-step audit structural rewrite",
        "status": "completed",
        "activeForm": "Rewriting audit protocol"
      },
      {
        "content": "P1#8: HarmThoughts data characteristics",
        "status": "completed",
        "activeForm": "Adding data characteristics"
      },
      {
        "content": "P1#9: Selectivity orthogonal→complementary",
        "status": "completed",
        "activeForm": "Replacing orthogonal"
      },
      {
        "content": "P1#10: AUROC one-sentence mention",
        "status": "completed",
        "activeForm": "Adding AUROC mention"
      },
      {
        "content": "P1#11: Boxo discussion expansion",
        "status": "completed",
        "activeForm": "Expanding Boxo discussion"
      },
      {
        "content": "P1#12: C=1.0 statement",
        "status": "completed",
        "activeForm": "Adding C=1.0 statement"
      },
      {
        "content": "P1#13: Trace-level bootstrap statement",
        "status": "completed",
        "activeForm": "Adding bootstrap statement"
      },
      {
        "content": "P1#14: Add Azaria & Mitchell + Turpin citations",
        "status": "completed",
        "activeForm": "Adding citations"
      },
      {
        "content": "P2#15: Shelf-life caveat",
        "status": "completed",
        "activeForm": "Adding shelf-life caveat"
      },
      {
        "content": "P2#16: CP permanence discussion",
        "status": "completed",
        "activeForm": "Adding CP permanence discussion"
      },
      {
        "content": "Compile, page check, commit, report to Director",
        "status": "in_progress",
        "activeForm": "Compiling and checking pages"
      }
    ],
    "itemCount": 17
  },
  "type": "attachment",
  "uuid": "097da65c-0886-42c0-9df2-17612f82baa1",
  "timestamp": "2026-05-19T13:35:02.614Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor"
}
```

---


### Assistant

_source line 2779 · 2026-05-19T13:35:05.460Z_

Also compress the "Layer selection" paragraph — it repeats experiment details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "097da65c-0886-42c0-9df2-17612f82baa1",
  "isSidechain": false,
  "requestId": "req_011CbC1qLnzZo3X3nrznhG2j",
  "type": "assistant",
  "uuid": "454f0108-825d-4bd9-b6c0-2369d031eeb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCBhvQqFe9dWB4wtdxLZpp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1771,
      "cache_read_input_tokens": 144606,
      "output_tokens": 660,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1771,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 660,
          "cache_read_input_tokens": 144606,
          "cache_creation_input_tokens": 1771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1771
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

_source line 2780 · 2026-05-19T13:35:17.429Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01NPG3nZkDVFvM3Z2kRF5Toc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex",
  "old_string": "Our five-metric ablation (\\cref{sec:layer-results}) shows that crossing rate reverses the central finding: at CR-composite layers, the HS advantage appears scale-dependent; at threshold-based layers, it is graded (confirmed at 7--8B, significant but position-competitive at QwQ-32B$^\\dagger$, exploratory at R1-32B$^\\dagger$). The mechanism---shallow-layer representation compression (\\cref{app:cosine_volatility}), confirmed as label-independent (\\cref{app:random_cp})---is likely generalizable to any threshold-based detection study. This robustness separates the two contributions: layer selection sensitivity (Contribution~1) follows from representation geometry regardless of sample size, while the empirical HS advantage (Contribution~2) is sample-dependent and requires larger-scale validation. The threshold-based layers are the deepest in the network (L63/64 for 32B), consistent with safety features concentrating in late layers~\\citep{wollschlager2025geometry}; however, R1-32B's residualized selectivity is only 3.0pp (\\cref{app:control}), below the 5pp threshold of \\citet{hewitt2019control}.",
  "new_string": "Our five-metric ablation (\\cref{sec:layer-results}) shows that crossing rate reverses the central finding via shallow-layer representation compression (\\cref{app:cosine_volatility}), confirmed as label-independent (\\cref{app:random_cp}) and likely generalizable to any threshold-based detection study. This separates the two contributions: layer selection sensitivity (Contribution~1) follows from representation geometry regardless of sample size; the empirical HS advantage (Contribution~2) is sample-dependent. The threshold-based layers are the deepest in the network (L63/64 for 32B), consistent with late-layer safety features~\\citep{wollschlager2025geometry}; however, R1-32B's residualized selectivity is only 3.0pp (\\cref{app:control}), below the 5pp threshold of \\citet{hewitt2019control}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "454f0108-825d-4bd9-b6c0-2369d031eeb3",
  "isSidechain": false,
  "requestId": "req_011CbC1qLnzZo3X3nrznhG2j",
  "type": "assistant",
  "uuid": "af1e93be-a73f-4bd2-8274-8947221646a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCBhvQqFe9dWB4wtdxLZpp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1771,
      "cache_read_input_tokens": 144606,
      "output_tokens": 660,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1771,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 660,
          "cache_read_input_tokens": 144606,
          "cache_creation_input_tokens": 1771,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1771
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

_source line 2781 · 2026-05-19T13:35:17.446Z_

<details><summary>↩ Tool result · `toolu_01NPG3nZkDVFvM3Z2kRF5Toc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af1e93be-a73f-4bd2-8274-8947221646a2",
  "isSidechain": false,
  "promptId": "bf44e86a-6a77-4d12-b438-d4d4b2ba2396",
  "type": "user",
  "uuid": "b33fcba3-367f-4e4f-b156-4eb0a3be6291",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex",
    "oldString": "Our five-metric ablation (\\cref{sec:layer-results}) shows that crossing rate reverses the central finding: at CR-composite layers, the HS advantage appears scale-dependent; at threshold-based layers, it is graded (confirmed at 7--8B, significant but position-competitive at QwQ-32B$^\\dagger$, exploratory at R1-32B$^\\dagger$). The mechanism---shallow-layer representation compression (\\cref{app:cosine_volatility}), confirmed as label-independent (\\cref{app:random_cp})---is likely generalizable to any threshold-based detection study. This robustness separates the two contributions: layer selection sensitivity (Contribution~1) follows from representation geometry regardless of sample size, while the empirical HS advantage (Contribution~2) is sample-dependent and requires larger-scale validation. The threshold-based layers are the deepest in the network (L63/64 for 32B), consistent with safety features concentrating in late layers~\\citep{wollschlager2025geometry}; however, R1-32B's residualized selectivity is only 3.0pp (\\cref{app:control}), below the 5pp threshold of \\citet{hewitt2019control}.",
    "newString": "Our five-metric ablation (\\cref{sec:layer-results}) shows that crossing rate reverses the central finding via shallow-layer representation compression (\\cref{app:cosine_volatility}), confirmed as label-independent (\\cref{app:random_cp}) and likely generalizable to any threshold-based detection study. This separates the two contributions: layer selection sensitivity (Contribution~1) follows from representation geometry regardless of sample size; the empirical HS advantage (Contribution~2) is sample-dependent. The threshold-based layers are the deepest in the network (L63/64 for 32B), consistent with late-layer safety features~\\citep{wollschlager2025geometry}; however, R1-32B's residualized selectivity is only 3.0pp (\\cref{app:control}), below the 5pp threshold of \\citet{hewitt2019control}.",
    "originalFile": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Layer selection as researcher degree of freedom.}\nOur five-metric ablation (\\cref{sec:layer-results}) shows that crossing rate reverses the central finding: at CR-composite layers, the HS advantage appears scale-dependent; at threshold-based layers, it is graded (confirmed at 7--8B, significant but position-competitive at QwQ-32B$^\\dagger$, exploratory at R1-32B$^\\dagger$). The mechanism---shallow-layer representation compression (\\cref{app:cosine_volatility}), confirmed as label-independent (\\cref{app:random_cp})---is likely generalizable to any threshold-based detection study. This robustness separates the two contributions: layer selection sensitivity (Contribution~1) follows from representation geometry regardless of sample size, while the empirical HS advantage (Contribution~2) is sample-dependent and requires larger-scale validation. The threshold-based layers are the deepest in the network (L63/64 for 32B), consistent with safety features concentrating in late layers~\\citep{wollschlager2025geometry}; however, R1-32B's residualized selectivity is only 3.0pp (\\cref{app:control}), below the 5pp threshold of \\citet{hewitt2019control}.\n\n\\paragraph{Encoder-quality boundary.}\nThe HS advantage is significant against 384d MiniLM (confirmed at 7--8B; descriptive at 32B) but attenuated against 1024d BGE-large (1/4 HB). PCA capacity matching preserves significance (+16.8 to +23.1pp), providing partial evidence against a pure capacity explanation. This boundary is itself a finding: the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference~\\citep{boxo2025linear_probes}. Whether stronger future encoders (e.g., LLM-based embeddings~\\citep{wang2024e5mistral}) could close the gap entirely bounds the shelf life of our HS advantage claims.\n\n\\paragraph{Guidance for future research.}\nConverging evidence (oracle analysis, PCA capacity control, control task selectivity, position residualization) supports genuine safety representations, but causal validation via DAS~\\citep{geiger2025causal} or ITI~\\citep{li2024iti} is needed. We propose---but have not validated---a multi-metric audit protocol for layer selection: compute $\\geq$3 metrics (threshold-free and threshold-based), flag metric disagreement, and verify cosine volatility at candidate layers; details and requirements in \\cref{app:cosine_volatility}. Raising $K$ yields low-FPR operating points ($K{=}10$: 8\\% FPR at 21\\% coverage; \\cref{app:deployment_operating_points}). Three of four models share the Qwen architecture; broader validation across architectures, datasets, and attack types is needed before deployment.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " \\section{Discussion}\\label{sec:discussion}",
          " ",
          " \\paragraph{Layer selection as researcher degree of freedom.}",
          "-Our five-metric ablation (\\cref{sec:layer-results}) shows that crossing rate reverses the central finding: at CR-composite layers, the HS advantage appears scale-dependent; at threshold-based layers, it is graded (confirmed at 7--8B, significant but position-competitive at QwQ-32B$^\\dagger$, exploratory at R1-32B$^\\dagger$). The mechanism---shallow-layer representation compression (\\cref{app:cosine_volatility}), confirmed as label-independent (\\cref{app:random_cp})---is likely generalizable to any threshold-based detection study. This robustness separates the two contributions: layer selection sensitivity (Contribution~1) follows from representation geometry regardless of sample size, while the empirical HS advantage (Contribution~2) is sample-dependent and requires larger-scale validation. The threshold-based layers are the deepest in the network (L63/64 for 32B), consistent with safety features concentrating in late layers~\\citep{wollschlager2025geometry}; however, R1-32B's residualized selectivity is only 3.0pp (\\cref{app:control}), below the 5pp threshold of \\citet{hewitt2019control}.",
          "+Our five-metric ablation (\\cref{sec:layer-results}) shows that crossing rate reverses the central finding via shallow-layer representation compression (\\cref{app:cosine_volatility}), confirmed as label-independent (\\cref{app:random_cp}) and likely generalizable to any threshold-based detection study. This separates the two contributions: layer selection sensitivity (Contribution~1) follows from representation geometry regardless of sample size; the empirical HS advantage (Contribution~2) is sample-dependent. The threshold-based layers are the deepest in the network (L63/64 for 32B), consistent with late-layer safety features~\\citep{wollschlager2025geometry}; however, R1-32B's residualized selectivity is only 3.0pp (\\cref{app:control}), below the 5pp threshold of \\citet{hewitt2019control}.",
          " ",
          " \\paragraph{Encoder-quality boundary.}",
          " The HS advantage is significant against 384d MiniLM (confirmed at 7--8B; descriptive at 32B) but attenuated against 1024d BGE-large (1/4 HB). PCA capacity matching preserves significance (+16.8 to +23.1pp), providing partial evidence against a pure capacity explanation. This boundary is itself a finding: the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference~\\citep{boxo2025linear_probes}. Whether stronger future encoders (e.g., LLM-based embeddings~\\citep{wang2024e5mistral}) could close the gap entirely bounds the shelf life of our HS advantage claims."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "af1e93be-a73f-4bd2-8274-8947221646a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor"
}
```

</details>

---


### Runtime record

_source line 2782_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-19。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] [Patch] R18 审稿修订 — 16 项论文修改，0 实验  R18 Fresh Review Overall 3.0 (Findings)。以下修改全部需要在 DDL 5/25 前完…",
  "leafUuid": "b33fcba3-367f-4e4f-b156-4eb0a3be6291",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c"
}
```

---


### Runtime record

_source line 2783_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent response to director callback",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c"
}
```

---


### Tool call

_source line 2784 · 2026-05-19T13:35:20.846Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_01THwrUCzVEWk2EEZP8W4dQP`</summary>

```json
{
  "project": "contrastive_trace_safety",
  "max_pages": 8,
  "preview": false
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b33fcba3-367f-4e4f-b156-4eb0a3be6291",
  "isSidechain": false,
  "requestId": "req_011CbC1rS7kW3Zkm4Yzg1pw9",
  "type": "assistant",
  "uuid": "57e2d8ab-9492-4424-b25f-0fb99f6cd281",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HiEqwPSPJQwDv7KJD8c6o3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 146377,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 108,
          "cache_read_input_tokens": 146377,
          "cache_creation_input_tokens": 717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 717
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

_source line 2785 · 2026-05-19T13:35:23.794Z_

<details><summary>↩ Tool result · `toolu_01THwrUCzVEWk2EEZP8W4dQP`</summary>

```text
{"result":"{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"Overfull \\\\hbox (40.70114pt too wide) in paragraph at lines 910--923\\n [][] \\n []\\n\\n\\nLaTeX Warning: `h' float specifier changed to `ht'.\\n\\n\\nUnderfull \\\\hbox (badness 1721) in paragraph at lines 925--926\\n []\\\\OT1/ptm/b/n/10.95 R1-8B per-metric HB pass rates.[] \\\\OT1/ptm/m/n/10.95 ta-b\\nle [][]31[][]\\n []\\n\\n[26]\\nUnderfull \\\\hbox (badness 2285) in paragraph at lines 947--948\\n\\\\OT1/ptm/m/n/10.95 while HS FPR ranges from 6.1% to 16.1%\\n []\\n\\n\\nOverfull \\\\hbox (26.43713pt too wide) in paragraph at lines 956--969\\n [][] \\n []\\n\\n\\nLaTeX Warning: `h' float specifier changed to `ht'.\\n\\n\\nOverfull \\\\hbox (69.97162pt too wide) in paragraph at lines 983--993\\n [][] \\n []\\n\\n\\nLaTeX Warning: `h' float specifier changed to `ht'.\\n\\n) [27] [28\\n\\n] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: CC402E3DC09C704AE4937AB6CA378D89;8278.\\n ) \\nHere is how much of TeX's memory you used:\\n 15661 strings out of 469438\\n 258273 string characters out of 5468411\\n 735367 words of memory out of 5000000\\n 43840 multiletter control sequences out of 15000+600000\\n 666418 words of font info for 128 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,15n,93p,2271b,690s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texl\\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/tex\\nmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist\\n/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\\ntype1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\\nublic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\\nmsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\\ncm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/\\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5.pfb>&lt;/usr/sha\\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texl\\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/tex\\nmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist\\n/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\\ntype1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\nype1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\npe1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/time\\ns/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/\\nusr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (28 pages, 724871 bytes).\\nPDF statistics:\\n 1548 PDF objects out of 1728 (max. 8388607)\\n 1266 compressed objects within 13 object streams\\n 251 named destinations out of 1000 (max. 500000)\\n 410 words of extra memory for PDF output out of 10000 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 28, \"warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\"]}, \"pages\": 28, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 2980) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 1968) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 1546) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 2662) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 3148) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 2990) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 3386) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 1389) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 2351) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 1117) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 1412) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 2221) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 1874) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 5787) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1237) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1418) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1092) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1248) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 2922) in paragraph at lines 9--10\", \"Underfull \\\\hbox (badness 1701) in paragraph at lines 9--10\", \"Underfull \\\\hbox (badness 1694) in paragraph at lines 9--10\", \"Underfull \\\\hbox (badness 1609) in paragraph at lines 15--16\", \"Underfull \\\\hbox (badness 1199) in paragraph at lines 15--16\", \"Underfull \\\\hbox (badness 1789) in paragraph at lines 15--16\", \"Underfull \\\\hbox (badness 3679) in paragraph at lines 15--16\", \"Underfull \\\\hbox (badness 2469) in paragraph at lines 15--16\", \"Underfull \\\\hbox (badness 2103) in paragraph at lines 17--18\", \"Underfull \\\\hbox (badness 3323) in paragraph at lines 17--18\", \"Underfull \\\\hbox (badness 2608) in paragraph at lines 17--18\", \"Underfull \\\\hbox (badness 2903) in paragraph at lines 17--18\", \"Underfull \\\\hbox (badness 1783) in paragraph at lines 10--11\", \"Underfull \\\\hbox (badness 2837) in paragraph at lines 13--14\", \"Underfull \\\\hbox (badness 1253) in paragraph at lines 13--14\", \"Underfull \\\\hbox (badness 2393) in paragraph at lines 16--17\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 19--30\", \"Underfull \\\\hbox (badness 1924) in paragraph at lines 19--30\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 19--30\", \"Underfull \\\\hbox (badness 1895) in paragraph at lines 19--30\", \"Underfull \\\\hbox (badness 1728) in paragraph at lines 24--24\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 24--24\", \"Underfull \\\\hbox (badness 4940) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2103) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 1490) in paragraph at lines 52--32\", \"Underfull \\\\hbox (badness 2401) in paragraph at lines 9--10\", \"Underfull \\\\hbox (badness 4168) in paragraph at lines 9--10\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 9--10\", \"Underfull \\\\hbox (badness 4608) in paragraph at lines 9--10\", \"Underfull \\\\hbox (badness 1281) in paragraph at lines 39--40\", \"Underfull \\\\hbox (badness 1314) in paragraph at lines 39--40\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1331) in paragraph at lines 65--66\", \"Underfull \\\\hbox (badness 1286) in paragraph at lines 69--70\", \"Underfull \\\\hbox (badness 1490) in paragraph at lines 71--72\", \"Underfull \\\\vbox (badness 6001) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 2376) in paragraph at lines 73--74\", \"Overfull \\\\hbox (31.90076pt too wide) in paragraph at lines 82--90\", \"Underfull \\\\hbox (badness 2005) in paragraph at lines 90--90\", \"Underfull \\\\hbox (badness 5036) in paragraph at lines 98--99\", \"Underfull \\\\hbox (badness 2057) in paragraph at lines 107--108\", \"Underfull \\\\hbox (badness 1831) in paragraph at lines 111--34\", \"Underfull \\\\hbox (badness 3668) in paragraph at lines 4--5\", \"Underfull \\\\hbox (badness 1983) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 1412) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 1968) in paragraph at lines 5--9\", \"Underfull \\\\hbox (badness 1596) in paragraph at lines 33--39\", \"Underfull \\\\hbox (badness 1502) in paragraph at lines 49--54\", \"Underfull \\\\hbox (badness 4595) in paragraph at lines 102--108\", \"Underfull \\\\hbox (badness 3088) in paragraph at lines 111--118\", \"Underfull \\\\hbox (badness 1831) in paragraph at lines 126--129\", \"Underfull \\\\hbox (badness 2503) in paragraph at lines 145--151\", \"Underfull \\\\hbox (badness 1253) in paragraph at lines 171--176\", \"Underfull \\\\hbox (badness 1688) in paragraph at lines 171--176\", \"Underfull \\\\hbox (badness 1360) in paragraph at lines 253--260\", \"Underfull \\\\hbox (badness 2042) in paragraph at lines 253--260\", \"Underfull \\\\hbox (badness 1184) in paragraph at lines 272--278\", \"Underfull \\\\hbox (badness 1509) in paragraph at lines 272--278\", \"Underfull \\\\hbox (badness 1484) in paragraph at lines 296--302\", \"Underfull \\\\hbox (badness 2229) in paragraph at lines 305--310\", \"Underfull \\\\hbox (badness 2698) in paragraph at lines 397--403\", \"Underfull \\\\hbox (badness 1552) in paragraph at lines 405--410\", \"Underfull \\\\hbox (badness 1014) in paragraph at lines 413--419\", \"Underfull \\\\hbox (badness 2401) in paragraph at lines 453--457\", \"Underfull \\\\hbox (badness 6078) in paragraph at lines 482--488\", \"Underfull \\\\hbox (badness 2503) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 1383) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 1776) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 2486) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 3088) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 6157) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 2990) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 1642) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 1377) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 1565) in paragraph at lines 47--48\", \"Underfull \\\\hbox (badness 1983) in paragraph at lines 51--52\", \"Underfull \\\\hbox (badness 1142) in paragraph at lines 51--52\", \"Underfull \\\\hbox (badness 1418) in paragraph at lines 51--52\", \"Underfull \\\\hbox (badness 1796) in paragraph at lines 53--54\", \"Overfull \\\\hbox (4.98106pt too wide) in paragraph at lines 82--93\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 95--96\", \"Underfull \\\\hbox (badness 1867) in paragraph at lines 124--125\", \"Underfull \\\\hbox (badness 1117) in paragraph at lines 124--125\", \"Underfull \\\\hbox (badness 4341) in paragraph at lines 158--159\", \"Underfull \\\\hbox (badness 2547) in paragraph at lines 160--161\", \"Underfull \\\\hbox (badness 1383) in paragraph at lines 228--229\", \"Underfull \\\\hbox (badness 1158) in paragraph at lines 228--229\", \"Underfull \\\\hbox (badness 1122) in paragraph at lines 230--231\", \"Underfull \\\\hbox (badness 1859) in paragraph at lines 232--233\", \"Underfull \\\\hbox (badness 1173) in paragraph at lines 232--233\", \"Underfull \\\\hbox (badness 3302) in paragraph at lines 260--261\", \"Underfull \\\\hbox (badness 2213) in paragraph at lines 260--261\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 266--267\", \"Underfull \\\\hbox (badness 1107) in paragraph at lines 266--267\", \"Underfull \\\\hbox (badness 6493) in paragraph at lines 316--317\", \"Underfull \\\\hbox (badness 1694) in paragraph at lines 316--317\", \"Underfull \\\\hbox (badness 6364) in paragraph at lines 316--317\", \"Underfull \\\\hbox (badness 1308) in paragraph at lines 318--319\", \"Underfull \\\\hbox (badness 1983) in paragraph at lines 318--319\", \"Underfull \\\\hbox (badness 2875) in paragraph at lines 318--319\", \"Underfull \\\\hbox (badness 1960) in paragraph at lines 318--319\", \"Underfull \\\\hbox (badness 1308) in paragraph at lines 318--319\", \"Underfull \\\\hbox (badness 4254) in paragraph at lines 324--325\", \"Underfull \\\\hbox (badness 2460) in paragraph at lines 324--325\", \"Underfull \\\\hbox (badness 1448) in paragraph at lines 324--325\", \"Underfull \\\\hbox (badness 5908) in paragraph at lines 328--329\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 328--329\", \"Underfull \\\\hbox (badness 3078) in paragraph at lines 396--397\", \"Underfull \\\\hbox (badness 4048) in paragraph at lines 396--397\", \"Underfull \\\\hbox (badness 4779) in paragraph at lines 399--400\", \"Underfull \\\\hbox (badness 1028) in paragraph at lines 399--400\", \"Underfull \\\\hbox (badness 1057) in paragraph at lines 413--414\", \"Underfull \\\\hbox (badness 2556) in paragraph at lines 415--416\", \"Underfull \\\\hbox (badness 1122) in paragraph at lines 415--416\", \"Underfull \\\\hbox (badness 1867) in paragraph at lines 417--418\", \"Underfull \\\\hbox (badness 1052) in paragraph at lines 419--420\", \"Underfull \\\\hbox (badness 1112) in paragraph at lines 419--420\", \"Overfull \\\\hbox (15.98772pt too wide) in paragraph at lines 434--444\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 521--522\", \"Underfull \\\\hbox (badness 2401) in paragraph at lines 521--522\", \"Underfull \\\\vbox (badness 3240) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (42.53093pt too wide) in paragraph at lines 539--552\", \"Overfull \\\\hbox (39.81337pt too wide) in paragraph at lines 574--585\", \"Underfull \\\\hbox (badness 1184) in paragraph at lines 587--588\", \"Underfull \\\\hbox (badness 1077) in paragraph at lines 597--598\", \"Underfull \\\\hbox (badness 6876) in paragraph at lines 606--607\", \"Underfull \\\\hbox (badness 1087) in paragraph at lines 606--607\", \"Underfull \\\\hbox (badness 1253) in paragraph at lines 606--607\", \"Underfull \\\\hbox (badness 2600) in paragraph at lines 617--618\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 642--643\", \"Overfull \\\\hbox (3.81432pt too wide) in paragraph at lines 644--644\", \"Underfull \\\\hbox (badness 4254) in paragraph at lines 644--645\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 647--647\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 647--648\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 648--649\", \"Overfull \\\\hbox (7.54723pt too wide) in paragraph at lines 638--651\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 655--656\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 655--656\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 655--656\", \"Underfull \\\\hbox (badness 3492) in paragraph at lines 655--656\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 657--658\", \"Underfull \\\\hbox (badness 1067) in paragraph at lines 670--671\", \"Underfull \\\\hbox (badness 2547) in paragraph at lines 672--673\", \"Underfull \\\\hbox (badness 2088) in paragraph at lines 672--673\", \"Underfull \\\\hbox (badness 1320) in paragraph at lines 672--673\", \"Underfull \\\\hbox (badness 1603) in paragraph at lines 672--673\", \"Underfull \\\\hbox (badness 1019) in paragraph at lines 674--675\", \"Underfull \\\\hbox (badness 1314) in paragraph at lines 682--683\", \"Underfull \\\\hbox (badness 1527) in paragraph at lines 682--683\", \"Overfull \\\\hbox (93.51962pt too wide) in paragraph at lines 689--699\", \"Overfull \\\\hbox (28.59872pt too wide) in paragraph at lines 710--720\", \"Underfull \\\\hbox (badness 1454) in paragraph at lines 754--755\", \"Overfull \\\\hbox (99.48677pt too wide) in paragraph at lines 761--771\", \"Underfull \\\\hbox (badness 2903) in paragraph at lines 779--780\", \"Overfull \\\\hbox (61.30083pt too wide) in paragraph at lines 784--795\", \"Underfull \\\\hbox (badness 3375) in paragraph at lines 795--795\", \"Underfull \\\\hbox (badness 1418) in paragraph at lines 795--795\", \"Underfull \\\\hbox (badness 1087) in paragraph at lines 799--800\", \"Underfull \\\\hbox (badness 2165) in paragraph at lines 799--800\", \"Underfull \\\\hbox (badness 1152) in paragraph at lines 799--800\", \"Underfull \\\\hbox (badness 1509) in paragraph at lines 813--814\", \"Overfull \\\\hbox (74.61569pt too wide) in paragraph at lines 820--828\", \"Underfull \\\\hbox (badness 1005) in paragraph at lines 831--832\", \"Overfull \\\\hbox (88.5769pt too wide) in paragraph at lines 844--852\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 857--858\", \"Overfull \\\\hbox (26.73994pt too wide) in paragraph at lines 870--880\", \"Overfull \\\\hbox (36.54951pt too wide) in paragraph at lines 891--901\", \"Overfull \\\\hbox (40.70114pt too wide) in paragraph at lines 910--923\", \"Underfull \\\\hbox (badness 1721) in paragraph at lines 925--926\", \"Underfull \\\\hbox (badness 2285) in paragraph at lines 947--948\", \"Overfull \\\\hbox (26.43713pt too wide) in paragraph at lines 956--969\", \"Overfull \\\\hbox (69.97162pt too wide) in paragraph at lines 983--993\"], \"issues\": [\"pages 28 > limit 8\"], \"summary\": \"FAIL: pages 28 > limit 8\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57e2d8ab-9492-4424-b25f-0fb99f6cd281",
  "isSidechain": false,
  "promptId": "bf44e86a-6a77-4d12-b438-d4d4b2ba2396",
  "type": "user",
  "uuid": "3a32a6ac-58bf-4ff8-851c-02d216c9362b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"passed\\\": false, \\\"compiled\\\": {\\\"success\\\": true, \\\"pdf_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.pdf\\\", \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"Overfull \\\\\\\\hbox (40.70114pt too wide) in paragraph at lines 910--923\\\\n [][] \\\\n []\\\\n\\\\n\\\\nLaTeX Warning: `h' float specifier changed to `ht'.\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1721) in paragraph at lines 925--926\\\\n []\\\\\\\\OT1/ptm/b/n/10.95 R1-8B per-metric HB pass rates.[] \\\\\\\\OT1/ptm/m/n/10.95 ta-b\\\\nle [][]31[][]\\\\n []\\\\n\\\\n[26]\\\\nUnderfull \\\\\\\\hbox (badness 2285) in paragraph at lines 947--948\\\\n\\\\\\\\OT1/ptm/m/n/10.95 while HS FPR ranges from 6.1% to 16.1%\\\\n []\\\\n\\\\n\\\\nOverfull \\\\\\\\hbox (26.43713pt too wide) in paragraph at lines 956--969\\\\n [][] \\\\n []\\\\n\\\\n\\\\nLaTeX Warning: `h' float specifier changed to `ht'.\\\\n\\\\n\\\\nOverfull \\\\\\\\hbox (69.97162pt too wide) in paragraph at lines 983--993\\\\n [][] \\\\n []\\\\n\\\\n\\\\nLaTeX Warning: `h' float specifier changed to `ht'.\\\\n\\\\n) [27] [28\\\\n\\\\n] (./main.aux)\\\\n ***********\\\\nLaTeX2e <2025-11-01>\\\\nL3 programming layer <2026-01-19>\\\\n ***********\\\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\\\n(rerunfilecheck)             Checksum: CC402E3DC09C704AE4937AB6CA378D89;8278.\\\\n ) \\\\nHere is how much of TeX's memory you used:\\\\n 15661 strings out of 469438\\\\n 258273 string characters out of 5468411\\\\n 735367 words of memory out of 5000000\\\\n 43840 multiletter control sequences out of 15000+600000\\\\n 666418 words of font info for 128 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,15n,93p,2271b,690s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us\\\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\\\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texl\\\\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/tex\\\\nmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist\\\\n/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\\\\ntype1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\\\\nublic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\\\\nmsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\\\\ncm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.\\\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/\\\\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5.pfb>&lt;/usr/sha\\\\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texl\\\\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/tex\\\\nmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist\\\\n/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\\\\ntype1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\\\nype1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\\\npe1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/time\\\\ns/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/\\\\nusr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\\\nOutput written on main.pdf (28 pages, 724871 bytes).\\\\nPDF statistics:\\\\n 1548 PDF objects out of 1728 (max. 8388607)\\\\n 1266 compressed objects within 13 object streams\\\\n 251 named destinations out of 1000 (max. 500000)\\\\n 410 words of extra memory for PDF output out of 10000 (max. 10000000)\\\\n\\\", \\\"error\\\": \\\"\\\", \\\"pages\\\": 28, \\\"warnings\\\": [\\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\"]}, \\\"pages\\\": 28, \\\"page_status\\\": \\\"over_limit\\\", \\\"max_pages\\\": 8, \\\"min_pages\\\": null, \\\"critical_warnings\\\": [], \\\"minor_warnings\\\": [\\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 1--25\\\", \\\"Underfull \\\\\\\\hbox (badness 2980) in paragraph at lines 1--25\\\", \\\"Underfull \\\\\\\\hbox (badness 1968) in paragraph at lines 1--25\\\", \\\"Underfull \\\\\\\\hbox (badness 1546) in paragraph at lines 1--25\\\", \\\"Underfull \\\\\\\\hbox (badness 2662) in paragraph at lines 1--25\\\", \\\"Underfull \\\\\\\\hbox (badness 3148) in paragraph at lines 1--25\\\", \\\"Underfull \\\\\\\\hbox (badness 2990) in paragraph at lines 1--25\\\", \\\"Underfull \\\\\\\\hbox (badness 3386) in paragraph at lines 1--25\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 1--25\\\", \\\"Underfull \\\\\\\\hbox (badness 1389) in paragraph at lines 1--25\\\", \\\"Underfull \\\\\\\\hbox (badness 2351) in paragraph at lines 1--25\\\", \\\"Underfull \\\\\\\\hbox (badness 1117) in paragraph at lines 1--25\\\", \\\"Underfull \\\\\\\\hbox (badness 1412) in paragraph at lines 1--25\\\", \\\"Underfull \\\\\\\\hbox (badness 2221) in paragraph at lines 1--25\\\", \\\"Underfull \\\\\\\\hbox (badness 1874) in paragraph at lines 1--25\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 3--4\\\", \\\"Underfull \\\\\\\\hbox (badness 5787) in paragraph at lines 3--4\\\", \\\"Underfull \\\\\\\\hbox (badness 1237) in paragraph at lines 3--4\\\", \\\"Underfull \\\\\\\\hbox (badness 1226) in paragraph at lines 3--4\\\", \\\"Underfull \\\\\\\\hbox (badness 1418) in paragraph at lines 3--4\\\", \\\"Underfull \\\\\\\\hbox (badness 1092) in paragraph at lines 3--4\\\", \\\"Underfull \\\\\\\\hbox (badness 1248) in paragraph at lines 3--4\\\", \\\"Underfull \\\\\\\\hbox (badness 1400) in paragraph at lines 5--6\\\", \\\"Underfull \\\\\\\\hbox (badness 2922) in paragraph at lines 9--10\\\", \\\"Underfull \\\\\\\\hbox (badness 1701) in paragraph at lines 9--10\\\", \\\"Underfull \\\\\\\\hbox (badness 1694) in paragraph at lines 9--10\\\", \\\"Underfull \\\\\\\\hbox (badness 1609) in paragraph at lines 15--16\\\", \\\"Underfull \\\\\\\\hbox (badness 1199) in paragraph at lines 15--16\\\", \\\"Underfull \\\\\\\\hbox (badness 1789) in paragraph at lines 15--16\\\", \\\"Underfull \\\\\\\\hbox (badness 3679) in paragraph at lines 15--16\\\", \\\"Underfull \\\\\\\\hbox (badness 2469) in paragraph at lines 15--16\\\", \\\"Underfull \\\\\\\\hbox (badness 2103) in paragraph at lines 17--18\\\", \\\"Underfull \\\\\\\\hbox (badness 3323) in paragraph at lines 17--18\\\", \\\"Underfull \\\\\\\\hbox (badness 2608) in paragraph at lines 17--18\\\", \\\"Underfull \\\\\\\\hbox (badness 2903) in paragraph at lines 17--18\\\", \\\"Underfull \\\\\\\\hbox (badness 1783) in paragraph at lines 10--11\\\", \\\"Underfull \\\\\\\\hbox (badness 2837) in paragraph at lines 13--14\\\", \\\"Underfull \\\\\\\\hbox (badness 1253) in paragraph at lines 13--14\\\", \\\"Underfull \\\\\\\\hbox (badness 2393) in paragraph at lines 16--17\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 19--30\\\", \\\"Underfull \\\\\\\\hbox (badness 1924) in paragraph at lines 19--30\\\", \\\"Underfull \\\\\\\\hbox (badness 1221) in paragraph at lines 19--30\\\", \\\"Underfull \\\\\\\\hbox (badness 1895) in paragraph at lines 19--30\\\", \\\"Underfull \\\\\\\\hbox (badness 1728) in paragraph at lines 24--24\\\", \\\"Underfull \\\\\\\\hbox (badness 1210) in paragraph at lines 24--24\\\", \\\"Underfull \\\\\\\\hbox (badness 4940) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 2103) in paragraph at lines 42--43\\\", \\\"Underfull \\\\\\\\hbox (badness 1490) in paragraph at lines 52--32\\\", \\\"Underfull \\\\\\\\hbox (badness 2401) in paragraph at lines 9--10\\\", \\\"Underfull \\\\\\\\hbox (badness 4168) in paragraph at lines 9--10\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 9--10\\\", \\\"Underfull \\\\\\\\hbox (badness 4608) in paragraph at lines 9--10\\\", \\\"Underfull \\\\\\\\hbox (badness 1281) in paragraph at lines 39--40\\\", \\\"Underfull \\\\\\\\hbox (badness 1314) in paragraph at lines 39--40\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1331) in paragraph at lines 65--66\\\", \\\"Underfull \\\\\\\\hbox (badness 1286) in paragraph at lines 69--70\\\", \\\"Underfull \\\\\\\\hbox (badness 1490) in paragraph at lines 71--72\\\", \\\"Underfull \\\\\\\\vbox (badness 6001) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 2376) in paragraph at lines 73--74\\\", \\\"Overfull \\\\\\\\hbox (31.90076pt too wide) in paragraph at lines 82--90\\\", \\\"Underfull \\\\\\\\hbox (badness 2005) in paragraph at lines 90--90\\\", \\\"Underfull \\\\\\\\hbox (badness 5036) in paragraph at lines 98--99\\\", \\\"Underfull \\\\\\\\hbox (badness 2057) in paragraph at lines 107--108\\\", \\\"Underfull \\\\\\\\hbox (badness 1831) in paragraph at lines 111--34\\\", \\\"Underfull \\\\\\\\hbox (badness 3668) in paragraph at lines 4--5\\\", \\\"Underfull \\\\\\\\hbox (badness 1983) in paragraph at lines 7--8\\\", \\\"Underfull \\\\\\\\hbox (badness 1412) in paragraph at lines 7--8\\\", \\\"Underfull \\\\\\\\hbox (badness 1968) in paragraph at lines 5--9\\\", \\\"Underfull \\\\\\\\hbox (badness 1596) in paragraph at lines 33--39\\\", \\\"Underfull \\\\\\\\hbox (badness 1502) in paragraph at lines 49--54\\\", \\\"Underfull \\\\\\\\hbox (badness 4595) in paragraph at lines 102--108\\\", \\\"Underfull \\\\\\\\hbox (badness 3088) in paragraph at lines 111--118\\\", \\\"Underfull \\\\\\\\hbox (badness 1831) in paragraph at lines 126--129\\\", \\\"Underfull \\\\\\\\hbox (badness 2503) in paragraph at lines 145--151\\\", \\\"Underfull \\\\\\\\hbox (badness 1253) in paragraph at lines 171--176\\\", \\\"Underfull \\\\\\\\hbox (badness 1688) in paragraph at lines 171--176\\\", \\\"Underfull \\\\\\\\hbox (badness 1360) in paragraph at lines 253--260\\\", \\\"Underfull \\\\\\\\hbox (badness 2042) in paragraph at lines 253--260\\\", \\\"Underfull \\\\\\\\hbox (badness 1184) in paragraph at lines 272--278\\\", \\\"Underfull \\\\\\\\hbox (badness 1509) in paragraph at lines 272--278\\\", \\\"Underfull \\\\\\\\hbox (badness 1484) in paragraph at lines 296--302\\\", \\\"Underfull \\\\\\\\hbox (badness 2229) in paragraph at lines 305--310\\\", \\\"Underfull \\\\\\\\hbox (badness 2698) in paragraph at lines 397--403\\\", \\\"Underfull \\\\\\\\hbox (badness 1552) in paragraph at lines 405--410\\\", \\\"Underfull \\\\\\\\hbox (badness 1014) in paragraph at lines 413--419\\\", \\\"Underfull \\\\\\\\hbox (badness 2401) in paragraph at lines 453--457\\\", \\\"Underfull \\\\\\\\hbox (badness 6078) in paragraph at lines 482--488\\\", \\\"Underfull \\\\\\\\hbox (badness 2503) in paragraph at lines 3--26\\\", \\\"Underfull \\\\\\\\hbox (badness 1383) in paragraph at lines 3--26\\\", \\\"Underfull \\\\\\\\hbox (badness 1776) in paragraph at lines 3--26\\\", \\\"Underfull \\\\\\\\hbox (badness 2486) in paragraph at lines 3--26\\\", \\\"Underfull \\\\\\\\hbox (badness 3088) in paragraph at lines 3--26\\\", \\\"Underfull \\\\\\\\hbox (badness 6157) in paragraph at lines 3--26\\\", \\\"Underfull \\\\\\\\hbox (badness 2990) in paragraph at lines 3--26\\\", \\\"Underfull \\\\\\\\hbox (badness 1642) in paragraph at lines 3--26\\\", \\\"Underfull \\\\\\\\hbox (badness 1377) in paragraph at lines 3--26\\\", \\\"Underfull \\\\\\\\hbox (badness 1565) in paragraph at lines 47--48\\\", \\\"Underfull \\\\\\\\hbox (badness 1983) in paragraph at lines 51--52\\\", \\\"Underfull \\\\\\\\hbox (badness 1142) in paragraph at lines 51--52\\\", \\\"Underfull \\\\\\\\hbox (badness 1418) in paragraph at lines 51--52\\\", \\\"Underfull \\\\\\\\hbox (badness 1796) in paragraph at lines 53--54\\\", \\\"Overfull \\\\\\\\hbox (4.98106pt too wide) in paragraph at lines 82--93\\\", \\\"Underfull \\\\\\\\hbox (badness 1062) in paragraph at lines 95--96\\\", \\\"Underfull \\\\\\\\hbox (badness 1867) in paragraph at lines 124--125\\\", \\\"Underfull \\\\\\\\hbox (badness 1117) in paragraph at lines 124--125\\\", \\\"Underfull \\\\\\\\hbox (badness 4341) in paragraph at lines 158--159\\\", \\\"Underfull \\\\\\\\hbox (badness 2547) in paragraph at lines 160--161\\\", \\\"Underfull \\\\\\\\hbox (badness 1383) in paragraph at lines 228--229\\\", \\\"Underfull \\\\\\\\hbox (badness 1158) in paragraph at lines 228--229\\\", \\\"Underfull \\\\\\\\hbox (badness 1122) in paragraph at lines 230--231\\\", \\\"Underfull \\\\\\\\hbox (badness 1859) in paragraph at lines 232--233\\\", \\\"Underfull \\\\\\\\hbox (badness 1173) in paragraph at lines 232--233\\\", \\\"Underfull \\\\\\\\hbox (badness 3302) in paragraph at lines 260--261\\\", \\\"Underfull \\\\\\\\hbox (badness 2213) in paragraph at lines 260--261\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 266--267\\\", \\\"Underfull \\\\\\\\hbox (badness 1107) in paragraph at lines 266--267\\\", \\\"Underfull \\\\\\\\hbox (badness 6493) in paragraph at lines 316--317\\\", \\\"Underfull \\\\\\\\hbox (badness 1694) in paragraph at lines 316--317\\\", \\\"Underfull \\\\\\\\hbox (badness 6364) in paragraph at lines 316--317\\\", \\\"Underfull \\\\\\\\hbox (badness 1308) in paragraph at lines 318--319\\\", \\\"Underfull \\\\\\\\hbox (badness 1983) in paragraph at lines 318--319\\\", \\\"Underfull \\\\\\\\hbox (badness 2875) in paragraph at lines 318--319\\\", \\\"Underfull \\\\\\\\hbox (badness 1960) in paragraph at lines 318--319\\\", \\\"Underfull \\\\\\\\hbox (badness 1308) in paragraph at lines 318--319\\\", \\\"Underfull \\\\\\\\hbox (badness 4254) in paragraph at lines 324--325\\\", \\\"Underfull \\\\\\\\hbox (badness 2460) in paragraph at lines 324--325\\\", \\\"Underfull \\\\\\\\hbox (badness 1448) in paragraph at lines 324--325\\\", \\\"Underfull \\\\\\\\hbox (badness 5908) in paragraph at lines 328--329\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 328--329\\\", \\\"Underfull \\\\\\\\hbox (badness 3078) in paragraph at lines 396--397\\\", \\\"Underfull \\\\\\\\hbox (badness 4048) in paragraph at lines 396--397\\\", \\\"Underfull \\\\\\\\hbox (badness 4779) in paragraph at lines 399--400\\\", \\\"Underfull \\\\\\\\hbox (badness 1028) in paragraph at lines 399--400\\\", \\\"Underfull \\\\\\\\hbox (badness 1057) in paragraph at lines 413--414\\\", \\\"Underfull \\\\\\\\hbox (badness 2556) in paragraph at lines 415--416\\\", \\\"Underfull \\\\\\\\hbox (badness 1122) in paragraph at lines 415--416\\\", \\\"Underfull \\\\\\\\hbox (badness 1867) in paragraph at lines 417--418\\\", \\\"Underfull \\\\\\\\hbox (badness 1052) in paragraph at lines 419--420\\\", \\\"Underfull \\\\\\\\hbox (badness 1112) in paragraph at lines 419--420\\\", \\\"Overfull \\\\\\\\hbox (15.98772pt too wide) in paragraph at lines 434--444\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 521--522\\\", \\\"Underfull \\\\\\\\hbox (badness 2401) in paragraph at lines 521--522\\\", \\\"Underfull \\\\\\\\vbox (badness 3240) has occurred while \\\\\\\\output is active []\\\", \\\"Overfull \\\\\\\\hbox (42.53093pt too wide) in paragraph at lines 539--552\\\", \\\"Overfull \\\\\\\\hbox (39.81337pt too wide) in paragraph at lines 574--585\\\", \\\"Underfull \\\\\\\\hbox (badness 1184) in paragraph at lines 587--588\\\", \\\"Underfull \\\\\\\\hbox (badness 1077) in paragraph at lines 597--598\\\", \\\"Underfull \\\\\\\\hbox (badness 6876) in paragraph at lines 606--607\\\", \\\"Underfull \\\\\\\\hbox (badness 1087) in paragraph at lines 606--607\\\", \\\"Underfull \\\\\\\\hbox (badness 1253) in paragraph at lines 606--607\\\", \\\"Underfull \\\\\\\\hbox (badness 2600) in paragraph at lines 617--618\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 642--643\\\", \\\"Overfull \\\\\\\\hbox (3.81432pt too wide) in paragraph at lines 644--644\\\", \\\"Underfull \\\\\\\\hbox (badness 4254) in paragraph at lines 644--645\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 647--647\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 647--648\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 648--649\\\", \\\"Overfull \\\\\\\\hbox (7.54723pt too wide) in paragraph at lines 638--651\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 655--656\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 655--656\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 655--656\\\", \\\"Underfull \\\\\\\\hbox (badness 3492) in paragraph at lines 655--656\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 657--658\\\", \\\"Underfull \\\\\\\\hbox (badness 1067) in paragraph at lines 670--671\\\", \\\"Underfull \\\\\\\\hbox (badness 2547) in paragraph at lines 672--673\\\", \\\"Underfull \\\\\\\\hbox (badness 2088) in paragraph at lines 672--673\\\", \\\"Underfull \\\\\\\\hbox (badness 1320) in paragraph at lines 672--673\\\", \\\"Underfull \\\\\\\\hbox (badness 1603) in paragraph at lines 672--673\\\", \\\"Underfull \\\\\\\\hbox (badness 1019) in paragraph at lines 674--675\\\", \\\"Underfull \\\\\\\\hbox (badness 1314) in paragraph at lines 682--683\\\", \\\"Underfull \\\\\\\\hbox (badness 1527) in paragraph at lines 682--683\\\", \\\"Overfull \\\\\\\\hbox (93.51962pt too wide) in paragraph at lines 689--699\\\", \\\"Overfull \\\\\\\\hbox (28.59872pt too wide) in paragraph at lines 710--720\\\", \\\"Underfull \\\\\\\\hbox (badness 1454) in paragraph at lines 754--755\\\", \\\"Overfull \\\\\\\\hbox (99.48677pt too wide) in paragraph at lines 761--771\\\", \\\"Underfull \\\\\\\\hbox (badness 2903) in paragraph at lines 779--780\\\", \\\"Overfull \\\\\\\\hbox (61.30083pt too wide) in paragraph at lines 784--795\\\", \\\"Underfull \\\\\\\\hbox (badness 3375) in paragraph at lines 795--795\\\", \\\"Underfull \\\\\\\\hbox (badness 1418) in paragraph at lines 795--795\\\", \\\"Underfull \\\\\\\\hbox (badness 1087) in paragraph at lines 799--800\\\", \\\"Underfull \\\\\\\\hbox (badness 2165) in paragraph at lines 799--800\\\", \\\"Underfull \\\\\\\\hbox (badness 1152) in paragraph at lines 799--800\\\", \\\"Underfull \\\\\\\\hbox (badness 1509) in paragraph at lines 813--814\\\", \\\"Overfull \\\\\\\\hbox (74.61569pt too wide) in paragraph at lines 820--828\\\", \\\"Underfull \\\\\\\\hbox (badness 1005) in paragraph at lines 831--832\\\", \\\"Overfull \\\\\\\\hbox (88.5769pt too wide) in paragraph at lines 844--852\\\", \\\"Underfull \\\\\\\\hbox (badness 2173) in paragraph at lines 857--858\\\", \\\"Overfull \\\\\\\\hbox (26.73994pt too wide) in paragraph at lines 870--880\\\", \\\"Overfull \\\\\\\\hbox (36.54951pt too wide) in paragraph at lines 891--901\\\", \\\"Overfull \\\\\\\\hbox (40.70114pt too wide) in paragraph at lines 910--923\\\", \\\"Underfull \\\\\\\\hbox (badness 1721) in paragraph at lines 925--926\\\", \\\"Underfull \\\\\\\\hbox (badness 2285) in paragraph at lines 947--948\\\", \\\"Overfull \\\\\\\\hbox (26.43713pt too wide) in paragraph at lines 956--969\\\", \\\"Overfull \\\\\\\\hbox (69.97162pt too wide) in paragraph at lines 983--993\\\"], \\\"issues\\\": [\\\"pages 28 > limit 8\\\"], \\\"summary\\\": \\\"FAIL: pages 28 > limit 8\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"Overfull \\\\hbox (40.70114pt too wide) in paragraph at lines 910--923\\n [][] \\n []\\n\\n\\nLaTeX Warning: `h' float specifier changed to `ht'.\\n\\n\\nUnderfull \\\\hbox (badness 1721) in paragraph at lines 925--926\\n []\\\\OT1/ptm/b/n/10.95 R1-8B per-metric HB pass rates.[] \\\\OT1/ptm/m/n/10.95 ta-b\\nle [][]31[][]\\n []\\n\\n[26]\\nUnderfull \\\\hbox (badness 2285) in paragraph at lines 947--948\\n\\\\OT1/ptm/m/n/10.95 while HS FPR ranges from 6.1% to 16.1%\\n []\\n\\n\\nOverfull \\\\hbox (26.43713pt too wide) in paragraph at lines 956--969\\n [][] \\n []\\n\\n\\nLaTeX Warning: `h' float specifier changed to `ht'.\\n\\n\\nOverfull \\\\hbox (69.97162pt too wide) in paragraph at lines 983--993\\n [][] \\n []\\n\\n\\nLaTeX Warning: `h' float specifier changed to `ht'.\\n\\n) [27] [28\\n\\n] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: CC402E3DC09C704AE4937AB6CA378D89;8278.\\n ) \\nHere is how much of TeX's memory you used:\\n 15661 strings out of 469438\\n 258273 string characters out of 5468411\\n 735367 words of memory out of 5000000\\n 43840 multiletter control sequences out of 15000+600000\\n 666418 words of font info for 128 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,15n,93p,2271b,690s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/us\\nr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/shar\\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texl\\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/tex\\nmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist\\n/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\\ntype1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\\nublic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\\nmsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\\ncm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/\\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5.pfb>&lt;/usr/sha\\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texl\\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/tex\\nmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist\\n/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\\ntype1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\\nype1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\npe1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/time\\ns/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/\\nusr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (28 pages, 724871 bytes).\\nPDF statistics:\\n 1548 PDF objects out of 1728 (max. 8388607)\\n 1266 compressed objects within 13 object streams\\n 251 named destinations out of 1000 (max. 500000)\\n 410 words of extra memory for PDF output out of 10000 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 28, \"warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\"]}, \"pages\": 28, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 2980) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 1968) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 1546) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 2662) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 3148) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 2990) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 3386) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 1389) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 2351) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 1117) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 1412) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 2221) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 1874) in paragraph at lines 1--25\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 5787) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1237) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1418) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1092) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1248) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 2922) in paragraph at lines 9--10\", \"Underfull \\\\hbox (badness 1701) in paragraph at lines 9--10\", \"Underfull \\\\hbox (badness 1694) in paragraph at lines 9--10\", \"Underfull \\\\hbox (badness 1609) in paragraph at lines 15--16\", \"Underfull \\\\hbox (badness 1199) in paragraph at lines 15--16\", \"Underfull \\\\hbox (badness 1789) in paragraph at lines 15--16\", \"Underfull \\\\hbox (badness 3679) in paragraph at lines 15--16\", \"Underfull \\\\hbox (badness 2469) in paragraph at lines 15--16\", \"Underfull \\\\hbox (badness 2103) in paragraph at lines 17--18\", \"Underfull \\\\hbox (badness 3323) in paragraph at lines 17--18\", \"Underfull \\\\hbox (badness 2608) in paragraph at lines 17--18\", \"Underfull \\\\hbox (badness 2903) in paragraph at lines 17--18\", \"Underfull \\\\hbox (badness 1783) in paragraph at lines 10--11\", \"Underfull \\\\hbox (badness 2837) in paragraph at lines 13--14\", \"Underfull \\\\hbox (badness 1253) in paragraph at lines 13--14\", \"Underfull \\\\hbox (badness 2393) in paragraph at lines 16--17\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 19--30\", \"Underfull \\\\hbox (badness 1924) in paragraph at lines 19--30\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 19--30\", \"Underfull \\\\hbox (badness 1895) in paragraph at lines 19--30\", \"Underfull \\\\hbox (badness 1728) in paragraph at lines 24--24\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 24--24\", \"Underfull \\\\hbox (badness 4940) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 2103) in paragraph at lines 42--43\", \"Underfull \\\\hbox (badness 1490) in paragraph at lines 52--32\", \"Underfull \\\\hbox (badness 2401) in paragraph at lines 9--10\", \"Underfull \\\\hbox (badness 4168) in paragraph at lines 9--10\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 9--10\", \"Underfull \\\\hbox (badness 4608) in paragraph at lines 9--10\", \"Underfull \\\\hbox (badness 1281) in paragraph at lines 39--40\", \"Underfull \\\\hbox (badness 1314) in paragraph at lines 39--40\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1331) in paragraph at lines 65--66\", \"Underfull \\\\hbox (badness 1286) in paragraph at lines 69--70\", \"Underfull \\\\hbox (badness 1490) in paragraph at lines 71--72\", \"Underfull \\\\vbox (badness 6001) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 2376) in paragraph at lines 73--74\", \"Overfull \\\\hbox (31.90076pt too wide) in paragraph at lines 82--90\", \"Underfull \\\\hbox (badness 2005) in paragraph at lines 90--90\", \"Underfull \\\\hbox (badness 5036) in paragraph at lines 98--99\", \"Underfull \\\\hbox (badness 2057) in paragraph at lines 107--108\", \"Underfull \\\\hbox (badness 1831) in paragraph at lines 111--34\", \"Underfull \\\\hbox (badness 3668) in paragraph at lines 4--5\", \"Underfull \\\\hbox (badness 1983) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 1412) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 1968) in paragraph at lines 5--9\", \"Underfull \\\\hbox (badness 1596) in paragraph at lines 33--39\", \"Underfull \\\\hbox (badness 1502) in paragraph at lines 49--54\", \"Underfull \\\\hbox (badness 4595) in paragraph at lines 102--108\", \"Underfull \\\\hbox (badness 3088) in paragraph at lines 111--118\", \"Underfull \\\\hbox (badness 1831) in paragraph at lines 126--129\", \"Underfull \\\\hbox (badness 2503) in paragraph at lines 145--151\", \"Underfull \\\\hbox (badness 1253) in paragraph at lines 171--176\", \"Underfull \\\\hbox (badness 1688) in paragraph at lines 171--176\", \"Underfull \\\\hbox (badness 1360) in paragraph at lines 253--260\", \"Underfull \\\\hbox (badness 2042) in paragraph at lines 253--260\", \"Underfull \\\\hbox (badness 1184) in paragraph at lines 272--278\", \"Underfull \\\\hbox (badness 1509) in paragraph at lines 272--278\", \"Underfull \\\\hbox (badness 1484) in paragraph at lines 296--302\", \"Underfull \\\\hbox (badness 2229) in paragraph at lines 305--310\", \"Underfull \\\\hbox (badness 2698) in paragraph at lines 397--403\", \"Underfull \\\\hbox (badness 1552) in paragraph at lines 405--410\", \"Underfull \\\\hbox (badness 1014) in paragraph at lines 413--419\", \"Underfull \\\\hbox (badness 2401) in paragraph at lines 453--457\", \"Underfull \\\\hbox (badness 6078) in paragraph at lines 482--488\", \"Underfull \\\\hbox (badness 2503) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 1383) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 1776) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 2486) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 3088) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 6157) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 2990) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 1642) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 1377) in paragraph at lines 3--26\", \"Underfull \\\\hbox (badness 1565) in paragraph at lines 47--48\", \"Underfull \\\\hbox (badness 1983) in paragraph at lines 51--52\", \"Underfull \\\\hbox (badness 1142) in paragraph at lines 51--52\", \"Underfull \\\\hbox (badness 1418) in paragraph at lines 51--52\", \"Underfull \\\\hbox (badness 1796) in paragraph at lines 53--54\", \"Overfull \\\\hbox (4.98106pt too wide) in paragraph at lines 82--93\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 95--96\", \"Underfull \\\\hbox (badness 1867) in paragraph at lines 124--125\", \"Underfull \\\\hbox (badness 1117) in paragraph at lines 124--125\", \"Underfull \\\\hbox (badness 4341) in paragraph at lines 158--159\", \"Underfull \\\\hbox (badness 2547) in paragraph at lines 160--161\", \"Underfull \\\\hbox (badness 1383) in paragraph at lines 228--229\", \"Underfull \\\\hbox (badness 1158) in paragraph at lines 228--229\", \"Underfull \\\\hbox (badness 1122) in paragraph at lines 230--231\", \"Underfull \\\\hbox (badness 1859) in paragraph at lines 232--233\", \"Underfull \\\\hbox (badness 1173) in paragraph at lines 232--233\", \"Underfull \\\\hbox (badness 3302) in paragraph at lines 260--261\", \"Underfull \\\\hbox (badness 2213) in paragraph at lines 260--261\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 266--267\", \"Underfull \\\\hbox (badness 1107) in paragraph at lines 266--267\", \"Underfull \\\\hbox (badness 6493) in paragraph at lines 316--317\", \"Underfull \\\\hbox (badness 1694) in paragraph at lines 316--317\", \"Underfull \\\\hbox (badness 6364) in paragraph at lines 316--317\", \"Underfull \\\\hbox (badness 1308) in paragraph at lines 318--319\", \"Underfull \\\\hbox (badness 1983) in paragraph at lines 318--319\", \"Underfull \\\\hbox (badness 2875) in paragraph at lines 318--319\", \"Underfull \\\\hbox (badness 1960) in paragraph at lines 318--319\", \"Underfull \\\\hbox (badness 1308) in paragraph at lines 318--319\", \"Underfull \\\\hbox (badness 4254) in paragraph at lines 324--325\", \"Underfull \\\\hbox (badness 2460) in paragraph at lines 324--325\", \"Underfull \\\\hbox (badness 1448) in paragraph at lines 324--325\", \"Underfull \\\\hbox (badness 5908) in paragraph at lines 328--329\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 328--329\", \"Underfull \\\\hbox (badness 3078) in paragraph at lines 396--397\", \"Underfull \\\\hbox (badness 4048) in paragraph at lines 396--397\", \"Underfull \\\\hbox (badness 4779) in paragraph at lines 399--400\", \"Underfull \\\\hbox (badness 1028) in paragraph at lines 399--400\", \"Underfull \\\\hbox (badness 1057) in paragraph at lines 413--414\", \"Underfull \\\\hbox (badness 2556) in paragraph at lines 415--416\", \"Underfull \\\\hbox (badness 1122) in paragraph at lines 415--416\", \"Underfull \\\\hbox (badness 1867) in paragraph at lines 417--418\", \"Underfull \\\\hbox (badness 1052) in paragraph at lines 419--420\", \"Underfull \\\\hbox (badness 1112) in paragraph at lines 419--420\", \"Overfull \\\\hbox (15.98772pt too wide) in paragraph at lines 434--444\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 521--522\", \"Underfull \\\\hbox (badness 2401) in paragraph at lines 521--522\", \"Underfull \\\\vbox (badness 3240) has occurred while \\\\output is active []\", \"Overfull \\\\hbox (42.53093pt too wide) in paragraph at lines 539--552\", \"Overfull \\\\hbox (39.81337pt too wide) in paragraph at lines 574--585\", \"Underfull \\\\hbox (badness 1184) in paragraph at lines 587--588\", \"Underfull \\\\hbox (badness 1077) in paragraph at lines 597--598\", \"Underfull \\\\hbox (badness 6876) in paragraph at lines 606--607\", \"Underfull \\\\hbox (badness 1087) in paragraph at lines 606--607\", \"Underfull \\\\hbox (badness 1253) in paragraph at lines 606--607\", \"Underfull \\\\hbox (badness 2600) in paragraph at lines 617--618\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 642--643\", \"Overfull \\\\hbox (3.81432pt too wide) in paragraph at lines 644--644\", \"Underfull \\\\hbox (badness 4254) in paragraph at lines 644--645\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 647--647\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 647--648\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 648--649\", \"Overfull \\\\hbox (7.54723pt too wide) in paragraph at lines 638--651\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 655--656\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 655--656\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 655--656\", \"Underfull \\\\hbox (badness 3492) in paragraph at lines 655--656\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 657--658\", \"Underfull \\\\hbox (badness 1067) in paragraph at lines 670--671\", \"Underfull \\\\hbox (badness 2547) in paragraph at lines 672--673\", \"Underfull \\\\hbox (badness 2088) in paragraph at lines 672--673\", \"Underfull \\\\hbox (badness 1320) in paragraph at lines 672--673\", \"Underfull \\\\hbox (badness 1603) in paragraph at lines 672--673\", \"Underfull \\\\hbox (badness 1019) in paragraph at lines 674--675\", \"Underfull \\\\hbox (badness 1314) in paragraph at lines 682--683\", \"Underfull \\\\hbox (badness 1527) in paragraph at lines 682--683\", \"Overfull \\\\hbox (93.51962pt too wide) in paragraph at lines 689--699\", \"Overfull \\\\hbox (28.59872pt too wide) in paragraph at lines 710--720\", \"Underfull \\\\hbox (badness 1454) in paragraph at lines 754--755\", \"Overfull \\\\hbox (99.48677pt too wide) in paragraph at lines 761--771\", \"Underfull \\\\hbox (badness 2903) in paragraph at lines 779--780\", \"Overfull \\\\hbox (61.30083pt too wide) in paragraph at lines 784--795\", \"Underfull \\\\hbox (badness 3375) in paragraph at lines 795--795\", \"Underfull \\\\hbox (badness 1418) in paragraph at lines 795--795\", \"Underfull \\\\hbox (badness 1087) in paragraph at lines 799--800\", \"Underfull \\\\hbox (badness 2165) in paragraph at lines 799--800\", \"Underfull \\\\hbox (badness 1152) in paragraph at lines 799--800\", \"Underfull \\\\hbox (badness 1509) in paragraph at lines 813--814\", \"Overfull \\\\hbox (74.61569pt too wide) in paragraph at lines 820--828\", \"Underfull \\\\hbox (badness 1005) in paragraph at lines 831--832\", \"Overfull \\\\hbox (88.5769pt too wide) in paragraph at lines 844--852\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 857--858\", \"Overfull \\\\hbox (26.73994pt too wide) in paragraph at lines 870--880\", \"Overfull \\\\hbox (36.54951pt too wide) in paragraph at lines 891--901\", \"Overfull \\\\hbox (40.70114pt too wide) in paragraph at lines 910--923\", \"Underfull \\\\hbox (badness 1721) in paragraph at lines 925--926\", \"Underfull \\\\hbox (badness 2285) in paragraph at lines 947--948\", \"Overfull \\\\hbox (26.43713pt too wide) in paragraph at lines 956--969\", \"Overfull \\\\hbox (69.97162pt too wide) in paragraph at lines 983--993\"], \"issues\": [\"pages 28 > limit 8\"], \"summary\": \"FAIL: pages 28 > limit 8\"}"
    }
  },
  "sourceToolAssistantUUID": "57e2d8ab-9492-4424-b25f-0fb99f6cd281",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor"
}
```

</details>

---


### Runtime record

_source line 2786_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-19。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] [Patch] R18 审稿修订 — 16 项论文修改，0 实验  R18 Fresh Review Overall 3.0 (Findings)。以下修改全部需要在 DDL 5/25 前完…",
  "leafUuid": "3a32a6ac-58bf-4ff8-851c-02d216c9362b",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c"
}
```

---


### Runtime record

_source line 2787_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent response to director callback",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c"
}
```

---


### Tool call

_source line 2788 · 2026-05-19T13:35:32.018Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TUmzdKCWqD4WMqtsZMyDPh`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', '/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\x0c')\nfor i in range(min(12, len(pages))):\n    page = pages[i]\n    for kw in ['6   Conclusion', '7   Limitation', 'Reference']:\n        if kw.lower() in page.lower():\n            lines = page.split('\\n')\n            for line in lines:\n                if kw.lower() in line.lower().strip():\n                    print(f'Page {i+1}: {line.strip()[:100]}')\n                    break\n\"",
  "description": "Find exact section positions in PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a32a6ac-58bf-4ff8-851c-02d216c9362b",
  "isSidechain": false,
  "requestId": "req_011CbC1ruGe4jPys2Hzp5HWE",
  "type": "assistant",
  "uuid": "0ba4d9f1-8805-40e9-9b67-5ef81e54f04a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TebE54onfzZUN8A4yUNo9w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7629,
      "cache_read_input_tokens": 147094,
      "output_tokens": 282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 282,
          "cache_read_input_tokens": 147094,
          "cache_creation_input_tokens": 7629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7629
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

_source line 2789 · 2026-05-19T13:35:32.340Z_

<details><summary>↩ Tool result · `toolu_01TUmzdKCWqD4WMqtsZMyDPh`</summary>

```text
Page 8: 6   Conclusion                                          656
Page 8: 619   advantage (Contribution 2) is sample-dependent.                                            7  
Page 9: 713   (up to 64), W (7 values), K (5 values), and                References
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ba4d9f1-8805-40e9-9b67-5ef81e54f04a",
  "isSidechain": false,
  "promptId": "bf44e86a-6a77-4d12-b438-d4d4b2ba2396",
  "type": "user",
  "uuid": "b9b0d1a2-3110-464a-9771-e34a7bee20c3",
  "toolUseResult": {
    "stdout": "Page 8: 6   Conclusion                                          656\nPage 8: 619   advantage (Contribution 2) is sample-dependent.                                            7  \nPage 9: 713   (up to 64), W (7 values), K (5 values), and                References",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0ba4d9f1-8805-40e9-9b67-5ef81e54f04a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor"
}
```

</details>

---


### Assistant

_source line 2790 · 2026-05-19T13:35:44.270Z_

<details><summary>Logged reasoning block</summary>

```text
Now I can see:
- Page 8 has "6 Conclusion" — the Conclusion header is on page 8
- Page 8 also has "7" appearing — which means Limitations also starts on page 8!
- Page 9 has "References"

Wait, let me re-examine. The pdftotext layout shows:
- Page 8: "6   Conclusion" and also what appears to be "7" (Limitations header) on the same page
- Page 9: "References"

This means Conclusion and Limitations are both on page 8, and References starts on page 9. 

Since EMNLP allows Limitations to not count toward the 8-page limit, having both Conclusion and Limitations on page 8 should be acceptable. But I'm second-guessing whether that "7" is actually the Limitations section header or just a stray number from the text — I should check the page images to be sure.

Let me look at page 8 visually to see how the two-column layout actually breaks down.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9b0d1a2-3110-464a-9771-e34a7bee20c3",
  "isSidechain": false,
  "requestId": "req_011CbC1sXtJ9esJpnqFJ5y7X",
  "type": "assistant",
  "uuid": "af893b2c-c537-4db5-b5c3-9b07d58dd6a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7UfEf6BdAs8ESg1CnKsVn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 361,
      "cache_read_input_tokens": 154723,
      "output_tokens": 502,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 502,
          "cache_read_input_tokens": 154723,
          "cache_creation_input_tokens": 361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 361
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

_source line 2791 · 2026-05-19T13:35:44.279Z_

Conclusion and Limitations section header both appear on page 8 now. Let me verify with the image.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af893b2c-c537-4db5-b5c3-9b07d58dd6a8",
  "isSidechain": false,
  "requestId": "req_011CbC1sXtJ9esJpnqFJ5y7X",
  "type": "assistant",
  "uuid": "8c0a0d73-538a-49b4-a528-fcda56777058",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7UfEf6BdAs8ESg1CnKsVn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 361,
      "cache_read_input_tokens": 154723,
      "output_tokens": 502,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 502,
          "cache_read_input_tokens": 154723,
          "cache_creation_input_tokens": 361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 361
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

_source line 2792 · 2026-05-19T13:35:44.709Z_

<details open><summary>🔧 Tool call — Read · `toolu_018KakNyV8VfSM78Cvp21nFG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c0a0d73-538a-49b4-a528-fcda56777058",
  "isSidechain": false,
  "requestId": "req_011CbC1sXtJ9esJpnqFJ5y7X",
  "type": "assistant",
  "uuid": "2e61de5f-c5b7-47b4-8b60-cfc9969bf7d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L7UfEf6BdAs8ESg1CnKsVn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 361,
      "cache_read_input_tokens": 154723,
      "output_tokens": 502,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 361,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 502,
          "cache_read_input_tokens": 154723,
          "cache_creation_input_tokens": 361,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 361
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

_source line 2793 · 2026-05-19T13:35:45.281Z_

<details><summary>↩ Tool result · `toolu_018KakNyV8VfSM78Cvp21nFG`</summary>

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
  "parentUuid": "2e61de5f-c5b7-47b4-8b60-cfc9969bf7d7",
  "isSidechain": false,
  "promptId": "bf44e86a-6a77-4d12-b438-d4d4b2ba2396",
  "type": "user",
  "uuid": "0cd1f31f-c9ee-4334-9c7f-9814273f733d",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 512741
    }
  },
  "sourceToolAssistantUUID": "2e61de5f-c5b7-47b4-8b60-cfc9969bf7d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor"
}
```

</details>

---


### Runtime record

_source line 2794_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-19。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] [Patch] R18 审稿修订 — 16 项论文修改，0 实验  R18 Fresh Review Overall 3.0 (Findings)。以下修改全部需要在 DDL 5/25 前完…",
  "leafUuid": "0cd1f31f-c9ee-4334-9c7f-9814273f733d",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c"
}
```

---


### Runtime record

_source line 2795_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent response to director callback",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c"
}
```

---


### Assistant

_source line 2796 · 2026-05-19T13:35:54.742Z_

<details><summary>Logged reasoning block</summary>

```text
Looking at page 8:
- Left column: Forest plot figure, Negative Results text, starts "5 Discussion"
- Right column: Discussion continues (Encoder-quality boundary, Guidance, Generalizability), then "6 Conclusion" starts near the bottom

At the very bottom of the right column I can see:
"6 Conclusion"
"Layer selection is a critical researcher degree of"
"freedom that can reverse a study's central conclu-"
"sion; the multi-metric audit workflow described in"
"section 5 would have prevented our initial spuri-"
"ous scale-dependent finding. The HS advantage"


And the conclusion continues onto page 9, so let me look at what comes next.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cd1f31f-c9ee-4334-9c7f-9814273f733d",
  "isSidechain": false,
  "requestId": "req_011CbC1tV8st9JbgGR3fjU2P",
  "type": "assistant",
  "uuid": "a24831bb-cb35-49c9-a54b-a0f972e89948",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVtthD9QyeZPE532fy3rZd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 879,
      "cache_read_input_tokens": 155084,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 274,
          "cache_read_input_tokens": 155084,
          "cache_creation_input_tokens": 879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 879
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

_source line 2797 · 2026-05-19T13:35:54.772Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FgNAB9QmSjH9MEBH4hBn55`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a24831bb-cb35-49c9-a54b-a0f972e89948",
  "isSidechain": false,
  "requestId": "req_011CbC1tV8st9JbgGR3fjU2P",
  "type": "assistant",
  "uuid": "c543b058-9adb-45a8-91e2-db1adcd1e5d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TVtthD9QyeZPE532fy3rZd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 879,
      "cache_read_input_tokens": 155084,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 274,
          "cache_read_input_tokens": 155084,
          "cache_creation_input_tokens": 879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 879
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

_source line 2798 · 2026-05-19T13:35:55.340Z_

<details><summary>↩ Tool result · `toolu_01FgNAB9QmSjH9MEBH4hBn55`</summary>

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
  "parentUuid": "c543b058-9adb-45a8-91e2-db1adcd1e5d9",
  "isSidechain": false,
  "promptId": "bf44e86a-6a77-4d12-b438-d4d4b2ba2396",
  "type": "user",
  "uuid": "d3434b49-1a5a-45c1-adf5-c0850227dd0b",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 502391
    }
  },
  "sourceToolAssistantUUID": "c543b058-9adb-45a8-91e2-db1adcd1e5d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor"
}
```

</details>

---


### Runtime record

_source line 2799_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-19。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] [Patch] R18 审稿修订 — 16 项论文修改，0 实验  R18 Fresh Review Overall 3.0 (Findings)。以下修改全部需要在 DDL 5/25 前完…",
  "leafUuid": "d3434b49-1a5a-45c1-adf5-c0850227dd0b",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c"
}
```

---


### Runtime record

_source line 2800_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent response to director callback",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c"
}
```

---


### Assistant

_source line 2801 · 2026-05-19T13:36:19.296Z_

<details><summary>Logged reasoning block</summary>

```text
Looking at page 9:
- Left column: Continues what was on page 8 right column - the Guidance paragraph (audit protocol), Generalizability, then "6 Conclusion" starts about 2/3 down, then "7 Limitations" header near the bottom.
- Right column: Limitations content continues.

Wait, I'm confused. Page 8 right column showed Conclusion starting at the bottom. But page 9 left column also shows "6 Conclusion" about 2/3 down.

OH WAIT. This is a two-column layout. The flow goes: page 8 left column → page 8 right column → page 9 left column → page 9 right column. 

So what I see on page 8 right column at the bottom is probably NOT the start of Conclusion — it's text that will continue onto page 9 left column. Let me re-examine page 8 right column bottom more carefully. I see the Guidance paragraph about Oracle analysis, then the Generalizability section discussing production monitoring and reliability thresholds, which continues partway down the page.

Now looking at the next chunk, I can see the Conclusion section actually does start on page 8 right column at the very bottom with just 2-3 lines of body text before it continues onto page 9. But when I look at page 9 left column, the text starting with "layer selection in hidden-state probing studies:" appears to be part of the audit protocol, not a continuation of Conclusion. I need to trace through this more carefully to understand where each section actually begins and ends across the page break. The page footer numbers are the authoritative source here, so Conclusion is definitely on page 9. I'm realizing the pdftotext output might be stale or cached from an earlier render, so I should regenerate the page 9 image fresh to verify what I'm actually seeing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3434b49-1a5a-45c1-adf5-c0850227dd0b",
  "isSidechain": false,
  "requestId": "req_011CbC1uE9FwV7aqsFxLtAaa",
  "type": "assistant",
  "uuid": "f92fdbcc-2ee1-49a5-86a2-6527d8989d90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01816mLGm3vL71YwLqfZS6xh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 155963,
      "output_tokens": 1303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1303,
          "cache_read_input_tokens": 155963,
          "cache_creation_input_tokens": 652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 652
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

_source line 2802 · 2026-05-19T13:36:19.298Z_

Let me re-render pages 8-9 fresh to check after latest changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f92fdbcc-2ee1-49a5-86a2-6527d8989d90",
  "isSidechain": false,
  "requestId": "req_011CbC1uE9FwV7aqsFxLtAaa",
  "type": "assistant",
  "uuid": "9aea0256-0063-47f7-a0d1-4a821dc6a830",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01816mLGm3vL71YwLqfZS6xh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 155963,
      "output_tokens": 1303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1303,
          "cache_read_input_tokens": 155963,
          "cache_creation_input_tokens": 652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 652
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

_source line 2803 · 2026-05-19T13:36:22.382Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SkUfPJ9xAh9gofErpVF2N4`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess, json\n# Use pdftotext to find page numbers from the actual text, looking for section headers\nresult = subprocess.run(['pdftotext', '/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\x0c')\nfor i in range(7, min(12, len(pages))):\n    page = pages[i]\n    # Search for section numbers\n    if '6 Conclusion' in page or '7 Limitations' in page or 'References' in page:\n        # Get the first and last few meaningful lines\n        lines = [l.strip() for l in page.split('\\n') if l.strip()]\n        print(f'=== Page {i+1} (first 5 lines) ===')\n        for l in lines[:5]:\n            print(f'  {l[:80]}')\n        print(f'=== Page {i+1} (last 5 lines) ===')\n        for l in lines[-5:]:\n            print(f'  {l[:80]}')\n        print()\n\"",
  "description": "Detailed page analysis for section placement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9aea0256-0063-47f7-a0d1-4a821dc6a830",
  "isSidechain": false,
  "requestId": "req_011CbC1uE9FwV7aqsFxLtAaa",
  "type": "assistant",
  "uuid": "35e83273-2f49-4657-bfdd-4de9189873f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01816mLGm3vL71YwLqfZS6xh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 155963,
      "output_tokens": 1303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 652,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1303,
          "cache_read_input_tokens": 155963,
          "cache_creation_input_tokens": 652,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 652
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

_source line 2804 · 2026-05-19T13:36:22.669Z_

<details><summary>↩ Tool result · `toolu_01SkUfPJ9xAh9gofErpVF2N4`</summary>

```text
=== Page 9 (first 5 lines) ===
  678
  679
  680
  681
  682
=== Page 9 (last 5 lines) ===
  757
  758
  759
  760
  761
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35e83273-2f49-4657-bfdd-4de9189873f4",
  "isSidechain": false,
  "promptId": "bf44e86a-6a77-4d12-b438-d4d4b2ba2396",
  "type": "user",
  "uuid": "9efaef17-f816-4c4a-b632-a757d96deb19",
  "toolUseResult": {
    "stdout": "=== Page 9 (first 5 lines) ===\n  678\n  679\n  680\n  681\n  682\n=== Page 9 (last 5 lines) ===\n  757\n  758\n  759\n  760\n  761",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "35e83273-2f49-4657-bfdd-4de9189873f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor"
}
```

</details>

---


### Assistant

_source line 2805 · 2026-05-19T13:36:27.123Z_

<details><summary>Logged reasoning block</summary>

```text
The pdftotext output without -layout gives much less useful results — just line numbers. Let me try with -layout and look at the actual text content around the Conclusion section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9efaef17-f816-4c4a-b632-a757d96deb19",
  "isSidechain": false,
  "requestId": "req_011CbC1wF48SFxFLyUcbSmuZ",
  "type": "assistant",
  "uuid": "3130e510-4c3d-46a8-a1ab-a1411d39344e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012nTSS1aN8PwSiFZNfkTKj2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 156615,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1375,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 338,
          "cache_read_input_tokens": 156615,
          "cache_creation_input_tokens": 1375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1375
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

_source line 2806 · 2026-05-19T13:36:29.675Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SeuFdkapwfj5QQQhxjHTGf`</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', '/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\x0c')\n# Look at page 8 and 9 (0-indexed: 7 and 8)\nfor pidx in [7, 8]:\n    page = pages[pidx]\n    lines = page.split('\\n')\n    print(f'=== Physical Page {pidx+1} last 20 lines ===')\n    for line in lines[-25:]:\n        if line.strip():\n            print(f'  {line.rstrip()[:100]}')\n    print()\n\"",
  "description": "Check last lines of pages 8-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3130e510-4c3d-46a8-a1ab-a1411d39344e",
  "isSidechain": false,
  "requestId": "req_011CbC1wF48SFxFLyUcbSmuZ",
  "type": "assistant",
  "uuid": "4538b7c8-a2c1-47eb-86b7-79a9d208213a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012nTSS1aN8PwSiFZNfkTKj2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1375,
      "cache_read_input_tokens": 156615,
      "output_tokens": 338,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1375,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 338,
          "cache_read_input_tokens": 156615,
          "cache_creation_input_tokens": 1375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1375
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

_source line 2807 · 2026-05-19T13:36:29.959Z_

<details><summary>↩ Tool result · `toolu_01SeuFdkapwfj5QQQhxjHTGf`</summary>

```text
=== Physical Page 8 last 20 lines ===
                                                                                                   cod
  616   contributions: layer selection sensitivity (Con-
                                                                                                   tio
  617   tribution 1) follows from representation geome-
                                                                                                   Li 
  618   try regardless of sample size; the empirical HS
  619   advantage (Contribution 2) is sample-dependent.                                            7  
  620   The threshold-based layers are the deepest in the
  621   network (L63/64 for 32B), consistent with late-                                            Sin
  622   layer safety features (Wollschläger et al., 2025);                                        (Ha
  623   however, R1-32B’s residualized selectivity is only                                         vid
  624   3.0pp (section H), below the 5pp threshold of He-                                          ual
  625   witt and Liang (2019).                                                                     spa
                                                                                                   fra
  626   Encoder-quality boundary. The HS advantage                                                 sul
  627   is significant against 384d MiniLM (confirmed at                                           rea
  628   7–8B; descriptive at 32B) but attenuated against                                           fer
                                                                                               8

=== Physical Page 9 last 20 lines ===
  713   (up to 64), W (7 values), K (5 values), and                References                         
  714   threshold are selected on the same validation set          Ryan Prescott Adams and David J.C. 
  715   (n=4–9 per-class at 32B, up to 2,240 configu-                Bayesian online changepoint detec
  716   rations); cumulative degrees of freedom are sub-             preprint arXiv:0710.3742.        
  717   stantial (section W provides convergence, cross-           Patrick Ahrend, Tobias Eder, Xiyang
  718   validation, and bootstrap analyses addressing this           and Georg Groh. 2026. Safer reaso
  719   concern). BA-optimal layer indices are sensitive             suring and mitigating chain-of-th
  720   to the train/validation split, spanning 7–98% depth          LLMs. arXiv preprint arXiv:2603.0
  721   across models and splits (section Y); for exam-
                                                                   Guillaume Alain and Yoshua Bengio. 
  722   ple, OT-7B shifts from L16 to L2 and QwQ-32B                 standing intermediate layers usin
  723   from L60 to L63 between 70/30 and 60/20/20                   probes. In Workshop Track, Intern
  724   splits, a direct manifestation of the layer selec-           ence on Learning Representations 
  725   tion sensitivity that constitutes our primary find-
                                                                   Tyler Alvarez and Ali Baheri. 2026.
  726   ing. Threshold-based metrics are more stable but             reasoning break? step-level hallu
  727   still vary by up to 4 layers. K=5 was selected               via hidden-state transport geomet
  728   on the R1-8B validation set and held fixed (sec-             arXiv:2605.13772. Concurrent work
                                                               9
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4538b7c8-a2c1-47eb-86b7-79a9d208213a",
  "isSidechain": false,
  "promptId": "bf44e86a-6a77-4d12-b438-d4d4b2ba2396",
  "type": "user",
  "uuid": "71df1919-0829-40f6-81a0-9ead26aa1928",
  "toolUseResult": {
    "stdout": "=== Physical Page 8 last 20 lines ===\n                                                                                                   cod\n  616   contributions: layer selection sensitivity (Con-\n                                                                                                   tio\n  617   tribution 1) follows from representation geome-\n                                                                                                   Li \n  618   try regardless of sample size; the empirical HS\n  619   advantage (Contribution 2) is sample-dependent.                                            7  \n  620   The threshold-based layers are the deepest in the\n  621   network (L63/64 for 32B), consistent with late-                                            Sin\n  622   layer safety features (Wollschläger et al., 2025);                                        (Ha\n  623   however, R1-32B’s residualized selectivity is only                                         vid\n  624   3.0pp (section H), below the 5pp threshold of He-                                          ual\n  625   witt and Liang (2019).                                                                     spa\n                                                                                                   fra\n  626   Encoder-quality boundary. The HS advantage                                                 sul\n  627   is significant against 384d MiniLM (confirmed at                                           rea\n  628   7–8B; descriptive at 32B) but attenuated against                                           fer\n                                                                                               8\n\n=== Physical Page 9 last 20 lines ===\n  713   (up to 64), W (7 values), K (5 values), and                References                         \n  714   threshold are selected on the same validation set          Ryan Prescott Adams and David J.C. \n  715   (n=4–9 per-class at 32B, up to 2,240 configu-                Bayesian online changepoint detec\n  716   rations); cumulative degrees of freedom are sub-             preprint arXiv:0710.3742.        \n  717   stantial (section W provides convergence, cross-           Patrick Ahrend, Tobias Eder, Xiyang\n  718   validation, and bootstrap analyses addressing this           and Georg Groh. 2026. Safer reaso\n  719   concern). BA-optimal layer indices are sensitive             suring and mitigating chain-of-th\n  720   to the train/validation split, spanning 7–98% depth          LLMs. arXiv preprint arXiv:2603.0\n  721   across models and splits (section Y); for exam-\n                                                                   Guillaume Alain and Yoshua Bengio. \n  722   ple, OT-7B shifts from L16 to L2 and QwQ-32B                 standing intermediate layers usin\n  723   from L60 to L63 between 70/30 and 60/20/20                   probes. In Workshop Track, Intern\n  724   splits, a direct manifestation of the layer selec-           ence on Learning Representations \n  725   tion sensitivity that constitutes our primary find-\n                                                                   Tyler Alvarez and Ali Baheri. 2026.\n  726   ing. Threshold-based metrics are more stable but             reasoning break? step-level hallu\n  727   still vary by up to 4 layers. K=5 was selected               via hidden-state transport geomet\n  728   on the R1-8B validation set and held fixed (sec-             arXiv:2605.13772. Concurrent work\n                                                               9",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "4538b7c8-a2c1-47eb-86b7-79a9d208213a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor"
}
```

</details>

---


### Runtime record

_source line 2808 · 2026-05-19T13:36:29.963Z_

```json
{
  "parentUuid": "71df1919-0829-40f6-81a0-9ead26aa1928",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [
      {
        "content": "P0#1: Abstract rewrite",
        "status": "completed",
        "activeForm": "Rewriting abstract"
      },
      {
        "content": "P0#2: Introduction framework shift",
        "status": "completed",
        "activeForm": "Updating introduction"
      },
      {
        "content": "P0#3: 32B descriptive reporting",
        "status": "completed",
        "activeForm": "Updating 32B descriptive wording"
      },
      {
        "content": "P0#4: Graded wording replacements",
        "status": "completed",
        "activeForm": "Replacing count-based claims"
      },
      {
        "content": "P0#5: Garden-of-forking-paths paragraph",
        "status": "completed",
        "activeForm": "Adding garden-of-forking-paths"
      },
      {
        "content": "P0#6: K=5 wording unification",
        "status": "completed",
        "activeForm": "Unifying K=5 wording"
      },
      {
        "content": "P0#7: Five-step audit structural rewrite",
        "status": "completed",
        "activeForm": "Rewriting audit protocol"
      },
      {
        "content": "P1#8: HarmThoughts data characteristics",
        "status": "completed",
        "activeForm": "Adding data characteristics"
      },
      {
        "content": "P1#9: Selectivity orthogonal→complementary",
        "status": "completed",
        "activeForm": "Replacing orthogonal"
      },
      {
        "content": "P1#10: AUROC one-sentence mention",
        "status": "completed",
        "activeForm": "Adding AUROC mention"
      },
      {
        "content": "P1#11: Boxo discussion expansion",
        "status": "completed",
        "activeForm": "Expanding Boxo discussion"
      },
      {
        "content": "P1#12: C=1.0 statement",
        "status": "completed",
        "activeForm": "Adding C=1.0 statement"
      },
      {
        "content": "P1#13: Trace-level bootstrap statement",
        "status": "completed",
        "activeForm": "Adding bootstrap statement"
      },
      {
        "content": "P1#14: Add Azaria & Mitchell + Turpin citations",
        "status": "completed",
        "activeForm": "Adding citations"
      },
      {
        "content": "P2#15: Shelf-life caveat",
        "status": "completed",
        "activeForm": "Adding shelf-life caveat"
      },
      {
        "content": "P2#16: CP permanence discussion",
        "status": "completed",
        "activeForm": "Adding CP permanence discussion"
      },
      {
        "content": "Compile, page check, commit, report to Director",
        "status": "in_progress",
        "activeForm": "Compiling and checking pages"
      }
    ],
    "itemCount": 17
  },
  "type": "attachment",
  "uuid": "35e8c391-60ec-4897-87df-d8fe251f9a2f",
  "timestamp": "2026-05-19T13:36:29.963Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor"
}
```

---


### Assistant

_source line 2809 · 2026-05-19T13:37:01.322Z_

<details><summary>Logged reasoning block</summary>

```text
Looking at the output:

**Page 8**: The right column shows "7" and text starting with "Sin" (likely "Single dataset" = start of Limitations) AND ends with "8" (page number). The left column shows discussion text ending at line 625, then "Encoder-quality boundary" starting. So the left column has Discussion up through the Layer Selection paragraph, and the right column has Limitations section 7 starting.

Wait, this is confusing. Let me parse more carefully.

The two-column layout in pdftotext -layout interleaves columns. The left column text appears on the left side, and right column text appears on the right side of each line.


I'm seeing the Limitations section 7 does start on page 8's right column, which means the Conclusion must appear earlier on that same page. Let me trace through the page 8 text more systematically to find where Conclusion begins. I'm working through the page layout structure more carefully now. The left column of page 8 ends partway through the Discussion section with the Encoder-quality boundary paragraph starting, while the right column contains the tail end of the Conclusion followed by the Limitations section header and its opening content. This suggests the Discussion section spans across both columns before transitioning to Conclusion and then Limitations. Looking at page 9, I can see the Limitations section continues with hyperparameter configuration details, and the References start on the right column. This means the main text actually fits within the 8-page limit—Conclusion ends on page 8, and Limitations begins there too, which doesn't count against the constraint per EMNLP rules. The page_status flag is reporting the total document length, but that's not what matters for the submission requirements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35e8c391-60ec-4897-87df-d8fe251f9a2f",
  "isSidechain": false,
  "requestId": "req_011CbC1wnCdPnpHSg9w1vmZ3",
  "type": "assistant",
  "uuid": "046f6597-682d-4e86-817b-05ff72f0d901",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KufetvFPKGsAAmBvCyUHPD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1595,
      "cache_read_input_tokens": 157990,
      "output_tokens": 1442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1595,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1442,
          "cache_read_input_tokens": 157990,
          "cache_creation_input_tokens": 1595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1595
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

_source line 2810 · 2026-05-19T13:37:02.253Z_

Looking at the layout data: page 8 right column shows Limitations (section 7) starting, which means Conclusion ends on page 8. The "over_limit" is the total PDF pages (28) vs the max_pages check (8), but EMNLP only counts main text. Let me re-render page 8 to confirm visually.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "046f6597-682d-4e86-817b-05ff72f0d901",
  "isSidechain": false,
  "requestId": "req_011CbC1wnCdPnpHSg9w1vmZ3",
  "type": "assistant",
  "uuid": "93a374d0-d964-4800-a015-e1d923d205b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KufetvFPKGsAAmBvCyUHPD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1595,
      "cache_read_input_tokens": 157990,
      "output_tokens": 1442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1595,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1442,
          "cache_read_input_tokens": 157990,
          "cache_creation_input_tokens": 1595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1595
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

_source line 2811 · 2026-05-19T13:37:02.793Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_011EsthsxegnfvgCSWsnwySc`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.pdf",
  "pages": "8",
  "dpi": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93a374d0-d964-4800-a015-e1d923d205b0",
  "isSidechain": false,
  "requestId": "req_011CbC1wnCdPnpHSg9w1vmZ3",
  "type": "assistant",
  "uuid": "5c7ba989-b8f7-48d6-ab4c-c3cfb21039cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/paper_agent_bacd83c4",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "replicated-honking-meteor",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KufetvFPKGsAAmBvCyUHPD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1595,
      "cache_read_input_tokens": 157990,
      "output_tokens": 1442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1595,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1442,
          "cache_read_input_tokens": 157990,
          "cache_creation_input_tokens": 1595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1595
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

_source line 2812_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-19。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [Director 指令] [Patch] R18 审稿修订 — 16 项论文修改，0 实验  R18 Fresh Review Overall 3.0 (Findings)。以下修改全部需要在 DDL 5/25 前完…",
  "leafUuid": "5c7ba989-b8f7-48d6-ab4c-c3cfb21039cf",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c"
}
```

---


### Runtime record

_source line 2813_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent response to director callback",
  "sessionId": "6007b120-a1ab-45ef-9f2c-75b81f58a04c"
}
```

---


### Large event (continued)

````text
### Tool result

_source line 2814 · 2026-05-19T13:37:03.747Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_011EsthsxegnfvgCSWsnwySc`&lt;/summary>

```text
Error: result (921,361 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-paper-agent-bacd83c4/6007b120-a1ab-45ef-9f2c-75b81f58a04c/tool-results/mcp-agent-ml-research-pdf_to_images-1779197823740.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-paper-agent-bacd83c4/6007b120-a1ab-45ef-9f2c-75b81f58a04c/tool-results/mcp-agent-ml-research-pdf_to_images-1779197823740.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c7ba989-b8f7-48d6-ab4c-c3cfb21039cf",
  "isSidechain": false,
  "promptId": "bf44e86a-6a77-4d12-b438-d4d4b2ba2396",
  "type": "user",
  "uuid": "1e91e932-7904-4f64-bfc0-506e6ff50ca1",
  "toolUseResult": "Error: result (921,361 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-paper-agent-bacd83c4/6007b120-a1ab-45ef-9f2c-75b81f58a04c/tool-results/mcp-agent-ml-research-pdf_to_images-1779197823740.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-paper-agent-bacd83c4/6007b120-a1ab-45ef-9f2c-75b81f58a04c/tool-results/mcp-agent-ml-research-pdf_to_images-1779197823740.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/_pdf_images/main_p8.png\", \"base64\": \"iVBORw0KGgoAAAANSUhEUgAABnYAAAkjCAIAAACzq+aSAAAACXBIWXMAAB7CAAAewgFu0HU+AAqJiklEQVR4nOzdCbxV0x/38VMhU9E/lAalRGQWKlOpaNKgokhJA1HG/Mn0KAlJhn8TCkURoYkkY6VB80yTSvOsaFT3+T7n91ivbZ9p37tv9974vF+9et2z9zp7XHvvtX5n7bUiaQAAAAAAAABCiGT3BgAAAAAAAACHN0JsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJsAAAAAAAAQCiE2AAAAAAAAIBQCLEBAAAAAAAAoRBiAwAAAAAAAEIhxAYAAAAAAACEQogNAAAAAAAACIUQGwAAAAAAABAKITYAAAAAAAAgFEJs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0PHHH29pdHLvvffeJPWudJ3HuHTitCUucenSpWfMmOHmWhPOvn37tmvXzm35Nddc44sWffrpp+5wibZ/0KBBbq7q8965V1555erVq71fT35azZtvvlmsWDG3EGW/zZs3u7lPPvmkJqoCdvXVV1uC2Ji42bJli3Km2xe56KKLXCgtUzK2jobbVGVI1VXKRbkEuqILFy5sf//nP//xZSdV9d0eeaMbyQ9jkDOVMovqbubyMw4L69ev79ChQ968eWNfNPZasGDBZZddVqZMmd69e7/99ttXXHGFngXKM3ET6wLUTc+bJ6+//vqVK1cG2R5Vy+3+M3369JSJBw8erLuTrUt37+SJdWdr3ry59ybgpetIl1i9evU++eSTIGGOoUOHXnrppfZdLbNixYraAN1vdYHrQOlg6iItXry4S//ee+/Vrl3bPW1T6t69e8ptEBUYrrvuOne0c2BXDGEo1+l2GjfEFjDfOlYM01lIlMB+Hkj+sHMefvhhnWXv+TruuOMaNWrk/VFHjzCdcVcqM9WqVdMpC5kV9bzQcypTWsHroVC3bt0jjzwydjO05XrK3HDDDb169Yr7c6DZu3dvv379lPntK/pDRaBTTjlFH4855hiVRR944IEzzjhD/yffEpVSVEB95JFHwu/UP4OevFaQU/kqu7clh1IRrn379q5eEySMC2QNQmxAVlDxQiXg2PYsXbp00VPh448/to+qddvTNDYYl4QqM/qWSkIq3k2aNGnGjBm33HKLpqj0aQlUcMmXL9/JJ5+s/1XrVonKugBbsWKFikH6oirVs2bN0nRVno844giLoKVF29E0aNBAi2rSpMm33347d+5cVSpUbdi4cWNatDcxzerRo4cl1npVulJxSsvR9k+dOlXFMtesQMkinirTvHnzTjjhhBIlSrz77rv6W0dAZU1t3po1ayyBvh6JhifOO+88lYm1XxYvuPHGG5McipEjR6rYOmzYsJkzZ2p7unbtqvqMqnYuweLFi7VeFQE//fRT/T1gwACtVBVFrd0S6BhqLd7opI6eStKnnnqqa5ugnVLx+vPPP9eWT5w40Y62eyFRB03nWul1YFWSVoKBAweqnKRCsyXYtGmTDlGuXLlU1P7qL0GWLDfffLOmqEYxefLkKVOmqGalKpym6DBaAhV2dYJU6+jUqZPS6Lg1btxYCd54441EBy1d5zHW6NGj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3XXXuY9JQmzWqKdLly7eibqiLYSRgRCbbqTro1atWqXrQltiddeSJUvGNrqxvkojnq4VM8ZV0XU7+slDG6Ad1GWVWSE2nVl7s9U7AIW1xdOj36VZvXq1dTIgupnoxqXqSuvWrfPnzz98+PC06JNFy/E+xHVTtchFsWLFvotyPUWq+qSSg/dFWtWm7J5ctmzZlE1c7QeSJM96794lybeOvcsc++KhqvHaeItNmOwNsaUrK/pYWVHP7uBbHitRiE3H2XpjjPzV3Yd3+FH3tkSGae90fFy7JCvLRaKj8XpDLUH88ssvymk6196rwF6kjXgaywe5Lvbv369ykeVGy+dajhUI9WhWMdumN2/e3C0hyGKNXa3ea0QXlP1i6nq9WLly5YIFC+wq84bYzGmnnRaJ96KovTMRidd1psohOqSxP8HG0qotx5566ql33HGHKx+68XOrV6/epEkT1+2s7g/WyNHb0UTwo2E/9EbivSga5ECleUJs5cqVe+6556xIrGeTnkqRaITatZBCNlJGsiiYMnaiNCpGxkbK9NSwRmqiS1uXof3t63/J4neSgZ4WDgVCbMChZWOx+QYZTPurc3HVOuyjnkZt27a1oc0dVa1Vl0j0IkZa9L5z3HHHNWjQQOVy10eMHjze/gisn6a446n37t27YMGCbnVHHnnktdde632L5/PPP3e/VUq+fPn0FZulLXej1B88ePCqq66yjs+Niob2c3datM15njx5vAWRtGhHUa48p6e+iobeTuK9CzfWGLBVq1aJDkVaNMCho2HLVLlk1KhRKtB7X4bVkVT9wW1k/fr1dV70x7Bhw7zLUb3OErjQiZf3F36Va3WoI56XJeMe7csvv9zXkcq4ceNUhbBfnl3rpORLTosO76iyo75VoEABnXSVpbRY3ytFKq1aJx3OhRdemKTn4ODnMS6dNVVvVKFyXznhhBNc2S7uqbfCkLemrbqllYSMluZtEaNVNG7c2M1VAdq1djFBTuuyZctq167tPSzFixfXrtlcqybFfY0o1osvvmglPKNa9+TJk93c8BlbmccNWahzrSKmNSNygbnYPGYZw35dt5pk7B4lP4wBz1TyLJquw4icI3mowpogSaIel2xukj4K06KDDyqNC2p7zZw5s3Dhwt4eCRKF2LZt26Zbn64+3y8fYj8/ZCDEFkvXY+vWreN2nOzujUlePtLF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2l1HeMobmzZt8qXRRLtTFS5cOL3teuyLsSE23dg1Xf/7pts4J942a8EP8rhx42zikCFDbIpFSIMfqBEjRlgyX38FS5Yssendu3dP1+7jUNBNyRqaffPNNyo86Maoe/j48eMtNGY/OO3Zs8catVnfatNj2G9Irts15a4dO3Yo87smbDlnAEBCbAAAAP9SbkCDG264IVGaadOmnXzyyarnu/7UVdKtVq2aqkC+Ws2jjz4aSUp13eTbkyjEluZpq1WwYMEHHnhAteiePXuWLVtWG2bTTz/99AcffDD58lXzdO+4Kb1q+8uWLVu4cOHXX3/92GOPaYrNOvfcc31dLDu//vqre2O0evXqOgLewNbatWuffPJJqxxeeumlvo603VtR8swzz0yZMkWr1i5rG1SHVO3iiSee0B5ZguADRFatWtW+4iqiaZ5zoapvp06dWrVqVbp0afcu59VXX63j+emnnyrlu+++axO9fbc7rjlJJPpScNGiRbWF5cuXr1mz5iOPPOLbyDlz5rjhJiPRftnOOeecY6K8b8AlocVGkr6yapLn29tuuy3i6ScriAyE2Owrxhtt8XItd+T555/3zgqfFdP+CgPpzLoGHaKqpn03tgFUXMoGbiOfffbZYHv//+gatAB3JBpUHT58uHbBtmTz5s3ad+XMMmXKfP/99+4rqlpbv37K/8kX7lonRYINXapLz90KjGXFIkWKeHNp8OvChdh0GF1LPd36WrdufdRRR/ni0cEXq7tWrly53Ebmy5fPRvnQte/bI7c7vpfrdZez6Q8//PD777+vu9Dy5ctjD0iXLl0iAUKZPlu3brXbl687Qu24ngJ2E/AFfC2gJm5okeBHY8uWLfaS8hlnnPHhhx/qIOjebgsJeKBcez394Z3+ySef2PQwA7AgE+kK/TYeF3JNlMCxQHmiZCozeG+D2YsQGwAAwL/OK6+8opqPG14gEo1WPP7447GxLVmzZk2lSpVKlSrVvXv311577ZJLLjnvvPN8YQXX6iSJlFGPJCG2tGg/6/YSkznnnHNmzZpVq1atQoUKdejQYerUqUmW/Pnnn9evX98bAPJSXa548eKVK1fWMVHdLGUH2CrQ16tXz46eqoglS5a88MILrbd+LUcLUQLfwbnyyitTHh8n4HuvqoW69+ls1ffff7/Vt//44w/3dm3u3LkbN26sk6j90kGzia1bt543b97NN9/s+uGSOnXq+CJBixYtstYrcanS62uWqLWozu9ePJSGDRsGH7PPmtS1adMmUYKU+VbVsBNOOEEnNOCYrSZdIbY777zz3HPP9R6HI488Uns9cuRIl6Zfv346Nd4YgZQvX75r166ZmBUfe+wxfUW5yztx69at9oZpyjdzP/300ypVqrje4syll14aPCqxc+fOLl26nHnmmd4skTdvXttZnSxvAFrXr73kaEesbt2648aNi12mTmWTJk0soONcdtllEyZMSL4xyvMtWrRwrZ+0X8pIOhq+NCmvC2v25UJs3bp1u+CCC84444yqVavqwCqlcmnsqgMuNi3adMtFV0XHxPcuZ6dOnexdS6PbywMPPOACWGvXrtXG2KzSpUsnejnu66+/jqRzPApdR7qxu/U2atTIgt29evXS/d9Nv/jii5WNNf3DDz908f1IdAxTi5ym62jomWITdeLuu+8+b5u75Adq9erVt99+u7t9KUfp7C9evFgHql27dtabm9EGxL4+jKynbPDdd99542ILFixwtzg9JoKE2NKi7577lqOSQMBm7FmDEBsAAABSmzt37uDBg4cOHapqWzb+XKwa5jfffONabC1ZsiS7ejjev3//tGnTRowY0b9/fx2Zr776Kue8qGJ0cL796zUc8/vvv3///ffBw09KWatWrWlRI0eOHDRoUN++fV988cWnnnqqZcuWhQsXvvLKK2O/tXfvXqVX5T8D47upepw/f35tZ3q/aDZt2tSrVy+djox9/TCye/fu00477aqrroq9GHfs2JHF3RItW7bsiy++ePvtt3XkleWCjFFwiGzZsmXChAnTp0+P7RDQCXJdePti0xHWV3Tb0f9JVp2uy23evHlaYMYOlHZt8uTJOsVJ7sNdu3atUKFCBhaeWYIfjZUrVypl3LEj08IdKOQ0f/75p060zriyQZjRP/WI2bhx44oVK5QxdLvLxC3MFITYAAAAAPitWrWqRIkSSXqd27p162mnnZa5K1Xd6cILL0z5IiEee+yx/Pnz//LLL9m9If9MSYY7yPkOHjxYsmRJ18EZgKxEiA0AAACAn40hmKRB2caNG2vXrp3p612+fHnJkiVjX8eDM3fu3AIFCkyaNCm7N+Qf67AOsX300UeFCxfev39/dm8I8G9EiA0AAADA32zYsMFCDEOHDo2bYMeOHQ0bNkzZQ1bG/PTTT2efffbs2bMPxcIPd4sWLTrrrLO+++677N6Qf7LDK8S2d+/eQYMGffzxx2vXrp0/f/5JJ53Us2fP7N4o4F+KEBsAAAAAPxvTMFeuXM2aNRs2bNj06dMXL148adIk1eTbtm17zjnnHNLow6pVq2rVqvX5558fulUcjsaPH1+zZs24g0giE40dO9ZCbO+88052b0tqL7/8csTjoosuyq4eKgEQYgMAAADgt3bt2sqVK0di5MuXr0uXLhkekSC4gwcP0teYz8qVK7NxsJF/ifXr19erV89ye6VKlZYuXZrDI1YDBw50l2fp0qWTD8sA4JAixAYAAAAgvkWLFvXq1atjx47t27fv2rXrmDFjsiC4BmSX2bNn3x3jvvvuy+7tSuHjjz/WRvbr12/btm3ZvS3AvxohNgAAAAAAACAUQmwAAAAAAABAKITYAAAAAAAAgFAIsQEAkG1+//33mrVqNmnaJId3pZyINnv9+vWbNm9K17f27dv366+/7tq1yztRh2Lp0qV79uxJ+fW9e/eujtIf6dtcAAAA4JAhxAYAQLYZPXp006ZNa9epPX369OzelvT5888/Bw4aqC2vWq2q/rW8o+WCBQvc3L59+9p09++25rfZrBkzZtRvUL/6ddWvu/66Tz75xH3l6c5Pt27TWotNstK1a9cqWY2aNWyZWshjjz+2detWzer4cEdNub3l7YdmdwEAAIAUCLEBOdeECRMGDx6c3VsB4BC6p/09A94a8Gy3Z7s808VN/OWXXwYOGqh/27dvHzRoUOfOnd96+62dO3cGmZtlXn/99arVqtauU/uNN9548skn9XedG+qs37De5lqITVNubnKz/XPDsTW7rVmr1q327t3b9dmu1a+rvmXLFk2cPn260s+bNy/JGlesXFGvfj0X0ev4cMdbbr1Ffy9dujSNEBsAAACyGyE2IOe66667ihcvnt1b4XfgwIE/ElPlv9/r/fR/kjSH6QtxQKZbsWJF1WpVf/311+nTp9eoWWPHjh02/dtvv/3/gaSWLV0rsLZ3trUWXsnnZhmLdvXp2yct2qKtfoP6+ti7T2+bayG2AQMG+L61b98+TX/uuef094gRI/T33LlzNbHF7S2ef+H55Gu89757lb5a9WrjJ4x3E6dNm7Zp0/97TZUQGwAAALIXITYg58rJIbY9e/bsjmfFihX9Xu+n/+PO1bcIsQFO375927dvnxa9rG666aYRI0bYdBdEe7bbsxs2bBgxcoR9HPvl2JRzs8aff/5ZrXo1rXTIkCE25dZmt+rjXe3ucrumj23atnns8ce6v9h9zBdjXASwSdMmSqZd7vFSDy1k06ZNQ94fUrdeXXvfM5H1G9a7vY6bgBAbAAAAshchNiDnyskhtt27d2egFZt9ixAbkBaNUjVs1NCF1fr27duuXTv72wXRVq9ebVOa3tJUH3v27Jlybpa5o9Ud1npu48aNU6ZMsU266aab3O74+mJr3769jU4w8YeJtevUrt+gfrXq1d599931G9bXql3LjsOvv/66dOnSffv2xa7O3iTVP3fEfAixAQAAIHsRYgNyLkJswD/YD5N+uL7G9b/99pt9XLZ8WdVqVZctW5bmCaJt377d5rZp20YfO3fpnHJulpkxY4YbdsD9u+XWW2zulClTpk2btm3btk2bN/V4qYfNHTNmjM3duXPngoUL7AXP//N//s+dd925Z8+ejg93rH5d9dp1at/a7FYXPXS0tP8fYhtJiA0AAAA5ESE2IOcixAb8gz0pTz3pndKmbZtevXqleYJoU6ZM0ccdO3bUql1LH/v3759yblZavXr1oEGDerzUY/jw4U888YS2oWPHjrHJdu3aZRv8v17/8836cdqPmr5w4cIxY8boj2+/+3bT5k3Vr6verVs3X8p169bZQmJnGUJs6fLll1/efffdyceXwL/H9u3bH3300VdeeeXgwYNZttIgmXDjxo1vvvnmnXfe2ahRo1atWukOuXnz5izbwpxsxowZKlNl4gJ1G4/bgjiJpUuXvvPOO//973/btWsX/LsqIo4YMeLll18eMmTI3Llz07+lOcjy5cs//PBDZcvvvvvO9aaayOLFi4cOHaqrbNSoUeGzcQbOVxi6M4wfPz51OgCE2ICcjBBbxqgccADIbJlb89y6dWv166p/8ukn6z107TS4sYEKzS6IVr9B/R49etgrmdddf92aNWvSPCG2uHOzjPeAaOPr3FBHm/Hp8E9tiqp/LsH8+fNtgwcNGuRdwt69e5u3aK5d0N9v9n/TRn7Q341vatzh3g6xa9REG+5gwoQJbuLceXMZ7iC9du3adfzxx0cikfLly2f3tiBH6Nq1ayTq888/z5o1BsmEr732mkpB7777ru4Mn332WaFChZRe/69cuTJrNjJn0q21c+fO7dq1y6whboYPH37++efr2LqW0cnpIdWnT5+zzz67YMGC7du3/+abbwJuiQqHjRo1Klq0aKdOnXr37n3PPfccd9xxVapUWbhwYbg9yAbKk5UrV454nHDCCW+88UaixPXr1/cmVuZ/5ZVXMrbq9J6vzPLoo4/eeeedmRvYBf6RCLEBORchtvTSwufOnztj5gz+8e9Q/Ju/YP6ePXsyJa9++OGHvlcs3b/xE8a7INonn35Su05t/aH/x3zx/9+yTD43y4z9cuwDDz7Qu0/vnj172nCibe9sa72tSd16dZvd1uyZrs882+1Z28iatWpaBM15b/B7+qK9Kjtu3DgbsWH16tXVr6ve/cXusWtcsWKFDWOqf61bt37kkUduufUW/b106dI0QmzpoSp6yZIlVUNr0KBBdm8LcoR33nnHav5Z1qooZSZ87bXXNHfUqFFuirYtf/78mvjee+9lzUbmQLrH1qpV69FHH82UpenwXnTRRS7uEyRkM2XKlLJlyypx3bp17eeNgDZs2FCkSJELL7zw999/dxOXL1+uc1q0aNGNGzdmZAeyybRp00444YS8efOec845pUuXzpUrlzuGsadGD75TTjmlQoUKL7744oABAzp06HD00Udb4sGDB6drvRk4X5mrT58+1157bWYVhIB/KkJsQM5FiC1d/vzzzxkzZ8yaPWvd+nVbgMy2Zu2aWbNmzZw189DFiB0XRNu1a5eumpUrV+qPgHOzzMQfJtasVdO25Poa13ft2tX1KyfPPf9c3Xp1Xdyww70dFixY4P36unXr9PXRn422j7p+O3furJTVr6vepm2bRNWttWvXPt35adcHnBI/9vhjNhQpIbZ0Ud3siy++yMr3jJDDTZo0acmSJVm5xiSZcNu2bfny5VNl3jd9+vTpulGkfCPvn0r3ybp16zZp0iRTlvb555+PHj161apVF198ccCQzbBhw4466qjcuXNnoF+CG2+80RczNU899ZSmx+1kINa0adPSu95MpwdumTJlmjVr5kbB1rPv7rvvtmOYK1euyZMne9NXrFjxtdde805ZtGjRscceq8TnnXde8PVm4HwdCo8//njNmjWzoCAEHL4IsQE5FyG2dFGJfMbMGa4RDZDpdu/ZrTzmDSQdIt4gWnrnZqX9+/evW7cuUYxPV7pqIKoPxJ2rC3bp0qW+1281cf369SnfydVl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5oILLrDpp512mi4QVWv1DNJE+xngpJNOim1BM2jQoLx587700ku6R61bt65Bgwa2hDx58uSP0pUbuw26xt24eOeff/7o0aOPO+443aYssCKqdbv7wPr16++9995TTz3VZn3wwQe680T+8sADD1iy4cOHly1btk+fPtOnT1d9rEqVKppbsmTJ2bNne1et2ql2yv1g0LdvXyVTpdqbJuWiPvzwQ91jc+fOremq0enWcfLJJ9v2aKJuuSr3u0EDdV/17b41YPnoo4/cFN3nGzZsWLdu3S+//FIrffnll6039Pvvv9/7RW12gQIFOnfubB91v9JhVMpE5zrILutEt2vXrmDBgra1vXr18n1d21ahQgVlBt02dT/UyTrmmGMssc6aTrE2W7fNli1bHnXUUTZd5+65555TsvLlyyvb2ETvEyRRJtQ99r0om1WzZk37+O677/bv3/+ee+6x6ZUqVYrdze7du2tR/fr1U4bZtWuX9eamg/P999+7NJpeuXLl448/3lXjVV2PRF9+dI+DjF0IQdaeFjiXxtKzUimfeuqp5MlMpofYrJQSib6mOnDgQB3DwoUL6+Do1L/11lsB16JCjjuwyhjLly8fP368DmadOnV27tyZ5IuqZqtAYhnp8ssvHxY1ceJEl0B1bF0IWvisWbOUFZVjdVtQ4hIlSvja5gcRJsSmm6G+qyyUJI1ula1bt45tJh9ckvOVrltruhL7dO3aVQkuueSS9G78obj5Z24GwCGia/bbb7/VA9FFltesWfNDlI20o5qFi6+5oriLsi1btsymzJgxw6asWrXKpiif2JS45Y1sQYgNyLkIsaVLkBDbY58tTBRfs39vTI7/67TPK6+84i1YqKysuoSeDfqjWLFiqnGdc845qgjFjs729NNPq6javHlz+wFWW1u0aNHBgwdH/gqxPfTQQ61atUqLPjCsTqKyxSmnnFKqVCn3+qRWba3AkoTYVO9Vcd8KcG+88Ub9+vVVf0sZYps8ebIKN1Zo++yzz0488UQXnFLxxfsGqwqIKmCpOuENsWmlqrqo/lCmTBntRdwQm+qWKlm6j8FDbCqO66NvVMq06MukWuNNN92klZ5wwgnaU+Uxm6XyVpEiRVQ7UgHOtUeLe44GDBignVVpT8fZu0eFChXyVo8JseEfYOXKlbqOVPfwRTfSoq//VKxYMRLtIUh1YFeJHT58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9vZGmHfffffLL7/EtxJJIhk3bhxFBjEx+92///67V69ePj4+dIeRI0cah4+KihowYEDRokUp/K+//uporJ2NSdITExPTrVu3ggULWsRIkyYN3OyePXuy7FKQLl26Dz/8sH///gqlsnfv3iVKlND8ioeHR548eZo2bTpv3jypuBngTKN47Xj8+HGGDBmQ2PLlyyd3XIQ4ffp0nTp19CQ2dAW7d++eOXMmlWCRIkVWrFixd+/ef/75RxEyNjZ26NChFAw3XLBggfqnDheC/r9NmzZeXl7GwfAu+Oqrr0qXLo23wxdffPHRRx+hjT948CDxIgYWLVqUO3fuFi1aIN8mTJhQuXLlTJkyTZ482eArv/zyS7ly5VBz0qdPjy9GR0fzV2/fvt2uXbuUKVOGh4cnaswlEimxSSQSiUQikbzt1KtXD06dt7e3QZjIyMgsWbKMHDny0aNHiRqZn3/+mZxMB9zLhw8f3rhxA56YoLAVHx+PdMGBdLnEZjYmycWzZ8/KlClDkaxYseLly5dvcFy8ePHEiRNTpkxB0cM7pa+8ePGievXq9JWyZctGRERcuHAhICDghx9+KFy4MNlr1qwZFRXFP6hBgwZ06b333kP4mzdvnjx58rfffvP398edYc+cObMbzvVzE5xpFK8dqGAFChRAYps3b57ccbHP7t2733///UuXLhkHO3z4MJXgsmXLDIINGjTogw8+SIzptERMTMwff/yxePHiLl26oFFTezQIf/fu3Y8++qhq1ar//vsvWdBjoM2ipSsauAsZP348IrZy5Ure2L9/fxgnTJigDv/kyZOOHTviavv27dHxXrlypWvXrkhdz5490QPjbm3btm3UqJGnp2evXr0SKc4SCUNKbBKJRCKRSCRvNXCZ0qdPD/8EbolemL/++qtevXr4P2midOjQoQsXLjj89bi4OFPCFvN+XSixORaTZAFePUXy888/1wuzZcsWBGAfkRz6SufOnflgL1686Nu3L10qVKgQPxdyypQpZG/cuLHi5nv37iWVDehNBXp7uHz58t27d9V2JxvF60VsbOyuXbsMVh+Lc+zYMedvoseBAwcyZ878999/2w35/fffUw2/du2aZgD0w1988cXw4cNdkmo9kBv+/v7Dhg3bv38/uju7ElunTp3SpUunqJDx8fHZs2fHGyExYhgWFpYiRYqyZcsq7I8fP06TJg06ivv37ysukeLv5+fHL6OuVq3a8ePHN2/evGfPHrSpxYsXZ8iQQXBVrETiDFJik0gkEolEInmrYQLT8uXLNQMsWLCgY8eOib0yyIX8+++/poQteGKJJLGZjUmyMHr0aLsSG3zXbNmywbWmj0wvUEhsICEhoWTJknT1u+++Y3Z24lCTJk3U9+/duzddrV27tivS9Lry9OlTX19fEclGIsKWLVv8/f0T6eYRERGZMmUaMWKESGCaKVywYEHNq1FRUY0bN965c6dLI2iH9evXG0tsR48eRYB27dqpL9GcssQ4OmzGjBm4c4sWLdSXPvzwQ1z6448/eCN1LB4eHpcvX+btzZs3v379Ov396NGjXLlyTZw40eWxlUjUSIlNIpFIJBKJ5K3GYHrF48ePu3XrNmvWrGSJmMNIic0UIhKb1eZvP3/+nP42kNisL91vUK1aNWY0lth++eUXupoxY0bnUvN6Q1KjlNhcwoULFzJlyqQp1riEGjVq5MuXT71tpRrjmcL79u1r2LBhREREIsTRCLsSGzoEBNDs/9etW6c5I9V5evXqhTv7+PioL73//vu4FBgYyCwxMTEoYovWmuKSJUuy+YCjRo1CSbG1rpLk4vr163iP7N+/H4V48uTJGzduKAKcPXs2TAu9VckUXvAojCRDSmwSiUQikUgkbzV60yvOnz//ySefHDp0KFli5QxSYjOFXYktISFBYTGW2H788Ue6yu+kbiyx/fbbb3Q1ZcqUbK7c28bChQspE6TE5jz37t2jQzYSSWIjUXjIkCEigQ1mCk+YMKFv377JUuftSmz58+dHgNWrV6svHThwAJfSpk3LZHdXgQyhvEIO8/bLly+nSJEie/bs/LkoTJrfs2cPH/jp06cfffQR/X39+nXEc8WKFa6Np8QsoaGhf6o4e/YsC/DixQt1AAKjEfUNb926RVfVUl3yIiU2iUQikUgkkrcXvekVGzZsaNas2e3bt528/2+//dahQ4f2L+nRowe/pf2yZcs6duwIO8KwTbgSEhK2bdvWpk0bzX3BY2NjR44cWbt27bx581avXn348OHqX7CNhS14X1OnTv34448LFixYoUKF77//Xm8vtps3b/br169JkyatWrVCfMaNGzd+/HhTyTeOCVyObt26FS9evECBAkWKFMEj9u/fzwcYMWIEyzpkEQoFxo0bN7bn6NSp05Yt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
```

---
