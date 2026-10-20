# Research conversation: In /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/, I need to find where the planned experi

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a35a40d5f6dfb18b5.jsonl`
- **Structured JSON:** [`6b422f95fab63a9136f4.json`](../../sessions/6b/6b422f95fab63a9136f4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-13T08:30:58.536Z_

In /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/, I need to find where the planned experiments are defined. The experiment_plan.yaml is empty. Look for:
1. ROADMAP.md - read it fully for experiment plan details
2. Any files with "plan_004", "plan_005", "plan_006" etc.
3. Any YAML/MD files that define what experiments are planned (not completed)
4. The dream report files in artifacts/dream_reports/ - especially any imagined_experiments.yaml files
5. Any file mentioning "Qwen ACDC" or "phase2" plans

Read the full contents of the most relevant files. I need to know what experiments are PLANNED (not yet done) and their plan_ids.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "agentId": "a35a40d5f6dfb18b5",
  "type": "user",
  "uuid": "b420a815-9623-4087-afa9-594cd4ba254f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-13T08:31:01.444Z_

I'll help you find the planned experiments in the structfuse-context project. Let me start by exploring the directory structure and searching for the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b420a815-9623-4087-afa9-594cd4ba254f",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFnzmm5WkdjFkqmhP7G",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aad65cfd-6ef4-48c6-a332-09ca3d437b40",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018BvNgnmoZhryPpyBVkz6zG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 13807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 610,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 3 · 2026-05-13T08:31:01.862Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KPKvDrAWPJm4SNFd7Ji3iK`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ -type f -name \"*.md\" -o -name \"*.yaml\" | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aad65cfd-6ef4-48c6-a332-09ca3d437b40",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFnzmm5WkdjFkqmhP7G",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a0528dea-32af-41d7-a090-eceb9df6bdf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018BvNgnmoZhryPpyBVkz6zG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 13807,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 610
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 134,
          "cache_read_input_tokens": 13807,
          "cache_creation_input_tokens": 610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 610,
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

_source line 4 · 2026-05-13T08:31:02.054Z_

<details><summary>↩ Tool result · `toolu_01KPKvDrAWPJm4SNFd7Ji3iK`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/task_context/agent.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/task_context/director.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/task_context/reviewer.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/task_context/history/director/loop_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/task_context/history/agent/loop_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/task_context/history/reviewer/loop_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/task_context/history/reviewer/loop_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/sessions/director_df679b87/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/sessions/director_df679b87/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/sessions/agent_7e74ce9e/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/sessions/agent_7e74ce9e/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/sessions/agent_1f8a7b5e/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/sessions/agent_1f8a7b5e/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/sessions/reviewer_2ef08c26/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/sessions/reviewer_2ef08c26/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/.claude/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/literature_jaccard_overlap.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/data/phase2_configs.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_jaccard_overlap.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/LARGE_MODEL_THIRD_METHOD.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/related_work_notes_114feb.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/edge_pruning_precheck_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/literature_survey_related_work.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/ifr_code_survey.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/report/related_work_notes.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/best/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/D020_acdc_edge_selection.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/phase2_configs.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/mvp_pilot_gpt2_ioi_v3/report/D020_acdc_edge_selection.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/mvp_arithmetic_gpt2_k3/report/acdc_topk_sweep_results.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/mvp_arithmetic_gpt2_k3/report/mvp_gate_checklist_d025.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0528dea-32af-41d7-a090-eceb9df6bdf0",
  "isSidechain": true,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "agentId": "a35a40d5f6dfb18b5",
  "type": "user",
  "uuid": "c88f5d76-5730-4166-af7e-bf08b0cf5176",
  "sourceToolAssistantUUID": "a0528dea-32af-41d7-a090-eceb9df6bdf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-13T08:31:03.543Z_

Now let me look for ROADMAP.md, phase2_configs, and the imagined_experiments files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c88f5d76-5730-4166-af7e-bf08b0cf5176",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFoFqd9PMt34QpNrgoM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e2ae7a6c-a33a-4004-a9a1-ed052bb9f0bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EJE1gcWaY7N9GVTCADbBj6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3149,
      "cache_read_input_tokens": 14417,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3149,
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

_source line 6 · 2026-05-13T08:31:03.774Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KwxG7kZT6BVKxWAr1e1rK1`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ -type f -name \"ROADMAP*\" -o -name \"*plan_00*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2ae7a6c-a33a-4004-a9a1-ed052bb9f0bd",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFoFqd9PMt34QpNrgoM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8ad99a9f-fce6-4120-900f-e98a466c9dba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EJE1gcWaY7N9GVTCADbBj6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 3149,
      "cache_read_input_tokens": 14417,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3149
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 126,
          "cache_read_input_tokens": 14417,
          "cache_creation_input_tokens": 3149,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3149,
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

_source line 7 · 2026-05-13T08:31:03.838Z_

<details><summary>↩ Tool result · `toolu_01KwxG7kZT6BVKxWAr1e1rK1`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ROADMAP.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ROADMAP.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ad99a9f-fce6-4120-900f-e98a466c9dba",
  "isSidechain": true,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "agentId": "a35a40d5f6dfb18b5",
  "type": "user",
  "uuid": "d35c347e-d39c-4e7c-842a-afa04d48be99",
  "sourceToolAssistantUUID": "8ad99a9f-fce6-4120-900f-e98a466c9dba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-13T08:31:04.937Z_

Great! Let me read the key files: ROADMAP.md, phase2_configs.yaml, and the imagined_experiments.yaml files from the dream reports.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d35c347e-d39c-4e7c-842a-afa04d48be99",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFoPRXmYL4okomSMLPT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1381f468-e7ca-492d-bfeb-041e8f2eb18f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F4P5kr9BsT3mQ48PUeZnRB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 17566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 204,
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

_source line 9 · 2026-05-13T08:31:05.393Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K9y8qYMkAsqv1eZMDEMntR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1381f468-e7ca-492d-bfeb-041e8f2eb18f",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFoPRXmYL4okomSMLPT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b9d79304-82bd-455a-be47-48882c97ba4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F4P5kr9BsT3mQ48PUeZnRB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 17566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 204,
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

_source line 10 · 2026-05-13T08:31:05.399Z_

<details><summary>↩ Tool result · `toolu_01K9y8qYMkAsqv1eZMDEMntR`</summary>

```text
1	# structfuse-context — Research Dashboard
2	
3	> 最后更新: 2026-05-13 UTC | 更新原因: 更新当前进展与近期任务（IOI PASS_MAIN, Arithmetic 运行中）
4	
5	## 核心方向
6	跨方法二值共识（CSS）用于鲁棒电路编辑：证明 binary stability scoring + family-agreement constraint 在分布偏移下优于 score averaging 和单方法电路。
7	
8	## 当前进展
9	- **阶段**: MVP 验证 — IOI 已 PASS_MAIN（off-diagonal 13.3%），Arithmetic 确认实验运行中
10	- **核心假设**: CSS off-diagonal ≥5%（D021 CSS-only gate，D024 覆盖 D002）
11	- **基础设施**: cqa1-21977 (cuda:5, RTX 4090D) 已配置
12	- **大模型方案已定 (D006)**: IFR 作为第三方法，triangulation 框架定位
13	- **目标**: EMNLP 2026 Main（ARR deadline 2026-05-25，剩余 12 天）
14	
15	## 方法配置
16	| 模型 | K | 方法 | 算法族 |
17	|------|---|------|--------|
18	| GPT-2 Small | 3 | EAP-IG + Edge Pruning + ACDC | gradient / mask / greedy causal |
19	| Qwen-2.5 0.5B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |
20	| Gemma-2 2B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |
21	| Llama-3.1 8B | 3 | EAP-IG + Edge Pruning + IFR | gradient / mask / similarity |
22	
23	论文需披露：GPT-2 Small CSS = 3 因果方法共识；大模型 CSS = 2 因果 + 1 相似度方法共识（triangulation）。
24	
25	## MVP Gate 规则（D001-D003）
26	| off-diagonal % | 决策 |
27	|---|---|
28	| ≥10% | → Main track |
29	| 5-10% | → Findings + 追加 Arithmetic 验证 |
30	| 2-5% | → Findings 确认 |
31	| <2% (两组) + ΔF 无差异 | → Kill |
32	
33	## 阶段规划
34	
35	### Phase 1: MVP pilot（当前）
36	- GPT-2 Small / IOI，K=3（3 因果族），~2h → off-diagonal 判定
37	
38	### Phase 2: K=3 checkpoint + 全量 CSS（MVP 后 ~3天）
39	- Qwen-2.5 0.5B / IOI K=3（含 IFR）快速检查
40	- 全 4 模型 × 4 任务 CSS 计算
41	- 确认 Edge Pruning 实现：princeton-nlp/edge-pruning（非 auto-circuit mask gradient）
42	
43	### Phase 3: OOD editing（~4天）
44	### Phase 4: 分析 + 写作（~3天，最迟 5月22日）
45	
46	## 近期任务
47	- [ ] 等待 mvp_arithmetic_gpt2_k3 完成 → gate 判定
48	- [ ] Gate PASS 后 complete_mvp → 进入 research
49	- [ ] 写 paper_framing.md + experiment_plan.yaml
50	- [ ] 部署 IFR + Phase 2 实验脚本到服务器
51	- [ ] 下载目标模型（Qwen-2.5 0.5B 优先）
52	
53	## GPU 预算
54	- 已分配: 1× RTX 4090D (cuda:5@cqa1-21977)
55	- MVP: ~2h | 全量: ~290h A100（需后续扩卡）
56	
57	## 关键决策日志
58	
59	| ID | 日期 | 摘要 | 关联实验 |
60	|----|------|------|----------|
61	| D033 | 2026-05-13 | D033: SVA 判定降级为 inconclusive——单 seed Δ=0.013 不具鲁棒性 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |
62	| D032 | 2026-05-13 | D032: 条件④评估指标修正——必须用 css_1.00 而非 css_0.67 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |
63	| D031 | 2026-05-13 | 统一 D025 条件④标准：zero PASS 或 mean Δ≥0.01，SVA 两次均判 neg | mvp_sva_gpt2_k3, mvp_sva_gpt2_k3_topk |
64	| D030 | 2026-05-13 | SVA D025 gate FAIL（zero FAIL / mean 边际 Δ=0.008）；发现 | mvp_sva_gpt2_k3_topk |
65	| D029 | 2026-05-13 | Phase 2 第三方法：放弃 IFR，改用 ACDC top-k。IFR 跨族分歧作为 Discu | phase2_qwen05b_ioi_k3 |
66	| D028 | 2026-05-13 | Phase 2 IFR 零重叠问题：暂停 Qwen/Gemma 新实验，先修 IFR per-hea | phase2_qwen05b_ioi_k3 |
67	| D027 | 2026-05-13 | MVP 最终判定：CSS faithfulness 优势 task-dependent（IOI PA | mvp_arithmetic_gpt2_k3, mvp_pilot_gpt2_ioi_v3 |
68	| D026 | 2026-05-13 | Arithmetic D025 gate FAIL（条件④），暂不判 MVP 结果，先做 ACDC  | mvp_arithmetic_gpt2_k3 |
69	| D025 | 2026-05-13 | 更新 Arithmetic gate 为 CSS-only 四条件标准（替代 D024 的单一 5% | mvp_arithmetic_gpt2_k3 |
70	| D024 | 2026-05-13 | D021 覆盖 D002 灰区定义：arithmetic CSS off-diagonal ≥5%  | — |
71	
72	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9d79304-82bd-455a-be47-48882c97ba4e",
  "isSidechain": true,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "agentId": "a35a40d5f6dfb18b5",
  "type": "user",
  "uuid": "9471163c-74d1-4588-bf08-47c4eab3b13b",
  "sourceToolAssistantUUID": "b9d79304-82bd-455a-be47-48882c97ba4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T08:31:05.605Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TddbCegN88qBwBiGmR6ZF6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/phase2_configs.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9471163c-74d1-4588-bf08-47c4eab3b13b",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFoPRXmYL4okomSMLPT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f22890f8-aad1-42c6-ac4b-e4ee854a1ebd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F4P5kr9BsT3mQ48PUeZnRB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 17566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 204,
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

_source line 12 · 2026-05-13T08:31:05.612Z_

<details><summary>↩ Tool result · `toolu_01TddbCegN88qBwBiGmR6ZF6`</summary>

