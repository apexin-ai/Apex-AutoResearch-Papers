# Research conversation: <project_context> # 项目: structfuse-context ## 运行环境 - 服务器名: bjb1-42106 - SSH 账户: root（调用 ssh_execute / submit_training_jo

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/559ab8d5-54a8-4e66-9e37-55b92c9e8c98.jsonl`
- **Structured JSON:** [`56b68647fd691907cbb6.json`](../../sessions/56/56b68647fd691907cbb6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T09:58:36.289Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T09:58:36.289Z",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "content": "&lt;project_context>\n# 项目: structfuse-context\n\n## 运行环境\n- 服务器名: bjb1-42106\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.bjb1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/structfuse\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：Related Work v1 修正（4 项）\n\n修改文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md`\n\n同时需要参考 Introduction 文件（只读，不修改）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md`\n\n### 修正 1 [WARNING]：GraphCoder/ARISE scope 事实核实\n\n用 WebSearch 查阅以下两篇论文原文，确认 data-flow scope：\n- **GraphCoder** (ASE 2024, Liu et al.) — 当前文中写 \"limited to intra-procedural scope\"\n- **ARISE** (arXiv 2605.03117, Seddik et al., 2026) — 当前文中同样写 \"limited to intra-procedural scope\"\n\n确认：它们是否真的限于 intra-procedural？如果有 inter-procedural 组件，改为 \"primarily intra-procedural\" 或更精确描述。这是审稿人容易攻击的事实性断言。\n\n当前原文（§2.4 倒数第二句）：\n> \"GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope.\"\n\n### 修正 2 [WARNING]：\"all these methods\" 断言软化\n\n当前原文（§2.4 最后一段）：\n> \"Critically, all these methods construct and query graphs at inference time\"\n\n改为：\n> \"Critically, these methods primarily leverage structural graphs at inference time\"\n\n除非你通过 WebSearch 逐一确认了 6 个系统（CodexGraph, RepoGraph, LocAgent, RANGER, GraphCoder, ARISE）全部只在推理时用图，否则必须软化。\n\n### 修正 3 [INFO]：CoCoHaNeRe 双重描述统一\n\n问题：Introduction 说 CoCoHaNeRe \"argues that non-differentiable embedding-based negatives are 'slow and ineffective'\"（批评 embedding negatives），但 Related Work §2.3 说 \"reports that BM25-selected negatives can be detrimental\"（批评 BM25 negatives）。两处描述不一致，读者会困惑。\n\n在 §2.3 CoCoHaNeRe 那句后面加一句，说明 CoCoHaNeRe 同时研究了多种非梯度负样本挖掘方法（包括 BM25 和 embedding-based），消除读者困惑。不要改 Introduction 的措辞。\n\n### 修正 4 [INFO]：GraphCodeBERT 区分强化\n\n§2.2 最后两句目前：\n> \"GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension...\"\n\n在 \"StructFuse addresses a complementary dimension\" 前加半句，明确区分 \"pretraining objective (GraphCodeBERT) vs training-time negative selection (StructFuse)\"。类似：\n> \"While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: ...\"\n\n但不要重复 GraphCodeBERT 已经说过的内容，保持简洁。\n\n### 输出要求\n- 直接用 Edit 工具修改 related_work_v1.md\n- 每项修正单独一次 Edit（方便 review）\n- WebSearch 结果如有重要发现（如 GraphCoder/ARISE 确实有 inter-procedural 组件），在修改时注明来源\n- 完成后输出修改摘要"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T09:58:36.293Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T09:58:36.293Z",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98"
}
```

---

## Round 1

56 recorded events

### User

_source line 3 · 2026-05-15T09:58:36.329Z_

&lt;project_context>
# 项目: structfuse-context

## 运行环境
- 服务器名: bjb1-42106
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.bjb1.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/structfuse


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：Related Work v1 修正（4 项）

修改文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md`

同时需要参考 Introduction 文件（只读，不修改）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md`

### 修正 1 [WARNING]：GraphCoder/ARISE scope 事实核实

用 WebSearch 查阅以下两篇论文原文，确认 data-flow scope：
- **GraphCoder** (ASE 2024, Liu et al.) — 当前文中写 "limited to intra-procedural scope"
- **ARISE** (arXiv 2605.03117, Seddik et al., 2026) — 当前文中同样写 "limited to intra-procedural scope"

确认：它们是否真的限于 intra-procedural？如果有 inter-procedural 组件，改为 "primarily intra-procedural" 或更精确描述。这是审稿人容易攻击的事实性断言。

当前原文（§2.4 倒数第二句）：
> "GraphCoder \cite{liu2024graphcoder} and ARISE \cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope."

### 修正 2 [WARNING]："all these methods" 断言软化

当前原文（§2.4 最后一段）：
> "Critically, all these methods construct and query graphs at inference time"

改为：
> "Critically, these methods primarily leverage structural graphs at inference time"

除非你通过 WebSearch 逐一确认了 6 个系统（CodexGraph, RepoGraph, LocAgent, RANGER, GraphCoder, ARISE）全部只在推理时用图，否则必须软化。

### 修正 3 [INFO]：CoCoHaNeRe 双重描述统一

问题：Introduction 说 CoCoHaNeRe "argues that non-differentiable embedding-based negatives are 'slow and ineffective'"（批评 embedding negatives），但 Related Work §2.3 说 "reports that BM25-selected negatives can be detrimental"（批评 BM25 negatives）。两处描述不一致，读者会困惑。

在 §2.3 CoCoHaNeRe 那句后面加一句，说明 CoCoHaNeRe 同时研究了多种非梯度负样本挖掘方法（包括 BM25 和 embedding-based），消除读者困惑。不要改 Introduction 的措辞。

### 修正 4 [INFO]：GraphCodeBERT 区分强化

§2.2 最后两句目前：
> "GraphCodeBERT \cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension..."

在 "StructFuse addresses a complementary dimension" 前加半句，明确区分 "pretraining objective (GraphCodeBERT) vs training-time negative selection (StructFuse)"。类似：
> "While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: ..."

但不要重复 GraphCodeBERT 已经说过的内容，保持简洁。

### 输出要求
- 直接用 Edit 工具修改 related_work_v1.md
- 每项修正单独一次 Edit（方便 review）
- WebSearch 结果如有重要发现（如 GraphCoder/ARISE 确实有 inter-procedural 组件），在修改时注明来源
- 完成后输出修改摘要

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "62ec9e26-7205-4414-b673-6110d35d9a64",
  "type": "user",
  "uuid": "a91d32cb-7464-4fdb-9665-0a5c5a3080e8",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T09:58:36.328Z_

