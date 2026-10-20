# Research conversation: [HANDOFF] 你是 Main Agent，这是 Loop #13。 ## 上一轮交接 (task_context) ### 1. 🔴 硬约束 / 红线 - 本项目只能用 westd-19828 的 cuda:0 和 cuda:1（gp — Part 5 of 5

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../research-conversation-handoff-main-agent-loop-13-task-context-1-westd-19828-cuda-0-cuda-1-gp-copy-2.md) · [Structured JSON](../../../sessions/89/896a3e3c2e3dec9faa3e.json)

## Round 141

### Assistant

_source line 1250 · 2026-05-18T12:54:16.236Z_

<details><summary>Logged reasoning block</summary>

```text
Director wants me to directly edit the paper files, not spawn a worker. But the files are on a remote server (westd-19828). I can't use Edit tool on remote files directly. I need to either:

1. Use SSH to read and edit the files
2. Spawn a worker with SSH access

But Director explicitly said "不要 spawn worker，直接在当前 session 完成编辑。"

Hmm, but I'm the coordinator - I'm not supposed to do SSH operations directly. The rule says "你不做 SSH / 代码 / 日志分析 / 文献调研——这些全部 spawn_worker 委派"


The Director's instruction overrides my default behavior since this is marked CRITICAL priority. But I don't actually have SSH tools available—only local tools like Bash, Read, Edit, and Write. Let me check if there's a local copy of the paper files in the project working directory at /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35904ebb-a287-4062-b9be-bb09dcd706fa",
  "isSidechain": false,
  "requestId": "req_011CbA4smRiraDVizH3sF1sT",
  "type": "assistant",
  "uuid": "d076a0e4-bafe-4906-b8d8-66660721ab6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016j4Z5QScuKTHhdneY9RvpT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 143471,
      "cache_read_input_tokens": 11841,
      "output_tokens": 709,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 143471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 709,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 143471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 143471
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 93643
      }
    }
  }
}
```

</details>

---


### Assistant

_source line 1251 · 2026-05-18T12:54:16.237Z_

先确认论文文件位置，然后直接编辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d076a0e4-bafe-4906-b8d8-66660721ab6c",
  "isSidechain": false,
  "requestId": "req_011CbA4smRiraDVizH3sF1sT",
  "type": "assistant",
  "uuid": "43e3941c-cbee-45c6-b598-9722bf524da0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016j4Z5QScuKTHhdneY9RvpT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 143471,
      "cache_read_input_tokens": 11841,
      "output_tokens": 709,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 143471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 709,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 143471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 143471
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 93643
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-18T12:54:17.172Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WLWR4oW4mJgDDLSoafMaUV`</summary>

```json
{
  "pattern": "**/docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43e3941c-cbee-45c6-b598-9722bf524da0",
  "isSidechain": false,
  "requestId": "req_011CbA4smRiraDVizH3sF1sT",
  "type": "assistant",
  "uuid": "e25bd214-4e02-4479-9298-fce74315fe55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016j4Z5QScuKTHhdneY9RvpT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 143471,
      "cache_read_input_tokens": 11841,
      "output_tokens": 709,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 143471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 709,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 143471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 143471
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 93643
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 1253 · 2026-05-18T12:54:17.477Z_

<details><summary>↩ Tool result · `toolu_01C917YYS4TzBJTVgbv7eDT9`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/single_method_errors.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/single_method_errors_ae8937.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/generalization_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64a5fa15-5948-4542-beeb-5df9270e8571",
  "isSidechain": false,
  "promptId": "e0dec198-abf3-497e-80c7-3f5c472bf9b3",
  "type": "user",
  "uuid": "89d5d065-a1d4-44d3-bae9-6e6855c8fa8f",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/background.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/experiments.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ethics.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/single_method_errors.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/single_method_errors_ae8937.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/generalization_draft.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
    ],
    "durationMs": 15,
    "numFiles": 23,
    "truncated": false
  },
  "sourceToolAssistantUUID": "64a5fa15-5948-4542-beeb-5df9270e8571",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

</details>

---


### Tool result

_source line 1254 · 2026-05-18T12:54:17.190Z_

<details><summary>↩ Tool result · `toolu_01WLWR4oW4mJgDDLSoafMaUV`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e25bd214-4e02-4479-9298-fce74315fe55",
  "isSidechain": false,
  "promptId": "e0dec198-abf3-497e-80c7-3f5c472bf9b3",
  "type": "user",
  "uuid": "fe4790f0-f3f3-43b6-9c44-cf156999e298",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ethics.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex",
      "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
    ],
    "durationMs": 12,
    "numFiles": 12,
    "truncated": false
  },
  "sourceToolAssistantUUID": "e25bd214-4e02-4479-9298-fce74315fe55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

</details>

---


### Tool call