```text
1	# Phase 2 实验矩阵
2	# 每个实验 = 一个 model × task × methods 组合
3	#
4	# Priority: 1 = MVP 已在跑, 2 = MVP 后立即跑, 3 = 有空再跑
5	# Backend: transformerlens (GPT-2) | huggingface (其他)
6	# Methods: GPT-2 用 ACDC, 大模型用 IFR (D006)
7	#
8	# 预估单实验耗时（基于 MVP 经验）:
9	#   GPT-2 Small:  EAP-IG ~2min, EP ~5min, ACDC TBD - 待 v3 实际数据更新  → ~20min/task
10	#   Qwen-2.5 0.5B: EAP-IG ~5min, EP ~15min, IFR ~3min → ~25min/task
11	#   Gemma-2 2B:   EAP-IG ~15min, EP ~40min, IFR ~8min  → ~65min/task
12	#   Llama-3.1 8B: EAP-IG ~40min, EP ~90min, IFR ~15min → ~150min/task
13	
14	defaults:
15	  K: 3
16	  num_samples: 50
17	  seed: 42
18	  gpu_id: "5"
19	  eap_ig_steps: 5
20	  edge_pruning_epochs: 100
21	  edge_pruning_lambda: 1e-2
22	  ifr_threshold: 0.1
23	  css_threshold: 0.67
24	  circus_B: 10
25	
26	experiments:
27	
28	  # ===================================================================
29	  # GPT-2 Small — TransformerLens, K=3 causal methods (EAP-IG + EP + ACDC)
30	  # 预估总耗时: ~60min (3 tasks × ~20min)
31	  # ===================================================================
32	
33	  gpt2_ioi:
34	    model: "gpt2"
35	    model_path: null
36	    task: "ioi"
37	    methods: ["eap_ig", "edge_pruning", "acdc"]
38	    backend: "transformerlens"
39	    thresholds:
40	      acdc: [0.01, 0.03, 0.05, 0.1, 0.3]
41	    binarize:
42	      eap_ig: {strategy: "topn", n: 200}
43	      edge_pruning: {strategy: "threshold", t: 0.5}
44	      acdc: {strategy: "threshold", threshold: 0.05}
45	    priority: 1
46	    notes: "MVP baseline, 已有部分结果"
47	
48	  gpt2_greater_than:
49	    model: "gpt2"
50	    model_path: null
51	    task: "greater_than"
52	    methods: ["eap_ig", "edge_pruning", "acdc"]
53	    backend: "transformerlens"
54	    thresholds:
55	      acdc: [0.01, 0.03, 0.05, 0.1, 0.3]
56	    binarize:
57	      eap_ig: {strategy: "topn", n: 200}
58	      edge_pruning: {strategy: "threshold", t: 0.5}
59	      acdc: {strategy: "threshold", threshold: 0.05}
60	    priority: 2
61	    notes: "数值推理任务, 预期电路更紧凑"
62	
63	  gpt2_docstring:
64	    model: "gpt2"
65	    model_path: null
66	    task: "docstring"
67	    methods: ["eap_ig", "edge_pruning", "acdc"]
68	    backend: "transformerlens"
69	    thresholds:
70	      acdc: [0.01, 0.03, 0.05, 0.1, 0.3]
71	    binarize:
72	      eap_ig: {strategy: "topn", n: 200}
73	      edge_pruning: {strategy: "threshold", t: 0.5}
74	      acdc: {strategy: "threshold", threshold: 0.05}
75	    priority: 2
76	    notes: "代码理解任务, 验证跨领域泛化"
77	
78	  # ===================================================================
79	  # Qwen-2.5 0.5B — HuggingFace, K=3 (EAP-IG + EP + IFR)
80	  # 预估总耗时: ~100min (4 tasks × ~25min)
81	  # ===================================================================
82	
83	  qwen05_ioi:
84	    model: "Qwen/Qwen2.5-0.5B"
85	    model_path: "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/"
86	    task: "ioi"
87	    methods: ["eap_ig", "edge_pruning", "ifr"]
88	    backend: "huggingface"
89	    binarize:
90	      eap_ig: {strategy: "topn", n: 200}
91	      edge_pruning: {strategy: "threshold", t: 0.5}
92	      ifr: {strategy: "unique_score_rank", n: 50}
93	    priority: 2
94	    notes: "Phase 2 首个大模型实验, MVP 后立即跑"
95	
96	  qwen05_greater_than:
97	    model: "Qwen/Qwen2.5-0.5B"
98	    model_path: "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/"
99	    task: "greater_than"
100	    methods: ["eap_ig", "edge_pruning", "ifr"]
101	    backend: "huggingface"
102	    binarize:
103	      eap_ig: {strategy: "topn", n: 200}
104	      edge_pruning: {strategy: "threshold", t: 0.5}
105	      ifr: {strategy: "unique_score_rank", n: 50}
106	    priority: 2
107	    notes: "Qwen 数值推理"
108	
109	  qwen05_docstring:
110	    model: "Qwen/Qwen2.5-0.5B"
111	    model_path: "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/"
112	    task: "docstring"
113	    methods: ["eap_ig", "edge_pruning", "ifr"]
114	    backend: "huggingface"
115	    binarize:
116	      eap_ig: {strategy: "topn", n: 200}
117	      edge_pruning: {strategy: "threshold", t: 0.5}
118	      ifr: {strategy: "unique_score_rank", n: 50}
119	    priority: 2
120	    notes: "Qwen 代码理解"
121	
122	  qwen05_ioi_variant:
123	    model: "Qwen/Qwen2.5-0.5B"
124	    model_path: "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/"
125	    task: "ioi_variant"
126	    methods: ["eap_ig", "edge_pruning", "ifr"]
127	    backend: "huggingface"
128	    binarize:
129	      eap_ig: {strategy: "topn", n: 200}
130	      edge_pruning: {strategy: "threshold", t: 0.5}
131	      ifr: {strategy: "unique_score_rank", n: 50}
132	    priority: 3
133	    notes: "IOI 变体 (name permutation), 验证电路稳定性"
134	
135	  # ===================================================================
136	  # Gemma-2 2B — HuggingFace, K=3 (EAP-IG + EP + IFR)
137	  # 预估总耗时: ~260min (4 tasks × ~65min)
138	  # ===================================================================
139	
140	  gemma2_ioi:
141	    model: "google/gemma-2-2b"
142	    model_path: "/root/autodl-tmp/.hf_cache/google/gemma-2-2b/"
143	    task: "ioi"
144	    methods: ["eap_ig", "edge_pruning", "ifr"]
145	    backend: "huggingface"
146	    num_samples: 30
147	    edge_pruning_epochs: 80
148	    binarize:
149	      eap_ig: {strategy: "topn", n: 200}
150	      edge_pruning: {strategy: "threshold", t: 0.5}
151	      ifr: {strategy: "unique_score_rank", n: 50}
152	    priority: 3
153	    notes: "2B 模型, 减 samples 和 EP epochs 控制显存"
154	
155	  gemma2_greater_than:
156	    model: "google/gemma-2-2b"
157	    model_path: "/root/autodl-tmp/.hf_cache/google/gemma-2-2b/"
158	    task: "greater_than"
159	    methods: ["eap_ig", "edge_pruning", "ifr"]
160	    backend: "huggingface"
161	    num_samples: 30
162	    edge_pruning_epochs: 80
163	    binarize:
164	      eap_ig: {strategy: "topn", n: 200}
165	      edge_pruning: {strategy: "threshold", t: 0.5}
166	      ifr: {strategy: "unique_score_rank", n: 50}
167	    priority: 3
168	    notes: "Gemma-2 数值推理"
169	
170	  gemma2_docstring:
171	    model: "google/gemma-2-2b"
172	    model_path: "/root/autodl-tmp/.hf_cache/google/gemma-2-2b/"
173	    task: "docstring"
174	    methods: ["eap_ig", "edge_pruning", "ifr"]
175	    backend: "huggingface"
176	    num_samples: 30
177	    edge_pruning_epochs: 80
178	    binarize:
179	      eap_ig: {strategy: "topn", n: 200}
180	      edge_pruning: {strategy: "threshold", t: 0.5}
181	      ifr: {strategy: "unique_score_rank", n: 50}
182	    priority: 3
183	    notes: "Gemma-2 代码理解"
184	
185	  gemma2_ioi_variant:
186	    model: "google/gemma-2-2b"
187	    model_path: "/root/autodl-tmp/.hf_cache/google/gemma-2-2b/"
188	    task: "ioi_variant"
189	    methods: ["eap_ig", "edge_pruning", "ifr"]
190	    backend: "huggingface"
191	    num_samples: 30
192	    edge_pruning_epochs: 80
193	    binarize:
194	      eap_ig: {strategy: "topn", n: 200}
195	      edge_pruning: {strategy: "threshold", t: 0.5}
196	      ifr: {strategy: "unique_score_rank", n: 50}
197	    priority: 3
198	    notes: "Gemma-2 IOI 变体"
199	
200	  # ===================================================================
201	  # Llama-3.1 8B — HuggingFace, K=3 (EAP-IG + EP + IFR)
202	  # 预估总耗时: ~600min (4 tasks × ~150min)
203	  # 需要 >=24GB VRAM (A6000), EP 可能需 gradient checkpointing
204	  # ===================================================================
205	
206	  llama31_ioi:
207	    model: "meta-llama/Llama-3.1-8B"
208	    model_path: "/root/autodl-tmp/.hf_cache/meta-llama/Llama-3.1-8B/"
209	    task: "ioi"
210	    methods: ["eap_ig", "edge_pruning", "ifr"]
211	    backend: "huggingface"
212	    num_samples: 20
213	    edge_pruning_epochs: 60
214	    edge_pruning_lambda: 5e-3
215	    binarize:
216	      eap_ig: {strategy: "topn", n: 200}
217	      edge_pruning: {strategy: "threshold", t: 0.5}
218	      ifr: {strategy: "unique_score_rank", n: 50}
219	    priority: 3
220	    notes: "8B 最大模型, 减 samples/epochs, 可能需 gradient checkpointing"
221	
222	  llama31_greater_than:
223	    model: "meta-llama/Llama-3.1-8B"
224	    model_path: "/root/autodl-tmp/.hf_cache/meta-llama/Llama-3.1-8B/"
225	    task: "greater_than"
226	    methods: ["eap_ig", "edge_pruning", "ifr"]
227	    backend: "huggingface"
228	    num_samples: 20
229	    edge_pruning_epochs: 60
230	    edge_pruning_lambda: 5e-3
231	    binarize:
232	      eap_ig: {strategy: "topn", n: 200}
233	      edge_pruning: {strategy: "threshold", t: 0.5}
234	      ifr: {strategy: "unique_score_rank", n: 50}
235	    priority: 3
236	    notes: "Llama-3.1 数值推理"
237	
238	  llama31_docstring:
239	    model: "meta-llama/Llama-3.1-8B"
240	    model_path: "/root/autodl-tmp/.hf_cache/meta-llama/Llama-3.1-8B/"
241	    task: "docstring"
242	    methods: ["eap_ig", "edge_pruning", "ifr"]
243	    backend: "huggingface"
244	    num_samples: 20
245	    edge_pruning_epochs: 60
246	    edge_pruning_lambda: 5e-3
247	    binarize:
248	      eap_ig: {strategy: "topn", n: 200}
249	      edge_pruning: {strategy: "threshold", t: 0.5}
250	      ifr: {strategy: "unique_score_rank", n: 50}
251	    priority: 3
252	    notes: "Llama-3.1 代码理解"
253	
254	  llama31_ioi_variant:
255	    model: "meta-llama/Llama-3.1-8B"
256	    model_path: "/root/autodl-tmp/.hf_cache/meta-llama/Llama-3.1-8B/"
257	    task: "ioi_variant"
258	    methods: ["eap_ig", "edge_pruning", "ifr"]
259	    backend: "huggingface"
260	    num_samples: 20
261	    edge_pruning_epochs: 60
262	    edge_pruning_lambda: 5e-3
263	    binarize:
264	      eap_ig: {strategy: "topn", n: 200}
265	      edge_pruning: {strategy: "threshold", t: 0.5}
266	      ifr: {strategy: "unique_score_rank", n: 50}
267	    priority: 3
268	    notes: "Llama-3.1 IOI 变体"
269	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f22890f8-aad1-42c6-ac4b-e4ee854a1ebd",
  "isSidechain": true,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "agentId": "a35a40d5f6dfb18b5",
  "type": "user",
  "uuid": "663366a4-2bfa-46e0-ac58-659e7df29c07",
  "sourceToolAssistantUUID": "f22890f8-aad1-42c6-ac4b-e4ee854a1ebd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T08:31:06.025Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M1sV9NbwVLRjEevVyZUoBw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/best/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "663366a4-2bfa-46e0-ac58-659e7df29c07",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFoPRXmYL4okomSMLPT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ff73aa68-366e-40ee-aeae-e2a7b83f70d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F4P5kr9BsT3mQ48PUeZnRB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 17566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 204,
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

_source line 14 · 2026-05-13T08:31:06.030Z_

<details><summary>↩ Tool result · `toolu_01M1sV9NbwVLRjEevVyZUoBw`</summary>

```text
1	tier: best
2	narrative_guidance: '原始 reframed claim 完整成立。四个任务（IOI、SVA、Factual Recall、Arithmetic）覆盖
3	  localized→distributed 全谱，Jaccard 作为 CSS utility 的 meta-diagnostic 是 novel 且 quantitatively
4	  validated 的 contribution。SVA 清晰复现 IOI 模式（低 Jaccard、CSS 优势显著）， Factual Recall 提供关键
5	  interpolation 数据点（中等 Jaccard、CSS 优势边际正），Arithmetic 作为 principled negative case 完善图景。IFR
6	  第四方法族在 Qwen 上进一步降低 max Jaccard， CSS=1.0 CPR 不退化甚至提升，直接回应 R3（K≈2 质疑）。Spearman ρ=0.94
7	  跨 6 个 model×task 组合成立，p=0.005，统计上无争议。论文叙事可以自信地以 Jaccard threshold (~0.55) 作为 practitioner
8	  guideline 收尾。
9	
10	  '
11	imagined_experiments:
12	- name: GPT-2 Small Subject-Verb Agreement K=3 CSS
13	  plan_id: plan_004
14	  description: '在 GPT-2 Small 上对 Subject-Verb Agreement (SVA) 任务运行三种发现方法 （EAP-IG,
15	    EP, ACDC），计算 CSS 分布和 faithfulness。SVA 是经典的 localized circuit 任务，核心计算集中在 layer
16	    7-10 的 number-tracking attention heads，预期方法间 Jaccard 低、CSS 优势显著。
17	
18	    '
19	  expected_results:
20	    eapig_edges: 50
21	    ep_edges: 50
22	    acdc_edges_isinf: 12
23	    acdc_edges_k50: 50
24	    jaccard_eapig_ep: 0.22
25	    jaccard_eapig_acdc: 0.08
26	    jaccard_ep_acdc: 0.06
27	    max_pairwise_jaccard: 0.22
28	    three_way_ratio: 0.032
29	    css_3of3_edges: 8
30	    css_2of3_edges: 31
31	    css_1of3_edges: 73
32	    css_1.00_edges: 8
33	    css_1.00_CPR: 0.12
34	    css_1.00_CMD: 0.89
35	    css_0.67_edges: 31
36	    css_0.67_CPR: 0.065
37	    css_0.67_CMD: 0.945
38	    acdc_edges: 12
39	    acdc_CPR: 0.03
40	    acdc_CMD: 0.975
41	    eapig_k50_CPR: -0.04
42	    eapig_k50_CMD: 1.05
43	    ep_k50_CPR: -0.07
44	    ep_k50_CMD: 1.08
45	    css1_cpr_advantage: 0.09
46	    css1_edge_ratio: 0.071
47	  result_rationale: 'SVA 在 GPT-2 Small 中依赖 layer 7-10 中约 5-8 个专门追踪主语数特征的 attention
48	    head。这是一个高度 localized 的电路：关键计算集中在少量 head 的 Q-K 匹配上。三种方法各自从不同角度发现该电路的不同子集——EAP-IG
49	    沿梯度 路径优先选取高 ∂L/∂e 的边，EP 通过逐步剪枝保留移除后损失最大的边，ACDC 通过激活差异识别 clean vs corrupt 下变化最大的边。由于电路
50	    localized，每种 方法只需少量边即可捕获核心功能，导致三组 top-50 edge set 的交集稀疏（max Jaccard=0.22）。CSS=1.0
51	    恰好捕获了所有三种方法共同认定的 8 条核心边—— 这些边对应 number-agreement 的关键 attention pattern，移除它们会破坏
52	    subject→verb 的 number propagation，因此 CPR=0.12 显著高于任何单方法。 ACDC 的 12 条 isinf 边虽然也
53	    localized，但包含了 4 条 ACDC 特有的 method-specific 边（其他方法未选中），导致部分噪声稀释了 faithfulness。
54	
55	    '
56	  tables:
57	  - name: 'Table: SVA Circuit Discovery Summary'
58	    description: '行: EAP-IG(k=50), EP(k=50), ACDC(isinf), CSS≥2/3, CSS=1.0 列: Edges,
59	      CPR, CMD, vs-best-single-Δ 展示 CSS=1.0 在仅 8 条边下达到 CPR=0.12，是 ACDC(0.03) 的 4 倍
60	
61	      '
62	  - name: 'Table: SVA Pairwise Jaccard Matrix'
63	    description: '3×3 对称矩阵，对角线为 1.0。EAP-IG×EP=0.22, EAP-IG×ACDC=0.08, EP×ACDC=0.06。与
64	      IOI 的 Jaccard 矩阵并列展示，突出 SVA 更低的 inter-method correlation
65	
66	      '
67	  figures_description:
68	  - 'Bar chart: x 轴为方法（EAP-IG, EP, ACDC, CSS≥2/3, CSS=1.0）， y 轴为 CPR。CSS=1.0 bar 显著高于其他所有方法，上方标注
69	    edge count。 与 IOI 对应图并列为 subplot，视觉化 CSS 优势在 localized tasks 上的复现
70	
71	    '
72	  analysis: 'SVA 完美复现 IOI 的核心模式：localized circuit → low Jaccard → CSS=1.0 faithfulness
73	    优势。max Jaccard 0.22 甚至低于 IOI 的 0.31，反映 SVA 电路更 集中（fewer critical heads），使方法分歧更大。CSS
74	    CPR advantage 0.09 与 IOI 的 0.08 一致，支撑 Claim 1。此结果将 Claim 1 的支持从 1 个任务扩展到 2 个，
75	    直接削弱 R1 泛化性质疑。
76	
77	    '
78	- name: GPT-2 Small Factual Recall K=3 CSS
79	  plan_id: plan_005
80	  description: '在 GPT-2 Small 上对 Factual Recall 任务（country→capital, e.g. "The capital
81	    of France is"）运行三种发现方法。这是一个 distributed computation 任务， 知识检索涉及多层 MLP 和跨层 attention
82	    routing，预期方法 Jaccard 中等， CSS 优势边际。
83	
84	    '
85	  expected_results:
86	    eapig_edges: 50
87	    ep_edges: 50
88	    acdc_edges_isinf: 22
89	    acdc_edges_k50: 50
90	    jaccard_eapig_ep: 0.48
91	    jaccard_eapig_acdc: 0.18
92	    jaccard_ep_acdc: 0.15
93	    max_pairwise_jaccard: 0.48
94	    three_way_ratio: 0.092
95	    css_3of3_edges: 15
96	    css_2of3_edges: 38
97	    css_1of3_edges: 69
98	    css_1.00_edges: 15
99	    css_1.00_CPR: 0.055
100	    css_1.00_CMD: 0.95
101	    css_0.67_edges: 38
102	    css_0.67_CPR: 0.04
103	    css_0.67_CMD: 0.965
104	    acdc_edges: 22
105	    acdc_CPR: 0.037
106	    acdc_CMD: 0.97
107	    eapig_k50_CPR: 0.03
108	    eapig_k50_CMD: 0.975
109	    ep_k50_CPR: 0.01
110	    ep_k50_CMD: 0.99
111	    css1_cpr_advantage: 0.018
112	    css1_edge_ratio: 0.123
113	  result_rationale: 'Factual recall 是一个 distributed computation：知识存储在中层 MLP（layer
114	    5-9） 的 key-value 机制中，而检索依赖多层 attention head 将 subject token 的 representation 路由到
115	    last token position。三种方法在 MLP 存储层的边上有较高 共识（这些边是任何方法都无法忽略的关键瓶颈），但在 attention routing
116	    边上 存在分歧——EAP-IG 偏好早期 attention head（梯度信号强），EP 保留后期 head （剪枝敏感），ACDC 选中的 head 分散在多层。这导致
117	    max Jaccard=0.48：高于 localized tasks（方法在核心 MLP 边上被迫共识），但远低于 Arithmetic（0.695） 因为
118	    routing 部分仍有显著分歧。CSS=1.0 的 15 条边捕获了 MLP 存储核心 + 最关键的 2-3 个 routing head，CPR=0.055
119	    略优于 ACDC(0.037)，但优势仅 0.018。 这符合理论预期：中等 Jaccard → 中等 CSS utility，consensus 的过滤效果被
120	    方法间部分冗余所稀释。
121	
122	    '
123	  tables:
124	  - name: 'Table: Factual Recall Circuit Discovery Summary'
125	    description: '格式同 SVA/IOI 表。CSS=1.0 的 15 条边 CPR=0.055 略优于 ACDC 的 22 条 边 CPR=0.037，但优势远小于
126	      IOI/SVA
127	
128	      '
129	  figures_description:
130	  - '与 IOI、SVA 的 CPR bar chart 并列的第三个 subplot。CSS=1.0 bar 仅略高于 ACDC bar，视觉化 CSS 优势随
131	    Jaccard 增加而递减的趋势
132	
133	    '
134	  analysis: 'Factual Recall 是论文叙事的关键 interpolation 点。它证明 CSS utility 不是 binary（有/无），而是连续的、可由
135	    Jaccard 预测的量。max Jaccard 0.48 落在 IOI(0.31) 和 Arithmetic(0.695) 之间，CSS advantage
136	    0.018 也相应落在 0.08 和 -0.066 之间。这将 Claim 2 从"两点定义的趋势"升级为"有中间插值的 连续关系"，显著增强说服力。同时，CSS=1.0
137	    的优势虽小但仍为正，使 n_tasks_css_wins 达到 3（IOI + SVA + Factual），满足 reviewer 对 majority-win
138	    的期望。
139	
140	    '
141	- name: Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + IFR)
142	  plan_id: plan_006
143	  description: '在 Qwen-2.5 0.5B 上运行 IOI，用 IFR（Iterative Feature Removal， similarity-based）替代
144	    ACDC，构成 K=3 = {EAP-IG, EP, IFR}。 IFR 来自不同算法族，预期降低 max Jaccard、维持或提升 CSS CPR。 同时验证
145	    CSS 跨模型架构（GQA, SwiGLU）的泛化性。
146	
147	    '
148	  expected_results:
149	    eapig_edges: 50
150	    ep_edges: 50
151	    ifr_edges: 50
152	    jaccard_eapig_ep: 0.28
153	    jaccard_eapig_ifr: 0.14
154	    jaccard_ep_ifr: 0.11
155	    max_pairwise_jaccard: 0.28
156	    css_3of3_edges: 10
157	    css_2of3_edges: 30
158	    css_1of3_edges: 82
159	    css_1.00_edges: 10
160	    css_1.00_CPR: 0.14
161	    css_1.00_CMD: 0.87
162	    css_0.67_edges: 30
163	    css_0.67_CPR: 0.08
164	    css_0.67_CMD: 0.93
165	    eapig_k50_CPR: 0.04
166	    ep_k50_CPR: 0.02
167	    ifr_k50_CPR: 0.05
168	    css1_cpr_advantage: 0.09
169	    max_jaccard_vs_gpt2_ioi: 0.28 ≤ 0.31 (GPT-2)
170	  result_rationale: 'IFR 通过逐步移除 feature 并测量 representation similarity 变化来评分边， 其算法逻辑与
171	    gradient-based EAP-IG 和 pruning-based EP 正交。在 Qwen 的 IOI 电路中，EAP-IG 和 EP 的 Jaccard
172	    从 GPT-2 的 0.31 降至 0.28——Qwen 的 GQA（Grouped Query Attention）使得 head 内 key-value
173	    sharing 改变了 gradient 和 pruning 的敏感度分布，两方法在 induction head 选择上出现更大 分歧。IFR 与 gradient
174	    方法的 Jaccard 极低（0.14/0.11），因为 similarity-based scoring 完全不依赖 loss gradient，而是基于
175	    intermediate representation 的 余弦距离变化。CSS=1.0 的 10 条边是三种完全不同的算法视角共同认定的 IOI 核心——name
176	    mover heads 和 S-inhibition heads 的关键边——CPR=0.14 不仅 不退化，反而高于 GPT-2 IOI 的 0.109。这验证了核心理论：方法多样性越高
177	    （更低 Jaccard），consensus 过滤越有效，CSS utility 越大。
178	
179	    '
180	  tables:
181	  - name: 'Table: Cross-Model IOI Comparison (GPT-2 vs Qwen)'
182	    description: '行: GPT-2 K=3(EAP-IG,EP,ACDC), Qwen K=3(EAP-IG,EP,IFR) 列: Max Jaccard,
183	      CSS=1.0 Edges, CSS=1.0 CPR, Best-Single CPR, Δ 突出 IFR 带来的 Jaccard 下降和 CPR 提升
184	
185	      '
186	  figures_description:
187	  - 'Paired bar chart: GPT-2 IOI vs Qwen IOI，每组有 CSS=1.0 和 best-single 两个 bar。Qwen
188	    的 CSS=1.0 bar 更高且与 best-single 的 gap 更大， 视觉化 method diversity → CSS utility 的因果链
189	
190	    '
191	  analysis: '此实验同时服务三个目标：(1) 验证 CSS 跨模型泛化（Qwen ≠ GPT-2 架构）， (2) 验证 IFR 作为第三算法族的加入降低
192	    Jaccard 并提升 CSS utility（直接回应 R3 的 K≈2 质疑），(3) 为 plan_013 提供第 5 个 Jaccard-CSS 数据点。
193	    max Jaccard 0.28 ≤ GPT-2 的 0.31，CSS CPR 0.14 > 0.109，两个指标同时 改善，是 best tier 最有力的单一证据。
194	
195	    '
196	- name: Qwen-2.5 0.5B Arithmetic K=3 (EAP-IG + EP + IFR)
197	  plan_id: plan_007
198	  description: 'Qwen 上运行 Arithmetic (Greaterthan)，IFR 替代 ACDC。测试 IFR 能否 打破 EAP-IG×EP
199	    的高 Jaccard 相关性、使 CSS 部分恢复。
200	
201	    '
202	  expected_results:
203	    jaccard_eapig_ep: 0.58
204	    jaccard_eapig_ifr: 0.28
205	    jaccard_ep_ifr: 0.24
206	    max_pairwise_jaccard: 0.58
207	    css_3of3_edges: 18
208	    css_2of3_edges: 35
209	    css_1of3_edges: 69
210	    css_1.00_CPR: 0.935
211	    eapig_k50_CPR: 0.975
212	    ep_k50_CPR: 0.95
213	    ifr_k50_CPR: 0.88
214	    css1_cpr_advantage: -0.04
215	  result_rationale: 'Arithmetic (Greaterthan) 的计算结构天然导致方法收敛：比较操作依赖一组固定的 comparison
216	    heads 和 magnitude-encoding MLPs，任何基于性能的方法都会被迫 选中这些瓶颈边。EAP-IG×EP 的 Jaccard 从 GPT-2
217	    的 0.695 降至 Qwen 的 0.58 ——Qwen 的更大模型容量和 GQA 结构使得 comparison 计算略微分散到更多 head， 降低了
218	    gradient-adjacent 的冗余。但 0.58 仍然远高于 CSS utility threshold (~0.55)。IFR 虽然作为不同族方法引入了新视角（IFR×EAP-IG=0.28），但
219	    max pairwise Jaccard 仍由 EAP-IG×EP=0.58 主导——CSS=1.0 的 filtering 效果被 两个 gradient-adjacent
220	    方法的高度共识所支配。CSS=1.0 CPR=0.935 低于 EAP-IG 的 0.975，确认 Arithmetic 在 Qwen 上仍是 CSS-negative
221	    case。 但 Jaccard 从 0.695 降至 0.58 提供了一个重要的 near-threshold 数据点， 说明 IFR 的加入确实在正确方向上推动了
222	    method diversity。
223	
224	    '
225	  tables:
226	  - name: 'Table: Arithmetic Cross-Model Comparison'
227	    description: 'GPT-2 K=3 vs Qwen K=3(with IFR)。突出 max Jaccard 从 0.695→0.58 的下降以及
228	      CSS advantage 从 -0.066 到 -0.04 的改善（趋势正确但未翻转）
229	
230	      '
231	  figures_description:
232	  - '在 Jaccard-CSS scatter plot 中，Qwen Arithmetic 的数据点落在 GPT-2 Arithmetic 的右上方（更高
233	    1-Jaccard，更小 negative advantage）， 视觉化 IFR 的正向但不充分的贡献
234	
235	    '
236	  analysis: '此实验的 negative result 实际上是论文叙事的资产而非负担。它证明：(1) Jaccard threshold 是稳健的——即使
237	    IFR 降低了 max Jaccard，只要仍高于 ~0.55， CSS 依然无效；(2) CSS utility 的 bottleneck 是 max pairwise
238	    Jaccard， 不是 average Jaccard——只要有一对方法高度相关，consensus 就会退化； (3) 为 Claim 2 提供了又一个符合预测的数据点（Spearman
239	    correlation 更稳健）。
240	
241	    '
242	- name: Gemma-2 2B IOI K=3 (EAP-IG + EP + IFR)
243	  plan_id: plan_008
244	  description: '将 CSS 扩展到 2B 参数量级模型。验证 localized circuit 模式在更大模型上是否 保持，以及 CSS faithfulness
245	    优势是否随模型规模 scale。
246	
247	    '
248	  expected_results:
249	    jaccard_eapig_ep: 0.25
250	    jaccard_eapig_ifr: 0.12
251	    jaccard_ep_ifr: 0.1
252	    max_pairwise_jaccard: 0.25
253	    css_3of3_edges: 12
254	    css_1.00_CPR: 0.13
255	    best_single_CPR: 0.04
256	    css1_cpr_advantage: 0.09
257	  result_rationale: '2B 模型的 IOI 电路比 0.5B 更分散——更多候选 head 可以承担 name mover 和 induction
258	    功能。这增加了方法间的分歧（max Jaccard 进一步降至 0.25），因为 每种方法在候选 head 中做出不同的排序选择。CSS=1.0 过滤出三种方法共同认定的
259	    12 条核心边，CPR=0.13 与 Qwen 结果一致。这证明 CSS 的 utility 不依赖于 特定模型架构或规模，而是由 method diversity（Jaccard）决定。
260	
261	    '
262	  tables:
263	  - name: 'Table: Model Scaling Summary (GPT-2 → Qwen → Gemma)'
264	    description: '三行对应三个模型，列: Params, Max Jaccard, CSS=1.0 Edges, CSS CPR, Advantage。展示
265	      CSS utility 跨模型稳定
266	
267	      '
268	  figures_description:
269	  - '补充到 cross-model bar chart 中作为第三个 subplot
270	
271	    '
272	  analysis: 'P2 优先级实验，为 camera-ready 提供额外的泛化性证据。如果 deadline 紧张 可以推迟到 revision 阶段。但如果完成，三个不同架构（GPT-2
273	    Transformer, Qwen GQA+SwiGLU, Gemma-2 sliding window）的一致结果将使 R1 泛化性 质疑几乎不可攻击。
274	
275	    '
276	- name: Llama-3.1 8B IOI K=3 (EAP-IG + EP + IFR)
277	  plan_id: plan_009
278	  description: '最大规模验证（8B）。P3 优先级，需 A100 80GB。best tier 下可能不完成， 但如果资源允许则提供 impressive
279	    scaling evidence。
280	
281	    '
282	  expected_results:
283	    max_pairwise_jaccard: 0.23
284	    css_3of3_edges: 14
285	    css_1.00_CPR: 0.12
286	    css1_cpr_advantage: 0.08
287	  result_rationale: '8B 模型有大量冗余 head，IOI 电路更分散但核心 name mover 功能仍由少量 head 主导。方法分歧进一步增加（Jaccard→0.23），CSS=1.0
288	    的 14 条边 精准锁定 consensus core。CPR=0.12 与小模型一致，说明 CSS utility 是 scale-invariant 的。EP
289	    在 8B 模型上计算量大（需 edge-level pruning on 8B），可能需要近似——如果近似引入噪声，Jaccard 可能进一步降低。
290	
291	    '
292	  tables: []
293	  figures_description:
294	  - '如果完成，加入 model scaling 图：x=model params (log scale), y=CSS CPR advantage，展示 flat
295	    trend 证明 scale invariance
296	
297	    '
298	  analysis: 'Stretch goal。如果完成，论文可以 claim CSS 在 117M→8B (68x) 范围内 稳健有效。如果未完成，Gemma-2
299	    2B 已经提供了足够的 scaling evidence。
300	
301	    '
302	- name: Top-k Binarization Sensitivity Sweep
303	  plan_id: plan_010
304	  description: '在所有已完成的 model×task 组合上系统扫描 k=50/75/100/150， 验证 CSS=1.0 CPR 对 k 选择的鲁棒性。直接回应
305	    R5。
306	
307	    '
308	  expected_results:
309	    ioi_gpt2:
310	      k50_css_edges: 7
311	      k50_css_CPR: 0.109
312	      k75_css_edges: 12
313	      k75_css_CPR: 0.102
314	      k100_css_edges: 18
315	      k100_css_CPR: 0.098
316	      k150_css_edges: 24
317	      k150_css_CPR: 0.091
318	    sva_gpt2:
319	      k50_css_edges: 8
320	      k50_css_CPR: 0.12
321	      k75_css_edges: 14
322	      k75_css_CPR: 0.11
323	      k100_css_edges: 20
324	      k100_css_CPR: 0.105
325	      k150_css_edges: 28
326	      k150_css_CPR: 0.095
327	    css_advantage_positive_across_all_k: true
328	    max_cpr_variation: 0.025
329	  result_rationale: '随着 k 增加，每个方法保留更多边，pairwise overlap 增加，CSS=1.0 集合扩大。 扩大的 CSS=1.0
330	    包含了更多低置信度的 consensus 边（三种方法在 top-50 之外 的边上的共识更可能是偶然的），因此 CPR 微降。但关键是：(1) CPR 始终为正
331	    且高于 best single method，说明 consensus core 的信号不依赖于 k 的精确选择； (2) 边数与 k 近似线性增长，说明新增的
332	    consensus 边是渐进的而非跳跃的—— 没有 critical threshold artifact。k=50 是合理的 default 选择（CPR
333	    最高）， 但 k=75-150 都给出 qualitatively identical 的结论。
334	
335	    '
336	  tables:
337	  - name: 'Table: Binarization Sensitivity (IOI + SVA)'
338	    description: '行: k=50, 75, 100, 150 + isinf baseline 列: CSS=1.0 Edges, CSS=1.0
339	      CPR, Best-Single CPR, Δ, Max Jaccard 每个 task 一个 sub-table
340	
341	      '
342	  figures_description:
343	  - 'Line plot: x=k, y=CPR, 两条线（CSS=1.0 和 best single method）。 CSS 线始终在 best-single
344	    线上方，两线间 shaded area 表示 CSS advantage。 IOI 和 SVA 各一个 subplot
345	
346	    '
347	  analysis: '此 ablation 是 R5 的完整回应。结论：CSS=1.0 的 faithfulness advantage 是 k-robust
348	    的（max variation < 0.025），实践中 k=50 是 conservative 且 sufficient 的默认值。论文可以在 Method
349	    章节推荐 k=50 并在 appendix 放 完整 sensitivity 表。
350	
351	    '
352	- name: Ablation Method Comparison (Zero vs Mean vs Resample)
353	  plan_id: plan_011
354	  description: '在 IOI 和 SVA 上比较三种 faithfulness 评估方式下的 CSS 优势稳定性。
355	
356	    '
357	  expected_results:
358	    ioi_zero:
359	      css_1.00_CPR: 0.109
360	      best_single_CPR: 0.029
361	      advantage: 0.08
362	    ioi_mean:
363	      css_1.00_CPR: 0.145
364	      best_single_CPR: 0.065
365	      advantage: 0.08
366	    ioi_resample_mean:
367	      css_1.00_CPR: 0.125
368	      best_single_CPR: 0.045
369	      advantage: 0.08
370	    ioi_resample_std: 0.018
371	    sva_zero:
372	      css_1.00_CPR: 0.12
373	      best_single_CPR: 0.03
374	      advantage: 0.09
375	    sva_mean:
376	      css_1.00_CPR: 0.155
377	      best_single_CPR: 0.065
378	      advantage: 0.09
379	    sva_resample_mean:
380	      css_1.00_CPR: 0.135
381	      best_single_CPR: 0.04
382	      advantage: 0.095
383	    advantage_stable_across_methods: true
384	    max_advantage_variation: 0.015
385	  result_rationale: '三种 ablation baseline 改变的是绝对 CPR 水平，但不改变 CSS=1.0 与 single-method
386	    之间的相对差异。Mean ablation 最温和（baseline 更接近正常 activations），所有方法的 CPR 都偏高；zero ablation
387	    最激进，CPR 整体偏低； resample 介于两者之间。CSS=1.0 的优势在三种评估下保持 Δ≈0.08-0.09， 因为 consensus 捕获的是
388	    method-independent 的核心功能边——这些边在任何 ablation scheme 下都是 critical 的。这排除了"CSS 优势是
389	    evaluation artifact" 的质疑。
390	
391	    '
392	  tables:
393	  - name: 'Table: Ablation Method Robustness'
394	    description: '行: Zero, Mean, Resample(n=10) 列: CSS=1.0 CPR, Best-Single CPR, Δ,
395	      p-value (resample) IOI 和 SVA 各一个 panel
396	
397	      '
398	  figures_description: []
399	  analysis: 'P2 实验，主要用于 appendix。如果 reviewer 质疑 evaluation protocol， 此表是 decisive
400	    response。实际上 zero ablation 是最保守的（CSS 优势最难 显现的条件），所以主实验用 zero ablation 是 methodologically
401	    conservative。
402	
403	    '
404	- name: CIRCUS vs CSS Negative Ablation
405	  plan_id: plan_012
406	  description: '系统对比 CIRCUS（threshold diversity within single method）和 CSS （cross-method
407	    consensus），证明结构共识优于单方法内部的阈值稳定性筛选。
408	
409	    '
410	  expected_results:
411	    ioi:
412	      circus_core_edges: 15
413	      circus_CPR: -0.108
414	      css_1.00_edges: 7
415	      css_1.00_CPR: 0.109
416	    sva:
417	      circus_core_edges: 12
418	      circus_CPR: -0.025
419	      css_1.00_edges: 8
420	      css_1.00_CPR: 0.12
421	    factual:
422	      circus_core_edges: 18
423	      circus_CPR: -0.015
424	      css_1.00_edges: 15
425	      css_1.00_CPR: 0.055
426	    circus_negative_on_all_tasks: true
427	  result_rationale: 'CIRCUS 通过扫描 EAP-IG 的阈值范围，选取在不同阈值下始终存在的"核心"边。 这些边确实是 EAP-IG 得分最高且最稳定的边——但它们仍然是
428	    EAP-IG 的 method-specific 视角。当 EAP-IG 本身存在系统性偏差（如过度依赖 early layer attention head
429	    的 gradient signal），CIRCUS 只会放大这种偏差而非 纠正它。IOI 上 CIRCUS CPR=-0.108 说明 EAP-IG 的"最确定"边恰恰是
430	    破坏性最大的（这些边可能是 EAP-IG gradient 信号的 artifact，不对应 真正的功能电路）。CSS=1.0 通过要求多方法共识，天然过滤掉了任何单方法的
431	    系统性偏差。在所有三个 CSS-positive 的任务上，CIRCUS CPR 均为负值， 而 CSS CPR 均为正值——这是 cross-method
432	    consensus 优于 within-method robustness 的 decisive evidence。
433	
434	    '
435	  tables:
436	  - name: 'Table: CIRCUS vs CSS Head-to-Head'
437	    description: '行: IOI, SVA, Factual Recall 列: Method, Edges, CPR, CMD 每个任务两行：CIRCUS
438	      core 和 CSS=1.0
439	
440	      '
441	  figures_description:
442	  - 'Grouped bar chart: 三个任务，每组两个 bar（CIRCUS 灰色，CSS=1.0 蓝色）。 CIRCUS bar 全部在 y=0 以下，CSS
443	    bar 全部在 y=0 以上，视觉冲击力强
444	
445	    '
446	  analysis: '此 negative ablation 是对 competitor CIRCUS (Parekh 2026) 的直接回应， 也从理论上论证了
447	    cross-method consensus 的必要性。即使 CIRCUS 在 Parekh 的原始 setting 中有效，它的 single-method
448	    assumption 使其在 CSS 的 framing 下天然处于劣势。此结果可以放在 Related Work 中用一段话 + 一个表来展示。
449	
450	    '
451	- name: Jaccard-CSS Utility Correlation Analysis
452	  plan_id: plan_013
453	  description: '汇总所有 model×task 组合的 (max pairwise Jaccard) 和 (CSS CPR advantage)，
454	    计算 Spearman 相关系数，拟合 CSS utility threshold。这是 Claim 2 的 definitive evidence。
455	
456	    '
457	  expected_results:
458	    data_points:
459	    - task: SVA (GPT-2)
460	      max_jaccard: 0.22
461	      one_minus_jaccard: 0.78
462	      css_cpr_advantage: 0.09
463	    - task: IOI (Qwen+IFR)
464	      max_jaccard: 0.28
465	      one_minus_jaccard: 0.72
466	      css_cpr_advantage: 0.09
467	    - task: IOI (GPT-2)
468	      max_jaccard: 0.31
469	      one_minus_jaccard: 0.69
470	      css_cpr_advantage: 0.08
471	    - task: Factual (GPT-2)
472	      max_jaccard: 0.48
473	      one_minus_jaccard: 0.52
474	      css_cpr_advantage: 0.018
475	    - task: Arithmetic (Qwen+IFR)
476	      max_jaccard: 0.58
477	      one_minus_jaccard: 0.42
478	      css_cpr_advantage: -0.04
479	    - task: Arithmetic (GPT-2)
480	      max_jaccard: 0.695
481	      one_minus_jaccard: 0.305
482	      css_cpr_advantage: -0.066
483	    spearman_rho: 0.94
484	    spearman_p: 0.005
485	    n_data_points: 6
486	    fitted_threshold: 0.53
487	    threshold_ci_95:
488	    - 0.48
489	    - 0.58
490	    spearman_rho_4task: 1.0
491	    spearman_p_4task: 0.042
492	  result_rationale: '(1-max_Jaccard) 与 CSS_CPR_advantage 的 Spearman ρ=0.94 (p=0.005)
493	    证明 方法多样性是 CSS utility 的强预测因子。这不是偶然的——有清晰的机械解释： 当三种方法独立发现不同的边集（低 Jaccard），它们的交集代表被多种不同算法
494	    视角共同验证的功能核心，这些边大概率是 true circuit edges 而非 method artifacts。当方法高度相关（高 Jaccard），交集趋近于最
495	    selective 的单方法 结果，共识不再增加信息量。 fitted threshold ≈ 0.53 意味着：如果三种发现方法的 max pairwise
496	    Jaccard < 0.53，使用 CSS=1.0 consensus 可以预期 faithfulness 提升；如果 > 0.53， 应直接使用性能最好的单方法。这是一个可操作的
497	    meta-diagnostic guideline。 6 个数据点覆盖了 Jaccard 0.22-0.695 的完整区间，包括 2 个模型、4 个任务，
498	    关系的稳健性已足够说服 reviewer。
499	
500	    '
501	  tables:
502	  - name: 'Table: Jaccard-CSS Correlation Data'
503	    description: '行: 6 个 model×task 组合 列: Task, Model, Methods, Max Jaccard, CSS=1.0
504	      CPR, Best-Single CPR, Δ(advantage), CSS=1.0 Edges 底部: Spearman ρ=0.94, p=0.005
505	
506	      '
507	  figures_description:
508	  - '核心 Figure（可能是 Figure 3 或 4）：Scatter plot，x 轴 = 1-max_Jaccard (method diversity),
509	    y 轴 = CSS CPR advantage。6 个点，颜色区分模型 （GPT-2 蓝色, Qwen 橙色），形状区分任务类型（圆=localized,
510	    三角=distributed）。 灰色虚线 y=0 分隔 CSS-positive 和 CSS-negative 区域。拟合线斜率为正。 右上角标注 ρ=0.94,
511	    p=0.005。垂直虚线标注 Jaccard threshold ≈ 0.53。 这可能是全文最重要的图——将整个叙事浓缩为一张可视化
512	
513	    '
514	  analysis: '此分析是论文的 crown jewel。6 个数据点虽然不多，但覆盖了 localized→distributed spectrum 和两个模型架构，Spearman
515	    ρ=0.94 在 p=0.005 下显著。Jaccard threshold ≈ 0.53 提供了 actionable guideline——这是 reviewer
516	    最希望看到的 practical contribution。仅用 4 个 GPT-2 任务时 ρ=1.0 但 p=0.042（4 个点的 perfect rank
517	    correlation 仍然 marginal），加入 Qwen 数据使 p 降至 0.005， 大幅增强统计说服力。建议论文主文放 4-task 分析（因为更
518	    clean），appendix 放 6-point 分析（加入跨模型验证）。
519	
520	    对 reviewer R1（泛化性）的回应：4 个任务覆盖 localized (SVA, IOI) 和 distributed (Factual, Arithmetic)，2
521	    个模型覆盖不同架构——足以建立 pattern。 对 reviewer R3（K≈2）的回应：IFR 的引入使 Qwen 数据点落在 GPT-2 趋势线上，
522	    证明 method diversity（而非特定方法组合）是 CSS utility 的决定因素。'
523	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff73aa68-366e-40ee-aeae-e2a7b83f70d2",
  "isSidechain": true,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "agentId": "a35a40d5f6dfb18b5",
  "type": "user",
  "uuid": "4b9045fc-53f8-49b1-b3d5-d0c023af23d9",
  "sourceToolAssistantUUID": "ff73aa68-366e-40ee-aeae-e2a7b83f70d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T08:31:06.463Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JEF6fKPxWMyHXUVVSSwERd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b9045fc-53f8-49b1-b3d5-d0c023af23d9",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFoPRXmYL4okomSMLPT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a0dbfc05-965c-4c11-839b-887c6425e49b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F4P5kr9BsT3mQ48PUeZnRB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 17566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 204,
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

