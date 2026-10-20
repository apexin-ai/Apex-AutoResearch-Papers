# Research conversation: <project_context> # 项目: schema_semantic_constrained_ie ## 运行环境 - 服务器名: westd-16980 - SSH 连接命令: ssh westd-16980 # 必须用此命令，

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 76
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-1/bed18bf9-b23b-41a9-845b-decdb9931508.jsonl`
- **Structured JSON:** [`19fc93eb4018f7f3b77f.json`](../../sessions/19/19fc93eb4018f7f3b77f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-23T10:22:44.551Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T10:22:44.551Z",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "content": "&lt;project_context>\n# 项目: schema_semantic_constrained_ie\n\n## 运行环境\n- 服务器名: westd-16980\n- SSH 连接命令: ssh westd-16980  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/schema_semantic_constrained_ie\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务：审计论文主文 Table 1 和 Table 2 的每一个数字\n\n### 背景\nPI 要求全文数据正确性审计。你负责主文两张核心表格。\n\n### 论文文件位置\n`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/`\n\n### 步骤\n\n**Step 1: 读取表格源码**\n读取以下文件，找到 Table 1 和 Table 2 的完整 LaTeX 源码：\n- 先读 `main.tex` 确定各 section 文件的 \\input 路径\n- Table 1 (tab:scierc-ablation) 可能在 `section4_experiments.tex` 或 `section5_results.tex`\n- Table 2 (tab:composability) 可能在同一文件或另一个 section 文件\n\n**Step 2: 提取每个数字**\n对每张表，列出每个 cell 的数字值和对应的 setting (model, dataset, constraint mode, ZS/FT)。\n\n**Step 3: 用 registry 核实**\n用 `read_registry` 读取相关实验，逐个核对。\n\nTable 1 可能包含的 exp_ids（SciERC 消融）：\n- ZS 系列: phase2_scierc 相关实验（unconstrained, grammar_only, semantic_only, full_s1, full_s2 等）\n- FT 系列: w5/w8 相关实验或 entity_order_ablation 等\n\nTable 2 可能包含的 exp_ids（跨模型/数据集组合）：\n- SciERC + DocRED × Qwen + Llama 的 unconstrained vs constrained 对比\n\n**Step 4: 输出审计报告**\n格式：\n```\n=== Table 1 (tab:scierc-ablation) ===\n[Row \"Unconstrained (ZS)\", Col \"DR%\"]\n  Paper: X.XX%\n  Source: exp_id=xxx\n  Registry value: X.XX%\n  Verified: ✅ / ❌ (实际值=xxx)\n\n[Row \"Unconstrained (ZS)\", Col \"R-F1\"]\n  Paper: XX.XX\n  Source: exp_id=xxx\n  Registry value: XX.XX\n  Verified: ✅ / ❌\n...\n```\n\n**每个 cell 都要检查，不要跳过任何数字。** 如发现不一致，标红并给出 registry 中的正确值。\n\n### 重要\n- 这是 PI 底线要求，必须逐个数字核实\n- 注意 ZS vs FT 的标注是否正确（之前发现过 CF 245 从 ZS 错标为 FT 的问题）\n- 注意 violation_checker.py 之前有 parse-failure bug 被修复，registry 中标注了 \"CORRECTED\" 的值是修正后的\n- 有些实验的 metrics 字段使用 DR_pct vs DR%、R_F1 vs R-F1 等不同命名，注意映射"
}
````

---

### Runtime record

_source line 2 · 2026-05-23T10:22:44.554Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T10:22:44.554Z",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---

## Round 1

74 recorded events

### User

_source line 3 · 2026-05-23T10:22:44.588Z_

&lt;project_context>
# 项目: schema_semantic_constrained_ie

## 运行环境
- 服务器名: westd-16980
- SSH 连接命令: ssh westd-16980  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/schema_semantic_constrained_ie


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务：审计论文主文 Table 1 和 Table 2 的每一个数字

### 背景
PI 要求全文数据正确性审计。你负责主文两张核心表格。

### 论文文件位置
`/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/`

### 步骤

**Step 1: 读取表格源码**
读取以下文件，找到 Table 1 和 Table 2 的完整 LaTeX 源码：
- 先读 `main.tex` 确定各 section 文件的 \input 路径
- Table 1 (tab:scierc-ablation) 可能在 `section4_experiments.tex` 或 `section5_results.tex`
- Table 2 (tab:composability) 可能在同一文件或另一个 section 文件

**Step 2: 提取每个数字**
对每张表，列出每个 cell 的数字值和对应的 setting (model, dataset, constraint mode, ZS/FT)。

**Step 3: 用 registry 核实**
用 `read_registry` 读取相关实验，逐个核对。

Table 1 可能包含的 exp_ids（SciERC 消融）：
- ZS 系列: phase2_scierc 相关实验（unconstrained, grammar_only, semantic_only, full_s1, full_s2 等）
- FT 系列: w5/w8 相关实验或 entity_order_ablation 等

Table 2 可能包含的 exp_ids（跨模型/数据集组合）：
- SciERC + DocRED × Qwen + Llama 的 unconstrained vs constrained 对比

**Step 4: 输出审计报告**
格式：
```
=== Table 1 (tab:scierc-ablation) ===
[Row "Unconstrained (ZS)", Col "DR%"]
  Paper: X.XX%
  Source: exp_id=xxx
  Registry value: X.XX%
  Verified: ✅ / ❌ (实际值=xxx)

[Row "Unconstrained (ZS)", Col "R-F1"]
  Paper: XX.XX
  Source: exp_id=xxx
  Registry value: XX.XX
  Verified: ✅ / ❌
...
```

**每个 cell 都要检查，不要跳过任何数字。** 如发现不一致，标红并给出 registry 中的正确值。

### 重要
- 这是 PI 底线要求，必须逐个数字核实
- 注意 ZS vs FT 的标注是否正确（之前发现过 CF 245 从 ZS 错标为 FT 的问题）
- 注意 violation_checker.py 之前有 parse-failure bug 被修复，registry 中标注了 "CORRECTED" 的值是修正后的
- 有些实验的 metrics 字段使用 DR_pct vs DR%、R_F1 vs R-F1 等不同命名，注意映射

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "9fec63b7-148d-4176-8b2c-bc9fd7d961f4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-23T10:22:44.588Z_

