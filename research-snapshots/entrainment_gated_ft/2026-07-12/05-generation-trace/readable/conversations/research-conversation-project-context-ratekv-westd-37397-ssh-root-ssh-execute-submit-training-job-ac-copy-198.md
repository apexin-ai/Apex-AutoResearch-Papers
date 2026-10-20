# Research conversation: <project_context> # 项目: ratekv ## 运行环境 - 服务器名: westd-37397 - SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 accou

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/dc54b085-27d2-470a-bc77-92c047e6b5f2.jsonl`
- **Structured JSON:** [`cfb3fc88591d9520d2d8.json`](../../sessions/cf/cfb3fc88591d9520d2d8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T09:22:50.221Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T09:22:50.221Z",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "content": "&lt;project_context>\n# 项目: ratekv\n\n## 运行环境\n- 服务器名: westd-37397\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh westd-37397  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/ratekv\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n在 related work section 补充 3 个方法的讨论。\n\n## 文件\n- Related work: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex\n- References: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib\n- Appendix (已有 KVTuner 引用): /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex\n\n## 任务\n\n先读 related_work.tex 和 references.bib 了解现有结构。\n\n### 1. QAQ (mixed-precision KV cache)\n- 搜索 bib 中是否有 QAQ 条目。如果没有，添加 bib 条目（QAQ: Quality Adaptive Quantization for KV Cache）。\n- 在 related work 的 KV cache quantization 段落加 1-2 句：区分 QAQ 的 attention-score-based adaptive 方法与我们的 profiling-based per-head allocation + cardinality constraint。QAQ 用 attention score 动态决定精度，我们用离线 profiling 静态决定 + constraint 防止 compounding。\n- QAQ 论文信息：Dong et al., 2024, \"QAQ: Quality Adaptive Quantization for LLM KV Cache\", arXiv:2403.04643\n\n### 2. AQLM/QuIP# (non-additive weight quantization)\n- 检查 bib 中是否有这些条目。如果没有，添加。\n- 在 related work 中加 1-2 句作为 conceptual parallel：weight quantization 领域的 AQLM 和 QuIP# 已观察到量化误差的 non-additive 行为，我们在 KV cache 的 per-head allocation 中独立发现了类似现象。\n- AQLM: Egiazarian et al., 2024, \"AQLM: Extreme Compression of Large Language Models via Additive Quantization\", ICML 2024\n- QuIP#: Tseng et al., 2024, \"QuIP#: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks\", ICML 2024\n\n### 3. KVTuner (per-layer mixed-precision)\n- 已在 bib 中 (li2025kvtuner)，已在 appendix L61 提及。\n- 在 related_work.tex 的 KV cache 段落加 1-2 句：KVTuner 在 layer 级别做 mixed-precision（所有 heads in a layer 共享 bitwidth），我们在 head 级别做（更细粒度但搜索空间更大），cardinality constraint 使搜索空间可控。\n\n## 规范\n- 每个方法 1-2 句，简洁对比\n- LaTeX citation 格式正确\n- 完成后 grep 确认新引用在正文和 bib 中都存在"
}
```

---

### Runtime record

_source line 2 · 2026-05-16T09:22:50.224Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T09:22:50.224Z",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-16T09:22:50.258Z_

&lt;project_context>
# 项目: ratekv

## 运行环境
- 服务器名: westd-37397
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh westd-37397  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/ratekv


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
在 related work section 补充 3 个方法的讨论。

## 文件
- Related work: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex
- References: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib
- Appendix (已有 KVTuner 引用): /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex

## 任务

先读 related_work.tex 和 references.bib 了解现有结构。

### 1. QAQ (mixed-precision KV cache)
- 搜索 bib 中是否有 QAQ 条目。如果没有，添加 bib 条目（QAQ: Quality Adaptive Quantization for KV Cache）。
- 在 related work 的 KV cache quantization 段落加 1-2 句：区分 QAQ 的 attention-score-based adaptive 方法与我们的 profiling-based per-head allocation + cardinality constraint。QAQ 用 attention score 动态决定精度，我们用离线 profiling 静态决定 + constraint 防止 compounding。
- QAQ 论文信息：Dong et al., 2024, "QAQ: Quality Adaptive Quantization for LLM KV Cache", arXiv:2403.04643

### 2. AQLM/QuIP# (non-additive weight quantization)
- 检查 bib 中是否有这些条目。如果没有，添加。
- 在 related work 中加 1-2 句作为 conceptual parallel：weight quantization 领域的 AQLM 和 QuIP# 已观察到量化误差的 non-additive 行为，我们在 KV cache 的 per-head allocation 中独立发现了类似现象。
- AQLM: Egiazarian et al., 2024, "AQLM: Extreme Compression of Large Language Models via Additive Quantization", ICML 2024
- QuIP#: Tseng et al., 2024, "QuIP#: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks", ICML 2024

### 3. KVTuner (per-layer mixed-precision)
- 已在 bib 中 (li2025kvtuner)，已在 appendix L61 提及。
- 在 related_work.tex 的 KV cache 段落加 1-2 句：KVTuner 在 layer 级别做 mixed-precision（所有 heads in a layer 共享 bitwidth），我们在 head 级别做（更细粒度但搜索空间更大），cardinality constraint 使搜索空间可控。

## 规范
- 每个方法 1-2 句，简洁对比
- LaTeX citation 格式正确
- 完成后 grep 确认新引用在正文和 bib 中都存在

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "57178dec-a181-4689-b8dc-6bbe16ba62d5",
  "type": "user",
  "uuid": "40a44b9f-ec42-4524-8222-9202fd9fab70",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T09:22:50.257Z_

```json
{
  "parentUuid": "40a44b9f-ec42-4524-8222-9202fd9fab70",
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
  "uuid": "1310ec62-d846-4e99-be62-3d4e159355fd",
  "timestamp": "2026-05-16T09:22:50.257Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T09:22:50.257Z_

```json
{
  "parentUuid": "1310ec62-d846-4e99-be62-3d4e159355fd",
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
  "uuid": "2e2a79b3-7380-4e74-b5af-ab5b0cf90dd0",
  "timestamp": "2026-05-16T09:22:50.257Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T09:22:50.257Z_

```json
{
  "parentUuid": "2e2a79b3-7380-4e74-b5af-ab5b0cf90dd0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "36dddfdd-af53-4c2c-a25b-a3caa9a53164",
  "timestamp": "2026-05-16T09:22:50.257Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
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
  "aiTitle": "Add three methods to related work section",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2"
}
```

---

### Assistant

_source line 8 · 2026-05-16T09:22:53.375Z_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the related_work.tex and references.bib files to understand the current structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36dddfdd-af53-4c2c-a25b-a3caa9a53164",
  "isSidechain": false,
  "requestId": "req_011Cb61B81UCdft6midd83iE",
  "type": "assistant",
  "uuid": "6f8bb246-b557-4c16-a105-321c6d8e82cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0128YotsKdoP1MSfMvmzkzSm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12719,
      "cache_read_input_tokens": 11841,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12719
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

_source line 9 · 2026-05-16T09:22:53.867Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DDHho3St23qDuwSsk3ktkQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f8bb246-b557-4c16-a105-321c6d8e82cd",
  "isSidechain": false,
  "requestId": "req_011Cb61B81UCdft6midd83iE",
  "type": "assistant",
  "uuid": "826d2f38-dc38-4377-b1ea-4662748895ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0128YotsKdoP1MSfMvmzkzSm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12719,
      "cache_read_input_tokens": 11841,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12719
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

_source line 10 · 2026-05-16T09:22:53.877Z_

<details><summary>↩ Tool result · `toolu_01DDHho3St23qDuwSsk3ktkQ`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{KV Cache Quantization.}
4	Uniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\cite{lin2024qserve}, salient-token identification~\cite{he2024zipcache}, low-rank plus sparse correction~\cite{kang2024gear}, sliding-window adaptation~\cite{duanmu2024skvq}, rotation-based outlier smoothing for robust 2-bit~\cite{su2025rotatekv}, 2-bit with adaptive token retention~\cite{sharma2025minikv}, and adapter-based inter-layer prediction at 2--2.5 bits~\cite{shutova2025aquakv}.
5	We extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\{2,4,8,16\}$.
6	Our per-head bit-width allocation is orthogonal to per-channel quantization schemes such as KIVI: KIVI determines \emph{how} each head is quantized (asymmetric per-channel scaling), while our method determines \emph{at what precision} (bit-width selection across heads).
7	The two can be composed, though the per-channel method dominates when available (\S\ref{sec:main_results}); per-head allocation provides independent value in symmetric-only environments where per-channel asymmetric quantization is unavailable.
8	
9	\paragraph{KV Cache Eviction.}
10	Complementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\cite{zhang2023h2o}, per-head important tokens~\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\cite{liu2024scissorhands}, attention sinks~\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\cite{yang2024pyramidinfer}.
11	Recent per-head eviction methods allocate non-uniform budgets across heads based on retrieval-vs-reasoning importance~\cite{fu2025headkv} or adaptive optimization extending SnapKV/PyramidKV~\cite{feng2025adakv}, confirming that head-level heterogeneity is exploitable for eviction; our work shows it is equally exploitable for quantization.
12	
13	
14	\paragraph{Mixed-Precision Quantization (Weights).}
15	Mixed-precision allocation has a long history at the weight level.
16	HAWQ~\cite{dong2019hawq} and HAWQ-V2~\cite{dong2020hawqv2} use second-order (Hessian-based) sensitivity to assign per-layer bit-widths, with V2 introducing block-wise trace-weighted scoring and Pareto-frontier selection; HAQ~\cite{wang2019haq} learns an allocation by reinforcement learning under hardware-aware latency/energy constraints.
17	These methods operate on weights, where per-layer distortions are approximately additive and sensitivity varies smoothly across layers.
18	KV cache quantization presents a qualitatively different challenge: 2-bit head distortions compound super-additively through the residual stream (\S\ref{sec:compounding}), a phenomenon absent in weight quantization where each layer's parameters are independently quantized.
19	Our primary contribution is not the allocation algorithm itself---any MCKP or greedy solver suffices---but the diagnosis and fix of this compounding effect via cardinality constraints, and the characterization of when non-uniform allocation is beneficial (\S\ref{sec:heterogeneity}).
20	
21	\paragraph{Mixed-Precision Rate-Distortion Allocation.}
22	RateQuant~\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\{2,\ldots,6\}$ via the polymatroid structure, which relies on the assumption that per-head distortions decompose additively into the global objective---valid when adjacent bit-widths differ by a single bit so that quantization noise stays in the small-perturbation regime.
23	On hardware-aligned $\{2,4,8,16\}$, the 4$\times$ gap between 2-bit and 4-bit drives 2-bit distortion to compound super-additively, breaking the polymatroid structure and the additivity assumption with it.
24	Concretely, running RateQuant's greedy algorithm (Algorithm~1) directly on $\{2,4,8,16\}$ yields 32.45 PPL on Qwen2.5-7B at $4\times$ compression---catastrophically worse than uniform 4-bit (15.45)---whereas our cardinality constraint on simultaneously active 2-bit heads recovers 10.91 PPL at the same average bit-width.
25	The constraint is the minimal fix that restores the additive regime in which RateQuant's polymatroid argument applies.
26	Related mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\cite{xia2025kitty}, token-level via a learned on-device controller~\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\cite{lei2026arkv}---at the weight level~\cite{kim2024squeezellm}, or dynamically at inference time~\cite{zhang2025mixkvq}; our allocation is static and per-head.
27	
28	\paragraph{Attention Head Analysis.}
29	Prior work studies head redundancy and pruning~\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.
30	Our analysis asks a different question: which heads are sensitive to \emph{quantization}, and how heterogeneous that sensitivity is across architectures---a property that determines whether non-uniform allocation is beneficial (\S\ref{sec:heterogeneity}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "826d2f38-dc38-4377-b1ea-4662748895ce",
  "isSidechain": false,
  "promptId": "57178dec-a181-4689-b8dc-6bbe16ba62d5",
  "type": "user",
  "uuid": "c6562eda-8642-4534-8023-bfe43cc2595d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{KV Cache Quantization.}\nUniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\\cite{lin2024qserve}, salient-token identification~\\cite{he2024zipcache}, low-rank plus sparse correction~\\cite{kang2024gear}, sliding-window adaptation~\\cite{duanmu2024skvq}, rotation-based outlier smoothing for robust 2-bit~\\cite{su2025rotatekv}, 2-bit with adaptive token retention~\\cite{sharma2025minikv}, and adapter-based inter-layer prediction at 2--2.5 bits~\\cite{shutova2025aquakv}.\nWe extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\\{2,4,8,16\\}$.\nOur per-head bit-width allocation is orthogonal to per-channel quantization schemes such as KIVI: KIVI determines \\emph{how} each head is quantized (asymmetric per-channel scaling), while our method determines \\emph{at what precision} (bit-width selection across heads).\nThe two can be composed, though the per-channel method dominates when available (\\S\\ref{sec:main_results}); per-head allocation provides independent value in symmetric-only environments where per-channel asymmetric quantization is unavailable.\n\n\\paragraph{KV Cache Eviction.}\nComplementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\\cite{zhang2023h2o}, per-head important tokens~\\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\\cite{liu2024scissorhands}, attention sinks~\\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\\cite{yang2024pyramidinfer}.\nRecent per-head eviction methods allocate non-uniform budgets across heads based on retrieval-vs-reasoning importance~\\cite{fu2025headkv} or adaptive optimization extending SnapKV/PyramidKV~\\cite{feng2025adakv}, confirming that head-level heterogeneity is exploitable for eviction; our work shows it is equally exploitable for quantization.\n\n\n\\paragraph{Mixed-Precision Quantization (Weights).}\nMixed-precision allocation has a long history at the weight level.\nHAWQ~\\cite{dong2019hawq} and HAWQ-V2~\\cite{dong2020hawqv2} use second-order (Hessian-based) sensitivity to assign per-layer bit-widths, with V2 introducing block-wise trace-weighted scoring and Pareto-frontier selection; HAQ~\\cite{wang2019haq} learns an allocation by reinforcement learning under hardware-aware latency/energy constraints.\nThese methods operate on weights, where per-layer distortions are approximately additive and sensitivity varies smoothly across layers.\nKV cache quantization presents a qualitatively different challenge: 2-bit head distortions compound super-additively through the residual stream (\\S\\ref{sec:compounding}), a phenomenon absent in weight quantization where each layer's parameters are independently quantized.\nOur primary contribution is not the allocation algorithm itself---any MCKP or greedy solver suffices---but the diagnosis and fix of this compounding effect via cardinality constraints, and the characterization of when non-uniform allocation is beneficial (\\S\\ref{sec:heterogeneity}).\n\n\\paragraph{Mixed-Precision Rate-Distortion Allocation.}\nRateQuant~\\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\\{2,\\ldots,6\\}$ via the polymatroid structure, which relies on the assumption that per-head distortions decompose additively into the global objective---valid when adjacent bit-widths differ by a single bit so that quantization noise stays in the small-perturbation regime.\nOn hardware-aligned $\\{2,4,8,16\\}$, the 4$\\times$ gap between 2-bit and 4-bit drives 2-bit distortion to compound super-additively, breaking the polymatroid structure and the additivity assumption with it.\nConcretely, running RateQuant's greedy algorithm (Algorithm~1) directly on $\\{2,4,8,16\\}$ yields 32.45 PPL on Qwen2.5-7B at $4\\times$ compression---catastrophically worse than uniform 4-bit (15.45)---whereas our cardinality constraint on simultaneously active 2-bit heads recovers 10.91 PPL at the same average bit-width.\nThe constraint is the minimal fix that restores the additive regime in which RateQuant's polymatroid argument applies.\nRelated mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\\cite{xia2025kitty}, token-level via a learned on-device controller~\\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\\cite{lei2026arkv}---at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.\n\n\\paragraph{Attention Head Analysis.}\nPrior work studies head redundancy and pruning~\\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.\nOur analysis asks a different question: which heads are sensitive to \\emph{quantization}, and how heterogeneous that sensitivity is across architectures---a property that determines whether non-uniform allocation is beneficial (\\S\\ref{sec:heterogeneity}).",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 30
    }
  },
  "sourceToolAssistantUUID": "826d2f38-dc38-4377-b1ea-4662748895ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T09:22:54.257Z_