_source line 16 · 2026-05-13T08:31:06.469Z_

<details><summary>↩ Tool result · `toolu_01JEF6fKPxWMyHXUVVSSwERd`</summary>

```text
1	tier: median
2	narrative_guidance: '论文重心从 "CSS empirically superior" 转向 "CSS as analytical framework
3	  + binarization pathology"。 SVA 提供第三个数据点但 CSS 优势不明显（CPR 差距 < 0.02），仅能 claim "comparable
4	  faithfulness at fraction of edges"。Jaccard-utility 趋势方向正确（3 点 Spearman ≈ 0.87）但无法做统计检验（p
5	  > 0.3）， 降级为 "observed trend"。DocQA 第四任务因 GPT-2 Small 能力不足未产出 clean circuit，被砍掉。
6	  IFR 加入 Qwen IOI 后某些 pair Jaccard 降低但 IFR×EP 高度相关（~0.55），CSS 优势被稀释。 Claim 3（binarization
7	  pathology）和 Claim 4（CSS taxonomy）成为最坚实的 methodological contribution。 仍可投 EMNLP main，framing
8	  为 analytical/diagnostic framework，reviewer 主攻点在 n=3 泛化性 和 ACDC top-k 的 degree of
9	  freedom。
10	
11	  '
12	imagined_experiments:
13	- name: GPT-2 SVA K=3 CSS
14	  plan_id: plan_004
15	  description: 'Subject-Verb Agreement on GPT-2 Small, K=3 (EAP-IG + EP + ACDC with
16	    top-k=75). SVA 是相对 localized 的语法任务，预期方法间有中等分歧。
17	
18	    '
19	  expected_results:
20	    status: done
21	    conclusion: partial_support
22	    pairwise_jaccard:
23	      eapig_x_ep: 0.38
24	      eapig_x_acdc_k75: 0.18
25	      ep_x_acdc_k75: 0.15
26	    max_jaccard: 0.38
27	    three_way_ratio: 0.067
28	    circuit_sizes:
29	      eapig_k75: 75
30	      ep_k75: 75
31	      acdc_k75: 75
32	      acdc_isinf: 22
33	    css_distribution:
34	      1/3: 148
35	      2/3: 54
36	      3/3: 23
37	    faithfulness_mean:
38	      css_1.00_k75:
39	        edges: 23
40	        CPR: 0.941
41	        CMD: 0.263
42	      css_0.67_k75:
43	        edges: 54
44	        CPR: 0.958
45	        CMD: 0.189
46	      eapig_k75:
47	        edges: 75
48	        CPR: 0.953
49	        CMD: 0.211
50	      ep_k75:
51	        edges: 75
52	        CPR: 0.937
53	        CMD: 0.284
54	      acdc_k75:
55	        edges: 75
56	        CPR: 0.922
57	        CMD: 0.347
58	    faithfulness_isinf_degeneration:
59	      css_1.00_isinf:
60	        edges: 22
61	        CPR: 0.918
62	        CMD: 0.368
63	      acdc_isinf:
64	        edges: 22
65	        CPR: 0.918
66	        CMD: 0.368
67	      degeneration_confirmed: true
68	    css1_cpr_advantage_over_best: -0.012
69	    css1_edge_ratio: 0.307
70	    sva_gate_verdict: MARGINAL — CSS=1.0 CPR comparable but not superior; edge efficiency
71	      3.3x
72	  result_rationale: 'SVA 在 GPT-2 Small 上的电路比 IOI 更 localized（主要涉及 subject token 到
73	    verb position 的 attention + 少量 MLP），但不如 IOI 那样有清晰的 "备份名字" 结构驱动方法分歧。EAP-IG 和 EP
74	    作为 gradient-adjacent 方法在 SVA 上 Jaccard=0.38（高于 IOI 的 0.31），因为 SVA 的 gradient landscape
75	    比 IOI 更平滑——主谓一致主要依赖几个 key attention head，gradient 方法容易收敛到 类似子集。ACDC top-k=75 normalization
76	    打破了 isinf 退化（isinf 只有 22 条 edge），但引入了 k 的选择作为额外自由度。CSS=1.0 包含 23 条边，CPR=0.941
77	    略低于 EAP-IG 的 0.953（差距 0.012）， 说明全共识子集在去除了各方法的 "独特发现" 后损失了少量信息。这符合 median 档预期：CSS
78	    部分支持 但不完美，edge efficiency 优势（3.3x fewer edges）是实在的，但 faithfulness 并无优势。
79	
80	    '
81	  tables:
82	  - name: 'Table: SVA Faithfulness Comparison (mean ablation, top-k=75)'
83	    columns:
84	    - Circuit
85	    - Edges
86	    - CPR ↑
87	    - CMD ↓
88	    - Edge Ratio
89	    rows:
90	    - - CSS=1.0 (k=75)
91	      - 23
92	      - 0.941
93	      - 0.263
94	      - 0.31x
95	    - - CSS≥0.67 (k=75)
96	      - 54
97	      - 0.958
98	      - 0.189
99	      - 0.72x
100	    - - EAP-IG (k=75)
101	      - 75
102	      - 0.953
103	      - 0.211
104	      - 1.00x
105	    - - EP (k=75)
106	      - 75
107	      - 0.937
108	      - 0.284
109	      - 1.00x
110	    - - ACDC (k=75)
111	      - 75
112	      - 0.922
113	      - 0.347
114	      - 1.00x
115	    - - ACDC (isinf)
116	      - 22
117	      - 0.918
118	      - 0.368
119	      - 0.29x
120	  - name: 'Table: SVA Pairwise Jaccard (top-k=75)'
121	    columns:
122	    - ''
123	    - EAP-IG
124	    - EP
125	    - ACDC
126	    rows:
127	    - - EAP-IG
128	      - —
129	      - 0.38
130	      - 0.18
131	    - - EP
132	      - 0.38
133	      - —
134	      - 0.15
135	    - - ACDC
136	      - 0.18
137	      - 0.15
138	      - —
139	  figures_description:
140	  - 'Fig: SVA CSS distribution histogram (1/3, 2/3, 3/3) — 与 IOI 对比显示更集中的分布'
141	  - 'Fig: SVA edge overlap Venn diagram (3 methods, top-k=75)'
142	  analysis: 'SVA 结果处于 IOI（CSS clear win）和 Arithmetic（CSS clear loss）之间的灰色地带。 CSS=1.0
143	    用 23 条边达到了 75 条边 EAP-IG 的 98.7% faithfulness (0.941/0.953)， edge efficiency 论点成立但
144	    CPR 没有优势。关键问题：top-k=75 是 SVA 上的最优 k， k=50 时 CSS=1.0 只有 15 条边且 CPR 降到 0.89，k=100
145	    时 CSS=1.0 有 31 条边但 CPR 不再提升——这个 k-sensitivity 是 reviewer 可攻击的 degree of freedom。
146	    对 Claim 1 的贡献：降级为 "comparable faithfulness at fraction of edges"。 对 Claim 2 的贡献：Jaccard=0.38
147	    + CSS marginal → 第三个数据点，位于 IOI 和 Arithmetic 之间，方向一致。
148	
149	    '
150	- name: GPT-2 DocQA/Factual K=3 CSS
151	  plan_id: plan_005
152	  description: 'Distributed computation task on GPT-2 Small. 预期高 Jaccard → CSS 应该失败（确认模式）。
153	
154	    '
155	  expected_results:
156	    status: abandoned
157	    conclusion: data_not_clean
158	    partial_metrics:
159	      eapig_completed: true
160	      ep_completed: true
161	      acdc_completed: false
162	      acdc_failure_reason: GPT-2 Small factual recall 太弱，ACDC 收敛到近空电路（< 5 edges）
163	    note: ACDC 无法产出有意义的电路，实验被终止。不纳入论文分析。
164	  result_rationale: 'GPT-2 Small (117M) 的 factual knowledge 极为有限，DocQA/Factual recall
165	    任务上 模型本身准确率不稳定（~55-65% vs random 25%）。EAP-IG 和 EP 可以强行产出 top-k 电路，但 ACDC 的 patching-based
166	    搜索在 clean performance 不稳定时无法收敛—— 阈值过高则电路为空，过低则几乎保留全图。尝试调低阈值后得到 3-5 条 isinf 边，
167	    top-k normalization 后虽能凑出 50-75 条边但其 faithfulness 接近随机（CPR ≈ 0）。 这不是 CSS 方法的失败而是
168	    task-model 匹配问题。在 deadline 压力下（ARR 5/25） 决定放弃第四任务，论文保持 3 个任务（IOI + Arithmetic
169	    + SVA）。
170	
171	    '
172	  tables: []
173	  figures_description: []
174	  analysis: '第四任务失败是 median 档的核心限制。论文需要在 Limitations 中说明 GPT-2 Small 对 factual recall
175	    的能力不足以支撑 circuit discovery，并将 broader task coverage 列为 future work。这会成为 reviewer
176	    攻击的主要靶点（"only 3 tasks on one model"）。 应对策略：强调 3 个任务已覆盖 localized（IOI）、distributed（Arithmetic）、
177	    intermediate（SVA）三种电路结构类型，以及 Qwen 上的 cross-model validation。
178	
179	    '
180	- name: Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + IFR)
181	  plan_id: plan_006
182	  description: '首次 larger model + IFR 作为第三方法（替换 ACDC）。IFR 是 similarity-based 方法， 与
183	    gradient 方法家族不同，预期降低 Jaccard。
184	
185	    '
186	  expected_results:
187	    status: done
188	    conclusion: mixed
189	    pairwise_jaccard:
190	      eapig_x_ep: 0.42
191	      eapig_x_ifr: 0.19
192	      ep_x_ifr: 0.55
193	    max_jaccard: 0.55
194	    three_way_ratio: 0.082
195	    circuit_sizes:
196	      eapig_k75: 75
197	      ep_k75: 75
198	      ifr_k75: 75
199	    css_distribution:
200	      1/3: 143
201	      2/3: 63
202	      3/3: 19
203	    faithfulness_mean:
204	      css_1.00:
205	        edges: 19
206	        CPR: 0.103
207	        CMD: 0.921
208	      css_0.67:
209	        edges: 63
210	        CPR: 0.087
211	        CMD: 0.944
212	      eapig_k75:
213	        edges: 75
214	        CPR: 0.091
215	        CMD: 0.938
216	      ep_k75:
217	        edges: 75
218	        CPR: 0.078
219	        CMD: 0.952
220	      ifr_k75:
221	        edges: 75
222	        CPR: 0.064
223	        CMD: 0.967
224	    css1_cpr: 0.103
225	    css1_vs_best_single: 0.012
226	    ifr_ep_correlation_note: 'IFR×EP Jaccard=0.55 远高于预期。IFR 虽然是 similarity-based，但在
227	      IOI 上 EP 的 edge importance 与 IFR 的 representation similarity 高度一致—— 可能因为 IOI
228	      的 backup name 机制使得 "重要的边" 在两种度量下都突出。 这削弱了 K≈3 independent methods 的假设，实际独立证据更接近
229	      K≈2.3。
230	
231	      '
232	  result_rationale: 'Qwen-2.5 0.5B 上 IOI 的电路结构与 GPT-2 类似（名字 mover head + backup 机制），
233	    但模型更大导致电路更分散。EAP-IG×EP 的 Jaccard 从 GPT-2 的 0.31 升至 0.42， 因为 Qwen 的 gradient landscape
234	    更平滑（more parameters → gradient 更 concentrated on true signal）。IFR 作为 similarity-based
235	    方法确实与 EAP-IG 差异大（Jaccard=0.19）， 但与 EP 的 Jaccard 意外达到 0.55——这是因为 EP 的 edge pruning
236	    和 IFR 的 representation similarity 都偏好 "移除后 representation 变化大" 的边，两者在 measurement
237	    层面有隐含重叠。CSS=1.0 的 19 条边 CPR=0.103 略好于 GPT-2 IOI 的 0.109 （量级一致），表明 CSS 在 larger
238	    model 上仍然能提取 faithful 子集。但 max_jaccard=0.55 使得这个数据点在 Jaccard-utility 图上落在不太理想的位置——CSS
239	    优势有限（+0.012 over EAP-IG）且 Jaccard 不够低。IFR 混入了与 EP 相关的信号，有效独立方法数 < 3。
240	
241	    '
242	  tables:
243	  - name: 'Table: Qwen-0.5B IOI Faithfulness (mean ablation, k=75)'
244	    columns:
245	    - Circuit
246	    - Edges
247	    - CPR ↑
248	    - CMD ↓
249	    rows:
250	    - - CSS=1.0
251	      - 19
252	      - 0.103
253	      - 0.921
254	    - - CSS≥0.67
255	      - 63
256	      - 0.087
257	      - 0.944
258	    - - EAP-IG
259	      - 75
260	      - 0.091
261	      - 0.938
262	    - - EP
263	      - 75
264	      - 0.078
265	      - 0.952
266	    - - IFR
267	      - 75
268	      - 0.064
269	      - 0.967
270	  - name: 'Table: Qwen-0.5B IOI Pairwise Jaccard'
271	    columns:
272	    - ''
273	    - EAP-IG
274	    - EP
275	    - IFR
276	    rows:
277	    - - EAP-IG
278	      - —
279	      - 0.42
280	      - 0.19
281	    - - EP
282	      - 0.42
283	      - —
284	      - 0.55
285	    - - IFR
286	      - 0.19
287	      - 0.55
288	      - —
289	  figures_description:
290	  - 'Fig: Qwen IOI CSS distribution vs GPT-2 IOI — 对比两个 model scale 下的 CSS 分布形态'
291	  - 'Fig: IFR vs EP edge importance scatter plot — 显示 Jaccard=0.55 的来源'
292	  analysis: 'Qwen IOI 结果是 "mixed" 的典型案例。好消息：CSS=1.0 在 larger model 上仍然 work， CPR 略优于
293	    best single method，证明 CSS 框架可跨模型。坏消息：IFR×EP Jaccard=0.55 说明 "不同算法家族 → 低相关" 的假设不总成立——算法差异不等于
294	    measurement independence。 这对 Claim 2 有双重影响：(1) max_jaccard=0.55 + CSS marginal
295	    win 支持 "中等 Jaccard → 中等 CSS 收益" 的连续关系假设；(2) 但也说明 Jaccard 可能需要分 pair 解读而非只看 max。
296	    论文中应在 Discussion 讨论 IFR-EP 相关性的 mechanistic 原因。
297	
298	    '
299	- name: Qwen-2.5 0.5B Arithmetic K=3
300	  plan_id: plan_007
301	  description: 'Qwen 上的 Arithmetic (Greaterthan) task，IFR 替换 ACDC。 验证 IFR 是否能降低 Arithmetic
302	    的 Jaccard 使 CSS recover。
303	
304	    '
305	  expected_results:
306	    status: done
307	    conclusion: negative
308	    pairwise_jaccard:
309	      eapig_x_ep: 0.61
310	      eapig_x_ifr: 0.38
311	      ep_x_ifr: 0.48
312	    max_jaccard: 0.61
313	    three_way_ratio: 0.195
314	    css_distribution:
315	      1/3: 98
316	      2/3: 73
317	      3/3: 54
318	    faithfulness_mean:
319	      css_1.00:
320	        edges: 54
321	        CPR: 0.932
322	        CMD: 0.302
323	      eapig_k75:
324	        edges: 75
325	        CPR: 0.971
326	        CMD: 0.128
327	      ep_k75:
328	        edges: 75
329	        CPR: 0.955
330	        CMD: 0.199
331	      ifr_k75:
332	        edges: 75
333	        CPR: 0.891
334	        CMD: 0.487
335	    css1_cpr_advantage_over_best: -0.039
336	    note: 'IFR 将 max_jaccard 从 GPT-2 的 0.695 降至 0.61，但仍不够低。 CSS=1.0 CPR=0.932 < EAP-IG=0.971。CSS
337	      未 recover。
338	
339	      '
340	  result_rationale: 'Arithmetic/Greaterthan 任务的电路结构本质上是 distributed 的——多个 MLP layer
341	    协同完成数值比较，gradient-based 方法容易收敛到相似的关键路径。IFR 替换 ACDC 后 确实降低了 max_jaccard（0.695 →
342	    0.61），但降幅不够大。原因：Arithmetic 的 "重要边" 集中在少数 MLP 到 final position 的连接上，无论用 gradient
343	    (EAP-IG/EP) 还是 similarity (IFR)，这些边都会被 rank 到顶部。IFR 本身表现较弱（CPR=0.891）， 拖累了 CSS=1.0
344	    的质量——共识要求三方都同意的边包含了 IFR 的一些 false positive。 这个结果实际上支持 Claim 2：Jaccard 仍然偏高（0.61）→
345	    CSS 仍然不优—— 趋势一致，但不是正面结果。
346	
347	    '
348	  tables:
349	  - name: 'Table: Qwen-0.5B Arithmetic Faithfulness (mean ablation)'
350	    columns:
351	    - Circuit
352	    - Edges
353	    - CPR ↑
354	    - CMD ↓
355	    rows:
356	    - - CSS=1.0
357	      - 54
358	      - 0.932
359	      - 0.302
360	    - - EAP-IG (k=75)
361	      - 75
362	      - 0.971
363	      - 0.128
364	    - - EP (k=75)
365	      - 75
366	      - 0.955
367	      - 0.199
368	    - - IFR (k=75)
369	      - 75
370	      - 0.891
371	      - 0.487
372	  figures_description:
373	  - 'Fig: Qwen Arithmetic CSS distribution — 与 GPT-2 Arithmetic 对比'
374	  analysis: 'IFR "部分修复" 了 Arithmetic 的 Jaccard 问题但不够彻底。从 Claim 2 角度看 这其实是一个有价值的 intermediate
375	    data point：Jaccard 从 0.695 降到 0.61， CSS 优势从 -0.066 改善到 -0.039，方向正确但仍为负。如果画 Jaccard
376	    vs CSS_advantage 的图，这个点和 GPT-2 Arithmetic 几乎在同一条趋势线上。 问题在于 IFR 本身在 Arithmetic
377	    上的 faithfulness 较差（CPR=0.891 远低于 EAP-IG 的 0.971），说明 similarity-based method 对
378	    distributed computation 的识别 能力有限——这是一个独立的 finding，可在 Discussion 中报告。
379	
380	    '
381	- name: Gemma-2 2B IOI K=3
382	  plan_id: plan_008
383	  description: Scale to 2B model (Gemma-2). P2 优先级。
384	  expected_results:
385	    status: not_attempted
386	    conclusion: null
387	    reason: 时间和 GPU 资源不足，P1 任务已消耗大部分 budget。列入 Future Work。
388	  result_rationale: 'Median 档的时间约束（ARR 5/25 deadline）下，plan_004 (SVA) + plan_006 (Qwen
389	    IOI) + plan_007 (Qwen Arith) 已消耗约 20 GPU-hours。Gemma-2 2B 需要 16 GPU-hours 且 依赖
390	    plan_006 结果（IFR pipeline 验证）。即使 plan_006 顺利完成，剩余时间不足 以完成 Gemma-2 实验 + 分析 + 论文写作。P2
391	    优先级下被合理推迟。
392	
393	    '
394	  tables: []
395	  figures_description: []
396	  analysis: Not attempted. 在 Limitations 中列为 model scale generalization future work。
397	- name: Llama-3.1 8B IOI K=3
398	  plan_id: plan_009
399	  description: Scale to 8B model. P3 优先级。Needs A100 80GB。
400	  expected_results:
401	    status: not_attempted
402	    conclusion: null
403	    reason: P3 优先级，且 plan_008 未完成作为前置。远超 deadline 范围。
404	  result_rationale: '8B 模型实验需要 A100 80GB（当前设备可能不支持 EP 的内存需求），且依赖 plan_008。 在 median
405	    档下属于完全不现实的目标。
406	
407	    '
408	  tables: []
409	  figures_description: []
410	  analysis: Not attempted. Future work 中的 stretch goal。
411	- name: Binarization sensitivity ablation
412	  plan_id: plan_010
413	  description: 'Systematic k sweep (k=50/75/100/150) on all completed model×task pairs.
414	    验证 CSS 在不同 k 下的稳定性。
415	
416	    '
417	  expected_results:
418	    status: done
419	    conclusion: partially_stable
420	    ioi_gpt2_k_sweep:
421	      k50:
422	        css_1.0_edges: 12
423	        css_1.0_cpr: 0.098
424	      k75:
425	        css_1.0_edges: 18
426	        css_1.0_cpr: 0.112
427	      k100:
428	        css_1.0_edges: 24
429	        css_1.0_cpr: 0.109
430	      k150:
431	        css_1.0_edges: 31
432	        css_1.0_cpr: 0.108
433	      verdict: stable (CPR range 0.098-0.112, Δ=0.014)
434	    arithmetic_gpt2_k_sweep:
435	      k50:
436	        css_1.0_edges: 44
437	        css_1.0_cpr: 0.919
438	      k75:
439	        css_1.0_edges: 54
440	        css_1.0_cpr: 0.919
441	      k100:
442	        css_1.0_edges: 62
443	        css_1.0_cpr: 0.926
444	      k150:
445	        css_1.0_edges: 71
446	        css_1.0_cpr: 0.933
447	      verdict: stable (CPR range 0.919-0.933, Δ=0.014)
448	    sva_gpt2_k_sweep:
449	      k50:
450	        css_1.0_edges: 15
451	        css_1.0_cpr: 0.891
452	      k75:
453	        css_1.0_edges: 23
454	        css_1.0_cpr: 0.941
455	      k100:
456	        css_1.0_edges: 29
457	        css_1.0_cpr: 0.944
458	      k150:
459	        css_1.0_edges: 38
460	        css_1.0_cpr: 0.94
461	      verdict: sensitive at k=50 (CPR drop 0.05), stable k=75-150
462	    qwen_ioi_k_sweep:
463	      k50:
464	        css_1.0_edges: 11
465	        css_1.0_cpr: 0.082
466	      k75:
467	        css_1.0_edges: 19
468	        css_1.0_cpr: 0.103
469	      k100:
470	        css_1.0_edges: 26
471	        css_1.0_cpr: 0.099
472	      k150:
473	        css_1.0_edges: 35
474	        css_1.0_cpr: 0.097
475	      verdict: stable k=75-150, drop at k=50
476	    overall_verdict: 'CSS=1.0 CPR 在 k=75-150 范围内对所有 task 稳定（max Δ < 0.015）。 k=50 在
477	      SVA 和 Qwen IOI 上 CPR 下降 ~0.04-0.05，因为 k=50 过小导致方法 重叠不足、CSS=1.0 边数太少。推荐 k=75
478	      作为默认值，但需要在论文中报告这个选择。
479	
480	      '
481	  result_rationale: 'Top-k normalization 的核心逻辑是让 ACDC 和其他方法在同一 edge budget 下比较。 k=75-150
482	    范围内，三种方法各自选择的 top edges 有足够的 overlap base 使 CSS=1.0 稳定。k=50 时边太少，方法间 overlap 降到
483	    noise level，CSS=1.0 变得不可靠。 SVA 比 IOI 更敏感于 k 的原因：SVA 电路更 concentrated（少数 critical
484	    edges 占比更大），k=50 可能恰好切掉了某些方法的 borderline critical edge。 这个 sensitivity 是 median
485	    档的典型问题——结果 "基本稳定但有 caveat"， reviewer 可以攻击 k=75 的选择是 cherry-picked（虽然实际不是）。
486	
487	    '
488	  tables:
489	  - name: 'Table: CSS=1.0 CPR across k values (all tasks)'
490	    columns:
491	    - Task
492	    - k=50
493	    - k=75
494	    - k=100
495	    - k=150
496	    - Max Δ
497	    rows:
498	    - - IOI (GPT-2)
499	      - 0.098
500	      - 0.112
501	      - 0.109
502	      - 0.108
503	      - 0.014
504	    - - Arith (GPT-2)
505	      - 0.919
506	      - 0.919
507	      - 0.926
508	      - 0.933
509	      - 0.014
510	    - - SVA (GPT-2)
511	      - 0.891
512	      - 0.941
513	      - 0.944
514	      - 0.94
515	      - 0.053
516	    - - IOI (Qwen)
517	      - 0.082
518	      - 0.103
519	      - 0.099
520	      - 0.097
521	      - 0.021
522	  figures_description:
523	  - 'Fig: Line plot of CSS=1.0 CPR vs k for all 4 model×task configs — 灰色 band 标记
524	    k=75-150 稳定区间'
525	  analysis: 'Binarization ablation 的结论可以支撑 Claim 3（top-k 修复 isinf 退化）， 但 SVA k=50
526	    的 sensitivity 会被 reviewer 追问。应对：(1) 论文推荐 k=75 并展示 full sweep 数据，(2) argue k=50
527	    本身就低于合理下界（只保留 0.15% edges for GPT-2 的 32k+ edge graph），(3) 指出 k=75-150 的 CPR 标准差
528	    < 0.01。
529	
530	    '
531	- name: Ablation method comparison (zero vs mean vs resample)
532	  plan_id: plan_011
533	  description: 'Compare ablation methods on all tasks. P2 优先级。 验证 CSS advantage 不依赖特定
534	    evaluation ablation。
535	
536	    '
537	  expected_results:
538	    status: partial
539	    conclusion: inconclusive
540	    completed_tasks:
541	    - IOI (GPT-2)
542	    ioi_gpt2:
543	      zero_ablation:
544	        css_1.0_cpr: 0.109
545	        best_single_cpr: 0.029
546	        css_advantage: 0.08
547	      mean_ablation:
548	        css_1.0_cpr: 0.112
549	        best_single_cpr: 0.091
550	        css_advantage: 0.021
551	      resample_ablation:
552	        css_1.0_cpr: 0.095
553	        best_single_cpr: 0.082
554	        css_advantage: 0.013
555	    note: '仅完成 IOI 一个 task 的三种 ablation 对比。CSS advantage 在三种 ablation 下 方向一致（正），但绝对值差异大（0.013-0.080）。SVA
556	      和 Arithmetic 未完成。
557	
558	      '
559	  result_rationale: '这是 P2 优先级实验，在 SVA (plan_004) 和 Qwen (plan_006/007) 完成后 时间已所剩不多。仅对
560	    IOI 跑了 zero/mean/resample 三种 ablation， 因为 IOI 是唯一 CSS clearly wins 的 task。结果显示
561	    CSS 优势在三种 ablation 下都为正但量级不同：zero ablation 下优势最大（因为 zero ablation 对电路外 edge 的破坏最大，小电路受益最多），resample
562	    下优势最小。这表明 CSS advantage 不是 ablation method artifact，但缺少 SVA 和 Arithmetic 的对比数据使结论不完整。
563	
564	    '
565	  tables:
566	  - name: 'Table: IOI CSS advantage under different ablation methods'
567	    columns:
568	    - Ablation
569	    - CSS=1.0 CPR
570	    - Best Single CPR
571	    - Advantage
572	    rows:
573	    - - Zero
574	      - 0.109
575	      - 0.029
576	      - '+0.080'
577	    - - Mean
578	      - 0.112
579	      - 0.091
580	      - '+0.021'
581	    - - Resample
582	      - 0.095
583	      - 0.082
584	      - '+0.013'
585	  figures_description: []
586	  analysis: '部分完成的 ablation 对比。IOI 结果可以放在 Appendix 中作为 robustness check。 关键 takeaway：CSS
587	    advantage 在 mean ablation（最常用）下为 +0.021，在 resample （最严格）下为 +0.013，都是正的。但仅一个 task
588	    不足以 claim robustness。 论文中可以 footnote 提及 IOI 上的一致性，full multi-task ablation 列为
589	    future work。
590	
591	    '
592	- name: CIRCUS as negative ablation
593	  plan_id: plan_012
594	  description: '使用 D021 中 CIRCUS 的已有失败结果作为 negative ablation。 0 GPU hours，仅需分析和写作。
595	
596	    '
597	  expected_results:
598	    status: done
599	    conclusion: negative_ablation_confirmed
600	    circus_vs_css:
601	      ioi_circus_core_cpr: -0.108
602	      ioi_css_1.0_cpr: 0.109
603	      ioi_circus_core_edges: 15
604	      ioi_css_1.0_edges: 7
605	    circus_failure_modes:
606	    - CIRCUS 基于 single-method faithfulness scoring 选 core edges，但 scoring 本身依赖 ablation
607	      noise
608	    - 'CIRCUS D021 三次运行结果不一致（edges: 12, 15, 18），说明 threshold sensitivity 严重'
609	    - CSS 的 binary consensus 不需要 score calibration，避免了 CIRCUS 的核心缺陷
610	  result_rationale: 'CIRCUS (Parekh 2026) 在 IOI 上的 D021 结果已有：core edges CPR=-0.108（负值，
611	    说明 CIRCUS core 实际上破坏了模型行为）。相比 CSS=1.0 的 CPR=0.109，差距极大。 CIRCUS 失败的根本原因是它在 single
612	    method 内部做 faithfulness scoring 来选 core， 但这个 scoring 对 threshold 和 ablation method
613	    极其敏感。CSS 通过 cross-method binary agreement 绕过了 score calibration 问题。这个对比自然成为论文中
614	    Claim 4 的关键证据：structural consensus (CSS) > faithfulness scoring (CIRCUS)。
615	
616	    '
617	  tables:
618	  - name: 'Table: CSS vs CIRCUS on IOI (negative ablation)'
619	    columns:
620	    - Method
621	    - Edges
622	    - CPR ↑
623	    - CMD ↓
624	    - Stable?
625	    rows:
626	    - - CSS=1.0
627	      - 7
628	      - 0.109
629	      - 0.911
630	      - Yes (3/3 runs identical)
631	    - - CIRCUS core
632	      - 15
633	      - -0.108
634	      - 1.134
635	      - No (12-18 edges across runs)
636	  figures_description:
637	  - 'Fig: CSS vs CIRCUS edge selection comparison — 显示两种方法选择的 edge 集合差异'
638	  analysis: 'CIRCUS negative ablation 是 Claim 4 最有力的证据，也是论文中最 "clean" 的结果之一。 CSS=1.0
639	    用更少的边（7 vs 15）达到正的 CPR，而 CIRCUS core 的 CPR 为负。 关键论点：binary consensus across methods
640	    比 within-method score selection 更稳定， 因为前者不需要 score calibration，后者严重依赖 ablation
641	    method 和 threshold。 这是 methodological contribution 的核心，reviewer 较难攻击（结果清晰、对比公平）。
642	
643	    '
644	- name: Jaccard-CSS correlation analysis
645	  plan_id: plan_013
646	  description: 'Across all model×task pairs, plot max pairwise Jaccard vs CSS faithfulness
647	    advantage. 3 个 task data points + Qwen cross-validation。
648	
649	    '
650	  expected_results:
651	    status: done
652	    conclusion: trend_observed_no_statistical_power
653	    data_points:
654	    - task: IOI (GPT-2)
655	      max_jaccard: 0.31
656	      css_advantage: 0.021
657	      css_wins: true
658	    - task: Arithmetic (GPT-2)
659	      max_jaccard: 0.695
660	      css_advantage: -0.066
661	      css_wins: false
662	    - task: SVA (GPT-2)
663	      max_jaccard: 0.38
664	      css_advantage: -0.012
665	      css_wins: false
666	    - task: IOI (Qwen)
667	      max_jaccard: 0.55
668	      css_advantage: 0.012
669	      css_wins: true
670	    - task: Arithmetic (Qwen)
671	      max_jaccard: 0.61
672	      css_advantage: -0.039
673	      css_wins: false
674	    spearman_rho: -0.9
675	    spearman_p: 0.037
676	    pearson_r: -0.82
677	    pearson_p: 0.089
678	    threshold_estimate: max_jaccard ≈ 0.45 (CSS advantage crosses zero)
679	    note: 'Spearman p=0.037 因为 5 个 data points 刚过 significance threshold， 但 Pearson
680	      p=0.089 不显著。Reviewer 会质疑 n=5 的统计力。 如果只看 3 个 GPT-2 tasks，Spearman 无法计算 meaningful
681	      p-value。
682	
683	      '
684	  result_rationale: '5 个 model×task 数据点显示清晰的负相关趋势：max_jaccard 越高，CSS advantage 越低。Spearman
685	    rho=-0.90 方向非常一致（只有 SVA 和 Qwen IOI 的排序有微小扰动）。 但 n=5 的统计检验力极弱——Spearman p=0.037
686	    刚好显著，Pearson 不显著。这是 因为 5 个点中有 3 个 "extremes"（IOI GPT-2 clearly positive，两个 Arithmetic
687	    clearly negative），中间的 SVA 和 Qwen IOI 决定了趋势的精确斜率但不足以 firm up p-value。如果只看 3 个 GPT-2
688	    任务（plan 最初设计），完全无法做统计检验； 加入 Qwen 的 2 个数据点后勉强可以报告 Spearman。 论文中应 claim "observed
689	    negative correlation consistent with hypothesis" 而非 "established significant correlation"。threshold
690	    ≈ 0.45 只是 visual estimate from 5 points，不具预测力。
691	
692	    '
693	  tables:
694	  - name: 'Table: Jaccard vs CSS Advantage (all model×task)'
695	    columns:
696	    - Task
697	    - Model
698	    - Max Jaccard
699	    - CSS Adv (CPR)
700	    - CSS Wins?
701	    rows:
702	    - - IOI
703	      - GPT-2
704	      - 0.31
705	      - '+0.021'
706	      - ✓
707	    - - SVA
708	      - GPT-2
709	      - 0.38
710	      - −0.012
711	      - ✗ (marginal)
712	    - - IOI
713	      - Qwen-0.5B
714	      - 0.55
715	      - '+0.012'
716	      - ✓ (marginal)
717	    - - Arithmetic
718	      - Qwen-0.5B
719	      - 0.61
720	      - −0.039
721	      - ✗
722	    - - Arithmetic
723	      - GPT-2
724	      - 0.695
725	      - −0.066
726	      - ✗
727	  figures_description:
728	  - 'Fig (KEY FIGURE): Scatter plot — x: max pairwise Jaccard, y: CSS CPR advantage.
729	    5 points with linear fit and 95% CI band. Vertical dashed line at Jaccard≈0.45.
730	    Points colored by task type (shape) and model (color).'
731	  - 'Fig: Heatmap — rows=tasks, cols=method pairs, cells=Jaccard values. Annotated
732	    with CSS outcome per task.'
733	  analysis: 这是 Claim 2 的核心 figure，也是论文能否从 "anecdotal 2-task observation" 升级为 "systematic
734	    pattern" 的关键。5 个数据点的 Spearman rho=-0.90 (p=0.037) 在 技术上可以 claim significance，但
735	    reviewer 很可能指出：(1) n=5 统计力不足， (2) IOI 和 Arithmetic 是 "designed" 对比（一个 localized
736	    一个 distributed）， 不是 random sample，(3) SVA 和 Qwen IOI 的 "marginal" 结果可以翻转。 应对策略：(1)
737	    不 over-claim，用 "observed trend" 而非 "significant correlation"； (2) 强调 mechanistic
738	    motivation（Jaccard 度量 method independence → independence 是 consensus 有价值的前提条件）比纯统计论证更重要；(3)
739	    提供 threshold 的 practical guidance（"practitioners should check Jaccard before applying
740	    CSS"）作为 actionable takeaway。
741	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0dbfc05-965c-4c11-839b-887c6425e49b",
  "isSidechain": true,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "agentId": "a35a40d5f6dfb18b5",
  "type": "user",
  "uuid": "a551f458-61ac-4e02-a797-274ec59a1d1c",
  "sourceToolAssistantUUID": "a0dbfc05-965c-4c11-839b-887c6425e49b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T08:31:06.665Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GXrfJadA8xP4uyfuuCwEUW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a551f458-61ac-4e02-a797-274ec59a1d1c",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFoPRXmYL4okomSMLPT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c52d921d-d60e-40dc-8339-b7091d931f28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F4P5kr9BsT3mQ48PUeZnRB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 204,
      "cache_read_input_tokens": 17566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 204,
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

_source line 18 · 2026-05-13T08:31:06.677Z_

<details><summary>↩ Tool result · `toolu_01GXrfJadA8xP4uyfuuCwEUW`</summary>

```text
1	tier: worst
2	narrative_guidance: 'Method paper 不可行。Gradient-based methods (EAP-IG, EP) 在 GPT-2
3	  上系统性高相关（Jaccard 0.50-0.70）， K=3 的有效独立方法数 K_eff≈1.5。IFR 未能打破这一退化——在 GPT-2 scale 上
4	  similarity-based attribution 收敛到 gradient proxy。唯一正面结果 IOI 是 outlier（14-edge ACDC
5	  强先验 + 极端 localized circuit）。 Jaccard-utility 关系仅有 3-4 个数据点且被 ACDC binarization confound
6	  驱动，去除 ACDC 后 K=2 consensus 无统计意义。重构为 analysis paper: ''When Does Cross-Method Consensus
7	  Fail in Circuit Discovery?'' 投 EMNLP Findings 或 workshop。
8	
9	  '
10	imagined_experiments:
11	- name: GPT-2 SVA K=3 CSS
12	  plan_id: plan_004
13	  description: 'Subject-Verb Agreement on GPT-2 Small, K=3 (EAP-IG + EP + ACDC)。 验证
14	    CSS 在第三个任务上的表现。SVA 电路预期比 IOI 更 localized， 但 worst 档假设 gradient methods 在 GPT-2
15	    上的相关性是系统性的，不因任务而异。
16	
17	    '
18	  expected_results:
19	    pairwise_jaccard:
20	      eapig_x_ep: 0.55
21	      eapig_x_acdc: 0.14
22	      ep_x_acdc: 0.11
23	    max_pairwise_jaccard: 0.55
24	    three_way_ratio: 0.09
25	    circuit_sizes:
26	      eapig: 100
27	      ep: 100
28	      acdc: 19
29	    acdc_binarization: isinf (19 edges)
30	    css_distribution:
31	      1/3: 42
32	      2/3: 58
33	      3/3: 19
34	    faithfulness_mean:
35	      css_1.00_isinf:
36	        edges: 19
37	        CPR: 0.91
38	        CMD: 0.12
39	      css_1.00_k50:
40	        edges: 38
41	        CPR: 0.88
42	        CMD: 0.18
43	      eapig_k50:
44	        edges: 50
45	        CPR: 0.95
46	        CMD: 0.07
47	      ep_k50:
48	        edges: 50
49	        CPR: 0.93
50	        CMD: 0.1
51	      acdc_k50:
52	        edges: 50
53	        CPR: 0.87
54	        CMD: 0.19
55	    faithfulness_zero:
56	      css_1.00:
57	        edges: 19
58	        CPR: -0.05
59	        CMD: 1.08
60	      eap_ig:
61	        edges: 100
62	        CPR: -0.03
63	        CMD: 1.04
64	    d025_verdict: 'FAIL (condition④: CSS=1.0 mean CPR=0.88 < EAP-IG=0.95)'
65	    method_diversity_1_minus_max_jaccard: 0.45
66	  result_rationale: 'SVA 虽然传统上被认为是 localized circuit，但在 GPT-2 Small 上 EAP-IG 和 EP
67	    同为 gradient-based，共享相同的 backward pass 信息——两者识别的 top-100 edges 有 55% 重叠。这不是偶然，而是因为
68	    GPT-2 的 12 层 12 头结构中， subject-verb 信息流经的 attention pattern 对 gradient magnitude
69	    和 edge pruning score 产生高度相似的排序。ACDC isinf 仅保留 19 条极端边，CSS=1.0≡ACDC， top-k 归一化后
70	    CSS=1.0 (38 edges) 的 CPR=0.88 仍低于 EAP-IG 单方法的 0.95， 因为 consensus 丢弃了 EAP-IG 独有的
71	    12 条高贡献边（这些边 EP 未覆盖因其 pruning criterion 对 indirect effects 的敏感度不同）。重复了 Arithmetic
72	    的负面模式。
73	
74	    '
75	  tables:
76	  - caption: 'Table: SVA pairwise Jaccard matrix (GPT-2 Small, k=100)'
77	    rows:
78	    - - ''
79	      - EAP-IG
80	      - EP
81	      - ACDC
82	    - - EAP-IG
83	      - '1.00'
84	      - '0.55'
85	      - '0.14'
86	    - - EP
87	      - '0.55'
88	      - '1.00'
89	      - '0.11'
90	    - - ACDC
91	      - '0.14'
92	      - '0.11'
93	      - '1.00'
94	  - caption: 'Table: SVA CSS faithfulness comparison (mean ablation, k=50)'
95	    rows:
96	    - - Method
97	      - Edges
98	      - CPR
99	      - CMD
100	    - - CSS=1.0 (isinf)
101	      - '19'
102	      - '0.91'
103	      - '0.12'
104	    - - CSS=1.0 (k=50)
105	      - '38'
106	      - '0.88'
107	      - '0.18'
108	    - - EAP-IG (k=50)
109	      - '50'
110	      - '0.95'
111	      - '0.07'
112	    - - EP (k=50)
113	      - '50'
114	      - '0.93'
115	      - '0.10'
116	    - - ACDC (k=50)
117	      - '50'
118	      - '0.87'
119	      - '0.19'
120	  figures_description:
121	  - 'Fig: SVA CSS distribution bar chart (1/3, 2/3, 3/3) — 右偏分布，3/3 占比 16%，与 Arithmetic
122	    类似'
123	  - 'Fig: SVA edge overlap Venn diagram — EAP-IG∩EP 大区域，ACDC 几乎不重叠'
124	  analysis: 'SVA 重复了 Arithmetic 的模式：gradient methods 高相关导致 K_eff≈1.5， CSS 退化为 ACDC
125	    和 gradient-consensus 的交集而非三方独立投票。 至此 3 个 GPT-2 任务中仅 IOI 支持 CSS，初步支持 IOI 是 outlier
126	    的假设。 对 Claim 2 提供第三个数据点（max Jaccard=0.55 → CSS fails），但 n=3 仍不足以 拟合 threshold。
127	
128	    '
129	- name: GPT-2 DocQA/Factual K=3 CSS
130	  plan_id: plan_005
131	  description: '在 GPT-2 Small 上运行分布式计算任务（factual recall 或 document QA）， K=3 (EAP-IG
132	    + EP + ACDC)。预期分布式电路导致更高的 inter-method 相关性。
133	
134	    '
135	  expected_results:
136	    pairwise_jaccard:
137	      eapig_x_ep: 0.62
138	      eapig_x_acdc: 0.22
139	      ep_x_acdc: 0.19
140	    max_pairwise_jaccard: 0.62
141	    three_way_ratio: 0.15
142	    circuit_sizes:
143	      eapig: 100
144	      ep: 100
145	      acdc: 35
146	    acdc_binarization: isinf (35 edges) — 分布式任务产生更多 extreme edges
147	    faithfulness_mean:
148	      css_1.00_k50:
149	        edges: 42
150	        CPR: 0.82
151	        CMD: 0.25
152	      eapig_k50:
153	        edges: 50
154	        CPR: 0.91
155	        CMD: 0.13
156	      ep_k50:
157	        edges: 50
158	        CPR: 0.88
159	        CMD: 0.17
160	    d025_verdict: 'FAIL (condition④: CSS=1.0 CPR=0.82 < EAP-IG=0.91)'
161	    method_diversity_1_minus_max_jaccard: 0.38
162	  result_rationale: 'Distributed computation tasks（如 factual recall）在 GPT-2 上涉及 MLP
163	    和多层 attention 的广泛交互——不存在像 IOI 那样的 sparse 14-edge bottleneck。 所有 gradient-based
164	    methods 都会识别出相似的 "information highway" 通路， 因为 distributed circuits 的 gradient
165	    landscape 更平坦，top edges 的排序差异更小。 ACDC isinf 产生 35 条边（比 IOI/SVA 多），因为分布式任务中更多边有
166	    extreme attribution。 CSS=1.0 丢弃了各方法独有的 task-specific edges，导致 CPR 下降。 本实验的价值在于确认
167	    "distributed circuit → high Jaccard → CSS fail" 的因果链， 但不产生超出 Arithmetic 已有结论的新
168	    insight。
169	
170	    '
171	  tables:
172	  - caption: 'Table: DocQA faithfulness comparison (mean ablation, k=50)'
173	    rows:
174	    - - Method
175	      - Edges
176	      - CPR
177	      - CMD
178	    - - CSS=1.0 (k=50)
179	      - '42'
180	      - '0.82'
181	      - '0.25'
182	    - - EAP-IG (k=50)
183	      - '50'
184	      - '0.91'
185	      - '0.13'
186	    - - EP (k=50)
187	      - '50'
188	      - '0.88'
189	      - '0.17'
190	    - - ACDC (k=50)
191	      - '50'
192	      - '0.84'
193	      - '0.22'
194	  figures_description:
195	  - 'Fig: DocQA CSS distribution — 集中在 2/3 和 3/3，分布式电路导致高一致性'
196	  analysis: '第四个数据点进一步确认 pattern 但边际贡献递减。4 个 GPT-2 任务中 3 个 FAIL， 仅 IOI PASS。这足以支撑
197	    analysis paper 的 "CSS fails when methods correlate" 叙事， 但无法支撑 method paper 的 "CSS
198	    is generally useful" claim。 对 Claim 2 的数据点：max_Jaccard=0.62 → CSS CPR advantage
199	    = -0.09。
200	
201	    '
202	- name: Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + IFR)
203	  plan_id: plan_006
204	  description: '首个非 GPT-2 模型。IFR 替代 ACDC 作为第三种方法（不同 algorithmic family）。 Worst 档假设
205	    IFR 在 0.5B scale 退化为 gradient proxy。
206	
207	    '
208	  expected_results:
209	    pairwise_jaccard:
210	      eapig_x_ep: 0.48
211	      eapig_x_ifr: 0.52
212	      ep_x_ifr: 0.45
213	    max_pairwise_jaccard: 0.52
214	    three_way_ratio: 0.28
215	    circuit_sizes:
216	      eapig: 100
217	      ep: 100
218	      ifr: 100
219	    css_distribution:
220	      1/3: 28
221	      2/3: 72
222	      3/3: 48
223	    faithfulness_mean:
224	      css_1.00:
225	        edges: 48
226	        CPR: 0.08
227	        CMD: 0.87
228	      eapig:
229	        edges: 100
230	        CPR: 0.1
231	        CMD: 0.85
232	      ep:
233	        edges: 100
234	        CPR: 0.06
235	        CMD: 0.9
236	      ifr:
237	        edges: 100
238	        CPR: 0.07
239	        CMD: 0.89
240	    css_1_cpr_vs_best_single: -0.02
241	    ioi_css1_cpr_with_ifr: 0.08
242	    method_diversity_1_minus_max_jaccard: 0.48
243	  result_rationale: 'IFR (Iterative Feature Removal) 本质上通过 feature similarity 来评估
244	    edge importance， 但在 0.5B transformer 中，feature similarity 的排序与 gradient magnitude
245	    高度相关—— 因为 transformer 的 residual stream 结构使得 gradient 和 activation similarity
246	    对 edge importance 产生相似的排序（Elhage et al. 2021 的 "privileged basis" 现象）。 Qwen-2.5
247	    0.5B 有 24 层 16 头，IOI circuit 比 GPT-2 更分散（更多层参与）， 导致 pairwise Jaccard 虽比 GPT-2
248	    IOI (0.31) 高但不如 Arithmetic (0.70)。 CSS=1.0 的 48 条边 CPR=0.08 略低于 EAP-IG 的 0.10——差距很小但方向为负，
249	    在 edge-efficiency (CPR/edge) 上 CSS 有微弱优势但不显著。 IFR 未能提供预期的 "different family" 独立性，K_eff
250	    仍约 1.8。
251	
252	    '
253	  tables:
254	  - caption: 'Table: Qwen-2.5 IOI Jaccard matrix (k=100)'
255	    rows:
256	    - - ''
257	      - EAP-IG
258	      - EP
259	      - IFR
260	    - - EAP-IG
261	      - '1.00'
262	      - '0.48'
263	      - '0.52'
264	    - - EP
265	      - '0.48'
266	      - '1.00'
267	      - '0.45'
268	    - - IFR
269	      - '0.52'
270	      - '0.45'
271	      - '1.00'
272	  - caption: 'Table: Qwen-2.5 IOI faithfulness (mean ablation)'
273	    rows:
274	    - - Method
275	      - Edges
276	      - CPR
277	      - CPR/edge
278	    - - CSS=1.0
279	      - '48'
280	      - '0.08'
281	      - '0.00167'
282	    - - EAP-IG
283	      - '100'
284	      - '0.10'
285	      - '0.00100'
286	    - - EP
287	      - '100'
288	      - '0.06'
289	      - '0.00060'
290	    - - IFR
291	      - '100'
292	      - '0.07'
293	      - '0.00070'
294	  figures_description:
295	  - 'Fig: Qwen IOI Jaccard heatmap — 三对 Jaccard 均在 0.45-0.52，无明显 low-correlation pair'
296	  - 'Fig: CPR vs edge count scatter (Qwen IOI) — CSS=1.0 在 Pareto front 上但优势微弱'
297	  analysis: 'IFR 的引入未能打破 gradient-method 相关性困境。虽然 IFR 名义上属于不同 algorithmic family，
298	    但其在 transformer 上的行为与 gradient methods 高度相关——这是 worst 档的核心假设。 IOI 在 Qwen 上 CSS
299	    的 CPR 优势 (-0.02) 处于噪声水平，与 GPT-2 IOI 的明确正面结果 (CPR=0.109 vs best single 0.029) 形成鲜明对比。这暗示
300	    GPT-2 IOI 的成功 可能依赖于其极端 localized 的 14-edge ACDC circuit（isinf binarization 的产物），
301	    而非 consensus 方法的内在优势。
302	
303	    '
304	- name: Qwen-2.5 0.5B Arithmetic K=3
305	  plan_id: plan_007
306	  description: 'Qwen-2.5 0.5B 上的 Arithmetic (Greaterthan)，K=3 with IFR。 验证 IFR 是否能在高相关任务上恢复
307	    CSS。
308	
309	    '
310	  expected_results:
311	    pairwise_jaccard:
312	      eapig_x_ep: 0.58
313	      eapig_x_ifr: 0.55
314	      ep_x_ifr: 0.5
315	    max_pairwise_jaccard: 0.58
316	    css_distribution:
317	      1/3: 22
318	      2/3: 68
319	      3/3: 52
320	    faithfulness_mean:
321	      css_1.00:
322	        edges: 52
323	        CPR: 0.9
324	        CMD: 0.15
325	      eapig:
326	        edges: 100
327	        CPR: 0.97
328	        CMD: 0.04
329	      ep:
330	        edges: 100
331	        CPR: 0.94
332	        CMD: 0.09
333	      ifr:
334	        edges: 100
335	        CPR: 0.92
336	        CMD: 0.12
337	    d025_verdict: 'FAIL (condition④: CSS=1.0 CPR=0.90 < EAP-IG=0.97)'
338	    method_diversity_1_minus_max_jaccard: 0.42
339	  result_rationale: 'Arithmetic 在 Qwen 上延续 GPT-2 的高相关模式。IFR 与 EAP-IG 的 Jaccard=0.55
340	    证实 similarity-based 方法未能提供独立视角。虽然 Qwen 的 EAP-IG×EP Jaccard (0.58) 比 GPT-2 (0.695)
341	    略低（因模型更大、电路更分散），但仍远高于 CSS 有效工作所需的阈值。 Arithmetic 作为数值比较任务，其计算通路在所有方法看来都很相似—— MLP
342	    中的 magnitude comparison 操作无论用 gradient、pruning 还是 feature removal 来检测， 排序都一致。CSS
343	    没有恢复。
344	
345	    '
346	  tables:
347	  - caption: 'Table: Qwen Arithmetic faithfulness (mean ablation)'
348	    rows:
349	    - - Method
350	      - Edges
351	      - CPR
352	      - CMD
353	    - - CSS=1.0
354	      - '52'
355	      - '0.90'
356	      - '0.15'
357	    - - EAP-IG
358	      - '100'
359	      - '0.97'
360	      - '0.04'
361	    - - EP
362	      - '100'
363	      - '0.94'
364	      - '0.09'
365	    - - IFR
366	      - '100'
367	      - '0.92'
368	      - '0.12'
369	  figures_description:
370	  - 'Fig: Qwen Arithmetic CSS distribution — 3/3 比例较高 (37%)，反映方法高一致性'
371	  analysis: 'Arithmetic 在两个模型上都失败，进一步支持 "task structure 决定 CSS utility" 的结论。 IFR 对
372	    method diversity 的贡献可以忽略。Worst 档的核心 thesis 成立： 在 transformer 上，所有主流 circuit discovery
373	    methods 共享底层 gradient 信息， 导致 consensus 退化。
374	
375	    '
376	- name: Gemma-2 2B IOI K=3
377	  plan_id: plan_008
378	  description: 'Scale 到 2B 模型 (Gemma-2)。IOI task，K=3 (EAP-IG + EP + IFR)。 验证 CSS 在更大模型上是否保持
379	    IOI 的正面结果。
380	
381	    '
382	  expected_results:
383	    pairwise_jaccard:
384	      eapig_x_ep: 0.42
385	      eapig_x_ifr: 0.48
386	      ep_x_ifr: 0.4
387	    max_pairwise_jaccard: 0.48
388	    css_distribution:
389	      1/3: 35
390	      2/3: 78
391	      3/3: 55
392	    faithfulness_mean:
393	      css_1.00:
394	        edges: 55
395	        CPR: 0.06
396	        CMD: 0.91
397	      eapig:
398	        edges: 100
399	        CPR: 0.07
400	        CMD: 0.9
401	      ep:
402	        edges: 100
403	        CPR: 0.04
404	        CMD: 0.93
405	      ifr:
406	        edges: 100
407	        CPR: 0.05
408	        CMD: 0.92
409	    css_1_cpr_vs_best_single: -0.01
410	    method_diversity_1_minus_max_jaccard: 0.52
411	  result_rationale: 'Gemma-2 2B 有 26 层 16 头，IOI circuit 比 GPT-2 的 12 层结构更分散。 更多参数意味着更多可能的
412	    edge pathways，pairwise Jaccard 自然降低（0.42-0.48）， 但这种降低是因为 circuit 变大变分散，而非方法真正独立。CSS=1.0
413	    的 55 条边 CPR=0.06 与 EAP-IG 的 0.07 差距 -0.01，在统计上不显著。 更大模型上 IOI 不再是极端 localized 的
414	    14-edge circuit—— GPT-2 上的 "IOI exception" 消失了。这强化了 IOI positive result 是 GPT-2
415	    特有 artifact 的论点。edge-efficiency (CPR/edge) 上 CSS 仍有优势 (0.00109 vs 0.00070)， 但绝对
416	    CPR 差为负。
417	
418	    '
419	  tables:
420	  - caption: 'Table: Gemma-2 IOI faithfulness (mean ablation)'
421	    rows:
422	    - - Method
423	      - Edges
424	      - CPR
425	      - CPR/edge
426	    - - CSS=1.0
427	      - '55'
428	      - '0.06'
429	      - '0.00109'
430	    - - EAP-IG
431	      - '100'
432	      - '0.07'
433	      - '0.00070'
434	    - - EP
435	      - '100'
436	      - '0.04'
437	      - '0.00040'
438	    - - IFR
439	      - '100'
440	      - '0.05'
441	      - '0.00050'
442	  figures_description:
443	  - 'Fig: Model scale vs CSS CPR advantage — 从 GPT-2 (+0.08) 到 Qwen (-0.02) 到 Gemma-2
444	    (-0.01)，趋势向零/负'
445	  analysis: 'Scale up 后 IOI 的 CSS 优势消失。GPT-2 IOI 的 positive result 越来越像 artifact：
446	    ACDC isinf 在 GPT-2 上产生极端 sparse circuit (14 edges)，而这 14 条边恰好是 高质量的——这是 GPT-2
447	    IOI 特有的幸运巧合，而非 consensus 方法的系统性优势。 在更大模型上，没有 ACDC isinf 的极端 sparsity，CSS 就退化为方法交集的
448	    artifact。
449	
450	    '
451	- name: Llama-3.1 8B IOI K=3
452	  plan_id: plan_009
453	  description: '最大规模实验。Llama-3.1 8B，IOI task，K=3。需要 A100 80GB。
454	
455	    '
456	  expected_results:
457	    pairwise_jaccard:
458	      eapig_x_ep: 0.38
459	      eapig_x_ifr: 0.44
460	      ep_x_ifr: 0.36
461	    max_pairwise_jaccard: 0.44
462	    circuit_sizes:
463	      eapig: 100
464	      ep: 100
465	      ifr: 100
466	    css_distribution:
467	      1/3: 42
468	      2/3: 82
469	      3/3: 60
470	    faithfulness_mean:
471	      css_1.00:
472	        edges: 60
473	        CPR: 0.04
474	        CMD: 0.94
475	      eapig:
476	        edges: 100
477	        CPR: 0.05
478	        CMD: 0.93
479	    css_1_cpr_vs_best_single: -0.01
480	    practical_note: EP 在 8B 上 GPU memory 紧张，需 gradient checkpointing，运行时间 ~6h
481	  result_rationale: '8B 模型有 32 层 32 头，edge space 巨大（~100K potential edges）。 k=100
482	    只覆盖 edge space 的 0.1%，导致 pairwise Jaccard 自然降低（稀释效应）， 但这不代表方法独立——它们在各自 top-100
483	    中识别的 functional role (e.g., induction heads, name mover heads) 相同，只是具体 edge indices
484	    因模型结构更大而分散。 CSS=1.0 的 60 条边 CPR=0.04 仅与 EAP-IG 差 -0.01。 在如此大的模型上，k=100 本身就是 underpowered——所有方法都在极度
485	    undersample， consensus 变得 trivially similar to random intersection。 这个实验最大的价值是展示
486	    "fixed-k consensus doesn''t scale"。
487	
488	    '
489	  tables:
490	  - caption: 'Table: Llama-3.1 8B IOI results summary'
491	    rows:
492	    - - Method
493	      - Edges
494	      - CPR
495	      - Max Jaccard
496	    - - CSS=1.0
497	      - '60'
498	      - '0.04'
499	      - —
500	    - - EAP-IG
501	      - '100'
502	      - '0.05'
503	      - '0.44'
504	    - - EP
505	      - '100'
506	      - '0.03'
507	      - —
508	    - - IFR
509	      - '100'
510	      - '0.04'
511	      - —
512	  figures_description:
513	  - 'Fig: Jaccard vs model size — Jaccard 随 model size 下降但 CSS advantage 也下降，表明低 Jaccard
514	    是稀释而非真正的方法独立性'
515	  analysis: '8B 实验的 ROI 极低。高 GPU 成本 (24h A100) 仅产生一个不显著的数据点。 在 analysis paper 中可作为
516	    "scaling caveat" 一段提及，但不值得单独的 figure。 Worst 档建议砍掉此实验以节省资源，或降为 appendix-only。
517	
518	    '
519	- name: Binarization sensitivity ablation
520	  plan_id: plan_010
521	  description: '系统性 top-k sweep (k=50, 75, 100, 150, 200) 在所有 model×task 对上， 验证 CSS
522	    在不同 k 下的稳定性。
523	
524	    '
525	  expected_results:
526	    ioi_gpt2_css_cpr_by_k:
527	      k50: 0.095
528	      k75: 0.1
529	      k100: 0.105
530	      k150: 0.098
531	    sva_gpt2_css_cpr_by_k:
532	      k50: 0.88
533	      k75: 0.87
534	      k100: 0.86
535	      k150: 0.85
536	    arithmetic_gpt2_css_cpr_by_k:
537	      k50: 0.919
538	      k75: 0.91
539	      k100: 0.905
540	      k150: 0.895
541	    css_stable_across_k: true
542	    but_advantage_never_positive_except_ioi: true
543	    key_finding: 'CSS CPR 在 k=50-150 范围内稳定（std < 0.02），但这仅说明 binarization 本身不是 CSS
544	      失败的原因——方法相关性才是。Worst 档的附加发现： ACDC isinf-vs-topk 的 Jaccard 差异驱动了 Jaccard-utility
545	      的虚假关联。
546	
547	      '
548	    acdc_isinf_vs_topk_jaccard_gap:
549	      ioi: isinf Jaccard=0.09 → topk Jaccard=0.25 (Δ=+0.16)
550	      arithmetic: isinf Jaccard=0.17 → topk Jaccard=0.42 (Δ=+0.25)
551	      sva: isinf Jaccard=0.14 → topk Jaccard=0.35 (Δ=+0.21)
552	  result_rationale: 'Binarization (isinf vs top-k) 直接影响 ACDC 的 circuit size，进而影响 pairwise
553	    Jaccard 和 CSS=1.0 的含义。isinf 下 ACDC 极度 sparse（14-35 edges）， 与 gradient methods
554	    的 Jaccard 极低；top-k 归一化后 Jaccard 显著上升。 这意味着之前观察到的 "low Jaccard → CSS works (IOI)"
555	    关系中，IOI 的 low Jaccard 部分由 isinf binarization 驱动。去除这个 confound 后，IOI 的 max Jaccard
556	    从 0.31 上升到约 0.25（top-k normalized，EAP-IG×EP pair）， CSS 的优势主要来自 ACDC isinf 的 extreme
557	    selection 而非 genuine consensus。 这是 worst 档 Jaccard-utility 关系 "被 confound 驱动"
558	    假设的关键证据。
559	
560	    '
561	  tables:
562	  - caption: 'Table: CSS=1.0 CPR across binarization k values'
563	    rows:
564	    - - Task
565	      - k=50
566	      - k=75
567	      - k=100
568	      - k=150
569	      - Stable?
570	    - - IOI (GPT-2)
571	      - '0.095'
572	      - '0.100'
573	      - '0.105'
574	      - '0.098'
575	      - 'Yes'
576	    - - SVA (GPT-2)
577	      - '0.88'
578	      - '0.87'
579	      - '0.86'
580	      - '0.85'
581	      - 'Yes'
582	    - - Arith (GPT-2)
583	      - '0.919'
584	      - '0.910'
585	      - '0.905'
586	      - '0.895'
587	      - 'Yes'
588	  - caption: 'Table: ACDC binarization method effect on Jaccard'
589	    rows:
590	    - - Task
591	      - Jaccard (isinf)
592	      - Jaccard (top-k)
593	      - Δ
594	    - - IOI
595	      - '0.09'
596	      - '0.25'
597	      - '+0.16'
598	    - - Arith
599	      - '0.17'
600	      - '0.42'
601	      - '+0.25'
602	    - - SVA
603	      - '0.14'
604	      - '0.35'
605	      - '+0.21'
606	  figures_description:
607	  - 'Fig: CPR vs k for each task — 平坦曲线，CSS stable 但永远不 beat single method (except
608	    IOI)'
609	  - 'Fig: ACDC isinf vs top-k Jaccard — 证明 binarization confound'
610	  analysis: '这是 worst 档下最有分析价值的实验。证明两件事：(1) CSS 对 binarization 稳定——好消息； (2) 但 Jaccard-utility
611	    关系的很大一部分方差由 ACDC binarization choice 解释， 而非 genuine method diversity——坏消息。这为 analysis
612	    paper 提供了 "ACDC binarization pathology 的完整 taxonomy" 贡献（Claim 3 的延伸）， 也是 ''When
613	    Does Consensus Fail'' 叙事的核心技术贡献。
614	
615	    '
616	- name: Ablation method comparison (zero vs mean vs resample)
617	  plan_id: plan_011
618	  description: '在所有 task 上比较 zero ablation、mean ablation、resample ablation 下 CSS 的
619	    faithfulness advantage，验证 CSS 优势是否对 evaluation choice robust。
620	
621	    '
622	  expected_results:
623	    ioi_gpt2:
624	      zero:
625	        css_1_cpr: 0.109
626	        best_single_cpr: 0.029
627	        advantage: 0.08
628	      mean:
629	        css_1_cpr: 0.095
630	        best_single_cpr: 0.088
631	        advantage: 0.007
632	      resample:
633	        css_1_cpr: 0.085
634	        best_single_cpr: 0.082
635	        advantage: 0.003
636	    sva_gpt2:
637	      zero:
638	        css_1_cpr: -0.05
639	        best_single_cpr: -0.03
640	        advantage: -0.02
641	      mean:
642	        css_1_cpr: 0.88
643	        best_single_cpr: 0.95
644	        advantage: -0.07
645	      resample:
646	        css_1_cpr: 0.8
647	        best_single_cpr: 0.87
648	        advantage: -0.07
649	    arithmetic_gpt2:
650	      zero:
651	        css_1_cpr: -0.184
652	        best_single_cpr: -0.131
653	        advantage: -0.053
654	      mean:
655	        css_1_cpr: 0.919
656	        best_single_cpr: 0.985
657	        advantage: -0.066
658	      resample:
659	        css_1_cpr: 0.85
660	        best_single_cpr: 0.92
661	        advantage: -0.07
662	    key_finding: 'IOI 的 CSS 优势在 zero ablation 下最大 (+0.08)，mean ablation 下微弱 (+0.007)，
663	      resample 下几乎消失 (+0.003)。其他任务在所有 ablation 下 CSS 都不优。 这意味着 IOI positive result
664	      部分依赖于 zero ablation 的破坏性—— zero ablation 对小 circuit 更友好（破坏比例更低），放大了 CSS=1.0
665	      的 edge-efficiency 优势。
666	
667	      '
668	  result_rationale: 'Zero ablation 将 ablated edges 置零，对大 circuit（100 edges）的破坏程度远大于
669	    小 circuit（14 edges），因为更多路径被切断。这给了 CSS=1.0 (14 edges) 一个 不公平的优势——不是因为它的 edges 更好，而是因为
670	    100-edge circuits 在 zero ablation 下 suffer disproportionately。Mean ablation 缓解了这个
671	    bias（替换为 mean 而非 0）， 导致大小 circuit 的 CPR 趋近。Resample ablation 进一步消除 out-of-distribution
672	    artifacts。在 SVA 和 Arithmetic 上，即使在对 CSS 最有利的 zero ablation 下， gradient methods
673	    的高相关性也阻止了 CSS 产生优势。
674	
675	    '
676	  tables:
677	  - caption: 'Table: CSS advantage across ablation methods'
678	    rows:
679	    - - Task
680	      - Zero Δ
681	      - Mean Δ
682	      - Resample Δ
683	    - - IOI
684	      - '+0.080'
685	      - '+0.007'
686	      - '+0.003'
687	    - - SVA
688	      - '-0.020'
689	      - '-0.070'
690	      - '-0.070'
691	    - - Arithmetic
692	      - '-0.053'
693	      - '-0.066'
694	      - '-0.070'
695	  figures_description:
696	  - 'Fig: Grouped bar chart — CSS CPR advantage by ablation method × task，IOI 的 zero
697	    ablation 优势显眼但 mean/resample 下消失'
698	  analysis: 'Worst 档下此实验揭示 IOI positive result 的第二个 confound（除 ACDC isinf 外）： zero
699	    ablation bias。这对 paper 是双刃剑——削弱了唯一的正面证据， 但为 analysis paper 提供了 "evaluation method
700	    confounds in circuit faithfulness" 的重要方法论贡献。建议在 paper 中诚实报告并讨论，这种 transparency
701	    反而加分。
702	
703	    '
704	- name: CIRCUS as negative ablation
705	  plan_id: plan_012
706	  description: '整理 D021 的 CIRCUS 三次失败结果，作为负面消融实验展示 structural consensus (CSS) vs faithfulness
707	    scoring (CIRCUS) 的区别。
708	
709	    '
710	  expected_results:
711	    circus_ioi_cpr: -0.108
712	    circus_sva_cpr: -0.15
713	    circus_arithmetic_cpr: -0.12
714	    circus_failure_rate: 3/3 tasks
715	    css_vs_circus_framing: 'CIRCUS 在所有任务上 CPR 为负（比 random circuit 还差）， 而 CSS 至少在 IOI
716	      上为正。但 worst 档下 CSS 在 3/4 任务上也失败， 所以 CSS vs CIRCUS 的对比变成 "both methods have severe
717	      limitations" 而非 "CSS > CIRCUS"。
718	
719	      '
720	  result_rationale: 'CIRCUS 使用 threshold diversity 在单一方法内部构建 consensus， 本质上是在同一 gradient
721	    landscape 上做不同切分——不提供新信息。 CSS 至少使用了不同方法，但当方法本身相关时也退化。 CIRCUS 的完全失败是可预期的：单方法 threshold
722	    sweep 生成的 "diverse" circuits 实际上是 nested sets（k=50 ⊂ k=100 ⊂ k=150），其交集就是最 conservative
723	    的 cut， 这不是 consensus 而是 trivial intersection。
724	
725	    '
726	  tables:
727	  - caption: 'Table: CIRCUS vs CSS faithfulness comparison'
728	    rows:
729	    - - Method
730	      - IOI CPR
731	      - SVA CPR
732	      - Arith CPR
733	    - - CIRCUS
734	      - '-0.108'
735	      - '-0.15'
736	      - '-0.12'
737	    - - CSS=1.0
738	      - '+0.109'
739	      - '-0.05'
740	      - -0.184 (zero) / +0.919 (mean)
741	    - - Best single
742	      - +0.029 (zero)
743	      - +0.95 (mean)
744	      - +0.985 (mean)
745	  figures_description:
746	  - 'Fig: CIRCUS vs CSS CPR across tasks — CIRCUS consistently negative, CSS mixed'
747	  analysis: 'CIRCUS 负面结果是 low-hanging fruit——容易写、审稿人会觉得有信息量。 在 analysis paper 中定位为
748	    "what definitely doesn''t work"， 与 CSS 的 "works under specific conditions" 形成对比。
749	    0 GPU hours，纯分析工作，性价比最高的 planned 实验。
750	
751	    '
752	- name: Jaccard-CSS correlation analysis
753	  plan_id: plan_013
754	  description: '跨所有 model×task 对，拟合 max pairwise Jaccard vs CSS faithfulness advantage
755	    的关系。 Worst 档下数据点少且关系被 confound 驱动。
756	
757	    '
758	  expected_results:
759	    data_points:
760	    - task: IOI
761	      model: GPT-2
762	      max_jaccard: 0.31
763	      css_advantage: 0.08
764	      note: isinf ACDC, zero ablation
765	    - task: Arithmetic
766	      model: GPT-2
767	      max_jaccard: 0.695
768	      css_advantage: -0.066
769	      note: mean ablation
770	    - task: SVA
771	      model: GPT-2
772	      max_jaccard: 0.55
773	      css_advantage: -0.07
774	      note: mean ablation
775	    - task: IOI
776	      model: Qwen-0.5B
777	      max_jaccard: 0.52
778	      css_advantage: -0.02
779	      note: with IFR
780	    - task: Arithmetic
781	      model: Qwen-0.5B
782	      max_jaccard: 0.58
783	      css_advantage: -0.07
784	      note: with IFR
785	    - task: IOI
786	      model: Gemma-2B
787	      max_jaccard: 0.48
788	      css_advantage: -0.01
789	      note: with IFR
790	    n_data_points: 6
791	    spearman_rho: -0.54
792	    spearman_p_value: 0.27
793	    pearson_r: -0.61
794	    pearson_p_value: 0.2
795	    fitted_threshold: max_Jaccard < 0.35 for CSS to work
796	    n_points_below_threshold: 1
797	    n_points_above_threshold: 5
798	    confound_analysis: '去除 IOI GPT-2 (唯一用 ACDC isinf 且 zero ablation 的数据点) 后： n=5,
799	      spearman_rho=-0.30, p=0.62。关系完全不显著。 IOI GPT-2 是 influential point (Cook''s D
800	      > 1.0)，驱动了整个 correlation。
801	
802	      '
803	  result_rationale: '6 个数据点本身就 underpowered（Spearman 需 n≈10 才有检测 ρ=0.6 的 80% power）。
804	    Worst 档下唯一的正面点 (IOI GPT-2) 同时有两个 confounds： (1) ACDC isinf 压低了 max_Jaccard（top-k
805	    归一化后 Jaccard 上升到 0.25→仍低，但方向变化） (2) zero ablation 放大了 CSS 的 edge-efficiency 优势。
806	    去除这个 influential point 后，剩余 5 个点都在 Jaccard 0.48-0.70 范围内， CSS advantage 都在 [-0.07,
807	    -0.01] 范围内——flat line，no correlation。 Jaccard-utility 关系变成了 "one-point story"，统计上不可信。
808	
809	    '
810	  tables:
811	  - caption: 'Table: Jaccard-CSS correlation data'
812	    rows:
813	    - - Task×Model
814	      - Max Jaccard
815	      - CSS Advantage
816	      - Confounds
817	    - - IOI×GPT-2
818	      - '0.31'
819	      - '+0.080'
820	      - ACDC isinf + zero ablation
821	    - - SVA×GPT-2
822	      - '0.55'
823	      - '-0.070'
824	      - —
825	    - - Arith×GPT-2
826	      - '0.695'
827	      - '-0.066'
828	      - —
829	    - - IOI×Qwen
830	      - '0.52'
831	      - '-0.020'
832	      - IFR may ≈ gradient
833	    - - Arith×Qwen
834	      - '0.58'
835	      - '-0.070'
836	      - —
837	    - - IOI×Gemma
838	      - '0.48'
839	      - '-0.010'
840	      - —
841	  - caption: 'Table: Correlation robustness'
842	    rows:
843	    - - Analysis
844	      - ρ
845	      - p-value
846	      - n
847	    - - All points
848	      - '-0.54'
849	      - '0.27'
850	      - '6'
851	    - - Remove IOI×GPT-2
852	      - '-0.30'
853	      - '0.62'
854	      - '5'
855	    - - Remove ACDC tasks only
856	      - '-0.10'
857	      - '0.87'
858	      - '3'
859	  figures_description:
860	  - 'Fig: Scatter plot — max Jaccard (x) vs CSS advantage (y)，IOI×GPT-2 是明显的 outlier，其余点
861	    cluster 在右下区域'
862	  - 'Fig: Same scatter with IOI×GPT-2 标记为 hollow circle (confounded)，回归线变平'
863	  analysis: 这是 worst 档对 Claim 2 (CSS utility predicted by inter-method correlation)
864	    的致命打击。 Correlation 在统计上不显著 (p=0.27)，且由单个 confounded data point 驱动。 Paper 不能声称
865	    "Jaccard predicts CSS utility" 作为 empirical finding—— 只能作为 "motivated conjecture"
866	    或 "necessary condition hypothesis"。 Analysis paper 的重构方向：Jaccard 是 necessary condition
867	    check （max_Jaccard > 0.5 → CSS almost certainly fails）， 但不是 sufficient condition（max_Jaccard
868	    < 0.5 不保证 CSS works， 因为只有一个数据点且有 confounds）。 这限制了 contribution 的强度，但对 EMNLP Findings
869	    或 workshop 仍可接受—— honest negative results 有其学术价值。
870	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c52d921d-d60e-40dc-8339-b7091d931f28",
  "isSidechain": true,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "agentId": "a35a40d5f6dfb18b5",
  "type": "user",
  "uuid": "05fe3f7d-f329-4569-9040-39322a324084",
  "sourceToolAssistantUUID": "c52d921d-d60e-40dc-8339-b7091d931f28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-13T08:31:09.091Z_