_source line 1255 · 2026-05-18T12:54:17.458Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01C917YYS4TzBJTVgbv7eDT9`</summary>

```json
{
  "pattern": "**/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe4790f0-f3f3-43b6-9c44-cf156999e298",
  "isSidechain": false,
  "requestId": "req_011CbA4smRiraDVizH3sF1sT",
  "type": "assistant",
  "uuid": "64a5fa15-5948-4542-beeb-5df9270e8571",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016j4Z5QScuKTHhdneY9RvpT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 143471,
      "cache_read_input_tokens": 11841,
      "output_tokens": 709,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 143471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 709,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 143471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 143471
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 93643
      }
    }
  }
}
```

</details>

---


### Runtime record

_source line 1256 · 2026-05-18T12:54:17.517Z_

```json
{
  "parentUuid": "89d5d065-a1d4-44d3-bae9-6e6855c8fa8f",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "163537cb-e995-4993-bbea-4afdf8a8999a",
  "timestamp": "2026-05-18T12:54:17.517Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

---


### Assistant

_source line 1257 · 2026-05-18T12:54:26.779Z_

<details><summary>Logged reasoning block</summary>

```text
There are local copies of the paper files at `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/`. I can edit these directly using Read and Edit tools.

But wait — the C002 constraint says the paper true source is at `docs/paper/`. There's also an `artifacts/_project/paper/` copy which should be ignored.

However, there might be sync issues between local and remote. The remote files at `/root/autodl-tmp/distrib_canary_collapse/docs/paper/` on westd-19828 might be different from the local copies. 

Previous edits were done via SSH workers on the remote server, so I need to check if the local experiments.tex matches the remote version. Let me read the local file first to see what state it's in, then I'll start editing experiments.tex along with conclusion.tex and discussion.tex to remove the "Preliminary" label from GPT-2m.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "163537cb-e995-4993-bbea-4afdf8a8999a",
  "isSidechain": false,
  "requestId": "req_011CbA4vBimqbg4rJPU8MAp2",
  "type": "assistant",
  "uuid": "4c5832ab-efce-4d0d-9568-42ad5d54c8e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwpnvKqSiuwTpAPdVxEycP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2245,
      "cache_read_input_tokens": 155312,
      "output_tokens": 437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 437,
          "cache_read_input_tokens": 155312,
          "cache_creation_input_tokens": 2245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2245
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

_source line 1258 · 2026-05-18T12:54:26.782Z_

本地有论文文件。读取 experiments.tex 开始编辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c5832ab-efce-4d0d-9568-42ad5d54c8e4",
  "isSidechain": false,
  "requestId": "req_011CbA4vBimqbg4rJPU8MAp2",
  "type": "assistant",
  "uuid": "d14864ad-3192-4adc-a977-751103436fa4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwpnvKqSiuwTpAPdVxEycP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2245,
      "cache_read_input_tokens": 155312,
      "output_tokens": 437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 437,
          "cache_read_input_tokens": 155312,
          "cache_creation_input_tokens": 2245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2245
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

_source line 1259 · 2026-05-18T12:54:26.788Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AoU4yUsxDTYJkVCrTA1UUa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d14864ad-3192-4adc-a977-751103436fa4",
  "isSidechain": false,
  "requestId": "req_011CbA4vBimqbg4rJPU8MAp2",
  "type": "assistant",
  "uuid": "6b6c4f3a-cda1-4f01-86a6-79d71dc5d613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QwpnvKqSiuwTpAPdVxEycP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2245,
      "cache_read_input_tokens": 155312,
      "output_tokens": 437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2245,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 437,
          "cache_read_input_tokens": 155312,
          "cache_creation_input_tokens": 2245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2245
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

_source line 1260_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] **CRITICAL: 论文 Table 7 有 8+ 处错误数据 — 立即修复**  上次 Worker 失败，论文未被修改。Reviewer 逐格核对发现至少 8 个数字错误 + 2 行缺失 + 多处正文引用错误。必须立即修复，否则是 desk reject 级数据完整性问题。  **编辑 `docs/paper/experiments.tex`（C002 真源）：…",
  "leafUuid": "6b6c4f3a-cda1-4f01-86a6-79d71dc5d613",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35"
}
```

---


### Runtime record

_source line 1261_

```json
{
  "type": "ai-title",
  "aiTitle": "Finalize paper Round 2 with C4 seed-43 analysis",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35"
}
```

---


### Tool result

_source line 1262 · 2026-05-18T12:54:27.047Z_

<details><summary>↩ Tool result · `toolu_01AoU4yUsxDTYJkVCrTA1UUa`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter decoder-only language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Cross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \S\ref{sec:method_sensitivity}, \S\ref{sec:regime}, and \S\ref{sec:discussion}.
10	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
11	
12	Our protocol follows the replace paradigm of \citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\alpha{<}1.0$.
13	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.
14	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.25, 0.50, 0.75, 1.00\}$.
15	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; $\alpha{=}0.00$, $\alpha{=}0.25$, and $\alpha{=}0.75$ each use three seeds $\{42, 43, 44\}$; $\alpha{=}0.50$ uses three seeds $\{42, 43, 44\}$.
16	
17	We track two \emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}) and three \emph{downstream metrics}.
18	Canary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).
19	Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).
20	Token entropy is the mean next-token prediction entropy $H(p_\theta | \text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.
21	We additionally evaluate effective rank and Self-BLEU as candidate canaries (\S\ref{sec:case_study}).
22	Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
23	Code and data will be released upon publication.
24	
25	All hypothesis tests apply Benjamini--Hochberg (BH) FDR correction at $q{=}0.05$.
26	Permutation Granger causality tests use 5{,}000 permutations on first-differenced series \cite{shojaie2022granger}.
27	Cross-correlation analysis uses a maximum lag of 5 generations.
28	Table~\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.
29	
30	\begin{table}[t]
31	\centering
32	\small
33	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
34	\label{tab:drift_summary}
35	\begin{tabular}{lccccc}
36	\toprule
37	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
38	\midrule
39	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
40	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
41	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
42	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}0.7$ \\
43	1.00 & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
44	\bottomrule
45	\end{tabular}
46	\end{table}
47	
48	
49	\subsection{Method Sensitivity Analysis}
50	\label{sec:method_sensitivity}
51	
52	We open with Claim~3 (method sensitivity) because it conditions the interpretation of all subsequent results.
53	If different statistical methods yield contradictory conclusions on the same data, any single-method analysis is unreliable by construction.
54	
55	\paragraph{Five-method ablation.}
56	We apply five lead-lag detection methods to the $\alpha{=}1.0$ condition (4~seeds, 16 canary$\to$downstream pairs).
57	The fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \textbf{16/16} (100\%), differenced cross-correlation \textbf{14/16} (87.5\%), threshold onset detection \textbf{9/16} (56.3\%), permutation Granger causality \textbf{6/16} (37.5\%), and Toda--Yamamoto Granger \textbf{4/16} (25.0\%).
58	Method choice alone swings significance from \textbf{100\% to 25\%}: 50--57\% of pairs classified as significant under one method flip to non-significant under another.
59	The spurious-signal rate (the fraction of pairs detected by the most liberal method but not confirmed by the most conservative) is \textbf{75\%} across all five methods and \textbf{62.5\%} when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate (\S\ref{sec:consensus_validation}).
60	Table~\ref{tab:method_comparison} reports significance rates restricted to 8 validated canary$\to$downstream pairs (excluding failed candidates); the 16-pair rates above include effective rank and Self-BLEU to capture the full method-sensitivity landscape.
61	
62	\paragraph{First-differencing diagnostic.}
63	A single preprocessing decision can eliminate an entire analysis channel.
64	For canary$\to$diversity pairs at $\alpha{=}1.0$, all pairs retain unanimous FDR significance after first-differencing (24/24$\to$24/24), confirming genuine temporal precedence rather than shared-trend confounding.
65	For canary$\to$perplexity, however, undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find \textbf{zero} significant pairs ($F{\approx}0$, $p{=}0.99$; Figure~\ref{fig:differencing_dmax}a).
66	The apparent canary$\to$perplexity relationship is entirely an artifact of co-trending.
67	Notably, at $\alpha{=}0.75$, differenced cross-correlation finds 8/8 pairs significant in \emph{both} forward and reverse directions per seed, demonstrating that this method alone cannot distinguish genuine directional precedence from shared dynamics even after detrending.
68	
69	\paragraph{Augmentation order sensitivity.}
70	Toda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\max}$ (Figure~\ref{fig:differencing_dmax}b).
71	At $d_{\max}{=}0$ (most permissive), approximately 6\% of pairs are rejected; at adaptive $d_{\max}$ determined by ADF unit-root tests, 75\%; at $d_{\max}{=}1$ (most conservative), \textbf{94\%}.
72	This single hyperparameter swings conclusions from near-universal significance to near-universal non-significance.
73	
74	\begin{figure}[t]
75	\centering
76	\includegraphics[width=\linewidth]{figures/differencing_dmax.pdf}
77	\caption{First-differencing diagnostic and augmentation order sensitivity (Pythia-410M, $\alpha{=}1.0$, 4~seeds). \textbf{(a)}~First-differencing eliminates the canary$\to$perplexity channel: undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find zero significant pairs ($F{\approx}0$, $p{=}0.99$), exposing these associations as shared-trend artifacts. Canary$\to$diversity pairs retain significance after differencing (24/24$\to$24/24). \textbf{(b)}~Toda--Yamamoto Granger significance rates vary dramatically with augmentation order $d_{\max}$: from $\sim$6\% rejection at $d_{\max}{=}0$ to 94\% at $d_{\max}{=}1$, demonstrating that this single hyperparameter can reverse conclusions about temporal precedence.}
78	\label{fig:differencing_dmax}
79	\end{figure}
80	
81	\paragraph{Inter-method agreement.}
82	Cohen's $\kappa$, averaged over all method pairs, is \textbf{0.185} (near chance; poor agreement); this value is consistent across contamination levels ($\alpha{=}0.0$ through $\alpha{=}1.0$), indicating that method disagreement is a structural property of the analysis rather than a regime-specific artifact.
83	Cross-architecture validation on GPT-2-medium (12 canary$\to$downstream pairs) yields Fleiss' $\kappa{=}0.091$, also in the ``slight agreement'' range, confirming that low inter-method agreement is not architecture-specific.
84	Restricting to three informative methods (excluding naive cross-correlation and Toda--Yamamoto, which anchor the permissive and conservative extremes respectively) raises $\kappa$ to 0.667 (substantial agreement), indicating that the low full-panel $\kappa$ is driven by the deliberate inclusion of methods spanning the entire permissive-to-conservative spectrum rather than by fundamental incoherence among methods.
85	Table~\ref{tab:method_comparison} extends the analysis across contamination levels.
86	At $\alpha{=}0.0$ (no synthetic data, serving as null control), naive cross-correlation finds \textbf{100\%} of pairs significant, a textbook spurious-regression outcome in trending time series.
87	Permutation Granger correctly finds 0\% across all three null-control seeds; Toda--Yamamoto finds 0--12.5\% (1/24 total, attributable to a degenerate $\text{df}_{\text{resid}}{=}1$ case; \S\ref{sec:consensus_validation}).
88	At $\alpha{=}0.50$, naive and differenced cross-correlation both find 100\% significance while threshold onset and all causal methods find 0\% (Figure~\ref{fig:consensus_heatmap}), illustrating that even among non-causal methods, sensitivity diverges sharply at this boundary.
89	
90	\paragraph{Method$\times$regime interaction.}
91	Table~\ref{tab:method_comparison} reveals that the correlation-versus-causal divergence is not uniform across contamination levels.
92	At $\alpha{=}0.25$, differenced cross-correlation drops to 25\% and threshold onset to 0\%, while naive cross-correlation remains at 100\%, demonstrating that even partial detrending removes marginal associations at low contamination.
93	In the lowest-contamination regime ($\alpha{\leq}0.25$, three seeds), the false confirmation rate for the most liberal method approaches 100\%, while all Granger-type tests correctly find 0\%, a regime where single-method analysis is maximally dangerous.
94	The graded response across methods, combined with the block structure visible in Figure~\ref{fig:consensus_heatmap}, motivates the regime-dependent analysis in \S\ref{sec:regime}.
95	
96	\begin{figure}[t]
97	\centering
98	\includegraphics[width=\linewidth]{figures/consensus_heatmap.pdf}
99	\caption{Method$\times$regime consensus heatmap (Pythia-410M). Each cell shows the consensus tier ($K$-of-$M$ agreement) for a given lead-lag method (rows) and contamination level $\alpha$ (columns). A clear block structure emerges: correlation-based methods (naive, differenced, threshold) find significance across all $\alpha$ levels, while Granger-type methods find significance only at $\alpha{\geq}0.75$. The $\alpha{=}0.50$ column is maximally dangerous (high correlation coexists with zero causal precedence), illustrating Pitfall~3 (regime dependence). Color scale: dark = significant (Tier~3), light = non-significant (Tier~1).}
100	\label{fig:consensus_heatmap}
101	\end{figure}
102	
103	\begin{table}[t]
104	\centering
105	\small
106	\caption{FDR significance rates (\%) for five lead-lag methods across contamination levels (Pythia-410M). Method choice swings significance from 100\% (naive cross-correlation) to 0\% (permutation Granger) at $\alpha{\leq}0.25$, with seed-dependent onset at $\alpha{=}0.50$, demonstrating that single-method conclusions are unreliable. Each cell reports the fraction of 8 canary$\to$downstream pairs (token entropy and ECE $\times$ 4 downstream metrics) reaching BH-corrected significance ($q{=}0.05$), excluding failed candidates (\S\ref{sec:case_study}). Seed coverage: $\alpha{=}1.0$: 4 seeds (32 pairs); $\alpha{=}0.00$, $\alpha{=}0.75$: 3 seeds (24 pairs); $\alpha{=}0.25$ Toda--Yamamoto: 3 seeds (24 pairs), other methods single seed; $\alpha{=}0.50$: 3~seeds for permutation Granger (range shown), single seed for other methods. $^\dagger$Seed-dependent onset: s42${=}$0/8, s43${=}$6/8, s44${=}$3/8 (median 3/8).}
107	\label{tab:method_comparison}
108	\begin{tabular}{lcccccc}
109	\toprule
110	Method & $\alpha{=}0.0$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.0$ & FPR$_\text{null}$ \\
111	\midrule
112	Naive XCorr     & 100   & 100  & 100  & 100   & 100   & 100  \\
113	Diff.\ XCorr   & 37.5  & 25   & 100  & 100   & 100   & 37.5 \\
114	Threshold       & 20.8  & 0    & 0    & 33.3  & 100   & 20.8 \\
115	Perm.\ Granger  & 0     & 0    & 0--75$^\dagger$  & 79.2  & 75    & 0    \\
116	Toda--Yamamoto  & 0     & 12.5 & 0    & 12.5  & 59.4  & 0    \\
117	\bottomrule
118	\end{tabular}
119	\end{table}
120	
121	
122	\subsection{Regime-Dependent Detectability}
123	\label{sec:regime}
124	
125	Beyond method choice, the contamination level~$\alpha$ determines whether a temporal lead exists to detect.
126	We present regime effects at two levels: raw metric drift (method-independent) and Granger-precedence detectability.
127	
128	\paragraph{Raw drift.}
129	Table~\ref{tab:drift_summary} shows that diversity collapse occurs at \emph{all} contamination levels, not only under full synthetic replacement.
130	Distinct-1 declines by 13.8\% even at $\alpha{=}0.0$ (attributable to fine-tuning on repeated real-data subsets), and more steeply at intermediate contamination: $-40.3{\pm}0.3\%$ ($\alpha{=}0.25$), $-37.1{\pm}0.4\%$ ($\alpha{=}0.50$), $-32.3{\pm}0.5\%$ ($\alpha{=}0.75$), and $-27.8{\pm}1.6\%$ ($\alpha{=}1.0$).
131	The non-monotonic pattern (diversity declining \emph{more} at moderate~$\alpha$ than at extreme~$\alpha$) is confirmed by 3-seed replication at $\alpha{=}0.25$ (std${=}0.3\%$), indicating that this relationship between contamination level and collapse severity is robust rather than a seed-specific artifact.
132	
133	\begin{figure}[t]
134	\centering
135	\includegraphics[width=\linewidth]{figures/regime_map.pdf}
136	\caption{Detectability regime map across contamination levels (Pythia-410M). Permutation Granger FDR significance rate (solid line) and consensus tier (shaded regions) as a function of $\alpha$. The onset boundary lies at $\alpha{\approx}0.25$--$0.50$: at $\alpha{\leq}0.25$, all seeds agree on null (0/24); at $\alpha{=}0.50$, detectability is seed-dependent (0/8--6/8, 3~seeds, median 3/8); at $\alpha{=}0.75$, directional asymmetry emerges robustly (19/24 forward, 0/24 reverse, 3~seeds) but method consensus remains transitional (Tier~2--3); at $\alpha{=}1.0$, full Confirmatory consensus is achieved (24/24 forward, Tier~3, 4~seeds). Multi-seed replication: $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3~seeds; $\alpha{=}1.0$: 4~seeds.}
137	\label{fig:regime_map}
138	\end{figure}
139	
140	\paragraph{Granger-precedence detectability.}
141	Despite ubiquitous drift, causal detectability is sharply regime-dependent (Figure~\ref{fig:regime_map}).
142	Permutation Granger tests (first-differenced, BH-corrected) find 0/24 pairs FDR-significant at $\alpha{=}0.00$ (3~seeds), 0/24 at $\alpha{=}0.25$ (3~seeds), 0/8--6/8 at $\alpha{=}0.50$ (seed-dependent; 3~seeds, median 3/8), and \textbf{6/8} at $\alpha{=}1.0$.
143	At $\alpha{=}0.75$ (3~seeds), permutation Granger finds 19/24 forward-direction pairs FDR-significant with 0/24 reverse, confirming directional asymmetry; however, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds), placing this regime in a transitional detection state.
144	Under Bonferroni correction, approximately 3/8 pairs per seed survive, consistent with the transitional nature of the $\alpha{=}0.75$ boundary where marginal signals are sensitive to correction stringency.
145	Within-$\alpha$ multi-seed analysis at $\alpha{=}1.0$ yields \textbf{24/24} canary$\to$diversity pairs FDR-significant across all four seeds, with 0/24 in the reverse direction, confirming temporal asymmetry.
146	The resulting dose-response pattern is monotonic: causal detectability is absent below $\alpha{=}0.25$, seed-dependent at $\alpha{=}0.50$, and robust above $\alpha{=}0.75$ (Figure~\ref{fig:regime_map}).
147	The onset boundary lies at $\alpha{\approx}0.25$--$0.50$, consistent with theoretical expectations about signal-to-noise limits in short time series~\cite{boettiger2012limits}.
148	At the extremes, the transition is unambiguous: 0/24 FDR-significant pairs at $\alpha{\leq}0.25$ (3~seeds) versus 24/24 at $\alpha{=}1.0$ (4~seeds, Tier~3 consensus).
149	Between these extremes, individual-seed stochasticity determines whether the consensus threshold is crossed; the data map a boundary region rather than a sharp phase transition.
150	Sensitivity analysis confirms that treatment/null separation is robust to FDR threshold choice ($q{=}0.01$: 0/24 null, 0/24 treatment at $\alpha{=}0.75$; $q{=}0.10$: 0/24 null, 24/24 treatment; Appendix~\ref{app:robustness}).
151	Cross-architecture validation on GPT-2-medium confirms this boundary: at $\alpha{=}0.25$, at most 1/8 pairs reach Confirmatory consensus ($K{\geq}4/5$), consistent with the null regime, despite substantially stronger canary drift (entropy $-32.8\%$ vs.\ Pythia $-4.7{\pm}0.5\%$), while at $\alpha{=}1.0$ all 6 canary$\to$diversity pairs reach $K{\geq}4/5$ (\S\ref{sec:discussion}).
152	Table~\ref{tab:cross_arch_regime} summarizes the regime map across both architectures.
153	At $\alpha{=}0.25$, GPT-2-medium yields 1/8 pairs at Tier~3 ($K{\geq}4/5$) and 7/8 at Tier~2 ($K{\geq}3/5$), consistent with Pythia's 0/8 Tier~3, 0/8 Tier~2 result at the same contamination level, placing both architectures in the null/low-detectability regime.
154	
155	\begin{table}[t]
156	\centering
157	\small
158	\caption{Cross-architecture regime map: lead-lag consensus tier and metric drift at $\alpha{=}0.25$ and $\alpha{=}1.0$. Tier~3: $K{\geq}4/5$ methods; Tier~2: $K{\geq}3/5$. Drift is generation~0$\to$10. GPT-2-medium $\alpha{=}0.25$: single seed (seed=42); Pythia $\alpha{=}0.25$: 3-seed mean${\pm}$std. The onset boundary ($\alpha{\approx}0.25$--$0.50$) is consistent across two transformer decoder-only model families of similar scale.}
159	\label{tab:cross_arch_regime}
160	\begin{tabular}{llcccccc}
161	\toprule
162	$\alpha$ & Model & Entropy & ECE & Distinct-1 & Distinct-2 & Perm.\ Granger & Tier~3 \\
163	\midrule
164	0.25 & Pythia-410M  & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & 0/8 & 0/8 \\
165	0.25 & GPT-2-medium & $-32.8$ & $+422$ & $-23.5$ & $-31.6$ & 0/8 & 1/8 \\
166	\midrule
167	1.00 & Pythia-410M  & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & 6/8 & 6/6 \\
168	1.00 & GPT-2-medium & \multicolumn{6}{c}{(reported in \S\ref{sec:discussion}; all 6 canary$\to$diversity Tier~3)} \\
169	\bottomrule
170	\end{tabular}
171	\end{table}
172	
173	\paragraph{Onset boundary at $\alpha{=}0.50$.}
174	The $\alpha{=}0.50$ regime provides particularly informative evidence.
175	Naive and differenced cross-correlation find 100\% significance while threshold onset finds 0\% (Table~\ref{tab:method_comparison}), and causal methods confirm emerging detectability in a majority of seeds: two of three seeds show directional asymmetry under permutation Granger (6/8 and 3/8 forward, 0/8 reverse), while one seed shows synchronous collapse (0/8).
176	The majority-signal outcome places $\alpha{=}0.50$ in a transitional regime where causal detectability is emerging but not yet robust, bridging the null regime ($\alpha{\leq}0.25$) and the consistently detectable regime ($\alpha{\geq}0.75$).
177	This seed dependence exemplifies our central argument: even within a single regime and method, stochastic variation in training determines whether the consensus threshold is crossed.
178	At this boundary, canary sensitivity is metric-dependent: token entropy fails to reach FDR significance in any seed ($p_{\text{fdr}}{\geq}0.086$), while ECE achieves significance in the two signal-positive seeds (s43, s44), identifying ECE as the more sensitive canary at the onset boundary.
179	Figure~\ref{fig:consensus_heatmap} visualizes this interaction across all method$\times\alpha$ combinations, revealing a clear block structure that separates correlation-based methods from causal methods as a function of regime.
180	
181	
182	\subsection{Case Study: Canary Prediction of Diversity Collapse}
183	\label{sec:case_study}
184	
185	Having established method sensitivity (Claim~3) and regime dependence (Claim~2), we present the conditions under which canary prediction succeeds (Claim~1).
186	We scope this claim precisely: canary metrics predict \emph{diversity collapse} (declining distinct-$n$), not model collapse broadly.
187	
188	\paragraph{Full synthetic replacement ($\alpha{=}1.0$, 4 seeds).}
189	Token entropy exhibits robust Granger-precedence over diversity collapse metrics, confirmed by 4 independent statistical methods (permutation Granger power${=}1.0$), 4 seeds, and cross-architecture replication on GPT-2-medium (Tier~3 consensus; \S\ref{sec:discussion}).
190	Cross-correlation peaks at lag$={+}1$ with $|r|{>}0.99$ (cross-seed standard deviation: 0.0), establishing a consistent one-generation lead.
191	Figure~\ref{fig:metric_trajectory} illustrates the one-generation offset between token entropy decline and distinct-1 decline, visible across all four seeds.
192	Permutation Granger tests (first-differenced) confirm all canary$\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\ref{app:distinct3}).
193	Reverse-direction tests (downstream$\to$canary) find \textbf{0/24} FDR-significant (all $p{>}0.49$), establishing complete directional asymmetry.
194	
195	\begin{figure}[t]
196	\centering
197	\includegraphics[width=\linewidth]{figures/metric_trajectory.pdf}
198	\caption{Metric trajectories across 10 generations at $\alpha{=}1.0$ (Pythia-410M, 4~seeds shown as individual traces). Token entropy (top, blue) drops sharply at generation~1, while distinct-1 (bottom, red) begins declining at generations~2--3, establishing a visible one-generation canary lead. The consistent lag across all four seeds confirms that the temporal offset is robust rather than seed-specific. Shaded bands show the inter-seed range. This visual pattern corresponds to the statistical finding of 24/24 forward-direction and 0/24 reverse-direction FDR-significant pairs.}
199	\label{fig:metric_trajectory}
200	\end{figure}
201	
202	\paragraph{High contamination ($\alpha{=}0.75$, 3 seeds).}
203	Directional asymmetry is robustly confirmed across three independent seeds (permutation Granger: 19/24 forward pairs FDR-significant, 0/24 reverse).
204	However, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds 42, 43, 44), placing $\alpha{=}0.75$ squarely in the transitional detection regime.
205	Differenced cross-correlation finds 8/8 pairs significant in \emph{both} forward and reverse directions at each seed, confirming that this method alone cannot distinguish genuine directional precedence from shared dynamics, a seed-level demonstration of Pitfall~1 (\S\ref{sec:pitfalls}).
206	
207	\paragraph{ECE as a conditional secondary canary.}
208	ECE performs equivalently to token entropy across four of five methods (naive, differenced, threshold, permutation Granger).
209	Its classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootstrap power analysis yields estimated power of 0.05--0.20 depending on $d_{\max}$.
210	Resolving ECE's true canary status requires longer time series.
211	
212	\paragraph{Failed canary candidates.}
213	Not all metrics serve as canaries.
214	Effective rank and Self-BLEU show no detectable lead-lag relationship with any downstream metric under any method or contamination level, and are excluded from the consensus framework.
215	Effective rank behavior is model-dependent in an unexpected way: in Pythia-410M, effective rank decreases during collapse (representational contraction), whereas in GPT-2-medium at $\alpha{=}0.25$ it \emph{increases} from 2.37 to 8.48 (+258\%).
216	The GPT-2-medium starting effective rank is near rank-2, suggesting the model's initial representation is already highly concentrated; iterative training disperses it rather than concentrating it further.
217	This opposite directionality across architectures precludes effective rank as a universal canary and motivates architecture-specific analysis (\S\ref{sec:discussion}).
218	
219	\paragraph{Consensus filtering.}
220	Of 16 canary$\to$downstream pairs tested at $\alpha{=}1.0$ (4 candidate canaries $\times$ 4 downstream metrics), \textbf{6 survive} the full consensus pipeline ($K{\geq}4/5$ methods, $S{\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\ref{app:distinct3} bring the total to~6).
221	The 10 eliminated pairs comprise all canary$\to$perplexity relationships (identified as spurious by the first-differencing diagnostic) and all effective-rank and Self-BLEU pairs (failed canaries).
222	The consensus framework reduces the naive 100\% significance rate to the 37.5\% rate supported by the most conservative individual methods (Figure~\ref{fig:consensus_workflow}).
223	
224	
225	\subsection{Consensus Framework Validation}
226	\label{sec:consensus_validation}
227	
228	We validate the consensus framework's calibration using built-in experimental controls.
229	
230	\paragraph{False positive rate.}
231	At $\alpha{=}0.0$ (three seeds, 24 total pairs), no synthetic data is injected; any detected lead-lag association is a false positive.
232	Individual-method FPR ranges from \textbf{100\%} (naive cross-correlation) through 37.5\% (differenced) and 20.8\% (threshold) down to \textbf{0\%} (permutation Granger: 0/24 across all three seeds).
233	The consensus framework at $K{\geq}4/5$ achieves \textbf{FPR${=}$0\%} (0/24 pairs, three independent seeds), matching the best individual methods while providing robustness against miscalibration of any single method (Table~\ref{tab:fpr_fnr}).
234	
235	\paragraph{False negative rate.}
236	At $\alpha{=}1.0$, we define 6 effect-size reference pairs (token entropy and ECE $\to$ distinct-1/2/3) using criteria independent of the consensus methods: drift ratio ${\geq}3\times$ the $\alpha{=}0.0$ baseline (entropy $11.93\times$, ECE $73.12\times$) and canary onset strictly preceding downstream onset by ${\geq}1$ generation (\S\ref{sec:calibration}).
237	FNR is calibrated on a 4-method panel (excluding differenced cross-correlation to avoid circularity): at $K{\geq}3/4$, $S{\geq}3/4$, all~6 are recovered (\textbf{FNR${=}$0\%}).
238	Toda--Yamamoto alone yields FNR${=}$33.3\% (2/6), missing ECE$\to$distinct-2 and ECE$\to$distinct-3 due to Type~II errors at $T{=}10$.
239	Both FPR and FNR are validated on the joint method${\times}$seed dimension (FPR: 3~seeds at $\alpha{=}0.0$; FNR: 4~seeds at $\alpha{=}1.0$), with cross-seed FPR variance negligible (all three seeds yield 0/8 robust pairs at $K{\geq}4/5$).
240	Table~\ref{tab:fpr_fnr} reports the calibration results.
241	Table~\ref{tab:single-method-errors} complements this analysis by showing the practical consequences of relying on any single method: naive cross-correlation produces false positives at every $\alpha$ including the null control, Toda--Yamamoto misses true signals at $\alpha{=}0.75$, while the consensus at $K{\geq}3$ yields the correct verdict across all five contamination levels.
242	
243	\begin{table}[t]
244	\centering
245	\caption{Single-method inference errors across contamination levels.
246	Each cell shows the verdict (significant or not) based on multi-seed majority ($\geq$2/3 seeds with $\geq$4/8 pairs significant).
247	\checkmark\ = correct, \textcolor{red}{FP} = false positive, \textcolor{blue}{FN} = false negative, $\circ$ = ambiguous ground truth (either verdict plausible).
248	Naive XCorr produces false positives at \emph{every} $\alpha$ including the null control, while TY Granger misses true signals at $\alpha{=}0.75$.
249	Only the multi-method consensus ($K{\geq}3$) yields the correct verdict at all five contamination levels.}
250	\label{tab:single-method-errors}
251	\resizebox{\columnwidth}{!}{%
252	\begin{tabular}{lccccc}
253	\toprule
254	 & \multicolumn{2}{c}{\textit{No signal}} & \textit{Ambiguous} & \multicolumn{2}{c}{\textit{Causal signal}} \\
255	\cmidrule(lr){2-3} \cmidrule(lr){4-4} \cmidrule(lr){5-6}
256	Method & $\alpha{=}0.00$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.00$ \\
257	\midrule
258	Naive XCorr
259	  & \textcolor{red}{FP}{\scriptsize\ 8,7,8}
260	  & \textcolor{red}{FP}{\scriptsize\ 8,8}
261	  & $\circ${\scriptsize\ 8,8,8}
262	  & \checkmark{\scriptsize\ 8,8,8}
263	  & \checkmark{\scriptsize\ 8,8,8} \\
264	Diff XCorr (FDR)
265	  & \checkmark{\scriptsize\ 4,3,3}
266	  & \checkmark{\scriptsize\ 3,1}
267	  & $\circ${\scriptsize\ 8,6,6}
268	  & \checkmark{\scriptsize\ 8,8,8}
269	  & \checkmark{\scriptsize\ 8,8,8} \\
270	Threshold Onset
271	  & \checkmark{\scriptsize\ 3,1,1}
272	  & \checkmark{\scriptsize\ 0,0}
273	  & $\circ${\scriptsize\ 0,0,0}
274	  & \checkmark{\scriptsize\ 4,0,4}
275	  & \checkmark{\scriptsize\ 8,8,8} \\
276	Perm Granger (FDR)
277	  & \checkmark{\scriptsize\ 0,0,0}
278	  & \checkmark{\scriptsize\ 0,0}
279	  & $\circ${\scriptsize\ 0,6,3}
280	  & \checkmark{\scriptsize\ 8,5,6}
281	  & \checkmark{\scriptsize\ 6,6,6} \\
282	TY Granger
283	  & \checkmark{\scriptsize\ 1,1,0}
284	  & \checkmark{\scriptsize\ 0,2}
285	  & $\circ${\scriptsize\ 0,0,0}
286	  & \textcolor{blue}{FN}{\scriptsize\ 1,1,1}
287	  & \checkmark{\scriptsize\ 6,6,4} \\
288	\midrule
289	\textbf{Consensus ($K{\geq}3$)}
290	  & \checkmark
291	  & \checkmark
292	  & $\circ$
293	  & \checkmark
294	  & \checkmark \\
295	\bottomrule
296	\multicolumn{6}{l}{\footnotesize Subscript numbers: per-seed significant pair counts out of 8.} \\
297	\multicolumn{6}{l}{\footnotesize Seeds: $\alpha{=}0.00/0.50/0.75$: 42, 43, 44; $\alpha{=}0.25$: 43, 44; $\alpha{=}1.00$: 42, 43, 45.} \\
298	\end{tabular}%
299	}
300	\end{table}
301	
302	\paragraph{Bootstrap power analysis.}
303	To quantify detection power beyond binary FNR, we perform bootstrap power analysis ($B{=}1{,}000$ resamples from 4-seed data at $\alpha{=}1.0$).
304	Permutation Granger achieves power${=}1.0$ on genuine pairs (canary$\to$diversity) and power${=}0.0$ on spurious pairs (canary$\to$perplexity), providing clean separation.
305	Toda--Yamamoto achieves power${=}0.05$--$0.20$ on genuine pairs (depending on $d_{\max}$), confirming its poor sensitivity at $T{=}10$.
306	We note that bootstrap power${=}1.0$ reflects the effect size in our 4-seed data and should not be interpreted as a universal power guarantee; furthermore, the two methods use different data-generating processes for calibration (permutation Granger resamples observed $\alpha{=}1.0$ trajectories, while Toda--Yamamoto power was estimated under a generic VAR(2) simulation with $\beta{=}0.3$).
307	
308	\begin{table}[t]
309	\centering
310	\small
311	\caption{False positive and false negative rates for individual methods and the consensus framework (Pythia-410M). The consensus threshold $K{\geq}4/5$ achieves FPR${=}$0\% and FNR${=}$0\%, matching the best individual method (permutation Granger) while providing robustness against miscalibration. FPR: $\alpha{=}0.0$ null control (three seeds, $M{=}5$ methods); values are 3-seed means with ranges in parentheses where cross-seed variance is non-negligible. FNR: $\alpha{=}1.0$ against 6 effect-size reference pairs (4-method panel excluding differenced cross-correlation, 4~seeds).}
312	\label{tab:fpr_fnr}
313	\begin{tabular}{lcc}
314	\toprule
315	Criterion & FPR ($\alpha{=}0.0$) & FNR ($\alpha{=}1.0$) \\
316	\midrule
317	Naive XCorr              & 100\%              & 0\%  \\
318	Differenced XCorr        & 37.5\%             & 0\%  \\
319	Threshold Onset          & 20.8\% (12.5--37.5) & 0\%  \\
320	Permutation Granger      & 0\%                & 0\%  \\
321	Toda--Yamamoto           & 4.2\% (0--12.5)    & 33.3\% \\
322	\midrule
323	Consensus ($K{\geq}4/5$)              & 0\%    & 0\%  \\
324	Consensus ($K{\geq}4/5$, $S{\geq}3/4$) & 0\%    & 0\%  \\
325	\bottomrule
326	\end{tabular}
327	\end{table}
328	
329	
330	\subsection{Cross-Architecture, Cross-Scale, and Cross-Domain Generalization}
331	\label{sec:generalization}
332	
333	The methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).
334	To test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).
335	All conditions use $\alpha{=}1.0$ and a single seed.
336	
337	\begin{table}[t]
338	\centering
339	\small
340	\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\alpha{=}1.0$, single seed per condition). Each cell reports the fraction of canary$\to$downstream pairs reaching BH-corrected FDR significance ($q{=}0.05$): 8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded). \textbf{[TBD]}: experiments in progress.}
341	\label{tab:generalization}
342	\begin{tabular}{llccccccc}
343	\toprule
344	Variation & Model / Dataset & \rotatebox{70}{Naive} & \rotatebox{70}{Diff.\ XCorr} & \rotatebox{70}{Threshold} & \rotatebox{70}{PermG (fwd)} & \rotatebox{70}{PermG (rev)} & \rotatebox{70}{TY} & \rotatebox{70}{$K{\geq}4/5$} \\
345	\midrule
346	Baseline      & Pythia-410M / Wiki    & 7/8 & 6/8 & 6/8 & 6/8 & 0/8 & 6/8 & 6/8 \\
347	Architecture  & GPT-2-medium / Wiki   & 6/6 & 6/6 & 6/6 & 6/6 & 0/6 & 0/6 & 6/6 \\
348	Architecture  & OPT-1.3B / Wiki       & 6/8 & 6/8 & 8/8 & 6/8 & 0/8 & 2/8 & 6/8 \\
349	Scale ($3.4\times$) & Pythia-1.4B / Wiki & \multicolumn{7}{c}{\textbf{[TBD]}} \\
350	Domain        & Pythia-1B / C4        & \multicolumn{7}{c}{\textbf{[TBD]}} \\
351	\bottomrule
352	\end{tabular}
353	\end{table}
354	
355	\paragraph{Architecture generalization.}
356	Table~\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.
357	All models reach Tier~3 consensus ($K{\geq}4/5$) with 6/8 (or 6/6) canary$\to$diversity pairs confirmed.
358	Permutation Granger directionality is perfect across architectures: all forward-direction pairs are FDR-significant while 0 reverse-direction pairs reach significance in any architecture.
359	
360	Method-level variation across architectures is informative.
361	Threshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\to$1 discontinuity that cleanly exceeds the onset threshold.
362	Toda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\S\ref{sec:consensus_validation}).
363	Despite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\geq}4/5$.
364	
365	% [PLACEHOLDER — activate when Pythia-1.4B and Pythia-1B/C4 results arrive]
366	% \paragraph{Scale and domain generalization.}
367	% Scaling from 410M to 1.4B parameters within the Pythia family (3.4$\times$)
368	% preserves the core pattern: permutation Granger identifies \textbf{XX}/8
369	% forward-direction pairs with 0/8 reverse, and consensus $K{\geq}4/5$
370	% yields \textbf{XX}/8 (Table~\ref{tab:generalization}).
371	% This confirms that the methodological pitfalls are not artifacts of
372	% small-model capacity limitations, since the same consensus threshold
373	% operates identically at 3.4$\times$ the parameter count.
374	%
375	% Replacing WikiText-103 with C4 tests whether the lead-lag pattern
376	% depends on the training data distribution. Pythia-1B on C4 yields
377	% \textbf{XX}/8 forward-direction permutation Granger pairs with
378	% \textbf{XX}/8 reverse, and consensus $K{\geq}4/5$ at \textbf{XX}/8.
379	% Together with the architecture results, this establishes five
380	% independent validation lines (three architectures, one scale, one
381	% domain) converging on the same conclusion: token entropy
382	% Granger-precedes diversity collapse at $\alpha{=}1.0$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b6c4f3a-cda1-4f01-86a6-79d71dc5d613",
  "isSidechain": false,
  "promptId": "e0dec198-abf3-497e-80c7-3f5c472bf9b3",
  "type": "user",
  "uuid": "38f1eb95-54d3-4db5-9606-83586947d011",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\nPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\nCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\S\\ref{sec:method_sensitivity}, \\S\\ref{sec:regime}, and \\S\\ref{sec:discussion}.\nTraining data is drawn from WikiText-103 \\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\n\nOur protocol follows the replace paradigm of \\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\alpha{<}1.0$.\nEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\alpha$ fraction synthetic data and $(1{-}\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\nWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\alpha \\in \\{0.00, 0.25, 0.50, 0.75, 1.00\\}$.\nThe $\\alpha{=}1.0$ condition uses four random seeds $\\{42, 43, 44, 45\\}$; $\\alpha{=}0.00$, $\\alpha{=}0.25$, and $\\alpha{=}0.75$ each use three seeds $\\{42, 43, 44\\}$; $\\alpha{=}0.50$ uses three seeds $\\{42, 43, 44\\}$.\n\nWe track two \\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\cite{scheffer2009early}) and three \\emph{downstream metrics}.\nCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\nDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\nToken entropy is the mean next-token prediction entropy $H(p_\\theta | \\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\nWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\S\\ref{sec:case_study}).\nResults for distinct-3 are reported in Appendix~\\ref{app:distinct3}.\nCode and data will be released upon publication.\n\nAll hypothesis tests apply Benjamini--Hochberg (BH) FDR correction at $q{=}0.05$.\nPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\cite{shojaie2022granger}.\nCross-correlation analysis uses a maximum lag of 5 generations.\nTable~\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Metric drift (\\%, generation~0$\\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\\alpha$ levels, with the strongest decline at moderate contamination ($\\alpha{=}0.25$: distinct-1 $-40.3{\\pm}0.3\\%$) rather than full replacement ($\\alpha{=}1.0$: $-27.8{\\pm}1.6\\%$). $\\alpha{=}0.00$, $\\alpha{=}0.25$, $\\alpha{=}0.50$, $\\alpha{=}0.75$: 3-seed mean${\\pm}$std (seeds 42, 43, 44); $\\alpha{=}1.0$: 4-seed mean${\\pm}$std (seeds 42, 43, 44, 45).}\n\\label{tab:drift_summary}\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\\\\n\\midrule\n0.00 & $-4.6{\\pm}0.4$ & $+37.6{\\pm}14$ & $-14.1{\\pm}0.4$ & $-9.6{\\pm}0.4$ & $-20.6{\\pm}1.0$ \\\\\n0.25 & $-4.7{\\pm}0.5$ & $+81.8{\\pm}15.9$ & $-40.3{\\pm}0.3$ & $-56.4{\\pm}0.7$ & $-18.1{\\pm}0.8$ \\\\\n0.50 & $-18.0{\\pm}0.5$ & $+822.6{\\pm}18.3$ & $-37.1{\\pm}0.4$ & $-50.4{\\pm}1.0$ & $+21.0{\\pm}0.1$ \\\\\n0.75 & $-27.6{\\pm}0.2$ & $+1791{\\pm}18$ & $-32.3{\\pm}0.5$ & $-41.0{\\pm}1.0$ & $+182.6{\\pm}0.7$ \\\\\n1.00 & $-60.8{\\pm}1.2$ & $+3780{\\pm}30$ & $-27.8{\\pm}1.6$ & $-34.0{\\pm}3.3$ & $+3674{\\pm}45$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Method Sensitivity Analysis}\n\\label{sec:method_sensitivity}\n\nWe open with Claim~3 (method sensitivity) because it conditions the interpretation of all subsequent results.\nIf different statistical methods yield contradictory conclusions on the same data, any single-method analysis is unreliable by construction.\n\n\\paragraph{Five-method ablation.}\nWe apply five lead-lag detection methods to the $\\alpha{=}1.0$ condition (4~seeds, 16 canary$\\to$downstream pairs).\nThe fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \\textbf{16/16} (100\\%), differenced cross-correlation \\textbf{14/16} (87.5\\%), threshold onset detection \\textbf{9/16} (56.3\\%), permutation Granger causality \\textbf{6/16} (37.5\\%), and Toda--Yamamoto Granger \\textbf{4/16} (25.0\\%).\nMethod choice alone swings significance from \\textbf{100\\% to 25\\%}: 50--57\\% of pairs classified as significant under one method flip to non-significant under another.\nThe spurious-signal rate (the fraction of pairs detected by the most liberal method but not confirmed by the most conservative) is \\textbf{75\\%} across all five methods and \\textbf{62.5\\%} when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate (\\S\\ref{sec:consensus_validation}).\nTable~\\ref{tab:method_comparison} reports significance rates restricted to 8 validated canary$\\to$downstream pairs (excluding failed candidates); the 16-pair rates above include effective rank and Self-BLEU to capture the full method-sensitivity landscape.\n\n\\paragraph{First-differencing diagnostic.}\nA single preprocessing decision can eliminate an entire analysis channel.\nFor canary$\\to$diversity pairs at $\\alpha{=}1.0$, all pairs retain unanimous FDR significance after first-differencing (24/24$\\to$24/24), confirming genuine temporal precedence rather than shared-trend confounding.\nFor canary$\\to$perplexity, however, undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find \\textbf{zero} significant pairs ($F{\\approx}0$, $p{=}0.99$; Figure~\\ref{fig:differencing_dmax}a).\nThe apparent canary$\\to$perplexity relationship is entirely an artifact of co-trending.\nNotably, at $\\alpha{=}0.75$, differenced cross-correlation finds 8/8 pairs significant in \\emph{both} forward and reverse directions per seed, demonstrating that this method alone cannot distinguish genuine directional precedence from shared dynamics even after detrending.\n\n\\paragraph{Augmentation order sensitivity.}\nToda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\\max}$ (Figure~\\ref{fig:differencing_dmax}b).\nAt $d_{\\max}{=}0$ (most permissive), approximately 6\\% of pairs are rejected; at adaptive $d_{\\max}$ determined by ADF unit-root tests, 75\\%; at $d_{\\max}{=}1$ (most conservative), \\textbf{94\\%}.\nThis single hyperparameter swings conclusions from near-universal significance to near-universal non-significance.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/differencing_dmax.pdf}\n\\caption{First-differencing diagnostic and augmentation order sensitivity (Pythia-410M, $\\alpha{=}1.0$, 4~seeds). \\textbf{(a)}~First-differencing eliminates the canary$\\to$perplexity channel: undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find zero significant pairs ($F{\\approx}0$, $p{=}0.99$), exposing these associations as shared-trend artifacts. Canary$\\to$diversity pairs retain significance after differencing (24/24$\\to$24/24). \\textbf{(b)}~Toda--Yamamoto Granger significance rates vary dramatically with augmentation order $d_{\\max}$: from $\\sim$6\\% rejection at $d_{\\max}{=}0$ to 94\\% at $d_{\\max}{=}1$, demonstrating that this single hyperparameter can reverse conclusions about temporal precedence.}\n\\label{fig:differencing_dmax}\n\\end{figure}\n\n\\paragraph{Inter-method agreement.}\nCohen's $\\kappa$, averaged over all method pairs, is \\textbf{0.185} (near chance; poor agreement); this value is consistent across contamination levels ($\\alpha{=}0.0$ through $\\alpha{=}1.0$), indicating that method disagreement is a structural property of the analysis rather than a regime-specific artifact.\nCross-architecture validation on GPT-2-medium (12 canary$\\to$downstream pairs) yields Fleiss' $\\kappa{=}0.091$, also in the ``slight agreement'' range, confirming that low inter-method agreement is not architecture-specific.\nRestricting to three informative methods (excluding naive cross-correlation and Toda--Yamamoto, which anchor the permissive and conservative extremes respectively) raises $\\kappa$ to 0.667 (substantial agreement), indicating that the low full-panel $\\kappa$ is driven by the deliberate inclusion of methods spanning the entire permissive-to-conservative spectrum rather than by fundamental incoherence among methods.\nTable~\\ref{tab:method_comparison} extends the analysis across contamination levels.\nAt $\\alpha{=}0.0$ (no synthetic data, serving as null control), naive cross-correlation finds \\textbf{100\\%} of pairs significant, a textbook spurious-regression outcome in trending time series.\nPermutation Granger correctly finds 0\\% across all three null-control seeds; Toda--Yamamoto finds 0--12.5\\% (1/24 total, attributable to a degenerate $\\text{df}_{\\text{resid}}{=}1$ case; \\S\\ref{sec:consensus_validation}).\nAt $\\alpha{=}0.50$, naive and differenced cross-correlation both find 100\\% significance while threshold onset and all causal methods find 0\\% (Figure~\\ref{fig:consensus_heatmap}), illustrating that even among non-causal methods, sensitivity diverges sharply at this boundary.\n\n\\paragraph{Method$\\times$regime interaction.}\nTable~\\ref{tab:method_comparison} reveals that the correlation-versus-causal divergence is not uniform across contamination levels.\nAt $\\alpha{=}0.25$, differenced cross-correlation drops to 25\\% and threshold onset to 0\\%, while naive cross-correlation remains at 100\\%, demonstrating that even partial detrending removes marginal associations at low contamination.\nIn the lowest-contamination regime ($\\alpha{\\leq}0.25$, three seeds), the false confirmation rate for the most liberal method approaches 100\\%, while all Granger-type tests correctly find 0\\%, a regime where single-method analysis is maximally dangerous.\nThe graded response across methods, combined with the block structure visible in Figure~\\ref{fig:consensus_heatmap}, motivates the regime-dependent analysis in \\S\\ref{sec:regime}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/consensus_heatmap.pdf}\n\\caption{Method$\\times$regime consensus heatmap (Pythia-410M). Each cell shows the consensus tier ($K$-of-$M$ agreement) for a given lead-lag method (rows) and contamination level $\\alpha$ (columns). A clear block structure emerges: correlation-based methods (naive, differenced, threshold) find significance across all $\\alpha$ levels, while Granger-type methods find significance only at $\\alpha{\\geq}0.75$. The $\\alpha{=}0.50$ column is maximally dangerous (high correlation coexists with zero causal precedence), illustrating Pitfall~3 (regime dependence). Color scale: dark = significant (Tier~3), light = non-significant (Tier~1).}\n\\label{fig:consensus_heatmap}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{FDR significance rates (\\%) for five lead-lag methods across contamination levels (Pythia-410M). Method choice swings significance from 100\\% (naive cross-correlation) to 0\\% (permutation Granger) at $\\alpha{\\leq}0.25$, with seed-dependent onset at $\\alpha{=}0.50$, demonstrating that single-method conclusions are unreliable. Each cell reports the fraction of 8 canary$\\to$downstream pairs (token entropy and ECE $\\times$ 4 downstream metrics) reaching BH-corrected significance ($q{=}0.05$), excluding failed candidates (\\S\\ref{sec:case_study}). Seed coverage: $\\alpha{=}1.0$: 4 seeds (32 pairs); $\\alpha{=}0.00$, $\\alpha{=}0.75$: 3 seeds (24 pairs); $\\alpha{=}0.25$ Toda--Yamamoto: 3 seeds (24 pairs), other methods single seed; $\\alpha{=}0.50$: 3~seeds for permutation Granger (range shown), single seed for other methods. $^\\dagger$Seed-dependent onset: s42${=}$0/8, s43${=}$6/8, s44${=}$3/8 (median 3/8).}\n\\label{tab:method_comparison}\n\\begin{tabular}{lcccccc}\n\\toprule\nMethod & $\\alpha{=}0.0$ & $\\alpha{=}0.25$ & $\\alpha{=}0.50$ & $\\alpha{=}0.75$ & $\\alpha{=}1.0$ & FPR$_\\text{null}$ \\\\\n\\midrule\nNaive XCorr     & 100   & 100  & 100  & 100   & 100   & 100  \\\\\nDiff.\\ XCorr   & 37.5  & 25   & 100  & 100   & 100   & 37.5 \\\\\nThreshold       & 20.8  & 0    & 0    & 33.3  & 100   & 20.8 \\\\\nPerm.\\ Granger  & 0     & 0    & 0--75$^\\dagger$  & 79.2  & 75    & 0    \\\\\nToda--Yamamoto  & 0     & 12.5 & 0    & 12.5  & 59.4  & 0    \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Regime-Dependent Detectability}\n\\label{sec:regime}\n\nBeyond method choice, the contamination level~$\\alpha$ determines whether a temporal lead exists to detect.\nWe present regime effects at two levels: raw metric drift (method-independent) and Granger-precedence detectability.\n\n\\paragraph{Raw drift.}\nTable~\\ref{tab:drift_summary} shows that diversity collapse occurs at \\emph{all} contamination levels, not only under full synthetic replacement.\nDistinct-1 declines by 13.8\\% even at $\\alpha{=}0.0$ (attributable to fine-tuning on repeated real-data subsets), and more steeply at intermediate contamination: $-40.3{\\pm}0.3\\%$ ($\\alpha{=}0.25$), $-37.1{\\pm}0.4\\%$ ($\\alpha{=}0.50$), $-32.3{\\pm}0.5\\%$ ($\\alpha{=}0.75$), and $-27.8{\\pm}1.6\\%$ ($\\alpha{=}1.0$).\nThe non-monotonic pattern (diversity declining \\emph{more} at moderate~$\\alpha$ than at extreme~$\\alpha$) is confirmed by 3-seed replication at $\\alpha{=}0.25$ (std${=}0.3\\%$), indicating that this relationship between contamination level and collapse severity is robust rather than a seed-specific artifact.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/regime_map.pdf}\n\\caption{Detectability regime map across contamination levels (Pythia-410M). Permutation Granger FDR significance rate (solid line) and consensus tier (shaded regions) as a function of $\\alpha$. The onset boundary lies at $\\alpha{\\approx}0.25$--$0.50$: at $\\alpha{\\leq}0.25$, all seeds agree on null (0/24); at $\\alpha{=}0.50$, detectability is seed-dependent (0/8--6/8, 3~seeds, median 3/8); at $\\alpha{=}0.75$, directional asymmetry emerges robustly (19/24 forward, 0/24 reverse, 3~seeds) but method consensus remains transitional (Tier~2--3); at $\\alpha{=}1.0$, full Confirmatory consensus is achieved (24/24 forward, Tier~3, 4~seeds). Multi-seed replication: $\\alpha{=}0.00$, $\\alpha{=}0.25$, $\\alpha{=}0.50$, $\\alpha{=}0.75$: 3~seeds; $\\alpha{=}1.0$: 4~seeds.}\n\\label{fig:regime_map}\n\\end{figure}\n\n\\paragraph{Granger-precedence detectability.}\nDespite ubiquitous drift, causal detectability is sharply regime-dependent (Figure~\\ref{fig:regime_map}).\nPermutation Granger tests (first-differenced, BH-corrected) find 0/24 pairs FDR-significant at $\\alpha{=}0.00$ (3~seeds), 0/24 at $\\alpha{=}0.25$ (3~seeds), 0/8--6/8 at $\\alpha{=}0.50$ (seed-dependent; 3~seeds, median 3/8), and \\textbf{6/8} at $\\alpha{=}1.0$.\nAt $\\alpha{=}0.75$ (3~seeds), permutation Granger finds 19/24 forward-direction pairs FDR-significant with 0/24 reverse, confirming directional asymmetry; however, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds), placing this regime in a transitional detection state.\nUnder Bonferroni correction, approximately 3/8 pairs per seed survive, consistent with the transitional nature of the $\\alpha{=}0.75$ boundary where marginal signals are sensitive to correction stringency.\nWithin-$\\alpha$ multi-seed analysis at $\\alpha{=}1.0$ yields \\textbf{24/24} canary$\\to$diversity pairs FDR-significant across all four seeds, with 0/24 in the reverse direction, confirming temporal asymmetry.\nThe resulting dose-response pattern is monotonic: causal detectability is absent below $\\alpha{=}0.25$, seed-dependent at $\\alpha{=}0.50$, and robust above $\\alpha{=}0.75$ (Figure~\\ref{fig:regime_map}).\nThe onset boundary lies at $\\alpha{\\approx}0.25$--$0.50$, consistent with theoretical expectations about signal-to-noise limits in short time series~\\cite{boettiger2012limits}.\nAt the extremes, the transition is unambiguous: 0/24 FDR-significant pairs at $\\alpha{\\leq}0.25$ (3~seeds) versus 24/24 at $\\alpha{=}1.0$ (4~seeds, Tier~3 consensus).\nBetween these extremes, individual-seed stochasticity determines whether the consensus threshold is crossed; the data map a boundary region rather than a sharp phase transition.\nSensitivity analysis confirms that treatment/null separation is robust to FDR threshold choice ($q{=}0.01$: 0/24 null, 0/24 treatment at $\\alpha{=}0.75$; $q{=}0.10$: 0/24 null, 24/24 treatment; Appendix~\\ref{app:robustness}).\nCross-architecture validation on GPT-2-medium confirms this boundary: at $\\alpha{=}0.25$, at most 1/8 pairs reach Confirmatory consensus ($K{\\geq}4/5$), consistent with the null regime, despite substantially stronger canary drift (entropy $-32.8\\%$ vs.\\ Pythia $-4.7{\\pm}0.5\\%$), while at $\\alpha{=}1.0$ all 6 canary$\\to$diversity pairs reach $K{\\geq}4/5$ (\\S\\ref{sec:discussion}).\nTable~\\ref{tab:cross_arch_regime} summarizes the regime map across both architectures.\nAt $\\alpha{=}0.25$, GPT-2-medium yields 1/8 pairs at Tier~3 ($K{\\geq}4/5$) and 7/8 at Tier~2 ($K{\\geq}3/5$), consistent with Pythia's 0/8 Tier~3, 0/8 Tier~2 result at the same contamination level, placing both architectures in the null/low-detectability regime.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture regime map: lead-lag consensus tier and metric drift at $\\alpha{=}0.25$ and $\\alpha{=}1.0$. Tier~3: $K{\\geq}4/5$ methods; Tier~2: $K{\\geq}3/5$. Drift is generation~0$\\to$10. GPT-2-medium $\\alpha{=}0.25$: single seed (seed=42); Pythia $\\alpha{=}0.25$: 3-seed mean${\\pm}$std. The onset boundary ($\\alpha{\\approx}0.25$--$0.50$) is consistent across two transformer decoder-only model families of similar scale.}\n\\label{tab:cross_arch_regime}\n\\begin{tabular}{llcccccc}\n\\toprule\n$\\alpha$ & Model & Entropy & ECE & Distinct-1 & Distinct-2 & Perm.\\ Granger & Tier~3 \\\\\n\\midrule\n0.25 & Pythia-410M  & $-4.7{\\pm}0.5$ & $+81.8{\\pm}15.9$ & $-40.3{\\pm}0.3$ & $-56.4{\\pm}0.7$ & 0/8 & 0/8 \\\\\n0.25 & GPT-2-medium & $-32.8$ & $+422$ & $-23.5$ & $-31.6$ & 0/8 & 1/8 \\\\\n\\midrule\n1.00 & Pythia-410M  & $-60.8{\\pm}1.2$ & $+3780{\\pm}30$ & $-27.8{\\pm}1.6$ & $-34.0{\\pm}3.3$ & 6/8 & 6/6 \\\\\n1.00 & GPT-2-medium & \\multicolumn{6}{c}{(reported in \\S\\ref{sec:discussion}; all 6 canary$\\to$diversity Tier~3)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Onset boundary at $\\alpha{=}0.50$.}\nThe $\\alpha{=}0.50$ regime provides particularly informative evidence.\nNaive and differenced cross-correlation find 100\\% significance while threshold onset finds 0\\% (Table~\\ref{tab:method_comparison}), and causal methods confirm emerging detectability in a majority of seeds: two of three seeds show directional asymmetry under permutation Granger (6/8 and 3/8 forward, 0/8 reverse), while one seed shows synchronous collapse (0/8).\nThe majority-signal outcome places $\\alpha{=}0.50$ in a transitional regime where causal detectability is emerging but not yet robust, bridging the null regime ($\\alpha{\\leq}0.25$) and the consistently detectable regime ($\\alpha{\\geq}0.75$).\nThis seed dependence exemplifies our central argument: even within a single regime and method, stochastic variation in training determines whether the consensus threshold is crossed.\nAt this boundary, canary sensitivity is metric-dependent: token entropy fails to reach FDR significance in any seed ($p_{\\text{fdr}}{\\geq}0.086$), while ECE achieves significance in the two signal-positive seeds (s43, s44), identifying ECE as the more sensitive canary at the onset boundary.\nFigure~\\ref{fig:consensus_heatmap} visualizes this interaction across all method$\\times\\alpha$ combinations, revealing a clear block structure that separates correlation-based methods from causal methods as a function of regime.\n\n\n\\subsection{Case Study: Canary Prediction of Diversity Collapse}\n\\label{sec:case_study}\n\nHaving established method sensitivity (Claim~3) and regime dependence (Claim~2), we present the conditions under which canary prediction succeeds (Claim~1).\nWe scope this claim precisely: canary metrics predict \\emph{diversity collapse} (declining distinct-$n$), not model collapse broadly.\n\n\\paragraph{Full synthetic replacement ($\\alpha{=}1.0$, 4 seeds).}\nToken entropy exhibits robust Granger-precedence over diversity collapse metrics, confirmed by 4 independent statistical methods (permutation Granger power${=}1.0$), 4 seeds, and cross-architecture replication on GPT-2-medium (Tier~3 consensus; \\S\\ref{sec:discussion}).\nCross-correlation peaks at lag$={+}1$ with $|r|{>}0.99$ (cross-seed standard deviation: 0.0), establishing a consistent one-generation lead.\nFigure~\\ref{fig:metric_trajectory} illustrates the one-generation offset between token entropy decline and distinct-1 decline, visible across all four seeds.\nPermutation Granger tests (first-differenced) confirm all canary$\\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\\ref{app:distinct3}).\nReverse-direction tests (downstream$\\to$canary) find \\textbf{0/24} FDR-significant (all $p{>}0.49$), establishing complete directional asymmetry.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/metric_trajectory.pdf}\n\\caption{Metric trajectories across 10 generations at $\\alpha{=}1.0$ (Pythia-410M, 4~seeds shown as individual traces). Token entropy (top, blue) drops sharply at generation~1, while distinct-1 (bottom, red) begins declining at generations~2--3, establishing a visible one-generation canary lead. The consistent lag across all four seeds confirms that the temporal offset is robust rather than seed-specific. Shaded bands show the inter-seed range. This visual pattern corresponds to the statistical finding of 24/24 forward-direction and 0/24 reverse-direction FDR-significant pairs.}\n\\label{fig:metric_trajectory}\n\\end{figure}\n\n\\paragraph{High contamination ($\\alpha{=}0.75$, 3 seeds).}\nDirectional asymmetry is robustly confirmed across three independent seeds (permutation Granger: 19/24 forward pairs FDR-significant, 0/24 reverse).\nHowever, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds 42, 43, 44), placing $\\alpha{=}0.75$ squarely in the transitional detection regime.\nDifferenced cross-correlation finds 8/8 pairs significant in \\emph{both} forward and reverse directions at each seed, confirming that this method alone cannot distinguish genuine directional precedence from shared dynamics, a seed-level demonstration of Pitfall~1 (\\S\\ref{sec:pitfalls}).\n\n\\paragraph{ECE as a conditional secondary canary.}\nECE performs equivalently to token entropy across four of five methods (naive, differenced, threshold, permutation Granger).\nIts classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootstrap power analysis yields estimated power of 0.05--0.20 depending on $d_{\\max}$.\nResolving ECE's true canary status requires longer time series.\n\n\\paragraph{Failed canary candidates.}\nNot all metrics serve as canaries.\nEffective rank and Self-BLEU show no detectable lead-lag relationship with any downstream metric under any method or contamination level, and are excluded from the consensus framework.\nEffective rank behavior is model-dependent in an unexpected way: in Pythia-410M, effective rank decreases during collapse (representational contraction), whereas in GPT-2-medium at $\\alpha{=}0.25$ it \\emph{increases} from 2.37 to 8.48 (+258\\%).\nThe GPT-2-medium starting effective rank is near rank-2, suggesting the model's initial representation is already highly concentrated; iterative training disperses it rather than concentrating it further.\nThis opposite directionality across architectures precludes effective rank as a universal canary and motivates architecture-specific analysis (\\S\\ref{sec:discussion}).\n\n\\paragraph{Consensus filtering.}\nOf 16 canary$\\to$downstream pairs tested at $\\alpha{=}1.0$ (4 candidate canaries $\\times$ 4 downstream metrics), \\textbf{6 survive} the full consensus pipeline ($K{\\geq}4/5$ methods, $S{\\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\\ref{app:distinct3} bring the total to~6).\nThe 10 eliminated pairs comprise all canary$\\to$perplexity relationships (identified as spurious by the first-differencing diagnostic) and all effective-rank and Self-BLEU pairs (failed canaries).\nThe consensus framework reduces the naive 100\\% significance rate to the 37.5\\% rate supported by the most conservative individual methods (Figure~\\ref{fig:consensus_workflow}).\n\n\n\\subsection{Consensus Framework Validation}\n\\label{sec:consensus_validation}\n\nWe validate the consensus framework's calibration using built-in experimental controls.\n\n\\paragraph{False positive rate.}\nAt $\\alpha{=}0.0$ (three seeds, 24 total pairs), no synthetic data is injected; any detected lead-lag association is a false positive.\nIndividual-method FPR ranges from \\textbf{100\\%} (naive cross-correlation) through 37.5\\% (differenced) and 20.8\\% (threshold) down to \\textbf{0\\%} (permutation Granger: 0/24 across all three seeds).\nThe consensus framework at $K{\\geq}4/5$ achieves \\textbf{FPR${=}$0\\%} (0/24 pairs, three independent seeds), matching the best individual methods while providing robustness against miscalibration of any single method (Table~\\ref{tab:fpr_fnr}).\n\n\\paragraph{False negative rate.}\nAt $\\alpha{=}1.0$, we define 6 effect-size reference pairs (token entropy and ECE $\\to$ distinct-1/2/3) using criteria independent of the consensus methods: drift ratio ${\\geq}3\\times$ the $\\alpha{=}0.0$ baseline (entropy $11.93\\times$, ECE $73.12\\times$) and canary onset strictly preceding downstream onset by ${\\geq}1$ generation (\\S\\ref{sec:calibration}).\nFNR is calibrated on a 4-method panel (excluding differenced cross-correlation to avoid circularity): at $K{\\geq}3/4$, $S{\\geq}3/4$, all~6 are recovered (\\textbf{FNR${=}$0\\%}).\nToda--Yamamoto alone yields FNR${=}$33.3\\% (2/6), missing ECE$\\to$distinct-2 and ECE$\\to$distinct-3 due to Type~II errors at $T{=}10$.\nBoth FPR and FNR are validated on the joint method${\\times}$seed dimension (FPR: 3~seeds at $\\alpha{=}0.0$; FNR: 4~seeds at $\\alpha{=}1.0$), with cross-seed FPR variance negligible (all three seeds yield 0/8 robust pairs at $K{\\geq}4/5$).\nTable~\\ref{tab:fpr_fnr} reports the calibration results.\nTable~\\ref{tab:single-method-errors} complements this analysis by showing the practical consequences of relying on any single method: naive cross-correlation produces false positives at every $\\alpha$ including the null control, Toda--Yamamoto misses true signals at $\\alpha{=}0.75$, while the consensus at $K{\\geq}3$ yields the correct verdict across all five contamination levels.\n\n\\begin{table}[t]\n\\centering\n\\caption{Single-method inference errors across contamination levels.\nEach cell shows the verdict (significant or not) based on multi-seed majority ($\\geq$2/3 seeds with $\\geq$4/8 pairs significant).\n\\checkmark\\ = correct, \\textcolor{red}{FP} = false positive, \\textcolor{blue}{FN} = false negative, $\\circ$ = ambiguous ground truth (either verdict plausible).\nNaive XCorr produces false positives at \\emph{every} $\\alpha$ including the null control, while TY Granger misses true signals at $\\alpha{=}0.75$.\nOnly the multi-method consensus ($K{\\geq}3$) yields the correct verdict at all five contamination levels.}\n\\label{tab:single-method-errors}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n & \\multicolumn{2}{c}{\\textit{No signal}} & \\textit{Ambiguous} & \\multicolumn{2}{c}{\\textit{Causal signal}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-4} \\cmidrule(lr){5-6}\nMethod & $\\alpha{=}0.00$ & $\\alpha{=}0.25$ & $\\alpha{=}0.50$ & $\\alpha{=}0.75$ & $\\alpha{=}1.00$ \\\\\n\\midrule\nNaive XCorr\n  & \\textcolor{red}{FP}{\\scriptsize\\ 8,7,8}\n  & \\textcolor{red}{FP}{\\scriptsize\\ 8,8}\n  & $\\circ${\\scriptsize\\ 8,8,8}\n  & \\checkmark{\\scriptsize\\ 8,8,8}\n  & \\checkmark{\\scriptsize\\ 8,8,8} \\\\\nDiff XCorr (FDR)\n  & \\checkmark{\\scriptsize\\ 4,3,3}\n  & \\checkmark{\\scriptsize\\ 3,1}\n  & $\\circ${\\scriptsize\\ 8,6,6}\n  & \\checkmark{\\scriptsize\\ 8,8,8}\n  & \\checkmark{\\scriptsize\\ 8,8,8} \\\\\nThreshold Onset\n  & \\checkmark{\\scriptsize\\ 3,1,1}\n  & \\checkmark{\\scriptsize\\ 0,0}\n  & $\\circ${\\scriptsize\\ 0,0,0}\n  & \\checkmark{\\scriptsize\\ 4,0,4}\n  & \\checkmark{\\scriptsize\\ 8,8,8} \\\\\nPerm Granger (FDR)\n  & \\checkmark{\\scriptsize\\ 0,0,0}\n  & \\checkmark{\\scriptsize\\ 0,0}\n  & $\\circ${\\scriptsize\\ 0,6,3}\n  & \\checkmark{\\scriptsize\\ 8,5,6}\n  & \\checkmark{\\scriptsize\\ 6,6,6} \\\\\nTY Granger\n  & \\checkmark{\\scriptsize\\ 1,1,0}\n  & \\checkmark{\\scriptsize\\ 0,2}\n  & $\\circ${\\scriptsize\\ 0,0,0}\n  & \\textcolor{blue}{FN}{\\scriptsize\\ 1,1,1}\n  & \\checkmark{\\scriptsize\\ 6,6,4} \\\\\n\\midrule\n\\textbf{Consensus ($K{\\geq}3$)}\n  & \\checkmark\n  & \\checkmark\n  & $\\circ$\n  & \\checkmark\n  & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize Subscript numbers: per-seed significant pair counts out of 8.} \\\\\n\\multicolumn{6}{l}{\\footnotesize Seeds: $\\alpha{=}0.00/0.50/0.75$: 42, 43, 44; $\\alpha{=}0.25$: 43, 44; $\\alpha{=}1.00$: 42, 43, 45.} \\\\\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{Bootstrap power analysis.}\nTo quantify detection power beyond binary FNR, we perform bootstrap power analysis ($B{=}1{,}000$ resamples from 4-seed data at $\\alpha{=}1.0$).\nPermutation Granger achieves power${=}1.0$ on genuine pairs (canary$\\to$diversity) and power${=}0.0$ on spurious pairs (canary$\\to$perplexity), providing clean separation.\nToda--Yamamoto achieves power${=}0.05$--$0.20$ on genuine pairs (depending on $d_{\\max}$), confirming its poor sensitivity at $T{=}10$.\nWe note that bootstrap power${=}1.0$ reflects the effect size in our 4-seed data and should not be interpreted as a universal power guarantee; furthermore, the two methods use different data-generating processes for calibration (permutation Granger resamples observed $\\alpha{=}1.0$ trajectories, while Toda--Yamamoto power was estimated under a generic VAR(2) simulation with $\\beta{=}0.3$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{False positive and false negative rates for individual methods and the consensus framework (Pythia-410M). The consensus threshold $K{\\geq}4/5$ achieves FPR${=}$0\\% and FNR${=}$0\\%, matching the best individual method (permutation Granger) while providing robustness against miscalibration. FPR: $\\alpha{=}0.0$ null control (three seeds, $M{=}5$ methods); values are 3-seed means with ranges in parentheses where cross-seed variance is non-negligible. FNR: $\\alpha{=}1.0$ against 6 effect-size reference pairs (4-method panel excluding differenced cross-correlation, 4~seeds).}\n\\label{tab:fpr_fnr}\n\\begin{tabular}{lcc}\n\\toprule\nCriterion & FPR ($\\alpha{=}0.0$) & FNR ($\\alpha{=}1.0$) \\\\\n\\midrule\nNaive XCorr              & 100\\%              & 0\\%  \\\\\nDifferenced XCorr        & 37.5\\%             & 0\\%  \\\\\nThreshold Onset          & 20.8\\% (12.5--37.5) & 0\\%  \\\\\nPermutation Granger      & 0\\%                & 0\\%  \\\\\nToda--Yamamoto           & 4.2\\% (0--12.5)    & 33.3\\% \\\\\n\\midrule\nConsensus ($K{\\geq}4/5$)              & 0\\%    & 0\\%  \\\\\nConsensus ($K{\\geq}4/5$, $S{\\geq}3/4$) & 0\\%    & 0\\%  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Cross-Architecture, Cross-Scale, and Cross-Domain Generalization}\n\\label{sec:generalization}\n\nThe methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).\nTo test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).\nAll conditions use $\\alpha{=}1.0$ and a single seed.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\\alpha{=}1.0$, single seed per condition). Each cell reports the fraction of canary$\\to$downstream pairs reaching BH-corrected FDR significance ($q{=}0.05$): 8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded). \\textbf{[TBD]}: experiments in progress.}\n\\label{tab:generalization}\n\\begin{tabular}{llccccccc}\n\\toprule\nVariation & Model / Dataset & \\rotatebox{70}{Naive} & \\rotatebox{70}{Diff.\\ XCorr} & \\rotatebox{70}{Threshold} & \\rotatebox{70}{PermG (fwd)} & \\rotatebox{70}{PermG (rev)} & \\rotatebox{70}{TY} & \\rotatebox{70}{$K{\\geq}4/5$} \\\\\n\\midrule\nBaseline      & Pythia-410M / Wiki    & 7/8 & 6/8 & 6/8 & 6/8 & 0/8 & 6/8 & 6/8 \\\\\nArchitecture  & GPT-2-medium / Wiki   & 6/6 & 6/6 & 6/6 & 6/6 & 0/6 & 0/6 & 6/6 \\\\\nArchitecture  & OPT-1.3B / Wiki       & 6/8 & 6/8 & 8/8 & 6/8 & 0/8 & 2/8 & 6/8 \\\\\nScale ($3.4\\times$) & Pythia-1.4B / Wiki & \\multicolumn{7}{c}{\\textbf{[TBD]}} \\\\\nDomain        & Pythia-1B / C4        & \\multicolumn{7}{c}{\\textbf{[TBD]}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Architecture generalization.}\nTable~\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\nAll models reach Tier~3 consensus ($K{\\geq}4/5$) with 6/8 (or 6/6) canary$\\to$diversity pairs confirmed.\nPermutation Granger directionality is perfect across architectures: all forward-direction pairs are FDR-significant while 0 reverse-direction pairs reach significance in any architecture.\n\nMethod-level variation across architectures is informative.\nThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\to$1 discontinuity that cleanly exceeds the onset threshold.\nToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\S\\ref{sec:consensus_validation}).\nDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\geq}4/5$.\n\n% [PLACEHOLDER — activate when Pythia-1.4B and Pythia-1B/C4 results arrive]\n% \\paragraph{Scale and domain generalization.}\n% Scaling from 410M to 1.4B parameters within the Pythia family (3.4$\\times$)\n% preserves the core pattern: permutation Granger identifies \\textbf{XX}/8\n% forward-direction pairs with 0/8 reverse, and consensus $K{\\geq}4/5$\n% yields \\textbf{XX}/8 (Table~\\ref{tab:generalization}).\n% This confirms that the methodological pitfalls are not artifacts of\n% small-model capacity limitations, since the same consensus threshold\n% operates identically at 3.4$\\times$ the parameter count.\n%\n% Replacing WikiText-103 with C4 tests whether the lead-lag pattern\n% depends on the training data distribution. Pythia-1B on C4 yields\n% \\textbf{XX}/8 forward-direction permutation Granger pairs with\n% \\textbf{XX}/8 reverse, and consensus $K{\\geq}4/5$ at \\textbf{XX}/8.\n% Together with the architecture results, this establishes five\n% independent validation lines (three architectures, one scale, one\n% domain) converging on the same conclusion: token entropy\n% Granger-precedes diversity collapse at $\\alpha{=}1.0$.",
      "numLines": 382,
      "startLine": 1,
      "totalLines": 382
    }
  },
  "sourceToolAssistantUUID": "6b6c4f3a-cda1-4f01-86a6-79d71dc5d613",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

