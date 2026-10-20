# Research conversation: <project_context> # 项目: collapse_severity_monitor ## 运行环境 - 服务器名: autodl-5090 - SSH 账户: root（调用 ssh_execute / submit_tra

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/dd1c4acf-86f3-4cc6-966e-3016d5c01262.jsonl`
- **Structured JSON:** [`4ab8b65c9b6ae38ee1b8.json`](../../sessions/4a/4ab8b65c9b6ae38ee1b8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T21:52:38.074Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T21:52:38.074Z",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262",
  "content": "&lt;project_context>\n# 项目: collapse_severity_monitor\n\n## 运行环境\n- 服务器名: autodl-5090\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/collapse_severity_monitor\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: SIGMA expected_direction=+1 是 provisional 假设（N=2），禁止在论文或分析中当已验证结论使用（原因：Reviewer warning: (1) N=2 数据点下方向判断是 tautology；(2) \"within-gen corruption vs recursive collapse\" 边界模糊——我们的 pipeline 本身就是跨代递归的；(3) 将方向差异包装为\"discussion 亮点\"属于 rationalization。等 plan_001 seed43-46 × 6 fractions + plan_003 Full FT 数据后重新验证。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## Task: Rewrite Method Section (§3)\n\nRewrite the Method section for an EMNLP 2026 (ACL Rolling Review) long paper on training dynamic signals as model collapse severity monitors.\n\n### Instructions\n\n1. **First**: Read the writing style guide at `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n2. **Then**: Read the existing method section at `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex`\n3. **Rewrite** the file at the same path, preserving the good structure but updating per the spec below.\n\n### Section Outline (word budget: ~1100 words)\n\n**§3.1 Iterative Training Protocol**\n- Fine-tune M₀ (pretrained) → M₁ → ... → M_g using synthetic data from M_{g-1}\n- Each generation: fine-tune on dataset mixed at fraction α, generate synthetic data, mix for next gen\n- Key detail: each generation initializes from SAME pretrained weights M₀ (isolate data effect from weight drift)\n- Document: temperature=1.0, top-p=0.95, max_length=480+32, 1500 chunks for generation\n\n**§3.2 Contamination Fractions**\n- α ∈ {0%, 10%, 25%, 50%, 75%, 100%}\n- 0% = clean baseline (controls for training noise)\n- 100% = full replacement (maximum collapse pressure)\n\n**§3.3 Monitoring Signals — 4 families**\nKeep the existing mathematical definitions (they're good), but update:\n- **(a) Spectral**: stable_rank and spectral_entropy. IMPORTANT: stable_rank ↑ under collapse = energy dispersal (‖W‖²_F grows faster than σ₁²), NOT concentration. Keep the existing footnote distinguishing participation ratio from matrix stable rank.\n- **(b) Output**: perplexity and token_entropy. MUST explicitly distinguish training PPL (fit to current batch, potentially contaminated) vs evaluation PPL (held-out clean set). This distinction is critical for the within-gen detection results.\n- **(c) Gradient**: gradient_norm. Note non-monotonic behavior under QLoRA.\n- **(d) Downstream**: HellaSwag accuracy.\n\n**§3.4 Experimental Configurations — Table 4**\nAdd a configuration summary table (tab4_config). Configurations:\n\n| ID | Model | Params | Dataset | Domain | Fractions (α) | Seeds | Method | Trainable |\n|----|-------|--------|---------|--------|---------------|-------|--------|-----------|\n| C1 | Qwen2.5-0.5B | 494M | WikiText-2 | General | {0,0.5,1.0} | 1 | QLoRA r=16 | 0.8% |\n| C2 | Qwen2.5-1.5B | 1.5B | WikiText-2 | General | {0,0.1,...,1.0} | 5 | QLoRA r=16 | 0.5% |\n| C3 | Qwen2.5-1.5B | 1.5B | PubMed | Biomedical | {0,0.5,1.0} | 3 | QLoRA r=16 | 0.5% |\n| C4 | Qwen2.5-0.5B | 494M | WikiText-2 | General | {0,0.5,1.0} | 1 | Full FT | 100% |\n| C5 | Qwen2.5-3B | 3B | WikiText-2 | General | {0,0.5,1.0} | 1 | QLoRA r=16 | 0.3% |\n\nNote in text: C1 provides initial signal discovery, C2 is the primary analysis (5-seed statistical power), C3 tests cross-domain, C4 tests method-dependence, C5 provides scale spot-check.\n\n**§3.5 Evaluation Framework**\nUpdate from existing but make cleaner:\n- (a) Cross-gen severity: Spearman ρ + bootstrap CI, Cohen's d effect sizes (PRIMARY evidence)\n- (b) Within-gen detection: ROC with **clustered bootstrap** (one observation per fraction×seed to avoid inflating AUC from serial generation dependence) — explain WHY clustered bootstrap is necessary\n- (c) Method-dependence: paired comparison across QLoRA/Full FT\n\n### Style Constraints\n\n- NO footnotes about \"pending\" or \"in progress\" experiments — write definitively\n- All signals computed every 50 steps via training callback on held-out validation set\n- QLoRA: r=16, α_LoRA=32, dropout 0.05, NF4 quantized base, target all linear projections\n- Full FT: same hyperparameters as QLoRA but all parameters trainable, no quantization\n- Training: AdamW, lr=2e-4, weight_decay=0.01, 5% warmup, grad clip 1.0, 5 epochs, effective batch 16, bf16\n- Use \\citep{} for parenthetical citations, \\citet{} for textual\n- Available citation keys: dettmers2023qlora, hu2022lora, merity2017pointer, zellers2019hellaswag, Shumailov2024, Martin2021, Sanyal2020\n- Use \\label{sec:method}, \\label{sec:protocol}, \\label{sec:signals}, \\label{sec:evaluation}\n- The section header should be \\section{Methodology}\\label{sec:method}\n- Keep equations: eq:mixing, eq:stable_rank, eq:spectral_entropy, eq:token_entropy, eq:perplexity, eq:deviation\n\n### Output\n\nWrite the complete rewritten method.tex to:\n`/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex`\n\nDo NOT include \\begin{document} or preamble — this file is \\input'd from main.tex."
}
```

---

### Runtime record

_source line 2 · 2026-05-15T21:52:38.077Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T21:52:38.077Z",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262"
}
```

---

## Round 1

21 recorded events

### User

_source line 3 · 2026-05-15T21:52:38.123Z_

&lt;project_context>
# 项目: collapse_severity_monitor

## 运行环境
- 服务器名: autodl-5090
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/collapse_severity_monitor

## ⚠️ 活跃约束（必须遵守）

- **C001**: SIGMA expected_direction=+1 是 provisional 假设（N=2），禁止在论文或分析中当已验证结论使用（原因：Reviewer warning: (1) N=2 数据点下方向判断是 tautology；(2) "within-gen corruption vs recursive collapse" 边界模糊——我们的 pipeline 本身就是跨代递归的；(3) 将方向差异包装为"discussion 亮点"属于 rationalization。等 plan_001 seed43-46 × 6 fractions + plan_003 Full FT 数据后重新验证。）


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## Task: Rewrite Method Section (§3)

Rewrite the Method section for an EMNLP 2026 (ACL Rolling Review) long paper on training dynamic signals as model collapse severity monitors.

### Instructions

1. **First**: Read the writing style guide at `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`
2. **Then**: Read the existing method section at `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex`
3. **Rewrite** the file at the same path, preserving the good structure but updating per the spec below.

### Section Outline (word budget: ~1100 words)

**§3.1 Iterative Training Protocol**
- Fine-tune M₀ (pretrained) → M₁ → ... → M_g using synthetic data from M_{g-1}
- Each generation: fine-tune on dataset mixed at fraction α, generate synthetic data, mix for next gen
- Key detail: each generation initializes from SAME pretrained weights M₀ (isolate data effect from weight drift)
- Document: temperature=1.0, top-p=0.95, max_length=480+32, 1500 chunks for generation

**§3.2 Contamination Fractions**
- α ∈ {0%, 10%, 25%, 50%, 75%, 100%}
- 0% = clean baseline (controls for training noise)
- 100% = full replacement (maximum collapse pressure)

