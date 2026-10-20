# Research conversation: <project_context> # 项目: distrib_canary_collapse ## 运行环境 - 服务器名: westd-19828 - SSH 账户: root（调用 ssh_execute / submit_train

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-3/05ec08f8-52e4-4210-a7ed-efa1f9d51d3f.jsonl`
- **Structured JSON:** [`c099a6b3255178caecd4.json`](../../sessions/c0/c099a6b3255178caecd4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T19:52:05.434Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T19:52:05.434Z",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "content": "&lt;project_context>\n# 项目: distrib_canary_collapse\n\n## 运行环境\n- 服务器名: westd-19828\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh westd-19828  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/distrib_canary_collapse\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: 论文禁止引用 Phase 2 单 seed 的 TY 跨 α 趋势——必须等 D026 multi-seed 数据确认 TY 非单调性是否可复现（原因：Reviewer Loop #7 发现 TY sig rate 跨 α 呈反直觉非单调模式（0%→62.5%→0%→59.4%），T=10 下 TY 自由度极低（df_resid≈6），单 seed 大概率是噪声。若论文引用此趋势，审稿人会攻击。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## 任务\n撰写论文 Related Work 章节（§2），输出到 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex`。\n\n## 写作规范\n写之前 **必须先 Read** 以下两个 skill：\n1. `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n2. `/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md`\n\n## 上下文文件（必须 Read）\n- references.bib: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib`（所有可引用的 key 都在这里）\n- introduction.tex: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex`（Introduction 的定位、已有引用，避免重复叙事）\n- literature_map.yaml: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml`（文献知识库，按 category 分类）\n\n## 章节结构（~900 words）\n\nRelated Work 分 4 个主题段落（用 \\paragraph{}），不用 subsection：\n\n### \\paragraph{Model collapse in iterative training.} (~250 words)\n- 基础理论：Shumailov et al. 2024 (curse of recursion, full-replacement paradigm), Alemohammad et al. 2024 (MAD, self-consuming generative models)\n- 理论分析：Dohmatob et al. 2024 (tail-cutting), Dohmatob et al. 2025 (strong collapse)\n- 数据混合/缓解：Dey et al. 2024 / Gerstgrasser et al. 2024 (accumulation prevents collapse, key=dey2024breaking), Kazdan et al. 2025 (synthetic data promises and perils), Fu et al. 2025 (self-consuming prevention theory)\n- 校准/多样性：Guo et al. 2024 (linguistic diversity decline), He et al. 2025 (golden ratio)\n- 简要提及 position/survey：Schaeffer et al. 2025 (model collapse semantics)\n\n### \\paragraph{Canary metrics and collapse monitoring.} (~250 words)\n- Du et al. 2026 (geometric regulation, 非正式观察 ECE 领先 accuracy — 最接近前辈)\n- Chen et al. 2025 (scales, ECE 先于 accuracy — 与 Du 类似但更系统)\n- SIGMA 2026 (spectral indicators for distributional shift)\n- Kalinowski 2026 (topological footprint-predictable collapse index)\n- DCES 2026 (center-edge sampling dynamics)\n- Gambetta 2024 (surplexity for mitigating collapse)\n- 明确指出：这些工作提出了各种监控指标但**方法论基础薄弱**——无差分检验、无多方法验证、无 FDR 校正\n- **与 Du et al. 的 4 点显式区分**：(1) 多指标家族系统对比；(2) 多方法交叉验证 + d_max sensitivity；(3) regime-dependent mapping；(4) 方法选择敏感性本身是主要贡献\n\n### \\paragraph{Early-warning signals and critical transitions.} (~200 words)\n- Scheffer et al. 2009 (Nature, early-warning signals for critical transitions — 理论基础)\n- Scheffer et al. 2012 (Science, anticipating critical transitions)\n- Boettiger & Hastings 2012 (detection limits of early warning — T 对 power 的影响)\n- 定位：生态/气候科学的 early-warning 框架是本工作的理论灵感，但 model collapse 文献尚未系统性引入这些方法论工具\n- Truong & Truong 2025 (entropy collapse as universal failure mode — 连接 entropy 与 collapse)\n\n### \\paragraph{Lead-lag methodology.} (~200 words)\n- Granger 1969 (原始 Granger causality 定义)\n- Shojaie & Fox 2022 (Granger causality review and recent advances)\n- 简述 Toda-Yamamoto approach 的来源\n- 定位：time-series econometrics 的方法论框架在 ML 中使用不足；model collapse 文献普遍使用 naive correlation 而非 formal causal tests\n\n## 关键约束\n- PC14: 不用 \"consistently outperforms\" / \"state-of-the-art\" / 无检验的 \"significantly\"\n- 不重复 Introduction 已说的内容（Introduction 已提到 Du et al. gap、Scheffer motivation、4 个方法论缺陷）\n- Related Work 是定位和对比，不做 claim\n- 避免过度列举——每篇论文一句话定位即可，重点是与本文的关系\n\n## 引用\n只用 references.bib 中已有的 key。Read references.bib 确认所有 key 拼写正确。\n\n主要 key（按 paragraph）：\n- Collapse: shumailov2024curse, alemohammad2024mad, dohmatob2024tale, dohmatob2025strong, dey2024breaking, kazdan2025collapse, fu2025selfconsuming, guo2024linguistic, he2025golden, schaeffer2025position\n- Canary: du2026geometric, chen2025scales, sigma2026spectral, kalinowski2026topology, dces2026counter, gambetta2024surplexity\n- EWS: scheffer2009early, scheffer2012anticipating, boettiger2012limits, truong2025entropy\n- Methodology: granger1969investigating, shojaie2022granger\n\n也可能用到但不必须：seddik2024howbad, briesch2024selfconsuming, wang2026contaminated, bakshi2026improvement, barzilai2025consistency, feng2025escaping, noci2024mind, jing2022understanding, marcinkevics2022neural, wright2025epistemic\n\n## 输出\n- 写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex`\n- `\\section{Related Work}` + `\\label{sec:related_work}`\n- 4 个 `\\paragraph{}`\n- ~900 words\n\n## 验证\n写完后：\n1. \\label{sec:related_work} 存在\n2. 所有 \\cite{} key 在 references.bib 中\n3. 与 Du et al. 的 4 点区分明确\n4. 无结果 claim、无强度词违规\n5. 引用数在 citation_budget (40-45) 范围内（仅计此章节贡献的新引用）\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T19:52:05.437Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T19:52:05.437Z",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f"
}
```

---

## Round 1

36 recorded events

### User

_source line 3 · 2026-05-15T19:52:05.467Z_

&lt;project_context>
# 项目: distrib_canary_collapse

## 运行环境
- 服务器名: westd-19828
- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account="root"）
- SSH 连接命令: ssh westd-19828  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP
- 项目代码根目录: /root/autodl-tmp/distrib_canary_collapse

## ⚠️ 活跃约束（必须遵守）

- **C001**: 论文禁止引用 Phase 2 单 seed 的 TY 跨 α 趋势——必须等 D026 multi-seed 数据确认 TY 非单调性是否可复现（原因：Reviewer Loop #7 发现 TY sig rate 跨 α 呈反直觉非单调模式（0%→62.5%→0%→59.4%），T=10 下 TY 自由度极低（df_resid≈6），单 seed 大概率是噪声。若论文引用此趋势，审稿人会攻击。）


## 环境搭建
连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。

## 输出风格
回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。
&lt;/project_context>
## 任务
撰写论文 Related Work 章节（§2），输出到 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex`。

## 写作规范
写之前 **必须先 Read** 以下两个 skill：
1. `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`
2. `/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md`

## 上下文文件（必须 Read）
- references.bib: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib`（所有可引用的 key 都在这里）
- introduction.tex: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex`（Introduction 的定位、已有引用，避免重复叙事）
- literature_map.yaml: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml`（文献知识库，按 category 分类）

## 章节结构（~900 words）

Related Work 分 4 个主题段落（用 \paragraph{}），不用 subsection：

### \paragraph{Model collapse in iterative training.} (~250 words)
- 基础理论：Shumailov et al. 2024 (curse of recursion, full-replacement paradigm), Alemohammad et al. 2024 (MAD, self-consuming generative models)
- 理论分析：Dohmatob et al. 2024 (tail-cutting), Dohmatob et al. 2025 (strong collapse)
- 数据混合/缓解：Dey et al. 2024 / Gerstgrasser et al. 2024 (accumulation prevents collapse, key=dey2024breaking), Kazdan et al. 2025 (synthetic data promises and perils), Fu et al. 2025 (self-consuming prevention theory)
- 校准/多样性：Guo et al. 2024 (linguistic diversity decline), He et al. 2025 (golden ratio)
- 简要提及 position/survey：Schaeffer et al. 2025 (model collapse semantics)

### \paragraph{Canary metrics and collapse monitoring.} (~250 words)
- Du et al. 2026 (geometric regulation, 非正式观察 ECE 领先 accuracy — 最接近前辈)
- Chen et al. 2025 (scales, ECE 先于 accuracy — 与 Du 类似但更系统)
- SIGMA 2026 (spectral indicators for distributional shift)
- Kalinowski 2026 (topological footprint-predictable collapse index)
- DCES 2026 (center-edge sampling dynamics)
- Gambetta 2024 (surplexity for mitigating collapse)
- 明确指出：这些工作提出了各种监控指标但**方法论基础薄弱**——无差分检验、无多方法验证、无 FDR 校正
- **与 Du et al. 的 4 点显式区分**：(1) 多指标家族系统对比；(2) 多方法交叉验证 + d_max sensitivity；(3) regime-dependent mapping；(4) 方法选择敏感性本身是主要贡献

### \paragraph{Early-warning signals and critical transitions.} (~200 words)
- Scheffer et al. 2009 (Nature, early-warning signals for critical transitions — 理论基础)
- Scheffer et al. 2012 (Science, anticipating critical transitions)
- Boettiger & Hastings 2012 (detection limits of early warning — T 对 power 的影响)
- 定位：生态/气候科学的 early-warning 框架是本工作的理论灵感，但 model collapse 文献尚未系统性引入这些方法论工具
- Truong & Truong 2025 (entropy collapse as universal failure mode — 连接 entropy 与 collapse)

### \paragraph{Lead-lag methodology.} (~200 words)
- Granger 1969 (原始 Granger causality 定义)
- Shojaie & Fox 2022 (Granger causality review and recent advances)
- 简述 Toda-Yamamoto approach 的来源
- 定位：time-series econometrics 的方法论框架在 ML 中使用不足；model collapse 文献普遍使用 naive correlation 而非 formal causal tests

## 关键约束
- PC14: 不用 "consistently outperforms" / "state-of-the-art" / 无检验的 "significantly"
- 不重复 Introduction 已说的内容（Introduction 已提到 Du et al. gap、Scheffer motivation、4 个方法论缺陷）
- Related Work 是定位和对比，不做 claim
- 避免过度列举——每篇论文一句话定位即可，重点是与本文的关系

## 引用
只用 references.bib 中已有的 key。Read references.bib 确认所有 key 拼写正确。

主要 key（按 paragraph）：
- Collapse: shumailov2024curse, alemohammad2024mad, dohmatob2024tale, dohmatob2025strong, dey2024breaking, kazdan2025collapse, fu2025selfconsuming, guo2024linguistic, he2025golden, schaeffer2025position
- Canary: du2026geometric, chen2025scales, sigma2026spectral, kalinowski2026topology, dces2026counter, gambetta2024surplexity
- EWS: scheffer2009early, scheffer2012anticipating, boettiger2012limits, truong2025entropy
- Methodology: granger1969investigating, shojaie2022granger

也可能用到但不必须：seddik2024howbad, briesch2024selfconsuming, wang2026contaminated, bakshi2026improvement, barzilai2025consistency, feng2025escaping, noci2024mind, jing2022understanding, marcinkevics2022neural, wright2025epistemic

## 输出
- 写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex`
- `\section{Related Work}` + `\label{sec:related_work}`
- 4 个 `\paragraph{}`
- ~900 words

## 验证
写完后：
1. \label{sec:related_work} 存在
2. 所有 \cite{} key 在 references.bib 中
3. 与 Du et al. 的 4 点区分明确
4. 无结果 claim、无强度词违规
5. 引用数在 citation_budget (40-45) 范围内（仅计此章节贡献的新引用）


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "bc9d0e00-4871-4d43-b046-0cec4ce72249",
  "type": "user",
  "uuid": "4d9e0e16-5ba8-471a-a8a2-4f9530a4e089",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T19:52:05.467Z_

