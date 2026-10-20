# Research conversation: <project_context> # 项目: exec-sim-repair-verifier ## 运行环境 - 服务器名: seetacloud-westd-4x5090 - SSH 账户: root（调用 ssh_execute /

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/2c27d302-54b8-4f87-80cf-476c5bb38813.jsonl`
- **Structured JSON:** [`16b741c8e070616863de.json`](../../sessions/16/16b741c8e070616863de.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T15:04:07.223Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T15:04:07.223Z",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "content": "&lt;project_context>\n# 项目: exec-sim-repair-verifier\n\n## 运行环境\n- 服务器名: seetacloud-westd-4x5090\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /home/sonny/exec-sim-repair-verifier\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：将 experiments.tex 从 artifacts 同步到 docs/paper/，合并 lr fix\n\n### 背景\n- `artifacts/_project/paper/experiments.tex` 是 experiments-draft Worker 写的完整草稿\n- `docs/paper/experiments.tex` 是编译用的源文件，之前已有 lr fix（$2{\\times}10^{-4}$ function-level / $5{\\times}10^{-5}$ repo-level）\n- 需要将 artifacts 版本的完整内容同步到 docs/paper/，但确保 lr 值是正确的\n\n### 步骤\n\n1. **Read 两个文件**：\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/experiments.tex`（artifacts 完整草稿）\n   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex`（当前编译版本，含 lr fix）\n\n2. **同步策略**：\n   - 将 artifacts 版本的内容写入 docs/paper/experiments.tex\n   - 但必须确保最终版本中 lr 值正确：function-level 用 $2{\\times}10^{-4}$，repo-level 用 $5{\\times}10^{-5}$\n   - 如果 artifacts 版本的 lr 还是错的（$2{\\times}10^{-5}$），在同步时修正\n\n3. **引用 key 检查**：\n   - 确保使用 `shum2025swerm`（不是 zhang2025swerm）\n   - 确保使用 `maimon2026selfexecution`（不是 ding2025selfexecution）\n\n4. **验证**：\n   - Read 最终文件确认 lr 值正确\n   - grep 确认无旧引用 key\n   - grep 确认无 $2{\\times}10^{-5}$（在 lr 上下文）\n\n5. **注意事项**：\n   - paragraph (h) rank ablation 部分保持原样——等实验完成后再更新\n   - Table 4 CLS 8B s42 数字保持原样——等 val-sweep 完成后更新\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T15:04:07.226Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T15:04:07.226Z",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813"
}
```

---

## Round 1

23 recorded events

### User

_source line 3 · 2026-05-15T15:04:07.263Z_

&lt;project_context>
# 项目: exec-sim-repair-verifier

## 运行环境
- 服务器名: seetacloud-westd-4x5090
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh connect.westd.seetacloud.com  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /home/sonny/exec-sim-repair-verifier


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：将 experiments.tex 从 artifacts 同步到 docs/paper/，合并 lr fix

### 背景
- `artifacts/_project/paper/experiments.tex` 是 experiments-draft Worker 写的完整草稿
- `docs/paper/experiments.tex` 是编译用的源文件，之前已有 lr fix（$2{\times}10^{-4}$ function-level / $5{\times}10^{-5}$ repo-level）
- 需要将 artifacts 版本的完整内容同步到 docs/paper/，但确保 lr 值是正确的

### 步骤

1. **Read 两个文件**：
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/experiments.tex`（artifacts 完整草稿）
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex`（当前编译版本，含 lr fix）

2. **同步策略**：
   - 将 artifacts 版本的内容写入 docs/paper/experiments.tex
   - 但必须确保最终版本中 lr 值正确：function-level 用 $2{\times}10^{-4}$，repo-level 用 $5{\times}10^{-5}$
   - 如果 artifacts 版本的 lr 还是错的（$2{\times}10^{-5}$），在同步时修正

3. **引用 key 检查**：
   - 确保使用 `shum2025swerm`（不是 zhang2025swerm）
   - 确保使用 `maimon2026selfexecution`（不是 ding2025selfexecution）

4. **验证**：
   - Read 最终文件确认 lr 值正确
   - grep 确认无旧引用 key
   - grep 确认无 $2{\times}10^{-5}$（在 lr 上下文）

5. **注意事项**：
   - paragraph (h) rank ablation 部分保持原样——等实验完成后再更新
   - Table 4 CLS 8B s42 数字保持原样——等 val-sweep 完成后更新


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d23e62c5-31bd-43a9-9cde-fc27110c6abe",
  "type": "user",
  "uuid": "841cbc63-6791-4a70-8408-d188550c469f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T15:04:07.263Z_