</details>

---


### Runtime record

_source line 1263_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] **CRITICAL: 论文 Table 7 有 8+ 处错误数据 — 立即修复**  上次 Worker 失败，论文未被修改。Reviewer 逐格核对发现至少 8 个数字错误 + 2 行缺失 + 多处正文引用错误。必须立即修复，否则是 desk reject 级数据完整性问题。  **编辑 `docs/paper/experiments.tex`（C002 真源）：…",
  "leafUuid": "38f1eb95-54d3-4db5-9606-83586947d011",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35"
}
```

---


### Runtime record

_source line 1264_

```json
{
  "type": "ai-title",
  "aiTitle": "Finalize paper Round 2 with C4 seed-43 analysis",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35"
}
```

---


### Runtime record

_source line 1265_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] **CRITICAL: 论文 Table 7 有 8+ 处错误数据 — 立即修复**  上次 Worker 失败，论文未被修改。Reviewer 逐格核对发现至少 8 个数字错误 + 2 行缺失 + 多处正文引用错误。必须立即修复，否则是 desk reject 级数据完整性问题。  **编辑 `docs/paper/experiments.tex`（C002 真源）：…",
  "leafUuid": "38f1eb95-54d3-4db5-9606-83586947d011",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35"
}
```

---


### Runtime record

_source line 1266_

```json
{
  "type": "ai-title",
  "aiTitle": "Finalize paper Round 2 with C4 seed-43 analysis",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35"
}
```

---


### System

_source line 1267 · 2026-05-18T12:56:54.165Z_