```json
{
  "parentUuid": "a91d32cb-7464-4fdb-9665-0a5c5a3080e8",
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
  "uuid": "44be99c1-1968-4b02-b484-08e9cacbc516",
  "timestamp": "2026-05-15T09:58:36.328Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T09:58:36.328Z_

```json
{
  "parentUuid": "44be99c1-1968-4b02-b484-08e9cacbc516",
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
  "uuid": "f66b2794-fefb-45ee-9030-fc76aa037424",
  "timestamp": "2026-05-15T09:58:36.328Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T09:58:36.328Z_

```json
{
  "parentUuid": "f66b2794-fefb-45ee-9030-fc76aa037424",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "89e4438e-7402-4dc2-a777-bc1544e0497b",
  "timestamp": "2026-05-15T09:58:36.328Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
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
  "aiTitle": "Fix related work section with fact-checking",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98"
}
```

---

### Assistant

_source line 8 · 2026-05-15T09:58:39.260Z_

我先读取两个文件，同时搜索 GraphCoder 和 ARISE 的论文信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89e4438e-7402-4dc2-a777-bc1544e0497b",
  "isSidechain": false,
  "requestId": "req_011Cb4A6QKeCcvp4Kweg5ijQ",
  "type": "assistant",
  "uuid": "8da78e1c-0c34-48b8-a394-af186a1e621b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsyhWpx2mRFGgh2ZiSo9cW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11804,
      "cache_read_input_tokens": 11841,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 261,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11804
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

_source line 9 · 2026-05-15T09:58:39.771Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NRcguekN7Mjc5DzQbfgBbW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8da78e1c-0c34-48b8-a394-af186a1e621b",
  "isSidechain": false,
  "requestId": "req_011Cb4A6QKeCcvp4Kweg5ijQ",
  "type": "assistant",
  "uuid": "5b0cf173-28dd-4b1e-955e-6bbf3aca1600",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsyhWpx2mRFGgh2ZiSo9cW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11804,
      "cache_read_input_tokens": 11841,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 261,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11804
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

_source line 10 · 2026-05-15T09:58:39.783Z_

<details><summary>↩ Tool result · `toolu_01NRcguekN7Mjc5DzQbfgBbW`</summary>

```text
1	# 2. Related Work
2	
3	## 2.1 Dense Retrieval for Code
4	
5	Code retrieval has evolved from sparse lexical methods such as BM25 \cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \cite{feng2020codebert}, UniXcoder \cite{guo2022unixcoder}, and InferCode \cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \cite{lozhkov2024starcoder2} and Qwen2.5-Coder \cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \cite{zhang2024codesage} and SCodeR \cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \cite{jimenez2024swebench}---has motivated specialized systems: SweRank \cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.
6	
7	## 2.2 Contrastive Learning for Code
8	
9	Contrastive learning has become a dominant paradigm for code representation learning. ContraCode \cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.
10	
11	## 2.3 Hard Negative Mining
12	
13	The quality of negative examples critically affects contrastive learning \cite{chen2020simclr}. In dense text retrieval, DPR \cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \cite{zeng2022cldrd} and CAPSTONE \cite{he2023capstone}---schedule negative difficulty progressively during training.
14	
15	In the code domain, CoCoHaNeRe \cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.
16	
17	## 2.4 Code Structure in Machine Learning
18	
19	Program dependence graphs \cite{ferrante1987pdg} and code property graphs \cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.
20	
21	Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \cite{liu2025codexgraph} and RepoGraph \cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \cite{chen2025locagent} and RANGER \cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \cite{liu2024graphcoder} and ARISE \cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope. Critically, all these methods construct and query graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b0cf173-28dd-4b1e-955e-6bbf3aca1600",
  "isSidechain": false,
  "promptId": "62ec9e26-7205-4414-b673-6110d35d9a64",
  "type": "user",
  "uuid": "508553d8-89e1-40e4-9a3e-2d5a7b8283b7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
      "content": "# 2. Related Work\n\n## 2.1 Dense Retrieval for Code\n\nCode retrieval has evolved from sparse lexical methods such as BM25 \\cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \\cite{feng2020codebert}, UniXcoder \\cite{guo2022unixcoder}, and InferCode \\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \\cite{zhang2024codesage} and SCodeR \\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \\cite{jimenez2024swebench}---has motivated specialized systems: SweRank \\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.\n\n## 2.2 Contrastive Learning for Code\n\nContrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.\n\n## 2.3 Hard Negative Mining\n\nThe quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.\n\nIn the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.\n\n## 2.4 Code Structure in Machine Learning\n\nProgram dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.\n\nRecent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope. Critically, all these methods construct and query graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  },
  "sourceToolAssistantUUID": "5b0cf173-28dd-4b1e-955e-6bbf3aca1600",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T09:58:40.416Z_

<details><summary>↩ Tool result · `toolu_01EgyEM3ztHw8J6xeDnD9kDy`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "570cd770-6bef-41e2-94ad-9db3183d7407",
  "isSidechain": false,
  "promptId": "62ec9e26-7205-4414-b673-6110d35d9a64",
  "type": "user",
  "uuid": "fd93ec4f-2cb6-41fc-99f9-3e9857dc8e36",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "570cd770-6bef-41e2-94ad-9db3183d7407",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T09:58:40.229Z_

<details open><summary>🔧 Tool call — Read · `toolu_012m9ZBFfcWjND5x3cDDNNTD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "508553d8-89e1-40e4-9a3e-2d5a7b8283b7",
  "isSidechain": false,
  "requestId": "req_011Cb4A6QKeCcvp4Kweg5ijQ",
  "type": "assistant",
  "uuid": "7131abad-df5e-453a-985a-b2e7b5fb09c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsyhWpx2mRFGgh2ZiSo9cW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11804,
      "cache_read_input_tokens": 11841,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 261,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11804
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

_source line 13 · 2026-05-15T09:58:40.235Z_

<details><summary>↩ Tool result · `toolu_012m9ZBFfcWjND5x3cDDNNTD`</summary>

```text
1	# 1. Introduction
2	
3	Resolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \cite{jimenez2024swebench}.
4	Dense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \cite{reddy2025swerank,xie2025swefixer}.
5	These approaches build on a rich lineage of pre-trained code representations---from CodeBERT \cite{feng2020codebert} and UniXcoder \cite{guo2022unixcoder} to decoder-only code models \cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.
6	Yet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.
7	Despite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.
8	
9	In open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.
10	DPR \cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.
11	These methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \cite{zhan2021star,zeng2022cldrd}.
12	In the code domain, however, the picture is less clear.
13	CoCoHaNeRe \cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''
14	This finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?
15	
16	We observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.
17	This structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.
18	We operationalize this insight using CodeQL \cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by lexical similarity.
19	Crucially, this structure-grounded mining is a \emph{training-time} intervention only, incurring zero additional inference cost.
20	This positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \cite{liu2025codexgraph}, RANGER \cite{shah2025ranger}, and RepoGraph \cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.
21	
22	Our systematic comparison of three negative mining strategies---random, embedding-distance, and dataflow-aware---across two decoder-only encoders yields the following findings.
23	First, simple static embedding-distance mining provides a reliable retrieval improvement at negligible additional cost compared to random sampling, with consistent R@1 improvements of +X.X pp across N random seeds (95\% CI: [a, b]) on Qwen2.5-Coder-3B \cite{hui2024qwen25coder} (with StarCoder2-3B \cite{lozhkov2024starcoder2} validation in progress). % TODO: fill final numbers after all seeds complete
24	This establishes embedding-distance mining as a strong baseline requiring no gradient computation, for future work on more sophisticated strategies.
25	Second, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\ 0.80), respond differently to structural negatives.
26	We report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.
27	
28	Our contributions are as follows:
29	
30	1. **A systematic comparison of three negative mining strategies** (random, embedding-distance, dataflow-aware) across decoder-only encoders (Qwen2.5-Coder-3B, with StarCoder2-3B validation in progress) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.
31	
32	2. **A practical CodeQL-based pipeline for structure-grounded hard negative mining** using inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\% timeout rate, 78\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives without requiring gradient computation.
33	
34	3. **Preliminary mechanistic analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7131abad-df5e-453a-985a-b2e7b5fb09c1",
  "isSidechain": false,
  "promptId": "62ec9e26-7205-4414-b673-6110d35d9a64",
  "type": "user",
  "uuid": "45087c88-1d21-4d11-b22a-c1bd89433a14",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/introduction_v1.md",
      "content": "# 1. Introduction\n\nResolving real-world software issues in large repositories requires accurately localizing the relevant source files from hundreds or thousands of candidates \\cite{jimenez2024swebench}.\nDense retrieval has emerged as the dominant paradigm for this task, with recent systems employing contrastive learning to train encoders that map issue descriptions and code files into a shared embedding space \\cite{reddy2025swerank,xie2025swefixer}.\nThese approaches build on a rich lineage of pre-trained code representations---from CodeBERT \\cite{feng2020codebert} and UniXcoder \\cite{guo2022unixcoder} to decoder-only code models \\cite{hui2024qwen25coder,lozhkov2024starcoder2}---that have steadily improved code understanding across retrieval, completion, and search tasks.\nYet the training signal for contrastive code retrievers depends not only on positive pairs but critically on the selection of \\emph{negative} examples: which non-relevant files the model learns to distinguish from the ground truth.\nDespite the importance of negative selection, systematic study of what mining strategies work for code retrieval---and why---remains limited.\n\nIn open-domain text retrieval, hard negative mining has proven essential for training effective dense retrievers.\nDPR \\cite{karpukhin2020dpr} established the practice of using BM25-retrieved passages as hard negatives, ANCE \\cite{xiong2021ance} introduced dynamic mining from approximate nearest neighbor indices, and RocketQA \\cite{qu2021rocketqa} developed cross-encoder-filtered denoised negatives.\nThese methods consistently outperform random negative sampling by exposing the encoder to confusable examples during training \\cite{zhan2021star,zeng2022cldrd}.\nIn the code domain, however, the picture is less clear.\nCoCoHaNeRe \\cite{fan2025cocohanere}, published in ACM TOSEM 2025, proposes differentiable gradient-based hard negative mechanisms for code search and argues that non-differentiable embedding-based negatives are ``slow and ineffective.''\nThis finding raises a natural question: does simple, static embedding-distance mining---the most accessible form of hard negative selection---genuinely fail for code retrieval, or has its potential been underexplored in the structural code retrieval setting?\n\nWe observe that code possesses rich structural information---call graphs, data-flow dependencies, inter-procedural taint tracking---that is absent in natural language text.\nThis structural connectivity can serve as an independent signal dimension for constructing hard negatives: files that are structurally disconnected from the query yet lexically similar provide challenging training examples grounded in program semantics rather than surface similarity alone.\nWe operationalize this insight using CodeQL \\cite{avgustinov2016ql} inter-procedural data-flow analysis to compute structural connectivity at repository scale, then select negatives from structurally unreachable files ranked by lexical similarity.\nCrucially, this structure-grounded mining is a \\emph{training-time} intervention only, incurring zero additional inference cost.\nThis positions our approach as complementary to inference-time graph-guided methods such as CodexGraph \\cite{liu2025codexgraph}, RANGER \\cite{shah2025ranger}, and RepoGraph \\cite{ouyang2025repograph}, which leverage structural graphs during retrieval but do not use them to improve the training signal.\n\nOur systematic comparison of three negative mining strategies---random, embedding-distance, and dataflow-aware---across two decoder-only encoders yields the following findings.\nFirst, simple static embedding-distance mining provides a reliable retrieval improvement at negligible additional cost compared to random sampling, with consistent R@1 improvements of +X.X pp across N random seeds (95\\% CI: [a, b]) on Qwen2.5-Coder-3B \\cite{hui2024qwen25coder} (with StarCoder2-3B \\cite{lozhkov2024starcoder2} validation in progress). % TODO: fill final numbers after all seeds complete\nThis establishes embedding-distance mining as a strong baseline requiring no gradient computation, for future work on more sophisticated strategies.\nSecond, structure-grounded (dataflow) negatives exhibit an encoder-dependent interaction: the two encoders, which differ markedly in representation geometry (positive-pair cosine similarity 0.99 vs.\\ 0.80), respond differently to structural negatives.\nWe report this as an exploratory observation supported by preliminary mechanistic analysis of negative difficulty margins, not as an established finding.\n\nOur contributions are as follows:\n\n1. **A systematic comparison of three negative mining strategies** (random, embedding-distance, dataflow-aware) across decoder-only encoders (Qwen2.5-Coder-3B, with StarCoder2-3B validation in progress) with distinct pretraining paradigms and representation geometries. We evaluate with multi-seed statistical validation and report both best-by-R@1 and fixed-checkpoint metrics for transparency.\n\n2. **A practical CodeQL-based pipeline for structure-grounded hard negative mining** using inter-procedural data-flow analysis. The pipeline computes scope-bounded structural connectivity across entire repositories (123 repos, 0\\% timeout rate, 78\\% connected-not-gold rate), enabling any contrastive code retrieval system to incorporate structural negatives without requiring gradient computation.\n\n3. **Preliminary mechanistic analysis of representation geometry's role in strategy effectiveness.** Through negative difficulty margin analysis across strategies and encoders, we offer preliminary mechanistic evidence for when and why different mining strategies yield different outcomes, providing a candidate heuristic (positive-pair similarity threshold) that may help practitioners select strategies without exhaustive experimentation.\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  },
  "sourceToolAssistantUUID": "7131abad-df5e-453a-985a-b2e7b5fb09c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T09:58:40.412Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EgyEM3ztHw8J6xeDnD9kDy`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45087c88-1d21-4d11-b22a-c1bd89433a14",
  "isSidechain": false,
  "requestId": "req_011Cb4A6QKeCcvp4Kweg5ijQ",
  "type": "assistant",
  "uuid": "570cd770-6bef-41e2-94ad-9db3183d7407",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsyhWpx2mRFGgh2ZiSo9cW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11804,
      "cache_read_input_tokens": 11841,
      "output_tokens": 261,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 261,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11804
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

_source line 15_

```json
{
  "type": "last-prompt",
  "leafUuid": "fd93ec4f-2cb6-41fc-99f9-3e9857dc8e36",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix related work section with fact-checking",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98"
}
```

---

### Assistant

_source line 17 · 2026-05-15T09:58:43.331Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for GraphCoder and ARISE papers to fact-check the intra-procedural scope claim.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd93ec4f-2cb6-41fc-99f9-3e9857dc8e36",
  "isSidechain": false,
  "requestId": "req_011Cb4A6i3FYWMTvqJsri6We",
  "type": "assistant",
  "uuid": "e1cb4950-d114-46f5-b4b3-71b584eb8956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYEp6LRcaPwJyQaZCWwLMc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3779,
      "cache_read_input_tokens": 23645,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 23645,
          "cache_creation_input_tokens": 3779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3779
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

_source line 18 · 2026-05-15T09:58:43.859Z_

搜索 GraphCoder 和 ARISE 论文的 data-flow scope 信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1cb4950-d114-46f5-b4b3-71b584eb8956",
  "isSidechain": false,
  "requestId": "req_011Cb4A6i3FYWMTvqJsri6We",
  "type": "assistant",
  "uuid": "e85a6bb9-9903-47c8-9478-f6b95f05e515",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYEp6LRcaPwJyQaZCWwLMc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3779,
      "cache_read_input_tokens": 23645,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 23645,
          "cache_creation_input_tokens": 3779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3779
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

_source line 19 · 2026-05-15T09:58:44.821Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fa11q97dDFLWj7zLFPRNvG`</summary>

```json
{
  "query": "GraphCoder ASE 2024 Liu data-flow intra-procedural inter-procedural code retrieval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e85a6bb9-9903-47c8-9478-f6b95f05e515",
  "isSidechain": false,
  "requestId": "req_011Cb4A6i3FYWMTvqJsri6We",
  "type": "assistant",
  "uuid": "5f27f1b4-158b-4a1a-a2f7-cb22c72cf7e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYEp6LRcaPwJyQaZCWwLMc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3779,
      "cache_read_input_tokens": 23645,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 23645,
          "cache_creation_input_tokens": 3779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3779
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

_source line 20 · 2026-05-15T09:58:45.164Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WuSqTL4xCPuHj5NVcisLtC`</summary>

```json
{
  "query": "ARISE arXiv 2605.03117 Seddik 2026 data-flow scope intra-procedural"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f27f1b4-158b-4a1a-a2f7-cb22c72cf7e8",
  "isSidechain": false,
  "requestId": "req_011Cb4A6i3FYWMTvqJsri6We",
  "type": "assistant",
  "uuid": "d0467b35-8567-4a58-9cb3-bea80efc9e0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYEp6LRcaPwJyQaZCWwLMc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3779,
      "cache_read_input_tokens": 23645,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 23645,
          "cache_creation_input_tokens": 3779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3779
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

_source line 21 · 2026-05-15T09:58:51.089Z_

<details><summary>↩ Tool result · `toolu_01WuSqTL4xCPuHj5NVcisLtC`</summary>

```text
Web search results for query: "ARISE arXiv 2605.03117 Seddik 2026 data-flow scope intra-procedural"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"[2605.06826] How Does Attention Help? Insights from Random Matrices on Signal Recovery from Sequence Models","url":"https://arxiv.org/abs/2605.06826"},{"title":"[2605.13681] Sampling from Flow Language Models via Marginal-Conditioned Bridges","url":"https://arxiv.org/abs/2605.13681"},{"title":"[2605.13509] Quantifying information flow along a stochastic trajectory","url":"https://arxiv.org/abs/2605.13509"},{"title":"[2605.10938] ELF: Embedded Language Flows","url":"https://arxiv.org/abs/2605.10938"},{"title":"[2605.12951] Coreset-Induced Conditional Velocity Flow Matching","url":"https://arxiv.org/abs/2605.12951"},{"title":"[2605.02287] Per-Market Information Leakage and Order-Flow Skill: Two Methodological Lenses on Informed Trading in Decentralized Prediction Markets","url":"https://arxiv.org/abs/2605.02287"},{"title":"[2605.14137] Flow Field Reconstruction with Sensor Placement Policy Learning","url":"https://arxiv.org/abs/2605.14137"},{"title":"[2605.08648] FLUX: Geometry-Aware Longitudinal Flow Matching with Mixture of Experts","url":"https://arxiv.org/abs/2605.08648"}]

Based on the search results, I found the paper you're looking for:

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

Existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures, leaving agents without the semantic precision needed for function- and line-level localization.

ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.

The paper was authored by Shahd Seddik and Fatemeh Fard and submitted on May 4, 2026.

The paper is available at arXiv:2605.03117.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0467b35-8567-4a58-9cb3-bea80efc9e0e",
  "isSidechain": false,
  "promptId": "62ec9e26-7205-4414-b673-6110d35d9a64",
  "type": "user",
  "uuid": "13b30255-0402-4bd6-8b7c-ea1a71d82568",
  "toolUseResult": {
    "query": "ARISE arXiv 2605.03117 Seddik 2026 data-flow scope intra-procedural",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Su8dfZn21q4s2ejnMvTbeh",
        "content": [
          {
            "title": "[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/abs/2605.03117"
          },
          {
            "title": "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/html/2605.03117"
          },
          {
            "title": "[2605.06826] How Does Attention Help? Insights from Random Matrices on Signal Recovery from Sequence Models",
            "url": "https://arxiv.org/abs/2605.06826"
          },
          {
            "title": "[2605.13681] Sampling from Flow Language Models via Marginal-Conditioned Bridges",
            "url": "https://arxiv.org/abs/2605.13681"
          },
          {
            "title": "[2605.13509] Quantifying information flow along a stochastic trajectory",
            "url": "https://arxiv.org/abs/2605.13509"
          },
          {
            "title": "[2605.10938] ELF: Embedded Language Flows",
            "url": "https://arxiv.org/abs/2605.10938"
          },
          {
            "title": "[2605.12951] Coreset-Induced Conditional Velocity Flow Matching",
            "url": "https://arxiv.org/abs/2605.12951"
          },
          {
            "title": "[2605.02287] Per-Market Information Leakage and Order-Flow Skill: Two Methodological Lenses on Informed Trading in Decentralized Prediction Markets",
            "url": "https://arxiv.org/abs/2605.02287"
          },
          {
            "title": "[2605.14137] Flow Field Reconstruction with Sensor Placement Policy Learning",
            "url": "https://arxiv.org/abs/2605.14137"
          },
          {
            "title": "[2605.08648] FLUX: Geometry-Aware Longitudinal Flow Matching with Mixture of Experts",
            "url": "https://arxiv.org/abs/2605.08648"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.\n\nExisting graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures, leaving agents without the semantic precision needed for function- and line-level localization.\n\nARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.\n\nThe paper was authored by Shahd Seddik and Fatemeh Fard and submitted on May 4, 2026.\n\nThe paper is available at arXiv:2605.03117."
    ],
    "durationSeconds": 5.921278698999998
  },
  "sourceToolAssistantUUID": "d0467b35-8567-4a58-9cb3-bea80efc9e0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T09:58:52.760Z_

<details><summary>↩ Tool result · `toolu_01Fa11q97dDFLWj7zLFPRNvG`</summary>

```text
Web search results for query: "GraphCoder ASE 2024 Liu data-flow intra-procedural inter-procedural code retrieval"

Links: [{"title":"[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/abs/2406.07003"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024","url":"https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"},{"title":"[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3691620.3695054"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/html/2406.07003v2"},{"title":"GitHub - oceaneLIU/GraphCoder","url":"https://github.com/oceaneLIU/GraphCoder"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Request PDF","url":"https://www.researchgate.net/publication/385287286_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Coarse-to-fine_Retrieval_Based_on_Code_Context_Graph"},{"title":"39th ASE 2024: Sacramento, CA, USA","url":"https://dblp.org/db/conf/kbse/ase2024.html"},{"title":"2024 39th IEEE/ACM International Conference on ...","url":"https://www.computer.org/csdl/proceedings/ase/2024/22gEsOsLriM"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"}]

I found search results for GraphCoder and ASE 2024. Here are the key findings:

## GraphCoder ASE 2024 Paper

GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph was authored by Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, and Qianxiang Wang and presented at ASE 2024.

## Core Approach

GraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process, capturing the context of completion target through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements, and employs a coarse-to-fine retrieval process to locate context-similar code snippets from the current repository.

## Data-Flow and Procedural Analysis

GraphCoder captures the context through code context graph (CCG) that consists of control-flow and data/control-dependence between code statements, though the specific mention of "intra-procedural" and "inter-procedural" analysis in your query doesn't appear to be explicitly labeled with those terms in the search results. The framework appears to handle dependencies both within and across code structures through its graph-based approach.

The paper has been posted on arXiv and was presented at the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE 2024) in Sacramento, CA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f27f1b4-158b-4a1a-a2f7-cb22c72cf7e8",
  "isSidechain": false,
  "promptId": "62ec9e26-7205-4414-b673-6110d35d9a64",
  "type": "user",
  "uuid": "78b39499-ae74-445d-9e70-80de27be74ae",
  "toolUseResult": {
    "query": "GraphCoder ASE 2024 Liu data-flow intra-procedural inter-procedural code retrieval",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J6eZSYdkLJR9hr9WeuB4n1",
        "content": [
          {
            "title": "[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/abs/2406.07003"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024",
            "url": "https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"
          },
          {
            "title": "[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering",
            "url": "https://dl.acm.org/doi/10.1145/3691620.3695054"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/html/2406.07003v2"
          },
          {
            "title": "GitHub - oceaneLIU/GraphCoder",
            "url": "https://github.com/oceaneLIU/GraphCoder"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Request PDF",
            "url": "https://www.researchgate.net/publication/385287286_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Coarse-to-fine_Retrieval_Based_on_Code_Context_Graph"
          },
          {
            "title": "39th ASE 2024: Sacramento, CA, USA",
            "url": "https://dblp.org/db/conf/kbse/ase2024.html"
          },
          {
            "title": "2024 39th IEEE/ACM International Conference on ...",
            "url": "https://www.computer.org/csdl/proceedings/ase/2024/22gEsOsLriM"
          },
          {
            "title": "GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub",
            "url": "https://github.com/iSEngLab/AwesomeLLM4SE"
          }
        ]
      },
      "I found search results for GraphCoder and ASE 2024. Here are the key findings:\n\n## GraphCoder ASE 2024 Paper\n\nGraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph was authored by Wei Liu, Ailun Yu, Daoguang Zan, Bo Shen, Wei Zhang, Haiyan Zhao, Zhi Jin, and Qianxiang Wang and presented at ASE 2024.\n\n## Core Approach\n\nGraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process, capturing the context of completion target through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements, and employs a coarse-to-fine retrieval process to locate context-similar code snippets from the current repository.\n\n## Data-Flow and Procedural Analysis\n\nGraphCoder captures the context through code context graph (CCG) that consists of control-flow and data/control-dependence between code statements, though the specific mention of \"intra-procedural\" and \"inter-procedural\" analysis in your query doesn't appear to be explicitly labeled with those terms in the search results. The framework appears to handle dependencies both within and across code structures through its graph-based approach.\n\nThe paper has been posted on arXiv and was presented at the 39th IEEE/ACM International Conference on Automated Software Engineering (ASE 2024) in Sacramento, CA."
    ],
    "durationSeconds": 7.934743065999999
  },
  "sourceToolAssistantUUID": "5f27f1b4-158b-4a1a-a2f7-cb22c72cf7e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-15T09:58:58.006Z_

<details><summary>Logged reasoning block</summary>

```text
Let me get more details on both papers. The ARISE search result mentions "intra-procedural definition-use edges" - so it does seem limited to intra-procedural scope. Let me get more detail on GraphCoder's scope.

For GraphCoder, the search result says it uses "code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements". I need to check if this is intra-procedural or inter-procedural. Let me read the arxiv HTML page for more details.


I should look up more specifics about GraphCoder's scope to determine whether it handles inter-procedural analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78b39499-ae74-445d-9e70-80de27be74ae",
  "isSidechain": false,
  "requestId": "req_011Cb4A7cY8hKoU1fN1hZ9D1",
  "type": "assistant",
  "uuid": "4b4eda62-4c40-4012-9bf6-171325619c66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sjwe4szm5YV9pw8Es1ivjw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 1335,
      "cache_read_input_tokens": 27424,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1335,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 780,
          "output_tokens": 330,
          "cache_read_input_tokens": 27424,
          "cache_creation_input_tokens": 1335,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1335
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

_source line 24 · 2026-05-15T09:58:58.007Z_

需要更多细节，特别是 GraphCoder 的 CCG 是否跨过程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b4eda62-4c40-4012-9bf6-171325619c66",
  "isSidechain": false,
  "requestId": "req_011Cb4A7cY8hKoU1fN1hZ9D1",
  "type": "assistant",
  "uuid": "84fa2a4f-3051-4a37-87e3-ac3b70aacba4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sjwe4szm5YV9pw8Es1ivjw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 1335,
      "cache_read_input_tokens": 27424,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1335,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 780,
          "output_tokens": 330,
          "cache_read_input_tokens": 27424,
          "cache_creation_input_tokens": 1335,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1335
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

_source line 25 · 2026-05-15T09:58:58.668Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QXCQ3sX4vBuPopLrJK9DnJ`</summary>

```json
{
  "query": "GraphCoder \"code context graph\" CCG \"intra-procedural\" OR \"within function\" OR \"single function\" scope ASE 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84fa2a4f-3051-4a37-87e3-ac3b70aacba4",
  "isSidechain": false,
  "requestId": "req_011Cb4A7cY8hKoU1fN1hZ9D1",
  "type": "assistant",
  "uuid": "11a5481d-957a-4e52-aa47-d294dcfdadfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sjwe4szm5YV9pw8Es1ivjw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 1335,
      "cache_read_input_tokens": 27424,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1335,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 780,
          "output_tokens": 330,
          "cache_read_input_tokens": 27424,
          "cache_creation_input_tokens": 1335,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1335
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

_source line 26 · 2026-05-15T09:58:59.173Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VMMvtz6VCZJiRztBXu32eD`</summary>

```json
{
  "query": "ARISE arXiv 2605.03117 \"intra-procedural\" \"definition-use\" \"inter-procedural\" repository-level graph"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11a5481d-957a-4e52-aa47-d294dcfdadfb",
  "isSidechain": false,
  "requestId": "req_011Cb4A7cY8hKoU1fN1hZ9D1",
  "type": "assistant",
  "uuid": "49270132-91f6-4d2c-bda8-51f95eaf4f50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sjwe4szm5YV9pw8Es1ivjw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 780,
      "cache_creation_input_tokens": 1335,
      "cache_read_input_tokens": 27424,
      "output_tokens": 330,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1335,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 780,
          "output_tokens": 330,
          "cache_read_input_tokens": 27424,
          "cache_creation_input_tokens": 1335,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1335
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

_source line 27 · 2026-05-15T09:59:04.943Z_

<details><summary>↩ Tool result · `toolu_01QXCQ3sX4vBuPopLrJK9DnJ`</summary>

```text
Web search results for query: "GraphCoder "code context graph" CCG "intra-procedural" OR "within function" OR "single function" scope ASE 2024"

Links: [{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024","url":"https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1145/3691620.3695054"},{"title":"[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/abs/2406.07003"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/html/2406.07003v2"},{"title":"GitHub - oceaneLIU/GraphCoder","url":"https://github.com/oceaneLIU/GraphCoder"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code","url":"https://openreview.net/pdf/7a92572e89daf427869cbb262f97920e5f6f35a3.pdf"},{"title":"GraphCoder | NL2Code","url":"https://nl2code.github.io/posts/GraphCoder/"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240607003L/abstract"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph - Consensus","url":"https://consensus.app/papers/graphcoder-enhancing-repositorylevel-code-completion-wang-jin/b4870512e370577aa2ee9b8b4aee9bfd/"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Request PDF","url":"https://www.researchgate.net/publication/385287286_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Coarse-to-fine_Retrieval_Based_on_Code_Context_Graph"}]

## Search Results for GraphCoder with Code Context Graph (CCG)

I've found comprehensive information about GraphCoder and its use of Code Context Graphs. Here are the key findings:

### Overview

GraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process.

### Code Context Graph (CCG)

GraphCoder captures the context of completion target more accurately through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements, a more structured way to capture the completion target context than the sequence-based context used in existing retrieval-augmented approaches.

### Performance Results

Compared to baseline retrieval-augmented methods, GraphCoder achieves higher exact match (EM) on average, with increases of +6.06 in code match and +6.23 in identifier match, while using less time and space.

### Publication Details

The paper was presented at ASE 2024 Research Papers on October 31, 2024.

### Technical Approach

Based on CCG, GraphCoder further employs a coarse-to-fine retrieval process to locate context-similar code snippets with the completion target from the current repository.

The search results confirm that GraphCoder is a repository-level code completion framework presented at ASE 2024 that uses Code Context Graphs (CCG) to capture code dependencies and structural relationships for improved code completion tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11a5481d-957a-4e52-aa47-d294dcfdadfb",
  "isSidechain": false,
  "promptId": "62ec9e26-7205-4414-b673-6110d35d9a64",
  "type": "user",
  "uuid": "d80073dd-820b-45a1-888d-cae2dc5185b4",
  "toolUseResult": {
    "query": "GraphCoder \"code context graph\" CCG \"intra-procedural\" OR \"within function\" OR \"single function\" scope ASE 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QhQxnVtc3rfyieVwrdhkxw",
        "content": [
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph (ASE 2024 - Research Papers) - ASE 2024",
            "url": "https://conf.researchr.org/details/ase-2024/ase-2024-research/46/GraphCoder-Enhancing-Repository-Level-Code-Completion-via-Coarse-to-fine-Retrieval-B"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering",
            "url": "https://dl.acm.org/doi/10.1145/3691620.3695054"
          },
          {
            "title": "[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/abs/2406.07003"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/html/2406.07003v2"
          },
          {
            "title": "GitHub - oceaneLIU/GraphCoder",
            "url": "https://github.com/oceaneLIU/GraphCoder"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code",
            "url": "https://openreview.net/pdf/7a92572e89daf427869cbb262f97920e5f6f35a3.pdf"
          },
          {
            "title": "GraphCoder | NL2Code",
            "url": "https://nl2code.github.io/posts/GraphCoder/"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240607003L/abstract"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph - Consensus",
            "url": "https://consensus.app/papers/graphcoder-enhancing-repositorylevel-code-completion-wang-jin/b4870512e370577aa2ee9b8b4aee9bfd/"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Coarse-to-fine Retrieval Based on Code Context Graph | Request PDF",
            "url": "https://www.researchgate.net/publication/385287286_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Coarse-to-fine_Retrieval_Based_on_Code_Context_Graph"
          }
        ]
      },
      "## Search Results for GraphCoder with Code Context Graph (CCG)\n\nI've found comprehensive information about GraphCoder and its use of Code Context Graphs. Here are the key findings:\n\n### Overview\n\nGraphCoder is a retrieval-augmented code completion framework that leverages LLMs' general code knowledge and repository-specific knowledge via a graph-based retrieval-generation process.\n\n### Code Context Graph (CCG)\n\nGraphCoder captures the context of completion target more accurately through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements, a more structured way to capture the completion target context than the sequence-based context used in existing retrieval-augmented approaches.\n\n### Performance Results\n\nCompared to baseline retrieval-augmented methods, GraphCoder achieves higher exact match (EM) on average, with increases of +6.06 in code match and +6.23 in identifier match, while using less time and space.\n\n### Publication Details\n\nThe paper was presented at ASE 2024 Research Papers on October 31, 2024.\n\n### Technical Approach\n\nBased on CCG, GraphCoder further employs a coarse-to-fine retrieval process to locate context-similar code snippets with the completion target from the current repository.\n\nThe search results confirm that GraphCoder is a repository-level code completion framework presented at ASE 2024 that uses Code Context Graphs (CCG) to capture code dependencies and structural relationships for improved code completion tasks."
    ],
    "durationSeconds": 6.269019581000004
  },
  "sourceToolAssistantUUID": "11a5481d-957a-4e52-aa47-d294dcfdadfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "leafUuid": "d80073dd-820b-45a1-888d-cae2dc5185b4",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix related work section with fact-checking",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98"
}
```

---

### Tool result

_source line 30 · 2026-05-15T09:59:05.900Z_

<details><summary>↩ Tool result · `toolu_01VMMvtz6VCZJiRztBXu32eD`</summary>

```text
Web search results for query: "ARISE arXiv 2605.03117 "intra-procedural" "definition-use" "inter-procedural" repository-level graph"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"RepoAudit: An Autonomous LLM-Agent for Repository- ...","url":"https://arxiv.org/pdf/2501.18160"},{"title":"INTERPROCEDURAL ANALYSIS","url":"https://pages.cs.wisc.edu/~fischer/cs701.f14/6.INTERPROCEDURAL-ANALYSIS.html"},{"title":"[2605.00817] When LLMs Stop Following Steps: A Diagnostic Study of Procedural Execution in Language Models","url":"https://arxiv.org/abs/2605.00817"},{"title":"Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural","url":"https://www.arxiv.org/pdf/2602.06751"},{"title":"Retrieval from Within: An Intrinsic Capability of Attention-Based Models","url":"https://arxiv.org/html/2605.05806"},{"title":"SkillRAE: Agent Skill-Based Context Compilation for Retrieval-Augmented Execution","url":"https://arxiv.org/html/2605.10114"},{"title":"Beyond State Machines: Executing Network Procedures with Agentic Tool-Calling Sequences","url":"https://arxiv.org/html/2605.02584"},{"title":"Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural Vulnerability Detection","url":"https://arxiv.org/html/2602.06751v1"}]

