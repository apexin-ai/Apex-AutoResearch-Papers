# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T075006 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/3e227914-44fc-4375-965c-962f04adfef3.jsonl`
- **Structured JSON:** [`0b5caa7b8e151939975b.json`](../../sessions/0b/0b5caa7b8e151939975b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T08:28:06.915Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T08:28:06.915Z",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T075006 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Gradient narrative死掉——exp-002显示variance structure跨benchmark几乎不变（item_id range仅5.7pp），没有knowledge→reasoning的系统性梯度。必须reframe整篇论文。 新angle：MMLU作为\"case study in multi-facet evaluation measurement\"。 三条Primary contributions： (1) model×item interaction量化——42%→61%的inflation效应 + D-study Δ=0.004 out-of-sample验证，这些数字已锁定（来自actual 4-model data），不受exp-002影响； (2) IRT vs G-theory direct comparison——MMLU上3.6-4.4×差异是publishable finding， 但跨benchmark ratio从1.6×到4.1×不等（GSM8K/HellaSwag < 2×），所以\"3-4×\" 只能claim for MMLU，cross-benchmark需说\"benchmark-dependent\"； (3) variance structure benchmark-insensitivity本身reframe为positive： \"practitioners can cautiously extrapolate MMLU-derived budgets to other knowledge benchmarks\"——但D-study cross-bench Δ=0.03-0.06削弱了\"cautiously\"的程度。 Separability完全退出claims降为observation——exp-003（partial）显示hardware×method =4.2% binary，exp-002显示cross-bench separability max=4.8%。 Item resampling instability（CV=0.14）正面spin：item sampling本身就是major variance source，reinforcing G-theory over fixed-benchmark evaluation。 Leave-one-model-out matched rerun spread=0.058暴露4-model estimate的fragility， 需要10+模型才能stable——在Discussion中honest报告并标注为limitation。 Title改为：\"The Hidden Second Factor: Model×Item Interaction Accounts for 34% of LLM Evaluation Variance\"。 AAAI仍可冲（5-6/10），execution必须完美：writing clean、figures compelling、 related work滴水不漏。若AAAI被拒，ACL ARR October有充分时间补实验+扩模型数。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-21T08:28:06.919Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T08:28:06.919Z",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3"
}
```

---

## Round 1

36 recorded events

### User

_source line 3 · 2026-05-21T08:28:06.936Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T075006 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Gradient narrative死掉——exp-002显示variance structure跨benchmark几乎不变（item_id range仅5.7pp），没有knowledge→reasoning的系统性梯度。必须reframe整篇论文。 新angle：MMLU作为"case study in multi-facet evaluation measurement"。 三条Primary contributions： (1) model×item interaction量化——42%→61%的inflation效应 + D-study Δ=0.004 out-of-sample验证，这些数字已锁定（来自actual 4-model data），不受exp-002影响； (2) IRT vs G-theory direct comparison——MMLU上3.6-4.4×差异是publishable finding， 但跨benchmark ratio从1.6×到4.1×不等（GSM8K/HellaSwag < 2×），所以"3-4×" 只能claim for MMLU，cross-benchmark需说"benchmark-dependent"； (3) variance structure benchmark-insensitivity本身reframe为positive： "practitioners can cautiously extrapolate MMLU-derived budgets to other knowledge benchmarks"——但D-study cross-bench Δ=0.03-0.06削弱了"cautiously"的程度。 Separability完全退出claims降为observation——exp-003（partial）显示hardware×method =4.2% binary，exp-002显示cross-bench separability max=4.8%。 Item resampling instability（CV=0.14）正面spin：item sampling本身就是major variance source，reinforcing G-theory over fixed-benchmark evaluation。 Leave-one-model-out matched rerun spread=0.058暴露4-model estimate的fragility， 需要10+模型才能stable——在Discussion中honest报告并标注为limitation。 Title改为："The Hidden Second Factor: Model×Item Interaction Accounts for 34% of LLM Evaluation Variance"。 AAAI仍可冲（5-6/10），execution必须完美：writing clean、figures compelling、 related work滴水不漏。若AAAI被拒，ACL ARR October有充分时间补实验+扩模型数。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9d021380-77fd-4766-a060-794a49f7c1c1",
  "type": "user",
  "uuid": "f440a65d-20c5-4dc7-9309-cbaa5d03b66f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T08:28:06.935Z_

```json
{
  "parentUuid": "f440a65d-20c5-4dc7-9309-cbaa5d03b66f",
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
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
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
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "0ad03b57-2d57-44c1-9b9f-da9d6d8d002e",
  "timestamp": "2026-05-21T08:28:06.935Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T08:28:06.935Z_

```json
{
  "parentUuid": "0ad03b57-2d57-44c1-9b9f-da9d6d8d002e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7bcea5b4-3c4a-42da-98a6-91bfdac67901",
  "timestamp": "2026-05-21T08:28:06.935Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate LLM evaluation variance analysis paper",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3"
}
```

---

### Assistant

_source line 7 · 2026-05-21T08:28:09.704Z_

I'll start by reading the experiment data and paper framing files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bcea5b4-3c4a-42da-98a6-91bfdac67901",
  "isSidechain": false,
  "requestId": "req_011CbFQ3g5Wpn98s2Qdr9D76",
  "type": "assistant",
  "uuid": "72afd3a6-6f90-4518-9ac1-c8ed7a03ac71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEDWRq8QGheKCyD9qkJf9h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11879,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11879
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

_source line 8 · 2026-05-21T08:28:10.806Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WqCGApb4327pQPiCQWTn1z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72afd3a6-6f90-4518-9ac1-c8ed7a03ac71",
  "isSidechain": false,
  "requestId": "req_011CbFQ3g5Wpn98s2Qdr9D76",
  "type": "assistant",
  "uuid": "205be5b8-e484-444c-b459-05b770425772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEDWRq8QGheKCyD9qkJf9h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11879,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11879
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

_source line 9 · 2026-05-21T08:28:10.859Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CZZj8XSB4puk8J6RvdLCsZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "205be5b8-e484-444c-b459-05b770425772",
  "isSidechain": false,
  "requestId": "req_011CbFQ3g5Wpn98s2Qdr9D76",
  "type": "assistant",
  "uuid": "f8c71cc3-64a5-4c48-9769-61d60a3250e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEDWRq8QGheKCyD9qkJf9h",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11879,
      "cache_read_input_tokens": 11841,
      "output_tokens": 206,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11879,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 206,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11879
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

_source line 10 · 2026-05-21T08:28:10.869Z_

<details><summary>↩ Tool result · `toolu_01CZZj8XSB4puk8J6RvdLCsZ`</summary>

```text
1	# Paper Framing — nlp_variance_gtheory
2	
3	## Target Venue
4	- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)
5	- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)
6	- Extended: TACL (rolling)
7	
8	## Title
9	Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics
10	
11	## Core Claims (3 条，可证伪)
12	
13	**Claim 1 — Model-Conditional Item Dominance**: Item selection is the single largest variance source in single-model LLM evaluation (61.1% on MMLU), but model×item interaction (26.2%) emerges as the second-largest source when model is treated as a crossed facet. Item difficulty rankings are model-specific: two models with similar aggregate accuracy (Llama 66.4% vs Gemma 73.2%) disagree dramatically at the item level — item_id drops from 61% (single-model) to 38% (cross-model) as model×item absorbs the model-conditional portion. This means single-model variance decompositions overestimate item dominance by conflating universal and model-specific item difficulty. Cross-benchmark gradient (pending exp-002) is hypothesized to further modulate this structure.
14	**Empirical anchors (exp-001, 4 models, balanced bf16, 345,600 records)**: Single-model item_id=61.1%, cross-model item_id=42.1% [36.0-48.8%] (↓19pp), model×item=33.6% [28.4-37.9%] (second-largest source, increased from 3-model 31.7%). G_item=0.820 [0.782-0.861]. D-study prediction validated out-of-sample: 3-model predicted G=0.816 for n=4, actual=0.820 (Δ=0.004). Forward projection: 5 models → G=0.848, 8→0.893, 10→0.910 (G≥0.90 requires ~10 models). Residual dropped 24%→19.5% as 4th model split residual into model×item. Per-model interaction: Mistral 29.25% (lowest accuracy 63.8%) > Qwen 27.11% > Gemma 23.95% > Llama 19.69%.
15	**REML robustness**: REML-EM (500 iter, practical convergence Δ<0.003pp) confirms Henderson I: all components differ <0.5pp. Henderson I unbiased for balanced designs. Dataset B differences (item_id 38→52%, model×item 26→12%) due to design differences (factor selection), not estimator bias — measurement design choices themselves affect observed variance structure.
16	**Pending**: BF16-vs-FP16-only sensitivity (exclude FP32 confound); leave-one-model-out stability (4-model marginal concern).
17	
18	**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), "infrastructure" is currently limited to the precision facet.
19	
20	**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent and temperature-conditional. Binary correct: G=0.611 (200 items), G≥0.80 requires ~510 items (all facets random) or ~414 items (practical: precision+temperature fixed). Text-exact-match: G=0.007 (temperature dominates at 79.7%), unreliable at any temperature >0. Temperature-stratified analysis reveals binary G degrades monotonically (T=0.0: 0.760 → T=0.7: 0.549). G-theory requires 3.6-4.4× more items than IRT (510 vs 116) because it accounts for prompt×item (4.6%), seed×item (4.7%), and residual (21.6%) dimensions that IRT ignores. Current practices (1 prompt, 1 seed, ≤200 items) yield G=0.611 — below the 0.80 threshold for dependable measurement.
21	
22	## Contributions (4 条，明确区分)
23	
24	1. **Model×item interaction as the hidden dominant source**: In a balanced 4-model design (345,600 records), model×item interaction (33.6%, CI [28.4-37.9%]) is the second-largest variance source, while item_id drops from 61% (single-model) to 42%. Item difficulty rankings are model-specific — single-model G-studies overestimate item dominance by conflating universal and model-specific difficulty. G_item=0.820 [0.782-0.861] with 4 models; D-study prediction validated out-of-sample (3-model predicted 0.816, actual 0.820, Δ=0.004). Reaching G≥0.90 requires ~10 models. [Note: position as quantification of a phenomenon expected from measurement theory, not as a surprising discovery. The novelty is the magnitude, the out-of-sample D-study validation, and the cross-model generalizability implications.]
25	
26	2. **Precision separability with metric qualification**: Precision×methodology interactions are negligible under binary scoring (<0.1%), providing empirical support for isolated-factor studies. Under text-exact-match scoring, precision×temperature reaches 4.15%, consistent with floating-point non-associativity. Separability is confirmed as metric-conditional. [Note: scope to "numerical precision on single GPU architecture" — not "infrastructure" broadly. This is a confirmatory secondary finding, not a primary contribution. Pending BF16-vs-FP16 sensitivity to isolate FP32/vLLM confound.]
27	
28	3. **IRT vs G-theory: the cost of multi-facet reliability**: The first direct comparison showing G-theory requires 3.6-4.4× more items than IRT (510 vs 116 for MMLU) because it accounts for prompt, seed, and ordering dimensions that IRT ignores. At IRT's recommended 116 items, G-theory G is only 0.529. This quantifies the "hidden cost" of evaluation dimensions invisible to IRT.
29	
30	4. **Practitioner toolkit**: Open-source G-theory variance decomposition pipeline + D-study budget calculator for LLM evaluation. Includes: (a) benchmark-specific reproducibility budget tables (items × prompts × seeds for target G), (b) temperature-stratified reliability guide, (c) model-as-facet analysis template. Addresses "purely diagnostic" criticism — provides actionable tools, not just warnings.
31	
32	## Methodological Robustness Package (6 验证分析)
33	All completed on Llama 239,200 records:
34	- **Binary data not artifact**: Null simulation item_id=0.08% vs observed 61.1% (737.5×); obs/Bernoulli ratio=1.0008
35	- **Fixed vs random insensitive**: Binary G ranges 0.611-0.664 across all facet classification choices
36	- **Bootstrap = jackknife**: CI width ratio 0.96-1.04, independence violation negligible
37	- **Temperature stratification**: Binary G degrades T=0.0 (0.760) → T=0.7 (0.549); text metric unreliable at all T>0
38	- **D-study formula verified**: Monotonicity assertion added; min_items_G80=414 (practical) / 510 (all random)
39	- **IRT comparison**: G-theory 3.6-4.4× more conservative than IRT; difference attributable to prompt/seed/ordering dimensions
40	- **REML vs Henderson I**: REML-EM (500 iter) confirms all components within <0.5pp of Henderson I; Henderson I unbiased for balanced designs
41	- **BF16-vs-FP16 sensitivity**: Excluding FP32, precision effect drops from 0.4% to 0.0006% (precision×item: 1.3%→0.04%). FP32 anomaly is entirely a vLLM enforce_eager artifact, not a fundamental precision effect. BF16≈FP16 (Δ=0.23pp accuracy)
42	- **Leave-one-model-out stability**: All 4 three-model subsets preserve item_id dominance and G_item>0.80 (pending matched-specification rerun for absolute comparability)
43	
44	## Story Spine
45	
46	**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.
47	
48	**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.
49	
50	**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.
51	
52	**Headline result template**: "In a G-study of 345,600 evaluation records across 4 models on MMLU (200 items × 6 prompts × 6 seeds × 3 temperatures × 4 orderings), item selection accounts for 42% of variance when model is treated as a crossed facet — but model×item interaction (34%) emerges as the second-largest source, revealing that item difficulty rankings are substantially model-specific (G_item=0.82, requiring ~10 models for G≥0.90). A D-study from 3 models predicted the 4-model G coefficient within 0.004 — out-of-sample validation of the D-study methodology. G-theory requires 3.6-4.4× more items than IRT for reliable measurement because it accounts for prompt, seed, and ordering dimensions that IRT ignores. Numerical precision×methodology interactions are negligible under binary scoring (<0.1%). We release an open-source G-theory pipeline and D-study budget calculator."
53	
54	## Hook (Counter-Intuitive Quantified Claim)
55	"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory."
56	
57	## Narrative Strategy
58	- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)
59	- **Tension**: "No universal recipe" — the field seeks standardization but variance structure varies qualitatively across task types
60	- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)
61	- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)
62	- **Figure plan** (5 figures):
63	  1. **Stacked-bar: single-model vs cross-model variance decomposition** — item_id shrinks from 61% to 42%, model×item appears at 34%, residual drops 24%→20%. The "reveal" figure.
64	  2. **G-theory crossed design diagram** — facets, levels, crossing structure
65	  3. **D-study projection curves** — G vs item count for binary (practical vs all-random) and text metric. Shows G≥0.80 threshold at ~414/510 items.
66	  4. **IRT vs G-theory item requirement comparison** — bar chart showing 116 (IRT) vs 510 (G-theory) items, with breakdown of where the extra items go (prompt×item, seed×item, residual)
67	  5. **Temperature-stratified G coefficient heatmap** — binary vs text metric × 3 temperatures, showing metric×temperature interaction
68	- **Key framing shifts from Dream feedback**:
69	  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty
70	  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient
71	  - Cross-benchmark gradient is the **primary novel finding**
72	  - "Fully crossed" language qualified to MMLU exp-001 only; other benchmarks use reduced designs
73	
74	## Venue Fit Risks
75	- AAAI: Strong fit for "evaluation methodology" track. Risk: tight 9-week timeline requires overlapping experiments with writing.
76	- Reviewer concern 1: "Only open-weight models, not API models" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.
77	- Reviewer concern 2: "G-theory is borrowed methodology, not novel" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.
78	- Reviewer concern 3: "Item dominance is obvious from measurement theory" — Acknowledge explicitly. Contribution is quantification (X-Y%, pending exp-001/002), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.
79	
80	## Anticipated Reviewer Concerns & Planned Responses
81	1. **"Only N GPU types"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to "numerical precision" and frame hardware as future work.
82	2. **"float32 engine confound"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.
83	3. **"Only MMLU"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.
84	4. **"Small item sample"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.
85	5. **"No training-time analysis"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.
86	6. **"Missing scale validation"** → exp-005 (14B models)
87	7. **"G-theory may not be right framework"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.
88	8. **"Separability claim is metric-dependent"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.
89	9. **"FP32 degradation is already known (Yuan 2025)"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.
90	10. **"Incremental over Mesting (2026)"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.
91	11. **"Model not treated as G-theory facet"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.
92	12. **"No CIs on variance components"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.
93	13. **"Missing related work — IRT, tinyBenchmarks, Bouthillier"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.
94	14. **"Diagnostic tool claim unsubstantiated"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as "empirical analysis + data release."
95	15. **"Fine-tuning uses encoder-only RoBERTa"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.
96	
97	## Design Decisions
98	- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.
99	- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.
100	- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.
101	- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.
102	- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.
103	- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as "reduced crossing" rather than "fully crossed."
104	- **Gemma2 float16 exclusion**: Gemma2 architecture does not support float16 inference (vLLM numerical instability guard). Cross-model analysis uses bf16+fp32 (balanced). fp16 data from Llama/Mistral/Qwen used in within-model analyses. bf16≈fp16 difference <0.1pp (D005).
105	
106	## Methodological Defenses (Dream #2 审稿问题逐条应对)
107	
108	### MD1. Binary Data in G-theory
109	**Issue**: Standard G-theory assumes continuous, approximately normal response variables. Binary 0/1 data violates this; item variance is mechanically linked to item difficulty via Bernoulli p(1-p).
110	**Defense strategy**: (a) Report correlation between Bernoulli variance p_i(1-p_i) and observed item variance — quantify how much item_id is "mechanical" vs informative; (b) Run parallel analysis on text_exact_match (continuous metric) to show variance structure is robust across metrics; (c) Discuss generalized G-theory (Brennan 2001 Ch.12) in Limitations; (d) Cite Lalor et al. (2019) who used IRT (also assumes latent continuous) on binary NLP data without this criticism being fatal.
111	
112	### MD2. Fixed vs Random Facet Sensitivity
113	**Issue**: Temperature (2-3 design points) and ordering (4 systematic rotations) are not randomly sampled from a universe — treating them as random facets may be inappropriate.
114	**Defense strategy**: Run sensitivity analysis with temperature and ordering as fixed facets. If variance decomposition changes <5%, report as robust. If substantial, discuss implications and present both analyses. This directly addresses Reviewer concern.
115	
116	### MD3. Separability Claim Scope
117	**Issue**: Separability (<0.3%) holds for knowledge benchmarks but not reasoning tasks (GSM8K=3.0%, MATH=2.5%).
118	**Defense**: Qualify all separability claims as "under binary scoring on knowledge-retrieval benchmarks." Present benchmark-conditional separability as a finding (not a limitation): "separability itself varies across task types."
119	
120	### MD4. D-study Optimization Documentation
121	**Issue**: Optimization procedure undocumented; Table 10 arithmetic anomaly (fewer items → higher G).
122	**Defense**: Document grid search procedure (bounds, step sizes, objective function). Verify and explain any non-monotonicity (likely due to joint optimization across facets where reallocating item budget to prompt/seed is more efficient).
123	
124	### MD5. G-coefficient Interpretation
125	**Issue**: G=0.22 for 200 items ≠ "MMLU is unreliable" (standard MMLU uses ~14K items).
126	**Defense**: (a) Clearly distinguish "G for our 200-item subsample design" from "reliability of full MMLU"; (b) Report D-study projection to 14K items; (c) Frame G=0.22 as "cost of subsampling" rather than "MMLU is broken."
127	
128	### MD6. Bootstrap Independence
129	**Issue**: Item-level bootstrap with replacement creates ~127 unique items per 200-item resample, violating independence.
130	**Defense**: (a) Implement delete-1 jackknife as comparison; (b) If bootstrap and jackknife CIs are similar (within 20%), report as robust; (c) Discuss limitation in Methods.
131	
132	### MD7. IRT vs G-theory Comparison
133	**Issue**: tinyBenchmarks recommends ~100 items, D-study recommends 420. 4× discrepancy unexplained.
134	**Defense**: Direct comparison showing G-theory accounts for prompt/seed/ordering dimensions that IRT ignores. The 4× difference is the "cost of multi-facet reliability" — G-theory's budget is larger because it targets reliability across ALL facets, not just items. This comparison is a potential standalone contribution.
135	
136	### MD8. Cross-benchmark Design Asymmetry
137	**Issue**: MMLU uses 3 prec × 3 temp, other benchmarks use 2 × 2.
138	**Defense**: Re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7) and compare variance decomposition. If <5% change, report as robust to design reduction.
139	
140	### MD9. Title-Content Alignment
141	**Issue**: Title promises "Evaluation Metrics" but logprob analysis is minimal.
142	**Defense**: Expand logprob analysis across all benchmarks in exp-004, OR adjust title to "...Across Benchmarks and Models."
143	
144	## Required Bibliography (minimum 25 references)
145	Key references to include beyond current literature_map:
146	- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA
147	- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP
148	- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP
149	- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling
150	- Perlitz et al. (2023) — Efficient LLM benchmarking
151	- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition
152	- Shavelson & Webb (1991) — G-theory primer (canonical)
153	- Brennan (2001) — G-theory textbook (canonical, Ch.12 on binary data)
154	- Lu et al. (2022) — Option ordering effects in MC evaluation
155	- Pezeshkpour & Hruschka (2024) — Option ordering effects
156	- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)
157	- Sellam et al. (2022) — MultiBERTs, multi-seed training
158	- Dehghani et al. (2021) — Benchmark Lottery
159	- Biderman et al. (2024) — Evaluation reproducibility lessons
160	- Vania et al. (2021) — IRT item properties in NLP
161	- **Sclar et al. (2024, ICLR)** — Up to 76% accuracy swing from prompt formatting; directly relevant to prompt×item variance [Dream #3: all 3 tiers flagged as missing]
162	- **Kunievsky & Evans (2025)** — Alternative decomposition: intent/articulation/model uncertainty; competing framework to G-theory [Dream #3: all 3 tiers flagged]
163	- **Bui et al. (2025)** — Extreme seed sensitivity in fine-tuning (RTES variance=18.22 for RoBERTa on COPA) [Dream #3: relevant to exp-006]
164	- **Jiang & Skorupski (2017)** — Logistic-link generalized G-theory for binary data [Dream #3 worst: methodological defense for REML on binary]
165	- **Mushquash & O'Connor (2006)** — Binary-data G-theory [Dream #3: classical psychometrics gap]
166	- **Shavelson et al. (1989)** — Binary response G-theory treatment [Dream #3: classical psychometrics]
167	
168	## Dream #3 Framing Directives (2026-05-21, D006)
169	Post-analysis framing adjustments based on three-tier consistent feedback:
170	1. **Center gradient + model×item as primary contributions** — infrastructure crossing is confirmatory secondary
171	2. **Position explicitly as empirical extension of Mesting (2026)** with novel findings (model×item quantification, D-study out-of-sample validation, IRT comparison), not a new framework. Remove "first" claims where not defensible.
172	3. **Scope Claim 2 to "precision separability"** — not "infrastructure" broadly. Single GPU architecture.
173	4. **Item dominance is psychometrically expected** — contribution is quantification of magnitude, metric-conditionality, and D-study implications
174	5. **Fine-tuning (exp-006) downgraded** to Discussion-section preliminary observation, not a numbered contribution
175	6. **Add explicit judge-facet exclusion discussion** vs Mesting: we fix judge to isolate other factors; Mesting's 43.8% judge variance would dominate
176	7. **Practitioner toolkit must be concrete**: specify released scripts, D-study calculator, budget lookup tables
177	8. **Figures are non-negotiable**: 5 planned figures address all-tier "zero figures" criticism
178	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8c71cc3-64a5-4c48-9769-61d60a3250e5",
  "isSidechain": false,
  "promptId": "9d021380-77fd-4766-a060-794a49f7c1c1",
  "type": "user",
  "uuid": "761fd288-ba2e-4a3b-84d2-4c61a97ad278",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/paper_framing.md",
      "content": "# Paper Framing — nlp_variance_gtheory\n\n## Target Venue\n- Primary: AAAI 2027 (abstract Jul 21, paper Jul 28 — 9 weeks from today)\n- Backup: ACL 2027 via ARR (October 15 cycle — 21 weeks)\n- Extended: TACL (rolling)\n\n## Title\nReproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics\n\n## Core Claims (3 条，可证伪)\n\n**Claim 1 — Model-Conditional Item Dominance**: Item selection is the single largest variance source in single-model LLM evaluation (61.1% on MMLU), but model×item interaction (26.2%) emerges as the second-largest source when model is treated as a crossed facet. Item difficulty rankings are model-specific: two models with similar aggregate accuracy (Llama 66.4% vs Gemma 73.2%) disagree dramatically at the item level — item_id drops from 61% (single-model) to 38% (cross-model) as model×item absorbs the model-conditional portion. This means single-model variance decompositions overestimate item dominance by conflating universal and model-specific item difficulty. Cross-benchmark gradient (pending exp-002) is hypothesized to further modulate this structure.\n**Empirical anchors (exp-001, 4 models, balanced bf16, 345,600 records)**: Single-model item_id=61.1%, cross-model item_id=42.1% [36.0-48.8%] (↓19pp), model×item=33.6% [28.4-37.9%] (second-largest source, increased from 3-model 31.7%). G_item=0.820 [0.782-0.861]. D-study prediction validated out-of-sample: 3-model predicted G=0.816 for n=4, actual=0.820 (Δ=0.004). Forward projection: 5 models → G=0.848, 8→0.893, 10→0.910 (G≥0.90 requires ~10 models). Residual dropped 24%→19.5% as 4th model split residual into model×item. Per-model interaction: Mistral 29.25% (lowest accuracy 63.8%) > Qwen 27.11% > Gemma 23.95% > Llama 19.69%.\n**REML robustness**: REML-EM (500 iter, practical convergence Δ<0.003pp) confirms Henderson I: all components differ <0.5pp. Henderson I unbiased for balanced designs. Dataset B differences (item_id 38→52%, model×item 26→12%) due to design differences (factor selection), not estimator bias — measurement design choices themselves affect observed variance structure.\n**Pending**: BF16-vs-FP16-only sensitivity (exclude FP32 confound); leave-one-model-out stability (4-model marginal concern).\n\n**Claim 2 — Conditional Separability**: Infrastructure factors (numerical precision) and methodology factors (prompt, seed, temperature, ordering) are approximately separable at the aggregate level — direct infrastructure×methodology interaction ≈0% under binary scoring; the only detectable cross-factor interaction (precision×temperature=1.3%) emerges under text-exact-match scoring, consistent with floating-point non-associativity (Messina & Scotta, 2026). Both factor types interact substantially with item difficulty (precision×item, prompt×item), making their effects item-conditional. This provides a metric-qualified confirmatory finding for isolated-factor studies while warning that conclusions are conditional on item selection and evaluation metric. Note: with only numerical precision tested on a single GPU architecture (pending exp-003 for hardware crossing), \"infrastructure\" is currently limited to the precision facet.\n\n**Claim 3 — Metric-Conditional Reproducibility Budget**: Reproducibility budgets are fundamentally metric-dependent and temperature-conditional. Binary correct: G=0.611 (200 items), G≥0.80 requires ~510 items (all facets random) or ~414 items (practical: precision+temperature fixed). Text-exact-match: G=0.007 (temperature dominates at 79.7%), unreliable at any temperature >0. Temperature-stratified analysis reveals binary G degrades monotonically (T=0.0: 0.760 → T=0.7: 0.549). G-theory requires 3.6-4.4× more items than IRT (510 vs 116) because it accounts for prompt×item (4.6%), seed×item (4.7%), and residual (21.6%) dimensions that IRT ignores. Current practices (1 prompt, 1 seed, ≤200 items) yield G=0.611 — below the 0.80 threshold for dependable measurement.\n\n## Contributions (4 条，明确区分)\n\n1. **Model×item interaction as the hidden dominant source**: In a balanced 4-model design (345,600 records), model×item interaction (33.6%, CI [28.4-37.9%]) is the second-largest variance source, while item_id drops from 61% (single-model) to 42%. Item difficulty rankings are model-specific — single-model G-studies overestimate item dominance by conflating universal and model-specific difficulty. G_item=0.820 [0.782-0.861] with 4 models; D-study prediction validated out-of-sample (3-model predicted 0.816, actual 0.820, Δ=0.004). Reaching G≥0.90 requires ~10 models. [Note: position as quantification of a phenomenon expected from measurement theory, not as a surprising discovery. The novelty is the magnitude, the out-of-sample D-study validation, and the cross-model generalizability implications.]\n\n2. **Precision separability with metric qualification**: Precision×methodology interactions are negligible under binary scoring (<0.1%), providing empirical support for isolated-factor studies. Under text-exact-match scoring, precision×temperature reaches 4.15%, consistent with floating-point non-associativity. Separability is confirmed as metric-conditional. [Note: scope to \"numerical precision on single GPU architecture\" — not \"infrastructure\" broadly. This is a confirmatory secondary finding, not a primary contribution. Pending BF16-vs-FP16 sensitivity to isolate FP32/vLLM confound.]\n\n3. **IRT vs G-theory: the cost of multi-facet reliability**: The first direct comparison showing G-theory requires 3.6-4.4× more items than IRT (510 vs 116 for MMLU) because it accounts for prompt, seed, and ordering dimensions that IRT ignores. At IRT's recommended 116 items, G-theory G is only 0.529. This quantifies the \"hidden cost\" of evaluation dimensions invisible to IRT.\n\n4. **Practitioner toolkit**: Open-source G-theory variance decomposition pipeline + D-study budget calculator for LLM evaluation. Includes: (a) benchmark-specific reproducibility budget tables (items × prompts × seeds for target G), (b) temperature-stratified reliability guide, (c) model-as-facet analysis template. Addresses \"purely diagnostic\" criticism — provides actionable tools, not just warnings.\n\n## Methodological Robustness Package (6 验证分析)\nAll completed on Llama 239,200 records:\n- **Binary data not artifact**: Null simulation item_id=0.08% vs observed 61.1% (737.5×); obs/Bernoulli ratio=1.0008\n- **Fixed vs random insensitive**: Binary G ranges 0.611-0.664 across all facet classification choices\n- **Bootstrap = jackknife**: CI width ratio 0.96-1.04, independence violation negligible\n- **Temperature stratification**: Binary G degrades T=0.0 (0.760) → T=0.7 (0.549); text metric unreliable at all T>0\n- **D-study formula verified**: Monotonicity assertion added; min_items_G80=414 (practical) / 510 (all random)\n- **IRT comparison**: G-theory 3.6-4.4× more conservative than IRT; difference attributable to prompt/seed/ordering dimensions\n- **REML vs Henderson I**: REML-EM (500 iter) confirms all components within <0.5pp of Henderson I; Henderson I unbiased for balanced designs\n- **BF16-vs-FP16 sensitivity**: Excluding FP32, precision effect drops from 0.4% to 0.0006% (precision×item: 1.3%→0.04%). FP32 anomaly is entirely a vLLM enforce_eager artifact, not a fundamental precision effect. BF16≈FP16 (Δ=0.23pp accuracy)\n- **Leave-one-model-out stability**: All 4 three-model subsets preserve item_id dominance and G_item>0.80 (pending matched-specification rerun for absolute comparability)\n\n## Story Spine\n\n**Problem**: When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or item selection — let alone how these factors interact. Every prior study isolates at most two sources, implicitly assuming separability.\n\n**Existing approaches & gaps**: Bouthillier et al. (2021) decomposed ML benchmark variance across hyperparameters, data splits, and seeds via ANOVA, establishing the template for factorial variance decomposition in ML evaluation. Mesting (2026) adapted G-theory to 5 methodological facets in LLM evaluation but treated infrastructure as fixed. Yuan et al. (2025) documented up to 9% accuracy variation from hardware/precision without factorial attribution. Brittlebench (2026) quantified prompt sensitivity at 50% variance on fixed hardware. IRT-based approaches (Lalor et al. 2019; Rodriguez et al. 2021; Polo et al. 2024) have analyzed item-level properties and efficient subsampling, but from a different methodological perspective than G-theory. No study has: (a) crossed infrastructure and methodology in a unified G-theory framework, (b) compared variance structure across multiple benchmarks, or (c) provided metric-conditional reproducibility budgets.\n\n**Our framing**: We conduct a multi-benchmark G-theory study crossing infrastructure (numerical precision) × methodology (prompt, seed, temperature, ordering) × measurement (item) factors, with model treated as a crossed facet. The infrastructure crossing yields a confirmatory null result: aggregate separability holds, validating the implicit assumption of prior isolated-factor studies. The primary novel finding is the cross-benchmark variance gradient — item dominance systematically weakens as tasks shift from knowledge retrieval to multi-step reasoning — explaining divergent conclusions in the literature. D-study projections provide the first benchmark-specific, metric-conditional reproducibility budgets for LLM evaluation, directly comparable to IRT-based subsampling approaches.\n\n**Headline result template**: \"In a G-study of 345,600 evaluation records across 4 models on MMLU (200 items × 6 prompts × 6 seeds × 3 temperatures × 4 orderings), item selection accounts for 42% of variance when model is treated as a crossed facet — but model×item interaction (34%) emerges as the second-largest source, revealing that item difficulty rankings are substantially model-specific (G_item=0.82, requiring ~10 models for G≥0.90). A D-study from 3 models predicted the 4-model G coefficient within 0.004 — out-of-sample validation of the D-study methodology. G-theory requires 3.6-4.4× more items than IRT for reliable measurement because it accounts for prompt, seed, and ordering dimensions that IRT ignores. Numerical precision×methodology interactions are negligible under binary scoring (<0.1%). We release an open-source G-theory pipeline and D-study budget calculator.\"\n\n## Hook (Counter-Intuitive Quantified Claim)\n\"Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation implicitly assume that their findings will generalize across benchmarks — our G-theory analysis across N benchmarks shows the variance structure itself is benchmark-conditional, rendering any 'universal reproducibility recipe' illusory.\"\n\n## Narrative Strategy\n- **Type**: Cross-domain transfer (psychometrics G-theory → ML evaluation) + Empirical contribution (benchmark-conditional gradient)\n- **Tension**: \"No universal recipe\" — the field seeks standardization but variance structure varies qualitatively across task types\n- **Intro structure**: 4 paragraphs + 3 contributions (field mode from distilled writing patterns)\n- **Signature visual**: Stacked-bar variance decomposition chart across benchmarks (field idiom from Mesting/Brittlebench)\n- **Figure plan** (5 figures):\n  1. **Stacked-bar: single-model vs cross-model variance decomposition** — item_id shrinks from 61% to 42%, model×item appears at 34%, residual drops 24%→20%. The \"reveal\" figure.\n  2. **G-theory crossed design diagram** — facets, levels, crossing structure\n  3. **D-study projection curves** — G vs item count for binary (practical vs all-random) and text metric. Shows G≥0.80 threshold at ~414/510 items.\n  4. **IRT vs G-theory item requirement comparison** — bar chart showing 116 (IRT) vs 510 (G-theory) items, with breakdown of where the extra items go (prompt×item, seed×item, residual)\n  5. **Temperature-stratified G coefficient heatmap** — binary vs text metric × 3 temperatures, showing metric×temperature interaction\n- **Key framing shifts from Dream feedback**:\n  - Infrastructure crossing framed as **confirmatory** (validates isolated-factor studies), not as primary novelty\n  - Item dominance acknowledged as **psychometrically expected**; contribution is quantification + benchmark gradient\n  - Cross-benchmark gradient is the **primary novel finding**\n  - \"Fully crossed\" language qualified to MMLU exp-001 only; other benchmarks use reduced designs\n\n## Venue Fit Risks\n- AAAI: Strong fit for \"evaluation methodology\" track. Risk: tight 9-week timeline requires overlapping experiments with writing.\n- Reviewer concern 1: \"Only open-weight models, not API models\" — We intentionally study open-weight models where infrastructure is controllable; API models (studied by Mesting) have opaque infrastructure. Frame as complementary.\n- Reviewer concern 2: \"G-theory is borrowed methodology, not novel\" — Frame as cross-domain transfer. The novelty is the cross-benchmark variance gradient finding, not G-theory itself.\n- Reviewer concern 3: \"Item dominance is obvious from measurement theory\" — Acknowledge explicitly. Contribution is quantification (X-Y%, pending exp-001/002), benchmark-dependence, and D-study implications. Contextualize against IRT item analysis literature.\n\n## Anticipated Reviewer Concerns & Planned Responses\n1. **\"Only N GPU types\"** → exp-003 (multi-hardware crossing) addresses this. If blocked, explicitly scope to \"numerical precision\" and frame hardware as future work.\n2. **\"float32 engine confound\"** → exp-001 fixes with V0 enforce_eager for all precisions. Confound discovery itself is a standalone methodological contribution.\n3. **\"Only MMLU\"** → exp-002 expands to GSM8K, ARC-Challenge, HellaSwag. Cross-benchmark gradient is the core finding.\n4. **\"Small item sample\"** → exp-001 expands from 50 to 200 items. exp-001b tests resampling stability.\n5. **\"No training-time analysis\"** → exp-006 (fine-tuning G-study with RoBERTa). Explicitly qualify as encoder-only classification; decoder fine-tuning is future work.\n6. **\"Missing scale validation\"** → exp-005 (14B models)\n7. **\"G-theory may not be right framework\"** → Compare with ANOVA and regression decomposition as sensitivity analysis. Cite Bouthillier et al. (2021) as ANOVA-based predecessor; show G-theory adds D-study projections.\n8. **\"Separability claim is metric-dependent\"** → This is precisely the point: reproducibility budgets must be metric-qualified. Replace arbitrary threshold with bootstrap CI on interaction term.\n9. **\"FP32 degradation is already known (Yuan 2025)\"** → Position as supporting finding with novel item-level breakdown. Not an independent claim.\n10. **\"Incremental over Mesting (2026)\"** → Infrastructure crossing is confirmatory (valuable as validation, not breakthrough). Primary novelty: cross-benchmark gradient, task-specific budgets, dual-metric analysis, confound fix. Mesting = single benchmark, no infrastructure; we = multi-benchmark, infrastructure confirmation + benchmark gradient.\n11. **\"Model not treated as G-theory facet\"** → exp-004 includes model-as-facet reanalysis of MMLU data. Report model×item interaction separately from residual.\n12. **\"No CIs on variance components\"** → exp-004 includes bootstrap CIs (1000 resamples) on all variance components in all tables.\n13. **\"Missing related work — IRT, tinyBenchmarks, Bouthillier\"** → Comprehensive bibliography (25+ refs). Position D-study budgets against IRT-based subsampling. Cite Bouthillier et al. as ANOVA predecessor.\n14. **\"Diagnostic tool claim unsubstantiated\"** → Release analysis pipeline code (G-theory variance decomposition + D-study projections) as reusable tool. Or reframe as \"empirical analysis + data release.\"\n15. **\"Fine-tuning uses encoder-only RoBERTa\"** → Explicitly qualify. Decoder fine-tuning is a natural extension requiring substantially more compute.\n\n## Design Decisions\n- **Judge model fixed**: Unlike Mesting who includes judge as a facet, we fix the judge to isolate infrastructure × methodology interactions. Judge variance (Mesting: 43.8%) would dominate and obscure the effects we study. Adding judge is a natural extension for future work.\n- **Generation-based evaluation**: Following Hua et al. (EMNLP 2025), we avoid log-likelihood scoring to eliminate scoring artifacts that inflate apparent prompt sensitivity.\n- **Default vLLM settings**: We use default vLLM settings (without batch-invariant kernels) to reflect realistic practitioner conditions, making CUDA-level nondeterminism a measurable variance source.\n- **vLLM 0.9.2**: Required for Blackwell GPU (sm_100/sm_120) + CUDA 12.8 support.\n- **Model as crossed facet**: In exp-001 analysis (exp-004), model is treated as a crossed random facet in G-theory, not pooled or stratified. This properly attributes model×item interaction and avoids inflating item_id estimates.\n- **Reduced designs for non-MMLU benchmarks**: exp-002 uses 2 precisions × 2 temperatures (vs 3×3 in exp-001) due to GPU budget constraints. Explicitly described as \"reduced crossing\" rather than \"fully crossed.\"\n- **Gemma2 float16 exclusion**: Gemma2 architecture does not support float16 inference (vLLM numerical instability guard). Cross-model analysis uses bf16+fp32 (balanced). fp16 data from Llama/Mistral/Qwen used in within-model analyses. bf16≈fp16 difference <0.1pp (D005).\n\n## Methodological Defenses (Dream #2 审稿问题逐条应对)\n\n### MD1. Binary Data in G-theory\n**Issue**: Standard G-theory assumes continuous, approximately normal response variables. Binary 0/1 data violates this; item variance is mechanically linked to item difficulty via Bernoulli p(1-p).\n**Defense strategy**: (a) Report correlation between Bernoulli variance p_i(1-p_i) and observed item variance — quantify how much item_id is \"mechanical\" vs informative; (b) Run parallel analysis on text_exact_match (continuous metric) to show variance structure is robust across metrics; (c) Discuss generalized G-theory (Brennan 2001 Ch.12) in Limitations; (d) Cite Lalor et al. (2019) who used IRT (also assumes latent continuous) on binary NLP data without this criticism being fatal.\n\n### MD2. Fixed vs Random Facet Sensitivity\n**Issue**: Temperature (2-3 design points) and ordering (4 systematic rotations) are not randomly sampled from a universe — treating them as random facets may be inappropriate.\n**Defense strategy**: Run sensitivity analysis with temperature and ordering as fixed facets. If variance decomposition changes <5%, report as robust. If substantial, discuss implications and present both analyses. This directly addresses Reviewer concern.\n\n### MD3. Separability Claim Scope\n**Issue**: Separability (<0.3%) holds for knowledge benchmarks but not reasoning tasks (GSM8K=3.0%, MATH=2.5%).\n**Defense**: Qualify all separability claims as \"under binary scoring on knowledge-retrieval benchmarks.\" Present benchmark-conditional separability as a finding (not a limitation): \"separability itself varies across task types.\"\n\n### MD4. D-study Optimization Documentation\n**Issue**: Optimization procedure undocumented; Table 10 arithmetic anomaly (fewer items → higher G).\n**Defense**: Document grid search procedure (bounds, step sizes, objective function). Verify and explain any non-monotonicity (likely due to joint optimization across facets where reallocating item budget to prompt/seed is more efficient).\n\n### MD5. G-coefficient Interpretation\n**Issue**: G=0.22 for 200 items ≠ \"MMLU is unreliable\" (standard MMLU uses ~14K items).\n**Defense**: (a) Clearly distinguish \"G for our 200-item subsample design\" from \"reliability of full MMLU\"; (b) Report D-study projection to 14K items; (c) Frame G=0.22 as \"cost of subsampling\" rather than \"MMLU is broken.\"\n\n### MD6. Bootstrap Independence\n**Issue**: Item-level bootstrap with replacement creates ~127 unique items per 200-item resample, violating independence.\n**Defense**: (a) Implement delete-1 jackknife as comparison; (b) If bootstrap and jackknife CIs are similar (within 20%), report as robust; (c) Discuss limitation in Methods.\n\n### MD7. IRT vs G-theory Comparison\n**Issue**: tinyBenchmarks recommends ~100 items, D-study recommends 420. 4× discrepancy unexplained.\n**Defense**: Direct comparison showing G-theory accounts for prompt/seed/ordering dimensions that IRT ignores. The 4× difference is the \"cost of multi-facet reliability\" — G-theory's budget is larger because it targets reliability across ALL facets, not just items. This comparison is a potential standalone contribution.\n\n### MD8. Cross-benchmark Design Asymmetry\n**Issue**: MMLU uses 3 prec × 3 temp, other benchmarks use 2 × 2.\n**Defense**: Re-analyze MMLU with matched 2×2 design (bf16/fp16 × T=0.0/T=0.7) and compare variance decomposition. If <5% change, report as robust to design reduction.\n\n### MD9. Title-Content Alignment\n**Issue**: Title promises \"Evaluation Metrics\" but logprob analysis is minimal.\n**Defense**: Expand logprob analysis across all benchmarks in exp-004, OR adjust title to \"...Across Benchmarks and Models.\"\n\n## Required Bibliography (minimum 25 references)\nKey references to include beyond current literature_map:\n- Bouthillier et al. (2021, JMLR) — ML variance decomposition via ANOVA\n- Lalor et al. (2019, NAACL) — IRT-based item analysis in NLP\n- Rodriguez et al. (2021, ACL) — IRT evaluation for NLP\n- Polo et al. (2024) — tinyBenchmarks, IRT-based subsampling\n- Perlitz et al. (2023) — Efficient LLM benchmarking\n- Henderson et al. (2018) — Deep RL reproducibility, variance decomposition\n- Shavelson & Webb (1991) — G-theory primer (canonical)\n- Brennan (2001) — G-theory textbook (canonical, Ch.12 on binary data)\n- Lu et al. (2022) — Option ordering effects in MC evaluation\n- Pezeshkpour & Hruschka (2024) — Option ordering effects\n- Dodge et al. (2020, EMNLP) — Fine-tuning instability (seed, data order)\n- Sellam et al. (2022) — MultiBERTs, multi-seed training\n- Dehghani et al. (2021) — Benchmark Lottery\n- Biderman et al. (2024) — Evaluation reproducibility lessons\n- Vania et al. (2021) — IRT item properties in NLP\n- **Sclar et al. (2024, ICLR)** — Up to 76% accuracy swing from prompt formatting; directly relevant to prompt×item variance [Dream #3: all 3 tiers flagged as missing]\n- **Kunievsky & Evans (2025)** — Alternative decomposition: intent/articulation/model uncertainty; competing framework to G-theory [Dream #3: all 3 tiers flagged]\n- **Bui et al. (2025)** — Extreme seed sensitivity in fine-tuning (RTES variance=18.22 for RoBERTa on COPA) [Dream #3: relevant to exp-006]\n- **Jiang & Skorupski (2017)** — Logistic-link generalized G-theory for binary data [Dream #3 worst: methodological defense for REML on binary]\n- **Mushquash & O'Connor (2006)** — Binary-data G-theory [Dream #3: classical psychometrics gap]\n- **Shavelson et al. (1989)** — Binary response G-theory treatment [Dream #3: classical psychometrics]\n\n## Dream #3 Framing Directives (2026-05-21, D006)\nPost-analysis framing adjustments based on three-tier consistent feedback:\n1. **Center gradient + model×item as primary contributions** — infrastructure crossing is confirmatory secondary\n2. **Position explicitly as empirical extension of Mesting (2026)** with novel findings (model×item quantification, D-study out-of-sample validation, IRT comparison), not a new framework. Remove \"first\" claims where not defensible.\n3. **Scope Claim 2 to \"precision separability\"** — not \"infrastructure\" broadly. Single GPU architecture.\n4. **Item dominance is psychometrically expected** — contribution is quantification of magnitude, metric-conditionality, and D-study implications\n5. **Fine-tuning (exp-006) downgraded** to Discussion-section preliminary observation, not a numbered contribution\n6. **Add explicit judge-facet exclusion discussion** vs Mesting: we fix judge to isolate other factors; Mesting's 43.8% judge variance would dominate\n7. **Practitioner toolkit must be concrete**: specify released scripts, D-study calculator, budget lookup tables\n8. **Figures are non-negotiable**: 5 planned figures address all-tier \"zero figures\" criticism\n",
      "numLines": 178,
      "startLine": 1,
      "totalLines": 178
    }
  },
  "sourceToolAssistantUUID": "f8c71cc3-64a5-4c48-9769-61d60a3250e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T075006 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheor…",
  "leafUuid": "761fd288-ba2e-4a3b-84d2-4c61a97ad278",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate LLM evaluation variance analysis paper",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3"
}
```

---

### Tool result

_source line 13 · 2026-05-21T08:28:11.077Z_

<details><summary>↩ Tool result · `toolu_01WqCGApb4327pQPiCQWTn1z`</summary>

```text
1	[
2	  {
3	    "name": "exp-001: Full-scale 4-model MMLU precision study",
4	    "description": "4 models × 3 precisions × 6 prompts × 6 seeds × 3 temps × 4 orderings × 200 MMLU items。数据已收集完毕（Llama 239,200 + Gemma 172,800 + Mistral 259,200 + Qwen 259,200 = 930,400 total records）。Balanced cross-model analysis使用bf16 共享条件：432 conditions/model × 4 models × 200 items = 345,600 records。 核心数字已锁定。worst档新增两项robustness分析结果不理想： (a) leave-one-model-out matched-spec rerun显示G_item spread=0.058（>0.05）； (b) BF16-vs-FP16 sensitivity已完成确认precision=0.0006%（正面结果）。\n",
5	    "results": {
6	      "total_records": 930400,
7	      "balanced_cross_model_records": 345600,
8	      "total_conditions": 5184,
9	      "models_completed": 4,
10	      "cross_4model_item_id_pct": 42.1,
11	      "cross_4model_item_id_CI_95": [
12	        36.0,
13	        48.8
14	      ],
15	      "cross_4model_model_x_item_pct": 33.6,
16	      "cross_4model_model_x_item_CI_95": [
17	        28.4,
18	        37.9
19	      ],
20	      "cross_4model_G_item": 0.82,
21	      "cross_4model_G_item_CI_95": [
22	        0.782,
23	        0.861
24	      ],
25	      "d_study_3to4_predicted": 0.816,
26	      "d_study_3to4_actual": 0.82,
27	      "d_study_3to4_delta": 0.004,
28	      "single_model_llama_item_id_pct": 61.1,
29	      "per_model_interaction_mistral_pct": 29.25,
30	      "per_model_interaction_qwen_pct": 27.11,
31	      "per_model_interaction_gemma_pct": 23.95,
32	      "per_model_interaction_llama_pct": 19.69,
33	      "bf16_vs_fp16_precision_pct": 0.0006,
34	      "bf16_vs_fp16_precision_x_item_pct": 0.04,
35	      "infra_x_method_binary_pct": 0.08,
36	      "residual_pct": 19.5,
37	      "lomo_matched_spec_design": "bf16 × 4 prompts × 4 seeds × 2 temps × 2 orderings",
38	      "lomo_drop_mistral_G_item": 0.846,
39	      "lomo_drop_qwen_G_item": 0.834,
40	      "lomo_drop_gemma_G_item": 0.802,
41	      "lomo_drop_llama_G_item": 0.788,
42	      "lomo_spread": 0.058,
43	      "lomo_mean_G_item": 0.818,
44	      "lomo_sd_G_item": 0.026,
45	      "d_study_5model_G_item": 0.848,
46	      "d_study_8model_G_item": 0.893,
47	      "d_study_10model_G_item": 0.91
48	    },
49	    "tables": [
50	      {
51	        "name": "Table 1: Cross-model variance decomposition (4 models, MMLU, balanced bf16)",
52	        "data": {
53	          "columns": [
54	            "source",
55	            "pct",
56	            "CI_lower",
57	            "CI_upper"
58	          ],
59	          "rows": [
60	            [
61	              "item_id",
62	              42.1,
63	              36.0,
64	              48.8
65	            ],
66	            [
67	              "model_x_item",
68	              33.6,
69	              28.4,
70	              37.9
71	            ],
72	            [
73	              "residual",
74	              19.5,
75	              16.2,
76	              23.1
77	            ],
78	            [
79	              "prompt_x_item",
80	              4.6,
81	              3.1,
82	              6.4
83	            ],
84	            [
85	              "seed_x_item",
86	              4.7,
87	              3.2,
88	              6.5
89	            ],
90	            [
91	              "temperature",
92	              1.2,
93	              0.4,
94	              2.3
95	            ],
96	            [
97	              "model",
98	              0.8,
99	              0.1,
100	              2.1
101	            ],
102	            [
103	              "precision",
104	              0.0006,
105	              0.0,
106	              0.002
107	            ],
108	            [
109	              "other_interactions",
110	              0.5,
111	              0.1,
112	              1.2
113	            ]
114	          ]
115	        }
116	      },
117	      {
118	        "name": "Table 2: Leave-one-model-out matched-spec G_item",
119	        "data": {
120	          "columns": [
121	            "dropped_model",
122	            "G_item",
123	            "item_id_pct",
124	            "model_x_item_pct"
125	          ],
126	          "rows": [
127	            [
128	              "Mistral",
129	              0.846,
130	              44.8,
131	              28.3
132	            ],
133	            [
134	              "Qwen",
135	              0.834,
136	              43.2,
137	              30.1
138	            ],
139	            [
140	              "Gemma",
141	              0.802,
142	              40.5,
143	              35.8
144	            ],
145	            [
146	              "Llama",
147	              0.788,
148	              39.1,
149	              37.6
150	            ],
151	            [
152	              "All_4",
153	              0.82,
154	              42.1,
155	              33.6
156	            ]
157	          ]
158	        }
159	      },
160	      {
161	        "name": "Table 3: Per-model single-model variance decomposition",
162	        "data": {
163	          "columns": [
164	            "source",
165	            "llama_pct",
166	            "gemma_pct",
167	            "mistral_pct",
168	            "qwen_pct"
169	          ],
170	          "rows": [
171	            [
172	              "item_id",
173	              61.1,
174	              57.8,
175	              59.4,
176	              55.6
177	            ],
178	            [
179	              "residual",
180	              17.2,
181	              19.1,
182	              18.4,
183	              20.8
184	            ],
185	            [
186	              "precision_x_item",
187	              7.2,
188	              7.8,
189	              7.1,
190	              6.5
191	            ],
192	            [
193	              "prompt_x_item",
194	              4.6,
195	              5.3,
196	              4.9,
197	              6.2
198	            ],
199	            [
200	              "seed_x_item",
201	              4.7,
202	              4.5,
203	              4.6,
204	              5.1
205	            ],
206	            [
207	              "temperature_x_item",
208	              3.1,
209	              3.4,
210	              3.2,
211	              3.6
212	            ],
213	            [
214	              "temperature",
215	              1.2,
216	              1.1,
217	              1.5,
218	              1.2
219	            ],
220	            [
221	              "precision",
222	              0.5,
223	              0.6,
224	              0.5,
225	              0.7
226	            ]
227	          ]
228	        }
229	      }
230	    ],
231	    "figures": [],
232	    "analysis": "exp-001的锁定数字是worst档论文的foundation——model×item=33.6%和D-study Δ=0.004无论其他实验如何都是solid findings。leave-one-model-out matched-spec spread=0.058是worst档的核心concern：它意味着4-model estimate有~3%的standard deviation，reviewer可以argue point estimate不够precise。 Defense策略：(1) 所有4个子集都保持qualitative结论（item_id最大，model×item second largest），spread影响的是magnitude不是ranking；(2) D-study projection 清晰显示adding models monotonically improves G_item，当前4-model是under-powered 但方向正确；(3) unmatched analysis的spread仅0.023，matched的0.058部分归因于 reduced design（64 vs 432 conditions），真实spread可能介于两者之间。 BF16-vs-FP16 sensitivity确认FP32 anomaly是vLLM artifact（positive result）。\n\n\n核心cross-model数字已锁定不受worst档影响。worst档的关键问题在leave-one-model-out matched-spec rerun：初始unmatched analysis显示spread=0.023（看起来stable）， 但那是因为不同3-model子集使用了不同条件数（Gemma缺fp16→432 conditions/model vs其他648），设计不可比。matched-spec rerun统一使用最大公约数设计 （bf16 × 4 prompts × 4 seeds × 2 temps × 2 orderings = 64 conditions/model）， 条件数大幅减少使得估计精度下降。 Drop-Llama（spread最大端）G_item=0.788，因为Llama是interaction最低的模型 （19.69%），去掉它后剩余3模型（Mistral 29.25%、Qwen 27.11%、Gemma 23.95%） 的model×item更大，item difficulty generalizability更差。 Drop-Mistral（spread最小端）G_item=0.846，因为Mistral是interaction最高的模型 （29.25%），去掉它反而让剩余3模型的item ranking更一致。 Spread=0.058意味着G_item在[0.788, 0.846]区间内depending on model selection—— reviewer可以argue\"4个模型不够，G_item的point estimate不可靠\"。 但所有4个子集都保持G_item>0.78（>0.75阈值），item_id始终>35%且为最大source， 定性结论robust。这个fragility是real的，需要10+模型才能stabilize， 但在论文中可以honest报告并用D-study projection（10 models→G=0.910） 来argue方向是对的、只是当前sample不够大。\n"
233	  },
234	  {
235	    "name": "exp-001b: Item resampling stability test",
236	    "description": "3个独立200-item分层抽样（seeds 0, 7, 99）× Llama × 3 precisions × 3 prompts × 3 seeds × 2 orderings = 54 conditions/sample × 200 items = 10,800 records/sample。 Total 32,400 records。在worst档中，CV(item_id)=0.143，显示42%的point estimate 对item sampling敏感。\n",
237	    "results": {
238	      "total_samples": 3,
239	      "conditions_per_sample": 54,
240	      "records_per_sample": 10800,
241	      "total_records": 32400,
242	      "sample_seed0_item_id_pct": 61.1,
243	      "sample_seed7_item_id_pct": 52.8,
244	      "sample_seed99_item_id_pct": 70.4,
245	      "item_id_mean_pct": 61.4,
246	      "item_id_sd_pct": 8.8,
247	      "item_id_cv": 0.143,
248	      "sample_seed0_G_binary": 0.611,
249	      "sample_seed7_G_binary": 0.536,
250	      "sample_seed99_G_binary": 0.689,
251	      "G_binary_mean": 0.612,
252	      "G_binary_sd": 0.077,
253	      "G_binary_cv": 0.126,
254	      "sample_seed0_residual_pct": 17.2,
255	      "sample_seed7_residual_pct": 23.1,
256	      "sample_seed99_residual_pct": 12.8,
257	      "residual_cv": 0.293,
258	      "variance_ranking_preserved_all_samples": true,
259	      "item_id_always_largest": true,
260	      "profile_corr_seed0_seed7": 0.79,
261	      "profile_corr_seed0_seed99": 0.73,
262	      "profile_corr_seed7_seed99": 0.76,
263	      "avg_profile_corr": 0.76
264	    },
265	    "tables": [
266	      {
267	        "name": "Table 4: Resampling stability across 3 item draws (single-model Llama)",
268	        "data": {
269	          "columns": [
270	            "source",
271	            "seed0_pct",
272	            "seed7_pct",
273	            "seed99_pct",
274	            "mean_pct",
275	            "sd_pct",
276	            "cv"
277	          ],
278	          "rows": [
279	            [
280	              "item_id",
281	              61.1,
282	              52.8,
283	              70.4,
284	              61.4,
285	              8.8,
286	              0.143
287	            ],
288	            [
289	              "residual",
290	              17.2,
291	              23.1,
292	              12.8,
293	              17.7,
294	              5.2,
295	              0.291
296	            ],
297	            [
298	              "precision_x_item",
299	              7.2,
300	              8.7,
301	              5.6,
302	              7.2,
303	              1.6,
304	              0.217
305	            ],
306	            [
307	              "prompt_x_item",
308	              4.6,
309	              5.8,
310	              3.9,
311	              4.8,
312	              1.0,
313	              0.201
314	            ],
315	            [
316	              "seed_x_item",
317	              4.7,
318	              5.2,
319	              4.2,
320	              4.7,
321	              0.5,
322	              0.106
323	            ],
324	            [
325	              "temperature_x_item",
326	              3.1,
327	              3.3,
328	              2.7,
329	              3.0,
330	              0.3,
331	              0.1
332	            ],
333	            [
334	              "temperature",
335	              1.2,
336	              1.0,
337	              0.9,
338	              1.0,
339	              0.2,
340	              0.153
341	            ],
342	            [
343	              "precision",
344	              0.5,
345	              0.6,
346	              0.3,
347	              0.5,
348	              0.2,
349	              0.333
350	            ]
351	          ]
352	        }
353	      },
354	      {
355	        "name": "Table 5: G-coefficient stability across item draws",
356	        "data": {
357	          "columns": [
358	            "metric",
359	            "seed0_G",
360	            "seed7_G",
361	            "seed99_G",
362	            "mean_G",
363	            "sd_G",
364	            "cv"
365	          ],
366	          "rows": [
367	            [
368	              "binary",
369	              0.611,
370	              0.536,
371	              0.689,
372	              0.612,
373	              0.077,
374	              0.126
375	            ],
376	            [
377	              "text_exact",
378	              0.007,
379	              0.005,
380	              0.009,
381	              0.007,
382	              0.002,
383	              0.286
384	            ]
385	          ]
386	        }
387	      }
388	    ],
389	    "figures": [],
390	    "analysis": "CV=0.143直接影响headline claim的precision——论文不能报告\"item_id=42.1%\" 作为definitive number，需要报告\"42.1% [range across item samples: ~36-48%]\"。 但这与bootstrap CI [36.0, 48.8]一致，说明resampling instability和statistical uncertainty是同一量级的——bootstrap CI已经captures了item sampling variability。 正面spin：(1) item_id始终是largest source（even at 52.8%远超residual 23.1%）， 定性结论robust；(2) resampling instability本身reinforces G-theory的item-as-facet treatment——如果item sampling无关紧要，就不需要G-theory了； (3) G_binary的CV=0.126 < item_id的CV=0.143，reliability比raw variance %更stable。 Reviewer concern \"连自己的estimate都不stable\"可以用\"this is precisely why D-study budgets recommend 500+ items\"来回应。\n\n\n200 items是MMLU 14,042题的1.4%。即使分层抽样（按57个subjects），每个subject 内的difficulty分布仍有大量变异。seed 99抽到更多high-variance subjects （abstract_algebra, formal_logic, professional_medicine——这些subjects的item difficulty range极大，从trivial到near-impossible），导致item间方差膨胀至70.4%。 seed 7则抽到更多\"中等难度集中\"的subjects（high_school_biology, marketing）， item间差异较小，item_id降至52.8%。 CV=0.143意味着单次200-item抽样的item_id%有约14%的相对变异。 这不是catastrophic——variance ranking在所有3次抽样中保持（item_id始终最大）， 但足以让reviewer质疑\"42.1%\"这个具体数字。G系数的CV=0.126较低，说明 reliability estimate比variance percentage更robust——从0.536到0.689变化较大 但定性判断不变（全部<0.80阈值，需要more items）。 profile correlation平均0.76说明方差结构的shape有moderate一致性， 但不足以claim\"structure is invariant to item sampling\"。 关键defense：把instability本身spin为finding——\"item sampling is itself a major variance source, providing empirical justification for G-theory's item-as-facet treatment and D-study budgeting approach。\"\n"
391	  },
392	  {
393	    "name": "exp-002: Multi-benchmark replication (flat gradient)",
394	    "description": "4 models × 2 precisions (bf16/fp16) × 6 prompts × 6 seeds × 2 temperatures (T=0.0/T=0.7) × 4 orderings × 200 items on GSM8K, ARC-Challenge, HellaSwag。 Per benchmark: 4×2×6×6×2×4=2304 conditions × 200 items = 460,800 records。 Total: 1,382,400 records。Cross-model balanced analysis: bf16 only, 576 conditions/model × 4 × 200 = 230,400/benchmark。 结果：variance structure跨benchmark几乎不变，item_id range仅5.7pp， gradient narrative完全不成立。\n",
395	    "results": {
396	      "total_records_all_benchmarks": 1382400,
397	      "benchmarks_completed": 3,
398	      "mmlu_cross_item_id_pct": 42.1,
399	      "mmlu_cross_model_x_item_pct": 33.6,
400	      "mmlu_cross_residual_pct": 19.5,
401	      "mmlu_cross_G_item": 0.82,
402	      "gsm8k_cross_item_id_pct": 38.4,
403	      "gsm8k_cross_model_x_item_pct": 31.8,
404	      "gsm8k_cross_residual_pct": 22.6,
405	      "gsm8k_cross_prompt_x_item_pct": 8.4,
406	      "gsm8k_cross_seed_x_item_pct": 5.8,
407	      "gsm8k_cross_temperature_pct": 3.2,
408	      "gsm8k_cross_G_item": 0.682,
409	      "gsm8k_cross_G_binary_200items": 0.438,
410	      "gsm8k_overall_accuracy": 0.512,
411	      "arc_cross_item_id_pct": 44.1,
412	      "arc_cross_model_x_item_pct": 30.5,
413	      "arc_cross_residual_pct": 18.8,
414	      "arc_cross_prompt_x_item_pct": 5.2,
415	      "arc_cross_seed_x_item_pct": 4.6,
416	      "arc_cross_temperature_pct": 1.4,
417	      "arc_cross_G_item": 0.718,
418	      "arc_cross_G_binary_200items": 0.521,
419	      "arc_overall_accuracy": 0.548,
420	      "hellaswag_cross_item_id_pct": 41.8,
421	      "hellaswag_cross_model_x_item_pct": 35.2,
422	      "hellaswag_cross_residual_pct": 17.4,
423	      "hellaswag_cross_prompt_x_item_pct": 3.8,
424	      "hellaswag_cross_seed_x_item_pct": 4.2,
425	      "hellaswag_cross_temperature_pct": 0.8,
426	      "hellaswag_cross_G_item": 0.668,
427	      "hellaswag_cross_G_binary_200items": 0.492,
428	      "hellaswag_overall_accuracy": 0.621,
429	      "cross_bench_item_id_range_pp": 5.7,
430	      "cross_bench_item_id_min": 38.4,
431	      "cross_bench_item_id_max": 44.1,
432	      "cross_bench_model_x_item_range_pp": 4.7,
433	      "gradient_rank_knowledge_to_reasoning": null,
434	      "gradient_linear_fit_R2": 0.12,
435	      "separability_binary_mmlu_pct": 0.08,
436	      "separability_binary_gsm8k_pct": 3.6,
437	      "separability_binary_arc_pct": 2.4,
438	      "separability_binary_hellaswag_pct": 4.8,
439	      "separability_binary_max_pct": 4.8,
440	      "d_study_mmlu_510items_G": 0.8,
441	      "d_study_gsm8k_510items_G": 0.753,
442	      "d_study_arc_510items_G": 0.768,
443	      "d_study_hellaswag_510items_G": 0.742,
444	      "d_study_cross_bench_delta_max": 0.058,
445	      "d_study_cross_bench_delta_min": 0.032,
446	      "d_study_cross_bench_delta_mean": 0.047,
447	      "irt_gtheory_ratio_mmlu": 4.1,
448	      "irt_gtheory_ratio_gsm8k": 1.7,
449	      "irt_gtheory_ratio_arc": 2.5,
450	      "irt_gtheory_ratio_hellaswag": 1.6,
451	      "g_item_cross_bench_min": 0.668,
452	      "g_item_cross_bench_max": 0.82,
453	      "g_item_cross_bench_mean": 0.722,
454	      "mmlu_matched_2x2_item_id_pct": 43.8,
455	      "mmlu_matched_2x2_model_x_item_pct": 32.4,
456	      "mmlu_matched_2x2_delta_from_full": 1.7
457	    },
458	    "tables": [
459	      {
460	        "name": "Table 6: Cross-model variance decomposition by benchmark (4 models, bf16)",
461	        "data": {
462	          "columns": [
463	            "source",
464	            "mmlu_pct",
465	            "gsm8k_pct",
466	            "arc_pct",
467	            "hellaswag_pct",
468	            "range_pp"
469	          ],
470	          "rows": [
471	            [
472	              "item_id",
473	              42.1,
474	              38.4,
475	              44.1,
476	              41.8,
477	              5.7
478	            ],
479	            [
480	              "model_x_item",
481	              33.6,
482	              31.8,
483	              30.5,
484	              35.2,
485	              4.7
486	            ],
487	            [
488	              "residual",
489	              19.5,
490	              22.6,
491	              18.8,
492	              17.4,
493	              5.2
494	            ],
495	            [
496	              "prompt_x_item",
497	              4.6,
498	              8.4,
499	              5.2,
500	              3.8,
501	              4.6
502	            ],
503	            [
504	              "seed_x_item",
505	              4.7,
506	              5.8,
507	              4.6,
508	              4.2,
509	              1.6
510	            ],
511	            [
512	              "temperature",
513	              1.2,
514	              3.2,
515	              1.4,
516	              0.8,
517	              2.4
518	            ],
519	            [
520	              "model",
521	              0.8,
522	              1.2,
523	              0.9,
524	              0.6,
525	              0.6
526	            ],
527	            [
528	              "precision",
529	              0.0006,
530	              0.3,
531	              0.1,
532	              0.2,
533	              0.3
534	            ]
535	          ]
536	        }
537	      },
538	      {
539	        "name": "Table 7: G_item and IRT comparison by benchmark",
540	        "data": {
541	          "columns": [
542	            "benchmark",
543	            "G_item_4model",
544	            "G_binary_200items",
545	            "irt_items_needed",
546	            "gtheory_items_G80",
547	            "ratio"
548	          ],
549	          "rows": [
550	            [
551	              "MMLU",
552	              0.82,
553	              0.611,
554	              118,
555	              510,
556	              4.1
557	            ],
558	            [
559	              "GSM8K",
560	              0.682,
561	              0.438,
562	              286,
563	              486,
564	              1.7
565	            ],
566	            [
567	              "ARC-Challenge",
568	              0.718,
569	              0.521,
570	              178,
571	              448,
572	              2.5
573	            ],
574	            [
575	              "HellaSwag",
576	              0.668,
577	              0.492,
578	              312,
579	              502,
580	              1.6
581	            ]
582	          ]
583	        }
584	      },
585	      {
586	        "name": "Table 8: Cross-benchmark separability (binary, precision×methodology interaction)",
587	        "data": {
588	          "columns": [
589	            "benchmark",
590	            "prec_x_prompt_pct",
591	            "prec_x_seed_pct",
592	            "prec_x_temp_pct",
593	            "total_infra_x_method_pct"
594	          ],
595	          "rows": [
596	            [
597	              "MMLU",
598	              0.02,
599	              0.01,
600	              0.05,
601	              0.08
602	            ],
603	            [
604	              "GSM8K",
605	              1.2,
606	              0.8,
607	              1.6,
608	              3.6
609	            ],
610	            [
611	              "ARC-Challenge",
612	              0.9,
613	              0.5,
614	              1.0,
615	              2.4
616	            ],
617	            [
618	              "HellaSwag",
619	              1.6,
620	              1.1,
621	              2.1,
622	              4.8
623	            ]
624	          ]
625	        }
626	      },
627	      {
628	        "name": "Table 9: D-study cross-benchmark transfer error",
629	        "data": {
630	          "columns": [
631	            "benchmark",
632	            "mmlu_derived_G_at_510items",
633	            "actual_G_at_510items",
634	            "delta"
635	          ],
636	          "rows": [
637	            [
638	              "MMLU",
639	              0.8,
640	              0.8,
641	              0.0
642	            ],
643	            [
644	              "GSM8K",
645	              0.8,
646	              0.753,
647	              0.047
648	            ],
649	            [
650	              "ARC-Challenge",
651	              0.8,
652	              0.768,
653	              0.032
654	            ],
655	            [
656	              "HellaSwag",
657	              0.8,
658	              0.742,
659	              0.058
660	            ]
661	          ]
662	        }
663	      }
664	    ],
665	    "figures": [],
666	    "analysis": "exp-002是worst档叙事转向的关键实验。gradient死亡意味着原planned的 \"cross-benchmark variance gradient — the primary novel finding\"完全不可用。 但flat structure本身可以reframe： (1) Positive spin：\"variance structure is approximately benchmark-invariant\" → practitioners可以用MMLU结果cautiously extrapolate to other benchmarks。 这解决了一个practical question。 (2) D-study transfer error（Δ=0.03-0.06）限定了\"cautiously\"的程度—— MMLU-derived budgets会在其他benchmark上overestimate G by 3-6pp， 需要add 10-15% safety margin。 (3) IRT ratio的benchmark-dependence（1.6×-4.1×）是一个publishable finding 本身——解释了为什么field对\"IRT够不够\"的争论不收敛：答案是benchmark-dependent。 Separability failure across benchmarks（MMLU 0.08% vs HellaSwag 4.8%） means separability完全不能作为general claim，降为\"observed on MMLU under binary scoring; does not hold generally\"。 Net assessment: exp-002的data是有价值的，只是不支撑原叙事。reframe后 可以支撑contribution (3)（benchmark-insensitivity as positive）但forcing function是writing quality——flat results需要更skillful framing。\n\n\nGradient叙事死掉的核心原因：item_id跨4个benchmark的range仅5.7pp （38.4%-44.1%）。原假设是knowledge benchmarks（MMLU）有高item_id（>55%）， reasoning benchmarks（GSM8K）有低item_id（<30%），形成20+pp的gradient。 实际结果是所有benchmark都落在38-44%的狭窄区间内。 为什么flat？model×item交互在所有benchmark上都在30-36%——这意味着无论 task type如何，模型间的item difficulty ranking disagreement程度类似。 直觉上，这是因为7-9B模型在knowledge和reasoning tasks上都有类似程度的 model-specific strengths/weaknesses：Llama在MMLU的history和GSM8K的 word problems上都相对strong，Mistral在MMLU的STEM和GSM8K的multi-step上 都相对weak——model-specificity的pattern在task types之间有一致性。 G_item跨benchmark从0.668到0.820变化较大（range=0.152），但这主要由 residual差异驱动而非model×item差异。GSM8K和HellaSwag的G_item低 （0.668-0.682）是因为higher residual（22.6%和17.4%+更高的prompt×item）， 不是因为model×item更大。 IRT ratio在GSM8K（1.7×）和HellaSwag（1.6×）上collapse到<2×，原因是 这些benchmark的IRT也需要更多items（item discrimination更uniform， 2PL model的efficiency advantage减弱），所以分母增大、ratio压缩。 MMLU上IRT仍然只需~120 items因为items有strong discrimination gradients （从trivial到impossible跨57 subjects），2PL拟合效率高。 Cross-benchmark separability failure（max=4.8% on HellaSwag binary） 原因：HellaSwag的sentence completion任务对precision和temperature的 交互更敏感——不同precision下temperature>0生成的completions有更多 divergence，且binary scoring的粒度在这类任务上captures了更多差异。 D-study cross-bench Δ=0.032-0.058意味着MMLU-derived budgets在其他 benchmark上systematically overestimate reliability by 3-6pp。这是因为 MMLU的residual较低（19.5%）相对于GSM8K（22.6%）——更多unexplained variance意味着需要更多observations来stabilize。\n"
667	  },
668	  {
669	    "name": "exp-003: Multi-hardware G-study (partial)",
670	    "description": "原计划4 models × 2+ GPU types × 2 precisions × full crossing。 在worst档中，第二种GPU（RTX A6000 48GB）在deadline前4周获得， 仅完成2 models（Llama + Mistral）× 2 precisions（bf16/fp16）× 6 prompts × 6 seeds × 3 temps × 4 orderings × 200 items = 2 × 576 × 200 = 230,400 records。 Hardware × methodology interaction = 4.2% binary average，separability claim破裂。\n",
671	    "results": {
672	      "status": "PARTIAL",
673	      "gpu_types": [
674	        "RTX_PRO_6000_96GB",
675	        "RTX_A6000_48GB"
676	      ],
677	      "models_completed": 2,
678	      "models": [
679	        "Llama-3.1-8B-Instruct",
680	        "Mistral-7B-Instruct-v0.3"
681	      ],
682	      "total_records": 230400,
683	      "conditions_per_model": 576,
684	      "hardware_main_effect_pct": 1.8,
685	      "hardware_x_precision_pct": 0.9,
686	      "hardware_x_prompt_pct": 0.6,
687	      "hardware_x_seed_pct": 0.3,
688	      "hardware_x_temperature_pct": 1.4,
689	      "hardware_x_item_pct": 2.8,
690	      "total_hardware_x_methodology_pct": 4.2,
691	      "hardware_x_methodology_llama_pct": 3.8,
692	      "hardware_x_methodology_mistral_pct": 4.6,
693	      "single_gpu_infra_x_method_pct": 0.08,
694	      "multi_gpu_infra_x_method_pct": 4.2,
695	      "delta_pp": 4.12,
696	      "llama_pro6000_accuracy": 0.6814,
697	      "llama_a6000_accuracy": 0.6791,
698	      "llama_hardware_gap_pp": 0.23,
699	      "mistral_pro6000_accuracy": 0.6124,
700	      "mistral_a6000_accuracy": 0.6083,
701	      "mistral_hardware_gap_pp": 0.41,
702	      "G_binary_single_gpu": 0.611,
703	      "G_binary_two_gpu": 0.582,
704	      "G_delta": 0.029
705	    },
706	    "tables": [
707	      {
708	        "name": "Table 10: Hardware × methodology interaction breakdown (2 models, binary)",
709	        "data": {
710	          "columns": [
711	            "interaction_term",
712	            "llama_pct",
713	            "mistral_pct",
714	            "average_pct"
715	          ],
716	          "rows": [
717	            [
718	              "hardware_x_temperature",
719	              1.1,
720	              1.7,
721	              1.4
722	            ],
723	            [
724	              "hardware_x_precision",
725	              0.7,
726	              1.1,
727	              0.9
728	            ],
729	            [
730	              "hardware_x_prompt",
731	              0.5,
732	              0.7,
733	              0.6
734	            ],
735	            [
736	              "hardware_x_seed",
737	              0.2,
738	              0.4,
739	              0.3
740	            ],
741	            [
742	              "hardware_x_item",
743	              2.4,
744	              3.2,
745	              2.8
746	            ],
747	            [
748	              "hardware_main",
749	              1.3,
750	              2.3,
751	              1.8
752	            ],
753	            [
754	              "total_hardware_related",
755	              6.2,
756	              9.4,
757	              7.8
758	            ],
759	            [
760	              "total_hardware_x_methodology",
761	              3.8,
762	              4.6,
763	              4.2
764	            ]
765	          ]
766	        }
767	      }
768	    ],
769	    "figures": [],
770	    "analysis": "exp-003的partial completion足以kill separability claim但不够做full hardware G-study。只有2个模型意味着hardware×model interaction无法properly estimate。 但data is sufficient to downgrade separability from \"claim\" to \"observation limited to single-GPU environments\"。 论文framing：在Methods中honest报告\"hardware crossing was partially completed (2 of 4 models)\"，在Results中报告4.2% interaction as \"preliminary evidence that separability does not hold across GPU architectures\"，在Discussion中 qualify all prior separability statements to \"single-GPU, single-architecture\"。 这不fatal——separability在worst档叙事中已经不是contribution了。\n\n\nHardware×methodology interaction从single-GPU的0.08%跳至multi-GPU的4.2%， 原因是两种GPU有不同的CUDA kernel implementations（RTX PRO 6000使用 sm_89 Ada Lovelace kernels，A6000使用sm_86 Ampere kernels）。 BF16 matrix multiply的rounding behavior在两种架构上不同——不是precision 本身的问题（bf16 spec相同），而是kernel-level implementation差异导致 少量items在一个GPU上答对、另一个上答错。 hardware×temperature=1.4%是最大sub-interaction，因为temperature>0时的 sampling受CUDA RNG implementation影响，不同GPU的cuRAND版本产生 不同的pseudo-random sequences（即使seed相同）。 hardware×item=2.8%反映了~5-8个items在两GPU间有consistently不同的 答案——这些items恰好在model的decision boundary上，kernel-level numerical differences足以flip prediction。 Mistral（4.6%）比Llama（3.8%）的hardware interaction更大，因为Mistral accuracy更低（61.2%），更多items在decision boundary附近。 这个结果对separability是definitive negative：\"infrastructure×methodology ≈0%\"只在single-GPU上成立。跨GPU，interaction是non-negligible的。 但4.2%仍然是minor relative to item_id（42.1%）和model×item（33.6%）， 所以the hierarchy is preserved——hardware interaction doesn't dominate。\n"
771	  },
772	  {
773	    "name": "exp-004: Comprehensive analysis",
774	    "description": "基于exp-001/001b/002/003数据的全面分析。Worst档中exp-003仅有partial data， 但exp-001和exp-002完整。可执行13/17 planned analyses。 核心输出：IRT vs G-theory对比（benchmark-dependent ratio），D-study cross-benchmark transfer analysis，完整robustness package。\n",
775	    "results": {
776	      "planned_analyses": 17,
777	      "executable_analyses": 13,
778	      "blocked_analyses": 4,
779	      "blocked_list": [
780	        "full hardware G-study",
781	        "hardware ranking stability",
782	        "hardware logprob analysis",
783	        "hardware cost optimization"
784	      ],
785	      "model_as_facet_item_id_pct": 42.1,
786	      "model_as_facet_model_x_item_pct": 33.6,
787	      "model_as_facet_G_item": 0.82,
788	      "bootstrap_n": 1000,
789	      "item_id_CI_95": [
790	        36.0,
791	        48.8
792	      ],
793	      "model_x_item_CI_95": [
794	        28.4,
795	        37.9
796	      ],
797	      "residual_CI_95": [
798	        16.2,
799	        23.1
800	      ],
801	      "G_item_CI_95": [
802	        0.782,
803	        0.861
804	      ],
805	      "G_binary_CI_95": [
806	        0.571,
807	        0.652
808	      ],
809	      "d_study_practical_items_G80_mmlu": 510,
810	      "d_study_practical_items_G80_gsm8k": 624,
811	      "d_study_practical_items_G80_arc": 538,
812	      "d_study_practical_items_G80_hellaswag": 652,
813	      "d_study_cross_bench_delta_range": [
814	        0.032,
815	        0.058
816	      ],
817	      "d_study_14k_mmlu_G": 0.972,
818	      "reml_henderson_max_diff_pp": 0.4,
819	      "reml_convergence_iterations": 500,
820	      "reml_practical_convergence_delta": 0.003,
821	      "irt_gtheory_ratio_mmlu": 4.1,
822	      "irt_gtheory_ratio_gsm8k": 1.7,
823	      "irt_gtheory_ratio_arc": 2.5,
824	      "irt_gtheory_ratio_hellaswag": 1.6,
825	      "irt_gtheory_ratio_mean": 2.5,
826	      "irt_gtheory_ratio_sd": 1.14,
827	      "min_detectable_interaction_pct": 0.8,
828	      "power_at_1pct_interaction": 0.94,
829	      "power_at_5pct_interaction": 0.99,
830	      "G_all_random": 0.611,
831	      "G_temp_fixed": 0.634,
832	      "G_ordering_fixed": 0.645,
833	      "G_both_fixed": 0.664,
834	      "fixed_random_max_delta": 0.053,
835	      "bernoulli_obs_variance_corr": 0.91,
836	      "null_sim_item_id_pct": 0.08,
837	      "obs_to_bernoulli_ratio": 1.0008,
838	      "bootstrap_jackknife_CI_ratio_mean": 1.02,
839	      "bootstrap_jackknife_CI_ratio_range": [
840	        0.96,
841	        1.04
842	      ],
843	      "mmlu_2x2_vs_3x3_max_delta_pp": 1.7,
844	      "mmlu_14k_items_G_projected": 0.972,
845	      "logprob_mmlu_item_id_pct": 48.3,
846	      "logprob_gsm8k_item_id_pct": 44.8,
847	      "logprob_arc_item_id_pct": 46.1,
848	      "logprob_hellaswag_item_id_pct": 45.9,
849	      "logprob_cross_bench_range_pp": 3.5,
850	      "gpu_hours_G80_mmlu": 340,
851	      "gpu_hours_G80_gsm8k": 415,
852	      "gpu_hours_G80_hellaswag": 430,
853	      "gpu_hours_G90_mmlu": 890
854	    },
855	    "tables": [
856	      {
857	        "name": "Table 11: IRT vs G-theory item requirements by benchmark",
858	        "data": {
859	          "columns": [
860	            "benchmark",
861	            "irt_2pl_items",
862	            "gtheory_practical_items",
863	            "ratio",
864	            "gtheory_accounts_for"
865	          ],
866	          "rows": [
867	            [
868	              "MMLU",
869	              118,
870	              510,
871	              4.1,
872	              "prompt + seed + ordering + temp + prec"
873	            ],
874	            [
875	              "GSM8K",
876	              286,
877	              486,
878	              1.7,
879	              "same facets; IRT also needs more items"
880	            ],
881	            [
882	              "ARC-Challenge",
883	              178,
884	              448,
885	              2.5,
886	              "same"
887	            ],
888	            [
889	              "HellaSwag",
890	              312,
891	              502,
892	              1.6,
893	              "same; IRT needs most items here"
894	            ]
895	          ]
896	        }
897	      },
898	      {
899	        "name": "Table 12: D-study budget recommendations by benchmark (G≥0.80, practical)",
900	        "data": {
901	          "columns": [
902	            "benchmark",
903	            "items",
904	            "prompts",
905	            "seeds",
906	            "G_projected",
907	            "CI_95"
908	          ],
909	          "rows": [
910	            [
911	              "MMLU",
912	              510,
913	              2,
914	              3,
915	              0.8,
916	              "[0.782, 0.825]"
917	            ],
918	            [
919	              "GSM8K",
920	              624,
921	              3,
922	              4,
923	              0.801,
924	              "[0.774, 0.831]"
925	            ],
926	            [
927	              "ARC-Challenge",
928	              538,
929	              2,
930	              3,
931	              0.8,
932	              "[0.778, 0.826]"
933	            ],
934	            [
935	              "HellaSwag",
936	              652,
937	              3,
938	              4,
939	              0.802,
940	              "[0.771, 0.838]"
941	            ]
942	          ]
943	        }
944	      },
945	      {
946	        "name": "Table 13: Methodological robustness summary",
947	        "data": {
948	          "columns": [
949	            "analysis",
950	            "result",
951	            "status"
952	          ],
953	          "rows": [
954	            [
955	              "Binary not artifact (null sim)",
956	              "item_id=0.08% vs obs 61.1% (737×)",
957	              "PASS"
958	            ],
959	            [
960	              "Fixed vs random sensitivity",
961	              "max Δ(G)=0.053",
962	              "PASS"
963	            ],
964	            [
965	              "Bootstrap = Jackknife CIs",
966	              "ratio range [0.96, 1.04]",
967	              "PASS"
968	            ],
969	            [
970	              "REML vs Henderson I",
971	              "max diff < 0.4pp",
972	              "PASS"
973	            ],
974	            [
975	              "Temperature stratification",
976	              "binary G: 0.760→0.549 (T=0→0.7)",
977	              "PASS"
978	            ],
979	            [
980	              "Bernoulli variance correlation",
981	              "r=0.91 (item variance partly mechanical)",
982	              "NOTED"
983	            ],
984	            [
985	              "D-study cross-benchmark transfer",
986	              "Δ=0.032-0.058",
987	              "CAVEAT"
988	            ],
989	            [
990	              "Leave-one-model-out matched",
991	              "spread=0.058",
992	              "CAVEAT"
993	            ]
994	          ]
995	        }
996	      }
997	    ],
998	    "figures": [],
999	    "analysis": "exp-004在worst档中的关键产出是benchmark-conditional IRT ratio——这是 新发现，解释了field对\"IRT够不够\"的长期争论。可以claim：\"The IRT-G-theory gap is benchmark-dependent, ranging from 1.6× (HellaSwag) to 4.1× (MMLU), because IRT item parameters (discrimination, difficulty) vary across task types\"。这不需要gradient叙事，是self-contained的。 D-study cross-benchmark transfer analysis（Δ=0.03-0.06）is nuanced： 正面解读是MMLU budgets are \"approximately right\" (within 6pp G)； 负面解读是they're \"not directly transferable\"。论文adopt中间立场： \"MMLU-derived budgets provide a lower bound; benchmark-specific calibration improves precision by 3-6pp G\"。 Robustness package的6个PASS + 2个CAVEAT provides methodological credibility。 CAVEAT items (D-study transfer, LOMO) are discussed honestly rather than hidden。\n\n\nexp-004的analysis在worst档中产出两类结果： (1) Robust surviving findings（不受数据缺失影响）：IRT vs G-theory对比 在MMLU上4.1×（locked），但cross-benchmark显示ratio从1.6×到4.1×—— reviewer会说\"so the 3-4× claim is only valid for MMLU\"。ratio collapse的 原因：在reasoning benchmarks上，IRT的2PL model fit效率降低（items have 更uniform discrimination，lower slope parameters），IRT自己也需要更多items （GSM8K: 286 items vs MMLU: 118 items），所以G-theory的extra cost 相对缩小。论文可以claim \"3.6-4.4× on MMLU\" and \"1.6-4.1× benchmark- dependent range\"——后者本身是informative finding。 (2) Weakened findings：D-study cross-benchmark transfer Δ=0.03-0.06 意味着MMLU budgets不能直接apply to other benchmarks（会high by 3-6pp G）。 这undercuts contribution (3)的\"practitioners can extrapolate\"——需要加 significant caveat \"with 10-15% safety margin\"。 Robustness package全部基于exp-001 Llama数据，fully intact：binary not artifact（null sim 0.08%），fixed vs random insensitive（Δ<0.053）， bootstrap=jackknife（ratio 0.96-1.04），REML confirms Henderson I（<0.4pp）。 这些是论文的guaranteed floor——无论worst scenario多bad，robustness is there。 Logprob analysis跨benchmarks显示更tight的range（3.5pp vs binary的5.7pp）， suggesting logprob-based scoring reduces benchmark-dependence。This is a minor but novel observation that can go in Discussion。\n"
1000	  },
1001	  {
1002	    "name": "exp-005: 14B model extension",
1003	    "description": "Qwen3-14B和DeepSeek-R1-Distill-14B在datacenter GPU上的BF16/FP16测试。 Worst档中未执行——deps on exp-003 timeline + 无可用48GB+ GPU时间。\n",
1004	    "results": {
1005	      "status": "NOT_COMPLETED",
1006	      "records_collected": 0,
1007	      "blocking_reason": "exp-003在deadline前4周才partially完成，exp-005的protocol 依赖exp-003确定的multi-hardware procedure。同时14B模型需要 ~24GB VRAM（bf16），PRO 6000可以跑但被P0实验占满。 无法在AAAI deadline前执行。\n"
1008	    },
1009	    "tables": [],
1010	    "figures": [],
1011	    "analysis": "不fatal。论文scope明确为\"7-9B open-weight models\"。14B extension 适合ACL ARR camera-ready或后续独立paper。\n\n\nexp-005的timeline依赖链：exp-003 partial completion → protocol finalization → 14B model runs。exp-003在T-4周才完成，来不及做exp-005的full crossing。 此外，14B模型的inference latency比8B高~1.8×，即使有GPU也难在deadline内 完成576 conditions × 2 models × 200 items = 230,400 records。 对论文的影响：所有结论限于7-9B模型规模。reviewer concern \"scale validation\" 只能在Limitations中acknowledge，argue \"7-9B是最commonly used open-weight model class\"。\n"
1012	  },
1013	  {
1014	    "name": "exp-006: Fine-tuning G-study",
1015	    "description": "RoBERTa-large在SST-2/MNLI/RTE/COPA上的fine-tuning方差分解。 Worst档中未执行——P1优先级，GPU budget被P0消耗。\n",
1016	    "results": {
1017	      "status": "NOT_COMPLETED",
1018	      "records_collected": 0,
1019	      "blocking_reason": "P1 priority。P0实验（exp-001 ~100h + exp-002 ~200h + exp-003 ~60h partial） 消耗了大部分GPU budget。1,728次fine-tuning runs × ~15min ≈ 430 GPU-hours 无法accommodate。\n"
1020	    },
1021	    "tables": [],
1022	    "figures": [],
1023	    "analysis": "零影响。在Discussion中mention \"extending G-theory to fine-tuning variance is natural future work; Dodge et al. (2020) and Bui et al. (2025) provide preliminary evidence that seed/LR dominate fine-tuning variance\"。\n\n\nPer D006 framing directive #5，fine-tuning已降级为Discussion-section preliminary observation，不是numbered contribution。即使完成，encoder-only RoBERTa的fine-tuning与decoder LLM inference的methodological gap也会被 reviewer指出。在worst档reframed narrative（MMLU case study + IRT comparison） 中，fine-tuning完全outside scope。\n"
1024	  },
1025	  {
1026	    "name": "exp-007: LayerCast precision mitigation",
1027	    "description": "LayerCast（FP16 storage + FP32 compute）作为额外precision条件。 P2优先级，worst档中未执行。\n",
1028	    "results": {
1029	      "status": "NOT_COMPLETED",
1030	      "records_collected": 0,
1031	      "blocking_reason": "P2 priority, not attempted within AAAI timeline"
1032	    },
1033	    "tables": [],
1034	    "figures": [],
1035	    "analysis": "零影响。Precision在bf16/fp16上已经是non-issue（0.0006%）， LayerCast实验变得moot。\n\n\nLayerCast是mitigation strategy evaluation，不是core finding。 BF16-vs-FP16 sensitivity已显示precision effect=0.0006%（接近zero）， LayerCast的additional data point价值marginal——precision已经不是 variance source。可以在Discussion中cite Yuan et al. (2025)的 LayerCast results as \"practitioners can further reduce precision variance via mixed-precision strategies\"。\n"
1036	  },
1037	  {
1038	    "name": "exp-008: MATH benchmark extension",
1039	    "description": "MATH benchmark（200 items）测试reasoning-heavy任务的variance structure。 P2优先级且deps on exp-002，worst档中未执行。\n",
1040	    "results": {
1041	      "status": "NOT_COMPLETED",
1042	      "records_collected": 0,
1043	      "blocking_reason": "P2 priority。Deps on exp-002 pipeline（已完成但consumed timeline）。 MATH的chain-of-thought generation需要significantly longer inference time （avg ~45 tokens vs MMLU ~1 token），200h GPU budget已用尽。\n"
1044	    },
1045	    "tables": [],
1046	    "figures": [],
1047	    "analysis": "Marginal impact。4个benchmarks showing flat structure已经支撑 \"benchmark-insensitivity\" reframe。MATH would be 5th data point but not change the conclusion。适合ACL ARR补充。\n\nexp-002已经覆盖了GSM8K（math reasoning）、ARC（science reasoning）、 HellaSwag（commonsense），增加MATH的marginal value在worst档flat gradient 下更低——不会出现新pattern，只会是another data point在38-44% item_id区间内。 如果需要bolster \"benchmark-insensitivity\" claim，现有4个benchmarks （MMLU + 3 from exp-002）已经sufficient。\n"
1048	  }
1049	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "205be5b8-e484-444c-b459-05b770425772",
  "isSidechain": false,
  "promptId": "9d021380-77fd-4766-a060-794a49f7c1c1",
  "type": "user",
  "uuid": "621a6489-875f-4237-aec5-b8cbed943217",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"exp-001: Full-scale 4-model MMLU precision study\",\n    \"description\": \"4 models × 3 precisions × 6 prompts × 6 seeds × 3 temps × 4 orderings × 200 MMLU items。数据已收集完毕（Llama 239,200 + Gemma 172,800 + Mistral 259,200 + Qwen 259,200 = 930,400 total records）。Balanced cross-model analysis使用bf16 共享条件：432 conditions/model × 4 models × 200 items = 345,600 records。 核心数字已锁定。worst档新增两项robustness分析结果不理想： (a) leave-one-model-out matched-spec rerun显示G_item spread=0.058（>0.05）； (b) BF16-vs-FP16 sensitivity已完成确认precision=0.0006%（正面结果）。\\n\",\n    \"results\": {\n      \"total_records\": 930400,\n      \"balanced_cross_model_records\": 345600,\n      \"total_conditions\": 5184,\n      \"models_completed\": 4,\n      \"cross_4model_item_id_pct\": 42.1,\n      \"cross_4model_item_id_CI_95\": [\n        36.0,\n        48.8\n      ],\n      \"cross_4model_model_x_item_pct\": 33.6,\n      \"cross_4model_model_x_item_CI_95\": [\n        28.4,\n        37.9\n      ],\n      \"cross_4model_G_item\": 0.82,\n      \"cross_4model_G_item_CI_95\": [\n        0.782,\n        0.861\n      ],\n      \"d_study_3to4_predicted\": 0.816,\n      \"d_study_3to4_actual\": 0.82,\n      \"d_study_3to4_delta\": 0.004,\n      \"single_model_llama_item_id_pct\": 61.1,\n      \"per_model_interaction_mistral_pct\": 29.25,\n      \"per_model_interaction_qwen_pct\": 27.11,\n      \"per_model_interaction_gemma_pct\": 23.95,\n      \"per_model_interaction_llama_pct\": 19.69,\n      \"bf16_vs_fp16_precision_pct\": 0.0006,\n      \"bf16_vs_fp16_precision_x_item_pct\": 0.04,\n      \"infra_x_method_binary_pct\": 0.08,\n      \"residual_pct\": 19.5,\n      \"lomo_matched_spec_design\": \"bf16 × 4 prompts × 4 seeds × 2 temps × 2 orderings\",\n      \"lomo_drop_mistral_G_item\": 0.846,\n      \"lomo_drop_qwen_G_item\": 0.834,\n      \"lomo_drop_gemma_G_item\": 0.802,\n      \"lomo_drop_llama_G_item\": 0.788,\n      \"lomo_spread\": 0.058,\n      \"lomo_mean_G_item\": 0.818,\n      \"lomo_sd_G_item\": 0.026,\n      \"d_study_5model_G_item\": 0.848,\n      \"d_study_8model_G_item\": 0.893,\n      \"d_study_10model_G_item\": 0.91\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: Cross-model variance decomposition (4 models, MMLU, balanced bf16)\",\n        \"data\": {\n          \"columns\": [\n            \"source\",\n            \"pct\",\n            \"CI_lower\",\n            \"CI_upper\"\n          ],\n          \"rows\": [\n            [\n              \"item_id\",\n              42.1,\n              36.0,\n              48.8\n            ],\n            [\n              \"model_x_item\",\n              33.6,\n              28.4,\n              37.9\n            ],\n            [\n              \"residual\",\n              19.5,\n              16.2,\n              23.1\n            ],\n            [\n              \"prompt_x_item\",\n              4.6,\n              3.1,\n              6.4\n            ],\n            [\n              \"seed_x_item\",\n              4.7,\n              3.2,\n              6.5\n            ],\n            [\n              \"temperature\",\n              1.2,\n              0.4,\n              2.3\n            ],\n            [\n              \"model\",\n              0.8,\n              0.1,\n              2.1\n            ],\n            [\n              \"precision\",\n              0.0006,\n              0.0,\n              0.002\n            ],\n            [\n              \"other_interactions\",\n              0.5,\n              0.1,\n              1.2\n            ]\n          ]\n        }\n      },\n      {\n        \"name\": \"Table 2: Leave-one-model-out matched-spec G_item\",\n        \"data\": {\n          \"columns\": [\n            \"dropped_model\",\n            \"G_item\",\n            \"item_id_pct\",\n            \"model_x_item_pct\"\n          ],\n          \"rows\": [\n            [\n              \"Mistral\",\n              0.846,\n              44.8,\n              28.3\n            ],\n            [\n              \"Qwen\",\n              0.834,\n              43.2,\n              30.1\n            ],\n            [\n              \"Gemma\",\n              0.802,\n              40.5,\n              35.8\n            ],\n            [\n              \"Llama\",\n              0.788,\n              39.1,\n              37.6\n            ],\n            [\n              \"All_4\",\n              0.82,\n              42.1,\n              33.6\n            ]\n          ]\n        }\n      },\n      {\n        \"name\": \"Table 3: Per-model single-model variance decomposition\",\n        \"data\": {\n          \"columns\": [\n            \"source\",\n            \"llama_pct\",\n            \"gemma_pct\",\n            \"mistral_pct\",\n            \"qwen_pct\"\n          ],\n          \"rows\": [\n            [\n              \"item_id\",\n              61.1,\n              57.8,\n              59.4,\n              55.6\n            ],\n            [\n              \"residual\",\n              17.2,\n              19.1,\n              18.4,\n              20.8\n            ],\n            [\n              \"precision_x_item\",\n              7.2,\n              7.8,\n              7.1,\n              6.5\n            ],\n            [\n              \"prompt_x_item\",\n              4.6,\n              5.3,\n              4.9,\n              6.2\n            ],\n            [\n              \"seed_x_item\",\n              4.7,\n              4.5,\n              4.6,\n              5.1\n            ],\n            [\n              \"temperature_x_item\",\n              3.1,\n              3.4,\n              3.2,\n              3.6\n            ],\n            [\n              \"temperature\",\n              1.2,\n              1.1,\n              1.5,\n              1.2\n            ],\n            [\n              \"precision\",\n              0.5,\n              0.6,\n              0.5,\n              0.7\n            ]\n          ]\n        }\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-001的锁定数字是worst档论文的foundation——model×item=33.6%和D-study Δ=0.004无论其他实验如何都是solid findings。leave-one-model-out matched-spec spread=0.058是worst档的核心concern：它意味着4-model estimate有~3%的standard deviation，reviewer可以argue point estimate不够precise。 Defense策略：(1) 所有4个子集都保持qualitative结论（item_id最大，model×item second largest），spread影响的是magnitude不是ranking；(2) D-study projection 清晰显示adding models monotonically improves G_item，当前4-model是under-powered 但方向正确；(3) unmatched analysis的spread仅0.023，matched的0.058部分归因于 reduced design（64 vs 432 conditions），真实spread可能介于两者之间。 BF16-vs-FP16 sensitivity确认FP32 anomaly是vLLM artifact（positive result）。\\n\\n\\n核心cross-model数字已锁定不受worst档影响。worst档的关键问题在leave-one-model-out matched-spec rerun：初始unmatched analysis显示spread=0.023（看起来stable）， 但那是因为不同3-model子集使用了不同条件数（Gemma缺fp16→432 conditions/model vs其他648），设计不可比。matched-spec rerun统一使用最大公约数设计 （bf16 × 4 prompts × 4 seeds × 2 temps × 2 orderings = 64 conditions/model）， 条件数大幅减少使得估计精度下降。 Drop-Llama（spread最大端）G_item=0.788，因为Llama是interaction最低的模型 （19.69%），去掉它后剩余3模型（Mistral 29.25%、Qwen 27.11%、Gemma 23.95%） 的model×item更大，item difficulty generalizability更差。 Drop-Mistral（spread最小端）G_item=0.846，因为Mistral是interaction最高的模型 （29.25%），去掉它反而让剩余3模型的item ranking更一致。 Spread=0.058意味着G_item在[0.788, 0.846]区间内depending on model selection—— reviewer可以argue\\\"4个模型不够，G_item的point estimate不可靠\\\"。 但所有4个子集都保持G_item>0.78（>0.75阈值），item_id始终>35%且为最大source， 定性结论robust。这个fragility是real的，需要10+模型才能stabilize， 但在论文中可以honest报告并用D-study projection（10 models→G=0.910） 来argue方向是对的、只是当前sample不够大。\\n\"\n  },\n  {\n    \"name\": \"exp-001b: Item resampling stability test\",\n    \"description\": \"3个独立200-item分层抽样（seeds 0, 7, 99）× Llama × 3 precisions × 3 prompts × 3 seeds × 2 orderings = 54 conditions/sample × 200 items = 10,800 records/sample。 Total 32,400 records。在worst档中，CV(item_id)=0.143，显示42%的point estimate 对item sampling敏感。\\n\",\n    \"results\": {\n      \"total_samples\": 3,\n      \"conditions_per_sample\": 54,\n      \"records_per_sample\": 10800,\n      \"total_records\": 32400,\n      \"sample_seed0_item_id_pct\": 61.1,\n      \"sample_seed7_item_id_pct\": 52.8,\n      \"sample_seed99_item_id_pct\": 70.4,\n      \"item_id_mean_pct\": 61.4,\n      \"item_id_sd_pct\": 8.8,\n      \"item_id_cv\": 0.143,\n      \"sample_seed0_G_binary\": 0.611,\n      \"sample_seed7_G_binary\": 0.536,\n      \"sample_seed99_G_binary\": 0.689,\n      \"G_binary_mean\": 0.612,\n      \"G_binary_sd\": 0.077,\n      \"G_binary_cv\": 0.126,\n      \"sample_seed0_residual_pct\": 17.2,\n      \"sample_seed7_residual_pct\": 23.1,\n      \"sample_seed99_residual_pct\": 12.8,\n      \"residual_cv\": 0.293,\n      \"variance_ranking_preserved_all_samples\": true,\n      \"item_id_always_largest\": true,\n      \"profile_corr_seed0_seed7\": 0.79,\n      \"profile_corr_seed0_seed99\": 0.73,\n      \"profile_corr_seed7_seed99\": 0.76,\n      \"avg_profile_corr\": 0.76\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Resampling stability across 3 item draws (single-model Llama)\",\n        \"data\": {\n          \"columns\": [\n            \"source\",\n            \"seed0_pct\",\n            \"seed7_pct\",\n            \"seed99_pct\",\n            \"mean_pct\",\n            \"sd_pct\",\n            \"cv\"\n          ],\n          \"rows\": [\n            [\n              \"item_id\",\n              61.1,\n              52.8,\n              70.4,\n              61.4,\n              8.8,\n              0.143\n            ],\n            [\n              \"residual\",\n              17.2,\n              23.1,\n              12.8,\n              17.7,\n              5.2,\n              0.291\n            ],\n            [\n              \"precision_x_item\",\n              7.2,\n              8.7,\n              5.6,\n              7.2,\n              1.6,\n              0.217\n            ],\n            [\n              \"prompt_x_item\",\n              4.6,\n              5.8,\n              3.9,\n              4.8,\n              1.0,\n              0.201\n            ],\n            [\n              \"seed_x_item\",\n              4.7,\n              5.2,\n              4.2,\n              4.7,\n              0.5,\n              0.106\n            ],\n            [\n              \"temperature_x_item\",\n              3.1,\n              3.3,\n              2.7,\n              3.0,\n              0.3,\n              0.1\n            ],\n            [\n              \"temperature\",\n              1.2,\n              1.0,\n              0.9,\n              1.0,\n              0.2,\n              0.153\n            ],\n            [\n              \"precision\",\n              0.5,\n              0.6,\n              0.3,\n              0.5,\n              0.2,\n              0.333\n            ]\n          ]\n        }\n      },\n      {\n        \"name\": \"Table 5: G-coefficient stability across item draws\",\n        \"data\": {\n          \"columns\": [\n            \"metric\",\n            \"seed0_G\",\n            \"seed7_G\",\n            \"seed99_G\",\n            \"mean_G\",\n            \"sd_G\",\n            \"cv\"\n          ],\n          \"rows\": [\n            [\n              \"binary\",\n              0.611,\n              0.536,\n              0.689,\n              0.612,\n              0.077,\n              0.126\n            ],\n            [\n              \"text_exact\",\n              0.007,\n              0.005,\n              0.009,\n              0.007,\n              0.002,\n              0.286\n            ]\n          ]\n        }\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"CV=0.143直接影响headline claim的precision——论文不能报告\\\"item_id=42.1%\\\" 作为definitive number，需要报告\\\"42.1% [range across item samples: ~36-48%]\\\"。 但这与bootstrap CI [36.0, 48.8]一致，说明resampling instability和statistical uncertainty是同一量级的——bootstrap CI已经captures了item sampling variability。 正面spin：(1) item_id始终是largest source（even at 52.8%远超residual 23.1%）， 定性结论robust；(2) resampling instability本身reinforces G-theory的item-as-facet treatment——如果item sampling无关紧要，就不需要G-theory了； (3) G_binary的CV=0.126 < item_id的CV=0.143，reliability比raw variance %更stable。 Reviewer concern \\\"连自己的estimate都不stable\\\"可以用\\\"this is precisely why D-study budgets recommend 500+ items\\\"来回应。\\n\\n\\n200 items是MMLU 14,042题的1.4%。即使分层抽样（按57个subjects），每个subject 内的difficulty分布仍有大量变异。seed 99抽到更多high-variance subjects （abstract_algebra, formal_logic, professional_medicine——这些subjects的item difficulty range极大，从trivial到near-impossible），导致item间方差膨胀至70.4%。 seed 7则抽到更多\\\"中等难度集中\\\"的subjects（high_school_biology, marketing）， item间差异较小，item_id降至52.8%。 CV=0.143意味着单次200-item抽样的item_id%有约14%的相对变异。 这不是catastrophic——variance ranking在所有3次抽样中保持（item_id始终最大）， 但足以让reviewer质疑\\\"42.1%\\\"这个具体数字。G系数的CV=0.126较低，说明 reliability estimate比variance percentage更robust——从0.536到0.689变化较大 但定性判断不变（全部<0.80阈值，需要more items）。 profile correlation平均0.76说明方差结构的shape有moderate一致性， 但不足以claim\\\"structure is invariant to item sampling\\\"。 关键defense：把instability本身spin为finding——\\\"item sampling is itself a major variance source, providing empirical justification for G-theory's item-as-facet treatment and D-study budgeting approach。\\\"\\n\"\n  },\n  {\n    \"name\": \"exp-002: Multi-benchmark replication (flat gradient)\",\n    \"description\": \"4 models × 2 precisions (bf16/fp16) × 6 prompts × 6 seeds × 2 temperatures (T=0.0/T=0.7) × 4 orderings × 200 items on GSM8K, ARC-Challenge, HellaSwag。 Per benchmark: 4×2×6×6×2×4=2304 conditions × 200 items = 460,800 records。 Total: 1,382,400 records。Cross-model balanced analysis: bf16 only, 576 conditions/model × 4 × 200 = 230,400/benchmark。 结果：variance structure跨benchmark几乎不变，item_id range仅5.7pp， gradient narrative完全不成立。\\n\",\n    \"results\": {\n      \"total_records_all_benchmarks\": 1382400,\n      \"benchmarks_completed\": 3,\n      \"mmlu_cross_item_id_pct\": 42.1,\n      \"mmlu_cross_model_x_item_pct\": 33.6,\n      \"mmlu_cross_residual_pct\": 19.5,\n      \"mmlu_cross_G_item\": 0.82,\n      \"gsm8k_cross_item_id_pct\": 38.4,\n      \"gsm8k_cross_model_x_item_pct\": 31.8,\n      \"gsm8k_cross_residual_pct\": 22.6,\n      \"gsm8k_cross_prompt_x_item_pct\": 8.4,\n      \"gsm8k_cross_seed_x_item_pct\": 5.8,\n      \"gsm8k_cross_temperature_pct\": 3.2,\n      \"gsm8k_cross_G_item\": 0.682,\n      \"gsm8k_cross_G_binary_200items\": 0.438,\n      \"gsm8k_overall_accuracy\": 0.512,\n      \"arc_cross_item_id_pct\": 44.1,\n      \"arc_cross_model_x_item_pct\": 30.5,\n      \"arc_cross_residual_pct\": 18.8,\n      \"arc_cross_prompt_x_item_pct\": 5.2,\n      \"arc_cross_seed_x_item_pct\": 4.6,\n      \"arc_cross_temperature_pct\": 1.4,\n      \"arc_cross_G_item\": 0.718,\n      \"arc_cross_G_binary_200items\": 0.521,\n      \"arc_overall_accuracy\": 0.548,\n      \"hellaswag_cross_item_id_pct\": 41.8,\n      \"hellaswag_cross_model_x_item_pct\": 35.2,\n      \"hellaswag_cross_residual_pct\": 17.4,\n      \"hellaswag_cross_prompt_x_item_pct\": 3.8,\n      \"hellaswag_cross_seed_x_item_pct\": 4.2,\n      \"hellaswag_cross_temperature_pct\": 0.8,\n      \"hellaswag_cross_G_item\": 0.668,\n      \"hellaswag_cross_G_binary_200items\": 0.492,\n      \"hellaswag_overall_accuracy\": 0.621,\n      \"cross_bench_item_id_range_pp\": 5.7,\n      \"cross_bench_item_id_min\": 38.4,\n      \"cross_bench_item_id_max\": 44.1,\n      \"cross_bench_model_x_item_range_pp\": 4.7,\n      \"gradient_rank_knowledge_to_reasoning\": null,\n      \"gradient_linear_fit_R2\": 0.12,\n      \"separability_binary_mmlu_pct\": 0.08,\n      \"separability_binary_gsm8k_pct\": 3.6,\n      \"separability_binary_arc_pct\": 2.4,\n      \"separability_binary_hellaswag_pct\": 4.8,\n      \"separability_binary_max_pct\": 4.8,\n      \"d_study_mmlu_510items_G\": 0.8,\n      \"d_study_gsm8k_510items_G\": 0.753,\n      \"d_study_arc_510items_G\": 0.768,\n      \"d_study_hellaswag_510items_G\": 0.742,\n      \"d_study_cross_bench_delta_max\": 0.058,\n      \"d_study_cross_bench_delta_min\": 0.032,\n      \"d_study_cross_bench_delta_mean\": 0.047,\n      \"irt_gtheory_ratio_mmlu\": 4.1,\n      \"irt_gtheory_ratio_gsm8k\": 1.7,\n      \"irt_gtheory_ratio_arc\": 2.5,\n      \"irt_gtheory_ratio_hellaswag\": 1.6,\n      \"g_item_cross_bench_min\": 0.668,\n      \"g_item_cross_bench_max\": 0.82,\n      \"g_item_cross_bench_mean\": 0.722,\n      \"mmlu_matched_2x2_item_id_pct\": 43.8,\n      \"mmlu_matched_2x2_model_x_item_pct\": 32.4,\n      \"mmlu_matched_2x2_delta_from_full\": 1.7\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Cross-model variance decomposition by benchmark (4 models, bf16)\",\n        \"data\": {\n          \"columns\": [\n            \"source\",\n            \"mmlu_pct\",\n            \"gsm8k_pct\",\n            \"arc_pct\",\n            \"hellaswag_pct\",\n            \"range_pp\"\n          ],\n          \"rows\": [\n            [\n              \"item_id\",\n              42.1,\n              38.4,\n              44.1,\n              41.8,\n              5.7\n            ],\n            [\n              \"model_x_item\",\n              33.6,\n              31.8,\n              30.5,\n              35.2,\n              4.7\n            ],\n            [\n              \"residual\",\n              19.5,\n              22.6,\n              18.8,\n              17.4,\n              5.2\n            ],\n            [\n              \"prompt_x_item\",\n              4.6,\n              8.4,\n              5.2,\n              3.8,\n              4.6\n            ],\n            [\n              \"seed_x_item\",\n              4.7,\n              5.8,\n              4.6,\n              4.2,\n              1.6\n            ],\n            [\n              \"temperature\",\n              1.2,\n              3.2,\n              1.4,\n              0.8,\n              2.4\n            ],\n            [\n              \"model\",\n              0.8,\n              1.2,\n              0.9,\n              0.6,\n              0.6\n            ],\n            [\n              \"precision\",\n              0.0006,\n              0.3,\n              0.1,\n              0.2,\n              0.3\n            ]\n          ]\n        }\n      },\n      {\n        \"name\": \"Table 7: G_item and IRT comparison by benchmark\",\n        \"data\": {\n          \"columns\": [\n            \"benchmark\",\n            \"G_item_4model\",\n            \"G_binary_200items\",\n            \"irt_items_needed\",\n            \"gtheory_items_G80\",\n            \"ratio\"\n          ],\n          \"rows\": [\n            [\n              \"MMLU\",\n              0.82,\n              0.611,\n              118,\n              510,\n              4.1\n            ],\n            [\n              \"GSM8K\",\n              0.682,\n              0.438,\n              286,\n              486,\n              1.7\n            ],\n            [\n              \"ARC-Challenge\",\n              0.718,\n              0.521,\n              178,\n              448,\n              2.5\n            ],\n            [\n              \"HellaSwag\",\n              0.668,\n              0.492,\n              312,\n              502,\n              1.6\n            ]\n          ]\n        }\n      },\n      {\n        \"name\": \"Table 8: Cross-benchmark separability (binary, precision×methodology interaction)\",\n        \"data\": {\n          \"columns\": [\n            \"benchmark\",\n            \"prec_x_prompt_pct\",\n            \"prec_x_seed_pct\",\n            \"prec_x_temp_pct\",\n            \"total_infra_x_method_pct\"\n          ],\n          \"rows\": [\n            [\n              \"MMLU\",\n              0.02,\n              0.01,\n              0.05,\n              0.08\n            ],\n            [\n              \"GSM8K\",\n              1.2,\n              0.8,\n              1.6,\n              3.6\n            ],\n            [\n              \"ARC-Challenge\",\n              0.9,\n              0.5,\n              1.0,\n              2.4\n            ],\n            [\n              \"HellaSwag\",\n              1.6,\n              1.1,\n              2.1,\n              4.8\n            ]\n          ]\n        }\n      },\n      {\n        \"name\": \"Table 9: D-study cross-benchmark transfer error\",\n        \"data\": {\n          \"columns\": [\n            \"benchmark\",\n            \"mmlu_derived_G_at_510items\",\n            \"actual_G_at_510items\",\n            \"delta\"\n          ],\n          \"rows\": [\n            [\n              \"MMLU\",\n              0.8,\n              0.8,\n              0.0\n            ],\n            [\n              \"GSM8K\",\n              0.8,\n              0.753,\n              0.047\n            ],\n            [\n              \"ARC-Challenge\",\n              0.8,\n              0.768,\n              0.032\n            ],\n            [\n              \"HellaSwag\",\n              0.8,\n              0.742,\n              0.058\n            ]\n          ]\n        }\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-002是worst档叙事转向的关键实验。gradient死亡意味着原planned的 \\\"cross-benchmark variance gradient — the primary novel finding\\\"完全不可用。 但flat structure本身可以reframe： (1) Positive spin：\\\"variance structure is approximately benchmark-invariant\\\" → practitioners可以用MMLU结果cautiously extrapolate to other benchmarks。 这解决了一个practical question。 (2) D-study transfer error（Δ=0.03-0.06）限定了\\\"cautiously\\\"的程度—— MMLU-derived budgets会在其他benchmark上overestimate G by 3-6pp， 需要add 10-15% safety margin。 (3) IRT ratio的benchmark-dependence（1.6×-4.1×）是一个publishable finding 本身——解释了为什么field对\\\"IRT够不够\\\"的争论不收敛：答案是benchmark-dependent。 Separability failure across benchmarks（MMLU 0.08% vs HellaSwag 4.8%） means separability完全不能作为general claim，降为\\\"observed on MMLU under binary scoring; does not hold generally\\\"。 Net assessment: exp-002的data是有价值的，只是不支撑原叙事。reframe后 可以支撑contribution (3)（benchmark-insensitivity as positive）但forcing function是writing quality——flat results需要更skillful framing。\\n\\n\\nGradient叙事死掉的核心原因：item_id跨4个benchmark的range仅5.7pp （38.4%-44.1%）。原假设是knowledge benchmarks（MMLU）有高item_id（>55%）， reasoning benchmarks（GSM8K）有低item_id（<30%），形成20+pp的gradient。 实际结果是所有benchmark都落在38-44%的狭窄区间内。 为什么flat？model×item交互在所有benchmark上都在30-36%——这意味着无论 task type如何，模型间的item difficulty ranking disagreement程度类似。 直觉上，这是因为7-9B模型在knowledge和reasoning tasks上都有类似程度的 model-specific strengths/weaknesses：Llama在MMLU的history和GSM8K的 word problems上都相对strong，Mistral在MMLU的STEM和GSM8K的multi-step上 都相对weak——model-specificity的pattern在task types之间有一致性。 G_item跨benchmark从0.668到0.820变化较大（range=0.152），但这主要由 residual差异驱动而非model×item差异。GSM8K和HellaSwag的G_item低 （0.668-0.682）是因为higher residual（22.6%和17.4%+更高的prompt×item）， 不是因为model×item更大。 IRT ratio在GSM8K（1.7×）和HellaSwag（1.6×）上collapse到<2×，原因是 这些benchmark的IRT也需要更多items（item discrimination更uniform， 2PL model的efficiency advantage减弱），所以分母增大、ratio压缩。 MMLU上IRT仍然只需~120 items因为items有strong discrimination gradients （从trivial到impossible跨57 subjects），2PL拟合效率高。 Cross-benchmark separability failure（max=4.8% on HellaSwag binary） 原因：HellaSwag的sentence completion任务对precision和temperature的 交互更敏感——不同precision下temperature>0生成的completions有更多 divergence，且binary scoring的粒度在这类任务上captures了更多差异。 D-study cross-bench Δ=0.032-0.058意味着MMLU-derived budgets在其他 benchmark上systematically overestimate reliability by 3-6pp。这是因为 MMLU的residual较低（19.5%）相对于GSM8K（22.6%）——更多unexplained variance意味着需要更多observations来stabilize。\\n\"\n  },\n  {\n    \"name\": \"exp-003: Multi-hardware G-study (partial)\",\n    \"description\": \"原计划4 models × 2+ GPU types × 2 precisions × full crossing。 在worst档中，第二种GPU（RTX A6000 48GB）在deadline前4周获得， 仅完成2 models（Llama + Mistral）× 2 precisions（bf16/fp16）× 6 prompts × 6 seeds × 3 temps × 4 orderings × 200 items = 2 × 576 × 200 = 230,400 records。 Hardware × methodology interaction = 4.2% binary average，separability claim破裂。\\n\",\n    \"results\": {\n      \"status\": \"PARTIAL\",\n      \"gpu_types\": [\n        \"RTX_PRO_6000_96GB\",\n        \"RTX_A6000_48GB\"\n      ],\n      \"models_completed\": 2,\n      \"models\": [\n        \"Llama-3.1-8B-Instruct\",\n        \"Mistral-7B-Instruct-v0.3\"\n      ],\n      \"total_records\": 230400,\n      \"conditions_per_model\": 576,\n      \"hardware_main_effect_pct\": 1.8,\n      \"hardware_x_precision_pct\": 0.9,\n      \"hardware_x_prompt_pct\": 0.6,\n      \"hardware_x_seed_pct\": 0.3,\n      \"hardware_x_temperature_pct\": 1.4,\n      \"hardware_x_item_pct\": 2.8,\n      \"total_hardware_x_methodology_pct\": 4.2,\n      \"hardware_x_methodology_llama_pct\": 3.8,\n      \"hardware_x_methodology_mistral_pct\": 4.6,\n      \"single_gpu_infra_x_method_pct\": 0.08,\n      \"multi_gpu_infra_x_method_pct\": 4.2,\n      \"delta_pp\": 4.12,\n      \"llama_pro6000_accuracy\": 0.6814,\n      \"llama_a6000_accuracy\": 0.6791,\n      \"llama_hardware_gap_pp\": 0.23,\n      \"mistral_pro6000_accuracy\": 0.6124,\n      \"mistral_a6000_accuracy\": 0.6083,\n      \"mistral_hardware_gap_pp\": 0.41,\n      \"G_binary_single_gpu\": 0.611,\n      \"G_binary_two_gpu\": 0.582,\n      \"G_delta\": 0.029\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Hardware × methodology interaction breakdown (2 models, binary)\",\n        \"data\": {\n          \"columns\": [\n            \"interaction_term\",\n            \"llama_pct\",\n            \"mistral_pct\",\n            \"average_pct\"\n          ],\n          \"rows\": [\n            [\n              \"hardware_x_temperature\",\n              1.1,\n              1.7,\n              1.4\n            ],\n            [\n              \"hardware_x_precision\",\n              0.7,\n              1.1,\n              0.9\n            ],\n            [\n              \"hardware_x_prompt\",\n              0.5,\n              0.7,\n              0.6\n            ],\n            [\n              \"hardware_x_seed\",\n              0.2,\n              0.4,\n              0.3\n            ],\n            [\n              \"hardware_x_item\",\n              2.4,\n              3.2,\n              2.8\n            ],\n            [\n              \"hardware_main\",\n              1.3,\n              2.3,\n              1.8\n            ],\n            [\n              \"total_hardware_related\",\n              6.2,\n              9.4,\n              7.8\n            ],\n            [\n              \"total_hardware_x_methodology\",\n              3.8,\n              4.6,\n              4.2\n            ]\n          ]\n        }\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-003的partial completion足以kill separability claim但不够做full hardware G-study。只有2个模型意味着hardware×model interaction无法properly estimate。 但data is sufficient to downgrade separability from \\\"claim\\\" to \\\"observation limited to single-GPU environments\\\"。 论文framing：在Methods中honest报告\\\"hardware crossing was partially completed (2 of 4 models)\\\"，在Results中报告4.2% interaction as \\\"preliminary evidence that separability does not hold across GPU architectures\\\"，在Discussion中 qualify all prior separability statements to \\\"single-GPU, single-architecture\\\"。 这不fatal——separability在worst档叙事中已经不是contribution了。\\n\\n\\nHardware×methodology interaction从single-GPU的0.08%跳至multi-GPU的4.2%， 原因是两种GPU有不同的CUDA kernel implementations（RTX PRO 6000使用 sm_89 Ada Lovelace kernels，A6000使用sm_86 Ampere kernels）。 BF16 matrix multiply的rounding behavior在两种架构上不同——不是precision 本身的问题（bf16 spec相同），而是kernel-level implementation差异导致 少量items在一个GPU上答对、另一个上答错。 hardware×temperature=1.4%是最大sub-interaction，因为temperature>0时的 sampling受CUDA RNG implementation影响，不同GPU的cuRAND版本产生 不同的pseudo-random sequences（即使seed相同）。 hardware×item=2.8%反映了~5-8个items在两GPU间有consistently不同的 答案——这些items恰好在model的decision boundary上，kernel-level numerical differences足以flip prediction。 Mistral（4.6%）比Llama（3.8%）的hardware interaction更大，因为Mistral accuracy更低（61.2%），更多items在decision boundary附近。 这个结果对separability是definitive negative：\\\"infrastructure×methodology ≈0%\\\"只在single-GPU上成立。跨GPU，interaction是non-negligible的。 但4.2%仍然是minor relative to item_id（42.1%）和model×item（33.6%）， 所以the hierarchy is preserved——hardware interaction doesn't dominate。\\n\"\n  },\n  {\n    \"name\": \"exp-004: Comprehensive analysis\",\n    \"description\": \"基于exp-001/001b/002/003数据的全面分析。Worst档中exp-003仅有partial data， 但exp-001和exp-002完整。可执行13/17 planned analyses。 核心输出：IRT vs G-theory对比（benchmark-dependent ratio），D-study cross-benchmark transfer analysis，完整robustness package。\\n\",\n    \"results\": {\n      \"planned_analyses\": 17,\n      \"executable_analyses\": 13,\n      \"blocked_analyses\": 4,\n      \"blocked_list\": [\n        \"full hardware G-study\",\n        \"hardware ranking stability\",\n        \"hardware logprob analysis\",\n        \"hardware cost optimization\"\n      ],\n      \"model_as_facet_item_id_pct\": 42.1,\n      \"model_as_facet_model_x_item_pct\": 33.6,\n      \"model_as_facet_G_item\": 0.82,\n      \"bootstrap_n\": 1000,\n      \"item_id_CI_95\": [\n        36.0,\n        48.8\n      ],\n      \"model_x_item_CI_95\": [\n        28.4,\n        37.9\n      ],\n      \"residual_CI_95\": [\n        16.2,\n        23.1\n      ],\n      \"G_item_CI_95\": [\n        0.782,\n        0.861\n      ],\n      \"G_binary_CI_95\": [\n        0.571,\n        0.652\n      ],\n      \"d_study_practical_items_G80_mmlu\": 510,\n      \"d_study_practical_items_G80_gsm8k\": 624,\n      \"d_study_practical_items_G80_arc\": 538,\n      \"d_study_practical_items_G80_hellaswag\": 652,\n      \"d_study_cross_bench_delta_range\": [\n        0.032,\n        0.058\n      ],\n      \"d_study_14k_mmlu_G\": 0.972,\n      \"reml_henderson_max_diff_pp\": 0.4,\n      \"reml_convergence_iterations\": 500,\n      \"reml_practical_convergence_delta\": 0.003,\n      \"irt_gtheory_ratio_mmlu\": 4.1,\n      \"irt_gtheory_ratio_gsm8k\": 1.7,\n      \"irt_gtheory_ratio_arc\": 2.5,\n      \"irt_gtheory_ratio_hellaswag\": 1.6,\n      \"irt_gtheory_ratio_mean\": 2.5,\n      \"irt_gtheory_ratio_sd\": 1.14,\n      \"min_detectable_interaction_pct\": 0.8,\n      \"power_at_1pct_interaction\": 0.94,\n      \"power_at_5pct_interaction\": 0.99,\n      \"G_all_random\": 0.611,\n      \"G_temp_fixed\": 0.634,\n      \"G_ordering_fixed\": 0.645,\n      \"G_both_fixed\": 0.664,\n      \"fixed_random_max_delta\": 0.053,\n      \"bernoulli_obs_variance_corr\": 0.91,\n      \"null_sim_item_id_pct\": 0.08,\n      \"obs_to_bernoulli_ratio\": 1.0008,\n      \"bootstrap_jackknife_CI_ratio_mean\": 1.02,\n      \"bootstrap_jackknife_CI_ratio_range\": [\n        0.96,\n        1.04\n      ],\n      \"mmlu_2x2_vs_3x3_max_delta_pp\": 1.7,\n      \"mmlu_14k_items_G_projected\": 0.972,\n      \"logprob_mmlu_item_id_pct\": 48.3,\n      \"logprob_gsm8k_item_id_pct\": 44.8,\n      \"logprob_arc_item_id_pct\": 46.1,\n      \"logprob_hellaswag_item_id_pct\": 45.9,\n      \"logprob_cross_bench_range_pp\": 3.5,\n      \"gpu_hours_G80_mmlu\": 340,\n      \"gpu_hours_G80_gsm8k\": 415,\n      \"gpu_hours_G80_hellaswag\": 430,\n      \"gpu_hours_G90_mmlu\": 890\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: IRT vs G-theory item requirements by benchmark\",\n        \"data\": {\n          \"columns\": [\n            \"benchmark\",\n            \"irt_2pl_items\",\n            \"gtheory_practical_items\",\n            \"ratio\",\n            \"gtheory_accounts_for\"\n          ],\n          \"rows\": [\n            [\n              \"MMLU\",\n              118,\n              510,\n              4.1,\n              \"prompt + seed + ordering + temp + prec\"\n            ],\n            [\n              \"GSM8K\",\n              286,\n              486,\n              1.7,\n              \"same facets; IRT also needs more items\"\n            ],\n            [\n              \"ARC-Challenge\",\n              178,\n              448,\n              2.5,\n              \"same\"\n            ],\n            [\n              \"HellaSwag\",\n              312,\n              502,\n              1.6,\n              \"same; IRT needs most items here\"\n            ]\n          ]\n        }\n      },\n      {\n        \"name\": \"Table 12: D-study budget recommendations by benchmark (G≥0.80, practical)\",\n        \"data\": {\n          \"columns\": [\n            \"benchmark\",\n            \"items\",\n            \"prompts\",\n            \"seeds\",\n            \"G_projected\",\n            \"CI_95\"\n          ],\n          \"rows\": [\n            [\n              \"MMLU\",\n              510,\n              2,\n              3,\n              0.8,\n              \"[0.782, 0.825]\"\n            ],\n            [\n              \"GSM8K\",\n              624,\n              3,\n              4,\n              0.801,\n              \"[0.774, 0.831]\"\n            ],\n            [\n              \"ARC-Challenge\",\n              538,\n              2,\n              3,\n              0.8,\n              \"[0.778, 0.826]\"\n            ],\n            [\n              \"HellaSwag\",\n              652,\n              3,\n              4,\n              0.802,\n              \"[0.771, 0.838]\"\n            ]\n          ]\n        }\n      },\n      {\n        \"name\": \"Table 13: Methodological robustness summary\",\n        \"data\": {\n          \"columns\": [\n            \"analysis\",\n            \"result\",\n            \"status\"\n          ],\n          \"rows\": [\n            [\n              \"Binary not artifact (null sim)\",\n              \"item_id=0.08% vs obs 61.1% (737×)\",\n              \"PASS\"\n            ],\n            [\n              \"Fixed vs random sensitivity\",\n              \"max Δ(G)=0.053\",\n              \"PASS\"\n            ],\n            [\n              \"Bootstrap = Jackknife CIs\",\n              \"ratio range [0.96, 1.04]\",\n              \"PASS\"\n            ],\n            [\n              \"REML vs Henderson I\",\n              \"max diff < 0.4pp\",\n              \"PASS\"\n            ],\n            [\n              \"Temperature stratification\",\n              \"binary G: 0.760→0.549 (T=0→0.7)\",\n              \"PASS\"\n            ],\n            [\n              \"Bernoulli variance correlation\",\n              \"r=0.91 (item variance partly mechanical)\",\n              \"NOTED\"\n            ],\n            [\n              \"D-study cross-benchmark transfer\",\n              \"Δ=0.032-0.058\",\n              \"CAVEAT\"\n            ],\n            [\n              \"Leave-one-model-out matched\",\n              \"spread=0.058\",\n              \"CAVEAT\"\n            ]\n          ]\n        }\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-004在worst档中的关键产出是benchmark-conditional IRT ratio——这是 新发现，解释了field对\\\"IRT够不够\\\"的长期争论。可以claim：\\\"The IRT-G-theory gap is benchmark-dependent, ranging from 1.6× (HellaSwag) to 4.1× (MMLU), because IRT item parameters (discrimination, difficulty) vary across task types\\\"。这不需要gradient叙事，是self-contained的。 D-study cross-benchmark transfer analysis（Δ=0.03-0.06）is nuanced： 正面解读是MMLU budgets are \\\"approximately right\\\" (within 6pp G)； 负面解读是they're \\\"not directly transferable\\\"。论文adopt中间立场： \\\"MMLU-derived budgets provide a lower bound; benchmark-specific calibration improves precision by 3-6pp G\\\"。 Robustness package的6个PASS + 2个CAVEAT provides methodological credibility。 CAVEAT items (D-study transfer, LOMO) are discussed honestly rather than hidden。\\n\\n\\nexp-004的analysis在worst档中产出两类结果： (1) Robust surviving findings（不受数据缺失影响）：IRT vs G-theory对比 在MMLU上4.1×（locked），但cross-benchmark显示ratio从1.6×到4.1×—— reviewer会说\\\"so the 3-4× claim is only valid for MMLU\\\"。ratio collapse的 原因：在reasoning benchmarks上，IRT的2PL model fit效率降低（items have 更uniform discrimination，lower slope parameters），IRT自己也需要更多items （GSM8K: 286 items vs MMLU: 118 items），所以G-theory的extra cost 相对缩小。论文可以claim \\\"3.6-4.4× on MMLU\\\" and \\\"1.6-4.1× benchmark- dependent range\\\"——后者本身是informative finding。 (2) Weakened findings：D-study cross-benchmark transfer Δ=0.03-0.06 意味着MMLU budgets不能直接apply to other benchmarks（会high by 3-6pp G）。 这undercuts contribution (3)的\\\"practitioners can extrapolate\\\"——需要加 significant caveat \\\"with 10-15% safety margin\\\"。 Robustness package全部基于exp-001 Llama数据，fully intact：binary not artifact（null sim 0.08%），fixed vs random insensitive（Δ<0.053）， bootstrap=jackknife（ratio 0.96-1.04），REML confirms Henderson I（<0.4pp）。 这些是论文的guaranteed floor——无论worst scenario多bad，robustness is there。 Logprob analysis跨benchmarks显示更tight的range（3.5pp vs binary的5.7pp）， suggesting logprob-based scoring reduces benchmark-dependence。This is a minor but novel observation that can go in Discussion。\\n\"\n  },\n  {\n    \"name\": \"exp-005: 14B model extension\",\n    \"description\": \"Qwen3-14B和DeepSeek-R1-Distill-14B在datacenter GPU上的BF16/FP16测试。 Worst档中未执行——deps on exp-003 timeline + 无可用48GB+ GPU时间。\\n\",\n    \"results\": {\n      \"status\": \"NOT_COMPLETED\",\n      \"records_collected\": 0,\n      \"blocking_reason\": \"exp-003在deadline前4周才partially完成，exp-005的protocol 依赖exp-003确定的multi-hardware procedure。同时14B模型需要 ~24GB VRAM（bf16），PRO 6000可以跑但被P0实验占满。 无法在AAAI deadline前执行。\\n\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"不fatal。论文scope明确为\\\"7-9B open-weight models\\\"。14B extension 适合ACL ARR camera-ready或后续独立paper。\\n\\n\\nexp-005的timeline依赖链：exp-003 partial completion → protocol finalization → 14B model runs。exp-003在T-4周才完成，来不及做exp-005的full crossing。 此外，14B模型的inference latency比8B高~1.8×，即使有GPU也难在deadline内 完成576 conditions × 2 models × 200 items = 230,400 records。 对论文的影响：所有结论限于7-9B模型规模。reviewer concern \\\"scale validation\\\" 只能在Limitations中acknowledge，argue \\\"7-9B是最commonly used open-weight model class\\\"。\\n\"\n  },\n  {\n    \"name\": \"exp-006: Fine-tuning G-study\",\n    \"description\": \"RoBERTa-large在SST-2/MNLI/RTE/COPA上的fine-tuning方差分解。 Worst档中未执行——P1优先级，GPU budget被P0消耗。\\n\",\n    \"results\": {\n      \"status\": \"NOT_COMPLETED\",\n      \"records_collected\": 0,\n      \"blocking_reason\": \"P1 priority。P0实验（exp-001 ~100h + exp-002 ~200h + exp-003 ~60h partial） 消耗了大部分GPU budget。1,728次fine-tuning runs × ~15min ≈ 430 GPU-hours 无法accommodate。\\n\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"零影响。在Discussion中mention \\\"extending G-theory to fine-tuning variance is natural future work; Dodge et al. (2020) and Bui et al. (2025) provide preliminary evidence that seed/LR dominate fine-tuning variance\\\"。\\n\\n\\nPer D006 framing directive #5，fine-tuning已降级为Discussion-section preliminary observation，不是numbered contribution。即使完成，encoder-only RoBERTa的fine-tuning与decoder LLM inference的methodological gap也会被 reviewer指出。在worst档reframed narrative（MMLU case study + IRT comparison） 中，fine-tuning完全outside scope。\\n\"\n  },\n  {\n    \"name\": \"exp-007: LayerCast precision mitigation\",\n    \"description\": \"LayerCast（FP16 storage + FP32 compute）作为额外precision条件。 P2优先级，worst档中未执行。\\n\",\n    \"results\": {\n      \"status\": \"NOT_COMPLETED\",\n      \"records_collected\": 0,\n      \"blocking_reason\": \"P2 priority, not attempted within AAAI timeline\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"零影响。Precision在bf16/fp16上已经是non-issue（0.0006%）， LayerCast实验变得moot。\\n\\n\\nLayerCast是mitigation strategy evaluation，不是core finding。 BF16-vs-FP16 sensitivity已显示precision effect=0.0006%（接近zero）， LayerCast的additional data point价值marginal——precision已经不是 variance source。可以在Discussion中cite Yuan et al. (2025)的 LayerCast results as \\\"practitioners can further reduce precision variance via mixed-precision strategies\\\"。\\n\"\n  },\n  {\n    \"name\": \"exp-008: MATH benchmark extension\",\n    \"description\": \"MATH benchmark（200 items）测试reasoning-heavy任务的variance structure。 P2优先级且deps on exp-002，worst档中未执行。\\n\",\n    \"results\": {\n      \"status\": \"NOT_COMPLETED\",\n      \"records_collected\": 0,\n      \"blocking_reason\": \"P2 priority。Deps on exp-002 pipeline（已完成但consumed timeline）。 MATH的chain-of-thought generation需要significantly longer inference time （avg ~45 tokens vs MMLU ~1 token），200h GPU budget已用尽。\\n\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Marginal impact。4个benchmarks showing flat structure已经支撑 \\\"benchmark-insensitivity\\\" reframe。MATH would be 5th data point but not change the conclusion。适合ACL ARR补充。\\n\\nexp-002已经覆盖了GSM8K（math reasoning）、ARC（science reasoning）、 HellaSwag（commonsense），增加MATH的marginal value在worst档flat gradient 下更低——不会出现新pattern，只会是another data point在38-44% item_id区间内。 如果需要bolster \\\"benchmark-insensitivity\\\" claim，现有4个benchmarks （MMLU + 3 from exp-002）已经sufficient。\\n\"\n  }\n]",
      "numLines": 1049,
      "startLine": 1,
      "totalLines": 1049
    }
  },
  "sourceToolAssistantUUID": "205be5b8-e484-444c-b459-05b770425772",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T075006 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheor…",
  "leafUuid": "621a6489-875f-4237-aec5-b8cbed943217",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate LLM evaluation variance analysis paper",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3"
}
```

---

### Assistant

_source line 16 · 2026-05-21T08:28:29.552Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me also read the research and writing skills to inform the paper style.

Actually, I have enough context. Let me now write the full LaTeX paper based on:

1. The experiment data from the JSON
2. The paper framing document
3. The narrative guidance from the prompt

Key points from narrative guidance:
- Gradient narrative is dead — variance structure is approximately benchmark-invariant (item_id range only 5.7pp)
- Reframe as MMLU case study in multi-facet evaluation measurement
- Three primary contributions:
  (1) model×item interaction quantification — 42%→61% inflation + D-study Δ=0.004
  (2) IRT vs G-theory direct comparison — 3.6-4.4× on MMLU, benchmark-dependent cross-bench
  (3) Variance structure benchmark-insensitivity reframed as positive
- Separability demoted to observation
- Item resampling instability (CV=0.14) spun positively
- LOMO spread=0.058 reported honestly as limitation
- Title: "The Hidden Second Factor: Model×Item Interaction Accounts for 34% of LLM Evaluation Variance"

The title matches the narrative guidance, so I'll use that. Now I'm ready to compose the full paper with the LaTeX structure, weaving together the experimental findings, the theoretical framing, and the key contributions into a cohesive narrative.

I'm organizing the paper around five completed experiments: the core MMLU G-study, item resampling stability checks, cross-benchmark replication, multi-hardware validation, and comprehensive analysis. Each section will include its corresponding tables and results. I'll structure it with standard sections—abstract, introduction, related work, methods, experiments with subsections, results and discussion, and conclusion—then generate the LaTeX document.

Writing the paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "621a6489-875f-4237-aec5-b8cbed943217",
  "isSidechain": false,
  "requestId": "req_011CbFQ3yfwETxgd5wWFyoFf",
  "type": "assistant",
  "uuid": "c8f514a4-852e-4806-b840-b12404cb1386",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2gg4Bbj6ByW7VBxon7UYF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7061,
      "cache_creation_input_tokens": 16717,
      "cache_read_input_tokens": 23720,
      "output_tokens": 656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7061,
          "output_tokens": 656,
          "cache_read_input_tokens": 23720,
          "cache_creation_input_tokens": 16717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16717
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

_source line 17 · 2026-05-21T08:28:29.554Z_

Let me check the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8f514a4-852e-4806-b840-b12404cb1386",
  "isSidechain": false,
  "requestId": "req_011CbFQ3yfwETxgd5wWFyoFf",
  "type": "assistant",
  "uuid": "c1aa4dd4-7bd1-4960-8060-c5046966b226",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2gg4Bbj6ByW7VBxon7UYF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7061,
      "cache_creation_input_tokens": 16717,
      "cache_read_input_tokens": 23720,
      "output_tokens": 656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7061,
          "output_tokens": 656,
          "cache_read_input_tokens": 23720,
          "cache_creation_input_tokens": 16717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16717
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

_source line 18 · 2026-05-21T08:28:29.972Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HtZvLb8YoQ2KKBnBqzap1D`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/",
  "description": "List target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1aa4dd4-7bd1-4960-8060-c5046966b226",
  "isSidechain": false,
  "requestId": "req_011CbFQ3yfwETxgd5wWFyoFf",
  "type": "assistant",
  "uuid": "6876d20d-a138-4d1e-93b9-74cdb5b206f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2gg4Bbj6ByW7VBxon7UYF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7061,
      "cache_creation_input_tokens": 16717,
      "cache_read_input_tokens": 23720,
      "output_tokens": 656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16717,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7061,
          "output_tokens": 656,
          "cache_read_input_tokens": 23720,
          "cache_creation_input_tokens": 16717,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16717
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

_source line 19 · 2026-05-21T08:28:30.103Z_

<details><summary>↩ Tool result · `toolu_01HtZvLb8YoQ2KKBnBqzap1D`</summary>

```text
experiment_data.json
imagined_experiments.yaml
paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6876d20d-a138-4d1e-93b9-74cdb5b206f0",
  "isSidechain": false,
  "promptId": "9d021380-77fd-4766-a060-794a49f7c1c1",
  "type": "user",
  "uuid": "a853c19c-f287-4f64-85e9-b69cf578b954",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "6876d20d-a138-4d1e-93b9-74cdb5b206f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-21T08:28:32.801Z_

Now I'll write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a853c19c-f287-4f64-85e9-b69cf578b954",
  "isSidechain": false,
  "requestId": "req_011CbFQ5NzuyqdSNyDVZjB5B",
  "type": "assistant",
  "uuid": "da623921-a31e-42de-8691-11b5e2ec141b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DnJRHtvNV6JLKJVi3GrgU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7745,
      "cache_read_input_tokens": 40437,
      "output_tokens": 14632,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14632,
          "cache_read_input_tokens": 40437,
          "cache_creation_input_tokens": 7745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7745
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

_source line 21 · 2026-05-21T08:32:57.610Z_

<details open><summary>🔧 Tool call — Write · `toolu_01TSxkxWT3JwpgNvfA1Kqism`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/paper.tex",
  "content": "\\documentclass[letterpaper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{array}\n\\usepackage{caption}\n\n\\title{The Hidden Second Factor: Model$\\times$Item Interaction Accounts for 34\\% of LLM Evaluation Variance}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWhen LLM evaluation results vary across reproductions, practitioners cannot determine whether the variance originates from prompt phrasing, random seeds, numerical precision, temperature, or item selection---let alone how these factors interact.\nWe conduct a multi-benchmark Generalizability Theory (G-theory) study crossing infrastructure and methodology factors across 4 open-weight models (7--9B parameters) on MMLU, GSM8K, ARC-Challenge, and HellaSwag, totaling over 2.3 million evaluation records.\nOn MMLU (345,600 balanced cross-model records), item selection accounts for 42.1\\% of variance and model$\\times$item interaction emerges as the second-largest source at 33.6\\%, revealing that item difficulty rankings are substantially model-specific: single-model analyses inflate item dominance from 42\\% to 61\\% by conflating universal and model-specific difficulty.\nA Decision study (D-study) predicted the 4-model generalizability coefficient within $\\Delta=0.004$ of the observed value, providing out-of-sample validation.\nAcross four benchmarks, variance structure is approximately invariant (item dominance range = 5.7 percentage points), enabling cautious cross-benchmark extrapolation of MMLU-derived evaluation budgets with a 3--6 percentage-point safety margin.\nG-theory requires 1.6--4.1$\\times$ more items than IRT for reliable measurement, with the ratio being benchmark-dependent---resolving conflicting conclusions in the literature about IRT sufficiency.\nA partial two-GPU study reveals that hardware$\\times$methodology interaction reaches 4.2\\%, breaking the separability assumption that holds within single-GPU environments ($<$0.1\\%).\nWe release an open-source G-theory variance decomposition pipeline and D-study budget calculator.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nReproducibility failures in LLM evaluation undermine the credibility of benchmark-based comparisons.\nA model declared superior on MMLU under one evaluation protocol may lose its advantage under a different prompt template \\citep{sclar2024quantifying}, random seed \\citep{bui2025seed}, or numerical precision setting \\citep{yuan2025precision}.\nYet each prior study isolates at most one or two variance sources, implicitly assuming that these factors do not interact.\nThe field lacks a unified framework for simultaneously attributing evaluation variance to all relevant sources and their interactions.\n\nGeneralizability Theory (G-theory; \\citealt{shavelson1991generalizability, brennan2001generalizability}) provides exactly this framework.\nOriginally developed in educational measurement, G-theory decomposes observed variance into contributions from every facet (e.g., items, raters, occasions) and their interactions in a single analysis, then projects reliability under hypothetical measurement designs via Decision studies (D-studies).\n\\citet{mesting2026generalizability} adapted G-theory to LLM evaluation with five methodological facets on a single benchmark, establishing feasibility but leaving infrastructure factors, cross-benchmark comparisons, and model-as-facet analysis unexplored.\n\nWe extend this line of work with three contributions:\n\n\\textbf{(1) Model$\\times$item interaction quantification.}\nIn a balanced 4-model MMLU design (345,600 records), model$\\times$item interaction accounts for 33.6\\% [95\\% CI: 28.4--37.9\\%] of total variance---the second-largest source after item selection (42.1\\%).\nSingle-model analyses inflate item dominance to 61.1\\% by conflating universal and model-specific item difficulty.\nA D-study from 3 models predicted the 4-model generalizability coefficient ($G$) within $\\Delta = 0.004$, providing out-of-sample validation that G-theory's projective machinery works for LLM evaluation.\n\n\\textbf{(2) IRT vs.\\ G-theory direct comparison.}\nG-theory requires 3.6--4.1$\\times$ more items than IRT on MMLU to reach the same reliability target, because it accounts for prompt, seed, and ordering dimensions that IRT ignores.\nThis ratio is benchmark-dependent, ranging from 1.6$\\times$ (HellaSwag) to 4.1$\\times$ (MMLU), explaining why the field has not converged on whether IRT-based subsampling is sufficient.\n\n\\textbf{(3) Approximate benchmark-invariance of variance structure.}\nAcross MMLU, GSM8K, ARC-Challenge, and HellaSwag, the item dominance proportion varies by only 5.7 percentage points (38.4--44.1\\%), and the variance component ranking is preserved.\nMMLU-derived evaluation budgets transfer to other benchmarks with a 3--6 percentage-point $G$-coefficient error, enabling cautious cross-benchmark extrapolation.\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Variance decomposition in ML evaluation.}\n\\citet{bouthillier2021accounting} decomposed ML benchmark variance across hyperparameters, data splits, and random seeds via ANOVA, establishing factorial variance decomposition as a methodology for ML evaluation.\n\\citet{henderson2018deep} documented large variance across seeds in deep reinforcement learning.\n\\citet{dodge2020finetuning} and \\citet{sellam2022multberts} quantified fine-tuning instability from seeds and data ordering in BERT-scale models.\n\\citet{bui2025seed} extended this to instruction-tuned LLMs, finding extreme seed sensitivity (RTES variance up to 18.22 for RoBERTa on COPA).\n\n\\paragraph{Prompt and evaluation sensitivity.}\n\\citet{sclar2024quantifying} demonstrated up to 76\\% accuracy swings from prompt formatting alone.\n\\citet{lu2022fantastically} and \\citet{pezeshkpour2024large} documented option-ordering effects in multiple-choice evaluation.\nBrittleBench \\citep{brittlebench2026} quantified prompt sensitivity at 50\\% variance on fixed hardware.\n\n\\paragraph{Infrastructure effects.}\n\\citet{yuan2025precision} documented up to 9\\% accuracy variation from hardware and numerical precision without factorial attribution.\n\\citet{messina2026floating} identified floating-point non-associativity as a mechanism for cross-hardware divergence.\n\n\\paragraph{G-theory in LLM evaluation.}\n\\citet{mesting2026generalizability} adapted G-theory to LLM evaluation with 5 methodological facets on a single benchmark, finding judge identity as the dominant variance source (43.8\\%).\nWe build on this by (a) adding infrastructure as a facet, (b) treating model as a crossed facet to expose model$\\times$item interaction, (c) extending to four benchmarks, and (d) fixing the judge to isolate non-judge variance sources.\n\\citet{shavelson1991generalizability} and \\citet{brennan2001generalizability} provide the canonical G-theory references; \\citet{jiang2017generalized} and \\citet{mushquash2006generalizability} address G-theory for binary response data.\n\n\\paragraph{IRT-based evaluation.}\n\\citet{lalor2019learning} introduced IRT-based item analysis for NLP evaluation.\n\\citet{rodriguez2021evaluation} and \\citet{vania2021comparing} further developed IRT applications in NLP benchmarking.\n\\citet{polo2024tinybenchmarks} proposed IRT-based subsampling (tinyBenchmarks), recommending $\\sim$100 items for reliable evaluation.\n\\citet{perlitz2023efficient} explored efficient benchmarking strategies.\nOur work provides the first direct comparison of IRT and G-theory item requirements, quantifying the cost of multi-facet reliability.\n\n\\paragraph{Alternative frameworks.}\n\\citet{kunievsky2025alternative} proposed decomposing evaluation variance into intent, articulation, and model uncertainty---a complementary perspective to G-theory's facet-based approach.\n\\citet{dehghani2021benchmark} argued that benchmark selection itself is a variance source (the ``Benchmark Lottery'').\n\\citet{biderman2024lessons} synthesized practical lessons for evaluation reproducibility.\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Generalizability Theory Background}\n\nG-theory \\citep{shavelson1991generalizability, brennan2001generalizability} partitions observed score variance into components attributable to each facet and their interactions.\nFor a fully crossed design with items ($i$), prompts ($p$), seeds ($s$), temperatures ($t$), orderings ($o$), and precision ($r$), the observed score $X_{ipstor}$ decomposes as:\n\\begin{equation}\nX_{ipstor} = \\mu + \\alpha_i + \\beta_p + \\gamma_s + \\delta_t + \\epsilon_o + \\zeta_r + (\\alpha\\beta)_{ip} + \\cdots + e_{ipstor}\n\\end{equation}\nwhere each Greek letter denotes a main effect and parenthesized terms denote interactions.\nVariance components $\\hat{\\sigma}^2$ are estimated via Henderson's Method I (expected mean squares), with REML as a robustness check.\n\nThe \\textbf{generalizability coefficient} $G$ quantifies reliability:\n\\begin{equation}\nG = \\frac{\\hat{\\sigma}^2_i}{\\hat{\\sigma}^2_i + \\sum_{f \\neq i} \\frac{\\hat{\\sigma}^2_f}{n_f}}\n\\end{equation}\nwhere the sum runs over all non-item variance components divided by their respective sample sizes.\n\nA \\textbf{D-study} projects $G$ under hypothetical designs by varying $n_f$, enabling practitioners to determine the number of items, prompts, and seeds needed for a target reliability.\n\nWhen model is treated as a crossed facet, the item variance component splits into universal item difficulty ($\\hat{\\sigma}^2_i$) and model$\\times$item interaction ($\\hat{\\sigma}^2_{mi}$).\nThe generalizability of item difficulty rankings across models is captured by:\n\\begin{equation}\nG_{\\text{item}} = \\frac{\\hat{\\sigma}^2_i}{\\hat{\\sigma}^2_i + \\hat{\\sigma}^2_{mi} / n_m + \\hat{\\sigma}^2_{e} / (n_m \\cdot n_{\\text{cond}})}\n\\end{equation}\n\n\\paragraph{Binary data considerations.}\nOur primary metric (binary correct/incorrect) violates G-theory's normality assumption.\nWe address this via: (a) null simulations showing observed item variance exceeds Bernoulli-mechanical variance by 737$\\times$ (Section~\\ref{sec:robustness}); (b) parallel analysis on text-exact-match scoring; (c) sensitivity to fixed/random facet classification ($\\Delta G < 0.053$).\n\\citet{shavelson1989generalizability}, \\citet{mushquash2006generalizability}, and \\citet{jiang2017generalized} provide theoretical justification for G-theory with binary responses.\n\n\\subsection{Experimental Design}\n\n\\paragraph{Models.}\nFour open-weight instruction-tuned models in the 7--9B parameter range: Llama-3.1-8B-Instruct, Gemma-2-9B-it, Mistral-7B-Instruct-v0.3, and Qwen-2.5-7B-Instruct.\nAll inference uses vLLM 0.9.2 with default settings (no batch-invariant kernels), making CUDA-level nondeterminism a measurable variance source.\n\n\\paragraph{Benchmarks.}\nMMLU (primary, 200 stratified items from 57 subjects), GSM8K (200 items), ARC-Challenge (200 items), and HellaSwag (200 items).\n\n\\paragraph{Facets.}\n\\begin{itemize}\n  \\item \\textbf{Precision}: BF16, FP16 (FP32 excluded after identifying vLLM \\texttt{enforce\\_eager} confound; BF16$\\approx$FP16, $\\Delta=0.23$pp accuracy)\n  \\item \\textbf{Prompt}: 6 semantically equivalent templates\n  \\item \\textbf{Seed}: 6 random seeds\n  \\item \\textbf{Temperature}: $T \\in \\{0.0, 0.3, 0.7\\}$ (MMLU); $\\{0.0, 0.7\\}$ (others)\n  \\item \\textbf{Ordering}: 4 systematic option rotations\n  \\item \\textbf{Hardware}: RTX PRO 6000 96GB (primary); RTX A6000 48GB (partial crossing, 2 models)\n\\end{itemize}\n\n\\paragraph{Design structure.}\nExp-001 (MMLU): $4 \\text{ models} \\times 3 \\text{ precisions} \\times 6 \\text{ prompts} \\times 6 \\text{ seeds} \\times 3 \\text{ temperatures} \\times 4 \\text{ orderings} \\times 200 \\text{ items} = 930{,}400$ records.\nCross-model balanced analysis uses BF16 shared conditions: 432 conditions/model $\\times$ 4 models $\\times$ 200 items $= 345{,}600$ records.\nExp-002 (GSM8K, ARC, HellaSwag): $4 \\times 2 \\times 6 \\times 6 \\times 2 \\times 4 \\times 200 = 460{,}800$ records per benchmark (1,382,400 total).\nExp-003 (hardware crossing): 2 models $\\times$ 576 conditions $\\times$ 200 items $= 230{,}400$ records (partial).\n\n\\paragraph{Judge exclusion.}\nUnlike \\citet{mesting2026generalizability}, who includes judge as a facet (finding 43.8\\% judge variance), we fix evaluation to exact-match scoring to isolate infrastructure$\\times$methodology interactions.\nJudge variance is a natural extension for future work.\n\n% ============================================================\n% 4. EXPERIMENTS AND RESULTS\n% ============================================================\n\\section{Experiments and Results}\n\n\\subsection{Exp-001: Cross-Model MMLU Variance Decomposition}\n\\label{sec:exp001}\n\nTable~\\ref{tab:cross_model_decomp} presents the cross-model variance decomposition from the balanced 4-model BF16 design (345,600 records).\nItem selection is the largest source (42.1\\%, CI [36.0, 48.8]), followed by model$\\times$item interaction (33.6\\%, CI [28.4, 37.9]).\nTogether, these two sources account for 75.7\\% of total variance.\nResidual variance (19.5\\%) is the third-largest component; all other sources (prompt$\\times$item, seed$\\times$item, temperature, model main effect, precision) contribute $\\leq$4.7\\% each.\nPrecision is negligible at 0.0006\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model variance decomposition (4 models, MMLU, balanced BF16, 345,600 records). CI = 95\\% bootstrap confidence interval ($B=1{,}000$).}\n\\label{tab:cross_model_decomp}\n\\begin{tabular}{lccc}\n\\toprule\nSource & \\% Variance & CI Lower & CI Upper \\\\\n\\midrule\nItem ($i$)                  & 42.1 & 36.0 & 48.8 \\\\\nModel$\\times$Item ($m \\times i$) & 33.6 & 28.4 & 37.9 \\\\\nResidual                    & 19.5 & 16.2 & 23.1 \\\\\nSeed$\\times$Item            & 4.7  & 3.2  & 6.5  \\\\\nPrompt$\\times$Item          & 4.6  & 3.1  & 6.4  \\\\\nTemperature                 & 1.2  & 0.4  & 2.3  \\\\\nModel                       & 0.8  & 0.1  & 2.1  \\\\\nOther interactions          & 0.5  & 0.1  & 1.2  \\\\\nPrecision                   & 0.0006 & 0.0 & 0.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe generalizability of item difficulty rankings across models is $G_{\\text{item}} = 0.820$ [0.782, 0.861].\nA D-study using 3-model subsets predicted $G_{\\text{item}} = 0.816$ for $n_m = 4$; the observed value is 0.820 ($\\Delta = 0.004$), validating D-study projections out of sample.\nForward projections indicate $G_{\\text{item}} = 0.848$ at 5 models, 0.893 at 8, and 0.910 at 10; reaching $G \\geq 0.90$ requires approximately 10 models.\n\n\\paragraph{Single-model inflation effect.}\nTable~\\ref{tab:per_model_decomp} shows per-model single-model decompositions.\nItem selection accounts for 55.6--61.1\\% in single-model analyses versus 42.1\\% in the cross-model analysis---an inflation of up to 19 percentage points.\nThis inflation occurs because single-model analyses conflate universal item difficulty with model-specific item difficulty (model$\\times$item interaction).\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-model single-model variance decomposition (\\% of total variance, MMLU).}\n\\label{tab:per_model_decomp}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & Llama & Gemma & Mistral & Qwen \\\\\n\\midrule\nItem ($i$)             & 61.1 & 57.8 & 59.4 & 55.6 \\\\\nResidual               & 17.2 & 19.1 & 18.4 & 20.8 \\\\\nPrecision$\\times$Item  & 7.2  & 7.8  & 7.1  & 6.5  \\\\\nPrompt$\\times$Item     & 4.6  & 5.3  & 4.9  & 6.2  \\\\\nSeed$\\times$Item       & 4.7  & 4.5  & 4.6  & 5.1  \\\\\nTemp.$\\times$Item      & 3.1  & 3.4  & 3.2  & 3.6  \\\\\nTemperature            & 1.2  & 1.1  & 1.5  & 1.2  \\\\\nPrecision              & 0.5  & 0.6  & 0.5  & 0.7  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPer-model interaction magnitudes (from the cross-model analysis) correlate inversely with model accuracy: Mistral (29.25\\%, accuracy 63.8\\%) $>$ Qwen (27.11\\%) $>$ Gemma (23.95\\%) $>$ Llama (19.69\\%, accuracy 66.4\\%).\nLower-accuracy models show more model-specific item difficulty patterns, consistent with the interpretation that models near the decision boundary on more items exhibit greater item-level disagreement.\n\n\\paragraph{Leave-one-model-out stability.}\nTable~\\ref{tab:lomo} reports matched-specification leave-one-model-out (LOMO) results using a reduced balanced design (BF16 $\\times$ 4 prompts $\\times$ 4 seeds $\\times$ 2 temperatures $\\times$ 2 orderings = 64 conditions/model).\nThe $G_{\\text{item}}$ spread across 3-model subsets is 0.058 (range: 0.788--0.846), with a standard deviation of 0.026.\n\n\\begin{table}[t]\n\\centering\n\\caption{Leave-one-model-out matched-specification $G_{\\text{item}}$ analysis.}\n\\label{tab:lomo}\n\\begin{tabular}{lccc}\n\\toprule\nDropped Model & $G_{\\text{item}}$ & Item \\% & Model$\\times$Item \\% \\\\\n\\midrule\nMistral & 0.846 & 44.8 & 28.3 \\\\\nQwen    & 0.834 & 43.2 & 30.1 \\\\\nGemma   & 0.802 & 40.5 & 35.8 \\\\\nLlama   & 0.788 & 39.1 & 37.6 \\\\\n\\midrule\nAll 4   & 0.820 & 42.1 & 33.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis spread reflects sensitivity to model selection with only 4 models.\nDropping Llama (the model with the lowest interaction, 19.69\\%) produces the lowest $G_{\\text{item}}$ (0.788) because the remaining three models have higher and more heterogeneous interaction patterns.\nCritically, all four subsets preserve the qualitative conclusions: item selection remains the largest source ($>$39\\%), model$\\times$item is second-largest, and $G_{\\text{item}} > 0.78$ throughout.\nThe D-study projection to 10 models ($G = 0.910$) indicates that this instability is a consequence of small model samples, not a fundamental limitation of the approach.\n\n\\paragraph{BF16 vs.\\ FP16 sensitivity.}\nExcluding FP32 (identified as a vLLM \\texttt{enforce\\_eager} artifact), the precision effect drops to 0.0006\\% of total variance, with precision$\\times$item at 0.04\\%.\nBF16 and FP16 produce nearly identical results ($\\Delta = 0.23$pp accuracy), confirming that numerical precision between these two formats is a negligible variance source.\n\n\\subsection{Exp-001b: Item Resampling Stability}\n\\label{sec:exp001b}\n\nTo assess sensitivity to item selection, we drew three independent stratified samples of 200 MMLU items (seeds 0, 7, 99) and evaluated Llama under 54 conditions per sample (32,400 total records).\nTable~\\ref{tab:resampling} reports the variance decomposition across samples.\n\n\\begin{table}[t]\n\\centering\n\\caption{Resampling stability across 3 independent 200-item draws (single-model Llama, MMLU).}\n\\label{tab:resampling}\n\\begin{tabular}{lcccccc}\n\\toprule\nSource & Seed 0 & Seed 7 & Seed 99 & Mean & SD & CV \\\\\n\\midrule\nItem ($i$)         & 61.1 & 52.8 & 70.4 & 61.4 & 8.8 & 0.143 \\\\\nResidual           & 17.2 & 23.1 & 12.8 & 17.7 & 5.2 & 0.291 \\\\\nPrec.$\\times$Item  & 7.2  & 8.7  & 5.6  & 7.2  & 1.6 & 0.217 \\\\\nPrompt$\\times$Item & 4.6  & 5.8  & 3.9  & 4.8  & 1.0 & 0.201 \\\\\nSeed$\\times$Item   & 4.7  & 5.2  & 4.2  & 4.7  & 0.5 & 0.106 \\\\\nTemp.$\\times$Item  & 3.1  & 3.3  & 2.7  & 3.0  & 0.3 & 0.100 \\\\\nTemperature        & 1.2  & 1.0  & 0.9  & 1.0  & 0.2 & 0.153 \\\\\nPrecision          & 0.5  & 0.6  & 0.3  & 0.5  & 0.2 & 0.333 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe coefficient of variation (CV) for item dominance is 0.143, indicating moderate sensitivity to item selection.\nThe range (52.8--70.4\\%) is consistent with the bootstrap confidence interval [36.0, 48.8\\%] from the cross-model analysis, suggesting that bootstrap CIs already capture item sampling variability.\nImportantly, item selection remains the largest variance source across all three samples, and the variance component ranking is preserved.\n\n\\begin{table}[t]\n\\centering\n\\caption{G-coefficient stability across item draws (single-model Llama, MMLU).}\n\\label{tab:g_stability}\n\\begin{tabular}{lcccccc}\n\\toprule\nMetric & Seed 0 & Seed 7 & Seed 99 & Mean & SD & CV \\\\\n\\midrule\nBinary       & 0.611 & 0.536 & 0.689 & 0.612 & 0.077 & 0.126 \\\\\nText exact   & 0.007 & 0.005 & 0.009 & 0.007 & 0.002 & 0.286 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:g_stability} shows that the $G$-coefficient for binary scoring has lower variability (CV = 0.126) than raw variance percentages (CV = 0.143), indicating that reliability estimates are more stable than individual variance components.\nThe text-exact-match $G$ remains near zero across all samples, confirming that this metric is unreliable regardless of item selection.\nThe resampling instability reinforces the rationale for treating items as a facet in G-theory: if item selection were irrelevant, G-theory's item-as-facet treatment would be unnecessary.\nD-study budgets recommending 500+ items directly address this instability.\n\n\\subsection{Exp-002: Cross-Benchmark Variance Structure}\n\\label{sec:exp002}\n\nWe replicated the cross-model G-study on three additional benchmarks (GSM8K, ARC-Challenge, HellaSwag) using a reduced design ($4 \\times 2 \\times 6 \\times 6 \\times 2 \\times 4 \\times 200$; 460,800 records per benchmark, 1,382,400 total).\nTable~\\ref{tab:cross_bench} presents the cross-benchmark comparison.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model variance decomposition by benchmark (4 models, BF16). Range = max $-$ min across benchmarks.}\n\\label{tab:cross_bench}\n\\begin{tabular}{lccccc}\n\\toprule\nSource & MMLU & GSM8K & ARC & HSwag & Range \\\\\n\\midrule\nItem ($i$)              & 42.1 & 38.4 & 44.1 & 41.8 & 5.7 \\\\\nModel$\\times$Item       & 33.6 & 31.8 & 30.5 & 35.2 & 4.7 \\\\\nResidual                & 19.5 & 22.6 & 18.8 & 17.4 & 5.2 \\\\\nPrompt$\\times$Item      & 4.6  & 8.4  & 5.2  & 3.8  & 4.6 \\\\\nSeed$\\times$Item        & 4.7  & 5.8  & 4.6  & 4.2  & 1.6 \\\\\nTemperature             & 1.2  & 3.2  & 1.4  & 0.8  & 2.4 \\\\\nModel                   & 0.8  & 1.2  & 0.9  & 0.6  & 0.6 \\\\\nPrecision               & 0.0006 & 0.3 & 0.1 & 0.2 & 0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe variance structure is approximately invariant across benchmarks.\nItem dominance ranges from 38.4\\% (GSM8K) to 44.1\\% (ARC-Challenge)---a span of only 5.7 percentage points.\nModel$\\times$item interaction ranges from 30.5\\% to 35.2\\% (4.7pp range).\nThe variance component ranking is identical across all four benchmarks: item $>$ model$\\times$item $>$ residual $>$ prompt$\\times$item $\\geq$ seed$\\times$item.\nThe originally hypothesized systematic gradient from knowledge-retrieval to reasoning benchmarks does not materialize ($R^2 = 0.12$ for a linear fit of item dominance against task type).\n\n\\paragraph{Benchmark-specific differences.}\nGSM8K shows elevated prompt$\\times$item interaction (8.4\\% vs.\\ 3.8--5.2\\% on other benchmarks) and higher temperature sensitivity (3.2\\% vs.\\ 0.8--1.4\\%), consistent with mathematical reasoning tasks being more sensitive to prompt wording and sampling stochasticity.\nHellaSwag has the highest model$\\times$item interaction (35.2\\%) and lowest residual (17.4\\%), suggesting more structured model-specific difficulty patterns in commonsense reasoning.\n\n\\paragraph{IRT vs.\\ G-theory comparison.}\nTable~\\ref{tab:irt_gtheory} presents the first direct comparison of IRT and G-theory item requirements across benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{IRT vs.\\ G-theory item requirements by benchmark. $G_{\\text{item}}$ = cross-model generalizability coefficient (4 models, 200 items). Ratio = G-theory items / IRT items for $G \\geq 0.80$.}\n\\label{tab:irt_gtheory}\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & $G_{\\text{item}}$ & IRT Items & G-theory Items & Ratio \\\\\n\\midrule\nMMLU          & 0.820 & 118 & 510 & 4.1$\\times$ \\\\\nARC-Challenge & 0.718 & 178 & 448 & 2.5$\\times$ \\\\\nGSM8K         & 0.682 & 286 & 486 & 1.7$\\times$ \\\\\nHellaSwag     & 0.668 & 312 & 502 & 1.6$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe IRT-to-G-theory ratio ranges from 1.6$\\times$ (HellaSwag) to 4.1$\\times$ (MMLU).\nOn MMLU, IRT's 2-parameter logistic model achieves high efficiency because items span a wide discrimination range across 57 subjects; G-theory's additional budget accounts for prompt$\\times$item (4.6\\%), seed$\\times$item (4.7\\%), and residual (19.5\\%) variance that IRT ignores.\nOn reasoning benchmarks (GSM8K, HellaSwag), IRT itself requires more items (286--312) due to more uniform item discrimination, compressing the ratio.\nThis benchmark-dependence resolves conflicting claims in the literature: IRT-based subsampling \\citep{polo2024tinybenchmarks} is relatively more sufficient on reasoning benchmarks than on knowledge benchmarks.\n\n\\paragraph{D-study cross-benchmark transfer.}\nTable~\\ref{tab:d_study_transfer} evaluates whether MMLU-derived D-study budgets transfer to other benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study cross-benchmark transfer error. MMLU-derived budget (510 items, 2 prompts, 3 seeds) projected $G = 0.80$; actual $G$ varies by benchmark.}\n\\label{tab:d_study_transfer}\n\\begin{tabular}{lccc}\n\\toprule\nBenchmark & MMLU-Derived $G$ & Actual $G$ & $\\Delta$ \\\\\n\\midrule\nMMLU          & 0.800 & 0.800 & 0.000 \\\\\nARC-Challenge & 0.800 & 0.768 & 0.032 \\\\\nGSM8K         & 0.800 & 0.753 & 0.047 \\\\\nHellaSwag     & 0.800 & 0.742 & 0.058 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMMLU-derived budgets overestimate $G$ on other benchmarks by 3.2--5.8 percentage points, primarily because MMLU has lower residual variance (19.5\\%) than GSM8K (22.6\\%) or HellaSwag (17.4\\% residual but higher model$\\times$item at 35.2\\%).\nPractitioners applying MMLU-derived budgets to other benchmarks should add a 10--15\\% safety margin on item counts.\nDespite this transfer error, the qualitative conclusion is preserved: all four benchmarks require 400--650 items for $G \\geq 0.80$ under practical conditions.\n\n\\paragraph{Cross-benchmark separability.}\nTable~\\ref{tab:separability} reports precision$\\times$methodology interactions across benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Precision$\\times$methodology interaction by benchmark (binary scoring, 4 models).}\n\\label{tab:separability}\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & Prec.$\\times$Prompt & Prec.$\\times$Seed & Prec.$\\times$Temp & Total \\\\\n\\midrule\nMMLU          & 0.02\\% & 0.01\\% & 0.05\\% & 0.08\\% \\\\\nARC-Challenge & 0.9\\%  & 0.5\\%  & 1.0\\%  & 2.4\\%  \\\\\nGSM8K         & 1.2\\%  & 0.8\\%  & 1.6\\%  & 3.6\\%  \\\\\nHellaSwag     & 1.6\\%  & 1.1\\%  & 2.1\\%  & 4.8\\%  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPrecision$\\times$methodology separability holds on MMLU (total interaction $<$ 0.1\\%) but does not generalize: HellaSwag reaches 4.8\\% total interaction under binary scoring.\nSeparability is therefore benchmark-dependent and should not be assumed as a universal property.\nWe note this as an observation rather than a primary contribution.\n\n\\subsection{Exp-003: Multi-Hardware G-Study (Partial)}\n\\label{sec:exp003}\n\nA second GPU type (RTX A6000 48GB) became available four weeks before deadline, enabling a partial hardware crossing with 2 models (Llama, Mistral) under 576 conditions each (230,400 records total).\nTable~\\ref{tab:hardware} reports hardware$\\times$methodology interactions.\n\n\\begin{table}[t]\n\\centering\n\\caption{Hardware$\\times$methodology interaction breakdown (2 models, binary scoring, RTX PRO 6000 vs.\\ RTX A6000).}\n\\label{tab:hardware}\n\\begin{tabular}{lccc}\n\\toprule\nInteraction & Llama \\% & Mistral \\% & Average \\% \\\\\n\\midrule\nHardware$\\times$Temperature & 1.1 & 1.7 & 1.4 \\\\\nHardware$\\times$Precision   & 0.7 & 1.1 & 0.9 \\\\\nHardware$\\times$Prompt      & 0.5 & 0.7 & 0.6 \\\\\nHardware$\\times$Seed        & 0.2 & 0.4 & 0.3 \\\\\nHardware$\\times$Item        & 2.4 & 3.2 & 2.8 \\\\\nHardware main effect        & 1.3 & 2.3 & 1.8 \\\\\n\\midrule\nTotal hardware$\\times$methodology & 3.8 & 4.6 & 4.2 \\\\\nTotal hardware-related      & 6.2 & 9.4 & 7.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHardware$\\times$methodology interaction averages 4.2\\% across the two models---substantially larger than the within-single-GPU precision$\\times$methodology interaction of 0.08\\%.\nThe largest sub-interaction is hardware$\\times$temperature (1.4\\%), attributable to different CUDA RNG implementations across GPU architectures (Ada Lovelace sm\\_89 vs.\\ Ampere sm\\_86) producing different pseudo-random sequences even under identical seeds.\nHardware$\\times$item (2.8\\%) reflects a small number of items ($\\sim$5--8) near the decision boundary where kernel-level numerical differences flip predictions.\n\nMistral shows higher hardware interaction (4.6\\%) than Llama (3.8\\%), consistent with Mistral's lower accuracy (61.2\\% vs.\\ 68.1\\%) placing more items near the decision boundary.\nThe single-GPU $G_{\\text{binary}}$ of 0.611 degrades to 0.582 when hardware is added as a facet ($\\Delta G = 0.029$).\n\nThese results are preliminary (2 of 4 models) but sufficient to conclude that the precision separability observed within a single GPU environment does not extend across GPU architectures.\nAll separability-related conclusions in this paper are accordingly qualified to single-GPU, single-architecture settings.\n\n\\subsection{Exp-004: Comprehensive Analysis}\n\\label{sec:exp004}\n\nDrawing on all collected data, we conducted 13 of 17 planned analyses (4 blocked by incomplete hardware crossing).\nKey results are summarized below.\n\n\\paragraph{D-study budget recommendations.}\nTable~\\ref{tab:d_study_budgets} presents benchmark-specific evaluation budgets for achieving $G \\geq 0.80$.\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study budget recommendations by benchmark ($G \\geq 0.80$, practical design with temperature and ordering fixed).}\n\\label{tab:d_study_budgets}\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & Items & Prompts & Seeds & Projected $G$ [95\\% CI] \\\\\n\\midrule\nMMLU          & 510 & 2 & 3 & 0.800 [0.782, 0.825] \\\\\nARC-Challenge & 538 & 2 & 3 & 0.800 [0.778, 0.826] \\\\\nGSM8K         & 624 & 3 & 4 & 0.801 [0.774, 0.831] \\\\\nHellaSwag     & 652 & 3 & 4 & 0.802 [0.771, 0.838] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll benchmarks require 500--650 items with multiple prompts and seeds.\nCurrent standard practice (1 prompt, 1 seed, $\\leq$200 items) yields $G = 0.611$ on MMLU---below the 0.80 threshold for dependable measurement.\nUsing the full 14,042 MMLU items projects to $G = 0.972$, indicating that the complete benchmark is highly reliable but that common subsampling practices are not.\n\n\\paragraph{Methodological robustness.}\nTable~\\ref{tab:robustness} summarizes the robustness verification package.\n\n\\begin{table}[t]\n\\centering\n\\caption{Methodological robustness summary.}\n\\label{tab:robustness}\n\\begin{tabular}{lll}\n\\toprule\nAnalysis & Result & Status \\\\\n\\midrule\nBinary not artifact (null sim) & item$_{\\text{id}}$ = 0.08\\% vs.\\ obs.\\ 61.1\\% (737$\\times$) & PASS \\\\\nFixed vs.\\ random sensitivity  & max $\\Delta(G)$ = 0.053 & PASS \\\\\nBootstrap = Jackknife CIs      & ratio range [0.96, 1.04] & PASS \\\\\nREML vs.\\ Henderson I          & max diff $<$ 0.4pp & PASS \\\\\nTemp.\\ stratification           & binary $G$: 0.760 $\\to$ 0.549 ($T$=0 $\\to$ 0.7) & PASS \\\\\nBernoulli variance correlation & $r = 0.91$ & NOTED \\\\\nD-study cross-bench transfer   & $\\Delta$ = 0.032--0.058 & CAVEAT \\\\\nLOMO matched spread            & spread = 0.058 & CAVEAT \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\\label{sec:robustness}\n\nSix of eight analyses pass cleanly.\nThe null simulation confirms that observed item variance is not a Bernoulli artifact: simulated item$_{\\text{id}}$ under independence is 0.08\\% versus observed 61.1\\%.\nFixed vs.\\ random facet classification produces $G$ values ranging from 0.611 (all random) to 0.664 (temperature and ordering fixed), a maximum shift of 0.053---qualitative conclusions are robust.\nBootstrap and delete-1 jackknife confidence intervals agree (ratio 0.96--1.04), indicating that item-level resampling violations are negligible.\nREML-EM (500 iterations, practical convergence $\\Delta < 0.003$pp) confirms Henderson's Method~I within 0.4pp on all components.\n\nTwo caveated results require transparent reporting.\nThe D-study cross-benchmark transfer error ($\\Delta = 0.032$--$0.058$) means MMLU-derived budgets are approximately but not exactly portable.\nThe LOMO matched-specification spread (0.058) indicates that 4-model estimates have approximately 3\\% standard deviation; stable estimates require $\\sim$10 models.\n\n\\paragraph{Logprob analysis.}\nLogprob-based scoring produces tighter cross-benchmark variance structure (item dominance range = 3.5pp vs.\\ 5.7pp for binary scoring), suggesting that continuous scoring reduces benchmark-dependence.\nItem dominance under logprob scoring: MMLU 48.3\\%, GSM8K 44.8\\%, ARC 46.1\\%, HellaSwag 45.9\\%.\n\n\\paragraph{Computational cost.}\nAchieving $G \\geq 0.80$ requires approximately 340 GPU-hours on MMLU, 415 on GSM8K, and 430 on HellaSwag (using a single RTX PRO 6000).\n$G \\geq 0.90$ on MMLU requires $\\sim$890 GPU-hours.\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{The model$\\times$item interaction as a hidden factor.}\nThe central finding of this work is that model$\\times$item interaction accounts for 33.6\\% of cross-model evaluation variance on MMLU---nearly as large as item selection itself (42.1\\%).\nThis means that item difficulty rankings are substantially model-specific: an item that is easy for Llama may be difficult for Mistral, and vice versa.\nSingle-model G-studies (or ANOVA decompositions) inflate item dominance by up to 19 percentage points by absorbing this interaction into the item component.\nThis has direct implications for benchmark design: item selection strategies based on single-model difficulty estimates (e.g., selecting ``hard'' items based on one model's performance) will not generalize across models.\n\n\\paragraph{Practical implications of benchmark-invariance.}\nThe approximate invariance of variance structure across four benchmarks (item dominance range = 5.7pp) is a practically useful finding.\nIt means that practitioners who have conducted a thorough G-study on one benchmark can cautiously apply the resulting evaluation budgets to related benchmarks, with a 10--15\\% safety margin on item counts to account for the 3--6pp $G$-coefficient transfer error.\nThis is substantially more efficient than conducting a full G-study on every benchmark of interest.\n\n\\paragraph{When is IRT sufficient?}\nThe benchmark-dependent IRT-to-G-theory ratio (1.6--4.1$\\times$) provides a principled answer to when IRT-based subsampling is ``good enough.''\nOn reasoning benchmarks where item discrimination is relatively uniform (HellaSwag, GSM8K), IRT approaches G-theory's item requirements (ratio $<$ 2$\\times$), and the additional cost of a full G-study may not be justified.\nOn knowledge benchmarks with heterogeneous discrimination (MMLU), the 4.1$\\times$ gap indicates that IRT substantially underestimates the items needed for reliable multi-facet measurement.\n\n\\paragraph{Hardware separability is limited.}\nThe partial two-GPU study reveals that hardware$\\times$methodology interaction (4.2\\%) exceeds within-GPU precision$\\times$methodology interaction (0.08\\%) by approximately 50$\\times$.\nWhile this interaction is small relative to item (42.1\\%) and model$\\times$item (33.6\\%), it is large enough to shift $G$ by 0.029 points.\nEvaluation studies claiming reproducibility across hardware configurations should empirically verify this assumption rather than extrapolating from single-GPU precision studies.\n\n\\paragraph{Extending to fine-tuning.}\nG-theory naturally extends to fine-tuning variance, where training seed, learning rate, and data ordering are additional facets.\n\\citet{dodge2020finetuning} and \\citet{bui2025seed} provide preliminary evidence that seed and learning rate dominate fine-tuning variance; a full G-theory treatment of fine-tuning is a natural next step.\n\n\\subsection{Limitations}\n\n\\textbf{Model sample size.}\nAll results are based on 4 models in the 7--9B parameter range.\nThe LOMO spread of 0.058 indicates that point estimates have approximately 3\\% standard deviation; D-study projections suggest 10+ models are needed for stable estimates.\nScale validation (14B+ models) and closed-source API models remain for future work.\n\n\\textbf{Item sample size.}\nThe resampling CV of 0.143 shows that 200-item subsamples produce moderately variable variance estimates.\nAll reported confidence intervals account for this variability via bootstrap resampling.\n\n\\textbf{Binary data.}\nWhile null simulations and REML robustness checks support the validity of G-theory on binary data, the Bernoulli variance correlation ($r = 0.91$) indicates that a portion of item variance is mechanically linked to item difficulty.\nGeneralized G-theory with logistic link functions \\citep{jiang2017generalized} would provide a more principled treatment.\n\n\\textbf{Hardware crossing.}\nThe multi-GPU analysis covers only 2 of 4 models on 2 GPU architectures.\nFull hardware crossing is needed to quantify the hardware facet at the same precision as other facets.\n\n\\textbf{Judge exclusion.}\nBy fixing evaluation to exact-match scoring, we exclude judge variance---the largest source in \\citet{mesting2026generalizability}'s analysis.\nOur results are therefore specific to closed-form evaluation metrics.\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe presented a multi-benchmark Generalizability Theory analysis of LLM evaluation variance across 4 models, 4 benchmarks, and over 2.3 million evaluation records.\nThree findings emerge.\nFirst, model$\\times$item interaction accounts for 33.6\\% of cross-model variance on MMLU---nearly as large as item selection (42.1\\%)---revealing that item difficulty rankings are substantially model-specific.\nA D-study predicted the 4-model generalizability coefficient within $\\Delta = 0.004$, validating G-theory's projective machinery for LLM evaluation.\nSecond, G-theory requires 1.6--4.1$\\times$ more items than IRT for reliable measurement, with the ratio being benchmark-dependent.\nThird, variance structure is approximately benchmark-invariant (item dominance range = 5.7pp across four benchmarks), enabling cautious cross-benchmark extrapolation of evaluation budgets with a 3--6pp safety margin.\nCurrent evaluation practices (1 prompt, 1 seed, $\\leq$200 items) yield $G = 0.611$ on MMLU, well below the 0.80 reliability threshold.\nWe release an open-source G-theory pipeline and D-study calculator to support more rigorous evaluation design.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Biderman et~al.(2024)]{biderman2024lessons}\nS.~Biderman, et~al.\n\\newblock Lessons from the trenches on reproducible evaluation of language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.14782}, 2024.\n\n\\bibitem[Bouthillier et~al.(2021)]{bouthillier2021accounting}\nX.~Bouthillier, et~al.\n\\newblock Accounting for variance in machine learning benchmarks.\n\\newblock \\emph{Proceedings of Machine Learning and Systems}, 3:747--769, 2021.\n\n\\bibitem[Brennan(2001)]{brennan2001generalizability}\nR.~L. Brennan.\n\\newblock \\emph{Generalizability Theory}.\n\\newblock Springer-Verlag, 2001.\n\n\\bibitem[BrittleBench(2026)]{brittlebench2026}\nBrittleBench Team.\n\\newblock BrittleBench: Quantifying prompt sensitivity in LLM evaluation.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Bui et~al.(2025)]{bui2025seed}\nT.~Bui, et~al.\n\\newblock Extreme seed sensitivity in fine-tuning: RTES variance analysis.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\bibitem[Dehghani et~al.(2021)]{dehghani2021benchmark}\nM.~Dehghani, et~al.\n\\newblock The benchmark lottery.\n\\newblock \\emph{arXiv preprint arXiv:2107.07002}, 2021.\n\n\\bibitem[Dodge et~al.(2020)]{dodge2020finetuning}\nJ.~Dodge, et~al.\n\\newblock Fine-tuning pretrained language models: Weight initializations, data orders, and early stopping.\n\\newblock \\emph{arXiv preprint arXiv:2002.06305}, 2020.\n\n\\bibitem[Henderson et~al.(2018)]{henderson2018deep}\nP.~Henderson, et~al.\n\\newblock Deep reinforcement learning that matters.\n\\newblock In \\emph{AAAI}, 2018.\n\n\\bibitem[Hua et~al.(2025)]{hua2025emnlp}\nH.~Hua, et~al.\n\\newblock Generation-based evaluation for LLMs.\n\\newblock In \\emph{EMNLP}, 2025.\n\n\\bibitem[Jiang \\& Skorupski(2017)]{jiang2017generalized}\nZ.~Jiang and W.~P. Skorupski.\n\\newblock A generalized G-theory model for binary data.\n\\newblock \\emph{Applied Psychological Measurement}, 41(6):443--458, 2017.\n\n\\bibitem[Kunievsky \\& Evans(2025)]{kunievsky2025alternative}\nD.~Kunievsky and O.~Evans.\n\\newblock Decomposing evaluation variance: Intent, articulation, and model uncertainty.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\bibitem[Lalor et~al.(2019)]{lalor2019learning}\nJ.~P. Lalor, et~al.\n\\newblock Learning latent parameters without human response patterns: Item response theory with artificial crowds.\n\\newblock In \\emph{EMNLP-IJCNLP}, 2019.\n\n\\bibitem[Lu et~al.(2022)]{lu2022fantastically}\nY.~Lu, et~al.\n\\newblock Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity.\n\\newblock In \\emph{ACL}, 2022.\n\n\\bibitem[Messina \\& Scotta(2026)]{messina2026floating}\nE.~Messina and R.~Scotta.\n\\newblock Floating-point non-associativity in neural network inference.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Mesting(2026)]{mesting2026generalizability}\nF.~Mesting.\n\\newblock Generalizability theory for LLM evaluation: A five-facet analysis.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Mushquash \\& O'Connor(2006)]{mushquash2006generalizability}\nC.~Mushquash and B.~P. O'Connor.\n\\newblock SPSS and SAS programs for generalizability theory analyses.\n\\newblock \\emph{Behavior Research Methods}, 38(3):542--547, 2006.\n\n\\bibitem[Perlitz et~al.(2023)]{perlitz2023efficient}\nY.~Perlitz, et~al.\n\\newblock Efficient benchmarking (of language models).\n\\newblock \\emph{arXiv preprint arXiv:2308.11696}, 2023.\n\n\\bibitem[Pezeshkpour \\& Hruschka(2024)]{pezeshkpour2024large}\nP.~Pezeshkpour and E.~Hruschka.\n\\newblock Large language models sensitivity to the order of options in multiple-choice questions.\n\\newblock In \\emph{NAACL Findings}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo, et~al.\n\\newblock tinyBenchmarks: Evaluating LLMs with fewer examples.\n\\newblock \\emph{arXiv preprint arXiv:2402.14992}, 2024.\n\n\\bibitem[Rodriguez et~al.(2021)]{rodriguez2021evaluation}\nP.~Rodriguez, et~al.\n\\newblock Evaluation examples are not equally informative: How should that change NLP leaderboards?\n\\newblock In \\emph{ACL}, 2021.\n\n\\bibitem[Sclar et~al.(2024)]{sclar2024quantifying}\nM.~Sclar, et~al.\n\\newblock Quantifying language models' sensitivity to spurious features in prompt design.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Sellam et~al.(2022)]{sellam2022multberts}\nT.~Sellam, et~al.\n\\newblock The MultiBERTs: BERT reproductions for robustness analysis.\n\\newblock In \\emph{ICLR}, 2022.\n\n\\bibitem[Shavelson \\& Webb(1991)]{shavelson1991generalizability}\nR.~J. Shavelson and N.~M. Webb.\n\\newblock \\emph{Generalizability Theory: A Primer}.\n\\newblock Sage, 1991.\n\n\\bibitem[Shavelson et~al.(1989)]{shavelson1989generalizability}\nR.~J. Shavelson, et~al.\n\\newblock Generalizability of binary items.\n\\newblock \\emph{Journal of Educational Measurement}, 26(3):231--244, 1989.\n\n\\bibitem[Vania et~al.(2021)]{vania2021comparing}\nC.~Vania, et~al.\n\\newblock Comparing test sets with item response theory.\n\\newblock In \\emph{ACL}, 2021.\n\n\\bibitem[Yuan et~al.(2025)]{yuan2025precision}\nZ.~Yuan, et~al.\n\\newblock Precision matters: Up to 9\\% accuracy variation from numerical precision in LLM inference.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da623921-a31e-42de-8691-11b5e2ec141b",
  "isSidechain": false,
  "requestId": "req_011CbFQ5NzuyqdSNyDVZjB5B",
  "type": "assistant",
  "uuid": "f856b981-1072-49a5-b674-4d2ab142a248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DnJRHtvNV6JLKJVi3GrgU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7745,
      "cache_read_input_tokens": 40437,
      "output_tokens": 14632,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14632,
          "cache_read_input_tokens": 40437,
          "cache_creation_input_tokens": 7745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7745
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

_source line 22 · 2026-05-21T08:32:57.631Z_

<details><summary>↩ Tool result · `toolu_01TSxkxWT3JwpgNvfA1Kqism`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f856b981-1072-49a5-b674-4d2ab142a248",
  "isSidechain": false,
  "promptId": "9d021380-77fd-4766-a060-794a49f7c1c1",
  "type": "user",
  "uuid": "b954157f-051c-4df6-98b6-4c819aade514",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/paper.tex",
    "content": "\\documentclass[letterpaper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{array}\n\\usepackage{caption}\n\n\\title{The Hidden Second Factor: Model$\\times$Item Interaction Accounts for 34\\% of LLM Evaluation Variance}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWhen LLM evaluation results vary across reproductions, practitioners cannot determine whether the variance originates from prompt phrasing, random seeds, numerical precision, temperature, or item selection---let alone how these factors interact.\nWe conduct a multi-benchmark Generalizability Theory (G-theory) study crossing infrastructure and methodology factors across 4 open-weight models (7--9B parameters) on MMLU, GSM8K, ARC-Challenge, and HellaSwag, totaling over 2.3 million evaluation records.\nOn MMLU (345,600 balanced cross-model records), item selection accounts for 42.1\\% of variance and model$\\times$item interaction emerges as the second-largest source at 33.6\\%, revealing that item difficulty rankings are substantially model-specific: single-model analyses inflate item dominance from 42\\% to 61\\% by conflating universal and model-specific difficulty.\nA Decision study (D-study) predicted the 4-model generalizability coefficient within $\\Delta=0.004$ of the observed value, providing out-of-sample validation.\nAcross four benchmarks, variance structure is approximately invariant (item dominance range = 5.7 percentage points), enabling cautious cross-benchmark extrapolation of MMLU-derived evaluation budgets with a 3--6 percentage-point safety margin.\nG-theory requires 1.6--4.1$\\times$ more items than IRT for reliable measurement, with the ratio being benchmark-dependent---resolving conflicting conclusions in the literature about IRT sufficiency.\nA partial two-GPU study reveals that hardware$\\times$methodology interaction reaches 4.2\\%, breaking the separability assumption that holds within single-GPU environments ($<$0.1\\%).\nWe release an open-source G-theory variance decomposition pipeline and D-study budget calculator.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nReproducibility failures in LLM evaluation undermine the credibility of benchmark-based comparisons.\nA model declared superior on MMLU under one evaluation protocol may lose its advantage under a different prompt template \\citep{sclar2024quantifying}, random seed \\citep{bui2025seed}, or numerical precision setting \\citep{yuan2025precision}.\nYet each prior study isolates at most one or two variance sources, implicitly assuming that these factors do not interact.\nThe field lacks a unified framework for simultaneously attributing evaluation variance to all relevant sources and their interactions.\n\nGeneralizability Theory (G-theory; \\citealt{shavelson1991generalizability, brennan2001generalizability}) provides exactly this framework.\nOriginally developed in educational measurement, G-theory decomposes observed variance into contributions from every facet (e.g., items, raters, occasions) and their interactions in a single analysis, then projects reliability under hypothetical measurement designs via Decision studies (D-studies).\n\\citet{mesting2026generalizability} adapted G-theory to LLM evaluation with five methodological facets on a single benchmark, establishing feasibility but leaving infrastructure factors, cross-benchmark comparisons, and model-as-facet analysis unexplored.\n\nWe extend this line of work with three contributions:\n\n\\textbf{(1) Model$\\times$item interaction quantification.}\nIn a balanced 4-model MMLU design (345,600 records), model$\\times$item interaction accounts for 33.6\\% [95\\% CI: 28.4--37.9\\%] of total variance---the second-largest source after item selection (42.1\\%).\nSingle-model analyses inflate item dominance to 61.1\\% by conflating universal and model-specific item difficulty.\nA D-study from 3 models predicted the 4-model generalizability coefficient ($G$) within $\\Delta = 0.004$, providing out-of-sample validation that G-theory's projective machinery works for LLM evaluation.\n\n\\textbf{(2) IRT vs.\\ G-theory direct comparison.}\nG-theory requires 3.6--4.1$\\times$ more items than IRT on MMLU to reach the same reliability target, because it accounts for prompt, seed, and ordering dimensions that IRT ignores.\nThis ratio is benchmark-dependent, ranging from 1.6$\\times$ (HellaSwag) to 4.1$\\times$ (MMLU), explaining why the field has not converged on whether IRT-based subsampling is sufficient.\n\n\\textbf{(3) Approximate benchmark-invariance of variance structure.}\nAcross MMLU, GSM8K, ARC-Challenge, and HellaSwag, the item dominance proportion varies by only 5.7 percentage points (38.4--44.1\\%), and the variance component ranking is preserved.\nMMLU-derived evaluation budgets transfer to other benchmarks with a 3--6 percentage-point $G$-coefficient error, enabling cautious cross-benchmark extrapolation.\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Variance decomposition in ML evaluation.}\n\\citet{bouthillier2021accounting} decomposed ML benchmark variance across hyperparameters, data splits, and random seeds via ANOVA, establishing factorial variance decomposition as a methodology for ML evaluation.\n\\citet{henderson2018deep} documented large variance across seeds in deep reinforcement learning.\n\\citet{dodge2020finetuning} and \\citet{sellam2022multberts} quantified fine-tuning instability from seeds and data ordering in BERT-scale models.\n\\citet{bui2025seed} extended this to instruction-tuned LLMs, finding extreme seed sensitivity (RTES variance up to 18.22 for RoBERTa on COPA).\n\n\\paragraph{Prompt and evaluation sensitivity.}\n\\citet{sclar2024quantifying} demonstrated up to 76\\% accuracy swings from prompt formatting alone.\n\\citet{lu2022fantastically} and \\citet{pezeshkpour2024large} documented option-ordering effects in multiple-choice evaluation.\nBrittleBench \\citep{brittlebench2026} quantified prompt sensitivity at 50\\% variance on fixed hardware.\n\n\\paragraph{Infrastructure effects.}\n\\citet{yuan2025precision} documented up to 9\\% accuracy variation from hardware and numerical precision without factorial attribution.\n\\citet{messina2026floating} identified floating-point non-associativity as a mechanism for cross-hardware divergence.\n\n\\paragraph{G-theory in LLM evaluation.}\n\\citet{mesting2026generalizability} adapted G-theory to LLM evaluation with 5 methodological facets on a single benchmark, finding judge identity as the dominant variance source (43.8\\%).\nWe build on this by (a) adding infrastructure as a facet, (b) treating model as a crossed facet to expose model$\\times$item interaction, (c) extending to four benchmarks, and (d) fixing the judge to isolate non-judge variance sources.\n\\citet{shavelson1991generalizability} and \\citet{brennan2001generalizability} provide the canonical G-theory references; \\citet{jiang2017generalized} and \\citet{mushquash2006generalizability} address G-theory for binary response data.\n\n\\paragraph{IRT-based evaluation.}\n\\citet{lalor2019learning} introduced IRT-based item analysis for NLP evaluation.\n\\citet{rodriguez2021evaluation} and \\citet{vania2021comparing} further developed IRT applications in NLP benchmarking.\n\\citet{polo2024tinybenchmarks} proposed IRT-based subsampling (tinyBenchmarks), recommending $\\sim$100 items for reliable evaluation.\n\\citet{perlitz2023efficient} explored efficient benchmarking strategies.\nOur work provides the first direct comparison of IRT and G-theory item requirements, quantifying the cost of multi-facet reliability.\n\n\\paragraph{Alternative frameworks.}\n\\citet{kunievsky2025alternative} proposed decomposing evaluation variance into intent, articulation, and model uncertainty---a complementary perspective to G-theory's facet-based approach.\n\\citet{dehghani2021benchmark} argued that benchmark selection itself is a variance source (the ``Benchmark Lottery'').\n\\citet{biderman2024lessons} synthesized practical lessons for evaluation reproducibility.\n\n% ============================================================\n% 3. METHOD\n% ============================================================\n\\section{Method}\n\n\\subsection{Generalizability Theory Background}\n\nG-theory \\citep{shavelson1991generalizability, brennan2001generalizability} partitions observed score variance into components attributable to each facet and their interactions.\nFor a fully crossed design with items ($i$), prompts ($p$), seeds ($s$), temperatures ($t$), orderings ($o$), and precision ($r$), the observed score $X_{ipstor}$ decomposes as:\n\\begin{equation}\nX_{ipstor} = \\mu + \\alpha_i + \\beta_p + \\gamma_s + \\delta_t + \\epsilon_o + \\zeta_r + (\\alpha\\beta)_{ip} + \\cdots + e_{ipstor}\n\\end{equation}\nwhere each Greek letter denotes a main effect and parenthesized terms denote interactions.\nVariance components $\\hat{\\sigma}^2$ are estimated via Henderson's Method I (expected mean squares), with REML as a robustness check.\n\nThe \\textbf{generalizability coefficient} $G$ quantifies reliability:\n\\begin{equation}\nG = \\frac{\\hat{\\sigma}^2_i}{\\hat{\\sigma}^2_i + \\sum_{f \\neq i} \\frac{\\hat{\\sigma}^2_f}{n_f}}\n\\end{equation}\nwhere the sum runs over all non-item variance components divided by their respective sample sizes.\n\nA \\textbf{D-study} projects $G$ under hypothetical designs by varying $n_f$, enabling practitioners to determine the number of items, prompts, and seeds needed for a target reliability.\n\nWhen model is treated as a crossed facet, the item variance component splits into universal item difficulty ($\\hat{\\sigma}^2_i$) and model$\\times$item interaction ($\\hat{\\sigma}^2_{mi}$).\nThe generalizability of item difficulty rankings across models is captured by:\n\\begin{equation}\nG_{\\text{item}} = \\frac{\\hat{\\sigma}^2_i}{\\hat{\\sigma}^2_i + \\hat{\\sigma}^2_{mi} / n_m + \\hat{\\sigma}^2_{e} / (n_m \\cdot n_{\\text{cond}})}\n\\end{equation}\n\n\\paragraph{Binary data considerations.}\nOur primary metric (binary correct/incorrect) violates G-theory's normality assumption.\nWe address this via: (a) null simulations showing observed item variance exceeds Bernoulli-mechanical variance by 737$\\times$ (Section~\\ref{sec:robustness}); (b) parallel analysis on text-exact-match scoring; (c) sensitivity to fixed/random facet classification ($\\Delta G < 0.053$).\n\\citet{shavelson1989generalizability}, \\citet{mushquash2006generalizability}, and \\citet{jiang2017generalized} provide theoretical justification for G-theory with binary responses.\n\n\\subsection{Experimental Design}\n\n\\paragraph{Models.}\nFour open-weight instruction-tuned models in the 7--9B parameter range: Llama-3.1-8B-Instruct, Gemma-2-9B-it, Mistral-7B-Instruct-v0.3, and Qwen-2.5-7B-Instruct.\nAll inference uses vLLM 0.9.2 with default settings (no batch-invariant kernels), making CUDA-level nondeterminism a measurable variance source.\n\n\\paragraph{Benchmarks.}\nMMLU (primary, 200 stratified items from 57 subjects), GSM8K (200 items), ARC-Challenge (200 items), and HellaSwag (200 items).\n\n\\paragraph{Facets.}\n\\begin{itemize}\n  \\item \\textbf{Precision}: BF16, FP16 (FP32 excluded after identifying vLLM \\texttt{enforce\\_eager} confound; BF16$\\approx$FP16, $\\Delta=0.23$pp accuracy)\n  \\item \\textbf{Prompt}: 6 semantically equivalent templates\n  \\item \\textbf{Seed}: 6 random seeds\n  \\item \\textbf{Temperature}: $T \\in \\{0.0, 0.3, 0.7\\}$ (MMLU); $\\{0.0, 0.7\\}$ (others)\n  \\item \\textbf{Ordering}: 4 systematic option rotations\n  \\item \\textbf{Hardware}: RTX PRO 6000 96GB (primary); RTX A6000 48GB (partial crossing, 2 models)\n\\end{itemize}\n\n\\paragraph{Design structure.}\nExp-001 (MMLU): $4 \\text{ models} \\times 3 \\text{ precisions} \\times 6 \\text{ prompts} \\times 6 \\text{ seeds} \\times 3 \\text{ temperatures} \\times 4 \\text{ orderings} \\times 200 \\text{ items} = 930{,}400$ records.\nCross-model balanced analysis uses BF16 shared conditions: 432 conditions/model $\\times$ 4 models $\\times$ 200 items $= 345{,}600$ records.\nExp-002 (GSM8K, ARC, HellaSwag): $4 \\times 2 \\times 6 \\times 6 \\times 2 \\times 4 \\times 200 = 460{,}800$ records per benchmark (1,382,400 total).\nExp-003 (hardware crossing): 2 models $\\times$ 576 conditions $\\times$ 200 items $= 230{,}400$ records (partial).\n\n\\paragraph{Judge exclusion.}\nUnlike \\citet{mesting2026generalizability}, who includes judge as a facet (finding 43.8\\% judge variance), we fix evaluation to exact-match scoring to isolate infrastructure$\\times$methodology interactions.\nJudge variance is a natural extension for future work.\n\n% ============================================================\n% 4. EXPERIMENTS AND RESULTS\n% ============================================================\n\\section{Experiments and Results}\n\n\\subsection{Exp-001: Cross-Model MMLU Variance Decomposition}\n\\label{sec:exp001}\n\nTable~\\ref{tab:cross_model_decomp} presents the cross-model variance decomposition from the balanced 4-model BF16 design (345,600 records).\nItem selection is the largest source (42.1\\%, CI [36.0, 48.8]), followed by model$\\times$item interaction (33.6\\%, CI [28.4, 37.9]).\nTogether, these two sources account for 75.7\\% of total variance.\nResidual variance (19.5\\%) is the third-largest component; all other sources (prompt$\\times$item, seed$\\times$item, temperature, model main effect, precision) contribute $\\leq$4.7\\% each.\nPrecision is negligible at 0.0006\\%.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model variance decomposition (4 models, MMLU, balanced BF16, 345,600 records). CI = 95\\% bootstrap confidence interval ($B=1{,}000$).}\n\\label{tab:cross_model_decomp}\n\\begin{tabular}{lccc}\n\\toprule\nSource & \\% Variance & CI Lower & CI Upper \\\\\n\\midrule\nItem ($i$)                  & 42.1 & 36.0 & 48.8 \\\\\nModel$\\times$Item ($m \\times i$) & 33.6 & 28.4 & 37.9 \\\\\nResidual                    & 19.5 & 16.2 & 23.1 \\\\\nSeed$\\times$Item            & 4.7  & 3.2  & 6.5  \\\\\nPrompt$\\times$Item          & 4.6  & 3.1  & 6.4  \\\\\nTemperature                 & 1.2  & 0.4  & 2.3  \\\\\nModel                       & 0.8  & 0.1  & 2.1  \\\\\nOther interactions          & 0.5  & 0.1  & 1.2  \\\\\nPrecision                   & 0.0006 & 0.0 & 0.002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe generalizability of item difficulty rankings across models is $G_{\\text{item}} = 0.820$ [0.782, 0.861].\nA D-study using 3-model subsets predicted $G_{\\text{item}} = 0.816$ for $n_m = 4$; the observed value is 0.820 ($\\Delta = 0.004$), validating D-study projections out of sample.\nForward projections indicate $G_{\\text{item}} = 0.848$ at 5 models, 0.893 at 8, and 0.910 at 10; reaching $G \\geq 0.90$ requires approximately 10 models.\n\n\\paragraph{Single-model inflation effect.}\nTable~\\ref{tab:per_model_decomp} shows per-model single-model decompositions.\nItem selection accounts for 55.6--61.1\\% in single-model analyses versus 42.1\\% in the cross-model analysis---an inflation of up to 19 percentage points.\nThis inflation occurs because single-model analyses conflate universal item difficulty with model-specific item difficulty (model$\\times$item interaction).\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-model single-model variance decomposition (\\% of total variance, MMLU).}\n\\label{tab:per_model_decomp}\n\\begin{tabular}{lcccc}\n\\toprule\nSource & Llama & Gemma & Mistral & Qwen \\\\\n\\midrule\nItem ($i$)             & 61.1 & 57.8 & 59.4 & 55.6 \\\\\nResidual               & 17.2 & 19.1 & 18.4 & 20.8 \\\\\nPrecision$\\times$Item  & 7.2  & 7.8  & 7.1  & 6.5  \\\\\nPrompt$\\times$Item     & 4.6  & 5.3  & 4.9  & 6.2  \\\\\nSeed$\\times$Item       & 4.7  & 4.5  & 4.6  & 5.1  \\\\\nTemp.$\\times$Item      & 3.1  & 3.4  & 3.2  & 3.6  \\\\\nTemperature            & 1.2  & 1.1  & 1.5  & 1.2  \\\\\nPrecision              & 0.5  & 0.6  & 0.5  & 0.7  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPer-model interaction magnitudes (from the cross-model analysis) correlate inversely with model accuracy: Mistral (29.25\\%, accuracy 63.8\\%) $>$ Qwen (27.11\\%) $>$ Gemma (23.95\\%) $>$ Llama (19.69\\%, accuracy 66.4\\%).\nLower-accuracy models show more model-specific item difficulty patterns, consistent with the interpretation that models near the decision boundary on more items exhibit greater item-level disagreement.\n\n\\paragraph{Leave-one-model-out stability.}\nTable~\\ref{tab:lomo} reports matched-specification leave-one-model-out (LOMO) results using a reduced balanced design (BF16 $\\times$ 4 prompts $\\times$ 4 seeds $\\times$ 2 temperatures $\\times$ 2 orderings = 64 conditions/model).\nThe $G_{\\text{item}}$ spread across 3-model subsets is 0.058 (range: 0.788--0.846), with a standard deviation of 0.026.\n\n\\begin{table}[t]\n\\centering\n\\caption{Leave-one-model-out matched-specification $G_{\\text{item}}$ analysis.}\n\\label{tab:lomo}\n\\begin{tabular}{lccc}\n\\toprule\nDropped Model & $G_{\\text{item}}$ & Item \\% & Model$\\times$Item \\% \\\\\n\\midrule\nMistral & 0.846 & 44.8 & 28.3 \\\\\nQwen    & 0.834 & 43.2 & 30.1 \\\\\nGemma   & 0.802 & 40.5 & 35.8 \\\\\nLlama   & 0.788 & 39.1 & 37.6 \\\\\n\\midrule\nAll 4   & 0.820 & 42.1 & 33.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis spread reflects sensitivity to model selection with only 4 models.\nDropping Llama (the model with the lowest interaction, 19.69\\%) produces the lowest $G_{\\text{item}}$ (0.788) because the remaining three models have higher and more heterogeneous interaction patterns.\nCritically, all four subsets preserve the qualitative conclusions: item selection remains the largest source ($>$39\\%), model$\\times$item is second-largest, and $G_{\\text{item}} > 0.78$ throughout.\nThe D-study projection to 10 models ($G = 0.910$) indicates that this instability is a consequence of small model samples, not a fundamental limitation of the approach.\n\n\\paragraph{BF16 vs.\\ FP16 sensitivity.}\nExcluding FP32 (identified as a vLLM \\texttt{enforce\\_eager} artifact), the precision effect drops to 0.0006\\% of total variance, with precision$\\times$item at 0.04\\%.\nBF16 and FP16 produce nearly identical results ($\\Delta = 0.23$pp accuracy), confirming that numerical precision between these two formats is a negligible variance source.\n\n\\subsection{Exp-001b: Item Resampling Stability}\n\\label{sec:exp001b}\n\nTo assess sensitivity to item selection, we drew three independent stratified samples of 200 MMLU items (seeds 0, 7, 99) and evaluated Llama under 54 conditions per sample (32,400 total records).\nTable~\\ref{tab:resampling} reports the variance decomposition across samples.\n\n\\begin{table}[t]\n\\centering\n\\caption{Resampling stability across 3 independent 200-item draws (single-model Llama, MMLU).}\n\\label{tab:resampling}\n\\begin{tabular}{lcccccc}\n\\toprule\nSource & Seed 0 & Seed 7 & Seed 99 & Mean & SD & CV \\\\\n\\midrule\nItem ($i$)         & 61.1 & 52.8 & 70.4 & 61.4 & 8.8 & 0.143 \\\\\nResidual           & 17.2 & 23.1 & 12.8 & 17.7 & 5.2 & 0.291 \\\\\nPrec.$\\times$Item  & 7.2  & 8.7  & 5.6  & 7.2  & 1.6 & 0.217 \\\\\nPrompt$\\times$Item & 4.6  & 5.8  & 3.9  & 4.8  & 1.0 & 0.201 \\\\\nSeed$\\times$Item   & 4.7  & 5.2  & 4.2  & 4.7  & 0.5 & 0.106 \\\\\nTemp.$\\times$Item  & 3.1  & 3.3  & 2.7  & 3.0  & 0.3 & 0.100 \\\\\nTemperature        & 1.2  & 1.0  & 0.9  & 1.0  & 0.2 & 0.153 \\\\\nPrecision          & 0.5  & 0.6  & 0.3  & 0.5  & 0.2 & 0.333 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe coefficient of variation (CV) for item dominance is 0.143, indicating moderate sensitivity to item selection.\nThe range (52.8--70.4\\%) is consistent with the bootstrap confidence interval [36.0, 48.8\\%] from the cross-model analysis, suggesting that bootstrap CIs already capture item sampling variability.\nImportantly, item selection remains the largest variance source across all three samples, and the variance component ranking is preserved.\n\n\\begin{table}[t]\n\\centering\n\\caption{G-coefficient stability across item draws (single-model Llama, MMLU).}\n\\label{tab:g_stability}\n\\begin{tabular}{lcccccc}\n\\toprule\nMetric & Seed 0 & Seed 7 & Seed 99 & Mean & SD & CV \\\\\n\\midrule\nBinary       & 0.611 & 0.536 & 0.689 & 0.612 & 0.077 & 0.126 \\\\\nText exact   & 0.007 & 0.005 & 0.009 & 0.007 & 0.002 & 0.286 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:g_stability} shows that the $G$-coefficient for binary scoring has lower variability (CV = 0.126) than raw variance percentages (CV = 0.143), indicating that reliability estimates are more stable than individual variance components.\nThe text-exact-match $G$ remains near zero across all samples, confirming that this metric is unreliable regardless of item selection.\nThe resampling instability reinforces the rationale for treating items as a facet in G-theory: if item selection were irrelevant, G-theory's item-as-facet treatment would be unnecessary.\nD-study budgets recommending 500+ items directly address this instability.\n\n\\subsection{Exp-002: Cross-Benchmark Variance Structure}\n\\label{sec:exp002}\n\nWe replicated the cross-model G-study on three additional benchmarks (GSM8K, ARC-Challenge, HellaSwag) using a reduced design ($4 \\times 2 \\times 6 \\times 6 \\times 2 \\times 4 \\times 200$; 460,800 records per benchmark, 1,382,400 total).\nTable~\\ref{tab:cross_bench} presents the cross-benchmark comparison.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model variance decomposition by benchmark (4 models, BF16). Range = max $-$ min across benchmarks.}\n\\label{tab:cross_bench}\n\\begin{tabular}{lccccc}\n\\toprule\nSource & MMLU & GSM8K & ARC & HSwag & Range \\\\\n\\midrule\nItem ($i$)              & 42.1 & 38.4 & 44.1 & 41.8 & 5.7 \\\\\nModel$\\times$Item       & 33.6 & 31.8 & 30.5 & 35.2 & 4.7 \\\\\nResidual                & 19.5 & 22.6 & 18.8 & 17.4 & 5.2 \\\\\nPrompt$\\times$Item      & 4.6  & 8.4  & 5.2  & 3.8  & 4.6 \\\\\nSeed$\\times$Item        & 4.7  & 5.8  & 4.6  & 4.2  & 1.6 \\\\\nTemperature             & 1.2  & 3.2  & 1.4  & 0.8  & 2.4 \\\\\nModel                   & 0.8  & 1.2  & 0.9  & 0.6  & 0.6 \\\\\nPrecision               & 0.0006 & 0.3 & 0.1 & 0.2 & 0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe variance structure is approximately invariant across benchmarks.\nItem dominance ranges from 38.4\\% (GSM8K) to 44.1\\% (ARC-Challenge)---a span of only 5.7 percentage points.\nModel$\\times$item interaction ranges from 30.5\\% to 35.2\\% (4.7pp range).\nThe variance component ranking is identical across all four benchmarks: item $>$ model$\\times$item $>$ residual $>$ prompt$\\times$item $\\geq$ seed$\\times$item.\nThe originally hypothesized systematic gradient from knowledge-retrieval to reasoning benchmarks does not materialize ($R^2 = 0.12$ for a linear fit of item dominance against task type).\n\n\\paragraph{Benchmark-specific differences.}\nGSM8K shows elevated prompt$\\times$item interaction (8.4\\% vs.\\ 3.8--5.2\\% on other benchmarks) and higher temperature sensitivity (3.2\\% vs.\\ 0.8--1.4\\%), consistent with mathematical reasoning tasks being more sensitive to prompt wording and sampling stochasticity.\nHellaSwag has the highest model$\\times$item interaction (35.2\\%) and lowest residual (17.4\\%), suggesting more structured model-specific difficulty patterns in commonsense reasoning.\n\n\\paragraph{IRT vs.\\ G-theory comparison.}\nTable~\\ref{tab:irt_gtheory} presents the first direct comparison of IRT and G-theory item requirements across benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{IRT vs.\\ G-theory item requirements by benchmark. $G_{\\text{item}}$ = cross-model generalizability coefficient (4 models, 200 items). Ratio = G-theory items / IRT items for $G \\geq 0.80$.}\n\\label{tab:irt_gtheory}\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & $G_{\\text{item}}$ & IRT Items & G-theory Items & Ratio \\\\\n\\midrule\nMMLU          & 0.820 & 118 & 510 & 4.1$\\times$ \\\\\nARC-Challenge & 0.718 & 178 & 448 & 2.5$\\times$ \\\\\nGSM8K         & 0.682 & 286 & 486 & 1.7$\\times$ \\\\\nHellaSwag     & 0.668 & 312 & 502 & 1.6$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe IRT-to-G-theory ratio ranges from 1.6$\\times$ (HellaSwag) to 4.1$\\times$ (MMLU).\nOn MMLU, IRT's 2-parameter logistic model achieves high efficiency because items span a wide discrimination range across 57 subjects; G-theory's additional budget accounts for prompt$\\times$item (4.6\\%), seed$\\times$item (4.7\\%), and residual (19.5\\%) variance that IRT ignores.\nOn reasoning benchmarks (GSM8K, HellaSwag), IRT itself requires more items (286--312) due to more uniform item discrimination, compressing the ratio.\nThis benchmark-dependence resolves conflicting claims in the literature: IRT-based subsampling \\citep{polo2024tinybenchmarks} is relatively more sufficient on reasoning benchmarks than on knowledge benchmarks.\n\n\\paragraph{D-study cross-benchmark transfer.}\nTable~\\ref{tab:d_study_transfer} evaluates whether MMLU-derived D-study budgets transfer to other benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study cross-benchmark transfer error. MMLU-derived budget (510 items, 2 prompts, 3 seeds) projected $G = 0.80$; actual $G$ varies by benchmark.}\n\\label{tab:d_study_transfer}\n\\begin{tabular}{lccc}\n\\toprule\nBenchmark & MMLU-Derived $G$ & Actual $G$ & $\\Delta$ \\\\\n\\midrule\nMMLU          & 0.800 & 0.800 & 0.000 \\\\\nARC-Challenge & 0.800 & 0.768 & 0.032 \\\\\nGSM8K         & 0.800 & 0.753 & 0.047 \\\\\nHellaSwag     & 0.800 & 0.742 & 0.058 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nMMLU-derived budgets overestimate $G$ on other benchmarks by 3.2--5.8 percentage points, primarily because MMLU has lower residual variance (19.5\\%) than GSM8K (22.6\\%) or HellaSwag (17.4\\% residual but higher model$\\times$item at 35.2\\%).\nPractitioners applying MMLU-derived budgets to other benchmarks should add a 10--15\\% safety margin on item counts.\nDespite this transfer error, the qualitative conclusion is preserved: all four benchmarks require 400--650 items for $G \\geq 0.80$ under practical conditions.\n\n\\paragraph{Cross-benchmark separability.}\nTable~\\ref{tab:separability} reports precision$\\times$methodology interactions across benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Precision$\\times$methodology interaction by benchmark (binary scoring, 4 models).}\n\\label{tab:separability}\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & Prec.$\\times$Prompt & Prec.$\\times$Seed & Prec.$\\times$Temp & Total \\\\\n\\midrule\nMMLU          & 0.02\\% & 0.01\\% & 0.05\\% & 0.08\\% \\\\\nARC-Challenge & 0.9\\%  & 0.5\\%  & 1.0\\%  & 2.4\\%  \\\\\nGSM8K         & 1.2\\%  & 0.8\\%  & 1.6\\%  & 3.6\\%  \\\\\nHellaSwag     & 1.6\\%  & 1.1\\%  & 2.1\\%  & 4.8\\%  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nPrecision$\\times$methodology separability holds on MMLU (total interaction $<$ 0.1\\%) but does not generalize: HellaSwag reaches 4.8\\% total interaction under binary scoring.\nSeparability is therefore benchmark-dependent and should not be assumed as a universal property.\nWe note this as an observation rather than a primary contribution.\n\n\\subsection{Exp-003: Multi-Hardware G-Study (Partial)}\n\\label{sec:exp003}\n\nA second GPU type (RTX A6000 48GB) became available four weeks before deadline, enabling a partial hardware crossing with 2 models (Llama, Mistral) under 576 conditions each (230,400 records total).\nTable~\\ref{tab:hardware} reports hardware$\\times$methodology interactions.\n\n\\begin{table}[t]\n\\centering\n\\caption{Hardware$\\times$methodology interaction breakdown (2 models, binary scoring, RTX PRO 6000 vs.\\ RTX A6000).}\n\\label{tab:hardware}\n\\begin{tabular}{lccc}\n\\toprule\nInteraction & Llama \\% & Mistral \\% & Average \\% \\\\\n\\midrule\nHardware$\\times$Temperature & 1.1 & 1.7 & 1.4 \\\\\nHardware$\\times$Precision   & 0.7 & 1.1 & 0.9 \\\\\nHardware$\\times$Prompt      & 0.5 & 0.7 & 0.6 \\\\\nHardware$\\times$Seed        & 0.2 & 0.4 & 0.3 \\\\\nHardware$\\times$Item        & 2.4 & 3.2 & 2.8 \\\\\nHardware main effect        & 1.3 & 2.3 & 1.8 \\\\\n\\midrule\nTotal hardware$\\times$methodology & 3.8 & 4.6 & 4.2 \\\\\nTotal hardware-related      & 6.2 & 9.4 & 7.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nHardware$\\times$methodology interaction averages 4.2\\% across the two models---substantially larger than the within-single-GPU precision$\\times$methodology interaction of 0.08\\%.\nThe largest sub-interaction is hardware$\\times$temperature (1.4\\%), attributable to different CUDA RNG implementations across GPU architectures (Ada Lovelace sm\\_89 vs.\\ Ampere sm\\_86) producing different pseudo-random sequences even under identical seeds.\nHardware$\\times$item (2.8\\%) reflects a small number of items ($\\sim$5--8) near the decision boundary where kernel-level numerical differences flip predictions.\n\nMistral shows higher hardware interaction (4.6\\%) than Llama (3.8\\%), consistent with Mistral's lower accuracy (61.2\\% vs.\\ 68.1\\%) placing more items near the decision boundary.\nThe single-GPU $G_{\\text{binary}}$ of 0.611 degrades to 0.582 when hardware is added as a facet ($\\Delta G = 0.029$).\n\nThese results are preliminary (2 of 4 models) but sufficient to conclude that the precision separability observed within a single GPU environment does not extend across GPU architectures.\nAll separability-related conclusions in this paper are accordingly qualified to single-GPU, single-architecture settings.\n\n\\subsection{Exp-004: Comprehensive Analysis}\n\\label{sec:exp004}\n\nDrawing on all collected data, we conducted 13 of 17 planned analyses (4 blocked by incomplete hardware crossing).\nKey results are summarized below.\n\n\\paragraph{D-study budget recommendations.}\nTable~\\ref{tab:d_study_budgets} presents benchmark-specific evaluation budgets for achieving $G \\geq 0.80$.\n\n\\begin{table}[t]\n\\centering\n\\caption{D-study budget recommendations by benchmark ($G \\geq 0.80$, practical design with temperature and ordering fixed).}\n\\label{tab:d_study_budgets}\n\\begin{tabular}{lcccc}\n\\toprule\nBenchmark & Items & Prompts & Seeds & Projected $G$ [95\\% CI] \\\\\n\\midrule\nMMLU          & 510 & 2 & 3 & 0.800 [0.782, 0.825] \\\\\nARC-Challenge & 538 & 2 & 3 & 0.800 [0.778, 0.826] \\\\\nGSM8K         & 624 & 3 & 4 & 0.801 [0.774, 0.831] \\\\\nHellaSwag     & 652 & 3 & 4 & 0.802 [0.771, 0.838] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll benchmarks require 500--650 items with multiple prompts and seeds.\nCurrent standard practice (1 prompt, 1 seed, $\\leq$200 items) yields $G = 0.611$ on MMLU---below the 0.80 threshold for dependable measurement.\nUsing the full 14,042 MMLU items projects to $G = 0.972$, indicating that the complete benchmark is highly reliable but that common subsampling practices are not.\n\n\\paragraph{Methodological robustness.}\nTable~\\ref{tab:robustness} summarizes the robustness verification package.\n\n\\begin{table}[t]\n\\centering\n\\caption{Methodological robustness summary.}\n\\label{tab:robustness}\n\\begin{tabular}{lll}\n\\toprule\nAnalysis & Result & Status \\\\\n\\midrule\nBinary not artifact (null sim) & item$_{\\text{id}}$ = 0.08\\% vs.\\ obs.\\ 61.1\\% (737$\\times$) & PASS \\\\\nFixed vs.\\ random sensitivity  & max $\\Delta(G)$ = 0.053 & PASS \\\\\nBootstrap = Jackknife CIs      & ratio range [0.96, 1.04] & PASS \\\\\nREML vs.\\ Henderson I          & max diff $<$ 0.4pp & PASS \\\\\nTemp.\\ stratification           & binary $G$: 0.760 $\\to$ 0.549 ($T$=0 $\\to$ 0.7) & PASS \\\\\nBernoulli variance correlation & $r = 0.91$ & NOTED \\\\\nD-study cross-bench transfer   & $\\Delta$ = 0.032--0.058 & CAVEAT \\\\\nLOMO matched spread            & spread = 0.058 & CAVEAT \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\\label{sec:robustness}\n\nSix of eight analyses pass cleanly.\nThe null simulation confirms that observed item variance is not a Bernoulli artifact: simulated item$_{\\text{id}}$ under independence is 0.08\\% versus observed 61.1\\%.\nFixed vs.\\ random facet classification produces $G$ values ranging from 0.611 (all random) to 0.664 (temperature and ordering fixed), a maximum shift of 0.053---qualitative conclusions are robust.\nBootstrap and delete-1 jackknife confidence intervals agree (ratio 0.96--1.04), indicating that item-level resampling violations are negligible.\nREML-EM (500 iterations, practical convergence $\\Delta < 0.003$pp) confirms Henderson's Method~I within 0.4pp on all components.\n\nTwo caveated results require transparent reporting.\nThe D-study cross-benchmark transfer error ($\\Delta = 0.032$--$0.058$) means MMLU-derived budgets are approximately but not exactly portable.\nThe LOMO matched-specification spread (0.058) indicates that 4-model estimates have approximately 3\\% standard deviation; stable estimates require $\\sim$10 models.\n\n\\paragraph{Logprob analysis.}\nLogprob-based scoring produces tighter cross-benchmark variance structure (item dominance range = 3.5pp vs.\\ 5.7pp for binary scoring), suggesting that continuous scoring reduces benchmark-dependence.\nItem dominance under logprob scoring: MMLU 48.3\\%, GSM8K 44.8\\%, ARC 46.1\\%, HellaSwag 45.9\\%.\n\n\\paragraph{Computational cost.}\nAchieving $G \\geq 0.80$ requires approximately 340 GPU-hours on MMLU, 415 on GSM8K, and 430 on HellaSwag (using a single RTX PRO 6000).\n$G \\geq 0.90$ on MMLU requires $\\sim$890 GPU-hours.\n\n% ============================================================\n% 5. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{The model$\\times$item interaction as a hidden factor.}\nThe central finding of this work is that model$\\times$item interaction accounts for 33.6\\% of cross-model evaluation variance on MMLU---nearly as large as item selection itself (42.1\\%).\nThis means that item difficulty rankings are substantially model-specific: an item that is easy for Llama may be difficult for Mistral, and vice versa.\nSingle-model G-studies (or ANOVA decompositions) inflate item dominance by up to 19 percentage points by absorbing this interaction into the item component.\nThis has direct implications for benchmark design: item selection strategies based on single-model difficulty estimates (e.g., selecting ``hard'' items based on one model's performance) will not generalize across models.\n\n\\paragraph{Practical implications of benchmark-invariance.}\nThe approximate invariance of variance structure across four benchmarks (item dominance range = 5.7pp) is a practically useful finding.\nIt means that practitioners who have conducted a thorough G-study on one benchmark can cautiously apply the resulting evaluation budgets to related benchmarks, with a 10--15\\% safety margin on item counts to account for the 3--6pp $G$-coefficient transfer error.\nThis is substantially more efficient than conducting a full G-study on every benchmark of interest.\n\n\\paragraph{When is IRT sufficient?}\nThe benchmark-dependent IRT-to-G-theory ratio (1.6--4.1$\\times$) provides a principled answer to when IRT-based subsampling is ``good enough.''\nOn reasoning benchmarks where item discrimination is relatively uniform (HellaSwag, GSM8K), IRT approaches G-theory's item requirements (ratio $<$ 2$\\times$), and the additional cost of a full G-study may not be justified.\nOn knowledge benchmarks with heterogeneous discrimination (MMLU), the 4.1$\\times$ gap indicates that IRT substantially underestimates the items needed for reliable multi-facet measurement.\n\n\\paragraph{Hardware separability is limited.}\nThe partial two-GPU study reveals that hardware$\\times$methodology interaction (4.2\\%) exceeds within-GPU precision$\\times$methodology interaction (0.08\\%) by approximately 50$\\times$.\nWhile this interaction is small relative to item (42.1\\%) and model$\\times$item (33.6\\%), it is large enough to shift $G$ by 0.029 points.\nEvaluation studies claiming reproducibility across hardware configurations should empirically verify this assumption rather than extrapolating from single-GPU precision studies.\n\n\\paragraph{Extending to fine-tuning.}\nG-theory naturally extends to fine-tuning variance, where training seed, learning rate, and data ordering are additional facets.\n\\citet{dodge2020finetuning} and \\citet{bui2025seed} provide preliminary evidence that seed and learning rate dominate fine-tuning variance; a full G-theory treatment of fine-tuning is a natural next step.\n\n\\subsection{Limitations}\n\n\\textbf{Model sample size.}\nAll results are based on 4 models in the 7--9B parameter range.\nThe LOMO spread of 0.058 indicates that point estimates have approximately 3\\% standard deviation; D-study projections suggest 10+ models are needed for stable estimates.\nScale validation (14B+ models) and closed-source API models remain for future work.\n\n\\textbf{Item sample size.}\nThe resampling CV of 0.143 shows that 200-item subsamples produce moderately variable variance estimates.\nAll reported confidence intervals account for this variability via bootstrap resampling.\n\n\\textbf{Binary data.}\nWhile null simulations and REML robustness checks support the validity of G-theory on binary data, the Bernoulli variance correlation ($r = 0.91$) indicates that a portion of item variance is mechanically linked to item difficulty.\nGeneralized G-theory with logistic link functions \\citep{jiang2017generalized} would provide a more principled treatment.\n\n\\textbf{Hardware crossing.}\nThe multi-GPU analysis covers only 2 of 4 models on 2 GPU architectures.\nFull hardware crossing is needed to quantify the hardware facet at the same precision as other facets.\n\n\\textbf{Judge exclusion.}\nBy fixing evaluation to exact-match scoring, we exclude judge variance---the largest source in \\citet{mesting2026generalizability}'s analysis.\nOur results are therefore specific to closed-form evaluation metrics.\n\n% ============================================================\n% 6. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe presented a multi-benchmark Generalizability Theory analysis of LLM evaluation variance across 4 models, 4 benchmarks, and over 2.3 million evaluation records.\nThree findings emerge.\nFirst, model$\\times$item interaction accounts for 33.6\\% of cross-model variance on MMLU---nearly as large as item selection (42.1\\%)---revealing that item difficulty rankings are substantially model-specific.\nA D-study predicted the 4-model generalizability coefficient within $\\Delta = 0.004$, validating G-theory's projective machinery for LLM evaluation.\nSecond, G-theory requires 1.6--4.1$\\times$ more items than IRT for reliable measurement, with the ratio being benchmark-dependent.\nThird, variance structure is approximately benchmark-invariant (item dominance range = 5.7pp across four benchmarks), enabling cautious cross-benchmark extrapolation of evaluation budgets with a 3--6pp safety margin.\nCurrent evaluation practices (1 prompt, 1 seed, $\\leq$200 items) yield $G = 0.611$ on MMLU, well below the 0.80 reliability threshold.\nWe release an open-source G-theory pipeline and D-study calculator to support more rigorous evaluation design.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Biderman et~al.(2024)]{biderman2024lessons}\nS.~Biderman, et~al.\n\\newblock Lessons from the trenches on reproducible evaluation of language models.\n\\newblock \\emph{arXiv preprint arXiv:2405.14782}, 2024.\n\n\\bibitem[Bouthillier et~al.(2021)]{bouthillier2021accounting}\nX.~Bouthillier, et~al.\n\\newblock Accounting for variance in machine learning benchmarks.\n\\newblock \\emph{Proceedings of Machine Learning and Systems}, 3:747--769, 2021.\n\n\\bibitem[Brennan(2001)]{brennan2001generalizability}\nR.~L. Brennan.\n\\newblock \\emph{Generalizability Theory}.\n\\newblock Springer-Verlag, 2001.\n\n\\bibitem[BrittleBench(2026)]{brittlebench2026}\nBrittleBench Team.\n\\newblock BrittleBench: Quantifying prompt sensitivity in LLM evaluation.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Bui et~al.(2025)]{bui2025seed}\nT.~Bui, et~al.\n\\newblock Extreme seed sensitivity in fine-tuning: RTES variance analysis.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\bibitem[Dehghani et~al.(2021)]{dehghani2021benchmark}\nM.~Dehghani, et~al.\n\\newblock The benchmark lottery.\n\\newblock \\emph{arXiv preprint arXiv:2107.07002}, 2021.\n\n\\bibitem[Dodge et~al.(2020)]{dodge2020finetuning}\nJ.~Dodge, et~al.\n\\newblock Fine-tuning pretrained language models: Weight initializations, data orders, and early stopping.\n\\newblock \\emph{arXiv preprint arXiv:2002.06305}, 2020.\n\n\\bibitem[Henderson et~al.(2018)]{henderson2018deep}\nP.~Henderson, et~al.\n\\newblock Deep reinforcement learning that matters.\n\\newblock In \\emph{AAAI}, 2018.\n\n\\bibitem[Hua et~al.(2025)]{hua2025emnlp}\nH.~Hua, et~al.\n\\newblock Generation-based evaluation for LLMs.\n\\newblock In \\emph{EMNLP}, 2025.\n\n\\bibitem[Jiang \\& Skorupski(2017)]{jiang2017generalized}\nZ.~Jiang and W.~P. Skorupski.\n\\newblock A generalized G-theory model for binary data.\n\\newblock \\emph{Applied Psychological Measurement}, 41(6):443--458, 2017.\n\n\\bibitem[Kunievsky \\& Evans(2025)]{kunievsky2025alternative}\nD.~Kunievsky and O.~Evans.\n\\newblock Decomposing evaluation variance: Intent, articulation, and model uncertainty.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\bibitem[Lalor et~al.(2019)]{lalor2019learning}\nJ.~P. Lalor, et~al.\n\\newblock Learning latent parameters without human response patterns: Item response theory with artificial crowds.\n\\newblock In \\emph{EMNLP-IJCNLP}, 2019.\n\n\\bibitem[Lu et~al.(2022)]{lu2022fantastically}\nY.~Lu, et~al.\n\\newblock Fantastically ordered prompts and where to find them: Overcoming few-shot prompt order sensitivity.\n\\newblock In \\emph{ACL}, 2022.\n\n\\bibitem[Messina \\& Scotta(2026)]{messina2026floating}\nE.~Messina and R.~Scotta.\n\\newblock Floating-point non-associativity in neural network inference.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Mesting(2026)]{mesting2026generalizability}\nF.~Mesting.\n\\newblock Generalizability theory for LLM evaluation: A five-facet analysis.\n\\newblock \\emph{arXiv preprint}, 2026.\n\n\\bibitem[Mushquash \\& O'Connor(2006)]{mushquash2006generalizability}\nC.~Mushquash and B.~P. O'Connor.\n\\newblock SPSS and SAS programs for generalizability theory analyses.\n\\newblock \\emph{Behavior Research Methods}, 38(3):542--547, 2006.\n\n\\bibitem[Perlitz et~al.(2023)]{perlitz2023efficient}\nY.~Perlitz, et~al.\n\\newblock Efficient benchmarking (of language models).\n\\newblock \\emph{arXiv preprint arXiv:2308.11696}, 2023.\n\n\\bibitem[Pezeshkpour \\& Hruschka(2024)]{pezeshkpour2024large}\nP.~Pezeshkpour and E.~Hruschka.\n\\newblock Large language models sensitivity to the order of options in multiple-choice questions.\n\\newblock In \\emph{NAACL Findings}, 2024.\n\n\\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}\nF.~M. Polo, et~al.\n\\newblock tinyBenchmarks: Evaluating LLMs with fewer examples.\n\\newblock \\emph{arXiv preprint arXiv:2402.14992}, 2024.\n\n\\bibitem[Rodriguez et~al.(2021)]{rodriguez2021evaluation}\nP.~Rodriguez, et~al.\n\\newblock Evaluation examples are not equally informative: How should that change NLP leaderboards?\n\\newblock In \\emph{ACL}, 2021.\n\n\\bibitem[Sclar et~al.(2024)]{sclar2024quantifying}\nM.~Sclar, et~al.\n\\newblock Quantifying language models' sensitivity to spurious features in prompt design.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Sellam et~al.(2022)]{sellam2022multberts}\nT.~Sellam, et~al.\n\\newblock The MultiBERTs: BERT reproductions for robustness analysis.\n\\newblock In \\emph{ICLR}, 2022.\n\n\\bibitem[Shavelson \\& Webb(1991)]{shavelson1991generalizability}\nR.~J. Shavelson and N.~M. Webb.\n\\newblock \\emph{Generalizability Theory: A Primer}.\n\\newblock Sage, 1991.\n\n\\bibitem[Shavelson et~al.(1989)]{shavelson1989generalizability}\nR.~J. Shavelson, et~al.\n\\newblock Generalizability of binary items.\n\\newblock \\emph{Journal of Educational Measurement}, 26(3):231--244, 1989.\n\n\\bibitem[Vania et~al.(2021)]{vania2021comparing}\nC.~Vania, et~al.\n\\newblock Comparing test sets with item response theory.\n\\newblock In \\emph{ACL}, 2021.\n\n\\bibitem[Yuan et~al.(2025)]{yuan2025precision}\nZ.~Yuan, et~al.\n\\newblock Precision matters: Up to 9\\% accuracy variation from numerical precision in LLM inference.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "f856b981-1072-49a5-b674-4d2ab142a248",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T075006 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheor…",
  "leafUuid": "b954157f-051c-4df6-98b6-4c819aade514",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate LLM evaluation variance analysis paper",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3"
}
```

---

### Assistant

_source line 25 · 2026-05-21T08:33:01.227Z_

Now compiling the LaTeX.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b954157f-051c-4df6-98b6-4c819aade514",
  "isSidechain": false,
  "requestId": "req_011CbFQR6pssYRJSrmKwvH8J",
  "type": "assistant",
  "uuid": "9544008e-7cf7-44fd-bf7a-737776c4168b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMQTJFfyU9LqELzbC8Pj6k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14698,
      "cache_read_input_tokens": 48182,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 48182,
          "cache_creation_input_tokens": 14698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14698
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

_source line 26 · 2026-05-21T08:33:02.376Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Suss119T8sNbDXpoEyoe2h`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9544008e-7cf7-44fd-bf7a-737776c4168b",
  "isSidechain": false,
  "requestId": "req_011CbFQR6pssYRJSrmKwvH8J",
  "type": "assistant",
  "uuid": "8685fac4-a613-4c83-9342-f1378e0e18e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMQTJFfyU9LqELzbC8Pj6k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14698,
      "cache_read_input_tokens": 48182,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14698,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 48182,
          "cache_creation_input_tokens": 14698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14698
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

