# Research conversation: [系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director  — Part 25 of 46

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

[← Part 24](part-024.md) · [Transcript overview](../research-conversation-director-main-agent-post-to-director-director-main-agent-post-to-director.md) · [Part 26 →](part-026.md) · [Structured JSON](../../../sessions/23/233efc253e1583c5469f.json)

## Round 297

### Assistant

_source line 5788 · 2026-05-17T15:47:28.476Z_

Let me check the rendered pages directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9a80127-02e4-40f7-8e21-09ca98d81e33",
  "isSidechain": false,
  "requestId": "req_011Cb8QJmNQF1dupKuXi6ckb",
  "type": "assistant",
  "uuid": "421744cc-01ac-4eaf-8198-5a1f8e033ed1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PG7L8QCRNSnmTNZnHeVnjq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 55727,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 541,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 55727,
          "cache_creation_input_tokens": 541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 541
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

_source line 5789 · 2026-05-17T15:47:29.131Z_

<details open><summary>🔧 Tool call — Read · `toolu_01666NXcQ94cuSS5WnPTNzwn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "421744cc-01ac-4eaf-8198-5a1f8e033ed1",
  "isSidechain": false,
  "requestId": "req_011Cb8QJmNQF1dupKuXi6ckb",
  "type": "assistant",
  "uuid": "9e269012-f700-4349-8bf2-ee75823bbaae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PG7L8QCRNSnmTNZnHeVnjq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 55727,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 541,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 55727,
          "cache_creation_input_tokens": 541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 541
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

_source line 5790 · 2026-05-17T15:47:29.523Z_

<details open><summary>🔧 Tool call — Read · `toolu_019eoCpZmPpwWHib3W7iJov3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e269012-f700-4349-8bf2-ee75823bbaae",
  "isSidechain": false,
  "requestId": "req_011Cb8QJmNQF1dupKuXi6ckb",
  "type": "assistant",
  "uuid": "b3c7e656-0a0d-4f48-986d-114afaac671f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PG7L8QCRNSnmTNZnHeVnjq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 541,
      "cache_read_input_tokens": 55727,
      "output_tokens": 227,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 541,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 227,
          "cache_read_input_tokens": 55727,
          "cache_creation_input_tokens": 541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 541
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

_source line 5791 · 2026-05-17T15:47:29.734Z_

<details><summary>↩ Tool result · `toolu_01666NXcQ94cuSS5WnPTNzwn`</summary>

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
  "parentUuid": "9e269012-f700-4349-8bf2-ee75823bbaae",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "3adbf225-0508-4bb5-ba40-fc1ac1310b27",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 474892
    }
  },
  "sourceToolAssistantUUID": "9e269012-f700-4349-8bf2-ee75823bbaae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Runtime record

_source line 5792_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch — 页数压缩 + 附录重组] 三项修改，目标：正文（Abstract 到 Conclusion）严格 ≤ 8 页。  **当前问题**：Conclusion 结束在第 9 页右栏，超标约 1 页。  ---  **1. 正文压缩（目标省 ~1 页）**  具体策略（按优先级）：  A) **Cross-model per-class 表格移到附录**（省…",
  "leafUuid": "3adbf225-0508-4bb5-ba40-fc1ac1310b27",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Runtime record

_source line 5793_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent callback function implementation",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Tool result

_source line 5794 · 2026-05-17T15:47:30.251Z_

<details><summary>↩ Tool result · `toolu_019eoCpZmPpwWHib3W7iJov3`</summary>

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
  "parentUuid": "b3c7e656-0a0d-4f48-986d-114afaac671f",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "63277238-2922-46e7-81d8-a653a630f210",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 513045
    }
  },
  "sourceToolAssistantUUID": "b3c7e656-0a0d-4f48-986d-114afaac671f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Runtime record

_source line 5795_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch — 页数压缩 + 附录重组] 三项修改，目标：正文（Abstract 到 Conclusion）严格 ≤ 8 页。  **当前问题**：Conclusion 结束在第 9 页右栏，超标约 1 页。  ---  **1. 正文压缩（目标省 ~1 页）**  具体策略（按优先级）：  A) **Cross-model per-class 表格移到附录**（省…",
  "leafUuid": "63277238-2922-46e7-81d8-a653a630f210",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Runtime record

_source line 5796_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent callback function implementation",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Assistant

_source line 5797 · 2026-05-17T15:47:57.462Z_

<details><summary>Logged reasoning block</summary>

```text
Looking at the images:
- Page 8: Contains Discussion section (section 5) ending partway through the page, then the bottom has the rest of Discussion
- Page 9: Contains Limitations section and the beginning of Section 6 Conclusion, which continues and fills most of the page

So the main text (through Conclusion) extends to page 9. The Conclusion is on page 9, not page 8. I need more compression.

Wait, let me look more carefully:
- Page 8: Has the bottom of Results (Table 4 / baselines, Downstream Utility section 4.4), then Discussion section 5


- Page 9: Has the rest of Discussion (Granularity and robustness, Instruction tuning), then Section 6 Conclusion, then Limitations

The Conclusion is currently on page 9, but I need to compress the content enough to push it back to page 8.

Looking at the page breakdown, page 8 ends with the Discussion section starting, while page 9 contains the remaining Discussion subsections, followed by Conclusion and Limitations. Since the 8-page limit includes everything before the bibliography, I need to trim enough material so that the Conclusion section begins on page 8 instead of overflowing to page 9. Looking at the page layout, I need to figure out the exact formatting requirements for EMNLP. The Discussion and Conclusion are taking up too much space on pages 8-9, and I need to get the main content wrapped up by page 8 so Limitations can start fresh on page 9. That means I need to cut roughly a full page of material, which is significant. The Discussion section is the longest part here, so that's where I should focus my compression efforts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63277238-2922-46e7-81d8-a653a630f210",
  "isSidechain": false,
  "requestId": "req_011Cb8QKMzkPwL3akyTft7r4",
  "type": "assistant",
  "uuid": "9c9790ae-bd7c-416b-9f75-2cb17963570e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168KGjVEcZVF88Gv9itrAzu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1002,
      "cache_read_input_tokens": 56268,
      "output_tokens": 1142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1002,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1142,
          "cache_read_input_tokens": 56268,
          "cache_creation_input_tokens": 1002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1002
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

_source line 5798 · 2026-05-17T15:47:58.426Z_

Main text overflows to page 9. Conclusion and Limitations are on page 9 instead of having Conclusion end on page 8. I need to check page 7 as well and assess what further compression is needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c9790ae-bd7c-416b-9f75-2cb17963570e",
  "isSidechain": false,
  "requestId": "req_011Cb8QKMzkPwL3akyTft7r4",
  "type": "assistant",
  "uuid": "5d1e91f8-c25e-492c-ae29-33b16f47dd29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168KGjVEcZVF88Gv9itrAzu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1002,
      "cache_read_input_tokens": 56268,
      "output_tokens": 1142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1002,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1142,
          "cache_read_input_tokens": 56268,
          "cache_creation_input_tokens": 1002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1002
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

_source line 5799 · 2026-05-17T15:47:58.785Z_

<details open><summary>🔧 Tool call — Read · `toolu_011obAMV6aVF98t4NJp1NTrW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d1e91f8-c25e-492c-ae29-33b16f47dd29",
  "isSidechain": false,
  "requestId": "req_011Cb8QKMzkPwL3akyTft7r4",
  "type": "assistant",
  "uuid": "0ea0baad-24b7-4b21-999a-62b2eba3389b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168KGjVEcZVF88Gv9itrAzu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1002,
      "cache_read_input_tokens": 56268,
      "output_tokens": 1142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1002,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1142,
          "cache_read_input_tokens": 56268,
          "cache_creation_input_tokens": 1002,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1002
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

_source line 5800 · 2026-05-17T15:47:59.319Z_

<details><summary>↩ Tool result · `toolu_011obAMV6aVF98t4NJp1NTrW`</summary>

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
  "parentUuid": "0ea0baad-24b7-4b21-999a-62b2eba3389b",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "655cbe4c-2a07-4994-a667-1b675b6ace0d",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 463986
    }
  },
  "sourceToolAssistantUUID": "0ea0baad-24b7-4b21-999a-62b2eba3389b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Runtime record

_source line 5801 · 2026-05-17T15:47:59.324Z_

```json
{
  "parentUuid": "655cbe4c-2a07-4994-a667-1b675b6ace0d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "42c91813-29f1-489e-90c6-df2dd8cec7ae",
  "timestamp": "2026-05-17T15:47:59.324Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

---


### Runtime record

_source line 5802_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch — 页数压缩 + 附录重组] 三项修改，目标：正文（Abstract 到 Conclusion）严格 ≤ 8 页。  **当前问题**：Conclusion 结束在第 9 页右栏，超标约 1 页。  ---  **1. 正文压缩（目标省 ~1 页）**  具体策略（按优先级）：  A) **Cross-model per-class 表格移到附录**（省…",
  "leafUuid": "42c91813-29f1-489e-90c6-df2dd8cec7ae",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Runtime record

_source line 5803_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent callback function implementation",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Tool call

_source line 5804 · 2026-05-17T15:48:08.884Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bym8benAA2GefmYetWc3yy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42c91813-29f1-489e-90c6-df2dd8cec7ae",
  "isSidechain": false,
  "requestId": "req_011Cb8QMWKNFmDhL1wgroiB1",
  "type": "assistant",
  "uuid": "e47d54a4-845a-418c-8bdd-3eb07f5679df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NK1SuFU4QSLLyo2ZD9iPJK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 57270,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1624,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 231,
          "cache_read_input_tokens": 57270,
          "cache_creation_input_tokens": 1624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1624
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

_source line 5805 · 2026-05-17T15:48:08.889Z_

<details><summary>↩ Tool result · `toolu_01Bym8benAA2GefmYetWc3yy`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced ordinal generation depth estimation and documented a differential depth response across eight base-model generators from five families: recursive generation induces a systematic location shift in the token-level NLL distribution while preserving distributional shape, and this structured drift is detectable with a lightweight 7-feature ensemble (3-class F1\,=\,0.809 on cross-model chains, 0.762 under LOGO).
5	Despite this detectable drift, depth-aware data curation is practically equivalent to random subsampling at equal sample count (TOST $\pm$2\%, $p < 0.001$) within chains of $\leq$4 generations as measured by perplexity, establishing that detectability and downstream harm are decoupled in this regime.
6	
7	Two boundaries define the scope of these results.
8	First, instruction tuning compresses the distributional variation that fingerprinting exploits; extending to aligned models requires disentangling format-induced and depth-induced drift.
9	Second, while the signal generalizes across generators up to 8B parameters, frontier-scale models (70B+) with higher fluency may further compress feature margins.
10	All code, data, and trained models will be released upon publication.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e47d54a4-845a-418c-8bdd-3eb07f5679df",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "cd9eb81f-ff8f-42a7-b847-8eb818b2cc1e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced ordinal generation depth estimation and documented a differential depth response across eight base-model generators from five families: recursive generation induces a systematic location shift in the token-level NLL distribution while preserving distributional shape, and this structured drift is detectable with a lightweight 7-feature ensemble (3-class F1\\,=\\,0.809 on cross-model chains, 0.762 under LOGO).\nDespite this detectable drift, depth-aware data curation is practically equivalent to random subsampling at equal sample count (TOST $\\pm$2\\%, $p < 0.001$) within chains of $\\leq$4 generations as measured by perplexity, establishing that detectability and downstream harm are decoupled in this regime.\n\nTwo boundaries define the scope of these results.\nFirst, instruction tuning compresses the distributional variation that fingerprinting exploits; extending to aligned models requires disentangling format-induced and depth-induced drift.\nSecond, while the signal generalizes across generators up to 8B parameters, frontier-scale models (70B+) with higher fluency may further compress feature margins.\nAll code, data, and trained models will be released upon publication.\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  },
  "sourceToolAssistantUUID": "e47d54a4-845a-418c-8bdd-3eb07f5679df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool call

_source line 5806 · 2026-05-17T15:48:09.375Z_

<details open><summary>🔧 Tool call — Read · `toolu_011PAJMKU5zE32WRZznk3qc8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd9eb81f-ff8f-42a7-b847-8eb818b2cc1e",
  "isSidechain": false,
  "requestId": "req_011Cb8QMWKNFmDhL1wgroiB1",
  "type": "assistant",
  "uuid": "75745bd3-f016-4317-8c4c-0ecaee21ba3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NK1SuFU4QSLLyo2ZD9iPJK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 57270,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1624,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 231,
          "cache_read_input_tokens": 57270,
          "cache_creation_input_tokens": 1624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1624
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

_source line 5807 · 2026-05-17T15:48:09.574Z_

<details><summary>↩ Tool result · `toolu_01JPwSCfC3BXJ2WgDjKyq1Kt`</summary>