```json
{
  "parentUuid": null,
  "logicalParentUuid": "38f1eb95-54d3-4db5-9606-83586947d011",
  "isSidechain": false,
  "type": "system",
  "subtype": "compact_boundary",
  "content": "Conversation compacted",
  "isMeta": false,
  "timestamp": "2026-05-18T12:56:54.165Z",
  "uuid": "ed3e3c39-338b-4e8e-b2d8-3aa3d36ebb33",
  "level": "info",
  "compactMetadata": {
    "trigger": "auto",
    "preTokens": 167340,
    "preCompactDiscoveredTools": [
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_registry"
    ],
    "postTokens": 4142,
    "durationMs": 147110
  },
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

---


## Round 142

## Round 142

23 recorded events


### User

_source line 1268 · 2026-05-18T12:56:54.166Z_

This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.

Summary:
1. Primary Request and Intent:
   This is an ML research agent session managing the "distrib_canary_collapse" project (EMNLP 2026 target). The session handled multiple critical tasks:
   
   - **M004 n_perm Bug Fix Verification**: analyze_generalize.py's `--n_perm` parameter wasn't being passed to `perm_granger()`, meaning all prior analyses used n_perm=1000 instead of 5000. Director ordered full rerun of all 6 Table 7 conditions. Result: **PG significance is completely stable** between n_perm=1000 and 5000 across all conditions.
   
   - **M005 C4 Downstream Unification**: Discovered that old C4 s42 analysis used **mauve** as 4th downstream instead of perplexity. Director confirmed: unify all conditions to perplexity as 4th downstream ({token_entropy, ece} × {d1, d2, d3, ppl} = 8 canonical pairs).
   
   - **GPT-2m v4 Analysis**: Completed analysis with n_perm=5000 after training finished. Table 7 row: Naive=8/8, Diff=8/8, Thresh=8/8, PG_fwd=6/8, PG_rev=3/8, TY=5/8, K≥4=6/8.
   
   - **Intervention Experiments Launch**: intervention_predictive_s42 submitted on cuda:0 (PID 351357, token_entropy >15% drop trigger), intervention_reactive_s42 running on cuda:1 (PID 340964, distinct_1 >10% drop trigger).
   
   - **CRITICAL Paper Table 7 Update**: Director's final and most recent order — comprehensive update of experiments.tex Table 7 with 8+ error fixes, plus related text in discussion.tex and conclusion.tex. Director explicitly said "不要 spawn worker，直接在当前 session 完成编辑" (don't spawn worker, edit directly in current session).

2. Key Technical Concepts:
   - Permutation Granger causality (n_perm=5000, max_lag=1) — D057 unified parameters
   - Raw p<0.05 with consensus K≥4/5 as multiplicity control
   - 8 canonical pairs: {token_entropy, ECE} × {distinct_1, distinct_2, distinct_3, perplexity}
   - PG_fwd (canary→downstream) and PG_rev (downstream→canary) directionality
   - Canary quality hierarchy: token_entropy (0/24 reverse across all conditions) > ECE (condition-dependent reverse)
   - Intervention experiments: predictive (canary-triggered, token_entropy >15% drop) vs reactive (downstream-triggered, distinct_1 >10% drop)
   - n_perm bug: analyze_generalize.py wasn't passing --n_perm to perm_granger(), fixed by worker
   - M005: C4 old analysis incorrectly used mauve instead of perplexity as downstream
   - Registry state machine: PREPARING → PENDING → QUEUED → ALLOCATED → RUNNING → ANALYZING → DONE

3. Files and Code Sections:

   - **`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex`** (local, C002 true source)
     - **This is the CRITICAL file to edit now.** Read in full (384+ lines).
     - Table 7 (`\label{tab:generalization}`) at lines 337-353 has WRONG data that must be replaced:
       - Current Baseline row (L346): `7/8 & 6/8 & 6/8 & 6/8 & 0/8 & 6/8 & 6/8` — ALL WRONG
       - Current GPT-2m row (L347): `6/6 & 6/6 & 6/6 & 6/6 & 0/6 & 0/6 & 6/6` — WRONG (uses /6 denominator, MAUVE excluded)
       - Current OPT-1.3B row (L348): `6/8 & 6/8 & 8/8 & 6/8 & 0/8 & 2/8 & 6/8` — PARTIALLY WRONG
       - Scale and Domain rows (L349-350): `\multicolumn{7}{c}{\textbf{[TBD]}}` — Need to be filled
     - Caption (L340): Says "6~pairs for GPT-2-medium (MAUVE excluded)" — must change to 8 pairs, remove MAUVE exclusion
     - Line 335: "All conditions use $\alpha{=}1.0$ and a single seed." — needs update for multi-seed conditions
     - Line 362: "Toda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M)" — WRONG. Should be "0/8 (Scale 1.4B s42) to 6/8 (OPT-1.3B)"
     - Lines 365-379: Commented out placeholders for Scale/Domain paragraphs — need to be activated and filled with real data
   
   - **`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex`** (local)
     - Needs GPT-2m "Preliminary" conditional phrasing removed
     - Not yet read in this session
   
   - **`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex`** (local)
     - Needs GPT-2m "Preliminary" conditional phrasing removed
     - Not yet read in this session
   
   - **Remote: `/root/autodl-tmp/distrib_canary_collapse/analyze_generalize.py`** (on westd-19828)
     - Bug fixed by worker: --n_perm parameter now properly passed to perm_granger() (3 places fixed)
   
   - **Remote: `/root/autodl-tmp/distrib_canary_collapse/iterative_train.py`** (on westd-19828)
     - Previously modified with intervention mode support (~40 lines) and checkpoint auto-cleanup
   
   - **Artifacts saved**: `artifacts/M004_nperm5000/` on remote server with 6 subdirectories containing persisted analysis results

4. Errors and fixes:
   - **intervention_reactive_s42 not in registry**: The experiment was running (PID 340964) with a cron monitoring it, but the registry entry was stuck at PREPARING. Fixed by pushing through state machine: PREPARING→PENDING→QUEUED→ALLOCATED→RUNNING with proper spec.
   
   - **intervention_predictive_s42 stuck at PREPARING for 8+ hours**: Director flagged as CRITICAL — cuda:0 idle. The previous session's worker did analysis but never submitted the training. Fixed by directly calling submit_training_job (PID 351357) and pushing registry to RUNNING.
   
   - **n_perm bug in analyze_generalize.py**: --n_perm parameter not passed through to perm_granger(). All prior analyses actually used n_perm=1000. Worker fixed 3 pass-through points. Verified: results stable between n_perm=1000 and 5000.
   
   - **C4 s42 mauve vs perplexity mismatch**: Old C4 analysis used mauve as 4th downstream while all other conditions used perplexity. This caused apparent "flips" (Diff 8→6, PG_fwd 8→6) that were actually downstream metric changes, not n_perm effects. Director confirmed: unify to perplexity.
   
   - **16-pair vs 8-pair output**: analyze_generalize.py outputs 16 pairs (4 canaries × 4 downstreams) but Table 7 uses only 8 canonical pairs (2 canaries × 4 downstreams). Required extraction of subset for proper comparison.
   
   - **Paper update worker failed twice**: First worker (worker_paper_table7_update_m004) failed with no error output. Second worker (worker_paper_table7_update_m004_v2) spawned but server restarted before completion could be confirmed. Director then ordered direct editing without workers.
   
   - **Predictive cron possibly lost after server restart**: reconcile_crons only found reactive's cron, not predictive's. Not yet fixed.

5. Problem Solving:
   - **M004 validation complete**: All 6 Table 7 conditions verified with n_perm=5000. PG significance fully stable. Only changes: OPT Diff 8→6 (non-n_perm, code version) and C4 s42 corrections (mauve→ppl downstream change).
   - **Complete Table 7 assembled** (only missing 6.9B and GPT-2m s43):
     | Condition | Naive | Diff | Thresh | PG_fwd | PG_rev | TY | K≥4 |
     |-----------|-------|------|--------|--------|--------|-----|-----|
     | Baseline 410M | 8/8 | 8/8 | 8/8 | 6/8 | 3/8 | 4/8 | 6/8 |
     | GPT-2m | 8/8 | 8/8 | 8/8 | 6/8 | 3/8 | 5/8 | 6/8 |
     | OPT-1.3B | 8/8 | 6/8 | 8/8 | 6/8 | 2/8 | 6/8 | 6/8 |
     | Scale 1.4B s42 | 7/8 | 6/8 | 8/8 | 5/8 | 0/8 | 0/8 | 5/8 |
     | Scale 1.4B s43 | 8/8 | 6/8 | 8/8 | 6/8 | 2/8 | 4/8 | 6/8 |
     | C4 s42 | 8/8 | 6/8 | 8/8 | 6/8 | 3/8 | 3/8 | 6/8 |
     | C4 s43 | 8/8 | 6/8 | 8/8 | 6/8 | 0/8 | 3/8 | 6/8 |
   - **GPU saturation maintained**: Both cuda:0 (intervention_predictive PID 351357) and cuda:1 (intervention_reactive PID 340964) running. ~4-5h each estimated.
   - **Predictive cron may need re-registration** after server restart.

6. All user messages:
   - [服务器重启后首条消息] Current date 2026-05-18, server just restarted (opening message with prior session summary)
   - [WORKER DONE] worker_analysis_14b_s43_nperm5000_reverse_20260518T103359 done
   - [Director 指令] M004 修复 — n_perm 传参 bug 全量重跑所有 Table 7 分析（CPU 任务）— 6 conditions with fixed script
   - [WORKER DONE] worker_ops_check_progress_and_prepare_20260518T104000 done
   - [WORKER DONE] worker_analysis_nperm5000_rerun_batch1_20260518T105511 done
   - [WORKER DONE] worker_analysis_nperm5000_rerun_batch2_20260518T111504 done
   - [Director 指令] M004 修复 持久化 + 格式修正 — each condition to independent output_dir, extract 8 canonical pairs
   - [WORKER DONE] worker_analysis_m004_persist_batch2_20260518T111756 done
   - [WORKER DONE] worker_analysis_nperm5000_extract_8pair_20260518T111647 done
   - [WORKER DONE] worker_analysis_m004_persist_batch1_20260518T111739 done
   - [Director 指令] M004 决策回复 — C4 ppl confirmed, OPT Diff accepted, GPT-2m to analyze when done
   - [Director 指令] GPT-2m v4 完成 — 立即执行 3 步 (analyze + report + launch predictive)
   - [Director 指令] 紧急: cuda:0 空闲 8+ 小时 — intervention_predictive_s42 卡在 PREPARING
   - [Director 指令] 已批准。分析完成后立即在 cuda:0 启动 intervention_predictive_s42
   - [WORKER DONE] worker_analysis_gen_wiki_gpt2m_a100_s42_v4_20260518T113124 done
   - [WORKER DONE] worker_analysis_gpt2m_v4_table7_20260518T113128 done
   - [Director 指令] 论文 Table 7 更新（不依赖 GPU，立即执行）— edit experiments.tex with all final numbers
   - [服务器重启后首条消息] + [WORKER DONE] worker_paper_table7_update_m004_20260518T122421 failed
   - [Director 指令] CRITICAL: 论文 Table 7 有 8+ 处错误数据 — 立即修复. Comprehensive fix list (A through F). "不要 spawn worker，直接在当前 session 完成编辑。"

7. Pending Tasks:
   - **CRITICAL (immediate)**: Edit experiments.tex Table 7 with correct data for all 7 rows + fix caption + fix Architecture paragraph + fix Domain paragraph + remove mauve references + activate Scale/Domain paragraphs. Also edit discussion.tex and conclusion.tex to remove GPT-2m "Preliminary" phrasing. Director explicitly said to do this directly, not via worker.
   - **Predictive cron re-registration**: reconcile_crons only found reactive's cron after server restart. Need to register_cron for intervention_predictive_s42.
   - **Waiting for intervention experiments**: Both ~4-5h remaining. When done: analyze results, update registry, report to Director.
   - **Future**: α=0.60 and α=0.10 experiments after interventions complete. Then 6.9B (~50h).

8. Current Work:
   I had just read experiments.tex in full (the file is at `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex`) and was about to begin editing when the summary was requested. 
   
   The Director's CRITICAL instruction specifies these exact edits:
   
   **A. Table 7 data** (lines 346-350 in current file): Replace all rows with final n_perm=5000 confirmed numbers. Add 4 new rows (GPT-2m corrected, Scale 1.4B s43, C4 s42, C4 s43).
   
   **B. Caption** (line 340): Change "6~pairs for GPT-2-medium (MAUVE excluded)" to 8 pairs for all conditions.
   
   **C. Remove mauve references**: Domain segment that says "We exclude perplexity as a downstream variable in the C4 setting" and footnotes about "token_entropy→mauve".
   
   **D. Architecture paragraph** (line 362): Fix "Toda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M)" → "TY ranges from 0/8 (Scale 1.4B s42) to 6/8 (OPT-1.3B)"
   
   **E. Domain (C4) paragraph**: Fix "achieves 7/8 consensus at K≥4/5" → 6/8, "PermG forward reaches 8/8" → 6/8, add C4 s43 results.
   
   **F. GPT-2m Preliminary removal**: In conclusion.tex and discussion.tex.

9. Optional Next Step:
   **Continue editing experiments.tex** — I already read the file and identified all locations that need changes. The Director's most recent message was: "**CRITICAL: 论文 Table 7 有 8+ 处错误数据 — 立即修复**" with the instruction "不要 spawn worker，直接在当前 session 完成编辑。"
   
   The specific edits needed on the already-read experiments.tex:
   1. Replace Table 7 rows at lines 346-350 with correct 7-row data
   2. Fix caption at line 340 (remove MAUVE exclusion, change to 8 pairs)
   3. Fix line 362 (TY range description)
   4. Activate and fill the commented-out Scale/Domain paragraphs (lines 365-379)
   5. Then read and edit discussion.tex and conclusion.tex for GPT-2m conditional phrasing
   6. Verify with grep for residual errors
   
   Also need to re-register intervention_predictive_s42 cron and sync edited local files to the remote server.

If you need specific details from before compaction (like exact code snippets, error messages, or content you generated), read the full transcript at: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-agent-069782ef/26354fff-825d-4709-85fd-1f95e9631e35.jsonl
Continue the conversation from where it left off without asking the user any further questions. Resume directly — do not acknowledge the summary, do not recap what was happening, do not preface with "I'll continue" or similar. Pick up the last task as if the break never happened.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed3e3c39-338b-4e8e-b2d8-3aa3d36ebb33",
  "isSidechain": false,
  "promptId": "e0dec198-abf3-497e-80c7-3f5c472bf9b3",
  "type": "user",
  "isVisibleInTranscriptOnly": true,
  "isCompactSummary": true,
  "uuid": "7b151bd5-0bf0-4111-ba61-0119d0013369",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

</details>

---


### Runtime record

_source line 1269 · 2026-05-18T12:56:54.162Z_

```json
{
  "parentUuid": "7b151bd5-0bf0-4111-ba61-0119d0013369",
  "isSidechain": false,
  "attachment": {
    "type": "compact_file_reference",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
    "displayPath": "../../../docs/paper/experiments.tex"
  },
  "type": "attachment",
  "uuid": "f694b2f9-8cc7-4807-9217-9ba49832c355",
  "timestamp": "2026-05-18T12:56:54.162Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

---


### Runtime record

_source line 1270 · 2026-05-18T12:56:54.164Z_

```json
{
  "parentUuid": "f694b2f9-8cc7-4807-9217-9ba49832c355",
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
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
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "2808d440-166e-405c-b4ea-4e5e764ee138",
  "timestamp": "2026-05-18T12:56:54.164Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

---


### Runtime record

_source line 1271 · 2026-05-18T12:56:54.165Z_

```json
{
  "parentUuid": "2808d440-166e-405c-b4ea-4e5e764ee138",
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
  "uuid": "5a40d640-232f-4480-b9e9-839b37813ca9",
  "timestamp": "2026-05-18T12:56:54.165Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

---


### Assistant

_source line 1272 · 2026-05-18T12:56:58.927Z_

<details><summary>Logged reasoning block</summary>

```text
Let me continue with the critical task: editing experiments.tex Table 7 with correct data. I need to read the file first since the context was compacted, then make all the edits the Director specified.

Let me read experiments.tex to see the current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a40d640-232f-4480-b9e9-839b37813ca9",
  "isSidechain": false,
  "requestId": "req_011CbA57jbEdJwwNs5vsWAN5",
  "type": "assistant",
  "uuid": "7e2695c9-0350-4c29-9315-ff8c64b723e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRBSMWqu5hPYG9XLbtafPy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29796,
      "cache_read_input_tokens": 11841,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 162,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 29796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29796
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

_source line 1273 · 2026-05-18T12:56:59.345Z_

<details open><summary>🔧 Tool call — Read · `toolu_013VuEQaPjsGzkpz1vw5TGwU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e2695c9-0350-4c29-9315-ff8c64b723e0",
  "isSidechain": false,
  "requestId": "req_011CbA57jbEdJwwNs5vsWAN5",
  "type": "assistant",
  "uuid": "3d57549f-b14b-49fd-a659-e07123890b4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SRBSMWqu5hPYG9XLbtafPy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29796,
      "cache_read_input_tokens": 11841,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 29796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 162,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 29796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 29796
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

_source line 1274 · 2026-05-18T12:56:59.724Z_

<details><summary>↩ Tool result · `toolu_013VuEQaPjsGzkpz1vw5TGwU`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter decoder-only language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Cross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \S\ref{sec:method_sensitivity}, \S\ref{sec:regime}, and \S\ref{sec:discussion}.
10	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
11	
12	Our protocol follows the replace paradigm of \citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\alpha{<}1.0$.
13	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.
14	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.25, 0.50, 0.75, 1.00\}$.
15	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; $\alpha{=}0.00$, $\alpha{=}0.25$, and $\alpha{=}0.75$ each use three seeds $\{42, 43, 44\}$; $\alpha{=}0.50$ uses three seeds $\{42, 43, 44\}$.
16	
17	We track two \emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}) and three \emph{downstream metrics}.
18	Canary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).
19	Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).
20	Token entropy is the mean next-token prediction entropy $H(p_\theta | \text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.
21	We additionally evaluate effective rank and Self-BLEU as candidate canaries (\S\ref{sec:case_study}).
22	Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
23	Code and data will be released upon publication.
24	
25	All hypothesis tests apply Benjamini--Hochberg (BH) FDR correction at $q{=}0.05$.
26	Permutation Granger causality tests use 5{,}000 permutations on first-differenced series \cite{shojaie2022granger}.
27	Cross-correlation analysis uses a maximum lag of 5 generations.
28	Table~\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.
29	
30	\begin{table}[t]
31	\centering
32	\small
33	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
34	\label{tab:drift_summary}
35	\begin{tabular}{lccccc}
36	\toprule
37	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
38	\midrule
39	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
40	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
41	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
42	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}0.7$ \\
43	1.00 & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
44	\bottomrule
45	\end{tabular}
46	\end{table}
47	
48	
49	\subsection{Method Sensitivity Analysis}
50	\label{sec:method_sensitivity}
51	
52	We open with Claim~3 (method sensitivity) because it conditions the interpretation of all subsequent results.
53	If different statistical methods yield contradictory conclusions on the same data, any single-method analysis is unreliable by construction.
54	
55	\paragraph{Five-method ablation.}
56	We apply five lead-lag detection methods to the $\alpha{=}1.0$ condition (4~seeds, 16 canary$\to$downstream pairs).
57	The fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \textbf{16/16} (100\%), differenced cross-correlation \textbf{14/16} (87.5\%), threshold onset detection \textbf{9/16} (56.3\%), permutation Granger causality \textbf{6/16} (37.5\%), and Toda--Yamamoto Granger \textbf{4/16} (25.0\%).
58	Method choice alone swings significance from \textbf{100\% to 25\%}: 50--57\% of pairs classified as significant under one method flip to non-significant under another.
59	The spurious-signal rate (the fraction of pairs detected by the most liberal method but not confirmed by the most conservative) is \textbf{75\%} across all five methods and \textbf{62.5\%} when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate (\S\ref{sec:consensus_validation}).
60	Table~\ref{tab:method_comparison} reports significance rates restricted to 8 validated canary$\to$downstream pairs (excluding failed candidates); the 16-pair rates above include effective rank and Self-BLEU to capture the full method-sensitivity landscape.
61	
62	\paragraph{First-differencing diagnostic.}
63	A single preprocessing decision can eliminate an entire analysis channel.
64	For canary$\to$diversity pairs at $\alpha{=}1.0$, all pairs retain unanimous FDR significance after first-differencing (24/24$\to$24/24), confirming genuine temporal precedence rather than shared-trend confounding.
65	For canary$\to$perplexity, however, undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find \textbf{zero} significant pairs ($F{\approx}0$, $p{=}0.99$; Figure~\ref{fig:differencing_dmax}a).
66	The apparent canary$\to$perplexity relationship is entirely an artifact of co-trending.
67	Notably, at $\alpha{=}0.75$, differenced cross-correlation finds 8/8 pairs significant in \emph{both} forward and reverse directions per seed, demonstrating that this method alone cannot distinguish genuine directional precedence from shared dynamics even after detrending.
68	
69	\paragraph{Augmentation order sensitivity.}
70	Toda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\max}$ (Figure~\ref{fig:differencing_dmax}b).
71	At $d_{\max}{=}0$ (most permissive), approximately 6\% of pairs are rejected; at adaptive $d_{\max}$ determined by ADF unit-root tests, 75\%; at $d_{\max}{=}1$ (most conservative), \textbf{94\%}.
72	This single hyperparameter swings conclusions from near-universal significance to near-universal non-significance.
73	
74	\begin{figure}[t]
75	\centering
76	\includegraphics[width=\linewidth]{figures/differencing_dmax.pdf}
77	\caption{First-differencing diagnostic and augmentation order sensitivity (Pythia-410M, $\alpha{=}1.0$, 4~seeds). \textbf{(a)}~First-differencing eliminates the canary$\to$perplexity channel: undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find zero significant pairs ($F{\approx}0$, $p{=}0.99$), exposing these associations as shared-trend artifacts. Canary$\to$diversity pairs retain significance after differencing (24/24$\to$24/24). \textbf{(b)}~Toda--Yamamoto Granger significance rates vary dramatically with augmentation order $d_{\max}$: from $\sim$6\% rejection at $d_{\max}{=}0$ to 94\% at $d_{\max}{=}1$, demonstrating that this single hyperparameter can reverse conclusions about temporal precedence.}
78	\label{fig:differencing_dmax}
79	\end{figure}
80	
81	\paragraph{Inter-method agreement.}
82	Cohen's $\kappa$, averaged over all method pairs, is \textbf{0.185} (near chance; poor agreement); this value is consistent across contamination levels ($\alpha{=}0.0$ through $\alpha{=}1.0$), indicating that method disagreement is a structural property of the analysis rather than a regime-specific artifact.
83	Cross-architecture validation on GPT-2-medium (12 canary$\to$downstream pairs) yields Fleiss' $\kappa{=}0.091$, also in the ``slight agreement'' range, confirming that low inter-method agreement is not architecture-specific.
84	Restricting to three informative methods (excluding naive cross-correlation and Toda--Yamamoto, which anchor the permissive and conservative extremes respectively) raises $\kappa$ to 0.667 (substantial agreement), indicating that the low full-panel $\kappa$ is driven by the deliberate inclusion of methods spanning the entire permissive-to-conservative spectrum rather than by fundamental incoherence among methods.
85	Table~\ref{tab:method_comparison} extends the analysis across contamination levels.
86	At $\alpha{=}0.0$ (no synthetic data, serving as null control), naive cross-correlation finds \textbf{100\%} of pairs significant, a textbook spurious-regression outcome in trending time series.
87	Permutation Granger correctly finds 0\% across all three null-control seeds; Toda--Yamamoto finds 0--12.5\% (1/24 total, attributable to a degenerate $\text{df}_{\text{resid}}{=}1$ case; \S\ref{sec:consensus_validation}).
88	At $\alpha{=}0.50$, naive and differenced cross-correlation both find 100\% significance while threshold onset and all causal methods find 0\% (Figure~\ref{fig:consensus_heatmap}), illustrating that even among non-causal methods, sensitivity diverges sharply at this boundary.
89	
90	\paragraph{Method$\times$regime interaction.}
91	Table~\ref{tab:method_comparison} reveals that the correlation-versus-causal divergence is not uniform across contamination levels.
92	At $\alpha{=}0.25$, differenced cross-correlation drops to 25\% and threshold onset to 0\%, while naive cross-correlation remains at 100\%, demonstrating that even partial detrending removes marginal associations at low contamination.
93	In the lowest-contamination regime ($\alpha{\leq}0.25$, three seeds), the false confirmation rate for the most liberal method approaches 100\%, while all Granger-type tests correctly find 0\%, a regime where single-method analysis is maximally dangerous.
94	The graded response across methods, combined with the block structure visible in Figure~\ref{fig:consensus_heatmap}, motivates the regime-dependent analysis in \S\ref{sec:regime}.
95	
96	\begin{figure}[t]
97	\centering
98	\includegraphics[width=\linewidth]{figures/consensus_heatmap.pdf}
99	\caption{Method$\times$regime consensus heatmap (Pythia-410M). Each cell shows the consensus tier ($K$-of-$M$ agreement) for a given lead-lag method (rows) and contamination level $\alpha$ (columns). A clear block structure emerges: correlation-based methods (naive, differenced, threshold) find significance across all $\alpha$ levels, while Granger-type methods find significance only at $\alpha{\geq}0.75$. The $\alpha{=}0.50$ column is maximally dangerous (high correlation coexists with zero causal precedence), illustrating Pitfall~3 (regime dependence). Color scale: dark = significant (Tier~3), light = non-significant (Tier~1).}
100	\label{fig:consensus_heatmap}
101	\end{figure}
102	
103	\begin{table}[t]
104	\centering
105	\small
106	\caption{FDR significance rates (\%) for five lead-lag methods across contamination levels (Pythia-410M). Method choice swings significance from 100\% (naive cross-correlation) to 0\% (permutation Granger) at $\alpha{\leq}0.25$, with seed-dependent onset at $\alpha{=}0.50$, demonstrating that single-method conclusions are unreliable. Each cell reports the fraction of 8 canary$\to$downstream pairs (token entropy and ECE $\times$ 4 downstream metrics) reaching BH-corrected significance ($q{=}0.05$), excluding failed candidates (\S\ref{sec:case_study}). Seed coverage: $\alpha{=}1.0$: 4 seeds (32 pairs); $\alpha{=}0.00$, $\alpha{=}0.75$: 3 seeds (24 pairs); $\alpha{=}0.25$ Toda--Yamamoto: 3 seeds (24 pairs), other methods single seed; $\alpha{=}0.50$: 3~seeds for permutation Granger (range shown), single seed for other methods. $^\dagger$Seed-dependent onset: s42${=}$0/8, s43${=}$6/8, s44${=}$3/8 (median 3/8).}
107	\label{tab:method_comparison}
108	\begin{tabular}{lcccccc}
109	\toprule
110	Method & $\alpha{=}0.0$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.0$ & FPR$_\text{null}$ \\
111	\midrule
112	Naive XCorr     & 100   & 100  & 100  & 100   & 100   & 100  \\
113	Diff.\ XCorr   & 37.5  & 25   & 100  & 100   & 100   & 37.5 \\
114	Threshold       & 20.8  & 0    & 0    & 33.3  & 100   & 20.8 \\
115	Perm.\ Granger  & 0     & 0    & 0--75$^\dagger$  & 79.2  & 75    & 0    \\
116	Toda--Yamamoto  & 0     & 12.5 & 0    & 12.5  & 59.4  & 0    \\
117	\bottomrule
118	\end{tabular}
119	\end{table}
120	
121	
122	\subsection{Regime-Dependent Detectability}
123	\label{sec:regime}
124	
125	Beyond method choice, the contamination level~$\alpha$ determines whether a temporal lead exists to detect.
126	We present regime effects at two levels: raw metric drift (method-independent) and Granger-precedence detectability.
127	
128	\paragraph{Raw drift.}
129	Table~\ref{tab:drift_summary} shows that diversity collapse occurs at \emph{all} contamination levels, not only under full synthetic replacement.
130	Distinct-1 declines by 13.8\% even at $\alpha{=}0.0$ (attributable to fine-tuning on repeated real-data subsets), and more steeply at intermediate contamination: $-40.3{\pm}0.3\%$ ($\alpha{=}0.25$), $-37.1{\pm}0.4\%$ ($\alpha{=}0.50$), $-32.3{\pm}0.5\%$ ($\alpha{=}0.75$), and $-27.8{\pm}1.6\%$ ($\alpha{=}1.0$).
131	The non-monotonic pattern (diversity declining \emph{more} at moderate~$\alpha$ than at extreme~$\alpha$) is confirmed by 3-seed replication at $\alpha{=}0.25$ (std${=}0.3\%$), indicating that this relationship between contamination level and collapse severity is robust rather than a seed-specific artifact.
132	
133	\begin{figure}[t]
134	\centering
135	\includegraphics[width=\linewidth]{figures/regime_map.pdf}
136	\caption{Detectability regime map across contamination levels (Pythia-410M). Permutation Granger FDR significance rate (solid line) and consensus tier (shaded regions) as a function of $\alpha$. The onset boundary lies at $\alpha{\approx}0.25$--$0.50$: at $\alpha{\leq}0.25$, all seeds agree on null (0/24); at $\alpha{=}0.50$, detectability is seed-dependent (0/8--6/8, 3~seeds, median 3/8); at $\alpha{=}0.75$, directional asymmetry emerges robustly (19/24 forward, 0/24 reverse, 3~seeds) but method consensus remains transitional (Tier~2--3); at $\alpha{=}1.0$, full Confirmatory consensus is achieved (24/24 forward, Tier~3, 4~seeds). Multi-seed replication: $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3~seeds; $\alpha{=}1.0$: 4~seeds.}
137	\label{fig:regime_map}
138	\end{figure}
139	
140	\paragraph{Granger-precedence detectability.}
141	Despite ubiquitous drift, causal detectability is sharply regime-dependent (Figure~\ref{fig:regime_map}).
142	Permutation Granger tests (first-differenced, BH-corrected) find 0/24 pairs FDR-significant at $\alpha{=}0.00$ (3~seeds), 0/24 at $\alpha{=}0.25$ (3~seeds), 0/8--6/8 at $\alpha{=}0.50$ (seed-dependent; 3~seeds, median 3/8), and \textbf{6/8} at $\alpha{=}1.0$.
143	At $\alpha{=}0.75$ (3~seeds), permutation Granger finds 19/24 forward-direction pairs FDR-significant with 0/24 reverse, confirming directional asymmetry; however, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds), placing this regime in a transitional detection state.
144	Under Bonferroni correction, approximately 3/8 pairs per seed survive, consistent with the transitional nature of the $\alpha{=}0.75$ boundary where marginal signals are sensitive to correction stringency.
145	Within-$\alpha$ multi-seed analysis at $\alpha{=}1.0$ yields \textbf{24/24} canary$\to$diversity pairs FDR-significant across all four seeds, with 0/24 in the reverse direction, confirming temporal asymmetry.
146	The resulting dose-response pattern is monotonic: causal detectability is absent below $\alpha{=}0.25$, seed-dependent at $\alpha{=}0.50$, and robust above $\alpha{=}0.75$ (Figure~\ref{fig:regime_map}).
147	The onset boundary lies at $\alpha{\approx}0.25$--$0.50$, consistent with theoretical expectations about signal-to-noise limits in short time series~\cite{boettiger2012limits}.
148	At the extremes, the transition is unambiguous: 0/24 FDR-significant pairs at $\alpha{\leq}0.25$ (3~seeds) versus 24/24 at $\alpha{=}1.0$ (4~seeds, Tier~3 consensus).
149	Between these extremes, individual-seed stochasticity determines whether the consensus threshold is crossed; the data map a boundary region rather than a sharp phase transition.
150	Sensitivity analysis confirms that treatment/null separation is robust to FDR threshold choice ($q{=}0.01$: 0/24 null, 0/24 treatment at $\alpha{=}0.75$; $q{=}0.10$: 0/24 null, 24/24 treatment; Appendix~\ref{app:robustness}).
151	Cross-architecture validation on GPT-2-medium confirms this boundary: at $\alpha{=}0.25$, at most 1/8 pairs reach Confirmatory consensus ($K{\geq}4/5$), consistent with the null regime, despite substantially stronger canary drift (entropy $-32.8\%$ vs.\ Pythia $-4.7{\pm}0.5\%$), while at $\alpha{=}1.0$ all 6 canary$\to$diversity pairs reach $K{\geq}4/5$ (\S\ref{sec:discussion}).
152	Table~\ref{tab:cross_arch_regime} summarizes the regime map across both architectures.
153	At $\alpha{=}0.25$, GPT-2-medium yields 1/8 pairs at Tier~3 ($K{\geq}4/5$) and 7/8 at Tier~2 ($K{\geq}3/5$), consistent with Pythia's 0/8 Tier~3, 0/8 Tier~2 result at the same contamination level, placing both architectures in the null/low-detectability regime.
154	
155	\begin{table}[t]
156	\centering
157	\small
158	\caption{Cross-architecture regime map: lead-lag consensus tier and metric drift at $\alpha{=}0.25$ and $\alpha{=}1.0$. Tier~3: $K{\geq}4/5$ methods; Tier~2: $K{\geq}3/5$. Drift is generation~0$\to$10. GPT-2-medium $\alpha{=}0.25$: single seed (seed=42); Pythia $\alpha{=}0.25$: 3-seed mean${\pm}$std. The onset boundary ($\alpha{\approx}0.25$--$0.50$) is consistent across two transformer decoder-only model families of similar scale.}
159	\label{tab:cross_arch_regime}
160	\begin{tabular}{llcccccc}
161	\toprule
162	$\alpha$ & Model & Entropy & ECE & Distinct-1 & Distinct-2 & Perm.\ Granger & Tier~3 \\
163	\midrule
164	0.25 & Pythia-410M  & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & 0/8 & 0/8 \\
165	0.25 & GPT-2-medium & $-32.8$ & $+422$ & $-23.5$ & $-31.6$ & 0/8 & 1/8 \\
166	\midrule
167	1.00 & Pythia-410M  & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & 6/8 & 6/6 \\
168	1.00 & GPT-2-medium & \multicolumn{6}{c}{(reported in \S\ref{sec:discussion}; all 6 canary$\to$diversity Tier~3)} \\
169	\bottomrule
170	\end{tabular}
171	\end{table}
172	
173	\paragraph{Onset boundary at $\alpha{=}0.50$.}
174	The $\alpha{=}0.50$ regime provides particularly informative evidence.
175	Naive and differenced cross-correlation find 100\% significance while threshold onset finds 0\% (Table~\ref{tab:method_comparison}), and causal methods confirm emerging detectability in a majority of seeds: two of three seeds show directional asymmetry under permutation Granger (6/8 and 3/8 forward, 0/8 reverse), while one seed shows synchronous collapse (0/8).
176	The majority-signal outcome places $\alpha{=}0.50$ in a transitional regime where causal detectability is emerging but not yet robust, bridging the null regime ($\alpha{\leq}0.25$) and the consistently detectable regime ($\alpha{\geq}0.75$).
177	This seed dependence exemplifies our central argument: even within a single regime and method, stochastic variation in training determines whether the consensus threshold is crossed.
178	At this boundary, canary sensitivity is metric-dependent: token entropy fails to reach FDR significance in any seed ($p_{\text{fdr}}{\geq}0.086$), while ECE achieves significance in the two signal-positive seeds (s43, s44), identifying ECE as the more sensitive canary at the onset boundary.
179	Figure~\ref{fig:consensus_heatmap} visualizes this interaction across all method$\times\alpha$ combinations, revealing a clear block structure that separates correlation-based methods from causal methods as a function of regime.
180	
181	
182	\subsection{Case Study: Canary Prediction of Diversity Collapse}
183	\label{sec:case_study}
184	
185	Having established method sensitivity (Claim~3) and regime dependence (Claim~2), we present the conditions under which canary prediction succeeds (Claim~1).
186	We scope this claim precisely: canary metrics predict \emph{diversity collapse} (declining distinct-$n$), not model collapse broadly.
187	
188	\paragraph{Full synthetic replacement ($\alpha{=}1.0$, 4 seeds).}
189	Token entropy exhibits robust Granger-precedence over diversity collapse metrics, confirmed by 4 independent statistical methods (permutation Granger power${=}1.0$), 4 seeds, and cross-architecture replication on GPT-2-medium (Tier~3 consensus; \S\ref{sec:discussion}).
190	Cross-correlation peaks at lag$={+}1$ with $|r|{>}0.99$ (cross-seed standard deviation: 0.0), establishing a consistent one-generation lead.
191	Figure~\ref{fig:metric_trajectory} illustrates the one-generation offset between token entropy decline and distinct-1 decline, visible across all four seeds.
192	Permutation Granger tests (first-differenced) confirm all canary$\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\ref{app:distinct3}).
193	Reverse-direction tests (downstream$\to$canary) find \textbf{0/24} FDR-significant (all $p{>}0.49$), establishing complete directional asymmetry.
194	
195	\begin{figure}[t]
196	\centering
197	\includegraphics[width=\linewidth]{figures/metric_trajectory.pdf}
198	\caption{Metric trajectories across 10 generations at $\alpha{=}1.0$ (Pythia-410M, 4~seeds shown as individual traces). Token entropy (top, blue) drops sharply at generation~1, while distinct-1 (bottom, red) begins declining at generations~2--3, establishing a visible one-generation canary lead. The consistent lag across all four seeds confirms that the temporal offset is robust rather than seed-specific. Shaded bands show the inter-seed range. This visual pattern corresponds to the statistical finding of 24/24 forward-direction and 0/24 reverse-direction FDR-significant pairs.}
199	\label{fig:metric_trajectory}
200	\end{figure}
201	
202	\paragraph{High contamination ($\alpha{=}0.75$, 3 seeds).}
203	Directional asymmetry is robustly confirmed across three independent seeds (permutation Granger: 19/24 forward pairs FDR-significant, 0/24 reverse).
204	However, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds 42, 43, 44), placing $\alpha{=}0.75$ squarely in the transitional detection regime.
205	Differenced cross-correlation finds 8/8 pairs significant in \emph{both} forward and reverse directions at each seed, confirming that this method alone cannot distinguish genuine directional precedence from shared dynamics, a seed-level demonstration of Pitfall~1 (\S\ref{sec:pitfalls}).
206	
207	\paragraph{ECE as a conditional secondary canary.}
208	ECE performs equivalently to token entropy across four of five methods (naive, differenced, threshold, permutation Granger).
209	Its classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootstrap power analysis yields estimated power of 0.05--0.20 depending on $d_{\max}$.
210	Resolving ECE's true canary status requires longer time series.
211	
212	\paragraph{Failed canary candidates.}
213	Not all metrics serve as canaries.
214	Effective rank and Self-BLEU show no detectable lead-lag relationship with any downstream metric under any method or contamination level, and are excluded from the consensus framework.
215	Effective rank behavior is model-dependent in an unexpected way: in Pythia-410M, effective rank decreases during collapse (representational contraction), whereas in GPT-2-medium at $\alpha{=}0.25$ it \emph{increases} from 2.37 to 8.48 (+258\%).
216	The GPT-2-medium starting effective rank is near rank-2, suggesting the model's initial representation is already highly concentrated; iterative training disperses it rather than concentrating it further.
217	This opposite directionality across architectures precludes effective rank as a universal canary and motivates architecture-specific analysis (\S\ref{sec:discussion}).
218	
219	\paragraph{Consensus filtering.}
220	Of 16 canary$\to$downstream pairs tested at $\alpha{=}1.0$ (4 candidate canaries $\times$ 4 downstream metrics), \textbf{6 survive} the full consensus pipeline ($K{\geq}4/5$ methods, $S{\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\ref{app:distinct3} bring the total to~6).
221	The 10 eliminated pairs comprise all canary$\to$perplexity relationships (identified as spurious by the first-differencing diagnostic) and all effective-rank and Self-BLEU pairs (failed canaries).
222	The consensus framework reduces the naive 100\% significance rate to the 37.5\% rate supported by the most conservative individual methods (Figure~\ref{fig:consensus_workflow}).
223	
224	
225	\subsection{Consensus Framework Validation}
226	\label{sec:consensus_validation}
227	
228	We validate the consensus framework's calibration using built-in experimental controls.
229	
230	\paragraph{False positive rate.}
231	At $\alpha{=}0.0$ (three seeds, 24 total pairs), no synthetic data is injected; any detected lead-lag association is a false positive.
232	Individual-method FPR ranges from \textbf{100\%} (naive cross-correlation) through 37.5\% (differenced) and 20.8\% (threshold) down to \textbf{0\%} (permutation Granger: 0/24 across all three seeds).
233	The consensus framework at $K{\geq}4/5$ achieves \textbf{FPR${=}$0\%} (0/24 pairs, three independent seeds), matching the best individual methods while providing robustness against miscalibration of any single method (Table~\ref{tab:fpr_fnr}).
234	
235	\paragraph{False negative rate.}
236	At $\alpha{=}1.0$, we define 6 effect-size reference pairs (token entropy and ECE $\to$ distinct-1/2/3) using criteria independent of the consensus methods: drift ratio ${\geq}3\times$ the $\alpha{=}0.0$ baseline (entropy $11.93\times$, ECE $73.12\times$) and canary onset strictly preceding downstream onset by ${\geq}1$ generation (\S\ref{sec:calibration}).
237	FNR is calibrated on a 4-method panel (excluding differenced cross-correlation to avoid circularity): at $K{\geq}3/4$, $S{\geq}3/4$, all~6 are recovered (\textbf{FNR${=}$0\%}).
238	Toda--Yamamoto alone yields FNR${=}$33.3\% (2/6), missing ECE$\to$distinct-2 and ECE$\to$distinct-3 due to Type~II errors at $T{=}10$.
239	Both FPR and FNR are validated on the joint method${\times}$seed dimension (FPR: 3~seeds at $\alpha{=}0.0$; FNR: 4~seeds at $\alpha{=}1.0$), with cross-seed FPR variance negligible (all three seeds yield 0/8 robust pairs at $K{\geq}4/5$).
240	Table~\ref{tab:fpr_fnr} reports the calibration results.
241	Table~\ref{tab:single-method-errors} complements this analysis by showing the practical consequences of relying on any single method: naive cross-correlation produces false positives at every $\alpha$ including the null control, Toda--Yamamoto misses true signals at $\alpha{=}0.75$, while the consensus at $K{\geq}3$ yields the correct verdict across all five contamination levels.
242	
243	\begin{table}[t]
244	\centering
245	\caption{Single-method inference errors across contamination levels.
246	Each cell shows the verdict (significant or not) based on multi-seed majority ($\geq$2/3 seeds with $\geq$4/8 pairs significant).
247	\checkmark\ = correct, \textcolor{red}{FP} = false positive, \textcolor{blue}{FN} = false negative, $\circ$ = ambiguous ground truth (either verdict plausible).
248	Naive XCorr produces false positives at \emph{every} $\alpha$ including the null control, while TY Granger misses true signals at $\alpha{=}0.75$.
249	Only the multi-method consensus ($K{\geq}3$) yields the correct verdict at all five contamination levels.}
250	\label{tab:single-method-errors}
251	\resizebox{\columnwidth}{!}{%
252	\begin{tabular}{lccccc}
253	\toprule
254	 & \multicolumn{2}{c}{\textit{No signal}} & \textit{Ambiguous} & \multicolumn{2}{c}{\textit{Causal signal}} \\
255	\cmidrule(lr){2-3} \cmidrule(lr){4-4} \cmidrule(lr){5-6}
256	Method & $\alpha{=}0.00$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.00$ \\
257	\midrule
258	Naive XCorr
259	  & \textcolor{red}{FP}{\scriptsize\ 8,7,8}
260	  & \textcolor{red}{FP}{\scriptsize\ 8,8}
261	  & $\circ${\scriptsize\ 8,8,8}
262	  & \checkmark{\scriptsize\ 8,8,8}
263	  & \checkmark{\scriptsize\ 8,8,8} \\
264	Diff XCorr (FDR)
265	  & \checkmark{\scriptsize\ 4,3,3}
266	  & \checkmark{\scriptsize\ 3,1}
267	  & $\circ${\scriptsize\ 8,6,6}
268	  & \checkmark{\scriptsize\ 8,8,8}
269	  & \checkmark{\scriptsize\ 8,8,8} \\
270	Threshold Onset
271	  & \checkmark{\scriptsize\ 3,1,1}
272	  & \checkmark{\scriptsize\ 0,0}
273	  & $\circ${\scriptsize\ 0,0,0}
274	  & \checkmark{\scriptsize\ 4,0,4}
275	  & \checkmark{\scriptsize\ 8,8,8} \\
276	Perm Granger (FDR)
277	  & \checkmark{\scriptsize\ 0,0,0}
278	  & \checkmark{\scriptsize\ 0,0}
279	  & $\circ${\scriptsize\ 0,6,3}
280	  & \checkmark{\scriptsize\ 8,5,6}
281	  & \checkmark{\scriptsize\ 6,6,6} \\
282	TY Granger
283	  & \checkmark{\scriptsize\ 1,1,0}
284	  & \checkmark{\scriptsize\ 0,2}
285	  & $\circ${\scriptsize\ 0,0,0}
286	  & \textcolor{blue}{FN}{\scriptsize\ 1,1,1}
287	  & \checkmark{\scriptsize\ 6,6,4} \\
288	\midrule
289	\textbf{Consensus ($K{\geq}3$)}
290	  & \checkmark
291	  & \checkmark
292	  & $\circ$
293	  & \checkmark
294	  & \checkmark \\
295	\bottomrule
296	\multicolumn{6}{l}{\footnotesize Subscript numbers: per-seed significant pair counts out of 8.} \\
297	\multicolumn{6}{l}{\footnotesize Seeds: $\alpha{=}0.00/0.50/0.75$: 42, 43, 44; $\alpha{=}0.25$: 43, 44; $\alpha{=}1.00$: 42, 43, 45.} \\
298	\end{tabular}%
299	}
300	\end{table}
301	
302	\paragraph{Bootstrap power analysis.}
303	To quantify detection power beyond binary FNR, we perform bootstrap power analysis ($B{=}1{,}000$ resamples from 4-seed data at $\alpha{=}1.0$).
304	Permutation Granger achieves power${=}1.0$ on genuine pairs (canary$\to$diversity) and power${=}0.0$ on spurious pairs (canary$\to$perplexity), providing clean separation.
305	Toda--Yamamoto achieves power${=}0.05$--$0.20$ on genuine pairs (depending on $d_{\max}$), confirming its poor sensitivity at $T{=}10$.
306	We note that bootstrap power${=}1.0$ reflects the effect size in our 4-seed data and should not be interpreted as a universal power guarantee; furthermore, the two methods use different data-generating processes for calibration (permutation Granger resamples observed $\alpha{=}1.0$ trajectories, while Toda--Yamamoto power was estimated under a generic VAR(2) simulation with $\beta{=}0.3$).
307	
308	\begin{table}[t]
309	\centering
310	\small
311	\caption{False positive and false negative rates for individual methods and the consensus framework (Pythia-410M). The consensus threshold $K{\geq}4/5$ achieves FPR${=}$0\% and FNR${=}$0\%, matching the best individual method (permutation Granger) while providing robustness against miscalibration. FPR: $\alpha{=}0.0$ null control (three seeds, $M{=}5$ methods); values are 3-seed means with ranges in parentheses where cross-seed variance is non-negligible. FNR: $\alpha{=}1.0$ against 6 effect-size reference pairs (4-method panel excluding differenced cross-correlation, 4~seeds).}
312	\label{tab:fpr_fnr}
313	\begin{tabular}{lcc}
314	\toprule
315	Criterion & FPR ($\alpha{=}0.0$) & FNR ($\alpha{=}1.0$) \\
316	\midrule
317	Naive XCorr              & 100\%              & 0\%  \\
318	Differenced XCorr        & 37.5\%             & 0\%  \\
319	Threshold Onset          & 20.8\% (12.5--37.5) & 0\%  \\
320	Permutation Granger      & 0\%                & 0\%  \\
321	Toda--Yamamoto           & 4.2\% (0--12.5)    & 33.3\% \\
322	\midrule
323	Consensus ($K{\geq}4/5$)              & 0\%    & 0\%  \\
324	Consensus ($K{\geq}4/5$, $S{\geq}3/4$) & 0\%    & 0\%  \\
325	\bottomrule
326	\end{tabular}
327	\end{table}
328	
329	
330	\subsection{Cross-Architecture, Cross-Scale, and Cross-Domain Generalization}
331	\label{sec:generalization}
332	
333	The methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).
334	To test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).
335	All conditions use $\alpha{=}1.0$ and a single seed.
336	
337	\begin{table}[t]
338	\centering
339	\small
340	\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\alpha{=}1.0$, single seed per condition). Each cell reports the fraction of canary$\to$downstream pairs reaching BH-corrected FDR significance ($q{=}0.05$): 8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded). \textbf{[TBD]}: experiments in progress.}
341	\label{tab:generalization}
342	\begin{tabular}{llccccccc}
343	\toprule
344	Variation & Model / Dataset & \rotatebox{70}{Naive} & \rotatebox{70}{Diff.\ XCorr} & \rotatebox{70}{Threshold} & \rotatebox{70}{PermG (fwd)} & \rotatebox{70}{PermG (rev)} & \rotatebox{70}{TY} & \rotatebox{70}{$K{\geq}4/5$} \\
345	\midrule
346	Baseline      & Pythia-410M / Wiki    & 7/8 & 6/8 & 6/8 & 6/8 & 0/8 & 6/8 & 6/8 \\
347	Architecture  & GPT-2-medium / Wiki   & 6/6 & 6/6 & 6/6 & 6/6 & 0/6 & 0/6 & 6/6 \\
348	Architecture  & OPT-1.3B / Wiki       & 6/8 & 6/8 & 8/8 & 6/8 & 0/8 & 2/8 & 6/8 \\
349	Scale ($3.4\times$) & Pythia-1.4B / Wiki & \multicolumn{7}{c}{\textbf{[TBD]}} \\
350	Domain        & Pythia-1B / C4        & \multicolumn{7}{c}{\textbf{[TBD]}} \\
351	\bottomrule
352	\end{tabular}
353	\end{table}
354	
355	\paragraph{Architecture generalization.}
356	Table~\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.
357	All models reach Tier~3 consensus ($K{\geq}4/5$) with 6/8 (or 6/6) canary$\to$diversity pairs confirmed.
358	Permutation Granger directionality is perfect across architectures: all forward-direction pairs are FDR-significant while 0 reverse-direction pairs reach significance in any architecture.
359	
360	Method-level variation across architectures is informative.
361	Threshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\to$1 discontinuity that cleanly exceeds the onset threshold.
362	Toda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\S\ref{sec:consensus_validation}).
363	Despite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\geq}4/5$.
364	
365	% [PLACEHOLDER — activate when Pythia-1.4B and Pythia-1B/C4 results arrive]
366	% \paragraph{Scale and domain generalization.}
367	% Scaling from 410M to 1.4B parameters within the Pythia family (3.4$\times$)
368	% preserves the core pattern: permutation Granger identifies \textbf{XX}/8
369	% forward-direction pairs with 0/8 reverse, and consensus $K{\geq}4/5$
370	% yields \textbf{XX}/8 (Table~\ref{tab:generalization}).
371	% This confirms that the methodological pitfalls are not artifacts of
372	% small-model capacity limitations, since the same consensus threshold
373	% operates identically at 3.4$\times$ the parameter count.
374	%
375	% Replacing WikiText-103 with C4 tests whether the lead-lag pattern
376	% depends on the training data distribution. Pythia-1B on C4 yields
377	% \textbf{XX}/8 forward-direction permutation Granger pairs with
378	% \textbf{XX}/8 reverse, and consensus $K{\geq}4/5$ at \textbf{XX}/8.
379	% Together with the architecture results, this establishes five
380	% independent validation lines (three architectures, one scale, one
381	% domain) converging on the same conclusion: token entropy
382	% Granger-precedes diversity collapse at $\alpha{=}1.0$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d57549f-b14b-49fd-a659-e07123890b4e",
  "isSidechain": false,
  "promptId": "e0dec198-abf3-497e-80c7-3f5c472bf9b3",
  "type": "user",
  "uuid": "a0bed052-5535-4b7c-871f-9295e9b8f346",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \\cite{biderman2023pythia}, a 410M-parameter decoder-only language model.\nPythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.\nCross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \\S\\ref{sec:method_sensitivity}, \\S\\ref{sec:regime}, and \\S\\ref{sec:discussion}.\nTraining data is drawn from WikiText-103 \\cite{merity2017pointer}, using 5{,}000-sample subsets per generation.\n\nOur protocol follows the replace paradigm of \\citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\\alpha{<}1.0$.\nEach generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\\alpha$ fraction synthetic data and $(1{-}\\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.\nWe run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\\alpha \\in \\{0.00, 0.25, 0.50, 0.75, 1.00\\}$.\nThe $\\alpha{=}1.0$ condition uses four random seeds $\\{42, 43, 44, 45\\}$; $\\alpha{=}0.00$, $\\alpha{=}0.25$, and $\\alpha{=}0.75$ each use three seeds $\\{42, 43, 44\\}$; $\\alpha{=}0.50$ uses three seeds $\\{42, 43, 44\\}$.\n\nWe track two \\emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \\cite{scheffer2009early}) and three \\emph{downstream metrics}.\nCanary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).\nDownstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \\cite{li2016diversity}, computed over all 5{,}000 generated samples per generation) and perplexity (evaluated on held-out real data).\nToken entropy is the mean next-token prediction entropy $H(p_\\theta | \\text{context})$ averaged over 1{,}000 held-out samples; ECE uses 15 equal-width bins.\nWe additionally evaluate effective rank and Self-BLEU as candidate canaries (\\S\\ref{sec:case_study}).\nResults for distinct-3 are reported in Appendix~\\ref{app:distinct3}.\nCode and data will be released upon publication.\n\nAll hypothesis tests apply Benjamini--Hochberg (BH) FDR correction at $q{=}0.05$.\nPermutation Granger causality tests use 5{,}000 permutations on first-differenced series \\cite{shojaie2022granger}.\nCross-correlation analysis uses a maximum lag of 5 generations.\nTable~\\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all five contamination levels.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Metric drift (\\%, generation~0$\\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\\alpha$ levels, with the strongest decline at moderate contamination ($\\alpha{=}0.25$: distinct-1 $-40.3{\\pm}0.3\\%$) rather than full replacement ($\\alpha{=}1.0$: $-27.8{\\pm}1.6\\%$). $\\alpha{=}0.00$, $\\alpha{=}0.25$, $\\alpha{=}0.50$, $\\alpha{=}0.75$: 3-seed mean${\\pm}$std (seeds 42, 43, 44); $\\alpha{=}1.0$: 4-seed mean${\\pm}$std (seeds 42, 43, 44, 45).}\n\\label{tab:drift_summary}\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\\\\n\\midrule\n0.00 & $-4.6{\\pm}0.4$ & $+37.6{\\pm}14$ & $-14.1{\\pm}0.4$ & $-9.6{\\pm}0.4$ & $-20.6{\\pm}1.0$ \\\\\n0.25 & $-4.7{\\pm}0.5$ & $+81.8{\\pm}15.9$ & $-40.3{\\pm}0.3$ & $-56.4{\\pm}0.7$ & $-18.1{\\pm}0.8$ \\\\\n0.50 & $-18.0{\\pm}0.5$ & $+822.6{\\pm}18.3$ & $-37.1{\\pm}0.4$ & $-50.4{\\pm}1.0$ & $+21.0{\\pm}0.1$ \\\\\n0.75 & $-27.6{\\pm}0.2$ & $+1791{\\pm}18$ & $-32.3{\\pm}0.5$ & $-41.0{\\pm}1.0$ & $+182.6{\\pm}0.7$ \\\\\n1.00 & $-60.8{\\pm}1.2$ & $+3780{\\pm}30$ & $-27.8{\\pm}1.6$ & $-34.0{\\pm}3.3$ & $+3674{\\pm}45$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Method Sensitivity Analysis}\n\\label{sec:method_sensitivity}\n\nWe open with Claim~3 (method sensitivity) because it conditions the interpretation of all subsequent results.\nIf different statistical methods yield contradictory conclusions on the same data, any single-method analysis is unreliable by construction.\n\n\\paragraph{Five-method ablation.}\nWe apply five lead-lag detection methods to the $\\alpha{=}1.0$ condition (4~seeds, 16 canary$\\to$downstream pairs).\nThe fraction of pairs reaching BH-corrected FDR significance varies dramatically by method: naive cross-correlation \\textbf{16/16} (100\\%), differenced cross-correlation \\textbf{14/16} (87.5\\%), threshold onset detection \\textbf{9/16} (56.3\\%), permutation Granger causality \\textbf{6/16} (37.5\\%), and Toda--Yamamoto Granger \\textbf{4/16} (25.0\\%).\nMethod choice alone swings significance from \\textbf{100\\% to 25\\%}: 50--57\\% of pairs classified as significant under one method flip to non-significant under another.\nThe spurious-signal rate (the fraction of pairs detected by the most liberal method but not confirmed by the most conservative) is \\textbf{75\\%} across all five methods and \\textbf{62.5\\%} when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate (\\S\\ref{sec:consensus_validation}).\nTable~\\ref{tab:method_comparison} reports significance rates restricted to 8 validated canary$\\to$downstream pairs (excluding failed candidates); the 16-pair rates above include effective rank and Self-BLEU to capture the full method-sensitivity landscape.\n\n\\paragraph{First-differencing diagnostic.}\nA single preprocessing decision can eliminate an entire analysis channel.\nFor canary$\\to$diversity pairs at $\\alpha{=}1.0$, all pairs retain unanimous FDR significance after first-differencing (24/24$\\to$24/24), confirming genuine temporal precedence rather than shared-trend confounding.\nFor canary$\\to$perplexity, however, undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find \\textbf{zero} significant pairs ($F{\\approx}0$, $p{=}0.99$; Figure~\\ref{fig:differencing_dmax}a).\nThe apparent canary$\\to$perplexity relationship is entirely an artifact of co-trending.\nNotably, at $\\alpha{=}0.75$, differenced cross-correlation finds 8/8 pairs significant in \\emph{both} forward and reverse directions per seed, demonstrating that this method alone cannot distinguish genuine directional precedence from shared dynamics even after detrending.\n\n\\paragraph{Augmentation order sensitivity.}\nToda--Yamamoto Granger tests show extreme sensitivity to the augmentation order $d_{\\max}$ (Figure~\\ref{fig:differencing_dmax}b).\nAt $d_{\\max}{=}0$ (most permissive), approximately 6\\% of pairs are rejected; at adaptive $d_{\\max}$ determined by ADF unit-root tests, 75\\%; at $d_{\\max}{=}1$ (most conservative), \\textbf{94\\%}.\nThis single hyperparameter swings conclusions from near-universal significance to near-universal non-significance.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/differencing_dmax.pdf}\n\\caption{First-differencing diagnostic and augmentation order sensitivity (Pythia-410M, $\\alpha{=}1.0$, 4~seeds). \\textbf{(a)}~First-differencing eliminates the canary$\\to$perplexity channel: undifferenced tests find near-universal significance ($F{=}16$--$36$) while differenced tests find zero significant pairs ($F{\\approx}0$, $p{=}0.99$), exposing these associations as shared-trend artifacts. Canary$\\to$diversity pairs retain significance after differencing (24/24$\\to$24/24). \\textbf{(b)}~Toda--Yamamoto Granger significance rates vary dramatically with augmentation order $d_{\\max}$: from $\\sim$6\\% rejection at $d_{\\max}{=}0$ to 94\\% at $d_{\\max}{=}1$, demonstrating that this single hyperparameter can reverse conclusions about temporal precedence.}\n\\label{fig:differencing_dmax}\n\\end{figure}\n\n\\paragraph{Inter-method agreement.}\nCohen's $\\kappa$, averaged over all method pairs, is \\textbf{0.185} (near chance; poor agreement); this value is consistent across contamination levels ($\\alpha{=}0.0$ through $\\alpha{=}1.0$), indicating that method disagreement is a structural property of the analysis rather than a regime-specific artifact.\nCross-architecture validation on GPT-2-medium (12 canary$\\to$downstream pairs) yields Fleiss' $\\kappa{=}0.091$, also in the ``slight agreement'' range, confirming that low inter-method agreement is not architecture-specific.\nRestricting to three informative methods (excluding naive cross-correlation and Toda--Yamamoto, which anchor the permissive and conservative extremes respectively) raises $\\kappa$ to 0.667 (substantial agreement), indicating that the low full-panel $\\kappa$ is driven by the deliberate inclusion of methods spanning the entire permissive-to-conservative spectrum rather than by fundamental incoherence among methods.\nTable~\\ref{tab:method_comparison} extends the analysis across contamination levels.\nAt $\\alpha{=}0.0$ (no synthetic data, serving as null control), naive cross-correlation finds \\textbf{100\\%} of pairs significant, a textbook spurious-regression outcome in trending time series.\nPermutation Granger correctly finds 0\\% across all three null-control seeds; Toda--Yamamoto finds 0--12.5\\% (1/24 total, attributable to a degenerate $\\text{df}_{\\text{resid}}{=}1$ case; \\S\\ref{sec:consensus_validation}).\nAt $\\alpha{=}0.50$, naive and differenced cross-correlation both find 100\\% significance while threshold onset and all causal methods find 0\\% (Figure~\\ref{fig:consensus_heatmap}), illustrating that even among non-causal methods, sensitivity diverges sharply at this boundary.\n\n\\paragraph{Method$\\times$regime interaction.}\nTable~\\ref{tab:method_comparison} reveals that the correlation-versus-causal divergence is not uniform across contamination levels.\nAt $\\alpha{=}0.25$, differenced cross-correlation drops to 25\\% and threshold onset to 0\\%, while naive cross-correlation remains at 100\\%, demonstrating that even partial detrending removes marginal associations at low contamination.\nIn the lowest-contamination regime ($\\alpha{\\leq}0.25$, three seeds), the false confirmation rate for the most liberal method approaches 100\\%, while all Granger-type tests correctly find 0\\%, a regime where single-method analysis is maximally dangerous.\nThe graded response across methods, combined with the block structure visible in Figure~\\ref{fig:consensus_heatmap}, motivates the regime-dependent analysis in \\S\\ref{sec:regime}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/consensus_heatmap.pdf}\n\\caption{Method$\\times$regime consensus heatmap (Pythia-410M). Each cell shows the consensus tier ($K$-of-$M$ agreement) for a given lead-lag method (rows) and contamination level $\\alpha$ (columns). A clear block structure emerges: correlation-based methods (naive, differenced, threshold) find significance across all $\\alpha$ levels, while Granger-type methods find significance only at $\\alpha{\\geq}0.75$. The $\\alpha{=}0.50$ column is maximally dangerous (high correlation coexists with zero causal precedence), illustrating Pitfall~3 (regime dependence). Color scale: dark = significant (Tier~3), light = non-significant (Tier~1).}\n\\label{fig:consensus_heatmap}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{FDR significance rates (\\%) for five lead-lag methods across contamination levels (Pythia-410M). Method choice swings significance from 100\\% (naive cross-correlation) to 0\\% (permutation Granger) at $\\alpha{\\leq}0.25$, with seed-dependent onset at $\\alpha{=}0.50$, demonstrating that single-method conclusions are unreliable. Each cell reports the fraction of 8 canary$\\to$downstream pairs (token entropy and ECE $\\times$ 4 downstream metrics) reaching BH-corrected significance ($q{=}0.05$), excluding failed candidates (\\S\\ref{sec:case_study}). Seed coverage: $\\alpha{=}1.0$: 4 seeds (32 pairs); $\\alpha{=}0.00$, $\\alpha{=}0.75$: 3 seeds (24 pairs); $\\alpha{=}0.25$ Toda--Yamamoto: 3 seeds (24 pairs), other methods single seed; $\\alpha{=}0.50$: 3~seeds for permutation Granger (range shown), single seed for other methods. $^\\dagger$Seed-dependent onset: s42${=}$0/8, s43${=}$6/8, s44${=}$3/8 (median 3/8).}\n\\label{tab:method_comparison}\n\\begin{tabular}{lcccccc}\n\\toprule\nMethod & $\\alpha{=}0.0$ & $\\alpha{=}0.25$ & $\\alpha{=}0.50$ & $\\alpha{=}0.75$ & $\\alpha{=}1.0$ & FPR$_\\text{null}$ \\\\\n\\midrule\nNaive XCorr     & 100   & 100  & 100  & 100   & 100   & 100  \\\\\nDiff.\\ XCorr   & 37.5  & 25   & 100  & 100   & 100   & 37.5 \\\\\nThreshold       & 20.8  & 0    & 0    & 33.3  & 100   & 20.8 \\\\\nPerm.\\ Granger  & 0     & 0    & 0--75$^\\dagger$  & 79.2  & 75    & 0    \\\\\nToda--Yamamoto  & 0     & 12.5 & 0    & 12.5  & 59.4  & 0    \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Regime-Dependent Detectability}\n\\label{sec:regime}\n\nBeyond method choice, the contamination level~$\\alpha$ determines whether a temporal lead exists to detect.\nWe present regime effects at two levels: raw metric drift (method-independent) and Granger-precedence detectability.\n\n\\paragraph{Raw drift.}\nTable~\\ref{tab:drift_summary} shows that diversity collapse occurs at \\emph{all} contamination levels, not only under full synthetic replacement.\nDistinct-1 declines by 13.8\\% even at $\\alpha{=}0.0$ (attributable to fine-tuning on repeated real-data subsets), and more steeply at intermediate contamination: $-40.3{\\pm}0.3\\%$ ($\\alpha{=}0.25$), $-37.1{\\pm}0.4\\%$ ($\\alpha{=}0.50$), $-32.3{\\pm}0.5\\%$ ($\\alpha{=}0.75$), and $-27.8{\\pm}1.6\\%$ ($\\alpha{=}1.0$).\nThe non-monotonic pattern (diversity declining \\emph{more} at moderate~$\\alpha$ than at extreme~$\\alpha$) is confirmed by 3-seed replication at $\\alpha{=}0.25$ (std${=}0.3\\%$), indicating that this relationship between contamination level and collapse severity is robust rather than a seed-specific artifact.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/regime_map.pdf}\n\\caption{Detectability regime map across contamination levels (Pythia-410M). Permutation Granger FDR significance rate (solid line) and consensus tier (shaded regions) as a function of $\\alpha$. The onset boundary lies at $\\alpha{\\approx}0.25$--$0.50$: at $\\alpha{\\leq}0.25$, all seeds agree on null (0/24); at $\\alpha{=}0.50$, detectability is seed-dependent (0/8--6/8, 3~seeds, median 3/8); at $\\alpha{=}0.75$, directional asymmetry emerges robustly (19/24 forward, 0/24 reverse, 3~seeds) but method consensus remains transitional (Tier~2--3); at $\\alpha{=}1.0$, full Confirmatory consensus is achieved (24/24 forward, Tier~3, 4~seeds). Multi-seed replication: $\\alpha{=}0.00$, $\\alpha{=}0.25$, $\\alpha{=}0.50$, $\\alpha{=}0.75$: 3~seeds; $\\alpha{=}1.0$: 4~seeds.}\n\\label{fig:regime_map}\n\\end{figure}\n\n\\paragraph{Granger-precedence detectability.}\nDespite ubiquitous drift, causal detectability is sharply regime-dependent (Figure~\\ref{fig:regime_map}).\nPermutation Granger tests (first-differenced, BH-corrected) find 0/24 pairs FDR-significant at $\\alpha{=}0.00$ (3~seeds), 0/24 at $\\alpha{=}0.25$ (3~seeds), 0/8--6/8 at $\\alpha{=}0.50$ (seed-dependent; 3~seeds, median 3/8), and \\textbf{6/8} at $\\alpha{=}1.0$.\nAt $\\alpha{=}0.75$ (3~seeds), permutation Granger finds 19/24 forward-direction pairs FDR-significant with 0/24 reverse, confirming directional asymmetry; however, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds), placing this regime in a transitional detection state.\nUnder Bonferroni correction, approximately 3/8 pairs per seed survive, consistent with the transitional nature of the $\\alpha{=}0.75$ boundary where marginal signals are sensitive to correction stringency.\nWithin-$\\alpha$ multi-seed analysis at $\\alpha{=}1.0$ yields \\textbf{24/24} canary$\\to$diversity pairs FDR-significant across all four seeds, with 0/24 in the reverse direction, confirming temporal asymmetry.\nThe resulting dose-response pattern is monotonic: causal detectability is absent below $\\alpha{=}0.25$, seed-dependent at $\\alpha{=}0.50$, and robust above $\\alpha{=}0.75$ (Figure~\\ref{fig:regime_map}).\nThe onset boundary lies at $\\alpha{\\approx}0.25$--$0.50$, consistent with theoretical expectations about signal-to-noise limits in short time series~\\cite{boettiger2012limits}.\nAt the extremes, the transition is unambiguous: 0/24 FDR-significant pairs at $\\alpha{\\leq}0.25$ (3~seeds) versus 24/24 at $\\alpha{=}1.0$ (4~seeds, Tier~3 consensus).\nBetween these extremes, individual-seed stochasticity determines whether the consensus threshold is crossed; the data map a boundary region rather than a sharp phase transition.\nSensitivity analysis confirms that treatment/null separation is robust to FDR threshold choice ($q{=}0.01$: 0/24 null, 0/24 treatment at $\\alpha{=}0.75$; $q{=}0.10$: 0/24 null, 24/24 treatment; Appendix~\\ref{app:robustness}).\nCross-architecture validation on GPT-2-medium confirms this boundary: at $\\alpha{=}0.25$, at most 1/8 pairs reach Confirmatory consensus ($K{\\geq}4/5$), consistent with the null regime, despite substantially stronger canary drift (entropy $-32.8\\%$ vs.\\ Pythia $-4.7{\\pm}0.5\\%$), while at $\\alpha{=}1.0$ all 6 canary$\\to$diversity pairs reach $K{\\geq}4/5$ (\\S\\ref{sec:discussion}).\nTable~\\ref{tab:cross_arch_regime} summarizes the regime map across both architectures.\nAt $\\alpha{=}0.25$, GPT-2-medium yields 1/8 pairs at Tier~3 ($K{\\geq}4/5$) and 7/8 at Tier~2 ($K{\\geq}3/5$), consistent with Pythia's 0/8 Tier~3, 0/8 Tier~2 result at the same contamination level, placing both architectures in the null/low-detectability regime.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture regime map: lead-lag consensus tier and metric drift at $\\alpha{=}0.25$ and $\\alpha{=}1.0$. Tier~3: $K{\\geq}4/5$ methods; Tier~2: $K{\\geq}3/5$. Drift is generation~0$\\to$10. GPT-2-medium $\\alpha{=}0.25$: single seed (seed=42); Pythia $\\alpha{=}0.25$: 3-seed mean${\\pm}$std. The onset boundary ($\\alpha{\\approx}0.25$--$0.50$) is consistent across two transformer decoder-only model families of similar scale.}\n\\label{tab:cross_arch_regime}\n\\begin{tabular}{llcccccc}\n\\toprule\n$\\alpha$ & Model & Entropy & ECE & Distinct-1 & Distinct-2 & Perm.\\ Granger & Tier~3 \\\\\n\\midrule\n0.25 & Pythia-410M  & $-4.7{\\pm}0.5$ & $+81.8{\\pm}15.9$ & $-40.3{\\pm}0.3$ & $-56.4{\\pm}0.7$ & 0/8 & 0/8 \\\\\n0.25 & GPT-2-medium & $-32.8$ & $+422$ & $-23.5$ & $-31.6$ & 0/8 & 1/8 \\\\\n\\midrule\n1.00 & Pythia-410M  & $-60.8{\\pm}1.2$ & $+3780{\\pm}30$ & $-27.8{\\pm}1.6$ & $-34.0{\\pm}3.3$ & 6/8 & 6/6 \\\\\n1.00 & GPT-2-medium & \\multicolumn{6}{c}{(reported in \\S\\ref{sec:discussion}; all 6 canary$\\to$diversity Tier~3)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Onset boundary at $\\alpha{=}0.50$.}\nThe $\\alpha{=}0.50$ regime provides particularly informative evidence.\nNaive and differenced cross-correlation find 100\\% significance while threshold onset finds 0\\% (Table~\\ref{tab:method_comparison}), and causal methods confirm emerging detectability in a majority of seeds: two of three seeds show directional asymmetry under permutation Granger (6/8 and 3/8 forward, 0/8 reverse), while one seed shows synchronous collapse (0/8).\nThe majority-signal outcome places $\\alpha{=}0.50$ in a transitional regime where causal detectability is emerging but not yet robust, bridging the null regime ($\\alpha{\\leq}0.25$) and the consistently detectable regime ($\\alpha{\\geq}0.75$).\nThis seed dependence exemplifies our central argument: even within a single regime and method, stochastic variation in training determines whether the consensus threshold is crossed.\nAt this boundary, canary sensitivity is metric-dependent: token entropy fails to reach FDR significance in any seed ($p_{\\text{fdr}}{\\geq}0.086$), while ECE achieves significance in the two signal-positive seeds (s43, s44), identifying ECE as the more sensitive canary at the onset boundary.\nFigure~\\ref{fig:consensus_heatmap} visualizes this interaction across all method$\\times\\alpha$ combinations, revealing a clear block structure that separates correlation-based methods from causal methods as a function of regime.\n\n\n\\subsection{Case Study: Canary Prediction of Diversity Collapse}\n\\label{sec:case_study}\n\nHaving established method sensitivity (Claim~3) and regime dependence (Claim~2), we present the conditions under which canary prediction succeeds (Claim~1).\nWe scope this claim precisely: canary metrics predict \\emph{diversity collapse} (declining distinct-$n$), not model collapse broadly.\n\n\\paragraph{Full synthetic replacement ($\\alpha{=}1.0$, 4 seeds).}\nToken entropy exhibits robust Granger-precedence over diversity collapse metrics, confirmed by 4 independent statistical methods (permutation Granger power${=}1.0$), 4 seeds, and cross-architecture replication on GPT-2-medium (Tier~3 consensus; \\S\\ref{sec:discussion}).\nCross-correlation peaks at lag$={+}1$ with $|r|{>}0.99$ (cross-seed standard deviation: 0.0), establishing a consistent one-generation lead.\nFigure~\\ref{fig:metric_trajectory} illustrates the one-generation offset between token entropy decline and distinct-1 decline, visible across all four seeds.\nPermutation Granger tests (first-differenced) confirm all canary$\\to$diversity pairs as FDR-significant across all four seeds, including distinct-3 (Appendix~\\ref{app:distinct3}).\nReverse-direction tests (downstream$\\to$canary) find \\textbf{0/24} FDR-significant (all $p{>}0.49$), establishing complete directional asymmetry.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/metric_trajectory.pdf}\n\\caption{Metric trajectories across 10 generations at $\\alpha{=}1.0$ (Pythia-410M, 4~seeds shown as individual traces). Token entropy (top, blue) drops sharply at generation~1, while distinct-1 (bottom, red) begins declining at generations~2--3, establishing a visible one-generation canary lead. The consistent lag across all four seeds confirms that the temporal offset is robust rather than seed-specific. Shaded bands show the inter-seed range. This visual pattern corresponds to the statistical finding of 24/24 forward-direction and 0/24 reverse-direction FDR-significant pairs.}\n\\label{fig:metric_trajectory}\n\\end{figure}\n\n\\paragraph{High contamination ($\\alpha{=}0.75$, 3 seeds).}\nDirectional asymmetry is robustly confirmed across three independent seeds (permutation Granger: 19/24 forward pairs FDR-significant, 0/24 reverse).\nHowever, method-level consensus varies by seed (Tier~3 pairs: 4, 3, and 1 across seeds 42, 43, 44), placing $\\alpha{=}0.75$ squarely in the transitional detection regime.\nDifferenced cross-correlation finds 8/8 pairs significant in \\emph{both} forward and reverse directions at each seed, confirming that this method alone cannot distinguish genuine directional precedence from shared dynamics, a seed-level demonstration of Pitfall~1 (\\S\\ref{sec:pitfalls}).\n\n\\paragraph{ECE as a conditional secondary canary.}\nECE performs equivalently to token entropy across four of five methods (naive, differenced, threshold, permutation Granger).\nIts classification as ``secondary'' is driven entirely by Toda--Yamamoto Type~II errors at $T{=}10$, where bootstrap power analysis yields estimated power of 0.05--0.20 depending on $d_{\\max}$.\nResolving ECE's true canary status requires longer time series.\n\n\\paragraph{Failed canary candidates.}\nNot all metrics serve as canaries.\nEffective rank and Self-BLEU show no detectable lead-lag relationship with any downstream metric under any method or contamination level, and are excluded from the consensus framework.\nEffective rank behavior is model-dependent in an unexpected way: in Pythia-410M, effective rank decreases during collapse (representational contraction), whereas in GPT-2-medium at $\\alpha{=}0.25$ it \\emph{increases} from 2.37 to 8.48 (+258\\%).\nThe GPT-2-medium starting effective rank is near rank-2, suggesting the model's initial representation is already highly concentrated; iterative training disperses it rather than concentrating it further.\nThis opposite directionality across architectures precludes effective rank as a universal canary and motivates architecture-specific analysis (\\S\\ref{sec:discussion}).\n\n\\paragraph{Consensus filtering.}\nOf 16 canary$\\to$downstream pairs tested at $\\alpha{=}1.0$ (4 candidate canaries $\\times$ 4 downstream metrics), \\textbf{6 survive} the full consensus pipeline ($K{\\geq}4/5$ methods, $S{\\geq}3/4$ seeds): token entropy and ECE each predicting distinct-1 and distinct-2 (4 pairs; distinct-3 results in Appendix~\\ref{app:distinct3} bring the total to~6).\nThe 10 eliminated pairs comprise all canary$\\to$perplexity relationships (identified as spurious by the first-differencing diagnostic) and all effective-rank and Self-BLEU pairs (failed canaries).\nThe consensus framework reduces the naive 100\\% significance rate to the 37.5\\% rate supported by the most conservative individual methods (Figure~\\ref{fig:consensus_workflow}).\n\n\n\\subsection{Consensus Framework Validation}\n\\label{sec:consensus_validation}\n\nWe validate the consensus framework's calibration using built-in experimental controls.\n\n\\paragraph{False positive rate.}\nAt $\\alpha{=}0.0$ (three seeds, 24 total pairs), no synthetic data is injected; any detected lead-lag association is a false positive.\nIndividual-method FPR ranges from \\textbf{100\\%} (naive cross-correlation) through 37.5\\% (differenced) and 20.8\\% (threshold) down to \\textbf{0\\%} (permutation Granger: 0/24 across all three seeds).\nThe consensus framework at $K{\\geq}4/5$ achieves \\textbf{FPR${=}$0\\%} (0/24 pairs, three independent seeds), matching the best individual methods while providing robustness against miscalibration of any single method (Table~\\ref{tab:fpr_fnr}).\n\n\\paragraph{False negative rate.}\nAt $\\alpha{=}1.0$, we define 6 effect-size reference pairs (token entropy and ECE $\\to$ distinct-1/2/3) using criteria independent of the consensus methods: drift ratio ${\\geq}3\\times$ the $\\alpha{=}0.0$ baseline (entropy $11.93\\times$, ECE $73.12\\times$) and canary onset strictly preceding downstream onset by ${\\geq}1$ generation (\\S\\ref{sec:calibration}).\nFNR is calibrated on a 4-method panel (excluding differenced cross-correlation to avoid circularity): at $K{\\geq}3/4$, $S{\\geq}3/4$, all~6 are recovered (\\textbf{FNR${=}$0\\%}).\nToda--Yamamoto alone yields FNR${=}$33.3\\% (2/6), missing ECE$\\to$distinct-2 and ECE$\\to$distinct-3 due to Type~II errors at $T{=}10$.\nBoth FPR and FNR are validated on the joint method${\\times}$seed dimension (FPR: 3~seeds at $\\alpha{=}0.0$; FNR: 4~seeds at $\\alpha{=}1.0$), with cross-seed FPR variance negligible (all three seeds yield 0/8 robust pairs at $K{\\geq}4/5$).\nTable~\\ref{tab:fpr_fnr} reports the calibration results.\nTable~\\ref{tab:single-method-errors} complements this analysis by showing the practical consequences of relying on any single method: naive cross-correlation produces false positives at every $\\alpha$ including the null control, Toda--Yamamoto misses true signals at $\\alpha{=}0.75$, while the consensus at $K{\\geq}3$ yields the correct verdict across all five contamination levels.\n\n\\begin{table}[t]\n\\centering\n\\caption{Single-method inference errors across contamination levels.\nEach cell shows the verdict (significant or not) based on multi-seed majority ($\\geq$2/3 seeds with $\\geq$4/8 pairs significant).\n\\checkmark\\ = correct, \\textcolor{red}{FP} = false positive, \\textcolor{blue}{FN} = false negative, $\\circ$ = ambiguous ground truth (either verdict plausible).\nNaive XCorr produces false positives at \\emph{every} $\\alpha$ including the null control, while TY Granger misses true signals at $\\alpha{=}0.75$.\nOnly the multi-method consensus ($K{\\geq}3$) yields the correct verdict at all five contamination levels.}\n\\label{tab:single-method-errors}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n & \\multicolumn{2}{c}{\\textit{No signal}} & \\textit{Ambiguous} & \\multicolumn{2}{c}{\\textit{Causal signal}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-4} \\cmidrule(lr){5-6}\nMethod & $\\alpha{=}0.00$ & $\\alpha{=}0.25$ & $\\alpha{=}0.50$ & $\\alpha{=}0.75$ & $\\alpha{=}1.00$ \\\\\n\\midrule\nNaive XCorr\n  & \\textcolor{red}{FP}{\\scriptsize\\ 8,7,8}\n  & \\textcolor{red}{FP}{\\scriptsize\\ 8,8}\n  & $\\circ${\\scriptsize\\ 8,8,8}\n  & \\checkmark{\\scriptsize\\ 8,8,8}\n  & \\checkmark{\\scriptsize\\ 8,8,8} \\\\\nDiff XCorr (FDR)\n  & \\checkmark{\\scriptsize\\ 4,3,3}\n  & \\checkmark{\\scriptsize\\ 3,1}\n  & $\\circ${\\scriptsize\\ 8,6,6}\n  & \\checkmark{\\scriptsize\\ 8,8,8}\n  & \\checkmark{\\scriptsize\\ 8,8,8} \\\\\nThreshold Onset\n  & \\checkmark{\\scriptsize\\ 3,1,1}\n  & \\checkmark{\\scriptsize\\ 0,0}\n  & $\\circ${\\scriptsize\\ 0,0,0}\n  & \\checkmark{\\scriptsize\\ 4,0,4}\n  & \\checkmark{\\scriptsize\\ 8,8,8} \\\\\nPerm Granger (FDR)\n  & \\checkmark{\\scriptsize\\ 0,0,0}\n  & \\checkmark{\\scriptsize\\ 0,0}\n  & $\\circ${\\scriptsize\\ 0,6,3}\n  & \\checkmark{\\scriptsize\\ 8,5,6}\n  & \\checkmark{\\scriptsize\\ 6,6,6} \\\\\nTY Granger\n  & \\checkmark{\\scriptsize\\ 1,1,0}\n  & \\checkmark{\\scriptsize\\ 0,2}\n  & $\\circ${\\scriptsize\\ 0,0,0}\n  & \\textcolor{blue}{FN}{\\scriptsize\\ 1,1,1}\n  & \\checkmark{\\scriptsize\\ 6,6,4} \\\\\n\\midrule\n\\textbf{Consensus ($K{\\geq}3$)}\n  & \\checkmark\n  & \\checkmark\n  & $\\circ$\n  & \\checkmark\n  & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize Subscript numbers: per-seed significant pair counts out of 8.} \\\\\n\\multicolumn{6}{l}{\\footnotesize Seeds: $\\alpha{=}0.00/0.50/0.75$: 42, 43, 44; $\\alpha{=}0.25$: 43, 44; $\\alpha{=}1.00$: 42, 43, 45.} \\\\\n\\end{tabular}%\n}\n\\end{table}\n\n\\paragraph{Bootstrap power analysis.}\nTo quantify detection power beyond binary FNR, we perform bootstrap power analysis ($B{=}1{,}000$ resamples from 4-seed data at $\\alpha{=}1.0$).\nPermutation Granger achieves power${=}1.0$ on genuine pairs (canary$\\to$diversity) and power${=}0.0$ on spurious pairs (canary$\\to$perplexity), providing clean separation.\nToda--Yamamoto achieves power${=}0.05$--$0.20$ on genuine pairs (depending on $d_{\\max}$), confirming its poor sensitivity at $T{=}10$.\nWe note that bootstrap power${=}1.0$ reflects the effect size in our 4-seed data and should not be interpreted as a universal power guarantee; furthermore, the two methods use different data-generating processes for calibration (permutation Granger resamples observed $\\alpha{=}1.0$ trajectories, while Toda--Yamamoto power was estimated under a generic VAR(2) simulation with $\\beta{=}0.3$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{False positive and false negative rates for individual methods and the consensus framework (Pythia-410M). The consensus threshold $K{\\geq}4/5$ achieves FPR${=}$0\\% and FNR${=}$0\\%, matching the best individual method (permutation Granger) while providing robustness against miscalibration. FPR: $\\alpha{=}0.0$ null control (three seeds, $M{=}5$ methods); values are 3-seed means with ranges in parentheses where cross-seed variance is non-negligible. FNR: $\\alpha{=}1.0$ against 6 effect-size reference pairs (4-method panel excluding differenced cross-correlation, 4~seeds).}\n\\label{tab:fpr_fnr}\n\\begin{tabular}{lcc}\n\\toprule\nCriterion & FPR ($\\alpha{=}0.0$) & FNR ($\\alpha{=}1.0$) \\\\\n\\midrule\nNaive XCorr              & 100\\%              & 0\\%  \\\\\nDifferenced XCorr        & 37.5\\%             & 0\\%  \\\\\nThreshold Onset          & 20.8\\% (12.5--37.5) & 0\\%  \\\\\nPermutation Granger      & 0\\%                & 0\\%  \\\\\nToda--Yamamoto           & 4.2\\% (0--12.5)    & 33.3\\% \\\\\n\\midrule\nConsensus ($K{\\geq}4/5$)              & 0\\%    & 0\\%  \\\\\nConsensus ($K{\\geq}4/5$, $S{\\geq}3/4$) & 0\\%    & 0\\%  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Cross-Architecture, Cross-Scale, and Cross-Domain Generalization}\n\\label{sec:generalization}\n\nThe methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).\nTo test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).\nAll conditions use $\\alpha{=}1.0$ and a single seed.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\\alpha{=}1.0$, single seed per condition). Each cell reports the fraction of canary$\\to$downstream pairs reaching BH-corrected FDR significance ($q{=}0.05$): 8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded). \\textbf{[TBD]}: experiments in progress.}\n\\label{tab:generalization}\n\\begin{tabular}{llccccccc}\n\\toprule\nVariation & Model / Dataset & \\rotatebox{70}{Naive} & \\rotatebox{70}{Diff.\\ XCorr} & \\rotatebox{70}{Threshold} & \\rotatebox{70}{PermG (fwd)} & \\rotatebox{70}{PermG (rev)} & \\rotatebox{70}{TY} & \\rotatebox{70}{$K{\\geq}4/5$} \\\\\n\\midrule\nBaseline      & Pythia-410M / Wiki    & 7/8 & 6/8 & 6/8 & 6/8 & 0/8 & 6/8 & 6/8 \\\\\nArchitecture  & GPT-2-medium / Wiki   & 6/6 & 6/6 & 6/6 & 6/6 & 0/6 & 0/6 & 6/6 \\\\\nArchitecture  & OPT-1.3B / Wiki       & 6/8 & 6/8 & 8/8 & 6/8 & 0/8 & 2/8 & 6/8 \\\\\nScale ($3.4\\times$) & Pythia-1.4B / Wiki & \\multicolumn{7}{c}{\\textbf{[TBD]}} \\\\\nDomain        & Pythia-1B / C4        & \\multicolumn{7}{c}{\\textbf{[TBD]}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Architecture generalization.}\nTable~\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\nAll models reach Tier~3 consensus ($K{\\geq}4/5$) with 6/8 (or 6/6) canary$\\to$diversity pairs confirmed.\nPermutation Granger directionality is perfect across architectures: all forward-direction pairs are FDR-significant while 0 reverse-direction pairs reach significance in any architecture.\n\nMethod-level variation across architectures is informative.\nThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\to$1 discontinuity that cleanly exceeds the onset threshold.\nToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\S\\ref{sec:consensus_validation}).\nDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\geq}4/5$.\n\n% [PLACEHOLDER — activate when Pythia-1.4B and Pythia-1B/C4 results arrive]\n% \\paragraph{Scale and domain generalization.}\n% Scaling from 410M to 1.4B parameters within the Pythia family (3.4$\\times$)\n% preserves the core pattern: permutation Granger identifies \\textbf{XX}/8\n% forward-direction pairs with 0/8 reverse, and consensus $K{\\geq}4/5$\n% yields \\textbf{XX}/8 (Table~\\ref{tab:generalization}).\n% This confirms that the methodological pitfalls are not artifacts of\n% small-model capacity limitations, since the same consensus threshold\n% operates identically at 3.4$\\times$ the parameter count.\n%\n% Replacing WikiText-103 with C4 tests whether the lead-lag pattern\n% depends on the training data distribution. Pythia-1B on C4 yields\n% \\textbf{XX}/8 forward-direction permutation Granger pairs with\n% \\textbf{XX}/8 reverse, and consensus $K{\\geq}4/5$ at \\textbf{XX}/8.\n% Together with the architecture results, this establishes five\n% independent validation lines (three architectures, one scale, one\n% domain) converging on the same conclusion: token entropy\n% Granger-precedes diversity collapse at $\\alpha{=}1.0$.",
      "numLines": 382,
      "startLine": 1,
      "totalLines": 382
    }
  },
  "sourceToolAssistantUUID": "3d57549f-b14b-49fd-a659-e07123890b4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