_source line 27 · 2026-05-21T08:33:03.312Z_

<details><summary>↩ Tool result · `toolu_01Suss119T8sNbDXpoEyoe2h`</summary>

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `sclar2024quantifying' on page 1 undefined on 
input line 41.


Package natbib Warning: Citation `bui2025seed' on page 1 undefined on input lin
e 41.


Package natbib Warning: Citation `yuan2025precision' on page 1 undefined on inp
ut line 41.


Package natbib Warning: Citation `shavelson1991generalizability' on page 1 unde
fined on input line 45.


Package natbib Warning: Citation `brennan2001generalizability' on page 1 undefi
ned on input line 45.


Package natbib Warning: Citation `mesting2026generalizability' on page 1 undefi
ned on input line 47.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

Package natbib Warning: Citation `bouthillier2021accounting' on page 2 undefine
d on input line 70.


Package natbib Warning: Citation `henderson2018deep' on page 2 undefined on inp
ut line 71.


Package natbib Warning: Citation `dodge2020finetuning' on page 2 undefined on i
nput line 72.


Package natbib Warning: Citation `sellam2022multberts' on page 2 undefined on i
nput line 72.


Package natbib Warning: Citation `bui2025seed' on page 2 undefined on input lin
e 73.


Package natbib Warning: Citation `sclar2024quantifying' on page 2 undefined on 
input line 76.


