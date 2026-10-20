# Research conversation: <project_context> # 项目: causal_annot_error_attrib ## 运行环境 - 服务器名: home-1x5090 - SSH 账户: sonny（调用 ssh_execute / submit_tr

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/c98dbbb7-289c-4874-8b26-c493fcfcccfa.jsonl`
- **Structured JSON:** [`dcce73c414ac2a925d6e.json`](../../sessions/dc/dcce73c414ac2a925d6e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-23T14:31:42.719Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T14:31:42.719Z",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "content": "&lt;project_context>\n# 项目: causal_annot_error_attrib\n\n## 运行环境\n- 服务器名: home-1x5090\n- SSH 账户: sonny（调用 ssh_execute / submit_training_job 时传入 account=\"sonny\"）\n- SSH 连接命令: ssh implicit5638.xyfu.me  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /home/sonny/causal_annot_error_attrib\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：Mini End-to-End Demo 实验\n\n**目标**：展示框架端到端可用性——从 C 估计到 ASV 诊断到 Algorithm 1 路由到校正改善。\n\n**项目路径**：`/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/`\n\n### 具体步骤\n\n写 Python 脚本 `artifacts/e2e_demo.py`，执行以下流程：\n\n1. **选 2 个拓扑**：confounding（FWL 使校正无效）和 exposure（PPI++ 有效）\n2. **对每个拓扑**：\n   - 生成合成数据 N=10,000，K=3，true β 已知\n   - 用已知 C（diagonal-dominant，diag=0.7）生成 A* = misclassify(A, C)\n   - 从 held-out subset (20% gold labels, 即 2,000 个) 估计 Ĉ\n   - 计算 ASV（magnitude, significance, sign-flip）\n   - Algorithm 1 路由：confounding → \"no correction (FWL)\"；exposure → \"PPI++\"\n   - 应用校正方法（PPI++ for exposure; show that naive/MLA achieve 0% for confounding）\n   - 对比 naive bias vs corrected bias vs true\n3. **重复 100 次** 取 mean ± std\n\n### 代码参考\n\n- **DGP 和工具函数**：参考 `artifacts/compute_ppi_empirical.py` 的 DGP 结构（softmax_rows, sample_cat, make_p_A, misclassify 等函数）\n- **校正方法**：使用 `annot_sensitivity.correction` 中的 `correct_ppi`, `correct_naive_plugin`, `correct_mcsimex`, `correct_mla`\n- **ASV 计算**：使用 `annot_sensitivity.asv` 中的函数\n- **工具函数**：`annot_sensitivity.utils` 中的 `misclassify`, `make_dummies`, `ols`, `ols_with_se`\n- **bias 计算**：`annot_sensitivity.bias` 中的 plim 函数\n\n先 `Read` 这些模块了解 API，特别是 `annot_sensitivity/correction.py` 中 `correct_ppi` 的签名和参数。\n\n### DGP 设计\n\n**Confounding DAG**: Y = τ·X + γ₁·1[A=1] + γ₂·1[A=2] + ε\n- X = α₀ + α₁·1[A=1] + α₂·1[A=2] + ε_x\n- τ = 0.5 (target), γ = [0, 0.8, -0.4], α = [0, 0.6, -0.3]\n- 回归: OLS of Y on (X, D*), 关注 X 的系数 τ̂\n\n**Exposure DAG**: Y = β₁·1[A=1] + β₂·1[A=2] + ε\n- β = [0, 1.0, -0.5]\n- 回归: OLS of Y on D*, 关注 β̂₁, β̂₂\n\n**Confusion matrix C₀**: diagonal-dominant with diag=0.7, off-diagonal uniform\n```python\nC0 = np.array([[0.7, 0.15, 0.15],\n               [0.15, 0.7, 0.15],\n               [0.15, 0.15, 0.7]])\n```\n\n### Ĉ 估计\n从 held-out gold subset（20% of N）估计 confusion matrix：\n```python\ndef estimate_C(A_true_gold, A_star_gold, K):\n    C_hat = np.zeros((K, K))\n    for k in range(K):\n        mask = (A_true_gold == k)\n        if mask.sum() > 0:\n            for j in range(K):\n                C_hat[j, k] = (A_star_gold[mask] == j).sum() / mask.sum()\n    return C_hat\n```\n\n### ASV 计算\n对每个拓扑：\n- 用 Ĉ 作为 C₀ 参数化 C(δ) = (1-δ)I + δĈ\n- 扫描 δ 从 0 到 1，找到 magnitude ASV（bias 超过 10% threshold）\n- 找到 sign-flip ASV（如适用）\n\n### 产出\n\n1. **脚本** `artifacts/e2e_demo.py`\n2. **JSON 结果** `artifacts/e2e_demo_results.json`，包含：\n   - per-topology: naive_bias (mean±std), corrected_bias (mean±std), improvement_pct, asv_magnitude, asv_signflip, routed_method\n3. **LaTeX table** `artifacts/e2e_demo_table.tex`，列：\n   Topology | Naive Bias (%) | ASV δ*_mag | Routed Method | Corrected Bias (%) | Improvement (%)\n\n### 验证\n- 脚本写完后运行: `cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib && python artifacts/e2e_demo.py`\n- 确认结果合理：confounding 的 naive/corrected 差异应该≈0%（FWL invariance）；exposure 的 PPI++ 应显著降低 bias\n- 如果 annot_sensitivity 模块中的函数 API 不匹配，检查实际签名并适配\n\n### 注意\n- 文件顶部加文件注释（说明目的、输入输出）\n- 代码要可复现（固定 seed=42）\n- 如果 PPI++ 需要 gold labels 参数，用 20% gold ratio\n- 100 次重复可能需要几分钟，可以先用 10 次验证正确性再跑 100 次"
}
````

---

### Runtime record

_source line 2 · 2026-05-23T14:31:42.722Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T14:31:42.722Z",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa"
}
```

---

## Round 1

54 recorded events

### User

_source line 3 · 2026-05-23T14:31:42.749Z_

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
  "promptId": "d4f14da1-f244-4256-aa7c-b4a034dc23f5",
  "type": "user",
  "uuid": "83e1d212-7661-406a-989e-9251d8135ced",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-23T14:31:42.748Z_