Based on the web search results, I found information about the arXiv paper 2605.03117:

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

Repository-level fault localization and automated program repair require an agent to identify the relevant code units across files, follow call and data dependencies, and generate a valid patch. Existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures, leaving agents without the semantic precision needed for function- and line-level localization.

ARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.

The paper was published on arXiv on May 4, 2026, and addresses a key gap in existing systems: none constructs statement-level nodes, none models definition-use relationships, and none exposes a first-class data-flow slicing primitive to the agent.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "49270132-91f6-4d2c-bda8-51f95eaf4f50",
  "isSidechain": false,
  "promptId": "62ec9e26-7205-4414-b673-6110d35d9a64",
  "type": "user",
  "uuid": "4603aa9f-f5bf-4cd2-b987-7230ae5e4402",
  "toolUseResult": {
    "query": "ARISE arXiv 2605.03117 \"intra-procedural\" \"definition-use\" \"inter-procedural\" repository-level graph",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Kemj9qxQHeJHv2RVBoXfp6",
        "content": [
          {
            "title": "[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/abs/2605.03117"
          },
          {
            "title": "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/html/2605.03117"
          },
          {
            "title": "RepoAudit: An Autonomous LLM-Agent for Repository- ...",
            "url": "https://arxiv.org/pdf/2501.18160"
          },
          {
            "title": "INTERPROCEDURAL ANALYSIS",
            "url": "https://pages.cs.wisc.edu/~fischer/cs701.f14/6.INTERPROCEDURAL-ANALYSIS.html"
          },
          {
            "title": "[2605.00817] When LLMs Stop Following Steps: A Diagnostic Study of Procedural Execution in Language Models",
            "url": "https://arxiv.org/abs/2605.00817"
          },
          {
            "title": "Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural",
            "url": "https://www.arxiv.org/pdf/2602.06751"
          },
          {
            "title": "Retrieval from Within: An Intrinsic Capability of Attention-Based Models",
            "url": "https://arxiv.org/html/2605.05806"
          },
          {
            "title": "SkillRAE: Agent Skill-Based Context Compilation for Retrieval-Augmented Execution",
            "url": "https://arxiv.org/html/2605.10114"
          },
          {
            "title": "Beyond State Machines: Executing Network Procedures with Agentic Tool-Calling Sequences",
            "url": "https://arxiv.org/html/2605.02584"
          },
          {
            "title": "Beyond Function-Level Analysis: Context-Aware Reasoning for Inter-Procedural Vulnerability Detection",
            "url": "https://arxiv.org/html/2602.06751v1"
          }
        ]
      },
      "Based on the web search results, I found information about the arXiv paper 2605.03117:\n\nARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.\n\nRepository-level fault localization and automated program repair require an agent to identify the relevant code units across files, follow call and data dependencies, and generate a valid patch. Existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures, leaving agents without the semantic precision needed for function- and line-level localization.\n\nARISE exposes this graph through a three-tier tool API, which brings data-flow slicing as a first-class, queryable agent primitive that allows the model to trace, in a single call, which statements define or consume a variable of interest.\n\nThe paper was published on arXiv on May 4, 2026, and addresses a key gap in existing systems: none constructs statement-level nodes, none models definition-use relationships, and none exposes a first-class data-flow slicing primitive to the agent."
    ],
    "durationSeconds": 6.723058895999999
  },
  "sourceToolAssistantUUID": "49270132-91f6-4d2c-bda8-51f95eaf4f50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-15T09:59:05.904Z_

