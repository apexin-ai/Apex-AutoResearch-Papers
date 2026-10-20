# Research conversation: Read the file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper_framing.md and extra

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a5e7ddcdb00ffae00.jsonl`
- **Structured JSON:** [`c83990b9b9e0550a9ac7.json`](../../sessions/c8/c83990b9b9e0550a9ac7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

11 recorded events

### User

_source line 1 · 2026-05-19T18:24:21.729Z_

Read the file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper_framing.md and extract:
1. The full text of Claim 5 (about scaling/evidence tax)
2. Any sections about "variance compression" as a core finding
3. Any updated numbers or narrative guidance for the "1.7B RSFT vs 8B SFT" comparison
4. Any guidance about D112 Method B

Report the exact text. This is a markdown file, likely structured with headers and bullet points.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a52d2a02-5bc0-4012-8f39-29957ce260bc",
  "agentId": "a5e7ddcdb00ffae00",
  "type": "user",
  "uuid": "214a07f5-5f04-4c2f-985c-32041e3c2baf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-19T18:24:23.049Z_

I'll read the file and extract the requested information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "214a07f5-5f04-4c2f-985c-32041e3c2baf",
  "isSidechain": true,
  "agentId": "a5e7ddcdb00ffae00",
  "requestId": "req_011CbCPtxN3Y8wYes5DnGYNZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "010e6fef-a82c-4645-8fab-81823e5dc17b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0187pv8XTgYxuetvts5Gq5cu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 560,
      "cache_read_input_tokens": 24839,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 560,
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

_source line 3 · 2026-05-19T18:24:23.245Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PhGeNJCtffhsKy2LADS2hv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "010e6fef-a82c-4645-8fab-81823e5dc17b",
  "isSidechain": true,
  "agentId": "a5e7ddcdb00ffae00",
  "requestId": "req_011CbCPtxN3Y8wYes5DnGYNZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6adec0d7-ec80-4c30-971c-07930f4f696d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0187pv8XTgYxuetvts5Gq5cu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 560,
      "cache_read_input_tokens": 24839,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 560
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 24839,
          "cache_creation_input_tokens": 560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 560,
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

_source line 4 · 2026-05-19T18:24:23.262Z_

<details><summary>↩ Tool result · reported error · `toolu_01PhGeNJCtffhsKy2LADS2hv`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6adec0d7-ec80-4c30-971c-07930f4f696d",
  "isSidechain": true,
  "promptId": "a52d2a02-5bc0-4012-8f39-29957ce260bc",
  "agentId": "a5e7ddcdb00ffae00",
  "type": "user",
  "uuid": "1616ee1d-34dd-42de-9d94-c859e014fccb",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b.",
  "sourceToolAssistantUUID": "6adec0d7-ec80-4c30-971c-07930f4f696d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-19T18:24:24.662Z_

The file doesn't exist at that path. Let me find the correct location of the paper_framing.md file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1616ee1d-34dd-42de-9d94-c859e014fccb",
  "isSidechain": true,
  "agentId": "a5e7ddcdb00ffae00",
  "requestId": "req_011CbCPu4qUg7k7Nc6RiiNyW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fc27d9c9-c1ae-4617-850e-0d122c889f29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FsxKe86qbs5F86kS5oDheJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 25399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1006,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T18:24:24.849Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YQHSUizyX2jJM727CGYQnS`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie -name \"paper_framing.md\" -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc27d9c9-c1ae-4617-850e-0d122c889f29",
  "isSidechain": true,
  "agentId": "a5e7ddcdb00ffae00",
  "requestId": "req_011CbCPu4qUg7k7Nc6RiiNyW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ffd1f4c3-49f7-4d2d-afa0-4bf06e7ef5c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FsxKe86qbs5F86kS5oDheJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 25399,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1006
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 124,
          "cache_read_input_tokens": 25399,
          "cache_creation_input_tokens": 1006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1006,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T18:24:24.953Z_

<details><summary>↩ Tool result · `toolu_01YQHSUizyX2jJM727CGYQnS`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T105318/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T105318/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T105318/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T120227/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260516T155803/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260515T132059/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffd1f4c3-49f7-4d2d-afa0-4bf06e7ef5c3",
  "isSidechain": true,
  "promptId": "a52d2a02-5bc0-4012-8f39-29957ce260bc",
  "agentId": "a5e7ddcdb00ffae00",
  "type": "user",
  "uuid": "c1cf7abb-e963-442e-b224-304e5ff3543a",
  "sourceToolAssistantUUID": "ffd1f4c3-49f7-4d2d-afa0-4bf06e7ef5c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-19T18:24:26.359Z_

Found it. Let me read the main project file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1cf7abb-e963-442e-b224-304e5ff3543a",
  "isSidechain": true,
  "agentId": "a5e7ddcdb00ffae00",
  "requestId": "req_011CbCPuCAFx3rmgmQWEhxPt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "59da7cb8-5d3e-4ebf-84b5-0713839bd8a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01454RAyKKcDFAYcEhxmW57c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1800,
      "cache_read_input_tokens": 25399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1800,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T18:24:26.515Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K8CZDjM16gQsG6AjgZwKVT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59da7cb8-5d3e-4ebf-84b5-0713839bd8a6",
  "isSidechain": true,
  "agentId": "a5e7ddcdb00ffae00",
  "requestId": "req_011CbCPuCAFx3rmgmQWEhxPt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "58f2c7f8-15ea-41bc-8944-4afb99e6475b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01454RAyKKcDFAYcEhxmW57c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1800,
      "cache_read_input_tokens": 25399,
      "output_tokens": 98,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1800
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 98,
          "cache_read_input_tokens": 25399,
          "cache_creation_input_tokens": 1800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1800,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T18:24:26.528Z_

<details><summary>↩ Tool result · `toolu_01K8CZDjM16gQsG6AjgZwKVT`</summary>

