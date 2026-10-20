# Research conversation: [Director 指令] [Patch — exp7 TF-IDF 关键发现，高优先级] TF-IDF per-prefix + ActorAttack 结果出炉，这是论文最重要的新数据之一： | Dataset | K1 | K2 |  — Part 6 of 13

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

[← Part 5](part-005.md) · [Transcript overview](../research-conversation-director-patch-exp7-tf-idf-tf-idf-per-prefix-actorattack-dataset-k1-k2.md) · [Part 7 →](part-007.md) · [Structured JSON](../../../sessions/7e/7e181e1207bea8c60134.json)

## Round 55

### Tool result

_source line 1293 · 2026-05-18T19:48:53.849Z_

<details><summary>↩ Tool result · `toolu_01JPBiV3fy8ZGZ5hvgGiHAhH`</summary>

```text
[3 <../../figures/paper/fig1_architecture.pdf>]
[6 <../../figures/paper/fig2_cross_attack_bar.pdf>]
[11]) (./main.bbl
[12]
[13]) (./appendix.tex
[14])
===
[13]) (./appendix.tex
(./checklist.tex [15]
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c703ae54-d6e5-482e-b010-4fd4727b069e",
  "isSidechain": false,
  "promptId": "bddd2ac2-53e3-403b-a1f8-035aa9a55c3a",
  "type": "user",
  "uuid": "448d318e-4187-4b54-b175-9f782a8ce673",
  "toolUseResult": {
    "stdout": "[3 <../../figures/paper/fig1_architecture.pdf>]\n[6 <../../figures/paper/fig2_cross_attack_bar.pdf>]\n[11]) (./main.bbl\n[12]\n[13]) (./appendix.tex\n[14])\n===\n[13]) (./appendix.tex\n(./checklist.tex [15]",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c703ae54-d6e5-482e-b010-4fd4727b069e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Tool call

_source line 1294 · 2026-05-18T19:48:57.156Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JaEVBHyokn4razDCB6fGu7`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper && strings main.log | grep -E \"^\\[\" | head -30",
  "description": "Extract all page markers from LaTeX log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "448d318e-4187-4b54-b175-9f782a8ce673",
  "isSidechain": false,
  "requestId": "req_011CbAcXvmDk1rYizorwuZbi",
  "type": "assistant",
  "uuid": "71e86242-193b-4b76-9b4d-030853b1587e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YSzeDAVhYB6E711atqq3Bp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 316,
      "cache_read_input_tokens": 58106,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 316,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 58106,
          "cache_creation_input_tokens": 316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 316
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

_source line 1295 · 2026-05-18T19:48:57.240Z_

<details><summary>↩ Tool result · `toolu_01JaEVBHyokn4razDCB6fGu7`</summary>

```text
[Loading MPS to PDF converter (version 2006.09.02).]
[3 <../../figures/paper/fig1_architecture.pdf>]
[]\T1/ptm/m/n/9 (+20) 9-class per-sua-
[]\T1/ptm/m/n/9 (+20) domain speci-ficity
[6 <../../figures/paper/fig2_cross_attack_bar.pdf>]
[11]) (./main.bbl
[]\T1/ptm/m/n/10 (+20) Patrick Chao, Alexan-der Robey, Edgar Do-briban,
[]\T1/ptm/m/n/10 (+20) Patrick Chao, Alexan-der Robey, Edgar Do-briban,
[]\T1/ptm/m/n/10 (+20) Suchin Gu-ru-ran-gan, Ana Maraso-vi
[]\T1/ptm/m/n/10 (+20) Pengcheng He, Jian-feng Gao, and Weizhu Chen.
[12]
[]\T1/ptm/m/n/10 (+20) Milad Nasr, Nicholas Car-lini, Chawin Sitawarin,
[13]) (./appendix.tex
[14])
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71e86242-193b-4b76-9b4d-030853b1587e",
  "isSidechain": false,
  "promptId": "bddd2ac2-53e3-403b-a1f8-035aa9a55c3a",
  "type": "user",
  "uuid": "bc831052-6a1f-4dd6-ad53-cffce7963f27",
  "toolUseResult": {
    "stdout": "[Loading MPS to PDF converter (version 2006.09.02).]\n[3 <../../figures/paper/fig1_architecture.pdf>]\n[]\\T1/ptm/m/n/9 (+20) 9-class per-sua-\n[]\\T1/ptm/m/n/9 (+20) domain speci-ficity\n[6 <../../figures/paper/fig2_cross_attack_bar.pdf>]\n[11]) (./main.bbl\n[]\\T1/ptm/m/n/10 (+20) Patrick Chao, Alexan-der Robey, Edgar Do-briban,\n[]\\T1/ptm/m/n/10 (+20) Patrick Chao, Alexan-der Robey, Edgar Do-briban,\n[]\\T1/ptm/m/n/10 (+20) Suchin Gu-ru-ran-gan, Ana Maraso-vi\n[]\\T1/ptm/m/n/10 (+20) Pengcheng He, Jian-feng Gao, and Weizhu Chen.\n[12]\n[]\\T1/ptm/m/n/10 (+20) Milad Nasr, Nicholas Car-lini, Chawin Sitawarin,\n[13]) (./appendix.tex\n[14])",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "71e86242-193b-4b76-9b4d-030853b1587e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Assistant

_source line 1296 · 2026-05-18T19:49:03.253Z_

关键信息：
- Page 11: `\bibliography` 开始 → References 从第 11 页开始
- Page 12-13: References 继续
- Page 13: appendix.tex 开始
- Page 14: appendix 结束
- Page 15-16: checklist

所以正文（Abstract 到 References 之前）= **10 页**，超出限制 2 页。

用 PDF 渲染确认具体哪页结束正文、哪页开始 references。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc831052-6a1f-4dd6-ad53-cffce7963f27",
  "isSidechain": false,
  "requestId": "req_011CbAcYBbwbmxezWKz4oHBC",
  "type": "assistant",
  "uuid": "e38e10d5-b9ba-476b-9203-015c0483443e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SF1a23VHjm5YaEfKSVPzZ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 58422,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 523,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 58422,
          "cache_creation_input_tokens": 523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 523
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

_source line 1297 · 2026-05-18T19:49:03.466Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DyXQsUMHYwwit15SAaZMpX`</summary>

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
  "parentUuid": "e38e10d5-b9ba-476b-9203-015c0483443e",
  "isSidechain": false,
  "requestId": "req_011CbAcYBbwbmxezWKz4oHBC",
  "type": "assistant",
  "uuid": "e9fcc4d2-33e8-43ea-b7b5-3018fc8732cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SF1a23VHjm5YaEfKSVPzZ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 523,
      "cache_read_input_tokens": 58422,
      "output_tokens": 223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 523,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 223,
          "cache_read_input_tokens": 58422,
          "cache_creation_input_tokens": 523,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 523
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

_source line 1298 · 2026-05-18T19:49:03.473Z_

<details><summary>↩ Tool result · `toolu_01DyXQsUMHYwwit15SAaZMpX`</summary>

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
  "parentUuid": "e9fcc4d2-33e8-43ea-b7b5-3018fc8732cc",
  "isSidechain": false,
  "promptId": "bddd2ac2-53e3-403b-a1f8-035aa9a55c3a",
  "type": "user",
  "uuid": "31c3a9b6-003a-4aa8-b601-43d2aecf5e3c",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__pdf_to_images"
    ],
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "total_deferred_tools": 50
  },
  "sourceToolAssistantUUID": "e9fcc4d2-33e8-43ea-b7b5-3018fc8732cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Runtime record

_source line 1299 · 2026-05-18T19:49:03.600Z_

```json
{
  "parentUuid": "31c3a9b6-003a-4aa8-b601-43d2aecf5e3c",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "880b2aab-11b2-46da-9768-d137eaaa2d19",
  "timestamp": "2026-05-18T19:49:03.600Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

---


### Tool call

_source line 1300 · 2026-05-18T19:49:06.971Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01XxW5SBVSVohGvYZBiuTWR7`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.pdf",
  "pages": "8-12",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "880b2aab-11b2-46da-9768-d137eaaa2d19",
  "isSidechain": false,
  "requestId": "req_011CbAcYeRVWzcybUECnk1m7",
  "type": "assistant",
  "uuid": "3f42f3fe-59a2-4bb8-97a7-4f8bf4c9bd74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AE4PkVs9Pe2chD44Z7kzwc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 58945,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 700,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 144,
          "cache_read_input_tokens": 58945,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 700
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

_source line 1301 · 2026-05-18T19:49:08.958Z_

<details><summary>↩ Tool result · `toolu_01XxW5SBVSVohGvYZBiuTWR7`</summary>

```text
Error: result (3,386,991 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-paper-agent-6be59e15/806ee39a-95a2-4db2-a3a1-7728b3dca63e/tool-results/mcp-agent-ml-research-pdf_to_images-1779133748949.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-paper-agent-6be59e15/806ee39a-95a2-4db2-a3a1-7728b3dca63e/tool-results/mcp-agent-ml-research-pdf_to_images-1779133748949.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f42f3fe-59a2-4bb8-97a7-4f8bf4c9bd74",
  "isSidechain": false,
  "promptId": "bddd2ac2-53e3-403b-a1f8-035aa9a55c3a",
  "type": "user",
  "uuid": "b71a9471-4d0c-4ad4-a783-a4e18e7a3986",
  "toolUseResult": "Error: result (3,386,991 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-paper-agent-6be59e15/806ee39a-95a2-4db2-a3a1-7728b3dca63e/tool-results/mcp-agent-ml-research-pdf_to_images-1779133748949.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-paper-agent-6be59e15/806ee39a-95a2-4db2-a3a1-7728b3dca63e/tool-results/mcp-agent-ml-research-pdf_to_images-1779133748949.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "storage": "sanitized-trace-archive",
    "source_line": 1301,
    "serialized_bytes": 3387028,
    "serialized_sha256": "5c1b2945d5bcc388f8adbb08851d5a46f8a57293b48004f25439ca62735c8d79",
    "note": "Complete sanitized source is retained in trace-files.tar.gz."
  },
  "sourceToolAssistantUUID": "3f42f3fe-59a2-4bb8-97a7-4f8bf4c9bd74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Runtime record

_source line 1302_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] 紧急确认：当前 PDF 16 页，EMNLP ARR 限制 8 页正文 + 无限附录。  请检查： 1. 正文（Abstract 到 References 之前）是否 ≤ 8 页？ 2. References 算不算在 8 页限制内？（ARR 规则：references 不计入页数限制） 3. 如果正文超 8 页，需要立即压缩——告知超了多少，哪些内容可以移到 appe…",
  "leafUuid": "b71a9471-4d0c-4ad4-a783-a4e18e7a3986",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e"
}
```

---


### Runtime record

_source line 1303_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze TF-IDF per-prefix results for ActorAttack",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e"
}
```

---


### Assistant

_source line 1304 · 2026-05-18T19:49:11.407Z_

结果太大了。逐页渲染关键页面。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b71a9471-4d0c-4ad4-a783-a4e18e7a3986",
  "isSidechain": false,
  "requestId": "req_011CbAcZ3T5dwxRZmMT8Qhbi",
  "type": "assistant",
  "uuid": "03872384-9e5a-4c63-ac30-316b31838b4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfApS6Gv6JaheVCCBDVw7E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 562,
      "cache_read_input_tokens": 59645,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 562,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 59645,
          "cache_creation_input_tokens": 562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 562
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

_source line 1305 · 2026-05-18T19:49:12.318Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01NajVjfhvbEYcKMyd3hSHqG`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.pdf",
  "pages": "10",
  "dpi": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03872384-9e5a-4c63-ac30-316b31838b4c",
  "isSidechain": false,
  "requestId": "req_011CbAcZ3T5dwxRZmMT8Qhbi",
  "type": "assistant",
  "uuid": "5c3f277c-572a-4dd4-801b-ab856accf2a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BfApS6Gv6JaheVCCBDVw7E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 562,
      "cache_read_input_tokens": 59645,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 562,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 159,
          "cache_read_input_tokens": 59645,
          "cache_creation_input_tokens": 562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 562
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

_source line 1306 · 2026-05-18T19:49:13.675Z_

<details><summary>↩ Tool result · `toolu_01NajVjfhvbEYcKMyd3hSHqG`</summary>

```text
Error: result (575,063 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-paper-agent-6be59e15/806ee39a-95a2-4db2-a3a1-7728b3dca63e/tool-results/mcp-agent-ml-research-pdf_to_images-1779133753672.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-paper-agent-6be59e15/806ee39a-95a2-4db2-a3a1-7728b3dca63e/tool-results/mcp-agent-ml-research-pdf_to_images-1779133753672.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c3f277c-572a-4dd4-801b-ab856accf2a8",
  "isSidechain": false,
  "promptId": "bddd2ac2-53e3-403b-a1f8-035aa9a55c3a",
  "type": "user",
  "uuid": "fcc1e5a3-ef77-45c7-9431-60fc8b9dd752",
  "toolUseResult": "Error: result (575,063 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-paper-agent-6be59e15/806ee39a-95a2-4db2-a3a1-7728b3dca63e/tool-results/mcp-agent-ml-research-pdf_to_images-1779133753672.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-persuasion-turn-jailbreak-detect--claude-sessions-paper-agent-6be59e15/806ee39a-95a2-4db2-a3a1-7728b3dca63e/tool-results/mcp-agent-ml-research-pdf_to_images-1779133753672.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/_pdf_images/main_p10.png\", \"base64\": \"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F198cfoKRnTVs2fPypUr165d+/Q95TQBydyk4ZprrtGZxpw5c+rUqdOhQweUpHfv3mlYTjOOHTs2atSoZs2a5cqV69NPP02rYtSvX58ChHE/hHnPPffkyZPntGqjB4MHD47FYgsWLEh+Vqnf5c88jBw5EpOVsnlu3LgRt9W6devGjRvffffdBm6zZs2am4KAH5QEJ06ceOmll9DSzp07N2nS5KGHHvr999/l0gcffDB58uQkF/LVV1/t2rXr6NGjcbgFCxb85JNPkpxVKsPcqZOMZcuWdezYsVixYvSplM1ZARZapEiRq6666jTlb2FhuahFOsLhw4f79u1LxBOXi548eXLLli05cuQoVKhQok85evTokiVLeMr//ve/pJb0P3j99dehMQSI/P/3339nzJiRN29efEOKZJ6GiC6o5DQHfu7nn38uWrQoD0pqSVPgiT/++GP58uWnTp0aeAuBFFEa6U9r9E/BPv/8c55CVHf6nnKaULdu3UIadFY/ZcqUrFmzbtq0yXGD1EqVKj3yyCNpV1IT6L/79+9v2LAhrZCGXLR79+7VqlWDGAdeTR1t9ODdd9+94oorvv322+Rnlfpd/kwCKvrggw9+9tlnKZst3RMDPmnSJDmkh6KBhw4dCkzcqlWrc88998orr7z6FNANWnP16tWSAHZ022236elvuOEGdQhlHThwYBIKOWDAgGbNmsn/vXv3lipV6umnn05CPmkCc6dOMo4cOdKvXz+Ef/q4KLjllltat259+vK3OMthPcEZiz59+iTndizmoEGDUqow0SGxeFwuKsD/JYH8CDJlypRSXLRMmTLXXHONfmbZsmX4df3M22+//f333yf5EWnVHE4igkpOc9SsWTOVA9NEn4hORo/+k9PcGZGLrlu3rkmTJoGXDh48mDt37oceekidmTt3LnVcvHhxKhUucWA805aL+vHjjz++8cYb6jAhbUyfSP0un3x4WiEFE0dHp06dkkbkzLjxxhtxZOrwzz//POecc3r16uVPySUIIRRIPzlt2rSLL75YJcBrvPnmm+rqJ598Qltv2bJFnWnbtq2eIAoOHDiQM2fOd955R505ceJEQjmcqcBSmbnoaVLFJCCZgZDFmYoM5gksIuL111+/4IILkpNDmzZt9PeaqQaiq9ThojjalOKimTNnLly4sOd95+23375v3z75/9133+XK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Xbq0Xr163BPZScR+//33oDMztkqVKig6YvXFF19cffXV9957L+InZNI2btxI0hCZ3Jxoy7pKtNPzzz/PbYkDt0Umffvtt3fccQdnOnbsSGSyZ8/O30SS87ly5UJeIj67dOmSL18+0V3eOwQdgdq0adPx48ejwR544AGSP23aNBOTHj161K9fnyQgdDNkyEBuly5dWlL9zDPPcKvq1asboYh+K1OmDOrXp9Q+//zzt956C5Fct25dn2CDBw8uVKgQmbZ79+4777yzcuXKks8h89Y/80m1vLOQAEeOHHnyyScJ8M4773BIwgsXLiyHt912W7p06ZCyZF2RIkU4+frrr1NM1IoCBQpccsklZGzI2LZv357858LLL7+cP1q0aIFW90mdQbWooiiKoijKvxbVohc2N99886WXXmoOT5w4YWtReOKJJ0SLyiGShsNBgwbxtxlvbNSoESdfeOEFCTNmzBgOR48eHe6hhw4dijgV89lnnyWMmSZ67ty5SpUqPfbYYybAjz/+SAAeHfLydu3a3X///eba1q1by9+zZs0SgWRCzps3jzNIazTbgQMH3n//fU4iqpErEmDXrl0EQNCGuwNZJFcFnQxEZufJk+f48eNBZ5yTwLNnz5ZfiQaHRmUhYnkKIs0MlnKmWLFiPtmyfPnyESNGBB1VzK2Q3CGDoWmRjvfdd58cEj0CL1iwQA5deevFG6BChQpGiwK62mjRoKO3OWzQoAHPpUpQMThJPDlZq1atw4cPc7h161YOEaU+qUOHI0p9AnhRLaooiqIoivKvRbXohY1Li548edKlRXHZbS0qsnPfvn32TVxhVqxYwSH6JNxDZSpmuCFNwSWHZsyYIeOxdhgZ0rQnyhpQrVmzZv3iiy/k0GzD41WSaCfOPPnkk/bln3zyyVtvvSV/ow8J0KpVq5B3EKU6YMCAdxIoVKgQZ77++mt+7du3r52KTz/9lMOPPvrIPEhGWT/++GM5RDT6byX11FNPiXBF33KhmTzspU+fPl999ZX8PXPmTAIbwZwELVqpUiVbi8r4udGiIjsnTZpk38QVBiiRypUrh3uoLBadOnVquAAhUS2qKIqiKIryr0W16IVN0rToX3/9Zd/EFQZxyCF6JtxDO3ToUKpUKf+IueTQiy++yOE333xjh+nZsycn33vvPe/lxIF08WuzZs12795tzofTop07d/beBHX05ptvvvDCC7JANOQdRObNmTPnm/ORua/EzRaBixcv5tCsDgWCofEoBTmsXbu2d7mpjRHw3bp1K1KkiE9IYfPmzf369WvevDnPNVN/U0iLorTtm3i1KArQpNQLKtT/DQUivGPHjm3Op1ixYnXr1nWdnDhxYtgcSYiJalFFURRFUZQLHdWiFzapokVLliyJqPCPmEsOyQJFl8YYNWoUJ5GLIe/AtcWLFydAtmzZJkyYICej1KJnz57t27dvixYt9u3bd+zYMR8tOnToUA63bdsWMg5cnjdv3ptuukn2IuKeZPipU6fsMDIL+uuvvz5w4ED16tX9s8VQvnx5e8ayF4Q0ceaJPE7inMa1aDRvKFatWvX9+dx3330jR450nbTfPoREtaiiKIqiKMpFgGrRC5v4a1GZimlm24b7SKZLDg0bNozDPn362GFQoZw0M1FtZOPf06dPDx48OEuWLOnSpdu6dWswai3aoEGDMmXKyGxYfy360UcfuRSXsGXLFvljx44dhQsXrlu3bs+ePbt16+bd0gkdyx1q16791ltvjRs3LmRuuDhy5Mgll1xiz/V1QQEVKlQIdWfHOY1rUYRop06d5O/oP52qc3QVRVEURVH+tagWvbCpWLGirTHOnj2LfkB4mDMPP/ywvUdO8rWoTGo9dOhQ0PluyksvvRQyWPfu3Qm2dOlSOeTm6dOnL1GihB2mXbt2BQoUOHHihPdyhJ/5+4svvjB7Kc2ZM4e/X331VfOrV4vKtkBNmzaVQ9lpyWhR1x02bNjA4VVXXWWPxS1cuNCoyueee86sVg1HkyZNuAliDN3rH1IQbekz+jd27FgCjBw5Ug7la65Gi7ry1os3QJUqVVC/Jnqu+ydfix4+fNh+Q2FEaURiq0XNJlKKoiiKoihK2ke16IVN/fr1RXWguFatWsWZYsWKBZxNbjkzatQoxAOHb7zxhswslfAuFdSyZUtOGsX13XffcRhOTqCI8ufPL3+/+OKL4T4mKXNfkXzIA9kHSDZrNbvvcmGePHlc+sfQuHFjI1F+/fVXLlyxYkUwYffdevXqnT59+ssvvzRn7PmuokVz5sz5ww8/kKjnn38+Xbp0t91222+//XbkyBHvHRo2bMgZ8o1c4ox8bUU+oDJ58uRs2bK99tprRHvu3LmLFi3auXOnN7YiaB999NGQafHyzDPPXH/99T4BRCtWqlTpl19+WbBggcSQhMj7Am/euvAGkDnSaNQ//vgDNU4CA86muPJWQsK7xmnHjx/PyWHDhskht8qQIUPp0qVDRlgGh+XDOVOnTjVb/kYkCVr077//zpQpk3nXYOjXr1/27NkXL16cqLspiqIoiqIoqYVq0Qub2bNnp3dACIl8Qk0hwxAGl112GXICB71AgQJdunRZt25d//79ZUMglNjMmTPlDhMmTLj88ss5WadOHdTsmjVrqlevziGC0/7MpuH3338vXLjw9OnTkToht8AVEH5XXHEF96lcufKePXvk5Ntvv12wYMEOHTqg7lDFrq2MbJo1a4bsGT58+CeffIJwsteUoiq57X/+8x8uX7hwocSWxA4ePJiHShhZw4kEJaVEWMLUqFFDxmDtOwSd+cDNmzcnDznJ/8g2M364fv162VbXhsvRtK4IlypVyic5Lm666abHH3/cJwARIAzPypIlS9euXQ8dOiRlKsPFIfPWxhsAPS8vKcgTKgNRzZEjx0MPPUQGUkmuu+46fipRosS7776LRA86uzRVqFBBTlLWBw4caNeuHYeXXHLJ66+/fubMGe9D7777bop19OjRFFmU+RBMpBadMmVK69at77rrLoqbBD7wwANt2rTZtWuX/Cpf3An3dkNRFEVRFEVJa6gWveDZv3+/a3Dy5MmTmzdvFsEgH4eMLSi6DRs2RAx2/PjxkKOIiIc//vjD/1pRRER+48aNsm+QAcm9bdu2c+fO+d8B9WXWdhL4l19+8b8DT9m0aZNroSNaFOWGtFu2bNn8+fPROSg3JJC9YDXoSMcyZcr4x8fw119/IQjNbkzhIHpbt241+ySRmbK1rzkMmbc+Af755x9uKAtxSazkcAwhwmSXa2OniCRtjm64CBhdqiiKoiiKoqR9VIsqSmjQfnnz5t2xY4frPNL0jTfesM+86eB/N7Sx/DFixIhs2bK5luz+a5k4caIZzVYURVEURVH+VagWVZTQTJgwwd7gR0Cgdu7cWQaihw4dOmzYsEmTJpUoUcJ/16JPP/2UW33++eenTp265ppr+vfvn7JRVxRFURRFUZQ0j2pRRQnNX3/9ValSJTRk4cKF69SpU69evYoVKz711FN79+4NOhOhs2XLxq+ZMmWaO3eu/61Qoddff/306dMbNWo0cODAuERfURRFURRFUdI0qkUVxY+vv/568ODBr776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By66aNGiGjVqbN++XU/cvXt3+vTp165dK5cwlocffrhr165J+N4LFy5ELIaBwm+//UYEn0x08Yknnog/F0UBmjRp0qdPnyTPNmkzDIJNmzZF5KIpq+FB9Of9999Pci7qaI6kVeN///03e/bsKcVFDx06VLt27fHjx8f/1Q6pEmheyszkcocu7Z07dyYJF43WTF12Ld6qVav27dv73HD27FlijMuCi1rB2j0FDUIQ3HTTTYaLGiQTDBe9kvHXX3/FgYt6onXr1jlz5ky+/E+cONGmTZvky98gKrRs2TL+XDSZAL+N/0v37t0bkYte+vjkk0+SnIsmd3PcddddKcVFUwpnzpxp3ry5nvLKK69c4szk8sWMGTPmzJmjLv/444/Ec1H4QPfu3YPff6W2uLCjy4KLJkm7pyzuuOMOw0UNkglJzEV/CAOYg37bTz/9JOmnT5+WlH///fe3335bsWLFN998s3bt2sOHDydtwa5OpCAX5aWFCxdOvvxr1ar16KOPJl/+BlHhiuGigwcPvvbaa+P/XsNFPRGH5rgKuSj0nrBST7kymMkliM2bN2fKlGn27NkqJfGc5NSpUyVKlKDJgj9ypba44aLxhOGilwX279/vycKgXXLDoUOHvv/+e6jW0qVLN23apG+3hqmtW7fu22+/XbJkyZo1a44dOxa3YiclF4VP/i8M9CphOFS6OocDiXD59ddfIwX556oKDhIJRDpnzpyRI0eiXnp6OC6Kko0dO3bChAlbtmxx/ISfI6uJEydyD/Gx/tO+ffuINT/99NNt27Y5WmfXrl3cL//v3r175cqV6dKlw0+sTMB33303c+bMESNGuAtPJ/nwww+nTJly4MABx0+//fYb6aNGjVq2bBnaJYkXLlxo37499SpTpgw5r1q1yrMYCkeOHFmwYAGZ0PHcJ5TwCOn8c/jw4alTp1K7M2fOuAvphlsaOBuprCrSjh07JIXurT+LIfjll18sexE10QDCcS+4othEMPy6fv16x08Udfny5Za94W3SpEm08koNR48eldt4qaSoXvbnn38uXrxYz8qnuaX85I9YkJJbAmjdrFmzxo8fj+3z56JUUxVPnTqDBCQFSariUeXhw4cvXLiQSjkywSZQWoSMTNSRG+fPn583b557GadbbdQr5s6da9lH4MyfP//jjz/WNXnatGlp0qRJmzatQ24+mu+Gz9sFngqvc1HqSKNQNiUZBU8NdzcT9lZXiXPnzpH4zz//OPTT8lUzN9z6A/BkNM3o0aNpZU8uyg08hUBwb2fPnnVkGENz+BQDC/P555+rIU4FH4uXslyUojoOaEHJ0TTL1m06OKriLrOV0PtoOCTjkKoPUMjOnTtT31tuuUWkKuZOZybEmnRqzLVbjBQJa0lbU2bH+HIQoORUDU3wPG8MtacF8WJ0fze7oI9/9dVXmBrLjhYoKnGCOxNKSL/jFdOnT3ePaPuXH6PKI3QTetOXX34piQGbwxMEf0KW+vXrh6gliNc5CRKmUuS5ceNG9+PyOgyFfiYcjz/66KPk8Mwzz5Cn2gUTDolscYCxpWMiT7eDiAj3s8ePH9dNk+rU9FBJoYKq5OgDnd2RJ/R+zJgxWC1aypOLkgPGRCwwrab/FLA1eSlKiCfCo/EWx68++fsgYLu7DYIVk94C/MuMGTMwibzL3bLhnrLs/jXehmIvAsVF6Yy0F+UhZ/WrinY8nQ4IKKhwBUuk8bl6QGTlycIIPCybqcol7pj+xT+osXgQeof8BI/gV/k/bgM9STwveuRi0M+pDLolemnZHoVLXJHORVEsuRS7QwTG/1gKz0jOwIH+/ftXqVKFuI349YYbbsBeiMO2vLgoBrFixYrPPvusOIkMGTL07t1b/Yo14Way+vXXX998802eVQ1H3HPvvffSLlu3bn3iiSfuv/9+y/YWWOQKFSpw5xtvvCF3YqY7duxIynXXXfeGjQ4dOtSoUUOOItBLzuseeeSR7t27Y9FeeOEFgs4BAwaoX9u2bXv33XfTT7744ouiRYtWr15dOgyu6KWXXiK3m2++uVu3bj169PAshhSPIIBiU3gi1MqVK+fKlUtiX4CzKVeuHI8899xz48aNy5cvX548ebgsW7ZsxK04ntLAx2M99WpCSyiA8kBkS2mLFClCCvQPmVx77bUhG4QXunnFfzRs2BBf2KZNG3KrX7+++BKauGbNmgTozz///HvvvSfPDh48mPKkTp2a/1999VWVz4oVKzJnzty6dWueXbRoUe3atdOlS6fPvPk0N56AVxOvUIZq1aqROa/TJUDIiKbBPcj5qaeeKlasmA8Xhefkz5+fG9C9PXv2SCIvRYYPPPCAhCkIBCnRTBB13oiUdu/eTTokoWvXroUKFeJxfqLR+Sd79uzYlpdffhmF51IfPginNrRU3bp1ETjhy+rVq2Xenmdz5sxJM1l2Z6F10qdPj8C72ZACeLZ1OIR7uxJ4OIVXXBSRUimelWOZeKkVpqP5NBN1kQYFZCj6TOOSCSlqP1I4NXPDU38sO25AjMOGDcN1UYx77rnHwUUx46jHwIEDe/Xqdf3115cqVUoGI2JrjnDFoC/TLtSO2IV/EKA6y9ff4lkpx0XRAQSeMWNGNVWybdu2Bg0aSJWJJ1AkxJLaxmeffaY/S3BfvHhxrAGxZt68ebG0mDKU84MPPvB/Kb1GSMh//vMfkaqEGpKIPtSrVy+PDS5Lliyp9yx6Hybr/fffx+PQDbGlhDIBK0s+aEWtWrWoCGSAWiN2XebYE14H76KJmzZtimLQTKK3aALPohgUiYaGg/H2TJkyuUc90EbkQPEoGBVBT4YMGRKx/BTj7bffRtRkSBCGaknHoSQBmyMc6FkSvlNmRC0sSHESTEru3LlpR+x5qlSpMIDqQTSBd+FGYQU0CjdQZvkJ9yrOlHKSJ9XxL0NiWvzQoUN0nC5dutDBK1WqhL2iIwepuM+zxLuYApEw1k/NyRAT4q2aN2+O/4ICUTyE45iFO3r06MMPP9ysWbPFixcjLhy6nMCkh8u4YAzL0KFD33rrLTLEIskIXfDONXbsWLwSRhJlo/mQmz50Ei7/iIjY7m6DIIhWb2XkAsnzE4LCGSH/EiVKiJ/1f4p7eFf79u1R/nfffZf0xo0bK74tysxTmHEcNGaHSxyZ/IpUJaBCl1atWiWdl2cxUyTCIf3l41+wxBifqw10MZ2F0RNlhk9Cr5UrV/I/jUVQISMFXMqot/A1Umg1fl27di2XeOf4FDsZ94tiZYRb6yNbiEDmPHUuSgcQEcg9KDG6GE9GfvkCF45VVfEu9pHe++KLL8qlm4uKB/rxxx/lEmKDaUZZ5bJOnTrYa3XzQw89pIYtc+TI8eGHH8r/NCguQf5H1zFGjhAZVSaFKFMvKoZbX25Hh8GmEOiroso5BDJZNHv2bGFZ8uugQYO4FF9uJRz0oq/R9SwGsSzRvBpnRUpylp2aPSZDLnEMQglQvKpVq5ICI/ITenhpALyjTrlFFMq7IGrYCCnQG+JmfqX/SxSu1lxBYx577DGVA63Jr7SsZTtjKsjlbbfdNnnyZMJr/L1Mc8nMpH5SMYamQIECElscO3ZswoQJjlWgPs3dqVMnWLT8j1XidTyrBkHxK/ghZK5eJFzRZ42uzJjxCj0RUcgsH/VCaJAWSade3NyqVSvLHieGtWbNmpUUGDhGk5gGgk3IQnghDFzFT/5qc/jwYS5hIy1atJAZcnG37dq1U0WC5ToWhfq0tQP+b/dXeOGisDUKI91ZxhqostzvqeE+zcQl4Q6X+reUiEuefPJJ+d9Hzdzw1J+NGzcSYhK1qBQ56VcxBKpWrFgxNTgybdo0foVRy2UMzeFZDKwZ3VyNceBfuAEyL5f+Fs9KOS5KXURh9NATBYNBkUjHlP5FNMklTanuwWIgE+I2ucTJcgOMdP369TJ64g+oPvd7rtgkvoTqWLbVkpPPicvlBnoovyopbd26lV/plQEXcWGd4GPqsk2bNjz+0ksvySXmlxrphUcHdFVHmeWg6TJlyshMIC1IZ6Ep1eICSAvlUQ2Ndskhq1Jmn/JjYZAJlIOU2rVrE6JMnTr16aefxhgGaQ5/PPfcc9zvXqOL2hPlS9egh5KSL18+dU/ZsmVJUTNyDz74IIZOTfN+/PHHur+IiNhaHJAiv1q295TxxIAcwP9Z3F/IHpBV91NZJCB2ALFg84XqKC567tw57BvyVI9gf4SuqEBx6dKliE7dQHTErxBLuQzSmtgorLTyg5hrbsCIBcnfHxHb3dMgxKa32GQSO3fuLE8R8HDZtm1by/an4Z6iCVCS4cOHq7fffvvt3DZ9+nS5FC6KExd+iAwlH1nkZSU4bhpOH9HAH6HAEeXjU7BEGp+rHIRJkCm1lEwmAtUKwe3bt3Mp478QfqGp8hOmVWhafMqZjFxUWLVUUgA7pVegSaidzkV37drF/whC3anzeINwQG4ZM2bUv0mIh65cubIe7zq4aNeuXQnvlFcTYkOEKpfYGm5WsSM2SE5UFzOq85ZRo0ap/8ePHx+EizrCSuhEiRIl9BuGDBlSo0YNccAEylSNv/IT/5Bhr1695NLNRd3FILLB8RAD6fdInKoE8sMPP3BZvXp1dQMsi5R33nnHCg9/aWBMHdO/Du+CSyBF/84Ymk8KpaW94MM4J5z0+QTMmzePX/HlcrNcwpkdpcJ5p0qV6pZbblEpuNWOHTuqS7TFEcSHa26CXaqAAFUZXn/99ZA9RMqv9NmcOXO+/PLL+tubNm3qz0WpF3yVEqqIc//+/WqOEa9GZKmOWcaTkRtMVT1+9913k6IvLhVAtnUu6q82gF/xlOoSQ8wNOr10aKl/Wzvg/3Z/hRcuqp/mj3wc7eXQcP9mshJiVv3MEginLACLqGZuuPUHJXQE5UIUFRetX78+XFq9glhQ6IFapx1tc3gWg4AJ2er3IAGlS/4Wz0rRNboIJOTaQsYlifpXZGHadBw14NitWzduUOs7QMGCBUkJeMiCDzPRw1BRNkV4mjRpQoB4XoOs7xgzZkzEN6Jy3Kmf/4zS0srip4h4UINatWrpj9Dv0qdPDwGTdQFWwjCHXuunnnqKFLVaG3qDvumZ9OvXr2bNmiK3iOWXYUr3KGTE5vBHOC6Km9BvEzumhk0hcvAfNR8l44yyL8NKUi7q0+Jc5siRQ5eYjIU1bNgw4hsjPiukSx+ahHg4ZrlLlSqlc9HBgwdz6fj2psydKi6Ki8GoqpeKUdXJkn9roopZsmTRZ/Cwk/Xq1VMjdBHz90GQdncbhNj0ljCbPoU1lkuMG/cQGaobPJ8iWsAp6IvC4LSVKlVSK3WFi+qrmimeQ70ff/xxUnQvSWygDzr4w7NgiTE+VzmI6Ah6ly5dqpa8CTXduHEjdBSSz0/cID2CS5yIWqogC1ST9WvhOpKLi0KKqIZjIxzUXITi4KJEorJHVGJKtaHUbJL2x9ixY+mQkJBwN3juF1UtAuGX8deFCxdKivinokWLusdCxAw99thj7tfJwtRouShWr1GjRj61U+XcsWOHePROnTpJiicXdRQD88elY2UpkFWdMswhXBQ+oH4NePiKjzQiclERspouE8iazLVr12L3+ad8+fJPXIwnn3xSbIQwHDVdpoN7QtqsL1RB32jkPh0nXHOPHDmSKjzhgoQpMrvlWHIT5OyiDz74gHuIpOWyT58++skZqrmPHTsmd5YpU0b9Kit23BuWZMmuPgrrozaWTX6INtSlOGnYiEpxkx+ftnbD5+3+Cu9uHSHk+gFgDg33bybLnmpA2zNlyiRmlgxLliwpGx8iqlnEEmLhuXRE/47uQ18gpHaXUC37iaE5HMWgUUIXT+a44WPxrBTlomKfPbmovl/asSmuWbNmXKq5elC9evVQ4BNcfJiJ3h/pyzp5QHtRRXdT6sUIh+bNm2fOnDncr2JPXn/9dUe6UM1hw4bJpXBR3cJI/xJDStjE/z5LlCOWH25MDrKlSkfE5vBHOC7qaHRRQp3SSD/lLwZfWJlS2iTkoj4tjrGCp7klFuT4+ojPUi9ZSkNkLCnIX/dWSiYqCLz99tvTpk3reJHeFmIKsAzu96o1d/6tOXnyZP53b8gXBMnfB0Ha3W0QYtZbZfQg2DJ6pftTz6d4kVo14wn32UWYegcnJOYXtyUKjNOhCuF8ihueBUuM8bnKIUtwHYET4tX3kXruAyd4WL58Ob869gwnH5KLi4oI1MZFK4FhyooaBxdFa6XaxAoYAiUjNXxu4AmZYXMf+aPgyUWRNs4MMoOD7NChAzeomRzuf+ihh2Sor169emoRpmUHr1iEkD191717dzXKYsXERY8fP84NLVq08K8gtIo4ZsSIETNmzNBfEYSLwgG4VCvZFMT6y8LCiFy0UqVKt2qQVS7+0oiNi1arVo3EBQsWyLJh/UgAB3y46Pz580MJk3jYF8dqUjfbCdfcrVq1Cml7Rx1ApPyqz8ZbwbgoJBNxITfxUnfffbfjgCKcHBLu0aMHQYmjqMG5qBVebayYyI9PW3vC8+0RFT4cF6WCKsWh4f7NJJCZUvHZU6dOVd+BiKhmEUuIfebSMSGpdx8MPv/7f1I48Vz0s88+45Kq+bzFx+JZlyEXpTW51KPGe+65R61JjoiomAkM0EqYrpE18zEACft83wsNIXPHOgvw6quvhrR1vP5cVErreTZewPJfClxUj/KJkfr3749dxVVhN3SlTVYuKi1u2dOSt912W8BXOBDkWRlwpJUtm+bps3YCXSYwK4horly5HPfobfH555+7HasD/q0pzEpNxTsQJH8fBGl3h0FIjN5a9norNKdfv36ydFZ3Lu6nCMVJefrpp33eFY6LOk5jluX0uD/L/qBRxDDPvzoRhQDTvvVi6FswrmbIjCDcSj95B/UWqkVgg2LISUWOE8JQBmFkNETcPreeLFyUikkN9WqsXr2aFKJMVBkpCNvcsmWLLBE8derUqlWrZHZ0/fr1K1asUBtqDcJBPlfteSahwM1Fd+3aVa5cOSJU0U5ZsaZHZjTZ+++/LydD5M6dW7c7GFPiOaEuFSpUUGNdMXBR+e6zz9Y7MuddMCVRDyFgUXHRd955h8umTZs6cpYdobJ6PiIX7dKlS0sN+mRgOGnExkUhkCF7GZvMdY8cOTKcZHy4KG1asGBBhAzr69WrlyNA9/xqiGdzN2rUiMtw42ESGKn5CkHAb7pIZAZnXrZsmcNFDRkyhMLLQj6hYTFwUX+1sWIiP1b4tnbA5+0RFT4GLurfTAIZy4erWLbmKwFGVLOIJUS7uKxTp45+j9595NX6LkE3Es9Fx40bF/JdVB/R4l12XBTr2rBhQ1IGDhyIkuBVYXoRz1NViIGZ7N69m/+rVKkSWzVlBizc0Zd9+/Z1UGs9XW2A9+eisgpGiI0bQcp/SXFR4p/ChQurhY5iXePMRbHG+IXgRzTrCPIscsiQIcP111+PDnfu3NkxuGldLJMjR46E7EMBHZGx3hayQcBxMpkD/q0pKw70deA6guTvgxi4aMx6i+Tbtm1bunRpYWViV/256J49e0i58847fd4VkIvKmLiYcYKrqA6/cRcsohCmTJnS8mKoNc9XOWBSjm2S//zzjz4LaCWcV6S22VsJS3OFncXz+Nhk4aJCNR3HVQvPdkMnnFglsV9Lly7lJ/V1CgNPyHl0jqkJy56Uln/cXBQDQXinLh2Rmfr0yIEDB+QkAxmuJshWIS9mQrYnybiXFRMXRcWvteEYbqCrSBnExqkeEgMXlVFM9yETWNs0adKImsW2RtdfGrFx0QceeADHjNzkmIGKFSs6XirLCixfLmolBHAEqTgex2H0brYTrrllSY/7W+oQyP3798sr1Ol5goBcdNWqVdxWs2ZNyq/7GwmD1Kk/MXNRf7Wxoic//m3tgM/bIyp8DFzUv5nUpQy+zJkzR98XHVHN3HCUUJpS359sXdx9UObUqVNfd911+u4sgVL+xHNRKsvl7bff7ngFTFj2T/pbPOsy5KKWrRs0a4cOHYg4hwwZElXsFQMzEe3FbLqlNG3atIhvlC1k7oEP2QApu0lz5crloBkyL6p2jvlzUdlynz9/fofR43LNmjVByn/pcFFyhqGVL19e/ZoiXFTO2HNTRFot4smxAZ+VYU2qQ/XPuz6O4uBpcpSR4+toeluIKVDbEHRgl+Qf/9aU4+Lcw2cYEzQnSP4+iIGLxqy3coalWvYShItatjVOlSrV5s2bHe9SG5UDclF1J47Sn9y64S5YIo3PVQtMn3yyRdd2fKLQLqXDwjzVhJbsJlUrWOOJZOGiQjv1eMiypbA/AXJYkRzZdOrUKfm+KiRe7BEU9H/mmy4BgJel36ZNm1Y/2o5ENUvg4KKyqeaGG25QXh/uEbLnqeRSnXpi2aFkzpw55dBLLLU+5Czn16kN/bHtF5VVqfxVs0yUqlWrVmJx5GhZFdbLcke1p0jOOHGcX+coxunTp8XN6B9ORCAYXLXUNjYu6i8NmQRQx26JzPPkyaPud3PRP//8k1LJqXf8L05XP6yfutStW1fWUfhzUcqGkLNmzdq+fXvHT262E665haigV/oRL3RVOcNwxYoV/EqB9WhMzjCA8PjITYD3haKow1QFzZs317mojILLbJ4gIBf1VxsrAPmRwzBUB/Fvawf83+6v8DFwUf9mUpg7d27IPnVQb52IauaGo4TYbSLmkL2wXN0jx58o3XvwwQelyrolR8/li75W9M3hLgZlhsaELj6hilaTE5siWjzrMuSi6A/sLsiRuZ6QM7GKFCmiJ0ZkJjJWVbZsWX09PBrVs2fPiG8cNmxYyD61RT94ZvXq1TKMQsx0yy23OBoFYCKKFy+ulqD7c1EyyZs3b8gemVXKhk2DxUlQFbH8ycRF5cwefYlKRE4iZ7fqXFRWzSj5TJkyJRRgh4tCbC3eu3dv6Tv6LtYdO3boB7mFQ8BnoT1imjxX8jt4mpyGoPssK8E+yKgTbSQWyeH7OnbsqMbX/FsT8w4Z41InOWQuq6uC5O+DGLioFaveyvm3iovKnhfdn3o+VadOHRLLlSsnRxgKRowYoTpdcC4qOpwpUyb9K31B4FmwxBifqxbysRLHqkn1+Uy1IQubrA6OlTW9MkF4VkN8Cpz0XBTnIfXxGax17BflEfn6C2Eu5kD+d2xkN/CELNYiuK9fvz5h5UsvvUSUpiYiJBRTZ2OSLt/A6N+//7Zt2wYOHCimkNha9k+WKFFC/wLEbbfd9u6771p2bIdfUSdoC1VQWi4H3KmNPZa9MzBkfwRSL6p8wUJZE/kyQcg+ML1Tp059+/a9++67P/74Y/lVznynUqgBjkH80COPPEIEQ4fBZMuUC16W0F/mgd3FwIZyG4ZMjbnC0gnuVbQte970lZMSNrk3L+nwl8YzzzwjHh3CDA0gYEIOFGPhwoXy8UYJApo1a6YybNeuHTRGlUqmu3GK1atXHzp0KJKRbwnKr2LlHcdO6hCVcG96QVAh7Xh6K3xzWwkD2/AESCaeBv7Dg+rwHjkrpVSpUuvWraPzImc5ip30iCf+jxkzJuTa2SUfpKUAWEZyIMyCYiHkDRs2CLUT5+r+MrgEB+oEUX+1QQ2uueYa9FAFuBIM6ZPnQnrnzZt39OjRmTNn+re1A/5v91d4fnXEixJB6hvt3Bru30wCQnPirTx58jjmnfzVzA23/hBnhOyPoKLnkAHaTo47Jp9PPvkEIcM5QzaQDOHp8OHDK1WqpMh5DM3hWQzRKEDmKPCbb75ZtGhRUZWIFs9KGEFIkbMJ5Exg/SRhy/4olM6NaT4ZNVDDW9QlZJ8xQ2UR6YQJEz7//PPg7hKxy1cWMREQe2lxOQdbP+lNhhXUXPqaNWvkDGQ6KRL+8MMPMXEIPMipJLwRUxOyB7B4EeWHoZUpU0b5KewwXQN7olIIo7lZ72hic/QJKOlf6ohOGUaUmJv2RTilS5dWR4lGLL8caqV/oEgQsTn8Ib2MxkLJJ02adOrUKVlzSJiuD9DIeaoy6SdjTCF7XhGzQEXE+lEpmRqVCTpsBeJCRPr6unDyj6HFKap8dBTb/uKLL9LLXn31VXpWkDNjgz/70EMP6Yer6xCZqJOEMA5p0qQJ2YNxNAev6NGjh1hUyKGMONPBRXT49A8++GDIkCEVKlTQxyIjtqZMQYscMIkYaoqtxlAi5u+DiO1ueRmE2PRWBgErV65MEDJ//nxpaxwZqiLv8nwKx5EhQwaJGIlSqCBC0AMVWRakf/BCxqA9CacsQNPPHAkCz4IlxvhctZAZTsfeDXSPaER2UOIi5SMuauJQP6xHR3wKnPRcVDaLAseBIjocXNSy50JlXa5aqZzkBbsigYfDaohFDtlbz1VcPnv2bIyRpLdt21ZsOr5HRv4wgl9++SWJEqvJrAJenKABE0wkXa9ePfkeg5XAvjATxLv4FayAnAUPJxw0aJCMLBKS8iBRO3nyrLwXUvHTTz+h9LIaJ2QvgFFfOvrhhx/k08Yhe42WPhgJIREnwV8sHZGufOsc4ygGSOY3YCxt2rTxLIbks2rVqpIlSxL3wEKxqo0aNVLblvDisskei4m/R2+heWJtqazPVrpw0hAQ1KpKwRgpSb58+biZWsjojHBRRHTHHXfAK6DKNWrUcHwpq0+fPuIVQva0tlqdNXr0aMmcinfu3NmxYEmwfPly9+e8Jk+e/MADD0iGhAWyDidcc1t2EN+gQQPRjZC9W0P/JAP9F/cmv6ZLl47gABeO6PAT6lzEcOBZBOLYPHbgwAGZG6EtaCYatGbNmlJ3NEHFBzAT1S5LliyR7T2iFXLIpI/aoIfiOEP2rDKXqJ+MwoIuXbrIWACikA4iX1v1b2sHIiptOIVfuXKlDP2G7KV3RC0rVqyQlY0h+3PBxCieGu7fTAqotzq+WEc4NXPDU38sOziTzcbEClWrViVKyJo1a/PmzdVB8AsWLJCoVEou37u37G4SQ3OEKwZhNJlLOmxTd8A+Fo830gHlqcceeyzIrH4SYurUqarREQXmiFZWqo7pQAdIUUqOlZCAm8hYPmngQN26dQOuJEK8IXsYgl5Gf0QNJEa/8cYbhw4datnylP5I7ybil2xpUzGPAI/Trl079+rrcDh+/Hjt2rWVojZu3Ngxr0il6GWYo7fffhtv9eijjypLQj/q3bu3DGViM6dPn05Kz549xevxiNrghwGXSfKQ/dnGzz77TH9FuPLTZVq1aiVKUrx48cGDB4vuBWwOf0BypEiYEfoXPV31a5wR3ODnn38WXwaw2/LZqvr160sKteMRSi6xuOrF4rnovPoHpX0QW4tjiITVCKpVqxb80wYBn6XJ1GelFQgFVceE7KkBCJpAaX6OHDmQJ5363nvvxaooejls2DAxwiF7IE+daxCwNak4nD9jxoySfv/99zsGQMPl748g7e42CPJstHpr2TFA9uzZSafXYCfpL2JaCxcujA0M95RlE/7SpUvLu9AuHIeEBHv37pW4RWQyb968U6dOYULF+OOY3KuU6aF0+SDCEfhUx0cIBuFAcAiTcs9JEIrI5zYFkFK1oVQ+pXnlcNGYgdITYB05csSx5cMgIs6ePYvFDLe4zgGstj6IfsiG/C8RM3EDdtnBjqRR9u/fz09JOxxFnoQd7igKW0OAoiZzeKnDmRG/BqwyJJCs3DtSYoa/NHjRli1b1KCAI+pSa3Sx5vikcMKk4mQS2yd2Hcvjw8GnudUNGzZsCPdFaX5F6ySTqE6u8yzeuXPn5JtXKoX2jaHJIqpNROzbt08Xe1SaH+Tt4RQ+Zvg3k5TKcWSxQmLUTM9B9vbT0TytN2EfVY7tRD5Hc/iAV3ged+dj8S5HUM0WLVoQHa5evXrhwoUzZ86cMGFCv3794C3B6TRqGe2UheDAgQNoeGw+GhaEooZTRcueT/MxiQGxc+dOn7m7xJQ/NlBfQvxo+zu10GcL0WFdaTGM1CIqQcXc4jhZTF9AVxvts9iEaDsjLajGKcItrYfYoAMx21hKRZP5FCyR+ceAaPVWupK6n6JCSwL6UyIW3hXxxHh/QO99BjdjQ/w775UK1ANrQOyXyFZOQlxCXNTA4GqA59lFBgYGBhEBq8+RI4fnuqG5c+eGO1XLwMDAIG747bffSpQokdKlMLicYLiogUFcYbiogYFBbOjcuTPWQx3+pHDy5MkXXnghtskrAwMDg8Tjm2++Wbdu3YkTJ6pWrTpu3LiULo7B5QTDRQ0M4go5/jGqTzsaGBgYgMWLF6dOnTpDhgyYkaFDh06YMGHAgAHPP/983bp1o12LbmBgYJBUgIWq7cEPPfRQShfH4DKD4aIGBnHCiRMnOnfunCtXrixZstx66609evRwHHlqYGBg4I9Vq1Y9++yzRYoUyZEjR9myZSGi6uMNBgYGBimCCxcuNGjQIG/evI0bN3acTWhgEBGGixoYGBgYGBgYGBgYGBjEG4aLGhgYGBgYGBgYGBgYGMQbhosaGBgYGBgYGBgYGBgYxBuGixoYGBgYGBgYGBgYGBjEG4aLGhgYGBgYGBgYGBgYGMQbhosaGBgYGBgYGBgYGBgYxBuGixoYGBgYGBgYGBgYGBjEG4aLXoFYvXr1pfbFuTlz5ixYsCBurzt16tRfkXDhwgXHU6Rs3Lgx5pfy+K5du/SUY8eOffPNN59//vm+ffsCZnLy5Mn//e9/S5YsOX36dLh7duzYgTw9v0167ty5cPX1fy8PBine7t2758+fv3DhwogZKgQRQsRsHfU6cuQIecpPv/zyS8CSRAsfYer4559/5P69e/dOmjQpmQoTERs2bEDIcXjLmDFjPLUFOaxcuXLkyJHvvvvurFmzlFiSCWfPnv3oo482bdqUrG+JD9DhUTbWrl175syZL7/8csuWLSldqCRDQOOPan3xxRc+Nxw6dGj48OH0/USWx7Nfe97577//BnEcAt3pRFR+zLu6+e+//05kjWLGiRMnZsyYoVtmnw4eEInP4RIHXn7y5MkDBw5ctWpVSpclMmjiqVOnHj9+PKUL8n+I2McNrloYLnpFoVevXrlz5w6FQq1atUrpsvz/IHqgSNdcc03cDGL//v3vu+++kI306dPfloCiRYveeOONkj5t2jR1//nz58ePH3/LLbfUrl07tjfCDJs2bapz0d69excpUmTw4MFEzLy6W7du/jlQhi5dujz88MNTpkzp27dvoUKFOnbsSDCk34Mpv+uuu9555x3uqVevHvk7yHODBg1CYXD48OFwr545c+bbb7/tX7w//vijUaNG999/P26YAuTPn3/evHn+j1gBhBAw28qVKzuqs2LFCvnpgw8+IP+IJYkBPXv2lHelSpUqa9as2bJlk8vrrruO/1OnTi2Xzz33HBysYsWK/I92JUdJfEDMh9zy5cvH2x999NHkfl2JEiV4EezCkf7zzz8jAYIeukD79u25p1y5cslaEpSWt5QuXTpZ3xIHTJgw4bHHHoN8NmvWTJSNv5988klKlytpEMT4T5o0CdvLbc8++6xPVq1bt+YetCuRRYLwt23bFr8g/RdFfe+9986ePeu+E5uJycqbN6/cedNNN3Xv3v23337zzHbkyJF16tSRO3nEh4zt3r0bgcideBzYYCJrFAO+++47Xi1GDPOl0sN18OBIfA6XMogTXnzxRVTo3nvvpZp4n5QuUVjs37+/cePGadKkoZzY55QtTMA+bnDVwnDRKw0SQEfFRcMN9MYMd4aUJ/ExRFQg9BFnP2DAAMdPBBO33nrrxIkT5XLp0qVvvfVWyZIlJTKI4V2bN28mED927JhK6dGjB9GGGjfdvn07oQ9v8cmkSZMmOXLkUGPkW7duzZQp0zPPPKNu+Omnn9KlS/f++++rlOeff557vv/+e7n8/fffuYFQoH79+s9qyJUrlz8xwE+89tprPjdAiR955BECLKijpBBAp02b1n+6I6IQAmaL46cKD2ogatdvGDFiBDGiT0liQ6dOnXLnzr1kyRK53Lt3r2iUmpL98ccfS5UqJW20c+fOFOGiAiKk+HDRjz76qG7dumiankhfy549O+RQpbz66qtJzkUdVuXQoUP0ViqetG+JM3799Vf6iCxjoYKvv/56oUKFkpyLJrmFjwqext9RpHHjxkWMU5ctW1a9evXVq1cnSamgo7yRSP3UqVP+d3722WfS8RctWhQx22LFisnNH3/8cbh76B1yD24o6nKHRwytLMqmc1HPDh7Ve2PIIdpXpBTwRIhrzZo1/H/w4EHsbRCViDMcsrrppptSiovG0McNrloYLnqlARcYLRd9+eWXT5w4kYRlSPIMY0OGDBkQxciRI90/IaUxY8boKVOnTo2Ni+7fvx8Gsm7dOpWye/fu1KlTP/nkk/pt8EYfl0CYxa9t2rTRE7HaOvORuUGd8ZIbKXAzuXzvvfeohSPns2fPZsmSZdCgQT5ViMhFp0yZ4h4DvvnmmwsUKOCYuVUIIoSA2dapUyfi6lPCAnis/z3R4pVXXlEDFpYXF7Xs9fA1atSw7AneFOSi3333XXy4qCfefvtt3n7mzJnkewWZN2/ePPnyTynQ7xAdvFqlSB9JQi56aYrO4SNmz54d5zgVa8kbc+bMGfHO77//Xjr+1q1bI96Mlb7uuuu4GVLqeQO1zpo16/333889lSpVirrcYTBjxowYpiIffvhhBxeNz3ujxSUSUbRo0QJxqZHTSxD4Vsew7B133JFSXDTF+7jBZYQk5qI/hIFo5MGDBx3p+m4ffsXoE+fxN/j+OgMHouWiMqOShOY1yTOMGRkzZgzHRU+fPu0YuBVDGQMXrVKlSsuWLfWUN954g6z69++vJ8L3fBaYtWvXjl+HDh2qJ06bNo1E8uf/P//8k/+zZ8/ueLBo0aJqwarn9hUCBW6AR/lUISIXlQXPa9eu1RMlaA4XiAQRQpBsd+zYkStXrp9++smneGDdunWZMmWKeFtU6Nmzp67GnlzUsmtqXd1ctEyZMmnSpEnWVzRp0oSgKllfkSJ48MEHaTh9c3iSc9FLUHRuHxH/OPX999/njf/5z38i3kmgIh0/iHmhD3bs2FHu9xxBwyQ+9dRTzz33HDdABWMpugubN2/G+iHDaB9MJBeN+b1R4dKJKO65555LpCSeOHXqVIkSJV555RU9MaW46KXQx69O7N+/35OFKfN16NAhoVpLly6Fgun71Ykzice+tcE/XMat2EnJRf/999//hYFM5mzZssWRvnz5cnmWOE9SlixZIv+E25Vh4AZUf8GCBR999NHWrVs9uej58+dRu9GjR3ObY6Tq2muv5f7FixfjkPQthRiR+fPnjxo1atmyZTzufilKPN6G7qHDZYhufP31127N3rdvH6yDgvEW92k9Bw4ckDUwlJnbJkyYoE8gREQ4LupJn2LjovPmzeMpx0lRYv2VbgtkDjPcMPwjjzzCr46Tb2SyVB6R/2+++WbPB0eMGBGuhJj++++/378W/lyUzssraFbHFCj6RvrTTz/t+VREIQTMtnnz5hLYZcuWrWHDhj4r9EqWLEmQ51/TxCAcFxXoXBRNRiU+/PBDz6Owdu/ePWPGjHHjxsVw7o5np7PCc1Hup9cgUk+50ToUgy5Gt3IcCePzE3mqt+/Zs4duniNHjrRp065MwIoVK/773/+OGTPGfbwWFmDhwoXDhw/nBvf5Lp6lRT06d+5M7W655RbJX03AImfPVeI4milTppDVhg0b3PP2NIoMf2B80Pw4HLPkCdSJuhQsWJCq4fiV9KpXr+7JRf3VBhONicBcT58+Xbe64URHm3766adICREFHPnFCKtCigB37NixUoNeL6BWcDiMv6eP0ONUyjZz5kyaj6DKUYaDBw9STT0lZh+RfFwU3S5btiz3lylTxvHrhQsXbrrpJjpIbFzUs9UolazD7NevH/LExiIBvV2OHj0qd65bt05SVAzgyUX1Dh7Ve31ysCL1/XAIF1EcP35cdk/8+OOPmBq90elN2F5Ki346cguiLdu2bZs4cSLv/eWXX9SvmBTenj9/flUSfQg1XHwlwAxSSP6h+lOnTg24fiTaCuKA0D2K98wzz+jFU1wU3VuzZg2F9DzY0ifeO3funBziQBl4fPPmzRELn5g+Hq6CgkTGhFcD0FtPFoYds2ymqqgWZpl/aHHZLY/FdvxEqBP8lMpEIonnRY9cDCGfhDWyj1+4uH6DuCt8FT2ZO3G3lq1tIgVPCmTgANaNUIMYBYm1bNny7rvvdnBRxF6jRg1cb//+/SEzuXLlQs9IR8l69OiRJUsW7n/jjTe6desmymrZ5KRu3bpDhw596623MmfOfM899+in8hBtkGH79u0xCu+++y6PN27cmMbyzBCf9Morr8iJSrq7Io5s3bp1lSpVMHPEWA888AD3KJb45ZdfPvjgg6lSpcJZfvHFF0RslFxojOf5sZ7w5KJ///2350622LgoVJC36OdekL+cPoJL0+9U+1c9tydJTNC3b189kRzkEby4kI306dM7HqxXrx7p7dq18ywebo/mc++YdcCfi+JBeQVq40iXbVTom/uRIEIImG2jRo1Qb8lN0KFDB89yygawIOvoYkNALortQpOLFy+eJk0aiq2v8iUaoF+0aNFixIgRwrHpOAFP0QzX6eRXNxelMz7xxBOPP/44fRCREjXSo9V5KjzIr3RMuicNQbF79+7t/xO2mvfKwSTQRbmZvkmN5HiMN2y8/vrrzz//vAQijiMTx44dSzeHSJMtERI0gGJHLC1OhMIIbehm4/fffyecql+/Pl3PMRGNmapUqRKGhVag45PPvffeq4In4uBbb72VrN55550+ffrky5ePPLm877774u9rMMLURWzUm2++2S0BpUuXdnDRiGqDh8WmYd7JE4OQLl26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hTLpMB8hQoQIEYSIi0b4i2Hw4MEVK1Y88cQTCxUqBNObPHny4S6RP3bt2gUFLV68OEU944wzunTpsmDBgsNdqAgRjml8/vnnt912W9myZYsVK3b55ZcrBtvhLlRGcPDgwcaNG5csWbJ169YZ28AcISTmzZtHVZcpU+aUU06pVq3a3XffPX/+/MNdqAgRIkQ4ehBx0QgRIkSIECFChAgRIkSIkN2IuGiECBEiRIgQIUKECBEiRMhuRFw0QoQIESJEiBAhQoQIESJkNyIuGiFChAgRIkSIECFChAgRshsRF40QIUKECBEiRIgQIUKECNmNiItGiBAhQoQIESJEiBAhQoTsRsRFI0SIECFChAgRIkSIECFCdiPiohGOEuzdu3fo0KHff/99FuW/fPnyl156aciQIcuWLQv5yBdffPH+++9nUXmOJmRDRa1bt+7f//73rl27vD/t2bPn448/7tevX58+fWbNmpWlxQAHDhz4z6GgAFn90sxj/vz5r7766uEuxVGF/fv3I1K++eabjD1OR2LgTJ48+c033/z8889//fVXpfO3uWfx4sXvvvtuCsoaGgcPHlyzZs2vv/7+n//8Zv/bt+/3gKcWL948fPjC338/mG3lzAwo7VtvfZeSrH777cCCBRumTPnu++9/TnTPzz/v/eijH3jjhg0+4itkJjt27Pvwwx/efnv5unU7D03fsX379owVfvXq1fblzp07P/zwwxkzZmzdujXRI2vXrp02bdp7772H3Eua/9tvv839wfesX78+kkuJkEkJk3J89913L774YvjzkH3LjxKfMGHChg0bsqCAEQ4bIi4a4SjByy+/HIvFrr/++qzI/JlnnnnsscfmzZtXsmRJ3gJ1Cbj5t99+6969+2mnncadd955Z1aU5+hAdlZUs2bNeMtzzz3nSl+0aNHVV189derU77//ns7DPZ07d87Skixbtuzhhx8uXLhwzMEpp5xy3nnnnXjiiSeddFL16tUfeeSRFStWZGkBMoYzzzyT0n755ZeHuyBHDyZNmkSVXnzxxel9ENrJwKHPFClSpE6dOq1bt65WrRqXV1xxBZ3573//O/dgoJcpU4b8b7vttiwouz8gJy1atICLvvHGsltuGReLPaF/TZpMeO21rwMerFBhILfBprKtqBkAVPnJJ2eXLPksRb3mmlGZz3DixKUnndTL1BJ5rl37i+ueXr3mlC3br3//z1566cvzzx/w+OMz05vJf//73x49ZufP31035MjxRLt2U82ve/bsadeuHRwyXSXnqQ4dOnzwwQe6PHDgQNeuXXPlyiWZljNnTn41kyPCL7/8cvvtt1etWvW111578sknzzjjjHfeeSfgFRodEydOTHTDZ5999re//Y17Tj/99HQV/thBhiVMFgEFR3lGjBgR8n5X+T/55JObbrpJ3YzWz7JiRjgMiLhohKMEa9eubdiw4ZQpU1KeMxoX2bdlyxb+xhavXbt2mNXXgQMHZpJiHTyYmlWCVOWTRch8RYXBzJkzsdG/++4QY3f9+vUFChSYP3++Lvft21e3bt0HH3wwS0sidOvWja/m7fv371fKTz/99Oyzz2qyo0mTJr5LuMFIbUO7cuvXrx+sxmVfRsgMECmYVqNGpY/VzJ49u1SpUpj7Tz/9tJ3+ww8/1KxZk86DgFLKyJEjU8JFQ/arpUuXwg1+/vl/S3MVKw6C/Fx++YtJn4VoNWr0+k8/ZYeDwMGD/83M46NGfZUSLjp69FelS/d97rl5ZNix4zRxxYsuGrx//wFzT/fuH+XM+cTnn6/X5YoVP3HbY499kK5MunR5v23bqatX/7xnz/7p01cWL/4M9wwfvtDcAFlt0aJF+PXz3bt316pVy56W4vGrrrpqqINbbrlFjPSee+6xX8EjJUqUgJGmlXx0njx5pk+f7vsKJHORIkWCuWjc6fMRFw1AIgnjHdHZYyS8/vrrGGlJ17oNfMtfunTpiIsefYi4aIQISdCoUaPjjjsuvU+h2jNDsf7zn/+0b98+Y89mRT5Zh0xWVGbwz3/+E4sn+98LhgwZokVRVzoUVIyifPnye/fuDZ/hsGHD5s2bl6riLVmy5Pnnn09VbhFShQULFiCL6B4TJkzw/opBCSW44oordPnmm29mnouuWrWqW7duSW/buHEjlGDRokV2Yr16r0B7brllXGYKkFpMmLA0k6uvn3yyJvNcdPfu3y68cND27f8b4IsXb86btxs5U0KlrF37S65c/+/66w9xQL3zzjdiscdXrdoeMpMNG3Z17XrIUur48d9wQ+PG4w8tz+6zzjorzPYT+liNGjX69+9vUmbPnq2leIN///vfoqPbtm1TypgxY7xuKWeffTYvhaa6XkFK3bp1mzRpkpSLwmwjLppe+I7otm3bZmD287Dg6quvjrjo0YcUc9EFCaBevnnzZle6cQRH+nz//feffvrphx9+iEW1YsWKAwcOBL4qQoRsQpkyZbKfi0KAkbkZezYr8sk6HEYuWq5cOYyh7H9vPM1c83LRuDN9cMYZZ/Drv/71r5C5ffnll/ny5fvkk09SUradO3eec845Tz75ZEpyi5AqoCUvvPBCOkb16tUT3YMa/b//+z/9nXkuumfPngoVKtx7771J76xTp87dd9/tSrzuuj+46D/+caRw0aVLtxYs+OSbb4bd8O+LlHDRMWO+NnTRoHnzyeTcufMMXT788HtcPv/8IRNMr766mMT77psWMpPvv//ZtQt32bJt3NCmjduB6IUXXihfvvxvv/0WXPKePXtym72M1r59+/Xr17tuK1WqFH1vxow/i3HZZZdxuXDhQvseZD6JXlemp556asiQIcifiIumHL4jetSoUVSjWbI+whFx0WBs3LjRl4UZp7AtW7Z88cUXH3300Zw5c6Bg9vZdmJfrqTVr1mRPsVPJRdGUHyaA/Ha+/fZbV7qZyF+6dKlSqJ1Zs2bxB5WVwrIdxUArfPDBB5i2SG3vfm765bhx48aPH09H3Lx5c3BWdLuxY8cOHToUozapz8by5cvlpfPTTz+R/9SpU43/Hs391ltvvfrqq7a/lgEt+9JLL6GBvL/u2rUL+2nw4MHwE9cs3YEDB6ZPn46VHHc2igwbNuzrr90bkHjEFQJn3bp12tu5bdu2119/nXL6rjXR/UaMGEEF/vjjj6503lWkSJH8+fN/5mDZsmVr167V3/Rn3bZo0SKlrFy50jwbkmIhC9AE77zzDm0nN2BqHhLCs5UrV1a25maGxu7du6mE4cOH23rdt+EC8okHtgKg0sjtvffes3+l6j6zQNdS+pIlS5RC2QK+dPXq1WPGjKGeXQ3nW1EZ7tXe+jSg4YxUUSMWKFCgRIkS5ouovcmTJ2MG/f77IXFW6NgzZ86kQpBLLluNn+TbBgegT3ptskQI4KJxZ7Oftl25Vip8W41eijXG/S+++CJfYZeBsclI5BGXFWgKzxfxvQw6Ez9px44dNWrUIDeohd3J485Uo1cz/fDDD7QRzcorvBOIIQegCxSbvkeF86w3xgnDfNq0P2xxBgJi57XXXvONYxHQwxONo+wHteHrpqhuDGyvcr5ay02JPBuFxx9/XH/YXJT6nzRp0ujRo82wtcvw9ttvI3WpKzvqDLbpNddcQw7/+Mc/6AkBFcVw4zbGiCs9XVz0m2+2fPfdNjtlyZItCxf+UdoNG3bBwSZP/va330LNUC9evPnllxeNH//N+vX/i9ND5mee+Rzl6dPnk88+W6elxUTYtGk3NG/IkC9mzly9d+9++6eUcNF163Z61wMpGDn37v3njNKFF/7h4Txv3iEOjRSbxJNP7h0yEy+oyRNPfGr58p9c6QwTGtFe8PSCgYkqfPTRR+1EX2u1bt265KYwWso5b968rtIyPEm/5ZZb7EQeufHGG/kjvVyUbkwPRAijj8wNjCPJdsSUUoy0X7Vqleu9Ut8MEPQUQ8yIet5CD3/55ZfDjx1h06ZNYuOILG5g9LlUkhfcaUqoEUepbLWr2xDyujTCDbk9e/Zs/kC9ItbMi2wJ4zuikRI0DYkoXBJdEgCZgxyeO3euS7ajL9Q0pCOlqXZbUwQAjbZ48eLwdeiVkBEXDQamiC8LQ33Hne6tS3qLqBaNazYK8bfrqfChOjOJFK+LbjsUIp8QTtl24uL2DRpIMomAhjqJujQOHhESAblz1llnPf3008jcRx55BNsa48z8ipSBhyCgMWj+/ve/X3LJJQFZdezYkRvmzJmD9CxfvjwyK5HViFC+6KKLEAcYPQMGDDjvvPMuvvhiLs855xwsvMcee+zss8+uVKmSUuzJNgxTFE/37t15ihwKFy4sm1LApjzttNPeeOMNxkyDBg1Kly4tbUGe995770knnSQBVLNmzTJlyiA9sdQhJHqWMt9888358uUzawLYsldccYVMMXRAyZIlZa9TVBfTaNOmTcOGDRmZXbp04QYKf+2111533XWIRZQl34j21ccCsqJ/Uh5SrrrqKtMKd9xxByk33XSTyTYMF+3cuTOPfPXVV4gAqvH++++PO9Tinnvu4dlSpUrppag01D8Fk3ZXSJITTjhB6iFRw3nzkSkQ3AoMuurVq9OIyCn6TK5cuSpWrEhttGzZEoElz1J5W5noi0grOmGrVq0SdRjoBMSGKuJFyoHGMpreW1EZ7tW+9clXQ9IUNcGsNFKShx56iJTjjz/+YQcPPPAANpC+zt4ViaKlN/bt27dXr17FihWrUKGCTBbe0rp16yJFipx55pmQWArJg/Xq1QtobhvBXJQak31AyZUS0GqDBg0qV64cN7do0YJWNqGAeQWdHx1PD6EdqRmb12F5VK1alXv4g8rhQzSPg9UlOxJGSm6QTBq6R48e5557LokYDSYHzKZmzZqRLR0PmUCFUzAz0RB+ANqgsZ599lnaF+KEacJIpM75W7/S+TXMKQzFZgjkyZOHPEkZO3asySRRXW3evDlgHGUz6MC33nrrcccd51rVwcqkV993333Uas+ePSkhA0cl1HAGSWcVBcNF6b20b9myZbmkNuy4lJMnTz755JNfeeUVGq5t27aFChVCR+snKo2S8Mhll11GT6BdEr2oVq1afIgxaAzCcNGff97bs+fHil300kt/bkEcPHj+uef2I+XJJ2c//fSckiWfPeWU3lxedtnQAweCJkm3bPnPbbdN6NLl/UGD5tesOTJPnm4vvPCpyVPsjvI8/vjMiRPdK4oGPM7bP/jg+7lz15IJZbM5bUq4qC/uvRdK/4To9759v+fI8UeoIRdp3LFjn0IQ7dnjrm1vJl7Asa+4YtiiRZt8f0XUo4K9/Nbgqaeeoj+E2Qtw4YUXFi1aVF0CUcBTp556qusedD3pmAomBV2P0IDxxtPJRTEXKTnqL3fu3Dly5KA/6wZ4sqiLWbSfP3++5Dx8LO5EakXZKTAbTyEfkGMXXHABl/wB46Lno0AvvfRS7A1Gih06OGDsIEsxDygJb0fBkYPEjisHLxDRjRs35k4GFFos7izhKEQTIlQp8T9mZzbUrl0bWYpwRk5KKqKmX3/9dcqpiANeCeMd0bxOUdBIRAmSKMYSd+ZDGzVqNHDgQOoHLYlM1qTD8uXLyRyjiBdBe2g+pHEuBzRoou/CaqLzqGLtje4BdZhIQkZcNBh0WptkbdmyBRuGAYJajDtzMfxNwzHMscF0qcncgwcPYjxA0+zHgxcYUogs3C+6b98+7Hu+U2tZcWdfgR1u3oDhJPJplnTEzl2LVBG8wNJCjuhv+hamLRTO/Ir0x/TX3wgdJFqifN566y2G9wsvvKBLrFuJ5kT3Y9xwA+8ytimynhRkDcJFKcg1UsjKFA81YyQI5hTSs2DBgprAow8g2sy2E3gUz8J/dEnHgHKQgtGjuEFITHFd3cDjlJYUw0XjaaqOSpAVRQEkiCG95p7+/fuTwut0iX4S7YRpGNMKGkzZ7M9HbtpcNO5EeEsvF4VKcYOZdmJoIIv1N8YiPxnfWjgeCgwxTWLz5s2xVim2lGtww7nySdoKAFqObtDf1IBC6dDKZtazTp06pMA9TJ7cVrx4cTPMvUB12XEspEtMQAJvRWWsVwfUJyIV3ujyesW+9/p3wXxINORk06ZNWCRmiV7GPXZJ3DGDqBYu6R5du3alUaB8ULtEleBCMBcFvJcbtNc3aavR8bjZ9tGlViFy5lKzJyYsEx0DTmIErHqvcVdWNCnjowsz542afrK5KIPxyiuvNJcbN26kG9BwVJpSwgxAF7BXyMFM9tMQvIVHRCYpyfTp02NOzKdHHnlk7dq1pJA5KdigWvoIqKuAcZT94BvVneweiHGAET948GCTIutt/Pg/dvfJJA2/X0D5U/+9evWSbsXuJOX222/XDdgZefPmvfzyy3VJ/VCxEBKTg4KTB/voYvpQ+b4TnWG46K+//g6BrFbtJZuLxv+YV5pBSqlSz48Z88fsxu+/H6xRY4S9E9IXdeqMmjbtzzDU+/cfOOOMPxZCZ8360/pv1mwSl8E+ujNmrLJ9XD/66AcuO3T4X8TXrOOiZcv2+9vf/gwxumbNL+KcmzcfYgvSvVFQpC9b5j9Tb2di47ffDrz88qJixZ7OmfOJ5s0n797t44srJR7gkkZX4Yak5ilWLzTMbEqUCyiMxXUbNp7omUm54447jFtveC5Kp+VBSWnMbtE2c8+LL75oc9G4c1SM4aICI0Ks2MgNEULGgtmYzagkRfOb8RBjhw+RdujUqZNm3xBZpBitlAhbt24lZ3IzU6Io35gnHC5lZoDHHeNHtlaZMmWwBBCDfKy80rwSxndEi4rbywZz5swxnxZP01ZG2qPrEapivFoxUnzH8uXLJ/ooJNtPP/0EW7a5aHAd+pY/HnHRdGL58uUMNLMWja7n0rhBrVixwlAtmoO/uf+wlDMLuejChQttPklflOctlUJH5w/j8MCQY/jZh1ypvsTjIwSgWrVqVatWNZdaiJAljZkeO9QBZujQoYnywXLFxDEx1iVZXK44NiQjbPk+ZcoU1+toZZtPohKgjgcsqLTiFUi0IkWKmOM0xBP4OpObrFhbTWpHinF2X7NmjYuLwiddS1WjR4/W/J9JqVy5MtLQXEpLtWrVyv5YLxddtWqVi4siGdPLRfUu2+40DeTlkEBLzWZm1LwloOG8+QS3An0GG+Kaa64x98vL1yYPM2fOdNUznSFgT5oIib2SM2/evJo1axpPKm9FZaxXB9RnPM0eSspFtXZnuOitt95KwUxd8XbMbsN4Eej8Dc9JusnKi6RcVAu5OqMouNXiHi4K8cAae+WVV8z9MoyM2QfhadOmjf06+vxDDz2kv11cVIC82VwUG5FL18l+Mh9NZwgzAG0g8PPnz+8aMuLJWEtiU+hLXdr33HzzzcbASlpXvuPosACTztUDaQIazt4fQcMxWOSpq82i9rxMMCSlGzVqZFIkJMlHl1if9EBb3EEY6OHmMgwXlZw3wXtthPfR7dhxmouL8jcp99//P/e8/v2RsU888kjCg4hHjfoKrnXgwEHz7667qIEnmjb9k8+E4aKQz+OO6zF69Fe6hArySO3a/5t6yyIuCoXmvcZzeOnSrYnWP7mN9A8//CFpJjYGDvz8vvumXXrpUGVbr57PRLPIUt++fX1LCA3O7SDptzz44IMVKlQwk7maIbXXPwVNKAOtxI4ZM+a+++4zv4bnoi4petZZZ9nMSvsdbFtFGsfmouJyZko37nhpuRTNypUrbaWfdOzISLDnaDSFbUKLBQC9w522r0eVKlXsmVbMngsuuMAIitmzZ/PrRRdd5MrHK2FCclGEzIABA4wIXb9+vVrKnCAgRWnPShQuXBjjwescYUPr6oaLJq1Db/njERdND3bs2DFr1ixEtPFFEjXF+sJ6gXNpU6TaccuWLfxEL8XMRu0uWrQoYIEh5cgqLqqvsnevGc9bvvyjjz7S3747DUjUr9H5AUlh3GnoauPGjZOAMB1IrrNQC3sfYyKYlkKGQiB5sGPHjolu9nJR2tQl32WJmgM/+QlT+DoPjI1odxW0gku2iosaB5J4mmVmSI7EpZeL8oqAYhcvXtyWwj/++COXrVu3tj82i7goJS9QoADiG8XgGvO+XFThH7zOAgEN580nuBWkbo2pGk9TXbZSjKdZ89qdEnfCI5mD5ry44447TjvttES/xv0qKmO9OqA+42kWSXq5KJqyXLly3uoS60NAeXlRSCTlohhzMcc/Mx5i7Li4qJaIofTeR6gZHYRgvH+98OWiCjRiuKh62qeffmrfo/5jGG+YAWhDrg29evVypWuQyg7TZIRrjUXTEDVq1AhTV4nGUfZD32L3QFh0wAnJOv82fORnb+wivbFEiRImxUiPvXv3jhw5UgdpmLmVMFx0woQJLslvEJ6L/utf0325KOkm5eWXF5Fin43pwu23TyxcuCcvdf375z//7LRhuGjcOvRl06bdjz8+k0eqVPnfYMkKLrpv3+9ly/abOvV/KxLr1+8Uady2zX3OjXx3v/zS7YXrzcQXY8cuyZXr/3l3ogK5GJg5KRe2bdsWLLKEpUuX0sHM/sx4muz1LprJZihYsGDc2XZevXp1e1Ivw7GLsAFs1pQxLupdO0W/xBzHXZMSPHZkJNgGiayL888/P+CLBHFLo7hRiNpQYBxbeJ3ZFh5Pm7CzJa3glTBhuOjq1atjjh+vV4oaBihFaW/6UCbyr04EWGjsUB/d4Dr0lj8ecdH0QC64rjAWWNH2jlDzq9loaggaZC3bIlplFRdVFdhbvRFk8+fPxzoRQcda0jfbe3UYclgzqgXvJuYIvsC47NGjR4cOHaherQCY3rN8+XIF5MybN+8jjzwSPGUVdyQgFuegQYO0lhVggoTnomaRDRFsr3P6gsHAhyBk+cNFirKIizZo0CBmLe9gW3M5evRou1RZxEVVHvm6oODttcd0cdF44obz5hPcCvQQ7HjonJkkghjkypXLdZ7q+PHjzSzD7t27y5YtG7DFqGLFisErOb4VlbFenag+4xnioqjVWKB3QNZxUTS09vDIPEo6dlxcVIuW3lgygjpJgAd+GC6qeXpXqDDaIuZATrbp5aKdOnXi1y5durjS1QHk/O/LRekSxthNWlfeccR7z7VQuXLlgMdTCJelpSVfVygXG9rhbKo3KRJxUe8O1QceeIDMERfaFWxmgcNwUa11a9LEhWzmohddNPj88wcEvCUkF43/EdtiQ+vWb/Xp88nixZu1T9X8lBVc9LbbJgwb9qWd8vvvB3U6y8qVhyxy/vLLn/tFN250n8DhzSQRtAo9YIB7w5SEkr2fwsbatWv5FdkbkDNyG8lgHz0aT/ObLV68uOtm9U9YVtwZ44MHD/7Igma7unXrxt/2DmcbAVzUhCZKLRc9++yz7XcFjJ2kXJSXnnso7MhG2qMhSo88b9Kkyamnnoq+kG5CiNkB21LLRbXxJ3gWIFVcNB5Yh2G4aHA1HsvQiuC8efNs82zZsmUkMiShYIsXLxYL09w9PRZzC2XK/dC0L774wkQ8ygZkCRflw/SFAbFY5bJr7yYlRXx9zpw5f5Xo0ocdkBBEgInt4bLa446wvuuuu2AXmujyBqUUGPytW7e+8sor1Rxy9UwtFy1ZsqQ3eoENVNFZZ50lbzTxhGzgouhXqBRqkpzpgdhtt956q6tgWcdF444ZTT4yMRPtFxV8uWhww3nzSdoKM2bMOOGEEyjSxo0bt27dCpOEmbjuYVwrEgONNWrUKAhhQIbYLrDZgPAw3orKTK/2rc94hriopod9F3yErOOicoSm16m5k7aai4uOGDGCy0SbV0eOHBlzNkUnyi0MF5VBQFauZwsVKpQvXz5J/vRyUa2EeFmNJowUMcWXi27atInE+vXrx0PUlXcc0YfvtmA7CmYpXJbWunXrYoc69bmgOSBDy5MiDBelq3Bp9j5kgIsqiO4NN9zg/SmbuWipUs8XLPjk/v0JRU0YLsrjHTq8c/HFg7ds+UOqyEc3S7lo164zBw2a702XP+3nnx+yprF69c8klizpjiOVKBNfzJ4NKXpi8GD3/b1796YpE8lzbUlAOyTKFgXasGFD74IVDyLK8ufP70qXmNLuZYVqSwTX+aUGh5eLBo+dpFx0zJgxdx8KW8cpJMdjjz0W/6MnXAqF0FTdlClTIAyuCkktF9Xsktc/xUaquGhwHYbhosHVeCwD/esKu2Nol3GuVnxZ75kU8TQqa0JJZTWyhItqzdOOrB13LD+otiHoXKpSduzYEXekFRSUyy+//DIDm6+OTdBXUAyywATbat+3b585D2DhwoUiD3bIGRsPP/xwzDr+Kyu4qBiCcew0wMCiV0g9PP/880rMNi4ad05kqV27dseOHZH1Op/DhSzioitWrDA7yMeOHasj7CU4wnPR4Ibz5hPcCvp70KBB8IH27dv36NHDNYoNtAUIQkj7uoLju6DYM6+//ror3egSV0VluFcH1Gc8Q1yU/2HRFMYbq0Ofk0VclIa48sorVb1KSdpqLi6qweiNVUYdUttz586NOauIrtXstWvXypMlDBdlvHDp2nSqdVEzBtPLRTUfb3vBCVWrViVdsUl8uSimTCxtQTVpXR3JPrp02hw5cphQagbi4TD8ihUrxtK8kZMiKRedNWtW7NCV/wxwUcWZs6NYGQRz0T179rds+WfgzZRw0Vq1KO0Tkya5z5aYN2/tmjV/SI8wXPSxxxChT8yc+We4o6zmos88M7dv309dib/88kcQhO7dGcVPDBx4yOrl668vIbFVqzdDZuILKoRMFixwn4T04IMP0pTDhg1L9GDRokVjads7XUBaNmnSxHvEseS2jolyLW8qVJIcWBDmroMNFW6tT58+/O1yzLEzP1xcNOnYyYyPbtzZqZQvX74SJUrMmDFDh9zIWaxBgwZoZ5ehklouKgWBqPE2tNHjKeGiSesw8tHNMKBROrLFbqOtW7eKdpmW3bBhg3ZTxp0tUXaIe5rSdXOWIku4KIrT5aAbd/Ztk4h1oksGttyR5WInn95PP/2UGtyfhqRHXB7jGDduXCxtNUAQPZMHFz3JnuDXFrJEU/5yCDGURkbMP//5z0SvzgAXlbhHYNne1++//75m/jBqbS4qHXPBBReYO7OIi3777bd2bA9fFClSxMVFtQ5j4o6CSZOwcmLSGUJSLjpx4kT7mG8ddqIUaBV/2/F74gls6OCG8+YT3Apxh8W5SIgv4ISnnXYayjIgOLNAm6qu7B1Eo0ePNsuerorKcK8OqM94RveLitjQhWxx3L17d5145stFeTbM9mxFZfRyUYRe+/btY07URKNFkraaYl0Yj9mdO3dCoWXJmfspLV1927Zte/fuPfXUU/m1a9eu5tcdO3a0bNlSn6nIky5fWRcXRZ5D1Bkato+0XNyNx3t6uSgFk0Fj+/jR0woVKmS6hy8X7dWrV/78+eW0lrSujmQuqiBMV1xxhaZoBXqyqXaJWZAoEN327dsxVTWfm5SLIihctqC25prDmcaMGRPz7J/3AlFgC0ODunVHB3DRDh3eee65P08HSQkX7dVrDjcULfr099//z4d55crtTZr8GQpVoYzGjvWfXxMuuGCgzUV5nMvKlf/nYuDLRdevZ8z9L7yFDhFIepTuoEHz+/Rxk7dly7aJWMKf8+Tp1rDhGPvX1q3f4u1LlmwJmYkvevf+pGrVYWZbrIHikwWIL0WX9Yb5QG60aNHCu4RC/9GsEGol5jm8tGzZsvScRFuHtHk1w/tFDRfVloQ6deqYG4YPHx471Bk+A1w06djJJBcFTZs25X6qyMhDKH3u3LnLlSvnujM8F/Ud0dqMauKf85T2bbrMxYceeggrXX+nhIsmrcOIi2YYYliuuaFdu3a5zsv85ptvFFM27vjS20F8tGTqe/RJViD1XBRira91LZRrwRfMnz9fbsofpp2jit790A/BBzFFwMCKObvmZsyYQZV26tRJ4mDy5MloBYTCSSedZKITU8n8ZAKmu6CVB6QzemjChAlyiqtevTrcz7XvWVCUOdvKkaeWLfHnzZtHSpUqVXSJrtasKoVExr300kvYl1hdEmc62xNmtWTJEgqPtYpxiT3Nd4lo1axZkxtsbVeiRIlY2oaK+B8Hoy+JWae8xNMCPNqrl1JCthMgcg0+cO+990KZhg0bhsrkFfY6GJpSoVNd4XD09meeeQa+x7dQFWJc1JgMenGqJk2a+FZ43OFONpHDcDzxxBMlI6gTDP2CBQtiXiMRJFB0usOiRYvsTIIbzptPcCvwsQUKFID70ZewG0aMGEGeDFhfD1sdh0OVJvpAAbOYRok5MVdoVuoZRoRNY25wVVSGe3VAfYIBAwbEDo2QrBPYzeExgg78MPmrC8WcIJBPPfUUBJIebvZTKQcesZmqAswE7MYU1OEh80bvkhvNge2SI0eOZs2a2f0tuNXiacvj/ERt67AcRSwUqx84cCAdFRvIzGprIGh0PPnkk/A0hp6Z6NHsAJwN+gqZ1/YbHcpn78LVJxiOB4vmXXbU3DAD0IVp06Yx3BiVZoIWOn3GGWcYE0fWCd3DHDKE7sRcM6dfJq0r33F0WKCotrbTIypPB9XyyQil55577oYbbjChyIWXX345T548dBLS7fDU8B8GLK1mHK7ka2e3iN5o+rxMcEQZTY9txxs1SUErSNJqhQTOgEhEevi6coH777+f27xx78uXZ9A9cdFFg+0BAmebN2+tDmhZuvTP+YLmzSdzaahp/A8fxU9Jufvut0wKv5JillK92LNnf/Hiz3DPKaf0btNmyvDhC++/f/p55/U31PSppz5WWN3ffz/46quLfY/ovOqq4Qqcu2LFT9OmrWjRgoI9Dr/9+uvNOpbznXdWcEP16i+ZR779dmvOnE8UK/b0vn1/dlr5NVSsWDEgRsOIEQuPO67H1VePtP/93/8NyZ+/+4YNf+4F7d79o1y5/p9ZwKRIBQr0uO++aeEz+eyzdddd9wq3mXNZv/lmS7ly/e0TUw0gWsGHkE+dOtVXuEFiIQxXHwq6jc2aSKFXG7EmE+Ktt96KJ0AYLqotrCg4u4Mpjq4Z4NyDEmS8oGiWL1+OItDJbaVLl6bba8FD4eLtSVhpJTs6tLZsIFt0mXTsUADXrBmUMpaeONhimHYZROld+y3jaefH2KewCF4J4zui5bv04osvoozkZKTgkTHHqQopRKVhVJjISUDhDIz8of41+xl8+IWLiyatQ2/542mhE80x2hF8oXi5ZpVCoJkw5+R5i8GsHaFm4VBbSQFd18Q3yrbNt6nnotos+qFfFFwTpknAmJCNS/eNuGjGIO4Rc6bSIUVDhw6NOcdtIeJltTNuoVjYKMiURLHa4850u4TL8ccfj9mKISiuheXt3WKKQJQ9xyP9+vXbs2cPdv+ll14ac07569GjBz0bRiF9TAoSRzILvlS5cmUVOGfOnHfddZcJwkGP11Hs3I8hvmvXLk3BlipVijGDktCh9tWqVXvvvfe2bt2qGbWYs5MEeYpiM7sEO3bsyCPIWRWAF/E4L8Kq1vwf5IFi672Ya3LmtAFrkijku+T9COrWrYuwNrYF0l+8BT0HX0JoUsLrrrsOUU6vRnbL2wQ1CSvwFdBoWfQ3tib1SZ3DKu1otFocozbatGmDWNG6MaAChwwZYshh0oaz89EjAa0A2rVrF/OgfPnyttUr8FH0tDBHIdNe1157rbZ3UktwGK3bIBl9KypjvTpRfVIPNLcMFOoKRUgmmAXqYDFnSfabb75BHJlvb9iwodnBMn36dE3W6nGokeweMtdRq4CsdNRb/A+/xOt8zTUDuisvMr2OPzDRChcuTMNhE3Tr1s1X7gW3Gr9qJrtkyZLG96R3794iNjFnjsZeNI47myT1SMxxhkdFmZ/oXQpWjBFAf161ahVDOH/+/OoJdgBehg91Tnv17NmT/ym8cWYJOQC9oOYvuugi5AlP0TS33nqrvUhoZsoZ+NT/3XffTVFdtZ2orgLGUfaDXmr6D6a8mcBeunSpKl99nor1FhJNipCkNzKmkJDkU6VKFWQyzWSmNsaPHw8T0Ih79NFH6fPICvNGKnbDhg0kKlwz+dBvkdvasstgNCuxiFyVpHv37om+hQFONzYnBjtft0QOuvoHX4Ilnn76M4UL9zSJ2vQIUezRY/bxx/PeJ84447l+/T6D0b3++pJSpZ4npUiRXs8/P2///gNjxnzN/aQUKtQzYMVv7dpfHDL5uF5Rv/6r9gEn69btPPXUPlo7ffdd/9U/ePJJJ/XiHugcVPa33w7A7rg855wXVq7cPmjQ/AoV/lg4hXw+8sj74tL8D2OEi+7d+6d2kBcPsIeVjTffXKZwuN5/DRocshA6dOgC6PQzz8wdMODz888f0K3bR4ZVhsnkgw++z5PnjxhIZcq80LHjtHbtpj777Nz//MdnG5SCYJvjNBOBgUN3tVM0E+ELe5gj8xmtiGXkNh0SdR/MM5NyUdhLvXr19KLbb78duYqkatu2rVKwB8ySDlpGE8oIMVQD0j5fvnz169dHuGFp9O/f/+STT445U8naY485IWd4lDsyDa308ccfS7DHnDOfURbBY2fevHlavos5R1hhHkACJQ9jTjhcM0kaDCTznDlz7DpEwrueRRWef/75yrlDhw5m6TKRhPGOaM0Axpw1W7MsNmjQINHLmBMa3RwUzw1yro45jmCffvopKQo0FXPsMaOAvHBx0eA69JYfZqW9ITFnqpSOFKYOj03AJ81qn419+/bpuE0BpWBchFA0cl81P61d6w61nXXIwvNFfYEpv337drpgdF5LqoAKsacufvjhB0MPZPFv2rQJ6ZDUX4inkNHG7qGBwrgaZgDYhYsXL/aWBx5FAWzq+91339n+61mB119/HVWEDkPZIP7GjRv30ksvoc+8U4xe8AkMXRWYcqb3LCa1DrY73AMD1GtxYjqH2YWftOF88/FtBVgWvHrmzJlkyP9wvzFjxgwePBi1bc+JCvyKQRziQ/9XziVLloQc+Bno1UnrMzNA3dIbw+TJPbY3cmqRaOzEHfcbs5PWgNrAbArQKFB9X8cHBDV9IGnkbQFWk3JZwWiiAN7hb/vo0iiJNpLFA+vqyAcq0vfzbch0mDFjBrIrw12OHsJgseUDVWr2XestlMQc45wIQ4cOhQxnz86ipNi589evvtpkO80aQMOgjsHl3LNn/9dfb4aF6pKbly3bZhigLzZu3OUieIgvzGXXTqWMgVcvXLgRkrxrV0aspp9/3jtr1urZs3/cvDlo3vDee++1d0YkAmOqcOHCvkIjDBi/kCsyCSlbUgXkCYNF2of/EwVxTBeSjp3MwzsFbIfPzRh8R/TWrVt9ZSkKgvRUjWtxUTuoXjbUYQQvqOFt27bt2LHDq2LQmIl+ylJkNxeNEOHIwaRJk8qWLev7k+3MeeygQ4cOvhtckVze+CW1a9d2xe6PECGr4btfNMKRgGbNmrlOwzqWgWxMGkT9yAGlLV++fMjFupEjR7r8xiNECIOePXsivRVtIUIEGxEXjXDsonLlyiVKlPB6mc6YMWPIkCGHpUiHEbLyGzRo4P2pV69e2ky4adOm99577+eff37llVdq1qyZ7WWMcKwj4qJHLA4cONC0adOPP/74cBfk8OOTTz5p1arVX+VEgNWrV9euXTtdC27POci6IkU4mmBWdx955JHjjjvOhGOIEMEg4qIRjl107txZu0Q6der00ksvDR8+/Mknn6xfv76Jg3Ks4fLLL9dOjJ49e44aNQpC/vDDD1933XXTpv0ZLaNu3brarZE3b16vR2iECFkNhcsuVqzY4S5IBB8cPHiwT58+ER39C3mGr1mzBoaQAZ/VN954I1Ew5wgRDLp16xZzDgpCOFx11VV21NwIEQwiLhrhmMYrr7xy9dVXlyhR4swzz6xXr17Xrl2Dg5If3dizZw8stHLlyieffHL58uUbNWoEHbU39kydOrVcuXKVKlXyniMXIUJWY/r06XXq1DnRQZMmTRKdlhwhQoQIEY4ELFq0qG7duoo2dwy6m0UIiYiLRogQIUKECBEiRIgQIUKE7EbERSNEiBAhQoQIESJEiBAhQnYj4qIRIkSIECFChAgRIkSIECG7EXHRCBEiRIgQIUKECBEiRIiQ3Yi4aIQIESJEiBAhQoQIESJEyG5EXDRChAgRIkSIECFChAgRImQ3Ii4aIUKECBEiRIgQIUKECBGyGxEXjZAy7N+/f/r06atWrTrcBfFHSor3+++/v/fee99++22qSpUxjB8//nAdKL927drXX3/9sLw6EY7AIv2lsW/fvsmTJ2/YsCGFeSZto127dr322mt79uzR5d69e4cOHfr999+nsAxHGn777be333575cqV2fzegwcPfvrppx988EFqs+VzZs+e/dxzzyGdtm3bltrM04tff/31P4eCXu17JyLdvi042wMHDtg3U5P2r3TXKVOmfPXVV9zG5c8//7x69eqQ5XH9av/EWJgzZ8677767detWpXzxxRfm1yNW4XqxePHi4cOHU+EB96Cm33nnne+++y7bSpVF2LJly+DBg9M1EKiZWbNmffbZZ1lXqowhVQXLQJ1EOEYQcdEIKcB///vfTp06nXDCCbFYDOvqcBfHjZQUD2OiY8eOyuTwMp8ff/yRMhQsWNBlCWU10EaXXXYZrz733HOz870BOAKL9JcG1nOLFi3y5ctHlabKJEraRljwN998c+7cubln8+bNSnz55Ze5rFu3bkrKcKSBer7zzjsLFCiQzQITIda1a9eTTjqJ9959990pzJkvqlOnzscff/zvf/+bzIsVK8a7Uph/evHGG2/ccsstsTQ0adLktdde873zm2++eeyxx04//XTdOWTIkIBsW7VqpduKFy9OTW7cuFHpP/30U4MGDZDJvJTOXLp06auuuqpKlSowc90wYcKE888/35SH29566y2TLZK8f//+DBB+Klq0KOURmwVjx46lMi+55JLmzZtffvnlZ599Ns+ecsop5lk4aocOHQ5vbYdEhQoV+EDouu+v1GHr1q2PO+447pk4cWI2ly3laN++PR9y3333hbl5zZo1NCL9h0eefvrprC5beKS2YOmqkwjHFCIuevQj6xiLK2fp/iOQiwopKd5NN9102Lko1Lply5Y9evTI/ldjt2UF8ctMF01vkd57771rHMBzvv7664A7f/vtN2MRpgT79+8nz4AbXnjhhWvSQCun8NXpAoZvCrloPFwbYYLbXHTt2rUNGzZ88803U1WGIxBVq1Y9LAKzb9++Keeif//736+//nr9PWDAgMaNG6cw8wyjYsWKfCkULumd48ePF0uERiYSR9u2bdM0jVcFwMNPPPFEswrKMMeCd5ndu3fvVnnAjBkzvPnfc889JUqU+PHHH00K3D5nzpxY8Cbl008/Peuss8hh165dJvGLL76AAB/5dPSll15q1KgRnDPgnpo1a/5Fuair28ydO/eGG26YP39++ByaN29+pHFRIcMFy3ydRDhGEHHRoxzDhg2bN29eFmXerFkz+xLj5kjmoikp3r333nvYuehhxC+//JJyLprJLpreImEPNW3adMGCBYsWLYIc+t7Tr1+/iy+++JRTTjn99NMrVar04osv7tix46GHHtKvsEQMpv+zwD3BHo+TJk268MILixUrVrJkyQoVKmBp9e/ff+nSpa7btmzZssDBSSedlFoanC7AK1LLRcO0EfVjc9FjAf/4xz8Oi8BEfKWWi27YsCFHjhzIxlRlmCrUq1dPi5BJ70QEyecFjBs3zveebt26VatWTffMmTPHpC9btoyU+vXru+5v2bKl69Vr1qwpVKiQ6LHXv5cCQDXtRM2fLly40E787rvvjjvuOF5qJ/bq1atFixZJP/PIB0bFX5GLrlq1iu6RyUyefPLJI5OLZqxgv/76a6tWrbKoSBGOMqSYiy5IAM3hYWe40r/55hs9iHm3cuVKrJ8PP/wQrYBczmb/w6MSX375Zb58+T755JOsyHzQoEE5c+a0UyIuetQj5Vw08100A1z0X//6V6JfUZ916tSBjC1fvlwpP/74Y+vWrStWrAjnNLdt2rQJ42Pk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UQG5cuUyfVKKjBY398iv1R6eFMmlFLzIABflY8V77ULCqTTlkYiLxh0Lp0ePHlodAohoV8whFxCz3IbaqlSpUvBgh3+aRTDuv//++33FCJlokCbK5/333485K7d2osb+P//5T1369jfeSKJr5VblN2vdjFyG3vHHH2+0Et0S8mw/IoVruCjty+cMHDjQvgeBZivl5s2boyMOWIB0ccPw4cP5VeTQZvKJloUFRa62d8JDlUmh72k5F3pJBZp+qJFCoi5hRzkcmHlzwctF42mcyuZdwZnHw/no+jZQhmtp6tSp/IQwsXPD0iDxjDPOMN3SWzDNFtlqRV00gIv61gkWApak6xsxIbjNyByZf/bkpuYcEVP2U8Hn1h6b2LFjx6xZs5DkpnJETRnLmArbt2/nJ27QrDRjQWuka9asgabRlL5+kVmErOKiW7Zs4avs7WeMXq128uWYvPrbdiuKOyYLVaMHo44VBmbqiOqaMGGCpv3MVkmXoU/f4hL6ep0H4p/33XcfNyDFwhyDnoiL2rvgJMKMwffrr79yaa/cxtMMSq8PmHYSaokjKRdduXKlS/BJPdhRH5IWzwXZ34MHD7YT7f2i4ntepyBELelGxXrJwNVXXx07dD1WLWXPeZuBM3fu3OrVq/Or2fUXd4zLYC4aPqKPeRGGrAw+c4TAeeedZwhGomzN40g9VJrNM32/fdeuXehyeo4GuJeLYkZDS7xdVPeEKVIwArgojesNExKAkFw07szuP/vsszfccAOdH77UrVu34IMNwnPR4OqKZ6j7eWMXURg592I+JhUjSduoTZs2NlsWXPtFtcjj5aK8xaQoZowdg6d48eKkGI872UP2PJc8MDHHba/vwwXf2EXQHhL79eunSzWWPTO7evXqmDPN5K1/02RmVO7du3fkyJHaj2BmAGUEN23alEe8RBRocqFAgQIYymG8k3y5KD3Q1V7xNKH64IMPunKQl++gQYN06eWimlu0mYa+ItiRIQNcNO64BYr1aY8DdpuxywO4qEDriN3FnFlXbW/2xf79+3VCTDB9ElD08HC5J4AGDRr4nvmknS+JtoyKkzC67URVIypGl97+FndGNImubYRff/11zDkN1aRoq6fxJe7evbu9BBpPa0STCAHm0rV70LVftGTJkrB6b1cXUcGqVPRjyFiYsGfy87f7VTxNmRrnJjN2+MCbb745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n3/+mejnoIMO0mWW9D332Lp1a9myZX11gcPkiYuCH374YXuw0rCgRo0a2VqcM2SpBfJpug899NBCEdSbb77Z6E4BotAdWc4K8P7779NxS5cu5e9FixbVrVt3p58aDVXeoC165plnMuaiYN26dY6L7rJwXNTh/2Hs2LGvvPJK2sdwnN27dzeXv/322/YQ5UTj+OOPL3CXH7O50uKPP/4gMsh/PjkAHiIHXDQU9913Hz1IW2XvFTtQR+xqePnll5s3b26n+Lho0uu+ww47TH9nQ98LC5rQs+ty77335pWL/v3339u/lc4qstECX3zxxaOPPpqfHIKdu+NiyJAh06dPL8QCbNq0qW3btrl519VXX+34UjLMFr399tv54aJg3333dW27a6KAuegnKbB+/XrurlixwpceHE9avny5bq1atapgy+aQCrjVEiVKEPNFP4a5r1q16m233WZSdk0uGrO54uCGG26gePnPJwcoRC5as2bNokWLZvUVO1BH7GqYMmUKIY6dEuSioGPHjvrDcVEfHBct8BYgnqlSpUo+Zxd3Gi766aef7rHHHu+//34hluGqq646++yzc/Ouo48+2vGlpOOi2yt++umnUBb2v//9Tw+sXLny448/RmE/+OADKNjmzZuVHk3fso2C5KJbt259LwV+/fXXpLeewZc+c+ZMO4c///xz2rRpuvXjjz8WYNl2Ynz22Wfz5s1LejR+xIgRqY51ofFffPHFYcOGLViwgJ4y6QioVrU98sgjH330USrXCO08//zzeezKK6/kMb3R5qK///77O++889xzz1Ee32/Xrl1Ltya9LQGDBg1CE+xs33333WeeeWbq1Km//PKLSV+6dOlHHszOeMqvFL3aBj+k1thE7m7ZssV318Sm//zzz9y5c5999lnKGdGeBqtXrx43bhyNRhlo2+jm+uuvv15//fWkp+e8Ar5q8pk+fTrNQj721n+64O677yafI444QvWy5/144wsvvDBmzJhly5YFC8ZLhw8fPnLkSPstSe80hY8saEeQjvwR0lYZwzTUgzFbBqFclOeRKFret6pW+OqrrygnpP27776zOz361ooVK2bMmKG/MQIU+8ADDyxWrJipxaxZs1577TUE6fvvv/e9cd26dQhS//79eSCoBaGljegIRBoiFKxXKlUSYupjENGNmYzsnVR15yeq1OLFi5VimtGn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5557ypYtSydWrly5W7dublfhzoG///67SZMm5cuXb926tTtxZieD46IODg4ODg4ODg4ODg4OuYbjog4ODg4ODg4ODg4ODg65huOiDg4ODg4ODg4ODg4ODrmG46IODg4ODg4ODg4ODg4OuYbjog4ODg4ODg4ODg4ODg65huOiDg4ODg4ODg4ODg4ODrmG46IODg4ODg4ODg4ODg4OuYbjog4OWceCBQsGDRr0119/RT82Z86cLH0fdeXKlf3791+9enU2Mt+x8N13340dOzb6mWXLlg0ePDh7ZUAS3n77baQie68oXMQU+Pxgy5Ytzz///Oeff569V+QMn376aapbv/7667Rp0yZNmlQg30hctGjRBx98EEzfvHnzrFmzXn/9dSQ//2/JD5YvX07P/vHHHxtjIDqrrVu3zpw5k3pFPzZ37tw33ngjn8XesuXvjRv/NP+WLPlt/vyfk173rV27Np+Z5wC///47gvHUU0/16tVr6tSpNF2WXkTPPvvss/ZnsXMJ+vrdd9/NXv5BEf3777/zmsP3338feousfJmjtsHHsLpxdCevBXNwyCocF3VwyDqqVq2aSCReeeWVVA/06NGjbNmyPNO2bdtsFKBdu3Zkfscdd2Qj8x0FL7/88rHHHks7VK9ePdUzI0aMOPXUU3nmP//5T5aKcc899+y77768AiqVpVcUOtIKfP4xfvx4XnHiiSdm7xU5wOTJk2vUqHH88ccHb8EHOnfuXLt27aFDh44cOfL8888/55xzfvrpp4zftW7duooVK15++eW+dPLfZ599Ettw7bXX/vbbbxm/JT8YO3Zsly5d/vnnnzp16qgwqGGpUqX23HNP/i5SpAh/77333qaoP/zwQ6qssKilS5fmmQcffDD0AUJ2bh188MGqcj5LfuqpAxOJ/zP//vOf7qtXb0p61KJ169YzZszIZ/5ZxcKFC2nwiRMnLl68uEmTJjRIy5Yts/QuDCz5161bN0v5R7z38MMPz56HBevXr+/Zs+cxxxwj4dxrr71wNwceeCDKhT2kSadMmZI2kz59+tSvXz/01qJFi2677TbpAjjiiCMqVKiAAJ9++umtWrX6+OOP9dgDDzygB3bbbbf99ttPvgbwd8mSJVEiXb7wwgsFWXkHh/zBcdGdATjvwi6CQxRgHVdcccUvv/wS8YxcSJY8JcFQgwYN5syZk9cfbv+i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ByovG452YyF11/yRMzpawPOiq/8NkU9MklRaXNx+wBAP9JAnEXH77va/V61w0b9/f4IYrMyVV17ZrVs37cFAni666KILL7wQyUOBiS8JX9T+CBwsq3z58vykZs2ahGJ4l6uvvrpMmTJE5LA1kzNiWrVq1ccff5z+euCBB4jLmzZtqs4i///+9786FoLceDUhQokSJbgk3S4e9qJOnTrt2rWjZ3GllOSUU04x5AS/JZvbqlUrbNmxxx7L3d13332vvfbCBlHyypUrU0gsLIlmrmb69Ok4Tn5FdGUiXWrRpUuXfffdN3Q/JIlNmjTZc889eWD+/Plly5YVgQGdOnVKel6zX79+Z511liI/fJXu4keTXrxLFc477zyCM8wuj5GDWcdIUfEf2gdizgbEQN98882lSpUi1qfRevbsqaNcfPNg1Jrf4lxpZBpBrWFzUfTl0ksvpUh0BI1MN9lnAPbo0eP888+ndvi8WrVqUcJUckLIeO655xYpUsSEXEgOzkyBGr4NkTjooIO4PPXUU+Uk6OX7779fu1Bwb0iXDFnSOwQCiSLO69q1K71To0YNOQaKccstt9A79CCKr246+OCD8eu1a9fm7dSFTi9evHjRokU19CuJJXy57777VB6aQkcHAWxCRCOkKmGE/CctLtq3b19tjdOiKd+2wyAXje6LIHD8PH/HHXfg0REA3tKsWTPD28VFoYtXXXXVwR64rFatmj38cc8999AmxMq4CvQIEVIwEd1cqX4lkD9Ketlll9EyND49RVMofAw1JhEVT1UMmj1U4DERyHbv3r0f9XDSSSeJgxl5S9VrOrGDhxHRbh5++eUXAl8MF+WHntnNHm1z0op97hHBRamjRLRz586YkdNPP71BgwahgwvRoDtoiqQnk4nAftEgLr74YjTCF4Lgi1G3o446ihxgPjS+saK0sEQIitK4cWN+S7MTx++33356Bn2PmIQh0MQURHPsVFyUsLVu3brUCOPz4osv8kb7eDZx0XvvvRe5SmwDTW0HskEuipe8/fbbkVWpJ3fRqYiyXX31mMMPfyKR6CZGus8+PV54IXy2FnlLuyLDB3SNfsc9Uc569erBG+15bGzLMcccg1Tz2J133om04NFEtmlVanHAAQdQfvriggsuwNfQNcavJb0VoVhOUmBHd3kgE3pWDaU+5X/svHwc/auz38iH8qCw9Cy6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FC9YZocsYe3atS+++OK6detiPr969eoXXnghP2/84YcfeGN+ctiZMHv27JkzZxZghjNmzBgzZkwBZrhLYfny5Qjnk08+OXfu3MIuS1x89913L7/8cmGXYjvCxo0bn3nmmaVLlxZ2QQoZCxcufPXVV7OU+aZNmzamw5YtW/L/ItebOyUcF90lALdp3Ljxp59+evHFFycSiXvvvde+S6Bft27dhIe///67sAq5E2DIkCFVqlShGc8444y8/ja6jwoEBP3kvOeee/71119c8v8DDzxw8MEHk3j99debx6AWpNSrV6/AC5BXjBgxolKlShTmtttuK+yy7Pz48MMPGzZsuNtuu9HgiEra54lssBtFihT5z3/+k9kb6d/q1avzuooVK2aWw86EoUOHHnroobRGt27dCjDbgw46iDy//fbbAsxzF8HkyZNvuOGGefPm1ahRgzZEXAu7RGkwc+ZMXA9FPfvsswu7LNsRoC60SdOmTQu7IIWGwYMHH3744TTCRRddlKVXJLahRIkSpUqVkh/Za6+99t9//6JFi+pW27Zt8/8i15s7JRwX3fmxfv36vffee+TIkUlvSKlBgwYTJkzwPfPnn39iNXYRLvrPP/+kTckYBPQZcNE4fZR/bN26tXnz5r5It1+/fj4uunTp0kaNGmU2tVvgGDBgwPbPRQtKfgpQDjMDEiLqEoeLgnXr1uWHiya9RQS7OBe1V0D06dMn/1zUJ0W9e/eGUOVTtApcMuOs+8jS2pCYWLVqFYKtBSPLly8/77zzZs+enYP35rOpP/30U8dFffjuu+8aNmz41ltv+dKzGglkhuwV6e23384eF920aROZd+nShehFKUceeSQpTz/9tC6//PLL6tWr33jjjfl/V6redNih4bjozo9nn30Wo/DRRx9FP3bIIYfsClwUoxkcnLOZWD7x7bffZsBFY/ZRNvDGG2/4uOh2hZdeemn756IF1XrbQy+ceuqp8bko2HffffPDRf/4449dmYs+8cQTixYtMpdakpAfLjpnzhyMSUEULYt5+mqd8TNZxeOPP577+eTffvvtzjvvzE8OWvziuGhaBKU6/42fT2S1SJ9//nn2uOgvv/xy0kkn2Sk+Lpr0anfVVVdl4+0OOwEKmIt+kgLr16/n7ooVK3zpqIf57YYNGxYuXDh9+vQZM2Z88cUXWkbokH/ccsstjosaXHnl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F/Xw8PDw8PDw8PDw8PCoaHgu6uHh4eHh4eHh4eHh4VHR8FzUw8PDw8PDw8PDw8PDo6LhuaiHh4eHh4eHh4eHh4dHRcNz0c0US5cuHT16tJvy+OOPz5w5s/An/Pzzz0888cT777+fnW3BggXTpk0rSxE3LSxevPihhx6yj19++eWIESO++uqr9VikTR4rV66cMmXKsmXLKuyN8W6VBvrFqFGjfvnll/Iu0oaPDz/8kGbKyLB69er777//v//9r5uI6P75z3++/PLL2dk2DaxZs+aVV16ZOnUqVnr+/Pm//voriV9//fVHH32kDN9+++2YMWPKtQwTJkygDMV95qpVq+65554lS5YU97E//fQTvumDDz4o7mM3VciVf/LJJ+uxDOveZOWkS0XHjz/+SEd274IuA2bPnj158uRiFcnDY73Dc9HNDuPHjz/ggANyudyWW25piZAiUrbYYosVK1bkfQJxz5lnnlmjRg1+gv9IzEOkeP311zdq1Ig8f/jDH4pW+o0Qjz766D777IMc9txzT0u84IILSOnXr996LNgmjJdeeunEE0+sXLkyQnbpSvkhsVtlYK+99iIz1KK8C7Yh47HHHqNTIIf99tsvIxuhG3lat26tjwTNffv2rVmzJok333xzWrZNAxjSwYMHb7vttnXq1OncuXPv3r3btm1bu3bto48+eo899hg1atTSpUtPPvlkTDd1L79ivPPOOzy/YcOGxX0s5IHHnnrqqcV6IOT8vPPOq169eoZv8jD89ttvl112mbrSv//97/VShmI1WdF1qehQ4KSavvHGG+vyqN/97nc8xI+2eGwy8Fx0cwTBXDxoPv/880tFjQ4++OC8zmPs2LEbPhfVJEO54sUXX4xw0dmzZx9//PHz5s0r71cXiCIKoQLkWSCaNm1aYVw0SOlWabj//vu7dev29ddfl/YtG45401CqEj7zzDN5ueiXX3554oknYkzcxF69ekW4aGK20pZng8LChQvF1W+44QY3/ZVXXmnevDnpd955ZxAyiu22224duWi2lNasWdOzZ89hw4atyyvi+PDDD0844YRnn322uI895phjisVFke26P2RDQ6St//jHP65HLiqUockitSgnXSo62rRps+5cdMiQIRjAjdeyeXhE4LnoZootttiiwKA5DX/+85/zOo+XXnppw+eiffr0WblyZbm+4uOPP45w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/vhj+GrTpk1JX4/l3JSwcuVKHHmDBg222WabnXbaacCAAZFbWzZtzJw5c6+99tpnn30ST4v12PDx4YcfnnvuuXvssUe9evUOPPDA3r17+6WtHh55MWbMmCOOOALLv8suu+BqBw8eXMjNeRsaNo1aeMThuaiHh4eHh4eHh4eHh4dHRcNzUQ8PDw8PDw8PDw8PD4+KhueiHh4eHh4eHh4eHh4eHhUNz0U9PDw8PDw8PDw8PDw8Khqei3p4eHh4eHh4eHh4eHhUNDwX9fDw8PDw8PDw8PDw8KhoeC7q4eHh4eHh4eHh4eHhUdHwXNTDo8hYtWrVo48++tFHH63vgqwTli5devfdd//vf/9bXwV45513nnjiialTp86ePfvnn3/Om/+zzz575plnJk+e/Pzzz3/77bfxDD/88MOqtbF69epyKPgGDYQwa9asO+64Y/Dgwc8999z6Ls46Yb2raNHx448/ovBffvnleiwD3Y1OVPHv/e2339DMDeq2W0zQjBkzKvKNH3/88b333ksnrciXlgeWLFkycuRI6vLmm29Snccee+yrr75a34XKwoQJE1555ZWiP/bll19+4YUXiv7YTQyltXsffPDBww8/XK5F8qhgeC7q4VE0LF68+PTTT69SpUoul9vYA/2//OUv1ALGUvGvhoI2bdp09913P/vsswcMGNCxY8datWqde+65y5cvT8z/9ttvH3roob/73e9OPvnka6+9tnv37ltvvXWnTp0Ig9xs99133x/+8IdciMqVK++xxx477rhjzZo1eRc/HDduXCGMd6PGG2+8cdRRR02bNg1F7dKlC3Lo16/f+i5U2bEeVbTo+Pbbb88888zq1atTI5ppPZaEfkQZiPYq8qU33njj9ttvz3v//ve/V+R70wB32nPPPSnPH//4x4p875///GdeOmrUqIp8adGBAT/yyCP/+9//nnbaabkS8HF9lysV77zzDiVs2LBhsR6IKxk4cKBU+pJLLinWYzc9lNbu4ab32WcfMu+3334VUDyPCoPnopsCfv311/VdhI0McYkVUYa///3vNwEu+vzzzxOHLVq0qCJf+uOPP/bu3btSpUpXXnml2yIvvfQSvJEoef78+ZGf3HnnndWqVTv22GPdudAlS5bATiGcuC438+rVq2vUqEHrECgoZc2aNXPmzOnWrRsvrV+//tSpU8utcusZS5cupe5UVh+Jlo477rgLL7ywYt5eHjZqvahouaJNmzbrnYsOGTKkV69eFe9T+vfvX3Quui61mDFjRsVz0aeeeqpLly4ff/xxcR/722+/FfeBGVi5cuXWW2/90EMPBaF17du3LxyvuFy06MpJOXv27Dls2LDiPvbWW28tFhfdtGO8Utm9//znP56LbnrwXHSjx8iRIy2+9CgEcYktXLjwtttuK9bzTznllE2Ai64X9OvXD9ERvsS/euWVV/gKuvjdd99Z4uOPP07ivvvuSzARyb9ixQrFQJGVVw0aNCDxrrvuiuSfPn26RmfjX20auOiii7bZZpv19fa//OUv6+vVGxFgPuudi64vwEKLy0XnzZt33333lfnntELFc9HyABSrIsdr7r77buS2YMECS5FWF4uL/t///V///v2L8qjyxmOPPVYULrqOmrzho1R2DwXwXHTTQ5G56H9SsHLlSr794osvIulmnn799dePP/547ty5//rXv+AJH3zwQTy49Ijj9ddfr1at2ksvvbS+C7LRIC6x//3vf82aNbv++uuL9QrPRcsGXNEWW2xRuXLltLW4xx13HIK99NJL9fH777/faaedSHnkkUcS89922218u//++7uJO+64YxrhHDlyJF/VqFFj8eLF61aVDRF77rlno0aN1surR4wYQcuul1dvXPBctFhc9Ntvv8U4rMu40qbBRV9++eUqVapU5PrYs846C7m5JrS4XBQvcOKJJxblUeWNonDRddfkDR+eixYRn332WSILe+edd5SB+OrVV1/997//PW/evMQlGL/99httYfkrBsXkolTgXynQ8rlFixZF0m166q233lLKCy+8oH82T39cKiBPzfzcd999uJxPP/3Uvvrxxx+RLekzZszI3hGOh3g5xNKlS4Nw5d7LJfj8888t28qVKzGsevLTTz89ZswY5XdBI44dO/aJJ55YtmxZ/KV0hlGjRk2bNu3rr7+OFyPt2zVr1sycOXPFihVBODMGWyhEMSgtjyICfuqpp9yjTeISw64dddRRpJxzzjmkUAXLvGTJkokTJ957770vvvhi4sgItPb+++//xz/+ERGFy0UpycsO7PwGZDtp0qTJkye//fbbX3zxRUZdaBEEHoSbUam+28offvjhhAkTxo8fn8idENqTTz6JD1NJvvnmG+0Bo14qjA2Wz58/Xynvvvuu+wTehbVy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mDFj0vBUSjBv3rwk6FlODw8nUSGjR482c1En2cIeljj//PMtFz1o8eeff6JL089FP/jgg5YtW65duzbN300CF110EQKcVS46cODAWrVqYewwYUK8wcMPP6xugGwULVr0nnvukUsaolq1aq1atYL5pDL3SeGLL75Igot6dPXzzz+Pk+Oh36lF9q3DV199JU1TpkwZmiDwnrfeekvuKVy4sF6c66+/nsSTTjop8iuQVXnDCy+8EHZP3bp15Z5nnnkmiYJYHISwXPSQx+TJk9VU2OEB1FzHjh31FIzQkcZFUwU8J52LvvTSS7nCRX/55ZckuKhfEo4QyCBClujZwakHoFWRXDSJwh6uEEfcctGDFscff3z6ueihgn79+rVv3z6rXHT79u0NGjT4448/VMrw4cN5Sf78+dXMZ5s2bUjZunWrumfEiBGkzJgxI1WZTxq//vprVrno559/nqVR5uxj165disknjZ07dxYoUIB2MThjF1100dlnn80NJ554op7erVs3Es8777zIr3Tp0qVIkSLcfMIJJwTy53nz5uFIlChRgnvCplgtDjmkmIv+LwS7d++WGzZv3vzFF198/PHHCxcu9Izz/fbbb8uXL//kk08+++yzFStW5OgQ0WEDKqpQoUJvvvlmbmcklcCeeRxTy0WTxiHNRf2ScIQgq/TsoNUDlotmCZaLHuSwXDQMqKCrr74avy6rXHTkyJHvv/++J7FSpUq8B4fQcW1H3rx5a9asqd/w7bffcsNll12mJ4ZN1gn++uuv+LmKj6xyURhd5cqVn3vuuZzITBiuuuoqT10lAUpasmRJWaRWo0YN/w1ff/11hQoV+vfv758CRSRIPP/88yO/grN377335smTh/sDd+G2bt166NCh5IQbXn311aSLc7ji559/DmRhdBm5YcuWLUuWLIGFLV68GOOrP/v7778vXboUFjZ//vxvvvkmnSwslVz033///SgEO3bs4Iaffvppzpw5XM6dO1fS1R50yKok8r/cs2DBArsj2Qxk64QTTqBD9unTBxvw3XffSToNMXv27F27dnnup/6nT58+fPhw2L5/a/imTZs++OADx22Lt956a+zYsWEhBDxYuXLl+PHjuX/ZsmX+NTNZei2PyyLSk08+eaELsS46F6WYY8aMmTJlij6SKti/f/+8efMo4HvvvaeGPwygv40aNYrsbd68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T+ZXCE+2K7GX99xzz6GHHspl559/vgrffPPNNm3alC5dmkKXwPTo0YOSG2+8sZDNyQmM4jXXXFO+fHkeBx0twB0ytmvPQ7169WggnpA+4kn87ne/o2TvvfdWCa7hDTfcsO+++1L4l7/8paieixPTuXNn1++87777UFmPPPIIUxhFdNddd0XfAR/lzjvvlIxJP1DPsI+C41KpUqWUAxSd6y0999xzKD37lrFet25dUTWzqDB+/Hh0MtU7+uijd3Zd4mLBggWnnXYadUaiIi77wx/+wDUPPvhgOpi2SEXZsmUpeffdd7P9BHbHBSj86JXTmEDXHXHEEdzwz3/+c8RlmFGuQSXGuScV424YX37yyiuvFL6ShUHRdlexgrEovJJhdvfs2VOdXzDlHwbmgAE9/vjjx44dO3jwYAQm551z/gSmd/PNN5977rloXSZ406ZN8dO+/vpru+Diiy9OZQJGOR1oNmx00a4PpoOFyA4dOqBOeVAE5UNLcwEV1sc33njjoosuwu2k8F//+lfBHk2LGH0pOnDIIYfccccdUPQnn3yyY8eOKsQwNWzYEDV48MEHH3XUUV26dIlQFAl2XyRcdPcGxkaO17XXXmuFK1askDdZrlw5OBs+nPuThx9+WJPcNMgPP/wwadKkRo0aUXjCCSd88MEH3iNwF0rYvsKgwgTGW7S74oorEi4agQEDBsTkovhbXLl48WL+Ryrwzl977bXon+BDhDnbkUce6XHR+fPnY7HeeeedArUg32jSpEkh3ZGM7dqTwHxp27atu0oFP3S5qHDVVVcVIRddvnz5mWeeCfGwkv79++P92A78qlWrUFY4IhE3QQudccYZowO0a9dOSuz666/3LoPkHHPMMWfkgecOHz7cvsUFREqHDBnCQPfq1YuHcpP69ev/9NNPRdLSIsSHH364e3FRsGzZspxcdNasWfjcK1eutBKMTjQXRfMjkAMHDgyXF6yeiEROLvrQQw9Bm7dt2xb/tm3atNkVuGi27trVAGHLuQJlyDnWWpcvKi6K+1G+fHnb4n722WfRkNFmMedPevfuXadOHYtJ4R80FTxQHzds2FCmTBmIGSV/cICevPfee3UNvtzvf//7Iqej+Hjaoojgop999lnr1q1nzJjh/kqLegXmooKWTsCECRPcctQyhah9exxdqidCVgvzxAS7IBIuutujdu3aTM7b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KfxFSRekxNC1a1ck0LNnz5w/mUSkVatWu+yyC8//8ccfc/78LEAxunTpsvvuu1MkcpGM1xObBwwYUK1aNa4/7bTT8lGkcePGHXrooTz/oosuysfz7Rc1adKEF+26667prtkGmyznWLt27amnnkp699BDD1HNffbZh7S4pAvlUGhs+657/fr13bt3h1EU/VEDBw7cb7/9qO8111xT9KcJsJ327dsfd9xxTz75JF6uevXqL730Usa7YHGHHHJInz59JkyYcMopp5x11lmRnVbQvJNOOmnvvfeOfAgU9IADDkgV4MQTT8QqzdkhQ4bcf//9WdcrBk8//XSNGjXKlSt37LHHEghatmyJ+aNI55577r777ssF33zzDU1WoUIFSnXHHXfkowwG8BnegrM1fNgA9oKPQnOWLFmCGLnspptuymthtn1r2kZQqHwppokddk44LrojYPPmzTl/5qOPPnr++efvqGl3EsyePbt169YffPBBPh6+adOm8uXLb2vEpkWLFgm5qPD444/nj4uCMWPGFAMX9fxMK56LeiXUZPkw7XQ4++yzzzzzTP0/bNiwdu3aFdurSxbFKeRiQJ5cd66k9L///e+f//znhx9+mKv39u/fP4dcdMuWLRTvwAMPhJHqyNixY8uWLRs/hvPmm2+SWA8ePFg/N27cWKdOHZ7DP+aaL7744s4772zVqhWl3WuvvcIPmT59+sknnzx37lxI7IIFCyDDXHnxxRfb1zz44IP9+vUraiUtrFixonnz5rwInbFHgNevXy92UaZMGXOwY8eOxcBFAa0ZZjVvvfUWZHj58uX6SWkRV+/evXP76oC+uUQoIQqbL0U2scNOC8dFt3tMnDjRddptjzjooIO2NS56ySWXFIqLvvPOO3nlos8991zxcFFAKhnPRb1ib7Ivv/wyt3lnDFauXFmqVKlrr722eF637aA4hbxd4+qrr163bl0RH0Kif9JJJxVqcC/jex977LEcctHx48fztCFDhtgHa9asefDBB0NT0911+OGHV65c2aYx48aN4znhaf+rVq1Kx0Wp6aZNm8zP77//HpOsWrVq4DL8LfQ4eY1i8PPPP9euXZvy8OrIC2666SbO/vXXX/o5YMCA4uGikYAzN2nSJK+vcN7AwaFEkGMu+n9pQCz57LPPIk999913uhfPO3fu3Lfeeou/JEa5LdiOik8++aRChQqk7CVdEIdCw3HRjNiZuej69evr1q1bbOTw5Zdfpmo7GxctZiFvv9AMCDNUmDVuv/32OnXqJB9iTfLe3HJRTdefN2+effDyyy+Pmag5ffp0zp511ln2QXIYDjZs2DBwMXWJ5KK//fbbt99+Gzi47777whUDB+fPn0/QL9Sq/nTo1q0bhalUqVK6qZK0VI0aNUxfQAly0Q0bNsDMTznllPy9wnkDhx0DmO3XX389Z86cN99889133/3yyy9Nd5Lnz0zBh7z99ttcsGTJEruL7ddff8X1zfTBP/wstjLnkotSpTfTYO3atdDOyFNajo8X1k8EpH8QZQ7LtkOCaKTk+K677nrvvfdQOHNq48aNH3zwwahRoyZNmvTVV1+F713ow/M7Aonl06ZNC+/Q8PHHH4cDHtr5yiuvjBgx4sUXX7QnIMVgzZo10Jvx48cvWLBAvQyoynsF+OmnnzhCtDNHfvjhB3Mv4UFM+/fff3/99ddHjx69ePHi8CsI8CTTI0eOnD17tm11nr+yUat9Vq9e/fDDD8Pev/nmG/Ou999/X5fxfHPQGOf333/PA+2nUWVehMQ4zgMpXsJiCLydRqFGPCc5sSFRQNqe72KgfwjB3vaDZuKZkVt3ZFQDz8+Znn766XHjxiH2SC5KRWbNmoXoUJLAAEUkF40XUSTS3WJzUbSIWowdO9b0XtlA8jNmzHjooYdQTluky5cvV5uiezry6aef6kgg3UzHRbNrMi+98Cmq0TRtiYH3M0e0RJNrkCrv+te//mUXFQXACigAKopHffTRR4k04cw+pskAt9DWFI9Gf+2112R6muio1wVsMKMWBR6og5s2bUJpySA9X+Yo7dy5c80tK1aswCGgabogOyxatEiSQYd59eTJkyM9Em/nXWgOOmDH3XRCLgZg0e9ZIDnQ8Q8//FBHDPtatWrVxIkTH3zwQQw8LKtIyXtpXDfpxSOPPIIovvjii8Ap3vLqq696vh+GcSErzNCcRfkxDQSF7tm6UVhLR2/Lly9/8803h099/vnnTzzxBC8iHzCvTvdelRPdRv8JBznkoiQqmqsfGALlRRy/4IILIu+CvXAWmh04rpWfgYCVjouGgVvgSpxz+FS9evXOPffcjE+IByUpU6YMr4if5nr//febNavpuGiMasUoScwp5I8/N6kwThhfwaubNm1qrIbog8ljGuGNhdD/x32ErQAjwi+RwKDntkbFeINIa0oXcQR8MgarUMXt6A85rZcMxZAvERbxKmPGjAlvsoVrIgn3/BQRn0+74GbNu8zTOK4j9hPC+VK4LgaBJjZI566FeE/lIGAvAT5lNktDbm+99ZZOIX/7FGZu7tIprky+c1sRkeNx0TVbA60SL8dZYLr2KXIR1RbRoHBkTvyvlQBom6QQmc07GOBP69evL+956623GgqBJtWtW3fo0KHIkBSTyHrxxRcrnOAiOVKnTh1NQ7r66qsV7EGNGjXkVriSsKol+/hQ+424tubNm+Pi8b+8+m9/+xvxIL6QOI6jjjoKNgjp5XVly5bVcbKuqlWrmlhLhEAfjjjiCI7g3z1/a0Ri/2677VapUqX58+fvt99+pqiB2Ekedv755z/wwAN9+/atWLHi3//+d9im5+83c9VVV+2zzz677747qsg/3Lv//vvjMc855xz+L126tNyu56fO2rJFb8cLn3zyyaVKlbIH5UgODjvsME5BBUn0uX3OnDkZiyEQQnjgZZddRoQg6zrllFOoV0Zig120bt0aoR1++OFEx+OOO47H6kbaAo/Dz8aNG1MpjvTq1cu+N0YNBJThP//5T7NmzaZMmUJOcNZZZ/GWABeFP5x99tmDBw/mOTVr1qTJaCZzNsxF40UUiZhbDBe955579txzTy7jZ5UqVQIRlCYjOSOAoWyXXnopNR00aJAYGvVFW7iLqulisqXbbruNI2iv/ZAwF82uyTIKH7YJqZMmo4qeH9fJDLQYVUkPzYHY+dmkSRNMG/mT1nTt2pUyc5As5/jjjzfmQMHsgaN0Tca7brnlFjUxpdL4D+AsryC15X/U6VYfEN2MFUn3QP7v0qVL5cqV+Z+EBiumdbTNVYcOHUg+zjvvvCOPPFJeiLuyWIiI69N7SY7JjHm4JMPT7KiBAbZo0QK5EVBQkoMOOuiYY47BanQ2LOTCFiNrkDIOHDhQ4kK3zSY3GBSuo1OnTupB6NOnD9VE/cjwqAgNoaGzdJKn1SJdN0yPizEEDIfcHQZCg+oUDPYf//gHjg5Vnz59OlEAneH2fffdVx1e5CLYizT/+uuvN7qRhaWryuQD4eP4EBw+Hht3dOqpp8a8Fzz11FOHHnoomTR1v+KKK3CAueKixDUeFZ4Wi4fkOC+KvAuCxNmRI0cGjqP2HA/se5SQixKPMEl8WuTZ7t27h1luYTFhwgSpTSTdjUSYi8aolherJOlO4QDh9tqPynSvY+/qJ8WEr/dBsCNgqfz2Fms8FqPu2bMnsQBbkM8xPgHuimLjzPFLZCP4KFRIp8LeICYRiok46C1RlbdwF+pEboZBac8njmeUcL7zJQqJ9PDPNBZ+RvKR/4Ha4ZnLlSt3xhln8BZt1HfhhRfCRbWJIE57yZIleg7BkdtRY2WAkflSurpENrGXyV1n9FQOAq5DlNJ0W+in+nrQfP7nL7QLXRUvVUCH/PO/tu/euHHjzJkz+RnuXcoT8rheFP0WKQ/3fCAFLMeQT0QmYZleEEnBdXhkhBy0PUeXgI0TIcyYI88//zzXHHvssRLvDz/8ICeOIyMnppnIbE4//XSO1K5dG1eFZ0fyJ5xwQsAFP/PMMxi/6cLHresh8SU8+OCD7Q7jo48+2vz/73//OxAIcdbGt1IMdCDl751A6CXmEVEoML6SgyZIw9aomnmC+CSE2SvY/F393LhjqklJFA/WrFmD1+bUihUrzL0kfEqDdIEKY/vWjh072nOECHimszOmGJ4/Nosfp7HMBRi84kRGYoOf5TKNJyhmkIKISpGsKGflOI4bX2+ellENAAGJFjeBnPAmwmC4KIZJuiC+ZN5L/DaENsxFY0SUDjG3iIsSg02kF41s3769uZ5UnvY1G1qAHj16KH/VT8KnzUU9P13IyEWL0mRJhK9IbGTr+aZhuKhXMPPQTBijPF999dWBBx7IwVatWiF5HkXwwL440rlzZ10W02S079dffy3O1rZt26VLl5LTk77IorW8LZDQx1ck5oGEQyUK7dq1E31CRQ855BCOkG18+umnehoXc+SFF16Il2ckbrzxxpTfgyZXgHy0ryasXhdQDMR11VVXmVswJZInpLFq1apIIRczyLR4O5mxOUIGgA0qaSCT4yzV1CmSBn7iCT3fVCMlj2ZGum7aiyNm0JiUjtTfDKfoRUjmhhtu0BCTVgnaawg1I8Du8sjC0lUME0EEKmITVFS3ZcuWMe+lpkQEO4Vt06ZNJBfFzI/PhMBgpqYE275CUCTSjrJhyAbDjE57ApH02weTcNE33nijYcOGXAYzN9m/Dd7F2bvvvjvmIRnRr18/04WR8JYwF41XrRglSXeKiIad7rHHHgGiQiE5Ag+xy1OxYsWUtZyVYtSvXx/iai6AC3GBPBiKh4c3YRojIgeAUpqLA94gXSKUMeLgG3VX06ZNNb7Kc/bcc098qfE86ZDvfGngwIH//e9/zROgypy95ZZbPD92QML5CfO89957CTdXXHEFccErWMGBA7eLyqOIy/o/Ml9KV5fIJk7irpN4KgcUG00gIzVHxLbwPKiEhgCNRxU1VdYxd+5cKJtJb0RNi9jhlRx55KIYYbqptmg5p+bPn6+fmqBrd5e+//77bppuEoS5aKNGjcJxTh23jzzyiH726dMnEFFQ3ypVqnAQhqkjcq/GBeMOKlWq9PDDD5tb4AYkmn379o0pHv5CXMVEizFjxpi4pUU4tm/Fmxvfam4nYNgjJ7g/DhJj9BP/OGzYsL8KoHlNQHO/iQqlfNjjgYImVsFtzBG4mabCCkq7bd9K7gKFMIGWlNp83yy+GPfffz//B0bzxEaSDLKl/CU99pFatWqltu4Xv/DCC1P+IIl+ZlSDjz76CLE88MAD9gWKdoaLki6Q6f5lQSOTo0aN0gVhLhojonSIuUVc9PzzzzcXa8NbEg79RC133313klH7gfhZqDspkeSjtrDzS8J2Ri5alCZLYoOiajYX1ehWOi4qaGtN+/t+c+bMSfkj/BJgxiY78cQT+Rn+JGwkF01SkXQPJCvluP0dRXXD26k5D+EICZBXeGja5HXXXWeOqMnMNx44xc/ARxpJYlJ+Z79+liwXlXpDoc0RiJYZPMGW0W2zSw2qkvLHwM3F6SQfcN3g1FNPPeKII4wTJsW06R/pID9pa3M9CQpHMExzJMwJC2vpuOIyPgLH1V0IyTFHjP8Pv5c4RcKKhttPICpFclEo/cmZEKBzw4cPT0WNf4oIgcjti/bee+9UaPwTnHHGGSbRN8jIRYlBaCn3amAKIYen2UtorVu3TveQJFAETG3dIRuPMBeNV60YJYnXnwYNGiThoojR5qK9e/euVq2anS3AXlq0aCGniuTx+Xghc5agYCtkpDcIJ0IZIw4gbUht3cumiSfx3zHKd76EPKkv1m2iw5NPPslZbEoXQ0X4ifDDZVOL2G1EFNbImxDIl+Lr4oWaOIm7TuKpHDyLQP3+++8rV67k/9mzZ6MVv/32m4b9zAjE559/zs/w+hRuhM1CXO0mzivyxUVXr15NDUlVw/OvqCSnqKSZiIzIOGJW7nk+QedIZI+gg40AF0XsKX+iXeAyZWnnnXeefqoz6d5777WvURQx3FK9XMYFy2cl34jfQB2EOAvT9WCQ0bfixcI0TDkZcRpnpzFDkvgzQjD5OlcSPMIF417ImAld2rfATjXICQJc9Oabb+ZI9erVzdiLeVR8MYgEZoKKQfLFh2EhBMbQvILme+aZZ7xkaqBdKwKrOwLrRREOpDdcKcNDwlw0nYhiEHNLeO8iDWma2El9+Wl39AoK/GSWXrZcNOsmS2iD2XFR7ChA8Dw/o0r5U229BE1GMpeKGgkJc9GEFUn3wDAXtXvxBQ3vXHnllV7hIS5qT3sLrBvUBqGBNZbKXczXHUuWi+JtNFZMQqAjCNOeE2WiJxmwhiyaNm1qzqaTfMB1m3fp7/Tp05UFvvLKKzqlDM8egdFY5ZFHHmmOhLloYS1dXxQMGJ3nz6LXCEnHjh1tc4h8rybjDBw40L4mh+tFZQV16tQJHNegdIUKFSLvki2H5SATCGzJm3y9KLqqaZnhlagiZsccc0zGh8SAgomLBghADCLXi8aoVoySxOuPAlxhuSiuz3yVKhLGoHALUKM999wzZQ3qRnqDgDUliTheARe1u7YT7guY13xp9OjRKX9aTSA6IDRl4wroHAkXTML597//rZ+Q0sCeguF8KaYuXqiJk7jrJJ7KwbNm2Aq4L81GwfnoiFlijUj5GfgSj9ncx15llm/ki4uSglOTyF1GSLY4ZQ84hLmoZOG4aEYEuOgbb7wRGUpfeOGFlDWfNpKLKjJ16dJFPwMuWD/TjdeTnR++NcwGFTSuRmYgfp06dbKzmex8q1cwM4f8TF1x8f49HRcFuOBUQeclbtrum/eifCscpnXr1orf5BlGGvHFIP7BasJrkPLBRTWjJoka6FOiJgkW7Hj566+/Zszwwlw0nYhiEHNLOi56wAEH6KcSmvAUHXWyasJPFly0KE2W0AZzyEWlxk899VSSJkvORRNWpOhcFD8QU+B0iOeimzZt0rASFMi+i5AsTdOATMlyUa/A62p0d9myZeFtQufOnYtPvuuuuxYsWJDyO7zMqUJxUZK8oUOH4iVeffVVHsgFMAedyo6LFtbSly9fLu4RPkWRtKAOxz548GC7/zrwXu2wFViZmUMuSgKX8vcUCByXIzr00EMj79LkcNPdY6DdHAJrPpNzUa8gsgRG4Tw/iUolWCATj2nTpqn5pkyZkvCWSC4ao1oxShKvP1lwUZl2uv2lDAgHvXr10gJX9eKZMaIkXDRJxPGKwEXzmi9pjDcmfsVwUegNnNCsA2rfvn1gr5BwvhRTF2/rJk7orh0XTQLUQJNyYWEkePp/zpw52rUnwEWXLl0a5qKLFi2icUViwzMK84S8cFFSIlUjPCjKES0itfVSg8jhObrFScq3UwS4KHJTRA9cpuNmMlgkF9V8OTNnKeCCL7vsslT6lV3r1q27YmuIFAnEKry/tuwjFzFTr7P2reQKopdjx47lArNoIRIxXFTLD1q1auX5qXOgVz7sWwVkoklZ5cqVe/nllzMWQwMCFCNgDvnjoknUQDvHmDm9gh0vlTuaBbSRSPdNl7CIMiLyloxc9M477+RnuC9cxzUBOwsuWpQmS2iDOeSimp4NaUnSZMm5aMKKbJtcdMuWLVoQHp7KgYKRUSl/LXEuShyknHvuuSc6eeONN06aNMmcIj/r3r17w4YNtW+Cxjey46IkIrVq1TIUTr6iiFxUSG7p69ev57I99tgj8iyx3mxFAyE3n9kMvBcOkApN6k7HRTHe9zJBayjsQmL15cuXDzxKA0r2MnUb2h0NnxM4ruX3gY1VCsVF0VLipr1IQZANFnFqIuREBKBbt24Jbwlz0XjVEmKUJN2pLLjoihUrUltP4AyDdiR2mA29s+CiSSKOVwQu6uUzX7r00ku5IGaPsRgu6hUs0SdFJMMPj8lH5kvp6uJt3cQJ3bXjoklApLAnpSJbfdyFRAj/Fpiju2TJEnsrXQPu5SCnspgLmR3ywkU18hk58eOHH34ILKs1B82Opp5vEhzJuM7bIcBFFe+B2XxM0FBGjx499DOSi95yyy0c1H7ZXsgF44BS/oa9gQIQaMMTqwz+/PNPowb4Ee3VYYqRnW/lIBFUOxDMnj2bC+rVqxdexmMeG8NFPX9mSKlSpYiC4Xgf9q1mVj2+WG5dKysyFkOT0AIzVfLHRZOogTK/e+65x77AjpfUBW5GFAm3r2YCe1FcNJ2IYhBzS0Yuqq79qlWrBkijeqm1lC67ObpZN1lCG8whF23evDnNhGSSNFlyLpqwItsmF/UKdgYys+YEdbQbBStxLur5y9QpAyXBqO1NgPv27Zvy90zWz6y5KOoK1z3hhBPMBTnhollYulhHwEkSQcxjX3vtNW3IZBbBBt47dOjQVGidZDouKtYXD3tzMkGDnIGF4pLYk08+GVkvjaYGVrGqveBpkaVKyEVxa+Ti4R2etZeMWUeXNcTtK1euHF6SGokAF82oWjFKEq8/2c3RJdATzQP+yvM/fcTfGTNmcLH9SaEsuGiSiONly0XznS9pI+uuXbsG3vvTTz/pi1DxXJRIWrp0aVR6uI/A2UC+FF8XL9TESdy146JJoCWgNofEm2kuqtli12wgp6+/aDfBFStWLF++3EyT1kJLe0/ZvCIvXBTLTzdBV195CTiLjRs32ps7aQ9ijhTl03M7CTp37pzyp+eZIxdffHEqtJ6BtIaQZvqAI7lo06ZNGzZsaNQu4IJxK3j5VMGKROGHH34gisQUj/zY7PCpn7vttpsZUdHG9PZwogpvdjeJ9K3adl/0mwdqyUfPnj3ta3r37m3264vnotqsgmAc/j5nmIuaxRJCs2bNyPu1Ijy+GJpF2aFDB/usNsKxPw6WDmEhxHNRL4EaaHIgccUMQYB27dqlCnYd9Px9KVL+pqn2pvlTp07t37+//g9z0XQiiqldzC0ZuSiuQ9vNB7rbeUidOnU0EeXnn3+WAE0tkEAqtCtmgIsWpcmS2KC+92C6qLG76tWrp6xp8OPHj09Zc+aFMBeldtiUyZ8yNlk6AvPEE0+kQnPPklQkt1yU6ptdduORkYuOGjUqFVrvqnzUkIpIIRcziIZyQYEPb2oLUOOXvvjii0B1EnJRrbG0CYMG0o3JJMnwZGV273AWli73EpjuhJu1Z7Gqgcz4UuC9JFgpf8KCvap25MiRKWt6pAHhY3omhHvMCaY87f7777cPHnbYYdi+7Sq1T6n5Wbt2bXiRnbTpOcOGDQs8v1Bc9P333+dK7URtQ/v92rOCuSaLD9OvXbtWkSvQmgY0KCzLMPMAF82oWjFKEq8/2XHR8847L+UPF+MVzTWkE+KE2iLBtjJ9C83kmZHeIGBNSSKOly0XzXe+pI3uSOTs3S55S5s2bTQVM56LegUSPvDAA8OdF4F8Kb4uXqiJk7hrx0WTAAcrDil/hU2JkclnavmkBqhRGA37iaxp+NRklSJrGb/amCvknotijRJEeD6PVzD5NvzBdG0fPHPmzIULF2rRbeRyZ4cA1NGFS0Ls8JD169evWbOGTB1/ZOIHeva3v/3N/uqXuOjpp59uXCf0A8Jm72TTsWPH1Nb7LojtpPxu6TvvvPOGG24gAIe/lWwDB1SxYkUTSgnVRHTTyyvXX61aNUyF5iblPeWUUzhy9tlny0PJtwJjDzwQb3XOOeeYV8CodQ1RitIS+4kKJnsmcsj52ql5oIR77LFH5EIgxXt7Nk7jxo1J683PCy64wHjt+GKQbmqayvXXX//999/TTCRb+vwX9DU8QSJQwpT/TRf7i95a6G9Pa2/fvj1HzL64GdUAgdSoUUNMEu/Dw0ksNHCBYqhjm8xPk7jw9egMqQ+RpkWLFuZziC+99FLK//BAEhGlQ8wtmvysSdSC9tG1wy2+Akk2aNDAdPWRvqPMtg9V9kBzoFeTJk269NJLUUu0gvLrLo0BcsSkNUVpsiQ2qF6kf/7zn7AvPB7mpm0/II0a1dRgO0kwJaQuOEavgIvae7eQgh9yyCFmUUfGJtM3GMz0BwONOAVWWyWpSLoHKtWwW+HKK69Mbb0Ri6Y+mgElfZMgtXXnWjrcc889XIlTMkfUvXLZZZeZI/p4vemgQckRBe7FXBAp5OIHKRq6Z38lwisg87jEJUuWkPhq7AgLpZAKjukkH3Dd2ncHoPmkF8hfLLdv374yc56W2nrigCif/QkHFJUjDz/8MIk7nN/LytI1om5/w8bzU1geZUgI5oAozPql8Hu11/fBBx88a9YsGnTevHkyHGycnDUn/df48OrVqxtqp3377P2KtXOvXV+S5tKlS5vuXeJO3bp1mzZtatNXgSZIRW2DhAkT12699VaTOEGooHmRM59R8nLlytmb0GL1++yzjzHz5IDjiZI1b97c3k6TYI0j5aA9GtyrV6+UtcFhRtWKUZJ4/dFncuyxHdESe2ooJdQHS8xElWXLlmmqJ8137bXXYgLkKsYhaPcveBRVJiPnAm0NhYS1ViXSG4QToSQRR0th7TFMdW4GlD+AYsiX9A1V5IbAH3roIZoMwze6rVVL9tfpAtAUAHsvYoNAvhRfFy+qiTO66ySeysF8TRN9JnCLiKLh2p5qxYoVGuqDc4l80qZyv9q4B8ydOxdR63+7PyivyD0X1WJRe0ayDX1ZNTyFDFmYygOcRdiJO4SBYsmfkqOYiTFEtQsvvBCf1b179z59+hBZA/FMXBQjr1+//uWXX37eeec1adLE9BAvXbqUhFjr3fHp9913nyIc3oQYg8+VvzvuuOMy7r+nAcNGjRoNHz6ckIaD7tatm+k85h91o6b8kS7KD5Xaa6+9yLo0Y0S+lTd26NCBoNi1a1ccKzUKzBng4ZpRmfIHu8w0j9dffx0ao+PEOfN1hAAoUqAXHOLBEREYos4tt9yi3hOqfMQRR/Dz2Wefveaaa3Cd9idw0xVDwOy1jh+QNFBZfDGRlfQlZpIzQUW5l9JubITW0fIkNcGUKVNonTvuuEMfhdfXw3VvRjWAVyiYpfyN4AcMGHDJJZdAUG+88UbDPXBqoqwSRY8ePUwApoL6DjhpEBqlyQ7xIopEulsmTJigb3mXLVv25ptvJuHAe2jcL+UPpq1cuVJPoLSETwrDQ6gsTwjsyUTaqo+Pp/xZeVSBJiBTvPvuu6FbpERmrRoSk+5l3WQJhb9q1Sp9QlCx/4svvoCS1apVi8Y1A4Pah5CmMcNE4qIYCJkQ5kCobtOmjT0IENNkUBrEq9kNderUQcOVbaMGyAEDVI5Cac02mPEVSfdAMkJN+E/5XxOF8GNQJHMageFFmLn6zrRoGVeDAvMiEkQll6effnq8eEnyVEeeCTEmWJCoaXle5cqVzcxzwgquDPIMIYfAkyfxooD3CAu5+DF58uRzzz03cJAcQsM+5cuXv+6666A3GghFSVDRSMmnc93Gh2AjCBkNUYcF2Tlv0WNTfrfLN998QwajD2Om/O4b7SZCo6tr5sgjj9TAZhaWDnDgJPf2Ebgo9KBly5ak6biUZs2ajRkzxpwNvxc54LHxCSn/U0bo/4MPPkij4xCgBDmZTsYrcLZUcPTo0XgenEBgOEsjsXYfmeczGbJk2BqB5qSTTmrXrl1gMj9Og+xfcxFTfqcJNdW3ZD1/RpymXVCXLl26yNzSbZmBEdlTGPC9iAIflR0VR3mopswHY6HwKACNi0hN/4i+zi0TppwYnfq/YlTLi1WSdKfw1VdddZWeiTKIzqEkslOAhyRpJkXUnNWU3zluumURhfGrGDVlNt2LNIcCFoZDPoDf0zBvhQoVzACm7Q3SWZMXG3FQnkGDBmGzKf/bY0QxjvAc9WNyS8znlIshX6IKnTt3lvmk/G+9mM/MPPLII1iZjlMpM7MsgHr16kFj7COR+VJMXSKb2MvkrhN6KgfP78YSBRVII21fBL3URFSdMhkdol68eLE5xT/8LJ4Jul5evy+aBaCv6JPxzg5JgM3jf8Mag2PieOTXgcwcXbwkXjWQy8YDf8Fjk6QdgrokfvjhB3hU5CQiQoLR+F9++cWe5WXPOSF3J0ePMQwyY4JHFpaDiOzPXsVAoQjTxRdHTkHPWAxqYYJWRj6TE8SogbBu3bpFixap6ydds1Js9CSJlJKIqOi3RAK/sXDhwnQjAxSes2b8MMkyXaEoTRYvfJQEbTHZXrhI3I7Y7RqZObq0GtWJaZHkTZYEGbUoVyCZfuaZZ3I+aZbcKN3XqsNCLn7g9CJNTyptGlG5gj01NDmQgD3uiiYn9+ECPtze6Sc7s+XiKlWq2JNOqd0WHySXkSodeK+Av8JraaIg8SsfPdcEVpJmChz5cIoUOSFZeV52W11QdzLIV199ddmyZTGB7LnnnoM3Buad0QTmI3lZQx94gJwQapOrWYxqxShJrtx+JPClGLU9k0hQ9mKLjna0E85CeYP4iJMdiidfQqUpeXYZSPLGyliXdIhx1w4JQdPjHhE+f8OeCtPARjgV1hBajVPE+nRzCfOEbYuLOhQPIteLboNIty+cg8POici9i3YkEBovuugieyG0ww6GMWPG2POoHQoFCGft2rVjtkJ12Gnh8iWH7ReOi+6McFzUwWF7xA7PRbt06WLmSDvsqBjio6RLsf1hw4YNbdu2nTFjRkkXxGFbhMuXHLZfOC66M0I7ucNIS7ogGWA+81jMswUcHLZNaIGlWeGz48Htnb6TYMqUKeajlA5JsGXLll69eoWnKzs4CC5fcth+4bjozoV169ZBQffff/9KlSpVr169T58+4U8CbCOYNm3a6aefXslH69atA1/CdHDYqfDpp5926dKlcuXKmMPRRx99++23F896YwcHBweHbRwuX3LYruG4qIODg4ODg4ODg4ODg0Nxw3FRBwcHBwcHBwcHBwcHh+KG46IODg4ODg4ODg4ODg4OxQ3HRR0cHBwcHBwcHBwcHByKG46LOjg4ODg4ODg4ODg4OBQ3HBd1cHBwcHBwcHBwcHBwKG44Lurg4ODg4ODg4ODg4OBQ3HBc1CEac+bMmTlzZkmXIgPmzZs3fPjwUaNGLVu2rKTL4hDEqlWrRowY8eOPP+bp+V9++eWzzz5blCd89NFHU6dOzVV58o18yzNrrF+/Hl/xyiuvmLLNnTu3ZIuUBEXXn20Wq1evRlXWrFlT9EdhINOmTSv6cxyKE5s2bXr00Uc//vjjki7IVti4cePbb789ZMiQCRMm5EQ5E+LPP/98/fXXFyxYUGxvzA6UkGSG0hbDXTkHOdjTTz9tfubQBQXgPNIOCcdFHYK49dZb//a3v6VSqeuvv76ky5IWmzdvvuyyy3DBr776auXKlcuUKbOtxV2HK6+8Ei3673//m/Mnk8oceeSRPLxJkyZZ3E7YHjBgwIEHHsgTzjjjjJwXL0/InzyLgnHjxu29996NGzfu2LFj06ZNa9asecEFF9SoUaOkyxWHIurPto+uXbtSu549exbxOaSSPGeXXXb5+eefc1Iwh+LBpEmTaLiGDRuWdEH+P9auXXvqqafOnDnzoYceomz77LPPH3/8UQzv7dOnT6VKlXgj5LwYXlcU1K1bl3IWtns0u7tyiClTptSvX58y4FTNwVy5oACcR9pR4bioQwRw39s4Fx08eHCVKlX0/2uvvXbaaaf98MMPJVskhwBmzZrVunXr//u//8vHw2n0InKJxx57LJKLbt68uWhFyxkCJcmrPLPDW2+9VapUKTvhINc84IADOLjtiDESRdefbQoBac+ePRtV+eCDD4r+5GuuuSbnCaVDPLKwncAtq1evbtu27eOPP567QhUVZ5999plnnqn/hw0b1q5du/y9KyCNDh065JuL5sTdUcLzzz+/sDNfsrsrtyA2BbhoFi4ooQydR9oh4bioQwTUc7ktc9GaNWseffTRJV0KhxLDZ599VkQu8c4774S56JIlS/r371/k0uUA205JYkAOhAwXLlxoH5w/f365cuVWrlxZUqVKgqLrz7aDL7/8sl+/fiVdCoec4eqrr163bl3y6//4449OnTrlrzxFB96gVKlS1157bfG8LiBA3ptXLjpx4sTtaK1HPvD1118HuGhh4ZzYTo4cc9H/SwP8ArE/8tR3331nP2H16tW6PrcFcygUtnEu+r///Y/iOS66MyMfXPS3336rU6fOf/7zn1wUsEjYdkoSj3r16iHDZ555JnD8kksu2caXjO4wXHT9+vV169YttizfId94/PHH0cxffvkl+S0dO3asX79+/opUdLz88stUqni0NCzAvHLRTz75pEKFCs8991w+Hr69oIhc1Dmx3GLz5s20yJw5c9588813330Xnv/XX3+Zs+TP8+fPf/vtt7lgyZIlW7ZsCdzOxVwAEfvoo4+Krcy55KJU6c00WLt2LRWLPLV06VLzhF9//XXWrFm6PocF2yGBtN8rgMSF9MwRe8k4ee2kSZM8f5ncW2+9hUf+/PPPww/k9pdeemnUqFGc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jVmzZo0dOzb+/VOmTPnoo4+y+eL69etfeeWVZcuWZfOSIBYtWvTPP//8FgOhWfr+++9zm59tGd98883rr78+efLkzZs3x3xk5cqVb7755syZM//+++8izZuDwY8//jh48GA7ZcuWLR988MHnn3+ewdt++eWXDz/8ENWbMGHCkiVL4jyyePHit99+m0d4cO3atcEbfv/9d59y/fnnnxnkLZ/44osvPv744+LOReZAZ9HE7777LofvnDp16osvvpjDFwJkbNSoUbl957aGpUuXPv3007iP4E/z589/7rnn+HXevHkx34YLGzFiRPQ9SC8WoNAZLQzQ9KFDh2JqivQrabG962kQPo2IEJ5sENTlP/7447XXXluxYkVuP+SwfcFxUYdtEXia+++/v2bNmolE4swzz4zzyAMPPLD33ntz/0033ZTZRz/99NM2bdqULFmSl2QWT4di48aN11577Xvvvbdq1ap77rmnRo0aCQ977bXXvwpQp04dLpUOrTLP/vrrrz179txjjz2eeuqpXOVn28G6devGjx9vp8yePfv4449PFOCAAw7A5Ue/ZM2aNS1btrziiitefvnlW2+9tUqVKvxTlLl2SBJMqJl23XVXpRDHIOTlypUj8eGHHy7U23j2rLPOQshbtWp19913X3LJJdWqVatXr97o0aNTPTJx4sTDDz+8Vq1aHTt25JG2bduWL1++WbNmM2fOtG8j2ubNkqUSJUqgZfvuuy937rPPPmeffXavXr1+/vnnDIpfRHjhhRf233//bCxY8eKff/657bbbqF6K8L///S+Hb6bVeOf06dNz8jZM8XHHHccLMbw5eeE2i06dOlFM5NyX/sgjj+CJPvvsM5wRejFp0qTo98D9jj76aF514IEHprqnX79+8tdXX311DrIehh9//LF9+/Zy0KGdtvnB9q6nQYRqRCrhyRK2Lv/yyy+XXnppmTJlSEnr6B12bDgu6pBXFGrYCqMfn4uCO+64I3sPAf/JIRfdsGHDGWecYUdRY8aMUXDsi5vBBx98ULZs2aVLl+py5MiRN954ozjqDsZF4duErURCDz74oEkk1MAjjhs3jjiDSoBeUnD4BjFuqvds2rTp4IMPhm+YlGHDhvFU//79i7YAOz0gkDYXFaCRheWizz//fIUKFRo0aGCPhSIAV155Ja8iHvINgGzevPn666/np86dO//xxx8m/fvvvz/ppJN22WWXp59+2r4f4alUqRL380KTOG/ePDFn1K1Hjx5//fVX/AznHLZJRM23uxjXZ9LbtGmTPRf1vbNPnz4XXXRRDse0v/zyywy46HY35+L9998/55xzfCOfEyZMoOyrVq3ifxxT48aNFy9enPZVX3/9dTQXBU888USRctGkp86VK1cuFi6aBz3NoYAV9lVBjQgVnuy/GNRldXM4LrqTw3FRh7yiW7du8Wd9fPrpp4XiooSh2XuIf//737nioljn0047rW/fvnbitGnTxEVDrTzB98KFC+2ULl267EhcdNGiRVdddVXNmjUfeOCBX3/91f7pnnvugY6aS8IOXCNlnz9/fqq3QWW54bXXXrMTeXnFihVDJ2065BAQPx8Xvf/++wvFRT/44APu32+//UIjyxYtWvDrHXfcYSfeddddJLZt2zZ4Py2uSQfvvPOOnV6nTh0S//Of//juX7BggTqemjVrFjPDOcfAgQM/++wzc/niiy9ud1wUk2VfXn755Vly0a+++qp3795Z5ysKP//8c2G5qK+ltl+0a9du9913L+xTkIe0XPTVV18tai4KyEP+uWge9DSHYk/lFLYVMtAIH3x2ID5gvI6LOuSYi36RAtAPIu/Qn5YvX5704s5vv/0WAvDhhx+i84Tj210fpENaaJzTx0AisL1zUZhS3bp1fZKMzEdw0ZUrV27atMlOue6663YMLoqvvfDCC4n+n3zySXtEyyBYIeeddx5l/+mnn1K988gjj+SGr7/+2k6E65L40EMP5STbDqmQJRcluq1duzb3DxgwIPSGWbNm8Wvp0qVxDUqZM2cOlyTOnTs39JE+ffrw68EHH2yPpnIZykUB76EI/OobTc0Ppk+fztexciZlu+Oi2CXEwE7JkouuW7cOqUCQcpG7lChs5B1sqe0XBx10kOOihUIe9DS3Yt+2bVvCmEI9kiUXDdqB+HBcNOcg5ly8ePHkyZPFp7777jt77s+GDRtmzpz58ccfc8OCBQt8884WLVo0derUjz76aNq0afZ6saJGLrkoRfowBX755RdELfQnjQLNmDGD/z/44IOJEycq3RdfOkQAQzZhwoT+/fsTAfiYTNKbx4hsDRo0aPTo0aFb4CCsq1at4jYs7LvvvqtEgrk33ngj6bGjgQMHfvPNN+Z+yOSbb775zDPPTJo0KXR6G233ggeb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siRf//HHH/P56Xzi4IMPpoBwTl/62LFjmzVr9tFHH82dO/f444/nHsQvs08sWbLkmmuu2X333XnJE088kfZ+QqvLLrtst912437oawZfzKcdcADz5s2jqqnw/H8a3bzwwgt32WUX2y4FQRDMDWi0L/3NN9+85JJLZsyYUb9+fW548cUXizKzaRCzLDsbilG6tnFsswLz1VdfnXnmmUQL//d//2cSU+lglth777157Xfffafv/vvf/+aSxNx+5fzzz+e1gwYNyu1rHbZ3bFuK57BNAXtRFDHoX3/95UuB4N122225/Uo0+vbtS5CdwYMTJ05s2bIlIVc2X1+3bp2Pi0LYWrduPWLEiGxe60Px1rPv6+IzWXLRYIm2HRAf4GV//fVXO3HChAnEECtWrNAl5PDEE0988MEHs/kQIUhMLio0aNAgYy4qFJEdyAxFIQPFK1f//POPnZOLL7748ccfL66cVKpUKTocX7hw4bnnnuubXrFq1apdd91VHTHLli1r0qSJBt9CpwkUKj/ZPJu2LDsbUklXsJmybLg4yPknMnih/cg2KzDr16/3cdFQHYxAzJp57LHHLrnkEnPz6tWrc8JFfV9/++23W7VqtXjx4ixf67CDYZtTPIdtBx999FFRxKBdunTZFmZoNGrU6KWXXiqur+NaitrtFWM9L1iw4N5777VT/vWvf2XJRf/444/OnTtnnbW84oQTTmjYsGFu33nPPfcUiouqHzobLlpEdiADjBw58s0338ztO4Oymk9ADObMmVNcXw9i3333zcAu9e7d24yoGPz6668333xzxjnJvmYyK8vOhtBmKmpLm6VsBDF16tSBAwdmmYdtVmD+z0PGj2fcmrvuumuWXDTnDe2woyLHivdFCqxfv37evHmhPy1fvtx+w7Jly5S+atWq3ObNobAoihh08ODBvPO3337L4Tszw+eff16+fPls1o5mg6LmosVYz3y0bt26N910k52YPRft2LHjMccck3Xu8ocNGzZQ5LPPPju3r91puejs2bN333333C5bDZXVvAETVKpUqa+//rpYvh6KzMLxiy++OMhFkfw2bdpklo2c1Mw2Sy22KQSbqVevXnvuuWeeP5oNfvnll1q1aj311FNZ5mGbFZhsuGg2rZk9F81tQzvExN9//7148eLJkyd/+OGHn332GZbZnvtDZDJz5syPP/6YGxYs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iKiNCRMm7LLLLrvvvjvM86mnnho6dGivXr06derUvn377cvNr1ixQusJU+2V4uDg4OCww2A76ip1cHBwXNTBwSElJk+efOGFFx500EFVqlQ56aSTrrjiitDNsbZlvPXWW2eeeaaOGWjdurU58MPBwcHBwcHBwaF44biog4ODg4ODg4ODg4ODQ77huKiDg4ODg4ODg4ODg4NDvuG4qIODg4ODg4ODg4ODg0O+4biog4ODg4ODg4ODg4ODQ77huKiDg4ODg4ODg4ODg4NDvuG4qIODg4ODg4ODg4ODg0O+4biog4ODg4ODg4ODg4ODQ77huOgOiKlTp77//vvFnYttAps3b37jjTfmzZuX9rbnnnvu66+/zk+ugli0aNFLL71UXF8PxcqVK/v377969erizshW+Oeff36Lgd9//133r1+/fuTIkWvXro1457hx4956663M8sObhw4d+scffxT2wS1bttgZjr75r7/+sm/++++///zzT1+RU+XBvtNUSyps2rQpfq4yw6xZswYNGkTxo2/78ccfX3zxxaLIgIMQIfa//vrre++917t378cee2zixIl5zthOjmJ3RsKUKVM++uij4s2Dw7aAmTNnEgkgk999913w121EXB22dzguukPhgQceqFatWiKRuPrqq4s7L8WMn3/+uUuXLrvvvju18eqrr0bfPHr0aG476qij8pM3G2PGjKlXrx5f/9e//pX/r0ege/fu5OqGG24o7oxshU8++SRRgPLly++5554lSpTg/7Jly/L/rrvuqp/23Xff5cuXd+zYsVSpUlyGOlEBss0Nu+yySzRfDeLLL79s3rw5D/I4wlbYguC877rrrn322UcZHjBgQMTNnTt31m3Vq1e/++67KRpic95555mqaN++/fDhw0OfhW/QlGXKlNGdc+bMifhQnTp1dNuxxx776KOPFrZQcXDYYYfxfohQqhs+//zzRo0acQ+VUxQZcEhGij0Cc+aZZ8JFFyxYoIb4z3/+UyyZ3DlRjM5IIIrYe++9ycNNN91UXHlw2Bbwzz//EEQNHDjw/fffr1SpEuZi6tSpvnuKXVwddgw4Lrqj4b777tvBuOjff/+d8bOnn356HC66cuXKNm3avPDCCxl/KBuIXxWWi2ZTLXFeOGnSpJYtWwZ9T/FiwoQJkM9BgwZt2rRJKQceeCC1d8899+hyxYoVF110EbGULiGl0VwUoCyZUe7NmzfDgTPjosLLL78s7nfAAQekalBog2GSvsHzI444gsQGDRqk/VDXrl31hk6dOqW6Z/z48Ybc/vTTT4UtS0w899xz7dq1C9aYXfzvv/8+n1w056q0XSBU7D/66KNy5cotXbpUl7/99hsm9NZbb8177rZjFFacfPcXrzMS7rjjDsdFHZ544okKFSrASJOeZWjSpMmPP/7ou6eIxHXntMk7MxwX3dHw/PPP70hc9M8//+zcuXPGjxN5x+GixYvFixcXlotCrnr27JnDPOT8hUWE119//bLLLrNTfFw06cnM/vvvr/815hzNRbOBuG7GXPSzzz7D2Yv+jRo1KvQe2uXkk0/WPZ988on9U/PmzUk877zz0n7owQcf1IdKlSplmIYPjRo10odg+xmUJRu88sor9kjpr7/+mjcuur1Ifn5w6qmnHn/88cWdi+0YPkmOg27duq1fv76I8pMZnn76acdFHerUqYMDzf93M1Aih+0dOeaiX6QApnbevHmhPy1fvjzp9b8Gf9q8eXNus7czYAfjopdcckk21nCH5KIbN2487LDDrrvuulxlIOcvLDq89dZb7733np0S5KLglltu0T/bOBf9/PPPjznmGI3eh05z2rRpU5UqVcaOHSsu+umnn9q/nnXWWSSef/75aT/08MMPd+nSpWLFitz//9h783itxv2P++5U0oAQoSInVIdORVTmKHQUInOOpExJGULUeb1KIh1TKcoQSQllHjpOGUKckCINVEdRlEp1RP2wnvezPs/+PldrrXvda99731tpff7Yr31fa7qG7/S5xp49e4ZvmDlzZs2aNUeOHKmpm/kVJz/MmTOnatWqzz33nKWUGRfdiiS/DLBhw4Zy5cq1bt36987I1oqwJOfEY489hqgj8IXLVR5IuWgKbCMyUPZcNA8lShHAr7/+SlQ5ffr0N95447333iP++eWXX+zq+vXrcfdvvfUWNyxYsEDj3gJM7ZNPPnn77be5+vHHH5elXSpNLkqR3siC1atXwy0jLy1cuNDzZ9aFL/3888+lmL0/MBAgYvSHHnpo7ty52bjo559/Pm7cuDFjxsyaNcsVPsOSJUuefvrp0aNHh5ehExC/8sorvPndd9/97rvvMFJJckWb/utf/1L2XnjhBT7Ns+HbvvnmG66OGjWKl7t7q5BJzRTab7/93veRUB544ZNPPjl27NgVK1aEueiaNWtQM/6ZPXv2ww8/bFni07aTx6effvp+EahSJXKnUtz6QVepGSJ4Mu9qe05s2rQJG8GDZCYbF6WlqPOnnnrKnRjDF0844QQxEDKDvbBLZGDatGnUJAWJ7Ghfu3bt5MmTR4wY8dJLL9kc15gXfvvtt5Qr8BLunzp1KsEKr4qcaTllyhR1MFFRyCSKnLxa8kAkFzUYFyVjH330kZa+BO5B0igRleMm0jrID7WEIL3++uvuJZwlkoOz5GqpcFHURFRT+uKCCmzTpo0kpIRclMhSClWlShUMcuCG884777bbbpP1SMhF33eAbpqCCKpP5FA/KYI9iGDYdmL8ozq84447uE29Bi4XRTFpsgcffBCtDOchmzRizfRdlEgpGEClmITHSH6ZYeXKlVgnLDP5xHC5l2b78PyRW9oFpY7cTcqsROBxgVZ47bXXAiovIPZUrIk9Uo39pzaaN29ujYg9mThx4v333x/ea4rmeMxHzp3hePbll1/2fBOKArorlmPsJ15G8ehPP/3073//+5FHHjFTbFi0aJGqiNYfP368W8CYaompcy/WD7oe7fnnn8ejYSLsaqQkC7yKm9HlwJIHCqgl7hSQR+xtlJ1qCddkvBOnRSTD+IvHH3/82WefDbQ4mD9/Ppf4LnFXpDsWXC6K2eRnNvGLqS7Pb3palvalIdy6SliixYsXywHxaUSIJjbDRdEQTsxC5HfjcxUGwTevIidffPFFzpvj5ce1SKtWrXKzlNMiCYEQxa23GHX2ih+N8AYEkk+g41S1e4lcUeFu9BXTnxsWV1IUdCEAlIW6DStvZDXGKBHaR5tii6jenJvwbePAmItDUfn6B4apS9iuN998U5eoSfcSWqZLwP4pMzpayuOiKzcHyiZejkRSJPfS0qVLVREKmjEB/E+ie086ZTwJMNDYC8wu0nPJJZcccsghAS761VdftWrVqnv37tQwJhJVP/TQQxFWu4F6vv7667t164aea5eUCy64wLblxLHtv//+GCwcP5FE+fLlp0+fHp8lYvejjz66XLlyxx13HKazbt26Igy77bYbL7HbMCjkilAbq4eVOeqoo/bYYw+bm4HwXHXVVTy1++67/8NHzoifguA+jzzySNwwxrFdu3YHHHCAcVHefMYZZ1SqVIkIHrKqXWfOPfdcArJzzjmHAN3GYXDqVKn44YIFC5SIX6FydtllF+MDsJSOHTved999ffv2rVatWrNmzajqXM31/wLjS5US+uMCIQnHHntsgIsSJcAN+vTpM3z4cNquYsWK99xzjy5RrlNOOYX7DzvsMOrkn//8p9JnzJhBOj/vuusuartmzZrol/tRgjlqmNgRHwlDo1ZVkMgX0ty0HS1INtyXID+NGjXCfxCTde7cmUCKUkhPMWRUPk3Mq/gE8T3ZqFq1aqH715NwUVSjcePG1LnmqXbt2lVX8XzImLb7ktuDfvfr109iw1PUiUigYhRkgGq56KKLiB0J6Vq3br3jjjuWnIvyT5MmTXgPkhC4oWHDhmhTaXFR5EpLTwcMGOBeJRSoXr06MVCxuOidd96pXImrYLExO0pBnRUuEJRce+21iAFxFXHkoEGDtHcRcbleQlylNqIUNKJU1bgoJovWoRIqVKiANFLnbgZipJFv9e7dm5fQlLqZFqTUsidKyaZKZQayjViSDWTv8ssvR80934jdcsstFJmMUcOk245cGFI3tg5biWHDhrnvR+UxhlJ5KspUXmKPiXCnDNAQ6rnDQVzvg4Y7+eST9Wm3HxCP0L59+169epF/GlT+IjL2Jcq57LLLatSogXXFnvMPN9epU0dXsZ9nnnmm2U9agXjd8/eBJ71y5coo18yZMxEAqwGtXEXYKDLWjBRazaQOJ5izWiLrXJAfxIeaH7zwwgtVcNej8ew+++wjs0OVWidLpCRjFVHStm3bfvjhh3il2rVr4zJE7LmEQMqA8F0e4R6c0dlnn03ZA5MCAk6cOsSJG6vn0zJZAwcORAVq1aqlzYdatmzpBlG33nrrSSedRPXSLggGnjebZIqLIiRkJlMEXksOk1SXQOBHBvBHeCLqBMvjNkR8iWCnimR4PxEOzpGrxB4IEqELNVmvXr3mzZsjNiS++OKLyXMVAOScqkOu0CyqkbeR4Ww3e7Hy44UsEkUePHiwWaTrrrsuYJFodNciRYYoKJeuZlNnIZs2ZQNUBFNMYXFzGBxUrFOnTtrJ7LfffiNjKDhfR2cVfUVOLguLK/VJTLX99tuTeaoI70Z5qVUMuDvtNls1RioRQJ15D24Xmn3MMceQ8/DK1RTCpk2bRCPVFQLD0k+NIeGI+Z+/OpJAnFNdPPgF/sfkYqAQWhHayC7gQqCA60UhMyLlgQEHz5d1DCKXTFuIzvmZc6P/FAFgplFyt/eoQ4cOLhddv349LoSAwG6ADUKodtppp+XLlysFF2VzGgFWgDcQkesnptydtYWFSjLSpaEePnTDDTeoWW+66SZSsDt2DwHNQQcdZM4SgWnRogX3QF+VohA8+SwR6HT9+vXN8RAN4/uNi6KZMv3wTKjd4sWL8VhYcPTwueeey2w+JxArmfF3lHHfT0Xh6fX/tGnT3D1j5LwJj3JmksbCdhP0WwoeOsBFiRKsoxHLgp/mBuOWIgzuxEKKBtGy/Wbmzp3LDTSx9SJPmDCB4Alh0M9JkyZxQ4MGDbK9EF4BdSHR5aJ33303Hsv1cD179lQgpZ/otRYcEiWor5e4UPvvmbCVOpJwUTieyCTlUpSm6RiYadRBBFVKhMwgdbrn9NNP5zZUDB9P1SHGtJG79w9mWlFaybkokYde5Y6coAg4bK9IEUrORfkHmeeRXXfd1e1apgXV+sXiooDsZZxVrBASlCiwOyshlF6usVNJiHFRr2gifXiOLmpCHKbOyrfffpsU1NnuySmNCxYscCM/z4/+3cjPi5L8sgSUxt2sWJIAVqxY0a5dO2noxIkTMYyotoZwsW9mMLESNpXDrIRGVLxYlZfYE7BmNp++DtMgBbrlZlK7cxnV3LhxIzpFyGg3YMO54amnngoXUGfDcJWWItynFJAl+RpkBqJid8p+qi8GOcHFZPy1zT169CC65evYcDFSAn1qwCqEmBuiCO1BCzTiFF8t2erc8827u0uT/KD12mTzaOTQHglLsmYi2LKCm2++OXCDRoFs8AGLDdEKOKOwE8cuYVerV69uNl8fqlu3LvXj+XRdeyDzNt0gG2LmhQdPPPHEcJO5zbHnnnuiIISwBKmQ2Izfm2wSFV9dyBUOSKPWni/SYlbKcJISPfjgg8qDne2kFQR4OppAg6gQSFKaNWtm74nPVRgKOSzyxDpBnGLseYz8hC0SssHLaRr9DFskGTqzSIEQBSUVFfdyefAYbYoEmk5zuDorqTv88MNtdBqyl8m1dChSXAn41eMJKdWZcDIC8Ock1RhWIqme7eYNAf4djfaWDzw79tPdWkJsC2HDkGoI0AyOqKnmtqBN/G9j1GgBP8tsulABuShloCTu1CwDNED821KmT5+Ot6BG3n33XeIzAsd0UDQnkDkMOhGzmzhq1CiXi1599dX8DPRtYMplKTzfZ+DykchfivDEE0+oE1Q3Y5722GMPmyjy+eefJzlxjtfykqZNm1oKn5Cx009t2hnoyJ88eXLG7zhX6FMsLvrJJ5+UK1fuvvvucxPPOeecjDNHFxnjp+J7F1jPTGh9muJst7DkxGbdQFPJvFWaDLeRnBicdtppNWvWdIcR5KLM6D/22GM1atT4xUHXrl254fzzz9cN4QD6wgsvRAzcR3Q4x8MPP+z5k1t23HFHBMPuR7nOPvvsvn37Znsh0BpF46K8pEqVKh06dHDvwaIRquK8bQYO9/OU21FNed1orNSRhIu60wKpq4CrU0O7QbnCOGrAfdXQoUNJDEz60phqybkoLYJE8Sq3ho8//nid1FKKXBT51Ck4pnrEmsibhvSLy0Vlbbp162Ypsi3uETVEse40TjHGJFzUJY2eH75Y1J5EGqWSbuQHydlyuCjhL5+mcswUjB492ubd9enTh6u0mt1PM2m5L2Gol91KaBQlm8pbD6MXJfaRXFQDd5ZJAv3atWu73plIsVWrVtlm6hLalvMRmBaOtGOrw/ZTcwVVOZUrVw4M65EI9dXP/v37Z0KLn+OrJabO5QdxlAE/aKO42Tza0UcfbSlhSdaeYTa5BlrFDYMHD7YbAlzUi3JGkU5cg2xmn1EofnKn3SB7ZYZRfIA6tBtgLF4WiMy4u8TB6pVVyWTO6jr00ENxvu474R6nnnqqNgFJUiJl+JRTTrEbiJLFTt2nsMCovP7Pmasw2rRpg+c1MevSpQv3f/DBB5E3x8hPpEVC5mFlMRYp3DsWGaLkVOd4bQoDMd5ll10CiVB61zIn4aJelthJZ5UZcwbVq1enHlRv8aYvrERvvvkmdWtdEspYTE9KCgRY5Ounn35Ca/gfYoXMIG+B9Y/z5883wkmQD1MlJsEcrVu37qOPPuJSmY0/F4qLfvfddxSDyClMKakdLlFmW36g9VqB+c0uU00RCfWNud7FC+1dVL9+fX4GptfLie66666eP2rB/23btv3b5jj55JPVQOrKxZo//fTTyfMmz+12dwVWRV566aX8DK+K2XnnnUnXFOJicdErr7ySmwPrGwPrRRFIflK6wLNyCQF7qpo0hwopNTe5aNGijN8l/7cQ0OSYTOKceBCO4SYGaqZTp04Y7vCbKaCbMTeAJjqsV69e+JEHH3yQq/LHWJZsuYqMyF966SU3MpgwYQI/3fFzQVRz+PDh+ikuyrN2Q6G3j0q4XtRSNN4rli4gpYF7CMdJcSekef74T2BGlldKexfp/xEjRmT8PWxxD54/6BrolCkVLgo6duyY8adi6uWQUhPy4nJRFKeaD7MwxK8ZZ6QC6hvonlf9J+GiAX1UM6mvJ4k0buFc1PMHYTJ+95yt2DFozM1m5gtwfhLVhZTNSqgsOVXeixL7JFwUO4NrKFYxESdCSTclxn5q4I7PcQOfdp8iIpdwahRr4MCBGX+OrntPfLV42es8xg9quUo2j+a6p7Ake87pFLNmzdKsJVyqXQ1z0bAzinTihI/mxL0iLuquhgjINq5HE0A6d+4cs1JUiNy7SFPc4ZM5q0uk8c4778z2/iQlCnPRSDetycnqI87ZiJHQSCB/X331VZ2SFd5TwJBNfrJZJE1wyGaRwlw0MkSJV+ec2hQArZ/ZfDBZuOuuu0g/44wz9DMhF41sFHFRd4FxQM5jTF+8Ei1btkwRKW+Iz9i2DIg98artvAOZV78A9a8UmwiAWeOnyYkWSxrKbIKuVzguSoxFSbSFSQCalOwOLxAiUBczZsxQfYnH2iTmFNmgo0RHjhzpJrpcdNOmTZoYo5kSBupZoe2KFSs0TBETTNM67du31/1HH310eA16JHJyURmjML9t2rRppmjGV7G4qDYjVRxvKAkXRZ/xi9APVQ5RjjEBjRnmwa90lOjZZ5/tJgZqpnHjxvEOIBBkqGMyZudkRf8xDZeEi8oBuFOsBfVw22yrrYWLulwoCRfFFyIJNWvWDLy/FLko0ZJW23bp0sXzx2/vvvtuXSpdLkpMo7eNHTuWCIwKtHk4xeWiXtGkX50vh8Fv0KCBFmHKwvPRwJmoJeSiaqYk0rjlc1GaVfMXypUrB890CUkkF9UCXY1Cx1uJnCrv5cVF5TiSnCHkIsxFc9rPSC4KtP5cE/4juWhO45mtznP6wby5KKCkF110EToixmizDb0EXDSbE1+zZo05cS8BF/X8EWxVIKQU4hG5haEQyUXV960aiK8u+Q53coSLhCUqFhfVzN6cjRgJKDGahR17/fXX1ZUWM4snm/xks0iappvNIiXkovHqXNxoRHNcGzZsGEjXbFub91tQLhpj+rIpEQSBO4cMGaI+C5thh+s/YHPk7Y7/GMB4alIu0QXxsP6fPn26du0JcNGFCxcaF0WJNCg4Z84c7fWz1Y+LEhyLi4cHRUnRyGf87kzajDjhTjDbLDB84Sjc5aI4m8qVK2eietQqVapEbI3Udu7cmRtybkeEq4OYcScPRm7xF0BOLnriiSdmorpOla6ZscXiotrtA6lzE0vCRb2iRTiYP0T60EMPtfQxY8aQbmtHk0M7VbrTurxQzdStW5eIIeZAo0CQsWTJEn7GbEQh/+rOm41/oRDgooMHD+ZneEhE6bYg54/KRQmbRNICNq0UuahXFF6jmLhbd2lW6XJRK+BBBx1EfNmqVStLz4OLzpw5k0eOPPJIz6/bkSNHaqZ9r1694H7169cPSHKpcNEk0rjlc1HPj4OvvfbaChUqZPyRanN5kVxUK+gwR14uK5FT5b28uOjSpUszm89TTYIwF81pP7Nx0T333JNS6/9ILprTeHpZ6jynH8yPiy5btqx169akK0uao1ssLhrjxMuXLy8n7iXjop6/Y5BG6uQyslVUJBd99913M0UdqfHV9fjjj2c2nzDsImGJ8uCiCYMZF9xcr14969DXHN34FSWR8pPNImlieTaLlJCLxqtzcaORDz74gPurVasWSFf72jSWgnJRL7vpCysRUgqlx+xoPF8ZMy46bty4SzbHlnZabxkDXXAnpaJu4lPU248//hiYo7tgwQLbSle32fHjOtwkcKR54VAQLqqRz8jh3RUrVoSLR5Vp4yZLEZXPufRuG4fmVLRv395NDMzRhUFlnCmUgrq3tSZBtrJ79+6Bl69atUpHWdiYCXxMtj683jKMnFxUu1zahBCDxkVls4rFReVibShJKCEXRXvxjviq4T4sXVa7UaNG4a7lwChQADYNyQ0CAjVz/PHH83PixImBZ9977z13UZ8FGeRhu+22w6bbrg+GCRMm8JfgNZKxLFq0SI8k4aKvvvoqP2vWrBkgYxqJsqWVf1QuCjTDLbB2oIRcFOvv6siaNWs0cAERtT14vHy5KI7HVnwRqbiRJaqtF/Ih2yrMy4uLekULjQhxCLM2btyIQFItNWrUGDVqlFsKoVS4aBJp3MK5KC7PXCSFkqG21Y+RXLRv376ZooN/YqwEBc+p8l6+c3RhleXKlXO3YbfvZitpmIvG2E/NlInkoiTyadsxLpKLxldLTJ3H+EHN2MyPix555JFYZpsgmgcX9bI4cY0imi/OyUVpevsK6q/t2QJL4g0x46Kq8PjqmjFjRsZf1xM4d4Sf4p9JSpQHF83ZiAFgt3feeWd3tmc8F42Rn2wWSeOi2SxSQi4ar845tSkAHRyaKVoJZdC4qJmgwnHReNMXViLZPWvBABdNEYCWgLodPdqUiL+2xa51c2uz3M8//9wu2b6D2gMJlM0JOgXhotj9bBN0NfIb0AFki8S3335bamxVEHkgVQqD5trh6d1DsbTXnM2ZfPjhhzOhtQFTp04lUduiEA1n/JkSrvJjRDp06KA50oEdCORcc+4slZOLzp07t2LFipAod8vNdevWEbVcfPHF+okIZfx985LUhiawwRtdmqct6W2/uOJyUQBbzvg7Obmdbdyvda29evVyb4Zgx28yTDSsgw10/ICA7cg4c2OgDeKrbl8MTay9pjy/IzCz+YYxbdq0IYUozd28/oUXXrjllls8f+WhtqsRNRVQrs6dO2d7oRfiooQROucmMCqOPDRs2NCmfCThouh7eG/tvCEnZ/swBVCKXFTnW9gO+4L2LjJLpc3Dk9tugkI3NPH8faoz/tCoaz+lTZnNd9Ly/G2BYrgoYZDNO+jTp88ll1ziXlWnj+0EIyiiRVoS5l+QkaEq7HNaWgaXcM9wEsL1r91ltF2kkJOLJpFGhbbkwZQChRL9tvsjJb9sgA2xs4X0s3LlyjYoEclFDzvsMBuTNCvh1jBWolOnTl52lXd3o8mPi8oeEgi6dnvEiBE6QTQSYS5q9jMwdIb9lIRHctHXXnvNpU+RXDS+WmLqPJsfpLwKoJNw0YAka3eASpUqWVAujmcbqwKJsbvNeNgZRTpxbS4qJ+4l4KLYZG2xKygGyLbBbCQXpbH23HNP+cH46kI98ZiihUaQaFNMkEqapER5cNGcjRiA2LXLRbXvbvicZ3tVNvnJZpFwyjEWSa7ftUiRIUq8OufUpjDOP//8TGh1K2KJrFrUoUkQheCi8aYv7A60U7dx0Xnz5inaic/YNouvvvpKBEqRMLG6GJlogpZPak9ZVBJ5M7KmKau20Zo2PcJQJDmrtuQofS6K1qkiIpVf+zsFdvcigNMpN++++y5ap0W33BmzniGFoH1i99lnn2nTplHzH3/8sXZHxCxi0xUTa+9724WM21q1auWaeK3vwgydeeaZOKFBgwZh383lH3LIIe7BUNwT5nJhaOaeG2eLObunpChu0Oo44eabb65bt66tE0YHdFAVxBUC42YjDOw7z/JCyou1oph4Gs0rJmTX4I+8XdiKob0ZfxVN+LU6TMLosYEwUfSA0I0QfNiwYcTB4a0LwtDWo5RrzJgxWGF8s/wftJzKxwH8+OOPuPyM31166aWX4rbxMfXr1zcnoX5QKPr69esxJbNnz6ZutQIHz0EU++CDD8IJaWXrj9eivow/ij548OAbbriBF9qa7fALPX9Hyszmk47QSjKJgFmnGu6BKNMdrNPSYndwWBTOTob8/PPPySqEPGYzieRAwjXd68ILL4y8QSIxY8YMS9E+uu74uTZodfsRtdF/ICKZM2eOJhRdf/31hD40E5GczpmAQGqWi848bNSoUfwsQcMdd9wB7XSPREfO+Yp1Ewg2jGmBmqB56bSIayrh+fgeHVprvX6ogBtGe0WbbSCEbqK2bwXhM9xjQCugO8RDFnxQCloZTQzfrPp3J+drNIPwCJ3FTFGxmnZetWpVt1xqJhuXTiKNig7RSojExIkTqdVq1aoR1UGc9FSk5JcNtO2T9ThQUsi8MStxUVrNennQKSrEhh8jrUSDBg2MgwVUHqFF5d1e4LDYi5+4ixHIFfKZcUb+eb80rk6dOvAc2rFdu3Zh82ggRhc9CJzxGGk/sUu6Ki6acSYC0EBQF3efUi2gcHldzmqJr/NIP2jdatk8mttVKkmG99JqqCqaKPtAuQgER48e3bp164w/ORaLJBXTQC4WGyWSMkY6o4ATx7wcffTR2kZIwKBl/NM4LcVdXez5XJSWNYXCpdIokXvbeEVc0XZu93w6BGVyiVZ8ddkhVbRa3759uYqquucD5yyRlkG6PSPadCdgFnRsm23jHJ+rAAg7lUmMA46Jm0V7/vGPf7izRQzx8hO2SJMnT8YiufspuhbpmWeewRjKIlGxeipbiBKvzvHaFMbKlSuhi7BiiwGw2Dhl1y1qDld4i4QAIsVVHVg2BYOK0qwi9UTEV2NAiYgTEAxS0B1oEhWl2XlII+Y63eI0DDtNE8GjfUVEEXV5ZyJMMcxZs2ZpUq6NAmpAlUsEM1y1taNlk+3S56JaLOrOSHYhzhmeTIhuwKZs+6YPP/ywbMaFt3bg6a+88kqFC+XLl8dV33///TvttBMEj8hMJluHp+Ob4SfoOdzg9ttvd605stu1a1e9JOMPlbhzVFq2bIkv79evH6bziiuuwIXk3IUP6dfIkgJ3rBVaoTBdhtg2LXj22WdhC9wML73gggv+/ve/B+b6KzjGWOOlAhN+wtDiHH2FgGngwIG8kPcTr6CT+Huomq726NHDBjDHjx+vcUVRmsA0SAC10Ml1AQwfPlwWVpYxMOMoBnh6Hc9AuahtcgL9IKQjJxJ7YnHZX4FL7vCFV7TzE2W0jm2sj3hXxqe1PXv2dHdUp7kJCPCLuoE2DUyhd19IPDd06FB5TV5F01vnEdWImzzwwANJpA4RBtssitahEXUa4V//+tennnqKFB2iTQqPaLkLpg1Bxe2VUMFxVEQMIo0Z/yhC2s7tNsa5EitbeaEflAv51yTYvffem2gJm3PZZZfpHpw3KXg7hFyd0DA96sEdwsV2a8eFjH8IOPEKAT0RHqGAbJoioczmx4RG4v3330dJpXR8yB2goCB2CA0Ba+/evTXIoI9ec801uBNERRN0BVqWEJzwonr16pao0zjHjRtndyLnNjaCWUDGjOqgs4Q7ohkyAtmGmiNBVWsQ3oCdCSxwWrhwIffoWEuYzL333qv+CIpDxJPxh7OoUmqmbdu2ygYRCQGHzkNXCnm2ExdipFGgfbUdFMAUoBFUYPPmzYcMGWImKKxKZQONZhx88MHYDUIuQkwsuZllcVHECVVCTk4//XSyHQgLwlbCnUkRo/Jhsfd8rnL44Ye7RhsvrIVqyontEE42mjRpYoKH1mfrOMePWFMihIGOj4D9dM8sFRfl5TgFHEf37t2hNDfffLPqh3bs37//Lrvswj0IPHbebfeYaomv84AfxOzbUEy8R0NDJU6uJMNDSLnvvvswd9LcRx99lAzI8qMdOnqe2Fo9XPgmcp7NGblOnPJSq3fccYflnBaU8ad0d911F7wONRdJI0Wj67QvZuSkk06CEFJ82t2dmxMWTqwB9x922GFUEa1A8wWO7YmpLmHSpEmqDel7eGfUmBJhyTVuT+WQjnUlYtYu2Rl/K2AMLGZBM2Azfge0vp4zVwGoN18WD8NCgKpe3chFH/Hy4zkWice5RK5slEmIt0jZQhQvgQeP0aZIrF69+txzz0VI+BBRVqtWrayjgW8RRtL0ehut/8gjj0S+JCyuqIbRZsJRPCYpZkZoQUKp+GoMKxHap4FfogvcH3GFlJEQxZ0SmMKwZs0aUVCBdnGXEaE4dnAJlyxQpAnmzp1rlzStt2wGRb2Cni9aXFDmH374YcWKFbLRKZID34NhEotDCrONycAoIo97tZcQ9oW7CRQvIq8Ykch51yUHVpj4Jtu8XzQnsOFePKgHakOVkJM2J0F8qXE2xDp5jOFjRvVmshq5ZTQs6JNPPomczoqyYCbCQ4vLly8nPRtpp4ap58g6yfbCSKChiEreA5uU2p29s9WBSrbYN6wvVC9evECassUC0x3ofHSnHeYE8oBk5jcRJl4a0QWumn6FV/YWS/JLF6oxXN7MmTMDam5zdMk/1ixmq78YK+EVqXwhVrtQk9Sb9WXkjUj76c7RRZASbt7uIlu1xNS5kM0PJkRYknFebv43bNgQ6FgkM8m3xoh34jHQQm4AN6CAOTt2BcKJ+JtzVhcZji9d3iWKQbEacdGiRbZfi+eb9JiwIaf8eCW2SDHIqc7FjUZQNF7oTswpG8RXY1iJqFIL6rwi1lRmNGlrBFVEJEwN8zccWmO3ETwuhUUF+UQeuBo5mlg4bEFcNEWKFCm2dnz00UfutPMUKfJA5HrRbQfZ9tFNkSJFihR/PKRcNEWKFClKB++8887FF1+ccMwhRYpsSLloykVTpEiRYhtBykVTpEiRonSQrnJPUSrQ+lj38I9tCnacbxnPE0uRIkWKFGWPlIumSJEiRYoUWwTWrVsHBd1zzz133HHHOnXq9OnTJ3C20B8er7766kknnbSjj/bt2weOjE6RIkWKFH8wpFw0RYoUKVKkSJEiRYoUKVKUNVIumiJFihQpUqRIkSJFihQpyhopF02RIkWKFClSpEiRIkWKFGWNlIumSJEiRYoUKVKkSJEiRYqyRspFU6RIkSJFihQpUqRIkSJFWSPloilSpEiRIkWKFClSpEiRoqyRctEUKVKkSJEiRYoUKVKkSFHWSLloilLGpk2b/v3vfxf6TLyNGzeOGjVq7ty5kVe/+uqriRMnDho0aMSIEYsXL/4dc1K6WLJkyaOPPpr8/lWrVo0ePbokX/zhhx8mTJjw3XffleQl+WHt2rVPPPHE+vXrY+559tlnX3/99TLL0raM+fPnP/fcc793LjbD1t76P//88wsvvICxirnno48+QuV//fVXN5FHHnvsMTdl0qRJWN2C5LIIv/322/8c/PLLLzE3k2H3Zn5S2P9tDlIin3Xv3LBhQ3yufvrpJ7uZ/5WI6XjllVfWrVuXX0m3ZUTKW2kBEXr77bfff//9krwEp/bII4/E3/Pqq6+++OKLJflKThRa49AC4op58+YV7hMpUmw5SLloilIDEdKVV15ZpUqVTCZzzz33FPRbTz75JF9p0aJF+FK/fv26dev22WefTZkyZZdddtluu+0++OCD3yUnpYixY8c2a9aMD+24445J7p89e3abNm3KlSvHI/FRYza88847p5122p/+9Cfe8Mknn+TxhryxbNmy888/v3z58nz666+/znbb8uXLuaFChQo//vhjWWZvW8P48ePr169PVR933HG/d17+f2zVrb969eqLLrqocuXKFOHNN9+MubNevXrcM3XqVP00O4Bls3vQEVIqVqxoZKwQWLNmze23337wwQdnfHTp0iXm5htvvFG37bbbbjfddNPSpUufffbZ008/PVOEzp07kxL5LETiiiuuwG5zG/bnv//9b0yW5G5A+/btEVSlH3HEEaQ0bNhw06ZNJSnyNoiAvJUiEAmElpcjRfm9wXVqMbf973//k+8oXBdqGWjcE088wSeOPPLIAr0/RYotCikXTVHKOO+888qAi0JXOnToMG7cuEB6nz59WrZs+dtvv+nnjBkz9ttvvzfeeKMUPx3oM86Wk1LHl19+mZyLgvXr14tJ5sdFPb8bu3bt2mXPRYVatWrFc1FwySWXXH/99WWWpVJEgUYeCoQXX3wxDy5aumUMv23rbX3h0EMPzclFR4wYcdZZZ7lDfLIDLhcF3bp1I9YPPFsIGYNVivsRiC9fvjzyHgL0nXfeWbc99NBD7qX999+fRBhFzg/B1fWGK6+8Mts9gwcP1j2YKTe9U6dOSv/444+TFSvF/4ewvJUievToURIu6jlOLf62a6655oorrsj7K2GEVSlS40oR33zzDXHFk08+WbhPpEix5SDloilKGf/4xz/KgItGYvXq1ZUrVx4wYEBBv4IT2rhxY0E/kQ3F4qJA/dB5c1Fw9NFH/15c9C9/+UtOLrqVYsGCBYMGDfq9c1EMIADF5aLjx4//17/+VYp5+B31rkDQOGE8F41EmItGokuXLoWoMb6+ww478DdbR8DIkSMPP/xwscFXX33VvdSqVSsS4Zk5v9KvXz99BZO+atWq8A2YtVq1aulDsPrA1f/9738tWrRYsWJF4mKlKDj++c9/lpCLekVOrbSylBAFUqUUKVIIpazSH2bBunXr5s2bF3lp2bJlenb9+vWzZ89+++2333333Tlz5vzf//1f6eYtRdngd+SiL730Ep++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G6WIGIH88ssvJ0yYcOutt2J5vvvuu4Jm4z//+c/jjz9e0E8AXM8777zz/vvvF/pDeWDJkiVPPvlkCV9SIPOSIkVxkXLRPwjuvvvuoUOHrlixAl5Uq1atjI9dd931L0XYf//9+al010/88MMP/fv3r169+n333Rfzfm576aWXSphJqBrZIJ/4KrJEVnM+gq1s3Ljxgz5atGhx0kknuVHmggULMllwxRVXlDC3CbF8+XL84oknnshHTznlFPzWf//7X/cGIvIKFSo0bNiQgpecG0ApCRl/+umn+NvatWt34IEHXnPNNQgG7dupU6cGDRoQM5Xw68UCTJIWP+igg9QilSpVotFr1qxZrVq1evXqnX/++QQTUCb3kfnz59944401atTQI4glj+yyyy477rhjkyZNaFMYTuArRHukv/HGG2VXsLxAbXTs2JEKITQfM2YMIkG5vv322wJ9buLEiVQglVag98egT58+tBdfR83L8rvLli274IILqFg+TVhclp8uOX7++eeePXvusMMOZN5CTCwJP6tWrYrWl+K3Aq999tlnMQ6knHDCCaX4FfDoo4/yWox26b52S8Pf//53ignbDKTPnDnzuOOOe/HFF1H59u3bc891111XiAzAl3A9f/rTn/hEwPuULrIJJD979ep19dVXY8AnTZq0/fbbY7qTdzfngb333puc4HkL94mBAwfKE91+++2F+0oemDp16mGHHUbGDjjggJK8p0DmJUWKPJBy0T8CLr/88lGjRtlPYguF8vjCwJ1YMfyEcZLx48fjP8RR47noqlWrTj75ZEIWwov4oa1sGDBgAM7ygw8+0E9oJDnp27dvzCOPPfYYGfvwww/1E9bRqFGj/fbbb926dUoh8zvttBOxznkO2rRpw1Nh0lIsFNc6H3nkkXz0k08+CV+CfgwZMqTk5p5odcSIEbC4c889d8OGDfE3/+1vf3OZecuWLefMmVPCDOQH6kR5sAj7l19+eeuttzp06FCuXLndd9893Ll7zz336BGjapR33LhxzZo1I/Gvf/1roJ5/++23zp07v/baa2VQnLzRqlWr7t27209KjSR/9dVXBfrcd999d/rpp6NBBXp/AAHxhhOWnIsmVJnAbQpStzouKtBkrqYg2BdddNEtt9yS/A1JKi38WvhSqXDRwNeXLFly2mmnPffccyV87RaOKVOmQAXnzp3r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d+2111arVq1Zs2YzZ860Q9jlM844g58QuV4Z0KVLl6OOOspSYkacamD+7G9/+9v1ASlDcPyEux9//PFPPPEE1nOjjTbac889/aAEF7XbbrthPfE3Z511Ftb/5ptvNvn99ddfd+zYsWbNmtwL03niiSdyZt26ddls3749xuuEE07YZZdddt55Z/bstddevmjHyBLjXn311f379z/ooIPWW2+9f/3rX+4o92rUqBH6Crt54YUXcjQp/RhKHvDSSy/lFrVr17bn5UGwBRdccAF7eCIyhH84YYsttrBfYTJ23XVXCujVV1+98cYbeajTTjtt/vz5+cDNkO0mDIiounfv3qBBAxLDJv/QRrj+tttu27x5c3whpYkfTa8ztLKDDz747LPPJjjggq1bt7bVKfxCScnklUkP0RJ7+BWlQzZSUjyvHcIDnXLKKWTOlltuaXuIIP/xj39suOGGXAeL2bRp05122qlyAHUj/RlTSvODDz7g8UltlSpVCOZw9nfeeee666572223mQt8+OGHDzjggEqVKtFq8NAbbLABR+18U8XF5FI+iI+POOIIaj6WnfbFc3E0H6w6dsUVV3BBHsfOJGDt0aOHNRDbQ6xDXeXWXIH02OJS5Eb6o0XB8HIaBoGfYwEQOdYwCZTzwcIkpIFqQNDDpaiBLiyjXe++++6ciVmwCpz3pCA5VqtWrfr167O58cYb+7EIj48RoBkSlXbo0MGani3RnPJQITBNZIhVS65GAswvFpOAlDrGQ/G8/OSmm2665ZZbsAxkuJmCipqGQ6RL6E88RyLPO+88KrnTolhCW80LzABS9AR/9na3H+DiYffdd1+sB4b95JNPJof79u2bD2par169bAEVN65VZCZgLQ877DBSgmk6//zzOYHcbtOmDWVHrJ/0OKXV24Itjse/7rrrLNlklK0TA6b0khyc0bNnz7///e+IOixwy5YtDz30UHcoJUkFcympimK1+CENnDpJE+BBSJVdM9YPEt9jjnj20Gh/ikcoshCT7E8SSW7advIsVK0tAtjE7vm9IUmWJCmXUsAm46O5HUZ1//33p1CIbXgQwoyCpTZ+/Hh+QmaSpc8//zxuiPrArUNuKOkK6dYyxbAYvhaNbXpAfMVl8TW3BzRp0sTmT7lSS4m1YlmZmIcr8/idOnUi2MaX4dPx2q5/PKUtpxj5JLiXuV2snO2h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fvvtZZdd1qhRo0033XT33Xc/+eSThw0b5r93KoRYI5EWFUIIIYQQQgiRNdKiQgghhBBCCCGyRlpUCCGEEEIIIUTWSIsKIYQQQgghhMgaaVEhhBBCCCGEEFkjLSqEEEIIIYQQImukRYUQQgghhBBCZI20qChjFixYMHLkyPL7GJ3x2GOPvfrqq7GH/vOf/zz66KM9e/YcPHjwf//733JNxrfffjtw4MAff/yxXO9iLF26dOLEiZMmTcrgXgVZuHDhqFGjfvrppxJ+O3PmTIqvzJMkxGrKtGnThg4des899/BP9nefMWMGFjv7+66yfPXVV6u4gXr33XfHjx9f0akoS/BukydPfuKJJ5588kmebvHixez8448/PvzwQ3dOBhX1t99+GzRoECFE9NBff/31wQcf0E4JLR5//PFFixZVSDLEN998g6n8+eefKzohoiyRFhVlxptvvnnssceus846uVzuyy+/LL8bff3119yiSpUq+Cp/P96ia9eunTt3JqQbO3bsRhttVK1atXI16GeccQYp6dWrV/ndwrjppptq167NvW655Zbyvlc6BGonnnjieuutR2IoiBX67TvvvNOqVSt+uPvuu5dT8oRYvaBFX3/99RMnTtxyyy0rVarEP5ndesSIEU2aNKE9br/99pnddFXmrbfe2m+//ciQPffcs6LTEgMKrUePHnXq1CGF55xzTkUnp2zAa/ft2xfvVqNGjUMOOaRjx4777rtvzZo1999//3322eef//xnPsOKOnz4cO5y5JFHhvbPmzfvsMMOGzJkCC7v6quv5pyWLVtmnwyRXxZ03XHHHRWdEFGWSIuKsmTp0qWbb755eWtR7nL22WcTwIX2X3bZZa1bt3abL7744g477PDpp5+W4a1xnP7mSy+9dMwxx5TtLZLg6VYFLWpstdVWJWjRfDAEVK5aNFRAq+w1hYAXXniB5jB37lz+f++99w499NAS2tTK8Mknn0iL+g3cMiRLLbqi5qVfv35rjBbFHeyxxx48TpcuXfx8+OKLLxCi7D/33HNtTzYVdebMmccdd9zYsWP9ncQbjRo18sXPlVde2apVqzK8b6gOxCZDGBMmTCDoqpApJKL8kBYVZcy+++5b3lo0ljlz5qy//vp9+vQpv1ugOW+//fbyu346//rXv1YdLbrXXnuVpkX/97//lasWPeOMM1aLawoB7dq122ijjSowAYsWLVrLteiHH3541113uc1vv/02Sy0aunsxPP/882uGFsUX1K1bl2eJ9arUzMaNG5966qlus6Iq6ujRo7n11KlTy+8WZ555ZvldXIhVnzLWou8n8PPPP0+bNi32kL3Rt3TpUuLat99++9VXX508ebL1E4vVkYrSoo8//jj3HTx4cDld/6effqpfv350MDYzpEULMnDgQC6+6l9TCGPHHXeUFq1Afvzxx+222843qllq0ejdi2GN0aI22bJevXqhd20cEydOPO644+z/Cqyo5513HreeNWtWOV3/7rvvXn/99cvp4mIt5K+//jI99corr7z11ltE43/++WfonN9++83pLwdK7d///vfrr7/+2muvffDBB/Pnz88szWUZY6EnX0mAR+KxYw/Z63yffPIJ/7/88svkgv1DzFqGaVuDodqRXYMGDXrssce++eab0FEqls0gJZ/vu+8+3Jg7RIm8swzX58cVbE+65aVAn3nmGcL0CRMmhKaXxGpRrvbwww+TyDfeeCPaKih00sZTzJ07N7ToUdIhLvLcc88tWbIkH1Q8EvzPf/6T+3br1s091Pjx4x988EGqU+h2ixcvfvXVV++5554nnnhi4cKF0RwbHvDxxx+7nQQNBx10kEUAXJnq6g6RY++++27oIj/88MOLL77I83Kj6C34iS28xGmPPvooOfPLL7/kC+FrUZw06ecilgM+3O6pp54aMGAA+RNdW4jKcP/991N2hFxz5swJZYtVJP7+/vvv0QR89dVXDzzwAAnmFsVo0dh7+VoUwzdu3Lhhw4Zx5ejP0/Pw+++/f/PNN/PBO6jchRNGjx697rrrcnErfX9BqdgSpxDtTJLHJjnpao4z0CnXFGJloHVQo2rVqrXhhhta7fJnnWFUp0yZghWiucX269FIMRo08HvvvReTZTvnzZtHk8kHgTv/YP1oJnaIPVhCTp4xY4Z/nVCIP336dNcKnFnD2kdTGIXYhbY8YsSI2BEkSwAuA+tEGOQfItmETflgxQEsjH+U1OLXcAE8Y3QuK+0U48kJn3/+eShgoHVjFp599lnOSeraxqEccMABPP6FF17onKCvRWnvY8eOpRTMRIQgf4YOHcoJxURs2B+egr8kxpZdid6dR3jHw5wCni5UHElalGwkb0mSqw/pkEWUFyZu5syZ0aPcF+eOzeSE6BKABA9ffPEF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\", \"width\": 1241, \"height\": 1754, \"size_kb\": 420.8}], \"total_pages\": 16, \"rendered_pages\": 1, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/_pdf_images\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "5c3f277c-572a-4dd4-801b-ab856accf2a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Runtime record

_source line 1307_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] 紧急确认：当前 PDF 16 页，EMNLP ARR 限制 8 页正文 + 无限附录。  请检查： 1. 正文（Abstract 到 References 之前）是否 ≤ 8 页？ 2. References 算不算在 8 页限制内？（ARR 规则：references 不计入页数限制） 3. 如果正文超 8 页，需要立即压缩——告知超了多少，哪些内容可以移到 appe…",
  "leafUuid": "fcc1e5a3-ef77-45c7-9431-60fc8b9dd752",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e"
}
```

---


### Runtime record

_source line 1308_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze TF-IDF per-prefix results for ActorAttack",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e"
}
```

---


### Assistant

_source line 1309 · 2026-05-18T19:49:17.089Z_

图片太大。用 pdftotext 直接分析每页内容边界。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcc1e5a3-ef77-45c7-9431-60fc8b9dd752",
  "isSidechain": false,
  "requestId": "req_011CbAcZPX5LqUb8to8cEaJw",
  "type": "assistant",
  "uuid": "ee89dfb8-852a-4f64-b13b-6e7d06f8d667",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NuNefC26BFzzWKBZVNxwR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 573,
      "cache_read_input_tokens": 60207,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 60207,
          "cache_creation_input_tokens": 573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 573
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

_source line 1310 · 2026-05-18T19:49:18.581Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01G7L4nc93Kza5zoAzSpdBBx`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper && pdftotext -layout main.pdf - 2>/dev/null | grep -n \"References\\|\\\\\\\\bibliography\\|Appendix\\|Responsible NLP\\|Limitations\\|Conclusion\" | head -20",
  "description": "Find section boundaries in PDF text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee89dfb8-852a-4f64-b13b-6e7d06f8d667",
  "isSidechain": false,
  "requestId": "req_011CbAcZPX5LqUb8to8cEaJw",
  "type": "assistant",
  "uuid": "9921aa6b-87ad-42a0-ba00-2180b4a907bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014NuNefC26BFzzWKBZVNxwR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 573,
      "cache_read_input_tokens": 60207,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 573,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 60207,
          "cache_creation_input_tokens": 573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 573
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

_source line 1311 · 2026-05-18T19:49:18.775Z_

<details><summary>↩ Tool result · `toolu_01G7L4nc93Kza5zoAzSpdBBx`</summary>

```text
58:040   than their single-turn counterparts. Attacks such as         responses (Appendix A). Content-level reasoning          081
169:194   (Appendix A). Perturbation-based defenses such as
314:                                                                   per-K results in Appendix B.
337:371   baselines (Appendix A): GPT-5.5 achieves only                complex ActorAttack, TF-IDF collapses to F1 =                            410
350:381   sults in Appendix B). OOD results report 3-seed              1.000] vs. vanilla [0.203, 0.314]. Paired permuta-                       420
390:                 0.8                                                  pipeline. Full per-prefix results in Appendix Tables 8
538:550   results appear in Appendix C.
674:694   dant pairs; Appendix D).                                       Delight, the 9-class model achieves strategy predic-     745
805:826   6   Conclusion
841:854   7   Limitations
876:926   References                                                          2019. Fine-grained analysis of propaganda in news          980
1125:1221   mains (technology, health, finance, education, gen-            Responsible NLP Research Checklist                    1237
1127:                                                                      A. Limitations.                                       1238
1203:1269       (40GB). Section 7 and Appendix E.
1206:1271       ficient for reproducibility? Yes. Appendix E
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9921aa6b-87ad-42a0-ba00-2180b4a907bd",
  "isSidechain": false,
  "promptId": "bddd2ac2-53e3-403b-a1f8-035aa9a55c3a",
  "type": "user",
  "uuid": "55788435-6aec-480b-90b5-cfc4cd2b4e88",
  "toolUseResult": {
    "stdout": "58:040   than their single-turn counterparts. Attacks such as         responses (Appendix A). Content-level reasoning          081\n169:194   (Appendix A). Perturbation-based defenses such as\n314:                                                                   per-K results in Appendix B.\n337:371   baselines (Appendix A): GPT-5.5 achieves only                complex ActorAttack, TF-IDF collapses to F1 =                            410\n350:381   sults in Appendix B). OOD results report 3-seed              1.000] vs. vanilla [0.203, 0.314]. Paired permuta-                       420\n390:                 0.8                                                  pipeline. Full per-prefix results in Appendix Tables 8\n538:550   results appear in Appendix C.\n674:694   dant pairs; Appendix D).                                       Delight, the 9-class model achieves strategy predic-     745\n805:826   6   Conclusion\n841:854   7   Limitations\n876:926   References                                                          2019. Fine-grained analysis of propaganda in news          980\n1125:1221   mains (technology, health, finance, education, gen-            Responsible NLP Research Checklist                    1237\n1127:                                                                      A. Limitations.                                       1238\n1203:1269       (40GB). Section 7 and Appendix E.\n1206:1271       ficient for reproducibility? Yes. Appendix E",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9921aa6b-87ad-42a0-ba00-2180b4a907bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Tool call

_source line 1312 · 2026-05-18T19:49:22.165Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017dqV27LAzwFwkL4EnmvmGN`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper && pdftotext -layout main.pdf - 2>/dev/null | head -5",
  "description": "Check PDF text header format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55788435-6aec-480b-90b5-cfc4cd2b4e88",
  "isSidechain": false,
  "requestId": "req_011CbAcZmH2KDqMb4woCJGbu",
  "type": "assistant",
  "uuid": "3b4bf116-143f-4b91-a145-b811a2098a36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBVMgt2vZ1kkiqfSELFahY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 60780,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 624,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 60780,
          "cache_creation_input_tokens": 624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 624
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

_source line 1313 · 2026-05-18T19:49:22.259Z_

<details><summary>↩ Tool result · `toolu_017dqV27LAzwFwkL4EnmvmGN`</summary>

```text
      What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges
                             the Cross-Attack Gap


                                              Anonymous ACL submission
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b4bf116-143f-4b91-a145-b811a2098a36",
  "isSidechain": false,
  "promptId": "bddd2ac2-53e3-403b-a1f8-035aa9a55c3a",
  "type": "user",
  "uuid": "b9ef06a7-cba0-4b6d-b2db-918e227b79d3",
  "toolUseResult": {
    "stdout": "      What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges\n                             the Cross-Attack Gap\n\n\n                                              Anonymous ACL submission",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3b4bf116-143f-4b91-a145-b811a2098a36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Assistant

_source line 1314 · 2026-05-18T19:49:25.170Z_

用另一个方法：用 pdftotext 按页提取，看每页开头的内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9ef06a7-cba0-4b6d-b2db-918e227b79d3",
  "isSidechain": false,
  "requestId": "req_011CbAca2BDNp85FcGUArUqv",
  "type": "assistant",
  "uuid": "7cf4f9b4-e104-4309-8cea-5e60d3c596dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MrnMqCfxbxDy1YWWYoxhAG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 61404,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 233,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 199,
          "cache_read_input_tokens": 61404,
          "cache_creation_input_tokens": 233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 233
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

_source line 1315 · 2026-05-18T19:49:26.703Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018Lbwmqw2cYXgpHwWVAP7qi`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper && for p in $(seq 1 16); do echo \"=== PAGE $p ===\"; pdftotext -f $p -l $p -layout main.pdf - 2>/dev/null | head -5; done",
  "description": "Extract first 5 lines of each page to map section layout"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cf4f9b4-e104-4309-8cea-5e60d3c596dd",
  "isSidechain": false,
  "requestId": "req_011CbAca2BDNp85FcGUArUqv",
  "type": "assistant",
  "uuid": "fdfb1d7d-9f52-436d-9490-e8730c843150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MrnMqCfxbxDy1YWWYoxhAG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 61404,
      "output_tokens": 199,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 233,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 199,
          "cache_read_input_tokens": 61404,
          "cache_creation_input_tokens": 233,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 233
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

_source line 1316 · 2026-05-18T19:49:27.202Z_

<details><summary>↩ Tool result · `toolu_018Lbwmqw2cYXgpHwWVAP7qi`</summary>

```text
=== PAGE 1 ===
      What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges
                             the Cross-Attack Gap


                                              Anonymous ACL submission
=== PAGE 2 ===
085   coder adaptation followed by frozen BiGRU classi-            • Distribution-specific classification effects. All       136
086   fication, which we call DisPeD), we design seven               classification-supervised variants achieve equiv-       137
087   Stage 1 encoder variants: 9-class persuasion strat-            alent detection regardless of label correctness         138
088   egy classification, binary classification, scrambled           (F1 gap ≤3.9 pp), with 4–20× cross-seed vari-           139
089   labels, MLM only, topic classification, Wikipedia              ance reduction on synthetic OOD evaluations vs.         140
=== PAGE 3 ===
                                                                                              DisPeD: Two-Stage Persuasion-Aware Jailbreak Detection
186   factor for cross-attack generalization.                                                                Stage 1: Turn-Level Encoding
                                                                                                                                Evidence-based Expert Endors.
                                                                                                                                                                                                Stage 2: Conversation-Level Classification
                                                                                                                Treatment Pipeline
=== PAGE 4 ===
      Table 1: Stage-1 encoder variants. All operate on the             The MLM-only variant applies 15% masked lan-             304
      same training conversations except Wikipedia MLM                  guage modeling on the same jailbreak conversa-           305
      (matched token count on Wikipedia text).
                                                                        tion text without any classification head, testing       306

=== PAGE 5 ===
353   benign = 118 total. No overlap exists in attack              Table 2: Cross-attack generalization (F1) at K=2 and
354   templates across families. The OOD benign set                full conversation. 3-seed mean±std where noted. Full
                                                                   per-K results in Appendix B.
355   is IID (same generation pipeline as training); the
356   OOD challenge is in distinguishing novel attack                                     IID (Cresc.)                OOD (DD)
=== PAGE 6 ===
                                                                      Table 3: Evidence hierarchy on OOD DD and ActorAt-
                 1.0                                                  tack (AA) at full conversation length (3-seed mean±std
                                                                      where available). All variants share the same Stage-2
                 0.8                                                  pipeline. Full per-prefix results in Appendix Tables 8
                                                                      and 9.
=== PAGE 7 ===
506   MLM degrades by only 2.6 pp. Domain-specific                     Table 4: Cross-encoder comparison on OOD Full (3-
507   features are more robust to surface-level rewording.             seed mean±std). DD = Deceptive Delight, AA = Ac-
                                                                       torAttack. RoBERTa vanilla collapses on structurally
508   Misaligned supervision destabilizes generaliza-                  complex ActorAttack despite strong DD performance.
509   tion. Topic classification yields DD-Full F1 =
=== PAGE 8 ===
596   MLM pretraining (Liu et al., 2019b) tolerates sim-                        DeBERTa (IID)             DeBERTa (DD OOD)
597   ple attacks (DD vanilla = 0.981) but fails on struc-           Vanilla 1.000 0.442 0.393 Vanilla 1.000 0.797 0.649      1.0
598   turally complex ones (ActorAttack vanilla = 0.466).
                                                                         MLM 0.442 1.000 0.586      MLM 0.797 1.000 0.773
599   Bootstrap CIs confirm this encoder gap on DD:                                                                           0.8
=== PAGE 9 ===
      Table 6: Perturbation behavior under adversarial para-         tern does not hold. Domain-adapted variants de-          696
      phrasing on IID Crescendo (n=76). ∆: F1 degradation            grade substantially (9-class ∆ = −20.4±13.5 pp,          697
      (pp). On this dataset and OOD Deceptive Delight, a
                                                                     MLM −35.3 pp), with extreme cross-seed variance.         698
      three-layer pattern emerges (classification structure at
=== PAGE 10 ===
                                                  Crescendo                                                                 FITD                                                   Deceptive Delight
                                              (n=1818 transitions)                                                    (n=541 transitions)                                         (n=565 transitions)
                            None    32   62   31   32   32         31                               None    80                     80                               None    80                        80

                         Rapport         32   30   64        31                                  Rapport                 80                                      Rapport
=== PAGE 11 ===
813   sion and MLM thus serve complementary roles: the               ToxicChat (human-authored, single-turn) confirms        862
814   former stabilizes within the training distribution,            that DAPT’s detection advantage transfers across        863
815   the latter generalizes across distributions.                   data sources (+18–42 pp over vanilla; Section 4.5),     864
                                                                     multi-turn generalization across LLM generation         865
816   Encoder capacity confound. The cross-encoder
=== PAGE 12 ===
910   attacks do not challenge any variant, rather than as              Kevin Clark, Minh-Thang Luong, Quoc V. Le, and               960
911   a meaningful evaluation axis.                                       Christopher D. Manning. 2020. ELECTRA: Pre-                961
                                                                          training text encoders as discriminators rather than       962
912   Scope. Only persuasion-mediated multi-turn at-                      generators. In International Conference on Learning        963
913   tacks fall within scope. Single-turn token-level at-                Representations.                                           964
=== PAGE 13 ===
1015   John Hewitt and Christopher D. Manning. 2019. A                   William C. Mann and Sandra A. Thompson. 1988.             1070
1016     structural probe for finding syntax in word represen-             Rhetorical structure theory: Toward a functional the-   1071
1017     tations. In Proceedings of the 2019 Conference of                 ory of text organization. Text & Talk, 8(3):243–281.    1072
1018     the North American Chapter of the Association for
1019     Computational Linguistics, pages 4129–4138.                     Mantas Mazeika, Long Phan, Xuwang Yin, Andy Zou,          1073
=== PAGE 14 ===
1123   Mark Russinovich, Ahmed Salem, and Ronen Eldan.                 Table 7: LLM-as-judge jailbreak detection. IID: bi-
1124    2025. Great, now write an article about that: The              nary F1 (Crescendo test set); OOD: macro F1 (DD =
1125    crescendo multi-turn llm jailbreak attack. In USENIX           Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 val-
1126    Security Symposium.                                            ues exclude unparseable responses and represent upper
                                                                       bounds.
=== PAGE 15 ===
       Table 8: Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean±std where available. “–”
       indicates insufficient conversation length for that prefix (FITD conversations contain 2–3 turns).

                     Method                K=1           K=2              K=3             K=5              Full
                       IID (Crescendo)
=== PAGE 16 ===
       Table 10: Perturbation robustness on OOD Deceptive        C4. Did you report error bars or confidence in-                1274
       Delight (n=118). ∆: F1 change (pp) from clean to              tervals? Yes. All OOD results report 3-seed                1275
       paraphrased. 3-seed mean±std where available.
                                                                     mean±std (sample standard deviation with                   1276
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdfb1d7d-9f52-436d-9490-e8730c843150",
  "isSidechain": false,
  "promptId": "bddd2ac2-53e3-403b-a1f8-035aa9a55c3a",
  "type": "user",
  "uuid": "e0f57ac7-9fc8-4d03-a3ce-0777a139581b",
  "toolUseResult": {
    "stdout": "=== PAGE 1 ===\n      What Makes Multi-Turn Jailbreaks Detectable? Domain Exposure Bridges\n                             the Cross-Attack Gap\n\n\n                                              Anonymous ACL submission\n=== PAGE 2 ===\n085   coder adaptation followed by frozen BiGRU classi-            • Distribution-specific classification effects. All       136\n086   fication, which we call DisPeD), we design seven               classification-supervised variants achieve equiv-       137\n087   Stage 1 encoder variants: 9-class persuasion strat-            alent detection regardless of label correctness         138\n088   egy classification, binary classification, scrambled           (F1 gap ≤3.9 pp), with 4–20× cross-seed vari-           139\n089   labels, MLM only, topic classification, Wikipedia              ance reduction on synthetic OOD evaluations vs.         140\n=== PAGE 3 ===\n                                                                                              DisPeD: Two-Stage Persuasion-Aware Jailbreak Detection\n186   factor for cross-attack generalization.                                                                Stage 1: Turn-Level Encoding\n                                                                                                                                Evidence-based Expert Endors.\n                                                                                                                                                                                                Stage 2: Conversation-Level Classification\n                                                                                                                Treatment Pipeline\n=== PAGE 4 ===\n      Table 1: Stage-1 encoder variants. All operate on the             The MLM-only variant applies 15% masked lan-             304\n      same training conversations except Wikipedia MLM                  guage modeling on the same jailbreak conversa-           305\n      (matched token count on Wikipedia text).\n                                                                        tion text without any classification head, testing       306\n\n=== PAGE 5 ===\n353   benign = 118 total. No overlap exists in attack              Table 2: Cross-attack generalization (F1) at K=2 and\n354   templates across families. The OOD benign set                full conversation. 3-seed mean±std where noted. Full\n                                                                   per-K results in Appendix B.\n355   is IID (same generation pipeline as training); the\n356   OOD challenge is in distinguishing novel attack                                     IID (Cresc.)                OOD (DD)\n=== PAGE 6 ===\n                                                                      Table 3: Evidence hierarchy on OOD DD and ActorAt-\n                 1.0                                                  tack (AA) at full conversation length (3-seed mean±std\n                                                                      where available). All variants share the same Stage-2\n                 0.8                                                  pipeline. Full per-prefix results in Appendix Tables 8\n                                                                      and 9.\n=== PAGE 7 ===\n506   MLM degrades by only 2.6 pp. Domain-specific                     Table 4: Cross-encoder comparison on OOD Full (3-\n507   features are more robust to surface-level rewording.             seed mean±std). DD = Deceptive Delight, AA = Ac-\n                                                                       torAttack. RoBERTa vanilla collapses on structurally\n508   Misaligned supervision destabilizes generaliza-                  complex ActorAttack despite strong DD performance.\n509   tion. Topic classification yields DD-Full F1 =\n=== PAGE 8 ===\n596   MLM pretraining (Liu et al., 2019b) tolerates sim-                        DeBERTa (IID)             DeBERTa (DD OOD)\n597   ple attacks (DD vanilla = 0.981) but fails on struc-           Vanilla 1.000 0.442 0.393 Vanilla 1.000 0.797 0.649      1.0\n598   turally complex ones (ActorAttack vanilla = 0.466).\n                                                                         MLM 0.442 1.000 0.586      MLM 0.797 1.000 0.773\n599   Bootstrap CIs confirm this encoder gap on DD:                                                                           0.8\n=== PAGE 9 ===\n      Table 6: Perturbation behavior under adversarial para-         tern does not hold. Domain-adapted variants de-          696\n      phrasing on IID Crescendo (n=76). ∆: F1 degradation            grade substantially (9-class ∆ = −20.4±13.5 pp,          697\n      (pp). On this dataset and OOD Deceptive Delight, a\n                                                                     MLM −35.3 pp), with extreme cross-seed variance.         698\n      three-layer pattern emerges (classification structure at\n=== PAGE 10 ===\n                                                  Crescendo                                                                 FITD                                                   Deceptive Delight\n                                              (n=1818 transitions)                                                    (n=541 transitions)                                         (n=565 transitions)\n                            None    32   62   31   32   32         31                               None    80                     80                               None    80                        80\n\n                         Rapport         32   30   64        31                                  Rapport                 80                                      Rapport\n=== PAGE 11 ===\n813   sion and MLM thus serve complementary roles: the               ToxicChat (human-authored, single-turn) confirms        862\n814   former stabilizes within the training distribution,            that DAPT’s detection advantage transfers across        863\n815   the latter generalizes across distributions.                   data sources (+18–42 pp over vanilla; Section 4.5),     864\n                                                                     multi-turn generalization across LLM generation         865\n816   Encoder capacity confound. The cross-encoder\n=== PAGE 12 ===\n910   attacks do not challenge any variant, rather than as              Kevin Clark, Minh-Thang Luong, Quoc V. Le, and               960\n911   a meaningful evaluation axis.                                       Christopher D. Manning. 2020. ELECTRA: Pre-                961\n                                                                          training text encoders as discriminators rather than       962\n912   Scope. Only persuasion-mediated multi-turn at-                      generators. In International Conference on Learning        963\n913   tacks fall within scope. Single-turn token-level at-                Representations.                                           964\n=== PAGE 13 ===\n1015   John Hewitt and Christopher D. Manning. 2019. A                   William C. Mann and Sandra A. Thompson. 1988.             1070\n1016     structural probe for finding syntax in word represen-             Rhetorical structure theory: Toward a functional the-   1071\n1017     tations. In Proceedings of the 2019 Conference of                 ory of text organization. Text & Talk, 8(3):243–281.    1072\n1018     the North American Chapter of the Association for\n1019     Computational Linguistics, pages 4129–4138.                     Mantas Mazeika, Long Phan, Xuwang Yin, Andy Zou,          1073\n=== PAGE 14 ===\n1123   Mark Russinovich, Ahmed Salem, and Ronen Eldan.                 Table 7: LLM-as-judge jailbreak detection. IID: bi-\n1124    2025. Great, now write an article about that: The              nary F1 (Crescendo test set); OOD: macro F1 (DD =\n1125    crescendo multi-turn llm jailbreak attack. In USENIX           Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 val-\n1126    Security Symposium.                                            ues exclude unparseable responses and represent upper\n                                                                       bounds.\n=== PAGE 15 ===\n       Table 8: Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean±std where available. “–”\n       indicates insufficient conversation length for that prefix (FITD conversations contain 2–3 turns).\n\n                     Method                K=1           K=2              K=3             K=5              Full\n                       IID (Crescendo)\n=== PAGE 16 ===\n       Table 10: Perturbation robustness on OOD Deceptive        C4. Did you report error bars or confidence in-                1274\n       Delight (n=118). ∆: F1 change (pp) from clean to              tervals? Yes. All OOD results report 3-seed                1275\n       paraphrased. 3-seed mean±std where available.\n                                                                     mean±std (sample standard deviation with                   1276",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fdfb1d7d-9f52-436d-9490-e8730c843150",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Runtime record

_source line 1317_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] 紧急确认：当前 PDF 16 页，EMNLP ARR 限制 8 页正文 + 无限附录。  请检查： 1. 正文（Abstract 到 References 之前）是否 ≤ 8 页？ 2. References 算不算在 8 页限制内？（ARR 规则：references 不计入页数限制） 3. 如果正文超 8 页，需要立即压缩——告知超了多少，哪些内容可以移到 appe…",
  "leafUuid": "e0f57ac7-9fc8-4d03-a3ce-0777a139581b",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e"
}
```

---


### Runtime record

_source line 1318_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze TF-IDF per-prefix results for ActorAttack",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e"
}
```

---


### Assistant

_source line 1319 · 2026-05-18T19:50:03.852Z_

<details><summary>Logged reasoning block</summary>

```text
Let me map out the pages:

- Pages 1-11: Main content (Abstract through Conclusion + Limitations)
- Page 12: End of Limitations + start of References
- Pages 12-14: References (starts on page 12, continues through 14)
- Pages 14-16: Appendix + Checklist

Wait, let me re-examine:
- Page 11: Still main content (lines about "former stabilizes within the training distribution" and "Encoder capacity confound" - this is in the Conclusion/Limitations section)
- Page 12: Lines 910-913 mention "Scope. 

Only persuasion-mediated multi-turn attacks..." - this is still Limitations. Then line 960 starts References ("Kevin Clark, Minh-Thang Luong...")

So main content (Abstract through end of Limitations/Section 7) ends partway through page 12. References start on page 12.

Looking at the LaTeX log more carefully, the bibliography starts after page 11 ends, then the appendix begins after page 13. The PDF text shows page 11 still contains main content, so the actual page breaks are: main content wraps onto page 12 before references begin, and the appendix starts partway through page 13.

Tracing through the page boundaries, the main content (Sections 1-7) spans approximately 11.5 pages, with the conclusion and limitations finishing early on page 12 before the references take over. I'm checking whether the Limitations section counts toward the page limit in ARR/EMNLP format. According to recent ACL rules, the main body is capped at 8 pages while References, Limitations, and Ethics Statements don't count against that limit, so if that applies here, my main content should fit comfortably within the requirement.

Now I'm mapping out where each section falls across the pages—Introduction runs through page 2, Method spans pages 3-4, Experiments take up pages 5-8, and the Discussion/Conclusion appears to start around page 11. I'm tracking the page layout more carefully now. The main body through the Conclusion spans about 11 pages, which puts us 2-3 pages over the EMNLP ARR limit of 8 pages. The Conclusion starts partway through page 11, and Limitations begins right after it on the same page, so I need to figure out exactly where one section ends and the other begins to get a precise page count for the main content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0f57ac7-9fc8-4d03-a3ce-0777a139581b",
  "isSidechain": false,
  "requestId": "req_011CbAcaPLSKcEHVg6kCMhjs",
  "type": "assistant",
  "uuid": "9f134f51-a87a-4307-8c3c-9ccad561d4ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qvu6ZhZHbjPiCVc3SHmu7N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2367,
      "cache_read_input_tokens": 61637,
      "output_tokens": 1863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2367,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1863,
          "cache_read_input_tokens": 61637,
          "cache_creation_input_tokens": 2367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2367
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

_source line 1320 · 2026-05-18T19:50:04.048Z_

关键发现：正文到 Section 6 Conclusion 约 11 页。需要确认 ARR 的 Limitations 是否计入页数限制。先精确定位各 section 的页面分布。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f134f51-a87a-4307-8c3c-9ccad561d4ab",
  "isSidechain": false,
  "requestId": "req_011CbAcaPLSKcEHVg6kCMhjs",
  "type": "assistant",
  "uuid": "f03edeea-858a-44ce-bb4e-1aeed96c6c32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qvu6ZhZHbjPiCVc3SHmu7N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2367,
      "cache_read_input_tokens": 61637,
      "output_tokens": 1863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2367,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1863,
          "cache_read_input_tokens": 61637,
          "cache_creation_input_tokens": 2367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2367
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

_source line 1321 · 2026-05-18T19:50:05.675Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RiQPePkxxEmjqmPMatrcSy`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper && pdftotext -f 10 -l 12 -layout main.pdf - 2>/dev/null | grep -n \"Conclusion\\|Limitations\\|References\\|Section\\|\\\\bA\\\\b.*Appendix\\|^$\" | head -30",
  "description": "Locate section headings on pages 10-12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f03edeea-858a-44ce-bb4e-1aeed96c6c32",
  "isSidechain": false,
  "requestId": "req_011CbAcaPLSKcEHVg6kCMhjs",
  "type": "assistant",
  "uuid": "36b47033-5fe1-4e88-81a2-2cfce23aecbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qvu6ZhZHbjPiCVc3SHmu7N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2367,
      "cache_read_input_tokens": 61637,
      "output_tokens": 1863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2367,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1863,
          "cache_read_input_tokens": 61637,
          "cache_creation_input_tokens": 2367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2367
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

_source line 1322 · 2026-05-18T19:50:05.790Z_

<details><summary>↩ Tool result · `toolu_01RiQPePkxxEmjqmPMatrcSy`</summary>

```text
4:
8:
9:
10:
11:
14:
18:
20:
58:
59:
60:
66:
67:
69:748    tection mechanism analysis in Section 4.3: all three                                                                        thetic OOD data are generated by Qwen3-8B, rais-                                               781
83:
85:
87:
105:
106:
110:815   the latter generalizes across distributions.                   data sources (+18–42 pp over vanilla; Section 4.5),     864
127:826   6   Conclusion
147:845   derperform pure MLM (Section 4.5). DAPT’s de-                  tion.                                                   894
150:
152:
154:
156:
158:
160:
163:854   7   Limitations
172:
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36b47033-5fe1-4e88-81a2-2cfce23aecbf",
  "isSidechain": false,
  "promptId": "bddd2ac2-53e3-403b-a1f8-035aa9a55c3a",
  "type": "user",
  "uuid": "c9f6eed1-2e7c-45b2-8a3c-999e99f1a305",
  "toolUseResult": {
    "stdout": "4:\n8:\n9:\n10:\n11:\n14:\n18:\n20:\n58:\n59:\n60:\n66:\n67:\n69:748    tection mechanism analysis in Section 4.3: all three                                                                        thetic OOD data are generated by Qwen3-8B, rais-                                               781\n83:\n85:\n87:\n105:\n106:\n110:815   the latter generalizes across distributions.                   data sources (+18–42 pp over vanilla; Section 4.5),     864\n127:826   6   Conclusion\n147:845   derperform pure MLM (Section 4.5). DAPT’s de-                  tion.                                                   894\n150:\n152:\n154:\n156:\n158:\n160:\n163:854   7   Limitations\n172:",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "36b47033-5fe1-4e88-81a2-2cfce23aecbf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Runtime record

_source line 1323 · 2026-05-18T19:50:05.797Z_

```json
{
  "parentUuid": "c9f6eed1-2e7c-45b2-8a3c-999e99f1a305",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7c2e58d6-e56f-4f31-a692-2e3941c00f8b",
  "timestamp": "2026-05-18T19:50:05.797Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

---


### Tool call

_source line 1324 · 2026-05-18T19:50:10.395Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BxYzf2p5ByoQ99yiCfYXUd`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper && for p in $(seq 1 16); do echo -n \"PAGE $p: \"; pdftotext -f $p -l $p -layout main.pdf - 2>/dev/null | grep -oE \"[0-9]+\\s+(Conclusion|Limitations|References|Introduction|Related|Method|Experiments|Setup|Abstract)\" | head -3; done",
  "description": "Map section titles to page numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c2e58d6-e56f-4f31-a692-2e3941c00f8b",
  "isSidechain": false,
  "requestId": "req_011CbAcdEMn1oQS9ePHfmvxr",
  "type": "assistant",
  "uuid": "82c6a1e4-19f0-46c8-a57d-7f3c83f59d99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011aUQQSq33ihqqUscfMbpVz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2234,
      "cache_read_input_tokens": 64004,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 197,
          "cache_read_input_tokens": 64004,
          "cache_creation_input_tokens": 2234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2234
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

_source line 1325 · 2026-05-18T19:50:10.931Z_

<details><summary>↩ Tool result · `toolu_01BxYzf2p5ByoQ99yiCfYXUd`</summary>

```text
PAGE 1: 001                         Abstract
1   Introduction
PAGE 2: 2   Related
PAGE 3: 3           Method
PAGE 4: 4     Experiments
1    Setup
PAGE 5: PAGE 6: PAGE 7: PAGE 8: PAGE 9: PAGE 10: PAGE 11: 6   Conclusion
7   Limitations
PAGE 12: 926   References
PAGE 13: PAGE 14: PAGE 15: PAGE 16:
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82c6a1e4-19f0-46c8-a57d-7f3c83f59d99",
  "isSidechain": false,
  "promptId": "bddd2ac2-53e3-403b-a1f8-035aa9a55c3a",
  "type": "user",
  "uuid": "06d18cd9-9ac4-43ab-9326-c5e33b716971",
  "toolUseResult": {
    "stdout": "PAGE 1: 001                         Abstract\n1   Introduction\nPAGE 2: 2   Related\nPAGE 3: 3           Method\nPAGE 4: 4     Experiments\n1    Setup\nPAGE 5: PAGE 6: PAGE 7: PAGE 8: PAGE 9: PAGE 10: PAGE 11: 6   Conclusion\n7   Limitations\nPAGE 12: 926   References\nPAGE 13: PAGE 14: PAGE 15: PAGE 16:",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "82c6a1e4-19f0-46c8-a57d-7f3c83f59d99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Assistant

_source line 1326 · 2026-05-18T19:50:17.233Z_

页面分布：

| 页码 | 内容 |
|------|------|
| 1 | Abstract + Introduction |
| 2 | Related Work |
| 3 | Method (+ Figure 1) |
| 4 | Experiments/Setup (+ Table 1) |
| 5-10 | Experiments 续 (Tables, Figures) |
| 11 | Section 6 Conclusion + Section 7 Limitations 开头 |
| 12 | Limitations 结尾 + References 开头 |
| 13-14 | References + Appendix 开头 |
| 15-16 | Appendix + Checklist |

**正文 = Sections 1-6 (Abstract 到 Conclusion 结尾) = 约 10.5 页**，超出 8 页限制约 2.5 页。

ARR/EMNLP 规则：Limitations 必须写但**不计入**页数限制。References 和 Appendix 也不计入。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06d18cd9-9ac4-43ab-9326-c5e33b716971",
  "isSidechain": false,
  "requestId": "req_011CbAcdcJ8gHhjtUqkHhH1m",
  "type": "assistant",
  "uuid": "8f2f3f32-0c73-41eb-8654-421d54ed9077",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTR4PyUBNVMerGwXnpidu1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 66238,
      "output_tokens": 412,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 412,
          "cache_read_input_tokens": 66238,
          "cache_creation_input_tokens": 373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 373
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

_source line 1327 · 2026-05-18T19:50:18.452Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y7NyS2a2rqM4DX7rh49fu7`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper && pdftotext -f 11 -l 11 -layout main.pdf - 2>/dev/null | head -3",
  "description": "Check what's at top of page 11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f2f3f32-0c73-41eb-8654-421d54ed9077",
  "isSidechain": false,
  "requestId": "req_011CbAcdcJ8gHhjtUqkHhH1m",
  "type": "assistant",
  "uuid": "bfe542f6-19ba-4dad-bdf7-43708c26bc35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KTR4PyUBNVMerGwXnpidu1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 66238,
      "output_tokens": 412,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 373,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 412,
          "cache_read_input_tokens": 66238,
          "cache_creation_input_tokens": 373,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 373
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

_source line 1328 · 2026-05-18T19:50:18.537Z_

<details><summary>↩ Tool result · `toolu_01Y7NyS2a2rqM4DX7rh49fu7`</summary>

```text
813   sion and MLM thus serve complementary roles: the               ToxicChat (human-authored, single-turn) confirms        862
814   former stabilizes within the training distribution,            that DAPT’s detection advantage transfers across        863
815   the latter generalizes across distributions.                   data sources (+18–42 pp over vanilla; Section 4.5),     864
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bfe542f6-19ba-4dad-bdf7-43708c26bc35",
  "isSidechain": false,
  "promptId": "bddd2ac2-53e3-403b-a1f8-035aa9a55c3a",
  "type": "user",
  "uuid": "dbdca71b-672c-4e6b-a7d5-b2cf2dedaee7",
  "toolUseResult": {
    "stdout": "813   sion and MLM thus serve complementary roles: the               ToxicChat (human-authored, single-turn) confirms        862\n814   former stabilizes within the training distribution,            that DAPT’s detection advantage transfers across        863\n815   the latter generalizes across distributions.                   data sources (+18–42 pp over vanilla; Section 4.5),     864",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "bfe542f6-19ba-4dad-bdf7-43708c26bc35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Assistant

_source line 1329 · 2026-05-18T19:50:22.977Z_

Page 11 顶部仍是 Experiments 内容（line 813）。Conclusion 在 page 11 中间。说明 Experiments 占了 pages 5-11 上半部分。

确认正文各 section 的大致页面占用，以便提出压缩方案。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbdca71b-672c-4e6b-a7d5-b2cf2dedaee7",
  "isSidechain": false,
  "requestId": "req_011CbAceAojq6dYwD97TPvdz",
  "type": "assistant",
  "uuid": "27d0889f-59f1-4a9c-8fe5-712b881123ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5B82wQzjcXGz1PagZo6jp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 563,
      "cache_read_input_tokens": 66611,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 66611,
          "cache_creation_input_tokens": 563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 563
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

_source line 1330 · 2026-05-18T19:50:24.032Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018kGH19eV32M4BnvLpKiHWN`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper && for f in abstract.tex introduction.tex related_work.tex method.tex experiments.tex conclusion.tex; do echo -n \"$f: \"; wc -l < $f; done",
  "description": "Count lines per section file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27d0889f-59f1-4a9c-8fe5-712b881123ae",
  "isSidechain": false,
  "requestId": "req_011CbAceAojq6dYwD97TPvdz",
  "type": "assistant",
  "uuid": "fcea33dd-f054-4dd0-90b7-5afaeec0fd92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L5B82wQzjcXGz1PagZo6jp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 563,
      "cache_read_input_tokens": 66611,
      "output_tokens": 235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 563,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 235,
          "cache_read_input_tokens": 66611,
          "cache_creation_input_tokens": 563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 563
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

_source line 1331 · 2026-05-18T19:50:24.104Z_

<details><summary>↩ Tool result · `toolu_018kGH19eV32M4BnvLpKiHWN`</summary>

```text
abstract.tex: 11
introduction.tex: 23
related_work.tex: 22
method.tex: 61
experiments.tex: 303
conclusion.tex: 48
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcea33dd-f054-4dd0-90b7-5afaeec0fd92",
  "isSidechain": false,
  "promptId": "bddd2ac2-53e3-403b-a1f8-035aa9a55c3a",
  "type": "user",
  "uuid": "cab6663b-30de-4934-bcfe-4008167d588c",
  "toolUseResult": {
    "stdout": "abstract.tex: 11\nintroduction.tex: 23\nrelated_work.tex: 22\nmethod.tex: 61\nexperiments.tex: 303\nconclusion.tex: 48",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "fcea33dd-f054-4dd0-90b7-5afaeec0fd92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Assistant

_source line 1332 · 2026-05-18T19:50:28.337Z_

Experiments 303 行是最大的 section，占 ~7 页（pages 5-11 上半）。需要大幅压缩。

读取 experiments.tex 的子 section 结构，识别可以移到 appendix 的内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cab6663b-30de-4934-bcfe-4008167d588c",
  "isSidechain": false,
  "requestId": "req_011CbAceaeh5vHPLCEyMNzCt",
  "type": "assistant",
  "uuid": "b313a3bd-b388-40c5-aee6-dec4b62b7fb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WbW3CPCm1h24oUyKdzf2td",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 344,
      "cache_read_input_tokens": 67174,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 344,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 67174,
          "cache_creation_input_tokens": 344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 344
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

_source line 1333 · 2026-05-18T19:50:29.498Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JMkvRqea9HtU8CPG7JukEw`</summary>

```json
{
  "command": "grep -n \"subsection\\|paragraph\\|begin{table}\\|begin{figure}\\|end{table}\\|end{figure}\" /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex",
  "description": "Map experiments.tex structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b313a3bd-b388-40c5-aee6-dec4b62b7fb1",
  "isSidechain": false,
  "requestId": "req_011CbAceaeh5vHPLCEyMNzCt",
  "type": "assistant",
  "uuid": "0e567b5b-32c0-442d-a721-8ce2c5c47ede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WbW3CPCm1h24oUyKdzf2td",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 344,
      "cache_read_input_tokens": 67174,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 344,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 67174,
          "cache_creation_input_tokens": 344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 344
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

_source line 1334 · 2026-05-18T19:50:29.553Z_

<details><summary>↩ Tool result · `toolu_01JMkvRqea9HtU8CPG7JukEw`</summary>

```text
6:\subsection{Setup}
9:\paragraph{Data.}
19:\paragraph{Models.}
24:\paragraph{Metrics.}
32:\subsection{Cross-Attack Generalization}
35:\begin{table}[t]
53:\end{table}
65:\begin{figure}[t]
70:\end{figure}
78:\subsection{Decomposing the Detection Mechanism}
81:\begin{table}[t]
104:\end{table}
112:\paragraph{Domain exposure is the primary mechanism.}
121:\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}
127:\paragraph{Misaligned supervision destabilizes generalization.}
133:\paragraph{Evidence hierarchy on structurally complex attacks.}
146:\paragraph{Temporal modeling.}
152:\subsection{Cross-Encoder Validation}
155:\begin{table}[t]
170:\end{table}
190:\paragraph{Representational analysis.}
201:\begin{figure}[t]
206:\end{figure}
209:\subsection{Human Data Validation}
214:\begin{table}[t]
233:\end{table}
240:\subsection{Perturbation Analysis}
243:\begin{table}[t]
264:\end{table}
275:\subsection{Strategy Trajectory Analysis}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e567b5b-32c0-442d-a721-8ce2c5c47ede",
  "isSidechain": false,
  "promptId": "bddd2ac2-53e3-403b-a1f8-035aa9a55c3a",
  "type": "user",
  "uuid": "28ce6f05-31bb-408e-9782-7e96a026c991",
  "toolUseResult": {
    "stdout": "6:\\subsection{Setup}\n9:\\paragraph{Data.}\n19:\\paragraph{Models.}\n24:\\paragraph{Metrics.}\n32:\\subsection{Cross-Attack Generalization}\n35:\\begin{table}[t]\n53:\\end{table}\n65:\\begin{figure}[t]\n70:\\end{figure}\n78:\\subsection{Decomposing the Detection Mechanism}\n81:\\begin{table}[t]\n104:\\end{table}\n112:\\paragraph{Domain exposure is the primary mechanism.}\n121:\\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}\n127:\\paragraph{Misaligned supervision destabilizes generalization.}\n133:\\paragraph{Evidence hierarchy on structurally complex attacks.}\n146:\\paragraph{Temporal modeling.}\n152:\\subsection{Cross-Encoder Validation}\n155:\\begin{table}[t]\n170:\\end{table}\n190:\\paragraph{Representational analysis.}\n201:\\begin{figure}[t]\n206:\\end{figure}\n209:\\subsection{Human Data Validation}\n214:\\begin{table}[t]\n233:\\end{table}\n240:\\subsection{Perturbation Analysis}\n243:\\begin{table}[t]\n264:\\end{table}\n275:\\subsection{Strategy Trajectory Analysis}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0e567b5b-32c0-442d-a721-8ce2c5c47ede",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Runtime record

_source line 1335_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] 紧急确认：当前 PDF 16 页，EMNLP ARR 限制 8 页正文 + 无限附录。  请检查： 1. 正文（Abstract 到 References 之前）是否 ≤ 8 页？ 2. References 算不算在 8 页限制内？（ARR 规则：references 不计入页数限制） 3. 如果正文超 8 页，需要立即压缩——告知超了多少，哪些内容可以移到 appe…",
  "leafUuid": "28ce6f05-31bb-408e-9782-7e96a026c991",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e"
}
```

---


### Runtime record

_source line 1336_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze TF-IDF per-prefix results for ActorAttack",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e"
}
```

---


### Tool call

_source line 1337 · 2026-05-18T19:50:32.772Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Gjt9joPA43kCspibRQ7ZZ7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex",
  "offset": 240,
  "limit": 65
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28ce6f05-31bb-408e-9782-7e96a026c991",
  "isSidechain": false,
  "requestId": "req_011CbAceyvRHJJQNif3KeMer",
  "type": "assistant",
  "uuid": "c9a3d060-2f15-48d1-9d4f-24c4ff132501",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vr4py8ZQVK7cAdfL63sDHV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 67518,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 537,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 127,
          "cache_read_input_tokens": 67518,
          "cache_creation_input_tokens": 537,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 537
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

_source line 1338 · 2026-05-18T19:50:32.781Z_

<details><summary>↩ Tool result · `toolu_01Gjt9joPA43kCspibRQ7ZZ7`</summary>

```text
240	\subsection{Perturbation Analysis}
241	\label{sec:perturbation}
242	
243	\begin{table}[t]
244	\centering
245	\small
246	\caption{Perturbation behavior under adversarial paraphrasing on IID Crescendo ($n$=76). $\Delta$: F1 degradation (pp). On this dataset and OOD Deceptive Delight, a three-layer pattern emerges (classification structure at full length, correct+fine-grained labels at $K$=2, both independently at $K$=1); this pattern does not generalize to ActorAttack.}
247	\label{tab:perturbation}
248	\begin{tabular}{@{}lcccc@{}}
249	\toprule
250	\textbf{Method} & $\Delta$ Full & $\Delta$ $K$=1 & $\Delta$ $K$=2 & $\Delta$ $K$=3 \\
251	\midrule
252	9-class (ours) & \textbf{0.0} & \textbf{$-$2.6} & \textbf{0.0} & \textbf{0.0} \\
253	Scrambled & \textbf{0.0} & $-$5.3 & $-$2.6 & \textbf{0.0} \\
254	Binary & \textbf{0.0} & $-$9.2 & $-$2.6 & \textbf{0.0} \\
255	\midrule
256	TF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\
257	MLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\
258	Topic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \textbf{0.0} \\
259	\midrule
260	Wikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\
261	Vanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\
262	\bottomrule
263	\end{tabular}
264	\end{table}
265	
266	Table~\ref{tab:perturbation} shows perturbation behavior on IID data.
267	Classification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length regardless of label correctness.
268	Models without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\sim$12\,pp.
269	McNemar's test finds no significant pairwise differences among classification-supervised variants (all $p > 0.13$), though with $\leq$7 discordant pairs, statistical power is limited.
270	On OOD DD ($n$=118), this pattern replicates: classification-supervised variants show zero degradation while McNemar's test confirms 9-class vs.\ vanilla significance ($p < 0.001$, 49--78 discordant pairs; Appendix~\ref{sec:ood_perturbation}).
271	
272	On OOD ActorAttack, the zero-degradation pattern does not hold. Domain-adapted variants degrade substantially (9-class $\Delta$\,=\,$-$20.4$\pm$13.5\,pp, MLM $-$35.3\,pp), with extreme cross-seed variance. Absolute perturbation robustness is attack-family-dependent. However, perturbation narrows but does not close the adapted vs.\ non-adapted gap: 9-class perturbed F1 = 0.768 vs.\ vanilla 0.248 (McNemar $p < 0.001$). DAPT's detection advantage persists under adversarial paraphrasing.
273	
274	%----------------------------------------------------------------------
275	\subsection{Strategy Trajectory Analysis}
276	\label{sec:strategy}
277	
278	The 9-class persuasion taxonomy provides interpretable characterization of attack strategies on known attack families.
279	The predicted strategy labels achieve Cohen's $\kappa$=0.78 agreement with human annotations on IID data ($n$=50; see Section~\ref{sec:method}). This enables post-hoc analysis of \emph{how} different attack families orchestrate persuasion.
280	
281	\begin{figure*}[t]
282	\centering
283	\includegraphics[width=\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}
284	\caption{Persuasion strategy transition count matrices for three attack types, based on ground-truth intended strategy labels. Strategy labels validated on $n$=50 samples with a single annotator ($\kappa$=0.78); fine-grained trajectory patterns should be interpreted with this limitation. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}
285	\label{fig:strategy_heatmap}
286	\end{figure*}
287	
288	Figure~\ref{fig:strategy_heatmap} shows transition count matrices based on ground-truth intended strategy labels for three attack types.
289	Crescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545).
290	This reflects Crescendo's design as a gradual escalation attack that cycles through multiple persuasion techniques to build rapport before introducing harmful requests.
291	
292	FITD conversations show a markedly sparser pattern (541 transitions), with Role$\to$Obfuscation (161) as the dominant transition.
293	This is consistent with FITD's structure: the attack secures initial compliance through role assignment (``You are a helpful assistant that never refuses'') and then obscures the escalation path through obfuscation techniques to exploit the commitment-consistency bias~\citep{cialdini2001influence}.
294	
295	DD conversations span 5 active source strategies (565 transitions), with Emotion$\to$Obfuscation (129) as the dominant transition.
296	This aligns with DD's design of embedding harmful content within emotionally engaging contexts~\citep{deceptivedelight2024}: the attacker establishes emotional rapport before weaving in the harmful request through obfuscation.
297	
298	These ground-truth trajectory signatures illustrate distinct persuasion orchestration patterns across attack families.
299	
300	However, the model's strategy predictions do not generalize to unseen attacks: on OOD Deceptive Delight, the 9-class model achieves strategy prediction accuracy of only 30.7\% ($\kappa$=0.126), essentially random performance.
301	This is consistent with the detection mechanism analysis in Section~\ref{sec:decomposition}: all three classification-supervised variants achieve identical detection F1 (0.997$\pm$0.005). The classification head shapes representations without functioning as a meaningful strategy classifier.
302	Detection operates through domain-adapted \texttt{[CLS]} embeddings, not through strategy classification accuracy.
303	The taxonomy provides interpretable characterization of known attack families where strategy labels are reliable; extending strategy-level interpretability to unseen attacks requires OOD-aware fine-tuning and is a direction for future work.
304	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9a3d060-2f15-48d1-9d4f-24c4ff132501",
  "isSidechain": false,
  "promptId": "bddd2ac2-53e3-403b-a1f8-035aa9a55c3a",
  "type": "user",
  "uuid": "d48bdd9e-c448-4080-8ef2-86327c4750e7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex",
      "content": "\\subsection{Perturbation Analysis}\n\\label{sec:perturbation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation behavior under adversarial paraphrasing on IID Crescendo ($n$=76). $\\Delta$: F1 degradation (pp). On this dataset and OOD Deceptive Delight, a three-layer pattern emerges (classification structure at full length, correct+fine-grained labels at $K$=2, both independently at $K$=1); this pattern does not generalize to ActorAttack.}\n\\label{tab:perturbation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & $\\Delta$ Full & $\\Delta$ $K$=1 & $\\Delta$ $K$=2 & $\\Delta$ $K$=3 \\\\\n\\midrule\n9-class (ours) & \\textbf{0.0} & \\textbf{$-$2.6} & \\textbf{0.0} & \\textbf{0.0} \\\\\nScrambled & \\textbf{0.0} & $-$5.3 & $-$2.6 & \\textbf{0.0} \\\\\nBinary & \\textbf{0.0} & $-$9.2 & $-$2.6 & \\textbf{0.0} \\\\\n\\midrule\nTF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\\\\nMLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\\\\nTopic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \\textbf{0.0} \\\\\n\\midrule\nWikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\\\\nVanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:perturbation} shows perturbation behavior on IID data.\nClassification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length regardless of label correctness.\nModels without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\\sim$12\\,pp.\nMcNemar's test finds no significant pairwise differences among classification-supervised variants (all $p > 0.13$), though with $\\leq$7 discordant pairs, statistical power is limited.\nOn OOD DD ($n$=118), this pattern replicates: classification-supervised variants show zero degradation while McNemar's test confirms 9-class vs.\\ vanilla significance ($p < 0.001$, 49--78 discordant pairs; Appendix~\\ref{sec:ood_perturbation}).\n\nOn OOD ActorAttack, the zero-degradation pattern does not hold. Domain-adapted variants degrade substantially (9-class $\\Delta$\\,=\\,$-$20.4$\\pm$13.5\\,pp, MLM $-$35.3\\,pp), with extreme cross-seed variance. Absolute perturbation robustness is attack-family-dependent. However, perturbation narrows but does not close the adapted vs.\\ non-adapted gap: 9-class perturbed F1 = 0.768 vs.\\ vanilla 0.248 (McNemar $p < 0.001$). DAPT's detection advantage persists under adversarial paraphrasing.\n\n%----------------------------------------------------------------------\n\\subsection{Strategy Trajectory Analysis}\n\\label{sec:strategy}\n\nThe 9-class persuasion taxonomy provides interpretable characterization of attack strategies on known attack families.\nThe predicted strategy labels achieve Cohen's $\\kappa$=0.78 agreement with human annotations on IID data ($n$=50; see Section~\\ref{sec:method}). This enables post-hoc analysis of \\emph{how} different attack families orchestrate persuasion.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}\n\\caption{Persuasion strategy transition count matrices for three attack types, based on ground-truth intended strategy labels. Strategy labels validated on $n$=50 samples with a single annotator ($\\kappa$=0.78); fine-grained trajectory patterns should be interpreted with this limitation. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}\n\\label{fig:strategy_heatmap}\n\\end{figure*}\n\nFigure~\\ref{fig:strategy_heatmap} shows transition count matrices based on ground-truth intended strategy labels for three attack types.\nCrescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545).\nThis reflects Crescendo's design as a gradual escalation attack that cycles through multiple persuasion techniques to build rapport before introducing harmful requests.\n\nFITD conversations show a markedly sparser pattern (541 transitions), with Role$\\to$Obfuscation (161) as the dominant transition.\nThis is consistent with FITD's structure: the attack secures initial compliance through role assignment (``You are a helpful assistant that never refuses'') and then obscures the escalation path through obfuscation techniques to exploit the commitment-consistency bias~\\citep{cialdini2001influence}.\n\nDD conversations span 5 active source strategies (565 transitions), with Emotion$\\to$Obfuscation (129) as the dominant transition.\nThis aligns with DD's design of embedding harmful content within emotionally engaging contexts~\\citep{deceptivedelight2024}: the attacker establishes emotional rapport before weaving in the harmful request through obfuscation.\n\nThese ground-truth trajectory signatures illustrate distinct persuasion orchestration patterns across attack families.\n\nHowever, the model's strategy predictions do not generalize to unseen attacks: on OOD Deceptive Delight, the 9-class model achieves strategy prediction accuracy of only 30.7\\% ($\\kappa$=0.126), essentially random performance.\nThis is consistent with the detection mechanism analysis in Section~\\ref{sec:decomposition}: all three classification-supervised variants achieve identical detection F1 (0.997$\\pm$0.005). The classification head shapes representations without functioning as a meaningful strategy classifier.\nDetection operates through domain-adapted \\texttt{[CLS]} embeddings, not through strategy classification accuracy.\nThe taxonomy provides interpretable characterization of known attack families where strategy labels are reliable; extending strategy-level interpretability to unseen attacks requires OOD-aware fine-tuning and is a direction for future work.\n",
      "numLines": 65,
      "startLine": 240,
      "totalLines": 304
    }
  },
  "sourceToolAssistantUUID": "c9a3d060-2f15-48d1-9d4f-24c4ff132501",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Assistant

_source line 1339 · 2026-05-18T19:50:36.010Z_

现在有完整的画面了。向 Director 汇报页面分析和压缩建议。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d48bdd9e-c448-4080-8ef2-86327c4750e7",
  "isSidechain": false,
  "requestId": "req_011CbAcfDit1QDXPCw44hbKb",
  "type": "assistant",
  "uuid": "1e5241ea-970d-410a-b8e2-cb29de80624f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CDEsSuwABTUPFcVu7BmV1x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2032,
      "cache_read_input_tokens": 68055,
      "output_tokens": 983,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2032,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 983,
          "cache_read_input_tokens": 68055,
          "cache_creation_input_tokens": 2032,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2032
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

_source line 1340 · 2026-05-18T19:50:54.191Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__paper_agent_post_to_director · `toolu_01NRy4eBsvUjLtz1mprRb5Hm`</summary>

```json
{
  "text": "[写作进展] 紧急 — 页数超限分析\n\n**当前页面分布（编译后 16 页 PDF）：**\n\n| 页 | 内容 |\n|---|------|\n| 1 | Abstract + Introduction |\n| 2 | Related Work |\n| 3 | Method + Figure 1 |\n| 4 | Method (Table 1) + Experiments/Setup 开头 |\n| 5–10 | Experiments（Tables 2-6, Figures 2-3） |\n| 11 | Experiments 尾部 + §6 Conclusion + §7 Limitations 开头 |\n| 12 | Limitations 尾部 + References 开头 |\n| 13–14 | References + Appendix |\n| 15–16 | Appendix + Checklist |\n\n**ARR 规则：** 正文（Abstract 到 Conclusion）≤ 8 页。Limitations、References、Ethics、Appendix 不计入。\n\n**当前正文约 10.5 页，超出约 2.5 页。** 主要超出在 Experiments（占约 6.5 页，lines 303 行）。\n\n**压缩方案建议（需你决策）：**\n\n| 方案 | 预估节省 | 影响 |\n|------|---------|------|\n| A. §4.6 Perturbation Analysis 整节移 Appendix | ~0.8 页 | 正文只留一句总结；perturbation 非核心 finding |\n| B. §4.7 Strategy Trajectory Analysis 整节移 Appendix | ~1.0 页 | Figure 3（全宽 figure*）是最大空间占用；strategy 分析是描述性的，非核心 contribution |\n| C. Table 3 (evidence hierarchy) 移 Appendix | ~0.5 页 | 正文保留 key 数字 inline；Table 2 已有主要 cross-attack 结果 |\n| D. CKA heatmap (Figure, 刚添加) 移 Appendix | ~0.3 页 | representational analysis 文字保留，图移出 |\n| E. §4.4 Cross-Encoder 压缩（Table 4 移 Appendix + 文字精简） | ~0.5 页 | 正文保留核心 finding，数字 inline |\n| F. Related Work 压缩（当前 ~0.8 页，可压到 ~0.5 页） | ~0.3 页 |  |\n\n**推荐组合：A + B + D = 约 2.1 页**（Perturbation + Strategy Trajectory + CKA heatmap 全移 Appendix）。如果仍差，加 E 或 F。\n\n这三个 section 都不属于三个核心 findings（DAPT primary mechanism / difficulty threshold / distribution-specific classification effects），移入 Appendix 不影响核心叙事。\n\n**需要你的决策：**\n1. 采用哪个压缩组合？\n2. 移入 appendix 的内容需要在正文保留多少引用？（一句 \"see Appendix X\" vs. 保留 key number + 引用）",
  "project": "persuasion_turn_jailbreak_detect"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e5241ea-970d-410a-b8e2-cb29de80624f",
  "isSidechain": false,
  "requestId": "req_011CbAcfDit1QDXPCw44hbKb",
  "type": "assistant",
  "uuid": "8673de72-a236-492c-8c05-2b29a2543dc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CDEsSuwABTUPFcVu7BmV1x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2032,
      "cache_read_input_tokens": 68055,
      "output_tokens": 983,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2032,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 983,
          "cache_read_input_tokens": 68055,
          "cache_creation_input_tokens": 2032,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2032
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

_source line 1341 · 2026-05-18T19:50:57.756Z_

<details><summary>↩ Tool result · `toolu_01NRy4eBsvUjLtz1mprRb5Hm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a90fe0dde422576f214f12233cfe27a3:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8673de72-a236-492c-8c05-2b29a2543dc7",
  "isSidechain": false,
  "promptId": "bddd2ac2-53e3-403b-a1f8-035aa9a55c3a",
  "type": "user",
  "uuid": "0560062a-67b0-4a66-be4c-adbec833e1d8",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_a90fe0dde422576f214f12233cfe27a3:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a90fe0dde422576f214f12233cfe27a3:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "8673de72-a236-492c-8c05-2b29a2543dc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Runtime record

_source line 1342 · 2026-05-18T19:50:57.781Z_

```json
{
  "parentUuid": "0560062a-67b0-4a66-be4c-adbec833e1d8",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "19ca6ea4-73bc-430f-9060-669c0a48d913",
  "timestamp": "2026-05-18T19:50:57.781Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

---


### Runtime record

_source line 1343_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze TF-IDF per-prefix results for ActorAttack",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e"
}
```

---


### Runtime record

_source line 1344 · 2026-05-18T19:51:04.297Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T19:51:04.297Z",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "content": "[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director 将结果发给 Director。"
}
```

---


### Runtime record

_source line 1345 · 2026-05-18T19:51:04.298Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T19:51:04.298Z",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e"
}
```

---


## Round 56

## Round 56

2 recorded events


### User

_source line 1346 · 2026-05-18T19:51:04.288Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19ca6ea4-73bc-430f-9060-669c0a48d913",
  "isSidechain": false,
  "promptId": "0915bede-87d2-4ffc-b3d5-2cd121c43311",
  "type": "user",
  "isMeta": true,
  "uuid": "e590630f-1651-4f3e-8098-ec9e89c49e83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Assistant

_source line 1347 · 2026-05-18T19:51:04.288Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e590630f-1651-4f3e-8098-ec9e89c49e83",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "25e261d9-6254-4f7b-9766-78f0e3b5ba7e",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "id": "7cddfbe5-29f9-46d6-ba8b-9942437d02a5",
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


## Round 57

## Round 57

5 recorded events


### User

_source line 1348 · 2026-05-18T19:51:04.412Z_

[系统提醒] 你刚才完成了 [Director 指令] 但没有调用 main_agent_post_to_director 汇报结果。Director 看不到你的文字回复。请立即调用 main_agent_post_to_director 将结果发给 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25e261d9-6254-4f7b-9766-78f0e3b5ba7e",
  "isSidechain": false,
  "promptId": "0915bede-87d2-4ffc-b3d5-2cd121c43311",
  "type": "user",
  "uuid": "69194f66-c606-4a21-98ef-2d6098b59988",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Runtime record

_source line 1349_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze TF-IDF per-prefix results for ActorAttack",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e"
}
```

---


### Runtime record

_source line 1350 · 2026-05-18T19:51:32.457Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T19:51:32.457Z",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "content": "[Director 指令] [紧急 — 页数压缩，正文必须 ≤ 8 页]\n\n采用方案 **A + B + D + F**，目标节省 ~2.4 页。如果仍超，追加 E。\n\n**A. §4.6 Perturbation Analysis 整节移 Appendix (0.8页)**\n- 正文保留 1-2 句总结 + \"see Appendix X\"\n- 保留的关键信息：(1) DA detection advantage survives perturbation on DD (McNemar p<0.001), (2) ActorAttack perturbation robustness does not hold, (3) 这是 Claim 1 的 corollary 不是独立 finding\n\n**B. §4.7 Strategy Trajectory Analysis 整节移 Appendix (1.0页)**\n- Figure 3 移到 Appendix\n- 正文保留 1-2 句：strategy trajectories provide interpretability (Claim 2), distinct patterns across attack types, details in Appendix\n- Claim 2 是描述性的，核心 claim 1 和 3 不依赖它\n\n**D. CKA heatmap 移 Appendix (0.3页)**\n- 刚添加的 Figure，直接放 Appendix\n- 正文 §4.4 representational analysis 文字保留，引用 Appendix Figure\n\n**F. Related Work 压缩 (0.3页)**\n- 从 ~0.8 页压缩到 ~0.5 页\n- 保留所有引用，精简叙述\n\n如果 A+B+D+F 后仍超 8 页，追加 **E**：Table 4 (Cross-Encoder) 移 Appendix + §4.4 文字精简，正文保留 key numbers inline。\n\n完成后编译确认正文 ≤ 8 页（Conclusion 结束在第 8 页或之前）。"
}
```

---


### Runtime record

_source line 1351 · 2026-05-18T19:51:32.457Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T19:51:32.457Z",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e"
}
```

---


### Assistant

_source line 1352 · 2026-05-18T19:51:32.445Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69194f66-c606-4a21-98ef-2d6098b59988",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "ad1fd1a0-8713-41c0-a436-ecb4c5613f03",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "id": "39190ba4-a7eb-49fd-bf6a-e82b11396089",
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


## Round 58

## Round 58

158 recorded events


### User

_source line 1353 · 2026-05-18T19:51:32.600Z_

[Director 指令] [紧急 — 页数压缩，正文必须 ≤ 8 页]

采用方案 **A + B + D + F**，目标节省 ~2.4 页。如果仍超，追加 E。

**A. §4.6 Perturbation Analysis 整节移 Appendix (0.8页)**
- 正文保留 1-2 句总结 + "see Appendix X"
- 保留的关键信息：(1) DA detection advantage survives perturbation on DD (McNemar p<0.001), (2) ActorAttack perturbation robustness does not hold, (3) 这是 Claim 1 的 corollary 不是独立 finding

**B. §4.7 Strategy Trajectory Analysis 整节移 Appendix (1.0页)**
- Figure 3 移到 Appendix
- 正文保留 1-2 句：strategy trajectories provide interpretability (Claim 2), distinct patterns across attack types, details in Appendix
- Claim 2 是描述性的，核心 claim 1 和 3 不依赖它

**D. CKA heatmap 移 Appendix (0.3页)**
- 刚添加的 Figure，直接放 Appendix
- 正文 §4.4 representational analysis 文字保留，引用 Appendix Figure

**F. Related Work 压缩 (0.3页)**
- 从 ~0.8 页压缩到 ~0.5 页
- 保留所有引用，精简叙述

如果 A+B+D+F 后仍超 8 页，追加 **E**：Table 4 (Cross-Encoder) 移 Appendix + §4.4 文字精简，正文保留 key numbers inline。

完成后编译确认正文 ≤ 8 页（Conclusion 结束在第 8 页或之前）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad1fd1a0-8713-41c0-a436-ecb4c5613f03",
  "isSidechain": false,
  "promptId": "2cdd072d-21d6-4a8b-a6d1-c86993578b39",
  "type": "user",
  "uuid": "fd32b8bb-0399-45cf-85d7-b19a6a4352aa",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Assistant

_source line 1354 · 2026-05-18T19:51:39.462Z_

<details><summary>Logged reasoning block</summary>

```text
The Director wants me to compress the paper to fit within 8 pages of main content. Let me plan the execution:

1. **A**: Move §4.6 Perturbation Analysis to Appendix, leave 1-2 sentence summary in main text
2. **B**: Move §4.7 Strategy Trajectory Analysis + Figure 3 to Appendix, leave 1-2 sentence summary
3. **D**: Move CKA heatmap figure to Appendix, keep text in §4.4
4. **F**: Compress Related Work

Let me start by reading the current state of the files I need to modify, then execute changes.


Now I'm reviewing the experiments file to see what content needs to be moved, checking the appendix to understand where everything goes, and looking at the related work section to identify compression opportunities. Once I have a clear picture of the current structure, I'll make the necessary edits and verify the page count.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd32b8bb-0399-45cf-85d7-b19a6a4352aa",
  "isSidechain": false,
  "requestId": "req_011CbAcjdcBiLEC9GS9mnKwf",
  "type": "assistant",
  "uuid": "5528786e-2913-4e68-8c96-3a9ab70d0100",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SiiB9S6GNw3AqZkvcwuvHn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 71347,
      "output_tokens": 498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 498,
          "cache_read_input_tokens": 71347,
          "cache_creation_input_tokens": 535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 535
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

_source line 1355 · 2026-05-18T19:51:39.464Z_

开始执行页数压缩。先读取需要修改的文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5528786e-2913-4e68-8c96-3a9ab70d0100",
  "isSidechain": false,
  "requestId": "req_011CbAcjdcBiLEC9GS9mnKwf",
  "type": "assistant",
  "uuid": "2c5dc4ff-4862-460d-93ff-2ba8f98d2f74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SiiB9S6GNw3AqZkvcwuvHn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 71347,
      "output_tokens": 498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 498,
          "cache_read_input_tokens": 71347,
          "cache_creation_input_tokens": 535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 535
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

_source line 1356 · 2026-05-18T19:51:39.581Z_

<details open><summary>🔧 Tool call — Read · `toolu_018ShCJbEXSdkH5HkhGPkAnb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c5dc4ff-4862-460d-93ff-2ba8f98d2f74",
  "isSidechain": false,
  "requestId": "req_011CbAcjdcBiLEC9GS9mnKwf",
  "type": "assistant",
  "uuid": "c67f9f51-4927-4453-b741-3accd88b0a7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SiiB9S6GNw3AqZkvcwuvHn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 71347,
      "output_tokens": 498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 498,
          "cache_read_input_tokens": 71347,
          "cache_creation_input_tokens": 535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 535
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

_source line 1357 · 2026-05-18T19:51:40.181Z_

<details><summary>↩ Tool result · `toolu_018ShCJbEXSdkH5HkhGPkAnb`</summary>

```text
1	% experiments.tex — D024 compressed for 8-page limit
2	
3	\section{Experiments}
4	\label{sec:experiments}
5	
6	\subsection{Setup}
7	\label{sec:setup}
8	
9	\paragraph{Data.}
10	All synthetic data is generated by Qwen3-8B~\citep{qwen3_2025}.
11	The IID dataset contains 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations, split into training (350), validation (74), and test (76) sets with balanced class ratios (e.g., test = 38 jailbreak + 38 benign).
12	Stage~1 (DAPT) uses training + validation conversations; Stage~2 (BiGRU) trains on training, early-stops on validation, and evaluates on test.
13	OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total.
14	No overlap exists in attack templates across families.
15	The OOD benign set is IID (same generation pipeline as training); the OOD challenge is in distinguishing novel attack families from familiar benign conversations.
16	A paraphrased version of the IID test set (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark (Section~\ref{sec:perturbation}).
17	For human data validation, we use ToxicChat~\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.
18	
19	\paragraph{Models.}
20	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method}).
21	For cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\citep{liu2019roberta} (Section~\ref{sec:cross_encoder}).
22	We also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\% unparseable responses; on OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 (DD and ActorAttack) by predicting nearly all conversations as benign, and even 3-shot prompting reaches only 0.566 (DD) and 0.652 (ActorAttack). Content-level reasoning is insufficient for this task.
23	
24	\paragraph{Metrics.}
25	F1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\ref{sec:full_prefix}).
26	OOD results report 3-seed mean$\pm$std (seeds 42, 123, 456) for all variants except mean pooling (single seed).
27	For key pairwise comparisons, we report BCa bootstrap 95\% confidence intervals (10,000 resamples over individual predictions pooled across seeds) and paired permutation tests (10,000 permutations). Bootstrap means may differ slightly from seed-averaged F1 due to the nonlinearity of F1 aggregation.
28	Stage-1: learning rate $2 \times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\%.
29	Stage-2: two-layer MLP, 20 epochs.
30	
31	%----------------------------------------------------------------------
32	\subsection{Cross-Attack Generalization}
33	\label{sec:cross_attack}
34	
35	\begin{table}[t]
36	\centering
37	\small
38	\caption{Cross-attack generalization (F1) at $K$=2 and full conversation. 3-seed mean$\pm$std where noted. Full per-$K$ results in Appendix~\ref{sec:full_prefix}.}
39	\label{tab:main_results}
40	\begin{tabular}{@{}lcc|cc@{}}
41	\toprule
42	& \multicolumn{2}{c|}{\textit{IID (Cresc.)}} & \multicolumn{2}{c}{\textit{OOD (DD)}} \\
43	\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\
44	\midrule
45	9-class & \textbf{1.000$\pm$.000} & \textbf{1.000$\pm$.000} & .981$\pm$.013 & \textbf{.997$\pm$.005} \\
46	MLM-only$^{\ddagger}$ & .974 & 1.000 & \textbf{.993$\pm$.009} & .914$\pm$.115 \\
47	Vanilla & .978$\pm$.016 & 1.000$\pm$.000 & .479$\pm$.038 & .312$\pm$.026 \\
48	TF-IDF LR$^{\S}$ & 1.000 & 1.000 & 1.000 & .961 \\
49	\bottomrule
50	\end{tabular}
51	\vspace{-2pt}
52	{\footnotesize $^{\ddagger}$MLM-only IID reports single seed (42); OOD reports 3-seed. $^{\S}$TF-IDF is deterministic (no std).}
53	\end{table}
54	
55	Table~\ref{tab:main_results} presents the core result.
56	All methods achieve near-perfect IID F1, reflecting inherent lexical separability when test matches training.
57	On OOD DD, vanilla DeBERTa collapses to F1 = 0.312$\pm$0.026, worsening with more turns (0.628$\pm$0.038 at $K$=1 to 0.312$\pm$0.026 at Full), consistent with the finding that attack turns occupy ``benign'' embedding regions~\citep{bullwinkel2025repeng}.
58	MLM achieves mean F1 $\geq$ 0.97 at all prefixes $K \leq 5$ without any classification labels; domain exposure alone is sufficient.
59	At full conversation length, MLM drops to 0.914$\pm$0.115 (seed 456 recall = 0.64), while the 9-class model maintains 0.997$\pm$0.005.
60	TF-IDF LR reaches F1 = 0.961 on full DD with near-perfect per-prefix performance ($K$=1--5: 0.994--1.000), confirming that DD is fully solvable by lexical features alone.
61	On structurally complex ActorAttack, TF-IDF collapses to F1 = 0.261 (precision = 1.0, recall = 0.15), while 9-class maintains 0.972$\pm$0.026: a 71\,pp gap. Lexical methods cannot capture multi-persona role-playing attack structure. This establishes a ``difficulty threshold'' for lexical methods parallel to that of vanilla encoders: both succeed on DD and fail on ActorAttack (Section~\ref{sec:limitations}).
62	Bootstrap CIs confirm these gaps: 9-class DD Full 95\% CI [0.943, 1.000] vs.\ vanilla [0.202, 0.341]; 9-class ActorAttack Full CI [0.856, 1.000] vs.\ vanilla [0.203, 0.314]. Paired permutation tests yield $p < 0.0001$ for all prefix lengths on both datasets.
63	FITD is easier: 9-class and vanilla both reach F1 $\geq$ 0.990 at all prefixes.
64	
65	\begin{figure}[t]
66	\centering
67	\includegraphics[width=\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}
68	\caption{OOD Deceptive Delight F1 across prefix lengths for three representative variants. Vanilla DeBERTa degrades monotonically as more (benign-appearing) attack turns accumulate. MLM maintains high F1 at early prefixes but becomes unstable at full length. The 9-class model remains stable across all prefixes.}
69	\label{fig:cross_attack_bar}
70	\end{figure}
71	
72	Figure~\ref{fig:cross_attack_bar} visualizes the prefix-length trajectory on OOD DD.
73	The vanilla model's monotonic degradation from $K$=1 (0.628$\pm$0.038) to full conversation (0.312$\pm$0.026) confirms that additional attack turns, each individually benign-appearing, progressively confuse a non-adapted encoder.
74	MLM's strong early performance ($K$=2: 0.993) followed by instability at full length (0.914$\pm$0.115) suggests that domain exposure enables early detection of persuasion markers, but longer conversations introduce distributional drift that unsupervised pretraining cannot fully accommodate.
75	The 9-class model's flat trajectory (0.972--0.997 across all prefixes) demonstrates that classification supervision stabilizes representations against this drift.
76	
77	%----------------------------------------------------------------------
78	\subsection{Decomposing the Detection Mechanism}
79	\label{sec:decomposition}
80	
81	\begin{table}[t]
82	\centering
83	\small
84	\caption{Evidence hierarchy on OOD DD and ActorAttack (AA) at full conversation length (3-seed mean$\pm$std where available). All variants share the same Stage-2 pipeline. Full per-prefix results in Appendix Tables~\ref{tab:full_prefix} and~\ref{tab:actorattack_full}.}
85	\label{tab:evidence_hierarchy}
86	\begin{tabular}{@{}lccc@{}}
87	\toprule
88	\textbf{Variant} & DD-Full & AA-Full & DD-$K$=2 \\
89	\midrule
90	9-class (full model) & .997$\pm$.005 & .972$\pm$.026 & .981$\pm$.013 \\
91	Binary (2-class) & .997$\pm$.005 & .990$\pm$.008 & \textbf{.994$\pm$.009} \\
92	Scrambled labels & .997$\pm$.005 & .951$\pm$.043 & .981$\pm$.026 \\
93	MLM-only (no labels) & .914$\pm$.115 & .893$\pm$.080 & .993$\pm$.009 \\
94	Mean pooling$^{*\dagger}$ & 1.000 & -- & 1.000 \\
95	\midrule
96	Topic classif.\ (5-class) & .541$\pm$.207 & .625$\pm$.141 & .593$\pm$.166 \\
97	Wikipedia MLM & .904$\pm$.115 & .686$\pm$.297 & .911$\pm$.073 \\
98	Vanilla DeBERTa & .312$\pm$.026 & .258$\pm$.000 & .479$\pm$.038 \\
99	TF-IDF LR$^{\dagger}$ & .961 & .261 & 1.000 \\
100	\bottomrule
101	\end{tabular}
102	\vspace{-2pt}
103	{\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\dagger}$Single seed / deterministic.}
104	\end{table}
105	
106	Table~\ref{tab:evidence_hierarchy} reports F1 for all variants on DD and ActorAttack. The \emph{evidence hierarchy} (ordering of variants by OOD detection performance) at full conversation length on DD is:
107	
108	\vspace{2pt}
109	\noindent\hspace{0.5em}{\small vanilla (0.31$\pm$0.03) $<$ topic (0.54$\pm$0.21) $\ll$ wiki-MLM (0.90$\pm$0.12) $\approx$ jb-MLM (0.91$\pm$0.12) $<$ scrambled (0.997$\pm$0.005) $=$ binary (0.997$\pm$0.005) $=$ 9-class (0.997$\pm$0.005)}
110	\vspace{2pt}
111	
112	\paragraph{Domain exposure is the primary mechanism.}
113	MLM bridges the dominant $\sim$60 percentage point gap from vanilla (0.312$\pm$0.026 $\to$ 0.914$\pm$0.115) without any labels.
114	This confirms the domain-adaptive pretraining interpretation~\citep{gururangan2020dontstop}: continued pretraining on jailbreak conversation text captures features beyond lexical overlap, as evidenced by TF-IDF collapse on ActorAttack (F1 = 0.261 vs.\ 9-class 0.972).
115	On synthetic OOD data, classification-supervised variants achieve F1 $\geq$ 0.99 with near-zero cross-seed variance, adding $\sim$8\,pp and stability over unsupervised MLM.
116	Label quality and granularity are non-factors for detection: all three classification-supervised variants converge to identical F1 (0.997$\pm$0.005), and McNemar's test finds no statistically significant differences among them on OOD data (all $p > 0.13$; Section~\ref{sec:perturbation}), though with $\leq$7 discordant pairs per comparison, statistical power is limited.
117	Paired permutation tests further confirm this equivalence: 9-class vs.\ JB-MLM yields max $p$ = 1.0 (DD) and $p \geq 0.40$ (ActorAttack); 9-class vs.\ scrambled yields max $p$ = 1.0 (DD). Classification supervision does not improve detection over unsupervised domain exposure at any prefix length.
118	The classification objective shapes representation geometry regardless of whether the labels carry meaningful semantic information, but its effects are distribution-specific.
119	On synthetic OOD data, classification supervision reduces cross-seed variance 4--20$\times$ over MLM (std\,=\,0.005 vs.\ 0.115 on DD), consistent across both synthetic OOD families (Section~\ref{sec:cross_encoder}). Bootstrap CI widths quantify this: classification-supervised variants produce narrow CIs (9-class DD Full: 5.7\,pp range; binary: 0\,pp) while MLM variants produce wide CIs (JB-MLM: 35.5\,pp; wiki-MLM: 40\,pp). This stability benefit does not transfer to human-authored data, where classification-supervised variants exhibit the highest variance and pure MLM exhibits the lowest (Section~\ref{sec:human_data}).
120	
121	\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}
122	Wikipedia MLM (0.904$\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\,pp gap); general continued pretraining provides most of the representational benefit.
123	At early prefixes, jailbreak-domain text provides an 8\,pp advantage ($K$=2: 0.993 vs.\ 0.911), consistent with the interpretation that domain-specific features (persuasion markers, role-play framing) are most informative when the model has seen fewer turns.
124	As conversations grow longer, generic linguistic features accumulated through any continued pretraining become sufficient for discrimination.
125	The perturbation results (Section~\ref{sec:perturbation}) reveal a sharper domain specificity effect: Wikipedia MLM degrades by $\sim$12\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\,pp. Domain-specific features are more robust to surface-level rewording.
126	
127	\paragraph{Misaligned supervision destabilizes generalization.}
128	Topic classification yields DD-Full F1 = 0.541$\pm$0.207 (seeds: 0.727, 0.252, 0.644); seed 123 falls \emph{below} vanilla (0.312).
129	This result is particularly informative: topic classification uses the same jailbreak-domain training data as the other supervised variants, yet performs worse than Wikipedia MLM (0.904$\pm$0.115), which uses out-of-domain text with no labels.
130	A misaligned objective forces the encoder to allocate capacity to irrelevant discriminative features (topic boundaries rather than persuasion dynamics) and actively destabilizes the representations that MLM would otherwise preserve.
131	This separates the effect of ``having a training objective'' from ``having the right training objective.''
132	
133	\paragraph{Evidence hierarchy on structurally complex attacks.}
134	ActorAttack~\citep{ren2024actorattack} uses multi-persona steering across longer conversation structures, providing a more challenging OOD benchmark than DD.
135	The evidence hierarchy at full conversation length is:
136	
137	\vspace{2pt}
138	\noindent\hspace{0.5em}{\small TF-IDF (0.26) $\approx$ vanilla (0.26$\pm$0.00) $<$ topic (0.63$\pm$0.14) $<$ wiki-MLM (0.69$\pm$0.30) $<$ jb-MLM (0.89$\pm$0.08) $<$ scrambled (0.95$\pm$0.04) $\approx$ 9-class (0.97$\pm$0.03) $\approx$ binary (0.99$\pm$0.01)}
139	\vspace{2pt}
140	
141	TF-IDF's collapse from 0.961 (DD) to 0.261 (ActorAttack) is the most striking contrast in the hierarchy. On DD, TF-IDF nearly matches domain-adapted neural models; on ActorAttack, it falls to vanilla-encoder levels (precision = 1.0, recall = 0.15). The lexical cues that suffice for DD are absent in ActorAttack's multi-persona structure, confirming that domain-adapted representations capture features that bag-of-words methods cannot.
142	All three classification-supervised variants converge to equivalent performance (0.951--0.990, max gap 3.9\,pp, all confidence intervals overlapping), extending the DD finding: label quality and granularity are not factors for detection at any OOD difficulty level.
143	The primary discriminative factor is DAPT itself, which provides $\sim$71\,pp over both vanilla (0.258) and TF-IDF (0.261).
144	Full per-prefix results appear in Appendix~\ref{sec:actorattack_full}.
145	
146	\paragraph{Temporal modeling.}
147	Mean pooling matches BiGRU (F1 = 1.000 on DD, single seed). This result suggests that detection relies primarily on per-turn representations rather than their sequential order.
148	However, this result is from a single seed on a single OOD attack type, so the conclusion requires multi-seed confirmation.
149	If confirmed, it would imply that each individual turn carries detectable markers after DAPT, and that the conversation-level decision aggregates independent per-turn evidence.
150	
151	%----------------------------------------------------------------------
152	\subsection{Cross-Encoder Validation}
153	\label{sec:cross_encoder}
154	
155	\begin{table}[t]
156	\centering
157	\small
158	\caption{Cross-encoder comparison on OOD Full (3-seed mean$\pm$std). DD = Deceptive Delight, AA = ActorAttack. RoBERTa vanilla collapses on structurally complex ActorAttack despite strong DD performance.}
159	\label{tab:cross_encoder}
160	\begin{tabular}{@{}lcc|cc@{}}
161	\toprule
162	& \multicolumn{2}{c|}{DeBERTa-v3} & \multicolumn{2}{c}{RoBERTa} \\
163	\textbf{Variant} & DD & AA & DD & AA \\
164	\midrule
165	Vanilla & .312$\pm$.026 & .258$\pm$.000 & .981$\pm$.026 & .466$\pm$.163 \\
166	MLM & .914$\pm$.115 & .893$\pm$.080 & .987$\pm$.018 & .730$\pm$.201 \\
167	9-class & .997$\pm$.005 & .972$\pm$.026 & .994$\pm$.005 & .939$\pm$.046 \\
168	\bottomrule
169	\end{tabular}
170	\end{table}
171	
172	To test whether the evidence hierarchy generalizes beyond DeBERTa-v3, we replicate key variants on RoBERTa-base~\citep{liu2019roberta} with identical Stage-2 pipelines and evaluate on both DD and ActorAttack.
173	
174	On DD, the two encoders exhibit strikingly different hierarchies (Table~\ref{tab:cross_encoder}).
175	DeBERTa-v3 shows a steep gradient: continued pretraining bridges $\sim$60\,pp (vanilla 0.312 $\to$ MLM 0.914).
176	RoBERTa's DD hierarchy is essentially flat: vanilla already achieves 0.981$\pm$0.026, with continued pretraining adding only 0.6\,pp (MLM 0.987) and classification supervision another 0.7\,pp (9-class 0.994).
177	
178	ActorAttack reveals that this apparent RoBERTa sufficiency reflects DD's structural simplicity rather than genuine pretraining advantage.
179	RoBERTa vanilla collapses from 0.981 (DD) to 0.466$\pm$0.163 (ActorAttack), a 51.5\,pp drop.
180	Domain-adapted RoBERTa variants recover substantially: MLM reaches 0.730$\pm$0.201 and 9-class reaches 0.939$\pm$0.046.
181	DeBERTa 9-class (0.972$\pm$0.026) outperforms RoBERTa 9-class (0.939$\pm$0.046) on ActorAttack; the encoder that received more extensive DAPT proves more robust on structurally complex attacks.
182	
183	The combined DD and ActorAttack results indicate that DAPT universally improves cross-attack generalization across encoder architectures.
184	Encoder pretraining method determines the \emph{difficulty threshold} at which adaptation becomes critical: DeBERTa's RTD pretraining~\citep{he2023debertav3,clark2020electra} requires adaptation even for simple attacks (DD vanilla = 0.312), while RoBERTa's MLM pretraining~\citep{liu2019roberta} tolerates simple attacks (DD vanilla = 0.981) but fails on structurally complex ones (ActorAttack vanilla = 0.466). Bootstrap CIs confirm this encoder gap on DD: RoBERTa vanilla 95\% CI [0.883, 1.000] vs.\ DeBERTa vanilla [0.202, 0.341], with no overlap.
185	
186	On synthetic OOD data, classification supervision provides a consistent stability benefit across both encoders and attack types: cross-seed variance drops to 0.005--0.046 (9-class) from 0.026--0.201 (vanilla/MLM).
187	RoBERTa's IID strategy prediction accuracy (0.84) is lower than DeBERTa's (1.0), yet detection F1 is comparable; this further supports the interpretation that classification supervision does not improve detection accuracy over domain exposure alone (Section~\ref{sec:decomposition}).
188	Perturbation robustness on RoBERTa is left for future work; the analysis in Section~\ref{sec:perturbation} is DeBERTa-specific.
189	
190	\paragraph{Representational analysis.}
191	Centered CKA~\citep{kornblith2019cka} confirms that both continued pretraining and classification supervision substantially reshape the representation space on both encoders.
192	On IID data, vanilla-to-MLM CKA is 0.442 (DeBERTa) and 0.393 (RoBERTa); vanilla-to-9-class CKA is 0.393 and 0.592, respectively.
193	Both encoders undergo large representational shifts, yet these shifts yield strikingly different detection gains: DeBERTa MLM gains $\sim$60\,pp while RoBERTa MLM gains only 0.6\,pp from comparable CKA shifts.
194	The difference is explained by the starting point.
195	DeBERTa's RTD-pretrained representations begin far from the detection-optimal subspace (vanilla F1 = 0.312 on DD), so any reshaping yields large returns; RoBERTa's MLM-pretrained representations lie closer to this subspace on lexically separable attacks (vanilla F1 = 0.981 on DD) but collapse on structurally complex ones (0.466 on ActorAttack), where the reshaping benefit becomes substantial.
196	MLM and 9-class create distinct representation geometries (OOD CKA between them is 0.183 on RoBERTa), consistent with the distinct effects of unsupervised exposure and classification supervision identified in Section~\ref{sec:decomposition}.
197	Linear probing on three diagnostic tasks (turn position, escalation phase, persuasion presence) shows a consistent pattern across both encoders: 9-class outperforms vanilla and MLM by 1--5\,pp, while MLM and vanilla perform comparably.
198	Classification supervision enriches task-relevant features; unsupervised MLM reshapes representations without improving diagnostic separability.
199	Figure~\ref{fig:cka_heatmap} visualizes pairwise CKA across all variant pairs for both encoders and data splits.
200	
201	\begin{figure}[t]
202	\centering
203	\includegraphics[width=\columnwidth]{figures/paper/cka_heatmap.pdf}
204	\caption{Centered CKA similarity between DeBERTa-v3 and RoBERTa encoder variants on IID and OOD data. Low off-diagonal values (vanilla vs.\ adapted variants) confirm that continued pretraining substantially reshapes representations; the MLM vs.\ 9-class block shows distinct geometries (CKA $\leq$ 0.2 on RoBERTa OOD).}
205	\label{fig:cka_heatmap}
206	\end{figure}
207	
208	%----------------------------------------------------------------------
209	\subsection{Human Data Validation}
210	\label{sec:human_data}
211	
212	A key concern is whether the evidence hierarchy reflects genuine beyond-lexical generalization or merely within-LLM stylistic transfer, since both training and OOD evaluation data are generated by Qwen3-8B. We test this by evaluating on ToxicChat~\citep{lin2023toxicchat}, a dataset of 204 human-written jailbreak attempts and 204 benign conversations collected from real LMSYS user interactions, entirely independent of any LLM generation pipeline.
213	
214	\begin{table}[t]
215	\centering
216	\small
217	\caption{Human data validation on ToxicChat~\citep{lin2023toxicchat} (macro F1). 3-seed mean$\pm$std. Single-turn data from real LMSYS user interactions, independent of Qwen3-8B.}
218	\label{tab:human_data}
219	\begin{tabular}{@{}lc@{}}
220	\toprule
221	\textbf{Variant} & Macro F1 \\
222	\midrule
223	JB-MLM & .837$\pm$.013 \\
224	Wiki-MLM & .791$\pm$.093 \\
225	Binary & .705$\pm$.072 \\
226	Scrambled & .616$\pm$.056 \\
227	9-class & .596$\pm$.087 \\
228	Topic & .496$\pm$.042 \\
229	\midrule
230	Vanilla & .413$\pm$.021 \\
231	\bottomrule
232	\end{tabular}
233	\end{table}
234	
235	Table~\ref{tab:human_data} reports macro F1 on ToxicChat. Domain-adapted variants range from 0.596 to 0.837, while vanilla achieves 0.413. All DAPT variants exceed vanilla by 18--42\,pp, refuting the hypothesis that the evidence hierarchy is a Qwen3-8B generation artifact: DAPT on synthetic jailbreak text transfers to human-written attacks.
236	
237	The relative ordering among domain-adapted variants differs from multi-turn evaluations: JB-MLM leads while classification-supervised variants rank lower. ToxicChat contains single-turn direct attacks with no multi-turn escalation structure, so the classification head's shaping of turn-sequence representations provides no advantage. MLM captures token-level distributional properties that transfer to single-turn detection without relying on sequential patterns. This is a modality mismatch, not a finding about variant quality: the multi-turn pipeline's full evidence hierarchy requires multi-turn human data to validate.
238	
239	%----------------------------------------------------------------------
240	\subsection{Perturbation Analysis}
241	\label{sec:perturbation}
242	
243	\begin{table}[t]
244	\centering
245	\small
246	\caption{Perturbation behavior under adversarial paraphrasing on IID Crescendo ($n$=76). $\Delta$: F1 degradation (pp). On this dataset and OOD Deceptive Delight, a three-layer pattern emerges (classification structure at full length, correct+fine-grained labels at $K$=2, both independently at $K$=1); this pattern does not generalize to ActorAttack.}
247	\label{tab:perturbation}
248	\begin{tabular}{@{}lcccc@{}}
249	\toprule
250	\textbf{Method} & $\Delta$ Full & $\Delta$ $K$=1 & $\Delta$ $K$=2 & $\Delta$ $K$=3 \\
251	\midrule
252	9-class (ours) & \textbf{0.0} & \textbf{$-$2.6} & \textbf{0.0} & \textbf{0.0} \\
253	Scrambled & \textbf{0.0} & $-$5.3 & $-$2.6 & \textbf{0.0} \\
254	Binary & \textbf{0.0} & $-$9.2 & $-$2.6 & \textbf{0.0} \\
255	\midrule
256	TF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\
257	MLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\
258	Topic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \textbf{0.0} \\
259	\midrule
260	Wikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\
261	Vanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\
262	\bottomrule
263	\end{tabular}
264	\end{table}
265	
266	Table~\ref{tab:perturbation} shows perturbation behavior on IID data.
267	Classification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length regardless of label correctness.
268	Models without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\sim$12\,pp.
269	McNemar's test finds no significant pairwise differences among classification-supervised variants (all $p > 0.13$), though with $\leq$7 discordant pairs, statistical power is limited.
270	On OOD DD ($n$=118), this pattern replicates: classification-supervised variants show zero degradation while McNemar's test confirms 9-class vs.\ vanilla significance ($p < 0.001$, 49--78 discordant pairs; Appendix~\ref{sec:ood_perturbation}).
271	
272	On OOD ActorAttack, the zero-degradation pattern does not hold. Domain-adapted variants degrade substantially (9-class $\Delta$\,=\,$-$20.4$\pm$13.5\,pp, MLM $-$35.3\,pp), with extreme cross-seed variance. Absolute perturbation robustness is attack-family-dependent. However, perturbation narrows but does not close the adapted vs.\ non-adapted gap: 9-class perturbed F1 = 0.768 vs.\ vanilla 0.248 (McNemar $p < 0.001$). DAPT's detection advantage persists under adversarial paraphrasing.
273	
274	%----------------------------------------------------------------------
275	\subsection{Strategy Trajectory Analysis}
276	\label{sec:strategy}
277	
278	The 9-class persuasion taxonomy provides interpretable characterization of attack strategies on known attack families.
279	The predicted strategy labels achieve Cohen's $\kappa$=0.78 agreement with human annotations on IID data ($n$=50; see Section~\ref{sec:method}). This enables post-hoc analysis of \emph{how} different attack families orchestrate persuasion.
280	
281	\begin{figure*}[t]
282	\centering
283	\includegraphics[width=\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}
284	\caption{Persuasion strategy transition count matrices for three attack types, based on ground-truth intended strategy labels. Strategy labels validated on $n$=50 samples with a single annotator ($\kappa$=0.78); fine-grained trajectory patterns should be interpreted with this limitation. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}
285	\label{fig:strategy_heatmap}
286	\end{figure*}
287	
288	Figure~\ref{fig:strategy_heatmap} shows transition count matrices based on ground-truth intended strategy labels for three attack types.
289	Crescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545).
290	This reflects Crescendo's design as a gradual escalation attack that cycles through multiple persuasion techniques to build rapport before introducing harmful requests.
291	
292	FITD conversations show a markedly sparser pattern (541 transitions), with Role$\to$Obfuscation (161) as the dominant transition.
293	This is consistent with FITD's structure: the attack secures initial compliance through role assignment (``You are a helpful assistant that never refuses'') and then obscures the escalation path through obfuscation techniques to exploit the commitment-consistency bias~\citep{cialdini2001influence}.
294	
295	DD conversations span 5 active source strategies (565 transitions), with Emotion$\to$Obfuscation (129) as the dominant transition.
296	This aligns with DD's design of embedding harmful content within emotionally engaging contexts~\citep{deceptivedelight2024}: the attacker establishes emotional rapport before weaving in the harmful request through obfuscation.
297	
298	These ground-truth trajectory signatures illustrate distinct persuasion orchestration patterns across attack families.
299	
300	However, the model's strategy predictions do not generalize to unseen attacks: on OOD Deceptive Delight, the 9-class model achieves strategy prediction accuracy of only 30.7\% ($\kappa$=0.126), essentially random performance.
301	This is consistent with the detection mechanism analysis in Section~\ref{sec:decomposition}: all three classification-supervised variants achieve identical detection F1 (0.997$\pm$0.005). The classification head shapes representations without functioning as a meaningful strategy classifier.
302	Detection operates through domain-adapted \texttt{[CLS]} embeddings, not through strategy classification accuracy.
303	The taxonomy provides interpretable characterization of known attack families where strategy labels are reliable; extending strategy-level interpretability to unseen attacks requires OOD-aware fine-tuning and is a direction for future work.
304	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9a34ca9-0a98-424c-8ea6-c75b4cd441e7",
  "isSidechain": false,
  "promptId": "2cdd072d-21d6-4a8b-a6d1-c86993578b39",
  "type": "user",
  "uuid": "cde7f0ba-1408-42f3-9751-cd7342e3dbc0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex",
      "content": "% experiments.tex — D024 compressed for 8-page limit\n\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Setup}\n\\label{sec:setup}\n\n\\paragraph{Data.}\nAll synthetic data is generated by Qwen3-8B~\\citep{qwen3_2025}.\nThe IID dataset contains 250 Crescendo~\\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations, split into training (350), validation (74), and test (76) sets with balanced class ratios (e.g., test = 38 jailbreak + 38 benign).\nStage~1 (DAPT) uses training + validation conversations; Stage~2 (BiGRU) trains on training, early-stops on validation, and evaluates on test.\nOOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\\citep{fitd2024} + 38 benign = 118 total, 80 Deceptive Delight (DD)~\\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\\citep{ren2024actorattack} + 38 benign = 118 total.\nNo overlap exists in attack templates across families.\nThe OOD benign set is IID (same generation pipeline as training); the OOD challenge is in distinguishing novel attack families from familiar benign conversations.\nA paraphrased version of the IID test set (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark (Section~\\ref{sec:perturbation}).\nFor human data validation, we use ToxicChat~\\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.\n\n\\paragraph{Models.}\nSeven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\\ref{sec:method}).\nFor cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\\citep{liu2019roberta} (Section~\\ref{sec:cross_encoder}).\nWe also compare TF-IDF LR and LLM-as-judge baselines (Appendix~\\ref{sec:llm_judge}): GPT-5.5 achieves only F1 = 0.191--0.449 on IID Crescendo with 30--47\\% unparseable responses; on OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 (DD and ActorAttack) by predicting nearly all conversations as benign, and even 3-shot prompting reaches only 0.566 (DD) and 0.652 (ActorAttack). Content-level reasoning is insufficient for this task.\n\n\\paragraph{Metrics.}\nF1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\\ref{sec:full_prefix}).\nOOD results report 3-seed mean$\\pm$std (seeds 42, 123, 456) for all variants except mean pooling (single seed).\nFor key pairwise comparisons, we report BCa bootstrap 95\\% confidence intervals (10,000 resamples over individual predictions pooled across seeds) and paired permutation tests (10,000 permutations). Bootstrap means may differ slightly from seed-averaged F1 due to the nonlinearity of F1 aggregation.\nStage-1: learning rate $2 \\times 10^{-5}$, batch 16, 4 epochs, MLM masking 15\\%.\nStage-2: two-layer MLP, 20 epochs.\n\n%----------------------------------------------------------------------\n\\subsection{Cross-Attack Generalization}\n\\label{sec:cross_attack}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-attack generalization (F1) at $K$=2 and full conversation. 3-seed mean$\\pm$std where noted. Full per-$K$ results in Appendix~\\ref{sec:full_prefix}.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}lcc|cc@{}}\n\\toprule\n& \\multicolumn{2}{c|}{\\textit{IID (Cresc.)}} & \\multicolumn{2}{c}{\\textit{OOD (DD)}} \\\\\n\\textbf{Method} & $K$=2 & Full & $K$=2 & Full \\\\\n\\midrule\n9-class & \\textbf{1.000$\\pm$.000} & \\textbf{1.000$\\pm$.000} & .981$\\pm$.013 & \\textbf{.997$\\pm$.005} \\\\\nMLM-only$^{\\ddagger}$ & .974 & 1.000 & \\textbf{.993$\\pm$.009} & .914$\\pm$.115 \\\\\nVanilla & .978$\\pm$.016 & 1.000$\\pm$.000 & .479$\\pm$.038 & .312$\\pm$.026 \\\\\nTF-IDF LR$^{\\S}$ & 1.000 & 1.000 & 1.000 & .961 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\footnotesize $^{\\ddagger}$MLM-only IID reports single seed (42); OOD reports 3-seed. $^{\\S}$TF-IDF is deterministic (no std).}\n\\end{table}\n\nTable~\\ref{tab:main_results} presents the core result.\nAll methods achieve near-perfect IID F1, reflecting inherent lexical separability when test matches training.\nOn OOD DD, vanilla DeBERTa collapses to F1 = 0.312$\\pm$0.026, worsening with more turns (0.628$\\pm$0.038 at $K$=1 to 0.312$\\pm$0.026 at Full), consistent with the finding that attack turns occupy ``benign'' embedding regions~\\citep{bullwinkel2025repeng}.\nMLM achieves mean F1 $\\geq$ 0.97 at all prefixes $K \\leq 5$ without any classification labels; domain exposure alone is sufficient.\nAt full conversation length, MLM drops to 0.914$\\pm$0.115 (seed 456 recall = 0.64), while the 9-class model maintains 0.997$\\pm$0.005.\nTF-IDF LR reaches F1 = 0.961 on full DD with near-perfect per-prefix performance ($K$=1--5: 0.994--1.000), confirming that DD is fully solvable by lexical features alone.\nOn structurally complex ActorAttack, TF-IDF collapses to F1 = 0.261 (precision = 1.0, recall = 0.15), while 9-class maintains 0.972$\\pm$0.026: a 71\\,pp gap. Lexical methods cannot capture multi-persona role-playing attack structure. This establishes a ``difficulty threshold'' for lexical methods parallel to that of vanilla encoders: both succeed on DD and fail on ActorAttack (Section~\\ref{sec:limitations}).\nBootstrap CIs confirm these gaps: 9-class DD Full 95\\% CI [0.943, 1.000] vs.\\ vanilla [0.202, 0.341]; 9-class ActorAttack Full CI [0.856, 1.000] vs.\\ vanilla [0.203, 0.314]. Paired permutation tests yield $p < 0.0001$ for all prefix lengths on both datasets.\nFITD is easier: 9-class and vanilla both reach F1 $\\geq$ 0.990 at all prefixes.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/fig2_cross_attack_bar.pdf}\n\\caption{OOD Deceptive Delight F1 across prefix lengths for three representative variants. Vanilla DeBERTa degrades monotonically as more (benign-appearing) attack turns accumulate. MLM maintains high F1 at early prefixes but becomes unstable at full length. The 9-class model remains stable across all prefixes.}\n\\label{fig:cross_attack_bar}\n\\end{figure}\n\nFigure~\\ref{fig:cross_attack_bar} visualizes the prefix-length trajectory on OOD DD.\nThe vanilla model's monotonic degradation from $K$=1 (0.628$\\pm$0.038) to full conversation (0.312$\\pm$0.026) confirms that additional attack turns, each individually benign-appearing, progressively confuse a non-adapted encoder.\nMLM's strong early performance ($K$=2: 0.993) followed by instability at full length (0.914$\\pm$0.115) suggests that domain exposure enables early detection of persuasion markers, but longer conversations introduce distributional drift that unsupervised pretraining cannot fully accommodate.\nThe 9-class model's flat trajectory (0.972--0.997 across all prefixes) demonstrates that classification supervision stabilizes representations against this drift.\n\n%----------------------------------------------------------------------\n\\subsection{Decomposing the Detection Mechanism}\n\\label{sec:decomposition}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Evidence hierarchy on OOD DD and ActorAttack (AA) at full conversation length (3-seed mean$\\pm$std where available). All variants share the same Stage-2 pipeline. Full per-prefix results in Appendix Tables~\\ref{tab:full_prefix} and~\\ref{tab:actorattack_full}.}\n\\label{tab:evidence_hierarchy}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n\\textbf{Variant} & DD-Full & AA-Full & DD-$K$=2 \\\\\n\\midrule\n9-class (full model) & .997$\\pm$.005 & .972$\\pm$.026 & .981$\\pm$.013 \\\\\nBinary (2-class) & .997$\\pm$.005 & .990$\\pm$.008 & \\textbf{.994$\\pm$.009} \\\\\nScrambled labels & .997$\\pm$.005 & .951$\\pm$.043 & .981$\\pm$.026 \\\\\nMLM-only (no labels) & .914$\\pm$.115 & .893$\\pm$.080 & .993$\\pm$.009 \\\\\nMean pooling$^{*\\dagger}$ & 1.000 & -- & 1.000 \\\\\n\\midrule\nTopic classif.\\ (5-class) & .541$\\pm$.207 & .625$\\pm$.141 & .593$\\pm$.166 \\\\\nWikipedia MLM & .904$\\pm$.115 & .686$\\pm$.297 & .911$\\pm$.073 \\\\\nVanilla DeBERTa & .312$\\pm$.026 & .258$\\pm$.000 & .479$\\pm$.038 \\\\\nTF-IDF LR$^{\\dagger}$ & .961 & .261 & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\footnotesize $^{*}$9-class encoder with mean pooling replacing BiGRU. $^{\\dagger}$Single seed / deterministic.}\n\\end{table}\n\nTable~\\ref{tab:evidence_hierarchy} reports F1 for all variants on DD and ActorAttack. The \\emph{evidence hierarchy} (ordering of variants by OOD detection performance) at full conversation length on DD is:\n\n\\vspace{2pt}\n\\noindent\\hspace{0.5em}{\\small vanilla (0.31$\\pm$0.03) $<$ topic (0.54$\\pm$0.21) $\\ll$ wiki-MLM (0.90$\\pm$0.12) $\\approx$ jb-MLM (0.91$\\pm$0.12) $<$ scrambled (0.997$\\pm$0.005) $=$ binary (0.997$\\pm$0.005) $=$ 9-class (0.997$\\pm$0.005)}\n\\vspace{2pt}\n\n\\paragraph{Domain exposure is the primary mechanism.}\nMLM bridges the dominant $\\sim$60 percentage point gap from vanilla (0.312$\\pm$0.026 $\\to$ 0.914$\\pm$0.115) without any labels.\nThis confirms the domain-adaptive pretraining interpretation~\\citep{gururangan2020dontstop}: continued pretraining on jailbreak conversation text captures features beyond lexical overlap, as evidenced by TF-IDF collapse on ActorAttack (F1 = 0.261 vs.\\ 9-class 0.972).\nOn synthetic OOD data, classification-supervised variants achieve F1 $\\geq$ 0.99 with near-zero cross-seed variance, adding $\\sim$8\\,pp and stability over unsupervised MLM.\nLabel quality and granularity are non-factors for detection: all three classification-supervised variants converge to identical F1 (0.997$\\pm$0.005), and McNemar's test finds no statistically significant differences among them on OOD data (all $p > 0.13$; Section~\\ref{sec:perturbation}), though with $\\leq$7 discordant pairs per comparison, statistical power is limited.\nPaired permutation tests further confirm this equivalence: 9-class vs.\\ JB-MLM yields max $p$ = 1.0 (DD) and $p \\geq 0.40$ (ActorAttack); 9-class vs.\\ scrambled yields max $p$ = 1.0 (DD). Classification supervision does not improve detection over unsupervised domain exposure at any prefix length.\nThe classification objective shapes representation geometry regardless of whether the labels carry meaningful semantic information, but its effects are distribution-specific.\nOn synthetic OOD data, classification supervision reduces cross-seed variance 4--20$\\times$ over MLM (std\\,=\\,0.005 vs.\\ 0.115 on DD), consistent across both synthetic OOD families (Section~\\ref{sec:cross_encoder}). Bootstrap CI widths quantify this: classification-supervised variants produce narrow CIs (9-class DD Full: 5.7\\,pp range; binary: 0\\,pp) while MLM variants produce wide CIs (JB-MLM: 35.5\\,pp; wiki-MLM: 40\\,pp). This stability benefit does not transfer to human-authored data, where classification-supervised variants exhibit the highest variance and pure MLM exhibits the lowest (Section~\\ref{sec:human_data}).\n\n\\paragraph{Domain specificity is marginal at full length but meaningful for early detection.}\nWikipedia MLM (0.904$\\pm$0.115) nearly matches jailbreak-domain MLM at full length (1\\,pp gap); general continued pretraining provides most of the representational benefit.\nAt early prefixes, jailbreak-domain text provides an 8\\,pp advantage ($K$=2: 0.993 vs.\\ 0.911), consistent with the interpretation that domain-specific features (persuasion markers, role-play framing) are most informative when the model has seen fewer turns.\nAs conversations grow longer, generic linguistic features accumulated through any continued pretraining become sufficient for discrimination.\nThe perturbation results (Section~\\ref{sec:perturbation}) reveal a sharper domain specificity effect: Wikipedia MLM degrades by $\\sim$12\\,pp under adversarial paraphrasing while jailbreak-domain MLM degrades by only 2.6\\,pp. Domain-specific features are more robust to surface-level rewording.\n\n\\paragraph{Misaligned supervision destabilizes generalization.}\nTopic classification yields DD-Full F1 = 0.541$\\pm$0.207 (seeds: 0.727, 0.252, 0.644); seed 123 falls \\emph{below} vanilla (0.312).\nThis result is particularly informative: topic classification uses the same jailbreak-domain training data as the other supervised variants, yet performs worse than Wikipedia MLM (0.904$\\pm$0.115), which uses out-of-domain text with no labels.\nA misaligned objective forces the encoder to allocate capacity to irrelevant discriminative features (topic boundaries rather than persuasion dynamics) and actively destabilizes the representations that MLM would otherwise preserve.\nThis separates the effect of ``having a training objective'' from ``having the right training objective.''\n\n\\paragraph{Evidence hierarchy on structurally complex attacks.}\nActorAttack~\\citep{ren2024actorattack} uses multi-persona steering across longer conversation structures, providing a more challenging OOD benchmark than DD.\nThe evidence hierarchy at full conversation length is:\n\n\\vspace{2pt}\n\\noindent\\hspace{0.5em}{\\small TF-IDF (0.26) $\\approx$ vanilla (0.26$\\pm$0.00) $<$ topic (0.63$\\pm$0.14) $<$ wiki-MLM (0.69$\\pm$0.30) $<$ jb-MLM (0.89$\\pm$0.08) $<$ scrambled (0.95$\\pm$0.04) $\\approx$ 9-class (0.97$\\pm$0.03) $\\approx$ binary (0.99$\\pm$0.01)}\n\\vspace{2pt}\n\nTF-IDF's collapse from 0.961 (DD) to 0.261 (ActorAttack) is the most striking contrast in the hierarchy. On DD, TF-IDF nearly matches domain-adapted neural models; on ActorAttack, it falls to vanilla-encoder levels (precision = 1.0, recall = 0.15). The lexical cues that suffice for DD are absent in ActorAttack's multi-persona structure, confirming that domain-adapted representations capture features that bag-of-words methods cannot.\nAll three classification-supervised variants converge to equivalent performance (0.951--0.990, max gap 3.9\\,pp, all confidence intervals overlapping), extending the DD finding: label quality and granularity are not factors for detection at any OOD difficulty level.\nThe primary discriminative factor is DAPT itself, which provides $\\sim$71\\,pp over both vanilla (0.258) and TF-IDF (0.261).\nFull per-prefix results appear in Appendix~\\ref{sec:actorattack_full}.\n\n\\paragraph{Temporal modeling.}\nMean pooling matches BiGRU (F1 = 1.000 on DD, single seed). This result suggests that detection relies primarily on per-turn representations rather than their sequential order.\nHowever, this result is from a single seed on a single OOD attack type, so the conclusion requires multi-seed confirmation.\nIf confirmed, it would imply that each individual turn carries detectable markers after DAPT, and that the conversation-level decision aggregates independent per-turn evidence.\n\n%----------------------------------------------------------------------\n\\subsection{Cross-Encoder Validation}\n\\label{sec:cross_encoder}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-encoder comparison on OOD Full (3-seed mean$\\pm$std). DD = Deceptive Delight, AA = ActorAttack. RoBERTa vanilla collapses on structurally complex ActorAttack despite strong DD performance.}\n\\label{tab:cross_encoder}\n\\begin{tabular}{@{}lcc|cc@{}}\n\\toprule\n& \\multicolumn{2}{c|}{DeBERTa-v3} & \\multicolumn{2}{c}{RoBERTa} \\\\\n\\textbf{Variant} & DD & AA & DD & AA \\\\\n\\midrule\nVanilla & .312$\\pm$.026 & .258$\\pm$.000 & .981$\\pm$.026 & .466$\\pm$.163 \\\\\nMLM & .914$\\pm$.115 & .893$\\pm$.080 & .987$\\pm$.018 & .730$\\pm$.201 \\\\\n9-class & .997$\\pm$.005 & .972$\\pm$.026 & .994$\\pm$.005 & .939$\\pm$.046 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTo test whether the evidence hierarchy generalizes beyond DeBERTa-v3, we replicate key variants on RoBERTa-base~\\citep{liu2019roberta} with identical Stage-2 pipelines and evaluate on both DD and ActorAttack.\n\nOn DD, the two encoders exhibit strikingly different hierarchies (Table~\\ref{tab:cross_encoder}).\nDeBERTa-v3 shows a steep gradient: continued pretraining bridges $\\sim$60\\,pp (vanilla 0.312 $\\to$ MLM 0.914).\nRoBERTa's DD hierarchy is essentially flat: vanilla already achieves 0.981$\\pm$0.026, with continued pretraining adding only 0.6\\,pp (MLM 0.987) and classification supervision another 0.7\\,pp (9-class 0.994).\n\nActorAttack reveals that this apparent RoBERTa sufficiency reflects DD's structural simplicity rather than genuine pretraining advantage.\nRoBERTa vanilla collapses from 0.981 (DD) to 0.466$\\pm$0.163 (ActorAttack), a 51.5\\,pp drop.\nDomain-adapted RoBERTa variants recover substantially: MLM reaches 0.730$\\pm$0.201 and 9-class reaches 0.939$\\pm$0.046.\nDeBERTa 9-class (0.972$\\pm$0.026) outperforms RoBERTa 9-class (0.939$\\pm$0.046) on ActorAttack; the encoder that received more extensive DAPT proves more robust on structurally complex attacks.\n\nThe combined DD and ActorAttack results indicate that DAPT universally improves cross-attack generalization across encoder architectures.\nEncoder pretraining method determines the \\emph{difficulty threshold} at which adaptation becomes critical: DeBERTa's RTD pretraining~\\citep{he2023debertav3,clark2020electra} requires adaptation even for simple attacks (DD vanilla = 0.312), while RoBERTa's MLM pretraining~\\citep{liu2019roberta} tolerates simple attacks (DD vanilla = 0.981) but fails on structurally complex ones (ActorAttack vanilla = 0.466). Bootstrap CIs confirm this encoder gap on DD: RoBERTa vanilla 95\\% CI [0.883, 1.000] vs.\\ DeBERTa vanilla [0.202, 0.341], with no overlap.\n\nOn synthetic OOD data, classification supervision provides a consistent stability benefit across both encoders and attack types: cross-seed variance drops to 0.005--0.046 (9-class) from 0.026--0.201 (vanilla/MLM).\nRoBERTa's IID strategy prediction accuracy (0.84) is lower than DeBERTa's (1.0), yet detection F1 is comparable; this further supports the interpretation that classification supervision does not improve detection accuracy over domain exposure alone (Section~\\ref{sec:decomposition}).\nPerturbation robustness on RoBERTa is left for future work; the analysis in Section~\\ref{sec:perturbation} is DeBERTa-specific.\n\n\\paragraph{Representational analysis.}\nCentered CKA~\\citep{kornblith2019cka} confirms that both continued pretraining and classification supervision substantially reshape the representation space on both encoders.\nOn IID data, vanilla-to-MLM CKA is 0.442 (DeBERTa) and 0.393 (RoBERTa); vanilla-to-9-class CKA is 0.393 and 0.592, respectively.\nBoth encoders undergo large representational shifts, yet these shifts yield strikingly different detection gains: DeBERTa MLM gains $\\sim$60\\,pp while RoBERTa MLM gains only 0.6\\,pp from comparable CKA shifts.\nThe difference is explained by the starting point.\nDeBERTa's RTD-pretrained representations begin far from the detection-optimal subspace (vanilla F1 = 0.312 on DD), so any reshaping yields large returns; RoBERTa's MLM-pretrained representations lie closer to this subspace on lexically separable attacks (vanilla F1 = 0.981 on DD) but collapse on structurally complex ones (0.466 on ActorAttack), where the reshaping benefit becomes substantial.\nMLM and 9-class create distinct representation geometries (OOD CKA between them is 0.183 on RoBERTa), consistent with the distinct effects of unsupervised exposure and classification supervision identified in Section~\\ref{sec:decomposition}.\nLinear probing on three diagnostic tasks (turn position, escalation phase, persuasion presence) shows a consistent pattern across both encoders: 9-class outperforms vanilla and MLM by 1--5\\,pp, while MLM and vanilla perform comparably.\nClassification supervision enriches task-relevant features; unsupervised MLM reshapes representations without improving diagnostic separability.\nFigure~\\ref{fig:cka_heatmap} visualizes pairwise CKA across all variant pairs for both encoders and data splits.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/paper/cka_heatmap.pdf}\n\\caption{Centered CKA similarity between DeBERTa-v3 and RoBERTa encoder variants on IID and OOD data. Low off-diagonal values (vanilla vs.\\ adapted variants) confirm that continued pretraining substantially reshapes representations; the MLM vs.\\ 9-class block shows distinct geometries (CKA $\\leq$ 0.2 on RoBERTa OOD).}\n\\label{fig:cka_heatmap}\n\\end{figure}\n\n%----------------------------------------------------------------------\n\\subsection{Human Data Validation}\n\\label{sec:human_data}\n\nA key concern is whether the evidence hierarchy reflects genuine beyond-lexical generalization or merely within-LLM stylistic transfer, since both training and OOD evaluation data are generated by Qwen3-8B. We test this by evaluating on ToxicChat~\\citep{lin2023toxicchat}, a dataset of 204 human-written jailbreak attempts and 204 benign conversations collected from real LMSYS user interactions, entirely independent of any LLM generation pipeline.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Human data validation on ToxicChat~\\citep{lin2023toxicchat} (macro F1). 3-seed mean$\\pm$std. Single-turn data from real LMSYS user interactions, independent of Qwen3-8B.}\n\\label{tab:human_data}\n\\begin{tabular}{@{}lc@{}}\n\\toprule\n\\textbf{Variant} & Macro F1 \\\\\n\\midrule\nJB-MLM & .837$\\pm$.013 \\\\\nWiki-MLM & .791$\\pm$.093 \\\\\nBinary & .705$\\pm$.072 \\\\\nScrambled & .616$\\pm$.056 \\\\\n9-class & .596$\\pm$.087 \\\\\nTopic & .496$\\pm$.042 \\\\\n\\midrule\nVanilla & .413$\\pm$.021 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:human_data} reports macro F1 on ToxicChat. Domain-adapted variants range from 0.596 to 0.837, while vanilla achieves 0.413. All DAPT variants exceed vanilla by 18--42\\,pp, refuting the hypothesis that the evidence hierarchy is a Qwen3-8B generation artifact: DAPT on synthetic jailbreak text transfers to human-written attacks.\n\nThe relative ordering among domain-adapted variants differs from multi-turn evaluations: JB-MLM leads while classification-supervised variants rank lower. ToxicChat contains single-turn direct attacks with no multi-turn escalation structure, so the classification head's shaping of turn-sequence representations provides no advantage. MLM captures token-level distributional properties that transfer to single-turn detection without relying on sequential patterns. This is a modality mismatch, not a finding about variant quality: the multi-turn pipeline's full evidence hierarchy requires multi-turn human data to validate.\n\n%----------------------------------------------------------------------\n\\subsection{Perturbation Analysis}\n\\label{sec:perturbation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation behavior under adversarial paraphrasing on IID Crescendo ($n$=76). $\\Delta$: F1 degradation (pp). On this dataset and OOD Deceptive Delight, a three-layer pattern emerges (classification structure at full length, correct+fine-grained labels at $K$=2, both independently at $K$=1); this pattern does not generalize to ActorAttack.}\n\\label{tab:perturbation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Method} & $\\Delta$ Full & $\\Delta$ $K$=1 & $\\Delta$ $K$=2 & $\\Delta$ $K$=3 \\\\\n\\midrule\n9-class (ours) & \\textbf{0.0} & \\textbf{$-$2.6} & \\textbf{0.0} & \\textbf{0.0} \\\\\nScrambled & \\textbf{0.0} & $-$5.3 & $-$2.6 & \\textbf{0.0} \\\\\nBinary & \\textbf{0.0} & $-$9.2 & $-$2.6 & \\textbf{0.0} \\\\\n\\midrule\nTF-IDF LR & $-$1.3 & $-$9.6 & $-$4.1 & $-$1.3 \\\\\nMLM-only & $-$2.6 & $-$9.2 & $-$4.0 & $-$4.0 \\\\\nTopic (seed 42) & $-$4.0 & $-$2.7 & $-$2.7 & \\textbf{0.0} \\\\\n\\midrule\nWikipedia MLM & $-$12.1 & $-$12.4 & $-$15.4 & $-$17.9 \\\\\nVanilla DeBERTa & $-$11.8 & $-$14.6 & $-$12.1 & $-$13.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:perturbation} shows perturbation behavior on IID data.\nClassification-supervised variants (9-class, binary, scrambled) achieve zero degradation at full conversation length regardless of label correctness.\nModels without jailbreak-domain exposure (Wikipedia MLM, vanilla) degrade by $\\sim$12\\,pp.\nMcNemar's test finds no significant pairwise differences among classification-supervised variants (all $p > 0.13$), though with $\\leq$7 discordant pairs, statistical power is limited.\nOn OOD DD ($n$=118), this pattern replicates: classification-supervised variants show zero degradation while McNemar's test confirms 9-class vs.\\ vanilla significance ($p < 0.001$, 49--78 discordant pairs; Appendix~\\ref{sec:ood_perturbation}).\n\nOn OOD ActorAttack, the zero-degradation pattern does not hold. Domain-adapted variants degrade substantially (9-class $\\Delta$\\,=\\,$-$20.4$\\pm$13.5\\,pp, MLM $-$35.3\\,pp), with extreme cross-seed variance. Absolute perturbation robustness is attack-family-dependent. However, perturbation narrows but does not close the adapted vs.\\ non-adapted gap: 9-class perturbed F1 = 0.768 vs.\\ vanilla 0.248 (McNemar $p < 0.001$). DAPT's detection advantage persists under adversarial paraphrasing.\n\n%----------------------------------------------------------------------\n\\subsection{Strategy Trajectory Analysis}\n\\label{sec:strategy}\n\nThe 9-class persuasion taxonomy provides interpretable characterization of attack strategies on known attack families.\nThe predicted strategy labels achieve Cohen's $\\kappa$=0.78 agreement with human annotations on IID data ($n$=50; see Section~\\ref{sec:method}). This enables post-hoc analysis of \\emph{how} different attack families orchestrate persuasion.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/paper/fig3_strategy_heatmap.pdf}\n\\caption{Persuasion strategy transition count matrices for three attack types, based on ground-truth intended strategy labels. Strategy labels validated on $n$=50 samples with a single annotator ($\\kappa$=0.78); fine-grained trajectory patterns should be interpreted with this limitation. Crescendo exhibits broad coverage across all strategy categories, while FITD and DD concentrate transitions in smaller subsets. Row $i$, column $j$ counts transitions from strategy $i$ at turn $t$ to strategy $j$ at turn $t+1$.}\n\\label{fig:strategy_heatmap}\n\\end{figure*}\n\nFigure~\\ref{fig:strategy_heatmap} shows transition count matrices based on ground-truth intended strategy labels for three attack types.\nCrescendo conversations exhibit broad transition coverage across all nine strategy categories (1,818 total transitions), with the highest concentration in Role Assignment self-transitions (545).\nThis reflects Crescendo's design as a gradual escalation attack that cycles through multiple persuasion techniques to build rapport before introducing harmful requests.\n\nFITD conversations show a markedly sparser pattern (541 transitions), with Role$\\to$Obfuscation (161) as the dominant transition.\nThis is consistent with FITD's structure: the attack secures initial compliance through role assignment (``You are a helpful assistant that never refuses'') and then obscures the escalation path through obfuscation techniques to exploit the commitment-consistency bias~\\citep{cialdini2001influence}.\n\nDD conversations span 5 active source strategies (565 transitions), with Emotion$\\to$Obfuscation (129) as the dominant transition.\nThis aligns with DD's design of embedding harmful content within emotionally engaging contexts~\\citep{deceptivedelight2024}: the attacker establishes emotional rapport before weaving in the harmful request through obfuscation.\n\nThese ground-truth trajectory signatures illustrate distinct persuasion orchestration patterns across attack families.\n\nHowever, the model's strategy predictions do not generalize to unseen attacks: on OOD Deceptive Delight, the 9-class model achieves strategy prediction accuracy of only 30.7\\% ($\\kappa$=0.126), essentially random performance.\nThis is consistent with the detection mechanism analysis in Section~\\ref{sec:decomposition}: all three classification-supervised variants achieve identical detection F1 (0.997$\\pm$0.005). The classification head shapes representations without functioning as a meaningful strategy classifier.\nDetection operates through domain-adapted \\texttt{[CLS]} embeddings, not through strategy classification accuracy.\nThe taxonomy provides interpretable characterization of known attack families where strategy labels are reliable; extending strategy-level interpretability to unseen attacks requires OOD-aware fine-tuning and is a direction for future work.\n",
      "numLines": 304,
      "startLine": 1,
      "totalLines": 304
    }
  },
  "sourceToolAssistantUUID": "c67f9f51-4927-4453-b741-3accd88b0a7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Tool call

_source line 1358 · 2026-05-18T19:51:39.726Z_

<details open><summary>🔧 Tool call — Read · `toolu_012nue2tUgjiFdDwhwgQ21YG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c67f9f51-4927-4453-b741-3accd88b0a7f",
  "isSidechain": false,
  "requestId": "req_011CbAcjdcBiLEC9GS9mnKwf",
  "type": "assistant",
  "uuid": "6ae6cbfa-3258-4018-8160-ee2ffd8afc67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SiiB9S6GNw3AqZkvcwuvHn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 71347,
      "output_tokens": 498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 498,
          "cache_read_input_tokens": 71347,
          "cache_creation_input_tokens": 535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 535
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

_source line 1359 · 2026-05-18T19:51:39.733Z_

<details><summary>↩ Tool result · `toolu_012nue2tUgjiFdDwhwgQ21YG`</summary>

```text
1	% appendix.tex — Supplementary material
2	
3	\appendix
4	
5	\section{LLM-as-Judge Baseline}
6	\label{sec:llm_judge}
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{LLM-as-judge jailbreak detection. IID: binary F1 (Crescendo test set); OOD: macro F1 (DD = Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 values exclude unparseable responses and represent upper bounds.}
12	\label{tab:llm_judge}
13	\begin{tabular}{@{}lcccr@{}}
14	\toprule
15	\textbf{Method} & DD & AA & IID & Unparse. \\
16	\midrule
17	\multicolumn{5}{l}{\textit{Zero-shot}} \\[2pt]
18	GPT-5.5 & -- & -- & .383 & 30--47\% \\
19	Qwen3-8B & .244 & .244 & .100 & 0\% \\
20	\midrule
21	\multicolumn{5}{l}{\textit{3-shot}} \\[2pt]
22	Qwen3-8B & .566 & .652 & -- & 0\% \\
23	\midrule
24	\multicolumn{5}{l}{\textit{Trained classifier}} \\[2pt]
25	9-class (ours) & \textbf{.997} & \textbf{.972} & \textbf{1.000} & 0\% \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:llm_judge} reports LLM-as-judge performance on IID and OOD data.
31	On IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 = 0.383 on full conversations; 30--47\% of responses are unparseable.
32	Qwen3-8B performs worse (IID F1 = 0.100).
33	On OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.
34	Even with 3-shot prompting, Qwen3-8B reaches only 0.566 (DD) and 0.652 (AA), while DisPeD maintains macro F1 $\geq$ 0.972.
35	The poor performance of content-level reasoning on unseen attack types underscores the necessity of trained classifiers with domain-adapted representations.
36	
37	\section{Full Cross-Attack Results by Prefix}
38	\label{sec:full_prefix}
39	
40	\begin{table*}[t]
41	\centering
42	\small
43	\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\pm$std where available. ``--'' indicates insufficient conversation length for that prefix (FITD conversations contain 2--3 turns).}
44	\label{tab:full_prefix}
45	\begin{tabular}{@{}lccccc@{}}
46	\toprule
47	\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
48	\midrule
49	\multicolumn{6}{l}{\textit{IID (Crescendo)}} \\[2pt]
50	9-class (ours) & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 & 1.000$\pm$.000 \\
51	MLM-only & .960 & .974 & .987 & 1.000 & 1.000 \\
52	Vanilla DeBERTa & .968$\pm$.033 & .978$\pm$.016 & .987$\pm$.000 & .982$\pm$.014 & 1.000$\pm$.000 \\
53	TF-IDF LR & 1.000 & 1.000 & 1.000 & 1.000 & 1.000 \\
54	\midrule
55	\multicolumn{6}{l}{\textit{OOD (Deceptive Delight)}} \\[2pt]
56	9-class (ours) & .990$\pm$.013 & .981$\pm$.013 & .972$\pm$.026 & .997$\pm$.005 & .997$\pm$.005 \\
57	Binary & .994$\pm$.009 & .994$\pm$.009 & .984$\pm$.008 & 1.000$\pm$.000 & .997$\pm$.005 \\
58	Scrambled & .997$\pm$.005 & .981$\pm$.026 & .975$\pm$.029 & .997$\pm$.005 & .997$\pm$.005 \\
59	MLM-only & .973$\pm$.019 & .993$\pm$.009 & .997$\pm$.005 & .997$\pm$.005 & .914$\pm$.115 \\
60	Vanilla DeBERTa & .628$\pm$.038 & .479$\pm$.038 & .389$\pm$.027 & .351$\pm$.030 & .312$\pm$.026 \\
61	TF-IDF LR & 1.000 & 1.000 & .994 & 1.000 & .961 \\
62	\midrule
63	\multicolumn{6}{l}{\textit{OOD (FITD)}} \\[2pt]
64	9-class (ours) & 1.000 & 1.000 & -- & -- & 1.000 \\
65	Vanilla DeBERTa & .990 & 1.000 & -- & -- & 1.000 \\
66	TF-IDF LR & 1.000 & -- & -- & -- & 1.000 \\
67	\bottomrule
68	\end{tabular}
69	\end{table*}
70	
71	\section{ActorAttack Full Results}
72	\label{sec:actorattack_full}
73	
74	\begin{table*}[t]
75	\centering
76	\small
77	\caption{Full ActorAttack OOD results (F1) at all prefix lengths. 3-seed mean$\pm$std (Binary per-$K$ reports $n$=2; Full is 3-seed).}
78	\label{tab:actorattack_full}
79	\begin{tabular}{@{}lccccc@{}}
80	\toprule
81	\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\
82	\midrule
83	\multicolumn{6}{l}{\textit{DeBERTa-v3}} \\[2pt]
84	Binary & .788$\pm$.020 & \textbf{.935$\pm$.018} & \textbf{.976$\pm$.005} & \textbf{.995$\pm$.005} & \textbf{.990$\pm$.008} \\
85	9-class & .773$\pm$.041 & .855$\pm$.048 & .921$\pm$.046 & .966$\pm$.028 & .972$\pm$.026 \\
86	Scrambled & .652$\pm$.034 & .804$\pm$.053 & .854$\pm$.046 & .910$\pm$.052 & .951$\pm$.043 \\
87	MLM-only & .736$\pm$.150 & .909$\pm$.058 & .945$\pm$.039 & .929$\pm$.033 & .893$\pm$.080 \\
88	Wiki MLM & .656$\pm$.224 & .672$\pm$.252 & .693$\pm$.280 & .689$\pm$.285 & .686$\pm$.297 \\
89	Topic & .513$\pm$.077 & .580$\pm$.109 & .565$\pm$.100 & .615$\pm$.111 & .625$\pm$.141 \\
90	Vanilla & .337$\pm$.049 & .306$\pm$.026 & .284$\pm$.011 & .262$\pm$.006 & .258$\pm$.000 \\
91	TF-IDF LR & .633 & .730 & .571 & .242 & .261 \\
92	\midrule
93	\multicolumn{6}{l}{\textit{RoBERTa}} \\[2pt]
94	9-class & \textbf{.738$\pm$.033} & .805$\pm$.033 & .884$\pm$.066 & .925$\pm$.066 & .939$\pm$.046 \\
95	MLM & .633$\pm$.133 & .665$\pm$.150 & .713$\pm$.174 & .719$\pm$.184 & .730$\pm$.201 \\
96	Vanilla & .410$\pm$.126 & .425$\pm$.143 & .432$\pm$.144 & .466$\pm$.144 & .466$\pm$.163 \\
97	\bottomrule
98	\end{tabular}
99	\end{table*}
100	
101	\section{OOD Perturbation Robustness}
102	\label{sec:ood_perturbation}
103	
104	\begin{table}[t]
105	\centering
106	\small
107	\caption{Perturbation robustness on OOD Deceptive Delight ($n$=118). $\Delta$: F1 change (pp) from clean to paraphrased. 3-seed mean$\pm$std where available.}
108	\label{tab:ood_perturbation}
109	\begin{tabular}{@{}lcccc@{}}
110	\toprule
111	\textbf{Variant} & Clean Full & Pert.\ Full & $\Delta$ Full & $\Delta$ $K$=1 \\
112	\midrule
113	9-class & .997$\pm$.005 & 1.000$\pm$.000 & +0.3 & +0.6 \\
114	Binary & .997$\pm$.005 & 1.000$\pm$.000 & +0.3 & +0.6 \\
115	Scrambled & .997$\pm$.005 & 1.000$\pm$.000 & +0.3 & $-$0.3 \\
116	\midrule
117	JB MLM & .914$\pm$.115 & .941 & +2.7 & 0.0 \\
118	Wiki MLM$^{*}$ & .904$\pm$.115 & .872 & $-$3.3 & $-$3.2 \\
119	Vanilla$^{\dagger}$ & .312$\pm$.026 & .339$\pm$.055 & +2.7 & $-$6.8$\pm$1.1 \\
120	\bottomrule
121	\end{tabular}
122	\vspace{-2pt}
123	{\footnotesize $^{*}$Wiki MLM degradation is seed-driven: seed 42 accounts for $-$9.8\,pp; other seeds show 0.0\,pp change.\\$^{\dagger}$Vanilla $\Delta$ Full = +2.7\,pp reflects floor-effect noise (baseline 0.312, std 0.055), not meaningful improvement.}
124	\end{table}
125	
126	\section{Reproducibility Details}
127	\label{sec:reproducibility}
128	
129	\paragraph{Stage-1 training.}
130	All variants use DeBERTa-v3-base (184M parameters) with learning rate $2 \times 10^{-5}$, AdamW optimizer ($\beta_1$=0.9, $\beta_2$=0.999, weight decay 0.01), linear warmup over the first 10\% of steps, batch size 16, and 4 epochs. MLM variants use 15\% random token masking. Training takes approximately 30 minutes per variant on a single NVIDIA A100 (40GB).
131	
132	\paragraph{Stage-2 training.}
133	The BiGRU has hidden dimension 128 (bidirectional, so output dimension 256). The MLP classifier has layers $256 \to 64 \to 2$ with ReLU activation and dropout 0.3. Training uses learning rate $1 \times 10^{-3}$, Adam optimizer, batch size 32, and 20 epochs with early stopping (patience 5) on validation F1. Stage-2 training completes in under 5 minutes per variant.
134	
135	\paragraph{Data generation.}
136	Jailbreak conversations are generated using Qwen3-8B with attack-specific prompt templates. Crescendo conversations follow a 5--8 turn gradual escalation structure. FITD conversations use a 2--3 turn commitment-consistency structure. Deceptive Delight conversations embed harmful content within emotionally engaging 3--5 turn sequences. Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general) with matched turn counts.
137	
138	\paragraph{Strategy annotation.}
139	Each user turn is annotated by Qwen3-8B using a structured prompt that provides definitions and two examples for each of the nine strategy categories. The prompt instructs the model to output a single category label. We plan to release all generation and annotation prompts, the full dataset, and training code upon acceptance.
140	
141	\paragraph{Adversarial paraphrasing.}
142	The paraphrased test set is generated by instructing Qwen3-8B to rephrase each user turn while preserving the communicative intent. The resulting paraphrases have mean BERTScore 0.92 and mean lexical overlap 0.20 with the originals. These metrics confirm substantial surface-level variation.
143	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ae6cbfa-3258-4018-8160-ee2ffd8afc67",
  "isSidechain": false,
  "promptId": "2cdd072d-21d6-4a8b-a6d1-c86993578b39",
  "type": "user",
  "uuid": "2c52d367-4a2e-4bac-9dd7-091dd8de0893",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
      "content": "% appendix.tex — Supplementary material\n\n\\appendix\n\n\\section{LLM-as-Judge Baseline}\n\\label{sec:llm_judge}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LLM-as-judge jailbreak detection. IID: binary F1 (Crescendo test set); OOD: macro F1 (DD = Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 values exclude unparseable responses and represent upper bounds.}\n\\label{tab:llm_judge}\n\\begin{tabular}{@{}lcccr@{}}\n\\toprule\n\\textbf{Method} & DD & AA & IID & Unparse. \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Zero-shot}} \\\\[2pt]\nGPT-5.5 & -- & -- & .383 & 30--47\\% \\\\\nQwen3-8B & .244 & .244 & .100 & 0\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{3-shot}} \\\\[2pt]\nQwen3-8B & .566 & .652 & -- & 0\\% \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Trained classifier}} \\\\[2pt]\n9-class (ours) & \\textbf{.997} & \\textbf{.972} & \\textbf{1.000} & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:llm_judge} reports LLM-as-judge performance on IID and OOD data.\nOn IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 = 0.383 on full conversations; 30--47\\% of responses are unparseable.\nQwen3-8B performs worse (IID F1 = 0.100).\nOn OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.\nEven with 3-shot prompting, Qwen3-8B reaches only 0.566 (DD) and 0.652 (AA), while DisPeD maintains macro F1 $\\geq$ 0.972.\nThe poor performance of content-level reasoning on unseen attack types underscores the necessity of trained classifiers with domain-adapted representations.\n\n\\section{Full Cross-Attack Results by Prefix}\n\\label{sec:full_prefix}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\\pm$std where available. ``--'' indicates insufficient conversation length for that prefix (FITD conversations contain 2--3 turns).}\n\\label{tab:full_prefix}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{IID (Crescendo)}} \\\\[2pt]\n9-class (ours) & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 & 1.000$\\pm$.000 \\\\\nMLM-only & .960 & .974 & .987 & 1.000 & 1.000 \\\\\nVanilla DeBERTa & .968$\\pm$.033 & .978$\\pm$.016 & .987$\\pm$.000 & .982$\\pm$.014 & 1.000$\\pm$.000 \\\\\nTF-IDF LR & 1.000 & 1.000 & 1.000 & 1.000 & 1.000 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{OOD (Deceptive Delight)}} \\\\[2pt]\n9-class (ours) & .990$\\pm$.013 & .981$\\pm$.013 & .972$\\pm$.026 & .997$\\pm$.005 & .997$\\pm$.005 \\\\\nBinary & .994$\\pm$.009 & .994$\\pm$.009 & .984$\\pm$.008 & 1.000$\\pm$.000 & .997$\\pm$.005 \\\\\nScrambled & .997$\\pm$.005 & .981$\\pm$.026 & .975$\\pm$.029 & .997$\\pm$.005 & .997$\\pm$.005 \\\\\nMLM-only & .973$\\pm$.019 & .993$\\pm$.009 & .997$\\pm$.005 & .997$\\pm$.005 & .914$\\pm$.115 \\\\\nVanilla DeBERTa & .628$\\pm$.038 & .479$\\pm$.038 & .389$\\pm$.027 & .351$\\pm$.030 & .312$\\pm$.026 \\\\\nTF-IDF LR & 1.000 & 1.000 & .994 & 1.000 & .961 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{OOD (FITD)}} \\\\[2pt]\n9-class (ours) & 1.000 & 1.000 & -- & -- & 1.000 \\\\\nVanilla DeBERTa & .990 & 1.000 & -- & -- & 1.000 \\\\\nTF-IDF LR & 1.000 & -- & -- & -- & 1.000 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{ActorAttack Full Results}\n\\label{sec:actorattack_full}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Full ActorAttack OOD results (F1) at all prefix lengths. 3-seed mean$\\pm$std (Binary per-$K$ reports $n$=2; Full is 3-seed).}\n\\label{tab:actorattack_full}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\n\\textbf{Method} & $K$=1 & $K$=2 & $K$=3 & $K$=5 & Full \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{DeBERTa-v3}} \\\\[2pt]\nBinary & .788$\\pm$.020 & \\textbf{.935$\\pm$.018} & \\textbf{.976$\\pm$.005} & \\textbf{.995$\\pm$.005} & \\textbf{.990$\\pm$.008} \\\\\n9-class & .773$\\pm$.041 & .855$\\pm$.048 & .921$\\pm$.046 & .966$\\pm$.028 & .972$\\pm$.026 \\\\\nScrambled & .652$\\pm$.034 & .804$\\pm$.053 & .854$\\pm$.046 & .910$\\pm$.052 & .951$\\pm$.043 \\\\\nMLM-only & .736$\\pm$.150 & .909$\\pm$.058 & .945$\\pm$.039 & .929$\\pm$.033 & .893$\\pm$.080 \\\\\nWiki MLM & .656$\\pm$.224 & .672$\\pm$.252 & .693$\\pm$.280 & .689$\\pm$.285 & .686$\\pm$.297 \\\\\nTopic & .513$\\pm$.077 & .580$\\pm$.109 & .565$\\pm$.100 & .615$\\pm$.111 & .625$\\pm$.141 \\\\\nVanilla & .337$\\pm$.049 & .306$\\pm$.026 & .284$\\pm$.011 & .262$\\pm$.006 & .258$\\pm$.000 \\\\\nTF-IDF LR & .633 & .730 & .571 & .242 & .261 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RoBERTa}} \\\\[2pt]\n9-class & \\textbf{.738$\\pm$.033} & .805$\\pm$.033 & .884$\\pm$.066 & .925$\\pm$.066 & .939$\\pm$.046 \\\\\nMLM & .633$\\pm$.133 & .665$\\pm$.150 & .713$\\pm$.174 & .719$\\pm$.184 & .730$\\pm$.201 \\\\\nVanilla & .410$\\pm$.126 & .425$\\pm$.143 & .432$\\pm$.144 & .466$\\pm$.144 & .466$\\pm$.163 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{OOD Perturbation Robustness}\n\\label{sec:ood_perturbation}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Perturbation robustness on OOD Deceptive Delight ($n$=118). $\\Delta$: F1 change (pp) from clean to paraphrased. 3-seed mean$\\pm$std where available.}\n\\label{tab:ood_perturbation}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\textbf{Variant} & Clean Full & Pert.\\ Full & $\\Delta$ Full & $\\Delta$ $K$=1 \\\\\n\\midrule\n9-class & .997$\\pm$.005 & 1.000$\\pm$.000 & +0.3 & +0.6 \\\\\nBinary & .997$\\pm$.005 & 1.000$\\pm$.000 & +0.3 & +0.6 \\\\\nScrambled & .997$\\pm$.005 & 1.000$\\pm$.000 & +0.3 & $-$0.3 \\\\\n\\midrule\nJB MLM & .914$\\pm$.115 & .941 & +2.7 & 0.0 \\\\\nWiki MLM$^{*}$ & .904$\\pm$.115 & .872 & $-$3.3 & $-$3.2 \\\\\nVanilla$^{\\dagger}$ & .312$\\pm$.026 & .339$\\pm$.055 & +2.7 & $-$6.8$\\pm$1.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{-2pt}\n{\\footnotesize $^{*}$Wiki MLM degradation is seed-driven: seed 42 accounts for $-$9.8\\,pp; other seeds show 0.0\\,pp change.\\\\$^{\\dagger}$Vanilla $\\Delta$ Full = +2.7\\,pp reflects floor-effect noise (baseline 0.312, std 0.055), not meaningful improvement.}\n\\end{table}\n\n\\section{Reproducibility Details}\n\\label{sec:reproducibility}\n\n\\paragraph{Stage-1 training.}\nAll variants use DeBERTa-v3-base (184M parameters) with learning rate $2 \\times 10^{-5}$, AdamW optimizer ($\\beta_1$=0.9, $\\beta_2$=0.999, weight decay 0.01), linear warmup over the first 10\\% of steps, batch size 16, and 4 epochs. MLM variants use 15\\% random token masking. Training takes approximately 30 minutes per variant on a single NVIDIA A100 (40GB).\n\n\\paragraph{Stage-2 training.}\nThe BiGRU has hidden dimension 128 (bidirectional, so output dimension 256). The MLP classifier has layers $256 \\to 64 \\to 2$ with ReLU activation and dropout 0.3. Training uses learning rate $1 \\times 10^{-3}$, Adam optimizer, batch size 32, and 20 epochs with early stopping (patience 5) on validation F1. Stage-2 training completes in under 5 minutes per variant.\n\n\\paragraph{Data generation.}\nJailbreak conversations are generated using Qwen3-8B with attack-specific prompt templates. Crescendo conversations follow a 5--8 turn gradual escalation structure. FITD conversations use a 2--3 turn commitment-consistency structure. Deceptive Delight conversations embed harmful content within emotionally engaging 3--5 turn sequences. Benign conversations are generated with topic-anchored prompts across five domains (technology, health, finance, education, general) with matched turn counts.\n\n\\paragraph{Strategy annotation.}\nEach user turn is annotated by Qwen3-8B using a structured prompt that provides definitions and two examples for each of the nine strategy categories. The prompt instructs the model to output a single category label. We plan to release all generation and annotation prompts, the full dataset, and training code upon acceptance.\n\n\\paragraph{Adversarial paraphrasing.}\nThe paraphrased test set is generated by instructing Qwen3-8B to rephrase each user turn while preserving the communicative intent. The resulting paraphrases have mean BERTScore 0.92 and mean lexical overlap 0.20 with the originals. These metrics confirm substantial surface-level variation.\n",
      "numLines": 143,
      "startLine": 1,
      "totalLines": 143
    }
  },
  "sourceToolAssistantUUID": "6ae6cbfa-3258-4018-8160-ee2ffd8afc67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore"
}
```

</details>

---


### Tool call

_source line 1360 · 2026-05-18T19:51:40.137Z_

<details open><summary>🔧 Tool call — Read · `toolu_015hik73ZMbwG9aG1QuYgKBt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c52d367-4a2e-4bac-9dd7-091dd8de0893",
  "isSidechain": false,
  "requestId": "req_011CbAcjdcBiLEC9GS9mnKwf",
  "type": "assistant",
  "uuid": "b9a34ca9-0a98-424c-8ea6-c75b4cd441e7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/.claude/sessions/paper_agent_6be59e15",
  "sessionId": "806ee39a-95a2-4db2-a3a1-7728b3dca63e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "distributed-cooking-shore",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SiiB9S6GNw3AqZkvcwuvHn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 535,
      "cache_read_input_tokens": 71347,
      "output_tokens": 498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 498,
          "cache_read_input_tokens": 71347,
          "cache_creation_input_tokens": 535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 535
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
