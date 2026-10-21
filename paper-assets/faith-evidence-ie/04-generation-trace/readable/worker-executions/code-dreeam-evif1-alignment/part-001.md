# code dreeam evif1 alignment — Part 1 of 48

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

[Transcript overview](../code-dreeam-evif1-alignment.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/b0/b092146cd188122cf374.json)

## Before a recorded user message

## Before a recorded user message

156 recorded events


### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---


### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "77645bb7-1324-47f1-a2e2-55fd508799df",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/memory/"
  },
  "fast_mode_state": "off"
}
```

---


### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779022800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a946b0de-39ab-40f2-bf70-4735af9bad6e",
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the task. I need to:
1. Check our current Evi-F1 calculation code
2. Find and understand DREEAM's Evi-F1 calculation
3. Compare the two approaches
4. Align if needed
5. Recalculate with aligned metrics

Let me begin by SSH-ing to the server and examining the relevant code.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "e0929ab9-86d1-404f-9ed3-a44453f735cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCMCYbkH3gp3P6Kz3qBKid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13476,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13476
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 5_

开始对齐 DREEAM Evi-F1 计算协议。先查看我们的评估代码和 DREEAM 的实现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "6ae64f15-f882-45b5-b440-2783a7a2f008",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCMCYbkH3gp3P6Kz3qBKid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13476,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13476
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DriRyD9a6RPApU3kkbU9ET`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "0fafcd90-7269-477a-9abf-88532e12fc4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XCMCYbkH3gp3P6Kz3qBKid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13476,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13476
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-17T12:54:56.007Z_

<details><summary>↩ Tool result · `toolu_01DriRyD9a6RPApU3kkbU9ET`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "a58354c2-9c7a-49c9-9a66-264a881f9a8a",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 26
  }
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01M8FZeNo1ht8Tcs72jfeaez`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/freige/eval/ -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "c8ae4207-162a-4344-958a-8328cbd2e9c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ha4YS7ASj8b3cTADjac4N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 25317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1416
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-17T12:55:00.285Z_

<details><summary>↩ Tool result · `toolu_01M8FZeNo1ht8Tcs72jfeaez`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/freige/eval/__init__.py\\n/root/autodl-tmp/freige/eval/evaluator.py\\n/root/autodl-tmp/freige/eval/inference.py\\n/root/autodl-tmp/freige/eval/batch_eval.py\\n/root/autodl-tmp/freige/eval/find_best_checkpoint.py\\n/root/autodl-tmp/freige/eval/ced_reranker.py\\n/root/autodl-tmp/freige/eval/test_inference.py\\n/root/autodl-tmp/freige/eval/cross_method_table.py\\n/root/autodl-tmp/freige/eval/ced_evidence_filter.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.03}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "c1b76cc6-6001-4fcd-a749-5975c5d9531a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/freige/eval/__init__.py\\\\n/root/autodl-tmp/freige/eval/evaluator.py\\\\n/root/autodl-tmp/freige/eval/inference.py\\\\n/root/autodl-tmp/freige/eval/batch_eval.py\\\\n/root/autodl-tmp/freige/eval/find_best_checkpoint.py\\\\n/root/autodl-tmp/freige/eval/ced_reranker.py\\\\n/root/autodl-tmp/freige/eval/test_inference.py\\\\n/root/autodl-tmp/freige/eval/cross_method_table.py\\\\n/root/autodl-tmp/freige/eval/ced_evidence_filter.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.03}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/freige/eval/__init__.py\\n/root/autodl-tmp/freige/eval/evaluator.py\\n/root/autodl-tmp/freige/eval/inference.py\\n/root/autodl-tmp/freige/eval/batch_eval.py\\n/root/autodl-tmp/freige/eval/find_best_checkpoint.py\\n/root/autodl-tmp/freige/eval/ced_reranker.py\\n/root/autodl-tmp/freige/eval/test_inference.py\\n/root/autodl-tmp/freige/eval/cross_method_table.py\\n/root/autodl-tmp/freige/eval/ced_evidence_filter.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.03}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01T2iBh3Job2bzQgErhCHcUQ`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/ -maxdepth 3 -name \"*.py\" -path \"*dreeam*\" -o -name \"*.py\" -path \"*DREEAM*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "5cf8c6f8-534c-4915-bbef-15fb3aa2cfe3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Ha4YS7ASj8b3cTADjac4N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1416,
      "cache_read_input_tokens": 25317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1416
      },
      "output_tokens": 46,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-17T12:55:00.857Z_

<details><summary>↩ Tool result · `toolu_01T2iBh3Job2bzQgErhCHcUQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/baselines/dreeam/args.py\\n/root/autodl-tmp/baselines/dreeam/evaluation.py\\n/root/autodl-tmp/baselines/dreeam/long_seq.py\\n/root/autodl-tmp/baselines/dreeam/losses.py\\n/root/autodl-tmp/baselines/dreeam/model.py\\n/root/autodl-tmp/baselines/dreeam/prepro.py\\n/root/autodl-tmp/baselines/dreeam/run.py\\n/root/autodl-tmp/baselines/dreeam/utils.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "f2b2855a-d435-4b3a-a88a-b16155ad26fa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/baselines/dreeam/args.py\\\\n/root/autodl-tmp/baselines/dreeam/evaluation.py\\\\n/root/autodl-tmp/baselines/dreeam/long_seq.py\\\\n/root/autodl-tmp/baselines/dreeam/losses.py\\\\n/root/autodl-tmp/baselines/dreeam/model.py\\\\n/root/autodl-tmp/baselines/dreeam/prepro.py\\\\n/root/autodl-tmp/baselines/dreeam/run.py\\\\n/root/autodl-tmp/baselines/dreeam/utils.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/baselines/dreeam/args.py\\n/root/autodl-tmp/baselines/dreeam/evaluation.py\\n/root/autodl-tmp/baselines/dreeam/long_seq.py\\n/root/autodl-tmp/baselines/dreeam/losses.py\\n/root/autodl-tmp/baselines/dreeam/model.py\\n/root/autodl-tmp/baselines/dreeam/prepro.py\\n/root/autodl-tmp/baselines/dreeam/run.py\\n/root/autodl-tmp/baselines/dreeam/utils.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 12_

找到了两边的代码。先并行读取我们的评估核心代码和 DREEAM 的评估代码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "a01f9c26-a9b7-4720-bed2-9ea1a6fa799b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tp7fqzKHiNCwtiNmc4cDLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 26733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 818
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01LMMJT4hNfuhxUD1n2AhxGj`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/freige/eval/evaluator.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "928a34cc-00e3-4fd0-bd32-5a013d852995",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tp7fqzKHiNCwtiNmc4cDLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 26733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 818
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01JDzHqtbxF5yXytso539cMG`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/baselines/dreeam/evaluation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "a91fac28-9789-4947-8592-131739a01401",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tp7fqzKHiNCwtiNmc4cDLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 26733,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 818
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-17T12:55:06.315Z_

<details><summary>↩ Tool result · `toolu_01LMMJT4hNfuhxUD1n2AhxGj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"DocRED 关系抽取评测模块。\\n\\n指标:\\n  - F1 / Ign-F1: 关系三元组级别 micro-F1，Ign-F1 排除训练集中出现的三元组\\n  - Evi-F1: 对正确预测的三元组，计算 evidence 句子级 F1\\n  - EDCR: Evidence Distractor Citation Rate，预测 evidence 中非 gold 的比例\\n\\n输入: 预测列表 + gold 标注列表（每个元素为文档级标注）\\n输出: 指标字典\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nfrom collections import defaultdict\\nfrom typing import Optional\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef _triple_key(doc_id: str, head: str, tail: str, relation: str) -> tuple:\\n    return (doc_id, head.lower().strip(), tail.lower().strip(), relation.lower().strip())\\n\\n\\nclass DocREDEvaluator:\\n    \\\"\\\"\\\"DocRED 评测器。\\n\\n    Args:\\n        train_triples: 训练集中的三元组集合，用于计算 Ign-F1。\\n                       每个元素为 (doc_title, head_name, tail_name, relation)。\\n                       为 None 时 Ign-F1 = F1。\\n    \\\"\\\"\\\"\\n\\n    def __init__(self, train_triples: Optional[set[tuple]] = None, train_facts: Optional[set[tuple]] = None):\\n        self.train_triples = train_triples or set()\\n        self.train_facts = train_facts or set()\\n\\n    @classmethod\\n    def from_train_file(cls, train_path: str) -> \\\"DocREDEvaluator\\\":\\n        \\\"\\\"\\\"从训练集 JSON 文件构建 evaluator，自动提取训练集三元组。\\\"\\\"\\\"\\n        from freige.data.docred_processor import DOCRED_REL_INFO\\n\\n        with open(train_path) as f:\\n            train_data = json.load(f)\\n\\n        train_triples = set()\\n        train_facts = set()\\n        for doc in train_data:\\n            doc_id = doc.get(\\\"title\\\", \\\"\\\")\\n            vertex_set = doc[\\\"vertexSet\\\"]\\n            for label in doc.get(\\\"labels\\\", []):\\n                h_name = vertex_set[label[\\\"h\\\"]][0][\\\"name\\\"]\\n                t_name = vertex_set[label[\\\"t\\\"]][0][\\\"name\\\"]\\n                rel_name = DOCRED_REL_INFO.get(label[\\\"r\\\"], label[\\\"r\\\"])\\n                train_triples.add(\\n                    _triple_key(doc_id, h_name, t_name, rel_name)\\n                )\\n                train_facts.add((h_name.lower().strip(), t_name.lower().strip(), rel_name.lower().strip()))\\n\\n        logger.info(\\\"Loaded %d training triples (%d unique facts) for Ign-F1\\\", len(train_triples), len(train_facts))\\n        return cls(train_triples=train_triples, train_facts=train_facts)\\n\\n    def compute_f1(\\n        self,\\n        predictions: list[dict],\\n        gold: list[dict],\\n    ) -> dict:\\n        \\\"\\\"\\\"计算 F1 和 Ign-F1。\\\"\\\"\\\"\\n        pred_set = set()\\n        for p in predictions:\\n            pred_set.add(_triple_key(\\n                p[\\\"doc_id\\\"], p[\\\"head\\\"], p[\\\"tail\\\"], p[\\\"relation\\\"]\\n            ))\\n\\n        gold_set = set()\\n        for g in gold:\\n            gold_set.add(_triple_key(\\n                g[\\\"doc_id\\\"], g[\\\"head\\\"], g[\\\"tail\\\"], g[\\\"relation\\\"]\\n            ))\\n\\n        tp = pred_set & gold_set\\n        precision = len(tp) / len(pred_set) if pred_set else 0.0\\n        recall = len(tp) / len(gold_set) if gold_set else 0.0\\n        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0\\n\\n        pred_ign = {k for k in pred_set if k[1:] not in self.train_facts}\\n        gold_ign = {k for k in gold_set if k[1:] not in self.train_facts}\\n        tp_ign = pred_ign & gold_ign\\n        ign_prec = len(tp_ign) / len(pred_ign) if pred_ign else 0.0\\n        ign_rec = len(tp_ign) / len(gold_ign) if gold_ign else 0.0\\n        ign_f1 = (\\n            2 * ign_prec * ign_rec / (ign_prec + ign_rec)\\n            if (ign_prec + ign_rec) > 0 else 0.0\\n        )\\n\\n        return {\\n            \\\"precision\\\": precision,\\n            \\\"recall\\\": recall,\\n            \\\"f1\\\": f1,\\n            \\\"ign_precision\\\": ign_prec,\\n            \\\"ign_recall\\\": ign_rec,\\n            \\\"ign_f1\\\": ign_f1,\\n            \\\"tp\\\": len(tp),\\n            \\\"pred_count\\\": len(pred_set),\\n            \\\"gold_count\\\": len(gold_set),\\n        }\\n\\n    def compute_evi_f1(\\n        self,\\n        predictions: list[dict],\\n        gold: list[dict],\\n    ) -> dict:\\n        \\\"\\\"\\\"计�� Evidence F1（句子级）。\\\"\\\"\\\"\\n        gold_map = {}\\n        for g in gold:\\n            key = _triple_key(g[\\\"doc_id\\\"], g[\\\"head\\\"], g[\\\"tail\\\"], g[\\\"relation\\\"])\\n            gold_map.setdefault(key, set()).update(g.get(\\\"evidence\\\", []))\\n\\n        total_tp = 0\\n        total_pred = 0\\n      \\n\\n... [截断: 输出过长，省略 5937 字符] ...\\n\\n\\n            return False\\n\\n    @staticmethod\\n    def _parse_raw_json_list(text: str) -> Optional[list]:\\n        try:\\n            obj = json.loads(text)\\n            if isinstance(obj, list):\\n                return obj\\n        except json.JSONDecodeError:\\n            start = text.find(\\\"[\\\")\\n            end = text.rfind(\\\"]\\\") + 1\\n            if start >= 0 and end > start:\\n                try:\\n                    obj = json.loads(text[start:end])\\n                    if isinstance(obj, list):\\n                        return obj\\n                except json.JSONDecodeError:\\n                    pass\\n        return None\\n\\n    def evaluate(\\n        self,\\n        predictions: list[dict],\\n        gold: list[dict],\\n        raw_outputs: Optional[list[dict]] = None,\\n    ) -> dict:\\n        \\\"\\\"\\\"运行所有评测指标。\\\"\\\"\\\"\\n        f1_metrics = self.compute_f1(predictions, gold)\\n        evi_metrics = self.compute_evi_f1(predictions, gold)\\n        edcr_metrics = self.compute_edcr(predictions, gold)\\n        result = {**f1_metrics, **evi_metrics, **edcr_metrics}\\n        result.update(self.compute_evi_f1_joint(predictions, gold))\\n        if raw_outputs is not None:\\n            result.update(self.compute_format_compliance(raw_outputs))\\n        return result\\n\\n\\n\\n\\ndef _try_parse_json_list(text):\\n    try:\\n        obj = json.loads(text)\\n        if isinstance(obj, list):\\n            return obj\\n    except json.JSONDecodeError:\\n        pass\\n    return None\\n\\n\\ndef _repair_truncated_json(text):\\n    stripped = text.rstrip().rstrip(\\\",\\\")\\n    for suffix in [\\\"]\\\", \\\"}]\\\", '\\\"' + '}' + ']', \\\"null}]\\\"]:\\n        result = _try_parse_json_list(stripped + suffix)\\n        if result is not None:\\n            return result\\n\\n    last_brace = text.rfind(\\\"}\\\")\\n    if last_brace > 0:\\n        result = _try_parse_json_list(text[: last_brace + 1] + \\\"]\\\")\\n        if result is not None:\\n            return result\\n\\n    return None\\n\\n\\ndef _get_field(d, *keys):\\n    for k in keys:\\n        if k in d:\\n            return d[k]\\n    return None\\n\\n\\ndef _normalize_triples(triples):\\n    results = []\\n    for t in triples:\\n        if not isinstance(t, dict):\\n            continue\\n        head = _get_field(t, \\\"head\\\", \\\"head_entity\\\")\\n        tail = _get_field(t, \\\"tail\\\", \\\"tail_entity\\\")\\n        relation = _get_field(t, \\\"relation\\\", \\\"type\\\", \\\"label\\\")\\n        if head is None or tail is None or relation is None:\\n            continue\\n        evidence = _get_field(t, \\\"evidence\\\", \\\"sentence_ids\\\") or []\\n        results.append({\\n            \\\"head\\\": str(head),\\n            \\\"relation\\\": str(relation).lower().strip(),\\n            \\\"tail\\\": str(tail),\\n            \\\"evidence\\\": evidence,\\n        })\\n    return results\\n\\n\\ndef parse_model_output(output_text: str) -> tuple[list[dict], bool]:\\n    text = output_text.strip()\\n\\n    parsed = _try_parse_json_list(text)\\n    if parsed is not None:\\n        return _normalize_triples(parsed), True\\n\\n    start = text.find(\\\"[\\\")\\n    if start >= 0:\\n        end = text.rfind(\\\"]\\\")\\n        if end > start:\\n            parsed = _try_parse_json_list(text[start : end + 1])\\n            if parsed is not None:\\n                return _normalize_triples(parsed), True\\n\\n        repaired = _repair_truncated_json(text[start:])\\n        if repaired is not None:\\n            return _normalize_triples(repaired), True\\n\\n    return [], False\\n\\ndef gold_from_docred(\\n    docred_data: list[dict],\\n) -> list[dict]:\\n    \\\"\\\"\\\"将 DocRED 原始数据转为评测用 gold 格式。\\\"\\\"\\\"\\n    from freige.data.docred_processor import DOCRED_REL_INFO\\n\\n    gold = []\\n    for doc in docred_data:\\n        doc_id = doc.get(\\\"title\\\", \\\"\\\")\\n        vertex_set = doc[\\\"vertexSet\\\"]\\n        for label in doc.get(\\\"labels\\\", []):\\n            h_name = vertex_set[label[\\\"h\\\"]][0][\\\"name\\\"]\\n            t_name = vertex_set[label[\\\"t\\\"]][0][\\\"name\\\"]\\n            gold.append({\\n                \\\"doc_id\\\": doc_id,\\n                \\\"head\\\": h_name,\\n                \\\"tail\\\": t_name,\\n                \\\"relation\\\": DOCRED_REL_INFO.get(label[\\\"r\\\"], label[\\\"r\\\"]),\\n                \\\"evidence\\\": label.get(\\\"evidence\\\", []),\\n            })\\n    return gold\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "98cc4f66-2210-4b1e-b1ad-9c28502608a9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"DocRED 关系抽取评测模块。\\\\n\\\\n指标:\\\\n  - F1 / Ign-F1: 关系三元组级别 micro-F1，Ign-F1 排除训练集中出现的三元组\\\\n  - Evi-F1: 对正确预测的三元组，计算 evidence 句子级 F1\\\\n  - EDCR: Evidence Distractor Citation Rate，预测 evidence 中非 gold 的比例\\\\n\\\\n输入: 预测列表 + gold 标注列表（每个元素为文档级标注）\\\\n输出: 指标字典\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport json\\\\nimport logging\\\\nfrom collections import defaultdict\\\\nfrom typing import Optional\\\\n\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\n\\\\ndef _triple_key(doc_id: str, head: str, tail: str, relation: str) -> tuple:\\\\n    return (doc_id, head.lower().strip(), tail.lower().strip(), relation.lower().strip())\\\\n\\\\n\\\\nclass DocREDEvaluator:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"DocRED 评测器。\\\\n\\\\n    Args:\\\\n        train_triples: 训练集中的三元组集合，用于计算 Ign-F1。\\\\n                       每个元素为 (doc_title, head_name, tail_name, relation)。\\\\n                       为 None 时 Ign-F1 = F1。\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\n    def __init__(self, train_triples: Optional[set[tuple]] = None, train_facts: Optional[set[tuple]] = None):\\\\n        self.train_triples = train_triples or set()\\\\n        self.train_facts = train_facts or set()\\\\n\\\\n    @classmethod\\\\n    def from_train_file(cls, train_path: str) -> \\\\\\\"DocREDEvaluator\\\\\\\":\\\\n        \\\\\\\"\\\\\\\"\\\\\\\"从训练集 JSON 文件构建 evaluator，自动提取训练集三元组。\\\\\\\"\\\\\\\"\\\\\\\"\\\\n        from freige.data.docred_processor import DOCRED_REL_INFO\\\\n\\\\n        with open(train_path) as f:\\\\n            train_data = json.load(f)\\\\n\\\\n        train_triples = set()\\\\n        train_facts = set()\\\\n        for doc in train_data:\\\\n            doc_id = doc.get(\\\\\\\"title\\\\\\\", \\\\\\\"\\\\\\\")\\\\n            vertex_set = doc[\\\\\\\"vertexSet\\\\\\\"]\\\\n            for label in doc.get(\\\\\\\"labels\\\\\\\", []):\\\\n                h_name = vertex_set[label[\\\\\\\"h\\\\\\\"]][0][\\\\\\\"name\\\\\\\"]\\\\n                t_name = vertex_set[label[\\\\\\\"t\\\\\\\"]][0][\\\\\\\"name\\\\\\\"]\\\\n                rel_name = DOCRED_REL_INFO.get(label[\\\\\\\"r\\\\\\\"], label[\\\\\\\"r\\\\\\\"])\\\\n                train_triples.add(\\\\n                    _triple_key(doc_id, h_name, t_name, rel_name)\\\\n                )\\\\n                train_facts.add((h_name.lower().strip(), t_name.lower().strip(), rel_name.lower().strip()))\\\\n\\\\n        logger.info(\\\\\\\"Loaded %d training triples (%d unique facts) for Ign-F1\\\\\\\", len(train_triples), len(train_facts))\\\\n        return cls(train_triples=train_triples, train_facts=train_facts)\\\\n\\\\n    def compute_f1(\\\\n        self,\\\\n        predictions: list[dict],\\\\n        gold: list[dict],\\\\n    ) -> dict:\\\\n        \\\\\\\"\\\\\\\"\\\\\\\"计算 F1 和 Ign-F1。\\\\\\\"\\\\\\\"\\\\\\\"\\\\n        pred_set = set()\\\\n        for p in predictions:\\\\n            pred_set.add(_triple_key(\\\\n                p[\\\\\\\"doc_id\\\\\\\"], p[\\\\\\\"head\\\\\\\"], p[\\\\\\\"tail\\\\\\\"], p[\\\\\\\"relation\\\\\\\"]\\\\n            ))\\\\n\\\\n        gold_set = set()\\\\n        for g in gold:\\\\n            gold_set.add(_triple_key(\\\\n                g[\\\\\\\"doc_id\\\\\\\"], g[\\\\\\\"head\\\\\\\"], g[\\\\\\\"tail\\\\\\\"], g[\\\\\\\"relation\\\\\\\"]\\\\n            ))\\\\n\\\\n        tp = pred_set & gold_set\\\\n        precision = len(tp) / len(pred_set) if pred_set else 0.0\\\\n        recall = len(tp) / len(gold_set) if gold_set else 0.0\\\\n        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0\\\\n\\\\n        pred_ign = {k for k in pred_set if k[1:] not in self.train_facts}\\\\n        gold_ign = {k for k in gold_set if k[1:] not in self.train_facts}\\\\n        tp_ign = pred_ign & gold_ign\\\\n        ign_prec = len(tp_ign) / len(pred_ign) if pred_ign else 0.0\\\\n        ign_rec = len(tp_ign) / len(gold_ign) if gold_ign else 0.0\\\\n        ign_f1 = (\\\\n            2 * ign_prec * ign_rec / (ign_prec + ign_rec)\\\\n            if (ign_prec + ign_rec) > 0 else 0.0\\\\n        )\\\\n\\\\n        return {\\\\n            \\\\\\\"precision\\\\\\\": precision,\\\\n            \\\\\\\"recall\\\\\\\": recall,\\\\n            \\\\\\\"f1\\\\\\\": f1,\\\\n            \\\\\\\"ign_precision\\\\\\\": ign_prec,\\\\n            \\\\\\\"ign_recall\\\\\\\": ign_rec,\\\\n            \\\\\\\"ign_f1\\\\\\\": ign_f1,\\\\n            \\\\\\\"tp\\\\\\\": len(tp),\\\\n            \\\\\\\"pred_count\\\\\\\": len(pred_set),\\\\n            \\\\\\\"gold_count\\\\\\\": len(gold_set),\\\\n        }\\\\n\\\\n    def compute_evi_f1(\\\\n        self,\\\\n        predictions: list[dict],\\\\n        gold: list[dict],\\\\n    ) -> dict:\\\\n        \\\\\\\"\\\\\\\"\\\\\\\"计�� Evidence F1（句子级）。\\\\\\\"\\\\\\\"\\\\\\\"\\\\n        gold_map = {}\\\\n        for g in gold:\\\\n            key = _triple_key(g[\\\\\\\"doc_id\\\\\\\"], g[\\\\\\\"head\\\\\\\"], g[\\\\\\\"tail\\\\\\\"], g[\\\\\\\"relation\\\\\\\"])\\\\n            gold_map.setdefault(key, set()).update(g.get(\\\\\\\"evidence\\\\\\\", []))\\\\n\\\\n        total_tp = 0\\\\n        total_pred = 0\\\\n      \\\\n\\\\n... [截断: 输出过长，省略 5937 字符] ...\\\\n\\\\n\\\\n            return False\\\\n\\\\n    @staticmethod\\\\n    def _parse_raw_json_list(text: str) -> Optional[list]:\\\\n        try:\\\\n            obj = json.loads(text)\\\\n            if isinstance(obj, list):\\\\n                return obj\\\\n        except json.JSONDecodeError:\\\\n            start = text.find(\\\\\\\"[\\\\\\\")\\\\n            end = text.rfind(\\\\\\\"]\\\\\\\") + 1\\\\n            if start >= 0 and end > start:\\\\n                try:\\\\n                    obj = json.loads(text[start:end])\\\\n                    if isinstance(obj, list):\\\\n                        return obj\\\\n                except json.JSONDecodeError:\\\\n                    pass\\\\n        return None\\\\n\\\\n    def evaluate(\\\\n        self,\\\\n        predictions: list[dict],\\\\n        gold: list[dict],\\\\n        raw_outputs: Optional[list[dict]] = None,\\\\n    ) -> dict:\\\\n        \\\\\\\"\\\\\\\"\\\\\\\"运行所有评测指标。\\\\\\\"\\\\\\\"\\\\\\\"\\\\n        f1_metrics = self.compute_f1(predictions, gold)\\\\n        evi_metrics = self.compute_evi_f1(predictions, gold)\\\\n        edcr_metrics = self.compute_edcr(predictions, gold)\\\\n        result = {**f1_metrics, **evi_metrics, **edcr_metrics}\\\\n        result.update(self.compute_evi_f1_joint(predictions, gold))\\\\n        if raw_outputs is not None:\\\\n            result.update(self.compute_format_compliance(raw_outputs))\\\\n        return result\\\\n\\\\n\\\\n\\\\n\\\\ndef _try_parse_json_list(text):\\\\n    try:\\\\n        obj = json.loads(text)\\\\n        if isinstance(obj, list):\\\\n            return obj\\\\n    except json.JSONDecodeError:\\\\n        pass\\\\n    return None\\\\n\\\\n\\\\ndef _repair_truncated_json(text):\\\\n    stripped = text.rstrip().rstrip(\\\\\\\",\\\\\\\")\\\\n    for suffix in [\\\\\\\"]\\\\\\\", \\\\\\\"}]\\\\\\\", '\\\\\\\"' + '}' + ']', \\\\\\\"null}]\\\\\\\"]:\\\\n        result = _try_parse_json_list(stripped + suffix)\\\\n        if result is not None:\\\\n            return result\\\\n\\\\n    last_brace = text.rfind(\\\\\\\"}\\\\\\\")\\\\n    if last_brace > 0:\\\\n        result = _try_parse_json_list(text[: last_brace + 1] + \\\\\\\"]\\\\\\\")\\\\n        if result is not None:\\\\n            return result\\\\n\\\\n    return None\\\\n\\\\n\\\\ndef _get_field(d, *keys):\\\\n    for k in keys:\\\\n        if k in d:\\\\n            return d[k]\\\\n    return None\\\\n\\\\n\\\\ndef _normalize_triples(triples):\\\\n    results = []\\\\n    for t in triples:\\\\n        if not isinstance(t, dict):\\\\n            continue\\\\n        head = _get_field(t, \\\\\\\"head\\\\\\\", \\\\\\\"head_entity\\\\\\\")\\\\n        tail = _get_field(t, \\\\\\\"tail\\\\\\\", \\\\\\\"tail_entity\\\\\\\")\\\\n        relation = _get_field(t, \\\\\\\"relation\\\\\\\", \\\\\\\"type\\\\\\\", \\\\\\\"label\\\\\\\")\\\\n        if head is None or tail is None or relation is None:\\\\n            continue\\\\n        evidence = _get_field(t, \\\\\\\"evidence\\\\\\\", \\\\\\\"sentence_ids\\\\\\\") or []\\\\n        results.append({\\\\n            \\\\\\\"head\\\\\\\": str(head),\\\\n            \\\\\\\"relation\\\\\\\": str(relation).lower().strip(),\\\\n            \\\\\\\"tail\\\\\\\": str(tail),\\\\n            \\\\\\\"evidence\\\\\\\": evidence,\\\\n        })\\\\n    return results\\\\n\\\\n\\\\ndef parse_model_output(output_text: str) -> tuple[list[dict], bool]:\\\\n    text = output_text.strip()\\\\n\\\\n    parsed = _try_parse_json_list(text)\\\\n    if parsed is not None:\\\\n        return _normalize_triples(parsed), True\\\\n\\\\n    start = text.find(\\\\\\\"[\\\\\\\")\\\\n    if start >= 0:\\\\n        end = text.rfind(\\\\\\\"]\\\\\\\")\\\\n        if end > start:\\\\n            parsed = _try_parse_json_list(text[start : end + 1])\\\\n            if parsed is not None:\\\\n                return _normalize_triples(parsed), True\\\\n\\\\n        repaired = _repair_truncated_json(text[start:])\\\\n        if repaired is not None:\\\\n            return _normalize_triples(repaired), True\\\\n\\\\n    return [], False\\\\n\\\\ndef gold_from_docred(\\\\n    docred_data: list[dict],\\\\n) -> list[dict]:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"将 DocRED 原始数据转为评测用 gold 格式。\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    from freige.data.docred_processor import DOCRED_REL_INFO\\\\n\\\\n    gold = []\\\\n    for doc in docred_data:\\\\n        doc_id = doc.get(\\\\\\\"title\\\\\\\", \\\\\\\"\\\\\\\")\\\\n        vertex_set = doc[\\\\\\\"vertexSet\\\\\\\"]\\\\n        for label in doc.get(\\\\\\\"labels\\\\\\\", []):\\\\n            h_name = vertex_set[label[\\\\\\\"h\\\\\\\"]][0][\\\\\\\"name\\\\\\\"]\\\\n            t_name = vertex_set[label[\\\\\\\"t\\\\\\\"]][0][\\\\\\\"name\\\\\\\"]\\\\n            gold.append({\\\\n                \\\\\\\"doc_id\\\\\\\": doc_id,\\\\n                \\\\\\\"head\\\\\\\": h_name,\\\\n                \\\\\\\"tail\\\\\\\": t_name,\\\\n                \\\\\\\"relation\\\\\\\": DOCRED_REL_INFO.get(label[\\\\\\\"r\\\\\\\"], label[\\\\\\\"r\\\\\\\"]),\\\\n                \\\\\\\"evidence\\\\\\\": label.get(\\\\\\\"evidence\\\\\\\", []),\\\\n            })\\\\n    return gold\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"DocRED 关系抽取评测模块。\\n\\n指标:\\n  - F1 / Ign-F1: 关系三元组级别 micro-F1，Ign-F1 排除训练集中出现的三元组\\n  - Evi-F1: 对正确预测的三元组，计算 evidence 句子级 F1\\n  - EDCR: Evidence Distractor Citation Rate，预测 evidence 中非 gold 的比例\\n\\n输入: 预测列表 + gold 标注列表（每个元素为文档级标注）\\n输出: 指标字典\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nfrom collections import defaultdict\\nfrom typing import Optional\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef _triple_key(doc_id: str, head: str, tail: str, relation: str) -> tuple:\\n    return (doc_id, head.lower().strip(), tail.lower().strip(), relation.lower().strip())\\n\\n\\nclass DocREDEvaluator:\\n    \\\"\\\"\\\"DocRED 评测器。\\n\\n    Args:\\n        train_triples: 训练集中的三元组集合，用于计算 Ign-F1。\\n                       每个元素为 (doc_title, head_name, tail_name, relation)。\\n                       为 None 时 Ign-F1 = F1。\\n    \\\"\\\"\\\"\\n\\n    def __init__(self, train_triples: Optional[set[tuple]] = None, train_facts: Optional[set[tuple]] = None):\\n        self.train_triples = train_triples or set()\\n        self.train_facts = train_facts or set()\\n\\n    @classmethod\\n    def from_train_file(cls, train_path: str) -> \\\"DocREDEvaluator\\\":\\n        \\\"\\\"\\\"从训练集 JSON 文件构建 evaluator，自动提取训练集三元组。\\\"\\\"\\\"\\n        from freige.data.docred_processor import DOCRED_REL_INFO\\n\\n        with open(train_path) as f:\\n            train_data = json.load(f)\\n\\n        train_triples = set()\\n        train_facts = set()\\n        for doc in train_data:\\n            doc_id = doc.get(\\\"title\\\", \\\"\\\")\\n            vertex_set = doc[\\\"vertexSet\\\"]\\n            for label in doc.get(\\\"labels\\\", []):\\n                h_name = vertex_set[label[\\\"h\\\"]][0][\\\"name\\\"]\\n                t_name = vertex_set[label[\\\"t\\\"]][0][\\\"name\\\"]\\n                rel_name = DOCRED_REL_INFO.get(label[\\\"r\\\"], label[\\\"r\\\"])\\n                train_triples.add(\\n                    _triple_key(doc_id, h_name, t_name, rel_name)\\n                )\\n                train_facts.add((h_name.lower().strip(), t_name.lower().strip(), rel_name.lower().strip()))\\n\\n        logger.info(\\\"Loaded %d training triples (%d unique facts) for Ign-F1\\\", len(train_triples), len(train_facts))\\n        return cls(train_triples=train_triples, train_facts=train_facts)\\n\\n    def compute_f1(\\n        self,\\n        predictions: list[dict],\\n        gold: list[dict],\\n    ) -> dict:\\n        \\\"\\\"\\\"计算 F1 和 Ign-F1。\\\"\\\"\\\"\\n        pred_set = set()\\n        for p in predictions:\\n            pred_set.add(_triple_key(\\n                p[\\\"doc_id\\\"], p[\\\"head\\\"], p[\\\"tail\\\"], p[\\\"relation\\\"]\\n            ))\\n\\n        gold_set = set()\\n        for g in gold:\\n            gold_set.add(_triple_key(\\n                g[\\\"doc_id\\\"], g[\\\"head\\\"], g[\\\"tail\\\"], g[\\\"relation\\\"]\\n            ))\\n\\n        tp = pred_set & gold_set\\n        precision = len(tp) / len(pred_set) if pred_set else 0.0\\n        recall = len(tp) / len(gold_set) if gold_set else 0.0\\n        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0\\n\\n        pred_ign = {k for k in pred_set if k[1:] not in self.train_facts}\\n        gold_ign = {k for k in gold_set if k[1:] not in self.train_facts}\\n        tp_ign = pred_ign & gold_ign\\n        ign_prec = len(tp_ign) / len(pred_ign) if pred_ign else 0.0\\n        ign_rec = len(tp_ign) / len(gold_ign) if gold_ign else 0.0\\n        ign_f1 = (\\n            2 * ign_prec * ign_rec / (ign_prec + ign_rec)\\n            if (ign_prec + ign_rec) > 0 else 0.0\\n        )\\n\\n        return {\\n            \\\"precision\\\": precision,\\n            \\\"recall\\\": recall,\\n            \\\"f1\\\": f1,\\n            \\\"ign_precision\\\": ign_prec,\\n            \\\"ign_recall\\\": ign_rec,\\n            \\\"ign_f1\\\": ign_f1,\\n            \\\"tp\\\": len(tp),\\n            \\\"pred_count\\\": len(pred_set),\\n            \\\"gold_count\\\": len(gold_set),\\n        }\\n\\n    def compute_evi_f1(\\n        self,\\n        predictions: list[dict],\\n        gold: list[dict],\\n    ) -> dict:\\n        \\\"\\\"\\\"计�� Evidence F1（句子级）。\\\"\\\"\\\"\\n        gold_map = {}\\n        for g in gold:\\n            key = _triple_key(g[\\\"doc_id\\\"], g[\\\"head\\\"], g[\\\"tail\\\"], g[\\\"relation\\\"])\\n            gold_map.setdefault(key, set()).update(g.get(\\\"evidence\\\", []))\\n\\n        total_tp = 0\\n        total_pred = 0\\n      \\n\\n... [截断: 输出过长，省略 5937 字符] ...\\n\\n\\n            return False\\n\\n    @staticmethod\\n    def _parse_raw_json_list(text: str) -> Optional[list]:\\n        try:\\n            obj = json.loads(text)\\n            if isinstance(obj, list):\\n                return obj\\n        except json.JSONDecodeError:\\n            start = text.find(\\\"[\\\")\\n            end = text.rfind(\\\"]\\\") + 1\\n            if start >= 0 and end > start:\\n                try:\\n                    obj = json.loads(text[start:end])\\n                    if isinstance(obj, list):\\n                        return obj\\n                except json.JSONDecodeError:\\n                    pass\\n        return None\\n\\n    def evaluate(\\n        self,\\n        predictions: list[dict],\\n        gold: list[dict],\\n        raw_outputs: Optional[list[dict]] = None,\\n    ) -> dict:\\n        \\\"\\\"\\\"运行所有评测指标。\\\"\\\"\\\"\\n        f1_metrics = self.compute_f1(predictions, gold)\\n        evi_metrics = self.compute_evi_f1(predictions, gold)\\n        edcr_metrics = self.compute_edcr(predictions, gold)\\n        result = {**f1_metrics, **evi_metrics, **edcr_metrics}\\n        result.update(self.compute_evi_f1_joint(predictions, gold))\\n        if raw_outputs is not None:\\n            result.update(self.compute_format_compliance(raw_outputs))\\n        return result\\n\\n\\n\\n\\ndef _try_parse_json_list(text):\\n    try:\\n        obj = json.loads(text)\\n        if isinstance(obj, list):\\n            return obj\\n    except json.JSONDecodeError:\\n        pass\\n    return None\\n\\n\\ndef _repair_truncated_json(text):\\n    stripped = text.rstrip().rstrip(\\\",\\\")\\n    for suffix in [\\\"]\\\", \\\"}]\\\", '\\\"' + '}' + ']', \\\"null}]\\\"]:\\n        result = _try_parse_json_list(stripped + suffix)\\n        if result is not None:\\n            return result\\n\\n    last_brace = text.rfind(\\\"}\\\")\\n    if last_brace > 0:\\n        result = _try_parse_json_list(text[: last_brace + 1] + \\\"]\\\")\\n        if result is not None:\\n            return result\\n\\n    return None\\n\\n\\ndef _get_field(d, *keys):\\n    for k in keys:\\n        if k in d:\\n            return d[k]\\n    return None\\n\\n\\ndef _normalize_triples(triples):\\n    results = []\\n    for t in triples:\\n        if not isinstance(t, dict):\\n            continue\\n        head = _get_field(t, \\\"head\\\", \\\"head_entity\\\")\\n        tail = _get_field(t, \\\"tail\\\", \\\"tail_entity\\\")\\n        relation = _get_field(t, \\\"relation\\\", \\\"type\\\", \\\"label\\\")\\n        if head is None or tail is None or relation is None:\\n            continue\\n        evidence = _get_field(t, \\\"evidence\\\", \\\"sentence_ids\\\") or []\\n        results.append({\\n            \\\"head\\\": str(head),\\n            \\\"relation\\\": str(relation).lower().strip(),\\n            \\\"tail\\\": str(tail),\\n            \\\"evidence\\\": evidence,\\n        })\\n    return results\\n\\n\\ndef parse_model_output(output_text: str) -> tuple[list[dict], bool]:\\n    text = output_text.strip()\\n\\n    parsed = _try_parse_json_list(text)\\n    if parsed is not None:\\n        return _normalize_triples(parsed), True\\n\\n    start = text.find(\\\"[\\\")\\n    if start >= 0:\\n        end = text.rfind(\\\"]\\\")\\n        if end > start:\\n            parsed = _try_parse_json_list(text[start : end + 1])\\n            if parsed is not None:\\n                return _normalize_triples(parsed), True\\n\\n        repaired = _repair_truncated_json(text[start:])\\n        if repaired is not None:\\n            return _normalize_triples(repaired), True\\n\\n    return [], False\\n\\ndef gold_from_docred(\\n    docred_data: list[dict],\\n) -> list[dict]:\\n    \\\"\\\"\\\"将 DocRED 原始数据转为评测用 gold 格式。\\\"\\\"\\\"\\n    from freige.data.docred_processor import DOCRED_REL_INFO\\n\\n    gold = []\\n    for doc in docred_data:\\n        doc_id = doc.get(\\\"title\\\", \\\"\\\")\\n        vertex_set = doc[\\\"vertexSet\\\"]\\n        for label in doc.get(\\\"labels\\\", []):\\n            h_name = vertex_set[label[\\\"h\\\"]][0][\\\"name\\\"]\\n            t_name = vertex_set[label[\\\"t\\\"]][0][\\\"name\\\"]\\n            gold.append({\\n                \\\"doc_id\\\": doc_id,\\n                \\\"head\\\": h_name,\\n                \\\"tail\\\": t_name,\\n                \\\"relation\\\": DOCRED_REL_INFO.get(label[\\\"r\\\"], label[\\\"r\\\"]),\\n                \\\"evidence\\\": label.get(\\\"evidence\\\", []),\\n            })\\n    return gold\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 16 · 2026-05-17T12:55:06.708Z_

<details><summary>↩ Tool result · `toolu_01JDzHqtbxF5yXytso539cMG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"import os\\nimport os.path\\nimport json\\nimport numpy as np\\nfrom tqdm import tqdm\\n\\nrel2id = json.load(open('meta/rel2id.json', 'r'))\\nid2rel = {value: key for key, value in rel2id.items()}\\n\\ndef get_title2pred(pred: list) -> dict:\\n    '''\\n    Convert predictions into dictionary.\\n    Input:\\n        :pred: list of dictionaries, each dictionary entry is a predicted relation triple. Keys: ['title', 'h_idx', 't_idx', 'r', 'evidence', 'score']  \\n    Output:\\n        :title2pred: dictionary with (key, value) = (title, {rel_triple: score})\\n    '''\\n    \\n    title2pred = {}\\n\\n    for p in pred:\\n        if p[\\\"r\\\"] == \\\"Na\\\":\\n            continue\\n        curr = (p[\\\"h_idx\\\"], p[\\\"t_idx\\\"], p[\\\"r\\\"])\\n        \\n        if p[\\\"title\\\"] in title2pred:\\n            if curr in title2pred[p[\\\"title\\\"]]:\\n                title2pred[p[\\\"title\\\"]][curr] = max(p[\\\"score\\\"], title2pred[p[\\\"title\\\"]][curr])\\n            else:\\n                title2pred[p[\\\"title\\\"]][curr] = p[\\\"score\\\"]\\n        else:\\n            title2pred[p[\\\"title\\\"]] = {curr: p[\\\"score\\\"]}\\n    return title2pred\\n\\n\\ndef get_title2gt(features: dict) -> dict:\\n    '''\\n    Convert ground-truth labels to dictionary.\\n    Input:\\n        :features: list of features within each document. Identical to the lists obtained from pre-processing.\\n    Output:\\n        :title2gt: dictionary with (key, value) = (title, [gold_triples])\\n    '''\\n    title2gt = {}\\n    for f in features:\\n        title = f[\\\"title\\\"]\\n        title2gt[title] = []\\n        for idx, p in enumerate(f[\\\"hts\\\"]): \\n            h,t = p\\n            label = np.array(f['labels'][idx])\\n            rs = np.nonzero(label[1:])[0] + 1 # + 1 for no-label\\n            title2gt[title].extend([(h,t,id2rel[r]) for r in rs])\\n            \\n    return title2gt\\n\\ndef select_thresh(cand: list, num_gt: int, correct: int, num_pred: int):\\n    '''\\n    select threshold for relation predictions.\\n    Input:\\n        :cand: list of relation candidates\\n        :num_gt: number of ground-truth relations.\\n        :correct: number of correct relation predictions selected.\\n        :num_pred: number of relation predictions selected.\\n    Output:\\n        :thresh: threshold for selecting relations.\\n        :sorted_pred: predictions selected from cand. \\n    '''\\n    \\n    sorted_pred = sorted(cand, key=lambda x:x[1], reverse=True)\\n    precs, recalls = [], []\\n    \\n    for pred in sorted_pred:     \\n        correct += pred[0]\\n        num_pred += 1\\n        precs.append(correct / num_pred)  # Precision\\n        recalls.append(correct / num_gt)  # Recall                             \\n\\n    recalls = np.asarray(recalls, dtype='float32')\\n    precs = np.asarray(precs, dtype='float32')\\n    f1_arr = (2 * recalls * precs / (recalls + precs + 1e-20))\\n    f1 = f1_arr.max()\\n    f1_pos = f1_arr.argmax()\\n    thresh = sorted_pred[f1_pos][1]\\n\\n    print('Best thresh', thresh, '\\\\tbest F1', f1)\\n    return thresh, sorted_pred[:f1_pos + 1]\\n\\n\\ndef merge_results(pred: list, pred_pseudo: list, features: list, thresh: float = None):\\n    '''\\n    Merge relation predictions from the original document and psuedo documents.\\n    Input:\\n        :pred: list of dictionaries, each dictionary entry is a predicted relation triple from the original document. Keys: ['title', 'h_idx', 't_idx', 'r', 'evidence', 'score'].\\n        :pred_pseudo: list of dictionaries, each dictionary entry is a predicted relation triple from pseudo documents. Keys: ['title', 'h_idx', 't_idx', 'r', 'evidence', 'score'].\\n        :features: list of features within each document. Identical to the lists obtained from pre-processing.\\n        :thresh: threshold for selecting predictions.\\n    Output:\\n        :merged_res: list of merged relation predictions. Each relation prediction is a dictionay with keys (title, h_idx, t_idx, r).\\n        :thresh: threshold of selecting relation predictions.\\n    '''\\n    \\n    title2pred = get_title2pred(pred)\\n    title2pred_pseudo = get_title2pred(pred_pseudo)\\n\\n    title2gt = get_title2gt(features)\\n    num_gt = sum([len(title2gt[t]) for t in title2gt])\\n\\n    titl\\n\\n... [截断: 输出过长，省略 5470 字符] ...\\n\\nal evaluation code\\n    '''\\n    truth_dir = os.path.join(path, 'ref')\\n\\n    if not os.path.exists(truth_dir):\\n        os.makedirs(truth_dir)\\n\\n    fact_in_train_annotated = gen_train_facts(os.path.join(path, train_file), truth_dir)\\n    fact_in_train_distant = gen_train_facts(os.path.join(path, \\\"train_distant.json\\\"), truth_dir)\\n\\n    truth = json.load(open(os.path.join(path, dev_file)))\\n        \\n    std = {}\\n    tot_evidences = 0\\n    titleset = set([])\\n\\n    title2vectexSet = {}\\n\\n    for x in truth:\\n        title = x['title']\\n        titleset.add(title)\\n\\n        vertexSet = x['vertexSet']\\n        title2vectexSet[title] = vertexSet\\n\\n        if 'labels' not in x: # official test set from DocRED\\n            continue\\n        \\n        for label in x['labels']:\\n            r = label['r']\\n            h_idx = label['h']\\n            t_idx = label['t']\\n            std[(title, r, h_idx, t_idx)] = set(label['evidence'])\\n            tot_evidences += len(label['evidence'])\\n\\n    tot_relations = len(std)\\n    tmp.sort(key=lambda x: (x['title'], x['h_idx'], x['t_idx'], x['r']))\\n    submission_answer = [tmp[0]]\\n\\n    for i in range(1, len(tmp)):\\n        x = tmp[i]\\n        y = tmp[i - 1]\\n        if (x['title'], x['h_idx'], x['t_idx'], x['r']) != (y['title'], y['h_idx'], y['t_idx'], y['r']):\\n            submission_answer.append(tmp[i])\\n\\n    correct_re = 0\\n    correct_evidence = 0\\n    pred_evi = 0\\n\\n    correct_in_train_annotated = 0\\n    correct_in_train_distant = 0\\n    titleset2 = set([])\\n    for x in submission_answer:\\n        title = x['title']\\n        h_idx = x['h_idx']\\n        t_idx = x['t_idx']\\n        r = x['r']\\n        titleset2.add(title)\\n        if title not in title2vectexSet:\\n            continue\\n        vertexSet = title2vectexSet[title]\\n\\n        if 'evidence' in x : #and (title, h_idx, t_idx) in std:\\n            evi = set(x['evidence'])\\n        else:\\n            evi = set([])\\n        pred_evi += len(evi)\\n\\n        if (title, r, h_idx, t_idx) in std:\\n            correct_re += 1\\n            stdevi = std[(title, r, h_idx, t_idx)]\\n            correct_evidence += len(stdevi & evi)\\n            in_train_annotated = in_train_distant = False\\n            for n1 in vertexSet[h_idx]:\\n                for n2 in vertexSet[t_idx]:\\n                    if (n1['name'], n2['name'], r) in fact_in_train_annotated:\\n                        in_train_annotated = True\\n                    if (n1['name'], n2['name'], r) in fact_in_train_distant:\\n                        in_train_distant = True\\n\\n            if in_train_annotated:\\n                correct_in_train_annotated += 1\\n            if in_train_distant:\\n                correct_in_train_distant += 1\\n\\n    re_p = 1.0 * correct_re / len(submission_answer)\\n    re_r = 1.0 * correct_re / tot_relations if tot_relations != 0 else 0\\n    if re_p + re_r == 0:\\n        re_f1 = 0\\n    else:\\n        re_f1 = 2.0 * re_p * re_r / (re_p + re_r)\\n\\n    evi_p = 1.0 * correct_evidence / pred_evi if pred_evi > 0 else 0\\n    evi_r = 1.0 * correct_evidence / tot_evidences if tot_evidences > 0 else 0\\n\\n    if evi_p + evi_r == 0:\\n        evi_f1 = 0\\n    else:\\n        evi_f1 = 2.0 * evi_p * evi_r / (evi_p + evi_r)\\n\\n    re_p_ignore_train_annotated = 1.0 * (correct_re - correct_in_train_annotated) / (len(submission_answer) - correct_in_train_annotated + 1e-5)\\n    re_p_ignore_train = 1.0 * (correct_re - correct_in_train_distant) / (len(submission_answer) - correct_in_train_distant + 1e-5)\\n\\n    if re_p_ignore_train_annotated + re_r == 0:\\n        re_f1_ignore_train_annotated = 0\\n    else:\\n        re_f1_ignore_train_annotated = 2.0 * re_p_ignore_train_annotated * re_r / (re_p_ignore_train_annotated + re_r)\\n\\n    if re_p_ignore_train + re_r == 0:\\n        re_f1_ignore_train = 0\\n    else:\\n        re_f1_ignore_train = 2.0 * re_p_ignore_train * re_r / (re_p_ignore_train + re_r)\\n\\n    return [re_p, re_r, re_f1], [evi_p, evi_r, evi_f1],\\\\\\n        [re_p_ignore_train_annotated, re_r, re_f1_ignore_train_annotated], \\\\\\n        [re_p_ignore_train, re_r, re_f1_ignore_train]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "788c7c86-2c70-4a0b-b4c5-c0ee45dd3c28",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"import os\\\\nimport os.path\\\\nimport json\\\\nimport numpy as np\\\\nfrom tqdm import tqdm\\\\n\\\\nrel2id = json.load(open('meta/rel2id.json', 'r'))\\\\nid2rel = {value: key for key, value in rel2id.items()}\\\\n\\\\ndef get_title2pred(pred: list) -> dict:\\\\n    '''\\\\n    Convert predictions into dictionary.\\\\n    Input:\\\\n        :pred: list of dictionaries, each dictionary entry is a predicted relation triple. Keys: ['title', 'h_idx', 't_idx', 'r', 'evidence', 'score']  \\\\n    Output:\\\\n        :title2pred: dictionary with (key, value) = (title, {rel_triple: score})\\\\n    '''\\\\n    \\\\n    title2pred = {}\\\\n\\\\n    for p in pred:\\\\n        if p[\\\\\\\"r\\\\\\\"] == \\\\\\\"Na\\\\\\\":\\\\n            continue\\\\n        curr = (p[\\\\\\\"h_idx\\\\\\\"], p[\\\\\\\"t_idx\\\\\\\"], p[\\\\\\\"r\\\\\\\"])\\\\n        \\\\n        if p[\\\\\\\"title\\\\\\\"] in title2pred:\\\\n            if curr in title2pred[p[\\\\\\\"title\\\\\\\"]]:\\\\n                title2pred[p[\\\\\\\"title\\\\\\\"]][curr] = max(p[\\\\\\\"score\\\\\\\"], title2pred[p[\\\\\\\"title\\\\\\\"]][curr])\\\\n            else:\\\\n                title2pred[p[\\\\\\\"title\\\\\\\"]][curr] = p[\\\\\\\"score\\\\\\\"]\\\\n        else:\\\\n            title2pred[p[\\\\\\\"title\\\\\\\"]] = {curr: p[\\\\\\\"score\\\\\\\"]}\\\\n    return title2pred\\\\n\\\\n\\\\ndef get_title2gt(features: dict) -> dict:\\\\n    '''\\\\n    Convert ground-truth labels to dictionary.\\\\n    Input:\\\\n        :features: list of features within each document. Identical to the lists obtained from pre-processing.\\\\n    Output:\\\\n        :title2gt: dictionary with (key, value) = (title, [gold_triples])\\\\n    '''\\\\n    title2gt = {}\\\\n    for f in features:\\\\n        title = f[\\\\\\\"title\\\\\\\"]\\\\n        title2gt[title] = []\\\\n        for idx, p in enumerate(f[\\\\\\\"hts\\\\\\\"]): \\\\n            h,t = p\\\\n            label = np.array(f['labels'][idx])\\\\n            rs = np.nonzero(label[1:])[0] + 1 # + 1 for no-label\\\\n            title2gt[title].extend([(h,t,id2rel[r]) for r in rs])\\\\n            \\\\n    return title2gt\\\\n\\\\ndef select_thresh(cand: list, num_gt: int, correct: int, num_pred: int):\\\\n    '''\\\\n    select threshold for relation predictions.\\\\n    Input:\\\\n        :cand: list of relation candidates\\\\n        :num_gt: number of ground-truth relations.\\\\n        :correct: number of correct relation predictions selected.\\\\n        :num_pred: number of relation predictions selected.\\\\n    Output:\\\\n        :thresh: threshold for selecting relations.\\\\n        :sorted_pred: predictions selected from cand. \\\\n    '''\\\\n    \\\\n    sorted_pred = sorted(cand, key=lambda x:x[1], reverse=True)\\\\n    precs, recalls = [], []\\\\n    \\\\n    for pred in sorted_pred:     \\\\n        correct += pred[0]\\\\n        num_pred += 1\\\\n        precs.append(correct / num_pred)  # Precision\\\\n        recalls.append(correct / num_gt)  # Recall                             \\\\n\\\\n    recalls = np.asarray(recalls, dtype='float32')\\\\n    precs = np.asarray(precs, dtype='float32')\\\\n    f1_arr = (2 * recalls * precs / (recalls + precs + 1e-20))\\\\n    f1 = f1_arr.max()\\\\n    f1_pos = f1_arr.argmax()\\\\n    thresh = sorted_pred[f1_pos][1]\\\\n\\\\n    print('Best thresh', thresh, '\\\\\\\\tbest F1', f1)\\\\n    return thresh, sorted_pred[:f1_pos + 1]\\\\n\\\\n\\\\ndef merge_results(pred: list, pred_pseudo: list, features: list, thresh: float = None):\\\\n    '''\\\\n    Merge relation predictions from the original document and psuedo documents.\\\\n    Input:\\\\n        :pred: list of dictionaries, each dictionary entry is a predicted relation triple from the original document. Keys: ['title', 'h_idx', 't_idx', 'r', 'evidence', 'score'].\\\\n        :pred_pseudo: list of dictionaries, each dictionary entry is a predicted relation triple from pseudo documents. Keys: ['title', 'h_idx', 't_idx', 'r', 'evidence', 'score'].\\\\n        :features: list of features within each document. Identical to the lists obtained from pre-processing.\\\\n        :thresh: threshold for selecting predictions.\\\\n    Output:\\\\n        :merged_res: list of merged relation predictions. Each relation prediction is a dictionay with keys (title, h_idx, t_idx, r).\\\\n        :thresh: threshold of selecting relation predictions.\\\\n    '''\\\\n    \\\\n    title2pred = get_title2pred(pred)\\\\n    title2pred_pseudo = get_title2pred(pred_pseudo)\\\\n\\\\n    title2gt = get_title2gt(features)\\\\n    num_gt = sum([len(title2gt[t]) for t in title2gt])\\\\n\\\\n    titl\\\\n\\\\n... [截断: 输出过长，省略 5470 字符] ...\\\\n\\\\nal evaluation code\\\\n    '''\\\\n    truth_dir = os.path.join(path, 'ref')\\\\n\\\\n    if not os.path.exists(truth_dir):\\\\n        os.makedirs(truth_dir)\\\\n\\\\n    fact_in_train_annotated = gen_train_facts(os.path.join(path, train_file), truth_dir)\\\\n    fact_in_train_distant = gen_train_facts(os.path.join(path, \\\\\\\"train_distant.json\\\\\\\"), truth_dir)\\\\n\\\\n    truth = json.load(open(os.path.join(path, dev_file)))\\\\n        \\\\n    std = {}\\\\n    tot_evidences = 0\\\\n    titleset = set([])\\\\n\\\\n    title2vectexSet = {}\\\\n\\\\n    for x in truth:\\\\n        title = x['title']\\\\n        titleset.add(title)\\\\n\\\\n        vertexSet = x['vertexSet']\\\\n        title2vectexSet[title] = vertexSet\\\\n\\\\n        if 'labels' not in x: # official test set from DocRED\\\\n            continue\\\\n        \\\\n        for label in x['labels']:\\\\n            r = label['r']\\\\n            h_idx = label['h']\\\\n            t_idx = label['t']\\\\n            std[(title, r, h_idx, t_idx)] = set(label['evidence'])\\\\n            tot_evidences += len(label['evidence'])\\\\n\\\\n    tot_relations = len(std)\\\\n    tmp.sort(key=lambda x: (x['title'], x['h_idx'], x['t_idx'], x['r']))\\\\n    submission_answer = [tmp[0]]\\\\n\\\\n    for i in range(1, len(tmp)):\\\\n        x = tmp[i]\\\\n        y = tmp[i - 1]\\\\n        if (x['title'], x['h_idx'], x['t_idx'], x['r']) != (y['title'], y['h_idx'], y['t_idx'], y['r']):\\\\n            submission_answer.append(tmp[i])\\\\n\\\\n    correct_re = 0\\\\n    correct_evidence = 0\\\\n    pred_evi = 0\\\\n\\\\n    correct_in_train_annotated = 0\\\\n    correct_in_train_distant = 0\\\\n    titleset2 = set([])\\\\n    for x in submission_answer:\\\\n        title = x['title']\\\\n        h_idx = x['h_idx']\\\\n        t_idx = x['t_idx']\\\\n        r = x['r']\\\\n        titleset2.add(title)\\\\n        if title not in title2vectexSet:\\\\n            continue\\\\n        vertexSet = title2vectexSet[title]\\\\n\\\\n        if 'evidence' in x : #and (title, h_idx, t_idx) in std:\\\\n            evi = set(x['evidence'])\\\\n        else:\\\\n            evi = set([])\\\\n        pred_evi += len(evi)\\\\n\\\\n        if (title, r, h_idx, t_idx) in std:\\\\n            correct_re += 1\\\\n            stdevi = std[(title, r, h_idx, t_idx)]\\\\n            correct_evidence += len(stdevi & evi)\\\\n            in_train_annotated = in_train_distant = False\\\\n            for n1 in vertexSet[h_idx]:\\\\n                for n2 in vertexSet[t_idx]:\\\\n                    if (n1['name'], n2['name'], r) in fact_in_train_annotated:\\\\n                        in_train_annotated = True\\\\n                    if (n1['name'], n2['name'], r) in fact_in_train_distant:\\\\n                        in_train_distant = True\\\\n\\\\n            if in_train_annotated:\\\\n                correct_in_train_annotated += 1\\\\n            if in_train_distant:\\\\n                correct_in_train_distant += 1\\\\n\\\\n    re_p = 1.0 * correct_re / len(submission_answer)\\\\n    re_r = 1.0 * correct_re / tot_relations if tot_relations != 0 else 0\\\\n    if re_p + re_r == 0:\\\\n        re_f1 = 0\\\\n    else:\\\\n        re_f1 = 2.0 * re_p * re_r / (re_p + re_r)\\\\n\\\\n    evi_p = 1.0 * correct_evidence / pred_evi if pred_evi > 0 else 0\\\\n    evi_r = 1.0 * correct_evidence / tot_evidences if tot_evidences > 0 else 0\\\\n\\\\n    if evi_p + evi_r == 0:\\\\n        evi_f1 = 0\\\\n    else:\\\\n        evi_f1 = 2.0 * evi_p * evi_r / (evi_p + evi_r)\\\\n\\\\n    re_p_ignore_train_annotated = 1.0 * (correct_re - correct_in_train_annotated) / (len(submission_answer) - correct_in_train_annotated + 1e-5)\\\\n    re_p_ignore_train = 1.0 * (correct_re - correct_in_train_distant) / (len(submission_answer) - correct_in_train_distant + 1e-5)\\\\n\\\\n    if re_p_ignore_train_annotated + re_r == 0:\\\\n        re_f1_ignore_train_annotated = 0\\\\n    else:\\\\n        re_f1_ignore_train_annotated = 2.0 * re_p_ignore_train_annotated * re_r / (re_p_ignore_train_annotated + re_r)\\\\n\\\\n    if re_p_ignore_train + re_r == 0:\\\\n        re_f1_ignore_train = 0\\\\n    else:\\\\n        re_f1_ignore_train = 2.0 * re_p_ignore_train * re_r / (re_p_ignore_train + re_r)\\\\n\\\\n    return [re_p, re_r, re_f1], [evi_p, evi_r, evi_f1],\\\\\\\\\\\\n        [re_p_ignore_train_annotated, re_r, re_f1_ignore_train_annotated], \\\\\\\\\\\\n        [re_p_ignore_train, re_r, re_f1_ignore_train]\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.38}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"import os\\nimport os.path\\nimport json\\nimport numpy as np\\nfrom tqdm import tqdm\\n\\nrel2id = json.load(open('meta/rel2id.json', 'r'))\\nid2rel = {value: key for key, value in rel2id.items()}\\n\\ndef get_title2pred(pred: list) -> dict:\\n    '''\\n    Convert predictions into dictionary.\\n    Input:\\n        :pred: list of dictionaries, each dictionary entry is a predicted relation triple. Keys: ['title', 'h_idx', 't_idx', 'r', 'evidence', 'score']  \\n    Output:\\n        :title2pred: dictionary with (key, value) = (title, {rel_triple: score})\\n    '''\\n    \\n    title2pred = {}\\n\\n    for p in pred:\\n        if p[\\\"r\\\"] == \\\"Na\\\":\\n            continue\\n        curr = (p[\\\"h_idx\\\"], p[\\\"t_idx\\\"], p[\\\"r\\\"])\\n        \\n        if p[\\\"title\\\"] in title2pred:\\n            if curr in title2pred[p[\\\"title\\\"]]:\\n                title2pred[p[\\\"title\\\"]][curr] = max(p[\\\"score\\\"], title2pred[p[\\\"title\\\"]][curr])\\n            else:\\n                title2pred[p[\\\"title\\\"]][curr] = p[\\\"score\\\"]\\n        else:\\n            title2pred[p[\\\"title\\\"]] = {curr: p[\\\"score\\\"]}\\n    return title2pred\\n\\n\\ndef get_title2gt(features: dict) -> dict:\\n    '''\\n    Convert ground-truth labels to dictionary.\\n    Input:\\n        :features: list of features within each document. Identical to the lists obtained from pre-processing.\\n    Output:\\n        :title2gt: dictionary with (key, value) = (title, [gold_triples])\\n    '''\\n    title2gt = {}\\n    for f in features:\\n        title = f[\\\"title\\\"]\\n        title2gt[title] = []\\n        for idx, p in enumerate(f[\\\"hts\\\"]): \\n            h,t = p\\n            label = np.array(f['labels'][idx])\\n            rs = np.nonzero(label[1:])[0] + 1 # + 1 for no-label\\n            title2gt[title].extend([(h,t,id2rel[r]) for r in rs])\\n            \\n    return title2gt\\n\\ndef select_thresh(cand: list, num_gt: int, correct: int, num_pred: int):\\n    '''\\n    select threshold for relation predictions.\\n    Input:\\n        :cand: list of relation candidates\\n        :num_gt: number of ground-truth relations.\\n        :correct: number of correct relation predictions selected.\\n        :num_pred: number of relation predictions selected.\\n    Output:\\n        :thresh: threshold for selecting relations.\\n        :sorted_pred: predictions selected from cand. \\n    '''\\n    \\n    sorted_pred = sorted(cand, key=lambda x:x[1], reverse=True)\\n    precs, recalls = [], []\\n    \\n    for pred in sorted_pred:     \\n        correct += pred[0]\\n        num_pred += 1\\n        precs.append(correct / num_pred)  # Precision\\n        recalls.append(correct / num_gt)  # Recall                             \\n\\n    recalls = np.asarray(recalls, dtype='float32')\\n    precs = np.asarray(precs, dtype='float32')\\n    f1_arr = (2 * recalls * precs / (recalls + precs + 1e-20))\\n    f1 = f1_arr.max()\\n    f1_pos = f1_arr.argmax()\\n    thresh = sorted_pred[f1_pos][1]\\n\\n    print('Best thresh', thresh, '\\\\tbest F1', f1)\\n    return thresh, sorted_pred[:f1_pos + 1]\\n\\n\\ndef merge_results(pred: list, pred_pseudo: list, features: list, thresh: float = None):\\n    '''\\n    Merge relation predictions from the original document and psuedo documents.\\n    Input:\\n        :pred: list of dictionaries, each dictionary entry is a predicted relation triple from the original document. Keys: ['title', 'h_idx', 't_idx', 'r', 'evidence', 'score'].\\n        :pred_pseudo: list of dictionaries, each dictionary entry is a predicted relation triple from pseudo documents. Keys: ['title', 'h_idx', 't_idx', 'r', 'evidence', 'score'].\\n        :features: list of features within each document. Identical to the lists obtained from pre-processing.\\n        :thresh: threshold for selecting predictions.\\n    Output:\\n        :merged_res: list of merged relation predictions. Each relation prediction is a dictionay with keys (title, h_idx, t_idx, r).\\n        :thresh: threshold of selecting relation predictions.\\n    '''\\n    \\n    title2pred = get_title2pred(pred)\\n    title2pred_pseudo = get_title2pred(pred_pseudo)\\n\\n    title2gt = get_title2gt(features)\\n    num_gt = sum([len(title2gt[t]) for t in title2gt])\\n\\n    titl\\n\\n... [截断: 输出过长，省略 5470 字符] ...\\n\\nal evaluation code\\n    '''\\n    truth_dir = os.path.join(path, 'ref')\\n\\n    if not os.path.exists(truth_dir):\\n        os.makedirs(truth_dir)\\n\\n    fact_in_train_annotated = gen_train_facts(os.path.join(path, train_file), truth_dir)\\n    fact_in_train_distant = gen_train_facts(os.path.join(path, \\\"train_distant.json\\\"), truth_dir)\\n\\n    truth = json.load(open(os.path.join(path, dev_file)))\\n        \\n    std = {}\\n    tot_evidences = 0\\n    titleset = set([])\\n\\n    title2vectexSet = {}\\n\\n    for x in truth:\\n        title = x['title']\\n        titleset.add(title)\\n\\n        vertexSet = x['vertexSet']\\n        title2vectexSet[title] = vertexSet\\n\\n        if 'labels' not in x: # official test set from DocRED\\n            continue\\n        \\n        for label in x['labels']:\\n            r = label['r']\\n            h_idx = label['h']\\n            t_idx = label['t']\\n            std[(title, r, h_idx, t_idx)] = set(label['evidence'])\\n            tot_evidences += len(label['evidence'])\\n\\n    tot_relations = len(std)\\n    tmp.sort(key=lambda x: (x['title'], x['h_idx'], x['t_idx'], x['r']))\\n    submission_answer = [tmp[0]]\\n\\n    for i in range(1, len(tmp)):\\n        x = tmp[i]\\n        y = tmp[i - 1]\\n        if (x['title'], x['h_idx'], x['t_idx'], x['r']) != (y['title'], y['h_idx'], y['t_idx'], y['r']):\\n            submission_answer.append(tmp[i])\\n\\n    correct_re = 0\\n    correct_evidence = 0\\n    pred_evi = 0\\n\\n    correct_in_train_annotated = 0\\n    correct_in_train_distant = 0\\n    titleset2 = set([])\\n    for x in submission_answer:\\n        title = x['title']\\n        h_idx = x['h_idx']\\n        t_idx = x['t_idx']\\n        r = x['r']\\n        titleset2.add(title)\\n        if title not in title2vectexSet:\\n            continue\\n        vertexSet = title2vectexSet[title]\\n\\n        if 'evidence' in x : #and (title, h_idx, t_idx) in std:\\n            evi = set(x['evidence'])\\n        else:\\n            evi = set([])\\n        pred_evi += len(evi)\\n\\n        if (title, r, h_idx, t_idx) in std:\\n            correct_re += 1\\n            stdevi = std[(title, r, h_idx, t_idx)]\\n            correct_evidence += len(stdevi & evi)\\n            in_train_annotated = in_train_distant = False\\n            for n1 in vertexSet[h_idx]:\\n                for n2 in vertexSet[t_idx]:\\n                    if (n1['name'], n2['name'], r) in fact_in_train_annotated:\\n                        in_train_annotated = True\\n                    if (n1['name'], n2['name'], r) in fact_in_train_distant:\\n                        in_train_distant = True\\n\\n            if in_train_annotated:\\n                correct_in_train_annotated += 1\\n            if in_train_distant:\\n                correct_in_train_distant += 1\\n\\n    re_p = 1.0 * correct_re / len(submission_answer)\\n    re_r = 1.0 * correct_re / tot_relations if tot_relations != 0 else 0\\n    if re_p + re_r == 0:\\n        re_f1 = 0\\n    else:\\n        re_f1 = 2.0 * re_p * re_r / (re_p + re_r)\\n\\n    evi_p = 1.0 * correct_evidence / pred_evi if pred_evi > 0 else 0\\n    evi_r = 1.0 * correct_evidence / tot_evidences if tot_evidences > 0 else 0\\n\\n    if evi_p + evi_r == 0:\\n        evi_f1 = 0\\n    else:\\n        evi_f1 = 2.0 * evi_p * evi_r / (evi_p + evi_r)\\n\\n    re_p_ignore_train_annotated = 1.0 * (correct_re - correct_in_train_annotated) / (len(submission_answer) - correct_in_train_annotated + 1e-5)\\n    re_p_ignore_train = 1.0 * (correct_re - correct_in_train_distant) / (len(submission_answer) - correct_in_train_distant + 1e-5)\\n\\n    if re_p_ignore_train_annotated + re_r == 0:\\n        re_f1_ignore_train_annotated = 0\\n    else:\\n        re_f1_ignore_train_annotated = 2.0 * re_p_ignore_train_annotated * re_r / (re_p_ignore_train_annotated + re_r)\\n\\n    if re_p_ignore_train + re_r == 0:\\n        re_f1_ignore_train = 0\\n    else:\\n        re_f1_ignore_train = 2.0 * re_p_ignore_train * re_r / (re_p_ignore_train + re_r)\\n\\n    return [re_p, re_r, re_f1], [evi_p, evi_r, evi_f1],\\\\\\n        [re_p_ignore_train_annotated, re_r, re_f1_ignore_train_annotated], \\\\\\n        [re_p_ignore_train, re_r, re_f1_ignore_train]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

````text
Now I have both codebases. Let me carefully analyze the differences.

## DREEAM's Evi-F1 calculation (from `official_evaluate`):

```python
# Gold: for each (title, r, h_idx, t_idx), store set of evidence sentence indices
std[(title, r, h_idx, t_idx)] = set(label['evidence'])
tot_evidences += len(label['evidence'])  # total gold evidence sentences across ALL triples

# For predictions:
for x in submission_answer:


```

Calculating evidence metrics...

For each predicted triple, I'm checking if it was correctly predicted, and if so, counting the overlap between predicted and gold evidence sentences. Then I'm computing precision as correct evidence divided by all predicted evidence (including from wrong triples), recall as correct evidence divided by all gold evidence, and finally the F1 score from those two metrics. I need to look at the full `compute_evi_f1` method since the output got cut off earlier.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "87cf1bae-ea06-4346-8715-96bd4e98b587",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mcgmypd6RdvwLR3hYJ4g8X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6884,
      "cache_read_input_tokens": 27551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6884
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 18_

输出被截断了，需要完整读取 `compute_evi_f1` 方法。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "3f89fa6c-0862-4f61-9c60-f6f668304678",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mcgmypd6RdvwLR3hYJ4g8X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6884,
      "cache_read_input_tokens": 27551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6884
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01G9DcmUitRqB59GYiSNetzJ`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -n \"def compute_evi\" /root/autodl-tmp/freige/eval/evaluator.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "5223f888-e10d-4ca6-b6da-a1e7462871a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mcgmypd6RdvwLR3hYJ4g8X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6884,
      "cache_read_input_tokens": 27551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6884
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 20 · 2026-05-17T12:55:22.806Z_

<details><summary>↩ Tool result · `toolu_01G9DcmUitRqB59GYiSNetzJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"107:    def compute_evi_f1(\\n152:    def compute_evi_f1_joint(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "f027b3b3-2f5c-4eab-9f90-1e09e94fde29",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"107:    def compute_evi_f1(\\\\n152:    def compute_evi_f1_joint(\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.33}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"107:    def compute_evi_f1(\\n152:    def compute_evi_f1_joint(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.33}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Rk5J6eHoW1iHLpJXWSjAEA`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "head -250 /root/autodl-tmp/freige/eval/evaluator.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "9b7dceba-a194-4602-9bd5-fe408caaed6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UqnuMWhF8TfjRYLy4U2nqR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 852,
      "cache_read_input_tokens": 34435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 852
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 22 · 2026-05-17T12:55:25.185Z_

<details><summary>↩ Tool result · `toolu_01Rk5J6eHoW1iHLpJXWSjAEA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"DocRED 关系抽取评测模块。\\n\\n指标:\\n  - F1 / Ign-F1: 关系三元组级别 micro-F1，Ign-F1 排除训练集中出现的三元组\\n  - Evi-F1: 对正确预测的三元组，计算 evidence 句子级 F1\\n  - EDCR: Evidence Distractor Citation Rate，预测 evidence 中非 gold 的比例\\n\\n输入: 预测列表 + gold 标注列表（每个元素为文档级标注）\\n输出: 指标字典\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nfrom collections import defaultdict\\nfrom typing import Optional\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef _triple_key(doc_id: str, head: str, tail: str, relation: str) -> tuple:\\n    return (doc_id, head.lower().strip(), tail.lower().strip(), relation.lower().strip())\\n\\n\\nclass DocREDEvaluator:\\n    \\\"\\\"\\\"DocRED 评测器。\\n\\n    Args:\\n        train_triples: 训练集中的三元组集合，用于计算 Ign-F1。\\n                       每个元素为 (doc_title, head_name, tail_name, relation)。\\n                       为 None 时 Ign-F1 = F1。\\n    \\\"\\\"\\\"\\n\\n    def __init__(self, train_triples: Optional[set[tuple]] = None, train_facts: Optional[set[tuple]] = None):\\n        self.train_triples = train_triples or set()\\n        self.train_facts = train_facts or set()\\n\\n    @classmethod\\n    def from_train_file(cls, train_path: str) -> \\\"DocREDEvaluator\\\":\\n        \\\"\\\"\\\"从训练集 JSON 文件构建 evaluator，自动提取训练集三元组。\\\"\\\"\\\"\\n        from freige.data.docred_processor import DOCRED_REL_INFO\\n\\n        with open(train_path) as f:\\n            train_data = json.load(f)\\n\\n        train_triples = set()\\n        train_facts = set()\\n        for doc in train_data:\\n            doc_id = doc.get(\\\"title\\\", \\\"\\\")\\n            vertex_set = doc[\\\"vertexSet\\\"]\\n            for label in doc.get(\\\"labels\\\", []):\\n                h_name = vertex_set[label[\\\"h\\\"]][0][\\\"name\\\"]\\n                t_name = vertex_set[label[\\\"t\\\"]][0][\\\"name\\\"]\\n                rel_name = DOCRED_REL_INFO.get(label[\\\"r\\\"], label[\\\"r\\\"])\\n                train_triples.add(\\n                    _triple_key(doc_id, h_name, t_name, rel_name)\\n                )\\n                train_facts.add((h_name.lower().strip(), t_name.lower().strip(), rel_name.lower().strip()))\\n\\n        logger.info(\\\"Loaded %d training triples (%d unique facts) for Ign-F1\\\", len(train_triples), len(train_facts))\\n        return cls(train_triples=train_triples, train_facts=train_facts)\\n\\n    def compute_f1(\\n        self,\\n        predictions: list[dict],\\n        gold: list[dict],\\n    ) -> dict:\\n        \\\"\\\"\\\"计算 F1 和 Ign-F1。\\\"\\\"\\\"\\n        pred_set = set()\\n        for p in predictions:\\n            pred_set.add(_triple_key(\\n                p[\\\"doc_id\\\"], p[\\\"head\\\"], p[\\\"tail\\\"], p[\\\"relation\\\"]\\n            ))\\n\\n        gold_set = set()\\n        for g in gold:\\n            gold_set.add(_triple_key(\\n                g[\\\"doc_id\\\"], g[\\\"head\\\"], g[\\\"tail\\\"], g[\\\"relation\\\"]\\n            ))\\n\\n        tp = pred_set & gold_set\\n        precision = len(tp) / len(pred_set) if pred_set else 0.0\\n        recall = len(tp) / len(gold_set) if gold_set else 0.0\\n        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0\\n\\n        pred_ign = {k for k in pred_set if k[1:] not in self.train_facts}\\n        gold_ign = {k for k in gold_set if k[1:] not in self.train_facts}\\n        tp_ign = pred_ign & gold_ign\\n        ign_prec = len(tp_ign) / len(pred_ign) if pred_ign else 0.0\\n        ign_rec = len(tp_ign) / len(gold_ign) if gold_ign else 0.0\\n        ign_f1 = (\\n            2 * ign_prec * ign_rec / (ign_prec + ign_rec)\\n            if (ign_prec + ign_rec) > 0 else 0.0\\n        )\\n\\n        return {\\n            \\\"precision\\\": precision,\\n            \\\"recall\\\": recall,\\n            \\\"f1\\\": f1,\\n            \\\"ign_precision\\\": ign_prec,\\n            \\\"ign_recall\\\": ign_rec,\\n            \\\"ign_f1\\\": ign_f1,\\n            \\\"tp\\\": len(tp),\\n            \\\"pred_count\\\": len(pred_set),\\n            \\\"gold_count\\\": len(gold_set),\\n        }\\n\\n    def compute_evi_f1(\\n        self,\\n        predictions: list[dict],\\n        gold: list[dict],\\n    ) -> dict:\\n        \\\"\\\"\\\"计�� Evidence F1（句子级）。\\\"\\\"\\\"\\n        gold_map = {}\\n        for g in gold:\\n            key = _triple_key(g[\\\"doc_id\\\"], g[\\\"head\\\"], g[\\\"tail\\\"], g[\\\"relation\\\"])\\n            gold_map.setdefault(key, set()).update(g.get(\\\"evidence\\\", []))\\n\\n        total_tp = 0\\n        total_pred = 0\\n      \\n\\n... [截断: 输出过长，省略 180 字符] ...\\n\\nld_map:\\n                continue\\n\\n            pred_evi = set(p.get(\\\"evidence\\\", []))\\n            gold_evi = gold_map[key]\\n\\n            tp = len(pred_evi & gold_evi)\\n            total_tp += tp\\n            total_pred += len(pred_evi)\\n            total_gold += len(gold_evi)\\n            n_evaluated += 1\\n\\n        evi_prec = total_tp / total_pred if total_pred else 0.0\\n        evi_rec = total_tp / total_gold if total_gold else 0.0\\n        evi_f1 = (\\n            2 * evi_prec * evi_rec / (evi_prec + evi_rec)\\n            if (evi_prec + evi_rec) > 0 else 0.0\\n        )\\n\\n        return {\\n            \\\"evi_precision\\\": evi_prec,\\n            \\\"evi_recall\\\": evi_rec,\\n            \\\"evi_f1\\\": evi_f1,\\n            \\\"n_evaluated\\\": n_evaluated,\\n        }\\n\\n\\n    def compute_evi_f1_joint(\\n        self,\\n        predictions: list[dict],\\n        gold: list[dict],\\n    ) -> dict:\\n        \\\"\\\"\\\"Evidence F1 (joint) — DREEAM 协议对齐版本。\\n\\n        与 compute_evi_f1 的区别：FP triple 的 evidence 计入 precision 分母，\\n        FN triple 的 evidence 计入 recall 分母，而非仅在 TP triple 上计算。\\n        \\\"\\\"\\\"\\n        gold_map = {}\\n        for g in gold:\\n            key = _triple_key(g[\\\"doc_id\\\"], g[\\\"head\\\"], g[\\\"tail\\\"], g[\\\"relation\\\"])\\n            gold_map.setdefault(key, set()).update(g.get(\\\"evidence\\\", []))\\n\\n        pred_map = {}\\n        for p in predictions:\\n            key = _triple_key(p[\\\"doc_id\\\"], p[\\\"head\\\"], p[\\\"tail\\\"], p[\\\"relation\\\"])\\n            pred_map.setdefault(key, set()).update(p.get(\\\"evidence\\\", []))\\n\\n        evi_tp = 0\\n        evi_pred_total = 0\\n\\n        for key, pred_evi in pred_map.items():\\n            evi_pred_total += len(pred_evi)\\n            if key in gold_map:\\n                evi_tp += len(pred_evi & gold_map[key])\\n\\n        evi_gold_total = sum(len(evi) for evi in gold_map.values())\\n\\n        evi_prec = evi_tp / evi_pred_total if evi_pred_total else 0.0\\n        evi_rec = evi_tp / evi_gold_total if evi_gold_total else 0.0\\n        evi_f1 = (\\n            2 * evi_prec * evi_rec / (evi_prec + evi_rec)\\n            if (evi_prec + evi_rec) > 0 else 0.0\\n        )\\n\\n        return {\\n            \\\"evi_joint_precision\\\": evi_prec,\\n            \\\"evi_joint_recall\\\": evi_rec,\\n            \\\"evi_f1_joint\\\": evi_f1,\\n            \\\"evi_tp\\\": evi_tp,\\n            \\\"evi_pred_total\\\": evi_pred_total,\\n            \\\"evi_gold_total\\\": evi_gold_total,\\n        }\\n\\n    def compute_edcr(\\n        self,\\n        predictions: list[dict],\\n        gold: list[dict],\\n    ) -> dict:\\n        \\\"\\\"\\\"计算 EDCR（Evidence Distractor Citation Rate）���\\\"\\\"\\\"\\n        gold_map = {}\\n        for g in gold:\\n            key = _triple_key(g[\\\"doc_id\\\"], g[\\\"head\\\"], g[\\\"tail\\\"], g[\\\"relation\\\"])\\n            gold_map.setdefault(key, set()).update(g.get(\\\"evidence\\\", []))\\n\\n        n_distractor = 0\\n        n_total = 0\\n        n_evaluated = 0\\n\\n        for p in predictions:\\n            pred_evi = set(p.get(\\\"evidence\\\", []))\\n            if not pred_evi:\\n                continue\\n\\n            key = _triple_key(p[\\\"doc_id\\\"], p[\\\"head\\\"], p[\\\"tail\\\"], p[\\\"relation\\\"])\\n            gold_evi = gold_map.get(key, set())\\n\\n            distractors = pred_evi - gold_evi\\n            n_distractor += len(distractors)\\n            n_total += len(pred_evi)\\n            n_evaluated += 1\\n\\n        edcr = n_distractor / n_total if n_total else 0.0\\n\\n        return {\\n            \\\"edcr\\\": edcr,\\n            \\\"n_distractor_citations\\\": n_distractor,\\n            \\\"n_total_citations\\\": n_total,\\n            \\\"n_evaluated\\\": n_evaluated,\\n        }\\n\\n    def compute_format_compliance(self, raw_outputs: list[dict]) -> dict:\\n        \\\"\\\"\\\"计算模型输出的格式合规率。\\\"\\\"\\\"\\n        required_fields = {\\\"head\\\", \\\"relation\\\", \\\"tail\\\", \\\"evidence\\\"}\\n        n_total = len(raw_outputs)\\n        n_parseable = 0\\n        n_field_complete = 0\\n        n_evidence_valid = 0\\n\\n        for item in raw_outputs:\\n            doc_id = item.get(\\\"doc_id\\\", \\\"\\\")\\n            raw_text = item.get(\\\"raw_text\\\", \\\"\\\")\\n\\n            parsed, _ = parse_model_output(raw_text)\\n            if not parsed and not self._is_parseable_json_list(raw_text):\\n                continue\\n            n_parseable += 1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "feea556a-3376-4104-aae1-348b1715bbc0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"DocRED 关系抽取评测模块。\\\\n\\\\n指标:\\\\n  - F1 / Ign-F1: 关系三元组级别 micro-F1，Ign-F1 排除训练集中出现的三元组\\\\n  - Evi-F1: 对正确预测的三元组，计算 evidence 句子级 F1\\\\n  - EDCR: Evidence Distractor Citation Rate，预测 evidence 中非 gold 的比例\\\\n\\\\n输入: 预测列表 + gold 标注列表（每个元素为文档级标注）\\\\n输出: 指标字典\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport json\\\\nimport logging\\\\nfrom collections import defaultdict\\\\nfrom typing import Optional\\\\n\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\n\\\\ndef _triple_key(doc_id: str, head: str, tail: str, relation: str) -> tuple:\\\\n    return (doc_id, head.lower().strip(), tail.lower().strip(), relation.lower().strip())\\\\n\\\\n\\\\nclass DocREDEvaluator:\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"DocRED 评测器。\\\\n\\\\n    Args:\\\\n        train_triples: 训练集中的三元组集合，用于计算 Ign-F1。\\\\n                       每个元素为 (doc_title, head_name, tail_name, relation)。\\\\n                       为 None 时 Ign-F1 = F1。\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\n    def __init__(self, train_triples: Optional[set[tuple]] = None, train_facts: Optional[set[tuple]] = None):\\\\n        self.train_triples = train_triples or set()\\\\n        self.train_facts = train_facts or set()\\\\n\\\\n    @classmethod\\\\n    def from_train_file(cls, train_path: str) -> \\\\\\\"DocREDEvaluator\\\\\\\":\\\\n        \\\\\\\"\\\\\\\"\\\\\\\"从训练集 JSON 文件构建 evaluator，自动提取训练集三元组。\\\\\\\"\\\\\\\"\\\\\\\"\\\\n        from freige.data.docred_processor import DOCRED_REL_INFO\\\\n\\\\n        with open(train_path) as f:\\\\n            train_data = json.load(f)\\\\n\\\\n        train_triples = set()\\\\n        train_facts = set()\\\\n        for doc in train_data:\\\\n            doc_id = doc.get(\\\\\\\"title\\\\\\\", \\\\\\\"\\\\\\\")\\\\n            vertex_set = doc[\\\\\\\"vertexSet\\\\\\\"]\\\\n            for label in doc.get(\\\\\\\"labels\\\\\\\", []):\\\\n                h_name = vertex_set[label[\\\\\\\"h\\\\\\\"]][0][\\\\\\\"name\\\\\\\"]\\\\n                t_name = vertex_set[label[\\\\\\\"t\\\\\\\"]][0][\\\\\\\"name\\\\\\\"]\\\\n                rel_name = DOCRED_REL_INFO.get(label[\\\\\\\"r\\\\\\\"], label[\\\\\\\"r\\\\\\\"])\\\\n                train_triples.add(\\\\n                    _triple_key(doc_id, h_name, t_name, rel_name)\\\\n                )\\\\n                train_facts.add((h_name.lower().strip(), t_name.lower().strip(), rel_name.lower().strip()))\\\\n\\\\n        logger.info(\\\\\\\"Loaded %d training triples (%d unique facts) for Ign-F1\\\\\\\", len(train_triples), len(train_facts))\\\\n        return cls(train_triples=train_triples, train_facts=train_facts)\\\\n\\\\n    def compute_f1(\\\\n        self,\\\\n        predictions: list[dict],\\\\n        gold: list[dict],\\\\n    ) -> dict:\\\\n        \\\\\\\"\\\\\\\"\\\\\\\"计算 F1 和 Ign-F1。\\\\\\\"\\\\\\\"\\\\\\\"\\\\n        pred_set = set()\\\\n        for p in predictions:\\\\n            pred_set.add(_triple_key(\\\\n                p[\\\\\\\"doc_id\\\\\\\"], p[\\\\\\\"head\\\\\\\"], p[\\\\\\\"tail\\\\\\\"], p[\\\\\\\"relation\\\\\\\"]\\\\n            ))\\\\n\\\\n        gold_set = set()\\\\n        for g in gold:\\\\n            gold_set.add(_triple_key(\\\\n                g[\\\\\\\"doc_id\\\\\\\"], g[\\\\\\\"head\\\\\\\"], g[\\\\\\\"tail\\\\\\\"], g[\\\\\\\"relation\\\\\\\"]\\\\n            ))\\\\n\\\\n        tp = pred_set & gold_set\\\\n        precision = len(tp) / len(pred_set) if pred_set else 0.0\\\\n        recall = len(tp) / len(gold_set) if gold_set else 0.0\\\\n        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0\\\\n\\\\n        pred_ign = {k for k in pred_set if k[1:] not in self.train_facts}\\\\n        gold_ign = {k for k in gold_set if k[1:] not in self.train_facts}\\\\n        tp_ign = pred_ign & gold_ign\\\\n        ign_prec = len(tp_ign) / len(pred_ign) if pred_ign else 0.0\\\\n        ign_rec = len(tp_ign) / len(gold_ign) if gold_ign else 0.0\\\\n        ign_f1 = (\\\\n            2 * ign_prec * ign_rec / (ign_prec + ign_rec)\\\\n            if (ign_prec + ign_rec) > 0 else 0.0\\\\n        )\\\\n\\\\n        return {\\\\n            \\\\\\\"precision\\\\\\\": precision,\\\\n            \\\\\\\"recall\\\\\\\": recall,\\\\n            \\\\\\\"f1\\\\\\\": f1,\\\\n            \\\\\\\"ign_precision\\\\\\\": ign_prec,\\\\n            \\\\\\\"ign_recall\\\\\\\": ign_rec,\\\\n            \\\\\\\"ign_f1\\\\\\\": ign_f1,\\\\n            \\\\\\\"tp\\\\\\\": len(tp),\\\\n            \\\\\\\"pred_count\\\\\\\": len(pred_set),\\\\n            \\\\\\\"gold_count\\\\\\\": len(gold_set),\\\\n        }\\\\n\\\\n    def compute_evi_f1(\\\\n        self,\\\\n        predictions: list[dict],\\\\n        gold: list[dict],\\\\n    ) -> dict:\\\\n        \\\\\\\"\\\\\\\"\\\\\\\"计�� Evidence F1（句子级）。\\\\\\\"\\\\\\\"\\\\\\\"\\\\n        gold_map = {}\\\\n        for g in gold:\\\\n            key = _triple_key(g[\\\\\\\"doc_id\\\\\\\"], g[\\\\\\\"head\\\\\\\"], g[\\\\\\\"tail\\\\\\\"], g[\\\\\\\"relation\\\\\\\"])\\\\n            gold_map.setdefault(key, set()).update(g.get(\\\\\\\"evidence\\\\\\\", []))\\\\n\\\\n        total_tp = 0\\\\n        total_pred = 0\\\\n      \\\\n\\\\n... [截断: 输出过长，省略 180 字符] ...\\\\n\\\\nld_map:\\\\n                continue\\\\n\\\\n            pred_evi = set(p.get(\\\\\\\"evidence\\\\\\\", []))\\\\n            gold_evi = gold_map[key]\\\\n\\\\n            tp = len(pred_evi & gold_evi)\\\\n            total_tp += tp\\\\n            total_pred += len(pred_evi)\\\\n            total_gold += len(gold_evi)\\\\n            n_evaluated += 1\\\\n\\\\n        evi_prec = total_tp / total_pred if total_pred else 0.0\\\\n        evi_rec = total_tp / total_gold if total_gold else 0.0\\\\n        evi_f1 = (\\\\n            2 * evi_prec * evi_rec / (evi_prec + evi_rec)\\\\n            if (evi_prec + evi_rec) > 0 else 0.0\\\\n        )\\\\n\\\\n        return {\\\\n            \\\\\\\"evi_precision\\\\\\\": evi_prec,\\\\n            \\\\\\\"evi_recall\\\\\\\": evi_rec,\\\\n            \\\\\\\"evi_f1\\\\\\\": evi_f1,\\\\n            \\\\\\\"n_evaluated\\\\\\\": n_evaluated,\\\\n        }\\\\n\\\\n\\\\n    def compute_evi_f1_joint(\\\\n        self,\\\\n        predictions: list[dict],\\\\n        gold: list[dict],\\\\n    ) -> dict:\\\\n        \\\\\\\"\\\\\\\"\\\\\\\"Evidence F1 (joint) — DREEAM 协议对齐版本。\\\\n\\\\n        与 compute_evi_f1 的区别：FP triple 的 evidence 计入 precision 分母，\\\\n        FN triple 的 evidence 计入 recall 分母，而非仅在 TP triple 上计算。\\\\n        \\\\\\\"\\\\\\\"\\\\\\\"\\\\n        gold_map = {}\\\\n        for g in gold:\\\\n            key = _triple_key(g[\\\\\\\"doc_id\\\\\\\"], g[\\\\\\\"head\\\\\\\"], g[\\\\\\\"tail\\\\\\\"], g[\\\\\\\"relation\\\\\\\"])\\\\n            gold_map.setdefault(key, set()).update(g.get(\\\\\\\"evidence\\\\\\\", []))\\\\n\\\\n        pred_map = {}\\\\n        for p in predictions:\\\\n            key = _triple_key(p[\\\\\\\"doc_id\\\\\\\"], p[\\\\\\\"head\\\\\\\"], p[\\\\\\\"tail\\\\\\\"], p[\\\\\\\"relation\\\\\\\"])\\\\n            pred_map.setdefault(key, set()).update(p.get(\\\\\\\"evidence\\\\\\\", []))\\\\n\\\\n        evi_tp = 0\\\\n        evi_pred_total = 0\\\\n\\\\n        for key, pred_evi in pred_map.items():\\\\n            evi_pred_total += len(pred_evi)\\\\n            if key in gold_map:\\\\n                evi_tp += len(pred_evi & gold_map[key])\\\\n\\\\n        evi_gold_total = sum(len(evi) for evi in gold_map.values())\\\\n\\\\n        evi_prec = evi_tp / evi_pred_total if evi_pred_total else 0.0\\\\n        evi_rec = evi_tp / evi_gold_total if evi_gold_total else 0.0\\\\n        evi_f1 = (\\\\n            2 * evi_prec * evi_rec / (evi_prec + evi_rec)\\\\n            if (evi_prec + evi_rec) > 0 else 0.0\\\\n        )\\\\n\\\\n        return {\\\\n            \\\\\\\"evi_joint_precision\\\\\\\": evi_prec,\\\\n            \\\\\\\"evi_joint_recall\\\\\\\": evi_rec,\\\\n            \\\\\\\"evi_f1_joint\\\\\\\": evi_f1,\\\\n            \\\\\\\"evi_tp\\\\\\\": evi_tp,\\\\n            \\\\\\\"evi_pred_total\\\\\\\": evi_pred_total,\\\\n            \\\\\\\"evi_gold_total\\\\\\\": evi_gold_total,\\\\n        }\\\\n\\\\n    def compute_edcr(\\\\n        self,\\\\n        predictions: list[dict],\\\\n        gold: list[dict],\\\\n    ) -> dict:\\\\n        \\\\\\\"\\\\\\\"\\\\\\\"计算 EDCR（Evidence Distractor Citation Rate）���\\\\\\\"\\\\\\\"\\\\\\\"\\\\n        gold_map = {}\\\\n        for g in gold:\\\\n            key = _triple_key(g[\\\\\\\"doc_id\\\\\\\"], g[\\\\\\\"head\\\\\\\"], g[\\\\\\\"tail\\\\\\\"], g[\\\\\\\"relation\\\\\\\"])\\\\n            gold_map.setdefault(key, set()).update(g.get(\\\\\\\"evidence\\\\\\\", []))\\\\n\\\\n        n_distractor = 0\\\\n        n_total = 0\\\\n        n_evaluated = 0\\\\n\\\\n        for p in predictions:\\\\n            pred_evi = set(p.get(\\\\\\\"evidence\\\\\\\", []))\\\\n            if not pred_evi:\\\\n                continue\\\\n\\\\n            key = _triple_key(p[\\\\\\\"doc_id\\\\\\\"], p[\\\\\\\"head\\\\\\\"], p[\\\\\\\"tail\\\\\\\"], p[\\\\\\\"relation\\\\\\\"])\\\\n            gold_evi = gold_map.get(key, set())\\\\n\\\\n            distractors = pred_evi - gold_evi\\\\n            n_distractor += len(distractors)\\\\n            n_total += len(pred_evi)\\\\n            n_evaluated += 1\\\\n\\\\n        edcr = n_distractor / n_total if n_total else 0.0\\\\n\\\\n        return {\\\\n            \\\\\\\"edcr\\\\\\\": edcr,\\\\n            \\\\\\\"n_distractor_citations\\\\\\\": n_distractor,\\\\n            \\\\\\\"n_total_citations\\\\\\\": n_total,\\\\n            \\\\\\\"n_evaluated\\\\\\\": n_evaluated,\\\\n        }\\\\n\\\\n    def compute_format_compliance(self, raw_outputs: list[dict]) -> dict:\\\\n        \\\\\\\"\\\\\\\"\\\\\\\"计算模型输出的格式合规率。\\\\\\\"\\\\\\\"\\\\\\\"\\\\n        required_fields = {\\\\\\\"head\\\\\\\", \\\\\\\"relation\\\\\\\", \\\\\\\"tail\\\\\\\", \\\\\\\"evidence\\\\\\\"}\\\\n        n_total = len(raw_outputs)\\\\n        n_parseable = 0\\\\n        n_field_complete = 0\\\\n        n_evidence_valid = 0\\\\n\\\\n        for item in raw_outputs:\\\\n            doc_id = item.get(\\\\\\\"doc_id\\\\\\\", \\\\\\\"\\\\\\\")\\\\n            raw_text = item.get(\\\\\\\"raw_text\\\\\\\", \\\\\\\"\\\\\\\")\\\\n\\\\n            parsed, _ = parse_model_output(raw_text)\\\\n            if not parsed and not self._is_parseable_json_list(raw_text):\\\\n                continue\\\\n            n_parseable += 1\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.34}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"DocRED 关系抽取评测模块。\\n\\n指标:\\n  - F1 / Ign-F1: 关系三元组级别 micro-F1，Ign-F1 排除训练集中出现的三元组\\n  - Evi-F1: 对正确预测的三元组，计算 evidence 句子级 F1\\n  - EDCR: Evidence Distractor Citation Rate，预测 evidence 中非 gold 的比例\\n\\n输入: 预测列表 + gold 标注列表（每个元素为文档级标注）\\n输出: 指标字典\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nfrom collections import defaultdict\\nfrom typing import Optional\\n\\nlogger = logging.getLogger(__name__)\\n\\n\\ndef _triple_key(doc_id: str, head: str, tail: str, relation: str) -> tuple:\\n    return (doc_id, head.lower().strip(), tail.lower().strip(), relation.lower().strip())\\n\\n\\nclass DocREDEvaluator:\\n    \\\"\\\"\\\"DocRED 评测器。\\n\\n    Args:\\n        train_triples: 训练集中的三元组集合，用于计算 Ign-F1。\\n                       每个元素为 (doc_title, head_name, tail_name, relation)。\\n                       为 None 时 Ign-F1 = F1。\\n    \\\"\\\"\\\"\\n\\n    def __init__(self, train_triples: Optional[set[tuple]] = None, train_facts: Optional[set[tuple]] = None):\\n        self.train_triples = train_triples or set()\\n        self.train_facts = train_facts or set()\\n\\n    @classmethod\\n    def from_train_file(cls, train_path: str) -> \\\"DocREDEvaluator\\\":\\n        \\\"\\\"\\\"从训练集 JSON 文件构建 evaluator，自动提取训练集三元组。\\\"\\\"\\\"\\n        from freige.data.docred_processor import DOCRED_REL_INFO\\n\\n        with open(train_path) as f:\\n            train_data = json.load(f)\\n\\n        train_triples = set()\\n        train_facts = set()\\n        for doc in train_data:\\n            doc_id = doc.get(\\\"title\\\", \\\"\\\")\\n            vertex_set = doc[\\\"vertexSet\\\"]\\n            for label in doc.get(\\\"labels\\\", []):\\n                h_name = vertex_set[label[\\\"h\\\"]][0][\\\"name\\\"]\\n                t_name = vertex_set[label[\\\"t\\\"]][0][\\\"name\\\"]\\n                rel_name = DOCRED_REL_INFO.get(label[\\\"r\\\"], label[\\\"r\\\"])\\n                train_triples.add(\\n                    _triple_key(doc_id, h_name, t_name, rel_name)\\n                )\\n                train_facts.add((h_name.lower().strip(), t_name.lower().strip(), rel_name.lower().strip()))\\n\\n        logger.info(\\\"Loaded %d training triples (%d unique facts) for Ign-F1\\\", len(train_triples), len(train_facts))\\n        return cls(train_triples=train_triples, train_facts=train_facts)\\n\\n    def compute_f1(\\n        self,\\n        predictions: list[dict],\\n        gold: list[dict],\\n    ) -> dict:\\n        \\\"\\\"\\\"计算 F1 和 Ign-F1。\\\"\\\"\\\"\\n        pred_set = set()\\n        for p in predictions:\\n            pred_set.add(_triple_key(\\n                p[\\\"doc_id\\\"], p[\\\"head\\\"], p[\\\"tail\\\"], p[\\\"relation\\\"]\\n            ))\\n\\n        gold_set = set()\\n        for g in gold:\\n            gold_set.add(_triple_key(\\n                g[\\\"doc_id\\\"], g[\\\"head\\\"], g[\\\"tail\\\"], g[\\\"relation\\\"]\\n            ))\\n\\n        tp = pred_set & gold_set\\n        precision = len(tp) / len(pred_set) if pred_set else 0.0\\n        recall = len(tp) / len(gold_set) if gold_set else 0.0\\n        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0\\n\\n        pred_ign = {k for k in pred_set if k[1:] not in self.train_facts}\\n        gold_ign = {k for k in gold_set if k[1:] not in self.train_facts}\\n        tp_ign = pred_ign & gold_ign\\n        ign_prec = len(tp_ign) / len(pred_ign) if pred_ign else 0.0\\n        ign_rec = len(tp_ign) / len(gold_ign) if gold_ign else 0.0\\n        ign_f1 = (\\n            2 * ign_prec * ign_rec / (ign_prec + ign_rec)\\n            if (ign_prec + ign_rec) > 0 else 0.0\\n        )\\n\\n        return {\\n            \\\"precision\\\": precision,\\n            \\\"recall\\\": recall,\\n            \\\"f1\\\": f1,\\n            \\\"ign_precision\\\": ign_prec,\\n            \\\"ign_recall\\\": ign_rec,\\n            \\\"ign_f1\\\": ign_f1,\\n            \\\"tp\\\": len(tp),\\n            \\\"pred_count\\\": len(pred_set),\\n            \\\"gold_count\\\": len(gold_set),\\n        }\\n\\n    def compute_evi_f1(\\n        self,\\n        predictions: list[dict],\\n        gold: list[dict],\\n    ) -> dict:\\n        \\\"\\\"\\\"计�� Evidence F1（句子级）。\\\"\\\"\\\"\\n        gold_map = {}\\n        for g in gold:\\n            key = _triple_key(g[\\\"doc_id\\\"], g[\\\"head\\\"], g[\\\"tail\\\"], g[\\\"relation\\\"])\\n            gold_map.setdefault(key, set()).update(g.get(\\\"evidence\\\", []))\\n\\n        total_tp = 0\\n        total_pred = 0\\n      \\n\\n... [截断: 输出过长，省略 180 字符] ...\\n\\nld_map:\\n                continue\\n\\n            pred_evi = set(p.get(\\\"evidence\\\", []))\\n            gold_evi = gold_map[key]\\n\\n            tp = len(pred_evi & gold_evi)\\n            total_tp += tp\\n            total_pred += len(pred_evi)\\n            total_gold += len(gold_evi)\\n            n_evaluated += 1\\n\\n        evi_prec = total_tp / total_pred if total_pred else 0.0\\n        evi_rec = total_tp / total_gold if total_gold else 0.0\\n        evi_f1 = (\\n            2 * evi_prec * evi_rec / (evi_prec + evi_rec)\\n            if (evi_prec + evi_rec) > 0 else 0.0\\n        )\\n\\n        return {\\n            \\\"evi_precision\\\": evi_prec,\\n            \\\"evi_recall\\\": evi_rec,\\n            \\\"evi_f1\\\": evi_f1,\\n            \\\"n_evaluated\\\": n_evaluated,\\n        }\\n\\n\\n    def compute_evi_f1_joint(\\n        self,\\n        predictions: list[dict],\\n        gold: list[dict],\\n    ) -> dict:\\n        \\\"\\\"\\\"Evidence F1 (joint) — DREEAM 协议对齐版本。\\n\\n        与 compute_evi_f1 的区别：FP triple 的 evidence 计入 precision 分母，\\n        FN triple 的 evidence 计入 recall 分母，而非仅在 TP triple 上计算。\\n        \\\"\\\"\\\"\\n        gold_map = {}\\n        for g in gold:\\n            key = _triple_key(g[\\\"doc_id\\\"], g[\\\"head\\\"], g[\\\"tail\\\"], g[\\\"relation\\\"])\\n            gold_map.setdefault(key, set()).update(g.get(\\\"evidence\\\", []))\\n\\n        pred_map = {}\\n        for p in predictions:\\n            key = _triple_key(p[\\\"doc_id\\\"], p[\\\"head\\\"], p[\\\"tail\\\"], p[\\\"relation\\\"])\\n            pred_map.setdefault(key, set()).update(p.get(\\\"evidence\\\", []))\\n\\n        evi_tp = 0\\n        evi_pred_total = 0\\n\\n        for key, pred_evi in pred_map.items():\\n            evi_pred_total += len(pred_evi)\\n            if key in gold_map:\\n                evi_tp += len(pred_evi & gold_map[key])\\n\\n        evi_gold_total = sum(len(evi) for evi in gold_map.values())\\n\\n        evi_prec = evi_tp / evi_pred_total if evi_pred_total else 0.0\\n        evi_rec = evi_tp / evi_gold_total if evi_gold_total else 0.0\\n        evi_f1 = (\\n            2 * evi_prec * evi_rec / (evi_prec + evi_rec)\\n            if (evi_prec + evi_rec) > 0 else 0.0\\n        )\\n\\n        return {\\n            \\\"evi_joint_precision\\\": evi_prec,\\n            \\\"evi_joint_recall\\\": evi_rec,\\n            \\\"evi_f1_joint\\\": evi_f1,\\n            \\\"evi_tp\\\": evi_tp,\\n            \\\"evi_pred_total\\\": evi_pred_total,\\n            \\\"evi_gold_total\\\": evi_gold_total,\\n        }\\n\\n    def compute_edcr(\\n        self,\\n        predictions: list[dict],\\n        gold: list[dict],\\n    ) -> dict:\\n        \\\"\\\"\\\"计算 EDCR（Evidence Distractor Citation Rate）���\\\"\\\"\\\"\\n        gold_map = {}\\n        for g in gold:\\n            key = _triple_key(g[\\\"doc_id\\\"], g[\\\"head\\\"], g[\\\"tail\\\"], g[\\\"relation\\\"])\\n            gold_map.setdefault(key, set()).update(g.get(\\\"evidence\\\", []))\\n\\n        n_distractor = 0\\n        n_total = 0\\n        n_evaluated = 0\\n\\n        for p in predictions:\\n            pred_evi = set(p.get(\\\"evidence\\\", []))\\n            if not pred_evi:\\n                continue\\n\\n            key = _triple_key(p[\\\"doc_id\\\"], p[\\\"head\\\"], p[\\\"tail\\\"], p[\\\"relation\\\"])\\n            gold_evi = gold_map.get(key, set())\\n\\n            distractors = pred_evi - gold_evi\\n            n_distractor += len(distractors)\\n            n_total += len(pred_evi)\\n            n_evaluated += 1\\n\\n        edcr = n_distractor / n_total if n_total else 0.0\\n\\n        return {\\n            \\\"edcr\\\": edcr,\\n            \\\"n_distractor_citations\\\": n_distractor,\\n            \\\"n_total_citations\\\": n_total,\\n            \\\"n_evaluated\\\": n_evaluated,\\n        }\\n\\n    def compute_format_compliance(self, raw_outputs: list[dict]) -> dict:\\n        \\\"\\\"\\\"计算模型输出的格式合规率。\\\"\\\"\\\"\\n        required_fields = {\\\"head\\\", \\\"relation\\\", \\\"tail\\\", \\\"evidence\\\"}\\n        n_total = len(raw_outputs)\\n        n_parseable = 0\\n        n_field_complete = 0\\n        n_evidence_valid = 0\\n\\n        for item in raw_outputs:\\n            doc_id = item.get(\\\"doc_id\\\", \\\"\\\")\\n            raw_text = item.get(\\\"raw_text\\\", \\\"\\\")\\n\\n            parsed, _ = parse_model_output(raw_text)\\n            if not parsed and not self._is_parseable_json_list(raw_text):\\n                continue\\n            n_parseable += 1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

````text
Now I have a clear picture. Let me analyze the differences between our implementation and DREEAM's.

## Our `compute_evi_f1` method:
```python
def compute_evi_f1(self, predictions, gold):
    gold_map = {}
    for g in gold:
        key = _triple_key(g["doc_id"], g["head"], g["tail"], g["relation"])
        gold_map.setdefault(key, set()).update(g.get("evidence", []))

    total_tp = 0


```

Building the evaluation logic...

```

python
evi_total = sum(len(evi) for evi in gold_map.values())
    
    evi_prec = evi_tp / evi_pred_total  # ALL pred evi in denominator
    evi_rec = evi_tp / evi_gold_total   # ALL gold evi in denominator
```

## DREEAM's `official_evaluate`:
```python
# For each prediction:
pred_evi += len(evi)  # ALL predicted evidence (whether triple is correct or not)

if (title, r, h_idx, t_idx) in std:  # Only for correctly predicted triples
    correct_evidence += len(stdevi & evi)

# Then:
evi_p = correct_evidence / pred_evi   # ALL pred evi in denominator
evi_r = correct_evidence / tot_evidences  # ALL gold evi in

Finishing the evidence calculation...

Looking at the comparison table, I can see how our two approaches differ in their denominators and matching strategies. Our `compute_evi_f1_joint` actually aligns quite closely with DREEAM's protocol, with the main distinction being how we match entities—we use string-based name matching while DREEAM uses index-based matching. The key difference between our two methods is that `compute_evi_f1` restricts both the numerator and denominators to only true positive triples, whereas `compute_evi_f1_joint` uses all predicted evidence in the precision denominator, matching DREEAM's approach more closely. the one we report as `evi_f1`): Only considers TP triples for both precision and recall denominators. This will give **inflated** scores because:
   - Precision: doesn't penalize evidence from wrong triples
   - Recall: doesn't include evidence from missed triples
   
2. **`compute_evi_f1_joint`** (reported as `evi_f1_joint`): Matches DREEAM protocol for precision and recall denominators.

3. **Entity matching**: We match by entity name (string), DREEAM matches by entity index. This could cause discrepancies if entity names have normalization issues, but fundamentally these should be equivalent since each entity index maps to a specific name.

There's a potential issue where our system could conflate different entities if they share the same name, though in practice DocRED entities within a document have distinct names, so this shouldn't be problematic. The key insight is that our `evi_f1` metric inflates scores by only calculating against true positive triples, while `evi_f1_joint` properly aligns with DREEAM's methodology. The 0.80+ scores we're seeing likely come from the inflated `compute_evi_f1` rather than the more rigorous `compute_evi_f1_joint`. I need to check which metric is actually being reported and examine the evaluation outputs to confirm.

Checking the evaluate method... I'm seeing a key difference in how the two methods handle evidence deduplication. The `compute_evi_f1_joint` method unions all evidence from predictions that share the same triple key, while DREEAM's deduplication approach keeps only the first occurrence—this could lead to different metric calculations depending on which evidence sets are being counted. only the first prediction for each unique triple. But since DREEAM deduplicates before processing, and our code unions evidence sets for duplicate triples, the behavior for evidence should be the same if our model doesn't produce duplicate triples with different evidence sets. In practice, this is likely fine.

Let me also check the gold_map construction. In DREEAM, it overwrites duplicate keys while still counting all evidence lengths, whereas our approach unions the evidence sets and sums from those unioned sets. For DocRED, each triple should be unique anyway, so this difference shouldn't matter in practice.

Now I'm looking at how gold comes from `gold_from_docred()`... I'm realizing that using entity names could cause issues when different entity groups happen to share the same first-mention name, though this is rare in practice. The critical distinction I'm seeing is that `evi_f1` in the code measures evidence F1 only for correct triples, while `evi_f1_joint` properly accounts for false positives and negatives like DREEAM does. Those inflated 0.80+ scores are likely coming from `compute_evi_f1`, so I should verify this against existing evaluation results and check how evidence from predictions is being handled.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "e802f13e-d4de-4a63-8215-5b71b4eb3461",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CyY4Q1Y5XvobciVzru1pW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3870,
      "cache_read_input_tokens": 35287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3870
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 24_

现在清楚地看到了两边的代码。让我检查已有的 eval 结果，确认哪个 evi_f1 在被引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "0f479d5f-70f9-4523-b2c8-e4aba79a83b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CyY4Q1Y5XvobciVzru1pW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3870,
      "cache_read_input_tokens": 35287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3870
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01G5fjmS8CWyD93krvVcAxEw`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/freige -name \"eval_results*\" -o -name \"metrics*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "cb738f89-51a2-442d-8e68-54f1136041fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CyY4Q1Y5XvobciVzru1pW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3870,
      "cache_read_input_tokens": 35287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3870
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 26 · 2026-05-17T12:56:19.798Z_

<details><summary>↩ Tool result · `toolu_01G5fjmS8CWyD93krvVcAxEw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "bb98bfea-d45d-4793-98db-4f6a914ef0a6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_017e4SMTGnzjhrrx5a6dXW9J`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/freige -name \"*.json\" -path \"*eval*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "ac7f36eb-df42-4ca0-8ff5-4965c85d21ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tMDwZQyUY3zJ6B5RQK6xx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2958,
      "cache_read_input_tokens": 39157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2958
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 28 · 2026-05-17T12:56:22.314Z_

<details><summary>↩ Tool result · `toolu_017e4SMTGnzjhrrx5a6dXW9J`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "375355ae-5aee-4a44-9ae3-a511b10b2249",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Vt3LBqX1et53Qykgrf3QGG`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/freige/outputs -type f -name \"*.json\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "0fa3c089-4ee2-4c7e-9d9a-9b3629192a1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8tb7bCkAqNWYNQ9sCN2i7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 42115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 202
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 30 · 2026-05-17T12:56:24.810Z_

<details><summary>↩ Tool result · `toolu_01Vt3LBqX1et53Qykgrf3QGG`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "dca4c7ef-9beb-4718-9181-2ac5397c4337",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01UZH1gNVu32PGVUucVGTkK4`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/freige -type d -name \"outputs\" -o -type d -name \"results\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "839dd68f-7201-40fd-8b46-3363676f64f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H8tb7bCkAqNWYNQ9sCN2i7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 42115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 202
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 32 · 2026-05-17T12:56:25.883Z_

<details><summary>↩ Tool result · `toolu_01UZH1gNVu32PGVUucVGTkK4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/freige/outputs\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "418669ac-ec37-4083-83a6-571ac409f95c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/freige/outputs\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/freige/outputs\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 33_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01P9wDucgJmK2TM2HcXbipL8`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/freige/outputs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "cf0d09ab-750d-41b9-b476-af5a2bc5ef1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VtTDrk6UUVhn4KJ449Q9Jv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 486,
      "cache_read_input_tokens": 42317,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 486
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 34 · 2026-05-17T12:56:31.947Z_

<details><summary>↩ Tool result · `toolu_01P9wDucgJmK2TM2HcXbipL8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4\\ndrwxr-xr-x  6 root root  136 May 17 08:58 .\\ndrwxr-xr-x 15 root root 4096 May 17 19:54 ..\\ndrwxr-xr-x  2 root root   64 May 16 21:52 rsft_candidates_1_7b\\ndrwxr-xr-x  2 root root   86 May 17 09:56 rsft_candidates_8b\\ndrwxr-xr-x  2 root root   64 May 16 22:25 rsft_candidates_llama_8b\\ndrwxr-xr-x  2 root root   95 May 17 10:52 rsft_scored_1_7b\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "1ae20bf6-7a5f-477a-a6c0-0800060df8a8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"total 4\\\\ndrwxr-xr-x  6 root root  136 May 17 08:58 .\\\\ndrwxr-xr-x 15 root root 4096 May 17 19:54 ..\\\\ndrwxr-xr-x  2 root root   64 May 16 21:52 rsft_candidates_1_7b\\\\ndrwxr-xr-x  2 root root   86 May 17 09:56 rsft_candidates_8b\\\\ndrwxr-xr-x  2 root root   64 May 16 22:25 rsft_candidates_llama_8b\\\\ndrwxr-xr-x  2 root root   95 May 17 10:52 rsft_scored_1_7b\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"total 4\\ndrwxr-xr-x  6 root root  136 May 17 08:58 .\\ndrwxr-xr-x 15 root root 4096 May 17 19:54 ..\\ndrwxr-xr-x  2 root root   64 May 16 21:52 rsft_candidates_1_7b\\ndrwxr-xr-x  2 root root   86 May 17 09:56 rsft_candidates_8b\\ndrwxr-xr-x  2 root root   64 May 16 22:25 rsft_candidates_llama_8b\\ndrwxr-xr-x  2 root root   95 May 17 10:52 rsft_scored_1_7b\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01YT8renqwz9mZQcMf2pc1R6`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/freige -name \"summary*\" -o -name \"eval_summary*\" -o -name \"*result*json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "79c23461-c3ce-4978-8e7c-68a63cb16aaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6Q45uGeyt6ny8zcNsb12M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 397,
      "cache_read_input_tokens": 42803,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 397
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 36 · 2026-05-17T12:56:36.203Z_

<details><summary>↩ Tool result · `toolu_01YT8renqwz9mZQcMf2pc1R6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "faef4f96-457b-4d65-bd85-d4c092cc247c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 37_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Xmdxx9Vttkh6WYbs31KdSU`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -r \"evi_f1\" /root/autodl-tmp/freige/eval/batch_eval.py /root/autodl-tmp/freige/eval/inference.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "6a4f17e5-107d-4705-a881-59435b5a84e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyGKUSc3BttE5u2i7YWJBP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 212,
      "cache_read_input_tokens": 43200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 212
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 38 · 2026-05-17T12:56:44.282Z_

<details><summary>↩ Tool result · `toolu_01Xmdxx9Vttkh6WYbs31KdSU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/freige/eval/batch_eval.py:                    \\\"evi_f1\\\": existing.get(\\\"evi_f1\\\"),\\n/root/autodl-tmp/freige/eval/batch_eval.py:                \\\"evi_f1\\\": metrics.get(\\\"evi_f1\\\"),\\n/root/autodl-tmp/freige/eval/batch_eval.py:            print(f\\\"    F1={b['f1']:.4f}  Ign-F1={b['ign_f1']:.4f}  Evi-F1={b['evi_f1']:.4f}  EDCR={b.get('edcr', 0):.4f}\\\")\\n/root/autodl-tmp/freige/eval/inference.py:        print(f\\\"  Evi-F1:      {metrics['evi_f1']:.4f}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "b78b2814-e41f-4237-b2ea-8ebb2cbc9595",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/freige/eval/batch_eval.py:                    \\\\\\\"evi_f1\\\\\\\": existing.get(\\\\\\\"evi_f1\\\\\\\"),\\\\n/root/autodl-tmp/freige/eval/batch_eval.py:                \\\\\\\"evi_f1\\\\\\\": metrics.get(\\\\\\\"evi_f1\\\\\\\"),\\\\n/root/autodl-tmp/freige/eval/batch_eval.py:            print(f\\\\\\\"    F1={b['f1']:.4f}  Ign-F1={b['ign_f1']:.4f}  Evi-F1={b['evi_f1']:.4f}  EDCR={b.get('edcr', 0):.4f}\\\\\\\")\\\\n/root/autodl-tmp/freige/eval/inference.py:        print(f\\\\\\\"  Evi-F1:      {metrics['evi_f1']:.4f}\\\\\\\")\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/freige/eval/batch_eval.py:                    \\\"evi_f1\\\": existing.get(\\\"evi_f1\\\"),\\n/root/autodl-tmp/freige/eval/batch_eval.py:                \\\"evi_f1\\\": metrics.get(\\\"evi_f1\\\"),\\n/root/autodl-tmp/freige/eval/batch_eval.py:            print(f\\\"    F1={b['f1']:.4f}  Ign-F1={b['ign_f1']:.4f}  Evi-F1={b['evi_f1']:.4f}  EDCR={b.get('edcr', 0):.4f}\\\")\\n/root/autodl-tmp/freige/eval/inference.py:        print(f\\\"  Evi-F1:      {metrics['evi_f1']:.4f}\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
So the eval code reports `evi_f1` which is from `compute_evi_f1` — the per-TP-triple version that doesn't penalize FP/FN triples. This is NOT aligned with DREEAM.

Now let me also check the memory/report for the project to see what numbers have been reported.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "5d81dac9-8558-42ed-ac4d-becf56344dba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBgaf5ECZjJNzvDArov6rc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 43412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 40_

确认了：我们一直在报告的 `evi_f1` 来自 `compute_evi_f1`（只在 TP triples 上算），而不是 DREEAM 协议。让我检查已有预测结果的路径，准备重新计算。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "7e44bf7d-ade7-4c40-a660-4a417ae73851",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBgaf5ECZjJNzvDArov6rc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 43412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011bGsTcZDcAKs3B5YpnrcWW`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/freige -name \"predictions*\" -o -name \"pred*jsonl\" -o -name \"pred*json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "e5a46bd7-469d-42d4-900d-c6e85b8cfb7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBgaf5ECZjJNzvDArov6rc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 43412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 42 · 2026-05-17T12:56:52.563Z_

<details><summary>↩ Tool result · `toolu_011bGsTcZDcAKs3B5YpnrcWW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "ab70aec7-cf3c-489b-92b4-5de36a444014",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XgXgMhKEA8Zdggj4npKdEm`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/freige/eval/inference.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "4e70f343-00ca-4224-8676-12e4c4504da0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBgaf5ECZjJNzvDArov6rc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 43412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 44 · 2026-05-17T12:56:53.060Z_

<details><summary>↩ Tool result · `toolu_01XgXgMhKEA8Zdggj4npKdEm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"推理+评测完整流程: 加载 Qwen3-4B + LoRA adapter → 批量推理 → 解析输出 → 计算 F1/Evi-F1/EDCR。\\n\\n输入:\\n  - base model (Qwen3-4B) + 可选 LoRA adapter (SFT/GRPO checkpoint)\\n  - DocRED JSON 数据目录 (含 dev.json, train_annotated.json)\\n\\n输出 (保存到 --output_dir):\\n  - metrics.json: F1, Ign-F1, Evi-F1, EDCR, format_compliance_rate, n_truncated 等\\n  - predictions.json: 每个文档的详细预测 (doc_id, raw_output, parsed_triples, gold_triples, truncated, format_ok)\\n\\n依赖: transformers, peft, bitsandbytes, torch, tqdm\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport time\\nfrom pathlib import Path\\n\\nimport torch\\nfrom peft import PeftModel\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\\nfrom tqdm import tqdm\\n\\nfrom freige.data.docred_processor import DocREDProcessor, SPLIT_FILENAMES\\nfrom freige.training import LLAMA3_CHAT_TEMPLATE\\nfrom freige.eval.evaluator import DocREDEvaluator, gold_from_docred, parse_model_output\\n\\nlogging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\nlogger = logging.getLogger(__name__)\\n\\nSYSTEM_PROMPT = (\\n    \\\"You are an information extraction model. Given a document with numbered sentences \\\"\\n    \\\"and a list of entities, extract all relation triples. For each triple, provide the \\\"\\n    \\\"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \\\"\\n    \\\"Output as a JSON list.\\\"\\n)\\n\\n\\nNO_EVIDENCE_SYSTEM_PROMPT = (\\n    \\\"You are an information extraction model. Given a document with numbered sentences \\\"\\n    \\\"and a list of entities, extract all relation triples. For each triple, provide the \\\"\\n    \\\"head entity, relation type, and tail entity. \\\"\\n    \\\"Output as a JSON list.\\\"\\n)\\n\\n\\n# ---------------------------------------------------------------------------\\n# A. 模型加载\\n# ---------------------------------------------------------------------------\\n\\ndef load_model_and_tokenizer(model_path, adapter_path=None, sft_adapter_path=None, quantize=True):\\n    \\\"\\\"\\\"加载 Qwen3-4B + 可选 LoRA adapter (4-bit QLoRA)。\\n\\n    Args:\\n        model_path: base model 路径\\n        adapter_path: LoRA adapter 路径（SFT 或 GRPO checkpoint），None 则不加载\\n    Returns:\\n        (model, tokenizer)\\n    \\\"\\\"\\\"\\n    logger.info(\\\"Loading tokenizer: %s\\\", model_path)\\n    tokenizer = AutoTokenizer.from_pretrained(\\n        model_path,\\n        trust_remote_code=True,\\n        padding_side=\\\"left\\\",\\n    )\\n    if tokenizer.pad_token is None:\\n        tokenizer.pad_token = tokenizer.eos_token\\n    if not getattr(tokenizer, \\\"chat_template\\\", None):\\n        tokenizer.chat_template = LLAMA3_CHAT_TEMPLATE\\n\\n    logger.info(\\\"Loading model: %s\\\", model_path)\\n    model_kwargs = dict(\\n        trust_remote_code=True,\\n        attn_implementation=\\\"sdpa\\\",\\n        device_map=\\\"auto\\\",\\n    )\\n    if quantize:\\n        model_kwargs[\\\"quantization_config\\\"] = BitsAndBytesConfig(\\n            load_in_4bit=True,\\n            bnb_4bit_compute_dtype=torch.bfloat16,\\n            bnb_4bit_quant_type=\\\"nf4\\\",\\n            bnb_4bit_use_double_quant=True,\\n        )\\n    else:\\n        model_kwargs[\\\"torch_dtype\\\"] = torch.bfloat16\\n\\n    model = AutoModelForCausalLM.from_pretrained(model_path, **model_kwargs)\\n\\n    if sft_adapter_path:\\n        logger.info(\\\"Loading & merging SFT adapter: %s\\\", sft_adapter_path)\\n        model = PeftModel.from_pretrained(model, sft_adapter_path)\\n        model = model.merge_and_unload()\\n\\n    if adapter_path:\\n        logger.info(\\\"Loading LoRA adapter: %s\\\", adapter_path)\\n        model = PeftModel.from_pretrained(model, adapter_path)\\n\\n    model.eval()\\n    return model, tokenizer\\n\\n\\n# ---------------------------------------------------------------------------\\n# B. Prompt 构造\\n# ---------------------------------------------------------------------------\\n\\n\\ndef _apply_chat_template(tokenizer, messages, **kwargs):\\n    \\\"\\\"\\\"Wrap apply_chat_template to skip enable_thinking for tokenizers whose template doesn't use it.\\\"\\\"\\\"\\n    tmpl = getattr(tokenizer, \\\"chat_template\\\", None) or \\\"\\\"\\n    if \\\"enable_thinking\\\" not in tmpl:\\n        kwargs.pop(\\\"enable_thinking\\\", None)\\n    return tokenizer.apply_chat\\n\\n... [截断: 输出过长，省略 12422 字符] ...\\n\\nc = prepare_eval_data(\\n            args.data_path, args.split, tokenizer,\\n            include_evidence=_include_evi, system_prompt=_sys_prompt,\\n        )\\n\\n    t0 = time.time()\\n    raw_results = run_inference(\\n        model, tokenizer, eval_items, args.batch_size, args.max_new_tokens\\n    )\\n    elapsed = time.time() - t0\\n    logger.info(\\\"Inference: %.1fs (%.2f s/doc)\\\", elapsed, elapsed / max(len(eval_items), 1))\\n\\n    # 展平为 evaluator 格式\\n    all_predictions = []\\n    raw_outputs_for_eval = []\\n    for r in raw_results:\\n        doc_id = r[\\\"doc_id\\\"]\\n        for triple in r[\\\"parsed_triples\\\"]:\\n            all_predictions.append({\\n                \\\"doc_id\\\": doc_id,\\n                \\\"head\\\": triple[\\\"head\\\"],\\n                \\\"tail\\\": triple[\\\"tail\\\"],\\n                \\\"relation\\\": triple[\\\"relation\\\"],\\n                \\\"evidence\\\": triple.get(\\\"evidence\\\", []),\\n            })\\n        raw_outputs_for_eval.append({\\\"doc_id\\\": doc_id, \\\"raw_text\\\": r[\\\"raw_output\\\"]})\\n\\n    if args.split == \\\"test\\\":\\n        metrics = {\\\"note\\\": \\\"test split - submit to CodaLab for evaluation\\\"}\\n        codalab_preds = convert_to_codalab(raw_results, raw_docs)\\n        codalab_path = output_dir / \\\"codalab_submission.json\\\"\\n        with open(codalab_path, \\\"w\\\") as f:\\n            json.dump(codalab_preds, f, ensure_ascii=False)\\n        logger.info(\\\"CodaLab submission \\\\u2192 %s (%d predictions)\\\", codalab_path, len(codalab_preds))\\n    else:\\n        metrics = evaluate(all_predictions, gold, raw_outputs_for_eval, args.data_path, args.split)\\n\\n    n_truncated = sum(1 for r in raw_results if r[\\\"truncated\\\"])\\n    n_format_ok = sum(1 for r in raw_results if r[\\\"format_ok\\\"])\\n    n_total = len(raw_results)\\n    metrics[\\\"n_documents\\\"] = n_total\\n    metrics[\\\"n_predictions\\\"] = len(all_predictions)\\n    metrics[\\\"n_truncated\\\"] = n_truncated\\n    metrics[\\\"n_format_ok\\\"] = n_format_ok\\n    metrics[\\\"format_ok_rate\\\"] = n_format_ok / n_total if n_total else 0.0\\n    metrics[\\\"inference_time_seconds\\\"] = round(elapsed, 1)\\n    metrics[\\\"config\\\"] = vars(args)\\n\\n    # 保存 metrics.json\\n    metrics_path = output_dir / \\\"metrics.json\\\"\\n    with open(metrics_path, \\\"w\\\") as f:\\n        json.dump(metrics, f, indent=2, ensure_ascii=False)\\n    logger.info(\\\"Metrics → %s\\\", metrics_path)\\n\\n    # 保存 predictions.json（每文档详细信息）\\n    detailed = []\\n    for r in raw_results:\\n        doc_id = r[\\\"doc_id\\\"]\\n        doc_gold = gold_by_doc.get(doc_id, [])\\n        gold_triples = [\\n            {\\\"head\\\": g[\\\"head\\\"], \\\"tail\\\": g[\\\"tail\\\"], \\\"relation\\\": g[\\\"relation\\\"],\\n             \\\"evidence\\\": g.get(\\\"evidence\\\", [])}\\n            for g in doc_gold\\n        ]\\n        detailed.append({\\n            \\\"doc_id\\\": doc_id,\\n            \\\"raw_output\\\": r[\\\"raw_output\\\"],\\n            \\\"parsed_triples\\\": r[\\\"parsed_triples\\\"],\\n            \\\"gold_triples\\\": gold_triples,\\n            \\\"truncated\\\": r[\\\"truncated\\\"],\\n            \\\"format_ok\\\": r[\\\"format_ok\\\"],\\n        })\\n\\n    pred_path = output_dir / \\\"predictions.json\\\"\\n    with open(pred_path, \\\"w\\\") as f:\\n        json.dump(detailed, f, indent=2, ensure_ascii=False)\\n    logger.info(\\\"Predictions → %s\\\", pred_path)\\n\\n    # 控制台汇总\\n    if args.split == \\\"test\\\":\\n        print(\\\"\\\\n\\\" + \\\"=\\\" * 50)\\n        print(f\\\"  Test Documents: {n_total}\\\")\\n        print(f\\\"  Predictions:    {len(all_predictions)}\\\")\\n        print(f\\\"  CodaLab file:   {len(codalab_preds)} entries\\\")\\n        print(f\\\"  Format OK:      {n_format_ok}/{n_total} ({metrics.get('format_ok_rate', 0):.1%})\\\")\\n        print(f\\\"  Truncated:      {n_truncated}/{n_total}\\\")\\n        print(\\\"=\\\" * 50)\\n    else:\\n        print(\\\"\\\\n\\\" + \\\"=\\\" * 50)\\n        print(f\\\"  F1:          {metrics['f1']:.4f}\\\")\\n        print(f\\\"  Ign-F1:      {metrics['ign_f1']:.4f}\\\")\\n        print(f\\\"  Evi-F1:      {metrics['evi_f1']:.4f}\\\")\\n        print(f\\\"  EDCR:        {metrics.get('edcr', 0):.4f}\\\")\\n        print(f\\\"  Format OK:   {n_format_ok}/{n_total} ({metrics['format_ok_rate']:.1%})\\\")\\n        print(f\\\"  Truncated:   {n_truncated}/{n_total}\\\")\\n        print(f\\\"  Predictions: {len(all_predictions)}\\\")\\n        print(\\\"=\\\" * 50)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "07b810a2-72d4-42ca-afc0-1169612e3598",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\\\\\"\\\\\\\"\\\\\\\"推理+评测完整流程: 加载 Qwen3-4B + LoRA adapter → 批量推理 → 解析输出 → 计算 F1/Evi-F1/EDCR。\\\\n\\\\n输入:\\\\n  - base model (Qwen3-4B) + 可选 LoRA adapter (SFT/GRPO checkpoint)\\\\n  - DocRED JSON 数据目录 (含 dev.json, train_annotated.json)\\\\n\\\\n输出 (保存到 --output_dir):\\\\n  - metrics.json: F1, Ign-F1, Evi-F1, EDCR, format_compliance_rate, n_truncated 等\\\\n  - predictions.json: 每个文档的详细预测 (doc_id, raw_output, parsed_triples, gold_triples, truncated, format_ok)\\\\n\\\\n依赖: transformers, peft, bitsandbytes, torch, tqdm\\\\n\\\\\\\"\\\\\\\"\\\\\\\"\\\\n\\\\nimport argparse\\\\nimport json\\\\nimport logging\\\\nimport time\\\\nfrom pathlib import Path\\\\n\\\\nimport torch\\\\nfrom peft import PeftModel\\\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\\\\nfrom tqdm import tqdm\\\\n\\\\nfrom freige.data.docred_processor import DocREDProcessor, SPLIT_FILENAMES\\\\nfrom freige.training import LLAMA3_CHAT_TEMPLATE\\\\nfrom freige.eval.evaluator import DocREDEvaluator, gold_from_docred, parse_model_output\\\\n\\\\nlogging.basicConfig(level=logging.INFO, format=\\\\\\\"%(asctime)s %(levelname)s %(message)s\\\\\\\")\\\\nlogger = logging.getLogger(__name__)\\\\n\\\\nSYSTEM_PROMPT = (\\\\n    \\\\\\\"You are an information extraction model. Given a document with numbered sentences \\\\\\\"\\\\n    \\\\\\\"and a list of entities, extract all relation triples. For each triple, provide the \\\\\\\"\\\\n    \\\\\\\"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \\\\\\\"\\\\n    \\\\\\\"Output as a JSON list.\\\\\\\"\\\\n)\\\\n\\\\n\\\\nNO_EVIDENCE_SYSTEM_PROMPT = (\\\\n    \\\\\\\"You are an information extraction model. Given a document with numbered sentences \\\\\\\"\\\\n    \\\\\\\"and a list of entities, extract all relation triples. For each triple, provide the \\\\\\\"\\\\n    \\\\\\\"head entity, relation type, and tail entity. \\\\\\\"\\\\n    \\\\\\\"Output as a JSON list.\\\\\\\"\\\\n)\\\\n\\\\n\\\\n# ---------------------------------------------------------------------------\\\\n# A. 模型加载\\\\n# ---------------------------------------------------------------------------\\\\n\\\\ndef load_model_and_tokenizer(model_path, adapter_path=None, sft_adapter_path=None, quantize=True):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"加载 Qwen3-4B + 可选 LoRA adapter (4-bit QLoRA)。\\\\n\\\\n    Args:\\\\n        model_path: base model 路径\\\\n        adapter_path: LoRA adapter 路径（SFT 或 GRPO checkpoint），None 则不加载\\\\n    Returns:\\\\n        (model, tokenizer)\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"\\\\n    logger.info(\\\\\\\"Loading tokenizer: %s\\\\\\\", model_path)\\\\n    tokenizer = AutoTokenizer.from_pretrained(\\\\n        model_path,\\\\n        trust_remote_code=True,\\\\n        padding_side=\\\\\\\"left\\\\\\\",\\\\n    )\\\\n    if tokenizer.pad_token is None:\\\\n        tokenizer.pad_token = tokenizer.eos_token\\\\n    if not getattr(tokenizer, \\\\\\\"chat_template\\\\\\\", None):\\\\n        tokenizer.chat_template = LLAMA3_CHAT_TEMPLATE\\\\n\\\\n    logger.info(\\\\\\\"Loading model: %s\\\\\\\", model_path)\\\\n    model_kwargs = dict(\\\\n        trust_remote_code=True,\\\\n        attn_implementation=\\\\\\\"sdpa\\\\\\\",\\\\n        device_map=\\\\\\\"auto\\\\\\\",\\\\n    )\\\\n    if quantize:\\\\n        model_kwargs[\\\\\\\"quantization_config\\\\\\\"] = BitsAndBytesConfig(\\\\n            load_in_4bit=True,\\\\n            bnb_4bit_compute_dtype=torch.bfloat16,\\\\n            bnb_4bit_quant_type=\\\\\\\"nf4\\\\\\\",\\\\n            bnb_4bit_use_double_quant=True,\\\\n        )\\\\n    else:\\\\n        model_kwargs[\\\\\\\"torch_dtype\\\\\\\"] = torch.bfloat16\\\\n\\\\n    model = AutoModelForCausalLM.from_pretrained(model_path, **model_kwargs)\\\\n\\\\n    if sft_adapter_path:\\\\n        logger.info(\\\\\\\"Loading & merging SFT adapter: %s\\\\\\\", sft_adapter_path)\\\\n        model = PeftModel.from_pretrained(model, sft_adapter_path)\\\\n        model = model.merge_and_unload()\\\\n\\\\n    if adapter_path:\\\\n        logger.info(\\\\\\\"Loading LoRA adapter: %s\\\\\\\", adapter_path)\\\\n        model = PeftModel.from_pretrained(model, adapter_path)\\\\n\\\\n    model.eval()\\\\n    return model, tokenizer\\\\n\\\\n\\\\n# ---------------------------------------------------------------------------\\\\n# B. Prompt 构造\\\\n# ---------------------------------------------------------------------------\\\\n\\\\n\\\\ndef _apply_chat_template(tokenizer, messages, **kwargs):\\\\n    \\\\\\\"\\\\\\\"\\\\\\\"Wrap apply_chat_template to skip enable_thinking for tokenizers whose template doesn't use it.\\\\\\\"\\\\\\\"\\\\\\\"\\\\n    tmpl = getattr(tokenizer, \\\\\\\"chat_template\\\\\\\", None) or \\\\\\\"\\\\\\\"\\\\n    if \\\\\\\"enable_thinking\\\\\\\" not in tmpl:\\\\n        kwargs.pop(\\\\\\\"enable_thinking\\\\\\\", None)\\\\n    return tokenizer.apply_chat\\\\n\\\\n... [截断: 输出过长，省略 12422 字符] ...\\\\n\\\\nc = prepare_eval_data(\\\\n            args.data_path, args.split, tokenizer,\\\\n            include_evidence=_include_evi, system_prompt=_sys_prompt,\\\\n        )\\\\n\\\\n    t0 = time.time()\\\\n    raw_results = run_inference(\\\\n        model, tokenizer, eval_items, args.batch_size, args.max_new_tokens\\\\n    )\\\\n    elapsed = time.time() - t0\\\\n    logger.info(\\\\\\\"Inference: %.1fs (%.2f s/doc)\\\\\\\", elapsed, elapsed / max(len(eval_items), 1))\\\\n\\\\n    # 展平为 evaluator 格式\\\\n    all_predictions = []\\\\n    raw_outputs_for_eval = []\\\\n    for r in raw_results:\\\\n        doc_id = r[\\\\\\\"doc_id\\\\\\\"]\\\\n        for triple in r[\\\\\\\"parsed_triples\\\\\\\"]:\\\\n            all_predictions.append({\\\\n                \\\\\\\"doc_id\\\\\\\": doc_id,\\\\n                \\\\\\\"head\\\\\\\": triple[\\\\\\\"head\\\\\\\"],\\\\n                \\\\\\\"tail\\\\\\\": triple[\\\\\\\"tail\\\\\\\"],\\\\n                \\\\\\\"relation\\\\\\\": triple[\\\\\\\"relation\\\\\\\"],\\\\n                \\\\\\\"evidence\\\\\\\": triple.get(\\\\\\\"evidence\\\\\\\", []),\\\\n            })\\\\n        raw_outputs_for_eval.append({\\\\\\\"doc_id\\\\\\\": doc_id, \\\\\\\"raw_text\\\\\\\": r[\\\\\\\"raw_output\\\\\\\"]})\\\\n\\\\n    if args.split == \\\\\\\"test\\\\\\\":\\\\n        metrics = {\\\\\\\"note\\\\\\\": \\\\\\\"test split - submit to CodaLab for evaluation\\\\\\\"}\\\\n        codalab_preds = convert_to_codalab(raw_results, raw_docs)\\\\n        codalab_path = output_dir / \\\\\\\"codalab_submission.json\\\\\\\"\\\\n        with open(codalab_path, \\\\\\\"w\\\\\\\") as f:\\\\n            json.dump(codalab_preds, f, ensure_ascii=False)\\\\n        logger.info(\\\\\\\"CodaLab submission \\\\\\\\u2192 %s (%d predictions)\\\\\\\", codalab_path, len(codalab_preds))\\\\n    else:\\\\n        metrics = evaluate(all_predictions, gold, raw_outputs_for_eval, args.data_path, args.split)\\\\n\\\\n    n_truncated = sum(1 for r in raw_results if r[\\\\\\\"truncated\\\\\\\"])\\\\n    n_format_ok = sum(1 for r in raw_results if r[\\\\\\\"format_ok\\\\\\\"])\\\\n    n_total = len(raw_results)\\\\n    metrics[\\\\\\\"n_documents\\\\\\\"] = n_total\\\\n    metrics[\\\\\\\"n_predictions\\\\\\\"] = len(all_predictions)\\\\n    metrics[\\\\\\\"n_truncated\\\\\\\"] = n_truncated\\\\n    metrics[\\\\\\\"n_format_ok\\\\\\\"] = n_format_ok\\\\n    metrics[\\\\\\\"format_ok_rate\\\\\\\"] = n_format_ok / n_total if n_total else 0.0\\\\n    metrics[\\\\\\\"inference_time_seconds\\\\\\\"] = round(elapsed, 1)\\\\n    metrics[\\\\\\\"config\\\\\\\"] = vars(args)\\\\n\\\\n    # 保存 metrics.json\\\\n    metrics_path = output_dir / \\\\\\\"metrics.json\\\\\\\"\\\\n    with open(metrics_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(metrics, f, indent=2, ensure_ascii=False)\\\\n    logger.info(\\\\\\\"Metrics → %s\\\\\\\", metrics_path)\\\\n\\\\n    # 保存 predictions.json（每文档详细信息）\\\\n    detailed = []\\\\n    for r in raw_results:\\\\n        doc_id = r[\\\\\\\"doc_id\\\\\\\"]\\\\n        doc_gold = gold_by_doc.get(doc_id, [])\\\\n        gold_triples = [\\\\n            {\\\\\\\"head\\\\\\\": g[\\\\\\\"head\\\\\\\"], \\\\\\\"tail\\\\\\\": g[\\\\\\\"tail\\\\\\\"], \\\\\\\"relation\\\\\\\": g[\\\\\\\"relation\\\\\\\"],\\\\n             \\\\\\\"evidence\\\\\\\": g.get(\\\\\\\"evidence\\\\\\\", [])}\\\\n            for g in doc_gold\\\\n        ]\\\\n        detailed.append({\\\\n            \\\\\\\"doc_id\\\\\\\": doc_id,\\\\n            \\\\\\\"raw_output\\\\\\\": r[\\\\\\\"raw_output\\\\\\\"],\\\\n            \\\\\\\"parsed_triples\\\\\\\": r[\\\\\\\"parsed_triples\\\\\\\"],\\\\n            \\\\\\\"gold_triples\\\\\\\": gold_triples,\\\\n            \\\\\\\"truncated\\\\\\\": r[\\\\\\\"truncated\\\\\\\"],\\\\n            \\\\\\\"format_ok\\\\\\\": r[\\\\\\\"format_ok\\\\\\\"],\\\\n        })\\\\n\\\\n    pred_path = output_dir / \\\\\\\"predictions.json\\\\\\\"\\\\n    with open(pred_path, \\\\\\\"w\\\\\\\") as f:\\\\n        json.dump(detailed, f, indent=2, ensure_ascii=False)\\\\n    logger.info(\\\\\\\"Predictions → %s\\\\\\\", pred_path)\\\\n\\\\n    # 控制台汇总\\\\n    if args.split == \\\\\\\"test\\\\\\\":\\\\n        print(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 50)\\\\n        print(f\\\\\\\"  Test Documents: {n_total}\\\\\\\")\\\\n        print(f\\\\\\\"  Predictions:    {len(all_predictions)}\\\\\\\")\\\\n        print(f\\\\\\\"  CodaLab file:   {len(codalab_preds)} entries\\\\\\\")\\\\n        print(f\\\\\\\"  Format OK:      {n_format_ok}/{n_total} ({metrics.get('format_ok_rate', 0):.1%})\\\\\\\")\\\\n        print(f\\\\\\\"  Truncated:      {n_truncated}/{n_total}\\\\\\\")\\\\n        print(\\\\\\\"=\\\\\\\" * 50)\\\\n    else:\\\\n        print(\\\\\\\"\\\\\\\\n\\\\\\\" + \\\\\\\"=\\\\\\\" * 50)\\\\n        print(f\\\\\\\"  F1:          {metrics['f1']:.4f}\\\\\\\")\\\\n        print(f\\\\\\\"  Ign-F1:      {metrics['ign_f1']:.4f}\\\\\\\")\\\\n        print(f\\\\\\\"  Evi-F1:      {metrics['evi_f1']:.4f}\\\\\\\")\\\\n        print(f\\\\\\\"  EDCR:        {metrics.get('edcr', 0):.4f}\\\\\\\")\\\\n        print(f\\\\\\\"  Format OK:   {n_format_ok}/{n_total} ({metrics['format_ok_rate']:.1%})\\\\\\\")\\\\n        print(f\\\\\\\"  Truncated:   {n_truncated}/{n_total}\\\\\\\")\\\\n        print(f\\\\\\\"  Predictions: {len(all_predictions)}\\\\\\\")\\\\n        print(\\\\\\\"=\\\\\\\" * 50)\\\\n\\\\n\\\\nif __name__ == \\\\\\\"__main__\\\\\\\":\\\\n    main()\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"推理+评测完整流程: 加载 Qwen3-4B + LoRA adapter → 批量推理 → 解析输出 → 计算 F1/Evi-F1/EDCR。\\n\\n输入:\\n  - base model (Qwen3-4B) + 可选 LoRA adapter (SFT/GRPO checkpoint)\\n  - DocRED JSON 数据目录 (含 dev.json, train_annotated.json)\\n\\n输出 (保存到 --output_dir):\\n  - metrics.json: F1, Ign-F1, Evi-F1, EDCR, format_compliance_rate, n_truncated 等\\n  - predictions.json: 每个文档的详细预测 (doc_id, raw_output, parsed_triples, gold_triples, truncated, format_ok)\\n\\n依赖: transformers, peft, bitsandbytes, torch, tqdm\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport logging\\nimport time\\nfrom pathlib import Path\\n\\nimport torch\\nfrom peft import PeftModel\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig\\nfrom tqdm import tqdm\\n\\nfrom freige.data.docred_processor import DocREDProcessor, SPLIT_FILENAMES\\nfrom freige.training import LLAMA3_CHAT_TEMPLATE\\nfrom freige.eval.evaluator import DocREDEvaluator, gold_from_docred, parse_model_output\\n\\nlogging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s %(levelname)s %(message)s\\\")\\nlogger = logging.getLogger(__name__)\\n\\nSYSTEM_PROMPT = (\\n    \\\"You are an information extraction model. Given a document with numbered sentences \\\"\\n    \\\"and a list of entities, extract all relation triples. For each triple, provide the \\\"\\n    \\\"head entity, relation type, tail entity, and the sentence IDs that serve as evidence. \\\"\\n    \\\"Output as a JSON list.\\\"\\n)\\n\\n\\nNO_EVIDENCE_SYSTEM_PROMPT = (\\n    \\\"You are an information extraction model. Given a document with numbered sentences \\\"\\n    \\\"and a list of entities, extract all relation triples. For each triple, provide the \\\"\\n    \\\"head entity, relation type, and tail entity. \\\"\\n    \\\"Output as a JSON list.\\\"\\n)\\n\\n\\n# ---------------------------------------------------------------------------\\n# A. 模型加载\\n# ---------------------------------------------------------------------------\\n\\ndef load_model_and_tokenizer(model_path, adapter_path=None, sft_adapter_path=None, quantize=True):\\n    \\\"\\\"\\\"加载 Qwen3-4B + 可选 LoRA adapter (4-bit QLoRA)。\\n\\n    Args:\\n        model_path: base model 路径\\n        adapter_path: LoRA adapter 路径（SFT 或 GRPO checkpoint），None 则不加载\\n    Returns:\\n        (model, tokenizer)\\n    \\\"\\\"\\\"\\n    logger.info(\\\"Loading tokenizer: %s\\\", model_path)\\n    tokenizer = AutoTokenizer.from_pretrained(\\n        model_path,\\n        trust_remote_code=True,\\n        padding_side=\\\"left\\\",\\n    )\\n    if tokenizer.pad_token is None:\\n        tokenizer.pad_token = tokenizer.eos_token\\n    if not getattr(tokenizer, \\\"chat_template\\\", None):\\n        tokenizer.chat_template = LLAMA3_CHAT_TEMPLATE\\n\\n    logger.info(\\\"Loading model: %s\\\", model_path)\\n    model_kwargs = dict(\\n        trust_remote_code=True,\\n        attn_implementation=\\\"sdpa\\\",\\n        device_map=\\\"auto\\\",\\n    )\\n    if quantize:\\n        model_kwargs[\\\"quantization_config\\\"] = BitsAndBytesConfig(\\n            load_in_4bit=True,\\n            bnb_4bit_compute_dtype=torch.bfloat16,\\n            bnb_4bit_quant_type=\\\"nf4\\\",\\n            bnb_4bit_use_double_quant=True,\\n        )\\n    else:\\n        model_kwargs[\\\"torch_dtype\\\"] = torch.bfloat16\\n\\n    model = AutoModelForCausalLM.from_pretrained(model_path, **model_kwargs)\\n\\n    if sft_adapter_path:\\n        logger.info(\\\"Loading & merging SFT adapter: %s\\\", sft_adapter_path)\\n        model = PeftModel.from_pretrained(model, sft_adapter_path)\\n        model = model.merge_and_unload()\\n\\n    if adapter_path:\\n        logger.info(\\\"Loading LoRA adapter: %s\\\", adapter_path)\\n        model = PeftModel.from_pretrained(model, adapter_path)\\n\\n    model.eval()\\n    return model, tokenizer\\n\\n\\n# ---------------------------------------------------------------------------\\n# B. Prompt 构造\\n# ---------------------------------------------------------------------------\\n\\n\\ndef _apply_chat_template(tokenizer, messages, **kwargs):\\n    \\\"\\\"\\\"Wrap apply_chat_template to skip enable_thinking for tokenizers whose template doesn't use it.\\\"\\\"\\\"\\n    tmpl = getattr(tokenizer, \\\"chat_template\\\", None) or \\\"\\\"\\n    if \\\"enable_thinking\\\" not in tmpl:\\n        kwargs.pop(\\\"enable_thinking\\\", None)\\n    return tokenizer.apply_chat\\n\\n... [截断: 输出过长，省略 12422 字符] ...\\n\\nc = prepare_eval_data(\\n            args.data_path, args.split, tokenizer,\\n            include_evidence=_include_evi, system_prompt=_sys_prompt,\\n        )\\n\\n    t0 = time.time()\\n    raw_results = run_inference(\\n        model, tokenizer, eval_items, args.batch_size, args.max_new_tokens\\n    )\\n    elapsed = time.time() - t0\\n    logger.info(\\\"Inference: %.1fs (%.2f s/doc)\\\", elapsed, elapsed / max(len(eval_items), 1))\\n\\n    # 展平为 evaluator 格式\\n    all_predictions = []\\n    raw_outputs_for_eval = []\\n    for r in raw_results:\\n        doc_id = r[\\\"doc_id\\\"]\\n        for triple in r[\\\"parsed_triples\\\"]:\\n            all_predictions.append({\\n                \\\"doc_id\\\": doc_id,\\n                \\\"head\\\": triple[\\\"head\\\"],\\n                \\\"tail\\\": triple[\\\"tail\\\"],\\n                \\\"relation\\\": triple[\\\"relation\\\"],\\n                \\\"evidence\\\": triple.get(\\\"evidence\\\", []),\\n            })\\n        raw_outputs_for_eval.append({\\\"doc_id\\\": doc_id, \\\"raw_text\\\": r[\\\"raw_output\\\"]})\\n\\n    if args.split == \\\"test\\\":\\n        metrics = {\\\"note\\\": \\\"test split - submit to CodaLab for evaluation\\\"}\\n        codalab_preds = convert_to_codalab(raw_results, raw_docs)\\n        codalab_path = output_dir / \\\"codalab_submission.json\\\"\\n        with open(codalab_path, \\\"w\\\") as f:\\n            json.dump(codalab_preds, f, ensure_ascii=False)\\n        logger.info(\\\"CodaLab submission \\\\u2192 %s (%d predictions)\\\", codalab_path, len(codalab_preds))\\n    else:\\n        metrics = evaluate(all_predictions, gold, raw_outputs_for_eval, args.data_path, args.split)\\n\\n    n_truncated = sum(1 for r in raw_results if r[\\\"truncated\\\"])\\n    n_format_ok = sum(1 for r in raw_results if r[\\\"format_ok\\\"])\\n    n_total = len(raw_results)\\n    metrics[\\\"n_documents\\\"] = n_total\\n    metrics[\\\"n_predictions\\\"] = len(all_predictions)\\n    metrics[\\\"n_truncated\\\"] = n_truncated\\n    metrics[\\\"n_format_ok\\\"] = n_format_ok\\n    metrics[\\\"format_ok_rate\\\"] = n_format_ok / n_total if n_total else 0.0\\n    metrics[\\\"inference_time_seconds\\\"] = round(elapsed, 1)\\n    metrics[\\\"config\\\"] = vars(args)\\n\\n    # 保存 metrics.json\\n    metrics_path = output_dir / \\\"metrics.json\\\"\\n    with open(metrics_path, \\\"w\\\") as f:\\n        json.dump(metrics, f, indent=2, ensure_ascii=False)\\n    logger.info(\\\"Metrics → %s\\\", metrics_path)\\n\\n    # 保存 predictions.json（每文档详细信息）\\n    detailed = []\\n    for r in raw_results:\\n        doc_id = r[\\\"doc_id\\\"]\\n        doc_gold = gold_by_doc.get(doc_id, [])\\n        gold_triples = [\\n            {\\\"head\\\": g[\\\"head\\\"], \\\"tail\\\": g[\\\"tail\\\"], \\\"relation\\\": g[\\\"relation\\\"],\\n             \\\"evidence\\\": g.get(\\\"evidence\\\", [])}\\n            for g in doc_gold\\n        ]\\n        detailed.append({\\n            \\\"doc_id\\\": doc_id,\\n            \\\"raw_output\\\": r[\\\"raw_output\\\"],\\n            \\\"parsed_triples\\\": r[\\\"parsed_triples\\\"],\\n            \\\"gold_triples\\\": gold_triples,\\n            \\\"truncated\\\": r[\\\"truncated\\\"],\\n            \\\"format_ok\\\": r[\\\"format_ok\\\"],\\n        })\\n\\n    pred_path = output_dir / \\\"predictions.json\\\"\\n    with open(pred_path, \\\"w\\\") as f:\\n        json.dump(detailed, f, indent=2, ensure_ascii=False)\\n    logger.info(\\\"Predictions → %s\\\", pred_path)\\n\\n    # 控制台汇总\\n    if args.split == \\\"test\\\":\\n        print(\\\"\\\\n\\\" + \\\"=\\\" * 50)\\n        print(f\\\"  Test Documents: {n_total}\\\")\\n        print(f\\\"  Predictions:    {len(all_predictions)}\\\")\\n        print(f\\\"  CodaLab file:   {len(codalab_preds)} entries\\\")\\n        print(f\\\"  Format OK:      {n_format_ok}/{n_total} ({metrics.get('format_ok_rate', 0):.1%})\\\")\\n        print(f\\\"  Truncated:      {n_truncated}/{n_total}\\\")\\n        print(\\\"=\\\" * 50)\\n    else:\\n        print(\\\"\\\\n\\\" + \\\"=\\\" * 50)\\n        print(f\\\"  F1:          {metrics['f1']:.4f}\\\")\\n        print(f\\\"  Ign-F1:      {metrics['ign_f1']:.4f}\\\")\\n        print(f\\\"  Evi-F1:      {metrics['evi_f1']:.4f}\\\")\\n        print(f\\\"  EDCR:        {metrics.get('edcr', 0):.4f}\\\")\\n        print(f\\\"  Format OK:   {n_format_ok}/{n_total} ({metrics['format_ok_rate']:.1%})\\\")\\n        print(f\\\"  Truncated:   {n_truncated}/{n_total}\\\")\\n        print(f\\\"  Predictions: {len(all_predictions)}\\\")\\n        print(\\\"=\\\" * 50)\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding. Let me find existing predictions and run a recalculation. Let me also look for saved evaluation results to compare.

Let me look for existing model outputs/metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "08509165-8b05-4853-8479-0c2cf4ed3dc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdZUnrhRj3YUuM1t5DouPx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4089,
      "cache_read_input_tokens": 43879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4089
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 46_

现在找到了完整图景。让我找到已有的 predictions 文件来重新计算。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "af46cb34-b09c-43fd-a341-1f8ce535c0dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdZUnrhRj3YUuM1t5DouPx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4089,
      "cache_read_input_tokens": 43879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4089
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011zrqLSP5gca4PoLjWfVqpS`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/freige -name \"metrics.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "c5d57004-1b87-40c4-a1eb-1b4b97779593",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdZUnrhRj3YUuM1t5DouPx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4089,
      "cache_read_input_tokens": 43879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4089
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 48_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EFs1THNsRoQBAw2tmSaWrT`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp/freige -name \"predictions.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "1696336f-59b4-4b40-96f0-d4dd8312a9d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LdZUnrhRj3YUuM1t5DouPx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4089,
      "cache_read_input_tokens": 43879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4089
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-17T12:57:05.550Z_

<details><summary>↩ Tool result · `toolu_011zrqLSP5gca4PoLjWfVqpS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "320473cf-8516-4794-b69e-13e796dff1dc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 50 · 2026-05-17T12:57:05.933Z_

<details><summary>↩ Tool result · `toolu_01EFs1THNsRoQBAw2tmSaWrT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "1d26933f-aa0d-4a92-ab88-ff1c2f1b1d7b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 51_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01EHeCTK7TAAcYpHkoeoqHeA`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp -name \"metrics.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "e66470b8-ac7a-4479-b4cb-1f39e6500d1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gu6VZwZygBnarvVTvvnKiN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 524,
      "cache_read_input_tokens": 47968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 524
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 52 · 2026-05-17T12:57:08.416Z_

<details><summary>↩ Tool result · `toolu_01EHeCTK7TAAcYpHkoeoqHeA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-50/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-10/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-60/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-90/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-20/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-30/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_kl001_step100/checkpoint-100/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_lr5e6/checkpoint-20/metrics.json\\n/root/autodl-tmp/eval_results/lr5e6_r1_ckpt40/checkpoint-40/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60/metrics.json\\n/root/autodl-tmp/eval_results/lr5e6_r1_ckpt80/checkpoint-80/metrics.json\\n/root/autodl-tmp/eval_results/lr5e6_r1_ckpt100/checkpoint-100/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s44/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r1/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r2a/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r2b/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s43/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/metrics.json\\n/root/autodl-tmp/eval_results/grpo_g8_bf16/checkpoint-80/metrics.json\\n/root/autodl-tmp/eval_results/grpo_g8_bf16/checkpoint-100/metrics.json\\n/root/autodl-tmp/eval_results/grpo_g8_bf16/checkpoint-90/metrics.json\\n/root/autodl-tmp/eval_results/grpo_g8_bf16_ckpt100/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli/metrics.json\\n/root/autodl-tmp/eval_results/sft_no_evidence/metrics.json\\n/root/autodl-tmp/eval_results/test_rsft_s44/metrics.json\\n/root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step30/metrics.json\\n/root/autodl-tmp/eval_results/dpo_ced_1ep/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43/metrics.json\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step50/metrics.json\\n/root/autodl-tmp/eval_results/dpo_ced_1ep_fixed/metrics.json\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step70/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_topk3_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s44/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s45/metrics.json\\n/root/autodl-tmp/eval_results/sft_no_evidence_noquant/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s45/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s43/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval_r2/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s42_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s44_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s42_reeval/metrics.json\\n/root/autodl-tmp/eval_results/sft_baseline_d076_reeval/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_1_7b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/test_rsft_ced_s44/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_8b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_8b_no_evidence_eval_v2/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval_v3/metrics.json\\n/root/autodl-tmp/eval_results/llama_3_1_8b_no_evidence_eval/metrics.json\\n/root/autodl-tmp/eval_results/llama_3_1_8b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/plan_014_no_evidence_eval_d076/metrics.json\\n/root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r2/metrics.json\\n/root/autodl-tmp/eval_results/plan_002_test_rsft_s43/metrics.json\\n/root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r4/metrics.json\\n/root/autodl-tmp/eval_results/plan_002_test_rsft_s44/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds/metrics.json\\n/root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_eval_r2/metrics.json\\n/root/autodl-tmp/eval_results/plan_006_llama_rsft_r3_eval/metrics.json\\n/root/autodl-tmp/sft_eval_results/metrics.json\\n/root/autodl-tmp/sft_eval_r3_results/metrics.json\\n/root/autodl-tmp/sft_baseline_eval_results/metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "54bd1cc9-c933-426f-b5cb-84853b90aa76",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-50/metrics.json\\\\n/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-10/metrics.json\\\\n/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-60/metrics.json\\\\n/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-90/metrics.json\\\\n/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-20/metrics.json\\\\n/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-30/metrics.json\\\\n/root/autodl-tmp/eval_results/grpo_ced_kl001_step100/checkpoint-100/metrics.json\\\\n/root/autodl-tmp/eval_results/grpo_ced_lr5e6/checkpoint-20/metrics.json\\\\n/root/autodl-tmp/eval_results/lr5e6_r1_ckpt40/checkpoint-40/metrics.json\\\\n/root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60/metrics.json\\\\n/root/autodl-tmp/eval_results/lr5e6_r1_ckpt80/checkpoint-80/metrics.json\\\\n/root/autodl-tmp/eval_results/lr5e6_r1_ckpt100/checkpoint-100/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_s44/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_r1/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_r2a/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_r2b/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_s43/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/metrics.json\\\\n/root/autodl-tmp/eval_results/grpo_g8_bf16/checkpoint-80/metrics.json\\\\n/root/autodl-tmp/eval_results/grpo_g8_bf16/checkpoint-100/metrics.json\\\\n/root/autodl-tmp/eval_results/grpo_g8_bf16/checkpoint-90/metrics.json\\\\n/root/autodl-tmp/eval_results/grpo_g8_bf16_ckpt100/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_flat_nli/metrics.json\\\\n/root/autodl-tmp/eval_results/sft_no_evidence/metrics.json\\\\n/root/autodl-tmp/eval_results/test_rsft_s44/metrics.json\\\\n/root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step30/metrics.json\\\\n/root/autodl-tmp/eval_results/dpo_ced_1ep/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step50/metrics.json\\\\n/root/autodl-tmp/eval_results/dpo_ced_1ep_fixed/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step70/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_topk3_reeval/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s44/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s45/metrics.json\\\\n/root/autodl-tmp/eval_results/sft_no_evidence_noquant/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_ced_s45/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_ced_s43/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval_r2/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s42_reeval/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_ced_s44_reeval/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_ced_s42_reeval/metrics.json\\\\n/root/autodl-tmp/eval_results/sft_baseline_d076_reeval/metrics.json\\\\n/root/autodl-tmp/eval_results/qwen3_1_7b_sft_eval/metrics.json\\\\n/root/autodl-tmp/eval_results/test_rsft_ced_s44/metrics.json\\\\n/root/autodl-tmp/eval_results/qwen3_8b_sft_eval/metrics.json\\\\n/root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval/metrics.json\\\\n/root/autodl-tmp/eval_results/qwen3_8b_no_evidence_eval_v2/metrics.json\\\\n/root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval_v3/metrics.json\\\\n/root/autodl-tmp/eval_results/llama_3_1_8b_no_evidence_eval/metrics.json\\\\n/root/autodl-tmp/eval_results/llama_3_1_8b_sft_eval/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_014_no_evidence_eval_d076/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r2/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_002_test_rsft_s43/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r4/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_002_test_rsft_s44/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_eval_r2/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_006_llama_rsft_r3_eval/metrics.json\\\\n/root/autodl-tmp/sft_eval_results/metrics.json\\\\n/root/autodl-tmp/sft_eval_r3_results/metrics.json\\\\n/root/autodl-tmp/sft_baseline_eval_results/metrics.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-50/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-10/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-60/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-90/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-20/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_kl001/checkpoint-30/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_kl001_step100/checkpoint-100/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_lr5e6/checkpoint-20/metrics.json\\n/root/autodl-tmp/eval_results/lr5e6_r1_ckpt40/checkpoint-40/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60/metrics.json\\n/root/autodl-tmp/eval_results/lr5e6_r1_ckpt80/checkpoint-80/metrics.json\\n/root/autodl-tmp/eval_results/lr5e6_r1_ckpt100/checkpoint-100/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s44/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r1/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r2a/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r2b/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s43/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/metrics.json\\n/root/autodl-tmp/eval_results/grpo_g8_bf16/checkpoint-80/metrics.json\\n/root/autodl-tmp/eval_results/grpo_g8_bf16/checkpoint-100/metrics.json\\n/root/autodl-tmp/eval_results/grpo_g8_bf16/checkpoint-90/metrics.json\\n/root/autodl-tmp/eval_results/grpo_g8_bf16_ckpt100/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli/metrics.json\\n/root/autodl-tmp/eval_results/sft_no_evidence/metrics.json\\n/root/autodl-tmp/eval_results/test_rsft_s44/metrics.json\\n/root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step30/metrics.json\\n/root/autodl-tmp/eval_results/dpo_ced_1ep/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43/metrics.json\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step50/metrics.json\\n/root/autodl-tmp/eval_results/dpo_ced_1ep_fixed/metrics.json\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step70/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_topk3_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s44/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s45/metrics.json\\n/root/autodl-tmp/eval_results/sft_no_evidence_noquant/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s45/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s43/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval_r2/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s42_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s44_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s42_reeval/metrics.json\\n/root/autodl-tmp/eval_results/sft_baseline_d076_reeval/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_1_7b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/test_rsft_ced_s44/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_8b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_8b_no_evidence_eval_v2/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval_v3/metrics.json\\n/root/autodl-tmp/eval_results/llama_3_1_8b_no_evidence_eval/metrics.json\\n/root/autodl-tmp/eval_results/llama_3_1_8b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/plan_014_no_evidence_eval_d076/metrics.json\\n/root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r2/metrics.json\\n/root/autodl-tmp/eval_results/plan_002_test_rsft_s43/metrics.json\\n/root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r4/metrics.json\\n/root/autodl-tmp/eval_results/plan_002_test_rsft_s44/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds/metrics.json\\n/root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_eval_r2/metrics.json\\n/root/autodl-tmp/eval_results/plan_006_llama_rsft_r3_eval/metrics.json\\n/root/autodl-tmp/sft_eval_results/metrics.json\\n/root/autodl-tmp/sft_eval_r3_results/metrics.json\\n/root/autodl-tmp/sft_baseline_eval_results/metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
There are many eval results. Let me check a few key ones to see if they have `evi_f1_joint` already computed, and what the difference is. Let me pick the SFT baseline and a best RSFT result.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "63f62152-0792-4bec-8a18-6d85a3221c43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fE42xrBoGwtVqT9b19YPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 48492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2071
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 54_

有大量的 eval 结果。让我检查几个关键实验的 metrics，看 `evi_f1` vs `evi_f1_joint` 的差距。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "25cc3498-d1ed-4da8-b0a6-db41b82f7ba4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fE42xrBoGwtVqT9b19YPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 48492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2071
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 55_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01VsxHZCSNS55PgBdFK9pVEt`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/sft_baseline_d076_reeval/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "f6c26e50-f601-4851-ae23-7ef56864a016",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fE42xrBoGwtVqT9b19YPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 48492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2071
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 56 · 2026-05-17T12:57:15.361Z_

<details><summary>↩ Tool result · `toolu_01VsxHZCSNS55PgBdFK9pVEt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.41407190779287806,\\n  \\\"recall\\\": 0.39618138424821003,\\n  \\\"f1\\\": 0.4049291331959457,\\n  \\\"ign_precision\\\": 0.3936015950697843,\\n  \\\"ign_recall\\\": 0.401349228352278,\\n  \\\"ign_f1\\\": 0.3974376572866621,\\n  \\\"tp\\\": 4814,\\n  \\\"pred_count\\\": 11626,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.7941564561734213,\\n  \\\"evi_recall\\\": 0.8030880670987419,\\n  \\\"evi_f1\\\": 0.7985972893564591,\\n  \\\"n_evaluated\\\": 16699,\\n  \\\"edcr\\\": 0.6981983595400981,\\n  \\\"n_distractor_citations\\\": 19493,\\n  \\\"n_total_citations\\\": 27919,\\n  \\\"evi_joint_precision\\\": 0.3127146005227284,\\n  \\\"evi_joint_recall\\\": 0.31680598099787133,\\n  \\\"evi_f1_joint\\\": 0.31474699540929485,\\n  \\\"evi_tp\\\": 6102,\\n  \\\"evi_pred_total\\\": 19513,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9979695431472081,\\n  \\\"field_compliance_rate\\\": 0.7065989847715736,\\n  \\\"evidence_format_rate\\\": 0.7065989847715736,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 983,\\n  \\\"n_field_complete\\\": 696,\\n  \\\"n_evidence_valid\\\": 696,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 16880,\\n  \\\"n_truncated\\\": 288,\\n  \\\"n_format_ok\\\": 983,\\n  \\\"format_ok_rate\\\": 0.9979695431472081,\\n  \\\"inference_time_seconds\\\": 7056.5,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/sft_baseline_d076_reeval\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "13dae6d1-2382-4a2f-b779-fb1ae9ad691a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"precision\\\\\\\": 0.41407190779287806,\\\\n  \\\\\\\"recall\\\\\\\": 0.39618138424821003,\\\\n  \\\\\\\"f1\\\\\\\": 0.4049291331959457,\\\\n  \\\\\\\"ign_precision\\\\\\\": 0.3936015950697843,\\\\n  \\\\\\\"ign_recall\\\\\\\": 0.401349228352278,\\\\n  \\\\\\\"ign_f1\\\\\\\": 0.3974376572866621,\\\\n  \\\\\\\"tp\\\\\\\": 4814,\\\\n  \\\\\\\"pred_count\\\\\\\": 11626,\\\\n  \\\\\\\"gold_count\\\\\\\": 12151,\\\\n  \\\\\\\"evi_precision\\\\\\\": 0.7941564561734213,\\\\n  \\\\\\\"evi_recall\\\\\\\": 0.8030880670987419,\\\\n  \\\\\\\"evi_f1\\\\\\\": 0.7985972893564591,\\\\n  \\\\\\\"n_evaluated\\\\\\\": 16699,\\\\n  \\\\\\\"edcr\\\\\\\": 0.6981983595400981,\\\\n  \\\\\\\"n_distractor_citations\\\\\\\": 19493,\\\\n  \\\\\\\"n_total_citations\\\\\\\": 27919,\\\\n  \\\\\\\"evi_joint_precision\\\\\\\": 0.3127146005227284,\\\\n  \\\\\\\"evi_joint_recall\\\\\\\": 0.31680598099787133,\\\\n  \\\\\\\"evi_f1_joint\\\\\\\": 0.31474699540929485,\\\\n  \\\\\\\"evi_tp\\\\\\\": 6102,\\\\n  \\\\\\\"evi_pred_total\\\\\\\": 19513,\\\\n  \\\\\\\"evi_gold_total\\\\\\\": 19261,\\\\n  \\\\\\\"format_compliance_rate\\\\\\\": 0.9979695431472081,\\\\n  \\\\\\\"field_compliance_rate\\\\\\\": 0.7065989847715736,\\\\n  \\\\\\\"evidence_format_rate\\\\\\\": 0.7065989847715736,\\\\n  \\\\\\\"n_total\\\\\\\": 985,\\\\n  \\\\\\\"n_parseable\\\\\\\": 983,\\\\n  \\\\\\\"n_field_complete\\\\\\\": 696,\\\\n  \\\\\\\"n_evidence_valid\\\\\\\": 696,\\\\n  \\\\\\\"n_documents\\\\\\\": 985,\\\\n  \\\\\\\"n_predictions\\\\\\\": 16880,\\\\n  \\\\\\\"n_truncated\\\\\\\": 288,\\\\n  \\\\\\\"n_format_ok\\\\\\\": 983,\\\\n  \\\\\\\"format_ok_rate\\\\\\\": 0.9979695431472081,\\\\n  \\\\\\\"inference_time_seconds\\\\\\\": 7056.5,\\\\n  \\\\\\\"config\\\\\\\": {\\\\n    \\\\\\\"model_path\\\\\\\": \\\\\\\"/root/autodl-tmp/models/Qwen3-4B\\\\\\\",\\\\n    \\\\\\\"base_model\\\\\\\": \\\\\\\"/root/autodl-tmp/models/Qwen3-4B\\\\\\\",\\\\n    \\\\\\\"sft_adapter\\\\\\\": \\\\\\\"/root/autodl-tmp/sft_output\\\\\\\",\\\\n    \\\\\\\"data_path\\\\\\\": \\\\\\\"/root/autodl-tmp/data/docred\\\\\\\",\\\\n    \\\\\\\"output_dir\\\\\\\": \\\\\\\"/root/autodl-tmp/eval_results/sft_baseline_d076_reeval\\\\\\\",\\\\n    \\\\\\\"batch_size\\\\\\\": 4,\\\\n    \\\\\\\"max_new_tokens\\\\\\\": 1024,\\\\n    \\\\\\\"split\\\\\\\": \\\\\\\"dev\\\\\\\",\\\\n    \\\\\\\"seed\\\\\\\": 42,\\\\n    \\\\\\\"no_evidence\\\\\\\": false,\\\\n    \\\\\\\"quantize\\\\\\\": false\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.41407190779287806,\\n  \\\"recall\\\": 0.39618138424821003,\\n  \\\"f1\\\": 0.4049291331959457,\\n  \\\"ign_precision\\\": 0.3936015950697843,\\n  \\\"ign_recall\\\": 0.401349228352278,\\n  \\\"ign_f1\\\": 0.3974376572866621,\\n  \\\"tp\\\": 4814,\\n  \\\"pred_count\\\": 11626,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.7941564561734213,\\n  \\\"evi_recall\\\": 0.8030880670987419,\\n  \\\"evi_f1\\\": 0.7985972893564591,\\n  \\\"n_evaluated\\\": 16699,\\n  \\\"edcr\\\": 0.6981983595400981,\\n  \\\"n_distractor_citations\\\": 19493,\\n  \\\"n_total_citations\\\": 27919,\\n  \\\"evi_joint_precision\\\": 0.3127146005227284,\\n  \\\"evi_joint_recall\\\": 0.31680598099787133,\\n  \\\"evi_f1_joint\\\": 0.31474699540929485,\\n  \\\"evi_tp\\\": 6102,\\n  \\\"evi_pred_total\\\": 19513,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9979695431472081,\\n  \\\"field_compliance_rate\\\": 0.7065989847715736,\\n  \\\"evidence_format_rate\\\": 0.7065989847715736,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 983,\\n  \\\"n_field_complete\\\": 696,\\n  \\\"n_evidence_valid\\\": 696,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 16880,\\n  \\\"n_truncated\\\": 288,\\n  \\\"n_format_ok\\\": 983,\\n  \\\"format_ok_rate\\\": 0.9979695431472081,\\n  \\\"inference_time_seconds\\\": 7056.5,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/sft_baseline_d076_reeval\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019hikjmD2SPXaGGALzDejQV`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/rsft_ced_s44_reeval/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "c60e6899-472d-4cda-abe1-75e061ee5b0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fE42xrBoGwtVqT9b19YPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 48492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2071
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 58 · 2026-05-17T12:57:16.252Z_

<details><summary>↩ Tool result · `toolu_019hikjmD2SPXaGGALzDejQV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.47616136919315405,\\n  \\\"recall\\\": 0.44876964858859353,\\n  \\\"f1\\\": 0.4620599076388595,\\n  \\\"ign_precision\\\": 0.4526423520655006,\\n  \\\"ign_recall\\\": 0.44958876259125774,\\n  \\\"ign_f1\\\": 0.451110389911447,\\n  \\\"tp\\\": 5453,\\n  \\\"pred_count\\\": 11452,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.809657292702776,\\n  \\\"evi_recall\\\": 0.80039331366765,\\n  \\\"evi_f1\\\": 0.804998651442956,\\n  \\\"n_evaluated\\\": 15209,\\n  \\\"edcr\\\": 0.6350370913833864,\\n  \\\"n_distractor_citations\\\": 15580,\\n  \\\"n_total_citations\\\": 24534,\\n  \\\"evi_joint_precision\\\": 0.3745624899036132,\\n  \\\"evi_joint_recall\\\": 0.3611442811899694,\\n  \\\"evi_f1_joint\\\": 0.36773102135758096,\\n  \\\"evi_tp\\\": 6956,\\n  \\\"evi_pred_total\\\": 18571,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 1.0,\\n  \\\"field_compliance_rate\\\": 0.8020304568527918,\\n  \\\"evidence_format_rate\\\": 0.8020304568527918,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 985,\\n  \\\"n_field_complete\\\": 790,\\n  \\\"n_evidence_valid\\\": 790,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 15264,\\n  \\\"n_truncated\\\": 190,\\n  \\\"n_format_ok\\\": 985,\\n  \\\"format_ok_rate\\\": 1.0,\\n  \\\"inference_time_seconds\\\": 13077.6,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/rsft_output_s44/checkpoint-510\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/rsft_ced_s44_reeval\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 44,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "54794265-b695-44f0-a839-64e35732bd19",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"precision\\\\\\\": 0.47616136919315405,\\\\n  \\\\\\\"recall\\\\\\\": 0.44876964858859353,\\\\n  \\\\\\\"f1\\\\\\\": 0.4620599076388595,\\\\n  \\\\\\\"ign_precision\\\\\\\": 0.4526423520655006,\\\\n  \\\\\\\"ign_recall\\\\\\\": 0.44958876259125774,\\\\n  \\\\\\\"ign_f1\\\\\\\": 0.451110389911447,\\\\n  \\\\\\\"tp\\\\\\\": 5453,\\\\n  \\\\\\\"pred_count\\\\\\\": 11452,\\\\n  \\\\\\\"gold_count\\\\\\\": 12151,\\\\n  \\\\\\\"evi_precision\\\\\\\": 0.809657292702776,\\\\n  \\\\\\\"evi_recall\\\\\\\": 0.80039331366765,\\\\n  \\\\\\\"evi_f1\\\\\\\": 0.804998651442956,\\\\n  \\\\\\\"n_evaluated\\\\\\\": 15209,\\\\n  \\\\\\\"edcr\\\\\\\": 0.6350370913833864,\\\\n  \\\\\\\"n_distractor_citations\\\\\\\": 15580,\\\\n  \\\\\\\"n_total_citations\\\\\\\": 24534,\\\\n  \\\\\\\"evi_joint_precision\\\\\\\": 0.3745624899036132,\\\\n  \\\\\\\"evi_joint_recall\\\\\\\": 0.3611442811899694,\\\\n  \\\\\\\"evi_f1_joint\\\\\\\": 0.36773102135758096,\\\\n  \\\\\\\"evi_tp\\\\\\\": 6956,\\\\n  \\\\\\\"evi_pred_total\\\\\\\": 18571,\\\\n  \\\\\\\"evi_gold_total\\\\\\\": 19261,\\\\n  \\\\\\\"format_compliance_rate\\\\\\\": 1.0,\\\\n  \\\\\\\"field_compliance_rate\\\\\\\": 0.8020304568527918,\\\\n  \\\\\\\"evidence_format_rate\\\\\\\": 0.8020304568527918,\\\\n  \\\\\\\"n_total\\\\\\\": 985,\\\\n  \\\\\\\"n_parseable\\\\\\\": 985,\\\\n  \\\\\\\"n_field_complete\\\\\\\": 790,\\\\n  \\\\\\\"n_evidence_valid\\\\\\\": 790,\\\\n  \\\\\\\"n_documents\\\\\\\": 985,\\\\n  \\\\\\\"n_predictions\\\\\\\": 15264,\\\\n  \\\\\\\"n_truncated\\\\\\\": 190,\\\\n  \\\\\\\"n_format_ok\\\\\\\": 985,\\\\n  \\\\\\\"format_ok_rate\\\\\\\": 1.0,\\\\n  \\\\\\\"inference_time_seconds\\\\\\\": 13077.6,\\\\n  \\\\\\\"config\\\\\\\": {\\\\n    \\\\\\\"model_path\\\\\\\": \\\\\\\"/root/autodl-tmp/rsft_output_s44/checkpoint-510\\\\\\\",\\\\n    \\\\\\\"base_model\\\\\\\": \\\\\\\"/root/autodl-tmp/models/Qwen3-4B\\\\\\\",\\\\n    \\\\\\\"sft_adapter\\\\\\\": \\\\\\\"/root/autodl-tmp/sft_output\\\\\\\",\\\\n    \\\\\\\"data_path\\\\\\\": \\\\\\\"/root/autodl-tmp/data/docred\\\\\\\",\\\\n    \\\\\\\"output_dir\\\\\\\": \\\\\\\"/root/autodl-tmp/eval_results/rsft_ced_s44_reeval\\\\\\\",\\\\n    \\\\\\\"batch_size\\\\\\\": 4,\\\\n    \\\\\\\"max_new_tokens\\\\\\\": 1024,\\\\n    \\\\\\\"split\\\\\\\": \\\\\\\"dev\\\\\\\",\\\\n    \\\\\\\"seed\\\\\\\": 44,\\\\n    \\\\\\\"no_evidence\\\\\\\": false,\\\\n    \\\\\\\"quantize\\\\\\\": false\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.47616136919315405,\\n  \\\"recall\\\": 0.44876964858859353,\\n  \\\"f1\\\": 0.4620599076388595,\\n  \\\"ign_precision\\\": 0.4526423520655006,\\n  \\\"ign_recall\\\": 0.44958876259125774,\\n  \\\"ign_f1\\\": 0.451110389911447,\\n  \\\"tp\\\": 5453,\\n  \\\"pred_count\\\": 11452,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.809657292702776,\\n  \\\"evi_recall\\\": 0.80039331366765,\\n  \\\"evi_f1\\\": 0.804998651442956,\\n  \\\"n_evaluated\\\": 15209,\\n  \\\"edcr\\\": 0.6350370913833864,\\n  \\\"n_distractor_citations\\\": 15580,\\n  \\\"n_total_citations\\\": 24534,\\n  \\\"evi_joint_precision\\\": 0.3745624899036132,\\n  \\\"evi_joint_recall\\\": 0.3611442811899694,\\n  \\\"evi_f1_joint\\\": 0.36773102135758096,\\n  \\\"evi_tp\\\": 6956,\\n  \\\"evi_pred_total\\\": 18571,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 1.0,\\n  \\\"field_compliance_rate\\\": 0.8020304568527918,\\n  \\\"evidence_format_rate\\\": 0.8020304568527918,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 985,\\n  \\\"n_field_complete\\\": 790,\\n  \\\"n_evidence_valid\\\": 790,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 15264,\\n  \\\"n_truncated\\\": 190,\\n  \\\"n_format_ok\\\": 985,\\n  \\\"format_ok_rate\\\": 1.0,\\n  \\\"inference_time_seconds\\\": 13077.6,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/rsft_output_s44/checkpoint-510\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/rsft_ced_s44_reeval\\\",\\n    \\\"batch_size\\\": 4,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 44,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 59_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015cYGVphMUNpVzMKvRnFsT7`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/sft_baseline_eval_results/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "182e625c-debf-430d-91ce-d9259d583b7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012fE42xrBoGwtVqT9b19YPj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2071,
      "cache_read_input_tokens": 48492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2071
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 60 · 2026-05-17T12:57:16.775Z_

<details><summary>↩ Tool result · `toolu_015cYGVphMUNpVzMKvRnFsT7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.4042831453326794,\\n  \\\"recall\\\": 0.40704468768002633,\\n  \\\"f1\\\": 0.4056592167315973,\\n  \\\"ign_precision\\\": 0.4042831453326794,\\n  \\\"ign_recall\\\": 0.40704468768002633,\\n  \\\"ign_f1\\\": 0.4056592167315973,\\n  \\\"tp\\\": 4946,\\n  \\\"pred_count\\\": 12234,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.8034592626308603,\\n  \\\"evi_recall\\\": 0.79242233794218,\\n  \\\"evi_f1\\\": 0.7979026352664649,\\n  \\\"n_evaluated\\\": 18460,\\n  \\\"edcr\\\": 0.7117758474299524,\\n  \\\"n_distractor_citations\\\": 21796,\\n  \\\"n_total_citations\\\": 30622,\\n  \\\"format_compliance_rate\\\": 0.9979695431472081,\\n  \\\"field_compliance_rate\\\": 0.6263959390862944,\\n  \\\"evidence_format_rate\\\": 0.6263959390862944,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 983,\\n  \\\"n_field_complete\\\": 617,\\n  \\\"n_evidence_valid\\\": 617,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 18815,\\n  \\\"n_truncated\\\": 367,\\n  \\\"n_format_ok\\\": 983,\\n  \\\"format_ok_rate\\\": 0.9979695431472081,\\n  \\\"inference_time_seconds\\\": 6138.5,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": null,\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/sft_baseline_eval_results\\\",\\n    \\\"batch_size\\\": 16,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"quantize\\\": true\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "e62e4455-3ae4-4797-903c-5e2520987927",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"precision\\\\\\\": 0.4042831453326794,\\\\n  \\\\\\\"recall\\\\\\\": 0.40704468768002633,\\\\n  \\\\\\\"f1\\\\\\\": 0.4056592167315973,\\\\n  \\\\\\\"ign_precision\\\\\\\": 0.4042831453326794,\\\\n  \\\\\\\"ign_recall\\\\\\\": 0.40704468768002633,\\\\n  \\\\\\\"ign_f1\\\\\\\": 0.4056592167315973,\\\\n  \\\\\\\"tp\\\\\\\": 4946,\\\\n  \\\\\\\"pred_count\\\\\\\": 12234,\\\\n  \\\\\\\"gold_count\\\\\\\": 12151,\\\\n  \\\\\\\"evi_precision\\\\\\\": 0.8034592626308603,\\\\n  \\\\\\\"evi_recall\\\\\\\": 0.79242233794218,\\\\n  \\\\\\\"evi_f1\\\\\\\": 0.7979026352664649,\\\\n  \\\\\\\"n_evaluated\\\\\\\": 18460,\\\\n  \\\\\\\"edcr\\\\\\\": 0.7117758474299524,\\\\n  \\\\\\\"n_distractor_citations\\\\\\\": 21796,\\\\n  \\\\\\\"n_total_citations\\\\\\\": 30622,\\\\n  \\\\\\\"format_compliance_rate\\\\\\\": 0.9979695431472081,\\\\n  \\\\\\\"field_compliance_rate\\\\\\\": 0.6263959390862944,\\\\n  \\\\\\\"evidence_format_rate\\\\\\\": 0.6263959390862944,\\\\n  \\\\\\\"n_total\\\\\\\": 985,\\\\n  \\\\\\\"n_parseable\\\\\\\": 983,\\\\n  \\\\\\\"n_field_complete\\\\\\\": 617,\\\\n  \\\\\\\"n_evidence_valid\\\\\\\": 617,\\\\n  \\\\\\\"n_documents\\\\\\\": 985,\\\\n  \\\\\\\"n_predictions\\\\\\\": 18815,\\\\n  \\\\\\\"n_truncated\\\\\\\": 367,\\\\n  \\\\\\\"n_format_ok\\\\\\\": 983,\\\\n  \\\\\\\"format_ok_rate\\\\\\\": 0.9979695431472081,\\\\n  \\\\\\\"inference_time_seconds\\\\\\\": 6138.5,\\\\n  \\\\\\\"config\\\\\\\": {\\\\n    \\\\\\\"model_path\\\\\\\": \\\\\\\"/root/autodl-tmp/sft_output\\\\\\\",\\\\n    \\\\\\\"base_model\\\\\\\": \\\\\\\"/root/autodl-tmp/models/Qwen3-4B\\\\\\\",\\\\n    \\\\\\\"sft_adapter\\\\\\\": null,\\\\n    \\\\\\\"data_path\\\\\\\": \\\\\\\"/root/autodl-tmp/data/docred\\\\\\\",\\\\n    \\\\\\\"output_dir\\\\\\\": \\\\\\\"/root/autodl-tmp/sft_baseline_eval_results\\\\\\\",\\\\n    \\\\\\\"batch_size\\\\\\\": 16,\\\\n    \\\\\\\"max_new_tokens\\\\\\\": 1024,\\\\n    \\\\\\\"split\\\\\\\": \\\\\\\"dev\\\\\\\",\\\\n    \\\\\\\"seed\\\\\\\": 42,\\\\n    \\\\\\\"quantize\\\\\\\": true\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.4042831453326794,\\n  \\\"recall\\\": 0.40704468768002633,\\n  \\\"f1\\\": 0.4056592167315973,\\n  \\\"ign_precision\\\": 0.4042831453326794,\\n  \\\"ign_recall\\\": 0.40704468768002633,\\n  \\\"ign_f1\\\": 0.4056592167315973,\\n  \\\"tp\\\": 4946,\\n  \\\"pred_count\\\": 12234,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.8034592626308603,\\n  \\\"evi_recall\\\": 0.79242233794218,\\n  \\\"evi_f1\\\": 0.7979026352664649,\\n  \\\"n_evaluated\\\": 18460,\\n  \\\"edcr\\\": 0.7117758474299524,\\n  \\\"n_distractor_citations\\\": 21796,\\n  \\\"n_total_citations\\\": 30622,\\n  \\\"format_compliance_rate\\\": 0.9979695431472081,\\n  \\\"field_compliance_rate\\\": 0.6263959390862944,\\n  \\\"evidence_format_rate\\\": 0.6263959390862944,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 983,\\n  \\\"n_field_complete\\\": 617,\\n  \\\"n_evidence_valid\\\": 617,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 18815,\\n  \\\"n_truncated\\\": 367,\\n  \\\"n_format_ok\\\": 983,\\n  \\\"format_ok_rate\\\": 0.9979695431472081,\\n  \\\"inference_time_seconds\\\": 6138.5,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": null,\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/sft_baseline_eval_results\\\",\\n    \\\"batch_size\\\": 16,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"quantize\\\": true\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 61_

<details><summary>Logged reasoning block</summary>

```text
Now I have the key data. Let me summarize the findings:

### SFT baseline (d076_reeval, noquant):
- `evi_f1` = 0.7986 (our metric, TP-only)
- `evi_f1_joint` = 0.3147 (DREEAM-aligned)

### Best RSFT (rsft_ced_s44_reeval):
- `evi_f1` = 0.8050 (our metric, TP-only)


- `evi_f1_joint` = 0.3677 (DREEAM-aligned)

### DREEAM baseline: 
- dev_evi_f1 = 54.01 (= 0.5401)

This reveals a critical issue: our TP-only metric makes us look substantially ahead of DREEAM at 0.80 versus 0.54, but when I use the joint metric that aligns with their evaluation, we're actually trailing at 0.31-0.37. There's a fundamental mismatch in how we're measuring success.

Let me trace through DREEAM's evaluation logic to understand what their evi_f1 actually captures. Looking at their code, they're counting all predicted evidence in the denominator regardless of correctness, then only crediting matches when the triple itself is correct. That's exactly what our joint metric does, so the comparison is apples-to-apples—we're genuinely underperforming at 0.31 versus their 0.54.

The misleading 0.80+ number came from only evaluating evidence on correct triples, which hides the damage from false positives and negatives. But there's another factor dragging down our score: the evidence_format_rate is only 70% for SFT, meaning 30% of documents have malformed evidence fields that contribute empty predictions, tanking both precision and recall.

I should also check if there's a subtle difference in how we're computing this—DREEAM indexes entities by position while we use entity names, which could affect whether we're actually measuring the same thing. Looking at DREEAM's `re_eval` function more carefully, I see it iterates through sorted predictions and checks if each one matches a gold pair, then accumulates evidence accuracy across all predictions regardless of whether the relation itself was correct. This confirms that both `re_eval` and `official_evaluate` use the same evidence F1 calculation protocol. I'm looking at the evidence evaluation logic in the official DocRED evaluation function—it counts all predicted evidence regardless of whether the relation triple itself is correct, then calculates precision and recall based on how much the predicted evidence overlaps with the gold standard evidence. This matches what our `compute_evi_f1_joint` function does, so we're on the right track with the existing metrics.

The real problem is that the reported metric has been `evi_f1` (which inflates scores by only counting evidence from correct predictions), not `evi_f1_joint`. I need to verify our implementation is truly correct and then create a comparison table showing the difference between the two metrics.

Looking more closely at the implementations, there's a subtle difference in how duplicates are handled. Our approach unions evidence sets when the same triple appears multiple times, whereas DREEAM filters duplicates by keeping only the highest-scoring one. In practice this shouldn't matter since our model rarely produces exact duplicate triples, but I'm checking the deduplication logic...

Examining DREEAM's deduplication more carefully...

The key insight is that our `evi_f1` metric isn't actually DREEAM-compatible because it only counts true positives, which inflates the scores. Our `evi_f1_joint` metric is the one that matches DREEAM's evaluation, and when I look at the actual numbers, the gap is substantial—our best results are around 0.37 compared to DREEAM's 0.54. Now I'm trying to understand what's driving this discrepancy.

The main culprits seem to be our relation extraction F1 capping out around 0.40-0.46, which limits how high the evidence F1 can go, plus the high error rate in predicted evidence sentences even when the relations are correct. DREEAM achieves better results because it has stronger relation extraction performance and is specifically optimized for evidence extraction. Let me verify what DREEAM's actual relation extraction F1 was to see how much of the gap comes from that versus the evidence quality itself.

Now I need to validate my metric calculation, pull together the evidence F1 numbers from our key experiments, and compile everything into an analysis report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "f69a0792-6068-49d8-b143-8ce6c009abe7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9X26KNeQ4mUtV8LnXwRcr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3500,
      "cache_read_input_tokens": 50563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3500
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 62_

关键发现。数据非常清楚：

| 指标 | SFT baseline | RSFT best (s44) | DREEAM |
|------|-------------|----------------|--------|
| `evi_f1` (TP-only, 我们的) | 0.7986 | 0.8050 | - |
| `evi_f1_joint` (DREEAM协议) | **0.3147** | **0.3677** | **0.5401** |

差距巨大。`evi_f1` 严重膨胀，因为只在 TP triples 上算。让我再拉几个实验对比，并验证 `compute_evi_f1_joint` 的实现确实与 DREEAM 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "d5b70ed3-7a7e-448b-926b-ae03db654a82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9X26KNeQ4mUtV8LnXwRcr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3500,
      "cache_read_input_tokens": 50563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3500
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 63_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WdGCSmvsL1t8rEakxgKLBH`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "grep -l \"evi_f1_joint\" /root/autodl-tmp/eval_results/*/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "fca0775c-6477-45e1-aaeb-364e2769c4ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9X26KNeQ4mUtV8LnXwRcr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3500,
      "cache_read_input_tokens": 50563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3500
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 64 · 2026-05-17T12:58:15.967Z_

<details><summary>↩ Tool result · `toolu_01WdGCSmvsL1t8rEakxgKLBH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/eval_results/dpo_ced_1ep/metrics.json\\n/root/autodl-tmp/eval_results/dpo_ced_1ep_fixed/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60/metrics.json\\n/root/autodl-tmp/eval_results/grpo_g8_bf16_ckpt100/metrics.json\\n/root/autodl-tmp/eval_results/llama_3_1_8b_no_evidence_eval/metrics.json\\n/root/autodl-tmp/eval_results/llama_3_1_8b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/plan_006_llama_rsft_r3_eval/metrics.json\\n/root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_eval_r2/metrics.json\\n/root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r2/metrics.json\\n/root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r4/metrics.json\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step30/metrics.json\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step50/metrics.json\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step70/metrics.json\\n/root/autodl-tmp/eval_results/plan_014_no_evidence_eval_d076/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval_v3/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_1_7b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_8b_no_evidence_eval_v2/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_8b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s42_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s43/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s44_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s45/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s42_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval_r2/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s44/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s45/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r1/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r2a/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r2b/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s43/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s44/metrics.json\\n/root/autodl-tmp/eval_results/rsft_topk3_reeval/metrics.json\\n/root/autodl-tmp/eval_results/sft_baseline_d076_reeval/metrics.json\\n/root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json\\n/root/autodl-tmp/eval_results/sft_no_evidence/metrics.json\\n/root/autodl-tmp/eval_results/sft_no_evidence_noquant/metrics.json\\n/root/autodl-tmp/eval_results/test_rsft_s44/metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "d0e7d346-ea50-4a2b-b441-3e7c8bae51f2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/eval_results/dpo_ced_1ep/metrics.json\\\\n/root/autodl-tmp/eval_results/dpo_ced_1ep_fixed/metrics.json\\\\n/root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60/metrics.json\\\\n/root/autodl-tmp/eval_results/grpo_g8_bf16_ckpt100/metrics.json\\\\n/root/autodl-tmp/eval_results/llama_3_1_8b_no_evidence_eval/metrics.json\\\\n/root/autodl-tmp/eval_results/llama_3_1_8b_sft_eval/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_006_llama_rsft_r3_eval/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_eval_r2/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r2/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r4/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step30/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step50/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step70/metrics.json\\\\n/root/autodl-tmp/eval_results/plan_014_no_evidence_eval_d076/metrics.json\\\\n/root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval/metrics.json\\\\n/root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval_v3/metrics.json\\\\n/root/autodl-tmp/eval_results/qwen3_1_7b_sft_eval/metrics.json\\\\n/root/autodl-tmp/eval_results/qwen3_8b_no_evidence_eval_v2/metrics.json\\\\n/root/autodl-tmp/eval_results/qwen3_8b_sft_eval/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_ced_s42_reeval/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_ced_s43/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_ced_s44_reeval/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_ced_s45/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_flat_nli/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s42_reeval/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval_r2/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s44/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s45/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_r1/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_r2a/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_r2b/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_s43/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_s44/metrics.json\\\\n/root/autodl-tmp/eval_results/rsft_topk3_reeval/metrics.json\\\\n/root/autodl-tmp/eval_results/sft_baseline_d076_reeval/metrics.json\\\\n/root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json\\\\n/root/autodl-tmp/eval_results/sft_no_evidence/metrics.json\\\\n/root/autodl-tmp/eval_results/sft_no_evidence_noquant/metrics.json\\\\n/root/autodl-tmp/eval_results/test_rsft_s44/metrics.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/eval_results/dpo_ced_1ep/metrics.json\\n/root/autodl-tmp/eval_results/dpo_ced_1ep_fixed/metrics.json\\n/root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60/metrics.json\\n/root/autodl-tmp/eval_results/grpo_g8_bf16_ckpt100/metrics.json\\n/root/autodl-tmp/eval_results/llama_3_1_8b_no_evidence_eval/metrics.json\\n/root/autodl-tmp/eval_results/llama_3_1_8b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/plan_006_llama_rsft_r3_eval/metrics.json\\n/root/autodl-tmp/eval_results/plan_006_qwen3_1_7b_rsft_eval_r2/metrics.json\\n/root/autodl-tmp/eval_results/plan_007_redocred_4b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r2/metrics.json\\n/root/autodl-tmp/eval_results/plan_007_redocred_rsft_eval_r4/metrics.json\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step30/metrics.json\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step50/metrics.json\\n/root/autodl-tmp/eval_results/plan_011_bf16_g8_step70/metrics.json\\n/root/autodl-tmp/eval_results/plan_014_no_evidence_eval_d076/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_1_7b_no_evidence_eval_v3/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_1_7b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_8b_no_evidence_eval_v2/metrics.json\\n/root/autodl-tmp/eval_results/qwen3_8b_sft_eval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s42_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s43/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s44_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_ced_s45/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s42_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval_r2/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s44/metrics.json\\n/root/autodl-tmp/eval_results/rsft_flat_nli_s45/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r1/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r2a/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r2b/metrics.json\\n/root/autodl-tmp/eval_results/rsft_r2b_maxtok1536/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s43/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s43_dev_eval_preds/metrics.json\\n/root/autodl-tmp/eval_results/rsft_s44/metrics.json\\n/root/autodl-tmp/eval_results/rsft_topk3_reeval/metrics.json\\n/root/autodl-tmp/eval_results/sft_baseline_d076_reeval/metrics.json\\n/root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json\\n/root/autodl-tmp/eval_results/sft_no_evidence/metrics.json\\n/root/autodl-tmp/eval_results/sft_no_evidence_noquant/metrics.json\\n/root/autodl-tmp/eval_results/test_rsft_s44/metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 65_

`evi_f1_joint` 已经在大量 eval 中被计算。让我用一个脚本批量提取关键实验的对比数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "c03b7638-e77e-406a-b360-d00a9f5ce5f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4WreU8wQfuRsFKrmm9nam",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4312,
      "cache_read_input_tokens": 54063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4312
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 66_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Nk8Ba3vMF6P7AkDdXD74iA`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cd /root/autodl-tmp/eval_results && python3 -c \"\nimport json, os, glob\n\n# Key experiments to compare\nkey_exps = [\n    'sft_baseline_d076_reeval',\n    'sft_baseline_noquant',\n    'rsft_ced_s42_reeval',\n    'rsft_ced_s43',\n    'rsft_ced_s44_reeval',\n    'rsft_ced_s45',\n    'rsft_flat_nli_s43_reeval_r2',\n    'rsft_flat_nli_s44',\n    'rsft_flat_nli_s45',\n    'rsft_topk3_reeval',\n    'qwen3_1_7b_sft_eval',\n    'qwen3_8b_sft_eval',\n    'llama_3_1_8b_sft_eval',\n    'plan_006_qwen3_1_7b_rsft_eval_r2',\n    'plan_006_llama_rsft_r3_eval',\n    'dpo_ced_1ep_fixed',\n    'grpo_g8_bf16_ckpt100',\n    'plan_011_bf16_g8_step50',\n]\n\nprint(f\\\"{'Experiment':<40} {'F1':>6} {'Ign-F1':>7} {'evi_f1':>7} {'evi_f1_j':>9} {'EDCR':>6}\\\")\nprint('-' * 80)\n\nfor exp in key_exps:\n    path = f'{exp}/metrics.json'\n    if not os.path.exists(path):\n        continue\n    with open(path) as f:\n        m = json.load(f)\n    f1 = m.get('f1', 0)\n    ign = m.get('ign_f1', 0)\n    evi = m.get('evi_f1', 0)\n    evi_j = m.get('evi_f1_joint', 0)\n    edcr = m.get('edcr', 0)\n    print(f'{exp:<40} {f1:>6.4f} {ign:>7.4f} {evi:>7.4f} {evi_j:>9.4f} {edcr:>6.4f}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "5da08550-9231-439a-ab39-b4853986bc73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4WreU8wQfuRsFKrmm9nam",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4312,
      "cache_read_input_tokens": 54063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4312
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-17T12:58:31.154Z_

<details><summary>↩ Tool result · `toolu_01Nk8Ba3vMF6P7AkDdXD74iA`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/autodl-tmp/eval_results && python3 -c \\\"\\\\nimport json, os, glob\\\\n\\\\n# Key experiments to compare\\\\nkey_exps = [\\\\n    \\\\'sft_baseline_d076_reeval\\\\',\\\\n    \\\\'sft_baseline_noquant\\\\',\\\\n    \\\\'rsft_ced_s42_reeval\\\\',\\\\n    \\\\'rsft_ced_s43\\\\',\\\\n    \\\\'rsft_ced_s44_reeval\\\\',\\\\n    \\\\'rsft_ced_s45\\\\',\\\\n    \\\\'rsft_flat_nli_s43_reeval_r2\\\\',\\\\n    \\\\'rsft_flat_nli_s44\\\\',\\\\n    \\\\'rsft_flat_nli_s45\\\\',\\\\n    \\\\'rsft_topk3_reeval\\\\',\\\\n    \\\\'qwen3_1_7b_sft_eval\\\\',\\\\n    \\\\'qwen3_8b_sft_eval\\\\',\\\\n    \\\\'llama_3_1_8b_sft_eval\\\\',\\\\n    \\\\'plan_006_qwen3_1_7b_rsft_eval_r2\\\\',\\\\n    \\\\'plan_006_llama_rsft_r3_eval\\\\',\\\\n    \\\\'dpo_ced_1ep_fixed\\\\',\\\\n    \\\\'grpo_g8_bf16_ckpt100\\\\',\\\\n    \\\\'plan_011_bf16_g8_step50\\\\',\\\\n]\\\\n\\\\nprint(f\\\\\\\\\\\"{\\\\'Experiment\\\\':<40} {\\\\'F1\\\\':>6} {\\\\'Ign-F1\\\\':>7} {\\\\'evi_f1\\\\':>7} {\\\\'evi_f1_j\\\\':>9} {\\\\'EDCR\\\\':>6}\\\\\\\\\\\")\\\\nprint(\\\\'-\\\\' * 80)\\\\n\\\\nfor exp in key_exps:\\\\n    path = f\\\\'{exp}/metrics.json\\\\'\\\\n    if not os.path.exists(path):\\\\n        continue\\\\n    with open(path) as f:\\\\n        m = json.load(f)\\\\n    f1 = m.get(\\\\'f1\\\\', 0)\\\\n    ign = m.get(\\\\'ign_f1\\\\', 0)\\\\n    evi = m.get(\\\\'evi_f1\\\\', 0)\\\\n    evi_j = m.get(\\\\'evi_f1_joint\\\\', 0)\\\\n    edcr = m.get(\\\\'edcr\\\\', 0)\\\\n    print(f\\\\'{exp:<40} {f1:>6.4f} {ign:>7.4f} {evi:>7.4f} {evi_j:>9.4f} {edcr:>6.4f}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "0999d396-5395-4875-8929-d5f4d4ce0ec7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'cd /root/autodl-tmp/eval_results && python3 -c \\\\\\\"\\\\\\\\nimport json, os, glob\\\\\\\\n\\\\\\\\n# Key experiments to compare\\\\\\\\nkey_exps = [\\\\\\\\n    \\\\\\\\'sft_baseline_d076_reeval\\\\\\\\',\\\\\\\\n    \\\\\\\\'sft_baseline_noquant\\\\\\\\',\\\\\\\\n    \\\\\\\\'rsft_ced_s42_reeval\\\\\\\\',\\\\\\\\n    \\\\\\\\'rsft_ced_s43\\\\\\\\',\\\\\\\\n    \\\\\\\\'rsft_ced_s44_reeval\\\\\\\\',\\\\\\\\n    \\\\\\\\'rsft_ced_s45\\\\\\\\',\\\\\\\\n    \\\\\\\\'rsft_flat_nli_s43_reeval_r2\\\\\\\\',\\\\\\\\n    \\\\\\\\'rsft_flat_nli_s44\\\\\\\\',\\\\\\\\n    \\\\\\\\'rsft_flat_nli_s45\\\\\\\\',\\\\\\\\n    \\\\\\\\'rsft_topk3_reeval\\\\\\\\',\\\\\\\\n    \\\\\\\\'qwen3_1_7b_sft_eval\\\\\\\\',\\\\\\\\n    \\\\\\\\'qwen3_8b_sft_eval\\\\\\\\',\\\\\\\\n    \\\\\\\\'llama_3_1_8b_sft_eval\\\\\\\\',\\\\\\\\n    \\\\\\\\'plan_006_qwen3_1_7b_rsft_eval_r2\\\\\\\\',\\\\\\\\n    \\\\\\\\'plan_006_llama_rsft_r3_eval\\\\\\\\',\\\\\\\\n    \\\\\\\\'dpo_ced_1ep_fixed\\\\\\\\',\\\\\\\\n    \\\\\\\\'grpo_g8_bf16_ckpt100\\\\\\\\',\\\\\\\\n    \\\\\\\\'plan_011_bf16_g8_step50\\\\\\\\',\\\\\\\\n]\\\\\\\\n\\\\\\\\nprint(f\\\\\\\\\\\\\\\\\\\\\\\"{\\\\\\\\'Experiment\\\\\\\\':<40} {\\\\\\\\'F1\\\\\\\\':>6} {\\\\\\\\'Ign-F1\\\\\\\\':>7} {\\\\\\\\'evi_f1\\\\\\\\':>7} {\\\\\\\\'evi_f1_j\\\\\\\\':>9} {\\\\\\\\'EDCR\\\\\\\\':>6}\\\\\\\\\\\\\\\\\\\\\\\")\\\\\\\\nprint(\\\\\\\\'-\\\\\\\\' * 80)\\\\\\\\n\\\\\\\\nfor exp in key_exps:\\\\\\\\n    path = f\\\\\\\\'{exp}/metrics.json\\\\\\\\'\\\\\\\\n    if not os.path.exists(path):\\\\\\\\n        continue\\\\\\\\n    with open(path) as f:\\\\\\\\n        m = json.load(f)\\\\\\\\n    f1 = m.get(\\\\\\\\'f1\\\\\\\\', 0)\\\\\\\\n    ign = m.get(\\\\\\\\'ign_f1\\\\\\\\', 0)\\\\\\\\n    evi = m.get(\\\\\\\\'evi_f1\\\\\\\\', 0)\\\\\\\\n    evi_j = m.get(\\\\\\\\'evi_f1_joint\\\\\\\\', 0)\\\\\\\\n    edcr = m.get(\\\\\\\\'edcr\\\\\\\\', 0)\\\\\\\\n    print(f\\\\\\\\'{exp:<40} {f1:>6.4f} {ign:>7.4f} {evi:>7.4f} {evi_j:>9.4f} {edcr:>6.4f}\\\\\\\\')\\\\\\\\n\\\\\\\"\\\\\\\\n'\\\\n\\\\nExit code: 127\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\nbash: line 1: python3: command not found\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/autodl-tmp/eval_results && python3 -c \\\"\\\\nimport json, os, glob\\\\n\\\\n# Key experiments to compare\\\\nkey_exps = [\\\\n    \\\\'sft_baseline_d076_reeval\\\\',\\\\n    \\\\'sft_baseline_noquant\\\\',\\\\n    \\\\'rsft_ced_s42_reeval\\\\',\\\\n    \\\\'rsft_ced_s43\\\\',\\\\n    \\\\'rsft_ced_s44_reeval\\\\',\\\\n    \\\\'rsft_ced_s45\\\\',\\\\n    \\\\'rsft_flat_nli_s43_reeval_r2\\\\',\\\\n    \\\\'rsft_flat_nli_s44\\\\',\\\\n    \\\\'rsft_flat_nli_s45\\\\',\\\\n    \\\\'rsft_topk3_reeval\\\\',\\\\n    \\\\'qwen3_1_7b_sft_eval\\\\',\\\\n    \\\\'qwen3_8b_sft_eval\\\\',\\\\n    \\\\'llama_3_1_8b_sft_eval\\\\',\\\\n    \\\\'plan_006_qwen3_1_7b_rsft_eval_r2\\\\',\\\\n    \\\\'plan_006_llama_rsft_r3_eval\\\\',\\\\n    \\\\'dpo_ced_1ep_fixed\\\\',\\\\n    \\\\'grpo_g8_bf16_ckpt100\\\\',\\\\n    \\\\'plan_011_bf16_g8_step50\\\\',\\\\n]\\\\n\\\\nprint(f\\\\\\\\\\\"{\\\\'Experiment\\\\':<40} {\\\\'F1\\\\':>6} {\\\\'Ign-F1\\\\':>7} {\\\\'evi_f1\\\\':>7} {\\\\'evi_f1_j\\\\':>9} {\\\\'EDCR\\\\':>6}\\\\\\\\\\\")\\\\nprint(\\\\'-\\\\' * 80)\\\\n\\\\nfor exp in key_exps:\\\\n    path = f\\\\'{exp}/metrics.json\\\\'\\\\n    if not os.path.exists(path):\\\\n        continue\\\\n    with open(path) as f:\\\\n        m = json.load(f)\\\\n    f1 = m.get(\\\\'f1\\\\', 0)\\\\n    ign = m.get(\\\\'ign_f1\\\\', 0)\\\\n    evi = m.get(\\\\'evi_f1\\\\', 0)\\\\n    evi_j = m.get(\\\\'evi_f1_joint\\\\', 0)\\\\n    edcr = m.get(\\\\'edcr\\\\', 0)\\\\n    print(f\\\\'{exp:<40} {f1:>6.4f} {ign:>7.4f} {evi:>7.4f} {evi_j:>9.4f} {edcr:>6.4f}\\\\')\\\\n\\\"\\\\n'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 68_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01RjKyyAkPEJaQkkXoCnHM5K`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "which python",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "bcc86856-2fd4-4591-a332-fd795088d34c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwB2atsf6Vte8Zoz728j7P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1703,
      "cache_read_input_tokens": 58375,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1703
      },
      "output_tokens": 42,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-17T12:58:36.826Z_

<details><summary>↩ Tool result · `toolu_01RjKyyAkPEJaQkkXoCnHM5K`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'which python'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.91}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "7c8bed09-99ff-4bda-b5dc-425a5155ec39",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'which python'\\\\n\\\\nExit code: 1\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\n\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.91}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'which python'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.91}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 70_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01PfcAwfp6nHXQYKGy9mCAh8`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls /root/miniconda3/envs/*/bin/python 2>/dev/null || conda env list 2>/dev/null || ls /opt/conda/bin/python 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "a512f9a5-761d-42bd-a87b-d92260ac4e53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014nmNSMZNvsGWuQdPNeA5pn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 209,
      "cache_read_input_tokens": 60078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 209
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 71 · 2026-05-17T12:58:40.299Z_

<details><summary>↩ Tool result · `toolu_01PfcAwfp6nHXQYKGy9mCAh8`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'ls /root/miniconda3/envs/*/bin/python 2>/dev/null || conda env list 2>/dev/null || ls /opt/conda/bin/python 2>/dev/null'\\n\\nExit code: 2\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.66}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "699eeab8-d7f9-46b6-bda7-3c11d9b97237",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Encountered a bad command exit code!\\\\n\\\\nCommand: 'ls /root/miniconda3/envs/*/bin/python 2>/dev/null || conda env list 2>/dev/null || ls /opt/conda/bin/python 2>/dev/null'\\\\n\\\\nExit code: 2\\\\n\\\\nStdout:\\\\n\\\\n\\\\n\\\\nStderr:\\\\n\\\\n\\\\n\\\\n\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.66}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'ls /root/miniconda3/envs/*/bin/python 2>/dev/null || conda env list 2>/dev/null || ls /opt/conda/bin/python 2>/dev/null'\\n\\nExit code: 2\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.66}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01XCCYzvmDKZ6Snb7DkaVAXH`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root -name \"python\" -type f -maxdepth 5",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "d1e36afa-4111-4fc6-a8a9-473625842762",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132jJSkNBPe1YfYJ14WjzeM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 301,
      "cache_read_input_tokens": 60287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 301
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-17T12:58:43.283Z_

<details><summary>↩ Tool result · `toolu_01XCCYzvmDKZ6Snb7DkaVAXH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "c8467d79-788f-4eac-90c8-514d1008412f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.7}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 74_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_019jV6DQvC3aUBnbTncPwg5o`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find / -name \"python*\" -type f -maxdepth 4 -executable",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "6aacbbfa-2cac-4bf1-86e9-3138aa89faad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kgcp2EVMySkwUnanDo7F7b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 194,
      "cache_read_input_tokens": 60588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 194
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-17T12:58:46.194Z_

<details><summary>↩ Tool result · `toolu_019jV6DQvC3aUBnbTncPwg5o`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "ecdd004c-dc9c-4ddb-be71-f34515110b44",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/miniconda3/bin/python3.12\\\\n/root/miniconda3/bin/python3.12-config\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3.12\\n/root/miniconda3/bin/python3.12-config\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 76_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01RPy1hy1Vsu2sojqe66EB6T`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cd /root/autodl-tmp/eval_results && /root/miniconda3/bin/python3.12 -c \"\nimport json, os\n\nkey_exps = [\n    'sft_baseline_d076_reeval',\n    'rsft_ced_s42_reeval',\n    'rsft_ced_s43',\n    'rsft_ced_s44_reeval',\n    'rsft_ced_s45',\n    'rsft_flat_nli_s43_reeval_r2',\n    'rsft_flat_nli_s44',\n    'rsft_flat_nli_s45',\n    'rsft_topk3_reeval',\n    'qwen3_1_7b_sft_eval',\n    'qwen3_8b_sft_eval',\n    'llama_3_1_8b_sft_eval',\n    'plan_006_qwen3_1_7b_rsft_eval_r2',\n    'plan_006_llama_rsft_r3_eval',\n    'dpo_ced_1ep_fixed',\n    'grpo_g8_bf16_ckpt100',\n    'plan_011_bf16_g8_step50',\n]\n\nheader = f\\\"{'Experiment':<40} {'F1':>6} {'IgnF1':>6} {'evF1':>6} {'evF1_j':>6} {'EDCR':>6}\\\"\nprint(header)\nprint('-' * len(header))\n\nfor exp in key_exps:\n    path = f'{exp}/metrics.json'\n    if not os.path.exists(path):\n        continue\n    with open(path) as f:\n        m = json.load(f)\n    f1 = m.get('f1', 0)\n    ign = m.get('ign_f1', 0)\n    evi = m.get('evi_f1', 0)\n    evi_j = m.get('evi_f1_joint', 0) or 0\n    edcr = m.get('edcr', 0)\n    print(f'{exp:<40} {f1:.4f} {ign:.4f} {evi:.4f} {evi_j:.4f} {edcr:.4f}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "5c24ca84-5af6-4652-b776-b73b013f3145",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvMtwq1i2LpQp5je52Dxtt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 231,
      "cache_read_input_tokens": 60782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 231
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-17T12:58:59.310Z_

<details><summary>↩ Tool result · `toolu_01RPy1hy1Vsu2sojqe66EB6T`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Experiment                                   F1  IgnF1   evF1 evF1_j   EDCR\\n---------------------------------------------------------------------------\\nsft_baseline_d076_reeval                 0.4049 0.3974 0.7986 0.3147 0.6982\\nrsft_ced_s42_reeval                      0.4517 0.4423 0.8174 0.3518 0.6569\\nrsft_ced_s43                             0.4601 0.4512 0.8063 0.3605 0.6542\\nrsft_ced_s44_reeval                      0.4621 0.4511 0.8050 0.3677 0.6350\\nrsft_ced_s45                             0.4514 0.4416 0.8174 0.3558 0.6550\\nrsft_flat_nli_s43_reeval_r2              0.4586 0.4503 0.8113 0.3580 0.6552\\nrsft_flat_nli_s44                        0.4615 0.4615 0.8131 0.3597 0.6458\\nrsft_flat_nli_s45                        0.4551 0.4551 0.8154 0.3556 0.6521\\nrsft_topk3_reeval                        0.4454 0.4454 0.8088 0.3478 0.6635\\nqwen3_1_7b_sft_eval                      0.4945 0.4786 0.8316 0.3958 0.6704\\nqwen3_8b_sft_eval                        0.5262 0.5051 0.8188 0.4139 0.6510\\nllama_3_1_8b_sft_eval                    0.5514 0.5384 0.8151 0.4317 0.6280\\nplan_006_qwen3_1_7b_rsft_eval_r2         0.5219 0.5050 0.8309 0.4223 0.6297\\nplan_006_llama_rsft_r3_eval              0.5674 0.5563 0.8255 0.4571 0.5856\\ndpo_ced_1ep_fixed                        0.4034 0.4034 0.8088 0.3069 0.7139\\ngrpo_g8_bf16_ckpt100                     0.4549 0.4549 0.8086 0.3571 0.6318\\nplan_011_bf16_g8_step50                  0.4276 0.4276 0.8024 0.3300 0.6855\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "8d156e3b-ee62-4960-acf5-21da63130340",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Experiment                                   F1  IgnF1   evF1 evF1_j   EDCR\\\\n---------------------------------------------------------------------------\\\\nsft_baseline_d076_reeval                 0.4049 0.3974 0.7986 0.3147 0.6982\\\\nrsft_ced_s42_reeval                      0.4517 0.4423 0.8174 0.3518 0.6569\\\\nrsft_ced_s43                             0.4601 0.4512 0.8063 0.3605 0.6542\\\\nrsft_ced_s44_reeval                      0.4621 0.4511 0.8050 0.3677 0.6350\\\\nrsft_ced_s45                             0.4514 0.4416 0.8174 0.3558 0.6550\\\\nrsft_flat_nli_s43_reeval_r2              0.4586 0.4503 0.8113 0.3580 0.6552\\\\nrsft_flat_nli_s44                        0.4615 0.4615 0.8131 0.3597 0.6458\\\\nrsft_flat_nli_s45                        0.4551 0.4551 0.8154 0.3556 0.6521\\\\nrsft_topk3_reeval                        0.4454 0.4454 0.8088 0.3478 0.6635\\\\nqwen3_1_7b_sft_eval                      0.4945 0.4786 0.8316 0.3958 0.6704\\\\nqwen3_8b_sft_eval                        0.5262 0.5051 0.8188 0.4139 0.6510\\\\nllama_3_1_8b_sft_eval                    0.5514 0.5384 0.8151 0.4317 0.6280\\\\nplan_006_qwen3_1_7b_rsft_eval_r2         0.5219 0.5050 0.8309 0.4223 0.6297\\\\nplan_006_llama_rsft_r3_eval              0.5674 0.5563 0.8255 0.4571 0.5856\\\\ndpo_ced_1ep_fixed                        0.4034 0.4034 0.8088 0.3069 0.7139\\\\ngrpo_g8_bf16_ckpt100                     0.4549 0.4549 0.8086 0.3571 0.6318\\\\nplan_011_bf16_g8_step50                  0.4276 0.4276 0.8024 0.3300 0.6855\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.34}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Experiment                                   F1  IgnF1   evF1 evF1_j   EDCR\\n---------------------------------------------------------------------------\\nsft_baseline_d076_reeval                 0.4049 0.3974 0.7986 0.3147 0.6982\\nrsft_ced_s42_reeval                      0.4517 0.4423 0.8174 0.3518 0.6569\\nrsft_ced_s43                             0.4601 0.4512 0.8063 0.3605 0.6542\\nrsft_ced_s44_reeval                      0.4621 0.4511 0.8050 0.3677 0.6350\\nrsft_ced_s45                             0.4514 0.4416 0.8174 0.3558 0.6550\\nrsft_flat_nli_s43_reeval_r2              0.4586 0.4503 0.8113 0.3580 0.6552\\nrsft_flat_nli_s44                        0.4615 0.4615 0.8131 0.3597 0.6458\\nrsft_flat_nli_s45                        0.4551 0.4551 0.8154 0.3556 0.6521\\nrsft_topk3_reeval                        0.4454 0.4454 0.8088 0.3478 0.6635\\nqwen3_1_7b_sft_eval                      0.4945 0.4786 0.8316 0.3958 0.6704\\nqwen3_8b_sft_eval                        0.5262 0.5051 0.8188 0.4139 0.6510\\nllama_3_1_8b_sft_eval                    0.5514 0.5384 0.8151 0.4317 0.6280\\nplan_006_qwen3_1_7b_rsft_eval_r2         0.5219 0.5050 0.8309 0.4223 0.6297\\nplan_006_llama_rsft_r3_eval              0.5674 0.5563 0.8255 0.4571 0.5856\\ndpo_ced_1ep_fixed                        0.4034 0.4034 0.8088 0.3069 0.7139\\ngrpo_g8_bf16_ckpt100                     0.4549 0.4549 0.8086 0.3571 0.6318\\nplan_011_bf16_g8_step50                  0.4276 0.4276 0.8024 0.3300 0.6855\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 78_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have a comprehensive picture. Let me also check the DREEAM baseline result for comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "e5974a87-2f1d-48e7-a57d-b7607bc06df5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aa3DwYs2i9K8dVqCD25277",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 61013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1464
      },
      "output_tokens": 20,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 79_

数据非常清晰。现在验证 DREEAM baseline 结果的完整指标。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "07941d60-6142-4cb6-81ad-1fc35de54840",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aa3DwYs2i9K8dVqCD25277",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 61013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1464
      },
      "output_tokens": 20,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 80_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014nXjxr7S6DscrMqpqLPUwJ`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp -path \"*dreeam*\" -name \"*.log\" -o -path \"*dreeam*\" -name \"*.txt\" -o -path \"*dreeam*\" -name \"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "09842b99-3586-4d9b-9aff-d758a923f544",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Aa3DwYs2i9K8dVqCD25277",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 61013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1464
      },
      "output_tokens": 20,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-17T12:59:05.742Z_

<details><summary>↩ Tool result · `toolu_014nXjxr7S6DscrMqpqLPUwJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/baselines/dreeam/requirements.txt\\n/root/autodl-tmp/baselines/dreeam/dataset/docred/dev.json\\n/root/autodl-tmp/baselines/dreeam/dataset/docred/test.json\\n/root/autodl-tmp/baselines/dreeam/dataset/docred/train_annotated.json\\n/root/autodl-tmp/baselines/dreeam/dataset/docred/train_distant.json\\n/root/autodl-tmp/baselines/dreeam/meta/rel2id.json\\n/root/autodl-tmp/baselines/dreeam/meta/rel_info.json\\n/root/autodl-tmp/baselines/dreeam/train_teacher.log\\n/root/autodl-tmp/baselines/dreeam/checkpoints/teacher_roberta/2026-05-15_22:29:42.720935/results.json\\n/root/autodl-tmp/baselines/dreeam/checkpoints/teacher_roberta/2026-05-15_22:29:42.720935/topk_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "e8a4169c-143f-4a1d-b6cb-ba1e63bdfdf5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/baselines/dreeam/requirements.txt\\\\n/root/autodl-tmp/baselines/dreeam/dataset/docred/dev.json\\\\n/root/autodl-tmp/baselines/dreeam/dataset/docred/test.json\\\\n/root/autodl-tmp/baselines/dreeam/dataset/docred/train_annotated.json\\\\n/root/autodl-tmp/baselines/dreeam/dataset/docred/train_distant.json\\\\n/root/autodl-tmp/baselines/dreeam/meta/rel2id.json\\\\n/root/autodl-tmp/baselines/dreeam/meta/rel_info.json\\\\n/root/autodl-tmp/baselines/dreeam/train_teacher.log\\\\n/root/autodl-tmp/baselines/dreeam/checkpoints/teacher_roberta/2026-05-15_22:29:42.720935/results.json\\\\n/root/autodl-tmp/baselines/dreeam/checkpoints/teacher_roberta/2026-05-15_22:29:42.720935/topk_results.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/baselines/dreeam/requirements.txt\\n/root/autodl-tmp/baselines/dreeam/dataset/docred/dev.json\\n/root/autodl-tmp/baselines/dreeam/dataset/docred/test.json\\n/root/autodl-tmp/baselines/dreeam/dataset/docred/train_annotated.json\\n/root/autodl-tmp/baselines/dreeam/dataset/docred/train_distant.json\\n/root/autodl-tmp/baselines/dreeam/meta/rel2id.json\\n/root/autodl-tmp/baselines/dreeam/meta/rel_info.json\\n/root/autodl-tmp/baselines/dreeam/train_teacher.log\\n/root/autodl-tmp/baselines/dreeam/checkpoints/teacher_roberta/2026-05-15_22:29:42.720935/results.json\\n/root/autodl-tmp/baselines/dreeam/checkpoints/teacher_roberta/2026-05-15_22:29:42.720935/topk_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 82_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Bpci8saGWYSpPGzAVQdBAw`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/baselines/dreeam/checkpoints/teacher_roberta/2026-05-15_22:29:42.720935/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "87f770eb-6b4a-4652-b9de-061b65caaad3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgANEdWLAYk1riwiqQSC5B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 583,
      "cache_read_input_tokens": 62477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 583
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 83_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NtB4FL1WrrXkjjMXhPRWMs`</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/baselines/dreeam/checkpoints/teacher_roberta/2026-05-15_22:29:42.720935/topk_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "d0d08974-aefd-4ff6-a11c-208d064fc874",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EgANEdWLAYk1riwiqQSC5B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 583,
      "cache_read_input_tokens": 62477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 583
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 84 · 2026-05-17T12:59:09.524Z_

<details><summary>↩ Tool result · `toolu_01Bpci8saGWYSpPGzAVQdBAw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"[{\\\"title\\\":\\\"(I Am) The Seeker\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0],\\\"score\\\":3.697967529296875},{\\\"title\\\":\\\"(I Am) The Seeker\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":2,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":0.9657421112060547},{\\\"title\\\":\\\"(I Am) The Seeker\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":3,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":4.566144943237305},{\\\"title\\\":\\\"(I Am) The Seeker\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"P463\\\",\\\"evidence\\\":[0],\\\"score\\\":6.548666000366211},{\\\"title\\\":\\\"(I Am) The Seeker\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":1,\\\"r\\\":\\\"P463\\\",\\\"evidence\\\":[0],\\\"score\\\":8.283491134643555},{\\\"title\\\":\\\"(I Am) The Seeker\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":1,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.2059154510498047},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0],\\\"score\\\":9.141313552856445},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[0,1],\\\"score\\\":15.964946746826172},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":9.165733337402344},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0],\\\"score\\\":0.8681507110595703},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":13,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[4],\\\"score\\\":7.137664794921875},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":20,\\\"t_idx\\\":2,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0,6],\\\"score\\\":9.847187042236328},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":20,\\\"t_idx\\\":3,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[6],\\\"score\\\":7.742105484008789},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":20,\\\"t_idx\\\":4,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,6],\\\"score\\\":2.56552791595459},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":21,\\\"t_idx\\\":0,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0,6],\\\"score\\\":3.1435604095458984},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":21,\\\"t_idx\\\":2,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0,6],\\\"score\\\":7.491684913635254},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":21,\\\"t_idx\\\":3,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[0,6],\\\"score\\\":8.685039520263672},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":21,\\\"t_idx\\\":4,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1,6],\\\"score\\\":6.0979204177856445},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":22,\\\"t_idx\\\":2,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0,6],\\\"score\\\":4.051787376403809},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":22,\\\"t_idx\\\":3,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[1,6],\\\"score\\\":5.057645797729492},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":22,\\\"t_idx\\\":4,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[1,6],\\\"score\\\":3.568121910095215},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":23,\\\"t_idx\\\":2,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0,6],\\\"score\\\":9.088576316833496},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":23,\\\"t_idx\\\":3,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[6],\\\"score\\\":1.7855348587036133},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":23,\\\"t_idx\\\":4,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[6],\\\"score\\\":2.4017333984375},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":24,\\\"t_idx\\\":2,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0,6],\\\"score\\\":6.335969924926758},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":24,\\\"t_idx\\\":4,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[6],\\\"score\\\":3.3533220291137695},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":0,\\\"r\\\":\\\"P50\\\",\\\"evidence\\\":[0],\\\"score\\\":11.554618835449219},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":12,\\\"r\\\":\\\"P50\\\",\\\"evidence\\\":[0],\\\"score\\\":0.8883247375488281},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":17,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[6],\\\"score\\\":7.376331329345703},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":18,\\\"r\\\":\\\"P123\\\",\\\"evidence\\\":[0,6],\\\"score\\\":5.969117164611816},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":3,\\\"r\\\":\\\"P710\\\",\\\"evidence\\\":[0],\\\"score\\\":0.7415056228637695},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":5,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0],\\\"score\\\":0.7725467681884766},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":7,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":4.964677810668945},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":7,\\\"r\\\":\\\"P607\\\",\\\"evidence\\\":[0],\\\"score\\\":1.9792919158935547},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":6,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":8.417366027832031},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":7,\\\"r\\\":\\\"P607\\\",\\\"evidence\\\":[1],\\\"score\\\":16.68253517150879},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":7,\\\"r\\\":\\\"P607\\\",\\\"evidence\\\":[0,1],\\\"sco\\n\\n... [截断: 输出过长，省略 1164086 字符] ...\\n\\n\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":7.484807968139648},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1],\\\"score\\\":9.756553649902344},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":9,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,1],\\\"score\\\":6.396303176879883},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":11,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[2,3],\\\"score\\\":6.048531532287598},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":3,\\\"r\\\":\\\"P118\\\",\\\"evidence\\\":[0],\\\"score\\\":9.594766616821289},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":7,\\\"r\\\":\\\"P118\\\",\\\"evidence\\\":[1],\\\"score\\\":4.330738067626953},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":2,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[1],\\\"score\\\":3.1826248168945312},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[1],\\\"score\\\":10.465694427490234},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":2,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,1],\\\"score\\\":1.392085075378418},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":4,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":0.4117765426635742},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":5,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1],\\\"score\\\":7.184945106506348},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":9,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,1],\\\"score\\\":5.0524444580078125},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":11,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[2,3],\\\"score\\\":3.5564842224121094},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[2,3],\\\"score\\\":4.317239761352539},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":11,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[2,3],\\\"score\\\":1.8771638870239258},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":2,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[4],\\\"score\\\":0.4242515563964844},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[4],\\\"score\\\":8.229376792907715},{\\\"title\\\":\\\"\\\\u00c9amon \\\\u00d3 Cu\\\\u00edv\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":17.39966583251953},{\\\"title\\\":\\\"\\\\u00c9amon \\\\u00d3 Cu\\\\u00edv\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"P102\\\",\\\"evidence\\\":[0,5],\\\"score\\\":7.914501190185547},{\\\"title\\\":\\\"\\\\u00c9amon \\\\u00d3 Cu\\\\u00edv\\\",\\\"h_idx\\\":21,\\\"t_idx\\\":3,\\\"r\\\":\\\"P102\\\",\\\"evidence\\\":[3],\\\"score\\\":4.60417366027832},{\\\"title\\\":\\\"\\\\u00c9amon \\\\u00d3 Cu\\\\u00edv\\\",\\\"h_idx\\\":23,\\\"t_idx\\\":3,\\\"r\\\":\\\"P102\\\",\\\"evidence\\\":[4],\\\"score\\\":6.951519012451172},{\\\"title\\\":\\\"\\\\u00c9cole des officiers de la gendarmerie nationale\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0],\\\"score\\\":13.789529800415039},{\\\"title\\\":\\\"\\\\u00c9cole des officiers de la gendarmerie nationale\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":13,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[2,5],\\\"score\\\":1.4925498962402344},{\\\"title\\\":\\\"\\\\u00c9cole des officiers de la gendarmerie nationale\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":7,\\\"r\\\":\\\"P155\\\",\\\"evidence\\\":[2,5],\\\"score\\\":4.045356750488281},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":16.1859188079834},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,5],\\\"score\\\":5.842049598693848},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,2],\\\"score\\\":12.17776107788086},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":15.380714416503906},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":13.253593444824219},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":6,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,1,4],\\\"score\\\":9.252944946289062},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":7,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":12.900182723999023},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":10,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[2],\\\"score\\\":0.6088094711303711},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":13,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[2],\\\"score\\\":11.361888885498047},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":5,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[3],\\\"score\\\":8.67984390258789}]\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.85}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "8f79d011-ae35-49ce-9e4a-264d91555115",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"[{\\\\\\\"title\\\\\\\":\\\\\\\"(I Am) The Seeker\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":1,\\\\\\\"r\\\\\\\":\\\\\\\"P175\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":3.697967529296875},{\\\\\\\"title\\\\\\\":\\\\\\\"(I Am) The Seeker\\\\\\\",\\\\\\\"h_idx\\\\\\\":1,\\\\\\\"t_idx\\\\\\\":2,\\\\\\\"r\\\\\\\":\\\\\\\"P527\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":0.9657421112060547},{\\\\\\\"title\\\\\\\":\\\\\\\"(I Am) The Seeker\\\\\\\",\\\\\\\"h_idx\\\\\\\":1,\\\\\\\"t_idx\\\\\\\":3,\\\\\\\"r\\\\\\\":\\\\\\\"P527\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":4.566144943237305},{\\\\\\\"title\\\\\\\":\\\\\\\"(I Am) The Seeker\\\\\\\",\\\\\\\"h_idx\\\\\\\":2,\\\\\\\"t_idx\\\\\\\":1,\\\\\\\"r\\\\\\\":\\\\\\\"P463\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":6.548666000366211},{\\\\\\\"title\\\\\\\":\\\\\\\"(I Am) The Seeker\\\\\\\",\\\\\\\"h_idx\\\\\\\":3,\\\\\\\"t_idx\\\\\\\":1,\\\\\\\"r\\\\\\\":\\\\\\\"P463\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":8.283491134643555},{\\\\\\\"title\\\\\\\":\\\\\\\"(I Am) The Seeker\\\\\\\",\\\\\\\"h_idx\\\\\\\":14,\\\\\\\"t_idx\\\\\\\":1,\\\\\\\"r\\\\\\\":\\\\\\\"P175\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,1],\\\\\\\"score\\\\\\\":0.2059154510498047},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":2,\\\\\\\"r\\\\\\\":\\\\\\\"P175\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":9.141313552856445},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":3,\\\\\\\"r\\\\\\\":\\\\\\\"P577\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,1],\\\\\\\"score\\\\\\\":15.964946746826172},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":4,\\\\\\\"r\\\\\\\":\\\\\\\"P264\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,1],\\\\\\\"score\\\\\\\":9.165733337402344},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":2,\\\\\\\"t_idx\\\\\\\":1,\\\\\\\"r\\\\\\\":\\\\\\\"P27\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":0.8681507110595703},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":12,\\\\\\\"t_idx\\\\\\\":13,\\\\\\\"r\\\\\\\":\\\\\\\"P527\\\\\\\",\\\\\\\"evidence\\\\\\\":[4],\\\\\\\"score\\\\\\\":7.137664794921875},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":20,\\\\\\\"t_idx\\\\\\\":2,\\\\\\\"r\\\\\\\":\\\\\\\"P175\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,6],\\\\\\\"score\\\\\\\":9.847187042236328},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":20,\\\\\\\"t_idx\\\\\\\":3,\\\\\\\"r\\\\\\\":\\\\\\\"P577\\\\\\\",\\\\\\\"evidence\\\\\\\":[6],\\\\\\\"score\\\\\\\":7.742105484008789},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":20,\\\\\\\"t_idx\\\\\\\":4,\\\\\\\"r\\\\\\\":\\\\\\\"P264\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,6],\\\\\\\"score\\\\\\\":2.56552791595459},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":21,\\\\\\\"t_idx\\\\\\\":0,\\\\\\\"r\\\\\\\":\\\\\\\"P361\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,6],\\\\\\\"score\\\\\\\":3.1435604095458984},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":21,\\\\\\\"t_idx\\\\\\\":2,\\\\\\\"r\\\\\\\":\\\\\\\"P175\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,6],\\\\\\\"score\\\\\\\":7.491684913635254},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":21,\\\\\\\"t_idx\\\\\\\":3,\\\\\\\"r\\\\\\\":\\\\\\\"P577\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,6],\\\\\\\"score\\\\\\\":8.685039520263672},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":21,\\\\\\\"t_idx\\\\\\\":4,\\\\\\\"r\\\\\\\":\\\\\\\"P264\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,1,6],\\\\\\\"score\\\\\\\":6.0979204177856445},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":22,\\\\\\\"t_idx\\\\\\\":2,\\\\\\\"r\\\\\\\":\\\\\\\"P175\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,6],\\\\\\\"score\\\\\\\":4.051787376403809},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":22,\\\\\\\"t_idx\\\\\\\":3,\\\\\\\"r\\\\\\\":\\\\\\\"P577\\\\\\\",\\\\\\\"evidence\\\\\\\":[1,6],\\\\\\\"score\\\\\\\":5.057645797729492},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":22,\\\\\\\"t_idx\\\\\\\":4,\\\\\\\"r\\\\\\\":\\\\\\\"P264\\\\\\\",\\\\\\\"evidence\\\\\\\":[1,6],\\\\\\\"score\\\\\\\":3.568121910095215},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":23,\\\\\\\"t_idx\\\\\\\":2,\\\\\\\"r\\\\\\\":\\\\\\\"P175\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,6],\\\\\\\"score\\\\\\\":9.088576316833496},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":23,\\\\\\\"t_idx\\\\\\\":3,\\\\\\\"r\\\\\\\":\\\\\\\"P577\\\\\\\",\\\\\\\"evidence\\\\\\\":[6],\\\\\\\"score\\\\\\\":1.7855348587036133},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":23,\\\\\\\"t_idx\\\\\\\":4,\\\\\\\"r\\\\\\\":\\\\\\\"P264\\\\\\\",\\\\\\\"evidence\\\\\\\":[6],\\\\\\\"score\\\\\\\":2.4017333984375},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":24,\\\\\\\"t_idx\\\\\\\":2,\\\\\\\"r\\\\\\\":\\\\\\\"P175\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,6],\\\\\\\"score\\\\\\\":6.335969924926758},{\\\\\\\"title\\\\\\\":\\\\\\\"...Nothing Like the Sun\\\\\\\",\\\\\\\"h_idx\\\\\\\":24,\\\\\\\"t_idx\\\\\\\":4,\\\\\\\"r\\\\\\\":\\\\\\\"P264\\\\\\\",\\\\\\\"evidence\\\\\\\":[6],\\\\\\\"score\\\\\\\":3.3533220291137695},{\\\\\\\"title\\\\\\\":\\\\\\\"A Bridge Too Far (book)\\\\\\\",\\\\\\\"h_idx\\\\\\\":1,\\\\\\\"t_idx\\\\\\\":0,\\\\\\\"r\\\\\\\":\\\\\\\"P50\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":11.554618835449219},{\\\\\\\"title\\\\\\\":\\\\\\\"A Bridge Too Far (book)\\\\\\\",\\\\\\\"h_idx\\\\\\\":1,\\\\\\\"t_idx\\\\\\\":12,\\\\\\\"r\\\\\\\":\\\\\\\"P50\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":0.8883247375488281},{\\\\\\\"title\\\\\\\":\\\\\\\"A Bridge Too Far (book)\\\\\\\",\\\\\\\"h_idx\\\\\\\":1,\\\\\\\"t_idx\\\\\\\":17,\\\\\\\"r\\\\\\\":\\\\\\\"P577\\\\\\\",\\\\\\\"evidence\\\\\\\":[6],\\\\\\\"score\\\\\\\":7.376331329345703},{\\\\\\\"title\\\\\\\":\\\\\\\"A Bridge Too Far (book)\\\\\\\",\\\\\\\"h_idx\\\\\\\":1,\\\\\\\"t_idx\\\\\\\":18,\\\\\\\"r\\\\\\\":\\\\\\\"P123\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,6],\\\\\\\"score\\\\\\\":5.969117164611816},{\\\\\\\"title\\\\\\\":\\\\\\\"A Bridge Too Far (book)\\\\\\\",\\\\\\\"h_idx\\\\\\\":2,\\\\\\\"t_idx\\\\\\\":3,\\\\\\\"r\\\\\\\":\\\\\\\"P710\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":0.7415056228637695},{\\\\\\\"title\\\\\\\":\\\\\\\"A Bridge Too Far (book)\\\\\\\",\\\\\\\"h_idx\\\\\\\":2,\\\\\\\"t_idx\\\\\\\":5,\\\\\\\"r\\\\\\\":\\\\\\\"P276\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":0.7725467681884766},{\\\\\\\"title\\\\\\\":\\\\\\\"A Bridge Too Far (book)\\\\\\\",\\\\\\\"h_idx\\\\\\\":2,\\\\\\\"t_idx\\\\\\\":7,\\\\\\\"r\\\\\\\":\\\\\\\"P361\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":4.964677810668945},{\\\\\\\"title\\\\\\\":\\\\\\\"A Bridge Too Far (book)\\\\\\\",\\\\\\\"h_idx\\\\\\\":3,\\\\\\\"t_idx\\\\\\\":7,\\\\\\\"r\\\\\\\":\\\\\\\"P607\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":1.9792919158935547},{\\\\\\\"title\\\\\\\":\\\\\\\"A Bridge Too Far (book)\\\\\\\",\\\\\\\"h_idx\\\\\\\":5,\\\\\\\"t_idx\\\\\\\":6,\\\\\\\"r\\\\\\\":\\\\\\\"P17\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":8.417366027832031},{\\\\\\\"title\\\\\\\":\\\\\\\"A Bridge Too Far (book)\\\\\\\",\\\\\\\"h_idx\\\\\\\":9,\\\\\\\"t_idx\\\\\\\":7,\\\\\\\"r\\\\\\\":\\\\\\\"P607\\\\\\\",\\\\\\\"evidence\\\\\\\":[1],\\\\\\\"score\\\\\\\":16.68253517150879},{\\\\\\\"title\\\\\\\":\\\\\\\"A Bridge Too Far (book)\\\\\\\",\\\\\\\"h_idx\\\\\\\":10,\\\\\\\"t_idx\\\\\\\":7,\\\\\\\"r\\\\\\\":\\\\\\\"P607\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,1],\\\\\\\"sco\\\\n\\\\n... [截断: 输出过长，省略 1164086 字符] ...\\\\n\\\\n\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":4,\\\\\\\"r\\\\\\\":\\\\\\\"P54\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":7.484807968139648},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":5,\\\\\\\"r\\\\\\\":\\\\\\\"P54\\\\\\\",\\\\\\\"evidence\\\\\\\":[1],\\\\\\\"score\\\\\\\":9.756553649902344},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":9,\\\\\\\"r\\\\\\\":\\\\\\\"P27\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,1],\\\\\\\"score\\\\\\\":6.396303176879883},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":11,\\\\\\\"r\\\\\\\":\\\\\\\"P54\\\\\\\",\\\\\\\"evidence\\\\\\\":[2,3],\\\\\\\"score\\\\\\\":6.048531532287598},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":4,\\\\\\\"t_idx\\\\\\\":3,\\\\\\\"r\\\\\\\":\\\\\\\"P118\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":9.594766616821289},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":5,\\\\\\\"t_idx\\\\\\\":7,\\\\\\\"r\\\\\\\":\\\\\\\"P118\\\\\\\",\\\\\\\"evidence\\\\\\\":[1],\\\\\\\"score\\\\\\\":4.330738067626953},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":8,\\\\\\\"t_idx\\\\\\\":2,\\\\\\\"r\\\\\\\":\\\\\\\"P17\\\\\\\",\\\\\\\"evidence\\\\\\\":[1],\\\\\\\"score\\\\\\\":3.1826248168945312},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":8,\\\\\\\"t_idx\\\\\\\":9,\\\\\\\"r\\\\\\\":\\\\\\\"P17\\\\\\\",\\\\\\\"evidence\\\\\\\":[1],\\\\\\\"score\\\\\\\":10.465694427490234},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":10,\\\\\\\"t_idx\\\\\\\":2,\\\\\\\"r\\\\\\\":\\\\\\\"P27\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,1],\\\\\\\"score\\\\\\\":1.392085075378418},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":10,\\\\\\\"t_idx\\\\\\\":4,\\\\\\\"r\\\\\\\":\\\\\\\"P54\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":0.4117765426635742},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":10,\\\\\\\"t_idx\\\\\\\":5,\\\\\\\"r\\\\\\\":\\\\\\\"P54\\\\\\\",\\\\\\\"evidence\\\\\\\":[1],\\\\\\\"score\\\\\\\":7.184945106506348},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":10,\\\\\\\"t_idx\\\\\\\":9,\\\\\\\"r\\\\\\\":\\\\\\\"P27\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,1],\\\\\\\"score\\\\\\\":5.0524444580078125},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":10,\\\\\\\"t_idx\\\\\\\":11,\\\\\\\"r\\\\\\\":\\\\\\\"P54\\\\\\\",\\\\\\\"evidence\\\\\\\":[2,3],\\\\\\\"score\\\\\\\":3.5564842224121094},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":11,\\\\\\\"t_idx\\\\\\\":9,\\\\\\\"r\\\\\\\":\\\\\\\"P17\\\\\\\",\\\\\\\"evidence\\\\\\\":[2,3],\\\\\\\"score\\\\\\\":4.317239761352539},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":13,\\\\\\\"t_idx\\\\\\\":11,\\\\\\\"r\\\\\\\":\\\\\\\"P54\\\\\\\",\\\\\\\"evidence\\\\\\\":[2,3],\\\\\\\"score\\\\\\\":1.8771638870239258},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":15,\\\\\\\"t_idx\\\\\\\":2,\\\\\\\"r\\\\\\\":\\\\\\\"P17\\\\\\\",\\\\\\\"evidence\\\\\\\":[4],\\\\\\\"score\\\\\\\":0.4242515563964844},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c7a\\\\\\\\u011flar S\\\\\\\\u00f6y\\\\\\\\u00fcnc\\\\\\\\u00fc\\\\\\\",\\\\\\\"h_idx\\\\\\\":15,\\\\\\\"t_idx\\\\\\\":9,\\\\\\\"r\\\\\\\":\\\\\\\"P17\\\\\\\",\\\\\\\"evidence\\\\\\\":[4],\\\\\\\"score\\\\\\\":8.229376792907715},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c9amon \\\\\\\\u00d3 Cu\\\\\\\\u00edv\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":1,\\\\\\\"r\\\\\\\":\\\\\\\"P569\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":17.39966583251953},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c9amon \\\\\\\\u00d3 Cu\\\\\\\\u00edv\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":3,\\\\\\\"r\\\\\\\":\\\\\\\"P102\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,5],\\\\\\\"score\\\\\\\":7.914501190185547},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c9amon \\\\\\\\u00d3 Cu\\\\\\\\u00edv\\\\\\\",\\\\\\\"h_idx\\\\\\\":21,\\\\\\\"t_idx\\\\\\\":3,\\\\\\\"r\\\\\\\":\\\\\\\"P102\\\\\\\",\\\\\\\"evidence\\\\\\\":[3],\\\\\\\"score\\\\\\\":4.60417366027832},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c9amon \\\\\\\\u00d3 Cu\\\\\\\\u00edv\\\\\\\",\\\\\\\"h_idx\\\\\\\":23,\\\\\\\"t_idx\\\\\\\":3,\\\\\\\"r\\\\\\\":\\\\\\\"P102\\\\\\\",\\\\\\\"evidence\\\\\\\":[4],\\\\\\\"score\\\\\\\":6.951519012451172},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c9cole des officiers de la gendarmerie nationale\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":2,\\\\\\\"r\\\\\\\":\\\\\\\"P571\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":13.789529800415039},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c9cole des officiers de la gendarmerie nationale\\\\\\\",\\\\\\\"h_idx\\\\\\\":7,\\\\\\\"t_idx\\\\\\\":13,\\\\\\\"r\\\\\\\":\\\\\\\"P156\\\\\\\",\\\\\\\"evidence\\\\\\\":[2,5],\\\\\\\"score\\\\\\\":1.4925498962402344},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u00c9cole des officiers de la gendarmerie nationale\\\\\\\",\\\\\\\"h_idx\\\\\\\":13,\\\\\\\"t_idx\\\\\\\":7,\\\\\\\"r\\\\\\\":\\\\\\\"P155\\\\\\\",\\\\\\\"evidence\\\\\\\":[2,5],\\\\\\\"score\\\\\\\":4.045356750488281},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u0218tefan Grigorie\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":1,\\\\\\\"r\\\\\\\":\\\\\\\"P569\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":16.1859188079834},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u0218tefan Grigorie\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":2,\\\\\\\"r\\\\\\\":\\\\\\\"P27\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,5],\\\\\\\"score\\\\\\\":5.842049598693848},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u0218tefan Grigorie\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":3,\\\\\\\"r\\\\\\\":\\\\\\\"P54\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,2],\\\\\\\"score\\\\\\\":12.17776107788086},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u0218tefan Grigorie\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":4,\\\\\\\"r\\\\\\\":\\\\\\\"P54\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":15.380714416503906},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u0218tefan Grigorie\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":5,\\\\\\\"r\\\\\\\":\\\\\\\"P54\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":13.253593444824219},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u0218tefan Grigorie\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":6,\\\\\\\"r\\\\\\\":\\\\\\\"P54\\\\\\\",\\\\\\\"evidence\\\\\\\":[0,1,4],\\\\\\\"score\\\\\\\":9.252944946289062},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u0218tefan Grigorie\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":7,\\\\\\\"r\\\\\\\":\\\\\\\"P54\\\\\\\",\\\\\\\"evidence\\\\\\\":[0],\\\\\\\"score\\\\\\\":12.900182723999023},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u0218tefan Grigorie\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":10,\\\\\\\"r\\\\\\\":\\\\\\\"P54\\\\\\\",\\\\\\\"evidence\\\\\\\":[2],\\\\\\\"score\\\\\\\":0.6088094711303711},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u0218tefan Grigorie\\\\\\\",\\\\\\\"h_idx\\\\\\\":0,\\\\\\\"t_idx\\\\\\\":13,\\\\\\\"r\\\\\\\":\\\\\\\"P54\\\\\\\",\\\\\\\"evidence\\\\\\\":[2],\\\\\\\"score\\\\\\\":11.361888885498047},{\\\\\\\"title\\\\\\\":\\\\\\\"\\\\\\\\u0218tefan Grigorie\\\\\\\",\\\\\\\"h_idx\\\\\\\":16,\\\\\\\"t_idx\\\\\\\":5,\\\\\\\"r\\\\\\\":\\\\\\\"P54\\\\\\\",\\\\\\\"evidence\\\\\\\":[3],\\\\\\\"score\\\\\\\":8.67984390258789}]\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.85}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"[{\\\"title\\\":\\\"(I Am) The Seeker\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0],\\\"score\\\":3.697967529296875},{\\\"title\\\":\\\"(I Am) The Seeker\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":2,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":0.9657421112060547},{\\\"title\\\":\\\"(I Am) The Seeker\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":3,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":4.566144943237305},{\\\"title\\\":\\\"(I Am) The Seeker\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"P463\\\",\\\"evidence\\\":[0],\\\"score\\\":6.548666000366211},{\\\"title\\\":\\\"(I Am) The Seeker\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":1,\\\"r\\\":\\\"P463\\\",\\\"evidence\\\":[0],\\\"score\\\":8.283491134643555},{\\\"title\\\":\\\"(I Am) The Seeker\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":1,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.2059154510498047},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0],\\\"score\\\":9.141313552856445},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[0,1],\\\"score\\\":15.964946746826172},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":9.165733337402344},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0],\\\"score\\\":0.8681507110595703},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":13,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[4],\\\"score\\\":7.137664794921875},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":20,\\\"t_idx\\\":2,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0,6],\\\"score\\\":9.847187042236328},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":20,\\\"t_idx\\\":3,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[6],\\\"score\\\":7.742105484008789},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":20,\\\"t_idx\\\":4,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,6],\\\"score\\\":2.56552791595459},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":21,\\\"t_idx\\\":0,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0,6],\\\"score\\\":3.1435604095458984},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":21,\\\"t_idx\\\":2,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0,6],\\\"score\\\":7.491684913635254},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":21,\\\"t_idx\\\":3,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[0,6],\\\"score\\\":8.685039520263672},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":21,\\\"t_idx\\\":4,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1,6],\\\"score\\\":6.0979204177856445},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":22,\\\"t_idx\\\":2,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0,6],\\\"score\\\":4.051787376403809},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":22,\\\"t_idx\\\":3,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[1,6],\\\"score\\\":5.057645797729492},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":22,\\\"t_idx\\\":4,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[1,6],\\\"score\\\":3.568121910095215},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":23,\\\"t_idx\\\":2,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0,6],\\\"score\\\":9.088576316833496},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":23,\\\"t_idx\\\":3,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[6],\\\"score\\\":1.7855348587036133},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":23,\\\"t_idx\\\":4,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[6],\\\"score\\\":2.4017333984375},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":24,\\\"t_idx\\\":2,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0,6],\\\"score\\\":6.335969924926758},{\\\"title\\\":\\\"...Nothing Like the Sun\\\",\\\"h_idx\\\":24,\\\"t_idx\\\":4,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[6],\\\"score\\\":3.3533220291137695},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":0,\\\"r\\\":\\\"P50\\\",\\\"evidence\\\":[0],\\\"score\\\":11.554618835449219},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":12,\\\"r\\\":\\\"P50\\\",\\\"evidence\\\":[0],\\\"score\\\":0.8883247375488281},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":17,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[6],\\\"score\\\":7.376331329345703},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":18,\\\"r\\\":\\\"P123\\\",\\\"evidence\\\":[0,6],\\\"score\\\":5.969117164611816},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":3,\\\"r\\\":\\\"P710\\\",\\\"evidence\\\":[0],\\\"score\\\":0.7415056228637695},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":5,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0],\\\"score\\\":0.7725467681884766},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":7,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":4.964677810668945},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":7,\\\"r\\\":\\\"P607\\\",\\\"evidence\\\":[0],\\\"score\\\":1.9792919158935547},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":6,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":8.417366027832031},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":7,\\\"r\\\":\\\"P607\\\",\\\"evidence\\\":[1],\\\"score\\\":16.68253517150879},{\\\"title\\\":\\\"A Bridge Too Far (book)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":7,\\\"r\\\":\\\"P607\\\",\\\"evidence\\\":[0,1],\\\"sco\\n\\n... [截断: 输出过长，省略 1164086 字符] ...\\n\\n\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":7.484807968139648},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1],\\\"score\\\":9.756553649902344},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":9,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,1],\\\"score\\\":6.396303176879883},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":11,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[2,3],\\\"score\\\":6.048531532287598},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":3,\\\"r\\\":\\\"P118\\\",\\\"evidence\\\":[0],\\\"score\\\":9.594766616821289},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":7,\\\"r\\\":\\\"P118\\\",\\\"evidence\\\":[1],\\\"score\\\":4.330738067626953},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":2,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[1],\\\"score\\\":3.1826248168945312},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[1],\\\"score\\\":10.465694427490234},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":2,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,1],\\\"score\\\":1.392085075378418},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":4,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":0.4117765426635742},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":5,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1],\\\"score\\\":7.184945106506348},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":9,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,1],\\\"score\\\":5.0524444580078125},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":11,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[2,3],\\\"score\\\":3.5564842224121094},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[2,3],\\\"score\\\":4.317239761352539},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":11,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[2,3],\\\"score\\\":1.8771638870239258},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":2,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[4],\\\"score\\\":0.4242515563964844},{\\\"title\\\":\\\"\\\\u00c7a\\\\u011flar S\\\\u00f6y\\\\u00fcnc\\\\u00fc\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[4],\\\"score\\\":8.229376792907715},{\\\"title\\\":\\\"\\\\u00c9amon \\\\u00d3 Cu\\\\u00edv\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":17.39966583251953},{\\\"title\\\":\\\"\\\\u00c9amon \\\\u00d3 Cu\\\\u00edv\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"P102\\\",\\\"evidence\\\":[0,5],\\\"score\\\":7.914501190185547},{\\\"title\\\":\\\"\\\\u00c9amon \\\\u00d3 Cu\\\\u00edv\\\",\\\"h_idx\\\":21,\\\"t_idx\\\":3,\\\"r\\\":\\\"P102\\\",\\\"evidence\\\":[3],\\\"score\\\":4.60417366027832},{\\\"title\\\":\\\"\\\\u00c9amon \\\\u00d3 Cu\\\\u00edv\\\",\\\"h_idx\\\":23,\\\"t_idx\\\":3,\\\"r\\\":\\\"P102\\\",\\\"evidence\\\":[4],\\\"score\\\":6.951519012451172},{\\\"title\\\":\\\"\\\\u00c9cole des officiers de la gendarmerie nationale\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0],\\\"score\\\":13.789529800415039},{\\\"title\\\":\\\"\\\\u00c9cole des officiers de la gendarmerie nationale\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":13,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[2,5],\\\"score\\\":1.4925498962402344},{\\\"title\\\":\\\"\\\\u00c9cole des officiers de la gendarmerie nationale\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":7,\\\"r\\\":\\\"P155\\\",\\\"evidence\\\":[2,5],\\\"score\\\":4.045356750488281},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":16.1859188079834},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,5],\\\"score\\\":5.842049598693848},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,2],\\\"score\\\":12.17776107788086},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":15.380714416503906},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":13.253593444824219},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":6,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,1,4],\\\"score\\\":9.252944946289062},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":7,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":12.900182723999023},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":10,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[2],\\\"score\\\":0.6088094711303711},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":13,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[2],\\\"score\\\":11.361888885498047},{\\\"title\\\":\\\"\\\\u0218tefan Grigorie\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":5,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[3],\\\"score\\\":8.67984390258789}]\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.85}}"
    }
  }
}
```

</details>

---


### Large event (continued)

````text
### Tool result

_source line 85 · 2026-05-17T12:59:58.175Z_

&lt;details>&lt;summary>↩ Tool result · `toolu_01NtB4FL1WrrXkjjMXhPRWMs`&lt;/summary>

```text
Error: result (19,136,481 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2922664d-de47-47ee-b079-f72d8bbe808e/tool-results/mcp-agent-ml-research-ssh_read_only-1779022798042.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2922664d-de47-47ee-b079-f72d8bbe808e/tool-results/mcp-agent-ml-research-ssh_read_only-1779022798042.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

&lt;/details>

&lt;details>&lt;summary>Recorded metadata&lt;/summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2922664d-de47-47ee-b079-f72d8bbe808e",
  "uuid": "af3ceacb-2437-4887-98bb-4166245430b2",
  "tool_use_result": {
    "content": "Error: result (19,136,481 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2922664d-de47-47ee-b079-f72d8bbe808e/tool-results/mcp-agent-ml-research-ssh_read_only-1779022798042.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/2922664d-de47-47ee-b079-f72d8bbe808e/tool-results/mcp-agent-ml-research-ssh_read_only-1779022798042.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {

````

---

### Large event (continued)

```text
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cat /root/autodl-tmp/baselines/dreeam/checkpoints/teacher_roberta/2026-05-15_22:29:42.720935/topk_results.json'\\n\\nStdout:\\n\\n[{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":3.561478614807129},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":9,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-5.490738868713379},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":9,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-12.491901397705078},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-5.036534309387207},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":9,\\\"r\\\":\\\"P740\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-11.544083595275879},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":9,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-12.831392288208008},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.49231624603271484},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":9,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-7.662997722625732},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":9,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-11.943821907043457},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":0.9626502990722656},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-6.745988845825195},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-11.098243713378906},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-2.0693397521972656},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"P749\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-2.991583824157715},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"P463\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-8.97403335571289},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-7.078695297241211},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"P740\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-13.455198287963867},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-13.82735824584961},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":4.770299911499023},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":9,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-8.869468688964844},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":9,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0],\\\"score\\\":-11.521907806396484},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":0.09908294677734375},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"P495\\\",\\\"evidence\\\":[0],\\\"score\\\":-9.45114517211914},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0],\\\"score\\\":-11.424903869628906},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0,2],\\\"score\\\":6.211051940917969},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-16.64187240600586},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-16.665502548217773},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":6,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-22.985607147216797},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":6,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-23.38788414001465},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":6,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-24.20429039001465},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":7,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-25.696744918823242},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":7,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-27.982688903808594},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":7,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-28.100099563598633},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[4],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":8,\\\"r\\\":\\\"P463\\\",\\\"evidence\\\":[4],\\\"score\\\":-8.418916702270508},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":8,\\\"r\\\":\\\"P749\\\",\\\"evidence\\\":[4],\\\"score\\\":-18.471324920654297},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":8,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[4],\\\"score\\\":-19.177358627319336},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":10,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-9.543973922729492},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":10,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-12.041793823242188},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":10,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-14.0662202835083},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":0,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.717750549316406},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":0,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.818124771118164},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":0,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.60111427307129},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":2,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-13.730672836303711},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":2,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.768251419067383},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":2,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.88083267211914},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":3,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-17.242938995361328},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":3,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.849260330200195},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":3,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.853593826293945},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1198\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-21.657907485961914},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":4,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-22.60956573486328},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":4,\\\"r\\\":\\\"P576\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-23.70153045654297},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":5,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-10.839019775390625},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":5,\\\"r\\\":\\\"P36\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-13.012426376342773},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":5,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-15.056136131286621},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":6,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.04513168334961},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":6,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.84016227722168},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":6,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.89541244506836},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":7,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-26.472848892211914},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":7,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-27.09797477722168},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":7,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-28.10365104675293},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":8,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-23.025352478027344},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":8,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-23.81134033203125},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":8,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-24.140846252441406},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":9,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":-11.985332489013672},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-12.145174980163574},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":9,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-13.814995765686035},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":10,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-2.0437679290771484},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":10,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-12.381813049316406},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":10,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-13.538313865661621},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":0,\\\"r\\\":\\\"P206\\\",\\\"evidence\\\":[0],\\\"score\\\":-15.7254638671875},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":0,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-16.37633514404297},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":0,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-16.41520118713379},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-1.196192741394043},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-7.395739555358887},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-11.27735710144043},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":3,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-13.896036148071289},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":3,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0],\\\"score\\\":-16.769502639770508},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":3,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.717084884643555},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":4,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.724159240722656},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":4,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.572080612182617},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":4,\\\"r\\\":\\\"P206\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.165674209594727},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":5,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-14.189796447753906},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":5,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.020366668701172},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":5,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.947818756103516},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":6,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.98846435546875},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":6,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.7933349609375},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":6,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.206897735595703},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":7,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.61290168762207},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":7,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.0118350982666},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":7,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.112398147583008},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":8,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-15.61935806274414},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":8,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.810386657714844},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":8,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.899898529052734},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":10,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-9.970913887023926},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":10,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-13.128212928771973},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":10,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0],\\\"score\\\":-13.587684631347656},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":0,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.62493896484375},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":0,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-9.518804550170898},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":0,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-12.35206413269043},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":1,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-10.634570121765137},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":1,\\\"r\\\":\\\"P740\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-13.716085433959961},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":1,\\\"r\\\":\\\"P495\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-13.753893852233887},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":2,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":-8.66850471496582},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":2,\\\"r\\\":\\\"P740\\\",\\\"evidence\\\":[0],\\\"score\\\":-16.856246948242188},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":2,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.043516159057617},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":4,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.586814880371094},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":4,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.75031852722168},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":4,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.592266082763672},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":5,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":-12.323893547058105},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":5,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.128328323364258},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":5,\\\"r\\\":\\\"P740\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.863157272338867},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":6,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.022266387939453},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":6,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.095596313476562},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":6,\\\"r\\\":\\\"P171\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.848806381225586},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":7,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.59429931640625},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":7,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.717924118041992},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":7,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.196971893310547},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":8,\\\"r\\\":\\\"P171\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.170461654663086},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":8,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.67066764831543},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":8,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.690279006958008},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":10,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-13.125876426696777},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":10,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0],\\\"score\\\":-14.553075790405273},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":10,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.166465759277344},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":0,\\\"r\\\":\\\"P749\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-21.373857498168945},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":0,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-22.43741798400879},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":0,\\\"r\\\":\\\"P58\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-22.65311622619629},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":1,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-20.500627517700195},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":1,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-20.850244522094727},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":1,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-21.50922203063965},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":2,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.52073097229004},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":2,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.317981719970703},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":2,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.40873146057129},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":3,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.529159545898438},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":3,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.81770133972168},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":3,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.863359451293945},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":5,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[2],\\\"score\\\":-20.72356605529785},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":5,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[2],\\\"score\\\":-22.500059127807617},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":5,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[2],\\\"score\\\":-22.882118225097656},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":6,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-26.399934768676758},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":6,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-28.290803909301758},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":6,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-28.754392623901367},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":7,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-26.732040405273438},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":7,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-29.590274810791016},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":7,\\\"r\\\":\\\"P58\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-29.761125564575195},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":8,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.564851760864258},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":8,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.764041900634766},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":8,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.40738296508789},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":9,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-21.415767669677734},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":9,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-21.914228439331055},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":9,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-21.95240020751953},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":10,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-17.681175231933594},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":10,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-19.440296173095703},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":10,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-21.6646785736084},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":0,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-18.85932731628418},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":0,\\\"r\\\":\\\"P206\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-19.674467086791992},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":0,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-19.974071502685547},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":1,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.15869617462158203},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":1,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-6.758004188537598},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":1,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-10.425203323364258},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":2,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.938833236694336},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":2,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.893829345703125},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":2,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.853797912597656},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":3,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.687841415405273},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":3,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.748178482055664},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":3,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.915719985961914},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":4,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[2],\\\"score\\\":-19.94719123840332},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":4,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[2],\\\"score\\\":-22.252323150634766},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":4,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[2],\\\"score\\\":-23.013322830200195},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":6,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.7427978515625},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":6,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.75446128845215},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":6,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.964956283569336},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":7,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-27.066425323486328},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":7,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-27.13418197631836},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":7,\\\"r\\\":\\\"P206\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-29.450773239135742},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":8,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.47909927368164},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":8,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.659605026245117},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":8,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.427101135253906},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":10,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-9.650273323059082},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":10,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-11.652196884155273},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":10,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-11.751241683959961},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":0,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-24.034648895263672},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":0,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-24.586015701293945},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":0,\\\"r\\\":\\\"P749\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-24.675216674804688},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":1,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.117347717285156},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":1,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.77477264404297},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":1,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.99239730834961},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":2,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.15721893310547},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":2,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.18564796447754},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":2,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.545610427856445},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":3,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.787208557128906},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":3,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.676315307617188},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":3,\\\"r\\\":\\\"P749\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.043132781982422},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":4,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-22.68883514404297},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":4,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-23.230571746826172},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":4,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-24.04399299621582},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":5,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.242813110351562},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":5,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.46695327758789},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":5,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.037151336669922},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":7,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[3],\\\"score\\\":-26.17743492126465},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":7,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[3],\\\"score\\\":-26.53563690185547},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":7,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[3],\\\"score\\\":-26.704790115356445},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":8,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-21.829696655273438},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":8,\\\"r\\\":\\\"P463\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-23.311912536621094},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":8,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-24.20891571044922},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-12.762800216674805},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":9,\\\"r\\\":\\\"P740\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-19.844324111938477},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":9,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-20.044397354125977},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":10,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-15.409229278564453},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":10,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.39944839477539},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":10,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.279972076416016},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":0,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-23.991432189941406},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":0,\\\"r\\\":\\\"P137\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-24.156232833862305},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":0,\\\"r\\\":\\\"P749\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-24.574132919311523},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":1,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-14.925752639770508},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":1,\\\"r\\\":\\\"P495\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-19.83472442626953},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":1,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-20.138423919677734},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":2,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.433500289916992},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":2,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.725378036499023},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":2,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.818843841552734},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":3,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0],\\\"score\\\":-14.551268577575684},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":3,\\\"r\\\":\\\"P749\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.172426223754883},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":3,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.341398239135742},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":4,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-17.799213409423828},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":4,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-20.139385223388672},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":4,\\\"r\\\":\\\"P576\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-23.048967361450195},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":5,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-21.968313217163086},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":5,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-22.64657974243164},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":5,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-23.032386779785156},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":6,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[3],\\\"score\\\":-21.65232276916504},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":6,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[3],\\\"score\\\":-22.61806869506836},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":6,\\\"r\\\":\\\"P749\\\",\\\"evidence\\\":[3],\\\"score\\\":-22.75642967224121},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":8,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-22.729576110839844},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":8,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-23.30403709411621},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":8,\\\"r\\\":\\\"P463\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-23.569034576416016},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-8.225513458251953},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":9,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-16.858423233032227},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":9,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-17.733430862426758},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":10,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-15.869250297546387},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":10,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.62832260131836},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":10,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.074262619018555},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[4],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":0,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[4],\\\"score\\\":-14.31256103515625},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":0,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[4],\\\"score\\\":-15.678145408630371},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":0,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[4],\\\"score\\\":-17.912675857543945},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":1,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-15.463201522827148},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":1,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-18.44341468811035},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":1,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-18.856292724609375},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":2,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":-15.650589942932129},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":2,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.435136795043945},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":2,\\\"r\\\":\\\"P171\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.332801818847656},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":3,\\\"r\\\":\\\"P171\\\",\\\"evidence\\\":[0],\\\"score\\\":-16.887821197509766},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":3,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.20029067993164},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":3,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.987136840820312},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":4,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.47116470336914},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":4,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.16025161743164},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":4,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.300525665283203},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":5,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.08611488342285},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":5,\\\"r\\\":\\\"P171\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.2148380279541},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":5,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.54468536376953},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":6,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-21.68340301513672},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":6,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-21.86685562133789},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":6,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-22.089563369750977},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":7,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-23.228900909423828},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":7,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-23.277795791625977},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":7,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-23.87352180480957},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[4],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[4],\\\"score\\\":-2.060553550720215},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":9,\\\"r\\\":\\\"P740\\\",\\\"evidence\\\":[4],\\\"score\\\":-15.045235633850098},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":9,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[4],\\\"score\\\":-15.253809928894043},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":10,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-13.587791442871094},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":10,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-19.472394943237305},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":10,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-19.706998825073242},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":0,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.121957778930664},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":0,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.320589065551758},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":0,\\\"r\\\":\\\"P172\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.51906394958496},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":1,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-12.463937759399414},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":1,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-13.471460342407227},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":1,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":-13.636396408081055},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":2,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-12.343403816223145},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":2,\\\"r\\\":\\\"P840\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.33549690246582},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":2,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.347938537597656},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":3,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-17.241703033447266},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":3,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-17.573217391967773},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":3,\\\"r\\\":\\\"P1198\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-17.835609436035156},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1198\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-20.55229377746582},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":4,\\\"r\\\":\\\"P580\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-23.616497039794922},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":4,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-23.94887351989746},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":5,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-11.025148391723633},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":5,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-15.313657760620117},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":5,\\\"r\\\":\\\"P36\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-16.09646224975586},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":6,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-23.023218154907227},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":6,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-25.096960067749023},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":6,\\\"r\\\":\\\"P1198\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-26.00397491455078},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":7,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-25.643413543701172},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":7,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-26.786090850830078},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":7,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-27.119346618652344},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[4],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":8,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[4],\\\"score\\\":-18.865535736083984},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":8,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[4],\\\"score\\\":-18.932016372680664},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":8,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[4],\\\"score\\\":-19.24994659423828},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":10,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,5],\\\"score\\\":0.9998836517333984},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":10,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-13.128007888793945},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":10,\\\"r\\\":\\\"P172\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-14.462449073791504},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":0,\\\"r\\\":\\\"P175\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-23.973918914794922},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":0,\\\"r\\\":\\\"P749\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-24.081579208374023},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":0,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-24.25381851196289},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":1,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-12.076006889343262},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":1,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-12.814682960510254},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":1,\\\"r\\\":\\\"P495\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-13.237220764160156},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":2,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.85932731628418},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":2,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.616857528686523},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":2,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.747278213500977},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":3,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.586523056030273},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":3,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.357315063476562},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":3,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.380460739135742},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":4,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-23.85051727294922},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":4,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-25.88959312438965},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":4,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-26.128799438476562},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":5,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-18.393735885620117},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":5,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-18.56536865234375},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":5,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-19.41813850402832},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":6,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.976648330688477},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":6,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.956220626831055},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":6,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.083587646484375},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":7,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.236268997192383},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":7,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.25006103515625},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":7,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.765335083007812},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":8,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-24.632549285888672},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":8,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-24.686025619506836},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":8,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-25.0894775390625},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-9.800874710083008},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":9,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-10.91637897491455},{\\\"title\\\":\\\"Skai TV\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":9,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-15.473451614379883},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":5.369174003601074},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":5,\\\"r\\\":\\\"P495\\\",\\\"evidence\\\":[0],\\\"score\\\":-4.9154372215271},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":5,\\\"r\\\":\\\"P740\\\",\\\"evidence\\\":[0],\\\"score\\\":-12.868002891540527},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":4,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":15.669881820678711},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1001\\\",\\\"evidence\\\":[0],\\\"score\\\":-11.494429588317871},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":4,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0],\\\"score\\\":-14.350550651550293},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":12.2936429977417},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":5,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-11.738271713256836},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":5,\\\"r\\\":\\\"P495\\\",\\\"evidence\\\":[0],\\\"score\\\":-12.174752235412598},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":3,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":13.712352752685547},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":3,\\\"r\\\":\\\"P1001\\\",\\\"evidence\\\":[0],\\\"score\\\":-14.577264785766602},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":3,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-14.880248069763184},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":5,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":10.539473533630371},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":10.462260246276855},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":5,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0],\\\"score\\\":-9.974302291870117},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":4,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":14.497252464294434},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":4,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-14.766711235046387},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1001\\\",\\\"evidence\\\":[0],\\\"score\\\":-15.479114532470703},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-8.021479606628418},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":5,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-9.469987869262695},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":5,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-13.767824172973633},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-2.624728202819824},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":5,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-7.093881130218506},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":5,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-13.963303565979004},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":5,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,2],\\\"score\\\":3.7908124923706055},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-3.313488006591797},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":5,\\\"r\\\":\\\"P570\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-12.688376426696777},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":4,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[2],\\\"score\\\":13.308576583862305},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1001\\\",\\\"evidence\\\":[2],\\\"score\\\":-11.068175315856934},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1366\\\",\\\"evidence\\\":[2],\\\"score\\\":-15.927916526794434},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,2],\\\"score\\\":12.080501556396484},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":5,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-8.634912490844727},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":5,\\\"r\\\":\\\"P205\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-12.936415672302246},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":5,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-2.9232254028320312},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-13.192666053771973},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":5,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-14.629144668579102},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":12.393948554992676},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0],\\\"score\\\":-8.040266036987305},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-10.087352752685547},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":5,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-13.634821891784668},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-17.04779052734375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":5,\\\"r\\\":\\\"P205\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.229854583740234},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-15.266908645629883},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":5,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.97471046447754},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":5,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.118072509765625},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":4.771501541137695},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":5,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-0.32792091369628906},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":5,\\\"r\\\":\\\"P495\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-10.526191711425781},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"P155\\\",\\\"evidence\\\":[0],\\\"score\\\":-16.550567626953125},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.099666595458984},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.817331314086914},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-6.950357437133789},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-14.786724090576172},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"P585\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.62562370300293},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-0.6478910446166992},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":-10.625284194946289},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0],\\\"score\\\":-12.021932601928711},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":5.717775344848633},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1001\\\",\\\"evidence\\\":[0],\\\"score\\\":-13.44543170928955},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-14.737222671508789},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":6,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[1],\\\"score\\\":-2.985030174255371},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":6,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[1],\\\"score\\\":-7.070531845092773},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":6,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[1],\\\"score\\\":-7.478306770324707},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":7,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-5.919486999511719},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":7,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[1],\\\"score\\\":-7.28004264831543},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":7,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[1],\\\"score\\\":-7.36200475692749},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":8,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1,3],\\\"score\\\":-17.44679832458496},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":8,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0,1,3],\\\"score\\\":-20.135784149169922},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":8,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1,3],\\\"score\\\":-20.496673583984375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":9,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[1],\\\"score\\\":-14.988362312316895},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":9,\\\"r\\\":\\\"P585\\\",\\\"evidence\\\":[1],\\\"score\\\":-20.084590911865234},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":9,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[1],\\\"score\\\":-20.393878936767578},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":10,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[1],\\\"score\\\":-12.456836700439453},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":10,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[1],\\\"score\\\":-12.909647941589355},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":10,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[1],\\\"score\\\":-13.414451599121094},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":11,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.348176956176758},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":11,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.17947006225586},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":11,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.760412216186523},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":12,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.407188415527344},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":12,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.775094985961914},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":12,\\\"r\\\":\\\"P272\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.975887298583984},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":13,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-8.413412094116211},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":13,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-11.426286697387695},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":13,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-12.281822204589844},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":14,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-20.81293487548828},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":14,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-21.387065887451172},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":14,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-21.41538429260254},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":15,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.43433952331543},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":15,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.533369064331055},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":15,\\\"r\\\":\\\"P463\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.55613899230957},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":16,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-14.01582145690918},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":16,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.666540145874023},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":16,\\\"r\\\":\\\"P463\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.703441619873047},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":17,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-25.262500762939453},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":17,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-26.551651000976562},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":17,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-26.782085418701172},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":18,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-17.308988571166992},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":18,\\\"r\\\":\\\"P161\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-25.058094024658203},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":18,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-27.305696487426758},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":0,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-16.709312438964844},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":0,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.511613845825195},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":0,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.815959930419922},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":2,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[0],\\\"score\\\":-0.9731407165527344},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":2,\\\"r\\\":\\\"P585\\\",\\\"evidence\\\":[0],\\\"score\\\":-3.022425651550293},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":2,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0],\\\"score\\\":-8.771530151367188},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":3,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-16.037017822265625},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":3,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.597240447998047},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":3,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.135095596313477},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1001\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.741994857788086},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":4,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.62722396850586},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.990201950073242},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":6,\\\"r\\\":\\\"P162\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.163433074951172},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":6,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.771888732910156},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":6,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.845972061157227},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":7,\\\"r\\\":\\\"P58\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.20372200012207},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":7,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.26435089111328},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":7,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.79279136657715},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":8,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.713712692260742},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":8,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.875091552734375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":8,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.950098037719727},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":9,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-20.232866287231445},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":9,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.35028648376465},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.60521125793457},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":10,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.92087745666504},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":10,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.245363235473633},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":10,\\\"r\\\":\\\"P58\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.24694061279297},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":11,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.0289249420166},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":11,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.12290382385254},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":11,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.265268325805664},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":12,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.5781307220459},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":12,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.716032028198242},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":12,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.032230377197266},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":13,\\\"r\\\":\\\"P162\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.357580184936523},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":13,\\\"r\\\":\\\"P155\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.47454261779785},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":13,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.53583335876465},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":14,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-23.601465225219727},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":14,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-24.14299964904785},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":14,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-24.73722267150879},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":15,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.086366653442383},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":15,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.6035213470459},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":15,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.080528259277344},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":16,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-12.64500617980957},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":16,\\\"r\\\":\\\"P495\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.934724807739258},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":16,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.93606948852539},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":17,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.726028442382812},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":17,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.406021118164062},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":17,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.51515007019043},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":18,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.093507766723633},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":18,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.399581909179688},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":18,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.43569564819336},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":0,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-30.805343627929688},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":0,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-32.10506820678711},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":0,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-32.23674392700195},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-15.52740478515625},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"P155\\\",\\\"evidence\\\":[0],\\\"score\\\":-16.496597290039062},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[0],\\\"score\\\":-16.9444580078125},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":3,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.700611114501953},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":3,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.935075759887695},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":3,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-31.058469772338867},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.403730392456055},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":4,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.24411392211914},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1001\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.14942741394043},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-16.6619873046875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":5,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.846405029296875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":5,\\\"r\\\":\\\"P495\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.11160659790039},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":6,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.540037155151367},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":6,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.732345581054688},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":6,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-28.37049674987793},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":7,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-26.456613540649414},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":7,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[1],\\\"score\\\":-29.19343376159668},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":7,\\\"r\\\":\\\"P205\\\",\\\"evidence\\\":[1],\\\"score\\\":-29.35849952697754},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":8,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.495588302612305},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":8,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[0],\\\"score\\\":-32.028907775878906},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":8,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-33.28954315185547},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":9,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.380084991455078},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":9,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1],\\\"score\\\":-25.17068099975586},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":9,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-25.26936149597168},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":10,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[1],\\\"score\\\":-27.813444137573242},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":10,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[1],\\\"score\\\":-28.938552856445312},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":10,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-29.107324600219727},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":11,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[1],\\\"score\\\":-25.63003921508789},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":11,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-26.561538696289062},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":11,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1],\\\"score\\\":-27.209627151489258},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":12,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[1],\\\"score\\\":-27.45140266418457},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":12,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1],\\\"score\\\":-30.127073287963867},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":12,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1],\\\"score\\\":-30.50469207763672},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":13,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.707582473754883},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":13,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.355104446411133},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":13,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.71463394165039},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":14,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.24006462097168},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":14,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-33.51984786987305},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":14,\\\"r\\\":\\\"P205\\\",\\\"evidence\\\":[0],\\\"score\\\":-34.695011138916016},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":15,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.760665893554688},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":15,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.82476234436035},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":15,\\\"r\\\":\\\"P171\\\",\\\"evidence\\\":[0],\\\"score\\\":-31.085731506347656},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":16,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.74625015258789},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":16,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.770538330078125},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":16,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.976139068603516},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":17,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-31.406055450439453},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":17,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-36.62398910522461},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":17,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-36.94247055053711},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":18,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.714035034179688},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":18,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-33.049720764160156},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":18,\\\"r\\\":\\\"P171\\\",\\\"evidence\\\":[0],\\\"score\\\":-33.09445571899414},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":0,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-14.137751579284668},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":0,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.56545639038086},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":0,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.592220306396484},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":1,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.79454231262207},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":1,\\\"r\\\":\\\"P155\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.481687545776367},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":1,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.011444091796875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":2,\\\"r\\\":\\\"P580\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.72259521484375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":2,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.087825775146484},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":2,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.501571655273438},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":6,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-20.165254592895508},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":6,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.283935546875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":6,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.57278823852539},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":7,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.504499435424805},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":7,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.49979019165039},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":7,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.818103790283203},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":8,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-10.483296394348145},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":8,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-17.03712272644043},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":8,\\\"r\\\":\\\"P580\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-20.782642364501953},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.93977165222168},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":9,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.345962524414062},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":9,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.86379623413086},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":10,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.7999324798584},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":10,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.56113052368164},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":10,\\\"r\\\":\\\"P58\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.905498504638672},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":11,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.500812530517578},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":11,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.077272415161133},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":11,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.24947166442871},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":12,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.173276901245117},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":12,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.464948654174805},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":12,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-28.916215896606445},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":13,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.960351943969727},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":13,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.242338180541992},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":13,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.06242561340332},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":14,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-23.77287483215332},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":14,\\\"r\\\":\\\"P1365\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-25.585132598876953},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":14,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-25.961170196533203},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":15,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.175275802612305},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":15,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.3697566986084},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":15,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.985462188720703},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":16,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-12.910426139831543},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":16,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.28919219970703},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":16,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.84067726135254},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":17,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.344682693481445},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":17,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.41319465637207},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":17,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.88140296936035},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":18,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.161327362060547},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":18,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.848787307739258},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":18,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.3261775970459},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":0,\\\"r\\\":\\\"P400\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.766490936279297},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":0,\\\"r\\\":\\\"P800\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.94287872314453},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":0,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.191856384277344},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":1,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.34317398071289},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":1,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.597909927368164},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":1,\\\"r\\\":\\\"P403\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.319395065307617},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":2,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.711835861206055},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":2,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.332622528076172},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":2,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.970718383789062},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":6,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-20.681140899658203},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":6,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.94938850402832},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":6,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.313554763793945},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":7,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.73389434814453},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":7,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.192279815673828},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":7,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.745830535888672},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":8,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-14.189573287963867},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":8,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-19.386669158935547},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":8,\\\"r\\\":\\\"P674\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-19.601238250732422},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":9,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[1],\\\"score\\\":-19.035165786743164},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":9,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.992734909057617},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":9,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.714204788208008},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":10,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-20.02981185913086},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":10,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.903715133666992},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":10,\\\"r\\\":\\\"P674\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.936092376708984},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":11,\\\"r\\\":\\\"P1365\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.073862075805664},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":11,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.16802406311035},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":11,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.914234161376953},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":12,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.508634567260742},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":12,\\\"r\\\":\\\"P1365\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.655277252197266},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":12,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.719371795654297},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":13,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[2],\\\"score\\\":-17.62514877319336},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":13,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[2],\\\"score\\\":-19.164772033691406},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":13,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[2],\\\"score\\\":-19.516401290893555},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":14,\\\"r\\\":\\\"P403\\\",\\\"evidence\\\":[2],\\\"score\\\":-17.328245162963867},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":14,\\\"r\\\":\\\"P1365\\\",\\\"evidence\\\":[2],\\\"score\\\":-18.814559936523438},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":14,\\\"r\\\":\\\"P400\\\",\\\"evidence\\\":[2],\\\"score\\\":-18.841283798217773},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":15,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-22.24581527709961},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":15,\\\"r\\\":\\\"P403\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-25.915014266967773},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":15,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-26.056663513183594},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":16,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[2],\\\"score\\\":-13.947602272033691},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":16,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[2],\\\"score\\\":-14.695629119873047},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":16,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[2],\\\"score\\\":-16.557649612426758},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":17,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,2,3],\\\"score\\\":-24.309236526489258},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":17,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,2,3],\\\"score\\\":-28.44850730895996},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":17,\\\"r\\\":\\\"P403\\\",\\\"evidence\\\":[0,2,3],\\\"score\\\":-29.138383865356445},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":18,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.48069190979004},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":18,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.926116943359375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":18,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.98370933532715},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":0,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-10.997091293334961},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":0,\\\"r\\\":\\\"P800\\\",\\\"evidence\\\":[0],\\\"score\\\":-16.031259536743164},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":0,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.457286834716797},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":1,\\\"r\\\":\\\"P155\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.64661979675293},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":1,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.316076278686523},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":1,\\\"r\\\":\\\"P1344\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.027809143066406},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":2,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[0],\\\"score\\\":-16.7598876953125},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":2,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.466699600219727},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":2,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.617429733276367},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":3,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-15.86656379699707},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":3,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.5051326751709},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":3,\\\"r\\\":\\\"P69\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.70393180847168},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":6,\\\"r\\\":\\\"P6\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-17.34079360961914},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":6,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-19.272296905517578},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":6,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-20.1607666015625},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":7,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-16.724853515625},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":7,\\\"r\\\":\\\"P178\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-20.37151336669922},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":7,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-20.703271865844727},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":8,\\\"r\\\":\\\"P6\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-11.585044860839844},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":8,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-17.020851135253906},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":8,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.35433006286621},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":9,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[1],\\\"score\\\":-20.355928421020508},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":9,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.08075523376465},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":9,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.34917449951172},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":10,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[1],\\\"score\\\":-22.20992088317871},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":10,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.446088790893555},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":10,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-24.31841278076172},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":11,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.603893280029297},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":11,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.71672248840332},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":11,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.778898239135742},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":12,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.706457138061523},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":12,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.066791534423828},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":12,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.482215881347656},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":13,\\\"r\\\":\\\"P6\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-11.603102684020996},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":13,\\\"r\\\":\\\"P172\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-14.238277435302734},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":13,\\\"r\\\":\\\"P162\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-15.247950553894043},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":14,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-17.868074417114258},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":14,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-19.30335235595703},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":14,\\\"r\\\":\\\"P69\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-19.770950317382812},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":15,\\\"r\\\":\\\"P172\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-19.42972183227539},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":15,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-24.227149963378906},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":15,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-24.2352237701416},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":16,\\\"r\\\":\\\"P172\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-7.215775966644287},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":16,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-11.803657531738281},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":16,\\\"r\\\":\\\"P194\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-12.197860717773438},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":17,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-19.036775588989258},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":17,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-23.178518295288086},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":17,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-23.938615798950195},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":18,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-23.857656478881836},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":18,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-24.619958877563477},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":18,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-24.858671188354492},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":0,\\\"r\\\":\\\"P800\\\",\\\"evidence\\\":[1],\\\"score\\\":-10.677088737487793},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":0,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-12.481122016906738},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":0,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1],\\\"score\\\":-13.326051712036133},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":1,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.375825881958008},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":1,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.608346939086914},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":1,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.898767471313477},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":2,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.214563369750977},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":2,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.230403900146484},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":2,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.35322380065918},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":3,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.078630447387695},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":3,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.091447830200195},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":3,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.438570022583008},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":4,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.29217529296875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":4,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-20.744003295898438},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.746456146240234},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":7,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":4.7342119216918945},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":7,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1],\\\"score\\\":-13.670003890991211},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":7,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[1],\\\"score\\\":-14.615707397460938},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":8,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-17.761180877685547},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":8,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.02985382080078},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":8,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[1],\\\"score\\\":-22.67208480834961},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":9,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-22.77409553527832},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":9,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.472177505493164},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":9,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.773834228515625},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":10,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-5.99989128112793},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":10,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1],\\\"score\\\":-16.36683464050293},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":10,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[1],\\\"score\\\":-16.461881637573242},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":11,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-19.27284049987793},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":11,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[1],\\\"score\\\":-20.805511474609375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":11,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1],\\\"score\\\":-24.206035614013672},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":12,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.922710418701172},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":12,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1],\\\"score\\\":-26.334230422973633},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":12,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-27.60852813720703},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":13,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-12.988382339477539},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":13,\\\"r\\\":\\\"P22\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-13.244379043579102},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":13,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-13.498652458190918},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":14,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-26.09262466430664},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":14,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-27.006549835205078},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":14,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-27.41356658935547},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":15,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-23.577795028686523},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":15,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-23.765342712402344},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":15,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-24.460477828979492},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":16,\\\"r\\\":\\\"P172\\\",\\\"evidence\\\":[2],\\\"score\\\":-10.786362648010254},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":16,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[2],\\\"score\\\":-12.22368049621582},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":16,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[2],\\\"score\\\":-12.521775245666504},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":17,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.695693969726562},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":17,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.40709114074707},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":17,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.119192123413086},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":18,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.201736450195312},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":18,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.810325622558594},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":18,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.878549575805664},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":0,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-11.87627124786377},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":0,\\\"r\\\":\\\"P800\\\",\\\"evidence\\\":[1],\\\"score\\\":-12.778505325317383},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":0,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1],\\\"score\\\":-13.340521812438965},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":1,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.268310546875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":1,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.994850158691406},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":1,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.394081115722656},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":2,\\\"r\\\":\\\"P136\\\",\\\"evidence\\\":[1],\\\"score\\\":-18.482120513916016},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":2,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-18.655559539794922},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":2,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-18.971107482910156},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":3,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-19.050609588623047},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":3,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-20.013715744018555},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":3,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.450956344604492},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":4,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.158567428588867},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":4,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.75415802001953},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":4,\\\"r\\\":\\\"P136\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.30978012084961},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":6,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-0.5642852783203125},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":6,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1],\\\"score\\\":-12.123368263244629},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":6,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[1],\\\"score\\\":-12.684886932373047},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":8,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-11.539024353027344},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":8,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[1],\\\"score\\\":-17.30718421936035},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":8,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[1],\\\"score\\\":-18.590538024902344},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":9,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.028676986694336},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":9,\\\"r\\\":\\\"P136\\\",\\\"evidence\\\":[1],\\\"score\\\":-22.73794937133789},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":9,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1],\\\"score\\\":-22.94388771057129},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":10,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-5.8628034591674805},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":10,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1],\\\"score\\\":-13.634082794189453},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":10,\\\"r\\\":\\\"P25\\\",\\\"evidence\\\":[1],\\\"score\\\":-13.9449462890625},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":11,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-19.641685485839844},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":11,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.323148727416992},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":11,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1],\\\"score\\\":-24.674814224243164},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":12,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[1],\\\"score\\\":-26.09759521484375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":12,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1],\\\"score\\\":-26.70872688293457},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":12,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-27.23019027709961},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":13,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-4.640018463134766},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":13,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1],\\\"score\\\":-12.668571472167969},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":13,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[1],\\\"score\\\":-13.584484100341797},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":14,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-25.929426193237305},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":14,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-28.14066505432129},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":14,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-28.62036895751953},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":15,\\\"r\\\":\\\"P136\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.240650177001953},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":15,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.0516357421875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":15,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.10786247253418},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":16,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-20.531944274902344},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":16,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.204437255859375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":16,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.830446243286133},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":17,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-29.006380081176758},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":17,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-29.093233108520508},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":17,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-29.387235641479492},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":18,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.41640281677246},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":18,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.65445899963379},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":18,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.39511489868164},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":0,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,1,3],\\\"score\\\":-20.116361618041992},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":0,\\\"r\\\":\\\"P400\\\",\\\"evidence\\\":[0,1,3],\\\"score\\\":-21.029003143310547},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":0,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1,3],\\\"score\\\":-21.760454177856445},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":1,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.6801700592041},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":1,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.565135955810547},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":1,\\\"r\\\":\\\"P1344\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.403043746948242},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":2,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.908676147460938},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":2,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.67031478881836},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":2,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.93581199645996},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":3,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-2.0071048736572266},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":3,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-13.980289459228516},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":3,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-16.085025787353516},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":4,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-4.427236557006836},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":4,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-14.482124328613281},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":4,\\\"r\\\":\\\"P108\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-15.469401359558105},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":6,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[1],\\\"score\\\":-15.285942077636719},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":6,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-16.039936065673828},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":6,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1],\\\"score\\\":-19.236722946166992},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":7,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-7.117012977600098},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":7,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[1],\\\"score\\\":-14.452709197998047},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":7,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[1],\\\"score\\\":-16.16189193725586},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":9,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.612022399902344},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":9,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.883363723754883},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.940235137939453},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":10,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-20.53162384033203},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":10,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.668039321899414},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":10,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.12806510925293},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":11,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.657251358032227},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":11,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[1],\\\"score\\\":-22.353445053100586},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":11,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[1],\\\"score\\\":-22.628162384033203},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":12,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.56743621826172},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":12,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.7761173248291},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":12,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.802156448364258},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":13,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-18.34552574157715},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":13,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-21.345245361328125},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":13,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-21.350692749023438},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":14,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[2],\\\"score\\\":-21.576215744018555},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":14,\\\"r\\\":\\\"P400\\\",\\\"evidence\\\":[2],\\\"score\\\":-21.83979606628418},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":14,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[2],\\\"score\\\":-22.87384033203125},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":15,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-23.41214942932129},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":15,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-25.165916442871094},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":15,\\\"r\\\":\\\"P364\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-25.180898666381836},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":16,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-16.47821807861328},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":16,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-17.47647476196289},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":16,\\\"r\\\":\\\"P172\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-19.65420913696289},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":17,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[3],\\\"score\\\":-15.602682113647461},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":17,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[3],\\\"score\\\":-20.19228172302246},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":17,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[3],\\\"score\\\":-20.95561981201172},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":18,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.81693458557129},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":18,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.05913734436035},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":18,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.169227600097656},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":0,\\\"r\\\":\\\"P400\\\",\\\"evidence\\\":[1],\\\"score\\\":-30.335575103759766},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":0,\\\"r\\\":\\\"P205\\\",\\\"evidence\\\":[1],\\\"score\\\":-31.237089157104492},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":0,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[1],\\\"score\\\":-31.658187866210938},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":1,\\\"r\\\":\\\"P155\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.626047134399414},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":1,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-28.477859497070312},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":1,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-28.798505783081055},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":2,\\\"r\\\":\\\"P580\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.72319793701172},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":2,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.800453186035156},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":2,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.543933868408203},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":3,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-28.757610321044922},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":3,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-28.915699005126953},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":3,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-30.619220733642578},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":4,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1],\\\"score\\\":-25.652027130126953},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[1],\\\"score\\\":-25.73176383972168},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":4,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[1],\\\"score\\\":-25.956077575683594},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":5,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.271095275878906},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.75581932067871},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":5,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[1],\\\"score\\\":-24.5407657623291},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":6,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-27.56806755065918},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":6,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[1],\\\"score\\\":-29.489328384399414},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":6,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-29.955623626708984},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":7,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-28.611160278320312},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":7,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[1],\\\"score\\\":-28.725048065185547},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":7,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-29.545610427856445},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":8,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[1],\\\"score\\\":-30.581256866455078},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":8,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[1],\\\"score\\\":-31.01825714111328},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":8,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-31.06687355041504},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":10,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-25.1586971282959},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":10,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[1],\\\"score\\\":-27.306732177734375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":10,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1],\\\"score\\\":-27.832441329956055},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":11,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1],\\\"score\\\":-24.116029739379883},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":11,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-24.479921340942383},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":11,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-24.95216941833496},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":12,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-26.441980361938477},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":12,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1],\\\"score\\\":-27.858596801757812},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":12,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1],\\\"score\\\":-28.133197784423828},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":13,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-30.123790740966797},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":13,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-30.55086326599121},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":13,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1],\\\"score\\\":-30.999311447143555},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":14,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-31.54079818725586},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":14,\\\"r\\\":\\\"P155\\\",\\\"evidence\\\":[1],\\\"score\\\":-32.17679214477539},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":14,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[1],\\\"score\\\":-32.27409744262695},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":15,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-26.683231353759766},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":15,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1],\\\"score\\\":-27.838449478149414},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":15,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[1],\\\"score\\\":-28.430288314819336},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":16,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.28378677368164},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":16,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.733518600463867},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":16,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-28.09536361694336},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":17,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-33.24646759033203},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":17,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-34.579505920410156},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":17,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-34.89878463745117},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":18,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-31.556385040283203},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":18,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-32.11661911010742},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":18,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-32.23531723022461},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":0,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[1],\\\"score\\\":-17.26881980895996},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":0,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[1],\\\"score\\\":-18.168697357177734},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":0,\\\"r\\\":\\\"P800\\\",\\\"evidence\\\":[1],\\\"score\\\":-19.96236801147461},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":1,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.57594871520996},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":1,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.47667121887207},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":1,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.494728088378906},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":2,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-18.56275749206543},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":2,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[1],\\\"score\\\":-20.14931297302246},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":2,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-20.840429306030273},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":3,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.11899757385254},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":3,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.995956420898438},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":3,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.226953506469727},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":4,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.680906295776367},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.709184646606445},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1001\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.923789978027344},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[1],\\\"score\\\":-14.929183006286621},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":5,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[1],\\\"score\\\":-16.32843589782715},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":5,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-17.02412986755371},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":6,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-8.056291580200195},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":6,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[1],\\\"score\\\":-16.596792221069336},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":6,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[1],\\\"score\\\":-17.603225708007812},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":7,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-9.184304237365723},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":7,\\\"r\\\":\\\"P25\\\",\\\"evidence\\\":[1],\\\"score\\\":-14.727970123291016},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":7,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[1],\\\"score\\\":-15.16051197052002},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":8,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-22.44668197631836},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":8,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.870054244995117},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":8,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[1],\\\"score\\\":-24.894344329833984},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":9,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-20.37150001525879},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":9,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.135169982910156},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":9,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.765682220458984},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":11,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-15.031770706176758},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":11,\\\"r\\\":\\\"P25\\\",\\\"evidence\\\":[1],\\\"score\\\":-17.112260818481445},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":11,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[1],\\\"score\\\":-17.51050567626953},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":12,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.10664176940918},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":12,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.39385223388672},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":12,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.711790084838867},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":13,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-8.556818962097168},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":13,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[1],\\\"score\\\":-16.642963409423828},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":13,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[1],\\\"score\\\":-16.658205032348633},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":14,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-24.664306640625},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":14,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-24.82982063293457},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":14,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-25.84198760986328},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":15,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.145187377929688},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":15,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.16191291809082},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":15,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.40016746520996},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":16,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-19.81062889099121},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":16,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-20.892784118652344},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":16,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-21.5662899017334},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":17,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-25.810848236083984},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":17,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-26.84730339050293},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":17,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-27.564470291137695},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":18,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.725875854492188},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":18,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.370744705200195},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":18,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.398080825805664},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":0,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.34929656982422},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":0,\\\"r\\\":\\\"P205\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.884620666503906},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":0,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.18640899658203},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":1,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.171886444091797},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":1,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.899450302124023},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":1,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.401689529418945},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":2,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-17.902332305908203},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":2,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[1],\\\"score\\\":-20.801034927368164},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":2,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.699689865112305},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":3,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.637235641479492},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":3,\\\"r\\\":\\\"P1441\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.98202896118164},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":3,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.132160186767578},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1001\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.066667556762695},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":4,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-19.912073135375977},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":4,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.012813568115234},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":6,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.03862953186035},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":6,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[1],\\\"score\\\":-22.419414520263672},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":6,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.384435653686523},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":7,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-22.142072677612305},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":7,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.8280029296875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":7,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[1],\\\"score\\\":-25.09673500061035},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":8,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-24.064651489257812},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":8,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[1],\\\"score\\\":-24.343830108642578},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":8,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[1],\\\"score\\\":-25.18009376525879},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":9,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-19.12616729736328},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":9,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-20.69657325744629},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":9,\\\"r\\\":\\\"P570\\\",\\\"evidence\\\":[1],\\\"score\\\":-22.154821395874023},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":10,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-17.271953582763672},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":10,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-17.284090042114258},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":10,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[1],\\\"score\\\":-18.364625930786133},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":12,\\\"r\\\":\\\"P102\\\",\\\"evidence\\\":[1],\\\"score\\\":-20.5594425201416},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":12,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[1],\\\"score\\\":-20.93866539001465},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":12,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.28795051574707},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":13,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-21.500823974609375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":13,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-22.237178802490234},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":13,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-23.430410385131836},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":14,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-24.763916015625},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":14,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-25.8553524017334},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":14,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-26.24052619934082},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":15,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.551677703857422},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":15,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.783178329467773},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":15,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.106245040893555},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":16,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-22.130210876464844},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":16,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-22.867015838623047},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":16,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-22.999263763427734},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":17,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-27.80078887939453},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":17,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-28.243846893310547},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":17,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-28.842105865478516},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":18,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.661376953125},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":18,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.59457015991211},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":18,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.701889038085938},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":0,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.2297306060791},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":0,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-29.213809967041016},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":0,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-29.993301391601562},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":1,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.027706146240234},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":1,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.022340774536133},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":1,\\\"r\\\":\\\"P118\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.499595642089844},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":2,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.702970504760742},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":2,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.478885650634766},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":2,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1],\\\"score\\\":-24.246597290039062},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":3,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.999679565429688},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":3,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.02721405029297},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":3,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.65018653869629},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":4,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.220979690551758},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":4,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.425695419311523},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":4,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.824769973754883},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":6,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[1],\\\"score\\\":-25.737567901611328},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":6,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-27.065980911254883},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":6,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-27.276147842407227},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":7,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-26.744232177734375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":7,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1],\\\"score\\\":-27.433494567871094},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":7,\\\"r\\\":\\\"P118\\\",\\\"evidence\\\":[1],\\\"score\\\":-27.703123092651367},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":8,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.68509864807129},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":8,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.06759262084961},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":8,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.105195999145508},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":9,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-21.6157283782959},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":9,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1],\\\"score\\\":-22.380746841430664},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":9,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.577396392822266},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":10,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-20.84010887145996},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":10,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.088071823120117},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":10,\\\"r\\\":\\\"P118\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.981735229492188},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":11,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[1],\\\"score\\\":-18.456562042236328},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":11,\\\"r\\\":\\\"P162\\\",\\\"evidence\\\":[1],\\\"score\\\":-19.545907974243164},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":11,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[1],\\\"score\\\":-20.07727813720703},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":13,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-25.734180450439453},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":13,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-27.01349639892578},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":13,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-27.264636993408203},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":14,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-26.765050888061523},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":14,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-27.5279483795166},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":14,\\\"r\\\":\\\"P118\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-28.511497497558594},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":15,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-24.012733459472656},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":15,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-26.519256591796875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":15,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-27.966367721557617},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":16,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-24.529993057250977},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":16,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-25.43317222595215},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":16,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-25.72567367553711},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":17,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.68462371826172},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":17,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.213226318359375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":17,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.6646671295166},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":18,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.789094924926758},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":18,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.41078758239746},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":18,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.981473922729492},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":0,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-12.545401573181152},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":0,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-14.124406814575195},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":0,\\\"r\\\":\\\"P800\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-14.558652877807617},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":1,\\\"r\\\":\\\"P1344\\\",\\\"evidence\\\":[0],\\\"score\\\":-15.423983573913574},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":1,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.408687591552734},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":1,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.312381744384766},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":2,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.214473724365234},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":2,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.531028747558594},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":2,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.20548439025879},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":3,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.151649475097656},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":3,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.9249210357666},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":3,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.617900848388672},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":4,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[2],\\\"score\\\":-15.392383575439453},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":4,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[2],\\\"score\\\":-17.68118667602539},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":4,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[2],\\\"score\\\":-19.769344329833984},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":6,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-11.111534118652344},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":6,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-11.217514038085938},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":6,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-11.825187683105469},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":7,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":0.8082046508789062},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":7,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1],\\\"score\\\":-12.346399307250977},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":7,\\\"r\\\":\\\"P108\\\",\\\"evidence\\\":[1],\\\"score\\\":-13.041504859924316},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":8,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-20.943918228149414},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":8,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-22.924882888793945},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":8,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-23.915380477905273},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":9,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[1],\\\"score\\\":-25.53502655029297},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":9,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1],\\\"score\\\":-25.633514404296875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":9,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-25.82683563232422},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":10,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1],\\\"score\\\":-3.8679189682006836},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":10,\\\"r\\\":\\\"P25\\\",\\\"evidence\\\":[1],\\\"score\\\":-10.739500045776367},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":10,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1],\\\"score\\\":-13.94851016998291},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":11,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-17.884485244750977},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":11,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-20.530244827270508},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":11,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-21.922325134277344},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":12,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-24.530033111572266},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":12,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-24.74419593811035},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":12,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-25.867961883544922},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":14,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[2],\\\"score\\\":-23.509517669677734},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":14,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[2],\\\"score\\\":-24.062593460083008},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":14,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[2],\\\"score\\\":-24.34494972229004},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":15,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[2],\\\"score\\\":-21.107213973999023},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":15,\\\"r\\\":\\\"P172\\\",\\\"evidence\\\":[2],\\\"score\\\":-21.224088668823242},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":15,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[2],\\\"score\\\":-21.462661743164062},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":16,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[2],\\\"score\\\":-7.815303802490234},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":16,\\\"r\\\":\\\"P172\\\",\\\"evidence\\\":[2],\\\"score\\\":-9.224056243896484},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":16,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[2],\\\"score\\\":-13.644739151000977},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":17,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-25.703048706054688},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":17,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-27.170745849609375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":17,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-27.234668731689453},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":18,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.9913330078125},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":18,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.31467056274414},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":13,\\\"t_idx\\\":18,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.364667892456055},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":0,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-25.108325958251953},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":0,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-26.93352508544922},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":0,\\\"r\\\":\\\"P400\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-27.608619689941406},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":1,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-25.88494300842285},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":1,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-26.205968856811523},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":1,\\\"r\\\":\\\"P155\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-26.72294044494629},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":2,\\\"r\\\":\\\"P580\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.871822357177734},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":2,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.667678833007812},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":2,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.354219436645508},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":3,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-19.28624725341797},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":3,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-23.057147979736328},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":3,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-24.655372619628906},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":6,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-24.30094337463379},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":6,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-24.45260238647461},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":6,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-25.36969566345215},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":7,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-25.968338012695312},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":7,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-26.49686050415039},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":7,\\\"r\\\":\\\"P137\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-28.185544967651367},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":8,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[2],\\\"score\\\":-26.131895065307617},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":8,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[2],\\\"score\\\":-26.1976261138916},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":8,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[2],\\\"score\\\":-27.0140323638916},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[1],\\\"score\\\":-25.6038761138916},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":9,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[1],\\\"score\\\":-26.413536071777344},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":9,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[1],\\\"score\\\":-26.588972091674805},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":10,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-25.503826141357422},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":10,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-25.7908992767334},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":10,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-26.164718627929688},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":11,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-25.05060577392578},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":11,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-25.196704864501953},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":11,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-25.506431579589844},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":12,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-24.844989776611328},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":12,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-27.20168113708496},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":12,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[1,2],\\\"score\\\":-27.286666870117188},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":13,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[2],\\\"score\\\":-20.96980094909668},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":13,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[2],\\\"score\\\":-22.147235870361328},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":13,\\\"r\\\":\\\"P162\\\",\\\"evidence\\\":[2],\\\"score\\\":-24.172847747802734},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":15,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[2],\\\"score\\\":-25.731796264648438},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":15,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[2],\\\"score\\\":-26.97313117980957},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":15,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[2],\\\"score\\\":-27.33792495727539},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":16,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[2],\\\"score\\\":-16.670909881591797},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":16,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[2],\\\"score\\\":-19.651159286499023},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":16,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[2],\\\"score\\\":-22.867813110351562},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":17,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[2],\\\"score\\\":-29.32429313659668},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":17,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[2],\\\"score\\\":-31.90127944946289},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":17,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[2],\\\"score\\\":-32.134002685546875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":18,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-25.171463012695312},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":18,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-27.081682205200195},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":14,\\\"t_idx\\\":18,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-27.789161682128906},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":0,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.57975196838379},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":0,\\\"r\\\":\\\"P205\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.96466827392578},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":0,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-31.050289154052734},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":1,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.736970901489258},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":1,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.479467391967773},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":1,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.900304794311523},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":2,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.332778930664062},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":2,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.06410789489746},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":2,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.472675323486328},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":3,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.077558517456055},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":3,\\\"r\\\":\\\"P171\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.423377990722656},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":3,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.876375198364258},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":4,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-22.867786407470703},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":4,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-23.421554565429688},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1001\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-24.536701202392578},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":5,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-18.31422233581543},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-20.61053466796875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":5,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-21.25783920288086},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":6,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-25.592514038085938},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":6,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-26.786771774291992},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":6,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-27.72024154663086},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":7,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.712671279907227},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":7,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-28.143970489501953},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":7,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-28.177461624145508},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":8,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-27.249462127685547},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":8,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-27.983400344848633},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":8,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-28.39069366455078},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":9,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.16596221923828},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":9,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.525163650512695},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":9,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[1],\\\"score\\\":-23.696550369262695},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":10,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.51365852355957},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":10,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.879472732543945},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":10,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.346019744873047},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":11,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.896697998046875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":11,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.4178409576416},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":11,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.648418426513672},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":12,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-24.68132209777832},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":12,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-24.90966796875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":12,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-25.25216293334961},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":13,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[2],\\\"score\\\":-25.954509735107422},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":13,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[2],\\\"score\\\":-26.475475311279297},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":13,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[2],\\\"score\\\":-26.871688842773438},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":14,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[2],\\\"score\\\":-26.65700340270996},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":14,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[2],\\\"score\\\":-28.2175350189209},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":14,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[2],\\\"score\\\":-28.359067916870117},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":16,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[2],\\\"score\\\":-17.672605514526367},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":16,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[2],\\\"score\\\":-18.583974838256836},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":16,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[2],\\\"score\\\":-19.03498649597168},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":17,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-29.766246795654297},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":17,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-31.035789489746094},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":17,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-31.446744918823242},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":18,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.757831573486328},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":18,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.356948852539062},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":15,\\\"t_idx\\\":18,\\\"r\\\":\\\"P171\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.429527282714844},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":0,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.42911720275879},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":0,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.722087860107422},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":0,\\\"r\\\":\\\"P400\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.226398468017578},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":1,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.395156860351562},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":1,\\\"r\\\":\\\"P155\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.203121185302734},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":1,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.40805435180664},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":2,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.155128479003906},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":2,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.891815185546875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":2,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.31345558166504},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":3,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.89067268371582},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":3,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.012073516845703},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":3,\\\"r\\\":\\\"P171\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.35607147216797},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":4,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[2],\\\"score\\\":-7.831539154052734},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1001\\\",\\\"evidence\\\":[2],\\\"score\\\":-19.306468963623047},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":4,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[2],\\\"score\\\":-19.54962158203125},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-7.490976810455322},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":5,\\\"r\\\":\\\"P27\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-9.70700740814209},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":5,\\\"r\\\":\\\"P495\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-10.391053199768066},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":6,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[2],\\\"score\\\":-17.440927505493164},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":6,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[2],\\\"score\\\":-17.511205673217773},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":6,\\\"r\\\":\\\"P6\\\",\\\"evidence\\\":[2],\\\"score\\\":-17.65985679626465},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":7,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.598953247070312},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":7,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.6982479095459},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":7,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.2244873046875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":8,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-23.698747634887695},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":8,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-24.764833450317383},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":8,\\\"r\\\":\\\"P6\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-25.738698959350586},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":9,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.66697883605957},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":9,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.009124755859375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":9,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.921857833862305},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":10,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-23.153648376464844},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":10,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-23.280424118041992},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":10,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-23.847259521484375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":11,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-22.559133529663086},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":11,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-22.769939422607422},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":11,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-23.51133918762207},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":12,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-24.301414489746094},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":12,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-24.508623123168945},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":12,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-25.406877517700195},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":13,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[2],\\\"score\\\":-17.333396911621094},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":13,\\\"r\\\":\\\"P6\\\",\\\"evidence\\\":[2],\\\"score\\\":-17.801725387573242},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":13,\\\"r\\\":\\\"P40\\\",\\\"evidence\\\":[2],\\\"score\\\":-18.061382293701172},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":14,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[2],\\\"score\\\":-25.603832244873047},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":14,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[2],\\\"score\\\":-25.803884506225586},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":14,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[2],\\\"score\\\":-26.273563385009766},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":15,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[2],\\\"score\\\":-17.227357864379883},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":15,\\\"r\\\":\\\"P172\\\",\\\"evidence\\\":[2],\\\"score\\\":-18.39400291442871},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":15,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[2],\\\"score\\\":-19.720401763916016},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":17,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-26.89739227294922},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":17,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-27.65492057800293},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":17,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-28.008792877197266},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":18,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.154382705688477},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":18,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.21209716796875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":16,\\\"t_idx\\\":18,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.276229858398438},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":0,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-22.501317977905273},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":0,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-25.450523376464844},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":0,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-26.15431785583496},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":1,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.23533058166504},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":1,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.815933227539062},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":1,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.3800048828125},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":2,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.042400360107422},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":2,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.081785202026367},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":2,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.281192779541016},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":3,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-11.32913875579834},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":3,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.489856719970703},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":3,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.734691619873047},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":4,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,2,3],\\\"score\\\":-4.768796920776367},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1001\\\",\\\"evidence\\\":[0,2,3],\\\"score\\\":-20.530473709106445},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":4,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,2,3],\\\"score\\\":-21.1462459564209},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":5,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,3],\\\"score\\\":15.549283981323242},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":5,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-12.169244766235352},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":5,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-12.577645301818848},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":6,\\\"r\\\":\\\"P50\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.922073364257812},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":6,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.63222312927246},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":6,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.691801071166992},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":7,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.544973373413086},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":7,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.407629013061523},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":7,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.431154251098633},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":8,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[3],\\\"score\\\":-10.100671768188477},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":8,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[3],\\\"score\\\":-18.048288345336914},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":8,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[3],\\\"score\\\":-18.872661590576172},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.86845588684082},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":9,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.974468231201172},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":9,\\\"r\\\":\\\"P585\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.40106964111328},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":10,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-25.28901481628418},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":10,\\\"r\\\":\\\"P58\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-26.135290145874023},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":10,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1,2],\\\"score\\\":-27.063220977783203},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":11,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-24.619319915771484},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":11,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-24.626108169555664},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":11,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-24.995351791381836},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":12,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.632938385009766},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":12,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.94746971130371},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":12,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.555444717407227},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":13,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-21.73698616027832},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":13,\\\"r\\\":\\\"P50\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-22.279035568237305},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":13,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-22.841796875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":14,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[2],\\\"score\\\":-25.01353645324707},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":14,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[2],\\\"score\\\":-26.501375198364258},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":14,\\\"r\\\":\\\"P155\\\",\\\"evidence\\\":[2],\\\"score\\\":-27.0567569732666},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":15,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-27.265396118164062},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":15,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-28.11819839477539},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":15,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-28.787633895874023},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[2,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":16,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-14.745743751525879},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":16,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-21.699291229248047},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":16,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[2,3],\\\"score\\\":-22.837427139282227},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":18,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":18,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-28.488605499267578},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":18,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-28.992136001586914},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":17,\\\"t_idx\\\":18,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-29.022220611572266},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":0,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-27.231708526611328},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":0,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-28.0195369720459},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":0,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-28.22309112548828},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":1,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.698699951171875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":1,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.16495132446289},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":1,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.205110549926758},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":2,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.888914108276367},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":2,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.12348175048828},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":2,\\\"r\\\":\\\"P205\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.243589401245117},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":3,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.97553062438965},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":3,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.400054931640625},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":3,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.48409652709961},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":4,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.371788024902344},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1001\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.463891983032227},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":4,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.858226776123047},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":6,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.11897087097168},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":6,\\\"r\\\":\\\"P170\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.95340919494629},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":6,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.02601432800293},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":7,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.928024291992188},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":7,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.289155960083008},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":7,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.982004165649414},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":8,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.373516082763672},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":8,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.24800682067871},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":8,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.254615783691406},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":9,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-20.394155502319336},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":9,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.452302932739258},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":9,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.136445999145508},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":10,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-20.318662643432617},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":10,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.840282440185547},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":10,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.023454666137695},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":11,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-20.559709548950195},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":11,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-20.84222412109375},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":11,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.431787490844727},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":12,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.087556838989258},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":12,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.81317138671875},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":12,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.390399932861328},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":13,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.075056076049805},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":13,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.174015045166016},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":13,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.866605758666992},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,2],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":14,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-25.08240509033203},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":14,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-26.20568084716797},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":14,\\\"r\\\":\\\"P118\\\",\\\"evidence\\\":[0,2],\\\"score\\\":-27.330814361572266},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":15,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.201730728149414},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":15,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.99332046508789},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":15,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.58082389831543},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":16,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":16,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.755483627319336},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":16,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.870046615600586},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":16,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.129756927490234},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":17,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":17,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-28.689537048339844},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":17,\\\"r\\\":\\\"P551\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-29.882064819335938},{\\\"title\\\":\\\"Washington Place (West Virginia)\\\",\\\"h_idx\\\":18,\\\"t_idx\\\":17,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-30.17490005493164},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":-6.947835922241211},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0],\\\"score\\\":-11.017875671386719},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":2,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-11.569250106811523},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0,1],\\\"score\\\":8.711576461791992},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-12.940011024475098},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":4,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-15.075746536254883},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":0,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-9.491125106811523},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":0,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0],\\\"score\\\":-10.608945846557617},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":0,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":-13.366666793823242},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":7,\\\"r\\\":\\\"P749\\\",\\\"evidence\\\":[0],\\\"score\\\":-1.1932373046875},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":7,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":-4.783865451812744},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":7,\\\"r\\\":\\\"P127\\\",\\\"evidence\\\":[0],\\\"score\\\":-5.981253623962402},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":3,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":3.1616811752319336},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":3,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-8.885332107543945},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":3,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-9.606433868408203},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":1.728097915649414},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":9,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-5.892742156982422},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":9,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-8.364336013793945},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":1.1147117614746094},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":9,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-4.742542266845703},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":9,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-10.077286720275879},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":3,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":8.662054061889648},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":3,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":-3.3690357208251953},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":3,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-8.790180206298828},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":7,\\\"r\\\":\\\"P108\\\",\\\"evidence\\\":[5],\\\"score\\\":4.415596008300781},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":7,\\\"r\\\":\\\"P178\\\",\\\"evidence\\\":[5],\\\"score\\\":-12.018865585327148},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":12,\\\"t_idx\\\":7,\\\"r\\\":\\\"P69\\\",\\\"evidence\\\":[5],\\\"score\\\":-13.304216384887695},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":9,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":3.0771484375},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":9,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":0.22355937957763672},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":9,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":-9.001901626586914},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.494394302368164},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.691726684570312},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":1,\\\"r\\\":\\\"P463\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.296377182006836},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-8.4835205078125},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-13.405561447143555},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":3,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-13.712631225585938},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-7.250646591186523},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-9.474996566772461},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":5,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-11.719752311706543},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":6,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-8.436788558959961},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":6,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-11.128647804260254},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":6,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-13.22032642364502},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":7,\\\"r\\\":\\\"P749\\\",\\\"evidence\\\":[0],\\\"score\\\":-4.582836151123047},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":7,\\\"r\\\":\\\"P178\\\",\\\"evidence\\\":[0],\\\"score\\\":-7.500817775726318},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":7,\\\"r\\\":\\\"P108\\\",\\\"evidence\\\":[0],\\\"score\\\":-7.849102973937988},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":8,\\\"r\\\":\\\"P463\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-29.13332176208496},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":8,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-29.32899284362793},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":8,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-29.526769638061523},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-3.7671356201171875},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":9,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-15.60536003112793},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":9,\\\"r\\\":\\\"P495\\\",\\\"evidence\\\":[0],\\\"score\\\":-15.761947631835938},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":10,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.664968490600586},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":10,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.89031410217285},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":10,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.71644401550293},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":11,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.858444213867188},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":11,\\\"r\\\":\\\"P136\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.005769729614258},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":11,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.882232666015625},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":12,\\\"r\\\":\\\"P58\\\",\\\"evidence\\\":[0],\\\"score\\\":-15.289647102355957},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":12,\\\"r\\\":\\\"P86\\\",\\\"evidence\\\":[0],\\\"score\\\":-15.98243236541748},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":12,\\\"r\\\":\\\"P178\\\",\\\"evidence\\\":[0],\\\"score\\\":-16.74604034423828},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":13,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-27.752761840820312},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":13,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-28.46280288696289},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":13,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-28.945316314697266},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":14,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.985260009765625},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":14,\\\"r\\\":\\\"P463\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.008472442626953},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":14,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.171483993530273},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":15,\\\"r\\\":\\\"P463\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.393268585205078},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":15,\\\"r\\\":\\\"P58\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.141263961791992},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":0,\\\"t_idx\\\":15,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.566402435302734},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":0,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.04437255859375},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":0,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.082719802856445},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":0,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.110942840576172},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":2,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.137672424316406},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":2,\\\"r\\\":\\\"P171\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.76180076599121},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":2,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.8316650390625},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":3,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.62483787536621},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":3,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.63820457458496},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":3,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.38808250427246},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":4,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.468677520751953},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":4,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.594097137451172},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":4,\\\"r\\\":\\\"P205\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.655628204345703},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":5,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.198720932006836},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":5,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.18775177001953},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":5,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.482765197753906},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":6,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.33940887451172},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":6,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.60859489440918},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":6,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.90068817138672},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":7,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.79055404663086},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":7,\\\"r\\\":\\\"P178\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.099058151245117},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":7,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.49517250061035},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":8,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[3],\\\"score\\\":-28.847047805786133},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":8,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[3],\\\"score\\\":-29.291263580322266},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":8,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[3],\\\"score\\\":-29.39942169189453},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":9,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.057954788208008},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":9,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.38684844970703},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":9,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.335777282714844},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":10,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-29.85472869873047},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":10,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-30.304197311401367},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":10,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-31.14580726623535},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":11,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-27.99498176574707},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":11,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-29.21831512451172},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":11,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-30.781286239624023},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":12,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.90513801574707},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":12,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.661306381225586},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":12,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.10584831237793},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":13,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[5],\\\"score\\\":-20.434968948364258},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":13,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[5],\\\"score\\\":-22.19562530517578},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":13,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[5],\\\"score\\\":-22.2661075592041},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":14,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.616737365722656},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":14,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.85706329345703},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":14,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.87896156311035},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":15,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.174341201782227},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":15,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.177249908447266},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":1,\\\"t_idx\\\":15,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.915678024291992},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.010913848876953},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.158342361450195},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":1,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.376678466796875},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":3,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-7.646364212036133},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":3,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0],\\\"score\\\":-10.764965057373047},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":3,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-10.864920616149902},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":4,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0],\\\"score\\\":-8.91192626953125},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":4,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-13.989548683166504},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":4,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-15.332728385925293},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":5,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-8.672988891601562},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":5,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-10.364297866821289},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":5,\\\"r\\\":\\\"P740\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-10.542827606201172},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":6,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-10.849220275878906},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":6,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-14.06120491027832},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":6,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-15.452719688415527},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":8,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-26.85492515563965},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":8,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-27.153467178344727},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":8,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-27.19635772705078},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0],\\\"score\\\":-5.750702857971191},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":9,\\\"r\\\":\\\"P1056\\\",\\\"evidence\\\":[0],\\\"score\\\":-9.840442657470703},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":9,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-10.19326114654541},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":10,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.871742248535156},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":10,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.954307556152344},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":10,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.987977981567383},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":11,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-16.05739974975586},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":11,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-20.63752555847168},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":11,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-20.979625701904297},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":12,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-12.270034790039062},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":12,\\\"r\\\":\\\"P178\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-13.177509307861328},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":12,\\\"r\\\":\\\"P58\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-13.21528434753418},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":13,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[5],\\\"score\\\":-23.321884155273438},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":13,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[5],\\\"score\\\":-23.42463493347168},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":13,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[5],\\\"score\\\":-24.37476921081543},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,6],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":14,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-14.122772216796875},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":14,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-17.2097110748291},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":14,\\\"r\\\":\\\"P737\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-18.845670700073242},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,6],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":15,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-17.621530532836914},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":15,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-19.94554901123047},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":2,\\\"t_idx\\\":15,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-20.162981033325195},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":0,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-9.46287727355957},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":0,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-17.6851863861084},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":0,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.057479858398438},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":1,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.15534019470215},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":1,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.397239685058594},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":1,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.5878849029541},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":2,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-11.50663948059082},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":2,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-12.469015121459961},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":2,\\\"r\\\":\\\"P108\\\",\\\"evidence\\\":[0],\\\"score\\\":-14.216056823730469},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":4,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-14.796701431274414},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.23114776611328},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":4,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.676410675048828},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":5,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-11.668560981750488},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":5,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-11.787018775939941},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":5,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-12.864809036254883},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":6,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-10.698094367980957},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":6,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-11.697711944580078},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":6,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-14.242810249328613},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":7,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-10.138359069824219},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":7,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-10.203482627868652},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":7,\\\"r\\\":\\\"P178\\\",\\\"evidence\\\":[0],\\\"score\\\":-10.619842529296875},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":8,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-24.47126007080078},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":8,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-25.537134170532227},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":8,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-25.563257217407227},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":10,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-20.387062072753906},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":10,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-20.856626510620117},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":10,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-21.651283264160156},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":11,\\\"r\\\":\\\"P206\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-16.411357879638672},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":11,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-16.864477157592773},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":11,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-17.50458335876465},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":12,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-17.625545501708984},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":12,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-18.837533950805664},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":12,\\\"r\\\":\\\"P86\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-19.198087692260742},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":13,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-22.024850845336914},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":13,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-23.94176483154297},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":13,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-25.027402877807617},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":14,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.87917137145996},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":14,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.204294204711914},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":14,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.384492874145508},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":15,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.909929275512695},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":15,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.46116828918457},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":3,\\\"t_idx\\\":15,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.475215911865234},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":0,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-19.11055564880371},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":0,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.3989315032959},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":0,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.433151245117188},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":1,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.86079978942871},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":1,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-31.803255081176758},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":1,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-32.250648498535156},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":2,\\\"r\\\":\\\"P108\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.478561401367188},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":2,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.649295806884766},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":2,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.790611267089844},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":3,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-16.151931762695312},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":3,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-17.456199645996094},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":3,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.42630958557129},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":5,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.533592224121094},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":5,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.52241325378418},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":5,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.93085479736328},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":6,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.392505645751953},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":6,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.855525970458984},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":6,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.397014617919922},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":7,\\\"r\\\":\\\"P178\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.55412483215332},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":7,\\\"r\\\":\\\"P749\\\",\\\"evidence\\\":[0],\\\"score\\\":-21.588882446289062},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":7,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.181278228759766},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":8,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.07543182373047},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":8,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.69001007080078},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":8,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-31.93442153930664},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":9,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.543676376342773},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":9,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.452707290649414},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":9,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.800939559936523},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":10,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.512075424194336},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":10,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.605131149291992},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":10,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-31.7740421295166},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":11,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.47504997253418},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":11,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.776954650878906},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":11,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.310056686401367},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":12,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.410655975341797},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":12,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.617490768432617},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":12,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.441940307617188},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":13,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-30.88652801513672},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":13,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-32.78002166748047},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":13,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-33.64719009399414},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":14,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-31.389522552490234},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":14,\\\"r\\\":\\\"P264\\\",\\\"evidence\\\":[0],\\\"score\\\":-31.41710662841797},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":14,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0],\\\"score\\\":-31.533309936523438},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":15,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.56778907775879},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":15,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.58245277404785},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":4,\\\"t_idx\\\":15,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.672853469848633},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":0,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-14.976242065429688},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":0,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.208229064941406},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":0,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.43463897705078},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":1,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-18.565383911132812},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":1,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.116436004638672},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":1,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.19425392150879},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":2,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-9.401909828186035},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":2,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-14.489069938659668},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":2,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-14.867002487182617},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":4,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.63511848449707},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":4,\\\"r\\\":\\\"P206\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-19.404706954956055},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":4,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-19.531829833984375},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":6,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[1],\\\"score\\\":-19.05829620361328},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":6,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[1],\\\"score\\\":-19.095735549926758},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":6,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[1],\\\"score\\\":-19.580656051635742},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":7,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-9.967155456542969},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":7,\\\"r\\\":\\\"P749\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-12.406723022460938},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":7,\\\"r\\\":\\\"P178\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-13.04551887512207},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":8,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.343528747558594},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":8,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.356136322021484},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":8,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.42481231689453},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":10,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-19.825565338134766},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":10,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.85279083251953},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":10,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.133214950561523},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":11,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-17.20539093017578},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":11,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.57737922668457},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":11,\\\"r\\\":\\\"P206\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.732501983642578},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":12,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1,5],\\\"score\\\":-14.944526672363281},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":12,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1,5],\\\"score\\\":-19.462268829345703},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":12,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1,5],\\\"score\\\":-21.17957878112793},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":13,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.669649124145508},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":13,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.874897003173828},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":13,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.011028289794922},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":14,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.35572052001953},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":14,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.415651321411133},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":14,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.748876571655273},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":15,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.449806213378906},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":15,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.895605087280273},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":5,\\\"t_idx\\\":15,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.89082908630371},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":0,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-16.5987548828125},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":0,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.300077438354492},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":0,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.343700408935547},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":1,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.750167846679688},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":1,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.38838005065918},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":1,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-25.53160285949707},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":2,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-10.700660705566406},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":2,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-14.676923751831055},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":2,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-15.785752296447754},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":3,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":3.856283187866211},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":3,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-9.786556243896484},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":3,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-9.94398307800293},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":4,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-17.494096755981445},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":4,\\\"r\\\":\\\"P131\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.484798431396484},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":4,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-18.865556716918945},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":5,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[1],\\\"score\\\":-14.386190414428711},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":5,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[1],\\\"score\\\":-19.452367782592773},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":5,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[1],\\\"score\\\":-19.73563575744629},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":7,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-10.888036727905273},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":7,\\\"r\\\":\\\"P178\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-15.445388793945312},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":7,\\\"r\\\":\\\"P749\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-15.992769241333008},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":8,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-19.575809478759766},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":8,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.588685989379883},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":8,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.694091796875},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":10,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-19.675418853759766},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":10,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.033004760742188},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":10,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.210206985473633},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":11,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-17.034587860107422},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":11,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.483261108398438},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":11,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-22.74152183532715},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":12,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1,5],\\\"score\\\":-14.751297950744629},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":12,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1,5],\\\"score\\\":-20.178152084350586},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":12,\\\"r\\\":\\\"P6\\\",\\\"evidence\\\":[0,1,5],\\\"score\\\":-21.35379981994629},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":13,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-21.144287109375},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":13,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.060277938842773},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":13,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.67018699645996},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":14,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.904394149780273},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":14,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.4919490814209},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":14,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.9739933013916},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":15,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.410446166992188},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":15,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.595632553100586},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":6,\\\"t_idx\\\":15,\\\"r\\\":\\\"P37\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.909412384033203},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":0,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0],\\\"score\\\":-9.291869163513184},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":0,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":-13.40446662902832},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":0,\\\"r\\\":\\\"P527\\\",\\\"evidence\\\":[0],\\\"score\\\":-13.908027648925781},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":1,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.02767562866211},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":1,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.231639862060547},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":1,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.340946197509766},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":2,\\\"r\\\":\\\"P1056\\\",\\\"evidence\\\":[0],\\\"score\\\":-4.8090972900390625},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":2,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0],\\\"score\\\":-7.184810638427734},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":2,\\\"r\\\":\\\"P108\\\",\\\"evidence\\\":[0],\\\"score\\\":-8.382850646972656},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":3,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-9.362186431884766},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":3,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":-9.668428421020508},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":3,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0],\\\"score\\\":-10.607076644897461},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":4,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.122644424438477},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":4,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.824024200439453},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":4,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.063922882080078},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":5,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-7.606746673583984},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":5,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-11.110225677490234},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":5,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-16.026594161987305},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":6,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-9.799142837524414},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":6,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-13.212965965270996},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":6,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-17.89830207824707},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":8,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[3],\\\"score\\\":-29.605562210083008},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":8,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[3],\\\"score\\\":-30.934770584106445},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":8,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[3],\\\"score\\\":-31.493793487548828},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":9,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0,4,5],\\\"score\\\":-13.617172241210938},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":9,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,4,5],\\\"score\\\":-13.673526763916016},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[0,4,5],\\\"score\\\":-13.928226470947266},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":10,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-24.97310447692871},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":10,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-25.67245101928711},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":10,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-25.744178771972656},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":11,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-17.69106101989746},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":11,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-19.8242130279541},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":11,\\\"r\\\":\\\"P166\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-20.987464904785156},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":12,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[5],\\\"score\\\":-14.293783187866211},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":12,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[5],\\\"score\\\":-16.652254104614258},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":12,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[5],\\\"score\\\":-16.84220314025879},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":13,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[5],\\\"score\\\":-26.783872604370117},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":13,\\\"r\\\":\\\"P159\\\",\\\"evidence\\\":[5],\\\"score\\\":-27.835525512695312},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":13,\\\"r\\\":\\\"P1412\\\",\\\"evidence\\\":[5],\\\"score\\\":-27.967866897583008},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,6],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":14,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-16.47425079345703},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":14,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-21.87151336669922},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":14,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-22.00153923034668},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,6],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":15,\\\"r\\\":\\\"P355\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-21.382843017578125},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":15,\\\"r\\\":\\\"P1056\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-21.53511619567871},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":7,\\\"t_idx\\\":15,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-22.478981018066406},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":0,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-32.93543243408203},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":0,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-33.91706848144531},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":0,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-35.248714447021484},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":1,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[3],\\\"score\\\":-31.13232421875},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":1,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[3],\\\"score\\\":-32.65959167480469},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":1,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[3],\\\"score\\\":-33.26198959350586},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":2,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-29.640785217285156},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":2,\\\"r\\\":\\\"P171\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-30.309494018554688},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":2,\\\"r\\\":\\\"P108\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-30.538372039794922},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":3,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-24.226791381835938},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":3,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-27.080961227416992},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":3,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-27.81475830078125},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":4,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.94740104675293},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":4,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.17443084716797},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":4,\\\"r\\\":\\\"P205\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.78557586669922},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":5,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.704017639160156},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":5,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.795249938964844},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":5,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.981210708618164},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":6,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.46320915222168},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":6,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.56661605834961},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":6,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0],\\\"score\\\":-30.599075317382812},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":7,\\\"r\\\":\\\"P178\\\",\\\"evidence\\\":[3],\\\"score\\\":-25.838550567626953},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":7,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[3],\\\"score\\\":-27.74850845336914},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":7,\\\"r\\\":\\\"P108\\\",\\\"evidence\\\":[3],\\\"score\\\":-27.968839645385742},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":9,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-28.341541290283203},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":9,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-29.980939865112305},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":9,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-30.697141647338867},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":10,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[3],\\\"score\\\":-33.146297454833984},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":10,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[3],\\\"score\\\":-34.18794250488281},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":10,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[3],\\\"score\\\":-34.51270294189453},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[3,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":11,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[3,4],\\\"score\\\":-31.39203453063965},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":11,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[3,4],\\\"score\\\":-31.729581832885742},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":11,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[3,4],\\\"score\\\":-32.61418533325195},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":12,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-29.45476531982422},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":12,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-30.00889778137207},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":12,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-30.259363174438477},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":13,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[3],\\\"score\\\":-31.884675979614258},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":13,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[3],\\\"score\\\":-32.70466613769531},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":13,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[3],\\\"score\\\":-33.865562438964844},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":14,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[3],\\\"score\\\":-33.43254089355469},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":14,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[3],\\\"score\\\":-33.87025451660156},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":14,\\\"r\\\":\\\"P155\\\",\\\"evidence\\\":[3],\\\"score\\\":-34.017799377441406},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":15,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[3],\\\"score\\\":-31.278533935546875},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":15,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[3],\\\"score\\\":-31.63454818725586},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":8,\\\"t_idx\\\":15,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[3],\\\"score\\\":-32.262474060058594},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":0,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-16.740894317626953},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":0,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.198902130126953},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":0,\\\"r\\\":\\\"P1198\\\",\\\"evidence\\\":[0],\\\"score\\\":-20.30547332763672},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":1,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-23.176057815551758},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":1,\\\"r\\\":\\\"P1198\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.580324172973633},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":1,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.261568069458008},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":2,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-11.03584098815918},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":2,\\\"r\\\":\\\"P1198\\\",\\\"evidence\\\":[0],\\\"score\\\":-14.953210830688477},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":2,\\\"r\\\":\\\"P361\\\",\\\"evidence\\\":[0],\\\"score\\\":-15.251543998718262},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":4,\\\"r\\\":\\\"P1198\\\",\\\"evidence\\\":[0],\\\"score\\\":-22.628644943237305},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":4,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0],\\\"score\\\":-24.766454696655273},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":4,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.523143768310547},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":5,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-6.106231689453125},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":5,\\\"r\\\":\\\"P36\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-13.122530937194824},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":5,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-15.79046630859375},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":6,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-3.346376419067383},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":6,\\\"r\\\":\\\"P36\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-12.742910385131836},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":6,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-14.350057601928711},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":7,\\\"r\\\":\\\"P463\\\",\\\"evidence\\\":[0,4,5],\\\"score\\\":-10.195099830627441},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":7,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,4,5],\\\"score\\\":-11.716753005981445},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":7,\\\"r\\\":\\\"P178\\\",\\\"evidence\\\":[0,4,5],\\\"score\\\":-13.113197326660156},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":8,\\\"r\\\":\\\"P1198\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-22.66289520263672},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":8,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-23.5752010345459},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":8,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,3],\\\"score\\\":-26.387645721435547},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":10,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[4],\\\"score\\\":-17.473388671875},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":10,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[4],\\\"score\\\":-19.011899948120117},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":10,\\\"r\\\":\\\"P571\\\",\\\"evidence\\\":[4],\\\"score\\\":-20.07172203063965},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":11,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[4],\\\"score\\\":-14.267850875854492},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":11,\\\"r\\\":\\\"P206\\\",\\\"evidence\\\":[4],\\\"score\\\":-15.288780212402344},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":11,\\\"r\\\":\\\"P194\\\",\\\"evidence\\\":[4],\\\"score\\\":-15.395681381225586},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":12,\\\"r\\\":\\\"P1198\\\",\\\"evidence\\\":[5],\\\"score\\\":-18.00496482849121},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":12,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[5],\\\"score\\\":-18.4006290435791},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":12,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[5],\\\"score\\\":-23.64129066467285},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":13,\\\"r\\\":\\\"P1198\\\",\\\"evidence\\\":[5],\\\"score\\\":-24.121339797973633},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":13,\\\"r\\\":\\\"P30\\\",\\\"evidence\\\":[5],\\\"score\\\":-24.741134643554688},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":13,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[5],\\\"score\\\":-26.68038558959961},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,6],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":14,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-24.22472381591797},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":14,\\\"r\\\":\\\"P1198\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-25.74798011779785},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":14,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-26.461822509765625},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,6],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":15,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-23.747568130493164},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":15,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-25.600502014160156},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":9,\\\"t_idx\\\":15,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[0,6],\\\"score\\\":-26.65237045288086},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":0,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-31.167652130126953},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":0,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-31.426300048828125},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":0,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-31.46797752380371},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":1,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-29.306015014648438},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":1,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-30.779232025146484},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":1,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-30.920793533325195},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":2,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.320419311523438},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":2,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.522531509399414},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":2,\\\"r\\\":\\\"P171\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.373987197875977},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":3,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-19.088932037353516},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":3,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-22.135427474975586},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":3,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-22.623340606689453},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":4,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.293861389160156},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":4,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.92089080810547},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":4,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.01601791381836},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":5,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.710886001586914},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":5,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-28.403051376342773},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":5,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-28.52047348022461},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":6,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-24.474403381347656},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":6,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.57686424255371},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":6,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-28.45546531677246},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":7,\\\"r\\\":\\\"P178\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-23.018978118896484},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":7,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-23.256885528564453},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":7,\\\"r\\\":\\\"P749\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-24.102449417114258},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[3],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":8,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[3],\\\"score\\\":-30.213462829589844},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":8,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[3],\\\"score\\\":-30.463586807250977},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":8,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[3],\\\"score\\\":-31.410205841064453},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":9,\\\"r\\\":\\\"P17\\\",\\\"evidence\\\":[4],\\\"score\\\":-19.896076202392578},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":9,\\\"r\\\":\\\"P495\\\",\\\"evidence\\\":[4],\\\"score\\\":-21.71392822265625},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":9,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[4],\\\"score\\\":-21.818397521972656},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":11,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":11,\\\"r\\\":\\\"P31\\\",\\\"evidence\\\":[4],\\\"score\\\":-15.096111297607422},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":11,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[4],\\\"score\\\":-16.205617904663086},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":11,\\\"r\\\":\\\"P155\\\",\\\"evidence\\\":[4],\\\"score\\\":-18.928890228271484},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":12,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-26.591228485107422},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":12,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-27.02835464477539},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":12,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-27.439289093017578},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[4,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":13,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[4,5],\\\"score\\\":-29.819143295288086},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":13,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[4,5],\\\"score\\\":-31.561037063598633},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":13,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[4,5],\\\"score\\\":-31.655025482177734},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":14,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":14,\\\"r\\\":\\\"P155\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.999881744384766},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":14,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.129783630371094},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":14,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-29.33099937438965},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":15,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":15,\\\"r\\\":\\\"P54\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.25487518310547},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":15,\\\"r\\\":\\\"P35\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.4958553314209},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":10,\\\"t_idx\\\":15,\\\"r\\\":\\\"P112\\\",\\\"evidence\\\":[0],\\\"score\\\":-27.633899688720703},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":0,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":0,\\\"r\\\":\\\"P156\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.474977493286133},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":0,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.649085998535156},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":0,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0],\\\"score\\\":-28.85941505432129},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":1,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":1,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-29.432790756225586},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":1,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-29.932920455932617},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":1,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-30.060226440429688},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":2,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":2,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-22.705324172973633},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":2,\\\"r\\\":\\\"P69\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-23.856292724609375},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":2,\\\"r\\\":\\\"P171\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-24.24275779724121},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":3,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":3,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-15.793116569519043},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":3,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-17.077255249023438},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":3,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-17.180728912353516},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":4,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":4,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.749204635620117},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":4,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[0],\\\"score\\\":-25.809558868408203},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":4,\\\"r\\\":\\\"P205\\\",\\\"evidence\\\":[0],\\\"score\\\":-26.757368087768555},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":5,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":5,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.319433212280273},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":5,\\\"r\\\":\\\"P937\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.554275512695312},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":5,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.555585861206055},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":6,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,1],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":6,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-23.077239990234375},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":6,\\\"r\\\":\\\"P1376\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-26.559213638305664},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":6,\\\"r\\\":\\\"P276\\\",\\\"evidence\\\":[0,1],\\\"score\\\":-27.337806701660156},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":7,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":7,\\\"r\\\":\\\"P178\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-16.67437744140625},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":7,\\\"r\\\":\\\"P137\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-18.163225173950195},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":7,\\\"r\\\":\\\"P279\\\",\\\"evidence\\\":[0,4],\\\"score\\\":-19.251306533813477},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":8,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[3,4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":8,\\\"r\\\":\\\"P569\\\",\\\"evidence\\\":[3,4],\\\"score\\\":-28.05459213256836},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":8,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[3,4],\\\"score\\\":-28.40361785888672},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":8,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[3,4],\\\"score\\\":-29.809694290161133},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":9,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":9,\\\"r\\\":\\\"P495\\\",\\\"evidence\\\":[4],\\\"score\\\":-16.538265228271484},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":9,\\\"r\\\":\\\"P150\\\",\\\"evidence\\\":[4],\\\"score\\\":-17.910491943359375},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":9,\\\"r\\\":\\\"P205\\\",\\\"evidence\\\":[4],\\\"score\\\":-18.498098373413086},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":10,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":10,\\\"r\\\":\\\"P577\\\",\\\"evidence\\\":[4],\\\"score\\\":-14.561819076538086},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":10,\\\"r\\\":\\\"P582\\\",\\\"evidence\\\":[4],\\\"score\\\":-14.653136253356934},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":10,\\\"r\\\":\\\"P580\\\",\\\"evidence\\\":[4],\\\"score\\\":-15.604393005371094},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":12,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[0,5],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":12,\\\"r\\\":\\\"P706\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-24.957534790039062},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":12,\\\"r\\\":\\\"P26\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-25.664045333862305},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":12,\\\"r\\\":\\\"P3373\\\",\\\"evidence\\\":[0,5],\\\"score\\\":-25.666749954223633},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":13,\\\"r\\\":\\\"Na\\\",\\\"evidence\\\":[4],\\\"score\\\":0.0},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\\":11,\\\"t_idx\\\":13,\\\"r\\\":\\\"P19\\\",\\\"evidence\\\":[4],\\\"score\\\":-30.535202026367188},{\\\"title\\\":\\\"IBM Research \\\\u2013 Brazil\\\",\\\"h_idx\\
```

---
