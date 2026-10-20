# Research conversation: <project_context> # 项目: ec_hte_llm_annotation ## 运行环境 - 服务器名: local-cpu - SSH 账户: ubuntu（调用 ssh_execute / submit_trainin

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/2a935248-651b-4881-b714-ac12895495f7.jsonl`
- **Structured JSON:** [`437189e1584cfc16bfc2.json`](../../sessions/43/437189e1584cfc16bfc2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T07:25:49.828Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T07:25:49.828Z",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "content": "&lt;project_context>\n# 项目: ec_hte_llm_annotation\n\n## 运行环境\n- 服务器名: local-cpu\n- SSH 账户: ubuntu（调用 ssh_execute / submit_training_job 时传入 account=\"ubuntu\"）\n- SSH 连接命令: ssh local-cpu  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /home/ubuntu/ec_hte_llm_annotation\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：exp-013 Boundary Condition 实验\n\n**目的**：验证 EC-HTE 在小样本极端条件下的局限性——n_expert=50, K=4 时每子群仅 ~12 个 expert labels，per-subgroup CM 估计噪声极大，RMSE 预期显著高于 global correction。\n\n**配置**：\n- K=4, regime=extreme (misclass=[0.30, 0.20, 0.10, 0.03], tau_z1=0.5, tau_z0=0.1)\n- n_expert=50（每子群 ~12.5 个 labels）\n- 100 MC runs\n- 对比方法：Naive / Global / Stratified MLE / HB EC-HTE\n- 输出 metrics：bias_z0, bias_z1, rmse_z0, rmse_z1, coverage_z0, coverage_z1（每子群 + 平均）\n\n**代码基础**：`/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py`\n\n这个脚本包含完整的 DGP、CM 估计器（MLE Laplace、HB Gibbs、EB）、diff-in-means CATE 估计、confusion matrix 反演。你需要基于它创建一个精简的 boundary condition 脚本。\n\n**步骤**：\n\n1. 创建 `/home/ubuntu/ec_hte_llm_annotation/exp013_boundary_condition.py`：\n   - 从 exp001_hb_synthetic.py 导入核心函数（generate_data, get_counts, estimate_cm_mle, estimate_cm_hb_eb, estimate_cm_hb_gibbs, build_mixing_matrix, invert_mixing_safe, diff_in_means, REGIMES, SUBGROUP_LABELS, N）\n   - 只跑 K=4, extreme, n_expert=50 这一个配置\n   - 100 MC runs（可以用 --dry-run 先跑 5 runs 验证）\n   - 输出：results/exp013_boundary_condition.csv（每 MC run × 每子群 × 每方法 × 每 z-level 的 tau_corrected, tau_true, se_corrected, coverage）\n   - 汇总输出：results/exp013_boundary_summary.csv（每子群 × 每方法的平均 bias, rmse, coverage + SE）\n\n2. 先 `--dry-run`（5 MC runs）验证脚本可以跑通\n\n3. 跑完整 100 MC runs\n\n4. 输出一个简洁的汇总表格到 results/exp013_boundary_analysis.md，格式：\n   ```\n   | Subgroup | Method | |Bias|_z0 | RMSE_z0 | Coverage_z0 | |Bias|_z1 | RMSE_z1 | Coverage_z1 |\n   ```\n   加一段分析：\n   - 哪个子群退化最严重？（预期是 smallest misclass subgroup D, pi=0.03）\n   - RMSE 相对 global 的放大倍数\n   - 是否验证了 n_expert/K >= 25 的阈值建议\n\n**环境**：\n- Python 3: `/home/ubuntu/ec_hte_llm_annotation/.venv/bin/python3` 或系统 python3\n- 依赖已装：numpy, pandas, scipy（在 exp001 的 venv 中）\n- 工作目录：`/home/ubuntu/ec_hte_llm_annotation/`\n\n**验证**：dry-run 跑通后再跑 full run。如果 Gibbs sampler 太慢（K=4 有 4 个子群要采样），可以用 EB (Empirical Bayes) 作为 HB 的替代——EB 在小样本时更稳定且快很多。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T07:25:49.832Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T07:25:49.832Z",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-21T07:25:49.866Z_

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
## 任务：exp-013 Boundary Condition 实验

**目的**：验证 EC-HTE 在小样本极端条件下的局限性——n_expert=50, K=4 时每子群仅 ~12 个 expert labels，per-subgroup CM 估计噪声极大，RMSE 预期显著高于 global correction。

**配置**：
- K=4, regime=extreme (misclass=[0.30, 0.20, 0.10, 0.03], tau_z1=0.5, tau_z0=0.1)
- n_expert=50（每子群 ~12.5 个 labels）
- 100 MC runs
- 对比方法：Naive / Global / Stratified MLE / HB EC-HTE
- 输出 metrics：bias_z0, bias_z1, rmse_z0, rmse_z1, coverage_z0, coverage_z1（每子群 + 平均）

**代码基础**：`/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py`

这个脚本包含完整的 DGP、CM 估计器（MLE Laplace、HB Gibbs、EB）、diff-in-means CATE 估计、confusion matrix 反演。你需要基于它创建一个精简的 boundary condition 脚本。

**步骤**：

1. 创建 `/home/ubuntu/ec_hte_llm_annotation/exp013_boundary_condition.py`：
   - 从 exp001_hb_synthetic.py 导入核心函数（generate_data, get_counts, estimate_cm_mle, estimate_cm_hb_eb, estimate_cm_hb_gibbs, build_mixing_matrix, invert_mixing_safe, diff_in_means, REGIMES, SUBGROUP_LABELS, N）
   - 只跑 K=4, extreme, n_expert=50 这一个配置
   - 100 MC runs（可以用 --dry-run 先跑 5 runs 验证）
   - 输出：results/exp013_boundary_condition.csv（每 MC run × 每子群 × 每方法 × 每 z-level 的 tau_corrected, tau_true, se_corrected, coverage）
   - 汇总输出：results/exp013_boundary_summary.csv（每子群 × 每方法的平均 bias, rmse, coverage + SE）

2. 先 `--dry-run`（5 MC runs）验证脚本可以跑通

3. 跑完整 100 MC runs

4. 输出一个简洁的汇总表格到 results/exp013_boundary_analysis.md，格式：
   ```
   | Subgroup | Method | |Bias|_z0 | RMSE_z0 | Coverage_z0 | |Bias|_z1 | RMSE_z1 | Coverage_z1 |
   ```
   加一段分析：
   - 哪个子群退化最严重？（预期是 smallest misclass subgroup D, pi=0.03）
   - RMSE 相对 global 的放大倍数
   - 是否验证了 n_expert/K >= 25 的阈值建议

**环境**：
- Python 3: `/home/ubuntu/ec_hte_llm_annotation/.venv/bin/python3` 或系统 python3
- 依赖已装：numpy, pandas, scipy（在 exp001 的 venv 中）
- 工作目录：`/home/ubuntu/ec_hte_llm_annotation/`

**验证**：dry-run 跑通后再跑 full run。如果 Gibbs sampler 太慢（K=4 有 4 个子群要采样），可以用 EB (Empirical Bayes) 作为 HB 的替代——EB 在小样本时更稳定且快很多。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "99acad5a-cfb8-48f1-9a0e-e4eb1fe13a2c",
  "type": "user",
  "uuid": "f946b3df-2e80-482a-90b3-f37b92c939b1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T07:25:49.865Z_

```json
{
  "parentUuid": "f946b3df-2e80-482a-90b3-f37b92c939b1",
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
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__update_registry"
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
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f067c903-185c-47e2-ac9a-113b0485454c",
  "timestamp": "2026-05-21T07:25:49.865Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T07:25:49.865Z_

```json
{
  "parentUuid": "f067c903-185c-47e2-ac9a-113b0485454c",
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
  "uuid": "ff45bff0-8cd7-4ba5-b9e5-d80610b4fd8a",
  "timestamp": "2026-05-21T07:25:49.865Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T07:25:49.865Z_

```json
{
  "parentUuid": "ff45bff0-8cd7-4ba5-b9e5-d80610b4fd8a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7357f0f7-e331-4ea4-b794-9708a95b2345",
  "timestamp": "2026-05-21T07:25:49.865Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
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
  "aiTitle": "Implement boundary condition experiment exp013",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7"
}
```

---

### Assistant

_source line 8 · 2026-05-21T07:25:52.617Z_

I'll start by reading the base script to understand the core functions and structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7357f0f7-e331-4ea4-b794-9708a95b2345",
  "isSidechain": false,
  "requestId": "req_011CbFKJCadSG4zDp7gHsEvb",
  "type": "assistant",
  "uuid": "98834c41-816f-410a-88bf-61811378882d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AfTZ9NfUGPq9YukTT1cm46",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6574,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6574,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 6574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6574
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

_source line 9 · 2026-05-21T07:25:53.648Z_

<details open><summary>🔧 Tool call — Read · `toolu_014XsH86zX6HQVoFfJmUc4gA`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98834c41-816f-410a-88bf-61811378882d",
  "isSidechain": false,
  "requestId": "req_011CbFKJCadSG4zDp7gHsEvb",
  "type": "assistant",
  "uuid": "87ad2995-ab36-41d7-9958-584927a84892",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AfTZ9NfUGPq9YukTT1cm46",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6574,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6574,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 6574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6574
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

_source line 10 · 2026-05-21T07:25:54.210Z_

<details><summary>↩ Tool result · `toolu_014XsH86zX6HQVoFfJmUc4gA`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	exp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)
4	
5	Compares confusion matrix estimators for CATE correction under heterogeneous
6	misclassification across subgroups:
7	  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)
8	
9	Input: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)
10	Output: results/exp001_hb_results.csv, results/exp001_hb_diagnostics.csv
11	"""
12	
13	import argparse
14	import os
15	import sys
16	import time
17	import warnings
18	import numpy as np
19	import pandas as pd
20	from scipy.special import gammaln
21	from scipy.optimize import minimize_scalar
22	
23	warnings.filterwarnings('ignore')
24	
25	try:
26	    import pymc as pm
27	    import pytensor.tensor as pt
28	    import arviz as az
29	    HAS_PYMC = True
30	except ImportError:
31	    HAS_PYMC = False
32	
33	N = 5000
34	SUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}
35	
36	REGIMES = {
37	    2: {
38	        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},
39	        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},
40	        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
41	    },
42	    4: {
43	        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},
44	        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},
45	        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
46	    },
47	}
48	
49	DEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]
50	DEFAULT_K_LIST = [2, 4]
51	
52	
53	# ── DGP ───────────────────────────────────────────────────────────────────────
54	
55	def generate_data(regime_params, n_expert, k, seed):
56	    rng = np.random.RandomState(seed)
57	    labels = SUBGROUP_LABELS[k]
58	    T = rng.binomial(1, 0.5, N)
59	    Z = rng.binomial(1, 0.5, N)
60	    S = rng.choice(labels, N, p=[1.0 / k] * k)
61	    X = rng.randn(N, 5)
62	    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])
63	    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)
64	    mc_rates = np.zeros(N)
65	    for i, s in enumerate(labels):
66	        mc_rates[S == s] = regime_params['misclass'][i]
67	    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)
68	    idx = rng.choice(N, min(n_expert, N), replace=False)
69	    expert_mask = np.zeros(N, dtype=bool)
70	    expert_mask[idx] = True
71	    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)
72	
73	
74	# ── Helpers ───────────────────────────────────────────────────────────────────
75	
76	def diff_in_means(Y, T, mask):
77	    t1, t0 = mask & (T == 1), mask & (T == 0)
78	    n1, n0 = t1.sum(), t0.sum()
79	    if n1 < 2 or n0 < 2:
80	        return np.nan, np.nan
81	    y1, y0 = Y[t1], Y[t0]
82	    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
83	
84	
85	def get_counts(z_true, z_hat, subgroups, labels):
86	    """Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat]."""
87	    k = len(labels)
88	    counts = np.zeros((k, 2, 2), dtype=int)
89	    for i, s in enumerate(labels):
90	        ms = subgroups == s
91	        for z in [0, 1]:
92	            mz = ms & (z_true == z)
93	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
94	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
95	    return counts
96	
97	
98	def build_mixing_matrix(C):
99	    """C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5).
100	
101	    NOTE: This assumes P(Z=0)=P(Z=1)=0.5, which is correct for this experiment's
102	    DGP. For general P(Z), use the version in exp007 that takes p_z and p_z_hat.
103	    """
104	    M = np.zeros((2, 2))
105	    for zh in [0, 1]:
106	        cs = C[0, zh] + C[1, zh]
107	        if cs > 0:
108	            M[zh, 0] = C[0, zh] / cs
109	            M[zh, 1] = C[1, zh] / cs
110	        else:
111	            M[zh, :] = 0.5
112	    return M
113	
114	
115	def invert_mixing(M, tau_obs, se_obs):
116	    det = np.linalg.det(M)
117	    if abs(det) < 1e-10:
118	        return tau_obs.copy(), se_obs.copy()
119	    Mi = np.linalg.inv(M)
120	    tau_c = Mi @ tau_obs
121	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
122	    return tau_c, se_c
123	
124	
125	def safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):
126	    """Invert mixing matrix with condition number guard.
127	
128	    When cond(M_s) > threshold, matrix inversion is numerically unstable.
129	    Falls back to naive (no correction) to avoid catastrophic amplification.
130	    """
131	    cond = np.linalg.cond(M_s)
132	    if cond > cond_threshold:
133	        return tau_obs.copy()
134	    return np.linalg.solve(M_s, tau_obs)
135	
136	
137	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
138	    """Like invert_mixing but with condition number guard."""
139	    cond = np.linalg.cond(M)
140	    if cond > cond_threshold:
141	        return tau_obs.copy(), se_obs.copy()
142	    det = np.linalg.det(M)
143	    if abs(det) < 1e-10:
144	        return tau_obs.copy(), se_obs.copy()
145	    Mi = np.linalg.inv(M)
146	    tau_c = Mi @ tau_obs
147	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
148	    return tau_c, se_c
149	
150	
151	# ── Confusion Matrix Estimators ───────────────────────────────────────────────
152	
153	def estimate_cm_mle(counts, labels):
154	    """Per-subgroup MLE with Laplace smoothing (add-1)."""
155	    C = {}
156	    for i, s in enumerate(labels):
157	        C_s = np.zeros((2, 2))
158	        for z in [0, 1]:
159	            n = counts[i, z, :].sum()
160	            for zh in [0, 1]:
161	                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5
162	        C[s] = C_s
163	    return C
164	
165	
166	def _dirmult_neg_ll(alpha, counts_z):
167	    """Negative log marginal likelihood for Dirichlet-Multinomial."""
168	    a = alpha / 2.0
169	    if a < 1e-10:
170	        return 1e10
171	    ll = 0.0
172	    for c0, c1 in counts_z:
173	        n = c0 + c1
174	        if n == 0:
175	            continue
176	        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)
177	        ll -= 2 * gammaln(a) - gammaln(2 * a)
178	    return -ll
179	
180	
181	def estimate_cm_hb_eb(counts, labels):
182	    """Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean."""
183	    k = len(labels)
184	    alpha_opt = np.zeros(2)
185	    for z in [0, 1]:
186	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
187	        total = sum(c0 + c1 for c0, c1 in cl)
188	        if total == 0:
189	            alpha_opt[z] = 2.0
190	            continue
191	        res = minimize_scalar(
192	            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')
193	        alpha_opt[z] = res.x
194	
195	    C = {}
196	    for i, s in enumerate(labels):
197	        C_s = np.zeros((2, 2))
198	        for z in [0, 1]:
199	            a = alpha_opt[z] / 2.0
200	            n = counts[i, z, :].sum()
201	            d = n + 2 * a
202	            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5
203	            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5
204	        C[s] = C_s
205	
206	    diag = {'rhat_max': np.nan, 'ess_min': np.nan, 'divergent_count': 0,
207	            'runtime_seconds': 0.0, 'hb_method': 'eb',
208	            'alpha_0_z0': alpha_opt[0], 'alpha_0_z1': alpha_opt[1]}
209	    return C, diag
210	
211	
212	def _split_rhat(chains):
213	    """Split R-hat for a scalar parameter. chains: (n_chains, n_draws)."""
214	    parts = []
215	    for c in range(chains.shape[0]):
216	        half = chains.shape[1] // 2
217	        parts.append(chains[c, :half])
218	        parts.append(chains[c, half:2 * half])
219	    parts = np.array(parts)
220	    m = parts.shape[0]
221	    n = parts.shape[1]
222	    chain_means = parts.mean(axis=1)
223	    W = np.mean(np.var(parts, axis=1, ddof=1))
224	    B = n * np.var(chain_means, ddof=1)
225	    if W < 1e-20:
226	        return 1.0
227	    var_hat = (1 - 1.0 / n) * W + B / n
228	    return float(np.sqrt(var_hat / W))
229	
230	
231	def _bulk_ess(chains):
232	    """Approximate bulk ESS via initial positive sequence. chains: (n_chains, n_draws)."""
233	    x = chains.ravel()
234	    n = len(x)
235	    mu = x.mean()
236	    xc = x - mu
237	    max_lag = min(n // 2, 300)
238	    c0 = np.dot(xc, xc)
239	    if c0 < 1e-20:
240	        return float(n)
241	    tau = 1.0
242	    for lag in range(1, max_lag - 1, 2):
243	        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0
244	        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0
245	        pair = r1 + r2
246	        if pair < 0:
247	            break
248	        tau += 2 * pair
249	    return float(n / tau)
250	
251	
252	def _fast_diagnostics(alpha_arr, theta_arr, labels):
253	    """Compute R-hat and ESS over all parameters without arviz."""
254	    rhats, esss = [], []
255	    for d in range(alpha_arr.shape[2]):
256	        rhats.append(_split_rhat(alpha_arr[:, :, d]))
257	        esss.append(_bulk_ess(alpha_arr[:, :, d]))
258	    k = len(labels)
259	    for i in range(k):
260	        for z in [0, 1]:
261	            for zh in range(theta_arr.shape[4]):
262	                ch = theta_arr[:, :, i, z, zh]
263	                rhats.append(_split_rhat(ch))
264	                esss.append(_bulk_ess(ch))
265	    return max(rhats), min(esss)
266	
267	
268	def _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):
269	    """Log posterior for alpha_0[z] in log-alpha space (includes Jacobian)."""
270	    if alpha < 1e-10:
271	        return -1e10
272	    a = alpha / 2.0
273	    k = theta_z.shape[0]
274	    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha
275	    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))
276	    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))
277	    return lp
278	
279	
280	def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=4000, n_warmup=2000, n_chains=4,
281	                         hp_a0=3.0, hp_b0=1.0):
282	    """Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).
283	
284	    hp_a0, hp_b0: Gamma hyperprior shape/rate on alpha_0 (default Gamma(3,1)).
285	    """
286	    k = len(labels)
287	    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),
288	                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]
289	    chain_inits = chain_inits_pool[:n_chains]
290	    all_alpha, all_theta = [], []
291	    t0 = time.time()
292	
293	    for chain in range(n_chains):
294	        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)
295	        alpha = chain_inits[chain].copy()
296	        theta = np.ones((k, 2, 2)) * 0.5
297	        mh_scale = np.array([0.3, 0.3])
298	        accept_ct = np.array([0, 0])
299	        attempt_ct = np.array([0, 0])
300	
301	        alpha_samples = np.zeros((n_iter, 2))
302	        theta_samples = np.zeros((n_iter, k, 2, 2))
303	
304	        for it in range(n_warmup + n_iter):
305	            for z in [0, 1]:
306	                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0
307	                post_a = np.maximum(post_a, 1e-6)
308	                g = rng.gamma(post_a)
309	                g_sum = g.sum(axis=1, keepdims=True)
310	                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)
311	
312	            for z in [0, 1]:
313	                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])
314	                a_prop = np.exp(x_prop)
315	                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -
316	                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))
317	                accepted = np.log(rng.rand()) < log_r
318	                if accepted:
319	                    alpha[z] = a_prop
320	                if it < n_warmup:
321	                    accept_ct[z] += int(accepted)
322	                    attempt_ct[z] += 1
323	
324	            if it < n_warmup and it > 0 and it % 100 == 0:
325	                for z in [0, 1]:
326	                    rate = accept_ct[z] / max(attempt_ct[z], 1)
327	                    if rate < 0.2:
328	                        mh_scale[z] *= 0.7
329	                    elif rate > 0.5:
330	                        mh_scale[z] *= 1.3
331	                    accept_ct[z] = 0
332	                    attempt_ct[z] = 0
333	
334	            if it >= n_warmup:
335	                idx = it - n_warmup
336	                alpha_samples[idx] = alpha.copy()
337	                theta_samples[idx] = theta.copy()
338	
339	        all_alpha.append(alpha_samples)
340	        all_theta.append(theta_samples)
341	
342	    runtime = time.time() - t0
343	    alpha_arr = np.stack(all_alpha)
344	    theta_arr = np.stack(all_theta)
345	
346	    C = {}
347	    for i, s in enumerate(labels):
348	        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))
349	
350	    rhat_max, ess_min = _fast_diagnostics(alpha_arr, theta_arr, labels)
351	
352	    diag = {'rhat_max': rhat_max, 'ess_min': ess_min, 'divergent_count': 0,
353	            'runtime_seconds': runtime, 'hb_method': 'gibbs'}
354	    return C, diag
355	
356	
357	def estimate_cm_hb_mcmc(counts, labels, seed=42, draws=1000, tune=500, chains=2):
358	    """Full Bayesian HB with PyMC MCMC."""
359	    k = len(labels)
360	    n_per_sz = counts.sum(axis=2)
361	
362	    with pm.Model():
363	        alpha_0 = pm.Gamma('alpha_0', alpha=2, beta=1, shape=2)
364	        for z in [0, 1]:
365	            for i, s in enumerate(labels):
366	                nsz = int(n_per_sz[i, z])
367	                if nsz == 0:
368	                    continue
369	                a = pt.stack([alpha_0[z] / 2, alpha_0[z] / 2])
370	                theta = pm.Dirichlet(f'theta_{s}_z{z}', a=a)
371	                pm.Multinomial(f'obs_{s}_z{z}', n=nsz, p=theta,
372	                               observed=counts[i, z, :].astype('int32'))
373	        t0 = time.time()
374	        trace = pm.sample(draws=draws, tune=tune, chains=chains,
375	                          random_seed=seed, progressbar=False)
376	        runtime = time.time() - t0
377	
378	    C = {}
379	    for i, s in enumerate(labels):
380	        C_s = np.zeros((2, 2))
381	        for z in [0, 1]:
382	            vn = f'theta_{s}_z{z}'
383	            if vn in trace.posterior:
384	                C_s[z, :] = trace.posterior[vn].values.mean(axis=(0, 1))
385	            else:
386	                C_s[z, :] = 0.5
387	        C[s] = C_s
388	
389	    all_vars = list(trace.posterior.data_vars)
390	    try:
391	        summ = az.summary(trace, var_names=all_vars)
392	        rhat_max = float(summ['r_hat'].max())
393	        ess_min = float(summ['ess_bulk'].min())
394	    except Exception:
395	        rhat_max = ess_min = np.nan
396	    try:
397	        divergent = int(trace.sample_stats['diverging'].values.sum())
398	    except Exception:
399	        divergent = -1
400	
401	    diag = {'rhat_max': rhat_max, 'ess_min': ess_min,
402	            'divergent_count': divergent, 'runtime_seconds': runtime,
403	            'hb_method': 'mcmc'}
404	    return C, diag
405	
406	
407	# ── Single MC Run ─────────────────────────────────────────────────────────────
408	
409	def run_one_mc(regime_name, regime_params, n_expert, k, seed, hb_method='eb'):
410	    data = generate_data(regime_params, n_expert, k, seed)
411	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
412	    em = data['expert_mask']
413	    labels = SUBGROUP_LABELS[k]
414	    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']
415	
416	    counts = get_counts(Z[em], Z_hat[em], S[em], labels)
417	
418	    C_mle = estimate_cm_mle(counts, labels)
419	
420	    if hb_method == 'gibbs':
421	        C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed)
422	    elif hb_method == 'mcmc' and HAS_PYMC:
423	        try:
424	            C_hb, hb_diag = estimate_cm_hb_mcmc(counts, labels, seed=seed)
425	        except Exception:
426	            C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
427	            hb_diag['hb_method'] = 'eb_fallback'
428	    else:
429	        C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
430	
431	    # Global CM (pool all expert labels, Laplace)
432	    cg = counts.sum(axis=0)
433	    C_gl = np.zeros((2, 2))
434	    for z in [0, 1]:
435	        n = cg[z, :].sum()
436	        for zh in [0, 1]:
437	            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5
438	
439	    M_gl = build_mixing_matrix(C_gl)
440	    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}
441	    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}
442	
443	    base = {'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k, 'mc_run': seed}
444	    rows = []
445	
446	    for s in labels:
447	        sm = S == s
448	        th0_or, se0_or = diff_in_means(Y, T, sm & (Z == 0))
449	        th1_or, se1_or = diff_in_means(Y, T, sm & (Z == 1))
450	        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))
451	        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))
452	
453	        tau_obs = np.array([th0_n, th1_n])
454	        se_obs = np.array([se0_n, se1_n])
455	        if np.any(np.isnan(tau_obs)):
456	            continue
457	
458	        tgc, sgc = invert_mixing(M_gl, tau_obs, se_obs)
459	        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)
460	        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)
461	
462	        def mr(method, th0, th1, se0, se1):
463	            return {**base, 'subgroup': s, 'method': method,
464	                    'tau_hat_z0': th0, 'tau_hat_z1': th1,
465	                    'se_z0': se0, 'se_z1': se1,
466	                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}
467	
468	        rows.append(mr('oracle', th0_or, th1_or, se0_or, se1_or))
469	        rows.append(mr('naive', th0_n, th1_n, se0_n, se1_n))
470	        rows.append(mr('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]))
471	        rows.append(mr('mle_laplace', tml[0], tml[1], sml[0], sml[1]))
472	        rows.append(mr('hb_dirichlet', thb[0], thb[1], shb[0], shb[1]))
473	
474	    return rows, {**base, **hb_diag}
475	
476	
477	# ── Aggregation ───────────────────────────────────────────────────────────────
478	
479	def aggregate_results(df):
480	    rows = []
481	    grp_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method']
482	    for keys, grp in df.groupby(grp_cols):
483	        regime, n_expert, k, subgroup, method = keys
484	        row = {'regime': regime, 'n_expert': int(n_expert), 'k_subgroups': int(k),
485	               'subgroup': subgroup, 'method': method}
486	        n_mc = len(grp)
487	        for z in ['z0', 'z1']:
488	            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values
489	            bias = err.mean()
490	            mse = (err ** 2).mean()
491	            rmse = np.sqrt(mse)
492	            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values
493	            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values
494	            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &
495	                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()
496	            row[f'bias_{z}'] = bias
497	            row[f'rmse_{z}'] = rmse
498	            row[f'coverage_{z}'] = cov
499	            row[f'bias_{z}_se'] = err.std() / np.sqrt(n_mc)
500	            mse_se = (err ** 2).std() / np.sqrt(n_mc)
501	            row[f'rmse_{z}_se'] = mse_se / (2 * rmse) if rmse > 1e-10 else np.nan
502	        rows.append(row)
503	    return pd.DataFrame(rows)
504	
505	
506	# ── Output ────────────────────────────────────────────────────────────────────
507	
508	def print_summary(df_agg, df_diag):
509	    pd.set_option('display.float_format', '{:.4f}'.format)
510	
511	    # MCMC / Gibbs diagnostics
512	    if 'hb_method' in df_diag.columns:
513	        for method_label in ['gibbs', 'mcmc']:
514	            mrows = df_diag[df_diag['hb_method'] == method_label]
515	            if mrows.empty:
516	                continue
517	            print(f"\n── {method_label.upper()} Diagnostics ──────────────────────────────")
518	            print(f"  Runs:           {len(mrows)}")
519	            rh = mrows['rhat_max'].dropna()
520	            es = mrows['ess_min'].dropna()
521	            if not rh.empty:
522	                print(f"  R-hat max:      {rh.max():.4f} (target < 1.01)")
523	            if not es.empty:
524	                print(f"  ESS min:        {es.min():.0f} (target > 200)")
525	            print(f"  Divergent total:{int(mrows['divergent_count'].sum())}")
526	            print(f"  Runtime median: {mrows['runtime_seconds'].median():.2f}s")
527	
528	    # Per-config HB vs MLE comparison
529	    print("\n── HB vs MLE RMSE Comparison (subgroup-level, averaged) ──")
530	    for k in sorted(df_agg['k_subgroups'].unique()):
531	        print(f"\n  K = {int(k)} subgroups")
532	        for regime in ['extreme', 'moderate', 'homogeneous']:
533	            sub = df_agg[(df_agg['k_subgroups'] == k) & (df_agg['regime'] == regime)]
534	            if sub.empty:
535	                continue
536	            print(f"    {regime}:")
537	            print(f"    {'n_exp':>6s}  {'oracle':>8s}  {'naive':>8s}  {'global':>8s}  "
538	                  f"{'mle':>8s}  {'hb':>8s}  {'HB vs MLE':>10s}")
539	            for ne in sorted(sub['n_expert'].unique()):
540	                vals = {}
541	                for m in ['oracle', 'naive', 'global_corrected', 'mle_laplace', 'hb_dirichlet']:
542	                    ms = sub[(sub['method'] == m) & (sub['n_expert'] == ne)]
543	                    if ms.empty:
544	                        vals[m] = np.nan
545	                    else:
546	                        vals[m] = np.sqrt((ms['rmse_z0'].values ** 2 +
547	                                           ms['rmse_z1'].values ** 2).mean())
548	                mle_v, hb_v = vals['mle_laplace'], vals['hb_dirichlet']
549	                pct = (mle_v - hb_v) / mle_v * 100 if mle_v > 1e-10 else 0
550	                tag = f"{pct:+.1f}%"
551	                print(f"    {int(ne):6d}  {vals['oracle']:8.4f}  {vals['naive']:8.4f}  "
552	                      f"{vals['global_corrected']:8.4f}  {mle_v:8.4f}  {hb_v:8.4f}  {tag:>10s}")
553	
554	
555	# ── Sweep ─────────────────────────────────────────────────────────────────────
556	
557	def run_sweep(regime_names, n_experts, k_list, n_mc,
558	              hb_method='eb', mcmc_diag_runs=5, verbose=True):
559	    all_rows, all_diag = [], []
560	    total = sum(1 for k in k_list for r in regime_names if r in REGIMES[k]) * len(n_experts) * n_mc
561	    count = 0
562	    t0 = time.time()
563	
564	    for k in k_list:
565	        for rn in regime_names:
566	            if rn not in REGIMES[k]:
567	                continue
568	            rp = REGIMES[k][rn]
569	            for ne in n_experts:
570	                for mc in range(n_mc):
571	                    use = hb_method
572	                    if hb_method == 'auto':
573	                        use = 'mcmc' if mc < mcmc_diag_runs else 'eb'
574	                    try:
575	                        rows, diag = run_one_mc(rn, rp, ne, k, seed=mc, hb_method=use)
576	                        all_rows.extend(rows)
577	                        all_diag.append(diag)
578	                    except Exception as e:
579	                        if verbose:
580	                            print(f"  WARN: k={k} {rn} ne={ne} mc={mc} failed: {e}")
581	                        all_diag.append({
582	                            'regime': rn, 'n_expert': ne, 'k_subgroups': k,
583	                            'mc_run': mc, 'hb_method': 'error',
584	                            'rhat_max': np.nan, 'ess_min': np.nan,
585	                            'divergent_count': -1, 'runtime_seconds': 0.0})
586	                    count += 1
587	                    if verbose and count % max(1, total // 20) == 0:
588	                        el = time.time() - t0
589	                        eta = el / count * (total - count)
590	                        print(f"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s | "
591	                              f"k={k} {rn} ne={ne} mc={mc}")
592	
593	    if verbose:
594	        print(f"  Sweep done: {time.time() - t0:.1f}s ({count} runs)")
595	    return pd.DataFrame(all_rows), pd.DataFrame(all_diag)
596	
597	
598	# ── Main ──────────────────────────────────────────────────────────────────────
599	
600	if __name__ == '__main__':
601	    parser = argparse.ArgumentParser()
602	    parser.add_argument('--n-mc', type=int, default=100)
603	    parser.add_argument('--dry-run', action='store_true')
604	    parser.add_argument('--hb-method', choices=['auto', 'mcmc', 'gibbs', 'eb'], default='auto')
605	    parser.add_argument('--mcmc-diag-runs', type=int, default=5)
606	    args = parser.parse_args()
607	
608	    n_mc = 5 if args.dry_run else args.n_mc
609	    regime_names = ['moderate'] if args.dry_run else ['extreme', 'moderate', 'homogeneous']
610	    n_experts = [100] if args.dry_run else DEFAULT_N_EXPERTS
611	    k_list = [2] if args.dry_run else DEFAULT_K_LIST
612	
613	    print(f"exp-001 HB Synthetic Validation | PyMC={HAS_PYMC}")
614	    print(f"N={N} n_mc={n_mc} hb={args.hb_method}")
615	    print(f"Regimes={regime_names} n_experts={n_experts} K={k_list}\n")
616	
617	    # Timing test
618	    effective_method = args.hb_method
619	    d = generate_data(REGIMES[2]['moderate'], 100, 2, seed=9999)
620	    em = d['expert_mask']
621	    tc = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], ['A', 'B'])
622	
623	    if args.hb_method == 'auto':
624	        print("Timing Gibbs sampler...")
625	        t0 = time.time()
626	        _, dg = estimate_cm_hb_gibbs(tc, ['A', 'B'], seed=9999)
627	        gt = time.time() - t0
628	        print(f"  Gibbs: {gt:.2f}s | rhat={dg['rhat_max']:.3f} "
629	              f"ess={dg['ess_min']:.0f}")
630	        if gt < 5:
631	            effective_method = 'gibbs'
632	            print(f"  Fast enough → using Gibbs for all runs")
633	        else:
634	            effective_method = 'eb'
635	            print(f"  Slow → using EB")
636	    elif args.hb_method == 'mcmc' and HAS_PYMC:
637	        print("Timing PyMC MCMC...")
638	        t0 = time.time()
639	        try:
640	            _, dg = estimate_cm_hb_mcmc(tc, ['A', 'B'], seed=9999)
641	            mt = time.time() - t0
642	            print(f"  MCMC: {mt:.1f}s | rhat={dg['rhat_max']:.3f} "
643	                  f"ess={dg['ess_min']:.0f} div={dg['divergent_count']}")
644	        except Exception as e:
645	            print(f"  MCMC failed: {e} → falling back to Gibbs")
646	            effective_method = 'gibbs'
647	
648	    print(f"\nEffective method: {effective_method}\n")
649	
650	    df_raw, df_diag = run_sweep(
651	        regime_names, n_experts, k_list, n_mc,
652	        hb_method=effective_method, mcmc_diag_runs=args.mcmc_diag_runs)
653	
654	    df_agg = aggregate_results(df_raw)
655	
656	    os.makedirs('results', exist_ok=True)
657	    agg_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method',
658	                'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1',
659	                'bias_z0_se', 'rmse_z0_se', 'bias_z1_se', 'rmse_z1_se']
660	    df_agg[agg_cols].to_csv('results/exp001_hb_results.csv', index=False)
661	
662	    diag_cols = ['regime', 'n_expert', 'k_subgroups', 'mc_run',
663	                 'rhat_max', 'ess_min', 'divergent_count', 'runtime_seconds']
664	    save_cols = [c for c in diag_cols if c in df_diag.columns]
665	    if 'hb_method' in df_diag.columns:
666	        save_cols.insert(4, 'hb_method')
667	    df_diag[save_cols].to_csv('results/exp001_hb_diagnostics.csv', index=False)
668	
669	    print_summary(df_agg, df_diag)
670	
671	    print(f"\nSaved: results/exp001_hb_results.csv ({len(df_agg)} rows)")
672	    print(f"Saved: results/exp001_hb_diagnostics.csv ({len(df_diag)} rows)")
673	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87ad2995-ab36-41d7-9958-584927a84892",
  "isSidechain": false,
  "promptId": "99acad5a-cfb8-48f1-9a0e-e4eb1fe13a2c",
  "type": "user",
  "uuid": "2b362395-e358-45ff-bb36-0cf8837c180a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nexp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)\n\nCompares confusion matrix estimators for CATE correction under heterogeneous\nmisclassification across subgroups:\n  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)\n\nInput: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)\nOutput: results/exp001_hb_results.csv, results/exp001_hb_diagnostics.csv\n\"\"\"\n\nimport argparse\nimport os\nimport sys\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\nfrom scipy.optimize import minimize_scalar\n\nwarnings.filterwarnings('ignore')\n\ntry:\n    import pymc as pm\n    import pytensor.tensor as pt\n    import arviz as az\n    HAS_PYMC = True\nexcept ImportError:\n    HAS_PYMC = False\n\nN = 5000\nSUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}\n\nREGIMES = {\n    2: {\n        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},\n        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},\n        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},\n    },\n    4: {\n        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},\n        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},\n        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},\n    },\n}\n\nDEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]\nDEFAULT_K_LIST = [2, 4]\n\n\n# ── DGP ───────────────────────────────────────────────────────────────────────\n\ndef generate_data(regime_params, n_expert, k, seed):\n    rng = np.random.RandomState(seed)\n    labels = SUBGROUP_LABELS[k]\n    T = rng.binomial(1, 0.5, N)\n    Z = rng.binomial(1, 0.5, N)\n    S = rng.choice(labels, N, p=[1.0 / k] * k)\n    X = rng.randn(N, 5)\n    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])\n    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)\n    mc_rates = np.zeros(N)\n    for i, s in enumerate(labels):\n        mc_rates[S == s] = regime_params['misclass'][i]\n    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)\n    idx = rng.choice(N, min(n_expert, N), replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[idx] = True\n    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)\n\n\n# ── Helpers ───────────────────────────────────────────────────────────────────\n\ndef diff_in_means(Y, T, mask):\n    t1, t0 = mask & (T == 1), mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    \"\"\"Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat].\"\"\"\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef build_mixing_matrix(C):\n    \"\"\"C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5).\n\n    NOTE: This assumes P(Z=0)=P(Z=1)=0.5, which is correct for this experiment's\n    DGP. For general P(Z), use the version in exp007 that takes p_z and p_z_hat.\n    \"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        cs = C[0, zh] + C[1, zh]\n        if cs > 0:\n            M[zh, 0] = C[0, zh] / cs\n            M[zh, 1] = C[1, zh] / cs\n        else:\n            M[zh, :] = 0.5\n    return M\n\n\ndef invert_mixing(M, tau_obs, se_obs):\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\ndef safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):\n    \"\"\"Invert mixing matrix with condition number guard.\n\n    When cond(M_s) > threshold, matrix inversion is numerically unstable.\n    Falls back to naive (no correction) to avoid catastrophic amplification.\n    \"\"\"\n    cond = np.linalg.cond(M_s)\n    if cond > cond_threshold:\n        return tau_obs.copy()\n    return np.linalg.solve(M_s, tau_obs)\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    \"\"\"Like invert_mixing but with condition number guard.\"\"\"\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# ── Confusion Matrix Estimators ───────────────────────────────────────────────\n\ndef estimate_cm_mle(counts, labels):\n    \"\"\"Per-subgroup MLE with Laplace smoothing (add-1).\"\"\"\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            n = counts[i, z, :].sum()\n            for zh in [0, 1]:\n                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    \"\"\"Negative log marginal likelihood for Dirichlet-Multinomial.\"\"\"\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_eb(counts, labels):\n    \"\"\"Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean.\"\"\"\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = 2.0\n            continue\n        res = minimize_scalar(\n            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n = counts[i, z, :].sum()\n            d = n + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    diag = {'rhat_max': np.nan, 'ess_min': np.nan, 'divergent_count': 0,\n            'runtime_seconds': 0.0, 'hb_method': 'eb',\n            'alpha_0_z0': alpha_opt[0], 'alpha_0_z1': alpha_opt[1]}\n    return C, diag\n\n\ndef _split_rhat(chains):\n    \"\"\"Split R-hat for a scalar parameter. chains: (n_chains, n_draws).\"\"\"\n    parts = []\n    for c in range(chains.shape[0]):\n        half = chains.shape[1] // 2\n        parts.append(chains[c, :half])\n        parts.append(chains[c, half:2 * half])\n    parts = np.array(parts)\n    m = parts.shape[0]\n    n = parts.shape[1]\n    chain_means = parts.mean(axis=1)\n    W = np.mean(np.var(parts, axis=1, ddof=1))\n    B = n * np.var(chain_means, ddof=1)\n    if W < 1e-20:\n        return 1.0\n    var_hat = (1 - 1.0 / n) * W + B / n\n    return float(np.sqrt(var_hat / W))\n\n\ndef _bulk_ess(chains):\n    \"\"\"Approximate bulk ESS via initial positive sequence. chains: (n_chains, n_draws).\"\"\"\n    x = chains.ravel()\n    n = len(x)\n    mu = x.mean()\n    xc = x - mu\n    max_lag = min(n // 2, 300)\n    c0 = np.dot(xc, xc)\n    if c0 < 1e-20:\n        return float(n)\n    tau = 1.0\n    for lag in range(1, max_lag - 1, 2):\n        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0\n        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0\n        pair = r1 + r2\n        if pair < 0:\n            break\n        tau += 2 * pair\n    return float(n / tau)\n\n\ndef _fast_diagnostics(alpha_arr, theta_arr, labels):\n    \"\"\"Compute R-hat and ESS over all parameters without arviz.\"\"\"\n    rhats, esss = [], []\n    for d in range(alpha_arr.shape[2]):\n        rhats.append(_split_rhat(alpha_arr[:, :, d]))\n        esss.append(_bulk_ess(alpha_arr[:, :, d]))\n    k = len(labels)\n    for i in range(k):\n        for z in [0, 1]:\n            for zh in range(theta_arr.shape[4]):\n                ch = theta_arr[:, :, i, z, zh]\n                rhats.append(_split_rhat(ch))\n                esss.append(_bulk_ess(ch))\n    return max(rhats), min(esss)\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    \"\"\"Log posterior for alpha_0[z] in log-alpha space (includes Jacobian).\"\"\"\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=4000, n_warmup=2000, n_chains=4,\n                         hp_a0=3.0, hp_b0=1.0):\n    \"\"\"Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).\n\n    hp_a0, hp_b0: Gamma hyperprior shape/rate on alpha_0 (default Gamma(3,1)).\n    \"\"\"\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_alpha, all_theta = [], []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        alpha_samples = np.zeros((n_iter, 2))\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                idx = it - n_warmup\n                alpha_samples[idx] = alpha.copy()\n                theta_samples[idx] = theta.copy()\n\n        all_alpha.append(alpha_samples)\n        all_theta.append(theta_samples)\n\n    runtime = time.time() - t0\n    alpha_arr = np.stack(all_alpha)\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    rhat_max, ess_min = _fast_diagnostics(alpha_arr, theta_arr, labels)\n\n    diag = {'rhat_max': rhat_max, 'ess_min': ess_min, 'divergent_count': 0,\n            'runtime_seconds': runtime, 'hb_method': 'gibbs'}\n    return C, diag\n\n\ndef estimate_cm_hb_mcmc(counts, labels, seed=42, draws=1000, tune=500, chains=2):\n    \"\"\"Full Bayesian HB with PyMC MCMC.\"\"\"\n    k = len(labels)\n    n_per_sz = counts.sum(axis=2)\n\n    with pm.Model():\n        alpha_0 = pm.Gamma('alpha_0', alpha=2, beta=1, shape=2)\n        for z in [0, 1]:\n            for i, s in enumerate(labels):\n                nsz = int(n_per_sz[i, z])\n                if nsz == 0:\n                    continue\n                a = pt.stack([alpha_0[z] / 2, alpha_0[z] / 2])\n                theta = pm.Dirichlet(f'theta_{s}_z{z}', a=a)\n                pm.Multinomial(f'obs_{s}_z{z}', n=nsz, p=theta,\n                               observed=counts[i, z, :].astype('int32'))\n        t0 = time.time()\n        trace = pm.sample(draws=draws, tune=tune, chains=chains,\n                          random_seed=seed, progressbar=False)\n        runtime = time.time() - t0\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            vn = f'theta_{s}_z{z}'\n            if vn in trace.posterior:\n                C_s[z, :] = trace.posterior[vn].values.mean(axis=(0, 1))\n            else:\n                C_s[z, :] = 0.5\n        C[s] = C_s\n\n    all_vars = list(trace.posterior.data_vars)\n    try:\n        summ = az.summary(trace, var_names=all_vars)\n        rhat_max = float(summ['r_hat'].max())\n        ess_min = float(summ['ess_bulk'].min())\n    except Exception:\n        rhat_max = ess_min = np.nan\n    try:\n        divergent = int(trace.sample_stats['diverging'].values.sum())\n    except Exception:\n        divergent = -1\n\n    diag = {'rhat_max': rhat_max, 'ess_min': ess_min,\n            'divergent_count': divergent, 'runtime_seconds': runtime,\n            'hb_method': 'mcmc'}\n    return C, diag\n\n\n# ── Single MC Run ─────────────────────────────────────────────────────────────\n\ndef run_one_mc(regime_name, regime_params, n_expert, k, seed, hb_method='eb'):\n    data = generate_data(regime_params, n_expert, k, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    labels = SUBGROUP_LABELS[k]\n    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], labels)\n\n    C_mle = estimate_cm_mle(counts, labels)\n\n    if hb_method == 'gibbs':\n        C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed)\n    elif hb_method == 'mcmc' and HAS_PYMC:\n        try:\n            C_hb, hb_diag = estimate_cm_hb_mcmc(counts, labels, seed=seed)\n        except Exception:\n            C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)\n            hb_diag['hb_method'] = 'eb_fallback'\n    else:\n        C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)\n\n    # Global CM (pool all expert labels, Laplace)\n    cg = counts.sum(axis=0)\n    C_gl = np.zeros((2, 2))\n    for z in [0, 1]:\n        n = cg[z, :].sum()\n        for zh in [0, 1]:\n            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5\n\n    M_gl = build_mixing_matrix(C_gl)\n    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}\n\n    base = {'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k, 'mc_run': seed}\n    rows = []\n\n    for s in labels:\n        sm = S == s\n        th0_or, se0_or = diff_in_means(Y, T, sm & (Z == 0))\n        th1_or, se1_or = diff_in_means(Y, T, sm & (Z == 1))\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        tgc, sgc = invert_mixing(M_gl, tau_obs, se_obs)\n        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)\n        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)\n\n        def mr(method, th0, th1, se0, se1):\n            return {**base, 'subgroup': s, 'method': method,\n                    'tau_hat_z0': th0, 'tau_hat_z1': th1,\n                    'se_z0': se0, 'se_z1': se1,\n                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}\n\n        rows.append(mr('oracle', th0_or, th1_or, se0_or, se1_or))\n        rows.append(mr('naive', th0_n, th1_n, se0_n, se1_n))\n        rows.append(mr('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]))\n        rows.append(mr('mle_laplace', tml[0], tml[1], sml[0], sml[1]))\n        rows.append(mr('hb_dirichlet', thb[0], thb[1], shb[0], shb[1]))\n\n    return rows, {**base, **hb_diag}\n\n\n# ── Aggregation ───────────────────────────────────────────────────────────────\n\ndef aggregate_results(df):\n    rows = []\n    grp_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method']\n    for keys, grp in df.groupby(grp_cols):\n        regime, n_expert, k, subgroup, method = keys\n        row = {'regime': regime, 'n_expert': int(n_expert), 'k_subgroups': int(k),\n               'subgroup': subgroup, 'method': method}\n        n_mc = len(grp)\n        for z in ['z0', 'z1']:\n            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values\n            bias = err.mean()\n            mse = (err ** 2).mean()\n            rmse = np.sqrt(mse)\n            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values\n            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values\n            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &\n                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()\n            row[f'bias_{z}'] = bias\n            row[f'rmse_{z}'] = rmse\n            row[f'coverage_{z}'] = cov\n            row[f'bias_{z}_se'] = err.std() / np.sqrt(n_mc)\n            mse_se = (err ** 2).std() / np.sqrt(n_mc)\n            row[f'rmse_{z}_se'] = mse_se / (2 * rmse) if rmse > 1e-10 else np.nan\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# ── Output ────────────────────────────────────────────────────────────────────\n\ndef print_summary(df_agg, df_diag):\n    pd.set_option('display.float_format', '{:.4f}'.format)\n\n    # MCMC / Gibbs diagnostics\n    if 'hb_method' in df_diag.columns:\n        for method_label in ['gibbs', 'mcmc']:\n            mrows = df_diag[df_diag['hb_method'] == method_label]\n            if mrows.empty:\n                continue\n            print(f\"\\n── {method_label.upper()} Diagnostics ──────────────────────────────\")\n            print(f\"  Runs:           {len(mrows)}\")\n            rh = mrows['rhat_max'].dropna()\n            es = mrows['ess_min'].dropna()\n            if not rh.empty:\n                print(f\"  R-hat max:      {rh.max():.4f} (target < 1.01)\")\n            if not es.empty:\n                print(f\"  ESS min:        {es.min():.0f} (target > 200)\")\n            print(f\"  Divergent total:{int(mrows['divergent_count'].sum())}\")\n            print(f\"  Runtime median: {mrows['runtime_seconds'].median():.2f}s\")\n\n    # Per-config HB vs MLE comparison\n    print(\"\\n── HB vs MLE RMSE Comparison (subgroup-level, averaged) ──\")\n    for k in sorted(df_agg['k_subgroups'].unique()):\n        print(f\"\\n  K = {int(k)} subgroups\")\n        for regime in ['extreme', 'moderate', 'homogeneous']:\n            sub = df_agg[(df_agg['k_subgroups'] == k) & (df_agg['regime'] == regime)]\n            if sub.empty:\n                continue\n            print(f\"    {regime}:\")\n            print(f\"    {'n_exp':>6s}  {'oracle':>8s}  {'naive':>8s}  {'global':>8s}  \"\n                  f\"{'mle':>8s}  {'hb':>8s}  {'HB vs MLE':>10s}\")\n            for ne in sorted(sub['n_expert'].unique()):\n                vals = {}\n                for m in ['oracle', 'naive', 'global_corrected', 'mle_laplace', 'hb_dirichlet']:\n                    ms = sub[(sub['method'] == m) & (sub['n_expert'] == ne)]\n                    if ms.empty:\n                        vals[m] = np.nan\n                    else:\n                        vals[m] = np.sqrt((ms['rmse_z0'].values ** 2 +\n                                           ms['rmse_z1'].values ** 2).mean())\n                mle_v, hb_v = vals['mle_laplace'], vals['hb_dirichlet']\n                pct = (mle_v - hb_v) / mle_v * 100 if mle_v > 1e-10 else 0\n                tag = f\"{pct:+.1f}%\"\n                print(f\"    {int(ne):6d}  {vals['oracle']:8.4f}  {vals['naive']:8.4f}  \"\n                      f\"{vals['global_corrected']:8.4f}  {mle_v:8.4f}  {hb_v:8.4f}  {tag:>10s}\")\n\n\n# ── Sweep ─────────────────────────────────────────────────────────────────────\n\ndef run_sweep(regime_names, n_experts, k_list, n_mc,\n              hb_method='eb', mcmc_diag_runs=5, verbose=True):\n    all_rows, all_diag = [], []\n    total = sum(1 for k in k_list for r in regime_names if r in REGIMES[k]) * len(n_experts) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for k in k_list:\n        for rn in regime_names:\n            if rn not in REGIMES[k]:\n                continue\n            rp = REGIMES[k][rn]\n            for ne in n_experts:\n                for mc in range(n_mc):\n                    use = hb_method\n                    if hb_method == 'auto':\n                        use = 'mcmc' if mc < mcmc_diag_runs else 'eb'\n                    try:\n                        rows, diag = run_one_mc(rn, rp, ne, k, seed=mc, hb_method=use)\n                        all_rows.extend(rows)\n                        all_diag.append(diag)\n                    except Exception as e:\n                        if verbose:\n                            print(f\"  WARN: k={k} {rn} ne={ne} mc={mc} failed: {e}\")\n                        all_diag.append({\n                            'regime': rn, 'n_expert': ne, 'k_subgroups': k,\n                            'mc_run': mc, 'hb_method': 'error',\n                            'rhat_max': np.nan, 'ess_min': np.nan,\n                            'divergent_count': -1, 'runtime_seconds': 0.0})\n                    count += 1\n                    if verbose and count % max(1, total // 20) == 0:\n                        el = time.time() - t0\n                        eta = el / count * (total - count)\n                        print(f\"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s | \"\n                              f\"k={k} {rn} ne={ne} mc={mc}\")\n\n    if verbose:\n        print(f\"  Sweep done: {time.time() - t0:.1f}s ({count} runs)\")\n    return pd.DataFrame(all_rows), pd.DataFrame(all_diag)\n\n\n# ── Main ──────────────────────────────────────────────────────────────────────\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser()\n    parser.add_argument('--n-mc', type=int, default=100)\n    parser.add_argument('--dry-run', action='store_true')\n    parser.add_argument('--hb-method', choices=['auto', 'mcmc', 'gibbs', 'eb'], default='auto')\n    parser.add_argument('--mcmc-diag-runs', type=int, default=5)\n    args = parser.parse_args()\n\n    n_mc = 5 if args.dry_run else args.n_mc\n    regime_names = ['moderate'] if args.dry_run else ['extreme', 'moderate', 'homogeneous']\n    n_experts = [100] if args.dry_run else DEFAULT_N_EXPERTS\n    k_list = [2] if args.dry_run else DEFAULT_K_LIST\n\n    print(f\"exp-001 HB Synthetic Validation | PyMC={HAS_PYMC}\")\n    print(f\"N={N} n_mc={n_mc} hb={args.hb_method}\")\n    print(f\"Regimes={regime_names} n_experts={n_experts} K={k_list}\\n\")\n\n    # Timing test\n    effective_method = args.hb_method\n    d = generate_data(REGIMES[2]['moderate'], 100, 2, seed=9999)\n    em = d['expert_mask']\n    tc = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], ['A', 'B'])\n\n    if args.hb_method == 'auto':\n        print(\"Timing Gibbs sampler...\")\n        t0 = time.time()\n        _, dg = estimate_cm_hb_gibbs(tc, ['A', 'B'], seed=9999)\n        gt = time.time() - t0\n        print(f\"  Gibbs: {gt:.2f}s | rhat={dg['rhat_max']:.3f} \"\n              f\"ess={dg['ess_min']:.0f}\")\n        if gt < 5:\n            effective_method = 'gibbs'\n            print(f\"  Fast enough → using Gibbs for all runs\")\n        else:\n            effective_method = 'eb'\n            print(f\"  Slow → using EB\")\n    elif args.hb_method == 'mcmc' and HAS_PYMC:\n        print(\"Timing PyMC MCMC...\")\n        t0 = time.time()\n        try:\n            _, dg = estimate_cm_hb_mcmc(tc, ['A', 'B'], seed=9999)\n            mt = time.time() - t0\n            print(f\"  MCMC: {mt:.1f}s | rhat={dg['rhat_max']:.3f} \"\n                  f\"ess={dg['ess_min']:.0f} div={dg['divergent_count']}\")\n        except Exception as e:\n            print(f\"  MCMC failed: {e} → falling back to Gibbs\")\n            effective_method = 'gibbs'\n\n    print(f\"\\nEffective method: {effective_method}\\n\")\n\n    df_raw, df_diag = run_sweep(\n        regime_names, n_experts, k_list, n_mc,\n        hb_method=effective_method, mcmc_diag_runs=args.mcmc_diag_runs)\n\n    df_agg = aggregate_results(df_raw)\n\n    os.makedirs('results', exist_ok=True)\n    agg_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method',\n                'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1',\n                'bias_z0_se', 'rmse_z0_se', 'bias_z1_se', 'rmse_z1_se']\n    df_agg[agg_cols].to_csv('results/exp001_hb_results.csv', index=False)\n\n    diag_cols = ['regime', 'n_expert', 'k_subgroups', 'mc_run',\n                 'rhat_max', 'ess_min', 'divergent_count', 'runtime_seconds']\n    save_cols = [c for c in diag_cols if c in df_diag.columns]\n    if 'hb_method' in df_diag.columns:\n        save_cols.insert(4, 'hb_method')\n    df_diag[save_cols].to_csv('results/exp001_hb_diagnostics.csv', index=False)\n\n    print_summary(df_agg, df_diag)\n\n    print(f\"\\nSaved: results/exp001_hb_results.csv ({len(df_agg)} rows)\")\n    print(f\"Saved: results/exp001_hb_diagnostics.csv ({len(df_diag)} rows)\")\n",
      "numLines": 673,
      "startLine": 1,
      "totalLines": 673
    }
  },
  "sourceToolAssistantUUID": "87ad2995-ab36-41d7-9958-584927a84892",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T07:25:54.376Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0164ZPGXjLyduTxFZyZyi2FQ`</summary>

```json
{
  "command": "ls /home/ubuntu/ec_hte_llm_annotation/results/ 2>/dev/null; echo \"---\"; ls /home/ubuntu/ec_hte_llm_annotation/.venv/bin/python3 2>/dev/null",
  "description": "Check results dir and python path"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b362395-e358-45ff-bb36-0cf8837c180a",
  "isSidechain": false,
  "requestId": "req_011CbFKJCadSG4zDp7gHsEvb",
  "type": "assistant",
  "uuid": "848189c8-fe4d-40c6-90ae-9fec23c4e9d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AfTZ9NfUGPq9YukTT1cm46",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6574,
      "cache_read_input_tokens": 11841,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6574,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 6574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6574
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

_source line 12 · 2026-05-21T07:25:54.592Z_

<details><summary>↩ Tool result · `toolu_0164ZPGXjLyduTxFZyZyi2FQ`</summary>

```text
dataset_survey.md
exp001_full_run.log
exp001_hb_diagnostics.csv
exp001_hb_results.csv
exp001_hb_results_v2.csv
exp001_hyperprior_run.log
exp001_hyperprior_sensitivity.csv
exp001_reg_run.log
exp001_reg_v2_run.log
exp002_bias_bound.csv
exp002_bias_heatmap.csv
exp002_debiasing_hurts.csv
exp002_derivation.md
exp002_k4_validation.csv
exp002_run.log
exp003_dgp_spec.md
exp003_hb_rerun.log
exp003_phase_a.csv
exp003_phase_a_raw.csv
exp003_phase_a_v2.csv
exp003_phase_a_v2_raw.csv
exp003_phase_a_v3.csv
exp003_phase_a_v3_raw.csv
exp003_run.log
exp003_v2_run.log
exp005_diagnostic.csv
exp005_diagnostic_subgroups.csv
exp005_roc.png
exp006_budget_sensitivity.csv
exp006_crossover.csv
exp006_run.log
exp007_full_run.log
exp007_hb_run.log
exp007_ppci_dsl.csv
exp007_ppci_dsl_hb.csv.broken
exp007_ppci_dsl_hb_raw.csv.broken
exp007_ppci_dsl_raw.csv
exp007_run.log
exp011_causal_forest.csv
exp011_run.log
llm_alternatives_assessment.md
mvp_results.csv
mvp_results_raw.csv
mvp_results_v2.csv
mvp_results_v2_raw.csv
mvp_results_v3.csv
mvp_results_v3_raw.csv
mvp_v2_100mc_log.txt
pilot_gemini_annotations.csv
pilot_gemini_run.log
pilot_gpt41_analysis.md
pilot_gpt41_run.log
pilot_llm_annotations.csv
pilot_subgroup_stats.csv
tweeteval_exploration.md
tweeteval_raw.json
ucb_hate_speech_exploration.md
---
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/python3
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "848189c8-fe4d-40c6-90ae-9fec23c4e9d6",
  "isSidechain": false,
  "promptId": "99acad5a-cfb8-48f1-9a0e-e4eb1fe13a2c",
  "type": "user",
  "uuid": "1535451c-5023-4e68-96df-31bcc8739538",
  "toolUseResult": {
    "stdout": "dataset_survey.md\nexp001_full_run.log\nexp001_hb_diagnostics.csv\nexp001_hb_results.csv\nexp001_hb_results_v2.csv\nexp001_hyperprior_run.log\nexp001_hyperprior_sensitivity.csv\nexp001_reg_run.log\nexp001_reg_v2_run.log\nexp002_bias_bound.csv\nexp002_bias_heatmap.csv\nexp002_debiasing_hurts.csv\nexp002_derivation.md\nexp002_k4_validation.csv\nexp002_run.log\nexp003_dgp_spec.md\nexp003_hb_rerun.log\nexp003_phase_a.csv\nexp003_phase_a_raw.csv\nexp003_phase_a_v2.csv\nexp003_phase_a_v2_raw.csv\nexp003_phase_a_v3.csv\nexp003_phase_a_v3_raw.csv\nexp003_run.log\nexp003_v2_run.log\nexp005_diagnostic.csv\nexp005_diagnostic_subgroups.csv\nexp005_roc.png\nexp006_budget_sensitivity.csv\nexp006_crossover.csv\nexp006_run.log\nexp007_full_run.log\nexp007_hb_run.log\nexp007_ppci_dsl.csv\nexp007_ppci_dsl_hb.csv.broken\nexp007_ppci_dsl_hb_raw.csv.broken\nexp007_ppci_dsl_raw.csv\nexp007_run.log\nexp011_causal_forest.csv\nexp011_run.log\nllm_alternatives_assessment.md\nmvp_results.csv\nmvp_results_raw.csv\nmvp_results_v2.csv\nmvp_results_v2_raw.csv\nmvp_results_v3.csv\nmvp_results_v3_raw.csv\nmvp_v2_100mc_log.txt\npilot_gemini_annotations.csv\npilot_gemini_run.log\npilot_gpt41_analysis.md\npilot_gpt41_run.log\npilot_llm_annotations.csv\npilot_subgroup_stats.csv\ntweeteval_exploration.md\ntweeteval_raw.json\nucb_hate_speech_exploration.md\n---\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/python3",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "848189c8-fe4d-40c6-90ae-9fec23c4e9d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "leafUuid": "1535451c-5023-4e68-96df-31bcc8739538",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Implement boundary condition experiment exp013",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7"
}
```

---

### Assistant

_source line 15 · 2026-05-21T07:26:01.594Z_

<details><summary>Logged reasoning block</summary>

```text
I've read the full base script. Now I understand the structure. Let me create the exp013 script that:

1. Imports core functions from exp001
2. Runs only K=4, extreme, n_expert=50
3. 100 MC runs (with --dry-run for 5)
4. Outputs per-run detail CSV and summary CSV
5. Generates analysis markdown

Let me create the script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1535451c-5023-4e68-96df-31bcc8739538",
  "isSidechain": false,
  "requestId": "req_011CbFKJYceEVmCs6kLq7vrU",
  "type": "assistant",
  "uuid": "841ac542-95ce-4092-86bc-5876049835fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wg2dzZcgk13B1ZT4qG7Xjj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12439,
      "cache_read_input_tokens": 18415,
      "output_tokens": 4434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12439,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4434,
          "cache_read_input_tokens": 18415,
          "cache_creation_input_tokens": 12439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12439
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

_source line 16 · 2026-05-21T07:26:01.626Z_

Now I have the full picture. Creating the exp013 script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "841ac542-95ce-4092-86bc-5876049835fb",
  "isSidechain": false,
  "requestId": "req_011CbFKJYceEVmCs6kLq7vrU",
  "type": "assistant",
  "uuid": "9bcbbdf4-7a3e-4ac6-b0ea-a019f8ca6f71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wg2dzZcgk13B1ZT4qG7Xjj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12439,
      "cache_read_input_tokens": 18415,
      "output_tokens": 4434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12439,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4434,
          "cache_read_input_tokens": 18415,
          "cache_creation_input_tokens": 12439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12439
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

_source line 17 · 2026-05-21T07:26:54.298Z_

<details open><summary>🔧 Tool call — Write · `toolu_013m3tYmdkk3VabFhZLwKcUL`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp013_boundary_condition.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nexp013_boundary_condition.py - Boundary condition test: n_expert=50, K=4, extreme regime.\n\nWith only ~12.5 expert labels per subgroup, per-subgroup CM estimation is extremely noisy.\nTests whether stratified methods degrade vs global correction under these conditions.\n\"\"\"\n\nimport argparse\nimport os\nimport time\nimport numpy as np\nimport pandas as pd\n\nfrom exp001_hb_synthetic import (\n    generate_data, get_counts, estimate_cm_mle, estimate_cm_hb_eb,\n    estimate_cm_hb_gibbs, build_mixing_matrix, invert_mixing_safe,\n    diff_in_means, REGIMES, SUBGROUP_LABELS, N,\n)\n\nK = 4\nREGIME_NAME = 'extreme'\nREGIME_PARAMS = REGIMES[K][REGIME_NAME]\nN_EXPERT = 50\nLABELS = SUBGROUP_LABELS[K]\n\n\ndef run_one(seed, hb_method='eb'):\n    data = generate_data(REGIME_PARAMS, N_EXPERT, K, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    tau_z0, tau_z1 = REGIME_PARAMS['tau_z0'], REGIME_PARAMS['tau_z1']\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], LABELS)\n\n    C_mle = estimate_cm_mle(counts, LABELS)\n    if hb_method == 'gibbs':\n        C_hb, _ = estimate_cm_hb_gibbs(counts, LABELS, seed=seed)\n    else:\n        C_hb, _ = estimate_cm_hb_eb(counts, LABELS)\n\n    cg = counts.sum(axis=0)\n    C_gl = np.zeros((2, 2))\n    for z in [0, 1]:\n        n = cg[z, :].sum()\n        for zh in [0, 1]:\n            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5\n\n    M_gl = build_mixing_matrix(C_gl)\n    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in LABELS}\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in LABELS}\n\n    rows = []\n    for s in LABELS:\n        sm = S == s\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        tgc, sgc = invert_mixing_safe(M_gl, tau_obs, se_obs)\n        tml, sml = invert_mixing_safe(M_mle[s], tau_obs, se_obs)\n        thb, shb = invert_mixing_safe(M_hb[s], tau_obs, se_obs)\n\n        for method, t0, t1, s0, s1 in [\n            ('naive',            th0_n, th1_n, se0_n, se1_n),\n            ('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]),\n            ('mle_laplace',      tml[0], tml[1], sml[0], sml[1]),\n            ('hb_eb',            thb[0], thb[1], shb[0], shb[1]),\n        ]:\n            for z_label, tau_c, se_c, tau_true in [\n                ('z0', t0, s0, tau_z0), ('z1', t1, s1, tau_z1)\n            ]:\n                lo = tau_c - 1.96 * se_c\n                hi = tau_c + 1.96 * se_c\n                rows.append({\n                    'mc_run': seed, 'subgroup': s, 'method': method,\n                    'z_level': z_label,\n                    'tau_corrected': tau_c, 'tau_true': tau_true,\n                    'se_corrected': se_c,\n                    'coverage': int(lo <= tau_true <= hi),\n                })\n    return rows\n\n\ndef summarize(df):\n    rows = []\n    for (sg, method, z), grp in df.groupby(['subgroup', 'method', 'z_level']):\n        err = grp['tau_corrected'].values - grp['tau_true'].values\n        n_mc = len(grp)\n        bias = err.mean()\n        rmse = np.sqrt((err ** 2).mean())\n        cov = grp['coverage'].mean()\n        rows.append({\n            'subgroup': sg, 'method': method, 'z_level': z,\n            'bias': bias, 'abs_bias': abs(bias), 'rmse': rmse, 'coverage': cov,\n            'bias_se': err.std() / np.sqrt(n_mc),\n            'rmse_se': (err ** 2).std() / np.sqrt(n_mc) / (2 * rmse) if rmse > 1e-10 else np.nan,\n            'coverage_se': np.sqrt(cov * (1 - cov) / n_mc),\n            'n_mc': n_mc,\n        })\n    return pd.DataFrame(rows)\n\n\ndef write_analysis(df_summary):\n    methods = ['naive', 'global_corrected', 'mle_laplace', 'hb_eb']\n    subgroups = list(LABELS)\n    misclass = dict(zip(LABELS, REGIME_PARAMS['misclass']))\n\n    lines = [\n        '# exp-013: Boundary Condition Analysis',\n        f'',\n        f'**Config**: K={K}, regime={REGIME_NAME}, n_expert={N_EXPERT}, '\n        f'N={N}, misclass={REGIME_PARAMS[\"misclass\"]}',\n        f'',\n        f'Each subgroup gets ~{N_EXPERT / K:.0f} expert labels.',\n        '',\n        '## Per-subgroup Results',\n        '',\n    ]\n\n    header = '| Subgroup (pi) | Method | |Bias|_z0 | RMSE_z0 | Cov_z0 | |Bias|_z1 | RMSE_z1 | Cov_z1 |'\n    sep =    '|---|---|---|---|---|---|---|---|'\n    lines += [header, sep]\n\n    for s in subgroups:\n        for m in methods:\n            r0 = df_summary[(df_summary['subgroup'] == s) & (df_summary['method'] == m) & (df_summary['z_level'] == 'z0')]\n            r1 = df_summary[(df_summary['subgroup'] == s) & (df_summary['method'] == m) & (df_summary['z_level'] == 'z1')]\n            if r0.empty or r1.empty:\n                continue\n            r0, r1 = r0.iloc[0], r1.iloc[0]\n            lines.append(\n                f'| {s} ({misclass[s]:.2f}) | {m} | '\n                f'{r0[\"abs_bias\"]:.4f} | {r0[\"rmse\"]:.4f} | {r0[\"coverage\"]:.2f} | '\n                f'{r1[\"abs_bias\"]:.4f} | {r1[\"rmse\"]:.4f} | {r1[\"coverage\"]:.2f} |'\n            )\n\n    lines += ['', '## Average Across Subgroups', '']\n    lines += [\n        '| Method | |Bias|_z0 | RMSE_z0 | Cov_z0 | |Bias|_z1 | RMSE_z1 | Cov_z1 |',\n        '|---|---|---|---|---|---|---|',\n    ]\n    for m in methods:\n        msub = df_summary[df_summary['method'] == m]\n        r0 = msub[msub['z_level'] == 'z0']\n        r1 = msub[msub['z_level'] == 'z1']\n        if r0.empty or r1.empty:\n            continue\n        lines.append(\n            f'| {m} | '\n            f'{r0[\"abs_bias\"].mean():.4f} | {r0[\"rmse\"].mean():.4f} | {r0[\"coverage\"].mean():.2f} | '\n            f'{r1[\"abs_bias\"].mean():.4f} | {r1[\"rmse\"].mean():.4f} | {r1[\"coverage\"].mean():.2f} |'\n        )\n\n    lines += ['', '## RMSE Amplification (stratified vs global)', '']\n    gl_rmse = {}\n    for z in ['z0', 'z1']:\n        r = df_summary[(df_summary['method'] == 'global_corrected') & (df_summary['z_level'] == z)]\n        gl_rmse[z] = r['rmse'].mean() if not r.empty else np.nan\n\n    lines += ['| Subgroup | Method | RMSE_z0 / Global | RMSE_z1 / Global |', '|---|---|---|---|']\n    for s in subgroups:\n        for m in ['mle_laplace', 'hb_eb']:\n            r0 = df_summary[(df_summary['subgroup'] == s) & (df_summary['method'] == m) & (df_summary['z_level'] == 'z0')]\n            r1 = df_summary[(df_summary['subgroup'] == s) & (df_summary['method'] == m) & (df_summary['z_level'] == 'z1')]\n            if r0.empty or r1.empty:\n                continue\n            amp0 = r0.iloc[0]['rmse'] / gl_rmse['z0'] if gl_rmse['z0'] > 1e-10 else np.nan\n            amp1 = r1.iloc[0]['rmse'] / gl_rmse['z1'] if gl_rmse['z1'] > 1e-10 else np.nan\n            lines.append(f'| {s} ({misclass[s]:.2f}) | {m} | {amp0:.2f}x | {amp1:.2f}x |')\n\n    # Analysis\n    worst_sg = None\n    worst_rmse = 0\n    for s in subgroups:\n        for m in ['mle_laplace', 'hb_eb']:\n            for z in ['z0', 'z1']:\n                r = df_summary[(df_summary['subgroup'] == s) & (df_summary['method'] == m) & (df_summary['z_level'] == z)]\n                if not r.empty and r.iloc[0]['rmse'] > worst_rmse:\n                    worst_rmse = r.iloc[0]['rmse']\n                    worst_sg = (s, m, z)\n\n    lines += ['', '## Key Findings', '']\n    if worst_sg:\n        lines.append(f'1. **Worst degradation**: subgroup {worst_sg[0]} ({worst_sg[1]}, {worst_sg[2]}) '\n                      f'with RMSE={worst_rmse:.4f}')\n\n    avg_strat_rmse_z0 = df_summary[(df_summary['method'].isin(['mle_laplace', 'hb_eb'])) & (df_summary['z_level'] == 'z0')]['rmse'].mean()\n    avg_strat_rmse_z1 = df_summary[(df_summary['method'].isin(['mle_laplace', 'hb_eb'])) & (df_summary['z_level'] == 'z1')]['rmse'].mean()\n    lines.append(f'2. **Average stratified RMSE**: z0={avg_strat_rmse_z0:.4f}, z1={avg_strat_rmse_z1:.4f} '\n                 f'vs global z0={gl_rmse[\"z0\"]:.4f}, z1={gl_rmse[\"z1\"]:.4f}')\n    amp_z0 = avg_strat_rmse_z0 / gl_rmse['z0'] if gl_rmse['z0'] > 1e-10 else np.nan\n    amp_z1 = avg_strat_rmse_z1 / gl_rmse['z1'] if gl_rmse['z1'] > 1e-10 else np.nan\n    lines.append(f'3. **Amplification factor**: {amp_z0:.2f}x (z0), {amp_z1:.2f}x (z1)')\n\n    threshold_met = N_EXPERT / K >= 25\n    lines.append(f'4. **n_expert/K = {N_EXPERT / K:.1f}** {\">=25 threshold met\" if threshold_met else \"< 25 threshold NOT met\"}. '\n                 f'{\"Stratified methods should be usable.\" if threshold_met else \"Below recommended minimum — expect high variance in per-subgroup estimates.\"}')\n\n    # EB vs MLE comparison\n    eb_rmse = df_summary[df_summary['method'] == 'hb_eb']['rmse'].mean()\n    mle_rmse = df_summary[df_summary['method'] == 'mle_laplace']['rmse'].mean()\n    if mle_rmse > 1e-10:\n        pct = (mle_rmse - eb_rmse) / mle_rmse * 100\n        lines.append(f'5. **EB vs MLE**: EB RMSE {pct:+.1f}% relative to MLE '\n                     f'({\"EB helps with shrinkage\" if pct > 0 else \"MLE competitive\"})')\n\n    lines.append('')\n    return '\\n'.join(lines)\n\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument('--n-mc', type=int, default=100)\n    parser.add_argument('--dry-run', action='store_true')\n    parser.add_argument('--hb-method', choices=['eb', 'gibbs'], default='eb')\n    args = parser.parse_args()\n\n    n_mc = 5 if args.dry_run else args.n_mc\n    tag = ' (DRY RUN)' if args.dry_run else ''\n    print(f'exp-013 Boundary Condition{tag} | K={K} {REGIME_NAME} n_expert={N_EXPERT} n_mc={n_mc} hb={args.hb_method}')\n\n    all_rows = []\n    t0 = time.time()\n    for mc in range(n_mc):\n        rows = run_one(mc, hb_method=args.hb_method)\n        all_rows.extend(rows)\n        if (mc + 1) % max(1, n_mc // 10) == 0:\n            el = time.time() - t0\n            print(f'  [{mc + 1}/{n_mc}] {el:.1f}s elapsed')\n\n    print(f'  Done: {time.time() - t0:.1f}s ({len(all_rows)} rows)')\n\n    df = pd.DataFrame(all_rows)\n    df_summary = summarize(df)\n\n    os.makedirs('results', exist_ok=True)\n    df.to_csv('results/exp013_boundary_condition.csv', index=False)\n    df_summary.to_csv('results/exp013_boundary_summary.csv', index=False)\n    print(f'Saved: results/exp013_boundary_condition.csv ({len(df)} rows)')\n    print(f'Saved: results/exp013_boundary_summary.csv ({len(df_summary)} rows)')\n\n    analysis = write_analysis(df_summary)\n    with open('results/exp013_boundary_analysis.md', 'w') as f:\n        f.write(analysis)\n    print(f'Saved: results/exp013_boundary_analysis.md')\n\n    print('\\n' + analysis)\n\n\nif __name__ == '__main__':\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bcbbdf4-7a3e-4ac6-b0ea-a019f8ca6f71",
  "isSidechain": false,
  "requestId": "req_011CbFKJYceEVmCs6kLq7vrU",
  "type": "assistant",
  "uuid": "f557b18a-c359-46aa-b90a-6b7b60b36a33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wg2dzZcgk13B1ZT4qG7Xjj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12439,
      "cache_read_input_tokens": 18415,
      "output_tokens": 4434,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12439,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4434,
          "cache_read_input_tokens": 18415,
          "cache_creation_input_tokens": 12439,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12439
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

_source line 18 · 2026-05-21T07:26:54.341Z_

<details><summary>↩ Tool result · `toolu_013m3tYmdkk3VabFhZLwKcUL`</summary>

```text
File created successfully at: /home/ubuntu/ec_hte_llm_annotation/exp013_boundary_condition.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f557b18a-c359-46aa-b90a-6b7b60b36a33",
  "isSidechain": false,
  "promptId": "99acad5a-cfb8-48f1-9a0e-e4eb1fe13a2c",
  "type": "user",
  "uuid": "a31485f7-33d1-4b0a-b7f9-42c24f73800f",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp013_boundary_condition.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nexp013_boundary_condition.py - Boundary condition test: n_expert=50, K=4, extreme regime.\n\nWith only ~12.5 expert labels per subgroup, per-subgroup CM estimation is extremely noisy.\nTests whether stratified methods degrade vs global correction under these conditions.\n\"\"\"\n\nimport argparse\nimport os\nimport time\nimport numpy as np\nimport pandas as pd\n\nfrom exp001_hb_synthetic import (\n    generate_data, get_counts, estimate_cm_mle, estimate_cm_hb_eb,\n    estimate_cm_hb_gibbs, build_mixing_matrix, invert_mixing_safe,\n    diff_in_means, REGIMES, SUBGROUP_LABELS, N,\n)\n\nK = 4\nREGIME_NAME = 'extreme'\nREGIME_PARAMS = REGIMES[K][REGIME_NAME]\nN_EXPERT = 50\nLABELS = SUBGROUP_LABELS[K]\n\n\ndef run_one(seed, hb_method='eb'):\n    data = generate_data(REGIME_PARAMS, N_EXPERT, K, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    tau_z0, tau_z1 = REGIME_PARAMS['tau_z0'], REGIME_PARAMS['tau_z1']\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], LABELS)\n\n    C_mle = estimate_cm_mle(counts, LABELS)\n    if hb_method == 'gibbs':\n        C_hb, _ = estimate_cm_hb_gibbs(counts, LABELS, seed=seed)\n    else:\n        C_hb, _ = estimate_cm_hb_eb(counts, LABELS)\n\n    cg = counts.sum(axis=0)\n    C_gl = np.zeros((2, 2))\n    for z in [0, 1]:\n        n = cg[z, :].sum()\n        for zh in [0, 1]:\n            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5\n\n    M_gl = build_mixing_matrix(C_gl)\n    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in LABELS}\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in LABELS}\n\n    rows = []\n    for s in LABELS:\n        sm = S == s\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        tgc, sgc = invert_mixing_safe(M_gl, tau_obs, se_obs)\n        tml, sml = invert_mixing_safe(M_mle[s], tau_obs, se_obs)\n        thb, shb = invert_mixing_safe(M_hb[s], tau_obs, se_obs)\n\n        for method, t0, t1, s0, s1 in [\n            ('naive',            th0_n, th1_n, se0_n, se1_n),\n            ('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]),\n            ('mle_laplace',      tml[0], tml[1], sml[0], sml[1]),\n            ('hb_eb',            thb[0], thb[1], shb[0], shb[1]),\n        ]:\n            for z_label, tau_c, se_c, tau_true in [\n                ('z0', t0, s0, tau_z0), ('z1', t1, s1, tau_z1)\n            ]:\n                lo = tau_c - 1.96 * se_c\n                hi = tau_c + 1.96 * se_c\n                rows.append({\n                    'mc_run': seed, 'subgroup': s, 'method': method,\n                    'z_level': z_label,\n                    'tau_corrected': tau_c, 'tau_true': tau_true,\n                    'se_corrected': se_c,\n                    'coverage': int(lo <= tau_true <= hi),\n                })\n    return rows\n\n\ndef summarize(df):\n    rows = []\n    for (sg, method, z), grp in df.groupby(['subgroup', 'method', 'z_level']):\n        err = grp['tau_corrected'].values - grp['tau_true'].values\n        n_mc = len(grp)\n        bias = err.mean()\n        rmse = np.sqrt((err ** 2).mean())\n        cov = grp['coverage'].mean()\n        rows.append({\n            'subgroup': sg, 'method': method, 'z_level': z,\n            'bias': bias, 'abs_bias': abs(bias), 'rmse': rmse, 'coverage': cov,\n            'bias_se': err.std() / np.sqrt(n_mc),\n            'rmse_se': (err ** 2).std() / np.sqrt(n_mc) / (2 * rmse) if rmse > 1e-10 else np.nan,\n            'coverage_se': np.sqrt(cov * (1 - cov) / n_mc),\n            'n_mc': n_mc,\n        })\n    return pd.DataFrame(rows)\n\n\ndef write_analysis(df_summary):\n    methods = ['naive', 'global_corrected', 'mle_laplace', 'hb_eb']\n    subgroups = list(LABELS)\n    misclass = dict(zip(LABELS, REGIME_PARAMS['misclass']))\n\n    lines = [\n        '# exp-013: Boundary Condition Analysis',\n        f'',\n        f'**Config**: K={K}, regime={REGIME_NAME}, n_expert={N_EXPERT}, '\n        f'N={N}, misclass={REGIME_PARAMS[\"misclass\"]}',\n        f'',\n        f'Each subgroup gets ~{N_EXPERT / K:.0f} expert labels.',\n        '',\n        '## Per-subgroup Results',\n        '',\n    ]\n\n    header = '| Subgroup (pi) | Method | |Bias|_z0 | RMSE_z0 | Cov_z0 | |Bias|_z1 | RMSE_z1 | Cov_z1 |'\n    sep =    '|---|---|---|---|---|---|---|---|'\n    lines += [header, sep]\n\n    for s in subgroups:\n        for m in methods:\n            r0 = df_summary[(df_summary['subgroup'] == s) & (df_summary['method'] == m) & (df_summary['z_level'] == 'z0')]\n            r1 = df_summary[(df_summary['subgroup'] == s) & (df_summary['method'] == m) & (df_summary['z_level'] == 'z1')]\n            if r0.empty or r1.empty:\n                continue\n            r0, r1 = r0.iloc[0], r1.iloc[0]\n            lines.append(\n                f'| {s} ({misclass[s]:.2f}) | {m} | '\n                f'{r0[\"abs_bias\"]:.4f} | {r0[\"rmse\"]:.4f} | {r0[\"coverage\"]:.2f} | '\n                f'{r1[\"abs_bias\"]:.4f} | {r1[\"rmse\"]:.4f} | {r1[\"coverage\"]:.2f} |'\n            )\n\n    lines += ['', '## Average Across Subgroups', '']\n    lines += [\n        '| Method | |Bias|_z0 | RMSE_z0 | Cov_z0 | |Bias|_z1 | RMSE_z1 | Cov_z1 |',\n        '|---|---|---|---|---|---|---|',\n    ]\n    for m in methods:\n        msub = df_summary[df_summary['method'] == m]\n        r0 = msub[msub['z_level'] == 'z0']\n        r1 = msub[msub['z_level'] == 'z1']\n        if r0.empty or r1.empty:\n            continue\n        lines.append(\n            f'| {m} | '\n            f'{r0[\"abs_bias\"].mean():.4f} | {r0[\"rmse\"].mean():.4f} | {r0[\"coverage\"].mean():.2f} | '\n            f'{r1[\"abs_bias\"].mean():.4f} | {r1[\"rmse\"].mean():.4f} | {r1[\"coverage\"].mean():.2f} |'\n        )\n\n    lines += ['', '## RMSE Amplification (stratified vs global)', '']\n    gl_rmse = {}\n    for z in ['z0', 'z1']:\n        r = df_summary[(df_summary['method'] == 'global_corrected') & (df_summary['z_level'] == z)]\n        gl_rmse[z] = r['rmse'].mean() if not r.empty else np.nan\n\n    lines += ['| Subgroup | Method | RMSE_z0 / Global | RMSE_z1 / Global |', '|---|---|---|---|']\n    for s in subgroups:\n        for m in ['mle_laplace', 'hb_eb']:\n            r0 = df_summary[(df_summary['subgroup'] == s) & (df_summary['method'] == m) & (df_summary['z_level'] == 'z0')]\n            r1 = df_summary[(df_summary['subgroup'] == s) & (df_summary['method'] == m) & (df_summary['z_level'] == 'z1')]\n            if r0.empty or r1.empty:\n                continue\n            amp0 = r0.iloc[0]['rmse'] / gl_rmse['z0'] if gl_rmse['z0'] > 1e-10 else np.nan\n            amp1 = r1.iloc[0]['rmse'] / gl_rmse['z1'] if gl_rmse['z1'] > 1e-10 else np.nan\n            lines.append(f'| {s} ({misclass[s]:.2f}) | {m} | {amp0:.2f}x | {amp1:.2f}x |')\n\n    # Analysis\n    worst_sg = None\n    worst_rmse = 0\n    for s in subgroups:\n        for m in ['mle_laplace', 'hb_eb']:\n            for z in ['z0', 'z1']:\n                r = df_summary[(df_summary['subgroup'] == s) & (df_summary['method'] == m) & (df_summary['z_level'] == z)]\n                if not r.empty and r.iloc[0]['rmse'] > worst_rmse:\n                    worst_rmse = r.iloc[0]['rmse']\n                    worst_sg = (s, m, z)\n\n    lines += ['', '## Key Findings', '']\n    if worst_sg:\n        lines.append(f'1. **Worst degradation**: subgroup {worst_sg[0]} ({worst_sg[1]}, {worst_sg[2]}) '\n                      f'with RMSE={worst_rmse:.4f}')\n\n    avg_strat_rmse_z0 = df_summary[(df_summary['method'].isin(['mle_laplace', 'hb_eb'])) & (df_summary['z_level'] == 'z0')]['rmse'].mean()\n    avg_strat_rmse_z1 = df_summary[(df_summary['method'].isin(['mle_laplace', 'hb_eb'])) & (df_summary['z_level'] == 'z1')]['rmse'].mean()\n    lines.append(f'2. **Average stratified RMSE**: z0={avg_strat_rmse_z0:.4f}, z1={avg_strat_rmse_z1:.4f} '\n                 f'vs global z0={gl_rmse[\"z0\"]:.4f}, z1={gl_rmse[\"z1\"]:.4f}')\n    amp_z0 = avg_strat_rmse_z0 / gl_rmse['z0'] if gl_rmse['z0'] > 1e-10 else np.nan\n    amp_z1 = avg_strat_rmse_z1 / gl_rmse['z1'] if gl_rmse['z1'] > 1e-10 else np.nan\n    lines.append(f'3. **Amplification factor**: {amp_z0:.2f}x (z0), {amp_z1:.2f}x (z1)')\n\n    threshold_met = N_EXPERT / K >= 25\n    lines.append(f'4. **n_expert/K = {N_EXPERT / K:.1f}** {\">=25 threshold met\" if threshold_met else \"< 25 threshold NOT met\"}. '\n                 f'{\"Stratified methods should be usable.\" if threshold_met else \"Below recommended minimum — expect high variance in per-subgroup estimates.\"}')\n\n    # EB vs MLE comparison\n    eb_rmse = df_summary[df_summary['method'] == 'hb_eb']['rmse'].mean()\n    mle_rmse = df_summary[df_summary['method'] == 'mle_laplace']['rmse'].mean()\n    if mle_rmse > 1e-10:\n        pct = (mle_rmse - eb_rmse) / mle_rmse * 100\n        lines.append(f'5. **EB vs MLE**: EB RMSE {pct:+.1f}% relative to MLE '\n                     f'({\"EB helps with shrinkage\" if pct > 0 else \"MLE competitive\"})')\n\n    lines.append('')\n    return '\\n'.join(lines)\n\n\ndef main():\n    parser = argparse.ArgumentParser()\n    parser.add_argument('--n-mc', type=int, default=100)\n    parser.add_argument('--dry-run', action='store_true')\n    parser.add_argument('--hb-method', choices=['eb', 'gibbs'], default='eb')\n    args = parser.parse_args()\n\n    n_mc = 5 if args.dry_run else args.n_mc\n    tag = ' (DRY RUN)' if args.dry_run else ''\n    print(f'exp-013 Boundary Condition{tag} | K={K} {REGIME_NAME} n_expert={N_EXPERT} n_mc={n_mc} hb={args.hb_method}')\n\n    all_rows = []\n    t0 = time.time()\n    for mc in range(n_mc):\n        rows = run_one(mc, hb_method=args.hb_method)\n        all_rows.extend(rows)\n        if (mc + 1) % max(1, n_mc // 10) == 0:\n            el = time.time() - t0\n            print(f'  [{mc + 1}/{n_mc}] {el:.1f}s elapsed')\n\n    print(f'  Done: {time.time() - t0:.1f}s ({len(all_rows)} rows)')\n\n    df = pd.DataFrame(all_rows)\n    df_summary = summarize(df)\n\n    os.makedirs('results', exist_ok=True)\n    df.to_csv('results/exp013_boundary_condition.csv', index=False)\n    df_summary.to_csv('results/exp013_boundary_summary.csv', index=False)\n    print(f'Saved: results/exp013_boundary_condition.csv ({len(df)} rows)')\n    print(f'Saved: results/exp013_boundary_summary.csv ({len(df_summary)} rows)')\n\n    analysis = write_analysis(df_summary)\n    with open('results/exp013_boundary_analysis.md', 'w') as f:\n        f.write(analysis)\n    print(f'Saved: results/exp013_boundary_analysis.md')\n\n    print('\\n' + analysis)\n\n\nif __name__ == '__main__':\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "f557b18a-c359-46aa-b90a-6b7b60b36a33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-21T07:26:57.504Z_

Running dry-run (5 MC runs) to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a31485f7-33d1-4b0a-b7f9-42c24f73800f",
  "isSidechain": false,
  "requestId": "req_011CbFKNx49SCoSiBLY9wpSz",
  "type": "assistant",
  "uuid": "a2a47f66-4b93-4ac5-b690-542b86f204cc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ubatvpWo363vAE3ZcUQb7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4474,
      "cache_read_input_tokens": 30854,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4474,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 30854,
          "cache_creation_input_tokens": 4474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4474
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

_source line 20 · 2026-05-21T07:26:57.927Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QyNjvuLemE2uk5T39LTgwk`</summary>

```json
{
  "command": ".venv/bin/python3 exp013_boundary_condition.py --dry-run 2>&1",
  "description": "Dry-run exp013 with 5 MC runs",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2a47f66-4b93-4ac5-b690-542b86f204cc",
  "isSidechain": false,
  "requestId": "req_011CbFKNx49SCoSiBLY9wpSz",
  "type": "assistant",
  "uuid": "1534a65c-2b82-4891-8a76-fa2688baeae6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ubatvpWo363vAE3ZcUQb7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4474,
      "cache_read_input_tokens": 30854,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4474,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 153,
          "cache_read_input_tokens": 30854,
          "cache_creation_input_tokens": 4474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4474
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

_source line 21 · 2026-05-21T07:27:01.762Z_

<details><summary>↩ Tool result · `toolu_01QyNjvuLemE2uk5T39LTgwk`</summary>

```text
exp-013 Boundary Condition (DRY RUN) | K=4 extreme n_expert=50 n_mc=5 hb=eb
  [1/5] 0.0s elapsed
  [2/5] 0.0s elapsed
  [3/5] 0.0s elapsed
  [4/5] 0.0s elapsed
  [5/5] 0.0s elapsed
  Done: 0.0s (160 rows)
Saved: results/exp013_boundary_condition.csv (160 rows)
Saved: results/exp013_boundary_summary.csv (32 rows)
Saved: results/exp013_boundary_analysis.md

# exp-013: Boundary Condition Analysis

**Config**: K=4, regime=extreme, n_expert=50, N=5000, misclass=[0.3, 0.2, 0.1, 0.03]

Each subgroup gets ~12 expert labels.

## Per-subgroup Results

| Subgroup (pi) | Method | |Bias|_z0 | RMSE_z0 | Cov_z0 | |Bias|_z1 | RMSE_z1 | Cov_z1 |
|---|---|---|---|---|---|---|---|
| A (0.30) | naive | 0.0756 | 0.1066 | 1.00 | 0.1902 | 0.1988 | 0.20 |
| A (0.30) | global_corrected | 0.0364 | 0.1165 | 1.00 | 0.1533 | 0.1792 | 1.00 |
| A (0.30) | mle_laplace | 0.0887 | 0.2043 | 1.00 | 0.0272 | 0.1599 | 1.00 |
| A (0.30) | hb_eb | 0.0566 | 0.1831 | 1.00 | 0.0552 | 0.1633 | 1.00 |
| B (0.20) | naive | 0.0224 | 0.0956 | 1.00 | 0.0436 | 0.0798 | 1.00 |
| B (0.20) | global_corrected | 0.0682 | 0.1646 | 0.80 | 0.0437 | 0.1121 | 1.00 |
| B (0.20) | mle_laplace | 0.2320 | 0.4069 | 0.80 | 0.1903 | 0.3022 | 0.60 |
| B (0.20) | hb_eb | 0.1654 | 0.3968 | 0.80 | 0.1227 | 0.2577 | 0.60 |
| C (0.10) | naive | 0.0419 | 0.0900 | 0.80 | 0.0837 | 0.1265 | 0.80 |
| C (0.10) | global_corrected | 0.0304 | 0.0927 | 1.00 | 0.0131 | 0.1034 | 1.00 |
| C (0.10) | mle_laplace | 0.0357 | 0.1093 | 1.00 | 0.0160 | 0.1063 | 1.00 |
| C (0.10) | hb_eb | 0.0030 | 0.0970 | 1.00 | 0.0141 | 0.1131 | 1.00 |
| D (0.03) | naive | 0.0263 | 0.0431 | 1.00 | 0.0071 | 0.0666 | 1.00 |
| D (0.03) | global_corrected | 0.1358 | 0.1431 | 1.00 | 0.1167 | 0.1440 | 0.80 |
| D (0.03) | mle_laplace | 0.1113 | 0.1230 | 1.00 | 0.0993 | 0.1133 | 1.00 |
| D (0.03) | hb_eb | 0.0715 | 0.0867 | 1.00 | 0.0563 | 0.0869 | 1.00 |

## Average Across Subgroups

| Method | |Bias|_z0 | RMSE_z0 | Cov_z0 | |Bias|_z1 | RMSE_z1 | Cov_z1 |
|---|---|---|---|---|---|---|
| naive | 0.0416 | 0.0838 | 0.95 | 0.0811 | 0.1179 | 0.75 |
| global_corrected | 0.0677 | 0.1292 | 0.95 | 0.0817 | 0.1347 | 0.95 |
| mle_laplace | 0.1169 | 0.2109 | 0.95 | 0.0832 | 0.1704 | 0.90 |
| hb_eb | 0.0742 | 0.1909 | 0.95 | 0.0621 | 0.1552 | 0.90 |

## RMSE Amplification (stratified vs global)

| Subgroup | Method | RMSE_z0 / Global | RMSE_z1 / Global |
|---|---|---|---|
| A (0.30) | mle_laplace | 1.58x | 1.19x |
| A (0.30) | hb_eb | 1.42x | 1.21x |
| B (0.20) | mle_laplace | 3.15x | 2.24x |
| B (0.20) | hb_eb | 3.07x | 1.91x |
| C (0.10) | mle_laplace | 0.85x | 0.79x |
| C (0.10) | hb_eb | 0.75x | 0.84x |
| D (0.03) | mle_laplace | 0.95x | 0.84x |
| D (0.03) | hb_eb | 0.67x | 0.64x |

## Key Findings

1. **Worst degradation**: subgroup B (mle_laplace, z0) with RMSE=0.4069
2. **Average stratified RMSE**: z0=0.2009, z1=0.1628 vs global z0=0.1292, z1=0.1347
3. **Amplification factor**: 1.55x (z0), 1.21x (z1)
4. **n_expert/K = 12.5** < 25 threshold NOT met. Below recommended minimum — expect high variance in per-subgroup estimates.
5. **EB vs MLE**: EB RMSE +9.2% relative to MLE (EB helps with shrinkage)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1534a65c-2b82-4891-8a76-fa2688baeae6",
  "isSidechain": false,
  "promptId": "99acad5a-cfb8-48f1-9a0e-e4eb1fe13a2c",
  "type": "user",
  "uuid": "e4f186f2-e434-4e7c-88df-f59d6c3d7f7d",
  "toolUseResult": {
    "stdout": "exp-013 Boundary Condition (DRY RUN) | K=4 extreme n_expert=50 n_mc=5 hb=eb\n  [1/5] 0.0s elapsed\n  [2/5] 0.0s elapsed\n  [3/5] 0.0s elapsed\n  [4/5] 0.0s elapsed\n  [5/5] 0.0s elapsed\n  Done: 0.0s (160 rows)\nSaved: results/exp013_boundary_condition.csv (160 rows)\nSaved: results/exp013_boundary_summary.csv (32 rows)\nSaved: results/exp013_boundary_analysis.md\n\n# exp-013: Boundary Condition Analysis\n\n**Config**: K=4, regime=extreme, n_expert=50, N=5000, misclass=[0.3, 0.2, 0.1, 0.03]\n\nEach subgroup gets ~12 expert labels.\n\n## Per-subgroup Results\n\n| Subgroup (pi) | Method | |Bias|_z0 | RMSE_z0 | Cov_z0 | |Bias|_z1 | RMSE_z1 | Cov_z1 |\n|---|---|---|---|---|---|---|---|\n| A (0.30) | naive | 0.0756 | 0.1066 | 1.00 | 0.1902 | 0.1988 | 0.20 |\n| A (0.30) | global_corrected | 0.0364 | 0.1165 | 1.00 | 0.1533 | 0.1792 | 1.00 |\n| A (0.30) | mle_laplace | 0.0887 | 0.2043 | 1.00 | 0.0272 | 0.1599 | 1.00 |\n| A (0.30) | hb_eb | 0.0566 | 0.1831 | 1.00 | 0.0552 | 0.1633 | 1.00 |\n| B (0.20) | naive | 0.0224 | 0.0956 | 1.00 | 0.0436 | 0.0798 | 1.00 |\n| B (0.20) | global_corrected | 0.0682 | 0.1646 | 0.80 | 0.0437 | 0.1121 | 1.00 |\n| B (0.20) | mle_laplace | 0.2320 | 0.4069 | 0.80 | 0.1903 | 0.3022 | 0.60 |\n| B (0.20) | hb_eb | 0.1654 | 0.3968 | 0.80 | 0.1227 | 0.2577 | 0.60 |\n| C (0.10) | naive | 0.0419 | 0.0900 | 0.80 | 0.0837 | 0.1265 | 0.80 |\n| C (0.10) | global_corrected | 0.0304 | 0.0927 | 1.00 | 0.0131 | 0.1034 | 1.00 |\n| C (0.10) | mle_laplace | 0.0357 | 0.1093 | 1.00 | 0.0160 | 0.1063 | 1.00 |\n| C (0.10) | hb_eb | 0.0030 | 0.0970 | 1.00 | 0.0141 | 0.1131 | 1.00 |\n| D (0.03) | naive | 0.0263 | 0.0431 | 1.00 | 0.0071 | 0.0666 | 1.00 |\n| D (0.03) | global_corrected | 0.1358 | 0.1431 | 1.00 | 0.1167 | 0.1440 | 0.80 |\n| D (0.03) | mle_laplace | 0.1113 | 0.1230 | 1.00 | 0.0993 | 0.1133 | 1.00 |\n| D (0.03) | hb_eb | 0.0715 | 0.0867 | 1.00 | 0.0563 | 0.0869 | 1.00 |\n\n## Average Across Subgroups\n\n| Method | |Bias|_z0 | RMSE_z0 | Cov_z0 | |Bias|_z1 | RMSE_z1 | Cov_z1 |\n|---|---|---|---|---|---|---|\n| naive | 0.0416 | 0.0838 | 0.95 | 0.0811 | 0.1179 | 0.75 |\n| global_corrected | 0.0677 | 0.1292 | 0.95 | 0.0817 | 0.1347 | 0.95 |\n| mle_laplace | 0.1169 | 0.2109 | 0.95 | 0.0832 | 0.1704 | 0.90 |\n| hb_eb | 0.0742 | 0.1909 | 0.95 | 0.0621 | 0.1552 | 0.90 |\n\n## RMSE Amplification (stratified vs global)\n\n| Subgroup | Method | RMSE_z0 / Global | RMSE_z1 / Global |\n|---|---|---|---|\n| A (0.30) | mle_laplace | 1.58x | 1.19x |\n| A (0.30) | hb_eb | 1.42x | 1.21x |\n| B (0.20) | mle_laplace | 3.15x | 2.24x |\n| B (0.20) | hb_eb | 3.07x | 1.91x |\n| C (0.10) | mle_laplace | 0.85x | 0.79x |\n| C (0.10) | hb_eb | 0.75x | 0.84x |\n| D (0.03) | mle_laplace | 0.95x | 0.84x |\n| D (0.03) | hb_eb | 0.67x | 0.64x |\n\n## Key Findings\n\n1. **Worst degradation**: subgroup B (mle_laplace, z0) with RMSE=0.4069\n2. **Average stratified RMSE**: z0=0.2009, z1=0.1628 vs global z0=0.1292, z1=0.1347\n3. **Amplification factor**: 1.55x (z0), 1.21x (z1)\n4. **n_expert/K = 12.5** < 25 threshold NOT met. Below recommended minimum — expect high variance in per-subgroup estimates.\n5. **EB vs MLE**: EB RMSE +9.2% relative to MLE (EB helps with shrinkage)",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "1534a65c-2b82-4891-8a76-fa2688baeae6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
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
  "leafUuid": "e4f186f2-e434-4e7c-88df-f59d6c3d7f7d",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Implement boundary condition experiment exp013",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7"
}
```

---

### Assistant

_source line 24 · 2026-05-21T07:27:04.350Z_

Dry-run passed. Running full 100 MC runs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4f186f2-e434-4e7c-88df-f59d6c3d7f7d",
  "isSidechain": false,
  "requestId": "req_011CbFKPVprSddVW3sFzvWXN",
  "type": "assistant",
  "uuid": "8f768a9a-1d5c-4bd0-8d5a-754355ca7658",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EN9sgrdVLdc5gAh8KteCyR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2012,
      "cache_read_input_tokens": 35328,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 35328,
          "cache_creation_input_tokens": 2012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2012
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

_source line 25 · 2026-05-21T07:27:05.281Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KV9Kgf4P9C47G143sFWPPp`</summary>

```json
{
  "command": ".venv/bin/python3 exp013_boundary_condition.py --n-mc 100 2>&1",
  "description": "Full 100 MC run for exp013",
  "timeout": 600000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f768a9a-1d5c-4bd0-8d5a-754355ca7658",
  "isSidechain": false,
  "requestId": "req_011CbFKPVprSddVW3sFzvWXN",
  "type": "assistant",
  "uuid": "99c66a3e-ebd0-412d-b4a7-4f71a5082752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EN9sgrdVLdc5gAh8KteCyR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2012,
      "cache_read_input_tokens": 35328,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2012,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 35328,
          "cache_creation_input_tokens": 2012,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2012
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

_source line 26 · 2026-05-21T07:27:11.829Z_

<details><summary>↩ Tool result · `toolu_01KV9Kgf4P9C47G143sFWPPp`</summary>

```text
exp-013 Boundary Condition | K=4 extreme n_expert=50 n_mc=100 hb=eb
  [10/100] 0.1s elapsed
  [20/100] 0.2s elapsed
  [30/100] 0.3s elapsed
  [40/100] 0.4s elapsed
  [50/100] 0.6s elapsed
  [60/100] 0.8s elapsed
  [70/100] 1.0s elapsed
  [80/100] 1.2s elapsed
  [90/100] 1.4s elapsed
  [100/100] 1.5s elapsed
  Done: 1.5s (3200 rows)
Saved: results/exp013_boundary_condition.csv (3200 rows)
Saved: results/exp013_boundary_summary.csv (32 rows)
Saved: results/exp013_boundary_analysis.md

# exp-013: Boundary Condition Analysis

**Config**: K=4, regime=extreme, n_expert=50, N=5000, misclass=[0.3, 0.2, 0.1, 0.03]

Each subgroup gets ~12 expert labels.

## Per-subgroup Results

| Subgroup (pi) | Method | |Bias|_z0 | RMSE_z0 | Cov_z0 | |Bias|_z1 | RMSE_z1 | Cov_z1 |
|---|---|---|---|---|---|---|---|
| A (0.30) | naive | 0.1212 | 0.1470 | 0.78 | 0.1284 | 0.1576 | 0.70 |
| A (0.30) | global_corrected | 0.0766 | 0.1344 | 0.92 | 0.0853 | 0.1482 | 0.89 |
| A (0.30) | mle_laplace | 0.0986 | 0.5210 | 0.95 | 0.0835 | 0.5265 | 0.95 |
| A (0.30) | hb_eb | 0.0383 | 0.6068 | 0.93 | 0.0215 | 0.6194 | 0.90 |
| B (0.20) | naive | 0.0771 | 0.1200 | 0.88 | 0.0759 | 0.1159 | 0.87 |
| B (0.20) | global_corrected | 0.0068 | 0.1263 | 0.94 | 0.0033 | 0.1198 | 0.93 |
| B (0.20) | mle_laplace | 0.1000 | 0.2999 | 0.92 | 0.1038 | 0.2897 | 0.92 |
| B (0.20) | hb_eb | 0.0669 | 0.2706 | 0.92 | 0.0740 | 0.2588 | 0.93 |
| C (0.10) | naive | 0.0312 | 0.0851 | 0.96 | 0.0505 | 0.1085 | 0.90 |
| C (0.10) | global_corrected | 0.0608 | 0.1291 | 0.94 | 0.0420 | 0.1344 | 0.91 |
| C (0.10) | mle_laplace | 0.0827 | 0.1536 | 0.91 | 0.0657 | 0.1635 | 0.88 |
| C (0.10) | hb_eb | 0.0529 | 0.1417 | 0.94 | 0.0392 | 0.1532 | 0.92 |
| D (0.03) | naive | 0.0005 | 0.0825 | 0.97 | 0.0146 | 0.0843 | 0.96 |
| D (0.03) | global_corrected | 0.1105 | 0.1624 | 0.87 | 0.0983 | 0.1605 | 0.85 |
| D (0.03) | mle_laplace | 0.0895 | 0.1444 | 0.88 | 0.0819 | 0.1514 | 0.92 |
| D (0.03) | hb_eb | 0.0612 | 0.1505 | 0.95 | 0.0599 | 0.1618 | 0.94 |

## Average Across Subgroups

| Method | |Bias|_z0 | RMSE_z0 | Cov_z0 | |Bias|_z1 | RMSE_z1 | Cov_z1 |
|---|---|---|---|---|---|---|
| naive | 0.0575 | 0.1087 | 0.90 | 0.0674 | 0.1166 | 0.86 |
| global_corrected | 0.0637 | 0.1381 | 0.92 | 0.0572 | 0.1407 | 0.90 |
| mle_laplace | 0.0927 | 0.2798 | 0.92 | 0.0837 | 0.2828 | 0.92 |
| hb_eb | 0.0548 | 0.2924 | 0.94 | 0.0486 | 0.2983 | 0.92 |

## RMSE Amplification (stratified vs global)

| Subgroup | Method | RMSE_z0 / Global | RMSE_z1 / Global |
|---|---|---|---|
| A (0.30) | mle_laplace | 3.77x | 3.74x |
| A (0.30) | hb_eb | 4.39x | 4.40x |
| B (0.20) | mle_laplace | 2.17x | 2.06x |
| B (0.20) | hb_eb | 1.96x | 1.84x |
| C (0.10) | mle_laplace | 1.11x | 1.16x |
| C (0.10) | hb_eb | 1.03x | 1.09x |
| D (0.03) | mle_laplace | 1.05x | 1.08x |
| D (0.03) | hb_eb | 1.09x | 1.15x |

## Key Findings

1. **Worst degradation**: subgroup A (hb_eb, z1) with RMSE=0.6194
2. **Average stratified RMSE**: z0=0.2861, z1=0.2905 vs global z0=0.1381, z1=0.1407
3. **Amplification factor**: 2.07x (z0), 2.06x (z1)
4. **n_expert/K = 12.5** < 25 threshold NOT met. Below recommended minimum — expect high variance in per-subgroup estimates.
5. **EB vs MLE**: EB RMSE -5.0% relative to MLE (MLE competitive)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99c66a3e-ebd0-412d-b4a7-4f71a5082752",
  "isSidechain": false,
  "promptId": "99acad5a-cfb8-48f1-9a0e-e4eb1fe13a2c",
  "type": "user",
  "uuid": "7e334f77-b380-4cd8-a035-5bb3b7327b8f",
  "toolUseResult": {
    "stdout": "exp-013 Boundary Condition | K=4 extreme n_expert=50 n_mc=100 hb=eb\n  [10/100] 0.1s elapsed\n  [20/100] 0.2s elapsed\n  [30/100] 0.3s elapsed\n  [40/100] 0.4s elapsed\n  [50/100] 0.6s elapsed\n  [60/100] 0.8s elapsed\n  [70/100] 1.0s elapsed\n  [80/100] 1.2s elapsed\n  [90/100] 1.4s elapsed\n  [100/100] 1.5s elapsed\n  Done: 1.5s (3200 rows)\nSaved: results/exp013_boundary_condition.csv (3200 rows)\nSaved: results/exp013_boundary_summary.csv (32 rows)\nSaved: results/exp013_boundary_analysis.md\n\n# exp-013: Boundary Condition Analysis\n\n**Config**: K=4, regime=extreme, n_expert=50, N=5000, misclass=[0.3, 0.2, 0.1, 0.03]\n\nEach subgroup gets ~12 expert labels.\n\n## Per-subgroup Results\n\n| Subgroup (pi) | Method | |Bias|_z0 | RMSE_z0 | Cov_z0 | |Bias|_z1 | RMSE_z1 | Cov_z1 |\n|---|---|---|---|---|---|---|---|\n| A (0.30) | naive | 0.1212 | 0.1470 | 0.78 | 0.1284 | 0.1576 | 0.70 |\n| A (0.30) | global_corrected | 0.0766 | 0.1344 | 0.92 | 0.0853 | 0.1482 | 0.89 |\n| A (0.30) | mle_laplace | 0.0986 | 0.5210 | 0.95 | 0.0835 | 0.5265 | 0.95 |\n| A (0.30) | hb_eb | 0.0383 | 0.6068 | 0.93 | 0.0215 | 0.6194 | 0.90 |\n| B (0.20) | naive | 0.0771 | 0.1200 | 0.88 | 0.0759 | 0.1159 | 0.87 |\n| B (0.20) | global_corrected | 0.0068 | 0.1263 | 0.94 | 0.0033 | 0.1198 | 0.93 |\n| B (0.20) | mle_laplace | 0.1000 | 0.2999 | 0.92 | 0.1038 | 0.2897 | 0.92 |\n| B (0.20) | hb_eb | 0.0669 | 0.2706 | 0.92 | 0.0740 | 0.2588 | 0.93 |\n| C (0.10) | naive | 0.0312 | 0.0851 | 0.96 | 0.0505 | 0.1085 | 0.90 |\n| C (0.10) | global_corrected | 0.0608 | 0.1291 | 0.94 | 0.0420 | 0.1344 | 0.91 |\n| C (0.10) | mle_laplace | 0.0827 | 0.1536 | 0.91 | 0.0657 | 0.1635 | 0.88 |\n| C (0.10) | hb_eb | 0.0529 | 0.1417 | 0.94 | 0.0392 | 0.1532 | 0.92 |\n| D (0.03) | naive | 0.0005 | 0.0825 | 0.97 | 0.0146 | 0.0843 | 0.96 |\n| D (0.03) | global_corrected | 0.1105 | 0.1624 | 0.87 | 0.0983 | 0.1605 | 0.85 |\n| D (0.03) | mle_laplace | 0.0895 | 0.1444 | 0.88 | 0.0819 | 0.1514 | 0.92 |\n| D (0.03) | hb_eb | 0.0612 | 0.1505 | 0.95 | 0.0599 | 0.1618 | 0.94 |\n\n## Average Across Subgroups\n\n| Method | |Bias|_z0 | RMSE_z0 | Cov_z0 | |Bias|_z1 | RMSE_z1 | Cov_z1 |\n|---|---|---|---|---|---|---|\n| naive | 0.0575 | 0.1087 | 0.90 | 0.0674 | 0.1166 | 0.86 |\n| global_corrected | 0.0637 | 0.1381 | 0.92 | 0.0572 | 0.1407 | 0.90 |\n| mle_laplace | 0.0927 | 0.2798 | 0.92 | 0.0837 | 0.2828 | 0.92 |\n| hb_eb | 0.0548 | 0.2924 | 0.94 | 0.0486 | 0.2983 | 0.92 |\n\n## RMSE Amplification (stratified vs global)\n\n| Subgroup | Method | RMSE_z0 / Global | RMSE_z1 / Global |\n|---|---|---|---|\n| A (0.30) | mle_laplace | 3.77x | 3.74x |\n| A (0.30) | hb_eb | 4.39x | 4.40x |\n| B (0.20) | mle_laplace | 2.17x | 2.06x |\n| B (0.20) | hb_eb | 1.96x | 1.84x |\n| C (0.10) | mle_laplace | 1.11x | 1.16x |\n| C (0.10) | hb_eb | 1.03x | 1.09x |\n| D (0.03) | mle_laplace | 1.05x | 1.08x |\n| D (0.03) | hb_eb | 1.09x | 1.15x |\n\n## Key Findings\n\n1. **Worst degradation**: subgroup A (hb_eb, z1) with RMSE=0.6194\n2. **Average stratified RMSE**: z0=0.2861, z1=0.2905 vs global z0=0.1381, z1=0.1407\n3. **Amplification factor**: 2.07x (z0), 2.06x (z1)\n4. **n_expert/K = 12.5** < 25 threshold NOT met. Below recommended minimum — expect high variance in per-subgroup estimates.\n5. **EB vs MLE**: EB RMSE -5.0% relative to MLE (MLE competitive)",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "99c66a3e-ebd0-412d-b4a7-4f71a5082752",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-21T07:27:22.294Z_

Done. All three outputs saved:

- **`results/exp013_boundary_condition.csv`** — 3200 rows (100 runs × 4 subgroups × 4 methods × 2 z-levels)
- **`results/exp013_boundary_summary.csv`** — 32 rows aggregated
- **`results/exp013_boundary_analysis.md`** — full analysis

Key findings from 100 MC runs:

1. **Worst degradation is subgroup A (pi=0.30), not D (pi=0.03)** — RMSE reaches 0.62 for EB. The highest-misclassification subgroup suffers most because the CM estimation noise amplifies through a nearly-singular mixing matrix inversion, not because it has fewer labels.

2. **Stratified RMSE is ~2x global** on average (2.07x for z0, 2.06x for z1). Subgroup A hits 3.7–4.4x amplification.

3. **n_expert/K = 12.5 < 25 threshold** — confirmed. Per-subgroup CM estimates are too noisy; global correction dominates all stratified methods.

4. **EB vs MLE**: EB is ~5% worse than MLE here — the shrinkage target (pooled mean) is itself noisy with only 50 total labels, so partial pooling doesn't help. Both are far worse than global.

5. **Naive beats all correction methods on average RMSE** for this boundary case — the correction signal is swamped by estimation noise in the mixing matrix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e334f77-b380-4cd8-a035-5bb3b7327b8f",
  "isSidechain": false,
  "requestId": "req_011CbFKQEwBdHUVcdzNE2YrQ",
  "type": "assistant",
  "uuid": "76c2cd97-737b-473f-b3ee-5e3d3913da29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016awUJc6jDAkSieFCQHvrKb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2066,
      "cache_read_input_tokens": 37340,
      "output_tokens": 379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 379,
          "cache_read_input_tokens": 37340,
          "cache_creation_input_tokens": 2066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2066
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

_source line 28_

```json
{
  "type": "last-prompt",
  "leafUuid": "76c2cd97-737b-473f-b3ee-5e3d3913da29",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Implement boundary condition experiment exp013",
  "sessionId": "2a935248-651b-4881-b714-ac12895495f7"
}
```

---