```text
1	\section*{Ethics Statement}
2	\label{sec:ethics}
3	
4	All texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.
5	Our method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.
6	Individual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.
7	We acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).
8	We encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aab4f0bd-3b77-4c39-9547-093c44adad7f",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "1d469723-7da7-49bf-b2b8-647352064eaf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/ethics.tex",
      "content": "\\section*{Ethics Statement}\n\\label{sec:ethics}\n\nAll texts analyzed in this work are LLM-generated from publicly available Wikipedia seeds; no personal or sensitive data is involved.\nOur method estimates the generation depth of a text passage (how many recursive generation steps it has undergone), not the identity of its author.\nIndividual authorship attribution is outside both the scope and the capability of this approach; privacy implications are minimal.\nWe acknowledge that depth estimation tools could in principle be used to selectively suppress machine-generated text in contexts where such content is legitimate (e.g., accessibility tools, assistive writing).\nWe encourage deployment in data governance pipelines where provenance transparency, rather than content removal, is the objective.\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "aab4f0bd-3b77-4c39-9547-093c44adad7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool result

_source line 5808 · 2026-05-17T15:48:09.379Z_

<details><summary>↩ Tool result · `toolu_011PAJMKU5zE32WRZznk3qc8`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	All eight generators are base (pretrained) models.
5	This is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects, enabling controlled study of recursive distributional drift.
6	However, web text is predominantly produced by instruction-tuned and RLHF-aligned models.
7	Preliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1\,=\,0.338 (vs.\ 0.763 base) and Qwen3-0.6B with chat template to 0.667 (vs.\ 0.816 under a 7-generator split).
8	Length-matched analysis yields near-zero correlations ($|\rho| < 0.02$) and binary classification near chance (F1\,$\approx$\,0.5) for Qwen models, leaving interpretation ambiguous.
9	Extending depth fingerprinting to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.
10	
11	Our experiments include generators up to 8.2B parameters (Qwen3-8B).
12	Depth signal persists at this scale (Qwen3-8B 3-class F1\,=\,0.714), but cross-scale transfer incurs a moderate gap vs.\ $\leq$2.8B generators (F1\,=\,0.77--0.81).
13	Frontier models (70B+) remain untested; their higher fluency may further compress feature margins.
14	
15	Differential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type F1\,=\,0.781) compared to elaboration (0.730), rewriting (0.737), and paraphrastic chains (binary F1\,=\,0.671 vs.\ 0.749 for continuation).
16	DDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.
17	Cross-prompt-type transfer (LOPTO F1\,=\,0.753) confirms shared signal, yet additional prompt types (e.g., summarization, instruction following) and cross-generator $\times$ cross-prompt interactions remain untested.
18	
19	Our primary evaluation uses single-generator chains; cross-model chains (\S\ref{sec:results-classification}) confirm depth signal under generator heterogeneity (3-class F1\,=\,0.809, binary F1\,=\,0.764), though the eight generators represent a controlled laboratory setting rather than the full diversity of real-world contamination.
20	Simulated human editing (\S\ref{sec:discussion}) suggests graceful degradation, but the gap between simulated token replacement and real-world post-processing remains untested.
21	
22	The reference model is fixed to Pythia-410M throughout, although cross-family reference experiments (\S\ref{sec:results-differential}) confirm the phenomenon is not reference-specific (spread 0.013 across three references).
23	All seed texts in the main evaluation are English Wikipedia excerpts.
24	Cross-domain evaluation (Appendix~\ref{app:domain}) shows that depth signal persists across News, Academic, and Code domains (binary F1 $>$ 0.73 under LOGO at $t{=}1.0$), though a domain $\times$ temperature interaction exists: certain domain/generator combinations at lower temperature approach chance level (e.g., Academic domain binary F1\,=\,0.628 at $t{=}0.7$), suggesting that reference model calibration is critical for cross-domain deployment.
25	The reference model dependency (Pythia-410M, English-centric pretraining) limits non-English applicability and adds inference overhead relative to surface-feature-only approaches.
26	Generalization to other languages remains untested.
27	
28	Our default analysis uses fixed decoding parameters (temperature 0.7, nucleus $p{=}0.9$). A sampling ablation (Appendix~\ref{app:sampling-sensitivity}) shows robustness to moderate variation ($t \in [0.5, 0.7]$, ${\leq}0.3$\,pp) but substantial degradation at $t{=}1.0$ ($-6$\,pp), indicating that depth fingerprinting assumes standard decoding regimes.
29	
30	We use 3-class granularity (gen-0\,/\,gen-1\,/\,gen-2+). A 5-class evaluation (Appendix~\ref{app:finer-depth}) yields LOGO F1\,$\approx$\,0.50, with depths 2--4 mutually indistinguishable, validating the 3-class design as the practical resolution limit.
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75745bd3-f016-4317-8c4c-0ecaee21ba3b",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "0cd49764-f1ef-41ec-bc02-9cdc50d50553",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/limitations.tex",
      "content": "\\section*{Limitations}\n\\label{sec:limitations}\n\nAll eight generators are base (pretrained) models.\nThis is a deliberate design choice: base models isolate the generation mechanism from instruction-tuning effects, enabling controlled study of recursive distributional drift.\nHowever, web text is predominantly produced by instruction-tuned and RLHF-aligned models.\nPreliminary instruct experiments confirm that depth signal degrades substantially under instruction tuning: OLMo-2-1B-Instruct drops to LOGO F1\\,=\\,0.338 (vs.\\ 0.763 base) and Qwen3-0.6B with chat template to 0.667 (vs.\\ 0.816 under a 7-generator split).\nLength-matched analysis yields near-zero correlations ($|\\rho| < 0.02$) and binary classification near chance (F1\\,$\\approx$\\,0.5) for Qwen models, leaving interpretation ambiguous.\nExtending depth fingerprinting to instruct models requires addressing these confounds (length regulation, format constraints, safety-driven distribution shaping) that instruction tuning introduces.\n\nOur experiments include generators up to 8.2B parameters (Qwen3-8B).\nDepth signal persists at this scale (Qwen3-8B 3-class F1\\,=\\,0.714), but cross-scale transfer incurs a moderate gap vs.\\ $\\leq$2.8B generators (F1\\,=\\,0.77--0.81).\nFrontier models (70B+) remain untested; their higher fluency may further compress feature margins.\n\nDifferential depth response strength is prompt-type dependent: continuation chains show strongest drift (within-type F1\\,=\\,0.781) compared to elaboration (0.730), rewriting (0.737), and paraphrastic chains (binary F1\\,=\\,0.671 vs.\\ 0.749 for continuation).\nDDR is most reliably detected in continuation-style generation; near-paraphrastic settings approach the method's detection floor.\nCross-prompt-type transfer (LOPTO F1\\,=\\,0.753) confirms shared signal, yet additional prompt types (e.g., summarization, instruction following) and cross-generator $\\times$ cross-prompt interactions remain untested.\n\nOur primary evaluation uses single-generator chains; cross-model chains (\\S\\ref{sec:results-classification}) confirm depth signal under generator heterogeneity (3-class F1\\,=\\,0.809, binary F1\\,=\\,0.764), though the eight generators represent a controlled laboratory setting rather than the full diversity of real-world contamination.\nSimulated human editing (\\S\\ref{sec:discussion}) suggests graceful degradation, but the gap between simulated token replacement and real-world post-processing remains untested.\n\nThe reference model is fixed to Pythia-410M throughout, although cross-family reference experiments (\\S\\ref{sec:results-differential}) confirm the phenomenon is not reference-specific (spread 0.013 across three references).\nAll seed texts in the main evaluation are English Wikipedia excerpts.\nCross-domain evaluation (Appendix~\\ref{app:domain}) shows that depth signal persists across News, Academic, and Code domains (binary F1 $>$ 0.73 under LOGO at $t{=}1.0$), though a domain $\\times$ temperature interaction exists: certain domain/generator combinations at lower temperature approach chance level (e.g., Academic domain binary F1\\,=\\,0.628 at $t{=}0.7$), suggesting that reference model calibration is critical for cross-domain deployment.\nThe reference model dependency (Pythia-410M, English-centric pretraining) limits non-English applicability and adds inference overhead relative to surface-feature-only approaches.\nGeneralization to other languages remains untested.\n\nOur default analysis uses fixed decoding parameters (temperature 0.7, nucleus $p{=}0.9$). A sampling ablation (Appendix~\\ref{app:sampling-sensitivity}) shows robustness to moderate variation ($t \\in [0.5, 0.7]$, ${\\leq}0.3$\\,pp) but substantial degradation at $t{=}1.0$ ($-6$\\,pp), indicating that depth fingerprinting assumes standard decoding regimes.\n\nWe use 3-class granularity (gen-0\\,/\\,gen-1\\,/\\,gen-2+). A 5-class evaluation (Appendix~\\ref{app:finer-depth}) yields LOGO F1\\,$\\approx$\\,0.50, with depths 2--4 mutually indistinguishable, validating the 3-class design as the practical resolution limit.\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  },
  "sourceToolAssistantUUID": "75745bd3-f016-4317-8c4c-0ecaee21ba3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool call

_source line 5809 · 2026-05-17T15:48:09.571Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JPwSCfC3BXJ2WgDjKyq1Kt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cd49764-f1ef-41ec-bc02-9cdc50d50553",
  "isSidechain": false,
  "requestId": "req_011Cb8QMWKNFmDhL1wgroiB1",
  "type": "assistant",
  "uuid": "aab4f0bd-3b77-4c39-9547-093c44adad7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NK1SuFU4QSLLyo2ZD9iPJK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1624,
      "cache_read_input_tokens": 57270,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1624,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 231,
          "cache_read_input_tokens": 57270,
          "cache_creation_input_tokens": 1624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1624
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

_source line 5810 · 2026-05-17T15:51:08.590Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to understand the page layout better. Looking at the images:

Page 8: 
- Top of page: Tables 2 and 3 (cross-family reference models and feature ablation)
- "Cross-family reference models" paragraph
- "Temperature robustness" paragraph  
- "4.3 Comparison with Detection Baselines" with Table 4 and Figure 3
- Text about baselines
- "4.4 Downstream Utility" section
- Start of "5 Discussion" section

Page 9:
- Continues Discussion: "Prompt-type dependence", "Practical applicability", "The gen-1/gen-2+ boundary", "Relation to model collapse", "Granularity and robustness", "Instruction tuning"


- "6 Conclusion" section
- Start of "Limitations" section

So the Discussion and Conclusion are overflowing to page 9, which means I need to compress roughly a full page worth of content. The Discussion section has seven subsections that could be condensed or merged, while the Conclusion is already fairly compact at about ten lines. I should focus on tightening the Discussion since that's where most of the space is being used.

Looking at the Discussion subsections, several of them cover related ground—like the ones on prompt-type dependence, the gen-1/gen-2+ boundary, and instruction tuning are all touching on similar themes about model behavior. I could merge these together and eliminate redundancy, especially content that overlaps with what's already in the Limitations section. The Results section might also have some room for further compression if needed, though the Discussion is the bigger target here. I'm identifying where I can trim the Discussion section by removing redundancies with Limitations. The main opportunities are compressing sections on model collapse, granularity, and the generational boundary—each could save a few lines. That gets me to about 10 lines of cuts, but I need roughly 50 total. Let me look at the Results section more carefully to find additional compression points, particularly in the cross-model generalization discussion. Looking at the page breakdown, I see the real constraint now—Discussion and Conclusion are spilling onto page 9 when they need to fit within page 8. That's roughly a full page of content I need to cut. Let me map out what's currently occupying pages 1-8 and identify where the overflow is happening.

The Discussion is taking up about 35 lines and the Conclusion another 10, but since Discussion only starts near the bottom of page 8, most of that content is pushing onto page 9. I'm looking at needing to cut around 35 lines total from the main text to make this work.

My best approach is to aggressively compress the Discussion section—cutting it from roughly 35 lines down to 15 would save about 20 lines, then trim another 10-15 lines from the Results section and maybe 3 lines from the Conclusion. That combination should get me the space I need without gutting any single section too badly.

I'm also considering whether Introduction, Related Work, or Method sections have any slack I can tighten up for another 5 lines or so. The document-level F1 score of 0.63 works for flagging at scale where errors decrease with sample size, though misclassifications cluster in shallow generations where drift hasn't fully manifested. The real challenge is separating gen-1 from gen-2+—86% of errors are false negatives because the first recursion produces minimal shifts, causing depth-2 samples to overlap significantly with gen-1 in feature space, an effect that worsens with larger model sizes.

This differs fundamentally from model collapse, which occurs during retraining and progressively shrinks distributions; DDR instead shifts location while preserving shape under fixed parameters, and topic drift shows weak correlation with depth, suggesting it's a mediating factor rather than a confound. Three-class granularity presents a robustness tradeoff I'm evaluating.

Moving to finer distinctions, I see that five-class classification drops significantly in performance, with intermediate depths becoming indistinguishable, though fine-tuning recovers much stronger signal. The depth signal appears rooted in generative structure rather than surface tokens, since perturbations that alter sentence regeneration produce similar degradation to random word replacement. Instruction-tuned variants show markedly weaker fingerprints overall. and this suggests the phenomenon is driven by how standard decoding operates rather than something baked into the model architecture itself. Entropy standard deviation sits in an interesting middle ground—it's more correlated with the drifting features but not as tightly bound as the tail decay, which makes sense if it's partially capturing location-dependent variance.

When I look at prompt type, semantic constraints clearly dampen the drift effect, which aligns with prior work on how anchoring outputs to inputs limits accumulation. The cross-type transfer still holds up reasonably well though. For practical purposes, document-level performance shows F1 around 0.63 per class.

Now I'm examining the error patterns more closely. The performance is too low for reliable automated filtering, but it's actually workable for flagging at the corpus level where errors scale predictably. Most misclassifications happen in shallow generation samples where drift hasn't had time to build up yet, which tracks with the theory.

The real challenge is separating gen-1 from gen-2+. The vast majority of binary errors are false negatives—the model keeps predicting gen-2+ as gen-1—and this gets worse at depth-2 where the error rate hits 48% versus 20% at depth-4. This makes sense because the first recursive step produces the smallest shift, so depth-2 text sits right in the overlap zone with gen-1. Larger models make this worse since they produce text that statistically resembles human input more closely.

I'm also thinking about how this relates to model collapse, which is a different phenomenon entirely. Model collapse happens during retraining on model outputs and causes progressive loss of coverage, whereas what I'm seeing here is inference-chain drift with fixed parameters that's actually reversible. The distributional signatures diverge too—model collapse predicts tail shrinkage while this preserves shape and just shifts location. Topic drift shows...

Topic drift has weak correlation with depth, so it's not confounding the signal. Looking at the practical limits, three classes is about as fine-grained as I can get—going to five classes drops performance significantly and depths become indistinguishable. Fine-tuning with QLoRA recovers much better performance though, suggesting there's richer signal underneath. When I perturb the text, both LLM-based regeneration and random word replacement cause similar degradation, which tells me the signal is in the generative structure, not surface tokens. Instruction-tuned models are much weaker at this, so I'm sticking with base models to isolate the core phenomenon. I've identified about 8 lines of compression from the Discussion section, but that's not quite enough. Let me turn my attention to the Results section and see where else I can trim.

Looking back through results.tex, the main content blocks are the classification performance and cross-model generalization findings, the DDR analysis with its statistical tests and ablations, the baseline comparisons, and the downstream utility section. I'm now examining where the Results section can be condensed further—particularly looking at whether the ordinal regression methods warrant their own sentence or can be folded into existing discussion.

The Levene tests, feature complementarity details with their specific numbers, and the cross-model generalization breakdown with per-family results all seem like candidates for tightening. I need roughly 35 lines total to push the Conclusion back to page 8, which is a pretty aggressive cut—about half a page worth.

I'm considering a more structural approach: instead of keeping seven separate paragraph sections in the Discussion, I could merge related concepts together to eliminate redundant transitions and reduce overhead.

Another angle is moving some of the detailed numerical results to the appendix while keeping just the key insights in the main text. Table 3 with the feature ablation could shift to supplementary material, letting me condense that section to a single sentence. I could also push some of the granularity and instruction tuning specifics to a "Scope and Future Work" appendix section.

The Conclusion itself has some overlap with points already made in the paper, so there's room to compress it further without losing the main message.

Let me be more systematic about this. Moving Table 3 alone saves roughly 10 lines with its caption. Merging and tightening the Discussion sections could cut another 10-15 lines. Streamlining the Conclusion gets me 5 more. Removing the ordinal regression mention and a few other minor trims should get me to around 30-35 lines total, which is what I'm aiming for.

But I need to account for the two-column layout properly. Each page in this format holds about 95-100 lines of text across both columns. To drop a full page, I'm really looking at needing to cut roughly 47-50 lines of actual content. So my 30-35 line estimate might not be quite enough—I may need to be more aggressive, possibly moving Table 3 and also cutting deeper into the Discussion or Results sections. Looking at the space constraints, Discussion and Conclusion together take up about 0.7 pages, but I only have roughly 0.33 pages available on page 8 before they overflow onto page 9. That means I'm about 0.37 pages over, which translates to needing to cut around 50 lines across both sections.

Breaking down where I can trim: the Discussion section is the biggest target—I can compress it from about 25 lines down to 15, saving roughly 10 lines. In the Results section, I can remove the ordinal regression sentence and tighten up the Levene test and feature complementarity explanations for another 5 lines. The Conclusion can be slightly condensed for about 3 more lines. That gets me to roughly 18 lines of compression total, which should fit the space.

Now I'm working through the actual compressed versions of each section, starting with the Discussion.

The key insight about shape stationarity is that the softmax architecture and sampling parameters stay fixed across depths—recursive generation shifts the context toward high-probability regions but doesn't change the underlying generation mechanism. The sampling ablation confirms this approximate stationarity holds across different temperature settings, with entropy standard deviation sitting between the drifting features and the nearly-stationary tail decay. Prompt type does matter though—semantic-preservation constraints reduce drift compared to open-ended continuation, though cross-type transfer still works reasonably well. For practical use, the gen-1 versus gen-2+ boundary is where performance becomes viable at the document level.

Now looking at the error analysis: the F1 score of 0.63 is too low for automated filtering but works for corpus-level flagging where errors scale down with sample size. The real challenge is that 86% of binary classification errors are false negatives, with depth-2 showing a 48% error rate versus 20% at depth-4—this asymmetry makes sense given that the first recursive step produces the smallest location shift. I should clarify how this differs from model collapse, which involves retraining on outputs and causes degradation; what's happening here is inference-chain drift with fixed parameters that's fully reversible and only shifts location without changing the distribution's shape. The practical resolution ceiling appears to be around three classes, with performance dropping significantly when trying to distinguish five classes. I'm tracking the edits across the Discussion section—removing redundant explanations about why certain phenomena occur and consolidating related subsections to tighten the narrative. For the Conclusion, I'm distilling the key finding down to its essence: we've shown that recursive generation produces a measurable shift in how tokens distribute across depth levels, and this pattern holds consistently across different model families.

The practical takeaway is that while we can reliably detect this drift with a simple classifier, it doesn't actually translate into meaningful improvements when we try to use it for data curation—random sampling works just as well. I'm also flagging the two constraints that bound our findings: instruction tuning washes out the signal we're detecting, and the largest models might already have compressed these distributional margins naturally. The full feature ensemble achieves notably better F1 scores than either subset alone, with surface features proving critical for distinguishing gen-0 samples despite introducing some noise in binary classification—permutation importance shows hapax ratio and entropy metrics as the top contributors. All seven features show statistical significance after Bonferroni correction, with shape features exhibiting ~10× smaller KS statistics than drifting features, supporting the approximately stationary characterization. Levene tests reject equal variance across all features (p < 10^{-10}), but variance shifts are modest for shape features (<3% for entropy max) compared to drifting features (>15% for hapax ratio). Cross-model chains with random generators per step achieve 3-class F1=0.809 and binary F1=0.764, outperforming single-generator LOGO (0.762), which suggests that generator heterogeneity amplifies the distributional shifts between depths. Leave-one-family-out evaluation drops to binary F1=0.686, confirming transfer across architectural families remains challenging under the strictest unseen conditions.

Looking at per-family performance, smaller Pythia models (1B, 2.8B) show the strongest results with binary F1 around 0.718-0.724, while larger models like Mistral-7B degrade to 0.633—this inverse scaling pattern indicates that higher-capacity models compress the feature margins that the depth signal relies on. The signal generalizes across domains but with notable variation, ranging from 0.628 in academic text to 0.789 on Wikipedia at lower thresholds. I'm tallying up the space I can save across different sections—discussion, conclusion, and various results subsections—to see if I can hit my target of 18-20 lines while maintaining the key findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d469723-7da7-49bf-b2b8-647352064eaf",
  "isSidechain": false,
  "requestId": "req_011Cb8QNGK2mDV4K7Q6izMPo",
  "type": "assistant",
  "uuid": "8fe2deb2-937d-4184-9e1a-054d2d4bbbc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019EaA18g8NhUSz2goZNSRst",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1992,
      "cache_read_input_tokens": 58894,
      "output_tokens": 10778,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1992,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10778,
          "cache_read_input_tokens": 58894,
          "cache_creation_input_tokens": 1992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1992
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

_source line 5811 · 2026-05-17T15:51:08.591Z_

Conclusion is on page 9 instead of page 8. Need significant compression across Discussion, Conclusion, and Results. Let me implement all cuts systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fe2deb2-937d-4184-9e1a-054d2d4bbbc6",
  "isSidechain": false,
  "requestId": "req_011Cb8QNGK2mDV4K7Q6izMPo",
  "type": "assistant",
  "uuid": "c9e373dc-2116-4cf2-8332-ab090d4e675e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019EaA18g8NhUSz2goZNSRst",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1992,
      "cache_read_input_tokens": 58894,
      "output_tokens": 10778,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1992,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10778,
          "cache_read_input_tokens": 58894,
          "cache_creation_input_tokens": 1992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1992
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

_source line 5812 · 2026-05-17T15:51:30.160Z_

<details open><summary>🔧 Tool call — Edit · `toolu_013jeqtbWWQf1AYzj1EZnU4h`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
  "old_string": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why does shape remain approximately stationary?}\nThe softmax architecture and sampling hyperparameters that determine distributional shape are fixed across depths; recursive generation shifts context toward high-probability regions but does not alter the generation mechanism itself.\nThis predicts approximate stationarity under standard decoding, confirmed by sampling ablation ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}), and implies the phenomenon reflects a tendency of standard decoding rather than an architectural guarantee.\nEntropy std ($|\\rho| = 0.17$) is a borderline case between the drifting central-tendency features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$), consistent with a feature that partially captures location-dependent variance.\n\n\\paragraph{Prompt-type dependence.}\nSemantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}: the more a task anchors the output distribution to the input, the less room recursive drift has to accumulate.\nCross-type transfer remains viable (F1\\,=\\,0.753).\n\n\\paragraph{Practical applicability.}\nDocument-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging, where error scales as $O(1/\\sqrt{n})$.\nMisclassifications concentrate in shallow gen-2+ samples where drift has not yet accumulated (Appendix~\\ref{app:error-analysis}), consistent with DDR predictions.\n\n\\paragraph{The gen-1\\,/\\,gen-2+ boundary.}\nThe primary classification difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives (gen-2+ predicted as gen-1), with depth-2 error rate at 48\\% compared to 20\\% for depth-4.\nThis asymmetry follows directly from DDR: the first recursive step produces the smallest location shift, so depth-2 text occupies a region of feature space that overlaps heavily with gen-1.\nLarger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%), consistent with higher-capacity models producing text that more closely matches the statistical properties of human-sourced input.\n\n\\paragraph{Relation to model collapse.}\nModel collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs, progressively losing distributional coverage.\nDDR operates in a different regime: inference-chain drift occurs with fixed parameters and is fully reversible by changing the seed text.\nThe two phenomena diverge in distributional signatures: model collapse predicts progressive tail shrinkage \\cite{curse_of_recursion}, whereas DDR preserves distributional shape while shifting only location.\nTopic drift shows weak correlation with depth features ($|\\rho| < 0.29$), confirming it mediates rather than confounds depth signal.\n\n\\paragraph{Granularity and robustness.}\nThree classes represent the practical resolution ceiling: 5-class LOGO F1 drops to $\\approx$0.50, with depths 2--4 mutually indistinguishable (Appendix~\\ref{app:finer-depth}).\nQLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), confirming richer signal exists beyond summary statistics.\nUnder text perturbation, LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}), confirming depth signal resides in generative structure rather than surface tokens.\n\n\\paragraph{Instruction tuning.}\nInstruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base), justifying our restriction to base models for isolating the phenomenon.",
  "new_string": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why does shape remain approximately stationary?}\nThe softmax architecture and sampling hyperparameters that determine distributional shape are fixed across depths; recursive generation shifts context toward high-probability regions but does not alter the generation mechanism itself.\nThis predicts approximate stationarity under standard decoding, confirmed by sampling ablation ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}).\nEntropy std ($|\\rho| = 0.17$) occupies an intermediate position between the drifting features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$).\n\n\\paragraph{Prompt-type dependence.}\nSemantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}.\nCross-type transfer remains viable (F1\\,=\\,0.753).\n\n\\paragraph{Practical applicability and the gen-1\\,/\\,gen-2+ boundary.}\nDocument-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging ($O(1/\\sqrt{n})$ error scaling).\nThe primary difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives, with depth-2 error rate 48\\% vs.\\ 20\\% for depth-4 (Appendix~\\ref{app:error-analysis}).\nThis asymmetry follows from DDR: the first recursive step produces the smallest location shift.\nLarger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%).\n\n\\paragraph{Relation to model collapse.}\nModel collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs.\nDDR operates in a different regime: inference-chain drift occurs with fixed parameters, is fully reversible, and preserves distributional shape while shifting only location.\n\n\\paragraph{Scope.}\nThree classes represent the practical resolution ceiling (5-class F1\\,$\\approx$\\,0.50; Appendix~\\ref{app:finer-depth}); QLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), confirming richer signal beyond summary statistics.\nDepth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).\nInstruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base), justifying our restriction to base models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9e373dc-2116-4cf2-8332-ab090d4e675e",
  "isSidechain": false,
  "requestId": "req_011Cb8QNGK2mDV4K7Q6izMPo",
  "type": "assistant",
  "uuid": "668878dc-1094-4326-ba24-36ed681cf86a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019EaA18g8NhUSz2goZNSRst",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1992,
      "cache_read_input_tokens": 58894,
      "output_tokens": 10778,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1992,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10778,
          "cache_read_input_tokens": 58894,
          "cache_creation_input_tokens": 1992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1992
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

_source line 5813 · 2026-05-17T15:51:30.175Z_

<details><summary>↩ Tool result · `toolu_013jeqtbWWQf1AYzj1EZnU4h`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "668878dc-1094-4326-ba24-36ed681cf86a",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "3e60f38b-e74b-463b-9a7b-1d4d630ec06c",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/discussion.tex",
    "oldString": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why does shape remain approximately stationary?}\nThe softmax architecture and sampling hyperparameters that determine distributional shape are fixed across depths; recursive generation shifts context toward high-probability regions but does not alter the generation mechanism itself.\nThis predicts approximate stationarity under standard decoding, confirmed by sampling ablation ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}), and implies the phenomenon reflects a tendency of standard decoding rather than an architectural guarantee.\nEntropy std ($|\\rho| = 0.17$) is a borderline case between the drifting central-tendency features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$), consistent with a feature that partially captures location-dependent variance.\n\n\\paragraph{Prompt-type dependence.}\nSemantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}: the more a task anchors the output distribution to the input, the less room recursive drift has to accumulate.\nCross-type transfer remains viable (F1\\,=\\,0.753).\n\n\\paragraph{Practical applicability.}\nDocument-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging, where error scales as $O(1/\\sqrt{n})$.\nMisclassifications concentrate in shallow gen-2+ samples where drift has not yet accumulated (Appendix~\\ref{app:error-analysis}), consistent with DDR predictions.\n\n\\paragraph{The gen-1\\,/\\,gen-2+ boundary.}\nThe primary classification difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives (gen-2+ predicted as gen-1), with depth-2 error rate at 48\\% compared to 20\\% for depth-4.\nThis asymmetry follows directly from DDR: the first recursive step produces the smallest location shift, so depth-2 text occupies a region of feature space that overlaps heavily with gen-1.\nLarger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%), consistent with higher-capacity models producing text that more closely matches the statistical properties of human-sourced input.\n\n\\paragraph{Relation to model collapse.}\nModel collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs, progressively losing distributional coverage.\nDDR operates in a different regime: inference-chain drift occurs with fixed parameters and is fully reversible by changing the seed text.\nThe two phenomena diverge in distributional signatures: model collapse predicts progressive tail shrinkage \\cite{curse_of_recursion}, whereas DDR preserves distributional shape while shifting only location.\nTopic drift shows weak correlation with depth features ($|\\rho| < 0.29$), confirming it mediates rather than confounds depth signal.\n\n\\paragraph{Granularity and robustness.}\nThree classes represent the practical resolution ceiling: 5-class LOGO F1 drops to $\\approx$0.50, with depths 2--4 mutually indistinguishable (Appendix~\\ref{app:finer-depth}).\nQLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), confirming richer signal exists beyond summary statistics.\nUnder text perturbation, LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}), confirming depth signal resides in generative structure rather than surface tokens.\n\n\\paragraph{Instruction tuning.}\nInstruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base), justifying our restriction to base models for isolating the phenomenon.",
    "newString": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why does shape remain approximately stationary?}\nThe softmax architecture and sampling hyperparameters that determine distributional shape are fixed across depths; recursive generation shifts context toward high-probability regions but does not alter the generation mechanism itself.\nThis predicts approximate stationarity under standard decoding, confirmed by sampling ablation ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}).\nEntropy std ($|\\rho| = 0.17$) occupies an intermediate position between the drifting features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$).\n\n\\paragraph{Prompt-type dependence.}\nSemantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}.\nCross-type transfer remains viable (F1\\,=\\,0.753).\n\n\\paragraph{Practical applicability and the gen-1\\,/\\,gen-2+ boundary.}\nDocument-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging ($O(1/\\sqrt{n})$ error scaling).\nThe primary difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives, with depth-2 error rate 48\\% vs.\\ 20\\% for depth-4 (Appendix~\\ref{app:error-analysis}).\nThis asymmetry follows from DDR: the first recursive step produces the smallest location shift.\nLarger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%).\n\n\\paragraph{Relation to model collapse.}\nModel collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs.\nDDR operates in a different regime: inference-chain drift occurs with fixed parameters, is fully reversible, and preserves distributional shape while shifting only location.\n\n\\paragraph{Scope.}\nThree classes represent the practical resolution ceiling (5-class F1\\,$\\approx$\\,0.50; Appendix~\\ref{app:finer-depth}); QLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), confirming richer signal beyond summary statistics.\nDepth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).\nInstruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base), justifying our restriction to base models.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why does shape remain approximately stationary?}\nThe softmax architecture and sampling hyperparameters that determine distributional shape are fixed across depths; recursive generation shifts context toward high-probability regions but does not alter the generation mechanism itself.\nThis predicts approximate stationarity under standard decoding, confirmed by sampling ablation ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}), and implies the phenomenon reflects a tendency of standard decoding rather than an architectural guarantee.\nEntropy std ($|\\rho| = 0.17$) is a borderline case between the drifting central-tendency features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$), consistent with a feature that partially captures location-dependent variance.\n\n\\paragraph{Prompt-type dependence.}\nSemantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}: the more a task anchors the output distribution to the input, the less room recursive drift has to accumulate.\nCross-type transfer remains viable (F1\\,=\\,0.753).\n\n\\paragraph{Practical applicability.}\nDocument-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging, where error scales as $O(1/\\sqrt{n})$.\nMisclassifications concentrate in shallow gen-2+ samples where drift has not yet accumulated (Appendix~\\ref{app:error-analysis}), consistent with DDR predictions.\n\n\\paragraph{The gen-1\\,/\\,gen-2+ boundary.}\nThe primary classification difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives (gen-2+ predicted as gen-1), with depth-2 error rate at 48\\% compared to 20\\% for depth-4.\nThis asymmetry follows directly from DDR: the first recursive step produces the smallest location shift, so depth-2 text occupies a region of feature space that overlaps heavily with gen-1.\nLarger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%), consistent with higher-capacity models producing text that more closely matches the statistical properties of human-sourced input.\n\n\\paragraph{Relation to model collapse.}\nModel collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs, progressively losing distributional coverage.\nDDR operates in a different regime: inference-chain drift occurs with fixed parameters and is fully reversible by changing the seed text.\nThe two phenomena diverge in distributional signatures: model collapse predicts progressive tail shrinkage \\cite{curse_of_recursion}, whereas DDR preserves distributional shape while shifting only location.\nTopic drift shows weak correlation with depth features ($|\\rho| < 0.29$), confirming it mediates rather than confounds depth signal.\n\n\\paragraph{Granularity and robustness.}\nThree classes represent the practical resolution ceiling: 5-class LOGO F1 drops to $\\approx$0.50, with depths 2--4 mutually indistinguishable (Appendix~\\ref{app:finer-depth}).\nQLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), confirming richer signal exists beyond summary statistics.\nUnder text perturbation, LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}), confirming depth signal resides in generative structure rather than surface tokens.\n\n\\paragraph{Instruction tuning.}\nInstruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base), justifying our restriction to base models for isolating the phenomenon.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 32,
        "newStart": 3,
        "newLines": 24,
        "lines": [
          " ",
          " \\paragraph{Why does shape remain approximately stationary?}",
          " The softmax architecture and sampling hyperparameters that determine distributional shape are fixed across depths; recursive generation shifts context toward high-probability regions but does not alter the generation mechanism itself.",
          "-This predicts approximate stationarity under standard decoding, confirmed by sampling ablation ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}), and implies the phenomenon reflects a tendency of standard decoding rather than an architectural guarantee.",
          "-Entropy std ($|\\rho| = 0.17$) is a borderline case between the drifting central-tendency features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$), consistent with a feature that partially captures location-dependent variance.",
          "+This predicts approximate stationarity under standard decoding, confirmed by sampling ablation ($t \\in [0.5, 0.7]$: ${\\leq}0.3$\\,pp degradation; $t = 1.0$: $-6$\\,pp; Appendix~\\ref{app:sampling-sensitivity}).",
          "+Entropy std ($|\\rho| = 0.17$) occupies an intermediate position between the drifting features ($|\\rho| > 0.60$) and the near-stationary tail decay ($|\\rho| = 0.04$).",
          " ",
          " \\paragraph{Prompt-type dependence.}",
          "-Semantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}: the more a task anchors the output distribution to the input, the less room recursive drift has to accumulate.",
          "+Semantic-preservation constraints attenuate drift (elaboration F1\\,=\\,0.730 vs.\\ continuation 0.781; Appendix~\\ref{app:prompt-type}), consistent with \\citet{broken_telephone}.",
          " Cross-type transfer remains viable (F1\\,=\\,0.753).",
          " ",
          "-\\paragraph{Practical applicability.}",
          "-Document-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging, where error scales as $O(1/\\sqrt{n})$.",
          "-Misclassifications concentrate in shallow gen-2+ samples where drift has not yet accumulated (Appendix~\\ref{app:error-analysis}), consistent with DDR predictions.",
          "+\\paragraph{Practical applicability and the gen-1\\,/\\,gen-2+ boundary.}",
          "+Document-level gen-1 per-class F1\\,=\\,0.63 is insufficient for automated filtering but sufficient for corpus-level flagging ($O(1/\\sqrt{n})$ error scaling).",
          "+The primary difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives, with depth-2 error rate 48\\% vs.\\ 20\\% for depth-4 (Appendix~\\ref{app:error-analysis}).",
          "+This asymmetry follows from DDR: the first recursive step produces the smallest location shift.",
          "+Larger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%).",
          " ",
          "-\\paragraph{The gen-1\\,/\\,gen-2+ boundary.}",
          "-The primary classification difficulty is distinguishing gen-1 from gen-2+: 86\\% of binary errors are false negatives (gen-2+ predicted as gen-1), with depth-2 error rate at 48\\% compared to 20\\% for depth-4.",
          "-This asymmetry follows directly from DDR: the first recursive step produces the smallest location shift, so depth-2 text occupies a region of feature space that overlaps heavily with gen-1.",
          "-Larger generators exacerbate the overlap (Mistral-7B error rate 45\\% vs.\\ Pythia-1B 18\\%), consistent with higher-capacity models producing text that more closely matches the statistical properties of human-sourced input.",
          "-",
          " \\paragraph{Relation to model collapse.}",
          "-Model collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs, progressively losing distributional coverage.",
          "-DDR operates in a different regime: inference-chain drift occurs with fixed parameters and is fully reversible by changing the seed text.",
          "-The two phenomena diverge in distributional signatures: model collapse predicts progressive tail shrinkage \\cite{curse_of_recursion}, whereas DDR preserves distributional shape while shifting only location.",
          "-Topic drift shows weak correlation with depth features ($|\\rho| < 0.29$), confirming it mediates rather than confounds depth signal.",
          "+Model collapse \\cite{curse_of_recursion,strong_model_collapse} describes degradation when models are \\emph{retrained} on their own outputs.",
          "+DDR operates in a different regime: inference-chain drift occurs with fixed parameters, is fully reversible, and preserves distributional shape while shifting only location.",
          " ",
          "-\\paragraph{Granularity and robustness.}",
          "-Three classes represent the practical resolution ceiling: 5-class LOGO F1 drops to $\\approx$0.50, with depths 2--4 mutually indistinguishable (Appendix~\\ref{app:finer-depth}).",
          "-QLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), confirming richer signal exists beyond summary statistics.",
          "-Under text perturbation, LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}), confirming depth signal resides in generative structure rather than surface tokens.",
          "-",
          "-\\paragraph{Instruction tuning.}",
          "-Instruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base), justifying our restriction to base models for isolating the phenomenon.",
          "+\\paragraph{Scope.}",
          "+Three classes represent the practical resolution ceiling (5-class F1\\,$\\approx$\\,0.50; Appendix~\\ref{app:finer-depth}); QLoRA fine-tuning recovers F1\\,=\\,0.905 (Appendix~\\ref{app:qlora}), confirming richer signal beyond summary statistics.",
          "+Depth signal resides in generative structure rather than surface tokens: LLM-simulated sentence regeneration (50\\% edit distance) causes comparable degradation to 5\\% random word replacement (Appendix~\\ref{app:human-edit}).",
          "+Instruction-tuned models show substantially weaker fingerprints (OLMo-Instruct LOGO F1\\,=\\,0.338 vs.\\ 0.763 base), justifying our restriction to base models."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "668878dc-1094-4326-ba24-36ed681cf86a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Runtime record

_source line 5814_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch — 页数压缩 + 附录重组] 三项修改，目标：正文（Abstract 到 Conclusion）严格 ≤ 8 页。  **当前问题**：Conclusion 结束在第 9 页右栏，超标约 1 页。  ---  **1. 正文压缩（目标省 ~1 页）**  具体策略（按优先级）：  A) **Cross-model per-class 表格移到附录**（省…",
  "leafUuid": "3e60f38b-e74b-463b-9a7b-1d4d630ec06c",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Runtime record

_source line 5815_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent callback function implementation",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Assistant

_source line 5816 · 2026-05-17T15:51:32.069Z_

Now compress the Conclusion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e60f38b-e74b-463b-9a7b-1d4d630ec06c",
  "isSidechain": false,
  "requestId": "req_011Cb8Qd3xo9LGGHoByXJtz3",
  "type": "assistant",
  "uuid": "88e1b8eb-e718-4b30-966f-55db57e97eb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkRJUwKGAAra9Dq5VYmuxW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10827,
      "cache_read_input_tokens": 60886,
      "output_tokens": 595,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 595,
          "cache_read_input_tokens": 60886,
          "cache_creation_input_tokens": 10827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10827
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

_source line 5817 · 2026-05-17T15:51:44.898Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01KjSwc4J6vytAywkJviETt1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/conclusion.tex",
  "old_string": "We introduced ordinal generation depth estimation and documented a differential depth response across eight base-model generators from five families: recursive generation induces a systematic location shift in the token-level NLL distribution while preserving distributional shape, and this structured drift is detectable with a lightweight 7-feature ensemble (3-class F1\\,=\\,0.809 on cross-model chains, 0.762 under LOGO).\nDespite this detectable drift, depth-aware data curation is practically equivalent to random subsampling at equal sample count (TOST $\\pm$2\\%, $p < 0.001$) within chains of $\\leq$4 generations as measured by perplexity, establishing that detectability and downstream harm are decoupled in this regime.\n\nTwo boundaries define the scope of these results.\nFirst, instruction tuning compresses the distributional variation that fingerprinting exploits; extending to aligned models requires disentangling format-induced and depth-induced drift.\nSecond, while the signal generalizes across generators up to 8B parameters, frontier-scale models (70B+) with higher fluency may further compress feature margins.\nAll code, data, and trained models will be released upon publication.",
  "new_string": "We introduced ordinal generation depth estimation and documented a differential depth response across eight base-model generators from five families: recursive generation induces a systematic location shift in the token-level NLL distribution while preserving distributional shape, detectable with a lightweight 7-feature ensemble (3-class F1\\,=\\,0.809 on cross-model chains, 0.762 under LOGO).\nDespite this detectable drift, depth-aware data curation is practically equivalent to random subsampling at equal sample count (TOST $\\pm$2\\%, $p < 0.001$), establishing that detectability and downstream harm are decoupled in this regime.\nTwo boundaries remain: instruction tuning compresses the distributional variation that fingerprinting exploits, and frontier-scale models (70B+) may further compress feature margins.\nAll code, data, and trained models will be released upon publication."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88e1b8eb-e718-4b30-966f-55db57e97eb4",
  "isSidechain": false,
  "requestId": "req_011Cb8Qd3xo9LGGHoByXJtz3",
  "type": "assistant",
  "uuid": "1099946b-ca52-4c1f-bc0b-cf563dad9c11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkRJUwKGAAra9Dq5VYmuxW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10827,
      "cache_read_input_tokens": 60886,
      "output_tokens": 595,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 595,
          "cache_read_input_tokens": 60886,
          "cache_creation_input_tokens": 10827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10827
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

_source line 5818 · 2026-05-17T15:51:44.906Z_

<details><summary>↩ Tool result · `toolu_01KjSwc4J6vytAywkJviETt1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1099946b-ca52-4c1f-bc0b-cf563dad9c11",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "30a488d3-5b85-48b5-aeea-1672112c8e9c",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/conclusion.tex",
    "oldString": "We introduced ordinal generation depth estimation and documented a differential depth response across eight base-model generators from five families: recursive generation induces a systematic location shift in the token-level NLL distribution while preserving distributional shape, and this structured drift is detectable with a lightweight 7-feature ensemble (3-class F1\\,=\\,0.809 on cross-model chains, 0.762 under LOGO).\nDespite this detectable drift, depth-aware data curation is practically equivalent to random subsampling at equal sample count (TOST $\\pm$2\\%, $p < 0.001$) within chains of $\\leq$4 generations as measured by perplexity, establishing that detectability and downstream harm are decoupled in this regime.\n\nTwo boundaries define the scope of these results.\nFirst, instruction tuning compresses the distributional variation that fingerprinting exploits; extending to aligned models requires disentangling format-induced and depth-induced drift.\nSecond, while the signal generalizes across generators up to 8B parameters, frontier-scale models (70B+) with higher fluency may further compress feature margins.\nAll code, data, and trained models will be released upon publication.",
    "newString": "We introduced ordinal generation depth estimation and documented a differential depth response across eight base-model generators from five families: recursive generation induces a systematic location shift in the token-level NLL distribution while preserving distributional shape, detectable with a lightweight 7-feature ensemble (3-class F1\\,=\\,0.809 on cross-model chains, 0.762 under LOGO).\nDespite this detectable drift, depth-aware data curation is practically equivalent to random subsampling at equal sample count (TOST $\\pm$2\\%, $p < 0.001$), establishing that detectability and downstream harm are decoupled in this regime.\nTwo boundaries remain: instruction tuning compresses the distributional variation that fingerprinting exploits, and frontier-scale models (70B+) may further compress feature margins.\nAll code, data, and trained models will be released upon publication.",
    "originalFile": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe introduced ordinal generation depth estimation and documented a differential depth response across eight base-model generators from five families: recursive generation induces a systematic location shift in the token-level NLL distribution while preserving distributional shape, and this structured drift is detectable with a lightweight 7-feature ensemble (3-class F1\\,=\\,0.809 on cross-model chains, 0.762 under LOGO).\nDespite this detectable drift, depth-aware data curation is practically equivalent to random subsampling at equal sample count (TOST $\\pm$2\\%, $p < 0.001$) within chains of $\\leq$4 generations as measured by perplexity, establishing that detectability and downstream harm are decoupled in this regime.\n\nTwo boundaries define the scope of these results.\nFirst, instruction tuning compresses the distributional variation that fingerprinting exploits; extending to aligned models requires disentangling format-induced and depth-induced drift.\nSecond, while the signal generalizes across generators up to 8B parameters, frontier-scale models (70B+) with higher fluency may further compress feature margins.\nAll code, data, and trained models will be released upon publication.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 10,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " \\section{Conclusion}",
          " \\label{sec:conclusion}",
          " ",
          "-We introduced ordinal generation depth estimation and documented a differential depth response across eight base-model generators from five families: recursive generation induces a systematic location shift in the token-level NLL distribution while preserving distributional shape, and this structured drift is detectable with a lightweight 7-feature ensemble (3-class F1\\,=\\,0.809 on cross-model chains, 0.762 under LOGO).",
          "-Despite this detectable drift, depth-aware data curation is practically equivalent to random subsampling at equal sample count (TOST $\\pm$2\\%, $p < 0.001$) within chains of $\\leq$4 generations as measured by perplexity, establishing that detectability and downstream harm are decoupled in this regime.",
          "-",
          "-Two boundaries define the scope of these results.",
          "-First, instruction tuning compresses the distributional variation that fingerprinting exploits; extending to aligned models requires disentangling format-induced and depth-induced drift.",
          "-Second, while the signal generalizes across generators up to 8B parameters, frontier-scale models (70B+) with higher fluency may further compress feature margins.",
          "+We introduced ordinal generation depth estimation and documented a differential depth response across eight base-model generators from five families: recursive generation induces a systematic location shift in the token-level NLL distribution while preserving distributional shape, detectable with a lightweight 7-feature ensemble (3-class F1\\,=\\,0.809 on cross-model chains, 0.762 under LOGO).",
          "+Despite this detectable drift, depth-aware data curation is practically equivalent to random subsampling at equal sample count (TOST $\\pm$2\\%, $p < 0.001$), establishing that detectability and downstream harm are decoupled in this regime.",
          "+Two boundaries remain: instruction tuning compresses the distributional variation that fingerprinting exploits, and frontier-scale models (70B+) may further compress feature margins.",
          " All code, data, and trained models will be released upon publication."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "1099946b-ca52-4c1f-bc0b-cf563dad9c11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Assistant