</details>

---


### Runtime record

_source line 1275_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] **CRITICAL: 论文 Table 7 有 8+ 处错误数据 — 立即修复**  上次 Worker 失败，论文未被修改。Reviewer 逐格核对发现至少 8 个数字错误 + 2 行缺失 + 多处正文引用错误。必须立即修复，否则是 desk reject 级数据完整性问题。  **编辑 `docs/paper/experiments.tex`（C002 真源）：…",
  "leafUuid": "a0bed052-5535-4b7c-871f-9295e9b8f346",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35"
}
```

---


### Runtime record

_source line 1276_

```json
{
  "type": "ai-title",
  "aiTitle": "Finalize paper Round 2 with C4 seed-43 analysis",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35"
}
```

---


### Assistant

_source line 1277 · 2026-05-18T12:57:03.391Z_

Now let me read the rest of the file and also read discussion.tex and conclusion.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0bed052-5535-4b7c-871f-9295e9b8f346",
  "isSidechain": false,
  "requestId": "req_011CbA589BZLb6PM1nNq2u2c",
  "type": "assistant",
  "uuid": "b46143d8-dfbd-4a03-9807-d351fac974a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JcYEjoNySe9ygmQakatDU5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13141,
      "cache_read_input_tokens": 41637,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13141,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 41637,
          "cache_creation_input_tokens": 13141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13141
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

_source line 1278 · 2026-05-18T12:57:05.255Z_

<details open><summary>🔧 Tool call — Read · `toolu_013n2tVRyZqwCFarSfx9jDCJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
  "offset": 382
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b46143d8-dfbd-4a03-9807-d351fac974a0",
  "isSidechain": false,
  "requestId": "req_011CbA589BZLb6PM1nNq2u2c",
  "type": "assistant",
  "uuid": "21d30909-18e5-4858-bdf5-2acd5c133e96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JcYEjoNySe9ygmQakatDU5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13141,
      "cache_read_input_tokens": 41637,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13141,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 41637,
          "cache_creation_input_tokens": 13141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13141
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