```json
{
  "parentUuid": "83e1d212-7661-406a-989e-9251d8135ced",
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
  "uuid": "ec9ee7dc-48e6-48cb-a6ef-e1294ae4504e",
  "timestamp": "2026-05-23T14:31:42.748Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-23T14:31:42.748Z_

```json
{
  "parentUuid": "ec9ee7dc-48e6-48cb-a6ef-e1294ae4504e",
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
  "uuid": "77f1bc23-4247-4f2f-b59e-6c3774a6346c",
  "timestamp": "2026-05-23T14:31:42.748Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-23T14:31:42.748Z_

```json
{
  "parentUuid": "77f1bc23-4247-4f2f-b59e-6c3774a6346c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9c5cb6f1-9638-4079-a250-7cf07bf9e69f",
  "timestamp": "2026-05-23T14:31:42.748Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
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
  "aiTitle": "Build mini end-to-end demo for causal annotation error",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa"
}
```

---

### Assistant

_source line 8 · 2026-05-23T14:31:49.441Z_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c5cb6f1-9638-4079-a250-7cf07bf9e69f",
  "isSidechain": false,
  "requestId": "req_011CbKfPeKvFK6TGubxrVfLt",
  "type": "assistant",
  "uuid": "1ac0272d-3014-409a-b03d-9e4904d59d95",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01ALRPmHLtVbAeT3bdT2mzW3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 18127,
      "cache_read_input_tokens": 16241,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18127,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 181,
          "cache_read_input_tokens": 16241,
          "cache_creation_input_tokens": 18127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18127
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

_source line 9 · 2026-05-23T14:31:50.404Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ei8MgwrkuxZ4ixvMCajkv5`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/",
  "description": "List annot_sensitivity module"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ac0272d-3014-409a-b03d-9e4904d59d95",
  "isSidechain": false,
  "requestId": "req_011CbKfPeKvFK6TGubxrVfLt",
  "type": "assistant",
  "uuid": "a7b6d7de-6bba-4059-a919-2e3b16a036b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01ALRPmHLtVbAeT3bdT2mzW3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 18127,
      "cache_read_input_tokens": 16241,
      "output_tokens": 181,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18127,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 181,
          "cache_read_input_tokens": 16241,
          "cache_creation_input_tokens": 18127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18127
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

_source line 10 · 2026-05-23T14:31:50.533Z_

<details><summary>↩ Tool result · `toolu_01Ei8MgwrkuxZ4ixvMCajkv5`</summary>

```text
__init__.py
__pycache__
asv.py
bias.py
confusion.py
correction.py
dgp.py
examples
tests
utils.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7b6d7de-6bba-4059-a919-2e3b16a036b7",
  "isSidechain": false,
  "promptId": "d4f14da1-f244-4256-aa7c-b4a034dc23f5",
  "type": "user",
  "uuid": "f2a2cfd7-2d22-4539-bed5-5b0195f93372",
  "toolUseResult": {
    "stdout": "__init__.py\n__pycache__\nasv.py\nbias.py\nconfusion.py\ncorrection.py\ndgp.py\nexamples\ntests\nutils.py",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a7b6d7de-6bba-4059-a919-2e3b16a036b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T14:31:52.612Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VXN2axsL2jYGketMhhzKhD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/correction.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2a2cfd7-2d22-4539-bed5-5b0195f93372",
  "isSidechain": false,
  "requestId": "req_011CbKfQDMmunH8MEafWWRHt",
  "type": "assistant",
  "uuid": "53e75cb1-e95c-4674-aa6f-a27613c9c85e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XuRroBxmFdPqLBwjwNdVQz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 247,
      "cache_read_input_tokens": 34368,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 34368,
          "cache_creation_input_tokens": 247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 247
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

_source line 12 · 2026-05-23T14:31:52.624Z_

<details><summary>↩ Tool result · `toolu_01VXN2axsL2jYGketMhhzKhD`</summary>

```text
1	"""Correction methods and recommendation engine for annotation-error bias.
2	
3	Five correction methods:
4	  - naive_plugin: C^{-1} correction of dummy indicators
5	  - dsl: EM-based joint estimation of regression params and C
6	  - ppi: PPI++ combining gold-standard and full-sample estimates
7	  - mcsimex: MC-SIMEX extrapolation to lambda=-1
8	  - mla: Matrix-based label adjustment via D*_full @ C^{-1}
9	
10	Key finding (FWL theorem): naive_plugin and mla correct dummy coefficients
11	but NOT the treatment coefficient in regressions with a separate treatment T.
12	"""
13	
14	import numpy as np
15	from .utils import ols, ols_with_se, make_dummies, make_full_dummies, misclassify
16	
17	METHODS = ["naive_plugin", "dsl", "ppi", "mcsimex", "mla"]
18	
19	_EM_MAX_ITER = 100
20	_EM_TOL = 1e-6
21	_SIMEX_LAMBDAS = [0.5, 1.0, 1.5, 2.0]
22	_SIMEX_B = 50
23	
24	
25	def correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1):
26	    """Correct using C^{-1} applied per-observation to dummy indicators.
27	
28	    Args:
29	        X_other: (N, p) non-A regressors (includes intercept)
30	        Y: (N,) outcome
31	        Astar: (N,) misclassified labels
32	        C: (K, K) confusion matrix
33	        tau_idx: index of target coefficient in full design
34	
35	    Returns:
36	        (tau_hat, se, success) tuple
37	    """
38	    cond = np.linalg.cond(C)
39	    if cond > 1e12:
40	        return np.nan, np.nan, False
41	    try:
42	        C_inv = np.linalg.inv(C)
43	    except np.linalg.LinAlgError:
44	        return np.nan, np.nan, False
45	    D_corrected = C_inv[:, Astar].T[:, 1:]
46	    X = np.column_stack([X_other, D_corrected])
47	    try:
48	        beta, se = ols_with_se(X, Y)
49	        return float(beta[tau_idx]), float(se[tau_idx]), True
50	    except Exception:
51	        return np.nan, np.nan, False
52	
53	
54	def correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1):
55	    """EM-based joint estimation of regression params and C.
56	
57	    Args:
58	        X_other: (N, p) non-A regressors (includes intercept)
59	        Y: (N,) outcome
60	        Astar: (N,) misclassified labels
61	        A_gold: (N,) gold-standard labels (only gold_mask positions used)
62	        gold_mask: (N,) boolean mask for gold-standard observations
63	        tau_idx: index of target coefficient
64	
65	    Returns:
66	        (tau_hat, se, success) tuple
67	    """
68	    N = len(Y)
69	    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1
70	    n_other = X_other.shape[1]
71	
72	    C_est = np.zeros((K, K))
73	    for j in range(K):
74	        for k in range(K):
75	            C_est[k, j] = (
76	                (A_gold[gold_mask] == j) & (Astar[gold_mask] == k)
77	            ).sum()
78	    col_sums = C_est.sum(axis=0)
79	    col_sums[col_sums == 0] = 1.0
80	    C_est /= col_sums
81	    C_est = 0.9 * C_est + 0.1 / K * np.ones((K, K))
82	
83	    D_star = make_dummies(Astar, K)
84	    X_init = np.column_stack([X_other, D_star])
85	    try:
86	        beta = ols(X_init, Y)
87	    except Exception:
88	        return np.nan, np.nan, False
89	    sigma2 = 1.0
90	
91	    for _ in range(_EM_MAX_ITER):
92	        base = X_other @ beta[:n_other]
93	        resp = np.zeros((N, K))
94	        for j in range(K):
95	            mu_j = base + (beta[n_other + j - 1] if j > 0 else 0.0)
96	            resp[:, j] = (
97	                -0.5 * (Y - mu_j) ** 2 / sigma2
98	                + np.log(np.clip(C_est[Astar, j], 1e-15, None))
99	            )
100	        resp -= resp.max(axis=1, keepdims=True)
101	        resp = np.exp(resp)
102	        resp /= resp.sum(axis=1, keepdims=True)
103	        resp[gold_mask] = 0.0
104	        resp[gold_mask, A_gold[gold_mask]] = 1.0
105	
106	        D_exp = resp[:, 1:]
107	        X_new = np.column_stack([X_other, D_exp])
108	        try:
109	            beta_new = ols(X_new, Y)
110	        except Exception:
111	            return np.nan, np.nan, False
112	        sigma2_new = max(np.mean((Y - X_new @ beta_new) ** 2), 1e-6)
113	
114	        C_new = np.zeros((K, K))
115	        for j in range(K):
116	            for k in range(K):
117	                C_new[k, j] = resp[Astar == k, j].sum()
118	        cs = C_new.sum(axis=0)
119	        cs[cs == 0] = 1.0
120	        C_new /= cs
121	
122	        converged = (
123	            np.max(np.abs(beta_new - beta)) < _EM_TOL
124	            and np.max(np.abs(C_new - C_est)) < _EM_TOL
125	        )
126	        beta, C_est, sigma2 = beta_new, C_new, sigma2_new
127	        if converged:
128	            break
129	
130	    X_final = np.column_stack([X_other, resp[:, 1:]])
131	    try:
132	        beta_f, se_f = ols_with_se(X_final, Y)
133	        return float(beta_f[tau_idx]), float(se_f[tau_idx]), True
134	    except Exception:
135	        return np.nan, np.nan, False
136	
137	
138	def correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1, rng=None):
139	    """PPI++ with bootstrap lambda tuning.
140	
141	    Args:
142	        X_other: (N, p) non-A regressors (includes intercept)
143	        Y: (N,) outcome
144	        Astar: (N,) misclassified labels
145	        A_gold: (N,) gold-standard labels
146	        gold_mask: (N,) boolean mask for gold-standard observations
147	        tau_idx: index of target coefficient
148	        rng: numpy random Generator
149	
150	    Returns:
151	        (tau_hat, se, success) tuple
152	    """
153	    if rng is None:
154	        rng = np.random.default_rng()
155	    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1
156	    gold_idx = np.where(gold_mask)[0]
157	    n_gold = len(gold_idx)
158	
159	    D_g_true = make_dummies(A_gold[gold_mask], K)
160	    X_g_true = np.column_stack([X_other[gold_mask], D_g_true])
161	    D_g_star = make_dummies(Astar[gold_mask], K)
162	    X_g_star = np.column_stack([X_other[gold_mask], D_g_star])
163	    D_all_star = make_dummies(Astar, K)
164	    X_all_star = np.column_stack([X_other, D_all_star])
165	
166	    try:
167	        b_g_true = ols(X_g_true, Y[gold_mask])
168	        b_g_star = ols(X_g_star, Y[gold_mask])
169	        b_all_star = ols(X_all_star, Y)
170	    except Exception:
171	        return np.nan, np.nan, False
172	
173	    n_boot = 50
174	    tau_true_boot = np.zeros(n_boot)
175	    tau_rect_boot = np.zeros(n_boot)
176	    for b in range(n_boot):
177	        idx = rng.choice(gold_idx, size=n_gold, replace=True)
178	        try:
179	            bt = ols(
180	                np.column_stack([X_other[idx], make_dummies(A_gold[idx], K)]),
181	                Y[idx],
182	            )
183	            bs = ols(
184	                np.column_stack([X_other[idx], make_dummies(Astar[idx], K)]),
185	                Y[idx],
186	            )
187	            tau_true_boot[b] = bt[tau_idx]
188	            tau_rect_boot[b] = bs[tau_idx] - bt[tau_idx]
189	        except Exception:
190	            tau_true_boot[b] = tau_rect_boot[b] = np.nan
191	
192	    valid = np.isfinite(tau_true_boot) & np.isfinite(tau_rect_boot)
193	    if valid.sum() > 5:
194	        var_r = np.var(tau_rect_boot[valid])
195	        cov_tr = np.cov(tau_true_boot[valid], tau_rect_boot[valid])[0, 1]
196	        lam = np.clip(-cov_tr / var_r, 0, 1) if var_r > 1e-12 else 1.0
197	    else:
198	        lam = 1.0
199	
200	    tau_ppi = b_g_true[tau_idx] + lam * (b_all_star[tau_idx] - b_g_star[tau_idx])
201	    se_est = float(np.std(tau_true_boot[valid])) if valid.sum() > 1 else np.nan
202	    return float(tau_ppi), se_est, True
203	
204	
205	def correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=None):
206	    """MC-SIMEX: add extra misclassification at levels lambda, extrapolate to -1.
207	
208	    Args:
209	        X_other: (N, p) non-A regressors (includes intercept)
210	        Y: (N,) outcome
211	        Astar: (N,) misclassified labels
212	        C: (K, K) confusion matrix
213	        tau_idx: index of target coefficient
214	        rng: numpy random Generator
215	
216	    Returns:
217	        (tau_hat, se, success) tuple
218	    """
219	    if rng is None:
220	        rng = np.random.default_rng()
221	    K = C.shape[0]
222	    try:
223	        eigvals, eigvecs = np.linalg.eig(C)
224	        eigvecs_inv = np.linalg.inv(eigvecs)
225	    except np.linalg.LinAlgError:
226	        return np.nan, np.nan, False
227	
228	    lambdas = np.array([0.0] + _SIMEX_LAMBDAS)
229	    tau_lam = np.zeros(len(lambdas))
230	
231	    for li, lam_val in enumerate(lambdas):
232	        if lam_val == 0.0:
233	            D_star = make_dummies(Astar, K)
234	            X = np.column_stack([X_other, D_star])
235	            try:
236	                tau_lam[li] = ols(X, Y)[tau_idx]
237	            except Exception:
238	                return np.nan, np.nan, False
239	        else:
240	            C_lam_raw = np.real((eigvecs * (eigvals ** lam_val)) @ eigvecs_inv)
241	            C_lam = np.clip(C_lam_raw, 0, None)
242	            cs = C_lam.sum(axis=0)
243	            cs[cs == 0] = 1.0
244	            C_lam /= cs
245	
246	            tau_b = np.zeros(_SIMEX_B)
247	            for b in range(_SIMEX_B):
248	                rng_b = np.random.default_rng(
249	                    rng.integers(0, 2 ** 31) + b * 1000 + li * 100000
250	                )
251	                A_extra = misclassify(Astar, C_lam, rng_b)
252	                D_extra = make_dummies(A_extra, K)
253	                X_extra = np.column_stack([X_other, D_extra])
254	                try:
255	                    tau_b[b] = ols(X_extra, Y)[tau_idx]
256	                except Exception:
257	                    tau_b[b] = np.nan
258	            ok = np.isfinite(tau_b)
259	            if ok.sum() < _SIMEX_B // 2:
260	                return np.nan, np.nan, False
261	            tau_lam[li] = tau_b[ok].mean()
262	
263	    try:
264	        coeffs = np.polyfit(lambdas, tau_lam, 2)
265	        tau_simex = float(np.polyval(coeffs, -1.0))
266	    except Exception:
267	        return np.nan, np.nan, False
268	
269	    D_star = make_dummies(Astar, K)
270	    X = np.column_stack([X_other, D_star])
271	    try:
272	        _, se = ols_with_se(X, Y)
273	        return tau_simex, float(se[tau_idx]), True
274	    except Exception:
275	        return tau_simex, np.nan, True
276	
277	
278	def correct_mla(X_other, Y, Astar, C, tau_idx=1):
279	    """MLA: D_corrected = D*_full @ C^{-1}, drop reference category.
280	
281	    Args:
282	        X_other: (N, p) non-A regressors (includes intercept)
283	        Y: (N,) outcome
284	        Astar: (N,) misclassified labels
285	        C: (K, K) confusion matrix
286	        tau_idx: index of target coefficient
287	
288	    Returns:
289	        (tau_hat, se, success) tuple
290	    """
291	    cond = np.linalg.cond(C)
292	    if cond > 1e12:
293	        return np.nan, np.nan, False
294	    try:
295	        C_inv = np.linalg.inv(C)
296	    except np.linalg.LinAlgError:
297	        return np.nan, np.nan, False
298	    K = C.shape[0]
299	    D_full = make_full_dummies(Astar, K)
300	    D_corrected = (D_full @ C_inv)[:, 1:]
301	    X = np.column_stack([X_other, D_corrected])
302	    try:
303	        beta, se = ols_with_se(X, Y)
304	        return float(beta[tau_idx]), float(se[tau_idx]), True
305	    except Exception:
306	        return np.nan, np.nan, False
307	
308	
309	def recommend_correction(topology, C, has_gold=False, gold_fraction=0.1):
310	    """Recommend the best correction method based on topology and data availability.
311	
312	    Rules (from plan_007 conclusions):
313	      - has_gold=True  -> PPI++ (93.8% bias reduction, 96.8% coverage)
314	      - has_gold=False + confounding/mediation -> DSL
315	      - has_gold=False + other topologies -> MC-SIMEX
316	      - naive_plugin/MLA: only correct dummy coefficients (FWL theorem)
317	
318	    Args:
319	        topology: one of 7 DAG types
320	        C: (K, K) confusion matrix (used for diagnostics)
321	        has_gold: whether gold-standard labels are available
322	        gold_fraction: fraction of data with gold labels
323	
324	    Returns:
325	        dict with recommended, ranking, notes
326	    """
327	    dsl_safe = topology in ("confounding", "mediation")
328	
329	    if has_gold:
330	        recommended = "ppi"
331	    elif dsl_safe:
332	        recommended = "dsl"
333	    else:
334	        recommended = "mcsimex"
335	
336	    ranking = []
337	
338	    # PPI++
339	    if has_gold:
340	        ranking.append({
341	            "method": "ppi",
342	            "applicable": True,
343	            "expected_bias_reduction": 0.938,
344	            "notes": "Best with gold labels (93.8% bias reduction, 96.8% coverage)",
345	        })
346	    else:
347	        ranking.append({
348	            "method": "ppi",
349	            "applicable": False,
350	            "expected_bias_reduction": 0.0,
351	            "notes": "Requires gold-standard labels",
352	        })
353	
354	    # DSL
355	    if dsl_safe:
356	        ranking.append({
357	            "method": "dsl",
358	            "applicable": True,
359	            "expected_bias_reduction": 0.75,
360	            "notes": "Good for confounding/mediation"
361	                     + (" (best with gold for initialization)" if not has_gold else ""),
362	        })
363	    else:
364	        ranking.append({
365	            "method": "dsl",
366	            "applicable": False,
367	            "expected_bias_reduction": -5.0,
368	            "notes": f"Catastrophic for {topology} (e.g., mbias yields -768%)",
369	        })
370	
371	    # MC-SIMEX
372	    ranking.append({
373	        "method": "mcsimex",
374	        "applicable": True,
375	        "expected_bias_reduction": 0.209,
376	        "notes": "Moderate (20.9%) but broadly applicable; requires known C",
377	    })
378	
379	    # Naive Plugin
380	    ranking.append({
381	        "method": "naive_plugin",
382	        "applicable": True,
383	        "expected_bias_reduction": 0.0,
384	        "notes": "Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)",
385	    })
386	
387	    # MLA
388	    ranking.append({
389	        "method": "mla",
390	        "applicable": True,
391	        "expected_bias_reduction": 0.0,
392	        "notes": "Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)",
393	    })
394	
395	    ranking.sort(key=lambda m: -m["expected_bias_reduction"])
396	
397	    notes = []
398	    if has_gold:
399	        notes.append(f"Gold labels available ({gold_fraction:.0%} of data)")
400	        notes.append("PPI++ recommended: highest bias reduction with valid coverage")
401	    else:
402	        notes.append("No gold labels available")
403	        if dsl_safe:
404	            notes.append(f"DSL recommended for {topology} (EM-based, works with known C)")
405	        else:
406	            notes.append(
407	                f"MC-SIMEX recommended; DSL is catastrophic for {topology}"
408	            )
409	
410	    cond = np.linalg.cond(C)
411	    if cond > 100:
412	        notes.append(
413	            f"WARNING: C condition number = {cond:.0f}, "
414	            f"inverse-based methods may be unstable"
415	        )
416	
417	    return {
418	        "recommended": recommended,
419	        "ranking": ranking,
420	        "notes": notes,
421	    }
422	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53e75cb1-e95c-4674-aa6f-a27613c9c85e",
  "isSidechain": false,
  "promptId": "d4f14da1-f244-4256-aa7c-b4a034dc23f5",
  "type": "user",
  "uuid": "41df5006-c5ef-45c4-9ce0-b2f88e96693f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/correction.py",
      "content": "\"\"\"Correction methods and recommendation engine for annotation-error bias.\n\nFive correction methods:\n  - naive_plugin: C^{-1} correction of dummy indicators\n  - dsl: EM-based joint estimation of regression params and C\n  - ppi: PPI++ combining gold-standard and full-sample estimates\n  - mcsimex: MC-SIMEX extrapolation to lambda=-1\n  - mla: Matrix-based label adjustment via D*_full @ C^{-1}\n\nKey finding (FWL theorem): naive_plugin and mla correct dummy coefficients\nbut NOT the treatment coefficient in regressions with a separate treatment T.\n\"\"\"\n\nimport numpy as np\nfrom .utils import ols, ols_with_se, make_dummies, make_full_dummies, misclassify\n\nMETHODS = [\"naive_plugin\", \"dsl\", \"ppi\", \"mcsimex\", \"mla\"]\n\n_EM_MAX_ITER = 100\n_EM_TOL = 1e-6\n_SIMEX_LAMBDAS = [0.5, 1.0, 1.5, 2.0]\n_SIMEX_B = 50\n\n\ndef correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1):\n    \"\"\"Correct using C^{-1} applied per-observation to dummy indicators.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        C: (K, K) confusion matrix\n        tau_idx: index of target coefficient in full design\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    cond = np.linalg.cond(C)\n    if cond > 1e12:\n        return np.nan, np.nan, False\n    try:\n        C_inv = np.linalg.inv(C)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n    D_corrected = C_inv[:, Astar].T[:, 1:]\n    X = np.column_stack([X_other, D_corrected])\n    try:\n        beta, se = ols_with_se(X, Y)\n        return float(beta[tau_idx]), float(se[tau_idx]), True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1):\n    \"\"\"EM-based joint estimation of regression params and C.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        A_gold: (N,) gold-standard labels (only gold_mask positions used)\n        gold_mask: (N,) boolean mask for gold-standard observations\n        tau_idx: index of target coefficient\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    N = len(Y)\n    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1\n    n_other = X_other.shape[1]\n\n    C_est = np.zeros((K, K))\n    for j in range(K):\n        for k in range(K):\n            C_est[k, j] = (\n                (A_gold[gold_mask] == j) & (Astar[gold_mask] == k)\n            ).sum()\n    col_sums = C_est.sum(axis=0)\n    col_sums[col_sums == 0] = 1.0\n    C_est /= col_sums\n    C_est = 0.9 * C_est + 0.1 / K * np.ones((K, K))\n\n    D_star = make_dummies(Astar, K)\n    X_init = np.column_stack([X_other, D_star])\n    try:\n        beta = ols(X_init, Y)\n    except Exception:\n        return np.nan, np.nan, False\n    sigma2 = 1.0\n\n    for _ in range(_EM_MAX_ITER):\n        base = X_other @ beta[:n_other]\n        resp = np.zeros((N, K))\n        for j in range(K):\n            mu_j = base + (beta[n_other + j - 1] if j > 0 else 0.0)\n            resp[:, j] = (\n                -0.5 * (Y - mu_j) ** 2 / sigma2\n                + np.log(np.clip(C_est[Astar, j], 1e-15, None))\n            )\n        resp -= resp.max(axis=1, keepdims=True)\n        resp = np.exp(resp)\n        resp /= resp.sum(axis=1, keepdims=True)\n        resp[gold_mask] = 0.0\n        resp[gold_mask, A_gold[gold_mask]] = 1.0\n\n        D_exp = resp[:, 1:]\n        X_new = np.column_stack([X_other, D_exp])\n        try:\n            beta_new = ols(X_new, Y)\n        except Exception:\n            return np.nan, np.nan, False\n        sigma2_new = max(np.mean((Y - X_new @ beta_new) ** 2), 1e-6)\n\n        C_new = np.zeros((K, K))\n        for j in range(K):\n            for k in range(K):\n                C_new[k, j] = resp[Astar == k, j].sum()\n        cs = C_new.sum(axis=0)\n        cs[cs == 0] = 1.0\n        C_new /= cs\n\n        converged = (\n            np.max(np.abs(beta_new - beta)) < _EM_TOL\n            and np.max(np.abs(C_new - C_est)) < _EM_TOL\n        )\n        beta, C_est, sigma2 = beta_new, C_new, sigma2_new\n        if converged:\n            break\n\n    X_final = np.column_stack([X_other, resp[:, 1:]])\n    try:\n        beta_f, se_f = ols_with_se(X_final, Y)\n        return float(beta_f[tau_idx]), float(se_f[tau_idx]), True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1, rng=None):\n    \"\"\"PPI++ with bootstrap lambda tuning.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        A_gold: (N,) gold-standard labels\n        gold_mask: (N,) boolean mask for gold-standard observations\n        tau_idx: index of target coefficient\n        rng: numpy random Generator\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1\n    gold_idx = np.where(gold_mask)[0]\n    n_gold = len(gold_idx)\n\n    D_g_true = make_dummies(A_gold[gold_mask], K)\n    X_g_true = np.column_stack([X_other[gold_mask], D_g_true])\n    D_g_star = make_dummies(Astar[gold_mask], K)\n    X_g_star = np.column_stack([X_other[gold_mask], D_g_star])\n    D_all_star = make_dummies(Astar, K)\n    X_all_star = np.column_stack([X_other, D_all_star])\n\n    try:\n        b_g_true = ols(X_g_true, Y[gold_mask])\n        b_g_star = ols(X_g_star, Y[gold_mask])\n        b_all_star = ols(X_all_star, Y)\n    except Exception:\n        return np.nan, np.nan, False\n\n    n_boot = 50\n    tau_true_boot = np.zeros(n_boot)\n    tau_rect_boot = np.zeros(n_boot)\n    for b in range(n_boot):\n        idx = rng.choice(gold_idx, size=n_gold, replace=True)\n        try:\n            bt = ols(\n                np.column_stack([X_other[idx], make_dummies(A_gold[idx], K)]),\n                Y[idx],\n            )\n            bs = ols(\n                np.column_stack([X_other[idx], make_dummies(Astar[idx], K)]),\n                Y[idx],\n            )\n            tau_true_boot[b] = bt[tau_idx]\n            tau_rect_boot[b] = bs[tau_idx] - bt[tau_idx]\n        except Exception:\n            tau_true_boot[b] = tau_rect_boot[b] = np.nan\n\n    valid = np.isfinite(tau_true_boot) & np.isfinite(tau_rect_boot)\n    if valid.sum() > 5:\n        var_r = np.var(tau_rect_boot[valid])\n        cov_tr = np.cov(tau_true_boot[valid], tau_rect_boot[valid])[0, 1]\n        lam = np.clip(-cov_tr / var_r, 0, 1) if var_r > 1e-12 else 1.0\n    else:\n        lam = 1.0\n\n    tau_ppi = b_g_true[tau_idx] + lam * (b_all_star[tau_idx] - b_g_star[tau_idx])\n    se_est = float(np.std(tau_true_boot[valid])) if valid.sum() > 1 else np.nan\n    return float(tau_ppi), se_est, True\n\n\ndef correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=None):\n    \"\"\"MC-SIMEX: add extra misclassification at levels lambda, extrapolate to -1.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        C: (K, K) confusion matrix\n        tau_idx: index of target coefficient\n        rng: numpy random Generator\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    K = C.shape[0]\n    try:\n        eigvals, eigvecs = np.linalg.eig(C)\n        eigvecs_inv = np.linalg.inv(eigvecs)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n\n    lambdas = np.array([0.0] + _SIMEX_LAMBDAS)\n    tau_lam = np.zeros(len(lambdas))\n\n    for li, lam_val in enumerate(lambdas):\n        if lam_val == 0.0:\n            D_star = make_dummies(Astar, K)\n            X = np.column_stack([X_other, D_star])\n            try:\n                tau_lam[li] = ols(X, Y)[tau_idx]\n            except Exception:\n                return np.nan, np.nan, False\n        else:\n            C_lam_raw = np.real((eigvecs * (eigvals ** lam_val)) @ eigvecs_inv)\n            C_lam = np.clip(C_lam_raw, 0, None)\n            cs = C_lam.sum(axis=0)\n            cs[cs == 0] = 1.0\n            C_lam /= cs\n\n            tau_b = np.zeros(_SIMEX_B)\n            for b in range(_SIMEX_B):\n                rng_b = np.random.default_rng(\n                    rng.integers(0, 2 ** 31) + b * 1000 + li * 100000\n                )\n                A_extra = misclassify(Astar, C_lam, rng_b)\n                D_extra = make_dummies(A_extra, K)\n                X_extra = np.column_stack([X_other, D_extra])\n                try:\n                    tau_b[b] = ols(X_extra, Y)[tau_idx]\n                except Exception:\n                    tau_b[b] = np.nan\n            ok = np.isfinite(tau_b)\n            if ok.sum() < _SIMEX_B // 2:\n                return np.nan, np.nan, False\n            tau_lam[li] = tau_b[ok].mean()\n\n    try:\n        coeffs = np.polyfit(lambdas, tau_lam, 2)\n        tau_simex = float(np.polyval(coeffs, -1.0))\n    except Exception:\n        return np.nan, np.nan, False\n\n    D_star = make_dummies(Astar, K)\n    X = np.column_stack([X_other, D_star])\n    try:\n        _, se = ols_with_se(X, Y)\n        return tau_simex, float(se[tau_idx]), True\n    except Exception:\n        return tau_simex, np.nan, True\n\n\ndef correct_mla(X_other, Y, Astar, C, tau_idx=1):\n    \"\"\"MLA: D_corrected = D*_full @ C^{-1}, drop reference category.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        C: (K, K) confusion matrix\n        tau_idx: index of target coefficient\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    cond = np.linalg.cond(C)\n    if cond > 1e12:\n        return np.nan, np.nan, False\n    try:\n        C_inv = np.linalg.inv(C)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n    K = C.shape[0]\n    D_full = make_full_dummies(Astar, K)\n    D_corrected = (D_full @ C_inv)[:, 1:]\n    X = np.column_stack([X_other, D_corrected])\n    try:\n        beta, se = ols_with_se(X, Y)\n        return float(beta[tau_idx]), float(se[tau_idx]), True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef recommend_correction(topology, C, has_gold=False, gold_fraction=0.1):\n    \"\"\"Recommend the best correction method based on topology and data availability.\n\n    Rules (from plan_007 conclusions):\n      - has_gold=True  -> PPI++ (93.8% bias reduction, 96.8% coverage)\n      - has_gold=False + confounding/mediation -> DSL\n      - has_gold=False + other topologies -> MC-SIMEX\n      - naive_plugin/MLA: only correct dummy coefficients (FWL theorem)\n\n    Args:\n        topology: one of 7 DAG types\n        C: (K, K) confusion matrix (used for diagnostics)\n        has_gold: whether gold-standard labels are available\n        gold_fraction: fraction of data with gold labels\n\n    Returns:\n        dict with recommended, ranking, notes\n    \"\"\"\n    dsl_safe = topology in (\"confounding\", \"mediation\")\n\n    if has_gold:\n        recommended = \"ppi\"\n    elif dsl_safe:\n        recommended = \"dsl\"\n    else:\n        recommended = \"mcsimex\"\n\n    ranking = []\n\n    # PPI++\n    if has_gold:\n        ranking.append({\n            \"method\": \"ppi\",\n            \"applicable\": True,\n            \"expected_bias_reduction\": 0.938,\n            \"notes\": \"Best with gold labels (93.8% bias reduction, 96.8% coverage)\",\n        })\n    else:\n        ranking.append({\n            \"method\": \"ppi\",\n            \"applicable\": False,\n            \"expected_bias_reduction\": 0.0,\n            \"notes\": \"Requires gold-standard labels\",\n        })\n\n    # DSL\n    if dsl_safe:\n        ranking.append({\n            \"method\": \"dsl\",\n            \"applicable\": True,\n            \"expected_bias_reduction\": 0.75,\n            \"notes\": \"Good for confounding/mediation\"\n                     + (\" (best with gold for initialization)\" if not has_gold else \"\"),\n        })\n    else:\n        ranking.append({\n            \"method\": \"dsl\",\n            \"applicable\": False,\n            \"expected_bias_reduction\": -5.0,\n            \"notes\": f\"Catastrophic for {topology} (e.g., mbias yields -768%)\",\n        })\n\n    # MC-SIMEX\n    ranking.append({\n        \"method\": \"mcsimex\",\n        \"applicable\": True,\n        \"expected_bias_reduction\": 0.209,\n        \"notes\": \"Moderate (20.9%) but broadly applicable; requires known C\",\n    })\n\n    # Naive Plugin\n    ranking.append({\n        \"method\": \"naive_plugin\",\n        \"applicable\": True,\n        \"expected_bias_reduction\": 0.0,\n        \"notes\": \"Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)\",\n    })\n\n    # MLA\n    ranking.append({\n        \"method\": \"mla\",\n        \"applicable\": True,\n        \"expected_bias_reduction\": 0.0,\n        \"notes\": \"Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)\",\n    })\n\n    ranking.sort(key=lambda m: -m[\"expected_bias_reduction\"])\n\n    notes = []\n    if has_gold:\n        notes.append(f\"Gold labels available ({gold_fraction:.0%} of data)\")\n        notes.append(\"PPI++ recommended: highest bias reduction with valid coverage\")\n    else:\n        notes.append(\"No gold labels available\")\n        if dsl_safe:\n            notes.append(f\"DSL recommended for {topology} (EM-based, works with known C)\")\n        else:\n            notes.append(\n                f\"MC-SIMEX recommended; DSL is catastrophic for {topology}\"\n            )\n\n    cond = np.linalg.cond(C)\n    if cond > 100:\n        notes.append(\n            f\"WARNING: C condition number = {cond:.0f}, \"\n            f\"inverse-based methods may be unstable\"\n        )\n\n    return {\n        \"recommended\": recommended,\n        \"ranking\": ranking,\n        \"notes\": notes,\n    }\n",
      "numLines": 422,
      "startLine": 1,
      "totalLines": 422
    }
  },
  "sourceToolAssistantUUID": "53e75cb1-e95c-4674-aa6f-a27613c9c85e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "leafUuid": "41df5006-c5ef-45c4-9ce0-b2f88e96693f",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Build mini end-to-end demo for causal annotation error",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa"
}
```

---

### Tool call

_source line 15 · 2026-05-23T14:31:57.050Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ALhjpLLaE8PLASBf1EJAQ5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/utils.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41df5006-c5ef-45c4-9ce0-b2f88e96693f",
  "isSidechain": false,
  "requestId": "req_011CbKfQNbPrskhppM5c1rHp",
  "type": "assistant",
  "uuid": "378deb43-407d-4ab7-b909-9c8f50c68f34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014vW5uwsG1iSpgKbzNoWGvV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6994,
      "cache_read_input_tokens": 34615,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6994,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 34615,
          "cache_creation_input_tokens": 6994,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6994
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

_source line 16 · 2026-05-23T14:31:57.060Z_

<details><summary>↩ Tool result · `toolu_01ALhjpLLaE8PLASBf1EJAQ5`</summary>

```text
1	"""Shared utilities: OLS, dummy encoding, softmax sampling."""
2	
3	import numpy as np
4	
5	
6	def softmax_sample(logits, rng):
7	    """Sample categorical variable from row-wise softmax probabilities.
8	
9	    Args:
10	        logits: (N, K) array of logits
11	        rng: numpy random Generator
12	
13	    Returns:
14	        (N,) integer array with values in {0, ..., K-1}
15	    """
16	    e = np.exp(logits - logits.max(axis=1, keepdims=True))
17	    p = e / e.sum(axis=1, keepdims=True)
18	    cum = np.cumsum(p, axis=1)
19	    u = rng.uniform(size=logits.shape[0])
20	    K = logits.shape[1]
21	    result = np.zeros(logits.shape[0], dtype=int)
22	    for k in range(K - 1):
23	        result += (u >= cum[:, k]).astype(int)
24	    return result
25	
26	
27	def misclassify(A, C, rng):
28	    """Apply misclassification: A*_i ~ Cat(C[:, A_i]).
29	
30	    Args:
31	        A: (N,) true labels in {0, ..., K-1}
32	        C: (K, K) column-stochastic confusion matrix
33	        rng: numpy random Generator
34	
35	    Returns:
36	        (N,) misclassified labels
37	    """
38	    K = C.shape[0]
39	    probs = C[:, A]
40	    cum = np.cumsum(probs, axis=0)
41	    u = rng.uniform(size=len(A))
42	    result = np.zeros(len(A), dtype=int)
43	    for k in range(K - 1):
44	        result += (u >= cum[k]).astype(int)
45	    return result
46	
47	
48	def make_dummies(A, K=None):
49	    """Create K-1 dummy variables (reference category 0).
50	
51	    Args:
52	        A: (N,) categorical labels in {0, ..., K-1}
53	        K: number of categories (inferred from A if None)
54	
55	    Returns:
56	        (N, K-1) dummy matrix
57	    """
58	    if K is None:
59	        K = int(A.max()) + 1
60	    N = len(A)
61	    D = np.zeros((N, K - 1))
62	    for j in range(K - 1):
63	        D[:, j] = (A == j + 1).astype(float)
64	    return D
65	
66	
67	def make_full_dummies(A, K=None):
68	    """Create full K one-hot encoding.
69	
70	    Args:
71	        A: (N,) categorical labels in {0, ..., K-1}
72	        K: number of categories (inferred from A if None)
73	
74	    Returns:
75	        (N, K) one-hot matrix
76	    """
77	    if K is None:
78	        K = int(A.max()) + 1
79	    N = len(A)
80	    D = np.zeros((N, K))
81	    for j in range(K):
82	        D[:, j] = (A == j).astype(float)
83	    return D
84	
85	
86	def ols(X, Y):
87	    """OLS point estimate via least-squares.
88	
89	    Args:
90	        X: (N, p) design matrix
91	        Y: (N,) response
92	
93	    Returns:
94	        (p,) coefficient vector
95	    """
96	    return np.linalg.lstsq(X, Y, rcond=None)[0]
97	
98	
99	def ols_with_se(X, Y):
100	    """OLS point estimate with homoskedastic standard errors.
101	
102	    Args:
103	        X: (N, p) design matrix
104	        Y: (N,) response
105	
106	    Returns:
107	        (beta, se) tuple of (p,) arrays
108	    """
109	    beta = np.linalg.lstsq(X, Y, rcond=None)[0]
110	    resid = Y - X @ beta
111	    n, p = X.shape
112	    s2 = resid @ resid / max(n - p, 1)
113	    try:
114	        XtX_inv = np.linalg.inv(X.T @ X)
115	        se = np.sqrt(np.maximum(np.diag(s2 * XtX_inv), 0.0))
116	    except np.linalg.LinAlgError:
117	        se = np.full(p, np.nan)
118	    return beta, se
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "378deb43-407d-4ab7-b909-9c8f50c68f34",
  "isSidechain": false,
  "promptId": "d4f14da1-f244-4256-aa7c-b4a034dc23f5",
  "type": "user",
  "uuid": "f32c1279-78fd-4e13-a386-da5045094e69",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/utils.py",
      "content": "\"\"\"Shared utilities: OLS, dummy encoding, softmax sampling.\"\"\"\n\nimport numpy as np\n\n\ndef softmax_sample(logits, rng):\n    \"\"\"Sample categorical variable from row-wise softmax probabilities.\n\n    Args:\n        logits: (N, K) array of logits\n        rng: numpy random Generator\n\n    Returns:\n        (N,) integer array with values in {0, ..., K-1}\n    \"\"\"\n    e = np.exp(logits - logits.max(axis=1, keepdims=True))\n    p = e / e.sum(axis=1, keepdims=True)\n    cum = np.cumsum(p, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    K = logits.shape[1]\n    result = np.zeros(logits.shape[0], dtype=int)\n    for k in range(K - 1):\n        result += (u >= cum[:, k]).astype(int)\n    return result\n\n\ndef misclassify(A, C, rng):\n    \"\"\"Apply misclassification: A*_i ~ Cat(C[:, A_i]).\n\n    Args:\n        A: (N,) true labels in {0, ..., K-1}\n        C: (K, K) column-stochastic confusion matrix\n        rng: numpy random Generator\n\n    Returns:\n        (N,) misclassified labels\n    \"\"\"\n    K = C.shape[0]\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    result = np.zeros(len(A), dtype=int)\n    for k in range(K - 1):\n        result += (u >= cum[k]).astype(int)\n    return result\n\n\ndef make_dummies(A, K=None):\n    \"\"\"Create K-1 dummy variables (reference category 0).\n\n    Args:\n        A: (N,) categorical labels in {0, ..., K-1}\n        K: number of categories (inferred from A if None)\n\n    Returns:\n        (N, K-1) dummy matrix\n    \"\"\"\n    if K is None:\n        K = int(A.max()) + 1\n    N = len(A)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    return D\n\n\ndef make_full_dummies(A, K=None):\n    \"\"\"Create full K one-hot encoding.\n\n    Args:\n        A: (N,) categorical labels in {0, ..., K-1}\n        K: number of categories (inferred from A if None)\n\n    Returns:\n        (N, K) one-hot matrix\n    \"\"\"\n    if K is None:\n        K = int(A.max()) + 1\n    N = len(A)\n    D = np.zeros((N, K))\n    for j in range(K):\n        D[:, j] = (A == j).astype(float)\n    return D\n\n\ndef ols(X, Y):\n    \"\"\"OLS point estimate via least-squares.\n\n    Args:\n        X: (N, p) design matrix\n        Y: (N,) response\n\n    Returns:\n        (p,) coefficient vector\n    \"\"\"\n    return np.linalg.lstsq(X, Y, rcond=None)[0]\n\n\ndef ols_with_se(X, Y):\n    \"\"\"OLS point estimate with homoskedastic standard errors.\n\n    Args:\n        X: (N, p) design matrix\n        Y: (N,) response\n\n    Returns:\n        (beta, se) tuple of (p,) arrays\n    \"\"\"\n    beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n    resid = Y - X @ beta\n    n, p = X.shape\n    s2 = resid @ resid / max(n - p, 1)\n    try:\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(np.diag(s2 * XtX_inv), 0.0))\n    except np.linalg.LinAlgError:\n        se = np.full(p, np.nan)\n    return beta, se\n",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  },
  "sourceToolAssistantUUID": "378deb43-407d-4ab7-b909-9c8f50c68f34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T14:31:59.657Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y65CBLjiQm5Er9wS5wzxjy`</summary>

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
  "parentUuid": "f32c1279-78fd-4e13-a386-da5045094e69",
  "isSidechain": false,
  "requestId": "req_011CbKfQhesT3EzEDsnCkNoC",
  "type": "assistant",
  "uuid": "68f9468a-2e69-4024-b654-aaa5c1047153",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018FjoHqWrX9w9ubVgiQKPCQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1671,
      "cache_read_input_tokens": 41609,
      "output_tokens": 115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1671,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 115,
          "cache_read_input_tokens": 41609,
          "cache_creation_input_tokens": 1671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1671
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

_source line 18 · 2026-05-23T14:31:59.664Z_

<details><summary>↩ Tool result · `toolu_01Y65CBLjiQm5Er9wS5wzxjy`</summary>

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
  "parentUuid": "68f9468a-2e69-4024-b654-aaa5c1047153",
  "isSidechain": false,
  "promptId": "d4f14da1-f244-4256-aa7c-b4a034dc23f5",
  "type": "user",
  "uuid": "ab8ce115-8bf3-4350-95ea-7242d0ab8364",
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
  "sourceToolAssistantUUID": "68f9468a-2e69-4024-b654-aaa5c1047153",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T14:32:02.007Z_

<details open><summary>🔧 Tool call — Read · `toolu_01StEWrUwDHSGcPtRvBZyDaR`</summary>

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
  "parentUuid": "ab8ce115-8bf3-4350-95ea-7242d0ab8364",
  "isSidechain": false,
  "requestId": "req_011CbKfQtVV8yjhNa1K1qCEc",
  "type": "assistant",
  "uuid": "c8bcba5f-b4ad-48c0-86f7-d32aa903e542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KyNf3s89LLNeHinkKB4mCa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2027,
      "cache_read_input_tokens": 43280,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2027,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 116,
          "cache_read_input_tokens": 43280,
          "cache_creation_input_tokens": 2027,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2027
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

_source line 20 · 2026-05-23T14:32:02.029Z_

<details><summary>↩ Tool result · `toolu_01StEWrUwDHSGcPtRvBZyDaR`</summary>

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
  "parentUuid": "c8bcba5f-b4ad-48c0-86f7-d32aa903e542",
  "isSidechain": false,
  "promptId": "d4f14da1-f244-4256-aa7c-b4a034dc23f5",
  "type": "user",
  "uuid": "5dc78813-2649-4ed4-8227-33d6ca01c9f4",
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
  "sourceToolAssistantUUID": "c8bcba5f-b4ad-48c0-86f7-d32aa903e542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "leafUuid": "5dc78813-2649-4ed4-8227-33d6ca01c9f4",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Build mini end-to-end demo for causal annotation error",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa"
}
```

---

### Assistant

_source line 23 · 2026-05-23T14:32:04.435Z_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5dc78813-2649-4ed4-8227-33d6ca01c9f4",
  "isSidechain": false,
  "requestId": "req_011CbKfR4p6Y1xxgb4N2mBa2",
  "type": "assistant",
  "uuid": "35c5f6b0-76e0-43fe-bdfe-3229775db6c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Niqq5F9GKRkwSrnM4eqvdi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3872,
      "cache_read_input_tokens": 45307,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 45307,
          "cache_creation_input_tokens": 3872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3872
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

_source line 24 · 2026-05-23T14:32:06.022Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q3mF5JqKmVxqyG5sCJjeqG`</summary>

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
  "parentUuid": "35c5f6b0-76e0-43fe-bdfe-3229775db6c8",
  "isSidechain": false,
  "requestId": "req_011CbKfR4p6Y1xxgb4N2mBa2",
  "type": "assistant",
  "uuid": "8f8735e1-7337-41d8-98cf-3b67933a7c66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Niqq5F9GKRkwSrnM4eqvdi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3872,
      "cache_read_input_tokens": 45307,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 45307,
          "cache_creation_input_tokens": 3872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3872
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

_source line 25 · 2026-05-23T14:32:06.029Z_

<details><summary>↩ Tool result · `toolu_01Q3mF5JqKmVxqyG5sCJjeqG`</summary>

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
  "parentUuid": "8f8735e1-7337-41d8-98cf-3b67933a7c66",
  "isSidechain": false,
  "promptId": "d4f14da1-f244-4256-aa7c-b4a034dc23f5",
  "type": "user",
  "uuid": "395e93ec-784e-4fcd-a42d-7381d9cb0b87",
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
  "sourceToolAssistantUUID": "8f8735e1-7337-41d8-98cf-3b67933a7c66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "leafUuid": "395e93ec-784e-4fcd-a42d-7381d9cb0b87",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Build mini end-to-end demo for causal annotation error",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa"
}
```

---

### Assistant

_source line 28 · 2026-05-23T14:32:09.089Z_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "395e93ec-784e-4fcd-a42d-7381d9cb0b87",
  "isSidechain": false,
  "requestId": "req_011CbKfRPT1uynxGdvfuqbSu",
  "type": "assistant",
  "uuid": "ab3cc2be-87da-42d7-86bf-606f6a4ff6e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Tr9Giwo2XPZUhPvJ359LV2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11579,
      "cache_read_input_tokens": 49179,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11579,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 49179,
          "cache_creation_input_tokens": 11579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11579
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

_source line 29 · 2026-05-23T14:32:11.090Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FQ6NmGvhrw1m98NSuUEKGX`</summary>

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
  "parentUuid": "ab3cc2be-87da-42d7-86bf-606f6a4ff6e3",
  "isSidechain": false,
  "requestId": "req_011CbKfRPT1uynxGdvfuqbSu",
  "type": "assistant",
  "uuid": "a7575345-12f9-4bd0-ba9b-148ce9e044d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Tr9Giwo2XPZUhPvJ359LV2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11579,
      "cache_read_input_tokens": 49179,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11579,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 49179,
          "cache_creation_input_tokens": 11579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11579
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