```json
{
  "parentUuid": "841cbc63-6791-4a70-8408-d188550c469f",
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
  "uuid": "76e8992d-adda-4a24-98d2-41adafdca246",
  "timestamp": "2026-05-15T15:04:07.263Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T15:04:07.263Z_

```json
{
  "parentUuid": "76e8992d-adda-4a24-98d2-41adafdca246",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "7c8b2134-bc6a-4eda-aab8-713271f13da5",
  "timestamp": "2026-05-15T15:04:07.263Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T15:04:07.263Z_

```json
{
  "parentUuid": "7c8b2134-bc6a-4eda-aab8-713271f13da5",
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
  "uuid": "bd0088c5-4a87-472d-a188-af0913f76428",
  "timestamp": "2026-05-15T15:04:07.263Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7 · 2026-05-15T15:04:07.263Z_

```json
{
  "parentUuid": "bd0088c5-4a87-472d-a188-af0913f76428",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7f6c7741-bef1-40b4-99d9-5fa2329ccc25",
  "timestamp": "2026-05-15T15:04:07.263Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Sync experiments.tex and merge lr fix",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813"
}
```

---

### Assistant

_source line 9 · 2026-05-15T15:04:09.807Z_

Reading both files to compare them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f6c7741-bef1-40b4-99d9-5fa2329ccc25",
  "isSidechain": false,
  "requestId": "req_011Cb4ZPfFiys4bQoz5H21we",
  "type": "assistant",
  "uuid": "9c8560f5-6603-4fc8-a95f-c0b668058e8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014C28jekJvKExrjbakDjL9u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11809,
      "cache_read_input_tokens": 11447,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 174,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11809
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

_source line 10 · 2026-05-15T15:04:10.311Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MZWu2FTyhz6TL2RNYw441v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c8560f5-6603-4fc8-a95f-c0b668058e8e",
  "isSidechain": false,
  "requestId": "req_011Cb4ZPfFiys4bQoz5H21we",
  "type": "assistant",
  "uuid": "2c262053-8133-4103-bc20-6d3efe980178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014C28jekJvKExrjbakDjL9u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11809,
      "cache_read_input_tokens": 11447,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 174,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11809
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

_source line 11 · 2026-05-15T15:04:10.394Z_

<details><summary>↩ Tool result · `toolu_01MZWu2FTyhz6TL2RNYw441v`</summary>

```text
1	% Experiments draft — generated 2026-05-15, numbers from registry
2	% NOTE: All numbers cross-checked against experiment registry.
3	% exp_id references provided for key claims.
4	
5	\section{Experiments}
6	\label{sec:experiments}
7	
8	We evaluate the three formulations defined in \S\ref{sec:method} across two complexity levels---function-level and repository-level---to test the prediction that classification gains an increasing advantage over generation as code complexity grows.
9	
10	\subsection{Experimental Setup}
11	\label{ssec:setup}
12	
13	\paragraph{Function-Level Data.}
14	We construct a function-level benchmark from HumanEval~\citep{chen2021humaneval} and MBPP~\citep{austin2021mbpp} by applying five categories of systematic mutations---\texttt{off\_by\_one}, \texttt{operator\_swap}, \texttt{variable\_swap}, \texttt{return\_value}, and \texttt{boundary\_removal}---to correct solutions, yielding 19,076 (code, test, label) triples.
15	We split by problem identity: 15,290 train / 1,896 validation / 1,890 test, with zero problem overlap between splits.
16	The test set is approximately class-balanced (51.7\% \textsc{Pass}, 48.3\% \textsc{Fail}).
17	
18	\paragraph{Repo-Level Data.}
19	We derive a per-test verification dataset from SWE-bench Verified~\citep{jimenez2024swebench} by pairing each candidate patch with individual test cases and their ground-truth outcomes.
20	The resulting dataset contains approximately 70K training samples, 9,335 validation samples, and 9,784 test samples.
21	The test set is class-imbalanced (72.96\% \textsc{Pass}); we report the majority-class baseline throughout.
22	Validation and test splits have zero problem overlap and exhibit a mutation-type composition shift (operator\_swap: 19.1\% val $\to$ 34.3\% test), which we discuss in \S\ref{ssec:analysis}.
23	
24	\paragraph{Models and Training.}
25	All models use Qwen3~\citep{qwen2025qwen3} as the base architecture with LoRA adaptation~\citep{hu2022lora} (rank$=$16, $\alpha$$=$32).
26	We train Qwen3-4B and Qwen3-8B variants for CLS, CWM, and TRAJ formulations.
27	Training uses AdamW with learning rate $2 \times 10^{-4}$ (function-level) or $5 \times 10^{-5}$ (repo-level), weight decay 0.01, warmup ratio 0.05, batch size 32 (effective), and 3 epochs.
28	Function-level experiments use seeds 42, 123, 456, 789, and 0 (five seeds); 8B scaling experiments use seeds 42, 123, and 456 (three matched pairs).
29	Seeds 42/123/456 use bfloat16 precision; seeds 789 and 0 use NF4 quantization due to hardware constraints.\footnote{NF4 seeds appear only in 4B paired comparisons (\S\ref{ssec:equivalence}), where the within-seed paired design controls for quantization effects.}
30	
31	\paragraph{Checkpoint Selection.}
32	All reported results use validation-selected checkpoints: we sweep all saved checkpoints on the validation split and select the one with highest accuracy, then evaluate on the held-out test split exactly once.
33	
34	\paragraph{Statistical Methods.}
35	We report seed-level means $\pm$ sample standard deviations.
36	For the CLS--CWM comparison, we use seed-paired bootstrap (10,000 resamples) with one-sided tests.
37	For CLS--TRAJ equivalence, we apply the two one-sided tests (TOST) procedure~\citep{schuirmann1987tost} with a pre-specified $\pm$2 percentage-point (pp) equivalence margin.
38	For repo-level results with clustered per-test predictions, we use clustered bootstrap with 114 problem-level clusters and 10,000 resamples.
39	We report the intra-cluster correlation coefficient (ICC) and design effect (DEFF) to characterize block-correlation structure.
40	
41	
42	\subsection{Function-Level Results}
43	\label{ssec:func_results}
44	
45	% exp_id: multi-seed-core, cwm-baseline, cwm-seed{123,456,789,0},
46	%         cls-seed{789,0}, traj-level-{finetuned,seed123,seed456,seed789,seed0},
47	%         llm-judge-8b-zeroshot, llm-judge-32b-zeroshot
48	
49	\begin{table}[t]
50	\centering
51	\small
52	\begin{tabular}{llcc}
53	\toprule
54	\textbf{Method} & \textbf{Model} & \textbf{Accuracy (\%)} & \textbf{Seeds} \\
55	\midrule
56	CLS & Qwen3-4B & 88.43 $\pm$ 0.78 & 5 \\
57	CWM & Qwen3-4B & 87.19 $\pm$ 0.37 & 5 \\
58	TRAJ & Qwen3-4B & 86.30 $\pm$ 0.97 & 5 \\
59	\midrule
60	ZS Judge & Qwen3-8B & 64.40 & 1 \\
61	ZS Judge & Qwen3-32B\textsuperscript{\textdagger} & 71.69 & 1 \\
62	\bottomrule
63	\end{tabular}
64	\caption{Function-level per-test verification accuracy on HumanEval+MBPP mutants ($n$$=$$1{,}890$). CLS, CWM, and TRAJ are fine-tuned with LoRA; ZS Judge uses zero-shot prompting. \textsuperscript{\textdagger}NF4 quantization. All three fine-tuned formulations achieve $>$86\% accuracy, substantially outperforming zero-shot baselines.}
65	\label{tab:func_results}
66	\end{table}
67	
68	Table~\ref{tab:func_results} presents function-level results.
69	All three fine-tuned formulations---CLS, CWM, and TRAJ---achieve strong accuracy in the 86--89\% range, with CLS leading at 88.43\%.
70	
71	\paragraph{CLS vs.\ CWM.}
72	CLS outperforms CWM by 1.24pp across five matched seeds (bootstrap 95\% CI: [0.46, 2.04], one-sided $p = 0.025$).
73	The gap is consistent: CLS achieves higher accuracy in all five seed pairs, with per-seed gaps ranging from 0.32pp (seed 42) to 2.33pp (seed 789).
74	While statistically significant, this gap is modest---both formulations achieve near-equivalent accuracy on function-level code where execution outputs are short and CWM failure modes rarely activate.
75	
76	\paragraph{Zero-shot baselines.}
77	Zero-shot LLM-as-judge performance lags far behind fine-tuned models: Qwen3-8B achieves only 64.40\% and Qwen3-32B (NF4) reaches 71.69\%, both exhibiting a systematic bias toward predicting \textsc{Fail} (fail recall $>$92\%, pass recall $<$53\%).
78	The 16.7pp gap between the 32B zero-shot model and the fine-tuned 4B CLS confirms that task-specific fine-tuning is essential for execution simulation, and that the classification formulation's advantage is not an artifact of model scale.
79	
80	
81	\subsection{Scaling Behavior}
82	\label{ssec:scaling}
83	
84	% exp_id: model-size-scaling-cls8b, cls8b-seed{123,456},
85	%         model-size-scaling-cwm8b, cwm8b-seed{123,456}
86	
87	\begin{table}[t]
88	\centering
89	\small
90	\begin{tabular}{lcccc}
91	\toprule
92	\textbf{Method} & \textbf{4B} & \textbf{8B} & \textbf{$\Delta$} & \textbf{Gap} \\
93	\midrule
94	CLS & 88.43 & 89.39 $\pm$ 1.09 & +0.96 & \multirow{2}{*}{} \\
95	CWM & 87.19 & 86.96 $\pm$ 0.72 & $-$0.23 & \\
96	\midrule
97	CLS$-$CWM & 1.24 & 2.43 & & $p = 0.008$ \\
98	\bottomrule
99	\end{tabular}
100	\caption{Scaling from 4B to 8B on function-level data. 4B uses five seeds; 8B uses three matched seeds (42, 123, 456). CLS gains +0.96pp from scaling; CWM loses $-$0.23pp. The CLS--CWM gap nearly doubles from 1.24pp to 2.43pp ($p = 0.008$).}
101	\label{tab:scaling}
102	\end{table}
103	
104	Table~\ref{tab:scaling} examines scaling behavior by comparing 4B and 8B models with three matched seed pairs per formulation.
105	The key finding is asymmetric: CLS gains +0.96pp from doubling model size (88.43\% $\to$ 89.39\%), while CWM shows no improvement ($-$0.23pp, 87.19\% $\to$ 86.96\%).
106	The CLS--CWM gap consequently widens from 1.24pp at 4B to 2.43pp at 8B ($p = 0.008$, paired $t$-test across three seeds).
107	
108	This asymmetry is consistent with a \emph{generation bottleneck} rather than a capacity limitation.
109	If CWM's lower accuracy were due to insufficient model capacity, scaling should help CWM at least as much as CLS.
110	Instead, the generation formulation appears to have a ceiling imposed by the exact-match evaluation criterion: additional capacity helps the model produce better token-level predictions, but exact-match accuracy is dominated by the hardest output tokens (precision-sensitive numbers, formatting characters) where even small errors cause failure.
111	Classification sidesteps this bottleneck entirely---the model need only determine whether the output \emph{would differ} from the expected value, not reconstruct the differing string.
112	
113	
114	\subsection{Per-Test vs.\ Trajectory-Level Equivalence}
115	\label{ssec:equivalence}
116	
117	% exp_id: 5-paired-clustered-bootstrap, block-corr-empirical
118	
119	Per-test classification decomposes the verification task into $|T|$ binary predictions that are aggregated to a patch verdict by conjunction.
120	This decomposition could either help (richer signal) or hurt (error compounding).
121	We compare CLS (aggregated to variant level) against TRAJ across five matched seed pairs using the clustered bootstrap framework from \S\ref{ssec:setup}.
122	
123	The pooled CLS--TRAJ gap is $-$0.45pp (95\% CI: [$-$1.71, +0.84], $p = 0.499$), with per-seed gaps ranging from $-$1.84pp (seed 456) to +1.45pp (seed 123).
124	A TOST equivalence test confirms that the two formulations are statistically equivalent within $\pm$2pp ($p = 0.007$).
125	We justify this margin on the basis of the block-correlation structure: with an empirically estimated ICC of 0.191 and design effect of 3.97 (\S\ref{ssec:analysis}), a 2pp variant-level difference corresponds to substantially less than 1pp in effective independent predictions.
126	
127	The practical implication is that per-test classification achieves the \emph{same} patch-level accuracy as trajectory-level scoring while providing strictly more information: for each patch, CLS identifies which specific tests are predicted to fail, enabling diagnostic applications (targeted re-repair, failure triage) that trajectory-level verifiers cannot support.
128	
129	
130	\subsection{Accuracy-Utility Frontier}
131	\label{ssec:frontier}
132	
133	% exp_id: oracle-f2p-stratified, p2p-regression-rate
134	
135	\begin{table}[t]
136	\centering
137	\small
138	\begin{tabular}{lccc}
139	\toprule
140	$|T_{\textsc{f2p}}|$ & \textbf{\% Instances} & \textbf{Block Adv.\ (pp)} & \textbf{Contrib.\ (\%)} \\
141	\midrule
142	1 & 68.7 & $-$0.09 & --- \\
143	2 & 19.1 & 31.69 & 55.3 \\
144	3--5 & 7.1 & 40.74 & 26.3 \\
145	$\geq$ 6 & 5.1 & 40.06 & 18.4 \\
146	\bottomrule
147	\end{tabular}
148	\caption{Oracle accuracy-utility frontier stratified by the number of fail-to-pass tests $|T_{\textsc{f2p}}|$ in SWE-bench Verified. Block advantage measures the oracle gain from per-test over trajectory-level verification under the empirical ICC. The advantage concentrates in instances with $T \geq 2$ (31.3\% of instances, 100\% of advantage).}
149	\label{tab:frontier}
150	\end{table}
151	
152	Per-test verification provides value only when per-test predictions carry actionable information.
153	Table~\ref{tab:frontier} stratifies the per-test oracle advantage by the number of fail-to-pass tests ($|T_{\textsc{f2p}}|$) using the empirical correlation structure (ICC$=$0.191).
154	
155	When $|T_{\textsc{f2p}}| = 1$ (68.7\% of SWE-bench Verified instances), per-test and trajectory-level formulations are informationally equivalent: there is only one fail-to-pass test, so knowing \emph{which} test fails adds nothing beyond knowing \emph{that} a test fails.
156	The advantage concentrates in multi-test instances: at $|T_{\textsc{f2p}}| = 2$ (19.1\% of instances), the block-correlated oracle advantage is 31.69pp, accounting for 55.3\% of the total advantage.
157	
158	\paragraph{Pass-to-pass regression rate.}
159	We also examine whether per-test verification provides value through pass-to-pass (P2P) regression detection.
160	Empirically, the P2P regression rate on SWE-bench Verified is approximately 1\% (mean; 0\% median) across incorrect patches: 77\% of incorrect patches break zero P2P tests.
161	At this rate, per-test verification offers negligible advantage on the P2P dimension---the signal is too sparse.
162	We report this as an honest negative: the per-test formulation's value on SWE-bench Verified derives primarily from fail-to-pass discrimination in multi-test instances, not from regression detection.
163	The practical decision boundary is $|T_{\textsc{f2p}}| \geq 2$: below this threshold, trajectory-level scoring suffices.
164	
165	
166	\subsection{Repo-Level Results}
167	\label{ssec:repo_results}
168	
169	% exp_id: repo-level-cls-v5, repo-level-cwm-v12, repo-level-cwm-seed123-conda,
170	%         cls8b-s42-ckpt1000-test8192-eval, cls8b-seed123-ckpt3000-test8192-eval
171	
172	\begin{table}[t]
173	\centering
174	\small
175	\begin{tabular}{llcccc}
176	\toprule
177	\textbf{Method} & \textbf{Size} & \textbf{Seed} & \textbf{Acc (\%)} & \textbf{Unp.\ (\%)} & \textbf{vs Maj.} \\
178	\midrule
179	\multicolumn{6}{l}{\emph{Majority baseline}} \\
180	--- & --- & --- & 72.96 & --- & 0 \\
181	\midrule
182	\multicolumn{6}{l}{\emph{Same-size comparison (primary)}} \\
183	CLS & 4B & 42 & 83.63 & 1.3 & +10.67 \\
184	CWM & 4B & 42 & 58.04 & 53.7 & $-$14.92 \\
185	CWM & 4B & 123 & 59.09 & 67.2 & $-$13.87 \\
186	\midrule
187	\multicolumn{6}{l}{\emph{Cross-size comparison (secondary)}} \\
188	CLS & 8B & 42 & 83.52 & 0.0 & +10.56 \\
189	CLS & 8B & 123 & 85.60 & 0.0 & +12.64 \\
190	CWM & 8B & 42 & \multicolumn{3}{c}{\emph{in progress}} \\
191	\bottomrule
192	\end{tabular}
193	\caption{Repo-level verification on SWE-bench Verified ($n$$=$$9{,}784$). Unp.\ = unparseable prediction rate. CLS outperforms CWM by 25.59pp at matched 4B scale. CWM falls below the majority baseline in both seeds, with 54--67\% of predictions unparseable.}
194	\label{tab:repo_results}
195	\end{table}
196	
197	Table~\ref{tab:repo_results} presents the central result: at repository-level complexity, the CLS--CWM gap explodes from the 1--2pp range observed at function level to over 25pp.
198	
199	\paragraph{Primary comparison (same-size 4B).}
200	At matched model scale and seed, CLS achieves 83.63\% accuracy versus CWM at 58.04\%---a 25.59pp gap.
201	The gap is driven by CWM's catastrophic failure on repo-level code: 53.7--67.2\% of CWM predictions are unparseable (the model generates execution traces that consume the entire token budget without reaching a verdict).
202	CWM accuracy falls \emph{below} the majority baseline (72.96\%) by approximately 14pp in both seeds, meaning the CWM verifier provides negative value compared to always predicting the majority class.
203	Among the minority of parseable CWM predictions, accuracy is only 42--43\%---below random chance---indicating that the model is anti-informative even when it produces interpretable output.
204	
205	\paragraph{Secondary comparison (cross-size).}
206	Two 8B CLS seeds confirm the pattern: CLS at 83.52\% (seed 42) and 85.60\% (seed 123) versus matched-seed 4B CWM at 58.04\% and 59.09\%, yielding gaps of 25.48pp and 26.51pp respectively.
207	8B CWM training on repo-level data is in progress; we will include 8B--8B comparisons in the final version.
208	
209	\paragraph{Gap amplification.}
210	The CLS--CWM gap follows a clear complexity gradient: 1.24pp at function-level 4B, 2.43pp at function-level 8B, and $\sim$25pp at repo-level 4B.
211	This 20$\times$ amplification from function-level to repo-level confirms the complexity-dependent reformulation advantage predicted by the failure-mode analysis in \S\ref{ssec:failure_modes}: on simple code with short outputs, the generation formulation copes; on complex code with long traces, it collapses.
212	
213	
214	\subsection{Analysis}
215	\label{ssec:analysis}
216	
217	% exp_id: cwm-rank32-ablation-v2, cls8b-s42-ckpt1000-test-seq2048-ablation,
218	%         block-corr-empirical
219	
220	\paragraph{Error complementarity.}
221	CLS and CWM exhibit systematically opposite error patterns on function-level data.
222	Of CLS errors, 75.5\% are false negatives (missed bugs: the model predicts \textsc{Pass} for a truly failing test), while 83.1\% of CWM errors are false positives (false alarms: the model predicts \textsc{Fail} for a truly passing test).
223	An oracle that selects the correct prediction whenever the two models disagree achieves 90.63\% accuracy---a 2.20pp gain over CLS alone and 3.44pp over CWM.
224	This complementarity suggests that formulation diversity (combining classification and generation verifiers) may be a productive strategy for verification pipelines, even at function-level complexity where the individual formulations achieve similar accuracy.
225	
226	\paragraph{CWM error-mode breakdown.}
227	A detailed analysis of 500 repo-level CWM predictions reveals three error modes in order of prevalence.
228	\emph{Token-budget exhaustion} (77\% of unparseable predictions): the model generates realistic pytest execution traces---dots, warnings, file paths---that consume the entire 1,024-token generation budget before reaching any pass/fail verdict.
229	\emph{Keyword ambiguity} (23\% of unparseable): the generated trace contains both pass-indicating and fail-indicating keywords (e.g., test names containing ``fail,'' deprecation warnings alongside success indicators), preventing reliable keyword extraction.
230	Among the minority of parseable predictions, the model hallucinates failures: 90\% of parseable errors are \textsc{Pass}$\to$\textsc{Fail} misclassifications (64 of 71 wrong parseable predictions).
231	These failure modes are structural to the generation formulation and cannot be addressed by increasing model capacity---as confirmed by the CWM scaling results in \S\ref{ssec:scaling}.
232	
233	\paragraph{Per-repository variation.}
234	CWM unparseable rates vary dramatically across repositories: from $\sim$0\% on scikit-learn (concise test output) to 100\% on sphinx (verbose build output).
235	This variation reflects a fundamental dependency on the target repository's test output format---a dependency that CLS avoids by construction, since it never generates execution output.
236	
237	\paragraph{Sequence-length confound ablation.}
238	CLS and CWM use different maximum sequence lengths at repo-level (CLS: 8,192 tokens; CWM: 2,048 tokens), raising the concern that CLS's advantage could be an artifact of additional input context rather than formulation.
239	To control for this, we evaluate the CLS 8B model (seed 42, val-selected checkpoint) at $\text{max\_seq\_length} = 2{,}048$ (matching CWM's configuration).
240	Accuracy drops by only 0.69pp (83.52\% $\to$ 82.83\%), leaving a 24.79pp gap over CWM.
241	This confirms that the classification advantage is driven by the formulation, not the input sequence length.
242	
243	\paragraph{LoRA rank ablation.}
244	To address the concern that LoRA rank$=$16 may systematically disadvantage CWM (which must reconstruct output strings and might benefit from additional adapter capacity), we train a CWM 4B model with rank$=$32 on function-level data.
245	The rank$=$32 model achieves 87.0\% accuracy versus 87.51\% at rank$=$16 ($\Delta = -$0.51pp), well within seed-level variance ($\pm$0.53pp).
246	CWM's capacity to generate execution outputs is not bottlenecked by adapter rank at this scale.
247	
248	\paragraph{Block correlation.}
249	The empirical ICC of 0.191 ($p < 0.0001$) indicates significant block correlation: per-test predictions within the same patch are positively correlated, with a design effect of 3.97.
250	In practical terms, the 114 test-level clusters (problems) in our function-level evaluation yield an effective sample size of approximately $1{,}890 / 3.97 \approx 476$ independent observations.
251	This correlation structure has two implications: (1) it motivates the clustered bootstrap procedure used throughout, and (2) it amplifies the per-test advantage in the oracle framework (\S\ref{ssec:frontier}), since correlated correct predictions within a cluster mean that a single per-test error is more likely to flip the patch-level verdict.
252	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c262053-8133-4103-bc20-6d3efe980178",
  "isSidechain": false,
  "promptId": "d23e62c5-31bd-43a9-9cde-fc27110c6abe",
  "type": "user",
  "uuid": "1444c8f8-ea83-4c11-ba6a-ef5b742ba373",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/experiments.tex",
      "content": "% Experiments draft — generated 2026-05-15, numbers from registry\n% NOTE: All numbers cross-checked against experiment registry.\n% exp_id references provided for key claims.\n\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate the three formulations defined in \\S\\ref{sec:method} across two complexity levels---function-level and repository-level---to test the prediction that classification gains an increasing advantage over generation as code complexity grows.\n\n\\subsection{Experimental Setup}\n\\label{ssec:setup}\n\n\\paragraph{Function-Level Data.}\nWe construct a function-level benchmark from HumanEval~\\citep{chen2021humaneval} and MBPP~\\citep{austin2021mbpp} by applying five categories of systematic mutations---\\texttt{off\\_by\\_one}, \\texttt{operator\\_swap}, \\texttt{variable\\_swap}, \\texttt{return\\_value}, and \\texttt{boundary\\_removal}---to correct solutions, yielding 19,076 (code, test, label) triples.\nWe split by problem identity: 15,290 train / 1,896 validation / 1,890 test, with zero problem overlap between splits.\nThe test set is approximately class-balanced (51.7\\% \\textsc{Pass}, 48.3\\% \\textsc{Fail}).\n\n\\paragraph{Repo-Level Data.}\nWe derive a per-test verification dataset from SWE-bench Verified~\\citep{jimenez2024swebench} by pairing each candidate patch with individual test cases and their ground-truth outcomes.\nThe resulting dataset contains approximately 70K training samples, 9,335 validation samples, and 9,784 test samples.\nThe test set is class-imbalanced (72.96\\% \\textsc{Pass}); we report the majority-class baseline throughout.\nValidation and test splits have zero problem overlap and exhibit a mutation-type composition shift (operator\\_swap: 19.1\\% val $\\to$ 34.3\\% test), which we discuss in \\S\\ref{ssec:analysis}.\n\n\\paragraph{Models and Training.}\nAll models use Qwen3~\\citep{qwen2025qwen3} as the base architecture with LoRA adaptation~\\citep{hu2022lora} (rank$=$16, $\\alpha$$=$32).\nWe train Qwen3-4B and Qwen3-8B variants for CLS, CWM, and TRAJ formulations.\nTraining uses AdamW with learning rate $2 \\times 10^{-4}$ (function-level) or $5 \\times 10^{-5}$ (repo-level), weight decay 0.01, warmup ratio 0.05, batch size 32 (effective), and 3 epochs.\nFunction-level experiments use seeds 42, 123, 456, 789, and 0 (five seeds); 8B scaling experiments use seeds 42, 123, and 456 (three matched pairs).\nSeeds 42/123/456 use bfloat16 precision; seeds 789 and 0 use NF4 quantization due to hardware constraints.\\footnote{NF4 seeds appear only in 4B paired comparisons (\\S\\ref{ssec:equivalence}), where the within-seed paired design controls for quantization effects.}\n\n\\paragraph{Checkpoint Selection.}\nAll reported results use validation-selected checkpoints: we sweep all saved checkpoints on the validation split and select the one with highest accuracy, then evaluate on the held-out test split exactly once.\n\n\\paragraph{Statistical Methods.}\nWe report seed-level means $\\pm$ sample standard deviations.\nFor the CLS--CWM comparison, we use seed-paired bootstrap (10,000 resamples) with one-sided tests.\nFor CLS--TRAJ equivalence, we apply the two one-sided tests (TOST) procedure~\\citep{schuirmann1987tost} with a pre-specified $\\pm$2 percentage-point (pp) equivalence margin.\nFor repo-level results with clustered per-test predictions, we use clustered bootstrap with 114 problem-level clusters and 10,000 resamples.\nWe report the intra-cluster correlation coefficient (ICC) and design effect (DEFF) to characterize block-correlation structure.\n\n\n\\subsection{Function-Level Results}\n\\label{ssec:func_results}\n\n% exp_id: multi-seed-core, cwm-baseline, cwm-seed{123,456,789,0},\n%         cls-seed{789,0}, traj-level-{finetuned,seed123,seed456,seed789,seed0},\n%         llm-judge-8b-zeroshot, llm-judge-32b-zeroshot\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Model} & \\textbf{Accuracy (\\%)} & \\textbf{Seeds} \\\\\n\\midrule\nCLS & Qwen3-4B & 88.43 $\\pm$ 0.78 & 5 \\\\\nCWM & Qwen3-4B & 87.19 $\\pm$ 0.37 & 5 \\\\\nTRAJ & Qwen3-4B & 86.30 $\\pm$ 0.97 & 5 \\\\\n\\midrule\nZS Judge & Qwen3-8B & 64.40 & 1 \\\\\nZS Judge & Qwen3-32B\\textsuperscript{\\textdagger} & 71.69 & 1 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Function-level per-test verification accuracy on HumanEval+MBPP mutants ($n$$=$$1{,}890$). CLS, CWM, and TRAJ are fine-tuned with LoRA; ZS Judge uses zero-shot prompting. \\textsuperscript{\\textdagger}NF4 quantization. All three fine-tuned formulations achieve $>$86\\% accuracy, substantially outperforming zero-shot baselines.}\n\\label{tab:func_results}\n\\end{table}\n\nTable~\\ref{tab:func_results} presents function-level results.\nAll three fine-tuned formulations---CLS, CWM, and TRAJ---achieve strong accuracy in the 86--89\\% range, with CLS leading at 88.43\\%.\n\n\\paragraph{CLS vs.\\ CWM.}\nCLS outperforms CWM by 1.24pp across five matched seeds (bootstrap 95\\% CI: [0.46, 2.04], one-sided $p = 0.025$).\nThe gap is consistent: CLS achieves higher accuracy in all five seed pairs, with per-seed gaps ranging from 0.32pp (seed 42) to 2.33pp (seed 789).\nWhile statistically significant, this gap is modest---both formulations achieve near-equivalent accuracy on function-level code where execution outputs are short and CWM failure modes rarely activate.\n\n\\paragraph{Zero-shot baselines.}\nZero-shot LLM-as-judge performance lags far behind fine-tuned models: Qwen3-8B achieves only 64.40\\% and Qwen3-32B (NF4) reaches 71.69\\%, both exhibiting a systematic bias toward predicting \\textsc{Fail} (fail recall $>$92\\%, pass recall $<$53\\%).\nThe 16.7pp gap between the 32B zero-shot model and the fine-tuned 4B CLS confirms that task-specific fine-tuning is essential for execution simulation, and that the classification formulation's advantage is not an artifact of model scale.\n\n\n\\subsection{Scaling Behavior}\n\\label{ssec:scaling}\n\n% exp_id: model-size-scaling-cls8b, cls8b-seed{123,456},\n%         model-size-scaling-cwm8b, cwm8b-seed{123,456}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{4B} & \\textbf{8B} & \\textbf{$\\Delta$} & \\textbf{Gap} \\\\\n\\midrule\nCLS & 88.43 & 89.39 $\\pm$ 1.09 & +0.96 & \\multirow{2}{*}{} \\\\\nCWM & 87.19 & 86.96 $\\pm$ 0.72 & $-$0.23 & \\\\\n\\midrule\nCLS$-$CWM & 1.24 & 2.43 & & $p = 0.008$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Scaling from 4B to 8B on function-level data. 4B uses five seeds; 8B uses three matched seeds (42, 123, 456). CLS gains +0.96pp from scaling; CWM loses $-$0.23pp. The CLS--CWM gap nearly doubles from 1.24pp to 2.43pp ($p = 0.008$).}\n\\label{tab:scaling}\n\\end{table}\n\nTable~\\ref{tab:scaling} examines scaling behavior by comparing 4B and 8B models with three matched seed pairs per formulation.\nThe key finding is asymmetric: CLS gains +0.96pp from doubling model size (88.43\\% $\\to$ 89.39\\%), while CWM shows no improvement ($-$0.23pp, 87.19\\% $\\to$ 86.96\\%).\nThe CLS--CWM gap consequently widens from 1.24pp at 4B to 2.43pp at 8B ($p = 0.008$, paired $t$-test across three seeds).\n\nThis asymmetry is consistent with a \\emph{generation bottleneck} rather than a capacity limitation.\nIf CWM's lower accuracy were due to insufficient model capacity, scaling should help CWM at least as much as CLS.\nInstead, the generation formulation appears to have a ceiling imposed by the exact-match evaluation criterion: additional capacity helps the model produce better token-level predictions, but exact-match accuracy is dominated by the hardest output tokens (precision-sensitive numbers, formatting characters) where even small errors cause failure.\nClassification sidesteps this bottleneck entirely---the model need only determine whether the output \\emph{would differ} from the expected value, not reconstruct the differing string.\n\n\n\\subsection{Per-Test vs.\\ Trajectory-Level Equivalence}\n\\label{ssec:equivalence}\n\n% exp_id: 5-paired-clustered-bootstrap, block-corr-empirical\n\nPer-test classification decomposes the verification task into $|T|$ binary predictions that are aggregated to a patch verdict by conjunction.\nThis decomposition could either help (richer signal) or hurt (error compounding).\nWe compare CLS (aggregated to variant level) against TRAJ across five matched seed pairs using the clustered bootstrap framework from \\S\\ref{ssec:setup}.\n\nThe pooled CLS--TRAJ gap is $-$0.45pp (95\\% CI: [$-$1.71, +0.84], $p = 0.499$), with per-seed gaps ranging from $-$1.84pp (seed 456) to +1.45pp (seed 123).\nA TOST equivalence test confirms that the two formulations are statistically equivalent within $\\pm$2pp ($p = 0.007$).\nWe justify this margin on the basis of the block-correlation structure: with an empirically estimated ICC of 0.191 and design effect of 3.97 (\\S\\ref{ssec:analysis}), a 2pp variant-level difference corresponds to substantially less than 1pp in effective independent predictions.\n\nThe practical implication is that per-test classification achieves the \\emph{same} patch-level accuracy as trajectory-level scoring while providing strictly more information: for each patch, CLS identifies which specific tests are predicted to fail, enabling diagnostic applications (targeted re-repair, failure triage) that trajectory-level verifiers cannot support.\n\n\n\\subsection{Accuracy-Utility Frontier}\n\\label{ssec:frontier}\n\n% exp_id: oracle-f2p-stratified, p2p-regression-rate\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n$|T_{\\textsc{f2p}}|$ & \\textbf{\\% Instances} & \\textbf{Block Adv.\\ (pp)} & \\textbf{Contrib.\\ (\\%)} \\\\\n\\midrule\n1 & 68.7 & $-$0.09 & --- \\\\\n2 & 19.1 & 31.69 & 55.3 \\\\\n3--5 & 7.1 & 40.74 & 26.3 \\\\\n$\\geq$ 6 & 5.1 & 40.06 & 18.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Oracle accuracy-utility frontier stratified by the number of fail-to-pass tests $|T_{\\textsc{f2p}}|$ in SWE-bench Verified. Block advantage measures the oracle gain from per-test over trajectory-level verification under the empirical ICC. The advantage concentrates in instances with $T \\geq 2$ (31.3\\% of instances, 100\\% of advantage).}\n\\label{tab:frontier}\n\\end{table}\n\nPer-test verification provides value only when per-test predictions carry actionable information.\nTable~\\ref{tab:frontier} stratifies the per-test oracle advantage by the number of fail-to-pass tests ($|T_{\\textsc{f2p}}|$) using the empirical correlation structure (ICC$=$0.191).\n\nWhen $|T_{\\textsc{f2p}}| = 1$ (68.7\\% of SWE-bench Verified instances), per-test and trajectory-level formulations are informationally equivalent: there is only one fail-to-pass test, so knowing \\emph{which} test fails adds nothing beyond knowing \\emph{that} a test fails.\nThe advantage concentrates in multi-test instances: at $|T_{\\textsc{f2p}}| = 2$ (19.1\\% of instances), the block-correlated oracle advantage is 31.69pp, accounting for 55.3\\% of the total advantage.\n\n\\paragraph{Pass-to-pass regression rate.}\nWe also examine whether per-test verification provides value through pass-to-pass (P2P) regression detection.\nEmpirically, the P2P regression rate on SWE-bench Verified is approximately 1\\% (mean; 0\\% median) across incorrect patches: 77\\% of incorrect patches break zero P2P tests.\nAt this rate, per-test verification offers negligible advantage on the P2P dimension---the signal is too sparse.\nWe report this as an honest negative: the per-test formulation's value on SWE-bench Verified derives primarily from fail-to-pass discrimination in multi-test instances, not from regression detection.\nThe practical decision boundary is $|T_{\\textsc{f2p}}| \\geq 2$: below this threshold, trajectory-level scoring suffices.\n\n\n\\subsection{Repo-Level Results}\n\\label{ssec:repo_results}\n\n% exp_id: repo-level-cls-v5, repo-level-cwm-v12, repo-level-cwm-seed123-conda,\n%         cls8b-s42-ckpt1000-test8192-eval, cls8b-seed123-ckpt3000-test8192-eval\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{Seed} & \\textbf{Acc (\\%)} & \\textbf{Unp.\\ (\\%)} & \\textbf{vs Maj.} \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Majority baseline}} \\\\\n--- & --- & --- & 72.96 & --- & 0 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Same-size comparison (primary)}} \\\\\nCLS & 4B & 42 & 83.63 & 1.3 & +10.67 \\\\\nCWM & 4B & 42 & 58.04 & 53.7 & $-$14.92 \\\\\nCWM & 4B & 123 & 59.09 & 67.2 & $-$13.87 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Cross-size comparison (secondary)}} \\\\\nCLS & 8B & 42 & 83.52 & 0.0 & +10.56 \\\\\nCLS & 8B & 123 & 85.60 & 0.0 & +12.64 \\\\\nCWM & 8B & 42 & \\multicolumn{3}{c}{\\emph{in progress}} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Repo-level verification on SWE-bench Verified ($n$$=$$9{,}784$). Unp.\\ = unparseable prediction rate. CLS outperforms CWM by 25.59pp at matched 4B scale. CWM falls below the majority baseline in both seeds, with 54--67\\% of predictions unparseable.}\n\\label{tab:repo_results}\n\\end{table}\n\nTable~\\ref{tab:repo_results} presents the central result: at repository-level complexity, the CLS--CWM gap explodes from the 1--2pp range observed at function level to over 25pp.\n\n\\paragraph{Primary comparison (same-size 4B).}\nAt matched model scale and seed, CLS achieves 83.63\\% accuracy versus CWM at 58.04\\%---a 25.59pp gap.\nThe gap is driven by CWM's catastrophic failure on repo-level code: 53.7--67.2\\% of CWM predictions are unparseable (the model generates execution traces that consume the entire token budget without reaching a verdict).\nCWM accuracy falls \\emph{below} the majority baseline (72.96\\%) by approximately 14pp in both seeds, meaning the CWM verifier provides negative value compared to always predicting the majority class.\nAmong the minority of parseable CWM predictions, accuracy is only 42--43\\%---below random chance---indicating that the model is anti-informative even when it produces interpretable output.\n\n\\paragraph{Secondary comparison (cross-size).}\nTwo 8B CLS seeds confirm the pattern: CLS at 83.52\\% (seed 42) and 85.60\\% (seed 123) versus matched-seed 4B CWM at 58.04\\% and 59.09\\%, yielding gaps of 25.48pp and 26.51pp respectively.\n8B CWM training on repo-level data is in progress; we will include 8B--8B comparisons in the final version.\n\n\\paragraph{Gap amplification.}\nThe CLS--CWM gap follows a clear complexity gradient: 1.24pp at function-level 4B, 2.43pp at function-level 8B, and $\\sim$25pp at repo-level 4B.\nThis 20$\\times$ amplification from function-level to repo-level confirms the complexity-dependent reformulation advantage predicted by the failure-mode analysis in \\S\\ref{ssec:failure_modes}: on simple code with short outputs, the generation formulation copes; on complex code with long traces, it collapses.\n\n\n\\subsection{Analysis}\n\\label{ssec:analysis}\n\n% exp_id: cwm-rank32-ablation-v2, cls8b-s42-ckpt1000-test-seq2048-ablation,\n%         block-corr-empirical\n\n\\paragraph{Error complementarity.}\nCLS and CWM exhibit systematically opposite error patterns on function-level data.\nOf CLS errors, 75.5\\% are false negatives (missed bugs: the model predicts \\textsc{Pass} for a truly failing test), while 83.1\\% of CWM errors are false positives (false alarms: the model predicts \\textsc{Fail} for a truly passing test).\nAn oracle that selects the correct prediction whenever the two models disagree achieves 90.63\\% accuracy---a 2.20pp gain over CLS alone and 3.44pp over CWM.\nThis complementarity suggests that formulation diversity (combining classification and generation verifiers) may be a productive strategy for verification pipelines, even at function-level complexity where the individual formulations achieve similar accuracy.\n\n\\paragraph{CWM error-mode breakdown.}\nA detailed analysis of 500 repo-level CWM predictions reveals three error modes in order of prevalence.\n\\emph{Token-budget exhaustion} (77\\% of unparseable predictions): the model generates realistic pytest execution traces---dots, warnings, file paths---that consume the entire 1,024-token generation budget before reaching any pass/fail verdict.\n\\emph{Keyword ambiguity} (23\\% of unparseable): the generated trace contains both pass-indicating and fail-indicating keywords (e.g., test names containing ``fail,'' deprecation warnings alongside success indicators), preventing reliable keyword extraction.\nAmong the minority of parseable predictions, the model hallucinates failures: 90\\% of parseable errors are \\textsc{Pass}$\\to$\\textsc{Fail} misclassifications (64 of 71 wrong parseable predictions).\nThese failure modes are structural to the generation formulation and cannot be addressed by increasing model capacity---as confirmed by the CWM scaling results in \\S\\ref{ssec:scaling}.\n\n\\paragraph{Per-repository variation.}\nCWM unparseable rates vary dramatically across repositories: from $\\sim$0\\% on scikit-learn (concise test output) to 100\\% on sphinx (verbose build output).\nThis variation reflects a fundamental dependency on the target repository's test output format---a dependency that CLS avoids by construction, since it never generates execution output.\n\n\\paragraph{Sequence-length confound ablation.}\nCLS and CWM use different maximum sequence lengths at repo-level (CLS: 8,192 tokens; CWM: 2,048 tokens), raising the concern that CLS's advantage could be an artifact of additional input context rather than formulation.\nTo control for this, we evaluate the CLS 8B model (seed 42, val-selected checkpoint) at $\\text{max\\_seq\\_length} = 2{,}048$ (matching CWM's configuration).\nAccuracy drops by only 0.69pp (83.52\\% $\\to$ 82.83\\%), leaving a 24.79pp gap over CWM.\nThis confirms that the classification advantage is driven by the formulation, not the input sequence length.\n\n\\paragraph{LoRA rank ablation.}\nTo address the concern that LoRA rank$=$16 may systematically disadvantage CWM (which must reconstruct output strings and might benefit from additional adapter capacity), we train a CWM 4B model with rank$=$32 on function-level data.\nThe rank$=$32 model achieves 87.0\\% accuracy versus 87.51\\% at rank$=$16 ($\\Delta = -$0.51pp), well within seed-level variance ($\\pm$0.53pp).\nCWM's capacity to generate execution outputs is not bottlenecked by adapter rank at this scale.\n\n\\paragraph{Block correlation.}\nThe empirical ICC of 0.191 ($p < 0.0001$) indicates significant block correlation: per-test predictions within the same patch are positively correlated, with a design effect of 3.97.\nIn practical terms, the 114 test-level clusters (problems) in our function-level evaluation yield an effective sample size of approximately $1{,}890 / 3.97 \\approx 476$ independent observations.\nThis correlation structure has two implications: (1) it motivates the clustered bootstrap procedure used throughout, and (2) it amplifies the per-test advantage in the oracle framework (\\S\\ref{ssec:frontier}), since correlated correct predictions within a cluster mean that a single per-test error is more likely to flip the patch-level verdict.\n",
      "numLines": 252,
      "startLine": 1,
      "totalLines": 252
    }
  },
  "sourceToolAssistantUUID": "2c262053-8133-4103-bc20-6d3efe980178",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T15:04:10.816Z_