```json
{
  "parentUuid": "4603aa9f-f5bf-4cd2-b987-7230ae5e4402",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ddb1bcde-e986-4c95-b9d0-849ef783787d",
  "timestamp": "2026-05-15T09:59:05.904Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-15T09:59:08.688Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now read the actual GraphCoder paper HTML to determine whether the CCG is intra-procedural or inter-procedural. Let me fetch the arXiv HTML page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddb1bcde-e986-4c95-b9d0-849ef783787d",
  "isSidechain": false,
  "requestId": "req_011Cb4A8ajWxLFbK527BaTPa",
  "type": "assistant",
  "uuid": "bda9b8ac-2626-4fdf-a5dd-a328aeac9c77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KzitNvUPg3ox4f2Co3dmLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3127,
      "cache_read_input_tokens": 28759,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3127,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 28759,
          "cache_creation_input_tokens": 3127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3127
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

_source line 33 · 2026-05-15T09:59:09.639Z_

让我更深入查看 GraphCoder 论文的实际内容来确认 CCG 是否限于函数内部。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bda9b8ac-2626-4fdf-a5dd-a328aeac9c77",
  "isSidechain": false,
  "requestId": "req_011Cb4A8ajWxLFbK527BaTPa",
  "type": "assistant",
  "uuid": "d9f0e960-37f0-4fc0-8510-c01abf3e5a62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KzitNvUPg3ox4f2Co3dmLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3127,
      "cache_read_input_tokens": 28759,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3127,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 28759,
          "cache_creation_input_tokens": 3127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3127
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

_source line 34 · 2026-05-15T09:59:12.532Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q68udzjabaoe2zrXkvYXXX`</summary>