Let me also check for any other relevant files that might contain plan information:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05fe3f7d-f329-4569-9040-39322a324084",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFocGScUHhHjho127Uf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bbae1bb1-c159-432a-8984-8ee268f6bb6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CoGdLaThLGX6oH869kDeFX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 50472,
      "cache_read_input_tokens": 17770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 50472,
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

_source line 20 · 2026-05-13T08:31:09.858Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Nnde75RKAwXQqoJXq6wtPw`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ -type f -name \"*experiment*\" -o -name \"*plan*\" | grep -v \".git\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bbae1bb1-c159-432a-8984-8ee268f6bb6d",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFocGScUHhHjho127Uf",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fb62fc04-8915-4511-b2e1-f67bfb20e77d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CoGdLaThLGX6oH869kDeFX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 50472,
      "cache_read_input_tokens": 17770,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 50472
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 124,
          "cache_read_input_tokens": 17770,
          "cache_creation_input_tokens": 50472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 50472,
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

_source line 21 · 2026-05-13T08:31:09.930Z_

<details><summary>↩ Tool result · `toolu_01Nnde75RKAwXQqoJXq6wtPw`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/workers/worker_code_phase2_experiment_framework_20260512T220705.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/workers/worker_code_phase2_experiment_framework_20260512T220705_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/experiment_plan.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/_project/data/run_phase2_experiment.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/best/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/run_phase2_experiment.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb62fc04-8915-4511-b2e1-f67bfb20e77d",
  "isSidechain": true,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "agentId": "a35a40d5f6dfb18b5",
  "type": "user",
  "uuid": "a86defdb-55c4-4ce0-84af-bcc6bd31bab4",
  "sourceToolAssistantUUID": "fb62fc04-8915-4511-b2e1-f67bfb20e77d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-13T08:31:11.107Z_

Let me check the experiment_plan.yaml to confirm it's empty and also check the memory.md:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a86defdb-55c4-4ce0-84af-bcc6bd31bab4",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFoqSTFkmzj1yFHbai7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aa94fc52-ff89-4814-a556-30444227b40a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JbTFTzAsx2eNeG2Af3rFrY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 68242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 700,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 23 · 2026-05-13T08:31:11.312Z_

<details open><summary>🔧 Tool call — Read · `toolu_017GUK8RMc5gwYvqzig2nyKZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa94fc52-ff89-4814-a556-30444227b40a",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFoqSTFkmzj1yFHbai7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9ea812e2-64f3-48cc-8b6b-1c4e7bf333dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JbTFTzAsx2eNeG2Af3rFrY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 68242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 700,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 24 · 2026-05-13T08:31:11.325Z_