_source line 5819 · 2026-05-17T15:51:47.740Z_

Now compress Results: cross-model generalization, ordinal regression, KS/Levene, and feature complementarity.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30a488d3-5b85-48b5-aeea-1672112c8e9c",
  "isSidechain": false,
  "requestId": "req_011Cb8Qe8tVbpuWfSmq8nhuc",
  "type": "assistant",
  "uuid": "00820891-e943-4e93-8222-cee12e72119a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ca5EUN9HQBCBGYpcS31btR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 71713,
      "output_tokens": 998,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 998,
          "cache_read_input_tokens": 71713,
          "cache_creation_input_tokens": 668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 668
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

_source line 5820 · 2026-05-17T15:52:05.451Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01XMX1tR7Pfi84SBE7R5g3EL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex",
  "old_string": "\\paragraph{Cross-model generalization.}\nCross-model chains (randomly selected generator per step) yield 3-class F1\\,=\\,0.809 and binary F1\\,=\\,0.764 under 5-fold CV,\\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation.} confirming that depth signal persists when text passes through heterogeneous generators.\nThe higher cross-model performance relative to single-generator LOGO (3-class: 0.809 vs.\\ 0.762) suggests that generator heterogeneity amplifies distributional shifts between depths, making each recursive step more distinct.\nPer-class performance shows gen-0 F1\\,=\\,0.935, gen-1 0.768, gen-2+ 0.789 (Appendix~\\ref{app:cross-model-detail}).\n\nLeave-one-family-out (LOFO) evaluation yields average binary F1\\,=\\,0.686 ($\\Delta$\\,=\\,$-$0.8\\,pp vs.\\ LOGO), confirming transfer across architectural families under the strictest unseen-generator test.\nPer-family LOGO performance reveals a scale effect: Pythia generators (1B, 2.8B) achieve the highest binary F1 (0.718--0.724), followed by Qwen (0.691--0.709) and OLMo (0.695), while larger generators Qwen3-8B (0.692) and Mistral-7B (0.633) show degradation.\nThis pattern is consistent with higher-capacity models generating text closer to the human baseline distribution, compressing the feature margins that DDR exploits.\nAppendix~\\ref{app:domain} further demonstrates that the signal generalizes across text domains, though with substantial variation (Wikipedia binary F1\\,=\\,0.789 vs.\\ Academic 0.628 at $t{=}0.7$; all domains $>$\\,0.73 at $t{=}1.0$).",
  "new_string": "\\paragraph{Cross-model generalization.}\nCross-model chains (randomly selected generator per step) yield 3-class F1\\,=\\,0.809 and binary F1\\,=\\,0.764 under 5-fold CV,\\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation.} confirming that depth signal persists under generator heterogeneity.\nPer-class performance shows gen-0 F1\\,=\\,0.935, gen-1 0.768, gen-2+ 0.789 (Appendix~\\ref{app:cross-model-detail}).\n\nLeave-one-family-out (LOFO) evaluation yields average binary F1\\,=\\,0.686 ($\\Delta$\\,=\\,$-$0.8\\,pp vs.\\ LOGO), confirming transfer across architectural families.\nA scale effect emerges: Pythia generators (1B, 2.8B) achieve the highest binary F1 (0.718--0.724), while larger generators show degradation (Mistral-7B: 0.633), consistent with higher-capacity models compressing the feature margins DDR exploits.\nThe signal also generalizes across text domains (Appendix~\\ref{app:domain})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00820891-e943-4e93-8222-cee12e72119a",
  "isSidechain": false,
  "requestId": "req_011Cb8Qe8tVbpuWfSmq8nhuc",
  "type": "assistant",
  "uuid": "dbbe26e0-f0c5-47b0-a40e-80a6cb4a3853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ca5EUN9HQBCBGYpcS31btR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 71713,
      "output_tokens": 998,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 998,
          "cache_read_input_tokens": 71713,
          "cache_creation_input_tokens": 668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 668
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