```json
{
  "parentUuid": "4d9e0e16-5ba8-471a-a8a2-4f9530a4e089",
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
  "uuid": "8f6beb72-01a5-4f21-beec-a35bd61a1a64",
  "timestamp": "2026-05-15T19:52:05.467Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T19:52:05.467Z_

```json
{
  "parentUuid": "8f6beb72-01a5-4f21-beec-a35bd61a1a64",
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
  "uuid": "0bbfc0f4-1b50-4643-9048-5d400edfa6e4",
  "timestamp": "2026-05-15T19:52:05.467Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T19:52:05.467Z_

```json
{
  "parentUuid": "0bbfc0f4-1b50-4643-9048-5d400edfa6e4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e330d527-1cc2-4e94-949f-a9e0c88bdda4",
  "timestamp": "2026-05-15T19:52:05.467Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
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
  "aiTitle": "Write Related Work section for paper",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f"
}
```

---

### Assistant

_source line 8 · 2026-05-15T19:52:08.739Z_

I'll start by reading the required skills and context files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e330d527-1cc2-4e94-949f-a9e0c88bdda4",
  "isSidechain": false,
  "requestId": "req_011Cb4wMJeEyJ8DZVT5x3j6W",
  "type": "assistant",
  "uuid": "eb02215d-68f7-4f91-b4ef-1f02470ea651",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DK3LTJPt3oa8L1zKw8x5XW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13261,
      "cache_read_input_tokens": 11841,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 360,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13261
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

_source line 9 · 2026-05-15T19:52:09.241Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TPoNskBf6e4cMvGXVaK75W`</summary>

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
  "parentUuid": "eb02215d-68f7-4f91-b4ef-1f02470ea651",
  "isSidechain": false,
  "requestId": "req_011Cb4wMJeEyJ8DZVT5x3j6W",
  "type": "assistant",
  "uuid": "7671e705-188a-4001-b380-bb2f86d2ec27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DK3LTJPt3oa8L1zKw8x5XW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13261,
      "cache_read_input_tokens": 11841,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 360,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13261
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

_source line 10 · 2026-05-15T19:52:09.256Z_

<details><summary>↩ Tool result · `toolu_01TPoNskBf6e4cMvGXVaK75W`</summary>

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
  "parentUuid": "7671e705-188a-4001-b380-bb2f86d2ec27",
  "isSidechain": false,
  "promptId": "bc9d0e00-4871-4d43-b046-0cec4ce72249",
  "type": "user",
  "uuid": "0ce03840-089f-4322-a6ba-b6751ee83354",
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
  "sourceToolAssistantUUID": "7671e705-188a-4001-b380-bb2f86d2ec27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool call

_source line 11 · 2026-05-15T19:52:09.688Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W1GPuguygVqhC7C9pFWz6Q`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ce03840-089f-4322-a6ba-b6751ee83354",
  "isSidechain": false,
  "requestId": "req_011Cb4wMJeEyJ8DZVT5x3j6W",
  "type": "assistant",
  "uuid": "77c9bb9f-beaf-49ea-88c4-3532c2ff5ecc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DK3LTJPt3oa8L1zKw8x5XW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13261,
      "cache_read_input_tokens": 11841,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 360,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13261
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

_source line 12 · 2026-05-15T19:52:09.693Z_

<details><summary>↩ Tool result · `toolu_01W1GPuguygVqhC7C9pFWz6Q`</summary>

```text
1	---
2	name: red-section
3	description: "当实验结论为 negative / 审稿人指出 core claim 不成立 / 你要写或修改任何 paper/**/*.md 或 .tex 文件时,立即使用本 skill。提供 Framing 调整提案模板、写作规范、审稿攻击面预演。违反即被 Reviewer critical 打回。"
4	always: true
5	roles:
6	  - agent
7	---
8	
9	# Red Section — Narrative Re-framing
10	
11	## 什么时候用
12	- 实验 conclusion = negative
13	- 审稿人指出 core claim 不成立
14	- 写论文前（作为通用写作规范）
15	
16	## Negative 结果的正确心态
17	"不是失败，是发现了 X"。你的输出应该是 framing 调整提案，而不是 failure report。
18	
19	## 产出格式
20	
21	### Framing 调整提案模板
22	1. 原 claim：什么
23	2. 实验结果：什么（客观数字，不加修饰）
24	3. 重新审视：
25	   - 这个结果挑战了哪个 hypothesis？
26	   - 是否暴露了被忽略的变量？
27	   - 在新的 framing 下，哪些已做实验依然有效？哪些要补？
28	4. 新的 narrative 骨架（3 种备选，供 Director 选）
29	5. 对论文各章节的影响（abstract / intro / method / experiments / discussion / conclusion 逐一评估）
30	6. 建议下一步实验（必须至少 3 组备选，填新 framing 下的矩阵空格）
31	
32	### 写作规范（所有写作场景通用）
33	- 禁止 cherry-picking
34	- 所有数字必须追溯到 registry
35	- 强度与 evidence 匹配（1 个数据集 → 不能说 "consistently"）
36	- 每个定量 claim 必须附 exp_id
37	- 限制强度词（"significantly" 必须有统计检验）
38	
39	### 审稿攻击面预演
40	- 这个 section 最容易被审稿人攻击的点
41	- 预写 rebuttal 要点
42	
43	## 输出给谁
44	- Framing 调整提案 → Main Agent 向 Director 汇报
45	- 写作 skill 合规检查 → Reviewer 审查时验证
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "77c9bb9f-beaf-49ea-88c4-3532c2ff5ecc",
  "isSidechain": false,
  "promptId": "bc9d0e00-4871-4d43-b046-0cec4ce72249",
  "type": "user",
  "uuid": "6999b4da-095c-486b-ac43-fda7d9488208",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md",
      "content": "---\nname: red-section\ndescription: \"当实验结论为 negative / 审稿人指出 core claim 不成立 / 你要写或修改任何 paper/**/*.md 或 .tex 文件时,立即使用本 skill。提供 Framing 调整提案模板、写作规范、审稿攻击面预演。违反即被 Reviewer critical 打回。\"\nalways: true\nroles:\n  - agent\n---\n\n# Red Section — Narrative Re-framing\n\n## 什么时候用\n- 实验 conclusion = negative\n- 审稿人指出 core claim 不成立\n- 写论文前（作为通用写作规范）\n\n## Negative 结果的正确心态\n\"不是失败，是发现了 X\"。你的输出应该是 framing 调整提案，而不是 failure report。\n\n## 产出格式\n\n### Framing 调整提案模板\n1. 原 claim：什么\n2. 实验结果：什么（客观数字，不加修饰）\n3. 重新审视：\n   - 这个结果挑战了哪个 hypothesis？\n   - 是否暴露了被忽略的变量？\n   - 在新的 framing 下，哪些已做实验依然有效？哪些要补？\n4. 新的 narrative 骨架（3 种备选，供 Director 选）\n5. 对论文各章节的影响（abstract / intro / method / experiments / discussion / conclusion 逐一评估）\n6. 建议下一步实验（必须至少 3 组备选，填新 framing 下的矩阵空格）\n\n### 写作规范（所有写作场景通用）\n- 禁止 cherry-picking\n- 所有数字必须追溯到 registry\n- 强度与 evidence 匹配（1 个数据集 → 不能说 \"consistently\"）\n- 每个定量 claim 必须附 exp_id\n- 限制强度词（\"significantly\" 必须有统计检验）\n\n### 审稿攻击面预演\n- 这个 section 最容易被审稿人攻击的点\n- 预写 rebuttal 要点\n\n## 输出给谁\n- Framing 调整提案 → Main Agent 向 Director 汇报\n- 写作 skill 合规检查 → Reviewer 审查时验证\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  },
  "sourceToolAssistantUUID": "77c9bb9f-beaf-49ea-88c4-3532c2ff5ecc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T19:52:10.160Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PJyBYCBJndBoDj41CdqRoy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6999b4da-095c-486b-ac43-fda7d9488208",
  "isSidechain": false,
  "requestId": "req_011Cb4wMJeEyJ8DZVT5x3j6W",
  "type": "assistant",
  "uuid": "c9da175d-a243-4b89-aa5c-21e2bbcf6a10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DK3LTJPt3oa8L1zKw8x5XW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13261,
      "cache_read_input_tokens": 11841,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 360,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13261
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

_source line 14 · 2026-05-15T19:52:10.164Z_

<details><summary>↩ Tool result · `toolu_01PJyBYCBJndBoDj41CdqRoy`</summary>

```text
1	% ============================================================
2	% CORE MODEL COLLAPSE
3	% ============================================================
4	
5	@article{shumailov2024curse,
6	  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},
7	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},
8	  journal   = {Nature},
9	  year      = {2024},
10	  url       = {https://arxiv.org/abs/2305.17493},
11	}
12	
13	@inproceedings{alemohammad2024mad,
14	  title     = {Self-Consuming Generative Models Go {MAD}},
15	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard},
16	  booktitle = {International Conference on Learning Representations},
17	  year      = {2024},
18	  url       = {https://arxiv.org/abs/2307.01850},
19	}
20	
21	@inproceedings{dohmatob2024tale,
22	  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},
23	  author    = {Dohmatob, Elvis and Feng, Yunzhen and others},
24	  booktitle = {International Conference on Machine Learning},
25	  year      = {2024},
26	  url       = {https://arxiv.org/abs/2402.07043},
27	}
28	
29	@inproceedings{dohmatob2025strong,
30	  title     = {Strong Model Collapse},
31	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
32	  booktitle = {International Conference on Learning Representations},
33	  year      = {2025},
34	  url       = {https://arxiv.org/abs/2410.04840},
35	}
36	
37	@inproceedings{guo2024linguistic,
38	  title     = {The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},
39	  author    = {Guo, Yanzhu and Shang, Guokan and others},
40	  booktitle = {Findings of the Association for Computational Linguistics: {NAACL}},
41	  year      = {2024},
42	  url       = {https://arxiv.org/abs/2311.09807},
43	}
44	
45	@article{briesch2024selfconsuming,
46	  title     = {Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop},
47	  author    = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},
48	  journal   = {arXiv preprint arXiv:2311.16822},
49	  year      = {2024},
50	  url       = {https://arxiv.org/abs/2311.16822},
51	}
52	
53	@article{truong2025entropy,
54	  title     = {Entropy Collapse: A Universal Failure Mode of Intelligent Systems},
55	  author    = {Truong, Xuan Khanh and Truong, Quynh Hoa},
56	  journal   = {arXiv preprint arXiv:2512.12381},
57	  year      = {2025},
58	  url       = {https://arxiv.org/abs/2512.12381},
59	}
60	
61	@article{wang2026contaminated,
62	  title     = {Can Generative Artificial Intelligence Survive Data Contamination? {T}heoretical Guarantees under Contaminated Recursive Training},
63	  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},
64	  journal   = {arXiv preprint arXiv:2602.16065},
65	  year      = {2026},
66	  url       = {https://arxiv.org/abs/2602.16065},
67	}
68	
69	@article{du2026geometric,
70	  title     = {Escaping Mode Collapse in {LLM} Generation via Geometric Regulation},
71	  author    = {Du, Xin and Tanaka-Ishii, Kumiko},
72	  journal   = {arXiv preprint arXiv:2605.00435},
73	  year      = {2026},
74	  url       = {https://arxiv.org/abs/2605.00435},
75	}
76	
77	@article{gauthier2026alignment,
78	  title     = {Explaining and Preventing Alignment Collapse in Iterative {RLHF}},
79	  author    = {Gauthier, Etienne and Bach, Francis and Jordan, Michael I.},
80	  journal   = {arXiv preprint arXiv:2605.04266},
81	  year      = {2026},
82	  url       = {https://arxiv.org/abs/2605.04266},
83	}
84	
85	@article{shi2026pruning,
86	  title     = {Understanding Performance Collapse in Layer-Pruned {LLMs} via Decision Representation Transitions},
87	  author    = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},
88	  journal   = {arXiv preprint arXiv:2605.07271},
89	  year      = {2026},
90	  url       = {https://arxiv.org/abs/2605.07271},
91	}
92	
93	@article{tubingen2026diffusion,
94	  title     = {Layer Collapse in Diffusion Language Models},
95	  author    = {Conzelmann, Alexander and Catalan-Tatjer, Albert and Liu, Shiwei},
96	  journal   = {arXiv preprint arXiv:2605.06366},
97	  year      = {2026},
98	  url       = {https://arxiv.org/abs/2605.06366},
99	}
100	
101	% ============================================================
102	% CANARY / EARLY WARNING METRICS
103	% ============================================================
104	
105	@article{chen2025scales,
106	  title     = {Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios},
107	  author    = {Du, Y. and Wu, G. and Tang, G. and Wang, W. and Fan, Q.},
108	  journal   = {arXiv preprint arXiv:2510.05133},
109	  year      = {2025},
110	  url       = {https://arxiv.org/abs/2510.05133},
111	}
112	
113	@article{gambetta2024surplexity,
114	  title     = {Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},
115	  author    = {Gambetta, Daniele and others},
116	  journal   = {arXiv preprint arXiv:2410.12341},
117	  year      = {2024},
118	  url       = {https://arxiv.org/abs/2410.12341},
119	}
120	
121	@article{qiu2025spectral,
122	  title     = {Spectral Alignment as Predictor of Loss Explosion in Neural Network Training},
123	  author    = {Qiu, Haiquan and Wu, You and Tan, Yingjie and Wang, Yaqing and Yao, Quanming},
124	  journal   = {arXiv preprint arXiv:2510.04202},
125	  year      = {2025},
126	  url       = {https://arxiv.org/abs/2510.04202},
127	}
128	
129	@inproceedings{he2025closer,
130	  title     = {A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},
131	  author    = {He, Shiliang and others},
132	  booktitle = {Advances in Neural Information Processing Systems},
133	  year      = {2025},
134	  url       = {https://arxiv.org/abs/2509.16499},
135	}
136	
137	@inproceedings{ba2024fill,
138	  title     = {Fill In The Gaps: Model Calibration and Generalization with Synthetic Data},
139	  author    = {Ba, Yang and Mancenido, Michelle V and Pan, Rong},
140	  booktitle = {Conference on Empirical Methods in Natural Language Processing},
141	  year      = {2024},
142	  url       = {https://arxiv.org/abs/2410.10864},
143	}
144	
145	@article{sigma2026spectral,
146	  title     = {{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},
147	  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},
148	  journal   = {arXiv preprint arXiv:2601.03385},
149	  year      = {2026},
150	  url       = {https://arxiv.org/abs/2601.03385},
151	}
152	
153	@article{kalinowski2026topology,
154	  title     = {Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index},
155	  author    = {Kalinowski, Alexander},
156	  journal   = {arXiv preprint arXiv:2604.26984},
157	  year      = {2026},
158	  url       = {https://arxiv.org/abs/2604.26984},
159	}
160	
161	@article{bergsma2026scaling,
162	  title     = {Scaling with Collapse: Efficient and Predictable Training of {LLM} Families},
163	  author    = {Bergsma, Shane and Zhang, Bin Claire and Dey, Nolan and Muhammad, Shaheer and Gosal, Gurpreet and Hestness, Joel},
164	  journal   = {arXiv preprint arXiv:2509.25087},
165	  year      = {2026},
166	  url       = {https://arxiv.org/abs/2509.25087},
167	}
168	
169	% ============================================================
170	% DIVERSITY METRICS (BACKGROUND)
171	% ============================================================
172	
173	@inproceedings{zhu2018texygen,
174	  title     = {{Texygen}: A Benchmarking Platform for Text Generation Models},
175	  author    = {Zhu, Yaoming and others},
176	  booktitle = {International {ACM} {SIGIR} Conference on Research and Development in Information Retrieval},
177	  year      = {2018},
178	  url       = {https://arxiv.org/abs/1802.01886},
179	}
180	
181	@inproceedings{li2016diversity,
182	  title     = {A Diversity-Promoting Objective Function for Neural Conversation Models},
183	  author    = {Li, Jiwei and others},
184	  booktitle = {North American Chapter of the Association for Computational Linguistics},
185	  year      = {2016},
186	  url       = {https://arxiv.org/abs/1510.03055},
187	}
188	
189	% ============================================================
190	% REPRESENTATION / SPECTRAL COLLAPSE
191	% ============================================================
192	
193	@inproceedings{jing2022understanding,
194	  title     = {Understanding Dimensional Collapse in Contrastive Self-supervised Learning},
195	  author    = {Jing, Li and others},
196	  booktitle = {International Conference on Learning Representations},
197	  year      = {2022},
198	  url       = {https://openreview.net/forum?id=YevsQ05DEN7},
199	}
200	
201	@inproceedings{noci2024mind,
202	  title     = {Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers},
203	  author    = {Noci, Lorenzo and others},
204	  booktitle = {Advances in Neural Information Processing Systems},
205	  year      = {2024},
206	  url       = {https://arxiv.org/abs/2410.07799},
207	}
208	
209	% ============================================================
210	% DATA MIXING & ACCUMULATION
211	% ============================================================
212	
213	@inproceedings{kazdan2025collapse,
214	  title     = {Collapse or Thrive? {P}erils and Promises of Synthetic Data in a Self-Generating World},
215	  author    = {Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi},
216	  booktitle = {International Conference on Machine Learning},
217	  year      = {2025},
218	  url       = {https://arxiv.org/abs/2410.16713},
219	}
220	
221	@inproceedings{dey2024breaking,
222	  title     = {Is Model Collapse Inevitable? {B}reaking the Curse of Recursion by Accumulating Real and Synthetic Data},
223	  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
224	  booktitle = {International Conference on Machine Learning},
225	  year      = {2024},
226	  url       = {https://arxiv.org/abs/2404.01413},
227	}
228	
229	@article{seddik2024howbad,
230	  title     = {How Bad is Training on Synthetic Data? {A} Statistical Analysis of Language Model Collapse},
231	  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},
232	  journal   = {arXiv preprint arXiv:2404.05090},
233	  year      = {2024},
234	  url       = {https://arxiv.org/abs/2404.05090},
235	}
236	
237	@inproceedings{fu2025selfconsuming,
238	  title     = {A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops},
239	  author    = {Fu, Shi and Wang, Yingjie and Chen, Yuzhu and Tian, Xinmei and Tao, Dacheng},
240	  booktitle = {International Conference on Learning Representations},
241	  year      = {2025},
242	  url       = {https://arxiv.org/abs/2502.18865},
243	}
244	
245	@article{bakshi2026improvement,
246	  title     = {From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources},
247	  author    = {Bakshi, Soham and Chakraborty, Sunrit},
248	  journal   = {arXiv preprint arXiv:2602.10531},
249	  year      = {2026},
250	  url       = {https://arxiv.org/abs/2602.10531},
251	}
252	
253	@article{he2025golden,
254	  title     = {Golden Ratio Weighting Prevents Model Collapse},
255	  author    = {He, Shiliang and Xu, Zhongbin and Cheng, Yan},
256	  journal   = {arXiv preprint arXiv:2502.18049},
257	  year      = {2025},
258	  url       = {https://arxiv.org/abs/2502.18049},
259	}
260	
261	@article{xu2025mixing,
262	  title     = {Preventing Model Collapse Under Overparametrization: Optimal Mixing Ratios},
263	  author    = {Xu, Zhongbin and Cheng, Yan},
264	  journal   = {arXiv preprint arXiv:2509.22341},
265	  year      = {2025},
266	  url       = {https://arxiv.org/abs/2509.22341},
267	}
268	
269	% ============================================================
270	% MITIGATION & VERIFICATION
271	% ============================================================
272	
273	@inproceedings{feng2025escaping,
274	  title     = {Escaping Model Collapse via Synthetic Data Verification},
275	  author    = {Feng, Yunzhen and others},
276	  booktitle = {Advances in Neural Information Processing Systems},
277	  year      = {2025},
278	  url       = {https://arxiv.org/abs/2510.16657},
279	}
280	
281	@inproceedings{barzilai2025consistency,
282	  title     = {When Models Don't Collapse: On the Consistency of Iterative {MLE}},
283	  author    = {Barzilai, Daniel and Shamir, Ohad},
284	  booktitle = {International Conference on Machine Learning},
285	  year      = {2025},
286	  url       = {https://arxiv.org/abs/2505.19046},
287	}
288	
289	@article{dces2026counter,
290	  title     = {Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling},
291	  author    = {Zhu, Bingze and Xie, Yubo},
292	  journal   = {Electronics},
293	  year      = {2026},
294	  url       = {https://www.mdpi.com/2079-9292/15/4/869},
295	}
296	
297	% ============================================================
298	% POSITION / SURVEY / EPISTEMICS
299	% ============================================================
300	
301	@article{schaeffer2025position,
302	  title     = {Position: Model Collapse Does Not Mean What You Think},
303	  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},
304	  journal   = {arXiv preprint arXiv:2503.03150},
305	  year      = {2025},
306	  url       = {https://arxiv.org/abs/2503.03150},
307	}
308	
309	@article{wright2025epistemic,
310	  title     = {Epistemic Diversity and Knowledge Collapse in Large Language Models},
311	  author    = {Wright, Dustin and Masud, Sarah and Moore, Jared and Yadav, Srishti and Antoniak, Maria and Park, Chan Young and Augenstein, Isabelle},
312	  journal   = {arXiv preprint arXiv:2510.04226},
313	  year      = {2025},
314	  url       = {https://arxiv.org/abs/2510.04226},
315	}
316	
317	% ============================================================
318	% METHODOLOGY (GRANGER / LEAD-LAG)
319	% ============================================================
320	
321	@article{granger1969investigating,
322	  author    = {Granger, Clive W. J.},
323	  title     = {Investigating Causal Relations by Econometric Models and Cross-spectral Methods},
324	  journal   = {Econometrica},
325	  volume    = {37},
326	  number    = {3},
327	  pages     = {424--438},
328	  year      = {1969},
329	  publisher = {Wiley},
330	}
331	
332	@article{shojaie2022granger,
333	  title     = {{Granger} Causality: A Review and Recent Advances},
334	  author    = {Shojaie, Ali and Fox, Emily B.},
335	  journal   = {Annual Review of Statistics and Its Application},
336	  year      = {2022},
337	  url       = {https://arxiv.org/abs/2105.02675},
338	}
339	
340	@article{marcinkevics2022neural,
341	  title     = {{Granger} Causality Using Neural Networks},
342	  author    = {Marcinkevics, Raphael and Vogt, Julia},
343	  journal   = {arXiv preprint arXiv:2208.03703},
344	  year      = {2022},
345	  url       = {https://arxiv.org/abs/2208.03703},
346	}
347	
348	% ============================================================
349	% EARLY WARNING SIGNALS / TIPPING POINTS (ECOLOGICAL THEORY)
350	% ============================================================
351	
352	@article{scheffer2009early,
353	  title     = {Early-warning signals for critical transitions},
354	  author    = {Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George},
355	  journal   = {Nature},
356	  year      = {2009},
357	  doi       = {10.1038/nature08227},
358	}
359	
360	@article{scheffer2012anticipating,
361	  title     = {Anticipating Critical Transitions},
362	  author    = {Scheffer, Marten and Carpenter, Stephen R. and Lenton, Timothy M. and Bascompte, Jordi and Brock, William and Dakos, Vasilis and van de Koppel, Johan and van de Leemput, Ingrid A. and Levin, Simon A. and van Nes, Egbert H. and Pascual, Mercedes and Vandermeer, John},
363	  journal   = {Science},
364	  year      = {2012},
365	  doi       = {10.1126/science.1225244},
366	}
367	
368	@article{boettiger2012limits,
369	  title     = {Quantifying Limits to Detection of Early Warning for Critical Transitions},
370	  author    = {Boettiger, Carl and Hastings, Alan},
371	  journal   = {Journal of the Royal Society Interface},
372	  year      = {2012},
373	  doi       = {10.1098/rsif.2012.0125},
374	}
375	
376	% ============================================================
377	% MODELS
378	% ============================================================
379	
380	@inproceedings{biderman2023pythia,
381	  title     = {Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling},
382	  author    = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purber, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar},
383	  booktitle = {International Conference on Machine Learning},
384	  year      = {2023},
385	  url       = {https://arxiv.org/abs/2304.01373},
386	}
387	
388	% ============================================================
389	% DATASETS
390	% ============================================================
391	
392	@inproceedings{merity2017pointer,
393	  title     = {Pointer Sentinel Mixture Models},
394	  author    = {Merity, Stephen and Xiong, Caiming and Bradbury, James and Socher, Richard},
395	  booktitle = {International Conference on Learning Representations},
396	  year      = {2017},
397	  url       = {https://arxiv.org/abs/1609.07843},
398	}
399	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9da175d-a243-4b89-aa5c-21e2bbcf6a10",
  "isSidechain": false,
  "promptId": "bc9d0e00-4871-4d43-b046-0cec4ce72249",
  "type": "user",
  "uuid": "a359c427-1a15-4d0b-badf-3e827b8b74de",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib",
      "content": "% ============================================================\n% CORE MODEL COLLAPSE\n% ============================================================\n\n@article{shumailov2024curse,\n  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},\n  journal   = {Nature},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2305.17493},\n}\n\n@inproceedings{alemohammad2024mad,\n  title     = {Self-Consuming Generative Models Go {MAD}},\n  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2307.01850},\n}\n\n@inproceedings{dohmatob2024tale,\n  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and others},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.07043},\n}\n\n@inproceedings{dohmatob2025strong,\n  title     = {Strong Model Collapse},\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2410.04840},\n}\n\n@inproceedings{guo2024linguistic,\n  title     = {The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},\n  author    = {Guo, Yanzhu and Shang, Guokan and others},\n  booktitle = {Findings of the Association for Computational Linguistics: {NAACL}},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2311.09807},\n}\n\n@article{briesch2024selfconsuming,\n  title     = {Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop},\n  author    = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},\n  journal   = {arXiv preprint arXiv:2311.16822},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2311.16822},\n}\n\n@article{truong2025entropy,\n  title     = {Entropy Collapse: A Universal Failure Mode of Intelligent Systems},\n  author    = {Truong, Xuan Khanh and Truong, Quynh Hoa},\n  journal   = {arXiv preprint arXiv:2512.12381},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2512.12381},\n}\n\n@article{wang2026contaminated,\n  title     = {Can Generative Artificial Intelligence Survive Data Contamination? {T}heoretical Guarantees under Contaminated Recursive Training},\n  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},\n  journal   = {arXiv preprint arXiv:2602.16065},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2602.16065},\n}\n\n@article{du2026geometric,\n  title     = {Escaping Mode Collapse in {LLM} Generation via Geometric Regulation},\n  author    = {Du, Xin and Tanaka-Ishii, Kumiko},\n  journal   = {arXiv preprint arXiv:2605.00435},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2605.00435},\n}\n\n@article{gauthier2026alignment,\n  title     = {Explaining and Preventing Alignment Collapse in Iterative {RLHF}},\n  author    = {Gauthier, Etienne and Bach, Francis and Jordan, Michael I.},\n  journal   = {arXiv preprint arXiv:2605.04266},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2605.04266},\n}\n\n@article{shi2026pruning,\n  title     = {Understanding Performance Collapse in Layer-Pruned {LLMs} via Decision Representation Transitions},\n  author    = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},\n  journal   = {arXiv preprint arXiv:2605.07271},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2605.07271},\n}\n\n@article{tubingen2026diffusion,\n  title     = {Layer Collapse in Diffusion Language Models},\n  author    = {Conzelmann, Alexander and Catalan-Tatjer, Albert and Liu, Shiwei},\n  journal   = {arXiv preprint arXiv:2605.06366},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2605.06366},\n}\n\n% ============================================================\n% CANARY / EARLY WARNING METRICS\n% ============================================================\n\n@article{chen2025scales,\n  title     = {Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios},\n  author    = {Du, Y. and Wu, G. and Tang, G. and Wang, W. and Fan, Q.},\n  journal   = {arXiv preprint arXiv:2510.05133},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2510.05133},\n}\n\n@article{gambetta2024surplexity,\n  title     = {Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},\n  author    = {Gambetta, Daniele and others},\n  journal   = {arXiv preprint arXiv:2410.12341},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2410.12341},\n}\n\n@article{qiu2025spectral,\n  title     = {Spectral Alignment as Predictor of Loss Explosion in Neural Network Training},\n  author    = {Qiu, Haiquan and Wu, You and Tan, Yingjie and Wang, Yaqing and Yao, Quanming},\n  journal   = {arXiv preprint arXiv:2510.04202},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2510.04202},\n}\n\n@inproceedings{he2025closer,\n  title     = {A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},\n  author    = {He, Shiliang and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2509.16499},\n}\n\n@inproceedings{ba2024fill,\n  title     = {Fill In The Gaps: Model Calibration and Generalization with Synthetic Data},\n  author    = {Ba, Yang and Mancenido, Michelle V and Pan, Rong},\n  booktitle = {Conference on Empirical Methods in Natural Language Processing},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2410.10864},\n}\n\n@article{sigma2026spectral,\n  title     = {{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},\n  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  journal   = {arXiv preprint arXiv:2601.03385},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2601.03385},\n}\n\n@article{kalinowski2026topology,\n  title     = {Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index},\n  author    = {Kalinowski, Alexander},\n  journal   = {arXiv preprint arXiv:2604.26984},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2604.26984},\n}\n\n@article{bergsma2026scaling,\n  title     = {Scaling with Collapse: Efficient and Predictable Training of {LLM} Families},\n  author    = {Bergsma, Shane and Zhang, Bin Claire and Dey, Nolan and Muhammad, Shaheer and Gosal, Gurpreet and Hestness, Joel},\n  journal   = {arXiv preprint arXiv:2509.25087},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2509.25087},\n}\n\n% ============================================================\n% DIVERSITY METRICS (BACKGROUND)\n% ============================================================\n\n@inproceedings{zhu2018texygen,\n  title     = {{Texygen}: A Benchmarking Platform for Text Generation Models},\n  author    = {Zhu, Yaoming and others},\n  booktitle = {International {ACM} {SIGIR} Conference on Research and Development in Information Retrieval},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1802.01886},\n}\n\n@inproceedings{li2016diversity,\n  title     = {A Diversity-Promoting Objective Function for Neural Conversation Models},\n  author    = {Li, Jiwei and others},\n  booktitle = {North American Chapter of the Association for Computational Linguistics},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1510.03055},\n}\n\n% ============================================================\n% REPRESENTATION / SPECTRAL COLLAPSE\n% ============================================================\n\n@inproceedings{jing2022understanding,\n  title     = {Understanding Dimensional Collapse in Contrastive Self-supervised Learning},\n  author    = {Jing, Li and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2022},\n  url       = {https://openreview.net/forum?id=YevsQ05DEN7},\n}\n\n@inproceedings{noci2024mind,\n  title     = {Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers},\n  author    = {Noci, Lorenzo and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2410.07799},\n}\n\n% ============================================================\n% DATA MIXING & ACCUMULATION\n% ============================================================\n\n@inproceedings{kazdan2025collapse,\n  title     = {Collapse or Thrive? {P}erils and Promises of Synthetic Data in a Self-Generating World},\n  author    = {Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2410.16713},\n}\n\n@inproceedings{dey2024breaking,\n  title     = {Is Model Collapse Inevitable? {B}reaking the Curse of Recursion by Accumulating Real and Synthetic Data},\n  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2404.01413},\n}\n\n@article{seddik2024howbad,\n  title     = {How Bad is Training on Synthetic Data? {A} Statistical Analysis of Language Model Collapse},\n  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  journal   = {arXiv preprint arXiv:2404.05090},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2404.05090},\n}\n\n@inproceedings{fu2025selfconsuming,\n  title     = {A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops},\n  author    = {Fu, Shi and Wang, Yingjie and Chen, Yuzhu and Tian, Xinmei and Tao, Dacheng},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.18865},\n}\n\n@article{bakshi2026improvement,\n  title     = {From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources},\n  author    = {Bakshi, Soham and Chakraborty, Sunrit},\n  journal   = {arXiv preprint arXiv:2602.10531},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2602.10531},\n}\n\n@article{he2025golden,\n  title     = {Golden Ratio Weighting Prevents Model Collapse},\n  author    = {He, Shiliang and Xu, Zhongbin and Cheng, Yan},\n  journal   = {arXiv preprint arXiv:2502.18049},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.18049},\n}\n\n@article{xu2025mixing,\n  title     = {Preventing Model Collapse Under Overparametrization: Optimal Mixing Ratios},\n  author    = {Xu, Zhongbin and Cheng, Yan},\n  journal   = {arXiv preprint arXiv:2509.22341},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2509.22341},\n}\n\n% ============================================================\n% MITIGATION & VERIFICATION\n% ============================================================\n\n@inproceedings{feng2025escaping,\n  title     = {Escaping Model Collapse via Synthetic Data Verification},\n  author    = {Feng, Yunzhen and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2510.16657},\n}\n\n@inproceedings{barzilai2025consistency,\n  title     = {When Models Don't Collapse: On the Consistency of Iterative {MLE}},\n  author    = {Barzilai, Daniel and Shamir, Ohad},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2505.19046},\n}\n\n@article{dces2026counter,\n  title     = {Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling},\n  author    = {Zhu, Bingze and Xie, Yubo},\n  journal   = {Electronics},\n  year      = {2026},\n  url       = {https://www.mdpi.com/2079-9292/15/4/869},\n}\n\n% ============================================================\n% POSITION / SURVEY / EPISTEMICS\n% ============================================================\n\n@article{schaeffer2025position,\n  title     = {Position: Model Collapse Does Not Mean What You Think},\n  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},\n  journal   = {arXiv preprint arXiv:2503.03150},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2503.03150},\n}\n\n@article{wright2025epistemic,\n  title     = {Epistemic Diversity and Knowledge Collapse in Large Language Models},\n  author    = {Wright, Dustin and Masud, Sarah and Moore, Jared and Yadav, Srishti and Antoniak, Maria and Park, Chan Young and Augenstein, Isabelle},\n  journal   = {arXiv preprint arXiv:2510.04226},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2510.04226},\n}\n\n% ============================================================\n% METHODOLOGY (GRANGER / LEAD-LAG)\n% ============================================================\n\n@article{granger1969investigating,\n  author    = {Granger, Clive W. J.},\n  title     = {Investigating Causal Relations by Econometric Models and Cross-spectral Methods},\n  journal   = {Econometrica},\n  volume    = {37},\n  number    = {3},\n  pages     = {424--438},\n  year      = {1969},\n  publisher = {Wiley},\n}\n\n@article{shojaie2022granger,\n  title     = {{Granger} Causality: A Review and Recent Advances},\n  author    = {Shojaie, Ali and Fox, Emily B.},\n  journal   = {Annual Review of Statistics and Its Application},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2105.02675},\n}\n\n@article{marcinkevics2022neural,\n  title     = {{Granger} Causality Using Neural Networks},\n  author    = {Marcinkevics, Raphael and Vogt, Julia},\n  journal   = {arXiv preprint arXiv:2208.03703},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2208.03703},\n}\n\n% ============================================================\n% EARLY WARNING SIGNALS / TIPPING POINTS (ECOLOGICAL THEORY)\n% ============================================================\n\n@article{scheffer2009early,\n  title     = {Early-warning signals for critical transitions},\n  author    = {Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George},\n  journal   = {Nature},\n  year      = {2009},\n  doi       = {10.1038/nature08227},\n}\n\n@article{scheffer2012anticipating,\n  title     = {Anticipating Critical Transitions},\n  author    = {Scheffer, Marten and Carpenter, Stephen R. and Lenton, Timothy M. and Bascompte, Jordi and Brock, William and Dakos, Vasilis and van de Koppel, Johan and van de Leemput, Ingrid A. and Levin, Simon A. and van Nes, Egbert H. and Pascual, Mercedes and Vandermeer, John},\n  journal   = {Science},\n  year      = {2012},\n  doi       = {10.1126/science.1225244},\n}\n\n@article{boettiger2012limits,\n  title     = {Quantifying Limits to Detection of Early Warning for Critical Transitions},\n  author    = {Boettiger, Carl and Hastings, Alan},\n  journal   = {Journal of the Royal Society Interface},\n  year      = {2012},\n  doi       = {10.1098/rsif.2012.0125},\n}\n\n% ============================================================\n% MODELS\n% ============================================================\n\n@inproceedings{biderman2023pythia,\n  title     = {Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling},\n  author    = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purber, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2304.01373},\n}\n\n% ============================================================\n% DATASETS\n% ============================================================\n\n@inproceedings{merity2017pointer,\n  title     = {Pointer Sentinel Mixture Models},\n  author    = {Merity, Stephen and Xiong, Caiming and Bradbury, James and Socher, Richard},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1609.07843},\n}\n",
      "numLines": 399,
      "startLine": 1,
      "totalLines": 399
    }
  },
  "sourceToolAssistantUUID": "c9da175d-a243-4b89-aa5c-21e2bbcf6a10",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T19:52:10.632Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QTzcRbrTLXrctwd3jEFw4h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a359c427-1a15-4d0b-badf-3e827b8b74de",
  "isSidechain": false,
  "requestId": "req_011Cb4wMJeEyJ8DZVT5x3j6W",
  "type": "assistant",
  "uuid": "1c86a5b5-9050-4aff-a7a5-c78e2bc85df3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DK3LTJPt3oa8L1zKw8x5XW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13261,
      "cache_read_input_tokens": 11841,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 360,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13261
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

_source line 16 · 2026-05-15T19:52:10.641Z_

<details><summary>↩ Tool result · `toolu_01QTzcRbrTLXrctwd3jEFw4h`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training language models on their own output across successive generations leads to progressive distribution degradation, a phenomenon variously termed model collapse~\cite{shumailov2024curse} or Model Autophagy Disorder~\cite{alemohammad2024mad}.
5	Tail modes vanish, lexical diversity narrows, and calibration deteriorates as each generation's output becomes the next generation's training data.
6	As large language models become ubiquitous content generators, the fraction of machine-generated text on the web grows steadily, making iterative training collapse---where models are unwittingly trained on the output of earlier model generations---a practical concern for the long-term stability of language model ecosystems.
7	
8	A natural follow-up question is whether cheap-to-compute statistics---\emph{canary metrics}---can provide early warning of impending collapse, analogous to early-warning signals for critical transitions in ecological and climate systems~\cite{scheffer2009early,scheffer2012anticipating}.
9	Several recent studies have pursued this direction: \citet{du2026geometric} informally observe that expected calibration error rises before accuracy degrades; SIGMA~\cite{sigma2026spectral} proposes spectral indicators of distributional shift; and DCES~\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.
10	Yet the statistical methodology underlying these lead-lag claims---whether a canary metric genuinely \emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends---has received little scrutiny.
11	
12	We identify four methodological deficiencies that pervade existing lead-lag analyses of iterative training collapse:
13	(1)~no differencing tests to rule out spurious regression arising from shared non-stationary trends---a well-known hazard when correlating co-trending time series;
14	(2)~no multi-method cross-validation---conclusions rest on a single statistical method whose implicit assumptions about stationarity and directionality are rarely examined;
15	(3)~no multiple comparison correction (e.g., Benjamini--Hochberg FDR control), increasing the risk of false discoveries when testing many metric pairs simultaneously; and
16	(4)~no regime-dependent analysis, despite the possibility that the same statistical test yields opposite conclusions at different contamination levels.
17	The closest predecessor is \citet{du2026geometric}, who observe that calibration error rises before accuracy degrades in iteratively trained language models.
18	Their analysis, however, is limited to a single metric pair, spans only 1--3 generations, and reports informal visual comparisons without statistical tests---leaving open the question of whether the observed lead is genuine or an artifact of shared trends.
19	The early-warning framework of \citet{scheffer2009early,scheffer2012anticipating}---widely adopted in ecology for anticipating tipping points---provides the theoretical motivation for canary-based prediction, but has not been systematically applied to iterative training collapse with the methodological rigor that short, noisy time series demand~\cite{boettiger2012limits}.
20	
21	We address these gaps through a systematic case study of canary prediction of diversity collapse---the progressive loss of lexical diversity in model-generated text across training generations.
22	Using Pythia-410M across five contamination levels ($\alpha \in \{0.00, 0.25, 0.50, 0.75, 1.00\}$) and up to four random seeds, we expose three methodological pitfalls that undermine naive lead-lag analysis:
23	\begin{enumerate}
24	    \item \textbf{Method sensitivity.} Applied to the same data, five lead-lag detection methods yield FDR significance rates ranging from 100\% (naive cross-correlation) to 25\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\kappa{=}0.185$ (poor agreement).
25	    \item \textbf{Spurious regression.} Canary$\to$perplexity associations appear near-universal in undifferenced analysis but vanish entirely after first-differencing ($F{\approx}0$, $p{=}0.99$), revealing them as artifacts of co-trending rather than genuine temporal precedence.
26	    \item \textbf{Regime dependence.} Permutation Granger tests find 24/24 canary$\to$diversity pairs FDR-significant at full synthetic replacement ($\alpha{=}1.0$) but 0/8 at $\alpha{\leq}0.50$, demonstrating that detectability depends sharply on the contamination level.
27	\end{enumerate}
28	To move beyond single-method analysis, we propose a multi-method consensus framework with empirically calibrated thresholds, requiring agreement across multiple independent statistical methods and random seeds before classifying a lead-lag relationship as robust.
29	
30	The framework's utility is demonstrated by its calibration on built-in experimental controls.
31	Naive cross-correlation identifies 100\% of canary--collapse metric pairs as FDR-significant; the consensus pipeline (requiring ${\geq}4/5$ methods and ${\geq}3/4$ seeds) retains only those pairs independently validated by the first-differencing diagnostic.
32	On reference extremes, the framework achieves a false positive rate of 0\% at the $\alpha{=}0.0$ null control (where individual methods reach up to 100\% FPR) and a false negative rate of 0\% against six ground-truth pairs at $\alpha{=}1.0$.
33	Applying the framework, we identify token entropy as a robust one-generation-ahead canary for diversity collapse at contamination levels $\alpha{\geq}0.75$, with cross-correlation $|r|{>}0.99$ and directional asymmetry confirmed by 0/24 reverse-direction FDR-significant pairs.
34	We note that Granger precedence establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}.
35	
36	Our contributions are:
37	\begin{enumerate}
38	    \item \textbf{Systematic exposure of three methodological pitfalls} in lead-lag analysis of iterative training collapse.
39	    We quantify each pitfall: method choice alone swings significance from 100\% to 25\% with a spurious-signal rate of 75\%; first-differencing eliminates canary$\to$perplexity associations entirely; and the same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.
40	    These results demonstrate that single-method, single-regime analyses---the current norm in this literature---are unreliable.
41	
42	    \item \textbf{A multi-method consensus framework} with empirically calibrated thresholds and four-tier practical guidance ranging from exploratory ($K{\geq}1/5$) to conservative ($K{=}5/5$).
43	    The framework achieves FPR${=}$0\% and FNR${=}$0\% on reference extremes, providing robustness against miscalibration of any individual method.
44	
45	    \item \textbf{Application of the framework to identify token entropy} as a one-generation-ahead canary for diversity collapse at $\alpha{\geq}0.75$, scoped precisely to diversity metrics (distinct-$n$) rather than model collapse broadly, with a tiered practical guide mapping contamination regimes to recommended analysis strategies.
46	\end{enumerate}
47	
48	The remainder of this paper is organized as follows.
49	\S\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.
50	\S\ref{sec:background} establishes the formal setup, notation, and the five detection methods used throughout.
51	\S\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.
52	\S\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\S\ref{sec:method_sensitivity}), regime-dependent detectability (\S\ref{sec:regime}), a case study of canary prediction of diversity collapse (\S\ref{sec:case_study}), and consensus framework validation (\S\ref{sec:consensus_validation}).
53	\S\ref{sec:discussion} discusses limitations---including the short time-series constraint, single-model scope, and the distinction between Granger precedence and causality---and outlines directions for future work.
54	\S\ref{sec:conclusion} concludes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c86a5b5-9050-4aff-a7a5-c78e2bc85df3",
  "isSidechain": false,
  "promptId": "bc9d0e00-4871-4d43-b046-0cec4ce72249",
  "type": "user",
  "uuid": "cc6a9f23-7b12-4c9e-8d43-e3993c832798",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining language models on their own output across successive generations leads to progressive distribution degradation, a phenomenon variously termed model collapse~\\cite{shumailov2024curse} or Model Autophagy Disorder~\\cite{alemohammad2024mad}.\nTail modes vanish, lexical diversity narrows, and calibration deteriorates as each generation's output becomes the next generation's training data.\nAs large language models become ubiquitous content generators, the fraction of machine-generated text on the web grows steadily, making iterative training collapse---where models are unwittingly trained on the output of earlier model generations---a practical concern for the long-term stability of language model ecosystems.\n\nA natural follow-up question is whether cheap-to-compute statistics---\\emph{canary metrics}---can provide early warning of impending collapse, analogous to early-warning signals for critical transitions in ecological and climate systems~\\cite{scheffer2009early,scheffer2012anticipating}.\nSeveral recent studies have pursued this direction: \\citet{du2026geometric} informally observe that expected calibration error rises before accuracy degrades; SIGMA~\\cite{sigma2026spectral} proposes spectral indicators of distributional shift; and DCES~\\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.\nYet the statistical methodology underlying these lead-lag claims---whether a canary metric genuinely \\emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends---has received little scrutiny.\n\nWe identify four methodological deficiencies that pervade existing lead-lag analyses of iterative training collapse:\n(1)~no differencing tests to rule out spurious regression arising from shared non-stationary trends---a well-known hazard when correlating co-trending time series;\n(2)~no multi-method cross-validation---conclusions rest on a single statistical method whose implicit assumptions about stationarity and directionality are rarely examined;\n(3)~no multiple comparison correction (e.g., Benjamini--Hochberg FDR control), increasing the risk of false discoveries when testing many metric pairs simultaneously; and\n(4)~no regime-dependent analysis, despite the possibility that the same statistical test yields opposite conclusions at different contamination levels.\nThe closest predecessor is \\citet{du2026geometric}, who observe that calibration error rises before accuracy degrades in iteratively trained language models.\nTheir analysis, however, is limited to a single metric pair, spans only 1--3 generations, and reports informal visual comparisons without statistical tests---leaving open the question of whether the observed lead is genuine or an artifact of shared trends.\nThe early-warning framework of \\citet{scheffer2009early,scheffer2012anticipating}---widely adopted in ecology for anticipating tipping points---provides the theoretical motivation for canary-based prediction, but has not been systematically applied to iterative training collapse with the methodological rigor that short, noisy time series demand~\\cite{boettiger2012limits}.\n\nWe address these gaps through a systematic case study of canary prediction of diversity collapse---the progressive loss of lexical diversity in model-generated text across training generations.\nUsing Pythia-410M across five contamination levels ($\\alpha \\in \\{0.00, 0.25, 0.50, 0.75, 1.00\\}$) and up to four random seeds, we expose three methodological pitfalls that undermine naive lead-lag analysis:\n\\begin{enumerate}\n    \\item \\textbf{Method sensitivity.} Applied to the same data, five lead-lag detection methods yield FDR significance rates ranging from 100\\% (naive cross-correlation) to 25\\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\\kappa{=}0.185$ (poor agreement).\n    \\item \\textbf{Spurious regression.} Canary$\\to$perplexity associations appear near-universal in undifferenced analysis but vanish entirely after first-differencing ($F{\\approx}0$, $p{=}0.99$), revealing them as artifacts of co-trending rather than genuine temporal precedence.\n    \\item \\textbf{Regime dependence.} Permutation Granger tests find 24/24 canary$\\to$diversity pairs FDR-significant at full synthetic replacement ($\\alpha{=}1.0$) but 0/8 at $\\alpha{\\leq}0.50$, demonstrating that detectability depends sharply on the contamination level.\n\\end{enumerate}\nTo move beyond single-method analysis, we propose a multi-method consensus framework with empirically calibrated thresholds, requiring agreement across multiple independent statistical methods and random seeds before classifying a lead-lag relationship as robust.\n\nThe framework's utility is demonstrated by its calibration on built-in experimental controls.\nNaive cross-correlation identifies 100\\% of canary--collapse metric pairs as FDR-significant; the consensus pipeline (requiring ${\\geq}4/5$ methods and ${\\geq}3/4$ seeds) retains only those pairs independently validated by the first-differencing diagnostic.\nOn reference extremes, the framework achieves a false positive rate of 0\\% at the $\\alpha{=}0.0$ null control (where individual methods reach up to 100\\% FPR) and a false negative rate of 0\\% against six ground-truth pairs at $\\alpha{=}1.0$.\nApplying the framework, we identify token entropy as a robust one-generation-ahead canary for diversity collapse at contamination levels $\\alpha{\\geq}0.75$, with cross-correlation $|r|{>}0.99$ and directional asymmetry confirmed by 0/24 reverse-direction FDR-significant pairs.\nWe note that Granger precedence establishes temporal predictive improvement, not true causality~\\cite{shojaie2022granger}.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Systematic exposure of three methodological pitfalls} in lead-lag analysis of iterative training collapse.\n    We quantify each pitfall: method choice alone swings significance from 100\\% to 25\\% with a spurious-signal rate of 75\\%; first-differencing eliminates canary$\\to$perplexity associations entirely; and the same Granger test shifts from 24/24 FDR-significant pairs to 0/8 across contamination levels.\n    These results demonstrate that single-method, single-regime analyses---the current norm in this literature---are unreliable.\n\n    \\item \\textbf{A multi-method consensus framework} with empirically calibrated thresholds and four-tier practical guidance ranging from exploratory ($K{\\geq}1/5$) to conservative ($K{=}5/5$).\n    The framework achieves FPR${=}$0\\% and FNR${=}$0\\% on reference extremes, providing robustness against miscalibration of any individual method.\n\n    \\item \\textbf{Application of the framework to identify token entropy} as a one-generation-ahead canary for diversity collapse at $\\alpha{\\geq}0.75$, scoped precisely to diversity metrics (distinct-$n$) rather than model collapse broadly, with a tiered practical guide mapping contamination regimes to recommended analysis strategies.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related_work} surveys related work on model collapse, early-warning signals, and lead-lag methodology.\n\\S\\ref{sec:background} establishes the formal setup, notation, and the five detection methods used throughout.\n\\S\\ref{sec:method} distills the three methodological pitfalls into a unified diagnostic framework, presents the multi-method consensus pipeline, and reports its empirical calibration.\n\\S\\ref{sec:experiments} provides full experimental results: method sensitivity analysis (\\S\\ref{sec:method_sensitivity}), regime-dependent detectability (\\S\\ref{sec:regime}), a case study of canary prediction of diversity collapse (\\S\\ref{sec:case_study}), and consensus framework validation (\\S\\ref{sec:consensus_validation}).\n\\S\\ref{sec:discussion} discusses limitations---including the short time-series constraint, single-model scope, and the distinction between Granger precedence and causality---and outlines directions for future work.\n\\S\\ref{sec:conclusion} concludes.",
      "numLines": 54,
      "startLine": 1,
      "totalLines": 54
    }
  },
  "sourceToolAssistantUUID": "1c86a5b5-9050-4aff-a7a5-c78e2bc85df3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T19:52:11.060Z_

<details open><summary>🔧 Tool call — Read · `toolu_017rbBm21m5RTeLBn3iJvGbg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc6a9f23-7b12-4c9e-8d43-e3993c832798",
  "isSidechain": false,
  "requestId": "req_011Cb4wMJeEyJ8DZVT5x3j6W",
  "type": "assistant",
  "uuid": "7d050845-bdc0-426d-b65e-076a02656420",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DK3LTJPt3oa8L1zKw8x5XW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13261,
      "cache_read_input_tokens": 11841,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13261,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 360,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13261,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13261
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

_source line 18_

```json
{
  "type": "last-prompt",
  "leafUuid": "7d050845-bdc0-426d-b65e-076a02656420",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Write Related Work section for paper",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f"
}
```

---

### Tool result

_source line 20 · 2026-05-15T19:52:11.410Z_

<details><summary>↩ Tool result · `toolu_017rbBm21m5RTeLBn3iJvGbg`</summary>

```text
1	papers:
2	  # ============================================================
3	  # CORE MODEL COLLAPSE
4	  # ============================================================
5	  - id: "shumailov2024curse"
6	    title: "The Curse of Recursion: Training on Generated Data Makes Models Forget"
7	    authors: "Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson"
8	    venue: "Nature"
9	    year: 2024
10	    url: "https://arxiv.org/abs/2305.17493"
11	    category: "core-collapse"
12	    role: "foundation"
13	    key_findings:
14	      - "定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失"
15	      - "区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）"
16	      - "三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合"
17	      - "在 VAE、GMM、LLM 上均验证了 collapse 的普遍性"
18	    relevance_to_us: "奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段"
19	    metrics_studied: ["perplexity", "distributional tail mass"]
20	
21	  - id: "alemohammad2024mad"
22	    title: "Self-Consuming Generative Models Go MAD"
23	    authors: "Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk"
24	    venue: "ICLR 2024"
25	    year: 2024
26	    url: "https://arxiv.org/abs/2307.01850"
27	    category: "core-collapse"
28	    role: "foundation"
29	    key_findings:
30	      - "提出 Model Autophagy Disorder (MAD) 概念"
31	      - "autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降"
32	      - "在图像生成领域验证 self-consuming loop 的退化效应"
33	    relevance_to_us: "MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上"
34	    metrics_studied: ["FID", "precision", "recall", "diversity"]
35	
36	  - id: "dohmatob2024tale"
37	    title: "A Tale of Tails: Model Collapse as a Change of Scaling Laws"
38	    authors: "Elvis Dohmatob, Yunzhen Feng, et al."
39	    venue: "ICML 2024"
40	    year: 2024
41	    url: "https://arxiv.org/abs/2402.07043"
42	    category: "core-collapse"
43	    role: "foundation"
44	    key_findings:
45	      - "通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化"
46	      - "发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式"
47	      - "混入少量干净数据可缓解 collapse 并引发 grokking 现象"
48	      - "在 transformer 算术任务和 Llama2 文本生成上验证"
49	    relevance_to_us: "scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为"
50	    metrics_studied: ["test loss", "scaling exponents"]
51	
52	  - id: "dohmatob2025strong"
53	    title: "Strong Model Collapse"
54	    authors: "Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe"
55	    venue: "ICLR 2025 (Spotlight)"
56	    year: 2025
57	    url: "https://arxiv.org/abs/2410.04840"
58	    category: "core-collapse"
59	    role: "foundation"
60	    key_findings:
61	      - "即使合成数据占比极小（1/1000），仍可导致 model collapse"
62	      - "更大的训练集并不能避免 collapse"
63	      - "更大的模型（random projection 近似下）反而可能放大 collapse"
64	      - "存在 interpolation threshold 的 double-descent 现象"
65	    relevance_to_us: "强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感"
66	    metrics_studied: ["test loss", "population risk"]
67	
68	  - id: "guo2024linguistic"
69	    title: "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text"
70	    authors: "Yanzhu Guo, Guokan Shang, et al."
71	    venue: "NAACL 2024 Findings"
72	    year: 2024
73	    url: "https://arxiv.org/abs/2311.09807"
74	    category: "core-collapse"
75	    role: "evaluation"
76	    key_findings:
77	      - "递归微调中，linguistic diversity 在连续迭代中持续下降"
78	      - "创造性任务中 diversity 下降最显著"
79	      - "开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系"
80	    relevance_to_us: "其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度"
81	    metrics_studied: ["distinct-n", "type-token ratio", "syntactic diversity", "semantic diversity"]
82	
83	  - id: "briesch2024selfconsuming"
84	    title: "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop"
85	    authors: "Martin Briesch, Dominik Sobania, Franz Rothlauf"
86	    venue: "arXiv (2311.16822)"
87	    year: 2024
88	    url: "https://arxiv.org/abs/2311.16822"
89	    category: "core-collapse"
90	    role: "direct-competitor"
91	    key_findings:
92	      - "首次系统研究 LLM 的 self-consuming training loop"
93	      - "full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降"
94	      - "expanding data cycle（累积）在 50 代内保持 diversity"
95	    relevance_to_us: "其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置"
96	    metrics_studied: ["diversity", "quality"]
97	
98	  - id: "truong2025entropy"
99	    title: "Entropy Collapse: A Universal Failure Mode of Intelligent Systems"
100	    authors: "Truong Xuan Khanh, Truong Quynh Hoa"
101	    venue: "arXiv (2512.12381)"
102	    year: 2025
103	    url: "https://arxiv.org/abs/2512.12381"
104	    category: "core-collapse"
105	    role: "theoretical-foundation"
106	    key_findings:
107	      - "证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats"
108	      - "两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2"
109	      - "因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警"
110	    relevance_to_us: "定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效"
111	    gaps: "理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力"
112	    metrics_studied: ["entropy", "autocorrelation", "variance"]
113	
114	  - id: "wang2026contaminated"
115	    title: "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training"
116	    authors: "Kevin Wang, Hongqian Niu, Didong Li"
117	    venue: "arXiv (2602.16065)"
118	    year: 2026
119	    url: "https://arxiv.org/abs/2602.16065"
120	    category: "core-collapse"
121	    role: "theoretical-foundation"
122	    key_findings:
123	      - "首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛"
124	      - "收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈"
125	      - "突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布"
126	    relevance_to_us: "为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率"
127	    gaps: "universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为"
128	    metrics_studied: ["convergence rate", "population risk"]
129	
130	  - id: "du2026geometric"
131	    title: "Escaping Mode Collapse in LLM Generation via Geometric Regulation"
132	    authors: "Du, Tanaka-Ishii"
133	    venue: "arXiv (2605.00435)"
134	    year: 2026
135	    url: "https://arxiv.org/abs/2605.00435"
136	    category: "core-collapse"
137	    role: "background"
138	    key_findings:
139	      - "将 mode collapse 重新解释为表示空间中的 geometric collapse：生成时模型内部轨迹被限制在低维子空间"
140	      - "提出 RMR（Reinforced Mode Regulation），在 value cache 中抑制 dominant self-reinforcing directions"
141	    relevance_to_us: "针对推理时 mode collapse，非迭代训练场景。但 'geometric collapse = 低维子空间坍缩' 与我们的 effective rank 指标在概念上有连接，可在 related work 中引用以说明 representation-space collapse 检测的跨场景通用性"
142	    metrics_studied: ["effective rank proxy", "representation dimensionality"]
143	
144	  - id: "gauthier2026alignment"
145	    title: "Explaining and Preventing Alignment Collapse in Iterative RLHF"
146	    authors: "Gauthier, Bach, Jordan"
147	    venue: "arXiv (2605.04266)"
148	    year: 2026
149	    url: "https://arxiv.org/abs/2605.04266"
150	    category: "core-collapse"
151	    role: "complementary"
152	    key_findings:
153	      - "迭代 RLHF 中 policy 生成 reward model 的训练数据形成反馈环路，导致 alignment collapse（policy 系统性利用 reward model 盲区）"
154	      - "用 Stackelberg game 建模迭代 RLHF 的环路动力学，提出 FPO（foresighted policy optimization）"
155	    relevance_to_us: "RLHF iterative feedback loop 与本项目 iterative synthetic data loop 结构类似——模型输出成为下一轮输入的反馈环路均导致系统性退化。其 'collapse = 反馈环路中的系统性退化' 叙事支持我们的大框架；Stackelberg game 视角可能启发 canary 的博弈论解释"
156	    metrics_studied: ["alignment score", "reward model accuracy"]
157	
158	  - id: "shi2026pruning"
159	    title: "Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions"
160	    authors: "Shi et al."
161	    venue: "arXiv (2605.07271)"
162	    year: 2026
163	    url: "https://arxiv.org/abs/2605.07271"
164	    category: "core-collapse"
165	    role: "background"
166	    key_findings:
167	      - "层剪枝导致的 performance collapse，定义 Silent Phase（模型预测被单一选项主导 = distributional collapse）和 Decisive Phase"
168	      - "剪枝 Silent Phase 立即触发 collapse"
169	    relevance_to_us: "架构剪枝 collapse，非数据驱动。其 'distributional collapse = 预测分布退化为单峰' 的操作定义与我们 token entropy 下降检测的是同一现象的不同表现"
170	    metrics_studied: ["prediction distribution entropy", "task accuracy"]
171	
172	  - id: "tubingen2026diffusion"
173	    title: "Layer Collapse in Diffusion Language Models"
174	    authors: "Tübingen AI Center et al."
175	    venue: "arXiv (2605.06366)"
176	    year: 2026
177	    url: "https://arxiv.org/abs/2605.06366"
178	    category: "core-collapse"
179	    role: "background"
180	    key_findings:
181	      - "LLaDA-8B 中发现层级 activation collapse：少数早期层的 activation 被单个 super-outlier 主导"
182	      - "剪掉此 outlier 导致模型输出退化为重复随机 token"
183	    relevance_to_us: "Diffusion LM 的架构 collapse，与迭代合成数据训练无关。但 activation collapse 的表征与 spectral collapse 有交集"
184	    metrics_studied: ["activation magnitude", "output repetition"]
185	
186	  # ============================================================
187	  # CANARY / EARLY WARNING METRICS
188	  # ============================================================
189	  - id: "chen2025scales"
190	    title: "Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios"
191	    authors: "Anonymous"
192	    venue: "arXiv (2510.05133)"
193	    year: 2025
194	    url: "https://arxiv.org/abs/2510.05133"
195	    category: "canary-metrics"
196	    role: "direct-competitor"
197	    key_findings:
198	      - "**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal"
199	      - "20% synthetic data 以下性能稳定，30% 以上退化加速"
200	      - "大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒"
201	      - "推理任务比检索任务更易退化"
202	      - "iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）"
203	    relevance_to_us: "**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架"
204	    metrics_studied: ["ECE", "accuracy", "perplexity"]
205	
206	  - id: "gambetta2024surplexity"
207	    title: "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI"
208	    authors: "Daniele Gambetta et al."
209	    venue: "arXiv (2410.12341)"
210	    year: 2024
211	    url: "https://arxiv.org/abs/2410.12341"
212	    category: "canary-metrics"
213	    role: "direct-competitor"
214	    key_findings:
215	      - "提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据"
216	      - "用 semantic networks 分析文本重复性和语义多样性"
217	      - "用 next-token probability 定量衡量 diversity loss"
218	      - "高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜"
219	      - "不需要区分 human vs AI-generated data"
220	    relevance_to_us: "surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角"
221	    metrics_studied: ["surplexity", "semantic network metrics", "next-token probability"]
222	
223	  - id: "qiu2025spectral"
224	    title: "Spectral Alignment as Predictor of Loss Explosion in Neural Network Training"
225	    authors: "Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao"
226	    venue: "arXiv (2510.04202)"
227	    year: 2025
228	    url: "https://arxiv.org/abs/2510.04202"
229	    category: "canary-metrics"
230	    role: "method-component"
231	    key_findings:
232	      - "Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐"
233	      - "SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器"
234	      - "比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败"
235	      - "健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定"
236	    relevance_to_us: "SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel"
237	    metrics_studied: ["spectral alignment", "weight norm", "gradient norm"]
238	
239	  - id: "he2025closer"
240	    title: "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"
241	    authors: "Shiliang He et al."
242	    venue: "NeurIPS 2025 (Spotlight)"
243	    year: 2025
244	    url: "https://arxiv.org/abs/2509.16499"
245	    category: "canary-metrics"
246	    role: "direct-competitor"
247	    key_findings:
248	      - "识别 diffusion model collapse 中的 generalization → memorization 转变"
249	      - "**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**"
250	      - "提出基于 entropy 的数据选择策略，有效缓解 collapse"
251	    relevance_to_us: "data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效"
252	    metrics_studied: ["entropy", "FID", "diversity"]
253	
254	  - id: "ba2024fill"
255	    title: "Fill In The Gaps: Model Calibration and Generalization with Synthetic Data"
256	    authors: "Yang Ba, Michelle V Mancenido, Rong Pan"
257	    venue: "EMNLP 2024"
258	    year: 2024
259	    url: "https://arxiv.org/abs/2410.10864"
260	    category: "canary-metrics"
261	    role: "background"
262	    key_findings:
263	      - "用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins"
264	      - "推导了基于 PAC 框架的 ECE bound"
265	      - "合成数据可改善 calibration 但需精心设计生成策略"
266	    relevance_to_us: "ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据"
267	    metrics_studied: ["ECE", "accuracy"]
268	
269	  - id: "sigma2026spectral"
270	    title: "SIGMA: Scalable Spectral Insights for LLM Model Collapse"
271	    authors: "Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue"
272	    venue: "arXiv (2601.03385)"
273	    year: 2026
274	    url: "https://arxiv.org/abs/2601.03385"
275	    category: "canary-metrics"
276	    role: "direct-competitor"
277	    key_findings:
278	      - "基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样"
279	      - "Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影"
280	      - "随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控"
281	    relevance_to_us: "最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成"
282	    gaps: "未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略"
283	    metrics_studied: ["Gram matrix eigenspectrum", "spectral norm bounds"]
284	
285	  - id: "kalinowski2026topology"
286	    title: "Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index"
287	    authors: "Alexander Kalinowski"
288	    venue: "arXiv (2604.26984)"
289	    year: 2026
290	    url: "https://arxiv.org/abs/2604.26984"
291	    category: "canary-metrics"
292	    role: "background"
293	    key_findings:
294	      - "提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建"
295	      - "Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning"
296	      - "拓扑方法捕捉表示空间的各向异性和多尺度结构丧失"
297	    relevance_to_us: "topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由"
298	    gaps: "计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比"
299	    metrics_studied: ["Collapse Index", "persistent homology features"]
300	
301	  - id: "bergsma2026scaling"
302	    title: "Scaling with Collapse: Efficient and Predictable Training of LLM Families"
303	    authors: "Bergsma et al."
304	    venue: "arXiv (2509.25087, rev. Mar 2026)"
305	    year: 2026
306	    url: "https://arxiv.org/abs/2509.25087"
307	    category: "canary-metrics"
308	    role: "background"
309	    key_findings:
310	      - "'Collapse' 此处指 loss curve 归一化后坍缩到通用轨迹（非 model collapse）"
311	      - "deviation-from-collapse 作为训练病理的早期诊断信号"
312	    relevance_to_us: "不同语境下的 'collapse'。但其 '偏离通用轨迹 = 训练出问题' 的监控思路与我们的 canary 理念相似——均从时序异常检测角度切入"
313	    metrics_studied: ["loss curve deviation", "scaling law exponents"]
314	
315	  # ============================================================
316	  # DIVERSITY METRICS (BACKGROUND)
317	  # ============================================================
318	  - id: "zhu2018texygen"
319	    title: "Texygen: A Benchmarking Platform for Text Generation Models"
320	    authors: "Yaoming Zhu et al."
321	    venue: "SIGIR 2018"
322	    year: 2018
323	    url: "https://arxiv.org/abs/1802.01886"
324	    category: "canary-metrics"
325	    role: "background"
326	    key_findings:
327	      - "提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低"
328	      - "成为文本生成多样性评估的标准基准之一"
329	    relevance_to_us: "Self-BLEU 是我们 diversity canary 的经典候选"
330	    metrics_studied: ["Self-BLEU", "BLEU"]
331	
332	  - id: "li2016diversity"
333	    title: "A Diversity-Promoting Objective Function for Neural Conversation Models"
334	    authors: "Jiwei Li et al."
335	    venue: "NAACL 2016"
336	    year: 2016
337	    url: "https://arxiv.org/abs/1510.03055"
338	    category: "canary-metrics"
339	    role: "background"
340	    key_findings:
341	      - "提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性"
342	      - "计算 unique n-gram 数占总 n-gram 数的比例"
343	    relevance_to_us: "distinct-n 是最廉价的 diversity canary 之一，计算开销极低"
344	    metrics_studied: ["distinct-1", "distinct-2"]
345	
346	  # ============================================================
347	  # REPRESENTATION / SPECTRAL COLLAPSE
348	  # ============================================================
349	  - id: "jing2022understanding"
350	    title: "Understanding Dimensional Collapse in Contrastive Self-supervised Learning"
351	    authors: "Li Jing et al."
352	    venue: "ICLR 2022"
353	    year: 2022
354	    url: "https://openreview.net/forum?id=YevsQ05DEN7"
355	    category: "canary-metrics"
356	    role: "method-component"
357	    key_findings:
358	      - "定义 dimensional collapse：embedding 向量只跨越低维子空间"
359	      - "effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量"
360	      - "strong augmentation 和 implicit regularization 驱动低秩解"
361	    relevance_to_us: "effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控"
362	    metrics_studied: ["effective rank", "singular value spectrum"]
363	
364	  - id: "noci2024mind"
365	    title: "Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers"
366	    authors: "Lorenzo Noci et al."
367	    venue: "NeurIPS 2024"
368	    year: 2024
369	    url: "https://arxiv.org/abs/2410.07799"
370	    category: "canary-metrics"
371	    role: "method-component"
372	    key_findings:
373	      - "用 Random Matrix Theory 分析 attention 层的 rank collapse"
374	      - "发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因"
375	      - "rank collapse in depth: 所有 token 沿层收敛到单一表示"
376	    relevance_to_us: "spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作"
377	    metrics_studied: ["spectral gap", "singular values", "effective rank"]
378	
379	  # ============================================================
380	  # DATA MIXING & ACCUMULATION
381	  # ============================================================
382	  - id: "kazdan2025collapse"
383	    title: "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World"
384	    authors: "Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo"
385	    venue: "ICML 2025"
386	    year: 2025
387	    url: "https://arxiv.org/abs/2410.16713"
388	    category: "data-mixing"
389	    role: "foundation"
390	    key_findings:
391	      - "系统对比 replace vs accumulate 场景"
392	      - "replace → collapse；accumulate → 可避免 collapse"
393	      - "发现 real data 和 synthetic data 之间存在非平凡的交互效应"
394	      - "synthetic data 的价值取决于 real data 的绝对数量"
395	    relevance_to_us: "直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考"
396	    metrics_studied: ["test loss"]
397	
398	  - id: "dey2024breaking"
399	    title: "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data"
400	    authors: "Apratim Dey, David Donoho, et al."
401	    venue: "ICML 2024"
402	    year: 2024
403	    url: "https://arxiv.org/abs/2404.01413"
404	    category: "data-mixing"
405	    role: "foundation"
406	    key_findings:
407	      - "替换数据 → 发散 population risk；累积数据 → 避免发散"
408	      - "证明累积策略在多种模型（GMM, HMM, LLM）上有效"
409	    relevance_to_us: "为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子"
410	    metrics_studied: ["population risk"]
411	
412	  - id: "seddik2024howbad"
413	    title: "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse"
414	    authors: "Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane"
415	    venue: "arXiv (2404.05090)"
416	    year: 2024
417	    url: "https://arxiv.org/abs/2404.05090"
418	    category: "data-mixing"
419	    role: "background"
420	    key_findings:
421	      - "纯合成数据训练不可避免 collapse"
422	      - "给出 synthetic data 比例上界的估计——低于此比例可避免 collapse"
423	      - "递归训练使原始分布尾部消失"
424	    relevance_to_us: "其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值"
425	    metrics_studied: ["perplexity"]
426	
427	  - id: "fu2025selfconsuming"
428	    title: "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops"
429	    authors: "Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao"
430	    venue: "ICLR 2025"
431	    year: 2025
432	    url: "https://arxiv.org/abs/2502.18865"
433	    category: "data-mixing"
434	    role: "theoretical-foundation"
435	    key_findings:
436	      - "引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析"
437	      - "恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight"
438	      - "模型架构和 real/synthetic 数据比例共同决定 STL 的成败"
439	    relevance_to_us: "为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证"
440	    gaps: "理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构"
441	    metrics_studied: ["generalization bound", "population risk"]
442	
443	  - id: "bakshi2026improvement"
444	    title: "From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources"
445	    authors: "Soham Bakshi, Sunrit Chakraborty"
446	    venue: "arXiv (2602.10531)"
447	    year: 2026
448	    url: "https://arxiv.org/abs/2602.10531"
449	    category: "data-mixing"
450	    role: "theoretical-foundation"
451	    key_findings:
452	      - "αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency"
453	      - "当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）"
454	      - "αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime"
455	      - "在 next-token prediction 语言模型上分析完整迭代演化动态"
456	    relevance_to_us: "αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式"
457	    gaps: "理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime"
458	    metrics_studied: ["population risk", "total variation distance"]
459	
460	  - id: "he2025golden"
461	    title: "Golden Ratio Weighting Prevents Model Collapse"
462	    authors: "Shiliang He, Zhongbin Xu, Yan Cheng"
463	    venue: "arXiv (2502.18049)"
464	    year: 2025
465	    url: "https://arxiv.org/abs/2502.18049"
466	    category: "data-mixing"
467	    role: "theoretical-foundation"
468	    key_findings:
469	      - "最优 real data 权重在 Gaussian estimation、GLM、非参数估计中均收敛到黄金比例倒数 1/φ ≈ 0.618"
470	      - "最优权重 w*(λ) 作为正则化参数的函数既非单调也非凸——risk landscape 在 mixing ratio 空间上本身不是单调的"
471	      - "提供了 mixing ratio 非单调性的首个理论框架"
472	    relevance_to_us: "我们在 α-sweep 中观测到的非单调 dose-response（α=0.25 比 α=0.50 collapse 更严重）可视为该理论在 diversity metrics 上的实证验证。论文 Discussion 的理论锚点。"
473	    gaps: "理论基于线性回归和高斯分布，未直接推广到 LLM diversity metrics"
474	    metrics_studied: ["population risk", "optimal weight"]
475	
476	  - id: "xu2025mixing"
477	    title: "Preventing Model Collapse Under Overparametrization: Optimal Mixing Ratios"
478	    authors: "Zhongbin Xu, Yan Cheng"
479	    venue: "arXiv (2509.22341)"
480	    year: 2025
481	    url: "https://arxiv.org/abs/2509.22341"
482	    category: "data-mixing"
483	    role: "theoretical-foundation"
484	    key_findings:
485	      - "过参数化 regime（插值学习 + ridge 回归）中分析最优混合比例"
486	      - "插值学习：最优 real data 比例收敛到 1/φ"
487	      - "Ridge 回归：最优比例受谱几何控制，至少为 1/2"
488	      - "w > 1/3 时 variance 随迭代单调递减；w < 1/3 时 variance 可能增长——存在临界阈值"
489	    relevance_to_us: "1/3 临界阈值与我们 α=0.25（real weight=0.75 vs synthetic weight=0.25）处出现最强 collapse 的观测有概念对应。不同 regime 下 variance 行为质变支持我们的 regime-dependent 叙事。"
490	    gaps: "参数空间不完全对齐（他们的 w 是 real data weight，我们的 α 是 synthetic ratio）；未讨论 diversity metrics"
491	    metrics_studied: ["variance", "population risk", "optimal mixing ratio"]
492	
493	  # ============================================================
494	  # MITIGATION & VERIFICATION
495	  # ============================================================
496	  - id: "feng2025escaping"
497	    title: "Escaping Model Collapse via Synthetic Data Verification"
498	    authors: "Yunzhen Feng et al."
499	    venue: "NeurIPS 2025"
500	    year: 2025
501	    url: "https://arxiv.org/abs/2510.16657"
502	    category: "data-mixing"
503	    role: "background"
504	    key_findings:
505	      - "通过外部 verifier（human 或 better model）注入信息可避免 collapse"
506	      - "verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center"
507	      - "除非 verifier 完全可靠，早期收益会 plateau 甚至逆转"
508	    relevance_to_us: "verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention"
509	    metrics_studied: ["test loss"]
510	
511	  - id: "barzilai2025consistency"
512	    title: "When Models Don't Collapse: On the Consistency of Iterative MLE"
513	    authors: "Daniel Barzilai, Ohad Shamir"
514	    venue: "ICML 2025"
515	    year: 2025
516	    url: "https://arxiv.org/abs/2505.19046"
517	    category: "core-collapse"
518	    role: "background"
519	    key_findings:
520	      - "在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse"
521	      - "但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例"
522	    relevance_to_us: "理论上的 collapse 可发生任意快的结论强化了 early warning 的价值"
523	    metrics_studied: []
524	
525	  - id: "dces2026counter"
526	    title: "Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling"
527	    authors: "Anonymous"
528	    venue: "MDPI Electronics (2026)"
529	    year: 2026
530	    url: "https://www.mdpi.com/2079-9292/15/4/869"
531	    category: "data-mixing"
532	    role: "background"
533	    key_findings:
534	      - "提出 DCES（dynamic center-edge sampling）数据选择框架"
535	      - "DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择"
536	    relevance_to_us: "其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考"
537	    metrics_studied: ["ECE", "entropy"]
538	
539	  # ============================================================
540	  # POSITION / SURVEY / EPISTEMICS
541	  # ============================================================
542	  - id: "schaeffer2025position"
543	    title: "Position: Model Collapse Does Not Mean What You Think"
544	    authors: "Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo"
545	    venue: "arXiv (2503.03150)"
546	    year: 2025
547	    url: "https://arxiv.org/abs/2503.03150"
548	    category: "core-collapse"
549	    role: "background"
550	    key_findings:
551	      - "文献中实际包含 8 种不同且有时矛盾的 model collapse 定义"
552	      - "许多 collapse 预测依赖于与现实不符的假设"
553	      - "多种 collapse 场景是可以轻易避免的"
554	    relevance_to_us: "提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标"
555	    metrics_studied: []
556	
557	  - id: "wright2025epistemic"
558	    title: "Epistemic Diversity and Knowledge Collapse in Large Language Models"
559	    authors: "Wright, Dustin and Masud, Sarah and Moore, Jared and Yadav, Srishti and Antoniak, Maria and Park, Chan Young and Augenstein, Isabelle"
560	    venue: "arXiv (2510.04226)"
561	    year: 2025
562	    url: "https://arxiv.org/abs/2510.04226"
563	    category: "core-collapse"
564	    role: "background"
565	    key_findings:
566	      - "27 个 LLM 在 155 个主题上的 epistemic diversity 评估"
567	      - "所有模型的 epistemic diversity 低于基本 web 搜索"
568	      - "模型越大 epistemic diversity 反而越低；RAG 有正面效果"
569	    relevance_to_us: "knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic"
570	    metrics_studied: ["epistemic diversity"]
571	
572	  # ============================================================
573	  # METHODOLOGY (GRANGER / LEAD-LAG)
574	  # ============================================================
575	  - id: "shojaie2022granger"
576	    title: "Granger Causality: A Review and Recent Advances"
577	    authors: "Ali Shojaie, Emily B. Fox"
578	    venue: "Annual Review of Statistics and Its Application"
579	    year: 2022
580	    url: "https://arxiv.org/abs/2105.02675"
581	    category: "methodology"
582	    role: "method-component"
583	    key_findings:
584	      - "Granger causality 综述：从经典线性到非线性/neural 方法"
585	      - "Panel data 场景的 Granger causality 扩展"
586	      - "VAR 和 neural Granger causality 的对比"
587	    relevance_to_us: "为我们的 panel Granger causality 分析提供方法论基础"
588	    metrics_studied: []
589	
590	  - id: "marcinkevics2022neural"
591	    title: "Granger Causality Using Neural Networks"
592	    authors: "Raphael Marcinkevics, Julia Vogt"
593	    venue: "arXiv (2208.03703)"
594	    year: 2022
595	    url: "https://arxiv.org/abs/2208.03703"
596	    category: "methodology"
597	    role: "method-component"
598	    key_findings:
599	      - "用 neural network 估计 Granger causality，突破线性假设"
600	      - "两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据"
601	    relevance_to_us: "我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择"
602	    metrics_studied: []
603	
604	  # ============================================================
605	  # EARLY WARNING SIGNALS / TIPPING POINTS (ECOLOGICAL THEORY)
606	  # ============================================================
607	  - id: "scheffer2009early"
608	    title: "Early-warning signals for critical transitions"
609	    authors: "Marten Scheffer, Jordi Bascompte, William A. Brock, Victor Brovkin, Stephen R. Carpenter, Vasilis Dakos, Hermann Held, Egbert H. van Nes, Max Rietkerk, George Sugihara"
610	    venue: "Nature"
611	    year: 2009
612	    doi: "10.1038/nature08227"
613	    category: "early-warning-signals"
614	    role: "theoretical-foundation"
615	    key_findings:
616	      - "复杂系统（生态、气候、金融）在临界转变前存在通用 early warning signals：critical slowing down 导致 autocorrelation 增加、variance 增加、recovery rate 降低"
617	      - "这些 generic indicators 不依赖于系统具体机制，而是源于分岔点附近的数学共性"
618	      - "综述了跨领域的 tipping point 检测方法，建立了 early warning signals 的理论框架"
619	    relevance_to_us: "我们将 token entropy / diversity 下降类比为生态系统 tipping point 前的 early warning signal——diversity collapse 在概念上对应生态系统的 critical transition。Scheffer 的 generic indicator 框架为我们的 multi-metric canary panel 提供跨学科理论基础"
620	    one_line_finding: "复杂系统临界转变前存在通用早期预警信号（critical slowing down），可跨领域检测 tipping point"
621	    metrics_studied: ["autocorrelation", "variance", "recovery rate"]
622	
623	  - id: "scheffer2012anticipating"
624	    title: "Anticipating Critical Transitions"
625	    authors: "Marten Scheffer, Stephen R. Carpenter, Timothy M. Lenton, Jordi Bascompte, William Brock, Vasilis Dakos, Johan van de Koppel, Ingrid A. van de Leemput, Simon A. Levin, Egbert H. van Nes, Mercedes Pascual, John Vandermeer"
626	    venue: "Science"
627	    year: 2012
628	    doi: "10.1126/science.1225244"
629	    category: "early-warning-signals"
630	    role: "theoretical-foundation"
631	    key_findings:
632	      - "整合两条研究线：(1) 揭示网络架构特征导致 tipping points 的结构性原因，(2) 发现接近临界阈值的通用经验指标"
633	      - "Tipping points 既意味着 unwanted collapse 的风险，也意味着 positive change 的机会——关键在于预测能力"
634	      - "提出将网络架构分析与经验预警指标结合的交叉方法论"
635	    relevance_to_us: "将 early warning 从纯统计信号扩展到网络/架构分析——类比我们同时监控输出统计（ECE, entropy）和表征结构（effective rank, spectral）的多层 canary panel 设计。其 'architecture → tipping point' 分析呼应我们对模型内部表征 collapse 的关注"
636	    one_line_finding: "结合网络架构分析与经验预警指标可更有效地预测复杂系统的临界转变"
637	    metrics_studied: ["network architecture features", "empirical early warning indicators"]
638	
639	  - id: "boettiger2012limits"
640	    title: "Quantifying Limits to Detection of Early Warning for Critical Transitions"
641	    authors: "Carl Boettiger, Alan Hastings"
642	    venue: "Journal of the Royal Society Interface"
643	    year: 2012
644	    doi: "10.1098/rsif.2012.0125"
645	    category: "early-warning-signals"
646	    role: "methodological-precedent"
647	    key_findings:
648	      - "用 likelihood ratio 框架量化 early warning signals 的统计检测力——在有限长度时间序列下，EWS 检测力极低"
649	      - "即使系统确实在接近 tipping point，短时间序列中 autocorrelation 增加等 EWS 的统计显著性往往不足以拒绝零假设"
650	      - "检测力取决于时间序列长度、噪声水平、接近临界点的速率——现实数据常处于低检测力 regime"
651	    relevance_to_us: "与 Claim 3（方法选择敏感性）和 plan_009（TY power analysis, T=10 power=0.05-0.20）高度对齐。Boettiger & Hastings 从生态学角度量化了 EWS 在短时间序列下的统计极限，我们在 model collapse 迭代训练语境下独立发现了同样的问题——少数迭代轮次下 canary 检测力不足。他们的 power analysis 框架为我们的统计检测力论证提供了跨学科先例"
652	    one_line_finding: "Early warning signals 在短时间序列下统计检测力极低，量化了 EWS 检测的基本统计极限"
653	    metrics_studied: ["autocorrelation", "variance", "likelihood ratio", "statistical power"]
654	
655	gaps:
656	  - "无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse"
657	  - "ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析"
658	  - "embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过"
659	  - "多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系"
660	  - "alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化"
661	  - "diversity dose-response 非单调性（α=0.25 比 α=0.50 collapse 更严重）无先例报告——He et al. 2025 从理论上预测 risk landscape 非单调，但无人在 LLM diversity 上实证验证"
662	  - "predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益"
663	  - "surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证"
664	  - "跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠"
665	
666	novelty_assessment: |
667	  我们项目的核心 novelty 在于：
668	
669	  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。
670	     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，
671	     但没有人做过系统的 lead-lag 量化分析。
672	
673	  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、
674	     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。
675	     现有工作都是单一指标或最多两三个指标的孤立分析。
676	
677	  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary
678	     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，
679	     但没人研究 canary 在不同 alpha 下的行为。
680	
681	  4. **与已有工作的差异**：
682	     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化
683	     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；
684	       我们将其纳入更广的 panel 并研究其 lead-lag 特性
685	     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标
686	     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；
687	       我们将类似思路迁移到 iterative collapse 场景
688	
689	  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，
690	     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。
691	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d050845-bdc0-426d-b65e-076a02656420",
  "isSidechain": false,
  "promptId": "bc9d0e00-4871-4d43-b046-0cec4ce72249",
  "type": "user",
  "uuid": "24ba7bc8-70bb-42a3-bc57-a22fe244b118",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml",
      "content": "papers:\n  # ============================================================\n  # CORE MODEL COLLAPSE\n  # ============================================================\n  - id: \"shumailov2024curse\"\n    title: \"The Curse of Recursion: Training on Generated Data Makes Models Forget\"\n    authors: \"Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Yarin Gal, Nicolas Papernot, Ross Anderson\"\n    venue: \"Nature\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2305.17493\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"定义 model collapse 现象：迭代用合成数据替换真实数据训练会导致分布尾部消失\"\n      - \"区分 early model collapse（尾部信息丢失）和 late model collapse（分布完全收敛）\"\n      - \"三类误差来源：statistical approximation, functional expressivity, functional approximation，跨代复合\"\n      - \"在 VAE、GMM、LLM 上均验证了 collapse 的普遍性\"\n    relevance_to_us: \"奠基论文，定义了我们研究的核心现象。我们的 canary 指标旨在提前检测其描述的 early collapse 阶段\"\n    metrics_studied: [\"perplexity\", \"distributional tail mass\"]\n\n  - id: \"alemohammad2024mad\"\n    title: \"Self-Consuming Generative Models Go MAD\"\n    authors: \"Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard Baraniuk\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2307.01850\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"提出 Model Autophagy Disorder (MAD) 概念\"\n      - \"autophagous loop 中没有足够新鲜真实数据时，质量或多样性必然渐进下降\"\n      - \"在图像生成领域验证 self-consuming loop 的退化效应\"\n    relevance_to_us: \"MAD 框架与我们的 iterative loop 设置直接对应；其 quality vs diversity tradeoff 可能反映在不同 canary 指标上\"\n    metrics_studied: [\"FID\", \"precision\", \"recall\", \"diversity\"]\n\n  - id: \"dohmatob2024tale\"\n    title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.07043\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"通过 scaling laws 视角分析 model collapse：collapse 表现为 scaling law 的变化\"\n      - \"发现 loss of scaling, shifted scaling, skill un-learning, grokking 等多种退化模式\"\n      - \"混入少量干净数据可缓解 collapse 并引发 grokking 现象\"\n      - \"在 transformer 算术任务和 Llama2 文本生成上验证\"\n    relevance_to_us: \"scaling law 变化视角为我们提供了理论基础；grokking 现象暗示 canary 指标可能出现非单调行为\"\n    metrics_studied: [\"test loss\", \"scaling exponents\"]\n\n  - id: \"dohmatob2025strong\"\n    title: \"Strong Model Collapse\"\n    authors: \"Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe\"\n    venue: \"ICLR 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.04840\"\n    category: \"core-collapse\"\n    role: \"foundation\"\n    key_findings:\n      - \"即使合成数据占比极小（1/1000），仍可导致 model collapse\"\n      - \"更大的训练集并不能避免 collapse\"\n      - \"更大的模型（random projection 近似下）反而可能放大 collapse\"\n      - \"存在 interpolation threshold 的 double-descent 现象\"\n    relevance_to_us: \"强化了早期检测的必要性——即使极小的合成数据比例也能触发 collapse，因此 canary 指标必须敏感\"\n    metrics_studied: [\"test loss\", \"population risk\"]\n\n  - id: \"guo2024linguistic\"\n    title: \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\"\n    authors: \"Yanzhu Guo, Guokan Shang, et al.\"\n    venue: \"NAACL 2024 Findings\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.09807\"\n    category: \"core-collapse\"\n    role: \"evaluation\"\n    key_findings:\n      - \"递归微调中，linguistic diversity 在连续迭代中持续下降\"\n      - \"创造性任务中 diversity 下降最显著\"\n      - \"开发了覆盖 lexical、syntactic、semantic 三层的 diversity 指标体系\"\n    relevance_to_us: \"其多层 diversity 指标体系可直接作为我们 canary 指标的候选集；创造性 vs 事实任务的差异可能影响 canary 灵敏度\"\n    metrics_studied: [\"distinct-n\", \"type-token ratio\", \"syntactic diversity\", \"semantic diversity\"]\n\n  - id: \"briesch2024selfconsuming\"\n    title: \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop\"\n    authors: \"Martin Briesch, Dominik Sobania, Franz Rothlauf\"\n    venue: \"arXiv (2311.16822)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2311.16822\"\n    category: \"core-collapse\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"首次系统研究 LLM 的 self-consuming training loop\"\n      - \"full synthetic cycle（完全替换）导致单点 collapse；data augmentation cycle 导致 diversity 缓慢下降\"\n      - \"expanding data cycle（累积）在 50 代内保持 diversity\"\n    relevance_to_us: \"其不同 data cycle 策略的对比直接对应我们的 alpha（synthetic ratio）实验设置\"\n    metrics_studied: [\"diversity\", \"quality\"]\n\n  - id: \"truong2025entropy\"\n    title: \"Entropy Collapse: A Universal Failure Mode of Intelligent Systems\"\n    authors: \"Truong Xuan Khanh, Truong Quynh Hoa\"\n    venue: \"arXiv (2512.12381)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2512.12381\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"证明 entropy collapse 是一阶（不连续）相变，临界点 α_c(β) = 1/(1−β)，entropy 在临界点跳变 0.698 nats\"\n      - \"两个 universality class：Class 1（凸反馈，如 power-law）不可逆 ν=1；Class 2（线性反馈）可逆 ν=1/2\"\n      - \"因为是一阶相变，autocorrelation/variance 等传统 early-warning signal 在 collapse 前保持有限——无预警\"\n    relevance_to_us: \"定义了 canary 失效的 regime boundary：Class 1 凸反馈系统中传统 canary 理论上无效。我们需证明我们的 canary 在 Class 2+ regime 或非纯反馈场景中有效\"\n    gaps: \"理论框架高度抽象，未给出 LLM 具体场景下的 α/β 估计方法；未测试哪些 canary 在接近一阶相变时仍有部分预警能力\"\n    metrics_studied: [\"entropy\", \"autocorrelation\", \"variance\"]\n\n  - id: \"wang2026contaminated\"\n    title: \"Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training\"\n    authors: \"Kevin Wang, Hongqian Niu, Didong Li\"\n    venue: \"arXiv (2602.16065)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.16065\"\n    category: \"core-collapse\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"首个不限数据分布假设的正面理论结果：universal approximator 下 contaminated recursive training 仍可收敛\"\n      - \"收敛速率 = min(baseline 模型收敛速率, 每轮真实数据比例)——真实数据比例是瓶颈\"\n      - \"突破了先前仅限 discrete/Gaussian 分布的理论框架，适用于一般连续分布\"\n    relevance_to_us: \"为 post-MVP α-sweep 实验提供理论上界：收敛速率由 real data fraction 决定，可预测不同 α 下的 collapse 速率\"\n    gaps: \"universal approximator 假设在实际有限容量模型中不严格成立；未讨论 canary 指标行为\"\n    metrics_studied: [\"convergence rate\", \"population risk\"]\n\n  - id: \"du2026geometric\"\n    title: \"Escaping Mode Collapse in LLM Generation via Geometric Regulation\"\n    authors: \"Du, Tanaka-Ishii\"\n    venue: \"arXiv (2605.00435)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.00435\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"将 mode collapse 重新解释为表示空间中的 geometric collapse：生成时模型内部轨迹被限制在低维子空间\"\n      - \"提出 RMR（Reinforced Mode Regulation），在 value cache 中抑制 dominant self-reinforcing directions\"\n    relevance_to_us: \"针对推理时 mode collapse，非迭代训练场景。但 'geometric collapse = 低维子空间坍缩' 与我们的 effective rank 指标在概念上有连接，可在 related work 中引用以说明 representation-space collapse 检测的跨场景通用性\"\n    metrics_studied: [\"effective rank proxy\", \"representation dimensionality\"]\n\n  - id: \"gauthier2026alignment\"\n    title: \"Explaining and Preventing Alignment Collapse in Iterative RLHF\"\n    authors: \"Gauthier, Bach, Jordan\"\n    venue: \"arXiv (2605.04266)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.04266\"\n    category: \"core-collapse\"\n    role: \"complementary\"\n    key_findings:\n      - \"迭代 RLHF 中 policy 生成 reward model 的训练数据形成反馈环路，导致 alignment collapse（policy 系统性利用 reward model 盲区）\"\n      - \"用 Stackelberg game 建模迭代 RLHF 的环路动力学，提出 FPO（foresighted policy optimization）\"\n    relevance_to_us: \"RLHF iterative feedback loop 与本项目 iterative synthetic data loop 结构类似——模型输出成为下一轮输入的反馈环路均导致系统性退化。其 'collapse = 反馈环路中的系统性退化' 叙事支持我们的大框架；Stackelberg game 视角可能启发 canary 的博弈论解释\"\n    metrics_studied: [\"alignment score\", \"reward model accuracy\"]\n\n  - id: \"shi2026pruning\"\n    title: \"Understanding Performance Collapse in Layer-Pruned LLMs via Decision Representation Transitions\"\n    authors: \"Shi et al.\"\n    venue: \"arXiv (2605.07271)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.07271\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"层剪枝导致的 performance collapse，定义 Silent Phase（模型预测被单一选项主导 = distributional collapse）和 Decisive Phase\"\n      - \"剪枝 Silent Phase 立即触发 collapse\"\n    relevance_to_us: \"架构剪枝 collapse，非数据驱动。其 'distributional collapse = 预测分布退化为单峰' 的操作定义与我们 token entropy 下降检测的是同一现象的不同表现\"\n    metrics_studied: [\"prediction distribution entropy\", \"task accuracy\"]\n\n  - id: \"tubingen2026diffusion\"\n    title: \"Layer Collapse in Diffusion Language Models\"\n    authors: \"Tübingen AI Center et al.\"\n    venue: \"arXiv (2605.06366)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.06366\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"LLaDA-8B 中发现层级 activation collapse：少数早期层的 activation 被单个 super-outlier 主导\"\n      - \"剪掉此 outlier 导致模型输出退化为重复随机 token\"\n    relevance_to_us: \"Diffusion LM 的架构 collapse，与迭代合成数据训练无关。但 activation collapse 的表征与 spectral collapse 有交集\"\n    metrics_studied: [\"activation magnitude\", \"output repetition\"]\n\n  # ============================================================\n  # CANARY / EARLY WARNING METRICS\n  # ============================================================\n  - id: \"chen2025scales\"\n    title: \"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios\"\n    authors: \"Anonymous\"\n    venue: \"arXiv (2510.05133)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.05133\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"**Calibration degradation precedes accuracy loss** — ECE 是 collapse 的 early warning signal\"\n      - \"20% synthetic data 以下性能稳定，30% 以上退化加速\"\n      - \"大模型（6.9B-12B）比小模型（410M-1.4B）更鲁棒\"\n      - \"推理任务比检索任务更易退化\"\n      - \"iteration 1 + 30% synthetic 时 ECE 从 0.08 升至 0.14（+75%）\"\n    relevance_to_us: \"**最直接的竞争者/先驱**。证实 ECE 可作为 canary，但未做 lead-lag 分析，未建立多指标 panel 框架\"\n    metrics_studied: [\"ECE\", \"accuracy\", \"perplexity\"]\n\n  - id: \"gambetta2024surplexity\"\n    title: \"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI\"\n    authors: \"Daniele Gambetta et al.\"\n    venue: \"arXiv (2410.12341)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.12341\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"提出 surplexity（model surprise 度量）同时用于检测 collapse 和过滤训练数据\"\n      - \"用 semantic networks 分析文本重复性和语义多样性\"\n      - \"用 next-token probability 定量衡量 diversity loss\"\n      - \"高 surplexity 过滤策略至少与 human-data baseline 同效，且更能降低分布偏斜\"\n      - \"不需要区分 human vs AI-generated data\"\n    relevance_to_us: \"surplexity 可作为我们 canary 指标候选之一；其 semantic network 方法提供了 diversity 度量的另一视角\"\n    metrics_studied: [\"surplexity\", \"semantic network metrics\", \"next-token probability\"]\n\n  - id: \"qiu2025spectral\"\n    title: \"Spectral Alignment as Predictor of Loss Explosion in Neural Network Training\"\n    authors: \"Haiquan Qiu, You Wu, Yingjie Tan, Yaqing Wang, Quanming Yao\"\n    venue: \"arXiv (2510.04202)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04202\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"Spectral Alignment (SA) 监控层输入与权重矩阵主奇异向量的分布对齐\"\n      - \"SA sign diversity collapse 是 representational collapse 和训练发散的早期预测器\"\n      - \"比 weight norm、gradient norm 等传统指标更早、更清晰地检测到训练失败\"\n      - \"健康层的 SA 应有正负均衡分布，collapse 到单侧则预示不稳定\"\n    relevance_to_us: \"SA 是潜在的高价值 canary 指标——专门设计为 early warning，可直接纳入我们的指标 panel\"\n    metrics_studied: [\"spectral alignment\", \"weight norm\", \"gradient norm\"]\n\n  - id: \"he2025closer\"\n    title: \"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\"\n    authors: \"Shiliang He et al.\"\n    venue: \"NeurIPS 2025 (Spotlight)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2509.16499\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"识别 diffusion model collapse 中的 generalization → memorization 转变\"\n      - \"**训练数据的 entropy 递减是 collapse 的直接驱动因素和清晰指标**\"\n      - \"提出基于 entropy 的数据选择策略，有效缓解 collapse\"\n    relevance_to_us: \"data entropy 作为 canary 的有效性已被验证（diffusion domain）；需测试是否在 LLM 场景同样有效\"\n    metrics_studied: [\"entropy\", \"FID\", \"diversity\"]\n\n  - id: \"ba2024fill\"\n    title: \"Fill In The Gaps: Model Calibration and Generalization with Synthetic Data\"\n    authors: \"Yang Ba, Michelle V Mancenido, Rong Pan\"\n    venue: \"EMNLP 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.10864\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"用 LLM 生成合成数据来修复 calibration 错误的 reliability diagram bins\"\n      - \"推导了基于 PAC 框架的 ECE bound\"\n      - \"合成数据可改善 calibration 但需精心设计生成策略\"\n    relevance_to_us: \"ECE 的理论 bound 可为我们的 canary 阈值设定提供理论依据\"\n    metrics_studied: [\"ECE\", \"accuracy\"]\n\n  - id: \"sigma2026spectral\"\n    title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n    authors: \"Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\"\n    venue: \"arXiv (2601.03385)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2601.03385\"\n    category: \"canary-metrics\"\n    role: \"direct-competitor\"\n    key_findings:\n      - \"基于 embedding Gram matrix 谱分析的 collapse 监控框架：Track I（确定性谱界）保守但鲁棒，Track II（随机谱缩放）灵敏但需采样\"\n      - \"Track I/II 的分歧本身是 early-stage collapse 的诊断信号，早于表面重复性伪影\"\n      - \"随机谱界使部分观测的 Gram matrix 也可用于大规模模型的可扩展监控\"\n    relevance_to_us: \"最直接的 spectral canary 竞争者。我们的 effective rank 是其简化版（单一标量 vs 完整谱界）；需在 related work 中明确差异：SIGMA 提供双轨谱界，我们用单一 effective rank 换取更低计算开销和多指标 panel 集成\"\n    gaps: \"未做 lead-lag 分析，未与 ECE/diversity 等非谱指标对比；Track I/II 的计算开销在 iterative loop 多轮场景下可能不可忽略\"\n    metrics_studied: [\"Gram matrix eigenspectrum\", \"spectral norm bounds\"]\n\n  - id: \"kalinowski2026topology\"\n    title: \"Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index\"\n    authors: \"Alexander Kalinowski\"\n    venue: \"arXiv (2604.26984)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.26984\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出基于 Modular Morse Homology Maintenance (MMHM) 的在线拓扑监控方案，增量更新避免每轮重建\"\n      - \"Collapse Index (CI) 组合多尺度拓扑特征，在 LLM fine-tuning 和 temporal KGE 训练中提供低延迟 early-warning\"\n      - \"拓扑方法捕捉表示空间的各向异性和多尺度结构丧失\"\n    relevance_to_us: \"topology-based monitoring 是与 spectral 方法正交的 collapse 检测路线。我们排除了该方法（计算开销高、可解释性弱），但 related work 需要对比说明选择 spectral/calibration panel 而非 topology 的理由\"\n    gaps: \"计算开销显著高于 effective rank 等标量指标；未在 iterative synthetic training loop 场景下测试；与 ECE 等轻量 canary 无对比\"\n    metrics_studied: [\"Collapse Index\", \"persistent homology features\"]\n\n  - id: \"bergsma2026scaling\"\n    title: \"Scaling with Collapse: Efficient and Predictable Training of LLM Families\"\n    authors: \"Bergsma et al.\"\n    venue: \"arXiv (2509.25087, rev. Mar 2026)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2509.25087\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"'Collapse' 此处指 loss curve 归一化后坍缩到通用轨迹（非 model collapse）\"\n      - \"deviation-from-collapse 作为训练病理的早期诊断信号\"\n    relevance_to_us: \"不同语境下的 'collapse'。但其 '偏离通用轨迹 = 训练出问题' 的监控思路与我们的 canary 理念相似——均从时序异常检测角度切入\"\n    metrics_studied: [\"loss curve deviation\", \"scaling law exponents\"]\n\n  # ============================================================\n  # DIVERSITY METRICS (BACKGROUND)\n  # ============================================================\n  - id: \"zhu2018texygen\"\n    title: \"Texygen: A Benchmarking Platform for Text Generation Models\"\n    authors: \"Yaoming Zhu et al.\"\n    venue: \"SIGIR 2018\"\n    year: 2018\n    url: \"https://arxiv.org/abs/1802.01886\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 Self-BLEU 度量：计算生成句子间的 BLEU 相似度，Self-BLEU 越高多样性越低\"\n      - \"成为文本生成多样性评估的标准基准之一\"\n    relevance_to_us: \"Self-BLEU 是我们 diversity canary 的经典候选\"\n    metrics_studied: [\"Self-BLEU\", \"BLEU\"]\n\n  - id: \"li2016diversity\"\n    title: \"A Diversity-Promoting Objective Function for Neural Conversation Models\"\n    authors: \"Jiwei Li et al.\"\n    venue: \"NAACL 2016\"\n    year: 2016\n    url: \"https://arxiv.org/abs/1510.03055\"\n    category: \"canary-metrics\"\n    role: \"background\"\n    key_findings:\n      - \"提出 distinct-1 / distinct-2 指标衡量生成文本的 n-gram 多样性\"\n      - \"计算 unique n-gram 数占总 n-gram 数的比例\"\n    relevance_to_us: \"distinct-n 是最廉价的 diversity canary 之一，计算开销极低\"\n    metrics_studied: [\"distinct-1\", \"distinct-2\"]\n\n  # ============================================================\n  # REPRESENTATION / SPECTRAL COLLAPSE\n  # ============================================================\n  - id: \"jing2022understanding\"\n    title: \"Understanding Dimensional Collapse in Contrastive Self-supervised Learning\"\n    authors: \"Li Jing et al.\"\n    venue: \"ICLR 2022\"\n    year: 2022\n    url: \"https://openreview.net/forum?id=YevsQ05DEN7\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"定义 dimensional collapse：embedding 向量只跨越低维子空间\"\n      - \"effective rank（基于归一化特征值 entropy 的指数）作为 collapse 度量\"\n      - \"strong augmentation 和 implicit regularization 驱动低秩解\"\n    relevance_to_us: \"effective rank 的定义和计算方式可直接迁移到我们的 embedding 空间监控\"\n    metrics_studied: [\"effective rank\", \"singular value spectrum\"]\n\n  - id: \"noci2024mind\"\n    title: \"Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers\"\n    authors: \"Lorenzo Noci et al.\"\n    venue: \"NeurIPS 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2410.07799\"\n    category: \"canary-metrics\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 Random Matrix Theory 分析 attention 层的 rank collapse\"\n      - \"发现 attention matrix 最大两个奇异值之间的 spectral gap 是 width-collapse 的根因\"\n      - \"rank collapse in depth: 所有 token 沿层收敛到单一表示\"\n    relevance_to_us: \"spectral gap 作为另一种 spectral canary 候选；其 RMT 分析框架可启发我们的理论工作\"\n    metrics_studied: [\"spectral gap\", \"singular values\", \"effective rank\"]\n\n  # ============================================================\n  # DATA MIXING & ACCUMULATION\n  # ============================================================\n  - id: \"kazdan2025collapse\"\n    title: \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"\n    authors: \"Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, Sanmi Koyejo\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2410.16713\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"系统对比 replace vs accumulate 场景\"\n      - \"replace → collapse；accumulate → 可避免 collapse\"\n      - \"发现 real data 和 synthetic data 之间存在非平凡的交互效应\"\n      - \"synthetic data 的价值取决于 real data 的绝对数量\"\n    relevance_to_us: \"直接对应我们的 alpha（mixing ratio）实验维度；其 replace vs accumulate 框架是我们实验设计的重要参考\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"dey2024breaking\"\n    title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n    authors: \"Apratim Dey, David Donoho, et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.01413\"\n    category: \"data-mixing\"\n    role: \"foundation\"\n    key_findings:\n      - \"替换数据 → 发散 population risk；累积数据 → 避免发散\"\n      - \"证明累积策略在多种模型（GMM, HMM, LLM）上有效\"\n    relevance_to_us: \"为我们的 alpha 实验提供理论预测：累积 vs 替换是 collapse 速率的关键调节因子\"\n    metrics_studied: [\"population risk\"]\n\n  - id: \"seddik2024howbad\"\n    title: \"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse\"\n    authors: \"Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane\"\n    venue: \"arXiv (2404.05090)\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.05090\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"纯合成数据训练不可避免 collapse\"\n      - \"给出 synthetic data 比例上界的估计——低于此比例可避免 collapse\"\n      - \"递归训练使原始分布尾部消失\"\n    relevance_to_us: \"其 mixing ratio 上界估计可对比我们实验中观测到的 canary 触发阈值\"\n    metrics_studied: [\"perplexity\"]\n\n  - id: \"fu2025selfconsuming\"\n    title: \"A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops\"\n    authors: \"Shi Fu, Yingjie Wang, Yuzhu Chen, Xinmei Tian, Dacheng Tao\"\n    venue: \"ICLR 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.18865\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"引入 recursive stability 概念，首次给出 self-consuming loop 的泛化分析\"\n      - \"恒定比例的真实数据即可保证 STL 收敛；同时给出最优合成数据量的 insight\"\n      - \"模型架构和 real/synthetic 数据比例共同决定 STL 的成败\"\n    relevance_to_us: \"为 post-MVP α-sweep（synthetic ratio 梯度）实验提供理论预期：50% accumulation 条件下收敛有理论保证\"\n    gaps: \"理论分析限于特定 generalization bound 框架，未涉及 canary 指标的行为；未讨论不同 α 下 collapse 速率的精细结构\"\n    metrics_studied: [\"generalization bound\", \"population risk\"]\n\n  - id: \"bakshi2026improvement\"\n    title: \"From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources\"\n    authors: \"Soham Bakshi, Sunrit Chakraborty\"\n    venue: \"arXiv (2602.10531)\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2602.10531\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"αt（每轮混合权重）trajectory 和 nt（每轮样本量）scaling 的交互决定三种 regime：collapse / improvement / consistency\"\n      - \"当 αt 衰减足够快且 nt 增长足够快时，迭代估计可收敛到真实分布（improvement regime）\"\n      - \"αt 衰减不足或 nt 增长不足则进入 collapse regime；边界条件给出 consistency regime\"\n      - \"在 next-token prediction 语言模型上分析完整迭代演化动态\"\n    relevance_to_us: \"αt/nt 条件直接对应我们 α-sweep 实验的理论预期：不同 synthetic ratio 衰减曲线下 canary 应呈现不同时序模式\"\n    gaps: \"理论结果基于渐近分析，有限代数下的 transient behavior 未充分刻画；未讨论哪些指标能区分三种 regime\"\n    metrics_studied: [\"population risk\", \"total variation distance\"]\n\n  - id: \"he2025golden\"\n    title: \"Golden Ratio Weighting Prevents Model Collapse\"\n    authors: \"Shiliang He, Zhongbin Xu, Yan Cheng\"\n    venue: \"arXiv (2502.18049)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.18049\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"最优 real data 权重在 Gaussian estimation、GLM、非参数估计中均收敛到黄金比例倒数 1/φ ≈ 0.618\"\n      - \"最优权重 w*(λ) 作为正则化参数的函数既非单调也非凸——risk landscape 在 mixing ratio 空间上本身不是单调的\"\n      - \"提供了 mixing ratio 非单调性的首个理论框架\"\n    relevance_to_us: \"我们在 α-sweep 中观测到的非单调 dose-response（α=0.25 比 α=0.50 collapse 更严重）可视为该理论在 diversity metrics 上的实证验证。论文 Discussion 的理论锚点。\"\n    gaps: \"理论基于线性回归和高斯分布，未直接推广到 LLM diversity metrics\"\n    metrics_studied: [\"population risk\", \"optimal weight\"]\n\n  - id: \"xu2025mixing\"\n    title: \"Preventing Model Collapse Under Overparametrization: Optimal Mixing Ratios\"\n    authors: \"Zhongbin Xu, Yan Cheng\"\n    venue: \"arXiv (2509.22341)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2509.22341\"\n    category: \"data-mixing\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"过参数化 regime（插值学习 + ridge 回归）中分析最优混合比例\"\n      - \"插值学习：最优 real data 比例收敛到 1/φ\"\n      - \"Ridge 回归：最优比例受谱几何控制，至少为 1/2\"\n      - \"w > 1/3 时 variance 随迭代单调递减；w < 1/3 时 variance 可能增长——存在临界阈值\"\n    relevance_to_us: \"1/3 临界阈值与我们 α=0.25（real weight=0.75 vs synthetic weight=0.25）处出现最强 collapse 的观测有概念对应。不同 regime 下 variance 行为质变支持我们的 regime-dependent 叙事。\"\n    gaps: \"参数空间不完全对齐（他们的 w 是 real data weight，我们的 α 是 synthetic ratio）；未讨论 diversity metrics\"\n    metrics_studied: [\"variance\", \"population risk\", \"optimal mixing ratio\"]\n\n  # ============================================================\n  # MITIGATION & VERIFICATION\n  # ============================================================\n  - id: \"feng2025escaping\"\n    title: \"Escaping Model Collapse via Synthetic Data Verification\"\n    authors: \"Yunzhen Feng et al.\"\n    venue: \"NeurIPS 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.16657\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"通过外部 verifier（human 或 better model）注入信息可避免 collapse\"\n      - \"verifier-guided retraining 带来短期改善，但最终收敛到 verifier 的 knowledge center\"\n      - \"除非 verifier 完全可靠，早期收益会 plateau 甚至逆转\"\n    relevance_to_us: \"verification 作为 intervention 策略——如果 canary 触发，可考虑此类 reactive intervention\"\n    metrics_studied: [\"test loss\"]\n\n  - id: \"barzilai2025consistency\"\n    title: \"When Models Don't Collapse: On the Consistency of Iterative MLE\"\n    authors: \"Daniel Barzilai, Ohad Shamir\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2505.19046\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"在标准 MLE 一致性假设下，即使 real data fraction 趋近零也可避免 collapse\"\n      - \"但证明了某些情况下 collapse 可以任意快地发生——首次给出严格 collapse 反例\"\n    relevance_to_us: \"理论上的 collapse 可发生任意快的结论强化了 early warning 的价值\"\n    metrics_studied: []\n\n  - id: \"dces2026counter\"\n    title: \"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling\"\n    authors: \"Anonymous\"\n    venue: \"MDPI Electronics (2026)\"\n    year: 2026\n    url: \"https://www.mdpi.com/2079-9292/15/4/869\"\n    category: \"data-mixing\"\n    role: \"background\"\n    key_findings:\n      - \"提出 DCES（dynamic center-edge sampling）数据选择框架\"\n      - \"DCES 在 ECE（0.1058 vs 0.1200）和 entropy 保持上优于随机选择\"\n    relevance_to_us: \"其 ECE 和 entropy 对比数据为我们的指标 baseline 提供参考\"\n    metrics_studied: [\"ECE\", \"entropy\"]\n\n  # ============================================================\n  # POSITION / SURVEY / EPISTEMICS\n  # ============================================================\n  - id: \"schaeffer2025position\"\n    title: \"Position: Model Collapse Does Not Mean What You Think\"\n    authors: \"Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, Sanmi Koyejo\"\n    venue: \"arXiv (2503.03150)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.03150\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"文献中实际包含 8 种不同且有时矛盾的 model collapse 定义\"\n      - \"许多 collapse 预测依赖于与现实不符的假设\"\n      - \"多种 collapse 场景是可以轻易避免的\"\n    relevance_to_us: \"提醒我们明确定义 collapse 的操作标准；不同定义可能需要不同的 canary 指标\"\n    metrics_studied: []\n\n  - id: \"wright2025epistemic\"\n    title: \"Epistemic Diversity and Knowledge Collapse in Large Language Models\"\n    authors: \"Wright, Dustin and Masud, Sarah and Moore, Jared and Yadav, Srishti and Antoniak, Maria and Park, Chan Young and Augenstein, Isabelle\"\n    venue: \"arXiv (2510.04226)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.04226\"\n    category: \"core-collapse\"\n    role: \"background\"\n    key_findings:\n      - \"27 个 LLM 在 155 个主题上的 epistemic diversity 评估\"\n      - \"所有模型的 epistemic diversity 低于基本 web 搜索\"\n      - \"模型越大 epistemic diversity 反而越低；RAG 有正面效果\"\n    relevance_to_us: \"knowledge collapse 维度可扩展我们对 diversity canary 的理解——不仅是 lexical/syntactic 还有 epistemic\"\n    metrics_studied: [\"epistemic diversity\"]\n\n  # ============================================================\n  # METHODOLOGY (GRANGER / LEAD-LAG)\n  # ============================================================\n  - id: \"shojaie2022granger\"\n    title: \"Granger Causality: A Review and Recent Advances\"\n    authors: \"Ali Shojaie, Emily B. Fox\"\n    venue: \"Annual Review of Statistics and Its Application\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2105.02675\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"Granger causality 综述：从经典线性到非线性/neural 方法\"\n      - \"Panel data 场景的 Granger causality 扩展\"\n      - \"VAR 和 neural Granger causality 的对比\"\n    relevance_to_us: \"为我们的 panel Granger causality 分析提供方法论基础\"\n    metrics_studied: []\n\n  - id: \"marcinkevics2022neural\"\n    title: \"Granger Causality Using Neural Networks\"\n    authors: \"Raphael Marcinkevics, Julia Vogt\"\n    venue: \"arXiv (2208.03703)\"\n    year: 2022\n    url: \"https://arxiv.org/abs/2208.03703\"\n    category: \"methodology\"\n    role: \"method-component\"\n    key_findings:\n      - \"用 neural network 估计 Granger causality，突破线性假设\"\n      - \"两个模型对比法：含/不含外生变量的预测误差差异即 Granger causality 证据\"\n    relevance_to_us: \"我们的多指标时序可能存在非线性关系，neural Granger causality 是自然选择\"\n    metrics_studied: []\n\n  # ============================================================\n  # EARLY WARNING SIGNALS / TIPPING POINTS (ECOLOGICAL THEORY)\n  # ============================================================\n  - id: \"scheffer2009early\"\n    title: \"Early-warning signals for critical transitions\"\n    authors: \"Marten Scheffer, Jordi Bascompte, William A. Brock, Victor Brovkin, Stephen R. Carpenter, Vasilis Dakos, Hermann Held, Egbert H. van Nes, Max Rietkerk, George Sugihara\"\n    venue: \"Nature\"\n    year: 2009\n    doi: \"10.1038/nature08227\"\n    category: \"early-warning-signals\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"复杂系统（生态、气候、金融）在临界转变前存在通用 early warning signals：critical slowing down 导致 autocorrelation 增加、variance 增加、recovery rate 降低\"\n      - \"这些 generic indicators 不依赖于系统具体机制，而是源于分岔点附近的数学共性\"\n      - \"综述了跨领域的 tipping point 检测方法，建立了 early warning signals 的理论框架\"\n    relevance_to_us: \"我们将 token entropy / diversity 下降类比为生态系统 tipping point 前的 early warning signal——diversity collapse 在概念上对应生态系统的 critical transition。Scheffer 的 generic indicator 框架为我们的 multi-metric canary panel 提供跨学科理论基础\"\n    one_line_finding: \"复杂系统临界转变前存在通用早期预警信号（critical slowing down），可跨领域检测 tipping point\"\n    metrics_studied: [\"autocorrelation\", \"variance\", \"recovery rate\"]\n\n  - id: \"scheffer2012anticipating\"\n    title: \"Anticipating Critical Transitions\"\n    authors: \"Marten Scheffer, Stephen R. Carpenter, Timothy M. Lenton, Jordi Bascompte, William Brock, Vasilis Dakos, Johan van de Koppel, Ingrid A. van de Leemput, Simon A. Levin, Egbert H. van Nes, Mercedes Pascual, John Vandermeer\"\n    venue: \"Science\"\n    year: 2012\n    doi: \"10.1126/science.1225244\"\n    category: \"early-warning-signals\"\n    role: \"theoretical-foundation\"\n    key_findings:\n      - \"整合两条研究线：(1) 揭示网络架构特征导致 tipping points 的结构性原因，(2) 发现接近临界阈值的通用经验指标\"\n      - \"Tipping points 既意味着 unwanted collapse 的风险，也意味着 positive change 的机会——关键在于预测能力\"\n      - \"提出将网络架构分析与经验预警指标结合的交叉方法论\"\n    relevance_to_us: \"将 early warning 从纯统计信号扩展到网络/架构分析——类比我们同时监控输出统计（ECE, entropy）和表征结构（effective rank, spectral）的多层 canary panel 设计。其 'architecture → tipping point' 分析呼应我们对模型内部表征 collapse 的关注\"\n    one_line_finding: \"结合网络架构分析与经验预警指标可更有效地预测复杂系统的临界转变\"\n    metrics_studied: [\"network architecture features\", \"empirical early warning indicators\"]\n\n  - id: \"boettiger2012limits\"\n    title: \"Quantifying Limits to Detection of Early Warning for Critical Transitions\"\n    authors: \"Carl Boettiger, Alan Hastings\"\n    venue: \"Journal of the Royal Society Interface\"\n    year: 2012\n    doi: \"10.1098/rsif.2012.0125\"\n    category: \"early-warning-signals\"\n    role: \"methodological-precedent\"\n    key_findings:\n      - \"用 likelihood ratio 框架量化 early warning signals 的统计检测力——在有限长度时间序列下，EWS 检测力极低\"\n      - \"即使系统确实在接近 tipping point，短时间序列中 autocorrelation 增加等 EWS 的统计显著性往往不足以拒绝零假设\"\n      - \"检测力取决于时间序列长度、噪声水平、接近临界点的速率——现实数据常处于低检测力 regime\"\n    relevance_to_us: \"与 Claim 3（方法选择敏感性）和 plan_009（TY power analysis, T=10 power=0.05-0.20）高度对齐。Boettiger & Hastings 从生态学角度量化了 EWS 在短时间序列下的统计极限，我们在 model collapse 迭代训练语境下独立发现了同样的问题——少数迭代轮次下 canary 检测力不足。他们的 power analysis 框架为我们的统计检测力论证提供了跨学科先例\"\n    one_line_finding: \"Early warning signals 在短时间序列下统计检测力极低，量化了 EWS 检测的基本统计极限\"\n    metrics_studied: [\"autocorrelation\", \"variance\", \"likelihood ratio\", \"statistical power\"]\n\ngaps:\n  - \"无人系统做过 canary 指标的 lead-lag / Granger causality 分析——现有工作只在事后观察到指标变化，未量化哪些指标能提前多少步预测 collapse\"\n  - \"ECE 在 collapse 场景下几乎未被系统研究——chen2025scales 是唯一报告 ECE 先于 accuracy 退化的工作，但未做因果分析\"\n  - \"embedding effective rank 未在 iterative synthetic training 场景下被测试——仅在 contrastive learning/transformer 训练中研究过\"\n  - \"多指标 panel 框架缺失——无人同时追踪 ECE + effective rank + diversity + perplexity 的时序行为并分析其 lead-lag 关系\"\n  - \"alpha（synthetic ratio）对 canary 灵敏度的影响未被研究——现有工作只关注 alpha 对最终性能的影响，不关注 canary 的 lead time 如何随 alpha 变化\"\n  - \"diversity dose-response 非单调性（α=0.25 比 α=0.50 collapse 更严重）无先例报告——He et al. 2025 从理论上预测 risk landscape 非单调，但无人在 LLM diversity 上实证验证\"\n  - \"predictive intervention vs reactive intervention 缺少对比——没有工作量化 early warning 带来的实际干预收益\"\n  - \"surplexity 和 spectral alignment 未在 iterative collapse 场景下交叉验证\"\n  - \"跨任务 canary 普适性未知——reasoning vs retrieval vs creative tasks 中哪些 canary 更可靠\"\n\nnovelty_assessment: |\n  我们项目的核心 novelty 在于：\n\n  1. **Panel Granger Causality 框架**：首次将多指标时序数据的因果分析方法应用于 model collapse 早期预警。\n     现有工作（chen2025scales, gambetta2024surplexity）只是事后观察到某些指标先变化，\n     但没有人做过系统的 lead-lag 量化分析。\n\n  2. **多指标 Canary Panel**：同时追踪 ECE、effective rank、Self-BLEU/distinct-n、\n     perplexity、entropy、surplexity 等指标，分析其相互关系和各自的 lead time。\n     现有工作都是单一指标或最多两三个指标的孤立分析。\n\n  3. **alpha-dependent Canary Sensitivity**：系统研究 synthetic ratio 如何影响各 canary\n     指标的灵敏度和 lead time。dohmatob2025strong 证明极小的 alpha 就能触发 collapse，\n     但没人研究 canary 在不同 alpha 下的行为。\n\n  4. **与已有工作的差异**：\n     - vs chen2025scales: 他们发现 ECE 先退化但没有做因果分析；我们用 Granger causality 量化\n     - vs gambetta2024surplexity: 他们提出 surplexity 用于检测和缓解 collapse；\n       我们将其纳入更广的 panel 并研究其 lead-lag 特性\n     - vs he2025closer: 他们在 diffusion 中用 entropy 作为指标；我们在 LLM 中测试更多指标\n     - vs qiu2025spectral: 他们的 SA 用于训练 loss explosion 预警；\n       我们将类似思路迁移到 iterative collapse 场景\n\n  5. **潜在风险**：chen2025scales 已经非常接近我们的方向。如果他们扩展到 lead-lag 分析，\n     我们的 novelty 会被削弱。需要快速推进并在方法论（Granger causality）上建立壁垒。\n",
      "numLines": 691,
      "startLine": 1,
      "totalLines": 691
    }
  },
  "sourceToolAssistantUUID": "7d050845-bdc0-426d-b65e-076a02656420",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "leafUuid": "24ba7bc8-70bb-42a3-bc57-a22fe244b118",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Write Related Work section for paper",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f"
}
```

---

### Assistant

_source line 23 · 2026-05-15T19:52:50.033Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me also check if the output directory exists and if there's already a file there.

Let me now write the Related Work section based on all the context I've gathered. Let me carefully craft the 4 paragraphs as specified:

1. Model collapse in iterative training (~250 words)
2. Canary metrics and collapse monitoring (~250 words)
3. Early-warning signals and critical transitions (~200 words)
4. Lead-lag methodology (~200 words)

Key constraints:
- PC14: no "consistently outperforms" / "state-of-the-art" / unqualified "significantly"


- Don't repeat Introduction content (Du et al. gap, Scheffer motivation, 4 methodological deficiencies already mentioned)
- Related Work = positioning and contrast, no claims
- Avoid over-listing — one sentence per paper, focus on relation to this work
- Only use keys from references.bib
- ~900 words total

Now I'm verifying the bibliography keys I'll reference to make sure they're all available and correctly formatted. I'm checking the bibliography entry for this paper—the citation key is `dey2024breaking` but Gerstgrasser is listed as the first author, so depending on how I cite it, the rendered name will vary. Since the task mentions both "Dey et al." and "Gerstgrasser et al." interchangeably, I'll just use the citation key as-is.

Looking at what the Introduction already covers, I can see it references several foundational works on model collapse, early warning systems, and causal inference. For the Related Work section, I need to expand on these references with more depth and position each one relative to our contributions, rather than just repeating what's already been established in the Introduction.

The key distinction I'm tracking is how our work differs from Du et al. on four methodological fronts: we're doing a systematic comparison across multiple metrics, we're cross-validating methods and examining sensitivity to d_max, we're mapping how effectiveness varies across different regimes, and we're treating method selection sensitivity itself as a core contribution rather than a side observation.

I should be careful not to overstate claims or use strong language, and I'm aiming for around 900 words while keeping the narrative distinct from what the Introduction already established about the gap in the literature.

For the Toda-Yamamoto approach, I notice there's no specific citation in the references, so I'll describe it as a variant of Granger causality that handles integrated processes rather than trying to cite something that isn't there. I should frame the Related Work section by examining what each existing work does and doesn't do methodologically, rather than just restating the four deficiencies the Introduction already laid out.

Let me check if there's already a related_work.tex file to build on.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24ba7bc8-70bb-42a3-bc57-a22fe244b118",
  "isSidechain": false,
  "requestId": "req_011Cb4wMk7RgXxhsUwMAq2Xg",
  "type": "assistant",
  "uuid": "3b0ca858-5b51-4457-ab07-cf86094d7529",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8T7rwoGSVS5JBTpRpk1BM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30975,
      "cache_read_input_tokens": 25102,
      "output_tokens": 1545,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1545,
          "cache_read_input_tokens": 25102,
          "cache_creation_input_tokens": 30975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30975
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

_source line 24 · 2026-05-15T19:52:50.314Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01GfahmherF48MkKM5aZ6b4a`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex 2>/dev/null; echo \"---\"; ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/",
  "description": "Check if related_work.tex exists and list paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b0ca858-5b51-4457-ab07-cf86094d7529",
  "isSidechain": false,
  "requestId": "req_011Cb4wMk7RgXxhsUwMAq2Xg",
  "type": "assistant",
  "uuid": "c45ead31-a920-48a0-a9c4-f1212bcd62f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8T7rwoGSVS5JBTpRpk1BM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30975,
      "cache_read_input_tokens": 25102,
      "output_tokens": 1545,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 30975,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1545,
          "cache_read_input_tokens": 25102,
          "cache_creation_input_tokens": 30975,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 30975
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

_source line 25 · 2026-05-15T19:52:50.444Z_

<details><summary>↩ Tool result · `toolu_01GfahmherF48MkKM5aZ6b4a`</summary>

```text
---
background.tex
experiments.tex
introduction.tex
method.tex
references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c45ead31-a920-48a0-a9c4-f1212bcd62f9",
  "isSidechain": false,
  "promptId": "bc9d0e00-4871-4d43-b046-0cec4ce72249",
  "type": "user",
  "uuid": "857258aa-1236-4447-9caf-1ca2ca6efb74",
  "toolUseResult": {
    "stdout": "---\nbackground.tex\nexperiments.tex\nintroduction.tex\nmethod.tex\nreferences.bib",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "c45ead31-a920-48a0-a9c4-f1212bcd62f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-15T19:54:04.518Z_

<details><summary>Logged reasoning block</summary>

```text
The file doesn't exist yet. Let me create it. Let me now carefully draft the Related Work section.

Let me count citation keys per paragraph to make sure I'm within budget:

Paragraph 1 (Model collapse): shumailov2024curse, alemohammad2024mad, dohmatob2024tale, dohmatob2025strong, dey2024breaking, kazdan2025collapse, fu2025selfconsuming, guo2024linguistic, he2025golden, schaeffer2025position = 10

Paragraph 2 (Canary): du2026geometric, chen2025scales, sigma2026spectral, kalinowski2026topology, dces2026counter, gambetta2024surplexity = 6


Paragraph 3 (EWS): scheffer2009early, scheffer2012anticipating, boettiger2012limits, truong2025entropy = 4
Paragraph 4 (Methodology): granger1969investigating, shojaie2022granger = 2

That brings me to about 22 new citations total, which leaves plenty of room in my 40-45 citation budget. Several of these overlap with what I've already cited in the Introduction, so the truly novel citations being introduced here are fewer than that.

Wait, I need to reconsider what the task is actually asking for. It specifies counting only citations that appear for the first time in this section, not ones already cited earlier. Let me separate out what's genuinely new: the ones from the Introduction that I'm reusing don't count toward this section's budget. Looking at my new contributions, I have 8 from the first paragraph, and I'm partway through listing the rest. I'm parsing the citation budget constraint more carefully—it seems to mean the total citations across the whole paper should stay within 40-45, with this section contributing around 13 new ones, which feels appropriate without padding unnecessarily.

Now I'm ready to draft the Related Work section, keeping each citation to one focused sentence about its relevance, maintaining a clear 4-point distinction from Du et al., hitting around 900 words, and avoiding overclaimed language like "state-of-the-art" or unqualified "significantly."

Writing the Related Work section... VAEs, GMMs, and language models, and by \citet{alemohammad2024mad}, who demonstrated quality-diversity tradeoffs in self-consuming generative loops for image models.
Theoretical analyses have since sharpened these results: \citet{dohmatob2024tale} recast collapse as a change in scaling-law exponents, showing that even small fractions of synthetic data alter the effective scaling behavior, while \citet{dohmatob2025strong} proved that collapse can occur even when synthetic data constitutes a vanishingly small fraction of the training set.
The role of data accumulation has been a central theme. \citet{dey2024breaking} proved that accumulating data across generations---rather than replacing it---prevents divergence of population risk in GMMs, HMMs, and language models. \citet{kazdan2025collapse} systematically compared replace and accumulate regimes, showing that synthetic data value depends on the absolute quantity of co-present real data. Recent work by \citet{fu2025selfconsuming} established that maintaining a constant fraction of real data suffices for convergence under accumulation, while \citet{he2025golden} revealed that optimal real-data weighting converges to the golden-ratio inverse in Gaussian and GLM settings, with non-monotone risk landscapes that predict regime-dependent behavior. On the empirical side, \citet{guo2024linguistic} tracked progressive decline in lexical, syntactic, and semantic diversity across iterative fine-tuning generations, and \citet{schaeffer2025position} has catalogued multiple competing definitions of the phenomenon.

Now I'm seeing that the literature has identified eight distinct definitions of model collapse, which highlights why our framework needs to be explicit about what we're actually measuring. Recent work has proposed several monitoring metrics that can catch degradation early---calibration error tends to rise before accuracy drops, with studies showing ECE increases of 75% appearing at 30% synthetic contamination before accuracy becomes visibly affected. Beyond calibration, there are spectral approaches using embedding Gram matrices to detect divergence, and topological methods being developed as well.

The key limitation across all these approaches is methodological rigor: none of them properly test for genuine temporal precedence using differencing tests, none cross-validate across multiple statistical methods, and none correct for multiple comparisons. Our approach differs from the closest prior work in four key ways, starting with how we handle the temporal precedence question.

Now I'm moving into the theoretical foundations, looking at how early-warning signals from ecology and climate science provide the conceptual basis for using canary metrics to predict system failures. The core insight is that systems approaching critical transitions exhibit generic warning signs like rising autocorrelation and variance, independent of what specific system is collapsing.

The key constraint I'm identifying is that these early-warning methods have fundamental detection limits in short time series—a major problem for iterative training where we only have 5-20 generations of data, far fewer than the ecological datasets these methods were developed on. Recent work connects entropy collapse to phase transitions and shows whether classical warning signals even work depends on the system's universality class. The model collapse literature hasn't yet adopted these rigorous statistical tools or acknowledged the finite-sample constraints that make detecting lead-lag patterns genuinely difficult.

For the lead-lag analysis itself, I'm drawing on Granger causality as the standard framework, with modern extensions handling nonlinear relationships. The critical practical issue is that non-stationary time series—which we definitely have in iterative training—violate the assumptions of standard tests and produce false positives. The Toda-Yamamoto procedure fixes this by adjusting for integration order, but it's barely used in machine learning despite being standard in economics and neuroscience. Most existing canary studies just use visual inspection or basic correlation, which can't separate real temporal precedence from spurious trends driven by shared non-stationarity. I'm applying a more rigorous approach with five different tests.

To avoid over-relying on any single method, I'm requiring consensus across cross-correlation, standard Granger, Toda-Yamamoto, permutation Granger, and first-differenced regression before declaring a lead-lag relationship robust. This multi-method requirement directly tackles the problem where different tests give conflicting answers depending on their assumptions. I've verified the fourth methodological distinction about method-selection sensitivity and confirmed the paper avoids overclaiming language like "consistently outperforms" or "state-of-the-art." The Related Work section properly expands on the four-point comparison with Du et al. that the Introduction only hints at, providing substantive detail without redundancy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "857258aa-1236-4447-9caf-1ca2ca6efb74",
  "isSidechain": false,
  "requestId": "req_011Cb4wQkcXQ7vaJZk1mUChr",
  "type": "assistant",
  "uuid": "ba761ca6-fdae-4f7d-9648-55ad4d9828c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKZJ48xMQNP4TtueB59bW2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1576,
      "cache_read_input_tokens": 56077,
      "output_tokens": 5016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1576,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5016,
          "cache_read_input_tokens": 56077,
          "cache_creation_input_tokens": 1576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1576
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

_source line 27 · 2026-05-15T19:54:04.520Z_

Now writing the section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba761ca6-fdae-4f7d-9648-55ad4d9828c4",
  "isSidechain": false,
  "requestId": "req_011Cb4wQkcXQ7vaJZk1mUChr",
  "type": "assistant",
  "uuid": "daba4af9-3f44-4244-b1ad-d58a88972706",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKZJ48xMQNP4TtueB59bW2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1576,
      "cache_read_input_tokens": 56077,
      "output_tokens": 5016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1576,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5016,
          "cache_read_input_tokens": 56077,
          "cache_creation_input_tokens": 1576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1576
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

_source line 28 · 2026-05-15T19:54:16.970Z_

<details open><summary>🔧 Tool call — Write · `toolu_01GM9RhVoHKW8KvdRJhRhs6i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Model collapse in iterative training.}\n\nThe phenomenon of iterative training collapse was formalized by \\citet{shumailov2024curse}, who showed that recursively replacing real data with model-generated text causes progressive tail erosion across VAEs, GMMs, and language models, and by \\citet{alemohammad2024mad}, who demonstrated quality--diversity tradeoffs in self-consuming generative loops for image models.\nTheoretical analyses have since sharpened these results: \\citet{dohmatob2024tale} recast collapse as a change in scaling-law exponents, showing that even small fractions of synthetic data alter effective scaling behavior, while \\citet{dohmatob2025strong} proved that collapse can occur even when synthetic data constitutes a vanishingly small fraction of the training set.\nThe role of data accumulation has been a central theme.\n\\citet{dey2024breaking} proved that accumulating data across generations---rather than replacing it---prevents divergence of population risk in GMMs, HMMs, and language models.\n\\citet{kazdan2025collapse} systematically compared replace and accumulate regimes, finding that synthetic data value depends on the absolute quantity of co-present real data.\n\\citet{fu2025selfconsuming} provided generalization bounds for self-consuming loops, establishing that a constant fraction of real data suffices for convergence under accumulation.\nOn the calibration side, \\citet{he2025golden} showed that optimal real-data weighting converges to the golden-ratio inverse ($1/\\varphi \\approx 0.618$) in Gaussian and GLM settings, and that the risk landscape is non-monotone in mixing ratio---a theoretical prediction with implications for regime-dependent canary behavior.\nBeyond distributional statistics, \\citet{guo2024linguistic} documented progressive decline in lexical, syntactic, and semantic diversity across iterative fine-tuning generations, providing the multi-level diversity metrics that serve as downstream targets in our lead-lag analysis.\n\\citet{schaeffer2025position} catalogued eight distinct and sometimes contradictory definitions of ``model collapse'' in the literature, underscoring the importance of explicit operational definitions---a concern our framework addresses by scoping canary prediction to diversity metrics specifically.\n\n\\paragraph{Canary metrics and collapse monitoring.}\n\nSeveral recent works have proposed monitoring metrics that precede or accompany distributional degradation during iterative training.\n\\citet{du2026geometric} observe that calibration error rises before accuracy degrades in iteratively trained language models, interpreting this through a geometric-regulation lens.\n\\citet{chen2025scales} report a similar pattern across model scales and mixing ratios, noting that ECE increases of 75\\% appear at 30\\% synthetic contamination before accuracy drops become visible.\nBeyond calibration, SIGMA~\\cite{sigma2026spectral} introduces a dual-track spectral framework based on embedding Gram matrices, where divergence between deterministic and stochastic spectral bounds serves as an early collapse diagnostic.\n\\citet{kalinowski2026topology} proposes a topological monitoring approach using persistent homology features to detect multi-scale structural loss in representation space.\nDCES~\\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal and reports improvements in ECE and entropy preservation.\n\\citet{gambetta2024surplexity} introduces surplexity---a surprise-based metric that simultaneously detects collapse and filters training data---demonstrating that high-surplexity selection matches human-data baselines in maintaining distributional balance.\n\nThese works collectively demonstrate growing interest in collapse monitoring, yet they share methodological limitations that weaken their lead-lag claims.\nNone apply differencing tests to distinguish genuine temporal precedence from spurious co-trending; none cross-validate findings across multiple statistical methods; and none apply false discovery rate correction when testing multiple metric pairs.\nOur work differs from the closest predecessor, \\citet{du2026geometric}, in four respects:\n(i)~we compare an entire family of canary metrics rather than a single metric pair;\n(ii)~we cross-validate each lead-lag relationship across five independent statistical methods and quantify sensitivity to method choice via $d_{\\max}$;\n(iii)~we map detectability as a function of contamination regime rather than reporting a single aggregate result; and\n(iv)~we treat method-selection sensitivity itself as a primary finding, showing that it is the dominant source of variation in existing lead-lag conclusions.\n\n\\paragraph{Early-warning signals and critical transitions.}\n\nThe theoretical foundation for canary-based prediction of system failure originates in ecology and climate science.\n\\citet{scheffer2009early} established that complex systems approaching tipping points exhibit generic early-warning signals---rising autocorrelation and variance due to critical slowing down---independent of system-specific mechanisms.\n\\citet{scheffer2012anticipating} extended this framework by combining empirical warning indicators with network-architecture analysis, arguing that structural and statistical signals together improve anticipatory power.\nCrucially, \\citet{boettiger2012limits} quantified the statistical detection limits of these signals, showing that early-warning power is often negligible in short time series---a constraint directly relevant to iterative training, where the number of generations (typically 5--20) is far smaller than typical ecological datasets.\n\\citet{truong2025entropy} connects entropy collapse to critical transitions, characterizing it as a first-order phase transition with universality classes that determine whether classical early-warning signals retain predictive power.\nThe model collapse literature has not yet imported these methodological tools: existing canary studies neither frame their claims in terms of detection power under finite samples nor test whether observed lead-lag patterns survive the short-series constraints that \\citet{boettiger2012limits} identified as fundamental.\n\n\\paragraph{Lead-lag methodology.}\n\nGranger causality~\\cite{granger1969investigating} provides the standard econometric framework for testing whether one time series improves prediction of another beyond its own history.\n\\citet{shojaie2022granger} review classical and modern extensions, including VAR-based tests, kernel methods, and neural approaches for nonlinear dependencies.\nA key practical issue is non-stationarity: standard Granger tests applied to integrated (unit-root) series produce inflated rejection rates.\nThe Toda--Yamamoto procedure addresses this by augmenting the VAR lag order by the integration order and testing only the original lags, yielding valid asymptotic inference regardless of cointegration structure.\nDespite wide use in economics and neuroscience, these methods are largely absent from the machine learning literature on iterative training.\nExisting canary studies rely on visual inspection or naive cross-correlation, which cannot distinguish genuine temporal precedence from shared non-stationary trends.\nOur framework applies five complementary methods---cross-correlation, standard Granger, Toda--Yamamoto, permutation Granger, and first-differenced regression---and requires multi-method consensus before classifying a lead-lag relationship as robust, directly addressing the method-sensitivity problem that arises when any single test is taken in isolation.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "daba4af9-3f44-4244-b1ad-d58a88972706",
  "isSidechain": false,
  "requestId": "req_011Cb4wQkcXQ7vaJZk1mUChr",
  "type": "assistant",
  "uuid": "ab813610-144f-44a0-b132-9e8cc2e65429",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BKZJ48xMQNP4TtueB59bW2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1576,
      "cache_read_input_tokens": 56077,
      "output_tokens": 5016,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1576,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5016,
          "cache_read_input_tokens": 56077,
          "cache_creation_input_tokens": 1576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1576
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

_source line 29 · 2026-05-15T19:54:16.991Z_

<details><summary>↩ Tool result · `toolu_01GM9RhVoHKW8KvdRJhRhs6i`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab813610-144f-44a0-b132-9e8cc2e65429",
  "isSidechain": false,
  "promptId": "bc9d0e00-4871-4d43-b046-0cec4ce72249",
  "type": "user",
  "uuid": "5f816042-d48f-4c0d-8599-37132399445c",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Model collapse in iterative training.}\n\nThe phenomenon of iterative training collapse was formalized by \\citet{shumailov2024curse}, who showed that recursively replacing real data with model-generated text causes progressive tail erosion across VAEs, GMMs, and language models, and by \\citet{alemohammad2024mad}, who demonstrated quality--diversity tradeoffs in self-consuming generative loops for image models.\nTheoretical analyses have since sharpened these results: \\citet{dohmatob2024tale} recast collapse as a change in scaling-law exponents, showing that even small fractions of synthetic data alter effective scaling behavior, while \\citet{dohmatob2025strong} proved that collapse can occur even when synthetic data constitutes a vanishingly small fraction of the training set.\nThe role of data accumulation has been a central theme.\n\\citet{dey2024breaking} proved that accumulating data across generations---rather than replacing it---prevents divergence of population risk in GMMs, HMMs, and language models.\n\\citet{kazdan2025collapse} systematically compared replace and accumulate regimes, finding that synthetic data value depends on the absolute quantity of co-present real data.\n\\citet{fu2025selfconsuming} provided generalization bounds for self-consuming loops, establishing that a constant fraction of real data suffices for convergence under accumulation.\nOn the calibration side, \\citet{he2025golden} showed that optimal real-data weighting converges to the golden-ratio inverse ($1/\\varphi \\approx 0.618$) in Gaussian and GLM settings, and that the risk landscape is non-monotone in mixing ratio---a theoretical prediction with implications for regime-dependent canary behavior.\nBeyond distributional statistics, \\citet{guo2024linguistic} documented progressive decline in lexical, syntactic, and semantic diversity across iterative fine-tuning generations, providing the multi-level diversity metrics that serve as downstream targets in our lead-lag analysis.\n\\citet{schaeffer2025position} catalogued eight distinct and sometimes contradictory definitions of ``model collapse'' in the literature, underscoring the importance of explicit operational definitions---a concern our framework addresses by scoping canary prediction to diversity metrics specifically.\n\n\\paragraph{Canary metrics and collapse monitoring.}\n\nSeveral recent works have proposed monitoring metrics that precede or accompany distributional degradation during iterative training.\n\\citet{du2026geometric} observe that calibration error rises before accuracy degrades in iteratively trained language models, interpreting this through a geometric-regulation lens.\n\\citet{chen2025scales} report a similar pattern across model scales and mixing ratios, noting that ECE increases of 75\\% appear at 30\\% synthetic contamination before accuracy drops become visible.\nBeyond calibration, SIGMA~\\cite{sigma2026spectral} introduces a dual-track spectral framework based on embedding Gram matrices, where divergence between deterministic and stochastic spectral bounds serves as an early collapse diagnostic.\n\\citet{kalinowski2026topology} proposes a topological monitoring approach using persistent homology features to detect multi-scale structural loss in representation space.\nDCES~\\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal and reports improvements in ECE and entropy preservation.\n\\citet{gambetta2024surplexity} introduces surplexity---a surprise-based metric that simultaneously detects collapse and filters training data---demonstrating that high-surplexity selection matches human-data baselines in maintaining distributional balance.\n\nThese works collectively demonstrate growing interest in collapse monitoring, yet they share methodological limitations that weaken their lead-lag claims.\nNone apply differencing tests to distinguish genuine temporal precedence from spurious co-trending; none cross-validate findings across multiple statistical methods; and none apply false discovery rate correction when testing multiple metric pairs.\nOur work differs from the closest predecessor, \\citet{du2026geometric}, in four respects:\n(i)~we compare an entire family of canary metrics rather than a single metric pair;\n(ii)~we cross-validate each lead-lag relationship across five independent statistical methods and quantify sensitivity to method choice via $d_{\\max}$;\n(iii)~we map detectability as a function of contamination regime rather than reporting a single aggregate result; and\n(iv)~we treat method-selection sensitivity itself as a primary finding, showing that it is the dominant source of variation in existing lead-lag conclusions.\n\n\\paragraph{Early-warning signals and critical transitions.}\n\nThe theoretical foundation for canary-based prediction of system failure originates in ecology and climate science.\n\\citet{scheffer2009early} established that complex systems approaching tipping points exhibit generic early-warning signals---rising autocorrelation and variance due to critical slowing down---independent of system-specific mechanisms.\n\\citet{scheffer2012anticipating} extended this framework by combining empirical warning indicators with network-architecture analysis, arguing that structural and statistical signals together improve anticipatory power.\nCrucially, \\citet{boettiger2012limits} quantified the statistical detection limits of these signals, showing that early-warning power is often negligible in short time series---a constraint directly relevant to iterative training, where the number of generations (typically 5--20) is far smaller than typical ecological datasets.\n\\citet{truong2025entropy} connects entropy collapse to critical transitions, characterizing it as a first-order phase transition with universality classes that determine whether classical early-warning signals retain predictive power.\nThe model collapse literature has not yet imported these methodological tools: existing canary studies neither frame their claims in terms of detection power under finite samples nor test whether observed lead-lag patterns survive the short-series constraints that \\citet{boettiger2012limits} identified as fundamental.\n\n\\paragraph{Lead-lag methodology.}\n\nGranger causality~\\cite{granger1969investigating} provides the standard econometric framework for testing whether one time series improves prediction of another beyond its own history.\n\\citet{shojaie2022granger} review classical and modern extensions, including VAR-based tests, kernel methods, and neural approaches for nonlinear dependencies.\nA key practical issue is non-stationarity: standard Granger tests applied to integrated (unit-root) series produce inflated rejection rates.\nThe Toda--Yamamoto procedure addresses this by augmenting the VAR lag order by the integration order and testing only the original lags, yielding valid asymptotic inference regardless of cointegration structure.\nDespite wide use in economics and neuroscience, these methods are largely absent from the machine learning literature on iterative training.\nExisting canary studies rely on visual inspection or naive cross-correlation, which cannot distinguish genuine temporal precedence from shared non-stationary trends.\nOur framework applies five complementary methods---cross-correlation, standard Granger, Toda--Yamamoto, permutation Granger, and first-differenced regression---and requires multi-method consensus before classifying a lead-lag relationship as robust, directly addressing the method-sensitivity problem that arises when any single test is taken in isolation.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "ab813610-144f-44a0-b132-9e8cc2e65429",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "leafUuid": "5f816042-d48f-4c0d-8599-37132399445c",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Write Related Work section for paper",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f"
}
```

---

### Assistant

_source line 32 · 2026-05-15T19:54:20.066Z_

Now verifying the output against the checklist.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f816042-d48f-4c0d-8599-37132399445c",
  "isSidechain": false,
  "requestId": "req_011Cb4wX12ceJ2owKyDxtW9B",
  "type": "assistant",
  "uuid": "65b89264-4e39-4d5f-b714-72e4a6b186e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KkR4mhPZ81eerU2ZAQgY95",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 57653,
      "output_tokens": 612,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 612,
          "cache_read_input_tokens": 57653,
          "cache_creation_input_tokens": 5067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5067
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

_source line 33 · 2026-05-15T19:54:26.206Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017uxv63MGfsGGrxX5bQrkuc`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper && echo \"=== 1. label check ===\" && grep -c 'label{sec:related_work}' related_work.tex && echo \"=== 2. all cite keys ===\" && grep -oP '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u && echo \"=== 3. verify keys in bib ===\" && for key in $(grep -oP '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//'); do grep -q \"$key\" references.bib && echo \"OK: $key\" || echo \"MISSING: $key\"; done && echo \"=== 4. forbidden phrases ===\" && grep -iE 'consistently outperforms|state-of-the-art|state of the art' related_work.tex || echo \"None found\" && grep -P '\\bsignificantly\\b' related_work.tex || echo \"No bare 'significantly'\" && echo \"=== 5. Du et al. 4 distinctions ===\" && grep -c '(i)' related_work.tex && grep -c '(ii)' related_work.tex && grep -c '(iii)' related_work.tex && grep -c '(iv)' related_work.tex && echo \"=== 6. word count ===\" && wc -w related_work.tex && echo \"=== 7. unique new cites (not in intro) ===\" && comm -23 <(grep -oP '\\\\cite[tp]?\\{[^}]+\\}' related_work.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u) <(grep -oP '\\\\cite[tp]?\\{[^}]+\\}' introduction.tex | tr ',' '\\n' | sed 's/.*{//;s/}.*//' | sort -u)",
  "description": "Verify related_work.tex against all checklist items"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65b89264-4e39-4d5f-b714-72e4a6b186e5",
  "isSidechain": false,
  "requestId": "req_011Cb4wX12ceJ2owKyDxtW9B",
  "type": "assistant",
  "uuid": "7c034aa4-eb00-4a13-972f-ca12f2de5366",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KkR4mhPZ81eerU2ZAQgY95",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5067,
      "cache_read_input_tokens": 57653,
      "output_tokens": 612,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5067,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 612,
          "cache_read_input_tokens": 57653,
          "cache_creation_input_tokens": 5067,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5067
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

_source line 34 · 2026-05-15T19:54:26.354Z_

<details><summary>↩ Tool result · `toolu_017uxv63MGfsGGrxX5bQrkuc`</summary>

```text
=== 1. label check ===
1
=== 2. all cite keys ===
alemohammad2024mad
boettiger2012limits
chen2025scales
dces2026counter
dey2024breaking
dohmatob2024tale
dohmatob2025strong
du2026geometric
fu2025selfconsuming
gambetta2024surplexity
granger1969investigating
guo2024linguistic
he2025golden
kalinowski2026topology
kazdan2025collapse
schaeffer2025position
scheffer2009early
scheffer2012anticipating
shojaie2022granger
shumailov2024curse
sigma2026spectral
truong2025entropy
=== 3. verify keys in bib ===
OK: shumailov2024curse
OK: alemohammad2024mad
OK: dohmatob2024tale
OK: dohmatob2025strong
OK: dey2024breaking
OK: kazdan2025collapse
OK: fu2025selfconsuming
OK: he2025golden
OK: guo2024linguistic
OK: schaeffer2025position
OK: du2026geometric
OK: chen2025scales
OK: sigma2026spectral
OK: kalinowski2026topology
OK: dces2026counter
OK: gambetta2024surplexity
OK: du2026geometric
OK: scheffer2009early
OK: scheffer2012anticipating
OK: boettiger2012limits
OK: truong2025entropy
OK: boettiger2012limits
OK: granger1969investigating
OK: shojaie2022granger
=== 4. forbidden phrases ===
None found
No bare 'significantly'
=== 5. Du et al. 4 distinctions ===
1
1
1
1
=== 6. word count ===
900 related_work.tex
=== 7. unique new cites (not in intro) ===
chen2025scales
dey2024breaking
dohmatob2024tale
dohmatob2025strong
fu2025selfconsuming
gambetta2024surplexity
granger1969investigating
guo2024linguistic
he2025golden
kalinowski2026topology
kazdan2025collapse
schaeffer2025position
truong2025entropy
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7c034aa4-eb00-4a13-972f-ca12f2de5366",
  "isSidechain": false,
  "promptId": "bc9d0e00-4871-4d43-b046-0cec4ce72249",
  "type": "user",
  "uuid": "b743c200-a596-425d-b1db-4e2eeb5f8124",
  "toolUseResult": {
    "stdout": "=== 1. label check ===\n1\n=== 2. all cite keys ===\nalemohammad2024mad\nboettiger2012limits\nchen2025scales\ndces2026counter\ndey2024breaking\ndohmatob2024tale\ndohmatob2025strong\ndu2026geometric\nfu2025selfconsuming\ngambetta2024surplexity\ngranger1969investigating\nguo2024linguistic\nhe2025golden\nkalinowski2026topology\nkazdan2025collapse\nschaeffer2025position\nscheffer2009early\nscheffer2012anticipating\nshojaie2022granger\nshumailov2024curse\nsigma2026spectral\ntruong2025entropy\n=== 3. verify keys in bib ===\nOK: shumailov2024curse\nOK: alemohammad2024mad\nOK: dohmatob2024tale\nOK: dohmatob2025strong\nOK: dey2024breaking\nOK: kazdan2025collapse\nOK: fu2025selfconsuming\nOK: he2025golden\nOK: guo2024linguistic\nOK: schaeffer2025position\nOK: du2026geometric\nOK: chen2025scales\nOK: sigma2026spectral\nOK: kalinowski2026topology\nOK: dces2026counter\nOK: gambetta2024surplexity\nOK: du2026geometric\nOK: scheffer2009early\nOK: scheffer2012anticipating\nOK: boettiger2012limits\nOK: truong2025entropy\nOK: boettiger2012limits\nOK: granger1969investigating\nOK: shojaie2022granger\n=== 4. forbidden phrases ===\nNone found\nNo bare 'significantly'\n=== 5. Du et al. 4 distinctions ===\n1\n1\n1\n1\n=== 6. word count ===\n900 related_work.tex\n=== 7. unique new cites (not in intro) ===\nchen2025scales\ndey2024breaking\ndohmatob2024tale\ndohmatob2025strong\nfu2025selfconsuming\ngambetta2024surplexity\ngranger1969investigating\nguo2024linguistic\nhe2025golden\nkalinowski2026topology\nkazdan2025collapse\nschaeffer2025position\ntruong2025entropy",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "7c034aa4-eb00-4a13-972f-ca12f2de5366",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35 · 2026-05-15T19:54:26.358Z_

```json
{
  "parentUuid": "b743c200-a596-425d-b1db-4e2eeb5f8124",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "186e8146-08b8-489d-b56f-aed1e5170046",
  "timestamp": "2026-05-15T19:54:26.358Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 36 · 2026-05-15T19:54:32.582Z_

All checks pass:

1. `\label{sec:related_work}` present
2. All 22 `\cite` keys verified in `references.bib` — zero missing
3. No forbidden phrases ("consistently outperforms", "state-of-the-art", bare "significantly")
4. Du et al. 4-point distinction (i)–(iv) all present
5. Word count: 900
6. 13 new citations introduced (not already in Introduction), well within budget

Section written to `docs/paper/related_work.tex` with 4 `\paragraph{}` blocks as specified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "186e8146-08b8-489d-b56f-aed1e5170046",
  "isSidechain": false,
  "requestId": "req_011Cb4wXh1B6FjLdZVZLPgDt",
  "type": "assistant",
  "uuid": "4ff8f357-2f27-4e53-835a-a7a0c793fec9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PgmKdSbVhmvd4mnjymoYLb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1282,
      "cache_read_input_tokens": 62720,
      "output_tokens": 145,
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
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 62720,
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

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "leafUuid": "4ff8f357-2f27-4e53-835a-a7a0c793fec9",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Write Related Work section for paper",
  "sessionId": "05ec08f8-52e4-4210-a7ed-efa1f9d51d3f"
}
```

---