_source line 1279 · 2026-05-18T12:57:05.259Z_

<details><summary>↩ Tool result · `toolu_013n2tVRyZqwCFarSfx9jDCJ`</summary>

```text
382	% Granger-precedes diversity collapse at $\alpha{=}1.0$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21d30909-18e5-4858-bdf5-2acd5c133e96",
  "isSidechain": false,
  "promptId": "e0dec198-abf3-497e-80c7-3f5c472bf9b3",
  "type": "user",
  "uuid": "38a2bbf9-cb56-4c41-a2a6-f56de871a292",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
      "content": "% Granger-precedes diversity collapse at $\\alpha{=}1.0$.",
      "numLines": 1,
      "startLine": 382,
      "totalLines": 382
    }
  },
  "sourceToolAssistantUUID": "21d30909-18e5-4858-bdf5-2acd5c133e96",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

</details>

---


### Tool result

_source line 1280 · 2026-05-18T12:57:06.345Z_

<details><summary>↩ Tool result · `toolu_01YG3tB9JikNYFjNQ3qFgWHz`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Lead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.
5	Method choice alone inflates spurious-signal rates to at least 62.5\%, first-differencing exposes canary$\to$perplexity associations as entirely spurious, and regime dependence causes the same Granger test to shift from 24/24 to 0/8 significant pairs across contamination levels.
6	These pitfalls establish that single-method, single-regime analyses (the current default) cannot reliably distinguish genuine temporal precedence from statistical artifacts.
7	
8	Our multi-method consensus framework addresses this fragility by requiring convergent evidence across multiple independent methods and random seeds.
9	Calibrated on effect-size reference pairs with a non-circular 4-method panel, the framework achieves FPR${=}$0\% (0/24, three null-control seeds) and FNR${=}$0\% with permutation Granger power${=}1.0$, and four tiers of practical guidance scaling from exploratory screening to publication-grade claims.
10	
11	Applying the framework, token entropy exhibits robust Granger-precedence over diversity collapse at $\alpha{=}1.0$ (24/24 forward, 0/24 reverse, Tier~3 across 4~seeds, replicated on GPT-2-medium and OPT-1.3B) with a consistent one-generation lead; at $\alpha{=}0.75$, directional asymmetry is confirmed (19/24 forward, 0/24 reverse across 3~seeds) but method consensus remains transitional (Tier~2--3), mapping the detectability boundary.
12	This finding is deliberately scoped to lexical diversity, not model collapse broadly, since the perplexity channel proved entirely spurious under differencing.
13	
14	% [CONDITIONAL — activate when Pythia-1.4B + Pythia-1B/C4 results are positive]
15	% REPLACE the paragraph above with:
16	% Applying the framework, token entropy exhibits robust
17	% Granger-precedence over diversity collapse at $\alpha{=}1.0$ (24/24
18	% forward, 0/24 reverse, Tier~3 across 4~seeds), confirmed by five
19	% independent validation lines: three decoder-only architecture families
20	% (Pythia-410M, GPT-2-medium 345M, OPT-1.3B), within-family scale
21	% variation (Pythia-1.4B, $3.4\times$ parameters), and cross-domain
22	% transfer (Pythia-1B on C4).
23	% At $\alpha{=}0.75$, directional asymmetry is confirmed (19/24 forward,
24	% 0/24 reverse across 3~seeds) but method consensus remains transitional
25	% (Tier~2--3), mapping the detectability boundary.
26	% This finding is deliberately scoped to lexical diversity, not model
27	% collapse broadly, since the perplexity channel proved entirely spurious
28	% under differencing.
29	% [END CONDITIONAL]
30	
31	The methodological pitfalls we expose arise from generic properties of short, non-stationary time series, and we conjecture the consensus framework transfers to other iterative training settings where multiple detection methods can be applied in parallel.
32	Limitations are detailed in \S\ref{sec:limitations}; future directions are discussed in \S\ref{sec:discussion}.
33	
34	% [CONDITIONAL — activate when results positive]
35	% REPLACE "conjecture the consensus framework transfers" paragraph with:
36	% The methodological pitfalls we expose arise from generic properties of
37	% short, non-stationary time series. Cross-architecture (three families,
38	% 345M--1.4B), cross-scale ($3.4\times$), and cross-domain (C4)
39	% validation confirms that these pitfalls and the consensus framework's
40	% operating thresholds are not specific to a single experimental
41	% configuration; evaluation on models at ${>}$10B parameters remains an
42	% open direction.
43	% Limitations are detailed in \S\ref{sec:limitations}; future directions
44	% are discussed in \S\ref{sec:discussion}.
45	% [END CONDITIONAL]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42f5f8e8-34f9-4b60-b4ce-f2fe342084bd",
  "isSidechain": false,
  "promptId": "e0dec198-abf3-497e-80c7-3f5c472bf9b3",
  "type": "user",
  "uuid": "9fa6dc3e-9cdc-44ef-b33d-7006eddd4213",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nLead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.\nMethod choice alone inflates spurious-signal rates to at least 62.5\\%, first-differencing exposes canary$\\to$perplexity associations as entirely spurious, and regime dependence causes the same Granger test to shift from 24/24 to 0/8 significant pairs across contamination levels.\nThese pitfalls establish that single-method, single-regime analyses (the current default) cannot reliably distinguish genuine temporal precedence from statistical artifacts.\n\nOur multi-method consensus framework addresses this fragility by requiring convergent evidence across multiple independent methods and random seeds.\nCalibrated on effect-size reference pairs with a non-circular 4-method panel, the framework achieves FPR${=}$0\\% (0/24, three null-control seeds) and FNR${=}$0\\% with permutation Granger power${=}1.0$, and four tiers of practical guidance scaling from exploratory screening to publication-grade claims.\n\nApplying the framework, token entropy exhibits robust Granger-precedence over diversity collapse at $\\alpha{=}1.0$ (24/24 forward, 0/24 reverse, Tier~3 across 4~seeds, replicated on GPT-2-medium and OPT-1.3B) with a consistent one-generation lead; at $\\alpha{=}0.75$, directional asymmetry is confirmed (19/24 forward, 0/24 reverse across 3~seeds) but method consensus remains transitional (Tier~2--3), mapping the detectability boundary.\nThis finding is deliberately scoped to lexical diversity, not model collapse broadly, since the perplexity channel proved entirely spurious under differencing.\n\n% [CONDITIONAL — activate when Pythia-1.4B + Pythia-1B/C4 results are positive]\n% REPLACE the paragraph above with:\n% Applying the framework, token entropy exhibits robust\n% Granger-precedence over diversity collapse at $\\alpha{=}1.0$ (24/24\n% forward, 0/24 reverse, Tier~3 across 4~seeds), confirmed by five\n% independent validation lines: three decoder-only architecture families\n% (Pythia-410M, GPT-2-medium 345M, OPT-1.3B), within-family scale\n% variation (Pythia-1.4B, $3.4\\times$ parameters), and cross-domain\n% transfer (Pythia-1B on C4).\n% At $\\alpha{=}0.75$, directional asymmetry is confirmed (19/24 forward,\n% 0/24 reverse across 3~seeds) but method consensus remains transitional\n% (Tier~2--3), mapping the detectability boundary.\n% This finding is deliberately scoped to lexical diversity, not model\n% collapse broadly, since the perplexity channel proved entirely spurious\n% under differencing.\n% [END CONDITIONAL]\n\nThe methodological pitfalls we expose arise from generic properties of short, non-stationary time series, and we conjecture the consensus framework transfers to other iterative training settings where multiple detection methods can be applied in parallel.\nLimitations are detailed in \\S\\ref{sec:limitations}; future directions are discussed in \\S\\ref{sec:discussion}.\n\n% [CONDITIONAL — activate when results positive]\n% REPLACE \"conjecture the consensus framework transfers\" paragraph with:\n% The methodological pitfalls we expose arise from generic properties of\n% short, non-stationary time series. Cross-architecture (three families,\n% 345M--1.4B), cross-scale ($3.4\\times$), and cross-domain (C4)\n% validation confirms that these pitfalls and the consensus framework's\n% operating thresholds are not specific to a single experimental\n% configuration; evaluation on models at ${>}$10B parameters remains an\n% open direction.\n% Limitations are detailed in \\S\\ref{sec:limitations}; future directions\n% are discussed in \\S\\ref{sec:discussion}.\n% [END CONDITIONAL]",
      "numLines": 45,
      "startLine": 1,
      "totalLines": 45
    }
  },
  "sourceToolAssistantUUID": "42f5f8e8-34f9-4b60-b4ce-f2fe342084bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

</details>

---


### Tool call

_source line 1281 · 2026-05-18T12:57:05.806Z_

<details open><summary>🔧 Tool call — Read · `toolu_015Y4jfagoFZRQByfd94Lj6D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38a2bbf9-cb56-4c41-a2a6-f56de871a292",
  "isSidechain": false,
  "requestId": "req_011CbA589BZLb6PM1nNq2u2c",
  "type": "assistant",
  "uuid": "86547fdd-1f52-485a-96e3-e95e6a5f6fdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JcYEjoNySe9ygmQakatDU5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13141,
      "cache_read_input_tokens": 41637,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13141,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 41637,
          "cache_creation_input_tokens": 13141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13141
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