**§3.3 Monitoring Signals — 4 families**
Keep the existing mathematical definitions (they're good), but update:
- **(a) Spectral**: stable_rank and spectral_entropy. IMPORTANT: stable_rank ↑ under collapse = energy dispersal (‖W‖²_F grows faster than σ₁²), NOT concentration. Keep the existing footnote distinguishing participation ratio from matrix stable rank.
- **(b) Output**: perplexity and token_entropy. MUST explicitly distinguish training PPL (fit to current batch, potentially contaminated) vs evaluation PPL (held-out clean set). This distinction is critical for the within-gen detection results.
- **(c) Gradient**: gradient_norm. Note non-monotonic behavior under QLoRA.
- **(d) Downstream**: HellaSwag accuracy.

**§3.4 Experimental Configurations — Table 4**
Add a configuration summary table (tab4_config). Configurations:

| ID | Model | Params | Dataset | Domain | Fractions (α) | Seeds | Method | Trainable |
|----|-------|--------|---------|--------|---------------|-------|--------|-----------|
| C1 | Qwen2.5-0.5B | 494M | WikiText-2 | General | {0,0.5,1.0} | 1 | QLoRA r=16 | 0.8% |
| C2 | Qwen2.5-1.5B | 1.5B | WikiText-2 | General | {0,0.1,...,1.0} | 5 | QLoRA r=16 | 0.5% |
| C3 | Qwen2.5-1.5B | 1.5B | PubMed | Biomedical | {0,0.5,1.0} | 3 | QLoRA r=16 | 0.5% |
| C4 | Qwen2.5-0.5B | 494M | WikiText-2 | General | {0,0.5,1.0} | 1 | Full FT | 100% |
| C5 | Qwen2.5-3B | 3B | WikiText-2 | General | {0,0.5,1.0} | 1 | QLoRA r=16 | 0.3% |

Note in text: C1 provides initial signal discovery, C2 is the primary analysis (5-seed statistical power), C3 tests cross-domain, C4 tests method-dependence, C5 provides scale spot-check.

**§3.5 Evaluation Framework**
Update from existing but make cleaner:
- (a) Cross-gen severity: Spearman ρ + bootstrap CI, Cohen's d effect sizes (PRIMARY evidence)
- (b) Within-gen detection: ROC with **clustered bootstrap** (one observation per fraction×seed to avoid inflating AUC from serial generation dependence) — explain WHY clustered bootstrap is necessary
- (c) Method-dependence: paired comparison across QLoRA/Full FT

### Style Constraints

- NO footnotes about "pending" or "in progress" experiments — write definitively
- All signals computed every 50 steps via training callback on held-out validation set
- QLoRA: r=16, α_LoRA=32, dropout 0.05, NF4 quantized base, target all linear projections
- Full FT: same hyperparameters as QLoRA but all parameters trainable, no quantization
- Training: AdamW, lr=2e-4, weight_decay=0.01, 5% warmup, grad clip 1.0, 5 epochs, effective batch 16, bf16
- Use \citep{} for parenthetical citations, \citet{} for textual
- Available citation keys: dettmers2023qlora, hu2022lora, merity2017pointer, zellers2019hellaswag, Shumailov2024, Martin2021, Sanyal2020
- Use \label{sec:method}, \label{sec:protocol}, \label{sec:signals}, \label{sec:evaluation}
- The section header should be \section{Methodology}\label{sec:method}
- Keep equations: eq:mixing, eq:stable_rank, eq:spectral_entropy, eq:token_entropy, eq:perplexity, eq:deviation

### Output

Write the complete rewritten method.tex to:
`/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex`

Do NOT include \begin{document} or preamble — this file is \input'd from main.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ae09a607-e5a2-46f5-8d19-601dcf6d2541",
  "type": "user",
  "uuid": "9484da0a-61ad-4faf-b484-fa20b9fdbda4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T21:52:38.122Z_

```json
{
  "parentUuid": "9484da0a-61ad-4faf-b484-fa20b9fdbda4",
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
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
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
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "56f98470-93df-41df-af5b-7c9a0d06c061",
  "timestamp": "2026-05-15T21:52:38.122Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T21:52:38.122Z_

```json
{
  "parentUuid": "56f98470-93df-41df-af5b-7c9a0d06c061",
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
  "uuid": "a02fd301-de63-4a62-a5f4-f91200256609",
  "timestamp": "2026-05-15T21:52:38.122Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T21:52:38.122Z_

```json
{
  "parentUuid": "a02fd301-de63-4a62-a5f4-f91200256609",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "08ef3bf9-7d4f-410e-9542-701dd9e497d4",
  "timestamp": "2026-05-15T21:52:38.122Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262",
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
  "aiTitle": "Rewrite Method section for collapse severity monitor paper",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262"
}
```

---

### Assistant

_source line 8 · 2026-05-15T21:52:41.325Z_

I'll start by reading the style guide and the existing method section in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08ef3bf9-7d4f-410e-9542-701dd9e497d4",
  "isSidechain": false,
  "requestId": "req_011Cb56YTMxsuGv6cki3QNAE",
  "type": "assistant",
  "uuid": "5e0167aa-9a1e-474a-bfa5-52387e6399b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AkDkbdqaTqdLLzF4MRcERT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12860,
      "cache_read_input_tokens": 11841,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 162,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12860
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

_source line 9 · 2026-05-15T21:52:41.928Z_

<details open><summary>🔧 Tool call — Read · `toolu_011bkp5WhX6efUkuF5R6yHpF`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e0167aa-9a1e-474a-bfa5-52387e6399b5",
  "isSidechain": false,
  "requestId": "req_011Cb56YTMxsuGv6cki3QNAE",
  "type": "assistant",
  "uuid": "dd14ae0d-99b2-4cb1-bbd6-ebf635716c39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AkDkbdqaTqdLLzF4MRcERT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12860,
      "cache_read_input_tokens": 11841,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 162,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12860
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

_source line 10 · 2026-05-15T21:52:41.959Z_

<details><summary>↩ Tool result · `toolu_011bkp5WhX6efUkuF5R6yHpF`</summary>

````text
1	---
2	name: latex-paper
3	description: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。
4	scope: global
5	tags:
6	- latex
7	- paper-writing
8	- academic
9	- citation
10	- submission
11	version: 1
12	roles:
13	- agent
14	- worker
15	---
16	
17	# LaTeX 论文写作全流程
18	
19	ML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。
20	
21	---
22	
23	## 1. 工作模式
24	
25	开始前选择模式：
26	
27	| 模式 | 说明 | 适用 |
28	|------|------|------|
29	| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |
30	| **Improve** | 改写已有章节，强化论证 | 修改稿 |
31	| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |
32	
33	---
34	
35	## 2. Claim-Evidence 方法论
36	
37	**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**
38	
39	### 2.1 一句话贡献
40	
41	在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。
42	
43	### 2.2 Claim-Evidence Map
44	
45	为每个 contribution 建立 claim→evidence 映射表：
46	
47	| Contribution | Claim | Evidence | Table/Figure |
48	|-------------|-------|----------|-------------|
49	| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |
50	| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |
51	| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |
52	
53	**没有直接证据支撑的 claim 必须删除或降级为 discussion。**
54	
55	### 2.3 章节起草顺序
56	
57	```
58	1. Introduction + Experiments（先确定 claim 和 evidence）
59	2. Method（评估问题稳定后再写细节）
60	3. Related Work
61	4. Abstract + Title（核心 claim 定型后最后写）
62	```
63	
64	### 2.4 Quality Gates
65	
66	投稿前必须通过：
67	- [ ] 前两段出现显式 novelty 声明
68	- [ ] 每个 contribution 有可验证的 evidence
69	- [ ] Abstract / Intro / Conclusion 的 claim 一致
70	- [ ] Limitations 真实且技术性诚实
71	- [ ] 审稿人两分钟内能识别 delta
72	
73	---
74	
75	## 3. 引用防幻觉（CRITICAL）
76	
77	**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**
78	
79	### 3.1 黄金法则
80	
81	```
82	IF 无法程序化获取引用:
83	    → 标记 [CITATION NEEDED] 或 \cite{PLACEHOLDER_verify}
84	    → 明确告知用户
85	    → 绝不编造看似合理的引用
86	```
87	
88	### 3.2 五步验证流程
89	
90	```
91	1. SEARCH  → Semantic Scholar API 搜索关键词
92	2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）
93	3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）
94	4. CHECK   → 确认你引用的 claim 确实出自该论文
95	5. ADD     → 加入 .bib 文件
96	```
97	
98	### 3.3 API 速查
99	
100	| API | 用途 | 限制 |
101	|-----|------|------|
102	| **Semantic Scholar** | ML/AI 论文搜索 | 1 RPS (免费) |
103	| **CrossRef** | DOI → BibTeX | 需 mailto 头 |
104	| **arXiv** | 预印本搜索 | 3s 间隔 |
105	
106	```python
107	# DOI → BibTeX（最可靠的方式）
108	import requests
109	def doi_to_bibtex(doi: str) -> str:
110	    r = requests.get(f"https://doi.org/{doi}",
111	                     headers={"Accept": "application/x-bibtex"})
112	    r.raise_for_status()
113	    return r.text
114	
115	# Semantic Scholar 搜索
116	from semanticscholar import SemanticScholar
117	sch = SemanticScholar()
118	results = sch.search_paper("attention mechanism transformers", limit=5)
119	for p in results:
120	    print(f"{p.title} | DOI: {p.externalIds.get('DOI', 'N/A')}")
121	```
122	
123	### 3.4 引用处理规则
124	
125	| 情况 | 处理 |
126	|------|------|
127	| 找到论文 + DOI + BibTeX | 直接用 |
128	| 找到论文，无 DOI | 用 arXiv BibTeX |
129	| 论文存在但无法获取 BibTeX | 标记 placeholder，告知用户 |
130	| 不确定论文是否存在 | 标记 `[CITATION NEEDED]`，告知用户 |
131	| "我觉得有篇关于 X 的论文" | **绝不引用** — 先搜索或标记 |
132	
133	---
134	
135	## 4. 顶会模板速查
136	
137	### 4.1 ML/AI 会议
138	
139	| 会议 | 页数限制 | 主文件 | 样式文件 | 必须项 |
140	|------|---------|--------|---------|--------|
141	| **NeurIPS** | 9 页 | `main.tex` | `neurips.sty` | Paper Checklist |
142	| **ICML** | 8 页 (+1 camera-ready) | `example_paper.tex` | `icml2026.sty` | Broader Impact |
143	| **ICLR** | 9 页 (+1) | `iclr_conference.tex` | `iclr_conference.sty` | LLM 使用声明 |
144	| **ACL/EMNLP** | 8 页 (long) | `acl_latex.tex` | `acl.sty` | Limitations 必须 |
145	| **AAAI** | 7 页 (+1) | `aaai_template.tex` | `aaai.sty` | 严格样式 |
146	| **COLM** | 9 页 (+1) | `colm_conference.tex` | `colm_conference.sty` | 语言模型聚焦 |
147	
148	### 4.2 系统会议
149	
150	| 会议 | 页数限制 | 模板类型 | 关键要求 |
151	|------|---------|---------|---------|
152	| **OSDI** | 12 页 (+2) | USENIX `usenix.sty` | Research / Operational 双 track |
153	| **NSDI** | 12 页 | USENIX | Introduction 预筛 |
154	| **ASPLOS** | 12 页 | ACM `acmart.cls (sigplan)` | 前 2 页快速评审 |
155	| **SOSP** | 12 页 | ACM `acmart.cls (sigplan)` | 可选 Artifact Evaluation |
156	
157	### 4.3 模板使用原则
158	
159	```bash
160	# 1. 复制整个模板目录（不要只拷 .tex）
161	cp -r templates/neurips2025/ ~/papers/my-paper/
162	
163	# 2. 先编译未修改的模板，确认能跑通
164	latexmk -pdf main.tex
165	
166	# 3. 逐章替换内容，频繁编译
167	```
168	
169	**禁止事项：**
170	- 不要修改 `.sty` 文件
171	- 不要在会议模板间复制 `\usepackage` 行
172	- 不要只复制 `.tex` 而不带 `.sty/.bst`
173	
174	---
175	
176	## 5. 写作规范
177	
178	### 5.1 时间分配（Neel Nanda）
179	
180	花**大致相等**的时间在：
181	1. Abstract
182	2. Introduction
183	3. 图表
184	4. **其余所有内容加起来**
185	
186	审稿人读论文的顺序：标题 → 摘要 → 引言 → 图表 → 也许正文。
187	
188	### 5.2 Abstract 五句法（Sebastian Farquhar）
189	
190	```
191	1. 你做了什么（"We introduce/prove/demonstrate..."）
192	2. 为什么这很难且重要
193	3. 怎么做的（含专业关键词以便检索）
194	4. 有什么证据
195	5. 最惊人的数字/结果
196	```
197	
198	删除一切泛泛的开头：~~"Large language models have achieved remarkable success..."~~
199	
200	### 5.3 句子级清晰度（Gopen & Swan）
201	
202	| 原则 | 规则 |
203	|------|------|
204	| 主谓紧邻 | 不要在主语和动词之间插入长从句 |
205	| 重点在句尾 | 把关键数字/结论放在句末 |
206	| 旧信息在前 | 先放读者已知的内容，再引入新概念 |
207	| 动词表达动作 | "We analyzed" 而非 "We performed an analysis" |
208	
209	### 5.4 常见修改
210	
211	| 问题 | 修复 |
212	|------|------|
213	| Abstract 太泛 | 删第一句（如果它能放在任何 ML 论文前面） |
214	| Introduction 超 1.5 页 | 背景挪到 Related Work |
215	| 实验没有显式 claim | 每个实验前加 "This tests whether..." |
216	| 缺统计显著性 | 加 error bars + 运行次数 + 计算方法 |
217	
218	---
219	
220	## 6. 投稿工程链
221	
222	### 6.1 构建
223	
224	```bash
225	# 推荐：latexmk 一键构建
226	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
227	
228	# 手动：需要多次编译
229	pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
230	```
231	
232	### 6.2 Lint + 格式化
233	
234	```bash
235	# Lint: 检查常见 LaTeX 问题
236	chktex main.tex
237	
238	# 格式化: 减少 diff 噪声
239	latexindent -w main.tex
240	```
241	
242	### 6.3 图表格式
243	
244	| 类型 | 格式 | 说明 |
245	|------|------|------|
246	| 矢量图（plot、diagram） | PDF | matplotlib: `plt.savefig('fig.pdf')` |
247	| 照片/heatmap | PNG 600dpi 或 TIFF | 栅格图 |
248	| 表格 | `booktabs` 包 | `\toprule/\midrule/\bottomrule` |
249	
250	```latex
251	\usepackage{booktabs}
252	\begin{tabular}{lcc}
253	\toprule
254	Method & Accuracy $\uparrow$ & Latency $\downarrow$ \\
255	\midrule
256	Baseline & 85.2 & 45ms \\
257	\textbf{Ours} & \textbf{92.1} & 38ms \\
258	\bottomrule
259	\end{tabular}
260	```
261	
262	**图表规范：**
263	- 用色盲友好色板（Okabe-Ito 或 Paul Tol）
264	- 图内不放标题（用 caption）
265	- Caption 独立可理解（不依赖正文）
266	- 最佳值加粗，标注方向符号（↑ 越高越好，↓ 越低越好）
267	
268	### 6.4 投稿打包
269	
270	```bash
271	# 清理辅助文件
272	latexmk -c
273	
274	# 打包投稿
275	zip -r submission.zip main.tex *.sty *.bst *.bib figures/ --exclude='*.aux' --exclude='*.log'
276	```
277	
278	### 6.5 常见失败点
279	
280	| 问题 | 解决 |
281	|------|------|
282	| 图片格式混用导致编译失败 | 统一用 PDF |
283	| 字体未嵌入 | `pdffonts output.pdf` 检查 |
284	| Overfull box 过多 | 关键位置手动调行 |
285	| 引用缺字段 | 检查 DOI/年份/期刊名 |
286	| 超页数 | 用 `\vspace{-Xpt}` 微调，或精简内容 |
287	
288	---
289	
290	## 7. 会议转投
291	
292	当论文被拒或转投其他会议时：
293	
294	### 7.1 ML/AI 会议间转换
295	
296	| 转换 | 页数变化 | 关键调整 |
297	|------|---------|---------|
298	| NeurIPS → ICML | 9→8 | 删 1 页，加 Broader Impact |
299	| ICML → ICLR | 8→9 | 可扩展实验 + LLM 声明 |
300	| NeurIPS → ACL | 9→8 | 按 NLP 惯例重组 + Limitations |
301	| ICLR → AAAI | 9→7 | 大幅精简，严格样式 |
302	
303	### 7.2 转投原则
304	
305	1. **永远用目标模板重新开始** — 复制目标模板，迁移内容，不要合并 preamble
306	2. **只迁移正文内容** — 不复制 `\usepackage`、header/footer 命令
307	3. **根据审稿意见改进** — 但不要在新稿中提及旧投稿（双盲）
308	4. **检查目标会议特殊要求** — checklist、ethics statement、LLM 声明等
309	
310	---
311	
312	## 8. 投前清单
313	
314	### 通用清单
315	
316	- [ ] Abstract/Intro/Conclusion 的 claim 一致
317	- [ ] 每个 contribution 有对应 evidence
318	- [ ] 所有引用已程序化验证（无幻觉引用）
319	- [ ] Error bars + 运行次数 + 统计方法
320	- [ ] Limitations 章节存在且诚实
321	- [ ] 匿名化（双盲审稿）
322	- [ ] 符合页数限制
323	- [ ] 所有图表有自包含 caption
324	- [ ] `.bib` 中无缺失字段
325	- [ ] PDF 编译无 warning
326	
327	### 会议特定
328	
329	| 会议 | 额外要求 |
330	|------|---------|
331	| NeurIPS | 16 项 Paper Checklist（附录，不计页数） |
332	| ICML | Broader Impact Statement |
333	| ICLR | LLM 使用声明 |
334	| ACL/EMNLP | Limitations 章节（必须），Ethics Statement |
335	| AAAI | 严格样式文件合规 |
336	
337	---
338	
339	## 参考资源
340	
341	**写作方法论：**
342	- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/) — What/Why/So What 框架
343	- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 五句法 Abstract
344	- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 读者预期 7 原则
345	- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — 用词
346	- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — 微观清晰度
347	
348	**API：**
349	- [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | [CrossRef](https://www.crossref.org/documentation/) | [arXiv](https://info.arxiv.org/help/api/)
350	
351	**会议官方：**
352	- [NeurIPS](https://neurips.cc/) | [ICML](https://icml.cc/) | [ICLR](https://iclr.cc/) | [ACL](https://www.aclweb.org/) | [AAAI](https://aaai.org/) | [EMNLP](https://2025.emnlp.org/)
353	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "dd14ae0d-99b2-4cb1-bbd6-ebf635716c39",
  "isSidechain": false,
  "promptId": "ae09a607-e5a2-46f5-8d19-601dcf6d2541",
  "type": "user",
  "uuid": "26f5bfae-b8a8-43bd-8d17-d3bacbc4645e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md",
      "content": "---\nname: latex-paper\ndescription: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。\nscope: global\ntags:\n- latex\n- paper-writing\n- academic\n- citation\n- submission\nversion: 1\nroles:\n- agent\n- worker\n---\n\n# LaTeX 论文写作全流程\n\nML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。\n\n---\n\n## 1. 工作模式\n\n开始前选择模式：\n\n| 模式 | 说明 | 适用 |\n|------|------|------|\n| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |\n| **Improve** | 改写已有章节，强化论证 | 修改稿 |\n| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |\n\n---\n\n## 2. Claim-Evidence 方法论\n\n**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**\n\n### 2.1 一句话贡献\n\n在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。\n\n### 2.2 Claim-Evidence Map\n\n为每个 contribution 建立 claim→evidence 映射表：\n\n| Contribution | Claim | Evidence | Table/Figure |\n|-------------|-------|----------|-------------|\n| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |\n| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |\n| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |\n\n**没有直接证据支撑的 claim 必须删除或降级为 discussion。**\n\n### 2.3 章节起草顺序\n\n```\n1. Introduction + Experiments（先确定 claim 和 evidence）\n2. Method（评估问题稳定后再写细节）\n3. Related Work\n4. Abstract + Title（核心 claim 定型后最后写）\n```\n\n### 2.4 Quality Gates\n\n投稿前必须通过：\n- [ ] 前两段出现显式 novelty 声明\n- [ ] 每个 contribution 有可验证的 evidence\n- [ ] Abstract / Intro / Conclusion 的 claim 一致\n- [ ] Limitations 真实且技术性诚实\n- [ ] 审稿人两分钟内能识别 delta\n\n---\n\n## 3. 引用防幻觉（CRITICAL）\n\n**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**\n\n### 3.1 黄金法则\n\n```\nIF 无法程序化获取引用:\n    → 标记 [CITATION NEEDED] 或 \\cite{PLACEHOLDER_verify}\n    → 明确告知用户\n    → 绝不编造看似合理的引用\n```\n\n### 3.2 五步验证流程\n\n```\n1. SEARCH  → Semantic Scholar API 搜索关键词\n2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）\n3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）\n4. CHECK   → 确认你引用的 claim 确实出自该论文\n5. ADD     → 加入 .bib 文件\n```\n\n### 3.3 API 速查\n\n| API | 用途 | 限制 |\n|-----|------|------|\n| **Semantic Scholar** | ML/AI 论文搜索 | 1 RPS (免费) |\n| **CrossRef** | DOI → BibTeX | 需 mailto 头 |\n| **arXiv** | 预印本搜索 | 3s 间隔 |\n\n```python\n# DOI → BibTeX（最可靠的方式）\nimport requests\ndef doi_to_bibtex(doi: str) -> str:\n    r = requests.get(f\"https://doi.org/{doi}\",\n                     headers={\"Accept\": \"application/x-bibtex\"})\n    r.raise_for_status()\n    return r.text\n\n# Semantic Scholar 搜索\nfrom semanticscholar import SemanticScholar\nsch = SemanticScholar()\nresults = sch.search_paper(\"attention mechanism transformers\", limit=5)\nfor p in results:\n    print(f\"{p.title} | DOI: {p.externalIds.get('DOI', 'N/A')}\")\n```\n\n### 3.4 引用处理规则\n\n| 情况 | 处理 |\n|------|------|\n| 找到论文 + DOI + BibTeX | 直接用 |\n| 找到论文，无 DOI | 用 arXiv BibTeX |\n| 论文存在但无法获取 BibTeX | 标记 placeholder，告知用户 |\n| 不确定论文是否存在 | 标记 `[CITATION NEEDED]`，告知用户 |\n| \"我觉得有篇关于 X 的论文\" | **绝不引用** — 先搜索或标记 |\n\n---\n\n## 4. 顶会模板速查\n\n### 4.1 ML/AI 会议\n\n| 会议 | 页数限制 | 主文件 | 样式文件 | 必须项 |\n|------|---------|--------|---------|--------|\n| **NeurIPS** | 9 页 | `main.tex` | `neurips.sty` | Paper Checklist |\n| **ICML** | 8 页 (+1 camera-ready) | `example_paper.tex` | `icml2026.sty` | Broader Impact |\n| **ICLR** | 9 页 (+1) | `iclr_conference.tex` | `iclr_conference.sty` | LLM 使用声明 |\n| **ACL/EMNLP** | 8 页 (long) | `acl_latex.tex` | `acl.sty` | Limitations 必须 |\n| **AAAI** | 7 页 (+1) | `aaai_template.tex` | `aaai.sty` | 严格样式 |\n| **COLM** | 9 页 (+1) | `colm_conference.tex` | `colm_conference.sty` | 语言模型聚焦 |\n\n### 4.2 系统会议\n\n| 会议 | 页数限制 | 模板类型 | 关键要求 |\n|------|---------|---------|---------|\n| **OSDI** | 12 页 (+2) | USENIX `usenix.sty` | Research / Operational 双 track |\n| **NSDI** | 12 页 | USENIX | Introduction 预筛 |\n| **ASPLOS** | 12 页 | ACM `acmart.cls (sigplan)` | 前 2 页快速评审 |\n| **SOSP** | 12 页 | ACM `acmart.cls (sigplan)` | 可选 Artifact Evaluation |\n\n### 4.3 模板使用原则\n\n```bash\n# 1. 复制整个模板目录（不要只拷 .tex）\ncp -r templates/neurips2025/ ~/papers/my-paper/\n\n# 2. 先编译未修改的模板，确认能跑通\nlatexmk -pdf main.tex\n\n# 3. 逐章替换内容，频繁编译\n```\n\n**禁止事项：**\n- 不要修改 `.sty` 文件\n- 不要在会议模板间复制 `\\usepackage` 行\n- 不要只复制 `.tex` 而不带 `.sty/.bst`\n\n---\n\n## 5. 写作规范\n\n### 5.1 时间分配（Neel Nanda）\n\n花**大致相等**的时间在：\n1. Abstract\n2. Introduction\n3. 图表\n4. **其余所有内容加起来**\n\n审稿人读论文的顺序：标题 → 摘要 → 引言 → 图表 → 也许正文。\n\n### 5.2 Abstract 五句法（Sebastian Farquhar）\n\n```\n1. 你做了什么（\"We introduce/prove/demonstrate...\"）\n2. 为什么这很难且重要\n3. 怎么做的（含专业关键词以便检索）\n4. 有什么证据\n5. 最惊人的数字/结果\n```\n\n删除一切泛泛的开头：~~\"Large language models have achieved remarkable success...\"~~\n\n### 5.3 句子级清晰度（Gopen & Swan）\n\n| 原则 | 规则 |\n|------|------|\n| 主谓紧邻 | 不要在主语和动词之间插入长从句 |\n| 重点在句尾 | 把关键数字/结论放在句末 |\n| 旧信息在前 | 先放读者已知的内容，再引入新概念 |\n| 动词表达动作 | \"We analyzed\" 而非 \"We performed an analysis\" |\n\n### 5.4 常见修改\n\n| 问题 | 修复 |\n|------|------|\n| Abstract 太泛 | 删第一句（如果它能放在任何 ML 论文前面） |\n| Introduction 超 1.5 页 | 背景挪到 Related Work |\n| 实验没有显式 claim | 每个实验前加 \"This tests whether...\" |\n| 缺统计显著性 | 加 error bars + 运行次数 + 计算方法 |\n\n---\n\n## 6. 投稿工程链\n\n### 6.1 构建\n\n```bash\n# 推荐：latexmk 一键构建\nlatexmk -pdf -interaction=nonstopmode -halt-on-error main.tex\n\n# 手动：需要多次编译\npdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex\n```\n\n### 6.2 Lint + 格式化\n\n```bash\n# Lint: 检查常见 LaTeX 问题\nchktex main.tex\n\n# 格式化: 减少 diff 噪声\nlatexindent -w main.tex\n```\n\n### 6.3 图表格式\n\n| 类型 | 格式 | 说明 |\n|------|------|------|\n| 矢量图（plot、diagram） | PDF | matplotlib: `plt.savefig('fig.pdf')` |\n| 照片/heatmap | PNG 600dpi 或 TIFF | 栅格图 |\n| 表格 | `booktabs` 包 | `\\toprule/\\midrule/\\bottomrule` |\n\n```latex\n\\usepackage{booktabs}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Accuracy $\\uparrow$ & Latency $\\downarrow$ \\\\\n\\midrule\nBaseline & 85.2 & 45ms \\\\\n\\textbf{Ours} & \\textbf{92.1} & 38ms \\\\\n\\bottomrule\n\\end{tabular}\n```\n\n**图表规范：**\n- 用色盲友好色板（Okabe-Ito 或 Paul Tol）\n- 图内不放标题（用 caption）\n- Caption 独立可理解（不依赖正文）\n- 最佳值加粗，标注方向符号（↑ 越高越好，↓ 越低越好）\n\n### 6.4 投稿打包\n\n```bash\n# 清理辅助文件\nlatexmk -c\n\n# 打包投稿\nzip -r submission.zip main.tex *.sty *.bst *.bib figures/ --exclude='*.aux' --exclude='*.log'\n```\n\n### 6.5 常见失败点\n\n| 问题 | 解决 |\n|------|------|\n| 图片格式混用导致编译失败 | 统一用 PDF |\n| 字体未嵌入 | `pdffonts output.pdf` 检查 |\n| Overfull box 过多 | 关键位置手动调行 |\n| 引用缺字段 | 检查 DOI/年份/期刊名 |\n| 超页数 | 用 `\\vspace{-Xpt}` 微调，或精简内容 |\n\n---\n\n## 7. 会议转投\n\n当论文被拒或转投其他会议时：\n\n### 7.1 ML/AI 会议间转换\n\n| 转换 | 页数变化 | 关键调整 |\n|------|---------|---------|\n| NeurIPS → ICML | 9→8 | 删 1 页，加 Broader Impact |\n| ICML → ICLR | 8→9 | 可扩展实验 + LLM 声明 |\n| NeurIPS → ACL | 9→8 | 按 NLP 惯例重组 + Limitations |\n| ICLR → AAAI | 9→7 | 大幅精简，严格样式 |\n\n### 7.2 转投原则\n\n1. **永远用目标模板重新开始** — 复制目标模板，迁移内容，不要合并 preamble\n2. **只迁移正文内容** — 不复制 `\\usepackage`、header/footer 命令\n3. **根据审稿意见改进** — 但不要在新稿中提及旧投稿（双盲）\n4. **检查目标会议特殊要求** — checklist、ethics statement、LLM 声明等\n\n---\n\n## 8. 投前清单\n\n### 通用清单\n\n- [ ] Abstract/Intro/Conclusion 的 claim 一致\n- [ ] 每个 contribution 有对应 evidence\n- [ ] 所有引用已程序化验证（无幻觉引用）\n- [ ] Error bars + 运行次数 + 统计方法\n- [ ] Limitations 章节存在且诚实\n- [ ] 匿名化（双盲审稿）\n- [ ] 符合页数限制\n- [ ] 所有图表有自包含 caption\n- [ ] `.bib` 中无缺失字段\n- [ ] PDF 编译无 warning\n\n### 会议特定\n\n| 会议 | 额外要求 |\n|------|---------|\n| NeurIPS | 16 项 Paper Checklist（附录，不计页数） |\n| ICML | Broader Impact Statement |\n| ICLR | LLM 使用声明 |\n| ACL/EMNLP | Limitations 章节（必须），Ethics Statement |\n| AAAI | 严格样式文件合规 |\n\n---\n\n## 参考资源\n\n**写作方法论：**\n- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/) — What/Why/So What 框架\n- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 五句法 Abstract\n- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 读者预期 7 原则\n- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — 用词\n- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — 微观清晰度\n\n**API：**\n- [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | [CrossRef](https://www.crossref.org/documentation/) | [arXiv](https://info.arxiv.org/help/api/)\n\n**会议官方：**\n- [NeurIPS](https://neurips.cc/) | [ICML](https://icml.cc/) | [ICLR](https://iclr.cc/) | [ACL](https://www.aclweb.org/) | [AAAI](https://aaai.org/) | [EMNLP](https://2025.emnlp.org/)\n",
      "numLines": 353,
      "startLine": 1,
      "totalLines": 353
    }
  },
  "sourceToolAssistantUUID": "dd14ae0d-99b2-4cb1-bbd6-ebf635716c39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 11 · 2026-05-15T21:52:42.190Z_

<details><summary>↩ Tool result · `toolu_01F2ES21K4Hwn4vNz6rdqwQW`</summary>

```text
1	% Method section — collapse_severity_monitor
2	% Sources: MVP (mvp_frac50_100, within_gen_analysis, per_layer_analysis_v5)
3	% Pending: plan_001 (1.5B scale, 6 fractions, 5 seeds)
4	
5	\section{Methodology}
6	\label{sec:method}
7	
8	We design a controlled experimental framework to evaluate how training dynamic signals track model collapse severity under iterative synthetic data contamination.
9	Our protocol varies contamination level and generational depth while monitoring four families of training-time signals.
10	
11	\subsection{Iterative Synthetic Data Protocol}
12	\label{sec:protocol}
13	
14	We simulate iterative model collapse through a multi-generation fine-tuning loop.
15	Let $M_0$ denote a pretrained base model and $\mathcal{D}_\text{real}$ a real-text corpus.
16	At each generation $g \in \{0, 1, \ldots, G{-}1\}$ (with $G=5$), we execute the following steps:
17	
18	\begin{enumerate}
19	    \item \textbf{Fine-tune.} Initialize from $M_0$ with a QLoRA adapter and fine-tune on the current training corpus $\mathcal{D}_g$, yielding adapted model $\tilde{M}_g$.
20	    During training, we collect monitoring signals every 50 optimizer steps via a callback (Section~\ref{sec:signals}).
21	    \item \textbf{Generate.} Sample synthetic text $\mathcal{S}_g$ from $\tilde{M}_g$ by prompting with the first 32 tokens of randomly subsampled chunks from $\mathcal{D}_\text{real}$ and generating up to 480 new tokens with nucleus sampling ($p=0.95$, temperature $\tau=1.0$).
22	    We subsample 1{,}500 of $|\mathcal{D}_\text{real}|$ chunks for generation to keep wall-clock time tractable.
23	    \item \textbf{Mix.} Construct the next-generation corpus $\mathcal{D}_{g+1}$ by replacing a fraction $\alpha \in \{0, 0.1, 0.25, 0.5, 0.75, 1.0\}$ of real chunks with synthetic chunks from $\mathcal{S}_g$:
24	    \begin{equation}
25	        \mathcal{D}_{g+1} = (1 - \alpha)\,\mathcal{D}_\text{real} \cup \alpha\,\mathcal{S}_g.
26	        \label{eq:mixing}
27	    \end{equation}
28	    The $\alpha=0$ condition serves as a no-contamination baseline.
29	\end{enumerate}
30	
31	\noindent
32	Each generation thus starts from the \emph{same} pretrained weights $M_0$, isolating the effect of data contamination from cumulative weight drift.
33	The collapse pressure enters solely through the training corpus: at generation $g$, the synthetic component was produced by a model trained on data that itself contained synthetic text from generation $g{-}1$.
34	
35	\paragraph{Models.}
36	We use Qwen2.5-0.5B as our primary model (24 transformer layers, 494M parameters).%
37	\footnote{Scale validation on Qwen2.5-1.5B (28 layers, 1.5B parameters) is in progress; preliminary results will be included in the final version.}
38	All experiments use QLoRA~\citep{dettmers2023qlora} with rank $r=16$, scaling factor $\alpha_\text{LoRA}=32$, and dropout $0.05$.
39	Adapters are applied to all linear projections in each transformer layer: \texttt{q\_proj}, \texttt{k\_proj}, \texttt{v\_proj}, \texttt{o\_proj}, \texttt{up\_proj}, \texttt{down\_proj}, and \texttt{gate\_proj}.
40	The base model is quantized to 4-bit NormalFloat (NF4) with double quantization.
41	
42	\paragraph{Data.}
43	We use WikiText-2 (\texttt{wikitext-2-raw-v1})~\citep{merity2017pointer}, tokenized and chunked into fixed-length sequences of 512 tokens, yielding 4{,}916 training chunks and a held-out validation set.%
44	\footnote{Cross-domain validation on PubMed abstracts is planned as a secondary axis.}
45	
46	\paragraph{Training configuration.}
47	All fine-tuning runs use the AdamW optimizer with learning rate $2 \times 10^{-4}$, weight decay $0.01$, linear warmup over $5\%$ of steps, and gradient clipping at $\|\cdot\|_2 \leq 1.0$.
48	We train for 5 epochs with per-device batch size 4 and gradient accumulation over 4 steps (effective batch size 16), using \texttt{bf16} mixed precision.
49	Each generation comprises approximately 1{,}540 optimizer steps.
50	
51	\paragraph{Contamination fractions.}
52	Our MVP experiments use three fractions ($\alpha \in \{0, 0.5, 1.0\}$) with a single seed.
53	The full experimental design extends to six fractions ($\alpha \in \{0, 0.1, 0.25, 0.5, 0.75, 1.0\}$) with 5 independent seeds per configuration, yielding 150 fine-tuning runs (6~fractions $\times$ 5~generations $\times$ 5~seeds).%
54	\footnote{MVP results (3 fractions, seed 42) are reported here; full 6-fraction $\times$ 5-seed results pending \texttt{plan\_001}.}
55	
56	\subsection{Signal Families}
57	\label{sec:signals}
58	
59	We monitor four families of training-time signals, collected every 50 optimizer steps via a training callback.
60	All signals are computed on a held-out validation set in evaluation mode.
61	
62	\subsubsection{Spectral Signals}
63	\label{sec:spectral}
64	
65	Spectral signals characterize the geometry of the model's internal representations.
66	Given a set of $n$ validation sequences, we collect the last-layer hidden states into a matrix $\mathbf{H} \in \mathbb{R}^{T \times d}$, where $T$ is the total number of tokens across $n$ sequences and $d$ is the hidden dimension.
67	We center $\mathbf{H}$ by subtracting its column mean, then compute the sample covariance:
68	\begin{equation}
69	    \mathbf{C} = \frac{1}{T-1}\,\mathbf{H}^\top \mathbf{H} \in \mathbb{R}^{d \times d}.
70	\end{equation}
71	Let $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_d \geq 0$ denote the eigenvalues of $\mathbf{C}$ (equivalently, its singular values, since $\mathbf{C}$ is positive semidefinite).
72	
73	\paragraph{Stable rank.}
74	The participation ratio of the eigenspectrum measures the effective dimensionality of the representation:
75	\begin{equation}
76	    \mathrm{SR}(\mathbf{C}) = \frac{\left(\sum_{i=1}^{d} \lambda_i\right)^2}{\sum_{i=1}^{d} \lambda_i^2}.
77	    \label{eq:stable_rank}
78	\end{equation}
79	$\mathrm{SR} = 1$ when all variance concentrates on a single component; $\mathrm{SR} = d$ when variance is uniformly distributed.
80	Under model collapse, we observe that $\mathrm{SR}$ \emph{increases}: the Frobenius norm of the representation grows faster than its leading eigenvalue, dispersing energy across more dimensions rather than concentrating it.%
81	\footnote{This is the participation ratio of the covariance eigenspectrum, closely related to but distinct from the matrix stable rank $\|\mathbf{H}\|_F^2 / \|\mathbf{H}\|_2^2$; the two are monotonically related for centered data.}
82	
83	\paragraph{Spectral entropy.}
84	The normalized entropy of the eigenspectrum provides a complementary measure of spectral concentration:
85	\begin{equation}
86	    \mathrm{SE}(\mathbf{C}) = \frac{-\sum_{i=1}^{d} p_i \log p_i}{\log d}, \quad \text{where } p_i = \frac{\lambda_i}{\sum_{j=1}^{d} \lambda_j}.
87	    \label{eq:spectral_entropy}
88	\end{equation}
89	$\mathrm{SE} \in [0, 1]$, with $\mathrm{SE} = 1$ indicating a uniform spectrum and $\mathrm{SE} \to 0$ indicating concentration on few components.
90	We use $n=64$ validation chunks for SVD computation, retaining the top-5 singular values for trajectory logging.
91	
92	\subsubsection{Output Signals}
93	\label{sec:output}
94	
95	Output signals measure the model's predictive behavior on held-out real text.
96	
97	\paragraph{Token entropy.}
98	For each validation sequence $\mathbf{x} = (x_1, \ldots, x_L)$, we compute the mean per-position entropy of the next-token distribution:
99	\begin{equation}
100	    \mathrm{TE}(\mathbf{x}) = \frac{1}{L-1} \sum_{t=1}^{L-1} H\!\left(P_\theta(\cdot \mid x_{\leq t})\right), \quad H(P) = -\sum_{v} P(v) \log P(v),
101	    \label{eq:token_entropy}
102	\end{equation}
103	and report the average over 100 validation chunks.
104	Decreasing token entropy indicates the model is becoming more ``peaked'' in its predictions---a hallmark of mode collapse in generation.
105	
106	\paragraph{Perplexity.}
107	We compute perplexity as the exponentiated mean per-token negative log-likelihood over the full validation set:
108	\begin{equation}
109	    \mathrm{PPL} = \exp\!\left(\frac{1}{N}\sum_{i=1}^{|\mathcal{V}|} \ell(\mathbf{x}_i)\right),
110	    \label{eq:perplexity}
111	\end{equation}
112	where $\ell(\mathbf{x}_i)$ is the cross-entropy loss on validation sequence $\mathbf{x}_i$ and $N$ is the total token count.
113	Perplexity captures degradation in language modeling quality; under severe collapse, it increases by orders of magnitude (e.g., $15.7 \to 839.2$ over 5 generations at $\alpha=1.0$ in our MVP; source: \texttt{mvp\_frac50\_100}).
114	
115	\subsubsection{Gradient Signal}
116	\label{sec:gradient}
117	
118	We log the L2 gradient norm $\|\nabla_\theta \mathcal{L}\|_2$ computed by the trainer before each optimizer step.
119	Gradient norm is a zero-cost byproduct of standard training and reflects optimization landscape curvature.
120	In our MVP experiments, gradient norm exhibits non-monotonic behavior with respect to contamination fraction under QLoRA, limiting its utility as a standalone severity monitor (Section~\ref{sec:results}).
121	We attribute this non-monotonicity to two interacting factors specific to QLoRA training.
122	First, gradients flow only through the low-rank adapter matrices $A \in \mathbb{R}^{d \times r}$ and $B \in \mathbb{R}^{r \times d}$ rather than the full weight matrix~\citep{hu2022lora}, so the gradient landscape is confined to a rank-$r$ subspace that can amplify or attenuate contamination-induced shifts in ways that do not mirror full-rank fine-tuning.
123	Second, the NF4 quantization of frozen base weights introduces discretization noise that propagates through the backward pass~\citep{dettmers2023qlora}, adding a stochastic component to the gradient norm that obscures the monotonic contamination signal visible in spectral and output metrics.
124	
125	\subsubsection{Downstream Signal}
126	\label{sec:downstream}
127	
128	We evaluate HellaSwag~\citep{zellers2019hellaswag} accuracy (4-choice commonsense reasoning, 1{,}000 samples) as a downstream task probe.
129	HellaSwag is computed at the end of each generation (not at every signal checkpoint, due to evaluation cost).
130	At the 0.5B scale, HellaSwag shows minimal sensitivity to collapse: accuracy drops only 1.2\% (0.435 $\to$ 0.430) despite catastrophic perplexity explosion, suggesting that small-model benchmark performance is a poor proxy for generative collapse severity (source: \texttt{mvp\_frac50\_100}).
131	
132	\subsection{Evaluation Methodology}
133	\label{sec:evaluation}
134	
135	\subsubsection{Cross-Fraction Severity Correlation}
136	\label{sec:cross_fraction}
137	
138	For each signal $s$ and generation $g$, we compute the Spearman rank correlation $\rho_g^{(s)}$ between contamination fraction $\alpha$ and the end-of-generation signal value across all tested fractions.
139	We report the mean absolute correlation $\bar{|\rho|}^{(s)} = \frac{1}{G}\sum_{g=0}^{G-1} |\rho_g^{(s)}|$ as a summary statistic.
140	A signal is considered a reliable severity monitor if $\bar{|\rho|}^{(s)} > 0.7$.
141	
142	In the MVP (3 fractions, $n=1$ seed), spectral and output signals exhibit large effect sizes: 6.6$\times$ stable rank separation and 53$\times$ perplexity divergence between $\alpha=0$ and $\alpha=1.0$ at generation~4 ($|\rho|=1.0$; trivially achievable with $n=3$ severity levels).
143	The 6-fraction design (pending \texttt{plan\_001}) provides a more stringent monotonicity test; we treat effect sizes as primary evidence throughout (source: \texttt{mvp\_frac50\_100}).
144	
145	\subsubsection{Cross-Generation Tracking}
146	\label{sec:cross_gen}
147	
148	For each signal $s$ and contamination fraction $\alpha$, we compute the Spearman correlation between generation index $g$ and end-of-generation signal value.
149	This measures whether signals track the \emph{accumulation} of collapse across iterative retraining.
150	At $\alpha=1.0$, perplexity exhibits super-linear growth across generations ($15.7 \to 136.9 \to 394.3 \to 691.4 \to 839.2$), consistent with the accelerating degradation predicted by model collapse theory~\citep{Shumailov2024} (source: \texttt{mvp\_frac50\_100}).
151	
152	\subsubsection{Within-Generation Early Warning}
153	\label{sec:early_warning}
154	
155	We assess how early within a single training run each signal can distinguish a contaminated condition from the clean baseline.
156	Specifically, we compute the relative deviation at each signal checkpoint:
157	\begin{equation}
158	    \Delta_s(t, \alpha) = \frac{|s_\alpha(t) - s_0(t)|}{|s_0(t)|} \times 100\%,
159	    \label{eq:deviation}
160	\end{equation}
161	where $s_\alpha(t)$ and $s_0(t)$ are the signal values at step $t$ for fraction $\alpha$ and the clean baseline ($\alpha=0$), respectively.
162	A signal provides \emph{early warning} if $\Delta_s(t, \alpha) > 5\%$ within the first 10\% of training steps.
163	
164	In the MVP, stable rank achieves the largest early deviation: $\Delta_\mathrm{SR}(50, 1.0) = 34.4\%$ at step 50 (${\sim}3\%$ training progress), followed by token entropy at 24.5\% and perplexity at 17.7\%.
165	Spectral entropy (5.0\%) and gradient norm (2.1\%) respond more slowly, first exceeding 5\% at step 100 (${\sim}6\%$ progress) (source: \texttt{within\_gen\_analysis}).
166	
167	\subsubsection{Statistical Validity}
168	\label{sec:stats}
169	
170	\paragraph{Bootstrap confidence intervals.}
171	For the full experimental design (6 fractions $\times$ 5 seeds), we compute 95\% bootstrap confidence intervals for all reported correlations and effect sizes.
172	Crucially, we use \emph{clustered bootstrap} with the cluster unit being fraction $\times$ seed, rather than pooling individual generation observations.
173	Pooling would inflate sample size and produce artificially narrow intervals, because successive generations within a run are causally dependent---generation $g+1$ trains on data produced by the model from generation $g$.
174	
175	\paragraph{AUROC for collapse detection.}
176	We compute the area under the receiver operating characteristic curve (AUROC) for binary collapse detection at various severity thresholds (e.g., $\alpha \geq 0.5$ vs.\ $\alpha < 0.5$).
177	In the MVP (3 fractions, single seed), stable rank, spectral entropy, and token entropy each achieve AUROC $= 1.0$ for distinguishing the $\alpha = 1.0$ condition at step 50.
178	We treat AUROC as a secondary metric supporting the primary evidence from effect sizes and rank correlations, given the small sample size in the MVP (source: \texttt{within\_gen\_analysis}).
179	
180	\paragraph{Effect sizes.}
181	We prioritize absolute and relative effect sizes (e.g., 6.6$\times$ stable rank separation between $\alpha=0$ and $\alpha=1.0$ at generation 4) as primary evidence, with rank correlations as supporting statistics.
182	This hierarchy follows from the observation that $|\rho| = 1.0$ is easily achieved with few fractions and does not convey the \emph{magnitude} of signal separation (source: \texttt{mvp\_frac50\_100}).
183	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e716fb3d-1653-4026-acaf-66ca886bcc93",
  "isSidechain": false,
  "promptId": "ae09a607-e5a2-46f5-8d19-601dcf6d2541",
  "type": "user",
  "uuid": "0a15db82-1a5c-403d-bdb9-4a20582e9c93",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex",
      "content": "% Method section — collapse_severity_monitor\n% Sources: MVP (mvp_frac50_100, within_gen_analysis, per_layer_analysis_v5)\n% Pending: plan_001 (1.5B scale, 6 fractions, 5 seeds)\n\n\\section{Methodology}\n\\label{sec:method}\n\nWe design a controlled experimental framework to evaluate how training dynamic signals track model collapse severity under iterative synthetic data contamination.\nOur protocol varies contamination level and generational depth while monitoring four families of training-time signals.\n\n\\subsection{Iterative Synthetic Data Protocol}\n\\label{sec:protocol}\n\nWe simulate iterative model collapse through a multi-generation fine-tuning loop.\nLet $M_0$ denote a pretrained base model and $\\mathcal{D}_\\text{real}$ a real-text corpus.\nAt each generation $g \\in \\{0, 1, \\ldots, G{-}1\\}$ (with $G=5$), we execute the following steps:\n\n\\begin{enumerate}\n    \\item \\textbf{Fine-tune.} Initialize from $M_0$ with a QLoRA adapter and fine-tune on the current training corpus $\\mathcal{D}_g$, yielding adapted model $\\tilde{M}_g$.\n    During training, we collect monitoring signals every 50 optimizer steps via a callback (Section~\\ref{sec:signals}).\n    \\item \\textbf{Generate.} Sample synthetic text $\\mathcal{S}_g$ from $\\tilde{M}_g$ by prompting with the first 32 tokens of randomly subsampled chunks from $\\mathcal{D}_\\text{real}$ and generating up to 480 new tokens with nucleus sampling ($p=0.95$, temperature $\\tau=1.0$).\n    We subsample 1{,}500 of $|\\mathcal{D}_\\text{real}|$ chunks for generation to keep wall-clock time tractable.\n    \\item \\textbf{Mix.} Construct the next-generation corpus $\\mathcal{D}_{g+1}$ by replacing a fraction $\\alpha \\in \\{0, 0.1, 0.25, 0.5, 0.75, 1.0\\}$ of real chunks with synthetic chunks from $\\mathcal{S}_g$:\n    \\begin{equation}\n        \\mathcal{D}_{g+1} = (1 - \\alpha)\\,\\mathcal{D}_\\text{real} \\cup \\alpha\\,\\mathcal{S}_g.\n        \\label{eq:mixing}\n    \\end{equation}\n    The $\\alpha=0$ condition serves as a no-contamination baseline.\n\\end{enumerate}\n\n\\noindent\nEach generation thus starts from the \\emph{same} pretrained weights $M_0$, isolating the effect of data contamination from cumulative weight drift.\nThe collapse pressure enters solely through the training corpus: at generation $g$, the synthetic component was produced by a model trained on data that itself contained synthetic text from generation $g{-}1$.\n\n\\paragraph{Models.}\nWe use Qwen2.5-0.5B as our primary model (24 transformer layers, 494M parameters).%\n\\footnote{Scale validation on Qwen2.5-1.5B (28 layers, 1.5B parameters) is in progress; preliminary results will be included in the final version.}\nAll experiments use QLoRA~\\citep{dettmers2023qlora} with rank $r=16$, scaling factor $\\alpha_\\text{LoRA}=32$, and dropout $0.05$.\nAdapters are applied to all linear projections in each transformer layer: \\texttt{q\\_proj}, \\texttt{k\\_proj}, \\texttt{v\\_proj}, \\texttt{o\\_proj}, \\texttt{up\\_proj}, \\texttt{down\\_proj}, and \\texttt{gate\\_proj}.\nThe base model is quantized to 4-bit NormalFloat (NF4) with double quantization.\n\n\\paragraph{Data.}\nWe use WikiText-2 (\\texttt{wikitext-2-raw-v1})~\\citep{merity2017pointer}, tokenized and chunked into fixed-length sequences of 512 tokens, yielding 4{,}916 training chunks and a held-out validation set.%\n\\footnote{Cross-domain validation on PubMed abstracts is planned as a secondary axis.}\n\n\\paragraph{Training configuration.}\nAll fine-tuning runs use the AdamW optimizer with learning rate $2 \\times 10^{-4}$, weight decay $0.01$, linear warmup over $5\\%$ of steps, and gradient clipping at $\\|\\cdot\\|_2 \\leq 1.0$.\nWe train for 5 epochs with per-device batch size 4 and gradient accumulation over 4 steps (effective batch size 16), using \\texttt{bf16} mixed precision.\nEach generation comprises approximately 1{,}540 optimizer steps.\n\n\\paragraph{Contamination fractions.}\nOur MVP experiments use three fractions ($\\alpha \\in \\{0, 0.5, 1.0\\}$) with a single seed.\nThe full experimental design extends to six fractions ($\\alpha \\in \\{0, 0.1, 0.25, 0.5, 0.75, 1.0\\}$) with 5 independent seeds per configuration, yielding 150 fine-tuning runs (6~fractions $\\times$ 5~generations $\\times$ 5~seeds).%\n\\footnote{MVP results (3 fractions, seed 42) are reported here; full 6-fraction $\\times$ 5-seed results pending \\texttt{plan\\_001}.}\n\n\\subsection{Signal Families}\n\\label{sec:signals}\n\nWe monitor four families of training-time signals, collected every 50 optimizer steps via a training callback.\nAll signals are computed on a held-out validation set in evaluation mode.\n\n\\subsubsection{Spectral Signals}\n\\label{sec:spectral}\n\nSpectral signals characterize the geometry of the model's internal representations.\nGiven a set of $n$ validation sequences, we collect the last-layer hidden states into a matrix $\\mathbf{H} \\in \\mathbb{R}^{T \\times d}$, where $T$ is the total number of tokens across $n$ sequences and $d$ is the hidden dimension.\nWe center $\\mathbf{H}$ by subtracting its column mean, then compute the sample covariance:\n\\begin{equation}\n    \\mathbf{C} = \\frac{1}{T-1}\\,\\mathbf{H}^\\top \\mathbf{H} \\in \\mathbb{R}^{d \\times d}.\n\\end{equation}\nLet $\\lambda_1 \\geq \\lambda_2 \\geq \\cdots \\geq \\lambda_d \\geq 0$ denote the eigenvalues of $\\mathbf{C}$ (equivalently, its singular values, since $\\mathbf{C}$ is positive semidefinite).\n\n\\paragraph{Stable rank.}\nThe participation ratio of the eigenspectrum measures the effective dimensionality of the representation:\n\\begin{equation}\n    \\mathrm{SR}(\\mathbf{C}) = \\frac{\\left(\\sum_{i=1}^{d} \\lambda_i\\right)^2}{\\sum_{i=1}^{d} \\lambda_i^2}.\n    \\label{eq:stable_rank}\n\\end{equation}\n$\\mathrm{SR} = 1$ when all variance concentrates on a single component; $\\mathrm{SR} = d$ when variance is uniformly distributed.\nUnder model collapse, we observe that $\\mathrm{SR}$ \\emph{increases}: the Frobenius norm of the representation grows faster than its leading eigenvalue, dispersing energy across more dimensions rather than concentrating it.%\n\\footnote{This is the participation ratio of the covariance eigenspectrum, closely related to but distinct from the matrix stable rank $\\|\\mathbf{H}\\|_F^2 / \\|\\mathbf{H}\\|_2^2$; the two are monotonically related for centered data.}\n\n\\paragraph{Spectral entropy.}\nThe normalized entropy of the eigenspectrum provides a complementary measure of spectral concentration:\n\\begin{equation}\n    \\mathrm{SE}(\\mathbf{C}) = \\frac{-\\sum_{i=1}^{d} p_i \\log p_i}{\\log d}, \\quad \\text{where } p_i = \\frac{\\lambda_i}{\\sum_{j=1}^{d} \\lambda_j}.\n    \\label{eq:spectral_entropy}\n\\end{equation}\n$\\mathrm{SE} \\in [0, 1]$, with $\\mathrm{SE} = 1$ indicating a uniform spectrum and $\\mathrm{SE} \\to 0$ indicating concentration on few components.\nWe use $n=64$ validation chunks for SVD computation, retaining the top-5 singular values for trajectory logging.\n\n\\subsubsection{Output Signals}\n\\label{sec:output}\n\nOutput signals measure the model's predictive behavior on held-out real text.\n\n\\paragraph{Token entropy.}\nFor each validation sequence $\\mathbf{x} = (x_1, \\ldots, x_L)$, we compute the mean per-position entropy of the next-token distribution:\n\\begin{equation}\n    \\mathrm{TE}(\\mathbf{x}) = \\frac{1}{L-1} \\sum_{t=1}^{L-1} H\\!\\left(P_\\theta(\\cdot \\mid x_{\\leq t})\\right), \\quad H(P) = -\\sum_{v} P(v) \\log P(v),\n    \\label{eq:token_entropy}\n\\end{equation}\nand report the average over 100 validation chunks.\nDecreasing token entropy indicates the model is becoming more ``peaked'' in its predictions---a hallmark of mode collapse in generation.\n\n\\paragraph{Perplexity.}\nWe compute perplexity as the exponentiated mean per-token negative log-likelihood over the full validation set:\n\\begin{equation}\n    \\mathrm{PPL} = \\exp\\!\\left(\\frac{1}{N}\\sum_{i=1}^{|\\mathcal{V}|} \\ell(\\mathbf{x}_i)\\right),\n    \\label{eq:perplexity}\n\\end{equation}\nwhere $\\ell(\\mathbf{x}_i)$ is the cross-entropy loss on validation sequence $\\mathbf{x}_i$ and $N$ is the total token count.\nPerplexity captures degradation in language modeling quality; under severe collapse, it increases by orders of magnitude (e.g., $15.7 \\to 839.2$ over 5 generations at $\\alpha=1.0$ in our MVP; source: \\texttt{mvp\\_frac50\\_100}).\n\n\\subsubsection{Gradient Signal}\n\\label{sec:gradient}\n\nWe log the L2 gradient norm $\\|\\nabla_\\theta \\mathcal{L}\\|_2$ computed by the trainer before each optimizer step.\nGradient norm is a zero-cost byproduct of standard training and reflects optimization landscape curvature.\nIn our MVP experiments, gradient norm exhibits non-monotonic behavior with respect to contamination fraction under QLoRA, limiting its utility as a standalone severity monitor (Section~\\ref{sec:results}).\nWe attribute this non-monotonicity to two interacting factors specific to QLoRA training.\nFirst, gradients flow only through the low-rank adapter matrices $A \\in \\mathbb{R}^{d \\times r}$ and $B \\in \\mathbb{R}^{r \\times d}$ rather than the full weight matrix~\\citep{hu2022lora}, so the gradient landscape is confined to a rank-$r$ subspace that can amplify or attenuate contamination-induced shifts in ways that do not mirror full-rank fine-tuning.\nSecond, the NF4 quantization of frozen base weights introduces discretization noise that propagates through the backward pass~\\citep{dettmers2023qlora}, adding a stochastic component to the gradient norm that obscures the monotonic contamination signal visible in spectral and output metrics.\n\n\\subsubsection{Downstream Signal}\n\\label{sec:downstream}\n\nWe evaluate HellaSwag~\\citep{zellers2019hellaswag} accuracy (4-choice commonsense reasoning, 1{,}000 samples) as a downstream task probe.\nHellaSwag is computed at the end of each generation (not at every signal checkpoint, due to evaluation cost).\nAt the 0.5B scale, HellaSwag shows minimal sensitivity to collapse: accuracy drops only 1.2\\% (0.435 $\\to$ 0.430) despite catastrophic perplexity explosion, suggesting that small-model benchmark performance is a poor proxy for generative collapse severity (source: \\texttt{mvp\\_frac50\\_100}).\n\n\\subsection{Evaluation Methodology}\n\\label{sec:evaluation}\n\n\\subsubsection{Cross-Fraction Severity Correlation}\n\\label{sec:cross_fraction}\n\nFor each signal $s$ and generation $g$, we compute the Spearman rank correlation $\\rho_g^{(s)}$ between contamination fraction $\\alpha$ and the end-of-generation signal value across all tested fractions.\nWe report the mean absolute correlation $\\bar{|\\rho|}^{(s)} = \\frac{1}{G}\\sum_{g=0}^{G-1} |\\rho_g^{(s)}|$ as a summary statistic.\nA signal is considered a reliable severity monitor if $\\bar{|\\rho|}^{(s)} > 0.7$.\n\nIn the MVP (3 fractions, $n=1$ seed), spectral and output signals exhibit large effect sizes: 6.6$\\times$ stable rank separation and 53$\\times$ perplexity divergence between $\\alpha=0$ and $\\alpha=1.0$ at generation~4 ($|\\rho|=1.0$; trivially achievable with $n=3$ severity levels).\nThe 6-fraction design (pending \\texttt{plan\\_001}) provides a more stringent monotonicity test; we treat effect sizes as primary evidence throughout (source: \\texttt{mvp\\_frac50\\_100}).\n\n\\subsubsection{Cross-Generation Tracking}\n\\label{sec:cross_gen}\n\nFor each signal $s$ and contamination fraction $\\alpha$, we compute the Spearman correlation between generation index $g$ and end-of-generation signal value.\nThis measures whether signals track the \\emph{accumulation} of collapse across iterative retraining.\nAt $\\alpha=1.0$, perplexity exhibits super-linear growth across generations ($15.7 \\to 136.9 \\to 394.3 \\to 691.4 \\to 839.2$), consistent with the accelerating degradation predicted by model collapse theory~\\citep{Shumailov2024} (source: \\texttt{mvp\\_frac50\\_100}).\n\n\\subsubsection{Within-Generation Early Warning}\n\\label{sec:early_warning}\n\nWe assess how early within a single training run each signal can distinguish a contaminated condition from the clean baseline.\nSpecifically, we compute the relative deviation at each signal checkpoint:\n\\begin{equation}\n    \\Delta_s(t, \\alpha) = \\frac{|s_\\alpha(t) - s_0(t)|}{|s_0(t)|} \\times 100\\%,\n    \\label{eq:deviation}\n\\end{equation}\nwhere $s_\\alpha(t)$ and $s_0(t)$ are the signal values at step $t$ for fraction $\\alpha$ and the clean baseline ($\\alpha=0$), respectively.\nA signal provides \\emph{early warning} if $\\Delta_s(t, \\alpha) > 5\\%$ within the first 10\\% of training steps.\n\nIn the MVP, stable rank achieves the largest early deviation: $\\Delta_\\mathrm{SR}(50, 1.0) = 34.4\\%$ at step 50 (${\\sim}3\\%$ training progress), followed by token entropy at 24.5\\% and perplexity at 17.7\\%.\nSpectral entropy (5.0\\%) and gradient norm (2.1\\%) respond more slowly, first exceeding 5\\% at step 100 (${\\sim}6\\%$ progress) (source: \\texttt{within\\_gen\\_analysis}).\n\n\\subsubsection{Statistical Validity}\n\\label{sec:stats}\n\n\\paragraph{Bootstrap confidence intervals.}\nFor the full experimental design (6 fractions $\\times$ 5 seeds), we compute 95\\% bootstrap confidence intervals for all reported correlations and effect sizes.\nCrucially, we use \\emph{clustered bootstrap} with the cluster unit being fraction $\\times$ seed, rather than pooling individual generation observations.\nPooling would inflate sample size and produce artificially narrow intervals, because successive generations within a run are causally dependent---generation $g+1$ trains on data produced by the model from generation $g$.\n\n\\paragraph{AUROC for collapse detection.}\nWe compute the area under the receiver operating characteristic curve (AUROC) for binary collapse detection at various severity thresholds (e.g., $\\alpha \\geq 0.5$ vs.\\ $\\alpha < 0.5$).\nIn the MVP (3 fractions, single seed), stable rank, spectral entropy, and token entropy each achieve AUROC $= 1.0$ for distinguishing the $\\alpha = 1.0$ condition at step 50.\nWe treat AUROC as a secondary metric supporting the primary evidence from effect sizes and rank correlations, given the small sample size in the MVP (source: \\texttt{within\\_gen\\_analysis}).\n\n\\paragraph{Effect sizes.}\nWe prioritize absolute and relative effect sizes (e.g., 6.6$\\times$ stable rank separation between $\\alpha=0$ and $\\alpha=1.0$ at generation 4) as primary evidence, with rank correlations as supporting statistics.\nThis hierarchy follows from the observation that $|\\rho| = 1.0$ is easily achieved with few fractions and does not convey the \\emph{magnitude} of signal separation (source: \\texttt{mvp\\_frac50\\_100}).\n",
      "numLines": 183,
      "startLine": 1,
      "totalLines": 183
    }
  },
  "sourceToolAssistantUUID": "e716fb3d-1653-4026-acaf-66ca886bcc93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T21:52:42.183Z_

<details open><summary>🔧 Tool call — Read · `toolu_01F2ES21K4Hwn4vNz6rdqwQW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26f5bfae-b8a8-43bd-8d17-d3bacbc4645e",
  "isSidechain": false,
  "requestId": "req_011Cb56YTMxsuGv6cki3QNAE",
  "type": "assistant",
  "uuid": "e716fb3d-1653-4026-acaf-66ca886bcc93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AkDkbdqaTqdLLzF4MRcERT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12860,
      "cache_read_input_tokens": 11841,
      "output_tokens": 162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 162,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12860
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
  "leafUuid": "0a15db82-1a5c-403d-bdb9-4a20582e9c93",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Rewrite Method section for collapse severity monitor paper",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262"
}
```

---

### Assistant

_source line 15 · 2026-05-15T21:54:23.880Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have both the style guide and the existing method section. Let me also check the main.tex to understand what packages are available and what labels are used elsewhere.

Let me now write the rewritten method.tex. Let me carefully follow the spec:

Key changes from the existing version:
1. Remove all "pending" / "in progress" / "planned" footnotes — write definitively
2. Add §3.4 with Table 4 (configuration summary)
3. Update §3.2 to be its own subsection about contamination fractions
4. Update §3.3 signals section — clarify stable_rank direction, distinguish training vs eval PPL


5. Update §3.5 evaluation framework — cleaner structure with cross-gen severity, within-gen detection, method-dependence
6. Add C4 (Full FT) and C5 (3B) configurations
7. Remove specific MVP numbers from method section (those belong in results)
8. Keep all equation labels

I'll structure this as five subsections under Methodology with a ~1100 word budget: §3.1 covers the iterative training protocol, §3.2 focuses on contamination fractions, §3.3 describes the four monitoring signal families, §3.4 presents the experimental configurations in a table, and §3.5 lays out the evaluation framework with its three components.

Now I'm drafting the methodology section. For §3.1, I need to explain how we fine-tune from the same pretrained base across generations, then detail the generation process with specific hyperparameters for sampling and training — temperature, top-p, sequence length, batch configuration, optimizer settings, and QLoRA parameters all need to fit naturally into the narrative.

For §3.2 through §3.4, I'm laying out the contamination levels we're testing, the four categories of monitoring signals we'll track to detect model collapse, and then the experimental configurations table that ties everything together.

Now moving into §3.5, I need to specify how we'll actually evaluate whether these signals are useful—comparing their severity rankings across different generations, testing detection performance within a single generation, and checking if the patterns hold across different training methods. For generation, I sample 1,500 text chunks from the real corpus, use the first 32 tokens as prompts, and generate up to 480 new tokens with nucleus sampling. Then I construct the next training corpus by mixing a fraction α of synthetic samples with real data. Each generation starts fresh from the original pretrained weights to isolate the effect of data contamination without confounding weight drift.

The synthetic contamination accumulates through the training process itself—at each generation, the model trains on data containing synthetic text from the previous generation, creating a feedback loop. I'm using AdamW optimization with a learning rate of 2×10⁻⁴, weight decay, linear warmup, and gradient clipping, training for 5 epochs with batch size 16 in bfloat16 precision. For LoRA fine-tuning, I'm setting rank to 16 with a scaling factor of 32 and dropout of 0.05.

For the QLoRA approach, I'm applying adapters across all the key linear projections in the transformer while quantizing the base model to 4-bit NormalFloat format with double quantization. The full fine-tuning baseline uses the same hyperparameters but trains all parameters without quantization. I'm testing six contamination levels ranging from 0 (clean baseline) to 1.0 (fully synthetic).

Now I'm setting up the monitoring system to track four families of signals during training, sampled every 50 steps on a validation set. For the spectral analysis, I'm collecting the final layer hidden states, centering them, and computing the sample covariance matrix to examine how the model's representation structure changes across different contamination levels.

I'm using stable rank as a key metric—it captures the effective dimensionality by comparing the squared sum of eigenvalues to the sum of squared eigenvalues. Under model collapse, stable rank actually increases because the representation energy spreads across more dimensions rather than concentrating in the leading eigenvalue, which is the opposite of what we'd expect from typical dimensionality reduction.

Now I'm introducing spectral entropy as another way to measure how concentrated the spectrum is, normalizing it to a 0-1 scale where 1 represents maximum entropy across all dimensions.

I'm also defining two distinct perplexity metrics: one computed on the potentially noisy training batch to measure how well the model fits the mixed data, and another on clean held-out validation text to capture actual degradation in language modeling performance.

Beyond perplexity, I'm tracking token entropy—the average entropy of the model's next-token predictions across validation sequences—which drops as the model collapses into peaked, repetitive predictions. I'm also monitoring the L2 gradient norm...

Actually, let me reconsider. The gradient norm behavior under QLoRA is interesting: it's non-monotonic with contamination because gradients only flow through the low-rank adapters, and the quantized base weights introduce discretization noise that affects the backward pass. Finally, I'm using HellaSwag accuracy as a downstream probe to see how commonsense reasoning degrades during training.

Now I'm setting up five experimental configurations to test different aspects. C1 is a quick signal check on the smallest model, C2 is my main analysis with multiple seeds for statistical rigor, C3 tests whether findings generalize to biomedical text, C4 directly compares full fine-tuning versus QLoRA, and C5 scales up to 3B parameters to see if patterns hold. The table details each configuration with model size, dataset, contamination fractions, number of seeds, and training method. I'm looking at the experimental configurations for different model sizes and datasets, then moving into the evaluation methodology where I'm computing Spearman rank correlations between contamination levels and generation signals to measure cross-generation severity.

For within-generation detection, I'm calculating the area under the ROC curve at regular checkpoints using clustered bootstrap resampling—clustering by fraction and seed rather than individual observations since successive generations are causally dependent. I'm also defining a relative deviation metric that measures the percentage change in signal values compared to the clean baseline.

To assess whether collapse signatures are method-dependent, I'm comparing signal trajectories between QLoRA and full fine-tuning approaches under identical conditions, using paired differences in final signal values to determine if the fine-tuning method influences the detection patterns. , eq:stable_rank, eq:spectral_entropy, eq:token_entropy, eq:perplexity, eq:deviation
3. No footnotes about "pending" or "in progress": ✓ (removed all such footnotes)
4. All signals computed every 50 steps on held-out validation set: ✓
5. QLoRA params: r=16, α_LoRA=32, dropout 0.05, NF4, all linear projections: ✓
6. Full FT: same hyperparameters, all parameters trainable, no quantization: ✓
7. Training: AdamW, lr=2e-4, weight_decay=0.01, 5% warmup, grad clip 1.0, 5 epochs, effective batch 16, bf16: ✓
8. Citations: \citep{} for parenthetical, \citet{} for textual: ✓
9. Available citation keys used correctly: ✓
10. Table 4 with all 5 configurations: ✓
11. stable_rank ↑ under collapse = energy dispersal: ✓
12. Distinguish training vs eval PPL: ✓
13. gradient_norm non-monotonic under QLoRA: ✓
14. Cross-gen: Spearman ρ + bootstrap CI, Cohen's d: ✓
15. Within-gen: ROC with clustered bootstrap + explanation: ✓
16. Method-dependence: ✓
17. No \begin{document}: ✓

I'm checking the word count—around 1100 words, so I'm within budget. I should also fix the table label to use `tab:configs` instead of `tab4_config` for consistency. The spec references "tab4_config" but that's likely just a spec identifier—I'll stick with the semantic LaTeX label `tab:configs`. Looking at the table structure, I could merge the Domain column into Dataset to save space given the 8-page limit, though I should check what the existing section labels use to maintain consistency with the document's cross-referencing style. I'm considering whether to include the available citations—`Martin2021` on spectral methods and `Sanyal2020` on stable rank—but I should only add them if they genuinely fit the discussion rather than forcing references that don't belong naturally in the text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a15db82-1a5c-403d-bdb9-4a20582e9c93",
  "isSidechain": false,
  "requestId": "req_011Cb56YkuQSsnJd2ETatSBA",
  "type": "assistant",
  "uuid": "41c07852-7365-4e62-aea2-d4f5672fba7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXdbAdqNPfrYiEUJR2Zehs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10566,
      "cache_read_input_tokens": 24701,
      "output_tokens": 9125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10566,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9125,
          "cache_read_input_tokens": 24701,
          "cache_creation_input_tokens": 10566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10566
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

_source line 16 · 2026-05-15T21:54:23.882Z_

Now I'll write the rewritten method section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41c07852-7365-4e62-aea2-d4f5672fba7e",
  "isSidechain": false,
  "requestId": "req_011Cb56YkuQSsnJd2ETatSBA",
  "type": "assistant",
  "uuid": "c0f94f9a-c517-4753-bdf8-3c494b9dc1da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXdbAdqNPfrYiEUJR2Zehs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10566,
      "cache_read_input_tokens": 24701,
      "output_tokens": 9125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10566,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9125,
          "cache_read_input_tokens": 24701,
          "cache_creation_input_tokens": 10566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10566
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

_source line 17 · 2026-05-15T21:54:56.040Z_

<details open><summary>🔧 Tool call — Write · `toolu_01MEkK856Wp8jbL1VmG5b5ha`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex",
  "content": "% Method section — collapse_severity_monitor\n\n\\section{Methodology}\n\\label{sec:method}\n\nWe design a controlled framework to evaluate how training-time signals track model collapse severity under iterative synthetic data contamination.\nOur protocol varies contamination level and generational depth while monitoring four families of signals across five experimental configurations.\n\n\\subsection{Iterative Training Protocol}\n\\label{sec:protocol}\n\nWe simulate iterative model collapse through a multi-generation fine-tuning loop.\nLet $M_0$ denote a pretrained base model and $\\mathcal{D}_\\text{real}$ a corpus of real text.\nAt each generation $g \\in \\{0, 1, \\ldots, G{-}1\\}$ (with $G=5$), we execute three steps:\n\n\\begin{enumerate}\n    \\item \\textbf{Fine-tune.} Initialize from $M_0$ and fine-tune on the current training corpus $\\mathcal{D}_g$, yielding model $\\tilde{M}_g$. During training, we collect monitoring signals every 50 optimizer steps via a callback on a held-out validation set (Section~\\ref{sec:signals}).\n    \\item \\textbf{Generate.} Sample synthetic text $\\mathcal{S}_g$ from $\\tilde{M}_g$ by prompting with the first 32 tokens of randomly subsampled chunks from $\\mathcal{D}_\\text{real}$ and generating up to 480 new tokens with nucleus sampling ($p=0.95$, temperature $\\tau=1.0$). We subsample 1{,}500 chunks for generation.\n    \\item \\textbf{Mix.} Construct the next-generation corpus by replacing fraction $\\alpha$ of real chunks with synthetic chunks:\n    \\begin{equation}\n        \\mathcal{D}_{g+1} = (1 - \\alpha)\\,\\mathcal{D}_\\text{real} \\cup \\alpha\\,\\mathcal{S}_g.\n        \\label{eq:mixing}\n    \\end{equation}\n\\end{enumerate}\n\n\\noindent\nEach generation initializes from the \\emph{same} pretrained weights $M_0$, isolating the effect of data contamination from cumulative weight drift.\nCollapse pressure enters solely through the training corpus: at generation $g$, the synthetic component was produced by a model trained on data that itself contained synthetic text from generation $g{-}1$.\n\nAll fine-tuning runs use AdamW with learning rate $2 \\times 10^{-4}$, weight decay $0.01$, linear warmup over $5\\%$ of steps, and gradient clipping at $\\|\\cdot\\|_2 \\leq 1.0$.\nWe train for 5 epochs with effective batch size 16 (per-device batch 4, gradient accumulation 4) in \\texttt{bf16} mixed precision.\nQLoRA configurations~\\citep{dettmers2023qlora} use rank $r=16$, scaling factor $\\alpha_\\text{LoRA}=32$, dropout $0.05$, with adapters on all linear projections (\\texttt{q\\_proj}, \\texttt{k\\_proj}, \\texttt{v\\_proj}, \\texttt{o\\_proj}, \\texttt{up\\_proj}, \\texttt{down\\_proj}, \\texttt{gate\\_proj}); the base model is quantized to 4-bit NormalFloat (NF4) with double quantization.\nFull fine-tuning (C4; Table~\\ref{tab:configs}) uses identical hyperparameters with all parameters trainable and no quantization.\n\n\\subsection{Contamination Fractions}\n\\label{sec:fractions}\n\nWe test six contamination levels: $\\alpha \\in \\{0, 0.1, 0.25, 0.5, 0.75, 1.0\\}$.\nThe $\\alpha=0$ condition serves as a clean baseline, controlling for training noise and natural run-to-run variance in the absence of synthetic contamination.\nThe $\\alpha=1.0$ condition replaces the entire training set with synthetic data, applying maximum collapse pressure.\nIntermediate fractions trace the dose--response relationship between contamination level and signal behavior.\n\n\\subsection{Monitoring Signals}\n\\label{sec:signals}\n\nWe monitor four families of training-time signals, collected every 50 optimizer steps on a held-out validation set in evaluation mode.\n\n\\paragraph{Spectral signals.}\nGiven $n$ validation sequences, we collect last-layer hidden states into a matrix $\\mathbf{H} \\in \\mathbb{R}^{T \\times d}$ ($T$ total tokens, $d$ hidden dimension), center by subtracting the column mean, and compute the sample covariance $\\mathbf{C} = \\frac{1}{T-1}\\mathbf{H}^\\top\\mathbf{H}$ with eigenvalues $\\lambda_1 \\geq \\cdots \\geq \\lambda_d \\geq 0$.\n\n\\emph{Stable rank} measures the effective dimensionality of the representation:\n\\begin{equation}\n    \\mathrm{SR}(\\mathbf{C}) = \\frac{\\left(\\sum_{i=1}^{d} \\lambda_i\\right)^2}{\\sum_{i=1}^{d} \\lambda_i^2}.\n    \\label{eq:stable_rank}\n\\end{equation}\nUnder model collapse, $\\mathrm{SR}$ \\emph{increases}: the Frobenius norm $\\|\\mathbf{H}\\|_F^2$ grows faster than the leading eigenvalue $\\lambda_1$, dispersing energy across more dimensions rather than concentrating it.%\n\\footnote{This is the participation ratio of the covariance eigenspectrum, closely related to but distinct from the matrix stable rank $\\|\\mathbf{H}\\|_F^2 / \\|\\mathbf{H}\\|_2^2$; the two are monotonically related for centered data.}\n\n\\emph{Spectral entropy} provides a complementary measure of spectral concentration:\n\\begin{equation}\n    \\mathrm{SE}(\\mathbf{C}) = \\frac{-\\sum_{i=1}^{d} p_i \\log p_i}{\\log d}, \\quad p_i = \\frac{\\lambda_i}{\\sum_{j=1}^{d} \\lambda_j}.\n    \\label{eq:spectral_entropy}\n\\end{equation}\n$\\mathrm{SE} \\in [0,1]$, with $\\mathrm{SE}=1$ for a uniform spectrum and $\\mathrm{SE} \\to 0$ for concentration on few components.\nWe use $n=64$ validation chunks for SVD computation.\n\n\\paragraph{Output signals.}\nWe distinguish two perplexity regimes.\n\\emph{Training perplexity}, computed on the current (potentially contaminated) training batch, measures fit to the data mix; it can \\emph{decrease} even as the model collapses, since the model fits its own synthetic output well.\n\\emph{Evaluation perplexity}, computed on a held-out clean set, reliably tracks degradation in language modeling quality on real text:\n\\begin{equation}\n    \\mathrm{PPL}_\\text{eval} = \\exp\\!\\left(\\frac{1}{N}\\sum_{i=1}^{|\\mathcal{V}|} \\ell(\\mathbf{x}_i)\\right),\n    \\label{eq:perplexity}\n\\end{equation}\nwhere $\\ell(\\mathbf{x}_i)$ is the cross-entropy loss on validation sequence $\\mathbf{x}_i$ and $N$ is the total token count.\nThis distinction is critical for within-generation detection (Section~\\ref{sec:evaluation}): training perplexity is a misleading signal, while evaluation perplexity is a reliable one.\n\n\\emph{Token entropy} measures the mean per-position entropy of the next-token distribution:\n\\begin{equation}\n    \\mathrm{TE}(\\mathbf{x}) = \\frac{1}{L-1}\\sum_{t=1}^{L-1} H\\!\\left(P_\\theta(\\cdot \\mid x_{\\leq t})\\right), \\quad H(P) = -\\sum_v P(v) \\log P(v),\n    \\label{eq:token_entropy}\n\\end{equation}\naveraged over 100 validation chunks.\nDecreasing token entropy indicates the model is becoming more peaked in its predictions, a hallmark of mode collapse in generation.\n\n\\paragraph{Gradient signal.}\nWe log the L2 gradient norm $\\|\\nabla_\\theta \\mathcal{L}\\|_2$ before each optimizer step.\nGradient norm is a zero-cost byproduct of standard training.\nUnder QLoRA, gradient norm exhibits non-monotonic behavior with respect to contamination fraction: gradients flow only through low-rank adapter matrices~\\citep{hu2022lora}, confining the landscape to a rank-$r$ subspace, and NF4 quantization of frozen base weights introduces discretization noise that propagates through the backward pass~\\citep{dettmers2023qlora}.\n\n\\paragraph{Downstream signal.}\nWe evaluate HellaSwag~\\citep{zellers2019hellaswag} accuracy (4-choice commonsense reasoning, 1{,}000 samples) at the end of each generation as a downstream task probe.\n\n\\subsection{Experimental Configurations}\n\\label{sec:configs}\n\nTable~\\ref{tab:configs} summarizes our five experimental configurations.\nC1 provides initial signal discovery on the smallest model.\nC2 is the primary analysis configuration, with five independent seeds providing statistical power for bootstrap confidence intervals and effect size estimation.\nC3 tests cross-domain generalization on biomedical text.\nC4 isolates method-dependence by comparing full fine-tuning against QLoRA under matched conditions.\nC5 provides a scale spot-check at 3B parameters.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Experimental configurations. Trainable\\% indicates the fraction of parameters updated during fine-tuning.}\n\\label{tab:configs}\n\\begin{tabular}{llrllcll}\n\\toprule\nID & Model & Params & Dataset & Fractions ($\\alpha$) & Seeds & Method & Train.\\% \\\\\n\\midrule\nC1 & Qwen2.5-0.5B & 494M & WikiText-2 & \\{0, 0.5, 1.0\\} & 1 & QLoRA $r{=}16$ & 0.8 \\\\\nC2 & Qwen2.5-1.5B & 1.5B & WikiText-2 & \\{0, 0.1, \\ldots, 1.0\\} & 5 & QLoRA $r{=}16$ & 0.5 \\\\\nC3 & Qwen2.5-1.5B & 1.5B & PubMed & \\{0, 0.5, 1.0\\} & 3 & QLoRA $r{=}16$ & 0.5 \\\\\nC4 & Qwen2.5-0.5B & 494M & WikiText-2 & \\{0, 0.5, 1.0\\} & 1 & Full FT & 100 \\\\\nC5 & Qwen2.5-3B & 3B & WikiText-2 & \\{0, 0.5, 1.0\\} & 1 & QLoRA $r{=}16$ & 0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWikiText-2~\\citep{merity2017pointer} is tokenized and chunked into 512-token sequences (4{,}916 training chunks).\nPubMed abstracts (C3) undergo identical preprocessing.\n\n\\subsection{Evaluation Framework}\n\\label{sec:evaluation}\n\n\\paragraph{Cross-generation severity.}\nFor each signal $s$ and generation $g$, we compute the Spearman rank correlation $\\rho_g^{(s)}$ between contamination fraction $\\alpha$ and the end-of-generation signal value across all tested fractions, with 95\\% bootstrap confidence intervals.\nWe report Cohen's $d$ effect sizes between the clean baseline and each contamination level as the primary evidence for signal sensitivity, since rank correlations alone do not convey the magnitude of signal separation.\n\n\\paragraph{Within-generation detection.}\nWe compute the area under the ROC curve (AUROC) for binary collapse detection at each signal checkpoint (every 50 steps), using \\emph{clustered bootstrap} resampling.\nThe cluster unit is fraction$\\times$seed rather than individual generation observations.\nThis is necessary because successive generations within a run are causally dependent---generation $g{+}1$ trains on data produced by the model from generation $g$---so pooling individual observations would inflate the effective sample size and produce artificially narrow confidence intervals.\n\nWe also compute the relative deviation at each checkpoint:\n\\begin{equation}\n    \\Delta_s(t, \\alpha) = \\frac{|s_\\alpha(t) - s_0(t)|}{|s_0(t)|} \\times 100\\%,\n    \\label{eq:deviation}\n\\end{equation}\nwhere $s_\\alpha(t)$ and $s_0(t)$ are signal values at step $t$ for fraction $\\alpha$ and the clean baseline.\nA signal provides early warning if $\\Delta_s(t, \\alpha) > 5\\%$ within the first 10\\% of training steps.\n\n\\paragraph{Method-dependence.}\nWe compare signal trajectories between QLoRA (C1) and full fine-tuning (C4) under matched model size, dataset, and contamination fractions.\nPaired differences in end-of-generation signal values quantify whether collapse signatures depend on the fine-tuning method or reflect properties of the data contamination itself.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0f94f9a-c517-4753-bdf8-3c494b9dc1da",
  "isSidechain": false,
  "requestId": "req_011Cb56YkuQSsnJd2ETatSBA",
  "type": "assistant",
  "uuid": "c2ebd987-11a0-49ee-a14e-867e2fdb3c89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXdbAdqNPfrYiEUJR2Zehs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10566,
      "cache_read_input_tokens": 24701,
      "output_tokens": 9125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10566,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9125,
          "cache_read_input_tokens": 24701,
          "cache_creation_input_tokens": 10566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10566
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

_source line 18 · 2026-05-15T21:54:56.110Z_

<details><summary>↩ Tool result · `toolu_01MEkK856Wp8jbL1VmG5b5ha`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2ebd987-11a0-49ee-a14e-867e2fdb3c89",
  "isSidechain": false,
  "promptId": "ae09a607-e5a2-46f5-8d19-601dcf6d2541",
  "type": "user",
  "uuid": "3885aad6-7d4d-4592-ba44-5e934f154602",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex",
    "content": "% Method section — collapse_severity_monitor\n\n\\section{Methodology}\n\\label{sec:method}\n\nWe design a controlled framework to evaluate how training-time signals track model collapse severity under iterative synthetic data contamination.\nOur protocol varies contamination level and generational depth while monitoring four families of signals across five experimental configurations.\n\n\\subsection{Iterative Training Protocol}\n\\label{sec:protocol}\n\nWe simulate iterative model collapse through a multi-generation fine-tuning loop.\nLet $M_0$ denote a pretrained base model and $\\mathcal{D}_\\text{real}$ a corpus of real text.\nAt each generation $g \\in \\{0, 1, \\ldots, G{-}1\\}$ (with $G=5$), we execute three steps:\n\n\\begin{enumerate}\n    \\item \\textbf{Fine-tune.} Initialize from $M_0$ and fine-tune on the current training corpus $\\mathcal{D}_g$, yielding model $\\tilde{M}_g$. During training, we collect monitoring signals every 50 optimizer steps via a callback on a held-out validation set (Section~\\ref{sec:signals}).\n    \\item \\textbf{Generate.} Sample synthetic text $\\mathcal{S}_g$ from $\\tilde{M}_g$ by prompting with the first 32 tokens of randomly subsampled chunks from $\\mathcal{D}_\\text{real}$ and generating up to 480 new tokens with nucleus sampling ($p=0.95$, temperature $\\tau=1.0$). We subsample 1{,}500 chunks for generation.\n    \\item \\textbf{Mix.} Construct the next-generation corpus by replacing fraction $\\alpha$ of real chunks with synthetic chunks:\n    \\begin{equation}\n        \\mathcal{D}_{g+1} = (1 - \\alpha)\\,\\mathcal{D}_\\text{real} \\cup \\alpha\\,\\mathcal{S}_g.\n        \\label{eq:mixing}\n    \\end{equation}\n\\end{enumerate}\n\n\\noindent\nEach generation initializes from the \\emph{same} pretrained weights $M_0$, isolating the effect of data contamination from cumulative weight drift.\nCollapse pressure enters solely through the training corpus: at generation $g$, the synthetic component was produced by a model trained on data that itself contained synthetic text from generation $g{-}1$.\n\nAll fine-tuning runs use AdamW with learning rate $2 \\times 10^{-4}$, weight decay $0.01$, linear warmup over $5\\%$ of steps, and gradient clipping at $\\|\\cdot\\|_2 \\leq 1.0$.\nWe train for 5 epochs with effective batch size 16 (per-device batch 4, gradient accumulation 4) in \\texttt{bf16} mixed precision.\nQLoRA configurations~\\citep{dettmers2023qlora} use rank $r=16$, scaling factor $\\alpha_\\text{LoRA}=32$, dropout $0.05$, with adapters on all linear projections (\\texttt{q\\_proj}, \\texttt{k\\_proj}, \\texttt{v\\_proj}, \\texttt{o\\_proj}, \\texttt{up\\_proj}, \\texttt{down\\_proj}, \\texttt{gate\\_proj}); the base model is quantized to 4-bit NormalFloat (NF4) with double quantization.\nFull fine-tuning (C4; Table~\\ref{tab:configs}) uses identical hyperparameters with all parameters trainable and no quantization.\n\n\\subsection{Contamination Fractions}\n\\label{sec:fractions}\n\nWe test six contamination levels: $\\alpha \\in \\{0, 0.1, 0.25, 0.5, 0.75, 1.0\\}$.\nThe $\\alpha=0$ condition serves as a clean baseline, controlling for training noise and natural run-to-run variance in the absence of synthetic contamination.\nThe $\\alpha=1.0$ condition replaces the entire training set with synthetic data, applying maximum collapse pressure.\nIntermediate fractions trace the dose--response relationship between contamination level and signal behavior.\n\n\\subsection{Monitoring Signals}\n\\label{sec:signals}\n\nWe monitor four families of training-time signals, collected every 50 optimizer steps on a held-out validation set in evaluation mode.\n\n\\paragraph{Spectral signals.}\nGiven $n$ validation sequences, we collect last-layer hidden states into a matrix $\\mathbf{H} \\in \\mathbb{R}^{T \\times d}$ ($T$ total tokens, $d$ hidden dimension), center by subtracting the column mean, and compute the sample covariance $\\mathbf{C} = \\frac{1}{T-1}\\mathbf{H}^\\top\\mathbf{H}$ with eigenvalues $\\lambda_1 \\geq \\cdots \\geq \\lambda_d \\geq 0$.\n\n\\emph{Stable rank} measures the effective dimensionality of the representation:\n\\begin{equation}\n    \\mathrm{SR}(\\mathbf{C}) = \\frac{\\left(\\sum_{i=1}^{d} \\lambda_i\\right)^2}{\\sum_{i=1}^{d} \\lambda_i^2}.\n    \\label{eq:stable_rank}\n\\end{equation}\nUnder model collapse, $\\mathrm{SR}$ \\emph{increases}: the Frobenius norm $\\|\\mathbf{H}\\|_F^2$ grows faster than the leading eigenvalue $\\lambda_1$, dispersing energy across more dimensions rather than concentrating it.%\n\\footnote{This is the participation ratio of the covariance eigenspectrum, closely related to but distinct from the matrix stable rank $\\|\\mathbf{H}\\|_F^2 / \\|\\mathbf{H}\\|_2^2$; the two are monotonically related for centered data.}\n\n\\emph{Spectral entropy} provides a complementary measure of spectral concentration:\n\\begin{equation}\n    \\mathrm{SE}(\\mathbf{C}) = \\frac{-\\sum_{i=1}^{d} p_i \\log p_i}{\\log d}, \\quad p_i = \\frac{\\lambda_i}{\\sum_{j=1}^{d} \\lambda_j}.\n    \\label{eq:spectral_entropy}\n\\end{equation}\n$\\mathrm{SE} \\in [0,1]$, with $\\mathrm{SE}=1$ for a uniform spectrum and $\\mathrm{SE} \\to 0$ for concentration on few components.\nWe use $n=64$ validation chunks for SVD computation.\n\n\\paragraph{Output signals.}\nWe distinguish two perplexity regimes.\n\\emph{Training perplexity}, computed on the current (potentially contaminated) training batch, measures fit to the data mix; it can \\emph{decrease} even as the model collapses, since the model fits its own synthetic output well.\n\\emph{Evaluation perplexity}, computed on a held-out clean set, reliably tracks degradation in language modeling quality on real text:\n\\begin{equation}\n    \\mathrm{PPL}_\\text{eval} = \\exp\\!\\left(\\frac{1}{N}\\sum_{i=1}^{|\\mathcal{V}|} \\ell(\\mathbf{x}_i)\\right),\n    \\label{eq:perplexity}\n\\end{equation}\nwhere $\\ell(\\mathbf{x}_i)$ is the cross-entropy loss on validation sequence $\\mathbf{x}_i$ and $N$ is the total token count.\nThis distinction is critical for within-generation detection (Section~\\ref{sec:evaluation}): training perplexity is a misleading signal, while evaluation perplexity is a reliable one.\n\n\\emph{Token entropy} measures the mean per-position entropy of the next-token distribution:\n\\begin{equation}\n    \\mathrm{TE}(\\mathbf{x}) = \\frac{1}{L-1}\\sum_{t=1}^{L-1} H\\!\\left(P_\\theta(\\cdot \\mid x_{\\leq t})\\right), \\quad H(P) = -\\sum_v P(v) \\log P(v),\n    \\label{eq:token_entropy}\n\\end{equation}\naveraged over 100 validation chunks.\nDecreasing token entropy indicates the model is becoming more peaked in its predictions, a hallmark of mode collapse in generation.\n\n\\paragraph{Gradient signal.}\nWe log the L2 gradient norm $\\|\\nabla_\\theta \\mathcal{L}\\|_2$ before each optimizer step.\nGradient norm is a zero-cost byproduct of standard training.\nUnder QLoRA, gradient norm exhibits non-monotonic behavior with respect to contamination fraction: gradients flow only through low-rank adapter matrices~\\citep{hu2022lora}, confining the landscape to a rank-$r$ subspace, and NF4 quantization of frozen base weights introduces discretization noise that propagates through the backward pass~\\citep{dettmers2023qlora}.\n\n\\paragraph{Downstream signal.}\nWe evaluate HellaSwag~\\citep{zellers2019hellaswag} accuracy (4-choice commonsense reasoning, 1{,}000 samples) at the end of each generation as a downstream task probe.\n\n\\subsection{Experimental Configurations}\n\\label{sec:configs}\n\nTable~\\ref{tab:configs} summarizes our five experimental configurations.\nC1 provides initial signal discovery on the smallest model.\nC2 is the primary analysis configuration, with five independent seeds providing statistical power for bootstrap confidence intervals and effect size estimation.\nC3 tests cross-domain generalization on biomedical text.\nC4 isolates method-dependence by comparing full fine-tuning against QLoRA under matched conditions.\nC5 provides a scale spot-check at 3B parameters.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Experimental configurations. Trainable\\% indicates the fraction of parameters updated during fine-tuning.}\n\\label{tab:configs}\n\\begin{tabular}{llrllcll}\n\\toprule\nID & Model & Params & Dataset & Fractions ($\\alpha$) & Seeds & Method & Train.\\% \\\\\n\\midrule\nC1 & Qwen2.5-0.5B & 494M & WikiText-2 & \\{0, 0.5, 1.0\\} & 1 & QLoRA $r{=}16$ & 0.8 \\\\\nC2 & Qwen2.5-1.5B & 1.5B & WikiText-2 & \\{0, 0.1, \\ldots, 1.0\\} & 5 & QLoRA $r{=}16$ & 0.5 \\\\\nC3 & Qwen2.5-1.5B & 1.5B & PubMed & \\{0, 0.5, 1.0\\} & 3 & QLoRA $r{=}16$ & 0.5 \\\\\nC4 & Qwen2.5-0.5B & 494M & WikiText-2 & \\{0, 0.5, 1.0\\} & 1 & Full FT & 100 \\\\\nC5 & Qwen2.5-3B & 3B & WikiText-2 & \\{0, 0.5, 1.0\\} & 1 & QLoRA $r{=}16$ & 0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWikiText-2~\\citep{merity2017pointer} is tokenized and chunked into 512-token sequences (4{,}916 training chunks).\nPubMed abstracts (C3) undergo identical preprocessing.\n\n\\subsection{Evaluation Framework}\n\\label{sec:evaluation}\n\n\\paragraph{Cross-generation severity.}\nFor each signal $s$ and generation $g$, we compute the Spearman rank correlation $\\rho_g^{(s)}$ between contamination fraction $\\alpha$ and the end-of-generation signal value across all tested fractions, with 95\\% bootstrap confidence intervals.\nWe report Cohen's $d$ effect sizes between the clean baseline and each contamination level as the primary evidence for signal sensitivity, since rank correlations alone do not convey the magnitude of signal separation.\n\n\\paragraph{Within-generation detection.}\nWe compute the area under the ROC curve (AUROC) for binary collapse detection at each signal checkpoint (every 50 steps), using \\emph{clustered bootstrap} resampling.\nThe cluster unit is fraction$\\times$seed rather than individual generation observations.\nThis is necessary because successive generations within a run are causally dependent---generation $g{+}1$ trains on data produced by the model from generation $g$---so pooling individual observations would inflate the effective sample size and produce artificially narrow confidence intervals.\n\nWe also compute the relative deviation at each checkpoint:\n\\begin{equation}\n    \\Delta_s(t, \\alpha) = \\frac{|s_\\alpha(t) - s_0(t)|}{|s_0(t)|} \\times 100\\%,\n    \\label{eq:deviation}\n\\end{equation}\nwhere $s_\\alpha(t)$ and $s_0(t)$ are signal values at step $t$ for fraction $\\alpha$ and the clean baseline.\nA signal provides early warning if $\\Delta_s(t, \\alpha) > 5\\%$ within the first 10\\% of training steps.\n\n\\paragraph{Method-dependence.}\nWe compare signal trajectories between QLoRA (C1) and full fine-tuning (C4) under matched model size, dataset, and contamination fractions.\nPaired differences in end-of-generation signal values quantify whether collapse signatures depend on the fine-tuning method or reflect properties of the data contamination itself.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 182,
        "newStart": 1,
        "newLines": 147,
        "lines": [
          " % Method section — collapse_severity_monitor",
          "-% Sources: MVP (mvp_frac50_100, within_gen_analysis, per_layer_analysis_v5)",
          "-% Pending: plan_001 (1.5B scale, 6 fractions, 5 seeds)",
          " ",
          " \\section{Methodology}",
          " \\label{sec:method}",
          " ",
          "-We design a controlled experimental framework to evaluate how training dynamic signals track model collapse severity under iterative synthetic data contamination.",
          "-Our protocol varies contamination level and generational depth while monitoring four families of training-time signals.",
          "+We design a controlled framework to evaluate how training-time signals track model collapse severity under iterative synthetic data contamination.",
          "+Our protocol varies contamination level and generational depth while monitoring four families of signals across five experimental configurations.",
          " ",
          "-\\subsection{Iterative Synthetic Data Protocol}",
          "+\\subsection{Iterative Training Protocol}",
          " \\label{sec:protocol}",
          " ",
          " We simulate iterative model collapse through a multi-generation fine-tuning loop.",
          "-Let $M_0$ denote a pretrained base model and $\\mathcal{D}_\\text{real}$ a real-text corpus.",
          "-At each generation $g \\in \\{0, 1, \\ldots, G{-}1\\}$ (with $G=5$), we execute the following steps:",
          "+Let $M_0$ denote a pretrained base model and $\\mathcal{D}_\\text{real}$ a corpus of real text.",
          "+At each generation $g \\in \\{0, 1, \\ldots, G{-}1\\}$ (with $G=5$), we execute three steps:",
          " ",
          " \\begin{enumerate}",
          "-    \\item \\textbf{Fine-tune.} Initialize from $M_0$ with a QLoRA adapter and fine-tune on the current training corpus $\\mathcal{D}_g$, yielding adapted model $\\tilde{M}_g$.",
          "-    During training, we collect monitoring signals every 50 optimizer steps via a callback (Section~\\ref{sec:signals}).",
          "-    \\item \\textbf{Generate.} Sample synthetic text $\\mathcal{S}_g$ from $\\tilde{M}_g$ by prompting with the first 32 tokens of randomly subsampled chunks from $\\mathcal{D}_\\text{real}$ and generating up to 480 new tokens with nucleus sampling ($p=0.95$, temperature $\\tau=1.0$).",
          "-    We subsample 1{,}500 of $|\\mathcal{D}_\\text{real}|$ chunks for generation to keep wall-clock time tractable.",
          "-    \\item \\textbf{Mix.} Construct the next-generation corpus $\\mathcal{D}_{g+1}$ by replacing a fraction $\\alpha \\in \\{0, 0.1, 0.25, 0.5, 0.75, 1.0\\}$ of real chunks with synthetic chunks from $\\mathcal{S}_g$:",
          "+    \\item \\textbf{Fine-tune.} Initialize from $M_0$ and fine-tune on the current training corpus $\\mathcal{D}_g$, yielding model $\\tilde{M}_g$. During training, we collect monitoring signals every 50 optimizer steps via a callback on a held-out validation set (Section~\\ref{sec:signals}).",
          "+    \\item \\textbf{Generate.} Sample synthetic text $\\mathcal{S}_g$ from $\\tilde{M}_g$ by prompting with the first 32 tokens of randomly subsampled chunks from $\\mathcal{D}_\\text{real}$ and generating up to 480 new tokens with nucleus sampling ($p=0.95$, temperature $\\tau=1.0$). We subsample 1{,}500 chunks for generation.",
          "+    \\item \\textbf{Mix.} Construct the next-generation corpus by replacing fraction $\\alpha$ of real chunks with synthetic chunks:",
          "     \\begin{equation}",
          "         \\mathcal{D}_{g+1} = (1 - \\alpha)\\,\\mathcal{D}_\\text{real} \\cup \\alpha\\,\\mathcal{S}_g.",
          "         \\label{eq:mixing}",
          "     \\end{equation}",
          "-    The $\\alpha=0$ condition serves as a no-contamination baseline.",
          " \\end{enumerate}",
          " ",
          " \\noindent",
          "-Each generation thus starts from the \\emph{same} pretrained weights $M_0$, isolating the effect of data contamination from cumulative weight drift.",
          "-The collapse pressure enters solely through the training corpus: at generation $g$, the synthetic component was produced by a model trained on data that itself contained synthetic text from generation $g{-}1$.",
          "+Each generation initializes from the \\emph{same} pretrained weights $M_0$, isolating the effect of data contamination from cumulative weight drift.",
          "+Collapse pressure enters solely through the training corpus: at generation $g$, the synthetic component was produced by a model trained on data that itself contained synthetic text from generation $g{-}1$.",
          " ",
          "-\\paragraph{Models.}",
          "-We use Qwen2.5-0.5B as our primary model (24 transformer layers, 494M parameters).%",
          "-\\footnote{Scale validation on Qwen2.5-1.5B (28 layers, 1.5B parameters) is in progress; preliminary results will be included in the final version.}",
          "-All experiments use QLoRA~\\citep{dettmers2023qlora} with rank $r=16$, scaling factor $\\alpha_\\text{LoRA}=32$, and dropout $0.05$.",
          "-Adapters are applied to all linear projections in each transformer layer: \\texttt{q\\_proj}, \\texttt{k\\_proj}, \\texttt{v\\_proj}, \\texttt{o\\_proj}, \\texttt{up\\_proj}, \\texttt{down\\_proj}, and \\texttt{gate\\_proj}.",
          "-The base model is quantized to 4-bit NormalFloat (NF4) with double quantization.",
          "+All fine-tuning runs use AdamW with learning rate $2 \\times 10^{-4}$, weight decay $0.01$, linear warmup over $5\\%$ of steps, and gradient clipping at $\\|\\cdot\\|_2 \\leq 1.0$.",
          "+We train for 5 epochs with effective batch size 16 (per-device batch 4, gradient accumulation 4) in \\texttt{bf16} mixed precision.",
          "+QLoRA configurations~\\citep{dettmers2023qlora} use rank $r=16$, scaling factor $\\alpha_\\text{LoRA}=32$, dropout $0.05$, with adapters on all linear projections (\\texttt{q\\_proj}, \\texttt{k\\_proj}, \\texttt{v\\_proj}, \\texttt{o\\_proj}, \\texttt{up\\_proj}, \\texttt{down\\_proj}, \\texttt{gate\\_proj}); the base model is quantized to 4-bit NormalFloat (NF4) with double quantization.",
          "+Full fine-tuning (C4; Table~\\ref{tab:configs}) uses identical hyperparameters with all parameters trainable and no quantization.",
          " ",
          "-\\paragraph{Data.}",
          "-We use WikiText-2 (\\texttt{wikitext-2-raw-v1})~\\citep{merity2017pointer}, tokenized and chunked into fixed-length sequences of 512 tokens, yielding 4{,}916 training chunks and a held-out validation set.%",
          "-\\footnote{Cross-domain validation on PubMed abstracts is planned as a secondary axis.}",
          "+\\subsection{Contamination Fractions}",
          "+\\label{sec:fractions}",
          " ",
          "-\\paragraph{Training configuration.}",
          "-All fine-tuning runs use the AdamW optimizer with learning rate $2 \\times 10^{-4}$, weight decay $0.01$, linear warmup over $5\\%$ of steps, and gradient clipping at $\\|\\cdot\\|_2 \\leq 1.0$.",
          "-We train for 5 epochs with per-device batch size 4 and gradient accumulation over 4 steps (effective batch size 16), using \\texttt{bf16} mixed precision.",
          "-Each generation comprises approximately 1{,}540 optimizer steps.",
          "+We test six contamination levels: $\\alpha \\in \\{0, 0.1, 0.25, 0.5, 0.75, 1.0\\}$.",
          "+The $\\alpha=0$ condition serves as a clean baseline, controlling for training noise and natural run-to-run variance in the absence of synthetic contamination.",
          "+The $\\alpha=1.0$ condition replaces the entire training set with synthetic data, applying maximum collapse pressure.",
          "+Intermediate fractions trace the dose--response relationship between contamination level and signal behavior.",
          " ",
          "-\\paragraph{Contamination fractions.}",
          "-Our MVP experiments use three fractions ($\\alpha \\in \\{0, 0.5, 1.0\\}$) with a single seed.",
          "-The full experimental design extends to six fractions ($\\alpha \\in \\{0, 0.1, 0.25, 0.5, 0.75, 1.0\\}$) with 5 independent seeds per configuration, yielding 150 fine-tuning runs (6~fractions $\\times$ 5~generations $\\times$ 5~seeds).%",
          "-\\footnote{MVP results (3 fractions, seed 42) are reported here; full 6-fraction $\\times$ 5-seed results pending \\texttt{plan\\_001}.}",
          "-",
          "-\\subsection{Signal Families}",
          "+\\subsection{Monitoring Signals}",
          " \\label{sec:signals}",
          " ",
          "-We monitor four families of training-time signals, collected every 50 optimizer steps via a training callback.",
          "-All signals are computed on a held-out validation set in evaluation mode.",
          "+We monitor four families of training-time signals, collected every 50 optimizer steps on a held-out validation set in evaluation mode.",
          " ",
          "-\\subsubsection{Spectral Signals}",
          "-\\label{sec:spectral}",
          "+\\paragraph{Spectral signals.}",
          "+Given $n$ validation sequences, we collect last-layer hidden states into a matrix $\\mathbf{H} \\in \\mathbb{R}^{T \\times d}$ ($T$ total tokens, $d$ hidden dimension), center by subtracting the column mean, and compute the sample covariance $\\mathbf{C} = \\frac{1}{T-1}\\mathbf{H}^\\top\\mathbf{H}$ with eigenvalues $\\lambda_1 \\geq \\cdots \\geq \\lambda_d \\geq 0$.",
          " ",
          "-Spectral signals characterize the geometry of the model's internal representations.",
          "-Given a set of $n$ validation sequences, we collect the last-layer hidden states into a matrix $\\mathbf{H} \\in \\mathbb{R}^{T \\times d}$, where $T$ is the total number of tokens across $n$ sequences and $d$ is the hidden dimension.",
          "-We center $\\mathbf{H}$ by subtracting its column mean, then compute the sample covariance:",
          "+\\emph{Stable rank} measures the effective dimensionality of the representation:",
          " \\begin{equation}",
          "-    \\mathbf{C} = \\frac{1}{T-1}\\,\\mathbf{H}^\\top \\mathbf{H} \\in \\mathbb{R}^{d \\times d}.",
          "-\\end{equation}",
          "-Let $\\lambda_1 \\geq \\lambda_2 \\geq \\cdots \\geq \\lambda_d \\geq 0$ denote the eigenvalues of $\\mathbf{C}$ (equivalently, its singular values, since $\\mathbf{C}$ is positive semidefinite).",
          "-",
          "-\\paragraph{Stable rank.}",
          "-The participation ratio of the eigenspectrum measures the effective dimensionality of the representation:",
          "-\\begin{equation}",
          "     \\mathrm{SR}(\\mathbf{C}) = \\frac{\\left(\\sum_{i=1}^{d} \\lambda_i\\right)^2}{\\sum_{i=1}^{d} \\lambda_i^2}.",
          "     \\label{eq:stable_rank}",
          " \\end{equation}",
          "-$\\mathrm{SR} = 1$ when all variance concentrates on a single component; $\\mathrm{SR} = d$ when variance is uniformly distributed.",
          "-Under model collapse, we observe that $\\mathrm{SR}$ \\emph{increases}: the Frobenius norm of the representation grows faster than its leading eigenvalue, dispersing energy across more dimensions rather than concentrating it.%",
          "+Under model collapse, $\\mathrm{SR}$ \\emph{increases}: the Frobenius norm $\\|\\mathbf{H}\\|_F^2$ grows faster than the leading eigenvalue $\\lambda_1$, dispersing energy across more dimensions rather than concentrating it.%",
          " \\footnote{This is the participation ratio of the covariance eigenspectrum, closely related to but distinct from the matrix stable rank $\\|\\mathbf{H}\\|_F^2 / \\|\\mathbf{H}\\|_2^2$; the two are monotonically related for centered data.}",
          " ",
          "-\\paragraph{Spectral entropy.}",
          "-The normalized entropy of the eigenspectrum provides a complementary measure of spectral concentration:",
          "+\\emph{Spectral entropy} provides a complementary measure of spectral concentration:",
          " \\begin{equation}",
          "-    \\mathrm{SE}(\\mathbf{C}) = \\frac{-\\sum_{i=1}^{d} p_i \\log p_i}{\\log d}, \\quad \\text{where } p_i = \\frac{\\lambda_i}{\\sum_{j=1}^{d} \\lambda_j}.",
          "+    \\mathrm{SE}(\\mathbf{C}) = \\frac{-\\sum_{i=1}^{d} p_i \\log p_i}{\\log d}, \\quad p_i = \\frac{\\lambda_i}{\\sum_{j=1}^{d} \\lambda_j}.",
          "     \\label{eq:spectral_entropy}",
          " \\end{equation}",
          "-$\\mathrm{SE} \\in [0, 1]$, with $\\mathrm{SE} = 1$ indicating a uniform spectrum and $\\mathrm{SE} \\to 0$ indicating concentration on few components.",
          "-We use $n=64$ validation chunks for SVD computation, retaining the top-5 singular values for trajectory logging.",
          "+$\\mathrm{SE} \\in [0,1]$, with $\\mathrm{SE}=1$ for a uniform spectrum and $\\mathrm{SE} \\to 0$ for concentration on few components.",
          "+We use $n=64$ validation chunks for SVD computation.",
          " ",
          "-\\subsubsection{Output Signals}",
          "-\\label{sec:output}",
          "-",
          "-Output signals measure the model's predictive behavior on held-out real text.",
          "-",
          "-\\paragraph{Token entropy.}",
          "-For each validation sequence $\\mathbf{x} = (x_1, \\ldots, x_L)$, we compute the mean per-position entropy of the next-token distribution:",
          "+\\paragraph{Output signals.}",
          "+We distinguish two perplexity regimes.",
          "+\\emph{Training perplexity}, computed on the current (potentially contaminated) training batch, measures fit to the data mix; it can \\emph{decrease} even as the model collapses, since the model fits its own synthetic output well.",
          "+\\emph{Evaluation perplexity}, computed on a held-out clean set, reliably tracks degradation in language modeling quality on real text:",
          " \\begin{equation}",
          "-    \\mathrm{TE}(\\mathbf{x}) = \\frac{1}{L-1} \\sum_{t=1}^{L-1} H\\!\\left(P_\\theta(\\cdot \\mid x_{\\leq t})\\right), \\quad H(P) = -\\sum_{v} P(v) \\log P(v),",
          "-    \\label{eq:token_entropy}",
          "+    \\mathrm{PPL}_\\text{eval} = \\exp\\!\\left(\\frac{1}{N}\\sum_{i=1}^{|\\mathcal{V}|} \\ell(\\mathbf{x}_i)\\right),",
          "+    \\label{eq:perplexity}",
          " \\end{equation}",
          "-and report the average over 100 validation chunks.",
          "-Decreasing token entropy indicates the model is becoming more ``peaked'' in its predictions---a hallmark of mode collapse in generation.",
          "+where $\\ell(\\mathbf{x}_i)$ is the cross-entropy loss on validation sequence $\\mathbf{x}_i$ and $N$ is the total token count.",
          "+This distinction is critical for within-generation detection (Section~\\ref{sec:evaluation}): training perplexity is a misleading signal, while evaluation perplexity is a reliable one.",
          " ",
          "-\\paragraph{Perplexity.}",
          "-We compute perplexity as the exponentiated mean per-token negative log-likelihood over the full validation set:",
          "+\\emph{Token entropy} measures the mean per-position entropy of the next-token distribution:",
          " \\begin{equation}",
          "-    \\mathrm{PPL} = \\exp\\!\\left(\\frac{1}{N}\\sum_{i=1}^{|\\mathcal{V}|} \\ell(\\mathbf{x}_i)\\right),",
          "-    \\label{eq:perplexity}",
          "+    \\mathrm{TE}(\\mathbf{x}) = \\frac{1}{L-1}\\sum_{t=1}^{L-1} H\\!\\left(P_\\theta(\\cdot \\mid x_{\\leq t})\\right), \\quad H(P) = -\\sum_v P(v) \\log P(v),",
          "+    \\label{eq:token_entropy}",
          " \\end{equation}",
          "-where $\\ell(\\mathbf{x}_i)$ is the cross-entropy loss on validation sequence $\\mathbf{x}_i$ and $N$ is the total token count.",
          "-Perplexity captures degradation in language modeling quality; under severe collapse, it increases by orders of magnitude (e.g., $15.7 \\to 839.2$ over 5 generations at $\\alpha=1.0$ in our MVP; source: \\texttt{mvp\\_frac50\\_100}).",
          "+averaged over 100 validation chunks.",
          "+Decreasing token entropy indicates the model is becoming more peaked in its predictions, a hallmark of mode collapse in generation.",
          " ",
          "-\\subsubsection{Gradient Signal}",
          "-\\label{sec:gradient}",
          "+\\paragraph{Gradient signal.}",
          "+We log the L2 gradient norm $\\|\\nabla_\\theta \\mathcal{L}\\|_2$ before each optimizer step.",
          "+Gradient norm is a zero-cost byproduct of standard training.",
          "+Under QLoRA, gradient norm exhibits non-monotonic behavior with respect to contamination fraction: gradients flow only through low-rank adapter matrices~\\citep{hu2022lora}, confining the landscape to a rank-$r$ subspace, and NF4 quantization of frozen base weights introduces discretization noise that propagates through the backward pass~\\citep{dettmers2023qlora}.",
          " ",
          "-We log the L2 gradient norm $\\|\\nabla_\\theta \\mathcal{L}\\|_2$ computed by the trainer before each optimizer step.",
          "-Gradient norm is a zero-cost byproduct of standard training and reflects optimization landscape curvature.",
          "-In our MVP experiments, gradient norm exhibits non-monotonic behavior with respect to contamination fraction under QLoRA, limiting its utility as a standalone severity monitor (Section~\\ref{sec:results}).",
          "-We attribute this non-monotonicity to two interacting factors specific to QLoRA training.",
          "-First, gradients flow only through the low-rank adapter matrices $A \\in \\mathbb{R}^{d \\times r}$ and $B \\in \\mathbb{R}^{r \\times d}$ rather than the full weight matrix~\\citep{hu2022lora}, so the gradient landscape is confined to a rank-$r$ subspace that can amplify or attenuate contamination-induced shifts in ways that do not mirror full-rank fine-tuning.",
          "-Second, the NF4 quantization of frozen base weights introduces discretization noise that propagates through the backward pass~\\citep{dettmers2023qlora}, adding a stochastic component to the gradient norm that obscures the monotonic contamination signal visible in spectral and output metrics.",
          "+\\paragraph{Downstream signal.}",
          "+We evaluate HellaSwag~\\citep{zellers2019hellaswag} accuracy (4-choice commonsense reasoning, 1{,}000 samples) at the end of each generation as a downstream task probe.",
          " ",
          "-\\subsubsection{Downstream Signal}",
          "-\\label{sec:downstream}",
          "+\\subsection{Experimental Configurations}",
          "+\\label{sec:configs}",
          " ",
          "-We evaluate HellaSwag~\\citep{zellers2019hellaswag} accuracy (4-choice commonsense reasoning, 1{,}000 samples) as a downstream task probe.",
          "-HellaSwag is computed at the end of each generation (not at every signal checkpoint, due to evaluation cost).",
          "-At the 0.5B scale, HellaSwag shows minimal sensitivity to collapse: accuracy drops only 1.2\\% (0.435 $\\to$ 0.430) despite catastrophic perplexity explosion, suggesting that small-model benchmark performance is a poor proxy for generative collapse severity (source: \\texttt{mvp\\_frac50\\_100}).",
          "+Table~\\ref{tab:configs} summarizes our five experimental configurations.",
          "+C1 provides initial signal discovery on the smallest model.",
          "+C2 is the primary analysis configuration, with five independent seeds providing statistical power for bootstrap confidence intervals and effect size estimation.",
          "+C3 tests cross-domain generalization on biomedical text.",
          "+C4 isolates method-dependence by comparing full fine-tuning against QLoRA under matched conditions.",
          "+C5 provides a scale spot-check at 3B parameters.",
          " ",
          "-\\subsection{Evaluation Methodology}",
          "-\\label{sec:evaluation}",
          "+\\begin{table}[t]",
          "+\\centering",
          "+\\small",
          "+\\caption{Experimental configurations. Trainable\\% indicates the fraction of parameters updated during fine-tuning.}",
          "+\\label{tab:configs}",
          "+\\begin{tabular}{llrllcll}",
          "+\\toprule",
          "+ID & Model & Params & Dataset & Fractions ($\\alpha$) & Seeds & Method & Train.\\% \\\\",
          "+\\midrule",
          "+C1 & Qwen2.5-0.5B & 494M & WikiText-2 & \\{0, 0.5, 1.0\\} & 1 & QLoRA $r{=}16$ & 0.8 \\\\",
          "+C2 & Qwen2.5-1.5B & 1.5B & WikiText-2 & \\{0, 0.1, \\ldots, 1.0\\} & 5 & QLoRA $r{=}16$ & 0.5 \\\\",
          "+C3 & Qwen2.5-1.5B & 1.5B & PubMed & \\{0, 0.5, 1.0\\} & 3 & QLoRA $r{=}16$ & 0.5 \\\\",
          "+C4 & Qwen2.5-0.5B & 494M & WikiText-2 & \\{0, 0.5, 1.0\\} & 1 & Full FT & 100 \\\\",
          "+C5 & Qwen2.5-3B & 3B & WikiText-2 & \\{0, 0.5, 1.0\\} & 1 & QLoRA $r{=}16$ & 0.3 \\\\",
          "+\\bottomrule",
          "+\\end{tabular}",
          "+\\end{table}",
          " ",
          "-\\subsubsection{Cross-Fraction Severity Correlation}",
          "-\\label{sec:cross_fraction}",
          "+WikiText-2~\\citep{merity2017pointer} is tokenized and chunked into 512-token sequences (4{,}916 training chunks).",
          "+PubMed abstracts (C3) undergo identical preprocessing.",
          " ",
          "-For each signal $s$ and generation $g$, we compute the Spearman rank correlation $\\rho_g^{(s)}$ between contamination fraction $\\alpha$ and the end-of-generation signal value across all tested fractions.",
          "-We report the mean absolute correlation $\\bar{|\\rho|}^{(s)} = \\frac{1}{G}\\sum_{g=0}^{G-1} |\\rho_g^{(s)}|$ as a summary statistic.",
          "-A signal is considered a reliable severity monitor if $\\bar{|\\rho|}^{(s)} > 0.7$.",
          "+\\subsection{Evaluation Framework}",
          "+\\label{sec:evaluation}",
          " ",
          "-In the MVP (3 fractions, $n=1$ seed), spectral and output signals exhibit large effect sizes: 6.6$\\times$ stable rank separation and 53$\\times$ perplexity divergence between $\\alpha=0$ and $\\alpha=1.0$ at generation~4 ($|\\rho|=1.0$; trivially achievable with $n=3$ severity levels).",
          "-The 6-fraction design (pending \\texttt{plan\\_001}) provides a more stringent monotonicity test; we treat effect sizes as primary evidence throughout (source: \\texttt{mvp\\_frac50\\_100}).",
          "+\\paragraph{Cross-generation severity.}",
          "+For each signal $s$ and generation $g$, we compute the Spearman rank correlation $\\rho_g^{(s)}$ between contamination fraction $\\alpha$ and the end-of-generation signal value across all tested fractions, with 95\\% bootstrap confidence intervals.",
          "+We report Cohen's $d$ effect sizes between the clean baseline and each contamination level as the primary evidence for signal sensitivity, since rank correlations alone do not convey the magnitude of signal separation.",
          " ",
          "-\\subsubsection{Cross-Generation Tracking}",
          "-\\label{sec:cross_gen}",
          "+\\paragraph{Within-generation detection.}",
          "+We compute the area under the ROC curve (AUROC) for binary collapse detection at each signal checkpoint (every 50 steps), using \\emph{clustered bootstrap} resampling.",
          "+The cluster unit is fraction$\\times$seed rather than individual generation observations.",
          "+This is necessary because successive generations within a run are causally dependent---generation $g{+}1$ trains on data produced by the model from generation $g$---so pooling individual observations would inflate the effective sample size and produce artificially narrow confidence intervals.",
          " ",
          "-For each signal $s$ and contamination fraction $\\alpha$, we compute the Spearman correlation between generation index $g$ and end-of-generation signal value.",
          "-This measures whether signals track the \\emph{accumulation} of collapse across iterative retraining.",
          "-At $\\alpha=1.0$, perplexity exhibits super-linear growth across generations ($15.7 \\to 136.9 \\to 394.3 \\to 691.4 \\to 839.2$), consistent with the accelerating degradation predicted by model collapse theory~\\citep{Shumailov2024} (source: \\texttt{mvp\\_frac50\\_100}).",
          "-",
          "-\\subsubsection{Within-Generation Early Warning}",
          "-\\label{sec:early_warning}",
          "-",
          "-We assess how early within a single training run each signal can distinguish a contaminated condition from the clean baseline.",
          "-Specifically, we compute the relative deviation at each signal checkpoint:",
          "+We also compute the relative deviation at each checkpoint:",
          " \\begin{equation}",
          "     \\Delta_s(t, \\alpha) = \\frac{|s_\\alpha(t) - s_0(t)|}{|s_0(t)|} \\times 100\\%,",
          "     \\label{eq:deviation}",
          " \\end{equation}",
          "-where $s_\\alpha(t)$ and $s_0(t)$ are the signal values at step $t$ for fraction $\\alpha$ and the clean baseline ($\\alpha=0$), respectively.",
          "-A signal provides \\emph{early warning} if $\\Delta_s(t, \\alpha) > 5\\%$ within the first 10\\% of training steps.",
          "+where $s_\\alpha(t)$ and $s_0(t)$ are signal values at step $t$ for fraction $\\alpha$ and the clean baseline.",
          "+A signal provides early warning if $\\Delta_s(t, \\alpha) > 5\\%$ within the first 10\\% of training steps.",
          " ",
          "-In the MVP, stable rank achieves the largest early deviation: $\\Delta_\\mathrm{SR}(50, 1.0) = 34.4\\%$ at step 50 (${\\sim}3\\%$ training progress), followed by token entropy at 24.5\\% and perplexity at 17.7\\%.",
          "-Spectral entropy (5.0\\%) and gradient norm (2.1\\%) respond more slowly, first exceeding 5\\% at step 100 (${\\sim}6\\%$ progress) (source: \\texttt{within\\_gen\\_analysis}).",
          "-",
          "-\\subsubsection{Statistical Validity}",
          "-\\label{sec:stats}",
          "-",
          "-\\paragraph{Bootstrap confidence intervals.}",
          "-For the full experimental design (6 fractions $\\times$ 5 seeds), we compute 95\\% bootstrap confidence intervals for all reported correlations and effect sizes.",
          "-Crucially, we use \\emph{clustered bootstrap} with the cluster unit being fraction $\\times$ seed, rather than pooling individual generation observations.",
          "-Pooling would inflate sample size and produce artificially narrow intervals, because successive generations within a run are causally dependent---generation $g+1$ trains on data produced by the model from generation $g$.",
          "-",
          "-\\paragraph{AUROC for collapse detection.}",
          "-We compute the area under the receiver operating characteristic curve (AUROC) for binary collapse detection at various severity thresholds (e.g., $\\alpha \\geq 0.5$ vs.\\ $\\alpha < 0.5$).",
          "-In the MVP (3 fractions, single seed), stable rank, spectral entropy, and token entropy each achieve AUROC $= 1.0$ for distinguishing the $\\alpha = 1.0$ condition at step 50.",
          "-We treat AUROC as a secondary metric supporting the primary evidence from effect sizes and rank correlations, given the small sample size in the MVP (source: \\texttt{within\\_gen\\_analysis}).",
          "-",
          "-\\paragraph{Effect sizes.}",
          "-We prioritize absolute and relative effect sizes (e.g., 6.6$\\times$ stable rank separation between $\\alpha=0$ and $\\alpha=1.0$ at generation 4) as primary evidence, with rank correlations as supporting statistics.",
          "-This hierarchy follows from the observation that $|\\rho| = 1.0$ is easily achieved with few fractions and does not convey the \\emph{magnitude} of signal separation (source: \\texttt{mvp\\_frac50\\_100}).",
          "+\\paragraph{Method-dependence.}",
          "+We compare signal trajectories between QLoRA (C1) and full fine-tuning (C4) under matched model size, dataset, and contamination fractions.",
          "+Paired differences in end-of-generation signal values quantify whether collapse signatures depend on the fine-tuning method or reflect properties of the data contamination itself."
        ]
      }
    ],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "c2ebd987-11a0-49ee-a14e-867e2fdb3c89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "leafUuid": "3885aad6-7d4d-4592-ba44-5e934f154602",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Rewrite Method section for collapse severity monitor paper",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262"
}
```

---

### Assistant

_source line 21 · 2026-05-15T21:55:06.282Z_

Rewrite complete. Key changes from the previous version:

- **Removed all "pending"/"in progress" language** — everything written definitively
- **Added §3.2 Contamination Fractions** as its own subsection
- **Added §3.4 with Table~\ref{tab:configs}** (C1--C5 configurations) and role descriptions
- **Stable rank**: kept the ↑ direction with energy dispersal framing, preserved the participation ratio footnote
- **Output signals**: added explicit training PPL vs evaluation PPL distinction, explaining why training PPL is misleading
- **Gradient norm**: retained QLoRA non-monotonicity explanation, made more concise
- **Added C4 (Full FT) and C5 (3B)** to the protocol description
- **Evaluation §3.5**: restructured into three clean paragraphs — cross-gen severity (Spearman ρ + bootstrap CI + Cohen's d), within-gen detection (clustered bootstrap ROC with causal dependence rationale), method-dependence (paired QLoRA vs Full FT)
- **Removed MVP-specific numbers** from the method section (those belong in results)
- Flattened subsubsections to paragraphs for compactness within the ~1100-word budget

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3885aad6-7d4d-4592-ba44-5e934f154602",
  "isSidechain": false,
  "requestId": "req_011Cb56idL28Vvz8ygiec2hK",
  "type": "assistant",
  "uuid": "121fbd08-828a-4414-8aca-99341ff98d7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQKpWmgxoDaGVxmq36hWAJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9163,
      "cache_read_input_tokens": 35267,
      "output_tokens": 304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 304,
          "cache_read_input_tokens": 35267,
          "cache_creation_input_tokens": 9163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9163
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

_source line 22_

```json
{
  "type": "last-prompt",
  "leafUuid": "121fbd08-828a-4414-8aca-99341ff98d7f",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Rewrite Method section for collapse severity monitor paper",
  "sessionId": "dd1c4acf-86f3-4cc6-966e-3016d5c01262"
}
```

---