<details><summary>↩ Tool result · `toolu_017GUK8RMc5gwYvqzig2nyKZ`</summary>

```text
1	experiments: []
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ea812e2-64f3-48cc-8b6b-1c4e7bf333dd",
  "isSidechain": true,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "agentId": "a35a40d5f6dfb18b5",
  "type": "user",
  "uuid": "52cefbfc-d8e0-4b44-bf34-32e75ab029c7",
  "sourceToolAssistantUUID": "9ea812e2-64f3-48cc-8b6b-1c4e7bf333dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T08:31:11.548Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ba4bESnk6Bz7sUjQ3KYBRX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52cefbfc-d8e0-4b44-bf34-32e75ab029c7",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFoqSTFkmzj1yFHbai7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2d1bc337-f15f-4307-bd1a-3ae404d917ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JbTFTzAsx2eNeG2Af3rFrY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 700,
      "cache_read_input_tokens": 68242,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 700
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 174,
          "cache_read_input_tokens": 68242,
          "cache_creation_input_tokens": 700,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 700,
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

_source line 26 · 2026-05-13T08:31:11.553Z_

<details><summary>↩ Tool result · `toolu_01Ba4bESnk6Bz7sUjQ3KYBRX`</summary>

```text
1	# Memory — structfuse-context
2	
3	## GPU 越界教训 (2026-05-13)
4	
5	第三次 GPU 越界事件：PID 897752 占用 cuda:0（属于 rl-active-probe-fl），导致对方数据丢失。根因：旧进程或直接运行库模块时未设 CUDA_VISIBLE_DEVICES，torch 默认使用 cuda:0。
6	
7	**硬规则**：
8	- 项目只有 cuda:5@cqa1-21977，所有 .py 文件（含库模块）必须在 import torch 前用 `os.environ.setdefault("CUDA_VISIBLE_DEVICES", "5")` 防护
9	- 入口脚本用 `os.environ["CUDA_VISIBLE_DEVICES"] = "5"`（强制覆盖），库模块用 `setdefault`（不覆盖入口已设的值）
10	- Worker 提交实验必须用 submit_training_job（自动管理 CUDA_VISIBLE_DEVICES），禁止 nohup
11	
12	## ACDC isinf 退化——核心方法论问题 (2026-05-13)
13	
14	ACDC binarization 用 `isinf` 只选出极少边（IOI 14, Arithmetic 17），但 ACDC 实际有 0.03-0.09 四级中间分数。isinf 导致 CSS=1.0 与 ACDC 完全重合，跨方法共识退化。top-k binarization（k=50-75）解决此问题：Arithmetic CSS 3/3 从 17→44-54。
15	
16	**但 top-k 未翻转条件④**：CSS=1.0 mean CPR=0.919 < EAP-IG=0.985。
17	
18	## D021: CSS-only 叙事 (2026-05-13)
19	
20	放弃 CIRCUS 作为独立 claim。转 CSS-only 叙事。
21	
22	## 竞争定位：CSS vs CIRCUS (2026-05-13)
23	
24	- **CIRCUS (Parekh, 2026)** 最大竞争对手。CSS 差异化 = method diversity > threshold diversity
25	- **Mondorf et al.** direct competitor：仅 gradient 族、score averaging（非 binary consensus）
26	- 关键支撑：Miller et al. (COLM 2024) faithfulness 对消融敏感；Méloux et al. EAP/EAP-IG 高方差
27	
28	## D026: MVP Gate 最终结论 (2026-05-13)
29	
30	**Arithmetic 条件④ FAIL（CSS=1.0 < EAP-IG），IOI PASS。**
31	
32	关键教训：
33	1. **Zero ablation 是 artifact 源**——所有小电路 zero CPR 为负，mean ablation 翻正到 0.9+
34	2. **节点级 ablation 的局限**——CSS=1.0 CPR 在 k=50→75 不变（节点集相同，边数变化无法区分）
35	3. **EAP-IG×EP 在 arithmetic 上 Jaccard=0.695**——两方法高度一致，CSS 缺少第三方视角的信息增益
36	4. **IOI 上 CSS 边效率极高**——14 edges CPR≈50 edges 单方法，每条边贡献远超单方法
37	5. **IOI CPR 不一致是误报**——mean_ablation_results.json 中标注为 IOI 的数据实际是 Arithmetic
38	
39	**等待 Director 决策：edge-efficiency claim / 原 claim + 更多任务 / pivot。**
40	
41	## IFR 作为第三方法——已证伪 (2026-05-13)
42	
43	**phase2_qwen05b_ioi_k3 (negative)**: Qwen-2.5 0.5B 上 IFR 与 EAP-IG/EP 的 Jaccard = 0.00。
44	
45	**D028 诊断结论**:
46	1. **Per-head 分解无效**: IFR 已经在用 per-head 分解，不是修复方向
47	2. **根本原因**: IFR (proximity) 度量 activation magnitude → 偏向高幅度 MLP 输出 (m2, m20, m22)；gradient 方法度量 causal influence → 偏向任务关键 attention heads (a20.h9)。两者解构的是不同维度
48	3. **Jaccard sweep**: 首次非零在 N=500 (J=0.045)，unique_score_rank 展开到 2191 边也仅 J=0.065
49	4. **Destination-side 退化 100%**: 同层头共享 residual stream，所有头得到相同 destination score
50	
51	**结论**: IFR 不能作为 CSS 第三方法用于大模型。gradient 族内部仍有共识（EAP-IG×EP Jaccard=0.54）。Phase 2 需要替代第三方法（ACDC top-k 或另一个 gradient 方法）。
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d1bc337-f15f-4307-bd1a-3ae404d917ec",
  "isSidechain": true,
  "promptId": "2fa59d90-4f34-4fb4-92b2-6f113da9e9bc",
  "agentId": "a35a40d5f6dfb18b5",
  "type": "user",
  "uuid": "90ed95ad-7960-4627-81e8-9aaac6bd2017",
  "sourceToolAssistantUUID": "2d1bc337-f15f-4307-bd1a-3ae404d917ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-13T08:31:34.733Z_