```json
{
  "query": "GraphCoder arxiv 2406.07003 \"code context graph\" scope statement-level function-level \"control flow\" \"data dependence\" construction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9f0e960-37f0-4fc0-8510-c01abf3e5a62",
  "isSidechain": false,
  "requestId": "req_011Cb4A8ajWxLFbK527BaTPa",
  "type": "assistant",
  "uuid": "dd232889-1cdd-436b-8dd1-2a6680b0f85d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KzitNvUPg3ox4f2Co3dmLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3127,
      "cache_read_input_tokens": 28759,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3127,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 28759,
          "cache_creation_input_tokens": 3127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3127
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

_source line 35 · 2026-05-15T09:59:12.599Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0138Yv4kUtnu5QEbqBsSSLuR`</summary>

```json
{
  "query": "ARISE arxiv 2605.03117 \"inter-procedural\" OR \"cross-function\" OR \"call graph\" data-flow edges graph construction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd232889-1cdd-436b-8dd1-2a6680b0f85d",
  "isSidechain": false,
  "requestId": "req_011Cb4A8ajWxLFbK527BaTPa",
  "type": "assistant",
  "uuid": "3b984ccb-e31b-411b-b181-4d193068e6e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KzitNvUPg3ox4f2Co3dmLa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3127,
      "cache_read_input_tokens": 28759,
      "output_tokens": 243,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3127,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 243,
          "cache_read_input_tokens": 28759,
          "cache_creation_input_tokens": 3127,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3127
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

_source line 36 · 2026-05-15T09:59:18.781Z_

<details><summary>↩ Tool result · `toolu_0138Yv4kUtnu5QEbqBsSSLuR`</summary>

```text
Web search results for query: "ARISE arxiv 2605.03117 "inter-procedural" OR "cross-function" OR "call graph" data-flow edges graph construction"