_source line 5821 · 2026-05-17T15:52:05.466Z_

<details><summary>↩ Tool result · `toolu_01XMX1tR7Pfi84SBE7R5g3EL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbbe26e0-f0c5-47b0-a40e-80a6cb4a3853",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "efadf647-693e-4157-848e-49b2022b10ee",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex",
    "oldString": "\\paragraph{Cross-model generalization.}\nCross-model chains (randomly selected generator per step) yield 3-class F1\\,=\\,0.809 and binary F1\\,=\\,0.764 under 5-fold CV,\\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation.} confirming that depth signal persists when text passes through heterogeneous generators.\nThe higher cross-model performance relative to single-generator LOGO (3-class: 0.809 vs.\\ 0.762) suggests that generator heterogeneity amplifies distributional shifts between depths, making each recursive step more distinct.\nPer-class performance shows gen-0 F1\\,=\\,0.935, gen-1 0.768, gen-2+ 0.789 (Appendix~\\ref{app:cross-model-detail}).\n\nLeave-one-family-out (LOFO) evaluation yields average binary F1\\,=\\,0.686 ($\\Delta$\\,=\\,$-$0.8\\,pp vs.\\ LOGO), confirming transfer across architectural families under the strictest unseen-generator test.\nPer-family LOGO performance reveals a scale effect: Pythia generators (1B, 2.8B) achieve the highest binary F1 (0.718--0.724), followed by Qwen (0.691--0.709) and OLMo (0.695), while larger generators Qwen3-8B (0.692) and Mistral-7B (0.633) show degradation.\nThis pattern is consistent with higher-capacity models generating text closer to the human baseline distribution, compressing the feature margins that DDR exploits.\nAppendix~\\ref{app:domain} further demonstrates that the signal generalizes across text domains, though with substantial variation (Wikipedia binary F1\\,=\\,0.789 vs.\\ Academic 0.628 at $t{=}0.7$; all domains $>$\\,0.73 at $t{=}1.0$).",
    "newString": "\\paragraph{Cross-model generalization.}\nCross-model chains (randomly selected generator per step) yield 3-class F1\\,=\\,0.809 and binary F1\\,=\\,0.764 under 5-fold CV,\\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation.} confirming that depth signal persists under generator heterogeneity.\nPer-class performance shows gen-0 F1\\,=\\,0.935, gen-1 0.768, gen-2+ 0.789 (Appendix~\\ref{app:cross-model-detail}).\n\nLeave-one-family-out (LOFO) evaluation yields average binary F1\\,=\\,0.686 ($\\Delta$\\,=\\,$-$0.8\\,pp vs.\\ LOGO), confirming transfer across architectural families.\nA scale effect emerges: Pythia generators (1B, 2.8B) achieve the highest binary F1 (0.718--0.724), while larger generators show degradation (Mistral-7B: 0.633), consistent with higher-capacity models compressing the feature margins DDR exploits.\nThe signal also generalizes across text domains (Appendix~\\ref{app:domain}).",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 10,
        "oldLines": 14,
        "newStart": 10,
        "newLines": 12,
        "lines": [
          " Larger generators show moderate degradation (Qwen3-8B: 0.692, Mistral-7B: 0.633) relative to the 0.694 average.",
          " ",
          " \\paragraph{Cross-model generalization.}",
          "-Cross-model chains (randomly selected generator per step) yield 3-class F1\\,=\\,0.809 and binary F1\\,=\\,0.764 under 5-fold CV,\\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation.} confirming that depth signal persists when text passes through heterogeneous generators.",
          "-The higher cross-model performance relative to single-generator LOGO (3-class: 0.809 vs.\\ 0.762) suggests that generator heterogeneity amplifies distributional shifts between depths, making each recursive step more distinct.",
          "+Cross-model chains (randomly selected generator per step) yield 3-class F1\\,=\\,0.809 and binary F1\\,=\\,0.764 under 5-fold CV,\\footnote{Cross-model chains use the original five-generator subset (Pythia, OLMo, Qwen); Llama and Mistral were added later for single-generator evaluation.} confirming that depth signal persists under generator heterogeneity.",
          " Per-class performance shows gen-0 F1\\,=\\,0.935, gen-1 0.768, gen-2+ 0.789 (Appendix~\\ref{app:cross-model-detail}).",
          " ",
          "-Leave-one-family-out (LOFO) evaluation yields average binary F1\\,=\\,0.686 ($\\Delta$\\,=\\,$-$0.8\\,pp vs.\\ LOGO), confirming transfer across architectural families under the strictest unseen-generator test.",
          "-Per-family LOGO performance reveals a scale effect: Pythia generators (1B, 2.8B) achieve the highest binary F1 (0.718--0.724), followed by Qwen (0.691--0.709) and OLMo (0.695), while larger generators Qwen3-8B (0.692) and Mistral-7B (0.633) show degradation.",
          "-This pattern is consistent with higher-capacity models generating text closer to the human baseline distribution, compressing the feature margins that DDR exploits.",
          "-Appendix~\\ref{app:domain} further demonstrates that the signal generalizes across text domains, though with substantial variation (Wikipedia binary F1\\,=\\,0.789 vs.\\ Academic 0.628 at $t{=}0.7$; all domains $>$\\,0.73 at $t{=}1.0$).",
          "+Leave-one-family-out (LOFO) evaluation yields average binary F1\\,=\\,0.686 ($\\Delta$\\,=\\,$-$0.8\\,pp vs.\\ LOGO), confirming transfer across architectural families.",
          "+A scale effect emerges: Pythia generators (1B, 2.8B) achieve the highest binary F1 (0.718--0.724), while larger generators show degradation (Mistral-7B: 0.633), consistent with higher-capacity models compressing the feature margins DDR exploits.",
          "+The signal also generalizes across text domains (Appendix~\\ref{app:domain}).",
          " ",
          " \\paragraph{Length confound control.}",
          " Length-matched subsampling yields binary F1\\,=\\,0.724 ($\\Delta$\\,=\\,$-$0.046 vs.\\ unmatched), with length accounting for $\\approx$6\\% of discriminative performance (Appendix~\\ref{app:length})."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "dbbe26e0-f0c5-47b0-a40e-80a6cb4a3853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Tool call

_source line 5822 · 2026-05-17T15:52:15.902Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01BbXZsQqCGRe8H9Mf5ZKJf9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex",
  "old_string": "Ordinal regression methods (CORAL \\cite{coral_ordinal}, Frank-Hall \\cite{frank_hall_ordinal}) achieve comparable F1 with overlapping CIs, confirming that 3-class granularity provides insufficient resolution for ranking-aware losses.\n\n\\subsection{Differential Depth Response}",
  "new_string": "\\subsection{Differential Depth Response}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "efadf647-693e-4157-848e-49b2022b10ee",
  "isSidechain": false,
  "requestId": "req_011Cb8Qffnss82ZyZTvGEmxK",
  "type": "assistant",
  "uuid": "d591f598-9e7e-499a-a1ac-a5cb4668de6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MANqChSXkAczm13b4fJ2hq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1052,
      "cache_read_input_tokens": 72381,
      "output_tokens": 221,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1052,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 221,
          "cache_read_input_tokens": 72381,
          "cache_creation_input_tokens": 1052,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1052
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

_source line 5823 · 2026-05-17T15:52:15.917Z_

<details><summary>↩ Tool result · `toolu_01BbXZsQqCGRe8H9Mf5ZKJf9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d591f598-9e7e-499a-a1ac-a5cb4668de6d",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "6fdf8300-3b66-4dff-b710-5837b8fd481e",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex",
    "oldString": "Ordinal regression methods (CORAL \\cite{coral_ordinal}, Frank-Hall \\cite{frank_hall_ordinal}) achieve comparable F1 with overlapping CIs, confirming that 3-class granularity provides insufficient resolution for ranking-aware losses.\n\n\\subsection{Differential Depth Response}",
    "newString": "\\subsection{Differential Depth Response}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 45,
        "oldLines": 8,
        "newStart": 45,
        "newLines": 6,
        "lines": [
          " \\label{tab:logo-results}",
          " \\end{table}",
          " ",
          "-Ordinal regression methods (CORAL \\cite{coral_ordinal}, Frank-Hall \\cite{frank_hall_ordinal}) achieve comparable F1 with overlapping CIs, confirming that 3-class granularity provides insufficient resolution for ranking-aware losses.",
          "-",
          " \\subsection{Differential Depth Response}",
          " \\label{sec:results-differential}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "d591f598-9e7e-499a-a1ac-a5cb4668de6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Runtime record

_source line 5824 · 2026-05-17T15:52:15.924Z_

```json
{
  "parentUuid": "6fdf8300-3b66-4dff-b710-5837b8fd481e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e454a7ae-263a-4601-be79-822157f37bb5",
  "timestamp": "2026-05-17T15:52:15.924Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

---


### Tool call

_source line 5825 · 2026-05-17T15:52:25.572Z_

<details open><summary>🔧 Tool call — Edit · `toolu_0172hdXgt8ys67taN5xM5ypf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex",
  "old_string": "All seven features reach statistical significance after Bonferroni correction, but shape-feature KS statistics are ${\\sim}10\\times$ smaller than drifting features, supporting the ``approximately stationary'' characterization.\nEntropy std occupies an intermediate position (KS\\,=\\,0.285), consistent with its borderline rank correlation.\nLevene tests for variance homogeneity reject equal variance for all seven features ($p < 10^{-10}$), indicating that recursive generation alters spread as well as location, though the magnitude of variance change is substantially smaller for shape features (coefficient of variation shift $<$3\\% for entropy max vs.\\ $>$15\\% for hapax ratio).",
  "new_string": "All seven features reach statistical significance after Bonferroni correction, but shape-feature KS statistics are ${\\sim}10\\times$ smaller than drifting features, supporting the ``approximately stationary'' characterization.\nEntropy std occupies an intermediate position (KS\\,=\\,0.285), consistent with its borderline rank correlation.\nLevene tests reject equal variance for all features ($p < 10^{-10}$), though variance changes are substantially smaller for shape features."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e454a7ae-263a-4601-be79-822157f37bb5",
  "isSidechain": false,
  "requestId": "req_011Cb8QgRQiaHgBgnw15CbP7",
  "type": "assistant",
  "uuid": "a0c55805-86b9-4e56-96cb-81844bc48f92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VqphiEQgTcHBhBV5XdsKnu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 379,
      "cache_read_input_tokens": 73433,
      "output_tokens": 409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 379,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 409,
          "cache_read_input_tokens": 73433,
          "cache_creation_input_tokens": 379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 379
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

_source line 5826 · 2026-05-17T15:52:25.580Z_

<details><summary>↩ Tool result · `toolu_0172hdXgt8ys67taN5xM5ypf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0c55805-86b9-4e56-96cb-81844bc48f92",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "6d7a27a0-4076-47ce-bfca-1c871ee82991",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex",
    "oldString": "All seven features reach statistical significance after Bonferroni correction, but shape-feature KS statistics are ${\\sim}10\\times$ smaller than drifting features, supporting the ``approximately stationary'' characterization.\nEntropy std occupies an intermediate position (KS\\,=\\,0.285), consistent with its borderline rank correlation.\nLevene tests for variance homogeneity reject equal variance for all seven features ($p < 10^{-10}$), indicating that recursive generation alters spread as well as location, though the magnitude of variance change is substantially smaller for shape features (coefficient of variation shift $<$3\\% for entropy max vs.\\ $>$15\\% for hapax ratio).",
    "newString": "All seven features reach statistical significance after Bonferroni correction, but shape-feature KS statistics are ${\\sim}10\\times$ smaller than drifting features, supporting the ``approximately stationary'' characterization.\nEntropy std occupies an intermediate position (KS\\,=\\,0.285), consistent with its borderline rank correlation.\nLevene tests reject equal variance for all features ($p < 10^{-10}$), though variance changes are substantially smaller for shape features.",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 65,
        "oldLines": 7,
        "newStart": 65,
        "newLines": 7,
        "lines": [
          " Two-sample Kolmogorov--Smirnov tests between gen-1 and gen-2+ distributions isolate the recursive depth effect (excluding the initial human$\\rightarrow$LLM transition): drifting features exhibit large distributional shifts (entropy mean KS\\,=\\,0.537, TTR\\,=\\,0.517, hapax ratio\\,=\\,0.516; all $p \\approx 0$), while shape features show order-of-magnitude smaller shifts (entropy max KS\\,=\\,0.043, tail decay\\,=\\,0.052).",
          " All seven features reach statistical significance after Bonferroni correction, but shape-feature KS statistics are ${\\sim}10\\times$ smaller than drifting features, supporting the ``approximately stationary'' characterization.",
          " Entropy std occupies an intermediate position (KS\\,=\\,0.285), consistent with its borderline rank correlation.",
          "-Levene tests for variance homogeneity reject equal variance for all seven features ($p < 10^{-10}$), indicating that recursive generation alters spread as well as location, though the magnitude of variance change is substantially smaller for shape features (coefficient of variation shift $<$3\\% for entropy max vs.\\ $>$15\\% for hapax ratio).",
          "+Levene tests reject equal variance for all features ($p < 10^{-10}$), though variance changes are substantially smaller for shape features.",
          " ",
          " \\paragraph{Feature complementarity.}",
          " Under 10-fold stratified CV, the full 7-feature set (F1\\,=\\,0.773) significantly outperforms surface-only (F1\\,=\\,0.688) and reference-only (F1\\,=\\,0.713; McNemar $p \\approx 0$; Table~\\ref{tab:ablation})."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "a0c55805-86b9-4e56-96cb-81844bc48f92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Runtime record

_source line 5827_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch — 页数压缩 + 附录重组] 三项修改，目标：正文（Abstract 到 Conclusion）严格 ≤ 8 页。  **当前问题**：Conclusion 结束在第 9 页右栏，超标约 1 页。  ---  **1. 正文压缩（目标省 ~1 页）**  具体策略（按优先级）：  A) **Cross-model per-class 表格移到附录**（省…",
  "leafUuid": "6d7a27a0-4076-47ce-bfca-1c871ee82991",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Runtime record

_source line 5828_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent callback function implementation",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Tool call

_source line 5829 · 2026-05-17T15:52:36.913Z_

<details open><summary>🔧 Tool call — Edit · `toolu_012eQzmwddS82uggUZxZvAoJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex",
  "old_string": "\\paragraph{Feature complementarity.}\nUnder 10-fold stratified CV, the full 7-feature set (F1\\,=\\,0.773) significantly outperforms surface-only (F1\\,=\\,0.688) and reference-only (F1\\,=\\,0.713; McNemar $p \\approx 0$; Table~\\ref{tab:ablation}).\nReference-only features yield higher binary F1 (0.833 vs.\\ 0.695 for the full ensemble) because surface lexical features introduce noise at the gen-1/gen-2+ boundary.\nHowever, surface features are essential for 3-class classification, where they improve gen-0 discrimination by capturing vocabulary diversity patterns absent in reference-model entropy statistics (Full 3-class F1\\,=\\,0.773 vs.\\ Reference-only 0.713).\nPermutation importance: hapax ratio (0.35), entropy mean (0.23), TTR (0.18).\nLeave-one-feature-out confirms 6 of 7 features contribute positively (Appendix~\\ref{app:lofo}).",
  "new_string": "\\paragraph{Feature complementarity.}\nUnder 10-fold stratified CV, the full 7-feature set (F1\\,=\\,0.773) significantly outperforms surface-only (F1\\,=\\,0.688) and reference-only (F1\\,=\\,0.713; McNemar $p \\approx 0$; Table~\\ref{tab:ablation}).\nSurface and reference features are complementary: surface features improve gen-0 discrimination, while reference features dominate binary depth separation.\nPermutation importance: hapax ratio (0.35), entropy mean (0.23), TTR (0.18); leave-one-feature-out confirms 6 of 7 features contribute positively (Appendix~\\ref{app:lofo})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d7a27a0-4076-47ce-bfca-1c871ee82991",
  "isSidechain": false,
  "requestId": "req_011Cb8Qh93kJfdvxyBkFXWsY",
  "type": "assistant",
  "uuid": "c8609b8d-ca54-49b0-9ebf-036f19a4dc8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BsvS2ScVdaD4RDNHFEXap",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 73812,
      "output_tokens": 589,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 463,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 589,
          "cache_read_input_tokens": 73812,
          "cache_creation_input_tokens": 463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 463
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

_source line 5830 · 2026-05-17T15:52:36.928Z_

<details><summary>↩ Tool result · `toolu_012eQzmwddS82uggUZxZvAoJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c8609b8d-ca54-49b0-9ebf-036f19a4dc8a",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "fadba9e1-4d56-4503-878d-b91bf5741bf0",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/results.tex",
    "oldString": "\\paragraph{Feature complementarity.}\nUnder 10-fold stratified CV, the full 7-feature set (F1\\,=\\,0.773) significantly outperforms surface-only (F1\\,=\\,0.688) and reference-only (F1\\,=\\,0.713; McNemar $p \\approx 0$; Table~\\ref{tab:ablation}).\nReference-only features yield higher binary F1 (0.833 vs.\\ 0.695 for the full ensemble) because surface lexical features introduce noise at the gen-1/gen-2+ boundary.\nHowever, surface features are essential for 3-class classification, where they improve gen-0 discrimination by capturing vocabulary diversity patterns absent in reference-model entropy statistics (Full 3-class F1\\,=\\,0.773 vs.\\ Reference-only 0.713).\nPermutation importance: hapax ratio (0.35), entropy mean (0.23), TTR (0.18).\nLeave-one-feature-out confirms 6 of 7 features contribute positively (Appendix~\\ref{app:lofo}).",
    "newString": "\\paragraph{Feature complementarity.}\nUnder 10-fold stratified CV, the full 7-feature set (F1\\,=\\,0.773) significantly outperforms surface-only (F1\\,=\\,0.688) and reference-only (F1\\,=\\,0.713; McNemar $p \\approx 0$; Table~\\ref{tab:ablation}).\nSurface and reference features are complementary: surface features improve gen-0 discrimination, while reference features dominate binary depth separation.\nPermutation importance: hapax ratio (0.35), entropy mean (0.23), TTR (0.18); leave-one-feature-out confirms 6 of 7 features contribute positively (Appendix~\\ref{app:lofo}).",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 69,
        "oldLines": 10,
        "newStart": 69,
        "newLines": 8,
        "lines": [
          " ",
          " \\paragraph{Feature complementarity.}",
          " Under 10-fold stratified CV, the full 7-feature set (F1\\,=\\,0.773) significantly outperforms surface-only (F1\\,=\\,0.688) and reference-only (F1\\,=\\,0.713; McNemar $p \\approx 0$; Table~\\ref{tab:ablation}).",
          "-Reference-only features yield higher binary F1 (0.833 vs.\\ 0.695 for the full ensemble) because surface lexical features introduce noise at the gen-1/gen-2+ boundary.",
          "-However, surface features are essential for 3-class classification, where they improve gen-0 discrimination by capturing vocabulary diversity patterns absent in reference-model entropy statistics (Full 3-class F1\\,=\\,0.773 vs.\\ Reference-only 0.713).",
          "-Permutation importance: hapax ratio (0.35), entropy mean (0.23), TTR (0.18).",
          "-Leave-one-feature-out confirms 6 of 7 features contribute positively (Appendix~\\ref{app:lofo}).",
          "+Surface and reference features are complementary: surface features improve gen-0 discrimination, while reference features dominate binary depth separation.",
          "+Permutation importance: hapax ratio (0.35), entropy mean (0.23), TTR (0.18); leave-one-feature-out confirms 6 of 7 features contribute positively (Appendix~\\ref{app:lofo}).",
          " ",
          " \\paragraph{Cross-family reference models.}",
          " Alternative references (OLMo-2-1B, Qwen3-0.6B) achieve comparable LOGO F1 (spread 0.013; Table~\\ref{tab:cross-ref}), confirming DDR is not reference-specific."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "c8609b8d-ca54-49b0-9ebf-036f19a4dc8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Assistant

_source line 5831 · 2026-05-17T15:52:39.560Z_

Now compile to check if Conclusion fits on page 8.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fadba9e1-4d56-4503-878d-b91bf5741bf0",
  "isSidechain": false,
  "requestId": "req_011Cb8QhyDgVbgLtujkE4htc",
  "type": "assistant",
  "uuid": "156f56a4-b12b-4aef-9e02-c20da05ddb40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AibpKf2mjyZfLNN85z34Yk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 74275,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 643,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 74275,
          "cache_creation_input_tokens": 643,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 643
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

_source line 5832 · 2026-05-17T15:52:40.506Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_015iu4dTAxoPt1VwCW8Nmx3k`</summary>

```json
{
  "project": "gen-depth-fingerprint",
  "max_pages": 8,
  "min_pages": 8,
  "clean": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "156f56a4-b12b-4aef-9e02-c20da05ddb40",
  "isSidechain": false,
  "requestId": "req_011Cb8QhyDgVbgLtujkE4htc",
  "type": "assistant",
  "uuid": "1ed02b9c-f852-4053-a588-c88ee8aab103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AibpKf2mjyZfLNN85z34Yk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 74275,
      "output_tokens": 140,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 643,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 140,
          "cache_read_input_tokens": 74275,
          "cache_creation_input_tokens": 643,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 643
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

_source line 5833 · 2026-05-17T15:52:43.823Z_

<details><summary>↩ Tool result · `toolu_015iu4dTAxoPt1VwCW8Nmx3k`</summary>

```text
{"result":"{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"Package pdftex.def Info: ../chart/fig_appendix_confusion.pdf  used on input lin\\ne 49.\\n(pdftex.def)             Requested size: 386.96027pt x 146.88148pt.\\n<../chart/fig_appendix_per_gen.pdf, id=816, 697.08195pt x 334.55302pt>\\nFile: ../chart/fig_appendix_per_gen.pdf Graphic file (type pdf)\\n&lt;use ../chart/fig_appendix_per_gen.pdf>\\nPackage pdftex.def Info: ../chart/fig_appendix_per_gen.pdf  used on input line \\n63.\\n(pdftex.def)             Requested size: 455.24411pt x 218.48807pt.\\n) (./appendix_cross_temp.tex\\n<../chart/fig_appendix_cross_temp.pdf, id=818, 681.36423pt x 205.48087pt>\\nFile: ../chart/fig_appendix_cross_temp.pdf Graphic file (type pdf)\\n&lt;use ../chart/fig_appendix_cross_temp.pdf>\\nPackage pdftex.def Info: ../chart/fig_appendix_cross_temp.pdf  used on input li\\nne 6.\\n(pdftex.def)             Requested size: 455.24411pt x 137.29208pt.\\n\\nUnderfull \\\\hbox (badness 2318) in paragraph at lines 14--15\\n[]\\\\OT1/ptm/b/n/10.95 Matched-temperature ro-bust-ness\\\\OT1/ptm/m/n/10.95 : Both\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1596) in paragraph at lines 20--21\\n[]\\\\OT1/ptm/b/n/10.95 Binary ro-bust-ness\\\\OT1/ptm/m/n/10.95 : Bi-nary clas-si-fi\\n-ca-tion\\n []\\n\\n\\nUnderfull \\\\hbox (badness 3088) in paragraph at lines 20--21\\n\\\\OT1/ptm/m/n/10.95 (gen-0/1 vs. gen-2+) is more ro-bust to\\n []\\n\\n) [20\\n\\n] [21 <../chart/fig_appendix_violin.pdf>] [22 <../chart/fig_appendix_ddr_trends\\n.pdf> <../chart/fig_appendix_umap.pdf>] [23 <../chart/fig_appendix_confusion.pd\\nf> <../chart/fig_appendix_per_gen.pdf> <../chart/fig_appendix_cross_temp.pdf>] \\n(./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\n\\n\\nLaTeX Warning: There were undefined references.\\n\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 02C04B264EFD503E3903600144F58112;5530.\\n ) \\nHere is how much of TeX's memory you used:\\n 13561 strings out of 469438\\n 216033 string characters out of 5468411\\n 667729 words of memory out of 5000000\\n 41760 multiletter control sequences out of 15000+600000\\n 661166 words of font info for 112 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,14n,93p,720b,677s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texliv\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/f\\nonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\\nc/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\\nts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\\nsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pf\\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/\\ntexlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\\ntype1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\\n/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (23 pages, 2744832 bytes).\\nPDF statistics:\\n 1410 PDF objects out of 1440 (max. 8388607)\\n 794 compressed objects within 8 object streams\\n 206 named destinations out of 1000 (max. 500000)\\n 302 words of extra memory for PDF output out of 10000 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 23, \"warnings\": [\"Reference `app:cross-model-detail' on page 6 undefined on input\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"There were undefined references.\"]}, \"pages\": 23, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": 8, \"critical_warnings\": [\"Reference `app:cross-model-detail' on page 6 undefined on input\", \"There were undefined references.\"], \"minor_warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Underfull \\\\hbox (badness 2005) in paragraph at lines 3--9\", \"Underfull \\\\hbox (badness 1297) in paragraph at lines 3--9\", \"Underfull \\\\hbox (badness 1509) in paragraph at lines 11--14\", \"Underfull \\\\hbox (badness 1824) in paragraph at lines 11--14\", \"Underfull \\\\hbox (badness 1502) in paragraph at lines 11--14\", \"Underfull \\\\hbox (badness 1194) in paragraph at lines 11--14\", \"Underfull \\\\hbox (badness 1360) in paragraph at lines 15--17\", \"Underfull \\\\hbox (badness 1354) in paragraph at lines 21--22\", \"Underfull \\\\hbox (badness 1097) in paragraph at lines 21--22\", \"Underfull \\\\hbox (badness 2165) in paragraph at lines 7--15\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 7--15\", \"Underfull \\\\hbox (badness 1430) in paragraph at lines 28--32\", \"Underfull \\\\hbox (badness 1281) in paragraph at lines 43--1\", \"Underfull \\\\hbox (badness 5431) in paragraph at lines 23--25\", \"Underfull \\\\hbox (badness 2698) in paragraph at lines 23--25\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 23--25\", \"Underfull \\\\hbox (badness 3907) in paragraph at lines 23--25\", \"Underfull \\\\hbox (badness 1661) in paragraph at lines 26--35\", \"Underfull \\\\hbox (badness 1629) in paragraph at lines 39--43\", \"Underfull \\\\hbox (badness 1571) in paragraph at lines 47--50\", \"Underfull \\\\hbox (badness 2073) in paragraph at lines 69--72\", \"Underfull \\\\hbox (badness 7256) in paragraph at lines 77--79\", \"Underfull \\\\hbox (badness 7522) in paragraph at lines 77--79\", \"Underfull \\\\hbox (badness 2293) in paragraph at lines 77--79\", \"Underfull \\\\hbox (badness 1112) in paragraph at lines 77--79\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 81--87\", \"Underfull \\\\hbox (badness 3612) in paragraph at lines 81--87\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 81--87\", \"Underfull \\\\hbox (badness 2671) in paragraph at lines 81--87\", \"Underfull \\\\hbox (badness 5460) in paragraph at lines 81--87\", \"Underfull \\\\hbox (badness 2050) in paragraph at lines 81--87\", \"Underfull \\\\hbox (badness 3229) in paragraph at lines 81--87\", \"Underfull \\\\hbox (badness 1701) in paragraph at lines 89--96\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 89--96\", \"Underfull \\\\hbox (badness 1199) in paragraph at lines 98--100\", \"Underfull \\\\hbox (badness 1281) in paragraph at lines 7--11\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 13--15\", \"Underfull \\\\hbox (badness 1424) in paragraph at lines 13--15\", \"Underfull \\\\hbox (badness 5817) in paragraph at lines 13--15\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 16--19\", \"Underfull \\\\hbox (badness 1648) in paragraph at lines 16--19\", \"Underfull \\\\hbox (badness 1281) in paragraph at lines 16--19\", \"Underfull \\\\hbox (badness 2990) in paragraph at lines 16--19\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 21--22\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 21--22\", \"Underfull \\\\hbox (badness 1776) in paragraph at lines 21--22\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 51--52\", \"Underfull \\\\hbox (badness 3229) in paragraph at lines 51--52\", \"Underfull \\\\hbox (badness 1803) in paragraph at lines 51--52\", \"Underfull \\\\hbox (badness 2359) in paragraph at lines 51--52\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 65--69\", \"Underfull \\\\hbox (badness 6995) in paragraph at lines 65--69\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 65--69\", \"Underfull \\\\hbox (badness 3568) in paragraph at lines 65--69\", \"Underfull \\\\hbox (badness 5652) in paragraph at lines 65--69\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 76--77\", \"Underfull \\\\hbox (badness 1189) in paragraph at lines 76--77\", \"Underfull \\\\hbox (badness 6691) in paragraph at lines 130--130\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 4242) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 3826) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 4391) in paragraph at lines 14--18\", \"Underfull \\\\hbox (badness 1337) in paragraph at lines 20--22\", \"Underfull \\\\hbox (badness 3417) in paragraph at lines 24--1\", \"Underfull \\\\hbox (badness 2653) in paragraph at lines 24--1\", \"Underfull \\\\hbox (badness 4242) in paragraph at lines 4--10\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 4--10\", \"Underfull \\\\hbox (badness 1371) in paragraph at lines 4--10\", \"Underfull \\\\hbox (badness 1466) in paragraph at lines 4--10\", \"Underfull \\\\hbox (badness 1609) in paragraph at lines 4--10\", \"Underfull \\\\hbox (badness 1009) in paragraph at lines 4--10\", \"Underfull \\\\hbox (badness 1137) in paragraph at lines 11--14\", \"Underfull \\\\hbox (badness 7740) in paragraph at lines 15--18\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 15--18\", \"Underfull \\\\hbox (badness 1394) in paragraph at lines 15--18\", \"Underfull \\\\hbox (badness 3769) in paragraph at lines 19--21\", \"Underfull \\\\hbox (badness 1960) in paragraph at lines 56--61\", \"Underfull \\\\hbox (badness 1033) in paragraph at lines 112--116\", \"Underfull \\\\hbox (badness 3058) in paragraph at lines 120--128\", \"Underfull \\\\hbox (badness 1024) in paragraph at lines 131--136\", \"Underfull \\\\hbox (badness 3514) in paragraph at lines 143--150\", \"Underfull \\\\hbox (badness 1924) in paragraph at lines 143--150\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 170--176\", \"Underfull \\\\hbox (badness 1810) in paragraph at lines 170--176\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 170--176\", \"Underfull \\\\hbox (badness 2111) in paragraph at lines 191--195\", \"Underfull \\\\hbox (badness 2486) in paragraph at lines 198--203\", \"Underfull \\\\hbox (badness 1789) in paragraph at lines 198--203\", \"Underfull \\\\hbox (badness 1533) in paragraph at lines 198--203\", \"Underfull \\\\hbox (badness 4686) in paragraph at lines 206--211\", \"Underfull \\\\hbox (badness 5147) in paragraph at lines 261--265\", \"Underfull \\\\hbox (badness 1320) in paragraph at lines 268--274\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 383--389\", \"Underfull \\\\hbox (badness 1005) in paragraph at lines 383--389\", \"Underfull \\\\hbox (badness 2452) in paragraph at lines 383--389\", \"Underfull \\\\hbox (badness 1769) in paragraph at lines 442--448\", \"Underfull \\\\hbox (badness 1590) in paragraph at lines 442--448\", \"Underfull \\\\hbox (badness 1102) in paragraph at lines 442--448\", \"Underfull \\\\hbox (badness 3375) in paragraph at lines 451--455\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 38--40\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 38--40\", \"Underfull \\\\hbox (badness 2990) in paragraph at lines 38--40\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 13--17\", \"Underfull \\\\hbox (badness 5302) in paragraph at lines 13--17\", \"Underfull \\\\hbox (badness 7558) in paragraph at lines 13--17\", \"Underfull \\\\hbox (badness 2799) in paragraph at lines 19--22\", \"Underfull \\\\hbox (badness 1184) in paragraph at lines 19--22\", \"Underfull \\\\hbox (badness 1259) in paragraph at lines 19--22\", \"Underfull \\\\hbox (badness 2418) in paragraph at lines 1--2\", \"Underfull \\\\hbox (badness 2277) in paragraph at lines 1--2\", \"Underfull \\\\hbox (badness 4779) in paragraph at lines 1--2\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--50\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--50\", \"Underfull \\\\hbox (badness 1142) in paragraph at lines 7--50\", \"Underfull \\\\hbox (badness 1168) in paragraph at lines 7--50\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 50--54\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 3746) in paragraph at lines 4--7\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 25--28\", \"Underfull \\\\hbox (badness 1675) in paragraph at lines 25--28\", \"Underfull \\\\hbox (badness 2359) in paragraph at lines 25--28\", \"Underfull \\\\hbox (badness 3333) in paragraph at lines 30--31\", \"Underfull \\\\hbox (badness 1577) in paragraph at lines 30--31\", \"Underfull \\\\hbox (badness 7308) in paragraph at lines 21--21\", \"Underfull \\\\hbox (badness 6016) in paragraph at lines 1--2\", \"Underfull \\\\hbox (badness 1097) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 1540) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 3668) in paragraph at lines 25--27\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 29--35\", \"Underfull \\\\hbox (badness 3815) in paragraph at lines 29--35\", \"Underfull \\\\hbox (badness 1571) in paragraph at lines 78--83\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 85--90\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 85--90\", \"Underfull \\\\hbox (badness 1163) in paragraph at lines 85--90\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 85--90\", \"Underfull \\\\hbox (badness 4168) in paragraph at lines 85--90\", \"Underfull \\\\hbox (badness 1953) in paragraph at lines 85--90\", \"Underfull \\\\hbox (badness 2221) in paragraph at lines 85--90\", \"Underfull \\\\hbox (badness 2142) in paragraph at lines 24--28\", \"Underfull \\\\hbox (badness 4353) in paragraph at lines 24--28\", \"Underfull \\\\hbox (badness 1043) in paragraph at lines 24--28\", \"Underfull \\\\hbox (badness 2503) in paragraph at lines 24--28\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 24--28\", \"Underfull \\\\hbox (badness 1946) in paragraph at lines 30--78\", \"Underfull \\\\hbox (badness 1163) in paragraph at lines 1--2\", \"Underfull \\\\hbox (badness 2310) in paragraph at lines 1--2\", \"Underfull \\\\hbox (badness 2393) in paragraph at lines 8--11\", \"Underfull \\\\hbox (badness 1975) in paragraph at lines 8--11\", \"Underfull \\\\hbox (badness 2689) in paragraph at lines 38--82\", \"Underfull \\\\hbox (badness 2698) in paragraph at lines 22--26\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 5711) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 1490) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 4024) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 2903) in paragraph at lines 31--34\", \"Underfull \\\\hbox (badness 2351) in paragraph at lines 31--34\", \"Underfull \\\\hbox (badness 2318) in paragraph at lines 14--15\", \"Underfull \\\\hbox (badness 1596) in paragraph at lines 20--21\", \"Underfull \\\\hbox (badness 3088) in paragraph at lines 20--21\"], \"issues\": [\"2 critical warning(s): Reference `app:cross-model-detail' on page 6 undefined on input; There were undefined references.\", \"pages 23 > limit 8\"], \"summary\": \"FAIL: 2 critical warning(s): Reference `app:cross-model-detail' on page 6 undefined on input; There were undefined references.; pages 23 > limit 8\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ed02b9c-f852-4053-a588-c88ee8aab103",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "93cf02a5-b7b3-465b-911a-0746156261c3",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"passed\\\": false, \\\"compiled\\\": {\\\"success\\\": true, \\\"pdf_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf\\\", \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"Package pdftex.def Info: ../chart/fig_appendix_confusion.pdf  used on input lin\\\\ne 49.\\\\n(pdftex.def)             Requested size: 386.96027pt x 146.88148pt.\\\\n<../chart/fig_appendix_per_gen.pdf, id=816, 697.08195pt x 334.55302pt>\\\\nFile: ../chart/fig_appendix_per_gen.pdf Graphic file (type pdf)\\\\n&lt;use ../chart/fig_appendix_per_gen.pdf>\\\\nPackage pdftex.def Info: ../chart/fig_appendix_per_gen.pdf  used on input line \\\\n63.\\\\n(pdftex.def)             Requested size: 455.24411pt x 218.48807pt.\\\\n) (./appendix_cross_temp.tex\\\\n<../chart/fig_appendix_cross_temp.pdf, id=818, 681.36423pt x 205.48087pt>\\\\nFile: ../chart/fig_appendix_cross_temp.pdf Graphic file (type pdf)\\\\n&lt;use ../chart/fig_appendix_cross_temp.pdf>\\\\nPackage pdftex.def Info: ../chart/fig_appendix_cross_temp.pdf  used on input li\\\\nne 6.\\\\n(pdftex.def)             Requested size: 455.24411pt x 137.29208pt.\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 2318) in paragraph at lines 14--15\\\\n[]\\\\\\\\OT1/ptm/b/n/10.95 Matched-temperature ro-bust-ness\\\\\\\\OT1/ptm/m/n/10.95 : Both\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1596) in paragraph at lines 20--21\\\\n[]\\\\\\\\OT1/ptm/b/n/10.95 Binary ro-bust-ness\\\\\\\\OT1/ptm/m/n/10.95 : Bi-nary clas-si-fi\\\\n-ca-tion\\\\n []\\\\n\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 3088) in paragraph at lines 20--21\\\\n\\\\\\\\OT1/ptm/m/n/10.95 (gen-0/1 vs. gen-2+) is more ro-bust to\\\\n []\\\\n\\\\n) [20\\\\n\\\\n] [21 <../chart/fig_appendix_violin.pdf>] [22 <../chart/fig_appendix_ddr_trends\\\\n.pdf> <../chart/fig_appendix_umap.pdf>] [23 <../chart/fig_appendix_confusion.pd\\\\nf> <../chart/fig_appendix_per_gen.pdf> <../chart/fig_appendix_cross_temp.pdf>] \\\\n(./main.aux)\\\\n ***********\\\\nLaTeX2e <2025-11-01>\\\\nL3 programming layer <2026-01-19>\\\\n ***********\\\\n\\\\n\\\\nLaTeX Warning: There were undefined references.\\\\n\\\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\\\n(rerunfilecheck)             Checksum: 02C04B264EFD503E3903600144F58112;5530.\\\\n ) \\\\nHere is how much of TeX's memory you used:\\\\n 13561 strings out of 469438\\\\n 216033 string characters out of 5468411\\\\n 667729 words of memory out of 5000000\\\\n 41760 multiletter control sequences out of 15000+600000\\\\n 661166 words of font info for 112 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,14n,93p,720b,677s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr\\\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share\\\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texliv\\\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf\\\\n-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/f\\\\nonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\\\ne1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\\\\nc/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\\\\nts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\\\\nsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pf\\\\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr\\\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/\\\\ntexlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf\\\\n-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\\\\ntype1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\\\\n/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\\\nOutput written on main.pdf (23 pages, 2744832 bytes).\\\\nPDF statistics:\\\\n 1410 PDF objects out of 1440 (max. 8388607)\\\\n 794 compressed objects within 8 object streams\\\\n 206 named destinations out of 1000 (max. 500000)\\\\n 302 words of extra memory for PDF output out of 10000 (max. 10000000)\\\\n\\\", \\\"error\\\": \\\"\\\", \\\"pages\\\": 23, \\\"warnings\\\": [\\\"Reference `app:cross-model-detail' on page 6 undefined on input\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"There were undefined references.\\\"]}, \\\"pages\\\": 23, \\\"page_status\\\": \\\"over_limit\\\", \\\"max_pages\\\": 8, \\\"min_pages\\\": 8, \\\"critical_warnings\\\": [\\\"Reference `app:cross-model-detail' on page 6 undefined on input\\\", \\\"There were undefined references.\\\"], \\\"minor_warnings\\\": [\\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"Underfull \\\\\\\\hbox (badness 2005) in paragraph at lines 3--9\\\", \\\"Underfull \\\\\\\\hbox (badness 1297) in paragraph at lines 3--9\\\", \\\"Underfull \\\\\\\\hbox (badness 1509) in paragraph at lines 11--14\\\", \\\"Underfull \\\\\\\\hbox (badness 1824) in paragraph at lines 11--14\\\", \\\"Underfull \\\\\\\\hbox (badness 1502) in paragraph at lines 11--14\\\", \\\"Underfull \\\\\\\\hbox (badness 1194) in paragraph at lines 11--14\\\", \\\"Underfull \\\\\\\\hbox (badness 1360) in paragraph at lines 15--17\\\", \\\"Underfull \\\\\\\\hbox (badness 1354) in paragraph at lines 21--22\\\", \\\"Underfull \\\\\\\\hbox (badness 1097) in paragraph at lines 21--22\\\", \\\"Underfull \\\\\\\\hbox (badness 2165) in paragraph at lines 7--15\\\", \\\"Underfull \\\\\\\\hbox (badness 1406) in paragraph at lines 7--15\\\", \\\"Underfull \\\\\\\\hbox (badness 1430) in paragraph at lines 28--32\\\", \\\"Underfull \\\\\\\\hbox (badness 1281) in paragraph at lines 43--1\\\", \\\"Underfull \\\\\\\\hbox (badness 5431) in paragraph at lines 23--25\\\", \\\"Underfull \\\\\\\\hbox (badness 2698) in paragraph at lines 23--25\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 23--25\\\", \\\"Underfull \\\\\\\\hbox (badness 3907) in paragraph at lines 23--25\\\", \\\"Underfull \\\\\\\\hbox (badness 1661) in paragraph at lines 26--35\\\", \\\"Underfull \\\\\\\\hbox (badness 1629) in paragraph at lines 39--43\\\", \\\"Underfull \\\\\\\\hbox (badness 1571) in paragraph at lines 47--50\\\", \\\"Underfull \\\\\\\\hbox (badness 2073) in paragraph at lines 69--72\\\", \\\"Underfull \\\\\\\\hbox (badness 7256) in paragraph at lines 77--79\\\", \\\"Underfull \\\\\\\\hbox (badness 7522) in paragraph at lines 77--79\\\", \\\"Underfull \\\\\\\\hbox (badness 2293) in paragraph at lines 77--79\\\", \\\"Underfull \\\\\\\\hbox (badness 1112) in paragraph at lines 77--79\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 81--87\\\", \\\"Underfull \\\\\\\\hbox (badness 3612) in paragraph at lines 81--87\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 81--87\\\", \\\"Underfull \\\\\\\\hbox (badness 2671) in paragraph at lines 81--87\\\", \\\"Underfull \\\\\\\\hbox (badness 5460) in paragraph at lines 81--87\\\", \\\"Underfull \\\\\\\\hbox (badness 2050) in paragraph at lines 81--87\\\", \\\"Underfull \\\\\\\\hbox (badness 3229) in paragraph at lines 81--87\\\", \\\"Underfull \\\\\\\\hbox (badness 1701) in paragraph at lines 89--96\\\", \\\"Underfull \\\\\\\\hbox (badness 1062) in paragraph at lines 89--96\\\", \\\"Underfull \\\\\\\\hbox (badness 1199) in paragraph at lines 98--100\\\", \\\"Underfull \\\\\\\\hbox (badness 1281) in paragraph at lines 7--11\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 13--15\\\", \\\"Underfull \\\\\\\\hbox (badness 1424) in paragraph at lines 13--15\\\", \\\"Underfull \\\\\\\\hbox (badness 5817) in paragraph at lines 13--15\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 16--19\\\", \\\"Underfull \\\\\\\\hbox (badness 1648) in paragraph at lines 16--19\\\", \\\"Underfull \\\\\\\\hbox (badness 1281) in paragraph at lines 16--19\\\", \\\"Underfull \\\\\\\\hbox (badness 2990) in paragraph at lines 16--19\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 21--22\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 21--22\\\", \\\"Underfull \\\\\\\\hbox (badness 1776) in paragraph at lines 21--22\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 51--52\\\", \\\"Underfull \\\\\\\\hbox (badness 3229) in paragraph at lines 51--52\\\", \\\"Underfull \\\\\\\\hbox (badness 1803) in paragraph at lines 51--52\\\", \\\"Underfull \\\\\\\\hbox (badness 2359) in paragraph at lines 51--52\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 65--69\\\", \\\"Underfull \\\\\\\\hbox (badness 6995) in paragraph at lines 65--69\\\", \\\"Underfull \\\\\\\\hbox (badness 1400) in paragraph at lines 65--69\\\", \\\"Underfull \\\\\\\\hbox (badness 3568) in paragraph at lines 65--69\\\", \\\"Underfull \\\\\\\\hbox (badness 5652) in paragraph at lines 65--69\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 76--77\\\", \\\"Underfull \\\\\\\\hbox (badness 1189) in paragraph at lines 76--77\\\", \\\"Underfull \\\\\\\\hbox (badness 6691) in paragraph at lines 130--130\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 10--12\\\", \\\"Underfull \\\\\\\\hbox (badness 4242) in paragraph at lines 10--12\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 10--12\\\", \\\"Underfull \\\\\\\\hbox (badness 3826) in paragraph at lines 10--12\\\", \\\"Underfull \\\\\\\\hbox (badness 4391) in paragraph at lines 14--18\\\", \\\"Underfull \\\\\\\\hbox (badness 1337) in paragraph at lines 20--22\\\", \\\"Underfull \\\\\\\\hbox (badness 3417) in paragraph at lines 24--1\\\", \\\"Underfull \\\\\\\\hbox (badness 2653) in paragraph at lines 24--1\\\", \\\"Underfull \\\\\\\\hbox (badness 4242) in paragraph at lines 4--10\\\", \\\"Underfull \\\\\\\\hbox (badness 1406) in paragraph at lines 4--10\\\", \\\"Underfull \\\\\\\\hbox (badness 1371) in paragraph at lines 4--10\\\", \\\"Underfull \\\\\\\\hbox (badness 1466) in paragraph at lines 4--10\\\", \\\"Underfull \\\\\\\\hbox (badness 1609) in paragraph at lines 4--10\\\", \\\"Underfull \\\\\\\\hbox (badness 1009) in paragraph at lines 4--10\\\", \\\"Underfull \\\\\\\\hbox (badness 1137) in paragraph at lines 11--14\\\", \\\"Underfull \\\\\\\\hbox (badness 7740) in paragraph at lines 15--18\\\", \\\"Underfull \\\\\\\\hbox (badness 1226) in paragraph at lines 15--18\\\", \\\"Underfull \\\\\\\\hbox (badness 1394) in paragraph at lines 15--18\\\", \\\"Underfull \\\\\\\\hbox (badness 3769) in paragraph at lines 19--21\\\", \\\"Underfull \\\\\\\\hbox (badness 1960) in paragraph at lines 56--61\\\", \\\"Underfull \\\\\\\\hbox (badness 1033) in paragraph at lines 112--116\\\", \\\"Underfull \\\\\\\\hbox (badness 3058) in paragraph at lines 120--128\\\", \\\"Underfull \\\\\\\\hbox (badness 1024) in paragraph at lines 131--136\\\", \\\"Underfull \\\\\\\\hbox (badness 3514) in paragraph at lines 143--150\\\", \\\"Underfull \\\\\\\\hbox (badness 1924) in paragraph at lines 143--150\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 170--176\\\", \\\"Underfull \\\\\\\\hbox (badness 1810) in paragraph at lines 170--176\\\", \\\"Underfull \\\\\\\\hbox (badness 1400) in paragraph at lines 170--176\\\", \\\"Underfull \\\\\\\\hbox (badness 2111) in paragraph at lines 191--195\\\", \\\"Underfull \\\\\\\\hbox (badness 2486) in paragraph at lines 198--203\\\", \\\"Underfull \\\\\\\\hbox (badness 1789) in paragraph at lines 198--203\\\", \\\"Underfull \\\\\\\\hbox (badness 1533) in paragraph at lines 198--203\\\", \\\"Underfull \\\\\\\\hbox (badness 4686) in paragraph at lines 206--211\\\", \\\"Underfull \\\\\\\\hbox (badness 5147) in paragraph at lines 261--265\\\", \\\"Underfull \\\\\\\\hbox (badness 1320) in paragraph at lines 268--274\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 383--389\\\", \\\"Underfull \\\\\\\\hbox (badness 1005) in paragraph at lines 383--389\\\", \\\"Underfull \\\\\\\\hbox (badness 2452) in paragraph at lines 383--389\\\", \\\"Underfull \\\\\\\\hbox (badness 1769) in paragraph at lines 442--448\\\", \\\"Underfull \\\\\\\\hbox (badness 1590) in paragraph at lines 442--448\\\", \\\"Underfull \\\\\\\\hbox (badness 1102) in paragraph at lines 442--448\\\", \\\"Underfull \\\\\\\\hbox (badness 3375) in paragraph at lines 451--455\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 38--40\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 38--40\\\", \\\"Underfull \\\\\\\\hbox (badness 2990) in paragraph at lines 38--40\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 13--17\\\", \\\"Underfull \\\\\\\\hbox (badness 5302) in paragraph at lines 13--17\\\", \\\"Underfull \\\\\\\\hbox (badness 7558) in paragraph at lines 13--17\\\", \\\"Underfull \\\\\\\\hbox (badness 2799) in paragraph at lines 19--22\\\", \\\"Underfull \\\\\\\\hbox (badness 1184) in paragraph at lines 19--22\\\", \\\"Underfull \\\\\\\\hbox (badness 1259) in paragraph at lines 19--22\\\", \\\"Underfull \\\\\\\\hbox (badness 2418) in paragraph at lines 1--2\\\", \\\"Underfull \\\\\\\\hbox (badness 2277) in paragraph at lines 1--2\\\", \\\"Underfull \\\\\\\\hbox (badness 4779) in paragraph at lines 1--2\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 7--50\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 7--50\\\", \\\"Underfull \\\\\\\\hbox (badness 1142) in paragraph at lines 7--50\\\", \\\"Underfull \\\\\\\\hbox (badness 1168) in paragraph at lines 7--50\\\", \\\"Underfull \\\\\\\\hbox (badness 1210) in paragraph at lines 50--54\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 3746) in paragraph at lines 4--7\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 25--28\\\", \\\"Underfull \\\\\\\\hbox (badness 1675) in paragraph at lines 25--28\\\", \\\"Underfull \\\\\\\\hbox (badness 2359) in paragraph at lines 25--28\\\", \\\"Underfull \\\\\\\\hbox (badness 3333) in paragraph at lines 30--31\\\", \\\"Underfull \\\\\\\\hbox (badness 1577) in paragraph at lines 30--31\\\", \\\"Underfull \\\\\\\\hbox (badness 7308) in paragraph at lines 21--21\\\", \\\"Underfull \\\\\\\\hbox (badness 6016) in paragraph at lines 1--2\\\", \\\"Underfull \\\\\\\\hbox (badness 1097) in paragraph at lines 35--36\\\", \\\"Underfull \\\\\\\\hbox (badness 1540) in paragraph at lines 35--36\\\", \\\"Underfull \\\\\\\\hbox (badness 3668) in paragraph at lines 25--27\\\", \\\"Underfull \\\\\\\\hbox (badness 1221) in paragraph at lines 29--35\\\", \\\"Underfull \\\\\\\\hbox (badness 3815) in paragraph at lines 29--35\\\", \\\"Underfull \\\\\\\\hbox (badness 1571) in paragraph at lines 78--83\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 85--90\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 85--90\\\", \\\"Underfull \\\\\\\\hbox (badness 1163) in paragraph at lines 85--90\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 85--90\\\", \\\"Underfull \\\\\\\\hbox (badness 4168) in paragraph at lines 85--90\\\", \\\"Underfull \\\\\\\\hbox (badness 1953) in paragraph at lines 85--90\\\", \\\"Underfull \\\\\\\\hbox (badness 2221) in paragraph at lines 85--90\\\", \\\"Underfull \\\\\\\\hbox (badness 2142) in paragraph at lines 24--28\\\", \\\"Underfull \\\\\\\\hbox (badness 4353) in paragraph at lines 24--28\\\", \\\"Underfull \\\\\\\\hbox (badness 1043) in paragraph at lines 24--28\\\", \\\"Underfull \\\\\\\\hbox (badness 2503) in paragraph at lines 24--28\\\", \\\"Underfull \\\\\\\\hbox (badness 1210) in paragraph at lines 24--28\\\", \\\"Underfull \\\\\\\\hbox (badness 1946) in paragraph at lines 30--78\\\", \\\"Underfull \\\\\\\\hbox (badness 1163) in paragraph at lines 1--2\\\", \\\"Underfull \\\\\\\\hbox (badness 2310) in paragraph at lines 1--2\\\", \\\"Underfull \\\\\\\\hbox (badness 2393) in paragraph at lines 8--11\\\", \\\"Underfull \\\\\\\\hbox (badness 1975) in paragraph at lines 8--11\\\", \\\"Underfull \\\\\\\\hbox (badness 2689) in paragraph at lines 38--82\\\", \\\"Underfull \\\\\\\\hbox (badness 2698) in paragraph at lines 22--26\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 35--36\\\", \\\"Underfull \\\\\\\\hbox (badness 5711) in paragraph at lines 35--36\\\", \\\"Underfull \\\\\\\\hbox (badness 1490) in paragraph at lines 35--36\\\", \\\"Underfull \\\\\\\\hbox (badness 4024) in paragraph at lines 35--36\\\", \\\"Underfull \\\\\\\\hbox (badness 2903) in paragraph at lines 31--34\\\", \\\"Underfull \\\\\\\\hbox (badness 2351) in paragraph at lines 31--34\\\", \\\"Underfull \\\\\\\\hbox (badness 2318) in paragraph at lines 14--15\\\", \\\"Underfull \\\\\\\\hbox (badness 1596) in paragraph at lines 20--21\\\", \\\"Underfull \\\\\\\\hbox (badness 3088) in paragraph at lines 20--21\\\"], \\\"issues\\\": [\\\"2 critical warning(s): Reference `app:cross-model-detail' on page 6 undefined on input; There were undefined references.\\\", \\\"pages 23 > limit 8\\\"], \\\"summary\\\": \\\"FAIL: 2 critical warning(s): Reference `app:cross-model-detail' on page 6 undefined on input; There were undefined references.; pages 23 > limit 8\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"Package pdftex.def Info: ../chart/fig_appendix_confusion.pdf  used on input lin\\ne 49.\\n(pdftex.def)             Requested size: 386.96027pt x 146.88148pt.\\n<../chart/fig_appendix_per_gen.pdf, id=816, 697.08195pt x 334.55302pt>\\nFile: ../chart/fig_appendix_per_gen.pdf Graphic file (type pdf)\\n&lt;use ../chart/fig_appendix_per_gen.pdf>\\nPackage pdftex.def Info: ../chart/fig_appendix_per_gen.pdf  used on input line \\n63.\\n(pdftex.def)             Requested size: 455.24411pt x 218.48807pt.\\n) (./appendix_cross_temp.tex\\n<../chart/fig_appendix_cross_temp.pdf, id=818, 681.36423pt x 205.48087pt>\\nFile: ../chart/fig_appendix_cross_temp.pdf Graphic file (type pdf)\\n&lt;use ../chart/fig_appendix_cross_temp.pdf>\\nPackage pdftex.def Info: ../chart/fig_appendix_cross_temp.pdf  used on input li\\nne 6.\\n(pdftex.def)             Requested size: 455.24411pt x 137.29208pt.\\n\\nUnderfull \\\\hbox (badness 2318) in paragraph at lines 14--15\\n[]\\\\OT1/ptm/b/n/10.95 Matched-temperature ro-bust-ness\\\\OT1/ptm/m/n/10.95 : Both\\n []\\n\\n\\nUnderfull \\\\hbox (badness 1596) in paragraph at lines 20--21\\n[]\\\\OT1/ptm/b/n/10.95 Binary ro-bust-ness\\\\OT1/ptm/m/n/10.95 : Bi-nary clas-si-fi\\n-ca-tion\\n []\\n\\n\\nUnderfull \\\\hbox (badness 3088) in paragraph at lines 20--21\\n\\\\OT1/ptm/m/n/10.95 (gen-0/1 vs. gen-2+) is more ro-bust to\\n []\\n\\n) [20\\n\\n] [21 <../chart/fig_appendix_violin.pdf>] [22 <../chart/fig_appendix_ddr_trends\\n.pdf> <../chart/fig_appendix_umap.pdf>] [23 <../chart/fig_appendix_confusion.pd\\nf> <../chart/fig_appendix_per_gen.pdf> <../chart/fig_appendix_cross_temp.pdf>] \\n(./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\n\\n\\nLaTeX Warning: There were undefined references.\\n\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 02C04B264EFD503E3903600144F58112;5530.\\n ) \\nHere is how much of TeX's memory you used:\\n 13561 strings out of 469438\\n 216033 string characters out of 5468411\\n 667729 words of memory out of 5000000\\n 41760 multiletter control sequences out of 15000+600000\\n 661166 words of font info for 112 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,14n,93p,720b,677s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texliv\\ne/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/f\\nonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\\nc/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\\nts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\\nsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pf\\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/\\ntexlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\\ntype1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times\\n/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (23 pages, 2744832 bytes).\\nPDF statistics:\\n 1410 PDF objects out of 1440 (max. 8388607)\\n 794 compressed objects within 8 object streams\\n 206 named destinations out of 1000 (max. 500000)\\n 302 words of extra memory for PDF output out of 10000 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 23, \"warnings\": [\"Reference `app:cross-model-detail' on page 6 undefined on input\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"There were undefined references.\"]}, \"pages\": 23, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": 8, \"critical_warnings\": [\"Reference `app:cross-model-detail' on page 6 undefined on input\", \"There were undefined references.\"], \"minor_warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Underfull \\\\hbox (badness 2005) in paragraph at lines 3--9\", \"Underfull \\\\hbox (badness 1297) in paragraph at lines 3--9\", \"Underfull \\\\hbox (badness 1509) in paragraph at lines 11--14\", \"Underfull \\\\hbox (badness 1824) in paragraph at lines 11--14\", \"Underfull \\\\hbox (badness 1502) in paragraph at lines 11--14\", \"Underfull \\\\hbox (badness 1194) in paragraph at lines 11--14\", \"Underfull \\\\hbox (badness 1360) in paragraph at lines 15--17\", \"Underfull \\\\hbox (badness 1354) in paragraph at lines 21--22\", \"Underfull \\\\hbox (badness 1097) in paragraph at lines 21--22\", \"Underfull \\\\hbox (badness 2165) in paragraph at lines 7--15\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 7--15\", \"Underfull \\\\hbox (badness 1430) in paragraph at lines 28--32\", \"Underfull \\\\hbox (badness 1281) in paragraph at lines 43--1\", \"Underfull \\\\hbox (badness 5431) in paragraph at lines 23--25\", \"Underfull \\\\hbox (badness 2698) in paragraph at lines 23--25\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 23--25\", \"Underfull \\\\hbox (badness 3907) in paragraph at lines 23--25\", \"Underfull \\\\hbox (badness 1661) in paragraph at lines 26--35\", \"Underfull \\\\hbox (badness 1629) in paragraph at lines 39--43\", \"Underfull \\\\hbox (badness 1571) in paragraph at lines 47--50\", \"Underfull \\\\hbox (badness 2073) in paragraph at lines 69--72\", \"Underfull \\\\hbox (badness 7256) in paragraph at lines 77--79\", \"Underfull \\\\hbox (badness 7522) in paragraph at lines 77--79\", \"Underfull \\\\hbox (badness 2293) in paragraph at lines 77--79\", \"Underfull \\\\hbox (badness 1112) in paragraph at lines 77--79\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 81--87\", \"Underfull \\\\hbox (badness 3612) in paragraph at lines 81--87\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 81--87\", \"Underfull \\\\hbox (badness 2671) in paragraph at lines 81--87\", \"Underfull \\\\hbox (badness 5460) in paragraph at lines 81--87\", \"Underfull \\\\hbox (badness 2050) in paragraph at lines 81--87\", \"Underfull \\\\hbox (badness 3229) in paragraph at lines 81--87\", \"Underfull \\\\hbox (badness 1701) in paragraph at lines 89--96\", \"Underfull \\\\hbox (badness 1062) in paragraph at lines 89--96\", \"Underfull \\\\hbox (badness 1199) in paragraph at lines 98--100\", \"Underfull \\\\hbox (badness 1281) in paragraph at lines 7--11\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 13--15\", \"Underfull \\\\hbox (badness 1424) in paragraph at lines 13--15\", \"Underfull \\\\hbox (badness 5817) in paragraph at lines 13--15\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 16--19\", \"Underfull \\\\hbox (badness 1648) in paragraph at lines 16--19\", \"Underfull \\\\hbox (badness 1281) in paragraph at lines 16--19\", \"Underfull \\\\hbox (badness 2990) in paragraph at lines 16--19\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 21--22\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 21--22\", \"Underfull \\\\hbox (badness 1776) in paragraph at lines 21--22\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 51--52\", \"Underfull \\\\hbox (badness 3229) in paragraph at lines 51--52\", \"Underfull \\\\hbox (badness 1803) in paragraph at lines 51--52\", \"Underfull \\\\hbox (badness 2359) in paragraph at lines 51--52\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 65--69\", \"Underfull \\\\hbox (badness 6995) in paragraph at lines 65--69\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 65--69\", \"Underfull \\\\hbox (badness 3568) in paragraph at lines 65--69\", \"Underfull \\\\hbox (badness 5652) in paragraph at lines 65--69\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 76--77\", \"Underfull \\\\hbox (badness 1189) in paragraph at lines 76--77\", \"Underfull \\\\hbox (badness 6691) in paragraph at lines 130--130\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 4242) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 3826) in paragraph at lines 10--12\", \"Underfull \\\\hbox (badness 4391) in paragraph at lines 14--18\", \"Underfull \\\\hbox (badness 1337) in paragraph at lines 20--22\", \"Underfull \\\\hbox (badness 3417) in paragraph at lines 24--1\", \"Underfull \\\\hbox (badness 2653) in paragraph at lines 24--1\", \"Underfull \\\\hbox (badness 4242) in paragraph at lines 4--10\", \"Underfull \\\\hbox (badness 1406) in paragraph at lines 4--10\", \"Underfull \\\\hbox (badness 1371) in paragraph at lines 4--10\", \"Underfull \\\\hbox (badness 1466) in paragraph at lines 4--10\", \"Underfull \\\\hbox (badness 1609) in paragraph at lines 4--10\", \"Underfull \\\\hbox (badness 1009) in paragraph at lines 4--10\", \"Underfull \\\\hbox (badness 1137) in paragraph at lines 11--14\", \"Underfull \\\\hbox (badness 7740) in paragraph at lines 15--18\", \"Underfull \\\\hbox (badness 1226) in paragraph at lines 15--18\", \"Underfull \\\\hbox (badness 1394) in paragraph at lines 15--18\", \"Underfull \\\\hbox (badness 3769) in paragraph at lines 19--21\", \"Underfull \\\\hbox (badness 1960) in paragraph at lines 56--61\", \"Underfull \\\\hbox (badness 1033) in paragraph at lines 112--116\", \"Underfull \\\\hbox (badness 3058) in paragraph at lines 120--128\", \"Underfull \\\\hbox (badness 1024) in paragraph at lines 131--136\", \"Underfull \\\\hbox (badness 3514) in paragraph at lines 143--150\", \"Underfull \\\\hbox (badness 1924) in paragraph at lines 143--150\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 170--176\", \"Underfull \\\\hbox (badness 1810) in paragraph at lines 170--176\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 170--176\", \"Underfull \\\\hbox (badness 2111) in paragraph at lines 191--195\", \"Underfull \\\\hbox (badness 2486) in paragraph at lines 198--203\", \"Underfull \\\\hbox (badness 1789) in paragraph at lines 198--203\", \"Underfull \\\\hbox (badness 1533) in paragraph at lines 198--203\", \"Underfull \\\\hbox (badness 4686) in paragraph at lines 206--211\", \"Underfull \\\\hbox (badness 5147) in paragraph at lines 261--265\", \"Underfull \\\\hbox (badness 1320) in paragraph at lines 268--274\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 383--389\", \"Underfull \\\\hbox (badness 1005) in paragraph at lines 383--389\", \"Underfull \\\\hbox (badness 2452) in paragraph at lines 383--389\", \"Underfull \\\\hbox (badness 1769) in paragraph at lines 442--448\", \"Underfull \\\\hbox (badness 1590) in paragraph at lines 442--448\", \"Underfull \\\\hbox (badness 1102) in paragraph at lines 442--448\", \"Underfull \\\\hbox (badness 3375) in paragraph at lines 451--455\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 38--40\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 38--40\", \"Underfull \\\\hbox (badness 2990) in paragraph at lines 38--40\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 13--17\", \"Underfull \\\\hbox (badness 5302) in paragraph at lines 13--17\", \"Underfull \\\\hbox (badness 7558) in paragraph at lines 13--17\", \"Underfull \\\\hbox (badness 2799) in paragraph at lines 19--22\", \"Underfull \\\\hbox (badness 1184) in paragraph at lines 19--22\", \"Underfull \\\\hbox (badness 1259) in paragraph at lines 19--22\", \"Underfull \\\\hbox (badness 2418) in paragraph at lines 1--2\", \"Underfull \\\\hbox (badness 2277) in paragraph at lines 1--2\", \"Underfull \\\\hbox (badness 4779) in paragraph at lines 1--2\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--50\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--50\", \"Underfull \\\\hbox (badness 1142) in paragraph at lines 7--50\", \"Underfull \\\\hbox (badness 1168) in paragraph at lines 7--50\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 50--54\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 3746) in paragraph at lines 4--7\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 25--28\", \"Underfull \\\\hbox (badness 1675) in paragraph at lines 25--28\", \"Underfull \\\\hbox (badness 2359) in paragraph at lines 25--28\", \"Underfull \\\\hbox (badness 3333) in paragraph at lines 30--31\", \"Underfull \\\\hbox (badness 1577) in paragraph at lines 30--31\", \"Underfull \\\\hbox (badness 7308) in paragraph at lines 21--21\", \"Underfull \\\\hbox (badness 6016) in paragraph at lines 1--2\", \"Underfull \\\\hbox (badness 1097) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 1540) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 3668) in paragraph at lines 25--27\", \"Underfull \\\\hbox (badness 1221) in paragraph at lines 29--35\", \"Underfull \\\\hbox (badness 3815) in paragraph at lines 29--35\", \"Underfull \\\\hbox (badness 1571) in paragraph at lines 78--83\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 85--90\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 85--90\", \"Underfull \\\\hbox (badness 1163) in paragraph at lines 85--90\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 85--90\", \"Underfull \\\\hbox (badness 4168) in paragraph at lines 85--90\", \"Underfull \\\\hbox (badness 1953) in paragraph at lines 85--90\", \"Underfull \\\\hbox (badness 2221) in paragraph at lines 85--90\", \"Underfull \\\\hbox (badness 2142) in paragraph at lines 24--28\", \"Underfull \\\\hbox (badness 4353) in paragraph at lines 24--28\", \"Underfull \\\\hbox (badness 1043) in paragraph at lines 24--28\", \"Underfull \\\\hbox (badness 2503) in paragraph at lines 24--28\", \"Underfull \\\\hbox (badness 1210) in paragraph at lines 24--28\", \"Underfull \\\\hbox (badness 1946) in paragraph at lines 30--78\", \"Underfull \\\\hbox (badness 1163) in paragraph at lines 1--2\", \"Underfull \\\\hbox (badness 2310) in paragraph at lines 1--2\", \"Underfull \\\\hbox (badness 2393) in paragraph at lines 8--11\", \"Underfull \\\\hbox (badness 1975) in paragraph at lines 8--11\", \"Underfull \\\\hbox (badness 2689) in paragraph at lines 38--82\", \"Underfull \\\\hbox (badness 2698) in paragraph at lines 22--26\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 5711) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 1490) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 4024) in paragraph at lines 35--36\", \"Underfull \\\\hbox (badness 2903) in paragraph at lines 31--34\", \"Underfull \\\\hbox (badness 2351) in paragraph at lines 31--34\", \"Underfull \\\\hbox (badness 2318) in paragraph at lines 14--15\", \"Underfull \\\\hbox (badness 1596) in paragraph at lines 20--21\", \"Underfull \\\\hbox (badness 3088) in paragraph at lines 20--21\"], \"issues\": [\"2 critical warning(s): Reference `app:cross-model-detail' on page 6 undefined on input; There were undefined references.\", \"pages 23 > limit 8\"], \"summary\": \"FAIL: 2 critical warning(s): Reference `app:cross-model-detail' on page 6 undefined on input; There were undefined references.; pages 23 > limit 8\"}"
    }
  },
  "sourceToolAssistantUUID": "1ed02b9c-f852-4053-a588-c88ee8aab103",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Runtime record

