# Research conversation: [WORKER DONE] Worker worker_ssh_check-exp-014_20260517T125849 已完成（status=done）。用 `get_worker_status('worker_ssh_check-ex — Part 7 of 12

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

[← Part 6](part-006.md) · [Transcript overview](../research-conversation-worker-done-worker-worker-ssh-check-exp-014-20260517t125849-status-done-get-wo.md) · [Part 8 →](part-008.md) · [Structured JSON](../../../sessions/4d/4d55fe511db184af4c07.json)

## Round 141

### User

_source line 1776 · 2026-05-17T19:18:46.098Z_

[WORKER DONE] Worker worker_paper_writing_abstract_20260517T191146 已完成（status=done）。用 `get_worker_status('worker_paper_writing_abstract_20260517T191146')` 读取结果，然后处理。

- worker_id: worker_paper_writing_abstract_20260517T191146
- project: symb_invariant_consensus
- status: done

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1e3435f-6e05-4e03-af61-e90144f8a329",
  "isSidechain": false,
  "promptId": "5dfa7354-04dc-46bd-84c6-95f82a39d833",
  "type": "user",
  "uuid": "b22e4818-b2d2-4967-8753-67f0f4e2f023",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Runtime record

_source line 1777 · 2026-05-17T19:18:46.098Z_

```json
{
  "parentUuid": "b22e4818-b2d2-4967-8753-67f0f4e2f023",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c6231060-ef71-479d-890d-5a1a142152c9",
  "timestamp": "2026-05-17T19:18:46.098Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

---


### Tool call

_source line 1778 · 2026-05-17T19:18:49.141Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_01M7PwtwjiC2SYxdmNsUCbpG`</summary>

```json
{
  "worker_id": "worker_paper_writing_abstract_20260517T191146"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6231060-ef71-479d-890d-5a1a142152c9",
  "isSidechain": false,
  "requestId": "req_011Cb8gRknErGFBBzvFvdWh8",
  "type": "assistant",
  "uuid": "fbe0b3be-313d-492f-b8d7-0232db82608f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B969gQb6zR3YZoTDghEWvW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 227,
      "cache_read_input_tokens": 140553,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 227,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 80,
          "cache_read_input_tokens": 140553,
          "cache_creation_input_tokens": 227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 227
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

_source line 1779 · 2026-05-17T19:18:49.191Z_

<details><summary>↩ Tool result · `toolu_01M7PwtwjiC2SYxdmNsUCbpG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_abstract_20260517T191146\", \"status\": \"done\", \"task_type\": \"paper_writing:abstract\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:11:46.587214+00:00\", \"ended_at\": \"2026-05-17T19:13:54.705487+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"\\\"voting.\\\" is part of \\\"majority voting.\\\" which is a noun phrase (the object of the preposition), not a participial phrase ending. No issues.\\n\\nAbstract written (~216 words). Key design choices:\\n- Opens with the research question (can self-extraction work?) rather than leading with the negative result\\n- Oracle-positive framing: proves aggregation is sound, localizes failure to extraction quality\\n- Three key numbers only: +8.82pp, p<0.001, 11.5% discriminative rate\\n- All abbreviations defined inline (FOL, LLM, SICA, MAX-SAT, SC)\\n- No em-dashes, no -ing phrase endings, no blacklisted words\"}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbe0b3be-313d-492f-b8d7-0232db82608f",
  "isSidechain": false,
  "promptId": "5dfa7354-04dc-46bd-84c6-95f82a39d833",
  "type": "user",
  "uuid": "0cc79de1-148e-4026-a20b-23109b0fc064",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_paper_writing_abstract_20260517T191146\\\", \\\"status\\\": \\\"done\\\", \\\"task_type\\\": \\\"paper_writing:abstract\\\", \\\"project\\\": \\\"symb_invariant_consensus\\\", \\\"started_at\\\": \\\"2026-05-17T19:11:46.587214+00:00\\\", \\\"ended_at\\\": \\\"2026-05-17T19:13:54.705487+00:00\\\", \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}, \\\"result\\\": {\\\"raw\\\": \\\"\\\\\\\"voting.\\\\\\\" is part of \\\\\\\"majority voting.\\\\\\\" which is a noun phrase (the object of the preposition), not a participial phrase ending. No issues.\\\\n\\\\nAbstract written (~216 words). Key design choices:\\\\n- Opens with the research question (can self-extraction work?) rather than leading with the negative result\\\\n- Oracle-positive framing: proves aggregation is sound, localizes failure to extraction quality\\\\n- Three key numbers only: +8.82pp, p<0.001, 11.5% discriminative rate\\\\n- All abbreviations defined inline (FOL, LLM, SICA, MAX-SAT, SC)\\\\n- No em-dashes, no -ing phrase endings, no blacklisted words\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_writing_abstract_20260517T191146\", \"status\": \"done\", \"task_type\": \"paper_writing:abstract\", \"project\": \"symb_invariant_consensus\", \"started_at\": \"2026-05-17T19:11:46.587214+00:00\", \"ended_at\": \"2026-05-17T19:13:54.705487+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"\\\"voting.\\\" is part of \\\"majority voting.\\\" which is a noun phrase (the object of the preposition), not a participial phrase ending. No issues.\\n\\nAbstract written (~216 words). Key design choices:\\n- Opens with the research question (can self-extraction work?) rather than leading with the negative result\\n- Oracle-positive framing: proves aggregation is sound, localizes failure to extraction quality\\n- Three key numbers only: +8.82pp, p<0.001, 11.5% discriminative rate\\n- All abbreviations defined inline (FOL, LLM, SICA, MAX-SAT, SC)\\n- No em-dashes, no -ing phrase endings, no blacklisted words\"}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "fbe0b3be-313d-492f-b8d7-0232db82608f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Assistant

_source line 1780 · 2026-05-17T19:18:52.553Z_

<details><summary>Logged reasoning block</summary>

```text
This worker rewrote the abstract. Let me check if it changed the abstract.tex file and if the content is consistent with the rest of the paper. Let me read the current abstract.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cc79de1-148e-4026-a20b-23109b0fc064",
  "isSidechain": false,
  "requestId": "req_011Cb8gRyzjAvHpc5LBWNGby",
  "type": "assistant",
  "uuid": "5b5b03c6-9eac-4446-9e6b-a07f5180981e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YeJfcYezvHmC8sGRZoR1e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 444,
      "cache_read_input_tokens": 140780,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 444,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 140780,
          "cache_creation_input_tokens": 444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 444
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

_source line 1781 · 2026-05-17T19:18:52.555Z_

Worker 重写了 abstract。检查当前状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b5b03c6-9eac-4446-9e6b-a07f5180981e",
  "isSidechain": false,
  "requestId": "req_011Cb8gRyzjAvHpc5LBWNGby",
  "type": "assistant",
  "uuid": "649abfbe-a393-42f0-878e-7b99da86458e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YeJfcYezvHmC8sGRZoR1e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 444,
      "cache_read_input_tokens": 140780,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 444,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 140780,
          "cache_creation_input_tokens": 444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 444
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

_source line 1782 · 2026-05-17T19:18:53.153Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GSKz2hHRDYErGXoxgZ4gZQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "649abfbe-a393-42f0-878e-7b99da86458e",
  "isSidechain": false,
  "requestId": "req_011Cb8gRyzjAvHpc5LBWNGby",
  "type": "assistant",
  "uuid": "6225c9fd-c657-4313-a2f9-1ea4bf7ef1e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018YeJfcYezvHmC8sGRZoR1e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 444,
      "cache_read_input_tokens": 140780,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 444,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 161,
          "cache_read_input_tokens": 140780,
          "cache_creation_input_tokens": 444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 444
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

_source line 1783 · 2026-05-17T19:18:53.161Z_

<details><summary>↩ Tool result · `toolu_01GSKz2hHRDYErGXoxgZ4gZQ`</summary>

```text
1	\begin{abstract}
2	Neuro-symbolic methods propose extracting first-order logic (FOL) constraints from Large Language Model (LLM) reasoning traces to improve answer aggregation beyond majority voting. Whether the reasoning model itself can produce useful constraints through self-extraction has not been systematically evaluated. If self-extraction works, it eliminates the need for trained verifiers, external provers, or domain-specific infrastructure. We evaluate Symbolic Invariant Consensus Aggregation (SICA), which formulates a weighted partial Maximum Satisfiability (MAX-SAT) problem over self-extracted FOL constraints, across five model families (7B to 32B parameters) and three reasoning domains with more than 1,300 total instances. We include an oracle control that replaces self-extraction with gold FOL annotations verified by Z3 to isolate extraction quality from aggregation effectiveness. Self-extracted SICA provides no statistically significant improvement over Self-Consistency (SC) in any tested condition. The oracle variant achieves $+8.82$ percentage points over SC ($p < 0.001$), which proves the aggregation mechanism is sound when supplied with high-quality constraints. We identify this failure as a \emph{capability trap}: because the same model that produced potentially flawed reasoning also extracts the constraints, those constraints are semantically coupled to their source answers and carry no independent discriminative signal. Only 11.5\% of self-extracted constraints evaluate differently across candidate answers. This result establishes that same-model constraint extraction cannot improve LLM answer aggregation without independent sources of formal knowledge.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6225c9fd-c657-4313-a2f9-1ea4bf7ef1e0",
  "isSidechain": false,
  "promptId": "5dfa7354-04dc-46bd-84c6-95f82a39d833",
  "type": "user",
  "uuid": "723d6c7e-b651-4213-a46f-75e7a8ad20c2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nNeuro-symbolic methods propose extracting first-order logic (FOL) constraints from Large Language Model (LLM) reasoning traces to improve answer aggregation beyond majority voting. Whether the reasoning model itself can produce useful constraints through self-extraction has not been systematically evaluated. If self-extraction works, it eliminates the need for trained verifiers, external provers, or domain-specific infrastructure. We evaluate Symbolic Invariant Consensus Aggregation (SICA), which formulates a weighted partial Maximum Satisfiability (MAX-SAT) problem over self-extracted FOL constraints, across five model families (7B to 32B parameters) and three reasoning domains with more than 1,300 total instances. We include an oracle control that replaces self-extraction with gold FOL annotations verified by Z3 to isolate extraction quality from aggregation effectiveness. Self-extracted SICA provides no statistically significant improvement over Self-Consistency (SC) in any tested condition. The oracle variant achieves $+8.82$ percentage points over SC ($p < 0.001$), which proves the aggregation mechanism is sound when supplied with high-quality constraints. We identify this failure as a \\emph{capability trap}: because the same model that produced potentially flawed reasoning also extracts the constraints, those constraints are semantically coupled to their source answers and carry no independent discriminative signal. Only 11.5\\% of self-extracted constraints evaluate differently across candidate answers. This result establishes that same-model constraint extraction cannot improve LLM answer aggregation without independent sources of formal knowledge.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  },
  "sourceToolAssistantUUID": "6225c9fd-c657-4313-a2f9-1ea4bf7ef1e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Runtime record

_source line 1784_

```json
{
  "type": "ai-title",
  "aiTitle": "Retrieve and process SSH check worker results",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746"
}
```

---


### Runtime record

_source line 1785 · 2026-05-17T19:19:05.070Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T19:19:05.070Z",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "content": "[Director 指令] 8pp 达标，但两个章节过薄需要回填（利用 200-300 word buffer）：\n\n**1. Introduction 645 → ~800 words (+155)**\n645 对 EMNLP Intro 太短。把砍掉的核心内容加回来：\n- 确保贡献列表完整（4 条 contributions）\n- 确保 oracle 结果在 Intro 中被提及（+8.82pp）\n- 不要加回冗余背景\n\n**2. Discussion 273 → ~400 words (+130)**\n273 太薄，审稿人会觉得分析不够。加回：\n- Constructive outlook（trained extractors / external provers 可解锁 +8.82pp gap）\n- C0 作为 practitioners 的 zero-cost diagnostic\n- 不要重复 Experiments 数字\n\n总计回填 ~285 words，仍在 8 页内。改完重新编译确认仍 ≤8 页。\n\n同时处理队列中的修复清单（Table 3 确认、LLaMA Δ、11.5%、overhead 措辞、T=0.7 数据）。"
}
```

---


### Runtime record

_source line 1786 · 2026-05-17T19:19:05.071Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T19:19:05.071Z",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746"
}
```

---


## Round 142

## Round 142

2 recorded events


### User

_source line 1787 · 2026-05-17T19:19:05.056Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "723d6c7e-b651-4213-a46f-75e7a8ad20c2",
  "isSidechain": false,
  "promptId": "0fe74f2a-7c66-4010-b7d3-d39840f075b8",
  "type": "user",
  "isMeta": true,
  "uuid": "c4a65939-3775-4ff0-af6e-b62828d37e36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Assistant

_source line 1788 · 2026-05-17T19:19:05.057Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4a65939-3775-4ff0-af6e-b62828d37e36",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "d0597c3c-369b-45bf-b6bd-964fe8a751a6",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "id": "129dfa1e-4677-45d4-b513-0d57c553d9e0",
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


## Round 143

## Round 143

39 recorded events


### User

_source line 1789 · 2026-05-17T19:19:05.207Z_

[Director 指令] 8pp 达标，但两个章节过薄需要回填（利用 200-300 word buffer）：

**1. Introduction 645 → ~800 words (+155)**
645 对 EMNLP Intro 太短。把砍掉的核心内容加回来：
- 确保贡献列表完整（4 条 contributions）
- 确保 oracle 结果在 Intro 中被提及（+8.82pp）
- 不要加回冗余背景

**2. Discussion 273 → ~400 words (+130)**
273 太薄，审稿人会觉得分析不够。加回：
- Constructive outlook（trained extractors / external provers 可解锁 +8.82pp gap）
- C0 作为 practitioners 的 zero-cost diagnostic
- 不要重复 Experiments 数字

总计回填 ~285 words，仍在 8 页内。改完重新编译确认仍 ≤8 页。

同时处理队列中的修复清单（Table 3 确认、LLaMA Δ、11.5%、overhead 措辞、T=0.7 数据）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0597c3c-369b-45bf-b6bd-964fe8a751a6",
  "isSidechain": false,
  "promptId": "0fe74f2a-7c66-4010-b7d3-d39840f075b8",
  "type": "user",
  "uuid": "7629ed95-4219-4d1d-8922-6693366cf3f3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Assistant

_source line 1790 · 2026-05-17T19:19:09.118Z_

<details><summary>Logged reasoning block</summary>

```text
The Director wants me to:
1. Expand Introduction from 645 to ~800 words (+155)
2. Expand Discussion from 273 to ~400 words (+130)

The repair items (Table 3, LLaMA Δ, 11.5%, overhead, T=0.7) were already completed in previous turns. Let me just do the two expansions.

Let me read both files and make the edits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7629ed95-4219-4d1d-8922-6693366cf3f3",
  "isSidechain": false,
  "requestId": "req_011Cb8gTAVnf2UVQdPWgCYDV",
  "type": "assistant",
  "uuid": "aec831cc-b630-45b4-9551-b7d5d8179d5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dCcV8ViXfSpAuqj3UGECg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 141759,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 343,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 327,
          "cache_read_input_tokens": 141759,
          "cache_creation_input_tokens": 343,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 343
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

_source line 1791 · 2026-05-17T19:19:10.069Z_

修复清单（Table 3、LLaMA Δ、11.5%、overhead、T=0.7）已在前几轮全部完成。现在做两个回填。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aec831cc-b630-45b4-9551-b7d5d8179d5c",
  "isSidechain": false,
  "requestId": "req_011Cb8gTAVnf2UVQdPWgCYDV",
  "type": "assistant",
  "uuid": "6bc68109-8bf8-4680-8630-d6e5d4c50f6f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dCcV8ViXfSpAuqj3UGECg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 141759,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 343,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 327,
          "cache_read_input_tokens": 141759,
          "cache_creation_input_tokens": 343,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 343
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

_source line 1792 · 2026-05-17T19:19:10.618Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QSxHzDaQ5wSpGbeaM81U6o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bc68109-8bf8-4680-8630-d6e5d4c50f6f",
  "isSidechain": false,
  "requestId": "req_011Cb8gTAVnf2UVQdPWgCYDV",
  "type": "assistant",
  "uuid": "79db5a09-9aa2-4c79-acd1-48b8031ce3af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dCcV8ViXfSpAuqj3UGECg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 141759,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 343,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 327,
          "cache_read_input_tokens": 141759,
          "cache_creation_input_tokens": 343,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 343
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

_source line 1793 · 2026-05-17T19:19:11.003Z_

<details><summary>↩ Tool result · `toolu_01Ue3er5KzqDcEALHZZa4ddn`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	The oracle experiment (Table~\ref{tab:main_results}, bottom) constitutes a causal intervention that isolates the source of failure. By replacing only the constraint source while holding all other pipeline components fixed, we establish that aggregation is not the bottleneck: the $+8.82$\,pp improvement ($p < 0.001$) pinpoints same-model self-extraction as the single point of failure. This oracle design follows established methodology where component-level interventions isolate error sources \citep{press2023compositionality, trivedi2023ircot, saparov2023greedy}.
5	
6	Manual analysis of constraint quality explains the mechanism. Across 43 pilot problems (23 with multiple candidates), only 11.5\% of unique constraints evaluated differently across candidates. The remainder encoded shared domain facts (predicate definitions, background implications, intermediate steps) satisfied equally by every candidate. In only 4 of 23 multi-answer problems (17.4\%) did discriminative constraints favor a non-majority answer, accounting for the 803/804 agreement between MAX-SAT and count-only (Table~\ref{tab:ablation}).
7	
8	The computational cost is substantial: constraint extraction accounts for 48.7\% of total SICA pipeline time, roughly doubling wall-clock cost compared to SC alone. Among 31 disagreements with SC, wins and losses approximately cancel (16 vs.\ 14), yielding zero net accuracy gain.
9	
10	The $+8.82$\,pp oracle ceiling quantifies the potential locked behind the capability trap. Three paths can unlock it: trained FOL extractors supervised on gold annotations, external provers that verify constraints independently of the reasoning model, and cross-model extraction that breaks the self-reference loop. Each targets the extraction bottleneck; improving the aggregation mechanism offers no path forward. For practitioners, $C_0$ provides a zero-cost screening criterion: when $C_0 < 5\%$, SICA degenerates to SC by construction. High $C_0$ is necessary but not sufficient, as the capability trap renders constraints non-discriminative even when disagreement is abundant ($C_0 = 61.8\%$, $\Delta = -2.45$~pp, n.s., for LLaMA-3.1-8B on FOLIO).
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdee3443-d5a6-4d6d-9b92-f1e72cd7bb36",
  "isSidechain": false,
  "promptId": "0fe74f2a-7c66-4010-b7d3-d39840f075b8",
  "type": "user",
  "uuid": "14209e81-b2d1-460e-8894-85715b0ba7cf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\nThe oracle experiment (Table~\\ref{tab:main_results}, bottom) constitutes a causal intervention that isolates the source of failure. By replacing only the constraint source while holding all other pipeline components fixed, we establish that aggregation is not the bottleneck: the $+8.82$\\,pp improvement ($p < 0.001$) pinpoints same-model self-extraction as the single point of failure. This oracle design follows established methodology where component-level interventions isolate error sources \\citep{press2023compositionality, trivedi2023ircot, saparov2023greedy}.\n\nManual analysis of constraint quality explains the mechanism. Across 43 pilot problems (23 with multiple candidates), only 11.5\\% of unique constraints evaluated differently across candidates. The remainder encoded shared domain facts (predicate definitions, background implications, intermediate steps) satisfied equally by every candidate. In only 4 of 23 multi-answer problems (17.4\\%) did discriminative constraints favor a non-majority answer, accounting for the 803/804 agreement between MAX-SAT and count-only (Table~\\ref{tab:ablation}).\n\nThe computational cost is substantial: constraint extraction accounts for 48.7\\% of total SICA pipeline time, roughly doubling wall-clock cost compared to SC alone. Among 31 disagreements with SC, wins and losses approximately cancel (16 vs.\\ 14), yielding zero net accuracy gain.\n\nThe $+8.82$\\,pp oracle ceiling quantifies the potential locked behind the capability trap. Three paths can unlock it: trained FOL extractors supervised on gold annotations, external provers that verify constraints independently of the reasoning model, and cross-model extraction that breaks the self-reference loop. Each targets the extraction bottleneck; improving the aggregation mechanism offers no path forward. For practitioners, $C_0$ provides a zero-cost screening criterion: when $C_0 < 5\\%$, SICA degenerates to SC by construction. High $C_0$ is necessary but not sufficient, as the capability trap renders constraints non-discriminative even when disagreement is abundant ($C_0 = 61.8\\%$, $\\Delta = -2.45$~pp, n.s., for LLaMA-3.1-8B on FOLIO).\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  },
  "sourceToolAssistantUUID": "bdee3443-d5a6-4d6d-9b92-f1e72cd7bb36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Tool result

_source line 1794 · 2026-05-17T19:19:10.645Z_

<details><summary>↩ Tool result · `toolu_01QSxHzDaQ5wSpGbeaM81U6o`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Neuro-symbolic methods that augment large language model (LLM) reasoning with formal solvers have demonstrated gains on logical reasoning benchmarks. Logic-LM \citep{pan2023logiclm} and LINC \citep{olausson2023linc} delegate formalization to external provers. More recent systems route problems to specialized solver paradigms \citep{xu2026dylos}, apply logic-complete decomposition \citep{li2025aristotle}, train dedicated first-order logic (FOL) verifiers on supervised data \citep{wang2025fover}, or employ multi-perspective grounding \citep{luo2025logicagent}. These systems report positive results on formal reasoning benchmarks, but a critical commonality unites them: each introduces capabilities beyond the reasoning model itself, whether trained verifiers, multi-paradigm solver selection, or external knowledge bases. The external machinery is effective but imposes practical costs in training data, integration complexity, and domain-specific engineering that limits portability.
4	
5	These results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability solver. Yet no prior work has systematically evaluated whether self-extraction produces constraints useful for answer aggregation, or characterized the conditions under which it succeeds or fails. This gap is consequential: the practical promise of neuro-symbolic reasoning hinges on whether the reasoning model alone can supply formal structure of sufficient quality, or whether external grounding is fundamentally required.
6	
7	Self-Consistency (SC) selects the most frequent answer across multiple chain-of-thought samples \citep{wang2023sc} and remains competitive across mathematical, logical, and commonsense reasoning \citep{chen2024usc, taubenfeld2025cisc}. SC treats traces as black boxes, discarding all intermediate reasoning. Each trace, however, contains logical dependencies and structural relationships that could ground aggregation in formal logic, adding discriminative power beyond vote counting. This would also address SC's known scaling plateau, where additional traces yield diminishing returns \citep{loo2025reevaluating}.
8	
9	We evaluate this possibility through Symbolic Invariant Consensus Aggregation (SICA), a pipeline that extracts FOL constraints from $K$ reasoning traces produced by a single LLM, deduplicates by syntactic equivalence, and solves a weighted partial MAX-SAT problem via Z3 \citep{demoura2008z3}. The answer best supported by the largest satisfiable constraint subset is selected (Figure~\ref{fig:pipeline}). We test five model families spanning 7B to 32B parameters (Qwen2.5-14B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B, QwQ-32B) across three reasoning domains: formal logic (FOLIO \citep{han2022folio}, ProofWriter \citep{tafjord2021proofwriter}), commonsense (StrategyQA \citep{geva2021strategyqa}), and science (ARC-Challenge \citep{clark2018arc}), with supplementary probes on GSM8K \citep{cobbe2021gsm8k} and AIME 2024, totaling more than 1,300 instances. An oracle control on FOLIO ($n=204$) replaces self-extracted constraints with gold FOL annotations verified by Z3, isolating extraction quality from aggregation effectiveness following established methodology \citep{press2023compositionality}.
10	
11	Across all conditions, SICA provides no statistically significant improvement over SC, with accuracy gaps between $-3.3$ and $+3.3$\,pp. The oracle experiment yields a fundamentally different result: $+8.82$\,pp over SC (McNemar $p = 6.15 \times 10^{-5}$), confirming that the MAX-SAT mechanism is sound when given discriminative constraints. The bottleneck is extraction quality. Because the same model generates both answers and constraints, the extracted constraints are semantically coupled to their source answers and carry no independent signal. We term this the \emph{capability trap}: the model cannot formalize corrections to its own reasoning errors because extraction inherits the same biases that produced those errors. A constraint ablation confirms the diagnosis: MAX-SAT and count-only aggregation agree on 803 of 804 predictions (\S\ref{sec:ablation}). Manual analysis shows only 11.5\% of unique constraints evaluate differently across candidates; the remainder encode shared domain facts that contribute identical scores to every answer. Constraint extraction accounts for 48.7\% of total SICA pipeline time, roughly doubling wall-clock cost for zero expected accuracy gain.
12	
13	Our contributions are:
14	\begin{itemize}
15	\item We evaluate SICA across five model families and three reasoning domains ($N > 1{,}300$), finding no improvement over majority voting in any condition.
16	\item We design an oracle control achieving $+8.82$\,pp over SC ($p < 0.001$), causally localizing the failure to extraction quality rather than the aggregation mechanism.
17	\item We identify the multi-candidate rate $C_0$ as a zero-cost diagnostic: low $C_0$ rules out any possible SICA gain before constraint extraction begins.
18	\end{itemize}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79db5a09-9aa2-4c79-acd1-48b8031ce3af",
  "isSidechain": false,
  "promptId": "0fe74f2a-7c66-4010-b7d3-d39840f075b8",
  "type": "user",
  "uuid": "4f590baf-7842-4026-9002-c6967be9ff40",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nNeuro-symbolic methods that augment large language model (LLM) reasoning with formal solvers have demonstrated gains on logical reasoning benchmarks. Logic-LM \\citep{pan2023logiclm} and LINC \\citep{olausson2023linc} delegate formalization to external provers. More recent systems route problems to specialized solver paradigms \\citep{xu2026dylos}, apply logic-complete decomposition \\citep{li2025aristotle}, train dedicated first-order logic (FOL) verifiers on supervised data \\citep{wang2025fover}, or employ multi-perspective grounding \\citep{luo2025logicagent}. These systems report positive results on formal reasoning benchmarks, but a critical commonality unites them: each introduces capabilities beyond the reasoning model itself, whether trained verifiers, multi-paradigm solver selection, or external knowledge bases. The external machinery is effective but imposes practical costs in training data, integration complexity, and domain-specific engineering that limits portability.\n\nThese results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability solver. Yet no prior work has systematically evaluated whether self-extraction produces constraints useful for answer aggregation, or characterized the conditions under which it succeeds or fails. This gap is consequential: the practical promise of neuro-symbolic reasoning hinges on whether the reasoning model alone can supply formal structure of sufficient quality, or whether external grounding is fundamentally required.\n\nSelf-Consistency (SC) selects the most frequent answer across multiple chain-of-thought samples \\citep{wang2023sc} and remains competitive across mathematical, logical, and commonsense reasoning \\citep{chen2024usc, taubenfeld2025cisc}. SC treats traces as black boxes, discarding all intermediate reasoning. Each trace, however, contains logical dependencies and structural relationships that could ground aggregation in formal logic, adding discriminative power beyond vote counting. This would also address SC's known scaling plateau, where additional traces yield diminishing returns \\citep{loo2025reevaluating}.\n\nWe evaluate this possibility through Symbolic Invariant Consensus Aggregation (SICA), a pipeline that extracts FOL constraints from $K$ reasoning traces produced by a single LLM, deduplicates by syntactic equivalence, and solves a weighted partial MAX-SAT problem via Z3 \\citep{demoura2008z3}. The answer best supported by the largest satisfiable constraint subset is selected (Figure~\\ref{fig:pipeline}). We test five model families spanning 7B to 32B parameters (Qwen2.5-14B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B, QwQ-32B) across three reasoning domains: formal logic (FOLIO \\citep{han2022folio}, ProofWriter \\citep{tafjord2021proofwriter}), commonsense (StrategyQA \\citep{geva2021strategyqa}), and science (ARC-Challenge \\citep{clark2018arc}), with supplementary probes on GSM8K \\citep{cobbe2021gsm8k} and AIME 2024, totaling more than 1,300 instances. An oracle control on FOLIO ($n=204$) replaces self-extracted constraints with gold FOL annotations verified by Z3, isolating extraction quality from aggregation effectiveness following established methodology \\citep{press2023compositionality}.\n\nAcross all conditions, SICA provides no statistically significant improvement over SC, with accuracy gaps between $-3.3$ and $+3.3$\\,pp. The oracle experiment yields a fundamentally different result: $+8.82$\\,pp over SC (McNemar $p = 6.15 \\times 10^{-5}$), confirming that the MAX-SAT mechanism is sound when given discriminative constraints. The bottleneck is extraction quality. Because the same model generates both answers and constraints, the extracted constraints are semantically coupled to their source answers and carry no independent signal. We term this the \\emph{capability trap}: the model cannot formalize corrections to its own reasoning errors because extraction inherits the same biases that produced those errors. A constraint ablation confirms the diagnosis: MAX-SAT and count-only aggregation agree on 803 of 804 predictions (\\S\\ref{sec:ablation}). Manual analysis shows only 11.5\\% of unique constraints evaluate differently across candidates; the remainder encode shared domain facts that contribute identical scores to every answer. Constraint extraction accounts for 48.7\\% of total SICA pipeline time, roughly doubling wall-clock cost for zero expected accuracy gain.\n\nOur contributions are:\n\\begin{itemize}\n\\item We evaluate SICA across five model families and three reasoning domains ($N > 1{,}300$), finding no improvement over majority voting in any condition.\n\\item We design an oracle control achieving $+8.82$\\,pp over SC ($p < 0.001$), causally localizing the failure to extraction quality rather than the aggregation mechanism.\n\\item We identify the multi-candidate rate $C_0$ as a zero-cost diagnostic: low $C_0$ rules out any possible SICA gain before constraint extraction begins.\n\\end{itemize}\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  },
  "sourceToolAssistantUUID": "79db5a09-9aa2-4c79-acd1-48b8031ce3af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Tool call

_source line 1795 · 2026-05-17T19:19:10.996Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ue3er5KzqDcEALHZZa4ddn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f590baf-7842-4026-9002-c6967be9ff40",
  "isSidechain": false,
  "requestId": "req_011Cb8gTAVnf2UVQdPWgCYDV",
  "type": "assistant",
  "uuid": "bdee3443-d5a6-4d6d-9b92-f1e72cd7bb36",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018dCcV8ViXfSpAuqj3UGECg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 141759,
      "output_tokens": 327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 343,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 327,
          "cache_read_input_tokens": 141759,
          "cache_creation_input_tokens": 343,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 343
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

_source line 1796 · 2026-05-17T19:19:20.338Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to:

1. Introduction 645→~800 words (+155):
   - Add 4th contribution (constraint ablation)
   - Flesh out the experimental setup paragraph slightly
   - Add a sentence about model selection rationale

2. Discussion 273→~400 words (+130):
   - Expand constructive outlook paragraph
   - Expand C0 practical guidance

Let me make the edits.

For Introduction, the current contributions are 3 items. I need to add back the 4th one (constraint ablation). Also, I can flesh out a few areas:


- Para 2: add one more sentence about the appeal of self-extraction
- Para 4: add brief model selection rationale  
- Para 5: maybe expand slightly
- Add 4th contribution item

For Discussion:
- Expand the constructive outlook (para 4) with more detail about each path
- Expand C0 guidance with practical recommendation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14209e81-b2d1-460e-8894-85715b0ba7cf",
  "isSidechain": false,
  "requestId": "req_011Cb8gTbVSogESi1vXNYzea",
  "type": "assistant",
  "uuid": "fdf4b730-af62-4d32-b4e6-da039085d956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BE2235SiyKVdR84M17gcTR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2287,
      "cache_read_input_tokens": 142102,
      "output_tokens": 700,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 700,
          "cache_read_input_tokens": 142102,
          "cache_creation_input_tokens": 2287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2287
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

_source line 1797 · 2026-05-17T19:19:20.420Z_

**Introduction**: adding 4th contribution and fleshing out key paragraphs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdf4b730-af62-4d32-b4e6-da039085d956",
  "isSidechain": false,
  "requestId": "req_011Cb8gTbVSogESi1vXNYzea",
  "type": "assistant",
  "uuid": "8ac7c42a-38eb-46e4-800c-de5834984c90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BE2235SiyKVdR84M17gcTR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2287,
      "cache_read_input_tokens": 142102,
      "output_tokens": 700,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 700,
          "cache_read_input_tokens": 142102,
          "cache_creation_input_tokens": 2287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2287
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

_source line 1798 · 2026-05-17T19:19:23.724Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01CgYJrtDDw8YDz1V5ZDRohh`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
  "old_string": "These results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability solver. Yet no prior work has systematically evaluated whether self-extraction produces constraints useful for answer aggregation, or characterized the conditions under which it succeeds or fails. This gap is consequential: the practical promise of neuro-symbolic reasoning hinges on whether the reasoning model alone can supply formal structure of sufficient quality, or whether external grounding is fundamentally required.",
  "new_string": "These results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability solver, with no domain-specific infrastructure. If successful, this approach would provide a lightweight, portable alternative to the external machinery that current systems require. Yet no prior work has systematically evaluated whether self-extraction produces constraints useful for answer aggregation, or characterized the conditions under which it succeeds or fails. This gap is consequential: the practical promise of neuro-symbolic reasoning hinges on whether the reasoning model alone can supply formal structure of sufficient quality, or whether external grounding is fundamentally required."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ac7c42a-38eb-46e4-800c-de5834984c90",
  "isSidechain": false,
  "requestId": "req_011Cb8gTbVSogESi1vXNYzea",
  "type": "assistant",
  "uuid": "f85b912d-a174-42ac-9cd8-f817fe8b0db7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BE2235SiyKVdR84M17gcTR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2287,
      "cache_read_input_tokens": 142102,
      "output_tokens": 700,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 700,
          "cache_read_input_tokens": 142102,
          "cache_creation_input_tokens": 2287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2287
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

_source line 1799 · 2026-05-17T19:19:23.749Z_

<details><summary>↩ Tool result · `toolu_01CgYJrtDDw8YDz1V5ZDRohh`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f85b912d-a174-42ac-9cd8-f817fe8b0db7",
  "isSidechain": false,
  "promptId": "0fe74f2a-7c66-4010-b7d3-d39840f075b8",
  "type": "user",
  "uuid": "4246ee1b-87b4-4035-9af1-1bb281e891fb",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
    "oldString": "These results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability solver. Yet no prior work has systematically evaluated whether self-extraction produces constraints useful for answer aggregation, or characterized the conditions under which it succeeds or fails. This gap is consequential: the practical promise of neuro-symbolic reasoning hinges on whether the reasoning model alone can supply formal structure of sufficient quality, or whether external grounding is fundamentally required.",
    "newString": "These results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability solver, with no domain-specific infrastructure. If successful, this approach would provide a lightweight, portable alternative to the external machinery that current systems require. Yet no prior work has systematically evaluated whether self-extraction produces constraints useful for answer aggregation, or characterized the conditions under which it succeeds or fails. This gap is consequential: the practical promise of neuro-symbolic reasoning hinges on whether the reasoning model alone can supply formal structure of sufficient quality, or whether external grounding is fundamentally required.",
    "originalFile": "\\section{Introduction}\\label{sec:introduction}\n\nNeuro-symbolic methods that augment large language model (LLM) reasoning with formal solvers have demonstrated gains on logical reasoning benchmarks. Logic-LM \\citep{pan2023logiclm} and LINC \\citep{olausson2023linc} delegate formalization to external provers. More recent systems route problems to specialized solver paradigms \\citep{xu2026dylos}, apply logic-complete decomposition \\citep{li2025aristotle}, train dedicated first-order logic (FOL) verifiers on supervised data \\citep{wang2025fover}, or employ multi-perspective grounding \\citep{luo2025logicagent}. These systems report positive results on formal reasoning benchmarks, but a critical commonality unites them: each introduces capabilities beyond the reasoning model itself, whether trained verifiers, multi-paradigm solver selection, or external knowledge bases. The external machinery is effective but imposes practical costs in training data, integration complexity, and domain-specific engineering that limits portability.\n\nThese results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability solver. Yet no prior work has systematically evaluated whether self-extraction produces constraints useful for answer aggregation, or characterized the conditions under which it succeeds or fails. This gap is consequential: the practical promise of neuro-symbolic reasoning hinges on whether the reasoning model alone can supply formal structure of sufficient quality, or whether external grounding is fundamentally required.\n\nSelf-Consistency (SC) selects the most frequent answer across multiple chain-of-thought samples \\citep{wang2023sc} and remains competitive across mathematical, logical, and commonsense reasoning \\citep{chen2024usc, taubenfeld2025cisc}. SC treats traces as black boxes, discarding all intermediate reasoning. Each trace, however, contains logical dependencies and structural relationships that could ground aggregation in formal logic, adding discriminative power beyond vote counting. This would also address SC's known scaling plateau, where additional traces yield diminishing returns \\citep{loo2025reevaluating}.\n\nWe evaluate this possibility through Symbolic Invariant Consensus Aggregation (SICA), a pipeline that extracts FOL constraints from $K$ reasoning traces produced by a single LLM, deduplicates by syntactic equivalence, and solves a weighted partial MAX-SAT problem via Z3 \\citep{demoura2008z3}. The answer best supported by the largest satisfiable constraint subset is selected (Figure~\\ref{fig:pipeline}). We test five model families spanning 7B to 32B parameters (Qwen2.5-14B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B, QwQ-32B) across three reasoning domains: formal logic (FOLIO \\citep{han2022folio}, ProofWriter \\citep{tafjord2021proofwriter}), commonsense (StrategyQA \\citep{geva2021strategyqa}), and science (ARC-Challenge \\citep{clark2018arc}), with supplementary probes on GSM8K \\citep{cobbe2021gsm8k} and AIME 2024, totaling more than 1,300 instances. An oracle control on FOLIO ($n=204$) replaces self-extracted constraints with gold FOL annotations verified by Z3, isolating extraction quality from aggregation effectiveness following established methodology \\citep{press2023compositionality}.\n\nAcross all conditions, SICA provides no statistically significant improvement over SC, with accuracy gaps between $-3.3$ and $+3.3$\\,pp. The oracle experiment yields a fundamentally different result: $+8.82$\\,pp over SC (McNemar $p = 6.15 \\times 10^{-5}$), confirming that the MAX-SAT mechanism is sound when given discriminative constraints. The bottleneck is extraction quality. Because the same model generates both answers and constraints, the extracted constraints are semantically coupled to their source answers and carry no independent signal. We term this the \\emph{capability trap}: the model cannot formalize corrections to its own reasoning errors because extraction inherits the same biases that produced those errors. A constraint ablation confirms the diagnosis: MAX-SAT and count-only aggregation agree on 803 of 804 predictions (\\S\\ref{sec:ablation}). Manual analysis shows only 11.5\\% of unique constraints evaluate differently across candidates; the remainder encode shared domain facts that contribute identical scores to every answer. Constraint extraction accounts for 48.7\\% of total SICA pipeline time, roughly doubling wall-clock cost for zero expected accuracy gain.\n\nOur contributions are:\n\\begin{itemize}\n\\item We evaluate SICA across five model families and three reasoning domains ($N > 1{,}300$), finding no improvement over majority voting in any condition.\n\\item We design an oracle control achieving $+8.82$\\,pp over SC ($p < 0.001$), causally localizing the failure to extraction quality rather than the aggregation mechanism.\n\\item We identify the multi-candidate rate $C_0$ as a zero-cost diagnostic: low $C_0$ rules out any possible SICA gain before constraint extraction begins.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 7,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          " ",
          " Neuro-symbolic methods that augment large language model (LLM) reasoning with formal solvers have demonstrated gains on logical reasoning benchmarks. Logic-LM \\citep{pan2023logiclm} and LINC \\citep{olausson2023linc} delegate formalization to external provers. More recent systems route problems to specialized solver paradigms \\citep{xu2026dylos}, apply logic-complete decomposition \\citep{li2025aristotle}, train dedicated first-order logic (FOL) verifiers on supervised data \\citep{wang2025fover}, or employ multi-perspective grounding \\citep{luo2025logicagent}. These systems report positive results on formal reasoning benchmarks, but a critical commonality unites them: each introduces capabilities beyond the reasoning model itself, whether trained verifiers, multi-paradigm solver selection, or external knowledge bases. The external machinery is effective but imposes practical costs in training data, integration complexity, and domain-specific engineering that limits portability.",
          " ",
          "-These results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability solver. Yet no prior work has systematically evaluated whether self-extraction produces constraints useful for answer aggregation, or characterized the conditions under which it succeeds or fails. This gap is consequential: the practical promise of neuro-symbolic reasoning hinges on whether the reasoning model alone can supply formal structure of sufficient quality, or whether external grounding is fundamentally required.",
          "+These results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability solver, with no domain-specific infrastructure. If successful, this approach would provide a lightweight, portable alternative to the external machinery that current systems require. Yet no prior work has systematically evaluated whether self-extraction produces constraints useful for answer aggregation, or characterized the conditions under which it succeeds or fails. This gap is consequential: the practical promise of neuro-symbolic reasoning hinges on whether the reasoning model alone can supply formal structure of sufficient quality, or whether external grounding is fundamentally required.",
          " ",
          " Self-Consistency (SC) selects the most frequent answer across multiple chain-of-thought samples \\citep{wang2023sc} and remains competitive across mathematical, logical, and commonsense reasoning \\citep{chen2024usc, taubenfeld2025cisc}. SC treats traces as black boxes, discarding all intermediate reasoning. Each trace, however, contains logical dependencies and structural relationships that could ground aggregation in formal logic, adding discriminative power beyond vote counting. This would also address SC's known scaling plateau, where additional traces yield diminishing returns \\citep{loo2025reevaluating}.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "f85b912d-a174-42ac-9cd8-f817fe8b0db7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Runtime record

_source line 1800_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] 8pp 达标，但两个章节过薄需要回填（利用 200-300 word buffer）：  **1. Introduction 645 → ~800 words (+155)** 645 对 EMNLP Intro 太短。把砍掉的核心内容加回来： - 确保贡献列表完整（4 条 contributions） - 确保 oracle 结果在 Intro 中被提及（+8.82p…",
  "leafUuid": "4246ee1b-87b4-4035-9af1-1bb281e891fb",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746"
}
```

---


### Runtime record

_source line 1801_

```json
{
  "type": "ai-title",
  "aiTitle": "Retrieve and process SSH check worker results",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746"
}
```

---


### Tool call

_source line 1802 · 2026-05-17T19:19:29.281Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01K8XnWNwh3ifvxzEjgVHUvR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
  "old_string": "We test five model families spanning 7B to 32B parameters (Qwen2.5-14B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B, QwQ-32B) across three reasoning domains",
  "new_string": "We test five model families spanning 7B to 32B parameters (Qwen2.5-14B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B, QwQ-32B), including instruction-tuned models, a reasoning-specialized model, and a distilled reasoning model, across three reasoning domains"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4246ee1b-87b4-4035-9af1-1bb281e891fb",
  "isSidechain": false,
  "requestId": "req_011Cb8gUXmEnM5euBkBe25pR",
  "type": "assistant",
  "uuid": "5bfd9a80-70ab-4fc9-9735-1f41b56c6420",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhFqVtMqN5YdzgY1RUdFrr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 753,
      "cache_read_input_tokens": 144389,
      "output_tokens": 346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 346,
          "cache_read_input_tokens": 144389,
          "cache_creation_input_tokens": 753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 753
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

_source line 1803 · 2026-05-17T19:19:29.321Z_

<details><summary>↩ Tool result · `toolu_01K8XnWNwh3ifvxzEjgVHUvR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bfd9a80-70ab-4fc9-9735-1f41b56c6420",
  "isSidechain": false,
  "promptId": "0fe74f2a-7c66-4010-b7d3-d39840f075b8",
  "type": "user",
  "uuid": "4d5d8b11-0734-43bb-9e6f-5c9b24ef8194",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
    "oldString": "We test five model families spanning 7B to 32B parameters (Qwen2.5-14B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B, QwQ-32B) across three reasoning domains",
    "newString": "We test five model families spanning 7B to 32B parameters (Qwen2.5-14B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B, QwQ-32B), including instruction-tuned models, a reasoning-specialized model, and a distilled reasoning model, across three reasoning domains",
    "originalFile": "\\section{Introduction}\\label{sec:introduction}\n\nNeuro-symbolic methods that augment large language model (LLM) reasoning with formal solvers have demonstrated gains on logical reasoning benchmarks. Logic-LM \\citep{pan2023logiclm} and LINC \\citep{olausson2023linc} delegate formalization to external provers. More recent systems route problems to specialized solver paradigms \\citep{xu2026dylos}, apply logic-complete decomposition \\citep{li2025aristotle}, train dedicated first-order logic (FOL) verifiers on supervised data \\citep{wang2025fover}, or employ multi-perspective grounding \\citep{luo2025logicagent}. These systems report positive results on formal reasoning benchmarks, but a critical commonality unites them: each introduces capabilities beyond the reasoning model itself, whether trained verifiers, multi-paradigm solver selection, or external knowledge bases. The external machinery is effective but imposes practical costs in training data, integration complexity, and domain-specific engineering that limits portability.\n\nThese results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability solver, with no domain-specific infrastructure. If successful, this approach would provide a lightweight, portable alternative to the external machinery that current systems require. Yet no prior work has systematically evaluated whether self-extraction produces constraints useful for answer aggregation, or characterized the conditions under which it succeeds or fails. This gap is consequential: the practical promise of neuro-symbolic reasoning hinges on whether the reasoning model alone can supply formal structure of sufficient quality, or whether external grounding is fundamentally required.\n\nSelf-Consistency (SC) selects the most frequent answer across multiple chain-of-thought samples \\citep{wang2023sc} and remains competitive across mathematical, logical, and commonsense reasoning \\citep{chen2024usc, taubenfeld2025cisc}. SC treats traces as black boxes, discarding all intermediate reasoning. Each trace, however, contains logical dependencies and structural relationships that could ground aggregation in formal logic, adding discriminative power beyond vote counting. This would also address SC's known scaling plateau, where additional traces yield diminishing returns \\citep{loo2025reevaluating}.\n\nWe evaluate this possibility through Symbolic Invariant Consensus Aggregation (SICA), a pipeline that extracts FOL constraints from $K$ reasoning traces produced by a single LLM, deduplicates by syntactic equivalence, and solves a weighted partial MAX-SAT problem via Z3 \\citep{demoura2008z3}. The answer best supported by the largest satisfiable constraint subset is selected (Figure~\\ref{fig:pipeline}). We test five model families spanning 7B to 32B parameters (Qwen2.5-14B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B, QwQ-32B) across three reasoning domains: formal logic (FOLIO \\citep{han2022folio}, ProofWriter \\citep{tafjord2021proofwriter}), commonsense (StrategyQA \\citep{geva2021strategyqa}), and science (ARC-Challenge \\citep{clark2018arc}), with supplementary probes on GSM8K \\citep{cobbe2021gsm8k} and AIME 2024, totaling more than 1,300 instances. An oracle control on FOLIO ($n=204$) replaces self-extracted constraints with gold FOL annotations verified by Z3, isolating extraction quality from aggregation effectiveness following established methodology \\citep{press2023compositionality}.\n\nAcross all conditions, SICA provides no statistically significant improvement over SC, with accuracy gaps between $-3.3$ and $+3.3$\\,pp. The oracle experiment yields a fundamentally different result: $+8.82$\\,pp over SC (McNemar $p = 6.15 \\times 10^{-5}$), confirming that the MAX-SAT mechanism is sound when given discriminative constraints. The bottleneck is extraction quality. Because the same model generates both answers and constraints, the extracted constraints are semantically coupled to their source answers and carry no independent signal. We term this the \\emph{capability trap}: the model cannot formalize corrections to its own reasoning errors because extraction inherits the same biases that produced those errors. A constraint ablation confirms the diagnosis: MAX-SAT and count-only aggregation agree on 803 of 804 predictions (\\S\\ref{sec:ablation}). Manual analysis shows only 11.5\\% of unique constraints evaluate differently across candidates; the remainder encode shared domain facts that contribute identical scores to every answer. Constraint extraction accounts for 48.7\\% of total SICA pipeline time, roughly doubling wall-clock cost for zero expected accuracy gain.\n\nOur contributions are:\n\\begin{itemize}\n\\item We evaluate SICA across five model families and three reasoning domains ($N > 1{,}300$), finding no improvement over majority voting in any condition.\n\\item We design an oracle control achieving $+8.82$\\,pp over SC ($p < 0.001$), causally localizing the failure to extraction quality rather than the aggregation mechanism.\n\\item We identify the multi-candidate rate $C_0$ as a zero-cost diagnostic: low $C_0$ rules out any possible SICA gain before constraint extraction begins.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 7,
        "newStart": 6,
        "newLines": 7,
        "lines": [
          " ",
          " Self-Consistency (SC) selects the most frequent answer across multiple chain-of-thought samples \\citep{wang2023sc} and remains competitive across mathematical, logical, and commonsense reasoning \\citep{chen2024usc, taubenfeld2025cisc}. SC treats traces as black boxes, discarding all intermediate reasoning. Each trace, however, contains logical dependencies and structural relationships that could ground aggregation in formal logic, adding discriminative power beyond vote counting. This would also address SC's known scaling plateau, where additional traces yield diminishing returns \\citep{loo2025reevaluating}.",
          " ",
          "-We evaluate this possibility through Symbolic Invariant Consensus Aggregation (SICA), a pipeline that extracts FOL constraints from $K$ reasoning traces produced by a single LLM, deduplicates by syntactic equivalence, and solves a weighted partial MAX-SAT problem via Z3 \\citep{demoura2008z3}. The answer best supported by the largest satisfiable constraint subset is selected (Figure~\\ref{fig:pipeline}). We test five model families spanning 7B to 32B parameters (Qwen2.5-14B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B, QwQ-32B) across three reasoning domains: formal logic (FOLIO \\citep{han2022folio}, ProofWriter \\citep{tafjord2021proofwriter}), commonsense (StrategyQA \\citep{geva2021strategyqa}), and science (ARC-Challenge \\citep{clark2018arc}), with supplementary probes on GSM8K \\citep{cobbe2021gsm8k} and AIME 2024, totaling more than 1,300 instances. An oracle control on FOLIO ($n=204$) replaces self-extracted constraints with gold FOL annotations verified by Z3, isolating extraction quality from aggregation effectiveness following established methodology \\citep{press2023compositionality}.",
          "+We evaluate this possibility through Symbolic Invariant Consensus Aggregation (SICA), a pipeline that extracts FOL constraints from $K$ reasoning traces produced by a single LLM, deduplicates by syntactic equivalence, and solves a weighted partial MAX-SAT problem via Z3 \\citep{demoura2008z3}. The answer best supported by the largest satisfiable constraint subset is selected (Figure~\\ref{fig:pipeline}). We test five model families spanning 7B to 32B parameters (Qwen2.5-14B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B, QwQ-32B), including instruction-tuned models, a reasoning-specialized model, and a distilled reasoning model, across three reasoning domains: formal logic (FOLIO \\citep{han2022folio}, ProofWriter \\citep{tafjord2021proofwriter}), commonsense (StrategyQA \\citep{geva2021strategyqa}), and science (ARC-Challenge \\citep{clark2018arc}), with supplementary probes on GSM8K \\citep{cobbe2021gsm8k} and AIME 2024, totaling more than 1,300 instances. An oracle control on FOLIO ($n=204$) replaces self-extracted constraints with gold FOL annotations verified by Z3, isolating extraction quality from aggregation effectiveness following established methodology \\citep{press2023compositionality}.",
          " ",
          " Across all conditions, SICA provides no statistically significant improvement over SC, with accuracy gaps between $-3.3$ and $+3.3$\\,pp. The oracle experiment yields a fundamentally different result: $+8.82$\\,pp over SC (McNemar $p = 6.15 \\times 10^{-5}$), confirming that the MAX-SAT mechanism is sound when given discriminative constraints. The bottleneck is extraction quality. Because the same model generates both answers and constraints, the extracted constraints are semantically coupled to their source answers and carry no independent signal. We term this the \\emph{capability trap}: the model cannot formalize corrections to its own reasoning errors because extraction inherits the same biases that produced those errors. A constraint ablation confirms the diagnosis: MAX-SAT and count-only aggregation agree on 803 of 804 predictions (\\S\\ref{sec:ablation}). Manual analysis shows only 11.5\\% of unique constraints evaluate differently across candidates; the remainder encode shared domain facts that contribute identical scores to every answer. Constraint extraction accounts for 48.7\\% of total SICA pipeline time, roughly doubling wall-clock cost for zero expected accuracy gain.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "5bfd9a80-70ab-4fc9-9735-1f41b56c6420",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Runtime record

_source line 1804 · 2026-05-17T19:19:29.329Z_

```json
{
  "parentUuid": "4d5d8b11-0734-43bb-9e6f-5c9b24ef8194",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8fe8ac6d-8a98-4796-9185-a286bd4c1839",
  "timestamp": "2026-05-17T19:19:29.329Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

---


### Tool call

_source line 1805 · 2026-05-17T19:19:34.758Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01WPvFemRnDqhGT2wsvFiCuN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
  "old_string": "\\item We identify the multi-candidate rate $C_0$ as a zero-cost diagnostic: low $C_0$ rules out any possible SICA gain before constraint extraction begins.\n\\end{itemize}",
  "new_string": "\\item We identify the multi-candidate rate $C_0$ as a zero-cost diagnostic: low $C_0$ rules out any possible SICA gain before constraint extraction begins.\n\\item We show through constraint ablation that MAX-SAT, count-only, and random-weight aggregation produce nearly identical predictions (803/804 agreement), confirming that self-extracted constraints carry no discriminative signal beyond vote counts (\\S\\ref{sec:ablation}).\n\\end{itemize}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fe8ac6d-8a98-4796-9185-a286bd4c1839",
  "isSidechain": false,
  "requestId": "req_011Cb8gUwi9XGjjkD6p3n7pj",
  "type": "assistant",
  "uuid": "3b936e8b-22eb-46fb-b955-f1e16d4a25e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019mFWPycisyedcwimCbfmur",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 505,
      "cache_read_input_tokens": 145142,
      "output_tokens": 298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 505,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 298,
          "cache_read_input_tokens": 145142,
          "cache_creation_input_tokens": 505,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 505
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

_source line 1806 · 2026-05-17T19:19:34.769Z_

<details><summary>↩ Tool result · `toolu_01WPvFemRnDqhGT2wsvFiCuN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b936e8b-22eb-46fb-b955-f1e16d4a25e3",
  "isSidechain": false,
  "promptId": "0fe74f2a-7c66-4010-b7d3-d39840f075b8",
  "type": "user",
  "uuid": "ecfc4670-362a-454d-9a67-3438f9d09565",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
    "oldString": "\\item We identify the multi-candidate rate $C_0$ as a zero-cost diagnostic: low $C_0$ rules out any possible SICA gain before constraint extraction begins.\n\\end{itemize}",
    "newString": "\\item We identify the multi-candidate rate $C_0$ as a zero-cost diagnostic: low $C_0$ rules out any possible SICA gain before constraint extraction begins.\n\\item We show through constraint ablation that MAX-SAT, count-only, and random-weight aggregation produce nearly identical predictions (803/804 agreement), confirming that self-extracted constraints carry no discriminative signal beyond vote counts (\\S\\ref{sec:ablation}).\n\\end{itemize}",
    "originalFile": "\\section{Introduction}\\label{sec:introduction}\n\nNeuro-symbolic methods that augment large language model (LLM) reasoning with formal solvers have demonstrated gains on logical reasoning benchmarks. Logic-LM \\citep{pan2023logiclm} and LINC \\citep{olausson2023linc} delegate formalization to external provers. More recent systems route problems to specialized solver paradigms \\citep{xu2026dylos}, apply logic-complete decomposition \\citep{li2025aristotle}, train dedicated first-order logic (FOL) verifiers on supervised data \\citep{wang2025fover}, or employ multi-perspective grounding \\citep{luo2025logicagent}. These systems report positive results on formal reasoning benchmarks, but a critical commonality unites them: each introduces capabilities beyond the reasoning model itself, whether trained verifiers, multi-paradigm solver selection, or external knowledge bases. The external machinery is effective but imposes practical costs in training data, integration complexity, and domain-specific engineering that limits portability.\n\nThese results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability solver, with no domain-specific infrastructure. If successful, this approach would provide a lightweight, portable alternative to the external machinery that current systems require. Yet no prior work has systematically evaluated whether self-extraction produces constraints useful for answer aggregation, or characterized the conditions under which it succeeds or fails. This gap is consequential: the practical promise of neuro-symbolic reasoning hinges on whether the reasoning model alone can supply formal structure of sufficient quality, or whether external grounding is fundamentally required.\n\nSelf-Consistency (SC) selects the most frequent answer across multiple chain-of-thought samples \\citep{wang2023sc} and remains competitive across mathematical, logical, and commonsense reasoning \\citep{chen2024usc, taubenfeld2025cisc}. SC treats traces as black boxes, discarding all intermediate reasoning. Each trace, however, contains logical dependencies and structural relationships that could ground aggregation in formal logic, adding discriminative power beyond vote counting. This would also address SC's known scaling plateau, where additional traces yield diminishing returns \\citep{loo2025reevaluating}.\n\nWe evaluate this possibility through Symbolic Invariant Consensus Aggregation (SICA), a pipeline that extracts FOL constraints from $K$ reasoning traces produced by a single LLM, deduplicates by syntactic equivalence, and solves a weighted partial MAX-SAT problem via Z3 \\citep{demoura2008z3}. The answer best supported by the largest satisfiable constraint subset is selected (Figure~\\ref{fig:pipeline}). We test five model families spanning 7B to 32B parameters (Qwen2.5-14B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B, QwQ-32B), including instruction-tuned models, a reasoning-specialized model, and a distilled reasoning model, across three reasoning domains: formal logic (FOLIO \\citep{han2022folio}, ProofWriter \\citep{tafjord2021proofwriter}), commonsense (StrategyQA \\citep{geva2021strategyqa}), and science (ARC-Challenge \\citep{clark2018arc}), with supplementary probes on GSM8K \\citep{cobbe2021gsm8k} and AIME 2024, totaling more than 1,300 instances. An oracle control on FOLIO ($n=204$) replaces self-extracted constraints with gold FOL annotations verified by Z3, isolating extraction quality from aggregation effectiveness following established methodology \\citep{press2023compositionality}.\n\nAcross all conditions, SICA provides no statistically significant improvement over SC, with accuracy gaps between $-3.3$ and $+3.3$\\,pp. The oracle experiment yields a fundamentally different result: $+8.82$\\,pp over SC (McNemar $p = 6.15 \\times 10^{-5}$), confirming that the MAX-SAT mechanism is sound when given discriminative constraints. The bottleneck is extraction quality. Because the same model generates both answers and constraints, the extracted constraints are semantically coupled to their source answers and carry no independent signal. We term this the \\emph{capability trap}: the model cannot formalize corrections to its own reasoning errors because extraction inherits the same biases that produced those errors. A constraint ablation confirms the diagnosis: MAX-SAT and count-only aggregation agree on 803 of 804 predictions (\\S\\ref{sec:ablation}). Manual analysis shows only 11.5\\% of unique constraints evaluate differently across candidates; the remainder encode shared domain facts that contribute identical scores to every answer. Constraint extraction accounts for 48.7\\% of total SICA pipeline time, roughly doubling wall-clock cost for zero expected accuracy gain.\n\nOur contributions are:\n\\begin{itemize}\n\\item We evaluate SICA across five model families and three reasoning domains ($N > 1{,}300$), finding no improvement over majority voting in any condition.\n\\item We design an oracle control achieving $+8.82$\\,pp over SC ($p < 0.001$), causally localizing the failure to extraction quality rather than the aggregation mechanism.\n\\item We identify the multi-candidate rate $C_0$ as a zero-cost diagnostic: low $C_0$ rules out any possible SICA gain before constraint extraction begins.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 4,
        "newStart": 15,
        "newLines": 5,
        "lines": [
          " \\item We evaluate SICA across five model families and three reasoning domains ($N > 1{,}300$), finding no improvement over majority voting in any condition.",
          " \\item We design an oracle control achieving $+8.82$\\,pp over SC ($p < 0.001$), causally localizing the failure to extraction quality rather than the aggregation mechanism.",
          " \\item We identify the multi-candidate rate $C_0$ as a zero-cost diagnostic: low $C_0$ rules out any possible SICA gain before constraint extraction begins.",
          "+\\item We show through constraint ablation that MAX-SAT, count-only, and random-weight aggregation produce nearly identical predictions (803/804 agreement), confirming that self-extracted constraints carry no discriminative signal beyond vote counts (\\S\\ref{sec:ablation}).",
          " \\end{itemize}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "3b936e8b-22eb-46fb-b955-f1e16d4a25e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Assistant

_source line 1807 · 2026-05-17T19:19:37.283Z_

Now expand SC paragraph slightly:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecfc4670-362a-454d-9a67-3438f9d09565",
  "isSidechain": false,
  "requestId": "req_011Cb8gVLsBEXLx1nwR7jQxH",
  "type": "assistant",
  "uuid": "d197d389-4ab3-4b17-b1bb-ab9f2c3b97e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BovbfnMuZ5cqtBKLExhbP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 353,
      "cache_read_input_tokens": 145647,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 353,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 211,
          "cache_read_input_tokens": 145647,
          "cache_creation_input_tokens": 353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 353
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

_source line 1808 · 2026-05-17T19:19:38.979Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01UHMWZwx4TphzdjXxgRjqCp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
  "old_string": "Each trace, however, contains logical dependencies and structural relationships that could ground aggregation in formal logic, adding discriminative power beyond vote counting.",
  "new_string": "Each trace, however, contains intermediate steps, logical dependencies, and structural relationships that could in principle ground aggregation in formal logic, adding discriminative power beyond vote counting."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d197d389-4ab3-4b17-b1bb-ab9f2c3b97e3",
  "isSidechain": false,
  "requestId": "req_011Cb8gVLsBEXLx1nwR7jQxH",
  "type": "assistant",
  "uuid": "41ded333-fb7d-40f8-a515-7bb65dbc08d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BovbfnMuZ5cqtBKLExhbP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 353,
      "cache_read_input_tokens": 145647,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 353,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 211,
          "cache_read_input_tokens": 145647,
          "cache_creation_input_tokens": 353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 353
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

_source line 1809 · 2026-05-17T19:19:38.991Z_

<details><summary>↩ Tool result · `toolu_01UHMWZwx4TphzdjXxgRjqCp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41ded333-fb7d-40f8-a515-7bb65dbc08d3",
  "isSidechain": false,
  "promptId": "0fe74f2a-7c66-4010-b7d3-d39840f075b8",
  "type": "user",
  "uuid": "f478523f-6bca-4174-ad5d-40a84d46451d",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/introduction.tex",
    "oldString": "Each trace, however, contains logical dependencies and structural relationships that could ground aggregation in formal logic, adding discriminative power beyond vote counting.",
    "newString": "Each trace, however, contains intermediate steps, logical dependencies, and structural relationships that could in principle ground aggregation in formal logic, adding discriminative power beyond vote counting.",
    "originalFile": "\\section{Introduction}\\label{sec:introduction}\n\nNeuro-symbolic methods that augment large language model (LLM) reasoning with formal solvers have demonstrated gains on logical reasoning benchmarks. Logic-LM \\citep{pan2023logiclm} and LINC \\citep{olausson2023linc} delegate formalization to external provers. More recent systems route problems to specialized solver paradigms \\citep{xu2026dylos}, apply logic-complete decomposition \\citep{li2025aristotle}, train dedicated first-order logic (FOL) verifiers on supervised data \\citep{wang2025fover}, or employ multi-perspective grounding \\citep{luo2025logicagent}. These systems report positive results on formal reasoning benchmarks, but a critical commonality unites them: each introduces capabilities beyond the reasoning model itself, whether trained verifiers, multi-paradigm solver selection, or external knowledge bases. The external machinery is effective but imposes practical costs in training data, integration complexity, and domain-specific engineering that limits portability.\n\nThese results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability solver, with no domain-specific infrastructure. If successful, this approach would provide a lightweight, portable alternative to the external machinery that current systems require. Yet no prior work has systematically evaluated whether self-extraction produces constraints useful for answer aggregation, or characterized the conditions under which it succeeds or fails. This gap is consequential: the practical promise of neuro-symbolic reasoning hinges on whether the reasoning model alone can supply formal structure of sufficient quality, or whether external grounding is fundamentally required.\n\nSelf-Consistency (SC) selects the most frequent answer across multiple chain-of-thought samples \\citep{wang2023sc} and remains competitive across mathematical, logical, and commonsense reasoning \\citep{chen2024usc, taubenfeld2025cisc}. SC treats traces as black boxes, discarding all intermediate reasoning. Each trace, however, contains logical dependencies and structural relationships that could ground aggregation in formal logic, adding discriminative power beyond vote counting. This would also address SC's known scaling plateau, where additional traces yield diminishing returns \\citep{loo2025reevaluating}.\n\nWe evaluate this possibility through Symbolic Invariant Consensus Aggregation (SICA), a pipeline that extracts FOL constraints from $K$ reasoning traces produced by a single LLM, deduplicates by syntactic equivalence, and solves a weighted partial MAX-SAT problem via Z3 \\citep{demoura2008z3}. The answer best supported by the largest satisfiable constraint subset is selected (Figure~\\ref{fig:pipeline}). We test five model families spanning 7B to 32B parameters (Qwen2.5-14B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B, QwQ-32B), including instruction-tuned models, a reasoning-specialized model, and a distilled reasoning model, across three reasoning domains: formal logic (FOLIO \\citep{han2022folio}, ProofWriter \\citep{tafjord2021proofwriter}), commonsense (StrategyQA \\citep{geva2021strategyqa}), and science (ARC-Challenge \\citep{clark2018arc}), with supplementary probes on GSM8K \\citep{cobbe2021gsm8k} and AIME 2024, totaling more than 1,300 instances. An oracle control on FOLIO ($n=204$) replaces self-extracted constraints with gold FOL annotations verified by Z3, isolating extraction quality from aggregation effectiveness following established methodology \\citep{press2023compositionality}.\n\nAcross all conditions, SICA provides no statistically significant improvement over SC, with accuracy gaps between $-3.3$ and $+3.3$\\,pp. The oracle experiment yields a fundamentally different result: $+8.82$\\,pp over SC (McNemar $p = 6.15 \\times 10^{-5}$), confirming that the MAX-SAT mechanism is sound when given discriminative constraints. The bottleneck is extraction quality. Because the same model generates both answers and constraints, the extracted constraints are semantically coupled to their source answers and carry no independent signal. We term this the \\emph{capability trap}: the model cannot formalize corrections to its own reasoning errors because extraction inherits the same biases that produced those errors. A constraint ablation confirms the diagnosis: MAX-SAT and count-only aggregation agree on 803 of 804 predictions (\\S\\ref{sec:ablation}). Manual analysis shows only 11.5\\% of unique constraints evaluate differently across candidates; the remainder encode shared domain facts that contribute identical scores to every answer. Constraint extraction accounts for 48.7\\% of total SICA pipeline time, roughly doubling wall-clock cost for zero expected accuracy gain.\n\nOur contributions are:\n\\begin{itemize}\n\\item We evaluate SICA across five model families and three reasoning domains ($N > 1{,}300$), finding no improvement over majority voting in any condition.\n\\item We design an oracle control achieving $+8.82$\\,pp over SC ($p < 0.001$), causally localizing the failure to extraction quality rather than the aggregation mechanism.\n\\item We identify the multi-candidate rate $C_0$ as a zero-cost diagnostic: low $C_0$ rules out any possible SICA gain before constraint extraction begins.\n\\item We show through constraint ablation that MAX-SAT, count-only, and random-weight aggregation produce nearly identical predictions (803/804 agreement), confirming that self-extracted constraints carry no discriminative signal beyond vote counts (\\S\\ref{sec:ablation}).\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 7,
        "newStart": 4,
        "newLines": 7,
        "lines": [
          " ",
          " These results raise a direct question: can the reasoning model itself extract useful formal constraints from its own traces? Same-model self-extraction would require no training data, no external prover, and no second model. Practitioners could augment any LLM with symbolic verification by adding a single extraction prompt and a satisfiability solver, with no domain-specific infrastructure. If successful, this approach would provide a lightweight, portable alternative to the external machinery that current systems require. Yet no prior work has systematically evaluated whether self-extraction produces constraints useful for answer aggregation, or characterized the conditions under which it succeeds or fails. This gap is consequential: the practical promise of neuro-symbolic reasoning hinges on whether the reasoning model alone can supply formal structure of sufficient quality, or whether external grounding is fundamentally required.",
          " ",
          "-Self-Consistency (SC) selects the most frequent answer across multiple chain-of-thought samples \\citep{wang2023sc} and remains competitive across mathematical, logical, and commonsense reasoning \\citep{chen2024usc, taubenfeld2025cisc}. SC treats traces as black boxes, discarding all intermediate reasoning. Each trace, however, contains logical dependencies and structural relationships that could ground aggregation in formal logic, adding discriminative power beyond vote counting. This would also address SC's known scaling plateau, where additional traces yield diminishing returns \\citep{loo2025reevaluating}.",
          "+Self-Consistency (SC) selects the most frequent answer across multiple chain-of-thought samples \\citep{wang2023sc} and remains competitive across mathematical, logical, and commonsense reasoning \\citep{chen2024usc, taubenfeld2025cisc}. SC treats traces as black boxes, discarding all intermediate reasoning. Each trace, however, contains intermediate steps, logical dependencies, and structural relationships that could in principle ground aggregation in formal logic, adding discriminative power beyond vote counting. This would also address SC's known scaling plateau, where additional traces yield diminishing returns \\citep{loo2025reevaluating}.",
          " ",
          " We evaluate this possibility through Symbolic Invariant Consensus Aggregation (SICA), a pipeline that extracts FOL constraints from $K$ reasoning traces produced by a single LLM, deduplicates by syntactic equivalence, and solves a weighted partial MAX-SAT problem via Z3 \\citep{demoura2008z3}. The answer best supported by the largest satisfiable constraint subset is selected (Figure~\\ref{fig:pipeline}). We test five model families spanning 7B to 32B parameters (Qwen2.5-14B-Instruct, Mistral-7B-Instruct-v0.3, LLaMA-3.1-8B-Instruct, DeepSeek-R1-Distill-Qwen-7B, QwQ-32B), including instruction-tuned models, a reasoning-specialized model, and a distilled reasoning model, across three reasoning domains: formal logic (FOLIO \\citep{han2022folio}, ProofWriter \\citep{tafjord2021proofwriter}), commonsense (StrategyQA \\citep{geva2021strategyqa}), and science (ARC-Challenge \\citep{clark2018arc}), with supplementary probes on GSM8K \\citep{cobbe2021gsm8k} and AIME 2024, totaling more than 1,300 instances. An oracle control on FOLIO ($n=204$) replaces self-extracted constraints with gold FOL annotations verified by Z3, isolating extraction quality from aggregation effectiveness following established methodology \\citep{press2023compositionality}.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "41ded333-fb7d-40f8-a515-7bb65dbc08d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Runtime record

_source line 1810_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] 8pp 达标，但两个章节过薄需要回填（利用 200-300 word buffer）：  **1. Introduction 645 → ~800 words (+155)** 645 对 EMNLP Intro 太短。把砍掉的核心内容加回来： - 确保贡献列表完整（4 条 contributions） - 确保 oracle 结果在 Intro 中被提及（+8.82p…",
  "leafUuid": "f478523f-6bca-4174-ad5d-40a84d46451d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746"
}
```

---


### Runtime record

_source line 1811_

```json
{
  "type": "ai-title",
  "aiTitle": "Retrieve and process SSH check worker results",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746"
}
```

---


### Assistant

_source line 1812 · 2026-05-17T19:19:42.668Z_

Now **Discussion** (273→~400 words): expand constructive outlook and C0 guidance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f478523f-6bca-4174-ad5d-40a84d46451d",
  "isSidechain": false,
  "requestId": "req_011Cb8gVfysrC6z8nqUcmQ1o",
  "type": "assistant",
  "uuid": "b604fee4-77e3-4ccb-a7d5-a828d8be3d69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uM3a19jJzh7D39ZWS9PT7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 266,
      "cache_read_input_tokens": 146000,
      "output_tokens": 715,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 266,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 715,
          "cache_read_input_tokens": 146000,
          "cache_creation_input_tokens": 266,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 266
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

_source line 1813 · 2026-05-17T19:19:51.184Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01GSPXB4s7XYL8GfdunazPQ1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex",
  "old_string": "The $+8.82$\\,pp oracle ceiling quantifies the potential locked behind the capability trap. Three paths can unlock it: trained FOL extractors supervised on gold annotations, external provers that verify constraints independently of the reasoning model, and cross-model extraction that breaks the self-reference loop. Each targets the extraction bottleneck; improving the aggregation mechanism offers no path forward. For practitioners, $C_0$ provides a zero-cost screening criterion: when $C_0 < 5\\%$, SICA degenerates to SC by construction. High $C_0$ is necessary but not sufficient, as the capability trap renders constraints non-discriminative even when disagreement is abundant ($C_0 = 61.8\\%$, $\\Delta = -2.45$~pp, n.s., for LLaMA-3.1-8B on FOLIO).",
  "new_string": "The $+8.82$\\,pp oracle ceiling quantifies the potential locked behind the capability trap. Three concrete paths can unlock it. First, trained FOL extractors supervised on datasets with gold annotations (such as FOLIO) can learn extraction patterns that exceed same-model capabilities; FoVer \\citep{wang2025fover} demonstrates this approach with a dedicated verifier. Second, external provers that verify constraints independently of the reasoning model eliminate the circular dependency between generation and verification. Third, cross-model extraction, where a separate model extracts constraints from another model's traces, breaks the self-reference loop that produces non-discriminative constraints. Each path targets the extraction bottleneck directly; since MAX-SAT and count-only produce identical predictions on 803/804 instances, improving the aggregation mechanism offers no path forward.\n\nFor practitioners considering constraint-based voting, $C_0$ provides a zero-cost screening criterion computable from the trace sampling stage alone, before any constraint extraction or solver invocation. When $C_0$ falls below 5\\%, SICA degenerates to SC by construction. High $C_0$ is necessary but not sufficient, as the capability trap renders constraints non-discriminative even when disagreement is abundant ($C_0 = 61.8\\%$, $\\Delta = -2.45$~pp, n.s., for LLaMA-3.1-8B on FOLIO). The recommended workflow is: compute $C_0$, and if it exceeds 5\\%, assess constraint quality on a small pilot before committing to full-scale extraction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b604fee4-77e3-4ccb-a7d5-a828d8be3d69",
  "isSidechain": false,
  "requestId": "req_011Cb8gVfysrC6z8nqUcmQ1o",
  "type": "assistant",
  "uuid": "ff131d3c-d342-4e7e-8d80-fb026dfc42d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012uM3a19jJzh7D39ZWS9PT7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 266,
      "cache_read_input_tokens": 146000,
      "output_tokens": 715,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 266,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 715,
          "cache_read_input_tokens": 146000,
          "cache_creation_input_tokens": 266,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 266
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

_source line 1814 · 2026-05-17T19:19:51.203Z_

<details><summary>↩ Tool result · `toolu_01GSPXB4s7XYL8GfdunazPQ1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff131d3c-d342-4e7e-8d80-fb026dfc42d0",
  "isSidechain": false,
  "promptId": "0fe74f2a-7c66-4010-b7d3-d39840f075b8",
  "type": "user",
  "uuid": "64bbd97d-a8f4-4ccd-adb5-b965638ef36d",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/discussion.tex",
    "oldString": "The $+8.82$\\,pp oracle ceiling quantifies the potential locked behind the capability trap. Three paths can unlock it: trained FOL extractors supervised on gold annotations, external provers that verify constraints independently of the reasoning model, and cross-model extraction that breaks the self-reference loop. Each targets the extraction bottleneck; improving the aggregation mechanism offers no path forward. For practitioners, $C_0$ provides a zero-cost screening criterion: when $C_0 < 5\\%$, SICA degenerates to SC by construction. High $C_0$ is necessary but not sufficient, as the capability trap renders constraints non-discriminative even when disagreement is abundant ($C_0 = 61.8\\%$, $\\Delta = -2.45$~pp, n.s., for LLaMA-3.1-8B on FOLIO).",
    "newString": "The $+8.82$\\,pp oracle ceiling quantifies the potential locked behind the capability trap. Three concrete paths can unlock it. First, trained FOL extractors supervised on datasets with gold annotations (such as FOLIO) can learn extraction patterns that exceed same-model capabilities; FoVer \\citep{wang2025fover} demonstrates this approach with a dedicated verifier. Second, external provers that verify constraints independently of the reasoning model eliminate the circular dependency between generation and verification. Third, cross-model extraction, where a separate model extracts constraints from another model's traces, breaks the self-reference loop that produces non-discriminative constraints. Each path targets the extraction bottleneck directly; since MAX-SAT and count-only produce identical predictions on 803/804 instances, improving the aggregation mechanism offers no path forward.\n\nFor practitioners considering constraint-based voting, $C_0$ provides a zero-cost screening criterion computable from the trace sampling stage alone, before any constraint extraction or solver invocation. When $C_0$ falls below 5\\%, SICA degenerates to SC by construction. High $C_0$ is necessary but not sufficient, as the capability trap renders constraints non-discriminative even when disagreement is abundant ($C_0 = 61.8\\%$, $\\Delta = -2.45$~pp, n.s., for LLaMA-3.1-8B on FOLIO). The recommended workflow is: compute $C_0$, and if it exceeds 5\\%, assess constraint quality on a small pilot before committing to full-scale extraction.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\nThe oracle experiment (Table~\\ref{tab:main_results}, bottom) constitutes a causal intervention that isolates the source of failure. By replacing only the constraint source while holding all other pipeline components fixed, we establish that aggregation is not the bottleneck: the $+8.82$\\,pp improvement ($p < 0.001$) pinpoints same-model self-extraction as the single point of failure. This oracle design follows established methodology where component-level interventions isolate error sources \\citep{press2023compositionality, trivedi2023ircot, saparov2023greedy}.\n\nManual analysis of constraint quality explains the mechanism. Across 43 pilot problems (23 with multiple candidates), only 11.5\\% of unique constraints evaluated differently across candidates. The remainder encoded shared domain facts (predicate definitions, background implications, intermediate steps) satisfied equally by every candidate. In only 4 of 23 multi-answer problems (17.4\\%) did discriminative constraints favor a non-majority answer, accounting for the 803/804 agreement between MAX-SAT and count-only (Table~\\ref{tab:ablation}).\n\nThe computational cost is substantial: constraint extraction accounts for 48.7\\% of total SICA pipeline time, roughly doubling wall-clock cost compared to SC alone. Among 31 disagreements with SC, wins and losses approximately cancel (16 vs.\\ 14), yielding zero net accuracy gain.\n\nThe $+8.82$\\,pp oracle ceiling quantifies the potential locked behind the capability trap. Three paths can unlock it: trained FOL extractors supervised on gold annotations, external provers that verify constraints independently of the reasoning model, and cross-model extraction that breaks the self-reference loop. Each targets the extraction bottleneck; improving the aggregation mechanism offers no path forward. For practitioners, $C_0$ provides a zero-cost screening criterion: when $C_0 < 5\\%$, SICA degenerates to SC by construction. High $C_0$ is necessary but not sufficient, as the capability trap renders constraints non-discriminative even when disagreement is abundant ($C_0 = 61.8\\%$, $\\Delta = -2.45$~pp, n.s., for LLaMA-3.1-8B on FOLIO).\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 4,
        "newStart": 7,
        "newLines": 6,
        "lines": [
          " ",
          " The computational cost is substantial: constraint extraction accounts for 48.7\\% of total SICA pipeline time, roughly doubling wall-clock cost compared to SC alone. Among 31 disagreements with SC, wins and losses approximately cancel (16 vs.\\ 14), yielding zero net accuracy gain.",
          " ",
          "-The $+8.82$\\,pp oracle ceiling quantifies the potential locked behind the capability trap. Three paths can unlock it: trained FOL extractors supervised on gold annotations, external provers that verify constraints independently of the reasoning model, and cross-model extraction that breaks the self-reference loop. Each targets the extraction bottleneck; improving the aggregation mechanism offers no path forward. For practitioners, $C_0$ provides a zero-cost screening criterion: when $C_0 < 5\\%$, SICA degenerates to SC by construction. High $C_0$ is necessary but not sufficient, as the capability trap renders constraints non-discriminative even when disagreement is abundant ($C_0 = 61.8\\%$, $\\Delta = -2.45$~pp, n.s., for LLaMA-3.1-8B on FOLIO).",
          "+The $+8.82$\\,pp oracle ceiling quantifies the potential locked behind the capability trap. Three concrete paths can unlock it. First, trained FOL extractors supervised on datasets with gold annotations (such as FOLIO) can learn extraction patterns that exceed same-model capabilities; FoVer \\citep{wang2025fover} demonstrates this approach with a dedicated verifier. Second, external provers that verify constraints independently of the reasoning model eliminate the circular dependency between generation and verification. Third, cross-model extraction, where a separate model extracts constraints from another model's traces, breaks the self-reference loop that produces non-discriminative constraints. Each path targets the extraction bottleneck directly; since MAX-SAT and count-only produce identical predictions on 803/804 instances, improving the aggregation mechanism offers no path forward.",
          "+",
          "+For practitioners considering constraint-based voting, $C_0$ provides a zero-cost screening criterion computable from the trace sampling stage alone, before any constraint extraction or solver invocation. When $C_0$ falls below 5\\%, SICA degenerates to SC by construction. High $C_0$ is necessary but not sufficient, as the capability trap renders constraints non-discriminative even when disagreement is abundant ($C_0 = 61.8\\%$, $\\Delta = -2.45$~pp, n.s., for LLaMA-3.1-8B on FOLIO). The recommended workflow is: compute $C_0$, and if it exceeds 5\\%, assess constraint quality on a small pilot before committing to full-scale extraction."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "ff131d3c-d342-4e7e-8d80-fb026dfc42d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Assistant

_source line 1815 · 2026-05-17T19:19:53.713Z_

Compile and check page count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64bbd97d-a8f4-4ccd-adb5-b965638ef36d",
  "isSidechain": false,
  "requestId": "req_011Cb8gWZ89c4GNhVgVkvXFm",
  "type": "assistant",
  "uuid": "8b9c02d0-8e58-4334-8e66-91c36da3b810",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Yb9pyXKeSayxkJSH8j6DiN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 146266,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 146266,
          "cache_creation_input_tokens": 770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 770
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

_source line 1816 · 2026-05-17T19:19:57.566Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EbjEGDVmBzesPrDuox7SaE`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && bibtex main 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep \"Output written\"",
  "description": "Full build after expansion"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b9c02d0-8e58-4334-8e66-91c36da3b810",
  "isSidechain": false,
  "requestId": "req_011Cb8gWZ89c4GNhVgVkvXFm",
  "type": "assistant",
  "uuid": "3ab306d4-d05d-42b3-b1af-b84fc0de9430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Yb9pyXKeSayxkJSH8j6DiN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 146266,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 770,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 204,
          "cache_read_input_tokens": 146266,
          "cache_creation_input_tokens": 770,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 770
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

_source line 1817 · 2026-05-17T19:20:00.825Z_

<details><summary>↩ Tool result · `toolu_01EbjEGDVmBzesPrDuox7SaE`</summary>

```text
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
Output written on main.pdf (12 pages, 378616 bytes).
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ab306d4-d05d-42b3-b1af-b84fc0de9430",
  "isSidechain": false,
  "promptId": "0fe74f2a-7c66-4010-b7d3-d39840f075b8",
  "type": "user",
  "uuid": "7192933c-cf77-4915-94f5-3bb010423d5e",
  "toolUseResult": {
    "stdout": "The top-level auxiliary file: main.aux\nThe style file: acl_natbib.bst\nDatabase file #1: references.bib\nOutput written on main.pdf (12 pages, 378616 bytes).",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "3ab306d4-d05d-42b3-b1af-b84fc0de9430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Assistant

_source line 1818 · 2026-05-17T19:20:03.436Z_

12 pages. Verify main content boundary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7192933c-cf77-4915-94f5-3bb010423d5e",
  "isSidechain": false,
  "requestId": "req_011Cb8gXGES6xZCPqvtHNLuM",
  "type": "assistant",
  "uuid": "6bbe0859-75a0-4320-861f-7d21e21fc295",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBJpBK6C2cURSGf5JvMgUF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 317,
      "cache_read_input_tokens": 147036,
      "output_tokens": 311,
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
          "output_tokens": 311,
          "cache_read_input_tokens": 147036,
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

_source line 1819 · 2026-05-17T19:20:07.407Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DgqSYxeK2Rq3DQe4s3rMAt`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper && python3 -c \"\nimport subprocess, re\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\nfor kw in ['Limitations', 'References']:\n    for m in re.finditer(kw, text):\n        pos = m.start()\n        page = text[:pos].count('\\f') + 1\n        ctx = text[max(0,pos-10):pos+40].replace('\\n',' ').strip()\n        print(f'{kw}: page {page} ... {ctx}')\n\" && echo \"---\" && for f in introduction.tex discussion.tex; do count=$(wc -w < \"$f\"); printf \"%-20s %4d words\\n\" \"$f\" \"$count\"; done",
  "description": "Verify page boundary and word counts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bbe0859-75a0-4320-861f-7d21e21fc295",
  "isSidechain": false,
  "requestId": "req_011Cb8gXGES6xZCPqvtHNLuM",
  "type": "assistant",
  "uuid": "8d64bc72-431d-4c8f-b27c-a5e83e69e54d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBJpBK6C2cURSGf5JvMgUF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 317,
      "cache_read_input_tokens": 147036,
      "output_tokens": 311,
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
          "output_tokens": 311,
          "cache_read_input_tokens": 147036,
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

_source line 1820 · 2026-05-17T19:20:07.655Z_

<details><summary>↩ Tool result · `toolu_01DgqSYxeK2Rq3DQe4s3rMAt`</summary>

```text
Limitations: page 5 ... Scope and Limitations  5  411 412 413 414  416  4
Limitations: page 8 ... ap.  643  Limitations  644  Several limitations bo
References: page 8 ... 645  664  References  665  Xinyun Chen, Renat Aksi
---
introduction.tex      719 words
discussion.tex        378 words
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d64bc72-431d-4c8f-b27c-a5e83e69e54d",
  "isSidechain": false,
  "promptId": "0fe74f2a-7c66-4010-b7d3-d39840f075b8",
  "type": "user",
  "uuid": "4b85c263-bf3c-46ba-a2bd-84e705808cdf",
  "toolUseResult": {
    "stdout": "Limitations: page 5 ... Scope and Limitations  5  411 412 413 414  416  4\nLimitations: page 8 ... ap.  643  Limitations  644  Several limitations bo\nReferences: page 8 ... 645  664  References  665  Xinyun Chen, Renat Aksi\n---\nintroduction.tex      719 words\ndiscussion.tex        378 words",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8d64bc72-431d-4c8f-b27c-a5e83e69e54d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Assistant

_source line 1821 · 2026-05-17T19:20:13.307Z_

Limitations section on page 8, References on page 8. Main content ≤ 8 pages confirmed.

Word counts: Introduction 719 (target ~800), Discussion 378 (target ~400). Both within range.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b85c263-bf3c-46ba-a2bd-84e705808cdf",
  "isSidechain": false,
  "requestId": "req_011Cb8gXmTLQQyyYUCJxs1bH",
  "type": "assistant",
  "uuid": "ca1f2dc0-e05d-4cfe-a031-a9c375505afb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQRrJojKkSt4ySYZ5qsftr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 468,
      "cache_read_input_tokens": 147353,
      "output_tokens": 477,
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
          "output_tokens": 477,
          "cache_read_input_tokens": 147353,
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

_source line 1822 · 2026-05-17T19:20:21.312Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director · `toolu_01EyBSS2wiBFzzjf845D7Boy`</summary>

```json
{
  "text": "[资源] GPU 0/0 | Worker 0 | 磁盘: 未检查\n\n回填完成，编译确认仍 ≤8pp（Limitations page 8, References page 8）。\n\n| Section | Before | After | Target |\n|---------|--------|-------|--------|\n| Introduction | 645 | 719 | ~800 |\n| Discussion | 273 | 378 | ~400 |\n\nIntroduction 变更：\n- Para 2 加回 \"with no domain-specific infrastructure. If successful...\" 一句（self-extraction 的实际价值）\n- Para 4 加 \"including instruction-tuned models, a reasoning-specialized model, and a distilled reasoning model\"\n- 贡献列表恢复为 4 条（+constraint ablation: 803/804 agreement）\n- SC 段加 \"intermediate steps\"\n\nDiscussion 变更：\n- Constructive outlook 扩展为完整段落，三条路径各有 1-2 句说明，引用 FoVer 作为 trained extractor 先例\n- C0 实用指导扩展：加 \"computable from trace sampling stage alone\"，加推荐工作流（compute C0 → assess pilot quality）\n\n修复清单全部完成。待处理：fig1_pipeline.pdf",
  "project": "symb_invariant_consensus"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca1f2dc0-e05d-4cfe-a031-a9c375505afb",
  "isSidechain": false,
  "requestId": "req_011Cb8gXmTLQQyyYUCJxs1bH",
  "type": "assistant",
  "uuid": "79a4c8ed-fad9-4a9d-920d-83e4bb9ac2de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WQRrJojKkSt4ySYZ5qsftr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 468,
      "cache_read_input_tokens": 147353,
      "output_tokens": 477,
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
          "output_tokens": 477,
          "cache_read_input_tokens": 147353,
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

_source line 1823 · 2026-05-17T19:20:25.007Z_

<details><summary>↩ Tool result · `toolu_01EyBSS2wiBFzzjf845D7Boy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79a4c8ed-fad9-4a9d-920d-83e4bb9ac2de",
  "isSidechain": false,
  "promptId": "0fe74f2a-7c66-4010-b7d3-d39840f075b8",
  "type": "user",
  "uuid": "8bbe18cc-8333-4433-8496-62d8bff59b5b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_970d5ea3f54df81296b97321fcded892:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "79a4c8ed-fad9-4a9d-920d-83e4bb9ac2de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Runtime record

_source line 1824 · 2026-05-17T19:20:25.012Z_

```json
{
  "parentUuid": "8bbe18cc-8333-4433-8496-62d8bff59b5b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ccd151bf-226d-4c3e-be65-e3ab910d4568",
  "timestamp": "2026-05-17T19:20:25.012Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

---


### Runtime record

_source line 1825_

```json
{
  "type": "ai-title",
  "aiTitle": "Retrieve and process SSH check worker results",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746"
}
```

---


### Runtime record

_source line 1826 · 2026-05-17T19:20:56.010Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T19:20:56.010Z",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "content": "[Director 指令] **fig1 pipeline 图 — 最简方案**\n\n之前的 Worker 卡了 100 分钟。换简单方案：\n\n**直接用 TikZ 在 LaTeX 中画 pipeline 图**，不用 Python/matplotlib。SICA pipeline 就是一个简单流程图：\n\n```\nQuestion q → Sample K traces (T=0.7) → Extract FOL constraints → Deduplicate + Weight → MAX-SAT (Z3) → Answer\n                                                                                              ↕\n                                                              SC baseline: majority vote ←────┘\n```\n\n要求：\n1. 简洁的水平流程图，5-6 个 box + arrows\n2. 用 TikZ（\\usepackage{tikz}），不依赖外部文件\n3. 标注 SC 分支（majority vote）和 SICA 分支（MAX-SAT）的分叉点\n4. 放在 method.tex 的 \\subsection{Overview} 后面\n5. 单栏宽度，不超过 5cm 高\n\n如果 \\includegraphics 之前引用的是 fig1_pipeline.pdf，改为 inline TikZ。如果实在写不出好的 TikZ，跳过 fig1（删除引用），投稿时不含 pipeline 图也可以。不要再 spawn worker 做这个。"
}
````

---


### Runtime record

_source line 1827 · 2026-05-17T19:20:56.011Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T19:20:56.011Z",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746"
}
```

---


## Round 144

## Round 144

2 recorded events


### User

_source line 1828 · 2026-05-17T19:20:55.996Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ccd151bf-226d-4c3e-be65-e3ab910d4568",
  "isSidechain": false,
  "promptId": "febadbac-8aba-4e81-aed3-8415bae4e429",
  "type": "user",
  "isMeta": true,
  "uuid": "30ffb0e1-ecda-4e24-ae92-6b386277123c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Assistant

_source line 1829 · 2026-05-17T19:20:55.996Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30ffb0e1-ecda-4e24-ae92-6b386277123c",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "9ccccb0f-0ee8-4c6a-8d8c-3599a7795c26",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "id": "1c2568e2-01df-4af9-8388-21669b260232",
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


## Round 145

## Round 145

44 recorded events


### User

_source line 1830 · 2026-05-17T19:20:56.132Z_

[Director 指令] **fig1 pipeline 图 — 最简方案**

之前的 Worker 卡了 100 分钟。换简单方案：

**直接用 TikZ 在 LaTeX 中画 pipeline 图**，不用 Python/matplotlib。SICA pipeline 就是一个简单流程图：

```
Question q → Sample K traces (T=0.7) → Extract FOL constraints → Deduplicate + Weight → MAX-SAT (Z3) → Answer
                                                                                              ↕
                                                              SC baseline: majority vote ←────┘
```

要求：
1. 简洁的水平流程图，5-6 个 box + arrows
2. 用 TikZ（\usepackage{tikz}），不依赖外部文件
3. 标注 SC 分支（majority vote）和 SICA 分支（MAX-SAT）的分叉点
4. 放在 method.tex 的 \subsection{Overview} 后面
5. 单栏宽度，不超过 5cm 高

如果 \includegraphics 之前引用的是 fig1_pipeline.pdf，改为 inline TikZ。如果实在写不出好的 TikZ，跳过 fig1（删除引用），投稿时不含 pipeline 图也可以。不要再 spawn worker 做这个。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ccccb0f-0ee8-4c6a-8d8c-3599a7795c26",
  "isSidechain": false,
  "promptId": "febadbac-8aba-4e81-aed3-8415bae4e429",
  "type": "user",
  "uuid": "d561152f-581c-4deb-a87d-004709edc20f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Tool call

_source line 1831 · 2026-05-17T19:20:59.109Z_

<details open><summary>🔧 Tool call — Read · `toolu_014eZnxWgKHWcSW28FrQ1s3D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex",
  "offset": 1,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d561152f-581c-4deb-a87d-004709edc20f",
  "isSidechain": false,
  "requestId": "req_011Cb8gbLktqHP9rvqZEvFod",
  "type": "assistant",
  "uuid": "b83d665d-019e-4fbf-a92c-a7713a9090e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RRtt9VcMLDyyspmn3qhh2i",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 387,
      "cache_read_input_tokens": 148472,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 387,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 124,
          "cache_read_input_tokens": 148472,
          "cache_creation_input_tokens": 387,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 387
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

_source line 1832 · 2026-05-17T19:20:59.129Z_

<details><summary>↩ Tool result · `toolu_014eZnxWgKHWcSW28FrQ1s3D`</summary>

```text
1	\section{Method: The SICA Pipeline}
2	\label{sec:method}
3	
4	This section describes Symbolic Invariant Consensus Aggregation (SICA), which extracts first-order logic (FOL) constraints from multiple reasoning traces produced by a single LLM, formulates a weighted partial MAX-SAT problem, and selects the answer best supported by the satisfiable subset.
5	
6	\subsection{Overview}
7	\label{sec:method-overview}
8	
9	Given a question $q$, SICA proceeds in four stages. First, an LLM generates $K$ independent reasoning traces $\{t_1, \ldots, t_K\}$ by sampling at temperature $T$; each trace $t_i$ yields a candidate answer $a_i$. Second, the same LLM extracts a set of structured FOL constraints $C_i$ from each trace $t_i$. Third, constraints are deduplicated across traces by syntactic equivalence, and each unique constraint receives a weight equal to the number of traces that produced it. Fourth, the deduplicated constraint pool is formulated as a weighted partial MAX-SAT instance and solved by Z3 \cite{demoura2008z3}. Each candidate answer is scored by the total weight of satisfied constraints, and the highest-scoring answer is selected.
10	
11	Self-Consistency (SC) uses only the first stage: it selects $a^* = \arg\max_{a} \sum_{i=1}^{K} \mathbf{1}[a_i = a]$. SICA's additional signal comes from constraint satisfaction structure. Whether this signal provides discriminative power beyond vote counting is the central empirical question.
12	
13	\begin{figure*}[t]
14	\centering
15	\includegraphics[width=\textwidth]{fig1_pipeline.pdf}
16	\caption{The SICA pipeline compared with Self-Consistency (SC). Both methods sample $K$ reasoning traces at temperature $T$. SC selects the majority answer (left). SICA additionally extracts FOL constraints from each trace, deduplicates them, and solves a weighted partial MAX-SAT instance via Z3 to score candidate answers (right). The oracle variant (dashed) replaces self-extracted constraints with gold FOL annotations.}
17	\label{fig:pipeline}
18	\end{figure*}
19	
20	\subsection{Constraint Extraction}
21	\label{sec:constraint-extraction}
22	
23	For each trace $t_i$, the same LLM that generated $t_i$ is prompted to extract structured FOL constraints. While we prompt for FOL-style formalizations, the extracted constraints are predominantly propositional ground clauses without quantifiers, reflecting instruction-scale model capabilities. The extraction prompt requests JSON output containing the constraint type, a human-readable expression, and a Z3-compatible formula string. Each constraint $c$ is associated with its source trace $t_i$ and the answer $a_i$ that trace produced. The full prompt template is in Appendix~\ref{app:prompts}.
24	
25	We define the \emph{extraction rate} as the fraction of traces yielding at least one parseable constraint. Traces with no valid constraints are excluded from MAX-SAT but still contribute answers to the candidate pool. Deduplication proceeds by syntactic equivalence: each unique constraint $c_m$ receives weight $w_m$ equal to the number of distinct traces that produced it.
26	
27	\subsection{Weighted Partial MAX-SAT Formulation}
28	\label{sec:maxsat}
29	
30	Let $\mathcal{A}(q) = \{a : a \in \{a_1, \ldots, a_K\}\}$ denote the set of distinct candidate answers for question $q$, and let $\mathcal{C} = \{c_1, \ldots, c_M\}$ denote the deduplicated constraint pool with weights $\{w_1, \ldots, w_M\}$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b83d665d-019e-4fbf-a92c-a7713a9090e9",
  "isSidechain": false,
  "promptId": "febadbac-8aba-4e81-aed3-8415bae4e429",
  "type": "user",
  "uuid": "52341fa9-3777-4e71-8208-a12ac6964886",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex",
      "content": "\\section{Method: The SICA Pipeline}\n\\label{sec:method}\n\nThis section describes Symbolic Invariant Consensus Aggregation (SICA), which extracts first-order logic (FOL) constraints from multiple reasoning traces produced by a single LLM, formulates a weighted partial MAX-SAT problem, and selects the answer best supported by the satisfiable subset.\n\n\\subsection{Overview}\n\\label{sec:method-overview}\n\nGiven a question $q$, SICA proceeds in four stages. First, an LLM generates $K$ independent reasoning traces $\\{t_1, \\ldots, t_K\\}$ by sampling at temperature $T$; each trace $t_i$ yields a candidate answer $a_i$. Second, the same LLM extracts a set of structured FOL constraints $C_i$ from each trace $t_i$. Third, constraints are deduplicated across traces by syntactic equivalence, and each unique constraint receives a weight equal to the number of traces that produced it. Fourth, the deduplicated constraint pool is formulated as a weighted partial MAX-SAT instance and solved by Z3 \\cite{demoura2008z3}. Each candidate answer is scored by the total weight of satisfied constraints, and the highest-scoring answer is selected.\n\nSelf-Consistency (SC) uses only the first stage: it selects $a^* = \\arg\\max_{a} \\sum_{i=1}^{K} \\mathbf{1}[a_i = a]$. SICA's additional signal comes from constraint satisfaction structure. Whether this signal provides discriminative power beyond vote counting is the central empirical question.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_pipeline.pdf}\n\\caption{The SICA pipeline compared with Self-Consistency (SC). Both methods sample $K$ reasoning traces at temperature $T$. SC selects the majority answer (left). SICA additionally extracts FOL constraints from each trace, deduplicates them, and solves a weighted partial MAX-SAT instance via Z3 to score candidate answers (right). The oracle variant (dashed) replaces self-extracted constraints with gold FOL annotations.}\n\\label{fig:pipeline}\n\\end{figure*}\n\n\\subsection{Constraint Extraction}\n\\label{sec:constraint-extraction}\n\nFor each trace $t_i$, the same LLM that generated $t_i$ is prompted to extract structured FOL constraints. While we prompt for FOL-style formalizations, the extracted constraints are predominantly propositional ground clauses without quantifiers, reflecting instruction-scale model capabilities. The extraction prompt requests JSON output containing the constraint type, a human-readable expression, and a Z3-compatible formula string. Each constraint $c$ is associated with its source trace $t_i$ and the answer $a_i$ that trace produced. The full prompt template is in Appendix~\\ref{app:prompts}.\n\nWe define the \\emph{extraction rate} as the fraction of traces yielding at least one parseable constraint. Traces with no valid constraints are excluded from MAX-SAT but still contribute answers to the candidate pool. Deduplication proceeds by syntactic equivalence: each unique constraint $c_m$ receives weight $w_m$ equal to the number of distinct traces that produced it.\n\n\\subsection{Weighted Partial MAX-SAT Formulation}\n\\label{sec:maxsat}\n\nLet $\\mathcal{A}(q) = \\{a : a \\in \\{a_1, \\ldots, a_K\\}\\}$ denote the set of distinct candidate answers for question $q$, and let $\\mathcal{C} = \\{c_1, \\ldots, c_M\\}$ denote the deduplicated constraint pool with weights $\\{w_1, \\ldots, w_M\\}$.",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 69
    }
  },
  "sourceToolAssistantUUID": "b83d665d-019e-4fbf-a92c-a7713a9090e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Assistant

_source line 1833 · 2026-05-17T19:21:02.803Z_

<details><summary>Logged reasoning block</summary>

```text
I need to replace the `\begin{figure*}` with `\includegraphics{fig1_pipeline.pdf}` with an inline TikZ figure. Let me also check if tikz is already loaded.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52341fa9-3777-4e71-8208-a12ac6964886",
  "isSidechain": false,
  "requestId": "req_011Cb8gbaC3BawhjTDkJrfDc",
  "type": "assistant",
  "uuid": "ffa4642c-8451-4b1c-bf70-a6407030de2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Brweyshi3vYVtjpLm7KXM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1114,
      "cache_read_input_tokens": 148859,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 148859,
          "cache_creation_input_tokens": 1114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1114
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

_source line 1834 · 2026-05-17T19:21:03.341Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01B7yVJK6fEZ4ehdSGeuMGnA`</summary>

```json
{
  "command": "grep -n \"tikz\" /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
  "description": "Check if tikz is loaded"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffa4642c-8451-4b1c-bf70-a6407030de2b",
  "isSidechain": false,
  "requestId": "req_011Cb8gbaC3BawhjTDkJrfDc",
  "type": "assistant",
  "uuid": "b0b8db90-a74a-46d1-8fa7-0ca7dbdd9edc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Brweyshi3vYVtjpLm7KXM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1114,
      "cache_read_input_tokens": 148859,
      "output_tokens": 180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 180,
          "cache_read_input_tokens": 148859,
          "cache_creation_input_tokens": 1114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1114
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

_source line 1835 · 2026-05-17T19:21:03.510Z_

<details><summary>↩ Tool result · `toolu_01B7yVJK6fEZ4ehdSGeuMGnA`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0b8db90-a74a-46d1-8fa7-0ca7dbdd9edc",
  "isSidechain": false,
  "promptId": "febadbac-8aba-4e81-aed3-8415bae4e429",
  "type": "user",
  "uuid": "0649a839-c710-47f4-bfde-b4814a798220",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b0b8db90-a74a-46d1-8fa7-0ca7dbdd9edc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Assistant

_source line 1836 · 2026-05-17T19:21:06.785Z_

Need to add tikz. Let me add it and replace the figure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0649a839-c710-47f4-bfde-b4814a798220",
  "isSidechain": false,
  "requestId": "req_011Cb8gbtDVuhYcJhh2BCrh9",
  "type": "assistant",
  "uuid": "649a1abc-fce1-47b6-a7a6-ac60cf940ea1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYi4vpbS6uaJspexLTQUia",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 198,
      "cache_read_input_tokens": 149973,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 149973,
          "cache_creation_input_tokens": 198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 198
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

_source line 1837 · 2026-05-17T19:21:08.297Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01QVpLz6KnEWzQvxHq2977FG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
  "old_string": "\\usepackage{subcaption}",
  "new_string": "\\usepackage{subcaption}\n\\usepackage{tikz}\n\\usetikzlibrary{arrows.meta,positioning,calc}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "649a1abc-fce1-47b6-a7a6-ac60cf940ea1",
  "isSidechain": false,
  "requestId": "req_011Cb8gbtDVuhYcJhh2BCrh9",
  "type": "assistant",
  "uuid": "df916462-e37c-4ec7-a58d-cb91082d0d6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYi4vpbS6uaJspexLTQUia",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 198,
      "cache_read_input_tokens": 149973,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 198,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 149973,
          "cache_creation_input_tokens": 198,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 198
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

_source line 1838 · 2026-05-17T19:21:08.300Z_

<details><summary>↩ Tool result · reported error · `toolu_01QVpLz6KnEWzQvxHq2977FG`</summary>

```text
&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df916462-e37c-4ec7-a58d-cb91082d0d6b",
  "isSidechain": false,
  "promptId": "febadbac-8aba-4e81-aed3-8415bae4e429",
  "type": "user",
  "uuid": "091f4303-f45d-48ea-809b-acb42104219d",
  "toolUseResult": "Error: File has not been read yet. Read it first before writing to it.",
  "sourceToolAssistantUUID": "df916462-e37c-4ec7-a58d-cb91082d0d6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Tool call

_source line 1839 · 2026-05-17T19:21:11.273Z_

<details open><summary>🔧 Tool call — Read · `toolu_018Fdxhur7E4nHoJDUL2mzP4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "091f4303-f45d-48ea-809b-acb42104219d",
  "isSidechain": false,
  "requestId": "req_011Cb8gcF19siHdc476k3EhZ",
  "type": "assistant",
  "uuid": "20092d83-e5b3-4151-9b8f-813d06de437c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZ5mvm98rgfvDKPyKdXeeT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 249,
      "cache_read_input_tokens": 150171,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 106,
          "cache_read_input_tokens": 150171,
          "cache_creation_input_tokens": 249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 249
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

_source line 1840 · 2026-05-17T19:21:11.283Z_

<details><summary>↩ Tool result · `toolu_018Fdxhur7E4nHoJDUL2mzP4`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % removed: not available in this TeX distribution
9	\usepackage{graphicx}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{booktabs}
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{listings}
17	\usepackage{hyperref}
18	\usepackage{cleveref}
19	
20	\lstset{
21	  basicstyle=\small\ttfamily,
22	  breaklines=true,
23	  frame=single,
24	  xleftmargin=1em,
25	  xrightmargin=1em,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "20092d83-e5b3-4151-9b8f-813d06de437c",
  "isSidechain": false,
  "promptId": "febadbac-8aba-4e81-aed3-8415bae4e429",
  "type": "user",
  "uuid": "092ad5ac-0bd4-49e8-b69d-e99275e12760",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n% \\usepackage{inconsolata} % removed: not available in this TeX distribution\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{listings}\n\\usepackage{hyperref}\n\\usepackage{cleveref}\n\n\\lstset{\n  basicstyle=\\small\\ttfamily,\n  breaklines=true,\n  frame=single,\n  xleftmargin=1em,\n  xrightmargin=1em,",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 62
    }
  },
  "sourceToolAssistantUUID": "20092d83-e5b3-4151-9b8f-813d06de437c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Tool call

_source line 1841 · 2026-05-17T19:21:15.564Z_

<details open><summary>🔧 Tool call — Edit · `toolu_017fU9vEM1yZxoaCXkaFeVoX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
  "old_string": "\\usepackage{subcaption}\n\\usepackage{listings}",
  "new_string": "\\usepackage{subcaption}\n\\usepackage{tikz}\n\\usetikzlibrary{arrows.meta,positioning,calc}\n\\usepackage{listings}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "092ad5ac-0bd4-49e8-b69d-e99275e12760",
  "isSidechain": false,
  "requestId": "req_011Cb8gcTSGDqGTg464xyLTU",
  "type": "assistant",
  "uuid": "1123e492-e1e1-4786-b2f2-8505ea54e82b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Gw64t8YptR8cUK2Q8YGAt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 150420,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 150420,
          "cache_creation_input_tokens": 410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 410
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

_source line 1842 · 2026-05-17T19:21:15.582Z_

<details><summary>↩ Tool result · `toolu_017fU9vEM1yZxoaCXkaFeVoX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1123e492-e1e1-4786-b2f2-8505ea54e82b",
  "isSidechain": false,
  "promptId": "febadbac-8aba-4e81-aed3-8415bae4e429",
  "type": "user",
  "uuid": "a8615bb4-5087-4a17-9003-5f0ef4859338",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.tex",
    "oldString": "\\usepackage{subcaption}\n\\usepackage{listings}",
    "newString": "\\usepackage{subcaption}\n\\usepackage{tikz}\n\\usetikzlibrary{arrows.meta,positioning,calc}\n\\usepackage{listings}",
    "originalFile": "\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n% \\usepackage{inconsolata} % removed: not available in this TeX distribution\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{listings}\n\\usepackage{hyperref}\n\\usepackage{cleveref}\n\n\\lstset{\n  basicstyle=\\small\\ttfamily,\n  breaklines=true,\n  frame=single,\n  xleftmargin=1em,\n  xrightmargin=1em,\n  aboveskip=0.5em,\n  belowskip=0.5em,\n}\n\n\\graphicspath{{../figures/paper/}{figures/}}\n\n\\title{The Capability Trap: Why Self-Extracted Constraints\\\\Cannot Improve LLM Majority Voting}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{method}\n\n\\input{experiments}\n\n\\input{discussion}\n\n\\input{conclusion}\n\n\\section*{Limitations}\n\\input{limitations_content}\n\n\\bibliography{references}\n\n\\appendix\n\\input{appendix}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 13,
        "oldLines": 6,
        "newStart": 13,
        "newLines": 8,
        "lines": [
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          " \\usepackage{subcaption}",
          "+\\usepackage{tikz}",
          "+\\usetikzlibrary{arrows.meta,positioning,calc}",
          " \\usepackage{listings}",
          " \\usepackage{hyperref}",
          " \\usepackage{cleveref}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "1123e492-e1e1-4786-b2f2-8505ea54e82b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Assistant

_source line 1843 · 2026-05-17T19:21:18.247Z_

Now replace the figure* block with inline TikZ.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a8615bb4-5087-4a17-9003-5f0ef4859338",
  "isSidechain": false,
  "requestId": "req_011Cb8gcn2TfuntzrSDHSkYv",
  "type": "assistant",
  "uuid": "91ac1632-4b63-4927-b62a-de070d1abe62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013n5Knb2mYojwmkinofi9Sj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 150830,
      "output_tokens": 928,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 928,
          "cache_read_input_tokens": 150830,
          "cache_creation_input_tokens": 258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 258
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

_source line 1844 · 2026-05-17T19:21:29.500Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01GjzinyvhgojLgJVQ8LEMvb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex",
  "old_string": "\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_pipeline.pdf}\n\\caption{The SICA pipeline compared with Self-Consistency (SC). Both methods sample $K$ reasoning traces at temperature $T$. SC selects the majority answer (left). SICA additionally extracts FOL constraints from each trace, deduplicates them, and solves a weighted partial MAX-SAT instance via Z3 to score candidate answers (right). The oracle variant (dashed) replaces self-extracted constraints with gold FOL annotations.}\n\\label{fig:pipeline}\n\\end{figure*}",
  "new_string": "\\begin{figure}[t]\n\\centering\n\\small\n\\begin{tikzpicture}[\n    node distance=0.4cm and 0.35cm,\n    box/.style={draw, rounded corners=2pt, minimum height=0.6cm,\n                text width=1.6cm, align=center, font=\\scriptsize},\n    arr/.style={-{Stealth[length=4pt]}, thick},\n    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},\n    lbl/.style={font=\\tiny, text=gray!70!black},\n]\n\\node[box] (q) {Question $q$};\n\\node[box, right=of q] (sample) {Sample $K$\\\\traces};\n\\node[box, right=of sample] (extract) {Extract FOL\\\\constraints};\n\\node[box, right=of extract] (dedup) {Dedup.\\ +\\\\weight};\n\\node[box, right=of dedup] (maxsat) {MAX-SAT\\\\(Z3)};\n\n\\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};\n\\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\\\vote};\n\n\\draw[arr] (q) -- (sample);\n\\draw[arr] (sample) -- (extract);\n\\draw[arr] (extract) -- (dedup);\n\\draw[arr] (dedup) -- (maxsat);\n\\draw[arr] (maxsat) -- (ans);\n\\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);\n\n\\node[lbl, above=0.01cm of extract] {same LLM};\n\\node[lbl, above=0.01cm of maxsat] {SICA};\n\n\\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};\n\\end{tikzpicture}\n\\caption{The SICA pipeline. Both SC and SICA sample $K$ traces. SC selects the majority answer directly. SICA extracts FOL constraints from each trace, deduplicates, and solves a MAX-SAT instance via Z3. Dashed arrow: the oracle variant substitutes gold FOL annotations.}\n\\label{fig:pipeline}\n\\end{figure}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91ac1632-4b63-4927-b62a-de070d1abe62",
  "isSidechain": false,
  "requestId": "req_011Cb8gcn2TfuntzrSDHSkYv",
  "type": "assistant",
  "uuid": "a2c8a9ae-e4c4-40af-977b-e32f6750d823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013n5Knb2mYojwmkinofi9Sj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 258,
      "cache_read_input_tokens": 150830,
      "output_tokens": 928,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 928,
          "cache_read_input_tokens": 150830,
          "cache_creation_input_tokens": 258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 258
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

_source line 1845 · 2026-05-17T19:21:29.515Z_

<details><summary>↩ Tool result · `toolu_01GjzinyvhgojLgJVQ8LEMvb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2c8a9ae-e4c4-40af-977b-e32f6750d823",
  "isSidechain": false,
  "promptId": "febadbac-8aba-4e81-aed3-8415bae4e429",
  "type": "user",
  "uuid": "533a0a4b-b556-4634-9dbb-a6ea077130ff",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/method.tex",
    "oldString": "\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_pipeline.pdf}\n\\caption{The SICA pipeline compared with Self-Consistency (SC). Both methods sample $K$ reasoning traces at temperature $T$. SC selects the majority answer (left). SICA additionally extracts FOL constraints from each trace, deduplicates them, and solves a weighted partial MAX-SAT instance via Z3 to score candidate answers (right). The oracle variant (dashed) replaces self-extracted constraints with gold FOL annotations.}\n\\label{fig:pipeline}\n\\end{figure*}",
    "newString": "\\begin{figure}[t]\n\\centering\n\\small\n\\begin{tikzpicture}[\n    node distance=0.4cm and 0.35cm,\n    box/.style={draw, rounded corners=2pt, minimum height=0.6cm,\n                text width=1.6cm, align=center, font=\\scriptsize},\n    arr/.style={-{Stealth[length=4pt]}, thick},\n    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},\n    lbl/.style={font=\\tiny, text=gray!70!black},\n]\n\\node[box] (q) {Question $q$};\n\\node[box, right=of q] (sample) {Sample $K$\\\\traces};\n\\node[box, right=of sample] (extract) {Extract FOL\\\\constraints};\n\\node[box, right=of extract] (dedup) {Dedup.\\ +\\\\weight};\n\\node[box, right=of dedup] (maxsat) {MAX-SAT\\\\(Z3)};\n\n\\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};\n\\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\\\vote};\n\n\\draw[arr] (q) -- (sample);\n\\draw[arr] (sample) -- (extract);\n\\draw[arr] (extract) -- (dedup);\n\\draw[arr] (dedup) -- (maxsat);\n\\draw[arr] (maxsat) -- (ans);\n\\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);\n\n\\node[lbl, above=0.01cm of extract] {same LLM};\n\\node[lbl, above=0.01cm of maxsat] {SICA};\n\n\\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};\n\\end{tikzpicture}\n\\caption{The SICA pipeline. Both SC and SICA sample $K$ traces. SC selects the majority answer directly. SICA extracts FOL constraints from each trace, deduplicates, and solves a MAX-SAT instance via Z3. Dashed arrow: the oracle variant substitutes gold FOL annotations.}\n\\label{fig:pipeline}\n\\end{figure}",
    "originalFile": "\\section{Method: The SICA Pipeline}\n\\label{sec:method}\n\nThis section describes Symbolic Invariant Consensus Aggregation (SICA), which extracts first-order logic (FOL) constraints from multiple reasoning traces produced by a single LLM, formulates a weighted partial MAX-SAT problem, and selects the answer best supported by the satisfiable subset.\n\n\\subsection{Overview}\n\\label{sec:method-overview}\n\nGiven a question $q$, SICA proceeds in four stages. First, an LLM generates $K$ independent reasoning traces $\\{t_1, \\ldots, t_K\\}$ by sampling at temperature $T$; each trace $t_i$ yields a candidate answer $a_i$. Second, the same LLM extracts a set of structured FOL constraints $C_i$ from each trace $t_i$. Third, constraints are deduplicated across traces by syntactic equivalence, and each unique constraint receives a weight equal to the number of traces that produced it. Fourth, the deduplicated constraint pool is formulated as a weighted partial MAX-SAT instance and solved by Z3 \\cite{demoura2008z3}. Each candidate answer is scored by the total weight of satisfied constraints, and the highest-scoring answer is selected.\n\nSelf-Consistency (SC) uses only the first stage: it selects $a^* = \\arg\\max_{a} \\sum_{i=1}^{K} \\mathbf{1}[a_i = a]$. SICA's additional signal comes from constraint satisfaction structure. Whether this signal provides discriminative power beyond vote counting is the central empirical question.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig1_pipeline.pdf}\n\\caption{The SICA pipeline compared with Self-Consistency (SC). Both methods sample $K$ reasoning traces at temperature $T$. SC selects the majority answer (left). SICA additionally extracts FOL constraints from each trace, deduplicates them, and solves a weighted partial MAX-SAT instance via Z3 to score candidate answers (right). The oracle variant (dashed) replaces self-extracted constraints with gold FOL annotations.}\n\\label{fig:pipeline}\n\\end{figure*}\n\n\\subsection{Constraint Extraction}\n\\label{sec:constraint-extraction}\n\nFor each trace $t_i$, the same LLM that generated $t_i$ is prompted to extract structured FOL constraints. While we prompt for FOL-style formalizations, the extracted constraints are predominantly propositional ground clauses without quantifiers, reflecting instruction-scale model capabilities. The extraction prompt requests JSON output containing the constraint type, a human-readable expression, and a Z3-compatible formula string. Each constraint $c$ is associated with its source trace $t_i$ and the answer $a_i$ that trace produced. The full prompt template is in Appendix~\\ref{app:prompts}.\n\nWe define the \\emph{extraction rate} as the fraction of traces yielding at least one parseable constraint. Traces with no valid constraints are excluded from MAX-SAT but still contribute answers to the candidate pool. Deduplication proceeds by syntactic equivalence: each unique constraint $c_m$ receives weight $w_m$ equal to the number of distinct traces that produced it.\n\n\\subsection{Weighted Partial MAX-SAT Formulation}\n\\label{sec:maxsat}\n\nLet $\\mathcal{A}(q) = \\{a : a \\in \\{a_1, \\ldots, a_K\\}\\}$ denote the set of distinct candidate answers for question $q$, and let $\\mathcal{C} = \\{c_1, \\ldots, c_M\\}$ denote the deduplicated constraint pool with weights $\\{w_1, \\ldots, w_M\\}$.\n\n\\paragraph{MAX-SAT instance.} Each unique constraint $c_m$ serves as a soft clause with weight $w_m$. The objective is to find the largest-weight satisfiable subset:\n\\begin{equation}\n\\label{eq:maxsat}\n\\mathcal{C}^* = \\arg\\max_{\\mathcal{S} \\subseteq \\mathcal{C}} \\sum_{c \\in \\mathcal{S}} w_c \\quad \\text{s.t.} \\quad \\mathcal{S} \\text{ is satisfiable.}\n\\end{equation}\nZ3's optimization engine solves this with a 10-second per-problem timeout.\n\n\\paragraph{Answer scoring.} Each candidate answer $a \\in \\mathcal{A}(q)$ is scored by:\n\\begin{equation}\n\\label{eq:score}\n\\text{score}(a) = \\sum_{c \\in \\mathcal{C}^*} w_c \\cdot \\sigma(c, a),\n\\end{equation}\nwhere $\\sigma(c, a) \\in \\{0, 1\\}$ is determined by Z3: $\\sigma(c, a) = 1$ if constraint $c$ is satisfiable under the assignment implied by answer $a$. Each constraint is evaluated against every candidate, so a constraint from one trace can support or exclude answers from other traces. The selected answer is $a^* = \\arg\\max_{a \\in \\mathcal{A}} \\text{score}(a)$.\n\n\\paragraph{Degeneration under non-discriminative constraints.}\nIn practice, self-extracted constraints are tightly coupled to their source answer: $c_m$ derived from trace $t_i$ typically entails $a_i$ ($\\sigma(c_m, a_i) \\approx 1$). When constraints lack discriminative power across candidates, the score function degenerates:\n\\begin{equation}\n\\label{eq:degenerate}\n\\text{score}(a) \\approx \\sum_{\\substack{c \\in \\mathcal{C}^* \\\\ \\text{source}(c) \\to a}} w_c,\n\\end{equation}\nwhich reduces to a weighted count of traces supporting $a$, equivalent to majority voting when weights are uniform. The ablation in \\S\\ref{sec:ablation} confirms this empirically: MAX-SAT, count-only, and random-weight baselines produce nearly identical accuracy.\n\n\\subsection{The $C_0$ Diagnostic}\n\\label{sec:c0}\n\nWe define the multi-candidate rate $C_0$ as the fraction of questions for which $K$ sampled traces produce more than one distinct answer:\n\\begin{equation}\n\\label{eq:c0}\nC_0 = \\frac{|\\{q \\in \\mathcal{Q} : |\\mathcal{A}(q)| > 1\\}|}{|\\mathcal{Q}|}.\n\\end{equation}\n\n$C_0$ is a zero-cost diagnostic computable before any constraint extraction. When $C_0$ falls below 5\\%, nearly all questions are answered unanimously, and SICA produces the same output as SC by construction. High $C_0$ does not guarantee improvement, as it merely ensures disagreement exists without ensuring constraints can resolve it. $C_0$ serves as a necessary-condition screening criterion for practitioners considering symbolic aggregation.\n\n\\subsection{Scope and Limitations}\n\\label{sec:scope}\n\nSICA as evaluated here uses \\emph{same-model self-extraction}: the same LLM generates traces and extracts constraints. This isolates whether an LLM's own reasoning can be usefully formalized for aggregation. Our evaluation does not cover trained extractors, external provers, or cross-model setups. Published methods achieving positive results through different mechanisms \\citep{xu2026dylos, li2025aristotle, wang2025fover, luo2025logicagent} are complementary to our findings. An oracle variant (\\S\\ref{sec:oracle}) disentangles extraction quality from aggregation effectiveness.\n",
    "structuredPatch": [
      {
        "oldStart": 10,
        "oldLines": 12,
        "newStart": 10,
        "newLines": 41,
        "lines": [
          " ",
          " Self-Consistency (SC) uses only the first stage: it selects $a^* = \\arg\\max_{a} \\sum_{i=1}^{K} \\mathbf{1}[a_i = a]$. SICA's additional signal comes from constraint satisfaction structure. Whether this signal provides discriminative power beyond vote counting is the central empirical question.",
          " ",
          "-\\begin{figure*}[t]",
          "+\\begin{figure}[t]",
          " \\centering",
          "-\\includegraphics[width=\\textwidth]{fig1_pipeline.pdf}",
          "-\\caption{The SICA pipeline compared with Self-Consistency (SC). Both methods sample $K$ reasoning traces at temperature $T$. SC selects the majority answer (left). SICA additionally extracts FOL constraints from each trace, deduplicates them, and solves a weighted partial MAX-SAT instance via Z3 to score candidate answers (right). The oracle variant (dashed) replaces self-extracted constraints with gold FOL annotations.}",
          "+\\small",
          "+\\begin{tikzpicture}[",
          "+    node distance=0.4cm and 0.35cm,",
          "+    box/.style={draw, rounded corners=2pt, minimum height=0.6cm,",
          "+                text width=1.6cm, align=center, font=\\scriptsize},",
          "+    arr/.style={-{Stealth[length=4pt]}, thick},",
          "+    darr/.style={-{Stealth[length=4pt]}, thick, densely dashed},",
          "+    lbl/.style={font=\\tiny, text=gray!70!black},",
          "+]",
          "+\\node[box] (q) {Question $q$};",
          "+\\node[box, right=of q] (sample) {Sample $K$\\\\traces};",
          "+\\node[box, right=of sample] (extract) {Extract FOL\\\\constraints};",
          "+\\node[box, right=of extract] (dedup) {Dedup.\\ +\\\\weight};",
          "+\\node[box, right=of dedup] (maxsat) {MAX-SAT\\\\(Z3)};",
          "+",
          "+\\node[box, below=0.7cm of maxsat, fill=gray!12] (ans) {Answer $a^*$};",
          "+\\node[box, below=0.7cm of sample, fill=gray!12] (sc) {Majority\\\\vote};",
          "+",
          "+\\draw[arr] (q) -- (sample);",
          "+\\draw[arr] (sample) -- (extract);",
          "+\\draw[arr] (extract) -- (dedup);",
          "+\\draw[arr] (dedup) -- (maxsat);",
          "+\\draw[arr] (maxsat) -- (ans);",
          "+\\draw[arr] (sample) -- node[lbl, right, yshift=0pt] {SC} (sc);",
          "+",
          "+\\node[lbl, above=0.01cm of extract] {same LLM};",
          "+\\node[lbl, above=0.01cm of maxsat] {SICA};",
          "+",
          "+\\draw[darr, gray!60] ([xshift=-0.1cm]dedup.south) -- ++(0,-0.35) node[lbl, below, yshift=-0.05cm] {oracle: gold FOL};",
          "+\\end{tikzpicture}",
          "+\\caption{The SICA pipeline. Both SC and SICA sample $K$ traces. SC selects the majority answer directly. SICA extracts FOL constraints from each trace, deduplicates, and solves a MAX-SAT instance via Z3. Dashed arrow: the oracle variant substitutes gold FOL annotations.}",
          " \\label{fig:pipeline}",
          "-\\end{figure*}",
          "+\\end{figure}",
          " ",
          " \\subsection{Constraint Extraction}",
          " \\label{sec:constraint-extraction}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "a2c8a9ae-e4c4-40af-977b-e32f6750d823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Runtime record

_source line 1846_

````json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] **fig1 pipeline 图 — 最简方案**  之前的 Worker 卡了 100 分钟。换简单方案：  **直接用 TikZ 在 LaTeX 中画 pipeline 图**，不用 Python/matplotlib。SICA pipeline 就是一个简单流程图：  ``` Question q → Sample K traces (T=0.7) → Extr…",
  "leafUuid": "533a0a4b-b556-4634-9dbb-a6ea077130ff",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746"
}
````

---


### Runtime record

_source line 1847_

```json
{
  "type": "ai-title",
  "aiTitle": "Retrieve and process SSH check worker results",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746"
}
```

---


### Tool call

_source line 1848 · 2026-05-17T19:21:34.062Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0141Ts96KUyVKqC93Rf7REY1`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Output written|Error|Undefined\" | head -10",
  "description": "Compile with TikZ figure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "533a0a4b-b556-4634-9dbb-a6ea077130ff",
  "isSidechain": false,
  "requestId": "req_011Cb8gdoR5Esa6ekG6r6ie1",
  "type": "assistant",
  "uuid": "ad61d3f1-067b-485f-8b84-1899f9741055",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LJb5WD8f4f6egH44Zmcw9q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 983,
      "cache_read_input_tokens": 151088,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 151088,
          "cache_creation_input_tokens": 983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 983
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

_source line 1849 · 2026-05-17T19:21:35.578Z_

<details><summary>↩ Tool result · `toolu_0141Ts96KUyVKqC93Rf7REY1`</summary>

```text
Output written on main.pdf (12 pages, 358615 bytes).
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad61d3f1-067b-485f-8b84-1899f9741055",
  "isSidechain": false,
  "promptId": "febadbac-8aba-4e81-aed3-8415bae4e429",
  "type": "user",
  "uuid": "e5128d67-7801-4b9a-8852-4b2c71c428fa",
  "toolUseResult": {
    "stdout": "Output written on main.pdf (12 pages, 358615 bytes).",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ad61d3f1-067b-485f-8b84-1899f9741055",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Runtime record

_source line 1850 · 2026-05-17T19:21:35.585Z_

```json
{
  "parentUuid": "e5128d67-7801-4b9a-8852-4b2c71c428fa",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3f1009ef-1674-40be-8753-1d65457f0d0b",
  "timestamp": "2026-05-17T19:21:35.585Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

---


### Assistant

_source line 1851 · 2026-05-17T19:21:39.319Z_

Compiles. Let me visually check the figure renders correctly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f1009ef-1674-40be-8753-1d65457f0d0b",
  "isSidechain": false,
  "requestId": "req_011Cb8geFPXKBQY7Ssod8ZB2",
  "type": "assistant",
  "uuid": "38a221d8-d447-4bed-be83-338692ceed42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0142WX1PdqdNn5MQUiX9sPMk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 152071,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 152071,
          "cache_creation_input_tokens": 326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 326
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

_source line 1852 · 2026-05-17T19:21:39.981Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01T5vPdVAqYiPRf4eTzi5PFP`</summary>

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
  "parentUuid": "38a221d8-d447-4bed-be83-338692ceed42",
  "isSidechain": false,
  "requestId": "req_011Cb8geFPXKBQY7Ssod8ZB2",
  "type": "assistant",
  "uuid": "48dd4cc6-76fd-4229-96f8-0bf8bd36c4c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0142WX1PdqdNn5MQUiX9sPMk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 152071,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 326,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 102,
          "cache_read_input_tokens": 152071,
          "cache_creation_input_tokens": 326,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 326
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

_source line 1853 · 2026-05-17T19:21:39.987Z_

<details><summary>↩ Tool result · `toolu_01T5vPdVAqYiPRf4eTzi5PFP`</summary>

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
  "parentUuid": "48dd4cc6-76fd-4229-96f8-0bf8bd36c4c9",
  "isSidechain": false,
  "promptId": "febadbac-8aba-4e81-aed3-8415bae4e429",
  "type": "user",
  "uuid": "5c51b63e-7108-4497-a694-66551a9d0b9a",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__pdf_to_images"
    ],
    "query": "select:mcp__agent-ml-research__pdf_to_images",
    "total_deferred_tools": 80
  },
  "sourceToolAssistantUUID": "48dd4cc6-76fd-4229-96f8-0bf8bd36c4c9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson"
}
```

</details>

---


### Tool call

_source line 1854 · 2026-05-17T19:21:43.360Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images · `toolu_01GE97MNKhEmf7ZMVYDcz5rg`</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/main.pdf",
  "pages": "4",
  "dpi": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c51b63e-7108-4497-a694-66551a9d0b9a",
  "isSidechain": false,
  "requestId": "req_011Cb8geaUUqwPysFU6Q2xLM",
  "type": "assistant",
  "uuid": "865526fa-ab22-4061-a240-50463e2ba7ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/agent_47e5a40d",
  "sessionId": "f2e14b4e-afcd-4be8-b19d-82d2efd6e746",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "parallel-exploring-wilkinson",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019nZXM1TA6y4WHLHwdF8GFF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 477,
      "cache_read_input_tokens": 152397,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 477,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 138,
          "cache_read_input_tokens": 152397,
          "cache_creation_input_tokens": 477,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 477
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

_source line 1855 · 2026-05-17T19:21:44.150Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_01GE97MNKhEmf7ZMVYDcz5rg`&lt;/summary>

```text
Error: result (913,097 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-agent-47e5a40d/f2e14b4e-afcd-4be8-b19d-82d2efd6e746/tool-results/mcp-agent-ml-research-pdf_to_images-1779045704134.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-agent-47e5a40d/f2e14b4e-afcd-4be8-b19d-82d2efd6e746/tool-results/mcp-agent-ml-research-pdf_to_images-1779045704134.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "865526fa-ab22-4061-a240-50463e2ba7ef",
  "isSidechain": false,
  "promptId": "febadbac-8aba-4e81-aed3-8415bae4e429",
  "type": "user",
  "uuid": "d0511ade-f316-4e68-aca1-a95fb5935ce4",
  "toolUseResult": "Error: result (913,097 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-agent-47e5a40d/f2e14b4e-afcd-4be8-b19d-82d2efd6e746/tool-results/mcp-agent-ml-research-pdf_to_images-1779045704134.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-3-projects-symb-invariant-consensus--claude-sessions-agent-47e5a40d/f2e14b4e-afcd-4be8-b19d-82d2efd6e746/tool-results/mcp-agent-ml-research-pdf_to_images-1779045704134.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": true, \"data\": {\"images\": [{\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/_pdf_images/main_p4.png\", \"base64\": \"iVBORw0KGgoAAAANSUhEUgAABnYAAAkjCAIAAACzq+aSAAAACXBIWXMAAB7CAAAewgFu0HU+AApxVElEQVR4nOzdedxNVf//8ctMyNCAUoaKZEhmGTMmU6ZShMJtnkUKtxQZInOIZEiSsZJCpsxDyDxF5hQyT3F+799ZX+ux73Ou61znuvY18nr+cT3OWWeffdbee6219/pca68d4gEAAAAAAADgQkhsZwAAAAAAAACI3wixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAAAAuEKIDQAAAAAAAHCFEBsAAAAAAADgCiE2AAAAAAAAwBVCbAAAAAAAAIArhNgAAAAAAAAAVwixAQAAAAAAAK4QYgMAAAAAAABcIcQGAAAAAACA2Hfx4sVjx47dunVLr//5559gvnL69OmTJ0+ar1y+fPn69es+C9y+fVurjfKs+iPEBgAAAAAAgFg2ffr0Ll26TJs2bcSIEX379h04cKASL126tGjRopYtW77++usjR47csWOHWfjq1atasnPnzqNHj545c+awYcPefffdTp06HT161Ge1W7du1RdjIP+E2BCNrl+/roKumlCvXr2OHTtu2LAhtnMUNXbu3Pn+++/v2bMntjMS0/bu3du/f/+NGzdG7uuHDh1SQzlnzhyf9DNnzkyYMGHx4sWuM4h44OzZs927dx8+fPjt27djOy+IGrromTVr1tChQ2M7I4Hcs+02AABAfLFp06aGDRueO3fOvF29enWXLl3sp59++ulrr712+vRp8/bixYvt27f/73//e/78ebvM9u3bGzVqdPDgQZ81Dxo0SGtWTySat4AQG6LNkSNH8uXL179//19++aVUqVIhISEJEiRYuHBhbOcr8v7666+2bdtmzZo1xEvbFds5iiFHjx5t06bNk08+aTZ87ty5Efq6mrn//Oc/9uu9e/f2WSBv3rzmo48++ijqco046oMPPjCH+6effortvMCtb775plKlSkmTJtUBLVeuXGxnJxT3bLsNAPeaQ4cODR8+/PXXX2/VqtXixYuvXbvm/FT96pkzZzZo0EB97NmzZ9suunH79u3ly5d37dpVXw/1QnfBggX6SBe0unq5efNm9G4JcA+bPn16kyZNnPX3008/ta8/++yz1157zQbgRowYoRrtU51FdXz37t3OlD///HPAgAGqxTNmzIi2vP8fQmyILsWLF8+XL595febMmWzZsql7M3r06NjNlRs3btz4448/mjZteq911a5evXrkyJGOHTtGLsR28eLFkydP9uvXL9QQmxrQVKlSmY9Sp07NyKa73ueff24O986dO2M7L3Dr77//Xrt27X333RdnQ2z3bLsNAPegU6dOqfs9bty4sBZo06aNLmjD+nT+/Pn6eosWLXxmcbp161b37t31kfrzUZldAH6WLFmiujZ06FBbDVWvbQ/RGWJTB1OvP/nkE/+VnD17Vp86U6ZNm3bo0KHBgwc3b97cf5q2qEWIDdFi1apV6sy88sorNuXYsWM6b6m3E4u5igT/m1vnzp17b3bVli1bFrkQm6GueFij2L7++uvKlSvny5cvYcKEPv9yxF1p9erV+/fvj+1c/J+75gb2mHHgwAH/AfaqvHEqxEa7DQD3Jl1tqsv9+eefh7VAhw4dunbtGtanP/zww0cffaQ1qJPvTF+/fr3650ofM2ZMVGYXgJ/r16/36tVL1U21devWrT6fOkNs69at0+uZM2eGu051MAcNGqQXv/32m77y888/R0fOLUJsiBZmyECjRo1iOyOuzJo169VXX/VJ/O677+7Nrpq2102I7eLFi2GF2IwtW7Y8++yz7vIIREyodRxh0QVKwYIFfQbeS4ECBeJOiI12GwDiiLNnzy5YsGD58uVLly69cOGCSdy/f78S1Su2c/vevHlz27ZtixYtunr16sKFCydPnvzHH38oXYlTpkxRih3A8u+//y5btmzixInff/+9Fvb/RfchtvXr1zdr1qxTp07muYRG//79zfg4QmxADNAF57Rp0xo0aGCGjjpHYDhDbHPmzNHrH3/8MdwV/vzzz6tXr/Z4bwnv3LlzgEYgSsRoiE2bdOTIkc2bN+sad+XKlZs2bfr999/VVvospuZYTar2glpkNXP79u1zjuXbu3fvbwFduXIlJjcKoSpSpEh8D7Ht2bMnVapUzoF4xj3bVYvuEFv9+vXVN3aXRyACwqrjCEvz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XsWKFStevHjZsmUbNGgwatSoSE8zN2HChDJlyiRKlOjQoUNRmtk4J36F2MaOHVutWjUd6Pz58+v8FeoyS5YsMYWhZs2aM0N7WOqBAwfKly/vn65T4eDBg4sWLWq+Xrdu3WnTppmPduzY0alTJyUWLly4c+fOJ06cCCuHKnJ16tRJmzatCmGFChXat2+vF/rFUBf2z8mFCxfyhcc+pJtGFgAA4J7wxhtvxOV/X8P6559/QkJC9DdqVxszIbZLly7Z12E9+jlaXbly5dy5cy5Xsm3btt9++23v3r27du3asmWLT39+z549W7du1d/t27dH+WEyCLHFHSpOMT/49y4IscmCBQtU5DJnzmweYfn333/PnTu3ZMmSiRMnbtGihapqJNb52muvaZ2E2CIn+kaxbdq0ycyM3Llz51AXqFChgllATWuoC3To0EGf/vrrr6F+unnz5tSpU2uBLl26ONNXr16dLl06fRogbzdv3ixYsGCVKlXM6enatWsdO3bUqlasWBFkTk6cOKFCq3OoGny1Bh988IEW6Natm16fP39epTpFihT79+83C9PIAgAA3BPUMyHEFi/E0xDblClTsmTJkjNnTnWlatWq1bNnz8aNG0ffz/mbNm1a5cqVkydP/tVXX7lc1dChQ1999VUdhQwZMvTq1Us9KOen3bt310cZM2Zs3br1zp07Xf5WqOJmiE39yU8++aR06dJm1IZelPMqVapU/vz5lTJhwoSoym102LhxY8uWLU3mCxcubDL/wgsvFClSRCnqhDsXHj9+fKVKlVSiXnnllWeffVZLOjvk6nL37t27QIEC+mKhQoX69u2r3RuFWb07Qmza4Spy2kU+6e+++67SVWxM6C1CunXrRogt0qIvxKYa8fDDD+vQpEyZ8uzZsz6f/vbbb6px5mFlf/31l//XL1y4oMZWnzZo0CCsn5g/f74WSJs27alTp0zKpUuXVAdXr14dOG8bNmzQF1WjnYm6Ipo+fXqQOTlw4ECzZs3sWxtisymdOnXatm2beU2IDQAA4J5AiC2+iI8htnnz5iVIkODnn382b9evX58lS5ayZctG08+FZfDgwdp17kNsHu8taVqVVuiTruNSr149VaVr1665/5WwxM0QmzFu3DitRzl0Jp4/f75p06Z9+vQJciXRN5dW4DXfvn37kUceUf5tWTXWrFmjrrt5ffLkyQoV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3bt3y5Ythw4dGhQUFB0d/fTp06+++srpuzdu3JgxY4Y2/PLly7pldgSUwVEWKMnHH3/cqFGjhw8fmqyRhCOsXbu2ZMmS6G73k9KODgPcvn1bfHfv3r2BgYGtWrXq37+/m07Ajx49qs0OaW7fvv3gwYPXr193r5bO8erVK2Q0evTojh07xl4uFy5cwERRpUoVeXJfQsISJMUmISEhISEhISHhGWzatKlSpUrkird3795xkGNwcPDHH3+cOHFi8qMSBznGKp4/f/7nn39++eWXSZIkoWZs2bKl07caNGigvEZAQMDWrVv/++8/R5EfPnyYKlWq4cOHGyQYEhIyePBgLy8vTrZ58+ZBQUF3797lODt37uzXrx89RacvW7bs0qVLZup4+fLlkiVLvvfee23atJk0aVLnzp2zZ8+eMmVKX1/fwoULO30djZM8eXKxJIS5c+dSYSAMmTJlyp8/f758+SgkRYoUBQoUyJ07d/r06blGDx48cJQFuoDirFu3zkyNJAxQoUIFtGTRokXdT+rAgQPULxAeSEuVKlVqxUTBggUpQubMme/cuUNvPXv2DDKGwESJEnHv169f32CMGCM8PHzJkiUffvghF6Zq1arVqlXLkycPuUjKli0bZHv79u3uV1mLq1evYjDSjFeuXLnYyOLJkyfdu3dPly4dVfB///tfbOQiIfG2QlJsEhISEhISEhISnkSJEiXijGIjTJ8+/e2g2BitW7cm/TZRokQXL140iHnmzBkmDooUKeI05e+++w4x06dPD0XaOObGjRuZlZg7d642wp49e/CoS5cuL168cJovATGJhF27di0HPn78uFOnTgiEVm/8enR0dObMmRFz8uTJqkczZsxA+BdffBEZGUkh9+/fp8LXq1ePo507d65OnToIvHnzpqNcoqKiGjZsiLc4KQmXsXLlyqJFiy5dutT9pCAzRCLr9svTp08LFy5MPf77779zeIcOHZo1a3b8+PGXL1+i0wcPHkxxJk6c6E5hmIetW7euGB4WFta2bVuiwEqXLm3+aKcl9OrVK/YoNsKGDRskxSYh4QIkxSYhISEhISEhIeFJ1KtXL44pttWrV79lFNuwYcPee+89UnH79+9vEBPt7OfnRzEbNmzoNOVChQpR5Pnz5zuNPGvWLIqMt1SnfqKjo0uXLt24cWPz/JrtNTGRI0cO7aP27dvjkTHxt2rVKiqPr6+vKt+JEyfWqVNHDNGl2IDbt2+nSJHiwoUL5ovtcTx9+nTMmDHxWIA3ETNmzGjTpo2jp3ymUpx5goODO3fu/OrVKzFm8+bNEa1q1aruFOb48eOU3aeffqp9evTo0SxZsuBpqlSpRL7PU/jyyy9jm2Lbu3evpNgkJFyApNgkJCQkJCQkJCQ8ibin2H799de3jGL74osv6tSpA/0c9UqZMuX9+/d1oz148ABP582bR8rwxx9/bJzsjh07MmTIkCdPHkQ2cysTaNKkCSU+depUMbxPnz5+fn5WrZVNmjQJSWXPnl376NGjR+nTpw8PDzd4vWrVqmXLlqXyrFmzRnwUGBi4ePFiMcQRxQY0bNjw+PHjlkruWXTp0sUMHyohYtCgQY7oqj/++IP6umDBgiJLO23aNC1p+/PPPytu3109deqUAcUGXLx4MW3atMSyIbI7eWkhKTYJiQQLSbFJSEhISEhISEh4EpJicx9ffPHFJ598MnDgQNJyJ02apBtt+vTpefPmvX79ukmKDWkOHjx46tSpFP+vv/5yWhIo2JkyZULkZMmSMVOwaNGi1KlTnz592mq9xowZQ1lv2bJF+zQgIGDnzp2O3j127Ji3tzcq6+PjgxSqVKkiPj1w4IDKLrsBxXbw4EG21RX3WLhwockjhxIiduzY8fjxY204RPSDDz5AkyZJkgQ96zQdMts3aNAgdwrjlGIDFixYYP54qSVIik1CIsFCUmwSEhISEhISEu8W/vvvvxUrVgQEBDRr1qxv375aZ3/Pnz/fsGHDgAEDbPYbbdOnT2/SpEm3bt1CQ0N1E9yyZUuXLl0QZ9iwYVeuXDFPsV26dGnUqFF4d/DgwUuXLhXtczGg4C1cuLBPnz5NmzYdPXr05s2bVde+bHoUG8r8jYATJ05Q+OXLlzlQZHNevny5cuVKtAZygfp66NAhVRbIdPny5T179uzRo8ekSZO2b9++b98+pxV02tSOQBQbSktGnbJmzRodHa2KgzLnzp3722+/vXnzphmK7dq1a15eXuHh4ffu3UuWLBnio8vMFOa3336j9EuXLo1ioOLe3t6uuWXcuHEjJZU+fXotm3bnzh0D82dofHKhOHToUEpE200iDCg2p7h+/TokRGWx3vy4MJCWH3/8kfrUz8+P5FAUJPROYGBg+/btW7VqNX78+PPnz6tStjo29+/fD3mGVHfq1Gn+/Pl4RRXBqeSr8M8//4gjC9XhR7/88gsFTp06la/x4p8///xzyJAhqnRcHhpaQOypoydMmGAmfuPGjdH4bjrKNEOxoW2JngbOnDkjPnLa0cYTjkixXb16deTIkSQGO3bs0C0JskMuLVu27Nq164IFC549e6aNExERMW7cOIgBRhmytkSxOa0Ohva0adP++usv1Gvu3LnodD5zavCIEBwcjDRbtGiBwn///feiW5V///1XlEYIp83+AUAMxPRFkY8cOUIhs2bN4hQwx0L8Vq9e7bSOEhImISk2CQkJCQkJCYl3CNDHChQo0KBBg9OnT0MDhFYMJapDhw7EW0H1glKXOnVqonUuXLhQuHBhX19fcsWYJEkSlQoXHR3dvXv3nDlzrl+//tq1a1D+ixQpQgbpnVJsUJx8fHwoQWhZdCHx+fPnYpxNmzZ98MEHUCBR2gMHDpCR75o1a0IvEqNpKTaoi2z7fN26dSIrhxwVu5F+PhGDxKtWrTpq1CiUf/bs2RkzZkycODG0Pn4Frzdq1Ag63sOHD/H/xo0bkydPPmLECHea2hhEsdkEvwdag/Fo8zRp0jx69MgkxYYK1q9fn/4n9wLvvfeeVhnWRZs2bSiLgIAACAaKZ+YtLdAOxYsXp6S8vLzGjBmj6nFHiIyMTJkyJanQFy9eJEN1qIXBK65RbMuWLatduzalz/yRpXFhIC1IZ+bMmRUrVlTs5u1m2AHBphcnTpzo7e29YsWKqKgoCHDlypUzZMhAVbZaBpvddWzXrl3Lli0LqQ4PDx83bpxit4In9rhTydcCNfr++++pYVFC0TEr/kfFU6VKRWQQSvj555/TbIACi4m4MzRU4FvSKAySchr/p59+ql69uvsns8xQbDY7L0zR0LwcaNzRNhMTDlNsQUFBadOmzZs3L3F5kFutG1xkhyqj4mvWrGnZsiWilSxZUuVEBbljph0wYMCxY8fQKZhp2T2r07Yyrg5EC3M7uSdevHhx//79KVlILF5x9IjkCn/btWsHUfnjjz+uXLmyfPnyXLlypUiR4ocffqDEMSg6duxIb40fP56+Q0C6+Hr7nDlzeIb577//6AAv5I0Lj+5T7F5lrl+/blxNCQmTkBSbhISEhISEhMQ7BKi10ChWrVrFIRUqVFBi3hkcOXKkYjchVKNGDTrV8vTpU/yPwGrVqompQQlENCg/HHLixAkoSGYoNqhwrVq14p/Qpnx8fMRDTL///jvSUTFZUNoRmC1btkePHnGg7kVR1Ii0rE2bNonh0PyhpPEZFiiQ2bNnh/7JEbZu3UovhoSEUMjKlSvxUzSoNG7cuIEDBxpX0ExTOwJTbGFhYVSYYsWKqeKgRwYPHox/zFBsUD6hhEPdpZ8HDhygV5zWgnD37l26iwfUrl3bDJfhCJcuXSJjcAToz3///bfTt2bNmlWyZEn+2bBhQ+rxW7duOXrFNYrtzJkzW7ZsoRfFI1o20+PCqbT06NFD0Vwe3Ldvn2I/2sYh5BpCdR/W/Nhs3bp1uXLl2BIZuixnzpyI5u/vTyFmJN8RUCpEK1WqlCq8Y8eOPGBv37597ty5jz76SEuxuTM0RKCzkidPjhdTp05t7HgXwJAnEiddunSTJk1ygc4TYZJiYzoSnU4hZjraqQgRxZYlS5b69euT+UIMcPyvnShQUwwxkciGVCAaZIZDMMl4e3ur3Kq0bdvWDMXmtDrol/Xr11NSKOHs2bOPHj0KWS1fvvz58+cdPYK4ooMqVqyInhULgMoSmThz5kwKuX79Oq04P//8M0fDJEMs+f79+8XSrlu3TtU+mGkRLUOGDFFRUQbVlJAwD0mxSUh4BpcvX54xYwYWFRfehVKxbNkyrMEeL9UbhN27d48aNQo7M+wIsYdAS7q59ZF4c4E9JbaShw8fju+CeBIeqdT27dt79erl9BZPAgRmOexip06dqvJIKBEvyJUrFzQKqHAcQucaJk+ezCFr1qxR7Aci7t69y4HkzBEKLYdAD9el0sqUKeOUYouMjFTshynEQEg41HL6/9mzZ3nz5k2cOLFYBpudUKBjO6JC6MgWG5UEuqIYOHHixO7du/PPQYMGIUFx0cH/lEWjRo04Dn5u3LiR40RERPTt29eggjZzTe0ITLEB0DlJCxXvLUIXRePQaT4zFNuKFSt8fX1Faowah87BOS2PzX5ojnLJkyePrkks80DrkVdHRqdOncTzUCqgRwoUKCASXsyCjR071tFb7lwUhcqtpdhMjgun0qJLsf3000+K3Vo/h5w8eVKxm8BzoQzoboQEBQWJ706bNg2BTZs25XI6lXxH2Lx5M7WteP8RYxPtJhLuwLfffqul2NwZGozo6OhSpUpRMZYsWWIcedasWfny5WMvvUDPnj3N56WFSYqNRw0PZzMd7VSEiGJDM4rEEHFbAN8DxVtIltkoAn5StLCwMAqpUaNGkiRJbty4IUbjIWZMsZmUW8wzCGzfvr02BUePyJKd9hsAhESxO4FhSWvWrJl29qtVqxYC6SMEA4rGnDlzxBDIfHBwsGqVkZBwB5Jik5BwC1h1sAoWKVKEFiFsIyy9Pn369MqVK5NJDl563zVcvXq1evXqTZo0OXDgwLlz5+h4AtCtW7f4LppEnAKjCdvH3LlzkwDEhpP7uIcHKwXVhXyTYcLxYAnjBhMnTqQW0LW0JRHH+Oeff7777jvxUAMpt8OHD+cQsr2VKFEi8cXdu3dTP/L5L6J+tm7dqsrCjC22Fy9ekDmwgIAAVgihMrGtKEgLsTnad/v164dH3t7ebO/JEcW2fPlyChc1qAIFCvDVPOhXPj4+2bJl+zwmsmTJothPu1C0CRMm4GemTJnEMxFnz541qKDNXFM7gkixsf0ykSrq0qULUqP/zVBslSpVGj9+vBiyePFieguFdFoem3AjDxA5SpexefNmX19fThOTm0rJZ2zfvh16uMgmkB06vJU5c2atlTqCOxQbnZRRUWwmx4VTadGl2J48eTJz5sx///2XQ4iqEBkT82XImTMnxpf2a+WxY8foU4dJyXcEvJ4/f37EFI2srVixQmvX/4cfflA0FJs7Q4OByCr2yikePnw4d+5c4k+BvXv3ms9OBZMU27p16ygamRG0metopyKk6+7gzJkzlM6FCxcoZNasWfiJthW7mNltMkn2999/4/+yZcuqSm7SFptJuaU2X7hwoTYFR49IvRLPphFu3bpFx9Z4QqPTlwjkLzQ2+714mh94mYiMjITMG1D5EhIegaTYJCTcAjYHV69exRRPa4lVig1bSajc9Ent3aTYsNfBFq1o0aLiMkzf7rCZjseCScQ9oCNdvnyZFA/lbaHYPFgp6DP58uVDIh999JEHSxg3wBaZWsCMeXiJOAM07bVr17Zt2zZHjhzoHahe/EhXjVdpXC9fviSODEq7KmWT7g5GjBhBCebNm1fL05HryfLly2tfpBM6inCRyhHFhmX6/fffZ2USCA0NLV68OEc4ceIEnpYpU+ZXB6BjXxEREcRxY8nu2bOnVUPpBk3tCCLFhuHPdpGote/cuYPGZwv3Tim2w4cPo+RhYWFXBZw7dy5lypR4Cwux05Pje/bs8fLywj4na9aslNfmzZt1Y16/fv1qTIh6rwqPHj3q06cPny3y8/PTNc3m7+/foUMHVbLs9GD58uW6iccNxaZlIpxKiy7FJuLSpUsYHXTFEhCPGZopA3pWsdt6M6igSck3wPTp05ECxhdTnHXr1tU6wdCl2BguDA1CSEgIiU2WLFmsOof9999/U6RIocQ8CWsVVi+K6ppudNTRTkVIl2K7ePGiamJs0aIFfn7zzTe6XUyTCdF5WjXEBY+iBnJLPJrKj4HBIwgG2Wj7448/tK8Qvct2BiCr2bNnR8iMGTP4dV9fX+pl3nrNmTOHiU4JidiDpNgkJP7fN3MDQx5mwKusVYqNQNu4WKLY+BB4wsTYsWO1yyc2+jNnztSaa5V4+6CVz02bNr1NFBvBU5V68ODB1q1btf7gCAlksDuaUbFZF83KvE1wfxGJezx//nzWrFkVK1ZcunQp/oei4gLFdv78efrJJyYYJik26EVsC1yx318TW5Ls6+fKlUv74s6dO+kVNrLmiGKzvT7qUrhwYfrZrVs38aLQ9u3b8bRSpUrGRQUOHjzIxsgyZszoiNZRwWlTO4JIsdmEE2SfffaZza4Vi9q1U4oNtVYMoaU4RVy/fh1179evn00w14UQXd2brn2JUBEBWmzYsMHb25sia68KYohBFA0Krz2AQ4gvis3mTFoMKLYjR460bNkSvXzmzBneXlql2MgKYe7cuQ0qaF7yHQHNS3bQ1qxZY7NfSsiWLZvWGoAjis3loUFZ8/lH14y0DBw4EO/WrVvXhXcJJim2Pn36UDTVBsBpRxuLkEmKDf2rxLxgrkWHDh0U4ZAdwxLF5rQ6Vik2PpEn2gpk1KxZU4lpCnD06NEI4c8naC6I1rBhwxDYunVrCsTTXbt2Oa2LhISbkBSbxLsObAWqVKkiHm92AfS1UHGVYqMPwrFBsWE5Z4sbCRDPnj2jb3Qqsx0S7wh05ZOsm2s3o2804qBSCWSwe2RGfbPwJlb59OnTfn5+KDY7FnCNYgsNDaWfWsvoJik2wqZNm+gAgmK/1MOXoUg19fLy0h6wQhUoPh+gM6DY2O71P//88+TJE2QhXhQi76IINGMA9N69e9AhmdlxSgeYaWpHUFFsT58+hZpNDYJFM1u2bKIdK2OKjagQ1PQ/DchUuWK3Ne6oJFisoclXrVqV2ZPOnTvTW82aNdPGDwgI+DQm2FzayZMnHX0MWLhwIaWpstlvsxv4r169urbwADk9oM7VrTg9jXuKzWYoLY4oti+//DJJkiTEWNkEEscqxUZX/xDH0RVam0XJdwSSBBKe8ePHo6e0cXQpNneGhk3wb+vUHqIj0Lpcs2ZN1163maPY0La0yU+XLp34ecxMR9sMRcgkxYZhi59z5841qEjdunWVmN4PCOYpNjPVsUqx3b17lxJRXW8nkJ9lcYbkeZ6M3pYoUQIjhXi6ZMmSYc7HXCcajJOQiD3EKcWGWQZ7goMHD+7atWvnzp1YYi9cuMC3oxkYUUeOHNmzZ09wcPD+/fuvXr2qmvqxWhx1ANELlYSEGZBrobeSYjt//jxWdAOzLPEOXryt3riReAvgSD4lxeYCEs5g98iM+mbhjatyVFQUOXOE2HCgaxRbREQE/VTREDZzFNt///3H17uePHkyevRoUpDq1KlDgVALVeoigyxPQaljBsGAYrO99j7ZpUuXZcuWqfThy5cvUy586VIEmousNaGyHAhVrXDhwvQW9quOKmiyqR1BRbEBX331FWVavHjx7Nmzi8eFjCm2b775Jl++fI4yKlu2rKN2JnTu3DlbtmziAUPst5kV1T1j4ghoTN2bvzb7kUb66pY/f34x/OnTpz4+Pug43bf4SF2bNm20T+Pxoig/1ZUWXYqNDip26NCBQ1ym2G7cuEE/2YGsCKhaGHEmJd8Y5O4WI/fSpUsFChQQRZ2hpdjcHBpseaBQoULsL1UFjA6Md4NE6AtBQECA0+wcwQzFRrYglZhnM810tFMRMkmxEUPn6LDejh07oGXTUWKMcZXGbZJiMym3Vik2gA7xiV6nGbVr18YjTIliINYOBA4YMCAoKAjSSNWpWLEiDWTIw9SpUw0qIiHhKcQdxYaF8+DBg39rgAlOJPXDw8O1cY4cOSKOeWjj2jgE83fFJSSARYsW0Rrw9lFs2FYWLVrU0W47gWDp0qXaNVjiXYCBfEqKzSoSzmD31Iz6BuFNrDK5I/T29hYNLZH1a6sUG0DOB7WkiRmKDYkMGzZMDKFzTClSpKCfZ86cIXdAo0ePVr1LOra/vz+HGFNs5BoPKUPd2r17t/gI7ZAqVSrFwTGubt26nT59Gv9AbROXqsjISFJ6v/nmG0cVNNnUjoA4Kgrm9u3bjm5TGlBs0dHR2bNnnzhxoqOMlixZQu/26tVL+3T27NkQAy2TSBICpE6d+tKlS06rQ0CnK46NuGXOnFkRbnUR5s6dmzZtWkcX5KEgkNODJEmSXL9+XfU0vig2p9JCpIZK5CjOhAkTOOT48ePabZLJMlD5ixUrpjrI9uLFi7Zt2z5+/Nik5DsF+aWtW7du7dq1dSNoKTZ3hsbFixchctTjBv61N23aZHx/k2abnTt3GmdnAKcUG4rKM6RocdhMRzsVIZMUG+Irdg5US6SePHmyR48eNvsYp7dUZltMUmwm5dYFio1usCZPnlyrJuTJkweVOnjwoBi4cuVKxX6pFqLII5fckpYsWRJ9IYkCibhB3FFsGPPEggUHB2PYnz17dteuXRTCG9O7d+9yHAx7bK04jmjm49q1a5JiS+C4evXq8OHDq1WrVrNmTawrHTt2dPSZF3sjbJ4++uij/PnzY5HGir5ixQq8rhv5wYMHgYGBmDezZctWpUqVwYMHaw3oQpyQNZ7a7FYeMON/+OGH2Fxi06n6PDtmzBg2r4sCtLPjyJEjTmuHzcq0adOwquXKlats2bJfffUVryVais1MmUWKbfv27Y0bN/b19S1VqlT//v21Bm5sdn0AGyyoFjVq1EDzYluDuojmgVFT/t6FfKlqWIytFkwX6LKgoKBWrVqtWrXKZvfFni9fvgoVKojrnNPEoR2hSOxqHam1E4BtFjZ8fn5+KsMT5jvXajXXrl2L9mzWrFnLli27d+/+3Xff6X741cJpX7hWcoPyhIWFiW3VtWtX1BGdgrEjhgcEBHBN0VMUiM2KapKEvLVv375IkSLYrKAX+JA/w2l337p1q1+/fk2aNGnRogWiYTholWEVjOVTxUZB90O7Qe/C9ghdqTXyEhERAVWzQYMGNvthLgyfHDlyiA7ObHYHamhGtDnGLGoKAVNZHbpx48bAgQO59cLDwyl89erVnTp10oaL7WNmBrNaKUe4fPky9GTRdI6nBrvTZnQ6qxvPqKjjli1boNfNmzePQvbt29e5c2duWwgnInBq8+fP53CRl3R54rJZH4ZuVjnBYubMmVRmNknz8OFDOlFClrYI5M1TpcazBTSeScgjgRLT3jyUSTKThOnFoCRIBANH1LGxvELrZqNpNrueqdhNSqlognr16iGmuERijlLslyh180IuGP6K3Zq+9ukXX3xBtcCyy5rw48ePMZGy38zevXurHNt9/fXXymsrVLow2dSOgMlHa8IM5VHsXKHq9DfbLdIeVyENU3c7QUBNyaIW/qqsCmKqhAyMGjVK90W6XwZUrVpVeyvFEdKmTQsdGHqBKhwTLKUmNimGKnrf2EI5cQ0AJgTVI4xiLqHJ4jGIHPnhhx/EQJPjwqm0kKOPokWL0k9aBegQX61atfgttpQvdrfJMpArSao7+2nFU8x4zGWYkXyn4C8NtE/QghicTJkycYjLQwNiRsbFAAPW+MmTJ4UKFaLryRj72mUCazeWbEwvYiAaGR0HaTcpzNgIUUl05RP7K7rZjYVeVQAzHe1UhKjvRGNkNrvLUUoHigmFQLkmRjJLliziRh3LGRr83LlzNjsTTdKO1MQLYcSNAtrNj9Xq2FzyKAqVn/yxqB4R96cVUUwXPj4+iv36M8szRIucHrD/ZRXQaNhpaM9iS0i4jLij2DAYVCxYVFRUcHAwBdK3KT7mxodjMUWGhIQgZPfu3XyQDSMBIdAzozVw6vtGIg6wadOmpEmTYmNNEyu2a9hDIATKqirmo0ePoO1AY0efYj3btm0bLQO0fUyTJg00eY68cePGggULYsewf/9+6PzkrQYLBn+WwUYQyxi9joX8ypUrxYsXz5o1KwLpMzgSZ9UXuxmsUljIKT672hEPZusCAgyNK2/evNgWIBHUEVooOThXNBSb0zITmGLjOyAMrDqQdjEyBgXUS7QPhgYNCloCsYXijzzQ8VAXOl/NvqJ27NhhtWAq3Lx5E5swdiWGLRpvzhT7BRzziWP8YuvAXsNRhZ/tQJrYeDH1xtsLS51rtZpDhw6Fus63Feh7Pqpm0BTm+8KFkjstD296oHjwFQnsisgyhWI/rq/aINJ2VtxAYM/RqlUrtMnvv/+O7pgzZw4ZqO7atSvt9c10N6qD3QzC2eMeHcg35oyM5ZPZKMwkkBBMHUgTDUKBosaOKQXtTzawc+TIcenSJS6t8trAHwo2efLkZMmSTZgwga6kHThwgPxyopWwreTUELNdu3b0rng7BsqGv7+/NtxmZQYzXylHQPsjL07cZGPaTIwCM83odFY3mFGh2Pfq1Yt2vUrMIz/QAUixB0R+jTBlyhSEY6duvi6O4MIwdKfKTnszfsEG1AoXLow5YfTo0RAtul+DKQWSRhMvn2u4fPkyv4unFMgW0LCXK1CggGI/JTF48GDI3h9//FG3bl26RYih99lnn6G/dEtCB5qmT5/OIeQ/gXlYm31mI426U6dOHLhs2TJIjup+4qRJk6hsjnwLUgQxOwamgpw5c9LrGE0Y8g0bNsT6C6WRP5lA40Uc6Kv8FuYQDH9MEbrZ2Uw3tS5QJJQEA5Mt0xGIStMeD+SugYSLV+fQGjQ/GJPRNCsCdKqFsHPnTtJvSQ/XApXiuQIvmjTpRUs8WkA0wX7jxg1MmMprZw4M8tjep08fgwQhD1QGSIWKC8CApUfoTUvn5dHRRKCrjIuZHBdOpYWO2yh27gCzWZs2bTCl0NlPxX6SC6MAcsjOQAYNGjRmzBiiP0yWAWpR+fLluYP8/PzwE0NSPKtoRvKdAvKWPn16TPKOXiGi3MvLi7vA5aFBPrIUu4MLtMajmEB1/v33X7xOfDpdLm7WrJli/wrC3z/QMmgEZKcqMB34UhyfslSBPZCgZ7FlQgHw959//pk6dWqRIkUUu/21wMBArTk8Mx3tVIQ+/fRTxX5iS9zvYfqldEQXEDNmzGAxwHTasmXL0qVLJ0mSRPx8xWMZi+OiRYv27duHJZgOyCv23YXq053V6mDPSaut6uSyzb4ddfTIZr9p6+3tjTWau+/BgwflypWrXLmy2DgMEjbM9mJgx44dEYhNmm7527Ztq9iXMGkYWsJTiCOKDYOfuDPVcVzodcy7YWHGU4ojLtInTpygOLxnOnz4MH6+rY7J3nRg6sf6rcQ8bEwLPzbcKg4UyjwvgQS2WQC9Bb3M+3L8j8VA3I1hXaQVFGoq7yaxjJFdT6igWD/++usvCieTror9fr5YALbmYPKODzLKmzcvNh/8PZDQpUsXSkek2EyW2faaYoNyi8JjbUY0LCRQJyhNrCviySPymKO6lUOezufPny8G0vdA7Z0R8wVTAbsHaKG0elHKI0aMwK4dnZUqVSrSdiwlTl/kFM0RdPJyBfzyyy8caLVzTZbk5MmTiuYWEjrUzC0ek31hqeRmyoNxROqQylnY9evXUWXt6zb7R2YUjPdhmGOhA2NHK062vMEiMTbT3a1atcLGSNykQkMWt9EGcCSfzEZ9+OGH2NJRT6ENGzVqRHsgVvZQvIMHD77//vuKnWdp0aIFVge0av78+bEvJJqPaEFImpgF1BLS/6tVqya2AOtpKiqNb1Gpws3PYOYr5QiXLl3CakiNJlJsxo1pZhQ4bUbzs7rujAqdBxMmD3bVrTr+rqB1zvjdd99hvuX0XZ64CJaGoZtVTvigEzQAxi+ml3v37rFiBsU1IiICA4dZUUxxdOZl3LhxdChDsZ++YYYL6lObNm1o8gF8fX0h8FC6MOcgI8ito2Jg5ofIoZcxk2DOnD59OvRtra0cTFwYNRDRggUL9unTB3MXCimeFkTjQx0lMkixa4PQw7V0D6avtGnT6mplNjulAs2QND0AqSERUa769u0L5dPPzw8aI+aEzz77DFOoiv+y2tS6jmihpbdr146uTAJp0qRp3bq1yBxhpIv5/vrrr40bN+aSA9DMO3fuHBUVtWLFChojQIkSJaAza7PD6tCkSRNFQIMGDTBAMBVwmlhxunXrJnKX0MDRAlxIQqFChWbOnGncIDb7wvHJJ59g/sQShvZs3rx57dq10eDoHYx6Hl9YR/g7HHRsKMl8MIeBuaVXr178uUKx80R0hRYzMzoU6xE/QrRPP/3U6VDFxIJ5iT/1YcZA15PJGvPjwqm0IBfmv0qWLEk3bU+fPk2XXhX7+r5x40bba0tS6Aus0ZbKYLOfJ0X78JcMbF8XLFigGhpOJd8MMH/q8iMQpB49evDtZtRlxowZ9MiFocE3x02ClmxiaRX7Ulu9evVmzZo1bNgQTaSdIrZs2YI4SZMmdboir127VjXoCJA3SCC6HuMFqwPGoO7rTjvaZihCWLWRPk+5tWrVoosOgYGB/IUM87DoN3n16tXsnFSxE20YwqpSbdq0iYcSKtK2bdugoCCUB82F3bijupipDmZ1bH4oApoXs9O6devoXYNHjKNHj6LA0IYw9aHimGcMThqiMOnSpRMd2tjsXwuwTXL0DWDChAmKfX4QL/NKSLiDOKLYILJhdqhWx0OHDhF9hn0PFhv6X+USiK2z8beaPXv20E+sChfswC5Nnl9LIDhw4ABNlL/99hsHsg4jfnDD8kmBmDo5EGJAZ5WheXIgOhfzL7YgqrxGjhxJKYirCPbZ2rxsr635isfibNa1I1qnhw8frgrn8/lMsVkqM62I+CsuYFgJ6KuLYj/Az+Fks7lYsWJisqQ6qr796mrdlgqmCwPvY1YTd0SxsfUHkWKzWelc8yUhYxyqY0SYmsw4wjPfF+ZLbrI806ZNowRVdiiw50NggQIFVEVt2rSpSDPR93PaBjEgfrRfzJQpE29EjJ3NEVGlOjUAbc3MnX2nFJvqDsiuXbsoXGX0GtoghWvdyZ06dQrbxFSpUj18+FD1iPlE8bwM2XJSNFQa5FAbbn4Gc6FSjkB2SUxSbJbGo0Ezmp/VDWZUOp2kaCg2qFXEjKhaDKhcuTKr6+5PXDYrw9AjVU7guHbtGlYu8WQT1FeV6VtLwE5v//79bJMLezOnSaFbSZN/9OgRGhCvGyv2aPmQkBDzZr+0cGpb6unTp5j0Tp48qT2KS4dHUGYUA02nkiIDeLyp33RAHeCTOOiRDRs2YI49fPiw+WNTCR9mpCU6OhpTDXk/ZKAREIhFn8UDS/Pu3bvd8QoFYUaCWBANdCUDyTcDLIjiqXCTiLOhcfHixbVr1y5duhRr8c2bNw1iYqlydAzWs3Da0S5POAZAIsjCeId25coVbAPoehn2TiZNMMWG3KpAIorZw5FZRobulw/jyf/YsWNOk5WQMI849SiqAkYjHVsDMA4xJulOqOoU2/HjxykOfVLA1E8/iWhjYNRJi+kJAei7oUOH9uvXT9wq/W33Ha5SQsj2MKD6kPLJJ58oMa2l0Os1a9b8OSb69OlDKbRo0YIjk3M3QFUwxFHsZzTEQEvaEZszUO2HbHruDiyVmSi2pk2bqpJl/9NQ2jkQK1+rVq3Ei2BAtWrVtAq2rtZtqWC6QFtRTK0LcKuJW6XYzHeu+ZIQe5I4cWLVnaOgoCDjdrBZ6QvzJTdZHmwBkyZNqmiuC/G1BZEMioiISJ48uXj0kgr53XffqdqHrzzzwROD7gbogliFChXEgyEmZ2OnFJvKMwD7LlSxVEhBsZ9c0GbRvn17Rc8Qu82+eSUzzyKfaIliMz+DuVApR6ADsyYpNkvj0aAZzc/qBjMqW0TS2oan0aG6owFFK1myZLw7d3/islkZhh6psoSEhISEhISExLuGeKPYXrx4ceTIEWLH+AjAgQMHKIRNojx8+JDttZ08edJmv48gMmu7d+/m/0NDQ80bW5WIG0A/gXZK+rxKQWUDGVBrxVeGDRuGwBo1anAIXfUqU6ZMFwcQj+c4UqLIylKGDBnEQEva0aZNmyiy6vixTY9is1RmA4+iaAdK2ZEVFSiigwcPTpcunaJxmKWrdVsqmC6Yc9G6/rGauKcoNm3nmi8JepOvV/j7+xsYhHYKg74wX3Lz5SHLa8hOPNnOZ5FEK7Djx48XCdyoqKgkSZIkSpTIUeMAfAnLoLttwv0LlPnHH3+0dJrYKsX26NEjCleZySNuKEeOHNos6PaBrrt32+tDiIpwDM0SxWZ+BnOhUo7QxQrFZmk8GjSjCgazumsUG5tnDgwM5EA0o2hA2v2Jy2ZxdXC/yhISEhISEhISEu8a4odiw26Vr4ju27ePzUBGREQwX4YIUHvoXBuBTnjevHmTfh48eJBefPjwIZ9oc+f6gIRngZ4aNWpUrVq15s+fz8c9RM3k/PnzdERLdSfu888/V2K6hSIqwambQkLsUWyTJ09W7AZBtI+0FJulMhtQbD169KCUVZ7sXr16hVZt3Lhx9+7dDx8+TLqfGYrNUsF0YcC5WE089ig2SyXB1EEHmqh/IbeWjoub6QtLYmmyPHxtbeXKlRRy7NgxLy8vyit16tR05erly5c5cuQQmR3MpfSimW8SxhQbJnMyJEwoXbq09pqhI8Q2xYYFgiyV6F5xBdgcLxvat0SxmZ/BXKiUI1ii2CyNAjMUm9NZ3TWKzfbaLyFmQpJJ/M2cObM46bk/cdlcothcrnKHDh3KaTB06FB3yi8hISEhISEhIZHAEQ8U271795gRw5ZUdLMCTRUq4t8xAYWN/qHTHFAXX9ghXia9du0axdHe4JOIe0DrHjlyZLp06WbNmkWnWvh+jUpxpTs+SZMmZeUE8QsXLgw1T7y9T27jPv30UzO5xx7F9tlnn1Fk7SU4LcVmqcwGFNu4ceMoZVG29+3bV6JEiapVq7K5AfMUm6WC6cKAc7GaeOxRbFZLcuLECZXjLQMT3SJM9oVV3d5kefLnz4+ndevWpZ/Q6jt16nT79m2ilsh+/ObNm3PmzCmeL9u/fz8le/HiRacVNKbYbHY2ZNKkSWQbXrFf9xs1apTTZG2xT7FxfEwpugXgI3jsZMoSxWYzPYO5UClHsESxWRoFxhSbyVndZYpt48aN9JRsNm/atEnVa+5PXDaLw9DNKhcrVkzRQCvtEhISEhISEhISbxPilGJ79erVpUuXmDsLDw/XtWd5/fr1w4cP7969+8CBAzdu3Dh//jzFR7ijlPn2aGhoaGzWQMI5oJZUrlxZiekezhHFBr3l66+/9vb2hm4DdXf16tUNGzasWrWqyiZl9+7dFfsBBzMGUGOPYuvXrx9F1pIdWorNUpkNKDZiARInTsz22tevX+/l5VW0aFHRLLR5is1SwXRhwLlYTTz2KDYXqglpnD9/PvlVVOxGqZwaeTXfFy4cnzFTnilTpiivjVgBSZMmJVfLTZs2RXjt2rVt9uuQ48aNE9/CvEppipb+HcEpxUbAfE6ZElQ56iIOLormzJlTsfvj0y0A89c84Vil2EzOYC5UyhEsUWyWRoFBM5qf1V2m2NCS5Pfwo48+wk9/f3/RO7PVujiC+WHofpWxY7moga6PPAkJCQkJCQkJibcGcUqxQesgImznzp0mHZTYBHcHZE77+WuI++z79+9TnP3798dK0SVMgygh0Ty/zTHFZrObr6pSpQpU/RkzZnz//fe6t8yIRwC2b9+um+kPP/zAXR97FBuKR5Hxj+qRlmKzVGYDio0Uy5o1a9LPyMhIVAEhs2bNEqOZp9gsFUwXBpyL1cRjj2IzX5IdO3ZERERwOFq4SZMm9C4ScdAG/z+m+b4wX3JL5bl9+7aXlxceoSUHDhzo7+9P4Zs3b6ZXQkJCkiZNKjo6IKRIkUKxe23XrdrDhw8HDBhA/xtTbCtWrBB/bty4ka644q9Tu2xxQLGRf1VFc8+aQBdFs2XLxiFWKTabuRnMhUo5giWKzdJ4NGhG87O6yxSbTeCLUaQ0adKonNO5P3HZrAxDj1RZQkJCQkJCQkLiXUPcUWzQ8fj8miMPvuHh4cftYGfe//33H3kdDQ4OJhMtYWFhlIjoUxkvUiC5RJCIR9CXf+h7YqCuCRsA/VWxYsXIyEjjNHfv3k2v+/n5RUVFaZ/WqVOHf1qi2FhzNnP+8eDBgxQ5f/78qpMUTLHNnj3bhTIbUGzFixeHznngwAH6GRQURMlCrxOjlSlTRkvrkLdHvkXoQsF0YcC5WE089ig28yX59ttvVY358uXLQoUK4V2mmXRhqS/Ml9xqeVq2bEnMSKpUqdi1JWZLEqpMmTI1a9ZM+1bt2rUddWJ0dDRe+euvv+inMcVWrlw5VcjKlSspvtYriAq68mnzKMXGLkp69OihW3g8mj9/PocwNclXRwkY1+7MYC5UyhEcUWzuD3aDZjQ/qxvMqE4ptrt379J1Y19f306dOmlL6+bEZbMyDD1SZQkJCQkJCQkJiXcNcUexsUm1nTt3HtSAvldDXWFfB9ht37t3j70iMHd27tw5ttF2586dhw8fXrp0ib2OirybRLygdOnSiv0kAtsOe/LkCRtEFw8gPH36NGvWrNWrV2cHsgYgY9gAtGJ2//fs2bPvv/8eelFYWBjH7NWrl64SRWVIly6dGMgG45csWUIhxh4zuCJ9+/YVWbapU6dSuGjj3HyZHVFsROIgLw5hCkDkTSD/3t7eiuZQUtWqVRGYM2dOzvrmzZuWCqYLphp1rxlaSnz06NEUmQrGCAkJUfULwVLnmizJt99+CyFUJUjnm1RUlwqW+sJ8ya2Wh5k+lQvLkSNHUvgff/yhfSs0NJSeJk6ceNq0aexO4fjx47Vr127ZsiXHNO5utCSqLIZERERouQldOJLP9evXU46//fabGP/27dsUPmTIEDGcjqplzpxZNxd/f388TZs2rXg2EMAERbIhDmR2bSn6sjxx4gTb1ULZONzSDGa1Uo7Qpk0b6jVVuPuD3aAZzc/qBjPqmTNn6JHBJWK2d6k9LWipLo5gfhh6pMoSEhISEhISEhLvGuKIYsPe9G9DQM2w2b/niy5EGbt27WIN8Pnz5+wtQQWT5sklYhWs2L///vsjRozo3r07lG1moMqWLTtq1ChSRY4dO6a8RtKkSRE/d+7cRYsWrVSpUvv27RcuXCi6O0TkTJkycXxfX9/ChQunSJEiSZIkqlMhderUoTjXrl3jQGjR+fLlI5WJbhwT7t27R+cmcuXKtXLlyq+//jogIMCgdhcuXMiePTszGjNnzly1atWnn35apUoVCkyUKBF03aCgIEtlphMTPj4+opYIOcfrPXv2FO183blzJ3Xq1JQgVGI0JjT8Jk2akHrs5eUFRb1Vq1YUediwYRRzwIABv/zyS/369YmqNl8wXaxYsYJe7Nq1q/appcTJSyDAZ6YIixYtonBUQQy31LkmS/Ltt98qMS//RkdHI2bJkiWhvRu0g6W+MF9yq+VBInnz5sUrf/75pxgeHh5Ogu3IdlXv3r25cdAsRYoUIdmuXbu2mJFxd2fIkOHDDz+kCVyM/+uvvxo0HcGRfPJ0MXbsWDE+hITCxeuQqF3BggWpDS9fvqzNJSIiguinUqVKsaOSGzduoNhlypTROnzgsVyvXr3AwMCmTZuiedesWcNSNGjQIErH0gxmqVIGQPoU/9y5c2Ya0+QoMG5G87O6wYy6du1ait+uXTtHtTt06BAioI66T92cuGxWhqFHqiwhISEhISEhIfGuIY4oNmxbzVBsNrvWGhoaKj7au3cvG3onQL05ePCgGCc4OPjChQtOTf9IxAGioqIaNWpEegg0Fn9/fyix0GHYPWKLFi1YgR8/fnzy5MkVB6hRo4aoo968ebNhw4bkKpGAjI4fP84RIDmiwfX8+fND7UTWW7duJR2bAK1M5C+mTZtG4YkSJerZs+fz58+NKwhhbt68OTRqegvl6dOnz4kTJxT7waXvvvtONGjttMyE//3vfwMHDsySJQtpdNADoc4VKFBAPDLDQGC6dOkotcyZM8+fPx913Lx5M1pbsRsP4hMWN27coOtjiv3+l2iOymTBVECE1q1bc90Vu23yMWPGqKKZSfyvv/7q0KED2pwi+Pj49OvXD0136tSpXr16pUmThsITJ06MaEeOHHGtc82U5Ntvvy1SpAjUYzyCMEyfPr106dKQUtXBOl2Y6QurJXehPDNmzIDOrw2vWbPmpEmTDMq/ePHiDz74gMuQMWPG2bNns5dnM90NQS1TpgxKO3jw4Llz5/bt2zdnzpyihXgDaOXz+vXrXbp0oWOANLjQ+8eOHcMSgJTRnlySxo0bo3iTJ09Gu3EgugCDUXtfD0vDxIkT8Toqi/Q//vhjZDd8+HDRnzUD81WFChU4zTZt2mB4HjhwAH1arVo1tI/IzpiZwaxWSretIDAjR45k+k+xE0yYNNgLkDuD3WkzWprVtTMq1ugePXrwoAaQwtKlS3VrCmkXr+6q4NrEZbO+OrhZZaflkZCQkJCQkJCQeCsRp+4OTAI6yZ07dy7bgX90j2AgMDIyEkoFxZE72oSGc+fO7dixQ3QC++TJk+DgYNWNqp9++ikgICA8PByRV65cuWDBglmzZkFrhfLToEEDKDarVq1SpYy+DgsL279/v4p4dQdXrlxRldYpoJyjGCEhIXTqAbXTPUFDMF/mCxcu7Nq1C4XBPwbRHj16BBUaCYoU5NmzZ/fu3asaC1ACEaiK6ULBXECsJu7BkiCQJhl0JVoVUmrpvrn5vjAJF8rz9OlT1ZkmwpkzZ7RWq7SA5P/999/EIFgtLZkh+++//06ePLl9+/bjx4/rSpojGMunZ4FCHj58eNu2bQcPHjTuGrQDJiWMbra4j17W9QXpwgwWe4jtwW5yVre5NKMyTpw4oUt9ioizuSVuqiwhISEhISEhIfHWICFSbBLvCMaNG5cnTx6+AqzFlClTVJeqJCQkJBII5AwmISEhISEhISEhISFCUmwS8YNt27YpitK/f3+DOGPGjNm8eXOcFUlCQkLCJOQMJiEhISEhISEhISGhgqTYJOIHffr0gYJavHhxNkCuwo4dO/z9/eUVYAkJiQQIOYNJvH148ODBqlWrmjdvvmnTpvguSxzh5cuXhw4dGj9+fIUKFd6s0RodHd2iRYt69er973//i++yeBLokT179gwdOrRbt26xlMXb2nTuw9Jw+O+//3bv3v35558b9NTDhw9/Mw1dn3X3799fsWJF//79W9kxYMAAzFG6JgL279+vm+zjx4+ttsO7CTkuJCQ8CEmxScQP2Ltc3rx5sZz//fffJ0+ePHr06Pbt2+fMmVOrVq06deqI3iElJCQkEg7kDCbxlmHBggV58uQhqf7ll1/iuzhxgV27djVt2jRx4sRUa4NL3wkQO3fupGIvXrw4vsviMezfv79+/fpUL8yisZTLW9l07sPScEDkevXqOe2pJ0+ebNy4sU2bNuxSBitmLQEVKlTInz8/PRo8eLD4bmRk5JAhQ7y9vTNmzNilS5d58+b9+OOPvXr1Sp06dfLkyUeNGqXizo4fP47Flz04vffee0OHDv3999+NXcNLMOS4kJDwICTFJhFvwHrJ3hhFlClThn1iSkhISCRMyBlM4i3DvXv33imKjYCB/CZSbM+fP/f3969Zs6auJ5Y3GqhXrFJsb3HTuQ9Lw8FkT718+TJz5syUrNZXDHDq1KksWbKIhhcuXbpUqFAhSlzlTh0/GzdujEdFihQRHXwTvv/+e8roo48+clp+CRFyXEhIeBCSYpOITzx79uy3334bP3587969hw0bNmfOnKNHj8Z3oSQkJCRMQc5gEm8uoqOjv/jiC1VgokSJ3jWKbevWrW8ixRZnWL9+/Z49e+Iyxx49eniQYrNUft1BEXvZJUBYGg7me6pcuXKULPvpVmHevHm9evWi/x88eJA3b15ErlKlysuXL7WRnz9/Xr58eUTInTs3IouPfv/9d8oIi7LTUr3RcEdW3ZdzCQkJY0iKTUJCQkJCQkLi3ULfvn0rVaqkCnwHKTbWySXFpsX58+fTpk0bx8dyPUixWS2/7qCIvewSICwNB/M9hVY1ptiuXbu2cOFC+r9Dhw4U2eCT1f79+ylOu3btxHA0PoUbOyN6C+COrLop5xISEk4hKTYJCQkJCQkJiXcIP//8M7RQSbHZJMXmGI8fPy5WrBha5g2l2KyW39GgiKXsEibii2JjnDp16r333kPMsmXLGsekg2yIfPbsWQ58Ryg2d2TVTTmXkJAwA0mxSUhISEhISEi8K1i0aFGSJEmgZeXMmfMbO3bs2EGPRIoNynanTp2aNGkyYsQIXes8r169Wrt27cCBA/39/UeOHLlr1y7zZQgNDZ00aVLr1q0//fTTWbNmQa/Wxrl3797s2bO3bNmC/5cvX960adNp06bx00uXLo0dO7Zjx47NmzcfM2aMowMvT58+Xbx4cUBAwMcffzxgwABtIQ04hStXrqCQbdq0QSHnzJkTGRlpXKmZM2d+IyAsLIzCHzx4wIHr1q0zXwXjFoiIiECOGzZsUL3lNNno6OjNmzf37NnTZvcLOW/ePKSMOiKQ49y8ebNy5crUMt27d6fCG1uOv3r1amBgYJcuXSASCxcu3LhxI3l+vH79+tSpUykFqPcU+cyZM2JboUicjkjcHD58uH///ui7L774Yt++fdpMV69e3atXL5Rw3Lhxf/75Z0hIiJnya5tOd1CsWbOGS3j+/HmKCXHiwODgYJPNZUaWHNXFGI8fP4aQdOjQoW3btlOmTNm7d++LFy90Y96/f/+nn37CKMCAHT58+K+//io2O8GYYgsKCkLxGjduPGjQoJMnT3qEYnv58mWfPn34JwpGMSFLxmlizqGY4p1HD1JsTscRIkycOPG3337D/2gN9B1aBoXR1tF8TILx9GgwgQPoffRs7969P/nkE8x7GIkY4ybfdTSlOC2S1Wo6miskJN4aSIpNQkJCQkJCQuKdANR+KFFVq1aFlpUrV64ZdjBTQBTb8uXLofwkTZq0SJEi+IuQbNmyqdSk8PDwmjVrDhkyZP369fPmzfP19UW0zz//XNd2kgioUp07d86RIwcUOShaa9asKVasGLQ+KLGsCkLj8vf3p6y//fZbPFJe4/Tp04gwffp0vAJ1EamhYFDkkidPjrdUeUF7LFCgAJT2ffv2HTlyhI69QEUUC+mIU0AWlStXRhbr1q3r2rUrIuTJk+fff/81qNqtW7eKFy9OqeFFMZfjx4+nSJGiVq1aTFYaV8G4BZYtW1a3bl3qLCjJqmIbJIveh9adJk0avIjy3Lhxo1y5clmyZHn//fe52BQzJCRkwoQJFIhXSE4MKLY9e/akT59+69atNrsvSDQyXmRa6ubNmx9++CFCSpUqRSFonCtXrjRv3pyyePToESfFxA0ElQ40EfD/lClTONqrV6+aNm3apEkTkkz0dYYMGTp06GBcft2mczQoUEg2n79p0yaKjKL+8ccf1DUQeDPN5VSWjOtiACSCAvfv3x9DKSgoCMMKiSdLlqxw4cIYVj/88APH3LZtW9asWfv163fs2LGjR48SPwVxxbgQE3Q0HF68eDFgwIDMmTOvXr362rVr27dvR1cia/cpNkhOtWrV+GfJkiVVDe4IkGqKibblQE9RbMbjCHJesWJFyghShHZOmTJl/vz5ib3CnMOtZz4mwen0aDyBY0RjoKE90csQKggq3q1Xr15UVJTxuwZTipkZ21I1jecKCYm3A5Jik5CQkJCQkJB4hwD9U3F8UbRQoUJTpkwhpejEiRPQ2BE4efJkjnb37l1oaHPmzOEQqPqkXy1ZssQ46+rVq3t7e1+5coVD/ve//0EHw7t8mOXixYtbtmyhBOvXrz9+/PjTp083atSoYMGC0Pcor+zZs3MKR44cQYivr6/IalHJmTMC/vzzT0pz7dq1HKjLKUDzzJkzJ+mlBHKemC9fPu3BHxG7d++m1Pi4FuH58+cozOHDh8XmMqiCcQvg/+3btxP9JOrDJltm7NixCIT2W6NGjdDQUJud8Grbti0Cs2TJwjHv379PBTBz87Fw4cJNmjQR64u2QhdwyMCBA0WKjbB+/XpHFFu2bNmg8+/fv//evXvQxsn+vdh3UPXx89ChQ/wi+rpFixb8U7f8jprO5mBQREZG6jI+xKUyxWbQXGZkyWlddPHkyRMMnKxZs/KxNaRAZQgMDEQxmLbYsWOHovEAMHv2bMXOtF66dIkDHVFsHTt2xLAVr2TevHmTfGpboth27tz572vs3bt3+fLlqIJIsaVMmZJi8mBxBDbH5uPjw4EeodjMjCOIZYYMGRCYP39+iMHjx48pmpeXFwLnzp3L75qPaTM3PdocT+Aff/wxwtmqHdC0aVOELFiwwPhdg3Fhskjmq+l0rpCQeAsgKTYJCQkJCQkJiXcIxhTbhAkTxECo+ghs1qwZhwwZMgSasHj/yGZXnBCtYMGCBvkuWbIEcbp166YKX716tWI/pkSMDyFTpkwIFJUxwooVK1QKMLQ70qtv3LhBIVDbSpQoUbx48VevXnG0Fy9eFClSxCnFdvv27RQpUkycOFHMlEgQYOXKlQYVBOiQSIMGDVQVRLilKhi0ACFr1qwqfdhksps3b6bAq1evcuC+ffsokHVp8xRbVFQUovn5+YmtDSkSOaNhw4ZpKTZufC3FljlzZvHQ3LVr19KnT6/YT8QQozR06FBVdyB++/bt+adB+bVNZ3MwKCAVuhQbuch0SrGZlCWnddEFjZratWuLgaVLl0Yg3QImYCwQIYI2VKVARwtFWdWl2Pbu3YuQzz77TPU6HUK0RLGlEJA4cWIKZIqNWxu4fPmycZrh4eEUE/MGM18eodhMjiNq6i5duojvojER2LlzZzHQZEzz06OjCTx//vxKTIqtX79+iv3yMoc4etemNy4szdj/x955gEVxdX18EQsqltixBGNEBTVI1Chq7CUajb3HqK8m1lhj1Fg+iF1RVFQsqLE37CVWRJAmgoKiUgUEVJpIk7bsd7LH3Iwzs8vsAgvi+T37+OCZO3fuvXPm7pz/3iKlmlL6CoIoAZDERhAEQRAE8QmhXmLjbXfw22+/yTirj0NoVKNGjdq1a8/7EAzjgYSEBFXXxfXgufPXkKysLJyryJ0ch/Heli1beIkzMjLAeO/ePWZhAfDjx4/RcuDAAdmHizQhqampgYGBXItQU7Czs5MpJUVu7SZMmIDJZs6cqap2yPnz5zH45A4O6tOnz+HDhzWqgpoWQHBWIDcelpitqIwSFRWFRhYzS5fYwCVw8NH48ePZcK24uDi4OkujqcQmFG7gLnDrAhWHv6tVq+bi4sLScIdZqSm/sOkUhSOxSfSlPOsiCi5bxtsWYO7cuWD8/vvvmeXs2bNgqVWrljCHzZs3Y0nYeDdR3+jZs6fsQ2Eayf9abC9evOjXrx+T2HJycmT/EhISoj7PgIAATFm6dGlmLBCJTeJzhD4Ajs09FycC9+rVi2uUmFJ696iqA/f29t66dSv33qHENnToUGZRI7EJnwuNemwp1ZTSVxBECYAkNoIgCIIgiE8IjSS2P/74A4wQa+F/nzx5IlOu4nRKBaq2BcjOzsZJQ46OjsKjONiBXUXxr8BkZ2enpiLR0dHW1taDBw/GAJitbzVmzBjZh6M5VCHUFIYPHy5TDuUTrZ2Hh4f6DOVyOUaqS5YsQUtUVBSEo6oWMlNVhTxbQFQnkpKtqIzy8uVLNLIdITSaKLp8+XJMXL9+/RMnTggT5F9iw7FUANwFhTIsx4lpwLhx46D8vPTFQWKT6Et51kWUZcuWyZTCHHcW8JYtW8D466+/Mgsu5Ne8eXNhDmzoIi5Rr1DhG6iJeHt7804vkO0OQkJCuBNFq1evjim5CpcoN2/exJRGRkbMWOA7iqp5jkQVJdE2kZJSo+5RjUyGgEtcunQJfKlp06aQ8ocffmCHpEtsmvbYEhskz76CIEoAJLERBEEQBEF8QuRHYsMg1sLCQtOLBgYGYmS1bds24dGff/5ZppxHxizqBaYnT56MHTt21KhR/v7+TN1gAXCnTp3gv9zV4lQh1BRQDhBuniAdXPkeIn+cS7tq1ao5c+ZoWgWFthJbntkWhsSWm5s7e/Zs2b907dqVt355/iW26OhoTLxr1y60QAUhSkejoaHh1q1bubPPioPEJt2X1NdFFG9vb0zPzX/RokVguXr1KrOAJ8g+XLCMERMTgzmwphD6RkREBFrAr3inF4jEplCO9WN/o3Aj7IWE7N27F1P27duXGQtQYsvzOSpYiU2j7lGNTAZ9jr29vaWl5e7du9PT0zGldhKbpj22xAbJs68giBIASWxEyQG+V5ydnefPnx8bG6vpufDqBt9G3AVBCd0TFxcHt4C7OrVCuXvX8uXLIWKBd4WiKljhUbJrV8KQy+VvVKD+9ml9IryJCk+RXuCkpCTeuXnu9sggzyzZ5Ediw6XTq1atyhZZl0hCQgLGVAsXLhQeXbJkiezDsTZqBKaVK1eWLl36wIED+F9hANy5c2f4r6iwxUOoKeBiahs3btSodlzgJQR3nMTBQY0bN3769KmmVVBoJbFJybYwJDYEUrJ9CQwNDbnrNOVfYoN3PEx89+5dZkxOTp4+fTr6LTBixAgp2zXoTGLTyJfU1EUVkLOenh74Ca4WHxISUqtWLZ7GMXPmTOHtRtjETDZMSegbbFeBa9eu8U4vKImNC47Ckwk2ZxCCI1WBrVu3MmNBSWxSnqOCldg06h5VdeDBwcEtWrRo06YNm62fH4lN0x5beoMo1PYVBFECIImNKAnA92vfvn2hj8bO+vnz5xJPhJeSqVOnNmvWDE/86aefCrOYhDjwJrd48eK2bdviZka8pVLZWiHsh+uSRMmuXQkDXrInTZoE0bKMQ+XKlUeOHIkTlwr8RHg0IMzo0qUL98Tz589LKa2Liwv3rEaNGk2cOPHVq1cSK0ueWbLJj8TGRrVcv35dmHNubu6tW7dUXdfIyEj24agTBo6JGDVqFLOoEphw9Ap3dSFhAIy5mZiYiOqA3GX+hZoCLpVlaWkpWgVvb++kpCRVFWSMHTtWplxIHp5E7kYH0qugpgUQoU4kMdsCl9igkePi4vDvzMzM9evXly5dGtufpcm/xMaGXCUnJ8N/ub2Zv78/hvfAkSNH8iy/ziQ2ib6UZ13UAGlq1aplYWEBzjZ69Gjh07d7927MTTj1kjUpW6BQ6BtMZ+EqWUhhSGzQIJUqVZIpt+9UI+JDP4NrgVWpUoX7PEqU2KCaatpW4nNUsBKbQpPuUdRX09PTcbsD7oJx+ZHYNCqSxGpK6SsIogRAEhtREoBXw0ePHuFeNjJNJDZ4q4M3m23btuGJJLEVCXK5PCoqCrdwkgkkNrb31pUrV4qqhIVHya5diQReEDt27Ih3rUKFCtHR0YV9ouLfxbCR9u3bSzll4MCB7BToG3mbP+YJeWbJBufptGvXjmeXIrFBcIsxMPizcC7bmjVrLl26pOq68CULJ+rr6wsHm+OS6idPnmQWVQKTubk52P/8809miY+P5wXA9vb2aNmzZw/v9ICAgLlz57L/CjUFGxsbtAg1RCg2d2dVNbi7u8uUmx706NGDu9GB9CqoaQFEGA9LzFaixJaUlIQW7qxDUd68ecMVm4DLly/juSycXrx4sezDlZuAM2fOYDIpEpuzszPYhw0bhv+Fm8jVa6AuODuYjX5SU35RiU30ocjMzMRM2GplSMuWLWUfSmyil5PoS3nWRRV+fn6jR49Wv1R8UFAQ7t0pVJ3c3NzA3qJFCzZcTtQ3cGdbqDLv9MKQ2BScRlOzey8cwjS2trZcuxSJLSsrC+oCTacqgcTnqMAlNundo6ivnjt3Dk/ndsszZsyQfSixqer8FWLPhUY9tpRqSukrCKIEQBIbUXKwsrLCblq6xIbAuwWOnyKJrQiBu4C3jyexKZS/9Kp5GfrYKdm1K5Gwrkai2pX/E+G1XsaBu+ucKCEhIdCn4VQ1YMGCBRpdDtGxZ3p5eensWgSugN6gQQP8LyqwEJihwxw6dIibGPxH9uGEIFxnHZg4cSLbFS4zM3PlypXq4+2YmBiU53hT56KioiCK452LAyiE+2nigugDBw5kFqbUsHE67969w5WtINutW7cyifnOnTumpqavX79m57IAj82JTkxMrFKliky5fBXTmxTKtZnMzMxu376tpoJcLCwsIJPPPvtMuNGBlCqoaQHu0TVr1miaLasyV0aJjIxEI6syfCmjNMNWb1Cl1EPY/MUXX/CO1q1bt3Llyky72bVrF2RlYGDAGj8rK2vEiBF4Ue4dUSXcjBo1ytDQkP04MWvWLN52Fnv27IETbWxs8iy/sOkUKh4KoE6dOmDnyrLQmOXKlQPj1KlTmVH0chJ9Kc+6iPLixYtatWrxtD9RcFPgmjVr8ib+T5kyhfeFInwcgLVr16KRt7MkSiqtW7fOswCoSAJSfluCjmjIkCFYYHBLYQJ4ya9Ro4ZMOZeWdwhlJplqiQ3uyMiRI2vXrq2mABKfozZt2ggVJegShd4rMaX07lHUV9lwgYcPH6Ideh68NHcYmio/V4g9Fxr12FKqKaWvePv27a+//grfO8KpzQTxsUASG1FygG8F/HbRVGIDMBYlia1owQEUQomNIIoVtra22NX07t1bNydCnwZnYaQH9OvXT336GTNmQAjx/fffY/oVK1ZodDnd4+zszN1UjihsWCC6efNmaHyIOVNSUiBqQiPEYNzEQ4cOlX24cSGEQI0aNcLEEI72799/wIAB4J/NmzdXP6AGOHnyZPny5cuVK+fm5oYWiAPBV01NTcPCwliytLQ0oYqBgP/jpcHP9+zZM2rUqMmTJ2Pi0aNHb9myBedJnT9/HrfDkynHjVpaWjZp0gS+6+/cucPNzc7ODtOEhIQwIwtWgbZt20Ik36FDBz09vd27d0tvZAcHB5mK9eCkVEFNCyiUtwBrxz0qsWV27tyJyXABLwSX2JP9u18ngsN5WrVq5e7uDt2Xqu0jcBodt5+Ji4szMDD4448/mCUiIgIsMuVgKGjG1atXQ+asnQcNGgQ+iSlx1CT0YFx5Bcpco0YN7gDJWbNmGRkZcbW53377DdLExMSoL79o0ylUPBRgnzZtGhjh/QRuJbTq+PHjwV3xofjss8/Wrl3Lrih6OSm+JKUuQlCGg6xMTEw6duzYp0+fIUOGwHvs8uXLeb9YpKam4oIDAwcOZE/xjRs3KlasuGrVKm5K0ccBntAWLVqgffr06deuXbt58ybcMtYJQKXOnDmjqpzx8fF464HTp0+rqREjJycHl5CrW7cubzvL48ePowQ2e/Zs4UzShQsX4oW+/vprf3//ly9fximB71BPT8+NGzfi9NJx48apubqU5yg3NxcFKTasEsHV98zMzJhFekqF5O5R1FfZqnmNGzcG74LnETo9uE3oqFARnOqrys9VPRcSiySxmlL6CuaEbC08gvjo0KnEBo8ffF/6+Pi4urq6uLjcv38fHk5h/5iQkODn5wdPMjz50F+8ePFCOBMBLNHR0d7e3vCqdPfuXUgvcYtrogRDEtvHDklsxEdBUUls69atY6EaBA+qEsMrbIUKFSBwwoEAsmIvscGLAQSTokvDEIUEvHrhhgBA06ZNAwIC9u/f/9VXX6EF/AdifnitAjeDWBRHeQPdunVji1InJSUNHz4cl9EB4Dt07ty5eepryLNnzyDgNzQ0/O677yCcg+gd/uWOmoFIuHnz5pizvr7+2LFjDx48yI4GBQWxlQ0hAsc1laAwaFm8eDF7aYR3SJYPAMEed5WiBw8eQAiNYzRkymF6VlZWbMYiBKI4TxOBxhEu966etLS0atWqBQcHCw/lWQUbGxtVLZCZmQnlxAEj2PK//PILRr9SWmbJkiWoMsiUYhDuFbh9+3ZjY2M01q9ff+3atXitS5cu4dsR3Ghuw/KAPqd27dpwaYjn7e3tIZI3NzdftGgR7w3/+PHj3NaGd3hoHPje79q1644dO9h6ZNBuUMh69epBxSEfiNghPu/Xrx93BT1gzpw5cFPgosuWLfvrr7+mTZtmYWEBkQU3Da/8GRkZqppOIfZQsNr16dOH3QuoF9yCMWPG1KlTB/wHQhUmWqlqrjx9SUpdhMDjxn5HEbJy5UpuYigkvCRDmRs2bAiPG5zYsmVLKDxLoP5xSE1NHT9+PBsZDS4EDgmtB1339OnTWRvygHsK79WovLA2Hzx4ME81U4WXlxeUs0yZMuAM/fv3h+4CsjIwMPjhhx/AeXiJHRwcunfvrqo1eKhf5C7P5wjC2AEDBuB/oXjQnk+ePAkMDGQ7MMiUsqOvry+EqBJTsqvn2T0qVPsq+A921/AvZBsTE/Pw4UPspeG+46YrwnPVdCkSiyS9mlL6ilu3bkH5odjCu0wQHwu6k9igc/fx8bktAF7XuANBQ0JChGn8/Py43+vwN7z2CZNBF5DnFtdECYYkto8dktiIj4KiktjgtZ6t5gYht6rEEB5XqFABoq+PQmJ7+/bt119/LVOx+jJReEBI46NE+j6zQjIyMiAKglcyCNI0PRdOuX//PkTR3HW4JJKVlQXnwqVZYAYWCPNEf22Nj4+HcFG7hX6ioqJUZSsFeC9VdUijKkinwLN9/fq1i4sLd4CVEHj3xngbHme4oR4eHqruaVpaGiQIDQ3F/8L7v5qcod+DkkOYAHdQeDQ1NRUvHRwcDCEA5CkaAkgpP0PNQwGFgXrhRRXKSZqiD46ay6nxJYl14QGNCW+t169f9/X1vXTp0tGjR3fv3g3fMtbW1v3794cXKtF2i46OvnPnjqjymyf4zLIBbhEREZqu8qkF4FRQYKido6MjNKBuNrkupMdTOnl2j6p8NSYmBpqLO/4xPDwcKsK9U9p1/vnpsRkS+woos/TdmQiiGKI7iQ2+nFAIc3Z2fvr0aVBQEEQLaGGLRyYkJLA0qH+zNNzBqPDgoRE6O/iSCAgIgN4ELcLlGAldcuTIkQkTJoxRsnTpUmb/9ddfISBE+8yZM7mnQG8Lt2/cuHEODg7w30OHDjVv3vyrr75i68VCAnh1GDp0aJcuXSwtLbt16zZ//nzR/bwKQ2KTePXk5OQTJ04MHjwYfxCGt+pRo0bVq1fPzMxs7ty5qlYTOHDgwIABA5o1a2Zubg6X3rNnD7y4cN+rtGhP6WWWXgwu8NCNHz++VatWxsbGgwYN2rVrl3a6Nnyv79ixo2PHjpCPhYXFnDlzoISiEhu8Cly7dg0uum7dOl4m0GNA1eBVctiwYcOHD1+8ePHKlStF3ylPnz4NLdayZcvPP/8cGgRuE1s/CF5E4B6N+RfWHcFr68SJE5lduP7O5cuXoQXgpsOl4TbZ2dkJx7TnmUZN7bCV4Lno3bs33J26devCczFr1izoAIUpIcQFD4GWxLOggnCPjIyMevbsyf2ZWjoSvQietQ0bNrRu3RrHF8ALE1QWrvvFF1/Mnj2bvQp7enr++OOPX375JdxueDRUvaTC98L06dPhNjVq1Khhw4Z9+/Y9ePCg0MG0e9yghNOmTQOXg5z79OmzcOFCaBl4ydOicYpQYrt48SLmoK+vL+oJEAaAq0AXAX/nR2JT5ZlaNL6apwBeBtj8oxo1auCzBp7DzpXoh9r5v5pugQtEv6tWrQKfqV+//jfffDNjxgzR6FRKh0AQBFEgwNdrp06duNPreEDvzdbkIgiCIHSJ7iQ2Dw8PVMHYD4nwLgvvvmjE93I2zI1J1/AVgvIZBPYYaMG/bm5umIy9DUdHR7sr4a4dQBQJT548wcn8vK3ZIZTCNV8h/EMLhNkQSkFshvEVBJ+bNm1iI4pxXR6c8A8ZXr16FX9suXDhAhxt1qxZVFQU79IFLrFJvPqkSZNwjQaZcpXQ/fv3V6xY0dzcvEGDBmiEMI93OXB4MEJT4AhNLy8vNokAsqqsBBdIlt6eGpVZ02IolA8jvLF17doVIl54VKGatWvXlilXUZWyRRQXnHYB17p+/Trkn5KSYmNjw5qLSWzh4eEQzeJWVjLBEqrgP3Xq1Jk5cyb+NPf27dv+/ftDMl70C87Qq1cviLeht4EqQF8BVZApF4ZgQg80FO6aBFy8eJGdm5WVhauByATb0llZWVWrVo3NOYLoGlpszJgx0tOor51COaS3Y8eOjRo1cnV1hTpmZmbu2LGjVKlS4F3wBxOe4EazvXTBjWNjY+G1u2bNmm3atEG31NfX5609lCdSvAj6W9xPCgFHnTZtWo0aNaC1cQlkmXLVEjh97ty5lSpV6t69O6RHZ4ZK8ca8QHU2b95cvnz5RYsWYf//7NkzS0tLmXJuGveJ1uJxA86ePWtoaDhv3jy4bmJi4vz581nJ0c/hZklvnyKU2KCh2PQxobyuUP5KAU6CLaadxKbGM7VofPVPgb+//6lTp3AaUdOmTU8pYXuYSvFD7fxfSreAXLt2DS63bt06T09PeOsYO3YsJAN/5k10ktIhEARBFBTQq/PeWHjAW5ZwKR6CIAhCB+hIYoNeHkUx3j5o9+/fZ7obRA5wFNNwhy0EBARgGhycAinxvxDR6abwhKZApCSUhIAePXpwJSFcXBm3KgP69+8PITrcX4hVIBjGmHDVqlUYenHzwbUzIUjm5V/gEpv0q7N1gk1MTEaMGIG+Cm4MESnaeTEe7qJtZ2fHLLh1uky5tTZ6OBu/LbE9NS2zpsUYMGAARKTcNzYIPjFxnvvKc4Gw2dTUtEKFCtyhqQrOllVMYktKSoqJidmwYYOoCDV+/HgwJiQkMEtiYmL16tUfPXrELOBgEPy3bduWOzjl/PnzwmKzDeB5L6x3795FO1diCw0N1dPT4wkcf/7555AhQ6SnUV87qFeNGjUqVqzIGyp/+PBhTM/dqD4rKwudQV9fv02bNmzRaOgkoZ3B3rVrV4UmSPci3P1dplxcZu/evazrZp7fu3dvyI25zd9//432Y8eO8VpGmDmbQli/fn3ucDNNHzfwtEqVKtWuXZs7UYLpg2fOnMGJOdLbpwglNoVy2ClmUr58eeHcNwsLC7bJmnYSm3rP1KjxpTwpQJMmTWRiE0Ul+qGm/i+9W3B3dy9XrhxvGW9Ufg0MDNha7BKrSRAEUVCMGzcOOqJOnToJJ6VC1zR69GjWExIEQRA6RkcSGwTV95VwF5oFfH192QTPzMxM/NvT05Obhq3OFhERoVDOJML/RkdHw2s9vCJDLErb+hYrcMlkoSSEe/TwJCE/Pz8MbL755hvhogC4Z5OxsTHXiC8W7du35yUucIlN+tVTUlLw0oMHD+bawXvRzp1slZiYiEae4oybmjds2JBXNo3aU3qZNSoGblguXCAWtziEyFb6ognr16+HU6ZMmcKzw2siloc3UZTZeaE+RPhg9PHx4Rp//fVX7vKoAwcOhDROTk7cNNDV4DZY3Nt99uxZvApPYoPc0M6V2I4ePSpTisLclNCJ/fDDDxqlUVO7CRMmgHHevHkKAbigb/ny5bmqEKTEfOCB4ibGQTeQWJiPGqR70aFDh/C6vG3CvLy80C7ctwuHR40fP55ZAgMDyyoRCkaurq6YD9dhNHrcFP/qgN26deMaocCYWIvZfEUrsWVnZ7NRY8uWLeMmg29GMLJFsvMzUVSVZ2rU+BKfAlUSm3Q/1Mj/JXYL8IJhbm7euHFjXql27dqF12KamsRqEgRBFBTwclK1alWZcmsF+HabOHHijBkzhg0b9rWSGzduFHUBCYIgPl10uqMoD3ijxWFrOOUT1+QSjmJ7/PgxpsH5X/ACzRQ3+IJhex1ApE1CWzFBI0no6dOnGK6wHay4wG0dMWIEmzeE4Jw+iMp4iQtcYpN+dfA9vPSsWbO4dgiG0T5t2jRmZIO/2HpzCISyaOctH6tRe0ovs0bFgBc4sNjY2Bz6ENTjgJMnTyokkJCQULlyZUgvukCS6FpsuMO3MNTHZoECREdHM+OzZ8/YpmOPHj2CBHXq1BFeCNIcO3YsOTmZWTSS2DCxnp4e7oDOuHnzpkZpVNUuNDQUjaK7bp06dQqPwis1M7K7xpu0u3TpUrRrtE6ldC+CZsT8eWvVvXz5UvSuKf69cVyNCUWT5s2bixaGzYvEX1kUGj5uQPv27cHYrl07rjE9PR0Tc1c5lEjRSmzcfD777DO2/DbQv3//Ll26sP/mR2JT9dxp1PgSnwJVEpt0P5Tu/9K7BXgVgZSWlpa8Ts/KygrzNDU11aiaBEEQBQh8L8yfP79p06YGBgbw+mRkZDRo0CB4GaOd3wiCIIqWIpPYcnJymFjm7++PRiaZsSAZXnbZem04M5QNfBPi5uamg61tiDzRTmLjTnxTRWRk5PLly3Hhns8//5x3tLB3FFVzdVVhp0JMNmJqzu7du7kp9+zZI1Ou+c3LQaP2lF5m6cVIT0/HJbQmTpz4PxX8/fffaorBYIOeRFdq10hi27hxI9orV668adOmrKwsXm44y+zbb7+VUjCNJLaUlBS2CX2PHj14g3Olp1FVO0dHRzSKbljOtCHuDVUlMeByLQDrVLVAjRepkthU3TUAV2rDlekRFNHAn0WvzuaS79+/Hy0aPW6Kf58gKD8vMa48uH37drW1F6HIJbbU1NTPPvuM13MGBQXBfy9fvszO0qXEphBrfIlPgSqJjYcaP5Tu/9K7hSVLlkBKc3NzVZ3e1KlTNaomQRBEIUGyGkEQRPGhaCS2zMxMppR5eXmx2PjVq1dML4ME/v7+bKtQAPc+Z8u3ARClp6WlxcfHu7u7o0Wj9XSIQqIwJLZbt25BuDhu3Li7d+/iKAZdSmx5Xl2jsDMiIgKNffv25aa0t7cXGhXaSmx5lll6MQIDA7F22m2/yAXaB7Niuyhw0Uhiy87OHj16tOxfmjZteu3aNW6CMWPGqBFueGgksSmUizThdhMy5TzZmTNnCnc5lJJGtHZsmIyqUTDVq1eHo9Bc7K26kCS2PL1Ia4kNvBr/C/0/CrgdO3YULcO2bdswqz///BMtmkpskydPxvT37t3j2nHKKs8ohSKX2IBly5ZhVvXr18fv0KlTp5qamnIDrSKX2BTSnoI8JbY8/VC6/0vvFkaNGgUp58yZk2dKidUkCIIgCIIgSjxFILElJiayLUEfPHjAHXsCscGjR494Y9NwGy8AF0dnu44+ffqUnZiQkMCmi+q+RgSPgpXYfH1927dv37p1a7bIji4lNolX1zTsZANzuPMlv//++4oVK3IdG9FUYpPeYhKLce/ePUzG3UlAOzC+BYTbmyo0lNgU/25DCaWV/Qucy7oUbB/hhGJRNJXYFMpBQ126dGGXrlevHm9VOylpRGuH21DIOOO2eLRq1QqOlilThlkKXGKT6EX5l9ji4+MxpdA/EbYO/erVq9Gi6eMGHULNmjVlSmGLjXTGOztp0iRp7fEBxUFii4uLK1++POZ24MAB+BKE/+7bt497VnGQ2BQSngI1EptEP5Tu/9K7hb59+0JK6VsWSOkQCIIgCIIgiJKNTiU2iIfDw8OZdhYSEiI6sDk6Ovrhw4d3796FECgmJiY0NBTT44pLbHopdw8duVyORm4EQhQVBSixXblypVy5co0bN+aOCNCZxCb96lqEnTY2NhUrVqxQocKyZcscHR1//PHH5s2bg9sLy6ZRe2rUYhKLwdbV2rhxozAHjWCj2Nzc3IRHNZXYkMjISFzUHJkwYQLap02bJlOuBMzdN1AVWkhsyOHDh+vXr49poBkDAgI0SiNau5UrV6LRyspK9KLm5uZwlLsQe8FKbNK9KP8SG/TeOIpNX1+fu18t49y5c5gV221Di8ctMDAQd6Ls1q3bgQMHduzYARWZN2+edit4aqSUcTfw0fpEocSm4EixZmZmcKPr1KmTmZnJTVBMJDZEzVOgSmKT7ofS/V96t/DLL7/IlKvdCSehq0FKh0AQBEEQBEGUVHQqsT179gyFMBcXF+HOcapg2x0kJCQolJGSUGKDwAyNHh4ehVJ0QhMKSmJLTU3FsSerVq3i2nUjsWl0dS3CzvDwcIj5t2/fvmXLFjs7uzt37qhaSVB6e2raYtKLgSPFzM3NRWVxuVw+adIkUX2EB85ClXFGJHHRSGI7fvw497/Qq2DdAZTjoTpqroU5JCYm4t8aSWyurq7cPRbg7k+cOBGT/fzzz9LTqKodrrMuU26zK1ryatWqwVG2FJSiQCU2jbwo/xKb4t/NNADRFf3wPurp6b18+RIt2qk8UJ2xY8fu27dv3bp1J06ciIyMVN8OapCulPn4+HAnwGp9YlhYmEyw+S90dPr6+pgh9GDQAfIyKXKJTeJTICqxaeSH0v1ferewYcMGTAmdg2hKJycnHGcqsZoEQRAEQRBEiUd3EltMTAwbv8bCWh4hISGPlbAt0iDax11HnZ2dMYCPi4sTThRli7ixnROIIqRdu3YQWpiYmPDsbdu2lWkiscFNx0M7duzg2ocNGyYMsRQFLbFpdHVNY35w9TZt2kjc5FF6e2raYtKL0atXL1W3SaGccCpltwrgwYMHmI+RkZFwbAi2FXejTIXqUL99+/a8093d3TElThh/8uQJZlilShXhWJK7d+8OHjyY/ffq1at47tGjR7nJrly5gnauxAZ/Ozg48DLEJurfv7/0NKpqJ5fL8aYDwonDERERYC9fvjzXzwtQYtPIiwpEYmONPHLkSGF5UK3g6olaSGxQDJ5Skx82bdqEBVCvlMH3l6WlJVfe0vpEPz8/OOvSpUu8lGw5wooVK/JuPTBw4EA8WlQSm8SnwMzMTCb4FUEjP5Tu/9K7BdafGBsbC9sWOk8oMA6Fk1hNgiAIgiAIosSjO4mNLanm4uLiIwDfX+Hdl+11kJCQkJiYyHZFwO1EFcrZpmwpt9DQ0OTk5JiYGFdXV7S8evVKZzUiVIGjDAA20Qnu2q5duwwNDVEa4M5mevz4MSZet24dLx+mevTs2ZMZIdSsUaMGGKtVq8ZL/+eff2J6CH40KjAUDweDjB07Vrurgx+Khp1QU7Sz2YsK5fruELO1bt0alxfME+ntqVGZNSoGW45Nppy9mJKSgvaIiAhoNAsLC94MNTUMHz4c8/nxxx+5I+bYkls9evTgpo+Ojkb77Nmzufa6devyBj1BsxgYGJQtW5btpfDzzz/judBWe/fuxaGv6enpdnZ2tWvX5u6OghPxZMp10NlIvcjIyO7duwtFCoio27VrxxvQhwovm9opJY2a2vn7+6NPcqUlZOHChWDnDVmaO3euqMSwaNEitMOdUkhDIy9iW8TyJDa2whqvXgC4HNhbtGjBNaJXlCtXjrfVLHwLgIfXqlWLWy+NHjfFv5vkOjg4wK2X2AjqYVsN8HyVCxQSB5Fxt4XV+kRUIe3t7XmJUXoTbWeALQ02f/58DaqnRJVnatT4Ep8CHMZYtWpV7BDkcjk8ehr5oUb+L71bwOXYgObNm3t5eaERinfy5EnwyRMnTmhUTYIgCIIgCKLEoyOJDV5eb6sFx9FA3M7dQpTh6urKXTGHOyCOi6+vr26qQ6iHTXODAAbCMwh+zM3Nx48fP2fOHLR37tx5+/btmPj06dNoFK4qDdE126MNoqylS5d+9913nTp14s7B+emnn9hYHjYrCmIzjQr86NEjPBHCJO2ufv/+fTQOHTqUmzNTpiDWZcbg4GDZv5QuXRoiRmNjYwjh4OrDhg2zsbFhozg1bU+NyqxpMVgQCxgYGJiZmUH6UqVKmZqaSp/3rVCqcg0bNsR82rdvv379+lOnTkG4DrXQ09NDe6tWrXbv3o3pr127hkbewJ+6det++eWX0Bswi5ubm+xDrRYKhjsDMKCaUOZy5crxJCGgR48emAZabNmyZaNGjYJLQDI0Vq5ceerUqajeomQDJeeeDg1ev379+Ph4/K+UNGpqp1CqVzg/d+vWrcx45swZKPzMmTN5YwC///57zOfx48dcO9MIuDtaqEcjL1qyZAkajx07xs3E09MT7V27duXas7OzcfZfmTJluL063Cls/yZNmjB3gm+Ebt26gZtxVyVTaPi4KTibbACVKlUyMjIyMTGxsLDo3r379OnTRZcFVENGRgaqhOgVhw8f9vDweKAEd+OBGweugm0I/saUl/yciPcXTk9OTuaVp0+fPvr6+jxpUqEUiMFV8HLwXGu66pwqz9So8SU+BUx5nDRp0smTJwcMGICj3aX7oUb+L71bePr0KXgLSwYdQsuWLeHewd/sK0x6NQmCIAiCIIgSj44kNrbjp3qJTaEc++Du7s49BEGIMKiIjo7miXEBAQGqlrIidM/OnTsrVKiAYQmESbt27YJwcd68eRCcQLh7+vTptLQ0iIVGjRrFgkCZciXyRYsWcUeaXL58uXr16ni0WrVqGzZsgLv88OFDnNcJ/0LOkGzz5s1MHwHglGnTprFBB2oAt4GYFodFIJDPypUrNbr68uXLGzRowHIYPHjw+fPnwQ4xYZ06dZgd4ka2lJKNjQ2OQRPF2NiYF5hJaU+NyqxdMY4dO1avXj2WAM7ljmiTTlJS0tixYw0MDDAfPT29kSNHvnnzRl9fv3nz5tD+qGTBMz5lypSqVauyK/bp04dFtqampm3btoWWnzNnDrTPggUL4G/wBN5YkoyMjJkzZ+KC+ghE46LjHF+8eNG5c2futcLDw6F28LeFhQWUio2lhYjazMysUaNGvXr1Wrdu3datW8F1wXOCgoJYbnmmUV87JDQ0FE6H9unQocMvv/wC9W3WrBncYm4aT09PJi7LlBPowDGg2GAHl2N2IyMjaCKJN0iKF4EzT548mT2/NWvWnD17NjzU0NtDAbh+0q9fv71790K20Ag4uxlp2bIldywe3LgtW7ZAPtAm48aNGz58ONRl4sSJb9++5ZZNi8cNbnenTp1U+TkAD4KUZoGqDR06tG7dumqy4oEDY/Nz4qBBg9jy+UDt2rXBwp3cDV9/o0eP5pbz0qVLffv2ZT0GAo0DfsJdMkwVajxT08aX8qQolJpXixYt8NxatWqx9RCl+KF2/i+9W4CyQYPjFZGOHTvyNoSRWE2CIAiCIAiixKPT7Q4kkpOTA4F9hBL4Q3R5dYVyNMTr168hBn758iVvuA1RHICbAkGOn58fkz5fvHghfTohIy0tzd3d3cPDg3tuZGQkhHBaiDvF5OrHjx8fN25cWFiYs7PzyZMn9+3bB1HZmjVr/vjjDwgXDQwMhGqI9PaUXmYtiqH4d+nD4OBgKfsbqAGjZe78buG6Y2pA5UUulwcGBt68eROyUuNdSUlJbkqEej2P58+f37lzhw2kgvyFS/tBM4JdoVyvCtrZyclJOEVdShqJQGGg5Ldu3dJ0BnR+KKrnDhrt8ePHN27cuHfvXkF17PA9MnDgQLgFvr6+Fy9ePHTo0M6dO21sbKytrWfMmNG8eXN9ff08HYPQAulPAbiZl5cXdHG8p7hQ/VB6t5CVlfXgwQMoiXBRNkWBPuwEQRAEQRDER01xlNgIomSzYcOGevXqqQnqrly58sMPP3wixSCIQiU6OtrExGTTpk2qEsjl8vbt2z948ECXpSIIgiAIgiAIouRBEhtB6JRbt27JxHY85OLo6Pjnn39+CsUgiMIGp4iq31C1bdu2WgywJQiCIAiCIAiC4EISG0HolBkzZsiUa7qLTjhSKJeH69mz58uXLz+FYhBEocI2Nt2xY4doArlcvnTp0tWrV+u4YARBEARBEARBlDxIYiMInXL27FmM+Rs0aLBs2bKbN2/6+/sHBAQ4OTnt27dv4MCBbdq00WhJso+6GARR2Hz11Vfo6kOGDMFNPAMDA728vC5evLho0aIWLVosXbq0qMtIEARBEARBEERJgCQ2gtA1e/furVatmnAPQRMTk2PHjqna36OkFoMgCpVXr1717t1b6Of6+vqTJk2KjIws6gISBEEQBEEQBFFCIImNIIqAzMzMCxcurF27dsaMGb/99tvmzZvv3buXzw06P95iEERhExoaam9vv2jRounTpy9fvvzUqVOxsbFFXSiCIAiCIAiCIEoUJLERBEEQBEEQBEEQBEEQRL4giY0gCIIgCIIgCIIgCIIg8gVJbARBEARBEARBEARBEASRL0hiIwiCIAiCIAiCIAiCIIh8QRIbQRAEQRAEQRAEQRAEQeQLktgIgiAIgiAIgiAIgiAIIl+QxEYQBEEQBEEQBEEQBEEQ+YIkNoIgCIIgCIIgCIIgCILIFySxEQRBEARBEARBEARBEES+IImNIAiCIAiCIAiCIAiCIPIFSWxEoRMeHh4REZGWlvXmzTvRT25ubp6ZpKRkLl/utHq1S3p6lg7KXOKJjk7evfu+g4OPbi734sXbc+eebt7s8fffwa9fp+aZPiAg9vjxRxs3ujs6BsCtL8DM373LdnOL3LXrvr29t7Pz8+xsuQbVyAtVHp5nFT4pirPvwc1ycgqzs/MCD3nw4KX6xBkZ2ffuRe3c6b1//wNf3xiNfCk5OWPVKhcvryiu8eHDh/Hx8dIzyScZGRlvVJCamvdDWrDExcU5ODjs27dPu9P9/PyWL1/+7Nmzgi0VQRAEQRAEQWgESWxE4bJnz56BAwdCzHbkiH///kdKl7aWyf6Pfb75ZveUKRelCBAQIeMpEPrqoNgllYCA2KlTLzZrZoeN+dNPZwr7iq9fpw4ceIx70/X1rX///boqqTQ0NLFnzwN169ps2OB28ODDoUNPVK68eutWzwLJ/PTpJw0abOKmb9Jkq7Pz84Kq7LRpl9q338PNn1uw6tXXffXVjp9/vnDgwMOEhPSCuujHQjH3vdzc3O3b74GzjRx56tAhv3Xr7taqtb5z530REUmimR879uizz9ZyM2/efLubW6TEsv3442k4xdbWg2t89uxZly5drl69qmlNtcPV1XXChAmNGzeWcahSpcqoUaPs7e11U4Z3794tXry4bdu2enp6cPX//e9/Gp3++PHjiRMn1q1bFwsPNSqkchIEQRAEQRCEFEhiIwoLCFl//vnn4cOHZ2dnM+O1ayEsIp0z52/puTk6BuBZV64EFUJhPxVSUjJfvUrZts1LNzLH48eva9RYV7q0dZMmW01Nt+nr/yewdu68Ty7nj158+jTO0HCVkZFNVNRbZpw79yqkX7Dgej4z37DBrVy5FZMnn9+503vzZo9+/Q5j4sqVV4eEJBRgrWfNusJKcudOeGxsKhQVPH/fPt+RI09hOcuXXzl16sXISHH5pkRSzH1v0qTzcGjZMidmCQtLrFZtbc2a658/f8NLPG3aJUgM+VtY7KxefR3LWU/P6saN0DzLdvSoP6bnSWyKf4bRvWnXrt3hw4e1qrQ2QEf97bffokRlaGj4+vVrnV0akMvlUVFRR48exQJoKrGlpqY+f/580KBBJLERBEEQBEEQxQGS2IjC4pdffunQoQNXX1P8E1DlliplheHltWshGmXo7R3t5/eqQMtYfOHNICtY4C7o6VkVtsyRmZnTsuWOH344GhOTjJaMjOw1a1zLlVuBDrBu3V1uejhqaroN7LwphOnpWbVrbwD7mTNPtM7c1TWiceMtoaGJXOOmTe6YeN68ghw3dOrUezm4YUNb4dGoqLdz5vyNCapWXXPxYmABXjr/xMamChWlAqR4+t7Bgw/xfmVl5XDttrb/DJ5t1cqeK8kdP/7I0HDViROPmeXhw5ft2r0fvWhkZPPmzTs1ZYPmhTTYCEKJDUhISGjcuLGjo6MWFdeOpUuXokTVsWNHnV2Ui1wu105iQ/bs2VOoEpuXl1dhZEsQBEEQBEGUPEhiIwqF1atXly5dOiAgQHiocuXVGIt6eLzQfcE+Cpydn3furOWaRBIpW/bPwpY5du70bt9+T2ZmDs/u4OCDDtCy5Q6hvXz5lWlp/Hl8qEk1bryFLXelaeaDBh0TKke5ubmNGm2GxN26/aVdHUX5++9gLANkrirNoUN+bNL0kSP+BXj1/CCX5/bufVDKOKz8UNx8LydHbmxsC0Yrq9u89AkJ6Tj87a+/HrDE9eptvHCBv+ZXenqWiclWzJyrBfMAB4aC7dnjg40gKrEBN2/erFChwpMnKvMpWDZs2IASVb9+/XRzRSGlSpXSWmLbv39/4Ulszs7OnTt3LvBsCYIgCIIgiBKJTiU2CGgjIyN9fHzgPdjFxeX+/fthYWE5OfwoKCEhwc/Pz83NDV5t79279+LFC+5y+IGBgf5qSU//5BY5Km7AnS1duvTvv/8uepQkNvVERibVqLGuQweHQr2KDmSOzp333b8fLXqoadN/FuQqVcqKq6Y1b74djL17HxSmZ/OL2ZgvjTLPzparGjI5YMBRSDx48HHp9coTKRIbYGPjhsnKlVsREBBbgAXQmoULb0B5SoDEppF7sEnooj0SLq739dc78b9OTmH9+x8RzfnYsUeYz6JFN1QVbMmSW+hs6iU2wNLS0tTUVDfbDpDEpgp4Y6lRo0aHDh0KNluCIAiCIAiipKI7iU0ul/v4+NwW4O7u/u7df9NqQkJChGn8/PyYyubh4SFMwCUlJUVnlSJEadWqFUQ7T58+FT1KEpsa3r7NgGAeGudjl9jggV258o6qo6NHO6IPvHv3fh5xaGgiWhYuFJEnYmNTuQt4aZq5GnBqqnBQUn6QKLHJ5blt2+7GlAMHHivAAmjHoUN+WJiPXWLT1D1w5wE9PSvh8EnFv8uuwScs7J9ZxpcvB/n4xIjmHBQUr15ic3EJb9BgE+50kafEtm/fPuhFra2tVVe0wCCJTZS3b99+/fXXkC1JbARBEARBEIREdCexPX/+HCUwZ2fnp0+fBgUFwdswWh48eD8HJyEhgaV58uRJYGAgSxMWFoZp8pTYdPOzP6GKq1evQkxibGysKoF2EltOzj8DkcaPP8tbREmhjKgvXQocOvREly77LS0dunX7a/78a0lJ/OWQkpMzTpx4PHjw8W3b/llY59mzuFGjTtWrt9HMbNvcuVdVyTEvXryFGLtjx70NG9r26XNo4cIbzs7P377NkF5yLnfvRkAVWrWyNza2HTTo2K5d97kjNJ8+jWvRYjs2To0a68aMcYTP7NkabAohsSkUOhlJpIaJE8/B1T//fBOz7N3rixXfvVt8x9iKFVfhXFEtMlfFvXtRenpWv//O30hB8Y+3JP/www9mZmbXrl3LMx8eEiU2xT/SwAO2Un5U1NuYmGRwRbzv8Hnw4CUmu349BCrF7LdvP9e0SIq8fG/FijtskcTu3f/CC7m4hEvP/+XLlGXLnMDxevQ40Lbt7pEjT6laZq64+R5uMmtkZCOang02zHM+b2RkEqaE2yo8+ubNO7iok9P7L7I8Jbbw8HDoSCtXrvzmTSEujYeokdj8/f2XLl1qYWGhUP5Otm3btlatWhkZGfXs2RO+prW7HOSzY8eOjh07wtcE5DxnzpykpCQ1Etvdu3fHjx8P14X0gwYN2rVrF9d1FR9KbCkpKWvXrm3dunXdunX79OljY2OTlSWinL58+XLZsmVdunTp0aNH27ZtR44cefHiRW4CeEtp0aIFZlujRo0xSmbPns1NAy8bq1atgqvUr1//m2++mTFjRnBwsHZtQhAEQRAEQZQMdCexMWksLi4OLWlpafCOjkYcyMaGub169X5V+/T09Dt37oAFXrLxrTpLjIiICDxRZ4vXEKqAIA1ikilTpqhKoKnEFh7+ZsaMy7VqrcezeIJIRkb2998fKVPmz6tXg3FJ8gsXnkGyZs3suLtSTpp0nq10vmaNK8TAFSuuMje3x+gaPj17HhBe+uzZp4aGq+bNu5qZmZOYmD5//jUmiEAt4CNcvEkV6elZ48ef7dp1/6VLgT4+MVAAXMK/b9/DbHF0f/9Xp04FQKgP9qZN7eBv+EjfQVViUyBFK3N06rRX9uEmoXCLeVNBebCFrlJTMzXNXBRoE1PTbXv2+Ige3bZtG0bXjRs3Vp+PEOkSW1LSO7Yi2969vgrl0Da4KcKmyMrKmTnzfROpKrMq8vS9nBy5o2PA7NnvN2FYtswJfQ8ePYmXuH49pHz5lQMHHouLS1MoB2N26/YXZGVj4yZMXKx8Lz4+DWvNpoLyYLt/5ulRt26F4bRf6CuER4cNO8HNIU+JDfj888/BA21sxLW/AkRUYrt69Wrr1q3RXrZs2djY2E6dOtWsWbNNmzblypUDo76+Pnw7a3qtN2/e9OnTp27dutevX8/IyEhJSYEKNmjQQHS7A3gBGD9+fNeuXS9dugSvB/v3769duzYk69u3L1d5ZBLbqVOnzMzMZB/y7bff8rZJhUuXL19+4MCB+Dby9u3bbt268Zra398fcjMyMgJ706ZNTym5cuUKS3Dt2rVmzZqtW7fO09MT3j3Gjh0LKStVqqTLfSoIgiAIgiCI4oaOJLacnByUwFxcXLj2+/fvM90tNzcXjmIa7m/UAQEBmCY+Pl40c3hHR6kO3nSFK7sRuiQzMxNCF4g0HBxUznPUVGJLSnoXE5O8YYObqMS2apULClJc47ff7gPj/PkfjD9ycgrDHExMto4YcRJCa4Vy2NekSefRfufOB2N2wsISK1VaXbv2BrbEPtCz5wHZvyua3779nLdDpRoGDDjaqpV9Ts5/WbH1xaZPv8RN2aTJVu0mikpvCkWRyhyxsallyvwJBcCZd8jw4SdF7wID58+y+XoaZc5DLs89fvxR9errIDdo7XPnRGY0e3t7Y3z+/fffS67Ze6RLbEDDhraYeO7c97uaQtlE1ca7dyO0k9gk+h5bSkzTiaIZGdmGhv+MMYSSMyM+bnAj8EHjUqx878mTWKx11677RU+Bu4AJxo3Lo8CoUU6efF54yMHBBxyYu12pFIltzJgx4IHdu3dXf938o2oUW1ZWVo8ePVBNa9Omzblz59D+5MmTChUqgL1r164aXSgjI8PU1BTOZcPSkbVr14pKbAMGDGjVqhX3a/3atWuYcvr06czIJLYvv/zS2to6JiYmNTX1ypUr8F9hvaAMhoaGYDx+/L8VGJ2cnFBJ5L1mNGnSRHSiqLu7e7ly5c6c+cAlLC0tIbGBgUFkZKRGzUIQBEEQBEGUGHQkscFL7X0ljx8/5tp9fX1RPouNjc3MzMS/PT09uWnY6mwRERHCnOVy+b1793BuKa3CVuS4urpiSKNmep12E0Vfv04VldiGDj0BRmNjW64RgmEwtm+/h2tMScnEHHhr24eEJKCdNwUVA2beXpOnTz/BxAcOPJRe+DNnnohONKtT55/BRPr61q9e/ee6Wkts0ptCUaQyB6qlq1d/oLbjoCf4eHqKe4WlpQMmYNMnpWfOxd7e+4svNrPRiPixs/MSpnz06NHZs2dFZ5mpRyOJDW40Jh479jRazp59KiqxeXtHayGxSfc9rSW2x49f44ls202FUqFGo3CjiWLley4u4VjOPn0OiZ5y/fp7OfKHH46qyTkjI7tatbW1a28QDmELDIyvWXM9/Ms1SpHY5s2bB31pmTJlCnsPHzUTRbEMgJ+fH9eOg7bKly+v0YXWr18vOsb59evXQontzBnou2RHjvA3l6hTpw6qfmy0O5PYli9fzk0ZExNTr149POTk5IRGeAlBy19//de3h4WFiX5ziUpsubm55ubmwvGtu3btwkxmzpwpsUEIgiAIgiCIEoZOdxTlkZmZicPWgLS0NHhtxTmhvFFs8EKMaURXOQkPD8ejoaGFu0Q3IQUIWjDG8PFRqQJoJ7G9efNOVGLz8YkZMeIkbzYlTrVr0mQr1/juXTbmMGvWFa49O1uO9mnTPhhNhjsJtmv3gTiVnp6FiZcuvSW98GzS3KFDftxPy5Y7MLeTJ/+TnrWW2KQ3haLoZI74+LTq1dd17ryPOzYQ6NPnEDaFl1eU6IkdO+7FBP7+rzTNnAccjYxMOnDgITY1fAwMVkifFJknGklsXbvux8STJr0f/VSwEpt039NaYgPgcZg69SJ3Du/z528wN8iWl7hY+Z6n5wss53ffiUtsN2+GikrzPKysbpcqZQW3nmfPzMyxsNgpvGVSJLaVK1didxoUJHW2uHaokdh+//13PMRbEm7p0qVoj42VuhluQkJC5cqV4RTRRdyEa7GxyZuHPqRly5Z46ZMnT2JKJrEJJ66iqAeMHz+eW/ipU6dyl219/vw5Jjt27IONR0QlNnhFAaOlpSWvYFZWVpiJqampxDYhCIIgCIIgShhFJrHl5OT4+fmhOubv/36Ehbe3N1pevHgvviQnJ7P12oTrrGVkZKAq5+rqmp2d9+6BRGED4RDGGAEBAarSFKzExiMyMmn5cidczoy34L0qiU3xT3QHodH//e9/57jGr776R4MQLoJet+4/mW/ffk9iydPTs8qU+SecnjjxHFxC9MONzLWW2HioaQpF0ckcEyacNTXdxpafY4wZ836fR1VL7LduvQsTxMQka5q5KjIzc5i099tvGm9roAqNJLamTe14om0BSmwa+V5+JDYuOTny8+ef9e9/RKZi7f9i5XvBwe8HsfLGqzIuXXo/UfTnny+oyjkwMB4qtWuXyE4d8+ZdFdXmpEhsbEFANzeRJe0KEC0kthUrVqCdfVnnyaFDh/CU8HCRZ5wnsaWnp5cpUwYsEydO/J8K/v77/VYwanYUjY+Px0PffPONaKngVeT8+fP9+/fHZJAV96ioxLZkyRIwmpubqyrY1KlTJbYJQRAEQRAEUcIoGoktMzOTTRH18vJiU7FevXrFNgaFBP7+/qigIc+ePePlExwcrGYOKaF7rK2tMVB5+lRkfSukkCS2W7fChgw5Pm7cmbt3I3DoVj4ltsmT36/Rdu/eB+OqcOMFnlENEH5jPhL3Ic2/xJZnUyiKSObYu9e3QYNNERFJwkNwW7GVVG3vgFKUnp4Vd0EriZmrISnpHTqkqnmCWiBdYpPLcytVev84nD37/pEpQIlNI9/Lv8QWH5+2apVL1677bW09fH1jipXEpso9UlMzwamgPG3b7hY9kS2Np2rgKrStmdk20Z1Prl0LqV9/Y0KCyDRPKRIb06QuX76sJln+0Y3ENmvWLDwlI0PEG3kSW2BgICZ++5a/VYsQNRIbUK1aNTj02Wef8ezx8fGrVq3q2rWrra0tvG9Il9hGjRoFxjlz5uRZMIIgCIIgCOJTowgktsTERDc3N5TGHjx4wF3qKDc399GjR7c/BLfrAngLJMvl8rt374L9zp07tMtBMWHr1q0YqPAW1ONS4BIbBPPt2+9p3XqXn9/7KYQFIrE9f/6mZs1/1LTevQ+ymWUoc7A5fVK4dy8Kr/vo0eu8U+dPYpPYFIqikDmcnMKMjW1DQhJEj546FYCttG+fr2iCKlXWwNFWrey1yFw9U6dehJybN9+uxbmiSJfY2BYcBgYr0tLe94QFKLFp5Hv5kdjgAbG2doZ7tHq1C2qgbKJocZDY1LuHmdk2KE+DBvxnBNm82QMrcv48/zcehXLIHvQPCxfeED2XbQ6b5+eXX0SGyO3YsQO7U/imk1xXbdCNxIa7NwBRUSK/T/Aktnv37mFieCXIM2f1Epu5uTkcqlevHrNkZ2dbW1tXqVJl9erV+AbCJopKkdj69u0LxiFDhuRdZ4IgCIIgCOITQ6cSW25uLls6DQgJCeGuucaIjo5++PAhBBXe3t4xMTGhoaGYHuzcZHFxcWjnbaFAFCFHjx7FQIVN4REiXWJ7+TKFjTpRJbFduRJUrtyKxo23JCX9N/+rQCQ2hXIQEO7I2a3bXwcOPNyx4x7kOW/eVchKfcl5tcDrbtzoLiW91hKb9KZQ6Fzm8PaONjHZ+uxZnKoEUVFv1YwVghqpundSMlfP1q2ekHP37uLzBLVAusTGdrOdMeO/YUoFKLFp5HtaS2zZ2XJoPTgRHhBmLD4SW57ugXdBX986I0PkucZtT+AjHIwml+eOGeMICVTlPHXqRejuRD+YJzyw+N85c0QyYWuxCUdwFyw6HsUmOu+VJ7G9fPkSE2/cuDHPnKVIbGxj1uzsbPgbLDt27GBpNJLYfvnlFxwWp8VeKARBEARBEETJRqcSG8QJKIq5uLjExUmNh9l2BwkJH4xBYOPdXr+WNDiI0AEPHz7EQOXoUZW770mX2Pr3P8KifVGJLTU1EwearVr1wQ6SBSWxAZDz2LGn9+3zXbfu7okTjyMjNZuHiFSsuAryNze3F9WUIVCHID8n5/1AOe0kNo2aQqFbmcPP75WJydbHj8WfU6ai4p6hcNOFaW7ffo73Dv7QLnM1WFndhpxXrOAvlK41EiU2V9cInKJYteqauLg0Zi/Y7Q6k+57WEhtu02lgsIK7jUAxkdikuAfbM9THJ0aYpnPnf0R2+Jdnh/acPPn81KkXRXN+/TpVVLBjYDeofqLonDlzoC8tV67cu3dSlxfUDt1IbPb29njK6tWrhUeF2x1UrFhRplzyTIXryidNmoQD2NVLbFWrVoVDmzdv5lbWwMCAu36rRhIba66zZ8+K1tTJyYmXD0EQBEEQBPGJoDuJLSYmho1fS0xMFE0TEhLyWAnb6gtegnHXUWdnZ+5sUHjnhpdpzI02Oig+wH2pVasWxB4QhKhKwxafUi+xXb4cVKHCShamikpszs7vlRfu8Blg2LATBSKxwbV4ipV29Op1EC8tGlEvWHCda8dpa19/vVOjS2jUFAq1MoeqgDYzM1Noz5Nnz+KaNrV78OCl6NHz55+xAu/d6wtFAvcQahMLF94QnSUqPXM19O17uHz5lS9eiCz5pJ20IUVie/IktkGDTZAGbgRPN7x69f3pR4/6c+1XrgRpIbFJ9z02V5cn7eVJly7/bIpas+Z6rjEgIFYLiU3U97QWmCS6h1yeCw8IFGn1av7D/vZtBpb23Dn+4pK//npl4sRzogUGBx48+Lj6bW2lSGzjxo2DvrRr1648u+hF84NuJLYHDx7gKUZGRsLxXyixTZw4kVl69eqF6W1tbYW5LViwgNnVSGzBwfA0yUxMTNgCcF26dAFLzZo1uckCAgJEJTYzMzMwfv3111yju7s7JjY2NuY1i0L5GgPp09L+E80LWyElCIIgCIIgig+6k9jYkmouLi4+AvA99cmTJ2yvg4SEhMTERLYrAm870dTUVLQX9lZrhKZAjASxxw8//CB6FKJZHLkDn7t3VW5ScflyEISg/fodZpbo6GQ8izsti4kRPXseYEY/v1c1aqwDY7Vqa7l5JidniEpsmZk5aJ8w4YMhCXv2+IDRwcEnPT2/s4HYkljwsbK6nZLyXquKiEgaO/a0hcVOKANL3K3bXziyCUN0aDEpQ+c0agoI0fX1rcEOV+faoRi9ex8sW/bP5cuduHZ40OrXr1+mTJnFixdrVPHQ0MS6dW0gt4sXA3mfs2efWls7V6++jq3ED/U1N7eHUh08+JCbybt32fXqbQQ7d99VTTN/+PClk1MYGyrIcHWNgJzt7b159sDAwJYtW4In9+/fnyn+EmEL5Isu7wXutHv3fRxcVqvWel6lFJzxX+D/TEwBH8DJmJoOuJPuey4u4bxZpeHhb6SoOe3a7eE90XArZ8y4jEY7Oy9uYk19b9SoUaVKlTI1NRXuKK0ejdwD5UUTk608XWzbNi+wW1o6wGPItS9adKNJk63nzz8TZg7e27Hj3mXLPqiFECkSW9OmTYU/V5w/f75y5cpNmjThLU6aH3CLTMDS0pJ3aO7cuaIS26JFi9Cu0V5Dw4cPx7N+/PFH7m9jUCm09+jRgxnZcmyAlZVVSkoK2uGKY8eOtbCwYKK/Golt8uTJYIcejFnatWuHidkKd1CSGTNmoNHOzo57erdu3cBYtWpVLK1cLo+MjFT8uxwb0Lx5cy+v9x4OR0+ePFmrVq0TJ06wHLR2YIIgCIIgCOJjREcSW3p6+m21xMbGQjJ4h+ZuIcqA92be78CvX79mYpxuqkBIBAIJPT09iElEg/PTp5+wgH/UqFO3boXdvx/94MFL+Li7R16+HLR2rSsEqMLg/Nq195O5IA5nxsTEdFwFH6WlpUtvfffdoU6d9k6ceA6NP/984aefzjx//k9wCBdC49ChJ7hFYhpEly77ufYxYxxZUStVWm1kZAMRuIXFzu7d/5o+/ZKbW6RGzTJ37lWWm4HBCjOzbcbGtqVKWZmabuNOEgQgOMdkkyadP3ny8YABR4WzI4Vo1BSPHr1GY7t2e7iZsEaGD1dYHDFiBIt1b968KbHKL168hTqyDEU/vFXeoWANGmyqW9cmKuq/MWXYdDzNQqPMExLSUdZp2tTu+PFHzDOvXw/5/PNN27Z9oAEha9euZVVevny5xCorlBLSuHH/LXLv6BgQEpIQEBAL7n34sB/cAkPDVehRM2Zc5t16Ro8eB/B0uINQcXhSoE3YbNnKlVdPnXpR+t4OEn3v7dsMFP7q1NkARd240R2eFJ60JArzWPDABQuuw9PRqNHmLVs8sc3hb2trZ/hgYo187+nTp+wudOzYUWJ9FVr5HrYSV+ALDU2sXn0dtEZ0dDI35YoVd9TnDG0rOiiSS54SG05drFixIk/bat++PTbIwoULpTeIGnJycpjqZGBgwFPuvv/+ezzEW/OUaUzOzs7SrxUREdGwYUM8ESqyfv36U6dOzZo1q3PnzvCtgfZWrVrt3v1+d1cm8GHZzMzMjI2NUbHirjUBrw2YZsyYMcnJ728WPIlWVlZVqlQ5cuSDuefLli3DxHBowYIF06dPb9So0ZYtW/T19cEIf1sr4SWeNGnSyZMnBwwYgGodeKaRkRErW926dVu2bFm5cmX4e/v2/zZO0dqBCYIgCIIgiI8UHUlsCQkJUiQ2ID4+3t3dnXvIw8ODvTQzIPwQHd1GFAdw5zgfnw+mszk4+OCqRtI/wcH/iAh37oRPmXKxatU1zN6nz6Ht299PALx8OQjCYLRXq7Z2wwa37Gz5w4cvcXoX/Ltr131IBpEzzsvDz+DBx3F/wKVLb0EIzewDBhx1cQnHnENCEjp12qumeDY2mo2gPHbsEY7Gwo+h4SruqCJGXFxaixbbMU2tWuulz9qT0hQBAbFTp17EoW346dHjwMqV70dFJSdnYA7t238gfxw+fLhs2bIYKK5cuVJKYd69yzYx2ZrnLRZO4ouPT/v++yO1a2+wtnbeseNev36H4W9Hx4D8ZC6X5/bseYDZjY1te/c+aG5uP336JfQxIdCxfPbZZ1jlPn36SKkyMHq0Y7NmdqKFgdv9+eeboGFnzbpy4sTj1FR1s25fvHjLfVjA4cPD34CrwN8WFjvhfj15EiuxSIhE34MGZ4NMR4w4Cf4gJXO4HYMGHeN6FK59BjkwNe3161QtfC8nJ+err77Cu1C6dGmJEyS19j24L1WqrBk48Ji9vfeyZU5QHrihPBl03z7fPHOGHPIsZJ4S2/bt0AnIfvvtN559zZo12BqXLl2S0hpquHnz5tChQxs0aCDjYGBg8N13323YsMHT03PIkCHM/vnnn8+bNy8lJQXsAwYMYHYjI6MFCxZIv2hSUtLYsWPhKni6np7eyJEj37x5o6+v37x5c+heQkJCuOmPHTtWr149djlDQ0PuiDbG1atXu3fvXqZMGcjQzMysW7duNWrU6N+/v3CQ3bt37wYNGsQy7NGjB6qH7IeEdu3asQVe4+LiWrRogfZatWpdvPjf0ntwCPJhHSOKaLy9X7VzYIIgCIIgCOLjRafbHUgE3krj4+MjlMAf9Fb60fHq1avatWv/8ssvurlcWlqWu3ukh8cL7nTLyMgkF5dwoYggnfj4NAiVnZzCfH1jLl4MPHTIb+dObxsbN2tr5xkzLjdvvl1f31qiBsHl1auU27efBwcnCCctMqAiXl5Rnp4f1EgK+W+K1NRMuK7woYOYFkLfVq1aHTx4UPTEgiUoKP748UcHDz6Exle/bLx0/PxeHT3qv3v3fUfHAPg7z/FZ0BEFBQWBG0+ePLlACqApz5+/uXMnnEk8UGAchKg1UnwvOjoZfF7KNhE8wsISb9364ES4iqtrRGBgvMQcVPleWFjYoUOHvvjiC02LpAXv3mVfvx6yd6/v338H8wav6RKUZkxMTLhLejH8/Pw+9k1+srOzHz58ePv2bfiyQMvTp/zV7rhAMkgcHBzMXZJVCDQXNM6NGze8vLyEq6RxAae6desWV4CDnF1dXQMD+T9pZGZmQm6enp6ii1FmZWU9ePDA3d1dzeV06cAEQRAEQRBE0VIcJTaiBADhUIUKFYKCgoq6IFoC0bWJydZNm9xVJZDLc9u336NqJfUSSXx8/JdffpmUpM2eqh8vHTp0oAUfi5ylS5dKHD5ZMrC1tS1Tpgxb5Iv42PnUHJggCIIgCOKThSQ2orDYvn17u3bt0tPTi7og2oBTRNUvqNS27W5NR5l9vMB97NWrl6OjY1EXRKcsXLhw1qxZRV2KT52LFy927tz5I+1JtCAkJKRatWoXLlzIOynxMfCpOTBBEARBEMSnDElsRCGyZcuW3r17a7ohY5ETH5+Gayrt2HFPNIFcnrt06a3Vq110XLCiIikpqWfPnmfOnCnqguiUyZMnW1lZ0UT1osXBwWHEiBGfztjJkJCQZs2anT17Nu+kxMfAp+bABEEQBEEQnzgksRGFy4ULF3r16hUVFVXUBdGMr77agSrbkCHHDx/28/B4ERgY7+UVdfFi4KJFN1q02L506a2iLqPuyM3NTUxMLOpS6JqEBKlbdhKFxyd1F9zc3Pr06UN7+JQkPikHJgiCIAiCIEhiIwqduLi4j+43/FevUnr3PijcK1Bf33rSpPORkR9ZdQiCKP5ERESoX86fIAiCIAiCIIjiDElsBKGS0NBEe3vvRYtuTJ9+aflyp1OnAmJjP7JJrwRBEARBEARBEARB6ACS2AiCIAiCIAiCIAiCIAgiX5DERhAEQRAEQRAEQRAEQRD5giQ2giAIgiAIgiAIgiAIgsgXJLERBEEQBEEQBEEQBEEQRL4giY0gCIIgCIIgCIIgCIIg8gVJbARBEARBEARBEARBEASRL0hiIwiCIAiCIAiCIAiCIIh8QRIbQRAEQRAEQRAEQRAEQeQLktgIgiAIgiAIgiAIgiAIIl+QxEYQBEEQBEEQBEEQBEEQ+YIkNqLkExcX5+DgsG/fPu1Oz87OdnZ2nj9/fmxsbMEWrAhJT0+/cOHCsmXLirogBPEeeMqmTp3q7u5e1AV5T/4f/OJWo0+B3NxcNzc3uGsJCQlFXRaCIAiCIAjik4MkNqLE8u7du8WLF7dt21ZPT08mk/3vf//TNIetW7f27dvX0NBQpuT58+eFUExdc+bMme+++87AwABq1KhRo6IuDkH8Q1ZWVo0aNcAn69atK5fLi7YwBfLgF6safQrcunVr1KhR2ObAixcvirpExZqkpKQ3koHEwhwCAwOPHz9ua2t74cKF+Pj4/BQmIyPDy8srz2TBwQlr17p6ehbMnU1Pz3rz5h33k5mZI/Hct28zeOfK5bkFUqpPBIm3MinpHa+d8ZOSkinxQq9epcyff23Xrvv5LnJJIDQ08cSJx3Z2XrdvP09OzlCfODY29erVYFtbj/37Hzx//kZ94pwcua9vzMGDDzdv9vj77+DsbHVfefDo3b0b4eDgAyW5di0E7jIvga+vL3Q7UmokBfj+ld7XqeruCpDU1FRHR0cbG5tCvUqREBwcvHbtWk9PT64RmnTRokXwTSH9RUg0H4L4uCCJjSixQG8eFRV19OhRjLi0kNhevnz56NGj1q1blySJLSEhwdvbu2rVqiSxEcWKFi1agE+2bdu2qAtSYA9+8anRpwC8x4eEhHTs2JEktjzJzMyUaUKzZs24p0dGRg4aNIiboFKlSlu2bNGuMP7+/t26dVMjsUVHJ8+cednEZKtM9n/wOXUqQLsL8Thz5sno0Y7Vqq3FbOEzePBxKSc+fRrHToFP48ZbJk06/+YNXyYghGh6K2fNutK790E9PStug+OnXLkVxsa27dvvWbLklhoBCHLA9F5eUQVdm4+JyMikLl32cxuwSpU1e/b4iCbOzpavWuVSocLKKVMuHj7st2jRDUPDVRMmnE1PzxJN/+jR6zZtdjVpsnX79nt79/paWjo0aLDp5s1QYcrc3Fy4qJGRzZAhx21tPeAqkBhKsmGDGzdZQEBA586d79y5k/+KK5QvvfD+/8UXX0js7gwNDQvkukJOnTrVu3fvsmXLwlWggoV0Fd0THR09c+ZMExMTbECoJvfoihUr0H758uX85EMQHxcksRElHLlcrrXEhlhZWZUkiQ3p0KEDSWyE1kgZcqIpycnJ8AaWlpZW4DlrR/4ffN3UKDY2Vpddk44vpynLly8niS1PQkJC2Nfi6dOnfXx8YmJiXn6Ig4MDpilduvT9+/8NAoqMjKxVq1b79u3Xr18PaX799VccEw0cPy5JouJy5cqVJk2ahIWFqUmTkZEdGZm0YMH1gpXYkLi4tEqVVmPOenpWwcF5zy+eMuUi0ynatNmVk0NjVKWi3a3cu9eXNfi9e1Fv3ryLiEhydY2wtfVo0GAT3rhRo06lpooMbduwwQ0S6Otbw3ULujYfDdBoVaqsKVduhZnZti+/3MKVLJcuvSVMP3jwcTi0e/d/T/3169Bj/F/HjnuFIz0h87Jl/2zWzO7t2/fD4rKz5V277i9VyurChWe8xCtW3IF8jh17xCy5ubkzZlwG47p1d7kp4YumVatWly5dyk/FuWRnZ5ubm2NPBd1XaGgot7uDLhF6uXXr1lWpUqVs2bIFdVEe8fHxHh4eFSpUKGESW0ZGBnwvLFiwQFQa279/P9r9/Pzykw9BfFyQxEaUfEqVKpUfiW3NmjUlT2KDb3eS2AjtcHZ2Lklvh6r4KB58uVzeu3fvGzdulMjLaQH7wZwkNjXcunVLT0/v+vXrqhJAzMmm3K5evZp7yNLSkjdg7fHjx+XLl4eUFhYWGhXDycmpcuXKAQGSdBYPjxeFIbEBHTvuZYrD1KkX1SdOTEwvX35l2bJ/YvoFC1S2IaEKTW9laGgiu0G8Q1lZOT17HsBDI0acFD3d2fl5eHiBzTr86EhLyzIx2frjj6cTEtLR8ubNu2nTLmGjlSplxRvfZ2fnhdoxL59hw06Aff78a1xjSkqmsbEt2C9fDuLaHz9+DcbKlVdHRyczo5/fKz09q7ZtdwtLaGCwQl/fmieSRkdHN2jQ4Pbt29pUW4zZs2djnzZ9+nRVaRwdHaFvLKgrivLVV1+VMIkN8fDwUCWNubm5BQUFiZ6lUT7S4f4sRBBFgk4lttzc3MjISB8fH1dXVxcXF3gAwsLCcnL4P4kkJCT4+fnBAwmB3L179+BFGU7kpUlLS3vy5ImnpyekgacR3vBSUlJ0VQ/iI4MkNiEksRHaAX04xN4dOnQo6oIUOh/Fg79w4UIooc40Lx1fTgtIYpPC/v37R44cqeoovHH17t0bm/Hbb7/lLqBz/fr1P/74Q3jKrFmzcLyb8I1OFfD6Z2houGTJEonpvb2jC0li69fvcO3aGzBzCPVjY1PVJF671rVChZUjRpzE9CtWFMxctk8KTW9lXFyaKokNj5YubY1HAwPztSYg8upVyrBhJ0THxH2M2Np69OhxQDjWkg3G5KpmmZk5tWqtB6O9vTcv/eXLQWAvW/bPiIj/xgNu3uwBxjp1NgjDtDZtdvE0602b3FUpoa1a2cMhZ+fnPPuRI0dq1ar18uVLqbVVCxvjrEZigx6sSpUq0vsxLfj6669LpMTm7e1dIKPP8p/PuXPn1HzBEYRu0J3EBm9pPj4+twW4u7u/e/ffGhYhISHCNH5+ftzuOy4uztnZWZgsJiZGZ9UhPiJIYhNCEhuhBW/fvsW3Q5LYigOHDh3CEupG89Lx5bSDJDYpWFtbQ+yq6ujGjRuxDSHUjIiI4B66detWZqaI9LBnzx5IX7VqVYkFgBfCb7/9tkGDBunp6RJPKVSJbdy4M02b2mH+y5c7qUqZnS2vX3/jjBmXf/nlAklsWlOwEhtgbm6PRw8fzmMmmhTg/k6efD7/+RQTLC0dnjwR2RQ7MTEdG61Ll/3MePDgQzSGhSXy0r97l62vb817QBo12gwWeHyE+S9ZcgsOlS+/komVKOo1a2YnTNykyT/L87m7R/LsEPo1bty4e/fuBbJlkBSJDfD09BQqhgUISWyFmk9gYGClSpVGjBiRnzIQhQfEEY8fP+aOkUpN5f+sBa8Zz549A0+4c+eOm5vbgwcPRLdUwuFWbEgWnJKRkccuLrpEdxIbRCkohEFDPH36NCgoyNXVFS3QdpgmISGBpYFWg+eEpWFLdWRlZbm4uKDx4cOHoaGhjx49YmdJf10jCg+41xs2bGjdujUGOV5eXoMHDzYyMvriiy9mz57N7hE8YD/++OOXX35pbGw8atQoVb9TgavA12HLli0bNWrUsGHDvn37Hjx4UNX3H3wN79ixo2PHjpCnhYXFnDlzkpKS1Ehsd+/eHT9+fKtWrSD9oEGDdu3aJcxZTaR9+fJlOAtqN3z48AkTJtjZ2R04cEB6Q0G3smrVqj59+tSvX/+bb76ZMWNGcHAwOxoeHj5lypQxHCBBYmIiBDk//fQTWsaNG+fr6yvM+fTp02PHjoVG+/zzz7t167Zt2zbeglBcie3169fQUM2aNYN7BK8yoiuSQrNcunRp6NChXbp0sbS0hDznz58v3HcpOTn5xIkT0CBwRfgv9HdwZ+vVq2dmZjZ37lyumM4F/GTatGlw1+D+QmssXLgQnmXohUUTS7llapBYkbi4OFtbW3wHAs8cOXIk3CNwV+5vm3kWOyYmBmrNbh/r6K5fvz5x4kRm582DKNjHJ8/mkn7LoN/G9fuBGjVqYOGhSCwBdODQmP379x82bBg8EYsXL165cqX0rQajoqIgtm/Tpg0vhvf391+6dCnOQYMHHMoJ1YEG6dmzJzS4xMyBiIgIKE/Xrl0VSp+fN2+eqakp3NYhQ4YcO3ZMmF7Ngw+tvWzZMnChHj16tG3bFtzj4kWR+WWqaqTdY8JjxYoV2LMB8Nji7YAvR24aNXdf0+5FyuVUIaW5tGuTgIAAeJRMlPTu3fvq1avSJbYjR45Ap40VAQdj9l9//RU6T7TPnDmTe0p2djb0HuDe8B2kUP5U3qtXr7p168Ithi70I/qRD260qjdR6KbKlCmDbSj6XIjy+++/Q/pZs2ZJTI+r88CdlZheUcgS208/ndmzxwfzr159napl3U+ceKynZxUSkkASW34ocImte/e/8Ojx449EE0gnIiLJ0HBViVm4DTr8NWv+n73rgLPp+P6PFawSvUUPokUQvYUQokSUSFNCIoIgRQlS/PXoUaN3ESR6CYKoS1ZbRA3BYvW2WCyb9/96h2PMLW/u27dFfvP9+Pjsmzt37typ53zvmXM2WV3NnXu4RLHRadCUKfub5i9ceAyu4n/6uX//BWr2YcOCjJl//XU/XcUflNKv30ZK+emnvWLOY8euYFplyDDI1HIQQrKjtcgGXik2CHixEP5bU2wxVw6kUMh1uFdTbPETkIpNbaQuXHj8GQAaGWRXYx5RQXZ7xJgNGzZIebZs2QJhMtZfyxyxR7Ft3bqV3h+6K6VA5+eGJgGazdzOnTtHeaBPUguiuUk3QDdQHvFcd2hoKCWi82LtjTSMCAoKgt7reoQDBw60bdsW2jj0kNKlS1Pi+++/jz0MsnXKlCmhqiE/CfTPP/+8pIiix4cPHx4YGNitWzcaEtC7ypUrh8yvvvqqUe+9evXq66+/DoVn9erV0B9u3LgxZMiQ7Nmz03Mlig1DC8on9G2oTBh4kPgzZcqEbLVq1ZKChVtp2j179kybNu1ff/1FP5cvX54kSRJoZYpttWrVqgIFCgwcOHDbtm0YulDqXJ64bL/++ivnwVt0796dnp4mTRrmdyZPnoyUjz/+2BjXHJVEa0OpJsb5zJkzeEdkhqYqsjBMsUGFxotnzpy5QoUK5E8HWLDgiW+SqEadOnXQTdBgSf5YsgQKxoMwc+KMa9myJVqASkCjoUmTJ09etGhR7gL0tbEdFi5cmCJFio4dO6L3sWJ26tSJx8+zHqCdKad6l1lB5UXmzZuHBgwICKAKnD9/Pm/evFwlpsMUq42nfPDBB5Qu0gqRkZHQ3il94sSJlOjf6aPSXI66bO/evZB4smTJgvT8+fP/4sGKFSvoKkYXRhFe6t69e27Pd6o33ngDOaVN0RTTp0+vXLlyggQJ6KHMp6CbOKxn4sSJsfhXrFgxQ4YMJUuWpGqjm1SCjs2YMaNUqVJUTsaMGbEZoVUx2tlNO4Cmls6GWE18LC+4t169erSX4U2xHCEbVhuvb+S0za2AqmKhYM8y3333HXXHiRMnKINK76svL14fZwOV5vKtTVCBZMmSYchRNXbv3o1epvHpUrNiwxSj6QOdR0w/ePBgqlSpkI7dhFKwAWEiUyBmYPTo0WheajceQsgM3cDrQ+MzIJVhMaTXwZakeBcGW548ecqXL6/4jRM7O/YjPAKboFWeu3fvDxy4uWTJ8bly/VCmzMQBAzbZO/BaseLIe+/9UrDg6Hz5RjZu/Ct+Klbe/Yhiu3PnHh8X/fHHYNOcZctOrF//gapvT7FFRt7/4Yetr7wy5YUXRmbNOhR3IZtEH8ycuad584WoKv4hMyVevHirTZullIh/48c/4U7o7Nkb33+/qW7d2e4HstDFGjVm5Mz5g1iBEyeudu68qlKlKa++Og0PbdFi4e7dDk7Yqdx+7dpt1LxmzZlEZgUFhdaqNStz5sGlSk0YPdo8Bo7TrjTCnmKLivo3ffqBVgdF0ReLFh2sV+9n/G+8d9euMLwmhk327MMwcpo0mY9Wbd9e/spo3/I7d4Z16bIajeb2mHr17PlH/vyjUGCjRnPFM5UirlyJ6N59DW7B8KhceSr+RsM6eqhfUKjQaDSaaLJHU+Cll340zf/GGz+R+zY6djp27HZq9oULTdoWzSKZhZ46dZ2cGCZN2mft2odmE1gNUCzKtKJHof25PEJa9MkvrxQbdA1TG21sMZ07d65UqRI2r7Jly7Zo0YK/mErA60ybNq1Ro0aQkbAqQuCcP3++VHORYoOA9OGHH0J+y5EjB3ZJ6Djqr6PyLMXKX7t2bebMmTVr1qSQNZBFISpAosOWSh+9jIDACf0FwliuXLnKlCkzYMAAKx9qEHch/b777ruobXTKgRyClLp16+JFIBKjtsgsim379+8nfg1Ae9J3skGDBomFQFyH2IMSsmbNCiENfxs/sWvEECAhMO2zZ8+eo0ePBgcH089NmzaR7oBRTUoxAIEKeZCTGTQWSpGZbbCkomIiGptviCWKDXOA3lz66L1jxw7m3dCsZJ6G/0U7C8wZykPWEMymicYRkAsp8dgxkyjRGrEM1sReeuklaGvcm9CjKL1GjRr9+vXjlfG3336jdOk7Ve/e2IxdnTp1EhP5qFq2bNlEiyGoi1hboXFJscmwBFPhEsWGZbpYsWLi6gxx33T3NdW0MdKgP0s2Dqhww4YNVZoIGxhUSonJIvYQaj8GuZhOVAWAu9yeBahq1apNmzY1Fnv69GkopdgURZu1xYsXG9+LKLa0adMiM8/KI0eOpEyZkjpOLJa+ImIXFxOxYRt7Z926dfSsfPnyvfPOOzRJUWHueokQQWfhiVD+aW0lMM2E9hEntXqXWUHlRaCZQ/6AtuzyxG5/7733sI7v3LmzRIkSOXPmJJrSUbUhslC6ZLlDgqNLoNgI/po+is3ltMteeOEFl9lBUWIcLl9+HI8Poky6dOn27fNuVgAREJIl6/YiIQXhrFq1ai4PmwYhbNGiRZR+4MABCstFVmn2wEKBDRgSFc0vjHk0BSRRLBqYHc8++6xpR5hOfNyCUeF6MngitWHixIl5V7J5I7fzNrcCepzyG7UC9cmivrzYPM4Kis3ldt4mM2bMQGKbNm3ERAw5RxQbgNXAZaDYABp1TLFhpkNKYRM5PKVjx47nz593e/oaqwSlQ0kwPUf5tOCTTz6hF8FaZ2VHLAEtAxUR6pOi9SWA5RGPwA5odcu5czfKlZtUoMCorVtPQZkn4ilz5sGmvMz163feemvum2/OXrXq6PbtZ4YNCwoM7Gv0y24DotjcgpXN888Pj4qSjaODg0/j0qZND07O2lBsf/11vlixsfi3a1cYCkH1Pv8cS/T/5c49fMOGJyjpkJCzCRP2xCVUXkxfsuQQFU61cnus56pWnUaZX3hh5JEjlzJkGER5AgJ6hYc/MEhcsOBAokS9WrZcTGTNmTPhefKMSJasL5pFpRG83o53adFi4TPPPIzzMHXq7v79N6KpS5YczwzXgAGywZSjrrSCPcXWo8c6utS06XwxHYOhWbMFqVN/T1fFKJbuB1pJFPouSZI+Q4ZsuXIlAj/Xrv2HPPfXqDHj6tWHI9O+5X/9dT+fUc2RY9g//1wpWHA0/kAiRe3MmHGQkTtbuPBg/vyjxowJRg3RvFWqTKXhsWfPOZWHUndHH1hd8fooc/Xqh1189uwNegpawPSWVq0eDnuy8uNZgM41Zg4LC6erH364iBP5ICoGEqZqRERk48a/oo9MSToCVlT6AANRJ1ovrECxFS1a1Li7QaJLlCgRdiLiYs6cOZMnTx6IH8YvBAcPHqSzEVDyIbocPnw4R44ceNxbb70lyopMsaEE7I/PP/986dKl6bMuBEtFSxHFZ3mtPAShFi1asOXy1KlT+/fvHxgYCHGLI95AjZKefu7cOTwdEs7WrVshZmBzxF6cOXNmys/UGETltm3bQg6k9FGj5DPCiuW4PYd+KleuDGmNBBVg0CBMClft2rXx+pQSEhKCW6jakFHpQyAEeC5k4cKF2PHHjBmzfft2tADZH+TOndtrqFMNvwDCEnE1GK6Ugk7fsmULJUJ+c3vYXubXmC/eu3cvJbKCj2lCKdAFKAXDfseOHUEexJPjorFEseFtd3jAJj+EXbt2URtduHAByyj9vW3bNjEPe2cjnyDoA/opGkdg1ZBM5DTiEOyyZ/78JyQe7ASU3qxZM+mWjBkzIh1aOqdgBib2wNinWDGpnNatW3MirbZiCgFaEGUWKTbsOkgxOqOhlR1bHdtRui007dmzZyMF2ql4O4bxm2++adomIiDZYCPPmzevlD5+/Hh6kMTcoTJkK4GNGSvOsGHDrPSfevXqIRuUVTERMwtbONI/+OADTiSKLVWqVBKd16pVK6qDeDYeezYpXWJOdKLLE/tcTLxx4wbd3qBBAzEds5jSBw4cKKYTnQQpQUzEsKHM4qlbR11mBfUXqV+/PtXB9NiserXdnk2d0iWKjY3hJWbHL9NHvbmcdpkVxZYvXz6k79y5U0zs0KGDul0PRCt6oqR4d+zYkdIlMYgMPyELKpYPUczl8cguHejDBk/lZ82aVXy06cTHFkaJ4vdY7PqUKMncVm/ktM2tYMV5OZos6suLDxSbenM5ahNkxpjHixi1EW5zRYqNgrsZKTYaLUyxEXjOShoa2q1mzZp0yeqbf/wHr1QJEybcvHmzyi2QbitUqODymO726dNH0Ud4t27dXNbhRylGYcaMg6SwAw0bzjHyMlFR/1arNr1q1SeMIwYP3uLo2CBTbFeuRCRP3k863cZ4771fOMyiFcUWFhaeMmV/VF7iQTp0WEH8CNMoBOJ0JIoNoGowxXbq1PUdO86kS/eAycItaIr9+y/89tvf+LtixcnuB+es75B9kOgw/ocfHriiL1LE3CJJhPrty5YdphfPl29ku3bLb916oNzevHm3bNmJSEyd+nvxjK2jrrSBSLGdPXuD/u3de27hwoM1a84ku6o2bZZKdoK4C9mo5Y0UW+fOq5A4aNAT4/ytt+ZS5vLlJ0VGPhjMXlv+7t375cpNosOVGB6bNz/0XTh//gFT2nHt2n8SJeq1ceNjshXVpggDhQqNJuswrw/1C9asOebyeEbjz3gYnFTnRo3mmt7SseNKykCvWb/+z/QT1TNmRu/TVcxQMZ0iJNA/DBjMPvsAI+5Hn59FrxS+gSm2xo0bHxQQEhICSa9Ro0bG3S08PBxqCNJFrxQ//IBp6ypSpIiYE/tapkyZXn/9dZHhIkMBYN68x0Ee2EoAchR/g1y2bBnl7Ny5s9cXUXyWeuX56RDk2rVrRx/poQVAMHZ5nGyKFsrYfyEkYAsWD/e5H8zrhlQIU2NXr16FuMXNLlFs6uW4H+0alStX5hSMW7Irl4wViGo0HhRdu3YtxD/R0AcvSMJzoUKFYjTAhQbh0KFDxNWIH+Mx+yiRLBggkRpNppibw2ylFAhjlBKf/YPFakRRCdD82asa5jNmC50JlazYIKNLnBqn4I/Q0FC0OFke7t69O0ZdVGoogjWxP550MoX5Q+lfffWVdAvpOTVq1OAUIj4KFy5s+gikU1FEvGK6kimKqW8moy82Pqk080lg1zFuh6aaNmkjCRIkGDlypPisNWvWeGkdtxsjHPdCaJCe3rNnT3pQwYIFpVtmzZpFlz755JPAwEDxswwDWzUyQIs2XoK2iU4RD6hbhTtAm9CDeCFze05wY7viI4EEOv/4wgsviIm3b9+m2yWnPJADKL1t27ZiOu3fZcqUEROxYlJm0UGSoy6zgvqLIJvLQ9+YLinq1XY7p9j8Mn3Um8tpl1lRbFQHlH/mzBlOxIaq7nWeghK6DIQUuXkCpOPAaGdKl+QzK7z55psuz0FR4yVqLmDLli2caHVQFM9t06aNyEEjA+WUDAmt3shpm1vBivNyOllUlhebx9lDsbkctQl1vShtM5yGO3BEsUHGoMLHjh0r5adV3aV2zjce4vTp02nTpjVdwUyB7aZ69equJ1G/fn2VZ2H1QGarz1FklGSMOcC2XSIvM3v2XqT89tsTp9GhsVPOQoWU6E6m2NwP5uxDRqZ06QlinjNnwhMl6sWcnRXFRpFG+/WTfRTevn2PzKlKlhwv2seRl3cjxZY27QCRYiO89tp0emhIiHx+k49eik2xYMFDloeIMBuo386GTm3bLhNL+OmnvZQucoiOutIGIsVm/Jcv38ilSw9b3btlS6iRYtu373xAQC/0iPhqO3eGpUs3sGvX3yn/jBkhfMmm5d2PBgMKDAt7wgdQ3rwjkE4niwno+gIFRklDC0BjGhvE/qHRx3vv/eJ6ZJVJWLfuH3pikybzTW/p3n2N2JiVKk2hn0ePXjZmjoy8T1cxyKVLaFuy0cO/NGkGrFnj5fgRffK0UgfUwVyPDaTdjQ8tijZ09BELEM+LUBRm6UMgNBQywZsyZQonEsWWM2dOSaShzahChQpeX0TxWeqVZ/FSkj1++uknShefRc2I/6Vakd8Vl+GA5+HDhyldotgclUOvXLp0aTEniTQSKWlKsUVFRRUoUEC63f1g6rU1rbNGTABy4FUPmBqGhhUUFESUDkmJd+7coTyi2MzHGemramRkJP0kiR2lIf/169djwZGiI8QZxXb//n0+Xrt370PPl8xKsnAcHh7OB3fZGhCNyDkZWErYWFQjbmHFEWAOULqRIyBXU+JnbSLRoOeYPqJLly5U1NSpU92C4Y+pbyCJYouIiCCj6A8//PAjC4gbkqmmfePGDT6RVK1aNck80x7ffPMN7ipatKjV06XTTwSyUAM6duxoWiydgqxUqZJKHawoNqiO9BQb46PQ0FBsivT62MzES1Z6stsiriuJFChKykznNMeMeehV12mXKcLmRYhie/bZZ01vVKw2wV8Um/r0cdRcTrvMimLjKIRotGHDhvmwGjul2JySKTYUG8VDdD0pB6tEFMVGtnjxYj5rScuR1zdy2uZWMOW8fJssXpcXq8c5gk1zOWoTMssVzTYZcUWxAXQSOXv27CrPjVeATMUsc6lSpUTLCPu7MCXXrVvHg8elpqiQW8AWLVoYL124cDNZsr6mdjGmPvLLl39gQDR27PaZM/eI/1Kleng88NKlW25vECm2EyeuUthEiX3o3n1N9uzD7t17KMGbUmwHD16kRPYzJYLNqcSTm44oNtSTzJqMhUNR6dRp1Rdf/MY1dHsOJNITT53ycuZX/XZmuyQn+sxkLVny0JmU0660gUixHTt25fDhS7t2ha1c+fegQZtLlBhP6cWKjd2x44zxXn6WSLERE1qp0hQxZ82aM1Hg2bM3aACgZL5k0/LAp58+IMgSJ+4tpRNHVrz4OE75/fcHhmNIl4brhx8uokq2a/fYat7+odHEzp1hCRP27Nz5CbNrDHiX2ZFbBgUJZf6Ro0ygU4yZ79+Poqu5cw+X0j///Le8eUc899wQyoCajBlj7v2QgLXC5XHy4Pg9nwRTbCjwrABsFiEhIR06dDDubp6p0emLL74QV0UW6niX2blzp8vs67jbs2tA9hONpKzCHdAxC0kWNUL9WYqVd3sCfFEixB6xQLbxX7JkCaVcuHCBfHTs3y9PXqswBfxRTaTYnJYTFBT09ttvS86maPuW5CVTig3d6vJ8AJO+O0JMome1a9fO2J4aMQfoCNeuXWOTKVMvhBjJ0LU5WiYGBo3t8PBwSvnzzz9PnjzJNNGGDRviVSj5uKHY7t69y0dE6Rg5pbN9IIAMe/fuFaNFUAegfdmD2+bNm7Gg8DleFPVUu0H5z8BnjoBdgGFIkJZo9T1n9OjRVFTv3g/EGlZlTQ9gSxoaf1FR9DVjpWljxSeX2C7P2av27dsres0kxz3Y9lQyM/g8V7ly5Uyp+saNG7usSUkJvlFsa9eubdiwYbNmzTD1yPgrmhTbxx9/TPmDg58QsMh4mxOddplXeH0Re4pNsdqEWKPYePo4ai5/UWyQ4d5//33XI+TPn9/Gl7kp4pBiW7NmDRUlflC1p9guXbrUr1+/KlWq/PDDD9itKGd8oNh8myxelxerxynCa3OptwlPhK5duxofFIcUGx2ZBKgBmzdvXtoAUyd3cQ72WJo8eXKV+CRG0OEjGj9eMydKlMhl8KNHYMspY2xBIy9z48bdgIBeiRL1+uijRVb/TpzwHglHpNjcj6x78I88zbsf0NaR6dINHDLksYmrKcX288/7KPHvv02Melau/JuuDhz4+HCiDxSb0SbIiNu3702fHlKmzESb+vh2uxXFZuwdR11pD3tfbJMm7STHZxgMkrc7twXFli/fg2Zv3PhxaKlNm05myTKETrlWrDgZV1HmnTsPiQn7lrei2Ogu0ZTyq69WuzwGklbDdeTIbdLtKt3tFFFR/6IO9ev/LDkc5Aihb79tfiagU6dVlIHCiVD4Ufw7cMDEkBz9TldLlZogJlarNj1//lHnz9+8dOlWnTo/cc9OnWoeQACAtEzLi2gN7QO8+mIrXry4/e6GfWr69OllypShcni1pDModevWVamGFcVGsmjatGntb3f0LJXKu60pNiPbxUZwxr5wRLH5UI6I/fv3Q1QgT69SlDlTio3ESGzBVt8dpQNJGjENMYgB/jY9MMTO9wFo3EwWsccwU0juj+IQcUCxoWmYFIPAKho7oIn37dsnNRaHliAvd0eOHKGfISEhRGdCnGUbQiMdrhH7iD5HAH2Mclp9z2EX/v37PwguTuwSYOooVNLQgoODKbOKI3a3raaN0Vi5cmXXI2TNmlX6xmKKWrVqIbNiYAQGNEaOZzd06FBjBtIJpQOPVnBKsUErLlu2bIkSJdhc3C8UG5o0Q4YMLs8hR/7ORvtry5YtOZvTLrOB4ovYU2yK1SbEPsXmqLn8RbG5H4UAhpbOMwL3qpuzxSHFdvDgQePMspr46PFevXqlSpUKiw+9HUuQ8YFi822yeF1erB7nFYrNpd4mUAwop3GuueOUYqNFA0I//SQ9SoIUSSY+AAsRcV7A5Mm+e3p6/fXXXR7/nvbZ7t69S88y1XIp4EDy5P3M6inzMn/9dZ5MYKLpIUSi2HbtCmO1/+DBB65gJ0zYkSJFv+vXH3/AM6XYvv764TG6nTuf8PZIYP5CZHb8TrGdORPetevvr702fdq03faUn2+3q1NsjrrSHvYUm/uRYzX8y5592O3bT9hgGik2ZDBGmahUacrYsQ9lnvff/1Xsfbf/KDby9da7t4k/EyNijmJDc5UtO9F4fPjatdv04ni06Y2tWy+lDGQwSHE88A+NbMx87tzDM8V16jz0ChoZeb9atQeWfZhilIKZixlEDCk6BTPa9LlMjYluKHyAV4qtS5cuVrsbHt21a9fXXntt2rRpvBUyS0WLv2IU5mhSbI6epVJ5txOKjY7LQMwzPsURxeZDOW7PgFmyZAl2Z/Qg9H3avlUoNrIQJJsMjfgAjmBAOHDggHEfFym2PzxWbCRDXrp0iRMh8UI1uHnz5uHDhykFang8OdQYqxQbmo9d1gFHjx41FYywFoSEhGzevBmtGRYWduzYMcpPayvTc+In+oiICEpcv369dscW54g+RxAVFUVWbAEBAaZOKBctWkRFkUtvVmVFV0oMSUNjpwNWmqQEr+fFZs2alS1bNsqTLFkyrzwvRW1LkyaN+iqAUf3qq6927NiRIlInTZr0yJEjUh7yKQBlSfSwYAVHFNuKFSuSJEmSN29e0UzPLxSb22N0QzE98YLTp0//8ccfUSbeVGQlnHaZFdRfxJ5iU6w2IfYpNkfN5UeKjYBNkQIREEyPg5kiDim2oKAgYx+ZTvx79+5VrVoViehxToxXFJsPk0VlebF6nD3Um8sHKzZTr2dxSLGRbzIuCtLLcQOiqSL6HRBMsR7SSzn96iPBxipBAgaYy0JFbNp0PqnlElHiNuNlgoIeHk48fTpa1s0SxeYWTsC1bLkYPwsVGv3FF0+crTal2JhxWLzY5MxLePgdo4mQHym2O3fuffXV6jRpBowbt53EYD7pqUKxKd6uTrE56kp7eKXY9u07zxk44ID0LKbYLl26JVlXrVz59/PPD6f4Bm6BsGPjLH9RbNWrz+BB5RUxRLFNnx5SvPg4Y5xTQp48D/zHvfzyONOr9eo9iG/wzDO9qU9nzdpDDWXqCy8k5Cxd/e67h874JkzY4TKczwVGjtxmZJ9FcMijmLZiM8WdO3cghEBiHzdu3KOp8VCoY5aKPIVJUbOsEE2KzdGzVCrvdkKxNW3a1FSqMc1MMKXYfCgHchr2a0gULJKpU2y0O5t+ltOIK0C7h0TEpxVNZTYM2itXrmzdupXykGMxtmJbv369GO6AzziK4RTiELFKsXEsiY0bN6qH/uSTutRkfOZWnJZRUVHM3MUT8vJ/GdHnCNyCA3JTH1tYqV2eaAMUgoSJITJqk2DUWsnQpmjRoqaELIYTFmKm9kw17U2bNonKEkYjH+lv1aqVVcsQBg8eTDmx1ZlmWLdunaSr45YCBQpgswwODqbXKV++vHSei9rEqhGAOXPmUFBktxOKDTINWWz16/fE52h/UWxuz+csqFtTpkwZOHDg3LlzTa18HXWZKRy9iFeKTbHa7rig2NxOmstfFBtGl/gTizy1tkv5y3McUmyovMtDLYncq+nEp8mLnKJzk3hFsbmdTxaV5cXmcTZQby5HbUInslOlSmXUuOKQYsufPz8ude/eXeW58QTk5Ije1EYqxbxgn7lWOHDggEstwi99kapTp47xEvt9P3LkknTJyMuEhl6jlGnTLI+YqcBIsfGhzsSJe8+cuSdhwp7SgVNTim3ixJ2UOHr0n8ansIlQp06PT9D7i2LjuJbz5x/gRHWKTf12dYrNUVfawyvFdvlyBGcYP36H6bPEg6IUsDVTpsH0s0SJ8bNmPfbm3r79cpfnoCjbLfqLYiOfa4ru1WKCYlux4shLL/2I9rTK0KTJA2IUw8/0arFikA8fhFuln0ePXqa2HTXKZMAvXvwwqMXvvz+MZkDhXz/7bIUxc5UqU3Hp+eeHGy+5Hy1TSZIksX87r1Cn2G7dukXS8t27dymeqRjh3chSkfOQ1KlTqziyjCbFpv4sxcq7nVBsHB/A+B3OEcXmtJwFCxYkSpSoRIkSojsgdYqNFLScOXNatZVGXIFdre3YscMqD4R/Jnkw7K9fv05///nnEysPm2TFE49ssUexhYWFcQOxni/h6NGjf3nAcjOakqKOrl+/nlQC6ABUCHErBGY0TY2YNGIZfuEIVqxYQZnfffdd4yNouWRnLqz5ZMmSxcixkoaGWziFQ6H98IOJrNOlSxcx3VTTnjhx4qRJk6Qbqdg33njDWKYINpkxRhRye2YBNmDREi0kJAQ6Ku7i6tHtw4YNE2+EhkNvCs3TaEm3efPmBg0a8E91ig1Tj1JEOxT3AzccDwKcR59iw2CQOC9TOOoyUzh6Ea8Um2K13Q+0tZX03Nmzn9CjeITHBMWm3lxOu6xQoUIuM0rC+E2Vx/nOnTuNdTAiDik2kuC/+eYbMdF04tPB8AwZMog5Md0oZyxTbBBAqRyJvXU0WRSXF5vH2UC9uRy1CfvXHz1aDhnJo0LRHwc5psmXL5+UXqpUKZcTig2DJEGCBFh7L12SCYV4i3nz5rkewZ42HT9+/JAhQ+xLwxaDcmrWrOn1uTQ+TR2tsj3LxInyomHkZf79998kSdDd/1e16jTTB507d6N7d+8xvmvVmtWs2QIpsUiRH5lla9RornTVlGLbtu2UdDJOBB1rdT3yY0XwF8XWt+8GXMqcebCYqE6xqd+uTrE56kp7eKXYNm48wRnWrz9u+iyRYmMrRVz99df9L744RvRK1rDhHNeTHsT8RbH177/RZYikIQLD6fjxqyoP9QFopcKFx5w5E268FBERSbybTYiMyMj7eEfXk84EX3rpwTT56KNFxjJ79YLE9SBgKHm4cz8KTtKx40pjZhotGTIMMq057d3RP2WvTrE1btx4woQHA6Bv377InzlzZvGqkaXicE90lxGimBdNik39WYqVdzuh2EaOHEkpkuBqmplgSrE5Kuf69evkKxY7kZhTnWLr378/lWkVMB2Sg01gKw2/AC180ANRJGb6jKTQ8+fPUx7xmx/2eravioiIuHv3rinFBvWZ0s+dO+eOB4g9io1dqm3cuHGnAaQ7HThwgPLs2rULjXvlyhWOisDhRLEoUArmSVhY2I0bN9CUfHpU+2KLD+D4nhJHwB7WPv/8c+mWEiVKIP3FF18UE99++22X58uVFCcUAyMwMBCqsqhyU2agadOm4rcd9tpWrVo1TmR3RUDPnj0xiij95MmTTZo0KV68uBg3o3fv3pQTs5cTsStAN5OMREgnR4Fem4jcsbk8Ych5jYiKioLOg/eaO/exQI+VqGDBgqLaeefOnQIFCrg8tiGHDz9hn9+qVSsqNkWKFJMnT8ZS5fYco8bGlilTpmPHHkdGJ8VSUiDdwubNKjczROKxrD179qRPn94oDYSHh1NmSU9m/zvSsUGK5Dhp0iTR1tcUjrrMFI5ehBw3WH01Va+2WxAvateuzQMG+j8doAOwtYv5/TJ91JvLaZeReSl/QcWgJS4DY0kyOMXLYogmTpzYNAiJERxEQgob8uWXX1K6RLF169aN0vFSKuWTmI6lQzJ9Onv2LDoa845biWA68dlV8ObND9UMtEO7du0oUYpJb/VGTtvcCthMKT+fCcVSiWZX731Hy4vV42xqqN5cjtpk3759xLthHG7dulWsvPGJ9iCtBoCIQil4I8jx5EcZo0VcWJhiE8NiEDArkT5okLmKGA+BacvhemzCyLo9DQKd0MrmmjF8+HCXEHjOBmTbmDt3buOlP/88TRr+iy+OkS4xVzJv3uP43ZUrT6XEOXNkz4NQ7KtWnbZ3r3dRu2LFyfXr/ywlzpgRwqzNtm0yid+y5WIjxXb/fhSZ+QQE9LpwQbavpFN1pUpNEKdM0aIP8r/66hMU4b17UeQsTJ1iq1BhssTmAD/9tFeRYlO/XZ1ic9qVNvBKsfXs+QddTZ68340bT0gCphTb7NkPX61jx5UFC44WD/aid3Lnxkh+HBrV7T+Kbf364/RcjBPj+dllyw6/88486XYbis14ws4GO3acwZsyfyehbdtlZKcZGXk/ffqBeO7kybukPGvWPAiHGhjY98qVx2LP8OFbXR4XeMYyaVB17fqYu2/T5oErtzfeMCGg8TiXJ9aqafUqVqxo3Brcns4yzW8FRYoNewrykPtvCmJTqFAhMcNPP/1E5TBLFRISQikQhCSFBRgxYoT4iSKaFJv6sxQr73ZCsUFhoRRJXxMzQ5ER000pNkflcEAqibwjLwcSxUYBxyHviYn8ib1YsWLGibNs2TKJktOICfCpRNFtOjtcw8DGT1yin8jMeTiE6IYNG2jWY5BIB0WRjkFF2ZA/dt/MHLFEsbGvNCtcuPDA5QE0ATGEKGPTpk08Je7fv89snQSI1DqiaHzAN998Q2vZzz8/Ibai4yi9SpUqYjqULjpT9swzz4hrHxb9atWquTwu/PlkMQYJlPycOXOyRkSA9pgrVy4qv2zZslB1sBZjS8Y2liBBAl5b+bMP6+0ujzKJTQhlQm2DwimdYm7YsCFlW7ny8cc3Ilkkheq1117Lli2bihXDwYMHs2TJwhXATlmkSJFnn30Wf48Z84Q8CsUSO66k/EONoRtRbZHpR83xji4B6dOnx0slSZJE5GswiajBAwICaOoxmjdvTjdOm/ZQ6L9y5QprYnjBb7/9tmbNmpB4xIOxkAzo+8+OHTso8a233hKLZZ2/cuXKYjrHqQBSpkyJNsmXL1/x4sWrVq0KGUgySlXvMlOovwhWanQHJZr6jHdUbYCGMYDHfffdd++99x56HD1Ciej3Nm3aMI/jr+mj2FxOuwz1p/SWLVtCAKpbty4NLbxRnjx5wsIe+/mmcO8DBw702jUETFsqWSRNgDp16lC6uOO6BZ4au6xK+USxuTyGNrzBo8KFCxfOnj270UbddOLz62MsdenSBd0NeQ5CLaaSy2MW2ssD+zdy2uZWuH79Op0JzZw586xZs4YOHYoC6YCnYu87Wl5sHmcF9eZy2iZMgCZLlqxt27aYLGPHji1atGj58uUpPU2aNOhx+sxgA+YNU6RI8fnnn6PdUAiWQY5hhx2E12Sm2PBQtAC/O32Q79Chg8opofgA1JxcSbo8tiE2gpPHH/kDw0CKD4MxAG1EPENAwBDCMqiopbAZo7EcoG7d2URDdOmyWkznYAJiZE82X3rmmd6jRv159+7D4887d4aVLTvx00+XqdTn+eeHlygxXkqMjLyfNetQlFyunGyu7n7ktx7/Ond+Im4yG7IZXdpXrDg5QYKe5CeeQTEZkybtc+zYw7Mdd+7c69BhRWBgX6S//vpMMTOds8uVy8Q09eWXx7k8DuPZQ//Nm3dr1JhBlQkJMWln324PCws3pdg2bHjYEXPnPl6lHXWlDfhAIv5xFzMWLjwYENCLrornPQmmFNu9e1ElS45HYqJEvcqUecKIhogkiQayaXn3g0+bS0wpNjr8WKDAE99dXn11GtUH44F9vd26FTl48JYMGQaJh2ptHopZiZ0Xkm2pUqVMY3xJwINQOFp76dLD0r9fftnftOl8caSRxzQ+DcqgKBDffrtWTLx9+x6mj0s4DUo4dOgiRnv69APPnn28uSxffoRIOqPzRDILHT58q9sALKqQsrBcrFjx+IQpVjCszNjapEMJ9mC7cmwZVnmw40Bs5g8ARIdh64TQTik3b94kb2gAkQIEdkGL26F90BdB7La0p4jHayByuDzRLaVHk6EAB8yxgeKz1CsPQYgSJYoNKjmlix/+MfYoEXu6mPnrr7+mdMnkmRd8KV29nKVLl1KKyKZBMKMvbfXq1RNvp7OxBQoU4FcmpYy9D0EOZ6udW7duDR48GCK0qf9ZDf/i1KlTzOpg94fYgOWLjioCpEUikVkdpISHh2NgM+0DGYyKYibuzz//RP9eu3aNo2UiJZ445Y8lig1iugrF5vZYagQFBYmXoJxIfCTUSGPgUbR7NB1hakQfmCoff/xxkiRJaCHDsgWlBYoxBkDHjh2zZs3KWl/t2rUpeBmUEzqSQyhSpIi4xGOeQB9DOalTp27WrBl2oBw5cnz44YdisAsG5hg2HnKl7PJ4anv33Xex90Cdw5bWt29f0RrF7TmRJ1YJG5to8eH2fJZncgRIly4dNmYyOps4cSL0T6iI1atXHzhwIN4Cyzcyqy/TWDXq16+fOHFiLr9ChQqi5QX2NvoGhTfq1q0bp+/atYvJBZeHnhsw4LHjjDt37rRv356CRRDq1KkjvviUKVPEUHd58uTBfoZ0TCLUh9OhS7dp04a26uXLl+PdKR0KOTYkCD3Ynqny+J+Mt3v06JE9e3YuoUGDBosXP3Dr++2330In53Rsqxx3FRWj75NWkLZkr11mD5UXQW+++OKL/Ahka926tWSf5bTa2FfoZC7h9ddfP3HiBKqNv4sXL46RSfu936eP1+byocswbrl9MmbMyGcGCxYsiJqgtC+++GLcuHGQmfA3ZpDKVocRWKVKFX4cisUYPnz4MLZV5rlcnsO8aAfUH+ksnLk8x8MlEc0UfFB07NixqVKlKlu2bJkyZTBTkC4RzTYTH7uPOE2QjYg/OlkMoMzz589bvZFvbW4DKBj8CQF1EPdK+973bXmxeZwpFJvLtzbB2IMiJA4D3NWnT59kyZJh5V+0aJHiJzcMV9xChWBgYBHAoMVIe/bZZyHQz58/n4/tM8WGFkP/ZsuWDet/pkyZ8OgZM2aoPCuegI/TojfxggcNwIq0evVqtAwdQgdo5GBTcHnMe6HL8cckCLvly5fHBq3+jZPGmGTsQPj778vPPTeEaIjq1WeMGvXnzz/ve/vteWQUQ1xGtWrTOSjhxx8vZv4lRYp+RYr8mCXLg9sbNpxz/74d/0tYtuywy8xNPjBkyBak//qrfDbi8uWINGkG0F143J07T/CqP/4YjBomSNBzwYLHfs169FiXLFnf6dNDpKJ+++2h07eMGQd99dXqtm2X5cr1w4gR2+hIHQpp0mQ+nXyMivo3b94RRCaGhcnzrlu336kcvHv37ms++mhRnjwj+FhilSpTu3RZbRqEwentTKWJ9lZu4VioSL057Uor4Ebu4t691x8+fOnIkUvbt5+ZMSOkbt3ZxK/h/379TBZMU4rN/WDQXi9YcDRRXez7//jxq2j/V1+ddu7c413SvuXdj6g0lxAewe1h8dCnSHz22f7iCAkJOUtmYvQvZ84fChUanTRpn8DAvlu2PD7bbv9QNvMB3n//ffvWw0txL1j9E8cqVr9mzRZIhmyrVx/FaKxadZpxTm3degpvhLdg13WRkffRhugR3CVlJkM2DIarVx9/DsTUS5SoF0aCeFyXQV9B8uXLJ8oS69at493Z/vUZERERZKDt8lhOrVy5Eus5ZDmo8diag4ODZ86cCXmDBDB2qczG8ljku3fv/tFHH0Fm5lOH2AUge9BuhWWQy+e64X9sE6IvC4jo9DU9TZo0koE/hRtyKbivVXyWeuWZSpM+k/BxTlGw/PvvvyEYUDp2wFGjRkHYgHZGEoXLI0tjr4csQfnZI4EUbUC9HIidZFdO4gHkK+TBLk9SFrQVejsqloNjfPXVVz/99BNKJu4Goj6dWSHkzJkTShzkn8DAQO1jKnYQFRXFzr4kQMBmB8EcG1QCRqnoRoxt1iTEk1gH7lgOd6AItDJEt5Me4A8rDQ1SL0RzaKrnsBkq69gaTyMwLaGY/f7775icXolUIk3+EA5j8wccUyAbMmOtt3eWLwFDjkwYrl69unXrVuz3vp39joyMxDYfFBRkdMoWHVy7dm2LB/4yl8V0QyXxpqISFRoaCuknOrMPE7xevXpoPWyiUJgh4kCpGzJkSK9evdq1a1e4cOGAgADjK/jWZX58Ed+qjW0eOwTbEGH8xI7rh+g0lynQdNjbtm3bJrYhsd54KeyOa9aswRyMbzbFoi82LCPQUtDpErmmiH/++Wft2rXiAVW07aZNm6STlbEDiOMYilanZf3e+/aPM0WMNhd6kGYivSDmskpIZQkYDxjPe/bsYTM0KCrGASz5YoP4gffau3evvSlffMORI0fIilAd7MEQ+hh/A4BiU7ly5TJlytStW1c9AgaBTgmxN1UJFy/eqlfv52ee6c1ETJcuq7dtO0VKPjR/UT93e+xuMmQYxHxBlixDJk7c6ZVfGzduO3M9ZNCEwpcvf/yRLDz8TrFiY0W1H3V4442fUqf+XqQnnntuyFtvzb18+fHpub17z5UtOxG1rVFjRsuWiwsXHlOp0pRDh8xNrYcM2cJvmj37sJUrH5zeKl9+Ev7+/PPfNm8+CRl44MDNhQqNFp/YocMK0SDu5s27ZPRExmjvvDPv9Onr9+5FEYuEf61bLzXlLxzd/s03a5msCQjo1aTJ/C1bQtFKbdsuS5q0D6UHBvb95JMl7FDfaVdKaNFiIbGNpv9SpOhXtOjYhg3n9O69XopHwbCi2IDRo//MkWNYqlTf46XwLnXq/JQr1w/ff79JbCj7lg8KCqUgm/SvQIFRZOS1cOHB0qUncHqpUhNmz34cLQRtW736DIw3ztCo0dyjRy8rPtTtoWko7pDL85XUpgEjIiLJyszmX+bMg9HX0o0//hicLFnf5s0XYpq0b78cTd2jxzoOuirh1Knr5cpNypNnxKBBm0eM2Fa8+Dj0y+7dJraTmJVjx27HbM2adSjGSf/+G9999xd0Qa9e6zEITQsnmybJYxe0aCKqJKtnU2CPaNiwYaZMmdRXPGb/sTXUrFmTEhMmTPjOO++cPn0a2wTTYa1bt+b1H5mbNWtGplWUH1dF2X7SpElFixblp+DvESNGuB+cXJ7N9tcuj3235HTMCK/PUq/8N998w1QXtoYmTZqQ7tC2bVs2WQgMDPzkk09YfMUfkIH5W37ixIm7dOmCPTRBggRVq1adPHky1QSyB+4iI0SX54tOo0aNxMOeiuW4PeEO+BhK1qxZ6ZsWH3rNkiUL1EPKCRGFw2RjdogHFPD61atXT5QoETc16iPZXmjEKG7fvg2RSSLF9u3bJx7BgSyHTmHnawT0rzS8sQxCJBPzbN68OV45w42PFJuGhsb/ArAR5suXz+hVnYG9v2zZsmwYHE/wlFZbwybcgYaGCuwjiv6PAGLukiVLJkyYMGvWLAjBPp8egP5mGhOWcffu/eDg05s2nSQjo/DwO6Y2RAzo+X/8cfzkyWvx5JDImTPhGzacwD/xrJwprl+/s3nzyUOHLnLN//nHPCaYPY4cubRu3T+iBdaNG3fXrz8upsTc7TZw2pV+BFNsYpQJt+dAbrZsQ7dtO4U/kGf16qMhIWeNTFPMAc9Fm+zYccaKWvKKY8eODR48WHIc4Uegm5YuPTx58i6MAXsmlLBnz7mZM/fMmbPv4MGLNnyu2/PuaG3knD17r30LRERE5MiR45VXXjFO6uvXr9uEIPQvjhw5In1Hv3HjBlY/0y/rFy9e3Lhx4/bt2x05y/MNKs9yVHlHuHv3bnBw8KZNm8jbbHh4uOgqxO/lIH3z5s3odPGb1v79+3Gv5KIBrREUFCTlZFDwdFzVR9/iCuRG/8SJE+fPn7fqBXTihQsXTp48icGAgWG1rWNUnDp1KjQ09MqVK/HNU4em2DQ0NOIGdNbSPhxkqVKl4psx1FNabQ1NsWlEE5pi8yOg5xQrVkwK9qKh4V8wxfbXX0+4Zfzhh6316skxLp46tGzZcvp08xAB/w18/fXXzz77LEUe0NDQ0HiKoCk2DQ2NOADHx7TyVhsVFfXtt9/2798/litmj6e02hpuTbFpRBuaYvMvjh07litXLo6praHhdwQFhRLFFh7+2O/VzZt3M2ceLJFuTx1mzpz5xhtvPF2n1B1hz549adKk0X6yNDQ0nkZoik1DQyNu8NJLL5G+2rBhw1mzZm3duvXw4cNQt5YuXdqtW7cXX3zx22+/jes6muAprbYGRTBIkiRJXFdE42nF5s2bae5LYdc0fMbBgwcLFiyoj9Vr+BGHDl3kwKOrVh11uf6vTp0nIoQeP37VJvjDU4Hhw4c3b948Fo4ixhUOHDiQP3/+PzzxyjU0NDSeOmiKTUNDI25w7tw5Dh8uIiAgoGXLlqGhod6LiAs8pdX+X0ZkZOSaNWvYce+AAQPI5YeGhjow8TkQasGCBfft2xffHH88pTh58mTt2rWXL18e1xXR+C+AYpuWLDme3If16/cgLqoYrPO/gfgTNS8msGHDhlq1ah07diyuK6KhoaHhIzTFpqGhEZeAFDV27Nhu3bp9+umnPXr0+OWXX3wL8hjLeEqr/b+J/v37f2oARaTS0FBBSEhIu3btpCGElHgVvurpRVRUlHa3pOEXTJmyi06GFi06tkePddmzD5s796+4rpSGM5w4ceI/fABWQ0PjfwGaYtPQ0NDQ0NDQ0NDQeOqxfv3xrl1/79hx5cyZe0JDtcGyhoaGhkZsQ1NsGhoaGhoaGhoaGhoaGhoaGhoa0YKm2DQ0NDQ0NDQ0NDQ0NDQ0NDQ0NKIFTbFpaGhoaGhoaGhoaGhoaGhoaGhEC5pi09DQ0NDQ0NDQ0NDQ0NDQ0NDQiBY0xaahoaGhoaGhoaGhoaGhoaGhoREtaIpNQ0NDQ0NDQ0NDQ0NDQ0NDQ0MjWtAUm4aGhoaGhoaGhoaGhoaGhoaGRrSgKTYNDQ0NDQ0NDQ0NDQ0NDQ0NDY1oQVNsGrGHa9euzZgxY8KECXFdESXs2bPnm2++OXHihB/LXLJkSfv27Y8cOeLHMuMEFy9e7Ny58/jx49VveVre/d9//922bVvHjh1v3boV13Vxhp07d3bt2vXcuXNxXRENjRjB3bt3N27cOGrUqHHjxuGP+/fvUzq2Fc5z586dqxbA7VYl79u3D4UMGTJkxIgRc+bMwU+sA3Rp9erVp06dsq/YmTNntm7dGu3309DQ0NDQ0NDQeOqhKTaN2AD0lldeeSVRokQul6tx48ZxXR07XLx4sV27djlz5nR5sHv3bn+VfP369aRJk6LM2rVr+6vMuEL37t2pfbZv366S/6l497/++qt58+YZM2akV4NOHtc1UsKBAwc++uijrFmzUrX//vvvuK6Rhob/sXr16jx58mCEY6gXLlw4YcKEadKkefvttz/55BP8wdn++OOPDz74IHv27C4BefPm/fDDD4ODg6Uyb968OXDgwGzZsiFPkiRJUGyZMmVSpkyJn+nTp2/QoEH79u1TpEixbt06+7p16tSpUKFC/n9nDQ0NDQ0NDQ2Npw2aYtOIDZw9e3b9+vUBAQHxn2KLjIw8ceJEs2bN/E6x3bt3L0uWLCgTOqG/yowrjBkzBi+CDvVq30F4Kt4d+vaxY8dee+21p4tiQ7VPnjz59ttva4pN47+KTZs2JUyYMGXKlKtWraIUDPtx48YFBgbSsL9z546YH8s48XFA6dKlo6KijGVu2bKFyLWMGTNOnjz5xo0blP7vv/8eOnSoQYMGzNAtW7bMpm63b99OmzYtsv3+++9+el2NeASILm3atAkKCorrijxluHjx4qRJk6ZMmaJ+S3h4+Jw5c4YOHRpztfIBERERS5Ys+e677+K6InGJM2fOTJgwAR0a1xWxBBbwHj169O/fH/0VnXLieXejIzBBmjdv/v777/fq1QuyX1zX6DH8uFTu3LmzT58+eE1Itu3atZs7d660xfsLPixTGhqK0BSbRuwhR44c0aTYFG2mol/szz//7HeKDbh06RJUxHv37vmxzLjCxo0brU7RmnbT0/LugwcPfrooNsLUqVM1xabxn8T9+/dp7xg2bJh06cCBA+nSpcOlf/75R7rUtGlTmhHdunUzlrl06VL65FOkSBEI2abPnTFjRsKECZFn3rx5NtXjqffGG284eS2NpwCRkZHp06dH5z733HOmRK2GhNu3b3fv3r1UqVIJEiRAu3300Ucqd/3www+VKlWigw5Vq1aN6UoqYsGCBTVr1iQD/Oeffz6uqxMH2L9/f5s2bQoUKEBL3AcffBDXNbLE8OHDqZKOHJiIiP/dPWvWrDx58ixfvnzRokX0XSdVqlShoaFxXa8H8NdSCU0BOylWg02bNh0/fnzIkCG0kpQtW9aPK7Bvy5SGhiNoik0j9oBNKzoU2/Tp02PCBsq02F9++SUmKLb/BcRQN8UaIOs/jRTbzJkzNcWm8Z8E1Dwa25C5jVeXLVuGS5s3b5bSP/30U7rr+++/ly5hVU+WLBkdDj19+rTNo/v06YNs06ZNs8lTokQJehCE9aNHj6q9k8ZTgxdffBGdC2UsrivydABqMObU7NmzaVIo6q5hYWG///47Mdrxh2K7fPny9u3bU6dOHW85l5jGjRs3zp07N3r06PhPsf36669UyRUrVvhWQjzv7p07dwYEBPB3pj/++IMo6V27dsVtxRjRXyrv3LlTrFixHDlyXLt2jRPHjx9PPXv8+HE/1NID35YpDQ1HiFWK7d9//w0NDcUyAUF548aNO3bs+Oeff9hjMQPL3J49e7Zs2bJ+/frg4OBTp06x42FGREQExO5t27YhT1BQELTKyMjI2HoPDR8RHYpt3759gYGBfudurIrVFJtviKFuik1oik1DI15h7ty5NLatjilVrlzZaGhmQ7FVqFCBLn322Wf2j4Ygjm3rxx9/tMrw559/JkiQoFevXlTg559/rvBCGk8TwsPDly9f/tRFv4lbYOL4oLs+99xzcUuxXbhwwajGly9fPq44F9P6xH456E0y9onPFJvbc34CymM0C/Ghu/3VTfaA6oSK/fbbb5yC94UqHdPPNQU2PmNi9JfKESNG4B1nzZolpf/8888jR470uVgr+LZMaWgoIvYoNgzlnTt3/mFAUFDQ7du3OdvRo0eNebBoiiwblrMNGzZIebZu3RpDR7U1/AWfKbaLFy/my5fP5W9PXjbFaorNB8RQN8UyNMWmoRGvsGrVKhrbOXLkuH79ujHD+PHjR48eLSVaUWxcWpIkScLCwrw+vW/fvkOGDLG6Cp2zdu3akD3ovGrKlCnZp5uGxv8yyCTNke5K58HjimKDklKjRg2jR8VXXnklTig2q/rESTmJEyeO/xSbX+C0u/3VTfbAtkJdAG03Rh+kgvXr16OV/F4sWjJTpkyxbJfnwzKloaGI2KPYjh8/TlwYJufBgwePHDmyadMmSmEW4/Lly5znwIEDhw8f5jzsaeXu3bucGBISAn3yzz//pJ/xx1xWw+3x1VW/fv1cuXK9+OKLzZo1Cw0NtaLYjh492qFDh0qVKlWuXLl8+fKffPKJ6OQLXZw/f35SivLmzdvYA8mc4fz58506dapYsWLWrFmrV68OnQrjxL569sWKFFtkZCRUrOLFi2fOnBmP+Omnn0wLVKkD3rRnz55169aV0k+fPt27d++mTZu6PR+mUEi+fPmmTp1qU38odXPmzMGDMP5Rw6FDh7788stZsmSpVavWhAkTTG+5ffs2alWuXDkUni1bNrT2qFGjjM7R/v333+nTp6OSDRs2bNSoEbpm2LBh+/btE/Pg1RYsWID+Xbx4sUp72ry7esWuXLmCNqlWrdrq1avx87fffkNOdApGDldDxKlTp1q1avXmm2++/fbbqMzgwYNRrE2TEkSKDYO2Xbt2BQoUyJMnD4RLrEvG/KjnrFmz0OyvvvpqyZIl8YITJ040ZlNpVbfySL5161avXr2KFi2aO3duZJ48ebIPFNvWrVubNGmCt4Nig/9btmxprA+qHRwc/MUXXzRo0AA/r1279uWXX+KhaJCPP/7YlO8wwoexqtgOKtl8mFwQ9ZYvX46Rg0UM/dutWzc0Ue3atTECHT3a6wjEHvfVV181b97c7Tm9+O677+JBhQsXbtOmzbFjx0zrFhO95sfBqViUI1y4cCFJkiQ0vLEOnzlzRuUuK4oNLUbpWElUyjl79uxff/1leunSpUuoGIYK/u7cuTMVq7LIaGj85/HUUWxdu3Z1mQUtiSuKzao+cVKOptis4K9usgdEF9pf4pxig1ScPn16aGp+LxlyAr3jkSNH/F64FTTFFvuACAqZio4hQqDF3zdv3pTyQLY8dOgQhv2GDRu2bNkC8RjiFl+FdrbXFlaOwmMZsUexoR2JCGPXwtAS0b6USIZsbOZ27tw5yhMREUEGa5s3byZDNigelOfgwYOU5/79++gGStQfkOMJRo4c+cwzz4wYMQJKKabKzz//nD17dnJ/I1FsuIQ1rmPHjjTHMKnSpEmTKVMm1sr27Nnzyy+/pEqVCve+9tprv3iwY8cOsQSompMmTcL4Wbp0adGiRV0edwD2mph9sUyxbdq0qUKFCilSpIBiiYpRolE/91oHXCpbtizd/sILL4g3Vq5cmYzwsWlhJONZlA0tZlrzsLAwtGHKlCkpGx5XunTpgIAATiFJSDo6vWvXroIFC1aqVIkmDqYYxaBEJdHmYs7WrVujhmTfERUV1b17d3oKXT169Ognn3xC7ioA1N9re1q9u3rFUI0WLVqQ4wlgyZIlX375ZfLkyZFHbAexWGzSuMSxyVB4zpw5X375ZdMmFcEU25o1a8ihLAONLBnLhIeH49UyZswYEhJC9Wzfvj1ytmvXTirWvlUJiiP59OnTxYsXL1myJJoOq+LJkyfr1auXOXNmdYoNYwMVSJo06YQJE/AKKARNioEHMXrgwIHsU3bFihUvvfQSFYumw74FFShfvnzs/Nir0w3fxqpiO3jN5sPkwr3oO/qUSnLze++9x1XlsFMqNbQfgVhD6C6XR6WcPn06FkyaPoR06dJJ/sVirtf8ODhVivIBpMYQMmTIYDxIYoQVxUZRRIFWrVpFs1Zo9ly5clHLQzKhkYamNrq20ND4X8PTRbHxN6p4QrHZ1CdOytEUmyn81bxesXLlSnpQ3FJs169fh1BBApXfC1+wYAG9YyycumVoii2WAf2FmR8RFy5c4DzXrl2D9GvMw9oN9ETjVRGQe+Po/Z5ALFFs9+/fp9eWzo1DA2feDVIprlIeUULdv38/5SEKE5o8/YSOwXkg5VOidjYcHzBkyBCsWdLJefZFKlJsV65cobBuxFAQPvvsM6S888474u0ZM2Z0mZ1AhD6ZKFEi0YAxNDSUpIG33nrLa1WtimWKrUiRImPHjiWLKoxSMsTLkyeP0zqcOHECQ5d4EJFmOnXqVHBwMKnWhQsXbtCgAXJCgUyfPv2HH35oWmdo2qhJp06dqIbQ8UaPHn379m1oelu2bMmePTuli2TQyZMnAwMDUXnxMDVeqnbt2qSysnkO9GekMC/g9pillC5dGg1CP69evQr9uUuXLvQUpths2tPq3R1VzC0MISix3333HfEy58+fJ7kclRRLfuONN1KmTCmmLF++vFChQqZNKoIptmLFik2bNg0iBZaXESNG0EB1PelzvWPHjkipV68ep6B9KBt/A1BpVbfySMbe89xzz6HTRXewaArUlp6rQrG1a9fOZfBshfWTHtevXz9ORL+QRIW+KFOmDDs6GTBgAD1O9AxihA9jVbEdVLL5MLlu3LiBuzCAqWJvvvkm6oaS69evj7vocYo1tB+BGFeHDh2iuqVLl+61114jmQDNxfZQWbNmFedFDPWaHwenSlG+AQOJmHdG9erV7bd7U4oNLcMloDWiUyWMYYxnsZCaNWtSyT77245loHeWLVuGHqxcuXK5cuVeffVVTFVxYSFgZH777bfFixd3e94aMwKrTZYsWTBoTQ17L1++jHIw/hs1aoRe6969e9++ffkTNIpqLGDcuHHuR7aZnIi/xfHcu3dvSm/Tpo30LAjizZs3R31y5syJSTp+/HiJ38TPDRs2NGvWjCYOVGIsBS+99BJUVsVWgkqAIV2yZEmjzSZmNB6KhQWv2aJFi1GjRk2fPl2xWEclQKPo1q1b1apVsWai8shpdWjjyJEjGPmQW7CrYnzWqlVrxowZRs5XpVlu3ryJXnj99dezZcuGWYz1x2pzwaj48ccfK1SogF7AOPniiy8wiqJJsWGDwPjJnTs31sxWrVqJX1Uxi1u3bi2OImzEYt0w/Gg4ffDBB2fPnvX63D59+lBt6elUJmsrIucCeQNvV6BAAYx/5CQLViPUm86H+hBUOtprOWgciFKY/tWqVStVqtS7775r9TnEKcW2e/ducUZjw6XAMtjdxI7D8OBjTNinMJcpXWKsvE5zt0fNXLVqFbINHDjQtEpkXo2+K1q0KF5k4sSJ2EGM5ah3t0o32QMTBxOwRo0aeATkOkxAqD+SAQ61GNXK5TG+5tZTd45kvyYTvG4HkGkpoAEAcYjqILoftVkq7Sswe/ZsFAVZhQqHRC0OEtwCjQCNg7uMrxb7y5SGz4iIiGB+DfMdExAiOv2EYkWKNsbhtm3bKHH79u3Iw7QPQA58vFJsVicPYhmxRLFhIdjhgfTakBKYv8ScpL/RuGIe9s4GbdztcbJIP8U5jInKfRY7b6RhBaiIUCyx/kqrP1Y3MiERKTZMKlpSIWFz4rBhw5CCRVC83ZS7wZ6aJ08eCPpSHaB9UbGHDx+2r61Xik2Sd1lHZWNMR3XABuMys+SqWLEi0p955hn1rzdQkql8KUI55gsJQ9iwuQuwYyHF6LT7n3/+oUJatmxJKWPGjHEZvIDTOUQxhXRplxrFZvPu6hVzew6bUyKEQjEzfro8Jmbi2VKMwAQJEkgyBIQGY8UkMMW2YMECMZ0/V4qf7yBXIQUSkpiTTLTEKIReW1V9FEHRklgMwqBBgyinV1EefYeWwfAwHsWFeOry+KgSC4Ew6vLEhhfpTgwtMirs2bOn/ePcTsaqYjs4mnQ+TK61a9dSOUZDJ/VHq4xASIQuj0mdZMfHhxn51GHM9ZofB6fi6uEbUI0ePXqgH12PkDRpUojpxgYhmFJskCL49rlz50anPtBGUBnx0+uSJUuoZIj70Sk5doDBUKdOHbzCypUryRCP6g9lj6Os4hLHS8VUxctiNmXIkAFKFB3dxaq7YcMGsVgo7ZkzZ27fvj31y/Xr12nl58GJlMKFC1OZIo+2d+9elEzp8+fPF8uEzA0tC7qQ6BoVwjpGfpUqVdARmB1Tp04l49NatWqRFI6aQP3LmjUrlYmFnUQLgoovIez+bAYLiF6DAUyitGnTskwL9Rtt4sjVrGIJmFbI1r9/f6xgWCj4U5P0FROtNHz48MDAQOwRdBDk0KFDUJWRE8sOr36KzbJq1SqMhIEDB5K206RJE5fH1SCeLlUPrY0Bj6Vp9erVGFQ3btwYMmQIfz7xjWLDi3CzE9Ay4paK3se2S5ekz7GE999/HyNWRdHCwoKXQptQaRAnyAafmQ7mXKCwYIxheENLRztTfklOcNR0vtVHsaO9loP+QiGQwUiaxcTE7chp6nrSByu2KVOm0KPTpUvH3gnQcV9++SWlY/vDT/EW9BfSMdnZKNvrNHd7PuK2a9eOhE/gq6++kmqCmYv9C0OU/HpDi6TAGjSunvWApWXF7vbavF4B+Qcl40FELkClhSSMVS558uT4g7k/DCcUy1+1v/76618ewRgt0BRe12S32naAJRoPzZIlC9Lz589PdaDvSfZLpdcKoGchJNBMASDNzvQAUx6rH0saHTt2lF4tTpYpDZ+B2UFcDQuNGMNbtmyhRBJWr127xvwarwMYe5RITsOQHmkA1go6LgmZxHjyNE4QqxFFJWBBIbM14NatW/RVzWjFhjWX8tBsDAkJoZ+iQxksAdwlcfAmGgLIrsfUSMToiw2zC/pY165dxR4njgN7nnivKXdDttNYrGc+CbKBAqw8PdkX67YOdwDRX0p3VIeGDRu6zCg2Ymqgt9jXVsTvv/9O5YtGVQQKPOR6RFxibaKfpt+9q1WrRldJVySpCGKH+DETC59oZugWnCaoU2zGd3dUMbfHKIlSJGdn0OEpPTQ0lBNp74QULi6169atMz5IAlNsly9fli5RMAeApSg0PuR7KbgShq7Lo7pwitdWVRxFkKdJ1BPflKDui61BgwbIZuoUb/PmzVSIeNAVwofLw4JJmenAnZU5mAj1sarYDo4mnQ+Ti6l/o5GC+qNVRiAFLzMejDpy5AiVxuxtzPWavwanSlHRx8GDBytVquQSULNmTdMQZqYUG2YH3zh79uzo1ATPhRovpkDsy5kzJxUunb6Ph+jXr5/LoymJidS2nTp14hRIrrQUBwQEYBItWrSI0g8cOECeH6D9iiUQ4SsunhgA0LFFf3y8vY4YMUK8d+jQoZRujDIE3V4yS8dcKFasmKhkciALdL3bY5EKyZBVUwzgtm3bXrx4sWfPnilSpOjTp4/XJsI6j37kE9ai3kjngqE0ivl79+6Nbc5rsY5KQD3xaMkOlGyWcfv58+fFe6W+cwsHuzDxSWZWaZagoCDMYok8IhInadKk4u4DZbVgwYIYCewumcAfI32g2FDVUqVKrV+/HoWj/b/66iues8HBwZwZiySp9KYHS1FbvJf6oyHJ0COsDoqmTZsWtWIbJfIDgPSXXnpJzKzedD7XR7Gj7ctB29I37zlz5nAitieXh0yXvgy5faLYINUTmY6mEyV8zKP06dO7PEbi0i30GVVcK7xOc7dHJw8LCxs8eDClGyk2MgAXvWRCq6fMqAMpj6zMO+pum26yB1ZINELy5MnZLRJh1qxZVKAoQAILFy6kdPtzA6ZQWZMVtwMAMrzLcFDUZqlUrIBbkL3FIyBuQfKXejaulikNn4FBQtNNHAzM6pDFMVuoif6ImZuTxoYIJotUwljFDuKMYsOKybZ/fGiWXaphRlFKeHg4WxVCpHN7RGT6iclJqzZEQLYqxJSLqzfSIJAhca9evYyXvEYURXf/+OOPhQoVom1evGTK3dCJKqz1H1lA+hhuhFOKje1xmCxwVAd7is2RdwMb2mLx4sV0acaMGfiJ/+knW96JYK1mzZo17kdGiJTSokUL0UZDhF8oNkcVc1tTbKbsEll7uTxRCI3fmW1gE1G0b9++dAlCnum9WMFatmxJR0pFxd5rqyqOImJ4UT6Lg/aNYIrcuXOL4qkEErsrVKjAKVZkjXqAYPWxqtgOjiadD5OLKTaj3Kz+aJURaEWxuR9p0egs+hlzveavwalSlF+AfX/cuHGiOz/UzWjLZkqxQbLnu4xBSNVx9OhRlCA5ywP69+9PhVv1VPzBW2+95TJYizdr1gyJZcuWFRPpsxkgnRIgk4HAwEAxkb5D7Ny5U0zs0KGD+PkTnUWmEOKIdXuOI5CVpaRKQVzMkCHD2rVrOYW89hhDD5E7AqyQrLiizlT50qVLG5dNFbRp04ZKEPXG2bNnuzz8lJgTA97IGlhBpYRdu3YlSJAAiq5076RJk1weio3PSh8+fDixB8bNlFez1q1bc6JNs2B+FS1aNG/evFI548ePp1tEWpCsp8WSCefPn6fMHzmn2FKlSiVtvkQqAVJT0BhGO0jnFaCbGQehPbxSbKiVRJC1atWKbuGPKI6azrf6OO1oq3LIXsz1pLk9nx4wSji++WKDPE8FshRH+OKLL1yejzFSR48cObJixYr8U32au4UhJ60evOZLRziLFCni8jivkApX7253NCg27I8uM7Ms9yOJBeuqSDFEh2JTWZPVtwNTio1gulQqVsBtTbGx9xWxZ+NwmdLwGZg7Vz1ggQ39GBQURAQOzaw7d+5QHnEUsccwtqmUgK6kDMgZCy+iiLih2O7evctHRCnGHKWLx2uRYe/evWTXRqDPwuJRXtyLfUL0iicdMtWIZUAUpp2YHKxIsNHJjx8//tlnn9WqVevXX38lV24qFBvtCsOGDfO5wtGn2BzVIXYoNpae6RgOfwQ2dV00d+5cusofzZYtW0adCKROnVo0WWf4hWJzWjFHFBsWCjYvd3lMXRQdNdpQbFylMWPGiOkY9riEx3Xu3BkjmazYJCfr9q2qOIqI48uUKZPxkiLFduvWLfryD/XYNAN9hxRtSGOUYpPGqmI7OJp0/qXY1B+tMgJtKLb69eu7POdb3THfa34ZnCpF+RGQtOiYLcFYPatwBxyqxVS9UQSxTqUNoO9DQPLkyY1OzeIVoPC88847kts4Ol8s7VC8UEtL4rfffkvpIpdKoTagvopxMCC88XdT6V7J3I+OdUOFFu1W5s+fDyVNzMYn2iTLSlKbgXnz5lFOaGuU4rPrPXIO63pSbySNF7NSOq0pUQk2UCmBpp50vt7tUUuWLFkiuicjZbhw4cKmz+KTueRuxW3bLBs3bkR6uXLlpLbt2bMn3VKwYEHKefnyZdrsTF3y+eyLTbKLdHvsnjj0kHgQjx1WfPzxx2J+Cret/ly3AsVm9H9PkqpLYATUm87n+jjtaJv3whxs06aNSBixLw5JrnP7SrGFh4eTret7770nprMrBslJCOavSKipT3O3BRHjFqzeJPeLvKxJn2fUu9vtK8VGFDBgenaYtQ/R2Dw6FJvKmqy+HdhQbKZLpWIF3A4ptjhcpjT8gsjISMhIbHpmavgPMeDGjRtYl/icounhaBRFRBBGheR0JW4RBxTblStX+OTt7t27xeaA3ADV/Y8nwRZqbOGJaWmVx8oFrEbsgHeOvn37Gq+aanfQHjt06JA+fXreWWmdVaHYSIMV3W06RfQpNkd1iB2K7eLFi3SJ4u6RkbzVBhMUFERXRR+xwcHBLKu5PBSAdGrSLxSb04o5otjcHiq/W7duHKYAop5KIEIbio1P5IkffrHs5M+f/80332S3yqYUm9u2VRVHUdOmTV0e2sVIWyhSbJcuXaJslStXNs1ANUmaNCmnxCjFJo1VxXZwNOn8S7E5erTXEWhDsRFDRJFVYqHXoj84VYryARjqVh5nsHeULFmSnpItWzbpqhXFVrduXUqXAqSoIyIiIk2aNJiMg81QvHhxKj86335iH6GhoT169CDjshw5coiXrCg2OsMIiJoSWx9jGUQLWMm7eByxxl26dOHEsLAw5meXLVvG6RhCovdJtD+55IMKamVZyYooc0nSwSt1mOqNkPuprVweB+Q+OFf2WgJWj+TJk+Oqin8DmnG1a9c2vcrHQjkYuk2zfPPNN0gvWrSoVdty0AnedEz9T/k3oihLCxLFQKsTho14OChfvnziqUAV+ECxjR07lm5hYxz1pvO5Pk47WpEDwhq7ePFi8pAl3s7wOaIo+RXF7aJXUO7NEiVKcCK23XTp0rFPNEfT3G1NsTE5JfmNgRjp8rjtlyqs3t1uXyk2dqdo6toIL05XxXU4OhSb4poswmY78IFiU6yAI4otDpcpDb9ADGJAThKNeTAOOQ9UQquRw6cbYzMWrQpilWJDC/J52j880T9N2/TMmTMhISHQZrH6YNc8duwY5Rf5byzWUPLR4tu2bUMG6GmUJ55EkfifxYULF2gtMyVZjNodFmLyHyHuT+oUG9laW33QU0H0KTZHdYgdio39DZFhNtvqzzRzOs60kUSWQb4fMGAAifguw4kev1BsTivmlGIjYDEhywiXx2TA6ownw4ZiY/8d+INSUDfs0JDJRBbAimJzW7eq4ihq27Yt3WiMkqZ+UJR8ilvFpCe/S2I3xSjFJo1VxXZwNOn8S7H5sObYjEAbio281PE5sljotWgOTpWifMDevXvr1KljdfXAgQOuRxBVOLc1xTZ9+nRKDwgIEIUKdUyePNl4xInBulDu3Ll9O5kYy1i7di0W52bNmmHJJbOF6FBs9+7de//997lT8ufPb7Xkki8/bBlsRdK5c+fKlStTgIUGDRpQ4qFDh5ImTSqytIcPH6bCRZ9TVoghis3t+QhEEYFpLLVv396p3aJ9Cbw2enUxDMWDyAiriTZ69Ggqqnfv3pRi0yzvvfce0r/44guv9eeWMY1s6F+KbdSoUfQsyegPYj+ls/odHBwsEToq8AvFpt50vtXHh472ygFdunSpX79+VapUwUjYtWsXZfYjxYbGoTKZ9IS+FhgYyIGz2VMQWg+JfKOjae62pthOnjxJQ7FWrVpiOnWflOiOFYqNLa2sjF7TpUuHq6g268jRodjU12S3wnbgA8WmWAFHFFscLlMafgFHMCBAljMyQiLFRlZsRpYN0iYdbcSIVQwAEmuIVYqNHd1t3LjR1PuSKdiM0OZLOIc7EM+ua8QJ6BhOgQIFjJeM2h3FgpTOgKhTbOSh02XmHZnQtm1bY/Ror8W6nVBsjuoQOxQb+ayFWkJewJkvMD1lRocfofkTa4OdT9SjoDuxUQbzSm4/UWyOKuZ2SLGJTnzdHgGdtlJjYEQJNhQbec9JmzYt6YQQ4olNk/ymGyk2r62qOIqGDx9O2YzBENUpNhpsVjnpyKH4sT1GKTZprCq2g6NJ51+KTf3RKiPQhmIjT8McPDfmes1fg1OlKB+AgYHbxTNxEkgbSZQokSTWW1FsqCpbD4kmVOooUqSIzbCHkMdxyhYvXuxD+bEGaNRly5YtUaIEO1mLPsXmfhTxkAlWl0eBMUrGHIAV2qPb47M8ZcqUq1evJmc66FA6fwoFqWnTpuKNwcHBdKPkLdsUMUexuT1O0CtXrsyvmTVrVsnfk1fYlMDchPHUngS2cpU6jsEuL/v3708pNs1Sq1YtpKvEbeBgNab+cfxLsS1atIieNWnSJOlSmTJlXJ4wgsTFdOjQ4d1331V/KMEvFJt60/lWHx862ua9IMb06tUrVapUyEzTkw+K+pFiA2gX4EAB2NSw8UVFRVFYW7KPPn/+PB4h+lJwNM3d1hSbWzDuEw9M1KlTB2uU0Xt6LFBsbMRnbGcCeWIlNxGE6FBsbrU1WXE78IFiU6yAI4otDpcpDX8BwtKZM2fYIZgkSBAwcqBqUajQPwTf/Qw+1xjfTNjcsUmxhYWFMRNp9X0Jy+tfHrB3AOwBFHUUKyPRkyiH8ojuP9izm9MvVxp+B0dSN245pN2JUdjImY50YIc0Oolioxjb0gZP+rnL803P6O566NChplEXvBbrdkKxOapD7FBs5GeddyPUig4XJEuWzBh6jzK3bNmSfg4ePJhjxhEgtiZJksT1pNsIK4rNqj3dZu/uqGJuhxSb8TMvFejVGMeGYqNg8+xnkAeDKPRAcCRhVFTsvbaq4ijCNkPZjEOFGwE6m/0LslBonB1UK9Rf/FYRoxSbNFYV28HRpPMvxab+aJURaEWxYewFBgamSJGCt7mY6zV/DU6VohiOHLRlzpy5cuXKVj44aLqJB44IVhSbW1BXUDcpHLARK1euhObAP8mzj/3ZPeaeTMmCeIIVK1bg9fPmzStaTvmFYiOEhoZSPARCixYtpAzoUIpvS1aK0PMp7C/7bxo2bBj2hVSpUkn87NmzZ6lM8fSoFWKUYiPMmjWLXoT2Mh/cLZuWwGcCunfvbn87Nh0ybgoICDCdJsxPsTsOm2b55JNPkJ4mTRqvB8q4ZUwJ9Bii2IybCF8aOHAgXj9jxoxOfc+7/USxqTedb/XxoaOt3gsrOe2Moje0GKLY2AP9jh07oNyhfegYODlkTJcuHX02kz5/OprmbluKze3xpJY8eXJMru+++w6bUdOmTbERG+PVuGOFYuPAWT179jTNULRoUVwVfflHk2Ij2KzJ6tuBbxSb1wq4HVJscbhMafgX7GrN5ksqxgAzSJIUynEyRbeS8QSxR7Gxu7SNGzfuNIBEtwMHDrBLtcuXL1+5coW5Mwon6haoOsyWc+fOQRo7fPgwpUD/jCHPyhrqgMZCy1mePHnY5Sqwe/duWsvEmFDkBRObN+eEWEkfcABx6aREXtYvXrxIpAyfwHr99dfZWx8GT8eOHbFbYHjY19aqWI6cjUEl5qcIR64nVSz1OtSsWdNliNoDVKlSBemkYCiCaQtJd0X9M2TIgI1HVIc2bNhAmSXnsmjhTJkypU6dmq1KoSQbY6LRV2Ix3DX3suiVzG3dnlbvrl4xtxDuSqLYJkyYQOliWDGIUxI9ClUZeZo1a+a2hRXFdv369ZQpU5YqVYoPf7HQI1oPUaw34Ouvv+ZElVZVHEXUjC7hM7XbQ1g0atTIODKtQF6Ec+XKJe1JdBjnm2++ERPJv7KRrCFTIMmNsSkcjVXFdlCfdD5MLh6Wy5cvN15VfLTKCCSKzUj7kmdliU2LoV7z4+BUKQpTGylQdch2SQUVKlRACR06dDBekiLSimBR3tRUrUePHnQV64zk45mBqn7//ffYyEQKCU2BytufAD1y5IjrEeJnCCYMITp6TGFGGNGn2CTjTch79CDAeCyXDkxBMDh27FjGjBk58O6HH35I8wJLfZEiRYz1J2sIKKKmIh96p2XLlsRBxBDFtmnTJvF1cInqDLRq1UqlWJUSyMc//jc9K3fjxg327UiLg8tCA6clQjQJt2kWzGK6ZDVDscUQBcOkg7gZMfxLsY0YMcLloWOMLD/GQMGCBV2eKBmoM2QMHxQBv1Bs6k3nc32cdrRVOVTVpEmTiu0ZQxQbBirFvIakhPHG5mwnTpwgh4zz5s0zjbutPs3d3ig2PAuqx5gxYzCQ0ErY4o0DiRALFBu56ndZ+wOliS8KltGh2LyuyY62Ax8oNsVNwRHFFofLlIbPwApz0ANxhDB9FhQU5PYYtFIe8eQiVgAOdBkREcHpWFsoMX4KWrFEsaFF/rAFfatHY4khRBmQRbg/sJ4yWyfh0qVLsfM6GvbgdRYKXrdu3ebPn08BnugUIVCsWDFa+ygum8vDvEBFbNq0KUQlFugbN26MhY9Mx9kLFcT66dOn16hRg8T9HTt2QEWnS1grsS/mz5//mWeegbClYjVqVSz7SpBOJXDweDHIl2IdsEbgNV0e0wlRYuaDRc8++6y6MxemLbJmzcofZ7BTQgJLnz698UvvsGHDEiVKhFqxqTyeixaGhom5w9lo3xLPIZ47dy5lypRibCNgypQp9HT0r0p7Wr27esXcQmSoTz/9VExnq3sxYhTUYGjy4rMwrpBoPBcggb8D9+3bl0leLPply5aFdi0qk2gZsrZweWwzu3btWrx48S+//DJv3rxIyZIlS08PFFtVcRSh/mgZyvbmm29CBUU7QychssblCeNYr149ewfzEDfp7Ebt2rVZ0Ny6dWuqVKkgVEniEV6cqiQ6gEP9STRBI9u3p9vhWFVsB8Vsvk0ucoTssvjIrPholRHIvdahQwdsf5SIEYjS0BHSIfcY6jU/Dk6VopYvX07lqNsVNm/enG5p1KiReNYDMjTtKdLq5PYQFqSuuzyBzEzdBUyePBl146mE1YNmNzmNhSYGXaJmzZrilCcCnY+kWYH9Vbs8SlS8CnFFwGJL1ZO+bRBTHx2KDQNPehYHriF/iyLQmzQgCxcujK2fFWk210X/SjUkcKxeU+KsS5cunB5DFBuWCOOJRaoV+0+0h0oJ5G/I5fG9ILG6WAEaNGjANpgrVqygnKZnJIm8EzV2m2bh/sKWbTTlhjz28ssv05ez3bt3U05sdsZBTj1rnJs2sKHY6LQXBA/TG+fNm0c1wYZiZRlkDz64sHTpUumSOuei3nQ+18dpR1uVQ8eTM2TIICbu37+fMvuXYgNat27t8uzC2bJlEwkXOvWCaY4hZOS81Ke525ZiQ8uXLFlSPPlkA0cUm82wsQHmMn15chnoJLfHeRzSAwMDxb01OhSb1zXZ0XZAUbMxko0PsqLYFDcFRxRbHC5TGj6DHX+Jghw7XAsJCXELjr9E3/rh4eGUuGHDBpFw53u9esiJE8QSxQZ9T4Vic3t8DWDmiJcgbEm2SJg2mJZino0bNxr9f2vEISAJMaEGVKxYEUoLNq18+fL16tWLJwN6lhx1uzy+Vz7++OMrV65gDJB7nYCAAOg5lBObDTu4KVasmOiyASVjU6SFku7Cdn7+/HmVehqLhbYAjY6s8V2eUxuQbjG6UGeIF6gkp0OO4aluXwdk6969O++pAHYpyAdY7gcMGEB+lAhooi+//FJ8OyswbTFs2LA8efJARalSpUrSpEkrVapkGjfH7fFtgXdE3aBP4h1xV7169aADi3mgJBctWhRt8vbbb48cOfL7779Hl3Xs2JG3TEw3dBO7VECDNGnSZPXq1VbtafPujirWrVs3ppaSJEmCHXHfvn3oLHQKfQh1eQxS2HYM1cAWmz9/fjx93LhxNucCjIC8DsUYxeJB5cqVK1GiRObMmXv37m08mjF37lz6POvyWPXT8QeMcEpBS9I3Oq+tSlAcyRiN0Pw5TiX6AtNk5syZEIIbNmy4YMECe/+DBORBL+BetHarVq1effVVjL3p06eLedBcHGIMKF68OB3ZgGaIhuV05KGvT1ZwOlYV28FrNh8mFzb1d955h6c/yoSUKfLp6jVUGYFEsWF57NSpU+rUqaFbon3wh1UwypjoNT8OTpWiMHqJmJbM7mzQp0+fUqVK4X9sFrgXb/H666+jZJdHN5Ps16CBYBaIu4/LI1sj0Tj9L168iJbnJYtmUyIPMMXmz5/POe/cuSO26osvviiaqYod1KJFC7KpYaDC0mf8OAcZVLqe9Ay4Z8+e9OnTuzxmU2JmOiDvMlBsdPAZEM3Vn3vuOUkJxBaAyY7VydTbNNZ8KkTqR/IhgO4wNUVnP00uDw/O9DRqgv0IY57XQMxoyiaGzHYE7HdUgsjRT5w4EZuaZFyDAe+yPvwlQaUE7Kd0ztrlIdYh9xINAVUEc79du3bivZh0Ls/mKC2qkKmgrmNGiN1n3yzk58jloT6ZxYuKisLOiHJEDp0eCmB9EykSNi/FnFVpDYIVxYY3woKDXcPqRjQjna3Dri2ORnWwYREfS8RDqXdIejFaBHOcRHH7U286n+vjqKOtymGRjFdFdB9/rZTisSI/yRumbnNVwDQHxCSRLGaKir2OilCf5m5PoDzKKQW/hqiZM2dOSHHiOQwbOOpum26yx969e6lJjUFmu3bt6jL4N+CDNeKupAiva7Kj7YDsKCGl0HxHb4aGhtIl06VSpQIErEV0u+R9D2KGac/G1TKl4TPYb9qmTZsgCmJGnz59mryB/fHImRobplEKBADIaWxZJR0NYc7Ot9BVMY1YDXegCOixly5dOukB/rBarbCLoG+wnEEVt7L41YhboHfWrFnDhJp4jk8ExcEQjRAxo9avXy8t07du3YI0wJ44JeAqdj6InqZyvA3si3ValG918AGifyuM//37969bt463OhugU5Bzy5YtpoZOrM9gWmHhQzYWaxThc3vaV8wpyMwE0hVEGbSVVfxiG0Bg3bFjx+rVq/EuNisMHoSGQqeL5W/fvh1SAqc4alXFURQREbF161YURV/qULLTeHZuj7EPqor2wUYVc6fsfRuriu0Qm5PO0aNVRqDoiw2L3oYNG9AdXl/Ev73mx8GpWBRmllXkBFNg4+BN5ObNm2vXrp0xY8acOXMwkPy19aOopUuXTpo0CXI5lq//vFNXvCDHsoRa9e2339asWbNixYriWcUPPviARN46depQohSxnTUc0Yk4tKk8efKEhYVxCgVitmK4yConV65cUldSaBebQ5dM/Lk8590KFSoERTphwoQFCxYU3QtAI6U8PjuhJ4NQ15NeI8jQddCgQWJOtGS2bNkUj1MoljBu3Dj+muLy2LaQ6aVoykrAW3NkYW4BTECoxGgZ6RyNfbMcPHiQQ4IQ3VCkSBEK4zNmzBgxJ6R09B1lQ0PhdX755ZfPPvvslVde4U9fxYoVmzBhgkqb0KH+5MmTi1EjMP3xRnhf+++mFIyoevXqKg8yAss1fTjMnDnzrFmzhg4d+tZbb0Fdhz5Ch9rQC5IZFFvXiu4y1JvOt/q4HXa0VTkUagzAOtClS5dPP/30+eefHzFiBA02/N3LAyqEfe+qGK1boVSpUi7DuRDsj2heTFtTf45u5WnuFk451KhRQ0znyLwuzyfh9OnTo4TChQvjXRo1ajRkyBDR8YLT7rbpJq+YOXMm3SsGyV2wYEGSJEnat28v2VtxO3j1zGiE1zXZ0XbAI6dly5bz5s2rW7cuHzcxXSpVKkAgB7KA9EWKDdYkb31xtUxp+AxMjeDgYFNDqz///JONGNj9lwRIyJKbFNxFl+KnzBYfKTaN/2fvveOkqr3//4GldxGkg4A0qSodlN5EehdwpShdEESKwAMQEKQqyFsUUQFBekdAOrv03kVY6i5LWaTDLmV+r8+cr/nFe+feyZ2+y3n+wYPNZHKTk5PcnDMnCcO4xOQIeYYJKlhXjTC5UZRhfMqaNWsoWtzmiFMYP378kydPDh8+TDvC8O+MGTNgrtM1NUTu3Ln79u0LYx7psKxEOuwcceAdTF/Y0rly5erTp8/333+PdPx/ypQpRr5grLkLFiyot21iYmJgUZv/VDN//ny6lJBIkyaNHOpy/Pjx1q1biygwUK1atYEDB8onuZgzePBgcvoQr7zyCkxf+qXwxx9/hLWfL1++WrVqwVCEkYzCa9So4fK2GYF6CTBHKWaTQK9BsE7NeAj5m2++yZw5c4YMGdq3b9+iRQt0GexkeV+zolhu3LjRuHFjUgaiUqVKTsPAb9++3bZtW3QWZYPJ2qpVq3/++SckJKRo0aKjRo1Sicon0OmkMDbHQeaYGKFOaILTzcIa6DYk9TAxPXiKsLdbtmx59+7dWbNmvfnmm0IC+fPnp9hVWHQQjkhPnTp1165dhU9EXXRW6yM+Uulo83IePXokNwGKRw50ZKCUcuXKXbt27cSJE2gaRTOJnOhTN8T722+/5cmTR79TDz3epEkTky+aD3O74+zULl26QBQiT506dWQny4QJE8RuAz2oFTm13etuk25yyblz5zD88XWsBD7++GPMnIULF9acADtp0iQ8XTwiceLE+BMVU/8pWmVOVnkdUE6od7FixSgnpkTaIWsyVapUABL+4IMPxG8JadOmhYQhnKtXr+IrdIsaUbduXflKpYBMU4wnYOY5evSoxnd27Ngxea/D06dP0R3i8DVi7969mjh6+YA2oxs2Agu72BgmXsJuCya+wLpqBLvYmABCMYm7du2S91tdunRp+/btVoOXBWTkP3v2DPbVxo0bYaS53Ld+8uRJp9GIiqGO0dHRWxxHsTi9Y9FHQD7k5MKiHwLcvHmz5mQDr5dw6tQpyFMlHBvFHj9+HLMubBIPL1mLi4tDL0BJ9KcdaSCDHB0hWuHy2FMTLl68GB4ejvaePn1a8Su///77yy+/7GEsc2RkJDrCva2mGtRF53Z91DvaqJyIiIhNmzbJ6RhEeE0b7TjxBNTW6WW7N2/eVNl+4ckwh260b98ejYVBvnDhwlmzZtE5BoMHD27atGmKFCmcXomjjodqc+PGDWg7OsJHXh7FOVn9dYAMe/bs2b17t8qZJOoVcJtATVOM20Cj0AUXLly4du2a0dz16NGj69evY1hFRUXdvn07Pt5myS42homXsNuCiS+wrhrBLjaGYRjPqVKlivrxjsyLw/jx43PkyGESXLZ27Vr9RdgMwzAewi42homXiIsv6Yh9hglaWFeNoCO633rrrUBXhGEYJr6yd+/epEmT8qVnjIZNmzbhDduxY0eTPIsXLx45cqTfqsQwzAsCu9gYJv4RFRUljprGfy5duhQfY2iZFwHWVafExcWtXLmSLujEv8uXLw/OsyQYhmGCjdjY2Dlz5ixYsODixYvnz5/Pnz9/9+7dA10pJuigO1ILFixotIXwxIkTNWvWZOcswzBeh11sDBPPOHToUHcd/CscE4SwrhoxevRojVhgDOzfvz/Q9WIYhgl2pk6dKg44T5QoUc6cOS0dM8+8ICxbtoyUJFeuXEOHDt24cePRo0fpTvNZs2Y1atSodOnSfBoXwzC+gF1sDMMwDMMwDMPEA+bNmydcbFmzZt23b1+ga8QEKT/99FPGjBltOgoUKDB//nyOqWcYxkewi41hGIZhGIZhmPjBihUrevfu/e233/IuP8ac2NjYlStXjh07tkePHp999tmUKVP27t3rzwuIGYZ5AWEXG8MwDMMwDMMwDMMwDMN4BLvYGIZhGIZhGIZhGIZhGMYj2MXGMAzDMAzDMAzDMAzDMB7BLjaGYRiGYRiGYRiGYRiG8Qh2sTEMwzAMwzAMwzAMwzCMR7CLjWEYhmEYhmEYhmEYhmE8gl1sDMMwDMMwDMMwDMMwDOMR7GJjGIZhGIZhGIZhGIZhGI9gFxsTjMTGxm7ZsqVfv37Xr18PdF2YICIyMvKHH36YOXOmpY98x40bN/DEWbNmyYn37t0bNmzYmDFjHj58aPRF1HbixImhoaFt2rQZMWLExYsXxUfPnz9ft25d7969W7Zs+fHHHy9evBgpPmwDE8ScOXNm7NixO3bs8N0jVNQ1geF02HoXHsUMwzAMwzAvJuxiY4KL2bNn16tXL1WqVDYH58+fD3SNmMBz4sSJrl27Fi5cmLTigw8+UPnIdzx69GjQoEFlypRJlCgRHtqxY0f50ylTplBlZsyY4fTrc+fOzZ8//5o1a5YvX54xY0bkTJ8+/aVLl/DRP//8U7Vq1W7duu3atSs0NJTK6du3rx8axQQPMTExvXr1gpKQAsyZM8d3z3KprgkG82HrRXgUMwzDMAzDvLCwi40JLm7evHn06NHSpUuzi40R3Lt3Lzo6etq0aXo/mslHvuPZs2dXrlyZN28ePVRjqy9evJjS165dq//ugQMHQkJCJk2aRH9u2bIlSZIkyHzw4EH82aRJk4wZM8bFxeH/T58+rVOnDj5q0KCB79vEBBFQgIsXL/bs2dMPLjZzdU1ImA9bL8KjON6xdevWrl277ty5M9AVCWqeP38eHh7er1+/mJgYD4t6+PDhypUrhw4d6pWK+eKJ3lIJP0Qivzi8gDHX8R2eWpkXFnaxMb5iz549bn93+PDhL6yLzRO5+YLgqQ8sZAo/0fvRTD7yaX2MbPV9+/YdOXLE6bfef/99fOWPP/6QM2/fvt3uWIvjo7Jly4qPsKBctGiR5/aMf7h+/foLOGB9x59//ukHF5vdVF19QWD1xGTYeoX4PopfQOLi4jJlyoRey549O9Qj0NUJRjZt2tS6dWuSErh8+bLbRS1durRu3bopUqRAOfny5fNiJb34RM9Vwp+RyC8OL07MdcKAp1bmRYZdbIxP2Lp16zvvvOP217/66qsX08Xmody8TrDVJ1myZEZ+NJOPfEfixIkt2eowtqmeW7Zs0X86aNAgfBRUAlcH66fatWv/+eefga5IwgFKkvDMs2DQE6vD1hLxehS/sBQrVgy9VqZMmUBXJEj5559/zp49W6lSJc9dbDExMfv27cuQIYPfXGzuPdFDlfBnJPKLw4sTc51g4KmVeWHxq4sNa+vz588fPHhwh4P9+/fjPa13bD948ODYsWPIAPN+9+7d586de/r0qSbPkydP/vrrr/DwcBgh+PfUqVMcNhw8XLp0KVOmTBUrVnS7hBfTxea53LxLsNXHHv9dbFjok2I7dbG9++678dc4HzBgACrPLjYvkiBdbMGgJz51scXrURzM+DSe+u7du2vWrMHi0/OiEnAw77Bhw9xwsTkVCNYVfnOxufdEr6iE3yKRjUh42ujnmGvGQ7w4tTJM/MJ/LrbHjx/v379/iw4kyl62W7du7dixQ5MHSys61oR49OjR3r17NXm2b99+584dvzWHMQK98Oabb2JJwS42S3hFbl4k2OpDxHcX27p160xcbOXKlYunxjnsB2oXu9i8SMJzsQWJnvjUxRZ/R3EwE2zx1EYEQ5Cm7/jyyy+tutiMBILe9LOLzf9PtAd6Dk/Y2sgwDBPM+M/FdurUKfKFhYeHnzlzBn9izUQpwo3y+PHjbdu2UeLBgweRjeLUwIkTJyjP8+fP9+3bR4m7d+9GHvHnzp07ebN3YEG3UlQwyJQp0/sOevfuLTKg+1avXt2sWbMqVapUqFChWrVq/fr1u337tqYcvYtt7969/fv3f/9fPvroo//973/yV+7fvz969Og6derkzJmzbNmyPXr0+Pvvv/U1XLNmTePGjZs0adKiRYsPP/xw6tSpv/76q0rTFGtugsmjzeWGR2NctG/ffubMmXaHmVq0aNESJUqsW7fut99+Q1GUf8iQIeJZvXr1atu2LaX37NnTaX2WLFmCPMWLF8+dOzeaM23aNPFDk0l93HjijRs3Jk+eTAbS1atXW7VqhT5q166diE5Vl626iw2TSZcuXd6X6Nu3r6wSeARVGF9BrQy77V8wt0yfPr1SpUp58uR54403+vTpgxo6tdXRrvXr14eGho4bN04kfvbZZ3gWrfJBjRo1RMXQufQf2smSOXNm8dG8efPkklWU3KW0Fcs5evQo+hctpbZDPUqVKpUtW7aaNWti6pZzwu4iOYDq1atTzel0OXNQvaFDh6LTIY0yZcqgqqtWrdLkefLkCXSjefPms2fPxp/Lly+vVatW9uzZS5cujS6IiorS5L948eKoUaOqVq2K/1+7dg2dXqRIETSzadOm8+fP12Q2GVkiD9qOT2GoFC5cGM/Fp5988smFCxfcbpEgOjp64MCBkFiuXLlQLIYVXXkh0Jhny5Ytg/BRB1SyW7dud+/e1RSIlIYNG77++utQP6OH6nGqroS6DhDms6uKnoSFhaEmeApGGYqaMWMG+kjzFEtTsfqwNUFFB3bt2qU4ihmrBGE8tRHBEKTpO9xwsRkJhF1sfiBhayPDMPGRO3fuHD9+fPfu3VhGYuGE/8Mk0eSJjY09ffr0vn37sEQPDw8/dOjQzZs3NXmwFIyMjDxw4MCOHTuwkty/fz+WCkHlBfKTiw2CIIcahCV2dEIWwptGKREREZQiwoBh8wunG2xmu+NICOGqg/Vld1gIIqgNNpV/WsQ4BSbZokWLYIPhvV6oUKFFDsShCejB+vXrJ02aFBYsDYOVK1ciJ+yWK1euyOU4jWLDAEuUKFHu3LlhamrsLpiIKAQmIgYt1KBt27b4btq0aRcvXixnGz58eMaMGTGe6U8YhMmTJ4cJ5LJd6jU3wvzRRnKDxd67d+8cOXKQNCZPnjxp0iTbv5Ab5eTJk6gY/nzzzTflJ546dSp9+vQ2xzmjmspAqrVq1YIdi1GJ8YhJqmrVqsgJ45ycTeb9qP7EhQsX4kEhISFITJcuHYbna6+9JupPkVyWZGspig1Ng1VMz2rZsqX+K23atMG3RKeYgGmnTp06aNeGDRtQ4Xv37k2YMCFXrlxUuLDVYXX36NHjlVdeofTPP/9clAAVhQz79+9PHw0ePHjRv+Bb9J88efLgI4hIfISOkEswV3IVaauUg45466236FuQz/Xr1ytXrpw5c+bSpUtDaZGIR2BapsyYfvFFaCnlHzp0qGiUuUghyZQpUzZq1OjGjRt2x0u3WrVqKAGCpQzR0dHoTXJYgGnTpoWGhuI/L730kmgUegTvYMo/e/bsMmXKUDq6AG9umOV4BJ1yTXTr1o1cjSojC9DxQ7DK8ArH6wZv/enTpydOnDh16tT4j2YWctkime+++w4TwpgxYzAY4+LixBEz3377rcgjzDM0rUuXLhA7GijOz8b41VRA3KuLfjcXPmGirpZ0gDCf4lzqCUYr+hcT0erVq7Fm+vnnn7NkyYKc9erVw+gTT7E0XSgOW3MUdeDy5csqo5ixSnDGUzslSII0fYdVF5uJQNjF5msSvDYyDBPvwDpNxFfJYJEp8ty+fTssLEyfRw4FwPLv4MGD+jx79+4l11Aw4CcXG1a31HgsnUUihEiJsIUoBZ9Sinz3FpanlAiLC3+eO3eO/sR/RB687ynx9OnT/mkRY0LBggWdLohHjx5tc7hs5MS3334bif369ZMT9S42WEc1atRo3ry5PnZj586dsOWWLl0qJ1aoUAFfh3V96dIlSoHCJEqUSBNgNXLkyKZNm7pskXrNnaL4aL3c0GrMR8Iv895773Xr1g0GPKzZNGnSYL1L2VAxm87hBSAxm87FhgJhZMJWlw9HWLFiBT2ie/fuJvURKD4RA/PQoUP4E4mocOvWrWGmYpjDeochSu48S7K1ulH0zJkzdNNo9erV9V+BkkCe+nQNmL6KFCmSKlWqiIgIOX3s2LEaWx1zWlRU1Pjx4/U+C2LZsmX0kXyjqKBEiRK2/95FKFBRchVpKw6WuLg46sqQkJDSpUsvX76c0k+ePAk5IJ3CxATz58+3tJqHSFFD5P/9999F4ubNm8mhQ79W4TUJVRdGXbZs2fr27Us/oly4cAGto/RXX301NjbW7jDFz549S14ztAUavn79eryG8Syod7p06Sj/jz/+aFcbWXgNZcqUKXXq1PTqEcydO5e+NXnyZEstElCjFi1aJCeWKlUKiVBX8UORMM+gfr169RJTH6pK6VAnuQRx0l/9+vVVesFcXS3pgOIUZ6InDRo0gATkWEt0n35SUp8u1IetCZZ0gDAZxcGJSTizDOZSdASy5cuXD4OuXr16s2fP1scYQksXLFjQpEkTlIM/sSTDUMWofP311z/99NNHjx7pS/ZFfLcoXDGwFLPBxIkToec0mbjRHJdBmtAlqCimGixj0NJBgwaNGjVK/8u8VRQbaDUiFZw4caJDhw4FHNSuXRtSteRiMxeI7PDCjNenT5/ChQujPsgJfXBaoOJOBSOsPtFIJQhIAPNwpUqVMBZQpQEDBkCM+sNqrEYiEyrBvObq5HZouUrhMt6dPVyOaKOYazemHbtyJ5rjowFo3gUoSt6i8f3339sdkdRiKwnA/zFeRIF4HVN6165d5QepDCuVmdYIk3Hk9qYil/Kx1DrGbzx8+FD4144cOYIVuwiQop8w7Q5lo5//Ada0yIOcwoMmfnAVviB8EdMLuhXWDaVg2RDQVv7/+MnFhmnxHwcwbERiZGQkiePYsWOUIk5hkydEyJcSaaEsPG7y3i6MK0rUbLRhAoKRa6ZZs2ZIx6JBTsSsjcTy5cvLiRoXG1QFbyYk6p+F0ViyZEl91AYWJVSCsPrmzZtHtrSc7fr16w0bNnTZIvWaO0Xx0UZyw/xCbcEbwmkQLBl1eocXHbytcbE1atQIiTD+5US8/LD0sf3XRWXiYrP0RLxEqf5OF7KWZOvGWWxUPuz/v/76S07HBI102elvxNdff42cXbp00aRjme7UVhfp3nKxqSu53VTalsrp27cvJWqOFqaot5QpU8qJVl1sx48fp/y//PKLSMQMT4nyPkfhNpL9LHbHIrVu3br0Ea2qCdLAJEmSaPaQhoeHU2Ysu8X7xXxkYc2HjyAHff1htJAQxC896i3CSwra+Pbbb2vKxOKVFBWvPEoR5pmmDmgapet90HiZQsfko0tdYqKu6jqgOMUZ6cnSpUuR+Ntvv2kqkDVrVpvDxyc8XOrThdVh6xRLOkDEIxeby3BmAvPGlClT0NKBAwdSR8CCJb88jGo50rxTp04U5Ajwvv75559Tp06NOUdEDsKe1NTBd/HddrXAUhh1MI/plxggLz7Vm+MySBMVhjJjgiUrAjXBYEFOD+09lQa6EZEKUPlUqVKhwtSEQ4cOlSlThjrCpuBicykQ4fDCfJglSxYIp1KlSmgL5df8CGRX3qlggvoTTVSCwBybJk0aTAtYON26dQvzsNC9dA6g1ZRzi8VIZMVgXnN1cju0XKVwgXdnD5cj2iTm2o1px1InmuCjAeiyC5BStGhRKlP2o2HCRMmUvmTJErlMdETz5s0TJ06MsSwSXQ4rxZnWKebjyO1NRSryUWwd42cwislXI8wxTFbiQDAMQ7sUfYXFv1iWC8+P+MWUfHMYOEKvoAzkZQsLC/N7y5zj1xtFCYzzBw8ewEggh9r27dtpFy4ELfyUcpif6BJyTIo7E2hGI/QBcUwAMXLNYMXQsmVLzWXbH3zwATLjK3Ki7GLDFIwVif4cJQL6g2x4Yc/5L5i+qYQiRYpQTvJuYLqXt2KBjRs3umyRes2dovhoI7lB86ktY8eOdVq+usMLFjhS8HLSF4JFM4Qs/6zqLRcbRGdz2KL6Hy3tFmXrhosN5ZP0OnfuLKePGDECizB9ORpiYmIoAMrpL41OD3XCUli/CiTcc7GpK7ndVNqWykHlKVFe2dsdP59SuhzXbdXFRuV07dpVPoIBg50KkQc7loOUqDl7UTRHs4Bu2LChzbFRVP9EWvsCvNEpxWRkkQcWOF2NwVyhTzt06GC1ReQkmjFjhqZM9NfKlSvxghMpW4w3GVHEnNPtz1YxUVd1HVCc4oz0RJglGs0sXrw45V+4cCHlVJwu3Bi2etzQAXv8cbGphzOPHDnSpvPniv2bOXPmlOM+KHITFChQAD1FYQXQbZjBlC4bkz6N71YMLMUKEzY/LDEqSmMHWmqOyTRIm9zl/RkwJ15++WXxA7MbqEfOWo1Knj17NhI10S6osLqLjTARCDm8YGNDA0V01ZkzZ2AAIx2DSM6sGHxtjvoTzVUCNh6+kiVLFtlOwTuIMqOS8iYbq5HIisG8KurkxktZvXCvzx4uR7R5zLWlcWq32IlG+G4AqnSBeAF988038ncnTpxI6bIrjcCLEssP8afKsFLcSeMUk3HkyaYiu5p8vDJpMN4F+qDfqnj48GE5cCo6Olq/VVHjCLI71v9bHBdmyuWfOHGCsgXJiWwBcLHhHSNcaVj+ilOKY2NjRbpsHIoj2+jGgz179sj+Tk2ZwnZiAoiJa0YGPTts2DBatOXOnVv+SLjYfvrpJ/Nfk7744gtkK1myZEcDxDIRrwqxQMTbTuUELjdq7hTFR7t0sek3JRHqDi/aZqWPoLFUH0tPtP/r9EE/qjzUXLbu3Shaq1YtWvTIkU1Yik2dOtVlfcSBJk5/AfaPi01dye2m0rZUjpF7xeleIbdX8wQsCqzO6XdI8PPPP4uPTFxsgH5cxVpfpJi42H788UcqatasWZRiMrLE4WjirDeZhw8f0qdGw9+oRXjNpU6d2qYLI3WKiYuNfszHcHNZiEvccLHpdUBxinOqJxAmne3YoUMHI810Ol7sxtOFG8NWj3s6EF9cbIrhzH/99VcyB/KPmsSOHTtIAnKoIDSBEps0aSJnPnv2LKXLO7x8Gt+tHlgKMPVRusafYqk5JtMgXjc2XdB0r169nKqWIpYaqB6RiiZjegkJCdEfbiik5C0XW/r06TW27kcffURfEb9VWAq+NkH9iZrGalSCosOqVasmJy5ZsoQya3a6WYpEVg/mVVEnt1/KKoX7aPZwuWPDKOba0ji1W+xEI3w0AO1qXfDkyRN68VWqVEnOdvPmzSRJkuhFhDVJ5syZN23aRH9aGlYu+8UEp+PIk01FdgX5eGvSYLwL5lja0Shc2+gpscGTZuDHjx9THllhhO9MvJXoILbt27fTMf12h4bv2rVri+M4Nv82y5AAu9i2OLbR0o8Y4rw2jYsNAqVE8k+LPbryoh8dI0rzf4sYDS5dbJjlmzZt2r59+7CwMApAMHKx0XntadKkOXnypNOi6EimPn36qFQMI5nO46f1CiZZS1eCqtTck0f7wcX2/vvv25Qtcz+72FRk656LTSxzxZoDUzDyy256Iz755BP6rpjHZfzjYrOk5CbStlSOf1xsWA6OHj26atWq0G28MqkQdRcbFpf0qVj2mbjYNm7cSJmHDRtGKSYjS0T2GUW5vvzyy/gUCqCJFjRv0d9//00pKqZ1PHKx2dWmOKd6AjOMEi0dgmM+XbgxbPW4pwPxwsWmHs5Mm3CLFi3qtByxWenixYuUgmUxpaAL5JxYUlO6fPylr+O7FQNL7ZLCaPwplppjMg2SVhQvXjwyMlIknj59Wv1qTg8bqB6RSilVqlTRP87qdQcuXWz6ywcmTJhAX5GjFWzKwdcmqD+RMFKJ8uXLI7FcuXJyonC4y9es2y1GIqsH86qok9svZZeF+272cDmijd5Wlsap3WInmuCLAWhXni7EdzWnkFeuXJk6SA6HXLJkSYECBcSfloaVy34xwek48mRTkV1BPt6aNBjfERcXhyXi8ePHyXvj9CR9KPC9e/cwpigPls1CpbFcpEA2rDwjIiIuXLhAW0e3bt2qYtn5hwC42IgHDx7AdiKpYYkMAwniFi42eV7A5EuJ5GQRZ+PJUbiQNSVC1gFoDPNfTFwzsDnxbnvrrbfELznmLrYdO3aQGYN3g1N3WL169fCpYnSx3bEvAGtH27/kyJFD8QhYxZp78mg/uNgoRWVzq0l9LD3RruBiU5etey42gLWUzXEKA5nxvXr1atWqlVF9ZMgpCZxeHesfF5slJTeRtqVyfO1iw9p3xIgR6dOnHzNmDJ0dJtam6i42aixsFZFi4mIT42jixImaFP3I6tGjh74yMnQ7QdKkSS21SBwtZ7TzXSZ+udjsClOcUz3BO50SFTfNqUwXbgxbPW7ogD2euNjUw5nJDDbSNLGBSIjIyNa1OxO7r+O7ZUxCZe3WXWxOm2MyDYrdW5iZJ02aZOm0REXMG6g+likQKTQ0VP8IP7jYMM/TV8SPEJaCr01QfyJhpBI0wKG3mnLooqHvvvtOTlSfwy0F86qok9suNpeF+272cDmirbrY7AazvaVOVMRbA9CuPF1cunSJTjqDJEViVFQULYbB6tWrRXr16tXFysducVhZmmk1OB1HHm4qcikfb00ajO+QLzHA/52eIyR2MZJ7R9PR165d26IjqLYAB8zFZnecV71t2zbhL4N8hYzkm0ciIiIoEct3u8Pioj/FtWt2xzZsSgye+MAXGaMF8dq1a5MnT/7aa6/JzjJzFxts1PXr19NbBO9pfYjyxx9/jI9eeuklS2vWuXPn5syZkx6RKlUq2oNsgnrNPXm0H1xsdAJIkiRJnN76pME/LjZLsnXbxbZ8+XKS4bhx47ASwupWcd0p1gdON6H7x8VmSclNpG2pHJ+62J48eUKnxU+fPl0kuuFioy3Ash6auNjwhqaixIVfJiNr1KhR9JHRLnWs3myOMFtLLbp+/TqlDBo0yEg4gnjnYiNMpjinenL16lVKlA0AIxSnCzeGrR6rOkDECxebYjgzJgoy+zV7kQTTpk0jEY0cOZJSrNq6Po3vJlyGytp972LD/NCmTRvbvxQqVEizj8wTVBqoOJbFbDBgwAD9gwLiYrMUfG2Ct1xsnTt3pnSNuUFzsiZRfQ63FMyrok5Gwg8NDS2ro127duqF+2728JuLzVInusSLA5BQny5oyY1qi513n332WZUqVeiCBbFt9vTp0ylSpJAPwLI0rLzuYrN7tqnIpXzUWxcWFqYfDkB/AwzjXcQNBiKISu9lk11sFMUmjJfo6GhxOSnS9+/fL/70MDbci/jJxXbv3r1TDjQtF/4yOiOJttEC+cx1fEuWmvhTdlVijU6Jnpwdy3gLpwvi+/fv00038vU3dgUXG/4cOnQo/fnFF19oniVOP9WcGivYvHkzvep27NghBxVjuu/QoQN996OPPjJpjqWaO0Xx0X5wsU2dOpWKGjNmjNOifv/9dxFk6wcXm1XZuu1iw9xdpEgRmyN4HqqSJ08ep7+Z6BHrb6cS84+LTV3J7abStlSOT11sVBOs+eTDht1wsWFpZfuvu8rExQbdpoeKlZzJyBJ3KRj5SjJmzGiTTgRXbxF9Ef86NaXwrpw7dy79Px652BSnOCM9ofPpSpYs6XRUPnv2rFOnTk+fPlWfLtwYtnqs6gARL1xsiuHMMB1JAkavOXHAuZCzVVvX7sv4bsVQWbvvXWz2f69WJFUn8F0Pw9nUG6g4lsVOdow4/eMC4mKzulPBCG+52CBhmoVq164tZnsKT9YLTX0OtxrM61KdjIRP9wxo0NwvYV6472YPv7nYLHWiCV4fgALF6WLlypX0KS3qsLZJmzbthg0b6NCxJEmS0P5TiEX2ototDitfuNjsHmwqsruSj3rrVq1apR8ONuNFMuNFsKjDulHEWjl9raCjYZMK79DRo0ftjmMfhUNNOI6xohZFaQ7WDBR+crGJs9LCw8NFIBKEGxYWRulk84gD7cTOfGQWJ+FRHvQH/SmfGSl28ypeSs34lNdff92m879gPNDMJUd5gObNm+vfwRoXG9RA3PWjuYhaRKbkyZNH8+qyO846RTUoYuvHH3+cOXOmJgNFwWgO3dRgqeZOUXy0U7nZFV5vtAtSPmeBKFOmjO2/Dq+TJ0/SggNrAn3sHsajfFisUX0sPdFu6vSxKlu3XWxg4cKF9KxMmTKpXMdOCBdPtmzZ9OsbEqbmSkGvu9jUldxuKm1L5VhaEYrLrUSAmDm0rsIaV06EQlIhii42TA6JEiWCJsuHBpi42D788EPbf930JiMLcw4puU13Ro/dcXyBzXFEMU1QllpEv6+Cjz/+WBOWi/U6BuCePXvoT/dcbIq+Y4FXXGyKU5yRnlBOoymuf//+lK4+XbgxbPVY1QEiXrjYFMOZIQGKQwkJCZGP7xCI6GBxRrsbLjbC6/Hd6qGydr+42IhLly7RAecEJiWjnC6x1ECrUWzyNc1GmV3iFRebezsV9HjLxWZ3RJy9/fbbNsd5+b/++ivkj8mnb9+++pzqc7ilYF6BiToZCT8qKuq8DvkHEpeF+2728JuLzW6lE43wxQDU4HK6gGBp2qxfvz7+HDNmTOnSpe2OQ8/prtJJkyahm7BM0gR0WxpWPnKxEVY3FckYyUe9dQ8fPtQPB6Cy0YfxCuKoNc31oDIYNSKWDeNOOIIOHz4sZ4OFG1S+ID+52LDoF96048eP3759G/ISF7Vu376d5t/r169TyrZt2yBBZDt27BilwDgky0F2XsImvHPnjthJCnhUBAN0aGuGDBno1yG8aDEPrlu3Tr90O3LkSKZMmWyOmA65BLwnKLOwXqAbdEpC6tSpNeOQfq+wOQ5VFdYpHrpw4UIsYhYsWEApMAJhL2nsT/LlmTtcLNXcKYqPdio3u3RvkeZSJAEFcYDdu3dTCp41Y8YMOk8XRqC881rcn4VPf/rpJ9pwjdfM1KlTs2TJIl+TbFQfq09s1qwZEpMnT+6hbPEIrNWQjneqphyTj+Q8tLErUaJEwomvQosWLaiS7dq1k2OUxG+wNWrUkPNj7qL03r17a4rCYoI+0niKifz58+OjYsWK6T9SVHK7qbQtlfPpp586XREOHDiQ0mUZingfYR7gDWfi6xGeC7wXKAWCFUdfyTe9Cl+JuKNAQJeCff3113IiudiggZpfsWDAQCZo471790Si+cg6evQoKZX+2I4BAwYgHUPYjRZhTkNNKB321YEDB0ip8ELEiMNXRE4xOjCBaCpAA61WrVpyIsYyNBwzpN6cM8FEXdV1QHGKM9ITEcFB+UUfoXyM6DfeeIPmE0vThdVh6xRLOkCYjOLgQT2cmd4CNoNfBagczKgYX5Riydb1aXy3emCp3fcuNshT/hMDgYJogFPvhgqWGqhu4ZPrBza5PhAgIC42S8HXJnjRxWZ3nEeGqWnWrFl4d+C9aXQAkKWfSRSDee1q6uT2WWwuC/fd7OFPF5tduRON8NEAtFucLugIfzQTq3co1dKlSymd5lKs9PB2Ll68uNPKKw4rr7vY3N5URLiUj7cmDca7YHTQjkZZGYT7jA7TxzqW8sj7mjElCs8PzFWsG+n/mt8+MQQonQ4WCzj+O4vN6bl0hJheIUThd5OBZOUrn4XLU8PZs2f91hzGBLGvEwsCmO4NGjRA7+CNKzbew0AaMmRI3bp1K1euLE+sH3zwAfnUunTpQokrV64UxQrzDKYUVEKkY4yJgzNtjhAqvE7SpUtn+++ppXjN2HQGOWqSM2dOOQpGj6WaO0Xx0U7lZpeuEjcKexaSgeENOxmGMVZpoaGhffr0oXQsLoUoMJTolG4BDFS8nmH20+Nc1sfSEzGoxX1Y+h0QlmRL91jZdPdAmX8kQzeFaxwTLoGd/+qrr1L55cuXRz8uWrQI6wa0kU4JBBDpDz/8QPnXr19PibVr19YUJXwW+qO40C8UiJcqVSr9hTiKSm4ubfVyQP369SmP5iRa4aSTx+CdO3fIPMiaNevcuXMnTpzYrFkzk8vdhWqh9/v379+9e3dYPt988w25M/D/EQ7skosNYkHJosxvv/0Wib169ZJXt/Z/XWwAiiSOuo+KisJCM1euXBrvvMuRBbuI2iXfe4UlLAZLz5495R9I1VsEvv/+e0onUqZMmTZtWpvD3JKbIywZjdkgFvFQS9kYw+MoPU+ePEaS12Oiruo6oDjFmeiJGBo2h9Hy+uuvoxWYl4oUKSLe/pamC6vD1gh1HbC7GsXBg3o489q1a0lWTu+HIcnL/kdLtq5P47vVA0vtXnKxmQTzQgM1KSKm+MCBAyIRY0H+dcocSw1Ut/AbNWpEKdOmTdM8UWRWdEaYCETd4WUp+NoEL7rYIEzNXnUjLLnYFIN57WrqZDW0XOCycN/NHv50sal3ohE+GoB25emCwDqH2ohFDl6XYkmwa9cu+go0TRP3bbc4rLzuYnN7UxHhUj7emjQY7yJ2HMr3UIkD1ygkDR+JeCyR5+7duyIACxqOhRb9uXv3bnkNjN6ndLd/uPIufr3uAHbOjh07ZKcY5mI6hU0AA0NErhH4imapCoFGREQIjyYRVLdIvOBA+4sVKyYmd/GCX7NmDV0PanO4ycaPH4/uxqAimwT/zpgxA2+CGjVq2P4ld+7cWFjs3bsXttnw4cNluxRTpLjCHE9s3LixuEbH5jhgVYSTEJjTsVLHAgvz+Lhx42AvVatWDc9S8Xar1Nzk64qP1ssNU0zr1q1FzIvNEdM+cODAhw8fah4Bo53Cwmndg/pgmPTt2zddunTvv//+kiVL5NfJ48ePYRxSDD8BW1rvoTbqR/UnorGiBBJdly5dNL9nqsgWqxaswyhWhYD0Ro0aZXcsaIw+0oNFDDLIsVqK3L59u23btrD86REw0bFkxJsbCollDR5H0sPsjwZmyJBBVKZOnTrkupo0aRJUVNj2WBLhz8GDB8fExBw9erR3795YCohvvfrqq7169RK/RoruMFdyFWmrlIOXVtOmTeUxiG69d+8e0hs0aCDSs2XLJt9jhZErWteyZUv5PE09WGyhDnKX0duUdrnaHK5Siq8ULjaofdWqVXPmzIlBlCVLFjx99uzZ+pLFRlEYTlBLLMVQFFQd6XQoCaE+ss6dO4cnomkVK1b8+OOPy5QpU7hwYSit2y0iwsPDCxQoIPJjCGBACQci1gcwCWR9Qzn0Ex/6IleuXOKLKBZmDH3r9OnT1K0ut0ASJupqVQfUZ1cTPZk/f36OHDlE4WnSpJEj2ghLU7HisHWJig4ojuLgQT2cmeIBMVg0my+wMEuZMiXGmmzDoEOpWI2tGxsbS+nyXiefxnerB5bapePPNUduW2qOSTBv9uzZNVMx0qGZ0Fi8jikF61jMb5isVO5CsdpA9YhUrMDJYofAYaWLnKin/onmmAiEitKcKWGX7gqk6Y5QD742wdIT7cYqQT8nzJw5U/+y0GMpElkxmNeupk5WQ8sFKoX7aPZwuWPDKOba0ji1W+xEI3w0AO1qXSAjflnULIroRtfUqVM7XY+pDyuX/WKC03Hk9qYiQkU+Xpk0GO8CE0w4dq5evYop7sqVK5ipKJF+HEWicOwgBaoLmwUrT0qBRWB3jGtx7BpeWBhT0C5xUv+WF+0sNgEmIJiUWB5BrJhhNQEIApI7ZuTo6GijPBBxVFQU8mDO9WSWZHwBegeTGkaF5ifZBw8eYB2DdZucDn3AGNOYUm4QFxeH4Yfy9b9a2B1KRRYsPkUFNm/eDO1SL9yTmqs/2khuKmBOwRePHDkihgymM5NyMCWFOzDxhpjXx+oTjfCpVsj8/vvvsM+drlFUIGMe07foPv0JTb7GXMn9X44MpmLotvom3IiIiE2bNsn5nz59ilfvX3/9JVI0Z7FhwsdXjh49ahQiJ5/FBv3ct28ftEh2rrkH3vEYKXi0uVNGpUUy0J+NGzeiTKsHqJnUk5YgfsbS7GquJ/gihtjff//t9Pgeu/XpwlvDVlEH4gvq4czISb97FSxYUEQUQtTVqlXLkyePOCuA2L9/P5XWrFkzOV24D6pUqSISfRrfbSmwtHz58pRZdipZbY5JkCZswvz588u/KEOXNCarcMcDTAv6FnnSQEtRySNHjqTEVKlSdevWbf78+Zh+S5YsWbFiRUp/6aWXMNPKvxk4xUggGNq0sQtV1UzOoaGh9IhffvlFJKoHXxth9Yl2Y5Wg+zSJtGnTomIFChR44403qlevji7QnHhlNRJZJZjXrqZOVkPLLRXuo9nDZVy5Ucy1pXFqt9iJRvhuAKp0gQxFC0KXNPbylClTbMZbL9WHlct+McHpOHJ7UxGhIh/PJw3G62D+wZB0ug0RlqZY8mHB7DTPtm3bhO9MHMemB+vwwDXxP/jbxcYwDBMosMzSX0rLBDPmN4rqMbnugGEYGcVwZrsjRgCmY+bMmTNkyNC+ffsWLVrkzp27Q4cOmltxhw0bJodYNmnSZMWKFUgfMmQI7HyR3qBBA7o5zqfx3YqBpYMHD65atarIhvIhE/KJW22O3ThIs0iRImXKlEFpffr0+f7772GQ4/8wgGX3yty5c0VwsVEgtoxiA92LSoaQ8+bNK3+Ktn/55ZepUqVq1arV8uXLFX9L0wtk1qxZ8qWWMJXRBXZHEJ/cnNSpU3ft2lVsxFbZqWCE1SeaqITdscuscuXKNmMmTJhgdzcS2a4WzKuiTk6FryIuxcK9O3u4HNEmMddujFPFTjTHdwNQsQsEz549K1iwoP7Qg5iYGGigfDegBpfDSj3eX4/JOPJkU5G6fDyZNBgfgVFz9OhRjVPs2LFj8j7ip0+fYoRqtiru3btXExAQFRUlTvknMMAvXbrkrV+sPYddbAzDvBBggsZyUJz8yMQL2MXGMD5FJZyZgCEHi+vPP//EXOqVjRh+iO+2GljqOU6DNMmbgMbiuRs3bjx8+LDThkAgMC1KlSrldBe8U3zawOvXr6MtBw8epPgCWC9uHGBkNbrZBF8EX1vl5s2bjRo1IrGsWrVqzpw5MPInTJgwYsSIHj16FC1aNCQkRNGZZYJ5MK+iOtndEr564faAzh6e4MVO9MUAtNQFxMmTJ51u+VKJavf/sPJwU5El+QTDpMFogAKgxy9cuHDt2jWj2eDRo0d4AWFkRUVFYZ5x6jjDWLt169aVK1fwboqJifHw1mmvwy42hmESJnjpYuW0YMECzNHnz5/Pnz9/9+7dA10pxhrsYmMY5sUBxj9eVZrzv5ggITIyskCBApMmTTLKALO/fPnyAdmtzyjCncgwjB9gFxvDMAkTcQyKzbFNI2fOnJ7/tsz4mbCwMOrBr776SiU/HfuSPHlyX1eMYRjGuzx8+LBWrVqLFy8OdEUY59DuQvnyRz1lypRx40Raxm9wJzIM4wfYxcYwTMJk3rx5wsWWNWvWffv2BbpGjDWio6PFsSZFihQ5duyY0e03dsd2gI0bN4qzb8aOHcuRIAzDxBcwX9WsWTNor6Blbt68SS+X6dOnO83w7NmzIUOGjBkzxs8VY9ThTmQYxj+wi41hmATLihUrevfu/e233/IRbPGOw4cP9+jRo/t/QYrRhVNYE3fXoX6kEcMwTAB5/vz5rVu3Al0LxowSJUqQg6Zp06Zz587dtWvXX3/9tWfPnlWrVg0cOLBYsWJDhgwJdB0ZF3AnMgzjB9jFxjAMwzAMwzAMY0h0dHTt2rX1F1CGhIR06tTp0qVLga4g4xruRIZh/AC72BiGYRiGYRiGYVxw7ty5//3vfwMHDuzevfuwYcMWLVp0/fr1QFeKsQZ3IsMwPoVdbAzDMAzDMAzDMAzDMAzjEexiYxiGYRiGYRiGYRiGYRiPYBcbwzAMwzAMwzAMwzAMw3gEu9gYhmEYhmEYhmEYhmEYxiPYxcYwDMMwDMMwDMMwDMMwHsEuNoZhGIZhGIZhGIZhGIbxCHaxMQzDMAzDMAzDMAzDMIxHsIuNYRiGYRiGYRiGYRiGYTyCXWwMY5mzZ89OnDhxw4YNPsrPBIQnT56sXbu2X79+rVu3bteu3bBhw06ePBnoSiUQVq5c2atXr7///jvQFXkROXr06ODBg6HVHTt2nD17NvQ80DVyn0ePHq1evfrzzz8PdEUYhmEYhmEYxgnsYmMYVY4cOfLRRx/ly5fP5mDq1Knezc8EkGPHjhUrVqx79+6nTp06dOhQnTp10GUhISErVqwIdNXiPXfu3EmRIgXkWb9+/UDX5YXjiy++ePvtt8PDw0eOHEkTUefOnQNdKXeYMGFCzZo1SZEyZswY6OokBGJjYzds2NCrV69nz54Fui5ucvbs2bFjx+7cuTPQFWEYhmEYhvl/sIuNYVS5e/duVFTUsGHDFF1mVvMzgeLKlSuvvPJKgwYNRMrDhw8rVKiAXuvQoUMAK5YwePLkSdasWSHMLl26BLouLxYLFiyA2Hft2kV/9urVC39WrVo1sLVyj6tXrx44cCB//vzsYvOcyZMn165dO1WqVPRuineBjZGRkVDmQoUKUf3nz58f6BoxDMMwDMP8P9jFxsQnYGIFugr/546x5DKzmp/xP926dUMHabYx3rhxY+jQoadOnQpUrYIHz8cdhLl+/XojSz7g4/r48eOPHz8ObB3sPpBDmTJloNj//PMP/Qn5L1269Nq1a959ij/p1KkTu9g85+rVq4cPHy5atGg8dbFhtF6+fPnzzz9nFxvDMAzDMMEGu9iYeMOvv/7avXv3QNfi/5wFllxmVvMzfubmzZvJkiVLkiTJ8+fPA12XYMTX4y7g4/rBgwdFixbFOA1gHew+kMPp06dp5nn06JEXiw0sEBG72LxF7969/eZii4iIwEzr3TJ37drFLjaGYRiGYYINv7rYnj17dv78+YMHD+5wsH///suXL+sPAYHBc+zYMWTYunXr7t27z5079/TpU6My//nnn6NHj/71118+rjsTYNDLKVOmZBcb43VWrVqF3kmXLl2gKxKM+HrcBcO4btu2LRQgsC42X8hh0aJF7GJjTBBRYL52scXGxpYtWxbrOu8Wu2/fPnaxMQzDMAwTbPjPxfb48eP9+/dv0YFE2ct269atHTt2aPLs2bMnLi5OX+bTp0+pTHHWDJMggfX72muvYSXNLjbG60yaNImNdqf4etwFw7ieMmUKDc8Auth8JIfvv/+eXWyMCX5zsXXt2hVPYRcbwzAMw7zI3Llz5/jx47t37966deuuXbvw//v372vyxMbGnj59Gq/4bdu2hYeHHzp0SB8F//z588uXLx88eHC7A6d5Aov/XGynTp0ifxmEdebMGfwJ4VLK+fPnKc/jx48hTUqE1JANmenPEydOyKU9e/YMZgmkT5+yiy14gNLv3bu3T58+jRs3tjvCDHv37p03b17YkB9//PHdu3c1+bG4nzNnTr169apXr166dOmGDRv+9NNPcoa///67YMGCtJIuUKDA+w5mzZqFb4WGhtKfM2fOpMzQq86dO7//L5s2bZKLunLlyogRI9q2bYv/79mzp1KlSihw9uzZ8rN69uxZuXLlKlWq4NMuXbpcunRJU2Evuthctt3ucDqjsciwYcMG/LlmzZp33nkna9asb7/99urVq50+MS4ubuzYsTVq1MiXLx8yQ/7r1q0T5zGRHJAopIRHUPqkSZPatWtHiXprX0U4ihWQiY6O7tu3L4rNkSNH7dq1x40b59Sfrsdlb9odgTzNmzdHetGiRTt06IAZQ/70119/RUvpQKJkyZK9L9GmTRsoMFqaO3fuBw8eiK9YVW/FBkJvhw0bVq5cOXoEKob/v/LKK/j3jz/+oDx4LX355ZdvvPFGtmzZatasaXSJnnmT7coaZTTuTHrEBJSGBpLQPCzfXJ7/+9//oBKiHzt27Ij3LsSL/1BK+/bt8XKhzOKSTdCsWTPKcPv2bbvj9xtI47333sObG+O0f//+uXLlql+/Pn1qVxu8Iuf06dMbNWqE4VC4cOEWLVrgNacoB1IGFN60aVN06yeffDJhwgTN21APje633nqLim3dujUVO3nyZDnbw4cPx4wZU758eTw3Z86c1apVQz31MePmA81bqqs4vbjhYjOXv1VpuDEhBy3+cbH98MMP9BR2sTEMwzDMCwvWk8L5I3P9+nWRB8vssLAwfR75vGyszbCS1+e5cOFCIJrlHD+52LDyJpliaYuFLCViAS28aZQSERFBKUeOHKEUGLfC6SaOo9aHubGLLUhYtWpVsWLFaNX75ptvHj58GLYKDEgYNpRYsWJFOf/du3dh0sAeQ067Y8zAskI2mIgiD5Rh0aJFadKkQXqdOnUWOSCdESts2M8iP5QNVjelw96mRCzBYbklSpSI6rB3797UqVNTnrx584o8iRMnhvVODnXYsenSpYNNqDFoveVic9l2mD2hoaFJkiShr69YsQIfodplypRJmzYtUtCc9evXax537dq14sWLo2T859GjRyKSxebYCwnGjx9Pj4PNSemXL18WX4+MjIRAkIiKycUqCke9AsTcuXOhGzBZDxw4gAaS8uC70dHRJiJV6U2IvW7duu3atdu0adPu3bu/+OIL1D9p0qQ//vijKAdfnDNnTu3atfHFlClTzvkX1AfGdqZMmTT2p1X1Vmkg5jcY50I+eP2gaWhFgwYNIF4kQgHwXVQ1d+7cRYsWbdiwYZYsWZCeKlUqzQZ5l022pFEm484SeHq5cuXoia+//rpId698FYVB2zNkyEBPxP8pcfv27fizRYsWMTExQhp4IqYOyokyqQ54DfXo0QP6T+l//vlny5YthQ6Ta0ll4iKQoWTJkk2aNMF/kA31oWschw8friIHFIv2Xr161e74Yemzzz5DNuG6MmLt2rUoBH1Ndf7111+pWNm3BQEWKlQIykYXeuARTZs2JWGKdYz5QPOi6qpPL1ZdbC7lry4N9ybkYMbcxQY1a9OmDcbsa6+9hv8YORDxwv3ll1+aN28OAebPn//dd99dvHix2JogLtQG9evXJ1fv2bNn3XhQbGws3h2QNnQMU8pXX33FZ7ExDMMwTLzg4cOHwr+GpS9WAlgf0p87duygdQhWFFinUSJsfORBTuHtEbEa586do5SwsLAzZ85grSjyiKiRgOMnF9vjx4+p5fKNabdv39Y4yPAppQgryO44pIYShRGld1uyiy14QF+XKlUKq95MmTJVqFAB3UfpImBk8+bNIjNsKqTA/hEp6GXKprneETaVzdlGKvKDyC42cOHCBSpEuNguX76MkZw+fXokwtiD+XTx4kVYyy+//PJHH31kd8QmhISE4FNRYbvDvkUKhW8IvOViU2z7ggULKLFgwYIjRoyggB1YgNmzZ0ciTFzN48hxFh4eLlJ69OhBJcydO1f28X/33XeULrvYAFnmsotNXTiWKgBTKmnSpMKfDs6fP48U5IShZSxR172JmbpixYqw+uRvde7cGflhyZ88eVJO/+STT2zOzmKjDgJyoiX1Vmwg3igwO8klgQ7dvn07pUNz0CKkw56sVKlSREQEpWN6JLVHDUUh6k22pFFG404ddDckkDVrVtt/XWxulK+uMKKNaCCldOvWrUaNGvqjPzEqKafYKHrv3j0o2Mcff0zpDRo0wEiBgjVs2DBz5szU44qD9/Tp0y+99FKrVq3kmzRQVcqJJYK5HPBCROI333wjUlD/N954Y9myZSrimjx5Mj1IH0CKTkmZMuVrr70WGxsrEqEJderUQf5s2bLduXPHrjDQvKK6lqYXSy42RfkrSoOwOiEHM0YuNrS3WbNmUPj169djjTtp0iTyS/bp00dzJ8ypU6cwDVarVo1O8/jrr7/y5MmDnI0bN45zsHjxYuoygHLI1SsWeOoPunbtGhSpcOHCWOw9ffoUCta1a1eaVWzsYmMYhmGY4AZrLXLaiB9Z8TYXuxXJNSZcQ1gSiBW7cATRYhLfIlcd/hVhW1gkUB6vx8u7jZ9cbBDHPw5gvYjEyMhIjThEeJp8dszZs2dlydodJhCBdS272IIQMrpgBcmm3YMHDyga4quvvhKJ1atXR8q7774rf51s5t9++01ONDLFybDRuNigGLTyFi42onLlykhE+fpQUugefUXeWDdmzBikwPSSc3rLxabYdljs9PWRI0fKOck6Sp48uWyKiDsE5R2LR44cocTp06fLJfz444+UrnGxkXNBdrGpC0e9AjDq8uXLV7duXY24YK1RZjHejTDpzVmzZuEjWH1yIsUxgQ8++EBON3KxifgLTbqieltq4Pjx4522WsRYid30BJqAxBIlSrjRZEsa5bmLjXjvvfdsnrnYrCoMjHwkpk6d+sqVKxs2bEifPr3TjYd6FxuxadMmSidfkgbFwfvOO+8kSZJE03dYE1DJsq/QqRzICf7pp5/Kid9//72iQ8HExdawYUP99GiXdEOuiclAs3tDddWnF7tFF5ui/C1Jw9LwCXKcutiwqK1RowY0XM45ceJEyimrN3o8S5YsderUkb8+evRoyjlv3jxK+fnnnylFs/BVf9D9+/dfffVVvJLkvSSAIg1t7GJjGIZhmOAGFqI+jurw4cOUSNs1oqOj6U/5R2jhm6N9BjAw6U/5d1lA3jqs8fxwSboKfr1RlMACFOZoVFQUOdRgBNLekKdPn4qoNFk6GsnK6OPgmGCAjKjcuXNr0il+oVu3biIFvd+yZUvNcVHJkiWz6RxSXnGxkWFcunRpfZ2hfr169Ro8eLCc+NVXX+nNOW+52BTbDvuQvg5DRc4pYtBkq2Pu3LmUeO3aNTlz5syZkfjZZ5/JieouNnXhqFfgjz/+QAqM2zn/hSJHwC+//GI3xaQ3y5YtmyhRIkhMLlkcCZQnTx45s1UXm6J6W2qgkTdk+PDhlK45sZ5sY0jVjSZb0ihvudjIGPbExWZVYSIjI9GnNsf2tFy5cmkaKzBysQm/z5o1a/TfUhm8e/bssTnbOww2btwoh3kayYHcpilSpFi7dq1IvHnzpmZVYYSRUgmXt9NtuVWqVLE59jyKU+dMBprJU9RVV316sVtxsSnK36o0LA2fIMepi23evHk23WZkaB3lLFy4sEikLfayp9juOGkFGot0TD6UYuRiU38Q6RImZE39V65cSZnZxcYwDMMwwcz9+/cp3EosOZ4/f75z507y5JAv6PHjx5RHXjqKfaBYYNilgLXTp0/L5YtLNeWdBwEkAC424X0kX6NYucbGxop0+XdgcWSb/lgWdrEFJ0Y+CKfuMJndu3d36NCBooHkE7vsXnWxOTW6NGB8wlQuVKiQzXFykPyRj24UNWq7kUXn1EEmXCoa479s2bJInDBhgssS7M5cbBpMhKNeATpVCn3R0YAVK1YYS+v/MOpNzDCJEyeGmWdUcufOneUZxlsuNo0qWmqgkZ+CHA16PwXVDdriRpMtaVTwuNjcUBhxDmDNmjWNinXpYvvzzz9d1s3p4B06dKhNFzJphFM5oEp0yBfpldU7T42Uavbs2U6bTIiDLMPCwijFfNr0UHX1mEwvdisuNkX5W5WGpeET5Dh1saGjbY5Xp8aX/dJLL1Fm+vmEdjEXKVJEX+yRI0dWrlwpboowcrEpPuj69et0AqB+BcjXHTAMwzBMvCMuLu727dvHjx936iwjsIq4d+8eFl1i6yitK4TzR/6FDzaOuCTB6mrZRwTYxbbFccQduRvFeW0aF9uVK1c0+0kF7GILTqy62DBmsESuVavWgAEDLl26RMEggXKxRURE9OzZs379+suWLRs1apTezPOui81l2y1ZdIcOHaJEmJdyZrpbUD4mzKgEu6mLzaVw1CvQrFkzpGiuOLSEUW9iyrY5c5kZ4SMXm6UGuuenEHWz1OR46mJzQ2HwHqHz+NE1Rj9qeeJiMx+8LVq0wJ89evRQqaqRHFavXk3Fgpdeeun7779X34dopFTCsSLH4Qt+++03zeTpCxebfljZFaYXuxUXm6L8rUpDffhAc8rqUPmBx2/oXWxYzoaEhCRJksTIkQ1oRzBFljVo0MDlU5y62NQfBGWgr9NP3DLsYmMYhmGYeId8iQH+73RlK0KswM6dO+noW7vDPSfSxalEwlkEoqKi/NcSYwLgYiMePHgAa5xkERYW9uzZM1lk4vdPcPHiRUrUHFJuZxdbsGLJxYbuK1iwYOPGjcXWwkC52KCTMPAyZ878+++/UwpZib5zsam03WrQROvWrW0OB5lIj4yMRLHy0ezmJTh1sSkKR70CtWrVsunOmbKEUW9iIqZ2KYYK+8jFZqmBHvopLDU5nrrY3FAYvFYoUgZ06dLFaR63XWwuBy9to9MfHucUEzns2bOnSJEitn+pWbOm4n1JRkolrh8RtxPIiPP7xDULfnCxqU8v6i42RflblYb68Jk/f75NR+LEiV3W3G/oXWzkrE+UKJFLTy5ds6u/j0KPUxeb+oPocLfUqVPrP2IXG8MwDMPEO8QNBsLDo18MyC42imITXrZTp05R4rZt21DUwYMH5ZzieszAEjAXm91h/0A0JI6bN29CuEI68sVeERERlHjmzBlNCexiC07UXWxYGcPkqFatmnzTX0BcbA8fPnzzzTdt/4208qmLTbHtVl1smID69u2LkvPlywezcM6cOcWKFevQoYPYke2yBL2LTV046hX48MMPbf899dwqRr158eJFapfixYs+crFZaqCHfgpLTY6nLjY3FObrr7+uUKFC+/btqV1OfSjuudhUBm+nTp1IT1TizszlgBfi6NGj6bJFUKVKFZcF2o2Vavr06ZSuuVKGELcBCF3ytYvN0vSi7mJTlL9VaagPn/v375/X4fTKiEChd7EJZ73L7a7kwSxfvrzLpzh1sak/qF27dk4Vyc4uNoZhGIaJnzx9+jQyMlI4gpwuBrB+u3Xr1q5duyiPOIkYq+I9e/bIbjWs1sSxboq/Q/saP7nY7t27d8qBRoIikI2C+oQQ5esIhatSL312sQUnij6ImJgYOo984cKFcraAuNi++OILm+5kGd+52NTb7sbRP3v37oURjvwTJkz45ZdfxO3IGtRdbOrCUa+AuHjO6H5l9LUczarHqDefPXtGYmzatKnTL+7evXvWrFniTx+52Cw10EM/haUmx1MXm1WFOXHiRJo0aY4fP46xRrdtFCxY8PHjx5pvueFiUxy84qrNJUuW6GuLmsg+HadyWL9+vRyWePHixZIlS1KZmqtjnWKkVKJpTs8po62RiRMnFlc++drFZml6UXexKcrfqjQS9llsly5dcto6PZ07d0a2DBkyuLy6y6mLTf1B3bp1o5z6H1nZxcYwDMMw8Rdx1Nr+/fuN8mB5KVxpYsmBBf/Zs2fxrbCwsEOHDiHPgQMHKM+DBw/8VX0z/ORiu3//PjU7PDxc/OwP6Yij6SjCRdwZAVuC8iCz8Erqw3DYxRacKPogVq9erTdi4+LiYM/YdC62V155xebsHLf8+fMjvUWLFnIibUKxWXGx0WFhmo+GDBmiN/O84mJTb7tVi27v3r01a9aU40CNELd/arZg06FXsotNXTjqFdi0aRM9/Z133tEbaWPHjh03bpx5CSa9WblyZSp8/fr1mo+ioqLKli177949keIjF5ulBnrup1BvsiWNMhp3AI0y94HKGLnYTMrXYEmeyAClFZdU0t2FQHNtJcAU4XQcmbjYFAcvnQcPChUqpLll8vnz5x06dNi2bZu5HFAUniWnQD2SJk2KnMuXL3cuJgkjpYJw0BFIT5MmzcOHDzXfomsl5CPMfO1iszS9qLvYFOVvVRoJ28UGySRPnhwp6HSnX4EkBwwYgP9MnDiRvituDtUAgdB/nLrY1B/07bff0tdFgQJ2sTEMwzBMvADLJwq3kpeFwn22c+dOu+O2UMojfte0OxYMW7dupWz6dZrIEx4eTuFs6raJT/GTi02+6OH48eO3b9+GTA8fPkwp27dvJ3FgUSX21kZGRiIb1mRC9PrtHuxiC07atGnj1AdBN4V9+OGH9OeiRYtofdyzZ0+RR1i8w4cPl79brFgxJFauXJn+hKrQMKtbty5ZXMKIunXrVvPmzUNCQpA+YsQIuZAqVaogsXTp0vo6k5WVIkUKuhLY7hjn9FBYzvJwjYqKohpOmTJFRRpO86u3/cyZM04tOmF4CH+03TFVQRRNmzbVmJRO2bNnD5UAa1YkrlmzhgJqYP+IkB914ViqgPAKvfvuu2L/1M2bNz/55JPChQu7/BXCpDc3btxIJcNEnz17tqjhhg0b8ubNK4ewga5duzo15gcOHEiFaEKfFNXbUgNFxI3GT0GHvgPNDwwU+APELxbqTbakUUbjbvny5ZkyZUqTJg2eZVeAxmn+/Pk16UblO0Vdnhj4r732mvwWr1evHr6YJEkSvHfkMpcsWUJlbtq0iVKoZLFDECNCUw31wUsn7oM8efKsW7eOahgREYEB0q5dO5dygFbowxLJIXXp0iUjKQmE8uBlqvkIL036aMaMGXJ6bGxs5syZ0bOyHpoMNLs3VFd9egEfffQR0tOnT++y+XZl+VuShqXhE+Q4vVGUutvmzG+FAVWrVq2DBw/i/xhHlC179uz63a/ffffd2LFj6f9z5syhnJprphUfJN5TRYsW1WQTLrZ58+ZpPlK/FYRhGIZhGF8j7g8Viz27dOAaLc7FrQXILPKIezK3bduGlztWLMcdnDx5UqwkhauOVg7BgP/OYsOieYsBV69epTwQnPC7ycDacXoDK7vYghMYY1j1hoSEyH4WDBtaDYuDhGD4pUyZkhLbtm2L5X7JkiU/++yzvHnzIiVHjhzDhg0TPjKyrMDo0aNh29SuXZu2UC1cuFAYUYMGDerYsSNW/KtWraKdXPi3W7duZI5iTObMmZMS9afCUygTwNNhBKI+MPz69+9PibDHQkNDz58/j5ww1SixV69eKtJwml+97bDwKRtqKBdL+3QARodIFAfckMmaJUuW/PnzlypVqmrVql27dtWcRQXbtXjx4pS5VatWkB66pnr16mPGjBE9NXPmTEvCsVQBGEgZMmSgzLClkbNgwYJJkyZF8116EMx70y6d4GNz7GZCS2m3IASryVmzZk2ntjFkQumHDh2S0xXV21IDRW9qNtXSAWRgx44dcjq6gNJlh5Fiky1plNG4o8sHqJddXo+NiR3DkzLL8YMm5TtFUZ5QM/TO4sWL5e+KyFZ8Rf5x7PLlyxR99tZbby1atKh79+7Tpk1D+owZMyi/xk1vtzJ4L1y4QGG2BGpF/uty5cppPIlO5UDeK3mfY1RUVOrUqZHZXOAEhaMCTSgcMWHCBNQnWbJkQrUwpqDz2bJlk5XN5UDzXHXVpxdQvnx5Sr9586ZLCajLX1EadovDJ8j59NNPqc7yrwjihockSZJ8++23Ih4Z02DFihXla0PEhJMpUyaMHXJEol8wFjD5iC9u2LCBsomd0eSSU39QgwYNKGffvn3l+gt3rXDnEStWrMAweeONN1SUhGEYhmEYX4P1NjltsKy6evUqzAGYTlgJUCIt85AonD9IuXv3LkyM3bt3U4owx8QGx1OnTmFpCnOMQthkn1LA8et1BzAPIFbZdxYWFqa5WhXrWhG5JnrC6OA6drEFG+jQ+vXrC5PmzTffnDx5MtK///77AgUKiPRGjRrt3bvX7tjAhaUwJSLD2rVr7dK6GV8XQ+XcuXNk6QEsnSMiIsRDYdCSkWxz/NBN27nTp09frFixL7/88vTp03bHPrJChQqJCrz22mtYrMuFQJeqVatGn8Jox/oeBgMGLYUmwQb47rvvjhw5AuOWnHeU2KZNm6VLlxpJwzy/StsHDhxIO8hsDvdEx44dT5w4gUkHtk2iRIkoPXv27CJw5vnz5wMGDKCtZE6ZNGmSXEOUBonRR7AwBw0aBDsHXYaKwbyEbU+GqIpw3KsA2vL222+L7kNR3bt3d+mycdmbBBpCFjVRuHDhlStXyhn+/PNP4UezOSx8GPZ2h02IdCHhHDlykGlnVb1VGrh58+bQ0FAKuqRKohcgdsx777//vkjPmjUrDFd8Ee+V5s2bi7rlzp178ODBwkJ22WSrGmU07qZOnSrqhhnYqKeePn2KJ5YrV05UCaPy888/F6FJJuPaKS7l2alTJxpWzZo1E04fvNeFZ4c6VA4phcApPXny5FCt48ePt2jRQugwmok/NZvU1CcujB3URMgWMods9duoncph/PjxJUuWRHrLli2//fbbMWPGQNWhBvpz3zWMGzeOwgaJtGnToqM1u+btjvgglA8ZQmM/+OCD/Pnzo6qyMM0HmrdUV3F6+frrrytVqiTrNkarJnROj6L8VaRhtz58gpwaNWpQneWfi+2Su9Dm2D9bvHhx2gXfuHFjOagwMjJSvuvW5vC1kQTknytu3rxJxxRCfxYsWDBkyBBxL7Dig/7++29Ktzlu1MXkM3/+fAwKoQ9Qm+rVq4soOUwRlK54mAPDMAzDMD7l2bNnMI6cxlphASZe+li6O82zbdu2+/fvUx4sP5zmOXDggHwLWWDx942iT548iYmJuXTp0pUrV27dumV0UC65Ni9cuBAdHe3yMF0mXgMTCMNGs3sLgw2mi2avx4MHD8LCwo4cOaIvBLq0fft22T53aavrwePobg05yAWWHqpnElnjCeptV+ebb76BqX/69OkNGzbMmzfvhx9+mDRp0siRIz/55JMSJUrAFNGEb2AyOnnyZHh4uNhnd/XqVf1mPXXhWK2A3dGzML/Rs/rT6D0HmrB161aNK9/P+LSBerzbZKNxh0GHFyEM47Nnz/qifPOveFeeaIJGt11iafBiTKF8VFjcOK5HLwdx7Q/eg5jf0GRNDKBXwHt28+bNmAECeAeTr+deFfkTwSANPzBx4kSxTxPkypWrT58+586dExkwb1MMLJEtWzak6M83wXpXdrMmTpz4o48+0o+jcePGUQbk7N27t1yO4oNu3LjRqFEj4fhOlixZ//79d+/enShRoqpVq/7444+ys5Wc3SlSpNBsTWUYhmEYJlA8evTo6NGjGr/YsWPH5F+O6R4DcfgasXfvXs1PqhcvXhS3kRJYkKscRO43/O1iYxjGdwwYMOCNN94wcuEjvUKFCprLDRJYBRh/cuTIEaNT8BmGie/Qtg4sZM1/8rl58+b27dv37dtnEl9Jvsvo6GhPHoTVM9bZeBYtte/evas/Z5A4cOCAywhHhmEYhmH8zL1797AYwKrg2rVrIjBNA5YT169fx6ogKirq9u3bTtcGWBKghPPnz2MJIX6TDh7YxcYwCYQVK1bYdNdEaKhYsaLvwkIDXgHGn8CuLleunCaMi2EYhmEYhmEY5oWFXWwMk0Do2LGjzXEpodHuuVGjRn311VcJuAKM34iMjKxevTrdsc0wDMMwDMMwDMPY2cXGMAmGuXPn0jk1xYoVmzRp0vbt20+fPn3gwIG1a9d++eWXpUqV+vzzzxN2BRi/ERsbaxTdzTAMwzAMwzAM82LCLjaGSThMnjw5TZo0Nh3Nmzc/c+bMi1ABhmEYhmEYhmEYhgkI7GJjmATF/fv3f//995EjR3br1m3QoEE///zzxYsXX6gKMAzDMAzDMAzDMIz/YRcbwzAMwzAMwzAMwzAMw3gEu9gYhmEYhmEYhmEYhmEYxiPYxcYwDMMwDMMwDMMwDMMwHsEuNoZhGIZhGIZhGIZhGIbxCHaxMQzDMAzDMAzDMAzDMIxHsIuNYRiGYRiGYRiGYRiGYTyCXWwMwzAMwzAMwzAMwzAM4xHsYmMYhmEYhmEYhmEYhmEYj2AXG8MwDMMwDMMwDMMwDMN4BLvYmATL1q1bu3btunPnzkBXJLh4/vx5eHh4v379YmJiAl0XbxIZGfnDDz/MnDkz0BXxAkZ9xCrNmPDw4cOVK1cOHTo00BXxPmfOnBk7duyOHTsCXRGGYRiGYRiGMYNdbEzCJC4uLlOmTDabLXv27M+ePQt0dYKCTZs2tW7dmsQCLl++HOgaeYETJ0507dq1cOHC1KgPPvgg0DXyCJM+YpVmjFi6dGndunVTpEgB9ciXL1+gq+M1YmJievXqlT9/fhoOc+bMCXSNGIZhGIZhGMYMdrExCZZixYrBKitTpkygKxIs/PPPP2fPnq1UqVJCcrHdu3cvOjp62rRpCcPFZt5HrNKMU2JiYvbt25chQ4YE5mKLi4u7ePFiz5492cUWH3n+/PmBAwdmzpz5zTffrFixApMbpe/atev06dNuF/vkyZOtW7f269fv+vXrRs9dt25d7969W7Ro0aVLl6VLlyLFjafs3Lnz559//vrrr/F+WbBgwfHjx0U5e/bsOXr0qNtN8Dp4Dw4bNmzMmDEPHz4MdF3iAefPn7906ZIm8caNG6tXr544ceKsWbMOHjxIfY1/f/nlF5cFXr16dcmSJVOnToW24OsbNmy4c+cOffTs2bOffvpJ/H/Lli3ebMmLjcupwEdQVHVA9hNgRh05cmRoaCgmtx49eixcuDA2Ntb/1WAYxiXsYmMCCdapviv87t27a9asefDggedF4f2NNZnn5QQDWIgnJBcbgZVrokSJEoCLjTDqIy+qNONTfDqz2Q1mpIoVKyYwFxvx559/Br+LLSG9I7zC/v37y5Urh17LkCFDyZIlU6dOHRISUqlSpf79++fJk2fGjBlulPntt9/Wq1cvTZo0pA9OBf7PP/9UqVKle/fuu3btwuuAcn7++efqT4mIiOjatWu6dOnwRTyrRIkSZcuWRf3x58svv9ywYcPevXtnzpzZvSb4iClTplBLg6pWwckPP/zQqFEj4fAFjx8/HjFiRIoUKRInTlygQAEKm82aNWu7du1CQ0PxH6Oinj59Om/evLfeeouE/+qrr2ISzps3L/6PokqVKgU9hMaKEp4/f46XO8rEq9zn7UzQqEwFXkcTVT1//nw/PFRw48aN+vXrV61aNSwsDO39+uuvqRpQOTd+QmAYxtewi40JGFu3bn3nnXcCXQvXPHv2rHbt2jDzAl0R7/Dll18mPBcbSJYsWYJxsSXUPnpB8PXMZjQj4aEJ0sW2ZcuWIHexJbB3hOecOnUqVapUiRIlmj59Ou1qx7+7du0qXrw4daV7JwZevXr12LFjwqPh1K5u0qRJxowZnzx5Ynd4QNAvyIlElfJhqY4fPz5p0qT4SokSJVatWhUXF0cfof5oVLNmzWz/MnnyZDea4CMWL15Mtfrjjz8CXZfgBZ3YqVOnVq1akXoIOnbsCNGVK1fu3LlzlBITEzNixIiQkBCkQ401+Ym///67dOnSyJAkSZLPP/9c1sbbt29jshIHPqRLl07+4q+//opniTA3xg1UpgKvQ1HVPXr08L+L7dGjR5g88+bNK6vNd999xwtFhgla/Opiw+sN8+DBgwd3ONi/fz/mBf2hQg8ePMDUiQwwVHbv3o13HtZJmjz3798/fvw4PkUerNuOHj2KV5q/2sF4gUuXLmH9UbFixUBXxDUDBgzAOyzBmE8J1X3DLjYmGPDDzGY0I7GLLVAksHeE57z55psQSKdOnTTpsbGxbdq0wUcdOnRwu/Dhw4cb2dVnzpxBetmyZUXKvXv3Fi1aJIcsGfH8+fP27dtTyXiP6JedxOLFi+ldM2rUKLeb4Av27dvn4d7VvXv3eqsyQQj6FwpZuXJljb9s1apV1On6raMwLlKlSuX0owMHDqRNm5aCNI3kduPGjTp16iBPSEiI5qOJEyeWL1+ed/V6iMlU4C30nSuiqv3pYps0aZLTJ/7222/Tpk3z0UOjo6MvXrzo9WIT9jzDMAL/udgeP368f//+LTqQKHvZbt26tWPHDk2ePXv2iN8SwbVr17Zu3aovKiIiwm/NYTzhzp07tAQPfhcbjDp6myYY8ymhum/YxcYEHD/MbCYzErvYAkLCe0d4yI0bN0ggP/zwg/7Thw8fFi9evHbt2m6X/9VXXxnZ1QMHDkS6ezGkn332GRVbrlw58/tkZsyYgWyDBg1y4ylBCxbV1atXD3QtfAjeqkmTJj158qQmvVu3bujNbNmyOf3W3Llz8emuXbvkRChe5syZSVvWrFlj8tC7d+8WLFgQ2WQTxu7w91WuXLljx45uNYX5f5hMBV7B6aAQ7yO/udiePn1K+nbo0CH/PNHuiImpVauW148OTPDzDMMI/OdiO3XqFDnCwsPDz5w5gz+Fm0xMjo8fP962bRslHjx4ENmQmf48ceIE5cGLKiwsjBL37dv3999/Y9IRXjaV3yoZP4BlR+PGjZs0adKiRYsPP/xw6tSpv/76K32ErqdT20GmTJned9C7d2/6FCsP6ED79u1nzpxpd1gvRYsWLVGixLp160ThV69eHTp0aJUqVWrUqFGmTJlWrVqtWrVKX4crV65MnDixdOnSmtNAjx49OmTIkDfeeMPueItMmzatVKlSWGDVrFkTOinnxJosceLEVFW8Faiq27dvV2mmJVRahLXaggUL8Cz6zer06dOtW7fOkSPH66+//umnnz569MhpyRg4HTp0KOAAVg3E6Lb7RqVr7t+/P3r06Dp16uTMmbNs2bI9evTACNUXFRMT069fv/fee6958+YQHWyVUaNG3bx5U5MNvYNnodqFCxfOnj07nvXJJ59cuHDBafX0Lrbhw4e/L/Hxxx/funWLPsI00qVLF0rv1KmTXKZiE7zV9XYrfWSk0or1URw4BB4N26NSpUqvvvoqpDFgwACMDv3eFpjTkydPJpsW5aNMyK1du3ZyDIiiSBVz4n0xfvz4t956i4SzZ88etBrjN2/evJhGRFzA7t27UY38+fPnyZMHIwV1c/pEvE1CQ0MxAyAbBAjjWXOsifq4M5/ZCA/VxnxGkl1s165d69OnDwYOJIOcejtQZTjbHWFB3bt3L168OIqFJtSrV2/27NmyiKKioiAHMcqEDbBhwwZotUh3ulJX1DGNi23ZsmWYqzEhoML4ununGqlMQWjm6tWrmzVrhiFToUKFatWq4SuaeHmX74gXkE2bNpFAoBhOM0Cq6Du3yzexq9999133XGzQWzrNE2zcuNFl/sqVK+NlZPUpQQvF3saLgzvcY+/evSEhIZhh9B+hK22O3aBG5gPeNYsXL5ZTGjVqRKqCucvlo2k46AvHDIl0lbsUGCN86mIzGhT+d7EdOXKEnojXsX+eaP83NNu7LrYEP88wKmCNJ29DxP+x8jfKjCX9sWPHjjrQRxNjzXbgwIFtDvbv3x8ZGRlU5xL6ycWGNpNDDVIQJhCEJbxplBIREUEpmFAo5cGDB8Lp9vjxY7vDihPhb0KUJ0+epEQYOf5pEWPC8OHDM2bMiGFDf8K6S548OQwP+hPjZNGiRTD8MH0XKlRokYO1a9eiZ2GOwnaldwnsdgqNJsSkjHVJypQpscSBbW93jFVYPsgwYcIEUQFYrTCKxIpZmMGwHsXZDcmSJbt+/TpWV5kzZy5dujRqaHPE80PfKPPTp0+xrkKVKP/QoUOpqsIdY95MdVRa1KlTJ6ohwKri559/Tp06dcmSJXPlykWJsDn1JaO2qVKl6tmzJ9UZVkSZMmVI8pZcbIpds379epj048aNw9SJwdi2bVt8mjZtWs3yFKVlzZoVtaL9GmgvDF3k1DhT6GJNGPY7duxAztjY2OnTp8OaRcPxH/00qnexIU+XLl2oktA0zcafuLi4ihUrQj7yqkWxCd7qertyHxmptHp9VNRMsGzZsjRp0vTt2xdiv3XrVr9+/UR3p3OAJy5cuLBWrVp0Wg1Srl279tprr4lsYmWmKFKVnDt37oSei0dg2u/WrRtWbKhG2bJlKbFNmzbPnj2DbY8vVq9eHfnpZCUoksYviTdRaGho1apVYfDjJY0xlSVLFuSsV6+eMIcsjTujmc1SN5ngckYSLja8UtEWjDKMIHQ65V+6dCllUxzOGD5TpkzB1wcOHBgdHW13uBcrVKiAPNAc2aSBwMW58rLTFkNMXAb6448/apqjomOUU5g0s2fPxoiGymGMiDOnS5UqZXVRpTIFYb1Rv359KA/eGhTTtHLlSuSBil65ckWxR15MMImRQKA8TpdkkFuRIkXcLt/ErqYLFtww4erWrUtlYppVyf/bb7917tzZ6lOCExF7m4BNX0zaaKDTe2wbNmxIXf/hhx86/e4333wj78Xbs2ePmKnEctEcvBlh++nT8R556aWX+FA2t/Gdi81kUPjfxbZkyRIfNdMIEZrtRRfbizDPMC7B8snpNkSjS4GxrhZ5xOKZEE4kGfni74DjJxcbVqvUeFgyIvH27duUKGKw8SmlxMTEiGxCvrTKh+FNf8oOAuQXcW3+aRFjxLlz5xIlSgTrRU4cOXJk06ZN5RQKnpe3U927dw9jr3///jSzw+aB/Xzjxg0YWrDEvvzyS7tDkegKod9//118cfPmzTaHy0zEIMDCwVoKthAVJfsjYPXVqFHD5vCmlS5devny5ZQOc50O3YDJLdcTL1EqRLMJSLGZLlFskUgEBQoUaNmyJX1Ex4s4Xe3BHEVi165d5USYsm642FS6ZufOncmTJxdmPEEGeYoUKeQfH0JDQ5Eoj3HU6uWXXz527JhIwaeZMmVKnTo1jXoB7dqwOTtq2ulGUdScAuxRvn7vD6wpGPbiT8UmeKvr7Vb6yESlVeqjrmZ2x08dadOmzZIli3xmjfBtQT6YafFQ1A22dPbs2W2Oe/dat269Y8cOzOFvvfVWnjx5KGpMXSvUcwqPRokSJX766SfxNhUDoXbt2qNHjxYe1T/++MPpgrhBgwalSpWSHa/r16+nnN27d9dISX3c6Wc2wltqYzQj2f91sWXMmLFMmTIikOrMmTN0ZhDERSkqw5nqhk/lAWKXVsk5c+aULUPoFZWmiYsMCwujdI2LTVHHKF2YNEWKFOnVq5cIW6MdXmDZsmWWZKgyBUGFbA5XqfzFt99+Wy8Tkx55McHsBCUkmaCLMbTVv4s5BHN4yZIlMYc0adJE75m1O7Orw8PDKX4wQ4YMSMecL8In582b5/Kh6H0Riog5WaWe9+/fx0M1iXjFoMK1atWC2mBiRCswWel/eLc7wlK++OILzD92XSi9U6/N6tWrKfq1efPmTqNfMY9h+oJijxs3ztLX5djb/4+9t46zsnj//w/sIl2SEgICkitSEoKEwCIhtXR3Kh1SD0AWARGkEQWV7hTeiHSDsHSHoHRJLcICnt/rc64v12+869z3OfeJhXn+wYOdM/fck9fMdd3XzHC9KXxvUdjhw4dDrmLUFytWDEKMx6bHJSKWLFmC1yEDaO5y5cpNmTKFv8FDkjRu3JjbsWXLluJlqRDLKAj9pNlJRGgKyJo1q+avX3/9teMlkOqKHZ1qunXrRpGzZctmHJPBEIDUVYfT2X9Dhw41eFbhJsz+Bwo3YbXnrNs+Q5gZceZT08R340ItCmzpNsaDQmFiW7p0KXQKZDJfvnxYOeh5VZusZwUQX3g1fTkANWrUEHdmoC0++eSTsLCwgQMHik9hfUIfKclFHTItb968qEmeobCM6dGjB6b+OnXqqJ24RddsFM28a7Y3ckbtM96rVy896zM6D2Z/rLLI/71fv37Inl7NmxFfAKsOLN6QK7cSQOIxEO9sX8NgP3fu3L59++hP8qVQxEefVJjP+CcsWSkQCSIcHYz9sTS/ZwQEP5nYMP3/7UKcZlALVB28ruVT2EQFkm1qdNQaJOl+F4r1McWRxygGHEwJpLaJgTdv3vz000/FED1FlD2iP/jgA7VNBAOJfhW969ExKBBLTDFyhw4dKFzh8oOphcJ5sUKQ10zChAnFQD31yWQx3WK+RBg7FKi4HA0DhMLFtTUip02bNiQkhB0uGK4WqxtFDZoGsyOWDjly5FA8QmfWANGykDNnToSI1nYAzVm0j2N6Rhy0lDob5cuXp2ZSTJN6Z7GRqgxEfyKn61tKvHjx+DBX80Wwq+k9aCPNLm0mP5YGDtmwsMQRA/k7qmJhjRUVhWtuRTRZpZb6D39fRZbEyOxcAL1FkQ7qGeHQPzkEyymEzJ07VxEzffr0Dpf9nW27lsadU1+y2dVt3JrYkidPrtBe2rZtS4+I3vjGkvb06dNvuCCfRxFM0/Rg+/btOXD58uUUqDCxYVBTuEKjsNTHWKVRCAQonxSusHm5xYwIorsjoQ6JcUglLl68uBgoTWxqoBs7XgIx27dv3+joaONHyKsUXYK9SmnYYsgoFC21Xg0xTv6DaC+EQ5IsfomZGwC4BQF6vmdFPnv27Icffpg9e3ZSFZ48eQINE5pqkiRJpk2bxtHWrVtHRmqHypWepjAInx07dogpDx48OHXq1HxYCoYYYmK5Qn9evHixc+fOVFegT58+iowZPy763ubJk0fte0vOxaNHjybnYqigDpefKdu1PSiR07WSr1ChAh6krS1QB0h8QQ+/ceMGp8yqvtodEi3lcN2bYXxwnvPl9mHFpywGb2evZIfrU4TaeCpCEh40aNDA+L1umTFjBtJJmTKl3t0ahOgmLN4Y+/TpU/7MgPEiPmLc6IT5EWcmNT18Ny6cOl5s3ncb40HB8xHm9DZt2ii8qgsXLqxwojFfz2oQHwse0k0AhuFsF1jITZ48mdwFxFFv7KJOh6Bh3kyXLt3nn39OFg0o5p988gl+xZLGqXLNHjJkiEnXbG/kjNpnfOXKlRRTvTzG4g2dp1evXuT/3r17dy4g+b+LF9G4FV8Mb8IQv0NL7AW9iGw1PM+iv/GBYHySD4GeQK3GZjjRxBYVFUWBvNzFop1CoAv4rUTG+PVGUQLSB4stDHIyqG3bto3W/ahoNlWKtkxuEoNNoGyG4+EtCRSka8WJE2fChAliuOJ8Ez1FFK1MYm7kyJGa6Q8cOBBLJVFXxORKjyi8VDCFULjCxIbZiMIVp2MgZQoXHVb11CeTxTSDyRKhFBSoOAIGg4XCsdhSlEVzz4vHZ7EZNA1GMcJLlCgx+7/wfU/itiAsYRESFhYmfmo4deoU5+f8+fP0lHovodO1s5J+VdxJp2diQyuTf2L16tUV9YBJ3YMi2NX0HrSRZpc2mR/zA6d48eIO15nfYiCWiRRZ8b20Xr16DpfFU+2bbb5KLfUfHpKb/7uFAYtLClcrmdTlxBPWeZOs4o3olpTIokWLKKalcefUl2x2dRu3Jjb1dQcoJj0izqHGkpZsSXoHZiGcnmULtVUTm6U+tln/ugPyzUQn1MynHm5FkNOl2yBZhV2eFF00sRgoTWyasJskkTlzZoVNXAHkM3Rs0dbA/qefffaZGNNgdxi1rHijqBmGDh3K+dQ71dSY27dva7pdQxOmZCdOnMiBois9lHMokxSO5WuCBAkc/91+Tt6v3bp1E5OFNhsREUH/v3fvHpbT7IqlkH5uHydIaqk3cJFzMTv7E+RTA5nP2q+lEjld37fQH9BM4pWapFQrJG39+vUpEPqCIm8Ym6GhoYoKVwM9nDbLz5gxQy8OhGGmTJnE7tq8eXPNjUvQ+th8o55orMJC2K2nJ7sJiyY2p+vweAoXTWwmG93kiDOZmia+GxeEnijwvts49QeF6FXdtWtXchzB+oe/gK5atUqMb16y6TFu3DiKr9CCeQnXv39/CiEXdb65pVq1ap07d7516xbaC3Mlqsv5chYTDxVFM7355pui+qy3ytLDSzmj6TNOmxgwj4iBFy5cQEEyZMig6f+Odchm4eZDk+KLIDsjSrF//34zRZZ4AFZZ6q2Khw4dokDFiclk/EFz8IZQNrFhNLE3HI8sjEH206KDxQJOAExsDx48YFMa6ojHOSZCDhe1Na5cPfMZmorrWh5qEHAg4nmbG+ZLxd5pxq2JTb0TUA2GFqZhOkbHofqOZ9XEpmnX0FOfTBbTKgYl0lP1Aa35xNupoGY7/uu2w3hvYlM3zYABAxBeoECBVjqIH5C/+eYbSidZsmRjx45Ve2UvWbKEImju+2Y9/O233xbDDW4UpaUPaomLDAmTNWvWX375xYMi2NX0HrSRZpf2ID/GA4fUVPUNa7QndPLkyWIgmdjQlOq3mK9SS/1Hb/GH4Uzhas2HTmqjG06cri5EB7S1bNlS742syVgad059yWZXt/HAxDZ16lT1gDKWtGREq1KlimYe2HrCPceqic1SHzMwsZE7gF4+9XArgtRgHQKFgVpQIXmkiU2PmTNn8o5RIjw8nHwlFJBXqfpsIzoeESqxaO+w3cTGrkAQC5YeZGjrsabbNY3KxIkTi24geq70DRo0cLj23XPI3LlzHa4NYmK0GzduKDaYI0RT+pl8XFP1JedihUEZTJs2TS0SzZfI+fK6AIUAhwqQLVs2hURlZ1u1zxRSrlmzptMd7HW7fv16g2jQt3lCJFKkSAFBpPh0hH7IEUaMGOH27cbwnGW8V9QpCFiFiW337t0KUew01+jmR5zJLqSJ78YFoScKvO82ThMmNsVYY69q8VYNS5JNDz0TG9/dzCY2gotfvHhx9bdPctc6dOiQGNi5c2fxulKrJjZv5IxTx2e8YcOGCCxVqpQYSO51FStWFAP5u/ucOXM40JL4crqWhQsXLmTznMQXPHr0iHY0soUUzbRr1y4y4IgeAFh408bPBw8eQA9SmNiwnKYQxceJ/fv3azrEBYoAm9g2u/bfkl2Mz2tTmNgw81GgeE4Kc+3aNbavqR1KJQEBnT558uQkxUJCQrp06aK4hc3ptYnt9u3bkZGRZcuWRbSoqCj1IsPpYxObyWKax22JzKv6vG7TvD/LFyY2WgApPmHpAdlKcyeRK1cuxUZF9l3Sc/BJlSqVw2UyEwWFgYnt+PHjlOCgQYMoBK0JPVncKWCpCN43vWdtpNelzefHzMBp06YNhSv23ZM5QxFoYGIzX6WWKt9jExsfRkZbRYCZTzJ2mdicNkkMP5jYYmJiyASpd18ebwMcNmwYhVg1sVnqY7ab2NyKIJGNGzdCT2jatOmOHTvo+79JExvUyw9UNGnSxFJWYzsQOO3ateN7WkhWbNq0SRHNrVepeEqj7SY2DGHOnttdh2qM3a65e7Rt25YD9RYh/fr1o3DWENj7VWF3VtShnvQz+bim6uvWuRit40GJsJJ3aJnXna4rhlFdimPLaJsnBCb7zDpdKlbChAnFj2R6sMOUYmO4JhBf9OmLiYiIEB0ikEP+iZcTHoMFDA0N9eEGCiyZ2Mw0uvkRZ7ILqfHpuCDcXi7scbdxmjCxqQ1niRMnRrh4hZElyaaHVRObsYs6CckCBQpcvXqVA0+dOiX6dFs1sXkjZ5w6PuO0qTNv3rxiIPm/K1YmfJqHaKq2JL4k/gfrTCyAjx07RgYcxV00mCYQSJfRqU1sfEabYq148OBBTYe4QBEAExsRHR3NdYGVK5Y1qG42sYkutZCPFHjixAkxBcSBHKGftm7dasbvV+I3MDDKlCnDa5GMGTMqDsv02MQG7QhiFJrqiBEjyPuAnaX9bGIzU0wzmCyReVX/7NmzFLN169bq1/nCxEYu1uYPbqfLCmk5QiDz7EvSuXNnzQZl3n//fYfK48DAxOZ8eYIblvX08QTTeWRkpDdF8LLpPWsjvS5tJj/mBw7C6Y6ISpUq8bcmspWoc2tgYjNfpZYq33sTG2Zliqn52UaBjSY2px0Sww8mNixf6CeFLYnhLV3sx2HVxGapj9luYnO6E0FEVFQUFvSFCxdmlwpLJjY+WkiEO+FrBSqQT+x2uET3unXr+Ff2KtVzKQWiDdR2ExsvCYDi7hczGLtdP3jwgH4VB6beImTw4MEUzhqC6P1asWJFvc0cetLP5OOaqi85F2O21WsU8VoY8yWiTWGlS5fWzIkavjJFlMCzZs1CuYyPMCN4m7zJY2SePn06cuRIvkja4boCi1/E0wHAQsVkEQygjy6VK1c2jmbJxOa20S2NOJNdSI1PxwVhIAq87DZOj0xsNB/x+apWJZseHpvYNNUoduJG30ME9RnzTusmNm/kjBpo/QMHDqSDcRXrGZLwmTNnVjxCNS9ebWFJfEn8D1YFbPPB/0WHCbrBcufOndQ51Sa2GzduUIjiwwlfjxkkNx4EzMTmdB1qwBdAYFlDd6AQmOQ42oULFyiQzJlEdHT03r17KRxzjN5NIpLAMmfOHD7hIlGiRKLY9czEhvFGtpIpU6ZwYABNbG6L6RbzJfLAi019dIVeMc1g0DTt2rVzuE7ttXQXz59//snHuIIWLVpQ+PDhwylkyJAhmg8WKFDA4TrTWgw0NrGtWLGC0ly6dCmkjfpwEM+K4HHTe9ZGBiY24/xYGjhOl58XXZ5Yrly5n3/+GU+9/fbbPXr0UL/XwMRmvkotVb73JjY+tQ1rTbevs9fERngjMfxgYsPUTIpBSEiIpjbCo4nvi7BqYnNa6WO+MLEReiLI6TqyB2o2hIzoaWjJxHb16tU/VATJys//oCNBD+SqRv9nZyX2KjW5kPPAxAZ9W+1RCOgA9enTp3PGPDgp2a3bNZlRxG9ClkwJZrxfDaSf+V0FCtWXnIu7d+9uphLMl4icUyyN2VKlSpGo5BN8oMZ/8cUXZp7lg/YMTnNWA11OdGf79ttv+Sc2Jbi1i5kBwsShukFFjSUTm9Ndo1sdcZ75X/t6XDgNRYHTu27jtMPEZrWe9bDXxKZw4s6dO7fazGfVxOb0Qs6IbNy4sVatWk2bNqVLoh2q9Qz7v0dFRYnhdCKBeIyaJfEl8T9sDmMnKrKy8S0HrKOpTWx8s4G4u9npkttBtanRTyY2rKVOulBojOzIRg6rmC3oT1EesasaP/vo0aNt27ZRIBpJ0wYvCRTbt28XtQjoSy1btiSZKDqEe2ZiozN9EyRIIDZ6QExsJovpFvMlsqTq00yPCU/c3G5QTDMYNA2ftay+pofYtGkTl0VxXw/GMvmzAKpScvB26Dsj0GyquCDM2MQGqU2XzVWoUAH5V5/Ua74IdjW9B22k2aXN5MfSwCEiIyMbN248c+bMUaNGLVy4UHFJJWNgYjNfpZb6j/cmNufLDR0FChRQn1TidPWW1q1bk3XJLhObXd3GP2ex0fYWh0qjIyZOnOhw7QphhccDE5vTdB+z3cTmVgRhSFKIwtfVkont9QQDymBJxg4UYpdgr1KTBxR6YGJDt3RoQd31zJkzHAJZZL6whFu36/z58zv+e1m5VVOC2vtVcY67gfQz87im6kvOxXXq1DFTCeZLRDv41GckGbB27VpKhHamIyno8GfPnjXz7IQJE+hZqG3qXw0+6ty8eZOtbBkyZOBwNk8kTZrUpD+UASlTpnS4zig0jmbVxOY0bHSrI844NT38MC6MTWzedBunHSY2D+pZE3tNbE4tJ+42bdqIY8EDE5vTUzlDREVFFStWrEiRInwHtKaJjf3fIZ14oqHb5Nu1ayfGtCS+JAEB8hMrLva1In2Hdi4eOHDg+Ut4L+PRo0fxJ3ovhDOFKO6mYM84cRN0APGTiQ0LVir2zp07+agL1NSOHTsonKzdx48fpz958zwi80l4FIcNnODQoUOaCpIkgGDd/MMPPygCK1as6HDdbsMhefPmRUihQoUUMY3nBhLfkLBiIJ+05QsTG5+jqVAdTRbTLeZLZEnVp+OEwaRJkxSRuZh6Cq0eBk2DQUo/ZcmSRVGrTteFv2jo6Oho+lP9wZYfJ6dfjHHeVaT+8gzhQMsyxaLK2MQGRo8ezRP/xo0bPS6CXU3vQRtpdmkz+bE0cJyuMaIwLuhhYGIzX6WW+o8tJjaqHz0507t3bw63amLTk2x2dRs9ieS01cTGykn9+vXVv5JxULRxr1u3juLPmzdPMx21ic18H7PdxOZWBPE9faLXJ4iIiHCoTGwGLfIacuHCBWOXHNbBeJ8Oe5WOHTvWzCs8MLE9fvxY7VEI+EZLOnzA4c7/VBO3btd0eUju3Lk5xKopgVB4v4pnpxib2Nw+rqn6knPxm2++aca52HyJ6HKJ0NBQFulmoAZKnTo1mgz9xO1eMwYSiTKg+bWgadOmBjv1WA6AW7duUSD78Dq8tqrzWWzqU/kVeGBiIzQb3eqIM05NDz+MC2MTm9OLbuO0w8TmcT0rsN3ERiicuDGt80+emdgIq3LG+dJnPGfOnOLxuJomNqfg/16+fHn2f+/Vq5fiEklL4ksSQDB4RXsZXzCqx+3btyEf6P8Kr/OoqCgKN3OLiB/wk4kNEwlb044dO3bv3j1UENfjtm3b6FsQGya3bt165coVRKMT7za7ro0gaxr7B1LlHvgvxhJf4gegShUrVkxh+qSJUJxoyUsiRYoU9CHixYsXZE1A9yDRPGrUKHXibHmh/R1Ol88zfysT7/92Ch7FCnfl7t27a87ifKKqeDwqe1TxnrKLFy+idCaL6RbzJeKjKxSq/tOnTylc3OWEgUP6P2oYizAOxySkfqNJjJuGPhkBLJtY6qFZFy1ahGXHwoULOWaGDBkUy0RUY4IECd544w2eI48cORISEuJQuaqBvn37IpxuHxdToPgGS9W7d+/S1e+YyDUjmCyCXU3vQRtpdmkz+bE0cJAgAn/44QfWPw2gq6CwPNL81XyvMB9z9uzZmos/PkGsa9euimwULlwY4fnz5+cQ/rxMtcR71jD20YUKFizIhxVYGndOfclmV7fRk0jOl60sOlwQ7Dok3r5kPJxB3bp1qWXFG9+crnGUMGFCNIooP9kjskqVKlxGFJy2J4Mvv/xSTMRSH2P7ndpOlyRJEofqfjG3uBVB/EZxH/fhw4ehqjlcq3bxWYMWeQ2hXcZr1qzRi8Dasrhjy9irFOvDVq1a8ddZ289icwqGGODWPUeBW7frZMmS4dcuXbpwiHlTgtr7FQKH4oheG3omNpOPa6q+bp2Lf/vtt1mzZlktEfnAOvRv5IR6r76IhnX+yZMnQz7ze90CRYMeVFj/CcilIkWK6D2LjkdzNFYXbBBEF82VKxel+fHHH5vMhiaQpZTO8OHDjWNaMrGZaXTzI85kF1Lj03FBuDWxedxtnHaY2JwWJZse9prYDJy42ffHqonNGzmj5zOuZ2JzuvzfmzZtOmPGDKxesETU3JFjSXxJ/APGKe1oFL0E2F5GC1QzJjY8zuYjMX3eCqm4MydQ+O8sNj6dTg0LTcggzcrdsmULf0FiTzdNPDhHQ2IvpDuNHj1aDISikilTJvEg4UGDBpH4a926NURk9erVSZQvXbqUwjXPPuenkidP3rt3706dOkH+jh8/nswr+P9QFxSZrp4Bov0CVK1alcIVztus5KO/cSCWejRHpk+ffs6cOVCi6tSpgxnRZDHdYr5E+/fvp5gKz2c2FpQpU0YMHzZsGIUnSpSoY8eOmDKnTp2Kmb5kyZIUnjJlSiwFMDBNZtW4aSA0+YwSh0vPDwsLoyWU4o4h/JQ9e3bRj3fnzp0Olao/e/ZsqvkJEyZw4LJly6DzY02m+DBFl5SBYsWKGRQBnc2hfwKXySLY1fRO622k2aXN5MfSwKGVDZE0aVLUSc6cObE8LV++PB5EY/FbILH5YizNqwPM9wrzMekUW4dqgbtnzx4KL1u2rBj+7NkzWsBB8xfndTa1O1xbaPPmzZslSxYoVHny5OHpxml93OlJNru6jZ5EwmKdiok2VXzBa968OWXpp59+4kDj4ex0Ld+hQDpcW7q4QrBwKVeuHCpKveuKIoNSpUqhEho0aIBGZG0ETdmhQ4dz585RZPN9zCno5AorJ9v1smbNasmk5VYEQfXlY2XQRgMHDqxcuTLKJe7tbdasGel1ei1iPj+vGLly5cJo0lvjQnpTHYpOf+xVCqGkfgRDVfwM4AsTG/pPeHg4JZs7d263R00dOHCAB46x2/WFCxccLgkvuiSbNyVAbkCTVKRJlmvR+1XPxGbycfK9LVq0qBhNdC5WV8iZM2cKFSrEEtV8iU6cOEF2Kwwx9TGUUJnq1q3rVIFKRrs4XB5JkBhmTPMEWpYMH5pbgBcsWODQdwG7c+cOZV7hlbx9+3YqApg+fbpxBiCZP/vsM8VtiQTkISWikHhq2OiPOUUMX7VqFYWLRTDT6OZHnMkupMan44Jwa2LzuNs4dQaF06KJzZJk08NeE5vayxj9meLz4fHsmq3Zb9V4I2fYVxSrXzG8Zs2aDi0TGzqJnnVexJL4Il7bD2N+Q/OsNEgACjx06JDTdYjtuf/CR4rt3bsXf9LXDshMCuTvMbxdEpNIkCzA/HrdASoOI1m0iO3YsUOxYxbqEHuuEXhEvKcZIkCa2IIZiFqIUYhFTC3QWCZMmACVDNqXeFuF0zU30EEMANMSVtsYe9DKxIuc8GC/fv3ESRECkcQugWTJTEa71RwuC8uNGzcw30DN5mhIH8v606dPQy3EspjD6XRtaAIIhybM4dD3evfuzS+dMmUKOfMDvIgOCjRZTLeYLBFWGJkzZ+ZotWrVWrlyJaLxtTsESiEa9VGr2bJlE8uFp7788kssa+rXr79ixQrxXhEDzDQNtSnKQhs2iQ8//FDtK5cnTx5MsShOt27dpk2bhqrG/7/99lv19Hb+/HlULyq/ZMmS7dq1w1NYLSn8I7BGh+pO3iVch3rfhCGpoQyrtyJaKoJdTU+YbCO9Lm0yPya7GUXGHEbnBOsxZswYRMO7eAg7XK497du3V2/GMdkrzMRE327Tpg33wzRp0nTt2hUFgSKEgZwxY0Z+sEqVKrTgQ22g23B4WFiY6P+IJbL4VJIkSUSPNqdrZW913Kklm+3dRi2RZs6cKd5fmT17dlpzY04U2x2dH4MF6xgzw9npWnFCMUA9p0iRomnTplB9ITNbtmyp9jFxuo6kpZ2qRHh4+MWLF1GZ+H/BggUxJEUfc5N97MqVK61atSLnU4fr9DeUlz51osXFpkEHNqkMOM2JIMiZVKlSUeLo29DPsThB1VH/xL/i5WWac8RrC3Qq1EPVqlXVJ1VhcUznW7333nuiesMGa1TjsGHDeAyiC6GvFi5cWPymwl8m2GLLoOc7/uuvap6bN2+Su6vDdfy83iUkKBSaO0OGDOJdZocPH9Zzu+7Vq5dDZd/Rc6WnyI6XZwI6XXJDrRLTSQKi9yvi04MKH16Tj5PvLfo5NRn73vJ3R0hOXl0jzoIFCyAWli5d6kGJQNu2bSkQIheCmqYe9A1IRchVhdssw2q/sfOUGrKMi4YPBo3ocH190bzZGWOc3qj2gEPFUouHhobqXcvodGnyqNsWLVpoqnzkK2RmLxt/TsBcw2IKFcXbrsV5zUyjmx9xJruQJr4bF4SBKGA87jZ6g4LNnWrLLHlVi/dgWJJsemDBQIkoPmTyqO/Zs6cYbuyiDtml2BxNrsfiPhL2QOSLPi5dumRggfJGznB9VqpUiWOi59D8i0WU4kUO0/7v5sWX0zXYsSjCmjNIHKBeSfjigu3bt1+7dg1VffnyZT5bX89Qrr7uwOkSrRQI/R2r7tu3b2OsUUjwbGf0942imIegDmFQoVrv3r2rNy1RvUMGXb9+Xd5mELtA29FiAnPk7t27N23apLi6kXn69CmkHoaHSUMPc+HChY0bN4rbOSE0MWLJ4uALMJOhIOIbzRfTDD4tETQHZC8qKopmNYw+S2egWAUrhoMHD0IN1rNkkX6O2kPpNmzYAK3VuANAeu7cuRP1Y7CKMo/iAhpNjItgb9MT3rSR+fyY7GaYq2rUqEH5Wb169ezZs6dNmzZmzJihQ4d27tw5X758WDRbNSK47RUexLQLOnzg7Nmz3p9dTWhKNnu7jVoi+Q5kGyub3377DSsY9dUcCrBI2rp1K3u94VnNZZMv+ph5TIogjEH0QzSW+CvGJlaE6lW4P1skyOnWrRspNiVKlBDvfcOSmj5lpUiRQm1Z1vQqhV6K/yjcPGvVqkXRoJuJ4eh1ZABNlCiR+F3WPFDb2OWTLsXjcYreghXpxIkT8+fPDzVMbYCbNWuW2u16yZIlyFLXrl0V61g9V3r2eWGLD6mUouc1FF1oqgrvV+jMajXV/OPse9umTZtFixZ9+umntFvWwLkYA9azEjldLcWH3xGpU6eOGzcu2h3SQ6NhXuY8R44ciAxBpBdHE2hc6EjodWobAZ8DgD4zfPhw8TinhQsXUoNCImkmu379ej5zKnfu3BBiR48eJVkB0QHB0q5dO7x01KhRei4VTZs2xbOofDOlYDfh0qVLk5twxowZ0T8pMHny5B07dqQ1kslGNzniTKamh4/GBaEnCkQ87jZ6g4Iv0FDcVkl+eQ7XJy6xp5mXbHq0atWKHhdPzHAKhjDF5bbGLuoYxTlz5hS9WzDoHP91sRdds+fOnYvWr1evnrGJzWM5I/qMo6EHDhwYHh7+0Ucf0eVCoH379hgpZN808H/HOFXsWDIvvgB/sZszZ45eMSVeAknIhjC1g5TeClzTxAZJy45sIghU30ofKPxtYpNIJBJJ0HLlyhUsWQxO58UcWbx4cTOWSolEE9nHXm2mTJny7rvvfvXVVzVq1IDuBC0LilPhwoXjx48PxRLqot7pBAqvUmhQQ4cOFa2ZUOHY0EB2mY4dO2JpfuTIEajrdGc0kTVr1s8//3zFihUe5J/cPFnro5yEhISEhoZWqlRp3rx5eqqm2u06T548CuVf7Urfs2fPR48e7dq1i+0LDpc7c79+/Zwu3TVfvnzvvPMOXg0dePz48WXKlKlQoQJfjAj1GCpoihQp+FkoqLy53u3jhOh7my5dOtFVXO1cXKpUKXFjo9USEU+ePOnSpUu8ePE4AiKjAo2bBlq3Zy6KpJmLBl8mTZo0n7t47733EiVKVKhQITQi2c7Qi5YtW2aQLEoxbtw4aPhcCvQTcmUiJ1mDS6XQi/BqRBbPJTBA4SZcuXLlS5cu0QZhhZuwyUZ3mhhxllLTwxfjQk8UaGbAs26jHhTkVc0O4OxVjabs3r0721sdLjdY0VPMTD1rsnnzZmSePAEdL89bQH1eu3YNvUu0H1WpUgU51Nxx8sUXX4i2Y3LiRg2TE3evXr3QV9GsCrEmumbXr1/fOLdeyhmFz/iYMWOePXt24MABEjsoDl8V5db/nd3u+I3G4oshezfGo3pTs8RG/vnnH8zXCrvY0aNHDeximiY2p2tnqMJghz+Dx77mlCY2iUQikTC0fNE8PpbB+syq56lEwsg+9mpz8eJFOlTF6dq4AOV54cKFM2fOhC6qucVYge1epZ6BnP/+++/Lly+fPn364sWLoZWZ9KuFUrdjx45Nmza5NRiZAZotqb6eeb+af9x4V4GPnIvv3bu304VJl9UcOXJonmnlFpQaKr16uyKgvf/E1atXoe3PmDFjxYoVUObNH+iDB3/77bfZs2ejn69bt87MTqUlS5Y4XFveTL6CuHDhgng4NcaI2k3Yap8xHnFe9kDG3nFhCY+7jcdbbTQJEsmmcOI+fPiw3mZV867Z3ssZA59x0Xf+9u3bNWvWxBA4cOCA2v89b968oaGhal97k+ILGZO7RP0D6hk9BEuFGzduuN0bYQB63d27d9FP0EvRN4LkCDZGmtgkEolE8n/wpZxTpkzRjIAJbODAgWbOmpVINJF9TCKReMDGjRuTJElixkqryebNmxMnTmze98qnQMPMmDFjzZo1A52RVx8vu40keCD/dwNrKd2woXn1lkTif6SJTSKRSCT/D7qSz+E6xWPOnDm7d+8+ffr03r17V69e3a9fv/z58w8cODDQeZTEbmQfk0gkVqlUqZLiTmGrTJ48uXjx4paulfQRHTp0KFeuXDDk5JXH+24jCRLI/128jFJNsWLFzNwgIZH4AWlik0gkEsn/4/r161iSqk+4CAkJad26tcHJMhKJSWQfk0gkbjlx4sTkyZO3b98eHR09fPjwRIkSeX+dyLhx4yB8vNma5D39+/cPDw/36a1TrzO+6DaSgGPG/33AgAHipQ0SSWCRJjaJRCKR/Ifz589PnTq1X79+nTp1Gjx48OLFi2/evBnoTEleKWQfk0gkejx79ixt2rSkVNOx64qDzD1m5cqVFSpUMPaF8RHPnz9v3br1V199FWxnBr0y+K7bSAKO6P8+d+7cPXv2nDlzZu/evatWrerbt++77747YMCAQOdRIvn/kSY2iUQikUgkEolEEixAZ2YX13bt2tlolrpx40agDufy/2H/rxu+6zaSwHL9+vWKFSuq/d/jxo376aef6t0nK5EECmlik0gkEolEIpFIJMECNOrhw4f36dNn3bp1gc6LJNYgu82rzblz56ZMmdK3b1/yf1+yZIn0f5cEJ9LEJpFIJBKJRCKRSCQSiUQikXiFNLFJJBKJRCKRSCQSyevCvXv3bt++ff/+/Ycubt26pbiEAX/evHnzwYMH+PXu3buByqdEIpHEOqSJTSKRSCQSiUQikUheF8aOHVunTp3Q0FCHw5EzZ85GjRotXbpUjLB48eKkSZPi1xQpUkRERDx58iRQWZVIJJLYhTSxSSQSiUQikUgkEslrxL///psqVSqHw3Hu3Dn1rwjMli3b+PHjY2Ji/J83iUQiib1IE5tEIpFIJBKJRCKRvEYcPXrU4XDkypVL/dPy5cubNGly7do1/+dKIpFIYjvSxCaRSCQSiUQikUgkrxETJ050OBzt27cXA//5559u3bpNmjQpULmSSCSS2I40sUkkEolEIpFIJBLJa0SdOnUcDseCBQs45OjRoxEREYcPHw5griQSiSS2I01sEolEIpFIJBKJRPIakSZNGofDcf36dfpzypQprVq1UtwrKpFIJBKrSBObxH4ePnw4ePDgESNGPH782MukDhw48OWXXzZv3rxu3bqdO3deuHChl1caHT58GHk7deqUmcgGBXn27NmWLVt69ux58+ZNk4+8qvihyKjqDh067Nq1y0fpx65smAQj5W8d/vnnHz9nBn1j1apVgwYNsivBf//9d926dV27dq1Xr167du2WLFmCELsSN48UERKJRCKxkU8++cRhH6KHmoJjx47xQWx37typUaMG/vz888/9WFZPgDpQ6SUnT54MdHYCw/bt27kSOnbsGOjsSCQSJdLEJrGfb7/9lqb27777zuNEbt++Xa1atdKlS2Mi+eOPP8aMGRMnThykWbx48RcvXlhNDSuJli1bZsiQgTKGNM08pVmQCRMmYAGUJEkS+gl5c/vIq42vixwTE5M6dWqkj+bzoOlfsWyYZ/Pmzc2bN8+aNavmsjtp0qQ5c+YsV64c+jPW1r7LxrJlyypXrpwgQQK89J133rElzb///rts2bJYVu7evRtlpBL16NHDlsQtIUWERCKxhefPn585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CIIgJGdEYhMEQXilCQ0NpSk8GnLlyjVnzhyDBaT/CcLDwxs3bkw5wn/gYyef4yyE5AA82PXr19Php/h37dq15s9X/U8TGxvbt29fPvWVSZUq1bJly0xGcunSJfX0WyJbtmwrVqxI0sQ74uLFi23atKFkvP/++76+vlevXj127NiCBQsqVKgAI/q6kSNHFipUCP/xSArjJcqGGx709OlTOgaX2Lp1q0uiNZn+kydPzp49+5133tFUnjfffBPVctCgQb17927evLl62HqaNGncljxPoT9AZurUqVwC1apV80iqBEEQBKcQiU0QBEGwHj16dMaMGYMHDx44cODEiRP/+ecfp46qTJ4cPny4r45x48Z5Ol1CMmLChAmaGtKvX78DBw54Ol1JS3R09AcffJArV66PPvqoadOmr732mipzZMiQwcza8IiIiCJFiujVeZA6deqQkBA3ZERly5Yt3t7elIDPPvtMI6Y/e/YMPRtLislTYouJialcufK8efPc8Kzz58+rr8wlE9mcTf/Dhw/TpUunJgOpUgPExsb+/fffJUuWdInE5s7iTQDr16/Ply+fxtixY0cuHJSVRxImCIIgOIVIbIIgCIIgCK8QI0eO7N69O8voERERNWvWVJWO5cuXxxsJzQ99991327Zt6+Pjo1HZ6tSpk8SZeIHNmzd7eXnRo995553Y2Fi7webNm5ecJbbBgwcjbe7RgFBErJCmSJEiODg48XEmIP20UwFz7949fZhLly5lz5498RKbO4vXWUJDQ7Nly5Y3b16NfcGCBVw4H3zwgUfSJgiCIDiFSGyCIAiCIAivCmfPnm3atKlmkldISIhTc5p8fX2zZMkSEBDAllWrVqVKlUqdceNI53I5ly5dypo1Kz96zZo1BoFHjBiRPCW2pUuXUvrdpgGdO3fu448/btas2bp16xIfW8LSX7x48XglNvDzzz8nUmJzf/Ga59GjR2XLlkXa9BIb2umsWbMaNWo0aNAg/TJSQRAEIRkiEpsgCIIgCMIrhH4ZODz5tGnTstLx559/GsdQv379v//+W2P8/vvvVbnkzJkzrky0Y9q1a8cPzZgxY0xMjEHg6OjookWLJjeJbf369WnSpEm2GlC8JDj9BhJbZGTk/Pnz6f8RERGJWSaZnIv38ePH9erVo7TpJTZBEISXhgcPHhw/fnzv3r1+fn5BQUH4v8FR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
```

---
