# Research conversation: <project_context> # 项目: causal_annot_error_attrib ## 运行环境 - 服务器名: home-1x5090 - SSH 账户: sonny（调用 ssh_execute / submit_tr

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-1/a1e14e23-41f7-42b4-ac49-b035326a4af4.jsonl`
- **Structured JSON:** [`d6f3f6a651fa8bd48cb6.json`](../../sessions/d6/d6f3f6a651fa8bd48cb6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-23T14:34:45.337Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T14:34:45.337Z",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "content": "&lt;project_context>\n# 项目: causal_annot_error_attrib\n\n## 运行环境\n- 服务器名: home-1x5090\n- SSH 账户: sonny（调用 ssh_execute / submit_training_job 时传入 account=\"sonny\"）\n- SSH 连接命令: ssh implicit5638.xyfu.me  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /home/sonny/causal_annot_error_attrib\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：Mini End-to-End Demo 实验\n\n**目标**：展示框架端到端可用性——从 C 估计到 ASV 诊断到 Algorithm 1 路由到校正改善。\n\n**项目路径**：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/`\n\n### 具体步骤\n\n写 Python 脚本 `artifacts/e2e_demo.py`，执行以下流程：\n\n1. **选 2 个拓扑**：confounding（FWL 使校正无效）和 exposure（PPI++ 有效）\n2. **对每个拓扑**：\n   - 生成合成数据 N=10,000，K=3，true β 已知\n   - 用已知 C（diagonal-dominant，diag=0.7）生成 A* = misclassify(A, C)\n   - 从 held-out subset (20% gold labels, 即 2,000 个) 估计 Ĉ\n   - 计算 ASV（magnitude, significance, sign-flip）\n   - Algorithm 1 路由：confounding → \"no correction (FWL)\"；exposure → \"PPI++\"\n   - 应用校正方法（PPI++ for exposure; show that naive/MLA achieve 0% for confounding）\n   - 对比 naive bias vs corrected bias vs true\n3. **重复 100 次** 取 mean ± std\n\n### 代码参考\n\n- **DGP 和工具函数**：参考 `artifacts/compute_ppi_empirical.py` 的 DGP 结构（softmax_rows, sample_cat, make_p_A, misclassify 等函数）\n- **校正方法**：使用 `annot_sensitivity.correction` 中的 `correct_ppi`, `correct_naive_plugin`, `correct_mcsimex`, `correct_mla`\n- **ASV 计算**：使用 `annot_sensitivity.asv` 中的函数\n- **工具函数**：`annot_sensitivity.utils` 中的 `misclassify`, `make_dummies`, `ols`, `ols_with_se`\n- **bias 计算**：`annot_sensitivity.bias` 中的 plim 函数\n\n先 `Read` 这些模块了解 API，特别是 `annot_sensitivity/correction.py` 中 `correct_ppi` 的签名和参数。\n\n### DGP 设计\n\n**Confounding DAG**: Y = τ·X + γ₁·1[A=1] + γ₂·1[A=2] + ε\n- X = α₀ + α₁·1[A=1] + α₂·1[A=2] + ε_x\n- τ = 0.5 (target), γ = [0, 0.8, -0.4], α = [0, 0.6, -0.3]\n- 回归: OLS of Y on (X, D*), 关注 X 的系数 τ̂\n\n**Exposure DAG**: Y = β₁·1[A=1] + β₂·1[A=2] + ε\n- β = [0, 1.0, -0.5]\n- 回归: OLS of Y on D*, 关注 β̂₁, β̂₂\n\n**Confusion matrix C₀**: diagonal-dominant with diag=0.7, off-diagonal uniform\n```python\nC0 = np.array([[0.7, 0.15, 0.15],\n               [0.15, 0.7, 0.15],\n               [0.15, 0.15, 0.7]])\n```\n\n### Ĉ 估计\n从 held-out gold subset（20% of N）估计 confusion matrix：\n```python\ndef estimate_C(A_true_gold, A_star_gold, K):\n    C_hat = np.zeros((K, K))\n    for k in range(K):\n        mask = (A_true_gold == k)\n        if mask.sum() > 0:\n            for j in range(K):\n                C_hat[j, k] = (A_star_gold[mask] == j).sum() / mask.sum()\n    return C_hat\n```\n\n### ASV 计算\n对每个拓扑：\n- 用 Ĉ 作为 C₀ 参数化 C(δ) = (1-δ)I + δĈ\n- 扫描 δ 从 0 到 1，找到 magnitude ASV（bias 超过 10% threshold）\n- 找到 sign-flip ASV（如适用）\n\n### 产出\n\n1. **脚本** `artifacts/e2e_demo.py`\n2. **JSON 结果** `artifacts/e2e_demo_results.json`，包含：\n   - per-topology: naive_bias (mean±std), corrected_bias (mean±std), improvement_pct, asv_magnitude, asv_signflip, routed_method\n3. **LaTeX table** `artifacts/e2e_demo_table.tex`，列：\n   Topology | Naive Bias (%) | ASV δ*_mag | Routed Method | Corrected Bias (%) | Improvement (%)\n\n### 验证\n- 脚本写完后运行: `cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib && python artifacts/e2e_demo.py`\n- 确认结果合理：confounding 的 naive/corrected 差异应该≈0%（FWL invariance）；exposure 的 PPI++ 应显著降低 bias\n- 如果 annot_sensitivity 模块中的函数 API 不匹配，检查实际签名并适配\n\n### 注意\n- 文件顶部加文件注释（说明目的、输入输出）\n- 代码要可复现（固定 seed=42）\n- 如果 PPI++ 需要 gold labels 参数，用 20% gold ratio\n- 100 次重复可能需要几分钟，可以先用 10 次验证正确性再跑 100 次"
}
````

---

### Runtime record

_source line 2 · 2026-05-23T14:34:45.340Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T14:34:45.340Z",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4"
}
```

---

## Round 1

38 recorded events

### User

_source line 3 · 2026-05-23T14:34:45.366Z_

&lt;project_context>
# 项目: causal_annot_error_attrib

## 运行环境
- 服务器名: home-1x5090
- SSH 账户: sonny（调用 ssh_execute / submit_training_job 时传入 account="sonny"）
- SSH 连接命令: ssh implicit5638.xyfu.me  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /home/sonny/causal_annot_error_attrib


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：Mini End-to-End Demo 实验

**目标**：展示框架端到端可用性——从 C 估计到 ASV 诊断到 Algorithm 1 路由到校正改善。

**项目路径**：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/`

### 具体步骤

写 Python 脚本 `artifacts/e2e_demo.py`，执行以下流程：

1. **选 2 个拓扑**：confounding（FWL 使校正无效）和 exposure（PPI++ 有效）
2. **对每个拓扑**：
   - 生成合成数据 N=10,000，K=3，true β 已知
   - 用已知 C（diagonal-dominant，diag=0.7）生成 A* = misclassify(A, C)
   - 从 held-out subset (20% gold labels, 即 2,000 个) 估计 Ĉ
   - 计算 ASV（magnitude, significance, sign-flip）
   - Algorithm 1 路由：confounding → "no correction (FWL)"；exposure → "PPI++"
   - 应用校正方法（PPI++ for exposure; show that naive/MLA achieve 0% for confounding）
   - 对比 naive bias vs corrected bias vs true
3. **重复 100 次** 取 mean ± std

### 代码参考

- **DGP 和工具函数**：参考 `artifacts/compute_ppi_empirical.py` 的 DGP 结构（softmax_rows, sample_cat, make_p_A, misclassify 等函数）
- **校正方法**：使用 `annot_sensitivity.correction` 中的 `correct_ppi`, `correct_naive_plugin`, `correct_mcsimex`, `correct_mla`
- **ASV 计算**：使用 `annot_sensitivity.asv` 中的函数
- **工具函数**：`annot_sensitivity.utils` 中的 `misclassify`, `make_dummies`, `ols`, `ols_with_se`
- **bias 计算**：`annot_sensitivity.bias` 中的 plim 函数

先 `Read` 这些模块了解 API，特别是 `annot_sensitivity/correction.py` 中 `correct_ppi` 的签名和参数。

### DGP 设计

**Confounding DAG**: Y = τ·X + γ₁·1[A=1] + γ₂·1[A=2] + ε
- X = α₀ + α₁·1[A=1] + α₂·1[A=2] + ε_x
- τ = 0.5 (target), γ = [0, 0.8, -0.4], α = [0, 0.6, -0.3]
- 回归: OLS of Y on (X, D*), 关注 X 的系数 τ̂

**Exposure DAG**: Y = β₁·1[A=1] + β₂·1[A=2] + ε
- β = [0, 1.0, -0.5]
- 回归: OLS of Y on D*, 关注 β̂₁, β̂₂

**Confusion matrix C₀**: diagonal-dominant with diag=0.7, off-diagonal uniform
```python
C0 = np.array([[0.7, 0.15, 0.15],
               [0.15, 0.7, 0.15],
               [0.15, 0.15, 0.7]])
```

### Ĉ 估计
从 held-out gold subset（20% of N）估计 confusion matrix：
```python
def estimate_C(A_true_gold, A_star_gold, K):
    C_hat = np.zeros((K, K))
    for k in range(K):
        mask = (A_true_gold == k)
        if mask.sum() > 0:
            for j in range(K):
                C_hat[j, k] = (A_star_gold[mask] == j).sum() / mask.sum()
    return C_hat
```

### ASV 计算
对每个拓扑：
- 用 Ĉ 作为 C₀ 参数化 C(δ) = (1-δ)I + δĈ
- 扫描 δ 从 0 到 1，找到 magnitude ASV（bias 超过 10% threshold）
- 找到 sign-flip ASV（如适用）

### 产出

1. **脚本** `artifacts/e2e_demo.py`
2. **JSON 结果** `artifacts/e2e_demo_results.json`，包含：
   - per-topology: naive_bias (mean±std), corrected_bias (mean±std), improvement_pct, asv_magnitude, asv_signflip, routed_method
3. **LaTeX table** `artifacts/e2e_demo_table.tex`，列：
   Topology | Naive Bias (%) | ASV δ*_mag | Routed Method | Corrected Bias (%) | Improvement (%)

### 验证
- 脚本写完后运行: `cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib && python artifacts/e2e_demo.py`
- 确认结果合理：confounding 的 naive/corrected 差异应该≈0%（FWL invariance）；exposure 的 PPI++ 应显著降低 bias
- 如果 annot_sensitivity 模块中的函数 API 不匹配，检查实际签名并适配

### 注意
- 文件顶部加文件注释（说明目的、输入输出）
- 代码要可复现（固定 seed=42）
- 如果 PPI++ 需要 gold labels 参数，用 20% gold ratio
- 100 次重复可能需要几分钟，可以先用 10 次验证正确性再跑 100 次

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "931f36b2-6e79-486e-89c9-9074426aeee2",
  "type": "user",
  "uuid": "81fe3eea-379a-45e4-93ef-3acec379afd9",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-23T14:34:45.366Z_

```json
{
  "parentUuid": "81fe3eea-379a-45e4-93ef-3acec379afd9",
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
  "uuid": "4ac61055-a0c9-4eb2-b2c9-9d57322d67f9",
  "timestamp": "2026-05-23T14:34:45.366Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-23T14:34:45.366Z_

```json
{
  "parentUuid": "4ac61055-a0c9-4eb2-b2c9-9d57322d67f9",
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
  "uuid": "ebbe7ec8-60d8-4dd7-9723-e5633886404a",
  "timestamp": "2026-05-23T14:34:45.366Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-23T14:34:45.366Z_

```json
{
  "parentUuid": "ebbe7ec8-60d8-4dd7-9723-e5633886404a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "38381e6c-989f-452f-8bdb-29541df02da0",
  "timestamp": "2026-05-23T14:34:45.366Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Mini end-to-end demo for causal annotation error",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4"
}
```

---

### Assistant

_source line 8 · 2026-05-23T14:34:48.262Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the relevant source modules to understand the API before writing the script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38381e6c-989f-452f-8bdb-29541df02da0",
  "isSidechain": false,
  "requestId": "req_011CbKfd6ugh6TqU775rzHEZ",
  "type": "assistant",
  "uuid": "13430d1a-7192-474a-8b7e-3e23f1ded87f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETzFqCtao5eUhQhYobuxwJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14264,
      "cache_read_input_tokens": 11841,
      "output_tokens": 383,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 383,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14264
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

_source line 9 · 2026-05-23T14:34:48.884Z_

I'll read the relevant source modules to understand the APIs first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13430d1a-7192-474a-8b7e-3e23f1ded87f",
  "isSidechain": false,
  "requestId": "req_011CbKfd6ugh6TqU775rzHEZ",
  "type": "assistant",
  "uuid": "8ca52535-d5be-48c5-ad7a-b34da0f92686",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETzFqCtao5eUhQhYobuxwJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14264,
      "cache_read_input_tokens": 11841,
      "output_tokens": 383,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 383,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14264
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

_source line 10 · 2026-05-23T14:34:55.635Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01H85xunvvATkySyCqM98VUT`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore annot_sensitivity modules",
  "prompt": "I need to understand the API of the `annot_sensitivity` package in `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/`. \n\nRead the following files fully:\n1. `annot_sensitivity/correction.py` — especially `correct_ppi`, `correct_naive_plugin`, `correct_mcsimex`, `correct_mla` signatures and docstrings\n2. `annot_sensitivity/asv.py` — all functions, especially how ASV is computed\n3. `annot_sensitivity/utils.py` — `misclassify`, `make_dummies`, `ols`, `ols_with_se`\n4. `annot_sensitivity/bias.py` — plim functions\n\nFor each function, report its full signature (all parameters with defaults) and a one-line description. Also note any imports or dependencies between them.\n\nAlso check `annot_sensitivity/__init__.py` for any re-exports.\n\nBe very thorough — read each file completely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ca52535-d5be-48c5-ad7a-b34da0f92686",
  "isSidechain": false,
  "requestId": "req_011CbKfd6ugh6TqU775rzHEZ",
  "type": "assistant",
  "uuid": "3abbbfcb-c91a-4dc0-9c21-48d4f17f186c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ETzFqCtao5eUhQhYobuxwJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14264,
      "cache_read_input_tokens": 11841,
      "output_tokens": 383,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14264,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 383,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 14264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14264
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

_source line 11 · 2026-05-23T14:35:26.183Z_

<details><summary>↩ Tool result · `toolu_01H85xunvvATkySyCqM98VUT`</summary>

````text
Perfect! I have read all the key files. Let me compile a comprehensive API reference for the `annot_sensitivity` package.

## API Reference: `annot_sensitivity` Package

### File: `annot_sensitivity/__init__.py`
**Re-exports (Public API):**
- `compute_bias` (from `.bias`)
- `compute_asv` (from `.asv`)
- `recommend_correction` (from `.correction`)
- `correct_naive_plugin`, `correct_dsl`, `correct_ppi`, `correct_mcsimex`, `correct_mla` (from `.correction`)
- `clear_cache` (from `.bias`)
- `METHODS` (from `.correction`)
- `validate_confusion_matrix`, `random_confusion_matrix`, `interpolate_confusion`, `predefined_matrices`, `delta_range` (from `.confusion`)
- `generate_data`, `TOPOLOGIES`, `DEFAULT_PARAMS`, `GEN_FUNCS` (from `.dgp`)
- `ols`, `ols_with_se`, `make_dummies`, `softmax_sample`, `misclassify` (from `.utils`)

---

### File: `annot_sensitivity/correction.py`

**Module Constants:**
- `METHODS = ["naive_plugin", "dsl", "ppi", "mcsimex", "mla"]`

**Functions:**

1. **`correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1)`**
   - Correct using C^{-1} applied per-observation to dummy indicators (reference category dropped)
   - Returns: `(tau_hat, se, success)` tuple of floats and bool

2. **`correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1)`**
   - EM-based joint estimation of regression parameters and confusion matrix C
   - Returns: `(tau_hat, se, success)` tuple

3. **`correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1, rng=None)`**
   - PPI++ with bootstrap lambda tuning using gold-standard labels
   - Returns: `(tau_hat, se, success)` tuple

4. **`correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=None)`**
   - MC-SIMEX: add extra misclassification at levels [0.5, 1.0, 1.5, 2.0], extrapolate quadratically to lambda=-1
   - Returns: `(tau_hat, se, success)` tuple

5. **`correct_mla(X_other, Y, Astar, C, tau_idx=1)`**
   - Matrix-based label adjustment: D_corrected = D_full @ C^{-1}, drop reference category
   - Returns: `(tau_hat, se, success)` tuple

6. **`recommend_correction(topology, C, has_gold=False, gold_fraction=0.1)`**
   - Recommend the best correction method based on topology and data availability
   - Returns: dict with keys `{"recommended", "ranking", "notes"}`

**Key Module Notes:**
- `_EM_MAX_ITER = 100`, `_EM_TOL = 1e-6` (DSL parameters)
- `_SIMEX_LAMBDAS = [0.5, 1.0, 1.5, 2.0]`, `_SIMEX_B = 50` (MC-SIMEX parameters)
- All correction functions follow pattern: (X_other, Y, Astar, ...) → (float, float, bool)
- FWL theorem note: `naive_plugin` and `mla` only correct dummy coefficients, NOT treatment coefficient when treatment is separate
- Imports: `numpy`, `ols`, `ols_with_se`, `make_dummies`, `make_full_dummies`, `misclassify` from utils

---

### File: `annot_sensitivity/asv.py`

**Functions:**

1. **`_compute_bias_curve(topology, C0, stats, K, tau_true, n_grid=1500)`**
   - Compute absolute bias along C(delta) interpolation path
   - Returns: `(deltas, bias_abs, tau_curve)` arrays

2. **`_compute_envelope(bias_abs)`**
   - Running maximum of absolute bias (for threshold crossing detection)
   - Returns: `(n_grid,)` envelope array

3. **`_find_threshold_crossing(envelope, deltas, tau_curve, tau_true, threshold_type, threshold_value)`**
   - Find delta where bias envelope crosses threshold
   - `threshold_type` in `{"magnitude", "significance", "sign_flip"}`
   - Returns: `float` delta or `None`

4. **`compute_asv(topology, C0, params=None, threshold_type="magnitude", threshold_value=0.1, n_grid=1500)`**
   - Compute Annotation Sensitivity Value: minimum delta at which bias threshold is crossed
   - Returns: dict with keys `{"asv", "bias_curve", "envelope", "deltas", "tau_true"}`

**Key Module Notes:**
- ASV measures robustness of causal inference to annotation error
- Uses interpolation path: C(delta) = (1-delta)*I + delta*C0
- Imports: `_precompute`, `_get_tau` from bias; `validate_confusion_matrix`, `interpolate_confusion`, `delta_range` from confusion; DEFAULT_PARAMS, TOPOLOGIES from dgp

---

### File: `annot_sensitivity/utils.py`

**Functions:**

1. **`softmax_sample(logits, rng)`**
   - Sample categorical variable from row-wise softmax probabilities
   - Args: `logits` (N, K), `rng` numpy Generator
   - Returns: `(N,)` integer array in {0, ..., K-1}

2. **`misclassify(A, C, rng)`**
   - Apply misclassification: A*_i ~ Cat(C[:, A_i]) using confusion matrix C
   - Args: `A` (N,) true labels, `C` (K, K) column-stochastic, `rng` Generator
   - Returns: `(N,)` misclassified labels

3. **`make_dummies(A, K=None)`**
   - Create K-1 dummy variables with reference category 0
   - Args: `A` (N,) labels in {0, ..., K-1}, `K` inferred from A.max()+1 if None
   - Returns: `(N, K-1)` dummy matrix

4. **`make_full_dummies(A, K=None)`**
   - Create full K one-hot encoding (all K categories)
   - Args: `A` (N,) labels, `K` optional
   - Returns: `(N, K)` one-hot matrix

5. **`ols(X, Y)`**
   - OLS point estimate via least-squares (numpy.linalg.lstsq)
   - Args: `X` (N, p) design matrix, `Y` (N,) response
   - Returns: `(p,)` coefficient vector

6. **`ols_with_se(X, Y)`**
   - OLS point estimate with homoskedastic standard errors
   - Args: `X` (N, p), `Y` (N,)
   - Returns: `(beta, se)` tuple of (p,) arrays

**Key Module Notes:**
- All sampling uses numpy random Generator (RNG) interface
- No imports beyond numpy

---

### File: `annot_sensitivity/bias.py`

**Module Constants:**
- `_N_PRECOMP = 2_000_000` (sample size for precomputation)
- `_precomp_cache = {}` (global cache for sufficient statistics)

**Functions:**

1. **`_params_key(params)`**
   - Convert parameter dict to hashable tuple key for caching
   - Returns: `tuple`

2. **`_precompute(topology, params, K, seed=999)`**
   - Precompute sufficient statistics from large-sample DGP simulations
   - Returns: dict with keys `E_Y`, `E_DA`, `E_DA_Y`, and optionally `E_T`, `E_T2`, `E_TY`, `E_DA_T`, `RF`, `FS`

3. **`_plim_with_T(C, stats, K)`**
   - OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}
   - Returns: `(1+K,)` coefficient vector

4. **`_plim_no_T(C, stats, K)`**
   - OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}
   - Returns: `(K,)` coefficient vector

5. **`_plim_iv(C, stats, K)`**
   - Wald estimator plim: RF / (C @ FS)[1]
   - Returns: `float` or `np.nan`

6. **`_get_tau(topology, C, stats, K)`**
   - Extract target coefficient from plim vector
   - For IV: Wald estimator; for others: coefficient at index 1
   - Returns: `float`

7. **`compute_bias(topology, C, params=None)`**
   - Compute annotation-error bias for a given topology and confusion matrix C
   - Returns: dict with keys `{"tau_true", "tau_biased", "bias", "bias_pct", "topology"}` (all floats)

8. **`clear_cache()`**
   - Clear the precomputed statistics cache
   - Returns: `None`

**Key Module Notes:**
- Plim calculations avoid Monte Carlo by using precomputed sufficient statistics from N=2M samples
- Condition number warnings logged if EZZ is poorly conditioned (cond > 1e12)
- Imports: `warnings`, `numpy`, DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES from dgp; `validate_confusion_matrix` from confusion

---

### Cross-Function Dependencies

```
correction.py
  ↓ uses
  ├─ utils: ols, ols_with_se, make_dummies, make_full_dummies, misclassify
  └─ (returns tau_hat, se, success tuples)