_source line 5834_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch — 页数压缩 + 附录重组] 三项修改，目标：正文（Abstract 到 Conclusion）严格 ≤ 8 页。  **当前问题**：Conclusion 结束在第 9 页右栏，超标约 1 页。  ---  **1. 正文压缩（目标省 ~1 页）**  具体策略（按优先级）：  A) **Cross-model per-class 表格移到附录**（省…",
  "leafUuid": "93cf02a5-b7b3-465b-911a-0746156261c3",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Runtime record

_source line 5835_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent callback function implementation",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Assistant

_source line 5836 · 2026-05-17T15:52:47.105Z_

<details><summary>Logged reasoning block</summary>

```text
It went from 24 pages to 23 pages. I saved 1 page total, but the total is still 23 with appendix. I need to visually check where the main text ends now. Let me render pages 7-9 to see if Conclusion ends on page 8.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93cf02a5-b7b3-465b-911a-0746156261c3",
  "isSidechain": false,
  "requestId": "req_011Cb8QiUhU49xMVbH2LvSNy",
  "type": "assistant",
  "uuid": "df1bbe2f-ad24-4bf6-9ce7-2ec0df217ce7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyEcGLv96m77ueYTFeYnN4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6650,
      "cache_read_input_tokens": 74918,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6650,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 285,
          "cache_read_input_tokens": 74918,
          "cache_creation_input_tokens": 6650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6650
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

_source line 5837 · 2026-05-17T15:52:47.648Z_

Down from 24 to 23 pages total. Let me visually check pages 7-9 to see where Conclusion ends.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df1bbe2f-ad24-4bf6-9ce7-2ec0df217ce7",
  "isSidechain": false,
  "requestId": "req_011Cb8QiUhU49xMVbH2LvSNy",
  "type": "assistant",
  "uuid": "de90857b-c49e-41e2-9022-dfa0c373ee7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyEcGLv96m77ueYTFeYnN4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6650,
      "cache_read_input_tokens": 74918,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6650,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 285,
          "cache_read_input_tokens": 74918,
          "cache_creation_input_tokens": 6650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6650
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

_source line 5838 · 2026-05-17T15:52:49.979Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S4645F9Sjx39YjNep5X1fK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de90857b-c49e-41e2-9022-dfa0c373ee7c",
  "isSidechain": false,
  "requestId": "req_011Cb8QiUhU49xMVbH2LvSNy",
  "type": "assistant",
  "uuid": "1d446726-9abe-42a2-9b66-fedee4b17cc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyEcGLv96m77ueYTFeYnN4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6650,
      "cache_read_input_tokens": 74918,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6650,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 285,
          "cache_read_input_tokens": 74918,
          "cache_creation_input_tokens": 6650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6650
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

_source line 5839 · 2026-05-17T15:52:50.422Z_

<details open><summary>🔧 Tool call — Read · `toolu_011uCRPPBsuB1XoHiGHH5h8m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d446726-9abe-42a2-9b66-fedee4b17cc1",
  "isSidechain": false,
  "requestId": "req_011Cb8QiUhU49xMVbH2LvSNy",
  "type": "assistant",
  "uuid": "3f2759b5-a998-4082-acc1-219de3925d39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyEcGLv96m77ueYTFeYnN4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6650,
      "cache_read_input_tokens": 74918,
      "output_tokens": 285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6650,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 285,
          "cache_read_input_tokens": 74918,
          "cache_creation_input_tokens": 6650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6650
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