Links: [{"title":"[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/abs/2605.03117"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"},{"title":"Interprocedural Dataflow Analysis in the Presence of Large Libraries | SpringerLink","url":"https://link.springer.com/chapter/10.1007/11688839_2"},{"title":"INTERPROCEDURAL ANALYSIS","url":"https://pages.cs.wisc.edu/~fischer/cs701.f14/6.INTERPROCEDURAL-ANALYSIS.html"},{"title":"GitHub - ChrisCummins/ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations · GitHub","url":"https://github.com/ChrisCummins/ProGraML"},{"title":"Precise interprocedural dataflow analysis with applications to constant propagation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/0304397596000722"},{"title":"[1304.6274] Interprocedural Data Flow Analysis in Soot using Value Contexts","url":"https://arxiv.org/abs/1304.6274"},{"title":"PROGRAML: A Graph-based Program Representation for Data Flow Analysis","url":"http://proceedings.mlr.press/v139/cummins21a/cummins21a.pdf"},{"title":"PROGRAML: A Graph-based Program Representation for ...","url":"https://www.research.ed.ac.uk/files/221627281/PROGRAML_CUMMINS_DOA08052021_AFV.pdf"},{"title":"PhASAR: An Inter-procedural Static Analysis Framework for C/C++ | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-030-17465-1_22"}]

Based on the search results, I found information about the ARISE paper (arxiv 2605.03117):

ARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.

Regarding inter-procedural and cross-function capabilities: Existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures. The paper positions ARISE as addressing this limitation by focusing on augmenting a structural repository graph with statement-level nodes and intra-procedural def-use edges, which means the graph construction emphasizes **intra-procedural** (within-function) data-flow edges rather than inter-procedural edges.

The repository graph unifies structural and data-flow information at statement granularity, enabling agents to query not only how code is organised (files, classes, functions) but also how values are defined and propagated within a procedure.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b984ccb-e31b-411b-b181-4d193068e6e9",
  "isSidechain": false,
  "promptId": "62ec9e26-7205-4414-b673-6110d35d9a64",
  "type": "user",
  "uuid": "d636bd7c-2d61-4014-a439-40f476b50273",
  "toolUseResult": {
    "query": "ARISE arxiv 2605.03117 \"inter-procedural\" OR \"cross-function\" OR \"call graph\" data-flow edges graph construction",
    "results": [
      {
        "tool_use_id": "srvtoolu_016qiDdL3tEmDWyKV1m39tyy",
        "content": [
          {
            "title": "[2605.03117] ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/abs/2605.03117"
          },
          {
            "title": "ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair",
            "url": "https://arxiv.org/html/2605.03117"
          },
          {
            "title": "Interprocedural Dataflow Analysis in the Presence of Large Libraries | SpringerLink",
            "url": "https://link.springer.com/chapter/10.1007/11688839_2"
          },
          {
            "title": "INTERPROCEDURAL ANALYSIS",
            "url": "https://pages.cs.wisc.edu/~fischer/cs701.f14/6.INTERPROCEDURAL-ANALYSIS.html"
          },
          {
            "title": "GitHub - ChrisCummins/ProGraML: A Graph-based Program Representation for Data Flow Analysis and Compiler Optimizations · GitHub",
            "url": "https://github.com/ChrisCummins/ProGraML"
          },
          {
            "title": "Precise interprocedural dataflow analysis with applications to constant propagation - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/0304397596000722"
          },
          {
            "title": "[1304.6274] Interprocedural Data Flow Analysis in Soot using Value Contexts",
            "url": "https://arxiv.org/abs/1304.6274"
          },
          {
            "title": "PROGRAML: A Graph-based Program Representation for Data Flow Analysis",
            "url": "http://proceedings.mlr.press/v139/cummins21a/cummins21a.pdf"
          },
          {
            "title": "PROGRAML: A Graph-based Program Representation for ...",
            "url": "https://www.research.ed.ac.uk/files/221627281/PROGRAML_CUMMINS_DOA08052021_AFV.pdf"
          },
          {
            "title": "PhASAR: An Inter-procedural Static Analysis Framework for C/C++ | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-030-17465-1_22"
          }
        ]
      },
      "Based on the search results, I found information about the ARISE paper (arxiv 2605.03117):\n\nARISE (Agentic Repository-level Issue Solving Engine) augments an LLM-based agent with a multi-granularity program graph that extends structural relationships down to statement-level nodes connected by intra-procedural definition-use edges.\n\nRegarding inter-procedural and cross-function capabilities: Existing graph-based systems provide structural representations of repositories (files, classes, functions and their relationships) but do not model how variable values flow within procedures. The paper positions ARISE as addressing this limitation by focusing on augmenting a structural repository graph with statement-level nodes and intra-procedural def-use edges, which means the graph construction emphasizes **intra-procedural** (within-function) data-flow edges rather than inter-procedural edges.\n\nThe repository graph unifies structural and data-flow information at statement granularity, enabling agents to query not only how code is organised (files, classes, functions) but also how values are defined and propagated within a procedure."
    ],
    "durationSeconds": 6.176961603999996
  },
  "sourceToolAssistantUUID": "3b984ccb-e31b-411b-b181-4d193068e6e9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T09:59:20.093Z_

<details><summary>↩ Tool result · `toolu_01Q68udzjabaoe2zrXkvYXXX`</summary>

```text
Web search results for query: "GraphCoder arxiv 2406.07003 "code context graph" scope statement-level function-level "control flow" "data dependence" construction"

Links: [{"title":"[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/abs/2406.07003"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://arxiv.org/html/2406.07003v2"},{"title":"[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"},{"title":"(PDF) GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://www.researchgate.net/publication/381318841_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Code_Context_Graph-based_Retrieval_and_Language_Model"},{"title":"GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240607003L/abstract"},{"title":"Enhancing Domain-Specific Code Completion via Collaborative Inference with Large and Small Language Models | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3770748"},{"title":"GraphCoder: Enhancing Repository-Level Code ...","url":"https://arxiv.org/pdf/2406.07003"},{"title":"CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation","url":"https://arxiv.org/html/2504.10046v1"},{"title":"Prometheus: Unified Knowledge Graphs for Issue Resolution in Multilingual Codebases","url":"https://arxiv.org/html/2507.19942v1"},{"title":"[Literature Review] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model","url":"https://www.themoonlight.io/en/review/graphcoder-enhancing-repository-level-code-completion-via-code-context-graph-based-retrieval-and-language-model"}]

Based on the search results for GraphCoder (arXiv 2406.07003), here's what I found regarding the code context graph and its construction:

## Code Context Graph (CCG) Overview

GraphCoder captures the context of completion target more accurately through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements.

## Graph Composition and Construction

A code context graph is the superposition of three kinds of graphs about code: control flow graph (CFG), control dependence graph (CDG), and data dependence graph (DDG).

## Scope and Level

The CCG is a statement-level multi-graph constructed from three types of graphs—control flow graphs (CFG), control dependence graphs (CDG), and data dependence graphs (DDG). Additionally, GraphCoder constructs code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements used in retrieval-augmented code completion task.

## Benefits of Graph-Based Approach

The CCG contributes to improving retrieval effectiveness from three aspects: (1) Replacing sequence representation of code with structured representation to capture more relevant statements of the completion task; (2) Augmenting the sequence-based similarity between the context of two statements with structure-based similarity to identify deeply matched statements of the completion target from the repository; (3) Adopting a decay-with-distance structural similarity to weight the different importance of context statements to the completion target.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd232889-1cdd-436b-8dd1-2a6680b0f85d",
  "isSidechain": false,
  "promptId": "62ec9e26-7205-4414-b673-6110d35d9a64",
  "type": "user",
  "uuid": "7ccc70df-e21e-4661-86e7-3ce7801fe727",
  "toolUseResult": {
    "query": "GraphCoder arxiv 2406.07003 \"code context graph\" scope statement-level function-level \"control flow\" \"data dependence\" construction",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E5RuPv39Pn859AGv2aqPKL",
        "content": [
          {
            "title": "[2406.07003] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/abs/2406.07003"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://arxiv.org/html/2406.07003v2"
          },
          {
            "title": "[PDF] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GraphCoder:-Enhancing-Repository-Level-Code-via-and-Liu-Yu/793bbb3c70d4bac3908bd8f2ecc309f1bfdf5f52"
          },
          {
            "title": "(PDF) GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://www.researchgate.net/publication/381318841_GraphCoder_Enhancing_Repository-Level_Code_Completion_via_Code_Context_Graph-based_Retrieval_and_Language_Model"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240607003L/abstract"
          },
          {
            "title": "Enhancing Domain-Specific Code Completion via Collaborative Inference with Large and Small Language Models | ACM Transactions on Software Engineering and Methodology",
            "url": "https://dl.acm.org/doi/10.1145/3770748"
          },
          {
            "title": "GraphCoder: Enhancing Repository-Level Code ...",
            "url": "https://arxiv.org/pdf/2406.07003"
          },
          {
            "title": "CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation",
            "url": "https://arxiv.org/html/2504.10046v1"
          },
          {
            "title": "Prometheus: Unified Knowledge Graphs for Issue Resolution in Multilingual Codebases",
            "url": "https://arxiv.org/html/2507.19942v1"
          },
          {
            "title": "[Literature Review] GraphCoder: Enhancing Repository-Level Code Completion via Code Context Graph-based Retrieval and Language Model",
            "url": "https://www.themoonlight.io/en/review/graphcoder-enhancing-repository-level-code-completion-via-code-context-graph-based-retrieval-and-language-model"
          }
        ]
      },
      "Based on the search results for GraphCoder (arXiv 2406.07003), here's what I found regarding the code context graph and its construction:\n\n## Code Context Graph (CCG) Overview\n\nGraphCoder captures the context of completion target more accurately through code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements.\n\n## Graph Composition and Construction\n\nA code context graph is the superposition of three kinds of graphs about code: control flow graph (CFG), control dependence graph (CDG), and data dependence graph (DDG).\n\n## Scope and Level\n\nThe CCG is a statement-level multi-graph constructed from three types of graphs—control flow graphs (CFG), control dependence graphs (CDG), and data dependence graphs (DDG). Additionally, GraphCoder constructs code context graph (CCG) that consists of control-flow, data- and control-dependence between code statements used in retrieval-augmented code completion task.\n\n## Benefits of Graph-Based Approach\n\nThe CCG contributes to improving retrieval effectiveness from three aspects: (1) Replacing sequence representation of code with structured representation to capture more relevant statements of the completion task; (2) Augmenting the sequence-based similarity between the context of two statements with structure-based similarity to identify deeply matched statements of the completion target from the repository; (3) Adopting a decay-with-distance structural similarity to weight the different importance of context statements to the completion target."
    ],
    "durationSeconds": 7.556468009000004
  },
  "sourceToolAssistantUUID": "dd232889-1cdd-436b-8dd1-2a6680b0f85d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-15T09:59:50.828Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to make the edits. Let me summarize what I've found:

1. **GraphCoder**: The CCG (Code Context Graph) is constructed from control-flow graphs, control-dependence graphs, and data-dependence graphs at the statement level. These are classic intra-procedural analyses (CFG, CDG, DDG are standard intra-procedural constructs). However, GraphCoder operates at repository-level for code completion, so the retrieval itself is cross-file, but the graph analysis for individual code snippets appears to be intra-procedural. The paper doesn't explicitly use the term "intra-procedural" from what I can see, but CFG/CDG/DDG are inherently intra-procedural constructs. I think the current claim is essentially correct - the data-flow analysis in GraphCoder is intra-procedural.


2. **ARISE**: The paper explicitly mentions "intra-procedural definition-use edges" and adds statement-level nodes with these edges to a repository-level structural graph covering files, classes, and functions. So the data-flow component is definitively intra-procedural, even though the broader structural graph spans cross-file relationships.

For both papers, the claim about intra-procedural scope is accurate for the data-flow analysis component, though each tool also incorporates cross-file structural information at a higher level. I'm verifying that the data-flow claim holds up for both GraphCoder and ARISE—their CFG/CDG/DDG and intra-procedural definition-use edges are indeed scoped within procedures, so I'll refine the wording to "data-flow edges that remain intra-procedural" to be more precise about what's actually limited. For the second point, I'll soften the language from "all these methods" to "these methods primarily leverage" to be less absolute.

Now I need to add a clarifying note about CoCoHaNeRe in section 2.3, then insert the distinction before the StructFuse discussion, and make all four edits together. I'm noting that CoCoHaNeRe actually evaluates multiple non-gradient strategies beyond just BM25—including embedding-based approaches—and finds limitations across both, which is what drives their gradient-based solution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ccc70df-e21e-4661-86e7-3ce7801fe727",
  "isSidechain": false,
  "requestId": "req_011Cb4A9dT1V1jVxz2RcNLkk",
  "type": "assistant",
  "uuid": "b7fbd284-0a3c-43f6-96fb-10775d405165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5PLjCdpmEPCmNuchZfj3N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 1282,
      "cache_read_input_tokens": 31886,
      "output_tokens": 1727,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1282,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 849,
          "output_tokens": 1727,
          "cache_read_input_tokens": 31886,
          "cache_creation_input_tokens": 1282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1282
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

_source line 39 · 2026-05-15T09:59:52.831Z_

搜索确认了：
- **GraphCoder** 的 CCG 由 CFG/CDG/DDG 构成，均为经典 intra-procedural 分析
- **ARISE** 明确描述其 data-flow 边为 "intra-procedural definition-use edges"（但整体结构图含跨文件的 call edges）

两者的 data-flow 分析确实限于 intra-procedural，当前断言基本正确，但需更精确地指明是 data-flow 分析的 scope 而非整个系统。现在执行四项修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7fbd284-0a3c-43f6-96fb-10775d405165",
  "isSidechain": false,
  "requestId": "req_011Cb4A9dT1V1jVxz2RcNLkk",
  "type": "assistant",
  "uuid": "530eaaf0-3d54-43e3-9278-88c13093322a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5PLjCdpmEPCmNuchZfj3N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 1282,
      "cache_read_input_tokens": 31886,
      "output_tokens": 1727,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1282,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 849,
          "output_tokens": 1727,
          "cache_read_input_tokens": 31886,
          "cache_creation_input_tokens": 1282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1282
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

_source line 40 · 2026-05-15T09:59:55.487Z_

<details open><summary>🔧 Tool call — Edit · `toolu_013fR4oJMd3ByidJZkYgQp8t`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope.",
  "new_string": "GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "530eaaf0-3d54-43e3-9278-88c13093322a",
  "isSidechain": false,
  "requestId": "req_011Cb4A9dT1V1jVxz2RcNLkk",
  "type": "assistant",
  "uuid": "2cc3d686-db30-4362-85a9-a7fda1ed153c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5PLjCdpmEPCmNuchZfj3N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 849,
      "cache_creation_input_tokens": 1282,
      "cache_read_input_tokens": 31886,
      "output_tokens": 1727,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1282,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 849,
          "output_tokens": 1727,
          "cache_read_input_tokens": 31886,
          "cache_creation_input_tokens": 1282,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1282
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

_source line 41 · 2026-05-15T09:59:55.507Z_

<details><summary>↩ Tool result · `toolu_013fR4oJMd3ByidJZkYgQp8t`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2cc3d686-db30-4362-85a9-a7fda1ed153c",
  "isSidechain": false,
  "promptId": "62ec9e26-7205-4414-b673-6110d35d9a64",
  "type": "user",
  "uuid": "8d4b7eb9-b267-4567-8db2-47ec654be137",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "oldString": "GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope.",
    "newString": "GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope.",
    "originalFile": "# 2. Related Work\n\n## 2.1 Dense Retrieval for Code\n\nCode retrieval has evolved from sparse lexical methods such as BM25 \\cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \\cite{feng2020codebert}, UniXcoder \\cite{guo2022unixcoder}, and InferCode \\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \\cite{zhang2024codesage} and SCodeR \\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \\cite{jimenez2024swebench}---has motivated specialized systems: SweRank \\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.\n\n## 2.2 Contrastive Learning for Code\n\nContrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.\n\n## 2.3 Hard Negative Mining\n\nThe quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.\n\nIn the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.\n\n## 2.4 Code Structure in Machine Learning\n\nProgram dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.\n\nRecent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope. Critically, all these methods construct and query graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 4,
        "newStart": 18,
        "newLines": 4,
        "lines": [
          " ",
          " Program dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.",
          " ",
          "-Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow information but remain limited to intra-procedural scope. Critically, all these methods construct and query graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.",
          "+Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, all these methods construct and query graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "2cc3d686-db30-4362-85a9-a7fda1ed153c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "leafUuid": "8d4b7eb9-b267-4567-8db2-47ec654be137",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix related work section with fact-checking",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98"
}
```

---

### Tool call

_source line 44 · 2026-05-15T09:59:59.714Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01QKyuYCxkhKVP3Jztgd3XZw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "Critically, all these methods construct and query graphs at inference time",
  "new_string": "Critically, these methods primarily leverage structural graphs at inference time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d4b7eb9-b267-4567-8db2-47ec654be137",
  "isSidechain": false,
  "requestId": "req_011Cb4ACF1y96yPqzJ4FwkmA",
  "type": "assistant",
  "uuid": "2d21a34a-117f-4388-8668-21009d469c1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017BTaHDWqby3R6C9FXZSb6N",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2651,
      "cache_read_input_tokens": 33168,
      "output_tokens": 175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2651,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 175,
          "cache_read_input_tokens": 33168,
          "cache_creation_input_tokens": 2651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2651
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

_source line 45 · 2026-05-15T09:59:59.723Z_

<details><summary>↩ Tool result · `toolu_01QKyuYCxkhKVP3Jztgd3XZw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d21a34a-117f-4388-8668-21009d469c1b",
  "isSidechain": false,
  "promptId": "62ec9e26-7205-4414-b673-6110d35d9a64",
  "type": "user",
  "uuid": "90fe2a6a-1ff9-4298-be32-d9111dae5c24",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "oldString": "Critically, all these methods construct and query graphs at inference time",
    "newString": "Critically, these methods primarily leverage structural graphs at inference time",
    "originalFile": "# 2. Related Work\n\n## 2.1 Dense Retrieval for Code\n\nCode retrieval has evolved from sparse lexical methods such as BM25 \\cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \\cite{feng2020codebert}, UniXcoder \\cite{guo2022unixcoder}, and InferCode \\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \\cite{zhang2024codesage} and SCodeR \\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \\cite{jimenez2024swebench}---has motivated specialized systems: SweRank \\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.\n\n## 2.2 Contrastive Learning for Code\n\nContrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.\n\n## 2.3 Hard Negative Mining\n\nThe quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.\n\nIn the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.\n\n## 2.4 Code Structure in Machine Learning\n\nProgram dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.\n\nRecent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, all these methods construct and query graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 4,
        "newStart": 18,
        "newLines": 4,
        "lines": [
          " ",
          " Program dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.",
          " ",
          "-Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, all these methods construct and query graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.",
          "+Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "2d21a34a-117f-4388-8668-21009d469c1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T10:00:04.510Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01QpJSfZAig1P7AjR7RqFcgB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training.",
  "new_string": "In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. More broadly, CoCoHaNeRe evaluates several non-gradient strategies---including both BM25 and embedding-based retrieval---and finds limitations in each, motivating their differentiable approach."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90fe2a6a-1ff9-4298-be32-d9111dae5c24",
  "isSidechain": false,
  "requestId": "req_011Cb4ACYzCuuoYhtjeTcx2C",
  "type": "assistant",
  "uuid": "a331ab90-b265-406b-862b-6a374bc0940d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X9xTSjYeiQZ8tzBsqpNBrq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 35819,
      "output_tokens": 303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 236,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 303,
          "cache_read_input_tokens": 35819,
          "cache_creation_input_tokens": 236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 236
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

_source line 47 · 2026-05-15T10:00:04.527Z_

<details><summary>↩ Tool result · `toolu_01QpJSfZAig1P7AjR7RqFcgB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a331ab90-b265-406b-862b-6a374bc0940d",
  "isSidechain": false,
  "promptId": "62ec9e26-7205-4414-b673-6110d35d9a64",
  "type": "user",
  "uuid": "f67351ca-1db2-4b58-8ab3-629ffb290dc9",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "oldString": "In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training.",
    "newString": "In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. More broadly, CoCoHaNeRe evaluates several non-gradient strategies---including both BM25 and embedding-based retrieval---and finds limitations in each, motivating their differentiable approach.",
    "originalFile": "# 2. Related Work\n\n## 2.1 Dense Retrieval for Code\n\nCode retrieval has evolved from sparse lexical methods such as BM25 \\cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \\cite{feng2020codebert}, UniXcoder \\cite{guo2022unixcoder}, and InferCode \\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \\cite{zhang2024codesage} and SCodeR \\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \\cite{jimenez2024swebench}---has motivated specialized systems: SweRank \\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.\n\n## 2.2 Contrastive Learning for Code\n\nContrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.\n\n## 2.3 Hard Negative Mining\n\nThe quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.\n\nIn the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.\n\n## 2.4 Code Structure in Machine Learning\n\nProgram dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.\n\nRecent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.\n",
    "structuredPatch": [
      {
        "oldStart": 12,
        "oldLines": 7,
        "newStart": 12,
        "newLines": 7,
        "lines": [
          " ",
          " The quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.",
          " ",
          "-In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.",
          "+In the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. More broadly, CoCoHaNeRe evaluates several non-gradient strategies---including both BM25 and embedding-based retrieval---and finds limitations in each, motivating their differentiable approach. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.",
          " ",
          " ## 2.4 Code Structure in Machine Learning",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "a331ab90-b265-406b-862b-6a374bc0940d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T10:00:08.312Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01XmvQUK6JYqP7BNjzDmyWyV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
  "old_string": "These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension:",
  "new_string": "These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension:"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f67351ca-1db2-4b58-8ab3-629ffb290dc9",
  "isSidechain": false,
  "requestId": "req_011Cb4ACuNYwRLnwghNpnZUz",
  "type": "assistant",
  "uuid": "ece5d237-77db-40e7-9207-a027868a680f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116fbHdnoJYB8XisDvD9mmi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 364,
      "cache_read_input_tokens": 36055,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 364,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 216,
          "cache_read_input_tokens": 36055,
          "cache_creation_input_tokens": 364,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 364
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

_source line 49 · 2026-05-15T10:00:08.321Z_

<details><summary>↩ Tool result · `toolu_01XmvQUK6JYqP7BNjzDmyWyV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ece5d237-77db-40e7-9207-a027868a680f",
  "isSidechain": false,
  "promptId": "62ec9e26-7205-4414-b673-6110d35d9a64",
  "type": "user",
  "uuid": "3db12874-61ef-463e-a717-5c153a52390e",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
    "oldString": "These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension:",
    "newString": "These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension:",
    "originalFile": "# 2. Related Work\n\n## 2.1 Dense Retrieval for Code\n\nCode retrieval has evolved from sparse lexical methods such as BM25 \\cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \\cite{feng2020codebert}, UniXcoder \\cite{guo2022unixcoder}, and InferCode \\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \\cite{zhang2024codesage} and SCodeR \\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \\cite{jimenez2024swebench}---has motivated specialized systems: SweRank \\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.\n\n## 2.2 Contrastive Learning for Code\n\nContrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.\n\n## 2.3 Hard Negative Mining\n\nThe quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.\n\nIn the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. More broadly, CoCoHaNeRe evaluates several non-gradient strategies---including both BM25 and embedding-based retrieval---and finds limitations in each, motivating their differentiable approach. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.\n\n## 2.4 Code Structure in Machine Learning\n\nProgram dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.\n\nRecent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 7,
        "newStart": 6,
        "newLines": 7,
        "lines": [
          " ",
          " ## 2.2 Contrastive Learning for Code",
          " ",
          "-Contrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.",
          "+Contrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.",
          " ",
          " ## 2.3 Hard Negative Mining",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "ece5d237-77db-40e7-9207-a027868a680f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 50_

```json
{
  "type": "last-prompt",
  "leafUuid": "3db12874-61ef-463e-a717-5c153a52390e",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix related work section with fact-checking",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98"
}
```

---

### Assistant

_source line 52 · 2026-05-15T10:00:10.775Z_

验证最终文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3db12874-61ef-463e-a717-5c153a52390e",
  "isSidechain": false,
  "requestId": "req_011Cb4ADBm39WQ4cyzwhyKUC",
  "type": "assistant",
  "uuid": "d3793abb-8342-47d5-a784-66b5b4a65d75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GnE5uWgWw8zpi9LEU4Uar9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 36419,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 36419,
          "cache_creation_input_tokens": 277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 277
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

_source line 53 · 2026-05-15T10:00:11.155Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Sh89ei8kVpQ5TSCkLp17eJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3793abb-8342-47d5-a784-66b5b4a65d75",
  "isSidechain": false,
  "requestId": "req_011Cb4ADBm39WQ4cyzwhyKUC",
  "type": "assistant",
  "uuid": "7918b1ce-7234-4961-b517-7de9e73f12d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GnE5uWgWw8zpi9LEU4Uar9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 36419,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 36419,
          "cache_creation_input_tokens": 277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 277
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

_source line 54 · 2026-05-15T10:00:11.160Z_

<details><summary>↩ Tool result · `toolu_01Sh89ei8kVpQ5TSCkLp17eJ`</summary>

```text
1	# 2. Related Work
2	
3	## 2.1 Dense Retrieval for Code
4	
5	Code retrieval has evolved from sparse lexical methods such as BM25 \cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \cite{feng2020codebert}, UniXcoder \cite{guo2022unixcoder}, and InferCode \cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \cite{lozhkov2024starcoder2} and Qwen2.5-Coder \cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \cite{zhang2024codesage} and SCodeR \cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \cite{jimenez2024swebench}---has motivated specialized systems: SweRank \cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.
6	
7	## 2.2 Contrastive Learning for Code
8	
9	Contrastive learning has become a dominant paradigm for code representation learning. ContraCode \cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.
10	
11	## 2.3 Hard Negative Mining
12	
13	The quality of negative examples critically affects contrastive learning \cite{chen2020simclr}. In dense text retrieval, DPR \cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \cite{zeng2022cldrd} and CAPSTONE \cite{he2023capstone}---schedule negative difficulty progressively during training.
14	
15	In the code domain, CoCoHaNeRe \cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. More broadly, CoCoHaNeRe evaluates several non-gradient strategies---including both BM25 and embedding-based retrieval---and finds limitations in each, motivating their differentiable approach. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.
16	
17	## 2.4 Code Structure in Machine Learning
18	
19	Program dependence graphs \cite{ferrante1987pdg} and code property graphs \cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.
20	
21	Recent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \cite{liu2025codexgraph} and RepoGraph \cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \cite{chen2025locagent} and RANGER \cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \cite{liu2024graphcoder} and ARISE \cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7918b1ce-7234-4961-b517-7de9e73f12d5",
  "isSidechain": false,
  "promptId": "62ec9e26-7205-4414-b673-6110d35d9a64",
  "type": "user",
  "uuid": "98dd95e8-3a25-4511-8902-f0ea720bdf02",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/paper_drafts/related_work_v1.md",
      "content": "# 2. Related Work\n\n## 2.1 Dense Retrieval for Code\n\nCode retrieval has evolved from sparse lexical methods such as BM25 \\cite{robertson2009bm25} to dense neural approaches. Early pretrained code models---CodeBERT \\cite{feng2020codebert}, UniXcoder \\cite{guo2022unixcoder}, and InferCode \\cite{bui2021infercode}---learn general-purpose code representations through masked language modeling and related pretraining objectives, enabling semantic matching beyond surface-level token overlap. More recent large-scale code models, including StarCoder2 \\cite{lozhkov2024starcoder2} and Qwen2.5-Coder \\cite{hui2024qwen25coder}, provide powerful encoder backbones trained on trillions of code tokens. In the retrieval domain, CodeSage \\cite{zhang2024codesage} and SCodeR \\cite{li2022scoder} introduce contrastive fine-tuning strategies that adapt pretrained representations for code search. The growing importance of repository-level retrieval---driven by benchmarks like SWE-bench \\cite{jimenez2024swebench}---has motivated specialized systems: SweRank \\cite{reddy2025swerank} formulates issue localization as code ranking, while SWE-Fixer \\cite{xie2025swefixer} combines BM25 with neural reranking in a coarse-to-fine pipeline. StructFuse builds on this foundation by improving the contrastive fine-tuning stage: rather than modifying the retrieval architecture, we enhance the training signal through structure-grounded negative selection.\n\n## 2.2 Contrastive Learning for Code\n\nContrastive learning has become a dominant paradigm for code representation learning. ContraCode \\cite{jain2021contracode} generates functionally equivalent program variants through compiler transformations, training models to be invariant to syntactic variation. CodeRetriever \\cite{li2022coderetriever} combines unimodal code-code and bimodal code-text contrastive objectives, achieving strong results across eleven code search benchmarks. SynCoBERT \\cite{wang2021syncobert} introduces syntax-guided multi-modal contrastive pretraining that aligns code, natural language, and AST modalities through identifier prediction and edge prediction objectives. ContraBERT \\cite{liu2023contrabert} takes a complementary robustness-oriented approach, designing adversarial augmentation operators---including identifier renaming, dead code insertion, and operand swapping---to improve model robustness while maintaining retrieval performance. GraphCodeBERT \\cite{guo2021graphcodebert} incorporates data-flow edges into pretraining, demonstrating that structural information improves code understanding tasks. These methods enrich the positive pair construction space or the pretraining signal. While GraphCodeBERT uses structural edges as a pretraining objective, StructFuse addresses a complementary dimension: rather than improving how positive pairs are constructed, we improve which negatives the model trains against by grounding selection in inter-procedural data-flow structure.\n\n## 2.3 Hard Negative Mining\n\nThe quality of negative examples critically affects contrastive learning \\cite{chen2020simclr}. In dense text retrieval, DPR \\cite{karpukhin2020dpr} established the practice of using BM25 top-ranked non-relevant passages as hard negatives. ANCE \\cite{xiong2021ance} dynamically mines negatives from an approximate nearest neighbor index updated during training, while RocketQA \\cite{qu2021rocketqa} introduces cross-batch denoised negatives with knowledge distillation. STAR \\cite{zhan2021star} further refines this paradigm by using the retriever's own top-ranked passages as training negatives. Curriculum-based approaches---CL-DRD \\cite{zeng2022cldrd} and CAPSTONE \\cite{he2023capstone}---schedule negative difficulty progressively during training.\n\nIn the code domain, CoCoHaNeRe \\cite{fan2025cocohanere} proposes gradient-based hard negative mining for code search and reports that BM25-selected negatives can be detrimental to contrastive training. More broadly, CoCoHaNeRe evaluates several non-gradient strategies---including both BM25 and embedding-based retrieval---and finds limitations in each, motivating their differentiable approach. StructFuse takes a different approach: we use static embedding-distance mining as a strong baseline and introduce data-flow structure as an orthogonal signal for negative selection, requiring no gradient computation or dynamic index updates.\n\n## 2.4 Code Structure in Machine Learning\n\nProgram dependence graphs \\cite{ferrante1987pdg} and code property graphs \\cite{yamaguchi2014cpg} have long served program analysis; tools like CodeQL \\cite{avgustinov2016ql} make inter-procedural analysis accessible at scale. In machine learning, code2vec \\cite{alon2019code2vec} pioneered learning from AST paths, while ProGraML \\cite{cummins2021programl} demonstrated that whole-program graph representations capturing control-flow, data-flow, and call relations are learnable and effective for compiler optimization tasks. CrossCodeEval \\cite{ding2023crosscodeeval} empirically validates that cross-file context is critical for code completion, with retrieval-augmented approaches yielding clear but still far-from-ceiling improvements.\n\nRecent inference-time graph methods bring structural reasoning to LLM-based software engineering. CodexGraph \\cite{liu2025codexgraph} and RepoGraph \\cite{ouyang2025repograph} build navigable code graph databases for LLM agents; LocAgent \\cite{chen2025locagent} and RANGER \\cite{shah2025ranger} employ multi-hop graph reasoning and MCTS-based traversal for fault localization and retrieval, respectively. GraphCoder \\cite{liu2024graphcoder} and ARISE \\cite{seddik2026arise} incorporate data-flow edges---control/data dependence and definition-use chains, respectively---but their data-flow analysis remains intra-procedural in scope. Critically, these methods primarily leverage structural graphs at inference time, incurring per-query latency proportional to graph complexity. StructFuse takes a fundamentally different approach: we leverage inter-procedural data-flow graphs at \\emph{training time} to mine structure-grounded negatives, producing an encoder that internalizes cross-function data-flow semantics with zero inference overhead. The two paradigms are complementary---a StructFuse-trained encoder can serve as an efficient first-stage retriever for inference-time graph systems that perform targeted reranking.\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  },
  "sourceToolAssistantUUID": "7918b1ce-7234-4961-b517-7de9e73f12d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 55 · 2026-05-15T10:00:11.222Z_

```json
{
  "parentUuid": "98dd95e8-3a25-4511-8902-f0ea720bdf02",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c4837cfb-c1e1-4394-a1f7-8d6b01c3fc6b",
  "timestamp": "2026-05-15T10:00:11.222Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 56 · 2026-05-15T10:00:19.616Z_

四项修改完成，摘要如下：

**修正 1 (§2.4)** — GraphCoder/ARISE scope：WebSearch 确认两者的 data-flow 分析确实是 intra-procedural（GraphCoder 用 CFG/CDG/DDG，ARISE 明确描述为 "intra-procedural definition-use edges"）。保留 intra-procedural 断言，但改写为更精确的表述，区分了两者各自的 data-flow 类型（control/data dependence vs. definition-use chains），并明确是 "data-flow analysis" 而非整个系统受限于 intra-procedural。

**修正 2 (§2.4)** — "all these methods" → "these methods primarily leverage structural graphs at inference time"，软化了全称断言。

**修正 3 (§2.3)** — CoCoHaNeRe 句后新增一句，说明该工作同时评估了多种非梯度策略（BM25 和 embedding-based），消除与 Introduction（批评 embedding negatives）的表述不一致。

**修正 4 (§2.2)** — 在 StructFuse 定位句前插入半句 "While GraphCodeBERT uses structural edges as a pretraining objective"，明确区分 pretraining objective vs. training-time negative selection。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4837cfb-c1e1-4394-a1f7-8d6b01c3fc6b",
  "isSidechain": false,
  "requestId": "req_011Cb4ADQ5he3XFYYvhSi4LJ",
  "type": "assistant",
  "uuid": "73c84579-8acc-426a-84f5-a21fbe750f91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018tZGctoP4LjYeHdAZPyADS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1836,
      "cache_read_input_tokens": 36696,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1836,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 367,
          "cache_read_input_tokens": 36696,
          "cache_creation_input_tokens": 1836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1836
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

_source line 57_

```json
{
  "type": "last-prompt",
  "leafUuid": "73c84579-8acc-426a-84f5-a21fbe750f91",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix related work section with fact-checking",
  "sessionId": "559ab8d5-54a8-4e66-9e37-55b92c9e8c98"
}
```

---