asv.py
  ↓ uses
  ├─ bias: _precompute, _get_tau
  ├─ confusion: validate_confusion_matrix, interpolate_confusion, delta_range
  ├─ dgp: DEFAULT_PARAMS, TOPOLOGIES
  └─ (returns asv dict with bias_curve, envelope, deltas, tau_true)

bias.py
  ↓ uses
  ├─ dgp: DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES
  ├─ confusion: validate_confusion_matrix
  └─ (returns tau_true, tau_biased, bias, bias_pct as floats)

utils.py
  ↓ standalone
  └─ (no dependencies on other annot_sensitivity modules)
```

---

### Summary: Function Signatures at a Glance

**Correction Methods** (all return `(tau_hat: float, se: float, success: bool)`)
- `correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1)`
- `correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1)`
- `correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1, rng=None)`
- `correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=None)`
- `correct_mla(X_other, Y, Astar, C, tau_idx=1)`

**Main API Functions**
- `compute_bias(topology, C, params=None)` → dict
- `compute_asv(topology, C0, params=None, threshold_type="magnitude", threshold_value=0.1, n_grid=1500)` → dict
- `recommend_correction(topology, C, has_gold=False, gold_fraction=0.1)` → dict

**Utilities**
- `ols(X, Y)` → (p,) coefficients
- `ols_with_se(X, Y)` → ((p,), (p,)) coefficients and standard errors
- `make_dummies(A, K=None)` → (N, K-1) dummies
- `make_full_dummies(A, K=None)` → (N, K) one-hot
- `misclassify(A, C, rng)` → (N,) misclassified labels
- `softmax_sample(logits, rng)` → (N,) sampled categories
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "3abbbfcb-c91a-4dc0-9c21-48d4f17f186c",
  "isSidechain": false,
  "promptId": "931f36b2-6e79-486e-89c9-9074426aeee2",
  "type": "user",
  "uuid": "55579b71-992a-46f4-9fa3-92a1becf82b4",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to understand the API of the `annot_sensitivity` package in `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/`. \n\nRead the following files fully:\n1. `annot_sensitivity/correction.py` — especially `correct_ppi`, `correct_naive_plugin`, `correct_mcsimex`, `correct_mla` signatures and docstrings\n2. `annot_sensitivity/asv.py` — all functions, especially how ASV is computed\n3. `annot_sensitivity/utils.py` — `misclassify`, `make_dummies`, `ols`, `ols_with_se`\n4. `annot_sensitivity/bias.py` — plim functions\n\nFor each function, report its full signature (all parameters with defaults) and a one-line description. Also note any imports or dependencies between them.\n\nAlso check `annot_sensitivity/__init__.py` for any re-exports.\n\nBe very thorough — read each file completely.",
    "agentId": "a57cdec08a0b4a571",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I have read all the key files. Let me compile a comprehensive API reference for the `annot_sensitivity` package.\n\n## API Reference: `annot_sensitivity` Package\n\n### File: `annot_sensitivity/__init__.py`\n**Re-exports (Public API):**\n- `compute_bias` (from `.bias`)\n- `compute_asv` (from `.asv`)\n- `recommend_correction` (from `.correction`)\n- `correct_naive_plugin`, `correct_dsl`, `correct_ppi`, `correct_mcsimex`, `correct_mla` (from `.correction`)\n- `clear_cache` (from `.bias`)\n- `METHODS` (from `.correction`)\n- `validate_confusion_matrix`, `random_confusion_matrix`, `interpolate_confusion`, `predefined_matrices`, `delta_range` (from `.confusion`)\n- `generate_data`, `TOPOLOGIES`, `DEFAULT_PARAMS`, `GEN_FUNCS` (from `.dgp`)\n- `ols`, `ols_with_se`, `make_dummies`, `softmax_sample`, `misclassify` (from `.utils`)\n\n---\n\n### File: `annot_sensitivity/correction.py`\n\n**Module Constants:**\n- `METHODS = [\"naive_plugin\", \"dsl\", \"ppi\", \"mcsimex\", \"mla\"]`\n\n**Functions:**\n\n1. **`correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1)`**\n   - Correct using C^{-1} applied per-observation to dummy indicators (reference category dropped)\n   - Returns: `(tau_hat, se, success)` tuple of floats and bool\n\n2. **`correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1)`**\n   - EM-based joint estimation of regression parameters and confusion matrix C\n   - Returns: `(tau_hat, se, success)` tuple\n\n3. **`correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1, rng=None)`**\n   - PPI++ with bootstrap lambda tuning using gold-standard labels\n   - Returns: `(tau_hat, se, success)` tuple\n\n4. **`correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=None)`**\n   - MC-SIMEX: add extra misclassification at levels [0.5, 1.0, 1.5, 2.0], extrapolate quadratically to lambda=-1\n   - Returns: `(tau_hat, se, success)` tuple\n\n5. **`correct_mla(X_other, Y, Astar, C, tau_idx=1)`**\n   - Matrix-based label adjustment: D_corrected = D_full @ C^{-1}, drop reference category\n   - Returns: `(tau_hat, se, success)` tuple\n\n6. **`recommend_correction(topology, C, has_gold=False, gold_fraction=0.1)`**\n   - Recommend the best correction method based on topology and data availability\n   - Returns: dict with keys `{\"recommended\", \"ranking\", \"notes\"}`\n\n**Key Module Notes:**\n- `_EM_MAX_ITER = 100`, `_EM_TOL = 1e-6` (DSL parameters)\n- `_SIMEX_LAMBDAS = [0.5, 1.0, 1.5, 2.0]`, `_SIMEX_B = 50` (MC-SIMEX parameters)\n- All correction functions follow pattern: (X_other, Y, Astar, ...) → (float, float, bool)\n- FWL theorem note: `naive_plugin` and `mla` only correct dummy coefficients, NOT treatment coefficient when treatment is separate\n- Imports: `numpy`, `ols`, `ols_with_se`, `make_dummies`, `make_full_dummies`, `misclassify` from utils\n\n---\n\n### File: `annot_sensitivity/asv.py`\n\n**Functions:**\n\n1. **`_compute_bias_curve(topology, C0, stats, K, tau_true, n_grid=1500)`**\n   - Compute absolute bias along C(delta) interpolation path\n   - Returns: `(deltas, bias_abs, tau_curve)` arrays\n\n2. **`_compute_envelope(bias_abs)`**\n   - Running maximum of absolute bias (for threshold crossing detection)\n   - Returns: `(n_grid,)` envelope array\n\n3. **`_find_threshold_crossing(envelope, deltas, tau_curve, tau_true, threshold_type, threshold_value)`**\n   - Find delta where bias envelope crosses threshold\n   - `threshold_type` in `{\"magnitude\", \"significance\", \"sign_flip\"}`\n   - Returns: `float` delta or `None`\n\n4. **`compute_asv(topology, C0, params=None, threshold_type=\"magnitude\", threshold_value=0.1, n_grid=1500)`**\n   - Compute Annotation Sensitivity Value: minimum delta at which bias threshold is crossed\n   - Returns: dict with keys `{\"asv\", \"bias_curve\", \"envelope\", \"deltas\", \"tau_true\"}`\n\n**Key Module Notes:**\n- ASV measures robustness of causal inference to annotation error\n- Uses interpolation path: C(delta) = (1-delta)*I + delta*C0\n- Imports: `_precompute`, `_get_tau` from bias; `validate_confusion_matrix`, `interpolate_confusion`, `delta_range` from confusion; DEFAULT_PARAMS, TOPOLOGIES from dgp\n\n---\n\n### File: `annot_sensitivity/utils.py`\n\n**Functions:**\n\n1. **`softmax_sample(logits, rng)`**\n   - Sample categorical variable from row-wise softmax probabilities\n   - Args: `logits` (N, K), `rng` numpy Generator\n   - Returns: `(N,)` integer array in {0, ..., K-1}\n\n2. **`misclassify(A, C, rng)`**\n   - Apply misclassification: A*_i ~ Cat(C[:, A_i]) using confusion matrix C\n   - Args: `A` (N,) true labels, `C` (K, K) column-stochastic, `rng` Generator\n   - Returns: `(N,)` misclassified labels\n\n3. **`make_dummies(A, K=None)`**\n   - Create K-1 dummy variables with reference category 0\n   - Args: `A` (N,) labels in {0, ..., K-1}, `K` inferred from A.max()+1 if None\n   - Returns: `(N, K-1)` dummy matrix\n\n4. **`make_full_dummies(A, K=None)`**\n   - Create full K one-hot encoding (all K categories)\n   - Args: `A` (N,) labels, `K` optional\n   - Returns: `(N, K)` one-hot matrix\n\n5. **`ols(X, Y)`**\n   - OLS point estimate via least-squares (numpy.linalg.lstsq)\n   - Args: `X` (N, p) design matrix, `Y` (N,) response\n   - Returns: `(p,)` coefficient vector\n\n6. **`ols_with_se(X, Y)`**\n   - OLS point estimate with homoskedastic standard errors\n   - Args: `X` (N, p), `Y` (N,)\n   - Returns: `(beta, se)` tuple of (p,) arrays\n\n**Key Module Notes:**\n- All sampling uses numpy random Generator (RNG) interface\n- No imports beyond numpy\n\n---\n\n### File: `annot_sensitivity/bias.py`\n\n**Module Constants:**\n- `_N_PRECOMP = 2_000_000` (sample size for precomputation)\n- `_precomp_cache = {}` (global cache for sufficient statistics)\n\n**Functions:**\n\n1. **`_params_key(params)`**\n   - Convert parameter dict to hashable tuple key for caching\n   - Returns: `tuple`\n\n2. **`_precompute(topology, params, K, seed=999)`**\n   - Precompute sufficient statistics from large-sample DGP simulations\n   - Returns: dict with keys `E_Y`, `E_DA`, `E_DA_Y`, and optionally `E_T`, `E_T2`, `E_TY`, `E_DA_T`, `RF`, `FS`\n\n3. **`_plim_with_T(C, stats, K)`**\n   - OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}\n   - Returns: `(1+K,)` coefficient vector\n\n4. **`_plim_no_T(C, stats, K)`**\n   - OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}\n   - Returns: `(K,)` coefficient vector\n\n5. **`_plim_iv(C, stats, K)`**\n   - Wald estimator plim: RF / (C @ FS)[1]\n   - Returns: `float` or `np.nan`\n\n6. **`_get_tau(topology, C, stats, K)`**\n   - Extract target coefficient from plim vector\n   - For IV: Wald estimator; for others: coefficient at index 1\n   - Returns: `float`\n\n7. **`compute_bias(topology, C, params=None)`**\n   - Compute annotation-error bias for a given topology and confusion matrix C\n   - Returns: dict with keys `{\"tau_true\", \"tau_biased\", \"bias\", \"bias_pct\", \"topology\"}` (all floats)\n\n8. **`clear_cache()`**\n   - Clear the precomputed statistics cache\n   - Returns: `None`\n\n**Key Module Notes:**\n- Plim calculations avoid Monte Carlo by using precomputed sufficient statistics from N=2M samples\n- Condition number warnings logged if EZZ is poorly conditioned (cond > 1e12)\n- Imports: `warnings`, `numpy`, DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES from dgp; `validate_confusion_matrix` from confusion\n\n---\n\n### Cross-Function Dependencies\n\n```\ncorrection.py\n  ↓ uses\n  ├─ utils: ols, ols_with_se, make_dummies, make_full_dummies, misclassify\n  └─ (returns tau_hat, se, success tuples)\n\nasv.py\n  ↓ uses\n  ├─ bias: _precompute, _get_tau\n  ├─ confusion: validate_confusion_matrix, interpolate_confusion, delta_range\n  ├─ dgp: DEFAULT_PARAMS, TOPOLOGIES\n  └─ (returns asv dict with bias_curve, envelope, deltas, tau_true)\n\nbias.py\n  ↓ uses\n  ├─ dgp: DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES\n  ├─ confusion: validate_confusion_matrix\n  └─ (returns tau_true, tau_biased, bias, bias_pct as floats)\n\nutils.py\n  ↓ standalone\n  └─ (no dependencies on other annot_sensitivity modules)\n```\n\n---\n\n### Summary: Function Signatures at a Glance\n\n**Correction Methods** (all return `(tau_hat: float, se: float, success: bool)`)\n- `correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1)`\n- `correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1)`\n- `correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1, rng=None)`\n- `correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=None)`\n- `correct_mla(X_other, Y, Astar, C, tau_idx=1)`\n\n**Main API Functions**\n- `compute_bias(topology, C, params=None)` → dict\n- `compute_asv(topology, C0, params=None, threshold_type=\"magnitude\", threshold_value=0.1, n_grid=1500)` → dict\n- `recommend_correction(topology, C, has_gold=False, gold_fraction=0.1)` → dict\n\n**Utilities**\n- `ols(X, Y)` → (p,) coefficients\n- `ols_with_se(X, Y)` → ((p,), (p,)) coefficients and standard errors\n- `make_dummies(A, K=None)` → (N, K-1) dummies\n- `make_full_dummies(A, K=None)` → (N, K) one-hot\n- `misclassify(A, C, rng)` → (N,) misclassified labels\n- `softmax_sample(logits, rng)` → (N,) sampled categories"
      }
    ],
    "totalDurationMs": 30544,
    "totalTokens": 34355,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 13113,
      "cache_read_input_tokens": 17997,
      "output_tokens": 3238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13113
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3238,
          "cache_read_input_tokens": 17997,
          "cache_creation_input_tokens": 13113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13113,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 5,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "3abbbfcb-c91a-4dc0-9c21-48d4f17f186c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
