# Research conversation: In /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/, find and read the following files: 1. R

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aa6e698b89154230b.jsonl`
- **Structured JSON:** [`64a2a1ae7b76d1e0fa70.json`](../../sessions/64/64a2a1ae7b76d1e0fa70.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

24 recorded events

### User

_source line 1 · 2026-05-13T08:44:12.353Z_

In /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/, find and read the following files:
1. ROADMAP.md or any roadmap file
2. All files in artifacts/dream_reports/ - especially the imagined_experiments.yaml files and experiment_data.json files
3. Any file that defines planned/remaining experiments

Read these files fully. I need to understand what experiments are planned but not yet completed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a58b825b-71c5-48ad-a01b-a7815951ccb9",
  "agentId": "aa6e698b89154230b",
  "type": "user",
  "uuid": "b7387ba3-69ed-47ab-8a20-e92e2d1484ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-13T08:44:13.265Z_

I'll help you find and read those files. Let me start by exploring the directory structure and locating the relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7387ba3-69ed-47ab-8a20-e92e2d1484ce",
  "isSidechain": true,
  "agentId": "aa6e698b89154230b",
  "requestId": "req_011CazGoWdycWspSQ4vumfsQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "be898aa1-d966-4a42-891a-972bed6b3708",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MiqmGSmzfi47AoXyUXAywE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 532,
      "cache_read_input_tokens": 13807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 532,
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

_source line 3 · 2026-05-13T08:44:13.645Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BWewFsUr1HG3ZACLwCKFpp`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ -type f -name \"*roadmap*\" -o -name \"*ROADMAP*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be898aa1-d966-4a42-891a-972bed6b3708",
  "isSidechain": true,
  "agentId": "aa6e698b89154230b",
  "requestId": "req_011CazGoWdycWspSQ4vumfsQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7e67584b-6f74-4439-b12b-064c01a0a61a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MiqmGSmzfi47AoXyUXAywE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 532,
      "cache_read_input_tokens": 13807,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 532
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 132,
          "cache_read_input_tokens": 13807,
          "cache_creation_input_tokens": 532,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 532,
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

_source line 4 · 2026-05-13T08:44:13.703Z_

<details><summary>↩ Tool result · `toolu_01BWewFsUr1HG3ZACLwCKFpp`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/workers/worker_knowledge_update-roadmap-tasks_20260513T031304.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/workers/worker_knowledge_update-roadmap-tasks_20260513T031304_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/chats/worker_knowledge_update-roadmap-tasks_20260513T031304.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/logs/chats/worker_knowledge_update-roadmap-tasks_20260513T031304.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ROADMAP.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ROADMAP.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e67584b-6f74-4439-b12b-064c01a0a61a",
  "isSidechain": true,
  "promptId": "a58b825b-71c5-48ad-a01b-a7815951ccb9",
  "agentId": "aa6e698b89154230b",
  "type": "user",
  "uuid": "8fbb5cc9-d61f-4545-a8ab-53c09ccadd20",
  "sourceToolAssistantUUID": "7e67584b-6f74-4439-b12b-064c01a0a61a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-13T08:44:14.938Z_

Now let me look for the artifacts directory and the files you mentioned:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fbb5cc9-d61f-4545-a8ab-53c09ccadd20",
  "isSidechain": true,
  "agentId": "aa6e698b89154230b",
  "requestId": "req_011CazGocTE1NEkfCAhzN7hH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ec1c929d-0842-4988-8b25-589c010bd8e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F1GftR8jBYDG6NGG8up5qe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1209,
      "cache_read_input_tokens": 14339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1209,
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

_source line 6 · 2026-05-13T08:44:15.231Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01By8y5jVkZhhwL64ZqCbF7f`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/ -type f 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec1c929d-0842-4988-8b25-589c010bd8e4",
  "isSidechain": true,
  "agentId": "aa6e698b89154230b",
  "requestId": "req_011CazGocTE1NEkfCAhzN7hH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0739cad9-6eae-4692-815a-d1250600feb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01F1GftR8jBYDG6NGG8up5qe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1209,
      "cache_read_input_tokens": 14339,
      "output_tokens": 114,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1209
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 114,
          "cache_read_input_tokens": 14339,
          "cache_creation_input_tokens": 1209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1209,
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

_source line 7 · 2026-05-13T08:44:15.301Z_

<details><summary>↩ Tool result · `toolu_01By8y5jVkZhhwL64ZqCbF7f`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/paper.aux
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/paper.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/paper.out
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/logs/phase2_best_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/logs/phase2_median_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/logs/paper_agent_worst.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/logs/phase2_worst_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/logs/paper_agent_best.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/logs/phase1_attempt0.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/logs/review_worst.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/logs/paper_agent_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/logs/orchestrator.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/logs/review_median.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/logs/review_best.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/paper.aux
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/paper.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/paper.out
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/imagined_experiments.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0739cad9-6eae-4692-815a-d1250600feb4",
  "isSidechain": true,
  "promptId": "a58b825b-71c5-48ad-a01b-a7815951ccb9",
  "agentId": "aa6e698b89154230b",
  "type": "user",
  "uuid": "d8f22f1f-de9d-4723-9469-8c7cbf21a84d",
  "sourceToolAssistantUUID": "0739cad9-6eae-4692-815a-d1250600feb4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-13T08:44:16.465Z_

Good! Now let me read the ROADMAP.md file and collect all the imagined_experiments.yaml and experiment_data.json files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8f22f1f-de9d-4723-9469-8c7cbf21a84d",
  "isSidechain": true,
  "agentId": "aa6e698b89154230b",
  "requestId": "req_011CazGojKinBzHE2CypaVs8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b9c411b-2ea2-4b5a-bd3e-d21cca7f6ee5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WCvbifxftnejbZy1SHgJ1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 15548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1656,
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

_source line 9 · 2026-05-13T08:44:16.896Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PWctAB3spBeEfdZcLg5STd`</summary>

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
  "parentUuid": "0b9c411b-2ea2-4b5a-bd3e-d21cca7f6ee5",
  "isSidechain": true,
  "agentId": "aa6e698b89154230b",
  "requestId": "req_011CazGojKinBzHE2CypaVs8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6c9031c8-ef6a-4a08-8c33-35357aa28018",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WCvbifxftnejbZy1SHgJ1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 15548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1656,
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

_source line 10 · 2026-05-13T08:44:16.908Z_

<details><summary>↩ Tool result · `toolu_01PWctAB3spBeEfdZcLg5STd`</summary>

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
61	| D034 | 2026-05-13 | D034: Qwen ACDC 确认 CSS 跨模型 scaling 根本性失败——问题不在方法选择 | phase2_qwen05b_ioi_acdc_k3, phase2_qwen05b_ioi_k3, mvp_pilot_gpt2_ioi_v3 |
62	| D033 | 2026-05-13 | D033: SVA 判定降级为 inconclusive——单 seed Δ=0.013 不具鲁棒性 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |
63	| D032 | 2026-05-13 | D032: 条件④评估指标修正——必须用 css_1.00 而非 css_0.67 | mvp_sva_gpt2_k3_topk, mvp_sva_gpt2_k3 |
64	| D031 | 2026-05-13 | 统一 D025 条件④标准：zero PASS 或 mean Δ≥0.01，SVA 两次均判 neg | mvp_sva_gpt2_k3, mvp_sva_gpt2_k3_topk |
65	| D030 | 2026-05-13 | SVA D025 gate FAIL（zero FAIL / mean 边际 Δ=0.008）；发现 | mvp_sva_gpt2_k3_topk |
66	| D029 | 2026-05-13 | Phase 2 第三方法：放弃 IFR，改用 ACDC top-k。IFR 跨族分歧作为 Discu | phase2_qwen05b_ioi_k3 |
67	| D028 | 2026-05-13 | Phase 2 IFR 零重叠问题：暂停 Qwen/Gemma 新实验，先修 IFR per-hea | phase2_qwen05b_ioi_k3 |
68	| D027 | 2026-05-13 | MVP 最终判定：CSS faithfulness 优势 task-dependent（IOI PA | mvp_arithmetic_gpt2_k3, mvp_pilot_gpt2_ioi_v3 |
69	| D026 | 2026-05-13 | Arithmetic D025 gate FAIL（条件④），暂不判 MVP 结果，先做 ACDC  | mvp_arithmetic_gpt2_k3 |
70	| D025 | 2026-05-13 | 更新 Arithmetic gate 为 CSS-only 四条件标准（替代 D024 的单一 5% | mvp_arithmetic_gpt2_k3 |
71	
72	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c9031c8-ef6a-4a08-8c33-35357aa28018",
  "isSidechain": true,
  "promptId": "a58b825b-71c5-48ad-a01b-a7815951ccb9",
  "agentId": "aa6e698b89154230b",
  "type": "user",
  "uuid": "7b28c85b-9a97-4ebb-a4f1-b7807bea8050",
  "sourceToolAssistantUUID": "6c9031c8-ef6a-4a08-8c33-35357aa28018",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T08:44:17.142Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LYbvEHuuCGhajXBDxSp64N`</summary>

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
  "parentUuid": "7b28c85b-9a97-4ebb-a4f1-b7807bea8050",
  "isSidechain": true,
  "agentId": "aa6e698b89154230b",
  "requestId": "req_011CazGojKinBzHE2CypaVs8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5ccd42e9-8611-4208-be82-e7922aa01e01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WCvbifxftnejbZy1SHgJ1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 15548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1656,
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

_source line 12 · 2026-05-13T08:44:17.149Z_

<details><summary>↩ Tool result · `toolu_01LYbvEHuuCGhajXBDxSp64N`</summary>

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
  "parentUuid": "5ccd42e9-8611-4208-be82-e7922aa01e01",
  "isSidechain": true,
  "promptId": "a58b825b-71c5-48ad-a01b-a7815951ccb9",
  "agentId": "aa6e698b89154230b",
  "type": "user",
  "uuid": "3496c987-1efc-47ac-88c5-c1be23f4abcc",
  "sourceToolAssistantUUID": "5ccd42e9-8611-4208-be82-e7922aa01e01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T08:44:17.326Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LU1XTcLXoht9EmDrSpv9WB`</summary>

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
  "parentUuid": "3496c987-1efc-47ac-88c5-c1be23f4abcc",
  "isSidechain": true,
  "agentId": "aa6e698b89154230b",
  "requestId": "req_011CazGojKinBzHE2CypaVs8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "35554357-7782-4560-9fd5-d4c0cf45021c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WCvbifxftnejbZy1SHgJ1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 15548,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1656,
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

_source line 14 · 2026-05-13T08:44:17.332Z_

<details><summary>↩ Tool result · `toolu_01LU1XTcLXoht9EmDrSpv9WB`</summary>

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
  "parentUuid": "35554357-7782-4560-9fd5-d4c0cf45021c",
  "isSidechain": true,
  "promptId": "a58b825b-71c5-48ad-a01b-a7815951ccb9",
  "agentId": "aa6e698b89154230b",
  "type": "user",
  "uuid": "7713fef0-c385-4681-9b36-6b21cc3b05d6",
  "sourceToolAssistantUUID": "35554357-7782-4560-9fd5-d4c0cf45021c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T08:44:17.607Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N4iQAtKa6DZ32Qdds7HDzr`</summary>

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
  "parentUuid": "7713fef0-c385-4681-9b36-6b21cc3b05d6",
  "isSidechain": true,
  "agentId": "aa6e698b89154230b",
  "requestId": "req_011CazGojKinBzHE2CypaVs8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7a4712c7-fd4c-4eac-bb22-b0205825761b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WCvbifxftnejbZy1SHgJ1a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1656,
      "cache_read_input_tokens": 15548,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1656
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 375,
          "cache_read_input_tokens": 15548,
          "cache_creation_input_tokens": 1656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1656,
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

_source line 16 · 2026-05-13T08:44:17.614Z_

<details><summary>↩ Tool result · `toolu_01N4iQAtKa6DZ32Qdds7HDzr`</summary>

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
  "parentUuid": "7a4712c7-fd4c-4eac-bb22-b0205825761b",
  "isSidechain": true,
  "promptId": "a58b825b-71c5-48ad-a01b-a7815951ccb9",
  "agentId": "aa6e698b89154230b",
  "type": "user",
  "uuid": "e90af9f4-2573-4246-af10-67cfdd0562c1",
  "sourceToolAssistantUUID": "7a4712c7-fd4c-4eac-bb22-b0205825761b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-13T08:44:20.391Z_

Now let me find experiment_data.json files for each dream report:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e90af9f4-2573-4246-af10-67cfdd0562c1",
  "isSidechain": true,
  "agentId": "aa6e698b89154230b",
  "requestId": "req_011CazGoumX3wTTf5evcjsRy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "848b8411-7bb1-49f4-a65e-0d39cc11061a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WhVJVXds1c11pSyyKNfBY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 46053,
      "cache_read_input_tokens": 17204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 46053,
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

_source line 18 · 2026-05-13T08:44:21.490Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CqBBSD13CSgnix2d1pVhwu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "848b8411-7bb1-49f4-a65e-0d39cc11061a",
  "isSidechain": true,
  "agentId": "aa6e698b89154230b",
  "requestId": "req_011CazGoumX3wTTf5evcjsRy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "88a80ad4-da7d-4971-8da0-1ef3512b8505",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WhVJVXds1c11pSyyKNfBY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 46053,
      "cache_read_input_tokens": 17204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 46053,
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

_source line 19 · 2026-05-13T08:44:21.856Z_

<details><summary>↩ Tool result · `toolu_01CqBBSD13CSgnix2d1pVhwu`</summary>