Package natbib Warning: Citation `lu2022fantastically' on page 2 undefined on i
nput line 77.


Package natbib Warning: Citation `pezeshkpour2024large' on page 2 undefined on 
input line 77.


Package natbib Warning: Citation `brittlebench2026' on page 2 undefined on inpu
t line 78.


Package natbib Warning: Citation `yuan2025precision' on page 2 undefined on inp
ut line 81.


Package natbib Warning: Citation `messina2026floating' on page 2 undefined on i
nput line 82.


Package natbib Warning: Citation `mesting2026generalizability' on page 2 undefi
ned on input line 85.


Package natbib Warning: Citation `shavelson1991generalizability' on page 2 unde
fined on input line 87.


Package natbib Warning: Citation `brennan2001generalizability' on page 2 undefi
ned on input line 87.


Package natbib Warning: Citation `jiang2017generalized' on page 2 undefined on 
input line 87.


Package natbib Warning: Citation `mushquash2006generalizability' on page 2 unde
fined on input line 87.


Package natbib Warning: Citation `lalor2019learning' on page 2 undefined on inp
ut line 90.


Package natbib Warning: Citation `rodriguez2021evaluation' on page 2 undefined 
on input line 91.


Package natbib Warning: Citation `vania2021comparing' on page 2 undefined on in
put line 91.


Package natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o
n input line 92.


Package natbib Warning: Citation `perlitz2023efficient' on page 2 undefined on 
input line 93.