````

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "leafUuid": "55579b71-992a-46f4-9fa3-92a1becf82b4",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Mini end-to-end demo for causal annotation error",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4"
}
```

---

### Assistant

_source line 14 · 2026-05-23T14:35:35.926Z_

Now let me also read the existing `compute_ppi_empirical.py` for DGP reference and the `dgp.py` module.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55579b71-992a-46f4-9fa3-92a1becf82b4",
  "isSidechain": false,
  "requestId": "req_011CbKfg7UzmXxEYXiJRtj8R",
  "type": "assistant",
  "uuid": "bba749a5-0f3f-4e6d-ab2c-7c47547490a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rerXLcjU94zeauoAzfSkR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3631,
      "cache_read_input_tokens": 26105,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 26105,
          "cache_creation_input_tokens": 3631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3631
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

_source line 15 · 2026-05-23T14:35:38.002Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G4oE4tcoA2DE6Dca2USsRb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_ppi_empirical.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bba749a5-0f3f-4e6d-ab2c-7c47547490a5",
  "isSidechain": false,
  "requestId": "req_011CbKfg7UzmXxEYXiJRtj8R",
  "type": "assistant",
  "uuid": "9061248f-6cce-4556-8d75-c24978f88fb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rerXLcjU94zeauoAzfSkR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3631,
      "cache_read_input_tokens": 26105,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 26105,
          "cache_creation_input_tokens": 3631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3631
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

_source line 16 · 2026-05-23T14:35:38.016Z_

<details><summary>↩ Tool result · `toolu_01G4oE4tcoA2DE6Dca2USsRb`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Empirical Correction Validation — HumAID K=10
4	
5	Loads 8 valid HumAID confusion matrices from asv_empirical_results.json,
6	generates synthetic MC data using plan_006's K=10 DGP for each of 7 topologies,
7	runs all 5 correction methods (PPI++, naive plug-in, DSL, MC-SIMEX, MLA),
8	and reports empirical bias reduction per topology × method.
9	
10	Input:  artifacts/plan006/asv_empirical_results.json
11	Output: artifacts/ppi_empirical_validation.json
12	
13	Dependencies: numpy, annot_sensitivity (local package)
14	"""
15	
16	import sys
17	import os
18	import json
19	import time
20	import numpy as np
21	
22	PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
23	sys.path.insert(0, PROJECT_ROOT)
24	
25	from annot_sensitivity.correction import (
26	    correct_ppi, correct_naive_plugin, correct_dsl, correct_mcsimex, correct_mla
27	)
28	from annot_sensitivity.utils import misclassify, make_dummies, ols, ols_with_se
29	
30	# ── Plan 006 DGP Infrastructure (K-general) ────────────────────────
31	
32	_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
33	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
34	_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
35	_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
36	_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]
37	_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
38	_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2, 0.15, -0.1, 0.05]
39	
40	
41	def softmax_rows(logits):
42	    e = np.exp(logits - logits.max(axis=1, keepdims=True))
43	    return e / e.sum(axis=1, keepdims=True)
44	
45	
46	def sample_cat(probs, rng):
47	    cum = np.cumsum(probs, axis=1)
48	    u = rng.uniform(size=probs.shape[0])[:, None]
49	    return (u >= cum[:, :-1]).sum(axis=1).astype(int)
50	
51	
52	def make_p_A(K):
53	    if K == 2:
54	        return np.array([0.55, 0.45])
55	    elif K == 3:
56	        return np.array([0.40, 0.35, 0.25])
57	    else:
58	        raw = np.array([1.0 / (i + 1) for i in range(K)])
59	        return raw / raw.sum()
60	
61	
62	def make_dgp_params(K):
63	    p_A = make_p_A(K)
64	    params = {
65	        'confounding': {
66	            'p_A': p_A,
67	            'alpha': np.array(_ALPHA_POOL[:K - 1]),
68	            'beta_A': np.array(_BETA_A_POOL[:K - 1]),
69	            'beta_T': 2.0,
70	            'sigma_T': 1.0,
71	        },
72	        'mediation': {
73	            'tau': 0.5,
74	            'gamma': np.array(_GAMMA_POOL[:K]),
75	            'delta': np.array(_DELTA_POOL[:K]),
76	            'beta': np.array(_BETA_POOL[:K]),
77	        },
78	        'collider': {
79	            'tau': 1.0,
80	            'g': np.zeros(K),
81	            'dT': np.array(_DT_POOL[:K]),
82	            'dY': np.array(_DY_POOL[:K]),
83	        },
84	        'exposure': {
85	            'beta': np.array(_BETA_POOL[:K]),
86	            'p_A': p_A,
87	        },
88	    }
89	    if K == 3:
90	        params['mbias'] = {
91	            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,
92	            'g': np.zeros(3),
93	            'a_U1': np.array([0.0, 0.8, -0.5]),
94	            'a_U2': np.array([0.0, 0.6, 0.9]),
95	        }
96	        params['iv'] = {
97	            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),
98	            'g': np.zeros(3),
99	            'dZ': np.array([0.0, 1.0, -0.5]),
100	            'dU': np.array([0.0, 0.8, 0.6]),
101	        }
102	        params['frontdoor'] = {
103	            'alpha_U': 1.0, 'lambda_U': 1.0,
104	            'gamma': np.array([0.0, 0.5, -0.3]),
105	            'delta_fd': np.array([0.0, 1.0, -0.8]),
106	            'beta': np.array([0.0, 1.0, -0.5]),
107	        }
108	    else:
109	        params['mbias'] = {
110	            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,
111	            'g': np.zeros(K),
112	            'a_U1': np.array([0.0] + [_ALPHA_POOL[i] * 0.6 for i in range(K - 1)]),
113	            'a_U2': np.array([0.0] + [_BETA_A_POOL[i] * 0.8 for i in range(K - 1)]),
114	        }
115	        iv_beta = np.array(_BETA_POOL[:K]) * 0.5
116	        iv_beta[0] = 0.0
117	        params['iv'] = {
118	            'lam': 1.0, 'beta': iv_beta,
119	            'g': np.zeros(K),
120	            'dZ': np.array([0.0] + [_ALPHA_POOL[i] * 0.7 for i in range(K - 1)]),
121	            'dU': np.array([0.0] + [_BETA_A_POOL[i] * 0.6 for i in range(K - 1)]),
122	        }
123	        fd_delta = np.array(_DELTA_POOL[:K])
124	        fd_delta[0] = 0.0
125	        params['frontdoor'] = {
126	            'alpha_U': 1.0, 'lambda_U': 1.0,
127	            'gamma': np.array(_GAMMA_POOL[:K]),
128	            'delta_fd': fd_delta,
129	            'beta': np.array(_BETA_POOL[:K]),
130	        }
131	    return params
132	
133	
134	# ── DGP Generators ──────────────────────────────────────────────────
135	
136	def gen_confounding(K, N, p, rng):
137	    A = rng.choice(K, size=N, p=p['p_A'])
138	    D = np.zeros((N, K - 1))
139	    for j in range(K - 1):
140	        D[:, j] = (A == j + 1).astype(float)
141	    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)
142	    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)
143	    return T, Y, A
144	
145	
146	def gen_mediation(K, N, p, rng):
147	    T = rng.binomial(1, 0.5, N).astype(float)
148	    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]
149	    probs = softmax_rows(logits)
150	    A = sample_cat(probs, rng)
151	    D = np.zeros((N, K - 1))
152	    for j in range(K - 1):
153	        D[:, j] = (A == j + 1).astype(float)
154	    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)
155	    return T, Y, A
156	
157	
158	def gen_collider(K, N, p, rng):
159	    T = rng.normal(0, 1, N)
160	    Y = p['tau'] * T + rng.normal(0, 1, N)
161	    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]
162	              + p['dY'][None, :] * Y[:, None])
163	    probs = softmax_rows(logits)
164	    A = sample_cat(probs, rng)
165	    return T, Y, A
166	
167	
168	def gen_exposure(K, N, p, rng):
169	    A = rng.choice(K, size=N, p=p['p_A'])
170	    D = np.zeros((N, K - 1))
171	    for j in range(K - 1):
172	        D[:, j] = (A == j + 1).astype(float)
173	    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)
174	    return None, Y, A
175	
176	
177	def gen_mbias(K, N, p, rng):
178	    U1 = rng.normal(0, 1, N)
179	    U2 = rng.normal(0, 1, N)
180	    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)
181	    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)
182	    logits = (p['g'][None, :] + p['a_U1'][None, :] * U1[:, None]
183	              + p['a_U2'][None, :] * U2[:, None])
184	    probs = softmax_rows(logits)
185	    A = sample_cat(probs, rng)
186	    return T, Y, A
187	
188	
189	def gen_iv(K, N, p, rng):
190	    Z = rng.binomial(1, 0.5, N).astype(float)
191	    U = rng.normal(0, 1, N)
192	    logits = (p['g'][None, :] + p['dZ'][None, :] * Z[:, None]
193	              + p['dU'][None, :] * U[:, None])
194	    probs = softmax_rows(logits)
195	    A = sample_cat(probs, rng)
196	    D = np.zeros((N, K - 1))
197	    for j in range(K - 1):
198	        D[:, j] = (A == j + 1).astype(float)
199	    Y = D @ p['beta'][1:] + p['lam'] * U + rng.normal(0, 1, N)
200	    return Z, Y, A
201	
202	
203	def gen_frontdoor(K, N, p, rng):
204	    U = rng.normal(0, 1, N)
205	    T = p['alpha_U'] * U + rng.normal(0, 1, N)
206	    logits = p['gamma'][None, :] + p['delta_fd'][None, :] * T[:, None]
207	    probs = softmax_rows(logits)
208	    M = sample_cat(probs, rng)
209	    D = np.zeros((N, K - 1))
210	    for j in range(K - 1):
211	        D[:, j] = (M == j + 1).astype(float)
212	    Y = D @ p['beta'][1:] + p['lambda_U'] * U + rng.normal(0, 1, N)
213	    return T, Y, M
214	
215	
216	GEN_FNS = {
217	    'confounding': gen_confounding, 'mediation': gen_mediation,
218	    'collider': gen_collider, 'exposure': gen_exposure,
219	    'mbias': gen_mbias, 'iv': gen_iv, 'frontdoor': gen_frontdoor,
220	}
221	
222	HAS_TREATMENT = {'confounding', 'mediation', 'collider', 'mbias', 'frontdoor'}
223	
224	
225	# ── Wald Estimator ──────────────────────────────────────────────────
226	
227	def wald_est(Z, Y, A_or_Astar, k=1):
228	    z1 = Z == 1; z0 = Z == 0
229	    n1, n0 = float(z1.sum()), float(z0.sum())
230	    if n1 < 2 or n0 < 2:
231	        return np.nan
232	    RF = Y[z1].mean() - Y[z0].mean()
233	    FS = (A_or_Astar[z1] == k).astype(float).mean() - \
234	         (A_or_Astar[z0] == k).astype(float).mean()
235	    if abs(FS) < 1e-8:
236	        return np.nan
237	    return RF / FS
238	
239	
240	def ppi_wald(Z, Y, A, Astar, gold_mask, k=1, rng=None, n_boot=50):
241	    """PPI++ for Wald estimator (IV topology)."""
242	    if rng is None:
243	        rng = np.random.default_rng()
244	    gold_idx = np.where(gold_mask)[0]
245	    n_gold = len(gold_idx)
246	
247	    tau_all_star = wald_est(Z, Y, Astar, k)
248	    tau_gold_true = wald_est(Z[gold_mask], Y[gold_mask], A[gold_mask], k)
249	    tau_gold_star = wald_est(Z[gold_mask], Y[gold_mask], Astar[gold_mask], k)
250	
251	    if np.isnan(tau_gold_true) or np.isnan(tau_all_star):
252	        return np.nan, False
253	
254	    tau_true_boot = np.zeros(n_boot)
255	    tau_rect_boot = np.zeros(n_boot)
256	    for b in range(n_boot):
257	        idx = rng.choice(gold_idx, size=n_gold, replace=True)
258	        bt = wald_est(Z[idx], Y[idx], A[idx], k)
259	        bs = wald_est(Z[idx], Y[idx], Astar[idx], k)
260	        tau_true_boot[b] = bt
261	        tau_rect_boot[b] = bs - bt
262	
263	    valid = np.isfinite(tau_true_boot) & np.isfinite(tau_rect_boot)
264	    if valid.sum() > 5:
265	        var_r = np.var(tau_rect_boot[valid])
266	        cov_tr = np.cov(tau_true_boot[valid], tau_rect_boot[valid])[0, 1]
267	        lam = np.clip(-cov_tr / var_r, 0, 1) if var_r > 1e-12 else 1.0
268	    else:
269	        lam = 1.0
270	
271	    tau_ppi = tau_gold_true + lam * (tau_all_star - tau_gold_star)
272	    return float(tau_ppi), True
273	
274	
275	# ── True Parameter Computation ──────────────────────────────────────
276	
277	def compute_tau_true(K, topology, params, N_large=500_000, seed=99):
278	    """Compute true tau by running estimator on very large uncontaminated sample."""
279	    rng = np.random.default_rng(seed)
280	    first_var, Y, A = GEN_FNS[topology](K, N_large, params[topology], rng)
281	
282	    if topology == 'iv':
283	        return wald_est(first_var, Y, A, k=1)
284	    elif topology == 'exposure':
285	        D = make_dummies(A, K)
286	        X = np.column_stack([np.ones(N_large), D])
287	        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
288	        return float(beta[1])
289	    else:
290	        T = first_var
291	        D = make_dummies(A, K)
292	        X = np.column_stack([np.ones(N_large), T, D])
293	        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
294	        return float(beta[1])
295	
296	
297	# ── MC-SIMEX for IV (custom) ────────────────────────────────────────
298	
299	def mcsimex_wald(Z, Y, Astar, C, k=1, rng=None, n_B=50,
300	                 lambdas_extra=(0.5, 1.0, 1.5, 2.0)):
301	    """MC-SIMEX for IV Wald estimator."""
302	    if rng is None:
303	        rng = np.random.default_rng()
304	    K = C.shape[0]
305	    try:
306	        eigvals, eigvecs = np.linalg.eig(C)
307	        eigvecs_inv = np.linalg.inv(eigvecs)
308	    except np.linalg.LinAlgError:
309	        return np.nan, False
310	
311	    lambdas = np.array([0.0] + list(lambdas_extra))
312	    tau_lam = np.zeros(len(lambdas))
313	
314	    for li, lam_val in enumerate(lambdas):
315	        if lam_val == 0.0:
316	            tau_lam[li] = wald_est(Z, Y, Astar, k)
317	        else:
318	            C_lam_raw = np.real((eigvecs * (eigvals ** lam_val)) @ eigvecs_inv)
319	            C_lam = np.clip(C_lam_raw, 0, None)
320	            cs = C_lam.sum(axis=0)
321	            cs[cs == 0] = 1.0
322	            C_lam /= cs
323	
324	            tau_b = np.zeros(n_B)
325	            for b in range(n_B):
326	                A_extra = misclassify(Astar, C_lam, rng)
327	                tau_b[b] = wald_est(Z, Y, A_extra, k)
328	            ok = np.isfinite(tau_b)
329	            if ok.sum() < n_B // 2:
330	                return np.nan, False
331	            tau_lam[li] = tau_b[ok].mean()
332	
333	    try:
334	        coeffs = np.polyfit(lambdas, tau_lam, 2)
335	        return float(np.polyval(coeffs, -1.0)), True
336	    except Exception:
337	        return np.nan, False
338	
339	
340	# ── Main ────────────────────────────────────────────────────────────
341	
342	N_SAMPLES = 10_000
343	N_REPS = 30
344	GOLD_FRACTION = 0.10
345	SEED = 42
346	TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
347	              'mbias', 'iv', 'frontdoor']
348	METHODS = ['ppi', 'naive_plugin', 'dsl', 'mcsimex', 'mla']
349	
350	JSON_PATH = os.path.join(PROJECT_ROOT, 'artifacts', 'plan006',
351	                         'asv_empirical_results.json')
352	
353	
354	def load_valid_humaid_configs():
355	    with open(JSON_PATH) as f:
356	        data = json.load(f)
357	
358	    zero_configs = {(e['model'], e['prompt'])
359	                    for e in data['f1_vs_bias'] if e['macro_f1'] == 0}
360	
361	    cms = {}
362	    for key, mat in data['confusion_matrices'].items():
363	        parts = key.split('_')
364	        if parts[0] != 'humaid':
365	            continue
366	        model = parts[1]
367	        prompt = '_'.join(parts[2:])
368	        if (model, prompt) in zero_configs:
369	            continue
370	        cms[key] = np.array(mat)
371	    return cms
372	
373	
374	def run_single_rep(K, topology, params, C, tau_true, rng, gold_frac):
375	    """Run one MC replication: generate data, misclassify, run corrections."""
376	    first_var, Y, A = GEN_FNS[topology](K, N_SAMPLES, params[topology], rng)
377	    Astar = misclassify(A, C, rng)
378	
379	    N = len(Y)
380	    n_gold = max(int(N * gold_frac), 50)
381	    gold_idx = rng.choice(N, size=n_gold, replace=False)
382	    gold_mask = np.zeros(N, dtype=bool)
383	    gold_mask[gold_idx] = True
384	
385	    results = {}
386	
387	    if topology == 'iv':
388	        Z = first_var
389	        tau_naive = wald_est(Z, Y, Astar, k=1)
390	        results['naive'] = float(tau_naive) if np.isfinite(tau_naive) else None
391	
392	        tau_ppi, ok = ppi_wald(Z, Y, A, Astar, gold_mask, k=1, rng=rng)
393	        results['ppi'] = float(tau_ppi) if ok and np.isfinite(tau_ppi) else None
394	
395	        tau_sim, ok = mcsimex_wald(Z, Y, Astar, C, k=1, rng=rng)
396	        results['mcsimex'] = float(tau_sim) if ok and np.isfinite(tau_sim) else None
397	
398	        results['naive_plugin'] = None
399	        results['dsl'] = None
400	        results['mla'] = None
401	
402	    elif topology == 'exposure':
403	        X_other = np.ones((N, 1))
404	        D_star = make_dummies(Astar, K)
405	        X_full = np.column_stack([X_other, D_star])
406	        try:
407	            beta_naive = np.linalg.lstsq(X_full, Y, rcond=None)[0]
408	            tau_naive = float(beta_naive[1])
409	        except Exception:
410	            tau_naive = np.nan
411	        results['naive'] = float(tau_naive) if np.isfinite(tau_naive) else None
412	
413	        for method in METHODS:
414	            if method == 'ppi':
415	                tau, se, ok = correct_ppi(X_other, Y, Astar, A, gold_mask,
416	                                          tau_idx=1, rng=rng)
417	            elif method == 'naive_plugin':
418	                tau, se, ok = correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1)
419	            elif method == 'dsl':
420	                tau, se, ok = correct_dsl(X_other, Y, Astar, A, gold_mask, tau_idx=1)
421	            elif method == 'mcsimex':
422	                tau, se, ok = correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=rng)
423	            elif method == 'mla':
424	                tau, se, ok = correct_mla(X_other, Y, Astar, C, tau_idx=1)
425	            else:
426	                continue
427	            results[method] = float(tau) if ok and np.isfinite(tau) else None
428	
429	    else:
430	        T = first_var
431	        X_other = np.column_stack([np.ones(N), T])
432	        D_star = make_dummies(Astar, K)
433	        X_full = np.column_stack([X_other, D_star])
434	        try:
435	            beta_naive = np.linalg.lstsq(X_full, Y, rcond=None)[0]
436	            tau_naive = float(beta_naive[1])
437	        except Exception:
438	            tau_naive = np.nan
439	        results['naive'] = float(tau_naive) if np.isfinite(tau_naive) else None
440	
441	        for method in METHODS:
442	            if method == 'ppi':
443	                tau, se, ok = correct_ppi(X_other, Y, Astar, A, gold_mask,
444	                                          tau_idx=1, rng=rng)
445	            elif method == 'naive_plugin':
446	                tau, se, ok = correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1)
447	            elif method == 'dsl':
448	                tau, se, ok = correct_dsl(X_other, Y, Astar, A, gold_mask, tau_idx=1)
449	            elif method == 'mcsimex':
450	                tau, se, ok = correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=rng)
451	            elif method == 'mla':
452	                tau, se, ok = correct_mla(X_other, Y, Astar, C, tau_idx=1)
453	            else:
454	                continue
455	            results[method] = float(tau) if ok and np.isfinite(tau) else None
456	
457	    results['tau_true'] = tau_true
458	    return results
459	
460	
461	def main():
462	    t_start = time.time()
463	    K = 10
464	    print("=" * 70)
465	    print("Empirical Correction Validation — HumAID K=10")
466	    print("=" * 70)
467	    print(f"N={N_SAMPLES}, N_REPS={N_REPS}, gold_fraction={GOLD_FRACTION}")
468	
469	    configs = load_valid_humaid_configs()
470	    print(f"Loaded {len(configs)} valid HumAID confusion matrices")
471	
472	    params = make_dgp_params(K)
473	    rng_master = np.random.default_rng(SEED)
474	
475	    print("\nComputing tau_true for each topology (N=500k)...")
476	    tau_true = {}
477	    for topo in TOPOLOGIES:
478	        tau_true[topo] = compute_tau_true(K, topo, params)
479	        print(f"  {topo}: tau_true = {tau_true[topo]:.6f}")
480	
481	    all_results = {}
482	    per_topo_method = {topo: {m: [] for m in METHODS}
483	                       for topo in TOPOLOGIES}
484	
485	    for ci, (config_name, C) in enumerate(configs.items()):
486	        print(f"\n[{ci+1}/{len(configs)}] {config_name}")
487	        config_results = {}
488	
489	        for topo in TOPOLOGIES:
490	            topo_reps = []
491	            for rep in range(N_REPS):
492	                seed_rep = rng_master.integers(0, 2**31)
493	                rng_rep = np.random.default_rng(seed_rep)
494	                res = run_single_rep(K, topo, params, C, tau_true[topo],
495	                                     rng_rep, GOLD_FRACTION)
496	                topo_reps.append(res)
497	
498	            naive_biases = []
499	            method_biases = {m: [] for m in METHODS}
500	            for res in topo_reps:
501	                tt = res['tau_true']
502	                if res['naive'] is not None:
503	                    naive_biases.append(res['naive'] - tt)
504	                for m in METHODS:
505	                    if res.get(m) is not None:
506	                        method_biases[m].append(res[m] - tt)
507	
508	            avg_naive_bias = np.mean(np.abs(naive_biases)) if naive_biases else None
509	            topo_summary = {
510	                'tau_true': tau_true[topo],
511	                'n_reps': N_REPS,
512	                'naive_mean_abs_bias': float(avg_naive_bias) if avg_naive_bias else None,
513	                'methods': {},
514	            }
515	
516	            for m in METHODS:
517	                biases = method_biases[m]
518	                if biases:
519	                    avg_abs = float(np.mean(np.abs(biases)))
520	                    mean_bias = float(np.mean(biases))
521	                    if avg_naive_bias and avg_naive_bias > 1e-8:
522	                        reduction = 1.0 - avg_abs / avg_naive_bias
523	                    else:
524	                        reduction = None
525	                    topo_summary['methods'][m] = {
526	                        'mean_abs_bias': avg_abs,
527	                        'mean_bias': mean_bias,
528	                        'bias_reduction': float(reduction) if reduction is not None else None,
529	                        'n_valid': len(biases),
530	                    }
531	                    per_topo_method[topo][m].append(
532	                        float(reduction) if reduction is not None else None
533	                    )
534	                else:
535	                    topo_summary['methods'][m] = {
536	                        'mean_abs_bias': None,
537	                        'mean_bias': None,
538	                        'bias_reduction': None,
539	                        'n_valid': 0,
540	                    }
541	
542	            config_results[topo] = topo_summary
543	            ppi_info = topo_summary['methods'].get('ppi', {})
544	            ppi_red = ppi_info.get('bias_reduction')
545	            ppi_str = f"{100*ppi_red:.1f}%" if ppi_red is not None else "N/A"
546	            print(f"  {topo:12s}: naive_bias={avg_naive_bias:.4f}" if avg_naive_bias else
547	                  f"  {topo:12s}: naive_bias=N/A", end="")
548	            print(f"  PPI++={ppi_str}")
549	
550	        all_results[config_name] = config_results
551	
552	    grand_summary = {}
553	    print("\n" + "=" * 70)
554	    print("GRAND SUMMARY: Mean bias reduction across 8 configs")
555	    print("=" * 70)
556	    print(f"\n{'Topology':14s}", end="")
557	    for m in METHODS:
558	        print(f"  {m:14s}", end="")
559	    print()
560	    print("-" * (14 + 16 * len(METHODS)))
561	
562	    for topo in TOPOLOGIES:
563	        grand_summary[topo] = {}
564	        print(f"{topo:14s}", end="")
565	        for m in METHODS:
566	            vals = [v for v in per_topo_method[topo][m] if v is not None]
567	            if vals:
568	                mean_red = float(np.mean(vals))
569	                grand_summary[topo][m] = {
570	                    'mean_reduction': mean_red,
571	                    'std_reduction': float(np.std(vals)),
572	                    'n_configs': len(vals),
573	                }
574	                print(f"  {100*mean_red:+12.1f}%", end="")
575	            else:
576	                grand_summary[topo][m] = None
577	                print(f"  {'N/A':>13s}", end="")
578	        print()
579	
580	    overall_ppi = []
581	    for topo in TOPOLOGIES:
582	        gs = grand_summary[topo].get('ppi')
583	        if gs:
584	            overall_ppi.append(gs['mean_reduction'])
585	    if overall_ppi:
586	        print(f"\nGrand mean PPI++ bias reduction: {100*np.mean(overall_ppi):.1f}%")
587	
588	    output = {
589	        'meta': {
590	            'scope': 'HumAID K=10, 8 valid configs',
591	            'n_samples': N_SAMPLES,
592	            'n_reps': N_REPS,
593	            'gold_fraction': GOLD_FRACTION,
594	            'seed': SEED,
595	            'topologies': TOPOLOGIES,
596	            'methods': METHODS,
597	            'n_configs': len(configs),
598	            'configs': list(configs.keys()),
599	        },
600	        'tau_true': {t: float(tau_true[t]) for t in TOPOLOGIES},
601	        'per_config': all_results,
602	        'grand_summary': grand_summary,
603	    }
604	
605	    out_path = os.path.join(PROJECT_ROOT, 'artifacts',
606	                            'ppi_empirical_validation.json')
607	    with open(out_path, 'w') as f:
608	        json.dump(output, f, indent=2)
609	
610	    elapsed = time.time() - t_start
611	    print(f"\nResults saved to: {out_path}")
612	    print(f"Total runtime: {elapsed:.1f}s")
613	
614	
615	if __name__ == '__main__':
616	    main()
617	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9061248f-6cce-4556-8d75-c24978f88fb5",
  "isSidechain": false,
  "promptId": "931f36b2-6e79-486e-89c9-9074426aeee2",
  "type": "user",
  "uuid": "805facd5-9af0-472b-b2ac-59ab414754a1",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_ppi_empirical.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nEmpirical Correction Validation — HumAID K=10\n\nLoads 8 valid HumAID confusion matrices from asv_empirical_results.json,\ngenerates synthetic MC data using plan_006's K=10 DGP for each of 7 topologies,\nruns all 5 correction methods (PPI++, naive plug-in, DSL, MC-SIMEX, MLA),\nand reports empirical bias reduction per topology × method.\n\nInput:  artifacts/plan006/asv_empirical_results.json\nOutput: artifacts/ppi_empirical_validation.json\n\nDependencies: numpy, annot_sensitivity (local package)\n\"\"\"\n\nimport sys\nimport os\nimport json\nimport time\nimport numpy as np\n\nPROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nsys.path.insert(0, PROJECT_ROOT)\n\nfrom annot_sensitivity.correction import (\n    correct_ppi, correct_naive_plugin, correct_dsl, correct_mcsimex, correct_mla\n)\nfrom annot_sensitivity.utils import misclassify, make_dummies, ols, ols_with_se\n\n# ── Plan 006 DGP Infrastructure (K-general) ────────────────────────\n\n_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]\n_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]\n_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]\n_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2, 0.15, -0.1, 0.05]\n\n\ndef softmax_rows(logits):\n    e = np.exp(logits - logits.max(axis=1, keepdims=True))\n    return e / e.sum(axis=1, keepdims=True)\n\n\ndef sample_cat(probs, rng):\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=probs.shape[0])[:, None]\n    return (u >= cum[:, :-1]).sum(axis=1).astype(int)\n\n\ndef make_p_A(K):\n    if K == 2:\n        return np.array([0.55, 0.45])\n    elif K == 3:\n        return np.array([0.40, 0.35, 0.25])\n    else:\n        raw = np.array([1.0 / (i + 1) for i in range(K)])\n        return raw / raw.sum()\n\n\ndef make_dgp_params(K):\n    p_A = make_p_A(K)\n    params = {\n        'confounding': {\n            'p_A': p_A,\n            'alpha': np.array(_ALPHA_POOL[:K - 1]),\n            'beta_A': np.array(_BETA_A_POOL[:K - 1]),\n            'beta_T': 2.0,\n            'sigma_T': 1.0,\n        },\n        'mediation': {\n            'tau': 0.5,\n            'gamma': np.array(_GAMMA_POOL[:K]),\n            'delta': np.array(_DELTA_POOL[:K]),\n            'beta': np.array(_BETA_POOL[:K]),\n        },\n        'collider': {\n            'tau': 1.0,\n            'g': np.zeros(K),\n            'dT': np.array(_DT_POOL[:K]),\n            'dY': np.array(_DY_POOL[:K]),\n        },\n        'exposure': {\n            'beta': np.array(_BETA_POOL[:K]),\n            'p_A': p_A,\n        },\n    }\n    if K == 3:\n        params['mbias'] = {\n            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,\n            'g': np.zeros(3),\n            'a_U1': np.array([0.0, 0.8, -0.5]),\n            'a_U2': np.array([0.0, 0.6, 0.9]),\n        }\n        params['iv'] = {\n            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),\n            'g': np.zeros(3),\n            'dZ': np.array([0.0, 1.0, -0.5]),\n            'dU': np.array([0.0, 0.8, 0.6]),\n        }\n        params['frontdoor'] = {\n            'alpha_U': 1.0, 'lambda_U': 1.0,\n            'gamma': np.array([0.0, 0.5, -0.3]),\n            'delta_fd': np.array([0.0, 1.0, -0.8]),\n            'beta': np.array([0.0, 1.0, -0.5]),\n        }\n    else:\n        params['mbias'] = {\n            'tau': 0.5, 'delta_coef': 1.0, 'lam': 1.0,\n            'g': np.zeros(K),\n            'a_U1': np.array([0.0] + [_ALPHA_POOL[i] * 0.6 for i in range(K - 1)]),\n            'a_U2': np.array([0.0] + [_BETA_A_POOL[i] * 0.8 for i in range(K - 1)]),\n        }\n        iv_beta = np.array(_BETA_POOL[:K]) * 0.5\n        iv_beta[0] = 0.0\n        params['iv'] = {\n            'lam': 1.0, 'beta': iv_beta,\n            'g': np.zeros(K),\n            'dZ': np.array([0.0] + [_ALPHA_POOL[i] * 0.7 for i in range(K - 1)]),\n            'dU': np.array([0.0] + [_BETA_A_POOL[i] * 0.6 for i in range(K - 1)]),\n        }\n        fd_delta = np.array(_DELTA_POOL[:K])\n        fd_delta[0] = 0.0\n        params['frontdoor'] = {\n            'alpha_U': 1.0, 'lambda_U': 1.0,\n            'gamma': np.array(_GAMMA_POOL[:K]),\n            'delta_fd': fd_delta,\n            'beta': np.array(_BETA_POOL[:K]),\n        }\n    return params\n\n\n# ── DGP Generators ──────────────────────────────────────────────────\n\ndef gen_confounding(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)\n    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_mediation(K, N, p, rng):\n    T = rng.binomial(1, 0.5, N).astype(float)\n    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_collider(K, N, p, rng):\n    T = rng.normal(0, 1, N)\n    Y = p['tau'] * T + rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dT'][None, :] * T[:, None]\n              + p['dY'][None, :] * Y[:, None])\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    return T, Y, A\n\n\ndef gen_exposure(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)\n    return None, Y, A\n\n\ndef gen_mbias(K, N, p, rng):\n    U1 = rng.normal(0, 1, N)\n    U2 = rng.normal(0, 1, N)\n    T = p['delta_coef'] * U1 + rng.normal(0, 1, N)\n    Y = p['tau'] * T + p['lam'] * U2 + rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['a_U1'][None, :] * U1[:, None]\n              + p['a_U2'][None, :] * U2[:, None])\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    return T, Y, A\n\n\ndef gen_iv(K, N, p, rng):\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dZ'][None, :] * Z[:, None]\n              + p['dU'][None, :] * U[:, None])\n    probs = softmax_rows(logits)\n    A = sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam'] * U + rng.normal(0, 1, N)\n    return Z, Y, A\n\n\ndef gen_frontdoor(K, N, p, rng):\n    U = rng.normal(0, 1, N)\n    T = p['alpha_U'] * U + rng.normal(0, 1, N)\n    logits = p['gamma'][None, :] + p['delta_fd'][None, :] * T[:, None]\n    probs = softmax_rows(logits)\n    M = sample_cat(probs, rng)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (M == j + 1).astype(float)\n    Y = D @ p['beta'][1:] + p['lambda_U'] * U + rng.normal(0, 1, N)\n    return T, Y, M\n\n\nGEN_FNS = {\n    'confounding': gen_confounding, 'mediation': gen_mediation,\n    'collider': gen_collider, 'exposure': gen_exposure,\n    'mbias': gen_mbias, 'iv': gen_iv, 'frontdoor': gen_frontdoor,\n}\n\nHAS_TREATMENT = {'confounding', 'mediation', 'collider', 'mbias', 'frontdoor'}\n\n\n# ── Wald Estimator ──────────────────────────────────────────────────\n\ndef wald_est(Z, Y, A_or_Astar, k=1):\n    z1 = Z == 1; z0 = Z == 0\n    n1, n0 = float(z1.sum()), float(z0.sum())\n    if n1 < 2 or n0 < 2:\n        return np.nan\n    RF = Y[z1].mean() - Y[z0].mean()\n    FS = (A_or_Astar[z1] == k).astype(float).mean() - \\\n         (A_or_Astar[z0] == k).astype(float).mean()\n    if abs(FS) < 1e-8:\n        return np.nan\n    return RF / FS\n\n\ndef ppi_wald(Z, Y, A, Astar, gold_mask, k=1, rng=None, n_boot=50):\n    \"\"\"PPI++ for Wald estimator (IV topology).\"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    gold_idx = np.where(gold_mask)[0]\n    n_gold = len(gold_idx)\n\n    tau_all_star = wald_est(Z, Y, Astar, k)\n    tau_gold_true = wald_est(Z[gold_mask], Y[gold_mask], A[gold_mask], k)\n    tau_gold_star = wald_est(Z[gold_mask], Y[gold_mask], Astar[gold_mask], k)\n\n    if np.isnan(tau_gold_true) or np.isnan(tau_all_star):\n        return np.nan, False\n\n    tau_true_boot = np.zeros(n_boot)\n    tau_rect_boot = np.zeros(n_boot)\n    for b in range(n_boot):\n        idx = rng.choice(gold_idx, size=n_gold, replace=True)\n        bt = wald_est(Z[idx], Y[idx], A[idx], k)\n        bs = wald_est(Z[idx], Y[idx], Astar[idx], k)\n        tau_true_boot[b] = bt\n        tau_rect_boot[b] = bs - bt\n\n    valid = np.isfinite(tau_true_boot) & np.isfinite(tau_rect_boot)\n    if valid.sum() > 5:\n        var_r = np.var(tau_rect_boot[valid])\n        cov_tr = np.cov(tau_true_boot[valid], tau_rect_boot[valid])[0, 1]\n        lam = np.clip(-cov_tr / var_r, 0, 1) if var_r > 1e-12 else 1.0\n    else:\n        lam = 1.0\n\n    tau_ppi = tau_gold_true + lam * (tau_all_star - tau_gold_star)\n    return float(tau_ppi), True\n\n\n# ── True Parameter Computation ──────────────────────────────────────\n\ndef compute_tau_true(K, topology, params, N_large=500_000, seed=99):\n    \"\"\"Compute true tau by running estimator on very large uncontaminated sample.\"\"\"\n    rng = np.random.default_rng(seed)\n    first_var, Y, A = GEN_FNS[topology](K, N_large, params[topology], rng)\n\n    if topology == 'iv':\n        return wald_est(first_var, Y, A, k=1)\n    elif topology == 'exposure':\n        D = make_dummies(A, K)\n        X = np.column_stack([np.ones(N_large), D])\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        return float(beta[1])\n    else:\n        T = first_var\n        D = make_dummies(A, K)\n        X = np.column_stack([np.ones(N_large), T, D])\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        return float(beta[1])\n\n\n# ── MC-SIMEX for IV (custom) ────────────────────────────────────────\n\ndef mcsimex_wald(Z, Y, Astar, C, k=1, rng=None, n_B=50,\n                 lambdas_extra=(0.5, 1.0, 1.5, 2.0)):\n    \"\"\"MC-SIMEX for IV Wald estimator.\"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    K = C.shape[0]\n    try:\n        eigvals, eigvecs = np.linalg.eig(C)\n        eigvecs_inv = np.linalg.inv(eigvecs)\n    except np.linalg.LinAlgError:\n        return np.nan, False\n\n    lambdas = np.array([0.0] + list(lambdas_extra))\n    tau_lam = np.zeros(len(lambdas))\n\n    for li, lam_val in enumerate(lambdas):\n        if lam_val == 0.0:\n            tau_lam[li] = wald_est(Z, Y, Astar, k)\n        else:\n            C_lam_raw = np.real((eigvecs * (eigvals ** lam_val)) @ eigvecs_inv)\n            C_lam = np.clip(C_lam_raw, 0, None)\n            cs = C_lam.sum(axis=0)\n            cs[cs == 0] = 1.0\n            C_lam /= cs\n\n            tau_b = np.zeros(n_B)\n            for b in range(n_B):\n                A_extra = misclassify(Astar, C_lam, rng)\n                tau_b[b] = wald_est(Z, Y, A_extra, k)\n            ok = np.isfinite(tau_b)\n            if ok.sum() < n_B // 2:\n                return np.nan, False\n            tau_lam[li] = tau_b[ok].mean()\n\n    try:\n        coeffs = np.polyfit(lambdas, tau_lam, 2)\n        return float(np.polyval(coeffs, -1.0)), True\n    except Exception:\n        return np.nan, False\n\n\n# ── Main ────────────────────────────────────────────────────────────\n\nN_SAMPLES = 10_000\nN_REPS = 30\nGOLD_FRACTION = 0.10\nSEED = 42\nTOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',\n              'mbias', 'iv', 'frontdoor']\nMETHODS = ['ppi', 'naive_plugin', 'dsl', 'mcsimex', 'mla']\n\nJSON_PATH = os.path.join(PROJECT_ROOT, 'artifacts', 'plan006',\n                         'asv_empirical_results.json')\n\n\ndef load_valid_humaid_configs():\n    with open(JSON_PATH) as f:\n        data = json.load(f)\n\n    zero_configs = {(e['model'], e['prompt'])\n                    for e in data['f1_vs_bias'] if e['macro_f1'] == 0}\n\n    cms = {}\n    for key, mat in data['confusion_matrices'].items():\n        parts = key.split('_')\n        if parts[0] != 'humaid':\n            continue\n        model = parts[1]\n        prompt = '_'.join(parts[2:])\n        if (model, prompt) in zero_configs:\n            continue\n        cms[key] = np.array(mat)\n    return cms\n\n\ndef run_single_rep(K, topology, params, C, tau_true, rng, gold_frac):\n    \"\"\"Run one MC replication: generate data, misclassify, run corrections.\"\"\"\n    first_var, Y, A = GEN_FNS[topology](K, N_SAMPLES, params[topology], rng)\n    Astar = misclassify(A, C, rng)\n\n    N = len(Y)\n    n_gold = max(int(N * gold_frac), 50)\n    gold_idx = rng.choice(N, size=n_gold, replace=False)\n    gold_mask = np.zeros(N, dtype=bool)\n    gold_mask[gold_idx] = True\n\n    results = {}\n\n    if topology == 'iv':\n        Z = first_var\n        tau_naive = wald_est(Z, Y, Astar, k=1)\n        results['naive'] = float(tau_naive) if np.isfinite(tau_naive) else None\n\n        tau_ppi, ok = ppi_wald(Z, Y, A, Astar, gold_mask, k=1, rng=rng)\n        results['ppi'] = float(tau_ppi) if ok and np.isfinite(tau_ppi) else None\n\n        tau_sim, ok = mcsimex_wald(Z, Y, Astar, C, k=1, rng=rng)\n        results['mcsimex'] = float(tau_sim) if ok and np.isfinite(tau_sim) else None\n\n        results['naive_plugin'] = None\n        results['dsl'] = None\n        results['mla'] = None\n\n    elif topology == 'exposure':\n        X_other = np.ones((N, 1))\n        D_star = make_dummies(Astar, K)\n        X_full = np.column_stack([X_other, D_star])\n        try:\n            beta_naive = np.linalg.lstsq(X_full, Y, rcond=None)[0]\n            tau_naive = float(beta_naive[1])\n        except Exception:\n            tau_naive = np.nan\n        results['naive'] = float(tau_naive) if np.isfinite(tau_naive) else None\n\n        for method in METHODS:\n            if method == 'ppi':\n                tau, se, ok = correct_ppi(X_other, Y, Astar, A, gold_mask,\n                                          tau_idx=1, rng=rng)\n            elif method == 'naive_plugin':\n                tau, se, ok = correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1)\n            elif method == 'dsl':\n                tau, se, ok = correct_dsl(X_other, Y, Astar, A, gold_mask, tau_idx=1)\n            elif method == 'mcsimex':\n                tau, se, ok = correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=rng)\n            elif method == 'mla':\n                tau, se, ok = correct_mla(X_other, Y, Astar, C, tau_idx=1)\n            else:\n                continue\n            results[method] = float(tau) if ok and np.isfinite(tau) else None\n\n    else:\n        T = first_var\n        X_other = np.column_stack([np.ones(N), T])\n        D_star = make_dummies(Astar, K)\n        X_full = np.column_stack([X_other, D_star])\n        try:\n            beta_naive = np.linalg.lstsq(X_full, Y, rcond=None)[0]\n            tau_naive = float(beta_naive[1])\n        except Exception:\n            tau_naive = np.nan\n        results['naive'] = float(tau_naive) if np.isfinite(tau_naive) else None\n\n        for method in METHODS:\n            if method == 'ppi':\n                tau, se, ok = correct_ppi(X_other, Y, Astar, A, gold_mask,\n                                          tau_idx=1, rng=rng)\n            elif method == 'naive_plugin':\n                tau, se, ok = correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1)\n            elif method == 'dsl':\n                tau, se, ok = correct_dsl(X_other, Y, Astar, A, gold_mask, tau_idx=1)\n            elif method == 'mcsimex':\n                tau, se, ok = correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=rng)\n            elif method == 'mla':\n                tau, se, ok = correct_mla(X_other, Y, Astar, C, tau_idx=1)\n            else:\n                continue\n            results[method] = float(tau) if ok and np.isfinite(tau) else None\n\n    results['tau_true'] = tau_true\n    return results\n\n\ndef main():\n    t_start = time.time()\n    K = 10\n    print(\"=\" * 70)\n    print(\"Empirical Correction Validation — HumAID K=10\")\n    print(\"=\" * 70)\n    print(f\"N={N_SAMPLES}, N_REPS={N_REPS}, gold_fraction={GOLD_FRACTION}\")\n\n    configs = load_valid_humaid_configs()\n    print(f\"Loaded {len(configs)} valid HumAID confusion matrices\")\n\n    params = make_dgp_params(K)\n    rng_master = np.random.default_rng(SEED)\n\n    print(\"\\nComputing tau_true for each topology (N=500k)...\")\n    tau_true = {}\n    for topo in TOPOLOGIES:\n        tau_true[topo] = compute_tau_true(K, topo, params)\n        print(f\"  {topo}: tau_true = {tau_true[topo]:.6f}\")\n\n    all_results = {}\n    per_topo_method = {topo: {m: [] for m in METHODS}\n                       for topo in TOPOLOGIES}\n\n    for ci, (config_name, C) in enumerate(configs.items()):\n        print(f\"\\n[{ci+1}/{len(configs)}] {config_name}\")\n        config_results = {}\n\n        for topo in TOPOLOGIES:\n            topo_reps = []\n            for rep in range(N_REPS):\n                seed_rep = rng_master.integers(0, 2**31)\n                rng_rep = np.random.default_rng(seed_rep)\n                res = run_single_rep(K, topo, params, C, tau_true[topo],\n                                     rng_rep, GOLD_FRACTION)\n                topo_reps.append(res)\n\n            naive_biases = []\n            method_biases = {m: [] for m in METHODS}\n            for res in topo_reps:\n                tt = res['tau_true']\n                if res['naive'] is not None:\n                    naive_biases.append(res['naive'] - tt)\n                for m in METHODS:\n                    if res.get(m) is not None:\n                        method_biases[m].append(res[m] - tt)\n\n            avg_naive_bias = np.mean(np.abs(naive_biases)) if naive_biases else None\n            topo_summary = {\n                'tau_true': tau_true[topo],\n                'n_reps': N_REPS,\n                'naive_mean_abs_bias': float(avg_naive_bias) if avg_naive_bias else None,\n                'methods': {},\n            }\n\n            for m in METHODS:\n                biases = method_biases[m]\n                if biases:\n                    avg_abs = float(np.mean(np.abs(biases)))\n                    mean_bias = float(np.mean(biases))\n                    if avg_naive_bias and avg_naive_bias > 1e-8:\n                        reduction = 1.0 - avg_abs / avg_naive_bias\n                    else:\n                        reduction = None\n                    topo_summary['methods'][m] = {\n                        'mean_abs_bias': avg_abs,\n                        'mean_bias': mean_bias,\n                        'bias_reduction': float(reduction) if reduction is not None else None,\n                        'n_valid': len(biases),\n                    }\n                    per_topo_method[topo][m].append(\n                        float(reduction) if reduction is not None else None\n                    )\n                else:\n                    topo_summary['methods'][m] = {\n                        'mean_abs_bias': None,\n                        'mean_bias': None,\n                        'bias_reduction': None,\n                        'n_valid': 0,\n                    }\n\n            config_results[topo] = topo_summary\n            ppi_info = topo_summary['methods'].get('ppi', {})\n            ppi_red = ppi_info.get('bias_reduction')\n            ppi_str = f\"{100*ppi_red:.1f}%\" if ppi_red is not None else \"N/A\"\n            print(f\"  {topo:12s}: naive_bias={avg_naive_bias:.4f}\" if avg_naive_bias else\n                  f\"  {topo:12s}: naive_bias=N/A\", end=\"\")\n            print(f\"  PPI++={ppi_str}\")\n\n        all_results[config_name] = config_results\n\n    grand_summary = {}\n    print(\"\\n\" + \"=\" * 70)\n    print(\"GRAND SUMMARY: Mean bias reduction across 8 configs\")\n    print(\"=\" * 70)\n    print(f\"\\n{'Topology':14s}\", end=\"\")\n    for m in METHODS:\n        print(f\"  {m:14s}\", end=\"\")\n    print()\n    print(\"-\" * (14 + 16 * len(METHODS)))\n\n    for topo in TOPOLOGIES:\n        grand_summary[topo] = {}\n        print(f\"{topo:14s}\", end=\"\")\n        for m in METHODS:\n            vals = [v for v in per_topo_method[topo][m] if v is not None]\n            if vals:\n                mean_red = float(np.mean(vals))\n                grand_summary[topo][m] = {\n                    'mean_reduction': mean_red,\n                    'std_reduction': float(np.std(vals)),\n                    'n_configs': len(vals),\n                }\n                print(f\"  {100*mean_red:+12.1f}%\", end=\"\")\n            else:\n                grand_summary[topo][m] = None\n                print(f\"  {'N/A':>13s}\", end=\"\")\n        print()\n\n    overall_ppi = []\n    for topo in TOPOLOGIES:\n        gs = grand_summary[topo].get('ppi')\n        if gs:\n            overall_ppi.append(gs['mean_reduction'])\n    if overall_ppi:\n        print(f\"\\nGrand mean PPI++ bias reduction: {100*np.mean(overall_ppi):.1f}%\")\n\n    output = {\n        'meta': {\n            'scope': 'HumAID K=10, 8 valid configs',\n            'n_samples': N_SAMPLES,\n            'n_reps': N_REPS,\n            'gold_fraction': GOLD_FRACTION,\n            'seed': SEED,\n            'topologies': TOPOLOGIES,\n            'methods': METHODS,\n            'n_configs': len(configs),\n            'configs': list(configs.keys()),\n        },\n        'tau_true': {t: float(tau_true[t]) for t in TOPOLOGIES},\n        'per_config': all_results,\n        'grand_summary': grand_summary,\n    }\n\n    out_path = os.path.join(PROJECT_ROOT, 'artifacts',\n                            'ppi_empirical_validation.json')\n    with open(out_path, 'w') as f:\n        json.dump(output, f, indent=2)\n\n    elapsed = time.time() - t_start\n    print(f\"\\nResults saved to: {out_path}\")\n    print(f\"Total runtime: {elapsed:.1f}s\")\n\n\nif __name__ == '__main__':\n    main()\n",
      "numLines": 617,
      "startLine": 1,
      "totalLines": 617
    }
  },
  "sourceToolAssistantUUID": "9061248f-6cce-4556-8d75-c24978f88fb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T14:35:38.736Z_

<details><summary>↩ Tool result · `toolu_01HZghw5juYNQNtPpfS8TVQk`</summary>

```text
1	"""Confusion matrix utilities: validation, generation, interpolation.
2	
3	Convention: C[j, i] = P(A*=j | A=i), columns sum to 1 (column-stochastic).
4	"""
5	
6	import numpy as np
7	
8	
9	def validate_confusion_matrix(C):
10	    """Check if C is a valid column-stochastic confusion matrix.
11	
12	    Args:
13	        C: array to validate
14	
15	    Returns:
16	        True if valid, False otherwise
17	    """
18	    if not isinstance(C, np.ndarray):
19	        return False
20	    if C.ndim != 2 or C.shape[0] != C.shape[1]:
21	        return False
22	    if C.shape[0] < 2:
23	        return False
24	    if (C < -1e-10).any():
25	        return False
26	    if not np.allclose(C.sum(axis=0), 1.0, atol=1e-6):
27	        return False
28	    return True
29	
30	
31	def random_confusion_matrix(K, diag_dominance=0.8, rng=None):
32	    """Generate a random column-stochastic confusion matrix.
33	
34	    Args:
35	        K: number of categories
36	        diag_dominance: controls diagonal strength (0 to 1)
37	        rng: numpy random Generator (created if None)
38	
39	    Returns:
40	        (K, K) column-stochastic matrix
41	    """
42	    if rng is None:
43	        rng = np.random.default_rng()
44	    diag_alpha = diag_dominance * 10
45	    offdiag_alpha = max((1 - diag_dominance) * 10 / max(K - 1, 1), 0.1)
46	    C = np.zeros((K, K))
47	    for k in range(K):
48	        alphas = np.full(K, offdiag_alpha)
49	        alphas[k] = diag_alpha
50	        C[:, k] = rng.dirichlet(alphas)
51	    return C
52	
53	
54	def interpolate_confusion(C0, delta):
55	    """Interpolate between identity and C0: C(delta) = (1-delta)*I + delta*C0.
56	
57	    Args:
58	        C0: (K, K) base confusion matrix
59	        delta: interpolation parameter (0 = identity, 1 = C0)
60	
61	    Returns:
62	        (K, K) interpolated column-stochastic matrix
63	    """
64	    K = C0.shape[0]
65	    C = (1 - delta) * np.eye(K) + delta * C0
66	    C = np.maximum(C, 0.0)
67	    col_sums = C.sum(axis=0)
68	    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
69	    return C / col_sums
70	
71	
72	def delta_range(C0):
73	    """Compute valid delta range for interpolation.
74	
75	    Args:
76	        C0: (K, K) base confusion matrix
77	
78	    Returns:
79	        (delta_min, delta_max) tuple
80	    """
81	    min_diag = np.diag(C0).min()
82	    if min_diag >= 1.0:
83	        return (0.0, 10.0)
84	    delta_max = min(1.0 / (1.0 - min_diag), 10.0)
85	    return (0.0, delta_max)
86	
87	
88	def predefined_matrices(K=3):
89	    """Return a dict of predefined K x K confusion matrices.
90	
91	    Args:
92	        K: number of categories (only K=3 supported)
93	
94	    Returns:
95	        dict mapping name to (K, K) confusion matrix
96	    """
97	    if K != 3:
98	        raise ValueError(f"Predefined matrices only available for K=3, got K={K}")
99	    return {
100	        "symmetric_high": np.array([
101	            [0.80, 0.10, 0.10],
102	            [0.10, 0.80, 0.10],
103	            [0.10, 0.10, 0.80]]),
104	        "mild_uniform": np.array([
105	            [0.8 + 0.2 / 3, 0.2 / 3, 0.2 / 3],
106	            [0.2 / 3, 0.8 + 0.2 / 3, 0.2 / 3],
107	            [0.2 / 3, 0.2 / 3, 0.8 + 0.2 / 3]]),
108	        "moderate_uniform": np.array([
109	            [0.6 + 0.4 / 3, 0.4 / 3, 0.4 / 3],
110	            [0.4 / 3, 0.6 + 0.4 / 3, 0.4 / 3],
111	            [0.4 / 3, 0.4 / 3, 0.6 + 0.4 / 3]]),
112	        "severe_uniform": np.array([
113	            [0.4 + 0.6 / 3, 0.6 / 3, 0.6 / 3],
114	            [0.6 / 3, 0.4 + 0.6 / 3, 0.6 / 3],
115	            [0.6 / 3, 0.6 / 3, 0.4 + 0.6 / 3]]),
116	        "asymmetric": np.array([
117	            [0.75, 0.05, 0.05],
118	            [0.20, 0.80, 0.10],
119	            [0.05, 0.15, 0.85]]),
120	        "near_permutation": np.array([
121	            [0.05, 0.05, 0.90],
122	            [0.90, 0.05, 0.05],
123	            [0.05, 0.90, 0.05]]),
124	        "realistic_llm": np.array([
125	            [0.78, 0.15, 0.03],
126	            [0.18, 0.72, 0.18],
127	            [0.04, 0.13, 0.79]]),
128	    }
129	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f32b727-3447-4d8d-902f-e6d8ff815046",
  "isSidechain": false,
  "promptId": "931f36b2-6e79-486e-89c9-9074426aeee2",
  "type": "user",
  "uuid": "2ac0164a-81f6-45ca-a2d2-ce01ebc304d6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/confusion.py",
      "content": "\"\"\"Confusion matrix utilities: validation, generation, interpolation.\n\nConvention: C[j, i] = P(A*=j | A=i), columns sum to 1 (column-stochastic).\n\"\"\"\n\nimport numpy as np\n\n\ndef validate_confusion_matrix(C):\n    \"\"\"Check if C is a valid column-stochastic confusion matrix.\n\n    Args:\n        C: array to validate\n\n    Returns:\n        True if valid, False otherwise\n    \"\"\"\n    if not isinstance(C, np.ndarray):\n        return False\n    if C.ndim != 2 or C.shape[0] != C.shape[1]:\n        return False\n    if C.shape[0] < 2:\n        return False\n    if (C < -1e-10).any():\n        return False\n    if not np.allclose(C.sum(axis=0), 1.0, atol=1e-6):\n        return False\n    return True\n\n\ndef random_confusion_matrix(K, diag_dominance=0.8, rng=None):\n    \"\"\"Generate a random column-stochastic confusion matrix.\n\n    Args:\n        K: number of categories\n        diag_dominance: controls diagonal strength (0 to 1)\n        rng: numpy random Generator (created if None)\n\n    Returns:\n        (K, K) column-stochastic matrix\n    \"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    diag_alpha = diag_dominance * 10\n    offdiag_alpha = max((1 - diag_dominance) * 10 / max(K - 1, 1), 0.1)\n    C = np.zeros((K, K))\n    for k in range(K):\n        alphas = np.full(K, offdiag_alpha)\n        alphas[k] = diag_alpha\n        C[:, k] = rng.dirichlet(alphas)\n    return C\n\n\ndef interpolate_confusion(C0, delta):\n    \"\"\"Interpolate between identity and C0: C(delta) = (1-delta)*I + delta*C0.\n\n    Args:\n        C0: (K, K) base confusion matrix\n        delta: interpolation parameter (0 = identity, 1 = C0)\n\n    Returns:\n        (K, K) interpolated column-stochastic matrix\n    \"\"\"\n    K = C0.shape[0]\n    C = (1 - delta) * np.eye(K) + delta * C0\n    C = np.maximum(C, 0.0)\n    col_sums = C.sum(axis=0)\n    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\n    return C / col_sums\n\n\ndef delta_range(C0):\n    \"\"\"Compute valid delta range for interpolation.\n\n    Args:\n        C0: (K, K) base confusion matrix\n\n    Returns:\n        (delta_min, delta_max) tuple\n    \"\"\"\n    min_diag = np.diag(C0).min()\n    if min_diag >= 1.0:\n        return (0.0, 10.0)\n    delta_max = min(1.0 / (1.0 - min_diag), 10.0)\n    return (0.0, delta_max)\n\n\ndef predefined_matrices(K=3):\n    \"\"\"Return a dict of predefined K x K confusion matrices.\n\n    Args:\n        K: number of categories (only K=3 supported)\n\n    Returns:\n        dict mapping name to (K, K) confusion matrix\n    \"\"\"\n    if K != 3:\n        raise ValueError(f\"Predefined matrices only available for K=3, got K={K}\")\n    return {\n        \"symmetric_high\": np.array([\n            [0.80, 0.10, 0.10],\n            [0.10, 0.80, 0.10],\n            [0.10, 0.10, 0.80]]),\n        \"mild_uniform\": np.array([\n            [0.8 + 0.2 / 3, 0.2 / 3, 0.2 / 3],\n            [0.2 / 3, 0.8 + 0.2 / 3, 0.2 / 3],\n            [0.2 / 3, 0.2 / 3, 0.8 + 0.2 / 3]]),\n        \"moderate_uniform\": np.array([\n            [0.6 + 0.4 / 3, 0.4 / 3, 0.4 / 3],\n            [0.4 / 3, 0.6 + 0.4 / 3, 0.4 / 3],\n            [0.4 / 3, 0.4 / 3, 0.6 + 0.4 / 3]]),\n        \"severe_uniform\": np.array([\n            [0.4 + 0.6 / 3, 0.6 / 3, 0.6 / 3],\n            [0.6 / 3, 0.4 + 0.6 / 3, 0.6 / 3],\n            [0.6 / 3, 0.6 / 3, 0.4 + 0.6 / 3]]),\n        \"asymmetric\": np.array([\n            [0.75, 0.05, 0.05],\n            [0.20, 0.80, 0.10],\n            [0.05, 0.15, 0.85]]),\n        \"near_permutation\": np.array([\n            [0.05, 0.05, 0.90],\n            [0.90, 0.05, 0.05],\n            [0.05, 0.90, 0.05]]),\n        \"realistic_llm\": np.array([\n            [0.78, 0.15, 0.03],\n            [0.18, 0.72, 0.18],\n            [0.04, 0.13, 0.79]]),\n    }\n",
      "numLines": 129,
      "startLine": 1,
      "totalLines": 129
    }
  },
  "sourceToolAssistantUUID": "7f32b727-3447-4d8d-902f-e6d8ff815046",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T14:35:38.368Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Jzin1Vjz7busUMTikeKYnh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/dgp.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "805facd5-9af0-472b-b2ac-59ab414754a1",
  "isSidechain": false,
  "requestId": "req_011CbKfg7UzmXxEYXiJRtj8R",
  "type": "assistant",
  "uuid": "71959910-e9fa-4c60-ba97-43b9b044202d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rerXLcjU94zeauoAzfSkR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3631,
      "cache_read_input_tokens": 26105,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 26105,
          "cache_creation_input_tokens": 3631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3631
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