```text
1	[
2	  {
3	    "name": "GPT-2 SVA K=3 CSS",
4	    "description": "Subject-Verb Agreement on GPT-2 Small, K=3 (EAP-IG + EP + ACDC with top-k=75). SVA 是相对 localized 的语法任务，预期方法间有中等分歧。\n",
5	    "results": {
6	      "status": "done",
7	      "conclusion": "partial_support",
8	      "pairwise_jaccard": {
9	        "eapig_x_ep": 0.38,
10	        "eapig_x_acdc_k75": 0.18,
11	        "ep_x_acdc_k75": 0.15
12	      },
13	      "max_jaccard": 0.38,
14	      "three_way_ratio": 0.067,
15	      "circuit_sizes": {
16	        "eapig_k75": 75,
17	        "ep_k75": 75,
18	        "acdc_k75": 75,
19	        "acdc_isinf": 22
20	      },
21	      "css_distribution": {
22	        "1/3": 148,
23	        "2/3": 54,
24	        "3/3": 23
25	      },
26	      "faithfulness_mean": {
27	        "css_1.00_k75": {
28	          "edges": 23,
29	          "CPR": 0.941,
30	          "CMD": 0.263
31	        },
32	        "css_0.67_k75": {
33	          "edges": 54,
34	          "CPR": 0.958,
35	          "CMD": 0.189
36	        },
37	        "eapig_k75": {
38	          "edges": 75,
39	          "CPR": 0.953,
40	          "CMD": 0.211
41	        },
42	        "ep_k75": {
43	          "edges": 75,
44	          "CPR": 0.937,
45	          "CMD": 0.284
46	        },
47	        "acdc_k75": {
48	          "edges": 75,
49	          "CPR": 0.922,
50	          "CMD": 0.347
51	        }
52	      },
53	      "faithfulness_isinf_degeneration": {
54	        "css_1.00_isinf": {
55	          "edges": 22,
56	          "CPR": 0.918,
57	          "CMD": 0.368
58	        },
59	        "acdc_isinf": {
60	          "edges": 22,
61	          "CPR": 0.918,
62	          "CMD": 0.368
63	        },
64	        "degeneration_confirmed": true
65	      },
66	      "css1_cpr_advantage_over_best": -0.012,
67	      "css1_edge_ratio": 0.307,
68	      "sva_gate_verdict": "MARGINAL — CSS=1.0 CPR comparable but not superior; edge efficiency 3.3x"
69	    },
70	    "tables": [
71	      {
72	        "name": "Table: SVA Faithfulness Comparison (mean ablation, top-k=75)",
73	        "columns": [
74	          "Circuit",
75	          "Edges",
76	          "CPR ↑",
77	          "CMD ↓",
78	          "Edge Ratio"
79	        ],
80	        "rows": [
81	          [
82	            "CSS=1.0 (k=75)",
83	            23,
84	            0.941,
85	            0.263,
86	            "0.31x"
87	          ],
88	          [
89	            "CSS≥0.67 (k=75)",
90	            54,
91	            0.958,
92	            0.189,
93	            "0.72x"
94	          ],
95	          [
96	            "EAP-IG (k=75)",
97	            75,
98	            0.953,
99	            0.211,
100	            "1.00x"
101	          ],
102	          [
103	            "EP (k=75)",
104	            75,
105	            0.937,
106	            0.284,
107	            "1.00x"
108	          ],
109	          [
110	            "ACDC (k=75)",
111	            75,
112	            0.922,
113	            0.347,
114	            "1.00x"
115	          ],
116	          [
117	            "ACDC (isinf)",
118	            22,
119	            0.918,
120	            0.368,
121	            "0.29x"
122	          ]
123	        ]
124	      },
125	      {
126	        "name": "Table: SVA Pairwise Jaccard (top-k=75)",
127	        "columns": [
128	          "",
129	          "EAP-IG",
130	          "EP",
131	          "ACDC"
132	        ],
133	        "rows": [
134	          [
135	            "EAP-IG",
136	            "—",
137	            0.38,
138	            0.18
139	          ],
140	          [
141	            "EP",
142	            0.38,
143	            "—",
144	            0.15
145	          ],
146	          [
147	            "ACDC",
148	            0.18,
149	            0.15,
150	            "—"
151	          ]
152	        ]
153	      }
154	    ],
155	    "figures": [],
156	    "analysis": "SVA 结果处于 IOI（CSS clear win）和 Arithmetic（CSS clear loss）之间的灰色地带。 CSS=1.0 用 23 条边达到了 75 条边 EAP-IG 的 98.7% faithfulness (0.941/0.953)， edge efficiency 论点成立但 CPR 没有优势。关键问题：top-k=75 是 SVA 上的最优 k， k=50 时 CSS=1.0 只有 15 条边且 CPR 降到 0.89，k=100 时 CSS=1.0 有 31 条边但 CPR 不再提升——这个 k-sensitivity 是 reviewer 可攻击的 degree of freedom。 对 Claim 1 的贡献：降级为 \"comparable faithfulness at fraction of edges\"。 对 Claim 2 的贡献：Jaccard=0.38 + CSS marginal → 第三个数据点，位于 IOI 和 Arithmetic 之间，方向一致。\n\n\nSVA 在 GPT-2 Small 上的电路比 IOI 更 localized（主要涉及 subject token 到 verb position 的 attention + 少量 MLP），但不如 IOI 那样有清晰的 \"备份名字\" 结构驱动方法分歧。EAP-IG 和 EP 作为 gradient-adjacent 方法在 SVA 上 Jaccard=0.38（高于 IOI 的 0.31），因为 SVA 的 gradient landscape 比 IOI 更平滑——主谓一致主要依赖几个 key attention head，gradient 方法容易收敛到 类似子集。ACDC top-k=75 normalization 打破了 isinf 退化（isinf 只有 22 条 edge），但引入了 k 的选择作为额外自由度。CSS=1.0 包含 23 条边，CPR=0.941 略低于 EAP-IG 的 0.953（差距 0.012）， 说明全共识子集在去除了各方法的 \"独特发现\" 后损失了少量信息。这符合 median 档预期：CSS 部分支持 但不完美，edge efficiency 优势（3.3x fewer edges）是实在的，但 faithfulness 并无优势。\n"
157	  },
158	  {
159	    "name": "GPT-2 DocQA/Factual K=3 CSS",
160	    "description": "Distributed computation task on GPT-2 Small. 预期高 Jaccard → CSS 应该失败（确认模式）。\n",
161	    "results": {
162	      "status": "abandoned",
163	      "conclusion": "data_not_clean",
164	      "partial_metrics": {
165	        "eapig_completed": true,
166	        "ep_completed": true,
167	        "acdc_completed": false,
168	        "acdc_failure_reason": "GPT-2 Small factual recall 太弱，ACDC 收敛到近空电路（< 5 edges）"
169	      },
170	      "note": "ACDC 无法产出有意义的电路，实验被终止。不纳入论文分析。"
171	    },
172	    "tables": [],
173	    "figures": [],
174	    "analysis": "第四任务失败是 median 档的核心限制。论文需要在 Limitations 中说明 GPT-2 Small 对 factual recall 的能力不足以支撑 circuit discovery，并将 broader task coverage 列为 future work。这会成为 reviewer 攻击的主要靶点（\"only 3 tasks on one model\"）。 应对策略：强调 3 个任务已覆盖 localized（IOI）、distributed（Arithmetic）、 intermediate（SVA）三种电路结构类型，以及 Qwen 上的 cross-model validation。\n\n\nGPT-2 Small (117M) 的 factual knowledge 极为有限，DocQA/Factual recall 任务上 模型本身准确率不稳定（~55-65% vs random 25%）。EAP-IG 和 EP 可以强行产出 top-k 电路，但 ACDC 的 patching-based 搜索在 clean performance 不稳定时无法收敛—— 阈值过高则电路为空，过低则几乎保留全图。尝试调低阈值后得到 3-5 条 isinf 边， top-k normalization 后虽能凑出 50-75 条边但其 faithfulness 接近随机（CPR ≈ 0）。 这不是 CSS 方法的失败而是 task-model 匹配问题。在 deadline 压力下（ARR 5/25） 决定放弃第四任务，论文保持 3 个任务（IOI + Arithmetic + SVA）。\n"
175	  },
176	  {
177	    "name": "Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + IFR)",
178	    "description": "首次 larger model + IFR 作为第三方法（替换 ACDC）。IFR 是 similarity-based 方法， 与 gradient 方法家族不同，预期降低 Jaccard。\n",
179	    "results": {
180	      "status": "done",
181	      "conclusion": "mixed",
182	      "pairwise_jaccard": {
183	        "eapig_x_ep": 0.42,
184	        "eapig_x_ifr": 0.19,
185	        "ep_x_ifr": 0.55
186	      },
187	      "max_jaccard": 0.55,
188	      "three_way_ratio": 0.082,
189	      "circuit_sizes": {
190	        "eapig_k75": 75,
191	        "ep_k75": 75,
192	        "ifr_k75": 75
193	      },
194	      "css_distribution": {
195	        "1/3": 143,
196	        "2/3": 63,
197	        "3/3": 19
198	      },
199	      "faithfulness_mean": {
200	        "css_1.00": {
201	          "edges": 19,
202	          "CPR": 0.103,
203	          "CMD": 0.921
204	        },
205	        "css_0.67": {
206	          "edges": 63,
207	          "CPR": 0.087,
208	          "CMD": 0.944
209	        },
210	        "eapig_k75": {
211	          "edges": 75,
212	          "CPR": 0.091,
213	          "CMD": 0.938
214	        },
215	        "ep_k75": {
216	          "edges": 75,
217	          "CPR": 0.078,
218	          "CMD": 0.952
219	        },
220	        "ifr_k75": {
221	          "edges": 75,
222	          "CPR": 0.064,
223	          "CMD": 0.967
224	        }
225	      },
226	      "css1_cpr": 0.103,
227	      "css1_vs_best_single": 0.012,
228	      "ifr_ep_correlation_note": "IFR×EP Jaccard=0.55 远高于预期。IFR 虽然是 similarity-based，但在 IOI 上 EP 的 edge importance 与 IFR 的 representation similarity 高度一致—— 可能因为 IOI 的 backup name 机制使得 \"重要的边\" 在两种度量下都突出。 这削弱了 K≈3 independent methods 的假设，实际独立证据更接近 K≈2.3。\n"
229	    },
230	    "tables": [
231	      {
232	        "name": "Table: Qwen-0.5B IOI Faithfulness (mean ablation, k=75)",
233	        "columns": [
234	          "Circuit",
235	          "Edges",
236	          "CPR ↑",
237	          "CMD ↓"
238	        ],
239	        "rows": [
240	          [
241	            "CSS=1.0",
242	            19,
243	            0.103,
244	            0.921
245	          ],
246	          [
247	            "CSS≥0.67",
248	            63,
249	            0.087,
250	            0.944
251	          ],
252	          [
253	            "EAP-IG",
254	            75,
255	            0.091,
256	            0.938
257	          ],
258	          [
259	            "EP",
260	            75,
261	            0.078,
262	            0.952
263	          ],
264	          [
265	            "IFR",
266	            75,
267	            0.064,
268	            0.967
269	          ]
270	        ]
271	      },
272	      {
273	        "name": "Table: Qwen-0.5B IOI Pairwise Jaccard",
274	        "columns": [
275	          "",
276	          "EAP-IG",
277	          "EP",
278	          "IFR"
279	        ],
280	        "rows": [
281	          [
282	            "EAP-IG",
283	            "—",
284	            0.42,
285	            0.19
286	          ],
287	          [
288	            "EP",
289	            0.42,
290	            "—",
291	            0.55
292	          ],
293	          [
294	            "IFR",
295	            0.19,
296	            0.55,
297	            "—"
298	          ]
299	        ]
300	      }
301	    ],
302	    "figures": [],
303	    "analysis": "Qwen IOI 结果是 \"mixed\" 的典型案例。好消息：CSS=1.0 在 larger model 上仍然 work， CPR 略优于 best single method，证明 CSS 框架可跨模型。坏消息：IFR×EP Jaccard=0.55 说明 \"不同算法家族 → 低相关\" 的假设不总成立——算法差异不等于 measurement independence。 这对 Claim 2 有双重影响：(1) max_jaccard=0.55 + CSS marginal win 支持 \"中等 Jaccard → 中等 CSS 收益\" 的连续关系假设；(2) 但也说明 Jaccard 可能需要分 pair 解读而非只看 max。 论文中应在 Discussion 讨论 IFR-EP 相关性的 mechanistic 原因。\n\n\nQwen-2.5 0.5B 上 IOI 的电路结构与 GPT-2 类似（名字 mover head + backup 机制）， 但模型更大导致电路更分散。EAP-IG×EP 的 Jaccard 从 GPT-2 的 0.31 升至 0.42， 因为 Qwen 的 gradient landscape 更平滑（more parameters → gradient 更 concentrated on true signal）。IFR 作为 similarity-based 方法确实与 EAP-IG 差异大（Jaccard=0.19）， 但与 EP 的 Jaccard 意外达到 0.55——这是因为 EP 的 edge pruning 和 IFR 的 representation similarity 都偏好 \"移除后 representation 变化大\" 的边，两者在 measurement 层面有隐含重叠。CSS=1.0 的 19 条边 CPR=0.103 略好于 GPT-2 IOI 的 0.109 （量级一致），表明 CSS 在 larger model 上仍然能提取 faithful 子集。但 max_jaccard=0.55 使得这个数据点在 Jaccard-utility 图上落在不太理想的位置——CSS 优势有限（+0.012 over EAP-IG）且 Jaccard 不够低。IFR 混入了与 EP 相关的信号，有效独立方法数 < 3。\n"
304	  },
305	  {
306	    "name": "Qwen-2.5 0.5B Arithmetic K=3",
307	    "description": "Qwen 上的 Arithmetic (Greaterthan) task，IFR 替换 ACDC。 验证 IFR 是否能降低 Arithmetic 的 Jaccard 使 CSS recover。\n",
308	    "results": {
309	      "status": "done",
310	      "conclusion": "negative",
311	      "pairwise_jaccard": {
312	        "eapig_x_ep": 0.61,
313	        "eapig_x_ifr": 0.38,
314	        "ep_x_ifr": 0.48
315	      },
316	      "max_jaccard": 0.61,
317	      "three_way_ratio": 0.195,
318	      "css_distribution": {
319	        "1/3": 98,
320	        "2/3": 73,
321	        "3/3": 54
322	      },
323	      "faithfulness_mean": {
324	        "css_1.00": {
325	          "edges": 54,
326	          "CPR": 0.932,
327	          "CMD": 0.302
328	        },
329	        "eapig_k75": {
330	          "edges": 75,
331	          "CPR": 0.971,
332	          "CMD": 0.128
333	        },
334	        "ep_k75": {
335	          "edges": 75,
336	          "CPR": 0.955,
337	          "CMD": 0.199
338	        },
339	        "ifr_k75": {
340	          "edges": 75,
341	          "CPR": 0.891,
342	          "CMD": 0.487
343	        }
344	      },
345	      "css1_cpr_advantage_over_best": -0.039,
346	      "note": "IFR 将 max_jaccard 从 GPT-2 的 0.695 降至 0.61，但仍不够低。 CSS=1.0 CPR=0.932 < EAP-IG=0.971。CSS 未 recover。\n"
347	    },
348	    "tables": [
349	      {
350	        "name": "Table: Qwen-0.5B Arithmetic Faithfulness (mean ablation)",
351	        "columns": [
352	          "Circuit",
353	          "Edges",
354	          "CPR ↑",
355	          "CMD ↓"
356	        ],
357	        "rows": [
358	          [
359	            "CSS=1.0",
360	            54,
361	            0.932,
362	            0.302
363	          ],
364	          [
365	            "EAP-IG (k=75)",
366	            75,
367	            0.971,
368	            0.128
369	          ],
370	          [
371	            "EP (k=75)",
372	            75,
373	            0.955,
374	            0.199
375	          ],
376	          [
377	            "IFR (k=75)",
378	            75,
379	            0.891,
380	            0.487
381	          ]
382	        ]
383	      }
384	    ],
385	    "figures": [],
386	    "analysis": "IFR \"部分修复\" 了 Arithmetic 的 Jaccard 问题但不够彻底。从 Claim 2 角度看 这其实是一个有价值的 intermediate data point：Jaccard 从 0.695 降到 0.61， CSS 优势从 -0.066 改善到 -0.039，方向正确但仍为负。如果画 Jaccard vs CSS_advantage 的图，这个点和 GPT-2 Arithmetic 几乎在同一条趋势线上。 问题在于 IFR 本身在 Arithmetic 上的 faithfulness 较差（CPR=0.891 远低于 EAP-IG 的 0.971），说明 similarity-based method 对 distributed computation 的识别 能力有限——这是一个独立的 finding，可在 Discussion 中报告。\n\n\nArithmetic/Greaterthan 任务的电路结构本质上是 distributed 的——多个 MLP layer 协同完成数值比较，gradient-based 方法容易收敛到相似的关键路径。IFR 替换 ACDC 后 确实降低了 max_jaccard（0.695 → 0.61），但降幅不够大。原因：Arithmetic 的 \"重要边\" 集中在少数 MLP 到 final position 的连接上，无论用 gradient (EAP-IG/EP) 还是 similarity (IFR)，这些边都会被 rank 到顶部。IFR 本身表现较弱（CPR=0.891）， 拖累了 CSS=1.0 的质量——共识要求三方都同意的边包含了 IFR 的一些 false positive。 这个结果实际上支持 Claim 2：Jaccard 仍然偏高（0.61）→ CSS 仍然不优—— 趋势一致，但不是正面结果。\n"
387	  },
388	  {
389	    "name": "Gemma-2 2B IOI K=3",
390	    "description": "Scale to 2B model (Gemma-2). P2 优先级。",
391	    "results": {
392	      "status": "not_attempted",
393	      "conclusion": null,
394	      "reason": "时间和 GPU 资源不足，P1 任务已消耗大部分 budget。列入 Future Work。"
395	    },
396	    "tables": [],
397	    "figures": [],
398	    "analysis": "Not attempted. 在 Limitations 中列为 model scale generalization future work。\n\nMedian 档的时间约束（ARR 5/25 deadline）下，plan_004 (SVA) + plan_006 (Qwen IOI) + plan_007 (Qwen Arith) 已消耗约 20 GPU-hours。Gemma-2 2B 需要 16 GPU-hours 且 依赖 plan_006 结果（IFR pipeline 验证）。即使 plan_006 顺利完成，剩余时间不足 以完成 Gemma-2 实验 + 分析 + 论文写作。P2 优先级下被合理推迟。\n"
399	  },
400	  {
401	    "name": "Llama-3.1 8B IOI K=3",
402	    "description": "Scale to 8B model. P3 优先级。Needs A100 80GB。",
403	    "results": {
404	      "status": "not_attempted",
405	      "conclusion": null,
406	      "reason": "P3 优先级，且 plan_008 未完成作为前置。远超 deadline 范围。"
407	    },
408	    "tables": [],
409	    "figures": [],
410	    "analysis": "Not attempted. Future work 中的 stretch goal。\n\n8B 模型实验需要 A100 80GB（当前设备可能不支持 EP 的内存需求），且依赖 plan_008。 在 median 档下属于完全不现实的目标。\n"
411	  },
412	  {
413	    "name": "Binarization sensitivity ablation",
414	    "description": "Systematic k sweep (k=50/75/100/150) on all completed model×task pairs. 验证 CSS 在不同 k 下的稳定性。\n",
415	    "results": {
416	      "status": "done",
417	      "conclusion": "partially_stable",
418	      "ioi_gpt2_k_sweep": {
419	        "k50": {
420	          "css_1.0_edges": 12,
421	          "css_1.0_cpr": 0.098
422	        },
423	        "k75": {
424	          "css_1.0_edges": 18,
425	          "css_1.0_cpr": 0.112
426	        },
427	        "k100": {
428	          "css_1.0_edges": 24,
429	          "css_1.0_cpr": 0.109
430	        },
431	        "k150": {
432	          "css_1.0_edges": 31,
433	          "css_1.0_cpr": 0.108
434	        },
435	        "verdict": "stable (CPR range 0.098-0.112, Δ=0.014)"
436	      },
437	      "arithmetic_gpt2_k_sweep": {
438	        "k50": {
439	          "css_1.0_edges": 44,
440	          "css_1.0_cpr": 0.919
441	        },
442	        "k75": {
443	          "css_1.0_edges": 54,
444	          "css_1.0_cpr": 0.919
445	        },
446	        "k100": {
447	          "css_1.0_edges": 62,
448	          "css_1.0_cpr": 0.926
449	        },
450	        "k150": {
451	          "css_1.0_edges": 71,
452	          "css_1.0_cpr": 0.933
453	        },
454	        "verdict": "stable (CPR range 0.919-0.933, Δ=0.014)"
455	      },
456	      "sva_gpt2_k_sweep": {
457	        "k50": {
458	          "css_1.0_edges": 15,
459	          "css_1.0_cpr": 0.891
460	        },
461	        "k75": {
462	          "css_1.0_edges": 23,
463	          "css_1.0_cpr": 0.941
464	        },
465	        "k100": {
466	          "css_1.0_edges": 29,
467	          "css_1.0_cpr": 0.944
468	        },
469	        "k150": {
470	          "css_1.0_edges": 38,
471	          "css_1.0_cpr": 0.94
472	        },
473	        "verdict": "sensitive at k=50 (CPR drop 0.05), stable k=75-150"
474	      },
475	      "qwen_ioi_k_sweep": {
476	        "k50": {
477	          "css_1.0_edges": 11,
478	          "css_1.0_cpr": 0.082
479	        },
480	        "k75": {
481	          "css_1.0_edges": 19,
482	          "css_1.0_cpr": 0.103
483	        },
484	        "k100": {
485	          "css_1.0_edges": 26,
486	          "css_1.0_cpr": 0.099
487	        },
488	        "k150": {
489	          "css_1.0_edges": 35,
490	          "css_1.0_cpr": 0.097
491	        },
492	        "verdict": "stable k=75-150, drop at k=50"
493	      },
494	      "overall_verdict": "CSS=1.0 CPR 在 k=75-150 范围内对所有 task 稳定（max Δ < 0.015）。 k=50 在 SVA 和 Qwen IOI 上 CPR 下降 ~0.04-0.05，因为 k=50 过小导致方法 重叠不足、CSS=1.0 边数太少。推荐 k=75 作为默认值，但需要在论文中报告这个选择。\n"
495	    },
496	    "tables": [
497	      {
498	        "name": "Table: CSS=1.0 CPR across k values (all tasks)",
499	        "columns": [
500	          "Task",
501	          "k=50",
502	          "k=75",
503	          "k=100",
504	          "k=150",
505	          "Max Δ"
506	        ],
507	        "rows": [
508	          [
509	            "IOI (GPT-2)",
510	            0.098,
511	            0.112,
512	            0.109,
513	            0.108,
514	            0.014
515	          ],
516	          [
517	            "Arith (GPT-2)",
518	            0.919,
519	            0.919,
520	            0.926,
521	            0.933,
522	            0.014
523	          ],
524	          [
525	            "SVA (GPT-2)",
526	            0.891,
527	            0.941,
528	            0.944,
529	            0.94,
530	            0.053
531	          ],
532	          [
533	            "IOI (Qwen)",
534	            0.082,
535	            0.103,
536	            0.099,
537	            0.097,
538	            0.021
539	          ]
540	        ]
541	      }
542	    ],
543	    "figures": [],
544	    "analysis": "Binarization ablation 的结论可以支撑 Claim 3（top-k 修复 isinf 退化）， 但 SVA k=50 的 sensitivity 会被 reviewer 追问。应对：(1) 论文推荐 k=75 并展示 full sweep 数据，(2) argue k=50 本身就低于合理下界（只保留 0.15% edges for GPT-2 的 32k+ edge graph），(3) 指出 k=75-150 的 CPR 标准差 < 0.01。\n\n\nTop-k normalization 的核心逻辑是让 ACDC 和其他方法在同一 edge budget 下比较。 k=75-150 范围内，三种方法各自选择的 top edges 有足够的 overlap base 使 CSS=1.0 稳定。k=50 时边太少，方法间 overlap 降到 noise level，CSS=1.0 变得不可靠。 SVA 比 IOI 更敏感于 k 的原因：SVA 电路更 concentrated（少数 critical edges 占比更大），k=50 可能恰好切掉了某些方法的 borderline critical edge。 这个 sensitivity 是 median 档的典型问题——结果 \"基本稳定但有 caveat\"， reviewer 可以攻击 k=75 的选择是 cherry-picked（虽然实际不是）。\n"
545	  },
546	  {
547	    "name": "Ablation method comparison (zero vs mean vs resample)",
548	    "description": "Compare ablation methods on all tasks. P2 优先级。 验证 CSS advantage 不依赖特定 evaluation ablation。\n",
549	    "results": {
550	      "status": "partial",
551	      "conclusion": "inconclusive",
552	      "completed_tasks": [
553	        "IOI (GPT-2)"
554	      ],
555	      "ioi_gpt2": {
556	        "zero_ablation": {
557	          "css_1.0_cpr": 0.109,
558	          "best_single_cpr": 0.029,
559	          "css_advantage": 0.08
560	        },
561	        "mean_ablation": {
562	          "css_1.0_cpr": 0.112,
563	          "best_single_cpr": 0.091,
564	          "css_advantage": 0.021
565	        },
566	        "resample_ablation": {
567	          "css_1.0_cpr": 0.095,
568	          "best_single_cpr": 0.082,
569	          "css_advantage": 0.013
570	        }
571	      },
572	      "note": "仅完成 IOI 一个 task 的三种 ablation 对比。CSS advantage 在三种 ablation 下 方向一致（正），但绝对值差异大（0.013-0.080）。SVA 和 Arithmetic 未完成。\n"
573	    },
574	    "tables": [
575	      {
576	        "name": "Table: IOI CSS advantage under different ablation methods",
577	        "columns": [
578	          "Ablation",
579	          "CSS=1.0 CPR",
580	          "Best Single CPR",
581	          "Advantage"
582	        ],
583	        "rows": [
584	          [
585	            "Zero",
586	            0.109,
587	            0.029,
588	            "+0.080"
589	          ],
590	          [
591	            "Mean",
592	            0.112,
593	            0.091,
594	            "+0.021"
595	          ],
596	          [
597	            "Resample",
598	            0.095,
599	            0.082,
600	            "+0.013"
601	          ]
602	        ]
603	      }
604	    ],
605	    "figures": [],
606	    "analysis": "部分完成的 ablation 对比。IOI 结果可以放在 Appendix 中作为 robustness check。 关键 takeaway：CSS advantage 在 mean ablation（最常用）下为 +0.021，在 resample （最严格）下为 +0.013，都是正的。但仅一个 task 不足以 claim robustness。 论文中可以 footnote 提及 IOI 上的一致性，full multi-task ablation 列为 future work。\n\n\n这是 P2 优先级实验，在 SVA (plan_004) 和 Qwen (plan_006/007) 完成后 时间已所剩不多。仅对 IOI 跑了 zero/mean/resample 三种 ablation， 因为 IOI 是唯一 CSS clearly wins 的 task。结果显示 CSS 优势在三种 ablation 下都为正但量级不同：zero ablation 下优势最大（因为 zero ablation 对电路外 edge 的破坏最大，小电路受益最多），resample 下优势最小。这表明 CSS advantage 不是 ablation method artifact，但缺少 SVA 和 Arithmetic 的对比数据使结论不完整。\n"
607	  },
608	  {
609	    "name": "CIRCUS as negative ablation",
610	    "description": "使用 D021 中 CIRCUS 的已有失败结果作为 negative ablation。 0 GPU hours，仅需分析和写作。\n",
611	    "results": {
612	      "status": "done",
613	      "conclusion": "negative_ablation_confirmed",
614	      "circus_vs_css": {
615	        "ioi_circus_core_cpr": -0.108,
616	        "ioi_css_1.0_cpr": 0.109,
617	        "ioi_circus_core_edges": 15,
618	        "ioi_css_1.0_edges": 7
619	      },
620	      "circus_failure_modes": [
621	        "CIRCUS 基于 single-method faithfulness scoring 选 core edges，但 scoring 本身依赖 ablation noise",
622	        "CIRCUS D021 三次运行结果不一致（edges: 12, 15, 18），说明 threshold sensitivity 严重",
623	        "CSS 的 binary consensus 不需要 score calibration，避免了 CIRCUS 的核心缺陷"
624	      ]
625	    },
626	    "tables": [
627	      {
628	        "name": "Table: CSS vs CIRCUS on IOI (negative ablation)",
629	        "columns": [
630	          "Method",
631	          "Edges",
632	          "CPR ↑",
633	          "CMD ↓",
634	          "Stable?"
635	        ],
636	        "rows": [
637	          [
638	            "CSS=1.0",
639	            7,
640	            0.109,
641	            0.911,
642	            "Yes (3/3 runs identical)"
643	          ],
644	          [
645	            "CIRCUS core",
646	            15,
647	            -0.108,
648	            1.134,
649	            "No (12-18 edges across runs)"
650	          ]
651	        ]
652	      }
653	    ],
654	    "figures": [],
655	    "analysis": "CIRCUS negative ablation 是 Claim 4 最有力的证据，也是论文中最 \"clean\" 的结果之一。 CSS=1.0 用更少的边（7 vs 15）达到正的 CPR，而 CIRCUS core 的 CPR 为负。 关键论点：binary consensus across methods 比 within-method score selection 更稳定， 因为前者不需要 score calibration，后者严重依赖 ablation method 和 threshold。 这是 methodological contribution 的核心，reviewer 较难攻击（结果清晰、对比公平）。\n\n\nCIRCUS (Parekh 2026) 在 IOI 上的 D021 结果已有：core edges CPR=-0.108（负值， 说明 CIRCUS core 实际上破坏了模型行为）。相比 CSS=1.0 的 CPR=0.109，差距极大。 CIRCUS 失败的根本原因是它在 single method 内部做 faithfulness scoring 来选 core， 但这个 scoring 对 threshold 和 ablation method 极其敏感。CSS 通过 cross-method binary agreement 绕过了 score calibration 问题。这个对比自然成为论文中 Claim 4 的关键证据：structural consensus (CSS) > faithfulness scoring (CIRCUS)。\n"
656	  },
657	  {
658	    "name": "Jaccard-CSS correlation analysis",
659	    "description": "Across all model×task pairs, plot max pairwise Jaccard vs CSS faithfulness advantage. 3 个 task data points + Qwen cross-validation。\n",
660	    "results": {
661	      "status": "done",
662	      "conclusion": "trend_observed_no_statistical_power",
663	      "data_points": [
664	        {
665	          "task": "IOI (GPT-2)",
666	          "max_jaccard": 0.31,
667	          "css_advantage": 0.021,
668	          "css_wins": true
669	        },
670	        {
671	          "task": "Arithmetic (GPT-2)",
672	          "max_jaccard": 0.695,
673	          "css_advantage": -0.066,
674	          "css_wins": false
675	        },
676	        {
677	          "task": "SVA (GPT-2)",
678	          "max_jaccard": 0.38,
679	          "css_advantage": -0.012,
680	          "css_wins": false
681	        },
682	        {
683	          "task": "IOI (Qwen)",
684	          "max_jaccard": 0.55,
685	          "css_advantage": 0.012,
686	          "css_wins": true
687	        },
688	        {
689	          "task": "Arithmetic (Qwen)",
690	          "max_jaccard": 0.61,
691	          "css_advantage": -0.039,
692	          "css_wins": false
693	        }
694	      ],
695	      "spearman_rho": -0.9,
696	      "spearman_p": 0.037,
697	      "pearson_r": -0.82,
698	      "pearson_p": 0.089,
699	      "threshold_estimate": "max_jaccard ≈ 0.45 (CSS advantage crosses zero)",
700	      "note": "Spearman p=0.037 因为 5 个 data points 刚过 significance threshold， 但 Pearson p=0.089 不显著。Reviewer 会质疑 n=5 的统计力。 如果只看 3 个 GPT-2 tasks，Spearman 无法计算 meaningful p-value。\n"
701	    },
702	    "tables": [
703	      {
704	        "name": "Table: Jaccard vs CSS Advantage (all model×task)",
705	        "columns": [
706	          "Task",
707	          "Model",
708	          "Max Jaccard",
709	          "CSS Adv (CPR)",
710	          "CSS Wins?"
711	        ],
712	        "rows": [
713	          [
714	            "IOI",
715	            "GPT-2",
716	            0.31,
717	            "+0.021",
718	            "✓"
719	          ],
720	          [
721	            "SVA",
722	            "GPT-2",
723	            0.38,
724	            "−0.012",
725	            "✗ (marginal)"
726	          ],
727	          [
728	            "IOI",
729	            "Qwen-0.5B",
730	            0.55,
731	            "+0.012",
732	            "✓ (marginal)"
733	          ],
734	          [
735	            "Arithmetic",
736	            "Qwen-0.5B",
737	            0.61,
738	            "−0.039",
739	            "✗"
740	          ],
741	          [
742	            "Arithmetic",
743	            "GPT-2",
744	            0.695,
745	            "−0.066",
746	            "✗"
747	          ]
748	        ]
749	      }
750	    ],
751	    "figures": [],
752	    "analysis": "这是 Claim 2 的核心 figure，也是论文能否从 \"anecdotal 2-task observation\" 升级为 \"systematic pattern\" 的关键。5 个数据点的 Spearman rho=-0.90 (p=0.037) 在 技术上可以 claim significance，但 reviewer 很可能指出：(1) n=5 统计力不足， (2) IOI 和 Arithmetic 是 \"designed\" 对比（一个 localized 一个 distributed）， 不是 random sample，(3) SVA 和 Qwen IOI 的 \"marginal\" 结果可以翻转。 应对策略：(1) 不 over-claim，用 \"observed trend\" 而非 \"significant correlation\"； (2) 强调 mechanistic motivation（Jaccard 度量 method independence → independence 是 consensus 有价值的前提条件）比纯统计论证更重要；(3) 提供 threshold 的 practical guidance（\"practitioners should check Jaccard before applying CSS\"）作为 actionable takeaway。\n\n5 个 model×task 数据点显示清晰的负相关趋势：max_jaccard 越高，CSS advantage 越低。Spearman rho=-0.90 方向非常一致（只有 SVA 和 Qwen IOI 的排序有微小扰动）。 但 n=5 的统计检验力极弱——Spearman p=0.037 刚好显著，Pearson 不显著。这是 因为 5 个点中有 3 个 \"extremes\"（IOI GPT-2 clearly positive，两个 Arithmetic clearly negative），中间的 SVA 和 Qwen IOI 决定了趋势的精确斜率但不足以 firm up p-value。如果只看 3 个 GPT-2 任务（plan 最初设计），完全无法做统计检验； 加入 Qwen 的 2 个数据点后勉强可以报告 Spearman。 论文中应 claim \"observed negative correlation consistent with hypothesis\" 而非 \"established significant correlation\"。threshold ≈ 0.45 只是 visual estimate from 5 points，不具预测力。\n"
753	  }
754	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88a80ad4-da7d-4971-8da0-1ef3512b8505",
  "isSidechain": true,
  "promptId": "a58b825b-71c5-48ad-a01b-a7815951ccb9",
  "agentId": "aa6e698b89154230b",
  "type": "user",
  "uuid": "7b8bb2ec-75fe-4aa2-a21e-b8f14b2e1f35",
  "sourceToolAssistantUUID": "88a80ad4-da7d-4971-8da0-1ef3512b8505",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-13T08:44:21.946Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KKtdyHDqtVnN7CfNnba1Y7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b8bb2ec-75fe-4aa2-a21e-b8f14b2e1f35",
  "isSidechain": true,
  "agentId": "aa6e698b89154230b",
  "requestId": "req_011CazGoumX3wTTf5evcjsRy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0ea333cc-f1da-49c6-a029-b28e825b8f79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WhVJVXds1c11pSyyKNfBY5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 46053,
      "cache_read_input_tokens": 17204,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 46053,
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

_source line 21 · 2026-05-13T08:44:21.968Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ejoh82U562bRfP2H9cFrGP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ea333cc-f1da-49c6-a029-b28e825b8f79",
  "isSidechain": true,
  "agentId": "aa6e698b89154230b",
  "requestId": "req_011CazGoumX3wTTf5evcjsRy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "50207826-8068-48d5-97fc-d69fea277340",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WhVJVXds1c11pSyyKNfBY5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 46053,
      "cache_read_input_tokens": 17204,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 46053
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 288,
          "cache_read_input_tokens": 17204,
          "cache_creation_input_tokens": 46053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 46053,
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

_source line 22 · 2026-05-13T08:44:22.268Z_

<details><summary>↩ Tool result · `toolu_01Ejoh82U562bRfP2H9cFrGP`</summary>

```text
1	[
2	  {
3	    "name": "GPT-2 SVA K=3 CSS",
4	    "description": "Subject-Verb Agreement on GPT-2 Small, K=3 (EAP-IG + EP + ACDC)。 验证 CSS 在第三个任务上的表现。SVA 电路预期比 IOI 更 localized， 但 worst 档假设 gradient methods 在 GPT-2 上的相关性是系统性的，不因任务而异。\n",
5	    "results": {
6	      "pairwise_jaccard": {
7	        "eapig_x_ep": 0.55,
8	        "eapig_x_acdc": 0.14,
9	        "ep_x_acdc": 0.11
10	      },
11	      "max_pairwise_jaccard": 0.55,
12	      "three_way_ratio": 0.09,
13	      "circuit_sizes": {
14	        "eapig": 100,
15	        "ep": 100,
16	        "acdc": 19
17	      },
18	      "acdc_binarization": "isinf (19 edges)",
19	      "css_distribution": {
20	        "1/3": 42,
21	        "2/3": 58,
22	        "3/3": 19
23	      },
24	      "faithfulness_mean": {
25	        "css_1.00_isinf": {
26	          "edges": 19,
27	          "CPR": 0.91,
28	          "CMD": 0.12
29	        },
30	        "css_1.00_k50": {
31	          "edges": 38,
32	          "CPR": 0.88,
33	          "CMD": 0.18
34	        },
35	        "eapig_k50": {
36	          "edges": 50,
37	          "CPR": 0.95,
38	          "CMD": 0.07
39	        },
40	        "ep_k50": {
41	          "edges": 50,
42	          "CPR": 0.93,
43	          "CMD": 0.1
44	        },
45	        "acdc_k50": {
46	          "edges": 50,
47	          "CPR": 0.87,
48	          "CMD": 0.19
49	        }
50	      },
51	      "faithfulness_zero": {
52	        "css_1.00": {
53	          "edges": 19,
54	          "CPR": -0.05,
55	          "CMD": 1.08
56	        },
57	        "eap_ig": {
58	          "edges": 100,
59	          "CPR": -0.03,
60	          "CMD": 1.04
61	        }
62	      },
63	      "d025_verdict": "FAIL (condition④: CSS=1.0 mean CPR=0.88 < EAP-IG=0.95)",
64	      "method_diversity_1_minus_max_jaccard": 0.45
65	    },
66	    "tables": [
67	      {
68	        "caption": "Table: SVA pairwise Jaccard matrix (GPT-2 Small, k=100)",
69	        "rows": [
70	          [
71	            "",
72	            "EAP-IG",
73	            "EP",
74	            "ACDC"
75	          ],
76	          [
77	            "EAP-IG",
78	            "1.00",
79	            "0.55",
80	            "0.14"
81	          ],
82	          [
83	            "EP",
84	            "0.55",
85	            "1.00",
86	            "0.11"
87	          ],
88	          [
89	            "ACDC",
90	            "0.14",
91	            "0.11",
92	            "1.00"
93	          ]
94	        ]
95	      },
96	      {
97	        "caption": "Table: SVA CSS faithfulness comparison (mean ablation, k=50)",
98	        "rows": [
99	          [
100	            "Method",
101	            "Edges",
102	            "CPR",
103	            "CMD"
104	          ],
105	          [
106	            "CSS=1.0 (isinf)",
107	            "19",
108	            "0.91",
109	            "0.12"
110	          ],
111	          [
112	            "CSS=1.0 (k=50)",
113	            "38",
114	            "0.88",
115	            "0.18"
116	          ],
117	          [
118	            "EAP-IG (k=50)",
119	            "50",
120	            "0.95",
121	            "0.07"
122	          ],
123	          [
124	            "EP (k=50)",
125	            "50",
126	            "0.93",
127	            "0.10"
128	          ],
129	          [
130	            "ACDC (k=50)",
131	            "50",
132	            "0.87",
133	            "0.19"
134	          ]
135	        ]
136	      }
137	    ],
138	    "figures": [],
139	    "analysis": "SVA 重复了 Arithmetic 的模式：gradient methods 高相关导致 K_eff≈1.5， CSS 退化为 ACDC 和 gradient-consensus 的交集而非三方独立投票。 至此 3 个 GPT-2 任务中仅 IOI 支持 CSS，初步支持 IOI 是 outlier 的假设。 对 Claim 2 提供第三个数据点（max Jaccard=0.55 → CSS fails），但 n=3 仍不足以 拟合 threshold。\n\n\nSVA 虽然传统上被认为是 localized circuit，但在 GPT-2 Small 上 EAP-IG 和 EP 同为 gradient-based，共享相同的 backward pass 信息——两者识别的 top-100 edges 有 55% 重叠。这不是偶然，而是因为 GPT-2 的 12 层 12 头结构中， subject-verb 信息流经的 attention pattern 对 gradient magnitude 和 edge pruning score 产生高度相似的排序。ACDC isinf 仅保留 19 条极端边，CSS=1.0≡ACDC， top-k 归一化后 CSS=1.0 (38 edges) 的 CPR=0.88 仍低于 EAP-IG 单方法的 0.95， 因为 consensus 丢弃了 EAP-IG 独有的 12 条高贡献边（这些边 EP 未覆盖因其 pruning criterion 对 indirect effects 的敏感度不同）。重复了 Arithmetic 的负面模式。\n"
140	  },
141	  {
142	    "name": "GPT-2 DocQA/Factual K=3 CSS",
143	    "description": "在 GPT-2 Small 上运行分布式计算任务（factual recall 或 document QA）， K=3 (EAP-IG + EP + ACDC)。预期分布式电路导致更高的 inter-method 相关性。\n",
144	    "results": {
145	      "pairwise_jaccard": {
146	        "eapig_x_ep": 0.62,
147	        "eapig_x_acdc": 0.22,
148	        "ep_x_acdc": 0.19
149	      },
150	      "max_pairwise_jaccard": 0.62,
151	      "three_way_ratio": 0.15,
152	      "circuit_sizes": {
153	        "eapig": 100,
154	        "ep": 100,
155	        "acdc": 35
156	      },
157	      "acdc_binarization": "isinf (35 edges) — 分布式任务产生更多 extreme edges",
158	      "faithfulness_mean": {
159	        "css_1.00_k50": {
160	          "edges": 42,
161	          "CPR": 0.82,
162	          "CMD": 0.25
163	        },
164	        "eapig_k50": {
165	          "edges": 50,
166	          "CPR": 0.91,
167	          "CMD": 0.13
168	        },
169	        "ep_k50": {
170	          "edges": 50,
171	          "CPR": 0.88,
172	          "CMD": 0.17
173	        }
174	      },
175	      "d025_verdict": "FAIL (condition④: CSS=1.0 CPR=0.82 < EAP-IG=0.91)",
176	      "method_diversity_1_minus_max_jaccard": 0.38
177	    },
178	    "tables": [
179	      {
180	        "caption": "Table: DocQA faithfulness comparison (mean ablation, k=50)",
181	        "rows": [
182	          [
183	            "Method",
184	            "Edges",
185	            "CPR",
186	            "CMD"
187	          ],
188	          [
189	            "CSS=1.0 (k=50)",
190	            "42",
191	            "0.82",
192	            "0.25"
193	          ],
194	          [
195	            "EAP-IG (k=50)",
196	            "50",
197	            "0.91",
198	            "0.13"
199	          ],
200	          [
201	            "EP (k=50)",
202	            "50",
203	            "0.88",
204	            "0.17"
205	          ],
206	          [
207	            "ACDC (k=50)",
208	            "50",
209	            "0.84",
210	            "0.22"
211	          ]
212	        ]
213	      }
214	    ],
215	    "figures": [],
216	    "analysis": "第四个数据点进一步确认 pattern 但边际贡献递减。4 个 GPT-2 任务中 3 个 FAIL， 仅 IOI PASS。这足以支撑 analysis paper 的 \"CSS fails when methods correlate\" 叙事， 但无法支撑 method paper 的 \"CSS is generally useful\" claim。 对 Claim 2 的数据点：max_Jaccard=0.62 → CSS CPR advantage = -0.09。\n\n\nDistributed computation tasks（如 factual recall）在 GPT-2 上涉及 MLP 和多层 attention 的广泛交互——不存在像 IOI 那样的 sparse 14-edge bottleneck。 所有 gradient-based methods 都会识别出相似的 \"information highway\" 通路， 因为 distributed circuits 的 gradient landscape 更平坦，top edges 的排序差异更小。 ACDC isinf 产生 35 条边（比 IOI/SVA 多），因为分布式任务中更多边有 extreme attribution。 CSS=1.0 丢弃了各方法独有的 task-specific edges，导致 CPR 下降。 本实验的价值在于确认 \"distributed circuit → high Jaccard → CSS fail\" 的因果链， 但不产生超出 Arithmetic 已有结论的新 insight。\n"
217	  },
218	  {
219	    "name": "Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + IFR)",
220	    "description": "首个非 GPT-2 模型。IFR 替代 ACDC 作为第三种方法（不同 algorithmic family）。 Worst 档假设 IFR 在 0.5B scale 退化为 gradient proxy。\n",
221	    "results": {
222	      "pairwise_jaccard": {
223	        "eapig_x_ep": 0.48,
224	        "eapig_x_ifr": 0.52,
225	        "ep_x_ifr": 0.45
226	      },
227	      "max_pairwise_jaccard": 0.52,
228	      "three_way_ratio": 0.28,
229	      "circuit_sizes": {
230	        "eapig": 100,
231	        "ep": 100,
232	        "ifr": 100
233	      },
234	      "css_distribution": {
235	        "1/3": 28,
236	        "2/3": 72,
237	        "3/3": 48
238	      },
239	      "faithfulness_mean": {
240	        "css_1.00": {
241	          "edges": 48,
242	          "CPR": 0.08,
243	          "CMD": 0.87
244	        },
245	        "eapig": {
246	          "edges": 100,
247	          "CPR": 0.1,
248	          "CMD": 0.85
249	        },
250	        "ep": {
251	          "edges": 100,
252	          "CPR": 0.06,
253	          "CMD": 0.9
254	        },
255	        "ifr": {
256	          "edges": 100,
257	          "CPR": 0.07,
258	          "CMD": 0.89
259	        }
260	      },
261	      "css_1_cpr_vs_best_single": -0.02,
262	      "ioi_css1_cpr_with_ifr": 0.08,
263	      "method_diversity_1_minus_max_jaccard": 0.48
264	    },
265	    "tables": [
266	      {
267	        "caption": "Table: Qwen-2.5 IOI Jaccard matrix (k=100)",
268	        "rows": [
269	          [
270	            "",
271	            "EAP-IG",
272	            "EP",
273	            "IFR"
274	          ],
275	          [
276	            "EAP-IG",
277	            "1.00",
278	            "0.48",
279	            "0.52"
280	          ],
281	          [
282	            "EP",
283	            "0.48",
284	            "1.00",
285	            "0.45"
286	          ],
287	          [
288	            "IFR",
289	            "0.52",
290	            "0.45",
291	            "1.00"
292	          ]
293	        ]
294	      },
295	      {
296	        "caption": "Table: Qwen-2.5 IOI faithfulness (mean ablation)",
297	        "rows": [
298	          [
299	            "Method",
300	            "Edges",
301	            "CPR",
302	            "CPR/edge"
303	          ],
304	          [
305	            "CSS=1.0",
306	            "48",
307	            "0.08",
308	            "0.00167"
309	          ],
310	          [
311	            "EAP-IG",
312	            "100",
313	            "0.10",
314	            "0.00100"
315	          ],
316	          [
317	            "EP",
318	            "100",
319	            "0.06",
320	            "0.00060"
321	          ],
322	          [
323	            "IFR",
324	            "100",
325	            "0.07",
326	            "0.00070"
327	          ]
328	        ]
329	      }
330	    ],
331	    "figures": [],
332	    "analysis": "IFR 的引入未能打破 gradient-method 相关性困境。虽然 IFR 名义上属于不同 algorithmic family， 但其在 transformer 上的行为与 gradient methods 高度相关——这是 worst 档的核心假设。 IOI 在 Qwen 上 CSS 的 CPR 优势 (-0.02) 处于噪声水平，与 GPT-2 IOI 的明确正面结果 (CPR=0.109 vs best single 0.029) 形成鲜明对比。这暗示 GPT-2 IOI 的成功 可能依赖于其极端 localized 的 14-edge ACDC circuit（isinf binarization 的产物）， 而非 consensus 方法的内在优势。\n\n\nIFR (Iterative Feature Removal) 本质上通过 feature similarity 来评估 edge importance， 但在 0.5B transformer 中，feature similarity 的排序与 gradient magnitude 高度相关—— 因为 transformer 的 residual stream 结构使得 gradient 和 activation similarity 对 edge importance 产生相似的排序（Elhage et al. 2021 的 \"privileged basis\" 现象）。 Qwen-2.5 0.5B 有 24 层 16 头，IOI circuit 比 GPT-2 更分散（更多层参与）， 导致 pairwise Jaccard 虽比 GPT-2 IOI (0.31) 高但不如 Arithmetic (0.70)。 CSS=1.0 的 48 条边 CPR=0.08 略低于 EAP-IG 的 0.10——差距很小但方向为负， 在 edge-efficiency (CPR/edge) 上 CSS 有微弱优势但不显著。 IFR 未能提供预期的 \"different family\" 独立性，K_eff 仍约 1.8。\n"
333	  },
334	  {
335	    "name": "Qwen-2.5 0.5B Arithmetic K=3",
336	    "description": "Qwen-2.5 0.5B 上的 Arithmetic (Greaterthan)，K=3 with IFR。 验证 IFR 是否能在高相关任务上恢复 CSS。\n",
337	    "results": {
338	      "pairwise_jaccard": {
339	        "eapig_x_ep": 0.58,
340	        "eapig_x_ifr": 0.55,
341	        "ep_x_ifr": 0.5
342	      },
343	      "max_pairwise_jaccard": 0.58,
344	      "css_distribution": {
345	        "1/3": 22,
346	        "2/3": 68,
347	        "3/3": 52
348	      },
349	      "faithfulness_mean": {
350	        "css_1.00": {
351	          "edges": 52,
352	          "CPR": 0.9,
353	          "CMD": 0.15
354	        },
355	        "eapig": {
356	          "edges": 100,
357	          "CPR": 0.97,
358	          "CMD": 0.04
359	        },
360	        "ep": {
361	          "edges": 100,
362	          "CPR": 0.94,
363	          "CMD": 0.09
364	        },
365	        "ifr": {
366	          "edges": 100,
367	          "CPR": 0.92,
368	          "CMD": 0.12
369	        }
370	      },
371	      "d025_verdict": "FAIL (condition④: CSS=1.0 CPR=0.90 < EAP-IG=0.97)",
372	      "method_diversity_1_minus_max_jaccard": 0.42
373	    },
374	    "tables": [
375	      {
376	        "caption": "Table: Qwen Arithmetic faithfulness (mean ablation)",
377	        "rows": [
378	          [
379	            "Method",
380	            "Edges",
381	            "CPR",
382	            "CMD"
383	          ],
384	          [
385	            "CSS=1.0",
386	            "52",
387	            "0.90",
388	            "0.15"
389	          ],
390	          [
391	            "EAP-IG",
392	            "100",
393	            "0.97",
394	            "0.04"
395	          ],
396	          [
397	            "EP",
398	            "100",
399	            "0.94",
400	            "0.09"
401	          ],
402	          [
403	            "IFR",
404	            "100",
405	            "0.92",
406	            "0.12"
407	          ]
408	        ]
409	      }
410	    ],
411	    "figures": [],
412	    "analysis": "Arithmetic 在两个模型上都失败，进一步支持 \"task structure 决定 CSS utility\" 的结论。 IFR 对 method diversity 的贡献可以忽略。Worst 档的核心 thesis 成立： 在 transformer 上，所有主流 circuit discovery methods 共享底层 gradient 信息， 导致 consensus 退化。\n\n\nArithmetic 在 Qwen 上延续 GPT-2 的高相关模式。IFR 与 EAP-IG 的 Jaccard=0.55 证实 similarity-based 方法未能提供独立视角。虽然 Qwen 的 EAP-IG×EP Jaccard (0.58) 比 GPT-2 (0.695) 略低（因模型更大、电路更分散），但仍远高于 CSS 有效工作所需的阈值。 Arithmetic 作为数值比较任务，其计算通路在所有方法看来都很相似—— MLP 中的 magnitude comparison 操作无论用 gradient、pruning 还是 feature removal 来检测， 排序都一致。CSS 没有恢复。\n"
413	  },
414	  {
415	    "name": "Gemma-2 2B IOI K=3",
416	    "description": "Scale 到 2B 模型 (Gemma-2)。IOI task，K=3 (EAP-IG + EP + IFR)。 验证 CSS 在更大模型上是否保持 IOI 的正面结果。\n",
417	    "results": {
418	      "pairwise_jaccard": {
419	        "eapig_x_ep": 0.42,
420	        "eapig_x_ifr": 0.48,
421	        "ep_x_ifr": 0.4
422	      },
423	      "max_pairwise_jaccard": 0.48,
424	      "css_distribution": {
425	        "1/3": 35,
426	        "2/3": 78,
427	        "3/3": 55
428	      },
429	      "faithfulness_mean": {
430	        "css_1.00": {
431	          "edges": 55,
432	          "CPR": 0.06,
433	          "CMD": 0.91
434	        },
435	        "eapig": {
436	          "edges": 100,
437	          "CPR": 0.07,
438	          "CMD": 0.9
439	        },
440	        "ep": {
441	          "edges": 100,
442	          "CPR": 0.04,
443	          "CMD": 0.93
444	        },
445	        "ifr": {
446	          "edges": 100,
447	          "CPR": 0.05,
448	          "CMD": 0.92
449	        }
450	      },
451	      "css_1_cpr_vs_best_single": -0.01,
452	      "method_diversity_1_minus_max_jaccard": 0.52
453	    },
454	    "tables": [
455	      {
456	        "caption": "Table: Gemma-2 IOI faithfulness (mean ablation)",
457	        "rows": [
458	          [
459	            "Method",
460	            "Edges",
461	            "CPR",
462	            "CPR/edge"
463	          ],
464	          [
465	            "CSS=1.0",
466	            "55",
467	            "0.06",
468	            "0.00109"
469	          ],
470	          [
471	            "EAP-IG",
472	            "100",
473	            "0.07",
474	            "0.00070"
475	          ],
476	          [
477	            "EP",
478	            "100",
479	            "0.04",
480	            "0.00040"
481	          ],
482	          [
483	            "IFR",
484	            "100",
485	            "0.05",
486	            "0.00050"
487	          ]
488	        ]
489	      }
490	    ],
491	    "figures": [],
492	    "analysis": "Scale up 后 IOI 的 CSS 优势消失。GPT-2 IOI 的 positive result 越来越像 artifact： ACDC isinf 在 GPT-2 上产生极端 sparse circuit (14 edges)，而这 14 条边恰好是 高质量的——这是 GPT-2 IOI 特有的幸运巧合，而非 consensus 方法的系统性优势。 在更大模型上，没有 ACDC isinf 的极端 sparsity，CSS 就退化为方法交集的 artifact。\n\n\nGemma-2 2B 有 26 层 16 头，IOI circuit 比 GPT-2 的 12 层结构更分散。 更多参数意味着更多可能的 edge pathways，pairwise Jaccard 自然降低（0.42-0.48）， 但这种降低是因为 circuit 变大变分散，而非方法真正独立。CSS=1.0 的 55 条边 CPR=0.06 与 EAP-IG 的 0.07 差距 -0.01，在统计上不显著。 更大模型上 IOI 不再是极端 localized 的 14-edge circuit—— GPT-2 上的 \"IOI exception\" 消失了。这强化了 IOI positive result 是 GPT-2 特有 artifact 的论点。edge-efficiency (CPR/edge) 上 CSS 仍有优势 (0.00109 vs 0.00070)， 但绝对 CPR 差为负。\n"
493	  },
494	  {
495	    "name": "Llama-3.1 8B IOI K=3",
496	    "description": "最大规模实验。Llama-3.1 8B，IOI task，K=3。需要 A100 80GB。\n",
497	    "results": {
498	      "pairwise_jaccard": {
499	        "eapig_x_ep": 0.38,
500	        "eapig_x_ifr": 0.44,
501	        "ep_x_ifr": 0.36
502	      },
503	      "max_pairwise_jaccard": 0.44,
504	      "circuit_sizes": {
505	        "eapig": 100,
506	        "ep": 100,
507	        "ifr": 100
508	      },
509	      "css_distribution": {
510	        "1/3": 42,
511	        "2/3": 82,
512	        "3/3": 60
513	      },
514	      "faithfulness_mean": {
515	        "css_1.00": {
516	          "edges": 60,
517	          "CPR": 0.04,
518	          "CMD": 0.94
519	        },
520	        "eapig": {
521	          "edges": 100,
522	          "CPR": 0.05,
523	          "CMD": 0.93
524	        }
525	      },
526	      "css_1_cpr_vs_best_single": -0.01,
527	      "practical_note": "EP 在 8B 上 GPU memory 紧张，需 gradient checkpointing，运行时间 ~6h"
528	    },
529	    "tables": [
530	      {
531	        "caption": "Table: Llama-3.1 8B IOI results summary",
532	        "rows": [
533	          [
534	            "Method",
535	            "Edges",
536	            "CPR",
537	            "Max Jaccard"
538	          ],
539	          [
540	            "CSS=1.0",
541	            "60",
542	            "0.04",
543	            "—"
544	          ],
545	          [
546	            "EAP-IG",
547	            "100",
548	            "0.05",
549	            "0.44"
550	          ],
551	          [
552	            "EP",
553	            "100",
554	            "0.03",
555	            "—"
556	          ],
557	          [
558	            "IFR",
559	            "100",
560	            "0.04",
561	            "—"
562	          ]
563	        ]
564	      }
565	    ],
566	    "figures": [],
567	    "analysis": "8B 实验的 ROI 极低。高 GPU 成本 (24h A100) 仅产生一个不显著的数据点。 在 analysis paper 中可作为 \"scaling caveat\" 一段提及，但不值得单独的 figure。 Worst 档建议砍掉此实验以节省资源，或降为 appendix-only。\n\n\n8B 模型有 32 层 32 头，edge space 巨大（~100K potential edges）。 k=100 只覆盖 edge space 的 0.1%，导致 pairwise Jaccard 自然降低（稀释效应）， 但这不代表方法独立——它们在各自 top-100 中识别的 functional role (e.g., induction heads, name mover heads) 相同，只是具体 edge indices 因模型结构更大而分散。 CSS=1.0 的 60 条边 CPR=0.04 仅与 EAP-IG 差 -0.01。 在如此大的模型上，k=100 本身就是 underpowered——所有方法都在极度 undersample， consensus 变得 trivially similar to random intersection。 这个实验最大的价值是展示 \"fixed-k consensus doesn't scale\"。\n"
568	  },
569	  {
570	    "name": "Binarization sensitivity ablation",
571	    "description": "系统性 top-k sweep (k=50, 75, 100, 150, 200) 在所有 model×task 对上， 验证 CSS 在不同 k 下的稳定性。\n",
572	    "results": {
573	      "ioi_gpt2_css_cpr_by_k": {
574	        "k50": 0.095,
575	        "k75": 0.1,
576	        "k100": 0.105,
577	        "k150": 0.098
578	      },
579	      "sva_gpt2_css_cpr_by_k": {
580	        "k50": 0.88,
581	        "k75": 0.87,
582	        "k100": 0.86,
583	        "k150": 0.85
584	      },
585	      "arithmetic_gpt2_css_cpr_by_k": {
586	        "k50": 0.919,
587	        "k75": 0.91,
588	        "k100": 0.905,
589	        "k150": 0.895
590	      },
591	      "css_stable_across_k": true,
592	      "but_advantage_never_positive_except_ioi": true,
593	      "key_finding": "CSS CPR 在 k=50-150 范围内稳定（std < 0.02），但这仅说明 binarization 本身不是 CSS 失败的原因——方法相关性才是。Worst 档的附加发现： ACDC isinf-vs-topk 的 Jaccard 差异驱动了 Jaccard-utility 的虚假关联。\n",
594	      "acdc_isinf_vs_topk_jaccard_gap": {
595	        "ioi": "isinf Jaccard=0.09 → topk Jaccard=0.25 (Δ=+0.16)",
596	        "arithmetic": "isinf Jaccard=0.17 → topk Jaccard=0.42 (Δ=+0.25)",
597	        "sva": "isinf Jaccard=0.14 → topk Jaccard=0.35 (Δ=+0.21)"
598	      }
599	    },
600	    "tables": [
601	      {
602	        "caption": "Table: CSS=1.0 CPR across binarization k values",
603	        "rows": [
604	          [
605	            "Task",
606	            "k=50",
607	            "k=75",
608	            "k=100",
609	            "k=150",
610	            "Stable?"
611	          ],
612	          [
613	            "IOI (GPT-2)",
614	            "0.095",
615	            "0.100",
616	            "0.105",
617	            "0.098",
618	            "Yes"
619	          ],
620	          [
621	            "SVA (GPT-2)",
622	            "0.88",
623	            "0.87",
624	            "0.86",
625	            "0.85",
626	            "Yes"
627	          ],
628	          [
629	            "Arith (GPT-2)",
630	            "0.919",
631	            "0.910",
632	            "0.905",
633	            "0.895",
634	            "Yes"
635	          ]
636	        ]
637	      },
638	      {
639	        "caption": "Table: ACDC binarization method effect on Jaccard",
640	        "rows": [
641	          [
642	            "Task",
643	            "Jaccard (isinf)",
644	            "Jaccard (top-k)",
645	            "Δ"
646	          ],
647	          [
648	            "IOI",
649	            "0.09",
650	            "0.25",
651	            "+0.16"
652	          ],
653	          [
654	            "Arith",
655	            "0.17",
656	            "0.42",
657	            "+0.25"
658	          ],
659	          [
660	            "SVA",
661	            "0.14",
662	            "0.35",
663	            "+0.21"
664	          ]
665	        ]
666	      }
667	    ],
668	    "figures": [],
669	    "analysis": "这是 worst 档下最有分析价值的实验。证明两件事：(1) CSS 对 binarization 稳定——好消息； (2) 但 Jaccard-utility 关系的很大一部分方差由 ACDC binarization choice 解释， 而非 genuine method diversity——坏消息。这为 analysis paper 提供了 \"ACDC binarization pathology 的完整 taxonomy\" 贡献（Claim 3 的延伸）， 也是 'When Does Consensus Fail' 叙事的核心技术贡献。\n\n\nBinarization (isinf vs top-k) 直接影响 ACDC 的 circuit size，进而影响 pairwise Jaccard 和 CSS=1.0 的含义。isinf 下 ACDC 极度 sparse（14-35 edges）， 与 gradient methods 的 Jaccard 极低；top-k 归一化后 Jaccard 显著上升。 这意味着之前观察到的 \"low Jaccard → CSS works (IOI)\" 关系中，IOI 的 low Jaccard 部分由 isinf binarization 驱动。去除这个 confound 后，IOI 的 max Jaccard 从 0.31 上升到约 0.25（top-k normalized，EAP-IG×EP pair）， CSS 的优势主要来自 ACDC isinf 的 extreme selection 而非 genuine consensus。 这是 worst 档 Jaccard-utility 关系 \"被 confound 驱动\" 假设的关键证据。\n"
670	  },
671	  {
672	    "name": "Ablation method comparison (zero vs mean vs resample)",
673	    "description": "在所有 task 上比较 zero ablation、mean ablation、resample ablation 下 CSS 的 faithfulness advantage，验证 CSS 优势是否对 evaluation choice robust。\n",
674	    "results": {
675	      "ioi_gpt2": {
676	        "zero": {
677	          "css_1_cpr": 0.109,
678	          "best_single_cpr": 0.029,
679	          "advantage": 0.08
680	        },
681	        "mean": {
682	          "css_1_cpr": 0.095,
683	          "best_single_cpr": 0.088,
684	          "advantage": 0.007
685	        },
686	        "resample": {
687	          "css_1_cpr": 0.085,
688	          "best_single_cpr": 0.082,
689	          "advantage": 0.003
690	        }
691	      },
692	      "sva_gpt2": {
693	        "zero": {
694	          "css_1_cpr": -0.05,
695	          "best_single_cpr": -0.03,
696	          "advantage": -0.02
697	        },
698	        "mean": {
699	          "css_1_cpr": 0.88,
700	          "best_single_cpr": 0.95,
701	          "advantage": -0.07
702	        },
703	        "resample": {
704	          "css_1_cpr": 0.8,
705	          "best_single_cpr": 0.87,
706	          "advantage": -0.07
707	        }
708	      },
709	      "arithmetic_gpt2": {
710	        "zero": {
711	          "css_1_cpr": -0.184,
712	          "best_single_cpr": -0.131,
713	          "advantage": -0.053
714	        },
715	        "mean": {
716	          "css_1_cpr": 0.919,
717	          "best_single_cpr": 0.985,
718	          "advantage": -0.066
719	        },
720	        "resample": {
721	          "css_1_cpr": 0.85,
722	          "best_single_cpr": 0.92,
723	          "advantage": -0.07
724	        }
725	      },
726	      "key_finding": "IOI 的 CSS 优势在 zero ablation 下最大 (+0.08)，mean ablation 下微弱 (+0.007)， resample 下几乎消失 (+0.003)。其他任务在所有 ablation 下 CSS 都不优。 这意味着 IOI positive result 部分依赖于 zero ablation 的破坏性—— zero ablation 对小 circuit 更友好（破坏比例更低），放大了 CSS=1.0 的 edge-efficiency 优势。\n"
727	    },
728	    "tables": [
729	      {
730	        "caption": "Table: CSS advantage across ablation methods",
731	        "rows": [
732	          [
733	            "Task",
734	            "Zero Δ",
735	            "Mean Δ",
736	            "Resample Δ"
737	          ],
738	          [
739	            "IOI",
740	            "+0.080",
741	            "+0.007",
742	            "+0.003"
743	          ],
744	          [
745	            "SVA",
746	            "-0.020",
747	            "-0.070",
748	            "-0.070"
749	          ],
750	          [
751	            "Arithmetic",
752	            "-0.053",
753	            "-0.066",
754	            "-0.070"
755	          ]
756	        ]
757	      }
758	    ],
759	    "figures": [],
760	    "analysis": "Worst 档下此实验揭示 IOI positive result 的第二个 confound（除 ACDC isinf 外）： zero ablation bias。这对 paper 是双刃剑——削弱了唯一的正面证据， 但为 analysis paper 提供了 \"evaluation method confounds in circuit faithfulness\" 的重要方法论贡献。建议在 paper 中诚实报告并讨论，这种 transparency 反而加分。\n\n\nZero ablation 将 ablated edges 置零，对大 circuit（100 edges）的破坏程度远大于 小 circuit（14 edges），因为更多路径被切断。这给了 CSS=1.0 (14 edges) 一个 不公平的优势——不是因为它的 edges 更好，而是因为 100-edge circuits 在 zero ablation 下 suffer disproportionately。Mean ablation 缓解了这个 bias（替换为 mean 而非 0）， 导致大小 circuit 的 CPR 趋近。Resample ablation 进一步消除 out-of-distribution artifacts。在 SVA 和 Arithmetic 上，即使在对 CSS 最有利的 zero ablation 下， gradient methods 的高相关性也阻止了 CSS 产生优势。\n"
761	  },
762	  {
763	    "name": "CIRCUS as negative ablation",
764	    "description": "整理 D021 的 CIRCUS 三次失败结果，作为负面消融实验展示 structural consensus (CSS) vs faithfulness scoring (CIRCUS) 的区别。\n",
765	    "results": {
766	      "circus_ioi_cpr": -0.108,
767	      "circus_sva_cpr": -0.15,
768	      "circus_arithmetic_cpr": -0.12,
769	      "circus_failure_rate": "3/3 tasks",
770	      "css_vs_circus_framing": "CIRCUS 在所有任务上 CPR 为负（比 random circuit 还差）， 而 CSS 至少在 IOI 上为正。但 worst 档下 CSS 在 3/4 任务上也失败， 所以 CSS vs CIRCUS 的对比变成 \"both methods have severe limitations\" 而非 \"CSS > CIRCUS\"。\n"
771	    },
772	    "tables": [
773	      {
774	        "caption": "Table: CIRCUS vs CSS faithfulness comparison",
775	        "rows": [
776	          [
777	            "Method",
778	            "IOI CPR",
779	            "SVA CPR",
780	            "Arith CPR"
781	          ],
782	          [
783	            "CIRCUS",
784	            "-0.108",
785	            "-0.15",
786	            "-0.12"
787	          ],
788	          [
789	            "CSS=1.0",
790	            "+0.109",
791	            "-0.05",
792	            "-0.184 (zero) / +0.919 (mean)"
793	          ],
794	          [
795	            "Best single",
796	            "+0.029 (zero)",
797	            "+0.95 (mean)",
798	            "+0.985 (mean)"
799	          ]
800	        ]
801	      }
802	    ],
803	    "figures": [],
804	    "analysis": "CIRCUS 负面结果是 low-hanging fruit——容易写、审稿人会觉得有信息量。 在 analysis paper 中定位为 \"what definitely doesn't work\"， 与 CSS 的 \"works under specific conditions\" 形成对比。 0 GPU hours，纯分析工作，性价比最高的 planned 实验。\n\n\nCIRCUS 使用 threshold diversity 在单一方法内部构建 consensus， 本质上是在同一 gradient landscape 上做不同切分——不提供新信息。 CSS 至少使用了不同方法，但当方法本身相关时也退化。 CIRCUS 的完全失败是可预期的：单方法 threshold sweep 生成的 \"diverse\" circuits 实际上是 nested sets（k=50 ⊂ k=100 ⊂ k=150），其交集就是最 conservative 的 cut， 这不是 consensus 而是 trivial intersection。\n"
805	  },
806	  {
807	    "name": "Jaccard-CSS correlation analysis",
808	    "description": "跨所有 model×task 对，拟合 max pairwise Jaccard vs CSS faithfulness advantage 的关系。 Worst 档下数据点少且关系被 confound 驱动。\n",
809	    "results": {
810	      "data_points": [
811	        {
812	          "task": "IOI",
813	          "model": "GPT-2",
814	          "max_jaccard": 0.31,
815	          "css_advantage": 0.08,
816	          "note": "isinf ACDC, zero ablation"
817	        },
818	        {
819	          "task": "Arithmetic",
820	          "model": "GPT-2",
821	          "max_jaccard": 0.695,
822	          "css_advantage": -0.066,
823	          "note": "mean ablation"
824	        },
825	        {
826	          "task": "SVA",
827	          "model": "GPT-2",
828	          "max_jaccard": 0.55,
829	          "css_advantage": -0.07,
830	          "note": "mean ablation"
831	        },
832	        {
833	          "task": "IOI",
834	          "model": "Qwen-0.5B",
835	          "max_jaccard": 0.52,
836	          "css_advantage": -0.02,
837	          "note": "with IFR"
838	        },
839	        {
840	          "task": "Arithmetic",
841	          "model": "Qwen-0.5B",
842	          "max_jaccard": 0.58,
843	          "css_advantage": -0.07,
844	          "note": "with IFR"
845	        },
846	        {
847	          "task": "IOI",
848	          "model": "Gemma-2B",
849	          "max_jaccard": 0.48,
850	          "css_advantage": -0.01,
851	          "note": "with IFR"
852	        }
853	      ],
854	      "n_data_points": 6,
855	      "spearman_rho": -0.54,
856	      "spearman_p_value": 0.27,
857	      "pearson_r": -0.61,
858	      "pearson_p_value": 0.2,
859	      "fitted_threshold": "max_Jaccard < 0.35 for CSS to work",
860	      "n_points_below_threshold": 1,
861	      "n_points_above_threshold": 5,
862	      "confound_analysis": "去除 IOI GPT-2 (唯一用 ACDC isinf 且 zero ablation 的数据点) 后： n=5, spearman_rho=-0.30, p=0.62。关系完全不显著。 IOI GPT-2 是 influential point (Cook's D > 1.0)，驱动了整个 correlation。\n"
863	    },
864	    "tables": [
865	      {
866	        "caption": "Table: Jaccard-CSS correlation data",
867	        "rows": [
868	          [
869	            "Task×Model",
870	            "Max Jaccard",
871	            "CSS Advantage",
872	            "Confounds"
873	          ],
874	          [
875	            "IOI×GPT-2",
876	            "0.31",
877	            "+0.080",
878	            "ACDC isinf + zero ablation"
879	          ],
880	          [
881	            "SVA×GPT-2",
882	            "0.55",
883	            "-0.070",
884	            "—"
885	          ],
886	          [
887	            "Arith×GPT-2",
888	            "0.695",
889	            "-0.066",
890	            "—"
891	          ],
892	          [
893	            "IOI×Qwen",
894	            "0.52",
895	            "-0.020",
896	            "IFR may ≈ gradient"
897	          ],
898	          [
899	            "Arith×Qwen",
900	            "0.58",
901	            "-0.070",
902	            "—"
903	          ],
904	          [
905	            "IOI×Gemma",
906	            "0.48",
907	            "-0.010",
908	            "—"
909	          ]
910	        ]
911	      },
912	      {
913	        "caption": "Table: Correlation robustness",
914	        "rows": [
915	          [
916	            "Analysis",
917	            "ρ",
918	            "p-value",
919	            "n"
920	          ],
921	          [
922	            "All points",
923	            "-0.54",
924	            "0.27",
925	            "6"
926	          ],
927	          [
928	            "Remove IOI×GPT-2",
929	            "-0.30",
930	            "0.62",
931	            "5"
932	          ],
933	          [
934	            "Remove ACDC tasks only",
935	            "-0.10",
936	            "0.87",
937	            "3"
938	          ]
939	        ]
940	      }
941	    ],
942	    "figures": [],
943	    "analysis": "这是 worst 档对 Claim 2 (CSS utility predicted by inter-method correlation) 的致命打击。 Correlation 在统计上不显著 (p=0.27)，且由单个 confounded data point 驱动。 Paper 不能声称 \"Jaccard predicts CSS utility\" 作为 empirical finding—— 只能作为 \"motivated conjecture\" 或 \"necessary condition hypothesis\"。 Analysis paper 的重构方向：Jaccard 是 necessary condition check （max_Jaccard > 0.5 → CSS almost certainly fails）， 但不是 sufficient condition（max_Jaccard < 0.5 不保证 CSS works， 因为只有一个数据点且有 confounds）。 这限制了 contribution 的强度，但对 EMNLP Findings 或 workshop 仍可接受—— honest negative results 有其学术价值。\n\n6 个数据点本身就 underpowered（Spearman 需 n≈10 才有检测 ρ=0.6 的 80% power）。 Worst 档下唯一的正面点 (IOI GPT-2) 同时有两个 confounds： (1) ACDC isinf 压低了 max_Jaccard（top-k 归一化后 Jaccard 上升到 0.25→仍低，但方向变化） (2) zero ablation 放大了 CSS 的 edge-efficiency 优势。 去除这个 influential point 后，剩余 5 个点都在 Jaccard 0.48-0.70 范围内， CSS advantage 都在 [-0.07, -0.01] 范围内——flat line，no correlation。 Jaccard-utility 关系变成了 \"one-point story\"，统计上不可信。\n"
944	  }
945	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50207826-8068-48d5-97fc-d69fea277340",
  "isSidechain": true,
  "promptId": "a58b825b-71c5-48ad-a01b-a7815951ccb9",
  "agentId": "aa6e698b89154230b",
  "type": "user",
  "uuid": "8cfdaa8d-582d-4bbd-a1ad-5769ed587fe3",
  "sourceToolAssistantUUID": "50207826-8068-48d5-97fc-d69fea277340",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-13T08:44:22.273Z_

<details><summary>↩ Tool result · `toolu_01KKtdyHDqtVnN7CfNnba1Y7`</summary>

```text
1	[
2	  {
3	    "name": "GPT-2 Small Subject-Verb Agreement K=3 CSS",
4	    "description": "在 GPT-2 Small 上对 Subject-Verb Agreement (SVA) 任务运行三种发现方法 （EAP-IG, EP, ACDC），计算 CSS 分布和 faithfulness。SVA 是经典的 localized circuit 任务，核心计算集中在 layer 7-10 的 number-tracking attention heads，预期方法间 Jaccard 低、CSS 优势显著。\n",
5	    "results": {
6	      "eapig_edges": 50,
7	      "ep_edges": 50,
8	      "acdc_edges_isinf": 12,
9	      "acdc_edges_k50": 50,
10	      "jaccard_eapig_ep": 0.22,
11	      "jaccard_eapig_acdc": 0.08,
12	      "jaccard_ep_acdc": 0.06,
13	      "max_pairwise_jaccard": 0.22,
14	      "three_way_ratio": 0.032,
15	      "css_3of3_edges": 8,
16	      "css_2of3_edges": 31,
17	      "css_1of3_edges": 73,
18	      "css_1.00_edges": 8,
19	      "css_1.00_CPR": 0.12,
20	      "css_1.00_CMD": 0.89,
21	      "css_0.67_edges": 31,
22	      "css_0.67_CPR": 0.065,
23	      "css_0.67_CMD": 0.945,
24	      "acdc_edges": 12,
25	      "acdc_CPR": 0.03,
26	      "acdc_CMD": 0.975,
27	      "eapig_k50_CPR": -0.04,
28	      "eapig_k50_CMD": 1.05,
29	      "ep_k50_CPR": -0.07,
30	      "ep_k50_CMD": 1.08,
31	      "css1_cpr_advantage": 0.09,
32	      "css1_edge_ratio": 0.071
33	    },
34	    "tables": [
35	      {
36	        "name": "Table: SVA Circuit Discovery Summary",
37	        "description": "行: EAP-IG(k=50), EP(k=50), ACDC(isinf), CSS≥2/3, CSS=1.0 列: Edges, CPR, CMD, vs-best-single-Δ 展示 CSS=1.0 在仅 8 条边下达到 CPR=0.12，是 ACDC(0.03) 的 4 倍\n"
38	      },
39	      {
40	        "name": "Table: SVA Pairwise Jaccard Matrix",
41	        "description": "3×3 对称矩阵，对角线为 1.0。EAP-IG×EP=0.22, EAP-IG×ACDC=0.08, EP×ACDC=0.06。与 IOI 的 Jaccard 矩阵并列展示，突出 SVA 更低的 inter-method correlation\n"
42	      }
43	    ],
44	    "figures": [],
45	    "analysis": "SVA 完美复现 IOI 的核心模式：localized circuit → low Jaccard → CSS=1.0 faithfulness 优势。max Jaccard 0.22 甚至低于 IOI 的 0.31，反映 SVA 电路更 集中（fewer critical heads），使方法分歧更大。CSS CPR advantage 0.09 与 IOI 的 0.08 一致，支撑 Claim 1。此结果将 Claim 1 的支持从 1 个任务扩展到 2 个， 直接削弱 R1 泛化性质疑。\n\n\nSVA 在 GPT-2 Small 中依赖 layer 7-10 中约 5-8 个专门追踪主语数特征的 attention head。这是一个高度 localized 的电路：关键计算集中在少量 head 的 Q-K 匹配上。三种方法各自从不同角度发现该电路的不同子集——EAP-IG 沿梯度 路径优先选取高 ∂L/∂e 的边，EP 通过逐步剪枝保留移除后损失最大的边，ACDC 通过激活差异识别 clean vs corrupt 下变化最大的边。由于电路 localized，每种 方法只需少量边即可捕获核心功能，导致三组 top-50 edge set 的交集稀疏（max Jaccard=0.22）。CSS=1.0 恰好捕获了所有三种方法共同认定的 8 条核心边—— 这些边对应 number-agreement 的关键 attention pattern，移除它们会破坏 subject→verb 的 number propagation，因此 CPR=0.12 显著高于任何单方法。 ACDC 的 12 条 isinf 边虽然也 localized，但包含了 4 条 ACDC 特有的 method-specific 边（其他方法未选中），导致部分噪声稀释了 faithfulness。\n"
46	  },
47	  {
48	    "name": "GPT-2 Small Factual Recall K=3 CSS",
49	    "description": "在 GPT-2 Small 上对 Factual Recall 任务（country→capital, e.g. \"The capital of France is\"）运行三种发现方法。这是一个 distributed computation 任务， 知识检索涉及多层 MLP 和跨层 attention routing，预期方法 Jaccard 中等， CSS 优势边际。\n",
50	    "results": {
51	      "eapig_edges": 50,
52	      "ep_edges": 50,
53	      "acdc_edges_isinf": 22,
54	      "acdc_edges_k50": 50,
55	      "jaccard_eapig_ep": 0.48,
56	      "jaccard_eapig_acdc": 0.18,
57	      "jaccard_ep_acdc": 0.15,
58	      "max_pairwise_jaccard": 0.48,
59	      "three_way_ratio": 0.092,
60	      "css_3of3_edges": 15,
61	      "css_2of3_edges": 38,
62	      "css_1of3_edges": 69,
63	      "css_1.00_edges": 15,
64	      "css_1.00_CPR": 0.055,
65	      "css_1.00_CMD": 0.95,
66	      "css_0.67_edges": 38,
67	      "css_0.67_CPR": 0.04,
68	      "css_0.67_CMD": 0.965,
69	      "acdc_edges": 22,
70	      "acdc_CPR": 0.037,
71	      "acdc_CMD": 0.97,
72	      "eapig_k50_CPR": 0.03,
73	      "eapig_k50_CMD": 0.975,
74	      "ep_k50_CPR": 0.01,
75	      "ep_k50_CMD": 0.99,
76	      "css1_cpr_advantage": 0.018,
77	      "css1_edge_ratio": 0.123
78	    },
79	    "tables": [
80	      {
81	        "name": "Table: Factual Recall Circuit Discovery Summary",
82	        "description": "格式同 SVA/IOI 表。CSS=1.0 的 15 条边 CPR=0.055 略优于 ACDC 的 22 条 边 CPR=0.037，但优势远小于 IOI/SVA\n"
83	      }
84	    ],
85	    "figures": [],
86	    "analysis": "Factual Recall 是论文叙事的关键 interpolation 点。它证明 CSS utility 不是 binary（有/无），而是连续的、可由 Jaccard 预测的量。max Jaccard 0.48 落在 IOI(0.31) 和 Arithmetic(0.695) 之间，CSS advantage 0.018 也相应落在 0.08 和 -0.066 之间。这将 Claim 2 从\"两点定义的趋势\"升级为\"有中间插值的 连续关系\"，显著增强说服力。同时，CSS=1.0 的优势虽小但仍为正，使 n_tasks_css_wins 达到 3（IOI + SVA + Factual），满足 reviewer 对 majority-win 的期望。\n\n\nFactual recall 是一个 distributed computation：知识存储在中层 MLP（layer 5-9） 的 key-value 机制中，而检索依赖多层 attention head 将 subject token 的 representation 路由到 last token position。三种方法在 MLP 存储层的边上有较高 共识（这些边是任何方法都无法忽略的关键瓶颈），但在 attention routing 边上 存在分歧——EAP-IG 偏好早期 attention head（梯度信号强），EP 保留后期 head （剪枝敏感），ACDC 选中的 head 分散在多层。这导致 max Jaccard=0.48：高于 localized tasks（方法在核心 MLP 边上被迫共识），但远低于 Arithmetic（0.695） 因为 routing 部分仍有显著分歧。CSS=1.0 的 15 条边捕获了 MLP 存储核心 + 最关键的 2-3 个 routing head，CPR=0.055 略优于 ACDC(0.037)，但优势仅 0.018。 这符合理论预期：中等 Jaccard → 中等 CSS utility，consensus 的过滤效果被 方法间部分冗余所稀释。\n"
87	  },
88	  {
89	    "name": "Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + IFR)",
90	    "description": "在 Qwen-2.5 0.5B 上运行 IOI，用 IFR（Iterative Feature Removal， similarity-based）替代 ACDC，构成 K=3 = {EAP-IG, EP, IFR}。 IFR 来自不同算法族，预期降低 max Jaccard、维持或提升 CSS CPR。 同时验证 CSS 跨模型架构（GQA, SwiGLU）的泛化性。\n",
91	    "results": {
92	      "eapig_edges": 50,
93	      "ep_edges": 50,
94	      "ifr_edges": 50,
95	      "jaccard_eapig_ep": 0.28,
96	      "jaccard_eapig_ifr": 0.14,
97	      "jaccard_ep_ifr": 0.11,
98	      "max_pairwise_jaccard": 0.28,
99	      "css_3of3_edges": 10,
100	      "css_2of3_edges": 30,
101	      "css_1of3_edges": 82,
102	      "css_1.00_edges": 10,
103	      "css_1.00_CPR": 0.14,
104	      "css_1.00_CMD": 0.87,
105	      "css_0.67_edges": 30,
106	      "css_0.67_CPR": 0.08,
107	      "css_0.67_CMD": 0.93,
108	      "eapig_k50_CPR": 0.04,
109	      "ep_k50_CPR": 0.02,
110	      "ifr_k50_CPR": 0.05,
111	      "css1_cpr_advantage": 0.09,
112	      "max_jaccard_vs_gpt2_ioi": "0.28 ≤ 0.31 (GPT-2)"
113	    },
114	    "tables": [
115	      {
116	        "name": "Table: Cross-Model IOI Comparison (GPT-2 vs Qwen)",
117	        "description": "行: GPT-2 K=3(EAP-IG,EP,ACDC), Qwen K=3(EAP-IG,EP,IFR) 列: Max Jaccard, CSS=1.0 Edges, CSS=1.0 CPR, Best-Single CPR, Δ 突出 IFR 带来的 Jaccard 下降和 CPR 提升\n"
118	      }
119	    ],
120	    "figures": [],
121	    "analysis": "此实验同时服务三个目标：(1) 验证 CSS 跨模型泛化（Qwen ≠ GPT-2 架构）， (2) 验证 IFR 作为第三算法族的加入降低 Jaccard 并提升 CSS utility（直接回应 R3 的 K≈2 质疑），(3) 为 plan_013 提供第 5 个 Jaccard-CSS 数据点。 max Jaccard 0.28 ≤ GPT-2 的 0.31，CSS CPR 0.14 > 0.109，两个指标同时 改善，是 best tier 最有力的单一证据。\n\n\nIFR 通过逐步移除 feature 并测量 representation similarity 变化来评分边， 其算法逻辑与 gradient-based EAP-IG 和 pruning-based EP 正交。在 Qwen 的 IOI 电路中，EAP-IG 和 EP 的 Jaccard 从 GPT-2 的 0.31 降至 0.28——Qwen 的 GQA（Grouped Query Attention）使得 head 内 key-value sharing 改变了 gradient 和 pruning 的敏感度分布，两方法在 induction head 选择上出现更大 分歧。IFR 与 gradient 方法的 Jaccard 极低（0.14/0.11），因为 similarity-based scoring 完全不依赖 loss gradient，而是基于 intermediate representation 的 余弦距离变化。CSS=1.0 的 10 条边是三种完全不同的算法视角共同认定的 IOI 核心——name mover heads 和 S-inhibition heads 的关键边——CPR=0.14 不仅 不退化，反而高于 GPT-2 IOI 的 0.109。这验证了核心理论：方法多样性越高 （更低 Jaccard），consensus 过滤越有效，CSS utility 越大。\n"
122	  },
123	  {
124	    "name": "Qwen-2.5 0.5B Arithmetic K=3 (EAP-IG + EP + IFR)",
125	    "description": "Qwen 上运行 Arithmetic (Greaterthan)，IFR 替代 ACDC。测试 IFR 能否 打破 EAP-IG×EP 的高 Jaccard 相关性、使 CSS 部分恢复。\n",
126	    "results": {
127	      "jaccard_eapig_ep": 0.58,
128	      "jaccard_eapig_ifr": 0.28,
129	      "jaccard_ep_ifr": 0.24,
130	      "max_pairwise_jaccard": 0.58,
131	      "css_3of3_edges": 18,
132	      "css_2of3_edges": 35,
133	      "css_1of3_edges": 69,
134	      "css_1.00_CPR": 0.935,
135	      "eapig_k50_CPR": 0.975,
136	      "ep_k50_CPR": 0.95,
137	      "ifr_k50_CPR": 0.88,
138	      "css1_cpr_advantage": -0.04
139	    },
140	    "tables": [
141	      {
142	        "name": "Table: Arithmetic Cross-Model Comparison",
143	        "description": "GPT-2 K=3 vs Qwen K=3(with IFR)。突出 max Jaccard 从 0.695→0.58 的下降以及 CSS advantage 从 -0.066 到 -0.04 的改善（趋势正确但未翻转）\n"
144	      }
145	    ],
146	    "figures": [],
147	    "analysis": "此实验的 negative result 实际上是论文叙事的资产而非负担。它证明：(1) Jaccard threshold 是稳健的——即使 IFR 降低了 max Jaccard，只要仍高于 ~0.55， CSS 依然无效；(2) CSS utility 的 bottleneck 是 max pairwise Jaccard， 不是 average Jaccard——只要有一对方法高度相关，consensus 就会退化； (3) 为 Claim 2 提供了又一个符合预测的数据点（Spearman correlation 更稳健）。\n\n\nArithmetic (Greaterthan) 的计算结构天然导致方法收敛：比较操作依赖一组固定的 comparison heads 和 magnitude-encoding MLPs，任何基于性能的方法都会被迫 选中这些瓶颈边。EAP-IG×EP 的 Jaccard 从 GPT-2 的 0.695 降至 Qwen 的 0.58 ——Qwen 的更大模型容量和 GQA 结构使得 comparison 计算略微分散到更多 head， 降低了 gradient-adjacent 的冗余。但 0.58 仍然远高于 CSS utility threshold (~0.55)。IFR 虽然作为不同族方法引入了新视角（IFR×EAP-IG=0.28），但 max pairwise Jaccard 仍由 EAP-IG×EP=0.58 主导——CSS=1.0 的 filtering 效果被 两个 gradient-adjacent 方法的高度共识所支配。CSS=1.0 CPR=0.935 低于 EAP-IG 的 0.975，确认 Arithmetic 在 Qwen 上仍是 CSS-negative case。 但 Jaccard 从 0.695 降至 0.58 提供了一个重要的 near-threshold 数据点， 说明 IFR 的加入确实在正确方向上推动了 method diversity。\n"
148	  },
149	  {
150	    "name": "Gemma-2 2B IOI K=3 (EAP-IG + EP + IFR)",
151	    "description": "将 CSS 扩展到 2B 参数量级模型。验证 localized circuit 模式在更大模型上是否 保持，以及 CSS faithfulness 优势是否随模型规模 scale。\n",
152	    "results": {
153	      "jaccard_eapig_ep": 0.25,
154	      "jaccard_eapig_ifr": 0.12,
155	      "jaccard_ep_ifr": 0.1,
156	      "max_pairwise_jaccard": 0.25,
157	      "css_3of3_edges": 12,
158	      "css_1.00_CPR": 0.13,
159	      "best_single_CPR": 0.04,
160	      "css1_cpr_advantage": 0.09
161	    },
162	    "tables": [
163	      {
164	        "name": "Table: Model Scaling Summary (GPT-2 → Qwen → Gemma)",
165	        "description": "三行对应三个模型，列: Params, Max Jaccard, CSS=1.0 Edges, CSS CPR, Advantage。展示 CSS utility 跨模型稳定\n"
166	      }
167	    ],
168	    "figures": [],
169	    "analysis": "P2 优先级实验，为 camera-ready 提供额外的泛化性证据。如果 deadline 紧张 可以推迟到 revision 阶段。但如果完成，三个不同架构（GPT-2 Transformer, Qwen GQA+SwiGLU, Gemma-2 sliding window）的一致结果将使 R1 泛化性 质疑几乎不可攻击。\n\n\n2B 模型的 IOI 电路比 0.5B 更分散——更多候选 head 可以承担 name mover 和 induction 功能。这增加了方法间的分歧（max Jaccard 进一步降至 0.25），因为 每种方法在候选 head 中做出不同的排序选择。CSS=1.0 过滤出三种方法共同认定的 12 条核心边，CPR=0.13 与 Qwen 结果一致。这证明 CSS 的 utility 不依赖于 特定模型架构或规模，而是由 method diversity（Jaccard）决定。\n"
170	  },
171	  {
172	    "name": "Llama-3.1 8B IOI K=3 (EAP-IG + EP + IFR)",
173	    "description": "最大规模验证（8B）。P3 优先级，需 A100 80GB。best tier 下可能不完成， 但如果资源允许则提供 impressive scaling evidence。\n",
174	    "results": {
175	      "max_pairwise_jaccard": 0.23,
176	      "css_3of3_edges": 14,
177	      "css_1.00_CPR": 0.12,
178	      "css1_cpr_advantage": 0.08
179	    },
180	    "tables": [],
181	    "figures": [],
182	    "analysis": "Stretch goal。如果完成，论文可以 claim CSS 在 117M→8B (68x) 范围内 稳健有效。如果未完成，Gemma-2 2B 已经提供了足够的 scaling evidence。\n\n\n8B 模型有大量冗余 head，IOI 电路更分散但核心 name mover 功能仍由少量 head 主导。方法分歧进一步增加（Jaccard→0.23），CSS=1.0 的 14 条边 精准锁定 consensus core。CPR=0.12 与小模型一致，说明 CSS utility 是 scale-invariant 的。EP 在 8B 模型上计算量大（需 edge-level pruning on 8B），可能需要近似——如果近似引入噪声，Jaccard 可能进一步降低。\n"
183	  },
184	  {
185	    "name": "Top-k Binarization Sensitivity Sweep",
186	    "description": "在所有已完成的 model×task 组合上系统扫描 k=50/75/100/150， 验证 CSS=1.0 CPR 对 k 选择的鲁棒性。直接回应 R5。\n",
187	    "results": {
188	      "ioi_gpt2": {
189	        "k50_css_edges": 7,
190	        "k50_css_CPR": 0.109,
191	        "k75_css_edges": 12,
192	        "k75_css_CPR": 0.102,
193	        "k100_css_edges": 18,
194	        "k100_css_CPR": 0.098,
195	        "k150_css_edges": 24,
196	        "k150_css_CPR": 0.091
197	      },
198	      "sva_gpt2": {
199	        "k50_css_edges": 8,
200	        "k50_css_CPR": 0.12,
201	        "k75_css_edges": 14,
202	        "k75_css_CPR": 0.11,
203	        "k100_css_edges": 20,
204	        "k100_css_CPR": 0.105,
205	        "k150_css_edges": 28,
206	        "k150_css_CPR": 0.095
207	      },
208	      "css_advantage_positive_across_all_k": true,
209	      "max_cpr_variation": 0.025
210	    },
211	    "tables": [
212	      {
213	        "name": "Table: Binarization Sensitivity (IOI + SVA)",
214	        "description": "行: k=50, 75, 100, 150 + isinf baseline 列: CSS=1.0 Edges, CSS=1.0 CPR, Best-Single CPR, Δ, Max Jaccard 每个 task 一个 sub-table\n"
215	      }
216	    ],
217	    "figures": [],
218	    "analysis": "此 ablation 是 R5 的完整回应。结论：CSS=1.0 的 faithfulness advantage 是 k-robust 的（max variation < 0.025），实践中 k=50 是 conservative 且 sufficient 的默认值。论文可以在 Method 章节推荐 k=50 并在 appendix 放 完整 sensitivity 表。\n\n\n随着 k 增加，每个方法保留更多边，pairwise overlap 增加，CSS=1.0 集合扩大。 扩大的 CSS=1.0 包含了更多低置信度的 consensus 边（三种方法在 top-50 之外 的边上的共识更可能是偶然的），因此 CPR 微降。但关键是：(1) CPR 始终为正 且高于 best single method，说明 consensus core 的信号不依赖于 k 的精确选择； (2) 边数与 k 近似线性增长，说明新增的 consensus 边是渐进的而非跳跃的—— 没有 critical threshold artifact。k=50 是合理的 default 选择（CPR 最高）， 但 k=75-150 都给出 qualitatively identical 的结论。\n"
219	  },
220	  {
221	    "name": "Ablation Method Comparison (Zero vs Mean vs Resample)",
222	    "description": "在 IOI 和 SVA 上比较三种 faithfulness 评估方式下的 CSS 优势稳定性。\n",
223	    "results": {
224	      "ioi_zero": {
225	        "css_1.00_CPR": 0.109,
226	        "best_single_CPR": 0.029,
227	        "advantage": 0.08
228	      },
229	      "ioi_mean": {
230	        "css_1.00_CPR": 0.145,
231	        "best_single_CPR": 0.065,
232	        "advantage": 0.08
233	      },
234	      "ioi_resample_mean": {
235	        "css_1.00_CPR": 0.125,
236	        "best_single_CPR": 0.045,
237	        "advantage": 0.08
238	      },
239	      "ioi_resample_std": 0.018,
240	      "sva_zero": {
241	        "css_1.00_CPR": 0.12,
242	        "best_single_CPR": 0.03,
243	        "advantage": 0.09
244	      },
245	      "sva_mean": {
246	        "css_1.00_CPR": 0.155,
247	        "best_single_CPR": 0.065,
248	        "advantage": 0.09
249	      },
250	      "sva_resample_mean": {
251	        "css_1.00_CPR": 0.135,
252	        "best_single_CPR": 0.04,
253	        "advantage": 0.095
254	      },
255	      "advantage_stable_across_methods": true,
256	      "max_advantage_variation": 0.015
257	    },
258	    "tables": [
259	      {
260	        "name": "Table: Ablation Method Robustness",
261	        "description": "行: Zero, Mean, Resample(n=10) 列: CSS=1.0 CPR, Best-Single CPR, Δ, p-value (resample) IOI 和 SVA 各一个 panel\n"
262	      }
263	    ],
264	    "figures": [],
265	    "analysis": "P2 实验，主要用于 appendix。如果 reviewer 质疑 evaluation protocol， 此表是 decisive response。实际上 zero ablation 是最保守的（CSS 优势最难 显现的条件），所以主实验用 zero ablation 是 methodologically conservative。\n\n\n三种 ablation baseline 改变的是绝对 CPR 水平，但不改变 CSS=1.0 与 single-method 之间的相对差异。Mean ablation 最温和（baseline 更接近正常 activations），所有方法的 CPR 都偏高；zero ablation 最激进，CPR 整体偏低； resample 介于两者之间。CSS=1.0 的优势在三种评估下保持 Δ≈0.08-0.09， 因为 consensus 捕获的是 method-independent 的核心功能边——这些边在任何 ablation scheme 下都是 critical 的。这排除了\"CSS 优势是 evaluation artifact\" 的质疑。\n"
266	  },
267	  {
268	    "name": "CIRCUS vs CSS Negative Ablation",
269	    "description": "系统对比 CIRCUS（threshold diversity within single method）和 CSS （cross-method consensus），证明结构共识优于单方法内部的阈值稳定性筛选。\n",
270	    "results": {
271	      "ioi": {
272	        "circus_core_edges": 15,
273	        "circus_CPR": -0.108,
274	        "css_1.00_edges": 7,
275	        "css_1.00_CPR": 0.109
276	      },
277	      "sva": {
278	        "circus_core_edges": 12,
279	        "circus_CPR": -0.025,
280	        "css_1.00_edges": 8,
281	        "css_1.00_CPR": 0.12
282	      },
283	      "factual": {
284	        "circus_core_edges": 18,
285	        "circus_CPR": -0.015,
286	        "css_1.00_edges": 15,
287	        "css_1.00_CPR": 0.055
288	      },
289	      "circus_negative_on_all_tasks": true
290	    },
291	    "tables": [
292	      {
293	        "name": "Table: CIRCUS vs CSS Head-to-Head",
294	        "description": "行: IOI, SVA, Factual Recall 列: Method, Edges, CPR, CMD 每个任务两行：CIRCUS core 和 CSS=1.0\n"
295	      }
296	    ],
297	    "figures": [],
298	    "analysis": "此 negative ablation 是对 competitor CIRCUS (Parekh 2026) 的直接回应， 也从理论上论证了 cross-method consensus 的必要性。即使 CIRCUS 在 Parekh 的原始 setting 中有效，它的 single-method assumption 使其在 CSS 的 framing 下天然处于劣势。此结果可以放在 Related Work 中用一段话 + 一个表来展示。\n\n\nCIRCUS 通过扫描 EAP-IG 的阈值范围，选取在不同阈值下始终存在的\"核心\"边。 这些边确实是 EAP-IG 得分最高且最稳定的边——但它们仍然是 EAP-IG 的 method-specific 视角。当 EAP-IG 本身存在系统性偏差（如过度依赖 early layer attention head 的 gradient signal），CIRCUS 只会放大这种偏差而非 纠正它。IOI 上 CIRCUS CPR=-0.108 说明 EAP-IG 的\"最确定\"边恰恰是 破坏性最大的（这些边可能是 EAP-IG gradient 信号的 artifact，不对应 真正的功能电路）。CSS=1.0 通过要求多方法共识，天然过滤掉了任何单方法的 系统性偏差。在所有三个 CSS-positive 的任务上，CIRCUS CPR 均为负值， 而 CSS CPR 均为正值——这是 cross-method consensus 优于 within-method robustness 的 decisive evidence。\n"
299	  },
300	  {
301	    "name": "Jaccard-CSS Utility Correlation Analysis",
302	    "description": "汇总所有 model×task 组合的 (max pairwise Jaccard) 和 (CSS CPR advantage)， 计算 Spearman 相关系数，拟合 CSS utility threshold。这是 Claim 2 的 definitive evidence。\n",
303	    "results": {
304	      "data_points": [
305	        {
306	          "task": "SVA (GPT-2)",
307	          "max_jaccard": 0.22,
308	          "one_minus_jaccard": 0.78,
309	          "css_cpr_advantage": 0.09
310	        },
311	        {
312	          "task": "IOI (Qwen+IFR)",
313	          "max_jaccard": 0.28,
314	          "one_minus_jaccard": 0.72,
315	          "css_cpr_advantage": 0.09
316	        },
317	        {
318	          "task": "IOI (GPT-2)",
319	          "max_jaccard": 0.31,
320	          "one_minus_jaccard": 0.69,
321	          "css_cpr_advantage": 0.08
322	        },
323	        {
324	          "task": "Factual (GPT-2)",
325	          "max_jaccard": 0.48,
326	          "one_minus_jaccard": 0.52,
327	          "css_cpr_advantage": 0.018
328	        },
329	        {
330	          "task": "Arithmetic (Qwen+IFR)",
331	          "max_jaccard": 0.58,
332	          "one_minus_jaccard": 0.42,
333	          "css_cpr_advantage": -0.04
334	        },
335	        {
336	          "task": "Arithmetic (GPT-2)",
337	          "max_jaccard": 0.695,
338	          "one_minus_jaccard": 0.305,
339	          "css_cpr_advantage": -0.066
340	        }
341	      ],
342	      "spearman_rho": 0.94,
343	      "spearman_p": 0.005,
344	      "n_data_points": 6,
345	      "fitted_threshold": 0.53,
346	      "threshold_ci_95": [
347	        0.48,
348	        0.58
349	      ],
350	      "spearman_rho_4task": 1.0,
351	      "spearman_p_4task": 0.042
352	    },
353	    "tables": [
354	      {
355	        "name": "Table: Jaccard-CSS Correlation Data",
356	        "description": "行: 6 个 model×task 组合 列: Task, Model, Methods, Max Jaccard, CSS=1.0 CPR, Best-Single CPR, Δ(advantage), CSS=1.0 Edges 底部: Spearman ρ=0.94, p=0.005\n"
357	      }
358	    ],
359	    "figures": [],
360	    "analysis": "此分析是论文的 crown jewel。6 个数据点虽然不多，但覆盖了 localized→distributed spectrum 和两个模型架构，Spearman ρ=0.94 在 p=0.005 下显著。Jaccard threshold ≈ 0.53 提供了 actionable guideline——这是 reviewer 最希望看到的 practical contribution。仅用 4 个 GPT-2 任务时 ρ=1.0 但 p=0.042（4 个点的 perfect rank correlation 仍然 marginal），加入 Qwen 数据使 p 降至 0.005， 大幅增强统计说服力。建议论文主文放 4-task 分析（因为更 clean），appendix 放 6-point 分析（加入跨模型验证）。\n对 reviewer R1（泛化性）的回应：4 个任务覆盖 localized (SVA, IOI) 和 distributed (Factual, Arithmetic)，2 个模型覆盖不同架构——足以建立 pattern。 对 reviewer R3（K≈2）的回应：IFR 的引入使 Qwen 数据点落在 GPT-2 趋势线上， 证明 method diversity（而非特定方法组合）是 CSS utility 的决定因素。\n\n(1-max_Jaccard) 与 CSS_CPR_advantage 的 Spearman ρ=0.94 (p=0.005) 证明 方法多样性是 CSS utility 的强预测因子。这不是偶然的——有清晰的机械解释： 当三种方法独立发现不同的边集（低 Jaccard），它们的交集代表被多种不同算法 视角共同验证的功能核心，这些边大概率是 true circuit edges 而非 method artifacts。当方法高度相关（高 Jaccard），交集趋近于最 selective 的单方法 结果，共识不再增加信息量。 fitted threshold ≈ 0.53 意味着：如果三种发现方法的 max pairwise Jaccard < 0.53，使用 CSS=1.0 consensus 可以预期 faithfulness 提升；如果 > 0.53， 应直接使用性能最好的单方法。这是一个可操作的 meta-diagnostic guideline。 6 个数据点覆盖了 Jaccard 0.22-0.695 的完整区间，包括 2 个模型、4 个任务， 关系的稳健性已足够说服 reviewer。\n"
361	  }
362	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ea333cc-f1da-49c6-a029-b28e825b8f79",
  "isSidechain": true,
  "promptId": "a58b825b-71c5-48ad-a01b-a7815951ccb9",
  "agentId": "aa6e698b89154230b",
  "type": "user",
  "uuid": "90dc3828-7bcd-4084-a021-e87e7f5dcbd5",
  "sourceToolAssistantUUID": "0ea333cc-f1da-49c6-a029-b28e825b8f79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-13T08:44:44.245Z_

Perfect! I've successfully read all the key files. Let me compile a comprehensive summary of the planned and remaining experiments.

## Summary: Planned and Remaining Experiments for StructFuse-Context

Based on the files read (ROADMAP.md, imagined_experiments.yaml files, and experiment_data.json files across best/median/worst tier scenarios), here is what I found:

### Project Status (as of 2026-05-13)

**Current Phase:** MVP validation — IOI has PASSED_MAIN (off-diagonal 13.3%), Arithmetic experiments running
**Deadline:** EMNLP 2026 ARR (May 25, 2026) — 12 days remaining

---

## Completed Experiments

### MVP Pilot Phase (DONE)
1. **GPT-2 Small IOI K=3** (EAP-IG + EP + ACDC)
   - Status: PASS — CSS shows clear advantage
   - Max Jaccard: 0.31, CSS=1.0 CPR: 0.109 vs best single 0.029 (+0.08 advantage)
   
2. **GPT-2 Small SVA K=3** (plan_004 - DONE across all tiers)
   - Median/Best: Partial support — CSS=1.0 CPR 0.941 (edge-efficient but not superior)
   - Worst: FAIL — CSS=1.0 CPR 0.88 < EAP-IG 0.95
   - Jaccard 0.38-0.55 depending on tier

### Phase 2 Cross-Model Experiments (DONE or IN PROGRESS)

3. **Qwen-2.5 0.5B IOI K=3 (EAP-IG + EP + IFR)** (plan_006 - DONE)
   - Median: Mixed (CPR 0.103, Jaccard 0.55 — IFR-EP high correlation weakens consensus)
   - Best: Strong support (CPR 0.14, Jaccard 0.28)
   - Worst: Negative (CPR 0.08 vs best single 0.10, Jaccard 0.52)

4. **Qwen-2.5 0.5B Arithmetic K=3** (plan_007 - DONE)
   - Median/Best: Negative case but important trend data (Jaccard 0.61, CSS advantage -0.04 to -0.039)
   - Worst: FAIL (Jaccard 0.58, CSS advantage -0.07)
   - Shows IFR partially lowers Jaccard but not enough

5. **GPT-2 Small DocQA/Factual K=3** (plan_005)
   - Median/Best: ABANDONED — GPT-2 factual recall too weak for meaningful circuits
   - Worst: FAIL — Task-model mismatch prevents valid results

---

## Planned But NOT YET Completed Experiments

### High Priority (P1) - Should Complete Before Deadline

6. **Arithmetic on GPT-2 Small** (plan continuation)
   - Status: GATE PENDING (awaiting mvp_arithmetic_gpt2_k3 completion)
   - Critical for: MVP gate decision (off-diagonal % determines Main vs Findings track)

### Medium Priority (P2) - May Complete If Time Allows

7. **Gemma-2 2B IOI K=3** (plan_008)
   - Status: NOT ATTEMPTED in median/worst
   - Best tier: PLANNED for model scaling evidence
   - Requires: ~16 GPU-hours, depends on plan_006 validation
   - Expected: Verify CSS utility stable across model scale

8. **Ablation Method Comparison** (plan_011 - PARTIAL)
   - Completed: IOI (GPT-2) zero/mean/resample ablation
   - NOT DONE: SVA and Arithmetic full ablation comparison
   - Status: P2 priority, low time budget remaining

9. **Binarization Sensitivity Sweep k=50/75/100/150** (plan_010)
   - Status: DONE for IOI/Arithmetic/SVA/Qwen-IOI
   - Shows CSS=1.0 CPR stable within k=75-150 range (Δ < 0.015)

### Low Priority (P3) - Likely Will NOT Complete

10. **Llama-3.1 8B IOI K=3** (plan_009)
    - Status: NOT ATTEMPTED across all tiers
    - Requires: A100 80GB (expensive), ~24 GPU-hours
    - Best tier: PLANNED as stretch goal
    - Worst tier: Explicitly recommend CANCEL to save resources

### Analysis-Only Experiments (0 GPU hours - Writing Work)

11. **Jaccard-CSS Correlation Analysis** (plan_013 - DONE)
    - Best: 6 data points, Spearman ρ=0.94 (p=0.005) — strong significant correlation
    - Median: 5 data points, Spearman ρ=-0.90 (p=0.037) — marginal statistical power
    - Worst: Underpowered (p=0.27) — relationship confounded by ACDC isinf binarization
    - Threshold: CSS utility when max_Jaccard < ~0.50

12. **CIRCUS vs CSS Negative Ablation** (plan_012 - DONE)
    - Best/Median: DONE — CSS shows clear superiority (CSS CPR positive vs CIRCUS negative)
    - Worst: DONE — Both methods fail, CSS vs CIRCUS becomes "less bad" comparison
    - GPU cost: 0 hours (analysis only)

---

## Key Gate Decisions Pending

| Decision ID | Status | Impact |
|---|---|---|
| D027 | PENDING | MVP final verdict (CSS faithfulness advantage task-dependent?) |
| D026 | FAIL | Arithmetic D025 gate failed, delaying MVP result |
| D025 | UPDATED | Arithmetic gate now requires 4-condition CSS-only standard |

---

## Resource & Timeline Constraints

- **GPU Budget:** ~290 GPU-hours total needed; RTX 4090D allocated (cuda:5@cqa1-21977)
- **Time Remaining:** 12 days to deadline (May 25)
- **Critical Path:** Complete Arithmetic validation → gate decision → Phase 2 → paper writing

---

## Actionable Next Steps

1. **Immediate (next 24h):** Complete `mvp_arithmetic_gpt2_k3` to trigger gate decision
2. **If PASS:** Proceed to `complete_mvp` → deploy IFR/Phase 2 scripts → start Qwen experiments
3. **If marginal:** Run ACDC top-k validation + SVA reconfirmation before advancing
4. **Paper:** Write paper_framing.md + experiment_plan.yaml (can proceed in parallel)
5. **Skip if time-pressed:** Gemma-2 2B and Llama-3.1 8B (push to revision or future work)

---

**File Locations:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/ROADMAP.md` — Full current roadmap
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/{best,median,worst}/imagined_experiments.yaml` — Per-tier planned experiments
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/dream_reports/dream_20260513T054654/{best,median,worst}/experiment_data.json` — Detailed results & analyses

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90dc3828-7bcd-4084-a021-e87e7f5dcbd5",
  "isSidechain": true,
  "agentId": "aa6e698b89154230b",
  "requestId": "req_011CazGpFShpaT9LNKCzpZVo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "19d1dd31-de70-4da2-a22b-dfa8a63a2f1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "e9dab49e-7023-433c-8732-47d8c2174eb9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012LtryrhsVpcLhwrCyFp1uU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 14335,
      "cache_creation_input_tokens": 23959,
      "cache_read_input_tokens": 63257,
      "output_tokens": 1904,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23959
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 14335,
          "output_tokens": 1904,
          "cache_read_input_tokens": 63257,
          "cache_creation_input_tokens": 23959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23959,
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
