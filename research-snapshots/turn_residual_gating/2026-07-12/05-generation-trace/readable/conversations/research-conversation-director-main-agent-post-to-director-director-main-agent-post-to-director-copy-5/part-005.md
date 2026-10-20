# Research conversation: [系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director  — Part 5 of 6

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../research-conversation-director-main-agent-post-to-director-director-main-agent-post-to-director-copy-5.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/3e/3e38c6ab3d9a8237302f.json)

## Round 23

### Assistant

_source line 996 · 2026-05-25T09:00:24.512Z_

Conclusion still spills 1-2 lines onto page 9. Let me tighten it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85f02903-b3d3-4a3a-8a23-43a7c6264054",
  "isSidechain": false,
  "requestId": "req_011CbP1jgM7EmnoiwFu5eB3Z",
  "type": "assistant",
  "uuid": "bce672de-0aaa-4f23-b3d9-6cb9706dedeb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nmti6XN62TkNkzZ5wXsHhG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 108838,
      "output_tokens": 264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 264,
          "cache_read_input_tokens": 108838,
          "cache_creation_input_tokens": 622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 622
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

_source line 997 · 2026-05-25T09:00:24.941Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BsXBkZjCLDL4J4bHqhbfgN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bce672de-0aaa-4f23-b3d9-6cb9706dedeb",
  "isSidechain": false,
  "requestId": "req_011CbP1jgM7EmnoiwFu5eB3Z",
  "type": "assistant",
  "uuid": "8c34ff23-62b5-4c82-b082-39470408897e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nmti6XN62TkNkzZ5wXsHhG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 108838,
      "output_tokens": 264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 622,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 264,
          "cache_read_input_tokens": 108838,
          "cache_creation_input_tokens": 622,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 622
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

_source line 998 · 2026-05-25T09:00:24.948Z_

<details><summary>↩ Tool result · `toolu_01BsXBkZjCLDL4J4bHqhbfgN`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\,=\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as the primary contributing factor consistent with all evidence, though KV cache drift remains an untested alternative; $\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause. Scheduled sampling compresses the gap to ${\sim}$1.3$\times$ on Qwen and ${\sim}$2.9$\times$ on Llama---the first transfer of time-scheduled sampling to auxiliary attention objectives in multi-turn transformers, generalizing across architectures.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c34ff23-62b5-4c82-b082-39470408897e",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "c9060142-d7ac-4d8f-881d-581431a06d8d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\n\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as the primary contributing factor consistent with all evidence, though KV cache drift remains an untested alternative; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause. Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama---the first transfer of time-scheduled sampling to auxiliary attention objectives in multi-turn transformers, generalizing across architectures.\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  },
  "sourceToolAssistantUUID": "8c34ff23-62b5-4c82-b082-39470408897e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Assistant

_source line 999 · 2026-05-25T09:00:29.038Z_

Already has `\looseness=-1`. Let me try tightening the text slightly to save 1-2 lines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9060142-d7ac-4d8f-881d-581431a06d8d",
  "isSidechain": false,
  "requestId": "req_011CbP1kDLvZcNVdvkFzv9Nh",
  "type": "assistant",
  "uuid": "de8e1781-3702-4f9e-8bc1-259d3dbe5bcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LR4H9ZrKcEKuqHhhJwCh43",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 468,
      "cache_read_input_tokens": 109460,
      "output_tokens": 503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 503,
          "cache_read_input_tokens": 109460,
          "cache_creation_input_tokens": 468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 468
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

_source line 1000 · 2026-05-25T09:00:33.630Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01WJkq7qQzp6xwVSMboCMKGh`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
  "old_string": "\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as the primary contributing factor consistent with all evidence, though KV cache drift remains an untested alternative; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause. Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama---the first transfer of time-scheduled sampling to auxiliary attention objectives in multi-turn transformers, generalizing across architectures.",
  "new_string": "\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama)---the first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, generalizing across architectures and seeds."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de8e1781-3702-4f9e-8bc1-259d3dbe5bcc",
  "isSidechain": false,
  "requestId": "req_011CbP1kDLvZcNVdvkFzv9Nh",
  "type": "assistant",
  "uuid": "1e9b27b2-3ddd-4e99-a0f3-c48c029e9ec1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LR4H9ZrKcEKuqHhhJwCh43",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 468,
      "cache_read_input_tokens": 109460,
      "output_tokens": 503,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 468,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 503,
          "cache_read_input_tokens": 109460,
          "cache_creation_input_tokens": 468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 468
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

_source line 1001 · 2026-05-25T09:00:33.652Z_

<details><summary>↩ Tool result · `toolu_01WJkq7qQzp6xwVSMboCMKGh`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e9b27b2-3ddd-4e99-a0f3-c48c029e9ec1",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "ecd159a3-19cd-4512-a523-4ab63878e7d7",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
    "oldString": "\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as the primary contributing factor consistent with all evidence, though KV cache drift remains an untested alternative; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause. Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama---the first transfer of time-scheduled sampling to auxiliary attention objectives in multi-turn transformers, generalizing across architectures.",
    "newString": "\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama)---the first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, generalizing across architectures and seeds.",
    "originalFile": "\\section{Conclusion}\\label{sec:conclusion}\n\n\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as the primary contributing factor consistent with all evidence, though KV cache drift remains an untested alternative; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause. Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama---the first transfer of time-scheduled sampling to auxiliary attention objectives in multi-turn transformers, generalizing across architectures.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 3,
        "lines": [
          " \\section{Conclusion}\\label{sec:conclusion}",
          " ",
          "-\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as the primary contributing factor consistent with all evidence, though KV cache drift remains an untested alternative; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause. Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ on Qwen and ${\\sim}$2.9$\\times$ on Llama---the first transfer of time-scheduled sampling to auxiliary attention objectives in multi-turn transformers, generalizing across architectures.",
          "+\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama)---the first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, generalizing across architectures and seeds."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "1e9b27b2-3ddd-4e99-a0f3-c48c029e9ec1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1002 · 2026-05-25T09:00:33.741Z_

```json
{
  "parentUuid": "ecd159a3-19cd-4512-a523-4ab63878e7d7",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f375fa16-3dc7-4ad7-863d-7afe7c803441",
  "timestamp": "2026-05-25T09:00:33.741Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---


### Tool call

_source line 1003 · 2026-05-25T09:00:37.288Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_01QG1qHd1c9ZHN1stSESYxe5`</summary>

```json
{
  "project": "turn_residual_gating",
  "max_pages": 8,
  "clean": true,
  "preview": false
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f375fa16-3dc7-4ad7-863d-7afe7c803441",
  "isSidechain": false,
  "requestId": "req_011CbP1krXZn23rVaQtKXgWB",
  "type": "assistant",
  "uuid": "cb2fa5d4-8186-4482-a858-6c2ee75891c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018qkp7GSf5yn17BkKSHwzAf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 109928,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 662,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 109928,
          "cache_creation_input_tokens": 662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 662
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

_source line 1004 · 2026-05-25T09:00:46.550Z_

<details><summary>↩ Tool result · `toolu_01QG1qHd1c9ZHN1stSESYxe5`</summary>

```text
{"result":"{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"on input line 759.\\n(pdftex.def)             Requested size: 341.43307pt x 345.55183pt.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `\\\\beta' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n<../figures/paper/fig_steering_perturn_4panel.pdf, id=1582, 241.8385pt x 399.49\\n25pt>\\nFile: ../figures/paper/fig_steering_perturn_4panel.pdf Graphic file (type pdf)\\n&lt;use ../figures/paper/fig_steering_perturn_4panel.pdf>\\nPackage pdftex.def Info: ../figures/paper/fig_steering_perturn_4panel.pdf  used\\n on input line 780.\\n(pdftex.def)             Requested size: 219.08614pt x 361.91727pt.\\n\\nUnderfull \\\\hbox (badness 1688) in paragraph at lines 781--781\\n[]\\\\T1/ptm/m/n/10 (+20) Figure 27: |Per-turn GAR un-der four $\\\\OML/cmm/m/it/10 ^\\n^L$\\\\T1/ptm/m/n/10 (+20) -steering\\n []\\n\\n[31] [32 <../figures/paper/fig_training_curves_6panel.pdf>]\\nUnderfull \\\\hbox (badness 1092) in paragraph at lines 840--842\\n[]\\\\T1/ptm/b/n/10.95 (+20) Code: \\\\T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment\\n scripts, data-\\n []\\n\\n) [33 <../figures/paper/fig_steering_perturn_4panel.pdf>] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 832B04ACB55D37C1F8BC0949A90C07C7;10309.\\n ) \\nHere is how much of TeX's memory you used:\\n 17366 strings out of 469438\\n 282183 string characters out of 5468411\\n 750243 words of memory out of 5000000\\n 44892 multiletter control sequences out of 15000+600000\\n 712034 words of font info for 468 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,12n,93p,1585b,690s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/s\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/f\\nonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\nic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/h\\nelvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (33 pages, 1043184 bytes).\\nPDF statistics:\\n 1849 PDF objects out of 2073 (max. 8388607)\\n 1468 compressed objects within 15 object streams\\n 291 named destinations out of 1000 (max. 500000)\\n 77912 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 33, \"warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\"]}, \"pages\": 33, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 2--2\", \"Underfull \\\\hbox (badness 1789) in paragraph at lines 2--3\", \"Underfull \\\\hbox (badness 3333) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 7925) in paragraph at lines 29--30\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1117) in paragraph at lines 32--33\", \"Underfull \\\\hbox (badness 1655) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1205) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1360) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1097) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 2189) in paragraph at lines 3--1\", \"Underfull \\\\hbox (badness 2913) in paragraph at lines 99--103\", \"Underfull \\\\hbox (badness 5548) in paragraph at lines 72--73\", \"Underfull \\\\hbox (badness 1616) in paragraph at lines 141--142\", \"Underfull \\\\hbox (badness 1342) in paragraph at lines 169--170\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 285--285\", \"Underfull \\\\hbox (badness 3815) in paragraph at lines 362--363\", \"Underfull \\\\hbox (badness 2359) in paragraph at lines 370--371\", \"Underfull \\\\hbox (badness 2005) in paragraph at lines 449--450\", \"Underfull \\\\hbox (badness 1831) in paragraph at lines 453--454\", \"Overfull \\\\hbox (6.85715pt too wide) in paragraph at lines 470--481\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 487--488\", \"Underfull \\\\hbox (badness 3189) in paragraph at lines 489--490\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 6944) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 1087) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 4927) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 2326) in paragraph at lines 631--632\", \"Underfull \\\\hbox (badness 2401) in paragraph at lines 645--646\", \"Underfull \\\\vbox (badness 2343) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 673--674\", \"Underfull \\\\hbox (badness 4886) in paragraph at lines 685--686\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 6559) in paragraph at lines 702--703\", \"Underfull \\\\hbox (badness 1688) in paragraph at lines 781--781\", \"Underfull \\\\hbox (badness 1092) in paragraph at lines 840--842\"], \"issues\": [\"pages 33 > limit 8\"], \"summary\": \"FAIL: pages 33 > limit 8\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb2fa5d4-8186-4482-a858-6c2ee75891c9",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "d0b85bdc-3502-4ed2-9e3a-635347a1c062",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"passed\\\": false, \\\"compiled\\\": {\\\"success\\\": true, \\\"pdf_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf\\\", \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"on input line 759.\\\\n(pdftex.def)             Requested size: 341.43307pt x 345.55183pt.\\\\n\\\\n\\\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\\\n(hyperref)                removing `math shift' on input line 764.\\\\n\\\\n\\\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\\\n(hyperref)                removing `\\\\\\\\beta' on input line 764.\\\\n\\\\n\\\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\\\n(hyperref)                removing `math shift' on input line 764.\\\\n\\\\n<../figures/paper/fig_steering_perturn_4panel.pdf, id=1582, 241.8385pt x 399.49\\\\n25pt>\\\\nFile: ../figures/paper/fig_steering_perturn_4panel.pdf Graphic file (type pdf)\\\\n&lt;use ../figures/paper/fig_steering_perturn_4panel.pdf>\\\\nPackage pdftex.def Info: ../figures/paper/fig_steering_perturn_4panel.pdf  used\\\\n on input line 780.\\\\n(pdftex.def)             Requested size: 219.08614pt x 361.91727pt.\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1688) in paragraph at lines 781--781\\\\n[]\\\\\\\\T1/ptm/m/n/10 (+20) Figure 27: |Per-turn GAR un-der four $\\\\\\\\OML/cmm/m/it/10 ^\\\\n^L$\\\\\\\\T1/ptm/m/n/10 (+20) -steering\\\\n []\\\\n\\\\n[31] [32 <../figures/paper/fig_training_curves_6panel.pdf>]\\\\nUnderfull \\\\\\\\hbox (badness 1092) in paragraph at lines 840--842\\\\n[]\\\\\\\\T1/ptm/b/n/10.95 (+20) Code: \\\\\\\\T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment\\\\n scripts, data-\\\\n []\\\\n\\\\n) [33 <../figures/paper/fig_steering_perturn_4panel.pdf>] (./main.aux)\\\\n ***********\\\\nLaTeX2e <2025-11-01>\\\\nL3 programming layer <2026-01-19>\\\\n ***********\\\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\\\n(rerunfilecheck)             Checksum: 832B04ACB55D37C1F8BC0949A90C07C7;10309.\\\\n ) \\\\nHere is how much of TeX's memory you used:\\\\n 17366 strings out of 469438\\\\n 282183 string characters out of 5468411\\\\n 750243 words of memory out of 5000000\\\\n 44892 multiletter control sequences out of 15000+600000\\\\n 712034 words of font info for 468 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,12n,93p,1585b,690s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/s\\\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/t\\\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive\\\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf\\\\n-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/f\\\\nonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\\\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\\\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\\\\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\\\\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p\\\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\\\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\\\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\\\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\\\\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\\\nnts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\\\ne1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\\\nic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/h\\\\nelvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.\\\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share\\\\n/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\\\nOutput written on main.pdf (33 pages, 1043184 bytes).\\\\nPDF statistics:\\\\n 1849 PDF objects out of 2073 (max. 8388607)\\\\n 1468 compressed objects within 15 object streams\\\\n 291 named destinations out of 1000 (max. 500000)\\\\n 77912 words of extra memory for PDF output out of 89155 (max. 10000000)\\\\n\\\", \\\"error\\\": \\\"\\\", \\\"pages\\\": 33, \\\"warnings\\\": [\\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\"]}, \\\"pages\\\": 33, \\\"page_status\\\": \\\"over_limit\\\", \\\"max_pages\\\": 8, \\\"min_pages\\\": null, \\\"critical_warnings\\\": [], \\\"minor_warnings\\\": [\\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 2--2\\\", \\\"Underfull \\\\\\\\hbox (badness 1789) in paragraph at lines 2--3\\\", \\\"Underfull \\\\\\\\hbox (badness 3333) in paragraph at lines 7--8\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 7--8\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 7--8\\\", \\\"Underfull \\\\\\\\hbox (badness 7925) in paragraph at lines 29--30\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1117) in paragraph at lines 32--33\\\", \\\"Underfull \\\\\\\\hbox (badness 1655) in paragraph at lines 3--4\\\", \\\"Underfull \\\\\\\\hbox (badness 1205) in paragraph at lines 3--4\\\", \\\"Underfull \\\\\\\\hbox (badness 1360) in paragraph at lines 5--6\\\", \\\"Underfull \\\\\\\\hbox (badness 1097) in paragraph at lines 5--6\\\", \\\"Underfull \\\\\\\\hbox (badness 2189) in paragraph at lines 3--1\\\", \\\"Underfull \\\\\\\\hbox (badness 2913) in paragraph at lines 99--103\\\", \\\"Underfull \\\\\\\\hbox (badness 5548) in paragraph at lines 72--73\\\", \\\"Underfull \\\\\\\\hbox (badness 1616) in paragraph at lines 141--142\\\", \\\"Underfull \\\\\\\\hbox (badness 1342) in paragraph at lines 169--170\\\", \\\"Underfull \\\\\\\\hbox (badness 1400) in paragraph at lines 285--285\\\", \\\"Underfull \\\\\\\\hbox (badness 3815) in paragraph at lines 362--363\\\", \\\"Underfull \\\\\\\\hbox (badness 2359) in paragraph at lines 370--371\\\", \\\"Underfull \\\\\\\\hbox (badness 2005) in paragraph at lines 449--450\\\", \\\"Underfull \\\\\\\\hbox (badness 1831) in paragraph at lines 453--454\\\", \\\"Overfull \\\\\\\\hbox (6.85715pt too wide) in paragraph at lines 470--481\\\", \\\"Underfull \\\\\\\\hbox (badness 1845) in paragraph at lines 487--488\\\", \\\"Underfull \\\\\\\\hbox (badness 3189) in paragraph at lines 489--490\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\hbox (badness 6944) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\hbox (badness 1087) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\hbox (badness 4927) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\hbox (badness 2326) in paragraph at lines 631--632\\\", \\\"Underfull \\\\\\\\hbox (badness 2401) in paragraph at lines 645--646\\\", \\\"Underfull \\\\\\\\vbox (badness 2343) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 2173) in paragraph at lines 673--674\\\", \\\"Underfull \\\\\\\\hbox (badness 4886) in paragraph at lines 685--686\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 6559) in paragraph at lines 702--703\\\", \\\"Underfull \\\\\\\\hbox (badness 1688) in paragraph at lines 781--781\\\", \\\"Underfull \\\\\\\\hbox (badness 1092) in paragraph at lines 840--842\\\"], \\\"issues\\\": [\\\"pages 33 > limit 8\\\"], \\\"summary\\\": \\\"FAIL: pages 33 > limit 8\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"on input line 759.\\n(pdftex.def)             Requested size: 341.43307pt x 345.55183pt.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `\\\\beta' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n<../figures/paper/fig_steering_perturn_4panel.pdf, id=1582, 241.8385pt x 399.49\\n25pt>\\nFile: ../figures/paper/fig_steering_perturn_4panel.pdf Graphic file (type pdf)\\n&lt;use ../figures/paper/fig_steering_perturn_4panel.pdf>\\nPackage pdftex.def Info: ../figures/paper/fig_steering_perturn_4panel.pdf  used\\n on input line 780.\\n(pdftex.def)             Requested size: 219.08614pt x 361.91727pt.\\n\\nUnderfull \\\\hbox (badness 1688) in paragraph at lines 781--781\\n[]\\\\T1/ptm/m/n/10 (+20) Figure 27: |Per-turn GAR un-der four $\\\\OML/cmm/m/it/10 ^\\n^L$\\\\T1/ptm/m/n/10 (+20) -steering\\n []\\n\\n[31] [32 <../figures/paper/fig_training_curves_6panel.pdf>]\\nUnderfull \\\\hbox (badness 1092) in paragraph at lines 840--842\\n[]\\\\T1/ptm/b/n/10.95 (+20) Code: \\\\T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment\\n scripts, data-\\n []\\n\\n) [33 <../figures/paper/fig_steering_perturn_4panel.pdf>] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 832B04ACB55D37C1F8BC0949A90C07C7;10309.\\n ) \\nHere is how much of TeX's memory you used:\\n 17366 strings out of 469438\\n 282183 string characters out of 5468411\\n 750243 words of memory out of 5000000\\n 44892 multiletter control sequences out of 15000+600000\\n 712034 words of font info for 468 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,12n,93p,1585b,690s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/s\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/f\\nonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\nic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/h\\nelvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (33 pages, 1043184 bytes).\\nPDF statistics:\\n 1849 PDF objects out of 2073 (max. 8388607)\\n 1468 compressed objects within 15 object streams\\n 291 named destinations out of 1000 (max. 500000)\\n 77912 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 33, \"warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\"]}, \"pages\": 33, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 2--2\", \"Underfull \\\\hbox (badness 1789) in paragraph at lines 2--3\", \"Underfull \\\\hbox (badness 3333) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 7925) in paragraph at lines 29--30\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1117) in paragraph at lines 32--33\", \"Underfull \\\\hbox (badness 1655) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1205) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1360) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1097) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 2189) in paragraph at lines 3--1\", \"Underfull \\\\hbox (badness 2913) in paragraph at lines 99--103\", \"Underfull \\\\hbox (badness 5548) in paragraph at lines 72--73\", \"Underfull \\\\hbox (badness 1616) in paragraph at lines 141--142\", \"Underfull \\\\hbox (badness 1342) in paragraph at lines 169--170\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 285--285\", \"Underfull \\\\hbox (badness 3815) in paragraph at lines 362--363\", \"Underfull \\\\hbox (badness 2359) in paragraph at lines 370--371\", \"Underfull \\\\hbox (badness 2005) in paragraph at lines 449--450\", \"Underfull \\\\hbox (badness 1831) in paragraph at lines 453--454\", \"Overfull \\\\hbox (6.85715pt too wide) in paragraph at lines 470--481\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 487--488\", \"Underfull \\\\hbox (badness 3189) in paragraph at lines 489--490\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 6944) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 1087) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 4927) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 2326) in paragraph at lines 631--632\", \"Underfull \\\\hbox (badness 2401) in paragraph at lines 645--646\", \"Underfull \\\\vbox (badness 2343) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 673--674\", \"Underfull \\\\hbox (badness 4886) in paragraph at lines 685--686\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 6559) in paragraph at lines 702--703\", \"Underfull \\\\hbox (badness 1688) in paragraph at lines 781--781\", \"Underfull \\\\hbox (badness 1092) in paragraph at lines 840--842\"], \"issues\": [\"pages 33 > limit 8\"], \"summary\": \"FAIL: pages 33 > limit 8\"}"
    }
  },
  "sourceToolAssistantUUID": "cb2fa5d4-8186-4482-a858-6c2ee75891c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1005_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 5 审稿后写作修改（批量）  以下修改按优先级排序，全部完成后编译 PDF 上传。这次不用验证引用。  ### 1. 标题修改（MF2+SF5） \"Exposure Bias **Destroys** Auxiliary Attention Losses in Multi-Turn Dialogue\" → \"Exposure Bias **C…",
  "leafUuid": "d0b85bdc-3502-4ed2-9e3a-635347a1c062",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1006_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Tool call

_source line 1007 · 2026-05-25T09:00:50.222Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_011WBehbRuPqXKnLjADXvnXZ`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf",
  "project": "turn_residual_gating",
  "pages": "8",
  "dpi": 165
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0b85bdc-3502-4ed2-9e3a-635347a1c062",
  "isSidechain": false,
  "requestId": "req_011CbP1mnfvGtxi8Qads9twH",
  "type": "assistant",
  "uuid": "7e9475f5-d1ea-4793-95eb-34a7662a333e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013WnN6twLxzYgRR9tnDJ2FY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3916,
      "cache_read_input_tokens": 110590,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 110590,
          "cache_creation_input_tokens": 3916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3916
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

_source line 1008 · 2026-05-25T09:00:50.477Z_

<details><summary>↩ Tool result · `toolu_011WBehbRuPqXKnLjADXvnXZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p8.png\", \"width\": 1365, \"height\": 1930, \"size_kb\": 476.0}], \"total_pages\": 33, \"rendered_pages\": 1, \"dpi\": 165, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e9475f5-d1ea-4793-95eb-34a7662a333e",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "6c9afc53-483e-47bd-9fcd-b6f1c437e101",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"images\\\": [{\\\"page\\\": 8, \\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p8.png\\\", \\\"width\\\": 1365, \\\"height\\\": 1930, \\\"size_kb\\\": 476.0}], \\\"total_pages\\\": 33, \\\"rendered_pages\\\": 1, \\\"dpi\\\": 165, \\\"output_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p8.png\", \"width\": 1365, \"height\": 1930, \"size_kb\": 476.0}], \"total_pages\": 33, \"rendered_pages\": 1, \"dpi\": 165, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "7e9475f5-d1ea-4793-95eb-34a7662a333e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool call

_source line 1009 · 2026-05-25T09:00:53.784Z_

<details open><summary>🔧 Tool call — Read · `toolu_012DzzMgkdA2hNiuwrzQAZy9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c9afc53-483e-47bd-9fcd-b6f1c437e101",
  "isSidechain": false,
  "requestId": "req_011CbP1n5ZREiJygJEPZi7Pc",
  "type": "assistant",
  "uuid": "5a28ac53-b774-4b99-8b21-af9f0cf71afe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PacQVmL6EGurwRr6L1U9HH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 356,
      "cache_read_input_tokens": 114506,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 356,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 114506,
          "cache_creation_input_tokens": 356,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 356
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

_source line 1010 · 2026-05-25T09:00:54.750Z_

<details><summary>↩ Tool result · `toolu_012DzzMgkdA2hNiuwrzQAZy9`</summary>

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
  "parentUuid": "5a28ac53-b774-4b99-8b21-af9f0cf71afe",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "69b408d5-edb5-487f-99cc-b7901af8cb76",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 487399
    }
  },
  "sourceToolAssistantUUID": "5a28ac53-b774-4b99-8b21-af9f0cf71afe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1011_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 5 审稿后写作修改（批量）  以下修改按优先级排序，全部完成后编译 PDF 上传。这次不用验证引用。  ### 1. 标题修改（MF2+SF5） \"Exposure Bias **Destroys** Auxiliary Attention Losses in Multi-Turn Dialogue\" → \"Exposure Bias **C…",
  "leafUuid": "69b408d5-edb5-487f-99cc-b7901af8cb76",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1012_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Assistant

_source line 1013 · 2026-05-25T09:01:11.234Z_

<details><summary>Logged reasoning block</summary>

```text
Looking at page 8 now, I can see:
- Left column: Figure 6 (gate shift), then "1.5B confirms..." text, then "6 Discussion"
- Right column: Discussion continues, then the split-softmax/Rhea paragraph, then "7 Conclusion"
- The Conclusion text reads: "Auxiliary attention losses converge under teacher forcing (GAR=0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; β-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). 

Scheduled sampling compresses the gap to ~1.3× (Qwen) and ~2.9× (Llama)—the first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, generalizing across architectures and seeds.

The Conclusion still overflows by about a line. I need to save roughly one more line of space. Let me see if I can tighten either the Discussion section or compress the Conclusion itself further.

Looking at the current text, I could shorten "the first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers" to something more concise. Alternatively, I could try using `\enlargethispage{1\baselineskip}` to force an extra line on page 8, but that might introduce formatting issues.

I think the better approach is to trim the Conclusion a bit more.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69b408d5-edb5-487f-99cc-b7901af8cb76",
  "isSidechain": false,
  "requestId": "req_011CbP1nPmnuDTSELJC2USMg",
  "type": "assistant",
  "uuid": "a227c489-a12a-48aa-83be-b04d772fd931",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDa93McS9uNz18xMTNU9sW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 114862,
      "output_tokens": 713,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 713,
          "cache_read_input_tokens": 114862,
          "cache_creation_input_tokens": 472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 472
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

_source line 1014 · 2026-05-25T09:01:11.236Z_

Still 1 line over. Let me tighten the Conclusion to fit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a227c489-a12a-48aa-83be-b04d772fd931",
  "isSidechain": false,
  "requestId": "req_011CbP1nPmnuDTSELJC2USMg",
  "type": "assistant",
  "uuid": "9d835bb6-9540-4080-9cf3-e2c56bb5680f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDa93McS9uNz18xMTNU9sW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 114862,
      "output_tokens": 713,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 713,
          "cache_read_input_tokens": 114862,
          "cache_creation_input_tokens": 472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 472
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

_source line 1015 · 2026-05-25T09:01:12.140Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01G616XHqVfFuHrxvn2xdxQx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
  "old_string": "Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama)---the first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, generalizing across architectures and seeds.",
  "new_string": "Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds---the first such transfer to auxiliary attention objectives in multi-turn transformers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d835bb6-9540-4080-9cf3-e2c56bb5680f",
  "isSidechain": false,
  "requestId": "req_011CbP1nPmnuDTSELJC2USMg",
  "type": "assistant",
  "uuid": "3496e0d9-3db5-4aa8-ba36-4fbd81152a34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDa93McS9uNz18xMTNU9sW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 114862,
      "output_tokens": 713,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 713,
          "cache_read_input_tokens": 114862,
          "cache_creation_input_tokens": 472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 472
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

_source line 1016 · 2026-05-25T09:01:12.156Z_

<details><summary>↩ Tool result · `toolu_01G616XHqVfFuHrxvn2xdxQx`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3496e0d9-3db5-4aa8-ba36-4fbd81152a34",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "9220b9bf-455d-4b20-8846-85d5a95f6da8",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
    "oldString": "Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama)---the first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, generalizing across architectures and seeds.",
    "newString": "Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds---the first such transfer to auxiliary attention objectives in multi-turn transformers.",
    "originalFile": "\\section{Conclusion}\\label{sec:conclusion}\n\n\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama)---the first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, generalizing across architectures and seeds.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 3,
        "lines": [
          " \\section{Conclusion}\\label{sec:conclusion}",
          " ",
          "-\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama)---the first application of scheduled sampling to auxiliary attention objectives in multi-turn transformers, generalizing across architectures and seeds.",
          "+\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds---the first such transfer to auxiliary attention objectives in multi-turn transformers."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "3496e0d9-3db5-4aa8-ba36-4fbd81152a34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool call

_source line 1017 · 2026-05-25T09:01:16.331Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_01982DNXqSrYwdM2fD57irKJ`</summary>

```json
{
  "project": "turn_residual_gating",
  "max_pages": 8,
  "clean": true,
  "preview": false
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9220b9bf-455d-4b20-8846-85d5a95f6da8",
  "isSidechain": false,
  "requestId": "req_011CbP1ogBJMz3GD38de9apw",
  "type": "assistant",
  "uuid": "bd4f02f5-fe1e-4943-a93a-dbd0f3ef88ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WiviGosLJ7J8sK2DNxWZW3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 768,
      "cache_read_input_tokens": 115334,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 115334,
          "cache_creation_input_tokens": 768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 768
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

_source line 1018 · 2026-05-25T09:01:24.457Z_

<details><summary>↩ Tool result · `toolu_01982DNXqSrYwdM2fD57irKJ`</summary>

```text
{"result":"{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"on input line 759.\\n(pdftex.def)             Requested size: 341.43307pt x 345.55183pt.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `\\\\beta' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n<../figures/paper/fig_steering_perturn_4panel.pdf, id=1582, 241.8385pt x 399.49\\n25pt>\\nFile: ../figures/paper/fig_steering_perturn_4panel.pdf Graphic file (type pdf)\\n&lt;use ../figures/paper/fig_steering_perturn_4panel.pdf>\\nPackage pdftex.def Info: ../figures/paper/fig_steering_perturn_4panel.pdf  used\\n on input line 780.\\n(pdftex.def)             Requested size: 219.08614pt x 361.91727pt.\\n\\nUnderfull \\\\hbox (badness 1688) in paragraph at lines 781--781\\n[]\\\\T1/ptm/m/n/10 (+20) Figure 27: |Per-turn GAR un-der four $\\\\OML/cmm/m/it/10 ^\\n^L$\\\\T1/ptm/m/n/10 (+20) -steering\\n []\\n\\n[31] [32 <../figures/paper/fig_training_curves_6panel.pdf>]\\nUnderfull \\\\hbox (badness 1092) in paragraph at lines 840--842\\n[]\\\\T1/ptm/b/n/10.95 (+20) Code: \\\\T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment\\n scripts, data-\\n []\\n\\n) [33 <../figures/paper/fig_steering_perturn_4panel.pdf>] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 832B04ACB55D37C1F8BC0949A90C07C7;10309.\\n ) \\nHere is how much of TeX's memory you used:\\n 17366 strings out of 469438\\n 282183 string characters out of 5468411\\n 750243 words of memory out of 5000000\\n 44892 multiletter control sequences out of 15000+600000\\n 712034 words of font info for 468 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,12n,93p,1585b,690s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/s\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/f\\nonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\nic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/h\\nelvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (33 pages, 1043160 bytes).\\nPDF statistics:\\n 1849 PDF objects out of 2073 (max. 8388607)\\n 1468 compressed objects within 15 object streams\\n 291 named destinations out of 1000 (max. 500000)\\n 77912 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 33, \"warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\"]}, \"pages\": 33, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 2--2\", \"Underfull \\\\hbox (badness 1789) in paragraph at lines 2--3\", \"Underfull \\\\hbox (badness 3333) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 7925) in paragraph at lines 29--30\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1117) in paragraph at lines 32--33\", \"Underfull \\\\hbox (badness 1655) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1205) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1360) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1097) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1248) in paragraph at lines 3--1\", \"Underfull \\\\hbox (badness 2913) in paragraph at lines 99--103\", \"Underfull \\\\hbox (badness 5548) in paragraph at lines 72--73\", \"Underfull \\\\hbox (badness 1616) in paragraph at lines 141--142\", \"Underfull \\\\hbox (badness 1342) in paragraph at lines 169--170\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 285--285\", \"Underfull \\\\hbox (badness 3815) in paragraph at lines 362--363\", \"Underfull \\\\hbox (badness 2359) in paragraph at lines 370--371\", \"Underfull \\\\hbox (badness 2005) in paragraph at lines 449--450\", \"Underfull \\\\hbox (badness 1831) in paragraph at lines 453--454\", \"Overfull \\\\hbox (6.85715pt too wide) in paragraph at lines 470--481\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 487--488\", \"Underfull \\\\hbox (badness 3189) in paragraph at lines 489--490\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 6944) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 1087) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 4927) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 2326) in paragraph at lines 631--632\", \"Underfull \\\\hbox (badness 2401) in paragraph at lines 645--646\", \"Underfull \\\\vbox (badness 2343) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 673--674\", \"Underfull \\\\hbox (badness 4886) in paragraph at lines 685--686\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 6559) in paragraph at lines 702--703\", \"Underfull \\\\hbox (badness 1688) in paragraph at lines 781--781\", \"Underfull \\\\hbox (badness 1092) in paragraph at lines 840--842\"], \"issues\": [\"pages 33 > limit 8\"], \"summary\": \"FAIL: pages 33 > limit 8\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd4f02f5-fe1e-4943-a93a-dbd0f3ef88ec",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "a54a944f-b3ad-4470-8374-c8bf0c12b8a9",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"passed\\\": false, \\\"compiled\\\": {\\\"success\\\": true, \\\"pdf_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf\\\", \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"on input line 759.\\\\n(pdftex.def)             Requested size: 341.43307pt x 345.55183pt.\\\\n\\\\n\\\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\\\n(hyperref)                removing `math shift' on input line 764.\\\\n\\\\n\\\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\\\n(hyperref)                removing `\\\\\\\\beta' on input line 764.\\\\n\\\\n\\\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\\\n(hyperref)                removing `math shift' on input line 764.\\\\n\\\\n<../figures/paper/fig_steering_perturn_4panel.pdf, id=1582, 241.8385pt x 399.49\\\\n25pt>\\\\nFile: ../figures/paper/fig_steering_perturn_4panel.pdf Graphic file (type pdf)\\\\n&lt;use ../figures/paper/fig_steering_perturn_4panel.pdf>\\\\nPackage pdftex.def Info: ../figures/paper/fig_steering_perturn_4panel.pdf  used\\\\n on input line 780.\\\\n(pdftex.def)             Requested size: 219.08614pt x 361.91727pt.\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1688) in paragraph at lines 781--781\\\\n[]\\\\\\\\T1/ptm/m/n/10 (+20) Figure 27: |Per-turn GAR un-der four $\\\\\\\\OML/cmm/m/it/10 ^\\\\n^L$\\\\\\\\T1/ptm/m/n/10 (+20) -steering\\\\n []\\\\n\\\\n[31] [32 <../figures/paper/fig_training_curves_6panel.pdf>]\\\\nUnderfull \\\\\\\\hbox (badness 1092) in paragraph at lines 840--842\\\\n[]\\\\\\\\T1/ptm/b/n/10.95 (+20) Code: \\\\\\\\T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment\\\\n scripts, data-\\\\n []\\\\n\\\\n) [33 <../figures/paper/fig_steering_perturn_4panel.pdf>] (./main.aux)\\\\n ***********\\\\nLaTeX2e <2025-11-01>\\\\nL3 programming layer <2026-01-19>\\\\n ***********\\\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\\\n(rerunfilecheck)             Checksum: 832B04ACB55D37C1F8BC0949A90C07C7;10309.\\\\n ) \\\\nHere is how much of TeX's memory you used:\\\\n 17366 strings out of 469438\\\\n 282183 string characters out of 5468411\\\\n 750243 words of memory out of 5000000\\\\n 44892 multiletter control sequences out of 15000+600000\\\\n 712034 words of font info for 468 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,12n,93p,1585b,690s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/s\\\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/t\\\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive\\\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf\\\\n-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/f\\\\nonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\\\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\\\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\\\\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\\\\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p\\\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\\\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\\\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\\\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\\\\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\\\nnts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\\\ne1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\\\nic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/h\\\\nelvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.\\\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share\\\\n/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\\\nOutput written on main.pdf (33 pages, 1043160 bytes).\\\\nPDF statistics:\\\\n 1849 PDF objects out of 2073 (max. 8388607)\\\\n 1468 compressed objects within 15 object streams\\\\n 291 named destinations out of 1000 (max. 500000)\\\\n 77912 words of extra memory for PDF output out of 89155 (max. 10000000)\\\\n\\\", \\\"error\\\": \\\"\\\", \\\"pages\\\": 33, \\\"warnings\\\": [\\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\"]}, \\\"pages\\\": 33, \\\"page_status\\\": \\\"over_limit\\\", \\\"max_pages\\\": 8, \\\"min_pages\\\": null, \\\"critical_warnings\\\": [], \\\"minor_warnings\\\": [\\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 2--2\\\", \\\"Underfull \\\\\\\\hbox (badness 1789) in paragraph at lines 2--3\\\", \\\"Underfull \\\\\\\\hbox (badness 3333) in paragraph at lines 7--8\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 7--8\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 7--8\\\", \\\"Underfull \\\\\\\\hbox (badness 7925) in paragraph at lines 29--30\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1117) in paragraph at lines 32--33\\\", \\\"Underfull \\\\\\\\hbox (badness 1655) in paragraph at lines 3--4\\\", \\\"Underfull \\\\\\\\hbox (badness 1205) in paragraph at lines 3--4\\\", \\\"Underfull \\\\\\\\hbox (badness 1360) in paragraph at lines 5--6\\\", \\\"Underfull \\\\\\\\hbox (badness 1097) in paragraph at lines 5--6\\\", \\\"Underfull \\\\\\\\hbox (badness 1248) in paragraph at lines 3--1\\\", \\\"Underfull \\\\\\\\hbox (badness 2913) in paragraph at lines 99--103\\\", \\\"Underfull \\\\\\\\hbox (badness 5548) in paragraph at lines 72--73\\\", \\\"Underfull \\\\\\\\hbox (badness 1616) in paragraph at lines 141--142\\\", \\\"Underfull \\\\\\\\hbox (badness 1342) in paragraph at lines 169--170\\\", \\\"Underfull \\\\\\\\hbox (badness 1400) in paragraph at lines 285--285\\\", \\\"Underfull \\\\\\\\hbox (badness 3815) in paragraph at lines 362--363\\\", \\\"Underfull \\\\\\\\hbox (badness 2359) in paragraph at lines 370--371\\\", \\\"Underfull \\\\\\\\hbox (badness 2005) in paragraph at lines 449--450\\\", \\\"Underfull \\\\\\\\hbox (badness 1831) in paragraph at lines 453--454\\\", \\\"Overfull \\\\\\\\hbox (6.85715pt too wide) in paragraph at lines 470--481\\\", \\\"Underfull \\\\\\\\hbox (badness 1845) in paragraph at lines 487--488\\\", \\\"Underfull \\\\\\\\hbox (badness 3189) in paragraph at lines 489--490\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\hbox (badness 6944) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\hbox (badness 1087) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\hbox (badness 4927) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\hbox (badness 2326) in paragraph at lines 631--632\\\", \\\"Underfull \\\\\\\\hbox (badness 2401) in paragraph at lines 645--646\\\", \\\"Underfull \\\\\\\\vbox (badness 2343) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 2173) in paragraph at lines 673--674\\\", \\\"Underfull \\\\\\\\hbox (badness 4886) in paragraph at lines 685--686\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 6559) in paragraph at lines 702--703\\\", \\\"Underfull \\\\\\\\hbox (badness 1688) in paragraph at lines 781--781\\\", \\\"Underfull \\\\\\\\hbox (badness 1092) in paragraph at lines 840--842\\\"], \\\"issues\\\": [\\\"pages 33 > limit 8\\\"], \\\"summary\\\": \\\"FAIL: pages 33 > limit 8\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"on input line 759.\\n(pdftex.def)             Requested size: 341.43307pt x 345.55183pt.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `\\\\beta' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n<../figures/paper/fig_steering_perturn_4panel.pdf, id=1582, 241.8385pt x 399.49\\n25pt>\\nFile: ../figures/paper/fig_steering_perturn_4panel.pdf Graphic file (type pdf)\\n&lt;use ../figures/paper/fig_steering_perturn_4panel.pdf>\\nPackage pdftex.def Info: ../figures/paper/fig_steering_perturn_4panel.pdf  used\\n on input line 780.\\n(pdftex.def)             Requested size: 219.08614pt x 361.91727pt.\\n\\nUnderfull \\\\hbox (badness 1688) in paragraph at lines 781--781\\n[]\\\\T1/ptm/m/n/10 (+20) Figure 27: |Per-turn GAR un-der four $\\\\OML/cmm/m/it/10 ^\\n^L$\\\\T1/ptm/m/n/10 (+20) -steering\\n []\\n\\n[31] [32 <../figures/paper/fig_training_curves_6panel.pdf>]\\nUnderfull \\\\hbox (badness 1092) in paragraph at lines 840--842\\n[]\\\\T1/ptm/b/n/10.95 (+20) Code: \\\\T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment\\n scripts, data-\\n []\\n\\n) [33 <../figures/paper/fig_steering_perturn_4panel.pdf>] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 832B04ACB55D37C1F8BC0949A90C07C7;10309.\\n ) \\nHere is how much of TeX's memory you used:\\n 17366 strings out of 469438\\n 282183 string characters out of 5468411\\n 750243 words of memory out of 5000000\\n 44892 multiletter control sequences out of 15000+600000\\n 712034 words of font info for 468 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,12n,93p,1585b,690s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/s\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/f\\nonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\nic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/h\\nelvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (33 pages, 1043160 bytes).\\nPDF statistics:\\n 1849 PDF objects out of 2073 (max. 8388607)\\n 1468 compressed objects within 15 object streams\\n 291 named destinations out of 1000 (max. 500000)\\n 77912 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 33, \"warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\"]}, \"pages\": 33, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 2--2\", \"Underfull \\\\hbox (badness 1789) in paragraph at lines 2--3\", \"Underfull \\\\hbox (badness 3333) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 7925) in paragraph at lines 29--30\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1117) in paragraph at lines 32--33\", \"Underfull \\\\hbox (badness 1655) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1205) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1360) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1097) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1248) in paragraph at lines 3--1\", \"Underfull \\\\hbox (badness 2913) in paragraph at lines 99--103\", \"Underfull \\\\hbox (badness 5548) in paragraph at lines 72--73\", \"Underfull \\\\hbox (badness 1616) in paragraph at lines 141--142\", \"Underfull \\\\hbox (badness 1342) in paragraph at lines 169--170\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 285--285\", \"Underfull \\\\hbox (badness 3815) in paragraph at lines 362--363\", \"Underfull \\\\hbox (badness 2359) in paragraph at lines 370--371\", \"Underfull \\\\hbox (badness 2005) in paragraph at lines 449--450\", \"Underfull \\\\hbox (badness 1831) in paragraph at lines 453--454\", \"Overfull \\\\hbox (6.85715pt too wide) in paragraph at lines 470--481\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 487--488\", \"Underfull \\\\hbox (badness 3189) in paragraph at lines 489--490\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 6944) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 1087) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 4927) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 2326) in paragraph at lines 631--632\", \"Underfull \\\\hbox (badness 2401) in paragraph at lines 645--646\", \"Underfull \\\\vbox (badness 2343) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 673--674\", \"Underfull \\\\hbox (badness 4886) in paragraph at lines 685--686\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 6559) in paragraph at lines 702--703\", \"Underfull \\\\hbox (badness 1688) in paragraph at lines 781--781\", \"Underfull \\\\hbox (badness 1092) in paragraph at lines 840--842\"], \"issues\": [\"pages 33 > limit 8\"], \"summary\": \"FAIL: pages 33 > limit 8\"}"
    }
  },
  "sourceToolAssistantUUID": "bd4f02f5-fe1e-4943-a93a-dbd0f3ef88ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1019_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 5 审稿后写作修改（批量）  以下修改按优先级排序，全部完成后编译 PDF 上传。这次不用验证引用。  ### 1. 标题修改（MF2+SF5） \"Exposure Bias **Destroys** Auxiliary Attention Losses in Multi-Turn Dialogue\" → \"Exposure Bias **C…",
  "leafUuid": "a54a944f-b3ad-4470-8374-c8bf0c12b8a9",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1020_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Tool call

_source line 1021 · 2026-05-25T09:01:28.136Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01YFQ9ZDfP78LgJmkoM1xpCH`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf",
  "project": "turn_residual_gating",
  "pages": "8",
  "dpi": 165
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a54a944f-b3ad-4470-8374-c8bf0c12b8a9",
  "isSidechain": false,
  "requestId": "req_011CbP1paehJLJm2frxFWT51",
  "type": "assistant",
  "uuid": "3890b054-0b2a-4d19-ac4a-937eb880cdb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y94uciZbP5Jg8j3eTuRFp1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3916,
      "cache_read_input_tokens": 116102,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 116102,
          "cache_creation_input_tokens": 3916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3916
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

_source line 1022 · 2026-05-25T09:01:28.339Z_

<details><summary>↩ Tool result · `toolu_01YFQ9ZDfP78LgJmkoM1xpCH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p8.png\", \"width\": 1365, \"height\": 1930, \"size_kb\": 473.5}], \"total_pages\": 33, \"rendered_pages\": 1, \"dpi\": 165, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3890b054-0b2a-4d19-ac4a-937eb880cdb5",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "5d2f8efd-e04b-49b6-9553-9c0d997f23be",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"images\\\": [{\\\"page\\\": 8, \\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p8.png\\\", \\\"width\\\": 1365, \\\"height\\\": 1930, \\\"size_kb\\\": 473.5}], \\\"total_pages\\\": 33, \\\"rendered_pages\\\": 1, \\\"dpi\\\": 165, \\\"output_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p8.png\", \"width\": 1365, \"height\": 1930, \"size_kb\": 473.5}], \"total_pages\": 33, \"rendered_pages\": 1, \"dpi\": 165, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "3890b054-0b2a-4d19-ac4a-937eb880cdb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool call

_source line 1023 · 2026-05-25T09:01:31.302Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xh1capP13iju57T2xLBBcR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d2f8efd-e04b-49b6-9553-9c0d997f23be",
  "isSidechain": false,
  "requestId": "req_011CbP1psGpbdLu59sxdTgF4",
  "type": "assistant",
  "uuid": "6caa55dd-5e08-4f1b-89b5-fec4d4d9a02a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MajmF2air3nNBUt6onTXfC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 356,
      "cache_read_input_tokens": 120018,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 356,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 120018,
          "cache_creation_input_tokens": 356,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 356
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

_source line 1024 · 2026-05-25T09:01:32.043Z_

<details><summary>↩ Tool result · `toolu_01Xh1capP13iju57T2xLBBcR`</summary>

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
  "parentUuid": "6caa55dd-5e08-4f1b-89b5-fec4d4d9a02a",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "dc380dab-dd21-4ee6-9a9f-e27b48010b2f",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 484887
    }
  },
  "sourceToolAssistantUUID": "6caa55dd-5e08-4f1b-89b5-fec4d4d9a02a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1025_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 5 审稿后写作修改（批量）  以下修改按优先级排序，全部完成后编译 PDF 上传。这次不用验证引用。  ### 1. 标题修改（MF2+SF5） \"Exposure Bias **Destroys** Auxiliary Attention Losses in Multi-Turn Dialogue\" → \"Exposure Bias **C…",
  "leafUuid": "dc380dab-dd21-4ee6-9a9f-e27b48010b2f",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1026_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Assistant

_source line 1027 · 2026-05-25T09:01:38.480Z_

<details><summary>Logged reasoning block</summary>

```text
Still just barely overflows. The last visible text on page 8 is "the first such transfer to auxiliary attention objectives in multi-turn" and presumably "transformers." is on page 9. So just one word overflows.

Let me try a different approach — I'll add `\enlargethispage{0.5\baselineskip}` before the Conclusion to squeeze one more line on page 8. Or I can add `\looseness=-2` to the Conclusion.

Actually, let me try `\looseness=-2` on the Conclusion paragraph.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc380dab-dd21-4ee6-9a9f-e27b48010b2f",
  "isSidechain": false,
  "requestId": "req_011CbP1q98ZGZFvyJFmwiQeg",
  "type": "assistant",
  "uuid": "86388345-265b-40ab-aace-ff4fe0fc8c04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzvgdbkGUAdaRLrBQWdXh5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 120374,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 337,
          "cache_read_input_tokens": 120374,
          "cache_creation_input_tokens": 472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 472
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

_source line 1028 · 2026-05-25T09:01:39.042Z_

One word still overflows. Let me use `\looseness=-2` on the Conclusion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86388345-265b-40ab-aace-ff4fe0fc8c04",
  "isSidechain": false,
  "requestId": "req_011CbP1q98ZGZFvyJFmwiQeg",
  "type": "assistant",
  "uuid": "cafc41f1-962e-4523-8cb3-8f1e0aa5ffed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzvgdbkGUAdaRLrBQWdXh5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 120374,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 337,
          "cache_read_input_tokens": 120374,
          "cache_creation_input_tokens": 472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 472
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

_source line 1029 · 2026-05-25T09:01:40.739Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Uy9iPCEyrpwmKpREJJT1kX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
  "old_string": "\\looseness=-1 Auxiliary attention losses converge under teacher forcing",
  "new_string": "\\looseness=-2 Auxiliary attention losses converge under teacher forcing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cafc41f1-962e-4523-8cb3-8f1e0aa5ffed",
  "isSidechain": false,
  "requestId": "req_011CbP1q98ZGZFvyJFmwiQeg",
  "type": "assistant",
  "uuid": "52f76711-7130-4f07-b374-2c423f97f559",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CzvgdbkGUAdaRLrBQWdXh5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 120374,
      "output_tokens": 337,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 337,
          "cache_read_input_tokens": 120374,
          "cache_creation_input_tokens": 472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 472
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

_source line 1030 · 2026-05-25T09:01:40.750Z_

<details><summary>↩ Tool result · `toolu_01Uy9iPCEyrpwmKpREJJT1kX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52f76711-7130-4f07-b374-2c423f97f559",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "7bf8c0ef-6dcc-46ef-91d1-262f63f14644",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
    "oldString": "\\looseness=-1 Auxiliary attention losses converge under teacher forcing",
    "newString": "\\looseness=-2 Auxiliary attention losses converge under teacher forcing",
    "originalFile": "\\section{Conclusion}\\label{sec:conclusion}\n\n\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds---the first such transfer to auxiliary attention objectives in multi-turn transformers.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 3,
        "lines": [
          " \\section{Conclusion}\\label{sec:conclusion}",
          " ",
          "-\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds---the first such transfer to auxiliary attention objectives in multi-turn transformers.",
          "+\\looseness=-2 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds---the first such transfer to auxiliary attention objectives in multi-turn transformers."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "52f76711-7130-4f07-b374-2c423f97f559",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1031 · 2026-05-25T09:01:40.842Z_

```json
{
  "parentUuid": "7bf8c0ef-6dcc-46ef-91d1-262f63f14644",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "01e638ce-1fb6-4e46-a0f5-3db37d4d33a9",
  "timestamp": "2026-05-25T09:01:40.842Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---


### Tool call

_source line 1032 · 2026-05-25T09:01:44.222Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_01UpjhL3pSP1PFCiT4rL1fFM`</summary>

```json
{
  "project": "turn_residual_gating",
  "max_pages": 8,
  "clean": true,
  "preview": false
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01e638ce-1fb6-4e46-a0f5-3db37d4d33a9",
  "isSidechain": false,
  "requestId": "req_011CbP1qnkjzw5acCiiXvzQ3",
  "type": "assistant",
  "uuid": "4c81228b-45a3-4dcb-8675-22d2c5d5b6f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HN3Evv7TtYhJ7TWkbiAb7J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 120846,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 120846,
          "cache_creation_input_tokens": 496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 496
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

_source line 1033 · 2026-05-25T09:01:53.418Z_

<details><summary>↩ Tool result · `toolu_01UpjhL3pSP1PFCiT4rL1fFM`</summary>

```text
{"result":"{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"on input line 759.\\n(pdftex.def)             Requested size: 341.43307pt x 345.55183pt.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `\\\\beta' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n<../figures/paper/fig_steering_perturn_4panel.pdf, id=1582, 241.8385pt x 399.49\\n25pt>\\nFile: ../figures/paper/fig_steering_perturn_4panel.pdf Graphic file (type pdf)\\n&lt;use ../figures/paper/fig_steering_perturn_4panel.pdf>\\nPackage pdftex.def Info: ../figures/paper/fig_steering_perturn_4panel.pdf  used\\n on input line 780.\\n(pdftex.def)             Requested size: 219.08614pt x 361.91727pt.\\n\\nUnderfull \\\\hbox (badness 1688) in paragraph at lines 781--781\\n[]\\\\T1/ptm/m/n/10 (+20) Figure 27: |Per-turn GAR un-der four $\\\\OML/cmm/m/it/10 ^\\n^L$\\\\T1/ptm/m/n/10 (+20) -steering\\n []\\n\\n[31] [32 <../figures/paper/fig_training_curves_6panel.pdf>]\\nUnderfull \\\\hbox (badness 1092) in paragraph at lines 840--842\\n[]\\\\T1/ptm/b/n/10.95 (+20) Code: \\\\T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment\\n scripts, data-\\n []\\n\\n) [33 <../figures/paper/fig_steering_perturn_4panel.pdf>] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 832B04ACB55D37C1F8BC0949A90C07C7;10309.\\n ) \\nHere is how much of TeX's memory you used:\\n 17366 strings out of 469438\\n 282183 string characters out of 5468411\\n 750243 words of memory out of 5000000\\n 44892 multiletter control sequences out of 15000+600000\\n 712034 words of font info for 468 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,12n,93p,1585b,690s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/s\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/f\\nonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\nic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/h\\nelvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (33 pages, 1043160 bytes).\\nPDF statistics:\\n 1849 PDF objects out of 2073 (max. 8388607)\\n 1468 compressed objects within 15 object streams\\n 291 named destinations out of 1000 (max. 500000)\\n 77912 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 33, \"warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\"]}, \"pages\": 33, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 2--2\", \"Underfull \\\\hbox (badness 1789) in paragraph at lines 2--3\", \"Underfull \\\\hbox (badness 3333) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 7925) in paragraph at lines 29--30\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1117) in paragraph at lines 32--33\", \"Underfull \\\\hbox (badness 1655) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1205) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1360) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1097) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1248) in paragraph at lines 3--1\", \"Underfull \\\\hbox (badness 2913) in paragraph at lines 99--103\", \"Underfull \\\\hbox (badness 5548) in paragraph at lines 72--73\", \"Underfull \\\\hbox (badness 1616) in paragraph at lines 141--142\", \"Underfull \\\\hbox (badness 1342) in paragraph at lines 169--170\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 285--285\", \"Underfull \\\\hbox (badness 3815) in paragraph at lines 362--363\", \"Underfull \\\\hbox (badness 2359) in paragraph at lines 370--371\", \"Underfull \\\\hbox (badness 2005) in paragraph at lines 449--450\", \"Underfull \\\\hbox (badness 1831) in paragraph at lines 453--454\", \"Overfull \\\\hbox (6.85715pt too wide) in paragraph at lines 470--481\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 487--488\", \"Underfull \\\\hbox (badness 3189) in paragraph at lines 489--490\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 6944) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 1087) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 4927) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 2326) in paragraph at lines 631--632\", \"Underfull \\\\hbox (badness 2401) in paragraph at lines 645--646\", \"Underfull \\\\vbox (badness 2343) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 673--674\", \"Underfull \\\\hbox (badness 4886) in paragraph at lines 685--686\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 6559) in paragraph at lines 702--703\", \"Underfull \\\\hbox (badness 1688) in paragraph at lines 781--781\", \"Underfull \\\\hbox (badness 1092) in paragraph at lines 840--842\"], \"issues\": [\"pages 33 > limit 8\"], \"summary\": \"FAIL: pages 33 > limit 8\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c81228b-45a3-4dcb-8675-22d2c5d5b6f8",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "6898961c-5f92-47db-8cb1-0b57544181a8",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"passed\\\": false, \\\"compiled\\\": {\\\"success\\\": true, \\\"pdf_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf\\\", \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"on input line 759.\\\\n(pdftex.def)             Requested size: 341.43307pt x 345.55183pt.\\\\n\\\\n\\\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\\\n(hyperref)                removing `math shift' on input line 764.\\\\n\\\\n\\\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\\\n(hyperref)                removing `\\\\\\\\beta' on input line 764.\\\\n\\\\n\\\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\\\n(hyperref)                removing `math shift' on input line 764.\\\\n\\\\n<../figures/paper/fig_steering_perturn_4panel.pdf, id=1582, 241.8385pt x 399.49\\\\n25pt>\\\\nFile: ../figures/paper/fig_steering_perturn_4panel.pdf Graphic file (type pdf)\\\\n&lt;use ../figures/paper/fig_steering_perturn_4panel.pdf>\\\\nPackage pdftex.def Info: ../figures/paper/fig_steering_perturn_4panel.pdf  used\\\\n on input line 780.\\\\n(pdftex.def)             Requested size: 219.08614pt x 361.91727pt.\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1688) in paragraph at lines 781--781\\\\n[]\\\\\\\\T1/ptm/m/n/10 (+20) Figure 27: |Per-turn GAR un-der four $\\\\\\\\OML/cmm/m/it/10 ^\\\\n^L$\\\\\\\\T1/ptm/m/n/10 (+20) -steering\\\\n []\\\\n\\\\n[31] [32 <../figures/paper/fig_training_curves_6panel.pdf>]\\\\nUnderfull \\\\\\\\hbox (badness 1092) in paragraph at lines 840--842\\\\n[]\\\\\\\\T1/ptm/b/n/10.95 (+20) Code: \\\\\\\\T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment\\\\n scripts, data-\\\\n []\\\\n\\\\n) [33 <../figures/paper/fig_steering_perturn_4panel.pdf>] (./main.aux)\\\\n ***********\\\\nLaTeX2e <2025-11-01>\\\\nL3 programming layer <2026-01-19>\\\\n ***********\\\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\\\n(rerunfilecheck)             Checksum: 832B04ACB55D37C1F8BC0949A90C07C7;10309.\\\\n ) \\\\nHere is how much of TeX's memory you used:\\\\n 17366 strings out of 469438\\\\n 282183 string characters out of 5468411\\\\n 750243 words of memory out of 5000000\\\\n 44892 multiletter control sequences out of 15000+600000\\\\n 712034 words of font info for 468 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,12n,93p,1585b,690s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/s\\\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/t\\\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive\\\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf\\\\n-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/f\\\\nonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\\\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\\\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\\\\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\\\\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p\\\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\\\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\\\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\\\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\\\\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\\\nnts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\\\ne1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\\\nic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/h\\\\nelvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.\\\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share\\\\n/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\\\nOutput written on main.pdf (33 pages, 1043160 bytes).\\\\nPDF statistics:\\\\n 1849 PDF objects out of 2073 (max. 8388607)\\\\n 1468 compressed objects within 15 object streams\\\\n 291 named destinations out of 1000 (max. 500000)\\\\n 77912 words of extra memory for PDF output out of 89155 (max. 10000000)\\\\n\\\", \\\"error\\\": \\\"\\\", \\\"pages\\\": 33, \\\"warnings\\\": [\\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\"]}, \\\"pages\\\": 33, \\\"page_status\\\": \\\"over_limit\\\", \\\"max_pages\\\": 8, \\\"min_pages\\\": null, \\\"critical_warnings\\\": [], \\\"minor_warnings\\\": [\\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 2--2\\\", \\\"Underfull \\\\\\\\hbox (badness 1789) in paragraph at lines 2--3\\\", \\\"Underfull \\\\\\\\hbox (badness 3333) in paragraph at lines 7--8\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 7--8\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 7--8\\\", \\\"Underfull \\\\\\\\hbox (badness 7925) in paragraph at lines 29--30\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1117) in paragraph at lines 32--33\\\", \\\"Underfull \\\\\\\\hbox (badness 1655) in paragraph at lines 3--4\\\", \\\"Underfull \\\\\\\\hbox (badness 1205) in paragraph at lines 3--4\\\", \\\"Underfull \\\\\\\\hbox (badness 1360) in paragraph at lines 5--6\\\", \\\"Underfull \\\\\\\\hbox (badness 1097) in paragraph at lines 5--6\\\", \\\"Underfull \\\\\\\\hbox (badness 1248) in paragraph at lines 3--1\\\", \\\"Underfull \\\\\\\\hbox (badness 2913) in paragraph at lines 99--103\\\", \\\"Underfull \\\\\\\\hbox (badness 5548) in paragraph at lines 72--73\\\", \\\"Underfull \\\\\\\\hbox (badness 1616) in paragraph at lines 141--142\\\", \\\"Underfull \\\\\\\\hbox (badness 1342) in paragraph at lines 169--170\\\", \\\"Underfull \\\\\\\\hbox (badness 1400) in paragraph at lines 285--285\\\", \\\"Underfull \\\\\\\\hbox (badness 3815) in paragraph at lines 362--363\\\", \\\"Underfull \\\\\\\\hbox (badness 2359) in paragraph at lines 370--371\\\", \\\"Underfull \\\\\\\\hbox (badness 2005) in paragraph at lines 449--450\\\", \\\"Underfull \\\\\\\\hbox (badness 1831) in paragraph at lines 453--454\\\", \\\"Overfull \\\\\\\\hbox (6.85715pt too wide) in paragraph at lines 470--481\\\", \\\"Underfull \\\\\\\\hbox (badness 1845) in paragraph at lines 487--488\\\", \\\"Underfull \\\\\\\\hbox (badness 3189) in paragraph at lines 489--490\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\hbox (badness 6944) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\hbox (badness 1087) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\hbox (badness 4927) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\hbox (badness 2326) in paragraph at lines 631--632\\\", \\\"Underfull \\\\\\\\hbox (badness 2401) in paragraph at lines 645--646\\\", \\\"Underfull \\\\\\\\vbox (badness 2343) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 2173) in paragraph at lines 673--674\\\", \\\"Underfull \\\\\\\\hbox (badness 4886) in paragraph at lines 685--686\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 6559) in paragraph at lines 702--703\\\", \\\"Underfull \\\\\\\\hbox (badness 1688) in paragraph at lines 781--781\\\", \\\"Underfull \\\\\\\\hbox (badness 1092) in paragraph at lines 840--842\\\"], \\\"issues\\\": [\\\"pages 33 > limit 8\\\"], \\\"summary\\\": \\\"FAIL: pages 33 > limit 8\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"on input line 759.\\n(pdftex.def)             Requested size: 341.43307pt x 345.55183pt.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `\\\\beta' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n<../figures/paper/fig_steering_perturn_4panel.pdf, id=1582, 241.8385pt x 399.49\\n25pt>\\nFile: ../figures/paper/fig_steering_perturn_4panel.pdf Graphic file (type pdf)\\n&lt;use ../figures/paper/fig_steering_perturn_4panel.pdf>\\nPackage pdftex.def Info: ../figures/paper/fig_steering_perturn_4panel.pdf  used\\n on input line 780.\\n(pdftex.def)             Requested size: 219.08614pt x 361.91727pt.\\n\\nUnderfull \\\\hbox (badness 1688) in paragraph at lines 781--781\\n[]\\\\T1/ptm/m/n/10 (+20) Figure 27: |Per-turn GAR un-der four $\\\\OML/cmm/m/it/10 ^\\n^L$\\\\T1/ptm/m/n/10 (+20) -steering\\n []\\n\\n[31] [32 <../figures/paper/fig_training_curves_6panel.pdf>]\\nUnderfull \\\\hbox (badness 1092) in paragraph at lines 840--842\\n[]\\\\T1/ptm/b/n/10.95 (+20) Code: \\\\T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment\\n scripts, data-\\n []\\n\\n) [33 <../figures/paper/fig_steering_perturn_4panel.pdf>] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 832B04ACB55D37C1F8BC0949A90C07C7;10309.\\n ) \\nHere is how much of TeX's memory you used:\\n 17366 strings out of 469438\\n 282183 string characters out of 5468411\\n 750243 words of memory out of 5000000\\n 44892 multiletter control sequences out of 15000+600000\\n 712034 words of font info for 468 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,12n,93p,1585b,690s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/s\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/f\\nonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\nic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/h\\nelvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (33 pages, 1043160 bytes).\\nPDF statistics:\\n 1849 PDF objects out of 2073 (max. 8388607)\\n 1468 compressed objects within 15 object streams\\n 291 named destinations out of 1000 (max. 500000)\\n 77912 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 33, \"warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\"]}, \"pages\": 33, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 2--2\", \"Underfull \\\\hbox (badness 1789) in paragraph at lines 2--3\", \"Underfull \\\\hbox (badness 3333) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 7925) in paragraph at lines 29--30\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1117) in paragraph at lines 32--33\", \"Underfull \\\\hbox (badness 1655) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1205) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1360) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1097) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1248) in paragraph at lines 3--1\", \"Underfull \\\\hbox (badness 2913) in paragraph at lines 99--103\", \"Underfull \\\\hbox (badness 5548) in paragraph at lines 72--73\", \"Underfull \\\\hbox (badness 1616) in paragraph at lines 141--142\", \"Underfull \\\\hbox (badness 1342) in paragraph at lines 169--170\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 285--285\", \"Underfull \\\\hbox (badness 3815) in paragraph at lines 362--363\", \"Underfull \\\\hbox (badness 2359) in paragraph at lines 370--371\", \"Underfull \\\\hbox (badness 2005) in paragraph at lines 449--450\", \"Underfull \\\\hbox (badness 1831) in paragraph at lines 453--454\", \"Overfull \\\\hbox (6.85715pt too wide) in paragraph at lines 470--481\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 487--488\", \"Underfull \\\\hbox (badness 3189) in paragraph at lines 489--490\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 6944) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 1087) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 4927) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 2326) in paragraph at lines 631--632\", \"Underfull \\\\hbox (badness 2401) in paragraph at lines 645--646\", \"Underfull \\\\vbox (badness 2343) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 673--674\", \"Underfull \\\\hbox (badness 4886) in paragraph at lines 685--686\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 6559) in paragraph at lines 702--703\", \"Underfull \\\\hbox (badness 1688) in paragraph at lines 781--781\", \"Underfull \\\\hbox (badness 1092) in paragraph at lines 840--842\"], \"issues\": [\"pages 33 > limit 8\"], \"summary\": \"FAIL: pages 33 > limit 8\"}"
    }
  },
  "sourceToolAssistantUUID": "4c81228b-45a3-4dcb-8675-22d2c5d5b6f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1034_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 5 审稿后写作修改（批量）  以下修改按优先级排序，全部完成后编译 PDF 上传。这次不用验证引用。  ### 1. 标题修改（MF2+SF5） \"Exposure Bias **Destroys** Auxiliary Attention Losses in Multi-Turn Dialogue\" → \"Exposure Bias **C…",
  "leafUuid": "6898961c-5f92-47db-8cb1-0b57544181a8",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1035_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Assistant

_source line 1036 · 2026-05-25T09:01:58.941Z_

<details><summary>Logged reasoning block</summary>

```text
`\looseness=-2` probably can't compress a 5-line paragraph by 2 lines (it depends on the paragraph length and elasticity). The paragraph is only about 5-6 lines — `\looseness=-2` would make it 3-4 lines, which may not be achievable.

Let me take a different approach. I'll add `\enlargethispage{\baselineskip}` right before the Conclusion section. This tells LaTeX to make page 8 one line taller, which should be enough to absorb the overflow.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6898961c-5f92-47db-8cb1-0b57544181a8",
  "isSidechain": false,
  "requestId": "req_011CbP1riZzrtUYQacg1F45R",
  "type": "assistant",
  "uuid": "b6b0cfbe-ad92-4e83-a03d-e698150c634e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVHvvP7tBDbyyqUfgdWbAQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3916,
      "cache_read_input_tokens": 121342,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 372,
          "cache_read_input_tokens": 121342,
          "cache_creation_input_tokens": 3916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3916
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

_source line 1037 · 2026-05-25T09:01:59.430Z_

`\looseness=-2` may not be achievable for a short paragraph. Let me use `\enlargethispage` instead.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6b0cfbe-ad92-4e83-a03d-e698150c634e",
  "isSidechain": false,
  "requestId": "req_011CbP1riZzrtUYQacg1F45R",
  "type": "assistant",
  "uuid": "6c25bfc4-e8ed-45e2-8d44-2941fbc4c54b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVHvvP7tBDbyyqUfgdWbAQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3916,
      "cache_read_input_tokens": 121342,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 372,
          "cache_read_input_tokens": 121342,
          "cache_creation_input_tokens": 3916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3916
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

_source line 1038 · 2026-05-25T09:02:01.127Z_

<details open><summary>🔧 Tool call — Edit · `toolu_011BiC1G2S5UicbMJk8Hwi49`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
  "old_string": "\\section{Conclusion}\\label{sec:conclusion}\n\n\\looseness=-2 Auxiliary attention losses",
  "new_string": "\\enlargethispage{\\baselineskip}\n\\section{Conclusion}\\label{sec:conclusion}\n\n\\looseness=-1 Auxiliary attention losses"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c25bfc4-e8ed-45e2-8d44-2941fbc4c54b",
  "isSidechain": false,
  "requestId": "req_011CbP1riZzrtUYQacg1F45R",
  "type": "assistant",
  "uuid": "b644853a-ccab-449b-a37b-d6686b7321dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVHvvP7tBDbyyqUfgdWbAQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3916,
      "cache_read_input_tokens": 121342,
      "output_tokens": 372,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 372,
          "cache_read_input_tokens": 121342,
          "cache_creation_input_tokens": 3916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3916
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

_source line 1039 · 2026-05-25T09:02:01.138Z_

<details><summary>↩ Tool result · `toolu_011BiC1G2S5UicbMJk8Hwi49`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b644853a-ccab-449b-a37b-d6686b7321dd",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "de31213c-c067-46f2-af87-5bda42c0a3fa",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
    "oldString": "\\section{Conclusion}\\label{sec:conclusion}\n\n\\looseness=-2 Auxiliary attention losses",
    "newString": "\\enlargethispage{\\baselineskip}\n\\section{Conclusion}\\label{sec:conclusion}\n\n\\looseness=-1 Auxiliary attention losses",
    "originalFile": "\\section{Conclusion}\\label{sec:conclusion}\n\n\\looseness=-2 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds---the first such transfer to auxiliary attention objectives in multi-turn transformers.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 3,
        "newStart": 1,
        "newLines": 4,
        "lines": [
          "+\\enlargethispage{\\baselineskip}",
          " \\section{Conclusion}\\label{sec:conclusion}",
          " ",
          "-\\looseness=-2 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds---the first such transfer to auxiliary attention objectives in multi-turn transformers.",
          "+\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds---the first such transfer to auxiliary attention objectives in multi-turn transformers."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "b644853a-ccab-449b-a37b-d6686b7321dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool call

_source line 1040 · 2026-05-25T09:02:04.611Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_compile_and_check · `toolu_01LzW3aBihaUNu6UTQXkJ3Jn`</summary>

```json
{
  "project": "turn_residual_gating",
  "max_pages": 8,
  "clean": true,
  "preview": false
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de31213c-c067-46f2-af87-5bda42c0a3fa",
  "isSidechain": false,
  "requestId": "req_011CbP1sHmmdm46tigoSXQKL",
  "type": "assistant",
  "uuid": "d06132c9-ee12-4557-9745-2a3d3c54b144",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGLYwxUay84dzbqEH88Ay9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 427,
      "cache_read_input_tokens": 125258,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 427,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 125,
          "cache_read_input_tokens": 125258,
          "cache_creation_input_tokens": 427,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 427
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

_source line 1041 · 2026-05-25T09:02:12.222Z_

<details><summary>↩ Tool result · `toolu_01LzW3aBihaUNu6UTQXkJ3Jn`</summary>

```text
{"result":"{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"on input line 759.\\n(pdftex.def)             Requested size: 341.43307pt x 345.55183pt.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `\\\\beta' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n<../figures/paper/fig_steering_perturn_4panel.pdf, id=1582, 241.8385pt x 399.49\\n25pt>\\nFile: ../figures/paper/fig_steering_perturn_4panel.pdf Graphic file (type pdf)\\n&lt;use ../figures/paper/fig_steering_perturn_4panel.pdf>\\nPackage pdftex.def Info: ../figures/paper/fig_steering_perturn_4panel.pdf  used\\n on input line 780.\\n(pdftex.def)             Requested size: 219.08614pt x 361.91727pt.\\n\\nUnderfull \\\\hbox (badness 1688) in paragraph at lines 781--781\\n[]\\\\T1/ptm/m/n/10 (+20) Figure 27: |Per-turn GAR un-der four $\\\\OML/cmm/m/it/10 ^\\n^L$\\\\T1/ptm/m/n/10 (+20) -steering\\n []\\n\\n[31] [32 <../figures/paper/fig_training_curves_6panel.pdf>]\\nUnderfull \\\\hbox (badness 1092) in paragraph at lines 840--842\\n[]\\\\T1/ptm/b/n/10.95 (+20) Code: \\\\T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment\\n scripts, data-\\n []\\n\\n) [33 <../figures/paper/fig_steering_perturn_4panel.pdf>] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 832B04ACB55D37C1F8BC0949A90C07C7;10309.\\n ) \\nHere is how much of TeX's memory you used:\\n 17366 strings out of 469438\\n 282183 string characters out of 5468411\\n 751092 words of memory out of 5000000\\n 44892 multiletter control sequences out of 15000+600000\\n 712034 words of font info for 468 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,12n,93p,1585b,692s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/s\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/f\\nonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\nic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/h\\nelvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (33 pages, 1043143 bytes).\\nPDF statistics:\\n 1849 PDF objects out of 2073 (max. 8388607)\\n 1468 compressed objects within 15 object streams\\n 291 named destinations out of 1000 (max. 500000)\\n 77912 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 33, \"warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\"]}, \"pages\": 33, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 2--2\", \"Underfull \\\\hbox (badness 1789) in paragraph at lines 2--3\", \"Underfull \\\\hbox (badness 3333) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 7925) in paragraph at lines 29--30\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1117) in paragraph at lines 32--33\", \"Underfull \\\\hbox (badness 1655) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1205) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1360) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1097) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1248) in paragraph at lines 4--1\", \"Underfull \\\\hbox (badness 2913) in paragraph at lines 99--103\", \"Underfull \\\\hbox (badness 5548) in paragraph at lines 72--73\", \"Underfull \\\\hbox (badness 1616) in paragraph at lines 141--142\", \"Underfull \\\\hbox (badness 1342) in paragraph at lines 169--170\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 285--285\", \"Underfull \\\\hbox (badness 3815) in paragraph at lines 362--363\", \"Underfull \\\\hbox (badness 2359) in paragraph at lines 370--371\", \"Underfull \\\\hbox (badness 2005) in paragraph at lines 449--450\", \"Underfull \\\\hbox (badness 1831) in paragraph at lines 453--454\", \"Overfull \\\\hbox (6.85715pt too wide) in paragraph at lines 470--481\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 487--488\", \"Underfull \\\\vbox (badness 1859) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 3189) in paragraph at lines 489--490\", \"Underfull \\\\vbox (badness 1048) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 6944) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 1087) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 4927) in paragraph at lines 543--544\", \"Underfull \\\\vbox (badness 4634) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 2326) in paragraph at lines 631--632\", \"Underfull \\\\hbox (badness 2401) in paragraph at lines 645--646\", \"Underfull \\\\vbox (badness 2343) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 673--674\", \"Underfull \\\\hbox (badness 4886) in paragraph at lines 685--686\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 6559) in paragraph at lines 702--703\", \"Underfull \\\\hbox (badness 1688) in paragraph at lines 781--781\", \"Underfull \\\\hbox (badness 1092) in paragraph at lines 840--842\"], \"issues\": [\"pages 33 > limit 8\"], \"summary\": \"FAIL: pages 33 > limit 8\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d06132c9-ee12-4557-9745-2a3d3c54b144",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "d66d0998-4f37-44b9-91f4-47d4a3a749eb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"passed\\\": false, \\\"compiled\\\": {\\\"success\\\": true, \\\"pdf_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf\\\", \\\"paper_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper\\\", \\\"main_tex\\\": \\\"main.tex\\\", \\\"log_tail\\\": \\\"on input line 759.\\\\n(pdftex.def)             Requested size: 341.43307pt x 345.55183pt.\\\\n\\\\n\\\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\\\n(hyperref)                removing `math shift' on input line 764.\\\\n\\\\n\\\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\\\n(hyperref)                removing `\\\\\\\\beta' on input line 764.\\\\n\\\\n\\\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\\\n(hyperref)                removing `math shift' on input line 764.\\\\n\\\\n<../figures/paper/fig_steering_perturn_4panel.pdf, id=1582, 241.8385pt x 399.49\\\\n25pt>\\\\nFile: ../figures/paper/fig_steering_perturn_4panel.pdf Graphic file (type pdf)\\\\n&lt;use ../figures/paper/fig_steering_perturn_4panel.pdf>\\\\nPackage pdftex.def Info: ../figures/paper/fig_steering_perturn_4panel.pdf  used\\\\n on input line 780.\\\\n(pdftex.def)             Requested size: 219.08614pt x 361.91727pt.\\\\n\\\\nUnderfull \\\\\\\\hbox (badness 1688) in paragraph at lines 781--781\\\\n[]\\\\\\\\T1/ptm/m/n/10 (+20) Figure 27: |Per-turn GAR un-der four $\\\\\\\\OML/cmm/m/it/10 ^\\\\n^L$\\\\\\\\T1/ptm/m/n/10 (+20) -steering\\\\n []\\\\n\\\\n[31] [32 <../figures/paper/fig_training_curves_6panel.pdf>]\\\\nUnderfull \\\\\\\\hbox (badness 1092) in paragraph at lines 840--842\\\\n[]\\\\\\\\T1/ptm/b/n/10.95 (+20) Code: \\\\\\\\T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment\\\\n scripts, data-\\\\n []\\\\n\\\\n) [33 <../figures/paper/fig_steering_perturn_4panel.pdf>] (./main.aux)\\\\n ***********\\\\nLaTeX2e <2025-11-01>\\\\nL3 programming layer <2026-01-19>\\\\n ***********\\\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\\\n(rerunfilecheck)             Checksum: 832B04ACB55D37C1F8BC0949A90C07C7;10309.\\\\n ) \\\\nHere is how much of TeX's memory you used:\\\\n 17366 strings out of 469438\\\\n 282183 string characters out of 5468411\\\\n 751092 words of memory out of 5000000\\\\n 44892 multiletter control sequences out of 15000+600000\\\\n 712034 words of font info for 468 fonts, out of 8000000 for 9000\\\\n 59 hyphenation exceptions out of 8191\\\\n 84i,12n,93p,1585b,692s stack positions out of 10000i,1000n,20000p,200000b,200000s\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>\\\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/s\\\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/t\\\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive\\\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf\\\\n-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/f\\\\nonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\\\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\\\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\\\\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\\\\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p\\\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\\\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\\\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\\\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\\\\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\\\nnts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\\\ne1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\\\nic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/h\\\\nelvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.\\\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share\\\\n/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\\\nOutput written on main.pdf (33 pages, 1043143 bytes).\\\\nPDF statistics:\\\\n 1849 PDF objects out of 2073 (max. 8388607)\\\\n 1468 compressed objects within 15 object streams\\\\n 291 named destinations out of 1000 (max. 500000)\\\\n 77912 words of extra memory for PDF output out of 89155 (max. 10000000)\\\\n\\\", \\\"error\\\": \\\"\\\", \\\"pages\\\": 33, \\\"warnings\\\": [\\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\"]}, \\\"pages\\\": 33, \\\"page_status\\\": \\\"over_limit\\\", \\\"max_pages\\\": 8, \\\"min_pages\\\": null, \\\"critical_warnings\\\": [], \\\"minor_warnings\\\": [\\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"`h' float specifier changed to `ht'.\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Token not allowed in a PDF string (Unicode):\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 2--2\\\", \\\"Underfull \\\\\\\\hbox (badness 1789) in paragraph at lines 2--3\\\", \\\"Underfull \\\\\\\\hbox (badness 3333) in paragraph at lines 7--8\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 7--8\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 7--8\\\", \\\"Underfull \\\\\\\\hbox (badness 7925) in paragraph at lines 29--30\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 1117) in paragraph at lines 32--33\\\", \\\"Underfull \\\\\\\\hbox (badness 1655) in paragraph at lines 3--4\\\", \\\"Underfull \\\\\\\\hbox (badness 1205) in paragraph at lines 3--4\\\", \\\"Underfull \\\\\\\\hbox (badness 1360) in paragraph at lines 5--6\\\", \\\"Underfull \\\\\\\\hbox (badness 1097) in paragraph at lines 5--6\\\", \\\"Underfull \\\\\\\\hbox (badness 1248) in paragraph at lines 4--1\\\", \\\"Underfull \\\\\\\\hbox (badness 2913) in paragraph at lines 99--103\\\", \\\"Underfull \\\\\\\\hbox (badness 5548) in paragraph at lines 72--73\\\", \\\"Underfull \\\\\\\\hbox (badness 1616) in paragraph at lines 141--142\\\", \\\"Underfull \\\\\\\\hbox (badness 1342) in paragraph at lines 169--170\\\", \\\"Underfull \\\\\\\\hbox (badness 1400) in paragraph at lines 285--285\\\", \\\"Underfull \\\\\\\\hbox (badness 3815) in paragraph at lines 362--363\\\", \\\"Underfull \\\\\\\\hbox (badness 2359) in paragraph at lines 370--371\\\", \\\"Underfull \\\\\\\\hbox (badness 2005) in paragraph at lines 449--450\\\", \\\"Underfull \\\\\\\\hbox (badness 1831) in paragraph at lines 453--454\\\", \\\"Overfull \\\\\\\\hbox (6.85715pt too wide) in paragraph at lines 470--481\\\", \\\"Underfull \\\\\\\\hbox (badness 1845) in paragraph at lines 487--488\\\", \\\"Underfull \\\\\\\\vbox (badness 1859) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 3189) in paragraph at lines 489--490\\\", \\\"Underfull \\\\\\\\vbox (badness 1048) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 10000) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\hbox (badness 6944) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\hbox (badness 1087) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\hbox (badness 4927) in paragraph at lines 543--544\\\", \\\"Underfull \\\\\\\\vbox (badness 4634) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 2326) in paragraph at lines 631--632\\\", \\\"Underfull \\\\\\\\hbox (badness 2401) in paragraph at lines 645--646\\\", \\\"Underfull \\\\\\\\vbox (badness 2343) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 2173) in paragraph at lines 673--674\\\", \\\"Underfull \\\\\\\\hbox (badness 4886) in paragraph at lines 685--686\\\", \\\"Underfull \\\\\\\\vbox (badness 10000) has occurred while \\\\\\\\output is active []\\\", \\\"Underfull \\\\\\\\hbox (badness 6559) in paragraph at lines 702--703\\\", \\\"Underfull \\\\\\\\hbox (badness 1688) in paragraph at lines 781--781\\\", \\\"Underfull \\\\\\\\hbox (badness 1092) in paragraph at lines 840--842\\\"], \\\"issues\\\": [\\\"pages 33 > limit 8\\\"], \\\"summary\\\": \\\"FAIL: pages 33 > limit 8\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"passed\": false, \"compiled\": {\"success\": true, \"pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf\", \"paper_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper\", \"main_tex\": \"main.tex\", \"log_tail\": \"on input line 759.\\n(pdftex.def)             Requested size: 341.43307pt x 345.55183pt.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `\\\\beta' on input line 764.\\n\\n\\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\\n(hyperref)                removing `math shift' on input line 764.\\n\\n<../figures/paper/fig_steering_perturn_4panel.pdf, id=1582, 241.8385pt x 399.49\\n25pt>\\nFile: ../figures/paper/fig_steering_perturn_4panel.pdf Graphic file (type pdf)\\n&lt;use ../figures/paper/fig_steering_perturn_4panel.pdf>\\nPackage pdftex.def Info: ../figures/paper/fig_steering_perturn_4panel.pdf  used\\n on input line 780.\\n(pdftex.def)             Requested size: 219.08614pt x 361.91727pt.\\n\\nUnderfull \\\\hbox (badness 1688) in paragraph at lines 781--781\\n[]\\\\T1/ptm/m/n/10 (+20) Figure 27: |Per-turn GAR un-der four $\\\\OML/cmm/m/it/10 ^\\n^L$\\\\T1/ptm/m/n/10 (+20) -steering\\n []\\n\\n[31] [32 <../figures/paper/fig_training_curves_6panel.pdf>]\\nUnderfull \\\\hbox (badness 1092) in paragraph at lines 840--842\\n[]\\\\T1/ptm/b/n/10.95 (+20) Code: \\\\T1/ptm/m/n/10.95 (+20) draft-ing ex-per-i-ment\\n scripts, data-\\n []\\n\\n) [33 <../figures/paper/fig_steering_perturn_4panel.pdf>] (./main.aux)\\n ***********\\nLaTeX2e <2025-11-01>\\nL3 programming layer <2026-01-19>\\n ***********\\nPackage rerunfilecheck Info: File `main.out' has not changed.\\n(rerunfilecheck)             Checksum: 832B04ACB55D37C1F8BC0949A90C07C7;10309.\\n ) \\nHere is how much of TeX's memory you used:\\n 17366 strings out of 469438\\n 282183 string characters out of 5468411\\n 751092 words of memory out of 5000000\\n 44892 multiletter control sequences out of 15000+600000\\n 712034 words of font info for 468 fonts, out of 8000000 for 9000\\n 59 hyphenation exceptions out of 8191\\n 84i,12n,93p,1585b,692s stack positions out of 10000i,1000n,20000p,200000b,200000s\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/inconsolata/Inconsolata-zi4\\nr.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>\\n&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/s\\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb>&lt;/usr/share/texlive/texmf\\n-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/f\\nonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\\npe1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\\nlic/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\\nm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.p\\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr\\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/t\\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive\\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-\\ndist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fo\\nnts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\\ne1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\\nic/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/h\\nelvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.\\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share\\n/texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>\\nOutput written on main.pdf (33 pages, 1043143 bytes).\\nPDF statistics:\\n 1849 PDF objects out of 2073 (max. 8388607)\\n 1468 compressed objects within 15 object streams\\n 291 named destinations out of 1000 (max. 500000)\\n 77912 words of extra memory for PDF output out of 89155 (max. 10000000)\\n\", \"error\": \"\", \"pages\": 33, \"warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\"]}, \"pages\": 33, \"page_status\": \"over_limit\", \"max_pages\": 8, \"min_pages\": null, \"critical_warnings\": [], \"minor_warnings\": [\"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"`h' float specifier changed to `ht'.\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Token not allowed in a PDF string (Unicode):\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 2--2\", \"Underfull \\\\hbox (badness 1789) in paragraph at lines 2--3\", \"Underfull \\\\hbox (badness 3333) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 7--8\", \"Underfull \\\\hbox (badness 7925) in paragraph at lines 29--30\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 1117) in paragraph at lines 32--33\", \"Underfull \\\\hbox (badness 1655) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1205) in paragraph at lines 3--4\", \"Underfull \\\\hbox (badness 1360) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1097) in paragraph at lines 5--6\", \"Underfull \\\\hbox (badness 1248) in paragraph at lines 4--1\", \"Underfull \\\\hbox (badness 2913) in paragraph at lines 99--103\", \"Underfull \\\\hbox (badness 5548) in paragraph at lines 72--73\", \"Underfull \\\\hbox (badness 1616) in paragraph at lines 141--142\", \"Underfull \\\\hbox (badness 1342) in paragraph at lines 169--170\", \"Underfull \\\\hbox (badness 1400) in paragraph at lines 285--285\", \"Underfull \\\\hbox (badness 3815) in paragraph at lines 362--363\", \"Underfull \\\\hbox (badness 2359) in paragraph at lines 370--371\", \"Underfull \\\\hbox (badness 2005) in paragraph at lines 449--450\", \"Underfull \\\\hbox (badness 1831) in paragraph at lines 453--454\", \"Overfull \\\\hbox (6.85715pt too wide) in paragraph at lines 470--481\", \"Underfull \\\\hbox (badness 1845) in paragraph at lines 487--488\", \"Underfull \\\\vbox (badness 1859) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 3189) in paragraph at lines 489--490\", \"Underfull \\\\vbox (badness 1048) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 10000) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 6944) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 1087) in paragraph at lines 543--544\", \"Underfull \\\\hbox (badness 4927) in paragraph at lines 543--544\", \"Underfull \\\\vbox (badness 4634) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 2326) in paragraph at lines 631--632\", \"Underfull \\\\hbox (badness 2401) in paragraph at lines 645--646\", \"Underfull \\\\vbox (badness 2343) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 2173) in paragraph at lines 673--674\", \"Underfull \\\\hbox (badness 4886) in paragraph at lines 685--686\", \"Underfull \\\\vbox (badness 10000) has occurred while \\\\output is active []\", \"Underfull \\\\hbox (badness 6559) in paragraph at lines 702--703\", \"Underfull \\\\hbox (badness 1688) in paragraph at lines 781--781\", \"Underfull \\\\hbox (badness 1092) in paragraph at lines 840--842\"], \"issues\": [\"pages 33 > limit 8\"], \"summary\": \"FAIL: pages 33 > limit 8\"}"
    }
  },
  "sourceToolAssistantUUID": "d06132c9-ee12-4557-9745-2a3d3c54b144",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1042_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 5 审稿后写作修改（批量）  以下修改按优先级排序，全部完成后编译 PDF 上传。这次不用验证引用。  ### 1. 标题修改（MF2+SF5） \"Exposure Bias **Destroys** Auxiliary Attention Losses in Multi-Turn Dialogue\" → \"Exposure Bias **C…",
  "leafUuid": "d66d0998-4f37-44b9-91f4-47d4a3a749eb",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1043_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Tool call

_source line 1044 · 2026-05-25T09:02:16.357Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_011XuWnbQTsuUmfDJ8bmDd1P`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/main.pdf",
  "project": "turn_residual_gating",
  "pages": "8,9",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d66d0998-4f37-44b9-91f4-47d4a3a749eb",
  "isSidechain": false,
  "requestId": "req_011CbP1t6tTbVQmWTqJdijXe",
  "type": "assistant",
  "uuid": "526786a1-b168-46fd-92e4-0a7b3c60f998",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FWnx9aRrBqNcwrR1bEu3yJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3973,
      "cache_read_input_tokens": 125685,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 125685,
          "cache_creation_input_tokens": 3973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3973
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

_source line 1045 · 2026-05-25T09:02:16.722Z_

<details><summary>↩ Tool result · `toolu_011XuWnbQTsuUmfDJ8bmDd1P`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 445.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 579.4}], \"total_pages\": 33, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "526786a1-b168-46fd-92e4-0a7b3c60f998",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "cdac00b6-ac37-4804-958e-e3884fe5bd9f",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"images\\\": [{\\\"page\\\": 8, \\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p8.png\\\", \\\"width\\\": 1241, \\\"height\\\": 1754, \\\"size_kb\\\": 445.3}, {\\\"page\\\": 9, \\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p9.png\\\", \\\"width\\\": 1241, \\\"height\\\": 1754, \\\"size_kb\\\": 579.4}], \\\"total_pages\\\": 33, \\\"rendered_pages\\\": 2, \\\"dpi\\\": 150, \\\"output_dir\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 445.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 579.4}], \"total_pages\": 33, \"rendered_pages\": 2, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "526786a1-b168-46fd-92e4-0a7b3c60f998",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool call

_source line 1046 · 2026-05-25T09:02:19.452Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KrW4kgZwTh44FJzFLn9xLy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdac00b6-ac37-4804-958e-e3884fe5bd9f",
  "isSidechain": false,
  "requestId": "req_011CbP1tSCok2HiD1vnaZQ9g",
  "type": "assistant",
  "uuid": "586e2209-f654-4f41-9cc6-368eb21c16ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019xBZ8U7QW4m8PSUCTa2eca",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 129658,
      "output_tokens": 94,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 442,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 94,
          "cache_read_input_tokens": 129658,
          "cache_creation_input_tokens": 442,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 442
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

_source line 1047 · 2026-05-25T09:02:20.065Z_

<details><summary>↩ Tool result · `toolu_01KrW4kgZwTh44FJzFLn9xLy`</summary>

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
  "parentUuid": "586e2209-f654-4f41-9cc6-368eb21c16ea",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "91d799db-72dd-4cd0-ae90-64c1dfce5ac2",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 456009
    }
  },
  "sourceToolAssistantUUID": "586e2209-f654-4f41-9cc6-368eb21c16ea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1048_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 5 审稿后写作修改（批量）  以下修改按优先级排序，全部完成后编译 PDF 上传。这次不用验证引用。  ### 1. 标题修改（MF2+SF5） \"Exposure Bias **Destroys** Auxiliary Attention Losses in Multi-Turn Dialogue\" → \"Exposure Bias **C…",
  "leafUuid": "91d799db-72dd-4cd0-ae90-64c1dfce5ac2",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1049_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Assistant

_source line 1050 · 2026-05-25T09:02:26.621Z_

<details><summary>Logged reasoning block</summary>

```text
Still overflows by the last word "transformers." at the very bottom of the right column. The `\enlargethispage{\baselineskip}` gave one extra line but it's still not quite enough. The page now extends slightly lower than usual. Let me try `\enlargethispage{2\baselineskip}` to get two extra lines.

Wait, actually the image shows the word "transformers." is visible at the very bottom of page 8. Let me check page 9 to confirm nothing else from the main text spills over.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91d799db-72dd-4cd0-ae90-64c1dfce5ac2",
  "isSidechain": false,
  "requestId": "req_011CbP1tgU3zcAerEbki7z5b",
  "type": "assistant",
  "uuid": "07a6057c-0ce6-42cb-8dd4-a1d53ece2f6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L14FLvgkpQG5hRUqJCF1ud",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 130100,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 130100,
          "cache_creation_input_tokens": 472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 472
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

_source line 1051 · 2026-05-25T09:02:26.811Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JrNjjQwBHJYPVw5kv9z27c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/_pdf_images/main_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07a6057c-0ce6-42cb-8dd4-a1d53ece2f6d",
  "isSidechain": false,
  "requestId": "req_011CbP1tgU3zcAerEbki7z5b",
  "type": "assistant",
  "uuid": "1faf760b-2441-4588-a031-bb627179bd20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L14FLvgkpQG5hRUqJCF1ud",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 472,
      "cache_read_input_tokens": 130100,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 130100,
          "cache_creation_input_tokens": 472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 472
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

_source line 1052 · 2026-05-25T09:02:27.419Z_

<details><summary>↩ Tool result · `toolu_01JrNjjQwBHJYPVw5kv9z27c`</summary>

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
  "parentUuid": "1faf760b-2441-4588-a031-bb627179bd20",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "09ebb06b-d692-497c-8c1f-1437648952ae",
  "toolUseResult": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/jpeg",
      "originalSize": 593317
    }
  },
  "sourceToolAssistantUUID": "1faf760b-2441-4588-a031-bb627179bd20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1053_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] Round 5 审稿后写作修改（批量）  以下修改按优先级排序，全部完成后编译 PDF 上传。这次不用验证引用。  ### 1. 标题修改（MF2+SF5） \"Exposure Bias **Destroys** Auxiliary Attention Losses in Multi-Turn Dialogue\" → \"Exposure Bias **C…",
  "leafUuid": "09ebb06b-d692-497c-8c1f-1437648952ae",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1054_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Assistant

_source line 1055 · 2026-05-25T09:02:31.535Z_

Page 9 now starts with "8 Limitations" — the entire Conclusion fits on page 8. Main text is within 8 pages. Now reporting to Director.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09ebb06b-d692-497c-8c1f-1437648952ae",
  "isSidechain": false,
  "requestId": "req_011CbP1uDqh38FYUJsKPBQns",
  "type": "assistant",
  "uuid": "6194e4ae-39b1-4077-bc0e-ee21f171e032",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L99c9pvirw7RSyHoK9r4Pv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 130572,
      "output_tokens": 922,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 609,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 922,
          "cache_read_input_tokens": 130572,
          "cache_creation_input_tokens": 609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 609
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

_source line 1056 · 2026-05-25T09:02:56.380Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_agent_post_to_director · `toolu_012FgBWhfc5ybARPqkq5qzS7`</summary>

```json
{
  "text": "[写作进展] Round 5 审稿后批量修改完成（8/8 项）\n\n## 修改清单\n\n### 1. 标题 ✅\n\"Destroys\" → \"Collapses\"（main.tex + fig1 caption）\n\n### 2. Exposure bias 措辞降级 ✅\n- 全文 7 处 \"the proximal cause\" / \"root cause\" → \"a proximal cause\" / \"primary contributing factor\"\n- §6 Discussion KV cache drift 扩展：添加 switching experiment 预告（\"training with SS but evaluating with ground-truth KV cache could disentangle\"），明确 \"cannot fully rule out a secondary role\"\n- Conclusion 同步降级\n\n### 3. Split-softmax / Rhea 对比 ✅\n§6 Discussion 新增段落：split-softmax（inference-time softmax domain separation）、Rhea（role-aware episodic attention）与 β-steering（diagnostic tool, not production-ready）的区别；SS（training-time, modifies representations）vs inference-time（leave training unchanged but cannot recover unlearned patterns）trade-off\n\n### 4. β-steering 解耦 ✅\n§4.3 拆分：(1) GAR recovery \"partly by construction\"——boosting logits mechanically increases attention metric；(2) 反事实论证——hidden-state drift 下 reweighting 不应恢复 GAR；(3) 下游 instruction retention +11.1pp, p=0.077 未达显著水平，单独报告\n- Discussion 中删除重复的下游结果\n\n### 5. GAR-ours vs GAR-D 选择理由 ✅\n§3.1 补充：GAR-Dongre 被 NTP attention 稀释至 ~0.01-0.02 失去区分度；GAR-ours 保持 order-of-magnitude range；差异本身是发现——goal attention 集中在 last-token position\n\n### 6. PCGrad 失败 scope 限定 ✅\n- §5.2 标题 + 正文：\"gradient conflict\" → \"gradient direction conflict\"（6 处，含 §1、§2、Appendix）\n- 补充：PCGrad 消除方向冲突但不处理 magnitude imbalance；worsening 可能部分反映投影副作用\n\n### 7. 数字冗余去除 ✅\n保留：Abstract、§4.2 首次报告、Table/Figure captions\n替换为回指：§1（2处）、§5.5、§6、§7 → \"order of magnitude\" / \"the observed gap\"\n\n### 8. LoRA rank capacity ✅\n§8 Limitations 更新：rank 16 fixed, higher ranks (32/64) might affect magnitude but unlikely direction given five-way consistency\n\n## 页面验证\n主文 8 页完整（Conclusion 结束在 P8，Limitations 从 P9 开始）。编译无 critical warnings。总页数 33。",
  "project": "turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6194e4ae-39b1-4077-bc0e-ee21f171e032",
  "isSidechain": false,
  "requestId": "req_011CbP1uDqh38FYUJsKPBQns",
  "type": "assistant",
  "uuid": "1d36bbbb-550f-4cbc-aae3-7c25e17c0323",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L99c9pvirw7RSyHoK9r4Pv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 609,
      "cache_read_input_tokens": 130572,
      "output_tokens": 922,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 609,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 922,
          "cache_read_input_tokens": 130572,
          "cache_creation_input_tokens": 609,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 609
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

_source line 1057 · 2026-05-25T09:03:00.788Z_

<details><summary>↩ Tool result · `toolu_012FgBWhfc5ybARPqkq5qzS7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d36bbbb-550f-4cbc-aae3-7c25e17c0323",
  "isSidechain": false,
  "promptId": "e629358b-d46e-4030-975d-addc2acdf7c3",
  "type": "user",
  "uuid": "7a5deb5e-bcf2-46bb-a393-78286ebfdda1",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_640e53b6afbbd5e34eb7273cd5a707a0:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "1d36bbbb-550f-4cbc-aae3-7c25e17c0323",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1058_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1059 · 2026-05-25T09:03:08.178Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T09:03:08.178Z",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "content": "[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director 将结果发给 Director。"
}
```

---


### Runtime record

_source line 1060 · 2026-05-25T09:03:08.178Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T09:03:08.178Z",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


## Round 24

## Round 24

2 recorded events


### User

_source line 1061 · 2026-05-25T09:03:08.163Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a5deb5e-bcf2-46bb-a393-78286ebfdda1",
  "isSidechain": false,
  "promptId": "1785bb60-969b-44b7-9ee1-b00ab5eea6f6",
  "type": "user",
  "isMeta": true,
  "uuid": "5243403e-ac0c-4b61-a38e-a2e4737f8b6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Assistant

_source line 1062 · 2026-05-25T09:03:08.164Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5243403e-ac0c-4b61-a38e-a2e4737f8b6d",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "5d6ae429-57e1-4cff-8fb7-a05206f685df",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "id": "cfb6e857-da5d-4927-a42d-680ee8303aea",
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


## Round 25

## Round 25

5 recorded events


### User

_source line 1063 · 2026-05-25T09:03:08.309Z_

[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director 将结果发给 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5d6ae429-57e1-4cff-8fb7-a05206f685df",
  "isSidechain": false,
  "promptId": "1785bb60-969b-44b7-9ee1-b00ab5eea6f6",
  "type": "user",
  "uuid": "98e48408-1e51-4847-8963-22a1e2b6f1f3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1064 · 2026-05-25T09:03:08.309Z_

```json
{
  "parentUuid": "98e48408-1e51-4847-8963-22a1e2b6f1f3",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "44c70f1c-874a-4dda-a2b5-1cde6cb7e88f",
  "timestamp": "2026-05-25T09:03:08.309Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---


### Runtime record

_source line 1065_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1066 · 2026-05-25T09:03:18.515Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T09:03:18.515Z",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "content": "[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director 将结果发给 Director。"
}
```

---


### Runtime record

_source line 1067 · 2026-05-25T09:03:18.515Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T09:03:18.515Z",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


## Round 26

## Round 26

2 recorded events


### User

_source line 1068 · 2026-05-25T09:03:18.500Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44c70f1c-874a-4dda-a2b5-1cde6cb7e88f",
  "isSidechain": false,
  "promptId": "de60e850-2669-407e-b01a-e5c2a3e6de64",
  "type": "user",
  "isMeta": true,
  "uuid": "1886493f-417b-425f-b0ba-f78e2730e71b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Assistant

_source line 1069 · 2026-05-25T09:03:18.500Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1886493f-417b-425f-b0ba-f78e2730e71b",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "0bd5b5b5-f23f-4c7e-82b1-a2cfcdd1964b",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "id": "eeae6e2c-a421-45e8-bb57-3c1719baf9c6",
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


## Round 27

## Round 27

5 recorded events


### User

_source line 1070 · 2026-05-25T09:03:18.659Z_

[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director 将结果发给 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0bd5b5b5-f23f-4c7e-82b1-a2cfcdd1964b",
  "isSidechain": false,
  "promptId": "de60e850-2669-407e-b01a-e5c2a3e6de64",
  "type": "user",
  "uuid": "e4472cf6-b032-4d23-ae06-4498a0cd1f6c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1071_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1072 · 2026-05-25T09:03:36.104Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T09:03:36.104Z",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "content": "[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director 将结果发给 Director。"
}
```

---


### Runtime record

_source line 1073 · 2026-05-25T09:03:36.105Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T09:03:36.105Z",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Assistant

_source line 1074 · 2026-05-25T09:03:36.088Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4472cf6-b032-4d23-ae06-4498a0cd1f6c",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "e8e4d805-a0bb-438e-b1be-20208686bf96",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "id": "fb0daad0-f3e2-4ef6-b6c4-799920541f7e",
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


## Round 28

## Round 28

5 recorded events


### User

_source line 1075 · 2026-05-25T09:03:36.245Z_

[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director 将结果发给 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8e4d805-a0bb-438e-b1be-20208686bf96",
  "isSidechain": false,
  "promptId": "70e01c54-8091-4498-b5ac-15f86a2b778e",
  "type": "user",
  "uuid": "ff3c83a2-c519-4f90-a76f-c4d855d154ee",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1076_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1077 · 2026-05-25T09:05:57.551Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-25T09:05:57.551Z",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "content": "[Director 指令] [Patch] 附录内容引用完整性检查\n\n**任务：** 检查论文附录的所有内容是否在正文中都有准确、合理的引用，修复孤儿附录。\n\n**Step 1：逐项盘点**\n列出附录里每一个 section/subsection/table/figure/algorithm/proof/prompt。\n\n**Step 2：逐项验证引用**\n对每一项，在正文搜索是否有至少一句话指向它。合格引用示例：\n- \"(see Appendix A for full hyperparameters)\"\n- \"Table 5 in Appendix C reports the breakdown\"\n\n不合格引用：\n- 只在末尾甩一句 \"See appendix for more details\"（没指向具体 section）\n- 在 Limitations/Conclusion 才提一次（应该在内容相关章节引出）\n- 引用了但没说明为什么读者要去看\n\n**Step 3：修复**\n- 优选：在最相关的正文章节加一句自然引用，说明为什么读者要翻那里、能找到什么\n- 次选：若附录内容对核心 claim 不必要且找不到合适引用位置，删除该附录内容\n- 禁止：在章节末尾硬塞 \"See Appendix X.\" 作为补丁\n\n**引用质量原则：** 每条引用让 reviewer 立刻明白 (1) 为什么要翻 (2) 能找到什么。\n\n完成后汇报：(a) 附录有多少个 section/subsection 及内容 (b) 哪些原本无正文引用、现在加在哪里 (c) 是否有附录被删除。\n\n编译 PDF 上传。这次不用验证引用。"
}
```

---


### Runtime record

_source line 1078 · 2026-05-25T09:05:57.551Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-25T09:05:57.551Z",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Assistant

_source line 1079 · 2026-05-25T09:05:57.536Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff3c83a2-c519-4f90-a76f-c4d855d154ee",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "76e0cc10-9fbc-4211-b9c0-3e111f2dcc97",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "id": "9dc1356a-9038-4e51-84f1-95a7a2d6e2ae",
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


## Round 29

## Round 29

26 recorded events


### User

_source line 1080 · 2026-05-25T09:05:57.732Z_

[Director 指令] [Patch] 附录内容引用完整性检查

**任务：** 检查论文附录的所有内容是否在正文中都有准确、合理的引用，修复孤儿附录。

**Step 1：逐项盘点**
列出附录里每一个 section/subsection/table/figure/algorithm/proof/prompt。

**Step 2：逐项验证引用**
对每一项，在正文搜索是否有至少一句话指向它。合格引用示例：
- "(see Appendix A for full hyperparameters)"
- "Table 5 in Appendix C reports the breakdown"

不合格引用：
- 只在末尾甩一句 "See appendix for more details"（没指向具体 section）
- 在 Limitations/Conclusion 才提一次（应该在内容相关章节引出）
- 引用了但没说明为什么读者要去看

**Step 3：修复**
- 优选：在最相关的正文章节加一句自然引用，说明为什么读者要翻那里、能找到什么
- 次选：若附录内容对核心 claim 不必要且找不到合适引用位置，删除该附录内容
- 禁止：在章节末尾硬塞 "See Appendix X." 作为补丁

**引用质量原则：** 每条引用让 reviewer 立刻明白 (1) 为什么要翻 (2) 能找到什么。

完成后汇报：(a) 附录有多少个 section/subsection 及内容 (b) 哪些原本无正文引用、现在加在哪里 (c) 是否有附录被删除。

编译 PDF 上传。这次不用验证引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76e0cc10-9fbc-4211-b9c0-3e111f2dcc97",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "741c8e9e-5237-4ab2-931b-9e94306143f3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Assistant

_source line 1081 · 2026-05-25T09:06:05.745Z_

<details><summary>Logged reasoning block</summary>

```text
The Director wants me to audit all appendix content for proper cross-references from the main text. Let me:

1. Read the full appendix to catalog every section/subsection/table/figure
2. Search the main text for references to each appendix item
3. Fix any orphaned appendix content

Let me start by reading the full appendix.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "741c8e9e-5237-4ab2-931b-9e94306143f3",
  "isSidechain": false,
  "requestId": "req_011CbP2Aj6FenfnATWawAxoJ",
  "type": "assistant",
  "uuid": "37ace468-5b3f-4adc-a027-ae3d3ed8e8e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rq3HHKRpiBKzPdvAzvTEo9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 132097,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 132097,
          "cache_creation_input_tokens": 520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 520
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 85315
      }
    }
  }
}
```

</details>

---


### Assistant

_source line 1082 · 2026-05-25T09:06:06.252Z_

先完整读取附录，盘点所有内容项。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37ace468-5b3f-4adc-a027-ae3d3ed8e8e8",
  "isSidechain": false,
  "requestId": "req_011CbP2Aj6FenfnATWawAxoJ",
  "type": "assistant",
  "uuid": "8bb4dc7b-4248-4992-ba6d-a42f423359d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rq3HHKRpiBKzPdvAzvTEo9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 132097,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 132097,
          "cache_creation_input_tokens": 520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 520
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 85315
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 1083 · 2026-05-25T09:06:06.813Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BnbCxgqyfkYzXcSFnhGb9w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bb4dc7b-4248-4992-ba6d-a42f423359d0",
  "isSidechain": false,
  "requestId": "req_011CbP2Aj6FenfnATWawAxoJ",
  "type": "assistant",
  "uuid": "689014ed-a7a4-461f-bfd2-5d1c632897b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rq3HHKRpiBKzPdvAzvTEo9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 132097,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 520,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 201,
          "cache_read_input_tokens": 132097,
          "cache_creation_input_tokens": 520,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 520
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 85315
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 1084 · 2026-05-25T09:06:07.129Z_

<details><summary>↩ Tool result · reported error · `toolu_01BnbCxgqyfkYzXcSFnhGb9w`</summary>

```text
File content (26103 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "689014ed-a7a4-461f-bfd2-5d1c632897b4",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "68618b2f-2957-4cb4-b2c9-ac2517bff613",
  "toolUseResult": "Error: File content (26103 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "689014ed-a7a4-461f-bfd2-5d1c632897b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool call

_source line 1085 · 2026-05-25T09:06:11.510Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DJC4xTcEnbn1eVXANevkYe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68618b2f-2957-4cb4-b2c9-ac2517bff613",
  "isSidechain": false,
  "requestId": "req_011CbP2BRGUUEQcLnFrai1rV",
  "type": "assistant",
  "uuid": "0930769e-7fac-48ca-b103-eeb486fd2214",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019xt221V3LmDQbj9Fj2hq1R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 262,
      "cache_read_input_tokens": 132617,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 262,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 107,
          "cache_read_input_tokens": 132617,
          "cache_creation_input_tokens": 262,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 262
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

_source line 1086 · 2026-05-25T09:06:11.792Z_

<details><summary>↩ Tool result · `toolu_01DJC4xTcEnbn1eVXANevkYe`</summary>

```text
1	\section{Training Configuration}\label{sec:appendix-hyper}
2	
3	Table~\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\times$ learning rate multiplier and are initialized with bias 1.5 ($\sigma(1.5) \approx 0.82$); the gate MLP adds ${\sim}$57K parameters per variant ($<$0.001\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB VRAM), requiring 6--8 hours per variant.
4	
5	\begin{table}[h]
6	\centering\small
7	\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\dagger$ apply only to ThreadGate and its ablations.}
8	\label{tab:hyperparams}
9	\begin{tabular}{l@{\hspace{8pt}}l}
10	\toprule
11	\textbf{Parameter} & \textbf{Value} \\
12	\midrule
13	Base model & Qwen-2.5-7B-Instruct \\
14	LoRA rank / $\alpha$ & 16 / 32 \\
15	LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
16	Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
17	Learning rate & $2 \times 10^{-4}$ \\
18	Gate LR mult.$^\dagger$ & $10\times$ \\
19	Batch / grad accum & 1 / 8 (eff.\ 8) \\
20	Epochs & 3 \\
21	Max seq length & 2048 \\
22	Training data & 8K UltraChat convs \\
23	Seed & 42 (+123 for TG, SS) \\
24	$\lambda_\text{GAR}$/$\lambda_\text{div}$ & 1.0 / 1.0 \\
25	GAR target $\tau$ & 0.5 \\
26	Gate init bias$^\dagger$ & 1.5 ($\sigma\!\approx\!0.82$) \\
27	Gate hidden dim$^\dagger$ & 64 \\
28	Turn embed dim$^\dagger$ & 16 \\
29	GPU & RTX PRO 6000 (96\,GB) \\
30	Training time & 6--8 h / variant \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Loss Formulation Search}\label{sec:appendix-loss}
36	
37	The final MSE + gate diversity loss (\S\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.
38	
39	\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.
40	
41	\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\text{mean}(\text{GAR})$). The unbounded objective rewards full pass-through ($g \to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\lambda$=2 (v3), gates froze within 100 steps; at $\lambda$=10 (v3b), convergence to identity accelerated; at $\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.
42	
43	\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.
44	
45	\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\tau$ incurs the same penalty as GAR below $\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\mathcal{L}_\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).
46	
47	\begin{table*}[t]
48	\centering\footnotesize
49	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
50	\label{tab:loss-iterations}
51	\begin{tabular}{l l l p{5.8cm} c c}
52	\toprule
53	 & \textbf{Loss Family} & \textbf{Status} & \textbf{Failure Mechanism} & \textbf{GAR} & \textbf{PPL} \\
54	\midrule
55	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\
56	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & Numerical instability from cumulative product; $\varepsilon$-stabilization insufficient & ---  & ---  \\
57	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\
58	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & Higher $\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\
59	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\
60	v6  & Smooth saturation       & \texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\
61	v7  & MSE + gate div          & \checkmark~\textbf{converged}  & \textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\
62	\bottomrule
63	\end{tabular}
64	\end{table*}
65	
66	\section{Instruction Retention Details}\label{sec:appendix-ir}
67	
68	To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\beta$\,=\,3 steering on $N$\,=\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.
69	
70	\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\,=\,54 paired evaluations (18 types $\times$ 3 conversations per type) for the McNemar analysis.
71	
72	\paragraph{Per-category results.} Table~\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.
73	
74	\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\,=\,0.200, $p$\,=\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\,=\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.
75	
76	Figure~\ref{fig:ir-bar} visualizes the per-category breakdown.
77	
78	\begin{figure}[h]
79	  \centering
80	  \includegraphics[width=\columnwidth]{fig_instruction_retention.pdf}
81	  \caption{Instruction retention by constraint category under $\beta$\,=\,3 steering. Content constraints benefit most (+23.8\,pp); format and count constraints are unaffected.}
82	  \label{fig:ir-bar}
83	\end{figure}
84	
85	\begin{table}[h]
86	\centering\small
87	\caption{Instruction retention by constraint category ($\beta$\,=\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}
88	\label{tab:ir-results}
89	\begin{tabular}{lccc}
90	\toprule
91	\textbf{Category} & $\beta$\,=\,0 & $\beta$\,=\,3 & $\Delta$ \\
92	\midrule
93	Content    & 61.9\% & 85.7\% & +23.8\,pp \\
94	Position   & 66.7\% & 73.3\% & +6.7\,pp \\
95	Count      & 100\%  & 100\%  & 0 \\
96	Format     & 100\%  & 100\%  & 0 \\
97	\midrule
98	\textbf{Overall} & 75.9\% & 87.0\% & +11.1\,pp \\
99	\bottomrule
100	\end{tabular}
101	\end{table}
102	
103	\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
104	
105	The main results (Table~\ref{tab:four-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.
106	
107	\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\times$ (0.064 vs.\ 0.037 in the $N$\,=\,50 evaluation) to 0.64$\times$ (0.016 vs.\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\,=\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.
108	
109	\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\times$ of the base model's GAR, compared to 3.4$\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.
110	
111	\paragraph{Caveats.} The $N$\,=\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.
112	
113	\begin{table}[h]
114	\centering\small
115	\caption{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref{tab:four-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}
116	\label{tab:n5-ar}
117	\begin{tabular}{lcc}
118	\toprule
119	\textbf{Configuration} & \textbf{AR GAR-O} & \textbf{$\Delta$ vs.\ Table~\ref{tab:four-way}} \\
120	\midrule
121	Base & 0.012 & $-$0.007 \\
122	\midrule
123	ThreadGate & 0.016 & $-$0.048 \\
124	\;+\,PCGrad & 0.015 & $-$0.015 \\
125	Uniform Gate & 0.015 & $-$0.018 \\
126	LoRA-only & 0.025 & $-$0.012 \\
127	\bottomrule
128	\end{tabular}
129	\end{table}
130	
131	\section{Statistical Test Details}\label{sec:appendix-stats}
132	
133	All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\ref{tab:stat-tests} consolidates the full results.
134	
135	\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\ LoRA-only comparison ($p$\,=\,0.004, $r$\,=\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\ +PCGrad comparison ($p$\,=\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.
136	
137	\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:four-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
138	
139	\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \leq r < 0.5$ is medium, and $r \geq 0.5$ is large. The TG vs.\ LoRA-only effect ($r$\,=\,0.454) is medium, and TG vs.\ Base ($r$\,=\,0.802) is large.
140	
141	\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \leq 0.004$) survive this correction.
142	
143	\begin{table}[h]
144	\centering\small
145	\caption{Consolidated statistical tests. All AR comparisons use $N$\,=\,50 conversations (39 with $\geq$3 turns); gate conditioning uses 28 layers.}
146	\label{tab:stat-tests}
147	\begin{tabular}{llcc}
148	\toprule
149	\textbf{Comparison} & \textbf{Test} & $p$ & $r$ \\
150	\midrule
151	\multicolumn{4}{l}{\emph{AR GAR-ours ($\beta$\,=\,0)}} \\
152	TG vs.\ Base & Wilcoxon & $<$0.001 & 0.802 \\
153	TG vs.\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\
154	TG vs.\ +PCGrad & Wilcoxon & 0.002 & --- \\
155	SS vs.\ TG & Wilcoxon & $<$0.001 & 0.869 \\
156	\midrule
157	\multicolumn{4}{l}{\emph{Gate conditioning (28 layers)}} \\
158	Turn 1 vs.\ Turn 21 & Wilcoxon & $3.7\!\times\!10^{-8}$ & 0.975 \\
159	\midrule
160	\multicolumn{4}{l}{\emph{Instruction retention}} \\
161	$\beta$\,=\,0 vs.\ $\beta$\,=\,3 & McNemar & 0.077 & --- \\
162	GAR--compliance & Pearson & 0.007 & 0.200 \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	
167	\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
168	
169	Table~\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \S\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.
170	
171	\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\ 0.50).
172	
173	\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\,=\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\% for ThreadGate (mean 0.043, std 0.100), and 5\% of turn-level measurements exhibit sporadic attention spikes (GAR $\geq$ 0.4). We therefore report both mean and median.
174	
175	\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719, L24\,=\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\times$ by median for Llama vs.\ 8--17$\times$ for Qwen).
176	
177	\begin{table}[h]
178	\centering\small
179	\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\,=\,50); AR: autoregressive ($N$\,=\,20 for Base/TG/LoRA-only, $N$\,=\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}
180	\label{tab:llama-full}
181	\resizebox{\columnwidth}{!}{%
182	\begin{tabular}{lcccc}
183	\toprule
184	& \multicolumn{2}{c}{\textbf{TF}} & \multicolumn{2}{c}{\textbf{AR}} \\
185	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
186	& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\
187	\midrule
188	Base & 0.017 & 3.45 & 0.009 & 0.009 \\
189	ThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\
190	LoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\
191	\textbf{SS} & 0.477 & 2.82 & \textbf{0.166} & --- \\
192	\bottomrule
193	\end{tabular}}
194	\end{table}
195	
196	\begin{figure}[t]
197	  \centering
198	  \includegraphics[width=\columnwidth]{fig_crossmodel.pdf}
199	  \caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\times$ by median), exceeding Qwen's 8$\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}
200	  \label{fig:crossmodel}
201	\end{figure}
202	
203	\paragraph{Cross-model summary.} Table~\ref{tab:crossmodel-detail} consolidates the cross-model comparison, showing TF GAR, AR GAR, PPL, and gap ratios side by side for both architectures. The consistent pattern---TF GAR $\approx$ 0.5, AR GAR $\ll$ 0.1, gap $\geq$ 7.9$\times$---across two architectures with different layer counts, attention head configurations, and pre-training corpora provides strong evidence that exposure bias is architecture-independent. Notably, Llama's larger gaps (27$\times$ by median for TG; mean-based range 11.2--17.2$\times$) compared to Qwen's (7.9--13.5$\times$) may reflect its deeper architecture (32 vs.\ 28 layers), which allows more layers for distributional drift to compound through.
204	
205	\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}
206	
207	\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\times$), compared to 1.28$\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.
208	
209	\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\% longer than Qwen due to Llama's larger layer count (32 vs.\ 28 layers).
210	
211	\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\% decline. This is steeper than Qwen's 70.8\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\ 28 KV heads).
212	
213	\paragraph{Cross-model gradient analysis.} Table~\ref{tab:gradient-crossmodel} compares NTP--GAR gradient interaction between the two architectures. Both models exhibit near-orthogonal gradients (cosine similarity $\approx$\,0), not systematic conflict: Qwen shows a slight negative mean ($-$0.042) while Llama is marginally positive (+0.005). NTP gradients dominate GAR by 14.7$\times$ on Qwen and 25.7$\times$ on Llama, indicating that the auxiliary signal is overwhelmed by magnitude rather than opposed by direction. The cross-model consistency---near-zero cosine similarity and order-of-magnitude NTP dominance on both architectures---reinforces the \emph{modus tollens} argument (\S\ref{subsec:pcgrad}): gradient direction conflict is not the primary cause of the TF-AR gap.
214	
215	\begin{table}[h]
216	\centering\small
217	\caption{Cross-model NTP--GAR gradient interaction. Gradients are near-orthogonal on both architectures; NTP magnitude dominates GAR by 15--26$\times$.}
218	\label{tab:gradient-crossmodel}
219	\begin{tabular}{lcc}
220	\toprule
221	\textbf{Metric} & \textbf{Qwen-7B} & \textbf{Llama-8B} \\
222	\midrule
223	Mean cos sim & $-$0.042 & +0.005 \\
224	Neg-layer \% & 67.9\% & 53.1\% \\
225	NTP/GAR mag ratio & 14.7$\times$ & 25.7$\times$ \\
226	\bottomrule
227	\end{tabular}
228	\end{table}
229	
230	\section{Additional Visualizations}\label{sec:appendix-viz}
231	
232	This section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.
233	
234	\subsection{Gate Profile Heatmap}
235	
236	Figure~\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.
237	
238	\begin{figure}[h]
239	\centering
240	\includegraphics[width=\columnwidth]{fig_gate_profile_heatmap.pdf}
241	\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\times$ 5 conditions) and Llama-3.1-8B (32 layers $\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}
242	\label{fig:gate-heatmap}
243	\end{figure}
244	
245	\subsection{Cross-Model Gate Profile Comparison}
246	
247	Figure~\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\,=\,0.793, L5\,=\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.
248	
249	\begin{figure}[h]
250	\centering
251	\includegraphics[width=\columnwidth]{fig_gate_profile_crossmodel.pdf}
252	\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}
253	\label{fig:gate-crossmodel}
254	\end{figure}
255	
256	\subsection{Per-Turn AR GAR Decay}
257	
258	Figure~\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\% from turn 1 to turn 10; Llama base drops 90\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\ref{tab:four-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.
259	
260	\begin{figure}[h]
261	\centering
262	\includegraphics[width=\columnwidth]{fig_ar_gar_perturn.pdf}
263	\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\% (turn 1$\to$10), Llama base drops 90\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}
264	\label{fig:ar-gar-perturn}
265	\end{figure}
266	
267	\subsection{Bootstrap Confidence Intervals}
268	
269	Figure~\ref{fig:bootstrap-ci} shows the bootstrap resampling distributions underlying the 95\% CIs reported in Table~\ref{tab:four-way}.
270	
271	\begin{figure}[h]
272	  \centering
273	  \includegraphics[width=\columnwidth]{fig_bootstrap_ci.pdf}
274	  \caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\ LoRA-only, $N$\,=\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\,=\,0.454).}
275	  \label{fig:bootstrap-ci}
276	\end{figure}
277	
278	\subsection{Gate Value Distributions}
279	
280	Figure~\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.
281	
282	\begin{figure}[h]
283	\centering
284	\includegraphics[width=\columnwidth]{fig_gate_distribution.pdf}
285	\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}
286	\label{fig:gate-distribution}
287	\end{figure}
288	
289	\subsection{Training Loss Curves}
290	
291	Figure~\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.
292	
293	\begin{figure}[h]
294	\centering
295	\includegraphics[width=\columnwidth]{fig_training_loss_curves.pdf}
296	\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}
297	\label{fig:training-loss}
298	\end{figure}
299	
300	\subsection{Full Attention Steering Results}\label{sec:appendix-steering}
301	
302	\begin{table*}[t]
303	\centering\small
304	\caption{Full attention steering results across evaluation settings.
305	\textbf{Bold} indicates the operating point cited in the main text ($\beta$\,=\,5).
306	A visual gap separates the phase-transition boundary: GAR jumps sharply between $\beta$\,=\,2 and $\beta$\,=\,3 across all settings.}
307	\label{tab:steering-full}
308	\begin{tabular}{r cc cc cc}
309	\toprule
310	 & \multicolumn{2}{c}{\textbf{$N$\,=\,5, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,50, Gen}} & \multicolumn{2}{c}{\textbf{$N$\,=\,200, TF}} \\
311	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}
312	$\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\
313	\midrule
314	0   & .028 & 1.41 & $.064 \pm .081$ & $1.43 \pm .10$ & .535 & 2.62 \\
315	0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\
316	1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\
317	2   & .062 & 1.41 & $.128 \pm .110$ & $1.48 \pm .14$ & .611 & 2.69 \\
318	\addlinespace[3pt]
319	3   & ---  & ---  & $.556 \pm .060$ & $1.56 \pm .17$ & .788 & 2.93 \\
320	4   & ---  & ---  & $.644 \pm .061$ & $1.67 \pm .22$ & .817 & 3.49 \\
321	\textbf{5}  & \textbf{.680} & \textbf{1.91} & $\mathbf{.727 \pm .061}$ & $\mathbf{1.77 \pm .27}$ & \textbf{.833} & \textbf{6.15} \\
322	10  & .959 & 4.22 & $.961 \pm .015$ & $3.45 \pm 1.78$ & .977 & 505.2 \\
323	\bottomrule
324	\end{tabular}
325	\end{table*}
326	
327	\begin{figure}[h]
328	  \centering
329	  \includegraphics[width=\columnwidth]{fig_steering_standalone.pdf}
330	  \caption{Detailed $\beta$-steering trade-off ($N$\,=\,50). GAR-ours (top) increases monotonically with $\beta$; PPL (bottom) remains stable below $\beta$\,=\,3 (9\% cost), then rises sharply. The $\beta$\,=\,3 operating point (circled) achieves 8.7$\times$ GAR recovery while crossing the TF baseline, representing the optimal trade-off.}
331	  \label{fig:steering-standalone}
332	\end{figure}
333	
334	\section{Per-Layer Gate Profile}\label{sec:appendix-gate-profile}
335	
336	Table~\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\sigma$\,=\,0.051).
337	
338	\begin{table}[h]
339	\centering\small
340	\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}
341	\label{tab:gate-profile}
342	\resizebox{\columnwidth}{!}{%
343	\begin{tabular}{cccccccc}
344	\toprule
345	L0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\
346	.883 & \textbf{.793} & .996 & .988 & .984 & \textbf{.797} & .961 & .918 \\
347	\midrule
348	L8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\
349	.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\
350	\midrule
351	L16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\
352	.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\
353	\midrule
354	L24 & L25 & L26 & L27 & \multicolumn{4}{c}{Summary} \\
355	.980 & .984 & .988 & 1.00 & \multicolumn{4}{c}{$\bar{g}$\,=\,.947, $\sigma$\,=\,.051} \\
356	\bottomrule
357	\end{tabular}}
358	\end{table}
359	
360	The gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.
361	
362	\paragraph{Cross-model comparison.} See \S\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.
363	
364	\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
365	
366	Our scheduled sampling implementation follows \citet{bengio2015scheduled} with modifications for multi-turn transformer training:
367	
368	\paragraph{Sampling schedule.} The model-generated context ratio $\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\%) is lower than the nominal schedule due to per-sample Bernoulli variance.
369	
370	\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.
371	
372	\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing (Figure~\ref{fig:ss-dynamics}). Gate profiles remain similar (mean 0.953 vs.\ 0.947, min at L4 vs.\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42), 10.8h (seed 123), and 6.5h (seed 456) vs.\ 6.0h for standard ThreadGate on Qwen. Seed 456 exhibits consistent training dynamics with seeds 42 and 123.
373	
374	\begin{figure}[h]
375	  \centering
376	  \includegraphics[width=\columnwidth]{fig_ss_training_dynamics.pdf}
377	  \caption{Scheduled sampling training dynamics: sampling ratio $\rho$ ramps linearly from 0 to 0.3 (left axis); GAR loss (right axis) shows higher early-epoch variance due to stochastic context mixing.}
378	  \label{fig:ss-dynamics}
379	\end{figure}
380	
381	\section{Computational Cost Analysis}\label{sec:appendix-cost}
382	
383	\begin{table}[h]
384	\centering\small
385	\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\,GB VRAM).}
386	\label{tab:cost}
387	\resizebox{\columnwidth}{!}{%
388	\begin{tabular}{lcccc}
389	\toprule
390	\textbf{Config} & \textbf{Params} & \textbf{Time (h)} & \textbf{VRAM} & \textbf{Overhead} \\
391	\midrule
392	\multicolumn{5}{l}{\emph{Qwen-2.5-7B-Instruct}} \\
393	LoRA-only & 4.2M & 6.0 & 42\,GB & baseline \\
394	ThreadGate & 4.3M & 6.0 & 43\,GB & $+$57K \\
395	\;+\,PCGrad & 4.3M & 8.0 & 43\,GB & $+$33\% \\
396	Uniform Gate & 4.3M & 6.0 & 43\,GB & $+$57K \\
397	SS (s42) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
398	SS (s123) & 4.3M & 10.8 & 43\,GB & $+$80\% \\
399	SS (s456) & 4.3M & 6.5 & 43\,GB & $+$8\% \\
400	\midrule
401	\multicolumn{5}{l}{\emph{Llama-3.1-8B-Instruct}} \\
402	LoRA-only & 4.2M & 7.0 & 45\,GB & baseline \\
403	ThreadGate & 4.3M & 7.3 & 46\,GB & $+$65K \\
404	\bottomrule
405	\end{tabular}}
406	\end{table}
407	
408	\paragraph{Parameter overhead.} ThreadGate adds ${\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\times$ 2K per gate MLP) and ${\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.
409	
410	\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\sim}$33\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\% (6.5h) due to efficient batched generation, while seed 123 adds 80\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.
411	
412	\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\to$64$\to$1 MLP forward pass per layer adds $<$0.1\% latency. $\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.
413	
414	\section{Qualitative Steering Examples}\label{sec:appendix-examples}
415	
416	Table~\ref{tab:examples} illustrates the effect of $\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''
417	
418	\begin{table*}[h]
419	\centering\small
420	\caption{Qualitative effect of $\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}
421	\label{tab:examples}
422	\begin{tabular}{c p{5.5cm} p{5.5cm}}
423	\toprule
424	\textbf{Turn} & \textbf{$\beta$\,=\,0 (unsteered)} & \textbf{$\beta$\,=\,3 (steered)} \\
425	\midrule
426	1 & \checkmark~Three bullet points, on-topic & \checkmark~Three bullet points, on-topic \\
427	2 & \checkmark~Three bullet points, relevant & \checkmark~Three bullet points, relevant \\
428	3 & $\sim$~Four bullet points, partially on-topic & \checkmark~Three bullet points, on-topic \\
429	4 & \texttimes~Free-form paragraph, no bullets & \checkmark~Three bullet points, on-topic \\
430	\bottomrule
431	\end{tabular}
432	\end{table*}
433	
434	The pattern is consistent with the GAR decay analysis (\S\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\ref{tab:ir-results} shows that content constraints benefit most from this effect.
435	
436	\section{Gradient Conflict Analysis}\label{sec:appendix-gradient}
437	
438	\begin{figure}[t]
439	  \centering
440	  \includegraphics[width=\columnwidth,height=0.42\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}
441	  \caption{(a)~Training GAR convergence to target ($\tau$\,=\,0.5). (b)~PCGrad removes gradient conflict but $\mathcal{L}_\text{GAR}$ still collapses, confirming that gradient conflict is not the cause (\S\ref{subsec:pcgrad}).}
442	  \label{fig:training-pcgrad}
443	\end{figure}
444	
445	This section provides extended gradient interaction analysis supporting the PCGrad exclusion argument in \S\ref{subsec:pcgrad}. We measure per-layer cosine similarity between NTP and GAR gradients, gradient magnitude ratios, and the effect of PCGrad projection on these quantities.
446	
447	\paragraph{Gradient direction analysis.} Figure~\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate and PCGrad training. Under standard training, 79\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---as GAR loss approaches zero, the GAR gradient shrinks proportionally, making cosine similarity measurements less reliable (small gradients produce noisy direction estimates). Under PCGrad training, the conflict percentage decreases more slowly (79\%$\to$71\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane but not eliminating the underlying gradient conflict.
448	
449	\paragraph{Spatial patterns.} The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\ref{fig:gate-heatmap}). This spatial correlation is not causal: removing gradient conflict via PCGrad does not improve AR GAR, and gates at high-conflict layers are not systematically different from gates at low-conflict layers (Spearman $\rho$\,=\,$-$0.12, $p$\,=\,0.54 between gate value and conflict magnitude).
450	
451	\paragraph{Magnitude dominance.} NTP gradient magnitude dominates GAR by 7.5$\times$ at epoch~0 and 14.7$\times$ by epoch~2, as GAR loss converges while NTP loss remains at $\sim$0.93. This growing dominance means that even when directions oppose, the effective update direction is determined almost entirely by NTP. PCGrad addresses gradient conflict but not magnitude dominance---it projects conflicting gradients onto the other's normal plane (changing direction) but preserves relative magnitudes. The 7.5--14.7$\times$ magnitude ratio means that even after PCGrad projection, GAR contributes $<$7\% of the effective update magnitude, explaining why PCGrad is ineffective.
452	
453	\paragraph{Cross-model consistency.} Table~\ref{tab:gradient-crossmodel} confirms the pattern on Llama-3.1-8B: gradients are near-orthogonal (mean cosine $+$0.005, essentially zero) rather than systematically conflicting, with 25.7$\times$ NTP dominance. The Llama result is particularly informative because it shows that even without systematic gradient conflict (53\% negative layers, near chance), the same TF-AR gap persists. This cross-model evidence strengthens the \textit{modus tollens} argument: if gradient conflict were the cause, it should be present on both architectures; it is absent on Llama, yet the gap persists; therefore gradient conflict is not the cause.
454	
455	\begin{figure*}[h]
456	\centering
457	\includegraphics[width=0.95\textwidth]{fig_gradient_conflict_heatmap.pdf}
458	\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\% to 68\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\%$\to$71\%) but does not improve AR GAR, ruling out gradient conflict as the cause (\S\ref{subsec:pcgrad}).}
459	\label{fig:gradient-heatmap}
460	\end{figure*}
461	
462	\section{Training Data Characteristics}\label{sec:appendix-data}
463	
464	All experiments use 8,000 multi-turn conversations sampled from the UltraChat \citep{ding2023ultrachat} training split. Table~\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\,=\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\,=\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\ref{sec:appendix-n5}).
465	
466	\begin{table}[h]
467	\centering\small
468	\caption{Training and evaluation data characteristics. All data from UltraChat \citep{ding2023ultrachat}.}
469	\label{tab:data-stats}
470	\begin{tabular}{lcc}
471	\toprule
472	\textbf{Property} & \textbf{Train} & \textbf{Eval (primary)} \\
473	\midrule
474	Conversations & 8,000 & 50 \\
475	Min user turns & 3 & 3 \\
476	Max sequence length & 2,048 & 2,048 \\
477	Source & UltraChat train & UltraChat train \\
478	Overlap & --- & non-overlapping \\
479	\bottomrule
480	\end{tabular}
481	\end{table}
482	
483	\section{Exposure Bias Scaling}\label{sec:appendix-eb-scaling}
484	
485	Figure~\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).
486	
487	\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.8$\times$) while PCGrad shows the largest (16.7$\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\sim}$1.3$\times$, the only variant approaching parity. The ordering of gap ratios (SS $\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\sim$27$\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\ 28 layers), which provides more layers for distributional drift to compound through.
488	
489	\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\,=\,50), ThreadGate's gap is 8$\times$; at 10 turns ($N$\,=\,5), it widens to 31$\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.
490	
491	\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\sim}$1.3$\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\ref{sec:appendix-steering-viz}).
492	
493	\begin{figure}[h]
494	\centering
495	\includegraphics[width=\columnwidth]{fig_eb_scaling.pdf}
496	\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\sim}$1.3$\times$) is the only variant near parity. Llama gaps ($\sim$27$\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\times$ (3.6 turns) to 31$\times$ (10 turns).}
497	\label{fig:eb-scaling}
498	\end{figure}
499	
500	\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0930769e-7fac-48ca-b103-eeb486fd2214",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "11e10c6a-b0d2-4c48-80de-a6cbdb0888f8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\\section{Training Configuration}\\label{sec:appendix-hyper}\n\nTable~\\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\\times$ learning rate multiplier and are initialized with bias 1.5 ($\\sigma(1.5) \\approx 0.82$); the gate MLP adds ${\\sim}$57K parameters per variant ($<$0.001\\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB VRAM), requiring 6--8 hours per variant.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\\dagger$ apply only to ThreadGate and its ablations.}\n\\label{tab:hyperparams}\n\\begin{tabular}{l@{\\hspace{8pt}}l}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\nBase model & Qwen-2.5-7B-Instruct \\\\\nLoRA rank / $\\alpha$ & 16 / 32 \\\\\nLoRA targets & \\texttt{q\\_proj}, \\texttt{v\\_proj} \\\\\nOptimizer & AdamW ($\\beta_1$\\!=\\!0.9, $\\beta_2$\\!=\\!0.999) \\\\\nLearning rate & $2 \\times 10^{-4}$ \\\\\nGate LR mult.$^\\dagger$ & $10\\times$ \\\\\nBatch / grad accum & 1 / 8 (eff.\\ 8) \\\\\nEpochs & 3 \\\\\nMax seq length & 2048 \\\\\nTraining data & 8K UltraChat convs \\\\\nSeed & 42 (+123 for TG, SS) \\\\\n$\\lambda_\\text{GAR}$/$\\lambda_\\text{div}$ & 1.0 / 1.0 \\\\\nGAR target $\\tau$ & 0.5 \\\\\nGate init bias$^\\dagger$ & 1.5 ($\\sigma\\!\\approx\\!0.82$) \\\\\nGate hidden dim$^\\dagger$ & 64 \\\\\nTurn embed dim$^\\dagger$ & 16 \\\\\nGPU & RTX PRO 6000 (96\\,GB) \\\\\nTraining time & 6--8 h / variant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Loss Formulation Search}\\label{sec:appendix-loss}\n\nThe final MSE + gate diversity loss (\\S\\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.\n\n\\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.\n\n\\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\\text{mean}(\\text{GAR})$). The unbounded objective rewards full pass-through ($g \\to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\\lambda$=2 (v3), gates froze within 100 steps; at $\\lambda$=10 (v3b), convergence to identity accelerated; at $\\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.\n\n\\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.\n\n\\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\\tau$ incurs the same penalty as GAR below $\\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\\mathcal{L}_\\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).\n\n\\begin{table*}[t]\n\\centering\\footnotesize\n\\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}\n\\label{tab:loss-iterations}\n\\begin{tabular}{l l l p{5.8cm} c c}\n\\toprule\n & \\textbf{Loss Family} & \\textbf{Status} & \\textbf{Failure Mechanism} & \\textbf{GAR} & \\textbf{PPL} \\\\\n\\midrule\nv1  & Cumulative            & \\texttimes~GAR loss $\\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\\\\nv2  & Cumulative + $\\varepsilon$ & \\texttimes~same trajectory & Numerical instability from cumulative product; $\\varepsilon$-stabilization insufficient & ---  & ---  \\\\\nv3  & Maximize ($\\lambda$=2)  & \\texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\\\\nv3b & Maximize ($\\lambda$=10) & \\texttimes~identity collapse   & Higher $\\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\\\\nv5  & Maximize ($\\lambda$=1)  & \\texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\\\\nv6  & Smooth saturation       & \\texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\\\\nv7  & MSE + gate div          & \\checkmark~\\textbf{converged}  & \\textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Instruction Retention Details}\\label{sec:appendix-ir}\n\nTo evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\\beta$\\,=\\,3 steering on $N$\\,=\\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.\n\n\\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\\,=\\,54 paired evaluations (18 types $\\times$ 3 conversations per type) for the McNemar analysis.\n\n\\paragraph{Per-category results.} Table~\\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.\n\n\\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\\,=\\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.\n\nFigure~\\ref{fig:ir-bar} visualizes the per-category breakdown.\n\n\\begin{figure}[h]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_instruction_retention.pdf}\n  \\caption{Instruction retention by constraint category under $\\beta$\\,=\\,3 steering. Content constraints benefit most (+23.8\\,pp); format and count constraints are unaffected.}\n  \\label{fig:ir-bar}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Instruction retention by constraint category ($\\beta$\\,=\\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}\n\\label{tab:ir-results}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Category} & $\\beta$\\,=\\,0 & $\\beta$\\,=\\,3 & $\\Delta$ \\\\\n\\midrule\nContent    & 61.9\\% & 85.7\\% & +23.8\\,pp \\\\\nPosition   & 66.7\\% & 73.3\\% & +6.7\\,pp \\\\\nCount      & 100\\%  & 100\\%  & 0 \\\\\nFormat     & 100\\%  & 100\\%  & 0 \\\\\n\\midrule\n\\textbf{Overall} & 75.9\\% & 87.0\\% & +11.1\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Long-Conversation AR Evaluation}\\label{sec:appendix-n5}\n\nThe main results (Table~\\ref{tab:four-way}) report AR GAR from $N$\\,=\\,50 held-out conversations with a mean of 3.6 user turns. Table~\\ref{tab:n5-ar} presents complementary results on $N$\\,=\\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.\n\n\\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\\times$ (0.064 vs.\\ 0.037 in the $N$\\,=\\,50 evaluation) to 0.64$\\times$ (0.016 vs.\\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\\,=\\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.\n\n\\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\\times$ of the base model's GAR, compared to 3.4$\\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.\n\n\\paragraph{Caveats.} The $N$\\,=\\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{AR GAR-ours on $N$\\,=\\,5 ten-turn conversations. The gating advantage observed in Table~\\ref{tab:four-way} ($N$\\,=\\,50, mean 3.6 turns) diminishes with conversation length.}\n\\label{tab:n5-ar}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Configuration} & \\textbf{AR GAR-O} & \\textbf{$\\Delta$ vs.\\ Table~\\ref{tab:four-way}} \\\\\n\\midrule\nBase & 0.012 & $-$0.007 \\\\\n\\midrule\nThreadGate & 0.016 & $-$0.048 \\\\\n\\;+\\,PCGrad & 0.015 & $-$0.015 \\\\\nUniform Gate & 0.015 & $-$0.018 \\\\\nLoRA-only & 0.025 & $-$0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Statistical Test Details}\\label{sec:appendix-stats}\n\nAll statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\\ref{tab:stat-tests} consolidates the full results.\n\n\\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\\ LoRA-only comparison ($p$\\,=\\,0.004, $r$\\,=\\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\\ +PCGrad comparison ($p$\\,=\\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.\n\n\\paragraph{Bootstrap confidence intervals.} The 95\\% CIs in Table~\\ref{tab:four-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.\n\n\\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \\sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \\leq r < 0.5$ is medium, and $r \\geq 0.5$ is large. The TG vs.\\ LoRA-only effect ($r$\\,=\\,0.454) is medium, and TG vs.\\ Base ($r$\\,=\\,0.802) is large.\n\n\\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \\leq 0.004$) survive this correction.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Consolidated statistical tests. All AR comparisons use $N$\\,=\\,50 conversations (39 with $\\geq$3 turns); gate conditioning uses 28 layers.}\n\\label{tab:stat-tests}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Test} & $p$ & $r$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{AR GAR-ours ($\\beta$\\,=\\,0)}} \\\\\nTG vs.\\ Base & Wilcoxon & $<$0.001 & 0.802 \\\\\nTG vs.\\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\\\\nTG vs.\\ +PCGrad & Wilcoxon & 0.002 & --- \\\\\nSS vs.\\ TG & Wilcoxon & $<$0.001 & 0.869 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Gate conditioning (28 layers)}} \\\\\nTurn 1 vs.\\ Turn 21 & Wilcoxon & $3.7\\!\\times\\!10^{-8}$ & 0.975 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Instruction retention}} \\\\\n$\\beta$\\,=\\,0 vs.\\ $\\beta$\\,=\\,3 & McNemar & 0.077 & --- \\\\\nGAR--compliance & Pearson & 0.007 & 0.200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Llama-3.1-8B Complete Results}\\label{sec:appendix-llama}\n\nTable~\\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \\S\\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.\n\n\\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\\ 0.50).\n\n\\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\\,=\\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\\% for ThreadGate (mean 0.043, std 0.100), and 5\\% of turn-level measurements exhibit sporadic attention spikes (GAR $\\geq$ 0.4). We therefore report both mean and median.\n\n\\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719, L24\\,=\\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\\times$ by median for Llama vs.\\ 8--17$\\times$ for Qwen).\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\\,=\\,50); AR: autoregressive ($N$\\,=\\,20 for Base/TG/LoRA-only, $N$\\,=\\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}\n\\label{tab:llama-full}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{TF}} & \\multicolumn{2}{c}{\\textbf{AR}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\\\\n\\midrule\nBase & 0.017 & 3.45 & 0.009 & 0.009 \\\\\nThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\\\\nLoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\\\\n\\textbf{SS} & 0.477 & 2.82 & \\textbf{0.166} & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_crossmodel.pdf}\n  \\caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\\times$ by median), exceeding Qwen's 8$\\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}\n  \\label{fig:crossmodel}\n\\end{figure}\n\n\\paragraph{Cross-model summary.} Table~\\ref{tab:crossmodel-detail} consolidates the cross-model comparison, showing TF GAR, AR GAR, PPL, and gap ratios side by side for both architectures. The consistent pattern---TF GAR $\\approx$ 0.5, AR GAR $\\ll$ 0.1, gap $\\geq$ 7.9$\\times$---across two architectures with different layer counts, attention head configurations, and pre-training corpora provides strong evidence that exposure bias is architecture-independent. Notably, Llama's larger gaps (27$\\times$ by median for TG; mean-based range 11.2--17.2$\\times$) compared to Qwen's (7.9--13.5$\\times$) may reflect its deeper architecture (32 vs.\\ 28 layers), which allows more layers for distributional drift to compound through.\n\n\\input{../artifacts/appendix_expansion/tab_crossmodel_detail.tex}\n\n\\paragraph{GAR-Dongre cross-model comparison.} GAR-Dongre shows negligible distribution shift on Llama (AR/TF ratio 1.002$\\times$), compared to 1.28$\\times$ on Qwen. This confirms the mechanism specificity finding: exposure bias selectively disrupts the concentrated last-token attention pattern (GAR-ours) while leaving the diffuse all-token attention (GAR-Dongre) unaffected across both architectures.\n\n\\paragraph{Training details.} Llama variants used the same pipeline as Qwen: 8K UltraChat conversations, LoRA rank 16 targeting $q$/$v$ projections, 3 epochs. Training loss converged to 0.929 (LoRA-only) and 0.934 (ThreadGate); the slight difference is attributable to the additional GAR loss component. Wall-clock time was 7.0h (LoRA-only) and 7.3h (ThreadGate), approximately 17\\% longer than Qwen due to Llama's larger layer count (32 vs.\\ 28 layers).\n\n\\paragraph{Phase 1 diagnostics.} Before fine-tuning, we confirmed that Llama exhibits the same goal attention decay as Qwen. Base model GAR decays from 0.026 (turn 1) to 0.003 (turn 10), a 90\\% decline. This is steeper than Qwen's 70.8\\% decline, suggesting that attention decay may be more severe in Llama's architecture despite its larger head count (32 vs.\\ 28 KV heads).\n\n\\paragraph{Cross-model gradient analysis.} Table~\\ref{tab:gradient-crossmodel} compares NTP--GAR gradient interaction between the two architectures. Both models exhibit near-orthogonal gradients (cosine similarity $\\approx$\\,0), not systematic conflict: Qwen shows a slight negative mean ($-$0.042) while Llama is marginally positive (+0.005). NTP gradients dominate GAR by 14.7$\\times$ on Qwen and 25.7$\\times$ on Llama, indicating that the auxiliary signal is overwhelmed by magnitude rather than opposed by direction. The cross-model consistency---near-zero cosine similarity and order-of-magnitude NTP dominance on both architectures---reinforces the \\emph{modus tollens} argument (\\S\\ref{subsec:pcgrad}): gradient direction conflict is not the primary cause of the TF-AR gap.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Cross-model NTP--GAR gradient interaction. Gradients are near-orthogonal on both architectures; NTP magnitude dominates GAR by 15--26$\\times$.}\n\\label{tab:gradient-crossmodel}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-7B} & \\textbf{Llama-8B} \\\\\n\\midrule\nMean cos sim & $-$0.042 & +0.005 \\\\\nNeg-layer \\% & 67.9\\% & 53.1\\% \\\\\nNTP/GAR mag ratio & 14.7$\\times$ & 25.7$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Additional Visualizations}\\label{sec:appendix-viz}\n\nThis section presents extended visualizations referenced in the main text. Each figure examines a different aspect of the gating behavior and its failure under autoregressive generation.\n\n\\subsection{Gate Profile Heatmap}\n\nFigure~\\ref{fig:gate-heatmap} shows the per-layer gate values across all training configurations for both Qwen-2.5-7B (28 layers) and Llama-3.1-8B (32 layers). The key observation is that early layers consistently receive the lowest gate values across all conditions, suggesting that these layers contribute more dispensable computations for the NTP objective. The pattern is remarkably consistent across ThreadGate, Uniform Gate, and PCGrad variants, indicating that gate-value allocation is driven primarily by the NTP loss landscape rather than the GAR auxiliary objective.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_profile_heatmap.pdf}\n\\caption{Per-layer gate values across training for Qwen-2.5-7B (28 layers $\\times$ 5 conditions) and Llama-3.1-8B (32 layers $\\times$ 1 condition). Early layers (L1, L4--5) consistently receive the lowest gate values across conditions.}\n\\label{fig:gate-heatmap}\n\\end{figure}\n\n\\subsection{Cross-Model Gate Profile Comparison}\n\nFigure~\\ref{fig:gate-crossmodel} compares gate profiles between the two architectures. Qwen-2.5-7B shows minimum gate values at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), suggesting these layers are most amenable to attenuation without disrupting NTP. Llama-3.1-8B instead shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719), indicating that architecturally distinct models learn different layer-importance hierarchies. Both profiles converge toward identity at their respective final layers, consistent with NTP gradient pressure dominating gate optimization at output-adjacent layers.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_profile_crossmodel.pdf}\n\\caption{Side-by-side gate profiles for Qwen-2.5-7B and Llama-3.1-8B. Qwen dips at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719). Both models learn layer-selective gating but with architecture-dependent patterns.}\n\\label{fig:gate-crossmodel}\n\\end{figure}\n\n\\subsection{Per-Turn AR GAR Decay}\n\nFigure~\\ref{fig:ar-gar-perturn} visualizes the monotonic decay of GAR across conversation turns under autoregressive generation. Qwen base drops 85\\% from turn 1 to turn 10; Llama base drops 90\\%. The ThreadGate-trained model shows slight elevation in absolute GAR values but follows the same decay pattern, confirming that training-time GAR optimization does not alter the fundamental decay dynamic during generation. This per-turn view complements the aggregate TF-AR gap reported in Table~\\ref{tab:four-way}: the gap is not a fixed offset but grows with conversation length, consistent with cumulative exposure bias.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_ar_gar_perturn.pdf}\n\\caption{GAR decays monotonically across turns under autoregressive generation. Qwen base drops 85\\% (turn 1$\\to$10), Llama base drops 90\\%. The ThreadGate-trained model (AR) shows slight elevation but the same decay pattern, confirming that training-time GAR optimization does not transfer to generation.}\n\\label{fig:ar-gar-perturn}\n\\end{figure}\n\n\\subsection{Bootstrap Confidence Intervals}\n\nFigure~\\ref{fig:bootstrap-ci} shows the bootstrap resampling distributions underlying the 95\\% CIs reported in Table~\\ref{tab:four-way}.\n\n\\begin{figure}[h]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_bootstrap_ci.pdf}\n  \\caption{Bootstrap CI distributions for AR GAR-ours (ThreadGate vs.\\ LoRA-only, $N$\\,=\\,50, 10K resamples). Distributions overlap substantially, consistent with the modest effect size ($r$\\,=\\,0.454).}\n  \\label{fig:bootstrap-ci}\n\\end{figure}\n\n\\subsection{Gate Value Distributions}\n\nFigure~\\ref{fig:gate-distribution} shows the full distribution of per-layer gate values for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96, concentrated between 0.9 and 1.0), confirming that the gating mechanism provides minimal modulation regardless of the specific variant. The distributions are right-skewed with a sharp cutoff at 1.0, reflecting NTP pressure pushing gates toward identity.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_gate_distribution.pdf}\n\\caption{Per-layer gate value distributions for ThreadGate, Uniform Gate, and PCGrad variants. All three converge to similar distributions (mean $\\sim$0.94--0.96), confirming minimal modulation from the gating mechanism.}\n\\label{fig:gate-distribution}\n\\end{figure}\n\n\\subsection{Training Loss Curves}\n\nFigure~\\ref{fig:training-loss} shows the NTP, GAR, and total loss trajectories during training. GAR loss collapses to near-zero within the first epoch across all variants, indicating rapid convergence of the auxiliary objective under teacher forcing. NTP loss converges normally to ${\\sim}$0.93 by epoch 3. The fast GAR convergence is not itself pathological---it indicates successful optimization under the training distribution. The pathology emerges only at the transition to autoregressive generation, where the learned attention patterns fail to transfer.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_training_loss_curves.pdf}\n\\caption{NTP, GAR, and total loss trajectories. GAR loss collapses to near-zero within the first epoch across all variants, while NTP loss converges normally.}\n\\label{fig:training-loss}\n\\end{figure}\n\n\\subsection{Full Attention Steering Results}\\label{sec:appendix-steering}\n\n\\begin{table*}[t]\n\\centering\\small\n\\caption{Full attention steering results across evaluation settings.\n\\textbf{Bold} indicates the operating point cited in the main text ($\\beta$\\,=\\,5).\nA visual gap separates the phase-transition boundary: GAR jumps sharply between $\\beta$\\,=\\,2 and $\\beta$\\,=\\,3 across all settings.}\n\\label{tab:steering-full}\n\\begin{tabular}{r cc cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,5, Gen}} & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,50, Gen}} & \\multicolumn{2}{c}{\\textbf{$N$\\,=\\,200, TF}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n$\\beta$ & GAR & PPL & GAR & PPL & GAR & PPL \\\\\n\\midrule\n0   & .028 & 1.41 & $.064 \\pm .081$ & $1.43 \\pm .10$ & .535 & 2.62 \\\\\n0.5 & .029 & 1.39 & ---             & ---             & ---  & ---  \\\\\n1   & .035 & 1.36 & ---             & ---             & ---  & ---  \\\\\n2   & .062 & 1.41 & $.128 \\pm .110$ & $1.48 \\pm .14$ & .611 & 2.69 \\\\\n\\addlinespace[3pt]\n3   & ---  & ---  & $.556 \\pm .060$ & $1.56 \\pm .17$ & .788 & 2.93 \\\\\n4   & ---  & ---  & $.644 \\pm .061$ & $1.67 \\pm .22$ & .817 & 3.49 \\\\\n\\textbf{5}  & \\textbf{.680} & \\textbf{1.91} & $\\mathbf{.727 \\pm .061}$ & $\\mathbf{1.77 \\pm .27}$ & \\textbf{.833} & \\textbf{6.15} \\\\\n10  & .959 & 4.22 & $.961 \\pm .015$ & $3.45 \\pm 1.78$ & .977 & 505.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[h]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_steering_standalone.pdf}\n  \\caption{Detailed $\\beta$-steering trade-off ($N$\\,=\\,50). GAR-ours (top) increases monotonically with $\\beta$; PPL (bottom) remains stable below $\\beta$\\,=\\,3 (9\\% cost), then rises sharply. The $\\beta$\\,=\\,3 operating point (circled) achieves 8.7$\\times$ GAR recovery while crossing the TF baseline, representing the optimal trade-off.}\n  \\label{fig:steering-standalone}\n\\end{figure}\n\n\\section{Per-Layer Gate Profile}\\label{sec:appendix-gate-profile}\n\nTable~\\ref{tab:gate-profile} reports the final per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct (28 layers). Gate values are averaged across all tokens in the evaluation set. Layers 1 and 5 show the lowest gate values (0.793 and 0.797), indicating these layers are most amenable to attenuation without disrupting NTP. Layers 26--27 converge to $\\geq$0.988, consistent with NTP gradient pressure dominating at output-adjacent layers. The mean across all layers is 0.947 ($\\sigma$\\,=\\,0.051).\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Per-layer gate values for ThreadGate (seed 123) on Qwen-2.5-7B-Instruct. Min values (L1, L5) in bold.}\n\\label{tab:gate-profile}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{cccccccc}\n\\toprule\nL0 & L1 & L2 & L3 & L4 & L5 & L6 & L7 \\\\\n.883 & \\textbf{.793} & .996 & .988 & .984 & \\textbf{.797} & .961 & .918 \\\\\n\\midrule\nL8 & L9 & L10 & L11 & L12 & L13 & L14 & L15 \\\\\n.965 & .934 & .969 & .918 & .926 & .941 & .930 & .965 \\\\\n\\midrule\nL16 & L17 & L18 & L19 & L20 & L21 & L22 & L23 \\\\\n.941 & .910 & .961 & .965 & .973 & .988 & .969 & .980 \\\\\n\\midrule\nL24 & L25 & L26 & L27 & \\multicolumn{4}{c}{Summary} \\\\\n.980 & .984 & .988 & 1.00 & \\multicolumn{4}{c}{$\\bar{g}$\\,=\\,.947, $\\sigma$\\,=\\,.051} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe gate profile exhibits two notable patterns: (1)~a bimodal dip at L1 and L5, suggesting two distinct ``dispensable'' layer clusters in Qwen's architecture; (2)~monotonic increase from L17 to L27, indicating output-adjacent layers are progressively more critical for NTP. Seed 42 produces a similar profile (mean 0.934, min at L3--L5), confirming the pattern is not seed-dependent.\n\n\\paragraph{Cross-model comparison.} See \\S\\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.\n\n\\section{Scheduled Sampling Implementation}\\label{sec:appendix-ss}\n\nOur scheduled sampling implementation follows \\citet{bengio2015scheduled} with modifications for multi-turn transformer training:\n\n\\paragraph{Sampling schedule.} The model-generated context ratio $\\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\\%) is lower than the nominal schedule due to per-sample Bernoulli variance.\n\n\\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.\n\n\\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing (Figure~\\ref{fig:ss-dynamics}). Gate profiles remain similar (mean 0.953 vs.\\ 0.947, min at L4 vs.\\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 42), 10.8h (seed 123), and 6.5h (seed 456) vs.\\ 6.0h for standard ThreadGate on Qwen. Seed 456 exhibits consistent training dynamics with seeds 42 and 123.\n\n\\begin{figure}[h]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_training_dynamics.pdf}\n  \\caption{Scheduled sampling training dynamics: sampling ratio $\\rho$ ramps linearly from 0 to 0.3 (left axis); GAR loss (right axis) shows higher early-epoch variance due to stochastic context mixing.}\n  \\label{fig:ss-dynamics}\n\\end{figure}\n\n\\section{Computational Cost Analysis}\\label{sec:appendix-cost}\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Computational cost across training configurations. All experiments use a single NVIDIA RTX PRO 6000 (96\\,GB VRAM).}\n\\label{tab:cost}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Config} & \\textbf{Params} & \\textbf{Time (h)} & \\textbf{VRAM} & \\textbf{Overhead} \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Qwen-2.5-7B-Instruct}} \\\\\nLoRA-only & 4.2M & 6.0 & 42\\,GB & baseline \\\\\nThreadGate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\n\\;+\\,PCGrad & 4.3M & 8.0 & 43\\,GB & $+$33\\% \\\\\nUniform Gate & 4.3M & 6.0 & 43\\,GB & $+$57K \\\\\nSS (s42) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\nSS (s123) & 4.3M & 10.8 & 43\\,GB & $+$80\\% \\\\\nSS (s456) & 4.3M & 6.5 & 43\\,GB & $+$8\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Llama-3.1-8B-Instruct}} \\\\\nLoRA-only & 4.2M & 7.0 & 45\\,GB & baseline \\\\\nThreadGate & 4.3M & 7.3 & 46\\,GB & $+$65K \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Parameter overhead.} ThreadGate adds ${\\sim}$57K gate parameters for Qwen-2.5-7B (28 layers $\\times$ 2K per gate MLP) and ${\\sim}$65K for Llama-3.1-8B (32 layers), representing $<$0.001\\% of the base model. LoRA adapters (rank 16, targeting $q$/$v$ projections) contribute 4.2M parameters across both architectures.\n\n\\paragraph{Training time.} Standard variants (ThreadGate, Uniform Gate, LoRA-only) train in 6.0--7.3 hours. PCGrad adds ${\\sim}$33\\% overhead due to the per-step gradient projection computation. Scheduled sampling overhead varies: seed 42 adds only 8\\% (6.5h) due to efficient batched generation, while seed 123 adds 80\\% (10.8h) because of a longer generation schedule. The difference is due to the extended AR generation schedule in the seed 123 variant.\n\n\\paragraph{Inference overhead.} Gate computation at inference time is negligible: a single 32$\\to$64$\\to$1 MLP forward pass per layer adds $<$0.1\\% latency. $\\beta$-steering requires identifying goal tokens (a one-time operation per conversation) and adding a constant bias to attention logits, with zero additional parameters.\n\n\\section{Qualitative Steering Examples}\\label{sec:appendix-examples}\n\nTable~\\ref{tab:examples} illustrates the effect of $\\beta$-steering on model behavior in a 4-turn conversation where the system prompt instructs ``Always respond in exactly three bullet points.''\n\n\\begin{table*}[h]\n\\centering\\small\n\\caption{Qualitative effect of $\\beta$-steering on instruction following across conversation turns. System prompt: ``Always respond in exactly three bullet points.'' ThreadGate checkpoint, 4-turn conversation.}\n\\label{tab:examples}\n\\begin{tabular}{c p{5.5cm} p{5.5cm}}\n\\toprule\n\\textbf{Turn} & \\textbf{$\\beta$\\,=\\,0 (unsteered)} & \\textbf{$\\beta$\\,=\\,3 (steered)} \\\\\n\\midrule\n1 & \\checkmark~Three bullet points, on-topic & \\checkmark~Three bullet points, on-topic \\\\\n2 & \\checkmark~Three bullet points, relevant & \\checkmark~Three bullet points, relevant \\\\\n3 & $\\sim$~Four bullet points, partially on-topic & \\checkmark~Three bullet points, on-topic \\\\\n4 & \\texttimes~Free-form paragraph, no bullets & \\checkmark~Three bullet points, on-topic \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\nThe pattern is consistent with the GAR decay analysis (\\S\\ref{sec:analysis}): unsteered models progressively lose attention to the system-prompt constraint, leading to format violations at later turns. Steering maintains goal-token attention, preserving instruction compliance. The per-category breakdown in Table~\\ref{tab:ir-results} shows that content constraints benefit most from this effect.\n\n\\section{Gradient Conflict Analysis}\\label{sec:appendix-gradient}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth,height=0.42\\textheight,keepaspectratio]{fig2_training_pcgrad.pdf}\n  \\caption{(a)~Training GAR convergence to target ($\\tau$\\,=\\,0.5). (b)~PCGrad removes gradient conflict but $\\mathcal{L}_\\text{GAR}$ still collapses, confirming that gradient conflict is not the cause (\\S\\ref{subsec:pcgrad}).}\n  \\label{fig:training-pcgrad}\n\\end{figure}\n\nThis section provides extended gradient interaction analysis supporting the PCGrad exclusion argument in \\S\\ref{subsec:pcgrad}. We measure per-layer cosine similarity between NTP and GAR gradients, gradient magnitude ratios, and the effect of PCGrad projection on these quantities.\n\n\\paragraph{Gradient direction analysis.} Figure~\\ref{fig:gradient-heatmap} visualizes the per-layer cosine similarity between NTP and GAR gradients across training epochs for both standard ThreadGate and PCGrad training. Under standard training, 79\\% of layers show negative cosine similarity (gradient conflict) at epoch~0, declining to 68\\% by epoch~2 as GAR loss converges to near-zero. This decline reflects diminishing GAR gradient magnitude rather than alignment improvement---as GAR loss approaches zero, the GAR gradient shrinks proportionally, making cosine similarity measurements less reliable (small gradients produce noisy direction estimates). Under PCGrad training, the conflict percentage decreases more slowly (79\\%$\\to$71\\%), consistent with PCGrad projecting conflicting gradients onto the other's normal plane but not eliminating the underlying gradient conflict.\n\n\\paragraph{Spatial patterns.} The early layers (L0--L5) and output-adjacent layers (L24--L27) show the strongest conflict, corresponding to the layers where gate values deviate most from identity (Figure~\\ref{fig:gate-heatmap}). This spatial correlation is not causal: removing gradient conflict via PCGrad does not improve AR GAR, and gates at high-conflict layers are not systematically different from gates at low-conflict layers (Spearman $\\rho$\\,=\\,$-$0.12, $p$\\,=\\,0.54 between gate value and conflict magnitude).\n\n\\paragraph{Magnitude dominance.} NTP gradient magnitude dominates GAR by 7.5$\\times$ at epoch~0 and 14.7$\\times$ by epoch~2, as GAR loss converges while NTP loss remains at $\\sim$0.93. This growing dominance means that even when directions oppose, the effective update direction is determined almost entirely by NTP. PCGrad addresses gradient conflict but not magnitude dominance---it projects conflicting gradients onto the other's normal plane (changing direction) but preserves relative magnitudes. The 7.5--14.7$\\times$ magnitude ratio means that even after PCGrad projection, GAR contributes $<$7\\% of the effective update magnitude, explaining why PCGrad is ineffective.\n\n\\paragraph{Cross-model consistency.} Table~\\ref{tab:gradient-crossmodel} confirms the pattern on Llama-3.1-8B: gradients are near-orthogonal (mean cosine $+$0.005, essentially zero) rather than systematically conflicting, with 25.7$\\times$ NTP dominance. The Llama result is particularly informative because it shows that even without systematic gradient conflict (53\\% negative layers, near chance), the same TF-AR gap persists. This cross-model evidence strengthens the \\textit{modus tollens} argument: if gradient conflict were the cause, it should be present on both architectures; it is absent on Llama, yet the gap persists; therefore gradient conflict is not the cause.\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{fig_gradient_conflict_heatmap.pdf}\n\\caption{Per-layer cosine similarity between NTP and GAR gradients across training epochs. (a)~Standard training: conflict decreases from 79\\% to 68\\% of layers as GAR loss vanishes. (b)~PCGrad training: projection reduces conflict more slowly (79\\%$\\to$71\\%) but does not improve AR GAR, ruling out gradient conflict as the cause (\\S\\ref{subsec:pcgrad}).}\n\\label{fig:gradient-heatmap}\n\\end{figure*}\n\n\\section{Training Data Characteristics}\\label{sec:appendix-data}\n\nAll experiments use 8,000 multi-turn conversations sampled from the UltraChat \\citep{ding2023ultrachat} training split. Table~\\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\\,=\\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\\,=\\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\\ref{sec:appendix-n5}).\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Training and evaluation data characteristics. All data from UltraChat \\citep{ding2023ultrachat}.}\n\\label{tab:data-stats}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Property} & \\textbf{Train} & \\textbf{Eval (primary)} \\\\\n\\midrule\nConversations & 8,000 & 50 \\\\\nMin user turns & 3 & 3 \\\\\nMax sequence length & 2,048 & 2,048 \\\\\nSource & UltraChat train & UltraChat train \\\\\nOverlap & --- & non-overlapping \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Exposure Bias Scaling}\\label{sec:appendix-eb-scaling}\n\nFigure~\\ref{fig:eb-scaling} quantifies two scaling dimensions of the exposure bias phenomenon: cross-variant gap ratios (panel~a) and length-dependent gap compounding (panel~b).\n\n\\paragraph{Cross-variant gaps.} On Qwen, ThreadGate achieves the smallest gap among standard variants (7.8$\\times$) while PCGrad shows the largest (16.7$\\times$, consistent with its counterproductive effect on AR GAR). Scheduled sampling reduces the gap to ${\\sim}$1.3$\\times$, the only variant approaching parity. The ordering of gap ratios (SS $\\ll$ TG $<$ LoRA $<$ UG $<$ PCGrad) differs from the ordering of TF GAR (all $\\approx$ 0.50), confirming that training-time optimization success does not predict inference-time robustness. On Llama, both ThreadGate and LoRA-only show $\\sim$27$\\times$ gaps (by median), larger than any Qwen variant. The consistently larger Llama gaps may reflect its deeper architecture (32 vs.\\ 28 layers), which provides more layers for distributional drift to compound through.\n\n\\paragraph{Length-dependent compounding.} Panel~(b) shows that the gap compounds with conversation length: at 3.6 mean turns ($N$\\,=\\,50), ThreadGate's gap is 8$\\times$; at 10 turns ($N$\\,=\\,5), it widens to 31$\\times$. The relationship is approximately linear in the number of turns on a log scale, suggesting that the per-turn drift contribution is roughly multiplicative. Extrapolating this trend suggests that at 20 turns the gap would exceed 100$\\times$, making any training-time attention signal essentially undetectable. This length dependence is consistent with cumulative distributional drift---each model-generated turn introduces additional divergence from the teacher-forced training distribution, and by turn~10 the accumulated drift overwhelms any gating signal.\n\n\\paragraph{Implications for deployment.} These scaling results have practical implications: (1)~for applications requiring sustained attention over many turns (e.g., long-form tutoring, multi-step reasoning), architectural modifications alone are insufficient---distributional robustification or inference-time intervention is necessary; (2)~the near-parity of scheduled sampling (${\\sim}$1.3$\\times$ gap) suggests that bridging the training-inference distribution gap is both necessary and sufficient for maintaining attention; (3)~the $\\beta$-steering approach provides a complementary inference-time solution, but its effectiveness also depends on conversation length (Appendix~\\ref{sec:appendix-steering-viz}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_eb_scaling.pdf}\n\\caption{Exposure bias scaling analysis. (a)~TF/AR gap ratio across training variants; scheduled sampling (SS, ${\\sim}$1.3$\\times$) is the only variant near parity. Llama gaps ($\\sim$27$\\times$) exceed all Qwen variants. (b)~Gap compounds with conversation length: ThreadGate's gap widens from 8$\\times$ (3.6 turns) to 31$\\times$ (10 turns).}\n\\label{fig:eb-scaling}\n\\end{figure}\n\n\\section{Per-Turn AR GAR Dynamics}\\label{sec:appendix-ar-gar-dynamics}",
      "numLines": 500,
      "startLine": 1,
      "totalLines": 847
    }
  },
  "sourceToolAssistantUUID": "0930769e-7fac-48ca-b103-eeb486fd2214",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1087_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 附录内容引用完整性检查  **任务：** 检查论文附录的所有内容是否在正文中都有准确、合理的引用，修复孤儿附录。  **Step 1：逐项盘点** 列出附录里每一个 section/subsection/table/figure/algorithm/proof/prompt。  **Step 2：逐项验证引用** 对每一项，在正文搜索是否有至少一句话指向…",
  "leafUuid": "11e10c6a-b0d2-4c48-80de-a6cbdb0888f8",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1088_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Tool call

_source line 1089 · 2026-05-25T09:06:16.731Z_

<details open><summary>🔧 Tool call — Read · `toolu_018PNha2gk5hQeN8vszfNTkb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "offset": 500,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11e10c6a-b0d2-4c48-80de-a6cbdb0888f8",
  "isSidechain": false,
  "requestId": "req_011CbP2BmBnjemw9SzSGbryB",
  "type": "assistant",
  "uuid": "a48c8332-6681-4294-914a-7ba222032c2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DRBQXQrw9BZqpSiPPXhGUY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15326,
      "cache_read_input_tokens": 132879,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 132879,
          "cache_creation_input_tokens": 15326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15326
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

_source line 1090 · 2026-05-25T09:06:17.094Z_

<details><summary>↩ Tool result · `toolu_018PNha2gk5hQeN8vszfNTkb`</summary>

```text
500	\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}
501	
502	To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.
503	
504	All six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\ref{tab:four-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\S\ref{subsec:ss}).}
505	
506	\begin{figure}[t]
507	\centering
508	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_curves.pdf}
509	\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}
510	\label{fig:kl_ar_gar_curves}
511	\end{figure}
512	
513	\begin{figure}[t]
514	\centering
515	\includegraphics[width=\columnwidth]{fig_kl_ar_gar_bar.pdf}
516	\caption{Mid-turn AR GAR comparison across six training configurations. Ranking from highest to lowest: Scheduled Sampling (0.423), ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), Base (0.019).}
517	\label{fig:kl_ar_gar_bar}
518	\end{figure}
519	
520	This pattern contrasts with teacher-forced evaluation, where GAR remains relatively stable across turns for all configurations. Under teacher forcing, the model conditions on ground-truth context at each turn, preventing the distributional drift that causes GAR erosion in AR mode. The divergence between TF stability and AR decay provides turn-level evidence for the exposure bias mechanism described in \S\ref{sec:analysis}: training-time attention patterns are optimized for a distribution that AR generation progressively departs from.
521	
522	\section{Per-Head KL Divergence Analysis}\label{sec:appendix-kl}
523	
524	To test whether exposure bias selectively disrupts goal-attending heads rather than uniformly affecting all attention patterns, we compute per-head TF vs.\ AR attention divergence on 30 held-out conversations. For each of the 28 attention heads per layer (784 heads total), we measure the KL divergence $D_\text{KL}(p_\text{TF} \| p_\text{AR})$ between teacher-forced and autoregressive attention distributions, and the absolute GAR shift $\Delta\text{GAR} = |\text{GAR}_\text{TF} - \text{GAR}_\text{AR}|$. This head-level analysis provides diagnostic evidence for the exposure bias interpretation beyond the aggregate TF-AR gap.
525	
526	\begin{table}[h]
527	\centering\small
528	\caption{Per-head TF-AR divergence statistics for Base and ThreadGate (Qwen-2.5-7B, 30 conversations). TG trains more concentrated goal attention under TF, but these high-GAR heads shift most under AR ($r$\,=\,0.743).}
529	\label{tab:kl-perhead}
530	\begin{tabular}{lcc}
531	\toprule
532	\textbf{Metric} & \textbf{Base} & \textbf{TG} \\
533	\midrule
534	Mean $\Delta$GAR & 0.012 & 0.016 \\
535	Mean KL & 0.043 & 0.054 \\
536	Corr(TF\_GAR, $\Delta$GAR) & 0.673 & 0.743 \\
537	\bottomrule
538	\end{tabular}
539	\end{table}
540	
541	\paragraph{Selective disruption.} ThreadGate exhibits 35\% larger mean $\Delta$GAR (0.016 vs.\ 0.012) and 26\% larger mean KL (0.054 vs.\ 0.043) than Base. This is counterintuitive: the auxiliary GAR loss successfully trains more concentrated goal attention (higher TF GAR per head), but these very same heads shift more under AR generation. The correlation between per-head TF GAR and $\Delta$GAR is strong for both models ($r$\,=\,0.673 for Base, 0.743 for TG), confirming that heads with higher goal attention under teacher forcing are disproportionately disrupted under autoregressive generation. This selectivity is a hallmark of exposure bias: the training-time optimization succeeds at creating a specific attention pattern (concentrated goal attention), but precisely this pattern has no autoregressive counterpart because it depends on conditioning on ground-truth context.
542	
543	\paragraph{Layer-depth dependence.} The highest-KL heads concentrate at output-adjacent layers (L23--L27, KL\,$>$\,0.077) and L9 (KL\,$\approx$\,0.068). Output-adjacent layers participate most directly in next-token prediction, so their attention distributions are most sensitive to changes in the conditioning context. L9's elevated KL may reflect a ``routing layer'' phenomenon observed in multi-layer transformers, where specific intermediate layers specialize in long-range information routing. The depth dependence is consistent with cumulative error propagation: distributional drift from model-generated tokens accumulates as information flows through successive layers, producing the largest attention shifts at the deepest layers.
544	
545	\paragraph{Gate--KL independence.} Gate magnitude does not predict per-layer exposure bias severity: Spearman correlation between gate value and per-layer KL is 0.061 ($p$\,=\,0.757). The highest KL values concentrate at deep layers (L22--L27) where gates are near identity ($\approx$1.0), while the lowest-gate layers show below-average KL (0.041 vs.\ 0.056 for highest-gate layers). This independence confirms that the gating mechanism and the exposure bias phenomenon operate on different axes: gates modulate the magnitude of residual contributions, while exposure bias disrupts the direction (attention distribution) of those contributions. Even a ``perfect'' gate that could fully attenuate certain layers' residuals would not address the fundamental distributional mismatch that causes the attention shift.
546	
547	\section{GAR Definition Robustness}\label{sec:appendix-gar-robust}
548	
549	To assess whether our conclusions depend on the specific GAR definition, we evaluate four alternative token-position variants on 50 held-out conversations (Table~\ref{tab:gar-robust}): (1)~\emph{ours} (last-token): attention from the last token to goal tokens (standard GAR-ours); (2)~\emph{all-token}: average attention from all tokens to goal tokens; (3)~\emph{first-token}: attention from the first assistant token to goal tokens; (4)~\emph{goal-only}: attention from the last token to system-prompt-only tokens (excluding conversation content).
550	
551	\begin{table}[h]
552	\centering\small
553	\caption{Mid-turn GAR under four alternative definitions ($N$\,=\,50 conversations). ThreadGate only improves query-position-specific definitions (last-token, goal-only); Scheduled Sampling raises all four definitions above 0.36.}
554	\label{tab:gar-robust}
555	\begin{tabular}{lccc}
556	\toprule
557	\textbf{Definition} & \textbf{Base} & \textbf{TG} & \textbf{SS} \\
558	\midrule
559	Ours (last-token) & 0.015 & \textbf{0.325} & \textbf{0.458} \\
560	All-token & 0.015 & 0.025 & \textbf{0.366} \\
561	First-token & 0.022 & 0.039 & \textbf{0.412} \\
562	Goal-only & 0.005 & \textbf{0.310} & \textbf{0.444} \\
563	\bottomrule
564	\end{tabular}
565	\end{table}
566	
567	ThreadGate improvements are query-position-specific: the two definitions using the last token as query (ours: $0.015 \to 0.325$; goal-only: $0.005 \to 0.310$) show large gains, while all-token ($0.025$) and first-token ($0.039$) remain near base levels. This is expected: the GAR loss optimizes attention at the last-token position, so the learned routing does not generalize to other query positions.
568	
569	Scheduled Sampling raises all four definitions above 0.36, with no definition falling below Base-relative gains. This confirms that SS builds a broad goal-attention pattern across token positions, rather than overfitting to the specific position targeted by the GAR loss. The pattern holds regardless of GAR definition: both the exposure bias diagnosis and the SS mitigation are robust to metric choice.
570	
571	\section{General Capability Preservation (MMLU)}\label{sec:appendix-mmlu}
572	
573	To confirm that auxiliary GAR losses and attention steering do not degrade general language understanding, we evaluate all six Qwen-2.5-7B variants on MMLU 5-shot \citep{hendrycks2021measuring} ($N$\,=\,14{,}042 questions).
574	
575	\begin{table}[h]
576	\centering\small
577	\caption{MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct. All fine-tuned variants remain within 0.8\,pp of the base LoRA-only checkpoint.}
578	\label{tab:mmlu}
579	\begin{tabular}{lcc}
580	\toprule
581	\textbf{Model} & \textbf{Acc (\%)} & \textbf{$\Delta$ vs Base} \\
582	\midrule
583	Base (LoRA-only) & 74.23 & --- \\
584	PCGrad & 73.86 & $-$0.38 \\
585	SS & 73.75 & $-$0.48 \\
586	LoRA-only & 73.57 & $-$0.66 \\
587	ThreadGate & 73.47 & $-$0.77 \\
588	Uniform Gate & 73.46 & $-$0.78 \\
589	\bottomrule
590	\end{tabular}
591	\end{table}
592	
593	All variants degrade by $<$0.8\,pp, confirming that attention steering and auxiliary GAR losses do not harm general language understanding. The ordering does not track GAR performance (e.g., PCGrad shows the smallest MMLU drop despite the worst AR GAR), consistent with GAR and NTP occupying largely orthogonal subspaces.
594	
595	\section{Cross-Scale Validation (Qwen-2.5-1.5B)}\label{sec:appendix-1.5b}
596	
597	We validate cross-scale on Qwen-2.5-1.5B-Instruct to test whether goal attention decay and $\beta$-steering generalize to smaller models.
598	
599	\paragraph{Phase~1 GAR decay.} The 1.5B base model exhibits 79.8\% GAR decline from turn~1 to mid-turns (vs.\ 70.8\% on 7B), confirming that attention decay is present across scales and is more severe at smaller model sizes.
600	
601	\paragraph{Steering evaluation.} Table~\ref{tab:1.5b-steering} reports AR evaluation ($N$\,=\,50). We report median PPL because Base $\beta$\,=\,3 contains a catastrophic outlier (conversation~\#11, PPL\,$>$\,$10^8$) that inflates the mean.\footnote{The outlier occurs in a single conversation where $\beta$-steering causes the base model to enter a degenerate repetition loop. ThreadGate produces zero such outliers across all $\beta$ values, suggesting the gate provides stability against catastrophic steering failures.}
602	
603	\begin{table}[h]
604	\centering\small
605	\caption{Cross-scale $\beta$-steering on Qwen-2.5-1.5B ($N$\,=\,50, AR). PPL is median due to catastrophic Base outlier at $\beta$\,=\,3. TG eliminates outliers across all $\beta$ values.}
606	\label{tab:1.5b-steering}
607	\begin{tabular}{llcc}
608	\toprule
609	\textbf{Model} & $\beta$ & \textbf{AR GAR} & \textbf{PPL (med)} \\
610	\midrule
611	Base & 0 & 0.017 & 1.909 \\
612	TG & 0 & 0.023 & 1.897 \\
613	\midrule
614	Base & 3 & 0.120 & 2.216 \\
615	TG & 3 & 0.114 & 1.975 \\
616	\midrule
617	Base & 5 & 0.657 & 2.804 \\
618	TG & 5 & 0.715 & 2.624 \\
619	\bottomrule
620	\end{tabular}
621	\end{table}
622	
623	The steering pattern mirrors the 7B results: $\beta$\,=\,5 recovers GAR to 0.657--0.715 ($p < 0.001$), confirming that attention misallocation is the proximal cause of GAR collapse across scales. At $\beta$\,=\,0, TG shows a small but significant GAR advantage ($p$\,=\,0.005); at $\beta$\,=\,3, the TG--Base difference is not statistically significant ($p$\,=\,0.815), unlike the 7B pattern where TG consistently outperforms Base. This scale-specific difference may reflect the 1.5B model's limited capacity to maintain learned routing at intermediate steering strengths. ThreadGate does provide a stability advantage---zero catastrophic PPL outliers vs.\ one in Base---suggesting that residual gating regularizes attention distributions even when aggregate GAR is comparable.
624	
625	\section{Per-Seed Detailed Results}\label{sec:appendix-perseed}
626	
627	Tables~\ref{tab:perseed-ss} and~\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.
628	
629	\paragraph{Scheduled sampling (3 seeds).} TF GAR-ours averages $0.517\pm0.032$ across seeds under the held-out protocol (Table~\ref{tab:perseed-ss}); under IID evaluation, TF is more stable ($0.499\pm0.003$), with the held-out variance driven by seed~123's higher value on the larger $N$\,=\,200 sample. AR GAR shows meaningful variance (std\,=\,0.047): seed 42 produces the lowest AR GAR (0.347, gap 1.4$\times$), seed 123 is intermediate (0.423, gap 1.3$\times$), and seed 456 is highest (0.433, gap 1.2$\times$). This variance is expected: AR evaluation involves free-form generation where small differences in learned attention patterns can compound across turns. The variance is asymmetric---all seeds remain well above the non-SS baseline (0.064)---so the qualitative conclusion (SS provides order-of-magnitude improvement) holds across seeds. At $\beta$\,=\,5, the cross-seed variance nearly vanishes ($0.717\pm0.001$), confirming that strong steering converges to a seed-independent attention equilibrium that overwhelms initialization differences.
630	
631	\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\pm0.001$) and similar AR GAR (0.064 vs.\ 0.055), with gap ratios of 7.8$\times$ and 9.1$\times$ respectively. The 15\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.
632	
633	\paragraph{Training dynamics.} Seed variance in training time is non-trivial for scheduled sampling: seed 123 requires 10.8 hours (80\% overhead) vs.\ 6.5 hours for seeds 42 and 456 (8\% overhead). This variance is driven by the stochastic Bernoulli sampling of model-generated contexts: seed 123 happens to trigger longer autoregressive generation episodes early in training, where the model produces longer outputs before hitting the max-length cutoff. Despite this training-time variance, all three seeds converge to similar final metrics, suggesting the optimization landscape is robust.
634	
635	\input{../artifacts/appendix_expansion/tab_perseed_ss.tex}
636	
637	\input{../artifacts/appendix_expansion/tab_perseed_tg.tex}
638	
639	\section{Per-Turn GAR Decay Analysis}\label{sec:appendix-perturn-detail}
640	
641	Tables~\ref{tab:perturn-qwen} and~\ref{tab:perturn-llama} present per-turn AR GAR values for all configurations on both architectures, complementing the aggregate mid-turn GAR reported in the main text (Table~\ref{tab:four-way}).
642	
643	\paragraph{Qwen per-turn dynamics.} On Qwen (Table~\ref{tab:perturn-qwen}), all non-SS variants show rapid monotonic decay: turn-1 GAR ranges from 0.085 (Base) to 0.130 (ThreadGate), but by turn~5 all collapse below 0.07. The decay rate is approximately exponential for the first 3 turns, then plateaus near a floor value that varies by configuration (Base: 0.004, ThreadGate: 0.043--0.066, LoRA-only: 0.040). ThreadGate and LoRA-only show occasional turn-level fluctuations (e.g., TG turn~5 = 0.066 $>$ turn~4 = 0.043), which reflect stochastic variation in individual conversations rather than systematic recovery. Scheduled sampling retains substantially higher GAR throughout (turn-5 GAR\,=\,0.365 vs.\ 0.066 for ThreadGate), with a much flatter decay profile (15\% decline from turn~1 to turn~5 vs.\ 49\% for ThreadGate). This flatter profile is the signature of distributional robustification: SS-trained models encounter model-generated context during training, so the attention patterns are calibrated for the distribution they actually face during inference.
644	
645	\paragraph{Llama per-turn dynamics.} On Llama (Table~\ref{tab:perturn-llama}), the decay is steeper: Base GAR drops from 0.028 to 0.008 over 4 turns (71\% decline in the $N$\,=\,20 evaluation), and from 0.026 to 0.003 over 10 turns (88\% decline in the $N$\,=\,5 long-conversation evaluation). ThreadGate on Llama shows a distinctive pattern: turn-level GAR is roughly constant (0.038--0.049) rather than monotonically declining, suggesting that the gating mechanism maintains a stable floor on Llama that it fails to maintain on Qwen. However, this floor (0.04) is still an order of magnitude below the TF target (0.484), confirming that the fundamental TF-AR gap persists.
646	
647	\paragraph{Cross-architecture comparison.} The per-turn decay profiles reveal an architectural difference: Qwen shows a sharper initial decline (turn~1 to turn~2: $-$62\% for Base) followed by a plateau, while Llama shows a more gradual and sustained decline throughout. This difference may reflect the two architectures' different attention head configurations and layer counts, but the qualitative pattern---monotonic or near-monotonic decline toward a near-zero floor---is universal.
648	
649	Figures~\ref{fig:perturn-qwen-detail} and~\ref{fig:perturn-llama-detail} visualize these trajectories.
650	
651	\input{../artifacts/appendix_expansion/tab_perturn_qwen.tex}
652	
653	\begin{figure}[t]
654	  \centering
655	  \includegraphics[width=\columnwidth]{fig_perturn_qwen_detail.pdf}
656	  \caption{Per-turn AR GAR-ours across six Qwen-2.5-7B configurations. Scheduled sampling (green) retains far higher GAR than all other variants, which cluster below 0.13 and decay rapidly.}
657	  \label{fig:perturn-qwen-detail}
658	\end{figure}
659	
660	\input{../artifacts/appendix_expansion/tab_perturn_llama.tex}
661	
662	\begin{figure}[t]
663	  \centering
664	  \includegraphics[width=\columnwidth]{fig_perturn_llama_detail.pdf}
665	  \caption{Per-turn AR GAR decay on Llama-3.1-8B. (a)~Three-way comparison (Base, TG, LoRA-only; $N$\,=\,20, 4 turns). (b)~Extended Base decay profile ($N$\,=\,5, 10 turns), showing 90\% decline.}
666	  \label{fig:perturn-llama-detail}
667	\end{figure}
668	
669	\section{Extended Dataset Statistics}\label{sec:appendix-dataset-ext}
670	
671	Table~\ref{tab:dataset_stats} provides detailed statistics for the UltraChat training and evaluation splits. From the full UltraChat-200K corpus (207,865 conversations in the \texttt{train\_sft} split), we filter for conversations with $\geq$5 assistant turns, yielding 17,302 candidates (8.3\% of the full corpus). We randomly sample 8,000 for training, 50 for primary AR evaluation (mean 3.6 user turns), 50 for IID GAR diagnostics, and 200 for the instruction retention evaluation.
672	
673	\paragraph{Filtering rationale.} The $\geq$5 assistant turns threshold was chosen empirically: conversations with fewer than 3 assistant turns do not exhibit measurable attention decay (turn-1 to turn-3 GAR decline $<$5\%), making them uninformative for studying multi-turn exposure bias. The 5-turn threshold provides sufficient turn depth while retaining a reasonable fraction of the corpus. The average conversation in the filtered set contains 5.6 assistant turns (range: 5--7), with a mean sequence length of 1,247 tokens after tokenization with the Qwen-2.5 tokenizer.
674	
675	\paragraph{Evaluation split design.} We maintain four non-overlapping evaluation sets to avoid contamination: (1)~the primary AR evaluation ($N$\,=\,50) uses the same conversation structure as training but with held-out conversations, enabling direct comparison of TF vs.\ AR behavior; (2)~the IID GAR diagnostic ($N$\,=\,50) uses a separate sample for ablation studies that require independent measurements; (3)~the large instruction retention set ($N$\,=\,200) provides sufficient statistical power for per-category compliance analysis across 18 constraint types; (4)~the long-conversation set ($N$\,=\,5, 10 turns each) tests scaling behavior beyond the training distribution.
676	
677	\paragraph{Domain diversity.} UltraChat covers a broad range of conversational topics including knowledge Q\&A, creative writing, reasoning, and open-ended discussion. We do not stratify by topic, as our focus is on the architectural mechanism (attention routing) rather than domain-specific performance. The topic diversity serves as implicit regularization against overfitting to specific conversation patterns.
678	
679	\input{../artifacts/appendix_expansion/tab_dataset_stats.tex}
680	
681	\section{Extended GAR Robustness Analysis}\label{sec:appendix-gar-ext}
682	
683	Table~\ref{tab:gar_robustness} and Figure~\ref{fig:gar-robust-grouped} extend the GAR robustness analysis from \S\ref{sec:appendix-gar-robust} with turn-1 GAR and gap ratio metrics across all four token-position variants. We evaluate four ways to select the query token position for gradient attribution: (1)~\textit{Last} (our default): the final token of each assistant turn, which captures the model's ``summary'' attention pattern at the prediction boundary; (2)~\textit{All}: the mean over all assistant tokens, providing a position-averaged view; (3)~\textit{First}: the first assistant token, which reflects initial attention allocation; (4)~\textit{Goal-only}: attention to goal tokens as defined by \citet{dongre2026attention}, which restricts the target set to system-prompt tokens.
684	
685	\paragraph{Position-specific vs.\ broad improvement.} The key finding is a clear dichotomy between ThreadGate and Scheduled Sampling. ThreadGate improvements are restricted to last-token and goal-only positions (the two definitions sharing the query position targeted by the GAR loss): gap ratios drop to 1.21$\times$ and 1.07$\times$ respectively. All-token (5.04$\times$) and first-token (8.24$\times$) GAR remain near base levels, confirming that the learned routing is position-specific. Scheduled Sampling raises all four definitions above 0.36 with gap ratios $\leq$1.83$\times$, demonstrating that distributional robustification builds broad goal attention across token positions rather than overfitting to the position targeted by the loss.
686	
687	\paragraph{Turn-1 vs.\ mid-turn dynamics.} Turn-1 GAR is consistently higher than mid-turn GAR across all definitions and conditions, reflecting the first turn's proximity to the ground-truth prefix in training. The gap ratio quantifies how much of this initial attention survives into later turns. First-token GAR shows the largest gap ratios (Base: 13.3$\times$, TG: 8.2$\times$), indicating that the first-token position is most vulnerable to distributional drift---the initial token's attention pattern is highly dependent on the conditioning context, which diverges most from training under autoregressive generation.
688	
689	\input{../artifacts/appendix_expansion/tab_gar_robustness.tex}
690	
691	\begin{figure}[t]
692	  \centering
693	  \includegraphics[width=\columnwidth]{fig_gar_robustness_grouped.pdf}
694	  \caption{Mid-turn GAR across four token-position definitions. SS raises all four above 0.36; TG only improves last-token and goal-only.}
695	  \label{fig:gar-robust-grouped}
696	\end{figure}
697	
698	\section{MMLU Category Breakdown}\label{sec:appendix-mmlu-ext}
699	
700	Table~\ref{tab:mmlu_detail} breaks down MMLU 5-shot accuracy by category (STEM, Social Sciences, Humanities, Other) for all six Qwen-2.5-7B training configurations. This analysis addresses a potential concern: that auxiliary attention objectives might divert representational capacity from general language understanding, particularly in knowledge-intensive STEM domains.
701	
702	\paragraph{Per-category analysis.} The maximum per-category degradation is 1.2\,pp (ThreadGate on STEM), and no category shows systematic degradation across all variants. Notably, the ordering of variants differs across categories: ThreadGate shows the largest STEM drop but the smallest Humanities drop, while PCGrad shows the smallest overall drop despite having the worst AR GAR. This lack of correlation between GAR performance and MMLU degradation is consistent with GAR and NTP occupying largely orthogonal parameter subspaces---the LoRA adapter capacity (4.2M parameters) is sufficient to accommodate both objectives without interference.
703	
704	\paragraph{Statistical significance.} The per-category differences are small relative to the evaluation noise: with $N$\,=\,14,042 questions total ($\sim$3,500 per category), a 0.8\,pp accuracy difference corresponds to $\sim$28 questions, well within expected stochastic variation for 5-shot in-context learning. A chi-squared test comparing the best (PCGrad, 73.86\%) and worst (Uniform Gate, 73.46\%) variants yields $p$\,=\,0.503, confirming no significant difference. The category-level stability confirms that auxiliary GAR losses and gating do not selectively harm any knowledge domain.
705	
706	Figure~\ref{fig:mmlu-comparison} visualizes the per-category comparison, showing tight clustering across all variants within each category.
707	
708	\input{../artifacts/appendix_expansion/tab_mmlu_detail.tex}
709	
710	\begin{figure}[t]
711	  \centering
712	  \includegraphics[width=\columnwidth]{fig_mmlu_comparison.pdf}
713	  \caption{MMLU 5-shot accuracy by category across training configurations. All variants remain within 1.2\,pp of the LoRA-only baseline across all categories.}
714	  \label{fig:mmlu-comparison}
715	\end{figure}
716	
717	\section{Extended Cross-Scale Results (Qwen-2.5-1.5B)}\label{sec:appendix-1.5b-ext}
718	
719	Table~\ref{tab:qwen15b_results} extends the cross-scale analysis with Phase~1 GAR diagnostics, detailed Phase~2 training results, and $\beta$-steering evaluation on the Qwen-2.5-1.5B-Instruct model.
720	
721	\paragraph{Phase 1: GAR decay.} The 1.5B base model exhibits 79.8\% relative GAR decline from turn~1 to mid-turns, more severe than the 7B model's 70.8\% decline. This scale-dependent decay severity is consistent with smaller models having less redundant attention capacity: with 28 layers but only 1.5B parameters (vs.\ 7B), each layer carries proportionally more of the total representational burden, leaving less room for goal-oriented attention to persist alongside the primary NTP objective.
722	
723	\paragraph{Phase 2: Training.} ThreadGate training on 1.5B converges to TF GAR-ours of 0.498 with PPL of 2.67, closely matching the 7B results (0.504 / 2.78). The gate parameter count scales linearly with layer count (identical architecture, so ${\sim}$57K gate parameters). Training completes in 2.1 hours vs.\ 6.0 hours for 7B, reflecting the smaller model's reduced forward/backward pass cost.
724	
725	\paragraph{Steering evaluation.} At $\beta$\,=\,5, ThreadGate recovers GAR to 0.715 ($p < 0.001$), closely matching the 7B result (0.727). The recovery is essentially scale-independent at the strong steering regime: the attention bias added by $\beta$-steering overwhelms any capacity differences. At $\beta$\,=\,3, the picture differs: the TG--Base difference is not statistically significant ($p$\,=\,0.815) on 1.5B, unlike the significant difference on 7B ($p$\,=\,0.039). This scale-dependent response at intermediate $\beta$ may reflect the 1.5B model's reduced capacity for fine-grained attention routing: with fewer parameters per layer, the model cannot sustain the subtle attention reweighting that $\beta$\,=\,3 attempts.
726	
727	\paragraph{Catastrophic outliers.} Base 1.5B at $\beta$\,=\,3 produces one catastrophic PPL outlier (conversation \#11, PPL $> 10^8$) caused by a degenerate repetition loop. ThreadGate produces zero such outliers across all $\beta$ values, suggesting the gate provides a stabilizing effect on attention distributions even when aggregate GAR is comparable. We report median PPL to avoid this outlier dominating the central tendency estimate.
728	
729	\input{../artifacts/appendix_expansion/tab_qwen15b_results.tex}
730	
731	\section{Extended Statistical Analysis}\label{sec:appendix-stats-ext}
732	
733	Table~\ref{tab:statistical_tests} consolidates all statistical tests reported in this paper, including effect sizes, 95\% bootstrap confidence intervals, and significance levels. This section provides methodological detail beyond the summary in Appendix~\ref{sec:appendix-stats}.
734	
735	\paragraph{Test selection rationale.} All primary comparisons use paired Wilcoxon signed-rank tests on $N$\,=\,39 conversations (those with $\geq$3 turns from the 50-conversation held-out set). We use non-parametric tests because per-conversation GAR distributions are heavily right-skewed (skewness $>$ 2.0 for Base and PCGrad at $\beta$\,=\,0), violating normality assumptions required by parametric alternatives. The pairing structure (same conversations evaluated under different training configurations) controls for conversation-level confounds (topic difficulty, conversation length, system-prompt complexity).
736	
737	\paragraph{Effect size interpretation.} Effect sizes are computed as rank-biserial correlations ($r = Z / \sqrt{N}$), following standard practice. The largest effect is SS vs.\ TG ($r$\,=\,0.869, $p < 0.001$), a large effect by conventional thresholds ($r \geq 0.5$), confirming that scheduled sampling produces a qualitatively different outcome. The TG vs.\ Base effect ($r$\,=\,0.802) is also large, while TG vs.\ LoRA-only ($r$\,=\,0.454) is medium, reflecting the modest incremental benefit of gating over LoRA alone.
738	
739	\paragraph{Steering dose-response pattern.} At $\beta$\,=\,0, all four comparisons are significant ($p \leq 0.004$). At $\beta$\,=\,3 (the phase transition), TG vs.\ Base becomes marginally significant ($p$\,=\,0.039) and SS vs.\ TG remains significant ($p$\,=\,0.010), but TG vs.\ LoRA-only and PCGrad vs.\ TG lose significance ($p > 0.7$). At $\beta$\,=\,5, no pairwise comparison reaches significance---steering dominates and equalizes all variants. This dose-response pattern confirms that the training-time variant effects are real but small relative to the inference-time steering effect.
740	
741	\paragraph{Instruction retention.} The instruction retention analysis uses McNemar's test on $N$\,=\,54 paired constraint evaluations (18 constraint types $\times$ 3 conversations). The marginal significance ($p$\,=\,0.077) reflects the small sample size rather than a null effect: the point-biserial correlation ($r$\,=\,0.200, $p$\,=\,0.007) is significant when treating compliance as a continuous variable, and the per-category breakdown (Table~\ref{tab:ir-results}) shows a clear content-constraint improvement (+23.8\,pp).
742	
743	\paragraph{Multiple comparisons.} We report uncorrected $p$-values for the same reason described in Appendix~\ref{sec:appendix-stats}: comparisons are hypothesis-driven (each tests a specific causal exclusion in the analysis chain), not exploratory. All reported significant results ($p \leq 0.039$) survive Holm-Bonferroni correction for the 4 primary comparisons within each $\beta$ level.
744	
745	\input{../artifacts/appendix_expansion/tab_statistical_tests.tex}
746	
747	\section{Extended Training Dynamics}\label{sec:appendix-training-ext}
748	
749	Figure~\ref{fig:training-6panel} presents the complete training loss landscape for all five Qwen-2.5-7B conditions (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Scheduled Sampling) plus the base model, showing NTP loss, GAR loss, and total loss across three epochs.
750	
751	\paragraph{NTP loss convergence.} All fine-tuned variants converge to NTP loss ${\sim}$0.93 by epoch~3, with final-epoch values ranging from 0.929 (LoRA-only) to 0.934 (ThreadGate). PCGrad shows marginally higher variance due to gradient projection, but converges to the same terminal value. The uniformity of NTP convergence across variants---including those with auxiliary losses (ThreadGate, PCGrad) and those without (LoRA-only)---confirms that the GAR auxiliary objective does not interfere with the primary language modeling task during training.
752	
753	\paragraph{GAR loss dynamics.} GAR loss collapses to near-zero within the first epoch under teacher forcing across all variants, consistent with the auxiliary objective being easy to optimize when the model conditions on ground-truth context. This rapid convergence is a double-edged sword: while it confirms that the MSE formulation (v7) achieves stable optimization, the ease of convergence also means the model never learns to maintain attention under distributional drift. The scheduled sampling variant shows distinctive dynamics: higher initial GAR loss variance from stochastic context mixing, with occasional spikes when a particularly challenging model-generated context is sampled, followed by convergence to a similar final value.
754	
755	\paragraph{Training-inference disconnect.} The key observation is that training-time convergence is indistinguishable across variants: an observer with access only to training curves could not predict the 5.4$\times$ AR GAR difference between SS and TG. This disconnect reinforces the diagnosis that the failure occurs at the training-to-inference transition, not during optimization, and explains why architectural modifications (gating, PCGrad) that operate during training cannot address the fundamental distributional mismatch.
756	
757	\begin{figure*}[t]
758	  \centering
759	  \includegraphics[width=0.75\textwidth]{fig_training_curves_6panel.pdf}
760	  \caption{Training loss curves for all five Qwen conditions. NTP loss (left) converges to ${\sim}$0.93 across variants; GAR loss (center) collapses within epoch~1; total loss (right) is NTP-dominated. Training-time behavior is indistinguishable; the failure emerges only at inference.}
761	  \label{fig:training-6panel}
762	\end{figure*}
763	
764	\section{Per-$\beta$ Steering Visualization}\label{sec:appendix-steering-viz}
765	
766	Figure~\ref{fig:steering-4panel} visualizes per-turn GAR trajectories under four steering strengths ($\beta$\,=\,0, 3, 5, 10), revealing the turn-level dynamics that underlie the aggregate steering results in Table~\ref{tab:steering-full}.
767	
768	\paragraph{Unsteered baseline ($\beta$\,=\,0).} GAR decays monotonically from 0.12 to 0.02 over five turns, with the steepest decline between turns~1 and~2 ($-$44\%). This trajectory matches the per-turn profiles in Appendix~\ref{sec:appendix-perturn-detail} and confirms that the decay is a smooth, progressive phenomenon rather than a discrete failure at a specific turn.
769	
770	\paragraph{Phase transition ($\beta$\,=\,3).} Turn-1 GAR jumps to ${\sim}$0.55, but per-turn decay persists (${\sim}$15\% decline from turn~1 to turn~5). This indicates that steering partially compensates for the distributional drift but does not eliminate it: the attention bias adds a constant offset to goal-token logits, while the drift compounds multiplicatively across turns. The residual decay at $\beta$\,=\,3 explains why this operating point shows the strongest training-variant effects in the dose-response analysis (Appendix~\ref{sec:appendix-stats-ext}).
771	
772	\paragraph{Sustained recovery ($\beta$\,=\,5).} GAR is sustained above 0.6 throughout, with minimal per-turn decay ($<$5\% decline). At this steering strength, the constant attention bias dominates the per-turn drift, effectively replacing the lost training-time signal with an inference-time substitute. The 9\% PPL cost (1.43 $\to$ 1.77) is modest compared to the order-of-magnitude GAR recovery.
773	
774	\paragraph{Saturation regime ($\beta$\,=\,10).} GAR saturates near 1.0 across all turns but PPL degrades catastrophically ($>$3.5), as the excessive attention bias distorts the attention distribution beyond the model's capacity for coherent generation. This regime is impractical and serves as an upper bound on the steering approach.
775	
776	\paragraph{Operating region.} The region $\beta \in [3, 5]$ balances GAR recovery against PPL cost, and the per-turn profiles confirm that steering must counteract an ongoing distributional drift rather than a one-time initialization failure---a key diagnostic that distinguishes exposure bias from alternative hypotheses (e.g., capacity limitations or optimization failures).
777	
778	\begin{figure}[t]
779	  \centering
780	  \includegraphics[width=\columnwidth]{fig_steering_perturn_4panel.pdf}
781	  \caption{Per-turn GAR under four $\beta$-steering strengths. At $\beta$\,=\,0, monotonic decay; at $\beta$\,=\,3, partial recovery with residual decay; at $\beta$\,=\,5, sustained high GAR; at $\beta$\,=\,10, saturation with catastrophic PPL.}
782	  \label{fig:steering-4panel}
783	\end{figure}
784	
785	\section{Llama-3.1-8B Scheduled Sampling Details}\label{sec:appendix-llama-ss}
786	
787	Llama-3.1-8B-Instruct was trained with scheduled sampling using the same protocol as Qwen (\S\ref{sec:appendix-ss}), with one key difference: training was stopped at 2 epochs (${\sim}$14{,}400 steps) instead of 3, because Llama's per-step wall-clock time was ${\sim}$4$\times$ slower than Qwen on the same hardware (624 steps/h vs.\ ${\sim}$2{,}400 steps/h for Qwen). This is attributable to different vocabulary sizes (Llama 128K vs.\ Qwen 152K tokens) and attention implementation. The 2-epoch checkpoint was selected based on convergence of TF GAR (0.477, within 0.02 of Qwen's 3-epoch value 0.498).
788	
789	\paragraph{$\beta$-steering on Llama SS.}
790	Table~\ref{tab:llama-ss-steering} reports $\beta$-steering results on the Llama SS model. Unlike Qwen, $\beta$\,=\,3 does not trigger recovery on Llama (GAR 0.173 vs.\ 0.166 at $\beta$\,=\,0). At $\beta$\,=\,5, GAR reaches 0.791---higher than Qwen's 0.717---suggesting that Llama's attention distribution is more responsive to the additive bias at higher steering strengths, possibly because the lower baseline AR GAR leaves more headroom for steering to exploit.
791	
792	\begin{table}[h]
793	\centering\small
794	\caption{$\beta$-steering on Llama-3.1-8B SS model ($N$\,=\,50, $T$\,=\,4).}
795	\label{tab:llama-ss-steering}
796	\begin{tabular}{@{}l ccc@{}}
797	\toprule
798	& $\beta$\,=\,0 & $\beta$\,=\,3 & $\beta$\,=\,5 \\
799	\midrule
800	AR GAR & 0.166 & 0.173 & 0.791 \\
801	\bottomrule
802	\end{tabular}
803	\end{table}
804	
805	\paragraph{Cross-model comparison.}
806	Table~\ref{tab:llama-vs-qwen-ss} compares scheduled sampling across both architectures. Both models show large gap compression relative to their ThreadGate baselines, but the residual gap on Llama (2.9$\times$) is larger than Qwen's (1.2$\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\times$ (from 27$\times$ to 2.9$\times$) while Qwen reduces by 6.5$\times$ (from 7.8$\times$ to 1.2$\times$), suggesting that a third epoch would likely narrow the residual gap further. Notably, $\beta$-steering is more effective on Llama (0.791 vs.\ 0.717 at $\beta$\,=\,5), partially compensating for the weaker training-time compression.
807	
808	\paragraph{Architectural differences.}
809	Several architectural differences between Qwen-2.5-7B and Llama-3.1-8B may contribute to the cross-model gap variation. Llama uses Grouped Query Attention (GQA) with 8 KV heads (vs.\ Qwen's full 28-head multi-head attention, MHA), which reduces the number of independently steerable attention heads by 3.5$\times$. Llama also uses Rotary Position Embedding (RoPE) with a longer default context (128K tokens vs.\ Qwen's 32K), which may affect how positional information interacts with goal-token attention at different conversation depths. Despite these differences, the qualitative pattern is identical: TF convergence, AR collapse, and SS-mediated recovery, confirming that exposure bias on auxiliary attention losses is architecture-general rather than an artifact of a specific attention implementation.
810	
811	\paragraph{Training dynamics.}
812	The Llama SS training loss trajectory closely mirrors Qwen's during the first two epochs: NTP loss converges within epoch~1 (final NTP loss 0.62 for Llama vs.\ 0.58 for Qwen), while GAR loss continues to decrease throughout epoch~2. The scheduled sampling ratio reaches ${\sim}$0.20 at the end of epoch~2 (vs.\ 0.30 at end of epoch~3 for Qwen), meaning Llama was exposed to less model-generated context during training. This partial exposure is sufficient to achieve meaningful gap compression (27$\times$ $\to$ 2.9$\times$ by median) but leaves a larger residual gap than Qwen's full 3-epoch schedule.
813	
814	\begin{table}[h]
815	\centering\small
816	\caption{Scheduled sampling comparison: Qwen-2.5-7B vs.\ Llama-3.1-8B.}
817	\label{tab:llama-vs-qwen-ss}
818	\begin{tabular}{@{}l cc@{}}
819	\toprule
820	\textbf{Metric} & \textbf{Qwen-7B} & \textbf{Llama-8B} \\
821	\midrule
822	SS epochs & 3 & 2 \\
823	TF GAR & 0.498 & 0.477 \\
824	AR GAR ($\beta$\,=\,0) & 0.401 & 0.166 \\
825	TF/AR gap & 1.2$\times$ & 2.9$\times$ \\
826	Baseline TG gap & 7.8$\times$ & 27$\times$ (median) \\
827	Gap compression & 6.5$\times$ & 9.3$\times$ \\
828	AR GAR ($\beta$\,=\,5) & 0.717 & 0.791 \\
829	TF PPL & 2.78 & 2.82 \\
830	AR PPL & 1.441 & 1.370 \\
831	\bottomrule
832	\end{tabular}
833	\end{table}
834	
835	\section{Use of AI Assistants}\label{sec:appendix-ai}
836	
837	We used Claude (Anthropic) as an AI coding and writing assistant
838	throughout this work. Specifically:
839	\begin{itemize}
840	    \item \textbf{Code:} drafting experiment scripts, data-processing
841	    pipelines, and analysis utilities; debugging and refactoring.
842	    \item \textbf{Writing:} drafting and revising paper sections,
843	    polishing prose, and reformatting LaTeX.
844	    \item \textbf{Literature:} summarizing related papers to inform
845	    related-work section.
846	\end{itemize}
847	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a48c8332-6681-4294-914a-7ba222032c2c",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "01cd419f-e228-4dea-b9a5-93357869db71",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\\section{Per-Turn AR GAR Dynamics}\\label{sec:appendix-ar-gar-dynamics}\n\nTo characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.\n\nAll six configurations exhibit monotonic GAR decay as turn index increases, consistent with cumulative exposure bias eroding attention to goal tokens. The decay rate varies substantially: Scheduled Sampling retains by far the highest mid-turn GAR (0.423), followed distantly by ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), and Base (0.019). Base decays most rapidly, losing the majority of its initial GAR within the first few turns. The large SS--TG gap mirrors Table~\\ref{tab:four-way} and confirms that distributional robustification---not gating architecture alone---is the primary driver of AR GAR retention.\\footnote{SS configuration uses seed 123 data; all other configurations use seed 42. Cross-seed trends are consistent (\\S\\ref{subsec:ss}).}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_kl_ar_gar_curves.pdf}\n\\caption{Per-turn AR GAR trajectories for six Qwen-2.5-7B configurations (turns 1--5). All models show monotonic decay; Scheduled Sampling retains far higher GAR throughout (0.53$\\to$0.39), while the remaining five variants cluster below 0.13 and decay rapidly.}\n\\label{fig:kl_ar_gar_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_kl_ar_gar_bar.pdf}\n\\caption{Mid-turn AR GAR comparison across six training configurations. Ranking from highest to lowest: Scheduled Sampling (0.423), ThreadGate (0.064), LoRA-only (0.037), Uniform Gate (0.033), PCGrad (0.030), Base (0.019).}\n\\label{fig:kl_ar_gar_bar}\n\\end{figure}\n\nThis pattern contrasts with teacher-forced evaluation, where GAR remains relatively stable across turns for all configurations. Under teacher forcing, the model conditions on ground-truth context at each turn, preventing the distributional drift that causes GAR erosion in AR mode. The divergence between TF stability and AR decay provides turn-level evidence for the exposure bias mechanism described in \\S\\ref{sec:analysis}: training-time attention patterns are optimized for a distribution that AR generation progressively departs from.\n\n\\section{Per-Head KL Divergence Analysis}\\label{sec:appendix-kl}\n\nTo test whether exposure bias selectively disrupts goal-attending heads rather than uniformly affecting all attention patterns, we compute per-head TF vs.\\ AR attention divergence on 30 held-out conversations. For each of the 28 attention heads per layer (784 heads total), we measure the KL divergence $D_\\text{KL}(p_\\text{TF} \\| p_\\text{AR})$ between teacher-forced and autoregressive attention distributions, and the absolute GAR shift $\\Delta\\text{GAR} = |\\text{GAR}_\\text{TF} - \\text{GAR}_\\text{AR}|$. This head-level analysis provides diagnostic evidence for the exposure bias interpretation beyond the aggregate TF-AR gap.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Per-head TF-AR divergence statistics for Base and ThreadGate (Qwen-2.5-7B, 30 conversations). TG trains more concentrated goal attention under TF, but these high-GAR heads shift most under AR ($r$\\,=\\,0.743).}\n\\label{tab:kl-perhead}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{Base} & \\textbf{TG} \\\\\n\\midrule\nMean $\\Delta$GAR & 0.012 & 0.016 \\\\\nMean KL & 0.043 & 0.054 \\\\\nCorr(TF\\_GAR, $\\Delta$GAR) & 0.673 & 0.743 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Selective disruption.} ThreadGate exhibits 35\\% larger mean $\\Delta$GAR (0.016 vs.\\ 0.012) and 26\\% larger mean KL (0.054 vs.\\ 0.043) than Base. This is counterintuitive: the auxiliary GAR loss successfully trains more concentrated goal attention (higher TF GAR per head), but these very same heads shift more under AR generation. The correlation between per-head TF GAR and $\\Delta$GAR is strong for both models ($r$\\,=\\,0.673 for Base, 0.743 for TG), confirming that heads with higher goal attention under teacher forcing are disproportionately disrupted under autoregressive generation. This selectivity is a hallmark of exposure bias: the training-time optimization succeeds at creating a specific attention pattern (concentrated goal attention), but precisely this pattern has no autoregressive counterpart because it depends on conditioning on ground-truth context.\n\n\\paragraph{Layer-depth dependence.} The highest-KL heads concentrate at output-adjacent layers (L23--L27, KL\\,$>$\\,0.077) and L9 (KL\\,$\\approx$\\,0.068). Output-adjacent layers participate most directly in next-token prediction, so their attention distributions are most sensitive to changes in the conditioning context. L9's elevated KL may reflect a ``routing layer'' phenomenon observed in multi-layer transformers, where specific intermediate layers specialize in long-range information routing. The depth dependence is consistent with cumulative error propagation: distributional drift from model-generated tokens accumulates as information flows through successive layers, producing the largest attention shifts at the deepest layers.\n\n\\paragraph{Gate--KL independence.} Gate magnitude does not predict per-layer exposure bias severity: Spearman correlation between gate value and per-layer KL is 0.061 ($p$\\,=\\,0.757). The highest KL values concentrate at deep layers (L22--L27) where gates are near identity ($\\approx$1.0), while the lowest-gate layers show below-average KL (0.041 vs.\\ 0.056 for highest-gate layers). This independence confirms that the gating mechanism and the exposure bias phenomenon operate on different axes: gates modulate the magnitude of residual contributions, while exposure bias disrupts the direction (attention distribution) of those contributions. Even a ``perfect'' gate that could fully attenuate certain layers' residuals would not address the fundamental distributional mismatch that causes the attention shift.\n\n\\section{GAR Definition Robustness}\\label{sec:appendix-gar-robust}\n\nTo assess whether our conclusions depend on the specific GAR definition, we evaluate four alternative token-position variants on 50 held-out conversations (Table~\\ref{tab:gar-robust}): (1)~\\emph{ours} (last-token): attention from the last token to goal tokens (standard GAR-ours); (2)~\\emph{all-token}: average attention from all tokens to goal tokens; (3)~\\emph{first-token}: attention from the first assistant token to goal tokens; (4)~\\emph{goal-only}: attention from the last token to system-prompt-only tokens (excluding conversation content).\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Mid-turn GAR under four alternative definitions ($N$\\,=\\,50 conversations). ThreadGate only improves query-position-specific definitions (last-token, goal-only); Scheduled Sampling raises all four definitions above 0.36.}\n\\label{tab:gar-robust}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Definition} & \\textbf{Base} & \\textbf{TG} & \\textbf{SS} \\\\\n\\midrule\nOurs (last-token) & 0.015 & \\textbf{0.325} & \\textbf{0.458} \\\\\nAll-token & 0.015 & 0.025 & \\textbf{0.366} \\\\\nFirst-token & 0.022 & 0.039 & \\textbf{0.412} \\\\\nGoal-only & 0.005 & \\textbf{0.310} & \\textbf{0.444} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThreadGate improvements are query-position-specific: the two definitions using the last token as query (ours: $0.015 \\to 0.325$; goal-only: $0.005 \\to 0.310$) show large gains, while all-token ($0.025$) and first-token ($0.039$) remain near base levels. This is expected: the GAR loss optimizes attention at the last-token position, so the learned routing does not generalize to other query positions.\n\nScheduled Sampling raises all four definitions above 0.36, with no definition falling below Base-relative gains. This confirms that SS builds a broad goal-attention pattern across token positions, rather than overfitting to the specific position targeted by the GAR loss. The pattern holds regardless of GAR definition: both the exposure bias diagnosis and the SS mitigation are robust to metric choice.\n\n\\section{General Capability Preservation (MMLU)}\\label{sec:appendix-mmlu}\n\nTo confirm that auxiliary GAR losses and attention steering do not degrade general language understanding, we evaluate all six Qwen-2.5-7B variants on MMLU 5-shot \\citep{hendrycks2021measuring} ($N$\\,=\\,14{,}042 questions).\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct. All fine-tuned variants remain within 0.8\\,pp of the base LoRA-only checkpoint.}\n\\label{tab:mmlu}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Model} & \\textbf{Acc (\\%)} & \\textbf{$\\Delta$ vs Base} \\\\\n\\midrule\nBase (LoRA-only) & 74.23 & --- \\\\\nPCGrad & 73.86 & $-$0.38 \\\\\nSS & 73.75 & $-$0.48 \\\\\nLoRA-only & 73.57 & $-$0.66 \\\\\nThreadGate & 73.47 & $-$0.77 \\\\\nUniform Gate & 73.46 & $-$0.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll variants degrade by $<$0.8\\,pp, confirming that attention steering and auxiliary GAR losses do not harm general language understanding. The ordering does not track GAR performance (e.g., PCGrad shows the smallest MMLU drop despite the worst AR GAR), consistent with GAR and NTP occupying largely orthogonal subspaces.\n\n\\section{Cross-Scale Validation (Qwen-2.5-1.5B)}\\label{sec:appendix-1.5b}\n\nWe validate cross-scale on Qwen-2.5-1.5B-Instruct to test whether goal attention decay and $\\beta$-steering generalize to smaller models.\n\n\\paragraph{Phase~1 GAR decay.} The 1.5B base model exhibits 79.8\\% GAR decline from turn~1 to mid-turns (vs.\\ 70.8\\% on 7B), confirming that attention decay is present across scales and is more severe at smaller model sizes.\n\n\\paragraph{Steering evaluation.} Table~\\ref{tab:1.5b-steering} reports AR evaluation ($N$\\,=\\,50). We report median PPL because Base $\\beta$\\,=\\,3 contains a catastrophic outlier (conversation~\\#11, PPL\\,$>$\\,$10^8$) that inflates the mean.\\footnote{The outlier occurs in a single conversation where $\\beta$-steering causes the base model to enter a degenerate repetition loop. ThreadGate produces zero such outliers across all $\\beta$ values, suggesting the gate provides stability against catastrophic steering failures.}\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Cross-scale $\\beta$-steering on Qwen-2.5-1.5B ($N$\\,=\\,50, AR). PPL is median due to catastrophic Base outlier at $\\beta$\\,=\\,3. TG eliminates outliers across all $\\beta$ values.}\n\\label{tab:1.5b-steering}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Model} & $\\beta$ & \\textbf{AR GAR} & \\textbf{PPL (med)} \\\\\n\\midrule\nBase & 0 & 0.017 & 1.909 \\\\\nTG & 0 & 0.023 & 1.897 \\\\\n\\midrule\nBase & 3 & 0.120 & 2.216 \\\\\nTG & 3 & 0.114 & 1.975 \\\\\n\\midrule\nBase & 5 & 0.657 & 2.804 \\\\\nTG & 5 & 0.715 & 2.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe steering pattern mirrors the 7B results: $\\beta$\\,=\\,5 recovers GAR to 0.657--0.715 ($p < 0.001$), confirming that attention misallocation is the proximal cause of GAR collapse across scales. At $\\beta$\\,=\\,0, TG shows a small but significant GAR advantage ($p$\\,=\\,0.005); at $\\beta$\\,=\\,3, the TG--Base difference is not statistically significant ($p$\\,=\\,0.815), unlike the 7B pattern where TG consistently outperforms Base. This scale-specific difference may reflect the 1.5B model's limited capacity to maintain learned routing at intermediate steering strengths. ThreadGate does provide a stability advantage---zero catastrophic PPL outliers vs.\\ one in Base---suggesting that residual gating regularizes attention distributions even when aggregate GAR is comparable.\n\n\\section{Per-Seed Detailed Results}\\label{sec:appendix-perseed}\n\nTables~\\ref{tab:perseed-ss} and~\\ref{tab:perseed-tg} report full per-seed breakdowns for the two multi-seed configurations, providing evidence that our main findings are robust to random initialization.\n\n\\paragraph{Scheduled sampling (3 seeds).} TF GAR-ours averages $0.517\\pm0.032$ across seeds under the held-out protocol (Table~\\ref{tab:perseed-ss}); under IID evaluation, TF is more stable ($0.499\\pm0.003$), with the held-out variance driven by seed~123's higher value on the larger $N$\\,=\\,200 sample. AR GAR shows meaningful variance (std\\,=\\,0.047): seed 42 produces the lowest AR GAR (0.347, gap 1.4$\\times$), seed 123 is intermediate (0.423, gap 1.3$\\times$), and seed 456 is highest (0.433, gap 1.2$\\times$). This variance is expected: AR evaluation involves free-form generation where small differences in learned attention patterns can compound across turns. The variance is asymmetric---all seeds remain well above the non-SS baseline (0.064)---so the qualitative conclusion (SS provides order-of-magnitude improvement) holds across seeds. At $\\beta$\\,=\\,5, the cross-seed variance nearly vanishes ($0.717\\pm0.001$), confirming that strong steering converges to a seed-independent attention equilibrium that overwhelms initialization differences.\n\n\\paragraph{ThreadGate (2 seeds).} Two seeds produce nearly identical TF metrics ($0.504\\pm0.001$) and similar AR GAR (0.064 vs.\\ 0.055), with gap ratios of 7.8$\\times$ and 9.1$\\times$ respectively. The 15\\% relative difference in AR GAR is small compared to the order-of-magnitude TF-AR gap, confirming that the exposure bias phenomenon is not seed-dependent.\n\n\\paragraph{Training dynamics.} Seed variance in training time is non-trivial for scheduled sampling: seed 123 requires 10.8 hours (80\\% overhead) vs.\\ 6.5 hours for seeds 42 and 456 (8\\% overhead). This variance is driven by the stochastic Bernoulli sampling of model-generated contexts: seed 123 happens to trigger longer autoregressive generation episodes early in training, where the model produces longer outputs before hitting the max-length cutoff. Despite this training-time variance, all three seeds converge to similar final metrics, suggesting the optimization landscape is robust.\n\n\\input{../artifacts/appendix_expansion/tab_perseed_ss.tex}\n\n\\input{../artifacts/appendix_expansion/tab_perseed_tg.tex}\n\n\\section{Per-Turn GAR Decay Analysis}\\label{sec:appendix-perturn-detail}\n\nTables~\\ref{tab:perturn-qwen} and~\\ref{tab:perturn-llama} present per-turn AR GAR values for all configurations on both architectures, complementing the aggregate mid-turn GAR reported in the main text (Table~\\ref{tab:four-way}).\n\n\\paragraph{Qwen per-turn dynamics.} On Qwen (Table~\\ref{tab:perturn-qwen}), all non-SS variants show rapid monotonic decay: turn-1 GAR ranges from 0.085 (Base) to 0.130 (ThreadGate), but by turn~5 all collapse below 0.07. The decay rate is approximately exponential for the first 3 turns, then plateaus near a floor value that varies by configuration (Base: 0.004, ThreadGate: 0.043--0.066, LoRA-only: 0.040). ThreadGate and LoRA-only show occasional turn-level fluctuations (e.g., TG turn~5 = 0.066 $>$ turn~4 = 0.043), which reflect stochastic variation in individual conversations rather than systematic recovery. Scheduled sampling retains substantially higher GAR throughout (turn-5 GAR\\,=\\,0.365 vs.\\ 0.066 for ThreadGate), with a much flatter decay profile (15\\% decline from turn~1 to turn~5 vs.\\ 49\\% for ThreadGate). This flatter profile is the signature of distributional robustification: SS-trained models encounter model-generated context during training, so the attention patterns are calibrated for the distribution they actually face during inference.\n\n\\paragraph{Llama per-turn dynamics.} On Llama (Table~\\ref{tab:perturn-llama}), the decay is steeper: Base GAR drops from 0.028 to 0.008 over 4 turns (71\\% decline in the $N$\\,=\\,20 evaluation), and from 0.026 to 0.003 over 10 turns (88\\% decline in the $N$\\,=\\,5 long-conversation evaluation). ThreadGate on Llama shows a distinctive pattern: turn-level GAR is roughly constant (0.038--0.049) rather than monotonically declining, suggesting that the gating mechanism maintains a stable floor on Llama that it fails to maintain on Qwen. However, this floor (0.04) is still an order of magnitude below the TF target (0.484), confirming that the fundamental TF-AR gap persists.\n\n\\paragraph{Cross-architecture comparison.} The per-turn decay profiles reveal an architectural difference: Qwen shows a sharper initial decline (turn~1 to turn~2: $-$62\\% for Base) followed by a plateau, while Llama shows a more gradual and sustained decline throughout. This difference may reflect the two architectures' different attention head configurations and layer counts, but the qualitative pattern---monotonic or near-monotonic decline toward a near-zero floor---is universal.\n\nFigures~\\ref{fig:perturn-qwen-detail} and~\\ref{fig:perturn-llama-detail} visualize these trajectories.\n\n\\input{../artifacts/appendix_expansion/tab_perturn_qwen.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_perturn_qwen_detail.pdf}\n  \\caption{Per-turn AR GAR-ours across six Qwen-2.5-7B configurations. Scheduled sampling (green) retains far higher GAR than all other variants, which cluster below 0.13 and decay rapidly.}\n  \\label{fig:perturn-qwen-detail}\n\\end{figure}\n\n\\input{../artifacts/appendix_expansion/tab_perturn_llama.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_perturn_llama_detail.pdf}\n  \\caption{Per-turn AR GAR decay on Llama-3.1-8B. (a)~Three-way comparison (Base, TG, LoRA-only; $N$\\,=\\,20, 4 turns). (b)~Extended Base decay profile ($N$\\,=\\,5, 10 turns), showing 90\\% decline.}\n  \\label{fig:perturn-llama-detail}\n\\end{figure}\n\n\\section{Extended Dataset Statistics}\\label{sec:appendix-dataset-ext}\n\nTable~\\ref{tab:dataset_stats} provides detailed statistics for the UltraChat training and evaluation splits. From the full UltraChat-200K corpus (207,865 conversations in the \\texttt{train\\_sft} split), we filter for conversations with $\\geq$5 assistant turns, yielding 17,302 candidates (8.3\\% of the full corpus). We randomly sample 8,000 for training, 50 for primary AR evaluation (mean 3.6 user turns), 50 for IID GAR diagnostics, and 200 for the instruction retention evaluation.\n\n\\paragraph{Filtering rationale.} The $\\geq$5 assistant turns threshold was chosen empirically: conversations with fewer than 3 assistant turns do not exhibit measurable attention decay (turn-1 to turn-3 GAR decline $<$5\\%), making them uninformative for studying multi-turn exposure bias. The 5-turn threshold provides sufficient turn depth while retaining a reasonable fraction of the corpus. The average conversation in the filtered set contains 5.6 assistant turns (range: 5--7), with a mean sequence length of 1,247 tokens after tokenization with the Qwen-2.5 tokenizer.\n\n\\paragraph{Evaluation split design.} We maintain four non-overlapping evaluation sets to avoid contamination: (1)~the primary AR evaluation ($N$\\,=\\,50) uses the same conversation structure as training but with held-out conversations, enabling direct comparison of TF vs.\\ AR behavior; (2)~the IID GAR diagnostic ($N$\\,=\\,50) uses a separate sample for ablation studies that require independent measurements; (3)~the large instruction retention set ($N$\\,=\\,200) provides sufficient statistical power for per-category compliance analysis across 18 constraint types; (4)~the long-conversation set ($N$\\,=\\,5, 10 turns each) tests scaling behavior beyond the training distribution.\n\n\\paragraph{Domain diversity.} UltraChat covers a broad range of conversational topics including knowledge Q\\&A, creative writing, reasoning, and open-ended discussion. We do not stratify by topic, as our focus is on the architectural mechanism (attention routing) rather than domain-specific performance. The topic diversity serves as implicit regularization against overfitting to specific conversation patterns.\n\n\\input{../artifacts/appendix_expansion/tab_dataset_stats.tex}\n\n\\section{Extended GAR Robustness Analysis}\\label{sec:appendix-gar-ext}\n\nTable~\\ref{tab:gar_robustness} and Figure~\\ref{fig:gar-robust-grouped} extend the GAR robustness analysis from \\S\\ref{sec:appendix-gar-robust} with turn-1 GAR and gap ratio metrics across all four token-position variants. We evaluate four ways to select the query token position for gradient attribution: (1)~\\textit{Last} (our default): the final token of each assistant turn, which captures the model's ``summary'' attention pattern at the prediction boundary; (2)~\\textit{All}: the mean over all assistant tokens, providing a position-averaged view; (3)~\\textit{First}: the first assistant token, which reflects initial attention allocation; (4)~\\textit{Goal-only}: attention to goal tokens as defined by \\citet{dongre2026attention}, which restricts the target set to system-prompt tokens.\n\n\\paragraph{Position-specific vs.\\ broad improvement.} The key finding is a clear dichotomy between ThreadGate and Scheduled Sampling. ThreadGate improvements are restricted to last-token and goal-only positions (the two definitions sharing the query position targeted by the GAR loss): gap ratios drop to 1.21$\\times$ and 1.07$\\times$ respectively. All-token (5.04$\\times$) and first-token (8.24$\\times$) GAR remain near base levels, confirming that the learned routing is position-specific. Scheduled Sampling raises all four definitions above 0.36 with gap ratios $\\leq$1.83$\\times$, demonstrating that distributional robustification builds broad goal attention across token positions rather than overfitting to the position targeted by the loss.\n\n\\paragraph{Turn-1 vs.\\ mid-turn dynamics.} Turn-1 GAR is consistently higher than mid-turn GAR across all definitions and conditions, reflecting the first turn's proximity to the ground-truth prefix in training. The gap ratio quantifies how much of this initial attention survives into later turns. First-token GAR shows the largest gap ratios (Base: 13.3$\\times$, TG: 8.2$\\times$), indicating that the first-token position is most vulnerable to distributional drift---the initial token's attention pattern is highly dependent on the conditioning context, which diverges most from training under autoregressive generation.\n\n\\input{../artifacts/appendix_expansion/tab_gar_robustness.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_gar_robustness_grouped.pdf}\n  \\caption{Mid-turn GAR across four token-position definitions. SS raises all four above 0.36; TG only improves last-token and goal-only.}\n  \\label{fig:gar-robust-grouped}\n\\end{figure}\n\n\\section{MMLU Category Breakdown}\\label{sec:appendix-mmlu-ext}\n\nTable~\\ref{tab:mmlu_detail} breaks down MMLU 5-shot accuracy by category (STEM, Social Sciences, Humanities, Other) for all six Qwen-2.5-7B training configurations. This analysis addresses a potential concern: that auxiliary attention objectives might divert representational capacity from general language understanding, particularly in knowledge-intensive STEM domains.\n\n\\paragraph{Per-category analysis.} The maximum per-category degradation is 1.2\\,pp (ThreadGate on STEM), and no category shows systematic degradation across all variants. Notably, the ordering of variants differs across categories: ThreadGate shows the largest STEM drop but the smallest Humanities drop, while PCGrad shows the smallest overall drop despite having the worst AR GAR. This lack of correlation between GAR performance and MMLU degradation is consistent with GAR and NTP occupying largely orthogonal parameter subspaces---the LoRA adapter capacity (4.2M parameters) is sufficient to accommodate both objectives without interference.\n\n\\paragraph{Statistical significance.} The per-category differences are small relative to the evaluation noise: with $N$\\,=\\,14,042 questions total ($\\sim$3,500 per category), a 0.8\\,pp accuracy difference corresponds to $\\sim$28 questions, well within expected stochastic variation for 5-shot in-context learning. A chi-squared test comparing the best (PCGrad, 73.86\\%) and worst (Uniform Gate, 73.46\\%) variants yields $p$\\,=\\,0.503, confirming no significant difference. The category-level stability confirms that auxiliary GAR losses and gating do not selectively harm any knowledge domain.\n\nFigure~\\ref{fig:mmlu-comparison} visualizes the per-category comparison, showing tight clustering across all variants within each category.\n\n\\input{../artifacts/appendix_expansion/tab_mmlu_detail.tex}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_mmlu_comparison.pdf}\n  \\caption{MMLU 5-shot accuracy by category across training configurations. All variants remain within 1.2\\,pp of the LoRA-only baseline across all categories.}\n  \\label{fig:mmlu-comparison}\n\\end{figure}\n\n\\section{Extended Cross-Scale Results (Qwen-2.5-1.5B)}\\label{sec:appendix-1.5b-ext}\n\nTable~\\ref{tab:qwen15b_results} extends the cross-scale analysis with Phase~1 GAR diagnostics, detailed Phase~2 training results, and $\\beta$-steering evaluation on the Qwen-2.5-1.5B-Instruct model.\n\n\\paragraph{Phase 1: GAR decay.} The 1.5B base model exhibits 79.8\\% relative GAR decline from turn~1 to mid-turns, more severe than the 7B model's 70.8\\% decline. This scale-dependent decay severity is consistent with smaller models having less redundant attention capacity: with 28 layers but only 1.5B parameters (vs.\\ 7B), each layer carries proportionally more of the total representational burden, leaving less room for goal-oriented attention to persist alongside the primary NTP objective.\n\n\\paragraph{Phase 2: Training.} ThreadGate training on 1.5B converges to TF GAR-ours of 0.498 with PPL of 2.67, closely matching the 7B results (0.504 / 2.78). The gate parameter count scales linearly with layer count (identical architecture, so ${\\sim}$57K gate parameters). Training completes in 2.1 hours vs.\\ 6.0 hours for 7B, reflecting the smaller model's reduced forward/backward pass cost.\n\n\\paragraph{Steering evaluation.} At $\\beta$\\,=\\,5, ThreadGate recovers GAR to 0.715 ($p < 0.001$), closely matching the 7B result (0.727). The recovery is essentially scale-independent at the strong steering regime: the attention bias added by $\\beta$-steering overwhelms any capacity differences. At $\\beta$\\,=\\,3, the picture differs: the TG--Base difference is not statistically significant ($p$\\,=\\,0.815) on 1.5B, unlike the significant difference on 7B ($p$\\,=\\,0.039). This scale-dependent response at intermediate $\\beta$ may reflect the 1.5B model's reduced capacity for fine-grained attention routing: with fewer parameters per layer, the model cannot sustain the subtle attention reweighting that $\\beta$\\,=\\,3 attempts.\n\n\\paragraph{Catastrophic outliers.} Base 1.5B at $\\beta$\\,=\\,3 produces one catastrophic PPL outlier (conversation \\#11, PPL $> 10^8$) caused by a degenerate repetition loop. ThreadGate produces zero such outliers across all $\\beta$ values, suggesting the gate provides a stabilizing effect on attention distributions even when aggregate GAR is comparable. We report median PPL to avoid this outlier dominating the central tendency estimate.\n\n\\input{../artifacts/appendix_expansion/tab_qwen15b_results.tex}\n\n\\section{Extended Statistical Analysis}\\label{sec:appendix-stats-ext}\n\nTable~\\ref{tab:statistical_tests} consolidates all statistical tests reported in this paper, including effect sizes, 95\\% bootstrap confidence intervals, and significance levels. This section provides methodological detail beyond the summary in Appendix~\\ref{sec:appendix-stats}.\n\n\\paragraph{Test selection rationale.} All primary comparisons use paired Wilcoxon signed-rank tests on $N$\\,=\\,39 conversations (those with $\\geq$3 turns from the 50-conversation held-out set). We use non-parametric tests because per-conversation GAR distributions are heavily right-skewed (skewness $>$ 2.0 for Base and PCGrad at $\\beta$\\,=\\,0), violating normality assumptions required by parametric alternatives. The pairing structure (same conversations evaluated under different training configurations) controls for conversation-level confounds (topic difficulty, conversation length, system-prompt complexity).\n\n\\paragraph{Effect size interpretation.} Effect sizes are computed as rank-biserial correlations ($r = Z / \\sqrt{N}$), following standard practice. The largest effect is SS vs.\\ TG ($r$\\,=\\,0.869, $p < 0.001$), a large effect by conventional thresholds ($r \\geq 0.5$), confirming that scheduled sampling produces a qualitatively different outcome. The TG vs.\\ Base effect ($r$\\,=\\,0.802) is also large, while TG vs.\\ LoRA-only ($r$\\,=\\,0.454) is medium, reflecting the modest incremental benefit of gating over LoRA alone.\n\n\\paragraph{Steering dose-response pattern.} At $\\beta$\\,=\\,0, all four comparisons are significant ($p \\leq 0.004$). At $\\beta$\\,=\\,3 (the phase transition), TG vs.\\ Base becomes marginally significant ($p$\\,=\\,0.039) and SS vs.\\ TG remains significant ($p$\\,=\\,0.010), but TG vs.\\ LoRA-only and PCGrad vs.\\ TG lose significance ($p > 0.7$). At $\\beta$\\,=\\,5, no pairwise comparison reaches significance---steering dominates and equalizes all variants. This dose-response pattern confirms that the training-time variant effects are real but small relative to the inference-time steering effect.\n\n\\paragraph{Instruction retention.} The instruction retention analysis uses McNemar's test on $N$\\,=\\,54 paired constraint evaluations (18 constraint types $\\times$ 3 conversations). The marginal significance ($p$\\,=\\,0.077) reflects the small sample size rather than a null effect: the point-biserial correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is significant when treating compliance as a continuous variable, and the per-category breakdown (Table~\\ref{tab:ir-results}) shows a clear content-constraint improvement (+23.8\\,pp).\n\n\\paragraph{Multiple comparisons.} We report uncorrected $p$-values for the same reason described in Appendix~\\ref{sec:appendix-stats}: comparisons are hypothesis-driven (each tests a specific causal exclusion in the analysis chain), not exploratory. All reported significant results ($p \\leq 0.039$) survive Holm-Bonferroni correction for the 4 primary comparisons within each $\\beta$ level.\n\n\\input{../artifacts/appendix_expansion/tab_statistical_tests.tex}\n\n\\section{Extended Training Dynamics}\\label{sec:appendix-training-ext}\n\nFigure~\\ref{fig:training-6panel} presents the complete training loss landscape for all five Qwen-2.5-7B conditions (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Scheduled Sampling) plus the base model, showing NTP loss, GAR loss, and total loss across three epochs.\n\n\\paragraph{NTP loss convergence.} All fine-tuned variants converge to NTP loss ${\\sim}$0.93 by epoch~3, with final-epoch values ranging from 0.929 (LoRA-only) to 0.934 (ThreadGate). PCGrad shows marginally higher variance due to gradient projection, but converges to the same terminal value. The uniformity of NTP convergence across variants---including those with auxiliary losses (ThreadGate, PCGrad) and those without (LoRA-only)---confirms that the GAR auxiliary objective does not interfere with the primary language modeling task during training.\n\n\\paragraph{GAR loss dynamics.} GAR loss collapses to near-zero within the first epoch under teacher forcing across all variants, consistent with the auxiliary objective being easy to optimize when the model conditions on ground-truth context. This rapid convergence is a double-edged sword: while it confirms that the MSE formulation (v7) achieves stable optimization, the ease of convergence also means the model never learns to maintain attention under distributional drift. The scheduled sampling variant shows distinctive dynamics: higher initial GAR loss variance from stochastic context mixing, with occasional spikes when a particularly challenging model-generated context is sampled, followed by convergence to a similar final value.\n\n\\paragraph{Training-inference disconnect.} The key observation is that training-time convergence is indistinguishable across variants: an observer with access only to training curves could not predict the 5.4$\\times$ AR GAR difference between SS and TG. This disconnect reinforces the diagnosis that the failure occurs at the training-to-inference transition, not during optimization, and explains why architectural modifications (gating, PCGrad) that operate during training cannot address the fundamental distributional mismatch.\n\n\\begin{figure*}[t]\n  \\centering\n  \\includegraphics[width=0.75\\textwidth]{fig_training_curves_6panel.pdf}\n  \\caption{Training loss curves for all five Qwen conditions. NTP loss (left) converges to ${\\sim}$0.93 across variants; GAR loss (center) collapses within epoch~1; total loss (right) is NTP-dominated. Training-time behavior is indistinguishable; the failure emerges only at inference.}\n  \\label{fig:training-6panel}\n\\end{figure*}\n\n\\section{Per-$\\beta$ Steering Visualization}\\label{sec:appendix-steering-viz}\n\nFigure~\\ref{fig:steering-4panel} visualizes per-turn GAR trajectories under four steering strengths ($\\beta$\\,=\\,0, 3, 5, 10), revealing the turn-level dynamics that underlie the aggregate steering results in Table~\\ref{tab:steering-full}.\n\n\\paragraph{Unsteered baseline ($\\beta$\\,=\\,0).} GAR decays monotonically from 0.12 to 0.02 over five turns, with the steepest decline between turns~1 and~2 ($-$44\\%). This trajectory matches the per-turn profiles in Appendix~\\ref{sec:appendix-perturn-detail} and confirms that the decay is a smooth, progressive phenomenon rather than a discrete failure at a specific turn.\n\n\\paragraph{Phase transition ($\\beta$\\,=\\,3).} Turn-1 GAR jumps to ${\\sim}$0.55, but per-turn decay persists (${\\sim}$15\\% decline from turn~1 to turn~5). This indicates that steering partially compensates for the distributional drift but does not eliminate it: the attention bias adds a constant offset to goal-token logits, while the drift compounds multiplicatively across turns. The residual decay at $\\beta$\\,=\\,3 explains why this operating point shows the strongest training-variant effects in the dose-response analysis (Appendix~\\ref{sec:appendix-stats-ext}).\n\n\\paragraph{Sustained recovery ($\\beta$\\,=\\,5).} GAR is sustained above 0.6 throughout, with minimal per-turn decay ($<$5\\% decline). At this steering strength, the constant attention bias dominates the per-turn drift, effectively replacing the lost training-time signal with an inference-time substitute. The 9\\% PPL cost (1.43 $\\to$ 1.77) is modest compared to the order-of-magnitude GAR recovery.\n\n\\paragraph{Saturation regime ($\\beta$\\,=\\,10).} GAR saturates near 1.0 across all turns but PPL degrades catastrophically ($>$3.5), as the excessive attention bias distorts the attention distribution beyond the model's capacity for coherent generation. This regime is impractical and serves as an upper bound on the steering approach.\n\n\\paragraph{Operating region.} The region $\\beta \\in [3, 5]$ balances GAR recovery against PPL cost, and the per-turn profiles confirm that steering must counteract an ongoing distributional drift rather than a one-time initialization failure---a key diagnostic that distinguishes exposure bias from alternative hypotheses (e.g., capacity limitations or optimization failures).\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_steering_perturn_4panel.pdf}\n  \\caption{Per-turn GAR under four $\\beta$-steering strengths. At $\\beta$\\,=\\,0, monotonic decay; at $\\beta$\\,=\\,3, partial recovery with residual decay; at $\\beta$\\,=\\,5, sustained high GAR; at $\\beta$\\,=\\,10, saturation with catastrophic PPL.}\n  \\label{fig:steering-4panel}\n\\end{figure}\n\n\\section{Llama-3.1-8B Scheduled Sampling Details}\\label{sec:appendix-llama-ss}\n\nLlama-3.1-8B-Instruct was trained with scheduled sampling using the same protocol as Qwen (\\S\\ref{sec:appendix-ss}), with one key difference: training was stopped at 2 epochs (${\\sim}$14{,}400 steps) instead of 3, because Llama's per-step wall-clock time was ${\\sim}$4$\\times$ slower than Qwen on the same hardware (624 steps/h vs.\\ ${\\sim}$2{,}400 steps/h for Qwen). This is attributable to different vocabulary sizes (Llama 128K vs.\\ Qwen 152K tokens) and attention implementation. The 2-epoch checkpoint was selected based on convergence of TF GAR (0.477, within 0.02 of Qwen's 3-epoch value 0.498).\n\n\\paragraph{$\\beta$-steering on Llama SS.}\nTable~\\ref{tab:llama-ss-steering} reports $\\beta$-steering results on the Llama SS model. Unlike Qwen, $\\beta$\\,=\\,3 does not trigger recovery on Llama (GAR 0.173 vs.\\ 0.166 at $\\beta$\\,=\\,0). At $\\beta$\\,=\\,5, GAR reaches 0.791---higher than Qwen's 0.717---suggesting that Llama's attention distribution is more responsive to the additive bias at higher steering strengths, possibly because the lower baseline AR GAR leaves more headroom for steering to exploit.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{$\\beta$-steering on Llama-3.1-8B SS model ($N$\\,=\\,50, $T$\\,=\\,4).}\n\\label{tab:llama-ss-steering}\n\\begin{tabular}{@{}l ccc@{}}\n\\toprule\n& $\\beta$\\,=\\,0 & $\\beta$\\,=\\,3 & $\\beta$\\,=\\,5 \\\\\n\\midrule\nAR GAR & 0.166 & 0.173 & 0.791 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-model comparison.}\nTable~\\ref{tab:llama-vs-qwen-ss} compares scheduled sampling across both architectures. Both models show large gap compression relative to their ThreadGate baselines, but the residual gap on Llama (2.9$\\times$) is larger than Qwen's (1.2$\\times$). We attribute this to training duration: Llama received only 2 epochs of scheduled sampling exposure versus Qwen's 3 epochs. Llama reduces its median-based gap by 9.3$\\times$ (from 27$\\times$ to 2.9$\\times$) while Qwen reduces by 6.5$\\times$ (from 7.8$\\times$ to 1.2$\\times$), suggesting that a third epoch would likely narrow the residual gap further. Notably, $\\beta$-steering is more effective on Llama (0.791 vs.\\ 0.717 at $\\beta$\\,=\\,5), partially compensating for the weaker training-time compression.\n\n\\paragraph{Architectural differences.}\nSeveral architectural differences between Qwen-2.5-7B and Llama-3.1-8B may contribute to the cross-model gap variation. Llama uses Grouped Query Attention (GQA) with 8 KV heads (vs.\\ Qwen's full 28-head multi-head attention, MHA), which reduces the number of independently steerable attention heads by 3.5$\\times$. Llama also uses Rotary Position Embedding (RoPE) with a longer default context (128K tokens vs.\\ Qwen's 32K), which may affect how positional information interacts with goal-token attention at different conversation depths. Despite these differences, the qualitative pattern is identical: TF convergence, AR collapse, and SS-mediated recovery, confirming that exposure bias on auxiliary attention losses is architecture-general rather than an artifact of a specific attention implementation.\n\n\\paragraph{Training dynamics.}\nThe Llama SS training loss trajectory closely mirrors Qwen's during the first two epochs: NTP loss converges within epoch~1 (final NTP loss 0.62 for Llama vs.\\ 0.58 for Qwen), while GAR loss continues to decrease throughout epoch~2. The scheduled sampling ratio reaches ${\\sim}$0.20 at the end of epoch~2 (vs.\\ 0.30 at end of epoch~3 for Qwen), meaning Llama was exposed to less model-generated context during training. This partial exposure is sufficient to achieve meaningful gap compression (27$\\times$ $\\to$ 2.9$\\times$ by median) but leaves a larger residual gap than Qwen's full 3-epoch schedule.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Scheduled sampling comparison: Qwen-2.5-7B vs.\\ Llama-3.1-8B.}\n\\label{tab:llama-vs-qwen-ss}\n\\begin{tabular}{@{}l cc@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Qwen-7B} & \\textbf{Llama-8B} \\\\\n\\midrule\nSS epochs & 3 & 2 \\\\\nTF GAR & 0.498 & 0.477 \\\\\nAR GAR ($\\beta$\\,=\\,0) & 0.401 & 0.166 \\\\\nTF/AR gap & 1.2$\\times$ & 2.9$\\times$ \\\\\nBaseline TG gap & 7.8$\\times$ & 27$\\times$ (median) \\\\\nGap compression & 6.5$\\times$ & 9.3$\\times$ \\\\\nAR GAR ($\\beta$\\,=\\,5) & 0.717 & 0.791 \\\\\nTF PPL & 2.78 & 2.82 \\\\\nAR PPL & 1.441 & 1.370 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Use of AI Assistants}\\label{sec:appendix-ai}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n",
      "numLines": 348,
      "startLine": 500,
      "totalLines": 847
    }
  },
  "sourceToolAssistantUUID": "a48c8332-6681-4294-914a-7ba222032c2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1091_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 附录内容引用完整性检查  **任务：** 检查论文附录的所有内容是否在正文中都有准确、合理的引用，修复孤儿附录。  **Step 1：逐项盘点** 列出附录里每一个 section/subsection/table/figure/algorithm/proof/prompt。  **Step 2：逐项验证引用** 对每一项，在正文搜索是否有至少一句话指向…",
  "leafUuid": "01cd419f-e228-4dea-b9a5-93357869db71",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1092_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Assistant

_source line 1093 · 2026-05-25T09:06:42.437Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full appendix. Let me catalog all sections/subsections/tables/figures and check if they are referenced from the main text.

**Appendix sections:**
1. `\section{Training Configuration}\label{sec:appendix-hyper}` — Table `tab:hyperparams`
2. `\section{Loss Formulation Search}\label{sec:appendix-loss}` — Table `tab:loss-iterations`
3. `\section{Instruction Retention Details}\label{sec:appendix-ir}` — Figure `fig:ir-bar`, Table `tab:ir-results`


4. `\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}` — Table `tab:n5-ar`
5. `\section{Statistical Test Details}\label{sec:appendix-stats}` — Table `tab:stat-tests`
6. `\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}` — Table `tab:llama-full`, Figure `fig:crossmodel`, Table `tab:crossmodel-detail`, Table `tab:gradient-crossmodel`
7. `\section{Additional Visualizations}\label{sec:appendix-viz}` — with subsections continuing below

: gate profile heatmaps, cross-model comparisons, per-turn attention and retrieval decay patterns, bootstrap confidence intervals, gate value distributions, training loss curves, full attention steering results, per-layer gate profiles, and scheduled sampling implementation details.
8. `\section{Per-Layer Gate Profile}\label{sec:appendix-gate-profile}` — Table `tab:gate-profile`
9. `\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}` — Figure `fig:ss-dynamics`
10. `\section{Computational Cost Analysis}\label{sec:appendix-cost}` — Table `tab:cost`
11. `\section{Qualitative Steering Examples}\label{sec:appendix-examples}` — Table `tab:examples`
12. `\section{Gradient Conflict Analysis}\label{sec:appendix-gradient}` — Figure `fig:training-pcgrad`, Figure `fig:gradient-heatmap`
13. `\section{Training Data Characteristics}\label{sec:appendix-data}` — Table `tab:data-stats`
14. `\section{Exposure Bias Scaling}\label{sec:appendix-eb-scaling}` — Figure `fig:eb-scaling`
15. `\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}` — Figures `fig:kl_ar_gar_curves`

Now I'm mapping out the remaining appendix sections covering computational costs, qualitative examples, gradient conflict analysis, training data statistics, exposure bias scaling, and per-turn attention-retrieval dynamics.

Continuing with per-head KL divergence analysis, GAR definition robustness checks, MMLU general capability preservation, cross-scale validation on smaller models, detailed per-seed results, per-turn GAR decay patterns, extended dataset statistics, extended GAR robustness analysis, and MMLU category breakdowns. I'm finishing up the appendix section labels and now need to check the main text to see which of these appendix references are actually cited, so I can verify the document structure is complete.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01cd419f-e228-4dea-b9a5-93357869db71",
  "isSidechain": false,
  "requestId": "req_011CbP2C9s3rWEUB1UqtTN94",
  "type": "assistant",
  "uuid": "6e510479-b125-42be-b55f-8e849fd4354f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lgng6MLFihN1B9y7tq1B4X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12953,
      "cache_read_input_tokens": 148205,
      "output_tokens": 1641,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1641,
          "cache_read_input_tokens": 148205,
          "cache_creation_input_tokens": 12953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12953
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

_source line 1094 · 2026-05-25T09:06:42.448Z_

Now let me find all appendix cross-references in the main text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e510479-b125-42be-b55f-8e849fd4354f",
  "isSidechain": false,
  "requestId": "req_011CbP2C9s3rWEUB1UqtTN94",
  "type": "assistant",
  "uuid": "e93122b8-f589-4b8d-9cb2-6e774f4b65a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lgng6MLFihN1B9y7tq1B4X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12953,
      "cache_read_input_tokens": 148205,
      "output_tokens": 1641,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1641,
          "cache_read_input_tokens": 148205,
          "cache_creation_input_tokens": 12953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12953
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

_source line 1095 · 2026-05-25T09:06:43.770Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01DLsPAGNvzCbDxZtLhPVN9H`</summary>

```json
{
  "pattern": "appendix-",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e93122b8-f589-4b8d-9cb2-6e774f4b65a0",
  "isSidechain": false,
  "requestId": "req_011CbP2C9s3rWEUB1UqtTN94",
  "type": "assistant",
  "uuid": "c0c16100-d349-4855-8a0d-580f85b7430b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lgng6MLFihN1B9y7tq1B4X",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12953,
      "cache_read_input_tokens": 148205,
      "output_tokens": 1641,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1641,
          "cache_read_input_tokens": 148205,
          "cache_creation_input_tokens": 12953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12953
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

_source line 1096 · 2026-05-25T09:06:43.796Z_

<details><summary>↩ Tool result · `toolu_01DLsPAGNvzCbDxZtLhPVN9H`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:7:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:11:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:13:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:17:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:32:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:34:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:6:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:12:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:27:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:38:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex:3:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex:5:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex:47:$\mathcal{L}_\text{NTP}$ is the standard next-token prediction loss. For $\mathcal{L}_\text{GAR}$, we use MSE rather than cross-entropy because GAR is a continuous ratio and MSE provides \emph{bidirectional} pressure---penalizing both under- and over-attention, preventing identity collapse (Appendix~\ref{sec:appendix-loss}):
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex:55:where $\mathbf{g} = [g_1, \ldots, g_L]$ and $\sigma_\text{min} = 0.05$ is a minimum standard deviation threshold ($\lambda_\text{GAR} = \lambda_\text{div} = 1.0$). This formulation emerged from seven iterations spanning four loss families (Appendix~\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity; only MSE provides the bidirectional pressure needed to prevent identity collapse.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex:59:We design a five-way comparison where each adjacent pair isolates one factor: \textbf{ThreadGate (TG) vs.\ Uniform Gate (UG)} (turn conditioning), \textbf{TG vs.\ LoRA-only} (gating mechanism), \textbf{ThreadGate vs.\ +PCGrad} (gradient conflict via gradient surgery \citep{yu2020pcgrad}), and \textbf{Fine-tuned vs.\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\ref{sec:appendix-hyper}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:1:\section{Training Configuration}\label{sec:appendix-hyper}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:35:\section{Loss Formulation Search}\label{sec:appendix-loss}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:66:\section{Instruction Retention Details}\label{sec:appendix-ir}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:103:\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:131:\section{Statistical Test Details}\label{sec:appendix-stats}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:167:\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:230:\section{Additional Visualizations}\label{sec:appendix-viz}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:300:\subsection{Full Attention Steering Results}\label{sec:appendix-steering}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:334:\section{Per-Layer Gate Profile}\label{sec:appendix-gate-profile}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:362:\paragraph{Cross-model comparison.} See \S\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:364:\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:381:\section{Computational Cost Analysis}\label{sec:appendix-cost}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:414:\section{Qualitative Steering Examples}\label{sec:appendix-examples}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:436:\section{Gradient Conflict Analysis}\label{sec:appendix-gradient}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:462:\section{Training Data Characteristics}\label{sec:appendix-data}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:464:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:483:\section{Exposure Bias Scaling}\label{sec:appendix-eb-scaling}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:491:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:500:\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:522:\section{Per-Head KL Divergence Analysis}\label{sec:appendix-kl}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:547:\section{GAR Definition Robustness}\label{sec:appendix-gar-robust}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:571:\section{General Capability Preservation (MMLU)}\label{sec:appendix-mmlu}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:595:\section{Cross-Scale Validation (Qwen-2.5-1.5B)}\label{sec:appendix-1.5b}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:625:\section{Per-Seed Detailed Results}\label{sec:appendix-perseed}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:639:\section{Per-Turn GAR Decay Analysis}\label{sec:appendix-perturn-detail}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:669:\section{Extended Dataset Statistics}\label{sec:appendix-dataset-ext}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:681:\section{Extended GAR Robustness Analysis}\label{sec:appendix-gar-ext}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:683:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:698:\section{MMLU Category Breakdown}\label{sec:appendix-mmlu-ext}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:717:\section{Extended Cross-Scale Results (Qwen-2.5-1.5B)}\label{sec:appendix-1.5b-ext}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:731:\section{Extended Statistical Analysis}\label{sec:appendix-stats-ext}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:733:Table~\ref{tab:statistical_tests} consolidates all statistical tests reported in this paper, including effect sizes, 95\% bootstrap confidence intervals, and significance levels. This section provides methodological detail beyond the summary in Appendix~\ref{sec:appendix-stats}.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:743:\paragraph{Multiple comparisons.} We report uncorrected $p$-values for the same reason described in Appendix~\ref{sec:appendix-stats}: comparisons are hypothesis-driven (each tests a specific causal exclusion in the analysis chain), not exploratory. All reported significant results ($p \leq 0.039$) survive Holm-Bonferroni correction for the 4 primary comparisons within each $\beta$ level.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:747:\section{Extended Training Dynamics}\label{sec:appendix-training-ext}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:764:\section{Per-$\beta$ Steering Visualization}\label{sec:appendix-steering-viz}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:768:\paragraph{Unsteered baseline ($\beta$\,=\,0).} GAR decays monotonically from 0.12 to 0.02 over five turns, with the steepest decline between turns~1 and~2 ($-$44\%). This trajectory matches the per-turn profiles in Appendix~\ref{sec:appendix-perturn-detail} and confirms that the decay is a smooth, progressive phenomenon rather than a discrete failure at a specific turn.
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:770:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:785:\section{Llama-3.1-8B Scheduled Sampling Details}\label{sec:appendix-llama-ss}
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:787:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:835:\section{Use of AI Assistants}\label{sec:appendix-ai}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0c16100-d349-4855-8a0d-580f85b7430b",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "e2968bb1-9d72-486c-91cc-57f95369e2e3",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:7:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:11:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:13:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:17:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:32:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex:34:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:6:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:12:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:27:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex:38:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex:3:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex:5:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex:47:$\\mathcal{L}_\\text{NTP}$ is the standard next-token prediction loss. For $\\mathcal{L}_\\text{GAR}$, we use MSE rather than cross-entropy because GAR is a continuous ratio and MSE provides \\emph{bidirectional} pressure---penalizing both under- and over-attention, preventing identity collapse (Appendix~\\ref{sec:appendix-loss}):\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex:55:where $\\mathbf{g} = [g_1, \\ldots, g_L]$ and $\\sigma_\\text{min} = 0.05$ is a minimum standard deviation threshold ($\\lambda_\\text{GAR} = \\lambda_\\text{div} = 1.0$). This formulation emerged from seven iterations spanning four loss families (Appendix~\\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity; only MSE provides the bidirectional pressure needed to prevent identity collapse.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex:59:We design a five-way comparison where each adjacent pair isolates one factor: \\textbf{ThreadGate (TG) vs.\\ Uniform Gate (UG)} (turn conditioning), \\textbf{TG vs.\\ LoRA-only} (gating mechanism), \\textbf{ThreadGate vs.\\ +PCGrad} (gradient conflict via gradient surgery \\citep{yu2020pcgrad}), and \\textbf{Fine-tuned vs.\\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\\ref{sec:appendix-hyper}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:1:\\section{Training Configuration}\\label{sec:appendix-hyper}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:35:\\section{Loss Formulation Search}\\label{sec:appendix-loss}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:66:\\section{Instruction Retention Details}\\label{sec:appendix-ir}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:103:\\section{Long-Conversation AR Evaluation}\\label{sec:appendix-n5}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:131:\\section{Statistical Test Details}\\label{sec:appendix-stats}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:167:\\section{Llama-3.1-8B Complete Results}\\label{sec:appendix-llama}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:230:\\section{Additional Visualizations}\\label{sec:appendix-viz}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:300:\\subsection{Full Attention Steering Results}\\label{sec:appendix-steering}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:334:\\section{Per-Layer Gate Profile}\\label{sec:appendix-gate-profile}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:362:\\paragraph{Cross-model comparison.} See \\S\\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:364:\\section{Scheduled Sampling Implementation}\\label{sec:appendix-ss}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:381:\\section{Computational Cost Analysis}\\label{sec:appendix-cost}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:414:\\section{Qualitative Steering Examples}\\label{sec:appendix-examples}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:436:\\section{Gradient Conflict Analysis}\\label{sec:appendix-gradient}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:462:\\section{Training Data Characteristics}\\label{sec:appendix-data}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:464:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:483:\\section{Exposure Bias Scaling}\\label{sec:appendix-eb-scaling}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:491:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:500:\\section{Per-Turn AR GAR Dynamics}\\label{sec:appendix-ar-gar-dynamics}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:522:\\section{Per-Head KL Divergence Analysis}\\label{sec:appendix-kl}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:547:\\section{GAR Definition Robustness}\\label{sec:appendix-gar-robust}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:571:\\section{General Capability Preservation (MMLU)}\\label{sec:appendix-mmlu}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:595:\\section{Cross-Scale Validation (Qwen-2.5-1.5B)}\\label{sec:appendix-1.5b}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:625:\\section{Per-Seed Detailed Results}\\label{sec:appendix-perseed}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:639:\\section{Per-Turn GAR Decay Analysis}\\label{sec:appendix-perturn-detail}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:669:\\section{Extended Dataset Statistics}\\label{sec:appendix-dataset-ext}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:681:\\section{Extended GAR Robustness Analysis}\\label{sec:appendix-gar-ext}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:683:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:698:\\section{MMLU Category Breakdown}\\label{sec:appendix-mmlu-ext}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:717:\\section{Extended Cross-Scale Results (Qwen-2.5-1.5B)}\\label{sec:appendix-1.5b-ext}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:731:\\section{Extended Statistical Analysis}\\label{sec:appendix-stats-ext}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:733:Table~\\ref{tab:statistical_tests} consolidates all statistical tests reported in this paper, including effect sizes, 95\\% bootstrap confidence intervals, and significance levels. This section provides methodological detail beyond the summary in Appendix~\\ref{sec:appendix-stats}.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:743:\\paragraph{Multiple comparisons.} We report uncorrected $p$-values for the same reason described in Appendix~\\ref{sec:appendix-stats}: comparisons are hypothesis-driven (each tests a specific causal exclusion in the analysis chain), not exploratory. All reported significant results ($p \\leq 0.039$) survive Holm-Bonferroni correction for the 4 primary comparisons within each $\\beta$ level.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:747:\\section{Extended Training Dynamics}\\label{sec:appendix-training-ext}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:764:\\section{Per-$\\beta$ Steering Visualization}\\label{sec:appendix-steering-viz}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:768:\\paragraph{Unsteered baseline ($\\beta$\\,=\\,0).} GAR decays monotonically from 0.12 to 0.02 over five turns, with the steepest decline between turns~1 and~2 ($-$44\\%). This trajectory matches the per-turn profiles in Appendix~\\ref{sec:appendix-perturn-detail} and confirms that the decay is a smooth, progressive phenomenon rather than a discrete failure at a specific turn.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:770:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:785:\\section{Llama-3.1-8B Scheduled Sampling Details}\\label{sec:appendix-llama-ss}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:787:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex:835:\\section{Use of AI Assistants}\\label{sec:appendix-ai}",
    "numLines": 55
  },
  "sourceToolAssistantUUID": "c0c16100-d349-4855-8a0d-580f85b7430b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1097_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 附录内容引用完整性检查  **任务：** 检查论文附录的所有内容是否在正文中都有准确、合理的引用，修复孤儿附录。  **Step 1：逐项盘点** 列出附录里每一个 section/subsection/table/figure/algorithm/proof/prompt。  **Step 2：逐项验证引用** 对每一项，在正文搜索是否有至少一句话指向…",
  "leafUuid": "e2968bb1-9d72-486c-91cc-57f95369e2e3",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1098_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Assistant

_source line 1099 · 2026-05-25T09:06:47.867Z_

Now let me systematically check which appendix labels appear in main text (excluding appendix.tex itself).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2968bb1-9d72-486c-91cc-57f95369e2e3",
  "isSidechain": false,
  "requestId": "req_011CbP2E8FchzSKtSWCzmCFv",
  "type": "assistant",
  "uuid": "d18fe314-4818-4a9a-a50f-9716df688a8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ubDQVVjirULizCVzxXM25",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5470,
      "cache_read_input_tokens": 161158,
      "output_tokens": 670,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 670,
          "cache_read_input_tokens": 161158,
          "cache_creation_input_tokens": 5470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5470
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

_source line 1100 · 2026-05-25T09:06:55.369Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01W747LaAEKfRqCEKANR7Vch`</summary>

```json
{
  "description": "Audit appendix cross-references",
  "prompt": "I need you to check which appendix section labels are referenced from the main text of a paper. \n\nThe appendix is at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex\n\nThe main text sections are these files (NOT appendix.tex):\n- abstract.tex\n- introduction.tex  \n- method.tex\n- related_work.tex\n- experiments.tex\n- analysis.tex\n- discussion.tex\n- conclusion.tex\n- limitations.tex\n\nAll in: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/\n\nHere are ALL the appendix section labels to check:\n1. sec:appendix-hyper\n2. sec:appendix-loss\n3. sec:appendix-ir\n4. sec:appendix-n5\n5. sec:appendix-stats\n6. sec:appendix-llama\n7. sec:appendix-viz\n8. sec:appendix-steering (subsection within viz)\n9. sec:appendix-gate-profile\n10. sec:appendix-ss\n11. sec:appendix-cost\n12. sec:appendix-examples\n13. sec:appendix-gradient\n14. sec:appendix-data\n15. sec:appendix-eb-scaling\n16. sec:appendix-ar-gar-dynamics\n17. sec:appendix-kl\n18. sec:appendix-gar-robust\n19. sec:appendix-mmlu\n20. sec:appendix-1.5b\n21. sec:appendix-perseed\n22. sec:appendix-perturn-detail\n23. sec:appendix-dataset-ext\n24. sec:appendix-gar-ext\n25. sec:appendix-mmlu-ext\n26. sec:appendix-1.5b-ext\n27. sec:appendix-stats-ext\n28. sec:appendix-training-ext\n29. sec:appendix-steering-viz\n30. sec:appendix-llama-ss\n31. sec:appendix-ai\n\nFor each label, grep in ALL the main text .tex files (NOT appendix.tex) to find if it's referenced. Report:\n- REFERENCED: which file and what context\n- NOT REFERENCED: orphan appendix\n\nBe thorough - check every single label. Report a clean list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d18fe314-4818-4a9a-a50f-9716df688a8a",
  "isSidechain": false,
  "requestId": "req_011CbP2E8FchzSKtSWCzmCFv",
  "type": "assistant",
  "uuid": "c0bd8e47-9f9a-4d34-bb0f-ed3727e93348",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ubDQVVjirULizCVzxXM25",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5470,
      "cache_read_input_tokens": 161158,
      "output_tokens": 670,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5470,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 670,
          "cache_read_input_tokens": 161158,
          "cache_creation_input_tokens": 5470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5470
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

_source line 1101 · 2026-05-25T09:08:32.807Z_

<details><summary>↩ Tool result · `toolu_01W747LaAEKfRqCEKANR7Vch`</summary>

```text
Here is the complete report.

---

## Appendix Label Reference Audit

### REFERENCED from main text (20 labels)

| # | Label | Referenced in | Context |
|---|-------|--------------|---------|
| 1 | `sec:appendix-hyper` | method.tex:59, experiments.tex:6 | "Appendix~\ref{sec:appendix-hyper}" for training config |
| 2 | `sec:appendix-loss` | method.tex:47, method.tex:55 | Loss formulation search (2 refs) |
| 3 | `sec:appendix-ir` | experiments.tex:27, discussion.tex:5 | Instruction retention details |
| 4 | `sec:appendix-n5` | experiments.tex:38 | Long-conversation evaluation |
| 5 | `sec:appendix-stats` | experiments.tex:12 | Statistical test details |
| 6 | `sec:appendix-llama` | analysis.tex:32, analysis.tex:34 | Llama complete results (2 refs) |
| 7 | `sec:appendix-viz` | analysis.tex:32 | Additional visualizations (gate convergence) |
| 8 | `sec:appendix-steering` | experiments.tex:27 | Full attention steering results |
| 9 | `sec:appendix-gate-profile` | analysis.tex:7 | Per-layer gate profile |
| 10 | `sec:appendix-ss` | experiments.tex:38 | Scheduled sampling implementation |
| 11 | `sec:appendix-cost` | experiments.tex:6 | Computational cost analysis |
| 12 | `sec:appendix-examples` | experiments.tex:27 | Qualitative steering examples |
| 13 | `sec:appendix-gradient` | analysis.tex:11, analysis.tex:13 | Gradient conflict analysis (2 refs) |
| 14 | `sec:appendix-data` | experiments.tex:6 | Training data characteristics |
| 15 | `sec:appendix-eb-scaling` | analysis.tex:17 | Exposure bias scaling analysis |
| 16 | `sec:appendix-kl` | discussion.tex:3 | Per-head KL divergence analysis |
| 17 | `sec:appendix-gar-robust` | experiments.tex:38 | GAR definition robustness |
| 18 | `sec:appendix-mmlu` | experiments.tex:12 | MMLU general capability preservation |
| 19 | `sec:appendix-1.5b` | analysis.tex:34 | Cross-scale validation (Qwen-2.5-1.5B) |
| 20 | `sec:appendix-perseed` | experiments.tex:38 | Per-seed detailed results |

### NOT REFERENCED from main text -- ORPHAN (11 labels)

| # | Label | Section title | Notes |
|---|-------|--------------|-------|
| 16 | `sec:appendix-ar-gar-dynamics` | Per-Turn AR GAR Dynamics | Only defined in appendix.tex:500 |
| 22 | `sec:appendix-perturn-detail` | Per-Turn GAR Decay Analysis | Only self-referenced within appendix (line 768 refs itself) |
| 23 | `sec:appendix-dataset-ext` | Extended Dataset Statistics | Only defined in appendix.tex:669 |
| 24 | `sec:appendix-gar-ext` | Extended GAR Robustness Analysis | Only defined in appendix.tex:681 |
| 25 | `sec:appendix-mmlu-ext` | MMLU Category Breakdown | Only defined in appendix.tex:698 |
| 26 | `sec:appendix-1.5b-ext` | Extended Cross-Scale Results (Qwen-2.5-1.5B) | Only defined in appendix.tex:717 |
| 27 | `sec:appendix-stats-ext` | Extended Statistical Analysis | Only self-referenced within appendix |
| 28 | `sec:appendix-training-ext` | Extended Training Dynamics | Only defined in appendix.tex:747 |
| 29 | `sec:appendix-steering-viz` | Per-beta Steering Visualization | Only cross-referenced from within appendix (line 491) |
| 30 | `sec:appendix-llama-ss` | Llama-3.1-8B Scheduled Sampling Details | Only defined in appendix.tex:785 |
| 31 | `sec:appendix-ai` | Use of AI Assistants | Only defined in appendix.tex:835 |

**Summary**: 20 of 31 appendix labels are referenced from the main text. **11 are orphans** -- never referenced from any main text file. Of those 11, a few (`perturn-detail`, `stats-ext`, `steering-viz`) are cross-referenced from other appendix sections but still have no main-text entry point. The rest (`ar-gar-dynamics`, `dataset-ext`, `gar-ext`, `mmlu-ext`, `1.5b-ext`, `training-ext`, `llama-ss`, `ai`) are completely unreferenced even within the appendix.

agentId: a8ac7bf6e07688487 (use SendMessage with to: 'a8ac7bf6e07688487' to continue this agent)
&lt;usage>total_tokens: 48684
tool_uses: 60
duration_ms: 97432&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c0bd8e47-9f9a-4d34-bb0f-ed3727e93348",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "5a0d5b3a-2e72-41cb-a19c-b545002b1435",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to check which appendix section labels are referenced from the main text of a paper. \n\nThe appendix is at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex\n\nThe main text sections are these files (NOT appendix.tex):\n- abstract.tex\n- introduction.tex  \n- method.tex\n- related_work.tex\n- experiments.tex\n- analysis.tex\n- discussion.tex\n- conclusion.tex\n- limitations.tex\n\nAll in: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/\n\nHere are ALL the appendix section labels to check:\n1. sec:appendix-hyper\n2. sec:appendix-loss\n3. sec:appendix-ir\n4. sec:appendix-n5\n5. sec:appendix-stats\n6. sec:appendix-llama\n7. sec:appendix-viz\n8. sec:appendix-steering (subsection within viz)\n9. sec:appendix-gate-profile\n10. sec:appendix-ss\n11. sec:appendix-cost\n12. sec:appendix-examples\n13. sec:appendix-gradient\n14. sec:appendix-data\n15. sec:appendix-eb-scaling\n16. sec:appendix-ar-gar-dynamics\n17. sec:appendix-kl\n18. sec:appendix-gar-robust\n19. sec:appendix-mmlu\n20. sec:appendix-1.5b\n21. sec:appendix-perseed\n22. sec:appendix-perturn-detail\n23. sec:appendix-dataset-ext\n24. sec:appendix-gar-ext\n25. sec:appendix-mmlu-ext\n26. sec:appendix-1.5b-ext\n27. sec:appendix-stats-ext\n28. sec:appendix-training-ext\n29. sec:appendix-steering-viz\n30. sec:appendix-llama-ss\n31. sec:appendix-ai\n\nFor each label, grep in ALL the main text .tex files (NOT appendix.tex) to find if it's referenced. Report:\n- REFERENCED: which file and what context\n- NOT REFERENCED: orphan appendix\n\nBe thorough - check every single label. Report a clean list.",
    "agentId": "a8ac7bf6e07688487",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete report.\n\n---\n\n## Appendix Label Reference Audit\n\n### REFERENCED from main text (20 labels)\n\n| # | Label | Referenced in | Context |\n|---|-------|--------------|---------|\n| 1 | `sec:appendix-hyper` | method.tex:59, experiments.tex:6 | \"Appendix~\\ref{sec:appendix-hyper}\" for training config |\n| 2 | `sec:appendix-loss` | method.tex:47, method.tex:55 | Loss formulation search (2 refs) |\n| 3 | `sec:appendix-ir` | experiments.tex:27, discussion.tex:5 | Instruction retention details |\n| 4 | `sec:appendix-n5` | experiments.tex:38 | Long-conversation evaluation |\n| 5 | `sec:appendix-stats` | experiments.tex:12 | Statistical test details |\n| 6 | `sec:appendix-llama` | analysis.tex:32, analysis.tex:34 | Llama complete results (2 refs) |\n| 7 | `sec:appendix-viz` | analysis.tex:32 | Additional visualizations (gate convergence) |\n| 8 | `sec:appendix-steering` | experiments.tex:27 | Full attention steering results |\n| 9 | `sec:appendix-gate-profile` | analysis.tex:7 | Per-layer gate profile |\n| 10 | `sec:appendix-ss` | experiments.tex:38 | Scheduled sampling implementation |\n| 11 | `sec:appendix-cost` | experiments.tex:6 | Computational cost analysis |\n| 12 | `sec:appendix-examples` | experiments.tex:27 | Qualitative steering examples |\n| 13 | `sec:appendix-gradient` | analysis.tex:11, analysis.tex:13 | Gradient conflict analysis (2 refs) |\n| 14 | `sec:appendix-data` | experiments.tex:6 | Training data characteristics |\n| 15 | `sec:appendix-eb-scaling` | analysis.tex:17 | Exposure bias scaling analysis |\n| 16 | `sec:appendix-kl` | discussion.tex:3 | Per-head KL divergence analysis |\n| 17 | `sec:appendix-gar-robust` | experiments.tex:38 | GAR definition robustness |\n| 18 | `sec:appendix-mmlu` | experiments.tex:12 | MMLU general capability preservation |\n| 19 | `sec:appendix-1.5b` | analysis.tex:34 | Cross-scale validation (Qwen-2.5-1.5B) |\n| 20 | `sec:appendix-perseed` | experiments.tex:38 | Per-seed detailed results |\n\n### NOT REFERENCED from main text -- ORPHAN (11 labels)\n\n| # | Label | Section title | Notes |\n|---|-------|--------------|-------|\n| 16 | `sec:appendix-ar-gar-dynamics` | Per-Turn AR GAR Dynamics | Only defined in appendix.tex:500 |\n| 22 | `sec:appendix-perturn-detail` | Per-Turn GAR Decay Analysis | Only self-referenced within appendix (line 768 refs itself) |\n| 23 | `sec:appendix-dataset-ext` | Extended Dataset Statistics | Only defined in appendix.tex:669 |\n| 24 | `sec:appendix-gar-ext` | Extended GAR Robustness Analysis | Only defined in appendix.tex:681 |\n| 25 | `sec:appendix-mmlu-ext` | MMLU Category Breakdown | Only defined in appendix.tex:698 |\n| 26 | `sec:appendix-1.5b-ext` | Extended Cross-Scale Results (Qwen-2.5-1.5B) | Only defined in appendix.tex:717 |\n| 27 | `sec:appendix-stats-ext` | Extended Statistical Analysis | Only self-referenced within appendix |\n| 28 | `sec:appendix-training-ext` | Extended Training Dynamics | Only defined in appendix.tex:747 |\n| 29 | `sec:appendix-steering-viz` | Per-beta Steering Visualization | Only cross-referenced from within appendix (line 491) |\n| 30 | `sec:appendix-llama-ss` | Llama-3.1-8B Scheduled Sampling Details | Only defined in appendix.tex:785 |\n| 31 | `sec:appendix-ai` | Use of AI Assistants | Only defined in appendix.tex:835 |\n\n**Summary**: 20 of 31 appendix labels are referenced from the main text. **11 are orphans** -- never referenced from any main text file. Of those 11, a few (`perturn-detail`, `stats-ext`, `steering-viz`) are cross-referenced from other appendix sections but still have no main-text entry point. The rest (`ar-gar-dynamics`, `dataset-ext`, `gar-ext`, `mmlu-ext`, `1.5b-ext`, `training-ext`, `llama-ss`, `ai`) are completely unreferenced even within the appendix."
      }
    ],
    "totalDurationMs": 97432,
    "totalTokens": 48684,
    "totalToolUseCount": 60,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4603,
      "cache_read_input_tokens": 42788,
      "output_tokens": 1292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4603
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1292,
          "cache_read_input_tokens": 42788,
          "cache_creation_input_tokens": 4603,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4603,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 9,
      "searchCount": 51,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "c0bd8e47-9f9a-4d34-bb0f-ed3727e93348",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1102 · 2026-05-25T09:08:32.816Z_

```json
{
  "parentUuid": "5a0d5b3a-2e72-41cb-a19c-b545002b1435",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2d476325-089d-48d5-af50-9a674ec4b255",
  "timestamp": "2026-05-25T09:08:32.816Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---


### Runtime record

_source line 1103_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 附录内容引用完整性检查  **任务：** 检查论文附录的所有内容是否在正文中都有准确、合理的引用，修复孤儿附录。  **Step 1：逐项盘点** 列出附录里每一个 section/subsection/table/figure/algorithm/proof/prompt。  **Step 2：逐项验证引用** 对每一项，在正文搜索是否有至少一句话指向…",
  "leafUuid": "2d476325-089d-48d5-af50-9a674ec4b255",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1104_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### System

_source line 1105 · 2026-05-25T09:10:08.572Z_

```json
{
  "parentUuid": null,
  "logicalParentUuid": "2d476325-089d-48d5-af50-9a674ec4b255",
  "isSidechain": false,
  "type": "system",
  "subtype": "compact_boundary",
  "content": "Conversation compacted",
  "isMeta": false,
  "timestamp": "2026-05-25T09:10:08.572Z",
  "uuid": "e004b6c4-d990-4ae4-9299-95ef15f2b19f",
  "level": "info",
  "compactMetadata": {
    "trigger": "auto",
    "preTokens": 168829,
    "preCompactDiscoveredTools": [
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_registry"
    ],
    "postTokens": 8055,
    "durationMs": 95753
  },
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---


## Round 30

## Round 30

104 recorded events


### User

_source line 1106 · 2026-05-25T09:10:08.573Z_

This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.

Summary:
1. Primary Request and Intent:
   This session continues Paper Agent work for the "turn_residual_gating" EMNLP 2026 paper. Four Director instructions were handled:
   - **Task B completion**: Finish data audit remnants (regenerate fig1, compile, report)
   - **Task C**: Normalize anonymous repo link (add GitHub footnote in Abstract, remove old link from Intro)
   - **Round 5 review patches**: 8 writing modifications addressing reviewer feedback (title change, exposure bias hedging, split-softmax/Rhea comparison, β-steering decomposition, GAR-ours rationale, PCGrad scope, number redundancy, LoRA rank)
   - **Appendix cross-reference audit**: Catalog all appendix content, verify each has a proper main-text reference, fix orphans

2. Key Technical Concepts:
   - Paper Agent communicates via `paper_agent_post_to_director` (NOT `main_agent_post_to_director`)
   - EMNLP 2026: 8-page main text limit (Limitations/References/Appendix excluded)
   - LaTeX page fitting: `\looseness=-1/-2`, `\enlargethispage{\baselineskip}` for micro-adjustments
   - Exposure bias hedging: "the proximal cause" → "a proximal cause consistent with current evidence"
   - PCGrad scope: "gradient conflict" → "gradient direction conflict" (excludes magnitude imbalance)
   - β-steering decomposition: GAR recovery is "by construction" (tautological) vs downstream instruction retention (p=0.077, not significant)
   - Appendix orphan detection: 31 appendix labels, 20 referenced from main text, 11 orphans

3. Files and Code Sections:

   - **paper/main.tex** (line 22)
     - Title changed from "Destroys" to "Collapses"
     ```latex
     \title{Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue}
     ```

   - **paper/sections/abstract.tex**
     - Added repo footnote at end of abstract
     ```latex
     ...generalizing across architectures and seeds.\footnote{Code and data: \url{https://github.com/anonymous-nlp-2026/turn_residual_gating}.}
     ```

   - **paper/sections/introduction.tex**
     - Removed old repo link from line 18
     - "destroys" → "collapses" in fig1 caption
     - "root cause" → "primary contributing factor"
     - "the proximal cause" → "a proximal cause" (contributions list)
     - "gradient conflict" → "gradient direction conflict" (3 places)
     - "8--17× on Qwen and 27× on Llama" → "an order of magnitude on both architectures"
     - "(8--27× gap...)" → "(order-of-magnitude gap...)"

   - **paper/sections/experiments.tex**
     - §4.3 caption: "the proximal cause" → "a proximal cause"
     - §4.3 body: completely rewritten β-steering paragraph:
     ```latex
     GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does---consistent with attention misallocation as a proximal cause consistent with current evidence (qualitative examples in Appendix~\ref{sec:appendix-examples}). Downstream, steering ($\beta$\,=\,3) raises late-turn instruction compliance by +11.1\,pp, though this effect does not reach conventional significance ($p$\,=\,0.077; content-constrained tasks benefit most, +23.8\,pp; Appendix~\ref{sec:appendix-ir}).
     ```

   - **paper/sections/analysis.tex**
     - §5 header: "gradient conflict" → "gradient direction conflict"
     - §5.2 title: "PCGrad Gradient Direction Conflict Exclusion"
     - §5.2 body: replaced magnitude dominance sentence with side-effects acknowledgment:
     ```latex
     PCGrad eliminates direction conflict but does not address magnitude imbalance (NTP dominates GAR by 7.5--14.7$\times$); the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor.
     ```
     - §5.5: removed redundant "(8--17× on Qwen, 27× on Llama)"

   - **paper/sections/discussion.tex**
     - KV cache drift expanded with switching experiment:
     ```latex
     Our exclusion identifies exposure bias as a primary contributing factor consistent with all current evidence, but we cannot fully rule out a secondary role for KV cache drift, where accumulated generation errors alter the key-value representations fed to subsequent turns. A switching experiment---training with scheduled sampling but evaluating with ground-truth KV cache---could disentangle the two mechanisms; we leave this to future work.
     ```
     - Added split-softmax/Rhea comparison paragraph
     - Removed duplicate downstream steering result (+11.1pp)
     - "8--27×" → "an order of magnitude"
     - Added `\looseness=-1` to both paragraphs

   - **paper/sections/conclusion.tex**
     - Tightened text, added hedging, `\enlargethispage{\baselineskip}`:
     ```latex
     \enlargethispage{\baselineskip}
     \section{Conclusion}\label{sec:conclusion}
     
     \looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\,=\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\sim}$1.3$\times$ (Qwen) and ${\sim}$2.9$\times$ (Llama), generalizing across architectures and seeds---the first such transfer to auxiliary attention objectives in multi-turn transformers.
     ```

   - **paper/sections/method.tex**
     - §3.1 added GAR-ours vs GAR-D rationale after GAR-ours definition:
     ```latex
     Empirically, GAR-Dongre is diluted by NTP attention patterns to ${\sim}$0.01--0.02 in multi-turn settings, losing discriminative power across configurations; GAR-ours retains an order-of-magnitude range (0.019--0.50). The contrast itself is informative: goal attention concentrates at the last-token position, and only this concentrated pattern is vulnerable to distribution shift (\S\ref{sec:analysis}).
     ```

   - **paper/sections/related_work.tex**
     - "conflict is a symptom, not the cause" → "direction conflict is a symptom, not the primary cause"

   - **paper/sections/limitations.tex**
     - LoRA rank sentence updated:
     ```latex
     LoRA rank is fixed at 16 throughout; higher ranks (32/64) might provide more capacity for the gating mechanism, potentially affecting the magnitude of the TF-AR gap, though unlikely its direction given the consistency across all five configurations.
     ```

   - **paper/sections/appendix.tex**
     - "gradient conflict is not the root cause" → "gradient direction conflict is not the primary cause"
     - Full appendix read (847 lines) for cross-reference audit
     - 31 labeled sections/subsections identified, 11 orphans found

   - **figures/paper/gen_fig1_3panel.py** — regenerated with 12.5× fix (from prior session edit)

4. Errors and Fixes:
   - **Page overflow after Round 5 patches**: Adding text to Discussion (split-softmax/Rhea, KV cache drift expansion) pushed Conclusion to page 9. Fixed through iterative tightening:
     1. Removed duplicate downstream result from Discussion
     2. Compressed split-softmax/Rhea paragraph with `\looseness=-1`
     3. Tightened Conclusion wording
     4. Added `\enlargethispage{\baselineskip}` before Conclusion
     5. Multiple compile-render-check cycles until Conclusion fit on page 8
   - **`\looseness=-2` ineffective**: Short paragraph couldn't be compressed by 2 lines; switched to `\enlargethispage` approach
   - **System reminders about `main_agent_post_to_director`**: Correctly ignored — Paper Agent uses `paper_agent_post_to_director` which was already called

5. Problem Solving:
   - All 8 Round 5 reviewer patches successfully applied with page limit preserved
   - Appendix audit completed (Step 1-2: inventory and verification). Step 3 (fixing orphans) is pending
   - Task B and Task C from prior session fully completed and reported to Director

6. All User Messages:
   - "Continue from where you left off." (resuming after context break)
   - "[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果..." (system reminder ×4 — Paper Agent correctly uses paper_agent_post_to_director instead)
   - "[Director 指令] [Patch] Round 5 审稿后写作修改（批量）" — 8 specific patches with detailed instructions for each
   - "Continue from where you left off." (after context break)
   - "[Director 指令] [Patch] 附录内容引用完整性检查" — audit all appendix content for proper main-text references, fix orphans, compile PDF, report

7. Pending Tasks:
   - **Appendix audit Step 3**: Fix the 11 orphan appendix sections by adding natural references in the most relevant main-text sections. The orphans are:
     1. `sec:appendix-ar-gar-dynamics` — Per-Turn AR GAR Dynamics
     2. `sec:appendix-perturn-detail` — Per-Turn GAR Decay Analysis
     3. `sec:appendix-dataset-ext` — Extended Dataset Statistics
     4. `sec:appendix-gar-ext` — Extended GAR Robustness Analysis
     5. `sec:appendix-mmlu-ext` — MMLU Category Breakdown
     6. `sec:appendix-1.5b-ext` — Extended Cross-Scale Results (1.5B)
     7. `sec:appendix-stats-ext` — Extended Statistical Analysis
     8. `sec:appendix-training-ext` — Extended Training Dynamics
     9. `sec:appendix-steering-viz` — Per-β Steering Visualization
     10. `sec:appendix-llama-ss` — Llama SS Details
     11. `sec:appendix-ai` — Use of AI Assistants
   - Compile PDF after fixes
   - Report to Director: (a) appendix inventory (b) which were orphaned and where references were added (c) whether any were deleted

8. Current Work:
   Working on the Director's appendix cross-reference audit instruction. Steps 1-2 (inventory and verification) are complete. The agent found 31 appendix labels total, 20 properly referenced from main text, 11 orphans. Step 3 (fixing orphans by adding natural references in the most relevant main-text sections) has NOT been started yet. No edits have been made to fix the orphans. After fixing, need to compile PDF and report to Director.

9. Optional Next Step:
   Execute Step 3 of the appendix audit: For each of the 11 orphan appendix sections, add a natural cross-reference in the most relevant main-text section. The Director's instruction states:
   - "优选：在最相关的正文章节加一句自然引用，说明为什么读者要翻那里、能找到什么"
   - "次选：若附录内容对核心 claim 不必要且找不到合适引用位置，删除该附录内容"
   - "禁止：在章节末尾硬塞 'See Appendix X.' 作为补丁"
   
   Then compile PDF and report via `paper_agent_post_to_director`.

If you need specific details from before compaction (like exact code snippets, error messages, or content you generated), read the full transcript at: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58.jsonl
Continue the conversation from where it left off without asking the user any further questions. Resume directly — do not acknowledge the summary, do not recap what was happening, do not preface with "I'll continue" or similar. Pick up the last task as if the break never happened.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e004b6c4-d990-4ae4-9299-95ef15f2b19f",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "isVisibleInTranscriptOnly": true,
  "isCompactSummary": true,
  "uuid": "f7f944ba-4192-41d8-929a-4a33f0d84b17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1107 · 2026-05-25T09:10:08.323Z_

```json
{
  "parentUuid": "f7f944ba-4192-41d8-929a-4a33f0d84b17",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex",
        "content": "\\enlargethispage{\\baselineskip}\n\\section{Conclusion}\\label{sec:conclusion}\n\n\\looseness=-1 Auxiliary attention losses converge under teacher forcing (GAR\\,=\\,0.50) but collapse by an order of magnitude under autoregressive generation on two architectures. A five-way diagnostic comparison identifies exposure bias as a primary contributing factor; $\\beta$-steering recovers GAR above the TF baseline, confirming attention misallocation as a proximal cause (KV cache drift remains untested). Scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama), generalizing across architectures and seeds---the first such transfer to auxiliary attention objectives in multi-turn transformers.\n",
        "numLines": 5,
        "startLine": 1,
        "totalLines": 5
      }
    },
    "displayPath": "../../../paper/sections/conclusion.tex"
  },
  "type": "attachment",
  "uuid": "41cd96c2-e562-46d4-bead-7b665a4b29d2",
  "timestamp": "2026-05-25T09:10:08.323Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---


### Runtime record

_source line 1108 · 2026-05-25T09:10:08.325Z_

```json
{
  "parentUuid": "41cd96c2-e562-46d4-bead-7b665a4b29d2",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex",
        "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\looseness=-1 The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP self-recovers because prediction is the same task at both regimes \\citep{he2019exposure}; GAR optimizes a \\emph{global property}---attention allocation to goal tokens---that has no autoregressive counterpart. The collapse is selective: GAR-ours (last-token) collapses by an order of magnitude while GAR-Dongre (all-token) shows negligible shift (${\\leq}$1.3$\\times$), implying the concentrated attention pattern is brittle under distribution shift. Per-head analysis confirms: heads with higher TF GAR shift most under AR generation ($r$\\,=\\,0.743; Appendix~\\ref{sec:appendix-kl}). Any auxiliary attention objective paired with teacher forcing should face the same barrier when targeting distributional properties rather than the prediction itself.\n\n\\looseness=-1 Our exclusion identifies exposure bias as a primary contributing factor consistent with all current evidence, but we cannot fully rule out a secondary role for KV cache drift, where accumulated generation errors alter the key-value representations fed to subsequent turns. A switching experiment---training with scheduled sampling but evaluating with ground-truth KV cache---could disentangle the two mechanisms; we leave this to future work. The PCGrad exclusion rules out gradient direction conflict but not magnitude imbalance (NTP dominance 7.5--14.7$\\times$, 25.7$\\times$ on Llama; \\citealp{chen2018gradnorm}). The overall GAR--compliance correlation is weak ($r$\\,=\\,0.200, $r^2$\\,=\\,0.04; Appendix~\\ref{sec:appendix-ir}), reinforcing GAR's role as a diagnostic probe rather than a direct optimization target.\n\n\\looseness=-1 Our $\\beta$-steering differs from inference-time remedies such as split-softmax \\citep{li2024measuring}, which separates instruction and conversation softmax domains, and Rhea \\citep{hong2025rhea}, which applies role-aware episodic attention. $\\beta$-steering is a \\emph{diagnostic} tool that confirms attention as the causal channel, not a production-ready strategy. SS and inference-time fixes offer complementary trade-offs: SS modifies internal representations so AR attention transfers without inference cost; inference-time methods leave training unchanged but cannot recover patterns the model never learned. At $\\beta$\\,=\\,5 the two converge (SS GAR\\,=\\,0.717 vs.\\ TG\\,=\\,0.727). SS is preferable when inference budgets are tight, steering when retraining is infeasible.\n",
        "numLines": 8,
        "startLine": 1,
        "totalLines": 8
      }
    },
    "displayPath": "../../../paper/sections/discussion.tex"
  },
  "type": "attachment",
  "uuid": "e3cac170-6d91-4d55-ac6a-ba281de2985d",
  "timestamp": "2026-05-25T09:10:08.325Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---


### Runtime record

_source line 1109 · 2026-05-25T09:10:08.324Z_

```json
{
  "parentUuid": "e3cac170-6d91-4d55-ac6a-ba281de2985d",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
        "content": "\\section{Introduction}\\label{sec:introduction}\n\nMulti-turn dialogue is central to how large language models are deployed, yet a persistent failure accompanies even the most fluent generation: as conversations grow longer, models pay progressively less attention to the system-prompt goals that define their task. \\citet{dongre2026attention} measured 27--48\\% Goal Accessibility Ratio (GAR) decline across 12 models over 50 turns, even as residual stream probes confirm that goal representations persist (AUC\\,=\\,0.98). This is not just a measurement artifact---exploratory evaluation suggests it can degrade instruction compliance by up to 24 percentage points on content-constrained tasks (\\S\\ref{sec:discussion}).\n\nExisting remedies address this decay at inference time. Split-softmax \\citep{li2024measuring} separates instruction from conversation tokens; StreamingLLM \\citep{xiao2024streaming} retains anchor tokens; Gated Attention \\citep{qiu2025gated} applies per-head sigmoid gates within a single forward pass. None of these intervenes during training. A natural alternative is to optimize goal attention directly through auxiliary attention losses trained alongside next-token prediction (NTP). Yet this strategy rests on an untested assumption: that attention patterns learned under teacher forcing transfer to autoregressive generation. Classical exposure bias research \\citep{bengio2015scheduled,lamb2016professor} has shown that teacher forcing creates a training--inference mismatch for RNN sequence models, but whether this mismatch extends to auxiliary attention objectives in multi-turn transformers remains unknown.\n\nWe test this assumption. We introduce ThreadGate, per-layer content-and-turn-conditioned gates on the residual stream ($x_{l+1} = x_l + g_l \\cdot f_l(x_l)$), designed not as a solution but as a controlled testbed for isolating failure mechanisms. A five-way comparison (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base) forms a causal exclusion chain (\\S\\ref{sec:comparison-design}): each adjacent pair rules out one alternative hypothesis---turn conditioning, gating mechanism, gradient direction conflict---tracing the failure to its primary contributing factor.\n\n\\begin{figure*}[t]\n  \\centering\n  \\includegraphics[width=\\textwidth]{fig1_headline.pdf}\n  \\caption{Exposure bias collapses auxiliary attention losses. \\textbf{(a)}~Goal attention decays 85--90\\% across turns under AR generation on both Qwen-2.5-7B and Llama-3.1-8B. \\textbf{(b)}~Under TF evaluation all variants reach GAR$\\approx$0.50, but AR generation collapses GAR by 8--17$\\times$ (log scale). \\textbf{(c)}~Scheduled sampling compresses the TF--AR gap from 7.8$\\times$ to 1.3$\\times$ (Qwen) and ${\\sim}$27$\\times$ to 2.9$\\times$ (Llama).}\n  \\label{fig:headline}\n\\end{figure*}\n\nTraining succeeds but inference fails. All variants converge to TF GAR\\,=\\,0.50, yet under AR generation GAR collapses by an order of magnitude on both architectures (Figure~\\ref{fig:headline}). The causal exclusion identifies exposure bias as the primary contributing factor: PCGrad removes gradient direction conflict yet \\emph{worsens} AR GAR ($p$\\,=\\,0.002); gating provides no benefit over LoRA-only. Steering ($\\beta$\\,=\\,5) recovers GAR to 0.727, confirming attention misallocation; scheduled sampling compresses the gap to ${\\sim}$1.3$\\times$ (Qwen) and ${\\sim}$2.9$\\times$ (Llama) with no perplexity cost.\n\nOur contributions: (1)~the first empirical characterization of exposure bias on auxiliary attention losses (order-of-magnitude gap across two architectures and scales); (2)~a five-way diagnostic testbed informed by seven loss iterations, enabling causal exclusion of gradient direction conflict via PCGrad ($p$\\,=\\,0.002, effect reverses); (3)~$\\beta$-steering confirms attention misallocation as a proximal cause; (4)~scheduled sampling compresses the gap to 1.3--2.9$\\times$, the first transfer to auxiliary attention objectives in multi-turn transformers ($0.401\\pm0.047$, three seeds).\n",
        "numLines": 19,
        "startLine": 1,
        "totalLines": 19
      }
    },
    "displayPath": "../../../paper/sections/introduction.tex"
  },
  "type": "attachment",
  "uuid": "de01ddd3-c086-4fb8-bdbb-ecc98e439126",
  "timestamp": "2026-05-25T09:10:08.324Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---


### Runtime record

_source line 1110 · 2026-05-25T09:10:08.325Z_

```json
{
  "parentUuid": "de01ddd3-c086-4fb8-bdbb-ecc98e439126",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex",
        "content": "\\section{Limitations}\\label{sec:limitations}\n\nOur findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B) and a single dataset (UltraChat, 8K conversations); generalization to other domains (e.g., code, reasoning) is untested. Most configurations use a single seed (scheduled sampling validated on three seeds; \\S\\ref{subsec:ss}), and quality assessment relies on PPL rather than comprehensive benchmarks \\citep{hendrycks2021measuring,lin2022truthfulqa}. LoRA rank is fixed at 16 throughout; higher ranks (32/64) might provide more capacity for the gating mechanism, potentially affecting the magnitude of the TF-AR gap, though unlikely its direction given the consistency across all five configurations. We test only one auxiliary loss family (GAR with MSE target $\\tau$\\,=\\,0.5); head-specific or layer-specific losses may exhibit different sensitivity to exposure bias. We do not experimentally compare against split-softmax \\citep{li2024measuring} or Rhea \\citep{hong2025rhea}, which operate at inference time; such comparisons would clarify the practical trade-off between training-time and inference-time interventions. The PCGrad exclusion addresses gradient conflict only; magnitude imbalance \\citep{chen2018gradnorm} and Nash equilibrium approaches \\citep{navon2022nash} remain untested.",
        "numLines": 3,
        "startLine": 1,
        "totalLines": 3
      }
    },
    "displayPath": "../../../paper/sections/limitations.tex"
  },
  "type": "attachment",
  "uuid": "276f9bab-1000-4cd3-bfc3-ce738066b137",
  "timestamp": "2026-05-25T09:10:08.325Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---


### Runtime record

_source line 1111 · 2026-05-25T09:10:08.568Z_

```json
{
  "parentUuid": "276f9bab-1000-4cd3-bfc3-ce738066b137",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
        "content": "\\section{Analysis}\\label{sec:analysis}\n\nEach subsection kills one alternative hypothesis via causal exclusion: \\S\\ref{subsec:gate-conditioning}~turn conditioning, \\S\\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\\S\\ref{subsec:dist-shift}). \\S\\ref{subsec:mechanism-specificity} confirms selectivity; \\S\\ref{subsec:cross-model} confirms cross-architecture generalization.\n\n\\subsection{Gate Turn Conditioning}\\label{subsec:gate-conditioning}\n\nWe compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \\emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \\times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \\citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\\% attenuation; Table~\\ref{tab:four-way}; full gate profiles in Appendix~\\ref{sec:appendix-gate-profile}). The Uniform Gate learns comparable per-layer variation (L3\\,=\\,0.777, L27\\,=\\,1.000) despite lacking turn conditioning, confirming the structure arises from LoRA$+$GAR pressure (Figure~\\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?\n\n\\subsection{PCGrad Gradient Direction Conflict Exclusion}\\label{subsec:pcgrad}\n\nNTP and GAR gradients oppose in 68--79\\% of layers (cosine similarity $-$0.089$\\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\\times$ to 14.7$\\times$ (full gradient statistics in Appendix~\\ref{sec:appendix-gradient}). If this direction conflict prevents GAR convergence, eliminating it via PCGrad \\citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \\emph{diagnostic} tool rather than an optimization method.\n\nPCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \\emph{worsens}: 0.064$\\to$0.030 ($p$\\,=\\,0.002; Figure~\\ref{fig:training-pcgrad}b in Appendix~\\ref{sec:appendix-gradient}). By \\emph{modus tollens}: removing gradient direction conflict does not prevent collapse; therefore it is not the primary cause. PCGrad eliminates direction conflict but does not address magnitude imbalance (NTP dominates GAR by 7.5--14.7$\\times$); the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\\,=\\,+0.005) with 25.7$\\times$ NTP magnitude dominance (Table~\\ref{tab:gradient-crossmodel}).\n\n\\subsection{Distribution Shift Analysis}\\label{subsec:dist-shift}\n\nThe TF-AR GAR gap persists across all variants (Table~\\ref{tab:four-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, confirming that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \\citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\\tau$\\,=\\,0.5 while AR GAR collapses (77--87\\% per-turn decay; Figure~\\ref{fig:attention-heatmap}; scaling analysis in Appendix~\\ref{sec:appendix-eb-scaling}).\n\n\\subsection{Mechanism Specificity}\\label{subsec:mechanism-specificity}\n\nWe test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\\times$) and Qwen (1.28$\\times$) vs.\\ the order-of-magnitude GAR-ours collapse.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_multiseed.pdf}\n  \\caption{Multi-seed AR GAR under scheduled sampling ($\\beta$\\,=\\,0 and $\\beta$\\,=\\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\\to$0.001).}\n  \\label{fig:ss-multiseed}\n\\end{figure}\n\n\\subsection{Cross-Model Replication}\\label{subsec:cross-model}\n\nWe replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\\,$>$\\,100\\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}). Gate profiles differ qualitatively (Figure~\\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\\,=\\,0.793) while Llama dips at late layers (L25\\,=\\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.\n\nScheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\\sim}$1.3$\\times$ likely due to fewer training epochs (2 vs.\\ 3). The phase transition is architecture-dependent: $\\beta$\\,=\\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\\beta$\\,=\\,5 (GAR 0.791, exceeding Qwen SS 0.717), suggesting deeper architectures need higher steering thresholds but ultimately provide more surface for attention reweighting (full results in Appendix~\\ref{sec:appendix-llama}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern: 79.8\\% GAR decay and $\\beta$-steering recovery to 0.715 (Appendix~\\ref{sec:appendix-1.5b}).\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig3_gate_shift.pdf}\n  \\caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \\times 10^{-8}$). (b)~Distribution shift ($N$\\,=\\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\\times$) exceed final $N$\\,=\\,50 estimates (8--17$\\times$; Table~\\ref{tab:four-way}) due to smaller sample size.}\n  \\label{fig:gate-shift}\n\\end{figure}",
        "numLines": 41,
        "startLine": 1,
        "totalLines": 41
      }
    },
    "displayPath": "../../../paper/sections/analysis.tex"
  },
  "type": "attachment",
  "uuid": "c2c2d438-a8bc-4f74-8752-42e3a659f09e",
  "timestamp": "2026-05-25T09:10:08.568Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---


### Runtime record

_source line 1112 · 2026-05-25T09:10:08.571Z_

```json
{
  "parentUuid": "c2c2d438-a8bc-4f74-8752-42e3a659f09e",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "704d9e25-334a-45aa-ad6c-ee8403b5ba95",
  "timestamp": "2026-05-25T09:10:08.571Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---


### Runtime record

_source line 1113 · 2026-05-25T09:10:08.571Z_

```json
{
  "parentUuid": "704d9e25-334a-45aa-ad6c-ee8403b5ba95",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "a386e8c1-b233-44fe-9778-16ae3cb1193f",
  "timestamp": "2026-05-25T09:10:08.571Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---


### Runtime record

_source line 1114 · 2026-05-25T09:10:08.571Z_

```json
{
  "parentUuid": "a386e8c1-b233-44fe-9778-16ae3cb1193f",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "0558701f-172b-43a3-ba83-e6c86fe04be1",
  "timestamp": "2026-05-25T09:10:08.571Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---


### Runtime record

_source line 1115_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 附录内容引用完整性检查  **任务：** 检查论文附录的所有内容是否在正文中都有准确、合理的引用，修复孤儿附录。  **Step 1：逐项盘点** 列出附录里每一个 section/subsection/table/figure/algorithm/proof/prompt。  **Step 2：逐项验证引用** 对每一项，在正文搜索是否有至少一句话指向…",
  "leafUuid": "f7f944ba-4192-41d8-929a-4a33f0d84b17",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1116_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Assistant

_source line 1117 · 2026-05-25T09:10:12.486Z_

<details><summary>Logged reasoning block</summary>

```text
I need to continue with Step 3 of the appendix audit: fixing the 11 orphan appendix sections by adding natural cross-references in the most relevant main-text sections. Let me first read the main text sections to find the best places to add references for each orphan.

Let me read the current state of the main text sections to find appropriate insertion points.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0558701f-172b-43a3-ba83-e6c86fe04be1",
  "isSidechain": false,
  "requestId": "req_011CbP2VDwLqRomHDVYHob5K",
  "type": "assistant",
  "uuid": "d43dcd28-bcfc-47f9-9603-49704cc03b8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtUYgNxfASjFcjuXD4igpC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31511,
      "cache_read_input_tokens": 11447,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31511,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 352,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 31511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31511
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

_source line 1118 · 2026-05-25T09:10:13.015Z_

Let me read the main text sections to find optimal insertion points for the 11 orphan appendix references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d43dcd28-bcfc-47f9-9603-49704cc03b8f",
  "isSidechain": false,
  "requestId": "req_011CbP2VDwLqRomHDVYHob5K",
  "type": "assistant",
  "uuid": "357a1c74-f486-4d74-98d9-50321dcd82c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtUYgNxfASjFcjuXD4igpC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31511,
      "cache_read_input_tokens": 11447,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31511,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 352,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 31511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31511
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

_source line 1119 · 2026-05-25T09:10:14.034Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AWMV1Ky1FESQjby6QrydyU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "357a1c74-f486-4d74-98d9-50321dcd82c4",
  "isSidechain": false,
  "requestId": "req_011CbP2VDwLqRomHDVYHob5K",
  "type": "assistant",
  "uuid": "3ef7b25e-614c-4f1d-b4bc-cffec2cb562d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtUYgNxfASjFcjuXD4igpC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31511,
      "cache_read_input_tokens": 11447,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31511,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 352,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 31511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31511
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

_source line 1120 · 2026-05-25T09:10:14.872Z_

<details><summary>↩ Tool result · `toolu_01KZwaTpMoU2QUfxQdnda5ig`</summary>

```text
1	\section{Analysis}\label{sec:analysis}
2	
3	Each subsection kills one alternative hypothesis via causal exclusion: \S\ref{subsec:gate-conditioning}~turn conditioning, \S\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms selectivity; \S\ref{subsec:cross-model} confirms cross-architecture generalization.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	We compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\% attenuation; Table~\ref{tab:four-way}; full gate profiles in Appendix~\ref{sec:appendix-gate-profile}). The Uniform Gate learns comparable per-layer variation (L3\,=\,0.777, L27\,=\,1.000) despite lacking turn conditioning, confirming the structure arises from LoRA$+$GAR pressure (Figure~\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?
8	
9	\subsection{PCGrad Gradient Direction Conflict Exclusion}\label{subsec:pcgrad}
10	
11	NTP and GAR gradients oppose in 68--79\% of layers (cosine similarity $-$0.089$\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\times$ to 14.7$\times$ (full gradient statistics in Appendix~\ref{sec:appendix-gradient}). If this direction conflict prevents GAR convergence, eliminating it via PCGrad \citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \emph{diagnostic} tool rather than an optimization method.
12	
13	PCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \emph{worsens}: 0.064$\to$0.030 ($p$\,=\,0.002; Figure~\ref{fig:training-pcgrad}b in Appendix~\ref{sec:appendix-gradient}). By \emph{modus tollens}: removing gradient direction conflict does not prevent collapse; therefore it is not the primary cause. PCGrad eliminates direction conflict but does not address magnitude imbalance (NTP dominates GAR by 7.5--14.7$\times$); the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\,=\,+0.005) with 25.7$\times$ NTP magnitude dominance (Table~\ref{tab:gradient-crossmodel}).
14	
15	\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
16	
17	The TF-AR GAR gap persists across all variants (Table~\ref{tab:four-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, confirming that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\tau$\,=\,0.5 while AR GAR collapses (77--87\% per-turn decay; Figure~\ref{fig:attention-heatmap}; scaling analysis in Appendix~\ref{sec:appendix-eb-scaling}).
18	
19	\subsection{Mechanism Specificity}\label{subsec:mechanism-specificity}
20	
21	We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\times$) and Qwen (1.28$\times$) vs.\ the order-of-magnitude GAR-ours collapse.
22	
23	\begin{figure}[t]
24	  \centering
25	  \includegraphics[width=\columnwidth]{fig_ss_multiseed.pdf}
26	  \caption{Multi-seed AR GAR under scheduled sampling ($\beta$\,=\,0 and $\beta$\,=\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\to$0.001).}
27	  \label{fig:ss-multiseed}
28	\end{figure}
29	
30	\subsection{Cross-Model Replication}\label{subsec:cross-model}
31	
32	We replicate on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\,=\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\,$>$\,100\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\times$ and 26$\times$ (Figure~\ref{fig:crossmodel}a in Appendix~\ref{sec:appendix-llama}). Gate profiles differ qualitatively (Figure~\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\,=\,0.793) while Llama dips at late layers (L25\,=\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.
33	
34	Scheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\sim}$27$\times$ to 2.9$\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\sim}$1.3$\times$ likely due to fewer training epochs (2 vs.\ 3). The phase transition is architecture-dependent: $\beta$\,=\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\beta$\,=\,5 (GAR 0.791, exceeding Qwen SS 0.717), suggesting deeper architectures need higher steering thresholds but ultimately provide more surface for attention reweighting (full results in Appendix~\ref{sec:appendix-llama}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern: 79.8\% GAR decay and $\beta$-steering recovery to 0.715 (Appendix~\ref{sec:appendix-1.5b}).
35	
36	\begin{figure}[t]
37	  \centering
38	  \includegraphics[width=\columnwidth]{fig3_gate_shift.pdf}
39	  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift ($N$\,=\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\times$) exceed final $N$\,=\,50 estimates (8--17$\times$; Table~\ref{tab:four-way}) due to smaller sample size.}
40	  \label{fig:gate-shift}
41	\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a84f1ae1-a456-46e5-864f-15b799a73155",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "95bd2982-13f8-4d20-9a4c-8814719566f8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
      "content": "\\section{Analysis}\\label{sec:analysis}\n\nEach subsection kills one alternative hypothesis via causal exclusion: \\S\\ref{subsec:gate-conditioning}~turn conditioning, \\S\\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\\S\\ref{subsec:dist-shift}). \\S\\ref{subsec:mechanism-specificity} confirms selectivity; \\S\\ref{subsec:cross-model} confirms cross-architecture generalization.\n\n\\subsection{Gate Turn Conditioning}\\label{subsec:gate-conditioning}\n\nWe compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \\emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \\times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \\citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\\% attenuation; Table~\\ref{tab:four-way}; full gate profiles in Appendix~\\ref{sec:appendix-gate-profile}). The Uniform Gate learns comparable per-layer variation (L3\\,=\\,0.777, L27\\,=\\,1.000) despite lacking turn conditioning, confirming the structure arises from LoRA$+$GAR pressure (Figure~\\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?\n\n\\subsection{PCGrad Gradient Direction Conflict Exclusion}\\label{subsec:pcgrad}\n\nNTP and GAR gradients oppose in 68--79\\% of layers (cosine similarity $-$0.089$\\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\\times$ to 14.7$\\times$ (full gradient statistics in Appendix~\\ref{sec:appendix-gradient}). If this direction conflict prevents GAR convergence, eliminating it via PCGrad \\citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \\emph{diagnostic} tool rather than an optimization method.\n\nPCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \\emph{worsens}: 0.064$\\to$0.030 ($p$\\,=\\,0.002; Figure~\\ref{fig:training-pcgrad}b in Appendix~\\ref{sec:appendix-gradient}). By \\emph{modus tollens}: removing gradient direction conflict does not prevent collapse; therefore it is not the primary cause. PCGrad eliminates direction conflict but does not address magnitude imbalance (NTP dominates GAR by 7.5--14.7$\\times$); the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\\,=\\,+0.005) with 25.7$\\times$ NTP magnitude dominance (Table~\\ref{tab:gradient-crossmodel}).\n\n\\subsection{Distribution Shift Analysis}\\label{subsec:dist-shift}\n\nThe TF-AR GAR gap persists across all variants (Table~\\ref{tab:four-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, confirming that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \\citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\\tau$\\,=\\,0.5 while AR GAR collapses (77--87\\% per-turn decay; Figure~\\ref{fig:attention-heatmap}; scaling analysis in Appendix~\\ref{sec:appendix-eb-scaling}).\n\n\\subsection{Mechanism Specificity}\\label{subsec:mechanism-specificity}\n\nWe test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\\times$) and Qwen (1.28$\\times$) vs.\\ the order-of-magnitude GAR-ours collapse.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_multiseed.pdf}\n  \\caption{Multi-seed AR GAR under scheduled sampling ($\\beta$\\,=\\,0 and $\\beta$\\,=\\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\\to$0.001).}\n  \\label{fig:ss-multiseed}\n\\end{figure}\n\n\\subsection{Cross-Model Replication}\\label{subsec:cross-model}\n\nWe replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\\,$>$\\,100\\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}). Gate profiles differ qualitatively (Figure~\\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\\,=\\,0.793) while Llama dips at late layers (L25\\,=\\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.\n\nScheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\\sim}$1.3$\\times$ likely due to fewer training epochs (2 vs.\\ 3). The phase transition is architecture-dependent: $\\beta$\\,=\\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\\beta$\\,=\\,5 (GAR 0.791, exceeding Qwen SS 0.717), suggesting deeper architectures need higher steering thresholds but ultimately provide more surface for attention reweighting (full results in Appendix~\\ref{sec:appendix-llama}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern: 79.8\\% GAR decay and $\\beta$-steering recovery to 0.715 (Appendix~\\ref{sec:appendix-1.5b}).\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig3_gate_shift.pdf}\n  \\caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \\times 10^{-8}$). (b)~Distribution shift ($N$\\,=\\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\\times$) exceed final $N$\\,=\\,50 estimates (8--17$\\times$; Table~\\ref{tab:four-way}) due to smaller sample size.}\n  \\label{fig:gate-shift}\n\\end{figure}",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  },
  "sourceToolAssistantUUID": "a84f1ae1-a456-46e5-864f-15b799a73155",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool result

_source line 1121 · 2026-05-25T09:10:14.042Z_

<details><summary>↩ Tool result · `toolu_01AWMV1Ky1FESQjby6QrydyU`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct with LoRA \citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; training costs in Appendix~\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\ref{sec:appendix-hyper}; dataset statistics in Appendix~\ref{sec:appendix-data}; the controlled comparison design is described in \S\ref{sec:comparison-design}. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \citep{dongre2026attention}, and perplexity (PPL).
7	
8	\subsection{Main Results}
9	
10	Table~\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\leq$2\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\leq$1\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, confirming that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\S\ref{subsec:ss}).
11	
12	Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\ LoRA-only is significant ($p$\,=\,0.004; Appendix~\ref{sec:appendix-stats}), yet the gap remains 7.8$\times$. A second seed confirms TF stability ($0.504\pm0.001$). MMLU 5-shot accuracy remains within 0.8\,pp across all variants (Appendix~\ref{sec:appendix-mmlu}). We analyze this distribution shift in \S\ref{sec:analysis}.
13	
14	\subsection{Inference-Time Attention Steering}\label{subsec:steering}
15	
16	\begin{figure}[t]
17	  \centering
18	  \includegraphics[width=\columnwidth]{fig5_attention_steering.pdf}
19	  \caption{Inference-time $\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation as a proximal cause (9\% PPL cost at $\beta$\,=\,3; phase transition at $\beta \in [2, 3]$).}
20	  \label{fig:steering-recovery}
21	\end{figure}
22	
23	All training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\beta$ to pre-softmax attention logits for goal-token positions during generation:
24	\begin{equation}
25	  \tilde{A}_{i,j}^{(\ell,h)} = A_{i,j}^{(\ell,h)} + \beta \cdot \mathbf{1}[j \in \mathcal{G}],
26	\end{equation}
27	where $\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\beta \in [0, 2]$ yields marginal improvement, then $\beta = 3$ triggers a phase transition to GAR\,=\,0.556 (9\% PPL cost). At $\beta$\,=\,5, GAR reaches 0.727$\pm$0.061 (PPL 1.77); the operating region $\beta \in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\ref{fig:steering-recovery}; full results in Appendix~\ref{sec:appendix-steering}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does---consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\ref{sec:appendix-examples}). Downstream, steering ($\beta$\,=\,3) raises late-turn instruction compliance by +11.1\,pp, though this effect does not reach conventional significance ($p$\,=\,0.077; content-constrained tasks benefit most, +23.8\,pp; Appendix~\ref{sec:appendix-ir}).
28	
29	\subsection{Scheduled Sampling Compresses the TF--AR Gap}\label{subsec:ss}
30	
31	\begin{figure}[t]
32	  \centering
33	  \includegraphics[width=\columnwidth]{fig_ss_gap_compression.pdf}
34	  \caption{Scheduled sampling compresses the TF-AR gap from 7.8$\times$ to ${\sim}$1.3$\times$, the only variant approaching parity across five training conditions.}
35	  \label{fig:ss-gap}
36	\end{figure}
37	
38	Scheduled sampling (SS; \citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\pm0.047$, compressing the gap from 7.8$\times$ to ${\sim}$1.3$\times$ (TF GAR $0.498\pm0.004$) with no PPL cost ($1.441\pm0.001$; Figure~\ref{fig:ss-gap}; per-seed details in Appendix~\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\beta$\,=\,5: $0.717\pm0.001$, std 0.047$\to$0.001; Figure~\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\ref{sec:appendix-gar-robust}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\sim}$27$\times$ to 2.9$\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\ 3; \S\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.
39	
40	
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ef7b25e-614c-4f1d-b4bc-cffec2cb562d",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "46184d63-2b4f-49e3-96c1-efe218b5dd6d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\nWe fine-tune Qwen-2.5-7B-Instruct with LoRA \\citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \\citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; training costs in Appendix~\\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\\ref{sec:appendix-hyper}; dataset statistics in Appendix~\\ref{sec:appendix-data}; the controlled comparison design is described in \\S\\ref{sec:comparison-design}. We evaluate under \\emph{IID} (same-distribution UltraChat text) and \\emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \\citep{dongre2026attention}, and perplexity (PPL).\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\\leq$2\\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\\leq$1\\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, confirming that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\\S\\ref{subsec:ss}).\n\nUnder AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendix~\\ref{sec:appendix-stats}), yet the gap remains 7.8$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). MMLU 5-shot accuracy remains within 0.8\\,pp across all variants (Appendix~\\ref{sec:appendix-mmlu}). We analyze this distribution shift in \\S\\ref{sec:analysis}.\n\n\\subsection{Inference-Time Attention Steering}\\label{subsec:steering}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig5_attention_steering.pdf}\n  \\caption{Inference-time $\\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation as a proximal cause (9\\% PPL cost at $\\beta$\\,=\\,3; phase transition at $\\beta \\in [2, 3]$).}\n  \\label{fig:steering-recovery}\n\\end{figure}\n\nAll training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\\beta$ to pre-softmax attention logits for goal-token positions during generation:\n\\begin{equation}\n  \\tilde{A}_{i,j}^{(\\ell,h)} = A_{i,j}^{(\\ell,h)} + \\beta \\cdot \\mathbf{1}[j \\in \\mathcal{G}],\n\\end{equation}\nwhere $\\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\\beta \\in [0, 2]$ yields marginal improvement, then $\\beta = 3$ triggers a phase transition to GAR\\,=\\,0.556 (9\\% PPL cost). At $\\beta$\\,=\\,5, GAR reaches 0.727$\\pm$0.061 (PPL 1.77); the operating region $\\beta \\in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does---consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\\ref{sec:appendix-examples}). Downstream, steering ($\\beta$\\,=\\,3) raises late-turn instruction compliance by +11.1\\,pp, though this effect does not reach conventional significance ($p$\\,=\\,0.077; content-constrained tasks benefit most, +23.8\\,pp; Appendix~\\ref{sec:appendix-ir}).\n\n\\subsection{Scheduled Sampling Compresses the TF--AR Gap}\\label{subsec:ss}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_gap_compression.pdf}\n  \\caption{Scheduled sampling compresses the TF-AR gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$, the only variant approaching parity across five training conditions.}\n  \\label{fig:ss-gap}\n\\end{figure}\n\nScheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.001$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.\n\n\n",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  },
  "sourceToolAssistantUUID": "3ef7b25e-614c-4f1d-b4bc-cffec2cb562d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool call

_source line 1122 · 2026-05-25T09:10:14.632Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RhfShz3gRPgqeFW29qEN3B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46184d63-2b4f-49e3-96c1-efe218b5dd6d",
  "isSidechain": false,
  "requestId": "req_011CbP2VDwLqRomHDVYHob5K",
  "type": "assistant",
  "uuid": "f6bc8b8d-9fa7-43c4-9655-e871ab5bd5da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtUYgNxfASjFcjuXD4igpC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31511,
      "cache_read_input_tokens": 11447,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31511,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 352,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 31511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31511
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

_source line 1123 · 2026-05-25T09:10:14.640Z_

<details><summary>↩ Tool result · `toolu_01RhfShz3gRPgqeFW29qEN3B`</summary>

```text
1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Accessibility Ratio.}
6	Standard metrics such as perplexity and attention entropy capture generation quality but not \emph{what} the model attends to. In multi-turn dialogue, a model may generate fluent text while progressively ignoring task specifications in the system prompt. We need a metric that directly measures whether goal-relevant context receives attention. To formalize this, we denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. However, averaging dilutes the signal with intermediate positions that may legitimately attend to local context rather than the system prompt. The last token of each assistant turn is where the model aggregates information for the next continuation---attention at this position most directly reflects the model's awareness of task specifications. \textbf{GAR-ours} restricts the measurement accordingly:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}). Empirically, GAR-Dongre is diluted by NTP attention patterns to ${\sim}$0.01--0.02 in multi-turn settings, losing discriminative power across configurations; GAR-ours retains an order-of-magnitude range (0.019--0.50). The contrast itself is informative: goal attention concentrates at the last-token position, and only this concentrated pattern is vulnerable to distribution shift (\S\ref{sec:analysis}). Throughout this work, GAR serves primarily as a \emph{diagnostic probe}: it measures whether auxiliary attention training transfers to autoregressive generation, rather than being an end-to-end optimization objective whose increase directly improves downstream task performance (the correlation with instruction retention is weak; $r$\,=\,0.200, $p$\,=\,0.007; \S\ref{sec:discussion}).
18	
19	\subsection{ThreadGate Architecture}
20	
21	\begin{figure}[t]
22	  \centering
23	  \includegraphics[width=\columnwidth]{fig4_attention_heatmap.pdf}
24	  \caption{Per-turn GAR-ours under AR generation ($N$\,=\,5 conversations, 10 turns). All fine-tuned variants cluster together (77--81\% decay; $\Delta$\,=\,3.3\,pp between ThreadGate and LoRA-only); Base decays 87.5\%. Gating adds zero incremental effect.}
25	  \label{fig:attention-heatmap}
26	\end{figure}
27	
28	Different transformer layers serve different roles: early layers capture local syntax while later layers integrate long-range context \citep{gromov2024unreasonable}. A global intervention would uniformly scale all layers, but goal attention decay is layer-dependent: some layers contribute more to cross-turn information routing than others. ThreadGate therefore adds a \emph{per-layer} gating mechanism to the residual stream, allowing the model to learn which layers to modulate. At each layer $l$, the residual update is scaled by a scalar gate:
29	\begin{equation}
30	  x_{l+1} = x_l + g_l \cdot f_l(x_l),
31	\end{equation}
32	where $f_l$ denotes the sublayer computation (self-attention or feed-forward network, FFN). Since residual networks can be viewed as ensembles of shallow paths \citep{veit2016residual}, per-layer gating selectively modulates individual paths within this ensemble. This resembles ReZero \citep{bachlechner2021rezero}, which initializes a single trainable scalar at zero to stabilize deep network training, but ThreadGate differs in three ways: (i)~gates are \emph{content-conditioned}, a function of the hidden state rather than a fixed scalar; (ii)~gates are \emph{turn-conditioned}, incorporating conversation-position features; (iii)~gates are initialized near identity ($\sigma(1.5) \approx 0.82$) rather than zero, preserving the pretrained model's computation.
33	
34	Concretely, each gate $g_l$ is produced by a two-layer MLP that takes both content and turn features as input:
35	\begin{align}\label{eq:gate}
36	  g_l = \sigma\bigl(W_2\,\text{ReLU}(&W_1\,[\text{proj}(x_l);\;\text{emb}(t_d, t_i)] \notag\\
37	  &+ b_1) + b_2\bigr),
38	\end{align}
39	where $\text{proj}(\cdot)$ reduces the hidden dimension to 16, and $\text{emb}(t_d, t_i)$ provides a 16-dimensional turn embedding encoding turn distance $t_d$ (turns since system prompt) and turn index $t_i$ via learned lookup tables. The 32-dimensional input passes through a 64-unit hidden layer to a scalar gate in $(0, 1)$ via sigmoid. For Qwen-2.5-7B ($L\!=\!28$), this adds ${\sim}$57K parameters ($<$0.001\% of 7B). To isolate the contribution of turn conditioning, the \textbf{Uniform Gate} ablation replaces $\text{emb}(\cdot)$ with a learnable constant, removing turn awareness while retaining content-conditioned gating. To preserve pretrained behavior, gate biases are initialized to 1.5 (${\sim}$82\% pass-through) rather than zero as in ReZero, and gate parameters receive a $10\times$ learning rate multiplier to accelerate adaptation.
40	
41	\subsection{Training Objective}\label{sec:loss}
42	
43	Next-token prediction alone provides no gradient signal for attention allocation; a model can achieve low perplexity while distributing attention arbitrarily. The auxiliary GAR loss provides explicit pressure to maintain goal-token attention, while a diversity regularizer prevents gate collapse. The training objective combines three terms:
44	\begin{equation}
45	  \mathcal{L} = \mathcal{L}_\text{NTP} + \lambda_\text{GAR}\,\mathcal{L}_\text{GAR} + \lambda_\text{div}\,\mathcal{L}_\text{div}.
46	\end{equation}
47	$\mathcal{L}_\text{NTP}$ is the standard next-token prediction loss. For $\mathcal{L}_\text{GAR}$, we use MSE rather than cross-entropy because GAR is a continuous ratio and MSE provides \emph{bidirectional} pressure---penalizing both under- and over-attention, preventing identity collapse (Appendix~\ref{sec:appendix-loss}):
48	\begin{equation}
49	  \mathcal{L}_\text{GAR} = \text{MSE}(\text{GAR\text{-}ours}, \tau),
50	\end{equation}
51	where $\tau = 0.5$ targets allocating half of the last token's attention to goal tokens. Without diversity pressure, all gates converge near 1.0; the gate diversity loss prevents this:
52	\begin{equation}
53	  \mathcal{L}_\text{div} = \text{ReLU}(\sigma_\text{min} - \text{std}(\mathbf{g})),
54	\end{equation}
55	where $\mathbf{g} = [g_1, \ldots, g_L]$ and $\sigma_\text{min} = 0.05$ is a minimum standard deviation threshold ($\lambda_\text{GAR} = \lambda_\text{div} = 1.0$). This formulation emerged from seven iterations spanning four loss families (Appendix~\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity; only MSE provides the bidirectional pressure needed to prevent identity collapse.
56	
57	\subsection{Controlled Comparison Design}\label{sec:comparison-design}
58	
59	We design a five-way comparison where each adjacent pair isolates one factor: \textbf{ThreadGate (TG) vs.\ Uniform Gate (UG)} (turn conditioning), \textbf{TG vs.\ LoRA-only} (gating mechanism), \textbf{ThreadGate vs.\ +PCGrad} (gradient conflict via gradient surgery \citep{yu2020pcgrad}), and \textbf{Fine-tuned vs.\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\ref{sec:appendix-hyper}).
60	
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6bc8b8d-9fa7-43c4-9655-e871ab5bd5da",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "559bfdb8-2c37-4b04-8d9b-3910b3516ba3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/method.tex",
      "content": "\\section{Method}\\label{sec:method}\n\n\\subsection{Preliminaries}\\label{sec:background}\n\n\\paragraph{Goal Accessibility Ratio.}\nStandard metrics such as perplexity and attention entropy capture generation quality but not \\emph{what} the model attends to. In multi-turn dialogue, a model may generate fluent text while progressively ignoring task specifications in the system prompt. We need a metric that directly measures whether goal-relevant context receives attention. To formalize this, we denote the task specification tokens in the system prompt as \\emph{goal tokens} $\\mathcal{G}$. \\citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\\tau$ as\n\\begin{equation}\\label{eq:gar}\n  \\text{GAR}(\\tau) = \\frac{1}{L \\cdot H \\cdot |\\mathcal{R}_\\tau|} \\sum_{\\ell=1}^{L} \\sum_{h=1}^{H} \\sum_{i \\in \\mathcal{R}_\\tau} \\sum_{j \\in \\mathcal{G}} A_{i,j}^{(\\ell,h)},\n\\end{equation}\nwhere $\\mathcal{R}_\\tau$ is the set of response tokens at turn $\\tau$ and $A_{i,j}^{(\\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\\ell$, head $h$.\n\n\\paragraph{Two GAR variants.}\n\\textbf{GAR-Dongre} is the original definition (Eq.~\\ref{eq:gar}), averaging over all response tokens. However, averaging dilutes the signal with intermediate positions that may legitimately attend to local context rather than the system prompt. The last token of each assistant turn is where the model aggregates information for the next continuation---attention at this position most directly reflects the model's awareness of task specifications. \\textbf{GAR-ours} restricts the measurement accordingly:\n\\begin{equation}\\label{eq:gar-ours}\n  \\text{GAR\\text{-}ours}(\\tau) = \\frac{1}{L \\cdot H} \\sum_{\\ell=1}^{L} \\sum_{h=1}^{H} \\sum_{j \\in \\mathcal{G}} A_{t_\\tau,\\, j}^{(\\ell,h)},\n\\end{equation}\nwhere $t_\\tau$ is the last token index at turn $\\tau$. Attention at this position reflects the information drawn upon for continuation; we use GAR-ours as the optimization target for $\\mathcal{L}_\\text{GAR}$ (\\S\\ref{sec:loss}). Empirically, GAR-Dongre is diluted by NTP attention patterns to ${\\sim}$0.01--0.02 in multi-turn settings, losing discriminative power across configurations; GAR-ours retains an order-of-magnitude range (0.019--0.50). The contrast itself is informative: goal attention concentrates at the last-token position, and only this concentrated pattern is vulnerable to distribution shift (\\S\\ref{sec:analysis}). Throughout this work, GAR serves primarily as a \\emph{diagnostic probe}: it measures whether auxiliary attention training transfers to autoregressive generation, rather than being an end-to-end optimization objective whose increase directly improves downstream task performance (the correlation with instruction retention is weak; $r$\\,=\\,0.200, $p$\\,=\\,0.007; \\S\\ref{sec:discussion}).\n\n\\subsection{ThreadGate Architecture}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig4_attention_heatmap.pdf}\n  \\caption{Per-turn GAR-ours under AR generation ($N$\\,=\\,5 conversations, 10 turns). All fine-tuned variants cluster together (77--81\\% decay; $\\Delta$\\,=\\,3.3\\,pp between ThreadGate and LoRA-only); Base decays 87.5\\%. Gating adds zero incremental effect.}\n  \\label{fig:attention-heatmap}\n\\end{figure}\n\nDifferent transformer layers serve different roles: early layers capture local syntax while later layers integrate long-range context \\citep{gromov2024unreasonable}. A global intervention would uniformly scale all layers, but goal attention decay is layer-dependent: some layers contribute more to cross-turn information routing than others. ThreadGate therefore adds a \\emph{per-layer} gating mechanism to the residual stream, allowing the model to learn which layers to modulate. At each layer $l$, the residual update is scaled by a scalar gate:\n\\begin{equation}\n  x_{l+1} = x_l + g_l \\cdot f_l(x_l),\n\\end{equation}\nwhere $f_l$ denotes the sublayer computation (self-attention or feed-forward network, FFN). Since residual networks can be viewed as ensembles of shallow paths \\citep{veit2016residual}, per-layer gating selectively modulates individual paths within this ensemble. This resembles ReZero \\citep{bachlechner2021rezero}, which initializes a single trainable scalar at zero to stabilize deep network training, but ThreadGate differs in three ways: (i)~gates are \\emph{content-conditioned}, a function of the hidden state rather than a fixed scalar; (ii)~gates are \\emph{turn-conditioned}, incorporating conversation-position features; (iii)~gates are initialized near identity ($\\sigma(1.5) \\approx 0.82$) rather than zero, preserving the pretrained model's computation.\n\nConcretely, each gate $g_l$ is produced by a two-layer MLP that takes both content and turn features as input:\n\\begin{align}\\label{eq:gate}\n  g_l = \\sigma\\bigl(W_2\\,\\text{ReLU}(&W_1\\,[\\text{proj}(x_l);\\;\\text{emb}(t_d, t_i)] \\notag\\\\\n  &+ b_1) + b_2\\bigr),\n\\end{align}\nwhere $\\text{proj}(\\cdot)$ reduces the hidden dimension to 16, and $\\text{emb}(t_d, t_i)$ provides a 16-dimensional turn embedding encoding turn distance $t_d$ (turns since system prompt) and turn index $t_i$ via learned lookup tables. The 32-dimensional input passes through a 64-unit hidden layer to a scalar gate in $(0, 1)$ via sigmoid. For Qwen-2.5-7B ($L\\!=\\!28$), this adds ${\\sim}$57K parameters ($<$0.001\\% of 7B). To isolate the contribution of turn conditioning, the \\textbf{Uniform Gate} ablation replaces $\\text{emb}(\\cdot)$ with a learnable constant, removing turn awareness while retaining content-conditioned gating. To preserve pretrained behavior, gate biases are initialized to 1.5 (${\\sim}$82\\% pass-through) rather than zero as in ReZero, and gate parameters receive a $10\\times$ learning rate multiplier to accelerate adaptation.\n\n\\subsection{Training Objective}\\label{sec:loss}\n\nNext-token prediction alone provides no gradient signal for attention allocation; a model can achieve low perplexity while distributing attention arbitrarily. The auxiliary GAR loss provides explicit pressure to maintain goal-token attention, while a diversity regularizer prevents gate collapse. The training objective combines three terms:\n\\begin{equation}\n  \\mathcal{L} = \\mathcal{L}_\\text{NTP} + \\lambda_\\text{GAR}\\,\\mathcal{L}_\\text{GAR} + \\lambda_\\text{div}\\,\\mathcal{L}_\\text{div}.\n\\end{equation}\n$\\mathcal{L}_\\text{NTP}$ is the standard next-token prediction loss. For $\\mathcal{L}_\\text{GAR}$, we use MSE rather than cross-entropy because GAR is a continuous ratio and MSE provides \\emph{bidirectional} pressure---penalizing both under- and over-attention, preventing identity collapse (Appendix~\\ref{sec:appendix-loss}):\n\\begin{equation}\n  \\mathcal{L}_\\text{GAR} = \\text{MSE}(\\text{GAR\\text{-}ours}, \\tau),\n\\end{equation}\nwhere $\\tau = 0.5$ targets allocating half of the last token's attention to goal tokens. Without diversity pressure, all gates converge near 1.0; the gate diversity loss prevents this:\n\\begin{equation}\n  \\mathcal{L}_\\text{div} = \\text{ReLU}(\\sigma_\\text{min} - \\text{std}(\\mathbf{g})),\n\\end{equation}\nwhere $\\mathbf{g} = [g_1, \\ldots, g_L]$ and $\\sigma_\\text{min} = 0.05$ is a minimum standard deviation threshold ($\\lambda_\\text{GAR} = \\lambda_\\text{div} = 1.0$). This formulation emerged from seven iterations spanning four loss families (Appendix~\\ref{sec:appendix-loss}): cumulative (v1--v2) and maximize (v3--v6) objectives either starve gate gradients at equilibrium or drive gates toward identity; only MSE provides the bidirectional pressure needed to prevent identity collapse.\n\n\\subsection{Controlled Comparison Design}\\label{sec:comparison-design}\n\nWe design a five-way comparison where each adjacent pair isolates one factor: \\textbf{ThreadGate (TG) vs.\\ Uniform Gate (UG)} (turn conditioning), \\textbf{TG vs.\\ LoRA-only} (gating mechanism), \\textbf{ThreadGate vs.\\ +PCGrad} (gradient conflict via gradient surgery \\citep{yu2020pcgrad}), and \\textbf{Fine-tuned vs.\\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\\ref{sec:appendix-hyper}).\n\n",
      "numLines": 61,
      "startLine": 1,
      "totalLines": 61
    }
  },
  "sourceToolAssistantUUID": "f6bc8b8d-9fa7-43c4-9655-e871ab5bd5da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool call

_source line 1124 · 2026-05-25T09:10:14.863Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KZwaTpMoU2QUfxQdnda5ig`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "559bfdb8-2c37-4b04-8d9b-3910b3516ba3",
  "isSidechain": false,
  "requestId": "req_011CbP2VDwLqRomHDVYHob5K",
  "type": "assistant",
  "uuid": "a84f1ae1-a456-46e5-864f-15b799a73155",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PtUYgNxfASjFcjuXD4igpC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 31511,
      "cache_read_input_tokens": 11447,
      "output_tokens": 352,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31511,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 352,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 31511,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31511
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

_source line 1125_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 附录内容引用完整性检查  **任务：** 检查论文附录的所有内容是否在正文中都有准确、合理的引用，修复孤儿附录。  **Step 1：逐项盘点** 列出附录里每一个 section/subsection/table/figure/algorithm/proof/prompt。  **Step 2：逐项验证引用** 对每一项，在正文搜索是否有至少一句话指向…",
  "leafUuid": "95bd2982-13f8-4d20-9a4c-8814719566f8",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1126_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Assistant

_source line 1127 · 2026-05-25T09:10:19.384Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read the related work and appendix to understand exactly what each orphan section contains, so I can find the best places to reference them.

Let me also read the related_work and the appendix sections for the orphans.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95bd2982-13f8-4d20-9a4c-8814719566f8",
  "isSidechain": false,
  "requestId": "req_011CbP2VghRCjvWgvc6nRpaq",
  "type": "assistant",
  "uuid": "8637c08a-25f3-49bc-b8c6-872588b50ad0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZVikyyveKuov6Em9kigVB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7390,
      "cache_read_input_tokens": 42958,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7390,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 251,
          "cache_read_input_tokens": 42958,
          "cache_creation_input_tokens": 7390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7390
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

_source line 1128 · 2026-05-25T09:10:19.840Z_

Now let me read the related work and the appendix to understand what each orphan section contains.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8637c08a-25f3-49bc-b8c6-872588b50ad0",
  "isSidechain": false,
  "requestId": "req_011CbP2VghRCjvWgvc6nRpaq",
  "type": "assistant",
  "uuid": "73b6bc24-3879-4294-85ea-3c7dad2eb09b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZVikyyveKuov6Em9kigVB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7390,
      "cache_read_input_tokens": 42958,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7390,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 251,
          "cache_read_input_tokens": 42958,
          "cache_creation_input_tokens": 7390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7390
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

_source line 1129 · 2026-05-25T09:10:21.190Z_

<details open><summary>🔧 Tool call — Read · `toolu_012E6rMqqpM3kLzkYDy2adN2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73b6bc24-3879-4294-85ea-3c7dad2eb09b",
  "isSidechain": false,
  "requestId": "req_011CbP2VghRCjvWgvc6nRpaq",
  "type": "assistant",
  "uuid": "4b4dc49e-4b9c-4321-bfda-975c9ae73fad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZVikyyveKuov6Em9kigVB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7390,
      "cache_read_input_tokens": 42958,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7390,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 251,
          "cache_read_input_tokens": 42958,
          "cache_creation_input_tokens": 7390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7390
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

_source line 1130 · 2026-05-25T09:10:21.194Z_

<details><summary>↩ Tool result · `toolu_012E6rMqqpM3kLzkYDy2adN2`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\begin{table*}[t]
4	\centering
5	\small
6	\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\,=\,50 held-out conversations (mean 3.6 user turns). All fine-tuned variants converge under TF ($\leq$2\,pp spread); the 8--17$\times$ TF-AR gap persists across all configurations. $\bar{g}\!\pm\!\sigma_g$: learned gate mean and std across 28 layers (LoRA-only has no gates). GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}.}
7	\label{tab:four-way}
8	\begin{tabular}{l ccc ccc cc c}
9	\toprule
10	& \multicolumn{3}{c}{\textbf{IID (TF)}} & \multicolumn{3}{c}{\textbf{Held-out (TF)}} & \multicolumn{2}{c}{\textbf{AR ($N$\,=\,50)}} & \\
11	\cmidrule(lr){2-4} \cmidrule(lr){5-7} \cmidrule(lr){8-9}
12	\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL & GAR-O & 95\% CI & $\bar{g}\!\pm\!\sigma_g$ \\
13	\midrule
14	\multicolumn{10}{l}{\emph{Baseline}} \\
15	Base              & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 & 0.019 & {\scriptsize[.014,\,.024]} & --- \\
16	\midrule
17	\multicolumn{10}{l}{\emph{Gated variants}} \\
18	ThreadGate        & 0.50 & \textbf{0.02} & 2.78 & 0.50 & \textbf{0.02} & 2.78 & \textbf{0.064} & {\scriptsize[.041,\,.091]} & .93\,{\scriptsize$\pm$\,.05} \\
19	\;+\,PCGrad       & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.030 & {\scriptsize[.023,\,.038]} & --- \\
20	Uniform Gate      & 0.49 & 0.01 & 2.78 & \textbf{0.51} & 0.01 & 2.78 & 0.033 & {\scriptsize[.025,\,.043]} & .96\,{\scriptsize$\pm$\,.05} \\
21	\midrule
22	\multicolumn{10}{l}{\emph{Ungated}} \\
23	LoRA-only         & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.037 & {\scriptsize[.027,\,.050]} & 1.00 \\
24	\bottomrule
25	\end{tabular}
26	\end{table*}
27	
28	\paragraph{Multi-turn dialogue and attention decay.}
29	Multi-turn coherence has been a persistent challenge from early dialogue systems \citep{li2016persona,roller2021recipes,zhang2020dialogpt} through modern long-context models \citep{xu2022goldfish}, with benchmarks such as MT-Bench \citep{zheng2024judging} and MT-Bench-101 \citep{bai2024mtbench101} continuing to expose quality gaps at later turns \citep{laban2025lost,liu2026intent}. Most relevant to our work, \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) and showed that attention to goal tokens decays 27--48\% across 12 models while residual probes retain goal information (AUC\,=\,0.98). We observe a steeper 70.8\% decline on Qwen-2.5-7B. \citet{li2024measuring} independently quantified instruction instability and proposed split-softmax as an inference-time remedy. Our work differs in scope: we diagnose \emph{why} training-time attention optimization fails to transfer to inference, and provide the first training-time mitigation.
30	
31	\paragraph{Gating and attention manipulation.}
32	Residual gating has evolved from highway networks \citep{srivastava2015highway} through ResNet skip connections \citep{he2016deep} to ReZero \citep{bachlechner2021rezero}, layer pruning \citep{gromov2024unreasonable}, LayerDrop \citep{fan2020layerdrop}, and adaptive depth \citep{schuster2022calm,raposo2024mixture}. Most relevant is Gated Attention \citep{qiu2025gated}: per-head sigmoid gates achieving Massive Multitask Language Understanding (MMLU; \citealp{hendrycks2021measuring}) $+$2.03 at 15B scale. ThreadGate differs in conditioning on turn position; our results show neither turn conditioning nor Gated Linear Unit (GLU)-style gating \citep{dauphin2017language,shazeer2020glu} overcomes exposure bias. On the analysis side, head specialization \citep{clark2019what,voita2019analyzing,kovaleva2019revealing}, attention visualization \citep{vig2019multiscale}, positional bias calibration \citep{liu2024lost,xiao2024streaming}, and attention steering (PASTA; \citealp{zhang2024tell}) address inference behavior; our $\beta$-steering serves a diagnostic role. Multi-task gradient methods---PCGrad \citep{yu2020pcgrad}, CAGrad \citep{liu2021cagrad}---treat conflict as the root cause; we repurpose PCGrad as a diagnostic and show direction conflict is a symptom, not the primary cause.
33	
34	\paragraph{Exposure bias in sequence models.}
35	Teacher forcing creates a distributional mismatch between training and inference \citep{wiseman2016sequence,arora2022exposure}. Scheduled sampling \citep{bengio2015scheduled} introduced curriculum-based mixing; subsequent work proposed sequence-level objectives \citep{ranzato2016sequence}, adversarial regularization \citep{lamb2016professor}, self-recovery analysis \citep{he2019exposure}, bridging strategies for neural machine translation (NMT; \citealp{zhang2019bridging}), and search-based training \citep{leblond2018searnn}. \citet{mihaylova2019scheduled} extended scheduled sampling to transformers for single-turn NMT. \citet{dou2019attention} proposed attention forcing---supervising cross-attention during NMT---and \citet{dou2022parallel} extended it with KL-divergence switching. Our work differs: (i)~time-scheduled sampling (linearly increasing $\rho$), not data-dependent; (ii)~self-attention in multi-turn dialogue, not cross-attention in NMT; (iii)~auxiliary attention objectives, not primary translation loss. No prior work examines exposure bias on \emph{auxiliary} attention objectives or provides multi-turn transformer mitigation; we fill both gaps.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b4dc49e-4b9c-4321-bfda-975c9ae73fad",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "2dd086c3-3a2e-4269-a628-fc04b528a888",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\\,=\\,50 held-out conversations (mean 3.6 user turns). All fine-tuned variants converge under TF ($\\leq$2\\,pp spread); the 8--17$\\times$ TF-AR gap persists across all configurations. $\\bar{g}\\!\\pm\\!\\sigma_g$: learned gate mean and std across 28 layers (LoRA-only has no gates). GAR-O = GAR-ours; GAR-D = GAR-Dongre \\citep{dongre2026attention}.}\n\\label{tab:four-way}\n\\begin{tabular}{l ccc ccc cc c}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{IID (TF)}} & \\multicolumn{3}{c}{\\textbf{Held-out (TF)}} & \\multicolumn{2}{c}{\\textbf{AR ($N$\\,=\\,50)}} & \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7} \\cmidrule(lr){8-9}\n\\textbf{Configuration} & GAR-O & GAR-D & PPL & GAR-O & GAR-D & PPL & GAR-O & 95\\% CI & $\\bar{g}\\!\\pm\\!\\sigma_g$ \\\\\n\\midrule\n\\multicolumn{10}{l}{\\emph{Baseline}} \\\\\nBase              & 0.01 & 0.00 & 4.23 & 0.01 & 0.00 & 4.34 & 0.019 & {\\scriptsize[.014,\\,.024]} & --- \\\\\n\\midrule\n\\multicolumn{10}{l}{\\emph{Gated variants}} \\\\\nThreadGate        & 0.50 & \\textbf{0.02} & 2.78 & 0.50 & \\textbf{0.02} & 2.78 & \\textbf{0.064} & {\\scriptsize[.041,\\,.091]} & .93\\,{\\scriptsize$\\pm$\\,.05} \\\\\n\\;+\\,PCGrad       & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.030 & {\\scriptsize[.023,\\,.038]} & --- \\\\\nUniform Gate      & 0.49 & 0.01 & 2.78 & \\textbf{0.51} & 0.01 & 2.78 & 0.033 & {\\scriptsize[.025,\\,.043]} & .96\\,{\\scriptsize$\\pm$\\,.05} \\\\\n\\midrule\n\\multicolumn{10}{l}{\\emph{Ungated}} \\\\\nLoRA-only         & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.037 & {\\scriptsize[.027,\\,.050]} & 1.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Multi-turn dialogue and attention decay.}\nMulti-turn coherence has been a persistent challenge from early dialogue systems \\citep{li2016persona,roller2021recipes,zhang2020dialogpt} through modern long-context models \\citep{xu2022goldfish}, with benchmarks such as MT-Bench \\citep{zheng2024judging} and MT-Bench-101 \\citep{bai2024mtbench101} continuing to expose quality gaps at later turns \\citep{laban2025lost,liu2026intent}. Most relevant to our work, \\citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) and showed that attention to goal tokens decays 27--48\\% across 12 models while residual probes retain goal information (AUC\\,=\\,0.98). We observe a steeper 70.8\\% decline on Qwen-2.5-7B. \\citet{li2024measuring} independently quantified instruction instability and proposed split-softmax as an inference-time remedy. Our work differs in scope: we diagnose \\emph{why} training-time attention optimization fails to transfer to inference, and provide the first training-time mitigation.\n\n\\paragraph{Gating and attention manipulation.}\nResidual gating has evolved from highway networks \\citep{srivastava2015highway} through ResNet skip connections \\citep{he2016deep} to ReZero \\citep{bachlechner2021rezero}, layer pruning \\citep{gromov2024unreasonable}, LayerDrop \\citep{fan2020layerdrop}, and adaptive depth \\citep{schuster2022calm,raposo2024mixture}. Most relevant is Gated Attention \\citep{qiu2025gated}: per-head sigmoid gates achieving Massive Multitask Language Understanding (MMLU; \\citealp{hendrycks2021measuring}) $+$2.03 at 15B scale. ThreadGate differs in conditioning on turn position; our results show neither turn conditioning nor Gated Linear Unit (GLU)-style gating \\citep{dauphin2017language,shazeer2020glu} overcomes exposure bias. On the analysis side, head specialization \\citep{clark2019what,voita2019analyzing,kovaleva2019revealing}, attention visualization \\citep{vig2019multiscale}, positional bias calibration \\citep{liu2024lost,xiao2024streaming}, and attention steering (PASTA; \\citealp{zhang2024tell}) address inference behavior; our $\\beta$-steering serves a diagnostic role. Multi-task gradient methods---PCGrad \\citep{yu2020pcgrad}, CAGrad \\citep{liu2021cagrad}---treat conflict as the root cause; we repurpose PCGrad as a diagnostic and show direction conflict is a symptom, not the primary cause.\n\n\\paragraph{Exposure bias in sequence models.}\nTeacher forcing creates a distributional mismatch between training and inference \\citep{wiseman2016sequence,arora2022exposure}. Scheduled sampling \\citep{bengio2015scheduled} introduced curriculum-based mixing; subsequent work proposed sequence-level objectives \\citep{ranzato2016sequence}, adversarial regularization \\citep{lamb2016professor}, self-recovery analysis \\citep{he2019exposure}, bridging strategies for neural machine translation (NMT; \\citealp{zhang2019bridging}), and search-based training \\citep{leblond2018searnn}. \\citet{mihaylova2019scheduled} extended scheduled sampling to transformers for single-turn NMT. \\citet{dou2019attention} proposed attention forcing---supervising cross-attention during NMT---and \\citet{dou2022parallel} extended it with KL-divergence switching. Our work differs: (i)~time-scheduled sampling (linearly increasing $\\rho$), not data-dependent; (ii)~self-attention in multi-turn dialogue, not cross-attention in NMT; (iii)~auxiliary attention objectives, not primary translation loss. No prior work examines exposure bias on \\emph{auxiliary} attention objectives or provides multi-turn transformer mitigation; we fill both gaps.\n",
      "numLines": 36,
      "startLine": 1,
      "totalLines": 36
    }
  },
  "sourceToolAssistantUUID": "4b4dc49e-4b9c-4321-bfda-975c9ae73fad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool call

_source line 1131 · 2026-05-25T09:10:21.860Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ANHUV3dtwP6t75VFr2HQ3g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dd086c3-3a2e-4269-a628-fc04b528a888",
  "isSidechain": false,
  "requestId": "req_011CbP2VghRCjvWgvc6nRpaq",
  "type": "assistant",
  "uuid": "bc70d9cd-b43f-48c7-bee7-6cbfef55b0ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RZVikyyveKuov6Em9kigVB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7390,
      "cache_read_input_tokens": 42958,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7390,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 251,
          "cache_read_input_tokens": 42958,
          "cache_creation_input_tokens": 7390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7390
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

_source line 1132 · 2026-05-25T09:10:22.124Z_

<details><summary>↩ Tool result · reported error · `toolu_01ANHUV3dtwP6t75VFr2HQ3g`</summary>

```text
File content (26103 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc70d9cd-b43f-48c7-bee7-6cbfef55b0ec",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "c884c715-d1f7-40b0-9baf-b225ea365fa8",
  "toolUseResult": "Error: File content (26103 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "bc70d9cd-b43f-48c7-bee7-6cbfef55b0ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Assistant

_source line 1133 · 2026-05-25T09:10:25.357Z_

<details><summary>Logged reasoning block</summary>

```text
The appendix is too long. Let me search for each orphan section to understand what it contains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c884c715-d1f7-40b0-9baf-b225ea365fa8",
  "isSidechain": false,
  "requestId": "req_011CbP2WDS7C6hdAggyyPWns",
  "type": "assistant",
  "uuid": "e9413c01-775d-4691-8b01-439596123d43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GLr8ey8RuKako3LLRxdgKz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2300,
      "cache_read_input_tokens": 50348,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2300,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 363,
          "cache_read_input_tokens": 50348,
          "cache_creation_input_tokens": 2300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2300
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

_source line 1134 · 2026-05-25T09:10:25.842Z_

Let me read the appendix in segments to understand the orphan sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9413c01-775d-4691-8b01-439596123d43",
  "isSidechain": false,
  "requestId": "req_011CbP2WDS7C6hdAggyyPWns",
  "type": "assistant",
  "uuid": "52c9999d-3404-462e-9c68-06eb3476d7c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GLr8ey8RuKako3LLRxdgKz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2300,
      "cache_read_input_tokens": 50348,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2300,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 363,
          "cache_read_input_tokens": 50348,
          "cache_creation_input_tokens": 2300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2300
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

_source line 1135 · 2026-05-25T09:10:26.783Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HHBMmU8hLeBmGbeB8biKSf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52c9999d-3404-462e-9c68-06eb3476d7c0",
  "isSidechain": false,
  "requestId": "req_011CbP2WDS7C6hdAggyyPWns",
  "type": "assistant",
  "uuid": "288cc4ca-c34d-452c-8c68-d59c69e93dab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GLr8ey8RuKako3LLRxdgKz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2300,
      "cache_read_input_tokens": 50348,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2300,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 363,
          "cache_read_input_tokens": 50348,
          "cache_creation_input_tokens": 2300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2300
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

_source line 1136 · 2026-05-25T09:10:29.084Z_

<details><summary>↩ Tool result · `toolu_0166nktmvi7aNvVdkRcnoZMM`</summary>

```text
499-
500:\section{Per-Turn AR GAR Dynamics}\label{sec:appendix-ar-gar-dynamics}
501-
502-To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.
503-
504-[Omitted long context line]
505-
--
638-
639:\section{Per-Turn GAR Decay Analysis}\label{sec:appendix-perturn-detail}
640-
641-Tables~\ref{tab:perturn-qwen} and~\ref{tab:perturn-llama} present per-turn AR GAR values for all configurations on both architectures, complementing the aggregate mid-turn GAR reported in the main text (Table~\ref{tab:four-way}).
642-
643-[Omitted long context line]
644-
--
668-
669:\section{Extended Dataset Statistics}\label{sec:appendix-dataset-ext}
670-
671-Table~\ref{tab:dataset_stats} provides detailed statistics for the UltraChat training and evaluation splits. From the full UltraChat-200K corpus (207,865 conversations in the \texttt{train\_sft} split), we filter for conversations with $\geq$5 assistant turns, yielding 17,302 candidates (8.3\% of the full corpus). We randomly sample 8,000 for training, 50 for primary AR evaluation (mean 3.6 user turns), 50 for IID GAR diagnostics, and 200 for the instruction retention evaluation.
672-
673-[Omitted long context line]
674-
--
680-
681:\section{Extended GAR Robustness Analysis}\label{sec:appendix-gar-ext}
682-
683-[Omitted long context line]
684-
685-[Omitted long context line]
686-
--
697-
698:\section{MMLU Category Breakdown}\label{sec:appendix-mmlu-ext}
699-
700-Table~\ref{tab:mmlu_detail} breaks down MMLU 5-shot accuracy by category (STEM, Social Sciences, Humanities, Other) for all six Qwen-2.5-7B training configurations. This analysis addresses a potential concern: that auxiliary attention objectives might divert representational capacity from general language understanding, particularly in knowledge-intensive STEM domains.
701-
702-[Omitted long context line]
703-
--
716-
717:\section{Extended Cross-Scale Results (Qwen-2.5-1.5B)}\label{sec:appendix-1.5b-ext}
718-
719-Table~\ref{tab:qwen15b_results} extends the cross-scale analysis with Phase~1 GAR diagnostics, detailed Phase~2 training results, and $\beta$-steering evaluation on the Qwen-2.5-1.5B-Instruct model.
720-
721-\paragraph{Phase 1: GAR decay.} The 1.5B base model exhibits 79.8\% relative GAR decline from turn~1 to mid-turns, more severe than the 7B model's 70.8\% decline. This scale-dependent decay severity is consistent with smaller models having less redundant attention capacity: with 28 layers but only 1.5B parameters (vs.\ 7B), each layer carries proportionally more of the total representational burden, leaving less room for goal-oriented attention to persist alongside the primary NTP objective.
722-
--
730-
731:\section{Extended Statistical Analysis}\label{sec:appendix-stats-ext}
732-
733-Table~\ref{tab:statistical_tests} consolidates all statistical tests reported in this paper, including effect sizes, 95\% bootstrap confidence intervals, and significance levels. This section provides methodological detail beyond the summary in Appendix~\ref{sec:appendix-stats}.
734-
735-[Omitted long context line]
736-
--
746-
747:\section{Extended Training Dynamics}\label{sec:appendix-training-ext}
748-
749-Figure~\ref{fig:training-6panel} presents the complete training loss landscape for all five Qwen-2.5-7B conditions (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Scheduled Sampling) plus the base model, showing NTP loss, GAR loss, and total loss across three epochs.
750-
751-[Omitted long context line]
752-
--
763-
764:\section{Per-$\beta$ Steering Visualization}\label{sec:appendix-steering-viz}
765-
766-Figure~\ref{fig:steering-4panel} visualizes per-turn GAR trajectories under four steering strengths ($\beta$\,=\,0, 3, 5, 10), revealing the turn-level dynamics that underlie the aggregate steering results in Table~\ref{tab:steering-full}.
767-
768-\paragraph{Unsteered baseline ($\beta$\,=\,0).} GAR decays monotonically from 0.12 to 0.02 over five turns, with the steepest decline between turns~1 and~2 ($-$44\%). This trajectory matches the per-turn profiles in Appendix~\ref{sec:appendix-perturn-detail} and confirms that the decay is a smooth, progressive phenomenon rather than a discrete failure at a specific turn.
769-
--
784-
785:\section{Llama-3.1-8B Scheduled Sampling Details}\label{sec:appendix-llama-ss}
786-
787-[Omitted long context line]
788-
789-\paragraph{$\beta$-steering on Llama SS.}
790-Table~\ref{tab:llama-ss-steering} reports $\beta$-steering results on the Llama SS model. Unlike Qwen, $\beta$\,=\,3 does not trigger recovery on Llama (GAR 0.173 vs.\ 0.166 at $\beta$\,=\,0). At $\beta$\,=\,5, GAR reaches 0.791---higher than Qwen's 0.717---suggesting that Llama's attention distribution is more responsive to the additive bias at higher steering strengths, possibly because the lower baseline AR GAR leaves more headroom for steering to exploit.
--
834-
835:\section{Use of AI Assistants}\label{sec:appendix-ai}
836-
837-We used Claude (Anthropic) as an AI coding and writing assistant
838-throughout this work. Specifically:
839-\begin{itemize}
840-    \item \textbf{Code:} drafting experiment scripts, data-processing
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7c346ee-51f1-4a03-bc98-600e879dfc6a",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "3fb16c0e-6f50-486a-9e5a-f6c4a9c7b49e",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "499-\n500:\\section{Per-Turn AR GAR Dynamics}\\label{sec:appendix-ar-gar-dynamics}\n501-\n502-To characterize how goal attention evolves across conversation turns under autoregressive generation, we compute per-turn AR GAR for all six Qwen-2.5-7B training configurations (Base, LoRA-only, Uniform Gate, PCGrad, Scheduled Sampling, ThreadGate) on the held-out evaluation set. Figure~\\ref{fig:kl_ar_gar_curves} plots per-turn AR GAR trajectories across turns 1--5, and Figure~\\ref{fig:kl_ar_gar_bar} compares mid-turn AR GAR levels across configurations.\n503-\n504-[Omitted long context line]\n505-\n--\n638-\n639:\\section{Per-Turn GAR Decay Analysis}\\label{sec:appendix-perturn-detail}\n640-\n641-Tables~\\ref{tab:perturn-qwen} and~\\ref{tab:perturn-llama} present per-turn AR GAR values for all configurations on both architectures, complementing the aggregate mid-turn GAR reported in the main text (Table~\\ref{tab:four-way}).\n642-\n643-[Omitted long context line]\n644-\n--\n668-\n669:\\section{Extended Dataset Statistics}\\label{sec:appendix-dataset-ext}\n670-\n671-Table~\\ref{tab:dataset_stats} provides detailed statistics for the UltraChat training and evaluation splits. From the full UltraChat-200K corpus (207,865 conversations in the \\texttt{train\\_sft} split), we filter for conversations with $\\geq$5 assistant turns, yielding 17,302 candidates (8.3\\% of the full corpus). We randomly sample 8,000 for training, 50 for primary AR evaluation (mean 3.6 user turns), 50 for IID GAR diagnostics, and 200 for the instruction retention evaluation.\n672-\n673-[Omitted long context line]\n674-\n--\n680-\n681:\\section{Extended GAR Robustness Analysis}\\label{sec:appendix-gar-ext}\n682-\n683-[Omitted long context line]\n684-\n685-[Omitted long context line]\n686-\n--\n697-\n698:\\section{MMLU Category Breakdown}\\label{sec:appendix-mmlu-ext}\n699-\n700-Table~\\ref{tab:mmlu_detail} breaks down MMLU 5-shot accuracy by category (STEM, Social Sciences, Humanities, Other) for all six Qwen-2.5-7B training configurations. This analysis addresses a potential concern: that auxiliary attention objectives might divert representational capacity from general language understanding, particularly in knowledge-intensive STEM domains.\n701-\n702-[Omitted long context line]\n703-\n--\n716-\n717:\\section{Extended Cross-Scale Results (Qwen-2.5-1.5B)}\\label{sec:appendix-1.5b-ext}\n718-\n719-Table~\\ref{tab:qwen15b_results} extends the cross-scale analysis with Phase~1 GAR diagnostics, detailed Phase~2 training results, and $\\beta$-steering evaluation on the Qwen-2.5-1.5B-Instruct model.\n720-\n721-\\paragraph{Phase 1: GAR decay.} The 1.5B base model exhibits 79.8\\% relative GAR decline from turn~1 to mid-turns, more severe than the 7B model's 70.8\\% decline. This scale-dependent decay severity is consistent with smaller models having less redundant attention capacity: with 28 layers but only 1.5B parameters (vs.\\ 7B), each layer carries proportionally more of the total representational burden, leaving less room for goal-oriented attention to persist alongside the primary NTP objective.\n722-\n--\n730-\n731:\\section{Extended Statistical Analysis}\\label{sec:appendix-stats-ext}\n732-\n733-Table~\\ref{tab:statistical_tests} consolidates all statistical tests reported in this paper, including effect sizes, 95\\% bootstrap confidence intervals, and significance levels. This section provides methodological detail beyond the summary in Appendix~\\ref{sec:appendix-stats}.\n734-\n735-[Omitted long context line]\n736-\n--\n746-\n747:\\section{Extended Training Dynamics}\\label{sec:appendix-training-ext}\n748-\n749-Figure~\\ref{fig:training-6panel} presents the complete training loss landscape for all five Qwen-2.5-7B conditions (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Scheduled Sampling) plus the base model, showing NTP loss, GAR loss, and total loss across three epochs.\n750-\n751-[Omitted long context line]\n752-\n--\n763-\n764:\\section{Per-$\\beta$ Steering Visualization}\\label{sec:appendix-steering-viz}\n765-\n766-Figure~\\ref{fig:steering-4panel} visualizes per-turn GAR trajectories under four steering strengths ($\\beta$\\,=\\,0, 3, 5, 10), revealing the turn-level dynamics that underlie the aggregate steering results in Table~\\ref{tab:steering-full}.\n767-\n768-\\paragraph{Unsteered baseline ($\\beta$\\,=\\,0).} GAR decays monotonically from 0.12 to 0.02 over five turns, with the steepest decline between turns~1 and~2 ($-$44\\%). This trajectory matches the per-turn profiles in Appendix~\\ref{sec:appendix-perturn-detail} and confirms that the decay is a smooth, progressive phenomenon rather than a discrete failure at a specific turn.\n769-\n--\n784-\n785:\\section{Llama-3.1-8B Scheduled Sampling Details}\\label{sec:appendix-llama-ss}\n786-\n787-[Omitted long context line]\n788-\n789-\\paragraph{$\\beta$-steering on Llama SS.}\n790-Table~\\ref{tab:llama-ss-steering} reports $\\beta$-steering results on the Llama SS model. Unlike Qwen, $\\beta$\\,=\\,3 does not trigger recovery on Llama (GAR 0.173 vs.\\ 0.166 at $\\beta$\\,=\\,0). At $\\beta$\\,=\\,5, GAR reaches 0.791---higher than Qwen's 0.717---suggesting that Llama's attention distribution is more responsive to the additive bias at higher steering strengths, possibly because the lower baseline AR GAR leaves more headroom for steering to exploit.\n--\n834-\n835:\\section{Use of AI Assistants}\\label{sec:appendix-ai}\n836-\n837-We used Claude (Anthropic) as an AI coding and writing assistant\n838-throughout this work. Specifically:\n839-\\begin{itemize}\n840-    \\item \\textbf{Code:} drafting experiment scripts, data-processing",
    "numLines": 87
  },
  "sourceToolAssistantUUID": "b7c346ee-51f1-4a03-bc98-600e879dfc6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool result

_source line 1137 · 2026-05-25T09:10:26.787Z_

<details><summary>↩ Tool result · `toolu_01HHBMmU8hLeBmGbeB8biKSf`</summary>

```text
1	\section{Training Configuration}\label{sec:appendix-hyper}
2	
3	Table~\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\times$ learning rate multiplier and are initialized with bias 1.5 ($\sigma(1.5) \approx 0.82$); the gate MLP adds ${\sim}$57K parameters per variant ($<$0.001\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB VRAM), requiring 6--8 hours per variant.
4	
5	\begin{table}[h]
6	\centering\small
7	\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\dagger$ apply only to ThreadGate and its ablations.}
8	\label{tab:hyperparams}
9	\begin{tabular}{l@{\hspace{8pt}}l}
10	\toprule
11	\textbf{Parameter} & \textbf{Value} \\
12	\midrule
13	Base model & Qwen-2.5-7B-Instruct \\
14	LoRA rank / $\alpha$ & 16 / 32 \\
15	LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
16	Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
17	Learning rate & $2 \times 10^{-4}$ \\
18	Gate LR mult.$^\dagger$ & $10\times$ \\
19	Batch / grad accum & 1 / 8 (eff.\ 8) \\
20	Epochs & 3 \\
21	Max seq length & 2048 \\
22	Training data & 8K UltraChat convs \\
23	Seed & 42 (+123 for TG, SS) \\
24	$\lambda_\text{GAR}$/$\lambda_\text{div}$ & 1.0 / 1.0 \\
25	GAR target $\tau$ & 0.5 \\
26	Gate init bias$^\dagger$ & 1.5 ($\sigma\!\approx\!0.82$) \\
27	Gate hidden dim$^\dagger$ & 64 \\
28	Turn embed dim$^\dagger$ & 16 \\
29	GPU & RTX PRO 6000 (96\,GB) \\
30	Training time & 6--8 h / variant \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Loss Formulation Search}\label{sec:appendix-loss}
36	
37	The final MSE + gate diversity loss (\S\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.
38	
39	\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.
40	
41	\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\text{mean}(\text{GAR})$). The unbounded objective rewards full pass-through ($g \to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\lambda$=2 (v3), gates froze within 100 steps; at $\lambda$=10 (v3b), convergence to identity accelerated; at $\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.
42	
43	\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.
44	
45	\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\tau$ incurs the same penalty as GAR below $\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\mathcal{L}_\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).
46	
47	\begin{table*}[t]
48	\centering\footnotesize
49	\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}
50	\label{tab:loss-iterations}
51	\begin{tabular}{l l l p{5.8cm} c c}
52	\toprule
53	 & \textbf{Loss Family} & \textbf{Status} & \textbf{Failure Mechanism} & \textbf{GAR} & \textbf{PPL} \\
54	\midrule
55	v1  & Cumulative            & \texttimes~GAR loss $\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\
56	v2  & Cumulative + $\varepsilon$ & \texttimes~same trajectory & Numerical instability from cumulative product; $\varepsilon$-stabilization insufficient & ---  & ---  \\
57	v3  & Maximize ($\lambda$=2)  & \texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\
58	v3b & Maximize ($\lambda$=10) & \texttimes~identity collapse   & Higher $\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\
59	v5  & Maximize ($\lambda$=1)  & \texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\
60	v6  & Smooth saturation       & \texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\
61	v7  & MSE + gate div          & \checkmark~\textbf{converged}  & \textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\
62	\bottomrule
63	\end{tabular}
64	\end{table*}
65	
66	\section{Instruction Retention Details}\label{sec:appendix-ir}
67	
68	To evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\beta$\,=\,3 steering on $N$\,=\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.
69	
70	\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\,=\,54 paired evaluations (18 types $\times$ 3 conversations per type) for the McNemar analysis.
71	
72	\paragraph{Per-category results.} Table~\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.
73	
74	\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\,=\,0.200, $p$\,=\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\,=\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.
75	
76	Figure~\ref{fig:ir-bar} visualizes the per-category breakdown.
77	
78	\begin{figure}[h]
79	  \centering
80	  \includegraphics[width=\columnwidth]{fig_instruction_retention.pdf}
81	  \caption{Instruction retention by constraint category under $\beta$\,=\,3 steering. Content constraints benefit most (+23.8\,pp); format and count constraints are unaffected.}
82	  \label{fig:ir-bar}
83	\end{figure}
84	
85	\begin{table}[h]
86	\centering\small
87	\caption{Instruction retention by constraint category ($\beta$\,=\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}
88	\label{tab:ir-results}
89	\begin{tabular}{lccc}
90	\toprule
91	\textbf{Category} & $\beta$\,=\,0 & $\beta$\,=\,3 & $\Delta$ \\
92	\midrule
93	Content    & 61.9\% & 85.7\% & +23.8\,pp \\
94	Position   & 66.7\% & 73.3\% & +6.7\,pp \\
95	Count      & 100\%  & 100\%  & 0 \\
96	Format     & 100\%  & 100\%  & 0 \\
97	\midrule
98	\textbf{Overall} & 75.9\% & 87.0\% & +11.1\,pp \\
99	\bottomrule
100	\end{tabular}
101	\end{table}
102	
103	\section{Long-Conversation AR Evaluation}\label{sec:appendix-n5}
104	
105	The main results (Table~\ref{tab:four-way}) report AR GAR from $N$\,=\,50 held-out conversations with a mean of 3.6 user turns. Table~\ref{tab:n5-ar} presents complementary results on $N$\,=\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.
106	
107	\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\times$ (0.064 vs.\ 0.037 in the $N$\,=\,50 evaluation) to 0.64$\times$ (0.016 vs.\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\,=\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.
108	
109	\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\times$ of the base model's GAR, compared to 3.4$\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.
110	
111	\paragraph{Caveats.} The $N$\,=\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.
112	
113	\begin{table}[h]
114	\centering\small
115	\caption{AR GAR-ours on $N$\,=\,5 ten-turn conversations. The gating advantage observed in Table~\ref{tab:four-way} ($N$\,=\,50, mean 3.6 turns) diminishes with conversation length.}
116	\label{tab:n5-ar}
117	\begin{tabular}{lcc}
118	\toprule
119	\textbf{Configuration} & \textbf{AR GAR-O} & \textbf{$\Delta$ vs.\ Table~\ref{tab:four-way}} \\
120	\midrule
121	Base & 0.012 & $-$0.007 \\
122	\midrule
123	ThreadGate & 0.016 & $-$0.048 \\
124	\;+\,PCGrad & 0.015 & $-$0.015 \\
125	Uniform Gate & 0.015 & $-$0.018 \\
126	LoRA-only & 0.025 & $-$0.012 \\
127	\bottomrule
128	\end{tabular}
129	\end{table}
130	
131	\section{Statistical Test Details}\label{sec:appendix-stats}
132	
133	All statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\ref{tab:stat-tests} consolidates the full results.
134	
135	\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\ LoRA-only comparison ($p$\,=\,0.004, $r$\,=\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\ +PCGrad comparison ($p$\,=\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.
136	
137	\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:four-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.
138	
139	\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \leq r < 0.5$ is medium, and $r \geq 0.5$ is large. The TG vs.\ LoRA-only effect ($r$\,=\,0.454) is medium, and TG vs.\ Base ($r$\,=\,0.802) is large.
140	
141	\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \leq 0.004$) survive this correction.
142	
143	\begin{table}[h]
144	\centering\small
145	\caption{Consolidated statistical tests. All AR comparisons use $N$\,=\,50 conversations (39 with $\geq$3 turns); gate conditioning uses 28 layers.}
146	\label{tab:stat-tests}
147	\begin{tabular}{llcc}
148	\toprule
149	\textbf{Comparison} & \textbf{Test} & $p$ & $r$ \\
150	\midrule
151	\multicolumn{4}{l}{\emph{AR GAR-ours ($\beta$\,=\,0)}} \\
152	TG vs.\ Base & Wilcoxon & $<$0.001 & 0.802 \\
153	TG vs.\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\
154	TG vs.\ +PCGrad & Wilcoxon & 0.002 & --- \\
155	SS vs.\ TG & Wilcoxon & $<$0.001 & 0.869 \\
156	\midrule
157	\multicolumn{4}{l}{\emph{Gate conditioning (28 layers)}} \\
158	Turn 1 vs.\ Turn 21 & Wilcoxon & $3.7\!\times\!10^{-8}$ & 0.975 \\
159	\midrule
160	\multicolumn{4}{l}{\emph{Instruction retention}} \\
161	$\beta$\,=\,0 vs.\ $\beta$\,=\,3 & McNemar & 0.077 & --- \\
162	GAR--compliance & Pearson & 0.007 & 0.200 \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	
167	\section{Llama-3.1-8B Complete Results}\label{sec:appendix-llama}
168	
169	Table~\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \S\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.
170	
171	\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\ 0.50).
172	
173	\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\,=\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\% for ThreadGate (mean 0.043, std 0.100), and 5\% of turn-level measurements exhibit sporadic attention spikes (GAR $\geq$ 0.4). We therefore report both mean and median.
174	
175	\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\,=\,0.793, L5\,=\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\,=\,0.719, L24\,=\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\times$ by median for Llama vs.\ 8--17$\times$ for Qwen).
176	
177	\begin{table}[h]
178	\centering\small
179	\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\,=\,50); AR: autoregressive ($N$\,=\,20 for Base/TG/LoRA-only, $N$\,=\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}
180	\label{tab:llama-full}
181	\resizebox{\columnwidth}{!}{%
182	\begin{tabular}{lcccc}
183	\toprule
184	& \multicolumn{2}{c}{\textbf{TF}} & \multicolumn{2}{c}{\textbf{AR}} \\
185	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
186	& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\
187	\midrule
188	Base & 0.017 & 3.45 & 0.009 & 0.009 \\
189	ThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\
190	LoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\
191	\textbf{SS} & 0.477 & 2.82 & \textbf{0.166} & --- \\
192	\bottomrule
193	\end{tabular}}
194	\end{table}
195	
196	\begin{figure}[t]
197	  \centering
198	  \includegraphics[width=\columnwidth]{fig_crossmodel.pdf}
199	  \caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\times$ by median), exceeding Qwen's 8$\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}
200	  \label{fig:crossmodel}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "288cc4ca-c34d-452c-8c68-d59c69e93dab",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "d9d804a8-3cba-4b82-b254-1ed9a0b7359b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
      "content": "\\section{Training Configuration}\\label{sec:appendix-hyper}\n\nTable~\\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\\times$ learning rate multiplier and are initialized with bias 1.5 ($\\sigma(1.5) \\approx 0.82$); the gate MLP adds ${\\sim}$57K parameters per variant ($<$0.001\\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB VRAM), requiring 6--8 hours per variant.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\\dagger$ apply only to ThreadGate and its ablations.}\n\\label{tab:hyperparams}\n\\begin{tabular}{l@{\\hspace{8pt}}l}\n\\toprule\n\\textbf{Parameter} & \\textbf{Value} \\\\\n\\midrule\nBase model & Qwen-2.5-7B-Instruct \\\\\nLoRA rank / $\\alpha$ & 16 / 32 \\\\\nLoRA targets & \\texttt{q\\_proj}, \\texttt{v\\_proj} \\\\\nOptimizer & AdamW ($\\beta_1$\\!=\\!0.9, $\\beta_2$\\!=\\!0.999) \\\\\nLearning rate & $2 \\times 10^{-4}$ \\\\\nGate LR mult.$^\\dagger$ & $10\\times$ \\\\\nBatch / grad accum & 1 / 8 (eff.\\ 8) \\\\\nEpochs & 3 \\\\\nMax seq length & 2048 \\\\\nTraining data & 8K UltraChat convs \\\\\nSeed & 42 (+123 for TG, SS) \\\\\n$\\lambda_\\text{GAR}$/$\\lambda_\\text{div}$ & 1.0 / 1.0 \\\\\nGAR target $\\tau$ & 0.5 \\\\\nGate init bias$^\\dagger$ & 1.5 ($\\sigma\\!\\approx\\!0.82$) \\\\\nGate hidden dim$^\\dagger$ & 64 \\\\\nTurn embed dim$^\\dagger$ & 16 \\\\\nGPU & RTX PRO 6000 (96\\,GB) \\\\\nTraining time & 6--8 h / variant \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Loss Formulation Search}\\label{sec:appendix-loss}\n\nThe final MSE + gate diversity loss (\\S\\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~\\ref{tab:loss-iterations} summarizes the progression. The search was motivated by a consistent failure mode: naive formulations either collapse to trivial solutions (cumulative losses) or drive gates toward identity (maximize-family losses). We describe each family below.\n\n\\paragraph{Cumulative losses (v1--v2).} These losses accumulate GAR contributions across layers, rewarding monotonically increasing attention. v1 collapsed because once the cumulative GAR exceeded the threshold, the loss gradient vanished and gates froze. v2 added an $\\varepsilon$-stabilization term to the cumulative product, but numerical instability from the product of 28 per-layer terms dominated, and training followed the same trajectory.\n\n\\paragraph{Maximize losses (v3--v5).} These losses directly maximize mean GAR ($-\\text{mean}(\\text{GAR})$). The unbounded objective rewards full pass-through ($g \\to 1.0$), collapsing gate diversity (std $<$ 0.025). At $\\lambda$=2 (v3), gates froze within 100 steps; at $\\lambda$=10 (v3b), convergence to identity accelerated; at $\\lambda$=1 (v5), rebalancing delayed but did not prevent the same degenerate solution.\n\n\\paragraph{Smooth saturation (v6).} This bounded the reward using a saturating function, intended to prevent the unbounded growth of maximize losses. In practice, the loss landscape remained monotonic in $g$, and training followed the same terminal trajectory as the maximize family, only more slowly.\n\n\\paragraph{MSE + gate diversity (v7).} The MSE formulation provides bidirectional pressure: GAR above $\\tau$ incurs the same penalty as GAR below $\\tau$, preventing the runaway optimization of maximize losses. The gate diversity regularizer ($\\mathcal{L}_\\text{div}$) enforces a minimum standard deviation across per-layer gate values, preventing all gates from collapsing to a uniform value. This combination is the only one that achieved stable convergence (GAR-ours = 0.50, PPL = 2.78).\n\n\\begin{table*}[t]\n\\centering\\footnotesize\n\\caption{Loss formulation iterations on Qwen-2.5-7B-Instruct. GAR-ours (teacher-forced) and PPL are reported only for the converged configuration (v7).}\n\\label{tab:loss-iterations}\n\\begin{tabular}{l l l p{5.8cm} c c}\n\\toprule\n & \\textbf{Loss Family} & \\textbf{Status} & \\textbf{Failure Mechanism} & \\textbf{GAR} & \\textbf{PPL} \\\\\n\\midrule\nv1  & Cumulative            & \\texttimes~GAR loss $\\to$ 0     & GAR loss collapses to zero once threshold is reached; gate gradients vanish at equilibrium & ---  & ---  \\\\\nv2  & Cumulative + $\\varepsilon$ & \\texttimes~same trajectory & Numerical instability from cumulative product; $\\varepsilon$-stabilization insufficient & ---  & ---  \\\\\nv3  & Maximize ($\\lambda$=2)  & \\texttimes~gate frozen        & Unbounded reward drives gates toward identity (all-pass); no layer selectivity & ---  & ---  \\\\\nv3b & Maximize ($\\lambda$=10) & \\texttimes~identity collapse   & Higher $\\lambda$ accelerates convergence to same degenerate identity solution & ---  & ---  \\\\\nv5  & Maximize ($\\lambda$=1)  & \\texttimes~identity collapse   & Rebalancing delays but does not prevent identity collapse & ---  & ---  \\\\\nv6  & Smooth saturation       & \\texttimes~identity collapse   & Monotonic reward identical to maximize in practice; boundedness slows but does not alter terminal trajectory & ---  & ---  \\\\\nv7  & MSE + gate div          & \\checkmark~\\textbf{converged}  & \\textbf{Bidirectional penalty prevents identity collapse; gate diversity regularizer enforces layer selectivity} & 0.50 & 2.78 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Instruction Retention Details}\\label{sec:appendix-ir}\n\nTo evaluate whether GAR improvements translate to downstream task performance, we test instruction retention across 18 system-prompt constraint types using the ThreadGate checkpoint with $\\beta$\\,=\\,3 steering on $N$\\,=\\,200 held-out conversations. Each constraint type requires the model to follow a specific instruction embedded in the system prompt (e.g., ``always respond in bullet points'', ``never use the word X'', ``include a summary at the end''). This evaluation bridges the gap between our attention-level metric (GAR) and observable model behavior.\n\n\\paragraph{Evaluation protocol.} For each conversation, we inject a constraint into the system prompt and evaluate compliance across all assistant turns. A turn is compliant if it satisfies the constraint according to rule-based checkers (for format, count, and position constraints) or GPT-4-based evaluation (for content constraints, which require semantic judgment). We use the same 18 constraint types across all conversations, yielding $N$\\,=\\,54 paired evaluations (18 types $\\times$ 3 conversations per type) for the McNemar analysis.\n\n\\paragraph{Per-category results.} Table~\\ref{tab:ir-results} reports per-category compliance rates. Content constraints---which require attending to and recalling specific system-prompt instructions across turns---show the largest improvement (+23.8\\,pp), consistent with GAR measuring attention to goal tokens. This category includes constraints like ``mention X in every response'' and ``always reference the original topic,'' which require sustained attention to the system prompt. Position constraints (e.g., ``start each response with Y'') show a modest improvement (+6.7\\,pp), as they partially depend on goal-token attention. Format (e.g., ``use bullet points'') and count constraints (e.g., ``exactly 3 sentences'') show no change, consistent with these being procedural patterns that are cached in the model's generation routine rather than requiring ongoing attention to the system prompt.\n\n\\paragraph{Correlation analysis.} The GAR-compliance correlation ($r$\\,=\\,0.200, $p$\\,=\\,0.007) is statistically significant but modest, suggesting that attention to goal tokens is one of several factors in instruction compliance. Other factors likely include the model's procedural memory for format constraints, the specificity of the constraint (vague constraints are harder regardless of attention), and the interaction between constraint type and conversation topic. McNemar's test ($p$\\,=\\,0.077) is marginally significant for the overall compliance improvement, reflecting the small sample size (18 constraint types). These results are exploratory and pending multi-model confirmation.\n\nFigure~\\ref{fig:ir-bar} visualizes the per-category breakdown.\n\n\\begin{figure}[h]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_instruction_retention.pdf}\n  \\caption{Instruction retention by constraint category under $\\beta$\\,=\\,3 steering. Content constraints benefit most (+23.8\\,pp); format and count constraints are unaffected.}\n  \\label{fig:ir-bar}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Instruction retention by constraint category ($\\beta$\\,=\\,3 steering on ThreadGate checkpoint). Content constraints benefit most from increased goal attention.}\n\\label{tab:ir-results}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Category} & $\\beta$\\,=\\,0 & $\\beta$\\,=\\,3 & $\\Delta$ \\\\\n\\midrule\nContent    & 61.9\\% & 85.7\\% & +23.8\\,pp \\\\\nPosition   & 66.7\\% & 73.3\\% & +6.7\\,pp \\\\\nCount      & 100\\%  & 100\\%  & 0 \\\\\nFormat     & 100\\%  & 100\\%  & 0 \\\\\n\\midrule\n\\textbf{Overall} & 75.9\\% & 87.0\\% & +11.1\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Long-Conversation AR Evaluation}\\label{sec:appendix-n5}\n\nThe main results (Table~\\ref{tab:four-way}) report AR GAR from $N$\\,=\\,50 held-out conversations with a mean of 3.6 user turns. Table~\\ref{tab:n5-ar} presents complementary results on $N$\\,=\\,5 conversations with 10 turns each, testing whether the observed patterns generalize beyond the training distribution's conversation length.\n\n\\paragraph{Gating advantage vanishes at length.} In these longer dialogues, the gating advantage observed in shorter conversations vanishes: all fine-tuned variants collapse to AR GAR-ours of 0.015--0.025, compared to 0.030--0.064 in the shorter evaluation. ThreadGate's advantage over LoRA-only shrinks from 1.7$\\times$ (0.064 vs.\\ 0.037 in the $N$\\,=\\,50 evaluation) to 0.64$\\times$ (0.016 vs.\\ 0.025), actually reversing the ordering. This reversal is not statistically robust given the small sample ($N$\\,=\\,5) but directionally suggests that architectural modifications provide diminishing returns as conversation length increases and exposure bias accumulates.\n\n\\paragraph{Convergence to base.} By turn~10, all fine-tuned variants converge to within 2$\\times$ of the base model's GAR, compared to 3.4$\\times$ at turn~1 in the shorter evaluation. This convergence is consistent with exposure bias compounding multiplicatively over turns: each model-generated turn introduces additional distributional drift from the teacher-forced training regime, and by turn~10 the accumulated drift overwhelms any gating or LoRA signal, leaving only the base model's intrinsic attention patterns.\n\n\\paragraph{Caveats.} The $N$\\,=\\,5 sample size limits statistical power, and the 10-turn conversations may differ systematically from the 3--5 turn training distribution in ways beyond length (e.g., topic complexity, user engagement patterns). We present these results as directional evidence rather than definitive conclusions.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{AR GAR-ours on $N$\\,=\\,5 ten-turn conversations. The gating advantage observed in Table~\\ref{tab:four-way} ($N$\\,=\\,50, mean 3.6 turns) diminishes with conversation length.}\n\\label{tab:n5-ar}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Configuration} & \\textbf{AR GAR-O} & \\textbf{$\\Delta$ vs.\\ Table~\\ref{tab:four-way}} \\\\\n\\midrule\nBase & 0.012 & $-$0.007 \\\\\n\\midrule\nThreadGate & 0.016 & $-$0.048 \\\\\n\\;+\\,PCGrad & 0.015 & $-$0.015 \\\\\nUniform Gate & 0.015 & $-$0.018 \\\\\nLoRA-only & 0.025 & $-$0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Statistical Test Details}\\label{sec:appendix-stats}\n\nAll statistical tests reported in the main text use non-parametric methods due to the non-normal, heavy-tailed distribution of per-conversation GAR values. Table~\\ref{tab:stat-tests} consolidates the full results.\n\n\\paragraph{Wilcoxon signed-rank tests.} We use paired Wilcoxon signed-rank tests for all pairwise configuration comparisons under AR evaluation, treating each conversation as a paired observation. The TG vs.\\ LoRA-only comparison ($p$\\,=\\,0.004, $r$\\,=\\,0.454) confirms that turn-conditioned gating provides a statistically significant but modest improvement. The TG vs.\\ +PCGrad comparison ($p$\\,=\\,0.002) shows that resolving gradient conflict is actively harmful. Gate turn conditioning uses an unpaired Wilcoxon test across 28 layers.\n\n\\paragraph{Bootstrap confidence intervals.} The 95\\% CIs in Table~\\ref{tab:four-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.\n\n\\paragraph{Effect sizes.} We report rank-biserial correlation $r = Z / \\sqrt{N}$ as the effect size for Wilcoxon tests, where $Z$ is the standardized test statistic and $N$ is the number of observations. By standard conventions: $r < 0.3$ is small, $0.3 \\leq r < 0.5$ is medium, and $r \\geq 0.5$ is large. The TG vs.\\ LoRA-only effect ($r$\\,=\\,0.454) is medium, and TG vs.\\ Base ($r$\\,=\\,0.802) is large.\n\n\\paragraph{Multiple comparisons.} We report uncorrected $p$-values throughout, as our comparisons are hypothesis-driven (each tests a specific causal exclusion) rather than exploratory. Applying Bonferroni correction to the 4 primary AR comparisons would adjust the significance threshold to 0.0125; all reported significant results ($p \\leq 0.004$) survive this correction.\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Consolidated statistical tests. All AR comparisons use $N$\\,=\\,50 conversations (39 with $\\geq$3 turns); gate conditioning uses 28 layers.}\n\\label{tab:stat-tests}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Comparison} & \\textbf{Test} & $p$ & $r$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{AR GAR-ours ($\\beta$\\,=\\,0)}} \\\\\nTG vs.\\ Base & Wilcoxon & $<$0.001 & 0.802 \\\\\nTG vs.\\ LoRA-only & Wilcoxon & 0.004 & 0.454 \\\\\nTG vs.\\ +PCGrad & Wilcoxon & 0.002 & --- \\\\\nSS vs.\\ TG & Wilcoxon & $<$0.001 & 0.869 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Gate conditioning (28 layers)}} \\\\\nTurn 1 vs.\\ Turn 21 & Wilcoxon & $3.7\\!\\times\\!10^{-8}$ & 0.975 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Instruction retention}} \\\\\n$\\beta$\\,=\\,0 vs.\\ $\\beta$\\,=\\,3 & McNemar & 0.077 & --- \\\\\nGAR--compliance & Pearson & 0.007 & 0.200 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Llama-3.1-8B Complete Results}\\label{sec:appendix-llama}\n\nTable~\\ref{tab:llama-full} presents the complete Llama-3.1-8B-Instruct results, complementing the summary in \\S\\ref{subsec:cross-model}. Three configurations were trained (Base, ThreadGate, LoRA-only) using the same training pipeline as Qwen-2.5-7B (8K UltraChat, 3 epochs, LoRA rank 16). Training required 7.0--7.3 hours per variant on the same GPU.\n\n\\paragraph{Teacher-forced evaluation.} TF GAR-ours is 0.484 (TG) and 0.481 (LoRA-only), confirming that gating provides zero benefit under teacher forcing on Llama, consistent with the Qwen results (0.50 vs.\\ 0.50).\n\n\\paragraph{Autoregressive evaluation.} AR evaluation uses $N$\\,=\\,20 mid-turn conversations (turns 3--$T$, excluding the first two turns to avoid initialization effects). The AR GAR distribution is heavy-tailed: the coefficient of variation exceeds 100\\% for ThreadGate (mean 0.043, std 0.100), and 5\\% of turn-level measurements exhibit sporadic attention spikes (GAR $\\geq$ 0.4). We therefore report both mean and median.\n\n\\paragraph{Gate profile.} Llama's gate profile differs qualitatively from Qwen's: Qwen shows minimum attenuation at early layers (L1\\,=\\,0.793, L5\\,=\\,0.797), while Llama shows a V-shaped valley at mid-to-late layers (L25\\,=\\,0.719, L24\\,=\\,0.809). Despite this architectural difference, both models converge toward identity under NTP pressure, and the TF-AR gap is comparable (27$\\times$ by median for Llama vs.\\ 8--17$\\times$ for Qwen).\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{Llama-3.1-8B-Instruct complete results. TF: teacher-forced ($N$\\,=\\,50); AR: autoregressive ($N$\\,=\\,20 for Base/TG/LoRA-only, $N$\\,=\\,50 for SS). Median is more representative due to heavy-tailed AR distributions (SS uses mean only).}\n\\label{tab:llama-full}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{TF}} & \\multicolumn{2}{c}{\\textbf{AR}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n& GAR-O & PPL & GAR-O (mean) & GAR-O (med) \\\\\n\\midrule\nBase & 0.017 & 3.45 & 0.009 & 0.009 \\\\\nThreadGate & 0.484 & 2.57 & 0.043 & 0.018 \\\\\nLoRA-only & 0.481 & 2.60 & 0.028 & 0.018 \\\\\n\\textbf{SS} & 0.477 & 2.82 & \\textbf{0.166} & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_crossmodel.pdf}\n  \\caption{Cross-architecture validation. (a)~The TF-AR gap persists on Llama-3.1-8B (27$\\times$ by median), exceeding Qwen's 8$\\times$. (b)~Gate profiles on normalized depth: Qwen dips at early layers, Llama at late layers; architecture-dependent patterns, but both converge toward identity.}\n  \\label{fig:crossmodel}",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 847
    }
  },
  "sourceToolAssistantUUID": "288cc4ca-c34d-452c-8c68-d59c69e93dab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool call

_source line 1138 · 2026-05-25T09:10:29.072Z_

<details open><summary>🔧 Tool call — Grep · `toolu_0166nktmvi7aNvVdkRcnoZMM`</summary>

```json
{
  "pattern": "\\\\label\\{sec:appendix-(ar-gar-dynamics|perturn-detail|dataset-ext|gar-ext|mmlu-ext|1\\.5b-ext|stats-ext|training-ext|steering-viz|llama-ss|ai)\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex",
  "output_mode": "content",
  "-B": 1,
  "-A": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9d804a8-3cba-4b82-b254-1ed9a0b7359b",
  "isSidechain": false,
  "requestId": "req_011CbP2WDS7C6hdAggyyPWns",
  "type": "assistant",
  "uuid": "b7c346ee-51f1-4a03-bc98-600e879dfc6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GLr8ey8RuKako3LLRxdgKz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2300,
      "cache_read_input_tokens": 50348,
      "output_tokens": 363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2300,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 363,
          "cache_read_input_tokens": 50348,
          "cache_creation_input_tokens": 2300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2300
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

_source line 1139 · 2026-05-25T09:10:29.124Z_

```json
{
  "parentUuid": "3fb16c0e-6f50-486a-9e5a-f6c4a9c7b49e",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e458bd41-6c87-4dd0-8bfd-2ea8dbc02602",
  "timestamp": "2026-05-25T09:10:29.124Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---


### Runtime record

_source line 1140_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 附录内容引用完整性检查  **任务：** 检查论文附录的所有内容是否在正文中都有准确、合理的引用，修复孤儿附录。  **Step 1：逐项盘点** 列出附录里每一个 section/subsection/table/figure/algorithm/proof/prompt。  **Step 2：逐项验证引用** 对每一项，在正文搜索是否有至少一句话指向…",
  "leafUuid": "e458bd41-6c87-4dd0-8bfd-2ea8dbc02602",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1141_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Assistant

_source line 1142 · 2026-05-25T09:11:48.845Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me map each orphan to its best insertion point in the main text:

1. `sec:appendix-ar-gar-dynamics` — Per-Turn AR GAR Dynamics — This shows per-turn AR GAR trajectories across configurations. Best fit: §5.3 Distribution Shift Analysis (which already mentions "77--87% per-turn decay") or §4.2 Main Results (AR generation discussion).

2. `sec:appendix-perturn-detail` — Per-Turn GAR Decay Analysis — Per-turn AR GAR values for all configurations on both architectures. 

Best fit: §5.3 or §4.2 where aggregate mid-turn GAR is reported.

3. `sec:appendix-dataset-ext` — Extended Dataset Statistics — I notice there's already a reference to dataset statistics in the appendix at line 6 of experiments.tex, but this extended version is a separate label, so it needs its own placement. Best fit: §4.1 Setup, where I can add a reference to this more detailed breakdown.

4. `sec:appendix-gar-ext` — Extended GAR Robustness Analysis — The main text references `appendix-gar-robust` in §4.4, which appears to be a different section. I need to verify whether these are distinct appendices or if one should replace the other.

5. `sec:appendix-mmlu-ext` — MMLU Category Breakdown — The text already cites `appendix-mmlu` for the 5-shot accuracy results, so I'm checking whether this extended version should be a separate appendix or consolidated with the existing one.

6. `sec:appendix-1.5b-ext` — Extended Cross-Scale Results (1.5B) — The main text references `appendix-1.5b` for the Qwen-2.5-1.5B validation, making this extended version potentially redundant.

7. `sec:appendix-stats-ext` — Extended Statistical Analysis — Similar pattern here: the base `appendix-stats` is already referenced, so the extended version appears to be orphaned.

8. `sec:appendix-training-ext` — Extended Training Dynamics — This section contains training dynamics plots across all experimental conditions.

So I'm seeing a pattern where several appendices have both a base version and an `-ext` version, but only the base versions are actually cited in the main text. I need to determine whether these extended versions should be merged with their base counterparts or if they're genuinely separate supplementary materials.

Let me think through where to anchor these orphaned sections. For the ones with clear thematic homes, I can add citations in the relevant main-text sections. For instance, the AR-GAR dynamics section fits naturally into the distribution shift analysis discussion in §5.3, where the text already talks about the per-turn decay rates. I can extend the existing references for several more appendices. For MMLU, I'll add the category breakdown reference in the Main Results section where MMLU is already mentioned. Similarly, I'll extend references for the 1.5B model results in the Cross-Model section, add stats references near the existing ones in Main Results or PCGrad, and include training dynamics in Main Results or Gate Conditioning since they're relevant there. I'll also add the steering visualization reference in the Steering section where β-steering is discussed, the Llama results in Cross-Model, and note that the AI disclosure section can stand alone.

For the AI disclosure appendix, I'm reconsidering whether it needs a main-text reference. The Director's guidance prioritizes natural references in relevant sections, but allows standalone appendices when they're standard disclosures. Since this is a typical disclosure section, I could either leave it as-is or add a brief mention in the Limitations section pointing to it. Many papers handle this without forcing a reference, so I'll keep it standalone without a forced citation.

Now I'm planning the specific edits for the other appendices. I need to be strategic about where to add references since page limits are tight—these will all be parenthetical additions to minimize space. For the attention dynamics appendix, I'll reference it in section 5.3 after discussing the decay rates. For the per-turn details appendix, the best placement is in section 4.2 where the main results are presented, since that appendix complements the aggregate values shown there. I need to figure out the best way to reference the extended GAR robustness analysis—it feels awkward to just tack it on, so I'll go with adding it as a separate extended analysis reference rather than trying to chain them together awkwardly.

For the MMLU breakdown, I can add a per-category reference right after the main appendix citation. The 1.5B extended diagnostics should follow the same pattern. The stats extension needs to mention the full test battery, and for the training dynamics appendix, it makes sense to place it in the Gate Conditioning section since that's where the discussion of NTP pressure and gate behavior happens—I'll add it after the existing gate profile reference.

The steering visualization appendix fits naturally in section 4.3 after the recovery figure, specifying the per-beta turn-level details. For Llama, I can add the cross-model specifics reference in section 5.5 where the SS results are discussed. Finally, in the Limitations section, I should disclose the AI assistant usage details with a straightforward appendix reference.

Now I'm going through each edit location carefully to ensure the old strings are distinct enough for reliable replacement. Let me pull the exact lines from analysis.tex to make precise substitutions.

For the second edit in analysis.tex §5.5, I'm updating the reference to the cross-model comparison figure to also point to the per-turn detail appendix. For the third edit in experiments.tex §4.1, I'm extending the dataset statistics reference to include the new extended dataset appendix. Moving on to the fourth edit location in experiments.tex §4.4...

Actually, let me reconsider the MMLU edit. The current text says "MMLU 5-shot accuracy remains within 0.8\,pp across all variants (Appendix~\ref{sec:appendix-mmlu})." I want to change this to point to the category breakdown in the extended appendix instead, so it becomes "(Appendix~\ref{sec:appendix-mmlu-ext})".

For the 1.5B model analysis, I'm adding a reference to extended diagnostics in a separate appendix section. And for the statistical tests, I'm expanding the reference to include the full test battery in another appendix section.

I'm also updating the gate profile reference to point to training dynamics in an additional appendix, and for the steering recovery results, I'm adding a reference to per-beta turn-level plots. The list continues with more appendix cross-references to be added throughout the document. I need to reconsider the approach here. The Director's feedback is clear: each appendix reference should feel integrated into the narrative, not just appended as a patch. Rather than simply citing "See Appendix X," I should explain why readers would want to look there and what they'll discover. Let me review each reference to ensure it's naturally embedded in the relevant section and provides context for what readers will find. Working through the remaining appendix references—most of these feel natural as-is when integrated into their respective sections. For the Llama screenshot reference, I need to find a better spot than a parenthetical to mention it.

Now I'm ready to apply these edits across the three main files, being mindful that these are all small additions to existing references, so page overflow shouldn't be an issue. I'll use `\looseness=-1` to handle any minor spacing adjustments needed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e458bd41-6c87-4dd0-8bfd-2ea8dbc02602",
  "isSidechain": false,
  "requestId": "req_011CbP2WjHy5uASwm3qPY58b",
  "type": "assistant",
  "uuid": "d5dc8438-886d-46d9-8af7-17deeadc6c5d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UzhVWnWMcT1QNG5JTcZCNs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8284,
      "cache_read_input_tokens": 52648,
      "output_tokens": 5088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8284,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5088,
          "cache_read_input_tokens": 52648,
          "cache_creation_input_tokens": 8284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8284
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

_source line 1143 · 2026-05-25T09:11:48.847Z_

I have a clear picture of all 11 orphans and where they naturally fit. Let me make the edits now — I'll add references within existing parenthetical contexts to keep them natural.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5dc8438-886d-46d9-8af7-17deeadc6c5d",
  "isSidechain": false,
  "requestId": "req_011CbP2WjHy5uASwm3qPY58b",
  "type": "assistant",
  "uuid": "4f07b4da-5fcf-4f87-bc5a-d7c45d570f98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UzhVWnWMcT1QNG5JTcZCNs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8284,
      "cache_read_input_tokens": 52648,
      "output_tokens": 5088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8284,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5088,
          "cache_read_input_tokens": 52648,
          "cache_creation_input_tokens": 8284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8284
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

_source line 1144 · 2026-05-25T09:11:50.724Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01KKWTqB3f7xU5bv4Kv9bWGb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "old_string": "dataset statistics in Appendix~\\ref{sec:appendix-data}",
  "new_string": "dataset statistics in Appendices~\\ref{sec:appendix-data} and~\\ref{sec:appendix-dataset-ext}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f07b4da-5fcf-4f87-bc5a-d7c45d570f98",
  "isSidechain": false,
  "requestId": "req_011CbP2WjHy5uASwm3qPY58b",
  "type": "assistant",
  "uuid": "a6252ebe-aaec-4a97-9aec-917f1d9db8cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UzhVWnWMcT1QNG5JTcZCNs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8284,
      "cache_read_input_tokens": 52648,
      "output_tokens": 5088,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8284,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5088,
          "cache_read_input_tokens": 52648,
          "cache_creation_input_tokens": 8284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8284
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

_source line 1145 · 2026-05-25T09:11:50.747Z_

<details><summary>↩ Tool result · `toolu_01KKWTqB3f7xU5bv4Kv9bWGb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6252ebe-aaec-4a97-9aec-917f1d9db8cc",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "3ecd8877-d078-4081-9cbd-115abf0c10ff",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
    "oldString": "dataset statistics in Appendix~\\ref{sec:appendix-data}",
    "newString": "dataset statistics in Appendices~\\ref{sec:appendix-data} and~\\ref{sec:appendix-dataset-ext}",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\nWe fine-tune Qwen-2.5-7B-Instruct with LoRA \\citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \\citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; training costs in Appendix~\\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\\ref{sec:appendix-hyper}; dataset statistics in Appendix~\\ref{sec:appendix-data}; the controlled comparison design is described in \\S\\ref{sec:comparison-design}. We evaluate under \\emph{IID} (same-distribution UltraChat text) and \\emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \\citep{dongre2026attention}, and perplexity (PPL).\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\\leq$2\\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\\leq$1\\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, confirming that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\\S\\ref{subsec:ss}).\n\nUnder AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendix~\\ref{sec:appendix-stats}), yet the gap remains 7.8$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). MMLU 5-shot accuracy remains within 0.8\\,pp across all variants (Appendix~\\ref{sec:appendix-mmlu}). We analyze this distribution shift in \\S\\ref{sec:analysis}.\n\n\\subsection{Inference-Time Attention Steering}\\label{subsec:steering}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig5_attention_steering.pdf}\n  \\caption{Inference-time $\\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation as a proximal cause (9\\% PPL cost at $\\beta$\\,=\\,3; phase transition at $\\beta \\in [2, 3]$).}\n  \\label{fig:steering-recovery}\n\\end{figure}\n\nAll training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\\beta$ to pre-softmax attention logits for goal-token positions during generation:\n\\begin{equation}\n  \\tilde{A}_{i,j}^{(\\ell,h)} = A_{i,j}^{(\\ell,h)} + \\beta \\cdot \\mathbf{1}[j \\in \\mathcal{G}],\n\\end{equation}\nwhere $\\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\\beta \\in [0, 2]$ yields marginal improvement, then $\\beta = 3$ triggers a phase transition to GAR\\,=\\,0.556 (9\\% PPL cost). At $\\beta$\\,=\\,5, GAR reaches 0.727$\\pm$0.061 (PPL 1.77); the operating region $\\beta \\in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does---consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\\ref{sec:appendix-examples}). Downstream, steering ($\\beta$\\,=\\,3) raises late-turn instruction compliance by +11.1\\,pp, though this effect does not reach conventional significance ($p$\\,=\\,0.077; content-constrained tasks benefit most, +23.8\\,pp; Appendix~\\ref{sec:appendix-ir}).\n\n\\subsection{Scheduled Sampling Compresses the TF--AR Gap}\\label{subsec:ss}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_gap_compression.pdf}\n  \\caption{Scheduled sampling compresses the TF-AR gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$, the only variant approaching parity across five training conditions.}\n  \\label{fig:ss-gap}\n\\end{figure}\n\nScheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.001$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " ",
          " \\subsection{Setup}",
          " ",
          "-We fine-tune Qwen-2.5-7B-Instruct with LoRA \\citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \\citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; training costs in Appendix~\\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\\ref{sec:appendix-hyper}; dataset statistics in Appendix~\\ref{sec:appendix-data}; the controlled comparison design is described in \\S\\ref{sec:comparison-design}. We evaluate under \\emph{IID} (same-distribution UltraChat text) and \\emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \\citep{dongre2026attention}, and perplexity (PPL).",
          "+We fine-tune Qwen-2.5-7B-Instruct with LoRA \\citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \\citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; training costs in Appendix~\\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\\ref{sec:appendix-hyper}; dataset statistics in Appendices~\\ref{sec:appendix-data} and~\\ref{sec:appendix-dataset-ext}; the controlled comparison design is described in \\S\\ref{sec:comparison-design}. We evaluate under \\emph{IID} (same-distribution UltraChat text) and \\emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \\citep{dongre2026attention}, and perplexity (PPL).",
          " ",
          " \\subsection{Main Results}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "a6252ebe-aaec-4a97-9aec-917f1d9db8cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1146_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 附录内容引用完整性检查  **任务：** 检查论文附录的所有内容是否在正文中都有准确、合理的引用，修复孤儿附录。  **Step 1：逐项盘点** 列出附录里每一个 section/subsection/table/figure/algorithm/proof/prompt。  **Step 2：逐项验证引用** 对每一项，在正文搜索是否有至少一句话指向…",
  "leafUuid": "3ecd8877-d078-4081-9cbd-115abf0c10ff",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1147_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Tool call

_source line 1148 · 2026-05-25T09:11:59.462Z_

<details open><summary>🔧 Tool call — Edit · `toolu_0115zTR4r2MZNPp3GXwzwPhK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "old_string": "(Appendix~\\ref{sec:appendix-mmlu})",
  "new_string": "(per-category breakdown in Appendix~\\ref{sec:appendix-mmlu-ext})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ecd8877-d078-4081-9cbd-115abf0c10ff",
  "isSidechain": false,
  "requestId": "req_011CbP2ckS6HLikQ9RrXFXst",
  "type": "assistant",
  "uuid": "960525cc-8ef8-4926-bb00-a8b17b7f5b96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016MELW72tAWhxkhesrzEzss",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5160,
      "cache_read_input_tokens": 60932,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5160,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 60932,
          "cache_creation_input_tokens": 5160,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5160
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

_source line 1149 · 2026-05-25T09:11:59.472Z_

<details><summary>↩ Tool result · `toolu_0115zTR4r2MZNPp3GXwzwPhK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "960525cc-8ef8-4926-bb00-a8b17b7f5b96",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "6fad3432-add3-41f2-b62f-9c2403477245",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
    "oldString": "(Appendix~\\ref{sec:appendix-mmlu})",
    "newString": "(per-category breakdown in Appendix~\\ref{sec:appendix-mmlu-ext})",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\nWe fine-tune Qwen-2.5-7B-Instruct with LoRA \\citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \\citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; training costs in Appendix~\\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\\ref{sec:appendix-hyper}; dataset statistics in Appendices~\\ref{sec:appendix-data} and~\\ref{sec:appendix-dataset-ext}; the controlled comparison design is described in \\S\\ref{sec:comparison-design}. We evaluate under \\emph{IID} (same-distribution UltraChat text) and \\emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \\citep{dongre2026attention}, and perplexity (PPL).\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\\leq$2\\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\\leq$1\\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, confirming that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\\S\\ref{subsec:ss}).\n\nUnder AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendix~\\ref{sec:appendix-stats}), yet the gap remains 7.8$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). MMLU 5-shot accuracy remains within 0.8\\,pp across all variants (Appendix~\\ref{sec:appendix-mmlu}). We analyze this distribution shift in \\S\\ref{sec:analysis}.\n\n\\subsection{Inference-Time Attention Steering}\\label{subsec:steering}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig5_attention_steering.pdf}\n  \\caption{Inference-time $\\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation as a proximal cause (9\\% PPL cost at $\\beta$\\,=\\,3; phase transition at $\\beta \\in [2, 3]$).}\n  \\label{fig:steering-recovery}\n\\end{figure}\n\nAll training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\\beta$ to pre-softmax attention logits for goal-token positions during generation:\n\\begin{equation}\n  \\tilde{A}_{i,j}^{(\\ell,h)} = A_{i,j}^{(\\ell,h)} + \\beta \\cdot \\mathbf{1}[j \\in \\mathcal{G}],\n\\end{equation}\nwhere $\\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\\beta \\in [0, 2]$ yields marginal improvement, then $\\beta = 3$ triggers a phase transition to GAR\\,=\\,0.556 (9\\% PPL cost). At $\\beta$\\,=\\,5, GAR reaches 0.727$\\pm$0.061 (PPL 1.77); the operating region $\\beta \\in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does---consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\\ref{sec:appendix-examples}). Downstream, steering ($\\beta$\\,=\\,3) raises late-turn instruction compliance by +11.1\\,pp, though this effect does not reach conventional significance ($p$\\,=\\,0.077; content-constrained tasks benefit most, +23.8\\,pp; Appendix~\\ref{sec:appendix-ir}).\n\n\\subsection{Scheduled Sampling Compresses the TF--AR Gap}\\label{subsec:ss}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_gap_compression.pdf}\n  \\caption{Scheduled sampling compresses the TF-AR gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$, the only variant approaching parity across five training conditions.}\n  \\label{fig:ss-gap}\n\\end{figure}\n\nScheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.001$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " ",
          " Table~\\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\\leq$2\\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\\leq$1\\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, confirming that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\\S\\ref{subsec:ss}).",
          " ",
          "-Under AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendix~\\ref{sec:appendix-stats}), yet the gap remains 7.8$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). MMLU 5-shot accuracy remains within 0.8\\,pp across all variants (Appendix~\\ref{sec:appendix-mmlu}). We analyze this distribution shift in \\S\\ref{sec:analysis}.",
          "+Under AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendix~\\ref{sec:appendix-stats}), yet the gap remains 7.8$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). MMLU 5-shot accuracy remains within 0.8\\,pp across all variants (per-category breakdown in Appendix~\\ref{sec:appendix-mmlu-ext}). We analyze this distribution shift in \\S\\ref{sec:analysis}.",
          " ",
          " \\subsection{Inference-Time Attention Steering}\\label{subsec:steering}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "960525cc-8ef8-4926-bb00-a8b17b7f5b96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool call

_source line 1150 · 2026-05-25T09:12:02.906Z_

<details open><summary>🔧 Tool call — Edit · `toolu_012Pe49PV2eBDP3cK53Cx78k`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "old_string": "$p$\\,=\\,0.004; Appendix~\\ref{sec:appendix-stats})",
  "new_string": "$p$\\,=\\,0.004; Appendices~\\ref{sec:appendix-stats} and~\\ref{sec:appendix-stats-ext})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fad3432-add3-41f2-b62f-9c2403477245",
  "isSidechain": false,
  "requestId": "req_011CbP2dQ4X2vpaHodR1is5i",
  "type": "assistant",
  "uuid": "48bc94ad-305c-4b7f-8f9c-66e28b6f507f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014F2KKmFAMMnjqTLU9D5zW5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 238,
      "cache_read_input_tokens": 66092,
      "output_tokens": 210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 210,
          "cache_read_input_tokens": 66092,
          "cache_creation_input_tokens": 238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 238
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

_source line 1151 · 2026-05-25T09:12:02.916Z_

<details><summary>↩ Tool result · `toolu_012Pe49PV2eBDP3cK53Cx78k`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48bc94ad-305c-4b7f-8f9c-66e28b6f507f",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "1cf720e4-50ca-4152-8840-a7df8bc3628a",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
    "oldString": "$p$\\,=\\,0.004; Appendix~\\ref{sec:appendix-stats})",
    "newString": "$p$\\,=\\,0.004; Appendices~\\ref{sec:appendix-stats} and~\\ref{sec:appendix-stats-ext})",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\nWe fine-tune Qwen-2.5-7B-Instruct with LoRA \\citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \\citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; training costs in Appendix~\\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\\ref{sec:appendix-hyper}; dataset statistics in Appendices~\\ref{sec:appendix-data} and~\\ref{sec:appendix-dataset-ext}; the controlled comparison design is described in \\S\\ref{sec:comparison-design}. We evaluate under \\emph{IID} (same-distribution UltraChat text) and \\emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \\citep{dongre2026attention}, and perplexity (PPL).\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\\leq$2\\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\\leq$1\\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, confirming that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\\S\\ref{subsec:ss}).\n\nUnder AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendix~\\ref{sec:appendix-stats}), yet the gap remains 7.8$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). MMLU 5-shot accuracy remains within 0.8\\,pp across all variants (per-category breakdown in Appendix~\\ref{sec:appendix-mmlu-ext}). We analyze this distribution shift in \\S\\ref{sec:analysis}.\n\n\\subsection{Inference-Time Attention Steering}\\label{subsec:steering}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig5_attention_steering.pdf}\n  \\caption{Inference-time $\\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation as a proximal cause (9\\% PPL cost at $\\beta$\\,=\\,3; phase transition at $\\beta \\in [2, 3]$).}\n  \\label{fig:steering-recovery}\n\\end{figure}\n\nAll training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\\beta$ to pre-softmax attention logits for goal-token positions during generation:\n\\begin{equation}\n  \\tilde{A}_{i,j}^{(\\ell,h)} = A_{i,j}^{(\\ell,h)} + \\beta \\cdot \\mathbf{1}[j \\in \\mathcal{G}],\n\\end{equation}\nwhere $\\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\\beta \\in [0, 2]$ yields marginal improvement, then $\\beta = 3$ triggers a phase transition to GAR\\,=\\,0.556 (9\\% PPL cost). At $\\beta$\\,=\\,5, GAR reaches 0.727$\\pm$0.061 (PPL 1.77); the operating region $\\beta \\in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does---consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\\ref{sec:appendix-examples}). Downstream, steering ($\\beta$\\,=\\,3) raises late-turn instruction compliance by +11.1\\,pp, though this effect does not reach conventional significance ($p$\\,=\\,0.077; content-constrained tasks benefit most, +23.8\\,pp; Appendix~\\ref{sec:appendix-ir}).\n\n\\subsection{Scheduled Sampling Compresses the TF--AR Gap}\\label{subsec:ss}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_gap_compression.pdf}\n  \\caption{Scheduled sampling compresses the TF-AR gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$, the only variant approaching parity across five training conditions.}\n  \\label{fig:ss-gap}\n\\end{figure}\n\nScheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.001$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " ",
          " Table~\\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\\leq$2\\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\\leq$1\\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, confirming that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\\S\\ref{subsec:ss}).",
          " ",
          "-Under AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendix~\\ref{sec:appendix-stats}), yet the gap remains 7.8$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). MMLU 5-shot accuracy remains within 0.8\\,pp across all variants (per-category breakdown in Appendix~\\ref{sec:appendix-mmlu-ext}). We analyze this distribution shift in \\S\\ref{sec:analysis}.",
          "+Under AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendices~\\ref{sec:appendix-stats} and~\\ref{sec:appendix-stats-ext}), yet the gap remains 7.8$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). MMLU 5-shot accuracy remains within 0.8\\,pp across all variants (per-category breakdown in Appendix~\\ref{sec:appendix-mmlu-ext}). We analyze this distribution shift in \\S\\ref{sec:analysis}.",
          " ",
          " \\subsection{Inference-Time Attention Steering}\\label{subsec:steering}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "48bc94ad-305c-4b7f-8f9c-66e28b6f507f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool call

_source line 1152 · 2026-05-25T09:12:06.488Z_

<details open><summary>🔧 Tool call — Edit · `toolu_011S3g1XmeNdHyuxtjizpMwr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "old_string": "Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering})",
  "new_string": "Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering}; per-$\\beta$ turn-level trajectories in Appendix~\\ref{sec:appendix-steering-viz})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cf720e4-50ca-4152-8840-a7df8bc3628a",
  "isSidechain": false,
  "requestId": "req_011CbP2denYXds9EdZcS9Q3T",
  "type": "assistant",
  "uuid": "295b5a6f-6162-41e1-810e-5dddc26cf4b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CkrpUWkxjFnFsVoMEhX6XX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 66330,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 265,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 66330,
          "cache_creation_input_tokens": 265,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 265
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

_source line 1153 · 2026-05-25T09:12:06.497Z_

<details><summary>↩ Tool result · `toolu_011S3g1XmeNdHyuxtjizpMwr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "295b5a6f-6162-41e1-810e-5dddc26cf4b6",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "8f593965-1cf1-463b-b282-1fac214f414a",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
    "oldString": "Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering})",
    "newString": "Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering}; per-$\\beta$ turn-level trajectories in Appendix~\\ref{sec:appendix-steering-viz})",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\nWe fine-tune Qwen-2.5-7B-Instruct with LoRA \\citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \\citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; training costs in Appendix~\\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\\ref{sec:appendix-hyper}; dataset statistics in Appendices~\\ref{sec:appendix-data} and~\\ref{sec:appendix-dataset-ext}; the controlled comparison design is described in \\S\\ref{sec:comparison-design}. We evaluate under \\emph{IID} (same-distribution UltraChat text) and \\emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \\citep{dongre2026attention}, and perplexity (PPL).\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\\leq$2\\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\\leq$1\\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, confirming that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\\S\\ref{subsec:ss}).\n\nUnder AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendices~\\ref{sec:appendix-stats} and~\\ref{sec:appendix-stats-ext}), yet the gap remains 7.8$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). MMLU 5-shot accuracy remains within 0.8\\,pp across all variants (per-category breakdown in Appendix~\\ref{sec:appendix-mmlu-ext}). We analyze this distribution shift in \\S\\ref{sec:analysis}.\n\n\\subsection{Inference-Time Attention Steering}\\label{subsec:steering}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig5_attention_steering.pdf}\n  \\caption{Inference-time $\\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation as a proximal cause (9\\% PPL cost at $\\beta$\\,=\\,3; phase transition at $\\beta \\in [2, 3]$).}\n  \\label{fig:steering-recovery}\n\\end{figure}\n\nAll training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\\beta$ to pre-softmax attention logits for goal-token positions during generation:\n\\begin{equation}\n  \\tilde{A}_{i,j}^{(\\ell,h)} = A_{i,j}^{(\\ell,h)} + \\beta \\cdot \\mathbf{1}[j \\in \\mathcal{G}],\n\\end{equation}\nwhere $\\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\\beta \\in [0, 2]$ yields marginal improvement, then $\\beta = 3$ triggers a phase transition to GAR\\,=\\,0.556 (9\\% PPL cost). At $\\beta$\\,=\\,5, GAR reaches 0.727$\\pm$0.061 (PPL 1.77); the operating region $\\beta \\in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does---consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\\ref{sec:appendix-examples}). Downstream, steering ($\\beta$\\,=\\,3) raises late-turn instruction compliance by +11.1\\,pp, though this effect does not reach conventional significance ($p$\\,=\\,0.077; content-constrained tasks benefit most, +23.8\\,pp; Appendix~\\ref{sec:appendix-ir}).\n\n\\subsection{Scheduled Sampling Compresses the TF--AR Gap}\\label{subsec:ss}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_gap_compression.pdf}\n  \\caption{Scheduled sampling compresses the TF-AR gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$, the only variant approaching parity across five training conditions.}\n  \\label{fig:ss-gap}\n\\end{figure}\n\nScheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.001$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 24,
        "oldLines": 7,
        "newStart": 24,
        "newLines": 7,
        "lines": [
          " \\begin{equation}",
          "   \\tilde{A}_{i,j}^{(\\ell,h)} = A_{i,j}^{(\\ell,h)} + \\beta \\cdot \\mathbf{1}[j \\in \\mathcal{G}],",
          " \\end{equation}",
          "-where $\\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\\beta \\in [0, 2]$ yields marginal improvement, then $\\beta = 3$ triggers a phase transition to GAR\\,=\\,0.556 (9\\% PPL cost). At $\\beta$\\,=\\,5, GAR reaches 0.727$\\pm$0.061 (PPL 1.77); the operating region $\\beta \\in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does---consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\\ref{sec:appendix-examples}). Downstream, steering ($\\beta$\\,=\\,3) raises late-turn instruction compliance by +11.1\\,pp, though this effect does not reach conventional significance ($p$\\,=\\,0.077; content-constrained tasks benefit most, +23.8\\,pp; Appendix~\\ref{sec:appendix-ir}).",
          "+where $\\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\\beta \\in [0, 2]$ yields marginal improvement, then $\\beta = 3$ triggers a phase transition to GAR\\,=\\,0.556 (9\\% PPL cost). At $\\beta$\\,=\\,5, GAR reaches 0.727$\\pm$0.061 (PPL 1.77); the operating region $\\beta \\in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering}; per-$\\beta$ turn-level trajectories in Appendix~\\ref{sec:appendix-steering-viz}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does---consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\\ref{sec:appendix-examples}). Downstream, steering ($\\beta$\\,=\\,3) raises late-turn instruction compliance by +11.1\\,pp, though this effect does not reach conventional significance ($p$\\,=\\,0.077; content-constrained tasks benefit most, +23.8\\,pp; Appendix~\\ref{sec:appendix-ir}).",
          " ",
          " \\subsection{Scheduled Sampling Compresses the TF--AR Gap}\\label{subsec:ss}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "295b5a6f-6162-41e1-810e-5dddc26cf4b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1154_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 附录内容引用完整性检查  **任务：** 检查论文附录的所有内容是否在正文中都有准确、合理的引用，修复孤儿附录。  **Step 1：逐项盘点** 列出附录里每一个 section/subsection/table/figure/algorithm/proof/prompt。  **Step 2：逐项验证引用** 对每一项，在正文搜索是否有至少一句话指向…",
  "leafUuid": "8f593965-1cf1-463b-b282-1fac214f414a",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1155_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Tool call

_source line 1156 · 2026-05-25T09:12:10.124Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01Vz4aYvHnw8UwhPMGk3WTg6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
  "old_string": "Appendix~\\ref{sec:appendix-gar-robust})",
  "new_string": "Appendix~\\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\\ref{sec:appendix-gar-ext})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f593965-1cf1-463b-b282-1fac214f414a",
  "isSidechain": false,
  "requestId": "req_011CbP2duussjKqqsdW9oTxH",
  "type": "assistant",
  "uuid": "95dadfd2-a30d-4781-bb13-1d36401eb91e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016e1CuPrtRE3jCp7pLcTu1S",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 66595,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 286,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 66595,
          "cache_creation_input_tokens": 286,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 286
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

_source line 1157 · 2026-05-25T09:12:10.141Z_

<details><summary>↩ Tool result · `toolu_01Vz4aYvHnw8UwhPMGk3WTg6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "95dadfd2-a30d-4781-bb13-1d36401eb91e",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "fc7f1dd1-dbdb-407b-a387-06a02e33a37d",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex",
    "oldString": "Appendix~\\ref{sec:appendix-gar-robust})",
    "newString": "Appendix~\\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\\ref{sec:appendix-gar-ext})",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\nWe fine-tune Qwen-2.5-7B-Instruct with LoRA \\citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \\citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \\times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\\,GB; training costs in Appendix~\\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\\ref{sec:appendix-hyper}; dataset statistics in Appendices~\\ref{sec:appendix-data} and~\\ref{sec:appendix-dataset-ext}; the controlled comparison design is described in \\S\\ref{sec:comparison-design}. We evaluate under \\emph{IID} (same-distribution UltraChat text) and \\emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \\citep{dongre2026attention}, and perplexity (PPL).\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\\leq$2\\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\\leq$1\\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, confirming that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\\S\\ref{subsec:ss}).\n\nUnder AR generation ($N$\\,=\\,50), GAR-ours drops to 0.019--0.064, an 8--17$\\times$ gap (Figure~\\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\\ LoRA-only is significant ($p$\\,=\\,0.004; Appendices~\\ref{sec:appendix-stats} and~\\ref{sec:appendix-stats-ext}), yet the gap remains 7.8$\\times$. A second seed confirms TF stability ($0.504\\pm0.001$). MMLU 5-shot accuracy remains within 0.8\\,pp across all variants (per-category breakdown in Appendix~\\ref{sec:appendix-mmlu-ext}). We analyze this distribution shift in \\S\\ref{sec:analysis}.\n\n\\subsection{Inference-Time Attention Steering}\\label{subsec:steering}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig5_attention_steering.pdf}\n  \\caption{Inference-time $\\beta$-steering recovers GAR from 0.064 to 0.727, confirming attention misallocation as a proximal cause (9\\% PPL cost at $\\beta$\\,=\\,3; phase transition at $\\beta \\in [2, 3]$).}\n  \\label{fig:steering-recovery}\n\\end{figure}\n\nAll training-time interventions leave the exposure bias gap intact. If the collapse is caused by attention misallocation rather than representation degradation, then directly correcting attention should recover GAR. We test this by adding a constant bias $\\beta$ to pre-softmax attention logits for goal-token positions during generation:\n\\begin{equation}\n  \\tilde{A}_{i,j}^{(\\ell,h)} = A_{i,j}^{(\\ell,h)} + \\beta \\cdot \\mathbf{1}[j \\in \\mathcal{G}],\n\\end{equation}\nwhere $\\tilde{A}$ denotes the modified logits before softmax. The additive form operates in log-probability space, providing uniform boost even when baseline attention is near zero. The response is sharply nonlinear: $\\beta \\in [0, 2]$ yields marginal improvement, then $\\beta = 3$ triggers a phase transition to GAR\\,=\\,0.556 (9\\% PPL cost). At $\\beta$\\,=\\,5, GAR reaches 0.727$\\pm$0.061 (PPL 1.77); the operating region $\\beta \\in [3, 5]$ exceeds the TF baseline while PPL remains below 1.8 (Figure~\\ref{fig:steering-recovery}; full results in Appendix~\\ref{sec:appendix-steering}; per-$\\beta$ turn-level trajectories in Appendix~\\ref{sec:appendix-steering-viz}). GAR recovery under steering is partly by construction: boosting attention logits toward goal tokens mechanically increases the attention-based metric. The stronger evidence is the counterfactual: if the collapse were due to hidden-state drift rather than attention misallocation, reweighting could not recover GAR, yet it does---consistent with attention misallocation as a proximal cause (qualitative examples in Appendix~\\ref{sec:appendix-examples}). Downstream, steering ($\\beta$\\,=\\,3) raises late-turn instruction compliance by +11.1\\,pp, though this effect does not reach conventional significance ($p$\\,=\\,0.077; content-constrained tasks benefit most, +23.8\\,pp; Appendix~\\ref{sec:appendix-ir}).\n\n\\subsection{Scheduled Sampling Compresses the TF--AR Gap}\\label{subsec:ss}\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_gap_compression.pdf}\n  \\caption{Scheduled sampling compresses the TF-AR gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$, the only variant approaching parity across five training conditions.}\n  \\label{fig:ss-gap}\n\\end{figure}\n\nScheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.001$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 35,
        "oldLines": 6,
        "newStart": 35,
        "newLines": 6,
        "lines": [
          "   \\label{fig:ss-gap}",
          " \\end{figure}",
          " ",
          "-Scheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.001$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.",
          "+Scheduled sampling (SS; \\citealp{bengio2015scheduled}), which mixes model-generated tokens into training prefixes with linearly increasing probability (Appendix~\\ref{sec:appendix-ss}), directly targets the training-inference mismatch. Across three seeds, AR GAR-ours rises to $0.401\\pm0.047$, compressing the gap from 7.8$\\times$ to ${\\sim}$1.3$\\times$ (TF GAR $0.498\\pm0.004$) with no PPL cost ($1.441\\pm0.001$; Figure~\\ref{fig:ss-gap}; per-seed details in Appendix~\\ref{sec:appendix-perseed}). Steering on SS models nearly eliminates seed variance ($\\beta$\\,=\\,5: $0.717\\pm0.001$, std 0.047$\\to$0.001; Figure~\\ref{fig:ss-multiseed}). SS generalizes across GAR definitions (mid-turn GAR above 0.36 for all token-position variants; Appendix~\\ref{sec:appendix-gar-robust}; extended robustness in Appendix~\\ref{sec:appendix-gar-ext}) and across architectures: on Llama-3.1-8B, SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$, weaker than Qwen likely due to fewer training epochs (2 vs.\\ 3; \\S\\ref{subsec:cross-model}). The benefit diminishes in longer dialogues (Appendix~\\ref{sec:appendix-n5}), consistent with exposure bias compounding over turns.",
          " ",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "95dadfd2-a30d-4781-bb13-1d36401eb91e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Assistant

_source line 1158 · 2026-05-25T09:12:12.514Z_

Now the analysis.tex edits:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc7f1dd1-dbdb-407b-a387-06a02e33a37d",
  "isSidechain": false,
  "requestId": "req_011CbP2eBPJYXnsXsYyfrtxR",
  "type": "assistant",
  "uuid": "a6bb5786-4901-47e1-8b0e-f2496b0f539b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011qxvz33NJYZzkrUwakXnNg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 66881,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 256,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 66881,
          "cache_creation_input_tokens": 256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 256
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

_source line 1159 · 2026-05-25T09:12:13.944Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01QamBYdwHvz5HKUhaSNbeuw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
  "old_string": "full gate profiles in Appendix~\\ref{sec:appendix-gate-profile})",
  "new_string": "full gate profiles in Appendix~\\ref{sec:appendix-gate-profile}; training dynamics in Appendix~\\ref{sec:appendix-training-ext})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6bb5786-4901-47e1-8b0e-f2496b0f539b",
  "isSidechain": false,
  "requestId": "req_011CbP2eBPJYXnsXsYyfrtxR",
  "type": "assistant",
  "uuid": "f465b1d9-5aed-40d8-add2-ed6e4a5367c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011qxvz33NJYZzkrUwakXnNg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 66881,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 256,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 66881,
          "cache_creation_input_tokens": 256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 256
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

_source line 1160 · 2026-05-25T09:12:13.952Z_

<details><summary>↩ Tool result · `toolu_01QamBYdwHvz5HKUhaSNbeuw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f465b1d9-5aed-40d8-add2-ed6e4a5367c9",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "66225ce2-bafb-40ca-a2e3-385838f4d935",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
    "oldString": "full gate profiles in Appendix~\\ref{sec:appendix-gate-profile})",
    "newString": "full gate profiles in Appendix~\\ref{sec:appendix-gate-profile}; training dynamics in Appendix~\\ref{sec:appendix-training-ext})",
    "originalFile": "\\section{Analysis}\\label{sec:analysis}\n\nEach subsection kills one alternative hypothesis via causal exclusion: \\S\\ref{subsec:gate-conditioning}~turn conditioning, \\S\\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\\S\\ref{subsec:dist-shift}). \\S\\ref{subsec:mechanism-specificity} confirms selectivity; \\S\\ref{subsec:cross-model} confirms cross-architecture generalization.\n\n\\subsection{Gate Turn Conditioning}\\label{subsec:gate-conditioning}\n\nWe compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \\emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \\times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \\citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\\% attenuation; Table~\\ref{tab:four-way}; full gate profiles in Appendix~\\ref{sec:appendix-gate-profile}). The Uniform Gate learns comparable per-layer variation (L3\\,=\\,0.777, L27\\,=\\,1.000) despite lacking turn conditioning, confirming the structure arises from LoRA$+$GAR pressure (Figure~\\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?\n\n\\subsection{PCGrad Gradient Direction Conflict Exclusion}\\label{subsec:pcgrad}\n\nNTP and GAR gradients oppose in 68--79\\% of layers (cosine similarity $-$0.089$\\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\\times$ to 14.7$\\times$ (full gradient statistics in Appendix~\\ref{sec:appendix-gradient}). If this direction conflict prevents GAR convergence, eliminating it via PCGrad \\citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \\emph{diagnostic} tool rather than an optimization method.\n\nPCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \\emph{worsens}: 0.064$\\to$0.030 ($p$\\,=\\,0.002; Figure~\\ref{fig:training-pcgrad}b in Appendix~\\ref{sec:appendix-gradient}). By \\emph{modus tollens}: removing gradient direction conflict does not prevent collapse; therefore it is not the primary cause. PCGrad eliminates direction conflict but does not address magnitude imbalance (NTP dominates GAR by 7.5--14.7$\\times$); the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\\,=\\,+0.005) with 25.7$\\times$ NTP magnitude dominance (Table~\\ref{tab:gradient-crossmodel}).\n\n\\subsection{Distribution Shift Analysis}\\label{subsec:dist-shift}\n\nThe TF-AR GAR gap persists across all variants (Table~\\ref{tab:four-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, confirming that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \\citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\\tau$\\,=\\,0.5 while AR GAR collapses (77--87\\% per-turn decay; Figure~\\ref{fig:attention-heatmap}; scaling analysis in Appendix~\\ref{sec:appendix-eb-scaling}).\n\n\\subsection{Mechanism Specificity}\\label{subsec:mechanism-specificity}\n\nWe test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\\times$) and Qwen (1.28$\\times$) vs.\\ the order-of-magnitude GAR-ours collapse.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_multiseed.pdf}\n  \\caption{Multi-seed AR GAR under scheduled sampling ($\\beta$\\,=\\,0 and $\\beta$\\,=\\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\\to$0.001).}\n  \\label{fig:ss-multiseed}\n\\end{figure}\n\n\\subsection{Cross-Model Replication}\\label{subsec:cross-model}\n\nWe replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\\,$>$\\,100\\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}). Gate profiles differ qualitatively (Figure~\\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\\,=\\,0.793) while Llama dips at late layers (L25\\,=\\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.\n\nScheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\\sim}$1.3$\\times$ likely due to fewer training epochs (2 vs.\\ 3). The phase transition is architecture-dependent: $\\beta$\\,=\\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\\beta$\\,=\\,5 (GAR 0.791, exceeding Qwen SS 0.717), suggesting deeper architectures need higher steering thresholds but ultimately provide more surface for attention reweighting (full results in Appendix~\\ref{sec:appendix-llama}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern: 79.8\\% GAR decay and $\\beta$-steering recovery to 0.715 (Appendix~\\ref{sec:appendix-1.5b}).\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig3_gate_shift.pdf}\n  \\caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \\times 10^{-8}$). (b)~Distribution shift ($N$\\,=\\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\\times$) exceed final $N$\\,=\\,50 estimates (8--17$\\times$; Table~\\ref{tab:four-way}) due to smaller sample size.}\n  \\label{fig:gate-shift}\n\\end{figure}",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 7,
        "newStart": 4,
        "newLines": 7,
        "lines": [
          " ",
          " \\subsection{Gate Turn Conditioning}\\label{subsec:gate-conditioning}",
          " ",
          "-We compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \\emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \\times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \\citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\\% attenuation; Table~\\ref{tab:four-way}; full gate profiles in Appendix~\\ref{sec:appendix-gate-profile}). The Uniform Gate learns comparable per-layer variation (L3\\,=\\,0.777, L27\\,=\\,1.000) despite lacking turn conditioning, confirming the structure arises from LoRA$+$GAR pressure (Figure~\\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?",
          "+We compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \\emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \\times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \\citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\\% attenuation; Table~\\ref{tab:four-way}; full gate profiles in Appendix~\\ref{sec:appendix-gate-profile}; training dynamics in Appendix~\\ref{sec:appendix-training-ext}). The Uniform Gate learns comparable per-layer variation (L3\\,=\\,0.777, L27\\,=\\,1.000) despite lacking turn conditioning, confirming the structure arises from LoRA$+$GAR pressure (Figure~\\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?",
          " ",
          " \\subsection{PCGrad Gradient Direction Conflict Exclusion}\\label{subsec:pcgrad}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "f465b1d9-5aed-40d8-add2-ed6e4a5367c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool call

_source line 1161 · 2026-05-25T09:12:17.629Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01FWPSTsKfi16Bw7vKScFQKy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
  "old_string": "Figure~\\ref{fig:attention-heatmap}; scaling analysis in Appendix~\\ref{sec:appendix-eb-scaling})",
  "new_string": "Figure~\\ref{fig:attention-heatmap}; per-configuration AR trajectories in Appendix~\\ref{sec:appendix-ar-gar-dynamics}; scaling analysis in Appendix~\\ref{sec:appendix-eb-scaling})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66225ce2-bafb-40ca-a2e3-385838f4d935",
  "isSidechain": false,
  "requestId": "req_011CbP2eTdrbMAkhq3XMzS58",
  "type": "assistant",
  "uuid": "87ba9c70-f859-4f21-9e69-4a380fc8e2c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N5vcgbSYc4bafQLU8mPV6c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 268,
      "cache_read_input_tokens": 67137,
      "output_tokens": 237,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 268,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 237,
          "cache_read_input_tokens": 67137,
          "cache_creation_input_tokens": 268,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 268
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

_source line 1162 · 2026-05-25T09:12:17.644Z_

<details><summary>↩ Tool result · `toolu_01FWPSTsKfi16Bw7vKScFQKy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87ba9c70-f859-4f21-9e69-4a380fc8e2c6",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "2fbdf733-fc53-4489-b5b8-8e87fad41563",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
    "oldString": "Figure~\\ref{fig:attention-heatmap}; scaling analysis in Appendix~\\ref{sec:appendix-eb-scaling})",
    "newString": "Figure~\\ref{fig:attention-heatmap}; per-configuration AR trajectories in Appendix~\\ref{sec:appendix-ar-gar-dynamics}; scaling analysis in Appendix~\\ref{sec:appendix-eb-scaling})",
    "originalFile": "\\section{Analysis}\\label{sec:analysis}\n\nEach subsection kills one alternative hypothesis via causal exclusion: \\S\\ref{subsec:gate-conditioning}~turn conditioning, \\S\\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\\S\\ref{subsec:dist-shift}). \\S\\ref{subsec:mechanism-specificity} confirms selectivity; \\S\\ref{subsec:cross-model} confirms cross-architecture generalization.\n\n\\subsection{Gate Turn Conditioning}\\label{subsec:gate-conditioning}\n\nWe compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \\emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \\times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \\citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\\% attenuation; Table~\\ref{tab:four-way}; full gate profiles in Appendix~\\ref{sec:appendix-gate-profile}; training dynamics in Appendix~\\ref{sec:appendix-training-ext}). The Uniform Gate learns comparable per-layer variation (L3\\,=\\,0.777, L27\\,=\\,1.000) despite lacking turn conditioning, confirming the structure arises from LoRA$+$GAR pressure (Figure~\\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?\n\n\\subsection{PCGrad Gradient Direction Conflict Exclusion}\\label{subsec:pcgrad}\n\nNTP and GAR gradients oppose in 68--79\\% of layers (cosine similarity $-$0.089$\\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\\times$ to 14.7$\\times$ (full gradient statistics in Appendix~\\ref{sec:appendix-gradient}). If this direction conflict prevents GAR convergence, eliminating it via PCGrad \\citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \\emph{diagnostic} tool rather than an optimization method.\n\nPCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \\emph{worsens}: 0.064$\\to$0.030 ($p$\\,=\\,0.002; Figure~\\ref{fig:training-pcgrad}b in Appendix~\\ref{sec:appendix-gradient}). By \\emph{modus tollens}: removing gradient direction conflict does not prevent collapse; therefore it is not the primary cause. PCGrad eliminates direction conflict but does not address magnitude imbalance (NTP dominates GAR by 7.5--14.7$\\times$); the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\\,=\\,+0.005) with 25.7$\\times$ NTP magnitude dominance (Table~\\ref{tab:gradient-crossmodel}).\n\n\\subsection{Distribution Shift Analysis}\\label{subsec:dist-shift}\n\nThe TF-AR GAR gap persists across all variants (Table~\\ref{tab:four-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, confirming that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \\citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\\tau$\\,=\\,0.5 while AR GAR collapses (77--87\\% per-turn decay; Figure~\\ref{fig:attention-heatmap}; scaling analysis in Appendix~\\ref{sec:appendix-eb-scaling}).\n\n\\subsection{Mechanism Specificity}\\label{subsec:mechanism-specificity}\n\nWe test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\\times$) and Qwen (1.28$\\times$) vs.\\ the order-of-magnitude GAR-ours collapse.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_multiseed.pdf}\n  \\caption{Multi-seed AR GAR under scheduled sampling ($\\beta$\\,=\\,0 and $\\beta$\\,=\\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\\to$0.001).}\n  \\label{fig:ss-multiseed}\n\\end{figure}\n\n\\subsection{Cross-Model Replication}\\label{subsec:cross-model}\n\nWe replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\\,$>$\\,100\\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}). Gate profiles differ qualitatively (Figure~\\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\\,=\\,0.793) while Llama dips at late layers (L25\\,=\\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.\n\nScheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\\sim}$1.3$\\times$ likely due to fewer training epochs (2 vs.\\ 3). The phase transition is architecture-dependent: $\\beta$\\,=\\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\\beta$\\,=\\,5 (GAR 0.791, exceeding Qwen SS 0.717), suggesting deeper architectures need higher steering thresholds but ultimately provide more surface for attention reweighting (full results in Appendix~\\ref{sec:appendix-llama}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern: 79.8\\% GAR decay and $\\beta$-steering recovery to 0.715 (Appendix~\\ref{sec:appendix-1.5b}).\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig3_gate_shift.pdf}\n  \\caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \\times 10^{-8}$). (b)~Distribution shift ($N$\\,=\\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\\times$) exceed final $N$\\,=\\,50 estimates (8--17$\\times$; Table~\\ref{tab:four-way}) due to smaller sample size.}\n  \\label{fig:gate-shift}\n\\end{figure}",
    "structuredPatch": [
      {
        "oldStart": 14,
        "oldLines": 7,
        "newStart": 14,
        "newLines": 7,
        "lines": [
          " ",
          " \\subsection{Distribution Shift Analysis}\\label{subsec:dist-shift}",
          " ",
          "-The TF-AR GAR gap persists across all variants (Table~\\ref{tab:four-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, confirming that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \\citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\\tau$\\,=\\,0.5 while AR GAR collapses (77--87\\% per-turn decay; Figure~\\ref{fig:attention-heatmap}; scaling analysis in Appendix~\\ref{sec:appendix-eb-scaling}).",
          "+The TF-AR GAR gap persists across all variants (Table~\\ref{tab:four-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, confirming that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \\citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\\tau$\\,=\\,0.5 while AR GAR collapses (77--87\\% per-turn decay; Figure~\\ref{fig:attention-heatmap}; per-configuration AR trajectories in Appendix~\\ref{sec:appendix-ar-gar-dynamics}; scaling analysis in Appendix~\\ref{sec:appendix-eb-scaling}).",
          " ",
          " \\subsection{Mechanism Specificity}\\label{subsec:mechanism-specificity}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "87ba9c70-f859-4f21-9e69-4a380fc8e2c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1163_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Patch] 附录内容引用完整性检查  **任务：** 检查论文附录的所有内容是否在正文中都有准确、合理的引用，修复孤儿附录。  **Step 1：逐项盘点** 列出附录里每一个 section/subsection/table/figure/algorithm/proof/prompt。  **Step 2：逐项验证引用** 对每一项，在正文搜索是否有至少一句话指向…",
  "leafUuid": "2fbdf733-fc53-4489-b5b8-8e87fad41563",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Runtime record

_source line 1164_

```json
{
  "type": "ai-title",
  "aiTitle": "Call main_agent_post_to_director to report results",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58"
}
```

---


### Tool call

_source line 1165 · 2026-05-25T09:12:21.781Z_

<details open><summary>🔧 Tool call — Edit · `toolu_016Mm9piFmy8uQZTPMqG5GFV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
  "old_string": "gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama})",
  "new_string": "gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}; per-turn values in Appendix~\\ref{sec:appendix-perturn-detail})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fbdf733-fc53-4489-b5b8-8e87fad41563",
  "isSidechain": false,
  "requestId": "req_011CbP2ejTri3NZ6fvyAqtct",
  "type": "assistant",
  "uuid": "ce1611c2-0e6f-4a5e-8619-b8130548c496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4UL4NmDU2hDefGbeQsfPu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 292,
      "cache_read_input_tokens": 67405,
      "output_tokens": 253,
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
          "output_tokens": 253,
          "cache_read_input_tokens": 67405,
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

_source line 1166 · 2026-05-25T09:12:21.799Z_

<details><summary>↩ Tool result · `toolu_016Mm9piFmy8uQZTPMqG5GFV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce1611c2-0e6f-4a5e-8619-b8130548c496",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "23ef06ff-7c35-4fa9-82c1-0b82d98401db",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
    "oldString": "gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama})",
    "newString": "gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}; per-turn values in Appendix~\\ref{sec:appendix-perturn-detail})",
    "originalFile": "\\section{Analysis}\\label{sec:analysis}\n\nEach subsection kills one alternative hypothesis via causal exclusion: \\S\\ref{subsec:gate-conditioning}~turn conditioning, \\S\\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\\S\\ref{subsec:dist-shift}). \\S\\ref{subsec:mechanism-specificity} confirms selectivity; \\S\\ref{subsec:cross-model} confirms cross-architecture generalization.\n\n\\subsection{Gate Turn Conditioning}\\label{subsec:gate-conditioning}\n\nWe compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \\emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \\times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \\citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\\% attenuation; Table~\\ref{tab:four-way}; full gate profiles in Appendix~\\ref{sec:appendix-gate-profile}; training dynamics in Appendix~\\ref{sec:appendix-training-ext}). The Uniform Gate learns comparable per-layer variation (L3\\,=\\,0.777, L27\\,=\\,1.000) despite lacking turn conditioning, confirming the structure arises from LoRA$+$GAR pressure (Figure~\\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?\n\n\\subsection{PCGrad Gradient Direction Conflict Exclusion}\\label{subsec:pcgrad}\n\nNTP and GAR gradients oppose in 68--79\\% of layers (cosine similarity $-$0.089$\\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\\times$ to 14.7$\\times$ (full gradient statistics in Appendix~\\ref{sec:appendix-gradient}). If this direction conflict prevents GAR convergence, eliminating it via PCGrad \\citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \\emph{diagnostic} tool rather than an optimization method.\n\nPCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \\emph{worsens}: 0.064$\\to$0.030 ($p$\\,=\\,0.002; Figure~\\ref{fig:training-pcgrad}b in Appendix~\\ref{sec:appendix-gradient}). By \\emph{modus tollens}: removing gradient direction conflict does not prevent collapse; therefore it is not the primary cause. PCGrad eliminates direction conflict but does not address magnitude imbalance (NTP dominates GAR by 7.5--14.7$\\times$); the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\\,=\\,+0.005) with 25.7$\\times$ NTP magnitude dominance (Table~\\ref{tab:gradient-crossmodel}).\n\n\\subsection{Distribution Shift Analysis}\\label{subsec:dist-shift}\n\nThe TF-AR GAR gap persists across all variants (Table~\\ref{tab:four-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, confirming that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \\citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\\tau$\\,=\\,0.5 while AR GAR collapses (77--87\\% per-turn decay; Figure~\\ref{fig:attention-heatmap}; per-configuration AR trajectories in Appendix~\\ref{sec:appendix-ar-gar-dynamics}; scaling analysis in Appendix~\\ref{sec:appendix-eb-scaling}).\n\n\\subsection{Mechanism Specificity}\\label{subsec:mechanism-specificity}\n\nWe test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\\times$) and Qwen (1.28$\\times$) vs.\\ the order-of-magnitude GAR-ours collapse.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_multiseed.pdf}\n  \\caption{Multi-seed AR GAR under scheduled sampling ($\\beta$\\,=\\,0 and $\\beta$\\,=\\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\\to$0.001).}\n  \\label{fig:ss-multiseed}\n\\end{figure}\n\n\\subsection{Cross-Model Replication}\\label{subsec:cross-model}\n\nWe replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\\,$>$\\,100\\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}). Gate profiles differ qualitatively (Figure~\\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\\,=\\,0.793) while Llama dips at late layers (L25\\,=\\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.\n\nScheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\\sim}$1.3$\\times$ likely due to fewer training epochs (2 vs.\\ 3). The phase transition is architecture-dependent: $\\beta$\\,=\\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\\beta$\\,=\\,5 (GAR 0.791, exceeding Qwen SS 0.717), suggesting deeper architectures need higher steering thresholds but ultimately provide more surface for attention reweighting (full results in Appendix~\\ref{sec:appendix-llama}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern: 79.8\\% GAR decay and $\\beta$-steering recovery to 0.715 (Appendix~\\ref{sec:appendix-1.5b}).\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig3_gate_shift.pdf}\n  \\caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \\times 10^{-8}$). (b)~Distribution shift ($N$\\,=\\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\\times$) exceed final $N$\\,=\\,50 estimates (8--17$\\times$; Table~\\ref{tab:four-way}) due to smaller sample size.}\n  \\label{fig:gate-shift}\n\\end{figure}",
    "structuredPatch": [
      {
        "oldStart": 29,
        "oldLines": 7,
        "newStart": 29,
        "newLines": 7,
        "lines": [
          " ",
          " \\subsection{Cross-Model Replication}\\label{subsec:cross-model}",
          " ",
          "-We replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\\,$>$\\,100\\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}). Gate profiles differ qualitatively (Figure~\\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\\,=\\,0.793) while Llama dips at late layers (L25\\,=\\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.",
          "+We replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\\,$>$\\,100\\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}; per-turn values in Appendix~\\ref{sec:appendix-perturn-detail}). Gate profiles differ qualitatively (Figure~\\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\\,=\\,0.793) while Llama dips at late layers (L25\\,=\\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.",
          " ",
          " Scheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\\sim}$1.3$\\times$ likely due to fewer training epochs (2 vs.\\ 3). The phase transition is architecture-dependent: $\\beta$\\,=\\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\\beta$\\,=\\,5 (GAR 0.791, exceeding Qwen SS 0.717), suggesting deeper architectures need higher steering thresholds but ultimately provide more surface for attention reweighting (full results in Appendix~\\ref{sec:appendix-llama}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern: 79.8\\% GAR decay and $\\beta$-steering recovery to 0.715 (Appendix~\\ref{sec:appendix-1.5b}).",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "ce1611c2-0e6f-4a5e-8619-b8130548c496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Runtime record

_source line 1167 · 2026-05-25T09:12:21.839Z_

```json
{
  "parentUuid": "23ef06ff-7c35-4fa9-82c1-0b82d98401db",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "a828cb00-4cb1-4407-aa5a-0951ce451d9e",
  "timestamp": "2026-05-25T09:12:21.839Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---


### Tool call

_source line 1168 · 2026-05-25T09:12:25.169Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01VJVFMYwMt9nnuD8Lb1hjCt`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
  "old_string": "(Appendix~\\ref{sec:appendix-1.5b})",
  "new_string": "(Appendix~\\ref{sec:appendix-1.5b}; extended diagnostics in Appendix~\\ref{sec:appendix-1.5b-ext})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a828cb00-4cb1-4407-aa5a-0951ce451d9e",
  "isSidechain": false,
  "requestId": "req_011CbP2f3EC7mYEbfokkoZ1C",
  "type": "assistant",
  "uuid": "faa1bad1-21e4-4cc8-8a16-d9026418a0a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdfEMguEX6ApryF8csBbs7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 412,
      "cache_read_input_tokens": 67697,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 412,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 67697,
          "cache_creation_input_tokens": 412,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 412
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

_source line 1169 · 2026-05-25T09:12:25.179Z_

<details><summary>↩ Tool result · `toolu_01VJVFMYwMt9nnuD8Lb1hjCt`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "faa1bad1-21e4-4cc8-8a16-d9026418a0a0",
  "isSidechain": false,
  "promptId": "1ce268e5-cb8f-414e-8f6b-2c826bf58c75",
  "type": "user",
  "uuid": "ddc65459-b82f-4ebe-811e-8bbd19319e93",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
    "oldString": "(Appendix~\\ref{sec:appendix-1.5b})",
    "newString": "(Appendix~\\ref{sec:appendix-1.5b}; extended diagnostics in Appendix~\\ref{sec:appendix-1.5b-ext})",
    "originalFile": "\\section{Analysis}\\label{sec:analysis}\n\nEach subsection kills one alternative hypothesis via causal exclusion: \\S\\ref{subsec:gate-conditioning}~turn conditioning, \\S\\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\\S\\ref{subsec:dist-shift}). \\S\\ref{subsec:mechanism-specificity} confirms selectivity; \\S\\ref{subsec:cross-model} confirms cross-architecture generalization.\n\n\\subsection{Gate Turn Conditioning}\\label{subsec:gate-conditioning}\n\nWe compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \\emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \\times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \\citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\\% attenuation; Table~\\ref{tab:four-way}; full gate profiles in Appendix~\\ref{sec:appendix-gate-profile}; training dynamics in Appendix~\\ref{sec:appendix-training-ext}). The Uniform Gate learns comparable per-layer variation (L3\\,=\\,0.777, L27\\,=\\,1.000) despite lacking turn conditioning, confirming the structure arises from LoRA$+$GAR pressure (Figure~\\ref{fig:gate-shift}a). Does the NTP-GAR gradient conflict prevent the intended behavior?\n\n\\subsection{PCGrad Gradient Direction Conflict Exclusion}\\label{subsec:pcgrad}\n\nNTP and GAR gradients oppose in 68--79\\% of layers (cosine similarity $-$0.089$\\to$$-$0.042 across epochs), with NTP magnitude dominance growing from 7.5$\\times$ to 14.7$\\times$ (full gradient statistics in Appendix~\\ref{sec:appendix-gradient}). If this direction conflict prevents GAR convergence, eliminating it via PCGrad \\citep{yu2020pcgrad}, which projects conflicting gradients onto the other's normal plane, should prevent the collapse. To our knowledge, this is the first application of PCGrad as a \\emph{diagnostic} tool rather than an optimization method.\n\nPCGrad shifts cosine similarity to oscillate around zero, yet TF metrics are unchanged. AR GAR \\emph{worsens}: 0.064$\\to$0.030 ($p$\\,=\\,0.002; Figure~\\ref{fig:training-pcgrad}b in Appendix~\\ref{sec:appendix-gradient}). By \\emph{modus tollens}: removing gradient direction conflict does not prevent collapse; therefore it is not the primary cause. PCGrad eliminates direction conflict but does not address magnitude imbalance (NTP dominates GAR by 7.5--14.7$\\times$); the worsening under PCGrad may partly reflect projection side-effects rather than confirming that direction conflict is entirely absent as a factor. Cross-model analysis confirms this pattern: Llama-3.1-8B gradients are near-orthogonal (cos\\,=\\,+0.005) with 25.7$\\times$ NTP magnitude dominance (Table~\\ref{tab:gradient-crossmodel}).\n\n\\subsection{Distribution Shift Analysis}\\label{subsec:dist-shift}\n\nThe TF-AR GAR gap persists across all variants (Table~\\ref{tab:four-way}). GAR-Dongre provides a control: it remains uniformly low (0.01--0.02) with no distribution gap, confirming that the shift selectively destroys concentrated last-token attention. The mechanism is exposure bias \\citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}: during training the model conditions on ground-truth prefixes; at inference, on its own outputs. GAR optimizes a distributional property with no autoregressive counterpart, explaining why TF GAR-ours remains near $\\tau$\\,=\\,0.5 while AR GAR collapses (77--87\\% per-turn decay; Figure~\\ref{fig:attention-heatmap}; per-configuration AR trajectories in Appendix~\\ref{sec:appendix-ar-gar-dynamics}; scaling analysis in Appendix~\\ref{sec:appendix-eb-scaling}).\n\n\\subsection{Mechanism Specificity}\\label{subsec:mechanism-specificity}\n\nWe test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\\times$) and Qwen (1.28$\\times$) vs.\\ the order-of-magnitude GAR-ours collapse.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig_ss_multiseed.pdf}\n  \\caption{Multi-seed AR GAR under scheduled sampling ($\\beta$\\,=\\,0 and $\\beta$\\,=\\,5, three seeds). Steering nearly eliminates seed variance (std: 0.047$\\to$0.001).}\n  \\label{fig:ss-multiseed}\n\\end{figure}\n\n\\subsection{Cross-Model Replication}\\label{subsec:cross-model}\n\nWe replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\\,$>$\\,100\\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}; per-turn values in Appendix~\\ref{sec:appendix-perturn-detail}). Gate profiles differ qualitatively (Figure~\\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\\,=\\,0.793) while Llama dips at late layers (L25\\,=\\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.\n\nScheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\\sim}$1.3$\\times$ likely due to fewer training epochs (2 vs.\\ 3). The phase transition is architecture-dependent: $\\beta$\\,=\\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\\beta$\\,=\\,5 (GAR 0.791, exceeding Qwen SS 0.717), suggesting deeper architectures need higher steering thresholds but ultimately provide more surface for attention reweighting (full results in Appendix~\\ref{sec:appendix-llama}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern: 79.8\\% GAR decay and $\\beta$-steering recovery to 0.715 (Appendix~\\ref{sec:appendix-1.5b}).\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig3_gate_shift.pdf}\n  \\caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \\times 10^{-8}$). (b)~Distribution shift ($N$\\,=\\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\\times$) exceed final $N$\\,=\\,50 estimates (8--17$\\times$; Table~\\ref{tab:four-way}) due to smaller sample size.}\n  \\label{fig:gate-shift}\n\\end{figure}",
    "structuredPatch": [
      {
        "oldStart": 31,
        "oldLines": 7,
        "newStart": 31,
        "newLines": 7,
        "lines": [
          " ",
          " We replicate on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3} (Base, ThreadGate, LoRA-only; $N$\\,=\\,20, 4 turns). TF GAR-ours is 0.484 (TG) / 0.481 (LoRA-only); gating contributes zero benefit. The AR distribution is heavy-tailed (coefficient of variation, CoV\\,$>$\\,100\\%); we report medians: 0.018 (TG and LoRA-only), 0.009 (Base), yielding gaps of 27$\\times$ and 26$\\times$ (Figure~\\ref{fig:crossmodel}a in Appendix~\\ref{sec:appendix-llama}; per-turn values in Appendix~\\ref{sec:appendix-perturn-detail}). Gate profiles differ qualitatively (Figure~\\ref{fig:crossmodel}b): Qwen attenuates early layers (L1\\,=\\,0.793) while Llama dips at late layers (L25\\,=\\,0.719), an architecture-dependent pattern, but convergence toward identity is universal (Appendix~\\ref{sec:appendix-viz}). The gap is substantial on both architectures, consistent with exposure bias as architecture-independent.",
          " ",
          "-Scheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\\sim}$1.3$\\times$ likely due to fewer training epochs (2 vs.\\ 3). The phase transition is architecture-dependent: $\\beta$\\,=\\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\\beta$\\,=\\,5 (GAR 0.791, exceeding Qwen SS 0.717), suggesting deeper architectures need higher steering thresholds but ultimately provide more surface for attention reweighting (full results in Appendix~\\ref{sec:appendix-llama}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern: 79.8\\% GAR decay and $\\beta$-steering recovery to 0.715 (Appendix~\\ref{sec:appendix-1.5b}).",
          "+Scheduled sampling confirms cross-model generalization: Llama SS compresses the gap from ${\\sim}$27$\\times$ to 2.9$\\times$ (TF GAR 0.477, AR GAR 0.166), weaker than Qwen's ${\\sim}$1.3$\\times$ likely due to fewer training epochs (2 vs.\\ 3). The phase transition is architecture-dependent: $\\beta$\\,=\\,3 triggers recovery on Qwen SS (0.593) but not Llama SS (0.173); Llama requires $\\beta$\\,=\\,5 (GAR 0.791, exceeding Qwen SS 0.717), suggesting deeper architectures need higher steering thresholds but ultimately provide more surface for attention reweighting (full results in Appendix~\\ref{sec:appendix-llama}). Cross-scale validation on Qwen-2.5-1.5B confirms the same pattern: 79.8\\% GAR decay and $\\beta$-steering recovery to 0.715 (Appendix~\\ref{sec:appendix-1.5b}; extended diagnostics in Appendix~\\ref{sec:appendix-1.5b-ext}).",
          " ",
          " \\begin{figure}[t]",
          "   \\centering"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "faa1bad1-21e4-4cc8-8a16-d9026418a0a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---


### Tool call

_source line 1170 · 2026-05-25T09:12:28.481Z_

<details open><summary>🔧 Tool call — Edit · `toolu_017s89cFXHAxtxXDW2FhD8Ds`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
  "old_string": "full results in Appendix~\\ref{sec:appendix-llama})",
  "new_string": "full results in Appendix~\\ref{sec:appendix-llama}; SS details in Appendix~\\ref{sec:appendix-llama-ss})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddc65459-b82f-4ebe-811e-8bbd19319e93",
  "isSidechain": false,
  "requestId": "req_011CbP2fHfMpY7ckVy2XSwBN",
  "type": "assistant",
  "uuid": "983fa3ab-8af4-4902-848e-ef344d57ecc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XUak69DR8Tjugr8gKNip9B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 259,
      "cache_read_input_tokens": 68109,
      "output_tokens": 201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 259,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 201,
          "cache_read_input_tokens": 68109,
          "cache_creation_input_tokens": 259,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 259
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