```text
1	# Paper Framing — FREIGE
2	
3	> **状态**: 审稿修复中（D103 Action Matrix）— Round 1 得分 3.0 (Findings)，22 个 issue 跟踪中
4	> **最后更新**: 2026-05-19 (D117-D120: 14B tax=0, surpasses→approaches, D112 Method B=0.5152, 8B RSFT 3v3 variance 7.4×)
5	> **审稿 Round 1**: 3.0 (Findings)。3 个系统性问题：claim>evidence、实验混淆、贡献过度
6	> **贡献重构**: 4 贡献 → 3 贡献（CED 合并入 RSFT，EDCR 降级为分析工具）
7	> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成
8	> **Dream v2**: best=3.0, median=2.5, worst=2.5
9	
10	## ⚠️ Post-Review Contribution Restructuring (D103)
11	
12	审稿后从 4 贡献重构为 3 贡献：
13	
14	### 原 4 贡献
15	1. Task formalization (evidence-grounded DocRE)
16	2. EDCR diagnostic metric
17	3. Decoupling spectrum
18	4. CED scoring
19	
20	### 新 3 贡献
21	1. **Evidence-grounded DocRE + RSFT with NLI-based scoring** — 合并原 C1+C4。CED 不再作为独立贡献，NLI-based scoring（CED/flat-NLI 等效）是 RSFT 有效的关键组件
22	2. **Decoupling spectrum（观察性，非因果）** — 原 C3 降级为观察性描述。"co-occurs with" 替代 "acts as amplifier"。EDCR 作为分析工具嵌入此贡献（不独立列出）
23	3. **Scale-dependent evidence tax + RSFT variance compression** — 原 C5 提升为正式贡献。4 尺度 (1.7B/4B/8B/14B) evidence tax curve + RSFT 跨 scale 一致压缩 seed 方差 (7-31×, D118)。"scale-dependent" 替代 "non-monotonic"（4 个数据点支撑趋势，非严格 non-monotonic claim）
24	
25	### 关键 claim 调整
26	- 所有因果 claim → 观察性描述（GRPO "acts as catastrophic amplifier" → "co-occurs with"）
27	- EDCR ρ 从 -0.965 (n=15) 改为去重后数值（待 Agent 计算完成）
28	- "+8pp" → fair subset "+6.2pp"，Abstract 加 "on a controlled evaluation subset"
29	- "matches 8B SFT" → "approaches 8B SFT"
30	- CED vs flat-NLI 不再区分，统称 "NLI-based scoring"
31	
32	## Target Venue
33	
34	- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)
35	- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)
36	
37	## Core Insight
38	
39	LLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。
40	
41	我们系统性地探索了 online RL (GRPO) 、offline preference optimization (DPO) 和 offline RL (RSFT) 三条技术路线。关键发现：**RL optimization pressure 与 evidence-extraction decoupling severity 正相关**——优化强度越大，evidence 质量提升的同时抽取能力退化越严重。QLoRA 放大至 catastrophic（rel_f1<0.02），bf16 GRPO 从 0.4549 退化至 ~0.434（mild, -2pp），DPO 呈 gradual 退化（1ep→3ep rel_f1 从 0.4034→0.3429），RSFT 无 decoupling。
42	
43	**Evidence tax 是 scale-dependent 的（non-monotonic pattern, D079/D082/D083/D117）**：1.7B 模型中 evidence generation 反而带来 +6.2pp 收益（隐式正则化），4B 模型付出 -7.5pp 代价，8B Qwen/LLaMA 和 14B 容量足够 absorb（≈0）。RSFT 不加重 tax（8B RSFT tax=-0.78pp, D119）。这推翻了"evidence 总有代价"的简单叙事。
44	
45	CED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 和 flat-NLI 作为 RSFT scoring functions 统计不可区分（D078 paired t-test p=0.44），但均显著优于 random/no scoring。CED 因可解释性优势作为默认推荐方案。
46	
47	## Story Arc
48	
49	1. **Problem**: LLM DocRE 无证据 → 部署障碍
50	2. **New task**: evidence-grounded DocRE — 同时生成关系和证据
51	3. **Cost of faithfulness**: evidence generation 代价是 **scale-dependent** 的——4B 付出 -7.5pp 代价，1.7B 反而获益 +6.2pp，8B 和 14B 趋近于零（D117: 14B tax=+0.03pp）。非固定成本，与模型容量非线性交互（D079/D082/D083/D117）
52	4. **Exploration**: 系统性比较 online RL (GRPO) vs offline preference (DPO) vs offline RL (RSFT)
53	5. **Key finding**: evidence-extraction decoupling — RL optimization pressure 与 decoupling severity 正相关，形成连续谱系（GRPO-QLoRA catastrophic > GRPO-bf16 mild > DPO gradual > RSFT none）
54	6. **QLoRA amplification**: QLoRA 量化将 mild decoupling 放大至 catastrophic forgetting——decoupling 是 RL-for-IE 中 multi-objective competition 的通用梯度（intra-task trade-off，非 inter-task forgetting），QLoRA 是 catastrophic amplifier
55	7. **What works**: RSFT with NLI-based scoring 是唯一有效路线——提升 evidence 质量而不牺牲抽取
56	8. **Best practical solution**: CED reranker（response-level 选择）恢复 97% 的 evidence 代价，evi_f1=0.8188。注意：CED 有效粒度是 response-level reranking，不是 sentence-level filtering（D090: sentence-level CED filter 是 negative result，recall -20pp）
57	8b. **Evidence strategy spectrum (D090/D091)**: Post-hoc retrieval（加法，BM25 k=2 evi_f1_joint=0.347）< Joint generation（RSFT, evi_f1_joint=0.361）。Post-hoc filter（减法，Lead 1 CED sentence filter）= negative。Joint generation 产出的 evidence 更 faithful（EDCR 0.654 vs 0.766）
58	9. **Diagnostic tool**: EDCR 双层诊断——方法级量化 decoupling（与 Claim 2 呼应），per-relation 级揭示 evi_f1 不捕捉的 relation-type 难度差异（D070 ✅）
59	10. **Scaling & generalization**: evidence tax 呈 non-monotonic scaling pattern（1.7B→4B→8B→14B, D079/D082/D083/D117），跨模型家族（LLaMA-8B, D082）和跨数据集（Re-DocRED, D080）验证泛化性。RSFT variance compression（7-31× across scales, D118）——CED filtering 消除 seed-dependent 噪声，使小模型 approaches 大模型 SFT 水平
60	
61	## Core Claims (reframed after Dream v1, updated D068-D083)
62	
63	### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力
64	- FREIGE 是首个**基于生成式 LLM** 的 evidence-grounded DocRE 方法（⚠️ 必须始终保持 "generative LLM" 限定词——SAIS 已做 encoder-based evidence retrieval + DocRE）
65	- **关键区分 (Reviewer warning)**：encoder-based evidence *retrieval*（SAIS, DREEAM — 分类哪些句子是证据，evidence supervision 提升 RE）vs generative evidence *production*（FREIGE — LLM 生成证据文本，额外生成负担导致 scale-dependent 代价）。论文 Related Work 必须精准讨论此对比，否则审稿人会问 "为什么 SAIS 说 evidence 有用，你说 evidence 有害"
66	- **Evidence generation tax**: scale-dependent，详见 Claim 5（D079/D082/D083）
67	- RSFT 在 4/4 配置下均超过 SFT baseline（Ign-F1 +3.3~5.5pp）
68	- **CED reranker 是最优实用方案**: rel_f1=0.4864（仅低于 no-evidence 0.29pp），evi_f1=0.8188（plan_005 ✅）
69	- **D076 统一协议最终数字（可写入论文）**:
70	  - SFT baseline: rel_f1=0.4049
71	  - CED RSFT mean: rel_f1=0.4569 (s42=0.4517, s44=0.4621)
72	  - flat-NLI RSFT mean: rel_f1=0.4561 (s42=0.4535, s43_r2=0.4586)
73	  - CED vs flat-NLI Δ=0.0008，统计不可区分（D078 p=0.44）
74	- **Cross-family validation (D082)**: LLaMA-3.1-8B SFT rel_f1=0.5514, evi_f1=0.8151; no-evidence rel_f1=0.5624（evidence tax = -0.7pp，8B 容量足够 absorb）
75	- **Cross-dataset validation (D080)**: Re-DocRED Ign-F1 下降 3.15pp 但 Evi-F1 保持 0.817——evidence extraction 能力跨数据集泛化
76	- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）
77	- **RSFT 方法论定位**：诚实承认 RSFT 是 STaR (NeurIPS 2022) 的单轮变体 + evidence quality scoring。创新点在于将 STaR-like self-improvement 应用于 evidence-grounded DocRE + CED/NLI 作为 domain-specific quality filter，而非框架本身
78	- **Evaluation caveat** (Limitations): GenRES 指出 exact match F1 低估 generative RE，FREIGE 所有 eval 用 exact match，应承认此局限（对所有方法同等适用，相对比较有效）
79	
80	### Claim 2 (Core finding): RL optimization pressure 与 evidence-extraction decoupling severity 正相关（D068/D069 修正）
81	- **Decoupling spectrum**: 优化强度越大，decoupling 越严重
82	  - GRPO QLoRA: catastrophic（rel_f1=0.0138, evi_f1=0.850, EDCR=0.99）— QLoRA 放大 decoupling
83	  - GRPO bf16: mild（rel_f1 从 0.4549→~0.434, -2pp; step_30=0.434, step_50=0.4276, step_70=0.4341）— 退化可控但持续（D065/D066）
84	  - DPO bf16 1ep→3ep: gradual（Ign-F1 38.88→TBD, rel_f1 0.4034→0.3429）— 随训练渐进退化（D067/D068）
85	  - RSFT: none — 无 decoupling，唯一有效路线
86	- **QLoRA 是 catastrophic amplifier，不是 root cause**: bf16 GRPO 仅 mild decoupling（-2pp），QLoRA 放大至 catastrophic（-39pp）（D054/D065/D066）
87	- **Decoupling 是 RL-for-IE 的通用梯度**: 跨方法（GRPO/DPO）、跨量化策略（QLoRA/bf16）一致出现，严重程度与优化压力正相关
88	- 三档 Dream 审稿均认为此发现\"genuinely novel and striking\"
89	- **已完成**: GRPO G=8 bf16 确认 mild decoupling（plan_011 ✅）; DPO 1ep/3ep 确认 gradual decoupling（plan_012 ✅）
90	
91	### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量——CED 与 flat-NLI 统计不可区分（D078）
92	- CED 和 flat-NLI 都显著优于 random/no scoring
93	- **D078 paired t-test 最终结论**: CED vs flat-NLI p=0.44，统计不可区分
94	  - CED RSFT mean rel_f1=0.4569 vs flat-NLI mean rel_f1=0.4561（Δ=0.0008）
95	  - 两种 scoring function 等效，CED 因可解释性（contrastive evidence discrimination）作为默认推荐
96	- ~~**Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为"one possible scoring function"~~ → **已确认降级（D078）**
97	- **论文叙事**: "NLI-based scoring（无论 CED 或 flat-NLI）是 RSFT 有效的关键——两种变体均等效提升质量，CED 额外提供可解释的 evidence discrimination"
98	- **top_k selection ablation (k=1 vs k=3)**:
99	  - k=1 (best-of-8) 优于 k=3 (top3-of-8)，CED scoring precision 随 k 增大下降
100	  - k=1 均值 (3 seeds s42/s43/s44): Ign-F1=45.00, rel_f1=0.4596, evi_f1=81.43, EDCR=0.6434
101	  - k=3 (1 seed, reeval_rsft_topk3): Ign-F1=43.64, rel_f1=0.4454, evi_f1=80.88, EDCR=0.6635
102	  - Δ (k=3 vs k=1 mean): Ign-F1 **-1.36pp**, rel_f1 **-1.42pp**, evi_f1 **-0.55pp**, EDCR +0.02
103	  - 训练数据质量下降: k=1 mean_f1=0.6157, mean_ced=0.6683 → k=3 mean_f1=0.5761, mean_ced=0.6205（来源: mvp2_rsft_ced_scoring / mvp2_rsft_ced_scoring_topk3_r2）
104	  - 训练集规模: k=1 选出 2718 样本 (12.4%), k=3 选出 8037 样本 (37%), 数据量 ×2.96 但质量下降抵消数量优势
105	  - **叙事**: 低排名 response 引入噪声——rank 2-3 样本的 F1 和 CED 分数均显著低于 rank 1，扩大训练集规模无法补偿数据质量的稀释。这表明 RSFT 的关键不在数据量而在 scoring precision
106	  - **注**: k=3 仅 1 seed，差异方向一致但尚不具备统计显著性；作为 ablation table 中的辅助行呈现，不作为独立 claim
107	  - **D102 跨 scale k=1 vs k=3 验证结果**:
108	    - 1.7B: k=1 +0.72pp ✓ | 4B: k=1 +1.02pp ✓ | LLaMA-8B: k=1 +1.51pp ✓ | 8B: k=1 -0.57pp (within seed variance 0.95pp)
109	    - **不能说 "k=1 consistently outperforms k=3"**（8B 方向相反）
110	    - **正确 framing**: "Methodological correction to match claimed k=1 protocol yields comparable or improved results across scales"
111	    - D102 的核心目标是方法学一致性修正，不是证明 k=1 更好
112	
113	### Claim 4 (Diagnostic): EDCR 双层诊断价值（D070/D072）
114	- **Layer 1 — 方法级**: EDCR 量化 evidence-extraction decoupling，与 Claim 2 spectrum 呼应
115	  - 方法级 EDCR 与 rel_f1 Spearman ρ=-0.965（plan_003 ✅）——本质是 decoupling 的度量
116	  - EDCR 识别病理模型（GRPO QLoRA: EDCR≈1.0）
117	- **Layer 2 — per-relation-type**: EDCR 提供 evi_f1 不捕捉的 relation-type 诊断信息 ✅
118	  - per-relation ρ(EDCR, evi_f1) = **-0.064** (p=0.58) → **完全独立于 evi_f1**
119	  - per-relation ρ(EDCR, rel_f1) = -0.793 (p<0.001) → 与 rel_f1 强相关但非完美
120	  - per-relation ρ(evi_f1, rel_f1) = -0.013 (p=0.91) → evidence 质量与抽取能力在 relation type 间完全解耦
121	  - 典型案例：date_of_birth (EDCR=0.118, 高 faithful) vs head_of_government (EDCR=0.956, 高 decoupled)
122	  - 93 relation types 分析（≥5 样本），76 个有非零数据
123	- **论文叙事**: EDCR 在方法级是 decoupling 度量工具（横向对比方法），在 relation 级是难度诊断工具（纵向定位薄弱 relation）——两层叙事互补
124	- **仍需**: 100 例人工标注验证（RC6）
125	
126	### Claim 5 (NEW — Scaling): Evidence Tax 呈 Non-Monotonic Scaling Pattern（D079/D082/D083）
127	- **核心发现**: evidence generation 的代价不是固定的——它与模型容量呈非线性关系
128	  - **1.7B (Qwen3-1.7B)**: +6.2pp BENEFIT — evidence generation 起隐式正则化作用，防止小模型过拟合（D083 公平子集分析确认）
129	  - **4B (Qwen3-4B)**: -7.47pp cost (D076: evi 39.74% / no-evi 47.21%) — 标准 evidence generation 负担，模型容量不足以同时优化两个目标
130	  - **8B Qwen (Qwen3-8B)**: ≈0 — 模型容量足够 absorb evidence generation 的额外负担
131	  - **8B LLaMA (LLaMA-3.1-8B)**: -0.7pp — 跨家族确认，8B 规模的 evidence tax 趋近于零
132	- **Non-monotonic 解释**: 小模型从 evidence 的正则化效应获益 > 生成负担；中等模型容量不足以同时做好两件事；大模型容量充裕，两个目标互不干扰
133	- **Mechanistic analysis (plan_020 完成)**：3 层机制解释 scale-dependent tax：
134	  - **(1) Duplication regularization（主因）**: monotonic decline — 1.7B 27.5pp gap (60.5%→33.0%), 4B 12.1pp gap (43.2%→31.1%), 8B 3.7pp gap (32.9%→29.2%)。正则化效应随容量增大递减
135	  - **(2) Truncation asymmetry**: 1.7B Δ=19pp (no-evi worse), 4B Δ=2pp (neutral), 8B Δ=-9pp (evi worse, tokens 消耗输出预算)
136	  - **(3) Fair comparison residual**: 排除截断后（442/985 docs），1.7B evidence 仍 +6.2pp (ign_f1)，8B Qwen -0.3pp，8B LLaMA +0.3pp — 证明 1.7B 有真实 reasoning scaffold 效应
137	  - **4B "capacity valley" 确认**: duplication 已低(31.1%，接近 8B 29.2%)不需正则化，truncation 中性(29.2% vs 31.2%)，但容量不足同时做 RE + evidence generation → 纯开销(+7.47pp tax, D076 protocol)
138	- **论文叙事**: "Evidence as implicit regularization" — 推翻 "evidence 总有代价" 的简单叙事。60.5%→33.0% duplication rate 是最有冲击力的数据点。建议 4 张图（duplication rate / truncation crossover / fair comparison / doc complexity）
139	- **Cross-family robustness**: LLaMA-8B 与 Qwen-8B 一致确认 8B 规模 evidence tax ≈ 0
140	- **RSFT 弥合 scale gap (D094→D102→D118)**: 1.7B RSFT 3-seed mean=**0.5119** (std=0.09pp) vs 8B SFT 3-seed mean=**0.5019** (std=3.72pp)，Δ=+1.0pp, p=0.69 不显著——CED-RSFT 使 1.7B 模型**接近** 4.7× 大的 8B SFT，但差异在统计噪声内。"surpasses" claim 被 D118 否定（8B SFT s43=0.5324 拉高均值），回退为 "approaches"
141	- **Variance Compression 为核心发现 (D118)**: RSFT 跨 3 个尺度一致性地压缩 seed 方差——1.7B **31×** (2.79pp→0.09pp), 4B **7.5×** (3.80pp→0.51pp), 8B **7.4×** (3.72pp→0.50pp)。这不仅是副产品而是 CED filtering 的本质效应：质量过滤消除了 seed-dependent 的训练噪声
142	- **14B SFT evidence tax ≈ 0 (D117)**: 14B with-evidence=0.5507, no-evidence=0.5510, tax=+0.03pp——14B 容量完全 absorb evidence 生成负担，延续 8B 的 neutral 趋势
143	- **RSFT evidence tax (D119/D121)**: RSFT 系统性消除 evidence 代价——4B RSFT tax=**+0.94pp** (vs SFT -7.47pp, 代价压缩 8×), 8B RSFT tax=**-0.78pp**。RSFT 在 ≥4B 尺度 evidence tax 趋近零，论文叙事："RSFT closes the evidence tax gap"
144	- **D112 Method B (full pipeline from s44 SFT)**: 4B RSFT bf16 ign_f1=**0.5152** (+4.18pp over SFT s44=0.4734)——确认 RSFT 不依赖特定 SFT seed，pipeline 可复现
145	
146	### Deep Error Analysis (plan_021 完成)
147	- **SFT→RSFT 三大改善机制（3 尺度一致）**:
148	  - **(1) Truncation FN 减少 -16~22%**: 1.7B 获益最大 (-841 FN)。与 evidence tax 的 truncation asymmetry 互洽
149	  - **(2) Hallucinated FP 减少 -6~12%**: LLaMA 获益最大 (-593, -11.8%)。CED filtering 淘汰了低质量 hallucinated responses
150	  - **(3) Duplicate 减少 -11~20%**: 1.7B 获益最大 (-20.2%)。与 duplication regularization 发现完全对应
151	- **未改善**: Evidence exact match 变化 <0.4pp（evidence grounding 需专门信号）; Relation confusion FP 稳定; Rare relation FN 稳定
152	- **与 Evidence Tax 分析的闭环**: Evidence regularization (tax analysis) ↔ RSFT format regularization (error analysis) 是同一机制的两个视角。小模型需要结构化约束来避免退化输出
153	- **Per-relation 获益最大**: participant, conflict, league, screenwriter, operator, contains_admin_territory — 跨句推理或长尾实体关系
154	- **Over-citation trend**: 大模型 over-citation 增加 (12%→17%)，边际预测的 evidence 精度下降
155	- **k=1 vs k=3 对比**: 1.7B + LLaMA k=1 优于 k=3; 8B k=3 略优 (+0.57 ign_f1)
156	- **关键 negative finding**: Evidence quality 完全不变 (exact match Δ<0.4pp) → RSFT 改善 RE 但不改善 evidence grounding → 需要专门的 evidence-aware 训练信号 → 直接 motivates GRPO+CED。形成完整 pipeline 故事线：SFT→RSFT(RE提升)→GRPO+CED(evidence提升)
157	- **Limitation**: "FN: other" 增加 ~13-15%（RSFT 消除 easy errors 但不解决 hard cases: 复杂推理、知识缺失）
158	- **产出**: art_20260518_cfce4e, LaTeX 表格已生成
159	
160	## MVP Evidence Summary (D071: 主表报 Ign-F1，附录报 F1; D076 统一协议 rel_f1)
161	
162	| Config | Ign-F1 | F1 | Δ vs SFT (Ign-F1) | Evi-F1 (cond) | Evi-F1 (joint) | EDCR |
163	|--------|--------|------|-------------------|---------------|---------------|------|
164	| **SFT no-evidence** | **47.21** | 48.76 | **+7.47pp** | **—** | **—** | **—** |
165	| SFT baseline (D076) | 39.74 | 40.49 | — | 79.86 | 31.47 | 0.6982 |
166	| **CED reranker** | **TBD** | 48.64 | **TBD** | **81.88** | — | **0.6156** |
167	| RSFT CED s43 (best) | **45.85** | 46.83 | **+6.11pp** | 81.56 | 37.11 | 0.6388 |
168	| RSFT CED s44 | 45.51 | 46.55 | +5.77pp | 80.87 | 37.13 | 0.6350 |
169	| RSFT CED s42 | 43.63 | 44.49 | +3.89pp | 81.87 | 34.68 | 0.6565 |
170	| RSFT CED k=3 | 43.64 | 44.54 | +3.90pp | 80.88 | — | 0.6635 |
171	| RSFT r2a (1ep) | 44.01 | 44.94 | +4.27pp | 81.08 | 35.09 | 0.6641 |
172	| RSFT r2b (1ep) | 44.10 | 44.93 | +4.36pp | 81.28 | 34.90 | 0.6609 |
173	| flat-NLI s42 | 44.49 | 45.39 | +4.75pp | 80.43 | — | 0.6431 |
174	| flat-NLI s43 (reeval) | TBD | 45.23 | TBD | 81.58 | — | 0.6505 |
175	| DPO bf16 1ep | 38.88 | 40.34 | -0.86pp | 80.88 | — | 0.7139 |
176	| DPO bf16 3ep | TBD | 34.29 | TBD | — | — | — |
177	| GRPO bf16 G=8 (best step) | 45.59 | ~43.4 | +5.85pp | 80.86 | — | — |
178	| GRPO QLoRA (lr=5e-6) | TBD | 1.38 | TBD | 85.00 | — | 0.9900 |
179	
180	注：Evi-F1 以百分比显示（×100）。Ign-F1 修正后排名无实质变化（仅 r2a/r2b 互换，差 0.09pp）。TBD 项等待 metrics_v2.json 补算。GRPO bf16 Ign-F1=45.59 > F1=43.4 因 train triples 过滤效应。RSFT CED k=3 数据来源: reeval_rsft_topk3 (ign_f1_corrected=true)。
181	
182	### D076 统一协议 rel_f1（可直接写入论文）
183	
184	| Config | rel_f1 | evi_f1 |
185	|--------|--------|--------|
186	| SFT baseline | 0.4049 | — |
187	| CED RSFT mean (s42, s44) | **0.4569** | — |
188	| CED RSFT s42 | 0.4517 | — |
189	| CED RSFT s44 | 0.4621 | — |
190	| flat-NLI RSFT mean (s42, s43_r2) | **0.4561** | — |
191	| flat-NLI RSFT s42 | 0.4535 | — |
192	| flat-NLI RSFT s43_r2 | 0.4586 | — |
193	| LLaMA-8B SFT | 0.5514 | 0.8151 |
194	| LLaMA-8B no-evidence | 0.5624 | — |
195	| **--- RSFT Scaling Study (D102 k=1 corrected) ---** | | |
196	| Qwen3-1.7B SFT | 0.4945 | — |
197	| Qwen3-1.7B RSFT k=1 s42 | **0.5290** (+3.5pp) | 0.8243, EDCR=0.6224 |
198	| Qwen3-8B SFT | 0.5262 | — |
199	| Qwen3-8B RSFT k=1 s42 | 0.5549 (+2.9pp) | 0.8136, EDCR=0.6231 |
200	| Qwen3-8B RSFT k=1 s43 | 0.5651 (+3.9pp) | 0.8180, EDCR=0.6094 |
201	| Qwen3-8B RSFT k=1 mean | **0.5600** (+3.4pp) | — |
202	| LLaMA-8B RSFT k=1 s42 | **0.5839** (+3.3pp) | 0.8243, EDCR=0.5799 |
203	| **--- Post-hoc Baseline (D091) ---** | | |
204	| BM25 entity k=2 | 0.4876 (no-evi) | evi_f1_joint=0.347 |
205	| BM25 oracle_k | 0.4876 | evi_f1_joint=0.383 |
206	
207	### Evidence Tax Scaling（D079/D082/D083/D117/D119）
208	
209	| Model | SFT Tax (Δ) | RSFT Tax (Δ) | 方向 |
210	|-------|-------------|-------------|------|
211	| Qwen3-1.7B | **+6.2pp** | **-7.7pp**⚠️ | SFT: BENEFIT（正则化）; RSFT: CONFOUNDED（59.2% truncation@1024, 2048 重跑中） |
212	| Qwen3-4B | **-7.5pp** | **+0.94pp** | SFT: cost; RSFT: near-zero（RSFT 消除 evidence 代价） |
213	| Qwen3-8B | **≈0** | **-0.78pp** | neutral（RSFT 微弱 benefit） |
214	| Qwen3-14B | **+0.03pp** | TBD (14B RSFT pipeline running) | neutral（容量完全 absorb） |
215	| LLaMA-3.1-8B | **-0.7pp** | — | near-neutral（跨家族确认） |
216	
217	### Cross-Dataset Validation（D080）
218	
219	| Dataset | Ign-F1 Δ | Evi-F1 | 说明 |
220	|---------|----------|--------|------|
221	| DocRED (in-domain) | baseline | — | — |
222	| Re-DocRED | -3.15pp | 0.817 | evidence extraction 泛化，relation extraction 有损 |
223	
224	## Anticipated Reviewer Concerns (updated from Dream, D068-D083)
225	
226	### RC1: "Online RL" 标题过度声称（Dream 三档一致 Critical）
227	- ~~标题和 claim 收窄到 "GRPO fails for DocRE"~~
228	- **D068/D069 修正**: 重新定位为 "RL optimization pressure correlates with decoupling severity"——不是 GRPO 特有问题，而是 RL-for-IE 的通用梯度
229	- DPO 数据支撑 decoupling spectrum（gradual decay confirms the pattern）
230	
231	### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）
232	- GRPO G=8 bf16 实验 ✅ — 确认 mild decoupling（-2pp），QLoRA 是 catastrophic amplifier（D065/D066）
233	- LoRA confound 已解决：bf16 LoRA vs QLoRA 直接对比
234	
235	### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）
236	- **已解决（D078）**: paired t-test p=0.44，CED 与 flat-NLI 统计不可区分
237	- **应对**: 不再声称 CED > flat-NLI；论文定位为 "NLI-based scoring 是关键（CED 和 flat-NLI 均有效），CED 因可解释性作为默认推荐"
238	- ~~5+ seeds 统计检验~~ → 不再需要，D078 已给出明确结论
239	
240	### RC4: RSFT 不新颖
241	- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR
242	- 诚实定位 RSFT 为 STaR (NeurIPS 2022) 单轮变体 + domain-specific quality filter
243	
244	### RC12: SAIS 说 evidence 有用，为何 FREIGE 说 evidence 有害？（文献审查 2026-05-16）
245	- **关键区分**: discriminative evidence *retrieval*（SAIS/DREEAM — 分类句子是否为证据，作为监督信号提升 RE）vs generative evidence *production*（FREIGE — LLM 生成完整证据文本，额外生成负担导致 scale-dependent 代价）
246	- SAIS 的 evidence supervision 是分类任务，不增加输出长度；FREIGE 的 evidence generation 显著增加生成序列长度，模型需分配容量同时完成 RE + evidence 生成
247	- **D079/D083 新弹药**: evidence tax 是 scale-dependent 的——1.7B 模型中 evidence 反而有益（+6.2pp），与 SAIS 的发现方向一致。这说明 evidence 的效果取决于模型容量和任务范式的交互，而非简单的有害/有益二分
248	- **应对**: Related Work 中精准讨论此对比，明确 FREIGE 研究的是 *generative production* 设定下的代价，与 *retrieval* 设定下的增益不矛盾——两者揭示了 evidence 在不同范式下的不同角色
249	
250	### RC13: 单模型单数据集泛化性不足（D077 scope 扩展）
251	- ~~plan_006: Qwen3-1.7B / 8B model size ablation~~ ✅ D079/D083 完成
252	- ~~plan_016: LLaMA-3.1-8B cross-family validation~~ ✅ D082 完成
253	- ~~plan_007: Re-DocRED cross-dataset evaluation~~ ✅ D080 完成
254	- **结果**: 三项泛化实验全部完成，支撑 C5 scaling pattern + cross-family + cross-dataset 叙事
255	
256	### RC5: 评测可比性 — ✅ RESOLVED (D093)
257	- **DREEAM 协议确认**: DREEAM 的 evi_f1=54.01% 等价于我们的 evi_f1_joint（FP/FN triples 计入分母）
258	- 我们最好: LLaMA-8B RSFT evi_f1_joint=45.71%（差 8.3pp，主要由 RE gap 6.8pp 驱动）
259	- TP-only evi_f1=82.55% 证明正确预测 triple 的 evidence 质量优秀
260	- **论文必须**: (1) 用 evi_f1_joint 对比 DREEAM (2) 同时报 TP-only 证明 evidence 质量高 (3) 标明版本避免混淆
261	- **Framing**: generative LLM 首次做 evidence-grounded DocRE vs encoder-based 专用模型，差距主要来自 RE 而非 evidence
262	
263	### RC6: EDCR 缺人工验证
264	- 100 例小规模标注
265	
266	### RC7: Missing DPO/PPO（Dream 两档 Major）
267	- DPO experiment ✅ — 结果确认 decoupling spectrum（D067/D068）
268	
269	### RC8: Dev-test degradation
270	- 观察项，等 test set 数据
271	
272	### RC9: 连接 reward overoptimization 文献
273	- 显式引用 Gao et al. 2023
274	
275	### RC10: Post-hoc evidence retrieval baseline — ✅ RESOLVED (D091)
276	- BM25 entity_only k=2: evi_f1_joint=0.347, EDCR=0.766 → 弱于 RSFT joint generation (0.361, EDCR=0.654)
277	- Oracle_k (=GT k): evi_f1_joint=0.383 略胜 RSFT，但 EDCR 仍差 7.9pp 且不实用
278	- 防御策略：指出 joint generation 的 evidence 更 faithful（EDCR 低 11pp），且一次推理完成无需额外检索管线
279	- NLI retrieval 变体降为 rebuttal 备用
280	
281	### RC11: "RL 不遗忘" 文献与 Claim 2 的张力（文献扫描 2026-05-16）
282	- 近期多篇论文（arXiv 2507.05386, 2506.23508, 2509.04259）论证 RL fine-tuning 天然缓解 catastrophic forgetting
283	- **关键区分**: FREIGE 的 decoupling 是 **intra-task multi-objective trade-off**（RE 抽取 vs evidence 生成两个优化目标的竞争），不是 **inter-task forgetting**（丢失预训练知识）。两者机制不同
284	- bf16 GRPO 的 mild decoupling（-2pp）恰好印证这一点：模型没有忘记"怎么做 IE"，而是在 evidence reward 压力下偏移了 RE-evidence 的资源分配
285	- **应对**: Related Work / Discussion 中显式回应这组文献，区分 intra-task trade-off vs inter-task forgetting
286	- **QuRL/QaRL 文献支撑 Claim 2**: QuRL 发现 quantized vs full-precision actor divergence 在长训练中指数增长（直接支撑 QLoRA amplification 叙事）；QaRL 的 error token failure mode 与 QLoRA GRPO garbled evidence 吻合
287	
288	## Key Baselines (12+)
289	
290	1. **SFT-only**: Qwen3-4B + LoRA SFT（with evidence）
291	1b. **SFT no-evidence**: Qwen3-4B + LoRA SFT（无 evidence，upper bound ablation）
292	2. **RSFT flat-NLI**: flat-NLI scored RSFT（核心 ablation）
293	3. **RSFT CED**: CED scored RSFT（主方法）
294	4. **CED-as-reranker**: 推理时 CED 重排（无训练）
295	5. **DPO+CED**: offline preference learning — gradual decoupling（D067/D068）
296	6. **GRPO+CED (QLoRA, G=4)**: catastrophic decoupling baseline
297	7. **GRPO+CED (bf16, G=8)**: mild decoupling — QLoRA confound 排除（D065/D066）
298	8. **Post-hoc retrieval**: SFT + BM25 evidence（NEW）
299	9. **DREEAM**: encoder evidence SOTA
300	10. **SAIS**: encoder evidence baseline
301	11. **DocKS-RAG**: extraction SOTA（无 evidence）
302	12. **LMRC**: generative LLM SOTA（无 evidence）
303	
304	## Publishability Threshold (revised after D078-D083)
305	
306	- **必要条件**: (1) RSFT 在 test set 上 Ign-F1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) Decoupling spectrum 有完整数据支撑（GRPO QLoRA/bf16 + DPO + RSFT）
307	- **充分条件**: 上述 + EDCR 人工验证 + scaling pattern (C5) 完整
308	- **已达成**: CED vs flat-NLI 统计检验完成（D078: 不可区分，不再是充分条件要素）; 泛化实验完成（D079/D080/D082/D083）
309	- **Failure pivot**: decoupling spectrum 不成立（bf16 GRPO 也 catastrophic）→ scope 大幅缩减。**已排除**: bf16 GRPO 确认 mild（D065/D066）
310	
311	## Research Phase Priorities (revised after D078-D083)
312	
313	| Priority | 实验 | Claim | GPU-h |
314	|----------|------|-------|-------|
315	| ~~P0~~ | ~~flat-NLI RSFT ablation (5 seeds)~~ → D078 已结论 | C3 | — |
316	| ~~P0~~ | ~~CED RSFT additional seeds (→5 total)~~ → D078 已结论 | C3 | — |
317	| P0 | DREEAM-protocol Evi-F1 对齐 | C1 | CPU |
318	| P0 | Test set evaluation | C1 | ~4h |
319	| P0 | DREEAM baseline reproduction | C1 | ~8h |
320	| ~~P0~~ | ~~GRPO G=8 experiment~~ ✅ | C2 | ~16h |
321	| ~~P0~~ | ~~DPO+CED experiment~~ ✅ | C2 | ~12h |
322	| ~~P0~~ | ~~EDCR per-relation analysis (D070)~~ ✅ | C4 | CPU |
323	| ~~P0~~ | ~~Ign-F1 bugfix + data sync (D071)~~ ✅ | ALL | CPU |
324	| ~~P0~~ | ~~Model size ablation (1.7B/8B)~~ ✅ D079/D083 | C5 | — |
325	| ~~P0~~ | ~~LLaMA-3.1-8B cross-family~~ ✅ D082 | C5 | — |
326	| ~~P0~~ | ~~Re-DocRED cross-dataset~~ ✅ D080 | C1/C5 | — |
327	| P1 | EDCR human validation | C4 | API |
328	| P1 | Post-hoc evidence retrieval baseline | C1 | ~4h |
329	| P1 | CED-as-reranker (running) | C1 | ~6h |
330	| ~~P0~~ | ~~GRPO forgetting dynamics figure (plan_009)~~ ✅ | C2 | ~2h |
331	| ~~P0~~ | ~~SFT-without-evidence ablation (plan_014)~~ ✅ | C1 | ~8h |
332	| P2 | Advantage variance measurement | C2 | CPU |
333	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58f2c7f8-15ea-41bc-8944-4afb99e6475b",
  "isSidechain": true,
  "promptId": "a52d2a02-5bc0-4012-8f39-29957ce260bc",
  "agentId": "a5e7ddcdb00ffae00",
  "type": "user",
  "uuid": "b1c86b49-005b-4479-883c-44b2fc734139",
  "sourceToolAssistantUUID": "58f2c7f8-15ea-41bc-8944-4afb99e6475b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-19T18:24:49.226Z_

Perfect! I have the file. Now let me extract the specific sections you requested:

## Extracted Information from paper_framing.md

### 1. **Full Text of Claim 5 (about scaling/evidence tax)**

**Claim 5 (NEW — Scaling): Evidence Tax 呈 Non-Monotonic Scaling Pattern（D079/D082/D083）**

**核心发现**: evidence generation 的代价不是固定的——它与模型容量呈非线性关系
- **1.7B (Qwen3-1.7B)**: +6.2pp BENEFIT — evidence generation 起隐式正则化作用，防止小模型过拟合（D083 公平子集分析确认）
- **4B (Qwen3-4B)**: -7.47pp cost (D076: evi 39.74% / no-evi 47.21%) — 标准 evidence generation 负担，模型容量不足以同时优化两个目标
- **8B Qwen (Qwen3-8B)**: ≈0 — 模型容量足够 absorb evidence generation 的额外负担
- **8B LLaMA (LLaMA-3.1-8B)**: -0.7pp — 跨家族确认，8B 规模的 evidence tax 趋近于零

**Non-monotonic 解释**: 小模型从 evidence 的正则化效应获益 > 生成负担；中等模型容量不足以同时做好两件事；大模型容量充裕，两个目标互不干扰

**Mechanistic analysis (plan_020 完成)**：3 层机制解释 scale-dependent tax：
- **(1) Duplication regularization（主因）**: monotonic decline — 1.7B 27.5pp gap (60.5%→33.0%), 4B 12.1pp gap (43.2%→31.1%), 8B 3.7pp gap (32.9%→29.2%)。正则化效应随容量增大递减
- **(2) Truncation asymmetry**: 1.7B Δ=19pp (no-evi worse), 4B Δ=2pp (neutral), 8B Δ=-9pp (evi worse, tokens 消耗输出预算)
- **(3) Fair comparison residual**: 排除截断后（442/985 docs），1.7B evidence 仍 +6.2pp (ign_f1)，8B Qwen -0.3pp，8B LLaMA +0.3pp — 证明 1.7B 有真实 reasoning scaffold 效应

**4B "capacity valley" 确认**: duplication 已低(31.1%，接近 8B 29.2%)不需正则化，truncation 中性(29.2% vs 31.2%)，但容量不足同时做 RE + evidence generation → 纯开销(+7.47pp tax, D076 protocol)

**论文叙事**: "Evidence as implicit regularization" — 推翻 "evidence 总有代价" 的简单叙事。60.5%→33.0% duplication rate 是最有冲击力的数据点。建议 4 张图（duplication rate / truncation crossover / fair comparison / doc complexity）

**Cross-family robustness**: LLaMA-8B 与 Qwen-8B 一致确认 8B 规模 evidence tax ≈ 0

---

### 2. **Sections about "variance compression" as a core finding**

Found in Claim 5 (lines 140-141):

**Variance Compression 为核心发现 (D118)**: RSFT 跨 3 个尺度一致性地压缩 seed 方差——1.7B **31×** (2.79pp→0.09pp), 4B **7.5×** (3.80pp→0.51pp), 8B **7.4×** (3.72pp→0.50pp)。这不仅是副产品而是 CED filtering 的本质效应：质量过滤消除了 seed-dependent 的训练噪声

Also referenced in the document header (line 4):
> **最后更新**: 2026-05-19 (D117-D120: 14B tax=0, surpasses→approaches, D112 Method B=0.5152, **8B RSFT 3v3 variance 7.4×**)

---

### 3. **Updated numbers for "1.7B RSFT vs 8B SFT" comparison**

Found in Claim 5 (lines 140-141):

**RSFT 弥合 scale gap (D094→D102→D118)**: 1.7B RSFT 3-seed mean=**0.5119** (std=0.09pp) vs 8B SFT 3-seed mean=**0.5019** (std=3.72pp)，Δ=+1.0pp, p=0.69 不显著——CED-RSFT 使 1.7B 模型**接近** 4.7× 大的 8B SFT，但差异在统计噪声内。"surpasses" claim 被 D118 否定（8B SFT s43=0.5324 拉高均值），回退为 "approaches"

Also in the D076 scaling table (lines 196-202):
- Qwen3-1.7B RSFT k=1 s42: **0.5290** (+3.5pp)
- Qwen3-8B SFT: **0.5262**
- Qwen3-8B RSFT k=1 mean: **0.5600** (+3.4pp)

The narrative guidance: Use "approaches" rather than "surpasses" when comparing 1.7B RSFT to 8B SFT due to high variance and statistical non-significance.

---

### 4. **Guidance about D112 Method B**

Found in Claim 5 (line 144):

**D112 Method B (full pipeline from s44 SFT)**: 4B RSFT bf16 ign_f1=**0.5152** (+4.18pp over SFT s44=0.4734)——确认 RSFT 不依赖特定 SFT seed，pipeline 可复现

This confirms that the RSFT pipeline is reproducible and doesn't depend on a specific SFT seed checkpoint. The Method B variant achieves ign_f1=0.5152 when trained from s44, demonstrating +4.18pp improvement over that baseline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1c86b49-005b-4479-883c-44b2fc734139",
  "isSidechain": true,
  "agentId": "a5e7ddcdb00ffae00",
  "requestId": "req_011CbCPuJrapKwXSgLqzVC1x",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "12ceda0c-a692-42d1-baa4-e03a6df616a7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/paper_agent_ae93019b",
  "sessionId": "519710f0-eea4-43f5-b902-4617530dfbfa",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "purring-shimmying-sutton",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MmzcKm5wH67CG2hEMx21vT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 13526,
      "cache_read_input_tokens": 27199,
      "output_tokens": 1708,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13526
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1708,
          "cache_read_input_tokens": 27199,
          "cache_creation_input_tokens": 13526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13526,
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
