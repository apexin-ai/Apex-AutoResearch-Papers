# Research conversation: <project_context> # 项目: ec_hte_llm_annotation ## 运行环境 - 服务器名: local-cpu - SSH 账户: ubuntu（调用 ssh_execute / submit_trainin

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/f105112c-0ede-4aff-9056-e21c0cb102f8.jsonl`
- **Structured JSON:** [`45fabd5e82508c182186.json`](../../sessions/45/45fabd5e82508c182186.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T00:14:58.686Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T00:14:58.686Z",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "content": "&lt;project_context>\n# 项目: ec_hte_llm_annotation\n\n## 运行环境\n- 服务器名: local-cpu\n- SSH 账户: ubuntu（调用 ssh_execute / submit_training_job 时传入 account=\"ubuntu\"）\n- SSH 连接命令: ssh local-cpu  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /home/ubuntu/ec_hte_llm_annotation\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：Mistral-7B heterogeneous-τ DGP 实验\n\n### 目标\n用 Mistral-7B-v0.3 的真实 per-subgroup confusion matrix 跑 heterogeneous-τ DGP 半合成实验。\n\n### 步骤\n\n1. **读取模板脚本**：\n   读 `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_qwen_hetero_tau.py` 作为模板。\n\n2. **创建 Mistral 版本**：\n   创建 `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_mistral_hetero_tau.py`\n   \n   **只替换 CM 参数为 Mistral 的值**，其余逻辑完全不变：\n\n   Mistral-7B Per-Subgroup Confusion Matrix (K=4, balanced Z):\n   | Subgroup | Weight | FPR | FNR | pi_s |\n   |----------|--------|------|------|------|\n   | False_medium | 0.3816 | 0.1800 | 0.2989 | 0.2394 |\n   | False_short | 0.2224 | 0.2414 | 0.1875 | 0.2144 |\n   | True_medium | 0.2551 | 0.2333 | 0.1684 | 0.2009 |\n   | True_short | 0.1408 | 0.0909 | 0.1207 | 0.1058 |\n\n   注意：Mistral 的 CM 与 Llama 非常接近，但 True_short FNR 更低（0.121 vs 0.190）。\n\n3. **DGP 参数（完全不变）**：\n   - N=5000, P(Z=1)=0.652, K=4 subgroups\n   - Heterogeneous τ: False_medium Δτ=0.1, False_short Δτ=0.1, True_medium Δτ=0.3, True_short Δτ=0.6\n   - n_expert ∈ {200, 500, 1000}, 50 MC seeds\n   - Methods: Naive, Global, Strat MLE, HB EC-HTE (MAP-EB Gamma(3,1))\n\n4. **Bias 指标必须用正确公式**：\n   - |Bias| = avg across cells of |mean(bias) across seeds|（先 seed 维度求 mean，再取绝对值）\n   - **不是** mean(|bias_per_seed|)\n\n5. **运行脚本**，输出到：\n   - CSV: `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/mistral_hetero_tau_results.csv`\n   - 分析: `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/mistral_hetero_tau_analysis.md`\n\n6. **分析报告格式**（参考 qwen_hetero_tau_analysis.md）：\n   - Design section (含 Mistral CM table)\n   - Summary table: n_expert × Method × |Bias| × RMSE × Coverage × CI Width\n   - EC-HTE vs Global comparison table\n   - Per-subgroup breakdown (每个 n_expert)\n   - Bias-variance decomposition\n   - Cross-model comparison: 与 Llama (exp-023 hetero_tau_analysis.md) 对比\n   - 结论\n\n### 环境\n- 本地 CPU，Python 3，numpy/scipy 已安装\n- 预计 10-20 分钟\n\n### 验证\n- CSV 行数应为 50 × 3 × 4 × 8 = 4800 数据行 + 1 header = 4801 行"
}
```

---

### Runtime record