_source line 30 · 2026-05-23T14:32:11.097Z_

<details><summary>↩ Tool result · `toolu_01FQ6NmGvhrw1m98NSuUEKGX`</summary>

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
  "parentUuid": "a7575345-12f9-4bd0-ba9b-148ce9e044d0",
  "isSidechain": false,
  "promptId": "d4f14da1-f244-4256-aa7c-b4a034dc23f5",
  "type": "user",
  "uuid": "586ecec3-9a7e-414a-86d7-53157e2d5a8b",
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
  "sourceToolAssistantUUID": "a7575345-12f9-4bd0-ba9b-148ce9e044d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-23T14:32:37.246Z_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "586ecec3-9a7e-414a-86d7-53157e2d5a8b",
  "isSidechain": false,
  "requestId": "req_011CbKfRjUn9Ar9S5RosstHC",
  "type": "assistant",
  "uuid": "8cb65a65-9055-4cd9-9c0a-4c6d0ab8449d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011RGq8fausWoQP67eVzQcSx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2207,
      "cache_read_input_tokens": 60758,
      "output_tokens": 1983,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1983,
          "cache_read_input_tokens": 60758,
          "cache_creation_input_tokens": 2207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2207
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

_source line 32 · 2026-05-23T14:32:38.845Z_

<details open><summary>🔧 Tool call — Read · `toolu_015CmEHUndP5puhiTPC6Ak8Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cb65a65-9055-4cd9-9c0a-4c6d0ab8449d",
  "isSidechain": false,
  "requestId": "req_011CbKfRjUn9Ar9S5RosstHC",
  "type": "assistant",
  "uuid": "35da70d4-0d90-460e-9e12-c91ae9828d65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011RGq8fausWoQP67eVzQcSx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2207,
      "cache_read_input_tokens": 60758,
      "output_tokens": 1983,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2207,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1983,
          "cache_read_input_tokens": 60758,
          "cache_creation_input_tokens": 2207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2207
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

_source line 33 · 2026-05-23T14:32:38.857Z_

<details><summary>↩ Tool result · `toolu_015CmEHUndP5puhiTPC6Ak8Y`</summary>

```text
1	"""Compute annotation-error bias via probability limit calculations.
2	
3	Uses precomputed sufficient statistics from large-sample DGP simulations
4	to compute OLS plim as a function of confusion matrix C, avoiding MC.
5	"""
6	
7	import warnings
8	import numpy as np
9	from .dgp import DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES
10	from .confusion import validate_confusion_matrix
11	
12	_N_PRECOMP = 2_000_000
13	_precomp_cache = {}
14	
15	
16	def _params_key(params):
17	    items = []
18	    for k, v in sorted(params.items()):
19	        if isinstance(v, np.ndarray):
20	            items.append((k, tuple(v.flat)))
21	        else:
22	            items.append((k, v))
23	    return tuple(items)
24	
25	
26	def _precompute(topology, params, K, seed=999):
27	    """Precompute sufficient statistics for plim calculation."""
28	    cache_key = (topology, _params_key(params), K)
29	    if cache_key in _precomp_cache:
30	        return _precomp_cache[cache_key]
31	
32	    rng = np.random.default_rng(seed)
33	    data = GEN_FUNCS[topology](_N_PRECOMP, params=params, rng=rng)
34	    Y = data["Y"]
35	    A = data["A"]
36	
37	    DA = np.zeros((_N_PRECOMP, K))
38	    for k in range(K):
39	        DA[:, k] = (A == k).astype(float)
40	
41	    stats = {
42	        "E_Y": Y.mean(),
43	        "E_DA": DA.mean(0),
44	        "E_DA_Y": (DA * Y[:, None]).mean(0),
45	    }
46	
47	    if topology in HAS_TREATMENT:
48	        T = data["T"]
49	        stats.update({
50	            "E_T": T.mean(),
51	            "E_T2": (T ** 2).mean(),
52	            "E_TY": (T * Y).mean(),
53	            "E_DA_T": (DA * T[:, None]).mean(0),
54	        })
55	
56	    if topology == "iv":
57	        Z = data["Z"]
58	        Zc = Z - Z.mean()
59	        var_Z = (Zc ** 2).mean()
60	        stats["RF"] = (Zc * (Y - Y.mean())).mean() / var_Z
61	        FS = np.zeros(K)
62	        for k in range(K):
63	            FS[k] = (Zc * (DA[:, k] - DA[:, k].mean())).mean() / var_Z
64	        stats["FS"] = FS
65	
66	    _precomp_cache[cache_key] = stats
67	    return stats
68	
69	
70	def _plim_with_T(C, stats, K):
71	    """OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}."""
72	    ds = C @ stats["E_DA"]
73	    dst = C @ stats["E_DA_T"]
74	    dsy = C @ stats["E_DA_Y"]
75	    ET, ET2 = stats["E_T"], stats["E_T2"]
76	    EY, ETY = stats["E_Y"], stats["E_TY"]
77	
78	    dim = 1 + K  # intercept + T + (K-1) dummies
79	    EZZ = np.zeros((dim, dim))
80	    EZZ[0, 0] = 1.0
81	    EZZ[0, 1] = EZZ[1, 0] = ET
82	    EZZ[1, 1] = ET2
83	    for j in range(1, K):
84	        idx = j + 1
85	        EZZ[0, idx] = EZZ[idx, 0] = ds[j]
86	        EZZ[1, idx] = EZZ[idx, 1] = dst[j]
87	        EZZ[idx, idx] = ds[j]
88	
89	    EZY = np.zeros(dim)
90	    EZY[0] = EY
91	    EZY[1] = ETY
92	    for j in range(1, K):
93	        EZY[j + 1] = dsy[j]
94	
95	    cond = np.linalg.cond(EZZ)
96	    if cond > 1e12:
97	        warnings.warn(
98	            f"EZZ condition number {cond:.1e} — plim may be numerically unstable"
99	        )
100	
101	    return np.linalg.solve(EZZ, EZY)
102	
103	
104	def _plim_no_T(C, stats, K):
105	    """OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}."""
106	    ds = C @ stats["E_DA"]
107	    dsy = C @ stats["E_DA_Y"]
108	    EY = stats["E_Y"]
109	
110	    dim = K  # intercept + (K-1) dummies
111	    EZZ = np.zeros((dim, dim))
112	    EZZ[0, 0] = 1.0
113	    for j in range(1, K):
114	        EZZ[0, j] = EZZ[j, 0] = ds[j]
115	        EZZ[j, j] = ds[j]
116	
117	    EZY = np.zeros(dim)
118	    EZY[0] = EY
119	    for j in range(1, K):
120	        EZY[j] = dsy[j]
121	
122	    cond = np.linalg.cond(EZZ)
123	    if cond > 1e12:
124	        warnings.warn(
125	            f"EZZ condition number {cond:.1e} — plim may be numerically unstable"
126	        )
127	
128	    return np.linalg.solve(EZZ, EZY)
129	
130	
131	def _plim_iv(C, stats, K):
132	    """Wald estimator plim: RF / (C @ FS)[1]."""
133	    FS_star = C @ stats["FS"]
134	    denom = FS_star[1]
135	    if abs(denom) < 1e-15:
136	        return np.nan
137	    return stats["RF"] / denom
138	
139	
140	def _get_tau(topology, C, stats, K):
141	    """Extract target coefficient from plim vector.
142	
143	    For IV: Wald estimator RF / (C @ FS)[1].
144	    For topologies with T: OLS coefficient index 1 (treatment effect).
145	    For topologies without T: OLS coefficient index 1 (first dummy).
146	    """
147	    if topology == "iv":
148	        return _plim_iv(C, stats, K)
149	    if topology in HAS_TREATMENT:
150	        coefs = _plim_with_T(C, stats, K)
151	    else:
152	        coefs = _plim_no_T(C, stats, K)
153	    return coefs[1]
154	
155	
156	def compute_bias(topology, C, params=None):
157	    """Compute annotation-error bias for a given topology and confusion matrix.
158	
159	    Args:
160	        topology: one of "confounding", "mediation", "collider", "exposure",
161	                  "mbias", "iv", "frontdoor"
162	        C: (K, K) column-stochastic confusion matrix, C[j,i] = P(A*=j|A=i)
163	        params: optional DGP parameters dict, None uses defaults
164	
165	    Returns:
166	        dict with tau_true, tau_biased, bias, bias_pct, topology
167	    """
168	    if topology not in TOPOLOGIES:
169	        raise ValueError(f"Unknown topology: {topology}. Choose from {TOPOLOGIES}")
170	    if not validate_confusion_matrix(C):
171	        raise ValueError("C must be a square, non-negative, column-stochastic matrix")
172	
173	    K = C.shape[0]
174	    merged = dict(DEFAULT_PARAMS[topology])
175	    if params is not None:
176	        merged.update(params)
177	
178	    stats = _precompute(topology, merged, K)
179	    tau_true = _get_tau(topology, np.eye(K), stats, K)
180	    tau_biased = _get_tau(topology, C, stats, K)
181	    bias = tau_biased - tau_true
182	    bias_pct = 100.0 * bias / tau_true if abs(tau_true) > 1e-12 else float("nan")
183	
184	    return {
185	        "tau_true": float(tau_true),
186	        "tau_biased": float(tau_biased),
187	        "bias": float(bias),
188	        "bias_pct": float(bias_pct),
189	        "topology": topology,
190	    }
191	
192	
193	def clear_cache():
194	    """Clear the precomputed statistics cache."""
195	    _precomp_cache.clear()
196	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35da70d4-0d90-460e-9e12-c91ae9828d65",
  "isSidechain": false,
  "promptId": "d4f14da1-f244-4256-aa7c-b4a034dc23f5",
  "type": "user",
  "uuid": "7023254c-71d8-425d-8788-3cdf0b9373df",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py",
      "content": "\"\"\"Compute annotation-error bias via probability limit calculations.\n\nUses precomputed sufficient statistics from large-sample DGP simulations\nto compute OLS plim as a function of confusion matrix C, avoiding MC.\n\"\"\"\n\nimport warnings\nimport numpy as np\nfrom .dgp import DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES\nfrom .confusion import validate_confusion_matrix\n\n_N_PRECOMP = 2_000_000\n_precomp_cache = {}\n\n\ndef _params_key(params):\n    items = []\n    for k, v in sorted(params.items()):\n        if isinstance(v, np.ndarray):\n            items.append((k, tuple(v.flat)))\n        else:\n            items.append((k, v))\n    return tuple(items)\n\n\ndef _precompute(topology, params, K, seed=999):\n    \"\"\"Precompute sufficient statistics for plim calculation.\"\"\"\n    cache_key = (topology, _params_key(params), K)\n    if cache_key in _precomp_cache:\n        return _precomp_cache[cache_key]\n\n    rng = np.random.default_rng(seed)\n    data = GEN_FUNCS[topology](_N_PRECOMP, params=params, rng=rng)\n    Y = data[\"Y\"]\n    A = data[\"A\"]\n\n    DA = np.zeros((_N_PRECOMP, K))\n    for k in range(K):\n        DA[:, k] = (A == k).astype(float)\n\n    stats = {\n        \"E_Y\": Y.mean(),\n        \"E_DA\": DA.mean(0),\n        \"E_DA_Y\": (DA * Y[:, None]).mean(0),\n    }\n\n    if topology in HAS_TREATMENT:\n        T = data[\"T\"]\n        stats.update({\n            \"E_T\": T.mean(),\n            \"E_T2\": (T ** 2).mean(),\n            \"E_TY\": (T * Y).mean(),\n            \"E_DA_T\": (DA * T[:, None]).mean(0),\n        })\n\n    if topology == \"iv\":\n        Z = data[\"Z\"]\n        Zc = Z - Z.mean()\n        var_Z = (Zc ** 2).mean()\n        stats[\"RF\"] = (Zc * (Y - Y.mean())).mean() / var_Z\n        FS = np.zeros(K)\n        for k in range(K):\n            FS[k] = (Zc * (DA[:, k] - DA[:, k].mean())).mean() / var_Z\n        stats[\"FS\"] = FS\n\n    _precomp_cache[cache_key] = stats\n    return stats\n\n\ndef _plim_with_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dst = C @ stats[\"E_DA_T\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    ET, ET2 = stats[\"E_T\"], stats[\"E_T2\"]\n    EY, ETY = stats[\"E_Y\"], stats[\"E_TY\"]\n\n    dim = 1 + K  # intercept + T + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    EZZ[0, 1] = EZZ[1, 0] = ET\n    EZZ[1, 1] = ET2\n    for j in range(1, K):\n        idx = j + 1\n        EZZ[0, idx] = EZZ[idx, 0] = ds[j]\n        EZZ[1, idx] = EZZ[idx, 1] = dst[j]\n        EZZ[idx, idx] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    EZY[1] = ETY\n    for j in range(1, K):\n        EZY[j + 1] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _plim_no_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    EY = stats[\"E_Y\"]\n\n    dim = K  # intercept + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    for j in range(1, K):\n        EZZ[0, j] = EZZ[j, 0] = ds[j]\n        EZZ[j, j] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    for j in range(1, K):\n        EZY[j] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _plim_iv(C, stats, K):\n    \"\"\"Wald estimator plim: RF / (C @ FS)[1].\"\"\"\n    FS_star = C @ stats[\"FS\"]\n    denom = FS_star[1]\n    if abs(denom) < 1e-15:\n        return np.nan\n    return stats[\"RF\"] / denom\n\n\ndef _get_tau(topology, C, stats, K):\n    \"\"\"Extract target coefficient from plim vector.\n\n    For IV: Wald estimator RF / (C @ FS)[1].\n    For topologies with T: OLS coefficient index 1 (treatment effect).\n    For topologies without T: OLS coefficient index 1 (first dummy).\n    \"\"\"\n    if topology == \"iv\":\n        return _plim_iv(C, stats, K)\n    if topology in HAS_TREATMENT:\n        coefs = _plim_with_T(C, stats, K)\n    else:\n        coefs = _plim_no_T(C, stats, K)\n    return coefs[1]\n\n\ndef compute_bias(topology, C, params=None):\n    \"\"\"Compute annotation-error bias for a given topology and confusion matrix.\n\n    Args:\n        topology: one of \"confounding\", \"mediation\", \"collider\", \"exposure\",\n                  \"mbias\", \"iv\", \"frontdoor\"\n        C: (K, K) column-stochastic confusion matrix, C[j,i] = P(A*=j|A=i)\n        params: optional DGP parameters dict, None uses defaults\n\n    Returns:\n        dict with tau_true, tau_biased, bias, bias_pct, topology\n    \"\"\"\n    if topology not in TOPOLOGIES:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    if not validate_confusion_matrix(C):\n        raise ValueError(\"C must be a square, non-negative, column-stochastic matrix\")\n\n    K = C.shape[0]\n    merged = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        merged.update(params)\n\n    stats = _precompute(topology, merged, K)\n    tau_true = _get_tau(topology, np.eye(K), stats, K)\n    tau_biased = _get_tau(topology, C, stats, K)\n    bias = tau_biased - tau_true\n    bias_pct = 100.0 * bias / tau_true if abs(tau_true) > 1e-12 else float(\"nan\")\n\n    return {\n        \"tau_true\": float(tau_true),\n        \"tau_biased\": float(tau_biased),\n        \"bias\": float(bias),\n        \"bias_pct\": float(bias_pct),\n        \"topology\": topology,\n    }\n\n\ndef clear_cache():\n    \"\"\"Clear the precomputed statistics cache.\"\"\"\n    _precomp_cache.clear()\n",
      "numLines": 196,
      "startLine": 1,
      "totalLines": 196
    }
  },
  "sourceToolAssistantUUID": "35da70d4-0d90-460e-9e12-c91ae9828d65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "leafUuid": "7023254c-71d8-425d-8788-3cdf0b9373df",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Build mini end-to-end demo for causal annotation error",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa"
}
```

---

### Assistant

_source line 36 · 2026-05-23T14:32:59.847Z_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7023254c-71d8-425d-8788-3cdf0b9373df",
  "isSidechain": false,
  "requestId": "req_011CbKfTn3NWocpbdZUXfMn3",
  "type": "assistant",
  "uuid": "e7d5fd1d-63c4-49c1-9f05-c01251e43612",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01L9eyHGCqCE1wFPjjwKQSTo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5092,
      "cache_read_input_tokens": 62965,
      "output_tokens": 8053,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8053,
          "cache_read_input_tokens": 62965,
          "cache_creation_input_tokens": 5092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5092
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

_source line 37 · 2026-05-23T14:33:00.440Z_

Now I have enough understanding. Let me write the e2e_demo.py script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7d5fd1d-63c4-49c1-9f05-c01251e43612",
  "isSidechain": false,
  "requestId": "req_011CbKfTn3NWocpbdZUXfMn3",
  "type": "assistant",
  "uuid": "a5b909af-f0f4-4641-b442-ddf99f4ca0ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01L9eyHGCqCE1wFPjjwKQSTo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5092,
      "cache_read_input_tokens": 62965,
      "output_tokens": 8053,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8053,
          "cache_read_input_tokens": 62965,
          "cache_creation_input_tokens": 5092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5092
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

_source line 38 · 2026-05-23T14:34:07.558Z_

<details open><summary>🔧 Tool call — Write · `toolu_01VQ1tPhwZ9BHxdTK3a3mzFx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nMini end-to-end demo: C estimation -> ASV diagnostic -> Algorithm 1 routing\n-> correction -> bias improvement.\n\nTwo topologies illustrate the dichotomy:\n  - confounding: FWL invariance => no plug-in correction helps the\n    treatment coefficient; routed method is \"no correction\".\n  - exposure: PPI++ recovers the target coefficient using a gold subset.\n\nPipeline for each topology:\n  1. Generate synthetic data with N=10000, K=3, known C0 (diag=0.7,\n     off-diagonal 0.15 uniform).\n  2. Sample 20% gold subset; estimate C_hat from gold (true vs. observed labels).\n  3. Compute ASV (magnitude & sign-flip) using C_hat as the base of the\n     interpolation path C(delta) = (1-delta) I + delta C_hat.\n  4. Algorithm 1 route:\n       - confounding => \"no correction (FWL)\"\n       - exposure    => \"PPI++\"\n  5. Apply correction(s); also run naive_plugin / MLA on confounding to\n     verify they do not move the treatment coefficient (FWL theorem).\n  6. Record naive bias, corrected bias, improvement.\n\n100 Monte Carlo replicates per topology (mean +/- std).\n\nOutputs:\n  - artifacts/e2e_demo_results.json\n  - artifacts/e2e_demo_table.tex\n\"\"\"\n\nimport json\nimport os\nimport sys\nimport time\n\nimport numpy as np\n\nPROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nsys.path.insert(0, PROJECT_ROOT)\n\nfrom annot_sensitivity.asv import compute_asv\nfrom annot_sensitivity.correction import (\n    correct_mla,\n    correct_naive_plugin,\n    correct_ppi,\n)\nfrom annot_sensitivity.dgp import gen_confounding, gen_exposure\nfrom annot_sensitivity.utils import make_dummies, misclassify, ols_with_se\n\nSEED = 42\nN = 10_000\nK = 3\nGOLD_FRACTION = 0.20\nN_REPS = 100\n\nC0 = np.array([\n    [0.70, 0.15, 0.15],\n    [0.15, 0.70, 0.15],\n    [0.15, 0.15, 0.70],\n])\n\nCONFOUNDING_PARAMS = {\n    \"p_A\": np.array([0.40, 0.35, 0.25]),\n    \"alpha\": np.array([0.6, -0.3]),\n    \"beta_A\": np.array([0.8, -0.4]),\n    \"beta_T\": 0.5,\n    \"sigma_T\": 1.0,\n}\n\nEXPOSURE_PARAMS = {\n    \"p_A\": np.array([0.40, 0.35, 0.25]),\n    \"beta\": np.array([0.0, 1.0, -0.5]),\n}\n\n\ndef estimate_C(A_true_gold, A_star_gold, K):\n    \"\"\"Column-stochastic Cˆ[j,k] = P(A* = j | A = k) from gold labels.\"\"\"\n    C_hat = np.zeros((K, K))\n    for k in range(K):\n        mask = A_true_gold == k\n        if mask.sum() > 0:\n            for j in range(K):\n                C_hat[j, k] = (A_star_gold[mask] == j).sum() / mask.sum()\n        else:\n            C_hat[k, k] = 1.0\n    return C_hat\n\n\ndef naive_confounding(X_other, Y, Astar, K, tau_idx=1):\n    D = make_dummies(Astar, K)\n    X = np.column_stack([X_other, D])\n    beta, se = ols_with_se(X, Y)\n    return float(beta[tau_idx]), float(se[tau_idx])\n\n\ndef naive_exposure(Y, Astar, K, tau_idx=1):\n    N_ = len(Y)\n    X_other = np.ones((N_, 1))\n    D = make_dummies(Astar, K)\n    X = np.column_stack([X_other, D])\n    beta, se = ols_with_se(X, Y)\n    return float(beta[tau_idx]), float(se[tau_idx])\n\n\ndef run_confounding_rep(rng, tau_true):\n    data = gen_confounding(N, params=CONFOUNDING_PARAMS, rng=rng)\n    T, Y, A = data[\"T\"], data[\"Y\"], data[\"A\"]\n    Astar = misclassify(A, C0, rng)\n\n    gold_idx = rng.choice(N, size=int(N * GOLD_FRACTION), replace=False)\n    gold_mask = np.zeros(N, dtype=bool)\n    gold_mask[gold_idx] = True\n    C_hat = estimate_C(A[gold_mask], Astar[gold_mask], K)\n\n    X_other = np.column_stack([np.ones(N), T])\n\n    tau_naive, _ = naive_confounding(X_other, Y, Astar, K, tau_idx=1)\n    tau_np, _, ok_np = correct_naive_plugin(X_other, Y, Astar, C_hat, tau_idx=1)\n    tau_mla, _, ok_mla = correct_mla(X_other, Y, Astar, C_hat, tau_idx=1)\n\n    return {\n        \"tau_naive\": tau_naive,\n        \"tau_np\": tau_np if ok_np else np.nan,\n        \"tau_mla\": tau_mla if ok_mla else np.nan,\n        \"C_hat\": C_hat,\n        \"tau_true\": tau_true,\n    }\n\n\ndef run_exposure_rep(rng, tau_true):\n    data = gen_exposure(N, params=EXPOSURE_PARAMS, rng=rng)\n    Y, A = data[\"Y\"], data[\"A\"]\n    Astar = misclassify(A, C0, rng)\n\n    gold_idx = rng.choice(N, size=int(N * GOLD_FRACTION), replace=False)\n    gold_mask = np.zeros(N, dtype=bool)\n    gold_mask[gold_idx] = True\n    C_hat = estimate_C(A[gold_mask], Astar[gold_mask], K)\n\n    X_other = np.ones((N, 1))\n    tau_naive, _ = naive_exposure(Y, Astar, K, tau_idx=1)\n    tau_ppi, _, ok_ppi = correct_ppi(X_other, Y, Astar, A, gold_mask,\n                                     tau_idx=1, rng=rng)\n\n    return {\n        \"tau_naive\": tau_naive,\n        \"tau_ppi\": tau_ppi if ok_ppi else np.nan,\n        \"C_hat\": C_hat,\n        \"tau_true\": tau_true,\n    }\n\n\ndef compute_summary(reps, method_keys, tau_true):\n    out = {\"tau_true\": float(tau_true)}\n    naive = np.array([r[\"tau_naive\"] for r in reps])\n    naive_bias = naive - tau_true\n    naive_bias_pct = 100.0 * naive_bias / tau_true\n    out[\"naive\"] = {\n        \"mean\": float(naive.mean()),\n        \"std\": float(naive.std(ddof=1)),\n        \"bias_mean\": float(naive_bias.mean()),\n        \"bias_std\": float(naive_bias.std(ddof=1)),\n        \"abs_bias_mean\": float(np.mean(np.abs(naive_bias))),\n        \"bias_pct_mean\": float(naive_bias_pct.mean()),\n        \"bias_pct_std\": float(naive_bias_pct.std(ddof=1)),\n    }\n    out[\"methods\"] = {}\n    naive_abs = np.mean(np.abs(naive_bias))\n    for key in method_keys:\n        vals = np.array([r[key] for r in reps])\n        valid = np.isfinite(vals)\n        if valid.sum() == 0:\n            out[\"methods\"][key] = None\n            continue\n        v = vals[valid]\n        bias = v - tau_true\n        bias_pct = 100.0 * bias / tau_true\n        abs_bias_mean = float(np.mean(np.abs(bias)))\n        improvement_pct = (\n            100.0 * (1.0 - abs_bias_mean / naive_abs)\n            if naive_abs > 1e-12 else float(\"nan\")\n        )\n        out[\"methods\"][key] = {\n            \"mean\": float(v.mean()),\n            \"std\": float(v.std(ddof=1)),\n            \"bias_mean\": float(bias.mean()),\n            \"bias_std\": float(bias.std(ddof=1)),\n            \"abs_bias_mean\": abs_bias_mean,\n            \"bias_pct_mean\": float(bias_pct.mean()),\n            \"bias_pct_std\": float(bias_pct.std(ddof=1)),\n            \"improvement_pct\": float(improvement_pct),\n            \"n_valid\": int(valid.sum()),\n        }\n    return out\n\n\ndef mean_C_hat(reps):\n    return np.mean(np.stack([r[\"C_hat\"] for r in reps]), axis=0)\n\n\ndef main():\n    t0 = time.time()\n    print(\"=\" * 70)\n    print(f\"Mini E2E demo: N={N}, K={K}, gold={int(N * GOLD_FRACTION)}, reps={N_REPS}\")\n    print(f\"C0 diag={C0.diagonal().tolist()}\")\n    print(\"=\" * 70)\n\n    rng_master = np.random.default_rng(SEED)\n\n    print(\"\\n[Confounding] target = treatment coefficient tau = 0.5\")\n    tau_true_conf = CONFOUNDING_PARAMS[\"beta_T\"]\n    conf_reps = []\n    for rep in range(N_REPS):\n        seed_rep = int(rng_master.integers(0, 2**31))\n        rng_rep = np.random.default_rng(seed_rep)\n        conf_reps.append(run_confounding_rep(rng_rep, tau_true_conf))\n        if (rep + 1) % 25 == 0:\n            print(f\"  rep {rep + 1}/{N_REPS}\")\n\n    print(\"\\n[Exposure] target = beta_1 = 1.0\")\n    tau_true_exp = EXPOSURE_PARAMS[\"beta\"][1]\n    exp_reps = []\n    for rep in range(N_REPS):\n        seed_rep = int(rng_master.integers(0, 2**31))\n        rng_rep = np.random.default_rng(seed_rep)\n        exp_reps.append(run_exposure_rep(rng_rep, tau_true_exp))\n        if (rep + 1) % 25 == 0:\n            print(f\"  rep {rep + 1}/{N_REPS}\")\n\n    conf_summary = compute_summary(\n        conf_reps,\n        method_keys=[\"tau_np\", \"tau_mla\"],\n        tau_true=tau_true_conf,\n    )\n    exp_summary = compute_summary(\n        exp_reps,\n        method_keys=[\"tau_ppi\"],\n        tau_true=tau_true_exp,\n    )\n\n    C_hat_conf_mean = mean_C_hat(conf_reps)\n    C_hat_exp_mean = mean_C_hat(exp_reps)\n\n    print(\"\\n[ASV] computing magnitude & sign-flip thresholds with mean Cˆ...\")\n    asv_conf_mag = compute_asv(\n        \"confounding\", C_hat_conf_mean, params=CONFOUNDING_PARAMS,\n        threshold_type=\"magnitude\", threshold_value=0.10,\n    )\n    asv_conf_sign = compute_asv(\n        \"confounding\", C_hat_conf_mean, params=CONFOUNDING_PARAMS,\n        threshold_type=\"sign_flip\",\n    )\n    asv_exp_mag = compute_asv(\n        \"exposure\", C_hat_exp_mean, params=EXPOSURE_PARAMS,\n        threshold_type=\"magnitude\", threshold_value=0.10,\n    )\n    asv_exp_sign = compute_asv(\n        \"exposure\", C_hat_exp_mean, params=EXPOSURE_PARAMS,\n        threshold_type=\"sign_flip\",\n    )\n\n    output = {\n        \"meta\": {\n            \"seed\": SEED,\n            \"N\": N,\n            \"K\": K,\n            \"gold_fraction\": GOLD_FRACTION,\n            \"n_reps\": N_REPS,\n            \"C0\": C0.tolist(),\n            \"confounding_params\": {\n                k: (v.tolist() if isinstance(v, np.ndarray) else v)\n                for k, v in CONFOUNDING_PARAMS.items()\n            },\n            \"exposure_params\": {\n                k: (v.tolist() if isinstance(v, np.ndarray) else v)\n                for k, v in EXPOSURE_PARAMS.items()\n            },\n        },\n        \"confounding\": {\n            **conf_summary,\n            \"routed_method\": \"no correction (FWL invariance)\",\n            \"C_hat_mean\": C_hat_conf_mean.tolist(),\n            \"asv_magnitude\": asv_conf_mag[\"asv\"],\n            \"asv_signflip\": asv_conf_sign[\"asv\"],\n            \"asv_tau_true_theoretical\": asv_conf_mag[\"tau_true\"],\n        },\n        \"exposure\": {\n            **exp_summary,\n            \"routed_method\": \"PPI++\",\n            \"C_hat_mean\": C_hat_exp_mean.tolist(),\n            \"asv_magnitude\": asv_exp_mag[\"asv\"],\n            \"asv_signflip\": asv_exp_sign[\"asv\"],\n            \"asv_tau_true_theoretical\": asv_exp_mag[\"tau_true\"],\n        },\n    }\n\n    out_json = os.path.join(PROJECT_ROOT, \"artifacts\", \"e2e_demo_results.json\")\n    with open(out_json, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nWrote {out_json}\")\n\n    write_latex_table(output)\n\n    print_console_summary(output)\n\n    print(f\"\\nElapsed: {time.time() - t0:.1f}s\")\n\n\ndef _fmt_asv(v):\n    return f\"{v:.3f}\" if v is not None else \"no crossing\"\n\n\ndef _fmt_pct(mean, std):\n    if not np.isfinite(mean):\n        return \"--\"\n    return f\"{mean:+.2f} $\\\\pm$ {std:.2f}\"\n\n\ndef write_latex_table(out):\n    conf = out[\"confounding\"]\n    exp = out[\"exposure\"]\n\n    conf_naive = conf[\"naive\"]\n    conf_np = conf[\"methods\"][\"tau_np\"]\n    conf_mla = conf[\"methods\"][\"tau_mla\"]\n    exp_naive = exp[\"naive\"]\n    exp_ppi = exp[\"methods\"][\"tau_ppi\"]\n\n    def _improve(m):\n        if m is None or not np.isfinite(m[\"improvement_pct\"]):\n            return \"--\"\n        return f\"{m['improvement_pct']:+.1f}\\\\%\"\n\n    def _bias_cell(m):\n        if m is None:\n            return \"--\"\n        return _fmt_pct(m[\"bias_pct_mean\"], m[\"bias_pct_std\"])\n\n    lines = []\n    lines.append(\"% Auto-generated by artifacts/e2e_demo.py\")\n    lines.append(\"\\\\begin{table}[t]\")\n    lines.append(\"\\\\centering\")\n    lines.append(\"\\\\small\")\n    lines.append(\"\\\\begin{tabular}{lrrlrr}\")\n    lines.append(\"\\\\toprule\")\n    lines.append(\n        \"Topology & Naive Bias (\\\\%) & ASV $\\\\delta^*_{\\\\mathrm{mag}}$ & \"\n        \"Routed Method & Corrected Bias (\\\\%) & Improvement (\\\\%) \\\\\\\\\"\n    )\n    lines.append(\"\\\\midrule\")\n\n    lines.append(\n        \"Confounding & \"\n        f\"{_fmt_pct(conf_naive['bias_pct_mean'], conf_naive['bias_pct_std'])} & \"\n        f\"{_fmt_asv(conf['asv_magnitude'])} & \"\n        \"no correction (FWL) & \"\n        f\"{_bias_cell(conf_np)} & {_improve(conf_np)} \\\\\\\\\"\n    )\n    lines.append(\n        \"\\\\quad (naive plug-in) & -- & -- & -- & \"\n        f\"{_bias_cell(conf_np)} & {_improve(conf_np)} \\\\\\\\\"\n    )\n    lines.append(\n        \"\\\\quad (MLA)          & -- & -- & -- & \"\n        f\"{_bias_cell(conf_mla)} & {_improve(conf_mla)} \\\\\\\\\"\n    )\n\n    lines.append(\n        \"Exposure & \"\n        f\"{_fmt_pct(exp_naive['bias_pct_mean'], exp_naive['bias_pct_std'])} & \"\n        f\"{_fmt_asv(exp['asv_magnitude'])} & \"\n        \"PPI++ & \"\n        f\"{_bias_cell(exp_ppi)} & {_improve(exp_ppi)} \\\\\\\\\"\n    )\n    lines.append(\"\\\\bottomrule\")\n    lines.append(\"\\\\end{tabular}\")\n    lines.append(\n        \"\\\\caption{End-to-end demo over \"\n        f\"{out['meta']['n_reps']} replicates \"\n        f\"(N={out['meta']['N']:,}, K={out['meta']['K']}, \"\n        f\"{int(out['meta']['gold_fraction']*100)}\\\\% gold). \"\n        \"Confounding: plug-in corrections leave the treatment coefficient \"\n        \"unchanged (FWL invariance), so Algorithm~1 routes to ``no correction''. \"\n        \"Exposure: PPI++ recovers the target coefficient using the gold subset.\"\n        \"}\"\n    )\n    lines.append(\"\\\\label{tab:e2e-demo}\")\n    lines.append(\"\\\\end{table}\")\n\n    out_tex = os.path.join(PROJECT_ROOT, \"artifacts\", \"e2e_demo_table.tex\")\n    with open(out_tex, \"w\") as f:\n        f.write(\"\\n\".join(lines) + \"\\n\")\n    print(f\"Wrote {out_tex}\")\n\n\ndef print_console_summary(out):\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SUMMARY\")\n    print(\"=\" * 70)\n    for topo in (\"confounding\", \"exposure\"):\n        s = out[topo]\n        print(f\"\\n[{topo}]  tau_true (empirical) = {s['tau_true']:.4f}\")\n        print(f\"  routed = {s['routed_method']}\")\n        nb = s[\"naive\"]\n        print(\n            f\"  naive       : tau = {nb['mean']:.4f} +/- {nb['std']:.4f}  \"\n            f\"bias = {nb['bias_pct_mean']:+.2f}% +/- {nb['bias_pct_std']:.2f}%\"\n        )\n        for key, m in s[\"methods\"].items():\n            if m is None:\n                print(f\"  {key:11s}: N/A\")\n                continue\n            print(\n                f\"  {key:11s}: tau = {m['mean']:.4f} +/- {m['std']:.4f}  \"\n                f\"bias = {m['bias_pct_mean']:+.2f}% +/- {m['bias_pct_std']:.2f}%  \"\n                f\"improvement = {m['improvement_pct']:+.1f}%\"\n            )\n        print(\n            f\"  ASV magnitude (10%) : {_fmt_asv(s['asv_magnitude'])}  |  \"\n            f\"ASV sign-flip : {_fmt_asv(s['asv_signflip'])}\"\n        )\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5b909af-f0f4-4641-b442-ddf99f4ca0ec",
  "isSidechain": false,
  "requestId": "req_011CbKfTn3NWocpbdZUXfMn3",
  "type": "assistant",
  "uuid": "99ef2d23-6cef-4607-9755-3094b24644a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01L9eyHGCqCE1wFPjjwKQSTo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5092,
      "cache_read_input_tokens": 62965,
      "output_tokens": 8053,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5092,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8053,
          "cache_read_input_tokens": 62965,
          "cache_creation_input_tokens": 5092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5092
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