_source line 19 · 2026-05-23T14:35:38.372Z_

<details><summary>↩ Tool result · `toolu_01Jzin1Vjz7busUMTikeKYnh`</summary>

```text
1	"""Data generation processes for 7 DAG topologies.
2	
3	Each topology generates synthetic data with a known causal structure.
4	The variable A (or M for frontdoor) is the one subject to misclassification.
5	"""
6	
7	import numpy as np
8	from .utils import softmax_sample, make_dummies
9	
10	DEFAULT_PARAMS = {
11	    "confounding": dict(
12	        p_A=np.array([0.40, 0.35, 0.25]),
13	        alpha=np.array([1.5, -1.0]),
14	        beta_A=np.array([1.0, -0.5]),
15	        beta_T=2.0, sigma_T=1.0),
16	    "mediation": dict(
17	        tau=0.5,
18	        gamma=np.array([0.0, 0.5, -0.3]),
19	        delta=np.array([0.0, 0.8, -0.6]),
20	        beta=np.array([0.0, 1.0, -0.5])),
21	    "collider": dict(
22	        tau=1.0,
23	        g=np.array([0.0, 0.0, 0.0]),
24	        dT=np.array([0.0, 0.5, -0.3]),
25	        dY=np.array([0.0, 0.8, 0.6])),
26	    "exposure": dict(
27	        beta=np.array([0.0, 1.0, -0.5]),
28	        p_A=np.array([0.40, 0.35, 0.25])),
29	    "mbias": dict(
30	        tau=1.0, delta_coef=1.0, lam=1.0,
31	        g=np.array([0.0, 0.0, 0.0]),
32	        a1=np.array([0.0, 0.8, -0.5]),
33	        a2=np.array([0.0, 0.6, 0.9])),
34	    "iv": dict(
35	        lam=1.0,
36	        g=np.array([0.0, 0.0, 0.0]),
37	        dZ=np.array([0.0, 1.0, -0.5]),
38	        dU=np.array([0.0, 0.8, 0.6]),
39	        beta=np.array([0.0, 1.0, -0.5])),
40	    "frontdoor": dict(
41	        alpha_U=1.0, lam_U=1.0,
42	        gamma=np.array([0.0, 0.5, -0.3]),
43	        delta=np.array([0.0, 1.0, -0.8]),
44	        beta=np.array([0.0, 1.0, -0.5])),
45	}
46	
47	TOPOLOGIES = list(DEFAULT_PARAMS.keys())
48	
49	HAS_TREATMENT = {"confounding", "mediation", "collider", "mbias", "frontdoor"}
50	NO_TREATMENT = {"exposure", "iv"}
51	
52	
53	def _get_rng(rng, seed):
54	    if rng is not None:
55	        return rng
56	    return np.random.default_rng(seed)
57	
58	
59	def _get_params(topology, params):
60	    p = dict(DEFAULT_PARAMS[topology])
61	    if params is not None:
62	        p.update(params)
63	    return p
64	
65	
66	def gen_confounding(N, params=None, rng=None, seed=None):
67	    """A->T, A->Y, T->Y. Researcher controls for A*.
68	
69	    Returns:
70	        dict with keys T, Y, A
71	    """
72	    rng = _get_rng(rng, seed)
73	    p = _get_params("confounding", params)
74	    K = len(p["p_A"])
75	    A = rng.choice(K, size=N, p=p["p_A"])
76	    D = make_dummies(A, K)
77	    T = D @ p["alpha"] + rng.normal(0, p["sigma_T"], N)
78	    Y = p["beta_T"] * T + D @ p["beta_A"] + rng.normal(0, 1, N)
79	    return {"T": T, "Y": Y, "A": A}
80	
81	
82	def gen_mediation(N, params=None, rng=None, seed=None):
83	    """T->A->Y. A mediates; researcher controls for A*.
84	
85	    Returns:
86	        dict with keys T, Y, A
87	    """
88	    rng = _get_rng(rng, seed)
89	    p = _get_params("mediation", params)
90	    T = rng.binomial(1, 0.5, N).astype(float)
91	    K = len(p["gamma"])
92	    logits = p["gamma"][None, :] + p["delta"][None, :] * T[:, None]
93	    A = softmax_sample(logits, rng)
94	    D = make_dummies(A, K)
95	    Y = p["beta"][0] + D @ p["beta"][1:] + p["tau"] * T + rng.normal(0, 1, N)
96	    return {"T": T, "Y": Y, "A": A}
97	
98	
99	def gen_collider(N, params=None, rng=None, seed=None):
100	    """T->A<-Y. Researcher wrongly controls for A*.
101	
102	    Returns:
103	        dict with keys T, Y, A
104	    """
105	    rng = _get_rng(rng, seed)
106	    p = _get_params("collider", params)
107	    T = rng.normal(0, 1, N)
108	    Y = p["tau"] * T + rng.normal(0, 1, N)
109	    logits = (p["g"][None, :] + p["dT"][None, :] * T[:, None]
110	              + p["dY"][None, :] * Y[:, None])
111	    A = softmax_sample(logits, rng)
112	    return {"T": T, "Y": Y, "A": A}
113	
114	
115	def gen_exposure(N, params=None, rng=None, seed=None):
116	    """A->Y (direct exposure, no treatment T).
117	
118	    Returns:
119	        dict with keys Y, A
120	    """
121	    rng = _get_rng(rng, seed)
122	    p = _get_params("exposure", params)
123	    K = len(p["p_A"])
124	    A = rng.choice(K, size=N, p=p["p_A"])
125	    D = make_dummies(A, K)
126	    Y = p["beta"][0] + D @ p["beta"][1:] + rng.normal(0, 1, N)
127	    return {"Y": Y, "A": A}
128	
129	
130	def gen_mbias(N, params=None, rng=None, seed=None):
131	    """U1->{A,T}, U2->{A,Y}, T->Y. Conditioning on A* induces M-bias.
132	
133	    Returns:
134	        dict with keys T, Y, A
135	    """
136	    rng = _get_rng(rng, seed)
137	    p = _get_params("mbias", params)
138	    N_out = N
139	    U1, U2 = rng.normal(0, 1, N_out), rng.normal(0, 1, N_out)
140	    T = p["delta_coef"] * U1 + rng.normal(0, 1, N_out)
141	    logits = (p["g"][None, :] + p["a1"][None, :] * U1[:, None]
142	              + p["a2"][None, :] * U2[:, None])
143	    A = softmax_sample(logits, rng)
144	    Y = p["tau"] * T + p["lam"] * U2 + rng.normal(0, 1, N_out)
145	    return {"T": T, "Y": Y, "A": A}
146	
147	
148	def gen_iv(N, params=None, rng=None, seed=None):
149	    """Z->A->Y, U->{A,Y}. IV topology with endogenous A.
150	
151	    Returns:
152	        dict with keys Z, Y, A
153	    """
154	    rng = _get_rng(rng, seed)
155	    p = _get_params("iv", params)
156	    K = len(p["g"])
157	    Z = rng.normal(0, 1, N)
158	    U = rng.normal(0, 1, N)
159	    logits = (p["g"][None, :] + p["dZ"][None, :] * Z[:, None]
160	              + p["dU"][None, :] * U[:, None])
161	    A = softmax_sample(logits, rng)
162	    D = make_dummies(A, K)
163	    Y = p["beta"][0] + D @ p["beta"][1:] + p["lam"] * U + rng.normal(0, 1, N)
164	    return {"Z": Z, "Y": Y, "A": A}
165	
166	
167	def gen_frontdoor(N, params=None, rng=None, seed=None):
168	    """T->M->Y, U->{T,Y}. Misclassified variable is M (mediator, stored as A).
169	
170	    Returns:
171	        dict with keys T, Y, A (A is the mediator M)
172	    """
173	    rng = _get_rng(rng, seed)
174	    p = _get_params("frontdoor", params)
175	    U = rng.normal(0, 1, N)
176	    T = p["alpha_U"] * U + rng.normal(0, 1, N)
177	    K = len(p["gamma"])
178	    logits = p["gamma"][None, :] + p["delta"][None, :] * T[:, None]
179	    A = softmax_sample(logits, rng)
180	    D = make_dummies(A, K)
181	    Y = p["beta"][0] + D @ p["beta"][1:] + p["lam_U"] * U + rng.normal(0, 1, N)
182	    return {"T": T, "Y": Y, "A": A}
183	
184	
185	GEN_FUNCS = {
186	    "confounding": gen_confounding,
187	    "mediation": gen_mediation,
188	    "collider": gen_collider,
189	    "exposure": gen_exposure,
190	    "mbias": gen_mbias,
191	    "iv": gen_iv,
192	    "frontdoor": gen_frontdoor,
193	}
194	
195	
196	def generate_data(topology, N, params=None, rng=None, seed=None):
197	    """Generate synthetic data for a given topology.
198	
199	    Args:
200	        topology: one of "confounding", "mediation", "collider", "exposure",
201	                  "mbias", "iv", "frontdoor"
202	        N: sample size
203	        params: optional DGP parameter overrides
204	        rng: numpy random Generator
205	        seed: random seed (used if rng is None)
206	
207	    Returns:
208	        dict with generated variables (topology-dependent keys)
209	    """
210	    if topology not in GEN_FUNCS:
211	        raise ValueError(f"Unknown topology: {topology}. Choose from {TOPOLOGIES}")
212	    return GEN_FUNCS[topology](N, params=params, rng=rng, seed=seed)
213	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71959910-e9fa-4c60-ba97-43b9b044202d",
  "isSidechain": false,
  "promptId": "931f36b2-6e79-486e-89c9-9074426aeee2",
  "type": "user",
  "uuid": "bf542fe3-e3cb-495a-ac2e-48d939ea1a03",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/dgp.py",
      "content": "\"\"\"Data generation processes for 7 DAG topologies.\n\nEach topology generates synthetic data with a known causal structure.\nThe variable A (or M for frontdoor) is the one subject to misclassification.\n\"\"\"\n\nimport numpy as np\nfrom .utils import softmax_sample, make_dummies\n\nDEFAULT_PARAMS = {\n    \"confounding\": dict(\n        p_A=np.array([0.40, 0.35, 0.25]),\n        alpha=np.array([1.5, -1.0]),\n        beta_A=np.array([1.0, -0.5]),\n        beta_T=2.0, sigma_T=1.0),\n    \"mediation\": dict(\n        tau=0.5,\n        gamma=np.array([0.0, 0.5, -0.3]),\n        delta=np.array([0.0, 0.8, -0.6]),\n        beta=np.array([0.0, 1.0, -0.5])),\n    \"collider\": dict(\n        tau=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        dT=np.array([0.0, 0.5, -0.3]),\n        dY=np.array([0.0, 0.8, 0.6])),\n    \"exposure\": dict(\n        beta=np.array([0.0, 1.0, -0.5]),\n        p_A=np.array([0.40, 0.35, 0.25])),\n    \"mbias\": dict(\n        tau=1.0, delta_coef=1.0, lam=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        a1=np.array([0.0, 0.8, -0.5]),\n        a2=np.array([0.0, 0.6, 0.9])),\n    \"iv\": dict(\n        lam=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        dZ=np.array([0.0, 1.0, -0.5]),\n        dU=np.array([0.0, 0.8, 0.6]),\n        beta=np.array([0.0, 1.0, -0.5])),\n    \"frontdoor\": dict(\n        alpha_U=1.0, lam_U=1.0,\n        gamma=np.array([0.0, 0.5, -0.3]),\n        delta=np.array([0.0, 1.0, -0.8]),\n        beta=np.array([0.0, 1.0, -0.5])),\n}\n\nTOPOLOGIES = list(DEFAULT_PARAMS.keys())\n\nHAS_TREATMENT = {\"confounding\", \"mediation\", \"collider\", \"mbias\", \"frontdoor\"}\nNO_TREATMENT = {\"exposure\", \"iv\"}\n\n\ndef _get_rng(rng, seed):\n    if rng is not None:\n        return rng\n    return np.random.default_rng(seed)\n\n\ndef _get_params(topology, params):\n    p = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        p.update(params)\n    return p\n\n\ndef gen_confounding(N, params=None, rng=None, seed=None):\n    \"\"\"A->T, A->Y, T->Y. Researcher controls for A*.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"confounding\", params)\n    K = len(p[\"p_A\"])\n    A = rng.choice(K, size=N, p=p[\"p_A\"])\n    D = make_dummies(A, K)\n    T = D @ p[\"alpha\"] + rng.normal(0, p[\"sigma_T\"], N)\n    Y = p[\"beta_T\"] * T + D @ p[\"beta_A\"] + rng.normal(0, 1, N)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_mediation(N, params=None, rng=None, seed=None):\n    \"\"\"T->A->Y. A mediates; researcher controls for A*.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"mediation\", params)\n    T = rng.binomial(1, 0.5, N).astype(float)\n    K = len(p[\"gamma\"])\n    logits = p[\"gamma\"][None, :] + p[\"delta\"][None, :] * T[:, None]\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"tau\"] * T + rng.normal(0, 1, N)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_collider(N, params=None, rng=None, seed=None):\n    \"\"\"T->A<-Y. Researcher wrongly controls for A*.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"collider\", params)\n    T = rng.normal(0, 1, N)\n    Y = p[\"tau\"] * T + rng.normal(0, 1, N)\n    logits = (p[\"g\"][None, :] + p[\"dT\"][None, :] * T[:, None]\n              + p[\"dY\"][None, :] * Y[:, None])\n    A = softmax_sample(logits, rng)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_exposure(N, params=None, rng=None, seed=None):\n    \"\"\"A->Y (direct exposure, no treatment T).\n\n    Returns:\n        dict with keys Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"exposure\", params)\n    K = len(p[\"p_A\"])\n    A = rng.choice(K, size=N, p=p[\"p_A\"])\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + rng.normal(0, 1, N)\n    return {\"Y\": Y, \"A\": A}\n\n\ndef gen_mbias(N, params=None, rng=None, seed=None):\n    \"\"\"U1->{A,T}, U2->{A,Y}, T->Y. Conditioning on A* induces M-bias.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"mbias\", params)\n    N_out = N\n    U1, U2 = rng.normal(0, 1, N_out), rng.normal(0, 1, N_out)\n    T = p[\"delta_coef\"] * U1 + rng.normal(0, 1, N_out)\n    logits = (p[\"g\"][None, :] + p[\"a1\"][None, :] * U1[:, None]\n              + p[\"a2\"][None, :] * U2[:, None])\n    A = softmax_sample(logits, rng)\n    Y = p[\"tau\"] * T + p[\"lam\"] * U2 + rng.normal(0, 1, N_out)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_iv(N, params=None, rng=None, seed=None):\n    \"\"\"Z->A->Y, U->{A,Y}. IV topology with endogenous A.\n\n    Returns:\n        dict with keys Z, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"iv\", params)\n    K = len(p[\"g\"])\n    Z = rng.normal(0, 1, N)\n    U = rng.normal(0, 1, N)\n    logits = (p[\"g\"][None, :] + p[\"dZ\"][None, :] * Z[:, None]\n              + p[\"dU\"][None, :] * U[:, None])\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"lam\"] * U + rng.normal(0, 1, N)\n    return {\"Z\": Z, \"Y\": Y, \"A\": A}\n\n\ndef gen_frontdoor(N, params=None, rng=None, seed=None):\n    \"\"\"T->M->Y, U->{T,Y}. Misclassified variable is M (mediator, stored as A).\n\n    Returns:\n        dict with keys T, Y, A (A is the mediator M)\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"frontdoor\", params)\n    U = rng.normal(0, 1, N)\n    T = p[\"alpha_U\"] * U + rng.normal(0, 1, N)\n    K = len(p[\"gamma\"])\n    logits = p[\"gamma\"][None, :] + p[\"delta\"][None, :] * T[:, None]\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"lam_U\"] * U + rng.normal(0, 1, N)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\nGEN_FUNCS = {\n    \"confounding\": gen_confounding,\n    \"mediation\": gen_mediation,\n    \"collider\": gen_collider,\n    \"exposure\": gen_exposure,\n    \"mbias\": gen_mbias,\n    \"iv\": gen_iv,\n    \"frontdoor\": gen_frontdoor,\n}\n\n\ndef generate_data(topology, N, params=None, rng=None, seed=None):\n    \"\"\"Generate synthetic data for a given topology.\n\n    Args:\n        topology: one of \"confounding\", \"mediation\", \"collider\", \"exposure\",\n                  \"mbias\", \"iv\", \"frontdoor\"\n        N: sample size\n        params: optional DGP parameter overrides\n        rng: numpy random Generator\n        seed: random seed (used if rng is None)\n\n    Returns:\n        dict with generated variables (topology-dependent keys)\n    \"\"\"\n    if topology not in GEN_FUNCS:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    return GEN_FUNCS[topology](N, params=params, rng=rng, seed=seed)\n",
      "numLines": 213,
      "startLine": 1,
      "totalLines": 213
    }
  },
  "sourceToolAssistantUUID": "71959910-e9fa-4c60-ba97-43b9b044202d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-23T14:35:38.732Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HZghw5juYNQNtPpfS8TVQk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/confusion.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf542fe3-e3cb-495a-ac2e-48d939ea1a03",
  "isSidechain": false,
  "requestId": "req_011CbKfg7UzmXxEYXiJRtj8R",
  "type": "assistant",
  "uuid": "7f32b727-3447-4d8d-902f-e6d8ff815046",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016rerXLcjU94zeauoAzfSkR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3631,
      "cache_read_input_tokens": 26105,
      "output_tokens": 271,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 271,
          "cache_read_input_tokens": 26105,
          "cache_creation_input_tokens": 3631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3631
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

_source line 21_

```json
{
  "type": "last-prompt",
  "leafUuid": "2ac0164a-81f6-45ca-a2d2-ce01ebc304d6",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Mini end-to-end demo for causal annotation error",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4"
}
```

---

### Assistant

_source line 23 · 2026-05-23T14:35:41.636Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the APIs. Let me also quickly check the existing `e2e_demo.py` and `e2e_demo_results.json` to see what's already there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ac0164a-81f6-45ca-a2d2-ce01ebc304d6",
  "isSidechain": false,
  "requestId": "req_011CbKfh3MV8FFgYtfNTap8J",
  "type": "assistant",
  "uuid": "67a27b62-2e85-49e9-a0ce-287a70d35337",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfFR2wC5xmiFqyQP18X6JG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15234,
      "cache_read_input_tokens": 29736,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 29736,
          "cache_creation_input_tokens": 15234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15234
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

_source line 24 · 2026-05-23T14:35:42.108Z_

Let me check the existing e2e_demo files to understand what's already there.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67a27b62-2e85-49e9-a0ce-287a70d35337",
  "isSidechain": false,
  "requestId": "req_011CbKfh3MV8FFgYtfNTap8J",
  "type": "assistant",
  "uuid": "73490dbb-2500-4d84-b6ea-1befd35876b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfFR2wC5xmiFqyQP18X6JG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15234,
      "cache_read_input_tokens": 29736,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 29736,
          "cache_creation_input_tokens": 15234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15234
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

_source line 25 · 2026-05-23T14:35:44.007Z_

<details open><summary>🔧 Tool call — Read · `toolu_014BHs9xvy9LPkScXJMpQyr4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73490dbb-2500-4d84-b6ea-1befd35876b9",
  "isSidechain": false,
  "requestId": "req_011CbKfh3MV8FFgYtfNTap8J",
  "type": "assistant",
  "uuid": "1ba47348-4c94-4e3a-a15b-c571a392ad61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfFR2wC5xmiFqyQP18X6JG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15234,
      "cache_read_input_tokens": 29736,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 29736,
          "cache_creation_input_tokens": 15234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15234
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