Package natbib Warning: Citation `kunievsky2025alternative' on page 2 undefined
 on input line 97.


Package natbib Warning: Citation `dehghani2021benchmark' on page 2 undefined on
 input line 98.


Package natbib Warning: Citation `biderman2024lessons' on page 2 undefined on i
nput line 99.


Package natbib Warning: Citation `shavelson1991generalizability' on page 2 unde
fined on input line 108.


Package natbib Warning: Citation `brennan2001generalizability' on page 2 undefi
ned on input line 108.

[2]

LaTeX Warning: Reference `sec:robustness' on page 3 undefined on input line 132
.


Package natbib Warning: Citation `shavelson1989generalizability' on page 3 unde
fined on input line 133.


Package natbib Warning: Citation `mushquash2006generalizability' on page 3 unde
fined on input line 133.


Package natbib Warning: Citation `jiang2017generalized' on page 3 undefined on 
input line 133.


Overfull \hbox (4.70984pt too wide) in paragraph at lines 142--143
 []\OT1/cmr/bx/n/10 Benchmarks.[] \OT1/cmr/m/n/10 MMLU (pri-mary, 200 strat-i-f
ied items from 57 sub-jects), GSM8K (200 items), ARC-Challenge

Overfull \hbox (3.9651pt too wide) in paragraph at lines 146--147
[]\OT1/cmr/bx/n/10 Precision\OT1/cmr/m/n/10 : BF16, FP16 (FP32 ex-cluded af-ter
 iden-ti-fy-ing vLLM \OT1/cmtt/m/n/10 enforce[]eager \OT1/cmr/m/n/10 con-found;
 BF16$\OMS/cmsy/m/n/10 ^^Y$\OT1/cmr/m/n/10 FP16,

Package natbib Warning: Citation `mesting2026generalizability' on page 3 undefi
ned on input line 161.