_source line 2 · 2026-05-22T00:14:58.690Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T00:14:58.690Z",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8"
}
```

---

## Round 1

37 recorded events

### User

_source line 3 · 2026-05-22T00:14:58.728Z_

&lt;project_context>
# 项目: ec_hte_llm_annotation

## 运行环境
- 服务器名: local-cpu
- SSH 账户: ubuntu（调用 ssh_execute / submit_training_job 时传入 account="ubuntu"）
- SSH 连接命令: ssh local-cpu  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /home/ubuntu/ec_hte_llm_annotation


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：Mistral-7B heterogeneous-τ DGP 实验

### 目标
用 Mistral-7B-v0.3 的真实 per-subgroup confusion matrix 跑 heterogeneous-τ DGP 半合成实验。

### 步骤

1. **读取模板脚本**：
   读 `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_qwen_hetero_tau.py` 作为模板。

2. **创建 Mistral 版本**：
   创建 `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_mistral_hetero_tau.py`
   
   **只替换 CM 参数为 Mistral 的值**，其余逻辑完全不变：

   Mistral-7B Per-Subgroup Confusion Matrix (K=4, balanced Z):
   | Subgroup | Weight | FPR | FNR | pi_s |
   |----------|--------|------|------|------|
   | False_medium | 0.3816 | 0.1800 | 0.2989 | 0.2394 |
   | False_short | 0.2224 | 0.2414 | 0.1875 | 0.2144 |
   | True_medium | 0.2551 | 0.2333 | 0.1684 | 0.2009 |
   | True_short | 0.1408 | 0.0909 | 0.1207 | 0.1058 |

   注意：Mistral 的 CM 与 Llama 非常接近，但 True_short FNR 更低（0.121 vs 0.190）。

3. **DGP 参数（完全不变）**：
   - N=5000, P(Z=1)=0.652, K=4 subgroups
   - Heterogeneous τ: False_medium Δτ=0.1, False_short Δτ=0.1, True_medium Δτ=0.3, True_short Δτ=0.6
   - n_expert ∈ {200, 500, 1000}, 50 MC seeds
   - Methods: Naive, Global, Strat MLE, HB EC-HTE (MAP-EB Gamma(3,1))

4. **Bias 指标必须用正确公式**：
   - |Bias| = avg across cells of |mean(bias) across seeds|（先 seed 维度求 mean，再取绝对值）
   - **不是** mean(|bias_per_seed|)

5. **运行脚本**，输出到：
   - CSV: `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/mistral_hetero_tau_results.csv`
   - 分析: `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/mistral_hetero_tau_analysis.md`

6. **分析报告格式**（参考 qwen_hetero_tau_analysis.md）：
   - Design section (含 Mistral CM table)
   - Summary table: n_expert × Method × |Bias| × RMSE × Coverage × CI Width
   - EC-HTE vs Global comparison table
   - Per-subgroup breakdown (每个 n_expert)
   - Bias-variance decomposition
   - Cross-model comparison: 与 Llama (exp-023 hetero_tau_analysis.md) 对比
   - 结论

### 环境
- 本地 CPU，Python 3，numpy/scipy 已安装
- 预计 10-20 分钟

### 验证
- CSV 行数应为 50 × 3 × 4 × 8 = 4800 数据行 + 1 header = 4801 行

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "695fc122-00c0-4b11-823d-9471ae018801",
  "type": "user",
  "uuid": "a03f7b7e-7b4e-43fd-8c67-4b4e16e2a3f7",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T00:14:58.727Z_

```json
{
  "parentUuid": "a03f7b7e-7b4e-43fd-8c67-4b4e16e2a3f7",
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "0cba0029-92f4-473e-b4a0-e91ffa62c5f2",
  "timestamp": "2026-05-22T00:14:58.727Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T00:14:58.727Z_

```json
{
  "parentUuid": "0cba0029-92f4-473e-b4a0-e91ffa62c5f2",
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
  "uuid": "51a94f25-e36c-474e-8349-e8dc7257a0df",
  "timestamp": "2026-05-22T00:14:58.727Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T00:14:58.727Z_

```json
{
  "parentUuid": "51a94f25-e36c-474e-8349-e8dc7257a0df",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3dbbccbd-97d9-46cf-a456-b20e28a8000b",
  "timestamp": "2026-05-22T00:14:58.727Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Mistral-7B heterogeneous-τ DGP experiment",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8"
}
```

---

### Assistant

_source line 8 · 2026-05-22T00:15:00.587Z_

I'll start by reading the template script to understand the structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dbbccbd-97d9-46cf-a456-b20e28a8000b",
  "isSidechain": false,
  "requestId": "req_011CbGeFWxZGei7AZoT1vmmG",
  "type": "assistant",
  "uuid": "69e517a2-3b09-4689-be19-d687fb86d6e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArNXTdiG16MkgRzjzSR3Yk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6556,
      "cache_read_input_tokens": 11841,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6556,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 6556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6556
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

_source line 9 · 2026-05-22T00:15:01.046Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R2TwEXiUdVr3eq7BTGZMPr`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_qwen_hetero_tau.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69e517a2-3b09-4689-be19-d687fb86d6e0",
  "isSidechain": false,
  "requestId": "req_011CbGeFWxZGei7AZoT1vmmG",
  "type": "assistant",
  "uuid": "9021316a-af65-4464-b4f5-1da8c5dce568",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArNXTdiG16MkgRzjzSR3Yk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6556,
      "cache_read_input_tokens": 11841,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6556,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 103,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 6556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6556
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

_source line 10 · 2026-05-22T00:15:01.328Z_

<details><summary>↩ Tool result · `toolu_01R2TwEXiUdVr3eq7BTGZMPr`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Heterogeneous-τ DGP experiment with Qwen2.5-7B confusion matrices.
4	Mirrors run_hetero_tau.py (Llama) but uses Qwen per-subgroup FPR/FNR.
5	"""
6	
7	import time
8	import warnings
9	import numpy as np
10	import pandas as pd
11	from scipy.optimize import minimize_scalar
12	from scipy.special import gammaln
13	
14	warnings.filterwarnings('ignore')
15	
16	# === Config ===
17	
18	N = 5000
19	N_EXPERT_LIST = [200, 500, 1000]
20	N_MC = 50
21	SEED_BASE = 0
22	
23	SUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']
24	SUBGROUP_WEIGHTS = np.array([0.3816, 0.2224, 0.2551, 0.1408])
25	SUBGROUP_WEIGHTS = SUBGROUP_WEIGHTS / SUBGROUP_WEIGHTS.sum()
26	
27	SUBGROUP_CM = {
28	    'False_medium': {'fpr': 0.1800, 'fnr': 0.2874},
29	    'False_short':  {'fpr': 0.2414, 'fnr': 0.1750},
30	    'True_medium':  {'fpr': 0.2333, 'fnr': 0.2105},
31	    'True_short':   {'fpr': 0.0000, 'fnr': 0.1379},
32	}
33	
34	SUBGROUP_TAU = {
35	    'True_short':   {'tau_z0': 0.2,  'tau_z1': 0.8},
36	    'True_medium':  {'tau_z0': 0.35, 'tau_z1': 0.65},
37	    'False_short':  {'tau_z0': 0.4,  'tau_z1': 0.5},
38	    'False_medium': {'tau_z0': 0.45, 'tau_z1': 0.55},
39	}
40	
41	P_Z1 = 0.652
42	P_T1 = 0.5
43	
44	
45	def get_cm_matrix(fpr, fnr):
46	    return np.array([[1 - fpr, fpr],
47	                     [fnr, 1 - fnr]])
48	
49	
50	# === Estimators ===
51	
52	def diff_in_means(Y, T, mask):
53	    t1 = mask & (T == 1)
54	    t0 = mask & (T == 0)
55	    n1, n0 = t1.sum(), t0.sum()
56	    if n1 < 2 or n0 < 2:
57	        return np.nan, np.nan
58	    y1, y0 = Y[t1], Y[t0]
59	    tau_hat = y1.mean() - y0.mean()
60	    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
61	    return tau_hat, se
62	
63	
64	def estimate_confusion_matrix(z_true, z_hat):
65	    C = np.zeros((2, 2))
66	    for zt in [0, 1]:
67	        mask = z_true == zt
68	        n = mask.sum()
69	        for zh in [0, 1]:
70	            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
71	    return C
72	
73	
74	def estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):
75	    C = {}
76	    for s in labels:
77	        ms = subgroups == s
78	        C_s = np.zeros((2, 2))
79	        for zt in [0, 1]:
80	            mask = ms & (z_true == zt)
81	            n = mask.sum()
82	            for zh in [0, 1]:
83	                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
84	        C[s] = C_s
85	    return C
86	
87	
88	def build_mixing_matrix(C, p_z, p_z_hat):
89	    M = np.zeros((2, 2))
90	    for zh in [0, 1]:
91	        for z in [0, 1]:
92	            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5
93	    return M
94	
95	
96	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
97	    cond = np.linalg.cond(M)
98	    if cond > cond_threshold:
99	        return tau_obs.copy(), se_obs.copy()
100	    det = np.linalg.det(M)
101	    if abs(det) < 1e-10:
102	        return tau_obs.copy(), se_obs.copy()
103	    Mi = np.linalg.inv(M)
104	    tau_c = Mi @ tau_obs
105	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
106	    return tau_c, se_c
107	
108	
109	# === MAP-EB ===
110	
111	def _dirmult_neg_ll(alpha, counts_z):
112	    a = alpha / 2.0
113	    if a < 1e-10:
114	        return 1e10
115	    ll = 0.0
116	    for c0, c1 in counts_z:
117	        n = c0 + c1
118	        if n == 0:
119	            continue
120	        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)
121	        ll -= 2 * gammaln(a) - gammaln(2 * a)
122	    return -ll
123	
124	
125	def estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):
126	    hp_rate = 1.0 / hp_scale
127	    k = len(labels)
128	    alpha_opt = np.zeros(2)
129	
130	    for z in [0, 1]:
131	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
132	        total = sum(c0 + c1 for c0, c1 in cl)
133	        if total == 0:
134	            alpha_opt[z] = hp_shape * hp_scale
135	            continue
136	
137	        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):
138	            nll = _dirmult_neg_ll(a, _cl)
139	            if a < 1e-10:
140	                return 1e10
141	            log_prior = (_shape - 1.0) * np.log(a) - _rate * a
142	            return nll - log_prior
143	
144	        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')
145	        alpha_opt[z] = res.x
146	
147	    C = {}
148	    for i, s in enumerate(labels):
149	        C_s = np.zeros((2, 2))
150	        for z in [0, 1]:
151	            a = alpha_opt[z] / 2.0
152	            n_sz = counts[i, z, :].sum()
153	            d = n_sz + 2 * a
154	            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5
155	            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5
156	        C[s] = C_s
157	
158	    return C, alpha_opt
159	
160	
161	def get_counts(z_true, z_hat, subgroups, labels):
162	    k = len(labels)
163	    counts = np.zeros((k, 2, 2), dtype=int)
164	    for i, s in enumerate(labels):
165	        ms = subgroups == s
166	        for z in [0, 1]:
167	            mz = ms & (z_true == z)
168	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
169	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
170	    return counts
171	
172	
173	# === DGP (heterogeneous tau) ===
174	
175	def generate_data(seed, n_expert):
176	    rng = np.random.RandomState(seed)
177	
178	    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)
179	    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])
180	
181	    Z = rng.binomial(1, P_Z1, N)
182	    T = rng.binomial(1, P_T1, N)
183	
184	    Z_hat = np.empty(N, dtype=int)
185	    for i in range(4):
186	        s_mask = S_idx == i
187	        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],
188	                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])
189	        z_s = Z[s_mask]
190	        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])
191	        Z_hat[s_mask] = rng.binomial(1, p_obs1)
192	
193	    tau_vals = np.zeros(N)
194	    for i, s in enumerate(SUBGROUP_LABELS):
195	        s_mask = S_idx == i
196	        tau_s = SUBGROUP_TAU[s]
197	        tau_vals[s_mask] = np.where(Z[s_mask] == 1, tau_s['tau_z1'], tau_s['tau_z0'])
198	
199	    eps = rng.randn(N)
200	    Y = 1.0 + tau_vals * T + eps
201	
202	    expert_idx = rng.choice(N, n_expert, replace=False)
203	    expert_mask = np.zeros(N, dtype=bool)
204	    expert_mask[expert_idx] = True
205	
206	    return {
207	        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,
208	        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,
209	    }
210	
211	
212	# === MC Runner ===
213	
214	def run_one_mc(data, seed):
215	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
216	    expert_mask = data['expert_mask']
217	
218	    z_exp = Z[expert_mask]
219	    zh_exp = Z_hat[expert_mask]
220	    s_exp = S[expert_mask]
221	
222	    C_global = estimate_confusion_matrix(z_exp, zh_exp)
223	    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])
224	    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])
225	    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)
226	
227	    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)
228	
229	    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)
230	    C_hb, _ = estimate_cm_hb_map_eb(counts, SUBGROUP_LABELS)
231	
232	    M_mle_sub = {}
233	    M_hb_sub = {}
234	    for s_val in SUBGROUP_LABELS:
235	        sm_exp = (s_exp == s_val)
236	        sm_all = (S == s_val)
237	        if sm_exp.sum() >= 4:
238	            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])
239	        else:
240	            p_z_s = p_z_global
241	        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])
242	        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)
243	        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)
244	
245	    rows = []
246	
247	    for s_val in SUBGROUP_LABELS:
248	        s_mask = S == s_val
249	        tau_s = SUBGROUP_TAU[s_val]
250	
251	        for z_level in [0, 1]:
252	            oracle_cate = tau_s['tau_z1'] if z_level == 1 else tau_s['tau_z0']
253	
254	            # Naive
255	            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))
256	            ci_w_nv = 2 * 1.96 * se_nv if not np.isnan(se_nv) else np.nan
257	            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan
258	            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan
259	            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0
260	            rows.append({
261	                'seed': seed, 'method': 'naive', 'subgroup': s_val,
262	                'z_level': z_level,
263	                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,
264	                'cate_est': th_nv, 'cate_true': oracle_cate,
265	                'coverage': cov_nv, 'ci_width': ci_w_nv,
266	            })
267	
268	            # Observed CATE in Z_hat=0 and Z_hat=1 cells
269	            tau_obs = np.array([
270	                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],
271	                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],
272	            ])
273	            se_obs = np.array([
274	                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],
275	                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],
276	            ])
277	
278	            if not np.any(np.isnan(tau_obs)):
279	                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)
280	                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]
281	
282	                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)
283	                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]
284	
285	                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)
286	                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]
287	            else:
288	                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan
289	
290	            # Global corrected
291	            ci_w_gc = 2 * 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan
292	            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan
293	            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan
294	            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0
295	            rows.append({
296	                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,
297	                'z_level': z_level,
298	                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,
299	                'cate_est': th_gc, 'cate_true': oracle_cate,
300	                'coverage': cov_gc, 'ci_width': ci_w_gc,
301	            })
302	
303	            # Stratified MLE
304	            ci_w_ml = 2 * 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan
305	            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan
306	            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan
307	            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0
308	            rows.append({
309	                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,
310	                'z_level': z_level,
311	                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,
312	                'cate_est': th_ml, 'cate_true': oracle_cate,
313	                'coverage': cov_ml, 'ci_width': ci_w_ml,
314	            })
315	
316	            # HB EC-HTE (MAP-EB)
317	            ci_w_hb = 2 * 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan
318	            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan
319	            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan
320	            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0
321	            rows.append({
322	                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,
323	                'z_level': z_level,
324	                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,
325	                'cate_est': th_hb, 'cate_true': oracle_cate,
326	                'coverage': cov_hb, 'ci_width': ci_w_hb,
327	            })
328	
329	    return rows
330	
331	
332	# === Aggregation ===
333	
334	def compute_corrected_abs_bias(df):
335	    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']
336	                 .mean().abs().reset_index(name='abs_mean_bias'))
337	    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']
338	            .mean().reset_index(name='abs_bias'))
339	
340	
341	def compute_rmse(df):
342	    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)
343	                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']
344	                 .mean().apply(np.sqrt).reset_index(name='rmse'))
345	    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']
346	            .mean().reset_index(name='rmse'))
347	
348	
349	def compute_coverage(df):
350	    return (df.groupby(['n_expert', 'method'])['coverage']
351	            .mean().reset_index(name='coverage'))
352	
353	
354	def compute_ci_width(df):
355	    return (df.groupby(['n_expert', 'method'])['ci_width']
356	            .mean().reset_index(name='ci_width'))
357	
358	
359	# === Analysis Report ===
360	
361	LLAMA_RESULTS = {
362	    200:  {'global_bias': 0.0365, 'echte_bias': 0.0248, 'global_rmse': 0.1780, 'echte_rmse': 0.2606},
363	    500:  {'global_bias': 0.0314, 'echte_bias': 0.0099, 'global_rmse': 0.1580, 'echte_rmse': 0.1760},
364	    1000: {'global_bias': 0.0286, 'echte_bias': 0.0130, 'global_rmse': 0.1554, 'echte_rmse': 0.1602},
365	}
366	
367	LLAMA_CM = {
368	    'False_medium': {'fpr': 0.235, 'fnr': 0.319},
369	    'False_short':  {'fpr': 0.310, 'fnr': 0.212},
370	    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},
371	    'True_short':   {'fpr': 0.091, 'fnr': 0.190},
372	}
373	
374	
375	def write_analysis(df_raw, outpath):
376	    abs_bias = compute_corrected_abs_bias(df_raw)
377	    rmse = compute_rmse(df_raw)
378	    cov = compute_coverage(df_raw)
379	    ciw = compute_ci_width(df_raw)
380	
381	    summary = abs_bias.merge(rmse, on=['n_expert', 'method']).merge(
382	        cov, on=['n_expert', 'method']).merge(ciw, on=['n_expert', 'method'])
383	
384	    lines = []
385	    lines.append("# Qwen2.5-7B Heterogeneous-τ DGP: EC-HTE vs Global Correction\n")
386	    lines.append("## Design\n")
387	    lines.append(f"- N={N}, P(Z=1)={P_Z1}, K=4 subgroups")
388	    lines.append("- **LLM**: Qwen2.5-7B (balanced binarization)")
389	    lines.append("- **Heterogeneous τ(z) across subgroups:**")
390	    for s in SUBGROUP_LABELS:
391	        t = SUBGROUP_TAU[s]
392	        lines.append(f"  - {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}")
393	    lines.append(f"- n_expert sweep: {N_EXPERT_LIST}")
394	    lines.append(f"- {N_MC} MC seeds per budget")
395	    lines.append("- HB method: MAP-EB (Gamma(3,1) prior)")
396	    lines.append(f"- |Bias| = avg across cells of |mean(bias) across seeds|")
397	    lines.append(f"- RMSE = avg across cells of sqrt(mean(bias²) across seeds)")
398	    lines.append("")
399	
400	    # Qwen CM table
401	    lines.append("## Qwen2.5-7B Per-Subgroup Confusion Matrix\n")
402	    lines.append("| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |")
403	    lines.append("|----------|-----|-----|-----|-----------|")
404	    for s in SUBGROUP_LABELS:
405	        cm = SUBGROUP_CM[s]
406	        w = SUBGROUP_WEIGHTS[SUBGROUP_LABELS.index(s)]
407	        lines.append(f"| {s} | {w:.4f} | {cm['fpr']:.4f} | {cm['fnr']:.4f} | {1-cm['fpr']-cm['fnr']:.4f} |")
408	    lines.append("")
409	    qwen_fpr_range = max(cm['fpr'] for cm in SUBGROUP_CM.values()) - min(cm['fpr'] for cm in SUBGROUP_CM.values())
410	    qwen_fnr_range = max(cm['fnr'] for cm in SUBGROUP_CM.values()) - min(cm['fnr'] for cm in SUBGROUP_CM.values())
411	    llama_fpr_range = max(cm['fpr'] for cm in LLAMA_CM.values()) - min(cm['fpr'] for cm in LLAMA_CM.values())
412	    llama_fnr_range = max(cm['fnr'] for cm in LLAMA_CM.values()) - min(cm['fnr'] for cm in LLAMA_CM.values())
413	    lines.append(f"- Qwen Δ_FPR = {qwen_fpr_range:.4f}, Δ_FNR = {qwen_fnr_range:.4f}")
414	    lines.append(f"- Llama Δ_FPR = {llama_fpr_range:.4f}, Δ_FNR = {llama_fnr_range:.4f}")
415	    lines.append(f"- Qwen has {'larger' if qwen_fpr_range > llama_fpr_range else 'smaller'} FPR heterogeneity "
416	                 f"and {'larger' if qwen_fnr_range > llama_fnr_range else 'smaller'} FNR heterogeneity than Llama")
417	    lines.append("")
418	
419	    # Summary table
420	    lines.append("## Summary Table (averaged across all cells)\n")
421	    lines.append("| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |")
422	    lines.append("|----------|--------|-------|------|----------|----------|")
423	
424	    method_order = ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']
425	    method_labels = {'naive': 'Naive', 'global_corrected': 'Global', 'stratified_mle': 'Strat MLE', 'hb_ec_hte': 'HB EC-HTE'}
426	
427	    for ne in N_EXPERT_LIST:
428	        for m in method_order:
429	            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]
430	            if len(row) > 0:
431	                r = row.iloc[0]
432	                lines.append(f"| {ne} | {method_labels[m]} | {r['abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} | {r['ci_width']:.3f} |")
433	        lines.append("|----------|--------|-------|------|----------|----------|")
434	    lines.append("")
435	
436	    # EC-HTE vs Global comparison
437	    lines.append("## EC-HTE vs Global Comparison\n")
438	    lines.append("| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |")
439	    lines.append("|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|")
440	    for ne in N_EXPERT_LIST:
441	        sub = summary[summary['n_expert'] == ne]
442	        gc = sub[sub['method'] == 'global_corrected'].iloc[0]
443	        hb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]
444	        d_bias = gc['abs_bias'] - hb['abs_bias']
445	        d_rmse = gc['rmse'] - hb['rmse']
446	        wb = "**YES**" if hb['abs_bias'] < gc['abs_bias'] else "no"
447	        wr = "**YES**" if hb['rmse'] < gc['rmse'] else "no"
448	        lines.append(f"| {ne} | {gc['abs_bias']:.4f} | {hb['abs_bias']:.4f} | {d_bias:+.4f} | {gc['rmse']:.4f} | {hb['rmse']:.4f} | {d_rmse:+.4f} | {wb} | {wr} |")
449	    lines.append("")
450	
451	    # Per-subgroup breakdown
452	    lines.append("## Per-Subgroup Breakdown\n")
453	    for ne in N_EXPERT_LIST:
454	        lines.append(f"### n_expert = {ne}\n")
455	        lines.append("| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |")
456	        lines.append("|----------|-----|---|-------------|-------------|-------------|-------------|------------|")
457	        sub_df = df_raw[df_raw['n_expert'] == ne]
458	        for s_val in SUBGROUP_LABELS:
459	            dt = SUBGROUP_TAU[s_val]['tau_z1'] - SUBGROUP_TAU[s_val]['tau_z0']
460	            for z_level in [0, 1]:
461	                cell_gc = sub_df[(sub_df['method'] == 'global_corrected') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]
462	                cell_hb = sub_df[(sub_df['method'] == 'hb_ec_hte') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]
463	                bias_gc = abs(cell_gc['bias'].mean())
464	                bias_hb = abs(cell_hb['bias'].mean())
465	                rmse_gc = np.sqrt((cell_gc['bias'] ** 2).mean())
466	                rmse_hb = np.sqrt((cell_hb['bias'] ** 2).mean())
467	                imp = bias_gc - bias_hb
468	                lines.append(f"| {s_val} | {dt:.1f} | {z_level} | {bias_gc:.4f} | {bias_hb:.4f} | {imp:+.4f} | {rmse_gc:.4f} | {rmse_hb:.4f} |")
469	        lines.append("")
470	
471	    # Bias-variance decomposition
472	    lines.append("## Bias-Variance Decomposition\n")
473	    lines.append("| n_expert | Method | Bias² | Variance | MSE |")
474	    lines.append("|----------|--------|-------|----------|-----|")
475	    for ne in N_EXPERT_LIST:
476	        for m in method_order:
477	            sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]
478	            cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']
479	                          .agg(['mean', 'var', 'count']).reset_index())
480	            mean_bias_sq = (cell_stats['mean'] ** 2).mean()
481	            variance = cell_stats['var'].mean()
482	            mse = mean_bias_sq + variance
483	            lines.append(f"| {ne} | {method_labels[m]} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |")
484	    lines.append("")
485	
486	    # Cross-model comparison with Llama
487	    lines.append("## Cross-Model Comparison: Qwen vs Llama (exp-023)\n")
488	    lines.append("### CM Heterogeneity\n")
489	    lines.append("| Metric | Qwen2.5-7B | Llama3.1-8B |")
490	    lines.append("|--------|-----------|------------|")
491	    lines.append(f"| Δ_FPR (max-min) | {qwen_fpr_range:.4f} | {llama_fpr_range:.4f} |")
492	    lines.append(f"| Δ_FNR (max-min) | {qwen_fnr_range:.4f} | {llama_fnr_range:.4f} |")
493	    lines.append(f"| Mean Δ_error | {(qwen_fpr_range+qwen_fnr_range)/2:.4f} | {(llama_fpr_range+llama_fnr_range)/2:.4f} |")
494	    lines.append("")
495	
496	    lines.append("### Bias Comparison\n")
497	    lines.append("| n_expert | Qwen |Bias|_Global | Qwen |Bias|_ECHTE | Qwen Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |")
498	    lines.append("|----------|------------------|--------------------|--------------|--------------------|--------------------|---------------|")
499	    for ne in N_EXPERT_LIST:
500	        sub = summary[summary['n_expert'] == ne]
501	        qgc = sub[sub['method'] == 'global_corrected'].iloc[0]
502	        qhb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]
503	        qd = qgc['abs_bias'] - qhb['abs_bias']
504	        lr = LLAMA_RESULTS[ne]
505	        ld = lr['global_bias'] - lr['echte_bias']
506	        lines.append(f"| {ne} | {qgc['abs_bias']:.4f} | {qhb['abs_bias']:.4f} | {qd:+.4f} | {lr['global_bias']:.4f} | {lr['echte_bias']:.4f} | {ld:+.4f} |")
507	    lines.append("")
508	
509	    lines.append("### RMSE Comparison\n")
510	    lines.append("| n_expert | Qwen RMSE_Global | Qwen RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |")
511	    lines.append("|----------|-----------------|----------------|------------------|-----------------|")
512	    for ne in N_EXPERT_LIST:
513	        sub = summary[summary['n_expert'] == ne]
514	        qgc = sub[sub['method'] == 'global_corrected'].iloc[0]
515	        qhb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]
516	        lr = LLAMA_RESULTS[ne]
517	        lines.append(f"| {ne} | {qgc['rmse']:.4f} | {qhb['rmse']:.4f} | {lr['global_rmse']:.4f} | {lr['echte_rmse']:.4f} |")
518	    lines.append("")
519	
520	    # Conclusion
521	    lines.append("## Conclusion\n")
522	    gc_all = summary[summary['method'] == 'global_corrected']
523	    hb_all = summary[summary['method'] == 'hb_ec_hte']
524	    n_bias_wins = 0
525	    n_rmse_wins = 0
526	    for ne in N_EXPERT_LIST:
527	        gc_row = gc_all[gc_all['n_expert'] == ne].iloc[0]
528	        hb_row = hb_all[hb_all['n_expert'] == ne].iloc[0]
529	        if hb_row['abs_bias'] < gc_row['abs_bias']:
530	            n_bias_wins += 1
531	        if hb_row['rmse'] < gc_row['rmse']:
532	            n_rmse_wins += 1
533	
534	    lines.append(f"EC-HTE wins on |Bias| in {n_bias_wins}/{len(N_EXPERT_LIST)} budget levels.")
535	    lines.append(f"EC-HTE wins on RMSE in {n_rmse_wins}/{len(N_EXPERT_LIST)} budget levels.\n")
536	
537	    if n_bias_wins == len(N_EXPERT_LIST):
538	        lines.append("**Result: Under heterogeneous-τ DGP with Qwen2.5-7B CMs, EC-HTE consistently outperforms Global correction in bias.**\n")
539	    elif n_bias_wins > 0:
540	        lines.append(f"**Result: Under heterogeneous-τ DGP with Qwen2.5-7B CMs, EC-HTE outperforms Global in bias at {n_bias_wins} of {len(N_EXPERT_LIST)} budget levels.**\n")
541	    else:
542	        lines.append("**Result: EC-HTE does not outperform Global in bias under this DGP configuration with Qwen CMs.**\n")
543	
544	    # Cross-model conclusion
545	    llama_bias_wins = sum(1 for ne in N_EXPERT_LIST if LLAMA_RESULTS[ne]['echte_bias'] < LLAMA_RESULTS[ne]['global_bias'])
546	    lines.append(f"**Cross-model consistency**: Llama EC-HTE wins on bias in {llama_bias_wins}/3 budgets; "
547	                 f"Qwen EC-HTE wins in {n_bias_wins}/3 budgets.")
548	    if n_bias_wins == len(N_EXPERT_LIST) and llama_bias_wins == len(N_EXPERT_LIST):
549	        lines.append("EC-HTE's bias advantage is consistent across both Llama and Qwen models.")
550	    lines.append("")
551	
552	    avg_qwen_improvement = np.mean([
553	        (summary[(summary['n_expert']==ne) & (summary['method']=='global_corrected')].iloc[0]['abs_bias'] -
554	         summary[(summary['n_expert']==ne) & (summary['method']=='hb_ec_hte')].iloc[0]['abs_bias'])
555	        for ne in N_EXPERT_LIST
556	    ])
557	    avg_llama_improvement = np.mean([
558	        LLAMA_RESULTS[ne]['global_bias'] - LLAMA_RESULTS[ne]['echte_bias']
559	        for ne in N_EXPERT_LIST
560	    ])
561	    lines.append(f"Average Δ|Bias| (Global - EC-HTE): Qwen = {avg_qwen_improvement:+.4f}, Llama = {avg_llama_improvement:+.4f}")
562	    if avg_qwen_improvement > avg_llama_improvement:
563	        lines.append(f"Qwen shows larger EC-HTE improvement, consistent with its greater CM heterogeneity "
564	                     f"(Δ_FPR={qwen_fpr_range:.3f} vs {llama_fpr_range:.3f}).")
565	    else:
566	        lines.append(f"Llama shows larger EC-HTE improvement despite smaller CM heterogeneity.")
567	    lines.append("")
568	
569	    report = "\n".join(lines)
570	    with open(outpath, 'w') as f:
571	        f.write(report)
572	    print(f"Wrote {outpath}")
573	
574	
575	# === Main ===
576	
577	if __name__ == '__main__':
578	    print("Qwen2.5-7B Heterogeneous-τ DGP: EC-HTE vs Global")
579	    print(f"N={N}, budgets={N_EXPERT_LIST}, seeds={N_MC}")
580	    print("Qwen per-subgroup CM:")
581	    for s in SUBGROUP_LABELS:
582	        cm = SUBGROUP_CM[s]
583	        print(f"  {s}: FPR={cm['fpr']:.4f}, FNR={cm['fnr']:.4f}")
584	    print("Subgroup τ values:")
585	    for s in SUBGROUP_LABELS:
586	        t = SUBGROUP_TAU[s]
587	        print(f"  {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}")
588	    print()
589	
590	    out_dir = 'artifacts/c1_multi_llm'
591	
592	    # Dry run: 1 budget, 1 seed
593	    print("=== Dry run (n_expert=200, 1 seed) ===")
594	    data = generate_data(SEED_BASE, 200)
595	    rows = run_one_mc(data, SEED_BASE)
596	    df_dry = pd.DataFrame(rows)
597	    df_dry['n_expert'] = 200
598	    print(f"Dry run OK: {len(df_dry)} rows, columns: {list(df_dry.columns)}")
599	    for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:
600	        sub = df_dry[df_dry['method'] == m]
601	        bias = sub['bias'].abs().mean()
602	        print(f"  {m:20s}: mean |bias| = {bias:.4f}")
603	
604	    # Verify oracle CATE values
605	    print("\n  Oracle CATE check:")
606	    for s_val in SUBGROUP_LABELS:
607	        for zl in [0, 1]:
608	            cell = df_dry[(df_dry['subgroup'] == s_val) & (df_dry['z_level'] == zl)]
609	            true_val = cell['cate_true'].iloc[0]
610	            expected = SUBGROUP_TAU[s_val]['tau_z1'] if zl == 1 else SUBGROUP_TAU[s_val]['tau_z0']
611	            ok = "OK" if abs(true_val - expected) < 1e-10 else "MISMATCH"
612	            print(f"    {s_val} z={zl}: cate_true={true_val:.2f} expected={expected:.2f} [{ok}]")
613	    print()
614	
615	    # Full run
616	    print(f"=== Full run ({len(N_EXPERT_LIST)} budgets x {N_MC} seeds) ===")
617	    all_results = []
618	    t0 = time.time()
619	    total_runs = len(N_EXPERT_LIST) * N_MC
620	    run_count = 0
621	
622	    for n_expert in N_EXPERT_LIST:
623	        print(f"\n--- n_expert = {n_expert} ---")
624	        t_budget = time.time()
625	        for mc in range(N_MC):
626	            seed = SEED_BASE + mc
627	            data = generate_data(seed, n_expert)
628	            mc_rows = run_one_mc(data, seed)
629	            for r in mc_rows:
630	                r['n_expert'] = n_expert
631	            all_results.extend(mc_rows)
632	            run_count += 1
633	            if (mc + 1) % 10 == 0:
634	                elapsed = time.time() - t0
635	                eta = elapsed / run_count * (total_runs - run_count)
636	                print(f"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s")
637	        budget_time = time.time() - t_budget
638	        print(f"  n_expert={n_expert} done in {budget_time:.1f}s")
639	
640	    total_time = time.time() - t0
641	    print(f"\nTotal time: {total_time:.1f}s")
642	
643	    df_raw = pd.DataFrame(all_results)
644	
645	    # Save results CSV
646	    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width']
647	    df_raw[col_order].to_csv(f'{out_dir}/qwen_hetero_tau_results.csv', index=False)
648	    print(f"Saved qwen_hetero_tau_results.csv ({len(df_raw)} rows)")
649	
650	    # Write analysis
651	    write_analysis(df_raw, f'{out_dir}/qwen_hetero_tau_analysis.md')
652	
653	    # Print summary
654	    print("\n=== Summary ===")
655	    abs_bias = compute_corrected_abs_bias(df_raw)
656	    rmse_df = compute_rmse(df_raw)
657	    summary = abs_bias.merge(rmse_df, on=['n_expert', 'method'])
658	    for ne in N_EXPERT_LIST:
659	        print(f"\n  n_expert={ne}:")
660	        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:
661	            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]
662	            if len(row) > 0:
663	                print(f"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}")
664	    print()
665	
666	    # EC-HTE vs Global
667	    print("=== EC-HTE vs Global (Qwen) ===")
668	    for ne in N_EXPERT_LIST:
669	        gc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]
670	        hb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]
671	        print(f"  n_expert={ne}: |Bias| Global={gc['abs_bias']:.4f} vs ECHTE={hb['abs_bias']:.4f} "
672	              f"({'ECHTE wins' if hb['abs_bias'] < gc['abs_bias'] else 'Global wins'})")
673	        print(f"              RMSE  Global={gc['rmse']:.4f} vs ECHTE={hb['rmse']:.4f} "
674	              f"({'ECHTE wins' if hb['rmse'] < gc['rmse'] else 'Global wins'})")
675	
676	    # Cross-model comparison
677	    print("\n=== Cross-Model: Qwen vs Llama ===")
678	    for ne in N_EXPERT_LIST:
679	        qgc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]
680	        qhb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]
681	        lr = LLAMA_RESULTS[ne]
682	        print(f"  n_expert={ne}:")
683	        print(f"    Qwen  Δ|Bias| = {qgc['abs_bias'] - qhb['abs_bias']:+.4f}")
684	        print(f"    Llama Δ|Bias| = {lr['global_bias'] - lr['echte_bias']:+.4f}")
685	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9021316a-af65-4464-b4f5-1da8c5dce568",
  "isSidechain": false,
  "promptId": "695fc122-00c0-4b11-823d-9471ae018801",
  "type": "user",
  "uuid": "bc5331ba-ad0b-4f72-b7f7-8928f576dff5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_qwen_hetero_tau.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nHeterogeneous-τ DGP experiment with Qwen2.5-7B confusion matrices.\nMirrors run_hetero_tau.py (Llama) but uses Qwen per-subgroup FPR/FNR.\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [200, 500, 1000]\nN_MC = 50\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']\nSUBGROUP_WEIGHTS = np.array([0.3816, 0.2224, 0.2551, 0.1408])\nSUBGROUP_WEIGHTS = SUBGROUP_WEIGHTS / SUBGROUP_WEIGHTS.sum()\n\nSUBGROUP_CM = {\n    'False_medium': {'fpr': 0.1800, 'fnr': 0.2874},\n    'False_short':  {'fpr': 0.2414, 'fnr': 0.1750},\n    'True_medium':  {'fpr': 0.2333, 'fnr': 0.2105},\n    'True_short':   {'fpr': 0.0000, 'fnr': 0.1379},\n}\n\nSUBGROUP_TAU = {\n    'True_short':   {'tau_z0': 0.2,  'tau_z1': 0.8},\n    'True_medium':  {'tau_z0': 0.35, 'tau_z1': 0.65},\n    'False_short':  {'tau_z0': 0.4,  'tau_z1': 0.5},\n    'False_medium': {'tau_z0': 0.45, 'tau_z1': 0.55},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\n\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === MAP-EB ===\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):\n    hp_rate = 1.0 / hp_scale\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = hp_shape * hp_scale\n            continue\n\n        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):\n            nll = _dirmult_neg_ll(a, _cl)\n            if a < 1e-10:\n                return 1e10\n            log_prior = (_shape - 1.0) * np.log(a) - _rate * a\n            return nll - log_prior\n\n        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n_sz = counts[i, z, :].sum()\n            d = n_sz + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    return C, alpha_opt\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\n# === DGP (heterogeneous tau) ===\n\ndef generate_data(seed, n_expert):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.zeros(N)\n    for i, s in enumerate(SUBGROUP_LABELS):\n        s_mask = S_idx == i\n        tau_s = SUBGROUP_TAU[s]\n        tau_vals[s_mask] = np.where(Z[s_mask] == 1, tau_s['tau_z1'], tau_s['tau_z0'])\n\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_map_eb(counts, SUBGROUP_LABELS)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n        tau_s = SUBGROUP_TAU[s_val]\n\n        for z_level in [0, 1]:\n            oracle_cate = tau_s['tau_z1'] if z_level == 1 else tau_s['tau_z0']\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_w_nv = 2 * 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_est': th_nv, 'cate_true': oracle_cate,\n                'coverage': cov_nv, 'ci_width': ci_w_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_w_gc = 2 * 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_est': th_gc, 'cate_true': oracle_cate,\n                'coverage': cov_gc, 'ci_width': ci_w_gc,\n            })\n\n            # Stratified MLE\n            ci_w_ml = 2 * 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_est': th_ml, 'cate_true': oracle_cate,\n                'coverage': cov_ml, 'ci_width': ci_w_ml,\n            })\n\n            # HB EC-HTE (MAP-EB)\n            ci_w_hb = 2 * 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_est': th_hb, 'cate_true': oracle_cate,\n                'coverage': cov_hb, 'ci_width': ci_w_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef compute_corrected_abs_bias(df):\n    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']\n                 .mean().abs().reset_index(name='abs_mean_bias'))\n    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']\n            .mean().reset_index(name='abs_bias'))\n\n\ndef compute_rmse(df):\n    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)\n                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']\n                 .mean().apply(np.sqrt).reset_index(name='rmse'))\n    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']\n            .mean().reset_index(name='rmse'))\n\n\ndef compute_coverage(df):\n    return (df.groupby(['n_expert', 'method'])['coverage']\n            .mean().reset_index(name='coverage'))\n\n\ndef compute_ci_width(df):\n    return (df.groupby(['n_expert', 'method'])['ci_width']\n            .mean().reset_index(name='ci_width'))\n\n\n# === Analysis Report ===\n\nLLAMA_RESULTS = {\n    200:  {'global_bias': 0.0365, 'echte_bias': 0.0248, 'global_rmse': 0.1780, 'echte_rmse': 0.2606},\n    500:  {'global_bias': 0.0314, 'echte_bias': 0.0099, 'global_rmse': 0.1580, 'echte_rmse': 0.1760},\n    1000: {'global_bias': 0.0286, 'echte_bias': 0.0130, 'global_rmse': 0.1554, 'echte_rmse': 0.1602},\n}\n\nLLAMA_CM = {\n    'False_medium': {'fpr': 0.235, 'fnr': 0.319},\n    'False_short':  {'fpr': 0.310, 'fnr': 0.212},\n    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},\n    'True_short':   {'fpr': 0.091, 'fnr': 0.190},\n}\n\n\ndef write_analysis(df_raw, outpath):\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse = compute_rmse(df_raw)\n    cov = compute_coverage(df_raw)\n    ciw = compute_ci_width(df_raw)\n\n    summary = abs_bias.merge(rmse, on=['n_expert', 'method']).merge(\n        cov, on=['n_expert', 'method']).merge(ciw, on=['n_expert', 'method'])\n\n    lines = []\n    lines.append(\"# Qwen2.5-7B Heterogeneous-τ DGP: EC-HTE vs Global Correction\\n\")\n    lines.append(\"## Design\\n\")\n    lines.append(f\"- N={N}, P(Z=1)={P_Z1}, K=4 subgroups\")\n    lines.append(\"- **LLM**: Qwen2.5-7B (balanced binarization)\")\n    lines.append(\"- **Heterogeneous τ(z) across subgroups:**\")\n    for s in SUBGROUP_LABELS:\n        t = SUBGROUP_TAU[s]\n        lines.append(f\"  - {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}\")\n    lines.append(f\"- n_expert sweep: {N_EXPERT_LIST}\")\n    lines.append(f\"- {N_MC} MC seeds per budget\")\n    lines.append(\"- HB method: MAP-EB (Gamma(3,1) prior)\")\n    lines.append(f\"- |Bias| = avg across cells of |mean(bias) across seeds|\")\n    lines.append(f\"- RMSE = avg across cells of sqrt(mean(bias²) across seeds)\")\n    lines.append(\"\")\n\n    # Qwen CM table\n    lines.append(\"## Qwen2.5-7B Per-Subgroup Confusion Matrix\\n\")\n    lines.append(\"| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |\")\n    lines.append(\"|----------|-----|-----|-----|-----------|\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        w = SUBGROUP_WEIGHTS[SUBGROUP_LABELS.index(s)]\n        lines.append(f\"| {s} | {w:.4f} | {cm['fpr']:.4f} | {cm['fnr']:.4f} | {1-cm['fpr']-cm['fnr']:.4f} |\")\n    lines.append(\"\")\n    qwen_fpr_range = max(cm['fpr'] for cm in SUBGROUP_CM.values()) - min(cm['fpr'] for cm in SUBGROUP_CM.values())\n    qwen_fnr_range = max(cm['fnr'] for cm in SUBGROUP_CM.values()) - min(cm['fnr'] for cm in SUBGROUP_CM.values())\n    llama_fpr_range = max(cm['fpr'] for cm in LLAMA_CM.values()) - min(cm['fpr'] for cm in LLAMA_CM.values())\n    llama_fnr_range = max(cm['fnr'] for cm in LLAMA_CM.values()) - min(cm['fnr'] for cm in LLAMA_CM.values())\n    lines.append(f\"- Qwen Δ_FPR = {qwen_fpr_range:.4f}, Δ_FNR = {qwen_fnr_range:.4f}\")\n    lines.append(f\"- Llama Δ_FPR = {llama_fpr_range:.4f}, Δ_FNR = {llama_fnr_range:.4f}\")\n    lines.append(f\"- Qwen has {'larger' if qwen_fpr_range > llama_fpr_range else 'smaller'} FPR heterogeneity \"\n                 f\"and {'larger' if qwen_fnr_range > llama_fnr_range else 'smaller'} FNR heterogeneity than Llama\")\n    lines.append(\"\")\n\n    # Summary table\n    lines.append(\"## Summary Table (averaged across all cells)\\n\")\n    lines.append(\"| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |\")\n    lines.append(\"|----------|--------|-------|------|----------|----------|\")\n\n    method_order = ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']\n    method_labels = {'naive': 'Naive', 'global_corrected': 'Global', 'stratified_mle': 'Strat MLE', 'hb_ec_hte': 'HB EC-HTE'}\n\n    for ne in N_EXPERT_LIST:\n        for m in method_order:\n            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n            if len(row) > 0:\n                r = row.iloc[0]\n                lines.append(f\"| {ne} | {method_labels[m]} | {r['abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} | {r['ci_width']:.3f} |\")\n        lines.append(\"|----------|--------|-------|------|----------|----------|\")\n    lines.append(\"\")\n\n    # EC-HTE vs Global comparison\n    lines.append(\"## EC-HTE vs Global Comparison\\n\")\n    lines.append(\"| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |\")\n    lines.append(\"|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        gc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        hb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        d_bias = gc['abs_bias'] - hb['abs_bias']\n        d_rmse = gc['rmse'] - hb['rmse']\n        wb = \"**YES**\" if hb['abs_bias'] < gc['abs_bias'] else \"no\"\n        wr = \"**YES**\" if hb['rmse'] < gc['rmse'] else \"no\"\n        lines.append(f\"| {ne} | {gc['abs_bias']:.4f} | {hb['abs_bias']:.4f} | {d_bias:+.4f} | {gc['rmse']:.4f} | {hb['rmse']:.4f} | {d_rmse:+.4f} | {wb} | {wr} |\")\n    lines.append(\"\")\n\n    # Per-subgroup breakdown\n    lines.append(\"## Per-Subgroup Breakdown\\n\")\n    for ne in N_EXPERT_LIST:\n        lines.append(f\"### n_expert = {ne}\\n\")\n        lines.append(\"| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\")\n        lines.append(\"|----------|-----|---|-------------|-------------|-------------|-------------|------------|\")\n        sub_df = df_raw[df_raw['n_expert'] == ne]\n        for s_val in SUBGROUP_LABELS:\n            dt = SUBGROUP_TAU[s_val]['tau_z1'] - SUBGROUP_TAU[s_val]['tau_z0']\n            for z_level in [0, 1]:\n                cell_gc = sub_df[(sub_df['method'] == 'global_corrected') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]\n                cell_hb = sub_df[(sub_df['method'] == 'hb_ec_hte') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]\n                bias_gc = abs(cell_gc['bias'].mean())\n                bias_hb = abs(cell_hb['bias'].mean())\n                rmse_gc = np.sqrt((cell_gc['bias'] ** 2).mean())\n                rmse_hb = np.sqrt((cell_hb['bias'] ** 2).mean())\n                imp = bias_gc - bias_hb\n                lines.append(f\"| {s_val} | {dt:.1f} | {z_level} | {bias_gc:.4f} | {bias_hb:.4f} | {imp:+.4f} | {rmse_gc:.4f} | {rmse_hb:.4f} |\")\n        lines.append(\"\")\n\n    # Bias-variance decomposition\n    lines.append(\"## Bias-Variance Decomposition\\n\")\n    lines.append(\"| n_expert | Method | Bias² | Variance | MSE |\")\n    lines.append(\"|----------|--------|-------|----------|-----|\")\n    for ne in N_EXPERT_LIST:\n        for m in method_order:\n            sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]\n            cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']\n                          .agg(['mean', 'var', 'count']).reset_index())\n            mean_bias_sq = (cell_stats['mean'] ** 2).mean()\n            variance = cell_stats['var'].mean()\n            mse = mean_bias_sq + variance\n            lines.append(f\"| {ne} | {method_labels[m]} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |\")\n    lines.append(\"\")\n\n    # Cross-model comparison with Llama\n    lines.append(\"## Cross-Model Comparison: Qwen vs Llama (exp-023)\\n\")\n    lines.append(\"### CM Heterogeneity\\n\")\n    lines.append(\"| Metric | Qwen2.5-7B | Llama3.1-8B |\")\n    lines.append(\"|--------|-----------|------------|\")\n    lines.append(f\"| Δ_FPR (max-min) | {qwen_fpr_range:.4f} | {llama_fpr_range:.4f} |\")\n    lines.append(f\"| Δ_FNR (max-min) | {qwen_fnr_range:.4f} | {llama_fnr_range:.4f} |\")\n    lines.append(f\"| Mean Δ_error | {(qwen_fpr_range+qwen_fnr_range)/2:.4f} | {(llama_fpr_range+llama_fnr_range)/2:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Bias Comparison\\n\")\n    lines.append(\"| n_expert | Qwen |Bias|_Global | Qwen |Bias|_ECHTE | Qwen Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |\")\n    lines.append(\"|----------|------------------|--------------------|--------------|--------------------|--------------------|---------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        qgc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        qhb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        qd = qgc['abs_bias'] - qhb['abs_bias']\n        lr = LLAMA_RESULTS[ne]\n        ld = lr['global_bias'] - lr['echte_bias']\n        lines.append(f\"| {ne} | {qgc['abs_bias']:.4f} | {qhb['abs_bias']:.4f} | {qd:+.4f} | {lr['global_bias']:.4f} | {lr['echte_bias']:.4f} | {ld:+.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### RMSE Comparison\\n\")\n    lines.append(\"| n_expert | Qwen RMSE_Global | Qwen RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |\")\n    lines.append(\"|----------|-----------------|----------------|------------------|-----------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        qgc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        qhb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        lr = LLAMA_RESULTS[ne]\n        lines.append(f\"| {ne} | {qgc['rmse']:.4f} | {qhb['rmse']:.4f} | {lr['global_rmse']:.4f} | {lr['echte_rmse']:.4f} |\")\n    lines.append(\"\")\n\n    # Conclusion\n    lines.append(\"## Conclusion\\n\")\n    gc_all = summary[summary['method'] == 'global_corrected']\n    hb_all = summary[summary['method'] == 'hb_ec_hte']\n    n_bias_wins = 0\n    n_rmse_wins = 0\n    for ne in N_EXPERT_LIST:\n        gc_row = gc_all[gc_all['n_expert'] == ne].iloc[0]\n        hb_row = hb_all[hb_all['n_expert'] == ne].iloc[0]\n        if hb_row['abs_bias'] < gc_row['abs_bias']:\n            n_bias_wins += 1\n        if hb_row['rmse'] < gc_row['rmse']:\n            n_rmse_wins += 1\n\n    lines.append(f\"EC-HTE wins on |Bias| in {n_bias_wins}/{len(N_EXPERT_LIST)} budget levels.\")\n    lines.append(f\"EC-HTE wins on RMSE in {n_rmse_wins}/{len(N_EXPERT_LIST)} budget levels.\\n\")\n\n    if n_bias_wins == len(N_EXPERT_LIST):\n        lines.append(\"**Result: Under heterogeneous-τ DGP with Qwen2.5-7B CMs, EC-HTE consistently outperforms Global correction in bias.**\\n\")\n    elif n_bias_wins > 0:\n        lines.append(f\"**Result: Under heterogeneous-τ DGP with Qwen2.5-7B CMs, EC-HTE outperforms Global in bias at {n_bias_wins} of {len(N_EXPERT_LIST)} budget levels.**\\n\")\n    else:\n        lines.append(\"**Result: EC-HTE does not outperform Global in bias under this DGP configuration with Qwen CMs.**\\n\")\n\n    # Cross-model conclusion\n    llama_bias_wins = sum(1 for ne in N_EXPERT_LIST if LLAMA_RESULTS[ne]['echte_bias'] < LLAMA_RESULTS[ne]['global_bias'])\n    lines.append(f\"**Cross-model consistency**: Llama EC-HTE wins on bias in {llama_bias_wins}/3 budgets; \"\n                 f\"Qwen EC-HTE wins in {n_bias_wins}/3 budgets.\")\n    if n_bias_wins == len(N_EXPERT_LIST) and llama_bias_wins == len(N_EXPERT_LIST):\n        lines.append(\"EC-HTE's bias advantage is consistent across both Llama and Qwen models.\")\n    lines.append(\"\")\n\n    avg_qwen_improvement = np.mean([\n        (summary[(summary['n_expert']==ne) & (summary['method']=='global_corrected')].iloc[0]['abs_bias'] -\n         summary[(summary['n_expert']==ne) & (summary['method']=='hb_ec_hte')].iloc[0]['abs_bias'])\n        for ne in N_EXPERT_LIST\n    ])\n    avg_llama_improvement = np.mean([\n        LLAMA_RESULTS[ne]['global_bias'] - LLAMA_RESULTS[ne]['echte_bias']\n        for ne in N_EXPERT_LIST\n    ])\n    lines.append(f\"Average Δ|Bias| (Global - EC-HTE): Qwen = {avg_qwen_improvement:+.4f}, Llama = {avg_llama_improvement:+.4f}\")\n    if avg_qwen_improvement > avg_llama_improvement:\n        lines.append(f\"Qwen shows larger EC-HTE improvement, consistent with its greater CM heterogeneity \"\n                     f\"(Δ_FPR={qwen_fpr_range:.3f} vs {llama_fpr_range:.3f}).\")\n    else:\n        lines.append(f\"Llama shows larger EC-HTE improvement despite smaller CM heterogeneity.\")\n    lines.append(\"\")\n\n    report = \"\\n\".join(lines)\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"Qwen2.5-7B Heterogeneous-τ DGP: EC-HTE vs Global\")\n    print(f\"N={N}, budgets={N_EXPERT_LIST}, seeds={N_MC}\")\n    print(\"Qwen per-subgroup CM:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.4f}, FNR={cm['fnr']:.4f}\")\n    print(\"Subgroup τ values:\")\n    for s in SUBGROUP_LABELS:\n        t = SUBGROUP_TAU[s]\n        print(f\"  {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}\")\n    print()\n\n    out_dir = 'artifacts/c1_multi_llm'\n\n    # Dry run: 1 budget, 1 seed\n    print(\"=== Dry run (n_expert=200, 1 seed) ===\")\n    data = generate_data(SEED_BASE, 200)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    df_dry['n_expert'] = 200\n    print(f\"Dry run OK: {len(df_dry)} rows, columns: {list(df_dry.columns)}\")\n    for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n\n    # Verify oracle CATE values\n    print(\"\\n  Oracle CATE check:\")\n    for s_val in SUBGROUP_LABELS:\n        for zl in [0, 1]:\n            cell = df_dry[(df_dry['subgroup'] == s_val) & (df_dry['z_level'] == zl)]\n            true_val = cell['cate_true'].iloc[0]\n            expected = SUBGROUP_TAU[s_val]['tau_z1'] if zl == 1 else SUBGROUP_TAU[s_val]['tau_z0']\n            ok = \"OK\" if abs(true_val - expected) < 1e-10 else \"MISMATCH\"\n            print(f\"    {s_val} z={zl}: cate_true={true_val:.2f} expected={expected:.2f} [{ok}]\")\n    print()\n\n    # Full run\n    print(f\"=== Full run ({len(N_EXPERT_LIST)} budgets x {N_MC} seeds) ===\")\n    all_results = []\n    t0 = time.time()\n    total_runs = len(N_EXPERT_LIST) * N_MC\n    run_count = 0\n\n    for n_expert in N_EXPERT_LIST:\n        print(f\"\\n--- n_expert = {n_expert} ---\")\n        t_budget = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, n_expert)\n            mc_rows = run_one_mc(data, seed)\n            for r in mc_rows:\n                r['n_expert'] = n_expert\n            all_results.extend(mc_rows)\n            run_count += 1\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / run_count * (total_runs - run_count)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n        budget_time = time.time() - t_budget\n        print(f\"  n_expert={n_expert} done in {budget_time:.1f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n\n    # Save results CSV\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width']\n    df_raw[col_order].to_csv(f'{out_dir}/qwen_hetero_tau_results.csv', index=False)\n    print(f\"Saved qwen_hetero_tau_results.csv ({len(df_raw)} rows)\")\n\n    # Write analysis\n    write_analysis(df_raw, f'{out_dir}/qwen_hetero_tau_analysis.md')\n\n    # Print summary\n    print(\"\\n=== Summary ===\")\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse_df = compute_rmse(df_raw)\n    summary = abs_bias.merge(rmse_df, on=['n_expert', 'method'])\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n  n_expert={ne}:\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n            if len(row) > 0:\n                print(f\"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}\")\n    print()\n\n    # EC-HTE vs Global\n    print(\"=== EC-HTE vs Global (Qwen) ===\")\n    for ne in N_EXPERT_LIST:\n        gc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]\n        hb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]\n        print(f\"  n_expert={ne}: |Bias| Global={gc['abs_bias']:.4f} vs ECHTE={hb['abs_bias']:.4f} \"\n              f\"({'ECHTE wins' if hb['abs_bias'] < gc['abs_bias'] else 'Global wins'})\")\n        print(f\"              RMSE  Global={gc['rmse']:.4f} vs ECHTE={hb['rmse']:.4f} \"\n              f\"({'ECHTE wins' if hb['rmse'] < gc['rmse'] else 'Global wins'})\")\n\n    # Cross-model comparison\n    print(\"\\n=== Cross-Model: Qwen vs Llama ===\")\n    for ne in N_EXPERT_LIST:\n        qgc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]\n        qhb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]\n        lr = LLAMA_RESULTS[ne]\n        print(f\"  n_expert={ne}:\")\n        print(f\"    Qwen  Δ|Bias| = {qgc['abs_bias'] - qhb['abs_bias']:+.4f}\")\n        print(f\"    Llama Δ|Bias| = {lr['global_bias'] - lr['echte_bias']:+.4f}\")\n",
      "numLines": 685,
      "startLine": 1,
      "totalLines": 685
    }
  },
  "sourceToolAssistantUUID": "9021316a-af65-4464-b4f5-1da8c5dce568",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "leafUuid": "bc5331ba-ad0b-4f72-b7f7-8928f576dff5",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Mistral-7B heterogeneous-τ DGP experiment",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8"
}
```

---

### Assistant

_source line 13 · 2026-05-22T00:15:04.410Z_

Now I'll create the Mistral version by replacing only the CM parameters and model-specific labels, then also check the Llama reference file for cross-model comparison data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc5331ba-ad0b-4f72-b7f7-8928f576dff5",
  "isSidechain": false,
  "requestId": "req_011CbGeFht8aQiHvE9W4DMo6",
  "type": "assistant",
  "uuid": "0ccf7665-8ab4-4f19-bab8-14b06c856d29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147H6bUjMuHmsWaPiNGQ41H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13636,
      "cache_read_input_tokens": 18397,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13636,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 369,
          "cache_read_input_tokens": 18397,
          "cache_creation_input_tokens": 13636,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13636
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

_source line 14 · 2026-05-22T00:15:08.417Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01RAGe9GiiobKMBeBPcNgPXd`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find Llama hetero_tau analysis",
  "prompt": "Find the Llama exp-023 hetero_tau_analysis.md file referenced in the project. Look in /home/ubuntu/ec_hte_llm_annotation/artifacts/ for files matching *hetero_tau_analysis* or in directories like exp-023, exp023, etc. Report the full path and key results: per-budget Global bias, ECHTE bias, Global RMSE, ECHTE RMSE values, and the Llama CM values used."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ccf7665-8ab4-4f19-bab8-14b06c856d29",
  "isSidechain": false,
  "requestId": "req_011CbGeFht8aQiHvE9W4DMo6",
  "type": "assistant",
  "uuid": "ce60d46f-7b10-434a-8855-e17c88976b13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147H6bUjMuHmsWaPiNGQ41H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13636,
      "cache_read_input_tokens": 18397,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13636,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 369,
          "cache_read_input_tokens": 18397,
          "cache_creation_input_tokens": 13636,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13636
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

_source line 15 · 2026-05-22T00:15:10.223Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Cf9UWNjmgNXQBBqeMEbE6S`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Check Qwen analysis format",
  "prompt": "Read /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md and report back its full content so I can see the exact format used."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce60d46f-7b10-434a-8855-e17c88976b13",
  "isSidechain": false,
  "requestId": "req_011CbGeFht8aQiHvE9W4DMo6",
  "type": "assistant",
  "uuid": "caa3acec-e882-467c-9e71-3250fb9b3aff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147H6bUjMuHmsWaPiNGQ41H",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13636,
      "cache_read_input_tokens": 18397,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13636,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 369,
          "cache_read_input_tokens": 18397,
          "cache_creation_input_tokens": 13636,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13636
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

_source line 16 · 2026-05-22T00:15:18.149Z_

<details><summary>↩ Tool result · `toolu_01Cf9UWNjmgNXQBBqeMEbE6S`</summary>

```text
Here's the full content of the file:

The document follows a structured analysis format for comparing EC-HTE (Empirical Calibration - Heterogeneous Treatment Effects) vs Global Correction methods. Here's the exact format used:

**Structure:**
1. **Design section** - Parameters and setup (sample size, treatment probability, subgroups, LLM used, heterogeneous τ values, expert budget sweep, method details)

2. **Confusion matrix table** - Per-subgroup metrics (Subgroup, π_s, FPR, FNR, 1-FPR-FNR)

3. **Summary table** - Aggregated metrics across all cells for different methods (n_expert, Method, |Bias|, RMSE, Coverage, CI Width)

4. **Comparison table** - EC-HTE vs Global direct comparison (n_expert, |Bias| values, RMSE values, difference columns, yes/no verdict columns)

5. **Per-subgroup breakdown** - Separate tables for each n_expert level (Subgroup, Δτ, z treatment indicator, |Bias|_Global, |Bias|_ECHTE, Improvement, RMSE metrics)

6. **Bias-variance decomposition** - Squared bias, variance, and MSE across methods and budgets

7. **Cross-model comparison** - Tables comparing Qwen vs Llama on heterogeneity and bias/RMSE metrics

8. **Conclusion** - Summary statements with key findings and consistency observations

**Key formatting elements:**
- Markdown headers (H1, H2, H3)
- Markdown tables with pipe delimiters
- Bullet points for design parameters
- Bold text for emphasis (**text**)
- Comparison metrics shown as positive/negative deltas (+/-0.XXXX)
- Yes/no verdict columns for method comparisons
- Cross-model comparison using consistent column structure

The file is 155 lines of markdown with data presented in tabular format, with tables separated by strategic breakpoints for different analyses.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "caa3acec-e882-467c-9e71-3250fb9b3aff",
  "isSidechain": false,
  "promptId": "695fc122-00c0-4b11-823d-9471ae018801",
  "type": "user",
  "uuid": "56c398ed-9658-4cbe-a57f-2d24f81b24fd",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Read /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md and report back its full content so I can see the exact format used.",
    "agentId": "acc702bdbdeab86f3",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Here's the full content of the file:\n\nThe document follows a structured analysis format for comparing EC-HTE (Empirical Calibration - Heterogeneous Treatment Effects) vs Global Correction methods. Here's the exact format used:\n\n**Structure:**\n1. **Design section** - Parameters and setup (sample size, treatment probability, subgroups, LLM used, heterogeneous τ values, expert budget sweep, method details)\n\n2. **Confusion matrix table** - Per-subgroup metrics (Subgroup, π_s, FPR, FNR, 1-FPR-FNR)\n\n3. **Summary table** - Aggregated metrics across all cells for different methods (n_expert, Method, |Bias|, RMSE, Coverage, CI Width)\n\n4. **Comparison table** - EC-HTE vs Global direct comparison (n_expert, |Bias| values, RMSE values, difference columns, yes/no verdict columns)\n\n5. **Per-subgroup breakdown** - Separate tables for each n_expert level (Subgroup, Δτ, z treatment indicator, |Bias|_Global, |Bias|_ECHTE, Improvement, RMSE metrics)\n\n6. **Bias-variance decomposition** - Squared bias, variance, and MSE across methods and budgets\n\n7. **Cross-model comparison** - Tables comparing Qwen vs Llama on heterogeneity and bias/RMSE metrics\n\n8. **Conclusion** - Summary statements with key findings and consistency observations\n\n**Key formatting elements:**\n- Markdown headers (H1, H2, H3)\n- Markdown tables with pipe delimiters\n- Bullet points for design parameters\n- Bold text for emphasis (**text**)\n- Comparison metrics shown as positive/negative deltas (+/-0.XXXX)\n- Yes/no verdict columns for method comparisons\n- Cross-model comparison using consistent column structure\n\nThe file is 155 lines of markdown with data presented in tabular format, with tables separated by strategic breakpoints for different analyses."
      }
    ],
    "totalDurationMs": 7924,
    "totalTokens": 23587,
    "totalToolUseCount": 1,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 5319,
      "cache_read_input_tokens": 17789,
      "output_tokens": 474,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5319
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 474,
          "cache_read_input_tokens": 17789,
          "cache_creation_input_tokens": 5319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5319,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "caa3acec-e882-467c-9e71-3250fb9b3aff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-22T00:15:21.155Z_

<details><summary>↩ Tool result · `toolu_01RAGe9GiiobKMBeBPcNgPXd`</summary>

```text
Perfect! I found the files. Based on your request for the Llama exp-023 results, here's what I found:

## File Location
**/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/hetero_tau_analysis.md**

This is the generic hetero_tau_analysis.md file that contains Llama results (the exp-023 reference appears in the qwen file as a cross-model comparison).

## Key Results for Llama:

### Per-Budget Global Bias (|Bias|_Global)
- **n_expert = 200**: 0.0365
- **n_expert = 500**: 0.0314
- **n_expert = 1000**: 0.0286

### Per-Budget ECHTE Bias (|Bias|_ECHTE)
- **n_expert = 200**: 0.0248
- **n_expert = 500**: 0.0099
- **n_expert = 1000**: 0.0130

### Per-Budget Global RMSE (RMSE_Global)
- **n_expert = 200**: 0.1780
- **n_expert = 500**: 0.1580
- **n_expert = 1000**: 0.1554

### Per-Budget ECHTE RMSE (RMSE_ECHTE)
- **n_expert = 200**: 0.2606
- **n_expert = 500**: 0.1760
- **n_expert = 1000**: 0.1602

### Llama Confusion Matrix (CM) Values
From the cross-model comparison section in qwen_hetero_tau_analysis.md:
- **Llama Δ_FPR (max-min)**: 0.2190
- **Llama Δ_FNR (max-min)**: 0.1290
- **Mean Δ_error**: 0.1740

These values represent the heterogeneity in Llama3.1-8B's classification metrics across the four subgroups.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce60d46f-7b10-434a-8855-e17c88976b13",
  "isSidechain": false,
  "promptId": "695fc122-00c0-4b11-823d-9471ae018801",
  "type": "user",
  "uuid": "f625a28a-3a58-4be0-a869-450bba8bfcc2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Find the Llama exp-023 hetero_tau_analysis.md file referenced in the project. Look in /home/ubuntu/ec_hte_llm_annotation/artifacts/ for files matching *hetero_tau_analysis* or in directories like exp-023, exp023, etc. Report the full path and key results: per-budget Global bias, ECHTE bias, Global RMSE, ECHTE RMSE values, and the Llama CM values used.",
    "agentId": "ad72143b5ba21a733",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I found the files. Based on your request for the Llama exp-023 results, here's what I found:\n\n## File Location\n**/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/hetero_tau_analysis.md**\n\nThis is the generic hetero_tau_analysis.md file that contains Llama results (the exp-023 reference appears in the qwen file as a cross-model comparison).\n\n## Key Results for Llama:\n\n### Per-Budget Global Bias (|Bias|_Global)\n- **n_expert = 200**: 0.0365\n- **n_expert = 500**: 0.0314\n- **n_expert = 1000**: 0.0286\n\n### Per-Budget ECHTE Bias (|Bias|_ECHTE)\n- **n_expert = 200**: 0.0248\n- **n_expert = 500**: 0.0099\n- **n_expert = 1000**: 0.0130\n\n### Per-Budget Global RMSE (RMSE_Global)\n- **n_expert = 200**: 0.1780\n- **n_expert = 500**: 0.1580\n- **n_expert = 1000**: 0.1554\n\n### Per-Budget ECHTE RMSE (RMSE_ECHTE)\n- **n_expert = 200**: 0.2606\n- **n_expert = 500**: 0.1760\n- **n_expert = 1000**: 0.1602\n\n### Llama Confusion Matrix (CM) Values\nFrom the cross-model comparison section in qwen_hetero_tau_analysis.md:\n- **Llama Δ_FPR (max-min)**: 0.2190\n- **Llama Δ_FNR (max-min)**: 0.1290\n- **Mean Δ_error**: 0.1740\n\nThese values represent the heterogeneity in Llama3.1-8B's classification metrics across the four subgroups."
      }
    ],
    "totalDurationMs": 12732,
    "totalTokens": 28773,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 4406,
      "cache_creation_input_tokens": 3864,
      "cache_read_input_tokens": 20002,
      "output_tokens": 501,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3864
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4406,
          "output_tokens": 501,
          "cache_read_input_tokens": 20002,
          "cache_creation_input_tokens": 3864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3864,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 2,
      "bashCount": 4,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "ce60d46f-7b10-434a-8855-e17c88976b13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-22T00:15:27.625Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me create the Mistral version by replacing the CM parameters and model-specific labels. The structure is identical to the Qwen template.

Key changes:
1. SUBGROUP_CM → Mistral values
2. Model name labels → Mistral-7B-v0.3
3. Output filenames → mistral_*
4. LLAMA_RESULTS and LLAMA_CM remain the same (for cross-model comparison)
5. Cross-model comparison section labels → Mistral vs Llama


6. Now generating the file...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f625a28a-3a58-4be0-a869-450bba8bfcc2",
  "isSidechain": false,
  "requestId": "req_011CbGeHAbzxDpY9P3WRuNeL",
  "type": "assistant",
  "uuid": "7149f55b-03c4-4c33-8fa9-ec23dac0ba33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bqW4eFzuBTNUokjTCaUhV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 500,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 32033,
      "output_tokens": 12317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 896,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 500,
          "output_tokens": 12317,
          "cache_read_input_tokens": 32033,
          "cache_creation_input_tokens": 896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 896
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

_source line 19 · 2026-05-22T00:15:27.626Z_

Creating the Mistral script now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7149f55b-03c4-4c33-8fa9-ec23dac0ba33",
  "isSidechain": false,
  "requestId": "req_011CbGeHAbzxDpY9P3WRuNeL",
  "type": "assistant",
  "uuid": "61a0464f-f880-45b7-8acd-46dac36f2e47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bqW4eFzuBTNUokjTCaUhV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 500,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 32033,
      "output_tokens": 12317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 896,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 500,
          "output_tokens": 12317,
          "cache_read_input_tokens": 32033,
          "cache_creation_input_tokens": 896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 896
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

_source line 20 · 2026-05-22T00:18:02.178Z_

<details open><summary>🔧 Tool call — Write · `toolu_01XKqjUL4AfWRqB7C7E4Pc2g`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_mistral_hetero_tau.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nHeterogeneous-τ DGP experiment with Mistral-7B-v0.3 confusion matrices.\nMirrors run_hetero_tau.py (Llama) but uses Mistral per-subgroup FPR/FNR.\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [200, 500, 1000]\nN_MC = 50\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']\nSUBGROUP_WEIGHTS = np.array([0.3816, 0.2224, 0.2551, 0.1408])\nSUBGROUP_WEIGHTS = SUBGROUP_WEIGHTS / SUBGROUP_WEIGHTS.sum()\n\nSUBGROUP_CM = {\n    'False_medium': {'fpr': 0.1800, 'fnr': 0.2989},\n    'False_short':  {'fpr': 0.2414, 'fnr': 0.1875},\n    'True_medium':  {'fpr': 0.2333, 'fnr': 0.1684},\n    'True_short':   {'fpr': 0.0909, 'fnr': 0.1207},\n}\n\nSUBGROUP_TAU = {\n    'True_short':   {'tau_z0': 0.2,  'tau_z1': 0.8},\n    'True_medium':  {'tau_z0': 0.35, 'tau_z1': 0.65},\n    'False_short':  {'tau_z0': 0.4,  'tau_z1': 0.5},\n    'False_medium': {'tau_z0': 0.45, 'tau_z1': 0.55},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\n\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === MAP-EB ===\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):\n    hp_rate = 1.0 / hp_scale\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = hp_shape * hp_scale\n            continue\n\n        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):\n            nll = _dirmult_neg_ll(a, _cl)\n            if a < 1e-10:\n                return 1e10\n            log_prior = (_shape - 1.0) * np.log(a) - _rate * a\n            return nll - log_prior\n\n        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n_sz = counts[i, z, :].sum()\n            d = n_sz + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    return C, alpha_opt\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\n# === DGP (heterogeneous tau) ===\n\ndef generate_data(seed, n_expert):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.zeros(N)\n    for i, s in enumerate(SUBGROUP_LABELS):\n        s_mask = S_idx == i\n        tau_s = SUBGROUP_TAU[s]\n        tau_vals[s_mask] = np.where(Z[s_mask] == 1, tau_s['tau_z1'], tau_s['tau_z0'])\n\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_map_eb(counts, SUBGROUP_LABELS)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n        tau_s = SUBGROUP_TAU[s_val]\n\n        for z_level in [0, 1]:\n            oracle_cate = tau_s['tau_z1'] if z_level == 1 else tau_s['tau_z0']\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_w_nv = 2 * 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_est': th_nv, 'cate_true': oracle_cate,\n                'coverage': cov_nv, 'ci_width': ci_w_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_w_gc = 2 * 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_est': th_gc, 'cate_true': oracle_cate,\n                'coverage': cov_gc, 'ci_width': ci_w_gc,\n            })\n\n            # Stratified MLE\n            ci_w_ml = 2 * 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_est': th_ml, 'cate_true': oracle_cate,\n                'coverage': cov_ml, 'ci_width': ci_w_ml,\n            })\n\n            # HB EC-HTE (MAP-EB)\n            ci_w_hb = 2 * 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_est': th_hb, 'cate_true': oracle_cate,\n                'coverage': cov_hb, 'ci_width': ci_w_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef compute_corrected_abs_bias(df):\n    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']\n                 .mean().abs().reset_index(name='abs_mean_bias'))\n    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']\n            .mean().reset_index(name='abs_bias'))\n\n\ndef compute_rmse(df):\n    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)\n                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']\n                 .mean().apply(np.sqrt).reset_index(name='rmse'))\n    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']\n            .mean().reset_index(name='rmse'))\n\n\ndef compute_coverage(df):\n    return (df.groupby(['n_expert', 'method'])['coverage']\n            .mean().reset_index(name='coverage'))\n\n\ndef compute_ci_width(df):\n    return (df.groupby(['n_expert', 'method'])['ci_width']\n            .mean().reset_index(name='ci_width'))\n\n\n# === Analysis Report ===\n\nLLAMA_RESULTS = {\n    200:  {'global_bias': 0.0365, 'echte_bias': 0.0248, 'global_rmse': 0.1780, 'echte_rmse': 0.2606},\n    500:  {'global_bias': 0.0314, 'echte_bias': 0.0099, 'global_rmse': 0.1580, 'echte_rmse': 0.1760},\n    1000: {'global_bias': 0.0286, 'echte_bias': 0.0130, 'global_rmse': 0.1554, 'echte_rmse': 0.1602},\n}\n\nLLAMA_CM = {\n    'False_medium': {'fpr': 0.235, 'fnr': 0.319},\n    'False_short':  {'fpr': 0.310, 'fnr': 0.212},\n    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},\n    'True_short':   {'fpr': 0.091, 'fnr': 0.190},\n}\n\n\ndef write_analysis(df_raw, outpath):\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse = compute_rmse(df_raw)\n    cov = compute_coverage(df_raw)\n    ciw = compute_ci_width(df_raw)\n\n    summary = abs_bias.merge(rmse, on=['n_expert', 'method']).merge(\n        cov, on=['n_expert', 'method']).merge(ciw, on=['n_expert', 'method'])\n\n    lines = []\n    lines.append(\"# Mistral-7B-v0.3 Heterogeneous-τ DGP: EC-HTE vs Global Correction\\n\")\n    lines.append(\"## Design\\n\")\n    lines.append(f\"- N={N}, P(Z=1)={P_Z1}, K=4 subgroups\")\n    lines.append(\"- **LLM**: Mistral-7B-v0.3 (balanced binarization)\")\n    lines.append(\"- **Heterogeneous τ(z) across subgroups:**\")\n    for s in SUBGROUP_LABELS:\n        t = SUBGROUP_TAU[s]\n        lines.append(f\"  - {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}\")\n    lines.append(f\"- n_expert sweep: {N_EXPERT_LIST}\")\n    lines.append(f\"- {N_MC} MC seeds per budget\")\n    lines.append(\"- HB method: MAP-EB (Gamma(3,1) prior)\")\n    lines.append(f\"- |Bias| = avg across cells of |mean(bias) across seeds|\")\n    lines.append(f\"- RMSE = avg across cells of sqrt(mean(bias²) across seeds)\")\n    lines.append(\"\")\n\n    # Mistral CM table\n    lines.append(\"## Mistral-7B-v0.3 Per-Subgroup Confusion Matrix\\n\")\n    lines.append(\"| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |\")\n    lines.append(\"|----------|-----|-----|-----|-----------|\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        w = SUBGROUP_WEIGHTS[SUBGROUP_LABELS.index(s)]\n        lines.append(f\"| {s} | {w:.4f} | {cm['fpr']:.4f} | {cm['fnr']:.4f} | {1-cm['fpr']-cm['fnr']:.4f} |\")\n    lines.append(\"\")\n    mistral_fpr_range = max(cm['fpr'] for cm in SUBGROUP_CM.values()) - min(cm['fpr'] for cm in SUBGROUP_CM.values())\n    mistral_fnr_range = max(cm['fnr'] for cm in SUBGROUP_CM.values()) - min(cm['fnr'] for cm in SUBGROUP_CM.values())\n    llama_fpr_range = max(cm['fpr'] for cm in LLAMA_CM.values()) - min(cm['fpr'] for cm in LLAMA_CM.values())\n    llama_fnr_range = max(cm['fnr'] for cm in LLAMA_CM.values()) - min(cm['fnr'] for cm in LLAMA_CM.values())\n    lines.append(f\"- Mistral Δ_FPR = {mistral_fpr_range:.4f}, Δ_FNR = {mistral_fnr_range:.4f}\")\n    lines.append(f\"- Llama Δ_FPR = {llama_fpr_range:.4f}, Δ_FNR = {llama_fnr_range:.4f}\")\n    lines.append(f\"- Mistral has {'larger' if mistral_fpr_range > llama_fpr_range else 'smaller'} FPR heterogeneity \"\n                 f\"and {'larger' if mistral_fnr_range > llama_fnr_range else 'smaller'} FNR heterogeneity than Llama\")\n    lines.append(\"\")\n\n    # Summary table\n    lines.append(\"## Summary Table (averaged across all cells)\\n\")\n    lines.append(\"| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |\")\n    lines.append(\"|----------|--------|-------|------|----------|----------|\")\n\n    method_order = ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']\n    method_labels = {'naive': 'Naive', 'global_corrected': 'Global', 'stratified_mle': 'Strat MLE', 'hb_ec_hte': 'HB EC-HTE'}\n\n    for ne in N_EXPERT_LIST:\n        for m in method_order:\n            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n            if len(row) > 0:\n                r = row.iloc[0]\n                lines.append(f\"| {ne} | {method_labels[m]} | {r['abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} | {r['ci_width']:.3f} |\")\n        lines.append(\"|----------|--------|-------|------|----------|----------|\")\n    lines.append(\"\")\n\n    # EC-HTE vs Global comparison\n    lines.append(\"## EC-HTE vs Global Comparison\\n\")\n    lines.append(\"| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |\")\n    lines.append(\"|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        gc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        hb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        d_bias = gc['abs_bias'] - hb['abs_bias']\n        d_rmse = gc['rmse'] - hb['rmse']\n        wb = \"**YES**\" if hb['abs_bias'] < gc['abs_bias'] else \"no\"\n        wr = \"**YES**\" if hb['rmse'] < gc['rmse'] else \"no\"\n        lines.append(f\"| {ne} | {gc['abs_bias']:.4f} | {hb['abs_bias']:.4f} | {d_bias:+.4f} | {gc['rmse']:.4f} | {hb['rmse']:.4f} | {d_rmse:+.4f} | {wb} | {wr} |\")\n    lines.append(\"\")\n\n    # Per-subgroup breakdown\n    lines.append(\"## Per-Subgroup Breakdown\\n\")\n    for ne in N_EXPERT_LIST:\n        lines.append(f\"### n_expert = {ne}\\n\")\n        lines.append(\"| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\")\n        lines.append(\"|----------|-----|---|-------------|-------------|-------------|-------------|------------|\")\n        sub_df = df_raw[df_raw['n_expert'] == ne]\n        for s_val in SUBGROUP_LABELS:\n            dt = SUBGROUP_TAU[s_val]['tau_z1'] - SUBGROUP_TAU[s_val]['tau_z0']\n            for z_level in [0, 1]:\n                cell_gc = sub_df[(sub_df['method'] == 'global_corrected') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]\n                cell_hb = sub_df[(sub_df['method'] == 'hb_ec_hte') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]\n                bias_gc = abs(cell_gc['bias'].mean())\n                bias_hb = abs(cell_hb['bias'].mean())\n                rmse_gc = np.sqrt((cell_gc['bias'] ** 2).mean())\n                rmse_hb = np.sqrt((cell_hb['bias'] ** 2).mean())\n                imp = bias_gc - bias_hb\n                lines.append(f\"| {s_val} | {dt:.1f} | {z_level} | {bias_gc:.4f} | {bias_hb:.4f} | {imp:+.4f} | {rmse_gc:.4f} | {rmse_hb:.4f} |\")\n        lines.append(\"\")\n\n    # Bias-variance decomposition\n    lines.append(\"## Bias-Variance Decomposition\\n\")\n    lines.append(\"| n_expert | Method | Bias² | Variance | MSE |\")\n    lines.append(\"|----------|--------|-------|----------|-----|\")\n    for ne in N_EXPERT_LIST:\n        for m in method_order:\n            sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]\n            cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']\n                          .agg(['mean', 'var', 'count']).reset_index())\n            mean_bias_sq = (cell_stats['mean'] ** 2).mean()\n            variance = cell_stats['var'].mean()\n            mse = mean_bias_sq + variance\n            lines.append(f\"| {ne} | {method_labels[m]} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |\")\n    lines.append(\"\")\n\n    # Cross-model comparison with Llama\n    lines.append(\"## Cross-Model Comparison: Mistral vs Llama (exp-023)\\n\")\n    lines.append(\"### CM Heterogeneity\\n\")\n    lines.append(\"| Metric | Mistral-7B-v0.3 | Llama3.1-8B |\")\n    lines.append(\"|--------|----------------|------------|\")\n    lines.append(f\"| Δ_FPR (max-min) | {mistral_fpr_range:.4f} | {llama_fpr_range:.4f} |\")\n    lines.append(f\"| Δ_FNR (max-min) | {mistral_fnr_range:.4f} | {llama_fnr_range:.4f} |\")\n    lines.append(f\"| Mean Δ_error | {(mistral_fpr_range+mistral_fnr_range)/2:.4f} | {(llama_fpr_range+llama_fnr_range)/2:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Bias Comparison\\n\")\n    lines.append(\"| n_expert | Mistral |Bias|_Global | Mistral |Bias|_ECHTE | Mistral Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |\")\n    lines.append(\"|----------|------------------|--------------------|--------------|--------------------|--------------------|---------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        mgc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        mhb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        md = mgc['abs_bias'] - mhb['abs_bias']\n        lr = LLAMA_RESULTS[ne]\n        ld = lr['global_bias'] - lr['echte_bias']\n        lines.append(f\"| {ne} | {mgc['abs_bias']:.4f} | {mhb['abs_bias']:.4f} | {md:+.4f} | {lr['global_bias']:.4f} | {lr['echte_bias']:.4f} | {ld:+.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### RMSE Comparison\\n\")\n    lines.append(\"| n_expert | Mistral RMSE_Global | Mistral RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |\")\n    lines.append(\"|----------|-----------------|----------------|------------------|-----------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        mgc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        mhb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        lr = LLAMA_RESULTS[ne]\n        lines.append(f\"| {ne} | {mgc['rmse']:.4f} | {mhb['rmse']:.4f} | {lr['global_rmse']:.4f} | {lr['echte_rmse']:.4f} |\")\n    lines.append(\"\")\n\n    # Conclusion\n    lines.append(\"## Conclusion\\n\")\n    gc_all = summary[summary['method'] == 'global_corrected']\n    hb_all = summary[summary['method'] == 'hb_ec_hte']\n    n_bias_wins = 0\n    n_rmse_wins = 0\n    for ne in N_EXPERT_LIST:\n        gc_row = gc_all[gc_all['n_expert'] == ne].iloc[0]\n        hb_row = hb_all[hb_all['n_expert'] == ne].iloc[0]\n        if hb_row['abs_bias'] < gc_row['abs_bias']:\n            n_bias_wins += 1\n        if hb_row['rmse'] < gc_row['rmse']:\n            n_rmse_wins += 1\n\n    lines.append(f\"EC-HTE wins on |Bias| in {n_bias_wins}/{len(N_EXPERT_LIST)} budget levels.\")\n    lines.append(f\"EC-HTE wins on RMSE in {n_rmse_wins}/{len(N_EXPERT_LIST)} budget levels.\\n\")\n\n    if n_bias_wins == len(N_EXPERT_LIST):\n        lines.append(\"**Result: Under heterogeneous-τ DGP with Mistral-7B-v0.3 CMs, EC-HTE consistently outperforms Global correction in bias.**\\n\")\n    elif n_bias_wins > 0:\n        lines.append(f\"**Result: Under heterogeneous-τ DGP with Mistral-7B-v0.3 CMs, EC-HTE outperforms Global in bias at {n_bias_wins} of {len(N_EXPERT_LIST)} budget levels.**\\n\")\n    else:\n        lines.append(\"**Result: EC-HTE does not outperform Global in bias under this DGP configuration with Mistral CMs.**\\n\")\n\n    # Cross-model conclusion\n    llama_bias_wins = sum(1 for ne in N_EXPERT_LIST if LLAMA_RESULTS[ne]['echte_bias'] < LLAMA_RESULTS[ne]['global_bias'])\n    lines.append(f\"**Cross-model consistency**: Llama EC-HTE wins on bias in {llama_bias_wins}/3 budgets; \"\n                 f\"Mistral EC-HTE wins in {n_bias_wins}/3 budgets.\")\n    if n_bias_wins == len(N_EXPERT_LIST) and llama_bias_wins == len(N_EXPERT_LIST):\n        lines.append(\"EC-HTE's bias advantage is consistent across both Llama and Mistral models.\")\n    lines.append(\"\")\n\n    avg_mistral_improvement = np.mean([\n        (summary[(summary['n_expert']==ne) & (summary['method']=='global_corrected')].iloc[0]['abs_bias'] -\n         summary[(summary['n_expert']==ne) & (summary['method']=='hb_ec_hte')].iloc[0]['abs_bias'])\n        for ne in N_EXPERT_LIST\n    ])\n    avg_llama_improvement = np.mean([\n        LLAMA_RESULTS[ne]['global_bias'] - LLAMA_RESULTS[ne]['echte_bias']\n        for ne in N_EXPERT_LIST\n    ])\n    lines.append(f\"Average Δ|Bias| (Global - EC-HTE): Mistral = {avg_mistral_improvement:+.4f}, Llama = {avg_llama_improvement:+.4f}\")\n    if avg_mistral_improvement > avg_llama_improvement:\n        lines.append(f\"Mistral shows larger EC-HTE improvement, consistent with its greater CM heterogeneity \"\n                     f\"(Δ_FPR={mistral_fpr_range:.3f} vs {llama_fpr_range:.3f}).\")\n    else:\n        lines.append(f\"Llama shows larger EC-HTE improvement despite smaller CM heterogeneity.\")\n    lines.append(\"\")\n\n    report = \"\\n\".join(lines)\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"Mistral-7B-v0.3 Heterogeneous-τ DGP: EC-HTE vs Global\")\n    print(f\"N={N}, budgets={N_EXPERT_LIST}, seeds={N_MC}\")\n    print(\"Mistral per-subgroup CM:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.4f}, FNR={cm['fnr']:.4f}\")\n    print(\"Subgroup τ values:\")\n    for s in SUBGROUP_LABELS:\n        t = SUBGROUP_TAU[s]\n        print(f\"  {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}\")\n    print()\n\n    out_dir = 'artifacts/c1_multi_llm'\n\n    # Dry run: 1 budget, 1 seed\n    print(\"=== Dry run (n_expert=200, 1 seed) ===\")\n    data = generate_data(SEED_BASE, 200)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    df_dry['n_expert'] = 200\n    print(f\"Dry run OK: {len(df_dry)} rows, columns: {list(df_dry.columns)}\")\n    for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n\n    # Verify oracle CATE values\n    print(\"\\n  Oracle CATE check:\")\n    for s_val in SUBGROUP_LABELS:\n        for zl in [0, 1]:\n            cell = df_dry[(df_dry['subgroup'] == s_val) & (df_dry['z_level'] == zl)]\n            true_val = cell['cate_true'].iloc[0]\n            expected = SUBGROUP_TAU[s_val]['tau_z1'] if zl == 1 else SUBGROUP_TAU[s_val]['tau_z0']\n            ok = \"OK\" if abs(true_val - expected) < 1e-10 else \"MISMATCH\"\n            print(f\"    {s_val} z={zl}: cate_true={true_val:.2f} expected={expected:.2f} [{ok}]\")\n    print()\n\n    # Full run\n    print(f\"=== Full run ({len(N_EXPERT_LIST)} budgets x {N_MC} seeds) ===\")\n    all_results = []\n    t0 = time.time()\n    total_runs = len(N_EXPERT_LIST) * N_MC\n    run_count = 0\n\n    for n_expert in N_EXPERT_LIST:\n        print(f\"\\n--- n_expert = {n_expert} ---\")\n        t_budget = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, n_expert)\n            mc_rows = run_one_mc(data, seed)\n            for r in mc_rows:\n                r['n_expert'] = n_expert\n            all_results.extend(mc_rows)\n            run_count += 1\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / run_count * (total_runs - run_count)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n        budget_time = time.time() - t_budget\n        print(f\"  n_expert={n_expert} done in {budget_time:.1f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n\n    # Save results CSV\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width']\n    df_raw[col_order].to_csv(f'{out_dir}/mistral_hetero_tau_results.csv', index=False)\n    print(f\"Saved mistral_hetero_tau_results.csv ({len(df_raw)} rows)\")\n\n    # Write analysis\n    write_analysis(df_raw, f'{out_dir}/mistral_hetero_tau_analysis.md')\n\n    # Print summary\n    print(\"\\n=== Summary ===\")\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse_df = compute_rmse(df_raw)\n    summary = abs_bias.merge(rmse_df, on=['n_expert', 'method'])\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n  n_expert={ne}:\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n            if len(row) > 0:\n                print(f\"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}\")\n    print()\n\n    # EC-HTE vs Global\n    print(\"=== EC-HTE vs Global (Mistral) ===\")\n    for ne in N_EXPERT_LIST:\n        gc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]\n        hb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]\n        print(f\"  n_expert={ne}: |Bias| Global={gc['abs_bias']:.4f} vs ECHTE={hb['abs_bias']:.4f} \"\n              f\"({'ECHTE wins' if hb['abs_bias'] < gc['abs_bias'] else 'Global wins'})\")\n        print(f\"              RMSE  Global={gc['rmse']:.4f} vs ECHTE={hb['rmse']:.4f} \"\n              f\"({'ECHTE wins' if hb['rmse'] < gc['rmse'] else 'Global wins'})\")\n\n    # Cross-model comparison\n    print(\"\\n=== Cross-Model: Mistral vs Llama ===\")\n    for ne in N_EXPERT_LIST:\n        mgc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]\n        mhb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]\n        lr = LLAMA_RESULTS[ne]\n        print(f\"  n_expert={ne}:\")\n        print(f\"    Mistral Δ|Bias| = {mgc['abs_bias'] - mhb['abs_bias']:+.4f}\")\n        print(f\"    Llama   Δ|Bias| = {lr['global_bias'] - lr['echte_bias']:+.4f}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61a0464f-f880-45b7-8acd-46dac36f2e47",
  "isSidechain": false,
  "requestId": "req_011CbGeHAbzxDpY9P3WRuNeL",
  "type": "assistant",
  "uuid": "e1a5d75d-622e-4083-94e6-667370dc8a20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018bqW4eFzuBTNUokjTCaUhV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 500,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 32033,
      "output_tokens": 12317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 896,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 500,
          "output_tokens": 12317,
          "cache_read_input_tokens": 32033,
          "cache_creation_input_tokens": 896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 896
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

_source line 21 · 2026-05-22T00:18:02.211Z_

<details><summary>↩ Tool result · `toolu_01XKqjUL4AfWRqB7C7E4Pc2g`</summary>

```text
File created successfully at: /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_mistral_hetero_tau.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1a5d75d-622e-4083-94e6-667370dc8a20",
  "isSidechain": false,
  "promptId": "695fc122-00c0-4b11-823d-9471ae018801",
  "type": "user",
  "uuid": "09051d43-2ba7-4776-a8e9-bdaa15f137b6",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_mistral_hetero_tau.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nHeterogeneous-τ DGP experiment with Mistral-7B-v0.3 confusion matrices.\nMirrors run_hetero_tau.py (Llama) but uses Mistral per-subgroup FPR/FNR.\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [200, 500, 1000]\nN_MC = 50\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']\nSUBGROUP_WEIGHTS = np.array([0.3816, 0.2224, 0.2551, 0.1408])\nSUBGROUP_WEIGHTS = SUBGROUP_WEIGHTS / SUBGROUP_WEIGHTS.sum()\n\nSUBGROUP_CM = {\n    'False_medium': {'fpr': 0.1800, 'fnr': 0.2989},\n    'False_short':  {'fpr': 0.2414, 'fnr': 0.1875},\n    'True_medium':  {'fpr': 0.2333, 'fnr': 0.1684},\n    'True_short':   {'fpr': 0.0909, 'fnr': 0.1207},\n}\n\nSUBGROUP_TAU = {\n    'True_short':   {'tau_z0': 0.2,  'tau_z1': 0.8},\n    'True_medium':  {'tau_z0': 0.35, 'tau_z1': 0.65},\n    'False_short':  {'tau_z0': 0.4,  'tau_z1': 0.5},\n    'False_medium': {'tau_z0': 0.45, 'tau_z1': 0.55},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\n\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === MAP-EB ===\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):\n    hp_rate = 1.0 / hp_scale\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = hp_shape * hp_scale\n            continue\n\n        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):\n            nll = _dirmult_neg_ll(a, _cl)\n            if a < 1e-10:\n                return 1e10\n            log_prior = (_shape - 1.0) * np.log(a) - _rate * a\n            return nll - log_prior\n\n        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n_sz = counts[i, z, :].sum()\n            d = n_sz + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    return C, alpha_opt\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\n# === DGP (heterogeneous tau) ===\n\ndef generate_data(seed, n_expert):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.zeros(N)\n    for i, s in enumerate(SUBGROUP_LABELS):\n        s_mask = S_idx == i\n        tau_s = SUBGROUP_TAU[s]\n        tau_vals[s_mask] = np.where(Z[s_mask] == 1, tau_s['tau_z1'], tau_s['tau_z0'])\n\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_map_eb(counts, SUBGROUP_LABELS)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n        tau_s = SUBGROUP_TAU[s_val]\n\n        for z_level in [0, 1]:\n            oracle_cate = tau_s['tau_z1'] if z_level == 1 else tau_s['tau_z0']\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_w_nv = 2 * 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_est': th_nv, 'cate_true': oracle_cate,\n                'coverage': cov_nv, 'ci_width': ci_w_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_w_gc = 2 * 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_est': th_gc, 'cate_true': oracle_cate,\n                'coverage': cov_gc, 'ci_width': ci_w_gc,\n            })\n\n            # Stratified MLE\n            ci_w_ml = 2 * 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_est': th_ml, 'cate_true': oracle_cate,\n                'coverage': cov_ml, 'ci_width': ci_w_ml,\n            })\n\n            # HB EC-HTE (MAP-EB)\n            ci_w_hb = 2 * 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_est': th_hb, 'cate_true': oracle_cate,\n                'coverage': cov_hb, 'ci_width': ci_w_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef compute_corrected_abs_bias(df):\n    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']\n                 .mean().abs().reset_index(name='abs_mean_bias'))\n    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']\n            .mean().reset_index(name='abs_bias'))\n\n\ndef compute_rmse(df):\n    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)\n                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']\n                 .mean().apply(np.sqrt).reset_index(name='rmse'))\n    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']\n            .mean().reset_index(name='rmse'))\n\n\ndef compute_coverage(df):\n    return (df.groupby(['n_expert', 'method'])['coverage']\n            .mean().reset_index(name='coverage'))\n\n\ndef compute_ci_width(df):\n    return (df.groupby(['n_expert', 'method'])['ci_width']\n            .mean().reset_index(name='ci_width'))\n\n\n# === Analysis Report ===\n\nLLAMA_RESULTS = {\n    200:  {'global_bias': 0.0365, 'echte_bias': 0.0248, 'global_rmse': 0.1780, 'echte_rmse': 0.2606},\n    500:  {'global_bias': 0.0314, 'echte_bias': 0.0099, 'global_rmse': 0.1580, 'echte_rmse': 0.1760},\n    1000: {'global_bias': 0.0286, 'echte_bias': 0.0130, 'global_rmse': 0.1554, 'echte_rmse': 0.1602},\n}\n\nLLAMA_CM = {\n    'False_medium': {'fpr': 0.235, 'fnr': 0.319},\n    'False_short':  {'fpr': 0.310, 'fnr': 0.212},\n    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},\n    'True_short':   {'fpr': 0.091, 'fnr': 0.190},\n}\n\n\ndef write_analysis(df_raw, outpath):\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse = compute_rmse(df_raw)\n    cov = compute_coverage(df_raw)\n    ciw = compute_ci_width(df_raw)\n\n    summary = abs_bias.merge(rmse, on=['n_expert', 'method']).merge(\n        cov, on=['n_expert', 'method']).merge(ciw, on=['n_expert', 'method'])\n\n    lines = []\n    lines.append(\"# Mistral-7B-v0.3 Heterogeneous-τ DGP: EC-HTE vs Global Correction\\n\")\n    lines.append(\"## Design\\n\")\n    lines.append(f\"- N={N}, P(Z=1)={P_Z1}, K=4 subgroups\")\n    lines.append(\"- **LLM**: Mistral-7B-v0.3 (balanced binarization)\")\n    lines.append(\"- **Heterogeneous τ(z) across subgroups:**\")\n    for s in SUBGROUP_LABELS:\n        t = SUBGROUP_TAU[s]\n        lines.append(f\"  - {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}\")\n    lines.append(f\"- n_expert sweep: {N_EXPERT_LIST}\")\n    lines.append(f\"- {N_MC} MC seeds per budget\")\n    lines.append(\"- HB method: MAP-EB (Gamma(3,1) prior)\")\n    lines.append(f\"- |Bias| = avg across cells of |mean(bias) across seeds|\")\n    lines.append(f\"- RMSE = avg across cells of sqrt(mean(bias²) across seeds)\")\n    lines.append(\"\")\n\n    # Mistral CM table\n    lines.append(\"## Mistral-7B-v0.3 Per-Subgroup Confusion Matrix\\n\")\n    lines.append(\"| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |\")\n    lines.append(\"|----------|-----|-----|-----|-----------|\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        w = SUBGROUP_WEIGHTS[SUBGROUP_LABELS.index(s)]\n        lines.append(f\"| {s} | {w:.4f} | {cm['fpr']:.4f} | {cm['fnr']:.4f} | {1-cm['fpr']-cm['fnr']:.4f} |\")\n    lines.append(\"\")\n    mistral_fpr_range = max(cm['fpr'] for cm in SUBGROUP_CM.values()) - min(cm['fpr'] for cm in SUBGROUP_CM.values())\n    mistral_fnr_range = max(cm['fnr'] for cm in SUBGROUP_CM.values()) - min(cm['fnr'] for cm in SUBGROUP_CM.values())\n    llama_fpr_range = max(cm['fpr'] for cm in LLAMA_CM.values()) - min(cm['fpr'] for cm in LLAMA_CM.values())\n    llama_fnr_range = max(cm['fnr'] for cm in LLAMA_CM.values()) - min(cm['fnr'] for cm in LLAMA_CM.values())\n    lines.append(f\"- Mistral Δ_FPR = {mistral_fpr_range:.4f}, Δ_FNR = {mistral_fnr_range:.4f}\")\n    lines.append(f\"- Llama Δ_FPR = {llama_fpr_range:.4f}, Δ_FNR = {llama_fnr_range:.4f}\")\n    lines.append(f\"- Mistral has {'larger' if mistral_fpr_range > llama_fpr_range else 'smaller'} FPR heterogeneity \"\n                 f\"and {'larger' if mistral_fnr_range > llama_fnr_range else 'smaller'} FNR heterogeneity than Llama\")\n    lines.append(\"\")\n\n    # Summary table\n    lines.append(\"## Summary Table (averaged across all cells)\\n\")\n    lines.append(\"| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |\")\n    lines.append(\"|----------|--------|-------|------|----------|----------|\")\n\n    method_order = ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']\n    method_labels = {'naive': 'Naive', 'global_corrected': 'Global', 'stratified_mle': 'Strat MLE', 'hb_ec_hte': 'HB EC-HTE'}\n\n    for ne in N_EXPERT_LIST:\n        for m in method_order:\n            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n            if len(row) > 0:\n                r = row.iloc[0]\n                lines.append(f\"| {ne} | {method_labels[m]} | {r['abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} | {r['ci_width']:.3f} |\")\n        lines.append(\"|----------|--------|-------|------|----------|----------|\")\n    lines.append(\"\")\n\n    # EC-HTE vs Global comparison\n    lines.append(\"## EC-HTE vs Global Comparison\\n\")\n    lines.append(\"| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |\")\n    lines.append(\"|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        gc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        hb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        d_bias = gc['abs_bias'] - hb['abs_bias']\n        d_rmse = gc['rmse'] - hb['rmse']\n        wb = \"**YES**\" if hb['abs_bias'] < gc['abs_bias'] else \"no\"\n        wr = \"**YES**\" if hb['rmse'] < gc['rmse'] else \"no\"\n        lines.append(f\"| {ne} | {gc['abs_bias']:.4f} | {hb['abs_bias']:.4f} | {d_bias:+.4f} | {gc['rmse']:.4f} | {hb['rmse']:.4f} | {d_rmse:+.4f} | {wb} | {wr} |\")\n    lines.append(\"\")\n\n    # Per-subgroup breakdown\n    lines.append(\"## Per-Subgroup Breakdown\\n\")\n    for ne in N_EXPERT_LIST:\n        lines.append(f\"### n_expert = {ne}\\n\")\n        lines.append(\"| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\")\n        lines.append(\"|----------|-----|---|-------------|-------------|-------------|-------------|------------|\")\n        sub_df = df_raw[df_raw['n_expert'] == ne]\n        for s_val in SUBGROUP_LABELS:\n            dt = SUBGROUP_TAU[s_val]['tau_z1'] - SUBGROUP_TAU[s_val]['tau_z0']\n            for z_level in [0, 1]:\n                cell_gc = sub_df[(sub_df['method'] == 'global_corrected') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]\n                cell_hb = sub_df[(sub_df['method'] == 'hb_ec_hte') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]\n                bias_gc = abs(cell_gc['bias'].mean())\n                bias_hb = abs(cell_hb['bias'].mean())\n                rmse_gc = np.sqrt((cell_gc['bias'] ** 2).mean())\n                rmse_hb = np.sqrt((cell_hb['bias'] ** 2).mean())\n                imp = bias_gc - bias_hb\n                lines.append(f\"| {s_val} | {dt:.1f} | {z_level} | {bias_gc:.4f} | {bias_hb:.4f} | {imp:+.4f} | {rmse_gc:.4f} | {rmse_hb:.4f} |\")\n        lines.append(\"\")\n\n    # Bias-variance decomposition\n    lines.append(\"## Bias-Variance Decomposition\\n\")\n    lines.append(\"| n_expert | Method | Bias² | Variance | MSE |\")\n    lines.append(\"|----------|--------|-------|----------|-----|\")\n    for ne in N_EXPERT_LIST:\n        for m in method_order:\n            sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]\n            cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']\n                          .agg(['mean', 'var', 'count']).reset_index())\n            mean_bias_sq = (cell_stats['mean'] ** 2).mean()\n            variance = cell_stats['var'].mean()\n            mse = mean_bias_sq + variance\n            lines.append(f\"| {ne} | {method_labels[m]} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |\")\n    lines.append(\"\")\n\n    # Cross-model comparison with Llama\n    lines.append(\"## Cross-Model Comparison: Mistral vs Llama (exp-023)\\n\")\n    lines.append(\"### CM Heterogeneity\\n\")\n    lines.append(\"| Metric | Mistral-7B-v0.3 | Llama3.1-8B |\")\n    lines.append(\"|--------|----------------|------------|\")\n    lines.append(f\"| Δ_FPR (max-min) | {mistral_fpr_range:.4f} | {llama_fpr_range:.4f} |\")\n    lines.append(f\"| Δ_FNR (max-min) | {mistral_fnr_range:.4f} | {llama_fnr_range:.4f} |\")\n    lines.append(f\"| Mean Δ_error | {(mistral_fpr_range+mistral_fnr_range)/2:.4f} | {(llama_fpr_range+llama_fnr_range)/2:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Bias Comparison\\n\")\n    lines.append(\"| n_expert | Mistral |Bias|_Global | Mistral |Bias|_ECHTE | Mistral Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |\")\n    lines.append(\"|----------|------------------|--------------------|--------------|--------------------|--------------------|---------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        mgc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        mhb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        md = mgc['abs_bias'] - mhb['abs_bias']\n        lr = LLAMA_RESULTS[ne]\n        ld = lr['global_bias'] - lr['echte_bias']\n        lines.append(f\"| {ne} | {mgc['abs_bias']:.4f} | {mhb['abs_bias']:.4f} | {md:+.4f} | {lr['global_bias']:.4f} | {lr['echte_bias']:.4f} | {ld:+.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### RMSE Comparison\\n\")\n    lines.append(\"| n_expert | Mistral RMSE_Global | Mistral RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |\")\n    lines.append(\"|----------|-----------------|----------------|------------------|-----------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        mgc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        mhb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        lr = LLAMA_RESULTS[ne]\n        lines.append(f\"| {ne} | {mgc['rmse']:.4f} | {mhb['rmse']:.4f} | {lr['global_rmse']:.4f} | {lr['echte_rmse']:.4f} |\")\n    lines.append(\"\")\n\n    # Conclusion\n    lines.append(\"## Conclusion\\n\")\n    gc_all = summary[summary['method'] == 'global_corrected']\n    hb_all = summary[summary['method'] == 'hb_ec_hte']\n    n_bias_wins = 0\n    n_rmse_wins = 0\n    for ne in N_EXPERT_LIST:\n        gc_row = gc_all[gc_all['n_expert'] == ne].iloc[0]\n        hb_row = hb_all[hb_all['n_expert'] == ne].iloc[0]\n        if hb_row['abs_bias'] < gc_row['abs_bias']:\n            n_bias_wins += 1\n        if hb_row['rmse'] < gc_row['rmse']:\n            n_rmse_wins += 1\n\n    lines.append(f\"EC-HTE wins on |Bias| in {n_bias_wins}/{len(N_EXPERT_LIST)} budget levels.\")\n    lines.append(f\"EC-HTE wins on RMSE in {n_rmse_wins}/{len(N_EXPERT_LIST)} budget levels.\\n\")\n\n    if n_bias_wins == len(N_EXPERT_LIST):\n        lines.append(\"**Result: Under heterogeneous-τ DGP with Mistral-7B-v0.3 CMs, EC-HTE consistently outperforms Global correction in bias.**\\n\")\n    elif n_bias_wins > 0:\n        lines.append(f\"**Result: Under heterogeneous-τ DGP with Mistral-7B-v0.3 CMs, EC-HTE outperforms Global in bias at {n_bias_wins} of {len(N_EXPERT_LIST)} budget levels.**\\n\")\n    else:\n        lines.append(\"**Result: EC-HTE does not outperform Global in bias under this DGP configuration with Mistral CMs.**\\n\")\n\n    # Cross-model conclusion\n    llama_bias_wins = sum(1 for ne in N_EXPERT_LIST if LLAMA_RESULTS[ne]['echte_bias'] < LLAMA_RESULTS[ne]['global_bias'])\n    lines.append(f\"**Cross-model consistency**: Llama EC-HTE wins on bias in {llama_bias_wins}/3 budgets; \"\n                 f\"Mistral EC-HTE wins in {n_bias_wins}/3 budgets.\")\n    if n_bias_wins == len(N_EXPERT_LIST) and llama_bias_wins == len(N_EXPERT_LIST):\n        lines.append(\"EC-HTE's bias advantage is consistent across both Llama and Mistral models.\")\n    lines.append(\"\")\n\n    avg_mistral_improvement = np.mean([\n        (summary[(summary['n_expert']==ne) & (summary['method']=='global_corrected')].iloc[0]['abs_bias'] -\n         summary[(summary['n_expert']==ne) & (summary['method']=='hb_ec_hte')].iloc[0]['abs_bias'])\n        for ne in N_EXPERT_LIST\n    ])\n    avg_llama_improvement = np.mean([\n        LLAMA_RESULTS[ne]['global_bias'] - LLAMA_RESULTS[ne]['echte_bias']\n        for ne in N_EXPERT_LIST\n    ])\n    lines.append(f\"Average Δ|Bias| (Global - EC-HTE): Mistral = {avg_mistral_improvement:+.4f}, Llama = {avg_llama_improvement:+.4f}\")\n    if avg_mistral_improvement > avg_llama_improvement:\n        lines.append(f\"Mistral shows larger EC-HTE improvement, consistent with its greater CM heterogeneity \"\n                     f\"(Δ_FPR={mistral_fpr_range:.3f} vs {llama_fpr_range:.3f}).\")\n    else:\n        lines.append(f\"Llama shows larger EC-HTE improvement despite smaller CM heterogeneity.\")\n    lines.append(\"\")\n\n    report = \"\\n\".join(lines)\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"Mistral-7B-v0.3 Heterogeneous-τ DGP: EC-HTE vs Global\")\n    print(f\"N={N}, budgets={N_EXPERT_LIST}, seeds={N_MC}\")\n    print(\"Mistral per-subgroup CM:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.4f}, FNR={cm['fnr']:.4f}\")\n    print(\"Subgroup τ values:\")\n    for s in SUBGROUP_LABELS:\n        t = SUBGROUP_TAU[s]\n        print(f\"  {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}\")\n    print()\n\n    out_dir = 'artifacts/c1_multi_llm'\n\n    # Dry run: 1 budget, 1 seed\n    print(\"=== Dry run (n_expert=200, 1 seed) ===\")\n    data = generate_data(SEED_BASE, 200)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    df_dry['n_expert'] = 200\n    print(f\"Dry run OK: {len(df_dry)} rows, columns: {list(df_dry.columns)}\")\n    for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n\n    # Verify oracle CATE values\n    print(\"\\n  Oracle CATE check:\")\n    for s_val in SUBGROUP_LABELS:\n        for zl in [0, 1]:\n            cell = df_dry[(df_dry['subgroup'] == s_val) & (df_dry['z_level'] == zl)]\n            true_val = cell['cate_true'].iloc[0]\n            expected = SUBGROUP_TAU[s_val]['tau_z1'] if zl == 1 else SUBGROUP_TAU[s_val]['tau_z0']\n            ok = \"OK\" if abs(true_val - expected) < 1e-10 else \"MISMATCH\"\n            print(f\"    {s_val} z={zl}: cate_true={true_val:.2f} expected={expected:.2f} [{ok}]\")\n    print()\n\n    # Full run\n    print(f\"=== Full run ({len(N_EXPERT_LIST)} budgets x {N_MC} seeds) ===\")\n    all_results = []\n    t0 = time.time()\n    total_runs = len(N_EXPERT_LIST) * N_MC\n    run_count = 0\n\n    for n_expert in N_EXPERT_LIST:\n        print(f\"\\n--- n_expert = {n_expert} ---\")\n        t_budget = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, n_expert)\n            mc_rows = run_one_mc(data, seed)\n            for r in mc_rows:\n                r['n_expert'] = n_expert\n            all_results.extend(mc_rows)\n            run_count += 1\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / run_count * (total_runs - run_count)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n        budget_time = time.time() - t_budget\n        print(f\"  n_expert={n_expert} done in {budget_time:.1f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n\n    # Save results CSV\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width']\n    df_raw[col_order].to_csv(f'{out_dir}/mistral_hetero_tau_results.csv', index=False)\n    print(f\"Saved mistral_hetero_tau_results.csv ({len(df_raw)} rows)\")\n\n    # Write analysis\n    write_analysis(df_raw, f'{out_dir}/mistral_hetero_tau_analysis.md')\n\n    # Print summary\n    print(\"\\n=== Summary ===\")\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse_df = compute_rmse(df_raw)\n    summary = abs_bias.merge(rmse_df, on=['n_expert', 'method'])\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n  n_expert={ne}:\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n            if len(row) > 0:\n                print(f\"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}\")\n    print()\n\n    # EC-HTE vs Global\n    print(\"=== EC-HTE vs Global (Mistral) ===\")\n    for ne in N_EXPERT_LIST:\n        gc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]\n        hb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]\n        print(f\"  n_expert={ne}: |Bias| Global={gc['abs_bias']:.4f} vs ECHTE={hb['abs_bias']:.4f} \"\n              f\"({'ECHTE wins' if hb['abs_bias'] < gc['abs_bias'] else 'Global wins'})\")\n        print(f\"              RMSE  Global={gc['rmse']:.4f} vs ECHTE={hb['rmse']:.4f} \"\n              f\"({'ECHTE wins' if hb['rmse'] < gc['rmse'] else 'Global wins'})\")\n\n    # Cross-model comparison\n    print(\"\\n=== Cross-Model: Mistral vs Llama ===\")\n    for ne in N_EXPERT_LIST:\n        mgc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]\n        mhb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]\n        lr = LLAMA_RESULTS[ne]\n        print(f\"  n_expert={ne}:\")\n        print(f\"    Mistral Δ|Bias| = {mgc['abs_bias'] - mhb['abs_bias']:+.4f}\")\n        print(f\"    Llama   Δ|Bias| = {lr['global_bias'] - lr['echte_bias']:+.4f}\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "e1a5d75d-622e-4083-94e6-667370dc8a20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "leafUuid": "09051d43-2ba7-4776-a8e9-bdaa15f137b6",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Mistral-7B heterogeneous-τ DGP experiment",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8"
}
```

---

### Assistant

_source line 24 · 2026-05-22T00:18:04.094Z_

Script created. Running it now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09051d43-2ba7-4776-a8e9-bdaa15f137b6",
  "isSidechain": false,
  "requestId": "req_011CbGeV3G4ZmniyvuScGfLR",
  "type": "assistant",
  "uuid": "c671e221-e444-4992-b4bf-7bdcd041b1ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UdMsaD5jJPCA1BAJRsSc9p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12869,
      "cache_read_input_tokens": 32929,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12869,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 32929,
          "cache_creation_input_tokens": 12869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12869
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

_source line 25 · 2026-05-22T00:18:06.022Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MfiW3QRkbmkyaHmTFh1rw5`</summary>

```json
{
  "command": "python artifacts/c1_multi_llm/run_mistral_hetero_tau.py 2>&1",
  "description": "Run Mistral heterogeneous-tau DGP experiment (50 seeds x 3 budgets)",
  "timeout": 600000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c671e221-e444-4992-b4bf-7bdcd041b1ec",
  "isSidechain": false,
  "requestId": "req_011CbGeV3G4ZmniyvuScGfLR",
  "type": "assistant",
  "uuid": "a479ef8a-4202-4cbb-a4dd-f46788f3786c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UdMsaD5jJPCA1BAJRsSc9p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12869,
      "cache_read_input_tokens": 32929,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12869,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 32929,
          "cache_creation_input_tokens": 12869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12869
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

_source line 26 · 2026-05-22T00:18:06.084Z_

<details><summary>↩ Tool result · reported error · `toolu_01MfiW3QRkbmkyaHmTFh1rw5`</summary>

```text
Exit code 127
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a479ef8a-4202-4cbb-a4dd-f46788f3786c",
  "isSidechain": false,
  "promptId": "695fc122-00c0-4b11-823d-9471ae018801",
  "type": "user",
  "uuid": "f64fc50b-9b93-4759-84e9-a08da198e162",
  "toolUseResult": "Error: Exit code 127\n/bin/bash: line 1: python: command not found",
  "sourceToolAssistantUUID": "a479ef8a-4202-4cbb-a4dd-f46788f3786c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T00:18:08.354Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SptJTQsTDnrRPmmgEye99x`</summary>

```json
{
  "command": "python3 artifacts/c1_multi_llm/run_mistral_hetero_tau.py 2>&1",
  "description": "Run Mistral heterogeneous-tau DGP experiment",
  "timeout": 600000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f64fc50b-9b93-4759-84e9-a08da198e162",
  "isSidechain": false,
  "requestId": "req_011CbGeVKpDzPvyjDUpCNWBs",
  "type": "assistant",
  "uuid": "1e88f5f5-c568-4be7-aa97-fa1689076d8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbhthKDZuY4rjom5ZYhZnc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 181,
      "cache_read_input_tokens": 45798,
      "output_tokens": 126,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 181,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 126,
          "cache_read_input_tokens": 45798,
          "cache_creation_input_tokens": 181,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 181
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

_source line 28 · 2026-05-22T00:18:11.672Z_

<details><summary>↩ Tool result · `toolu_01SptJTQsTDnrRPmmgEye99x`</summary>

```text
Mistral-7B-v0.3 Heterogeneous-τ DGP: EC-HTE vs Global
N=5000, budgets=[200, 500, 1000], seeds=50
Mistral per-subgroup CM:
  False_medium: FPR=0.1800, FNR=0.2989
  False_short: FPR=0.2414, FNR=0.1875
  True_medium: FPR=0.2333, FNR=0.1684
  True_short: FPR=0.0909, FNR=0.1207
Subgroup τ values:
  False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1
  False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1
  True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3
  True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6

=== Dry run (n_expert=200, 1 seed) ===
Dry run OK: 32 rows, columns: ['seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width', 'n_expert']
  naive               : mean |bias| = 0.1023
  global_corrected    : mean |bias| = 0.1140
  stratified_mle      : mean |bias| = 0.1571
  hb_ec_hte           : mean |bias| = 0.1587

  Oracle CATE check:
    False_medium z=0: cate_true=0.45 expected=0.45 [OK]
    False_medium z=1: cate_true=0.55 expected=0.55 [OK]
    False_short z=0: cate_true=0.40 expected=0.40 [OK]
    False_short z=1: cate_true=0.50 expected=0.50 [OK]
    True_medium z=0: cate_true=0.35 expected=0.35 [OK]
    True_medium z=1: cate_true=0.65 expected=0.65 [OK]
    True_short z=0: cate_true=0.20 expected=0.20 [OK]
    True_short z=1: cate_true=0.80 expected=0.80 [OK]

=== Full run (3 budgets x 50 seeds) ===

--- n_expert = 200 ---
  [10/50] 0s elapsed, ETA 2s
  [20/50] 0s elapsed, ETA 2s
  [30/50] 0s elapsed, ETA 2s
  [40/50] 1s elapsed, ETA 1s
  [50/50] 1s elapsed, ETA 1s
  n_expert=200 done in 0.7s

--- n_expert = 500 ---
  [10/50] 1s elapsed, ETA 1s
  [20/50] 1s elapsed, ETA 1s
  [30/50] 1s elapsed, ETA 1s
  [40/50] 1s elapsed, ETA 1s
  [50/50] 1s elapsed, ETA 1s
  n_expert=500 done in 0.6s

--- n_expert = 1000 ---
  [10/50] 1s elapsed, ETA 1s
  [20/50] 2s elapsed, ETA 0s
  [30/50] 2s elapsed, ETA 0s
  [40/50] 2s elapsed, ETA 0s
  [50/50] 2s elapsed, ETA 0s
  n_expert=1000 done in 0.7s

Total time: 2.0s
Saved mistral_hetero_tau_results.csv (4800 rows)
Wrote artifacts/c1_multi_llm/mistral_hetero_tau_analysis.md

=== Summary ===

  n_expert=200:
    naive               : |Bias|=0.0583  RMSE=0.1063
    global_corrected    : |Bias|=0.0266  RMSE=0.1536
    stratified_mle      : |Bias|=0.0284  RMSE=0.2364
    hb_ec_hte           : |Bias|=0.0281  RMSE=0.2384

  n_expert=500:
    naive               : |Bias|=0.0583  RMSE=0.1063
    global_corrected    : |Bias|=0.0245  RMSE=0.1369
    stratified_mle      : |Bias|=0.0194  RMSE=0.1710
    hb_ec_hte           : |Bias|=0.0191  RMSE=0.1717

  n_expert=1000:
    naive               : |Bias|=0.0583  RMSE=0.1063
    global_corrected    : |Bias|=0.0237  RMSE=0.1323
    stratified_mle      : |Bias|=0.0188  RMSE=0.1437
    hb_ec_hte           : |Bias|=0.0186  RMSE=0.1438

=== EC-HTE vs Global (Mistral) ===
  n_expert=200: |Bias| Global=0.0266 vs ECHTE=0.0281 (Global wins)
              RMSE  Global=0.1536 vs ECHTE=0.2384 (Global wins)
  n_expert=500: |Bias| Global=0.0245 vs ECHTE=0.0191 (ECHTE wins)
              RMSE  Global=0.1369 vs ECHTE=0.1717 (Global wins)
  n_expert=1000: |Bias| Global=0.0237 vs ECHTE=0.0186 (ECHTE wins)
              RMSE  Global=0.1323 vs ECHTE=0.1438 (Global wins)

=== Cross-Model: Mistral vs Llama ===
  n_expert=200:
    Mistral Δ|Bias| = -0.0015
    Llama   Δ|Bias| = +0.0117
  n_expert=500:
    Mistral Δ|Bias| = +0.0054
    Llama   Δ|Bias| = +0.0215
  n_expert=1000:
    Mistral Δ|Bias| = +0.0051
    Llama   Δ|Bias| = +0.0156
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e88f5f5-c568-4be7-aa97-fa1689076d8f",
  "isSidechain": false,
  "promptId": "695fc122-00c0-4b11-823d-9471ae018801",
  "type": "user",
  "uuid": "a25b2aad-4ec5-438d-8288-5cd43bcd2744",
  "toolUseResult": {
    "stdout": "Mistral-7B-v0.3 Heterogeneous-τ DGP: EC-HTE vs Global\nN=5000, budgets=[200, 500, 1000], seeds=50\nMistral per-subgroup CM:\n  False_medium: FPR=0.1800, FNR=0.2989\n  False_short: FPR=0.2414, FNR=0.1875\n  True_medium: FPR=0.2333, FNR=0.1684\n  True_short: FPR=0.0909, FNR=0.1207\nSubgroup τ values:\n  False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1\n  False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1\n  True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3\n  True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6\n\n=== Dry run (n_expert=200, 1 seed) ===\nDry run OK: 32 rows, columns: ['seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width', 'n_expert']\n  naive               : mean |bias| = 0.1023\n  global_corrected    : mean |bias| = 0.1140\n  stratified_mle      : mean |bias| = 0.1571\n  hb_ec_hte           : mean |bias| = 0.1587\n\n  Oracle CATE check:\n    False_medium z=0: cate_true=0.45 expected=0.45 [OK]\n    False_medium z=1: cate_true=0.55 expected=0.55 [OK]\n    False_short z=0: cate_true=0.40 expected=0.40 [OK]\n    False_short z=1: cate_true=0.50 expected=0.50 [OK]\n    True_medium z=0: cate_true=0.35 expected=0.35 [OK]\n    True_medium z=1: cate_true=0.65 expected=0.65 [OK]\n    True_short z=0: cate_true=0.20 expected=0.20 [OK]\n    True_short z=1: cate_true=0.80 expected=0.80 [OK]\n\n=== Full run (3 budgets x 50 seeds) ===\n\n--- n_expert = 200 ---\n  [10/50] 0s elapsed, ETA 2s\n  [20/50] 0s elapsed, ETA 2s\n  [30/50] 0s elapsed, ETA 2s\n  [40/50] 1s elapsed, ETA 1s\n  [50/50] 1s elapsed, ETA 1s\n  n_expert=200 done in 0.7s\n\n--- n_expert = 500 ---\n  [10/50] 1s elapsed, ETA 1s\n  [20/50] 1s elapsed, ETA 1s\n  [30/50] 1s elapsed, ETA 1s\n  [40/50] 1s elapsed, ETA 1s\n  [50/50] 1s elapsed, ETA 1s\n  n_expert=500 done in 0.6s\n\n--- n_expert = 1000 ---\n  [10/50] 1s elapsed, ETA 1s\n  [20/50] 2s elapsed, ETA 0s\n  [30/50] 2s elapsed, ETA 0s\n  [40/50] 2s elapsed, ETA 0s\n  [50/50] 2s elapsed, ETA 0s\n  n_expert=1000 done in 0.7s\n\nTotal time: 2.0s\nSaved mistral_hetero_tau_results.csv (4800 rows)\nWrote artifacts/c1_multi_llm/mistral_hetero_tau_analysis.md\n\n=== Summary ===\n\n  n_expert=200:\n    naive               : |Bias|=0.0583  RMSE=0.1063\n    global_corrected    : |Bias|=0.0266  RMSE=0.1536\n    stratified_mle      : |Bias|=0.0284  RMSE=0.2364\n    hb_ec_hte           : |Bias|=0.0281  RMSE=0.2384\n\n  n_expert=500:\n    naive               : |Bias|=0.0583  RMSE=0.1063\n    global_corrected    : |Bias|=0.0245  RMSE=0.1369\n    stratified_mle      : |Bias|=0.0194  RMSE=0.1710\n    hb_ec_hte           : |Bias|=0.0191  RMSE=0.1717\n\n  n_expert=1000:\n    naive               : |Bias|=0.0583  RMSE=0.1063\n    global_corrected    : |Bias|=0.0237  RMSE=0.1323\n    stratified_mle      : |Bias|=0.0188  RMSE=0.1437\n    hb_ec_hte           : |Bias|=0.0186  RMSE=0.1438\n\n=== EC-HTE vs Global (Mistral) ===\n  n_expert=200: |Bias| Global=0.0266 vs ECHTE=0.0281 (Global wins)\n              RMSE  Global=0.1536 vs ECHTE=0.2384 (Global wins)\n  n_expert=500: |Bias| Global=0.0245 vs ECHTE=0.0191 (ECHTE wins)\n              RMSE  Global=0.1369 vs ECHTE=0.1717 (Global wins)\n  n_expert=1000: |Bias| Global=0.0237 vs ECHTE=0.0186 (ECHTE wins)\n              RMSE  Global=0.1323 vs ECHTE=0.1438 (Global wins)\n\n=== Cross-Model: Mistral vs Llama ===\n  n_expert=200:\n    Mistral Δ|Bias| = -0.0015\n    Llama   Δ|Bias| = +0.0117\n  n_expert=500:\n    Mistral Δ|Bias| = +0.0054\n    Llama   Δ|Bias| = +0.0215\n  n_expert=1000:\n    Mistral Δ|Bias| = +0.0051\n    Llama   Δ|Bias| = +0.0156",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1e88f5f5-c568-4be7-aa97-fa1689076d8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-22T00:18:11.675Z_

```json
{
  "parentUuid": "a25b2aad-4ec5-438d-8288-5cd43bcd2744",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "10cf3d2a-4e57-4ece-a4d2-74ebe234f52c",
  "timestamp": "2026-05-22T00:18:11.675Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 30 · 2026-05-22T00:18:16.269Z_

Experiment completed. Let me verify the CSV row count and check the analysis report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10cf3d2a-4e57-4ece-a4d2-74ebe234f52c",
  "isSidechain": false,
  "requestId": "req_011CbGeVjdSbEqG4Lu1iYf9j",
  "type": "assistant",
  "uuid": "cba5e0c1-c061-4299-b677-242efa0e2116",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174ZajipMQiYGN2NPXv7mUv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2037,
      "cache_read_input_tokens": 45979,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2037,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 45979,
          "cache_creation_input_tokens": 2037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2037
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

_source line 31 · 2026-05-22T00:18:16.815Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KhdJpZRcjQrAFyCsrtokwy`</summary>

```json
{
  "command": "wc -l artifacts/c1_multi_llm/mistral_hetero_tau_results.csv",
  "description": "Verify CSV row count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cba5e0c1-c061-4299-b677-242efa0e2116",
  "isSidechain": false,
  "requestId": "req_011CbGeVjdSbEqG4Lu1iYf9j",
  "type": "assistant",
  "uuid": "a56ec69a-e135-41ca-801b-6f1e48af5093",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174ZajipMQiYGN2NPXv7mUv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2037,
      "cache_read_input_tokens": 45979,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2037,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 45979,
          "cache_creation_input_tokens": 2037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2037
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

_source line 32 · 2026-05-22T00:18:16.863Z_

<details><summary>↩ Tool result · `toolu_01KhdJpZRcjQrAFyCsrtokwy`</summary>

```text
4801 artifacts/c1_multi_llm/mistral_hetero_tau_results.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a56ec69a-e135-41ca-801b-6f1e48af5093",
  "isSidechain": false,
  "promptId": "695fc122-00c0-4b11-823d-9471ae018801",
  "type": "user",
  "uuid": "e37bb448-0e6c-4892-9e20-7e1fc77e93bc",
  "toolUseResult": {
    "stdout": "4801 artifacts/c1_multi_llm/mistral_hetero_tau_results.csv",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a56ec69a-e135-41ca-801b-6f1e48af5093",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-22T00:18:17.703Z_

<details><summary>↩ Tool result · `toolu_013sLEL5WuXN954XRZrEo5Tw`</summary>

```text
1	# Mistral-7B-v0.3 Heterogeneous-τ DGP: EC-HTE vs Global Correction
2	
3	## Design
4	
5	- N=5000, P(Z=1)=0.652, K=4 subgroups
6	- **LLM**: Mistral-7B-v0.3 (balanced binarization)
7	- **Heterogeneous τ(z) across subgroups:**
8	  - False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1
9	  - False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1
10	  - True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3
11	  - True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6
12	- n_expert sweep: [200, 500, 1000]
13	- 50 MC seeds per budget
14	- HB method: MAP-EB (Gamma(3,1) prior)
15	- |Bias| = avg across cells of |mean(bias) across seeds|
16	- RMSE = avg across cells of sqrt(mean(bias²) across seeds)
17	
18	## Mistral-7B-v0.3 Per-Subgroup Confusion Matrix
19	
20	| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |
21	|----------|-----|-----|-----|-----------|
22	| False_medium | 0.3816 | 0.1800 | 0.2989 | 0.5211 |
23	| False_short | 0.2224 | 0.2414 | 0.1875 | 0.5711 |
24	| True_medium | 0.2551 | 0.2333 | 0.1684 | 0.5983 |
25	| True_short | 0.1408 | 0.0909 | 0.1207 | 0.7884 |
26	
27	- Mistral Δ_FPR = 0.1505, Δ_FNR = 0.1782
28	- Llama Δ_FPR = 0.2190, Δ_FNR = 0.1290
29	- Mistral has smaller FPR heterogeneity and larger FNR heterogeneity than Llama
30	
31	## Summary Table (averaged across all cells)
32	
33	| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |
34	|----------|--------|-------|------|----------|----------|
35	| 200 | Naive | 0.0583 | 0.1063 | 0.890 | 0.336 |
36	| 200 | Global | 0.0266 | 0.1536 | 0.912 | 0.517 |
37	| 200 | Strat MLE | 0.0284 | 0.2364 | 0.815 | 0.551 |
38	| 200 | HB EC-HTE | 0.0281 | 0.2384 | 0.812 | 0.552 |
39	|----------|--------|-------|------|----------|----------|
40	| 500 | Naive | 0.0583 | 0.1063 | 0.890 | 0.336 |
41	| 500 | Global | 0.0245 | 0.1369 | 0.940 | 0.505 |
42	| 500 | Strat MLE | 0.0194 | 0.1710 | 0.873 | 0.501 |
43	| 500 | HB EC-HTE | 0.0191 | 0.1717 | 0.873 | 0.502 |
44	|----------|--------|-------|------|----------|----------|
45	| 1000 | Naive | 0.0583 | 0.1063 | 0.890 | 0.336 |
46	| 1000 | Global | 0.0237 | 0.1323 | 0.940 | 0.501 |
47	| 1000 | Strat MLE | 0.0188 | 0.1437 | 0.897 | 0.484 |
48	| 1000 | HB EC-HTE | 0.0186 | 0.1438 | 0.897 | 0.485 |
49	|----------|--------|-------|------|----------|----------|
50	
51	## EC-HTE vs Global Comparison
52	
53	| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |
54	|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|
55	| 200 | 0.0266 | 0.0281 | -0.0015 | 0.1536 | 0.2384 | -0.0848 | no | no |
56	| 500 | 0.0245 | 0.0191 | +0.0054 | 0.1369 | 0.1717 | -0.0348 | **YES** | no |
57	| 1000 | 0.0237 | 0.0186 | +0.0051 | 0.1323 | 0.1438 | -0.0114 | **YES** | no |
58	
59	## Per-Subgroup Breakdown
60	
61	### n_expert = 200
62	
63	| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
64	|----------|-----|---|-------------|-------------|-------------|-------------|------------|
65	| False_medium | 0.1 | 0 | 0.0107 | 0.0250 | -0.0143 | 0.1599 | 0.2225 |
66	| False_medium | 0.1 | 1 | 0.0132 | 0.0279 | -0.0147 | 0.0917 | 0.1163 |
67	| False_short | 0.1 | 0 | 0.0069 | 0.0065 | +0.0004 | 0.2117 | 0.3542 |
68	| False_short | 0.1 | 1 | 0.0004 | 0.0145 | -0.0140 | 0.1188 | 0.1914 |
69	| True_medium | 0.3 | 0 | 0.0272 | 0.0660 | -0.0388 | 0.1752 | 0.2444 |
70	| True_medium | 0.3 | 1 | 0.0001 | 0.0050 | -0.0049 | 0.0944 | 0.1367 |
71	| True_short | 0.6 | 0 | 0.1027 | 0.0511 | +0.0515 | 0.2286 | 0.4119 |
72	| True_short | 0.6 | 1 | 0.0518 | 0.0289 | +0.0229 | 0.1489 | 0.2299 |
73	
74	### n_expert = 500
75	
76	| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
77	|----------|-----|---|-------------|-------------|-------------|-------------|------------|
78	| False_medium | 0.1 | 0 | 0.0134 | 0.0076 | +0.0058 | 0.1354 | 0.1858 |
79	| False_medium | 0.1 | 1 | 0.0058 | 0.0143 | -0.0084 | 0.0796 | 0.0963 |
80	| False_short | 0.1 | 0 | 0.0064 | 0.0110 | -0.0046 | 0.1841 | 0.2516 |
81	| False_short | 0.1 | 1 | 0.0068 | 0.0002 | +0.0066 | 0.1059 | 0.1416 |
82	| True_medium | 0.3 | 0 | 0.0357 | 0.0508 | -0.0151 | 0.1533 | 0.1857 |
83	| True_medium | 0.3 | 1 | 0.0106 | 0.0042 | +0.0064 | 0.0836 | 0.1058 |
84	| True_short | 0.6 | 0 | 0.0837 | 0.0492 | +0.0345 | 0.2164 | 0.2535 |
85	| True_short | 0.6 | 1 | 0.0337 | 0.0155 | +0.0182 | 0.1369 | 0.1533 |
86	
87	### n_expert = 1000
88	
89	| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
90	|----------|-----|---|-------------|-------------|-------------|-------------|------------|
91	| False_medium | 0.1 | 0 | 0.0132 | 0.0079 | +0.0054 | 0.1317 | 0.1828 |
92	| False_medium | 0.1 | 1 | 0.0042 | 0.0031 | +0.0010 | 0.0745 | 0.0862 |
93	| False_short | 0.1 | 0 | 0.0074 | 0.0088 | -0.0014 | 0.1740 | 0.1933 |
94	| False_short | 0.1 | 1 | 0.0081 | 0.0007 | +0.0074 | 0.1036 | 0.1173 |
95	| True_medium | 0.3 | 0 | 0.0352 | 0.0405 | -0.0053 | 0.1476 | 0.1535 |
96	| True_medium | 0.3 | 1 | 0.0128 | 0.0011 | +0.0117 | 0.0815 | 0.0877 |
97	| True_short | 0.6 | 0 | 0.0798 | 0.0580 | +0.0218 | 0.2125 | 0.1951 |
98	| True_short | 0.6 | 1 | 0.0289 | 0.0288 | +0.0001 | 0.1333 | 0.1341 |
99	
100	## Bias-Variance Decomposition
101	
102	| n_expert | Method | Bias² | Variance | MSE |
103	|----------|--------|-------|----------|-----|
104	| 200 | Naive | 0.0058 | 0.0075 | 0.0133 |
105	| 200 | Global | 0.0018 | 0.0246 | 0.0264 |
106	| 200 | Strat MLE | 0.0012 | 0.0645 | 0.0658 |
107	| 200 | HB EC-HTE | 0.0012 | 0.0659 | 0.0671 |
108	| 500 | Naive | 0.0058 | 0.0075 | 0.0133 |
109	| 500 | Global | 0.0012 | 0.0199 | 0.0211 |
110	| 500 | Strat MLE | 0.0007 | 0.0322 | 0.0329 |
111	| 500 | HB EC-HTE | 0.0007 | 0.0325 | 0.0332 |
112	| 1000 | Naive | 0.0058 | 0.0075 | 0.0133 |
113	| 1000 | Global | 0.0011 | 0.0187 | 0.0198 |
114	| 1000 | Strat MLE | 0.0008 | 0.0221 | 0.0228 |
115	| 1000 | HB EC-HTE | 0.0007 | 0.0221 | 0.0229 |
116	
117	## Cross-Model Comparison: Mistral vs Llama (exp-023)
118	
119	### CM Heterogeneity
120	
121	| Metric | Mistral-7B-v0.3 | Llama3.1-8B |
122	|--------|----------------|------------|
123	| Δ_FPR (max-min) | 0.1505 | 0.2190 |
124	| Δ_FNR (max-min) | 0.1782 | 0.1290 |
125	| Mean Δ_error | 0.1643 | 0.1740 |
126	
127	### Bias Comparison
128	
129	| n_expert | Mistral |Bias|_Global | Mistral |Bias|_ECHTE | Mistral Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |
130	|----------|------------------|--------------------|--------------|--------------------|--------------------|---------------|
131	| 200 | 0.0266 | 0.0281 | -0.0015 | 0.0365 | 0.0248 | +0.0117 |
132	| 500 | 0.0245 | 0.0191 | +0.0054 | 0.0314 | 0.0099 | +0.0215 |
133	| 1000 | 0.0237 | 0.0186 | +0.0051 | 0.0286 | 0.0130 | +0.0156 |
134	
135	### RMSE Comparison
136	
137	| n_expert | Mistral RMSE_Global | Mistral RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |
138	|----------|-----------------|----------------|------------------|-----------------|
139	| 200 | 0.1536 | 0.2384 | 0.1780 | 0.2606 |
140	| 500 | 0.1369 | 0.1717 | 0.1580 | 0.1760 |
141	| 1000 | 0.1323 | 0.1438 | 0.1554 | 0.1602 |
142	
143	## Conclusion
144	
145	EC-HTE wins on |Bias| in 2/3 budget levels.
146	EC-HTE wins on RMSE in 0/3 budget levels.
147	
148	**Result: Under heterogeneous-τ DGP with Mistral-7B-v0.3 CMs, EC-HTE outperforms Global in bias at 2 of 3 budget levels.**
149	
150	**Cross-model consistency**: Llama EC-HTE wins on bias in 3/3 budgets; Mistral EC-HTE wins in 2/3 budgets.
151	
152	Average Δ|Bias| (Global - EC-HTE): Mistral = +0.0030, Llama = +0.0163
153	Llama shows larger EC-HTE improvement despite smaller CM heterogeneity.
154	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb3b8827-7124-4958-b7be-3aaa88465b5a",
  "isSidechain": false,
  "promptId": "695fc122-00c0-4b11-823d-9471ae018801",
  "type": "user",
  "uuid": "3aa5f979-3689-4930-9aaa-d915bee05b5f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/mistral_hetero_tau_analysis.md",
      "content": "# Mistral-7B-v0.3 Heterogeneous-τ DGP: EC-HTE vs Global Correction\n\n## Design\n\n- N=5000, P(Z=1)=0.652, K=4 subgroups\n- **LLM**: Mistral-7B-v0.3 (balanced binarization)\n- **Heterogeneous τ(z) across subgroups:**\n  - False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1\n  - False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1\n  - True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3\n  - True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6\n- n_expert sweep: [200, 500, 1000]\n- 50 MC seeds per budget\n- HB method: MAP-EB (Gamma(3,1) prior)\n- |Bias| = avg across cells of |mean(bias) across seeds|\n- RMSE = avg across cells of sqrt(mean(bias²) across seeds)\n\n## Mistral-7B-v0.3 Per-Subgroup Confusion Matrix\n\n| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |\n|----------|-----|-----|-----|-----------|\n| False_medium | 0.3816 | 0.1800 | 0.2989 | 0.5211 |\n| False_short | 0.2224 | 0.2414 | 0.1875 | 0.5711 |\n| True_medium | 0.2551 | 0.2333 | 0.1684 | 0.5983 |\n| True_short | 0.1408 | 0.0909 | 0.1207 | 0.7884 |\n\n- Mistral Δ_FPR = 0.1505, Δ_FNR = 0.1782\n- Llama Δ_FPR = 0.2190, Δ_FNR = 0.1290\n- Mistral has smaller FPR heterogeneity and larger FNR heterogeneity than Llama\n\n## Summary Table (averaged across all cells)\n\n| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |\n|----------|--------|-------|------|----------|----------|\n| 200 | Naive | 0.0583 | 0.1063 | 0.890 | 0.336 |\n| 200 | Global | 0.0266 | 0.1536 | 0.912 | 0.517 |\n| 200 | Strat MLE | 0.0284 | 0.2364 | 0.815 | 0.551 |\n| 200 | HB EC-HTE | 0.0281 | 0.2384 | 0.812 | 0.552 |\n|----------|--------|-------|------|----------|----------|\n| 500 | Naive | 0.0583 | 0.1063 | 0.890 | 0.336 |\n| 500 | Global | 0.0245 | 0.1369 | 0.940 | 0.505 |\n| 500 | Strat MLE | 0.0194 | 0.1710 | 0.873 | 0.501 |\n| 500 | HB EC-HTE | 0.0191 | 0.1717 | 0.873 | 0.502 |\n|----------|--------|-------|------|----------|----------|\n| 1000 | Naive | 0.0583 | 0.1063 | 0.890 | 0.336 |\n| 1000 | Global | 0.0237 | 0.1323 | 0.940 | 0.501 |\n| 1000 | Strat MLE | 0.0188 | 0.1437 | 0.897 | 0.484 |\n| 1000 | HB EC-HTE | 0.0186 | 0.1438 | 0.897 | 0.485 |\n|----------|--------|-------|------|----------|----------|\n\n## EC-HTE vs Global Comparison\n\n| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |\n|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|\n| 200 | 0.0266 | 0.0281 | -0.0015 | 0.1536 | 0.2384 | -0.0848 | no | no |\n| 500 | 0.0245 | 0.0191 | +0.0054 | 0.1369 | 0.1717 | -0.0348 | **YES** | no |\n| 1000 | 0.0237 | 0.0186 | +0.0051 | 0.1323 | 0.1438 | -0.0114 | **YES** | no |\n\n## Per-Subgroup Breakdown\n\n### n_expert = 200\n\n| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\n|----------|-----|---|-------------|-------------|-------------|-------------|------------|\n| False_medium | 0.1 | 0 | 0.0107 | 0.0250 | -0.0143 | 0.1599 | 0.2225 |\n| False_medium | 0.1 | 1 | 0.0132 | 0.0279 | -0.0147 | 0.0917 | 0.1163 |\n| False_short | 0.1 | 0 | 0.0069 | 0.0065 | +0.0004 | 0.2117 | 0.3542 |\n| False_short | 0.1 | 1 | 0.0004 | 0.0145 | -0.0140 | 0.1188 | 0.1914 |\n| True_medium | 0.3 | 0 | 0.0272 | 0.0660 | -0.0388 | 0.1752 | 0.2444 |\n| True_medium | 0.3 | 1 | 0.0001 | 0.0050 | -0.0049 | 0.0944 | 0.1367 |\n| True_short | 0.6 | 0 | 0.1027 | 0.0511 | +0.0515 | 0.2286 | 0.4119 |\n| True_short | 0.6 | 1 | 0.0518 | 0.0289 | +0.0229 | 0.1489 | 0.2299 |\n\n### n_expert = 500\n\n| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\n|----------|-----|---|-------------|-------------|-------------|-------------|------------|\n| False_medium | 0.1 | 0 | 0.0134 | 0.0076 | +0.0058 | 0.1354 | 0.1858 |\n| False_medium | 0.1 | 1 | 0.0058 | 0.0143 | -0.0084 | 0.0796 | 0.0963 |\n| False_short | 0.1 | 0 | 0.0064 | 0.0110 | -0.0046 | 0.1841 | 0.2516 |\n| False_short | 0.1 | 1 | 0.0068 | 0.0002 | +0.0066 | 0.1059 | 0.1416 |\n| True_medium | 0.3 | 0 | 0.0357 | 0.0508 | -0.0151 | 0.1533 | 0.1857 |\n| True_medium | 0.3 | 1 | 0.0106 | 0.0042 | +0.0064 | 0.0836 | 0.1058 |\n| True_short | 0.6 | 0 | 0.0837 | 0.0492 | +0.0345 | 0.2164 | 0.2535 |\n| True_short | 0.6 | 1 | 0.0337 | 0.0155 | +0.0182 | 0.1369 | 0.1533 |\n\n### n_expert = 1000\n\n| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\n|----------|-----|---|-------------|-------------|-------------|-------------|------------|\n| False_medium | 0.1 | 0 | 0.0132 | 0.0079 | +0.0054 | 0.1317 | 0.1828 |\n| False_medium | 0.1 | 1 | 0.0042 | 0.0031 | +0.0010 | 0.0745 | 0.0862 |\n| False_short | 0.1 | 0 | 0.0074 | 0.0088 | -0.0014 | 0.1740 | 0.1933 |\n| False_short | 0.1 | 1 | 0.0081 | 0.0007 | +0.0074 | 0.1036 | 0.1173 |\n| True_medium | 0.3 | 0 | 0.0352 | 0.0405 | -0.0053 | 0.1476 | 0.1535 |\n| True_medium | 0.3 | 1 | 0.0128 | 0.0011 | +0.0117 | 0.0815 | 0.0877 |\n| True_short | 0.6 | 0 | 0.0798 | 0.0580 | +0.0218 | 0.2125 | 0.1951 |\n| True_short | 0.6 | 1 | 0.0289 | 0.0288 | +0.0001 | 0.1333 | 0.1341 |\n\n## Bias-Variance Decomposition\n\n| n_expert | Method | Bias² | Variance | MSE |\n|----------|--------|-------|----------|-----|\n| 200 | Naive | 0.0058 | 0.0075 | 0.0133 |\n| 200 | Global | 0.0018 | 0.0246 | 0.0264 |\n| 200 | Strat MLE | 0.0012 | 0.0645 | 0.0658 |\n| 200 | HB EC-HTE | 0.0012 | 0.0659 | 0.0671 |\n| 500 | Naive | 0.0058 | 0.0075 | 0.0133 |\n| 500 | Global | 0.0012 | 0.0199 | 0.0211 |\n| 500 | Strat MLE | 0.0007 | 0.0322 | 0.0329 |\n| 500 | HB EC-HTE | 0.0007 | 0.0325 | 0.0332 |\n| 1000 | Naive | 0.0058 | 0.0075 | 0.0133 |\n| 1000 | Global | 0.0011 | 0.0187 | 0.0198 |\n| 1000 | Strat MLE | 0.0008 | 0.0221 | 0.0228 |\n| 1000 | HB EC-HTE | 0.0007 | 0.0221 | 0.0229 |\n\n## Cross-Model Comparison: Mistral vs Llama (exp-023)\n\n### CM Heterogeneity\n\n| Metric | Mistral-7B-v0.3 | Llama3.1-8B |\n|--------|----------------|------------|\n| Δ_FPR (max-min) | 0.1505 | 0.2190 |\n| Δ_FNR (max-min) | 0.1782 | 0.1290 |\n| Mean Δ_error | 0.1643 | 0.1740 |\n\n### Bias Comparison\n\n| n_expert | Mistral |Bias|_Global | Mistral |Bias|_ECHTE | Mistral Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |\n|----------|------------------|--------------------|--------------|--------------------|--------------------|---------------|\n| 200 | 0.0266 | 0.0281 | -0.0015 | 0.0365 | 0.0248 | +0.0117 |\n| 500 | 0.0245 | 0.0191 | +0.0054 | 0.0314 | 0.0099 | +0.0215 |\n| 1000 | 0.0237 | 0.0186 | +0.0051 | 0.0286 | 0.0130 | +0.0156 |\n\n### RMSE Comparison\n\n| n_expert | Mistral RMSE_Global | Mistral RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |\n|----------|-----------------|----------------|------------------|-----------------|\n| 200 | 0.1536 | 0.2384 | 0.1780 | 0.2606 |\n| 500 | 0.1369 | 0.1717 | 0.1580 | 0.1760 |\n| 1000 | 0.1323 | 0.1438 | 0.1554 | 0.1602 |\n\n## Conclusion\n\nEC-HTE wins on |Bias| in 2/3 budget levels.\nEC-HTE wins on RMSE in 0/3 budget levels.\n\n**Result: Under heterogeneous-τ DGP with Mistral-7B-v0.3 CMs, EC-HTE outperforms Global in bias at 2 of 3 budget levels.**\n\n**Cross-model consistency**: Llama EC-HTE wins on bias in 3/3 budgets; Mistral EC-HTE wins in 2/3 budgets.\n\nAverage Δ|Bias| (Global - EC-HTE): Mistral = +0.0030, Llama = +0.0163\nLlama shows larger EC-HTE improvement despite smaller CM heterogeneity.\n",
      "numLines": 154,
      "startLine": 1,
      "totalLines": 154
    }
  },
  "sourceToolAssistantUUID": "bb3b8827-7124-4958-b7be-3aaa88465b5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-22T00:18:17.698Z_

<details open><summary>🔧 Tool call — Read · `toolu_013sLEL5WuXN954XRZrEo5Tw`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/mistral_hetero_tau_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e37bb448-0e6c-4892-9e20-7e1fc77e93bc",
  "isSidechain": false,
  "requestId": "req_011CbGeVjdSbEqG4Lu1iYf9j",
  "type": "assistant",
  "uuid": "bb3b8827-7124-4958-b7be-3aaa88465b5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174ZajipMQiYGN2NPXv7mUv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2037,
      "cache_read_input_tokens": 45979,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2037,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 45979,
          "cache_creation_input_tokens": 2037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2037
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

_source line 35_

```json
{
  "type": "last-prompt",
  "leafUuid": "3aa5f979-3689-4930-9aaa-d915bee05b5f",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Mistral-7B heterogeneous-τ DGP experiment",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8"
}
```

---

### Assistant

_source line 37 · 2026-05-22T00:18:27.010Z_

Done. Results:

- **CSV**: 4801 lines (4800 data + 1 header) — matches expected count
- **Script**: `artifacts/c1_multi_llm/run_mistral_hetero_tau.py`
- **CSV**: `artifacts/c1_multi_llm/mistral_hetero_tau_results.csv`
- **Analysis**: `artifacts/c1_multi_llm/mistral_hetero_tau_analysis.md`

**Key findings**:
- EC-HTE wins on |Bias| in **2/3** budget levels (n=500, n=1000); Global wins at n=200
- EC-HTE wins on RMSE in **0/3** levels (higher variance from per-subgroup estimation)
- Average Δ|Bias|: Mistral +0.0030 vs Llama +0.0163 — Llama shows larger EC-HTE improvement
- Mistral has smaller FPR heterogeneity (0.15 vs 0.22) but larger FNR heterogeneity (0.18 vs 0.13) than Llama
- Mistral's CM is closer to Llama than Qwen's was, with True_short being the most accurate subgroup (FPR=0.091, FNR=0.121)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3aa5f979-3689-4930-9aaa-d915bee05b5f",
  "isSidechain": false,
  "requestId": "req_011CbGeWBkKqHGCVbxiawVFd",
  "type": "assistant",
  "uuid": "be464d1a-972d-444e-bceb-54e17da5e9a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtckGYj6zPr5S6BoLxBBj6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4644,
      "cache_read_input_tokens": 48016,
      "output_tokens": 323,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4644,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 323,
          "cache_read_input_tokens": 48016,
          "cache_creation_input_tokens": 4644,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4644
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

_source line 38_

```json
{
  "type": "last-prompt",
  "leafUuid": "be464d1a-972d-444e-bceb-54e17da5e9a4",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Mistral-7B heterogeneous-τ DGP experiment",
  "sessionId": "f105112c-0ede-4aff-9056-e21c0cb102f8"
}
```

---