Perfect! Now I have all the information I need. Let me compile a comprehensive summary of the planned experiments.

## Summary: Planned Experiments in structfuse-context

Based on my thorough review of the project files, I found that **experiment_plan.yaml is indeed empty**, but the planned experiments are comprehensively defined in the **imagined_experiments.yaml files** from the dream reports (best/median/worst tiers dated 2026-05-13).

### **Key Finding: Three Experiment Plan Tiers**

The project uses a "dream" simulation approach with three narrative tiers (best/median/worst), each containing detailed imagined experiments with plan_ids. Here are the **PLANNED (not yet done) experiments**:

---

## **BEST TIER** — Most Optimistic Scenario
Plan IDs: **plan_004 through plan_013**

### Core Planned Experiments:
1. **plan_004** — GPT-2 Small Subject-Verb Agreement (SVA) K=3 CSS
   - Methods: EAP-IG + EP + ACDC
   - Expected result: CSS 优势（low Jaccard 0.22 → CSS CPR=0.12）

2. **plan_005** — GPT-2 Small Factual Recall K=3 CSS
   - Methods: EAP-IG + EP + ACDC
   - Expected: Distributed task, medium Jaccard (0.48) → CSS margin (CPR advantage=0.018)

3. **plan_006** — Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + IFR)
   - **IFR as third method** (similarity-based, different from gradient methods)
   - Expected: Lower Jaccard (0.28) → stronger CSS CPR (0.14)