_source line 26 · 2026-05-23T14:35:44.512Z_

<details><summary>↩ Tool result · `toolu_01CUT1jWo63RNGoNXBZGNYHh`</summary>

```text
1	"""Annotation Sensitivity Value (ASV) computation.
2	
3	ASV measures how much misclassification is needed to cross a bias threshold,
4	using the C(delta) = (1-delta)*I + delta*C0 interpolation path.
5	"""
6	
7	import numpy as np
8	from .bias import _precompute, _get_tau
9	from .confusion import validate_confusion_matrix, interpolate_confusion, delta_range
10	from .dgp import DEFAULT_PARAMS, TOPOLOGIES
11	
12	
13	def _compute_bias_curve(topology, C0, stats, K, tau_true, n_grid=1500):
14	    dmin, dmax = delta_range(C0)
15	    deltas = np.linspace(dmin, dmax, n_grid)
16	    tau_curve = np.zeros(n_grid)
17	    for i, d in enumerate(deltas):
18	        C_d = interpolate_confusion(C0, d)
19	        tau_curve[i] = _get_tau(topology, C_d, stats, K)
20	    bias_abs = np.abs(tau_curve - tau_true)
21	    return deltas, bias_abs, tau_curve
22	
23	
24	def _compute_envelope(bias_abs):
25	    env = np.zeros_like(bias_abs)
26	    running_max = 0.0
27	    for i in range(len(bias_abs)):
28	        v = bias_abs[i]
29	        if not np.isnan(v):
30	            running_max = max(running_max, v)
31	        env[i] = running_max
32	    return env
33	
34	
35	def _find_threshold_crossing(envelope, deltas, tau_curve, tau_true,
36	                             threshold_type, threshold_value):
37	    if threshold_type == "magnitude":
38	        if abs(tau_true) < 1e-12:
39	            return None
40	        thresh = threshold_value * abs(tau_true)
41	        for i in range(len(deltas)):
42	            if envelope[i] > thresh:
43	                return float(deltas[i])
44	        return None
45	    elif threshold_type == "sign_flip":
46	        if abs(tau_true) < 1e-12:
47	            return None
48	        baseline_sign = np.sign(tau_true)
49	        for i in range(len(deltas)):
50	            if np.isnan(tau_curve[i]):
51	                continue
52	            if np.sign(tau_curve[i]) != baseline_sign:
53	                return float(deltas[i])
54	        return None
55	    elif threshold_type == "significance":
56	        z_crit = 1.96
57	        for i in range(len(deltas)):
58	            if np.isnan(tau_curve[i]):
59	                continue
60	            if abs(tau_curve[i]) < z_crit * threshold_value:
61	                return float(deltas[i])
62	        return None
63	    else:
64	        raise ValueError(
65	            f"Unknown threshold_type: {threshold_type}. "
66	            f"Choose from 'magnitude', 'significance', 'sign_flip'"
67	        )
68	
69	
70	def compute_asv(topology, C0, params=None, threshold_type="magnitude",
71	                threshold_value=0.1, n_grid=1500):
72	    """Compute Annotation Sensitivity Value for a topology and base confusion matrix.
73	
74	    ASV is the minimum interpolation delta at which a bias threshold is crossed
75	    along the path C(delta) = (1-delta)*I + delta*C0.
76	
77	    Args:
78	        topology: one of 7 DAG types
79	        C0: (K, K) base confusion matrix
80	        params: optional DGP parameters dict
81	        threshold_type: "magnitude" (relative to tau_true),
82	                        "significance" (threshold_value = SE),
83	                        "sign_flip" (sign of tau changes)
84	        threshold_value: threshold parameter (meaning depends on threshold_type)
85	        n_grid: number of delta grid points
86	
87	    Returns:
88	        dict with asv, bias_curve, envelope, deltas, tau_true
89	    """
90	    if topology not in TOPOLOGIES:
91	        raise ValueError(f"Unknown topology: {topology}. Choose from {TOPOLOGIES}")
92	    if not validate_confusion_matrix(C0):
93	        raise ValueError("C0 must be a valid column-stochastic matrix")
94	
95	    K = C0.shape[0]
96	    merged = dict(DEFAULT_PARAMS[topology])
97	    if params is not None:
98	        merged.update(params)
99	
100	    stats = _precompute(topology, merged, K)
101	    tau_true = _get_tau(topology, np.eye(K), stats, K)
102	
103	    deltas, bias_abs, tau_curve = _compute_bias_curve(
104	        topology, C0, stats, K, tau_true, n_grid
105	    )
106	    envelope = _compute_envelope(bias_abs)
107	
108	    asv = _find_threshold_crossing(
109	        envelope, deltas, tau_curve, tau_true, threshold_type, threshold_value
110	    )
111	
112	    return {
113	        "asv": asv,
114	        "bias_curve": bias_abs,
115	        "envelope": envelope,
116	        "deltas": deltas,
117	        "tau_true": float(tau_true),
118	    }
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f94f5b6c-cf28-43fc-95e8-cacc946e4315",
  "isSidechain": false,
  "promptId": "931f36b2-6e79-486e-89c9-9074426aeee2",
  "type": "user",
  "uuid": "80a40833-bbb2-4756-bdbf-ac3d62e89be6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/asv.py",
      "content": "\"\"\"Annotation Sensitivity Value (ASV) computation.\n\nASV measures how much misclassification is needed to cross a bias threshold,\nusing the C(delta) = (1-delta)*I + delta*C0 interpolation path.\n\"\"\"\n\nimport numpy as np\nfrom .bias import _precompute, _get_tau\nfrom .confusion import validate_confusion_matrix, interpolate_confusion, delta_range\nfrom .dgp import DEFAULT_PARAMS, TOPOLOGIES\n\n\ndef _compute_bias_curve(topology, C0, stats, K, tau_true, n_grid=1500):\n    dmin, dmax = delta_range(C0)\n    deltas = np.linspace(dmin, dmax, n_grid)\n    tau_curve = np.zeros(n_grid)\n    for i, d in enumerate(deltas):\n        C_d = interpolate_confusion(C0, d)\n        tau_curve[i] = _get_tau(topology, C_d, stats, K)\n    bias_abs = np.abs(tau_curve - tau_true)\n    return deltas, bias_abs, tau_curve\n\n\ndef _compute_envelope(bias_abs):\n    env = np.zeros_like(bias_abs)\n    running_max = 0.0\n    for i in range(len(bias_abs)):\n        v = bias_abs[i]\n        if not np.isnan(v):\n            running_max = max(running_max, v)\n        env[i] = running_max\n    return env\n\n\ndef _find_threshold_crossing(envelope, deltas, tau_curve, tau_true,\n                             threshold_type, threshold_value):\n    if threshold_type == \"magnitude\":\n        if abs(tau_true) < 1e-12:\n            return None\n        thresh = threshold_value * abs(tau_true)\n        for i in range(len(deltas)):\n            if envelope[i] > thresh:\n                return float(deltas[i])\n        return None\n    elif threshold_type == \"sign_flip\":\n        if abs(tau_true) < 1e-12:\n            return None\n        baseline_sign = np.sign(tau_true)\n        for i in range(len(deltas)):\n            if np.isnan(tau_curve[i]):\n                continue\n            if np.sign(tau_curve[i]) != baseline_sign:\n                return float(deltas[i])\n        return None\n    elif threshold_type == \"significance\":\n        z_crit = 1.96\n        for i in range(len(deltas)):\n            if np.isnan(tau_curve[i]):\n                continue\n            if abs(tau_curve[i]) < z_crit * threshold_value:\n                return float(deltas[i])\n        return None\n    else:\n        raise ValueError(\n            f\"Unknown threshold_type: {threshold_type}. \"\n            f\"Choose from 'magnitude', 'significance', 'sign_flip'\"\n        )\n\n\ndef compute_asv(topology, C0, params=None, threshold_type=\"magnitude\",\n                threshold_value=0.1, n_grid=1500):\n    \"\"\"Compute Annotation Sensitivity Value for a topology and base confusion matrix.\n\n    ASV is the minimum interpolation delta at which a bias threshold is crossed\n    along the path C(delta) = (1-delta)*I + delta*C0.\n\n    Args:\n        topology: one of 7 DAG types\n        C0: (K, K) base confusion matrix\n        params: optional DGP parameters dict\n        threshold_type: \"magnitude\" (relative to tau_true),\n                        \"significance\" (threshold_value = SE),\n                        \"sign_flip\" (sign of tau changes)\n        threshold_value: threshold parameter (meaning depends on threshold_type)\n        n_grid: number of delta grid points\n\n    Returns:\n        dict with asv, bias_curve, envelope, deltas, tau_true\n    \"\"\"\n    if topology not in TOPOLOGIES:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    if not validate_confusion_matrix(C0):\n        raise ValueError(\"C0 must be a valid column-stochastic matrix\")\n\n    K = C0.shape[0]\n    merged = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        merged.update(params)\n\n    stats = _precompute(topology, merged, K)\n    tau_true = _get_tau(topology, np.eye(K), stats, K)\n\n    deltas, bias_abs, tau_curve = _compute_bias_curve(\n        topology, C0, stats, K, tau_true, n_grid\n    )\n    envelope = _compute_envelope(bias_abs)\n\n    asv = _find_threshold_crossing(\n        envelope, deltas, tau_curve, tau_true, threshold_type, threshold_value\n    )\n\n    return {\n        \"asv\": asv,\n        \"bias_curve\": bias_abs,\n        \"envelope\": envelope,\n        \"deltas\": deltas,\n        \"tau_true\": float(tau_true),\n    }\n",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  },
  "sourceToolAssistantUUID": "f94f5b6c-cf28-43fc-95e8-cacc946e4315",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-23T14:35:44.011Z_

<details><summary>↩ Tool result · `toolu_014BHs9xvy9LPkScXJMpQyr4`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Mini end-to-end demo: C estimation -> ASV diagnostic -> Algorithm 1 routing
4	-> correction -> bias improvement.
5	
6	Two topologies illustrate the dichotomy:
7	  - confounding: FWL invariance => no plug-in correction helps the
8	    treatment coefficient; routed method is "no correction".
9	  - exposure: PPI++ recovers the target coefficient using a gold subset.
10	
11	Pipeline for each topology:
12	  1. Generate synthetic data with N=10000, K=3, known C0 (diag=0.7,
13	     off-diagonal 0.15 uniform).
14	  2. Sample 20% gold subset; estimate C_hat from gold (true vs. observed labels).
15	  3. Compute ASV (magnitude & sign-flip) using C_hat as the base of the
16	     interpolation path C(delta) = (1-delta) I + delta C_hat.
17	  4. Algorithm 1 route:
18	       - confounding => "no correction (FWL)"
19	       - exposure    => "PPI++"
20	  5. Apply correction(s); also run naive_plugin / MLA on confounding to
21	     verify they do not move the treatment coefficient (FWL theorem).
22	  6. Record naive bias, corrected bias, improvement.
23	
24	100 Monte Carlo replicates per topology (mean +/- std).
25	
26	Outputs:
27	  - artifacts/e2e_demo_results.json
28	  - artifacts/e2e_demo_table.tex
29	"""
30	
31	import json
32	import os
33	import sys
34	import time
35	
36	import numpy as np
37	
38	PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
39	sys.path.insert(0, PROJECT_ROOT)
40	
41	from annot_sensitivity.asv import compute_asv
42	from annot_sensitivity.correction import (
43	    correct_mla,
44	    correct_naive_plugin,
45	    correct_ppi,
46	)
47	from annot_sensitivity.dgp import gen_confounding, gen_exposure
48	from annot_sensitivity.utils import make_dummies, misclassify, ols_with_se
49	
50	SEED = 42
51	N = 10_000
52	K = 3
53	GOLD_FRACTION = 0.20
54	N_REPS = 100
55	
56	C0 = np.array([
57	    [0.70, 0.15, 0.15],
58	    [0.15, 0.70, 0.15],
59	    [0.15, 0.15, 0.70],
60	])
61	
62	CONFOUNDING_PARAMS = {
63	    "p_A": np.array([0.40, 0.35, 0.25]),
64	    "alpha": np.array([0.6, -0.3]),
65	    "beta_A": np.array([0.8, -0.4]),
66	    "beta_T": 0.5,
67	    "sigma_T": 1.0,
68	}
69	
70	EXPOSURE_PARAMS = {
71	    "p_A": np.array([0.40, 0.35, 0.25]),
72	    "beta": np.array([0.0, 1.0, -0.5]),
73	}
74	
75	
76	def estimate_C(A_true_gold, A_star_gold, K):
77	    """Column-stochastic Cˆ[j,k] = P(A* = j | A = k) from gold labels."""
78	    C_hat = np.zeros((K, K))
79	    for k in range(K):
80	        mask = A_true_gold == k
81	        if mask.sum() > 0:
82	            for j in range(K):
83	                C_hat[j, k] = (A_star_gold[mask] == j).sum() / mask.sum()
84	        else:
85	            C_hat[k, k] = 1.0
86	    return C_hat
87	
88	
89	def naive_confounding(X_other, Y, Astar, K, tau_idx=1):
90	    D = make_dummies(Astar, K)
91	    X = np.column_stack([X_other, D])
92	    beta, se = ols_with_se(X, Y)
93	    return float(beta[tau_idx]), float(se[tau_idx])
94	
95	
96	def naive_exposure(Y, Astar, K, tau_idx=1):
97	    N_ = len(Y)
98	    X_other = np.ones((N_, 1))
99	    D = make_dummies(Astar, K)
100	    X = np.column_stack([X_other, D])
101	    beta, se = ols_with_se(X, Y)
102	    return float(beta[tau_idx]), float(se[tau_idx])
103	
104	
105	def run_confounding_rep(rng, tau_true):
106	    data = gen_confounding(N, params=CONFOUNDING_PARAMS, rng=rng)
107	    T, Y, A = data["T"], data["Y"], data["A"]
108	    Astar = misclassify(A, C0, rng)
109	
110	    gold_idx = rng.choice(N, size=int(N * GOLD_FRACTION), replace=False)
111	    gold_mask = np.zeros(N, dtype=bool)
112	    gold_mask[gold_idx] = True
113	    C_hat = estimate_C(A[gold_mask], Astar[gold_mask], K)
114	
115	    X_other = np.column_stack([np.ones(N), T])
116	
117	    tau_naive, _ = naive_confounding(X_other, Y, Astar, K, tau_idx=1)
118	    tau_np, _, ok_np = correct_naive_plugin(X_other, Y, Astar, C_hat, tau_idx=1)
119	    tau_mla, _, ok_mla = correct_mla(X_other, Y, Astar, C_hat, tau_idx=1)
120	
121	    return {
122	        "tau_naive": tau_naive,
123	        "tau_np": tau_np if ok_np else np.nan,
124	        "tau_mla": tau_mla if ok_mla else np.nan,
125	        "C_hat": C_hat,
126	        "tau_true": tau_true,
127	    }
128	
129	
130	def run_exposure_rep(rng, tau_true):
131	    data = gen_exposure(N, params=EXPOSURE_PARAMS, rng=rng)
132	    Y, A = data["Y"], data["A"]
133	    Astar = misclassify(A, C0, rng)
134	
135	    gold_idx = rng.choice(N, size=int(N * GOLD_FRACTION), replace=False)
136	    gold_mask = np.zeros(N, dtype=bool)
137	    gold_mask[gold_idx] = True
138	    C_hat = estimate_C(A[gold_mask], Astar[gold_mask], K)
139	
140	    X_other = np.ones((N, 1))
141	    tau_naive, _ = naive_exposure(Y, Astar, K, tau_idx=1)
142	    tau_ppi, _, ok_ppi = correct_ppi(X_other, Y, Astar, A, gold_mask,
143	                                     tau_idx=1, rng=rng)
144	
145	    return {
146	        "tau_naive": tau_naive,
147	        "tau_ppi": tau_ppi if ok_ppi else np.nan,
148	        "C_hat": C_hat,
149	        "tau_true": tau_true,
150	    }
151	
152	
153	def compute_summary(reps, method_keys, tau_true):
154	    out = {"tau_true": float(tau_true)}
155	    naive = np.array([r["tau_naive"] for r in reps])
156	    naive_bias = naive - tau_true
157	    naive_bias_pct = 100.0 * naive_bias / tau_true
158	    out["naive"] = {
159	        "mean": float(naive.mean()),
160	        "std": float(naive.std(ddof=1)),
161	        "bias_mean": float(naive_bias.mean()),
162	        "bias_std": float(naive_bias.std(ddof=1)),
163	        "abs_bias_mean": float(np.mean(np.abs(naive_bias))),
164	        "bias_pct_mean": float(naive_bias_pct.mean()),
165	        "bias_pct_std": float(naive_bias_pct.std(ddof=1)),
166	    }
167	    out["methods"] = {}
168	    naive_abs = np.mean(np.abs(naive_bias))
169	    for key in method_keys:
170	        vals = np.array([r[key] for r in reps])
171	        valid = np.isfinite(vals)
172	        if valid.sum() == 0:
173	            out["methods"][key] = None
174	            continue
175	        v = vals[valid]
176	        bias = v - tau_true
177	        bias_pct = 100.0 * bias / tau_true
178	        abs_bias_mean = float(np.mean(np.abs(bias)))
179	        improvement_pct = (
180	            100.0 * (1.0 - abs_bias_mean / naive_abs)
181	            if naive_abs > 1e-12 else float("nan")
182	        )
183	        out["methods"][key] = {
184	            "mean": float(v.mean()),
185	            "std": float(v.std(ddof=1)),
186	            "bias_mean": float(bias.mean()),
187	            "bias_std": float(bias.std(ddof=1)),
188	            "abs_bias_mean": abs_bias_mean,
189	            "bias_pct_mean": float(bias_pct.mean()),
190	            "bias_pct_std": float(bias_pct.std(ddof=1)),
191	            "improvement_pct": float(improvement_pct),
192	            "n_valid": int(valid.sum()),
193	        }
194	    return out
195	
196	
197	def mean_C_hat(reps):
198	    return np.mean(np.stack([r["C_hat"] for r in reps]), axis=0)
199	
200	
201	def main():
202	    t0 = time.time()
203	    print("=" * 70)
204	    print(f"Mini E2E demo: N={N}, K={K}, gold={int(N * GOLD_FRACTION)}, reps={N_REPS}")
205	    print(f"C0 diag={C0.diagonal().tolist()}")
206	    print("=" * 70)
207	
208	    rng_master = np.random.default_rng(SEED)
209	
210	    print("\n[Confounding] target = treatment coefficient tau = 0.5")
211	    tau_true_conf = CONFOUNDING_PARAMS["beta_T"]
212	    conf_reps = []
213	    for rep in range(N_REPS):
214	        seed_rep = int(rng_master.integers(0, 2**31))
215	        rng_rep = np.random.default_rng(seed_rep)
216	        conf_reps.append(run_confounding_rep(rng_rep, tau_true_conf))
217	        if (rep + 1) % 25 == 0:
218	            print(f"  rep {rep + 1}/{N_REPS}")
219	
220	    print("\n[Exposure] target = beta_1 = 1.0")
221	    tau_true_exp = EXPOSURE_PARAMS["beta"][1]
222	    exp_reps = []
223	    for rep in range(N_REPS):
224	        seed_rep = int(rng_master.integers(0, 2**31))
225	        rng_rep = np.random.default_rng(seed_rep)
226	        exp_reps.append(run_exposure_rep(rng_rep, tau_true_exp))
227	        if (rep + 1) % 25 == 0:
228	            print(f"  rep {rep + 1}/{N_REPS}")
229	
230	    conf_summary = compute_summary(
231	        conf_reps,
232	        method_keys=["tau_np", "tau_mla"],
233	        tau_true=tau_true_conf,
234	    )
235	    exp_summary = compute_summary(
236	        exp_reps,
237	        method_keys=["tau_ppi"],
238	        tau_true=tau_true_exp,
239	    )
240	
241	    C_hat_conf_mean = mean_C_hat(conf_reps)
242	    C_hat_exp_mean = mean_C_hat(exp_reps)
243	
244	    print("\n[ASV] computing magnitude & sign-flip thresholds with mean Cˆ...")
245	    asv_conf_mag = compute_asv(
246	        "confounding", C_hat_conf_mean, params=CONFOUNDING_PARAMS,
247	        threshold_type="magnitude", threshold_value=0.10,
248	    )
249	    asv_conf_sign = compute_asv(
250	        "confounding", C_hat_conf_mean, params=CONFOUNDING_PARAMS,
251	        threshold_type="sign_flip",
252	    )
253	    asv_exp_mag = compute_asv(
254	        "exposure", C_hat_exp_mean, params=EXPOSURE_PARAMS,
255	        threshold_type="magnitude", threshold_value=0.10,
256	    )
257	    asv_exp_sign = compute_asv(
258	        "exposure", C_hat_exp_mean, params=EXPOSURE_PARAMS,
259	        threshold_type="sign_flip",
260	    )
261	
262	    output = {
263	        "meta": {
264	            "seed": SEED,
265	            "N": N,
266	            "K": K,
267	            "gold_fraction": GOLD_FRACTION,
268	            "n_reps": N_REPS,
269	            "C0": C0.tolist(),
270	            "confounding_params": {
271	                k: (v.tolist() if isinstance(v, np.ndarray) else v)
272	                for k, v in CONFOUNDING_PARAMS.items()
273	            },
274	            "exposure_params": {
275	                k: (v.tolist() if isinstance(v, np.ndarray) else v)
276	                for k, v in EXPOSURE_PARAMS.items()
277	            },
278	        },
279	        "confounding": {
280	            **conf_summary,
281	            "routed_method": "no correction (FWL invariance)",
282	            "C_hat_mean": C_hat_conf_mean.tolist(),
283	            "asv_magnitude": asv_conf_mag["asv"],
284	            "asv_signflip": asv_conf_sign["asv"],
285	            "asv_tau_true_theoretical": asv_conf_mag["tau_true"],
286	        },
287	        "exposure": {
288	            **exp_summary,
289	            "routed_method": "PPI++",
290	            "C_hat_mean": C_hat_exp_mean.tolist(),
291	            "asv_magnitude": asv_exp_mag["asv"],
292	            "asv_signflip": asv_exp_sign["asv"],
293	            "asv_tau_true_theoretical": asv_exp_mag["tau_true"],
294	        },
295	    }
296	
297	    out_json = os.path.join(PROJECT_ROOT, "artifacts", "e2e_demo_results.json")
298	    with open(out_json, "w") as f:
299	        json.dump(output, f, indent=2)
300	    print(f"\nWrote {out_json}")
301	
302	    write_latex_table(output)
303	
304	    print_console_summary(output)
305	
306	    print(f"\nElapsed: {time.time() - t0:.1f}s")
307	
308	
309	def _fmt_asv(v):
310	    return f"{v:.3f}" if v is not None else "no crossing"
311	
312	
313	def _fmt_pct(mean, std):
314	    if not np.isfinite(mean):
315	        return "--"
316	    return f"{mean:+.2f} $\\pm$ {std:.2f}"
317	
318	
319	def write_latex_table(out):
320	    conf = out["confounding"]
321	    exp = out["exposure"]
322	
323	    conf_naive = conf["naive"]
324	    conf_np = conf["methods"]["tau_np"]
325	    conf_mla = conf["methods"]["tau_mla"]
326	    exp_naive = exp["naive"]
327	    exp_ppi = exp["methods"]["tau_ppi"]
328	
329	    def _improve(m):
330	        if m is None or not np.isfinite(m["improvement_pct"]):
331	            return "--"
332	        return f"{m['improvement_pct']:+.1f}\\%"
333	
334	    def _bias_cell(m):
335	        if m is None:
336	            return "--"
337	        return _fmt_pct(m["bias_pct_mean"], m["bias_pct_std"])
338	
339	    lines = []
340	    lines.append("% Auto-generated by artifacts/e2e_demo.py")
341	    lines.append("\\begin{table}[t]")
342	    lines.append("\\centering")
343	    lines.append("\\small")
344	    lines.append("\\begin{tabular}{lrrlrr}")
345	    lines.append("\\toprule")
346	    lines.append(
347	        "Topology & Naive Bias (\\%) & ASV $\\delta^*_{\\mathrm{mag}}$ & "
348	        "Routed Method & Corrected Bias (\\%) & Improvement (\\%) \\\\"
349	    )
350	    lines.append("\\midrule")
351	
352	    lines.append(
353	        "Confounding & "
354	        f"{_fmt_pct(conf_naive['bias_pct_mean'], conf_naive['bias_pct_std'])} & "
355	        f"{_fmt_asv(conf['asv_magnitude'])} & "
356	        "no correction (FWL) & "
357	        f"{_bias_cell(conf_np)} & {_improve(conf_np)} \\\\"
358	    )
359	    lines.append(
360	        "\\quad (naive plug-in) & -- & -- & -- & "
361	        f"{_bias_cell(conf_np)} & {_improve(conf_np)} \\\\"
362	    )
363	    lines.append(
364	        "\\quad (MLA)          & -- & -- & -- & "
365	        f"{_bias_cell(conf_mla)} & {_improve(conf_mla)} \\\\"
366	    )
367	
368	    lines.append(
369	        "Exposure & "
370	        f"{_fmt_pct(exp_naive['bias_pct_mean'], exp_naive['bias_pct_std'])} & "
371	        f"{_fmt_asv(exp['asv_magnitude'])} & "
372	        "PPI++ & "
373	        f"{_bias_cell(exp_ppi)} & {_improve(exp_ppi)} \\\\"
374	    )
375	    lines.append("\\bottomrule")
376	    lines.append("\\end{tabular}")
377	    lines.append(
378	        "\\caption{End-to-end demo over "
379	        f"{out['meta']['n_reps']} replicates "
380	        f"(N={out['meta']['N']:,}, K={out['meta']['K']}, "
381	        f"{int(out['meta']['gold_fraction']*100)}\\% gold). "
382	        "Confounding: plug-in corrections leave the treatment coefficient "
383	        "unchanged (FWL invariance), so Algorithm~1 routes to ``no correction''. "
384	        "Exposure: PPI++ recovers the target coefficient using the gold subset."
385	        "}"
386	    )
387	    lines.append("\\label{tab:e2e-demo}")
388	    lines.append("\\end{table}")
389	
390	    out_tex = os.path.join(PROJECT_ROOT, "artifacts", "e2e_demo_table.tex")
391	    with open(out_tex, "w") as f:
392	        f.write("\n".join(lines) + "\n")
393	    print(f"Wrote {out_tex}")
394	
395	
396	def print_console_summary(out):
397	    print("\n" + "=" * 70)
398	    print("SUMMARY")
399	    print("=" * 70)
400	    for topo in ("confounding", "exposure"):
401	        s = out[topo]
402	        print(f"\n[{topo}]  tau_true (empirical) = {s['tau_true']:.4f}")
403	        print(f"  routed = {s['routed_method']}")
404	        nb = s["naive"]
405	        print(
406	            f"  naive       : tau = {nb['mean']:.4f} +/- {nb['std']:.4f}  "
407	            f"bias = {nb['bias_pct_mean']:+.2f}% +/- {nb['bias_pct_std']:.2f}%"
408	        )
409	        for key, m in s["methods"].items():
410	            if m is None:
411	                print(f"  {key:11s}: N/A")
412	                continue
413	            print(
414	                f"  {key:11s}: tau = {m['mean']:.4f} +/- {m['std']:.4f}  "
415	                f"bias = {m['bias_pct_mean']:+.2f}% +/- {m['bias_pct_std']:.2f}%  "
416	                f"improvement = {m['improvement_pct']:+.1f}%"
417	            )
418	        print(
419	            f"  ASV magnitude (10%) : {_fmt_asv(s['asv_magnitude'])}  |  "
420	            f"ASV sign-flip : {_fmt_asv(s['asv_signflip'])}"
421	        )
422	
423	
424	if __name__ == "__main__":
425	    main()
426	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ba47348-4c94-4e3a-a15b-c571a392ad61",
  "isSidechain": false,
  "promptId": "931f36b2-6e79-486e-89c9-9074426aeee2",
  "type": "user",
  "uuid": "e0b2f93c-90d4-497f-b2f9-ad42a2855f6a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nMini end-to-end demo: C estimation -> ASV diagnostic -> Algorithm 1 routing\n-> correction -> bias improvement.\n\nTwo topologies illustrate the dichotomy:\n  - confounding: FWL invariance => no plug-in correction helps the\n    treatment coefficient; routed method is \"no correction\".\n  - exposure: PPI++ recovers the target coefficient using a gold subset.\n\nPipeline for each topology:\n  1. Generate synthetic data with N=10000, K=3, known C0 (diag=0.7,\n     off-diagonal 0.15 uniform).\n  2. Sample 20% gold subset; estimate C_hat from gold (true vs. observed labels).\n  3. Compute ASV (magnitude & sign-flip) using C_hat as the base of the\n     interpolation path C(delta) = (1-delta) I + delta C_hat.\n  4. Algorithm 1 route:\n       - confounding => \"no correction (FWL)\"\n       - exposure    => \"PPI++\"\n  5. Apply correction(s); also run naive_plugin / MLA on confounding to\n     verify they do not move the treatment coefficient (FWL theorem).\n  6. Record naive bias, corrected bias, improvement.\n\n100 Monte Carlo replicates per topology (mean +/- std).\n\nOutputs:\n  - artifacts/e2e_demo_results.json\n  - artifacts/e2e_demo_table.tex\n\"\"\"\n\nimport json\nimport os\nimport sys\nimport time\n\nimport numpy as np\n\nPROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nsys.path.insert(0, PROJECT_ROOT)\n\nfrom annot_sensitivity.asv import compute_asv\nfrom annot_sensitivity.correction import (\n    correct_mla,\n    correct_naive_plugin,\n    correct_ppi,\n)\nfrom annot_sensitivity.dgp import gen_confounding, gen_exposure\nfrom annot_sensitivity.utils import make_dummies, misclassify, ols_with_se\n\nSEED = 42\nN = 10_000\nK = 3\nGOLD_FRACTION = 0.20\nN_REPS = 100\n\nC0 = np.array([\n    [0.70, 0.15, 0.15],\n    [0.15, 0.70, 0.15],\n    [0.15, 0.15, 0.70],\n])\n\nCONFOUNDING_PARAMS = {\n    \"p_A\": np.array([0.40, 0.35, 0.25]),\n    \"alpha\": np.array([0.6, -0.3]),\n    \"beta_A\": np.array([0.8, -0.4]),\n    \"beta_T\": 0.5,\n    \"sigma_T\": 1.0,\n}\n\nEXPOSURE_PARAMS = {\n    \"p_A\": np.array([0.40, 0.35, 0.25]),\n    \"beta\": np.array([0.0, 1.0, -0.5]),\n}\n\n\ndef estimate_C(A_true_gold, A_star_gold, K):\n    \"\"\"Column-stochastic Cˆ[j,k] = P(A* = j | A = k) from gold labels.\"\"\"\n    C_hat = np.zeros((K, K))\n    for k in range(K):\n        mask = A_true_gold == k\n        if mask.sum() > 0:\n            for j in range(K):\n                C_hat[j, k] = (A_star_gold[mask] == j).sum() / mask.sum()\n        else:\n            C_hat[k, k] = 1.0\n    return C_hat\n\n\ndef naive_confounding(X_other, Y, Astar, K, tau_idx=1):\n    D = make_dummies(Astar, K)\n    X = np.column_stack([X_other, D])\n    beta, se = ols_with_se(X, Y)\n    return float(beta[tau_idx]), float(se[tau_idx])\n\n\ndef naive_exposure(Y, Astar, K, tau_idx=1):\n    N_ = len(Y)\n    X_other = np.ones((N_, 1))\n    D = make_dummies(Astar, K)\n    X = np.column_stack([X_other, D])\n    beta, se = ols_with_se(X, Y)\n    return float(beta[tau_idx]), float(se[tau_idx])\n\n\ndef run_confounding_rep(rng, tau_true):\n    data = gen_confounding(N, params=CONFOUNDING_PARAMS, rng=rng)\n    T, Y, A = data[\"T\"], data[\"Y\"], data[\"A\"]\n    Astar = misclassify(A, C0, rng)\n\n    gold_idx = rng.choice(N, size=int(N * GOLD_FRACTION), replace=False)\n    gold_mask = np.zeros(N, dtype=bool)\n    gold_mask[gold_idx] = True\n    C_hat = estimate_C(A[gold_mask], Astar[gold_mask], K)\n\n    X_other = np.column_stack([np.ones(N), T])\n\n    tau_naive, _ = naive_confounding(X_other, Y, Astar, K, tau_idx=1)\n    tau_np, _, ok_np = correct_naive_plugin(X_other, Y, Astar, C_hat, tau_idx=1)\n    tau_mla, _, ok_mla = correct_mla(X_other, Y, Astar, C_hat, tau_idx=1)\n\n    return {\n        \"tau_naive\": tau_naive,\n        \"tau_np\": tau_np if ok_np else np.nan,\n        \"tau_mla\": tau_mla if ok_mla else np.nan,\n        \"C_hat\": C_hat,\n        \"tau_true\": tau_true,\n    }\n\n\ndef run_exposure_rep(rng, tau_true):\n    data = gen_exposure(N, params=EXPOSURE_PARAMS, rng=rng)\n    Y, A = data[\"Y\"], data[\"A\"]\n    Astar = misclassify(A, C0, rng)\n\n    gold_idx = rng.choice(N, size=int(N * GOLD_FRACTION), replace=False)\n    gold_mask = np.zeros(N, dtype=bool)\n    gold_mask[gold_idx] = True\n    C_hat = estimate_C(A[gold_mask], Astar[gold_mask], K)\n\n    X_other = np.ones((N, 1))\n    tau_naive, _ = naive_exposure(Y, Astar, K, tau_idx=1)\n    tau_ppi, _, ok_ppi = correct_ppi(X_other, Y, Astar, A, gold_mask,\n                                     tau_idx=1, rng=rng)\n\n    return {\n        \"tau_naive\": tau_naive,\n        \"tau_ppi\": tau_ppi if ok_ppi else np.nan,\n        \"C_hat\": C_hat,\n        \"tau_true\": tau_true,\n    }\n\n\ndef compute_summary(reps, method_keys, tau_true):\n    out = {\"tau_true\": float(tau_true)}\n    naive = np.array([r[\"tau_naive\"] for r in reps])\n    naive_bias = naive - tau_true\n    naive_bias_pct = 100.0 * naive_bias / tau_true\n    out[\"naive\"] = {\n        \"mean\": float(naive.mean()),\n        \"std\": float(naive.std(ddof=1)),\n        \"bias_mean\": float(naive_bias.mean()),\n        \"bias_std\": float(naive_bias.std(ddof=1)),\n        \"abs_bias_mean\": float(np.mean(np.abs(naive_bias))),\n        \"bias_pct_mean\": float(naive_bias_pct.mean()),\n        \"bias_pct_std\": float(naive_bias_pct.std(ddof=1)),\n    }\n    out[\"methods\"] = {}\n    naive_abs = np.mean(np.abs(naive_bias))\n    for key in method_keys:\n        vals = np.array([r[key] for r in reps])\n        valid = np.isfinite(vals)\n        if valid.sum() == 0:\n            out[\"methods\"][key] = None\n            continue\n        v = vals[valid]\n        bias = v - tau_true\n        bias_pct = 100.0 * bias / tau_true\n        abs_bias_mean = float(np.mean(np.abs(bias)))\n        improvement_pct = (\n            100.0 * (1.0 - abs_bias_mean / naive_abs)\n            if naive_abs > 1e-12 else float(\"nan\")\n        )\n        out[\"methods\"][key] = {\n            \"mean\": float(v.mean()),\n            \"std\": float(v.std(ddof=1)),\n            \"bias_mean\": float(bias.mean()),\n            \"bias_std\": float(bias.std(ddof=1)),\n            \"abs_bias_mean\": abs_bias_mean,\n            \"bias_pct_mean\": float(bias_pct.mean()),\n            \"bias_pct_std\": float(bias_pct.std(ddof=1)),\n            \"improvement_pct\": float(improvement_pct),\n            \"n_valid\": int(valid.sum()),\n        }\n    return out\n\n\ndef mean_C_hat(reps):\n    return np.mean(np.stack([r[\"C_hat\"] for r in reps]), axis=0)\n\n\ndef main():\n    t0 = time.time()\n    print(\"=\" * 70)\n    print(f\"Mini E2E demo: N={N}, K={K}, gold={int(N * GOLD_FRACTION)}, reps={N_REPS}\")\n    print(f\"C0 diag={C0.diagonal().tolist()}\")\n    print(\"=\" * 70)\n\n    rng_master = np.random.default_rng(SEED)\n\n    print(\"\\n[Confounding] target = treatment coefficient tau = 0.5\")\n    tau_true_conf = CONFOUNDING_PARAMS[\"beta_T\"]\n    conf_reps = []\n    for rep in range(N_REPS):\n        seed_rep = int(rng_master.integers(0, 2**31))\n        rng_rep = np.random.default_rng(seed_rep)\n        conf_reps.append(run_confounding_rep(rng_rep, tau_true_conf))\n        if (rep + 1) % 25 == 0:\n            print(f\"  rep {rep + 1}/{N_REPS}\")\n\n    print(\"\\n[Exposure] target = beta_1 = 1.0\")\n    tau_true_exp = EXPOSURE_PARAMS[\"beta\"][1]\n    exp_reps = []\n    for rep in range(N_REPS):\n        seed_rep = int(rng_master.integers(0, 2**31))\n        rng_rep = np.random.default_rng(seed_rep)\n        exp_reps.append(run_exposure_rep(rng_rep, tau_true_exp))\n        if (rep + 1) % 25 == 0:\n            print(f\"  rep {rep + 1}/{N_REPS}\")\n\n    conf_summary = compute_summary(\n        conf_reps,\n        method_keys=[\"tau_np\", \"tau_mla\"],\n        tau_true=tau_true_conf,\n    )\n    exp_summary = compute_summary(\n        exp_reps,\n        method_keys=[\"tau_ppi\"],\n        tau_true=tau_true_exp,\n    )\n\n    C_hat_conf_mean = mean_C_hat(conf_reps)\n    C_hat_exp_mean = mean_C_hat(exp_reps)\n\n    print(\"\\n[ASV] computing magnitude & sign-flip thresholds with mean Cˆ...\")\n    asv_conf_mag = compute_asv(\n        \"confounding\", C_hat_conf_mean, params=CONFOUNDING_PARAMS,\n        threshold_type=\"magnitude\", threshold_value=0.10,\n    )\n    asv_conf_sign = compute_asv(\n        \"confounding\", C_hat_conf_mean, params=CONFOUNDING_PARAMS,\n        threshold_type=\"sign_flip\",\n    )\n    asv_exp_mag = compute_asv(\n        \"exposure\", C_hat_exp_mean, params=EXPOSURE_PARAMS,\n        threshold_type=\"magnitude\", threshold_value=0.10,\n    )\n    asv_exp_sign = compute_asv(\n        \"exposure\", C_hat_exp_mean, params=EXPOSURE_PARAMS,\n        threshold_type=\"sign_flip\",\n    )\n\n    output = {\n        \"meta\": {\n            \"seed\": SEED,\n            \"N\": N,\n            \"K\": K,\n            \"gold_fraction\": GOLD_FRACTION,\n            \"n_reps\": N_REPS,\n            \"C0\": C0.tolist(),\n            \"confounding_params\": {\n                k: (v.tolist() if isinstance(v, np.ndarray) else v)\n                for k, v in CONFOUNDING_PARAMS.items()\n            },\n            \"exposure_params\": {\n                k: (v.tolist() if isinstance(v, np.ndarray) else v)\n                for k, v in EXPOSURE_PARAMS.items()\n            },\n        },\n        \"confounding\": {\n            **conf_summary,\n            \"routed_method\": \"no correction (FWL invariance)\",\n            \"C_hat_mean\": C_hat_conf_mean.tolist(),\n            \"asv_magnitude\": asv_conf_mag[\"asv\"],\n            \"asv_signflip\": asv_conf_sign[\"asv\"],\n            \"asv_tau_true_theoretical\": asv_conf_mag[\"tau_true\"],\n        },\n        \"exposure\": {\n            **exp_summary,\n            \"routed_method\": \"PPI++\",\n            \"C_hat_mean\": C_hat_exp_mean.tolist(),\n            \"asv_magnitude\": asv_exp_mag[\"asv\"],\n            \"asv_signflip\": asv_exp_sign[\"asv\"],\n            \"asv_tau_true_theoretical\": asv_exp_mag[\"tau_true\"],\n        },\n    }\n\n    out_json = os.path.join(PROJECT_ROOT, \"artifacts\", \"e2e_demo_results.json\")\n    with open(out_json, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nWrote {out_json}\")\n\n    write_latex_table(output)\n\n    print_console_summary(output)\n\n    print(f\"\\nElapsed: {time.time() - t0:.1f}s\")\n\n\ndef _fmt_asv(v):\n    return f\"{v:.3f}\" if v is not None else \"no crossing\"\n\n\ndef _fmt_pct(mean, std):\n    if not np.isfinite(mean):\n        return \"--\"\n    return f\"{mean:+.2f} $\\\\pm$ {std:.2f}\"\n\n\ndef write_latex_table(out):\n    conf = out[\"confounding\"]\n    exp = out[\"exposure\"]\n\n    conf_naive = conf[\"naive\"]\n    conf_np = conf[\"methods\"][\"tau_np\"]\n    conf_mla = conf[\"methods\"][\"tau_mla\"]\n    exp_naive = exp[\"naive\"]\n    exp_ppi = exp[\"methods\"][\"tau_ppi\"]\n\n    def _improve(m):\n        if m is None or not np.isfinite(m[\"improvement_pct\"]):\n            return \"--\"\n        return f\"{m['improvement_pct']:+.1f}\\\\%\"\n\n    def _bias_cell(m):\n        if m is None:\n            return \"--\"\n        return _fmt_pct(m[\"bias_pct_mean\"], m[\"bias_pct_std\"])\n\n    lines = []\n    lines.append(\"% Auto-generated by artifacts/e2e_demo.py\")\n    lines.append(\"\\\\begin{table}[t]\")\n    lines.append(\"\\\\centering\")\n    lines.append(\"\\\\small\")\n    lines.append(\"\\\\begin{tabular}{lrrlrr}\")\n    lines.append(\"\\\\toprule\")\n    lines.append(\n        \"Topology & Naive Bias (\\\\%) & ASV $\\\\delta^*_{\\\\mathrm{mag}}$ & \"\n        \"Routed Method & Corrected Bias (\\\\%) & Improvement (\\\\%) \\\\\\\\\"\n    )\n    lines.append(\"\\\\midrule\")\n\n    lines.append(\n        \"Confounding & \"\n        f\"{_fmt_pct(conf_naive['bias_pct_mean'], conf_naive['bias_pct_std'])} & \"\n        f\"{_fmt_asv(conf['asv_magnitude'])} & \"\n        \"no correction (FWL) & \"\n        f\"{_bias_cell(conf_np)} & {_improve(conf_np)} \\\\\\\\\"\n    )\n    lines.append(\n        \"\\\\quad (naive plug-in) & -- & -- & -- & \"\n        f\"{_bias_cell(conf_np)} & {_improve(conf_np)} \\\\\\\\\"\n    )\n    lines.append(\n        \"\\\\quad (MLA)          & -- & -- & -- & \"\n        f\"{_bias_cell(conf_mla)} & {_improve(conf_mla)} \\\\\\\\\"\n    )\n\n    lines.append(\n        \"Exposure & \"\n        f\"{_fmt_pct(exp_naive['bias_pct_mean'], exp_naive['bias_pct_std'])} & \"\n        f\"{_fmt_asv(exp['asv_magnitude'])} & \"\n        \"PPI++ & \"\n        f\"{_bias_cell(exp_ppi)} & {_improve(exp_ppi)} \\\\\\\\\"\n    )\n    lines.append(\"\\\\bottomrule\")\n    lines.append(\"\\\\end{tabular}\")\n    lines.append(\n        \"\\\\caption{End-to-end demo over \"\n        f\"{out['meta']['n_reps']} replicates \"\n        f\"(N={out['meta']['N']:,}, K={out['meta']['K']}, \"\n        f\"{int(out['meta']['gold_fraction']*100)}\\\\% gold). \"\n        \"Confounding: plug-in corrections leave the treatment coefficient \"\n        \"unchanged (FWL invariance), so Algorithm~1 routes to ``no correction''. \"\n        \"Exposure: PPI++ recovers the target coefficient using the gold subset.\"\n        \"}\"\n    )\n    lines.append(\"\\\\label{tab:e2e-demo}\")\n    lines.append(\"\\\\end{table}\")\n\n    out_tex = os.path.join(PROJECT_ROOT, \"artifacts\", \"e2e_demo_table.tex\")\n    with open(out_tex, \"w\") as f:\n        f.write(\"\\n\".join(lines) + \"\\n\")\n    print(f\"Wrote {out_tex}\")\n\n\ndef print_console_summary(out):\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SUMMARY\")\n    print(\"=\" * 70)\n    for topo in (\"confounding\", \"exposure\"):\n        s = out[topo]\n        print(f\"\\n[{topo}]  tau_true (empirical) = {s['tau_true']:.4f}\")\n        print(f\"  routed = {s['routed_method']}\")\n        nb = s[\"naive\"]\n        print(\n            f\"  naive       : tau = {nb['mean']:.4f} +/- {nb['std']:.4f}  \"\n            f\"bias = {nb['bias_pct_mean']:+.2f}% +/- {nb['bias_pct_std']:.2f}%\"\n        )\n        for key, m in s[\"methods\"].items():\n            if m is None:\n                print(f\"  {key:11s}: N/A\")\n                continue\n            print(\n                f\"  {key:11s}: tau = {m['mean']:.4f} +/- {m['std']:.4f}  \"\n                f\"bias = {m['bias_pct_mean']:+.2f}% +/- {m['bias_pct_std']:.2f}%  \"\n                f\"improvement = {m['improvement_pct']:+.1f}%\"\n            )\n        print(\n            f\"  ASV magnitude (10%) : {_fmt_asv(s['asv_magnitude'])}  |  \"\n            f\"ASV sign-flip : {_fmt_asv(s['asv_signflip'])}\"\n        )\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 426,
      "startLine": 1,
      "totalLines": 426
    }
  },
  "sourceToolAssistantUUID": "1ba47348-4c94-4e3a-a15b-c571a392ad61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-23T14:35:44.508Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CUT1jWo63RNGoNXBZGNYHh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/asv.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0b2f93c-90d4-497f-b2f9-ad42a2855f6a",
  "isSidechain": false,
  "requestId": "req_011CbKfh3MV8FFgYtfNTap8J",
  "type": "assistant",
  "uuid": "f94f5b6c-cf28-43fc-95e8-cacc946e4315",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfFR2wC5xmiFqyQP18X6JG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15234,
      "cache_read_input_tokens": 29736,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 29736,
          "cache_creation_input_tokens": 15234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15234
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

_source line 29_

```json
{
  "type": "last-prompt",
  "leafUuid": "80a40833-bbb2-4756-bdbf-ac3d62e89be6",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Mini end-to-end demo for causal annotation error",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4"
}
```

---

### Assistant

_source line 31 · 2026-05-23T14:35:58.762Z_

<details><summary>Logged reasoning block</summary>

```text
The existing `e2e_demo.py` already implements most of what's requested. Let me check the existing results and see if it already runs correctly or needs modifications.