_source line 39 · 2026-05-23T14:34:07.575Z_

<details><summary>↩ Tool result · `toolu_01VQ1tPhwZ9BHxdTK3a3mzFx`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99ef2d23-6cef-4607-9755-3094b24644a0",
  "isSidechain": false,
  "promptId": "d4f14da1-f244-4256-aa7c-b4a034dc23f5",
  "type": "user",
  "uuid": "dfe71302-bbe6-4eab-8f38-c960cd85b753",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nMini end-to-end demo: C estimation -> ASV diagnostic -> Algorithm 1 routing\n-> correction -> bias improvement.\n\nTwo topologies illustrate the dichotomy:\n  - confounding: FWL invariance => no plug-in correction helps the\n    treatment coefficient; routed method is \"no correction\".\n  - exposure: PPI++ recovers the target coefficient using a gold subset.\n\nPipeline for each topology:\n  1. Generate synthetic data with N=10000, K=3, known C0 (diag=0.7,\n     off-diagonal 0.15 uniform).\n  2. Sample 20% gold subset; estimate C_hat from gold (true vs. observed labels).\n  3. Compute ASV (magnitude & sign-flip) using C_hat as the base of the\n     interpolation path C(delta) = (1-delta) I + delta C_hat.\n  4. Algorithm 1 route:\n       - confounding => \"no correction (FWL)\"\n       - exposure    => \"PPI++\"\n  5. Apply correction(s); also run naive_plugin / MLA on confounding to\n     verify they do not move the treatment coefficient (FWL theorem).\n  6. Record naive bias, corrected bias, improvement.\n\n100 Monte Carlo replicates per topology (mean +/- std).\n\nOutputs:\n  - artifacts/e2e_demo_results.json\n  - artifacts/e2e_demo_table.tex\n\"\"\"\n\nimport json\nimport os\nimport sys\nimport time\n\nimport numpy as np\n\nPROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\nsys.path.insert(0, PROJECT_ROOT)\n\nfrom annot_sensitivity.asv import compute_asv\nfrom annot_sensitivity.correction import (\n    correct_mla,\n    correct_naive_plugin,\n    correct_ppi,\n)\nfrom annot_sensitivity.dgp import gen_confounding, gen_exposure\nfrom annot_sensitivity.utils import make_dummies, misclassify, ols_with_se\n\nSEED = 42\nN = 10_000\nK = 3\nGOLD_FRACTION = 0.20\nN_REPS = 100\n\nC0 = np.array([\n    [0.70, 0.15, 0.15],\n    [0.15, 0.70, 0.15],\n    [0.15, 0.15, 0.70],\n])\n\nCONFOUNDING_PARAMS = {\n    \"p_A\": np.array([0.40, 0.35, 0.25]),\n    \"alpha\": np.array([0.6, -0.3]),\n    \"beta_A\": np.array([0.8, -0.4]),\n    \"beta_T\": 0.5,\n    \"sigma_T\": 1.0,\n}\n\nEXPOSURE_PARAMS = {\n    \"p_A\": np.array([0.40, 0.35, 0.25]),\n    \"beta\": np.array([0.0, 1.0, -0.5]),\n}\n\n\ndef estimate_C(A_true_gold, A_star_gold, K):\n    \"\"\"Column-stochastic Cˆ[j,k] = P(A* = j | A = k) from gold labels.\"\"\"\n    C_hat = np.zeros((K, K))\n    for k in range(K):\n        mask = A_true_gold == k\n        if mask.sum() > 0:\n            for j in range(K):\n                C_hat[j, k] = (A_star_gold[mask] == j).sum() / mask.sum()\n        else:\n            C_hat[k, k] = 1.0\n    return C_hat\n\n\ndef naive_confounding(X_other, Y, Astar, K, tau_idx=1):\n    D = make_dummies(Astar, K)\n    X = np.column_stack([X_other, D])\n    beta, se = ols_with_se(X, Y)\n    return float(beta[tau_idx]), float(se[tau_idx])\n\n\ndef naive_exposure(Y, Astar, K, tau_idx=1):\n    N_ = len(Y)\n    X_other = np.ones((N_, 1))\n    D = make_dummies(Astar, K)\n    X = np.column_stack([X_other, D])\n    beta, se = ols_with_se(X, Y)\n    return float(beta[tau_idx]), float(se[tau_idx])\n\n\ndef run_confounding_rep(rng, tau_true):\n    data = gen_confounding(N, params=CONFOUNDING_PARAMS, rng=rng)\n    T, Y, A = data[\"T\"], data[\"Y\"], data[\"A\"]\n    Astar = misclassify(A, C0, rng)\n\n    gold_idx = rng.choice(N, size=int(N * GOLD_FRACTION), replace=False)\n    gold_mask = np.zeros(N, dtype=bool)\n    gold_mask[gold_idx] = True\n    C_hat = estimate_C(A[gold_mask], Astar[gold_mask], K)\n\n    X_other = np.column_stack([np.ones(N), T])\n\n    tau_naive, _ = naive_confounding(X_other, Y, Astar, K, tau_idx=1)\n    tau_np, _, ok_np = correct_naive_plugin(X_other, Y, Astar, C_hat, tau_idx=1)\n    tau_mla, _, ok_mla = correct_mla(X_other, Y, Astar, C_hat, tau_idx=1)\n\n    return {\n        \"tau_naive\": tau_naive,\n        \"tau_np\": tau_np if ok_np else np.nan,\n        \"tau_mla\": tau_mla if ok_mla else np.nan,\n        \"C_hat\": C_hat,\n        \"tau_true\": tau_true,\n    }\n\n\ndef run_exposure_rep(rng, tau_true):\n    data = gen_exposure(N, params=EXPOSURE_PARAMS, rng=rng)\n    Y, A = data[\"Y\"], data[\"A\"]\n    Astar = misclassify(A, C0, rng)\n\n    gold_idx = rng.choice(N, size=int(N * GOLD_FRACTION), replace=False)\n    gold_mask = np.zeros(N, dtype=bool)\n    gold_mask[gold_idx] = True\n    C_hat = estimate_C(A[gold_mask], Astar[gold_mask], K)\n\n    X_other = np.ones((N, 1))\n    tau_naive, _ = naive_exposure(Y, Astar, K, tau_idx=1)\n    tau_ppi, _, ok_ppi = correct_ppi(X_other, Y, Astar, A, gold_mask,\n                                     tau_idx=1, rng=rng)\n\n    return {\n        \"tau_naive\": tau_naive,\n        \"tau_ppi\": tau_ppi if ok_ppi else np.nan,\n        \"C_hat\": C_hat,\n        \"tau_true\": tau_true,\n    }\n\n\ndef compute_summary(reps, method_keys, tau_true):\n    out = {\"tau_true\": float(tau_true)}\n    naive = np.array([r[\"tau_naive\"] for r in reps])\n    naive_bias = naive - tau_true\n    naive_bias_pct = 100.0 * naive_bias / tau_true\n    out[\"naive\"] = {\n        \"mean\": float(naive.mean()),\n        \"std\": float(naive.std(ddof=1)),\n        \"bias_mean\": float(naive_bias.mean()),\n        \"bias_std\": float(naive_bias.std(ddof=1)),\n        \"abs_bias_mean\": float(np.mean(np.abs(naive_bias))),\n        \"bias_pct_mean\": float(naive_bias_pct.mean()),\n        \"bias_pct_std\": float(naive_bias_pct.std(ddof=1)),\n    }\n    out[\"methods\"] = {}\n    naive_abs = np.mean(np.abs(naive_bias))\n    for key in method_keys:\n        vals = np.array([r[key] for r in reps])\n        valid = np.isfinite(vals)\n        if valid.sum() == 0:\n            out[\"methods\"][key] = None\n            continue\n        v = vals[valid]\n        bias = v - tau_true\n        bias_pct = 100.0 * bias / tau_true\n        abs_bias_mean = float(np.mean(np.abs(bias)))\n        improvement_pct = (\n            100.0 * (1.0 - abs_bias_mean / naive_abs)\n            if naive_abs > 1e-12 else float(\"nan\")\n        )\n        out[\"methods\"][key] = {\n            \"mean\": float(v.mean()),\n            \"std\": float(v.std(ddof=1)),\n            \"bias_mean\": float(bias.mean()),\n            \"bias_std\": float(bias.std(ddof=1)),\n            \"abs_bias_mean\": abs_bias_mean,\n            \"bias_pct_mean\": float(bias_pct.mean()),\n            \"bias_pct_std\": float(bias_pct.std(ddof=1)),\n            \"improvement_pct\": float(improvement_pct),\n            \"n_valid\": int(valid.sum()),\n        }\n    return out\n\n\ndef mean_C_hat(reps):\n    return np.mean(np.stack([r[\"C_hat\"] for r in reps]), axis=0)\n\n\ndef main():\n    t0 = time.time()\n    print(\"=\" * 70)\n    print(f\"Mini E2E demo: N={N}, K={K}, gold={int(N * GOLD_FRACTION)}, reps={N_REPS}\")\n    print(f\"C0 diag={C0.diagonal().tolist()}\")\n    print(\"=\" * 70)\n\n    rng_master = np.random.default_rng(SEED)\n\n    print(\"\\n[Confounding] target = treatment coefficient tau = 0.5\")\n    tau_true_conf = CONFOUNDING_PARAMS[\"beta_T\"]\n    conf_reps = []\n    for rep in range(N_REPS):\n        seed_rep = int(rng_master.integers(0, 2**31))\n        rng_rep = np.random.default_rng(seed_rep)\n        conf_reps.append(run_confounding_rep(rng_rep, tau_true_conf))\n        if (rep + 1) % 25 == 0:\n            print(f\"  rep {rep + 1}/{N_REPS}\")\n\n    print(\"\\n[Exposure] target = beta_1 = 1.0\")\n    tau_true_exp = EXPOSURE_PARAMS[\"beta\"][1]\n    exp_reps = []\n    for rep in range(N_REPS):\n        seed_rep = int(rng_master.integers(0, 2**31))\n        rng_rep = np.random.default_rng(seed_rep)\n        exp_reps.append(run_exposure_rep(rng_rep, tau_true_exp))\n        if (rep + 1) % 25 == 0:\n            print(f\"  rep {rep + 1}/{N_REPS}\")\n\n    conf_summary = compute_summary(\n        conf_reps,\n        method_keys=[\"tau_np\", \"tau_mla\"],\n        tau_true=tau_true_conf,\n    )\n    exp_summary = compute_summary(\n        exp_reps,\n        method_keys=[\"tau_ppi\"],\n        tau_true=tau_true_exp,\n    )\n\n    C_hat_conf_mean = mean_C_hat(conf_reps)\n    C_hat_exp_mean = mean_C_hat(exp_reps)\n\n    print(\"\\n[ASV] computing magnitude & sign-flip thresholds with mean Cˆ...\")\n    asv_conf_mag = compute_asv(\n        \"confounding\", C_hat_conf_mean, params=CONFOUNDING_PARAMS,\n        threshold_type=\"magnitude\", threshold_value=0.10,\n    )\n    asv_conf_sign = compute_asv(\n        \"confounding\", C_hat_conf_mean, params=CONFOUNDING_PARAMS,\n        threshold_type=\"sign_flip\",\n    )\n    asv_exp_mag = compute_asv(\n        \"exposure\", C_hat_exp_mean, params=EXPOSURE_PARAMS,\n        threshold_type=\"magnitude\", threshold_value=0.10,\n    )\n    asv_exp_sign = compute_asv(\n        \"exposure\", C_hat_exp_mean, params=EXPOSURE_PARAMS,\n        threshold_type=\"sign_flip\",\n    )\n\n    output = {\n        \"meta\": {\n            \"seed\": SEED,\n            \"N\": N,\n            \"K\": K,\n            \"gold_fraction\": GOLD_FRACTION,\n            \"n_reps\": N_REPS,\n            \"C0\": C0.tolist(),\n            \"confounding_params\": {\n                k: (v.tolist() if isinstance(v, np.ndarray) else v)\n                for k, v in CONFOUNDING_PARAMS.items()\n            },\n            \"exposure_params\": {\n                k: (v.tolist() if isinstance(v, np.ndarray) else v)\n                for k, v in EXPOSURE_PARAMS.items()\n            },\n        },\n        \"confounding\": {\n            **conf_summary,\n            \"routed_method\": \"no correction (FWL invariance)\",\n            \"C_hat_mean\": C_hat_conf_mean.tolist(),\n            \"asv_magnitude\": asv_conf_mag[\"asv\"],\n            \"asv_signflip\": asv_conf_sign[\"asv\"],\n            \"asv_tau_true_theoretical\": asv_conf_mag[\"tau_true\"],\n        },\n        \"exposure\": {\n            **exp_summary,\n            \"routed_method\": \"PPI++\",\n            \"C_hat_mean\": C_hat_exp_mean.tolist(),\n            \"asv_magnitude\": asv_exp_mag[\"asv\"],\n            \"asv_signflip\": asv_exp_sign[\"asv\"],\n            \"asv_tau_true_theoretical\": asv_exp_mag[\"tau_true\"],\n        },\n    }\n\n    out_json = os.path.join(PROJECT_ROOT, \"artifacts\", \"e2e_demo_results.json\")\n    with open(out_json, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nWrote {out_json}\")\n\n    write_latex_table(output)\n\n    print_console_summary(output)\n\n    print(f\"\\nElapsed: {time.time() - t0:.1f}s\")\n\n\ndef _fmt_asv(v):\n    return f\"{v:.3f}\" if v is not None else \"no crossing\"\n\n\ndef _fmt_pct(mean, std):\n    if not np.isfinite(mean):\n        return \"--\"\n    return f\"{mean:+.2f} $\\\\pm$ {std:.2f}\"\n\n\ndef write_latex_table(out):\n    conf = out[\"confounding\"]\n    exp = out[\"exposure\"]\n\n    conf_naive = conf[\"naive\"]\n    conf_np = conf[\"methods\"][\"tau_np\"]\n    conf_mla = conf[\"methods\"][\"tau_mla\"]\n    exp_naive = exp[\"naive\"]\n    exp_ppi = exp[\"methods\"][\"tau_ppi\"]\n\n    def _improve(m):\n        if m is None or not np.isfinite(m[\"improvement_pct\"]):\n            return \"--\"\n        return f\"{m['improvement_pct']:+.1f}\\\\%\"\n\n    def _bias_cell(m):\n        if m is None:\n            return \"--\"\n        return _fmt_pct(m[\"bias_pct_mean\"], m[\"bias_pct_std\"])\n\n    lines = []\n    lines.append(\"% Auto-generated by artifacts/e2e_demo.py\")\n    lines.append(\"\\\\begin{table}[t]\")\n    lines.append(\"\\\\centering\")\n    lines.append(\"\\\\small\")\n    lines.append(\"\\\\begin{tabular}{lrrlrr}\")\n    lines.append(\"\\\\toprule\")\n    lines.append(\n        \"Topology & Naive Bias (\\\\%) & ASV $\\\\delta^*_{\\\\mathrm{mag}}$ & \"\n        \"Routed Method & Corrected Bias (\\\\%) & Improvement (\\\\%) \\\\\\\\\"\n    )\n    lines.append(\"\\\\midrule\")\n\n    lines.append(\n        \"Confounding & \"\n        f\"{_fmt_pct(conf_naive['bias_pct_mean'], conf_naive['bias_pct_std'])} & \"\n        f\"{_fmt_asv(conf['asv_magnitude'])} & \"\n        \"no correction (FWL) & \"\n        f\"{_bias_cell(conf_np)} & {_improve(conf_np)} \\\\\\\\\"\n    )\n    lines.append(\n        \"\\\\quad (naive plug-in) & -- & -- & -- & \"\n        f\"{_bias_cell(conf_np)} & {_improve(conf_np)} \\\\\\\\\"\n    )\n    lines.append(\n        \"\\\\quad (MLA)          & -- & -- & -- & \"\n        f\"{_bias_cell(conf_mla)} & {_improve(conf_mla)} \\\\\\\\\"\n    )\n\n    lines.append(\n        \"Exposure & \"\n        f\"{_fmt_pct(exp_naive['bias_pct_mean'], exp_naive['bias_pct_std'])} & \"\n        f\"{_fmt_asv(exp['asv_magnitude'])} & \"\n        \"PPI++ & \"\n        f\"{_bias_cell(exp_ppi)} & {_improve(exp_ppi)} \\\\\\\\\"\n    )\n    lines.append(\"\\\\bottomrule\")\n    lines.append(\"\\\\end{tabular}\")\n    lines.append(\n        \"\\\\caption{End-to-end demo over \"\n        f\"{out['meta']['n_reps']} replicates \"\n        f\"(N={out['meta']['N']:,}, K={out['meta']['K']}, \"\n        f\"{int(out['meta']['gold_fraction']*100)}\\\\% gold). \"\n        \"Confounding: plug-in corrections leave the treatment coefficient \"\n        \"unchanged (FWL invariance), so Algorithm~1 routes to ``no correction''. \"\n        \"Exposure: PPI++ recovers the target coefficient using the gold subset.\"\n        \"}\"\n    )\n    lines.append(\"\\\\label{tab:e2e-demo}\")\n    lines.append(\"\\\\end{table}\")\n\n    out_tex = os.path.join(PROJECT_ROOT, \"artifacts\", \"e2e_demo_table.tex\")\n    with open(out_tex, \"w\") as f:\n        f.write(\"\\n\".join(lines) + \"\\n\")\n    print(f\"Wrote {out_tex}\")\n\n\ndef print_console_summary(out):\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SUMMARY\")\n    print(\"=\" * 70)\n    for topo in (\"confounding\", \"exposure\"):\n        s = out[topo]\n        print(f\"\\n[{topo}]  tau_true (empirical) = {s['tau_true']:.4f}\")\n        print(f\"  routed = {s['routed_method']}\")\n        nb = s[\"naive\"]\n        print(\n            f\"  naive       : tau = {nb['mean']:.4f} +/- {nb['std']:.4f}  \"\n            f\"bias = {nb['bias_pct_mean']:+.2f}% +/- {nb['bias_pct_std']:.2f}%\"\n        )\n        for key, m in s[\"methods\"].items():\n            if m is None:\n                print(f\"  {key:11s}: N/A\")\n                continue\n            print(\n                f\"  {key:11s}: tau = {m['mean']:.4f} +/- {m['std']:.4f}  \"\n                f\"bias = {m['bias_pct_mean']:+.2f}% +/- {m['bias_pct_std']:.2f}%  \"\n                f\"improvement = {m['improvement_pct']:+.1f}%\"\n            )\n        print(\n            f\"  ASV magnitude (10%) : {_fmt_asv(s['asv_magnitude'])}  |  \"\n            f\"ASV sign-flip : {_fmt_asv(s['asv_signflip'])}\"\n        )\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "99ef2d23-6cef-4607-9755-3094b24644a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 40 · 2026-05-23T14:34:07.578Z_