_source line 1282 · 2026-05-18T12:57:05.810Z_

<details><summary>↩ Tool result · `toolu_015Y4jfagoFZRQByfd94Lj6D`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Granger precedence is not causation.}
4	Granger causality tests whether past values of one series improve prediction of another beyond its own history; it does not establish true causation~\cite{granger1969investigating,shojaie2022granger}.
5	Bivariate Granger tests cannot exclude confounders: an unobserved process (such as a latent distributional shift in the training data) could independently drive both token entropy and diversity metrics, producing spurious lead-lag associations even when no direct relationship exists.
6	Our multi-method consensus framework inherits this limitation in full.
7	Throughout this paper, ``Granger precedence'' denotes predictive improvement in a time-series forecasting sense, not a causal mechanism.
8	This distinction is why we scope our central claim to ``token entropy Granger-precedes diversity collapse'' rather than asserting that token entropy \emph{causes} diversity collapse.
9	
10	\paragraph{Calibration scope and generalization.}
11	All FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\alpha \in \{0.0, 0.25, 0.50, 0.75, 1.0\}$).
12	Generalization to other model architectures, datasets, or training protocols requires independent validation.
13	The consensus framework's structure (multi-method agreement combined with multi-seed replication) is intended to be applicable beyond this specific setting, but the operating thresholds ($K{\geq}4/5$ methods, $S{\geq}3/4$ seeds) are empirically calibrated and may require re-tuning under different conditions.
14	For instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.
15	Cross-architecture validation on GPT-2-medium and OPT-1.3B (single seed each, $\alpha{=}1.0$) replicates the entropy-leads-diversity pattern at Tier~3 consensus: all three model families (Pythia-410M, GPT-2-medium, OPT-1.3B) reach $K{\geq}4/5$ method agreement (Table~\ref{tab:generalization}), with 0 reverse-direction pairs significant across any architecture.
16	Full-panel inter-method agreement remains low (Fleiss' $\kappa{=}0.091$) but rises to $\kappa{=}0.667$ among the three informative methods (\S\ref{sec:method_sensitivity}), confirming that the consensus framework's structure transfers across architectures even if operating thresholds require architecture-specific calibration.
17	At $\alpha{=}0.25$, GPT-2-medium yields 1/8 pairs at Tier~3 consensus ($K{\geq}4/5$) and 7/8 at Tier~2 ($K{\geq}3/5$), placing it in the same null/low-detectability regime as Pythia (0/8 Tier~3) and confirming that the detectability boundary is consistent across two transformer decoder-only model families of similar scale.
18	The full GPT-2-medium drift profile at $\alpha{=}0.25$ is: entropy $-32.8\%$, ECE $+422\%$, perplexity $-44.5\%$, distinct-1 $-23.5\%$, distinct-2 $-31.6\%$, distinct-3 $-30.2\%$, MAUVE $0.0315 \to 0.0282$ ($-10.5\%$).
19	Compared to Pythia ($-4.7{\pm}0.5\%$ entropy, $-40.3{\pm}0.3\%$ distinct-1), GPT-2-medium shows substantially stronger canary drift but milder diversity decline, likely due to its $8\times$ larger batch size exposing more data per step.
20	The stronger canary signal approaches detectability (permutation Granger $F{=}64.09$, $p{=}0.081$ for entropy$\to$distinct-1, compared to $p{>}0.5$ in Pythia), suggesting that the regime boundary may shift with increased effective sample size, but single-seed $T{=}10$ power remains insufficient for Confirmatory claims.
21	Toda--Yamamoto Granger finds 1/8 pairs significant, consistent with its known instability at short series lengths (\S\ref{sec:consensus_validation}).
22	
23	% [CONDITIONAL — activate when Pythia-1.4B + Pythia-1B/C4 results are positive]
24	% UPDATE L15 above: "three model families" → "three architecture families
25	% spanning 345M--1.4B parameters, plus cross-domain (C4) validation"
26	%
27	% ADD after L21:
28	% \paragraph{Scale invariance within the Pythia family.}
29	% Pythia-410M and Pythia-1.4B (3.4$\times$ parameters, same architecture
30	% family and tokenizer) reach the same consensus level ($K{\geq}4/5$:
31	% \textbf{XX}/8 at 410M, \textbf{XX}/8 at 1.4B;
32	% Table~\ref{tab:generalization}), confirming that the methodological
33	% pitfalls and the entropy-leads-diversity pattern are not artifacts of
34	% small-model capacity limitations.
35	% This within-family scale comparison isolates the effect of model
36	% capacity from confounding differences in tokenizer, pre-training
37	% corpus, and architectural choices that vary across families.
38	%
39	% Cross-domain validation on C4 (\textbf{XX}/8 consensus $K{\geq}4/5$)
40	% further establishes that the lead-lag pattern is not an artifact of
41	% WikiText-103's narrow topical distribution.
42	% Together, five independent validation lines (three architectures, one
43	% scale, one domain) converge on the same conclusion at $\alpha{=}1.0$.
44	% [END CONDITIONAL]
45	
46	\paragraph{Why $K{=}4/5$ is the consensus tipping point.}
47	The $K{=}4/5$ threshold reflects the composition of the five-method panel rather than an arbitrary choice.
48	At $K{=}3/5$, the two high-FPR methods (naive cross-correlation at 100\% and differenced cross-correlation at 37.5\%) can form a majority with any single additional method, allowing false positives to pass even when both conservative methods (permutation Granger and Toda--Yamamoto) disagree.
49	At $K{=}4/5$, any agreeing coalition must include at least one low-FPR method, which effectively vetoes spurious signals: null-control FPR drops from 37.5\% to 0\%.
50	Raising the threshold to $K{=}5/5$ requires Toda--Yamamoto agreement, but its low power at $T{=}10$ produces Type~II errors on 3/6 reference pairs (FNR${=}$50\%).
51	The $K{=}4/5$ threshold thus occupies the unique operating point where exactly one low-power method can be excluded without admitting high-FPR coalitions.
52	
53	\paragraph{Short time-series constraint.}
54	With $T{=}10$ generation cycles (11 data points per series), our time-series analyses operate near the lower bound of what standard methods require.
55	This series length is typical for iterative training studies, where each generation involves a complete training run, but it severely limits statistical power.
56	The Toda--Yamamoto procedure's elevated FNR (33.3\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.
57	This finding aligns with \citet{boettiger2012limits}, who demonstrated that early-warning signals have limited detection power in short time series.
58	Longer generation chains would improve power for all methods but impose substantial computational cost; this trade-off between statistical power and compute budget is inherent to iterative training research and cannot be resolved by methodological improvements alone.
59	However, observation window sensitivity analysis provides reassurance: the $4/5$ consensus classification stabilizes at $T{\geq}5$, well below our observation window of $T{=}10$, with identical results from $T{=}5$ through $T{=}10$ (Appendix~\ref{app:window_sensitivity}).
60	The Toda--Yamamoto procedure produces valid test statistics at all window lengths ($T \in \{5, \ldots, 10\}$), but with unstable sensitivity (3/6 to 6/6 pairs reach significance depending on window length), confirming that its elevated FNR reflects limited residual degrees of freedom rather than absence of signal.
61	
62	\paragraph{Effective rank direction is model-dependent.}
63	Effective rank evolves in opposite directions across architectures during iterative training.
64	In Pythia-410M, effective rank decreases (representational contraction), consistent with mode collapse concentrating the output distribution into fewer dimensions.
65	In GPT-2-medium at $\alpha{=}0.25$, effective rank \emph{increases} from 2.37 to 8.48 (+258\%).
66	The likely explanation is starting-point dependence: GPT-2-medium begins near rank-2 (a highly concentrated initial representation), and iterative training disperses activation mass across more dimensions rather than concentrating it further.
67	This finding demonstrates that effective rank cannot serve as a direction-agnostic canary and that its trajectory must be interpreted relative to architecture-specific baselines.
68	We note this as a caveat on the generality of representational metrics as collapse indicators, even when the regime map (Table~\ref{tab:cross_arch_regime}) and lead-lag detectability are consistent across architectures.
69	
70	\paragraph{Diversity--calibration dissociation.}
71	Diversity metrics and calibration metrics respond to synthetic contamination in qualitatively opposite directions across the $\alpha$ spectrum.
72	Diversity collapse (distinct-$n$ decline) is most severe at low contamination ($\alpha{=}0.25$: distinct-3 declines by $58.9{\pm}0.9\%$) and attenuates at higher levels ($\alpha{=}1.0$: $-30.5\%$), while calibration degradation (ECE) increases monotonically with $\alpha$ ($+51.7\%$ at $\alpha{=}0.0$ to $+3780\%$ at $\alpha{=}1.0$).
73	This dissociation underscores the need for multi-method consensus: the regime in which a metric degrades most severely ($\alpha{=}0.25$ for diversity) does not coincide with the regime in which its temporal lead is most detectable ($\alpha{\geq}0.75$), and a single metric family cannot capture the full picture of iterative training degradation.
74	
75	\paragraph{Practical utility paradox.}
76	The canary framework exhibits a paradox: it works best where it is least needed.
77	At $\alpha{\geq}0.75$, token entropy reliably Granger-precedes diversity collapse, but at these contamination levels degradation is already severe and likely detectable through simpler means.
78	At $\alpha{\leq}0.25$, where early warning would be most valuable, the canary signal is undetectable by any method tested; at $\alpha{=}0.50$, detectability is seed-dependent (0/8--6/8, 3~seeds, median 3/8), marking the onset boundary where ECE outperforms token entropy as the more sensitive canary.
79	This sensitivity difference reflects how each metric aggregates distributional information: ECE decomposes calibration error across multiple probability bins, making it responsive to changes in the shape of the predicted distribution rather than just its mean, while token entropy compresses the full distribution into a single scalar average.
80	At moderate contamination ($\alpha{=}0.50$), the distributional shifts are subtle enough that bin-level decomposition detects them but the global average does not.
81	This is not a framework deficiency but an inherent characteristic of collapse dynamics: at low contamination, diversity changes are too small relative to inter-generation noise for any temporal lead to emerge above the statistical detection floor~\cite{boettiger2012limits}.
82	The practical implication is that the framework is better suited to continuous monitoring dashboards that track cumulative trend shifts across many generations than to single-point threshold alarms.
83	If contamination grows over time (as in realistic web-scale data pipelines), the canary signal will strengthen as $\alpha$ increases, providing earlier detection than post-hoc quality audits.
84	
85	\paragraph{Why this matters despite the paradox.}
86	In practice, the effective contamination level $\alpha$ is unknown and typically increases over time as web-scraped training corpora accumulate more machine-generated text.
87	A continuous monitoring dashboard would automatically trigger when $\alpha$ crosses the detectability threshold ($\alpha{\approx}0.50$), converting the paradox from a static limitation into a temporal advantage: the framework detects collapse precisely when contamination first becomes severe enough to matter.
88	The methodological contribution is independent of canary utility: the consensus framework and its three-pitfall diagnostic apply to any short-time-series lead-lag analysis in iterative training, regardless of which specific metrics are monitored.
89	The regime map itself is an actionable output: practitioners who know that $\alpha{<}0.25$ is below the detection floor should invest in data provenance and source filtering rather than metric monitoring at those contamination levels.
90	
91	\paragraph{Broader implications for training pipelines.}
92	In the Confirmatory regime ($\alpha{\geq}0.75$), the consensus framework can serve as a continuous monitoring signal within iterative training pipelines: the multi-method panel would run after each generation, and sustained Tier~3 agreement across metric pairs would flag potential collapse onset for human review.
93	This complements the continuous monitoring dashboard framing above, where cumulative trend shifts across generations provide more reliable detection than single-point threshold alarms.
94	The cost of running five lightweight statistical tests per generation is negligible relative to the cost of training itself, though the practical utility paradox (\S\ref{sec:discussion}) and the absence of intervention experiments (\S\ref{sec:limitations}) mean that such monitoring currently provides diagnostic evidence rather than actionable triggers.
95	
96	\paragraph{Token entropy versus perplexity.}
97	The finding that token entropy Granger-precedes diversity while perplexity does not ($F{\approx}0$, $p{=}0.99$ after differencing) requires clarification, since perplexity is the exponential of cross-entropy and appears mathematically related to token entropy.
98	The distinction lies in the evaluation domain: our ``token entropy'' is $H(p_\theta | \text{context})$ evaluated on \emph{held-out real data} (the model's predictive uncertainty on genuine text), while ``perplexity'' is $\exp(H_\text{cross})$ evaluated on \emph{model-generated text} (the model's self-consistency on its own outputs).
99	The identity $\text{ppl} = \exp(\text{entropy})$ holds only when the model distribution equals the data distribution, a condition that iterative collapse systematically violates.
100	In practice, both metrics trend downward during collapse (the model becomes more certain), producing high undifferenced correlation.
101	First-differencing removes this shared trend: the canary$\to$diversity channel survives because entropy \emph{leads} diversity decline by one generation (the model narrows its distribution before output diversity measurably falls), whereas the canary$\to$perplexity channel vanishes because entropy and perplexity co-move \emph{synchronously}, both driven by the same underlying distributional contraction.
102	Thus, the perplexity channel being ``spurious'' is not trivially expected from the mathematical relationship, but rather a substantive finding about collapse dynamics: the generation-evaluation divergence breaks the entropy--perplexity coupling in a temporally informative way.
103	
104	\paragraph{NLP-specific constraints on lead-lag analysis.}
105	Our application of Granger-type methods to iterative training faces constraints absent in their original econometric settings.
106	First, observation length: typical econometric applications use $T{=}100$--$1000$ time points, whereas iterative training studies are limited to $T{=}5$--$20$ generations due to computational cost.
107	This severely constrains degrees of freedom for VAR-based methods and explains the Toda--Yamamoto procedure's poor power in our setting.
108	Second, non-stationarity is by design: each generation's training data differs from the previous generation's, making the underlying process non-stationary by construction rather than as an incidental property.
109	Standard stationarity tests (ADF, KPSS) may yield misleading results when applied to processes with deterministic degradation trajectories rather than stochastic unit roots.
110	Third, the sample-size bottleneck compounds with multiple testing: with only 8--32 pairs per regime, FDR correction operates on small multiplicity, limiting its ability to separate true from false discoveries.
111	These constraints motivate our multi-method consensus approach as a complement to, rather than replacement for, traditional significance testing.
112	
113	\paragraph{Future work.}
114	Several directions extend this work.
115	Multivariate VAR models would enable testing for confounders and multi-directional Granger relationships beyond our current bivariate framework.
116	Multi-seed replication across the three validated architecture families (Pythia, GPT-2, OPT) would further strengthen the cross-architecture claims; evaluation on larger-scale models (${>}2$B parameters) remains an open direction.
117	% [CONDITIONAL — activate when Pythia-1.4B + C4 results positive]
118	% REPLACE above sentence with:
119	% Multi-seed replication across all five validated conditions would
120	% further strengthen the generalization claims; evaluation on models at
121	% ${>}$10B parameters remains the primary open scaling question.
122	% [END CONDITIONAL]
123	Online monitoring, where canary metrics are computed within training pipelines for real-time collapse detection, is a natural applied extension.
124	Accumulate-mode experiments~\cite{dey2024breaking} would test whether canary dynamics differ from the replace-mode setting studied here.
125	Finally, connecting the empirically observed onset boundary at $\alpha{\approx}0.25$--$0.50$ to theoretical phase transition analysis~\cite{truong2025entropy} could yield a principled explanation for why canary signals emerge at this contamination regime rather than at lower contamination levels.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86547fdd-1f52-485a-96e3-e95e6a5f6fdc",
  "isSidechain": false,
  "promptId": "e0dec198-abf3-497e-80c7-3f5c472bf9b3",
  "type": "user",
  "uuid": "d94f1d61-49b8-48ea-9000-91fae55daa14",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Granger precedence is not causation.}\nGranger causality tests whether past values of one series improve prediction of another beyond its own history; it does not establish true causation~\\cite{granger1969investigating,shojaie2022granger}.\nBivariate Granger tests cannot exclude confounders: an unobserved process (such as a latent distributional shift in the training data) could independently drive both token entropy and diversity metrics, producing spurious lead-lag associations even when no direct relationship exists.\nOur multi-method consensus framework inherits this limitation in full.\nThroughout this paper, ``Granger precedence'' denotes predictive improvement in a time-series forecasting sense, not a causal mechanism.\nThis distinction is why we scope our central claim to ``token entropy Granger-precedes diversity collapse'' rather than asserting that token entropy \\emph{causes} diversity collapse.\n\n\\paragraph{Calibration scope and generalization.}\nAll FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\\alpha \\in \\{0.0, 0.25, 0.50, 0.75, 1.0\\}$).\nGeneralization to other model architectures, datasets, or training protocols requires independent validation.\nThe consensus framework's structure (multi-method agreement combined with multi-seed replication) is intended to be applicable beyond this specific setting, but the operating thresholds ($K{\\geq}4/5$ methods, $S{\\geq}3/4$ seeds) are empirically calibrated and may require re-tuning under different conditions.\nFor instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.\nCross-architecture validation on GPT-2-medium and OPT-1.3B (single seed each, $\\alpha{=}1.0$) replicates the entropy-leads-diversity pattern at Tier~3 consensus: all three model families (Pythia-410M, GPT-2-medium, OPT-1.3B) reach $K{\\geq}4/5$ method agreement (Table~\\ref{tab:generalization}), with 0 reverse-direction pairs significant across any architecture.\nFull-panel inter-method agreement remains low (Fleiss' $\\kappa{=}0.091$) but rises to $\\kappa{=}0.667$ among the three informative methods (\\S\\ref{sec:method_sensitivity}), confirming that the consensus framework's structure transfers across architectures even if operating thresholds require architecture-specific calibration.\nAt $\\alpha{=}0.25$, GPT-2-medium yields 1/8 pairs at Tier~3 consensus ($K{\\geq}4/5$) and 7/8 at Tier~2 ($K{\\geq}3/5$), placing it in the same null/low-detectability regime as Pythia (0/8 Tier~3) and confirming that the detectability boundary is consistent across two transformer decoder-only model families of similar scale.\nThe full GPT-2-medium drift profile at $\\alpha{=}0.25$ is: entropy $-32.8\\%$, ECE $+422\\%$, perplexity $-44.5\\%$, distinct-1 $-23.5\\%$, distinct-2 $-31.6\\%$, distinct-3 $-30.2\\%$, MAUVE $0.0315 \\to 0.0282$ ($-10.5\\%$).\nCompared to Pythia ($-4.7{\\pm}0.5\\%$ entropy, $-40.3{\\pm}0.3\\%$ distinct-1), GPT-2-medium shows substantially stronger canary drift but milder diversity decline, likely due to its $8\\times$ larger batch size exposing more data per step.\nThe stronger canary signal approaches detectability (permutation Granger $F{=}64.09$, $p{=}0.081$ for entropy$\\to$distinct-1, compared to $p{>}0.5$ in Pythia), suggesting that the regime boundary may shift with increased effective sample size, but single-seed $T{=}10$ power remains insufficient for Confirmatory claims.\nToda--Yamamoto Granger finds 1/8 pairs significant, consistent with its known instability at short series lengths (\\S\\ref{sec:consensus_validation}).\n\n% [CONDITIONAL — activate when Pythia-1.4B + Pythia-1B/C4 results are positive]\n% UPDATE L15 above: \"three model families\" → \"three architecture families\n% spanning 345M--1.4B parameters, plus cross-domain (C4) validation\"\n%\n% ADD after L21:\n% \\paragraph{Scale invariance within the Pythia family.}\n% Pythia-410M and Pythia-1.4B (3.4$\\times$ parameters, same architecture\n% family and tokenizer) reach the same consensus level ($K{\\geq}4/5$:\n% \\textbf{XX}/8 at 410M, \\textbf{XX}/8 at 1.4B;\n% Table~\\ref{tab:generalization}), confirming that the methodological\n% pitfalls and the entropy-leads-diversity pattern are not artifacts of\n% small-model capacity limitations.\n% This within-family scale comparison isolates the effect of model\n% capacity from confounding differences in tokenizer, pre-training\n% corpus, and architectural choices that vary across families.\n%\n% Cross-domain validation on C4 (\\textbf{XX}/8 consensus $K{\\geq}4/5$)\n% further establishes that the lead-lag pattern is not an artifact of\n% WikiText-103's narrow topical distribution.\n% Together, five independent validation lines (three architectures, one\n% scale, one domain) converge on the same conclusion at $\\alpha{=}1.0$.\n% [END CONDITIONAL]\n\n\\paragraph{Why $K{=}4/5$ is the consensus tipping point.}\nThe $K{=}4/5$ threshold reflects the composition of the five-method panel rather than an arbitrary choice.\nAt $K{=}3/5$, the two high-FPR methods (naive cross-correlation at 100\\% and differenced cross-correlation at 37.5\\%) can form a majority with any single additional method, allowing false positives to pass even when both conservative methods (permutation Granger and Toda--Yamamoto) disagree.\nAt $K{=}4/5$, any agreeing coalition must include at least one low-FPR method, which effectively vetoes spurious signals: null-control FPR drops from 37.5\\% to 0\\%.\nRaising the threshold to $K{=}5/5$ requires Toda--Yamamoto agreement, but its low power at $T{=}10$ produces Type~II errors on 3/6 reference pairs (FNR${=}$50\\%).\nThe $K{=}4/5$ threshold thus occupies the unique operating point where exactly one low-power method can be excluded without admitting high-FPR coalitions.\n\n\\paragraph{Short time-series constraint.}\nWith $T{=}10$ generation cycles (11 data points per series), our time-series analyses operate near the lower bound of what standard methods require.\nThis series length is typical for iterative training studies, where each generation involves a complete training run, but it severely limits statistical power.\nThe Toda--Yamamoto procedure's elevated FNR (33.3\\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.\nThis finding aligns with \\citet{boettiger2012limits}, who demonstrated that early-warning signals have limited detection power in short time series.\nLonger generation chains would improve power for all methods but impose substantial computational cost; this trade-off between statistical power and compute budget is inherent to iterative training research and cannot be resolved by methodological improvements alone.\nHowever, observation window sensitivity analysis provides reassurance: the $4/5$ consensus classification stabilizes at $T{\\geq}5$, well below our observation window of $T{=}10$, with identical results from $T{=}5$ through $T{=}10$ (Appendix~\\ref{app:window_sensitivity}).\nThe Toda--Yamamoto procedure produces valid test statistics at all window lengths ($T \\in \\{5, \\ldots, 10\\}$), but with unstable sensitivity (3/6 to 6/6 pairs reach significance depending on window length), confirming that its elevated FNR reflects limited residual degrees of freedom rather than absence of signal.\n\n\\paragraph{Effective rank direction is model-dependent.}\nEffective rank evolves in opposite directions across architectures during iterative training.\nIn Pythia-410M, effective rank decreases (representational contraction), consistent with mode collapse concentrating the output distribution into fewer dimensions.\nIn GPT-2-medium at $\\alpha{=}0.25$, effective rank \\emph{increases} from 2.37 to 8.48 (+258\\%).\nThe likely explanation is starting-point dependence: GPT-2-medium begins near rank-2 (a highly concentrated initial representation), and iterative training disperses activation mass across more dimensions rather than concentrating it further.\nThis finding demonstrates that effective rank cannot serve as a direction-agnostic canary and that its trajectory must be interpreted relative to architecture-specific baselines.\nWe note this as a caveat on the generality of representational metrics as collapse indicators, even when the regime map (Table~\\ref{tab:cross_arch_regime}) and lead-lag detectability are consistent across architectures.\n\n\\paragraph{Diversity--calibration dissociation.}\nDiversity metrics and calibration metrics respond to synthetic contamination in qualitatively opposite directions across the $\\alpha$ spectrum.\nDiversity collapse (distinct-$n$ decline) is most severe at low contamination ($\\alpha{=}0.25$: distinct-3 declines by $58.9{\\pm}0.9\\%$) and attenuates at higher levels ($\\alpha{=}1.0$: $-30.5\\%$), while calibration degradation (ECE) increases monotonically with $\\alpha$ ($+51.7\\%$ at $\\alpha{=}0.0$ to $+3780\\%$ at $\\alpha{=}1.0$).\nThis dissociation underscores the need for multi-method consensus: the regime in which a metric degrades most severely ($\\alpha{=}0.25$ for diversity) does not coincide with the regime in which its temporal lead is most detectable ($\\alpha{\\geq}0.75$), and a single metric family cannot capture the full picture of iterative training degradation.\n\n\\paragraph{Practical utility paradox.}\nThe canary framework exhibits a paradox: it works best where it is least needed.\nAt $\\alpha{\\geq}0.75$, token entropy reliably Granger-precedes diversity collapse, but at these contamination levels degradation is already severe and likely detectable through simpler means.\nAt $\\alpha{\\leq}0.25$, where early warning would be most valuable, the canary signal is undetectable by any method tested; at $\\alpha{=}0.50$, detectability is seed-dependent (0/8--6/8, 3~seeds, median 3/8), marking the onset boundary where ECE outperforms token entropy as the more sensitive canary.\nThis sensitivity difference reflects how each metric aggregates distributional information: ECE decomposes calibration error across multiple probability bins, making it responsive to changes in the shape of the predicted distribution rather than just its mean, while token entropy compresses the full distribution into a single scalar average.\nAt moderate contamination ($\\alpha{=}0.50$), the distributional shifts are subtle enough that bin-level decomposition detects them but the global average does not.\nThis is not a framework deficiency but an inherent characteristic of collapse dynamics: at low contamination, diversity changes are too small relative to inter-generation noise for any temporal lead to emerge above the statistical detection floor~\\cite{boettiger2012limits}.\nThe practical implication is that the framework is better suited to continuous monitoring dashboards that track cumulative trend shifts across many generations than to single-point threshold alarms.\nIf contamination grows over time (as in realistic web-scale data pipelines), the canary signal will strengthen as $\\alpha$ increases, providing earlier detection than post-hoc quality audits.\n\n\\paragraph{Why this matters despite the paradox.}\nIn practice, the effective contamination level $\\alpha$ is unknown and typically increases over time as web-scraped training corpora accumulate more machine-generated text.\nA continuous monitoring dashboard would automatically trigger when $\\alpha$ crosses the detectability threshold ($\\alpha{\\approx}0.50$), converting the paradox from a static limitation into a temporal advantage: the framework detects collapse precisely when contamination first becomes severe enough to matter.\nThe methodological contribution is independent of canary utility: the consensus framework and its three-pitfall diagnostic apply to any short-time-series lead-lag analysis in iterative training, regardless of which specific metrics are monitored.\nThe regime map itself is an actionable output: practitioners who know that $\\alpha{<}0.25$ is below the detection floor should invest in data provenance and source filtering rather than metric monitoring at those contamination levels.\n\n\\paragraph{Broader implications for training pipelines.}\nIn the Confirmatory regime ($\\alpha{\\geq}0.75$), the consensus framework can serve as a continuous monitoring signal within iterative training pipelines: the multi-method panel would run after each generation, and sustained Tier~3 agreement across metric pairs would flag potential collapse onset for human review.\nThis complements the continuous monitoring dashboard framing above, where cumulative trend shifts across generations provide more reliable detection than single-point threshold alarms.\nThe cost of running five lightweight statistical tests per generation is negligible relative to the cost of training itself, though the practical utility paradox (\\S\\ref{sec:discussion}) and the absence of intervention experiments (\\S\\ref{sec:limitations}) mean that such monitoring currently provides diagnostic evidence rather than actionable triggers.\n\n\\paragraph{Token entropy versus perplexity.}\nThe finding that token entropy Granger-precedes diversity while perplexity does not ($F{\\approx}0$, $p{=}0.99$ after differencing) requires clarification, since perplexity is the exponential of cross-entropy and appears mathematically related to token entropy.\nThe distinction lies in the evaluation domain: our ``token entropy'' is $H(p_\\theta | \\text{context})$ evaluated on \\emph{held-out real data} (the model's predictive uncertainty on genuine text), while ``perplexity'' is $\\exp(H_\\text{cross})$ evaluated on \\emph{model-generated text} (the model's self-consistency on its own outputs).\nThe identity $\\text{ppl} = \\exp(\\text{entropy})$ holds only when the model distribution equals the data distribution, a condition that iterative collapse systematically violates.\nIn practice, both metrics trend downward during collapse (the model becomes more certain), producing high undifferenced correlation.\nFirst-differencing removes this shared trend: the canary$\\to$diversity channel survives because entropy \\emph{leads} diversity decline by one generation (the model narrows its distribution before output diversity measurably falls), whereas the canary$\\to$perplexity channel vanishes because entropy and perplexity co-move \\emph{synchronously}, both driven by the same underlying distributional contraction.\nThus, the perplexity channel being ``spurious'' is not trivially expected from the mathematical relationship, but rather a substantive finding about collapse dynamics: the generation-evaluation divergence breaks the entropy--perplexity coupling in a temporally informative way.\n\n\\paragraph{NLP-specific constraints on lead-lag analysis.}\nOur application of Granger-type methods to iterative training faces constraints absent in their original econometric settings.\nFirst, observation length: typical econometric applications use $T{=}100$--$1000$ time points, whereas iterative training studies are limited to $T{=}5$--$20$ generations due to computational cost.\nThis severely constrains degrees of freedom for VAR-based methods and explains the Toda--Yamamoto procedure's poor power in our setting.\nSecond, non-stationarity is by design: each generation's training data differs from the previous generation's, making the underlying process non-stationary by construction rather than as an incidental property.\nStandard stationarity tests (ADF, KPSS) may yield misleading results when applied to processes with deterministic degradation trajectories rather than stochastic unit roots.\nThird, the sample-size bottleneck compounds with multiple testing: with only 8--32 pairs per regime, FDR correction operates on small multiplicity, limiting its ability to separate true from false discoveries.\nThese constraints motivate our multi-method consensus approach as a complement to, rather than replacement for, traditional significance testing.\n\n\\paragraph{Future work.}\nSeveral directions extend this work.\nMultivariate VAR models would enable testing for confounders and multi-directional Granger relationships beyond our current bivariate framework.\nMulti-seed replication across the three validated architecture families (Pythia, GPT-2, OPT) would further strengthen the cross-architecture claims; evaluation on larger-scale models (${>}2$B parameters) remains an open direction.\n% [CONDITIONAL — activate when Pythia-1.4B + C4 results positive]\n% REPLACE above sentence with:\n% Multi-seed replication across all five validated conditions would\n% further strengthen the generalization claims; evaluation on models at\n% ${>}$10B parameters remains the primary open scaling question.\n% [END CONDITIONAL]\nOnline monitoring, where canary metrics are computed within training pipelines for real-time collapse detection, is a natural applied extension.\nAccumulate-mode experiments~\\cite{dey2024breaking} would test whether canary dynamics differ from the replace-mode setting studied here.\nFinally, connecting the empirically observed onset boundary at $\\alpha{\\approx}0.25$--$0.50$ to theoretical phase transition analysis~\\cite{truong2025entropy} could yield a principled explanation for why canary signals emerge at this contamination regime rather than at lower contamination levels.",
      "numLines": 125,
      "startLine": 1,
      "totalLines": 125
    }
  },
  "sourceToolAssistantUUID": "86547fdd-1f52-485a-96e3-e95e6a5f6fdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