<details><summary>↩ Tool result · `toolu_016huHvHaSMUFXRLiuQ2kFh1`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate \cls{}, \cwm{}, and trajectory-level scoring (TRAJ) across model sizes and complexity levels.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Function-level dataset.}
10	We construct a function-level benchmark from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} by generating mutated variants (five mutation types: \texttt{wrong\_operator}, \texttt{off\_by\_one}, \texttt{boundary\_error}, \texttt{return\_value}, \texttt{type\_error}), with labels verified by execution (5s timeout). The dataset contains 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	
12	\paragraph{Repo-level dataset.}
13	We construct a repo-level benchmark from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants, extracting per-test instances from repository-scale patches. The dataset contains approximately 70K training samples, with validation ($n{=}9{,}335$) and test ($n{=}9{,}784$) splits having zero problem overlap. The majority baseline (always predict pass) is 72.96\%. Mutation type composition differs between validation and test due to the non-overlapping problem split; this is a consequence of the design (no data leakage), and val-based checkpoint selection is standard practice~\cite{jimenez2024swebench}.
14	
15	\paragraph{Models and training.}
16	We fine-tune Qwen3-4B and Qwen3-8B~\cite{yang2024qwen25} with LoRA~\cite{hu2022lora} (rank 16, lr $2{\times}10^{-4}$ function-level / $5{\times}10^{-5}$ repo-level, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Our \cwm{} baseline is a LoRA fine-tuned variant trained for controlled comparison, not a reproduction of the full-scale 32B Code World Model~\cite{meta2025cwm}. Repo-level models use val-selected checkpoints: we select the checkpoint with highest validation accuracy for test evaluation (D088 protocol).
17	
18	\paragraph{Oracle analysis and statistics.}
19	We use SWE-bench Verified~\cite{chowdhury2024swebenchverified} (500 instances) to derive the accuracy-utility frontier (\S\ref{sec:oracle}). All confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); the per-test vs.\ trajectory-level comparison uses TOST~\cite{schuirmann1987tost} with $\pm$2\pp{} margin. Within-problem correlation is quantified via the intraclass correlation coefficient~\cite{shrout1979icc}.
20	
21	
22	\subsection{Function-Level Results}
23	\label{sec:func_results}
24	
25	Table~\ref{tab:main_results} reports function-level results across formulations.
26	
27	\begin{table}[t]
28	\centering
29	\small
30	\caption{Function-level per-test verification results on HumanEval+MBPP test set (1,890 samples). \cls{}: per-test binary classification; \cwm{}: execution output generation; TRAJ: trajectory-level scoring; ZS: zero-shot LLM-as-judge. Mean $\pm$ std over seeds reported where applicable.}
31	\label{tab:main_results}
32	\resizebox{\columnwidth}{!}{%
33	\setlength{\tabcolsep}{4pt}
34	\begin{tabular}{llcc}
35	\toprule
36	\textbf{Method} & \textbf{Model} & \textbf{Seeds} & \textbf{Accuracy (\%)} \\
37	\midrule
38	\cls{} (fine-tuned) & 4B & 5 & \textbf{88.43 $\pm$ 0.78} \\
39	\cwm{} (fine-tuned) & 4B & 5 & 87.19 $\pm$ 0.37 \\
40	TRAJ (fine-tuned) & 4B & 5 & 86.30 $\pm$ 0.97 \\
41	\midrule
42	ZS LLM-as-judge & 8B & 1 & 64.40 \\
43	ZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\
44	\bottomrule
45	\end{tabular}}
46	\end{table}
47	
48	Fine-tuned \cls{} achieves a mean accuracy of 88.43\% ($\pm$0.78 across seeds 87.83, 89.52, 87.88, 89.00, 87.94), compared to 87.19\% ($\pm$0.37; seeds: 87.51, 87.20, 86.98, 86.67, 87.57) for \cwm{} and 86.30\% ($\pm$0.97; seeds: 85.66, 85.47, 87.40, 87.31, 85.66) for TRAJ. The \cls{}--\cwm{} gap is 1.24\pp{}, which is modest at this complexity level---both formulations operate on short, single-function code with simple return values, where generation is not yet bottlenecked by token budget or string complexity.
49	
50	Zero-shot baselines lag by a wide margin: Qwen3-8B achieves 64.40\% and Qwen3-32B (NF4) achieves 71.69\%, both far below fine-tuned 4B models. The 8B zero-shot model exhibits a strong FAIL bias (fail recall 95.8\%, pass recall 35.1\%), indicating that zero-shot prompting cannot achieve the balanced precision/recall that fine-tuning produces. Even with 8$\times$ more parameters, the 32B zero-shot model trails the fine-tuned 4B \cls{} by 16.74\pp{}, confirming that task-specific fine-tuning, rather than model scale alone, is necessary for reliable per-test verification.
51	
52	
53	\subsection{Scaling Behavior}
54	\label{sec:scaling}
55	
56	Table~\ref{tab:scaling} compares \cls{} and \cwm{} at two model sizes using three matched seeds (42, 123, 456), all trained in full bfloat16 precision to ensure a controlled comparison.
57	
58	\begin{table}[t]
59	\centering
60	\small
61	\caption{Model-size scaling: \cls{} vs.\ \cwm{} accuracy (\%) at 4B and 8B. Three matched seeds in full precision. The \cls{}--\cwm{} gap widens from 1.18\pp{} to 2.43\pp{}.}
62	\label{tab:scaling}
63	\setlength{\tabcolsep}{4pt}
64	\begin{tabular}{llccccc}
65	\toprule
66	\textbf{Method} & \textbf{Size} & \textbf{s42} & \textbf{s123} & \textbf{s456} & \textbf{Mean} & \textbf{Gap} \\
67	\midrule
68	\cls{} & 4B & 87.83 & 89.52 & 87.88 & 88.41 & \multirow{2}{*}{1.18} \\
69	\cwm{} & 4B & 87.51 & 87.20 & 86.98 & 87.23 & \\
70	\midrule
71	\cls{} & 8B & \textbf{90.48} & 89.40 & 88.31 & \textbf{89.40} & \multirow{2}{*}{\textbf{2.43}} \\
72	\cwm{} & 8B & 87.67 & 86.98 & 86.24 & 86.96 & \\
73	\bottomrule
74	\end{tabular}
75	\end{table}
76	
77	At 4B, \cls{} and \cwm{} are separated by 1.18\pp{} on the matched three-seed subset. At 8B, the gap more than doubles to 2.43\pp{}. Clustered bootstrap analysis yields a mean gap of 2.26\pp{} ($p = 0.0066$, 95\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.
78	
79	The asymmetry in scaling efficiency is striking: from 4B to 8B, \cls{} gains +0.99\pp{} (88.41 $\to$ 89.40) while \cwm{} loses $-$0.27\pp{} (87.23 $\to$ 86.96). The additional model capacity benefits classification---where the model needs only to discriminate pass from fail---but provides no measurable improvement for generation, where the model must additionally produce exact output strings. This pattern is consistent with the hypothesis that the string-prediction bottleneck, not model capacity, bounds \cwm{} accuracy. However, the \cwm{} regression ($-$0.27\pp{}) falls within seed noise (3-seed std ${\sim}$0.5\pp{}) and could reflect suboptimal hyperparameter transfer (LoRA rank and learning rate were not re-tuned for 8B) rather than a fundamental bottleneck; disentangling these factors requires larger-scale experiments. We also acknowledge the limited model-level statistical power of three seeds: while the clustered bootstrap provides instance-level confidence (1,890 samples $\times$ 10K resamples), three model instances cannot fully separate seed variance from systematic scaling effects. Figure~\ref{fig:scaling_gap} visualizes the diverging trajectories. Whether this divergence amplifies at repository-level complexity is examined in \S\ref{sec:repo}.
80	
81	
82	\subsection{Per-Test vs.\ Trajectory-Level Equivalence}
83	\label{sec:equivalence}
84	
85	A natural concern is whether per-test predictions, when aggregated to the variant level, match the accuracy of a model trained directly at that granularity. We address this by comparing \cls{} (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds.
86	
87	The pooled gap is $-$0.45\pp{} (95\% CI [$-$1.71, +0.84]), with per-seed gaps ranging from $-$1.84 to +1.45\pp{} (seed 42: $-$0.97; seed 123: +1.45; seed 456: $-$1.84; seed 789: $-$0.78; seed 0: $-$0.29). The TOST equivalence test rejects the null hypothesis of non-equivalence at $p = 0.007$ with a $\pm$2\pp{} margin, confirming that per-test classification and trajectory-level scoring achieve statistically equivalent variant-level accuracy.
88	
89	Critically, however, predictions within the same problem are not independent. The intraclass correlation coefficient is ICC $= 0.191$ ($p < 0.0001$), yielding a design effect DEFF $= 3.97$. This means that naive i.i.d.\ confidence intervals would be approximately $2\times$ too narrow. All statistical tests in this paper use clustered bootstrap to account for this within-problem correlation.
90	
91	The practical implication is clear: per-test classification provides per-test diagnostic information---which specific tests fail and why---at no cost to variant-level accuracy. A trajectory-level model gives only a binary patch verdict, discarding the per-test signal that downstream repair systems could exploit for targeted re-repair.
92	
93	
94	\subsection{Accuracy-Utility Frontier}
95	\label{sec:oracle-results}
96	
97	Where does per-test granularity actually help? We formalize this via an oracle analysis on SWE-bench Verified, stratifying instances by the number of F2P tests $T$ and comparing per-test vs.\ trajectory-level oracle resolve rates under both i.i.d.\ and block-correlated error models (using the empirical ICC $= 0.191$).
98	
99	\begin{table}[t]
100	\centering
101	\small
102	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses empirical ICC $= 0.191$. P2P regression rate: 1.04\% mean, 0\% median.}
103	\label{tab:oracle}
104	\resizebox{\columnwidth}{!}{%
105	\setlength{\tabcolsep}{3pt}
106	\begin{tabular}{lcccc}
107	\toprule
108	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
109	\midrule
110	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
111	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
112	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
113	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
114	\midrule
115	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
116	\bottomrule
117	\end{tabular}}
118	\end{table}
119	
120	Table~\ref{tab:oracle} reveals a sharp concentration of per-test advantage. When $T = 1$---the dominant case at 68.7\% of SWE-bench instances---per-test and trajectory-level are informationally equivalent (block advantage $-$0.09\pp{}), because a single F2P test provides no more signal than a binary patch verdict. The advantage materializes at $T = 2$ (19.1\% of instances), where block-correlated advantage reaches 31.69\pp{}, contributing 55.3\% of the total advantage. Instances with $T \geq 3$ exhibit block advantages exceeding 40\pp{} but constitute only 12.2\% of instances. The overall block-correlated advantage is 10.93\pp{}, driven almost entirely by the $T \geq 2$ minority. Figure~\ref{fig:oracle_stratified} visualizes this distribution.
121	
122	Block correlation amplifies the advantage relative to the i.i.d.\ model: at $T = 2$, the block advantage (31.69\pp{}) is 1.7$\times$ the i.i.d.\ advantage (18.49\pp{}). This occurs because correlated errors make the per-test classifier more likely to get all tests correct or all wrong for a given problem, increasing the information value of each additional test.
123	
124	\paragraph{P2P regression signal.}
125	The P2P regression rate in SWE-bench Verified is low: 1.04\% mean and 0\% median---77\% of incorrect patches break zero P2P tests. This means per-test granularity on the P2P dimension currently provides minimal signal. The practical value of per-test verification concentrates in F2P discrimination, particularly for instances with multiple F2P tests.
126	
127	
128	\subsection{Repo-Level Results}
129	\label{sec:repo}
130	
131	Table~\ref{tab:repo_level} compares \cls{} and \cwm{} on SWE-bench Verified per-test classification at repository-level complexity. All checkpoints are selected by validation accuracy (D088 protocol); the test set ($n{=}9{,}784$) has zero problem overlap with validation.
132	
133	\begin{table}[t]
134	\centering
135	\small
136	\caption{Repo-level per-test verification on SWE-bench Verified test set ($n{=}9{,}784$, val-selected checkpoints). Same-size 4B comparison is primary; \cls{} 8B included for scaling context; \cwm{} 8B in progress.}
137	\label{tab:repo_level}
138	\resizebox{\columnwidth}{!}{%
139	\setlength{\tabcolsep}{3pt}
140	\begin{tabular}{llccccc}
141	\toprule
142	\textbf{Method} & \textbf{Size} & \textbf{Seed} & \textbf{Acc (\%)} & \textbf{Macro \fone{}} & \textbf{Unparse (\%)} & \textbf{vs Maj.\ (\pp{})} \\
143	\midrule
144	\cls{} & 4B & 42 & \textbf{83.63} & 75.63 & 0.0 & +10.67 \\
145	\cwm{} & 4B & 42 & 58.04 & 51.67 & 53.7 & $-$14.92 \\
146	\cwm{} & 4B & 123 & 59.09 & 43.43 & 67.2 & $-$13.87 \\
147	\midrule
148	\cls{} & 8B & 42 & 83.52 & 77.50 & 0.0 & +10.56 \\
149	\cls{} & 8B & 123 & 85.60 & 78.38 & 0.0 & +12.64 \\
150	\cwm{} & 8B & --- & --- & --- & --- & --- \\
151	\midrule
152	Majority & --- & --- & 72.96 & --- & --- & --- \\
153	\bottomrule
154	\end{tabular}}
155	\end{table}
156	
157	The same-size 4B comparison reveals a 25.59\pp{} gap: \cls{} achieves 83.63\% accuracy (macro \fone{} 75.63) versus \cwm{} at 58.04\% (macro \fone{} 51.67) on seed 42. \cwm{} falls 14.92\pp{} below the majority baseline (72.96\%), indicating negative utility---a system that always predicts pass outperforms \cwm{}. A second \cwm{} seed (123) yields 59.09\% with a higher unparseable rate (67.2\% vs.\ 53.7\%), confirming the failure is not seed-specific.
158	
159	The primary driver is output format compliance collapse. \cwm{} produces unparseable outputs for 53.7\% (seed 42) and 67.2\% (seed 123) of test instances, while \cls{} produces zero unparseable outputs across all configurations. The generation budget (1,024 tokens) is sufficient for the outputs required---this is not a token-budget limitation but a failure of the model to produce structured execution predictions when faced with repository-level code complexity. Among parseable \cwm{} outputs, accuracy is 42--43\%---below both the majority baseline (72.96\%) and chance level (50\%)---indicating that even well-formed \cwm{} predictions are anti-informative at this complexity level. \cls{}, producing a single binary token per test, is immune to format compliance failures by construction. Figure~\ref{fig:scaling_gap} visualizes the gap amplification from function level (1.24\pp{}) to repo level (25.59\pp{}).
160	
161	For scaling context, we include \cls{} 8B results (cross-size comparison, not directly comparable to the same-size gap above). \cls{} 8B achieves 83.52\% (seed 42) and 85.60\% (seed 123), yielding cross-size gaps of 25.48\pp{} and 26.51\pp{} against \cwm{} 4B at the corresponding seeds. Within \cls{}, the 4B$\to$8B transition at repo level shows 83.63\% $\to$ 83.52\% (seed 42), a difference within noise, suggesting that classification may be approaching a capacity ceiling at repo-level complexity or that checkpoint selection variance dominates at this scale. \cwm{} 8B training is in progress; if \cwm{} 8B performs similarly to 4B, this would confirm a generation bottleneck rather than a capacity limitation.
162	
163	\paragraph{Sequence length and formulation cost.} Both \cls{} and \cwm{} are trained with identical \texttt{max\_seq\_length}$=$2,048, so training-time input context is fully controlled. The asymmetry arises at inference: \cwm{} reserves \texttt{max\_new\_tokens}$=$1,024 for output generation, leaving an effective input window of ${\sim}$1,024 tokens; \cls{} produces a single token and can allocate nearly all context to input (\texttt{max\_seq\_length}$=$5,120 at 4B, 8,192 at 8B during evaluation). This eval-time difference primarily reflects structural properties of each formulation: generation \emph{must} reserve context for output tokens, while classification need not. A matched-context ablation confirms this: \cls{} 8B evaluated at \texttt{max\_seq\_length}$=$2,048 achieves 82.83\%, a reduction of only 0.69\pp{} from the 8,192-token evaluation (83.52\%). The matched-context gap (\cls{}@2,048 vs.\ \cwm{}@2,048) is 24.79\pp{}, accounting for 97\% of the full 25.59\pp{} gap---input context disparity explains at most 3\% of the observed difference. Moreover, input context cannot explain the qualitative failures. Format compliance collapse---53.7--67.2\% of \cwm{} outputs are unparseable despite sufficient generation budget---reflects the model's inability to produce structured predictions, not input truncation. Among parseable outputs where the model does produce well-formed predictions, accuracy is 42--43\%, below chance level (50\%): if input truncation were the sole issue, parseable outputs should at minimum exceed chance.
164	
165	\paragraph{Limitations.} The same-size 4B comparison uses a single seed; \cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\% test accuracy (+2.4\pp{} above majority baseline), indicating that val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The validation and test sets have zero problem overlap but differ in mutation type composition, introducing potential distribution shift. All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences.
166	
167	
168	\subsection{Analysis}
169	\label{sec:analysis}
170	
171	\paragraph{(a) Error complementarity.}
172	\cls{} and \cwm{} make errors in opposite directions at function level. Among \cls{} errors (seed 42), 75.5\% are false negatives (FAIL $\to$ PASS), meaning the classifier tends to over-predict passing. Among \cwm{} errors, 83.1\% are false positives (PASS $\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination that takes the correct answer whenever either model is right achieves 90.63\% accuracy, a 3.12\pp{} improvement over \cls{} alone (87.51\%). This complementarity suggests that ensemble approaches combining classification and generation signals could yield further gains.
173	
174	\paragraph{(b) CWM error mode breakdown.}
175	At repo level, \cwm{} output format compliance collapses. Of 9,784 test instances, 5,255 (53.7\%, seed 42) and 6,574 (67.2\%, seed 123) produce unparseable outputs. Among unparseable outputs, 76.9\% contain no execution keywords whatsoever, while 22.9\% contain ambiguous co-occurring keywords for both pass and fail. Among parseable outputs, \cwm{} achieves only 42.88\% accuracy (seed 42)---below the 50\% random baseline, indicating that even when the model produces well-formed outputs, its predictions are anti-informative. Format compliance varies across repositories: scikit-learn instances yield near-zero unparseable rates, while sphinx instances are 100\% unparseable. This per-repo variation suggests that certain code contexts---likely those with complex execution traces or domain-specific output patterns---prevent the model from generating structured responses.
176	
177	\paragraph{(c) Relaxed matching does not rescue \cwm{}.}
178	A natural concern is that strict parsing penalizes \cwm{} unfairly---perhaps many unparseable outputs contain correct predictions in a non-standard format. We test this with relaxed matching that tolerates format deviations across five levels (L0--L4). Counter-intuitively, relaxed matching \emph{decreases} \cwm{} accuracy: from 58.04\% to 56.98\% (seed 42, L4) and from 59.09\% to 55.91\% (seed 123, L4). The mechanism is straightforward: unparseable predictions default to the majority class (pass, 72.96\% base rate), which is more accurate than the model's own parseable predictions (42--53\% accuracy). Recovering these predictions from the majority-class fallback into the model's actual outputs \emph{hurts} performance. The \cls{}--\cwm{} gap widens from 26\pp{} (L0) to 28\pp{} (L4), ruling out the hypothesis that parsing strictness inflates the observed gap. This confirms that \cwm{}'s failure at repository-level complexity is not an artifact of format compliance evaluation but reflects the generation formulation itself.
179	
180	\paragraph{(d) Variance compression.}
181	\cwm{}'s 5-seed standard deviation (0.37\pp{}) is lower than \cls{} (0.78\pp{}) and TRAJ (0.97\pp{}) at function level. This is consistent with the bottleneck hypothesis: if \cwm{} performance is capped by output-format constraints, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.
182	
183	\paragraph{(e) Per-test precision and recall.}
184	At the per-test level (seed 42), \cls{} achieves fail \fone{} 87.86\% (precision 82.75\%, recall 93.64\%) and pass \fone{} 87.15\%. Of 114 problems, 48 (42.1\%) are perfectly predicted. Performance varies by mutation type: \texttt{return\_value} is easiest (97.3\%) while \texttt{off\_by\_one} is hardest (82.6\%). Multi-F2P instances with 6--10 tests reach 96.3\% accuracy, corroborating the oracle finding that per-test granularity is most valuable with multiple F2P tests.
185	
186	\paragraph{(f) Majority voting.}
187	Majority voting ($K{=}3$) decreases accuracy from 87.51\% to 86.83\% ($-$0.68\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.
188	
189	\paragraph{(g) Block correlation.}
190	Prediction errors within the same problem are correlated: ICC $= 0.191$ ($p < 0.0001$), DEFF $= 3.97$, with 2.81$\times$ more all-correct problems than expected under i.i.d.\ errors. All statistical tests use clustered bootstrap to account for this, and the block-correlated oracle model (\S\ref{sec:oracle-results}) is the more relevant estimate for deployment.
191	
192	\paragraph{(h) LoRA rank sensitivity.}
193	All \cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \cwm{}, we train a rank-32 variant (seed 42), doubling the number of adapter parameters. The rank-32 model achieves 87.0\% accuracy (fail \fone{} 87.1\%, pass \fone{} 86.9\%), compared with 87.51\% for rank-16 under the same seed---a difference of $-$0.51\pp{}, within the 2-seed variance of the rank-16 configuration (0.53\pp{} between seeds 42 and 456). This is consistent with \cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "daadff89-45ad-44b2-acac-f891d5c97ff0",
  "isSidechain": false,
  "promptId": "d23e62c5-31bd-43a9-9cde-fc27110c6abe",
  "type": "user",
  "uuid": "19a19ab8-371e-416d-8f6f-254f9849d0dc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate \\cls{}, \\cwm{}, and trajectory-level scoring (TRAJ) across model sizes and complexity levels.\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Function-level dataset.}\nWe construct a function-level benchmark from HumanEval~\\cite{chen2021humaneval} and MBPP~\\cite{austin2021mbpp} by generating mutated variants (five mutation types: \\texttt{wrong\\_operator}, \\texttt{off\\_by\\_one}, \\texttt{boundary\\_error}, \\texttt{return\\_value}, \\texttt{type\\_error}), with labels verified by execution (5s timeout). The dataset contains 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48, majority baseline 51.75\\%).\n\n\\paragraph{Repo-level dataset.}\nWe construct a repo-level benchmark from SWE-bench Verified~\\cite{chowdhury2024swebenchverified} mutants, extracting per-test instances from repository-scale patches. The dataset contains approximately 70K training samples, with validation ($n{=}9{,}335$) and test ($n{=}9{,}784$) splits having zero problem overlap. The majority baseline (always predict pass) is 72.96\\%. Mutation type composition differs between validation and test due to the non-overlapping problem split; this is a consequence of the design (no data leakage), and val-based checkpoint selection is standard practice~\\cite{jimenez2024swebench}.\n\n\\paragraph{Models and training.}\nWe fine-tune Qwen3-4B and Qwen3-8B~\\cite{yang2024qwen25} with LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-4}$ function-level / $5{\\times}10^{-5}$ repo-level, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Our \\cwm{} baseline is a LoRA fine-tuned variant trained for controlled comparison, not a reproduction of the full-scale 32B Code World Model~\\cite{meta2025cwm}. Repo-level models use val-selected checkpoints: we select the checkpoint with highest validation accuracy for test evaluation (D088 protocol).\n\n\\paragraph{Oracle analysis and statistics.}\nWe use SWE-bench Verified~\\cite{chowdhury2024swebenchverified} (500 instances) to derive the accuracy-utility frontier (\\S\\ref{sec:oracle}). All confidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); the per-test vs.\\ trajectory-level comparison uses TOST~\\cite{schuirmann1987tost} with $\\pm$2\\pp{} margin. Within-problem correlation is quantified via the intraclass correlation coefficient~\\cite{shrout1979icc}.\n\n\n\\subsection{Function-Level Results}\n\\label{sec:func_results}\n\nTable~\\ref{tab:main_results} reports function-level results across formulations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Function-level per-test verification results on HumanEval+MBPP test set (1,890 samples). \\cls{}: per-test binary classification; \\cwm{}: execution output generation; TRAJ: trajectory-level scoring; ZS: zero-shot LLM-as-judge. Mean $\\pm$ std over seeds reported where applicable.}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Model} & \\textbf{Seeds} & \\textbf{Accuracy (\\%)} \\\\\n\\midrule\n\\cls{} (fine-tuned) & 4B & 5 & \\textbf{88.43 $\\pm$ 0.78} \\\\\n\\cwm{} (fine-tuned) & 4B & 5 & 87.19 $\\pm$ 0.37 \\\\\nTRAJ (fine-tuned) & 4B & 5 & 86.30 $\\pm$ 0.97 \\\\\n\\midrule\nZS LLM-as-judge & 8B & 1 & 64.40 \\\\\nZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFine-tuned \\cls{} achieves a mean accuracy of 88.43\\% ($\\pm$0.78 across seeds 87.83, 89.52, 87.88, 89.00, 87.94), compared to 87.19\\% ($\\pm$0.37; seeds: 87.51, 87.20, 86.98, 86.67, 87.57) for \\cwm{} and 86.30\\% ($\\pm$0.97; seeds: 85.66, 85.47, 87.40, 87.31, 85.66) for TRAJ. The \\cls{}--\\cwm{} gap is 1.24\\pp{}, which is modest at this complexity level---both formulations operate on short, single-function code with simple return values, where generation is not yet bottlenecked by token budget or string complexity.\n\nZero-shot baselines lag by a wide margin: Qwen3-8B achieves 64.40\\% and Qwen3-32B (NF4) achieves 71.69\\%, both far below fine-tuned 4B models. The 8B zero-shot model exhibits a strong FAIL bias (fail recall 95.8\\%, pass recall 35.1\\%), indicating that zero-shot prompting cannot achieve the balanced precision/recall that fine-tuning produces. Even with 8$\\times$ more parameters, the 32B zero-shot model trails the fine-tuned 4B \\cls{} by 16.74\\pp{}, confirming that task-specific fine-tuning, rather than model scale alone, is necessary for reliable per-test verification.\n\n\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nTable~\\ref{tab:scaling} compares \\cls{} and \\cwm{} at two model sizes using three matched seeds (42, 123, 456), all trained in full bfloat16 precision to ensure a controlled comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: \\cls{} vs.\\ \\cwm{} accuracy (\\%) at 4B and 8B. Three matched seeds in full precision. The \\cls{}--\\cwm{} gap widens from 1.18\\pp{} to 2.43\\pp{}.}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{s456} & \\textbf{Mean} & \\textbf{Gap} \\\\\n\\midrule\n\\cls{} & 4B & 87.83 & 89.52 & 87.88 & 88.41 & \\multirow{2}{*}{1.18} \\\\\n\\cwm{} & 4B & 87.51 & 87.20 & 86.98 & 87.23 & \\\\\n\\midrule\n\\cls{} & 8B & \\textbf{90.48} & 89.40 & 88.31 & \\textbf{89.40} & \\multirow{2}{*}{\\textbf{2.43}} \\\\\n\\cwm{} & 8B & 87.67 & 86.98 & 86.24 & 86.96 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 4B, \\cls{} and \\cwm{} are separated by 1.18\\pp{} on the matched three-seed subset. At 8B, the gap more than doubles to 2.43\\pp{}. Clustered bootstrap analysis yields a mean gap of 2.26\\pp{} ($p = 0.0066$, 95\\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.\n\nThe asymmetry in scaling efficiency is striking: from 4B to 8B, \\cls{} gains +0.99\\pp{} (88.41 $\\to$ 89.40) while \\cwm{} loses $-$0.27\\pp{} (87.23 $\\to$ 86.96). The additional model capacity benefits classification---where the model needs only to discriminate pass from fail---but provides no measurable improvement for generation, where the model must additionally produce exact output strings. This pattern is consistent with the hypothesis that the string-prediction bottleneck, not model capacity, bounds \\cwm{} accuracy. However, the \\cwm{} regression ($-$0.27\\pp{}) falls within seed noise (3-seed std ${\\sim}$0.5\\pp{}) and could reflect suboptimal hyperparameter transfer (LoRA rank and learning rate were not re-tuned for 8B) rather than a fundamental bottleneck; disentangling these factors requires larger-scale experiments. We also acknowledge the limited model-level statistical power of three seeds: while the clustered bootstrap provides instance-level confidence (1,890 samples $\\times$ 10K resamples), three model instances cannot fully separate seed variance from systematic scaling effects. Figure~\\ref{fig:scaling_gap} visualizes the diverging trajectories. Whether this divergence amplifies at repository-level complexity is examined in \\S\\ref{sec:repo}.\n\n\n\\subsection{Per-Test vs.\\ Trajectory-Level Equivalence}\n\\label{sec:equivalence}\n\nA natural concern is whether per-test predictions, when aggregated to the variant level, match the accuracy of a model trained directly at that granularity. We address this by comparing \\cls{} (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds.\n\nThe pooled gap is $-$0.45\\pp{} (95\\% CI [$-$1.71, +0.84]), with per-seed gaps ranging from $-$1.84 to +1.45\\pp{} (seed 42: $-$0.97; seed 123: +1.45; seed 456: $-$1.84; seed 789: $-$0.78; seed 0: $-$0.29). The TOST equivalence test rejects the null hypothesis of non-equivalence at $p = 0.007$ with a $\\pm$2\\pp{} margin, confirming that per-test classification and trajectory-level scoring achieve statistically equivalent variant-level accuracy.\n\nCritically, however, predictions within the same problem are not independent. The intraclass correlation coefficient is ICC $= 0.191$ ($p < 0.0001$), yielding a design effect DEFF $= 3.97$. This means that naive i.i.d.\\ confidence intervals would be approximately $2\\times$ too narrow. All statistical tests in this paper use clustered bootstrap to account for this within-problem correlation.\n\nThe practical implication is clear: per-test classification provides per-test diagnostic information---which specific tests fail and why---at no cost to variant-level accuracy. A trajectory-level model gives only a binary patch verdict, discarding the per-test signal that downstream repair systems could exploit for targeted re-repair.\n\n\n\\subsection{Accuracy-Utility Frontier}\n\\label{sec:oracle-results}\n\nWhere does per-test granularity actually help? We formalize this via an oracle analysis on SWE-bench Verified, stratifying instances by the number of F2P tests $T$ and comparing per-test vs.\\ trajectory-level oracle resolve rates under both i.i.d.\\ and block-correlated error models (using the empirical ICC $= 0.191$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses empirical ICC $= 0.191$. P2P regression rate: 1.04\\% mean, 0\\% median.}\n\\label{tab:oracle}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$T$} & \\textbf{Inst.\\%} & \\textbf{i.i.d.\\ (\\pp{})} & \\textbf{Block (\\pp{})} & \\textbf{Contrib.\\%} \\\\\n\\midrule\n$1$ & 68.7 & $-$0.04 & $-$0.09 & $\\approx$0 \\\\\n$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\\\\n$3$--$5$ & 7.1 & 25.00 & 40.74 & $\\approx$26 \\\\\n$\\geq 6$ & 5.1 & 30.00 & 40.06 & $\\approx$19 \\\\\n\\midrule\n\\textbf{All} & 100.0 & --- & \\textbf{10.93} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:oracle} reveals a sharp concentration of per-test advantage. When $T = 1$---the dominant case at 68.7\\% of SWE-bench instances---per-test and trajectory-level are informationally equivalent (block advantage $-$0.09\\pp{}), because a single F2P test provides no more signal than a binary patch verdict. The advantage materializes at $T = 2$ (19.1\\% of instances), where block-correlated advantage reaches 31.69\\pp{}, contributing 55.3\\% of the total advantage. Instances with $T \\geq 3$ exhibit block advantages exceeding 40\\pp{} but constitute only 12.2\\% of instances. The overall block-correlated advantage is 10.93\\pp{}, driven almost entirely by the $T \\geq 2$ minority. Figure~\\ref{fig:oracle_stratified} visualizes this distribution.\n\nBlock correlation amplifies the advantage relative to the i.i.d.\\ model: at $T = 2$, the block advantage (31.69\\pp{}) is 1.7$\\times$ the i.i.d.\\ advantage (18.49\\pp{}). This occurs because correlated errors make the per-test classifier more likely to get all tests correct or all wrong for a given problem, increasing the information value of each additional test.\n\n\\paragraph{P2P regression signal.}\nThe P2P regression rate in SWE-bench Verified is low: 1.04\\% mean and 0\\% median---77\\% of incorrect patches break zero P2P tests. This means per-test granularity on the P2P dimension currently provides minimal signal. The practical value of per-test verification concentrates in F2P discrimination, particularly for instances with multiple F2P tests.\n\n\n\\subsection{Repo-Level Results}\n\\label{sec:repo}\n\nTable~\\ref{tab:repo_level} compares \\cls{} and \\cwm{} on SWE-bench Verified per-test classification at repository-level complexity. All checkpoints are selected by validation accuracy (D088 protocol); the test set ($n{=}9{,}784$) has zero problem overlap with validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level per-test verification on SWE-bench Verified test set ($n{=}9{,}784$, val-selected checkpoints). Same-size 4B comparison is primary; \\cls{} 8B included for scaling context; \\cwm{} 8B in progress.}\n\\label{tab:repo_level}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{Seed} & \\textbf{Acc (\\%)} & \\textbf{Macro \\fone{}} & \\textbf{Unparse (\\%)} & \\textbf{vs Maj.\\ (\\pp{})} \\\\\n\\midrule\n\\cls{} & 4B & 42 & \\textbf{83.63} & 75.63 & 0.0 & +10.67 \\\\\n\\cwm{} & 4B & 42 & 58.04 & 51.67 & 53.7 & $-$14.92 \\\\\n\\cwm{} & 4B & 123 & 59.09 & 43.43 & 67.2 & $-$13.87 \\\\\n\\midrule\n\\cls{} & 8B & 42 & 83.52 & 77.50 & 0.0 & +10.56 \\\\\n\\cls{} & 8B & 123 & 85.60 & 78.38 & 0.0 & +12.64 \\\\\n\\cwm{} & 8B & --- & --- & --- & --- & --- \\\\\n\\midrule\nMajority & --- & --- & 72.96 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe same-size 4B comparison reveals a 25.59\\pp{} gap: \\cls{} achieves 83.63\\% accuracy (macro \\fone{} 75.63) versus \\cwm{} at 58.04\\% (macro \\fone{} 51.67) on seed 42. \\cwm{} falls 14.92\\pp{} below the majority baseline (72.96\\%), indicating negative utility---a system that always predicts pass outperforms \\cwm{}. A second \\cwm{} seed (123) yields 59.09\\% with a higher unparseable rate (67.2\\% vs.\\ 53.7\\%), confirming the failure is not seed-specific.\n\nThe primary driver is output format compliance collapse. \\cwm{} produces unparseable outputs for 53.7\\% (seed 42) and 67.2\\% (seed 123) of test instances, while \\cls{} produces zero unparseable outputs across all configurations. The generation budget (1,024 tokens) is sufficient for the outputs required---this is not a token-budget limitation but a failure of the model to produce structured execution predictions when faced with repository-level code complexity. Among parseable \\cwm{} outputs, accuracy is 42--43\\%---below both the majority baseline (72.96\\%) and chance level (50\\%)---indicating that even well-formed \\cwm{} predictions are anti-informative at this complexity level. \\cls{}, producing a single binary token per test, is immune to format compliance failures by construction. Figure~\\ref{fig:scaling_gap} visualizes the gap amplification from function level (1.24\\pp{}) to repo level (25.59\\pp{}).\n\nFor scaling context, we include \\cls{} 8B results (cross-size comparison, not directly comparable to the same-size gap above). \\cls{} 8B achieves 83.52\\% (seed 42) and 85.60\\% (seed 123), yielding cross-size gaps of 25.48\\pp{} and 26.51\\pp{} against \\cwm{} 4B at the corresponding seeds. Within \\cls{}, the 4B$\\to$8B transition at repo level shows 83.63\\% $\\to$ 83.52\\% (seed 42), a difference within noise, suggesting that classification may be approaching a capacity ceiling at repo-level complexity or that checkpoint selection variance dominates at this scale. \\cwm{} 8B training is in progress; if \\cwm{} 8B performs similarly to 4B, this would confirm a generation bottleneck rather than a capacity limitation.\n\n\\paragraph{Sequence length and formulation cost.} Both \\cls{} and \\cwm{} are trained with identical \\texttt{max\\_seq\\_length}$=$2,048, so training-time input context is fully controlled. The asymmetry arises at inference: \\cwm{} reserves \\texttt{max\\_new\\_tokens}$=$1,024 for output generation, leaving an effective input window of ${\\sim}$1,024 tokens; \\cls{} produces a single token and can allocate nearly all context to input (\\texttt{max\\_seq\\_length}$=$5,120 at 4B, 8,192 at 8B during evaluation). This eval-time difference primarily reflects structural properties of each formulation: generation \\emph{must} reserve context for output tokens, while classification need not. A matched-context ablation confirms this: \\cls{} 8B evaluated at \\texttt{max\\_seq\\_length}$=$2,048 achieves 82.83\\%, a reduction of only 0.69\\pp{} from the 8,192-token evaluation (83.52\\%). The matched-context gap (\\cls{}@2,048 vs.\\ \\cwm{}@2,048) is 24.79\\pp{}, accounting for 97\\% of the full 25.59\\pp{} gap---input context disparity explains at most 3\\% of the observed difference. Moreover, input context cannot explain the qualitative failures. Format compliance collapse---53.7--67.2\\% of \\cwm{} outputs are unparseable despite sufficient generation budget---reflects the model's inability to produce structured predictions, not input truncation. Among parseable outputs where the model does produce well-formed predictions, accuracy is 42--43\\%, below chance level (50\\%): if input truncation were the sole issue, parseable outputs should at minimum exceed chance.\n\n\\paragraph{Limitations.} The same-size 4B comparison uses a single seed; \\cls{} 4B seed 123 (val-best ckpt-800) achieves only 75.33\\% test accuracy (+2.4\\pp{} above majority baseline), indicating that val-best selection at an early checkpoint (step 800) amplifies the val-test distribution shift observed across all configurations. The validation and test sets have zero problem overlap but differ in mutation type composition, introducing potential distribution shift. All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences.\n\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{(a) Error complementarity.}\n\\cls{} and \\cwm{} make errors in opposite directions at function level. Among \\cls{} errors (seed 42), 75.5\\% are false negatives (FAIL $\\to$ PASS), meaning the classifier tends to over-predict passing. Among \\cwm{} errors, 83.1\\% are false positives (PASS $\\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination that takes the correct answer whenever either model is right achieves 90.63\\% accuracy, a 3.12\\pp{} improvement over \\cls{} alone (87.51\\%). This complementarity suggests that ensemble approaches combining classification and generation signals could yield further gains.\n\n\\paragraph{(b) CWM error mode breakdown.}\nAt repo level, \\cwm{} output format compliance collapses. Of 9,784 test instances, 5,255 (53.7\\%, seed 42) and 6,574 (67.2\\%, seed 123) produce unparseable outputs. Among unparseable outputs, 76.9\\% contain no execution keywords whatsoever, while 22.9\\% contain ambiguous co-occurring keywords for both pass and fail. Among parseable outputs, \\cwm{} achieves only 42.88\\% accuracy (seed 42)---below the 50\\% random baseline, indicating that even when the model produces well-formed outputs, its predictions are anti-informative. Format compliance varies across repositories: scikit-learn instances yield near-zero unparseable rates, while sphinx instances are 100\\% unparseable. This per-repo variation suggests that certain code contexts---likely those with complex execution traces or domain-specific output patterns---prevent the model from generating structured responses.\n\n\\paragraph{(c) Relaxed matching does not rescue \\cwm{}.}\nA natural concern is that strict parsing penalizes \\cwm{} unfairly---perhaps many unparseable outputs contain correct predictions in a non-standard format. We test this with relaxed matching that tolerates format deviations across five levels (L0--L4). Counter-intuitively, relaxed matching \\emph{decreases} \\cwm{} accuracy: from 58.04\\% to 56.98\\% (seed 42, L4) and from 59.09\\% to 55.91\\% (seed 123, L4). The mechanism is straightforward: unparseable predictions default to the majority class (pass, 72.96\\% base rate), which is more accurate than the model's own parseable predictions (42--53\\% accuracy). Recovering these predictions from the majority-class fallback into the model's actual outputs \\emph{hurts} performance. The \\cls{}--\\cwm{} gap widens from 26\\pp{} (L0) to 28\\pp{} (L4), ruling out the hypothesis that parsing strictness inflates the observed gap. This confirms that \\cwm{}'s failure at repository-level complexity is not an artifact of format compliance evaluation but reflects the generation formulation itself.\n\n\\paragraph{(d) Variance compression.}\n\\cwm{}'s 5-seed standard deviation (0.37\\pp{}) is lower than \\cls{} (0.78\\pp{}) and TRAJ (0.97\\pp{}) at function level. This is consistent with the bottleneck hypothesis: if \\cwm{} performance is capped by output-format constraints, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.\n\n\\paragraph{(e) Per-test precision and recall.}\nAt the per-test level (seed 42), \\cls{} achieves fail \\fone{} 87.86\\% (precision 82.75\\%, recall 93.64\\%) and pass \\fone{} 87.15\\%. Of 114 problems, 48 (42.1\\%) are perfectly predicted. Performance varies by mutation type: \\texttt{return\\_value} is easiest (97.3\\%) while \\texttt{off\\_by\\_one} is hardest (82.6\\%). Multi-F2P instances with 6--10 tests reach 96.3\\% accuracy, corroborating the oracle finding that per-test granularity is most valuable with multiple F2P tests.\n\n\\paragraph{(f) Majority voting.}\nMajority voting ($K{=}3$) decreases accuracy from 87.51\\% to 86.83\\% ($-$0.68\\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.\n\n\\paragraph{(g) Block correlation.}\nPrediction errors within the same problem are correlated: ICC $= 0.191$ ($p < 0.0001$), DEFF $= 3.97$, with 2.81$\\times$ more all-correct problems than expected under i.i.d.\\ errors. All statistical tests use clustered bootstrap to account for this, and the block-correlated oracle model (\\S\\ref{sec:oracle-results}) is the more relevant estimate for deployment.\n\n\\paragraph{(h) LoRA rank sensitivity.}\nAll \\cwm{} experiments use LoRA rank $r{=}16$. To test whether this capacity constraint handicaps \\cwm{}, we train a rank-32 variant (seed 42), doubling the number of adapter parameters. The rank-32 model achieves 87.0\\% accuracy (fail \\fone{} 87.1\\%, pass \\fone{} 86.9\\%), compared with 87.51\\% for rank-16 under the same seed---a difference of $-$0.51\\pp{}, within the 2-seed variance of the rank-16 configuration (0.53\\pp{} between seeds 42 and 456). This is consistent with \\cwm{}'s function-level performance being bounded by output-format constraints rather than adapter capacity.",
      "numLines": 193,
      "startLine": 1,
      "totalLines": 193
    }
  },
  "sourceToolAssistantUUID": "daadff89-45ad-44b2-acac-f891d5c97ff0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T15:04:10.781Z_

<details open><summary>🔧 Tool call — Read · `toolu_016huHvHaSMUFXRLiuQ2kFh1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1444c8f8-ea83-4c11-ba6a-ef5b742ba373",
  "isSidechain": false,
  "requestId": "req_011Cb4ZPfFiys4bQoz5H21we",
  "type": "assistant",
  "uuid": "daadff89-45ad-44b2-acac-f891d5c97ff0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014C28jekJvKExrjbakDjL9u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11809,
      "cache_read_input_tokens": 11447,
      "output_tokens": 174,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 174,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 11809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11809
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

_source line 14_

```json
{
  "type": "last-prompt",
  "leafUuid": "19a19ab8-371e-416d-8f6f-254f9849d0dc",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Sync experiments.tex and merge lr fix",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813"
}
```

---

### Assistant

_source line 16 · 2026-05-15T15:05:12.267Z_

<details><summary>Logged reasoning block</summary>

```text
Let me compare the two files:

1. **artifacts version** - the complete draft from experiments-draft Worker
2. **docs/paper version** - current compilation version with lr fix

Key differences I need to check:

1. **LR values**: 
   - artifacts: line 27: `learning rate $2 \times 10^{-4}$ (function-level) or $5 \times 10^{-5}$ (repo-level)` — CORRECT
   - docs/paper: line 16: `lr $2{\times}10^{-4}$ function-level / $5{\times}10^{-5}$ repo-level` — CORRECT

Both files already have the correct learning rate values.

2. **Citation keys**: I need to verify whether `shum2025swerm` vs `zhang2025swerm` and `maimon2026selfexecution` vs `ding2025selfexecution` appear in the artifacts version. Searching through it, I don't see any references to `swerm` or `selfexecution`, so those citation keys might not be present in the experiments file.

3. The task is to sync the artifacts version to docs/paper/ while preserving the learning rate fix. But examining both versions more carefully, the docs/paper version is actually more polished—it uses proper LaTeX macros like `\cls{}`, `\cwm{}`, and `\resizebox` for tables, whereas the artifacts version uses raw text formatting. I need to reconsider which version should be the source of truth here.

Looking at the content depth, the docs/paper version has more analysis subsections covering relaxed matching, variance compression, per-test metrics, and majority voting—sections that are missing from the artifacts version. This contradicts the task description calling the artifacts version the "complete draft," so I need to figure out what the actual intent is. I'm realizing the docs/paper version actually contains more analysis sections than the artifacts version, so syncing in that direction would lose content. Let me reconsider what the task is asking—maybe I should look for specific textual improvements in the artifacts version that could be merged back into the more complete docs/paper version rather than doing a wholesale replacement. I'm realizing the task is asking me to merge the lr fix from docs/paper into the artifacts version, not the other way around. But looking at the actual lr values in artifacts, they're already correct at `$2 \times 10^{-4}$` for function-level and `$5 \times 10^{-5}$` for repo-level. The docs/paper version seems to have more polished formatting with LaTeX macros and additional analysis paragraphs that would be lost if I just copied artifacts over. I should clarify with the user whether they want a true sync or if there's a specific lr discrepancy I'm missing. I'm noticing the mutation type definitions are completely different between the two versions—artifacts lists off_by_one and operator_swap while docs/paper has wrong_operator and type_error instead. The dataset splits match up (15,290 train / 1,896 validation / 1,890 test), but the class balance descriptions use different phrasing and precision levels. I need to dig deeper into what other content diverges between them. Looking at the differences in how results are presented, the paper uses a matched three-seed subset for the scaling behavior comparison which gives 1.18pp instead of the 1.24pp from all seeds, and includes additional analysis sections like relaxed matching, variance compression, and majority voting that aren't in the artifacts version. The repo-level results also differ in table structure and the paper adds context about sequence length and limitations.

Since the user explicitly asked me to overwrite, but the paper version is actually more complete with additional analysis and proper formatting, I should flag this for them — both files already have correct learning rates, the paper is more comprehensive, and overwriting would lose content. The artifacts version might have updated experiment numbers worth checking, but it's formatted as a standalone draft rather than integrated into the paper's style. The artifacts version has structural incompatibilities with the paper—it doesn't use the same LaTeX macros, has incomplete content in the Analysis section, uses different table formatting, and follows different label conventions. Simply copying it over would break compilation and lose existing content, so I need to alert the user to these issues before proceeding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19a19ab8-371e-416d-8f6f-254f9849d0dc",
  "isSidechain": false,
  "requestId": "req_011Cb4ZPvT2YX8MKfFX9DLG3",
  "type": "assistant",
  "uuid": "46faf664-0b38-4ded-854c-a83281f3e992",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013qm9EQT1zEpRi57p42R3ci",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14332,
      "cache_read_input_tokens": 23256,
      "output_tokens": 3201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14332,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3201,
          "cache_read_input_tokens": 23256,
          "cache_creation_input_tokens": 14332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14332
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

_source line 17 · 2026-05-15T15:05:12.270Z_

Both files have correct lr values already. Let me check citation keys.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "46faf664-0b38-4ded-854c-a83281f3e992",
  "isSidechain": false,
  "requestId": "req_011Cb4ZPvT2YX8MKfFX9DLG3",
  "type": "assistant",
  "uuid": "31a7ddea-eb1c-418a-87a1-2149a5b672fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013qm9EQT1zEpRi57p42R3ci",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14332,
      "cache_read_input_tokens": 23256,
      "output_tokens": 3201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14332,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3201,
          "cache_read_input_tokens": 23256,
          "cache_creation_input_tokens": 14332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14332
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

_source line 18 · 2026-05-15T15:05:13.232Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CsCe9RMVXs4cXrKEdqV3oG`</summary>

```json
{
  "pattern": "zhang2025swerm|ding2025selfexecution|shum2025swerm|maimon2026selfexecution",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/_project/paper/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31a7ddea-eb1c-418a-87a1-2149a5b672fa",
  "isSidechain": false,
  "requestId": "req_011Cb4ZPvT2YX8MKfFX9DLG3",
  "type": "assistant",
  "uuid": "b52a0be3-133e-48d4-aa74-8c85d7f9fb42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013qm9EQT1zEpRi57p42R3ci",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14332,
      "cache_read_input_tokens": 23256,
      "output_tokens": 3201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14332,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3201,
          "cache_read_input_tokens": 23256,
          "cache_creation_input_tokens": 14332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14332
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

_source line 19 · 2026-05-15T15:05:14.112Z_

<details><summary>↩ Tool result · `toolu_012hT1SddzqSeCQJLPt7DjWz`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2d9bcf2-75f2-43b9-86db-b0ba5d492e48",
  "isSidechain": false,
  "promptId": "d23e62c5-31bd-43a9-9cde-fc27110c6abe",
  "type": "user",
  "uuid": "c9983b0f-a55d-4bf3-968a-e40a1282176b",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "b2d9bcf2-75f2-43b9-86db-b0ba5d492e48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T15:05:13.254Z_

<details><summary>↩ Tool result · `toolu_01CsCe9RMVXs4cXrKEdqV3oG`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b52a0be3-133e-48d4-aa74-8c85d7f9fb42",
  "isSidechain": false,
  "promptId": "d23e62c5-31bd-43a9-9cde-fc27110c6abe",
  "type": "user",
  "uuid": "1350b818-fb3e-40a9-9cd1-177a185e4465",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "b52a0be3-133e-48d4-aa74-8c85d7f9fb42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T15:05:14.098Z_

<details open><summary>🔧 Tool call — Grep · `toolu_012hT1SddzqSeCQJLPt7DjWz`</summary>

```json
{
  "pattern": "zhang2025swerm|ding2025selfexecution|shum2025swerm|maimon2026selfexecution",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1350b818-fb3e-40a9-9cd1-177a185e4465",
  "isSidechain": false,
  "requestId": "req_011Cb4ZPvT2YX8MKfFX9DLG3",
  "type": "assistant",
  "uuid": "b2d9bcf2-75f2-43b9-86db-b0ba5d492e48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013qm9EQT1zEpRi57p42R3ci",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14332,
      "cache_read_input_tokens": 23256,
      "output_tokens": 3201,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14332,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3201,
          "cache_read_input_tokens": 23256,
          "cache_creation_input_tokens": 14332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14332
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

_source line 22 · 2026-05-15T15:05:19.751Z_

<details><summary>Logged reasoning block</summary>

```text
Neither file contains those citation keys. So citation key check passes.

Now let me flag the key issue to the user: the docs/paper version is MORE complete than the artifacts version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9983b0f-a55d-4bf3-968a-e40a1282176b",
  "isSidechain": false,
  "requestId": "req_011Cb4ZUb1dBiZuLvzHJUntH",
  "type": "assistant",
  "uuid": "7b7112b0-1d07-40b1-82f8-11374f15e489",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169tNjxFYqAnq66xw7rUB6g",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3257,
      "cache_read_input_tokens": 37588,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 512,
          "cache_read_input_tokens": 37588,
          "cache_creation_input_tokens": 3257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3257
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

_source line 23 · 2026-05-15T15:05:26.656Z_

两个文件都没有旧引用 key，这项检查通过。

对比两个文件后，**docs/paper 版本实际上比 artifacts 版本更完整**，不建议直接用 artifacts 覆盖：

| 方面 | artifacts 版本 | docs/paper 版本 |
|------|---------------|----------------|
| LaTeX 宏 | 不用（直接写 CLS/CWM） | 用 `\cls{}`, `\cwm{}`, `\pp{}`, `\fone{}` 等宏 |
| Analysis 段落 | 6 段 | 8 段（多了 relaxed matching, variance compression, precision/recall, majority voting） |
| 表格格式 | 简单 | `\resizebox` + per-seed 列 |
| Repo-level | 无 limitations 段 | 有 limitations 段 |
| Scaling 表 | 只有 Mean | 含 s42/s123/s456 列 |
| Label 命名 | `\label{ssec:...}` | `\label{sec:...}` |
| 引用命令 | `\citep` | `\cite` |
| lr 值 | 正确 | 正确 |

两个文件 lr 值都已经是正确的（$2{\times}10^{-4}$ function / $5{\times}10^{-5}$ repo），citation keys 也没问题。

**结论：docs/paper/experiments.tex 已经是更完整、格式更正确的版本，不需要从 artifacts 同步。** 覆盖反而会丢失内容并破坏编译。是否跳过这次同步？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b7112b0-1d07-40b1-82f8-11374f15e489",
  "isSidechain": false,
  "requestId": "req_011Cb4ZUb1dBiZuLvzHJUntH",
  "type": "assistant",
  "uuid": "cc6fc979-9dc1-4aeb-8bb6-a1a41fae12f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169tNjxFYqAnq66xw7rUB6g",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3257,
      "cache_read_input_tokens": 37588,
      "output_tokens": 512,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3257,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 512,
          "cache_read_input_tokens": 37588,
          "cache_creation_input_tokens": 3257,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3257
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

_source line 24_

```json
{
  "type": "last-prompt",
  "leafUuid": "cc6fc979-9dc1-4aeb-8bb6-a1a41fae12f9",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Sync experiments.tex and merge lr fix",
  "sessionId": "2c27d302-54b8-4f87-80cf-476c5bb38813"
}
```

---