4. **plan_007** — Qwen-2.5 0.5B Arithmetic K=3 (EAP-IG + EP + IFR)
   - Testing if IFR breaks high-correlation arithmetic pattern
   - Expected: max_Jaccard 0.58 (still high), CSS negative

5. **plan_008** — Gemma-2 2B IOI K=3 (EAP-IG + EP + IFR)
   - Scale validation to 2B model
   - Expected: CSS=1.0 CPR=0.13, advantage 0.09

6. **plan_009** — Llama-3.1 8B IOI K=3 (EAP-IG + EP + IFR)
   - Stretch goal: 8B model validation
   - Expected: CSS CPR=0.12, similar to smaller models

7. **plan_010** — Top-k Binarization Sensitivity Sweep
   - Systematic k sweep (50/75/100/150) on all completed tasks
   - Response to R5 (k robustness)
   - Expected: CSS=1.0 CPR stable, k-robust

8. **plan_011** — Ablation Method Comparison (Zero vs Mean vs Resample)
   - Compare evaluation methods on IOI and SVA
   - Expected: CSS advantage stable across ablations

9. **plan_012** — CIRCUS vs CSS Negative Ablation
   - Compare CIRCUS (threshold diversity) vs CSS (cross-method consensus)
   - Expected: CIRCUS fails (CPR=-0.108), CSS wins on IOI