Looking at the task description vs the existing code:
- The existing code already does confounding + exposure, 100 reps, N=10000, K=3, C0 with diag=0.7
- It already estimates Ĉ from gold labels (20%)
- It already computes ASV (magnitude + sign-flip)
- It already does Algorithm 1 routing
- It already applies corrections and computes bias


- It already outputs JSON and LaTeX table

The implementation looks complete against the spec, so I should just run it and verify the results match expectations.

Let me double-check the requirements one more time to make sure nothing's been missed. The task calls for two topologies—confounding with FWL and exposure with PPI++—each with N=10000 and K=3, using a known C0 with diagonal 0.7, estimating Ĉ from 20% gold standard data, computing ASV, applying Algorithm 1 routing and corrections, then comparing naive versus corrected results across 100 replications. The script covers all of this, so I'm ready to execute it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80a40833-bbb2-4756-bdbf-ac3d62e89be6",
  "isSidechain": false,
  "requestId": "req_011CbKfhTz55bdnDqxqh5o24",
  "type": "assistant",
  "uuid": "70cd1b67-1280-43cd-a3b6-befab63d4853",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XeA2icqUa9hG83P7szhzrk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7945,
      "cache_read_input_tokens": 44970,
      "output_tokens": 492,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7945,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 492,
          "cache_read_input_tokens": 44970,
          "cache_creation_input_tokens": 7945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7945
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