LaTeX Warning: Reference `tab:cross_model_decomp' on page 3 undefined on input 
line 172.

[3]

LaTeX Warning: Reference `tab:per_model_decomp' on page 4 undefined on input li
ne 204.


LaTeX Warning: Reference `tab:lomo' on page 4 undefined on input line 232.

[4]

LaTeX Warning: Reference `tab:resampling' on page 5 undefined on input line 266
.


LaTeX Warning: Reference `tab:g_stability' on page 5 undefined on input line 30
6.


LaTeX Warning: Reference `tab:cross_bench' on page 5 undefined on input line 31
5.

[5]

LaTeX Warning: Reference `tab:irt_gtheory' on page 6 undefined on input line 34
8.


Package natbib Warning: Citation `polo2024tinybenchmarks' on page 6 undefined o
n input line 369.


LaTeX Warning: Reference `tab:d_study_transfer' on page 6 undefined on input li
ne 372.

[6]

LaTeX Warning: Reference `tab:separability' on page 7 undefined on input line 3
95.


LaTeX Warning: Reference `tab:hardware' on page 7 undefined on input line 421.


Overfull \hbox (39.47171pt too wide) in paragraph at lines 444--447
\OT1/cmr/m/n/10 within-single-GPU precision$\OMS/cmsy/m/n/10 ^^B$\OT1/cmr/m/n/1
0 methodology in-ter-ac-tion of 0.08%. The largest sub-interaction is hardware$
\OMS/cmsy/m/n/10 ^^B$\OT1/cmr/m/n/10 temperature

LaTeX Warning: Reference `tab:d_study_budgets' on page 7 undefined on input lin
e 461.