_source line 5840 · 2026-05-17T15:52:50.537Z_

<details><summary>↩ Tool result · `toolu_01S4645F9Sjx39YjNep5X1fK`</summary>

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
  "parentUuid": "1d446726-9abe-42a2-9b66-fedee4b17cc1",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "87c59f8e-17ea-457f-b23f-e7592c2db48d",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 474892
    }
  },
  "sourceToolAssistantUUID": "1d446726-9abe-42a2-9b66-fedee4b17cc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Runtime record

_source line 5841_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch — 页数压缩 + 附录重组] 三项修改，目标：正文（Abstract 到 Conclusion）严格 ≤ 8 页。  **当前问题**：Conclusion 结束在第 9 页右栏，超标约 1 页。  ---  **1. 正文压缩（目标省 ~1 页）**  具体策略（按优先级）：  A) **Cross-model per-class 表格移到附录**（省…",
  "leafUuid": "87c59f8e-17ea-457f-b23f-e7592c2db48d",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Runtime record

_source line 5842_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent callback function implementation",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Tool result

_source line 5843 · 2026-05-17T15:52:51.039Z_

<details><summary>↩ Tool result · `toolu_011uCRPPBsuB1XoHiGHH5h8m`</summary>

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
  "parentUuid": "3f2759b5-a998-4082-acc1-219de3925d39",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "d9f19bb8-3d57-4dab-805c-c7b7336368d9",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 513045
    }
  },
  "sourceToolAssistantUUID": "3f2759b5-a998-4082-acc1-219de3925d39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra"
}
```

</details>

---


### Runtime record

_source line 5844_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch — 页数压缩 + 附录重组] 三项修改，目标：正文（Abstract 到 Conclusion）严格 ≤ 8 页。  **当前问题**：Conclusion 结束在第 9 页右栏，超标约 1 页。  ---  **1. 正文压缩（目标省 ~1 页）**  具体策略（按优先级）：  A) **Cross-model per-class 表格移到附录**（省…",
  "leafUuid": "d9f19bb8-3d57-4dab-805c-c7b7336368d9",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Runtime record

_source line 5845_

```json
{
  "type": "ai-title",
  "aiTitle": "Agent callback function implementation",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448"
}
```

---


### Assistant

_source line 5846 · 2026-05-17T15:52:59.354Z_

<details><summary>Logged reasoning block</summary>

```text
Looking at the pages:

Page 8: The page still contains the same content as before - Table 4, baseline comparisons, Downstream Utility, and Discussion starts at the bottom. The Discussion hasn't been compressed on this rendered page - wait, I see it still shows the OLD discussion text. Let me check - the images might be stale from a previous rendering. Let me look more carefully.

Actually wait - the compile just ran and should have regenerated the PDF. But the _pdf_images folder might have stale images. Let me re-render pages 8-9 explicitly.

Actually, the `paper_compile_and_check` tool compiles the PDF but doesn't automatically render images. 

I need to regenerate the image files by calling `pdf_to_images` again to see the updated content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9f19bb8-3d57-4dab-805c-c7b7336368d9",
  "isSidechain": false,
  "requestId": "req_011Cb8Qj1YN2txpEDpwHQebS",
  "type": "assistant",
  "uuid": "aa5c26cc-2e50-4208-a544-24bd63b4f504",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UT71nrTLMHeQD3Ux9vsZ4u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 81568,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 363,
          "cache_read_input_tokens": 81568,
          "cache_creation_input_tokens": 1060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1060
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

_source line 5847 · 2026-05-17T15:52:59.659Z_

The images are stale from a previous render. Let me re-render pages 8-9.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa5c26cc-2e50-4208-a544-24bd63b4f504",
  "isSidechain": false,
  "requestId": "req_011Cb8Qj1YN2txpEDpwHQebS",
  "type": "assistant",
  "uuid": "40ee3535-09ce-46b3-8b10-22df2bbbb471",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UT71nrTLMHeQD3Ux9vsZ4u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 81568,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 363,
          "cache_read_input_tokens": 81568,
          "cache_creation_input_tokens": 1060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1060
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

_source line 5848 · 2026-05-17T15:53:00.513Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_014obe1wvqwyhYGx8Zu7CG5g`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/main.pdf",
  "pages": "8,9",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40ee3535-09ce-46b3-8b10-22df2bbbb471",
  "isSidechain": false,
  "requestId": "req_011Cb8Qj1YN2txpEDpwHQebS",
  "type": "assistant",
  "uuid": "0d6322bd-4537-48b7-b6fe-eead74287849",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/.claude/sessions/paper_agent_f6e70382",
  "sessionId": "29d8b308-43be-4df5-b301-2fd1aaa58448",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "stateful-foraging-zebra",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UT71nrTLMHeQD3Ux9vsZ4u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 81568,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1060,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 363,
          "cache_read_input_tokens": 81568,
          "cache_creation_input_tokens": 1060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1060
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

_source line 5849 · 2026-05-17T15:53:01.211Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_014obe1wvqwyhYGx8Zu7CG5g`&lt;/summary>