```json
{
  "parentUuid": "dfe71302-bbe6-4eab-8f38-c960cd85b753",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "61ff8f4e-5b31-4e88-94c1-6b64d382cddb",
  "timestamp": "2026-05-23T14:34:07.578Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "leafUuid": "61ff8f4e-5b31-4e88-94c1-6b64d382cddb",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Build mini end-to-end demo for causal annotation error",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa"
}
```

---

### Assistant

_source line 43 · 2026-05-23T14:34:14.025Z_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61ff8f4e-5b31-4e88-94c1-6b64d382cddb",
  "isSidechain": false,
  "requestId": "req_011CbKfaKNCzHxEj21dW4b7y",
  "type": "assistant",
  "uuid": "df2da6ac-7219-43bd-90b3-b96cbf2f1557",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015Ju9b9M1fJE8Xrtrx1HUPX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8279,
      "cache_read_input_tokens": 68057,
      "output_tokens": 570,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8279,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 570,
          "cache_read_input_tokens": 68057,
          "cache_creation_input_tokens": 8279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8279
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

_source line 44 · 2026-05-23T14:34:16.159Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01NSK47q3sr7zqoA3X4Xa28j`</summary>

```json
{
  "command": "python -c \"\nimport sys, os\nPROJECT_ROOT = '/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib'\nsys.path.insert(0, PROJECT_ROOT)\n# Patch N_REPS for quick smoke test\nimport artifacts.e2e_demo as m\nm.N_REPS = 5\nm.main()\n\" 2>&1 | tail -60",
  "description": "Smoke test with 5 reps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df2da6ac-7219-43bd-90b3-b96cbf2f1557",
  "isSidechain": false,
  "requestId": "req_011CbKfaKNCzHxEj21dW4b7y",
  "type": "assistant",
  "uuid": "62173cad-2736-45c1-a079-7292e254dce0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015Ju9b9M1fJE8Xrtrx1HUPX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8279,
      "cache_read_input_tokens": 68057,
      "output_tokens": 570,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8279,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 570,
          "cache_read_input_tokens": 68057,
          "cache_creation_input_tokens": 8279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8279
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

_source line 45 · 2026-05-23T14:34:16.211Z_

<details><summary>↩ Tool result · `toolu_01NSK47q3sr7zqoA3X4Xa28j`</summary>

```text
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62173cad-2736-45c1-a079-7292e254dce0",
  "isSidechain": false,
  "promptId": "d4f14da1-f244-4256-aa7c-b4a034dc23f5",
  "type": "user",
  "uuid": "e7f5b56e-a80c-4ff9-ab27-bea0f3c17bf0",
  "toolUseResult": {
    "stdout": "/bin/bash: line 1: python: command not found",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "62173cad-2736-45c1-a079-7292e254dce0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-23T14:34:19.675Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WG4cST3xPd2YpmKscTAKwh`</summary>

```json
{
  "command": "which python3 && python3 -c \"\nimport sys, os\nPROJECT_ROOT = '/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib'\nsys.path.insert(0, PROJECT_ROOT)\nimport artifacts.e2e_demo as m\nm.N_REPS = 5\nm.main()\n\" 2>&1 | tail -80",
  "description": "Smoke test with 5 reps via python3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7f5b56e-a80c-4ff9-ab27-bea0f3c17bf0",
  "isSidechain": false,
  "requestId": "req_011CbKfaxGixj9w3CYHzaDLy",
  "type": "assistant",
  "uuid": "7f0eb891-3213-4435-9be2-e3ea42e600e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FxUvQdfyRyajdzruM9avNW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 557,
      "cache_read_input_tokens": 76336,
      "output_tokens": 231,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 557,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 231,
          "cache_read_input_tokens": 76336,
          "cache_creation_input_tokens": 557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 557
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

_source line 47 · 2026-05-23T14:34:20.914Z_

<details><summary>↩ Tool result · `toolu_01WG4cST3xPd2YpmKscTAKwh`</summary>

```text
/usr/bin/python3
======================================================================
Mini E2E demo: N=10000, K=3, gold=2000, reps=5
C0 diag=[0.7, 0.7, 0.7]
======================================================================

[Confounding] target = treatment coefficient tau = 0.5

[Exposure] target = beta_1 = 1.0

[ASV] computing magnitude & sign-flip thresholds with mean Cˆ...

Wrote /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_results.json
Wrote /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_table.tex

======================================================================
SUMMARY
======================================================================

[confounding]  tau_true (empirical) = 0.5000
  routed = no correction (FWL invariance)
  naive       : tau = 0.6149 +/- 0.0077  bias = +22.99% +/- 1.53%
  tau_np     : tau = 0.6149 +/- 0.0077  bias = +22.99% +/- 1.53%  improvement = -0.0%
  tau_mla    : tau = 0.6149 +/- 0.0077  bias = +22.99% +/- 1.53%  improvement = -0.0%
  ASV magnitude (10%) : 0.365  |  ASV sign-flip : no crossing

[exposure]  tau_true (empirical) = 1.0000
  routed = PPI++
  naive       : tau = 0.5898 +/- 0.0265  bias = -41.02% +/- 2.65%
  tau_ppi    : tau = 0.9866 +/- 0.0427  bias = -1.34% +/- 4.27%  improvement = +91.5%
  ASV magnitude (10%) : 0.243  |  ASV sign-flip : 2.200

Elapsed: 1.1s
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7f0eb891-3213-4435-9be2-e3ea42e600e8",
  "isSidechain": false,
  "promptId": "d4f14da1-f244-4256-aa7c-b4a034dc23f5",
  "type": "user",
  "uuid": "e4843030-a147-4543-bd74-739e75828da7",
  "toolUseResult": {
    "stdout": "/usr/bin/python3\n======================================================================\nMini E2E demo: N=10000, K=3, gold=2000, reps=5\nC0 diag=[0.7, 0.7, 0.7]\n======================================================================\n\n[Confounding] target = treatment coefficient tau = 0.5\n\n[Exposure] target = beta_1 = 1.0\n\n[ASV] computing magnitude & sign-flip thresholds with mean Cˆ...\n\nWrote /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_results.json\nWrote /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_table.tex\n\n======================================================================\nSUMMARY\n======================================================================\n\n[confounding]  tau_true (empirical) = 0.5000\n  routed = no correction (FWL invariance)\n  naive       : tau = 0.6149 +/- 0.0077  bias = +22.99% +/- 1.53%\n  tau_np     : tau = 0.6149 +/- 0.0077  bias = +22.99% +/- 1.53%  improvement = -0.0%\n  tau_mla    : tau = 0.6149 +/- 0.0077  bias = +22.99% +/- 1.53%  improvement = -0.0%\n  ASV magnitude (10%) : 0.365  |  ASV sign-flip : no crossing\n\n[exposure]  tau_true (empirical) = 1.0000\n  routed = PPI++\n  naive       : tau = 0.5898 +/- 0.0265  bias = -41.02% +/- 2.65%\n  tau_ppi    : tau = 0.9866 +/- 0.0427  bias = -1.34% +/- 4.27%  improvement = +91.5%\n  ASV magnitude (10%) : 0.243  |  ASV sign-flip : 2.200\n\nElapsed: 1.1s",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7f0eb891-3213-4435-9be2-e3ea42e600e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-23T14:34:24.407Z_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4843030-a147-4543-bd74-739e75828da7",
  "isSidechain": false,
  "requestId": "req_011CbKfbJMTehNxEWQaVzovA",
  "type": "assistant",
  "uuid": "07bba124-3563-4f27-81a2-579fdc501b44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FKwwh4rg9NKuR4QZRPCPjr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 914,
      "cache_read_input_tokens": 76893,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 914,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 76893,
          "cache_creation_input_tokens": 914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 914
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

_source line 49 · 2026-05-23T14:34:24.936Z_

Smoke test passes. Now full 100 reps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07bba124-3563-4f27-81a2-579fdc501b44",
  "isSidechain": false,
  "requestId": "req_011CbKfbJMTehNxEWQaVzovA",
  "type": "assistant",
  "uuid": "3ffa294b-974b-4b7a-9265-0840e916aaed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FKwwh4rg9NKuR4QZRPCPjr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 914,
      "cache_read_input_tokens": 76893,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 914,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 76893,
          "cache_creation_input_tokens": 914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 914
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

_source line 50 · 2026-05-23T14:34:25.805Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01TQ2Gq7iwFcpZGuMxtrvY5x`</summary>

```json
{
  "command": "python3 artifacts/e2e_demo.py 2>&1 | tail -60",
  "description": "Run full 100-rep e2e demo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ffa294b-974b-4b7a-9265-0840e916aaed",
  "isSidechain": false,
  "requestId": "req_011CbKfbJMTehNxEWQaVzovA",
  "type": "assistant",
  "uuid": "ea07cb18-3e4c-44ef-859d-115cd31b304d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FKwwh4rg9NKuR4QZRPCPjr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 914,
      "cache_read_input_tokens": 76893,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 914,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 76893,
          "cache_creation_input_tokens": 914,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 914
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

_source line 51 · 2026-05-23T14:34:29.400Z_

<details><summary>↩ Tool result · `toolu_01TQ2Gq7iwFcpZGuMxtrvY5x`</summary>

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
  "parentUuid": "ea07cb18-3e4c-44ef-859d-115cd31b304d",
  "isSidechain": false,
  "promptId": "d4f14da1-f244-4256-aa7c-b4a034dc23f5",
  "type": "user",
  "uuid": "21f3063e-6f74-4ed9-9749-317cb4dc6091",
  "toolUseResult": {
    "stdout": "======================================================================\nMini E2E demo: N=10000, K=3, gold=2000, reps=100\nC0 diag=[0.7, 0.7, 0.7]\n======================================================================\n\n[Confounding] target = treatment coefficient tau = 0.5\n  rep 25/100\n  rep 50/100\n  rep 75/100\n  rep 100/100\n\n[Exposure] target = beta_1 = 1.0\n  rep 25/100\n  rep 50/100\n  rep 75/100\n  rep 100/100\n\n[ASV] computing magnitude & sign-flip thresholds with mean Cˆ...\n\nWrote /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_results.json\nWrote /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_table.tex\n\n======================================================================\nSUMMARY\n======================================================================\n\n[confounding]  tau_true (empirical) = 0.5000\n  routed = no correction (FWL invariance)\n  naive       : tau = 0.6136 +/- 0.0114  bias = +22.71% +/- 2.29%\n  tau_np     : tau = 0.6136 +/- 0.0114  bias = +22.71% +/- 2.29%  improvement = +0.0%\n  tau_mla    : tau = 0.6136 +/- 0.0114  bias = +22.71% +/- 2.29%  improvement = +0.0%\n  ASV magnitude (10%) : 0.352  |  ASV sign-flip : no crossing\n\n[exposure]  tau_true (empirical) = 1.0000\n  routed = PPI++\n  naive       : tau = 0.5713 +/- 0.0242  bias = -42.87% +/- 2.42%\n  tau_ppi    : tau = 0.9978 +/- 0.0494  bias = -0.22% +/- 4.94%  improvement = +90.9%\n  ASV magnitude (10%) : 0.239  |  ASV sign-flip : 2.220\n\nElapsed: 3.4s",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "ea07cb18-3e4c-44ef-859d-115cd31b304d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-23T14:34:31.755Z_

<details open><summary>🔧 Tool call — Read · `toolu_0144FKZwBzVF4nVnWDpypZGN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21f3063e-6f74-4ed9-9749-317cb4dc6091",
  "isSidechain": false,
  "requestId": "req_011CbKfbvdXmWkLtDQHmU4zx",
  "type": "assistant",
  "uuid": "6e00e712-eb83-47e3-a742-078e069de798",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016gi5UEEe1L4QNuKFqWHFr3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1040,
      "cache_read_input_tokens": 77807,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 118,
          "cache_read_input_tokens": 77807,
          "cache_creation_input_tokens": 1040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1040
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

_source line 53 · 2026-05-23T14:34:31.760Z_

<details><summary>↩ Tool result · `toolu_0144FKZwBzVF4nVnWDpypZGN`</summary>

```text
1	% Auto-generated by artifacts/e2e_demo.py
2	\begin{table}[t]
3	\centering
4	\small
5	\begin{tabular}{lrrlrr}
6	\toprule
7	Topology & Naive Bias (\%) & ASV $\delta^*_{\mathrm{mag}}$ & Routed Method & Corrected Bias (\%) & Improvement (\%) \\
8	\midrule
9	Confounding & +22.71 $\pm$ 2.29 & 0.352 & no correction (FWL) & +22.71 $\pm$ 2.29 & +0.0\% \\
10	\quad (naive plug-in) & -- & -- & -- & +22.71 $\pm$ 2.29 & +0.0\% \\
11	\quad (MLA)          & -- & -- & -- & +22.71 $\pm$ 2.29 & +0.0\% \\
12	Exposure & -42.87 $\pm$ 2.42 & 0.239 & PPI++ & -0.22 $\pm$ 4.94 & +90.9\% \\
13	\bottomrule
14	\end{tabular}
15	\caption{End-to-end demo over 100 replicates (N=10,000, K=3, 20\% gold). Confounding: plug-in corrections leave the treatment coefficient unchanged (FWL invariance), so Algorithm~1 routes to ``no correction''. Exposure: PPI++ recovers the target coefficient using the gold subset.}
16	\label{tab:e2e-demo}
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e00e712-eb83-47e3-a742-078e069de798",
  "isSidechain": false,
  "promptId": "d4f14da1-f244-4256-aa7c-b4a034dc23f5",
  "type": "user",
  "uuid": "ca7c9145-ee89-400d-9341-80086d9e1392",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/e2e_demo_table.tex",
      "content": "% Auto-generated by artifacts/e2e_demo.py\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrlrr}\n\\toprule\nTopology & Naive Bias (\\%) & ASV $\\delta^*_{\\mathrm{mag}}$ & Routed Method & Corrected Bias (\\%) & Improvement (\\%) \\\\\n\\midrule\nConfounding & +22.71 $\\pm$ 2.29 & 0.352 & no correction (FWL) & +22.71 $\\pm$ 2.29 & +0.0\\% \\\\\n\\quad (naive plug-in) & -- & -- & -- & +22.71 $\\pm$ 2.29 & +0.0\\% \\\\\n\\quad (MLA)          & -- & -- & -- & +22.71 $\\pm$ 2.29 & +0.0\\% \\\\\nExposure & -42.87 $\\pm$ 2.42 & 0.239 & PPI++ & -0.22 $\\pm$ 4.94 & +90.9\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{End-to-end demo over 100 replicates (N=10,000, K=3, 20\\% gold). Confounding: plug-in corrections leave the treatment coefficient unchanged (FWL invariance), so Algorithm~1 routes to ``no correction''. Exposure: PPI++ recovers the target coefficient using the gold subset.}\n\\label{tab:e2e-demo}\n\\end{table}\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  },
  "sourceToolAssistantUUID": "6e00e712-eb83-47e3-a742-078e069de798",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-23T14:34:39.508Z_

Done. Results match expectations.

**Summary (100 reps, N=10,000, K=3, 20% gold):**

| Topology | Naive bias | ASV δ*ₘₐg | Routed | Corrected bias | Improvement |
|---|---|---|---|---|---|
| Confounding (τ=0.5) | +22.71% ± 2.29% | 0.352 | no correction (FWL) | +22.71% (naive_plugin/MLA both) | +0.0% |
| Exposure (β₁=1.0) | −42.87% ± 2.42% | 0.239 | PPI++ | −0.22% ± 4.94% | **+90.9%** |

- Confounding: naive_plugin and MLA give *exactly* the same τ̂ as naive (FWL invariance demonstrated empirically); Algorithm 1 correctly routes to "no correction".
- Exposure: PPI++ recovers β₁ to within 0.2% of truth using 2,000 gold labels.
- ASV magnitude crossing is meaningfully smaller for exposure (0.239 → more sensitive) than confounding (0.352). Confounding has no sign-flip crossing within the valid δ range; exposure does at δ=2.22.

**Artifacts written:**
- `artifacts/e2e_demo.py`
- `artifacts/e2e_demo_results.json`
- `artifacts/e2e_demo_table.tex`

Total runtime: 3.4s.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca7c9145-ee89-400d-9341-80086d9e1392",
  "isSidechain": false,
  "requestId": "req_011CbKfc7FkNc5tu4EuiNSBh",
  "type": "assistant",
  "uuid": "2750583d-385e-4c62-837a-37d38ff8dcc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HLCJ3ozEQtUBVh8voDVshz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 78847,
      "output_tokens": 494,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 667,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 494,
          "cache_read_input_tokens": 78847,
          "cache_creation_input_tokens": 667,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 667
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

_source line 55_

```json
{
  "type": "last-prompt",
  "leafUuid": "2750583d-385e-4c62-837a-37d38ff8dcc1",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Build mini end-to-end demo for causal annotation error",
  "sessionId": "c98dbbb7-289c-4874-8b26-c493fcfcccfa"
}
```

---