</details>

---


### Tool call

_source line 1283 · 2026-05-18T12:57:06.341Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YG3tB9JikNYFjNQ3qFgWHz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d94f1d61-49b8-48ea-9000-91fae55daa14",
  "isSidechain": false,
  "requestId": "req_011CbA589BZLb6PM1nNq2u2c",
  "type": "assistant",
  "uuid": "42f5f8e8-34f9-4b60-b4ce-f2fe342084bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JcYEjoNySe9ygmQakatDU5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13141,
      "cache_read_input_tokens": 41637,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13141,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 41637,
          "cache_creation_input_tokens": 13141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13141
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

_source line 1284_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] **CRITICAL: 论文 Table 7 有 8+ 处错误数据 — 立即修复**  上次 Worker 失败，论文未被修改。Reviewer 逐格核对发现至少 8 个数字错误 + 2 行缺失 + 多处正文引用错误。必须立即修复，否则是 desk reject 级数据完整性问题。  **编辑 `docs/paper/experiments.tex`（C002 真源）：…",
  "leafUuid": "9fa6dc3e-9cdc-44ef-b33d-7006eddd4213",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35"
}
```

---


### Runtime record

_source line 1285_

```json
{
  "type": "ai-title",
  "aiTitle": "Finalize paper Round 2 with C4 seed-43 analysis",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35"
}
```

---


### Runtime record

_source line 1286_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] **CRITICAL: 论文 Table 7 有 8+ 处错误数据 — 立即修复**  上次 Worker 失败，论文未被修改。Reviewer 逐格核对发现至少 8 个数字错误 + 2 行缺失 + 多处正文引用错误。必须立即修复，否则是 desk reject 级数据完整性问题。  **编辑 `docs/paper/experiments.tex`（C002 真源）：…",
  "leafUuid": "9fa6dc3e-9cdc-44ef-b33d-7006eddd4213",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35"
}
```

---


### Runtime record

_source line 1287_

```json
{
  "type": "ai-title",
  "aiTitle": "Finalize paper Round 2 with C4 seed-43 analysis",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35"
}
```

---


### Runtime record

_source line 1288_

```json
{
  "type": "ai-title",
  "aiTitle": "Finalize paper Round 2 with C4 seed-43 analysis",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35"
}
```

---


### Runtime record

_source line 1289 · 2026-05-18T12:57:42.844Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T12:57:42.844Z",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "content": "[Director 指令] **Table 7 数字已确认，但 3 处残留错误需立即修复**\n\n编辑 `docs/paper/experiments.tex`：\n\n**a) CRITICAL — Domain 段 L381-383 重写**\n删除以下内容（或附近等价文本）：\n> \"We exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6→1682.6, ADF statistic +1.07) violates the stationarity assumption...\"\n> \"Instead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing.\"\n\n替换为：C4 使用与其他条件相同的 8 对 downstream（{token_entropy, ECE} × {d1, d2, d3, ppl}）。可以保留 perplexity 在 C4 域的极端 divergence 作为观察（ppl +50× 比 Pythia 更极端），但不能说\"排除\"。删除所有 MAUVE 引用。\n\n**b) WARNING — L337 seed 描述**\n\"All conditions use α=1.0 and a single seed.\" → \"All conditions use α=1.0. Architecture conditions use a single seed (s42); Scale and Domain conditions include two seeds (s42, s43).\"\n\n**c) WARNING — 验证维度计数**\n\"four independent validation axes (three architectures, one domain)\" → \"five independent validation axes (three architectures, one scale, one domain)\"\n\n**验证**：修复后执行：\n```bash\ngrep -in \"mauve\\|MAUVE\" docs/paper/experiments.tex\ngrep -n \"single seed\" docs/paper/experiments.tex\ngrep -n \"four independent\" docs/paper/experiments.tex\n```\n确认无残留。直接在当前 session 完成。"
}
````

---


### Runtime record

_source line 1290 · 2026-05-18T12:57:42.845Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T12:57:42.845Z",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35"
}
```

---


## Round 143

## Round 143

2 recorded events


### User

_source line 1291 · 2026-05-18T12:57:42.837Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fa6dc3e-9cdc-44ef-b33d-7006eddd4213",
  "isSidechain": false,
  "promptId": "f695f863-de11-482a-a067-372494e195a9",
  "type": "user",
  "isMeta": true,
  "uuid": "1603b703-0747-4fdc-9534-de08081f33ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

</details>

---


### Assistant

_source line 1292 · 2026-05-18T12:57:42.837Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1603b703-0747-4fdc-9534-de08081f33ac",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "54c5b739-bf5e-4cb1-95c8-12602b62fc22",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "id": "65ab4a3e-1802-4515-90c3-b93ff805adf7",
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


## Round 144

## Round 144

6 recorded events


### User

_source line 1293 · 2026-05-18T12:57:42.949Z_

[Director 指令] **Table 7 数字已确认，但 3 处残留错误需立即修复**

编辑 `docs/paper/experiments.tex`：

**a) CRITICAL — Domain 段 L381-383 重写**
删除以下内容（或附近等价文本）：
> "We exclude perplexity as a downstream variable in the C4 setting: its exponential divergence (20.6→1682.6, ADF statistic +1.07) violates the stationarity assumption..."
> "Instead, we use bounded diversity metrics (distinct-$n$, MAUVE) which remain well-behaved under differencing."

替换为：C4 使用与其他条件相同的 8 对 downstream（{token_entropy, ECE} × {d1, d2, d3, ppl}）。可以保留 perplexity 在 C4 域的极端 divergence 作为观察（ppl +50× 比 Pythia 更极端），但不能说"排除"。删除所有 MAUVE 引用。

**b) WARNING — L337 seed 描述**
"All conditions use α=1.0 and a single seed." → "All conditions use α=1.0. Architecture conditions use a single seed (s42); Scale and Domain conditions include two seeds (s42, s43)."

**c) WARNING — 验证维度计数**
"four independent validation axes (three architectures, one domain)" → "five independent validation axes (three architectures, one scale, one domain)"

**验证**：修复后执行：
```bash
grep -in "mauve\|MAUVE" docs/paper/experiments.tex
grep -n "single seed" docs/paper/experiments.tex
grep -n "four independent" docs/paper/experiments.tex
```
确认无残留。直接在当前 session 完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54c5b739-bf5e-4cb1-95c8-12602b62fc22",
  "isSidechain": false,
  "promptId": "f695f863-de11-482a-a067-372494e195a9",
  "type": "user",
  "uuid": "64f9f4f1-9803-4cb9-850e-2a080848ba92",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

</details>

---


### Runtime record

_source line 1294 · 2026-05-18T12:57:42.949Z_

```json
{
  "parentUuid": "64f9f4f1-9803-4cb9-850e-2a080848ba92",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a79c874f-66c4-4207-99e2-60a879c17981",
  "timestamp": "2026-05-18T12:57:42.949Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

---


### Assistant

_source line 1295 · 2026-05-18T12:58:05.326Z_

<details><summary>Logged reasoning block</summary>

```text
The Director wants me to fix 3 remaining errors in experiments.tex. Let me re-read the relevant sections to find the exact text that needs to be edited.

Let me identify the specific locations:

1. **a) Domain paragraph L381-383** - Need to find the text about excluding perplexity in C4 setting and MAUVE references
2. **b) L337 seed description** - Line 335 says "All conditions use $\alpha{=}1.0$ and a single seed."
3. **c) validation axes count** - Need to find "four independent"


I'm checking my previous read of the file against what the Director mentioned. The file appears to end at line 382 with a commented section, but the Director references L381-383 for the Domain paragraph, which suggests there might be content I need to locate more carefully or the line numbers have shifted. I'm noticing a discrepancy between what I read in the file and what the Director is referencing. The file I pulled shows Table 7 still has the original incorrect data, but the Director's message indicates those numbers have already been confirmed and fixed. This suggests either the file has been updated since my read, or I'm looking at a stale version. Let me pull the file again to see the current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a79c874f-66c4-4207-99e2-60a879c17981",
  "isSidechain": false,
  "requestId": "req_011CbA5BL4FGXXsg1xMMf8U5",
  "type": "assistant",
  "uuid": "cabbb462-b6c9-4dca-bb0d-712151a945d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EeRohBLVoJrfgmJJMgGtyZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1285,
      "cache_read_input_tokens": 60879,
      "output_tokens": 1038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1038,
          "cache_read_input_tokens": 60879,
          "cache_creation_input_tokens": 1285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1285
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

_source line 1296 · 2026-05-18T12:58:05.584Z_

先重新读取文件当前状态，确认 Table 7 已更新后定位三处残留错误。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cabbb462-b6c9-4dca-bb0d-712151a945d6",
  "isSidechain": false,
  "requestId": "req_011CbA5BL4FGXXsg1xMMf8U5",
  "type": "assistant",
  "uuid": "59ab9a55-7f56-4920-ba58-6a5f2cddd5e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EeRohBLVoJrfgmJJMgGtyZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1285,
      "cache_read_input_tokens": 60879,
      "output_tokens": 1038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1038,
          "cache_read_input_tokens": 60879,
          "cache_creation_input_tokens": 1285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1285
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

_source line 1297 · 2026-05-18T12:58:07.014Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YBKb56iHMmxPi4KrYsWDKN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
  "offset": 328
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59ab9a55-7f56-4920-ba58-6a5f2cddd5e2",
  "isSidechain": false,
  "requestId": "req_011CbA5BL4FGXXsg1xMMf8U5",
  "type": "assistant",
  "uuid": "fbfd358e-9b8a-45d2-9535-352ee9ec0459",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EeRohBLVoJrfgmJJMgGtyZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1285,
      "cache_read_input_tokens": 60879,
      "output_tokens": 1038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1038,
          "cache_read_input_tokens": 60879,
          "cache_creation_input_tokens": 1285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1285
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

_source line 1298 · 2026-05-18T12:58:07.025Z_

<details><summary>↩ Tool result · `toolu_01YBKb56iHMmxPi4KrYsWDKN`</summary>

```text
328	
329	
330	\subsection{Cross-Architecture, Cross-Scale, and Cross-Domain Generalization}
331	\label{sec:generalization}
332	
333	The methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).
334	To test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).
335	All conditions use $\alpha{=}1.0$ and a single seed.
336	
337	\begin{table}[t]
338	\centering
339	\small
340	\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\alpha{=}1.0$, single seed per condition). Each cell reports the fraction of canary$\to$downstream pairs reaching BH-corrected FDR significance ($q{=}0.05$): 8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded). \textbf{[TBD]}: experiments in progress.}
341	\label{tab:generalization}
342	\begin{tabular}{llccccccc}
343	\toprule
344	Variation & Model / Dataset & \rotatebox{70}{Naive} & \rotatebox{70}{Diff.\ XCorr} & \rotatebox{70}{Threshold} & \rotatebox{70}{PermG (fwd)} & \rotatebox{70}{PermG (rev)} & \rotatebox{70}{TY} & \rotatebox{70}{$K{\geq}4/5$} \\
345	\midrule
346	Baseline      & Pythia-410M / Wiki    & 7/8 & 6/8 & 6/8 & 6/8 & 0/8 & 6/8 & 6/8 \\
347	Architecture  & GPT-2-medium / Wiki   & 6/6 & 6/6 & 6/6 & 6/6 & 0/6 & 0/6 & 6/6 \\
348	Architecture  & OPT-1.3B / Wiki       & 6/8 & 6/8 & 8/8 & 6/8 & 0/8 & 2/8 & 6/8 \\
349	Scale ($3.4\times$) & Pythia-1.4B / Wiki & \multicolumn{7}{c}{\textbf{[TBD]}} \\
350	Domain        & Pythia-1B / C4        & \multicolumn{7}{c}{\textbf{[TBD]}} \\
351	\bottomrule
352	\end{tabular}
353	\end{table}
354	
355	\paragraph{Architecture generalization.}
356	Table~\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.
357	All models reach Tier~3 consensus ($K{\geq}4/5$) with 6/8 (or 6/6) canary$\to$diversity pairs confirmed.
358	Permutation Granger directionality is perfect across architectures: all forward-direction pairs are FDR-significant while 0 reverse-direction pairs reach significance in any architecture.
359	
360	Method-level variation across architectures is informative.
361	Threshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\to$1 discontinuity that cleanly exceeds the onset threshold.
362	Toda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\S\ref{sec:consensus_validation}).
363	Despite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\geq}4/5$.
364	
365	% [PLACEHOLDER — activate when Pythia-1.4B and Pythia-1B/C4 results arrive]
366	% \paragraph{Scale and domain generalization.}
367	% Scaling from 410M to 1.4B parameters within the Pythia family (3.4$\times$)
368	% preserves the core pattern: permutation Granger identifies \textbf{XX}/8
369	% forward-direction pairs with 0/8 reverse, and consensus $K{\geq}4/5$
370	% yields \textbf{XX}/8 (Table~\ref{tab:generalization}).
371	% This confirms that the methodological pitfalls are not artifacts of
372	% small-model capacity limitations, since the same consensus threshold
373	% operates identically at 3.4$\times$ the parameter count.
374	%
375	% Replacing WikiText-103 with C4 tests whether the lead-lag pattern
376	% depends on the training data distribution. Pythia-1B on C4 yields
377	% \textbf{XX}/8 forward-direction permutation Granger pairs with
378	% \textbf{XX}/8 reverse, and consensus $K{\geq}4/5$ at \textbf{XX}/8.
379	% Together with the architecture results, this establishes five
380	% independent validation lines (three architectures, one scale, one
381	% domain) converging on the same conclusion: token entropy
382	% Granger-precedes diversity collapse at $\alpha{=}1.0$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbfd358e-9b8a-45d2-9535-352ee9ec0459",
  "isSidechain": false,
  "promptId": "f695f863-de11-482a-a067-372494e195a9",
  "type": "user",
  "uuid": "79c0a174-f93e-4500-9fa9-1f7009d030e8",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
      "content": "\n\n\\subsection{Cross-Architecture, Cross-Scale, and Cross-Domain Generalization}\n\\label{sec:generalization}\n\nThe methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).\nTo test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).\nAll conditions use $\\alpha{=}1.0$ and a single seed.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\\alpha{=}1.0$, single seed per condition). Each cell reports the fraction of canary$\\to$downstream pairs reaching BH-corrected FDR significance ($q{=}0.05$): 8~pairs for Pythia models and OPT-1.3B, 6~pairs for GPT-2-medium (MAUVE excluded). \\textbf{[TBD]}: experiments in progress.}\n\\label{tab:generalization}\n\\begin{tabular}{llccccccc}\n\\toprule\nVariation & Model / Dataset & \\rotatebox{70}{Naive} & \\rotatebox{70}{Diff.\\ XCorr} & \\rotatebox{70}{Threshold} & \\rotatebox{70}{PermG (fwd)} & \\rotatebox{70}{PermG (rev)} & \\rotatebox{70}{TY} & \\rotatebox{70}{$K{\\geq}4/5$} \\\\\n\\midrule\nBaseline      & Pythia-410M / Wiki    & 7/8 & 6/8 & 6/8 & 6/8 & 0/8 & 6/8 & 6/8 \\\\\nArchitecture  & GPT-2-medium / Wiki   & 6/6 & 6/6 & 6/6 & 6/6 & 0/6 & 0/6 & 6/6 \\\\\nArchitecture  & OPT-1.3B / Wiki       & 6/8 & 6/8 & 8/8 & 6/8 & 0/8 & 2/8 & 6/8 \\\\\nScale ($3.4\\times$) & Pythia-1.4B / Wiki & \\multicolumn{7}{c}{\\textbf{[TBD]}} \\\\\nDomain        & Pythia-1B / C4        & \\multicolumn{7}{c}{\\textbf{[TBD]}} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Architecture generalization.}\nTable~\\ref{tab:generalization} confirms that the entropy-leads-diversity pattern generalizes across all three decoder-only transformer families tested to date.\nAll models reach Tier~3 consensus ($K{\\geq}4/5$) with 6/8 (or 6/6) canary$\\to$diversity pairs confirmed.\nPermutation Granger directionality is perfect across architectures: all forward-direction pairs are FDR-significant while 0 reverse-direction pairs reach significance in any architecture.\n\nMethod-level variation across architectures is informative.\nThreshold onset detection reaches 8/8 on OPT-1.3B (the highest single-method score) because OPT's token entropy exhibits a pronounced generation-0$\\to$1 discontinuity that cleanly exceeds the onset threshold.\nToda--Yamamoto ranges from 0/6 (GPT-2-medium) to 6/8 (Pythia-410M), consistent with its known sensitivity to residual degrees of freedom at short series lengths (\\S\\ref{sec:consensus_validation}).\nDespite this cross-method variance, the consensus threshold absorbs it: all three architectures converge at $K{\\geq}4/5$.\n\n% [PLACEHOLDER — activate when Pythia-1.4B and Pythia-1B/C4 results arrive]\n% \\paragraph{Scale and domain generalization.}\n% Scaling from 410M to 1.4B parameters within the Pythia family (3.4$\\times$)\n% preserves the core pattern: permutation Granger identifies \\textbf{XX}/8\n% forward-direction pairs with 0/8 reverse, and consensus $K{\\geq}4/5$\n% yields \\textbf{XX}/8 (Table~\\ref{tab:generalization}).\n% This confirms that the methodological pitfalls are not artifacts of\n% small-model capacity limitations, since the same consensus threshold\n% operates identically at 3.4$\\times$ the parameter count.\n%\n% Replacing WikiText-103 with C4 tests whether the lead-lag pattern\n% depends on the training data distribution. Pythia-1B on C4 yields\n% \\textbf{XX}/8 forward-direction permutation Granger pairs with\n% \\textbf{XX}/8 reverse, and consensus $K{\\geq}4/5$ at \\textbf{XX}/8.\n% Together with the architecture results, this establishes five\n% independent validation lines (three architectures, one scale, one\n% domain) converging on the same conclusion: token entropy\n% Granger-precedes diversity collapse at $\\alpha{=}1.0$.",
      "numLines": 55,
      "startLine": 328,
      "totalLines": 382
    }
  },
  "sourceToolAssistantUUID": "fbfd358e-9b8a-45d2-9535-352ee9ec0459",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/agent_069782ef",
  "sessionId": "26354fff-825d-4709-85fd-1f95e9631e35",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "floating-kindling-porcupine"
}
```

</details>

---