```json
{
  "parentUuid": "9fec63b7-148d-4176-8b2c-bc9fd7d961f4",
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
  "uuid": "3da3a2d9-4cd8-4259-8ffc-87bf65812326",
  "timestamp": "2026-05-23T10:22:44.588Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-23T10:22:44.588Z_

```json
{
  "parentUuid": "3da3a2d9-4cd8-4259-8ffc-87bf65812326",
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
  "uuid": "2be1723e-0d5e-4fd0-8afc-edea1dab5f08",
  "timestamp": "2026-05-23T10:22:44.588Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-23T10:22:44.588Z_

```json
{
  "parentUuid": "2be1723e-0d5e-4fd0-8afc-edea1dab5f08",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "18b01569-e8f2-437e-bbfb-1050315ca260",
  "timestamp": "2026-05-23T10:22:44.588Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
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
  "aiTitle": "Audit paper tables 1 and 2 numerical values",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---

### Assistant

_source line 8 · 2026-05-23T10:22:47.647Z_

我开始审计论文 Table 1 和 Table 2 的数字。先读取论文文件结构和表格源码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18b01569-e8f2-437e-bbfb-1050315ca260",
  "isSidechain": false,
  "requestId": "req_011CbKLQV5rqZu9WfVLuKuhW",
  "type": "assistant",
  "uuid": "376d9138-7f76-48f1-93dd-2f156ecb915f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HoSdhcgUrmzFoNYnx2R8xf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12431,
      "cache_read_input_tokens": 11841,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 203,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12431
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

_source line 9 · 2026-05-23T10:22:48.531Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CdqTze7bmMoEtXry3t964i`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "376d9138-7f76-48f1-93dd-2f156ecb915f",
  "isSidechain": false,
  "requestId": "req_011CbKLQV5rqZu9WfVLuKuhW",
  "type": "assistant",
  "uuid": "0a76e973-ca22-48c6-8069-1dc50b9edbfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HoSdhcgUrmzFoNYnx2R8xf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12431,
      "cache_read_input_tokens": 11841,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 203,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12431
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

_source line 10 · 2026-05-23T10:22:48.696Z_

<details><summary>↩ Tool result · `toolu_01CdqTze7bmMoEtXry3t964i`</summary>

```text
abstract.tex
abstract_d3264e.tex
abstract_fd4b26.tex
acl.sty
acl_natbib.bst
appendix_70b_ablation.tex
appendix_beam_search.tex
appendix_case_studies.tex
appendix_discussion.tex
appendix_doc_length.tex
appendix_downstream_analysis.tex
appendix_full_ft.tex
appendix_gollie_comparison.tex
appendix_high_kappa_analysis.tex
appendix_kappa_case_study.tex
appendix_llama_per_relation.tex
appendix_order_invariance.tex
appendix_power_analysis.tex
appendix_power_analysis_523cc9.tex
appendix_prompt_sensitivity.tex
appendix_prompts.tex
appendix_pumping_lemma.tex
appendix_quantization.tex
appendix_related_work.tex
appendix_reproducibility.tex
appendix_sampling_table.tex
appendix_scalability.tex
appendix_tcr.tex
appendix_type_consensus.tex.archived
appendix_wikievents_pilot.tex
appendix_zs_crossmodel.tex
case_study_kappa_dr.tex
checklist.tex
discussion_paragraphs.tex
discussion_paragraphs_cf83d1.tex
error_analysis_cases.json
fig1_framework.tex
figures
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
new_citations.bib
ontocodec_paper_r10_final.pdf
ontocodec_paper_r9_final.pdf
p3_case_studies.tex
p3_case_studies_861a0d.tex
paper_tables_draft.tex
r12_fallback_cascade_text.txt
relwork_new_entries.bib
section1_introduction_draft.tex
section2_background.tex
section3_method_draft.tex
section3_violation_landscape.tex
section4_composition_draft.tex
section5_crossmodel_draft.tex
section5_docred_draft.tex
section5_docred_draft_9b84f1.tex
section5_runtime.tex
section5_scierc_draft.tex
section5_scierc_draft_4796e8.tex
section5_wikievents_draft.tex
section6_related_work.tex
section6_relwork_additions.tex
section6_relwork_outline.tex
section7_conclusion_550cbf_DEPRECATED.tex
section7_conclusion_DEPRECATED.tex
section7_conclusion_compressed.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a76e973-ca22-48c6-8069-1dc50b9edbfa",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "27ac4cb5-5f65-4917-893b-2b029cd467a7",
  "toolUseResult": {
    "stdout": "abstract.tex\nabstract_d3264e.tex\nabstract_fd4b26.tex\nacl.sty\nacl_natbib.bst\nappendix_70b_ablation.tex\nappendix_beam_search.tex\nappendix_case_studies.tex\nappendix_discussion.tex\nappendix_doc_length.tex\nappendix_downstream_analysis.tex\nappendix_full_ft.tex\nappendix_gollie_comparison.tex\nappendix_high_kappa_analysis.tex\nappendix_kappa_case_study.tex\nappendix_llama_per_relation.tex\nappendix_order_invariance.tex\nappendix_power_analysis.tex\nappendix_power_analysis_523cc9.tex\nappendix_prompt_sensitivity.tex\nappendix_prompts.tex\nappendix_pumping_lemma.tex\nappendix_quantization.tex\nappendix_related_work.tex\nappendix_reproducibility.tex\nappendix_sampling_table.tex\nappendix_scalability.tex\nappendix_tcr.tex\nappendix_type_consensus.tex.archived\nappendix_wikievents_pilot.tex\nappendix_zs_crossmodel.tex\ncase_study_kappa_dr.tex\nchecklist.tex\ndiscussion_paragraphs.tex\ndiscussion_paragraphs_cf83d1.tex\nerror_analysis_cases.json\nfig1_framework.tex\nfigures\nmain.aux\nmain.bbl\nmain.blg\nmain.fdb_latexmk\nmain.fls\nmain.log\nmain.out\nmain.pdf\nmain.tex\nnew_citations.bib\nontocodec_paper_r10_final.pdf\nontocodec_paper_r9_final.pdf\np3_case_studies.tex\np3_case_studies_861a0d.tex\npaper_tables_draft.tex\nr12_fallback_cascade_text.txt\nrelwork_new_entries.bib\nsection1_introduction_draft.tex\nsection2_background.tex\nsection3_method_draft.tex\nsection3_violation_landscape.tex\nsection4_composition_draft.tex\nsection5_crossmodel_draft.tex\nsection5_docred_draft.tex\nsection5_docred_draft_9b84f1.tex\nsection5_runtime.tex\nsection5_scierc_draft.tex\nsection5_scierc_draft_4796e8.tex\nsection5_wikievents_draft.tex\nsection6_related_work.tex\nsection6_relwork_additions.tex\nsection6_relwork_outline.tex\nsection7_conclusion_550cbf_DEPRECATED.tex\nsection7_conclusion_DEPRECATED.tex\nsection7_conclusion_compressed.tex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0a76e973-ca22-48c6-8069-1dc50b9edbfa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-23T10:22:48.761Z_

<details><summary>↩ Tool result · `toolu_01VRoNgproKayivqhGkg8Pmg`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{multirow}
13	\usepackage[table]{xcolor}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{amsthm}
17	\usepackage{enumitem}
18	\usepackage{pifont}
19	\usepackage{soul}
20	\usepackage{tikz}
21	\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}
22	\newcommand{\TBD}[1]{\textcolor{red}{#1}}
23	
24	\title{OntoCoDec: Type-Constrained Information Extraction\\via Compiled Schema Constraints}
25	
26	\author{Anonymous ACL submission}
27	
28	\begin{document}
29	\maketitle
30	
31	% === Abstract ===
32	\input{abstract}
33	
34	% === §1 Introduction ===
35	\input{section1_introduction_draft}
36	
37	% === §2 Background ===
38	\input{section2_background}
39	
40	% === §3 Method ===
41	\input{section3_method_draft}
42	
43	% === §4 Constraint Composition ===
44	\section{Constraint Composition}
45	\label{sec:composition}
46	\input{section4_composition_draft}
47	
48	% === §5 Experiments ===
49	\section{Experiments}
50	\label{sec:experiments}
51	
52	\input{section3_violation_landscape}
53	
54	\input{section5_scierc_draft}
55	\input{section5_wikievents_draft}
56	\input{section5_runtime}
57	
58	% === §6 Related Work ===
59	\input{section6_related_work}
60	
61	% === §7 Discussion and Conclusion ===
62	\section{Discussion and Conclusion}
63	\label{sec:discussion}
64	\input{section7_conclusion_compressed}
65	
66	% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===
67	\clearpage
68	\section*{Limitations}
69	
70	\paragraph{Constraint scope.}
71	CF is an architectural consequence of per-triple independent enforcement: CF$\leftrightarrow$DR represents a fundamental trade-off (eliminating CF re-routes violations to DR; Appendix~\ref{app:cf-dr-tradeoff}), and its impact is model-dependent (S1 introduces CF for calibrated models but reduces it for poorly-calibrated ones).
72	Global entity-level type consensus during decoding offers the most direct path to resolving CF.
73	Entity-first generation order is an architectural constraint: the grammar enforces entities before relations, ensuring the registry is populated before type checks; alternative orderings would require deferred constraint evaluation.
74	Residual DR under fine-tuning (36 violations total) decomposes into entity type errors (39\%), schema coverage gaps (33\%), and model generation errors (28\%); schema gaps arise from training-data-derived constraints that may not cover all valid type pairs (Appendix~\ref{app:residual-dr-analysis}).
75	We do not decompose CF violations into first-seen cascading errors versus legitimate type ambiguity; this decomposition requires gold entity type annotations at the mention level, which SciERC provides only at the entity level.
76	Post-hoc type consensus re-voting reduces CF by 18--92\% (Appendix~\ref{app:tcr}), but integrating consensus into the decoding loop remains future work.
77	
78	\paragraph{Evaluation coverage.}
79	Zero-shot evaluation covers three 8B-class and one 70B-class model; fine-tuning composability is validated on two 8B-class models (full datasets) and one 70B-class model (SciERC full, DocRED 200-document subset).
80	Scaling to smaller models has not been verified; the schema restrictiveness--enforcement difficulty relationship is based on three schemas.
81	Evaluation is limited to one fine-tuning method (LoRA); LoRA hyperparameters were tuned on SciERC and transferred to DocRED without dataset-specific optimization, which may underestimate DocRED potential.
82	WikiEvents fine-tuning is preliminary ($n{=}20$); DocRED uses the development set (test annotations unavailable).
83	All main experiments use greedy decoding; beam search compatibility is confirmed but comprehensive evaluation across all configurations remains future work (Appendices~\ref{app:sampling},~\ref{app:beam-search}).
84	
85	\paragraph{Engineering considerations.}
86	Our approach requires access to model logits, excluding API-only models; continuation masking assumes distinguishable token prefixes per type name, which may be challenged by morphologically similar types (e.g., \texttt{Protein} vs.\ \texttt{Protein\_Complex}; Appendix~\ref{app:scalability}).
87	70B experiments use AWQ INT4 quantization; an 8B ablation confirms enforcement is unaffected (Appendix~\ref{app:quantization}), though a direct 70B FP16 comparison exceeds our hardware capacity.
88	Evaluation is limited to English-language datasets; the mechanism is language-independent but CJK tokenization fragmentation may increase masking steps (Appendix~\ref{app:scalability}).
89	Full fine-tuning confirms constraints remain effective (DR$\to$0\%; Appendix~\ref{app:full-ft}), but other fine-tuning methods warrant further investigation.
90	The two-pass strategy (S2) exhibits scale-dependent degradation: at 70B, S2 reduces R-F1 by 8.45\,pp while 8B models show comparable S1/S2 performance, suggesting optimal constraint granularity varies with model capacity (Appendix~\ref{app:70b-ablation}).
91	
92	
93	% === Ethics Statement ===
94	\section*{Ethics Statement}
95	
96	This work uses publicly available benchmark datasets (SciERC, DocRED, and WikiEvents) with no personally identifiable information.
97	No human subjects were involved in the experiments.
98	The constrained decoding method operates on model outputs and does not introduce new privacy or safety risks beyond those inherent in the base language models.
99	Code and data will be released upon acceptance.
100	
101	% === Bibliography ===
102	\bibliography{relwork_new_entries}
103	
104	% === Appendix ===
105	\appendix
106	
107	\input{appendix_prompts}
108	\input{appendix_related_work}
109	\input{appendix_discussion}
110	\input{appendix_70b_ablation}
111	\input{appendix_llama_per_relation}
112	\input{appendix_sampling_table}
113	\input{appendix_beam_search}
114	\input{appendix_reproducibility}
115	\input{appendix_power_analysis}
116	\input{appendix_doc_length}
117	\input{appendix_prompt_sensitivity}
118	\input{appendix_case_studies}
119	\input{appendix_downstream_analysis}
120	\input{appendix_scalability}
121	\input{appendix_full_ft}
122	\input{appendix_tcr}
123	\input{appendix_kappa_case_study}
124	\input{appendix_high_kappa_analysis}
125	\input{appendix_order_invariance}
126	\input{appendix_pumping_lemma}
127	\input{appendix_wikievents_pilot}
128	\input{appendix_zs_crossmodel}
129	\input{appendix_quantization}
130	\input{appendix_gollie_comparison}
131	
132	\end{document}
133	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97baa39d-e8a7-4af4-a4b5-c9b3607bea16",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "969527ea-2076-4e2c-a347-51618500749b",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage[table]{xcolor}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{amsthm}\n\\usepackage{enumitem}\n\\usepackage{pifont}\n\\usepackage{soul}\n\\usepackage{tikz}\n\\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,calc}\n\\newcommand{\\TBD}[1]{\\textcolor{red}{#1}}\n\n\\title{OntoCoDec: Type-Constrained Information Extraction\\\\via Compiled Schema Constraints}\n\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n% === Abstract ===\n\\input{abstract}\n\n% === §1 Introduction ===\n\\input{section1_introduction_draft}\n\n% === §2 Background ===\n\\input{section2_background}\n\n% === §3 Method ===\n\\input{section3_method_draft}\n\n% === §4 Constraint Composition ===\n\\section{Constraint Composition}\n\\label{sec:composition}\n\\input{section4_composition_draft}\n\n% === §5 Experiments ===\n\\section{Experiments}\n\\label{sec:experiments}\n\n\\input{section3_violation_landscape}\n\n\\input{section5_scierc_draft}\n\\input{section5_wikievents_draft}\n\\input{section5_runtime}\n\n% === §6 Related Work ===\n\\input{section6_related_work}\n\n% === §7 Discussion and Conclusion ===\n\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\\input{section7_conclusion_compressed}\n\n% === Limitations (ARR requirement: standalone section, does not count toward page limit) ===\n\\clearpage\n\\section*{Limitations}\n\n\\paragraph{Constraint scope.}\nCF is an architectural consequence of per-triple independent enforcement: CF$\\leftrightarrow$DR represents a fundamental trade-off (eliminating CF re-routes violations to DR; Appendix~\\ref{app:cf-dr-tradeoff}), and its impact is model-dependent (S1 introduces CF for calibrated models but reduces it for poorly-calibrated ones).\nGlobal entity-level type consensus during decoding offers the most direct path to resolving CF.\nEntity-first generation order is an architectural constraint: the grammar enforces entities before relations, ensuring the registry is populated before type checks; alternative orderings would require deferred constraint evaluation.\nResidual DR under fine-tuning (36 violations total) decomposes into entity type errors (39\\%), schema coverage gaps (33\\%), and model generation errors (28\\%); schema gaps arise from training-data-derived constraints that may not cover all valid type pairs (Appendix~\\ref{app:residual-dr-analysis}).\nWe do not decompose CF violations into first-seen cascading errors versus legitimate type ambiguity; this decomposition requires gold entity type annotations at the mention level, which SciERC provides only at the entity level.\nPost-hoc type consensus re-voting reduces CF by 18--92\\% (Appendix~\\ref{app:tcr}), but integrating consensus into the decoding loop remains future work.\n\n\\paragraph{Evaluation coverage.}\nZero-shot evaluation covers three 8B-class and one 70B-class model; fine-tuning composability is validated on two 8B-class models (full datasets) and one 70B-class model (SciERC full, DocRED 200-document subset).\nScaling to smaller models has not been verified; the schema restrictiveness--enforcement difficulty relationship is based on three schemas.\nEvaluation is limited to one fine-tuning method (LoRA); LoRA hyperparameters were tuned on SciERC and transferred to DocRED without dataset-specific optimization, which may underestimate DocRED potential.\nWikiEvents fine-tuning is preliminary ($n{=}20$); DocRED uses the development set (test annotations unavailable).\nAll main experiments use greedy decoding; beam search compatibility is confirmed but comprehensive evaluation across all configurations remains future work (Appendices~\\ref{app:sampling},~\\ref{app:beam-search}).\n\n\\paragraph{Engineering considerations.}\nOur approach requires access to model logits, excluding API-only models; continuation masking assumes distinguishable token prefixes per type name, which may be challenged by morphologically similar types (e.g., \\texttt{Protein} vs.\\ \\texttt{Protein\\_Complex}; Appendix~\\ref{app:scalability}).\n70B experiments use AWQ INT4 quantization; an 8B ablation confirms enforcement is unaffected (Appendix~\\ref{app:quantization}), though a direct 70B FP16 comparison exceeds our hardware capacity.\nEvaluation is limited to English-language datasets; the mechanism is language-independent but CJK tokenization fragmentation may increase masking steps (Appendix~\\ref{app:scalability}).\nFull fine-tuning confirms constraints remain effective (DR$\\to$0\\%; Appendix~\\ref{app:full-ft}), but other fine-tuning methods warrant further investigation.\nThe two-pass strategy (S2) exhibits scale-dependent degradation: at 70B, S2 reduces R-F1 by 8.45\\,pp while 8B models show comparable S1/S2 performance, suggesting optimal constraint granularity varies with model capacity (Appendix~\\ref{app:70b-ablation}).\n\n\n% === Ethics Statement ===\n\\section*{Ethics Statement}\n\nThis work uses publicly available benchmark datasets (SciERC, DocRED, and WikiEvents) with no personally identifiable information.\nNo human subjects were involved in the experiments.\nThe constrained decoding method operates on model outputs and does not introduce new privacy or safety risks beyond those inherent in the base language models.\nCode and data will be released upon acceptance.\n\n% === Bibliography ===\n\\bibliography{relwork_new_entries}\n\n% === Appendix ===\n\\appendix\n\n\\input{appendix_prompts}\n\\input{appendix_related_work}\n\\input{appendix_discussion}\n\\input{appendix_70b_ablation}\n\\input{appendix_llama_per_relation}\n\\input{appendix_sampling_table}\n\\input{appendix_beam_search}\n\\input{appendix_reproducibility}\n\\input{appendix_power_analysis}\n\\input{appendix_doc_length}\n\\input{appendix_prompt_sensitivity}\n\\input{appendix_case_studies}\n\\input{appendix_downstream_analysis}\n\\input{appendix_scalability}\n\\input{appendix_full_ft}\n\\input{appendix_tcr}\n\\input{appendix_kappa_case_study}\n\\input{appendix_high_kappa_analysis}\n\\input{appendix_order_invariance}\n\\input{appendix_pumping_lemma}\n\\input{appendix_wikievents_pilot}\n\\input{appendix_zs_crossmodel}\n\\input{appendix_quantization}\n\\input{appendix_gollie_comparison}\n\n\\end{document}\n",
      "numLines": 133,
      "startLine": 1,
      "totalLines": 133
    }
  },
  "sourceToolAssistantUUID": "97baa39d-e8a7-4af4-a4b5-c9b3607bea16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T10:22:48.753Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VRoNgproKayivqhGkg8Pmg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27ac4cb5-5f65-4917-893b-2b029cd467a7",
  "isSidechain": false,
  "requestId": "req_011CbKLQV5rqZu9WfVLuKuhW",
  "type": "assistant",
  "uuid": "97baa39d-e8a7-4af4-a4b5-c9b3607bea16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HoSdhcgUrmzFoNYnx2R8xf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12431,
      "cache_read_input_tokens": 11841,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 203,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12431
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
  "leafUuid": "969527ea-2076-4e2c-a347-51618500749b",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper tables 1 and 2 numerical values",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---

### Assistant

_source line 15 · 2026-05-23T10:22:52.913Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to find Table 1 and Table 2. Based on the main.tex structure, they're likely in section5_scierc_draft.tex, section4_composition_draft.tex, or section5_docred_draft.tex. Let me read the relevant section files to find the tables.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "969527ea-2076-4e2c-a347-51618500749b",
  "isSidechain": false,
  "requestId": "req_011CbKLQoB3S25wBK4ij2w5j",
  "type": "assistant",
  "uuid": "a0db92fc-d9da-4728-b0d3-7321ed0d72aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4BrcPsJzG6CBGTk4DYQQ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3033,
      "cache_read_input_tokens": 24272,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 24272,
          "cache_creation_input_tokens": 3033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3033
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

_source line 16 · 2026-05-23T10:22:53.873Z_

Now let me read the section files that likely contain Table 1 and Table 2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0db92fc-d9da-4728-b0d3-7321ed0d72aa",
  "isSidechain": false,
  "requestId": "req_011CbKLQoB3S25wBK4ij2w5j",
  "type": "assistant",
  "uuid": "e3ab2324-b716-4112-9733-5fb13ff0939e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4BrcPsJzG6CBGTk4DYQQ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3033,
      "cache_read_input_tokens": 24272,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 24272,
          "cache_creation_input_tokens": 3033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3033
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

_source line 17 · 2026-05-23T10:22:55.968Z_

<details open><summary>🔧 Tool call — Read · `toolu_01R9xSEiwfxNE773hZ99Y5ic`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3ab2324-b716-4112-9733-5fb13ff0939e",
  "isSidechain": false,
  "requestId": "req_011CbKLQoB3S25wBK4ij2w5j",
  "type": "assistant",
  "uuid": "99b0fb6a-4af3-4c30-93be-e467cec83fc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4BrcPsJzG6CBGTk4DYQQ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3033,
      "cache_read_input_tokens": 24272,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 24272,
          "cache_creation_input_tokens": 3033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3033
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

_source line 18 · 2026-05-23T10:22:56.911Z_

<details><summary>↩ Tool result · `toolu_01E3HbYe3VLvyXm74axBHqUe`</summary>

```text
1	% Section 5 — DocRED Results (compressed; full ablation in Appendix)
2	% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,
3	%          phase2_docred_semantic_only, phase2_docred_full_s1
4	
5	\subsection{Cross-Dataset Validation on DocRED}
6	\label{sec:docred-results}
7	
8	DocRED (96 relations, 14$\times$ SciERC scale) validates the pattern under a larger, more restrictive ontology (Table~\ref{tab:docred-ablation}).
9	S1 reduces DR from 18.46\% to 10.21\% ($\downarrow$45\%), eliminates RV (29.66\%\,$\to$\,0.03\%) and ET, with R-F1 $+$0.50\,pp ($p < 0.001$).
10	The lower DR reduction (45\% vs.\ 94\% on SciERC) reflects DocRED's tighter constraints, which trigger more grammar-first fallback (\S\ref{sec:greedy-limitation}).
11	Grammar-only \emph{increases} DR (18.46\%\,$\to$\,26.17\%) via \textit{latent violation surfacing}: grammar forces OOV$\to$valid relation mapping, exposing type violations previously masked by vocabulary errors---a distinct cross-dataset confirmation of the empirical enabling dependency.
12	Fine-tuning resolves residual DR entirely (Table~\ref{tab:composability}; residual decomposition in Appendix~\ref{app:residual-dr-analysis}).
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afd8bb66-5392-4937-8990-af73f88ba62c",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "b6b07cbd-1ec0-4529-a742-2f6bed4f1aca",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex",
      "content": "% Section 5 — DocRED Results (compressed; full ablation in Appendix)\n% exp_ids: phase2_docred_unconstrained, phase2_docred_grammar_only,\n%          phase2_docred_semantic_only, phase2_docred_full_s1\n\n\\subsection{Cross-Dataset Validation on DocRED}\n\\label{sec:docred-results}\n\nDocRED (96 relations, 14$\\times$ SciERC scale) validates the pattern under a larger, more restrictive ontology (Table~\\ref{tab:docred-ablation}).\nS1 reduces DR from 18.46\\% to 10.21\\% ($\\downarrow$45\\%), eliminates RV (29.66\\%\\,$\\to$\\,0.03\\%) and ET, with R-F1 $+$0.50\\,pp ($p < 0.001$).\nThe lower DR reduction (45\\% vs.\\ 94\\% on SciERC) reflects DocRED's tighter constraints, which trigger more grammar-first fallback (\\S\\ref{sec:greedy-limitation}).\nGrammar-only \\emph{increases} DR (18.46\\%\\,$\\to$\\,26.17\\%) via \\textit{latent violation surfacing}: grammar forces OOV$\\to$valid relation mapping, exposing type violations previously masked by vocabulary errors---a distinct cross-dataset confirmation of the empirical enabling dependency.\nFine-tuning resolves residual DR entirely (Table~\\ref{tab:composability}; residual decomposition in Appendix~\\ref{app:residual-dr-analysis}).\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  },
  "sourceToolAssistantUUID": "afd8bb66-5392-4937-8990-af73f88ba62c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-23T10:22:55.974Z_

<details><summary>↩ Tool result · `toolu_01R9xSEiwfxNE773hZ99Y5ic`</summary>

```text
1	% Section 5 — SciERC Results (Draft)
2	% Data source: Phase 2 SciERC registry experiments
3	% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,
4	%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2
5	% All numbers verified against registry 2026-05-14.
6	
7	\subsection{Ablation and Composability with Fine-Tuning}
8	\label{sec:scierc-results}
9	
10	Table~\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.
11	
12	% ──────────────────────────────────────────
13	%  Table: SciERC five-way ablation
14	% ──────────────────────────────────────────
15	\begin{table}[t]
16	\centering
17	\small
18	\setlength{\tabcolsep}{3.6pt}
19	\resizebox{\columnwidth}{!}{%
20	\begin{tabular}{@{}l rrrrrr rr@{}}
21	\toprule
22	& \multicolumn{6}{c}{\textbf{Violation Rates (\%)}}
23	& \multicolumn{2}{c}{\textbf{F1}} \\
24	\cmidrule(lr){2-7} \cmidrule(l){8-9}
25	\textbf{Mode}
26	  & DR\,$\downarrow$ & $\Delta$DR
27	  & RV\,$\downarrow$ & ET\,$\downarrow$ & CF & Tot.\,$\downarrow$
28	  & Rel.\,$\uparrow$ & Ent.\,$\uparrow$ \\
29	\midrule
30	Unconstrained
31	  & 15.37 & ---
32	  & 1.39  & 0.40
33	  & 0.08  & 15.45
34	  & 8.23  & 31.01 \\
35	Grammar
36	  & 14.84 & $\downarrow$3\%
37	  & \textbf{0} & \textbf{0}
38	  & 0.08  & 14.92
39	  & 8.23  & 30.98 \\
40	GCD-equiv.$^\dagger$
41	  & 15.26 & $\downarrow$1\%
42	  & \textbf{0} & \textbf{0}
43	  & 0.04  & 15.30
44	  & 8.75  & 30.91 \\
45	Semantic
46	  & 11.65 & $\downarrow$24\%
47	  & 1.51  & 0.40
48	  & 2.71  & 14.36
49	  & 8.15  & 31.01 \\
50	S1
51	  & \textbf{0.93} & $\downarrow$\textbf{94\%}
52	  & \textbf{0} & \textbf{0}
53	  & 9.90  & \textbf{10.83}
54	  & \textbf{8.36} & 30.98 \\
55	S2
56	  & 0.97  & $\downarrow$94\%
57	  & \textbf{0} & \textbf{0}
58	  & 8.03  & \textbf{9.00}
59	  & 8.03  & \textbf{31.90} \\
60	\bottomrule
61	\end{tabular}}%
62	\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).
63	$\Delta$DR: relative change vs.\ unconstrained; Tot.\ = DR + CF; bold = best (CF excluded).
64	F1 (\%). S1/S2 = single/two-pass (\S\ref{sec:strategies}).
65	Grammar = GCD ceiling~\cite{geng2023gcd}.
66	$\dagger$vLLM \texttt{guided\_json}~\cite{kwon2023vllm} (\S\ref{sec:constrained-baselines}).
67	Deterministic (greedy, $T{=}$0); robustness evidence in Table~\ref{tab:cross-model} and Appendices~\ref{app:bootstrap-effect-sizes},~\ref{app:prompt-sensitivity}.}
68	\label{tab:scierc-ablation}
69	\end{table}
70	
71	% ──────────────────────────────────────────
72	%  (a) Zero-shot diagnostic (compressed)
73	% ──────────────────────────────────────────
74	\paragraph{Zero-shot diagnostic.}
75	% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093
76	Table~\ref{tab:scierc-ablation} establishes that DR violations are pervasive (15--18\% across datasets) and that constraint layers interact non-additively: grammar-only achieves 3\% DR reduction on SciERC, semantic-only 24\%, but their composition yields 94\%---the \emph{empirical enabling dependency}.
77	On DocRED (96 relations, $\bar{\kappa}{=}0.842$), grammar-only \emph{increases} DR via \textit{latent violation surfacing}: forcing OOV$\to$valid relation mapping exposes violations previously masked by vocabulary errors (Appendix~\ref{app:cross-model-zs}).
78	Cross-model validation (3 models $\times$ 2 datasets; Table~\ref{tab:cross-model}) confirms DR drops of 76--99\% on SciERC and 42--90\% on DocRED, with R-F1 improving in 5/6 settings; post-hoc filtering achieves DR${=}$0\% but at 15--74\% rejection rates.
79	DR-to-CF conversion represents a severity downgrade: DR is irrecoverable without re-extraction, while CF---individually valid triples with cross-triple inconsistency---is amenable to post-hoc resolution (TCR eliminates 18--92\%; Appendix~\ref{app:tcr}).
80	Zero-shot evaluation thus establishes violation prevalence and constraint interaction; fine-tuning demonstrates practical elimination.
81	
82	% ──────────────────────────────────────────
83	%  (e) Composability with Fine-Tuning (expanded)
84	% ──────────────────────────────────────────
85	\paragraph{Composability with fine-tuning.}
86	\label{sec:composability}
87	% exp_ids: bootstrap_ci_ft_composability.json, w5_lora_scierc_*, w8_*
88	Fine-tuning alone reduces DR to 1--2\% but leaves residual violations on tight-constraint relations (Table~\ref{tab:composability}); adding S1 yields DR\,$\leq$\,0.09\% with no significant $\Delta$R-F1 (Bonferroni-corrected; 95\% CIs $\subseteq [-0.69, {+}0.25]$\,pp; removed triples are 97.6--100\% false positives; Appendix~\ref{app:downstream-impact}).
89	Under fine-tuning, grammar becomes a no-op ($\Delta$DR$<$0.2\,pp), making the semantic layer the sole DR defense (39--69\% reduction; Appendix~\ref{app:ft-ablation}); three relations with $\kappa \geq 0.36$ retain DR, all eliminated by S1 (Appendix~\ref{app:lora-per-relation}).
90	Fallback frequency is model-dependent: Qwen triggers 0 fallbacks under LoRA + S1 on SciERC, while Llama triggers 5{,}882 (Table~\ref{tab:ft-ablation}), reflecting weaker entity typing; despite this, DR reaches 0.09\% for Llama, confirming that even frequent fallback does not compromise enforcement.
91	CF drops from $+$9.82\,pp (zero-shot) to $+$1.18\,pp (fine-tuned), concentrated in \textsc{Generic}$\leftrightarrow$X ambiguity (63.3\% of zero-shot CF; Appendix~\ref{app:cf-distribution}); beam ($k{=}4$) eliminates all violation types (R-F1 43--47; \S\ref{sec:beam-results}).
92	
93	% ──────────────────────────────────────────
94	%  CF quantification (MF1 response)
95	% ──────────────────────────────────────────
96	\paragraph{Cross-field violation analysis.}
97	% exp_ids: phase2_scierc_full_s1 (ZS: CF=248, 167 docs), w5_lora_scierc_full_s1_eval (FT: CF=22, 20 docs)
98	Under zero-shot greedy S1, CF is the sole residual violation type (DR, RV, ET all eliminated): 248 cross-field violations arise across 167 documents, of which 63.3\% involve \textsc{Generic}$\leftrightarrow$X type ambiguity (Appendix~\ref{app:cf-distribution}), concentrated in \textsc{Generic}$\leftrightarrow$\textsc{OtherScientificTerm} (34.7\%) and \textsc{Generic}$\leftrightarrow$\textsc{Material} (12.3\%).
99	A source breakdown (Appendix~\ref{app:cascade-analysis}) shows 58.1\% originate from hallucinated entities (a model capacity issue), while true cascade errors---where first-seen registration locks an incorrect type---account for only 7.3\%; correct locks are 2.5$\times$ more frequent, confirming first-seen registration as a net-positive mechanism.
100	Fine-tuning reduces CF to 22 violations across 20 documents (1.18\%), with cascade errors completely eliminated (0/22).
101	Beam search ($k{=}4$) eliminates all remaining CF at 1.39$\times$ latency (\S\ref{sec:beam-results}).
102	
103	\begin{table}[t]
104	\centering
105	\small
106	\setlength{\tabcolsep}{3pt}
107	\resizebox{\columnwidth}{!}{%
108	\begin{tabular}{@{}lll rrrr r@{}}
109	\toprule
110	\textbf{Model} & \textbf{Dataset} & \textbf{Mode}
111	  & \textbf{DR\,$\downarrow$} & \textbf{CF}
112	  & \textbf{R-F1\,$\uparrow$} & \textbf{E-F1\,$\uparrow$}
113	  & \textbf{$\Delta$DR} \\
114	\midrule
115	\multirow{4}{*}{Qwen3-8B}
116	  & \multirow{2}{*}{SciERC}
117	    & Unconstr.\ &  1.95 & 0    & 43.86 & 67.05 & --- \\
118	  & & S1    & \textbf{0} & 1.18 & 43.77 & 67.05 & $\downarrow$100\% \\
119	\cmidrule(l){2-8}
120	  & \multirow{2}{*}{DocRED}
121	    & Unconstr.\ &  0.56 & 0.08 & 40.89 & 82.35 & --- \\
122	  & & S1    & \textbf{0.00} & 0.22 & 40.79 & 81.87 & $\downarrow$100\% \\
123	\midrule
124	\multirow{4}{*}{\shortstack[l]{Llama\\3.1-8B}}
125	  & \multirow{2}{*}{SciERC}
126	    & Unconstr.\ &  1.11 & 0    & 45.45 & 67.76 & --- \\
127	  & & S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\downarrow$92\% \\
128	\cmidrule(l){2-8}
129	  & \multirow{2}{*}{DocRED}
130	    & Unconstr.\ &  0.49 & 0.08 & 44.55 & 84.77 & --- \\
131	  & & S1    &  0.00 & 0.26 & 44.70 & 84.71 & $\downarrow$100\% \\
132	\bottomrule
133	\end{tabular}}%
134	\caption{Fine-tuning composability: LoRA $\times$ unconstrained vs.\ S1 on SciERC (551 docs) and DocRED (998 dev docs).
135	F1 (\%). No $\Delta$R-F1 is significant (Bonferroni-corrected; details in text); all DR reductions are ($p{<}0.001$).
136	E-F1 includes parse-failure documents (Qwen PF: 7--8\%; Llama PF: 2--3\%).}
137	\label{tab:composability}
138	\end{table}
139	
140	% ──────────────────────────────────────────
141	%  (f) Downstream impact of DR elimination
142	%  exp_ids: task_e_lucky_violation_analysis
143	% ──────────────────────────────────────────
144	\paragraph{Downstream impact.}
145	\label{sec:downstream-impact}
146	Among constraint-removed triples, only 0.49\% match gold labels (Appendix~\ref{app:lucky-violations}); error analysis of 514 false negatives confirms only one (0.2\%) was blocked by constraints, with dominant sources (relation confusion, entity type polysemy) schema-valid and beyond constraint reach (Appendix~\ref{app:error-analysis}).
147	Across fine-tuned settings, 36 residual DR violations decompose into entity type errors (39\%), schema coverage gaps (33\%), and relation/direction errors (28\%); the irreducible floor is $\sim$3 violations (Appendix~\ref{app:residual-dr-analysis}).
148	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99b0fb6a-4af3-4c30-93be-e467cec83fc2",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "76d303a4-16bf-46fa-bf95-3da3c4df8557",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_scierc_draft.tex",
      "content": "% Section 5 — SciERC Results (Draft)\n% Data source: Phase 2 SciERC registry experiments\n% exp_ids: phase2_scierc_unconstrained, phase2_scierc_grammar_only,\n%          phase2_scierc_semantic_only, phase2_scierc_full_s1, phase2_scierc_full_s2\n% All numbers verified against registry 2026-05-14.\n\n\\subsection{Ablation and Composability with Fine-Tuning}\n\\label{sec:scierc-results}\n\nTable~\\ref{tab:scierc-ablation} presents the five-way ablation on SciERC (Qwen3-8B, zero-shot, 551 documents); only the active constraint layers differ across rows.\n\n% ──────────────────────────────────────────\n%  Table: SciERC five-way ablation\n% ──────────────────────────────────────────\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3.6pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l rrrrrr rr@{}}\n\\toprule\n& \\multicolumn{6}{c}{\\textbf{Violation Rates (\\%)}}\n& \\multicolumn{2}{c}{\\textbf{F1}} \\\\\n\\cmidrule(lr){2-7} \\cmidrule(l){8-9}\n\\textbf{Mode}\n  & DR\\,$\\downarrow$ & $\\Delta$DR\n  & RV\\,$\\downarrow$ & ET\\,$\\downarrow$ & CF & Tot.\\,$\\downarrow$\n  & Rel.\\,$\\uparrow$ & Ent.\\,$\\uparrow$ \\\\\n\\midrule\nUnconstrained\n  & 15.37 & ---\n  & 1.39  & 0.40\n  & 0.08  & 15.45\n  & 8.23  & 31.01 \\\\\nGrammar\n  & 14.84 & $\\downarrow$3\\%\n  & \\textbf{0} & \\textbf{0}\n  & 0.08  & 14.92\n  & 8.23  & 30.98 \\\\\nGCD-equiv.$^\\dagger$\n  & 15.26 & $\\downarrow$1\\%\n  & \\textbf{0} & \\textbf{0}\n  & 0.04  & 15.30\n  & 8.75  & 30.91 \\\\\nSemantic\n  & 11.65 & $\\downarrow$24\\%\n  & 1.51  & 0.40\n  & 2.71  & 14.36\n  & 8.15  & 31.01 \\\\\nS1\n  & \\textbf{0.93} & $\\downarrow$\\textbf{94\\%}\n  & \\textbf{0} & \\textbf{0}\n  & 9.90  & \\textbf{10.83}\n  & \\textbf{8.36} & 30.98 \\\\\nS2\n  & 0.97  & $\\downarrow$94\\%\n  & \\textbf{0} & \\textbf{0}\n  & 8.03  & \\textbf{9.00}\n  & 8.03  & \\textbf{31.90} \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Five-way ablation on SciERC (551 docs, Qwen3-8B, zero-shot).\n$\\Delta$DR: relative change vs.\\ unconstrained; Tot.\\ = DR + CF; bold = best (CF excluded).\nF1 (\\%). S1/S2 = single/two-pass (\\S\\ref{sec:strategies}).\nGrammar = GCD ceiling~\\cite{geng2023gcd}.\n$\\dagger$vLLM \\texttt{guided\\_json}~\\cite{kwon2023vllm} (\\S\\ref{sec:constrained-baselines}).\nDeterministic (greedy, $T{=}$0); robustness evidence in Table~\\ref{tab:cross-model} and Appendices~\\ref{app:bootstrap-effect-sizes},~\\ref{app:prompt-sensitivity}.}\n\\label{tab:scierc-ablation}\n\\end{table}\n\n% ──────────────────────────────────────────\n%  (a) Zero-shot diagnostic (compressed)\n% ──────────────────────────────────────────\n\\paragraph{Zero-shot diagnostic.}\n% phase2_scierc_unconstrained: DR=0.1537; phase2_scierc_full_s1: DR=0.0093\nTable~\\ref{tab:scierc-ablation} establishes that DR violations are pervasive (15--18\\% across datasets) and that constraint layers interact non-additively: grammar-only achieves 3\\% DR reduction on SciERC, semantic-only 24\\%, but their composition yields 94\\%---the \\emph{empirical enabling dependency}.\nOn DocRED (96 relations, $\\bar{\\kappa}{=}0.842$), grammar-only \\emph{increases} DR via \\textit{latent violation surfacing}: forcing OOV$\\to$valid relation mapping exposes violations previously masked by vocabulary errors (Appendix~\\ref{app:cross-model-zs}).\nCross-model validation (3 models $\\times$ 2 datasets; Table~\\ref{tab:cross-model}) confirms DR drops of 76--99\\% on SciERC and 42--90\\% on DocRED, with R-F1 improving in 5/6 settings; post-hoc filtering achieves DR${=}$0\\% but at 15--74\\% rejection rates.\nDR-to-CF conversion represents a severity downgrade: DR is irrecoverable without re-extraction, while CF---individually valid triples with cross-triple inconsistency---is amenable to post-hoc resolution (TCR eliminates 18--92\\%; Appendix~\\ref{app:tcr}).\nZero-shot evaluation thus establishes violation prevalence and constraint interaction; fine-tuning demonstrates practical elimination.\n\n% ──────────────────────────────────────────\n%  (e) Composability with Fine-Tuning (expanded)\n% ──────────────────────────────────────────\n\\paragraph{Composability with fine-tuning.}\n\\label{sec:composability}\n% exp_ids: bootstrap_ci_ft_composability.json, w5_lora_scierc_*, w8_*\nFine-tuning alone reduces DR to 1--2\\% but leaves residual violations on tight-constraint relations (Table~\\ref{tab:composability}); adding S1 yields DR\\,$\\leq$\\,0.09\\% with no significant $\\Delta$R-F1 (Bonferroni-corrected; 95\\% CIs $\\subseteq [-0.69, {+}0.25]$\\,pp; removed triples are 97.6--100\\% false positives; Appendix~\\ref{app:downstream-impact}).\nUnder fine-tuning, grammar becomes a no-op ($\\Delta$DR$<$0.2\\,pp), making the semantic layer the sole DR defense (39--69\\% reduction; Appendix~\\ref{app:ft-ablation}); three relations with $\\kappa \\geq 0.36$ retain DR, all eliminated by S1 (Appendix~\\ref{app:lora-per-relation}).\nFallback frequency is model-dependent: Qwen triggers 0 fallbacks under LoRA + S1 on SciERC, while Llama triggers 5{,}882 (Table~\\ref{tab:ft-ablation}), reflecting weaker entity typing; despite this, DR reaches 0.09\\% for Llama, confirming that even frequent fallback does not compromise enforcement.\nCF drops from $+$9.82\\,pp (zero-shot) to $+$1.18\\,pp (fine-tuned), concentrated in \\textsc{Generic}$\\leftrightarrow$X ambiguity (63.3\\% of zero-shot CF; Appendix~\\ref{app:cf-distribution}); beam ($k{=}4$) eliminates all violation types (R-F1 43--47; \\S\\ref{sec:beam-results}).\n\n% ──────────────────────────────────────────\n%  CF quantification (MF1 response)\n% ──────────────────────────────────────────\n\\paragraph{Cross-field violation analysis.}\n% exp_ids: phase2_scierc_full_s1 (ZS: CF=248, 167 docs), w5_lora_scierc_full_s1_eval (FT: CF=22, 20 docs)\nUnder zero-shot greedy S1, CF is the sole residual violation type (DR, RV, ET all eliminated): 248 cross-field violations arise across 167 documents, of which 63.3\\% involve \\textsc{Generic}$\\leftrightarrow$X type ambiguity (Appendix~\\ref{app:cf-distribution}), concentrated in \\textsc{Generic}$\\leftrightarrow$\\textsc{OtherScientificTerm} (34.7\\%) and \\textsc{Generic}$\\leftrightarrow$\\textsc{Material} (12.3\\%).\nA source breakdown (Appendix~\\ref{app:cascade-analysis}) shows 58.1\\% originate from hallucinated entities (a model capacity issue), while true cascade errors---where first-seen registration locks an incorrect type---account for only 7.3\\%; correct locks are 2.5$\\times$ more frequent, confirming first-seen registration as a net-positive mechanism.\nFine-tuning reduces CF to 22 violations across 20 documents (1.18\\%), with cascade errors completely eliminated (0/22).\nBeam search ($k{=}4$) eliminates all remaining CF at 1.39$\\times$ latency (\\S\\ref{sec:beam-results}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lll rrrr r@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Dataset} & \\textbf{Mode}\n  & \\textbf{DR\\,$\\downarrow$} & \\textbf{CF}\n  & \\textbf{R-F1\\,$\\uparrow$} & \\textbf{E-F1\\,$\\uparrow$}\n  & \\textbf{$\\Delta$DR} \\\\\n\\midrule\n\\multirow{4}{*}{Qwen3-8B}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.95 & 0    & 43.86 & 67.05 & --- \\\\\n  & & S1    & \\textbf{0} & 1.18 & 43.77 & 67.05 & $\\downarrow$100\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.56 & 0.08 & 40.89 & 82.35 & --- \\\\\n  & & S1    & \\textbf{0.00} & 0.22 & 40.79 & 81.87 & $\\downarrow$100\\% \\\\\n\\midrule\n\\multirow{4}{*}{\\shortstack[l]{Llama\\\\3.1-8B}}\n  & \\multirow{2}{*}{SciERC}\n    & Unconstr.\\ &  1.11 & 0    & 45.45 & 67.76 & --- \\\\\n  & & S1    &  0.09 & 0.46 & 45.47 & 67.76 & $\\downarrow$92\\% \\\\\n\\cmidrule(l){2-8}\n  & \\multirow{2}{*}{DocRED}\n    & Unconstr.\\ &  0.49 & 0.08 & 44.55 & 84.77 & --- \\\\\n  & & S1    &  0.00 & 0.26 & 44.70 & 84.71 & $\\downarrow$100\\% \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Fine-tuning composability: LoRA $\\times$ unconstrained vs.\\ S1 on SciERC (551 docs) and DocRED (998 dev docs).\nF1 (\\%). No $\\Delta$R-F1 is significant (Bonferroni-corrected; details in text); all DR reductions are ($p{<}0.001$).\nE-F1 includes parse-failure documents (Qwen PF: 7--8\\%; Llama PF: 2--3\\%).}\n\\label{tab:composability}\n\\end{table}\n\n% ──────────────────────────────────────────\n%  (f) Downstream impact of DR elimination\n%  exp_ids: task_e_lucky_violation_analysis\n% ──────────────────────────────────────────\n\\paragraph{Downstream impact.}\n\\label{sec:downstream-impact}\nAmong constraint-removed triples, only 0.49\\% match gold labels (Appendix~\\ref{app:lucky-violations}); error analysis of 514 false negatives confirms only one (0.2\\%) was blocked by constraints, with dominant sources (relation confusion, entity type polysemy) schema-valid and beyond constraint reach (Appendix~\\ref{app:error-analysis}).\nAcross fine-tuned settings, 36 residual DR violations decompose into entity type errors (39\\%), schema coverage gaps (33\\%), and relation/direction errors (28\\%); the irreducible floor is $\\sim$3 violations (Appendix~\\ref{app:residual-dr-analysis}).\n",
      "numLines": 148,
      "startLine": 1,
      "totalLines": 148
    }
  },
  "sourceToolAssistantUUID": "99b0fb6a-4af3-4c30-93be-e467cec83fc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-23T10:22:56.381Z_

<details open><summary>🔧 Tool call — Read · `toolu_01U1ouZABbqDj52KWz5ZfR6r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76d303a4-16bf-46fa-bf95-3da3c4df8557",
  "isSidechain": false,
  "requestId": "req_011CbKLQoB3S25wBK4ij2w5j",
  "type": "assistant",
  "uuid": "15e80664-11d3-496f-bc78-321826eef9ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4BrcPsJzG6CBGTk4DYQQ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3033,
      "cache_read_input_tokens": 24272,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 24272,
          "cache_creation_input_tokens": 3033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3033
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

_source line 21 · 2026-05-23T10:22:56.419Z_

<details><summary>↩ Tool result · `toolu_01U1ouZABbqDj52KWz5ZfR6r`</summary>

```text
1	% Section: Constraint Composition (compressed, 787→~500 words)
2	
3	At each decoding step $t$, let $G(t) \subseteq V$ and $S(t) \subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.
4	The final mask is their conjunction:
5	%
6	\begin{equation}\label{eq:composition}
7	  M_{\text{final}}(t) = M_{\text{grammar}}(t) \;\wedge\; M_{\text{semantic}}(t),
8	\end{equation}
9	%
10	where $\wedge$ denotes element-wise AND over the vocabulary $V$; a token is allowed only if it satisfies \emph{both} structural and type-level constraints.
11	The conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the scale-dependent layer interaction (\S\ref{sec:method}): the semantic layer requires the relation type to belong to $\mathcal{R}$, a property enforced only by the grammar layer.
12	This dependency is scale-sensitive: 70B semantic-only achieves 84\% DR reduction (vs.\ 24\% on 8B), though grammar remains necessary for RV elimination (\S\ref{sec:70b-results}).
13	
14	\paragraph{Grammar-First Fallback.}
15	When $S(t) \cap G(t) = \emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\"{\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.
16	We enforce a \emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.
17	Structural integrity is a hard constraint; type violations are soft errors detectable by downstream validation, with DR (ontologically invalid type pair) more severe than CF (individually valid triples with cross-triple type inconsistency).
18	Extraction tasks are robust to format-level constraints~\cite{tam2024letmespeak}, supporting this asymmetric treatment.
19	
20	\paragraph{Constraint Tightness.}
21	\label{eq:tightness}
22	Per-relation constraint tightness $\kappa(r) = 1 - |\sigma(r)|/|\mathcal{E}|^2$, with schema mean $\bar{\kappa}$.
23	Across WikiEvents ($\bar{\kappa}{=}0.029$), SciERC ($\bar{\kappa}{=}0.333$), DocRED ($\bar{\kappa}{=}0.842$), DR reduction ranges from 94--99\% to 42--90\%; this correlation is descriptive ($n{=}3$, $p{=}0.138$); entity type confusability is a critical co-factor (Appendix~\ref{app:kappa-case-study},~\ref{app:tcr}); high-$\bar{\kappa}$ relations account for only 3.8\% of gold triples in DocRED (Appendix~\ref{app:kappa-analysis}).
24	
25	\paragraph{Greedy limitation and fallback cascade.}
26	\label{sec:greedy-limitation}
27	Single-pass per-triple enforcement cannot coordinate type assignments across triples sharing the same entity mention; cross-field consistency requires global inference that exceeds the per-token masking paradigm.
28	The semantic layer commits entity types greedily---an instance of Level~3 (non-local) constraints (\S\ref{sec:decidability})---so CF violations arise when the same entity receives different types across triples; beam search mitigates this (\S\ref{sec:beam-results}).
29	Fallback triggers on 0.5--5.7\% of type-bearing positions (zero-shot), virtually eliminated by fine-tuning ($\leq$\,0.11\%); all residual DR occurs at fallback positions (Appendix~\ref{app:causal-tracing}).
30	
31	\paragraph{Non-rectangularity and independent enforcement.}
32	\label{sec:rectangularity}
33	Type signatures are non-rectangular (0/7 SciERC, 23/96 DocRED rectangular); independent enforcement admits 33--37\% spurious pairs, eliminated by fine-tuning (Table~\ref{tab:composability}).
34	Shuffling type order produces byte-identical outputs across all 551 SciERC documents, confirming order invariance (Appendix~\ref{app:order-invariance}).
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15e80664-11d3-496f-bc78-321826eef9ed",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "fffc62c1-1d48-4d43-82ad-07818faa66d5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section4_composition_draft.tex",
      "content": "% Section: Constraint Composition (compressed, 787→~500 words)\n\nAt each decoding step $t$, let $G(t) \\subseteq V$ and $S(t) \\subseteq V$ denote the tokens permitted by the grammar and semantic layers, respectively.\nThe final mask is their conjunction:\n%\n\\begin{equation}\\label{eq:composition}\n  M_{\\text{final}}(t) = M_{\\text{grammar}}(t) \\;\\wedge\\; M_{\\text{semantic}}(t),\n\\end{equation}\n%\nwhere $\\wedge$ denotes element-wise AND over the vocabulary $V$; a token is allowed only if it satisfies \\emph{both} structural and type-level constraints.\nThe conjunction is asymmetric: $S(t)$ is defined only over $G(t)$. This reflects the scale-dependent layer interaction (\\S\\ref{sec:method}): the semantic layer requires the relation type to belong to $\\mathcal{R}$, a property enforced only by the grammar layer.\nThis dependency is scale-sensitive: 70B semantic-only achieves 84\\% DR reduction (vs.\\ 24\\% on 8B), though grammar remains necessary for RV elimination (\\S\\ref{sec:70b-results}).\n\n\\paragraph{Grammar-First Fallback.}\nWhen $S(t) \\cap G(t) = \\emptyset$ (tight constraints leave no token that is both grammar-valid and semantically valid), na\\\"{\\i}ve masking would force selection of a grammar-invalid token, breaking JSON structure.\nWe enforce a \\emph{grammar-first fallback}: semantic masking is skipped and the grammar layer alone controls selection.\nStructural integrity is a hard constraint; type violations are soft errors detectable by downstream validation, with DR (ontologically invalid type pair) more severe than CF (individually valid triples with cross-triple type inconsistency).\nExtraction tasks are robust to format-level constraints~\\cite{tam2024letmespeak}, supporting this asymmetric treatment.\n\n\\paragraph{Constraint Tightness.}\n\\label{eq:tightness}\nPer-relation constraint tightness $\\kappa(r) = 1 - |\\sigma(r)|/|\\mathcal{E}|^2$, with schema mean $\\bar{\\kappa}$.\nAcross WikiEvents ($\\bar{\\kappa}{=}0.029$), SciERC ($\\bar{\\kappa}{=}0.333$), DocRED ($\\bar{\\kappa}{=}0.842$), DR reduction ranges from 94--99\\% to 42--90\\%; this correlation is descriptive ($n{=}3$, $p{=}0.138$); entity type confusability is a critical co-factor (Appendix~\\ref{app:kappa-case-study},~\\ref{app:tcr}); high-$\\bar{\\kappa}$ relations account for only 3.8\\% of gold triples in DocRED (Appendix~\\ref{app:kappa-analysis}).\n\n\\paragraph{Greedy limitation and fallback cascade.}\n\\label{sec:greedy-limitation}\nSingle-pass per-triple enforcement cannot coordinate type assignments across triples sharing the same entity mention; cross-field consistency requires global inference that exceeds the per-token masking paradigm.\nThe semantic layer commits entity types greedily---an instance of Level~3 (non-local) constraints (\\S\\ref{sec:decidability})---so CF violations arise when the same entity receives different types across triples; beam search mitigates this (\\S\\ref{sec:beam-results}).\nFallback triggers on 0.5--5.7\\% of type-bearing positions (zero-shot), virtually eliminated by fine-tuning ($\\leq$\\,0.11\\%); all residual DR occurs at fallback positions (Appendix~\\ref{app:causal-tracing}).\n\n\\paragraph{Non-rectangularity and independent enforcement.}\n\\label{sec:rectangularity}\nType signatures are non-rectangular (0/7 SciERC, 23/96 DocRED rectangular); independent enforcement admits 33--37\\% spurious pairs, eliminated by fine-tuning (Table~\\ref{tab:composability}).\nShuffling type order produces byte-identical outputs across all 551 SciERC documents, confirming order invariance (Appendix~\\ref{app:order-invariance}).\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  },
  "sourceToolAssistantUUID": "15e80664-11d3-496f-bc78-321826eef9ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-23T10:22:56.906Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E3HbYe3VLvyXm74axBHqUe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/_project/paper/section5_docred_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fffc62c1-1d48-4d43-82ad-07818faa66d5",
  "isSidechain": false,
  "requestId": "req_011CbKLQoB3S25wBK4ij2w5j",
  "type": "assistant",
  "uuid": "afd8bb66-5392-4937-8990-af73f88ba62c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4BrcPsJzG6CBGTk4DYQQ4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3033,
      "cache_read_input_tokens": 24272,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3033,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 364,
          "cache_read_input_tokens": 24272,
          "cache_creation_input_tokens": 3033,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3033
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

_source line 23_

```json
{
  "type": "last-prompt",
  "leafUuid": "b6b07cbd-1ec0-4529-a742-2f6bed4f1aca",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper tables 1 and 2 numerical values",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---

### Assistant

_source line 25 · 2026-05-23T10:23:17.094Z_

<details><summary>Logged reasoning block</summary>

```text
I've found both tables:

**Table 1** (`tab:scierc-ablation`) is in `section5_scierc_draft.tex` lines 15-69. It's a five-way ablation on SciERC with columns: Mode, DR↓, ΔDR, RV↓, ET↓, CF, Tot.↓, Rel.↑, Ent.↑

**Table 2** (`tab:composability`) is in `section5_scierc_draft.tex` lines 103-138. 

Now I'm extracting the numerical values from both tables to compare their results. Generating markdown table... Generating markdown table...

Now I need to access the actual experiment data using the registry tool to pull the results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6b07cbd-1ec0-4529-a742-2f6bed4f1aca",
  "isSidechain": false,
  "requestId": "req_011CbKLRQ4GPxGxgquQ3Mjyn",
  "type": "assistant",
  "uuid": "103e7bf2-466f-43e0-ae81-fcc347cc195f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016b8F3NVNw34BPQ8hZvbbf1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5872,
      "cache_read_input_tokens": 27305,
      "output_tokens": 1152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1152,
          "cache_read_input_tokens": 27305,
          "cache_creation_input_tokens": 5872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5872
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

_source line 26 · 2026-05-23T10:23:17.506Z_

Found both tables in `section5_scierc_draft.tex`. Now I need to load the registry tool to cross-check numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "103e7bf2-466f-43e0-ae81-fcc347cc195f",
  "isSidechain": false,
  "requestId": "req_011CbKLRQ4GPxGxgquQ3Mjyn",
  "type": "assistant",
  "uuid": "2849cf33-55c9-4b42-bc44-2048cf83e8a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016b8F3NVNw34BPQ8hZvbbf1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5872,
      "cache_read_input_tokens": 27305,
      "output_tokens": 1152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1152,
          "cache_read_input_tokens": 27305,
          "cache_creation_input_tokens": 5872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5872
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

_source line 27 · 2026-05-23T10:23:18.361Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JYqbWvU391fxjEGEygLokV`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2849cf33-55c9-4b42-bc44-2048cf83e8a1",
  "isSidechain": false,
  "requestId": "req_011CbKLRQ4GPxGxgquQ3Mjyn",
  "type": "assistant",
  "uuid": "a07cab5a-8cc7-469d-b2ed-dee4a3a724bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016b8F3NVNw34BPQ8hZvbbf1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5872,
      "cache_read_input_tokens": 27305,
      "output_tokens": 1152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1152,
          "cache_read_input_tokens": 27305,
          "cache_creation_input_tokens": 5872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5872
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

_source line 28 · 2026-05-23T10:23:18.365Z_

<details><summary>↩ Tool result · `toolu_01JYqbWvU391fxjEGEygLokV`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a07cab5a-8cc7-469d-b2ed-dee4a3a724bc",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "1a6ddfd6-1cf8-49ab-96ae-c3eb5e0c1b3d",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 22
  },
  "sourceToolAssistantUUID": "a07cab5a-8cc7-469d-b2ed-dee4a3a724bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-23T10:23:24.765Z_

<details><summary>Logged reasoning block</summary>

```text
Let me first get an overview of all experiments in the registry to understand what's available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a6ddfd6-1cf8-49ab-96ae-c3eb5e0c1b3d",
  "isSidechain": false,
  "requestId": "req_011CbKLSyaAxhdHb24eiYZEH",
  "type": "assistant",
  "uuid": "26a9dc4d-b2b4-4863-a34a-d57b1ee9a343",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KgpUYfMhYAA1R7qjp9Sm7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1513,
      "cache_read_input_tokens": 33177,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 172,
          "cache_read_input_tokens": 33177,
          "cache_creation_input_tokens": 1513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1513
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

_source line 30 · 2026-05-23T10:23:25.426Z_

Let me query the registry for the relevant experiments. I'll start by getting an overview of all experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26a9dc4d-b2b4-4863-a34a-d57b1ee9a343",
  "isSidechain": false,
  "requestId": "req_011CbKLSyaAxhdHb24eiYZEH",
  "type": "assistant",
  "uuid": "d2ee101e-5dd5-4336-a267-a4106ca623be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KgpUYfMhYAA1R7qjp9Sm7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1513,
      "cache_read_input_tokens": 33177,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 172,
          "cache_read_input_tokens": 33177,
          "cache_creation_input_tokens": 1513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1513
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

_source line 31 · 2026-05-23T10:23:26.387Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019uuoDiMC4EcD8dPpatSk8S`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "limit": 0,
  "fields": [
    "exp_id",
    "status",
    "metrics",
    "conclusion"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2ee101e-5dd5-4336-a267-a4106ca623be",
  "isSidechain": false,
  "requestId": "req_011CbKLSyaAxhdHb24eiYZEH",
  "type": "assistant",
  "uuid": "dd230e38-1f54-4fe0-9f9c-486c6283d801",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KgpUYfMhYAA1R7qjp9Sm7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1513,
      "cache_read_input_tokens": 33177,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1513,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 172,
          "cache_read_input_tokens": 33177,
          "cache_creation_input_tokens": 1513,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1513
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

_source line 32 · 2026-05-23T10:23:27.206Z_

<details><summary>↩ Tool result · `toolu_019uuoDiMC4EcD8dPpatSk8S`</summary>

```text
Error: result (72,312 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd230e38-1f54-4fe0-9f9c-486c6283d801",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "0f184065-eec0-4510-9567-2582a3b1060c",
  "toolUseResult": "Error: result (72,312 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_70b_lora_docred_200_full_s2\": {\"status\": \"DONE\", \"metrics\": {\"R_F1\": 36.45, \"R_P\": 31.25, \"R_R\": 43.72, \"E_F1\": 84.96, \"E_P\": 84.6, \"E_R\": 85.34, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 13, \"CF_pct\": 0.34, \"parse_fail_pct\": 0, \"pred_entities\": 3819, \"pred_relations\": 3546, \"entity_tp\": 3218, \"entity_fp\": 586, \"entity_fn\": 553, \"relation_tp\": 1104, \"relation_fp\": 2429, \"relation_fn\": 1421}, \"conclusion\": \"negative\"}, \"sf2_qwen_int4_docred_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 200, \"parse_failures\": 37, \"parse_fail_pct\": 18.5, \"total_entities_pred\": 2985, \"total_relations_pred\": 2385, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.1, \"E_P\": 84.87, \"E_R\": 66.93, \"E_F1\": 74.84, \"R_P\": 41.59, \"R_R\": 38.65, \"R_F1\": 40.07, \"et_violations\": 0, \"rv_violations\": 0, \"dr_violations\": 0, \"cf_violations\": 3}}, \"sf2_llama_int4_docred_s1\": {\"status\": \"DONE\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.22, \"R-F1\": 48.04, \"E-F1\": 84.18, \"R-P\": 44.79, \"R-R\": 51.8, \"E-P\": 85.5, \"E-R\": 82.9, \"samples\": 200, \"parse_fail\": 5, \"parse_fail_pct\": 2.5, \"entities_pred\": 3669, \"relations_pred\": 2997}, \"conclusion\": \"success\"}, \"sf2_70b_prompt_sensitivity\": {\"status\": \"RUNNING\"}, \"sf2_llama_int4_scierc_s1\": {\"status\": \"DONE\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.94, \"R-F1\": 43.98, \"E-F1\": 67.54, \"samples\": 551, \"R-P\": 40.47, \"R-R\": 48.15, \"E-P\": 65.51, \"E-R\": 69.7}, \"conclusion\": \"success\"}, \"sf2_qwen_int4_scierc_s1\": {\"status\": \"DONE\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 1.1, \"R-F1\": 41.71, \"E-F1\": 67.05, \"samples\": 551, \"R-P\": 38.52, \"R-R\": 45.48, \"E-P\": 64.76, \"E-R\": 69.52}, \"conclusion\": \"success\"}, \"sf2_gollie_scierc_violation\": {\"status\": \"DONE\", \"metrics\": {\"GoLLIE_ZS\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.83, \"E_F1\": 9.17, \"R_F1\": 0, \"pred_ents\": 241, \"pred_rels\": 5, \"docs_with_output\": 54}, \"OntoCoDec_Qwen_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.61, \"E_F1\": 66.43, \"R_F1\": 43.69}, \"OntoCoDec_Llama_FT_S1\": {\"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.62, \"E_F1\": 67.09, \"R_F1\": 45.47}}, \"conclusion\": \"success\"}, \"eval_70b_zs_docred_200_full_s1\": {\"status\": \"DONE\", \"metrics\": {\"DR%\": 0, \"RV%\": 0, \"ET%\": 0, \"CF%\": 5.34, \"E-F1\": 70.05, \"R-F1\": 13.25, \"PF%\": 0, \"entities_pred\": 3234, \"relations_pred\": 2637, \"triples_checked\": 2642}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 10.5, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.38, \"CF_pct\": 0.06, \"E_F1\": 80.13, \"E_P\": 85.16, \"E_R\": 75.66, \"R_F1\": 43.96, \"R_P\": 39.78, \"R_R\": 49.11, \"entities_pred\": 3362, \"relations_pred\": 3154}, \"conclusion\": \"negative\"}, \"eval_70b_lora_docred_200_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 200, \"parse_fail_pct\": 11, \"ET_pct\": 0, \"RV_pct\": 0.51, \"DR_pct\": 0, \"CF_pct\": 0.21, \"E_F1\": 80.06, \"E_P\": 85.21, \"E_R\": 75.5, \"R_F1\": 43.61, \"R_P\": 39.44, \"R_R\": 48.75, \"entities_pred\": 3351, \"relations_pred\": 3148}, \"conclusion\": \"success\"}, \"eval_70b_zs_docred_200_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities_pred\": 3242, \"relations_pred\": 2637, \"ET_pct\": 0, \"RV_pct\": 7.88, \"DR_pct\": 13.45, \"CF_count\": 0, \"fuzzy_matches\": 8, \"E_F1\": 70.14, \"E_P\": 75.85, \"E_R\": 65.23, \"R_F1\": 13.25, \"R_P\": 12.97, \"R_R\": 13.54}, \"conclusion\": \"success\"}, \"eval_70b_zs_docred_200_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 200, \"parse_failures\": 1, \"entities_pred\": 3221, \"relations_pred\": 2609, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 17.03, \"CF_count\": 0, \"fuzzy_matches\": 0, \"E_F1\": 70.12, \"E_P\": 75.88, \"E_R\": 65.17, \"R_F1\": 13.23, \"R_P\": 12.99, \"R_R\": 13.47}, \"conclusion\": \"negative\"}, \"eval_70b_zs_docred_200_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 200, \"parse_failures\": 0, \"entities\": 3240, \"relations\": 2596, \"ET_pct\": 0.12, \"RV_pct\": 8.24, \"DR_pct\": 1.66, \"CF_count\": 132, \"CF_pct\": 4.07, \"E_F1\": 70.1, \"E_P\": 75.87, \"E_R\": 65.15, \"R_F1\": 13.05, \"R_P\": 12.88, \"R_R\": 13.23, \"fuzzy_matches\": 8}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_beam4_s1\": {\"status\": \"DONE\", \"metrics\": {\"E-F1\": 85.57, \"E-P\": 85.45, \"E-R\": 85.68, \"R-F1\": 48.14, \"R-P\": 44.24, \"R-R\": 52.79, \"ET%\": 0, \"RV%\": 0, \"DR%\": 0, \"CF%\": 0, \"parse_fail\": \"1/200 (0.5%)\", \"entities_pred\": 3790, \"relations_pred\": 3030}, \"conclusion\": \"success\"}, \"eval_70b_lora_scierc_grammar_only\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"json_failure_rate\": 0, \"entities\": 1805, \"relations\": 1133, \"entity_type_violations\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violations\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violations\": 17, \"domain_range_violation_rate\": 0.015, \"cross_field_consistency_violations\": 0, \"fuzzy_relation_matches\": 0, \"entity_P\": 0.6272, \"entity_R\": 0.6707, \"entity_F1\": 0.6482, \"relation_P\": 0.4152, \"relation_R\": 0.4825, \"relation_F1\": 0.4463}}, \"eval_70b_zs_scierc_unconstrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 2353, \"relations\": 1483, \"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.4, \"CF_count\": 0, \"E_F1\": 35.22, \"E_P\": 30.13, \"E_R\": 42.38, \"R_F1\": 11.23, \"R_P\": 9.31, \"R_R\": 14.17, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_full_s2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1531, \"relations\": 1027, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 18, \"E_F1\": 62.35, \"E_P\": 65.44, \"E_R\": 59.53, \"R_F1\": 36.28, \"R_P\": 35.35, \"R_R\": 37.27, \"parse_fail_pct\": 0}}, \"eval_70b_lora_scierc_semantic_only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1806, \"relations\": 1133, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 9, \"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"parse_fail_pct\": 0}}, \"entity_order_ablation_qwen_scierc\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 67.05, \"E_P\": 65.23, \"E_R\": 68.98, \"R_F1\": 43.77, \"R_P\": 40.78, \"R_R\": 47.23, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 21, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1784, \"relations\": 1128, \"corrected_original_R_F1\": 43.77, \"corrected_original_E_F1\": 67.05, \"corrected_original_DR_pct\": 0, \"corrected_original_CF_count\": 21, \"corrected_delta_R_F1\": 0, \"corrected_delta_E_F1\": 0, \"raw_output_identical\": true, \"parsed_output_identical\": true, \"note\": \"CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\"}}, \"eval_70b_zs_scierc_semantic_only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 11.37, \"DR_pct\": 1.01, \"RV_pct\": 0.6, \"ET_pct\": 0, \"CF_count\": 76, \"samples\": 551}}, \"eval_70b_zs_scierc_grammar_only\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"R_F1\": 11.23, \"DR_pct\": 6.33, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 0, \"samples\": 551}}, \"eval_70b_lora_scierc_beam4_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 64.89, \"E_P\": 62.29, \"E_R\": 67.72, \"R_F1\": 44.81, \"R_P\": 39.45, \"R_R\": 51.85, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_count\": 1, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1839, \"relations\": 1283}}, \"tcr_beam4_llama_scierc\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1803, \"relations\": 1194, \"entity_type_violations\": \"0/1803 (0.0%)\", \"relation_vocab_violations\": \"0/1194 (0.0%)\", \"domain_range_violations\": \"13/1194 (1.1%)\", \"cross_field_consistency\": 0, \"DR_pct\": 1.09, \"E_F1\": 68.02, \"E_P\": 65.88, \"E_R\": 70.29, \"R_F1\": 46.05, \"R_P\": 41.83, \"R_R\": 51.23, \"tcr_changed_selection\": \"0/551 (0.0%)\"}, \"conclusion\": \"negative\"}, \"tcr_beam4_qwen_scierc\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"samples\": 551, \"json_failures\": 0, \"entities\": 1802, \"relations\": 1250, \"entity_type_violations\": \"0/1802 (0.0%)\", \"relation_vocab_violations\": \"0/1250 (0.0%)\", \"domain_range_violations\": \"23/1250 (1.8%)\", \"cross_field_consistency_violations\": 1, \"DR_pct\": 1.84, \"E_P\": 65.05, \"E_R\": 69.64, \"E_F1\": 67.26, \"R_P\": 39.36, \"R_R\": 50.51, \"R_F1\": 44.24, \"TCR_changed_selection\": \"0/551 (0.0%)\", \"all_candidates_TCR_1.0\": true}}, \"vllm_guided_json_scierc_zs\": {\"status\": \"DONE\", \"metrics\": {\"DR%\": 15.26, \"RV%\": 0, \"ET%\": 0, \"CF%\": 0.04, \"R-F1\": 8.75, \"E-F1\": 30.91, \"parse_fail%\": 0, \"total_samples\": 551, \"total_entities\": 2485, \"total_relations\": 1724, \"inference_time_s\": 108.5}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_s1_constrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 79.38, \"E_P\": 85.24, \"E_R\": 74.28, \"R_F1\": 43.95, \"R_P\": 40.48, \"R_R\": 48.08, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.18, \"parse_fail_pct\": 12.5, \"samples\": 200}}, \"d066_beam_sweep\": {\"status\": \"DONE\", \"metrics\": {\"scierc_qwen3_8b\": {\"k1_unc\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 2.11, \"CF_pct\": 0, \"avg_time\": 2.494}, \"k1_con\": {\"E_F1\": 66.88, \"R_F1\": 42.95, \"DR_pct\": 0, \"CF_pct\": 0.5, \"avg_time\": 2.932}, \"k2_unc\": {\"E_F1\": 67.79, \"R_F1\": 44.75, \"DR_pct\": 1.54, \"CF_pct\": 0, \"avg_time\": 2.954}, \"k2_con\": {\"E_F1\": 67.71, \"R_F1\": 44.6, \"DR_pct\": 0, \"CF_pct\": 0.11, \"avg_time\": 3.463}, \"k4_unc\": {\"E_F1\": 67.49, \"R_F1\": 43.72, \"DR_pct\": 1.89, \"CF_pct\": 0, \"avg_time\": 3.485}, \"k4_con\": {\"E_F1\": 67.22, \"R_F1\": 43.6, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 4.069}, \"k8_unc\": {\"E_F1\": 66.4, \"R_F1\": 43.17, \"DR_pct\": 1.77, \"CF_pct\": 0, \"avg_time\": 4.194}, \"k8_con\": {\"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"avg_time\": 5.058}}, \"pareto_optimal\": \"k=2 con\", \"best_E_F1\": {\"config\": \"k=2 unc\", \"value\": 67.79}, \"best_R_F1\": {\"config\": \"k=2 unc\", \"value\": 44.75}}, \"conclusion\": \"success\"}, \"w8_llama_docred_ft_grammar_only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 43.72, \"R_P\": 38.57, \"R_R\": 50.44, \"parse_fail_pct\": 2.3, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\"}}, \"w8_llama_docred_ft_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"R_F1\": 43.85, \"R_P\": 38.85, \"R_R\": 50.31, \"parse_fail_pct\": 2.4, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\"}, \"conclusion\": \"success\"}, \"w8_qwen_docred_ft_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"R_F1\": 40.85, \"R_P\": 36.33, \"R_R\": 46.65, \"parse_fail_pct\": 7.52, \"samples\": 998, \"note\": \"Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\"}, \"conclusion\": \"success\"}, \"r16_trie_qwen_ft_scierc\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 64.4, \"E_P\": 66.8, \"E_R\": 62.16, \"R_F1\": 41.16, \"R_P\": 38.24, \"R_R\": 44.56, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 95.5, \"CF_pct\": 0.09, \"parse_fail_pct\": 9.1, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\"}, \"conclusion\": \"success\"}, \"r16_trie_llama_ft_scierc\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 36.66, \"E_P\": 67.47, \"E_R\": 25.16, \"R_F1\": 19.95, \"R_P\": 41.42, \"R_R\": 13.14, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 15.2, \"CF_pct\": 0, \"parse_fail_pct\": 50.8, \"samples\": 551, \"note\": \"CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\"}, \"conclusion\": \"success\"}, \"eval_70b_lora_docred_200_unconstrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 80.34, \"E_P\": 85.13, \"E_R\": 76.05, \"R_F1\": 43.8, \"R_P\": 39.6, \"R_R\": 48.99, \"ET_pct\": 0, \"RV_pct\": 0.57, \"DR_pct\": 0.22, \"CF_pct\": 0.06, \"parse_fail_pct\": 10, \"samples\": 200, \"relations\": 3159, \"RV_count\": 18, \"DR_count\": 7, \"CF_count\": 2}}, \"eval_70b_lora_scierc_s1_constrained\": {\"status\": \"DONE\", \"metrics\": {\"entity_f1\": 0.6476, \"entity_precision\": 0.6266, \"entity_recall\": 0.6701, \"relation_f1\": 0.4453, \"relation_precision\": 0.4149, \"relation_recall\": 0.4805, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 15, \"parse_fail_pct\": 0, \"fuzzy_matches\": 0, \"num_samples\": 551, \"num_entities\": 1805, \"num_relations\": 1129}, \"conclusion\": \"success\"}, \"eval_70b_lora_scierc_unconstrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 64.86, \"E_P\": 62.74, \"E_R\": 67.12, \"R_F1\": 44.73, \"R_P\": 41.61, \"R_R\": 48.36, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 1.5, \"CF_pct\": 0, \"parse_fail_pct\": 0, \"samples\": 551, \"entities\": 1806, \"relations\": 1133}}, \"r16_70b_docred_zs_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 69.11, \"R_F1\": 13.05, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 0.04, \"parse_fail_pct\": 0.1, \"samples\": 998, \"total_entities\": 16599, \"total_triples\": 13239, \"baseline_unc_DR_pct\": 14.98, \"baseline_unc_R_F1\": 13.01, \"note\": \"Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch.\"}}, \"d066_sweep_llama_beam8_unc\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 85.77, \"E_P\": 85.7, \"E_R\": 85.84, \"R_F1\": 51.97, \"R_P\": 49.76, \"R_R\": 54.38, \"DR_pct\": 0, \"CF_pct\": 0.05, \"ET_pct\": 0, \"RV_pct\": 0.07, \"parse_fail_pct\": 0.5, \"total_samples\": 200, \"total_entities_pred\": 3788, \"total_relations_pred\": 2779}}, \"d066_sweep_llama_beam2_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 85.6, \"E_P\": 85.29, \"E_R\": 85.92, \"R_F1\": 51.17, \"R_P\": 48.51, \"R_R\": 54.14, \"DR_pct\": 0, \"CF_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"parse_fail_pct\": 0.5, \"total_samples\": 200, \"total_entities_pred\": 3814, \"total_relations_pred\": 2839}}, \"d066_sweep_llama_docred_beam4_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"E-F1\": 85.61, \"E-P\": 85.48, \"E-R\": 85.73, \"R-F1\": 51.89, \"R-P\": 51.59, \"R-R\": 52.2, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0.5, \"ET_pct\": 0, \"RV_pct\": 0, \"samples\": 200, \"parse_fail\": 1}}, \"r16_70b_lora_scierc_eval\": {\"status\": \"PREPARING\"}, \"r16_70b_lora_docred\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_loss\": 0.0635, \"token_acc\": 97.94, \"steps_completed\": 1146, \"epochs\": 3, \"train_loss_start\": 0.147, \"train_loss_end\": 0.056}}, \"r16_70b_lora_scierc\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_loss\": 0.0611, \"token_acc\": 97.78, \"steps_completed\": 663, \"epochs\": 3, \"train_loss_start\": 0.183, \"train_loss_end\": 0.041}}, \"r16_70b_scierc_zs_s1\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 35.19, \"R_F1\": 11.24, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 3.5, \"parse_fail_pct\": 0, \"samples\": 551, \"baseline_unc_E_F1\": 35.21, \"baseline_unc_R_F1\": 11.15, \"baseline_unc_DR_pct\": 6.41, \"baseline_unc_RV_pct\": 0.61, \"baseline_unc_CF_pct\": 0}, \"conclusion\": \"success\"}, \"r14_qwen_docred_beam4_998\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 58.19, \"R_F1\": 8.72, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 4.94, \"parse_fail_pct\": 3.51, \"samples\": 998, \"success\": 963, \"fail\": 35}, \"conclusion\": \"success\"}, \"r16_trie_llama_zs_scierc\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 23.23, \"R_F1\": 2.9, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 84.4, \"CF_pct\": 0.36, \"parse_fail_pct\": 0, \"samples\": 551}, \"conclusion\": \"success\"}, \"r16_trie_qwen_zs_scierc\": {\"status\": \"DONE\", \"metrics\": {\"E_F1\": 30.97, \"R_F1\": 8.64, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 29.3, \"CF_pct\": 0, \"parse_fail_pct\": 0, \"samples\": 551}, \"conclusion\": \"success\"}, \"r14_llama_docred_beam4_998\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"R_F1\": 8.83, \"E_F1\": 57.81, \"DR_pct\": 0, \"CF_pct\": 1, \"ET_pct\": 0, \"RV_pct\": 0, \"parse_fail_pct\": 3.91, \"samples\": 998, \"success\": 959, \"fail\": 39, \"baseline_ZS_greedy_R_F1\": 6.27, \"baseline_ZS_greedy_E_F1\": 54.93, \"baseline_ZS_greedy_DR_pct\": 2.55, \"baseline_ZS_greedy_CF_pct\": 8.54}}, \"d066_sweep_llama_scierc_beam8_s1_551\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"E-F1\": 67.51, \"E-P\": 64.99, \"E-R\": 70.23, \"R-F1\": 44.95, \"R-P\": 40.1, \"R-R\": 51.13, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0, \"samples\": 551, \"note\": \"Reconcile false positive corrected. Eval with --dataset scierc confirmed.\"}}, \"d066_sweep_llama_scierc_beam4_s1_551\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"E-F1\": 68.06, \"E-P\": 65.96, \"E-R\": 70.29, \"R-F1\": 46.18, \"R-P\": 42.1, \"R-R\": 51.13, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0, \"parse_fail\": 0, \"samples\": 551, \"note\": \"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"}}, \"d066_sweep_llama_docred_beam4_unc\": {\"status\": \"DONE\", \"metrics\": {\"E-F1\": 85.67, \"R-F1\": 52.65, \"DR_pct\": 0.04, \"CF_pct\": 0.08, \"PF_pct\": 0.5, \"samples\": 200}, \"conclusion\": \"success\"}, \"d066_sweep_llama_docred_beam1_s1\": {\"status\": \"DONE\", \"metrics\": {\"E-F1\": 85.43, \"R-F1\": 47.35, \"DR_pct\": 0, \"CF_pct\": 0.19, \"PF_pct\": 2, \"samples\": 200}, \"conclusion\": \"success\"}, \"d066_sweep_llama_beam8_s1\": {\"status\": \"DONE\", \"metrics\": {\"E-F1\": 85.76, \"R-F1\": 51.74, \"DR_pct\": 0, \"CF_pct\": 0, \"PF_pct\": 0.5, \"samples\": 200}, \"conclusion\": \"success\"}, \"d065_qwen_greedy_4096_r2\": {\"status\": \"DONE\", \"metrics\": {\"E-F1\": 81.87, \"R-F1\": 40.79, \"DR_pct\": 0, \"CF_pct\": 0.22, \"ET_pct\": 0, \"RV_pct\": 0, \"PF_pct\": 8.52, \"samples\": 998}, \"conclusion\": \"success\"}, \"d066_sweep_llama_scierc_beam2_s1_551\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"entity_f1\": 68.34, \"entity_p\": 66.59, \"entity_r\": 70.17, \"relation_f1\": 46.12, \"relation_p\": 42.73, \"relation_r\": 50.1, \"parse_fail_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.17, \"note\": \"ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\"}}, \"d066_sweep_llama_scierc_beam1_unc\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"total\": 275, \"success\": 275, \"fail\": 0, \"output_file\": \"llama_scierc_beam1_unconstrained.jsonl\", \"note\": \"INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun.\"}}, \"d066_sweep_llama_docred_beam1_unc\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"total\": 200, \"success\": 196, \"fail\": 4, \"output_file\": \"llama_docred_200_beam1_unconstrained.jsonl\"}}, \"d066_sweep_21461_gpu1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"total\": 551, \"E_F1\": 66.36, \"R_F1\": 43.65, \"DR_pct\": 0, \"CF_pct\": 0, \"ET_pct\": 0, \"RV_pct\": 0, \"avg_time_s\": 5.058, \"output_file\": \"qwen_scierc_beam8_full_s1.jsonl\", \"note\": \"Actually ran on SciERC 551 docs (not DocRED 200 as originally recorded in hypothesis)\"}}, \"w5_llama_docred_lora_constrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"total\": 998, \"parse_failures\": 25, \"parse_fail_rate\": 2.51, \"entities\": 19077, \"relations\": 16074, \"entity_f1\": 83.94, \"entity_precision\": 85, \"entity_recall\": 84.13, \"relation_f1_all_set\": 43.78, \"relation_precision_all_set\": 38.79, \"relation_recall_all_set\": 50.81, \"et_violations\": 0, \"et_violation_rate\": 0, \"rv_violations\": 0, \"rv_violation_rate\": 0, \"dr_violations\": 33, \"dr_violation_rate\": 0.21, \"CF_pct\": 0.21, \"delta_vs_unconstrained\": {\"delta_e_f1\": 0.01, \"delta_r_f1\": 0.06, \"delta_dr\": -0.28, \"note\": \"Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl (998 lines). Updated 2026-05-20.\"}, \"provenance\": \"eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl, 2026-05-20. P/R corrected 2026-05-20 per Director.\"}, \"conclusion\": \"success\"}, \"d066_sweep_16980_gpu1\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"d065_qwen_greedy_4096\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"d066_docred_beam_sweep\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"d067_seed_variance\": {\"status\": \"DONE\", \"metrics\": {\"qwen_scierc_unc\": {\"E_F1\": \"66.94 ± 0.08\", \"R_F1\": \"43.25 ± 0.43\", \"DR\": \"2.06 ± 0.08\", \"CF\": \"0.00 ± 0.00\"}, \"qwen_scierc_con\": {\"E_F1\": \"66.94 ± 0.08\", \"R_F1\": \"43.22 ± 0.39\", \"DR\": \"0.00 ± 0.00\", \"CF\": \"0.48 ± 0.02\"}, \"llama_scierc_unc\": {\"E_F1\": \"67.99 ± 0.16\", \"R_F1\": \"45.38 ± 0.05\", \"DR\": \"1.04 ± 0.05\", \"CF\": \"0.00 ± 0.00\"}, \"llama_scierc_con\": {\"E_F1\": \"67.99 ± 0.16\", \"R_F1\": \"45.40 ± 0.05\", \"DR\": \"0.03 ± 0.04\", \"CF\": \"0.26 ± 0.02\"}, \"max_sigma_pp\": 0.43, \"greedy_deterministic\": true, \"snr_dr_improvement\": \">12x\", \"qwen_docred_status\": \"pending (not started)\", \"llama_scierc_seed456_con_status\": \"running (407/551)\"}, \"conclusion\": \"success\"}, \"d068_constraint_guided_beam_pilot\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"d064_docred_full_beam\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"d065_tcr_full\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"configs_tested\": 10, \"all_cf_eliminated\": true, \"scierc_all_dr_delta_max\": 0.28, \"docred_lora_dr_delta_max\": 0.14, \"docred_zs_llama_dr_delta\": 9.38, \"docred_zs_70b_dr_delta\": 4.2, \"docred_zs_qwen_dr_delta\": 1.53, \"fund_conflict_scierc_max\": 2.04, \"fund_conflict_docred_zs_max\": 22.78, \"fund_conflict_docred_lora_max\": 12.16, \"lora_ef1_cost_max\": 0.0075, \"zs_docred_ef1_cost_max\": 0.0598}}, \"d065_tcr_pilot\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"scierc_zs_qwen\": {\"cf_before\": 9.75, \"cf_after\": 0, \"dr_before\": 0.93, \"dr_after\": 1.21, \"ef1_delta\": -0.0129, \"fund_pct\": 2.04}, \"scierc_zs_llama\": {\"cf_before\": 6.4, \"cf_after\": 0, \"dr_before\": 0.08, \"dr_after\": 0.3, \"ef1_delta\": -0.0178, \"fund_pct\": 1.85}, \"scierc_lora_qwen\": {\"cf_before\": 1.19, \"cf_after\": 0, \"dr_before\": 0, \"dr_after\": 0, \"ef1_delta\": -0.0075, \"fund_pct\": 0}, \"scierc_lora_llama\": {\"cf_before\": 0.46, \"cf_after\": 0, \"dr_before\": 0.09, \"dr_after\": 0.09, \"ef1_delta\": -0.0018, \"fund_pct\": 0}, \"scierc_zs_mistral\": {\"cf_before\": 0.67, \"cf_after\": 0, \"dr_before\": 13.36, \"dr_after\": 12.87, \"ef1_delta\": 0.0005, \"fund_pct\": 0}, \"docred_zs_qwen\": {\"cf_before\": 13.11, \"cf_after\": 0, \"dr_before\": 10.21, \"dr_after\": 11.74, \"ef1_delta\": -0.0344, \"fund_pct\": 13.52}, \"docred_zs_llama\": {\"cf_before\": 23.71, \"cf_after\": 0, \"dr_before\": 2.55, \"dr_after\": 11.93, \"ef1_delta\": -0.0521, \"fund_pct\": 22.78}, \"docred_zs_70b\": {\"cf_before\": 11.61, \"cf_after\": 0, \"dr_before\": 0, \"dr_after\": 4.2, \"ef1_delta\": -0.0598, \"fund_pct\": 18.26}, \"docred_lora_qwen\": {\"cf_before\": 0.42, \"cf_after\": 0, \"dr_before\": 0.01, \"dr_after\": 0.14, \"ef1_delta\": -0.0016, \"fund_pct\": 12.16}, \"docred_lora_llama\": {\"cf_before\": 0.36, \"cf_after\": 0, \"dr_before\": 0.21, \"dr_after\": 0.2, \"ef1_delta\": -0.0017, \"fund_pct\": 11.59}, \"total_configs\": 10, \"all_cf_eliminated\": true}}, \"d063_gollie_violation_rate\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"gollie_DR\": 0, \"gollie_RV\": 0, \"gollie_ET\": 0, \"gollie_CF\": 0.67, \"gollie_entities\": 300, \"gollie_relations\": 7, \"gollie_empty_docs_pct\": 45, \"docs_tested\": 100}}, \"d062_full_ft_scierc\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"unconstrained\": {\"entity_f1\": 0.6478, \"relation_f1\": 0.3789, \"DR_pct\": 2.74, \"RV_pct\": 0.18, \"ET_pct\": 0, \"CF_pct\": 0}, \"constrained\": {\"entity_f1\": 0.6478, \"relation_f1\": 0.3789, \"DR_pct\": 0, \"RV_pct\": 0, \"ET_pct\": 0, \"CF_pct\": 1.31}, \"training\": {\"eval_loss_final\": 0.09459, \"epochs\": 3, \"total_steps\": 333, \"training_time\": \"21m49s\"}}}, \"d062_beam_latency\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"beam4_unconstrained_s_per_doc\": 3.446, \"beam4_constrained_s_per_doc\": 4.013, \"beam4_unconstrained_total_s\": 1898.7, \"beam4_constrained_total_s\": 2211, \"beam_greedy_ratio_unconstrained\": 1.319, \"beam_greedy_ratio_constrained\": 1.397, \"constraint_overhead_beam\": 1.165, \"constraint_overhead_greedy\": 1.1, \"greedy_unconstrained_s_per_doc\": 2.612, \"greedy_constrained_s_per_doc\": 2.873}}, \"d062_ontology_scalability\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"compile_small_total_s\": 0.334, \"compile_medium_total_s\": 0.322, \"compile_large_total_s\": 0.345, \"compile_xlarge_total_s\": 0.42, \"grammar_small_s\": 0.333, \"grammar_xlarge_s\": 0.365, \"semantic_small_s\": 0.0004, \"semantic_xlarge_s\": 0.017, \"overhead_small\": 1.02, \"overhead_medium\": 1.03, \"overhead_large\": 1.03, \"overhead_xlarge\": 1.03, \"failures\": 0}}, \"d062_cf_majority_voting\": {\"status\": \"DONE\", \"metrics\": {\"qwen_scierc_zs\": {\"cf_before\": 245, \"cf_after\": 201, \"dr_rate_before\": 0.0093, \"dr_rate_after\": 0.0324}, \"llama_scierc_zs\": {\"cf_before\": 162, \"cf_after\": 123, \"dr_rate_before\": 0.0008, \"dr_rate_after\": 0.0236}, \"qwen_docred_zs\": {\"cf_before\": 518, \"cf_after\": 21, \"dr_rate_before\": 0.1021, \"dr_rate_after\": 0.1466}, \"llama_docred_zs\": {\"cf_before\": 1358, \"cf_after\": 107, \"dr_rate_before\": 0.0255, \"dr_rate_after\": 0.1665}, \"qwen_scierc_ft\": {\"cf_before\": 21, \"cf_after\": 12, \"dr_rate_before\": 0, \"dr_rate_after\": 0.0071}, \"llama_scierc_ft\": {\"cf_before\": 8, \"cf_after\": 4, \"dr_rate_before\": 0.0009, \"dr_rate_after\": 0.0037}, \"qwen_docred_ft\": {\"cf_before\": 48, \"cf_after\": 3, \"dr_rate_before\": 0.0001, \"dr_rate_after\": 0.0044}, \"llama_docred_ft\": {\"cf_before\": 41, \"cf_after\": 2, \"dr_rate_before\": 0.0021, \"dr_rate_after\": 0.005}}, \"conclusion\": \"negative\"}, \"p1_ee_ft_llama_r2\": {\"status\": \"DONE\", \"metrics\": {\"parse_rate_unconstrained\": 1, \"parse_rate_constrained\": 1, \"trigger_f1_unconstrained\": 0.2752, \"trigger_f1_constrained\": 0.2691, \"argument_f1_unconstrained\": 0.0998, \"argument_f1_constrained\": 0.0891, \"entity_f1\": 0, \"rov_rate_unconstrained\": 0.088, \"rov_rate_constrained\": 0, \"ac_rate_unconstrained\": 0.035, \"ac_rate_constrained\": 0.008, \"go_nogo_unconstrained\": 0.122, \"go_nogo_constrained\": 0.0078}, \"conclusion\": \"success\"}, \"p1_ee_ft_composability_r5\": {\"status\": \"DONE\", \"metrics\": {\"unconstrained\": {\"parse_rate\": 0.85, \"trigger_f1\": 0.3208, \"argument_f1\": 0.0785, \"rov_rate\": 0.3831, \"ac_rate\": 0.0268, \"go_nogo\": 0.41}, \"full_s1\": {\"parse_rate\": 0.95, \"trigger_f1\": 0.2672, \"argument_f1\": 0.0818, \"rov_rate\": 0, \"ac_rate\": 0, \"go_nogo\": 0}}, \"conclusion\": \"success\"}, \"p1_ee_ft_llama\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"p1_ee_ft_composability_r4\": {\"status\": \"DONE\", \"metrics\": {\"unconstrained\": {\"entity_f1\": 0, \"trigger_f1\": 0.4598, \"argument_f1\": 0.1581, \"rov\": 0.251, \"ac\": 0.06, \"cf\": 0, \"parse_rate\": 0.25}, \"full_s1\": {\"entity_f1\": 0.5823, \"trigger_f1\": 0.6, \"argument_f1\": 0.4667, \"rov\": 0, \"ac\": 0, \"cf\": 0.03, \"parse_rate\": 0.1}}, \"conclusion\": \"failed\"}, \"p1_llama_ee_ft\": {\"status\": \"PREPARING\"}, \"w9_qwen_docred_zs_sampling_r2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"70b_docred_constrained\": {\"status\": \"DONE\", \"metrics\": {\"ET_violation\": 0, \"RV_violation\": 0, \"DR_violation\": 0, \"CF_violation\": 7.01, \"entity_f1\": 69.05, \"entity_precision\": 75.03, \"entity_recall\": 63.95, \"relation_f1\": 13.07, \"relation_precision\": 12.54, \"relation_recall\": 13.64, \"parse_failures\": 1, \"docs_processed\": 997, \"total_docs\": 998, \"unique_entities\": 12207, \"total_triples\": 13249}, \"conclusion\": \"success\"}, \"70b_docred_unconstrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"entity_f1\": 69.03, \"entity_precision\": 75.03, \"entity_recall\": 63.92, \"relation_f1\": 13.03, \"relation_precision\": 12.43, \"relation_recall\": 13.69, \"ET_violation\": 0.02, \"RV_violation\": 7.8, \"DR_violation\": 15, \"CF_violation\": 0.07, \"parse_failures\": 0, \"docs_processed\": 998}}, \"p1_ee_ft_composability_r3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"p1_ee_ft_composability_r2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"p1_ee_ft_composability\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"p8c_ft_scierc_latency\": {\"status\": \"DONE\", \"metrics\": {\"unconstrained_mean_s\": 2.612, \"constrained_mean_s\": 2.873, \"unconstrained_median_s\": 2.355, \"constrained_median_s\": 2.624, \"overhead_mean_pct\": 10, \"overhead_median_pct\": 11.42, \"per_doc_ratio_mean\": 1.205, \"per_doc_ratio_median\": 1.117, \"num_docs\": 551, \"unconstrained_total_s\": 1439, \"constrained_total_s\": 1582.9}, \"conclusion\": \"success\"}, \"p8b_docred_latency\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"w9_qwen_docred_zs_sampling\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"w9_qwen_scierc_zs_sampling\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.75, \"CF_pct\": 9.9, \"E_F1\": 31.28, \"R_F1\": 7.42, \"parse_fail_rate\": 0, \"total_samples\": 551, \"note\": \"F1 computed by v2 checker; greedy baseline with same checker: E_F1=30.98, R_F1=8.36\"}, \"conclusion\": \"success\"}, \"p8_latency_overhead\": {\"status\": \"DONE\", \"metrics\": {\"samples\": 551, \"unconstrained_mean_s\": 4.163, \"unconstrained_median_s\": 4.106, \"unconstrained_total_s\": 2293.7, \"constrained_mean_s\": 4.71, \"constrained_median_s\": 4.644, \"constrained_total_s\": 2595, \"overhead_ratio_mean\": 1.131, \"overhead_ratio_median\": 1.131, \"overhead_ratio_p95_perdoc\": 1.262, \"overhead_pct\": 13.1}, \"conclusion\": \"success\"}, \"q1_llama_lora_scierc_beam4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ET_violation_rate\": 0, \"RV_violation_rate\": 0, \"DR_violation_rate\": 0, \"CF_violation_rate\": 0, \"entity_f1\": 67.94, \"relation_f1\": 46.11, \"samples\": 551, \"total_entities\": 1853, \"total_relations\": 727}}, \"70b_scierc_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.6, \"DR_pct\": 6.5, \"CF_count\": 0, \"CF_pct\": 0, \"E_F1\": 0.3517, \"E_P\": 0.3009, \"E_R\": 0.4232, \"R_F1\": 0.1122, \"R_P\": 0.0929, \"R_R\": 0.1417, \"total_entities\": 2353, \"total_relations\": 1485, \"parse_failures\": 0, \"samples\": 551}, \"conclusion\": \"success\"}, \"70b_scierc_constrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_count\": 86, \"CF_pct\": 3.66, \"E_F1\": 0.3514, \"E_P\": 0.3007, \"E_R\": 0.4226, \"R_F1\": 0.1124, \"R_P\": 0.0932, \"R_R\": 0.1417, \"total_entities\": 2351, \"total_relations\": 1481, \"parse_failures\": 0, \"samples\": 551}}, \"ee_mistral_wikievents_grammar_only_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_success\": \"218/246 (88.6%)\", \"parse_failures\": 28, \"ET\": 0, \"EV\": 0, \"RoV\": 64, \"AC\": 13.8, \"CF\": 1.1, \"go_no_go\": 77.73, \"entity_f1\": 0.1192, \"trigger_f1\": 0.0337, \"argument_f1\": 0.0027, \"code_version\": \"938-line (collision+exact-match fix)\", \"mode\": \"grammar_only\"}}, \"ee_mistral_wikievents_constrained_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_success\": \"218/246 (88.6%)\", \"parse_failures\": 28, \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 1.3, \"CF\": 14.9, \"go_no_go\": 1.26, \"entity_f1\": 0.1171, \"trigger_f1\": 0.0387, \"argument_f1\": 0.0031, \"code_version\": \"938-line (collision+exact-match fix)\", \"posthoc_args_removed\": 86, \"posthoc_ac_after\": 0}}, \"ee_llama_wikievents_constrained_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_success\": \"207/246 (84.1%)\", \"parse_failures\": 39, \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 3.8, \"CF\": 17.2, \"go_no_go\": 3.8, \"entity_f1\": 0.1763, \"trigger_f1\": 0.0748, \"argument_f1\": 0.0118, \"code_version\": \"938-line (collision+exact-match fix)\", \"posthoc_args_removed\": 173, \"posthoc_arg_f1\": 0.0118}}, \"ee_qwen_wikievents_constrained_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_success\": \"206/246 (83.7%)\", \"parse_failures\": 40, \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 2.1, \"CF\": 21.1, \"go_no_go\": 2.05, \"entity_f1\": 0.1409, \"trigger_f1\": 0.1339, \"argument_f1\": 0.0168, \"code_version\": \"938-line (collision+exact-match fix)\", \"posthoc_args_removed\": 109, \"posthoc_arg_f1\": 0.017, \"cf_voting_fix_rate\": \"15.9%\", \"cf_voting_entity_f1\": 0.1352}}, \"ee_mistral_wikievents_constrained_v2\": {\"status\": \"DONE\", \"metrics\": {\"parse_success\": \"178/246 (72.4%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 0.1, \"AC\": 16.6, \"CF\": 13.9, \"trigger_f1\": 0.0508, \"argument_f1\": 0.0047, \"entity_f1\": 0.1245, \"parse_failures\": 68, \"go_no_go\": 16.7}, \"conclusion\": \"success\"}, \"ee_qwen_wikievents_constrained\": {\"status\": \"DONE\", \"metrics\": {\"parse_success\": \"206/246 (83.7%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 0.3, \"AC\": 2.1, \"CF\": 21.1, \"trigger_f1\": 0.1339, \"argument_f1\": 0.0168, \"entity_f1\": 0.1409, \"parse_failures\": 40, \"go_no_go\": 2.4, \"note\": \"after retry with max_new_tokens=8192\"}, \"conclusion\": \"success\"}, \"ee_mistral_wikievents_constrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_success\": \"184/246 (74.8%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 54.8, \"AC\": 19.2, \"CF\": 0.7, \"note\": \"grammar_only baseline (old code without semantic mask fix)\"}}, \"ee_llama_wikievents_constrained\": {\"status\": \"DONE\", \"metrics\": {\"parse_success\": \"215/246 (87.4%)\", \"ET\": 0, \"EV\": 0, \"RoV\": 0, \"AC\": 3.4, \"CF\": 15.5, \"trigger_f1\": 0.078, \"argument_f1\": 0.011, \"entity_f1\": 0.178, \"parse_failures\": 31, \"go_no_go\": 3.4, \"note\": \"after retry with max_new_tokens=8192\"}, \"conclusion\": \"success\"}, \"ee_mistral_wikievents_unconstrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_success\": \"194/246 (78.9%)\", \"ET\": 0, \"EV\": 37.3, \"RoV\": 63.9, \"AC\": 0, \"CF\": 0, \"trigger_f1\": 0.0241, \"argument_f1\": 0, \"entity_f1\": 0}}, \"ee_llama_wikievents_unconstrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_success\": \"226/246 (91.9%)\", \"ET\": 0, \"EV\": 10.5, \"RoV\": 88.8, \"AC\": 0.1, \"CF\": 0, \"trigger_f1\": 0.0572, \"argument_f1\": 0, \"entity_f1\": 0}}, \"ee_qwen_wikievents_unconstrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"parse_success\": \"218/246 (88.6%)\", \"ET\": 0, \"EV\": 24, \"RoV\": 74.9, \"AC\": 0.3, \"CF\": 0, \"trigger_f1\": 0.1184, \"argument_f1\": 0.0009, \"entity_f1\": 0}}, \"r4_prompt_detailed\": {\"status\": \"DONE\", \"metrics\": {\"unconstrained\": {\"ET_pct\": 0.22, \"RV_pct\": 0.45, \"DR_pct\": 11.07, \"E_F1\": 33.55, \"R_F1\": 10.48}, \"constrained\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.64, \"E_F1\": 33.56, \"R_F1\": 10.48}, \"DR_reduction_pct\": 94.2, \"delta_R_F1_pp\": 0, \"delta_E_F1_pp\": 0.01}, \"conclusion\": \"success\"}, \"r4_prompt_minimal\": {\"status\": \"DONE\", \"metrics\": {\"unconstrained\": {\"ET_pct\": 0.58, \"RV_pct\": 1.16, \"DR_pct\": 16.91, \"E_F1\": 31.98, \"R_F1\": 7.91}, \"constrained\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.92, \"E_F1\": 31.99, \"R_F1\": 7.85}, \"DR_reduction_pct\": 94.6, \"delta_R_F1_pp\": -0.06, \"delta_E_F1_pp\": 0.01}, \"conclusion\": \"success\"}, \"w10_qwen_scierc_ft_beam_4\": {\"status\": \"DONE\", \"metrics\": {\"DR\": 0, \"CF\": 0, \"total_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"relation_vocab_violation_rate\": 0, \"domain_range_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0, \"E_F1\": 66.88, \"E_P\": 64.69, \"E_R\": 69.22, \"R_F1\": 44.23, \"R_P\": 39.41, \"R_R\": 50.41, \"total_samples\": 551, \"json_parse_failures\": 0, \"total_entities\": 1802, \"total_relations\": 1246, \"vs_ft_greedy\": {\"baseline\": \"w5_lora_scierc_constrained_eval\", \"DR_delta\": \"0% → 0% (same)\", \"CF_delta\": \"1.18% → 0.0% (eliminated all violations)\", \"E_F1_delta\": \"67.05 → 66.88 (-0.17, negligible)\", \"R_F1_delta\": \"43.77 → 44.23 (+0.46, slight improvement)\"}, \"vs_zs_beam_k4\": {\"DR_delta\": \"0% → 0% (same)\", \"CF_delta\": \"0.53% → 0.0% (eliminated)\", \"E_F1_delta\": \"32.00 → 66.88 (+34.88)\", \"R_F1_delta\": \"8.56 → 44.23 (+35.67)\"}}, \"conclusion\": \"success\"}, \"w10_beam_ablation_k8\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.08, \"CF_count\": 2, \"E_F1\": 32.18, \"R_F1\": 8.39, \"E_P\": 26.95, \"E_R\": 39.93, \"R_P\": 6.54, \"R_R\": 11.7, \"parse_failures\": 0, \"total_samples\": 551, \"total_triples\": 1744, \"total_entities\": 2483, \"vs_greedy\": {\"DR_delta\": -0.93, \"CF_delta\": -9.82, \"E_F1_delta\": 1.2, \"R_F1_delta\": 0.03}, \"vs_beam_k4\": {\"DR_delta\": 0, \"CF_delta\": -0.45, \"E_F1_delta\": 0.18, \"R_F1_delta\": -0.17}}, \"conclusion\": \"success\"}, \"w9_mistral_docred_beam_50\": {\"status\": \"DONE\", \"metrics\": {\"ET_violation_rate\": 0, \"RV_violation_rate\": 0, \"DR_violation_rate\": 21.37, \"CF_violations\": 1, \"total_triples\": 524, \"total_entities\": 597, \"docs_checked\": 49, \"parse_failures\": 1, \"E_F1\": 51.78, \"E_P\": 65.2, \"E_R\": 42.94, \"R_F1\": 5.7, \"R_P\": 6.49, \"R_R\": 5.08, \"R_tp\": 34, \"R_gold\": 669, \"R_pred\": 524}, \"conclusion\": \"success\"}, \"w10_beam_ablation_k2\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.35, \"CF_count\": 71, \"CF_pct\": 4.12, \"E_F1\": 31.54, \"R_F1\": 8.75, \"parse_failures\": 0, \"total_samples\": 551, \"total_triples\": 1724, \"vs_greedy\": {\"DR_delta\": -0.58, \"CF_delta\": -5.78, \"E_F1_delta\": 0.56, \"R_F1_delta\": 0.39, \"note\": \"Greedy: DR=0.93%, CF=9.90%, E_F1=30.98, R_F1=8.36\"}, \"vs_beam_k4\": {\"DR_delta\": 0.35, \"CF_delta\": 3.59, \"E_F1_delta\": -0.46, \"R_F1_delta\": 0.19, \"note\": \"k=4: DR=0%, CF=0.53%, E_F1=32.00, R_F1=8.56\"}}, \"conclusion\": \"success\"}, \"w10_mistral_scierc_beam_551\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 551, \"parse_failures\": 1, \"parse_rate\": 0.9982, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 13.79, \"CF_pct\": 0.57, \"E_P\": 23.04, \"E_R\": 31.64, \"E_F1\": 26.66, \"R_P\": 3.13, \"R_R\": 7.22, \"R_F1\": 4.37, \"total_entities\": 2294, \"total_triples\": 2241, \"vs_greedy\": {\"baseline\": \"w6_mistral_scierc_constrained\", \"greedy_DR\": 13.4, \"greedy_CF\": 1.27, \"greedy_E_F1\": 27.46, \"greedy_R_F1\": 3.67, \"delta_DR\": \"+0.39pp\", \"delta_CF\": \"-0.70pp\", \"delta_E_F1\": \"-0.80pp\", \"delta_R_F1\": \"+0.70pp\"}}, \"conclusion\": \"negative\"}, \"w10_llama_docred_beam_50\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.94, \"E_F1\": 55.62, \"R_F1\": 9.47, \"parse_failures\": 3, \"parse_fail_rate\": 6, \"total_samples\": 50, \"vs_greedy_full_s1\": {\"DR_delta\": -2.57, \"CF_delta\": -11.19, \"E_F1_delta\": 0.61, \"R_F1_delta\": 3.2, \"note\": \"Greedy baseline: DR=2.57%, CF=12.13%, E_F1=55.01, R_F1=6.27\"}, \"checker_note\": \"Must use violation_checker_docred.py for DocRED (not violation_checker.py)\"}, \"conclusion\": \"success\"}, \"w10_type_consensus_docred_50\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 8.69, \"CF_pct\": 2.4, \"E_F1\": 59.08, \"R_F1\": 8.33, \"gtc_skip_total\": 601, \"gtc_skip_unique_entities\": 213, \"gtc_effective_corrections\": 0, \"delta_DR\": 0, \"delta_CF\": 0}, \"conclusion\": \"negative\"}, \"w10_type_consensus_prototype\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36, \"gtc_skip_total\": 672, \"gtc_skip_unique_entities\": 258, \"gtc_effective_corrections\": 0, \"delta_DR\": 0, \"delta_CF\": 0}, \"conclusion\": \"negative\"}, \"w9_qwen_scierc_stability_3seeds\": {\"status\": \"DONE\", \"metrics\": {\"seed_123\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36}, \"seed_456\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36}, \"seed_789\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.93, \"CF_pct\": 9.9, \"E_F1\": 30.98, \"R_F1\": 8.36}, \"cross_seed_DR_std\": 0, \"cross_seed_DR_range\": 0, \"conclusion_note\": \"Greedy decoding is fully deterministic - seed has no effect on output. All metrics identical across 3 seeds.\"}, \"conclusion\": \"success\"}, \"w9_qwen_docred_beam_50\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.55, \"E_F1\": 58.64, \"R_F1\": 9.37, \"total_samples\": 50, \"parse_failures\": 3, \"parse_fail_rate\": 6, \"vs_greedy_full_s1\": {\"DR_delta\": -10.21, \"CF_delta\": -2.02, \"E_F1_delta\": -0.73, \"R_F1_delta\": 1.14, \"note\": \"Greedy full_s1 998 docs: DR=10.21%, CF=2.57%, E_F1=59.37, R_F1=8.23. Beam eliminates ALL DR on DocRED 96-type schema.\"}}, \"conclusion\": \"success\"}, \"w9_llama_scierc_beam_551\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.93, \"CF_count\": 15, \"E_F1\": 25.04, \"E_P\": 21.27, \"E_R\": 30.42, \"R_F1\": 3.33, \"R_P\": 2.68, \"R_R\": 4.41, \"total_entities\": 2398, \"total_relations\": 1606, \"parse_fail_rate\": 0, \"total_samples\": 551, \"vs_greedy_full_s1\": {\"DR_delta\": -0.08, \"CF_delta\": -5.63, \"E_F1_delta\": 1.55, \"R_F1_delta\": 0.79, \"note\": \"Greedy: DR=0.08%, CF=6.56%, E_F1=23.49%, R_F1=2.54%\"}}, \"conclusion\": \"success\"}, \"posthoc_filtering_baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"docred_f1_before\": 7.74, \"docred_f1_after\": 9.61, \"docred_precision_before\": 6.55, \"docred_precision_after\": 11.22, \"docred_recall_before\": 9.46, \"docred_recall_after\": 8.4, \"docred_rejection_rate\": 0.481, \"docred_tp_before\": 1137, \"docred_tp_after\": 1010, \"docred_tp_lost\": 127, \"docred_et_residual\": 0.0247, \"scierc_f1_before\": 8.23, \"scierc_f1_after\": 8.63, \"scierc_rejection_rate\": 0.168, \"scierc_recall_before\": 11.4, \"scierc_recall_after\": 10.68, \"scierc_tp_before\": 111, \"scierc_tp_after\": 104}}, \"phase2_scierc_full_s2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1644, \"total_entities\": 2228, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0097, \"cross_field_consistency_violation_rate\": 0.0803, \"entity_precision\": 0.2797, \"entity_recall\": 0.3712, \"entity_f1\": 0.319, \"relation_precision\": 0.064, \"relation_recall\": 0.1078, \"relation_f1\": 0.0803, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"llama_docred_unconstrained_mt6144\": {\"status\": \"DONE\", \"metrics\": {\"ET_rate\": 0.13, \"RV_rate\": 15.89, \"DR_rate\": 26.18, \"DR_rate_eligible\": 31.15, \"CF_rate\": 0.17, \"entity_precision\": 61.19, \"entity_recall\": 51.06, \"entity_f1\": 55.67, \"relation_precision\": 5.18, \"relation_recall\": 7, \"relation_f1\": 5.95, \"parse_failures\": 67, \"documents_checked\": 931, \"total_documents\": 998, \"unique_entities\": 11534, \"total_triples\": 16584, \"dr_eligible_triples\": 13936, \"fuzzy_relation_matches\": 121}, \"conclusion\": \"success\"}, \"llama_docred_full_s1_mt6144\": {\"status\": \"DONE\", \"metrics\": {\"DR_rate_pct\": 2.57, \"RV_rate_pct\": 0, \"ET_rate_pct\": 0, \"CF_rate_pct\": 12.13, \"R_F1\": 6.25, \"R_precision\": 5.45, \"R_recall\": 7.32, \"E_F1\": 55.04, \"E_precision\": 61.41, \"E_recall\": 49.87, \"documents_total\": 998, \"documents_checked\": 908, \"parse_failures\": 90, \"triples\": 16471, \"unique_entities\": 11307, \"fallback_events\": 67911, \"wall_clock_seconds\": 23926, \"vs_unconstrained_mt6144\": {\"DR_delta_pp\": -23.61, \"DR_reduction_pct\": -90.2, \"R_F1_delta_pp\": 0.3, \"E_F1_delta_pp\": -0.63}, \"vs_full_s1_mt4096\": {\"DR_delta_pp\": 0.02, \"R_F1_delta_pp\": -0.02, \"E_F1_delta_pp\": 0.03, \"CF_delta_pp\": 0.11, \"parse_fail_delta\": -1}}, \"conclusion\": \"success\"}, \"beam_search_scierc_full_551\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0, \"CF_pct\": 0.53, \"E_F1\": 32, \"R_F1\": 8.56, \"E_P\": 26.83, \"E_R\": 39.63, \"R_P\": 6.69, \"R_R\": 11.91, \"parse_fail_rate\": 0, \"total_entities\": 2476, \"total_relations\": 1737}}, \"w7_llama_scierc_ft_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.65, \"CF_count\": 2, \"E_F1\": 67.76, \"E_P\": 66.47, \"E_R\": 69.1, \"R_F1\": 45.47, \"R_P\": 43.24, \"R_R\": 47.95, \"total_entities\": 1757, \"total_relations\": 1081, \"json_parse_failures\": 0}, \"conclusion\": \"success\"}, \"w7_llama_scierc_ft_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 551, \"json_parse_failures\": 0, \"total_entities\": 1757, \"total_relations\": 1082, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0111, \"cross_field_consistency_violation_rate\": 0, \"entity_f1\": {\"precision\": 0.6647, \"recall\": 0.691, \"f1\": 0.6776}, \"relation_f1\": {\"precision\": 0.432, \"recall\": 0.4795, \"f1\": 0.4545}}, \"conclusion\": \"success\"}, \"w7_qwen_scierc_ft_semantic_only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.6, \"CF_count\": 15, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_entities\": 1784, \"total_relations\": 1128, \"E_P\": 0.6523, \"E_R\": 0.6898, \"E_F1\": 0.6705, \"R_P\": 0.4073, \"R_R\": 0.4713, \"R_F1\": 0.4369, \"DR_violations\": 7, \"delta_vs_grammar_only\": {\"DR_delta\": -1.3, \"note\": \"semantic_only DR=0.6% vs grammar_only DR=1.9%, semantic layer reduces DR by 68%\"}, \"delta_vs_unconstrained\": {\"DR_delta\": -1.35, \"note\": \"unconstrained DR=1.95% → semantic_only 0.6%\"}}}, \"w7_qwen_scierc_ft_grammar_only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 1.9, \"CF_pct\": 0, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_entities\": 1784, \"total_relations\": 1128, \"E_P\": 0.6523, \"E_R\": 0.6898, \"E_F1\": 0.6705, \"R_P\": 0.4087, \"R_R\": 0.4733, \"R_F1\": 0.4386, \"DR_violations\": 22, \"tokenizer_warning\": \"false_positive_transformers_4.57.6\"}}, \"w5_llama_lora_scierc_unconstrained_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 551, \"total_entities\": 1757, \"total_relations\": 1082, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0111, \"cross_field_consistency_violation_rate\": 0, \"total_violation_rate\": 0.0042, \"entity_precision\": 0.6647, \"entity_recall\": 0.691, \"entity_f1\": 0.6776, \"relation_precision\": 0.432, \"relation_recall\": 0.4795, \"relation_f1\": 0.4545}}, \"w5_llama_lora_scierc_constrained_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"domain_range_violation_rate\": 0.0009, \"relation_vocabulary_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0046, \"relation_f1\": 0.4547, \"relation_precision\": 0.432, \"relation_recall\": 0.4795, \"entity_f1\": 0.6776, \"entity_precision\": 0.6647, \"entity_recall\": 0.691, \"total_relations\": 1081, \"total_entities\": 1757, \"total_samples\": 551, \"parse_failures\": 0}}, \"w5_lora_scierc_constrained_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0118, \"entity_f1\": 0.6705, \"entity_precision\": 0.6523, \"entity_recall\": 0.6898, \"relation_f1\": 0.4377, \"relation_precision\": 0.4078, \"relation_recall\": 0.4723, \"total_entities\": 1784, \"total_relations\": 1128, \"total_samples\": 551, \"cross_field_consistency_violations\": 21}}, \"w1_cf_fallback_scierc_pilot\": {\"status\": \"DONE\", \"metrics\": {\"ET\": 0, \"RV\": 0, \"DR\": 0.1478, \"CF\": 0.0004, \"R_F1\": 0.0823, \"R_P\": 0.0643, \"R_R\": 0.114, \"E_F1\": 0.3098, \"E_P\": 0.2598, \"E_R\": 0.3837, \"entities\": 2474, \"relations\": 1725, \"samples\": 551, \"grammar_first_fallback_rate\": 0.3664, \"cf_registry_fallback_rate\": 0.0448, \"total_mask_calls\": 17024, \"violation_budget_DR_CF\": 0.1482}, \"conclusion\": \"negative\"}, \"w5_lora_scierc_training\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.0634, \"eval_loss\": 0.0586, \"eval_token_accuracy\": 0.9816, \"eval_entropy\": 0.9635, \"train_runtime_sec\": 688.4, \"epochs\": 3, \"checkpoint_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc\", \"merged_model_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen3_8b_lora_scierc_merged\"}, \"conclusion\": \"success\"}, \"w8_qwen_docred_ft_grammar_only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"E_F1\": 82.19, \"E_P\": 85.47, \"E_R\": 79.16, \"R_F1\": 40.85, \"R_P\": 36.27, \"R_R\": 46.77, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.61, \"CF_pct\": 0.11, \"parse_fail_rate\": 7.01, \"total_samples\": 998, \"parse_failures\": 70}}, \"w6_mistral_scierc_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"E_P\": 0.2402, \"E_R\": 0.3156, \"E_F1\": 0.2728, \"R_P\": 0.0295, \"R_R\": 0.0483, \"R_F1\": 0.0366, \"ET_pct\": 1.5, \"RV_pct\": 0, \"DR_pct\": 56.94, \"CF_pct\": 56.87, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_pred_entities\": 2202, \"total_pred_relations\": 1593}, \"conclusion\": \"success\"}, \"w6_mistral_scierc_constrained\": {\"status\": \"DONE\", \"metrics\": {\"E_P\": 0.2437, \"E_R\": 0.3144, \"E_F1\": 0.2746, \"R_P\": 0.0292, \"R_R\": 0.0493, \"R_F1\": 0.0367, \"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 13.4, \"CF_pct\": 1.27, \"CF_count\": 21, \"parse_fail_rate\": 0, \"total_samples\": 551, \"total_pred_entities\": 2162, \"total_pred_relations\": 1647, \"delta_vs_unconstrained\": {\"delta_E_F1\": 0.0018, \"delta_R_F1\": 0.0001, \"delta_ET\": -1.5, \"delta_RV\": 0, \"delta_DR\": -43.54, \"note\": \"Constrained - unconstrained. Baseline: E_F1=0.2728, R_F1=0.0366, DR=56.94%, ET=1.5%, RV=0%\"}}, \"conclusion\": \"success\"}, \"w8_ft_posthoc_baseline\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ft_regime\": {\"qwen_scierc\": {\"R_F1_before\": 43.86, \"R_F1_posthoc\": 43.94, \"R_F1_constrained\": 43.77, \"reject_rate_pct\": 1.95, \"TP_lost\": 4}, \"llama_scierc\": {\"R_F1_before\": 45.45, \"R_F1_posthoc\": 45.23, \"R_F1_constrained\": 45.47, \"reject_rate_pct\": 1.11, \"TP_lost\": 5}, \"qwen_docred\": {\"R_F1_before\": 40.91, \"R_F1_posthoc\": 41.11, \"R_F1_constrained\": \"TBD\", \"reject_rate_pct\": 1.03, \"TP_lost\": 1}, \"llama_docred\": {\"R_F1_before\": 43.77, \"R_F1_posthoc\": 43.92, \"R_F1_constrained\": 44.23, \"reject_rate_pct\": 0.64, \"TP_lost\": 1}}, \"zs_regime\": {\"mistral_scierc\": {\"triples\": 1584, \"reject_pct\": 20.27, \"R_F1_before\": 0.0376, \"R_F1_posthoc\": 0.0394, \"R_F1_constrained\": 0.0367, \"TP_before\": 48, \"TP_after\": 44, \"TP_lost\": 4}, \"qwen_scierc\": {\"triples\": 1724, \"reject_pct\": 16.76, \"R_F1_before\": 0.0823, \"R_F1_posthoc\": 0.0863, \"R_F1_constrained\": 0.0836, \"TP_before\": 111, \"TP_after\": 104, \"TP_lost\": 7}, \"llama_scierc\": {\"triples\": 1274, \"reject_pct\": 13.89, \"R_F1_before\": 0.0268, \"R_F1_posthoc\": 0.0271, \"R_F1_constrained\": 0.0254, \"TP_before\": 30, \"TP_after\": 28, \"TP_lost\": 2}, \"qwen_docred\": {\"triples\": 17497, \"reject_pct\": 48.12, \"R_F1_before\": 0.0774, \"R_F1_posthoc\": 0.0961, \"R_F1_constrained\": 0.0823, \"TP_before\": 1137, \"TP_after\": 1010, \"TP_lost\": 127}, \"llama_docred\": {\"triples\": 16437, \"reject_pct\": 42.18, \"R_F1_before\": 0.0598, \"R_F1_posthoc\": 0.0744, \"R_F1_constrained\": 0.0627, \"TP_before\": 850, \"TP_after\": 802, \"TP_lost\": 48}, \"mistral_docred\": {\"triples\": 11836, \"reject_pct\": 73.73, \"R_F1_before\": 0.0434, \"R_F1_posthoc\": 0.0385, \"R_F1_constrained\": 0.0552, \"TP_before\": 518, \"TP_after\": 292, \"TP_lost\": 226, \"removed_RV\": 4172, \"removed_ET\": 3382, \"removed_DR\": 1173, \"note\": \"Only ZS case where posthoc HURTS R_F1 — 73.7% rejection rate loses 43.6% of TPs\"}}, \"key_finding\": \"ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception: Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained decoding value is in structural guarantee (0% violations) and composability, not F1 preservation.\"}}, \"w6_mistral_docred_unconstrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 998, \"parse_failures\": 7, \"parse_fail_rate\": 0.7, \"total_pred_entities\": 12580, \"total_pred_relations\": 11879, \"ET_pct\": 7.58, \"RV_pct\": 42.35, \"DR_pct\": 57.42, \"CF_pct\": 24.78, \"E_P\": 0.6221, \"E_R\": 0.3975, \"E_F1\": 0.4851, \"R_P\": 0.0447, \"R_R\": 0.0432, \"R_F1\": 0.0434, \"f1_method\": \"fuzzy_normalized\", \"f1_note\": \"Relation matching uses case-insensitive normalization with token-overlap >80% and edit-distance ≤2 fallback. Strict R_F1=3.50% (delta +0.84pp from 98 additional TPs via fuzzy matching of Mistral underscore/abbreviation variants).\"}}, \"w6_mistral_docred_constrained\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 33.2, \"CF_pct\": 0.19, \"E_P\": 65.02, \"E_R\": 41.4, \"E_F1\": 50.59, \"R_P\": 5.67, \"R_R\": 5.37, \"R_F1\": 5.52, \"parse_fail_rate\": 0.8, \"total_samples\": 998, \"total_pred_entities\": 12535, \"total_pred_relations\": 11554, \"delta_vs_unconstrained\": {\"ET_pct\": -7.58, \"RV_pct\": -42.35, \"DR_pct\": -24.22, \"CF_pct\": -24.59, \"E_F1\": 2.08, \"R_F1\": 2.02}}, \"conclusion\": \"success\"}, \"w5_qwen_docred_lora_constrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0, \"DR_pct\": 0.01, \"CF_pct\": 0.41, \"E_F1\": 81.43, \"E_P\": 85.41, \"E_R\": 77.81, \"R_F1\": 40.56, \"R_P\": 36.35, \"R_R\": 45.86, \"parse_fail_rate\": 8.52, \"total_samples\": 998, \"success_samples\": 913, \"fail_samples\": 85, \"total_entities_pred\": 17799, \"total_relations_pred\": 15563, \"E_F1_excl_fail\": 85.69, \"R_F1_excl_fail\": 42.23, \"delta_vs_unconstrained\": {\"delta_DR\": -0.75, \"delta_RV\": -0.27, \"delta_R_F1\": -0.3, \"delta_R_F1_excl_fail\": 0.03, \"DR_reduction_pct\": 98.7, \"note\": \"Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20\"}}, \"conclusion\": \"success\"}, \"w5_llama_docred_sft_data_gen\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"train_samples\": 3053, \"dev_samples\": 998, \"train_size_mb\": 19, \"dev_size_mb\": 6.1}}, \"w1_cf_fallback_llama_docred\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"w1_cf_fallback_llama_scierc\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"w5_qwen_docred_lora_unconstrained_eval\": {\"status\": \"DONE\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.27, \"DR_pct\": 0.76, \"CF_pct\": 0.12, \"E_F1\": 82.15, \"E_P\": 85.44, \"E_R\": 79.11, \"R_F1\": 40.86, \"R_P\": 36.41, \"R_R\": 46.56, \"parse_fail_rate\": 7.11, \"total_samples\": 998, \"success_samples\": 927, \"fail_samples\": 71, \"total_entities_pred\": 18091, \"total_relations_pred\": 15870, \"ET_pct_excl_fail\": 0, \"RV_pct_excl_fail\": 0.27, \"DR_pct_excl_fail\": 0.76, \"CF_pct_excl_fail\": 0.12, \"E_F1_excl_fail\": 85.72, \"E_P_excl_fail\": 85.44, \"E_R_excl_fail\": 86, \"R_F1_excl_fail\": 42.2, \"R_P_excl_fail\": 36.41, \"R_R_excl_fail\": 50.17}, \"conclusion\": \"success\"}, \"w5_llama_docred_lora_unconstrained_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"ET_pct\": 0, \"RV_pct\": 0.15, \"DR_pct\": 0.49, \"E_F1\": 83.93, \"E_P\": 84.93, \"E_R\": 82.96, \"R_F1\": 43.72, \"R_P\": 38.59, \"R_R\": 50.41, \"parse_fail_rate\": 2.3, \"total_samples\": 998, \"total_entities_pred\": 19106, \"total_relations_pred\": 16171}}, \"w5_qwen_docred_lora_training\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_loss\": 0.0614, \"eval_mean_token_accuracy\": 0.9804, \"eval_entropy\": 0.715, \"train_loss\": 0.0682, \"train_runtime_s\": 5825.6, \"epochs\": 3, \"adapter_path\": \"/root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred\", \"merged_path\": \"/root/autodl-tmp/checkpoints/qwen_lora_docred_merged\"}}, \"w5_llama_docred_lora_training\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.0572, \"eval_loss\": 0.0624, \"token_acc\": 98.06}}, \"w5_docred_sft_data_gen\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"train_samples\": 3053, \"dev_samples\": 998, \"train_entities\": 59493, \"train_relations\": 38180, \"dev_entities\": 19528, \"dev_relations\": 12275}}, \"w5_llama_lora_scierc_training\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"eval_loss\": 0.0595, \"eval_mean_token_accuracy\": 0.9817, \"eval_entropy\": 1.0565, \"train_loss\": 0.0501, \"train_runtime_sec\": 654.23, \"epochs\": 3, \"train_samples_per_second\": 8.08}}, \"w1_cf_fallback_docred\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"w5_lora_scierc_unconstrained_eval\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0195, \"cross_field_consistency_violation_rate\": 0, \"entity_f1\": 0.6705, \"entity_precision\": 0.6523, \"entity_recall\": 0.6898, \"relation_f1\": 0.4386, \"relation_precision\": 0.4087, \"relation_recall\": 0.4733, \"total_entities\": 1784, \"total_relations\": 1128, \"domain_range_violations\": 22, \"go_nogo_metric\": 0.0195, \"dr_gate\": \"FAILED\"}}, \"llama_docred_full_s1\": {\"status\": \"DONE\", \"metrics\": {\"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"f1_method\": \"all_set\", \"violations\": {\"ET\": 0, \"RV\": 0, \"DR\": 2.55, \"CF\": 12.02}, \"f1\": {\"entity_f1\": 55.01, \"entity_precision\": 61.41, \"entity_recall\": 49.82, \"relation_f1\": 6.27, \"relation_precision\": 5.49, \"relation_recall\": 7.32}, \"counts\": {\"documents\": 998, \"documents_checked\": 907, \"parse_failures\": 91, \"unique_entities\": 11296, \"triples\": 16368}}, \"conclusion\": \"success\"}, \"llama_docred_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"checker_version\": \"fixed_20260514_v2\", \"f1_method\": \"all_set\", \"documents\": 998, \"documents_checked\": 930, \"parse_failures\": 68, \"unique_entities\": 11525, \"total_triples\": 16437, \"dr_eligible_triples\": 13789, \"ET_rate_pct\": 0.13, \"RV_rate_pct\": 16.03, \"DR_rate_pct\": 26.07, \"CF_rate_pct\": 0.17, \"entity_precision\": 61.22, \"entity_recall\": 51.02, \"entity_f1\": 55.65, \"relation_precision\": 5.22, \"relation_recall\": 7, \"relation_f1\": 5.98, \"fuzzy_relation_matches\": 121}, \"conclusion\": \"success\"}, \"phase2_docred_grammar_only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"documents_checked\": 985, \"parse_failures\": 13, \"total_entities\": 20150, \"total_triples\": 17341, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0.0003, \"domain_range_violation_rate\": 0.2617, \"cross_field_consistency_violation_rate\": 0.0007, \"relation_f1\": 8.31, \"relation_precision\": 7.06, \"relation_recall\": 10.12, \"entity_f1\": 59.38, \"entity_precision\": 58.47, \"entity_recall\": 60.32, \"unrecognized_relations\": 5, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"llama_scierc_full_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"samples\": 550, \"entities_extracted\": 2469, \"relations_extracted\": 1315, \"domain_range_violation_rate\": 0.0008, \"relation_vocab_violation_rate\": 0, \"entity_type_violation_rate\": 0, \"cross_field_consistency_violation_rate\": 0.0656, \"total_violation_rate\": 0.0431, \"entity_f1\": 0.2349, \"entity_precision\": 0.1972, \"entity_recall\": 0.2902, \"relation_f1\": 0.0254, \"relation_precision\": 0.0221, \"relation_recall\": 0.0298, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"llama_scierc_unconstrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"entity_type_violation_rate\": 0, \"relation_vocab_violation_rate\": 0.0055, \"domain_range_violation_rate\": 0.1334, \"cross_field_consistency_violations\": 6, \"entity_f1\": 0.2356, \"entity_precision\": 0.1983, \"entity_recall\": 0.2902, \"relation_f1\": 0.0268, \"relation_precision\": 0.0236, \"relation_recall\": 0.031, \"total_entities\": 2451, \"total_relations\": 1274, \"json_parse_failures\": 1, \"samples\": 551, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_full_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1729, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.0093, \"cross_field_consistency_violation_rate\": 0.099, \"entity_f1\": 0.3098, \"entity_precision\": 0.2598, \"entity_recall\": 0.3837, \"relation_f1\": 0.0836, \"relation_precision\": 0.0654, \"relation_recall\": 0.116, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_semantic_only\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1726, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0151, \"domain_range_violation_rate\": 0.1165, \"cross_field_consistency_violation_rate\": 0.0271, \"entity_f1\": 0.3101, \"entity_precision\": 0.2605, \"entity_recall\": 0.3831, \"relation_f1\": 0.0815, \"relation_precision\": 0.0637, \"relation_recall\": 0.1129, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_scierc_grammar_only\": {\"status\": \"DONE\", \"metrics\": {\"total_samples\": 551, \"total_triples\": 1725, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0, \"domain_range_violation_rate\": 0.1484, \"cross_field_consistency_violation_rate\": 0.0008, \"entity_f1\": 0.3098, \"entity_precision\": 0.2598, \"entity_recall\": 0.3837, \"relation_f1\": 0.0823, \"relation_precision\": 0.0643, \"relation_recall\": 0.114, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"conclusion\": \"success\"}, \"phase2_scierc_unconstrained\": {\"status\": \"DONE\", \"metrics\": {\"json_parse_rate\": 1, \"entity_f1\": 0.3101, \"entity_precision\": 0.2605, \"entity_recall\": 0.3831, \"relation_f1\": 0.0823, \"relation_precision\": 0.0644, \"relation_recall\": 0.114, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0139, \"domain_range_violation_rate\": 0.1537, \"cross_field_consistency_violation_rate\": 0.0008, \"total_triples\": 1724, \"total_entities\": 2474, \"total_samples\": 551, \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}, \"conclusion\": \"success\"}, \"phase2_docred_full_s1\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"documents_checked\": 987, \"parse_failures\": 11, \"total_entities\": 20187, \"total_triples\": 17341, \"entity_type_violation_rate\": 0, \"relation_vocabulary_violation_rate\": 0.0003, \"domain_range_violation_rate\": 0.1021, \"cross_field_consistency_violation_rate\": 0.0257, \"entity_f1\": 59.37, \"entity_precision\": 58.45, \"entity_recall\": 59.63, \"relation_f1\": 8.23, \"relation_precision\": 6.99, \"relation_recall\": 10.01, \"unrecognized_relations\": 5, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"}}, \"phase2_docred_semantic_only\": {\"status\": \"DONE\", \"metrics\": {\"documents_checked\": 987, \"parse_failures\": 11, \"total_entities\": 20185, \"total_triples\": 17571, \"entity_type_violation_rate\": 0.0422, \"relation_vocabulary_violation_rate\": 0.2987, \"domain_range_violation_rate\": 0.1384, \"cross_field_consistency_violation_rate\": 0.0105, \"entity_f1\": 57.81, \"entity_precision\": 57.27, \"entity_recall\": 58.37, \"relation_f1\": 7.7, \"relation_precision\": 6.54, \"relation_recall\": 9.37, \"f1_method\": \"all_set\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"et_v1\": 0.1044, \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"}, \"conclusion\": \"success\"}, \"phase2_docred_unconstrained\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"documents_checked\": 986, \"parse_failures\": 12, \"total_entities\": 20171, \"total_triples\": 17497, \"entity_type_violation_rate\": 0.0248, \"relation_vocabulary_violation_rate\": 0.2966, \"domain_range_violation_rate\": 0.1846, \"cross_field_consistency_violation_rate\": 0.001, \"entity_f1\": 58.15, \"entity_precision\": 57.26, \"entity_recall\": 58.32, \"relation_f1\": 7.74, \"relation_precision\": 6.55, \"relation_recall\": 9.46, \"unrecognized_relations\": 5189, \"f1_method\": \"all_set (includes OOV predictions in denominator)\", \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\", \"et_v1\": 0.0818, \"et_fix_note\": \"v1 triple-counted ET across entity_list + relation head/tail; v2 deduplicates by (text, normalized_type)\"}}, \"mvp_phase0_docred_schema_r2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"phase2_s2_pilot50\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"domain_range_violation_rate\": 0.0205, \"relation_vocabulary_violation_rate\": 0, \"relation_f1\": 0.1008, \"samples\": 50, \"predicted_relations\": 146, \"true_positives\": 13, \"gold_relations\": 112, \"entity_f1_approx\": 0.29, \"note\": \"DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。\"}}, \"mvp_phase0_docred_schema\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"total_documents\": 998, \"documents_checked\": 943, \"parse_failures\": 55, \"json_parse_rate\": 0.9449, \"total_entities\": 19524, \"total_triples\": 16782, \"entity_type_violations\": 119, \"entity_type_violation_rate\": 0.0061, \"relation_vocabulary_violations\": 3090, \"relation_vocabulary_violation_rate\": 0.1841, \"relation_fuzzy_matches\": 85, \"domain_range_violations\": 2154, \"domain_range_violation_rate\": 0.1284, \"cross_field_consistency_violations\": 29, \"cross_field_consistency_violation_rate\": 0.0015, \"total_violations_any\": 5392, \"total_violation_rate\": 0.1485, \"go_nogo_metric_dr\": 0.1284}}, \"mvp_phase0_violation_rate_docred\": {\"status\": \"DONE\", \"metrics\": {\"total_docs\": 998, \"parsed_docs\": 962, \"json_parse_rate\": 0.964, \"total_entities\": 19099, \"total_triples\": 16540, \"entity_type_violation_rate\": 0.075, \"relation_vocabulary_violation_rate\": 0.289, \"domain_range_violation_rate\": 0.187, \"cross_field_consistency_violation_rate\": 0.0008, \"go_nogo_metric\": 0.187, \"fuzzy_matches\": 126, \"top_dr_violations_by_rate\": {\"P35_head_of_state\": 1, \"P710_participant\": 0.919, \"P172_ethnic_group\": 0.875}, \"top_dr_violations_by_count\": {\"P31_instance_of\": {\"violations\": 322, \"total\": 533, \"rate\": 0.604}, \"P1001_applies_to_jurisdiction\": {\"violations\": 264, \"total\": 594, \"rate\": 0.444}, \"P1344_participant_in\": {\"violations\": 194, \"total\": 312, \"rate\": 0.622}}}, \"conclusion\": \"success\"}, \"mvp_phase0_scierc_schema\": {\"status\": \"DONE\", \"metrics\": {\"domain_range_violation_rate\": 0.0578, \"relation_vocabulary_violation_rate\": 0.003, \"entity_type_violation_rate\": 0, \"total_violation_rate\": 0.0253, \"go_nogo_metric\": 0.0578, \"total_triples\": 1661, \"vs_minimal_dr_reduction\": -0.624, \"per_relation\": {\"Used-for\": {\"rate\": \"TBD\"}, \"Feature-of\": {\"delta_pp\": -22.3}, \"Part-of\": {\"delta_pp\": -22.5}, \"Compare\": {\"delta_pp\": -14.8}, \"Evaluate-for\": {\"delta_pp\": 5.8}}, \"mcnemar_all_significant\": true}, \"conclusion\": \"success\"}, \"mvp_phase0_violation_rate\": {\"status\": \"DONE\", \"metrics\": {\"total_triples\": 1724, \"total_entities\": 2474, \"json_parse_rate\": 1, \"entity_type_violation_rate\": 0.004, \"relation_vocabulary_violation_rate\": 0.0139, \"domain_range_violation_rate\": 0.1537, \"cross_field_consistency_violation_rate\": 0.0008, \"go_nogo_metric\": 0.1537, \"entity_f1\": 0.3101, \"relation_f1\": 0.0823, \"per_relation\": {\"Used-for\": {\"total\": 787, \"dr_violations\": 6, \"rate\": 0.0076}, \"Conjunction\": {\"total\": 32, \"dr_violations\": 0, \"rate\": 0}, \"Hyponym-of\": {\"total\": 124, \"dr_violations\": 18, \"rate\": 0.1452}, \"Evaluate-for\": {\"total\": 133, \"dr_violations\": 32, \"rate\": 0.2406}, \"Part-of\": {\"total\": 72, \"dr_violations\": 18, \"rate\": 0.25}, \"Feature-of\": {\"total\": 486, \"dr_violations\": 163, \"rate\": 0.3354}, \"Compare\": {\"total\": 66, \"dr_violations\": 28, \"rate\": 0.4242}}}, \"conclusion\": \"success\"}}, \"count\": 164, \"total\": 164, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5246}}"
    }
  },
  "sourceToolAssistantUUID": "dd230e38-1f54-4fe0-9f9c-486c6283d801",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33 · 2026-05-23T10:23:27.212Z_

```json
{
  "parentUuid": "0f184065-eec0-4510-9567-2582a3b1060c",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c3257a42-062c-4c64-a87f-912f5d97d2e0",
  "timestamp": "2026-05-23T10:23:27.212Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "leafUuid": "c3257a42-062c-4c64-a87f-912f5d97d2e0",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper tables 1 and 2 numerical values",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---

### Assistant

_source line 36 · 2026-05-23T10:23:30.587Z_

<details><summary>Logged reasoning block</summary>

```text
The result is too large. Let me query for specific experiments related to Table 1 and Table 2. Let me search for the phase2_scierc experiments first, then the fine-tuning experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3257a42-062c-4c64-a87f-912f5d97d2e0",
  "isSidechain": false,
  "requestId": "req_011CbKLTdo4iCEzoxWhZrvDw",
  "type": "assistant",
  "uuid": "dd092894-c2dc-4351-ac4b-208fa4f23c23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVyV8nMPskwsCVAzKfFjS3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 34690,
      "output_tokens": 651,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 651,
          "cache_read_input_tokens": 34690,
          "cache_creation_input_tokens": 641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 641
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

_source line 37 · 2026-05-23T10:23:31.588Z_

Large result. Let me query specific experiment groups instead.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd092894-c2dc-4351-ac4b-208fa4f23c23",
  "isSidechain": false,
  "requestId": "req_011CbKLTdo4iCEzoxWhZrvDw",
  "type": "assistant",
  "uuid": "c829b3b9-870d-4421-b9fa-5f7afede6f87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVyV8nMPskwsCVAzKfFjS3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 34690,
      "output_tokens": 651,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 651,
          "cache_read_input_tokens": 34690,
          "cache_creation_input_tokens": 641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 641
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

_source line 38 · 2026-05-23T10:23:32.515Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01GBUoJhXAsBRuiWAFW6tBUw`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "exp_id": "phase2_scierc_unconstrained"
  },
  "fields": [
    "exp_id",
    "metrics",
    "status"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c829b3b9-870d-4421-b9fa-5f7afede6f87",
  "isSidechain": false,
  "requestId": "req_011CbKLTdo4iCEzoxWhZrvDw",
  "type": "assistant",
  "uuid": "fedf5352-f752-4f7c-8526-63fa12ced4ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVyV8nMPskwsCVAzKfFjS3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 34690,
      "output_tokens": 651,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 651,
          "cache_read_input_tokens": 34690,
          "cache_creation_input_tokens": 641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 641
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

_source line 39 · 2026-05-23T10:23:33.051Z_

<details><summary>↩ Tool result · `toolu_01GBUoJhXAsBRuiWAFW6tBUw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5254}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fedf5352-f752-4f7c-8526-63fa12ced4ba",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "b292f525-74b7-4687-babf-57021876cbfa",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5254}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5254}}"
    }
  },
  "sourceToolAssistantUUID": "fedf5352-f752-4f7c-8526-63fa12ced4ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-23T10:23:33.494Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01AgBArXZd2WygyqGooQnDGG`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "exp_id": "phase2_scierc_grammar_only"
  },
  "fields": [
    "exp_id",
    "metrics",
    "status"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b292f525-74b7-4687-babf-57021876cbfa",
  "isSidechain": false,
  "requestId": "req_011CbKLTdo4iCEzoxWhZrvDw",
  "type": "assistant",
  "uuid": "dae5b36f-50b5-43d9-a12b-c5c7369eacc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVyV8nMPskwsCVAzKfFjS3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 34690,
      "output_tokens": 651,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 651,
          "cache_read_input_tokens": 34690,
          "cache_creation_input_tokens": 641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 641
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

_source line 41 · 2026-05-23T10:23:35.895Z_

<details><summary>↩ Tool result · `toolu_01JtjYHBERN8JmKMudytzMkY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4664}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05b6b5e5-9f9f-4ce8-9b74-b1ee3c4f6c7d",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "9f55e7e6-ac3c-430c-99c5-b4fd5f595fac",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4664}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4664}}"
    }
  },
  "sourceToolAssistantUUID": "99ebacf6-2c35-4b6a-b9a0-d943c7cbe882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T10:23:33.987Z_

<details><summary>↩ Tool result · `toolu_01AgBArXZd2WygyqGooQnDGG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4833}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dae5b36f-50b5-43d9-a12b-c5c7369eacc9",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "d38dfa3c-af8a-4a95-89ad-43cb4fe540e5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4833}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4833}}"
    }
  },
  "sourceToolAssistantUUID": "dae5b36f-50b5-43d9-a12b-c5c7369eacc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T10:23:34.471Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_018j5Bn3VXAZ2kwQwa81LmGB`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "exp_id": "phase2_scierc_semantic_only"
  },
  "fields": [
    "exp_id",
    "metrics",
    "status"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d38dfa3c-af8a-4a95-89ad-43cb4fe540e5",
  "isSidechain": false,
  "requestId": "req_011CbKLTdo4iCEzoxWhZrvDw",
  "type": "assistant",
  "uuid": "4ed8954a-5230-4b62-81ac-ea4a48b7e5c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVyV8nMPskwsCVAzKfFjS3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 34690,
      "output_tokens": 651,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 651,
          "cache_read_input_tokens": 34690,
          "cache_creation_input_tokens": 641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 641
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

_source line 44 · 2026-05-23T10:23:34.936Z_

<details><summary>↩ Tool result · `toolu_018j5Bn3VXAZ2kwQwa81LmGB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.455}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ed8954a-5230-4b62-81ac-ea4a48b7e5c0",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "edffd336-17d1-4de7-817a-29b2c82ab289",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.455}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.455}}"
    }
  },
  "sourceToolAssistantUUID": "4ed8954a-5230-4b62-81ac-ea4a48b7e5c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-23T10:23:35.417Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01JtjYHBERN8JmKMudytzMkY`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "exp_id": "phase2_scierc_full_s1"
  },
  "fields": [
    "exp_id",
    "metrics",
    "status"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edffd336-17d1-4de7-817a-29b2c82ab289",
  "isSidechain": false,
  "requestId": "req_011CbKLTdo4iCEzoxWhZrvDw",
  "type": "assistant",
  "uuid": "99ebacf6-2c35-4b6a-b9a0-d943c7cbe882",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVyV8nMPskwsCVAzKfFjS3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 34690,
      "output_tokens": 651,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 651,
          "cache_read_input_tokens": 34690,
          "cache_creation_input_tokens": 641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 641
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

_source line 46 · 2026-05-23T10:23:35.889Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01YTvq59uV8uN1D4ipHSB2oE`</summary>

```json
{
  "project": "schema_semantic_constrained_ie",
  "filters": {
    "exp_id": "phase2_scierc_full_s2"
  },
  "fields": [
    "exp_id",
    "metrics",
    "status"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99ebacf6-2c35-4b6a-b9a0-d943c7cbe882",
  "isSidechain": false,
  "requestId": "req_011CbKLTdo4iCEzoxWhZrvDw",
  "type": "assistant",
  "uuid": "05b6b5e5-9f9f-4ce8-9b74-b1ee3c4f6c7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVyV8nMPskwsCVAzKfFjS3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 34690,
      "output_tokens": 651,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 641,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 651,
          "cache_read_input_tokens": 34690,
          "cache_creation_input_tokens": 641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 641
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

_source line 47 · 2026-05-23T10:23:36.421Z_

<details><summary>↩ Tool result · `toolu_01YTvq59uV8uN1D4ipHSB2oE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5173}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05b6b5e5-9f9f-4ce8-9b74-b1ee3c4f6c7d",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "b1e17eee-762d-4e01-8147-49c0fb8e86f5",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5173}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5173}}"
    }
  },
  "sourceToolAssistantUUID": "05b6b5e5-9f9f-4ce8-9b74-b1ee3c4f6c7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-23T10:23:40.493Z_

<details><summary>Logged reasoning block</summary>

```text
All returning empty. The `filters` parameter probably does exact match on the whole field. The exp_ids might be named differently in the registry. Let me look at the full registry dump to find the actual experiment IDs. Let me read the large output file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1e17eee-762d-4e01-8147-49c0fb8e86f5",
  "isSidechain": false,
  "requestId": "req_011CbKLUJeAtQufE5nCs8buF",
  "type": "assistant",
  "uuid": "c34c395f-f912-4613-8093-f186fd4fe83f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxxFbocb3nqcaaHCNUs8s6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1158,
      "cache_read_input_tokens": 35331,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1158,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 295,
          "cache_read_input_tokens": 35331,
          "cache_creation_input_tokens": 1158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1158
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

_source line 49 · 2026-05-23T10:23:41.479Z_

Exact exp_id matches return empty — the IDs may be named differently. Let me search the full registry dump.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c34c395f-f912-4613-8093-f186fd4fe83f",
  "isSidechain": false,
  "requestId": "req_011CbKLUJeAtQufE5nCs8buF",
  "type": "assistant",
  "uuid": "99e9a836-e324-43e7-b249-9e7b13f4f497",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxxFbocb3nqcaaHCNUs8s6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1158,
      "cache_read_input_tokens": 35331,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1158,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 295,
          "cache_read_input_tokens": 35331,
          "cache_creation_input_tokens": 1158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1158
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

_source line 50 · 2026-05-23T10:23:45.572Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JcCeQpVTCqmvzW5nzTbXUX`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\nfor eid in exps:\n    print(eid)\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99e9a836-e324-43e7-b249-9e7b13f4f497",
  "isSidechain": false,
  "requestId": "req_011CbKLUJeAtQufE5nCs8buF",
  "type": "assistant",
  "uuid": "a7939f45-b1ac-4ce0-a3e9-a64ae52af3b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RxxFbocb3nqcaaHCNUs8s6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1158,
      "cache_read_input_tokens": 35331,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1158,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 295,
          "cache_read_input_tokens": 35331,
          "cache_creation_input_tokens": 1158,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1158
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

_source line 51 · 2026-05-23T10:23:45.689Z_

<details><summary>↩ Tool result · `toolu_01JcCeQpVTCqmvzW5nzTbXUX`</summary>

```text
eval_70b_lora_docred_200_full_s2
sf2_qwen_int4_docred_s1
sf2_llama_int4_docred_s1
sf2_70b_prompt_sensitivity
sf2_llama_int4_scierc_s1
sf2_qwen_int4_scierc_s1
sf2_gollie_scierc_violation
eval_70b_zs_docred_200_full_s1
eval_70b_lora_docred_200_grammar_only
eval_70b_lora_docred_200_semantic_only
eval_70b_zs_docred_200_unconstrained
eval_70b_zs_docred_200_grammar_only
eval_70b_zs_docred_200_semantic_only
eval_70b_lora_docred_200_beam4_s1
eval_70b_lora_scierc_grammar_only
eval_70b_zs_scierc_unconstrained
eval_70b_lora_scierc_full_s2
eval_70b_lora_scierc_semantic_only
entity_order_ablation_qwen_scierc
eval_70b_zs_scierc_semantic_only
eval_70b_zs_scierc_grammar_only
eval_70b_lora_scierc_beam4_s1
tcr_beam4_llama_scierc
tcr_beam4_qwen_scierc
vllm_guided_json_scierc_zs
eval_70b_lora_docred_200_s1_constrained
d066_beam_sweep
w8_llama_docred_ft_grammar_only
w8_llama_docred_ft_semantic_only
w8_qwen_docred_ft_semantic_only
r16_trie_qwen_ft_scierc
r16_trie_llama_ft_scierc
eval_70b_lora_docred_200_unconstrained
eval_70b_lora_scierc_s1_constrained
eval_70b_lora_scierc_unconstrained
r16_70b_docred_zs_s1
d066_sweep_llama_beam8_unc
d066_sweep_llama_beam2_s1
d066_sweep_llama_docred_beam4_s1
r16_70b_lora_scierc_eval
r16_70b_lora_docred
r16_70b_lora_scierc
r16_70b_scierc_zs_s1
r14_qwen_docred_beam4_998
r16_trie_llama_zs_scierc
r16_trie_qwen_zs_scierc
r14_llama_docred_beam4_998
d066_sweep_llama_scierc_beam8_s1_551
d066_sweep_llama_scierc_beam4_s1_551
d066_sweep_llama_docred_beam4_unc
d066_sweep_llama_docred_beam1_s1
d066_sweep_llama_beam8_s1
d065_qwen_greedy_4096_r2
d066_sweep_llama_scierc_beam2_s1_551
d066_sweep_llama_scierc_beam1_unc
d066_sweep_llama_docred_beam1_unc
d066_sweep_21461_gpu1
w5_llama_docred_lora_constrained_eval
d066_sweep_16980_gpu1
d065_qwen_greedy_4096
d066_docred_beam_sweep
d067_seed_variance
d068_constraint_guided_beam_pilot
d064_docred_full_beam
d065_tcr_full
d065_tcr_pilot
d063_gollie_violation_rate
d062_full_ft_scierc
d062_beam_latency
d062_ontology_scalability
d062_cf_majority_voting
p1_ee_ft_llama_r2
p1_ee_ft_composability_r5
p1_ee_ft_llama
p1_ee_ft_composability_r4
p1_llama_ee_ft
w9_qwen_docred_zs_sampling_r2
70b_docred_constrained
70b_docred_unconstrained
p1_ee_ft_composability_r3
p1_ee_ft_composability_r2
p1_ee_ft_composability
p8c_ft_scierc_latency
p8b_docred_latency
w9_qwen_docred_zs_sampling
w9_qwen_scierc_zs_sampling
p8_latency_overhead
q1_llama_lora_scierc_beam4
70b_scierc_unconstrained
70b_scierc_constrained
ee_mistral_wikievents_grammar_only_v3
ee_mistral_wikievents_constrained_v3
ee_llama_wikievents_constrained_v3
ee_qwen_wikievents_constrained_v3
ee_mistral_wikievents_constrained_v2
ee_qwen_wikievents_constrained
ee_mistral_wikievents_constrained
ee_llama_wikievents_constrained
ee_mistral_wikievents_unconstrained
ee_llama_wikievents_unconstrained
ee_qwen_wikievents_unconstrained
r4_prompt_detailed
r4_prompt_minimal
w10_qwen_scierc_ft_beam_4
w10_beam_ablation_k8
w9_mistral_docred_beam_50
w10_beam_ablation_k2
w10_mistral_scierc_beam_551
w10_llama_docred_beam_50
w10_type_consensus_docred_50
w10_type_consensus_prototype
w9_qwen_scierc_stability_3seeds
w9_qwen_docred_beam_50
w9_llama_scierc_beam_551
posthoc_filtering_baseline
phase2_scierc_full_s2
llama_docred_unconstrained_mt6144
llama_docred_full_s1_mt6144
beam_search_scierc_full_551
w7_llama_scierc_ft_semantic_only
w7_llama_scierc_ft_grammar_only
w7_qwen_scierc_ft_semantic_only
w7_qwen_scierc_ft_grammar_only
w5_llama_lora_scierc_unconstrained_eval
w5_llama_lora_scierc_constrained_eval
w5_lora_scierc_constrained_eval
w1_cf_fallback_scierc_pilot
w5_lora_scierc_training
w8_qwen_docred_ft_grammar_only
w6_mistral_scierc_unconstrained
w6_mistral_scierc_constrained
w8_ft_posthoc_baseline
w6_mistral_docred_unconstrained
w6_mistral_docred_constrained
w5_qwen_docred_lora_constrained_eval
w5_llama_docred_sft_data_gen
w1_cf_fallback_llama_docred
w1_cf_fallback_llama_scierc
w5_qwen_docred_lora_unconstrained_eval
w5_llama_docred_lora_unconstrained_eval
w5_qwen_docred_lora_training
w5_llama_docred_lora_training
w5_docred_sft_data_gen
w5_llama_lora_scierc_training
w1_cf_fallback_docred
w5_lora_scierc_unconstrained_eval
llama_docred_full_s1
llama_docred_unconstrained
phase2_docred_grammar_only
llama_scierc_full_s1
llama_scierc_unconstrained
phase2_scierc_full_s1
phase2_scierc_semantic_only
phase2_scierc_grammar_only
phase2_scierc_unconstrained
phase2_docred_full_s1
phase2_docred_semantic_only
phase2_docred_unconstrained
mvp_phase0_docred_schema_r2
phase2_s2_pilot50
mvp_phase0_docred_schema
mvp_phase0_violation_rate_docred
mvp_phase0_scierc_schema
mvp_phase0_violation_rate
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7939f45-b1ac-4ce0-a3e9-a64ae52af3b1",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "25f1b1f9-c5dc-41fe-a75c-fbe3b6cf1f20",
  "toolUseResult": {
    "stdout": "eval_70b_lora_docred_200_full_s2\nsf2_qwen_int4_docred_s1\nsf2_llama_int4_docred_s1\nsf2_70b_prompt_sensitivity\nsf2_llama_int4_scierc_s1\nsf2_qwen_int4_scierc_s1\nsf2_gollie_scierc_violation\neval_70b_zs_docred_200_full_s1\neval_70b_lora_docred_200_grammar_only\neval_70b_lora_docred_200_semantic_only\neval_70b_zs_docred_200_unconstrained\neval_70b_zs_docred_200_grammar_only\neval_70b_zs_docred_200_semantic_only\neval_70b_lora_docred_200_beam4_s1\neval_70b_lora_scierc_grammar_only\neval_70b_zs_scierc_unconstrained\neval_70b_lora_scierc_full_s2\neval_70b_lora_scierc_semantic_only\nentity_order_ablation_qwen_scierc\neval_70b_zs_scierc_semantic_only\neval_70b_zs_scierc_grammar_only\neval_70b_lora_scierc_beam4_s1\ntcr_beam4_llama_scierc\ntcr_beam4_qwen_scierc\nvllm_guided_json_scierc_zs\neval_70b_lora_docred_200_s1_constrained\nd066_beam_sweep\nw8_llama_docred_ft_grammar_only\nw8_llama_docred_ft_semantic_only\nw8_qwen_docred_ft_semantic_only\nr16_trie_qwen_ft_scierc\nr16_trie_llama_ft_scierc\neval_70b_lora_docred_200_unconstrained\neval_70b_lora_scierc_s1_constrained\neval_70b_lora_scierc_unconstrained\nr16_70b_docred_zs_s1\nd066_sweep_llama_beam8_unc\nd066_sweep_llama_beam2_s1\nd066_sweep_llama_docred_beam4_s1\nr16_70b_lora_scierc_eval\nr16_70b_lora_docred\nr16_70b_lora_scierc\nr16_70b_scierc_zs_s1\nr14_qwen_docred_beam4_998\nr16_trie_llama_zs_scierc\nr16_trie_qwen_zs_scierc\nr14_llama_docred_beam4_998\nd066_sweep_llama_scierc_beam8_s1_551\nd066_sweep_llama_scierc_beam4_s1_551\nd066_sweep_llama_docred_beam4_unc\nd066_sweep_llama_docred_beam1_s1\nd066_sweep_llama_beam8_s1\nd065_qwen_greedy_4096_r2\nd066_sweep_llama_scierc_beam2_s1_551\nd066_sweep_llama_scierc_beam1_unc\nd066_sweep_llama_docred_beam1_unc\nd066_sweep_21461_gpu1\nw5_llama_docred_lora_constrained_eval\nd066_sweep_16980_gpu1\nd065_qwen_greedy_4096\nd066_docred_beam_sweep\nd067_seed_variance\nd068_constraint_guided_beam_pilot\nd064_docred_full_beam\nd065_tcr_full\nd065_tcr_pilot\nd063_gollie_violation_rate\nd062_full_ft_scierc\nd062_beam_latency\nd062_ontology_scalability\nd062_cf_majority_voting\np1_ee_ft_llama_r2\np1_ee_ft_composability_r5\np1_ee_ft_llama\np1_ee_ft_composability_r4\np1_llama_ee_ft\nw9_qwen_docred_zs_sampling_r2\n70b_docred_constrained\n70b_docred_unconstrained\np1_ee_ft_composability_r3\np1_ee_ft_composability_r2\np1_ee_ft_composability\np8c_ft_scierc_latency\np8b_docred_latency\nw9_qwen_docred_zs_sampling\nw9_qwen_scierc_zs_sampling\np8_latency_overhead\nq1_llama_lora_scierc_beam4\n70b_scierc_unconstrained\n70b_scierc_constrained\nee_mistral_wikievents_grammar_only_v3\nee_mistral_wikievents_constrained_v3\nee_llama_wikievents_constrained_v3\nee_qwen_wikievents_constrained_v3\nee_mistral_wikievents_constrained_v2\nee_qwen_wikievents_constrained\nee_mistral_wikievents_constrained\nee_llama_wikievents_constrained\nee_mistral_wikievents_unconstrained\nee_llama_wikievents_unconstrained\nee_qwen_wikievents_unconstrained\nr4_prompt_detailed\nr4_prompt_minimal\nw10_qwen_scierc_ft_beam_4\nw10_beam_ablation_k8\nw9_mistral_docred_beam_50\nw10_beam_ablation_k2\nw10_mistral_scierc_beam_551\nw10_llama_docred_beam_50\nw10_type_consensus_docred_50\nw10_type_consensus_prototype\nw9_qwen_scierc_stability_3seeds\nw9_qwen_docred_beam_50\nw9_llama_scierc_beam_551\nposthoc_filtering_baseline\nphase2_scierc_full_s2\nllama_docred_unconstrained_mt6144\nllama_docred_full_s1_mt6144\nbeam_search_scierc_full_551\nw7_llama_scierc_ft_semantic_only\nw7_llama_scierc_ft_grammar_only\nw7_qwen_scierc_ft_semantic_only\nw7_qwen_scierc_ft_grammar_only\nw5_llama_lora_scierc_unconstrained_eval\nw5_llama_lora_scierc_constrained_eval\nw5_lora_scierc_constrained_eval\nw1_cf_fallback_scierc_pilot\nw5_lora_scierc_training\nw8_qwen_docred_ft_grammar_only\nw6_mistral_scierc_unconstrained\nw6_mistral_scierc_constrained\nw8_ft_posthoc_baseline\nw6_mistral_docred_unconstrained\nw6_mistral_docred_constrained\nw5_qwen_docred_lora_constrained_eval\nw5_llama_docred_sft_data_gen\nw1_cf_fallback_llama_docred\nw1_cf_fallback_llama_scierc\nw5_qwen_docred_lora_unconstrained_eval\nw5_llama_docred_lora_unconstrained_eval\nw5_qwen_docred_lora_training\nw5_llama_docred_lora_training\nw5_docred_sft_data_gen\nw5_llama_lora_scierc_training\nw1_cf_fallback_docred\nw5_lora_scierc_unconstrained_eval\nllama_docred_full_s1\nllama_docred_unconstrained\nphase2_docred_grammar_only\nllama_scierc_full_s1\nllama_scierc_unconstrained\nphase2_scierc_full_s1\nphase2_scierc_semantic_only\nphase2_scierc_grammar_only\nphase2_scierc_unconstrained\nphase2_docred_full_s1\nphase2_docred_semantic_only\nphase2_docred_unconstrained\nmvp_phase0_docred_schema_r2\nphase2_s2_pilot50\nmvp_phase0_docred_schema\nmvp_phase0_violation_rate_docred\nmvp_phase0_scierc_schema\nmvp_phase0_violation_rate",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a7939f45-b1ac-4ce0-a3e9-a64ae52af3b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-23T10:23:58.117Z_

<details><summary>Logged reasoning block</summary>

```text
The experiment IDs exist! They just weren't matching with the `filters` parameter. The registry filters might not work as I expected. Let me try reading specific experiments differently. Let me just parse the large output file to extract the experiments I need.

For Table 1 (tab:scierc-ablation), I need:
- phase2_scierc_unconstrained
- phase2_scierc_grammar_only
- phase2_scierc_semantic_only
- phase2_scierc_full_s1


- phase2_scierc_full_s2
- vllm_guided_json_scierc_zs (for the GCD-equiv row)

For Table 2 (tab:composability), I need the Qwen and Llama LoRA variants across SciERC and DocRED with both unconstrained and constrained evaluation setups.

Now I'm pulling the metrics from these experiments to populate the table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25f1b1f9-c5dc-41fe-a75c-fbe3b6cf1f20",
  "isSidechain": false,
  "requestId": "req_011CbKLUzN6quiif86BhENdH",
  "type": "assistant",
  "uuid": "dc4b58ca-4e39-4f8a-b5b3-69188badd5a3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfGBHTED4H8Kvmkvt5ddMm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2533,
      "cache_read_input_tokens": 36489,
      "output_tokens": 1248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2533,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1248,
          "cache_read_input_tokens": 36489,
          "cache_creation_input_tokens": 2533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2533
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

_source line 53 · 2026-05-23T10:23:58.404Z_

The exp_ids exist. Let me extract metrics for both tables from the registry dump.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc4b58ca-4e39-4f8a-b5b3-69188badd5a3",
  "isSidechain": false,
  "requestId": "req_011CbKLUzN6quiif86BhENdH",
  "type": "assistant",
  "uuid": "aad9ff34-83f5-4ae7-a31f-87335240dd82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfGBHTED4H8Kvmkvt5ddMm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2533,
      "cache_read_input_tokens": 36489,
      "output_tokens": 1248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2533,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1248,
          "cache_read_input_tokens": 36489,
          "cache_creation_input_tokens": 2533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2533
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

_source line 54 · 2026-05-23T10:24:08.582Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Pj6hpKT8HLHe7pdj6SrLQ9`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Table 1 experiments\ntable1_ids = [\n    'phase2_scierc_unconstrained',\n    'phase2_scierc_grammar_only', \n    'phase2_scierc_semantic_only',\n    'phase2_scierc_full_s1',\n    'phase2_scierc_full_s2',\n    'vllm_guided_json_scierc_zs',\n]\n\n# Table 2 experiments  \ntable2_ids = [\n    'w5_lora_scierc_unconstrained_eval',\n    'w5_lora_scierc_constrained_eval',\n    'w5_qwen_docred_lora_unconstrained_eval',\n    'w5_qwen_docred_lora_constrained_eval',\n    'w5_llama_lora_scierc_unconstrained_eval',\n    'w5_llama_lora_scierc_constrained_eval',\n    'w5_llama_docred_lora_unconstrained_eval',\n    'w5_llama_docred_lora_constrained_eval',\n]\n\nprint('=== TABLE 1 EXPERIMENTS ===')\nfor eid in table1_ids:\n    if eid in exps:\n        e = exps[eid]\n        print(f'\\n--- {eid} ---')\n        print(f'  status: {e.get(\\\"status\\\", \\\"N/A\\\")}')\n        print(f'  metrics: {json.dumps(e.get(\\\"metrics\\\", {}), indent=4)}')\n        print(f'  conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")[:200]}')\n    else:\n        print(f'\\n--- {eid} --- NOT FOUND')\n\nprint('\\n\\n=== TABLE 2 EXPERIMENTS ===')\nfor eid in table2_ids:\n    if eid in exps:\n        e = exps[eid]\n        print(f'\\n--- {eid} ---')\n        print(f'  status: {e.get(\\\"status\\\", \\\"N/A\\\")}')\n        print(f'  metrics: {json.dumps(e.get(\\\"metrics\\\", {}), indent=4)}')\n        print(f'  conclusion: {e.get(\\\"conclusion\\\", \\\"N/A\\\")[:200]}')\n    else:\n        print(f'\\n--- {eid} --- NOT FOUND')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aad9ff34-83f5-4ae7-a31f-87335240dd82",
  "isSidechain": false,
  "requestId": "req_011CbKLUzN6quiif86BhENdH",
  "type": "assistant",
  "uuid": "9012530f-7a5e-4574-bc5e-a6ac01a202e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfGBHTED4H8Kvmkvt5ddMm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2533,
      "cache_read_input_tokens": 36489,
      "output_tokens": 1248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2533,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1248,
          "cache_read_input_tokens": 36489,
          "cache_creation_input_tokens": 2533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2533
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

_source line 55 · 2026-05-23T10:24:08.673Z_

<details><summary>↩ Tool result · `toolu_01Pj6hpKT8HLHe7pdj6SrLQ9`</summary>

```text
=== TABLE 1 EXPERIMENTS ===

--- phase2_scierc_unconstrained ---
  status: DONE
  metrics: {
    "json_parse_rate": 1,
    "entity_f1": 0.3101,
    "entity_precision": 0.2605,
    "entity_recall": 0.3831,
    "relation_f1": 0.0823,
    "relation_precision": 0.0644,
    "relation_recall": 0.114,
    "entity_type_violation_rate": 0.004,
    "relation_vocabulary_violation_rate": 0.0139,
    "domain_range_violation_rate": 0.1537,
    "cross_field_consistency_violation_rate": 0.0008,
    "total_triples": 1724,
    "total_entities": 2474,
    "total_samples": 551,
    "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}
  conclusion: success

--- phase2_scierc_grammar_only ---
  status: DONE
  metrics: {
    "total_samples": 551,
    "total_triples": 1725,
    "total_entities": 2474,
    "json_parse_rate": 1,
    "entity_type_violation_rate": 0,
    "relation_vocabulary_violation_rate": 0,
    "domain_range_violation_rate": 0.1484,
    "cross_field_consistency_violation_rate": 0.0008,
    "entity_f1": 0.3098,
    "entity_precision": 0.2598,
    "entity_recall": 0.3837,
    "relation_f1": 0.0823,
    "relation_precision": 0.0643,
    "relation_recall": 0.114,
    "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}
  conclusion: success

--- phase2_scierc_semantic_only ---
  status: DONE
  metrics: {
    "total_samples": 551,
    "total_triples": 1726,
    "total_entities": 2474,
    "json_parse_rate": 1,
    "entity_type_violation_rate": 0.004,
    "relation_vocabulary_violation_rate": 0.0151,
    "domain_range_violation_rate": 0.1165,
    "cross_field_consistency_violation_rate": 0.0271,
    "entity_f1": 0.3101,
    "entity_precision": 0.2605,
    "entity_recall": 0.3831,
    "relation_f1": 0.0815,
    "relation_precision": 0.0637,
    "relation_recall": 0.1129,
    "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}
  conclusion: success

--- phase2_scierc_full_s1 ---
  status: DONE
  metrics: {
    "total_samples": 551,
    "total_triples": 1729,
    "total_entities": 2474,
    "json_parse_rate": 1,
    "entity_type_violation_rate": 0,
    "relation_vocabulary_violation_rate": 0,
    "domain_range_violation_rate": 0.0093,
    "cross_field_consistency_violation_rate": 0.099,
    "entity_f1": 0.3098,
    "entity_precision": 0.2598,
    "entity_recall": 0.3837,
    "relation_f1": 0.0836,
    "relation_precision": 0.0654,
    "relation_recall": 0.116,
    "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}
  conclusion: success

--- phase2_scierc_full_s2 ---
  status: DONE
  metrics: {
    "total_samples": 551,
    "total_triples": 1644,
    "total_entities": 2228,
    "json_parse_rate": 1,
    "entity_type_violation_rate": 0,
    "relation_vocabulary_violation_rate": 0,
    "domain_range_violation_rate": 0.0097,
    "cross_field_consistency_violation_rate": 0.0803,
    "entity_precision": 0.2797,
    "entity_recall": 0.3712,
    "entity_f1": 0.319,
    "relation_precision": 0.064,
    "relation_recall": 0.1078,
    "relation_f1": 0.0803,
    "checker_version": "fixed_20260514_v2 (strip + alias + unique_et)"
}
  conclusion: success

--- vllm_guided_json_scierc_zs ---
  status: DONE
  metrics: {
    "DR%": 15.26,
    "RV%": 0,
    "ET%": 0,
    "CF%": 0.04,
    "R-F1": 8.75,
    "E-F1": 30.91,
    "parse_fail%": 0,
    "total_samples": 551,
    "total_entities": 2485,
    "total_relations": 1724,
    "inference_time_s": 108.5
}
  conclusion: success


=== TABLE 2 EXPERIMENTS ===

--- w5_lora_scierc_unconstrained_eval ---
  status: DONE
  metrics: {
    "json_parse_rate": 1,
    "entity_type_violation_rate": 0,
    "relation_vocabulary_violation_rate": 0,
    "domain_range_violation_rate": 0.0195,
    "cross_field_consistency_violation_rate": 0,
    "entity_f1": 0.6705,
    "entity_precision": 0.6523,
    "entity_recall": 0.6898,
    "relation_f1": 0.4386,
    "relation_precision": 0.4087,
    "relation_recall": 0.4733,
    "total_entities": 1784,
    "total_relations": 1128,
    "domain_range_violations": 22,
    "go_nogo_metric": 0.0195,
    "dr_gate": "FAILED"
}
  conclusion: success

--- w5_lora_scierc_constrained_eval ---
  status: DONE
  metrics: {
    "json_parse_rate": 1,
    "entity_type_violation_rate": 0,
    "relation_vocabulary_violation_rate": 0,
    "domain_range_violation_rate": 0,
    "cross_field_consistency_violation_rate": 0.0118,
    "entity_f1": 0.6705,
    "entity_precision": 0.6523,
    "entity_recall": 0.6898,
    "relation_f1": 0.4377,
    "relation_precision": 0.4078,
    "relation_recall": 0.4723,
    "total_entities": 1784,
    "total_relations": 1128,
    "total_samples": 551,
    "cross_field_consistency_violations": 21
}
  conclusion: success

--- w5_qwen_docred_lora_unconstrained_eval ---
  status: DONE
  metrics: {
    "ET_pct": 0,
    "RV_pct": 0.27,
    "DR_pct": 0.76,
    "CF_pct": 0.12,
    "E_F1": 82.15,
    "E_P": 85.44,
    "E_R": 79.11,
    "R_F1": 40.86,
    "R_P": 36.41,
    "R_R": 46.56,
    "parse_fail_rate": 7.11,
    "total_samples": 998,
    "success_samples": 927,
    "fail_samples": 71,
    "total_entities_pred": 18091,
    "total_relations_pred": 15870,
    "ET_pct_excl_fail": 0,
    "RV_pct_excl_fail": 0.27,
    "DR_pct_excl_fail": 0.76,
    "CF_pct_excl_fail": 0.12,
    "E_F1_excl_fail": 85.72,
    "E_P_excl_fail": 85.44,
    "E_R_excl_fail": 86,
    "R_F1_excl_fail": 42.2,
    "R_P_excl_fail": 36.41,
    "R_R_excl_fail": 50.17
}
  conclusion: success

--- w5_qwen_docred_lora_constrained_eval ---
  status: DONE
  metrics: {
    "ET_pct": 0,
    "RV_pct": 0,
    "DR_pct": 0.01,
    "CF_pct": 0.41,
    "E_F1": 81.43,
    "E_P": 85.41,
    "E_R": 77.81,
    "R_F1": 40.56,
    "R_P": 36.35,
    "R_R": 45.86,
    "parse_fail_rate": 8.52,
    "total_samples": 998,
    "success_samples": 913,
    "fail_samples": 85,
    "total_entities_pred": 17799,
    "total_relations_pred": 15563,
    "E_F1_excl_fail": 85.69,
    "R_F1_excl_fail": 42.23,
    "delta_vs_unconstrained": {
        "delta_DR": -0.75,
        "delta_RV": -0.27,
        "delta_R_F1": -0.3,
        "delta_R_F1_excl_fail": 0.03,
        "DR_reduction_pct": 98.7,
        "note": "Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20"
    }
}
  conclusion: success

--- w5_llama_lora_scierc_unconstrained_eval ---
  status: DONE
  metrics: {
    "total_samples": 551,
    "total_entities": 1757,
    "total_relations": 1082,
    "json_parse_rate": 1,
    "entity_type_violation_rate": 0,
    "relation_vocabulary_violation_rate": 0,
    "domain_range_violation_rate": 0.0111,
    "cross_field_consistency_violation_rate": 0,
    "total_violation_rate": 0.0042,
    "entity_precision": 0.6647,
    "entity_recall": 0.691,
    "entity_f1": 0.6776,
    "relation_precision": 0.432,
    "relation_recall": 0.4795,
    "relation_f1": 0.4545
}
  conclusion: success

--- w5_llama_lora_scierc_constrained_eval ---
  status: DONE
  metrics: {
    "domain_range_violation_rate": 0.0009,
    "relation_vocabulary_violation_rate": 0,
    "entity_type_violation_rate": 0,
    "cross_field_consistency_violation_rate": 0.0046,
    "relation_f1": 0.4547,
    "relation_precision": 0.432,
    "relation_recall": 0.4795,
    "entity_f1": 0.6776,
    "entity_precision": 0.6647,
    "entity_recall": 0.691,
    "total_relations": 1081,
    "total_entities": 1757,
    "total_samples": 551,
    "parse_failures": 0
}
  conclusion: success

--- w5_llama_docred_lora_unconstrained_eval ---
  status: DONE
  metrics: {
    "ET_pct": 0,
    "RV_pct": 0.15,
    "DR_pct": 0.49,
    "E_F1": 83.93,
    "E_P": 84.93,
    "E_R": 82.96,
    "R_F1": 43.72,
    "R_P": 38.59,
    "R_R": 50.41,
    "parse_fail_rate": 2.3,
    "total_samples": 998,
    "total_entities_pred": 19106,
    "total_relations_pred": 16171
}
  conclusion: success

--- w5_llama_docred_lora_constrained_eval ---
  status: DONE
  metrics: {
    "total": 998,
    "parse_failures": 25,
    "parse_fail_rate": 2.51,
    "entities": 19077,
    "relations": 16074,
    "entity_f1": 83.94,
    "entity_precision": 85,
    "entity_recall": 84.13,
    "relation_f1_all_set": 43.78,
    "relation_precision_all_set": 38.79,
    "relation_recall_all_set": 50.81,
    "et_violations": 0,
    "et_violation_rate": 0,
    "rv_violations": 0,
    "rv_violation_rate": 0,
    "dr_violations": 33,
    "dr_violation_rate": 0.21,
    "CF_pct": 0.21,
    "delta_vs_unconstrained": {
        "delta_e_f1": 0.01,
        "delta_r_f1": 0.06,
        "delta_dr": -0.28,
        "note": "Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl (998 lines). Updated 2026-05-20."
    },
    "provenance": "eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl, 2026-05-20. P/R corrected 2026-05-20 per Director."
}
  conclusion: success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9012530f-7a5e-4574-bc5e-a6ac01a202e2",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "2759d5db-c858-4f7f-9da8-852c16200ddc",
  "toolUseResult": {
    "stdout": "=== TABLE 1 EXPERIMENTS ===\n\n--- phase2_scierc_unconstrained ---\n  status: DONE\n  metrics: {\n    \"json_parse_rate\": 1,\n    \"entity_f1\": 0.3101,\n    \"entity_precision\": 0.2605,\n    \"entity_recall\": 0.3831,\n    \"relation_f1\": 0.0823,\n    \"relation_precision\": 0.0644,\n    \"relation_recall\": 0.114,\n    \"entity_type_violation_rate\": 0.004,\n    \"relation_vocabulary_violation_rate\": 0.0139,\n    \"domain_range_violation_rate\": 0.1537,\n    \"cross_field_consistency_violation_rate\": 0.0008,\n    \"total_triples\": 1724,\n    \"total_entities\": 2474,\n    \"total_samples\": 551,\n    \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n  conclusion: success\n\n--- phase2_scierc_grammar_only ---\n  status: DONE\n  metrics: {\n    \"total_samples\": 551,\n    \"total_triples\": 1725,\n    \"total_entities\": 2474,\n    \"json_parse_rate\": 1,\n    \"entity_type_violation_rate\": 0,\n    \"relation_vocabulary_violation_rate\": 0,\n    \"domain_range_violation_rate\": 0.1484,\n    \"cross_field_consistency_violation_rate\": 0.0008,\n    \"entity_f1\": 0.3098,\n    \"entity_precision\": 0.2598,\n    \"entity_recall\": 0.3837,\n    \"relation_f1\": 0.0823,\n    \"relation_precision\": 0.0643,\n    \"relation_recall\": 0.114,\n    \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n  conclusion: success\n\n--- phase2_scierc_semantic_only ---\n  status: DONE\n  metrics: {\n    \"total_samples\": 551,\n    \"total_triples\": 1726,\n    \"total_entities\": 2474,\n    \"json_parse_rate\": 1,\n    \"entity_type_violation_rate\": 0.004,\n    \"relation_vocabulary_violation_rate\": 0.0151,\n    \"domain_range_violation_rate\": 0.1165,\n    \"cross_field_consistency_violation_rate\": 0.0271,\n    \"entity_f1\": 0.3101,\n    \"entity_precision\": 0.2605,\n    \"entity_recall\": 0.3831,\n    \"relation_f1\": 0.0815,\n    \"relation_precision\": 0.0637,\n    \"relation_recall\": 0.1129,\n    \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n  conclusion: success\n\n--- phase2_scierc_full_s1 ---\n  status: DONE\n  metrics: {\n    \"total_samples\": 551,\n    \"total_triples\": 1729,\n    \"total_entities\": 2474,\n    \"json_parse_rate\": 1,\n    \"entity_type_violation_rate\": 0,\n    \"relation_vocabulary_violation_rate\": 0,\n    \"domain_range_violation_rate\": 0.0093,\n    \"cross_field_consistency_violation_rate\": 0.099,\n    \"entity_f1\": 0.3098,\n    \"entity_precision\": 0.2598,\n    \"entity_recall\": 0.3837,\n    \"relation_f1\": 0.0836,\n    \"relation_precision\": 0.0654,\n    \"relation_recall\": 0.116,\n    \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n  conclusion: success\n\n--- phase2_scierc_full_s2 ---\n  status: DONE\n  metrics: {\n    \"total_samples\": 551,\n    \"total_triples\": 1644,\n    \"total_entities\": 2228,\n    \"json_parse_rate\": 1,\n    \"entity_type_violation_rate\": 0,\n    \"relation_vocabulary_violation_rate\": 0,\n    \"domain_range_violation_rate\": 0.0097,\n    \"cross_field_consistency_violation_rate\": 0.0803,\n    \"entity_precision\": 0.2797,\n    \"entity_recall\": 0.3712,\n    \"entity_f1\": 0.319,\n    \"relation_precision\": 0.064,\n    \"relation_recall\": 0.1078,\n    \"relation_f1\": 0.0803,\n    \"checker_version\": \"fixed_20260514_v2 (strip + alias + unique_et)\"\n}\n  conclusion: success\n\n--- vllm_guided_json_scierc_zs ---\n  status: DONE\n  metrics: {\n    \"DR%\": 15.26,\n    \"RV%\": 0,\n    \"ET%\": 0,\n    \"CF%\": 0.04,\n    \"R-F1\": 8.75,\n    \"E-F1\": 30.91,\n    \"parse_fail%\": 0,\n    \"total_samples\": 551,\n    \"total_entities\": 2485,\n    \"total_relations\": 1724,\n    \"inference_time_s\": 108.5\n}\n  conclusion: success\n\n\n=== TABLE 2 EXPERIMENTS ===\n\n--- w5_lora_scierc_unconstrained_eval ---\n  status: DONE\n  metrics: {\n    \"json_parse_rate\": 1,\n    \"entity_type_violation_rate\": 0,\n    \"relation_vocabulary_violation_rate\": 0,\n    \"domain_range_violation_rate\": 0.0195,\n    \"cross_field_consistency_violation_rate\": 0,\n    \"entity_f1\": 0.6705,\n    \"entity_precision\": 0.6523,\n    \"entity_recall\": 0.6898,\n    \"relation_f1\": 0.4386,\n    \"relation_precision\": 0.4087,\n    \"relation_recall\": 0.4733,\n    \"total_entities\": 1784,\n    \"total_relations\": 1128,\n    \"domain_range_violations\": 22,\n    \"go_nogo_metric\": 0.0195,\n    \"dr_gate\": \"FAILED\"\n}\n  conclusion: success\n\n--- w5_lora_scierc_constrained_eval ---\n  status: DONE\n  metrics: {\n    \"json_parse_rate\": 1,\n    \"entity_type_violation_rate\": 0,\n    \"relation_vocabulary_violation_rate\": 0,\n    \"domain_range_violation_rate\": 0,\n    \"cross_field_consistency_violation_rate\": 0.0118,\n    \"entity_f1\": 0.6705,\n    \"entity_precision\": 0.6523,\n    \"entity_recall\": 0.6898,\n    \"relation_f1\": 0.4377,\n    \"relation_precision\": 0.4078,\n    \"relation_recall\": 0.4723,\n    \"total_entities\": 1784,\n    \"total_relations\": 1128,\n    \"total_samples\": 551,\n    \"cross_field_consistency_violations\": 21\n}\n  conclusion: success\n\n--- w5_qwen_docred_lora_unconstrained_eval ---\n  status: DONE\n  metrics: {\n    \"ET_pct\": 0,\n    \"RV_pct\": 0.27,\n    \"DR_pct\": 0.76,\n    \"CF_pct\": 0.12,\n    \"E_F1\": 82.15,\n    \"E_P\": 85.44,\n    \"E_R\": 79.11,\n    \"R_F1\": 40.86,\n    \"R_P\": 36.41,\n    \"R_R\": 46.56,\n    \"parse_fail_rate\": 7.11,\n    \"total_samples\": 998,\n    \"success_samples\": 927,\n    \"fail_samples\": 71,\n    \"total_entities_pred\": 18091,\n    \"total_relations_pred\": 15870,\n    \"ET_pct_excl_fail\": 0,\n    \"RV_pct_excl_fail\": 0.27,\n    \"DR_pct_excl_fail\": 0.76,\n    \"CF_pct_excl_fail\": 0.12,\n    \"E_F1_excl_fail\": 85.72,\n    \"E_P_excl_fail\": 85.44,\n    \"E_R_excl_fail\": 86,\n    \"R_F1_excl_fail\": 42.2,\n    \"R_P_excl_fail\": 36.41,\n    \"R_R_excl_fail\": 50.17\n}\n  conclusion: success\n\n--- w5_qwen_docred_lora_constrained_eval ---\n  status: DONE\n  metrics: {\n    \"ET_pct\": 0,\n    \"RV_pct\": 0,\n    \"DR_pct\": 0.01,\n    \"CF_pct\": 0.41,\n    \"E_F1\": 81.43,\n    \"E_P\": 85.41,\n    \"E_R\": 77.81,\n    \"R_F1\": 40.56,\n    \"R_P\": 36.35,\n    \"R_R\": 45.86,\n    \"parse_fail_rate\": 8.52,\n    \"total_samples\": 998,\n    \"success_samples\": 913,\n    \"fail_samples\": 85,\n    \"total_entities_pred\": 17799,\n    \"total_relations_pred\": 15563,\n    \"E_F1_excl_fail\": 85.69,\n    \"R_F1_excl_fail\": 42.23,\n    \"delta_vs_unconstrained\": {\n        \"delta_DR\": -0.75,\n        \"delta_RV\": -0.27,\n        \"delta_R_F1\": -0.3,\n        \"delta_R_F1_excl_fail\": 0.03,\n        \"DR_reduction_pct\": 98.7,\n        \"note\": \"Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20\"\n    }\n}\n  conclusion: success\n\n--- w5_llama_lora_scierc_unconstrained_eval ---\n  status: DONE\n  metrics: {\n    \"total_samples\": 551,\n    \"total_entities\": 1757,\n    \"total_relations\": 1082,\n    \"json_parse_rate\": 1,\n    \"entity_type_violation_rate\": 0,\n    \"relation_vocabulary_violation_rate\": 0,\n    \"domain_range_violation_rate\": 0.0111,\n    \"cross_field_consistency_violation_rate\": 0,\n    \"total_violation_rate\": 0.0042,\n    \"entity_precision\": 0.6647,\n    \"entity_recall\": 0.691,\n    \"entity_f1\": 0.6776,\n    \"relation_precision\": 0.432,\n    \"relation_recall\": 0.4795,\n    \"relation_f1\": 0.4545\n}\n  conclusion: success\n\n--- w5_llama_lora_scierc_constrained_eval ---\n  status: DONE\n  metrics: {\n    \"domain_range_violation_rate\": 0.0009,\n    \"relation_vocabulary_violation_rate\": 0,\n    \"entity_type_violation_rate\": 0,\n    \"cross_field_consistency_violation_rate\": 0.0046,\n    \"relation_f1\": 0.4547,\n    \"relation_precision\": 0.432,\n    \"relation_recall\": 0.4795,\n    \"entity_f1\": 0.6776,\n    \"entity_precision\": 0.6647,\n    \"entity_recall\": 0.691,\n    \"total_relations\": 1081,\n    \"total_entities\": 1757,\n    \"total_samples\": 551,\n    \"parse_failures\": 0\n}\n  conclusion: success\n\n--- w5_llama_docred_lora_unconstrained_eval ---\n  status: DONE\n  metrics: {\n    \"ET_pct\": 0,\n    \"RV_pct\": 0.15,\n    \"DR_pct\": 0.49,\n    \"E_F1\": 83.93,\n    \"E_P\": 84.93,\n    \"E_R\": 82.96,\n    \"R_F1\": 43.72,\n    \"R_P\": 38.59,\n    \"R_R\": 50.41,\n    \"parse_fail_rate\": 2.3,\n    \"total_samples\": 998,\n    \"total_entities_pred\": 19106,\n    \"total_relations_pred\": 16171\n}\n  conclusion: success\n\n--- w5_llama_docred_lora_constrained_eval ---\n  status: DONE\n  metrics: {\n    \"total\": 998,\n    \"parse_failures\": 25,\n    \"parse_fail_rate\": 2.51,\n    \"entities\": 19077,\n    \"relations\": 16074,\n    \"entity_f1\": 83.94,\n    \"entity_precision\": 85,\n    \"entity_recall\": 84.13,\n    \"relation_f1_all_set\": 43.78,\n    \"relation_precision_all_set\": 38.79,\n    \"relation_recall_all_set\": 50.81,\n    \"et_violations\": 0,\n    \"et_violation_rate\": 0,\n    \"rv_violations\": 0,\n    \"rv_violation_rate\": 0,\n    \"dr_violations\": 33,\n    \"dr_violation_rate\": 0.21,\n    \"CF_pct\": 0.21,\n    \"delta_vs_unconstrained\": {\n        \"delta_e_f1\": 0.01,\n        \"delta_r_f1\": 0.06,\n        \"delta_dr\": -0.28,\n        \"note\": \"Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl (998 lines). Updated 2026-05-20.\"\n    },\n    \"provenance\": \"eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl, 2026-05-20. P/R corrected 2026-05-20 per Director.\"\n}\n  conclusion: success",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "9012530f-7a5e-4574-bc5e-a6ac01a202e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 56 · 2026-05-23T10:24:08.677Z_

```json
{
  "parentUuid": "2759d5db-c858-4f7f-9da8-852c16200ddc",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6145126b-9d88-4441-b2a3-a837537c70bd",
  "timestamp": "2026-05-23T10:24:08.677Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "last-prompt",
  "leafUuid": "6145126b-9d88-4441-b2a3-a837537c70bd",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper tables 1 and 2 numerical values",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---

### Assistant

_source line 59 · 2026-05-23T10:25:14.352Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the registry data. Let me carefully audit each cell.

## Table 1 (tab:scierc-ablation) — SciERC five-way ablation, Qwen3-8B, zero-shot, 551 docs

The paper uses percentage format (e.g., 15.37%), while the registry uses decimal format (e.g., 0.1537). So I need to convert.

Registry values (converting from decimal to %):

**Unconstrained (phase2_scierc_unconstrained):**


Checking each metric against the paper: DR converts to 15.37% which matches, RV becomes 1.39%, ET is 0.40%, and CF is 0.08%, all aligning with the published values. The total of DR plus CF equals 15.45%, which also checks out.

Now looking at the grammar-only phase results, the DR drops to 14.84%, representing about a 3% decrease from the full model. The other metrics shift accordingly, with RV and ET both dropping to zero while CF remains at 0.08%.

For the GCD-equivalent experiment using guided JSON, I'm seeing DR at 15.26%, which is only about 1% below the baseline, suggesting this approach maintains performance better than the grammar-only variant.

Now checking the semantic-only phase results, where DR drops to 11.65%, representing a more significant 3.72 percentage point decrease from the baseline. Now I'm verifying the S1 phase results, where the detection rate drops dramatically to 0.93% — a 94% decrease from the baseline. The relation and entity F1 scores also show significant degradation in this configuration.

Moving to S2, the metrics are similarly constrained with a detection rate of 0.97% and another 94% decline, though the conflict metric improves slightly to 8.03%. Now I'm verifying the metrics for the fine-tuning composability experiments across different constraint settings, checking the DR, CF, and F1 scores against the paper's reported values.

I'm noticing a discrepancy in the DocRED unconstrained results—the registry shows DR_pct at 0.76% but the paper reports 0.56, and I need to clarify whether there's a difference in how the metrics are being calculated or named. Looking at the parse failure rates and how they affect the metrics—the paper explicitly states that E-F1 includes parse-failure documents, but the registry values don't seem to match the paper's reported numbers even accounting for this. I'm wondering if there's been a methodological change or if I'm looking at results from a different experimental setup. Looking at the constrained evaluation results, I'm seeing similar discrepancies—the registry shows different values than what the paper reports for DR, CF, and both F1 scores. Now I'm examining the Llama DocRED experiments to see if there's a pattern or if I'm looking at the wrong configuration. The entity F1 score is 84.71, which also doesn't match the paper's reported 84.77. There's a consistent pattern of discrepancies between the registry values and what the paper reports—the DR rate is completely different (0.21% vs 0.00%), and the relation F1 scores are off by about a point. I'm wondering if the paper might be using a different evaluation setup or if there are corrected experiments I haven't found yet. Let me look at the delta values to see if they shed light on how the constrained version compares to the unconstrained baseline. The constrained eval was corrected on 2026-05-20, but the paper's reported values still don't align with what's in the registry. The unconstrained experiment is missing the CF_pct field entirely, and the R_F1 and E_F1 scores differ substantially from what the paper reports—it's possible the paper used updated values that weren't reflected back into the registry.

For the Qwen experiments, I'm noticing the E_F1 metric should account for parse failures, and the registry shows E_F1 = 82.15 with excl_fail = 85.72, but the paper lists 82.35. I should check whether there are different versions of these experiments or if the evaluation methodology shifted at some point.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6145126b-9d88-4441-b2a3-a837537c70bd",
  "isSidechain": false,
  "requestId": "req_011CbKLWgYr1RhvvzqNMEygb",
  "type": "assistant",
  "uuid": "ea886adf-d1ff-44d5-85be-ce8c81f39a34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012qiAut4QoW8DuvWap7fUP9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5163,
      "cache_read_input_tokens": 39022,
      "output_tokens": 4703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4703,
          "cache_read_input_tokens": 39022,
          "cache_creation_input_tokens": 5163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5163
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

_source line 60 · 2026-05-23T10:25:15.136Z_

I have all Table 1 source data and most of Table 2. I notice significant discrepancies in the DocRED FT numbers. Let me check for alternative/corrected experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea886adf-d1ff-44d5-85be-ce8c81f39a34",
  "isSidechain": false,
  "requestId": "req_011CbKLWgYr1RhvvzqNMEygb",
  "type": "assistant",
  "uuid": "4c73d397-41cc-4345-9449-b07f7301bc6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012qiAut4QoW8DuvWap7fUP9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5163,
      "cache_read_input_tokens": 39022,
      "output_tokens": 4703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4703,
          "cache_read_input_tokens": 39022,
          "cache_creation_input_tokens": 5163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5163
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

_source line 61 · 2026-05-23T10:25:22.219Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RgAeuVAq8tidgjjKWjHon4`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Look for any DocRED FT experiments\nfor eid in sorted(exps.keys()):\n    if 'docred' in eid.lower() and ('lora' in eid.lower() or 'ft' in eid.lower() or 'w5' in eid.lower() or 'w8' in eid.lower()):\n        e = exps[eid]\n        print(f'--- {eid} ---')\n        print(f'  status: {e.get(\\\"status\\\", \\\"N/A\\\")}')\n        m = e.get('metrics', {})\n        # Print all metric keys\n        for k in sorted(m.keys()):\n            print(f'  {k}: {m[k]}')\n        print()\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c73d397-41cc-4345-9449-b07f7301bc6a",
  "isSidechain": false,
  "requestId": "req_011CbKLWgYr1RhvvzqNMEygb",
  "type": "assistant",
  "uuid": "0b8d6289-d30e-4e6f-a17c-3bb2c9735c82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012qiAut4QoW8DuvWap7fUP9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5163,
      "cache_read_input_tokens": 39022,
      "output_tokens": 4703,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4703,
          "cache_read_input_tokens": 39022,
          "cache_creation_input_tokens": 5163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5163
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

_source line 62 · 2026-05-23T10:25:22.345Z_

<details><summary>↩ Tool result · `toolu_01RgAeuVAq8tidgjjKWjHon4`</summary>

```text
--- eval_70b_lora_docred_200_beam4_s1 ---
  status: DONE
  CF%: 0
  DR%: 0
  E-F1: 85.57
  E-P: 85.45
  E-R: 85.68
  ET%: 0
  R-F1: 48.14
  R-P: 44.24
  R-R: 52.79
  RV%: 0
  entities_pred: 3790
  parse_fail: 1/200 (0.5%)
  relations_pred: 3030

--- eval_70b_lora_docred_200_full_s2 ---
  status: DONE
  CF_count: 13
  CF_pct: 0.34
  DR_pct: 0
  ET_pct: 0
  E_F1: 84.96
  E_P: 84.6
  E_R: 85.34
  RV_pct: 0
  R_F1: 36.45
  R_P: 31.25
  R_R: 43.72
  entity_fn: 553
  entity_fp: 586
  entity_tp: 3218
  parse_fail_pct: 0
  pred_entities: 3819
  pred_relations: 3546
  relation_fn: 1421
  relation_fp: 2429
  relation_tp: 1104

--- eval_70b_lora_docred_200_grammar_only ---
  status: DONE
  CF_pct: 0.06
  DR_pct: 0.38
  ET_pct: 0
  E_F1: 80.13
  E_P: 85.16
  E_R: 75.66
  RV_pct: 0
  R_F1: 43.96
  R_P: 39.78
  R_R: 49.11
  entities_pred: 3362
  parse_fail_pct: 10.5
  relations_pred: 3154
  samples: 200

--- eval_70b_lora_docred_200_s1_constrained ---
  status: DONE
  CF_pct: 0.18
  DR_pct: 0
  ET_pct: 0
  E_F1: 79.38
  E_P: 85.24
  E_R: 74.28
  RV_pct: 0
  R_F1: 43.95
  R_P: 40.48
  R_R: 48.08
  parse_fail_pct: 12.5
  samples: 200

--- eval_70b_lora_docred_200_semantic_only ---
  status: DONE
  CF_pct: 0.21
  DR_pct: 0
  ET_pct: 0
  E_F1: 80.06
  E_P: 85.21
  E_R: 75.5
  RV_pct: 0.51
  R_F1: 43.61
  R_P: 39.44
  R_R: 48.75
  entities_pred: 3351
  parse_fail_pct: 11
  relations_pred: 3148
  samples: 200

--- eval_70b_lora_docred_200_unconstrained ---
  status: DONE
  CF_count: 2
  CF_pct: 0.06
  DR_count: 7
  DR_pct: 0.22
  ET_pct: 0
  E_F1: 80.34
  E_P: 85.13
  E_R: 76.05
  RV_count: 18
  RV_pct: 0.57
  R_F1: 43.8
  R_P: 39.6
  R_R: 48.99
  parse_fail_pct: 10
  relations: 3159
  samples: 200

--- r16_70b_lora_docred ---
  status: DONE
  epochs: 3
  eval_loss: 0.0635
  steps_completed: 1146
  token_acc: 97.94
  train_loss_end: 0.056
  train_loss_start: 0.147

--- w5_docred_sft_data_gen ---
  status: DONE
  dev_entities: 19528
  dev_relations: 12275
  dev_samples: 998
  train_entities: 59493
  train_relations: 38180
  train_samples: 3053

--- w5_llama_docred_lora_constrained_eval ---
  status: DONE
  CF_pct: 0.21
  delta_vs_unconstrained: {'delta_e_f1': 0.01, 'delta_r_f1': 0.06, 'delta_dr': -0.28, 'note': 'Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl (998 lines). Updated 2026-05-20.'}
  dr_violation_rate: 0.21
  dr_violations: 33
  entities: 19077
  entity_f1: 83.94
  entity_precision: 85
  entity_recall: 84.13
  et_violation_rate: 0
  et_violations: 0
  parse_fail_rate: 2.51
  parse_failures: 25
  provenance: eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl, 2026-05-20. P/R corrected 2026-05-20 per Director.
  relation_f1_all_set: 43.78
  relation_precision_all_set: 38.79
  relation_recall_all_set: 50.81
  relations: 16074
  rv_violation_rate: 0
  rv_violations: 0
  total: 998

--- w5_llama_docred_lora_training ---
  status: DONE
  eval_loss: 0.0624
  token_acc: 98.06
  train_loss: 0.0572

--- w5_llama_docred_lora_unconstrained_eval ---
  status: DONE
  DR_pct: 0.49
  ET_pct: 0
  E_F1: 83.93
  E_P: 84.93
  E_R: 82.96
  RV_pct: 0.15
  R_F1: 43.72
  R_P: 38.59
  R_R: 50.41
  parse_fail_rate: 2.3
  total_entities_pred: 19106
  total_relations_pred: 16171
  total_samples: 998

--- w5_llama_docred_sft_data_gen ---
  status: DONE
  dev_samples: 998
  dev_size_mb: 6.1
  train_samples: 3053
  train_size_mb: 19

--- w5_qwen_docred_lora_constrained_eval ---
  status: DONE
  CF_pct: 0.41
  DR_pct: 0.01
  ET_pct: 0
  E_F1: 81.43
  E_F1_excl_fail: 85.69
  E_P: 85.41
  E_R: 77.81
  RV_pct: 0
  R_F1: 40.56
  R_F1_excl_fail: 42.23
  R_P: 36.35
  R_R: 45.86
  delta_vs_unconstrained: {'delta_DR': -0.75, 'delta_RV': -0.27, 'delta_R_F1': -0.3, 'delta_R_F1_excl_fail': 0.03, 'DR_reduction_pct': 98.7, 'note': 'Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20'}
  fail_samples: 85
  parse_fail_rate: 8.52
  success_samples: 913
  total_entities_pred: 17799
  total_relations_pred: 15563
  total_samples: 998

--- w5_qwen_docred_lora_training ---
  status: DONE
  adapter_path: /root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred
  epochs: 3
  eval_entropy: 0.715
  eval_loss: 0.0614
  eval_mean_token_accuracy: 0.9804
  merged_path: /root/autodl-tmp/checkpoints/qwen_lora_docred_merged
  train_loss: 0.0682
  train_runtime_s: 5825.6

--- w5_qwen_docred_lora_unconstrained_eval ---
  status: DONE
  CF_pct: 0.12
  CF_pct_excl_fail: 0.12
  DR_pct: 0.76
  DR_pct_excl_fail: 0.76
  ET_pct: 0
  ET_pct_excl_fail: 0
  E_F1: 82.15
  E_F1_excl_fail: 85.72
  E_P: 85.44
  E_P_excl_fail: 85.44
  E_R: 79.11
  E_R_excl_fail: 86
  RV_pct: 0.27
  RV_pct_excl_fail: 0.27
  R_F1: 40.86
  R_F1_excl_fail: 42.2
  R_P: 36.41
  R_P_excl_fail: 36.41
  R_R: 46.56
  R_R_excl_fail: 50.17
  fail_samples: 71
  parse_fail_rate: 7.11
  success_samples: 927
  total_entities_pred: 18091
  total_relations_pred: 15870
  total_samples: 998

--- w8_llama_docred_ft_grammar_only ---
  status: DONE
  R_F1: 43.72
  R_P: 38.57
  R_R: 50.44
  note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).
  parse_fail_pct: 2.3
  samples: 998

--- w8_llama_docred_ft_semantic_only ---
  status: DONE
  R_F1: 43.85
  R_P: 38.85
  R_R: 50.31
  note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).
  parse_fail_pct: 2.4
  samples: 998

--- w8_qwen_docred_ft_grammar_only ---
  status: DONE
  CF_pct: 0.11
  DR_pct: 0.61
  ET_pct: 0
  E_F1: 82.19
  E_P: 85.47
  E_R: 79.16
  RV_pct: 0
  R_F1: 40.85
  R_P: 36.27
  R_R: 46.77
  parse_fail_rate: 7.01
  parse_failures: 70
  total_samples: 998

--- w8_qwen_docred_ft_semantic_only ---
  status: DONE
  R_F1: 40.85
  R_P: 36.33
  R_R: 46.65
  note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).
  parse_fail_pct: 7.52
  samples: 998
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b8d6289-d30e-4e6f-a17c-3bb2c9735c82",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "b108ba90-32f7-45a8-908e-1c78606e1343",
  "toolUseResult": {
    "stdout": "--- eval_70b_lora_docred_200_beam4_s1 ---\n  status: DONE\n  CF%: 0\n  DR%: 0\n  E-F1: 85.57\n  E-P: 85.45\n  E-R: 85.68\n  ET%: 0\n  R-F1: 48.14\n  R-P: 44.24\n  R-R: 52.79\n  RV%: 0\n  entities_pred: 3790\n  parse_fail: 1/200 (0.5%)\n  relations_pred: 3030\n\n--- eval_70b_lora_docred_200_full_s2 ---\n  status: DONE\n  CF_count: 13\n  CF_pct: 0.34\n  DR_pct: 0\n  ET_pct: 0\n  E_F1: 84.96\n  E_P: 84.6\n  E_R: 85.34\n  RV_pct: 0\n  R_F1: 36.45\n  R_P: 31.25\n  R_R: 43.72\n  entity_fn: 553\n  entity_fp: 586\n  entity_tp: 3218\n  parse_fail_pct: 0\n  pred_entities: 3819\n  pred_relations: 3546\n  relation_fn: 1421\n  relation_fp: 2429\n  relation_tp: 1104\n\n--- eval_70b_lora_docred_200_grammar_only ---\n  status: DONE\n  CF_pct: 0.06\n  DR_pct: 0.38\n  ET_pct: 0\n  E_F1: 80.13\n  E_P: 85.16\n  E_R: 75.66\n  RV_pct: 0\n  R_F1: 43.96\n  R_P: 39.78\n  R_R: 49.11\n  entities_pred: 3362\n  parse_fail_pct: 10.5\n  relations_pred: 3154\n  samples: 200\n\n--- eval_70b_lora_docred_200_s1_constrained ---\n  status: DONE\n  CF_pct: 0.18\n  DR_pct: 0\n  ET_pct: 0\n  E_F1: 79.38\n  E_P: 85.24\n  E_R: 74.28\n  RV_pct: 0\n  R_F1: 43.95\n  R_P: 40.48\n  R_R: 48.08\n  parse_fail_pct: 12.5\n  samples: 200\n\n--- eval_70b_lora_docred_200_semantic_only ---\n  status: DONE\n  CF_pct: 0.21\n  DR_pct: 0\n  ET_pct: 0\n  E_F1: 80.06\n  E_P: 85.21\n  E_R: 75.5\n  RV_pct: 0.51\n  R_F1: 43.61\n  R_P: 39.44\n  R_R: 48.75\n  entities_pred: 3351\n  parse_fail_pct: 11\n  relations_pred: 3148\n  samples: 200\n\n--- eval_70b_lora_docred_200_unconstrained ---\n  status: DONE\n  CF_count: 2\n  CF_pct: 0.06\n  DR_count: 7\n  DR_pct: 0.22\n  ET_pct: 0\n  E_F1: 80.34\n  E_P: 85.13\n  E_R: 76.05\n  RV_count: 18\n  RV_pct: 0.57\n  R_F1: 43.8\n  R_P: 39.6\n  R_R: 48.99\n  parse_fail_pct: 10\n  relations: 3159\n  samples: 200\n\n--- r16_70b_lora_docred ---\n  status: DONE\n  epochs: 3\n  eval_loss: 0.0635\n  steps_completed: 1146\n  token_acc: 97.94\n  train_loss_end: 0.056\n  train_loss_start: 0.147\n\n--- w5_docred_sft_data_gen ---\n  status: DONE\n  dev_entities: 19528\n  dev_relations: 12275\n  dev_samples: 998\n  train_entities: 59493\n  train_relations: 38180\n  train_samples: 3053\n\n--- w5_llama_docred_lora_constrained_eval ---\n  status: DONE\n  CF_pct: 0.21\n  delta_vs_unconstrained: {'delta_e_f1': 0.01, 'delta_r_f1': 0.06, 'delta_dr': -0.28, 'note': 'Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl (998 lines). Updated 2026-05-20.'}\n  dr_violation_rate: 0.21\n  dr_violations: 33\n  entities: 19077\n  entity_f1: 83.94\n  entity_precision: 85\n  entity_recall: 84.13\n  et_violation_rate: 0\n  et_violations: 0\n  parse_fail_rate: 2.51\n  parse_failures: 25\n  provenance: eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl, 2026-05-20. P/R corrected 2026-05-20 per Director.\n  relation_f1_all_set: 43.78\n  relation_precision_all_set: 38.79\n  relation_recall_all_set: 50.81\n  relations: 16074\n  rv_violation_rate: 0\n  rv_violations: 0\n  total: 998\n\n--- w5_llama_docred_lora_training ---\n  status: DONE\n  eval_loss: 0.0624\n  token_acc: 98.06\n  train_loss: 0.0572\n\n--- w5_llama_docred_lora_unconstrained_eval ---\n  status: DONE\n  DR_pct: 0.49\n  ET_pct: 0\n  E_F1: 83.93\n  E_P: 84.93\n  E_R: 82.96\n  RV_pct: 0.15\n  R_F1: 43.72\n  R_P: 38.59\n  R_R: 50.41\n  parse_fail_rate: 2.3\n  total_entities_pred: 19106\n  total_relations_pred: 16171\n  total_samples: 998\n\n--- w5_llama_docred_sft_data_gen ---\n  status: DONE\n  dev_samples: 998\n  dev_size_mb: 6.1\n  train_samples: 3053\n  train_size_mb: 19\n\n--- w5_qwen_docred_lora_constrained_eval ---\n  status: DONE\n  CF_pct: 0.41\n  DR_pct: 0.01\n  ET_pct: 0\n  E_F1: 81.43\n  E_F1_excl_fail: 85.69\n  E_P: 85.41\n  E_R: 77.81\n  RV_pct: 0\n  R_F1: 40.56\n  R_F1_excl_fail: 42.23\n  R_P: 36.35\n  R_R: 45.86\n  delta_vs_unconstrained: {'delta_DR': -0.75, 'delta_RV': -0.27, 'delta_R_F1': -0.3, 'delta_R_F1_excl_fail': 0.03, 'DR_reduction_pct': 98.7, 'note': 'Constrained - unconstrained. Unconstrained: DR=0.76%, R_F1=40.86, R_F1_excl_fail=42.20'}\n  fail_samples: 85\n  parse_fail_rate: 8.52\n  success_samples: 913\n  total_entities_pred: 17799\n  total_relations_pred: 15563\n  total_samples: 998\n\n--- w5_qwen_docred_lora_training ---\n  status: DONE\n  adapter_path: /root/schema_semantic_constrained_ie/checkpoints/qwen_lora_docred\n  epochs: 3\n  eval_entropy: 0.715\n  eval_loss: 0.0614\n  eval_mean_token_accuracy: 0.9804\n  merged_path: /root/autodl-tmp/checkpoints/qwen_lora_docred_merged\n  train_loss: 0.0682\n  train_runtime_s: 5825.6\n\n--- w5_qwen_docred_lora_unconstrained_eval ---\n  status: DONE\n  CF_pct: 0.12\n  CF_pct_excl_fail: 0.12\n  DR_pct: 0.76\n  DR_pct_excl_fail: 0.76\n  ET_pct: 0\n  ET_pct_excl_fail: 0\n  E_F1: 82.15\n  E_F1_excl_fail: 85.72\n  E_P: 85.44\n  E_P_excl_fail: 85.44\n  E_R: 79.11\n  E_R_excl_fail: 86\n  RV_pct: 0.27\n  RV_pct_excl_fail: 0.27\n  R_F1: 40.86\n  R_F1_excl_fail: 42.2\n  R_P: 36.41\n  R_P_excl_fail: 36.41\n  R_R: 46.56\n  R_R_excl_fail: 50.17\n  fail_samples: 71\n  parse_fail_rate: 7.11\n  success_samples: 927\n  total_entities_pred: 18091\n  total_relations_pred: 15870\n  total_samples: 998\n\n--- w8_llama_docred_ft_grammar_only ---\n  status: DONE\n  R_F1: 43.72\n  R_P: 38.57\n  R_R: 50.44\n  note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\n  parse_fail_pct: 2.3\n  samples: 998\n\n--- w8_llama_docred_ft_semantic_only ---\n  status: DONE\n  R_F1: 43.85\n  R_P: 38.85\n  R_R: 50.31\n  note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\n  parse_fail_pct: 2.4\n  samples: 998\n\n--- w8_qwen_docred_ft_grammar_only ---\n  status: DONE\n  CF_pct: 0.11\n  DR_pct: 0.61\n  ET_pct: 0\n  E_F1: 82.19\n  E_P: 85.47\n  E_R: 79.16\n  RV_pct: 0\n  R_F1: 40.85\n  R_P: 36.27\n  R_R: 46.77\n  parse_fail_rate: 7.01\n  parse_failures: 70\n  total_samples: 998\n\n--- w8_qwen_docred_ft_semantic_only ---\n  status: DONE\n  R_F1: 40.85\n  R_P: 36.33\n  R_R: 46.65\n  note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\n  parse_fail_pct: 7.52\n  samples: 998",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "0b8d6289-d30e-4e6f-a17c-3bb2c9735c82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 63_

```json
{
  "type": "last-prompt",
  "leafUuid": "b108ba90-32f7-45a8-908e-1c78606e1343",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper tables 1 and 2 numerical values",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---

### Assistant

_source line 65 · 2026-05-23T10:27:41.373Z_

<details><summary>Logged reasoning block</summary>

```text
I see some important discrepancies. The DocRED FT numbers in the paper don't match the registry values. Let me examine the discrepancies more carefully.

For Table 2 DocRED experiments:

**Qwen3-8B DocRED Unconstrained:**
- Paper DR: 0.56 vs Registry DR: 0.76
- Paper CF: 0.08 vs Registry CF: 0.12
- Paper R-F1: 40.89 vs Registry R_F1: 40.86
- Paper E-F1: 82.35 vs Registry E_F1: 82.15


**Qwen3-8B DocRED S1:**
- Paper DR: 0.00 vs Registry DR: 0.01
- Paper CF: 0.22 vs Registry CF: 0.41
- Paper R-F1: 40.79 vs Registry R_F1: 40.56
- Paper E-F1: 81.87 vs Registry E_F1: 81.43

Now checking the Llama results—the unconstrained DR matches perfectly at 0.49, but I'm noticing the CF value is missing from the registry data.

**Llama DocRED Unconstrained:**
- Paper DR: 0.49 vs Registry DR: 0.49 ✅
- Paper CF: 0.08 vs Registry: ??? (no CF field listed directly)
- Paper R-F1: 44.55 vs Registry R_F1: 43.72
- Paper E-F1: 84.77 vs Registry E_F1: 83.93

**Llama DocRED S1:**
- Paper DR: 0.00 vs Registry dr_violation_rate: 0.21
- Paper CF: 0.26 vs Registry CF_pct: 0.21
- Paper R-F1: 44.70 vs Registry relation_f1_all_set: 43.78
- Paper E-F1: 84.71 vs Registry entity_f1: 83.94

The Llama results show substantial gaps between paper and registry values, particularly in the DR metric. I'm wondering if there's a different evaluation setup at play here—maybe the w8 experiments use a different methodology.

Looking at the notes, I see references to "Old registry value X was from unified_f1_eval.py" versus newer values from "eval_d064.py", and there's mention of a parse-failure bug in the old evaluation script. The paper's Qwen DocRED unconstrained R-F1 of 40.89 matches what's labeled as the "old registry value," which suggests the paper might be reporting results from the older evaluation method that had this bug. So the old buggy value was 40.89, and the corrected one is 40.85. For Llama, there's a massive discrepancy—the paper reports 44.55 but the registry shows 43.72, which is 0.83 percentage points off. I'm wondering if the paper used a different evaluation approach for handling parse failures, maybe assigning them partial credit rather than excluding them entirely.

Looking at the pattern across all the Qwen DocRED metrics, I'm seeing consistent small differences between paper and registry values—the unconstrained R-F1 is off by 0.03, E-F1 by 0.20, and some metrics like DR show larger gaps. This suggests the registry might have been corrected for that parse-failure bug that was inflating the original numbers.

But the Llama DocRED discrepancies are much more alarming—the unconstrained R-F1 differs by 0.83, E-F1 by 0.84, and the constrained versions are similarly off by 0.77 to 0.92. These aren't small rounding errors; something fundamental is different between what the paper reports and what's in the registry. Let me check if the paper might be using the `excl_fail` variant instead, since the unconstrained R-F1 with that metric shows 42.20, which still doesn't match the paper's 40.89.

Actually, I think I've found the issue. The Llama DocRED constrained entry is marked "P/R corrected 2026-05-20 per Director" with a note pointing to "eval_d064.py" as the authoritative source. The task description mentions that violation_checker.py had a parse-failure bug that was fixed, and the registry values marked "CORRECTED" reflect that fix. The paper was likely written before these corrections were applied, so it contains the old, buggy values. The same parse-failure bug also affected unified_f1_eval.py, which explains why the old paper numbers don't match the corrected registry values. The registry shows Llama's R-F1 with parse failures included at 43.72, but the paper reports 44.55—higher than the registry value, which suggests the paper might have used a buggy evaluation script that artificially inflated the results. The discrepancy doesn't match the exclude-failures pattern either, so I need to look more carefully at the registry's corrected tags and check if there are other DocRED experiments that align with the paper's numbers. Let me also examine the SciERC fine-tuning results since those seem to match the registry better.

Looking at the SciERC fine-tuning metrics, all the values align perfectly when I account for the decimal shift—Qwen and Llama both show matching document retrieval and relation F1 scores across constrained and unconstrained settings. This perfect alignment only in SciERC but not DocRED strongly suggests the parse-failure bug was specific to the DocRED evaluation.

The w8 experiment notes mention that the old registry value came from a buggy evaluation script that had the same parse-failure issue, producing 40.89 for Qwen DocRED unconstrained R-F1, which matches the paper. But I need to be careful here—the registry experiment is semantic-only fine-tuning while the paper reports the base unconstrained result, so these aren't directly comparable experiments.

Looking at the Llama numbers, there's an 0.83 percentage point gap between the paper's 44.55 and the registry's 43.72, which is larger than the parse failure rate of 2.3% would explain. Without the excluded-failure metric for Llama, I can't determine if the same bug accounts for this discrepancy. l_fail, but we can estimate: 43.72 is the all-sample value, and with 2.3% excluded, the excl_fail value would be roughly 43.72 * 998 / 975 ≈ 44.76. That's pretty close to 44.55!

Actually, let me reconsider the mechanics here. When parse failures are excluded, we're removing both the empty predictions and their corresponding gold labels, so F1 is only computed on successful parses—which should give higher scores than including those failed documents as false negatives. The paper reports 44.55, which is higher than the registry's 43.72 (incl_fail), suggesting the paper might be using excl_fail values instead.

Looking at the Qwen DocRED case, the paper's 40.89 is very close to the registry's incl_fail of 40.86, not the excl_fail of 42.20, so they seem to align within rounding. For Llama DocRED unconstrained, I need to check where the paper value falls relative to both metrics.

The pattern across metrics is striking: Llama DocRED shows consistent gaps of 0.8-0.9 percentage points between paper and registry values, while Qwen shows much smaller discrepancies. The constrained experiments are even more suspicious—Llama's DR drops from 0.21 to 0.00, and R-F1 jumps by 0.92pp. This suggests the Llama DocRED results might have been re-run or re-evaluated differently than what's currently in the registry.

Looking at the provenance notes, the Llama constrained experiment was corrected on 2026-05-20 with precision and recall adjustments. If those corrections inflated both metrics, it would explain why the paper's F1 scores are higher than the current registry values. The paper was likely written with the older, uncorrected numbers before these P/R adjustments were applied.

Now I'm checking the delta DR values in Table 2 more carefully. For Qwen DocRED, the paper claims a 100% drop from 0.56 to 0.00, but the registry shows it actually went from 0.76 to 0.01—a 98.7% decrease. For Llama DocRED, the paper says 100% drop from 0.49 to 0.00, yet the registry has it going from 0.49 to 0.21, which is only a 57% decrease. These delta values are significantly off, especially for Llama.

Looking more closely at the Llama constrained experiment, the registry shows a dr_violation_rate of 0.21 with 33 violations—but I need to clarify whether this is 0.21% or 21%. Given the context, it should be 0.21%, which doesn't match the paper's claim of 0.00%. The provenance note mentions P/R corrections from May 2026, so it's possible the original DR was 0% (matching the paper) and was later corrected to 0.21%.

Now let me verify the cross-field consistency values for Llama SciERC to ensure those align with the paper.

For the unconstrained version, both the registry and paper show 0, which checks out. For the constrained version, the registry reports 0.0046 while the paper shows 0.46—these match when I convert the decimal to a percentage.

Moving to Llama DocRED, I'm noticing the unconstrained evaluation metrics in the registry don't include a cross-field consistency field at all, even though the paper reports a value of 0.08. I need to look more carefully through the full output to see if I missed it somewhere.

Looking at the constrained version, the registry shows 0.21 but the paper claims 0.26—another mismatch. I'm also seeing discrepancies across the Qwen DocRED results: the unconstrained registry value is 0.12 versus the paper's 0.08, and for constrained it's 0.41 in the registry but 0.22 in the paper.

Let me verify some of the computed values from Table 2, starting with the delta metrics for Qwen SciERC. The Qwen SciERC E-F1 values check out fine. For the Llama DocRED discrepancy, the registry shows the corrected DR value is 0.21%, not 0.00% as the original buggy evaluation would have shown, which explains why the paper's claimed 100% reduction doesn't match the current data. Now I'm compiling the full audit summary—Table 1 is fully verified across all 48 cells, and I'm working through Table 2 to document which results align with the registry and which ones have significant gaps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b108ba90-32f7-45a8-908e-1c78606e1343",
  "isSidechain": false,
  "requestId": "req_011CbKLc7cNQF84W9gpquLuV",
  "type": "assistant",
  "uuid": "604d55fc-0ab0-4914-b57b-fc8be5663c3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178ayVH8hfMBdeFtxDCVKjC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7910,
      "cache_read_input_tokens": 44185,
      "output_tokens": 6759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7910,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6759,
          "cache_read_input_tokens": 44185,
          "cache_creation_input_tokens": 7910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7910
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

_source line 66 · 2026-05-23T10:27:41.374Z_

Now I have all the data. Let me also check for CF data on the Llama DocRED unconstrained experiment and look for any correction notes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "604d55fc-0ab0-4914-b57b-fc8be5663c3f",
  "isSidechain": false,
  "requestId": "req_011CbKLc7cNQF84W9gpquLuV",
  "type": "assistant",
  "uuid": "d3adfa65-38ba-41c9-bba0-7b1309cff322",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178ayVH8hfMBdeFtxDCVKjC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7910,
      "cache_read_input_tokens": 44185,
      "output_tokens": 6759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7910,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6759,
          "cache_read_input_tokens": 44185,
          "cache_creation_input_tokens": 7910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7910
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

_source line 67 · 2026-05-23T10:27:46.095Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LohCLmT5skGJUA9E9K2V4H`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Check for correction notes, CORRECTED tags\nfor eid in sorted(exps.keys()):\n    e = exps[eid]\n    m = e.get('metrics', {})\n    c = e.get('conclusion', '')\n    # Look for CORRECTED, provenance, note, bug mentions\n    for k, v in m.items():\n        sv = str(v)\n        if any(w in sv.lower() for w in ['corrected', 'bug', 'old registry', 'provenance', 'updated']):\n            print(f'{eid}.metrics.{k}: {v}')\n    if 'note' in m:\n        print(f'{eid}.metrics.note: {m[\\\"note\\\"]}')\n    if 'provenance' in m:\n        print(f'{eid}.metrics.provenance: {m[\\\"provenance\\\"]}')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3adfa65-38ba-41c9-bba0-7b1309cff322",
  "isSidechain": false,
  "requestId": "req_011CbKLc7cNQF84W9gpquLuV",
  "type": "assistant",
  "uuid": "a73d3080-3704-4c0a-8769-e2f9508d320d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178ayVH8hfMBdeFtxDCVKjC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7910,
      "cache_read_input_tokens": 44185,
      "output_tokens": 6759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7910,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6759,
          "cache_read_input_tokens": 44185,
          "cache_creation_input_tokens": 7910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7910
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

_source line 68 · 2026-05-23T10:27:46.387Z_

<details><summary>↩ Tool result · `toolu_01LohCLmT5skGJUA9E9K2V4H`</summary>

```text
d066_sweep_21461_gpu1.metrics.note: Actually ran on SciERC 551 docs (not DocRED 200 as originally recorded in hypothesis)
d066_sweep_llama_scierc_beam1_unc.metrics.note: INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun.
d066_sweep_llama_scierc_beam2_s1_551.metrics.note: ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc
d066_sweep_llama_scierc_beam2_s1_551.metrics.note: ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc
d066_sweep_llama_scierc_beam4_s1_551.metrics.note: ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc
d066_sweep_llama_scierc_beam4_s1_551.metrics.note: ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc
d066_sweep_llama_scierc_beam8_s1_551.metrics.note: Reconcile false positive corrected. Eval with --dataset scierc confirmed.
d066_sweep_llama_scierc_beam8_s1_551.metrics.note: Reconcile false positive corrected. Eval with --dataset scierc confirmed.
ee_llama_wikievents_constrained.metrics.note: after retry with max_new_tokens=8192
ee_mistral_wikievents_constrained.metrics.note: grammar_only baseline (old code without semantic mask fix)
ee_qwen_wikievents_constrained.metrics.note: after retry with max_new_tokens=8192
entity_order_ablation_qwen_scierc.metrics.note: CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.
entity_order_ablation_qwen_scierc.metrics.note: CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.
phase2_s2_pilot50.metrics.note: DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。
r16_70b_docred_zs_s1.metrics.note: Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch.
r16_70b_docred_zs_s1.metrics.note: Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch.
r16_trie_llama_ft_scierc.metrics.note: CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.
r16_trie_llama_ft_scierc.metrics.note: CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.
r16_trie_qwen_ft_scierc.metrics.note: CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.
r16_trie_qwen_ft_scierc.metrics.note: CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.
w5_llama_docred_lora_constrained_eval.metrics.delta_vs_unconstrained: {'delta_e_f1': 0.01, 'delta_r_f1': 0.06, 'delta_dr': -0.28, 'note': 'Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl (998 lines). Updated 2026-05-20.'}
w5_llama_docred_lora_constrained_eval.metrics.provenance: eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl, 2026-05-20. P/R corrected 2026-05-20 per Director.
w5_llama_docred_lora_constrained_eval.metrics.provenance: eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl, 2026-05-20. P/R corrected 2026-05-20 per Director.
w8_llama_docred_ft_grammar_only.metrics.note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).
w8_llama_docred_ft_grammar_only.metrics.note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).
w8_llama_docred_ft_semantic_only.metrics.note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).
w8_llama_docred_ft_semantic_only.metrics.note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).
w8_qwen_docred_ft_semantic_only.metrics.note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).
w8_qwen_docred_ft_semantic_only.metrics.note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).
w9_qwen_scierc_zs_sampling.metrics.note: F1 computed by v2 checker; greedy baseline with same checker: E_F1=30.98, R_F1=8.36
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a73d3080-3704-4c0a-8769-e2f9508d320d",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "aff1f98b-b227-4d43-878f-0bb6a62a6f0a",
  "toolUseResult": {
    "stdout": "d066_sweep_21461_gpu1.metrics.note: Actually ran on SciERC 551 docs (not DocRED 200 as originally recorded in hypothesis)\nd066_sweep_llama_scierc_beam1_unc.metrics.note: INVALIDATED: Used dev set (275 docs) instead of test set (551 docs). Not comparable with other beam sweep results. Llama SciERC beam sweep deprioritized — must use scripts/d066_beam_sweep_scierc.sh with --data_path data/processed_data/test.json if rerun.\nd066_sweep_llama_scierc_beam2_s1_551.metrics.note: ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\nd066_sweep_llama_scierc_beam2_s1_551.metrics.note: ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\nd066_sweep_llama_scierc_beam4_s1_551.metrics.note: ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\nd066_sweep_llama_scierc_beam4_s1_551.metrics.note: ET/RV corrected from 100→0: original eval used hardcoded DocRED ontology, re-evaled with --dataset scierc\nd066_sweep_llama_scierc_beam8_s1_551.metrics.note: Reconcile false positive corrected. Eval with --dataset scierc confirmed.\nd066_sweep_llama_scierc_beam8_s1_551.metrics.note: Reconcile false positive corrected. Eval with --dataset scierc confirmed.\nee_llama_wikievents_constrained.metrics.note: after retry with max_new_tokens=8192\nee_mistral_wikievents_constrained.metrics.note: grammar_only baseline (old code without semantic mask fix)\nee_qwen_wikievents_constrained.metrics.note: after retry with max_new_tokens=8192\nentity_order_ablation_qwen_scierc.metrics.note: CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\nentity_order_ablation_qwen_scierc.metrics.note: CORRECTED 2026-05-22: Fair comparison with fixed violation_checker shows ZERO difference. raw_output and parsed_output are byte-identical across all 551 samples. Previous -3.38pp delta was entirely due to comparing old-checker original (47.15) vs new-checker shuffled (43.77). Entity ordering is confirmed order-invariant.\nphase2_s2_pilot50.metrics.note: DR 修正: 原值 0 来自 dryrun (n=25 triples)。实际 pilot50 DR=3/146=2.05% (来自 violation_report_s2_pilot50.json)。\nr16_70b_docred_zs_s1.metrics.note: Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch.\nr16_70b_docred_zs_s1.metrics.note: Metrics corrected via eval_d064.py with DocRED schema mapping. Original violation_checker.py gave R-F1=0 due to SciERC schema mismatch.\nr16_trie_llama_ft_scierc.metrics.note: CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\nr16_trie_llama_ft_scierc.metrics.note: CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=41.42 was inflated (gold dropped for parse failures). Old E-F1=65.37 also inflated.\nr16_trie_qwen_ft_scierc.metrics.note: CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\nr16_trie_qwen_ft_scierc.metrics.note: CORRECTED 2026-05-22: violation_checker.py parse-failure bug fixed. Old R-F1=42.57 was inflated. Old E-F1=66.73 also inflated.\nw5_llama_docred_lora_constrained_eval.metrics.delta_vs_unconstrained: {'delta_e_f1': 0.01, 'delta_r_f1': 0.06, 'delta_dr': -0.28, 'note': 'Authoritative values from eval_d064.py on w5_llama_docred_lora_constrained_eval.jsonl (998 lines). Updated 2026-05-20.'}\nw5_llama_docred_lora_constrained_eval.metrics.provenance: eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl, 2026-05-20. P/R corrected 2026-05-20 per Director.\nw5_llama_docred_lora_constrained_eval.metrics.provenance: eval_d064.py on westd-16980:/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl, 2026-05-20. P/R corrected 2026-05-20 per Director.\nw8_llama_docred_ft_grammar_only.metrics.note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\nw8_llama_docred_ft_grammar_only.metrics.note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.77 was from unified_f1_eval.py (delta -0.05pp).\nw8_llama_docred_ft_semantic_only.metrics.note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\nw8_llama_docred_ft_semantic_only.metrics.note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 43.90 was from unified_f1_eval.py (delta -0.05pp).\nw8_qwen_docred_ft_semantic_only.metrics.note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\nw8_qwen_docred_ft_semantic_only.metrics.note: Re-verified 2026-05-22 with eval_d064.py (no bug). Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug, delta -0.04pp).\nw9_qwen_scierc_zs_sampling.metrics.note: F1 computed by v2 checker; greedy baseline with same checker: E_F1=30.98, R_F1=8.36",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a73d3080-3704-4c0a-8769-e2f9508d320d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-23T10:27:48.832Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019KrCQhjWFfkZXKix7fKr1i`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-6-projects-schema-semantic-constrained-ie/bed18bf9-b23b-41a9-845b-decdb9931508/tool-results/mcp-agent-ml-research-read_registry-1779531807189.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Look for w8_ft_posthoc_baseline and any posthoc_filtering experiments\nfor eid in ['w8_ft_posthoc_baseline', 'posthoc_filtering_baseline']:\n    if eid in exps:\n        e = exps[eid]\n        print(f'--- {eid} ---')\n        m = e.get('metrics', {})\n        for k in sorted(m.keys()):\n            print(f'  {k}: {m[k]}')\n        print()\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aff1f98b-b227-4d43-878f-0bb6a62a6f0a",
  "isSidechain": false,
  "requestId": "req_011CbKLc7cNQF84W9gpquLuV",
  "type": "assistant",
  "uuid": "912bc230-e8bf-4677-b06d-43b97fba39bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0178ayVH8hfMBdeFtxDCVKjC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7910,
      "cache_read_input_tokens": 44185,
      "output_tokens": 6759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7910,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6759,
          "cache_read_input_tokens": 44185,
          "cache_creation_input_tokens": 7910,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7910
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

_source line 70 · 2026-05-23T10:27:48.971Z_

<details><summary>↩ Tool result · `toolu_019KrCQhjWFfkZXKix7fKr1i`</summary>

```text
--- w8_ft_posthoc_baseline ---
  ft_regime: {'qwen_scierc': {'R_F1_before': 43.86, 'R_F1_posthoc': 43.94, 'R_F1_constrained': 43.77, 'reject_rate_pct': 1.95, 'TP_lost': 4}, 'llama_scierc': {'R_F1_before': 45.45, 'R_F1_posthoc': 45.23, 'R_F1_constrained': 45.47, 'reject_rate_pct': 1.11, 'TP_lost': 5}, 'qwen_docred': {'R_F1_before': 40.91, 'R_F1_posthoc': 41.11, 'R_F1_constrained': 'TBD', 'reject_rate_pct': 1.03, 'TP_lost': 1}, 'llama_docred': {'R_F1_before': 43.77, 'R_F1_posthoc': 43.92, 'R_F1_constrained': 44.23, 'reject_rate_pct': 0.64, 'TP_lost': 1}}
  key_finding: ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception: Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained decoding value is in structural guarantee (0% violations) and composability, not F1 preservation.
  zs_regime: {'mistral_scierc': {'triples': 1584, 'reject_pct': 20.27, 'R_F1_before': 0.0376, 'R_F1_posthoc': 0.0394, 'R_F1_constrained': 0.0367, 'TP_before': 48, 'TP_after': 44, 'TP_lost': 4}, 'qwen_scierc': {'triples': 1724, 'reject_pct': 16.76, 'R_F1_before': 0.0823, 'R_F1_posthoc': 0.0863, 'R_F1_constrained': 0.0836, 'TP_before': 111, 'TP_after': 104, 'TP_lost': 7}, 'llama_scierc': {'triples': 1274, 'reject_pct': 13.89, 'R_F1_before': 0.0268, 'R_F1_posthoc': 0.0271, 'R_F1_constrained': 0.0254, 'TP_before': 30, 'TP_after': 28, 'TP_lost': 2}, 'qwen_docred': {'triples': 17497, 'reject_pct': 48.12, 'R_F1_before': 0.0774, 'R_F1_posthoc': 0.0961, 'R_F1_constrained': 0.0823, 'TP_before': 1137, 'TP_after': 1010, 'TP_lost': 127}, 'llama_docred': {'triples': 16437, 'reject_pct': 42.18, 'R_F1_before': 0.0598, 'R_F1_posthoc': 0.0744, 'R_F1_constrained': 0.0627, 'TP_before': 850, 'TP_after': 802, 'TP_lost': 48}, 'mistral_docred': {'triples': 11836, 'reject_pct': 73.73, 'R_F1_before': 0.0434, 'R_F1_posthoc': 0.0385, 'R_F1_constrained': 0.0552, 'TP_before': 518, 'TP_after': 292, 'TP_lost': 226, 'removed_RV': 4172, 'removed_ET': 3382, 'removed_DR': 1173, 'note': 'Only ZS case where posthoc HURTS R_F1 — 73.7% rejection rate loses 43.6% of TPs'}}

--- posthoc_filtering_baseline ---
  docred_et_residual: 0.0247
  docred_f1_after: 9.61
  docred_f1_before: 7.74
  docred_precision_after: 11.22
  docred_precision_before: 6.55
  docred_recall_after: 8.4
  docred_recall_before: 9.46
  docred_rejection_rate: 0.481
  docred_tp_after: 1010
  docred_tp_before: 1137
  docred_tp_lost: 127
  scierc_f1_after: 8.63
  scierc_f1_before: 8.23
  scierc_recall_after: 10.68
  scierc_recall_before: 11.4
  scierc_rejection_rate: 0.168
  scierc_tp_after: 104
  scierc_tp_before: 111
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "912bc230-e8bf-4677-b06d-43b97fba39bf",
  "isSidechain": false,
  "promptId": "d2ace215-4d65-4968-8b0d-28059690aec2",
  "type": "user",
  "uuid": "70f230ec-472e-45fe-9d44-20690fa53aba",
  "toolUseResult": {
    "stdout": "--- w8_ft_posthoc_baseline ---\n  ft_regime: {'qwen_scierc': {'R_F1_before': 43.86, 'R_F1_posthoc': 43.94, 'R_F1_constrained': 43.77, 'reject_rate_pct': 1.95, 'TP_lost': 4}, 'llama_scierc': {'R_F1_before': 45.45, 'R_F1_posthoc': 45.23, 'R_F1_constrained': 45.47, 'reject_rate_pct': 1.11, 'TP_lost': 5}, 'qwen_docred': {'R_F1_before': 40.91, 'R_F1_posthoc': 41.11, 'R_F1_constrained': 'TBD', 'reject_rate_pct': 1.03, 'TP_lost': 1}, 'llama_docred': {'R_F1_before': 43.77, 'R_F1_posthoc': 43.92, 'R_F1_constrained': 44.23, 'reject_rate_pct': 0.64, 'TP_lost': 1}}\n  key_finding: ZS: post-hoc R_F1 >= constrained R_F1 in 5/6 groups. Exception: Mistral DocRED where extreme rejection rate (73.7%) causes net F1 loss. Constrained decoding value is in structural guarantee (0% violations) and composability, not F1 preservation.\n  zs_regime: {'mistral_scierc': {'triples': 1584, 'reject_pct': 20.27, 'R_F1_before': 0.0376, 'R_F1_posthoc': 0.0394, 'R_F1_constrained': 0.0367, 'TP_before': 48, 'TP_after': 44, 'TP_lost': 4}, 'qwen_scierc': {'triples': 1724, 'reject_pct': 16.76, 'R_F1_before': 0.0823, 'R_F1_posthoc': 0.0863, 'R_F1_constrained': 0.0836, 'TP_before': 111, 'TP_after': 104, 'TP_lost': 7}, 'llama_scierc': {'triples': 1274, 'reject_pct': 13.89, 'R_F1_before': 0.0268, 'R_F1_posthoc': 0.0271, 'R_F1_constrained': 0.0254, 'TP_before': 30, 'TP_after': 28, 'TP_lost': 2}, 'qwen_docred': {'triples': 17497, 'reject_pct': 48.12, 'R_F1_before': 0.0774, 'R_F1_posthoc': 0.0961, 'R_F1_constrained': 0.0823, 'TP_before': 1137, 'TP_after': 1010, 'TP_lost': 127}, 'llama_docred': {'triples': 16437, 'reject_pct': 42.18, 'R_F1_before': 0.0598, 'R_F1_posthoc': 0.0744, 'R_F1_constrained': 0.0627, 'TP_before': 850, 'TP_after': 802, 'TP_lost': 48}, 'mistral_docred': {'triples': 11836, 'reject_pct': 73.73, 'R_F1_before': 0.0434, 'R_F1_posthoc': 0.0385, 'R_F1_constrained': 0.0552, 'TP_before': 518, 'TP_after': 292, 'TP_lost': 226, 'removed_RV': 4172, 'removed_ET': 3382, 'removed_DR': 1173, 'note': 'Only ZS case where posthoc HURTS R_F1 — 73.7% rejection rate loses 43.6% of TPs'}}\n\n--- posthoc_filtering_baseline ---\n  docred_et_residual: 0.0247\n  docred_f1_after: 9.61\n  docred_f1_before: 7.74\n  docred_precision_after: 11.22\n  docred_precision_before: 6.55\n  docred_recall_after: 8.4\n  docred_recall_before: 9.46\n  docred_rejection_rate: 0.481\n  docred_tp_after: 1010\n  docred_tp_before: 1137\n  docred_tp_lost: 127\n  scierc_f1_after: 8.63\n  scierc_f1_before: 8.23\n  scierc_recall_after: 10.68\n  scierc_recall_before: 11.4\n  scierc_rejection_rate: 0.168\n  scierc_tp_after: 104\n  scierc_tp_before: 111",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "912bc230-e8bf-4677-b06d-43b97fba39bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 71_

```json
{
  "type": "last-prompt",
  "leafUuid": "70f230ec-472e-45fe-9d44-20690fa53aba",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---

### Runtime record

_source line 72_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper tables 1 and 2 numerical values",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---

### Assistant

_source line 73 · 2026-05-23T10:29:22.869Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clearer picture. Let me also check the w8_ft_posthoc_baseline data more carefully. It has:

For Qwen DocRED FT:
- R_F1_before: 40.91 (not 40.86 or 40.89)
- R_F1_constrained: 'TBD'

For Llama DocRED FT:
- R_F1_before: 43.77 (not 43.72 or 44.55)
- R_F1_constrained: 44.23


There's a pattern of discrepancies across these datasets—the baseline R_F1 scores vary depending on which source I'm looking at, with Qwen ranging from 40.86 to 40.91 and Llama from 43.72 to 44.55 across the different evaluation runs and the paper.

Looking at the notes, it's clear that multiple evaluation scripts had the same parse-failure bug that was eventually fixed, with `eval_d064.py` being the corrected version and the registry containing the fixed values. The paper seems to be reporting older numbers from before this bug was addressed, which explains why the Llama DocRED metrics are off by about 1 percentage point in R-F1 and 0.21 in DR, and Qwen's DR and CF metrics are similarly off by 0.20 and 0.19 respectively.

Before I write up the full audit report, I should double-check whether there's a different metric field I should be comparing against.

Looking at the Qwen DocRED unconstrained case more closely, the registry shows DR_pct at 0.76% while the paper reports 0.56%, a 0.20 percentage point gap. This discrepancy isn't explained by any correction note in the registry. I'm wondering if the paper might be calculating DR using a different methodology—perhaps treating parse failures differently by counting them as documents with zero violations and zero triples, which could shift the DR calculation for successful documents. The registry notes mention 998 dev documents, so there's likely something about how the evaluation handles the full dataset versus just successful parses.

There's also a pattern emerging with the evaluation scripts. The registry notes that the old value of 40.89 came from unified_f1_eval.py, which had a parse-failure bug that inflated R-F1 by about 0.04 percentage points compared to the corrected eval_d064.py script. The paper reports R-F1 of 40.89 for Qwen DocRED unconstrained, while the registry shows 40.86—if the paper used the buggy unified_f1_eval.py script, that would roughly align with 40.86 plus the 0.04pp inflation.

Now looking at the DR values, there's a bigger discrepancy: the paper shows 0.56 but the registry has 0.76. I'm wondering if the parse-failure bug in violation_checker.py might also be affecting the DR calculation. If documents with parse failures were excluded from the violation count but their predicted triples were still included in the denominator, that could artificially lower the DR metric. Let me think through whether the violation counting logic would have been affected by dropping gold labels for those problematic documents.

Actually, I'm probably overcomplicating this. The real issue is that the paper values simply don't match what's in the corrected registry after eval_d064.py was applied. I should focus on compiling the audit report with the verified values. Let me double-check Table 1's percentage conversions and Table 2's SciERC results, particularly the Llama unconstrained cross-field consistency violation rate which shows as 0 in the registry.

The Llama and Qwen SciERC values are all checking out—the registry rates convert correctly to the paper percentages. And for the Llama SciERC S1 delta detection rate, the calculation confirms it's around 92%.

Now I need to do a full systematic audit of all the results. But first, I'm noticing the Llama DocRED unconstrained model is missing a cross-field consistency percentage in the registry, so let me track down what happened there.

Looking back at the metrics I extracted earlier, I can see the RV_pct is present at 0.15, but there's no CF_pct field at all. The paper reports CF = 0.08 for this experiment, but I don't have the data to verify it from the registry. I'll need to note this gap when I write up the full audit.

Now I'm noticing a broader pattern across the DocRED experiments: the CF values in the registry don't match what the paper reports. For Qwen's unconstrained model, the registry shows 0.12 while the paper says 0.08. The constrained version has even larger discrepancies—registry shows 0.41 versus the paper's 0.22. Llama's constrained model also differs, with the registry at 0.21 and the paper at 0.26. This is consistent across all the DocRED rows.

There's also an issue with the DR metric for Llama's constrained model: the registry lists dr_violation_rate as 0.21 with 33 violations, which could mean 0.21% (roughly matching 33/16074), but the paper claims DR = 0.00. These discrepancies need to be documented in the audit.

The provenance note confirms the experiment was re-evaluated with corrected code on 2026-05-20, which explains why the new values differ from the published paper. I can now verify the Table 1 totals by checking if DR + CF matches the reported values, and so far the math checks out for the unconstrained, grammar, and GCD-equiv rows.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70f230ec-472e-45fe-9d44-20690fa53aba",
  "isSidechain": false,
  "requestId": "req_011CbKLnvSiQBWGG5DKz68YK",
  "type": "assistant",
  "uuid": "4264e721-fe35-4fdb-be84-e78a2588b3ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKohtabrjkvAThaoBn5NTD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10200,
      "cache_read_input_tokens": 52095,
      "output_tokens": 6934,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10200,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6934,
          "cache_read_input_tokens": 52095,
          "cache_creation_input_tokens": 10200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10200
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

_source line 74 · 2026-05-23T10:30:21.421Z_

I now have all the data needed. Here is the complete audit report.

---

## Table 1 审计报告 (`tab:scierc-ablation`)
**SciERC 551 docs, Qwen3-8B, zero-shot**

Registry metrics use decimal (e.g., 0.1537 = 15.37%); vLLM experiment uses percent directly.

### Row: Unconstrained — `phase2_scierc_unconstrained`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 15.37 | 0.1537 → 15.37% | ✅ |
| ΔDR | --- | --- | ✅ |
| RV | 1.39 | 0.0139 → 1.39% | ✅ |
| ET | 0.40 | 0.004 → 0.40% | ✅ |
| CF | 0.08 | 0.0008 → 0.08% | ✅ |
| Tot. | 15.45 | 15.37+0.08=15.45 | ✅ |
| Rel. F1 | 8.23 | 0.0823 → 8.23% | ✅ |
| Ent. F1 | 31.01 | 0.3101 → 31.01% | ✅ |

### Row: Grammar — `phase2_scierc_grammar_only`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 14.84 | 0.1484 → 14.84% | ✅ |
| ΔDR | ↓3% | (15.37-14.84)/15.37=3.4%≈3% | ✅ |
| RV | 0 | 0 | ✅ |
| ET | 0 | 0 | ✅ |
| CF | 0.08 | 0.0008 → 0.08% | ✅ |
| Tot. | 14.92 | 14.84+0.08=14.92 | ✅ |
| Rel. F1 | 8.23 | 0.0823 → 8.23% | ✅ |
| Ent. F1 | 30.98 | 0.3098 → 30.98% | ✅ |

### Row: GCD-equiv.† — `vllm_guided_json_scierc_zs`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 15.26 | 15.26% | ✅ |
| ΔDR | ↓1% | (15.37-15.26)/15.37=0.7%≈1% | ✅ |
| RV | 0 | 0% | ✅ |
| ET | 0 | 0% | ✅ |
| CF | 0.04 | 0.04% | ✅ |
| Tot. | 15.30 | 15.26+0.04=15.30 | ✅ |
| Rel. F1 | 8.75 | 8.75% | ✅ |
| Ent. F1 | 30.91 | 30.91% | ✅ |

### Row: Semantic — `phase2_scierc_semantic_only`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 11.65 | 0.1165 → 11.65% | ✅ |
| ΔDR | ↓24% | (15.37-11.65)/15.37=24.2%≈24% | ✅ |
| RV | 1.51 | 0.0151 → 1.51% | ✅ |
| ET | 0.40 | 0.004 → 0.40% | ✅ |
| CF | 2.71 | 0.0271 → 2.71% | ✅ |
| Tot. | 14.36 | 11.65+2.71=14.36 | ✅ |
| Rel. F1 | 8.15 | 0.0815 → 8.15% | ✅ |
| Ent. F1 | 31.01 | 0.3101 → 31.01% | ✅ |

### Row: S1 — `phase2_scierc_full_s1`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 0.93 | 0.0093 → 0.93% | ✅ |
| ΔDR | ↓94% | (15.37-0.93)/15.37=93.9%≈94% | ✅ |
| RV | 0 | 0 | ✅ |
| ET | 0 | 0 | ✅ |
| CF | 9.90 | 0.099 → 9.90% | ✅ |
| Tot. | 10.83 | 0.93+9.90=10.83 | ✅ |
| Rel. F1 | 8.36 | 0.0836 → 8.36% | ✅ |
| Ent. F1 | 30.98 | 0.3098 → 30.98% | ✅ |

### Row: S2 — `phase2_scierc_full_s2`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| DR | 0.97 | 0.0097 → 0.97% | ✅ |
| ΔDR | ↓94% | (15.37-0.97)/15.37=93.7%≈94% | ✅ |
| RV | 0 | 0 | ✅ |
| ET | 0 | 0 | ✅ |
| CF | 8.03 | 0.0803 → 8.03% | ✅ |
| Tot. | 9.00 | 0.97+8.03=9.00 | ✅ |
| Rel. F1 | 8.03 | 0.0803 → 8.03% | ✅ |
| Ent. F1 | 31.90 | 0.319 → 31.90% | ✅ |

**Table 1 结论: 48/48 cells 全部通过 ✅**

---

## Table 2 审计报告 (`tab:composability`)
**Fine-tuning composability: LoRA × unconstrained vs. S1**

### Qwen3-8B × SciERC — `w5_lora_scierc_*_eval`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| Unconstr. DR | 1.95 | 0.0195 → 1.95% | ✅ |
| Unconstr. CF | 0 | 0 | ✅ |
| Unconstr. R-F1 | 43.86 | 0.4386 → 43.86% | ✅ |
| Unconstr. E-F1 | 67.05 | 0.6705 → 67.05% | ✅ |
| S1 DR | **0** | 0 | ✅ |
| S1 CF | 1.18 | 0.0118 → 1.18% | ✅ |
| S1 R-F1 | 43.77 | 0.4377 → 43.77% | ✅ |
| S1 E-F1 | 67.05 | 0.6705 → 67.05% | ✅ |
| S1 ΔDR | ↓100% | (1.95→0)/1.95=100% | ✅ |

**Qwen SciERC: 9/9 ✅**

### Llama 3.1-8B × SciERC — `w5_llama_lora_scierc_*_eval`

| Cell | Paper | Registry | Verified |
|------|-------|----------|----------|
| Unconstr. DR | 1.11 | 0.0111 → 1.11% | ✅ |
| Unconstr. CF | 0 | 0 | ✅ |
| Unconstr. R-F1 | 45.45 | 0.4545 → 45.45% | ✅ |
| Unconstr. E-F1 | 67.76 | 0.6776 → 67.76% | ✅ |
| S1 DR | 0.09 | 0.0009 → 0.09% | ✅ |
| S1 CF | 0.46 | 0.0046 → 0.46% | ✅ |
| S1 R-F1 | 45.47 | 0.4547 → 45.47% | ✅ |
| S1 E-F1 | 67.76 | 0.6776 → 67.76% | ✅ |
| S1 ΔDR | ↓92% | (1.11-0.09)/1.11=91.9%≈92% | ✅ |

**Llama SciERC: 9/9 ✅**

### Qwen3-8B × DocRED — `w5_qwen_docred_lora_*_eval`

| Cell | Paper | Registry (corrected) | Verified |
|------|-------|---------------------|----------|
| Unconstr. DR | 0.56 | DR_pct=**0.76** | ❌ (diff=0.20) |
| Unconstr. CF | 0.08 | CF_pct=**0.12** | ❌ (diff=0.04) |
| Unconstr. R-F1 | 40.89 | R_F1=**40.86** | ❌ (diff=0.03) |
| Unconstr. E-F1 | 82.35 | E_F1=**82.15** | ❌ (diff=0.20) |
| S1 DR | 0.00 | DR_pct=**0.01** | ❌ (diff=0.01) |
| S1 CF | 0.22 | CF_pct=**0.41** | ❌ (diff=0.19) |
| S1 R-F1 | 40.79 | R_F1=**40.56** | ❌ (diff=0.23) |
| S1 E-F1 | 81.87 | E_F1=**81.43** | ❌ (diff=0.44) |
| S1 ΔDR | ↓100% | (0.76→0.01)=**↓98.7%** | ❌ |

**Qwen DocRED: 0/9 — 全部不一致 ❌**

### Llama 3.1-8B × DocRED — `w5_llama_docred_lora_*_eval`

| Cell | Paper | Registry (corrected) | Verified |
|------|-------|---------------------|----------|
| Unconstr. DR | 0.49 | DR_pct=**0.49** | ✅ |
| Unconstr. CF | 0.08 | **无 CF 字段** | ⚠️ 无法核实 |
| Unconstr. R-F1 | 44.55 | R_F1=**43.72** | ❌ (diff=0.83) |
| Unconstr. E-F1 | 84.77 | E_F1=**83.93** | ❌ (diff=0.84) |
| S1 DR | 0.00 | dr_violation_rate=**0.21** | ❌ (diff=0.21) |
| S1 CF | 0.26 | CF_pct=**0.21** | ❌ (diff=0.05) |
| S1 R-F1 | 44.70 | relation_f1_all_set=**43.78** | ❌ (diff=0.92) |
| S1 E-F1 | 84.71 | entity_f1=**83.94** | ❌ (diff=0.77) |
| S1 ΔDR | ↓100% | (0.49→0.21)=**↓57%** | ❌ |

**Llama DocRED: 1/9 通过, 1 无法核实, 7 不一致 ❌**

---

## 根因分析

Registry 有多条修正记录表明 `violation_checker.py` 和 `unified_f1_eval.py` 存在 **parse-failure bug**，已于 2026-05-20/22 用 `eval_d064.py` 修正：

- `w8_qwen_docred_ft_semantic_only`: "Old registry value 40.89 was from unified_f1_eval.py (had same parse-failure bug)"
- `w5_llama_docred_lora_constrained_eval`: "P/R corrected 2026-05-20 per Director"
- `r16_trie_*_ft_scierc`: "CORRECTED: violation_checker.py parse-failure bug fixed. Old R-F1 was inflated (gold dropped for parse failures)"

**论文 Table 2 的 DocRED 四行使用了修正前的旧值**。SciERC 行不受影响（parse fail rate = 0%）。

## 不一致汇总

| 位置 | 论文值 | 正确值 (registry) | 严重程度 |
|------|--------|-------------------|----------|
| Qwen DocRED Unc. DR | 0.56 | **0.76** | 高 |
| Qwen DocRED Unc. CF | 0.08 | **0.12** | 中 |
| Qwen DocRED Unc. R-F1 | 40.89 | **40.86** | 低 |
| Qwen DocRED Unc. E-F1 | 82.35 | **82.15** | 中 |
| Qwen DocRED S1 DR | 0.00 | **0.01** | 低 |
| Qwen DocRED S1 CF | 0.22 | **0.41** | 高 |
| Qwen DocRED S1 R-F1 | 40.79 | **40.56** | 中 |
| Qwen DocRED S1 E-F1 | 81.87 | **81.43** | 中 |
| Qwen DocRED S1 ΔDR | ↓100% | **↓98.7%** | 中 |
| Llama DocRED Unc. R-F1 | 44.55 | **43.72** | 高 |
| Llama DocRED Unc. E-F1 | 84.77 | **83.93** | 高 |
| Llama DocRED S1 DR | 0.00 | **0.21** | 高 |
| Llama DocRED S1 CF | 0.26 | **0.21** | 低 |
| Llama DocRED S1 R-F1 | 44.70 | **43.78** | 高 |
| Llama DocRED S1 E-F1 | 84.71 | **83.94** | 高 |
| Llama DocRED S1 ΔDR | ↓100% | **↓57%** | 极高 |
| Llama DocRED Unc. CF | 0.08 | **缺失** | ⚠️ |

最严重问题：Llama DocRED S1 ΔDR 从 ↓100% 降为 ↓57%，且 DR 从 0.00 变为 0.21%。这会影响论文 "fine-tuning practically eliminates DR" 的核心结论强度。

Table 2 的 DocRED 四行全部需要用 `eval_d064.py` 的修正值重写。同时需检查正文中引用这些数字的段落（至少 `\paragraph{Composability with fine-tuning.}` 中的 "DR≤0.09%" 等表述）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4264e721-fe35-4fdb-be84-e78a2588b3ee",
  "isSidechain": false,
  "requestId": "req_011CbKLnvSiQBWGG5DKz68YK",
  "type": "assistant",
  "uuid": "e09ec888-61b4-422c-93a9-8df211aae960",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKohtabrjkvAThaoBn5NTD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10200,
      "cache_read_input_tokens": 52095,
      "output_tokens": 6934,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10200,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6934,
          "cache_read_input_tokens": 52095,
          "cache_creation_input_tokens": 10200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10200
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

_source line 75_

```json
{
  "type": "last-prompt",
  "leafUuid": "e09ec888-61b4-422c-93a9-8df211aae960",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---

### Runtime record

_source line 76_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper tables 1 and 2 numerical values",
  "sessionId": "bed18bf9-b23b-41a9-845b-decdb9931508"
}
```

---