Overfull \hbox (1.78891pt too wide) in paragraph at lines 461--462
 []\OT1/cmr/bx/n/10 D-study bud-get rec-om-men-da-tions.[] \OT1/cmr/m/n/10 Ta-b
le [] presents benchmark-specific eval-u-a-tion bud-gets for achiev-
[7]

LaTeX Warning: Reference `tab:robustness' on page 8 undefined on input line 484
.


Overfull \hbox (1.607pt too wide) in paragraph at lines 518--520
\OT1/cmr/m/n/10 dom-i-nance range = 3.5pp vs. 5.7pp for bi-nary scor-ing), sug-
gest-ing that con-tin-u-ous scor-ing re-duces benchmark-
[8]

Package natbib Warning: Citation `dodge2020finetuning' on page 9 undefined on i
nput line 553.


Package natbib Warning: Citation `bui2025seed' on page 9 undefined on input lin
e 553.

[9]

Package natbib Warning: Citation `jiang2017generalized' on page 10 undefined on
 input line 568.


Package natbib Warning: Citation `mesting2026generalizability' on page 10 undef
ined on input line 575.

[10]

Package natbib Warning: There were undefined citations.

[11] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.
pfb>
Output written on paper.pdf (11 pages, 280596 bytes).
Transcript written on paper.log.
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] [2]
Overfull \hbox (4.70984pt too wide) in paragraph at lines 142--143
 []\OT1/cmr/bx/n/10 Benchmarks.[] \OT1/cmr/m/n/10 MMLU (pri-mary, 200 strat-i-f
ied items from 57 sub-jects), GSM8K (200 items), ARC-Challenge

Overfull \hbox (3.9651pt too wide) in paragraph at lines 146--147
[]\OT1/cmr/bx/n/10 Precision\OT1/cmr/m/n/10 : BF16, FP16 (FP32 ex-cluded af-ter
 iden-ti-fy-ing vLLM \OT1/cmtt/m/n/10 enforce[]eager \OT1/cmr/m/n/10 con-found;
 BF16$\OMS/cmsy/m/n/10 ^^Y$\OT1/cmr/m/n/10 FP16,
[3] [4] [5] [6]
Overfull \hbox (39.47171pt too wide) in paragraph at lines 444--447
\OT1/cmr/m/n/10 within-single-GPU precision$\OMS/cmsy/m/n/10 ^^B$\OT1/cmr/m/n/1
0 methodology in-ter-ac-tion of 0.08%. The largest sub-interaction is hardware$
\OMS/cmsy/m/n/10 ^^B$\OT1/cmr/m/n/10 temperature
[7]
Overfull \hbox (0.92789pt too wide) in paragraph at lines 461--462
 []\OT1/cmr/bx/n/10 D-study bud-get rec-om-men-da-tions.[] \OT1/cmr/m/n/10 Ta-b
le []11[] presents benchmark-specific eval-u-a-tion bud-gets for achiev-

Overfull \hbox (1.607pt too wide) in paragraph at lines 518--520
\OT1/cmr/m/n/10 dom-i-nance range = 3.5pp vs. 5.7pp for bi-nary scor-ing), sug-
gest-ing that con-tin-u-ous scor-ing re-duces benchmark-
[8] [9] [10] [11] (./paper.aux)

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.

 )
(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025
/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/
type1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p
ublic/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/
amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive
/texmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.
pfb>
Output written on paper.pdf (11 pages, 286125 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8685fac4-a613-4c83-9342-f1378e0e18e8",
  "isSidechain": false,
  "promptId": "9d021380-77fd-4766-a060-794a49f7c1c1",
  "type": "user",
  "uuid": "038d1237-1034-4d9f-b6c4-3e896a1676e5",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `sclar2024quantifying' on page 1 undefined on \ninput line 41.\n\n\nPackage natbib Warning: Citation `bui2025seed' on page 1 undefined on input lin\ne 41.\n\n\nPackage natbib Warning: Citation `yuan2025precision' on page 1 undefined on inp\nut line 41.\n\n\nPackage natbib Warning: Citation `shavelson1991generalizability' on page 1 unde\nfined on input line 45.\n\n\nPackage natbib Warning: Citation `brennan2001generalizability' on page 1 undefi\nned on input line 45.\n\n\nPackage natbib Warning: Citation `mesting2026generalizability' on page 1 undefi\nned on input line 47.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `bouthillier2021accounting' on page 2 undefine\nd on input line 70.\n\n\nPackage natbib Warning: Citation `henderson2018deep' on page 2 undefined on inp\nut line 71.\n\n\nPackage natbib Warning: Citation `dodge2020finetuning' on page 2 undefined on i\nnput line 72.\n\n\nPackage natbib Warning: Citation `sellam2022multberts' on page 2 undefined on i\nnput line 72.\n\n\nPackage natbib Warning: Citation `bui2025seed' on page 2 undefined on input lin\ne 73.\n\n\nPackage natbib Warning: Citation `sclar2024quantifying' on page 2 undefined on \ninput line 76.\n\n\nPackage natbib Warning: Citation `lu2022fantastically' on page 2 undefined on i\nnput line 77.\n\n\nPackage natbib Warning: Citation `pezeshkpour2024large' on page 2 undefined on \ninput line 77.\n\n\nPackage natbib Warning: Citation `brittlebench2026' on page 2 undefined on inpu\nt line 78.\n\n\nPackage natbib Warning: Citation `yuan2025precision' on page 2 undefined on inp\nut line 81.\n\n\nPackage natbib Warning: Citation `messina2026floating' on page 2 undefined on i\nnput line 82.\n\n\nPackage natbib Warning: Citation `mesting2026generalizability' on page 2 undefi\nned on input line 85.\n\n\nPackage natbib Warning: Citation `shavelson1991generalizability' on page 2 unde\nfined on input line 87.\n\n\nPackage natbib Warning: Citation `brennan2001generalizability' on page 2 undefi\nned on input line 87.\n\n\nPackage natbib Warning: Citation `jiang2017generalized' on page 2 undefined on \ninput line 87.\n\n\nPackage natbib Warning: Citation `mushquash2006generalizability' on page 2 unde\nfined on input line 87.\n\n\nPackage natbib Warning: Citation `lalor2019learning' on page 2 undefined on inp\nut line 90.\n\n\nPackage natbib Warning: Citation `rodriguez2021evaluation' on page 2 undefined \non input line 91.\n\n\nPackage natbib Warning: Citation `vania2021comparing' on page 2 undefined on in\nput line 91.\n\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 2 undefined o\nn input line 92.\n\n\nPackage natbib Warning: Citation `perlitz2023efficient' on page 2 undefined on \ninput line 93.\n\n\nPackage natbib Warning: Citation `kunievsky2025alternative' on page 2 undefined\n on input line 97.\n\n\nPackage natbib Warning: Citation `dehghani2021benchmark' on page 2 undefined on\n input line 98.\n\n\nPackage natbib Warning: Citation `biderman2024lessons' on page 2 undefined on i\nnput line 99.\n\n\nPackage natbib Warning: Citation `shavelson1991generalizability' on page 2 unde\nfined on input line 108.\n\n\nPackage natbib Warning: Citation `brennan2001generalizability' on page 2 undefi\nned on input line 108.\n\n[2]\n\nLaTeX Warning: Reference `sec:robustness' on page 3 undefined on input line 132\n.\n\n\nPackage natbib Warning: Citation `shavelson1989generalizability' on page 3 unde\nfined on input line 133.\n\n\nPackage natbib Warning: Citation `mushquash2006generalizability' on page 3 unde\nfined on input line 133.\n\n\nPackage natbib Warning: Citation `jiang2017generalized' on page 3 undefined on \ninput line 133.\n\n\nOverfull \\hbox (4.70984pt too wide) in paragraph at lines 142--143\n []\\OT1/cmr/bx/n/10 Benchmarks.[] \\OT1/cmr/m/n/10 MMLU (pri-mary, 200 strat-i-f\nied items from 57 sub-jects), GSM8K (200 items), ARC-Challenge\n\nOverfull \\hbox (3.9651pt too wide) in paragraph at lines 146--147\n[]\\OT1/cmr/bx/n/10 Precision\\OT1/cmr/m/n/10 : BF16, FP16 (FP32 ex-cluded af-ter\n iden-ti-fy-ing vLLM \\OT1/cmtt/m/n/10 enforce[]eager \\OT1/cmr/m/n/10 con-found;\n BF16$\\OMS/cmsy/m/n/10 ^^Y$\\OT1/cmr/m/n/10 FP16,\n\nPackage natbib Warning: Citation `mesting2026generalizability' on page 3 undefi\nned on input line 161.\n\n\nLaTeX Warning: Reference `tab:cross_model_decomp' on page 3 undefined on input \nline 172.\n\n[3]\n\nLaTeX Warning: Reference `tab:per_model_decomp' on page 4 undefined on input li\nne 204.\n\n\nLaTeX Warning: Reference `tab:lomo' on page 4 undefined on input line 232.\n\n[4]\n\nLaTeX Warning: Reference `tab:resampling' on page 5 undefined on input line 266\n.\n\n\nLaTeX Warning: Reference `tab:g_stability' on page 5 undefined on input line 30\n6.\n\n\nLaTeX Warning: Reference `tab:cross_bench' on page 5 undefined on input line 31\n5.\n\n[5]\n\nLaTeX Warning: Reference `tab:irt_gtheory' on page 6 undefined on input line 34\n8.\n\n\nPackage natbib Warning: Citation `polo2024tinybenchmarks' on page 6 undefined o\nn input line 369.\n\n\nLaTeX Warning: Reference `tab:d_study_transfer' on page 6 undefined on input li\nne 372.\n\n[6]\n\nLaTeX Warning: Reference `tab:separability' on page 7 undefined on input line 3\n95.\n\n\nLaTeX Warning: Reference `tab:hardware' on page 7 undefined on input line 421.\n\n\nOverfull \\hbox (39.47171pt too wide) in paragraph at lines 444--447\n\\OT1/cmr/m/n/10 within-single-GPU precision$\\OMS/cmsy/m/n/10 ^^B$\\OT1/cmr/m/n/1\n0 methodology in-ter-ac-tion of 0.08%. The largest sub-interaction is hardware$\n\\OMS/cmsy/m/n/10 ^^B$\\OT1/cmr/m/n/10 temperature\n\nLaTeX Warning: Reference `tab:d_study_budgets' on page 7 undefined on input lin\ne 461.\n\n\nOverfull \\hbox (1.78891pt too wide) in paragraph at lines 461--462\n []\\OT1/cmr/bx/n/10 D-study bud-get rec-om-men-da-tions.[] \\OT1/cmr/m/n/10 Ta-b\nle [] presents benchmark-specific eval-u-a-tion bud-gets for achiev-\n[7]\n\nLaTeX Warning: Reference `tab:robustness' on page 8 undefined on input line 484\n.\n\n\nOverfull \\hbox (1.607pt too wide) in paragraph at lines 518--520\n\\OT1/cmr/m/n/10 dom-i-nance range = 3.5pp vs. 5.7pp for bi-nary scor-ing), sug-\ngest-ing that con-tin-u-ous scor-ing re-duces benchmark-\n[8]\n\nPackage natbib Warning: Citation `dodge2020finetuning' on page 9 undefined on i\nnput line 553.\n\n\nPackage natbib Warning: Citation `bui2025seed' on page 9 undefined on input lin\ne 553.\n\n[9]\n\nPackage natbib Warning: Citation `jiang2017generalized' on page 10 undefined on\n input line 568.\n\n\nPackage natbib Warning: Citation `mesting2026generalizability' on page 10 undef\nined on input line 575.\n\n[10]\n\nPackage natbib Warning: There were undefined citations.\n\n[11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.\npfb>\nOutput written on paper.pdf (11 pages, 280596 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size10.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2]\nOverfull \\hbox (4.70984pt too wide) in paragraph at lines 142--143\n []\\OT1/cmr/bx/n/10 Benchmarks.[] \\OT1/cmr/m/n/10 MMLU (pri-mary, 200 strat-i-f\nied items from 57 sub-jects), GSM8K (200 items), ARC-Challenge\n\nOverfull \\hbox (3.9651pt too wide) in paragraph at lines 146--147\n[]\\OT1/cmr/bx/n/10 Precision\\OT1/cmr/m/n/10 : BF16, FP16 (FP32 ex-cluded af-ter\n iden-ti-fy-ing vLLM \\OT1/cmtt/m/n/10 enforce[]eager \\OT1/cmr/m/n/10 con-found;\n BF16$\\OMS/cmsy/m/n/10 ^^Y$\\OT1/cmr/m/n/10 FP16,\n[3] [4] [5] [6]\nOverfull \\hbox (39.47171pt too wide) in paragraph at lines 444--447\n\\OT1/cmr/m/n/10 within-single-GPU precision$\\OMS/cmsy/m/n/10 ^^B$\\OT1/cmr/m/n/1\n0 methodology in-ter-ac-tion of 0.08%. The largest sub-interaction is hardware$\n\\OMS/cmsy/m/n/10 ^^B$\\OT1/cmr/m/n/10 temperature\n[7]\nOverfull \\hbox (0.92789pt too wide) in paragraph at lines 461--462\n []\\OT1/cmr/bx/n/10 D-study bud-get rec-om-men-da-tions.[] \\OT1/cmr/m/n/10 Ta-b\nle []11[] presents benchmark-specific eval-u-a-tion bud-gets for achiev-\n\nOverfull \\hbox (1.607pt too wide) in paragraph at lines 518--520\n\\OT1/cmr/m/n/10 dom-i-nance range = 3.5pp vs. 5.7pp for bi-nary scor-ing), sug-\ngest-ing that con-tin-u-ous scor-ing re-duces benchmark-\n[8] [9] [10] [11] (./paper.aux)\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1000.600pk>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmbx12.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/\ntype1/public/amsfonts/cm/cmbx9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/p\nublic/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/\namsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmmi5.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pf\nb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb>&lt;/usr/share/\ntexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb>&lt;/usr/share/texlive\n/texmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.\npfb>\nOutput written on paper.pdf (11 pages, 286125 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8685fac4-a613-4c83-9342-f1378e0e18e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T075006 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheor…",
  "leafUuid": "038d1237-1034-4d9f-b6c4-3e896a1676e5",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate LLM evaluation variance analysis paper",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3"
}
```

---

### Assistant

_source line 30 · 2026-05-21T08:33:09.518Z_

There's a label ordering issue — need a third pass to resolve the forward reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "038d1237-1034-4d9f-b6c4-3e896a1676e5",
  "isSidechain": false,
  "requestId": "req_011CbFQRX3uWEEtrn6qkYbTo",
  "type": "assistant",
  "uuid": "70f7e8d5-a895-4896-aac1-63cef16a1d63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWEweQH36yR4BMV69SPFWE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8617,
      "cache_read_input_tokens": 62880,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8617,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 62880,
          "cache_creation_input_tokens": 8617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8617
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

_source line 31 · 2026-05-21T08:33:12.673Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014w5F2tde2QWDSX8YiZUCpP`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Third LaTeX pass for cross-references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70f7e8d5-a895-4896-aac1-63cef16a1d63",
  "isSidechain": false,
  "requestId": "req_011CbFQRX3uWEEtrn6qkYbTo",
  "type": "assistant",
  "uuid": "2446aed2-85c0-4226-b2b6-ce9b825d4bb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DWEweQH36yR4BMV69SPFWE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8617,
      "cache_read_input_tokens": 62880,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8617,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 62880,
          "cache_creation_input_tokens": 8617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8617
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

_source line 32 · 2026-05-21T08:33:13.157Z_

<details><summary>↩ Tool result · `toolu_014w5F2tde2QWDSX8YiZUCpP`</summary>

```text
ts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c
mti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.
pfb>
Output written on paper.pdf (11 pages, 286125 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2446aed2-85c0-4226-b2b6-ce9b825d4bb0",
  "isSidechain": false,
  "promptId": "9d021380-77fd-4766-a060-794a49f7c1c1",
  "type": "user",
  "uuid": "bc0f67f0-3301-43ed-b896-40a75251a6d3",
  "toolUseResult": {
    "stdout": "ts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/c\nmti10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.\npfb>\nOutput written on paper.pdf (11 pages, 286125 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2446aed2-85c0-4226-b2b6-ce9b825d4bb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-21T08:33:13.159Z_

```json
{
  "parentUuid": "bc0f67f0-3301-43ed-b896-40a75251a6d3",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "02058828-3db0-4f7f-8c06-6b1e80afff9d",
  "timestamp": "2026-05-21T08:33:13.159Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 34 · 2026-05-21T08:33:17.813Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01SKnvdkdeKdJHCzJrN3xF4r`</summary>

```json
{
  "command": "grep -c \"Warning.*undefined\" /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst/paper.log",
  "description": "Check for remaining undefined references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02058828-3db0-4f7f-8c06-6b1e80afff9d",
  "isSidechain": false,
  "requestId": "req_011CbFQSF9iejV92wErQby2P",
  "type": "assistant",
  "uuid": "7aa498ad-22a3-4563-8736-07411aee934f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zeB3xzCSxdiFzUp4ZtyYr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 342,
      "cache_read_input_tokens": 71497,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 342,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 129,
          "cache_read_input_tokens": 71497,
          "cache_creation_input_tokens": 342,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 342
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

_source line 35 · 2026-05-21T08:33:17.875Z_

<details><summary>↩ Tool result · `toolu_01SKnvdkdeKdJHCzJrN3xF4r`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7aa498ad-22a3-4563-8736-07411aee934f",
  "isSidechain": false,
  "promptId": "9d021380-77fd-4766-a060-794a49f7c1c1",
  "type": "user",
  "uuid": "f4eb3f11-e5fa-456c-9139-a28cf6d625c0",
  "toolUseResult": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7aa498ad-22a3-4563-8736-07411aee934f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-21T08:33:25.490Z_

编译成功，11页，无未定义引用。

PDF 已生成：`worst/paper.pdf`（11页，286KB）。覆盖所有8个实验（exp-001到exp-008），包含13个表格对应的LaTeX表（Tables 1--13在数据中，论文中呈现为Tables 1--11 + robustness summary），26条参考文献。三条 primary contributions 按 narrative guidance 重构：model×item interaction 量化、IRT vs G-theory benchmark-dependent ratio、variance structure benchmark-invariance。Separability 降为 observation，LOMO spread=0.058 在 Limitations 中如实报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4eb3f11-e5fa-456c-9139-a28cf6d625c0",
  "isSidechain": false,
  "requestId": "req_011CbFQSbM9izKce1AAGFjpi",
  "type": "assistant",
  "uuid": "8a9178ec-4313-4a0e-a884-cdb40cba9973",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/dream_reports/dream_20260521T075006/worst",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vo8eJG6aX8EpQKdzzezsQH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 142,
      "cache_read_input_tokens": 71839,
      "output_tokens": 177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 142,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 177,
          "cache_read_input_tokens": 71839,
          "cache_creation_input_tokens": 142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 142
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

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260521T075006 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheor…",
  "leafUuid": "8a9178ec-4313-4a0e-a884-cdb40cba9973",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate LLM evaluation variance analysis paper",
  "sessionId": "3e227914-44fc-4375-965c-962f04adfef3"
}
```

---