<details><summary>↩ Tool result · `toolu_01BTDTnc8rFsiRzfNT8uwZ8g`</summary>

```text
1	% Auto-generated from literature_map.yaml (verified=true entries)
2	
3	@inproceedings{liu2024kivi,
4	  title = {{KIVI}: A Tuning-Free Asymmetric 2bit Quantization for {KV} Cache},
5	  author = {Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and Vladimir Braverman and Beidi Chen and Xia Hu},
6	  year = {2024},
7	  booktitle = {ICML 2024},
8	  url = {https://arxiv.org/abs/2402.02750},
9	}
10	
11	@inproceedings{hooper2024kvquant,
12	  title = {{KVQuant}: Towards 10 Million Context Length {LLM} Inference with {KV} Cache Quantization},
13	  author = {Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and Yakun Sophia Shao and Kurt Keutzer and Amir Gholami},
14	  year = {2024},
15	  booktitle = {NeurIPS 2024},
16	  url = {https://arxiv.org/abs/2401.18079},
17	}
18	
19	@inproceedings{lin2024qserve,
20	  title = {{QServe}: {W4A8KV4} Quantization and System Co-design for Efficient {LLM} Serving},
21	  author = {Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao and Chuang Gan and Song Han},
22	  year = {2025},
23	  booktitle = {MLSys 2025},
24	  url = {https://arxiv.org/abs/2405.04532},
25	}
26	
27	@inproceedings{he2024zipcache,
28	  title = {{ZipCache}: Accurate and Efficient {KV} Cache Quantization with Salient Token Identification},
29	  author = {Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zhuang},
30	  year = {2024},
31	  booktitle = {NeurIPS 2024},
32	  url = {https://arxiv.org/abs/2405.14256},
33	}
34	
35	@misc{kang2024gear,
36	  title = {{GEAR}: An Efficient {KV} Cache Compression Recipe for Near-Lossless Generative Inference of {LLM}},
37	  author = {Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and Tushar Krishna and Tuo Zhao},
38	  year = {2024},
39	  note = {arXiv preprint},
40	  url = {https://arxiv.org/abs/2403.05527},
41	  eprint = {2403.05527},
42	  archivePrefix = {arXiv},
43	}
44	
45	@misc{duanmu2024skvq,
46	  title = {{SKVQ}: Sliding-window Key and Value Cache Quantization for Large Language Models},
47	  author = {Haojie Duanmu and Zhihang Yuan and Xiuhong Li and Jiangfei Duan and Xingcheng Zhang and Dahua Lin},
48	  year = {2024},
49	  note = {arXiv preprint},
50	  url = {https://arxiv.org/abs/2405.06219},
51	  eprint = {2405.06219},
52	  archivePrefix = {arXiv},
53	}
54	
55	@inproceedings{zhang2023h2o,
56	  title = {{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},
57	  author = {Zhenyu Zhang and Ying Sheng and Tianyi Zhou and Tianlong Chen and Lianmin Zheng and Ruisi Cai and Zhao Song and Yuandong Tian and Christopher R{\'{e}} and Clark Barrett and Zhangyang Wang and Beidi Chen},
58	  year = {2023},
59	  booktitle = {NeurIPS 2023},
60	  url = {https://arxiv.org/abs/2306.14048},
61	}
62	
63	@inproceedings{li2024snapkv,
64	  title = {{SnapKV}: {LLM} Knows What You are Looking for Before Generation},
65	  author = {Yuhong Li and Yingbing Huang and Bowen Yang and Bharat Venkitesh and Acyr Locatelli and Hanchen Ye and Tianle Cai and Patrick Lewis and Deming Chen},
66	  year = {2024},
67	  booktitle = {NeurIPS 2024},
68	  url = {https://arxiv.org/abs/2404.14469},
69	}
70	
71	@inproceedings{ge2024fastgen,
72	  title = {Model Tells You What to Discard: Adaptive {KV} Cache Compression for {LLMs}},
73	  author = {Suyu Ge and Yunan Zhang and Liyuan Liu and Minjia Zhang and Jiawei Han and Jianfeng Gao},
74	  year = {2024},
75	  booktitle = {ICLR 2024},
76	  url = {https://arxiv.org/abs/2310.01801},
77	}
78	
79	@inproceedings{xiao2024streamingllm,
80	  title = {Efficient Streaming Language Models with Attention Sinks},
81	  author = {Guangxuan Xiao and Yuandong Tian and Beidi Chen and Song Han and Mike Lewis},
82	  year = {2024},
83	  booktitle = {ICLR 2024},
84	  url = {https://arxiv.org/abs/2309.17453},
85	}
86	
87	@inproceedings{liu2024scissorhands,
88	  title = {Scissorhands: Exploiting the Persistence of Importance Hypothesis for {LLM} {KV} Cache Compression at Test Time},
89	  author = {Zichang Liu and Aditya Desai and Fangshuo Liao and Weitao Wang and Victor Xie and Zhaozhuo Xu and Anastasios Kyrillidis and Anshumali Shrivastava},
90	  year = {2023},
91	  booktitle = {NeurIPS 2023},
92	  url = {https://arxiv.org/abs/2305.17118},
93	}
94	
95	@inproceedings{yang2024pyramidinfer,
96	  title = {{PyramidInfer}: Pyramid {KV} Cache Compression for High-throughput {LLM} Inference},
97	  author = {Dongjie Yang and Xiaodong Han and Yan Gao and Yao Hu and Shilin Zhang and Hai Zhao},
98	  year = {2024},
99	  booktitle = {Findings of ACL 2024},
100	  url = {https://arxiv.org/abs/2405.12532},
101	}
102	
103	@misc{zuo2026ratequant,
104	  title = {{RateQuant}: Optimal Mixed-Precision {KV} Cache Quantization via Rate-Distortion Theory},
105	  author = {Fei Zuo and Zikang Zhou and Hao Cong and Xiaoyan Xi and Ho Fai Leung},
106	  year = {2026},
107	  note = {arXiv preprint},
108	  url = {https://arxiv.org/abs/2605.06675},
109	  eprint = {2605.06675},
110	  archivePrefix = {arXiv},
111	}
112	
113	@misc{lei2026arkv,
114	  title = {{ARKV}: Adaptive and Resource-Efficient {KV} Cache Management under Limited Memory Budget for Long-Context Inference in {LLMs}},
115	  author = {Jianlong Lei and Shashikant Ilager},
116	  year = {2026},
117	  note = {arXiv preprint},
118	  url = {https://arxiv.org/abs/2603.08727},
119	  eprint = {2603.08727},
120	  archivePrefix = {arXiv},
121	}
122	
123	@misc{li2025kvmix,
124	  title = {{KVmix}: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for {KV} Cache},
125	  author = {Fei Li and Song Liu and Weiguo Wu and Shiqiang Nie and Jinyu Wang},
126	  year = {2025},
127	  note = {arXiv preprint},
128	  url = {https://arxiv.org/abs/2506.08018},
129	  eprint = {2506.08018},
130	  archivePrefix = {arXiv},
131	}
132	
133	@misc{zhang2025mixkvq,
134	  title = {{MixKVQ}: Query-Aware Mixed-Precision {KV} Cache Quantization for Long-Context Reasoning},
135	  author = {Tao Zhang and Ziqian Zeng and Hao Peng and Huiping Zhuang and Cen Chen},
136	  year = {2025},
137	  note = {arXiv preprint},
138	  url = {https://arxiv.org/abs/2512.19206},
139	  eprint = {2512.19206},
140	  archivePrefix = {arXiv},
141	}
142	
143	@inproceedings{kim2024squeezellm,
144	  title = {{SqueezeLLM}: Dense-and-Sparse Quantization},
145	  author = {Sehoon Kim and Coleman Hooper and Amir Gholami and Zhen Dong and Xiuyu Li and Sheng Shen and Michael W. Mahoney and Kurt Keutzer},
146	  year = {2024},
147	  booktitle = {ICML 2024},
148	  url = {https://arxiv.org/abs/2306.07629},
149	}
150	
151	@inproceedings{fu2025headkv,
152	  title = {Not All Heads Matter: A Head-Level {KV} Cache Compression Method with Integrated Retrieval and Reasoning},
153	  author = {Yu Fu and Zefan Cai and Abdelrahman Sid-Lakhdar and Wayne Xin Zhao and Richard Peng},
154	  year = {2025},
155	  booktitle = {ICLR 2025},
156	  url = {https://arxiv.org/abs/2410.19258},
157	}
158	
159	@inproceedings{feng2025adakv,
160	  title = {{Ada-KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation},
161	  author = {Yuan Feng and Junlin Lv and Yukun Cao and Xike Xie and S. Kevin Zhou},
162	  year = {2025},
163	  booktitle = {NeurIPS 2025},
164	  url = {https://arxiv.org/abs/2407.11550},
165	}
166	
167	@inproceedings{li2025kvtuner,
168	  title = {{KVTuner}: Sensitivity-Aware Layer-Wise Mixed-Precision {KV} Cache Quantization for Efficient and Nearly Lossless {LLM} Inference},
169	  author = {Li, Zhongzhi and Shen, Yuhan and Tang, Yixuan and Luo, Jian and Dai, Yonggang},
170	  year = {2025},
171	  booktitle = {ICML 2025},
172	  url = {https://arxiv.org/abs/2502.04420},
173	}
174	
175	@inproceedings{voita2019analyzing,
176	  title = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},
177	  author = {Elena Voita and David Talbot and Fedor Moiseev and Rico Sennrich and Ivan Titov},
178	  year = {2019},
179	  booktitle = {ACL 2019},
180	  url = {https://arxiv.org/abs/1905.09418},
181	}
182	
183	@inproceedings{michel2019sixteen,
184	  title = {Are Sixteen Heads Really Better than One?},
185	  author = {Paul Michel and Omer Levy and Graham Neubig},
186	  year = {2019},
187	  booktitle = {NeurIPS 2019},
188	  url = {https://arxiv.org/abs/1905.10650},
189	}
190	
191	@inproceedings{dong2019hawq,
192	  title = {{HAWQ}: {Hessian} AWare Quantization of Neural Networks with Mixed-Precision},
193	  author = {Zhen Dong and Zhewei Yao and Amir Gholami and Michael W. Mahoney and Kurt Keutzer},
194	  year = {2019},
195	  booktitle = {ICCV 2019},
196	  url = {https://arxiv.org/abs/1905.03696},
197	}
198	
199	@inproceedings{dong2020hawqv2,
200	  title = {{HAWQ-V2}: {Hessian} Aware trace-Weighted Quantization of Neural Networks},
201	  author = {Zhen Dong and Zhewei Yao and Yaohui Cai and Daiyaan Arfeen and Amir Gholami and Michael W. Mahoney and Kurt Keutzer},
202	  year = {2020},
203	  booktitle = {NeurIPS 2020},
204	  url = {https://arxiv.org/abs/1911.03852},
205	}
206	
207	@inproceedings{wang2019haq,
208	  title = {{HAQ}: Hardware-Aware Automated Quantization with Mixed Precision},
209	  author = {Kuan Wang and Zhijian Liu and Yujun Lin and Ji Lin and Song Han},
210	  year = {2019},
211	  booktitle = {CVPR 2019},
212	  url = {https://arxiv.org/abs/1811.08886},
213	}
214	
215	@inproceedings{su2025rotatekv,
216	  title = {{RotateKV}: Accurate and Robust 2-Bit {KV} Cache Quantization for {LLMs} via Outlier-Aware Adaptive Rotations},
217	  author = {Zunhai Su and Zhe Chen and Wang Shen and Hanyu Wei and Linge Li and Huangqi Yu and Kehong Yuan},
218	  year = {2025},
219	  booktitle = {IJCAI 2025},
220	  url = {https://arxiv.org/abs/2501.16383},
221	}
222	
223	@inproceedings{sharma2025minikv,
224	  title = {{MiniKV}: Pushing the Limits of 2-Bit {KV} Cache via Compression and System Co-Design for Efficient Long Context Inference},
225	  author = {Akshat Sharma and Hangliang Ding and Jianping Li and Neel Dani and Minjia Zhang},
226	  year = {2025},
227	  booktitle = {Findings of ACL 2025},
228	  url = {https://arxiv.org/abs/2411.18077},
229	}
230	
231	@inproceedings{shutova2025aquakv,
232	  title = {Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models},
233	  author = {Alina Shutova and Vladimir Malinovskii and Vage Egiazarian and Denis Kuznedelev and Denis Mazur and Nikita Surkov and Ivan Ermakov and Dan Alistarh},
234	  year = {2025},
235	  booktitle = {ICML 2025},
236	  url = {https://arxiv.org/abs/2501.19392},
237	}
238	
239	@misc{liu2025pmkvq,
240	  title = {{PM-KVQ}: Progressive Mixed-precision {KV} Cache Quantization for Long-CoT {LLMs}},
241	  author = {Tengxuan Liu and Shiyao Li and Jiayi Yang and Tianchen Zhao and Feng Zhou and Xiaohui Song and Guohao Dai and Shengen Yan and Huazhong Yang and Yu Wang},
242	  year = {2025},
243	  note = {arXiv preprint},
244	  url = {https://arxiv.org/abs/2505.18610},
245	  eprint = {2505.18610},
246	  archivePrefix = {arXiv},
247	}
248	
249	@misc{xia2025kitty,
250	  title = {{Kitty}: Accurate and Efficient 2-bit {KV} Cache Quantization with Dynamic Channel-wise Precision Boost},
251	  author = {Haojun Xia and Xiaoxia Wu and Jisen Li and Robert Wu and Junxiong Wang and Jue Wang and Chenxi Li and Aman Singhal and Alay Dilipbhai Shah and Alpay Ariyak and Donglin Zhuang and Zhongzhu Zhou and Ben Athiwaratkun and Zhen Zheng and Shuaiwen Leon Song},
252	  year = {2025},
253	  note = {arXiv preprint},
254	  url = {https://arxiv.org/abs/2511.18643},
255	  eprint = {2511.18643},
256	  archivePrefix = {arXiv},
257	}
258	
259	@inproceedings{haeriboroujeni2026dontwaste,
260	  title = {Don't Waste Bits! {Adaptive} {KV}-Cache Quantization for Lightweight On-Device {LLMs}},
261	  author = {Haeri Boroujeni, Sayed Pedram and Mehrabi, Niloufar and Woods, Patrick and Hillesheim, Gabriel and Razi, Abolfazl},
262	  year = {2026},
263	  booktitle = {CVPR 2026},
264	  url = {https://arxiv.org/abs/2604.04722},
265	}
266	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81e371c5-853f-44e9-89af-bd3bce878813",
  "isSidechain": false,
  "promptId": "57178dec-a181-4689-b8dc-6bbe16ba62d5",
  "type": "user",
  "uuid": "d529a322-7cf7-49ad-9201-b468d42058f7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib",
      "content": "% Auto-generated from literature_map.yaml (verified=true entries)\n\n@inproceedings{liu2024kivi,\n  title = {{KIVI}: A Tuning-Free Asymmetric 2bit Quantization for {KV} Cache},\n  author = {Zirui Liu and Jiayi Yuan and Hongye Jin and Shaochen Zhong and Zhaozhuo Xu and Vladimir Braverman and Beidi Chen and Xia Hu},\n  year = {2024},\n  booktitle = {ICML 2024},\n  url = {https://arxiv.org/abs/2402.02750},\n}\n\n@inproceedings{hooper2024kvquant,\n  title = {{KVQuant}: Towards 10 Million Context Length {LLM} Inference with {KV} Cache Quantization},\n  author = {Coleman Hooper and Sehoon Kim and Hiva Mohammadzadeh and Michael W. Mahoney and Yakun Sophia Shao and Kurt Keutzer and Amir Gholami},\n  year = {2024},\n  booktitle = {NeurIPS 2024},\n  url = {https://arxiv.org/abs/2401.18079},\n}\n\n@inproceedings{lin2024qserve,\n  title = {{QServe}: {W4A8KV4} Quantization and System Co-design for Efficient {LLM} Serving},\n  author = {Yujun Lin and Haotian Tang and Shang Yang and Zhekai Zhang and Guangxuan Xiao and Chuang Gan and Song Han},\n  year = {2025},\n  booktitle = {MLSys 2025},\n  url = {https://arxiv.org/abs/2405.04532},\n}\n\n@inproceedings{he2024zipcache,\n  title = {{ZipCache}: Accurate and Efficient {KV} Cache Quantization with Salient Token Identification},\n  author = {Yefei He and Luoming Zhang and Weijia Wu and Jing Liu and Hong Zhou and Bohan Zhuang},\n  year = {2024},\n  booktitle = {NeurIPS 2024},\n  url = {https://arxiv.org/abs/2405.14256},\n}\n\n@misc{kang2024gear,\n  title = {{GEAR}: An Efficient {KV} Cache Compression Recipe for Near-Lossless Generative Inference of {LLM}},\n  author = {Hao Kang and Qingru Zhang and Souvik Kundu and Geonhwa Jeong and Zaoxing Liu and Tushar Krishna and Tuo Zhao},\n  year = {2024},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2403.05527},\n  eprint = {2403.05527},\n  archivePrefix = {arXiv},\n}\n\n@misc{duanmu2024skvq,\n  title = {{SKVQ}: Sliding-window Key and Value Cache Quantization for Large Language Models},\n  author = {Haojie Duanmu and Zhihang Yuan and Xiuhong Li and Jiangfei Duan and Xingcheng Zhang and Dahua Lin},\n  year = {2024},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2405.06219},\n  eprint = {2405.06219},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{zhang2023h2o,\n  title = {{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n  author = {Zhenyu Zhang and Ying Sheng and Tianyi Zhou and Tianlong Chen and Lianmin Zheng and Ruisi Cai and Zhao Song and Yuandong Tian and Christopher R{\\'{e}} and Clark Barrett and Zhangyang Wang and Beidi Chen},\n  year = {2023},\n  booktitle = {NeurIPS 2023},\n  url = {https://arxiv.org/abs/2306.14048},\n}\n\n@inproceedings{li2024snapkv,\n  title = {{SnapKV}: {LLM} Knows What You are Looking for Before Generation},\n  author = {Yuhong Li and Yingbing Huang and Bowen Yang and Bharat Venkitesh and Acyr Locatelli and Hanchen Ye and Tianle Cai and Patrick Lewis and Deming Chen},\n  year = {2024},\n  booktitle = {NeurIPS 2024},\n  url = {https://arxiv.org/abs/2404.14469},\n}\n\n@inproceedings{ge2024fastgen,\n  title = {Model Tells You What to Discard: Adaptive {KV} Cache Compression for {LLMs}},\n  author = {Suyu Ge and Yunan Zhang and Liyuan Liu and Minjia Zhang and Jiawei Han and Jianfeng Gao},\n  year = {2024},\n  booktitle = {ICLR 2024},\n  url = {https://arxiv.org/abs/2310.01801},\n}\n\n@inproceedings{xiao2024streamingllm,\n  title = {Efficient Streaming Language Models with Attention Sinks},\n  author = {Guangxuan Xiao and Yuandong Tian and Beidi Chen and Song Han and Mike Lewis},\n  year = {2024},\n  booktitle = {ICLR 2024},\n  url = {https://arxiv.org/abs/2309.17453},\n}\n\n@inproceedings{liu2024scissorhands,\n  title = {Scissorhands: Exploiting the Persistence of Importance Hypothesis for {LLM} {KV} Cache Compression at Test Time},\n  author = {Zichang Liu and Aditya Desai and Fangshuo Liao and Weitao Wang and Victor Xie and Zhaozhuo Xu and Anastasios Kyrillidis and Anshumali Shrivastava},\n  year = {2023},\n  booktitle = {NeurIPS 2023},\n  url = {https://arxiv.org/abs/2305.17118},\n}\n\n@inproceedings{yang2024pyramidinfer,\n  title = {{PyramidInfer}: Pyramid {KV} Cache Compression for High-throughput {LLM} Inference},\n  author = {Dongjie Yang and Xiaodong Han and Yan Gao and Yao Hu and Shilin Zhang and Hai Zhao},\n  year = {2024},\n  booktitle = {Findings of ACL 2024},\n  url = {https://arxiv.org/abs/2405.12532},\n}\n\n@misc{zuo2026ratequant,\n  title = {{RateQuant}: Optimal Mixed-Precision {KV} Cache Quantization via Rate-Distortion Theory},\n  author = {Fei Zuo and Zikang Zhou and Hao Cong and Xiaoyan Xi and Ho Fai Leung},\n  year = {2026},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2605.06675},\n  eprint = {2605.06675},\n  archivePrefix = {arXiv},\n}\n\n@misc{lei2026arkv,\n  title = {{ARKV}: Adaptive and Resource-Efficient {KV} Cache Management under Limited Memory Budget for Long-Context Inference in {LLMs}},\n  author = {Jianlong Lei and Shashikant Ilager},\n  year = {2026},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2603.08727},\n  eprint = {2603.08727},\n  archivePrefix = {arXiv},\n}\n\n@misc{li2025kvmix,\n  title = {{KVmix}: Gradient-Based Layer Importance-Aware Mixed-Precision Quantization for {KV} Cache},\n  author = {Fei Li and Song Liu and Weiguo Wu and Shiqiang Nie and Jinyu Wang},\n  year = {2025},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2506.08018},\n  eprint = {2506.08018},\n  archivePrefix = {arXiv},\n}\n\n@misc{zhang2025mixkvq,\n  title = {{MixKVQ}: Query-Aware Mixed-Precision {KV} Cache Quantization for Long-Context Reasoning},\n  author = {Tao Zhang and Ziqian Zeng and Hao Peng and Huiping Zhuang and Cen Chen},\n  year = {2025},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2512.19206},\n  eprint = {2512.19206},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{kim2024squeezellm,\n  title = {{SqueezeLLM}: Dense-and-Sparse Quantization},\n  author = {Sehoon Kim and Coleman Hooper and Amir Gholami and Zhen Dong and Xiuyu Li and Sheng Shen and Michael W. Mahoney and Kurt Keutzer},\n  year = {2024},\n  booktitle = {ICML 2024},\n  url = {https://arxiv.org/abs/2306.07629},\n}\n\n@inproceedings{fu2025headkv,\n  title = {Not All Heads Matter: A Head-Level {KV} Cache Compression Method with Integrated Retrieval and Reasoning},\n  author = {Yu Fu and Zefan Cai and Abdelrahman Sid-Lakhdar and Wayne Xin Zhao and Richard Peng},\n  year = {2025},\n  booktitle = {ICLR 2025},\n  url = {https://arxiv.org/abs/2410.19258},\n}\n\n@inproceedings{feng2025adakv,\n  title = {{Ada-KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation},\n  author = {Yuan Feng and Junlin Lv and Yukun Cao and Xike Xie and S. Kevin Zhou},\n  year = {2025},\n  booktitle = {NeurIPS 2025},\n  url = {https://arxiv.org/abs/2407.11550},\n}\n\n@inproceedings{li2025kvtuner,\n  title = {{KVTuner}: Sensitivity-Aware Layer-Wise Mixed-Precision {KV} Cache Quantization for Efficient and Nearly Lossless {LLM} Inference},\n  author = {Li, Zhongzhi and Shen, Yuhan and Tang, Yixuan and Luo, Jian and Dai, Yonggang},\n  year = {2025},\n  booktitle = {ICML 2025},\n  url = {https://arxiv.org/abs/2502.04420},\n}\n\n@inproceedings{voita2019analyzing,\n  title = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},\n  author = {Elena Voita and David Talbot and Fedor Moiseev and Rico Sennrich and Ivan Titov},\n  year = {2019},\n  booktitle = {ACL 2019},\n  url = {https://arxiv.org/abs/1905.09418},\n}\n\n@inproceedings{michel2019sixteen,\n  title = {Are Sixteen Heads Really Better than One?},\n  author = {Paul Michel and Omer Levy and Graham Neubig},\n  year = {2019},\n  booktitle = {NeurIPS 2019},\n  url = {https://arxiv.org/abs/1905.10650},\n}\n\n@inproceedings{dong2019hawq,\n  title = {{HAWQ}: {Hessian} AWare Quantization of Neural Networks with Mixed-Precision},\n  author = {Zhen Dong and Zhewei Yao and Amir Gholami and Michael W. Mahoney and Kurt Keutzer},\n  year = {2019},\n  booktitle = {ICCV 2019},\n  url = {https://arxiv.org/abs/1905.03696},\n}\n\n@inproceedings{dong2020hawqv2,\n  title = {{HAWQ-V2}: {Hessian} Aware trace-Weighted Quantization of Neural Networks},\n  author = {Zhen Dong and Zhewei Yao and Yaohui Cai and Daiyaan Arfeen and Amir Gholami and Michael W. Mahoney and Kurt Keutzer},\n  year = {2020},\n  booktitle = {NeurIPS 2020},\n  url = {https://arxiv.org/abs/1911.03852},\n}\n\n@inproceedings{wang2019haq,\n  title = {{HAQ}: Hardware-Aware Automated Quantization with Mixed Precision},\n  author = {Kuan Wang and Zhijian Liu and Yujun Lin and Ji Lin and Song Han},\n  year = {2019},\n  booktitle = {CVPR 2019},\n  url = {https://arxiv.org/abs/1811.08886},\n}\n\n@inproceedings{su2025rotatekv,\n  title = {{RotateKV}: Accurate and Robust 2-Bit {KV} Cache Quantization for {LLMs} via Outlier-Aware Adaptive Rotations},\n  author = {Zunhai Su and Zhe Chen and Wang Shen and Hanyu Wei and Linge Li and Huangqi Yu and Kehong Yuan},\n  year = {2025},\n  booktitle = {IJCAI 2025},\n  url = {https://arxiv.org/abs/2501.16383},\n}\n\n@inproceedings{sharma2025minikv,\n  title = {{MiniKV}: Pushing the Limits of 2-Bit {KV} Cache via Compression and System Co-Design for Efficient Long Context Inference},\n  author = {Akshat Sharma and Hangliang Ding and Jianping Li and Neel Dani and Minjia Zhang},\n  year = {2025},\n  booktitle = {Findings of ACL 2025},\n  url = {https://arxiv.org/abs/2411.18077},\n}\n\n@inproceedings{shutova2025aquakv,\n  title = {Cache Me If You Must: Adaptive Key-Value Quantization for Large Language Models},\n  author = {Alina Shutova and Vladimir Malinovskii and Vage Egiazarian and Denis Kuznedelev and Denis Mazur and Nikita Surkov and Ivan Ermakov and Dan Alistarh},\n  year = {2025},\n  booktitle = {ICML 2025},\n  url = {https://arxiv.org/abs/2501.19392},\n}\n\n@misc{liu2025pmkvq,\n  title = {{PM-KVQ}: Progressive Mixed-precision {KV} Cache Quantization for Long-CoT {LLMs}},\n  author = {Tengxuan Liu and Shiyao Li and Jiayi Yang and Tianchen Zhao and Feng Zhou and Xiaohui Song and Guohao Dai and Shengen Yan and Huazhong Yang and Yu Wang},\n  year = {2025},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2505.18610},\n  eprint = {2505.18610},\n  archivePrefix = {arXiv},\n}\n\n@misc{xia2025kitty,\n  title = {{Kitty}: Accurate and Efficient 2-bit {KV} Cache Quantization with Dynamic Channel-wise Precision Boost},\n  author = {Haojun Xia and Xiaoxia Wu and Jisen Li and Robert Wu and Junxiong Wang and Jue Wang and Chenxi Li and Aman Singhal and Alay Dilipbhai Shah and Alpay Ariyak and Donglin Zhuang and Zhongzhu Zhou and Ben Athiwaratkun and Zhen Zheng and Shuaiwen Leon Song},\n  year = {2025},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2511.18643},\n  eprint = {2511.18643},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{haeriboroujeni2026dontwaste,\n  title = {Don't Waste Bits! {Adaptive} {KV}-Cache Quantization for Lightweight On-Device {LLMs}},\n  author = {Haeri Boroujeni, Sayed Pedram and Mehrabi, Niloufar and Woods, Patrick and Hillesheim, Gabriel and Razi, Abolfazl},\n  year = {2026},\n  booktitle = {CVPR 2026},\n  url = {https://arxiv.org/abs/2604.04722},\n}\n",
      "numLines": 266,
      "startLine": 1,
      "totalLines": 266
    }
  },
  "sourceToolAssistantUUID": "81e371c5-853f-44e9-89af-bd3bce878813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T09:22:54.246Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BTDTnc8rFsiRzfNT8uwZ8g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6562eda-8642-4534-8023-bfe43cc2595d",
  "isSidechain": false,
  "requestId": "req_011Cb61B81UCdft6midd83iE",
  "type": "assistant",
  "uuid": "81e371c5-853f-44e9-89af-bd3bce878813",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0128YotsKdoP1MSfMvmzkzSm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12719,
      "cache_read_input_tokens": 11841,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12719,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12719
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

_source line 13_

```json
{
  "type": "last-prompt",
  "leafUuid": "d529a322-7cf7-49ad-9201-b468d42058f7",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Add three methods to related work section",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2"
}
```

---

### Assistant

_source line 15 · 2026-05-16T09:23:05.129Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of the current state. Let me check if QAQ, AQLM, or QuIP# entries already exist in the bib file.

From my reading:
- QAQ: Not in bib
- AQLM: Not in bib
- QuIP#: Not in bib
- KVTuner: Already in bib as `li2025kvtuner`

Now I need to:
1. Add bib entries for QAQ, AQLM, and QuIP#
2. Edit related_work.tex to add discussions of all three methods


3. Place QAQ in the KV Cache Quantization section, AQLM and QuIP# in the Mixed-Precision Quantization section as conceptual parallels, and ensure KVTuner gets proper discussion in the Mixed-Precision Rate-Distortion Allocation paragraph where it's currently only cited.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d529a322-7cf7-49ad-9201-b468d42058f7",
  "isSidechain": false,
  "requestId": "req_011Cb61BRQitNZ5RrSv1r1tM",
  "type": "assistant",
  "uuid": "4a5d9cdc-4519-4203-9438-2cf4aaa4be45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DW6hnrNkEkytUdH1Px2E9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6809,
      "cache_read_input_tokens": 24560,
      "output_tokens": 1623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1623,
          "cache_read_input_tokens": 24560,
          "cache_creation_input_tokens": 6809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6809
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

_source line 16 · 2026-05-16T09:23:05.133Z_

Now I'll add the bib entries and update the related work text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a5d9cdc-4519-4203-9438-2cf4aaa4be45",
  "isSidechain": false,
  "requestId": "req_011Cb61BRQitNZ5RrSv1r1tM",
  "type": "assistant",
  "uuid": "db143d7c-a00b-4116-b51c-f1ea0dff5707",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DW6hnrNkEkytUdH1Px2E9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6809,
      "cache_read_input_tokens": 24560,
      "output_tokens": 1623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1623,
          "cache_read_input_tokens": 24560,
          "cache_creation_input_tokens": 6809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6809
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

_source line 17 · 2026-05-16T09:23:16.124Z_

<details open><summary>🔧 Tool call — Edit · `toolu_018t1gAW3YheYPrtk8aQDsji`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib",
  "old_string": "@inproceedings{haeriboroujeni2026dontwaste,\n  title = {Don't Waste Bits! {Adaptive} {KV}-Cache Quantization for Lightweight On-Device {LLMs}},\n  author = {Haeri Boroujeni, Sayed Pedram and Mehrabi, Niloufar and Woods, Patrick and Hillesheim, Gabriel and Razi, Abolfazl},\n  year = {2026},\n  booktitle = {CVPR 2026},\n  url = {https://arxiv.org/abs/2604.04722},\n}",
  "new_string": "@inproceedings{haeriboroujeni2026dontwaste,\n  title = {Don't Waste Bits! {Adaptive} {KV}-Cache Quantization for Lightweight On-Device {LLMs}},\n  author = {Haeri Boroujeni, Sayed Pedram and Mehrabi, Niloufar and Woods, Patrick and Hillesheim, Gabriel and Razi, Abolfazl},\n  year = {2026},\n  booktitle = {CVPR 2026},\n  url = {https://arxiv.org/abs/2604.04722},\n}\n\n@misc{dong2024qaq,\n  title = {{QAQ}: Quality Adaptive Quantization for {LLM} {KV} Cache},\n  author = {Shichen Dong and Wen Cheng and Jiayu Qin and Wei Wang},\n  year = {2024},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2403.04643},\n  eprint = {2403.04643},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{egiazarian2024aqlm,\n  title = {{AQLM}: Extreme Compression of Large Language Models via Additive Quantization},\n  author = {Vage Egiazarian and Andrei Panferov and Denis Kuznedelev and Elias Frantar and Artem Babenko and Dan Alistarh},\n  year = {2024},\n  booktitle = {ICML 2024},\n  url = {https://arxiv.org/abs/2401.06118},\n}\n\n@inproceedings{tseng2024quipsharp,\n  title = {{QuIP\\#}: Even Better {LLM} Quantization with {Hadamard} Incoherence and Lattice Codebooks},\n  author = {Albert Tseng and Jerry Chee and Qingyao Sun and Volodymyr Kuleshov and Christopher De Sa},\n  year = {2024},\n  booktitle = {ICML 2024},\n  url = {https://arxiv.org/abs/2402.04396},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db143d7c-a00b-4116-b51c-f1ea0dff5707",
  "isSidechain": false,
  "requestId": "req_011Cb61BRQitNZ5RrSv1r1tM",
  "type": "assistant",
  "uuid": "38fbf750-af5f-413f-8c94-4485c977507b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DW6hnrNkEkytUdH1Px2E9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6809,
      "cache_read_input_tokens": 24560,
      "output_tokens": 1623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1623,
          "cache_read_input_tokens": 24560,
          "cache_creation_input_tokens": 6809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6809
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

_source line 18 · 2026-05-16T09:23:24.180Z_

<details><summary>↩ Tool result · `toolu_01FQ17UJQmQj75iphPsfwQkw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6d384ca-8609-44ca-bd3b-b5807d38c743",
  "isSidechain": false,
  "promptId": "57178dec-a181-4689-b8dc-6bbe16ba62d5",
  "type": "user",
  "uuid": "e112260d-b5f4-44bd-8a87-8c51ec55fdf0",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex",
    "oldString": "Our per-head bit-width allocation is orthogonal to per-channel quantization schemes such as KIVI: KIVI determines \\emph{how} each head is quantized (asymmetric per-channel scaling), while our method determines \\emph{at what precision} (bit-width selection across heads).\nThe two can be composed, though the per-channel method dominates when available (\\S\\ref{sec:main_results}); per-head allocation provides independent value in symmetric-only environments where per-channel asymmetric quantization is unavailable.",
    "newString": "Our per-head bit-width allocation is orthogonal to per-channel quantization schemes such as KIVI: KIVI determines \\emph{how} each head is quantized (asymmetric per-channel scaling), while our method determines \\emph{at what precision} (bit-width selection across heads).\nThe two can be composed, though the per-channel method dominates when available (\\S\\ref{sec:main_results}); per-head allocation provides independent value in symmetric-only environments where per-channel asymmetric quantization is unavailable.\nQAQ~\\cite{dong2024qaq} also pursues mixed-precision KV cache but selects precision dynamically at inference time using attention scores; in contrast, our allocation is determined offline via one-shot profiling and enforces a cardinality constraint that prevents compounding---a failure mode that any unconstrained adaptive scheme remains susceptible to.",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{KV Cache Quantization.}\nUniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\\cite{lin2024qserve}, salient-token identification~\\cite{he2024zipcache}, low-rank plus sparse correction~\\cite{kang2024gear}, sliding-window adaptation~\\cite{duanmu2024skvq}, rotation-based outlier smoothing for robust 2-bit~\\cite{su2025rotatekv}, 2-bit with adaptive token retention~\\cite{sharma2025minikv}, and adapter-based inter-layer prediction at 2--2.5 bits~\\cite{shutova2025aquakv}.\nWe extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\\{2,4,8,16\\}$.\nOur per-head bit-width allocation is orthogonal to per-channel quantization schemes such as KIVI: KIVI determines \\emph{how} each head is quantized (asymmetric per-channel scaling), while our method determines \\emph{at what precision} (bit-width selection across heads).\nThe two can be composed, though the per-channel method dominates when available (\\S\\ref{sec:main_results}); per-head allocation provides independent value in symmetric-only environments where per-channel asymmetric quantization is unavailable.\n\n\\paragraph{KV Cache Eviction.}\nComplementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\\cite{zhang2023h2o}, per-head important tokens~\\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\\cite{liu2024scissorhands}, attention sinks~\\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\\cite{yang2024pyramidinfer}.\nRecent per-head eviction methods allocate non-uniform budgets across heads based on retrieval-vs-reasoning importance~\\cite{fu2025headkv} or adaptive optimization extending SnapKV/PyramidKV~\\cite{feng2025adakv}, confirming that head-level heterogeneity is exploitable for eviction; our work shows it is equally exploitable for quantization.\n\n\n\\paragraph{Mixed-Precision Quantization (Weights).}\nMixed-precision allocation has a long history at the weight level.\nHAWQ~\\cite{dong2019hawq} and HAWQ-V2~\\cite{dong2020hawqv2} use second-order (Hessian-based) sensitivity to assign per-layer bit-widths, with V2 introducing block-wise trace-weighted scoring and Pareto-frontier selection; HAQ~\\cite{wang2019haq} learns an allocation by reinforcement learning under hardware-aware latency/energy constraints.\nThese methods operate on weights, where per-layer distortions are approximately additive and sensitivity varies smoothly across layers.\nKV cache quantization presents a qualitatively different challenge: 2-bit head distortions compound super-additively through the residual stream (\\S\\ref{sec:compounding}), a phenomenon absent in weight quantization where each layer's parameters are independently quantized.\nOur primary contribution is not the allocation algorithm itself---any MCKP or greedy solver suffices---but the diagnosis and fix of this compounding effect via cardinality constraints, and the characterization of when non-uniform allocation is beneficial (\\S\\ref{sec:heterogeneity}).\n\n\\paragraph{Mixed-Precision Rate-Distortion Allocation.}\nRateQuant~\\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\\{2,\\ldots,6\\}$ via the polymatroid structure, which relies on the assumption that per-head distortions decompose additively into the global objective---valid when adjacent bit-widths differ by a single bit so that quantization noise stays in the small-perturbation regime.\nOn hardware-aligned $\\{2,4,8,16\\}$, the 4$\\times$ gap between 2-bit and 4-bit drives 2-bit distortion to compound super-additively, breaking the polymatroid structure and the additivity assumption with it.\nConcretely, running RateQuant's greedy algorithm (Algorithm~1) directly on $\\{2,4,8,16\\}$ yields 32.45 PPL on Qwen2.5-7B at $4\\times$ compression---catastrophically worse than uniform 4-bit (15.45)---whereas our cardinality constraint on simultaneously active 2-bit heads recovers 10.91 PPL at the same average bit-width.\nThe constraint is the minimal fix that restores the additive regime in which RateQuant's polymatroid argument applies.\nRelated mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\\cite{xia2025kitty}, token-level via a learned on-device controller~\\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\\cite{lei2026arkv}---at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.\n\n\\paragraph{Attention Head Analysis.}\nPrior work studies head redundancy and pruning~\\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.\nOur analysis asks a different question: which heads are sensitive to \\emph{quantization}, and how heterogeneous that sensitivity is across architectures---a property that determines whether non-uniform allocation is beneficial (\\S\\ref{sec:heterogeneity}).",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 6,
        "newStart": 5,
        "newLines": 7,
        "lines": [
          " We extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\\{2,4,8,16\\}$.",
          " Our per-head bit-width allocation is orthogonal to per-channel quantization schemes such as KIVI: KIVI determines \\emph{how} each head is quantized (asymmetric per-channel scaling), while our method determines \\emph{at what precision} (bit-width selection across heads).",
          " The two can be composed, though the per-channel method dominates when available (\\S\\ref{sec:main_results}); per-head allocation provides independent value in symmetric-only environments where per-channel asymmetric quantization is unavailable.",
          "+QAQ~\\cite{dong2024qaq} also pursues mixed-precision KV cache but selects precision dynamically at inference time using attention scores; in contrast, our allocation is determined offline via one-shot profiling and enforces a cardinality constraint that prevents compounding---a failure mode that any unconstrained adaptive scheme remains susceptible to.",
          " ",
          " \\paragraph{KV Cache Eviction.}",
          " Complementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\\cite{zhang2023h2o}, per-head important tokens~\\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\\cite{liu2024scissorhands}, attention sinks~\\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\\cite{yang2024pyramidinfer}."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "b6d384ca-8609-44ca-bd3b-b5807d38c743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T09:23:16.150Z_

<details><summary>↩ Tool result · `toolu_018t1gAW3YheYPrtk8aQDsji`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38fbf750-af5f-413f-8c94-4485c977507b",
  "isSidechain": false,
  "promptId": "57178dec-a181-4689-b8dc-6bbe16ba62d5",
  "type": "user",
  "uuid": "65febb6e-b6e1-4575-b77f-450745e12fb8",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/references.bib",
    "oldString": "@inproceedings{haeriboroujeni2026dontwaste,\n  title = {Don't Waste Bits! {Adaptive} {KV}-Cache Quantization for Lightweight On-Device {LLMs}},\n  author = {Haeri Boroujeni, Sayed Pedram and Mehrabi, Niloufar and Woods, Patrick and Hillesheim, Gabriel and Razi, Abolfazl},\n  year = {2026},\n  booktitle = {CVPR 2026},\n  url = {https://arxiv.org/abs/2604.04722},\n}",
    "newString": "@inproceedings{haeriboroujeni2026dontwaste,\n  title = {Don't Waste Bits! {Adaptive} {KV}-Cache Quantization for Lightweight On-Device {LLMs}},\n  author = {Haeri Boroujeni, Sayed Pedram and Mehrabi, Niloufar and Woods, Patrick and Hillesheim, Gabriel and Razi, Abolfazl},\n  year = {2026},\n  booktitle = {CVPR 2026},\n  url = {https://arxiv.org/abs/2604.04722},\n}\n\n@misc{dong2024qaq,\n  title = {{QAQ}: Quality Adaptive Quantization for {LLM} {KV} Cache},\n  author = {Shichen Dong and Wen Cheng and Jiayu Qin and Wei Wang},\n  year = {2024},\n  note = {arXiv preprint},\n  url = {https://arxiv.org/abs/2403.04643},\n  eprint = {2403.04643},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{egiazarian2024aqlm,\n  title = {{AQLM}: Extreme Compression of Large Language Models via Additive Quantization},\n  author = {Vage Egiazarian and Andrei Panferov and Denis Kuznedelev and Elias Frantar and Artem Babenko and Dan Alistarh},\n  year = {2024},\n  booktitle = {ICML 2024},\n  url = {https://arxiv.org/abs/2401.06118},\n}\n\n@inproceedings{tseng2024quipsharp,\n  title = {{QuIP\\#}: Even Better {LLM} Quantization with {Hadamard} Incoherence and Lattice Codebooks},\n  author = {Albert Tseng and Jerry Chee and Qingyao Sun and Volodymyr Kuleshov and Christopher De Sa},\n  year = {2024},\n  booktitle = {ICML 2024},\n  url = {https://arxiv.org/abs/2402.04396},\n}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 263,
        "oldLines": 3,
        "newStart": 263,
        "newLines": 29,
        "lines": [
          "   booktitle = {CVPR 2026},",
          "   url = {https://arxiv.org/abs/2604.04722},",
          " }",
          "+",
          "+@misc{dong2024qaq,",
          "+  title = {{QAQ}: Quality Adaptive Quantization for {LLM} {KV} Cache},",
          "+  author = {Shichen Dong and Wen Cheng and Jiayu Qin and Wei Wang},",
          "+  year = {2024},",
          "+  note = {arXiv preprint},",
          "+  url = {https://arxiv.org/abs/2403.04643},",
          "+  eprint = {2403.04643},",
          "+  archivePrefix = {arXiv},",
          "+}",
          "+",
          "+@inproceedings{egiazarian2024aqlm,",
          "+  title = {{AQLM}: Extreme Compression of Large Language Models via Additive Quantization},",
          "+  author = {Vage Egiazarian and Andrei Panferov and Denis Kuznedelev and Elias Frantar and Artem Babenko and Dan Alistarh},",
          "+  year = {2024},",
          "+  booktitle = {ICML 2024},",
          "+  url = {https://arxiv.org/abs/2401.06118},",
          "+}",
          "+",
          "+@inproceedings{tseng2024quipsharp,",
          "+  title = {{QuIP\\#}: Even Better {LLM} Quantization with {Hadamard} Incoherence and Lattice Codebooks},",
          "+  author = {Albert Tseng and Jerry Chee and Qingyao Sun and Volodymyr Kuleshov and Christopher De Sa},",
          "+  year = {2024},",
          "+  booktitle = {ICML 2024},",
          "+  url = {https://arxiv.org/abs/2402.04396},",
          "+}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "38fbf750-af5f-413f-8c94-4485c977507b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-16T09:23:24.163Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01FQ17UJQmQj75iphPsfwQkw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex",
  "old_string": "Our per-head bit-width allocation is orthogonal to per-channel quantization schemes such as KIVI: KIVI determines \\emph{how} each head is quantized (asymmetric per-channel scaling), while our method determines \\emph{at what precision} (bit-width selection across heads).\nThe two can be composed, though the per-channel method dominates when available (\\S\\ref{sec:main_results}); per-head allocation provides independent value in symmetric-only environments where per-channel asymmetric quantization is unavailable.",
  "new_string": "Our per-head bit-width allocation is orthogonal to per-channel quantization schemes such as KIVI: KIVI determines \\emph{how} each head is quantized (asymmetric per-channel scaling), while our method determines \\emph{at what precision} (bit-width selection across heads).\nThe two can be composed, though the per-channel method dominates when available (\\S\\ref{sec:main_results}); per-head allocation provides independent value in symmetric-only environments where per-channel asymmetric quantization is unavailable.\nQAQ~\\cite{dong2024qaq} also pursues mixed-precision KV cache but selects precision dynamically at inference time using attention scores; in contrast, our allocation is determined offline via one-shot profiling and enforces a cardinality constraint that prevents compounding---a failure mode that any unconstrained adaptive scheme remains susceptible to."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65febb6e-b6e1-4575-b77f-450745e12fb8",
  "isSidechain": false,
  "requestId": "req_011Cb61BRQitNZ5RrSv1r1tM",
  "type": "assistant",
  "uuid": "b6d384ca-8609-44ca-bd3b-b5807d38c743",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DW6hnrNkEkytUdH1Px2E9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6809,
      "cache_read_input_tokens": 24560,
      "output_tokens": 1623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6809,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1623,
          "cache_read_input_tokens": 24560,
          "cache_creation_input_tokens": 6809,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6809
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

_source line 21 · 2026-05-16T09:23:34.913Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01RR8yn1VXWd7dN4AGoGsSRe`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex",
  "old_string": "KV cache quantization presents a qualitatively different challenge: 2-bit head distortions compound super-additively through the residual stream (\\S\\ref{sec:compounding}), a phenomenon absent in weight quantization where each layer's parameters are independently quantized.",
  "new_string": "KV cache quantization presents a qualitatively different challenge: 2-bit head distortions compound super-additively through the residual stream (\\S\\ref{sec:compounding}), a phenomenon absent in weight quantization where each layer's parameters are independently quantized.\nNotably, AQLM~\\cite{egiazarian2024aqlm} and QuIP\\#~\\cite{tseng2024quipsharp} have observed non-additive error behaviour in extreme weight quantization when codebook interactions amplify distortion beyond per-parameter predictions; we independently identify an analogous phenomenon in per-head KV cache allocation, where co-activating multiple 2-bit heads triggers super-additive degradation through the residual stream."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e112260d-b5f4-44bd-8a87-8c51ec55fdf0",
  "isSidechain": false,
  "requestId": "req_011Cb61DdBTGU9sBLmHdvNhR",
  "type": "assistant",
  "uuid": "f8e82c60-9ee8-4fe1-9bc1-6938a42a4fca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167v9Lx1m8P1cndgU6D6gk5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 31369,
      "output_tokens": 954,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 954,
          "cache_read_input_tokens": 31369,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1801
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

_source line 22 · 2026-05-16T09:23:34.928Z_

<details><summary>↩ Tool result · `toolu_01RR8yn1VXWd7dN4AGoGsSRe`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8e82c60-9ee8-4fe1-9bc1-6938a42a4fca",
  "isSidechain": false,
  "promptId": "57178dec-a181-4689-b8dc-6bbe16ba62d5",
  "type": "user",
  "uuid": "8d5f6857-e942-4b93-b5cc-31900f8b9d8d",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex",
    "oldString": "KV cache quantization presents a qualitatively different challenge: 2-bit head distortions compound super-additively through the residual stream (\\S\\ref{sec:compounding}), a phenomenon absent in weight quantization where each layer's parameters are independently quantized.",
    "newString": "KV cache quantization presents a qualitatively different challenge: 2-bit head distortions compound super-additively through the residual stream (\\S\\ref{sec:compounding}), a phenomenon absent in weight quantization where each layer's parameters are independently quantized.\nNotably, AQLM~\\cite{egiazarian2024aqlm} and QuIP\\#~\\cite{tseng2024quipsharp} have observed non-additive error behaviour in extreme weight quantization when codebook interactions amplify distortion beyond per-parameter predictions; we independently identify an analogous phenomenon in per-head KV cache allocation, where co-activating multiple 2-bit heads triggers super-additive degradation through the residual stream.",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{KV Cache Quantization.}\nUniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\\cite{lin2024qserve}, salient-token identification~\\cite{he2024zipcache}, low-rank plus sparse correction~\\cite{kang2024gear}, sliding-window adaptation~\\cite{duanmu2024skvq}, rotation-based outlier smoothing for robust 2-bit~\\cite{su2025rotatekv}, 2-bit with adaptive token retention~\\cite{sharma2025minikv}, and adapter-based inter-layer prediction at 2--2.5 bits~\\cite{shutova2025aquakv}.\nWe extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\\{2,4,8,16\\}$.\nOur per-head bit-width allocation is orthogonal to per-channel quantization schemes such as KIVI: KIVI determines \\emph{how} each head is quantized (asymmetric per-channel scaling), while our method determines \\emph{at what precision} (bit-width selection across heads).\nThe two can be composed, though the per-channel method dominates when available (\\S\\ref{sec:main_results}); per-head allocation provides independent value in symmetric-only environments where per-channel asymmetric quantization is unavailable.\nQAQ~\\cite{dong2024qaq} also pursues mixed-precision KV cache but selects precision dynamically at inference time using attention scores; in contrast, our allocation is determined offline via one-shot profiling and enforces a cardinality constraint that prevents compounding---a failure mode that any unconstrained adaptive scheme remains susceptible to.\n\n\\paragraph{KV Cache Eviction.}\nComplementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\\cite{zhang2023h2o}, per-head important tokens~\\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\\cite{liu2024scissorhands}, attention sinks~\\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\\cite{yang2024pyramidinfer}.\nRecent per-head eviction methods allocate non-uniform budgets across heads based on retrieval-vs-reasoning importance~\\cite{fu2025headkv} or adaptive optimization extending SnapKV/PyramidKV~\\cite{feng2025adakv}, confirming that head-level heterogeneity is exploitable for eviction; our work shows it is equally exploitable for quantization.\n\n\n\\paragraph{Mixed-Precision Quantization (Weights).}\nMixed-precision allocation has a long history at the weight level.\nHAWQ~\\cite{dong2019hawq} and HAWQ-V2~\\cite{dong2020hawqv2} use second-order (Hessian-based) sensitivity to assign per-layer bit-widths, with V2 introducing block-wise trace-weighted scoring and Pareto-frontier selection; HAQ~\\cite{wang2019haq} learns an allocation by reinforcement learning under hardware-aware latency/energy constraints.\nThese methods operate on weights, where per-layer distortions are approximately additive and sensitivity varies smoothly across layers.\nKV cache quantization presents a qualitatively different challenge: 2-bit head distortions compound super-additively through the residual stream (\\S\\ref{sec:compounding}), a phenomenon absent in weight quantization where each layer's parameters are independently quantized.\nOur primary contribution is not the allocation algorithm itself---any MCKP or greedy solver suffices---but the diagnosis and fix of this compounding effect via cardinality constraints, and the characterization of when non-uniform allocation is beneficial (\\S\\ref{sec:heterogeneity}).\n\n\\paragraph{Mixed-Precision Rate-Distortion Allocation.}\nRateQuant~\\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\\{2,\\ldots,6\\}$ via the polymatroid structure, which relies on the assumption that per-head distortions decompose additively into the global objective---valid when adjacent bit-widths differ by a single bit so that quantization noise stays in the small-perturbation regime.\nOn hardware-aligned $\\{2,4,8,16\\}$, the 4$\\times$ gap between 2-bit and 4-bit drives 2-bit distortion to compound super-additively, breaking the polymatroid structure and the additivity assumption with it.\nConcretely, running RateQuant's greedy algorithm (Algorithm~1) directly on $\\{2,4,8,16\\}$ yields 32.45 PPL on Qwen2.5-7B at $4\\times$ compression---catastrophically worse than uniform 4-bit (15.45)---whereas our cardinality constraint on simultaneously active 2-bit heads recovers 10.91 PPL at the same average bit-width.\nThe constraint is the minimal fix that restores the additive regime in which RateQuant's polymatroid argument applies.\nRelated mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\\cite{xia2025kitty}, token-level via a learned on-device controller~\\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\\cite{lei2026arkv}---at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.\n\n\\paragraph{Attention Head Analysis.}\nPrior work studies head redundancy and pruning~\\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.\nOur analysis asks a different question: which heads are sensitive to \\emph{quantization}, and how heterogeneous that sensitivity is across architectures---a property that determines whether non-uniform allocation is beneficial (\\S\\ref{sec:heterogeneity}).",
    "structuredPatch": [
      {
        "oldStart": 17,
        "oldLines": 6,
        "newStart": 17,
        "newLines": 7,
        "lines": [
          " HAWQ~\\cite{dong2019hawq} and HAWQ-V2~\\cite{dong2020hawqv2} use second-order (Hessian-based) sensitivity to assign per-layer bit-widths, with V2 introducing block-wise trace-weighted scoring and Pareto-frontier selection; HAQ~\\cite{wang2019haq} learns an allocation by reinforcement learning under hardware-aware latency/energy constraints.",
          " These methods operate on weights, where per-layer distortions are approximately additive and sensitivity varies smoothly across layers.",
          " KV cache quantization presents a qualitatively different challenge: 2-bit head distortions compound super-additively through the residual stream (\\S\\ref{sec:compounding}), a phenomenon absent in weight quantization where each layer's parameters are independently quantized.",
          "+Notably, AQLM~\\cite{egiazarian2024aqlm} and QuIP\\#~\\cite{tseng2024quipsharp} have observed non-additive error behaviour in extreme weight quantization when codebook interactions amplify distortion beyond per-parameter predictions; we independently identify an analogous phenomenon in per-head KV cache allocation, where co-activating multiple 2-bit heads triggers super-additive degradation through the residual stream.",
          " Our primary contribution is not the allocation algorithm itself---any MCKP or greedy solver suffices---but the diagnosis and fix of this compounding effect via cardinality constraints, and the characterization of when non-uniform allocation is beneficial (\\S\\ref{sec:heterogeneity}).",
          " ",
          " \\paragraph{Mixed-Precision Rate-Distortion Allocation.}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "f8e82c60-9ee8-4fe1-9bc1-6938a42a4fca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T09:23:42.450Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01WZTeU3fD1PFLbaWM8CrCeB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex",
  "old_string": "Related mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\\cite{xia2025kitty}, token-level via a learned on-device controller~\\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\\cite{lei2026arkv}---at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.",
  "new_string": "Related mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\\cite{xia2025kitty}, token-level via a learned on-device controller~\\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\\cite{lei2026arkv}---at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.\nKVTuner~\\cite{li2025kvtuner} assigns mixed precision at the layer level (all heads within a layer share a single bit-width); our head-level granularity exposes intra-layer heterogeneity at the cost of a combinatorially larger search space, which the cardinality constraint renders tractable."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d5f6857-e942-4b93-b5cc-31900f8b9d8d",
  "isSidechain": false,
  "requestId": "req_011Cb61DdBTGU9sBLmHdvNhR",
  "type": "assistant",
  "uuid": "9deaf370-ee1c-45b5-a105-d66dfcd670f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167v9Lx1m8P1cndgU6D6gk5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1801,
      "cache_read_input_tokens": 31369,
      "output_tokens": 954,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1801,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 954,
          "cache_read_input_tokens": 31369,
          "cache_creation_input_tokens": 1801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1801
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

_source line 24 · 2026-05-16T09:23:42.472Z_

<details><summary>↩ Tool result · `toolu_01WZTeU3fD1PFLbaWM8CrCeB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9deaf370-ee1c-45b5-a105-d66dfcd670f3",
  "isSidechain": false,
  "promptId": "57178dec-a181-4689-b8dc-6bbe16ba62d5",
  "type": "user",
  "uuid": "971bb3f5-653d-41fb-ab28-c137aaa5bcd3",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex",
    "oldString": "Related mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\\cite{xia2025kitty}, token-level via a learned on-device controller~\\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\\cite{lei2026arkv}---at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.",
    "newString": "Related mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\\cite{xia2025kitty}, token-level via a learned on-device controller~\\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\\cite{lei2026arkv}---at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.\nKVTuner~\\cite{li2025kvtuner} assigns mixed precision at the layer level (all heads within a layer share a single bit-width); our head-level granularity exposes intra-layer heterogeneity at the cost of a combinatorially larger search space, which the cardinality constraint renders tractable.",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{KV Cache Quantization.}\nUniform-precision methods quantize the KV cache at a single bit-width across all heads, using techniques such as asymmetric per-channel/per-token schemes~\\cite{liu2024kivi,hooper2024kvquant}, quantization--serving co-design~\\cite{lin2024qserve}, salient-token identification~\\cite{he2024zipcache}, low-rank plus sparse correction~\\cite{kang2024gear}, sliding-window adaptation~\\cite{duanmu2024skvq}, rotation-based outlier smoothing for robust 2-bit~\\cite{su2025rotatekv}, 2-bit with adaptive token retention~\\cite{sharma2025minikv}, and adapter-based inter-layer prediction at 2--2.5 bits~\\cite{shutova2025aquakv}.\nWe extend the design space to per-head non-uniform allocation over hardware-aligned bit-widths $\\{2,4,8,16\\}$.\nOur per-head bit-width allocation is orthogonal to per-channel quantization schemes such as KIVI: KIVI determines \\emph{how} each head is quantized (asymmetric per-channel scaling), while our method determines \\emph{at what precision} (bit-width selection across heads).\nThe two can be composed, though the per-channel method dominates when available (\\S\\ref{sec:main_results}); per-head allocation provides independent value in symmetric-only environments where per-channel asymmetric quantization is unavailable.\nQAQ~\\cite{dong2024qaq} also pursues mixed-precision KV cache but selects precision dynamically at inference time using attention scores; in contrast, our allocation is determined offline via one-shot profiling and enforces a cardinality constraint that prevents compounding---a failure mode that any unconstrained adaptive scheme remains susceptible to.\n\n\\paragraph{KV Cache Eviction.}\nComplementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\\cite{zhang2023h2o}, per-head important tokens~\\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\\cite{liu2024scissorhands}, attention sinks~\\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\\cite{yang2024pyramidinfer}.\nRecent per-head eviction methods allocate non-uniform budgets across heads based on retrieval-vs-reasoning importance~\\cite{fu2025headkv} or adaptive optimization extending SnapKV/PyramidKV~\\cite{feng2025adakv}, confirming that head-level heterogeneity is exploitable for eviction; our work shows it is equally exploitable for quantization.\n\n\n\\paragraph{Mixed-Precision Quantization (Weights).}\nMixed-precision allocation has a long history at the weight level.\nHAWQ~\\cite{dong2019hawq} and HAWQ-V2~\\cite{dong2020hawqv2} use second-order (Hessian-based) sensitivity to assign per-layer bit-widths, with V2 introducing block-wise trace-weighted scoring and Pareto-frontier selection; HAQ~\\cite{wang2019haq} learns an allocation by reinforcement learning under hardware-aware latency/energy constraints.\nThese methods operate on weights, where per-layer distortions are approximately additive and sensitivity varies smoothly across layers.\nKV cache quantization presents a qualitatively different challenge: 2-bit head distortions compound super-additively through the residual stream (\\S\\ref{sec:compounding}), a phenomenon absent in weight quantization where each layer's parameters are independently quantized.\nNotably, AQLM~\\cite{egiazarian2024aqlm} and QuIP\\#~\\cite{tseng2024quipsharp} have observed non-additive error behaviour in extreme weight quantization when codebook interactions amplify distortion beyond per-parameter predictions; we independently identify an analogous phenomenon in per-head KV cache allocation, where co-activating multiple 2-bit heads triggers super-additive degradation through the residual stream.\nOur primary contribution is not the allocation algorithm itself---any MCKP or greedy solver suffices---but the diagnosis and fix of this compounding effect via cardinality constraints, and the characterization of when non-uniform allocation is beneficial (\\S\\ref{sec:heterogeneity}).\n\n\\paragraph{Mixed-Precision Rate-Distortion Allocation.}\nRateQuant~\\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\\{2,\\ldots,6\\}$ via the polymatroid structure, which relies on the assumption that per-head distortions decompose additively into the global objective---valid when adjacent bit-widths differ by a single bit so that quantization noise stays in the small-perturbation regime.\nOn hardware-aligned $\\{2,4,8,16\\}$, the 4$\\times$ gap between 2-bit and 4-bit drives 2-bit distortion to compound super-additively, breaking the polymatroid structure and the additivity assumption with it.\nConcretely, running RateQuant's greedy algorithm (Algorithm~1) directly on $\\{2,4,8,16\\}$ yields 32.45 PPL on Qwen2.5-7B at $4\\times$ compression---catastrophically worse than uniform 4-bit (15.45)---whereas our cardinality constraint on simultaneously active 2-bit heads recovers 10.91 PPL at the same average bit-width.\nThe constraint is the minimal fix that restores the additive regime in which RateQuant's polymatroid argument applies.\nRelated mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\\cite{xia2025kitty}, token-level via a learned on-device controller~\\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\\cite{lei2026arkv}---at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.\n\n\\paragraph{Attention Head Analysis.}\nPrior work studies head redundancy and pruning~\\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely.\nOur analysis asks a different question: which heads are sensitive to \\emph{quantization}, and how heterogeneous that sensitivity is across architectures---a property that determines whether non-uniform allocation is beneficial (\\S\\ref{sec:heterogeneity}).",
    "structuredPatch": [
      {
        "oldStart": 26,
        "oldLines": 6,
        "newStart": 26,
        "newLines": 7,
        "lines": [
          " Concretely, running RateQuant's greedy algorithm (Algorithm~1) directly on $\\{2,4,8,16\\}$ yields 32.45 PPL on Qwen2.5-7B at $4\\times$ compression---catastrophically worse than uniform 4-bit (15.45)---whereas our cardinality constraint on simultaneously active 2-bit heads recovers 10.91 PPL at the same average bit-width.",
          " The constraint is the minimal fix that restores the additive regime in which RateQuant's polymatroid argument applies.",
          " Related mixed-precision KV-cache work operates at coarser granularity---layer-level via gradient-based sensitivity~\\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\\cite{li2025kvtuner}, block-level via progressive decoding-step quantization for long-CoT reasoning~\\cite{liu2025pmkvq}, channel-level via dynamic precision boost on sensitive Key channels~\\cite{xia2025kitty}, token-level via a learned on-device controller~\\cite{haeriboroujeni2026dontwaste}, memory-budget-level~\\cite{lei2026arkv}---at the weight level~\\cite{kim2024squeezellm}, or dynamically at inference time~\\cite{zhang2025mixkvq}; our allocation is static and per-head.",
          "+KVTuner~\\cite{li2025kvtuner} assigns mixed precision at the layer level (all heads within a layer share a single bit-width); our head-level granularity exposes intra-layer heterogeneity at the cost of a combinatorially larger search space, which the cardinality constraint renders tractable.",
          " ",
          " \\paragraph{Attention Head Analysis.}",
          " Prior work studies head redundancy and pruning~\\cite{voita2019analyzing,michel2019sixteen}, focusing on which heads can be removed entirely."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "9deaf370-ee1c-45b5-a105-d66dfcd670f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "leafUuid": "971bb3f5-653d-41fb-ab28-c137aaa5bcd3",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Add three methods to related work section",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2"
}
```

---

### Assistant

_source line 27 · 2026-05-16T09:23:46.495Z_

验证新引用在正文和 bib 中都存在。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "971bb3f5-653d-41fb-ab28-c137aaa5bcd3",
  "isSidechain": false,
  "requestId": "req_011Cb61Eyufjb5oayDf66fa6",
  "type": "assistant",
  "uuid": "b1d2109f-bdd7-4d78-8620-cda726a7d71b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3hEwfFQWq2fS6oASnopmq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1095,
      "cache_read_input_tokens": 33170,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1095,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 33170,
          "cache_creation_input_tokens": 1095,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1095
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

_source line 28 · 2026-05-16T09:23:47.261Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01FByiRRK2kxw5V5wwEtRi7Z`</summary>

```json
{
  "pattern": "dong2024qaq|egiazarian2024aqlm|tseng2024quipsharp|li2025kvtuner",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1d2109f-bdd7-4d78-8620-cda726a7d71b",
  "isSidechain": false,
  "requestId": "req_011Cb61Eyufjb5oayDf66fa6",
  "type": "assistant",
  "uuid": "4f75dad2-411f-4acc-aa16-67ef83ab5cb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q3hEwfFQWq2fS6oASnopmq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1095,
      "cache_read_input_tokens": 33170,
      "output_tokens": 165,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1095,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 165,
          "cache_read_input_tokens": 33170,
          "cache_creation_input_tokens": 1095,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1095
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

_source line 29 · 2026-05-16T09:23:47.280Z_

<details><summary>↩ Tool result · `toolu_01FByiRRK2kxw5V5wwEtRi7Z`</summary>

```text
docs/paper/related_work.tex:8:QAQ~\cite{dong2024qaq} also pursues mixed-precision KV cache but selects precision dynamically at inference time using attention scores; in contrast, our allocation is determined offline via one-shot profiling and enforces a cardinality constraint that prevents compounding---a failure mode that any unconstrained adaptive scheme remains susceptible to.
docs/paper/related_work.tex:20:Notably, AQLM~\cite{egiazarian2024aqlm} and QuIP\#~\cite{tseng2024quipsharp} have observed non-additive error behaviour in extreme weight quantization when codebook interactions amplify distortion beyond per-parameter predictions; we independently identify an analogous phenomenon in per-head KV cache allocation, where co-activating multiple 2-bit heads triggers super-additive degradation through the residual stream.
docs/paper/related_work.tex:28:[Omitted long matching line]
docs/paper/related_work.tex:29:KVTuner~\cite{li2025kvtuner} assigns mixed precision at the layer level (all heads within a layer share a single bit-width); our head-level granularity exposes intra-layer heterogeneity at the cost of a combinatorially larger search space, which the cardinality constraint renders tractable.
docs/paper/main.bbl:115:  Dai}]{li2025kvtuner}
docs/paper/appendix.tex:61:\emph{Layer-level} allocation (KVmix~\cite{li2025kvmix}, KVTuner~\cite{li2025kvtuner}) keeps the search space small ($L$ layers) but forces all heads in a layer to share one bitwidth.
docs/paper/references.bib:167:@inproceedings{li2025kvtuner,
docs/paper/references.bib:267:@misc{dong2024qaq,
docs/paper/references.bib:277:@inproceedings{egiazarian2024aqlm,
docs/paper/references.bib:285:@inproceedings{tseng2024quipsharp,
docs/paper/main.aux:224:\citation{li2025kvtuner}
docs/paper/main.aux:927:\bibcite{li2025kvtuner}{{15}{2025{b}}{{Li et~al.}}{{Li, Shen, Tang, Luo, and Dai}}}
docs/paper/main.aux:1139:\citation{li2025kvtuner}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f75dad2-411f-4acc-aa16-67ef83ab5cb2",
  "isSidechain": false,
  "promptId": "57178dec-a181-4689-b8dc-6bbe16ba62d5",
  "type": "user",
  "uuid": "0b149636-417a-4e4b-9dce-ce989b9489d5",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:8:QAQ~\\cite{dong2024qaq} also pursues mixed-precision KV cache but selects precision dynamically at inference time using attention scores; in contrast, our allocation is determined offline via one-shot profiling and enforces a cardinality constraint that prevents compounding---a failure mode that any unconstrained adaptive scheme remains susceptible to.\ndocs/paper/related_work.tex:20:Notably, AQLM~\\cite{egiazarian2024aqlm} and QuIP\\#~\\cite{tseng2024quipsharp} have observed non-additive error behaviour in extreme weight quantization when codebook interactions amplify distortion beyond per-parameter predictions; we independently identify an analogous phenomenon in per-head KV cache allocation, where co-activating multiple 2-bit heads triggers super-additive degradation through the residual stream.\ndocs/paper/related_work.tex:28:[Omitted long matching line]\ndocs/paper/related_work.tex:29:KVTuner~\\cite{li2025kvtuner} assigns mixed precision at the layer level (all heads within a layer share a single bit-width); our head-level granularity exposes intra-layer heterogeneity at the cost of a combinatorially larger search space, which the cardinality constraint renders tractable.\ndocs/paper/main.bbl:115:  Dai}]{li2025kvtuner}\ndocs/paper/appendix.tex:61:\\emph{Layer-level} allocation (KVmix~\\cite{li2025kvmix}, KVTuner~\\cite{li2025kvtuner}) keeps the search space small ($L$ layers) but forces all heads in a layer to share one bitwidth.\ndocs/paper/references.bib:167:@inproceedings{li2025kvtuner,\ndocs/paper/references.bib:267:@misc{dong2024qaq,\ndocs/paper/references.bib:277:@inproceedings{egiazarian2024aqlm,\ndocs/paper/references.bib:285:@inproceedings{tseng2024quipsharp,\ndocs/paper/main.aux:224:\\citation{li2025kvtuner}\ndocs/paper/main.aux:927:\\bibcite{li2025kvtuner}{{15}{2025{b}}{{Li et~al.}}{{Li, Shen, Tang, Luo, and Dai}}}\ndocs/paper/main.aux:1139:\\citation{li2025kvtuner}",
    "numLines": 13
  },
  "sourceToolAssistantUUID": "4f75dad2-411f-4acc-aa16-67ef83ab5cb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-16T09:23:53.315Z_

全部完成。新增内容：

1. **QAQ** — `related_work.tex` KV Cache Quantization 段落末尾，区分 attention-score-based 动态方法 vs 我们的 offline profiling + cardinality constraint。bib 条目 `dong2024qaq` 已添加。

2. **AQLM/QuIP#** — Mixed-Precision Quantization (Weights) 段落，作为 non-additive error 的 conceptual parallel。bib 条目 `egiazarian2024aqlm` 和 `tseng2024quipsharp` 已添加。

3. **KVTuner** — Mixed-Precision Rate-Distortion Allocation 段落，区分 layer-level vs head-level granularity，cardinality constraint 使更大搜索空间可控。已有 bib 条目 `li2025kvtuner`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b149636-417a-4e4b-9dce-ce989b9489d5",
  "isSidechain": false,
  "requestId": "req_011Cb61FKvS81rSYzdjXXmZk",
  "type": "assistant",
  "uuid": "7841d934-9323-4f00-aa0a-80979af5fbc0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011g6wSH6hWZuYhLabLZmz5x",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 788,
      "cache_read_input_tokens": 34265,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 788,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 242,
          "cache_read_input_tokens": 34265,
          "cache_creation_input_tokens": 788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 788
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

_source line 31_

```json
{
  "type": "last-prompt",
  "leafUuid": "7841d934-9323-4f00-aa0a-80979af5fbc0",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Add three methods to related work section",
  "sessionId": "dc54b085-27d2-470a-bc77-92c047e6b5f2"
}
```

---