```text
Error: result (1,289,096 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-paper-agent-f6e70382/29d8b308-43be-4df5-b301-2fd1aaa58448/tool-results/mcp-agent-ml-research-pdf_to_images-1779033181208.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-paper-agent-f6e70382/29d8b308-43be-4df5-b301-2fd1aaa58448/tool-results/mcp-agent-ml-research-pdf_to_images-1779033181208.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0d6322bd-4537-48b7-b6fe-eead74287849",
  "isSidechain": false,
  "promptId": "dd837da6-1c71-4064-8f74-736a03a12b47",
  "type": "user",
  "uuid": "ed5ff08b-c25e-484b-a610-04cc6efc6d64",
  "toolUseResult": "Error: result (1,289,096 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-paper-agent-f6e70382/29d8b308-43be-4df5-b301-2fd1aaa58448/tool-results/mcp-agent-ml-research-pdf_to_images-1779033181208.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint--claude-sessions-paper-agent-f6e70382/29d8b308-43be-4df5-b301-2fd1aaa58448/tool-results/mcp-agent-ml-research-pdf_to_images-1779033181208.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/_pdf_images/main_p8.png\", \"base64\": \"iVBORw0KGgoAAAANSUhEUgAABNkAAAbaCAIAAAB3QTY3AAAACXBIWXMAABcSAAAXEgFnn9JSAAcXQ0lEQVR4nOzdB3QUVQMF4CAgiI0fC6CAICiKolIUERAVRaVJFRBBFAFpgiBSRXrvndBbgFBDb6EkdAIhgRQIBEJCeq+bLdn/sk+ew2zKJiQTIPc7OTm7b6e8mZ2dfXdn5o2dmYiIiIiIiEhbdvldASIiIiIiIipwmEWJiIiIiIhIa8yiREREREREpDVmUSIiIiIiItIasygRERERERFpjVmUiIiIiIiItMYsSkRERERERFpjFiUiIiIiIiKtMYsSERERERGR1phFiYiIiIiISGvMokRERERERKQ1ZlEiIiIiIiLSGrMoERERERERaY1ZlIiIiIiIiLTGLEpERERERERaYxYlIiIiIiIirTGLEhERERERkdaYRYmIiIiIiEhrzKJERERERESkNWZRIiIiIiIi0hqzKBEREREREWmNWZSIiIiIiIi0xixKREREREREWmMWJSIiIiIiIq0xixIREREREZHWmEWJiIiIiIhIa8yiREREREREpDVmUSIiIiIiItIasygRERERERFpjVmUiIiIiIiItMYsSkRERERERFpjFiUiIiIiIiKtMYsSERERERGR1phFiYiIiIiISGvMokRERERERKQ1ZlEiIiIiIiLSGrMoERERERERaY1ZlIiIiIiIiLTGLEpERERERERaYxYlIiIiIiIirTGLEhERERERkdaYRYmIiIiIiEhrzKJERERERESkNWZRIiIiIiIi0hqzKBEREREREWmNWZSIiIiIiIi0xixKREREREREWmMWJSIiIiIiIq0xixIREREREZHWmEWJiIiIiIhIa8yiREREREREpDVmUSIiIiIiItIasygRERERERFpjVmUiIiIiIiItMYsSkRERERERFpjFiUiIiIiIiKtMYsSERERERGR1phFiYiIiIiISGvMokRERERERKQ1ZlEiIiIiIiLSGrMoERERERERaY1ZlIiIiIiIiLTGLEpERERERERaYxYlIiIiIiIirTGLEhERERERkdaYRYmIiIiIiEhrzKJERERERESkNWZRIiIiIiIi0hqzKBEREREREWmNWZSIiIiIiIi0xixKREREREREWmMWJSIiIiIiIq0xixIREREREZHWmEWJiIiIiIhIa8yiREREREREpDVmUSIiIiIiItIasygRERERERFpjVmUiIiIiIiItMYsSkRERERERFpjFiUiIiIiIiKtMYsSERERERGR1phFiYiIiIiISGvMokRERERERKQ1ZlEiIiIiIiLSGrMoERERERERaY1ZlIiIiIiIiLTGLEpERERERERaYxYlIiIiIiIirTGLEhERERERkdaYRYmIiIiIiEhrzKJERERERESkNWZRIiIiIiIi0hqzKBEREREREWmNWZSIiIiIiIi0xixKREREREREWmMWJSIiIiIiIq0xixIREREREZHWmEWJiIiIiIhIa8yiREREREREpDVmUSIiIiIiItIasygRERERERFpjVmUiIiIiIiItMYsSkRERERERFpjFiUiIiIiIiKtMYsSERERERGR1phFiYiIiIiISGvMokRERERERKQ1ZlEiIiIiIiLSGrMoERERERERaY1ZlIiIiIiIiLTGLEpERERERERaYxYlIiIiIiIirTGLEhERERERkdaYRYmIiIiIiEhrzKJERERERESkNWZRIiIiIiIi0hqzKBEREREREWmNWZSIiIiIiIi0xixKREREREREWmMWJSIiIiIiIq0xixIREREREZHWmEWJiIiIiIhIa8yiREREREREpDVmUSIiIiIiItIasygRERERERFpjVmUiIiIiIiItMYsSkRERERERFpjFiUiIiIiIiKtMYsSERERERGR1phFiYiIiIiISGvMokRERERERKQ1ZlEiIiIiIiLSGrMoERERERERaY1ZlIiIiIiIiLTGLEpERERERERaYxYlIiIiIiIirTGLEhERERERkdaYRYmIiIiIiEhrzKJERERERESkNWZRIiIiIiIi0hqzKBEREREREWmNWZSIiIiIiIi0xixKREREREREWmMWJSIiIiIiIq0xixIREREREZHWmEWJiIiIiIhIa8yiREREREREpDVmUSIiIiIiItIasygRERERERFpjVmUiIiIiIiItMYsSkRERERERFpjFiUiIiIiIiKtMYsSERERERGR1phFiYiI8t+mTZvi4+Oty1NSUhIVXFxcYmNjrQdLS0uzLoyOjt67d2/u1zU7kpOTE+9nMplycfoXLlw4duxYJgMEBQUtWrQo3ZWWY5cvX1YthfVi6nS6HE8/LCwsJCQko1e9vLx27NiBLSHdDUZKdz37+PhgjakK/f39c1ZPIqIHxCxKRESUz2bMmGFnZ+fr66sqj4iIKF68uJ3Chx9+qBrGzc2tadOm33777RtvvDFnzhyj0YhCvV5/4MCB119/ff78+RotQwaQAz/++GNR+Wefffatt9566aWX8L958+YLFy5EhMvxlNetW1epUiVM9vfff89ksC5dumCYiRMn5nhGSkihrVq1wgSRNpXlq1at+vHHH8ViFilSpEaNGljG0qVL4y1Auaurq43TDw8PHzhw4FNPPbV7927rV/Fef/LJJ8OGDdu2bduECRMqVKiwfPly68EcHBwaNmzYrFmzatWq7du3TxQiuC5evBhvgYeHh2r4yZMn29vb21hDIqJcxCxKRFTgGE1p+MvvWtC/kA2efPLJdLPo33///c4773x6DwLGnj17lAOsX78e4w4aNAiP4+LiOnbs+NNPP/Xu3fvnn38eOXLkm2++KaJp/kKiFiFtxYoVogSJDvkZJajhnTt3sjU15eE+hKsss6izs3OLFi28vLxyUHOlyMhIRP0ffvhBLIsqiwq1atXCS23btpUliJSvvvoqCpH3spzFypUr+/Xr9/TTT2N46ywaHBz84osvLlu2TJbs2rWrUKFCJ0+eVA7Wp08fjI6X8PjWrVv16tXr1atXz549sVV06tQJG0a6s546derMmTOzrCERUe5iFiUiKnASdIbYZH1+14Lu0ul0SJgimKmyaHJycuXKlTM5D9Pf37948eLIPzJwLl++XB71QnbduXNn3tU8WxCZsIAbN26UJampqYjZKGzTpo3t00Fac3FxkU8xwSyzaK577rnnMsqizZs3x0vIq8pCV1dXEV/9/Pxsmb6YiHUWnTt3Lspv3LghS/C+Fy5cePDgwbJkw4YNqhXSt29f8SA6OhqpOJNTf+vUqZPuwVgiorzDLEpEVODojaZUQ25es0c5hqjg5OT0yy+/WGfR+fPnI6eFh4dnNO7333+PsTZv3ixLhg8fHhQUhAfbt29HxM2zWmfbE088ocqigBCFwhIlStg4EXd392LFiimvDs2XLPryyy9nlEVbtGhhnUXhmWeeQfnq1attmb54W61j4YABA1COd1aW3L59GyVDhgyRJWXKlEE6DQ4OliVdunQRD/r16zdmzJhM5nvkyJFSpUplElaJ6OGXkJDg6enp4uJy8uRJLy8vg8GgGiA5OdnNzU25l5CMRiN2s3j10qVL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Hmplib9mzZqaNWvu378/Zm+4d+9ey5Yt+/btG600xDUqVKgAYXjxxRdVyLFjxz744IO0adMmT568V69ecXESmP7O3377LY64aEgEzkfDw8NDyEVHjx7dqFEjZy/u2bNnDwIX9SclBgYPFgwXNTAwMDAwMIgJpk6dun79ev/jY0N36NAhmF8MCRo3bgwtgWNbwo8ePZovXz5u1apVK7BfhMyPGDFCXf7xxx9xxEVDhRdeeCGEXNQfPPfcc0HgogYGDx8MF024uHjxYufOnf2Pf/Lkyc8///yTTz6JuyQZxB4bN26cMGFCqFPhE6tWrerTp8/QoUP37t3rKw59+dc26EuSjh07Nnjw4G7dulEb7eepLl26VD3Fh0I4fhyQzGJifvzxx/379+dtlmfJOxL46KOPZs+eHQ+HyVevXv3hhx/26NFjw4YNllsHDhwYOHDge++9980339y7d8/hJc5lbRBa7Nq1K3ny5NHaOtigQYOXXnopmF8MCZo0aeKVi4IjR46QBe7OmDEjUJ/766+/ChQooM9VGi4afBguahBPcP36dayO9evXb9q0CRNCX05/4cKF7du3o0KxFfft22fZzU6HK3d//vlnf458DxQMF024qF69+qOPPupn5GvXro0aNQo9+8Ybb8Rpqgxigz///DN79uxYe6FOiHe0a9euWrVqaEl0XNGiRefOnes1muwfs0AN+X/77bcYJefPn+f3999/nzVr1uPHj6tnDx06pD/VsGHDuM+WdwQks/DS3Llznzx58vbt202bNu3UqZN68Ndffw0PDxeCOm7cuDJlyty4cSMI+fIT77zzTs6cOYsUKZI4cWJy1K9fP3Xrq6++ypYt29NPP506dWpuVaxY0dd6Reeyfghw+PBhunx+XL16dcGCBeRXWQawi2XLliEru0FApVq8ePH48eOXL19ud5SCGUEgcaZMmYJVASfZqgFNLtFUiPNYgIDqt3TpUhLDC8+dOyfldeDAAVmUSEp4z6lTp1R8GOM0D7B1VCAf6tatG/EpesunT58+zZv1L1Lo33zzzZw5c/gKWZBAX1/8999/EcXdu3ctyd65c+fkyZNnzpypp02AlTZ16tS1a9devHgxLtzhOHBRIHLImDGjZQjpl19+IcEU7uXLl/VwySCRsSkxLr/88svdu3eru//73//Kly/PC1u1aoVY0Azu+7kohU5d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Fy9O4OzZs+2YkydPbt68edhLK8p5AhKrQIECZimdu+66y2iwG264YdWqVcl+RUZjo8TuueeeKI/atm0bQpFDHn30UQn5+eef5SStW7c20RgrJJBhv3379qg4jB5ZkCnuv++migIny+KTvHjxYoljhq+wPrp58+a1tagTekfAq0W7devGZo0aNcyBU6dOFS0q/71aNNkzqCiKkoqsXLlSZCQi8++//2aMXbhwoTwvE426a9cuJ/R+nwhOWcSOyAjXFStW7LM4evRobNKsWlQJBuM+UVq0cePG3Kdz5Mjh0qLvv/++V4tOnDiRwKpVqyZbcs8bMGXuvffeGFxoz549V1xxBSaUCWnTpo1rbpBKoZwRpWHP0KhRIySi/XS/bNmytsH65Zdfcvj9998f9vBcuXJVrFjRbB46dAhb86233gob+corrxRh2axZM9cuRsOrr7565MiR7OWPvUueWdhaFJ5++mkCMUBd5ylfvnx8fHzYqyvK+cDvv/9udJHRTvfdd5+EIFOT3QioXr26uaLRXYHUqVNHDjHjP52UsYKQNGnSGC996Z5QokQJc6z4MsRZq/IyRsl0opmYPXbsmIQ89thjEhJWi4pvjq1FQR5p2VpU8pglSxbj4gFmHPv666+9WjR5M6goipKKnDhxQhSmd7kWbML5IcwukabywgJ3HP5v3Lgx1ikOoVr0guf777+3X7nctm3bRx995IRe/+PmivzzftT7888/79Gjx6hRo6Jc1z5RWnTQoEGSgCi16OjRo+OCntMvXbp0zpw59J+vvvoKs2PatGnGqUDYsmXL4MGDydQnn3zich/99ttvyeb+/fvF/80/Pqf95ptvuBz/582b16dPn5kzZ8q3/nbv3j1u3DhCvIW2du3ad955580331y2bJkJFN8zjBUuYU/chY3shN7Rklc0ue7AgQPFEv3jjz9IJ5skw5aaLjp06HDdddfZIQcOHHDF6dq1K+nh6mHPgG6MC/lUS8H+9NNP2HmUtuyl5GUOJ+xMphOy9uJCfoaySVHnzJmTEgsbGS2KhUd8bFDX6kdTpkxBplJlUWpR8fH2it4BAwYULlxYPXWV8xb77U2jDOWJj+Bq6udO3bp1zcmjfEb2119/mUMmTZpkwgsWLCiBxvnCSLWbb77ZRKtatarrcsYtuX79+ibawoULuTWYIetctCg3FwlhbGndurXr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8MEHX3755e7du8OmYfv27WRw0qRJHG6kIGdeehZxXSZrJuTYsWOuk/z444+UwMcff7xz507XroSEhLlz5w4fPpxfl6r3SUCUBQgHDhyYPXs256cQOINrL8nG1HNCr/N99NFHdoSDBw9SZRTyjh07vFoU6Thz5sxTp06ZEI4lPn+wGrkiRU31uS73zz//SGY//fRT194ka1HSzwlJTKTWFan5cUXaz6FDh/hPqxgxYgSty3s4Bfj555+zl/O4dkUqvUjZXL9+vXhZDx06lENMY/AWphNqz5jpY8eOjY+P37hxozdhPn0hSqgpWgXtf+XKlZG0qE/pkebjx4+jHxASI0eOXL16tdn7119/1ahRgxO2aNGCnP7888/Of7UovWbGjBk0Epp3YpPtM57Qiz/55JOJEydS1FxOAqdMmXLZZZdxaemeZjk00vDNN9/Yh9MZp02bJv8pE67yyy+/mL3kgpDvvvvOdVGfVq34QPnPnz+f8uSXAuTPkiVLxJWaIe67EMhU+WN2OaGKkEA5HBCusUmzalFFURRFSQUwAvLnz+9aSahjx45Zs2Yl0J6H/Pbbb++66y6ziSh96KGHevToMWTIkFtuuSVHjhyfffZZ4OWwwrGPZaWT5557TgI5w7XXXit2fKdOnYoUKZIrVy42mzdvLhGwPtu2bUsIu14LgV3YvXv3a665RszQ66+/XhaJkUfs6KUbbrhh2LBhmEEvvPAC1mrXrl1tPYCR3apVqzp16nz11VeYs3fffbcUgkhBDOLLL7+cTbLshIxvbOsrrrhCrmVOgqnNGUgG0dq3b58uXbpXX33V7EXJNGzY8O23337jjTfy5ct33XXX2bavfwKiYeDAgeXLl8dERmzXr1+fEkMPyy70VaNGjdKnT//YY4+999578lihZ8+eshdpceONN06YMGHOnDnUoPhjixalnNu1a5cnTx5CxKwnzcTJmDHjlVdeiSChVKWmqG576V2UVbFixXr37o0pyYWIP3XqVLM3CVp03759tD1qDWP0gQceSJs2Lem89957H330UYkQqfkhGjt06CCVtXjxYgqWBGfIkCFNmjRISvsStEPORvnQQiirevXqySLGPqXnk02aLqUqko/2SQv0FqawZcuWKlWqvPjii2hFmkfOnDmpPjP/E9gXomHZsmV0jXfeeQdzv0uXLrfeeqtLi0YqPex+Opqk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oKxw4cJdunQZMWLEqFGjXn/99fr16/Ob2klTFEVRFEVRlAsD1aKKkhTGjx9fs2bNggULokjr1q3brVu3lFgQX1EURVEURVEuVlSLKoqiKIqiKIqiKLFGtaiiKIqiKIqiKIoSa1SLKoqiKIqiKIqiKLFGtaiiKIqiKIqiKIoSa1SLKoqiKIqSbCxfvnzs2LGJOuTUqVNff/31pk2bzuW6//7776JFi5YtW3YuJ7lAWbNmzezZs6OP/8MPP1DgKZeeSxCaH21v0KBB48aN++OPP1I7Of+frVu3Tpo06fXXX//ggw9ik7DNmzePHj36vffe+/nnn2NwOeVCR7WooiiKoijJRpEiReLi4hYvXhxl/Jdeeil79uwc8tlnnyX5or17986TJw8neeONN5J8kguRESNGFCtWjIw/8cQTgZFPnz7dq1evAgUKEP+xxx6LQfIuESjYBx98cNq0aZMnT86QIUO2bNn27duX2oly/vnnn86dO7dv337Dhg2ff/55lixZSBjSNEUv+s4777z88stLly6VZjlz5swUvZxyEaBaVFEURVGUZGPw4MGPPPLI8ePHoz/koYceikaLYlv77O3YseMlqEVh5MiRUWpR4f3337+Itah/I0khXnvttWuuuUb+x8fH169fPyEhIfbJcEGPqFWrltmcPXs2iVy3bl3KXXHevHk0rd9//53/P/30E1f/5ZdfUu5yysWBalElKs6cOfPtt98yspiQTz/9lEEnFZN0gZIE77WLm5MnTw4fPnzz5s2pnZD/Y9euXcOGDfvrr79SOyGJxttDLz4S64WYuqdVEkXr1q0DtSjitm3btj4R3nnnnUtTi3799deJ0qKMFRerFkVo9e/fP/bXLVCgwN133x376/qwZ8+eDBkyDBw4MJYXfeSRR7hoLK+oXASoFlUCSEhI6NixY86cObl1ffjhhxL466+/spk5c+bTp0+nbvIuOBLrvXbRQ6OiQOxnt6kIxhyJ6dOnT2onJBGE7aEXGYnyQkz10ypJIBot+tBDD91+++0+EVSLRhn/YtWihw8fLlGixGuvvRbj6+7du5fyPN+06OTJk0nVBx98EMuLXn/99apFU52jR4+uXbt2wYIFixYtWrdunW2o//HHHytWrJg3b97333/Prr///tvsOnLkyOrVqzlq/vz5P/74YywfyqsWVaKCm5Zt6f7777/NmzdP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KjyxbNmy+vXrr1u3rnbt2tzy0ksvJbyEFr44fPhw06ZNM2fOTBcg5555vvrqq7p166ZPn548P/30U3IU49ChQy1bttywYYNcnj17tnv37hkyZBBxuvzyywcOHJiU5585c6ZXr1758+fnaU888UQiimxxscFyUQsLCwsLiwsAQ4cObdSokeNTW//8849++fjjj6cFLiqQwuhcdOHChQ8//PD3338f/CE//vhjEC7qaIeEw7PxzXj33XeDcNE4Sl66dOnChQs/9thjT2iALd98882+9x49ejRbtmwffvghf//11190x4wZM2ItgBvJ3f4XK8qUKWPgouHIGni+fPmSiYv+/vvvVatW3bFjh0pBXDt37rxr165jx45NnToVUYlpCiYaZCxYLmrhCctFLZw4efLkqFGjtm3bltoFSUasX79+/vz56jK+sLE0joCVmj59enKEkLkRJBLpEkHKBBwiAJMmTfLNFi3yEAfom2++GTJkyMSJE/fu3RvtFSk8cGxgoRvPPPOMftmyZcu0w0VffvllBxeNA7/99lsQLupoh7SAKVOmBOGisZYcYuD5TLjoG2+84Xv7e++9ZyY/cWDcuHEMyQQ+8NLBww8/7Nsdd955Z3Jw0dOnT5crVw7CqVJ27tzZr18/PU/fvn15dZ8+fZL4ri+++MJyUYtosFzUwon3338flVG9evXULkiyYPTo0UWKFKGCuvmPNWzsgkCQSv3888/kyZIly5kzZ5KvJEEikS4RpEzA4ZIlSypVqsRb8E19M3tGHiIPDRo0mDlzJsTv8ssvz5Yt28GDB933pvDAsYGFbowcOZKm0FMuTS7qboe0gCBcNI6Sf/fdd26NvWrVKp6zadMm39uff/75xKpiypMpU6aUmdO8+JCKXLRbt2533XWXnrJt2zbH+vacOXN49fDhw5P4LstFUxLHjh3bsGHD0qVLly9f/v3337vVxdGjR7+NQBcqEhnL3IULsWbNGjy3FCtwmtPdFqmOX3/9tV69eh999FGsN14oITo4Rg4uGkfYWDjN1zdapfRi//vvv7DE119/PQXK4xuJFARpvM2jQS92wIDDJAIDE5CLekYeIhLFihWTvydPnlynTp1Tp06FXe0f38CJD8kUWJha2Lx589fncOTIkT/++ONrDXJIyZ9//imXu3fvVjfiIqgNgWhp2dYl2WSBWueidM2YMWM+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4425c+eWdJ2h4bN26tQpS5Ysn3zySWJLcvbs2R49evDq0aNHv/3229dff/2HH35ovoXCPPLII0899RRuPZ5uiRIl2rRp8++//+p5pkyZUrRo0d69e0NFbr/99nbt2jkesnr1alpg4MCBEyZMuP/++ytVqpRMNNsiIViyZAl9hFhed911QfLT72XLliV/gQIFElIAhsOTTz552WWX8UwYaXwPgRtzO+MoGn9LMcQ67mCPoSgYN26cI/OJEyf69+9fqFChl19+ee3atfpPq1atuuGGG9S9FSpU2LJlS8JrFxN27tzZoEGDjBkzUh46KHULY5EqsFzUIiWArpE//vrrL3RurLfHd1diQRn2798fx42HDx/GMMT0WNTxP//8E8e7EgXM5BdffLFx48ZYb/zll19wT5OjSJcCdu/ePXLkyLjdrAsRJ0+eHDVq1LZt2/TE06dPf/755+vXr4/1abEu2qQudu3aJe7g5MmTHT999dVXV1xxBaNJLvE127dvnzVrVjInnIt27tw5U6ZMyh9l4OPuT506NVp+OGflypWfeOIJlQKHpGz/+c9/VAqFpKjjx4+XS7jr1Vdf3bZtW5UB3YLrqXxoFE7VqlUhLeRMXM0sEoyffvopOBcFP/74YwK5qCBv3rxJ4aJIb9OmTV9//fUEFik+xDruGD45c+asXbv2Expuv/329OnTHzx4UM+5ZMkSWqlixYrbt293PGTDhg158uSh+hMnToQJX3XVVTRmsWLFjh8/nvAKxoprr73WctFLFpaLWiQvDh061LJlSzSgXF6IXHTTpk316tVDfQ8dOrRu3boTJkwIeCPqvnr16t26dXv55ZcxGw7OaXjs1q1bn3322VRZJTh16lTHjh1z5MiBVXj//feD3/j1119XqVKFu/7v//4v+Yp3ceOZZ56hAfv27ZvaBUk5IGNUmWEil7AvXK4sWbKQ+N///jf4c2JdtEkjEC76v//9z/1T8+bNcf31lDp16iSci6JqeCaCpyfSkrlz5z59+rTnLShzbhkzZoyeePfdd+MWy9///PPPdRHoGXB8uWvdunVyee+992bIkEGPtJwzZw4ZXnzxxaRXyiKZ8Pfff8c0xM6ePZtwLnrjjTcmhYumEcQ67k6cOPHAAw+4J7Wffvrpe+65R09BmVx++eVly5b1DGO+7777vvvuO3W5a9cuoaNjx46Nuy6J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Pvts69atKVYShOSLL77YuHFjoh6Y3KBxZs+ebc7z7bff0owJfOmxY8cmT578559/mrMZumbbtm1jx44dPnz4pk2bElWqlOm7NWvWfPnll8n6CguL4LBc1CIxqFWrVhzeSXx3WVhYWFzQGDBgQJkyZeQjrjlz5uzWrZuvO/vvv//279//qquuuvPOOzt16tShQ4fbbrstb968/fr1+/vvvz1v+e677ypWrJg+ffqSJUs+/fTTDRs2vOGGG66//vpHHnkkR44cP/74oyM/fnmTJk2uvPLKBx988JVXXmnevHnBggVLly49ffp0PRscslWrVitWrIi11u+99979998vtb7ssstuuumma6+9NmvWrEWKFKFs77//fgpT0+uuu46SxFGR4KBns2fPzlvUR7aTtSQ0YMeOHelcnkZ7JvFpKQCaBeGktAiGZ4YzZ8706tUrf/785HniiScS8tKdO3c2aNAgY8aMPPPnn382Z47WNW+//XaPHj2+/vprpJcM8+bNS2KpUqbvPvjgg6JFi/KKF154IZleYWERKywXtYgfKHT1d9myZdWMe3DEd1dSgD/322+/nTx5Mqa7Tp8+vW/fvrNnz/rmxJysXr1aXf70008xF9HCwuISwK5du4SVDR061DfzL7/8ctddd2XLlm3q1Kl6Oj5rhgwZypUrd/DgQT39n3/+ee2114TvrV+/3nELbJP3rl27Vk//8ssvYYaQVT3/iRMn2rVrR+amTZvyTJWOMmzUqNGyZctiqnI4okuzZMnCA+G6qqg49I8//jicOU+ePI4KJitoeWpx/PhxR7pe0zjguJ2q+XLRaCWJD3C2WPlMEquclAfOmTPHwEUF7777bgK5qABpD8JFPbuGwcK9e/bs4e+NGzdWr179hx9+CCeiGePoO184SiWNabmoRdqB5aIW8eDQoUMtW7bcsGGDSkn7XBQW2rNnTxQ9irhjx478sX//ft+7/vjjjyZNmrRv3567+OOll17ClzLk79KlS/369dXlJ598wrsCRt9ZWFhcUhAuOnPmTHM2dFf58uXJ6VifFLz99tv8dO+99+qJ/fr1I/H222+HTLpv+eKLL9KlS/fVV1+pFLxqiO4VV1zh6ZrXrVuXp/Xq1UtPhP0WKlQIRm0uvBuyxkWxHenz5s2jAJ4/pSTGjRu3dOnSpDzhmWee0S+xlb5cNLHATsXEZyBa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
```

---