10. **plan_013** — Jaccard-CSS Utility Correlation Analysis (KEY ANALYSIS)
    - Core data: 6 model×task pairs (IOI/SVA/Factual/Arithmetic × GPT-2/Qwen/Gemma)
    - Spearman ρ=0.94 (p=0.005) — **threshold ≈0.53**
    - **This is the crown jewel figure** showing (1-max_Jaccard) vs CSS advantage correlation

---

## **MEDIAN TIER** — Realistic Scenario
Plan IDs: **plan_004 through plan_013** (partial completion)

### Status of Plans:
- **plan_004** (SVA) — DONE, but partial support (CSS marginal, not superior)
- **plan_005** (Factual) — ABANDONED (GPT-2 Small factual recall too weak, ACDC failed)
- **plan_006** (Qwen IOI) — DONE, mixed results (IFR×EP Jaccard=0.55, higher than expected)
- **plan_007** (Qwen Arithmetic) — DONE, negative (CSS-1.0 CPR=0.932 < EAP-IG=0.971)
- **plan_008** (Gemma-2) — NOT ATTEMPTED (P2 priority, time constraints)
- **plan_009** (Llama-3.1 8B) — NOT ATTEMPTED (P3 priority, A100 80GB required)
- **plan_010** (k-sweep) — DONE, stable (k=75-150 range recommended)
- **plan_011** (ablation methods) — PARTIAL (IOI only, plan_013 listed as "not completed")
- **plan_012** (CIRCUS ablation) — DONE (CIRCUS cores CPR negative)
- **plan_013** (Jaccard correlation) — DONE (5 data points, Spearman ρ=-0.9 p=0.037)

---

## **WORST TIER** — Pessimistic Scenario
Plan IDs: **plan_004 through plan_013**

### Key findings:
- **Method correlation is systematic** — gradient methods (EAP-IG, EP) high correlation even on different tasks (Jaccard 0.48-0.62)
- **IFR doesn't provide independence** — similarity-based scoring correlates with gradient in transformer (Jaccard 0.45-0.52)
- **K_eff ≈ 1.5-1.8** (not true K=3 independence)
- **Only IOI positive** — likely artifact of ACDC isinf extreme sparsity (14 edges) + zero ablation bias
- **Jaccard-CSS correlation is confounded** — remove IOI/GPT-2 and ρ collapses to -0.30 (p=0.62)

---

## **Phase 2 Configuration (Already Defined)**

From `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/phase2_configs.yaml`:

**GPT-2 Small experiments:**
- gpt2_ioi (Priority 1 — MVP baseline)
- gpt2_greater_than (Priority 2)
- gpt2_docstring (Priority 2)

**Qwen-2.5 0.5B experiments (4 tasks):**
- qwen05_ioi (Priority 2)
- qwen05_greater_than (Priority 2)
- qwen05_docstring (Priority 2)
- qwen05_ioi_variant (Priority 3)

**Gemma-2 2B experiments (4 tasks, Priority 3):**
- gemma2_ioi, gemma2_greater_than, gemma2_docstring, gemma2_ioi_variant

**Llama-3.1 8B experiments (4 tasks, Priority 3):**
- llama31_ioi, llama31_greater_than, llama31_docstring, llama31_ioi_variant

---

## **What "Qwen ACDC" or "Phase 2" means:**

- **Phase 2** = After MVP completion, running full K=3 CSS computations across all 4 models × 4 tasks
- Currently in **Phase 1 (MVP pilot)**: Just validating CSS concept on GPT-2 Small with IOI and Arithmetic
- **Large model strategy (D006)**: Use IFR (Iterative Feature Removal) as 3rd method for large models (Qwen, Gemma, Llama), not ACDC
- **Qwen ACDC decision**: Actually **D029 reversed this** — switched from IFR back to ACDC top-k after discovering IFR zero-overlap issue

---

## **Critical Status Notes (from ROADMAP.md):**

- **Current blocker**: Awaiting mvp_arithmetic_gpt2_k3 completion → gate judgment
- **MVP gate rule**: If off-diagonal ≥5%, proceed to Phase 2; if 2-5%, confirm with Arithmetic; if <2%, kill
- **ARR deadline**: 2026-05-25 (12 days from 2026-05-13)
- **Next immediate task**: Write paper_framing.md + populate experiment_plan.yaml (currently empty!)

---

**In summary**: You have comprehensive planned experiment definitions in the dream reports (best/median/worst tiers), with plan_ids ranging from **plan_004 to plan_013**. The BEST tier shows the most ambitious 10-experiment plan for a strong paper; MEDIAN is more realistic with partial completions; WORST assumes method correlation defeats CSS. The empty experiment_plan.yaml should be populated from these imagined_experiments.yaml files once the Director makes tier selection.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90ed95ad-7960-4627-81e8-9aaac6bd2017",
  "isSidechain": true,
  "agentId": "a35a40d5f6dfb18b5",
  "requestId": "req_011CazFoxe3U5k8nDfJ1Cpoy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "52c9c367-7ef5-46a4-90df-136a0460cdf8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "9fa4408e-fc3a-466c-8bb9-049ddeee63fb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MQXTDLMeBG4xzS4bAX8EKq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1742,
      "cache_read_input_tokens": 68942,
      "output_tokens": 2240,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1742
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2240,
          "cache_read_input_tokens": 68942,
          "cache_creation_input_tokens": 1742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1742,
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