_source line 32 · 2026-05-23T14:35:58.774Z_

The existing `e2e_demo.py` already implements the full spec. Let me run it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70cd1b67-1280-43cd-a3b6-befab63d4853",
  "isSidechain": false,
  "requestId": "req_011CbKfhTz55bdnDqxqh5o24",
  "type": "assistant",
  "uuid": "2b5713c0-3ec3-4da7-99af-e3615fcb0723",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XeA2icqUa9hG83P7szhzrk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7945,
      "cache_read_input_tokens": 44970,
      "output_tokens": 492,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7945,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 492,
          "cache_read_input_tokens": 44970,
          "cache_creation_input_tokens": 7945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7945
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

_source line 33 · 2026-05-23T14:36:02.076Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Red5JbHn5bec4JfStcTaiB`</summary>

```json
{
  "command": "python artifacts/e2e_demo.py 2>&1",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b5713c0-3ec3-4da7-99af-e3615fcb0723",
  "isSidechain": false,
  "requestId": "req_011CbKfhTz55bdnDqxqh5o24",
  "type": "assistant",
  "uuid": "74bd8e6c-d1b0-4b07-8ab6-315af47ba321",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XeA2icqUa9hG83P7szhzrk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7945,
      "cache_read_input_tokens": 44970,
      "output_tokens": 492,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7945,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 492,
          "cache_read_input_tokens": 44970,
          "cache_creation_input_tokens": 7945,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7945
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

_source line 34 · 2026-05-23T14:36:02.248Z_

<details><summary>↩ Tool result · reported error · `toolu_01Red5JbHn5bec4JfStcTaiB`</summary>

```text
Exit code 127
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "74bd8e6c-d1b0-4b07-8ab6-315af47ba321",
  "isSidechain": false,
  "promptId": "931f36b2-6e79-486e-89c9-9074426aeee2",
  "type": "user",
  "uuid": "40b00825-e4a3-4a35-98ab-3db6248a7be1",
  "toolUseResult": "Error: Exit code 127\n/bin/bash: line 1: python: command not found",
  "sourceToolAssistantUUID": "74bd8e6c-d1b0-4b07-8ab6-315af47ba321",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-23T14:36:02.253Z_

```json
{
  "parentUuid": "40b00825-e4a3-4a35-98ab-3db6248a7be1",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "da2c1d48-cb7b-451f-b4e3-f482b0e9beff",
  "timestamp": "2026-05-23T14:36:02.253Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Tool call

_source line 36 · 2026-05-23T14:36:10.825Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014oYPEsC51UskJK6fan8kU4`</summary>

```json
{
  "command": "python3 artifacts/e2e_demo.py 2>&1",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da2c1d48-cb7b-451f-b4e3-f482b0e9beff",
  "isSidechain": false,
  "requestId": "req_011CbKfimnfR83XDYz6PJLn5",
  "type": "assistant",
  "uuid": "50583019-d5cf-4c9e-a4fd-40f68c844d81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzskKU9wJERWDN7qoP4AvX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 604,
      "cache_read_input_tokens": 52915,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 52915,
          "cache_creation_input_tokens": 604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 604
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

_source line 37 · 2026-05-23T14:36:14.384Z_

<details><summary>↩ Tool result · `toolu_014oYPEsC51UskJK6fan8kU4`</summary>

```text
======================================================================
Mini E2E demo: N=10000, K=3, gold=2000, reps=100
C0 diag=[0.7, 0.7, 0.7]
======================================================================

[Confounding] target = treatment coefficient tau = 0.5
  rep 25/100
  rep 50/100
  rep 75/100
  rep 100/100

[Exposure] target = beta_1 = 1.0
  rep 25/100
  rep 50/100
  rep 75/100
  rep 100/100

[ASV] computing magnitude & sign-flip thresholds with mean Cˆ...

Wrote /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_results.json
Wrote /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_table.tex

======================================================================
SUMMARY
======================================================================

[confounding]  tau_true (empirical) = 0.5000
  routed = no correction (FWL invariance)
  naive       : tau = 0.6136 +/- 0.0114  bias = +22.71% +/- 2.29%
  tau_np     : tau = 0.6136 +/- 0.0114  bias = +22.71% +/- 2.29%  improvement = +0.0%
  tau_mla    : tau = 0.6136 +/- 0.0114  bias = +22.71% +/- 2.29%  improvement = +0.0%
  ASV magnitude (10%) : 0.352  |  ASV sign-flip : no crossing

[exposure]  tau_true (empirical) = 1.0000
  routed = PPI++
  naive       : tau = 0.5713 +/- 0.0242  bias = -42.87% +/- 2.42%
  tau_ppi    : tau = 0.9978 +/- 0.0494  bias = -0.22% +/- 4.94%  improvement = +90.9%
  ASV magnitude (10%) : 0.239  |  ASV sign-flip : 2.220

Elapsed: 3.4s
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50583019-d5cf-4c9e-a4fd-40f68c844d81",
  "isSidechain": false,
  "promptId": "931f36b2-6e79-486e-89c9-9074426aeee2",
  "type": "user",
  "uuid": "d6c6297c-771b-4cf9-8052-80fa3e036df2",
  "toolUseResult": {
    "stdout": "======================================================================\nMini E2E demo: N=10000, K=3, gold=2000, reps=100\nC0 diag=[0.7, 0.7, 0.7]\n======================================================================\n\n[Confounding] target = treatment coefficient tau = 0.5\n  rep 25/100\n  rep 50/100\n  rep 75/100\n  rep 100/100\n\n[Exposure] target = beta_1 = 1.0\n  rep 25/100\n  rep 50/100\n  rep 75/100\n  rep 100/100\n\n[ASV] computing magnitude & sign-flip thresholds with mean Cˆ...\n\nWrote /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_results.json\nWrote /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_table.tex\n\n======================================================================\nSUMMARY\n======================================================================\n\n[confounding]  tau_true (empirical) = 0.5000\n  routed = no correction (FWL invariance)\n  naive       : tau = 0.6136 +/- 0.0114  bias = +22.71% +/- 2.29%\n  tau_np     : tau = 0.6136 +/- 0.0114  bias = +22.71% +/- 2.29%  improvement = +0.0%\n  tau_mla    : tau = 0.6136 +/- 0.0114  bias = +22.71% +/- 2.29%  improvement = +0.0%\n  ASV magnitude (10%) : 0.352  |  ASV sign-flip : no crossing\n\n[exposure]  tau_true (empirical) = 1.0000\n  routed = PPI++\n  naive       : tau = 0.5713 +/- 0.0242  bias = -42.87% +/- 2.42%\n  tau_ppi    : tau = 0.9978 +/- 0.0494  bias = -0.22% +/- 4.94%  improvement = +90.9%\n  ASV magnitude (10%) : 0.239  |  ASV sign-flip : 2.220\n\nElapsed: 3.4s",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "50583019-d5cf-4c9e-a4fd-40f68c844d81",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-23T14:36:24.021Z_

脚本运行成功，结果符合预期：

- **Confounding**: naive bias = +22.71%, naive_plugin 和 MLA 的 improvement = 0.0%（FWL 不变性，校正无法改善 treatment coefficient），ASV magnitude δ* = 0.352
- **Exposure**: naive bias = -42.87%, PPI++ corrected bias = -0.22%, improvement = +90.9%，ASV magnitude δ* = 0.239

JSON 结果已写入 `artifacts/e2e_demo_results.json`，LaTeX 表格已写入 `artifacts/e2e_demo_table.tex`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6c6297c-771b-4cf9-8052-80fa3e036df2",
  "isSidechain": false,
  "requestId": "req_011CbKfjg6PUfWnneeDPA1xd",
  "type": "assistant",
  "uuid": "90825507-1fb5-4236-9ceb-cf439916b106",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SytqfkU2bQCZvu5U4cufhr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 53519,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 688,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 53519,
          "cache_creation_input_tokens": 688,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 688
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

_source line 39_

```json
{
  "type": "last-prompt",
  "leafUuid": "90825507-1fb5-4236-9ceb-cf439916b106",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Mini end-to-end demo for causal annotation error",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4"
}
```

---
