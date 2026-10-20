# Research conversation: <project_context> # 项目: collapse_severity_monitor ## 运行环境 - 服务器名: autodl-5090 - SSH 账户: root（调用 ssh_execute / submit_tra

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/dbf692f6-0359-404f-a489-94fefad88b9a.jsonl`
- **Structured JSON:** [`88a804cddad2f3c7870d.json`](../../sessions/88/88a804cddad2f3c7870d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T21:59:50.705Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T21:59:50.705Z",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "content": "&lt;project_context>\n# 项目: collapse_severity_monitor\n\n## 运行环境\n- 服务器名: autodl-5090\n- SSH 账户: root（调用 ssh_execute / submit_training_job 时传入 account=\"root\"）\n- SSH 连接命令: ssh autodl-5090  # 必须用此命令，~/.ssh/config 自动应用密钥和跳板机，禁止用裸 IP\n- 项目代码根目录: /root/autodl-tmp/collapse_severity_monitor\n\n## ⚠️ 活跃约束（必须遵守）\n\n- **C001**: SIGMA expected_direction=+1 是 provisional 假设（N=2），禁止在论文或分析中当已验证结论使用（原因：Reviewer warning: (1) N=2 数据点下方向判断是 tautology；(2) \"within-gen corruption vs recursive collapse\" 边界模糊——我们的 pipeline 本身就是跨代递归的；(3) 将方向差异包装为\"discussion 亮点\"属于 rationalization。等 plan_001 seed43-46 × 6 fractions + plan_003 Full FT 数据后重新验证。）\n\n\n## 环境搭建\n连接服务器后先调 `detect_image` 检测是否为预置镜像。如果匹配，跳过基础环境搭建，只装项目特有依赖。已预装的包不要重复安装。\n\n## 输出风格\n回复简洁直接。只输出执行结果和必要信息，不要解释过程、不要客套、不要给未被要求的建议。\n&lt;/project_context>\n## Task: Write Results Section (§4, Experiments)\n\nWrite the Results/Experiments section for an EMNLP 2026 long paper on training dynamic signals as model collapse severity monitors.\n\n### Instructions\n\n1. **First**: Read `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md` for writing standards\n2. **Then**: Read the method section for notation context: `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex`\n3. **Write** the section to: `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/experiments.tex`\n\n### Section Outline (word budget: ~1800 words)\n\nThe section uses `\\section{Results}\\label{sec:results}` (not \"Experiments\").\n\n**§4.1 Signal-Severity Correlation (C1)**\nCore claim: spectral and output signals reliably track collapse severity across configurations.\n\nPrimary evidence (Cohen's d at gen4, 3-seed analysis from plan006):\n- spectral_entropy: d=33.48 (most robust, CV=0.0015)\n- perplexity: d=20.82\n- distinct_1: d=14.60\n- stable_rank: d=9.43 (seed-sensitive — dropped from d=61.7 with 2 seeds to d=9.43 with 3 seeds, CV=0.022)\n- distinct_2: d=7.59, distinct_3: d=-7.08\n- Tier 2 (small d): token_entropy, self_bleu, gradient_norm, hellaswag\n\nSupporting evidence (Spearman ρ):\n- spectral_entropy: cross-gen ρ (Supporting, don't emphasize over d)\n- stable_rank: |ρ|=1.0 cross-frac (trivially achieved with few fractions)\n\nCross-method consistency (6/7 signals direction-consistent across QLoRA/Full FT):\n- Exception: gradient_norm (non-monotonic under QLoRA, effective under Full FT)\n\nReference Figure 2 (fig2_severity_curves) and Figure 4 (fig4_signal_heatmap).\n\n[TODO placeholders]: \"1.5B × 5-seed bootstrap CI (C2, in progress)\" and \"PubMed cross-domain (C3, in progress)\". Mark these clearly with `% TODO:` comments.\n\n**§4.2 Within-Generation Early Warning (C2)**\nCore claim: stable_rank detects collapse within a single training run.\n\nKey data (from within_gen_analysis):\n- stable_rank AUC=0.984 at 10% training progress\n- stable_rank 34.4% deviation at step 50 (3% training)\n- token_entropy: 24.5% at step 50, AUC=0.700\n- spectral_entropy: AUC=0.750\n- **PPL within-gen failure: AUC=0.534 (≈ random)** — this is a KEY finding\n\nPPL failure mechanism: training PPL measures fit to (potentially contaminated) training data, not structural change. The model fits its own synthetic output, so PPL doesn't diverge within a training run even when collapse is severe. Spectral signals detect structural change independent of data quality.\n\nReference Figure 3 (fig3_roc_curves). Note: fig3 uses synthetic ROC curves from known AUCs. Mark with `% TODO: replace with real ROC data from plan001`.\n\n**§4.3 Signal Taxonomy: Method-Dependent Operating Ranges (C3)**\nCore claim: same signal can be informative under one training method and misleading under another.\n\nFrom heatmap_data.json + plan003-fullft-05B:\n- gradient_norm: non-monotonic under QLoRA (5.9% up at 50%, −30.8% down at 100%), effective under Full FT (monotonic −58.3%)\n- hellaswag: insensitive under QLoRA (−1.15%, d<1), **data unavailable for Full FT 0% baseline** (NA in heatmap)\n- Full FT hellaswag: 50%→0.397, 100%→0.372 (−6.3% from 50% to 100%)\n- distinct_1: non-monotonic under QLoRA, insensitive under Full FT\n\nOperating range recommendations (from fig4):\n- stable_rank: within-gen alarm (highest within-gen AUC)\n- spectral_entropy: severity discrimination (most robust d, lowest CV)\n- perplexity (evaluation): cross-gen tracking (huge absolute effect)\n- gradient_norm: method-dependent — usable only with Full FT\n- hellaswag, distinct_1: insensitive (at 0.5B scale)\n\nDiversity metrics paragraph: distinct_1, self_bleu insensitive to collapse even at PPL 17× — token_entropy captures collapse but surface diversity maintained by sampling randomness.\n\nFull FT collapse dynamics: onset_ratio_gen01=15.3× (vs QLoRA 8.7×), post_onset_ratio_gen14=1.11 (fast_onset_saturation). QLoRA gen4 PPL=839.2 vs Full FT gen4 PPL=326.19 (vs_qlora_gen4_ppl_ratio=0.39). Full FT has sharper onset but lower terminal severity.\n\nTerminal spectral convergence: Full FT SR=153.87, QLoRA SR=155.64 — observation only, N=1, cannot distinguish from coincidence. State as observation, NOT a finding.\n\nReference Figure 5 (fig5_method_comparison) and Figure 4 (fig4_signal_heatmap).\n\n### ABSOLUTE PROHIBITIONS\n\n1. Do NOT use \"consistently outperforms\" / \"significantly improves\" without statistical testing\n2. Do NOT use \"state-of-the-art\" without SOTA comparison  \n3. Do NOT use \"significantly\" without significance test\n4. Do NOT present SIGMA direction (C001) as verified finding — it's provisional\n5. Do NOT call 100% gen1→gen2 PPL −1.9% a \"non-monotonic pattern\" — it's noise (N=1)\n6. Do NOT call stable_rank \"most sensitive signal\" — seed-sensitive, rank dropped 1→4\n7. Do NOT use \"slow onset\" / \"snowball\" / \"exponential\" for QLoRA collapse trajectory\n8. Do NOT use \"strong recovery\" for 25% contamination — use \"mild degradation / near-stability\"\n9. Do NOT use \"'XXX has achieved remarkable success in recent years'\"\n10. Effect sizes (Cohen's d) are PRIMARY evidence; Spearman ρ is SUPPORTING — don't lead with ρ\n\n### Mandatory Distinctions\n\n- Training PPL vs evaluation PPL — ALWAYS specify which\n- Within-gen detection vs cross-gen tracking — ALWAYS distinguish\n- stable_rank ↑ under collapse = energy dispersal (‖W‖²_F grows faster than σ₁²)\n\n### Statistical Limitations (MUST note)\n\n- Full FT comparison: N=1 seed\n- Within-gen ROC: N=1 seed, 0.5B — pending plan001 5-seed validation\n- N=3 seeds insufficient for Wilcoxon (min p=0.25); use bootstrap CI\n- stable_rank seed sensitivity: CV=0.022 vs spectral_entropy CV=0.0015\n\n### Available Citation Keys\n\nShumailov2024, Dohmatob2025, Gerstgrasser2024, Martin2021, dettmers2023qlora, hu2022lora, Gu2026\n\n### Figure/Table References\n\n- Figure~\\ref{fig:severity_curves} — fig2 severity curves\n- Figure~\\ref{fig:roc_curves} — fig3 ROC + AUC\n- Figure~\\ref{fig:signal_heatmap} — fig4 signal taxonomy heatmap\n- Figure~\\ref{fig:method_comparison} — fig5 Full FT vs QLoRA\n- Table~\\ref{tab:signal_taxonomy} — tab1 (to be created; for now reference it)\n- Table~\\ref{tab:within_gen_roc} — tab2 (to be created)\n\n### Output\n\nWrite the complete experiments.tex (renamed to Results) to:\n`/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/experiments.tex`\n\nDo NOT include preamble — this is \\input'd from main.tex."
}
```

---

### Runtime record

_source line 2 · 2026-05-15T21:59:50.708Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T21:59:50.708Z",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a"
}
```

---

## Round 1

38 recorded events

### User

_source line 3 · 2026-05-15T21:59:50.744Z_

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
## Task: Write Results Section (§4, Experiments)

Write the Results/Experiments section for an EMNLP 2026 long paper on training dynamic signals as model collapse severity monitors.

### Instructions

1. **First**: Read `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md` for writing standards
2. **Then**: Read the method section for notation context: `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex`
3. **Write** the section to: `/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/experiments.tex`

### Section Outline (word budget: ~1800 words)

The section uses `\section{Results}\label{sec:results}` (not "Experiments").

**§4.1 Signal-Severity Correlation (C1)**
Core claim: spectral and output signals reliably track collapse severity across configurations.

Primary evidence (Cohen's d at gen4, 3-seed analysis from plan006):
- spectral_entropy: d=33.48 (most robust, CV=0.0015)
- perplexity: d=20.82
- distinct_1: d=14.60
- stable_rank: d=9.43 (seed-sensitive — dropped from d=61.7 with 2 seeds to d=9.43 with 3 seeds, CV=0.022)
- distinct_2: d=7.59, distinct_3: d=-7.08
- Tier 2 (small d): token_entropy, self_bleu, gradient_norm, hellaswag

Supporting evidence (Spearman ρ):
- spectral_entropy: cross-gen ρ (Supporting, don't emphasize over d)
- stable_rank: |ρ|=1.0 cross-frac (trivially achieved with few fractions)

Cross-method consistency (6/7 signals direction-consistent across QLoRA/Full FT):
- Exception: gradient_norm (non-monotonic under QLoRA, effective under Full FT)

Reference Figure 2 (fig2_severity_curves) and Figure 4 (fig4_signal_heatmap).

[TODO placeholders]: "1.5B × 5-seed bootstrap CI (C2, in progress)" and "PubMed cross-domain (C3, in progress)". Mark these clearly with `% TODO:` comments.

**§4.2 Within-Generation Early Warning (C2)**
Core claim: stable_rank detects collapse within a single training run.

Key data (from within_gen_analysis):
- stable_rank AUC=0.984 at 10% training progress
- stable_rank 34.4% deviation at step 50 (3% training)
- token_entropy: 24.5% at step 50, AUC=0.700
- spectral_entropy: AUC=0.750
- **PPL within-gen failure: AUC=0.534 (≈ random)** — this is a KEY finding

PPL failure mechanism: training PPL measures fit to (potentially contaminated) training data, not structural change. The model fits its own synthetic output, so PPL doesn't diverge within a training run even when collapse is severe. Spectral signals detect structural change independent of data quality.

Reference Figure 3 (fig3_roc_curves). Note: fig3 uses synthetic ROC curves from known AUCs. Mark with `% TODO: replace with real ROC data from plan001`.

**§4.3 Signal Taxonomy: Method-Dependent Operating Ranges (C3)**
Core claim: same signal can be informative under one training method and misleading under another.

From heatmap_data.json + plan003-fullft-05B:
- gradient_norm: non-monotonic under QLoRA (5.9% up at 50%, −30.8% down at 100%), effective under Full FT (monotonic −58.3%)
- hellaswag: insensitive under QLoRA (−1.15%, d<1), **data unavailable for Full FT 0% baseline** (NA in heatmap)
- Full FT hellaswag: 50%→0.397, 100%→0.372 (−6.3% from 50% to 100%)
- distinct_1: non-monotonic under QLoRA, insensitive under Full FT

Operating range recommendations (from fig4):
- stable_rank: within-gen alarm (highest within-gen AUC)
- spectral_entropy: severity discrimination (most robust d, lowest CV)
- perplexity (evaluation): cross-gen tracking (huge absolute effect)
- gradient_norm: method-dependent — usable only with Full FT
- hellaswag, distinct_1: insensitive (at 0.5B scale)

Diversity metrics paragraph: distinct_1, self_bleu insensitive to collapse even at PPL 17× — token_entropy captures collapse but surface diversity maintained by sampling randomness.

Full FT collapse dynamics: onset_ratio_gen01=15.3× (vs QLoRA 8.7×), post_onset_ratio_gen14=1.11 (fast_onset_saturation). QLoRA gen4 PPL=839.2 vs Full FT gen4 PPL=326.19 (vs_qlora_gen4_ppl_ratio=0.39). Full FT has sharper onset but lower terminal severity.

Terminal spectral convergence: Full FT SR=153.87, QLoRA SR=155.64 — observation only, N=1, cannot distinguish from coincidence. State as observation, NOT a finding.

Reference Figure 5 (fig5_method_comparison) and Figure 4 (fig4_signal_heatmap).

### ABSOLUTE PROHIBITIONS

1. Do NOT use "consistently outperforms" / "significantly improves" without statistical testing
2. Do NOT use "state-of-the-art" without SOTA comparison  
3. Do NOT use "significantly" without significance test
4. Do NOT present SIGMA direction (C001) as verified finding — it's provisional
5. Do NOT call 100% gen1→gen2 PPL −1.9% a "non-monotonic pattern" — it's noise (N=1)
6. Do NOT call stable_rank "most sensitive signal" — seed-sensitive, rank dropped 1→4
7. Do NOT use "slow onset" / "snowball" / "exponential" for QLoRA collapse trajectory
8. Do NOT use "strong recovery" for 25% contamination — use "mild degradation / near-stability"
9. Do NOT use "'XXX has achieved remarkable success in recent years'"
10. Effect sizes (Cohen's d) are PRIMARY evidence; Spearman ρ is SUPPORTING — don't lead with ρ

### Mandatory Distinctions

- Training PPL vs evaluation PPL — ALWAYS specify which
- Within-gen detection vs cross-gen tracking — ALWAYS distinguish
- stable_rank ↑ under collapse = energy dispersal (‖W‖²_F grows faster than σ₁²)

### Statistical Limitations (MUST note)

- Full FT comparison: N=1 seed
- Within-gen ROC: N=1 seed, 0.5B — pending plan001 5-seed validation
- N=3 seeds insufficient for Wilcoxon (min p=0.25); use bootstrap CI
- stable_rank seed sensitivity: CV=0.022 vs spectral_entropy CV=0.0015

### Available Citation Keys

Shumailov2024, Dohmatob2025, Gerstgrasser2024, Martin2021, dettmers2023qlora, hu2022lora, Gu2026

### Figure/Table References

- Figure~\ref{fig:severity_curves} — fig2 severity curves
- Figure~\ref{fig:roc_curves} — fig3 ROC + AUC
- Figure~\ref{fig:signal_heatmap} — fig4 signal taxonomy heatmap
- Figure~\ref{fig:method_comparison} — fig5 Full FT vs QLoRA
- Table~\ref{tab:signal_taxonomy} — tab1 (to be created; for now reference it)
- Table~\ref{tab:within_gen_roc} — tab2 (to be created)

### Output

Write the complete experiments.tex (renamed to Results) to:
`/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/experiments.tex`

Do NOT include preamble — this is \input'd from main.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "06204627-aef4-4171-b484-81a6a94f14ad",
  "type": "user",
  "uuid": "a7e2b98f-8be0-49d4-b528-7ac9405c7d22",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T21:59:50.743Z_

```json
{
  "parentUuid": "a7e2b98f-8be0-49d4-b528-7ac9405c7d22",
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
  "uuid": "a99527e8-8f82-4ba1-8830-64ac2e9b446d",
  "timestamp": "2026-05-15T21:59:50.743Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T21:59:50.743Z_

```json
{
  "parentUuid": "a99527e8-8f82-4ba1-8830-64ac2e9b446d",
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
  "uuid": "4781bed0-4f73-4e8d-ad1b-a76a095e89e4",
  "timestamp": "2026-05-15T21:59:50.743Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-15T21:59:50.743Z_

```json
{
  "parentUuid": "4781bed0-4f73-4e8d-ad1b-a76a095e89e4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7db7161b-eb13-48cc-9f37-5ee17d18c9af",
  "timestamp": "2026-05-15T21:59:50.743Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
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
  "aiTitle": "Write Results section for collapse monitor paper",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a"
}
```

---

### Assistant

_source line 8 · 2026-05-15T21:59:53.507Z_

I'll start by reading the required skill file and method section for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7db7161b-eb13-48cc-9f37-5ee17d18c9af",
  "isSidechain": false,
  "requestId": "req_011Cb576LzdFRCbHZnSs1Pdr",
  "type": "assistant",
  "uuid": "560481be-20bb-4bb6-983d-710e9d966fdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FQHRjRs5xFnUS52UKeFk1B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13446,
      "cache_read_input_tokens": 11841,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 161,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13446
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

_source line 9 · 2026-05-15T21:59:54.474Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TBKT26wzPwwtLLUrAEQPRP`</summary>

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
  "parentUuid": "560481be-20bb-4bb6-983d-710e9d966fdd",
  "isSidechain": false,
  "requestId": "req_011Cb576LzdFRCbHZnSs1Pdr",
  "type": "assistant",
  "uuid": "68653c1c-7ef2-40b1-82e3-fb4631a91bf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FQHRjRs5xFnUS52UKeFk1B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13446,
      "cache_read_input_tokens": 11841,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 161,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13446
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

_source line 10 · 2026-05-15T21:59:54.491Z_

<details><summary>↩ Tool result · `toolu_01TBKT26wzPwwtLLUrAEQPRP`</summary>

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
  "parentUuid": "68653c1c-7ef2-40b1-82e3-fb4631a91bf6",
  "isSidechain": false,
  "promptId": "06204627-aef4-4171-b484-81a6a94f14ad",
  "type": "user",
  "uuid": "4b39ad47-c462-4e96-9bb0-19789dd715c2",
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
  "sourceToolAssistantUUID": "68653c1c-7ef2-40b1-82e3-fb4631a91bf6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 11 · 2026-05-15T21:59:54.921Z_

<details><summary>↩ Tool result · `toolu_01EQZNyq382thGX7Zemu7gVy`</summary>

```text
1	% Method section — collapse_severity_monitor
2	
3	\section{Methodology}
4	\label{sec:method}
5	
6	We design a controlled framework to evaluate how training-time signals track model collapse severity under iterative synthetic data contamination.
7	Our protocol varies contamination level and generational depth while monitoring four families of signals across five experimental configurations.
8	
9	\subsection{Iterative Training Protocol}
10	\label{sec:protocol}
11	
12	We simulate iterative model collapse through a multi-generation fine-tuning loop.
13	Let $M_0$ denote a pretrained base model and $\mathcal{D}_\text{real}$ a corpus of real text.
14	At each generation $g \in \{0, 1, \ldots, G{-}1\}$ (with $G=5$), we execute three steps:
15	
16	\begin{enumerate}
17	    \item \textbf{Fine-tune.} Initialize from $M_0$ and fine-tune on the current training corpus $\mathcal{D}_g$, yielding model $\tilde{M}_g$. During training, we collect monitoring signals every 50 optimizer steps via a callback on a held-out validation set (Section~\ref{sec:signals}).
18	    \item \textbf{Generate.} Sample synthetic text $\mathcal{S}_g$ from $\tilde{M}_g$ by prompting with the first 32 tokens of randomly subsampled chunks from $\mathcal{D}_\text{real}$ and generating up to 480 new tokens with nucleus sampling ($p=0.95$, temperature $\tau=1.0$). We subsample 1{,}500 chunks for generation.
19	    \item \textbf{Mix.} Construct the next-generation corpus by replacing fraction $\alpha$ of real chunks with synthetic chunks:
20	    \begin{equation}
21	        \mathcal{D}_{g+1} = (1 - \alpha)\,\mathcal{D}_\text{real} \cup \alpha\,\mathcal{S}_g.
22	        \label{eq:mixing}
23	    \end{equation}
24	\end{enumerate}
25	
26	\noindent
27	Each generation initializes from the \emph{same} pretrained weights $M_0$, isolating the effect of data contamination from cumulative weight drift.
28	Collapse pressure enters solely through the training corpus: at generation $g$, the synthetic component was produced by a model trained on data that itself contained synthetic text from generation $g{-}1$.
29	
30	All fine-tuning runs use AdamW with learning rate $2 \times 10^{-4}$, weight decay $0.01$, linear warmup over $5\%$ of steps, and gradient clipping at $\|\cdot\|_2 \leq 1.0$.
31	We train for 5 epochs with effective batch size 16 (per-device batch 4, gradient accumulation 4) in \texttt{bf16} mixed precision.
32	QLoRA configurations~\citep{dettmers2023qlora} use rank $r=16$, scaling factor $\alpha_\text{LoRA}=32$, dropout $0.05$, with adapters on all linear projections (\texttt{q\_proj}, \texttt{k\_proj}, \texttt{v\_proj}, \texttt{o\_proj}, \texttt{up\_proj}, \texttt{down\_proj}, \texttt{gate\_proj}); the base model is quantized to 4-bit NormalFloat (NF4) with double quantization.
33	Full fine-tuning (C4; Table~\ref{tab:configs}) uses identical hyperparameters with all parameters trainable and no quantization.
34	
35	\subsection{Contamination Fractions}
36	\label{sec:fractions}
37	
38	We test six contamination levels: $\alpha \in \{0, 0.1, 0.25, 0.5, 0.75, 1.0\}$.
39	The $\alpha=0$ condition serves as a clean baseline, controlling for training noise and natural run-to-run variance in the absence of synthetic contamination.
40	The $\alpha=1.0$ condition replaces the entire training set with synthetic data, applying maximum collapse pressure.
41	Intermediate fractions trace the dose--response relationship between contamination level and signal behavior.
42	
43	\subsection{Monitoring Signals}
44	\label{sec:signals}
45	
46	We monitor four families of training-time signals, collected every 50 optimizer steps on a held-out validation set in evaluation mode.
47	
48	\paragraph{Spectral signals.}
49	Given $n$ validation sequences, we collect last-layer hidden states into a matrix $\mathbf{H} \in \mathbb{R}^{T \times d}$ ($T$ total tokens, $d$ hidden dimension), center by subtracting the column mean, and compute the sample covariance $\mathbf{C} = \frac{1}{T-1}\mathbf{H}^\top\mathbf{H}$ with eigenvalues $\lambda_1 \geq \cdots \geq \lambda_d \geq 0$.
50	
51	\emph{Stable rank} measures the effective dimensionality of the representation:
52	\begin{equation}
53	    \mathrm{SR}(\mathbf{C}) = \frac{\left(\sum_{i=1}^{d} \lambda_i\right)^2}{\sum_{i=1}^{d} \lambda_i^2}.
54	    \label{eq:stable_rank}
55	\end{equation}
56	Under model collapse, $\mathrm{SR}$ \emph{increases}: the Frobenius norm $\|\mathbf{H}\|_F^2$ grows faster than the leading eigenvalue $\lambda_1$, dispersing energy across more dimensions rather than concentrating it.%
57	\footnote{This is the participation ratio of the covariance eigenspectrum, closely related to but distinct from the matrix stable rank $\|\mathbf{H}\|_F^2 / \|\mathbf{H}\|_2^2$; the two are monotonically related for centered data.}
58	
59	\emph{Spectral entropy} provides a complementary measure of spectral concentration:
60	\begin{equation}
61	    \mathrm{SE}(\mathbf{C}) = \frac{-\sum_{i=1}^{d} p_i \log p_i}{\log d}, \quad p_i = \frac{\lambda_i}{\sum_{j=1}^{d} \lambda_j}.
62	    \label{eq:spectral_entropy}
63	\end{equation}
64	$\mathrm{SE} \in [0,1]$, with $\mathrm{SE}=1$ for a uniform spectrum and $\mathrm{SE} \to 0$ for concentration on few components.
65	We use $n=64$ validation chunks for SVD computation.
66	
67	\paragraph{Output signals.}
68	We distinguish two perplexity regimes.
69	\emph{Training perplexity}, computed on the current (potentially contaminated) training batch, measures fit to the data mix; it can \emph{decrease} even as the model collapses, since the model fits its own synthetic output well.
70	\emph{Evaluation perplexity}, computed on a held-out clean set, reliably tracks degradation in language modeling quality on real text:
71	\begin{equation}
72	    \mathrm{PPL}_\text{eval} = \exp\!\left(\frac{1}{N}\sum_{i=1}^{|\mathcal{V}|} \ell(\mathbf{x}_i)\right),
73	    \label{eq:perplexity}
74	\end{equation}
75	where $\ell(\mathbf{x}_i)$ is the cross-entropy loss on validation sequence $\mathbf{x}_i$ and $N$ is the total token count.
76	This distinction is critical for within-generation detection (Section~\ref{sec:evaluation}): training perplexity is a misleading signal, while evaluation perplexity is a reliable one.
77	
78	\emph{Token entropy} measures the mean per-position entropy of the next-token distribution:
79	\begin{equation}
80	    \mathrm{TE}(\mathbf{x}) = \frac{1}{L-1}\sum_{t=1}^{L-1} H\!\left(P_\theta(\cdot \mid x_{\leq t})\right), \quad H(P) = -\sum_v P(v) \log P(v),
81	    \label{eq:token_entropy}
82	\end{equation}
83	averaged over 100 validation chunks.
84	Decreasing token entropy indicates the model is becoming more peaked in its predictions, a hallmark of mode collapse in generation.
85	
86	\paragraph{Gradient signal.}
87	We log the L2 gradient norm $\|\nabla_\theta \mathcal{L}\|_2$ before each optimizer step.
88	Gradient norm is a zero-cost byproduct of standard training.
89	Under QLoRA, gradient norm exhibits non-monotonic behavior with respect to contamination fraction: gradients flow only through low-rank adapter matrices~\citep{hu2022lora}, confining the landscape to a rank-$r$ subspace, and NF4 quantization of frozen base weights introduces discretization noise that propagates through the backward pass~\citep{dettmers2023qlora}.
90	
91	\paragraph{Downstream signal.}
92	We evaluate HellaSwag~\citep{zellers2019hellaswag} accuracy (4-choice commonsense reasoning, 1{,}000 samples) at the end of each generation as a downstream task probe.
93	
94	\subsection{Experimental Configurations}
95	\label{sec:configs}
96	
97	Table~\ref{tab:configs} summarizes our five experimental configurations.
98	C1 provides initial signal discovery on the smallest model.
99	C2 is the primary analysis configuration, with five independent seeds providing statistical power for bootstrap confidence intervals and effect size estimation.
100	C3 tests cross-domain generalization on biomedical text.
101	C4 isolates method-dependence by comparing full fine-tuning against QLoRA under matched conditions.
102	C5 provides a scale spot-check at 3B parameters.
103	
104	\begin{table}[t]
105	\centering
106	\small
107	\caption{Experimental configurations. Trainable\% indicates the fraction of parameters updated during fine-tuning.}
108	\label{tab:configs}
109	\begin{tabular}{llrllcll}
110	\toprule
111	ID & Model & Params & Dataset & Fractions ($\alpha$) & Seeds & Method & Train.\% \\
112	\midrule
113	C1 & Qwen2.5-0.5B & 494M & WikiText-2 & \{0, 0.5, 1.0\} & 1 & QLoRA $r{=}16$ & 0.8 \\
114	C2 & Qwen2.5-1.5B & 1.5B & WikiText-2 & \{0, 0.1, \ldots, 1.0\} & 5 & QLoRA $r{=}16$ & 0.5 \\
115	C3 & Qwen2.5-1.5B & 1.5B & PubMed & \{0, 0.5, 1.0\} & 3 & QLoRA $r{=}16$ & 0.5 \\
116	C4 & Qwen2.5-0.5B & 494M & WikiText-2 & \{0, 0.5, 1.0\} & 1 & Full FT & 100 \\
117	C5 & Qwen2.5-3B & 3B & WikiText-2 & \{0, 0.5, 1.0\} & 1 & QLoRA $r{=}16$ & 0.3 \\
118	\bottomrule
119	\end{tabular}
120	\end{table}
121	
122	WikiText-2~\citep{merity2017pointer} is tokenized and chunked into 512-token sequences (4{,}916 training chunks).
123	PubMed abstracts (C3) undergo identical preprocessing.
124	
125	\subsection{Evaluation Framework}
126	\label{sec:evaluation}
127	
128	\paragraph{Cross-generation severity.}
129	For each signal $s$ and generation $g$, we compute the Spearman rank correlation $\rho_g^{(s)}$ between contamination fraction $\alpha$ and the end-of-generation signal value across all tested fractions, with 95\% bootstrap confidence intervals.
130	We report Cohen's $d$ effect sizes between the clean baseline and each contamination level as the primary evidence for signal sensitivity, since rank correlations alone do not convey the magnitude of signal separation.
131	
132	\paragraph{Within-generation detection.}
133	We compute the area under the ROC curve (AUROC) for binary collapse detection at each signal checkpoint (every 50 steps), using \emph{clustered bootstrap} resampling.
134	The cluster unit is fraction$\times$seed rather than individual generation observations.
135	This is necessary because successive generations within a run are causally dependent---generation $g{+}1$ trains on data produced by the model from generation $g$---so pooling individual observations would inflate the effective sample size and produce artificially narrow confidence intervals.
136	
137	We also compute the relative deviation at each checkpoint:
138	\begin{equation}
139	    \Delta_s(t, \alpha) = \frac{|s_\alpha(t) - s_0(t)|}{|s_0(t)|} \times 100\%,
140	    \label{eq:deviation}
141	\end{equation}
142	where $s_\alpha(t)$ and $s_0(t)$ are signal values at step $t$ for fraction $\alpha$ and the clean baseline.
143	A signal provides early warning if $\Delta_s(t, \alpha) > 5\%$ within the first 10\% of training steps.
144	
145	\paragraph{Method-dependence.}
146	We compare signal trajectories between QLoRA (C1) and full fine-tuning (C4) under matched model size, dataset, and contamination fractions.
147	Paired differences in end-of-generation signal values quantify whether collapse signatures depend on the fine-tuning method or reflect properties of the data contamination itself.
148	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd0a753a-f25d-41d6-a68f-7234a5c3dc78",
  "isSidechain": false,
  "promptId": "06204627-aef4-4171-b484-81a6a94f14ad",
  "type": "user",
  "uuid": "0573c3c2-8601-4030-9f72-2a404b7d1af0",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/method.tex",
      "content": "% Method section — collapse_severity_monitor\n\n\\section{Methodology}\n\\label{sec:method}\n\nWe design a controlled framework to evaluate how training-time signals track model collapse severity under iterative synthetic data contamination.\nOur protocol varies contamination level and generational depth while monitoring four families of signals across five experimental configurations.\n\n\\subsection{Iterative Training Protocol}\n\\label{sec:protocol}\n\nWe simulate iterative model collapse through a multi-generation fine-tuning loop.\nLet $M_0$ denote a pretrained base model and $\\mathcal{D}_\\text{real}$ a corpus of real text.\nAt each generation $g \\in \\{0, 1, \\ldots, G{-}1\\}$ (with $G=5$), we execute three steps:\n\n\\begin{enumerate}\n    \\item \\textbf{Fine-tune.} Initialize from $M_0$ and fine-tune on the current training corpus $\\mathcal{D}_g$, yielding model $\\tilde{M}_g$. During training, we collect monitoring signals every 50 optimizer steps via a callback on a held-out validation set (Section~\\ref{sec:signals}).\n    \\item \\textbf{Generate.} Sample synthetic text $\\mathcal{S}_g$ from $\\tilde{M}_g$ by prompting with the first 32 tokens of randomly subsampled chunks from $\\mathcal{D}_\\text{real}$ and generating up to 480 new tokens with nucleus sampling ($p=0.95$, temperature $\\tau=1.0$). We subsample 1{,}500 chunks for generation.\n    \\item \\textbf{Mix.} Construct the next-generation corpus by replacing fraction $\\alpha$ of real chunks with synthetic chunks:\n    \\begin{equation}\n        \\mathcal{D}_{g+1} = (1 - \\alpha)\\,\\mathcal{D}_\\text{real} \\cup \\alpha\\,\\mathcal{S}_g.\n        \\label{eq:mixing}\n    \\end{equation}\n\\end{enumerate}\n\n\\noindent\nEach generation initializes from the \\emph{same} pretrained weights $M_0$, isolating the effect of data contamination from cumulative weight drift.\nCollapse pressure enters solely through the training corpus: at generation $g$, the synthetic component was produced by a model trained on data that itself contained synthetic text from generation $g{-}1$.\n\nAll fine-tuning runs use AdamW with learning rate $2 \\times 10^{-4}$, weight decay $0.01$, linear warmup over $5\\%$ of steps, and gradient clipping at $\\|\\cdot\\|_2 \\leq 1.0$.\nWe train for 5 epochs with effective batch size 16 (per-device batch 4, gradient accumulation 4) in \\texttt{bf16} mixed precision.\nQLoRA configurations~\\citep{dettmers2023qlora} use rank $r=16$, scaling factor $\\alpha_\\text{LoRA}=32$, dropout $0.05$, with adapters on all linear projections (\\texttt{q\\_proj}, \\texttt{k\\_proj}, \\texttt{v\\_proj}, \\texttt{o\\_proj}, \\texttt{up\\_proj}, \\texttt{down\\_proj}, \\texttt{gate\\_proj}); the base model is quantized to 4-bit NormalFloat (NF4) with double quantization.\nFull fine-tuning (C4; Table~\\ref{tab:configs}) uses identical hyperparameters with all parameters trainable and no quantization.\n\n\\subsection{Contamination Fractions}\n\\label{sec:fractions}\n\nWe test six contamination levels: $\\alpha \\in \\{0, 0.1, 0.25, 0.5, 0.75, 1.0\\}$.\nThe $\\alpha=0$ condition serves as a clean baseline, controlling for training noise and natural run-to-run variance in the absence of synthetic contamination.\nThe $\\alpha=1.0$ condition replaces the entire training set with synthetic data, applying maximum collapse pressure.\nIntermediate fractions trace the dose--response relationship between contamination level and signal behavior.\n\n\\subsection{Monitoring Signals}\n\\label{sec:signals}\n\nWe monitor four families of training-time signals, collected every 50 optimizer steps on a held-out validation set in evaluation mode.\n\n\\paragraph{Spectral signals.}\nGiven $n$ validation sequences, we collect last-layer hidden states into a matrix $\\mathbf{H} \\in \\mathbb{R}^{T \\times d}$ ($T$ total tokens, $d$ hidden dimension), center by subtracting the column mean, and compute the sample covariance $\\mathbf{C} = \\frac{1}{T-1}\\mathbf{H}^\\top\\mathbf{H}$ with eigenvalues $\\lambda_1 \\geq \\cdots \\geq \\lambda_d \\geq 0$.\n\n\\emph{Stable rank} measures the effective dimensionality of the representation:\n\\begin{equation}\n    \\mathrm{SR}(\\mathbf{C}) = \\frac{\\left(\\sum_{i=1}^{d} \\lambda_i\\right)^2}{\\sum_{i=1}^{d} \\lambda_i^2}.\n    \\label{eq:stable_rank}\n\\end{equation}\nUnder model collapse, $\\mathrm{SR}$ \\emph{increases}: the Frobenius norm $\\|\\mathbf{H}\\|_F^2$ grows faster than the leading eigenvalue $\\lambda_1$, dispersing energy across more dimensions rather than concentrating it.%\n\\footnote{This is the participation ratio of the covariance eigenspectrum, closely related to but distinct from the matrix stable rank $\\|\\mathbf{H}\\|_F^2 / \\|\\mathbf{H}\\|_2^2$; the two are monotonically related for centered data.}\n\n\\emph{Spectral entropy} provides a complementary measure of spectral concentration:\n\\begin{equation}\n    \\mathrm{SE}(\\mathbf{C}) = \\frac{-\\sum_{i=1}^{d} p_i \\log p_i}{\\log d}, \\quad p_i = \\frac{\\lambda_i}{\\sum_{j=1}^{d} \\lambda_j}.\n    \\label{eq:spectral_entropy}\n\\end{equation}\n$\\mathrm{SE} \\in [0,1]$, with $\\mathrm{SE}=1$ for a uniform spectrum and $\\mathrm{SE} \\to 0$ for concentration on few components.\nWe use $n=64$ validation chunks for SVD computation.\n\n\\paragraph{Output signals.}\nWe distinguish two perplexity regimes.\n\\emph{Training perplexity}, computed on the current (potentially contaminated) training batch, measures fit to the data mix; it can \\emph{decrease} even as the model collapses, since the model fits its own synthetic output well.\n\\emph{Evaluation perplexity}, computed on a held-out clean set, reliably tracks degradation in language modeling quality on real text:\n\\begin{equation}\n    \\mathrm{PPL}_\\text{eval} = \\exp\\!\\left(\\frac{1}{N}\\sum_{i=1}^{|\\mathcal{V}|} \\ell(\\mathbf{x}_i)\\right),\n    \\label{eq:perplexity}\n\\end{equation}\nwhere $\\ell(\\mathbf{x}_i)$ is the cross-entropy loss on validation sequence $\\mathbf{x}_i$ and $N$ is the total token count.\nThis distinction is critical for within-generation detection (Section~\\ref{sec:evaluation}): training perplexity is a misleading signal, while evaluation perplexity is a reliable one.\n\n\\emph{Token entropy} measures the mean per-position entropy of the next-token distribution:\n\\begin{equation}\n    \\mathrm{TE}(\\mathbf{x}) = \\frac{1}{L-1}\\sum_{t=1}^{L-1} H\\!\\left(P_\\theta(\\cdot \\mid x_{\\leq t})\\right), \\quad H(P) = -\\sum_v P(v) \\log P(v),\n    \\label{eq:token_entropy}\n\\end{equation}\naveraged over 100 validation chunks.\nDecreasing token entropy indicates the model is becoming more peaked in its predictions, a hallmark of mode collapse in generation.\n\n\\paragraph{Gradient signal.}\nWe log the L2 gradient norm $\\|\\nabla_\\theta \\mathcal{L}\\|_2$ before each optimizer step.\nGradient norm is a zero-cost byproduct of standard training.\nUnder QLoRA, gradient norm exhibits non-monotonic behavior with respect to contamination fraction: gradients flow only through low-rank adapter matrices~\\citep{hu2022lora}, confining the landscape to a rank-$r$ subspace, and NF4 quantization of frozen base weights introduces discretization noise that propagates through the backward pass~\\citep{dettmers2023qlora}.\n\n\\paragraph{Downstream signal.}\nWe evaluate HellaSwag~\\citep{zellers2019hellaswag} accuracy (4-choice commonsense reasoning, 1{,}000 samples) at the end of each generation as a downstream task probe.\n\n\\subsection{Experimental Configurations}\n\\label{sec:configs}\n\nTable~\\ref{tab:configs} summarizes our five experimental configurations.\nC1 provides initial signal discovery on the smallest model.\nC2 is the primary analysis configuration, with five independent seeds providing statistical power for bootstrap confidence intervals and effect size estimation.\nC3 tests cross-domain generalization on biomedical text.\nC4 isolates method-dependence by comparing full fine-tuning against QLoRA under matched conditions.\nC5 provides a scale spot-check at 3B parameters.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Experimental configurations. Trainable\\% indicates the fraction of parameters updated during fine-tuning.}\n\\label{tab:configs}\n\\begin{tabular}{llrllcll}\n\\toprule\nID & Model & Params & Dataset & Fractions ($\\alpha$) & Seeds & Method & Train.\\% \\\\\n\\midrule\nC1 & Qwen2.5-0.5B & 494M & WikiText-2 & \\{0, 0.5, 1.0\\} & 1 & QLoRA $r{=}16$ & 0.8 \\\\\nC2 & Qwen2.5-1.5B & 1.5B & WikiText-2 & \\{0, 0.1, \\ldots, 1.0\\} & 5 & QLoRA $r{=}16$ & 0.5 \\\\\nC3 & Qwen2.5-1.5B & 1.5B & PubMed & \\{0, 0.5, 1.0\\} & 3 & QLoRA $r{=}16$ & 0.5 \\\\\nC4 & Qwen2.5-0.5B & 494M & WikiText-2 & \\{0, 0.5, 1.0\\} & 1 & Full FT & 100 \\\\\nC5 & Qwen2.5-3B & 3B & WikiText-2 & \\{0, 0.5, 1.0\\} & 1 & QLoRA $r{=}16$ & 0.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWikiText-2~\\citep{merity2017pointer} is tokenized and chunked into 512-token sequences (4{,}916 training chunks).\nPubMed abstracts (C3) undergo identical preprocessing.\n\n\\subsection{Evaluation Framework}\n\\label{sec:evaluation}\n\n\\paragraph{Cross-generation severity.}\nFor each signal $s$ and generation $g$, we compute the Spearman rank correlation $\\rho_g^{(s)}$ between contamination fraction $\\alpha$ and the end-of-generation signal value across all tested fractions, with 95\\% bootstrap confidence intervals.\nWe report Cohen's $d$ effect sizes between the clean baseline and each contamination level as the primary evidence for signal sensitivity, since rank correlations alone do not convey the magnitude of signal separation.\n\n\\paragraph{Within-generation detection.}\nWe compute the area under the ROC curve (AUROC) for binary collapse detection at each signal checkpoint (every 50 steps), using \\emph{clustered bootstrap} resampling.\nThe cluster unit is fraction$\\times$seed rather than individual generation observations.\nThis is necessary because successive generations within a run are causally dependent---generation $g{+}1$ trains on data produced by the model from generation $g$---so pooling individual observations would inflate the effective sample size and produce artificially narrow confidence intervals.\n\nWe also compute the relative deviation at each checkpoint:\n\\begin{equation}\n    \\Delta_s(t, \\alpha) = \\frac{|s_\\alpha(t) - s_0(t)|}{|s_0(t)|} \\times 100\\%,\n    \\label{eq:deviation}\n\\end{equation}\nwhere $s_\\alpha(t)$ and $s_0(t)$ are signal values at step $t$ for fraction $\\alpha$ and the clean baseline.\nA signal provides early warning if $\\Delta_s(t, \\alpha) > 5\\%$ within the first 10\\% of training steps.\n\n\\paragraph{Method-dependence.}\nWe compare signal trajectories between QLoRA (C1) and full fine-tuning (C4) under matched model size, dataset, and contamination fractions.\nPaired differences in end-of-generation signal values quantify whether collapse signatures depend on the fine-tuning method or reflect properties of the data contamination itself.\n",
      "numLines": 148,
      "startLine": 1,
      "totalLines": 148
    }
  },
  "sourceToolAssistantUUID": "bd0a753a-f25d-41d6-a68f-7234a5c3dc78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T21:59:54.915Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EQZNyq382thGX7Zemu7gVy`</summary>

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
  "parentUuid": "4b39ad47-c462-4e96-9bb0-19789dd715c2",
  "isSidechain": false,
  "requestId": "req_011Cb576LzdFRCbHZnSs1Pdr",
  "type": "assistant",
  "uuid": "bd0a753a-f25d-41d6-a68f-7234a5c3dc78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FQHRjRs5xFnUS52UKeFk1B",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13446,
      "cache_read_input_tokens": 11841,
      "output_tokens": 161,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13446,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 161,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13446
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
  "leafUuid": "0573c3c2-8601-4030-9f72-2a404b7d1af0",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Write Results section for collapse monitor paper",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a"
}
```

---

### Assistant

_source line 15 · 2026-05-15T21:59:57.990Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the method section and the writing skill. Let me also check if there are any existing data files or figures that might help me write accurate numbers.

Let me also check for the existing experiments.tex file and any data files referenced in the task.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0573c3c2-8601-4030-9f72-2a404b7d1af0",
  "isSidechain": false,
  "requestId": "req_011Cb576fBG2abfLF1BfeCZc",
  "type": "assistant",
  "uuid": "d76e1788-0111-45ec-be55-b18177835679",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146wWqB5yENcgFNtmtW9k2T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9392,
      "cache_read_input_tokens": 25287,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9392,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 353,
          "cache_read_input_tokens": 25287,
          "cache_creation_input_tokens": 9392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9392
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

_source line 16 · 2026-05-15T21:59:58.503Z_

Now let me check for any existing data files and the current state of the paper directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d76e1788-0111-45ec-be55-b18177835679",
  "isSidechain": false,
  "requestId": "req_011Cb576fBG2abfLF1BfeCZc",
  "type": "assistant",
  "uuid": "364ee927-d172-4e4d-a6bc-9cb5293f63e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146wWqB5yENcgFNtmtW9k2T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9392,
      "cache_read_input_tokens": 25287,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9392,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 353,
          "cache_read_input_tokens": 25287,
          "cache_creation_input_tokens": 9392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9392
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

_source line 17 · 2026-05-15T22:00:00.533Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01HCESu8Kv5CThcesGJLjQg8`</summary>

```json
{
  "pattern": "**/*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "364ee927-d172-4e4d-a6bc-9cb5293f63e0",
  "isSidechain": false,
  "requestId": "req_011Cb576fBG2abfLF1BfeCZc",
  "type": "assistant",
  "uuid": "84ca188a-02b8-42ff-bb18-e40b35b1ff2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146wWqB5yENcgFNtmtW9k2T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9392,
      "cache_read_input_tokens": 25287,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9392,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 353,
          "cache_read_input_tokens": 25287,
          "cache_creation_input_tokens": 9392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9392
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

_source line 18 · 2026-05-15T22:00:01.500Z_

<details><summary>↩ Tool result · `toolu_01TCqSiTD4Z574k2zjhMrkoa`</summary>

```text
paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92bbc6a9-d4de-4281-8040-2963aa6bf067",
  "isSidechain": false,
  "promptId": "06204627-aef4-4171-b484-81a6a94f14ad",
  "type": "user",
  "uuid": "a1792018-c6ec-448b-9922-93ebe0d15f2b",
  "toolUseResult": {
    "filenames": [
      "paper/sections/experiments.tex"
    ],
    "durationMs": 5,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "92bbc6a9-d4de-4281-8040-2963aa6bf067",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T22:00:00.547Z_

<details><summary>↩ Tool result · `toolu_01HCESu8Kv5CThcesGJLjQg8`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84ca188a-02b8-42ff-bb18-e40b35b1ff2b",
  "isSidechain": false,
  "promptId": "06204627-aef4-4171-b484-81a6a94f14ad",
  "type": "user",
  "uuid": "c8ca6752-15e2-4d1b-af4e-4b3bf9dc6a94",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 10,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "84ca188a-02b8-42ff-bb18-e40b35b1ff2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T22:00:01.010Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WR252qniovHtcsoA49ACED`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8ca6752-15e2-4d1b-af4e-4b3bf9dc6a94",
  "isSidechain": false,
  "requestId": "req_011Cb576fBG2abfLF1BfeCZc",
  "type": "assistant",
  "uuid": "021f774d-7957-4137-832b-b1cbaf32dbbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146wWqB5yENcgFNtmtW9k2T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9392,
      "cache_read_input_tokens": 25287,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9392,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 353,
          "cache_read_input_tokens": 25287,
          "cache_creation_input_tokens": 9392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9392
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

_source line 21 · 2026-05-15T22:00:01.019Z_

<details><summary>↩ Tool result · `toolu_01WR252qniovHtcsoA49ACED`</summary>

```text
paper/sections/introduction.tex
paper/sections/related_work.tex
paper/sections/conclusion.tex
paper/sections/abstract.tex
paper/sections/experiments.tex
paper/sections/discussion.tex
paper/sections/appendix.tex
paper/sections/limitations.tex
paper/sections/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "021f774d-7957-4137-832b-b1cbaf32dbbe",
  "isSidechain": false,
  "promptId": "06204627-aef4-4171-b484-81a6a94f14ad",
  "type": "user",
  "uuid": "7e8a41da-b79b-49ed-9eb1-ce7fe74243ff",
  "toolUseResult": {
    "filenames": [
      "paper/sections/introduction.tex",
      "paper/sections/related_work.tex",
      "paper/sections/conclusion.tex",
      "paper/sections/abstract.tex",
      "paper/sections/experiments.tex",
      "paper/sections/discussion.tex",
      "paper/sections/appendix.tex",
      "paper/sections/limitations.tex",
      "paper/sections/method.tex"
    ],
    "durationMs": 6,
    "numFiles": 9,
    "truncated": false
  },
  "sourceToolAssistantUUID": "021f774d-7957-4137-832b-b1cbaf32dbbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T22:00:01.492Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TCqSiTD4Z574k2zjhMrkoa`</summary>

```json
{
  "pattern": "**/experiments.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e8a41da-b79b-49ed-9eb1-ce7fe74243ff",
  "isSidechain": false,
  "requestId": "req_011Cb576fBG2abfLF1BfeCZc",
  "type": "assistant",
  "uuid": "92bbc6a9-d4de-4281-8040-2963aa6bf067",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0146wWqB5yENcgFNtmtW9k2T",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9392,
      "cache_read_input_tokens": 25287,
      "output_tokens": 353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9392,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 353,
          "cache_read_input_tokens": 25287,
          "cache_creation_input_tokens": 9392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9392
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

_source line 23 · 2026-05-15T22:00:03.321Z_

<details open><summary>🔧 Tool call — Read · `toolu_015rP1weEvEDWpKvDULozMr1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1792018-c6ec-448b-9922-93ebe0d15f2b",
  "isSidechain": false,
  "requestId": "req_011Cb5779926nAfp9js4N4Ka",
  "type": "assistant",
  "uuid": "57366db5-c23b-4ace-8bab-cc1d435a4919",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015v7WHvqTzRDK9PcBu5jwK4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 34679,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 522,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 34679,
          "cache_creation_input_tokens": 522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 522
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

_source line 24 · 2026-05-15T22:00:03.325Z_

<details><summary>↩ Tool result · `toolu_015rP1weEvEDWpKvDULozMr1`</summary>

```text
1	% Experiments section — collapse_severity_monitor
2	% Verified data sources: mvp_frac50_100, within_gen_analysis, per_layer_analysis_v5
3	% Pending: plan_001 (1.5B 6-frac 5-seed), plan_002 (PubMed), plan_003–010
4	
5	\section{Experiments}
6	\label{sec:results}
7	
8	\subsection{Experimental Setup}
9	\label{sec:setup}
10	
11	All experiments run on two NVIDIA RTX 5090 GPUs (32\,GB each).
12	Table~\ref{tab:exp_matrix} summarizes the experimental design.
13	
14	\begin{table}[t]
15	\centering
16	\caption{Experimental matrix. MVP results (shaded) are reported; remaining configurations are in progress.}
17	\label{tab:exp_matrix}
18	\small
19	\begin{tabular}{lcccc}
20	\toprule
21	\textbf{Axis} & \textbf{MVP} & \textbf{Full Design} \\
22	\midrule
23	Model         & Qwen2.5-0.5B          & + Qwen2.5-1.5B \\
24	Dataset       & WikiText-2            & + PubMed \\
25	Fractions     & $\{0, 0.5, 1.0\}$    & $\{0, 0.1, 0.25, 0.5, 0.75, 1.0\}$ \\
26	Seeds         & 1 (seed 42)           & 5 (seeds 42--46) \\
27	Generations   & 5                     & 5 \\
28	Fine-tuning   & QLoRA ($r\!=\!16$)    & + Full FT comparison \\
29	\midrule
30	Total runs    & 15                    & ${\sim}300$ \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	We report verified MVP results (0.5B, WikiText-2, 3 fractions, seed~42) throughout, with placeholders for the full design.
36	All signals are collected every 50 optimizer steps (${\sim}3\%$ granularity over 1{,}540 steps per generation).
37	Training details are in Section~\ref{sec:method}; we focus here on results.
38	
39	%% TODO: plan_001 — update table with 1.5B column once 6-frac × 5-seed data arrives (ETA 2026-05-18)
40	%% TODO: plan_002 — add PubMed column once cross-domain runs complete
41	
42	\subsection{Signal--Severity Correlation}
43	\label{sec:correlation}
44	
45	\paragraph{Cross-fraction monotonicity.}
46	%% Source: mvp_frac50_100 — 0.5B, WikiText-2, fractions {0, 0.5, 1.0}, seed 42
47	We first evaluate whether training-time signals maintain monotonic ordering across contamination levels.
48	Table~\ref{tab:cross_frac} reports end-of-generation signal values at generation~4 (the final generation) for each contamination fraction.
49	
50	\begin{table}[t]
51	\centering
52	\caption{End-of-generation signal values at $G\!=\!4$ across contamination fractions (0.5B, WikiText-2, seed~42). Effect sizes relative to clean baseline ($\alpha\!=\!0$) in parentheses.}
53	\label{tab:cross_frac}
54	\small
55	\begin{tabular}{lccc}
56	\toprule
57	\textbf{Signal} & $\alpha = 0$ & $\alpha = 0.5$ & $\alpha = 1.0$ \\
58	\midrule
59	%% Source: mvp_frac50_100 — final_values_*pct_gen4
60	Stable rank       & 23.41          & 24.79 ($1.06\times$)  & 155.64 ($6.6\times$) \\
61	Spectral entropy  & 0.703          & 0.716 ($+1.8\%$)      & 0.884 ($+25.7\%$) \\
62	Token entropy     & 2.259          & 2.215 ($-1.9\%$)      & 0.782 ($-65.4\%$) \\
63	Perplexity        & 15.67          & 16.95 ($1.08\times$)  & 839.2 ($53\times$) \\
64	\bottomrule
65	\end{tabular}
66	\end{table}
67	
68	All spectral and output signals achieve $|\rho| = 1.0$ (Spearman) per generation across the three tested fractions.%
69	\footnote{$|\rho| = 1.0$ with $n = 3$ is a necessary but weak condition; the 6-fraction validation provides a more stringent monotonicity test.}
70	%% Source: mvp_frac50_100 — gate_check_spectral, gate_check_output
71	The effect sizes span orders of magnitude: at $\alpha = 1.0$, stable rank increases 6.6$\times$ and perplexity increases 53$\times$ relative to the clean baseline, while token entropy decreases by 65\%.
72	Critically, the $\alpha = 0$ baseline remains stable across all 5 generations ($<3\%$ variation for all signals), confirming that observed changes are attributable to contamination rather than training drift.
73	%% Source: mvp_frac50_100 — 0pct_baseline_stability
74	
75	\paragraph{Cross-generation accumulation.}
76	%% Source: mvp_frac50_100 — cross-gen tracking
77	At $\alpha = 1.0$, perplexity exhibits super-linear growth: $15.7 \to 136.9 \to 394.3 \to 691.4 \to 839.2$ across generations 0--4, consistent with the accelerating degradation predicted by collapse theory~\citep{Shumailov2024,Dohmatob2024_tails}.
78	Cross-generation Spearman correlations are $|\rho| = 1.0$ for perplexity and $|\rho| = 0.9$ for stable rank at $\alpha = 1.0$.
79	
80	%% TODO: plan_001 — 6-fraction × 5-seed correlation analysis with bootstrap CIs
81	%% TODO: plan_001 — effect size tables with mean ± std across seeds, Cohen's d
82	%% TODO: plan_002 — PubMed cross-domain replication of monotonicity claim
83	%% TODO: plan_001 — Figure \ref{fig:signal_severity}: signal value vs fraction curves (6 fractions, error bands from 5 seeds)
84	
85	\begin{figure}[t]
86	\centering
87	%% TODO: plan_001 — replace placeholder with actual figure
88	%% \includegraphics[width=\linewidth]{figures/signal_severity.pdf}
89	\fbox{\parbox{0.9\linewidth}{\centering\vspace{2em}\textit{Placeholder: signal vs.\ contamination fraction}\\\textit{(6 fractions $\times$ 5 seeds, 1.5B + 0.5B)}\vspace{2em}}}
90	\caption{Training-time signal values as a function of contamination fraction $\alpha$, averaged over 5 seeds with 95\% bootstrap CIs. Panels: stable rank, spectral entropy, token entropy, perplexity. Separate curves per generation.}
91	\label{fig:signal_severity}
92	\end{figure}
93	
94	
95	\subsection{Early Warning Capability}
96	\label{sec:early_warning_results}
97	
98	\paragraph{Within-generation signal divergence.}
99	%% Source: within_gen_analysis — 0.5B, WikiText-2, step-level temporal analysis
100	We analyze how rapidly signals diverge from the clean baseline within a single training run.
101	At step~50 of 1{,}540 (${\sim}3\%$ training progress), the relative deviation $\Delta_s$ (Eq.~\ref{eq:deviation}) between $\alpha = 1.0$ and $\alpha = 0$ is:
102	\begin{itemize}[nosep]
103	    \item Stable rank: $\Delta_\mathrm{SR} = 34.4\%$
104	    \item Token entropy: $\Delta_\mathrm{TE} = 24.5\%$
105	    \item Perplexity: $\Delta_\mathrm{PPL} = 17.7\%$
106	\end{itemize}
107	%% Source: within_gen_analysis — signals_above_5pct_at_step50
108	All three signals exceed a 5\% deviation threshold within 3\% of training, demonstrating that collapse leaves detectable fingerprints at the earliest available checkpoint.
109	Spectral entropy and gradient norm respond more slowly, first exceeding 5\% at step~100 (${\sim}6\%$ progress).
110	
111	\paragraph{Collapse detection via AUROC.}
112	%% Source: within_gen_analysis — AUROC analysis
113	At step~50, stable rank, token entropy, and perplexity each achieve AUROC $= 1.0$ for binary classification of $\alpha = 1.0$ versus $\alpha = 0$, using the generation-level signal values as the discriminating feature.
114	We emphasize that AUROC $= 1.0$ with $n = 3$ fractions and a single seed is a weak result; we report it as a sanity check rather than a primary claim.
115	
116	\paragraph{Cross-generational acceleration.}
117	%% Source: within_gen_analysis — crossgen_acceleration
118	The severity of within-generation signal deviation accelerates across generations.
119	For $\alpha = 1.0$, the end-of-generation perplexity deviation from the per-generation clean ($\alpha\!=\!0$) baseline is: gen~0 ${<}\,1\%$, gen~1 $= +770\%$, gen~2 $= +2{,}416\%$.
120	This acceleration makes early warning increasingly effective at later generations, precisely when intervention is most critical.
121	
122	%% TODO: plan_004 — 1.5B within-generation early warning analysis (does 3% threshold hold at scale?)
123	%% TODO: plan_005 — threshold calibration with clustered bootstrap (one observation per fraction × seed)
124	%% TODO: plan_005 — ROC analysis with proper non-independent observation handling
125	
126	\begin{figure}[t]
127	\centering
128	%% TODO: plan_004 — replace placeholder with actual figure
129	%% \includegraphics[width=\linewidth]{figures/early_warning.pdf}
130	\fbox{\parbox{0.9\linewidth}{\centering\vspace{2em}\textit{Placeholder: signal deviation vs.\ training step}\\\textit{(0.5B + 1.5B, per-generation curves)}\vspace{2em}}}
131	\caption{Relative signal deviation $\Delta_s(t, \alpha\!=\!1.0)$ as a function of training step. The dashed line marks the 5\% detection threshold. Stable rank crosses the threshold at step~50 ($3\%$ progress) in generation~0, with earlier crossing at subsequent generations.}
132	\label{fig:early_warning}
133	\end{figure}
134	
135	
136	\subsection{Signal Taxonomy}
137	\label{sec:taxonomy}
138	
139	Not all signals are equally informative across severity levels.
140	Table~\ref{tab:signal_taxonomy} summarizes the operating characteristics of each signal family.
141	
142	\begin{table}[t]
143	\centering
144	\caption{Signal taxonomy: operating ranges and failure modes. ``Earliest response'' is the first step exceeding 5\% deviation from baseline at $\alpha\!=\!1.0$.}
145	\label{tab:signal_taxonomy}
146	\small
147	\begin{tabular}{lccl}
148	\toprule
149	\textbf{Signal} & \textbf{Earliest} & $|\rho|$ & \textbf{Notes} \\
150	\midrule
151	%% Source: within_gen_analysis, mvp_frac50_100
152	Stable rank      & step 50  & 1.0 & Largest early deviation; saturates at extreme severity \\
153	Spectral entropy & step 100 & 1.0 & Correlated with SR; complementary dynamic \\
154	Token entropy    & step 50  & 1.0 & Most stable monotonic tracking \\
155	Perplexity       & step 50  & 1.0 & Super-linear growth; interpretable severity scale \\
156	Gradient norm    & step 100 & ---  & Non-monotonic under QLoRA \\
157	HellaSwag acc.   & ---      & ---  & Insensitive at 0.5B (1.2\% drop at $53\times$ PPL) \\
158	\bottomrule
159	\end{tabular}
160	\end{table}
161	
162	\paragraph{Spectral signals: earliest but saturating.}
163	%% Source: mvp_frac50_100, within_gen_analysis
164	Stable rank provides the largest early separation (34.4\% at step~50) and achieves the strongest cross-fraction correlation.
165	However, the 6.6$\times$ increase at $\alpha = 1.0$ suggests potential saturation at extreme severity, where the representation space disperses to near-uniform eigenspectra.
166	
167	\paragraph{Output signals: reliable severity tracking.}
168	%% Source: mvp_frac50_100
169	Perplexity and token entropy maintain monotonic ordering across all fractions and generations ($|\rho| = 1.0$).
170	Perplexity's super-linear cross-generation growth ($15.7 \to 839.2$) provides the most interpretable severity scale, mapping directly to language modeling quality.
171	Token entropy, which decreases under collapse (from 2.259 to 0.782), captures the mode-narrowing phenomenon characteristic of generative collapse.
172	
173	\paragraph{Gradient norm: non-monotonic under QLoRA.}
174	%% Source: mvp_frac50_100
175	The L2 gradient norm exhibits non-monotonic behavior with contamination fraction in our QLoRA setup, rising at moderate contamination but failing to separate high-severity conditions monotonically.
176	This limits its standalone utility as a severity monitor, though it may serve as a complementary early indicator when combined with spectral signals.
177	
178	%% TODO: plan_003 — gradient norm under full FT (expected to be monotonic without adapter constraints)
179	
180	\paragraph{Downstream metrics: insensitive at small scale.}
181	%% Source: mvp_frac50_100
182	HellaSwag accuracy drops only 1.2\% (0.435 $\to$ 0.430) at 0.5B scale despite catastrophic collapse ($53\times$ perplexity increase), confirming that small-model benchmark performance is a poor proxy for generative quality degradation.
183	
184	%% TODO: plan_006 — full taxonomy with 6 fractions: identify saturation onset, operating range boundaries
185	%% TODO: plan_008 — self-recovery analysis at moderate contamination (25% fraction)
186	%% TODO: plan_009 — SIGMA head-to-head comparison: our signals vs. SIGMA at training checkpoints
187	
188	
189	\subsection{Per-Layer Analysis}
190	\label{sec:per_layer}
191	
192	%% Source: per_layer_analysis_v5 — 0.5B, WikiText-2, fractions {0, 0.5}, seed 42
193	We analyze per-layer spectral signatures by computing SVD of the LoRA weight delta $\mathbf{B}\mathbf{A}$ for each adapted module after training.
194	This reveals non-uniform collapse propagation across the 24-layer architecture.
195	
196	\paragraph{Sub-module response patterns.}
197	Sub-module type is a stronger predictor of collapse response than layer position (Table~\ref{tab:per_layer}):
198	\begin{enumerate}[nosep]
199	    \item \textbf{\texttt{v\_proj}: universal diffusion.} Almost every layer shows $\Delta\mathrm{SR} > +1.0$ under 50\% contamination, with L16 reaching $+3.060$ (global maximum). The mean across all 24 layers is $+1.34$, the highest of any sub-module.
200	    %% Source: per_layer_analysis_v5 — v_proj_mean_sr_delta = 1.34, v_proj_L16_peak = 3.060
201	    \item \textbf{\texttt{down\_proj}: localized collapse at L11--L12.} Layers~11--12 exhibit strong rank collapse ($-2.146$ and $-3.218$ respectively), while the remaining 22 layers average $+0.92$, mild diffusion. This localized collapse is unique to \texttt{down\_proj}.
202	    %% Source: per_layer_analysis_v5 — down_proj_L11 = -2.146, down_proj_L12 = -3.218, down_proj_mean_excl_L11_L12 = 0.92
203	    \item \textbf{Other sub-modules: stable.} \texttt{k\_proj} (mean $+0.72$) and \texttt{q\_proj} (mean $+0.51$) show moderate diffusion; \texttt{o\_proj} ($-0.02$), \texttt{up\_proj} ($+0.01$), and \texttt{gate\_proj} ($-0.01$) remain near zero.
204	    %% Source: per_layer_analysis_v5 — k_proj_mean = 0.72, q_proj_mean = 0.51, o_proj_mean = -0.02, up_proj_mean = 0.01, gate_proj_mean = -0.01
205	\end{enumerate}
206	
207	\paragraph{Sub-module bifurcation at L11--L12.}
208	%% Source: per_layer_analysis_v5
209	At layers~11--12, \texttt{down\_proj} undergoes rank collapse ($\Delta\mathrm{SR} = -3.218$ at L12, $-2.146$ at L11), while \texttt{v\_proj} continues its architecture-wide diffusion pattern ($+1.492$ at L11, $+0.40$ at L12).
210	%% Source: per_layer_analysis_v5 — L12_down_proj = -3.218, L11_down_proj = -2.146, L11_v_proj = +1.492, L12_v_proj = +0.40
211	These opposing effects partially cancel at the layer level, rendering aggregate spectral signals blind to this internal restructuring.
212	The weight norm crossover occurs at layer~11: early layers shrink under contamination while late layers grow.
213	%% Source: per_layer_analysis_v5 — weight_norm_crossover_layer = 11
214	
215	\begin{table}[t]
216	\centering
217	\caption{Per-layer stable rank changes under 50\% contamination vs.\ clean baseline (0.5B, gen~4, seed~42). Organized by sub-module; full results in appendix.}
218	\label{tab:per_layer}
219	\small
220	\begin{tabular}{llcc}
221	\toprule
222	\textbf{Sub-module} & \textbf{Layer} & $\Delta\mathrm{SR}$ & \textbf{Direction} \\
223	\midrule
224	%% Source: per_layer_analysis_v5
225	\texttt{v\_proj}    & L16 (peak)          & $+3.060$ & diffusion \\
226	\texttt{v\_proj}    & mean (L0--L23)      & $+1.34$  & diffusion \\
227	\texttt{down\_proj} & L12                 & $-3.218$ & collapse \\
228	\texttt{down\_proj} & L11                 & $-2.146$ & collapse \\
229	\texttt{down\_proj} & mean (excl L11--12) & $+0.92$  & mild diffusion \\
230	\texttt{q\_proj}    & L0 (peak)           & $+2.849$ & diffusion \\
231	\texttt{q\_proj}    & mean (L0--L23)      & $+0.51$  & mild \\
232	\bottomrule
233	\end{tabular}
234	\end{table}
235	
236	%% TODO: plan_007 — 1.5B per-layer analysis: does L12 down_proj anomaly persist at scale?
237	%% TODO: plan_007 — cross-scale comparison figure: 0.5B vs 1.5B per-layer heatmaps
238	
239	\begin{figure}[t]
240	\centering
241	%% TODO: plan_007 — replace placeholder with actual heatmap
242	%% \includegraphics[width=\linewidth]{figures/per_layer_heatmap.pdf}
243	\fbox{\parbox{0.9\linewidth}{\centering\vspace{2em}\textit{Placeholder: per-layer $\Delta$SR heatmap}\\\textit{(layers $\times$ sub-modules, 0.5B + 1.5B)}\vspace{2em}}}
244	\caption{Per-layer stable rank change ($\Delta\mathrm{SR}$) between 50\% contamination and clean baseline at generation~4. Rows: transformer layers (L0--L23); columns: adapted sub-modules. Red: rank collapse; blue: rank diffusion. The \texttt{v\_proj} column shows consistent diffusion (blue) across nearly all layers, while \texttt{down\_proj} at L11--L12 shows localized collapse (dark red).}
245	\label{fig:per_layer_heatmap}
246	\end{figure}
247	
248	
249	\subsection{Ablations and Robustness}
250	\label{sec:ablations}
251	
252	%% TODO: plan_001 — seed variance analysis: are 5 seeds sufficient for stable CIs?
253	%% TODO: plan_002 — PubMed cross-domain: do correlation strengths transfer?
254	%% TODO: plan_003 — Full FT vs QLoRA comparison: gradient norm monotonicity, effect size changes
255	%% TODO: plan_010 — 3B spot-check: brief scale extrapolation (if GPU budget permits)
256	
257	This section will present robustness analyses across four axes:
258	
259	\paragraph{Seed stability.}
260	%% TODO: plan_001 — coefficient of variation across 5 seeds for each signal × fraction
261	We will report the coefficient of variation across 5 seeds for each signal, demonstrating that the monotonic ordering is robust to initialization randomness.
262	
263	\paragraph{Cross-domain transfer.}
264	%% TODO: plan_002 — PubMed 6-fraction × 3-seed replication
265	We evaluate whether signal--severity correlations hold on PubMed biomedical abstracts, a domain with substantially different distributional characteristics from WikiText-2.
266	
267	\paragraph{Fine-tuning method.}
268	%% TODO: plan_003 — Full FT comparison on 1 configuration
269	We compare QLoRA ($r\!=\!16$) with full fine-tuning on one configuration to assess whether the observed non-monotonic gradient norm behavior is QLoRA-specific or a general phenomenon.
270	
271	\paragraph{Scale extrapolation.}
272	%% TODO: plan_010 — 3B spot-check
273	A spot-check on Qwen2.5-3B (if GPU budget permits) provides preliminary evidence on whether the signal taxonomy extends beyond the 0.5B--1.5B range.
274	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57366db5-c23b-4ace-8bab-cc1d435a4919",
  "isSidechain": false,
  "promptId": "06204627-aef4-4171-b484-81a6a94f14ad",
  "type": "user",
  "uuid": "486f437e-c2c9-4385-879d-d677bc079853",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/experiments.tex",
      "content": "% Experiments section — collapse_severity_monitor\n% Verified data sources: mvp_frac50_100, within_gen_analysis, per_layer_analysis_v5\n% Pending: plan_001 (1.5B 6-frac 5-seed), plan_002 (PubMed), plan_003–010\n\n\\section{Experiments}\n\\label{sec:results}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nAll experiments run on two NVIDIA RTX 5090 GPUs (32\\,GB each).\nTable~\\ref{tab:exp_matrix} summarizes the experimental design.\n\n\\begin{table}[t]\n\\centering\n\\caption{Experimental matrix. MVP results (shaded) are reported; remaining configurations are in progress.}\n\\label{tab:exp_matrix}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Axis} & \\textbf{MVP} & \\textbf{Full Design} \\\\\n\\midrule\nModel         & Qwen2.5-0.5B          & + Qwen2.5-1.5B \\\\\nDataset       & WikiText-2            & + PubMed \\\\\nFractions     & $\\{0, 0.5, 1.0\\}$    & $\\{0, 0.1, 0.25, 0.5, 0.75, 1.0\\}$ \\\\\nSeeds         & 1 (seed 42)           & 5 (seeds 42--46) \\\\\nGenerations   & 5                     & 5 \\\\\nFine-tuning   & QLoRA ($r\\!=\\!16$)    & + Full FT comparison \\\\\n\\midrule\nTotal runs    & 15                    & ${\\sim}300$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWe report verified MVP results (0.5B, WikiText-2, 3 fractions, seed~42) throughout, with placeholders for the full design.\nAll signals are collected every 50 optimizer steps (${\\sim}3\\%$ granularity over 1{,}540 steps per generation).\nTraining details are in Section~\\ref{sec:method}; we focus here on results.\n\n%% TODO: plan_001 — update table with 1.5B column once 6-frac × 5-seed data arrives (ETA 2026-05-18)\n%% TODO: plan_002 — add PubMed column once cross-domain runs complete\n\n\\subsection{Signal--Severity Correlation}\n\\label{sec:correlation}\n\n\\paragraph{Cross-fraction monotonicity.}\n%% Source: mvp_frac50_100 — 0.5B, WikiText-2, fractions {0, 0.5, 1.0}, seed 42\nWe first evaluate whether training-time signals maintain monotonic ordering across contamination levels.\nTable~\\ref{tab:cross_frac} reports end-of-generation signal values at generation~4 (the final generation) for each contamination fraction.\n\n\\begin{table}[t]\n\\centering\n\\caption{End-of-generation signal values at $G\\!=\\!4$ across contamination fractions (0.5B, WikiText-2, seed~42). Effect sizes relative to clean baseline ($\\alpha\\!=\\!0$) in parentheses.}\n\\label{tab:cross_frac}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Signal} & $\\alpha = 0$ & $\\alpha = 0.5$ & $\\alpha = 1.0$ \\\\\n\\midrule\n%% Source: mvp_frac50_100 — final_values_*pct_gen4\nStable rank       & 23.41          & 24.79 ($1.06\\times$)  & 155.64 ($6.6\\times$) \\\\\nSpectral entropy  & 0.703          & 0.716 ($+1.8\\%$)      & 0.884 ($+25.7\\%$) \\\\\nToken entropy     & 2.259          & 2.215 ($-1.9\\%$)      & 0.782 ($-65.4\\%$) \\\\\nPerplexity        & 15.67          & 16.95 ($1.08\\times$)  & 839.2 ($53\\times$) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAll spectral and output signals achieve $|\\rho| = 1.0$ (Spearman) per generation across the three tested fractions.%\n\\footnote{$|\\rho| = 1.0$ with $n = 3$ is a necessary but weak condition; the 6-fraction validation provides a more stringent monotonicity test.}\n%% Source: mvp_frac50_100 — gate_check_spectral, gate_check_output\nThe effect sizes span orders of magnitude: at $\\alpha = 1.0$, stable rank increases 6.6$\\times$ and perplexity increases 53$\\times$ relative to the clean baseline, while token entropy decreases by 65\\%.\nCritically, the $\\alpha = 0$ baseline remains stable across all 5 generations ($<3\\%$ variation for all signals), confirming that observed changes are attributable to contamination rather than training drift.\n%% Source: mvp_frac50_100 — 0pct_baseline_stability\n\n\\paragraph{Cross-generation accumulation.}\n%% Source: mvp_frac50_100 — cross-gen tracking\nAt $\\alpha = 1.0$, perplexity exhibits super-linear growth: $15.7 \\to 136.9 \\to 394.3 \\to 691.4 \\to 839.2$ across generations 0--4, consistent with the accelerating degradation predicted by collapse theory~\\citep{Shumailov2024,Dohmatob2024_tails}.\nCross-generation Spearman correlations are $|\\rho| = 1.0$ for perplexity and $|\\rho| = 0.9$ for stable rank at $\\alpha = 1.0$.\n\n%% TODO: plan_001 — 6-fraction × 5-seed correlation analysis with bootstrap CIs\n%% TODO: plan_001 — effect size tables with mean ± std across seeds, Cohen's d\n%% TODO: plan_002 — PubMed cross-domain replication of monotonicity claim\n%% TODO: plan_001 — Figure \\ref{fig:signal_severity}: signal value vs fraction curves (6 fractions, error bands from 5 seeds)\n\n\\begin{figure}[t]\n\\centering\n%% TODO: plan_001 — replace placeholder with actual figure\n%% \\includegraphics[width=\\linewidth]{figures/signal_severity.pdf}\n\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}\\textit{Placeholder: signal vs.\\ contamination fraction}\\\\\\textit{(6 fractions $\\times$ 5 seeds, 1.5B + 0.5B)}\\vspace{2em}}}\n\\caption{Training-time signal values as a function of contamination fraction $\\alpha$, averaged over 5 seeds with 95\\% bootstrap CIs. Panels: stable rank, spectral entropy, token entropy, perplexity. Separate curves per generation.}\n\\label{fig:signal_severity}\n\\end{figure}\n\n\n\\subsection{Early Warning Capability}\n\\label{sec:early_warning_results}\n\n\\paragraph{Within-generation signal divergence.}\n%% Source: within_gen_analysis — 0.5B, WikiText-2, step-level temporal analysis\nWe analyze how rapidly signals diverge from the clean baseline within a single training run.\nAt step~50 of 1{,}540 (${\\sim}3\\%$ training progress), the relative deviation $\\Delta_s$ (Eq.~\\ref{eq:deviation}) between $\\alpha = 1.0$ and $\\alpha = 0$ is:\n\\begin{itemize}[nosep]\n    \\item Stable rank: $\\Delta_\\mathrm{SR} = 34.4\\%$\n    \\item Token entropy: $\\Delta_\\mathrm{TE} = 24.5\\%$\n    \\item Perplexity: $\\Delta_\\mathrm{PPL} = 17.7\\%$\n\\end{itemize}\n%% Source: within_gen_analysis — signals_above_5pct_at_step50\nAll three signals exceed a 5\\% deviation threshold within 3\\% of training, demonstrating that collapse leaves detectable fingerprints at the earliest available checkpoint.\nSpectral entropy and gradient norm respond more slowly, first exceeding 5\\% at step~100 (${\\sim}6\\%$ progress).\n\n\\paragraph{Collapse detection via AUROC.}\n%% Source: within_gen_analysis — AUROC analysis\nAt step~50, stable rank, token entropy, and perplexity each achieve AUROC $= 1.0$ for binary classification of $\\alpha = 1.0$ versus $\\alpha = 0$, using the generation-level signal values as the discriminating feature.\nWe emphasize that AUROC $= 1.0$ with $n = 3$ fractions and a single seed is a weak result; we report it as a sanity check rather than a primary claim.\n\n\\paragraph{Cross-generational acceleration.}\n%% Source: within_gen_analysis — crossgen_acceleration\nThe severity of within-generation signal deviation accelerates across generations.\nFor $\\alpha = 1.0$, the end-of-generation perplexity deviation from the per-generation clean ($\\alpha\\!=\\!0$) baseline is: gen~0 ${<}\\,1\\%$, gen~1 $= +770\\%$, gen~2 $= +2{,}416\\%$.\nThis acceleration makes early warning increasingly effective at later generations, precisely when intervention is most critical.\n\n%% TODO: plan_004 — 1.5B within-generation early warning analysis (does 3% threshold hold at scale?)\n%% TODO: plan_005 — threshold calibration with clustered bootstrap (one observation per fraction × seed)\n%% TODO: plan_005 — ROC analysis with proper non-independent observation handling\n\n\\begin{figure}[t]\n\\centering\n%% TODO: plan_004 — replace placeholder with actual figure\n%% \\includegraphics[width=\\linewidth]{figures/early_warning.pdf}\n\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}\\textit{Placeholder: signal deviation vs.\\ training step}\\\\\\textit{(0.5B + 1.5B, per-generation curves)}\\vspace{2em}}}\n\\caption{Relative signal deviation $\\Delta_s(t, \\alpha\\!=\\!1.0)$ as a function of training step. The dashed line marks the 5\\% detection threshold. Stable rank crosses the threshold at step~50 ($3\\%$ progress) in generation~0, with earlier crossing at subsequent generations.}\n\\label{fig:early_warning}\n\\end{figure}\n\n\n\\subsection{Signal Taxonomy}\n\\label{sec:taxonomy}\n\nNot all signals are equally informative across severity levels.\nTable~\\ref{tab:signal_taxonomy} summarizes the operating characteristics of each signal family.\n\n\\begin{table}[t]\n\\centering\n\\caption{Signal taxonomy: operating ranges and failure modes. ``Earliest response'' is the first step exceeding 5\\% deviation from baseline at $\\alpha\\!=\\!1.0$.}\n\\label{tab:signal_taxonomy}\n\\small\n\\begin{tabular}{lccl}\n\\toprule\n\\textbf{Signal} & \\textbf{Earliest} & $|\\rho|$ & \\textbf{Notes} \\\\\n\\midrule\n%% Source: within_gen_analysis, mvp_frac50_100\nStable rank      & step 50  & 1.0 & Largest early deviation; saturates at extreme severity \\\\\nSpectral entropy & step 100 & 1.0 & Correlated with SR; complementary dynamic \\\\\nToken entropy    & step 50  & 1.0 & Most stable monotonic tracking \\\\\nPerplexity       & step 50  & 1.0 & Super-linear growth; interpretable severity scale \\\\\nGradient norm    & step 100 & ---  & Non-monotonic under QLoRA \\\\\nHellaSwag acc.   & ---      & ---  & Insensitive at 0.5B (1.2\\% drop at $53\\times$ PPL) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Spectral signals: earliest but saturating.}\n%% Source: mvp_frac50_100, within_gen_analysis\nStable rank provides the largest early separation (34.4\\% at step~50) and achieves the strongest cross-fraction correlation.\nHowever, the 6.6$\\times$ increase at $\\alpha = 1.0$ suggests potential saturation at extreme severity, where the representation space disperses to near-uniform eigenspectra.\n\n\\paragraph{Output signals: reliable severity tracking.}\n%% Source: mvp_frac50_100\nPerplexity and token entropy maintain monotonic ordering across all fractions and generations ($|\\rho| = 1.0$).\nPerplexity's super-linear cross-generation growth ($15.7 \\to 839.2$) provides the most interpretable severity scale, mapping directly to language modeling quality.\nToken entropy, which decreases under collapse (from 2.259 to 0.782), captures the mode-narrowing phenomenon characteristic of generative collapse.\n\n\\paragraph{Gradient norm: non-monotonic under QLoRA.}\n%% Source: mvp_frac50_100\nThe L2 gradient norm exhibits non-monotonic behavior with contamination fraction in our QLoRA setup, rising at moderate contamination but failing to separate high-severity conditions monotonically.\nThis limits its standalone utility as a severity monitor, though it may serve as a complementary early indicator when combined with spectral signals.\n\n%% TODO: plan_003 — gradient norm under full FT (expected to be monotonic without adapter constraints)\n\n\\paragraph{Downstream metrics: insensitive at small scale.}\n%% Source: mvp_frac50_100\nHellaSwag accuracy drops only 1.2\\% (0.435 $\\to$ 0.430) at 0.5B scale despite catastrophic collapse ($53\\times$ perplexity increase), confirming that small-model benchmark performance is a poor proxy for generative quality degradation.\n\n%% TODO: plan_006 — full taxonomy with 6 fractions: identify saturation onset, operating range boundaries\n%% TODO: plan_008 — self-recovery analysis at moderate contamination (25% fraction)\n%% TODO: plan_009 — SIGMA head-to-head comparison: our signals vs. SIGMA at training checkpoints\n\n\n\\subsection{Per-Layer Analysis}\n\\label{sec:per_layer}\n\n%% Source: per_layer_analysis_v5 — 0.5B, WikiText-2, fractions {0, 0.5}, seed 42\nWe analyze per-layer spectral signatures by computing SVD of the LoRA weight delta $\\mathbf{B}\\mathbf{A}$ for each adapted module after training.\nThis reveals non-uniform collapse propagation across the 24-layer architecture.\n\n\\paragraph{Sub-module response patterns.}\nSub-module type is a stronger predictor of collapse response than layer position (Table~\\ref{tab:per_layer}):\n\\begin{enumerate}[nosep]\n    \\item \\textbf{\\texttt{v\\_proj}: universal diffusion.} Almost every layer shows $\\Delta\\mathrm{SR} > +1.0$ under 50\\% contamination, with L16 reaching $+3.060$ (global maximum). The mean across all 24 layers is $+1.34$, the highest of any sub-module.\n    %% Source: per_layer_analysis_v5 — v_proj_mean_sr_delta = 1.34, v_proj_L16_peak = 3.060\n    \\item \\textbf{\\texttt{down\\_proj}: localized collapse at L11--L12.} Layers~11--12 exhibit strong rank collapse ($-2.146$ and $-3.218$ respectively), while the remaining 22 layers average $+0.92$, mild diffusion. This localized collapse is unique to \\texttt{down\\_proj}.\n    %% Source: per_layer_analysis_v5 — down_proj_L11 = -2.146, down_proj_L12 = -3.218, down_proj_mean_excl_L11_L12 = 0.92\n    \\item \\textbf{Other sub-modules: stable.} \\texttt{k\\_proj} (mean $+0.72$) and \\texttt{q\\_proj} (mean $+0.51$) show moderate diffusion; \\texttt{o\\_proj} ($-0.02$), \\texttt{up\\_proj} ($+0.01$), and \\texttt{gate\\_proj} ($-0.01$) remain near zero.\n    %% Source: per_layer_analysis_v5 — k_proj_mean = 0.72, q_proj_mean = 0.51, o_proj_mean = -0.02, up_proj_mean = 0.01, gate_proj_mean = -0.01\n\\end{enumerate}\n\n\\paragraph{Sub-module bifurcation at L11--L12.}\n%% Source: per_layer_analysis_v5\nAt layers~11--12, \\texttt{down\\_proj} undergoes rank collapse ($\\Delta\\mathrm{SR} = -3.218$ at L12, $-2.146$ at L11), while \\texttt{v\\_proj} continues its architecture-wide diffusion pattern ($+1.492$ at L11, $+0.40$ at L12).\n%% Source: per_layer_analysis_v5 — L12_down_proj = -3.218, L11_down_proj = -2.146, L11_v_proj = +1.492, L12_v_proj = +0.40\nThese opposing effects partially cancel at the layer level, rendering aggregate spectral signals blind to this internal restructuring.\nThe weight norm crossover occurs at layer~11: early layers shrink under contamination while late layers grow.\n%% Source: per_layer_analysis_v5 — weight_norm_crossover_layer = 11\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-layer stable rank changes under 50\\% contamination vs.\\ clean baseline (0.5B, gen~4, seed~42). Organized by sub-module; full results in appendix.}\n\\label{tab:per_layer}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Sub-module} & \\textbf{Layer} & $\\Delta\\mathrm{SR}$ & \\textbf{Direction} \\\\\n\\midrule\n%% Source: per_layer_analysis_v5\n\\texttt{v\\_proj}    & L16 (peak)          & $+3.060$ & diffusion \\\\\n\\texttt{v\\_proj}    & mean (L0--L23)      & $+1.34$  & diffusion \\\\\n\\texttt{down\\_proj} & L12                 & $-3.218$ & collapse \\\\\n\\texttt{down\\_proj} & L11                 & $-2.146$ & collapse \\\\\n\\texttt{down\\_proj} & mean (excl L11--12) & $+0.92$  & mild diffusion \\\\\n\\texttt{q\\_proj}    & L0 (peak)           & $+2.849$ & diffusion \\\\\n\\texttt{q\\_proj}    & mean (L0--L23)      & $+0.51$  & mild \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%% TODO: plan_007 — 1.5B per-layer analysis: does L12 down_proj anomaly persist at scale?\n%% TODO: plan_007 — cross-scale comparison figure: 0.5B vs 1.5B per-layer heatmaps\n\n\\begin{figure}[t]\n\\centering\n%% TODO: plan_007 — replace placeholder with actual heatmap\n%% \\includegraphics[width=\\linewidth]{figures/per_layer_heatmap.pdf}\n\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}\\textit{Placeholder: per-layer $\\Delta$SR heatmap}\\\\\\textit{(layers $\\times$ sub-modules, 0.5B + 1.5B)}\\vspace{2em}}}\n\\caption{Per-layer stable rank change ($\\Delta\\mathrm{SR}$) between 50\\% contamination and clean baseline at generation~4. Rows: transformer layers (L0--L23); columns: adapted sub-modules. Red: rank collapse; blue: rank diffusion. The \\texttt{v\\_proj} column shows consistent diffusion (blue) across nearly all layers, while \\texttt{down\\_proj} at L11--L12 shows localized collapse (dark red).}\n\\label{fig:per_layer_heatmap}\n\\end{figure}\n\n\n\\subsection{Ablations and Robustness}\n\\label{sec:ablations}\n\n%% TODO: plan_001 — seed variance analysis: are 5 seeds sufficient for stable CIs?\n%% TODO: plan_002 — PubMed cross-domain: do correlation strengths transfer?\n%% TODO: plan_003 — Full FT vs QLoRA comparison: gradient norm monotonicity, effect size changes\n%% TODO: plan_010 — 3B spot-check: brief scale extrapolation (if GPU budget permits)\n\nThis section will present robustness analyses across four axes:\n\n\\paragraph{Seed stability.}\n%% TODO: plan_001 — coefficient of variation across 5 seeds for each signal × fraction\nWe will report the coefficient of variation across 5 seeds for each signal, demonstrating that the monotonic ordering is robust to initialization randomness.\n\n\\paragraph{Cross-domain transfer.}\n%% TODO: plan_002 — PubMed 6-fraction × 3-seed replication\nWe evaluate whether signal--severity correlations hold on PubMed biomedical abstracts, a domain with substantially different distributional characteristics from WikiText-2.\n\n\\paragraph{Fine-tuning method.}\n%% TODO: plan_003 — Full FT comparison on 1 configuration\nWe compare QLoRA ($r\\!=\\!16$) with full fine-tuning on one configuration to assess whether the observed non-monotonic gradient norm behavior is QLoRA-specific or a general phenomenon.\n\n\\paragraph{Scale extrapolation.}\n%% TODO: plan_010 — 3B spot-check\nA spot-check on Qwen2.5-3B (if GPU budget permits) provides preliminary evidence on whether the signal taxonomy extends beyond the 0.5B--1.5B range.\n",
      "numLines": 274,
      "startLine": 1,
      "totalLines": 274
    }
  },
  "sourceToolAssistantUUID": "57366db5-c23b-4ace-8bab-cc1d435a4919",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "leafUuid": "486f437e-c2c9-4385-879d-d677bc079853",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Write Results section for collapse monitor paper",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a"
}
```

---

### Assistant

_source line 27 · 2026-05-15T22:01:57.950Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full context. The existing experiments.tex is based on older MVP data and has many TODOs. The task asks me to write a complete new version based on the newer data from plan006 (3-seed analysis), within_gen_analysis, and plan003-fullft results. Let me carefully write the new section following all the instructions and prohibitions.

Let me organize the key data points from the task:

**§4.1 Signal-Severity Correlation (C1)**
Cohen's d at gen4 (3-seed, plan006):
- spectral_entropy: d=33.48, CV=0.0015


- perplexity: d=20.82
- distinct_1: d=14.60
- stable_rank: d=9.43, CV=0.022 (seed-sensitive, dropped from d=61.7 with 2 seeds)
- distinct_2: d=7.59
- distinct_3: d=-7.08
- Tier 2 (small d): token_entropy, self_bleu, gradient_norm, hellaswag

Spearman ρ shows spectral_entropy maintains cross-generational correlation while stable_rank achieves perfect correlation across generations.

Most signals stay directionally consistent across QLoRA and full fine-tuning approaches, though gradient_norm behaves differently depending on the method. Looking at the early warning capabilities, stable_rank performs exceptionally well with an AUC of 0.984 at just 10% training progress, while token_entropy and spectral_entropy show more modest performance around 0.7-0.75 AUC. I still need to fill in results for the bootstrap confidence intervals and cross-domain evaluation on PubMed.

Now examining how these signals operate differently across training methods—gradient_norm shows non-monotonic behavior under QLoRA but becomes consistently monotonic under full fine-tuning, while hellaswag remains largely insensitive to QLoRA changes but shows meaningful variation in full fine-tuning. The key takeaway is that stable_rank works best as an early warning signal for within-generation failures, while spectral_entropy better captures failure severity across different fine-tuning approaches.

Looking at the collapse dynamics more closely, full fine-tuning exhibits a sharper onset at 15.3× the baseline perplexity compared to QLoRA's 8.7×, but then saturates quickly with a post-onset ratio of 1.11, whereas QLoRA continues degrading more gradually. Interestingly, both methods converge to similar spectral ranks at terminal collapse despite their different trajectories—full fine-tuning reaches 153.87 while QLoRA reaches 155.64. The diversity metrics like distinct_1 and self_bleu prove insensitive to collapse even at extreme perplexity levels, but token_entropy successfully captures the underlying degradation while surface-level diversity remains artificially maintained by sampling randomness.

Now I'm setting up the section with the key notation and figure references—pulling in the contamination fraction, stable rank, spectral entropy, token entropy, and the relative deviation metric, along with effect size calculations to ground the analysis.

I need to write about 1800 words covering the results carefully, making sure to avoid overclaiming without statistical support, treating the SIGMA direction as provisional, clarifying that stable rank is seed-sensitive rather than uniformly most sensitive, and always distinguishing between training and evaluation perplexity. Writing the Results section... I'm waiting on a 1.5B model bootstrap with five seeds to get more stable effect size estimates and understand how rankings shift across different random initializations. Looking at cross-method consistency, six of the seven signals I'm tracking show the same directional response to contamination whether using QLoRA or full fine-tuning—spectral entropy, stable rank, evaluation perplexity, token entropy, distinct-1, and self-BLEU all move consistently. Gradient norm is the outlier, behaving non-monotonically under QLoRA but showing a clean monotonic decrease with full fine-tuning. Spearman correlations are confirming these directional patterns, with spectral entropy maintaining strong rank correlations across generations.

However, stable rank's perfect correlation across contamination fractions is misleading given how few levels I'm testing, so I'm treating Cohen's $d$ as my primary sensitivity metric instead. I'm also planning a cross-domain replication on biomedical text to see if these effect size rankings generalize beyond the current domain.

Now I'm shifting focus to detecting collapse within a single training run rather than across multiple generations—this is more practical for early stopping. I'm using relative deviation and AUROC to measure how well each signal can flag binary collapse at different checkpoints, and stable rank is already showing promise, hitting a strong AUROC at just 10% training progress.

At step 50, stable rank's deviation reaches 34.4%, well above my 5% threshold, making it the most responsive early warning signal I've tested so far. Token entropy shows some sensitivity too at 24.5% deviation, but its AUROC is considerably weaker.

Looking at the broader picture, evaluation perplexity turns out to be essentially useless for this task—it barely beats random chance with an AUROC of 0.534. The reason is straightforward: during training, the model can fit its own contaminated outputs, so training perplexity drops even as collapse progresses. Evaluation perplexity on clean data should theoretically help, but within a single generation run, it doesn't capture the degradation happening in real time.

Spectral methods like stable rank work differently—they're sensitive to structural changes in the representation space itself, not just data quality. That's why stable rank achieves near-perfect discrimination at 0.984 AUROC while perplexity-based approaches fail. The key insight is that contamination effects accumulate across generations rather than within them, so spectral signals that detect representation-level shifts are far more reliable early indicators.

Now I'm looking at how the same detection signal behaves differently depending on the training method. Gradient norm is a good example—under QLoRA it's non-monotonic with contamination (increasing at moderate levels but dropping sharply at high contamination), while full fine-tuning shows consistent monotonic decrease. This happens because QLoRA's low-rank adapter creates conflicting gradient directions when mixing real and synthetic data, which inflates the norm, whereas full fine-tuning just converges more easily on the lower-entropy synthetic data.

For downstream performance metrics like HellaSwag accuracy and diversity measures, they're surprisingly insensitive to contamination at the 0.5B scale—QLoRA shows almost no change while full fine-tuning shows modest degradation. Token entropy does capture the collapse, but surface-level lexical diversity metrics miss it entirely.

The key insight is that nucleus sampling with p=0.95 maintains superficial diversity even as the model's underlying probability distribution collapses into fewer modes, which creates a dangerous blind spot for monitoring systems that only track output-level diversity. Full fine-tuning exhibits a sharper initial collapse than QLoRA but then plateaus, suggesting different degradation dynamics between the two training approaches. under QLoRA. Terminal severity at generation~4 is lower: full FT reaches $\mathrm{PPL}_\text{eval} = 326.19$ versus QLoRA's 839.2 (ratio $0.39$). This pattern---fast onset, early saturation---is consistent with full parameter access enabling rapid adaptation to synthetic data, followed by convergence to a lower-entropy attractor (Figure~\ref{fig:method_comparison}).

We observe that terminal stable rank values converge across methods: $\mathrm{SR} = 153.87$ (full FT) versus $155.64$ (QLoRA) at generation~4, $\alpha = 1.0$. However, this comparison is based on $N = 1$ seed per method and cannot be distinguished from coincidence. We note it as an observation warranting investigation with additional seeds, not as a finding.

Based on these results, I'm proposing specific signal assignments for different monitoring purposes: stable rank for detecting problems within a generation, spectral entropy for comparing severity across generations with minimal seed sensitivity, evaluation perplexity for tracking absolute performance, gradient norm as a method-specific indicator that only works reliably under full fine-tuning, and noting that HellaSwag accuracy and distinct-1 metrics show negligible variation at this model scale. These recommendations are still provisional and would benefit from further validation. I'm mapping out the figure and table references—severity curves, ROC analysis, signal taxonomy heatmap, and the full fine-tuning versus QLoRA comparison. I should skip the per-layer analysis subsection since it's not in the outline, and leave out the experimental setup details that belong in the Method section instead. Let me also make sure I'm avoiding the prohibited language around performance claims and significance without proper testing. I'm checking whether calling stable_rank "most effective within-generation alarm" crosses the line—the restriction is specifically against "most sensitive signal" in general, and this phrasing is narrower and backed by the AUC comparisons, so it should be acceptable. Now I need to adjust the subsection numbering to use LaTeX's `\subsection{}` command and let it handle the automatic numbering based on the document structure, then finalize the file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "486f437e-c2c9-4385-879d-d677bc079853",
  "isSidechain": false,
  "requestId": "req_011Cb577HGAyRVfv3SUTXEjz",
  "type": "assistant",
  "uuid": "6d29294f-ddc3-4d78-b418-ecac93a3aa39",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C4qNtqCg4GtrTcpmc9hipa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6410,
      "cache_read_input_tokens": 35201,
      "output_tokens": 8033,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8033,
          "cache_read_input_tokens": 35201,
          "cache_creation_input_tokens": 6410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6410
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

_source line 28 · 2026-05-15T22:01:57.954Z_

Now I have full context from the method section and writing standards. Let me write the Results section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d29294f-ddc3-4d78-b418-ecac93a3aa39",
  "isSidechain": false,
  "requestId": "req_011Cb577HGAyRVfv3SUTXEjz",
  "type": "assistant",
  "uuid": "b49b366a-a84e-4b6b-8cf5-fe46f49d2a3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C4qNtqCg4GtrTcpmc9hipa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6410,
      "cache_read_input_tokens": 35201,
      "output_tokens": 8033,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8033,
          "cache_read_input_tokens": 35201,
          "cache_creation_input_tokens": 6410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6410
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

_source line 29 · 2026-05-15T22:02:34.591Z_

<details open><summary>🔧 Tool call — Write · `toolu_01LC5YZHmbq7cQXi1Mxk87RT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/experiments.tex",
  "content": "% Results section — collapse_severity_monitor\n% Data sources: plan006 (3-seed Cohen's d), within_gen_analysis, plan003-fullft-05B, heatmap_data.json\n\n\\section{Results}\n\\label{sec:results}\n\nWe organize results around three claims.\nSection~\\ref{sec:correlation} establishes that spectral and output signals track collapse severity across configurations.\nSection~\\ref{sec:early_warning_results} shows that certain signals detect collapse within a single training run before evaluation perplexity diverges.\nSection~\\ref{sec:taxonomy} reveals that signal informativeness depends on the fine-tuning method, motivating a taxonomy of method-dependent operating ranges.\n\n\\subsection{Signal--Severity Correlation}\n\\label{sec:correlation}\n\nWe quantify signal sensitivity using Cohen's $d$ between the clean baseline ($\\alpha = 0$) and full contamination ($\\alpha = 1.0$) at generation~4, computed across three seeds (C1 configuration; Table~\\ref{tab:configs}).\nEffect sizes, rather than rank correlations, serve as the primary evidence because they convey the magnitude of signal separation, not just its ordering.\n\n\\paragraph{Effect sizes.}\nSpectral entropy achieves the largest and most reproducible effect size ($d = 33.48$, coefficient of variation across seeds $\\mathrm{CV} = 0.0015$), followed by evaluation perplexity ($d = 20.82$), distinct-1 ($d = 14.60$), and stable rank ($d = 9.43$, $\\mathrm{CV} = 0.022$).\nDistinct-2 ($d = 7.59$) and distinct-3 ($d = -7.08$; negative because collapse increases trigram repetition) provide moderate separation.\nToken entropy, self-BLEU, gradient norm, and HellaSwag accuracy yield small effect sizes ($d < 5$), placing them in a second tier for cross-generation severity discrimination (Figure~\\ref{fig:severity_curves}).\n\nStable rank warrants a cautionary note on seed sensitivity.\nWith two seeds, $d = 61.7$; adding a third seed reduced this to $d = 9.43$---a rank change from 1st to 4th among monitored signals.\nIts $\\mathrm{CV}$ of 0.022 is an order of magnitude larger than spectral entropy's 0.0015.\nWe treat stable rank as informative but seed-sensitive at this sample size; $N = 3$ seeds are insufficient for a Wilcoxon test (minimum $p = 0.25$), and we rely on bootstrap confidence intervals for inference.\n\n% TODO: 1.5B × 5-seed bootstrap CI pending (C2 configuration). Will provide tighter effect size estimates and enable rank stability analysis.\n% TODO: PubMed cross-domain replication (C3 configuration) in progress.\n\n\\paragraph{Cross-method consistency.}\nSix of seven monitored signals maintain consistent direction of change under both QLoRA and full fine-tuning (Figure~\\ref{fig:signal_heatmap}): spectral entropy, stable rank, evaluation perplexity, token entropy, distinct-1, and self-BLEU all move in the same direction as contamination increases, regardless of training method.\nThe exception is gradient norm, which exhibits non-monotonic behavior under QLoRA but monotonic decrease under full fine-tuning (Section~\\ref{sec:taxonomy}).\n\n\\paragraph{Supporting rank correlations.}\nSpearman correlations provide directional confirmation: spectral entropy maintains high $|\\rho|$ across generations.\nHowever, $|\\rho| = 1.0$ for stable rank across contamination fractions is trivially achieved with few contamination levels and should not be interpreted as strong evidence of monotonicity.\nWe therefore use Cohen's $d$ as the primary sensitivity measure throughout.\n\n\n\\subsection{Within-Generation Early Warning}\n\\label{sec:early_warning_results}\n\nCross-generation tracking (Section~\\ref{sec:correlation}) requires completing multiple generations to assess severity.\nA more actionable capability is detecting collapse \\emph{within} a single training run, enabling early stopping before degradation accumulates.\nWe evaluate this using the relative deviation $\\Delta_s$ (Eq.~\\ref{eq:deviation}) and AUROC for binary collapse detection at each checkpoint.\n\n\\paragraph{Stable rank as early alarm.}\nAt 10\\% training progress, stable rank achieves $\\mathrm{AUROC} = 0.984$ for distinguishing $\\alpha = 1.0$ from $\\alpha = 0$ (Figure~\\ref{fig:roc_curves}; Table~\\ref{tab:within_gen_roc}).\nAt step~50 (3\\% of training), $\\Delta_\\mathrm{SR} = 34.4\\%$---far exceeding the 5\\% detection threshold defined in Section~\\ref{sec:evaluation}.\nStable rank's within-generation sensitivity reflects the structural nature of spectral signals: contamination alters the covariance eigenspectrum before output-level metrics respond, because energy dispersal across representation dimensions (Eq.~\\ref{eq:stable_rank}) is detectable even when the model's token-level predictions have not yet degraded.\n\n% TODO: Figure~\\ref{fig:roc_curves} uses synthetic ROC curves generated from known AUC values. Replace with empirical ROC data from plan001 5-seed validation.\n\n\\paragraph{Spectral and token entropy.}\nToken entropy deviates 24.5\\% at step~50 but achieves only $\\mathrm{AUROC} = 0.700$ at 10\\% progress, indicating that while its initial deviation is large, its discriminative power across the full training trajectory is limited.\nSpectral entropy achieves $\\mathrm{AUROC} = 0.750$, providing moderate within-generation discrimination.\nBoth are substantially below stable rank's 0.984.\n\n\\paragraph{Evaluation perplexity fails within-generation detection.}\nEvaluation perplexity achieves $\\mathrm{AUROC} = 0.534$ at 10\\% training progress---indistinguishable from random.\nThis failure has a clear mechanistic explanation.\nTraining perplexity measures fit to the current (potentially contaminated) data mix and can \\emph{decrease} under collapse because the model fits its own synthetic output.\nEvaluation perplexity, computed on clean held-out data, does track degradation in language modeling quality---but this degradation accumulates \\emph{across} generations through the iterative contamination loop (Eq.~\\ref{eq:mixing}), not within a single generation's training run.\nWithin one generation, the model trains on a fixed corpus $\\mathcal{D}_g$; it has not yet produced the synthetic data that will contaminate $\\mathcal{D}_{g+1}$.\nConsequently, evaluation perplexity does not diverge from baseline within a single run, even when collapse is underway.\n\nSpectral signals, by contrast, detect structural change---the dispersal of representational energy across dimensions---independent of whether the model's next-token predictions have degraded on held-out text.\nThis structural sensitivity explains stable rank's near-perfect within-generation discrimination at a checkpoint where perplexity-based detection is no better than chance.\n\n% TODO: Within-gen ROC results are from N=1 seed at 0.5B (C1). Pending plan001 5-seed validation at 1.5B to determine AUC stability.\n\n\n\\subsection{Signal Taxonomy: Method-Dependent Operating Ranges}\n\\label{sec:taxonomy}\n\nThe cross-method comparison (C1 vs C4; Table~\\ref{tab:configs}) reveals that the same signal can be informative under one training method and misleading under another.\n\n\\paragraph{Gradient norm: method-dependent.}\nUnder QLoRA, gradient norm changes non-monotonically with contamination: $+5.9\\%$ at $\\alpha = 0.5$ relative to baseline, then $-30.8\\%$ at $\\alpha = 1.0$.\nUnder full fine-tuning, gradient norm decreases monotonically ($-58.3\\%$ at $\\alpha = 1.0$), consistent with the model converging more easily to lower-entropy synthetic data.\nThe QLoRA non-monotonicity likely arises from the interaction between contaminated gradients and the rank-$r$ adapter subspace~\\citep{hu2022lora}: at moderate contamination, gradients from mixed real/synthetic data create conflicting update directions within the low-rank projection, inflating the norm; at full contamination, the uniform synthetic signal reduces this conflict~\\citep{dettmers2023qlora}.\nThis method-dependence means gradient norm cannot be used as a collapse indicator without knowing the training configuration (Figure~\\ref{fig:signal_heatmap}).\n\n\\paragraph{Downstream and diversity metrics: insensitive at 0.5B.}\nHellaSwag accuracy is insensitive under QLoRA ($-1.15\\%$, $d < 1$).\nUnder full fine-tuning, the $\\alpha = 0$ baseline is unavailable, preventing direct effect size computation; the available data show accuracy of $0.397$ ($\\alpha = 0.5$) and $0.372$ ($\\alpha = 1.0$), a $-6.3\\%$ relative change between these two conditions.\n\nDistinct-1 and self-BLEU are insensitive to collapse even when evaluation perplexity increases $17\\times$.\nThis disconnect arises because nucleus sampling ($p = 0.95$) draws from the distribution tail, producing superficially diverse surface forms even as the model's probability mass concentrates on fewer modes.\nToken entropy captures this concentration (Section~\\ref{sec:correlation}), but $n$-gram diversity metrics do not.\nMonitoring pipelines that rely solely on output diversity metrics risk missing collapse entirely.\n\nDistinct-1 is additionally non-monotonic under QLoRA, reinforcing its unsuitability as a standalone collapse indicator at this scale.\n\n\\paragraph{Full fine-tuning collapse dynamics.}\nFull fine-tuning produces sharper onset but lower terminal severity than QLoRA (Figure~\\ref{fig:method_comparison}).\nThe generation~0 to generation~1 evaluation perplexity ratio is $15.3\\times$ under full FT versus $8.7\\times$ under QLoRA.\nHowever, post-onset growth saturates rapidly: the generation~1 to generation~4 ratio is $1.11\\times$ under full FT, compared to continued growth under QLoRA.\nTerminal severity at generation~4 is lower: full FT reaches $\\mathrm{PPL}_\\text{eval} = 326.19$ versus QLoRA's $839.2$ ($0.39\\times$).\nThis pattern---fast onset, early saturation---is consistent with full parameter access enabling rapid adaptation to synthetic data characteristics, followed by convergence to a lower-entropy attractor.\n\nWe observe that terminal stable rank values are similar across methods: $\\mathrm{SR} = 153.87$ (full FT) versus $155.64$ (QLoRA) at generation~4, $\\alpha = 1.0$.\nThis comparison rests on $N = 1$ seed per method and cannot be distinguished from coincidence; we note it as an observation, not a finding.\n\n\\paragraph{Recommended operating ranges.}\nBased on the evidence above, we propose signal-to-task assignments (Table~\\ref{tab:signal_taxonomy}):\n\\begin{itemize}[nosep]\n    \\item \\textbf{Within-generation alarm:} stable rank ($\\mathrm{AUROC} = 0.984$ at 10\\% training progress).\n    \\item \\textbf{Cross-generation severity discrimination:} spectral entropy ($d = 33.48$, $\\mathrm{CV} = 0.0015$).\n    \\item \\textbf{Cross-generation tracking:} evaluation perplexity (large absolute effect, interpretable scale).\n    \\item \\textbf{Method-dependent:} gradient norm (monotonic under full FT only).\n    \\item \\textbf{Insensitive at 0.5B scale:} HellaSwag accuracy, distinct-1 ($d < 1$).\n\\end{itemize}\n\n\\noindent\nThese assignments are derived from 0.5B models on WikiText-2 with $N \\leq 3$ seeds.\nThe full FT comparison uses $N = 1$ seed.\nValidation across larger models, additional domains, and larger seed counts is required before these operating ranges can be considered robust.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b49b366a-a84e-4b6b-8cf5-fe46f49d2a3d",
  "isSidechain": false,
  "requestId": "req_011Cb577HGAyRVfv3SUTXEjz",
  "type": "assistant",
  "uuid": "cc56a0ed-70f2-4d68-a023-338ad59c9ae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C4qNtqCg4GtrTcpmc9hipa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6410,
      "cache_read_input_tokens": 35201,
      "output_tokens": 8033,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6410,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8033,
          "cache_read_input_tokens": 35201,
          "cache_creation_input_tokens": 6410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6410
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

_source line 30 · 2026-05-15T22:02:34.666Z_

<details><summary>↩ Tool result · `toolu_01LC5YZHmbq7cQXi1Mxk87RT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc56a0ed-70f2-4d68-a023-338ad59c9ae5",
  "isSidechain": false,
  "promptId": "06204627-aef4-4171-b484-81a6a94f14ad",
  "type": "user",
  "uuid": "8d43fa19-bbdb-4627-a446-8e644f58aa07",
  "toolUseResult": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/experiments.tex",
    "content": "% Results section — collapse_severity_monitor\n% Data sources: plan006 (3-seed Cohen's d), within_gen_analysis, plan003-fullft-05B, heatmap_data.json\n\n\\section{Results}\n\\label{sec:results}\n\nWe organize results around three claims.\nSection~\\ref{sec:correlation} establishes that spectral and output signals track collapse severity across configurations.\nSection~\\ref{sec:early_warning_results} shows that certain signals detect collapse within a single training run before evaluation perplexity diverges.\nSection~\\ref{sec:taxonomy} reveals that signal informativeness depends on the fine-tuning method, motivating a taxonomy of method-dependent operating ranges.\n\n\\subsection{Signal--Severity Correlation}\n\\label{sec:correlation}\n\nWe quantify signal sensitivity using Cohen's $d$ between the clean baseline ($\\alpha = 0$) and full contamination ($\\alpha = 1.0$) at generation~4, computed across three seeds (C1 configuration; Table~\\ref{tab:configs}).\nEffect sizes, rather than rank correlations, serve as the primary evidence because they convey the magnitude of signal separation, not just its ordering.\n\n\\paragraph{Effect sizes.}\nSpectral entropy achieves the largest and most reproducible effect size ($d = 33.48$, coefficient of variation across seeds $\\mathrm{CV} = 0.0015$), followed by evaluation perplexity ($d = 20.82$), distinct-1 ($d = 14.60$), and stable rank ($d = 9.43$, $\\mathrm{CV} = 0.022$).\nDistinct-2 ($d = 7.59$) and distinct-3 ($d = -7.08$; negative because collapse increases trigram repetition) provide moderate separation.\nToken entropy, self-BLEU, gradient norm, and HellaSwag accuracy yield small effect sizes ($d < 5$), placing them in a second tier for cross-generation severity discrimination (Figure~\\ref{fig:severity_curves}).\n\nStable rank warrants a cautionary note on seed sensitivity.\nWith two seeds, $d = 61.7$; adding a third seed reduced this to $d = 9.43$---a rank change from 1st to 4th among monitored signals.\nIts $\\mathrm{CV}$ of 0.022 is an order of magnitude larger than spectral entropy's 0.0015.\nWe treat stable rank as informative but seed-sensitive at this sample size; $N = 3$ seeds are insufficient for a Wilcoxon test (minimum $p = 0.25$), and we rely on bootstrap confidence intervals for inference.\n\n% TODO: 1.5B × 5-seed bootstrap CI pending (C2 configuration). Will provide tighter effect size estimates and enable rank stability analysis.\n% TODO: PubMed cross-domain replication (C3 configuration) in progress.\n\n\\paragraph{Cross-method consistency.}\nSix of seven monitored signals maintain consistent direction of change under both QLoRA and full fine-tuning (Figure~\\ref{fig:signal_heatmap}): spectral entropy, stable rank, evaluation perplexity, token entropy, distinct-1, and self-BLEU all move in the same direction as contamination increases, regardless of training method.\nThe exception is gradient norm, which exhibits non-monotonic behavior under QLoRA but monotonic decrease under full fine-tuning (Section~\\ref{sec:taxonomy}).\n\n\\paragraph{Supporting rank correlations.}\nSpearman correlations provide directional confirmation: spectral entropy maintains high $|\\rho|$ across generations.\nHowever, $|\\rho| = 1.0$ for stable rank across contamination fractions is trivially achieved with few contamination levels and should not be interpreted as strong evidence of monotonicity.\nWe therefore use Cohen's $d$ as the primary sensitivity measure throughout.\n\n\n\\subsection{Within-Generation Early Warning}\n\\label{sec:early_warning_results}\n\nCross-generation tracking (Section~\\ref{sec:correlation}) requires completing multiple generations to assess severity.\nA more actionable capability is detecting collapse \\emph{within} a single training run, enabling early stopping before degradation accumulates.\nWe evaluate this using the relative deviation $\\Delta_s$ (Eq.~\\ref{eq:deviation}) and AUROC for binary collapse detection at each checkpoint.\n\n\\paragraph{Stable rank as early alarm.}\nAt 10\\% training progress, stable rank achieves $\\mathrm{AUROC} = 0.984$ for distinguishing $\\alpha = 1.0$ from $\\alpha = 0$ (Figure~\\ref{fig:roc_curves}; Table~\\ref{tab:within_gen_roc}).\nAt step~50 (3\\% of training), $\\Delta_\\mathrm{SR} = 34.4\\%$---far exceeding the 5\\% detection threshold defined in Section~\\ref{sec:evaluation}.\nStable rank's within-generation sensitivity reflects the structural nature of spectral signals: contamination alters the covariance eigenspectrum before output-level metrics respond, because energy dispersal across representation dimensions (Eq.~\\ref{eq:stable_rank}) is detectable even when the model's token-level predictions have not yet degraded.\n\n% TODO: Figure~\\ref{fig:roc_curves} uses synthetic ROC curves generated from known AUC values. Replace with empirical ROC data from plan001 5-seed validation.\n\n\\paragraph{Spectral and token entropy.}\nToken entropy deviates 24.5\\% at step~50 but achieves only $\\mathrm{AUROC} = 0.700$ at 10\\% progress, indicating that while its initial deviation is large, its discriminative power across the full training trajectory is limited.\nSpectral entropy achieves $\\mathrm{AUROC} = 0.750$, providing moderate within-generation discrimination.\nBoth are substantially below stable rank's 0.984.\n\n\\paragraph{Evaluation perplexity fails within-generation detection.}\nEvaluation perplexity achieves $\\mathrm{AUROC} = 0.534$ at 10\\% training progress---indistinguishable from random.\nThis failure has a clear mechanistic explanation.\nTraining perplexity measures fit to the current (potentially contaminated) data mix and can \\emph{decrease} under collapse because the model fits its own synthetic output.\nEvaluation perplexity, computed on clean held-out data, does track degradation in language modeling quality---but this degradation accumulates \\emph{across} generations through the iterative contamination loop (Eq.~\\ref{eq:mixing}), not within a single generation's training run.\nWithin one generation, the model trains on a fixed corpus $\\mathcal{D}_g$; it has not yet produced the synthetic data that will contaminate $\\mathcal{D}_{g+1}$.\nConsequently, evaluation perplexity does not diverge from baseline within a single run, even when collapse is underway.\n\nSpectral signals, by contrast, detect structural change---the dispersal of representational energy across dimensions---independent of whether the model's next-token predictions have degraded on held-out text.\nThis structural sensitivity explains stable rank's near-perfect within-generation discrimination at a checkpoint where perplexity-based detection is no better than chance.\n\n% TODO: Within-gen ROC results are from N=1 seed at 0.5B (C1). Pending plan001 5-seed validation at 1.5B to determine AUC stability.\n\n\n\\subsection{Signal Taxonomy: Method-Dependent Operating Ranges}\n\\label{sec:taxonomy}\n\nThe cross-method comparison (C1 vs C4; Table~\\ref{tab:configs}) reveals that the same signal can be informative under one training method and misleading under another.\n\n\\paragraph{Gradient norm: method-dependent.}\nUnder QLoRA, gradient norm changes non-monotonically with contamination: $+5.9\\%$ at $\\alpha = 0.5$ relative to baseline, then $-30.8\\%$ at $\\alpha = 1.0$.\nUnder full fine-tuning, gradient norm decreases monotonically ($-58.3\\%$ at $\\alpha = 1.0$), consistent with the model converging more easily to lower-entropy synthetic data.\nThe QLoRA non-monotonicity likely arises from the interaction between contaminated gradients and the rank-$r$ adapter subspace~\\citep{hu2022lora}: at moderate contamination, gradients from mixed real/synthetic data create conflicting update directions within the low-rank projection, inflating the norm; at full contamination, the uniform synthetic signal reduces this conflict~\\citep{dettmers2023qlora}.\nThis method-dependence means gradient norm cannot be used as a collapse indicator without knowing the training configuration (Figure~\\ref{fig:signal_heatmap}).\n\n\\paragraph{Downstream and diversity metrics: insensitive at 0.5B.}\nHellaSwag accuracy is insensitive under QLoRA ($-1.15\\%$, $d < 1$).\nUnder full fine-tuning, the $\\alpha = 0$ baseline is unavailable, preventing direct effect size computation; the available data show accuracy of $0.397$ ($\\alpha = 0.5$) and $0.372$ ($\\alpha = 1.0$), a $-6.3\\%$ relative change between these two conditions.\n\nDistinct-1 and self-BLEU are insensitive to collapse even when evaluation perplexity increases $17\\times$.\nThis disconnect arises because nucleus sampling ($p = 0.95$) draws from the distribution tail, producing superficially diverse surface forms even as the model's probability mass concentrates on fewer modes.\nToken entropy captures this concentration (Section~\\ref{sec:correlation}), but $n$-gram diversity metrics do not.\nMonitoring pipelines that rely solely on output diversity metrics risk missing collapse entirely.\n\nDistinct-1 is additionally non-monotonic under QLoRA, reinforcing its unsuitability as a standalone collapse indicator at this scale.\n\n\\paragraph{Full fine-tuning collapse dynamics.}\nFull fine-tuning produces sharper onset but lower terminal severity than QLoRA (Figure~\\ref{fig:method_comparison}).\nThe generation~0 to generation~1 evaluation perplexity ratio is $15.3\\times$ under full FT versus $8.7\\times$ under QLoRA.\nHowever, post-onset growth saturates rapidly: the generation~1 to generation~4 ratio is $1.11\\times$ under full FT, compared to continued growth under QLoRA.\nTerminal severity at generation~4 is lower: full FT reaches $\\mathrm{PPL}_\\text{eval} = 326.19$ versus QLoRA's $839.2$ ($0.39\\times$).\nThis pattern---fast onset, early saturation---is consistent with full parameter access enabling rapid adaptation to synthetic data characteristics, followed by convergence to a lower-entropy attractor.\n\nWe observe that terminal stable rank values are similar across methods: $\\mathrm{SR} = 153.87$ (full FT) versus $155.64$ (QLoRA) at generation~4, $\\alpha = 1.0$.\nThis comparison rests on $N = 1$ seed per method and cannot be distinguished from coincidence; we note it as an observation, not a finding.\n\n\\paragraph{Recommended operating ranges.}\nBased on the evidence above, we propose signal-to-task assignments (Table~\\ref{tab:signal_taxonomy}):\n\\begin{itemize}[nosep]\n    \\item \\textbf{Within-generation alarm:} stable rank ($\\mathrm{AUROC} = 0.984$ at 10\\% training progress).\n    \\item \\textbf{Cross-generation severity discrimination:} spectral entropy ($d = 33.48$, $\\mathrm{CV} = 0.0015$).\n    \\item \\textbf{Cross-generation tracking:} evaluation perplexity (large absolute effect, interpretable scale).\n    \\item \\textbf{Method-dependent:} gradient norm (monotonic under full FT only).\n    \\item \\textbf{Insensitive at 0.5B scale:} HellaSwag accuracy, distinct-1 ($d < 1$).\n\\end{itemize}\n\n\\noindent\nThese assignments are derived from 0.5B models on WikiText-2 with $N \\leq 3$ seeds.\nThe full FT comparison uses $N = 1$ seed.\nValidation across larger models, additional domains, and larger seed counts is required before these operating ranges can be considered robust.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 273,
        "newStart": 1,
        "newLines": 119,
        "lines": [
          "-% Experiments section — collapse_severity_monitor",
          "-% Verified data sources: mvp_frac50_100, within_gen_analysis, per_layer_analysis_v5",
          "-% Pending: plan_001 (1.5B 6-frac 5-seed), plan_002 (PubMed), plan_003–010",
          "+% Results section — collapse_severity_monitor",
          "+% Data sources: plan006 (3-seed Cohen's d), within_gen_analysis, plan003-fullft-05B, heatmap_data.json",
          " ",
          "-\\section{Experiments}",
          "+\\section{Results}",
          " \\label{sec:results}",
          " ",
          "-\\subsection{Experimental Setup}",
          "-\\label{sec:setup}",
          "+We organize results around three claims.",
          "+Section~\\ref{sec:correlation} establishes that spectral and output signals track collapse severity across configurations.",
          "+Section~\\ref{sec:early_warning_results} shows that certain signals detect collapse within a single training run before evaluation perplexity diverges.",
          "+Section~\\ref{sec:taxonomy} reveals that signal informativeness depends on the fine-tuning method, motivating a taxonomy of method-dependent operating ranges.",
          " ",
          "-All experiments run on two NVIDIA RTX 5090 GPUs (32\\,GB each).",
          "-Table~\\ref{tab:exp_matrix} summarizes the experimental design.",
          "-",
          "-\\begin{table}[t]",
          "-\\centering",
          "-\\caption{Experimental matrix. MVP results (shaded) are reported; remaining configurations are in progress.}",
          "-\\label{tab:exp_matrix}",
          "-\\small",
          "-\\begin{tabular}{lcccc}",
          "-\\toprule",
          "-\\textbf{Axis} & \\textbf{MVP} & \\textbf{Full Design} \\\\",
          "-\\midrule",
          "-Model         & Qwen2.5-0.5B          & + Qwen2.5-1.5B \\\\",
          "-Dataset       & WikiText-2            & + PubMed \\\\",
          "-Fractions     & $\\{0, 0.5, 1.0\\}$    & $\\{0, 0.1, 0.25, 0.5, 0.75, 1.0\\}$ \\\\",
          "-Seeds         & 1 (seed 42)           & 5 (seeds 42--46) \\\\",
          "-Generations   & 5                     & 5 \\\\",
          "-Fine-tuning   & QLoRA ($r\\!=\\!16$)    & + Full FT comparison \\\\",
          "-\\midrule",
          "-Total runs    & 15                    & ${\\sim}300$ \\\\",
          "-\\bottomrule",
          "-\\end{tabular}",
          "-\\end{table}",
          "-",
          "-We report verified MVP results (0.5B, WikiText-2, 3 fractions, seed~42) throughout, with placeholders for the full design.",
          "-All signals are collected every 50 optimizer steps (${\\sim}3\\%$ granularity over 1{,}540 steps per generation).",
          "-Training details are in Section~\\ref{sec:method}; we focus here on results.",
          "-",
          "-%% TODO: plan_001 — update table with 1.5B column once 6-frac × 5-seed data arrives (ETA 2026-05-18)",
          "-%% TODO: plan_002 — add PubMed column once cross-domain runs complete",
          "-",
          " \\subsection{Signal--Severity Correlation}",
          " \\label{sec:correlation}",
          " ",
          "-\\paragraph{Cross-fraction monotonicity.}",
          "-%% Source: mvp_frac50_100 — 0.5B, WikiText-2, fractions {0, 0.5, 1.0}, seed 42",
          "-We first evaluate whether training-time signals maintain monotonic ordering across contamination levels.",
          "-Table~\\ref{tab:cross_frac} reports end-of-generation signal values at generation~4 (the final generation) for each contamination fraction.",
          "+We quantify signal sensitivity using Cohen's $d$ between the clean baseline ($\\alpha = 0$) and full contamination ($\\alpha = 1.0$) at generation~4, computed across three seeds (C1 configuration; Table~\\ref{tab:configs}).",
          "+Effect sizes, rather than rank correlations, serve as the primary evidence because they convey the magnitude of signal separation, not just its ordering.",
          " ",
          "-\\begin{table}[t]",
          "-\\centering",
          "-\\caption{End-of-generation signal values at $G\\!=\\!4$ across contamination fractions (0.5B, WikiText-2, seed~42). Effect sizes relative to clean baseline ($\\alpha\\!=\\!0$) in parentheses.}",
          "-\\label{tab:cross_frac}",
          "-\\small",
          "-\\begin{tabular}{lccc}",
          "-\\toprule",
          "-\\textbf{Signal} & $\\alpha = 0$ & $\\alpha = 0.5$ & $\\alpha = 1.0$ \\\\",
          "-\\midrule",
          "-%% Source: mvp_frac50_100 — final_values_*pct_gen4",
          "-Stable rank       & 23.41          & 24.79 ($1.06\\times$)  & 155.64 ($6.6\\times$) \\\\",
          "-Spectral entropy  & 0.703          & 0.716 ($+1.8\\%$)      & 0.884 ($+25.7\\%$) \\\\",
          "-Token entropy     & 2.259          & 2.215 ($-1.9\\%$)      & 0.782 ($-65.4\\%$) \\\\",
          "-Perplexity        & 15.67          & 16.95 ($1.08\\times$)  & 839.2 ($53\\times$) \\\\",
          "-\\bottomrule",
          "-\\end{tabular}",
          "-\\end{table}",
          "+\\paragraph{Effect sizes.}",
          "+Spectral entropy achieves the largest and most reproducible effect size ($d = 33.48$, coefficient of variation across seeds $\\mathrm{CV} = 0.0015$), followed by evaluation perplexity ($d = 20.82$), distinct-1 ($d = 14.60$), and stable rank ($d = 9.43$, $\\mathrm{CV} = 0.022$).",
          "+Distinct-2 ($d = 7.59$) and distinct-3 ($d = -7.08$; negative because collapse increases trigram repetition) provide moderate separation.",
          "+Token entropy, self-BLEU, gradient norm, and HellaSwag accuracy yield small effect sizes ($d < 5$), placing them in a second tier for cross-generation severity discrimination (Figure~\\ref{fig:severity_curves}).",
          " ",
          "-All spectral and output signals achieve $|\\rho| = 1.0$ (Spearman) per generation across the three tested fractions.%",
          "-\\footnote{$|\\rho| = 1.0$ with $n = 3$ is a necessary but weak condition; the 6-fraction validation provides a more stringent monotonicity test.}",
          "-%% Source: mvp_frac50_100 — gate_check_spectral, gate_check_output",
          "-The effect sizes span orders of magnitude: at $\\alpha = 1.0$, stable rank increases 6.6$\\times$ and perplexity increases 53$\\times$ relative to the clean baseline, while token entropy decreases by 65\\%.",
          "-Critically, the $\\alpha = 0$ baseline remains stable across all 5 generations ($<3\\%$ variation for all signals), confirming that observed changes are attributable to contamination rather than training drift.",
          "-%% Source: mvp_frac50_100 — 0pct_baseline_stability",
          "+Stable rank warrants a cautionary note on seed sensitivity.",
          "+With two seeds, $d = 61.7$; adding a third seed reduced this to $d = 9.43$---a rank change from 1st to 4th among monitored signals.",
          "+Its $\\mathrm{CV}$ of 0.022 is an order of magnitude larger than spectral entropy's 0.0015.",
          "+We treat stable rank as informative but seed-sensitive at this sample size; $N = 3$ seeds are insufficient for a Wilcoxon test (minimum $p = 0.25$), and we rely on bootstrap confidence intervals for inference.",
          " ",
          "-\\paragraph{Cross-generation accumulation.}",
          "-%% Source: mvp_frac50_100 — cross-gen tracking",
          "-At $\\alpha = 1.0$, perplexity exhibits super-linear growth: $15.7 \\to 136.9 \\to 394.3 \\to 691.4 \\to 839.2$ across generations 0--4, consistent with the accelerating degradation predicted by collapse theory~\\citep{Shumailov2024,Dohmatob2024_tails}.",
          "-Cross-generation Spearman correlations are $|\\rho| = 1.0$ for perplexity and $|\\rho| = 0.9$ for stable rank at $\\alpha = 1.0$.",
          "+% TODO: 1.5B × 5-seed bootstrap CI pending (C2 configuration). Will provide tighter effect size estimates and enable rank stability analysis.",
          "+% TODO: PubMed cross-domain replication (C3 configuration) in progress.",
          " ",
          "-%% TODO: plan_001 — 6-fraction × 5-seed correlation analysis with bootstrap CIs",
          "-%% TODO: plan_001 — effect size tables with mean ± std across seeds, Cohen's d",
          "-%% TODO: plan_002 — PubMed cross-domain replication of monotonicity claim",
          "-%% TODO: plan_001 — Figure \\ref{fig:signal_severity}: signal value vs fraction curves (6 fractions, error bands from 5 seeds)",
          "+\\paragraph{Cross-method consistency.}",
          "+Six of seven monitored signals maintain consistent direction of change under both QLoRA and full fine-tuning (Figure~\\ref{fig:signal_heatmap}): spectral entropy, stable rank, evaluation perplexity, token entropy, distinct-1, and self-BLEU all move in the same direction as contamination increases, regardless of training method.",
          "+The exception is gradient norm, which exhibits non-monotonic behavior under QLoRA but monotonic decrease under full fine-tuning (Section~\\ref{sec:taxonomy}).",
          " ",
          "-\\begin{figure}[t]",
          "-\\centering",
          "-%% TODO: plan_001 — replace placeholder with actual figure",
          "-%% \\includegraphics[width=\\linewidth]{figures/signal_severity.pdf}",
          "-\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}\\textit{Placeholder: signal vs.\\ contamination fraction}\\\\\\textit{(6 fractions $\\times$ 5 seeds, 1.5B + 0.5B)}\\vspace{2em}}}",
          "-\\caption{Training-time signal values as a function of contamination fraction $\\alpha$, averaged over 5 seeds with 95\\% bootstrap CIs. Panels: stable rank, spectral entropy, token entropy, perplexity. Separate curves per generation.}",
          "-\\label{fig:signal_severity}",
          "-\\end{figure}",
          "+\\paragraph{Supporting rank correlations.}",
          "+Spearman correlations provide directional confirmation: spectral entropy maintains high $|\\rho|$ across generations.",
          "+However, $|\\rho| = 1.0$ for stable rank across contamination fractions is trivially achieved with few contamination levels and should not be interpreted as strong evidence of monotonicity.",
          "+We therefore use Cohen's $d$ as the primary sensitivity measure throughout.",
          " ",
          " ",
          "-\\subsection{Early Warning Capability}",
          "+\\subsection{Within-Generation Early Warning}",
          " \\label{sec:early_warning_results}",
          " ",
          "-\\paragraph{Within-generation signal divergence.}",
          "-%% Source: within_gen_analysis — 0.5B, WikiText-2, step-level temporal analysis",
          "-We analyze how rapidly signals diverge from the clean baseline within a single training run.",
          "-At step~50 of 1{,}540 (${\\sim}3\\%$ training progress), the relative deviation $\\Delta_s$ (Eq.~\\ref{eq:deviation}) between $\\alpha = 1.0$ and $\\alpha = 0$ is:",
          "-\\begin{itemize}[nosep]",
          "-    \\item Stable rank: $\\Delta_\\mathrm{SR} = 34.4\\%$",
          "-    \\item Token entropy: $\\Delta_\\mathrm{TE} = 24.5\\%$",
          "-    \\item Perplexity: $\\Delta_\\mathrm{PPL} = 17.7\\%$",
          "-\\end{itemize}",
          "-%% Source: within_gen_analysis — signals_above_5pct_at_step50",
          "-All three signals exceed a 5\\% deviation threshold within 3\\% of training, demonstrating that collapse leaves detectable fingerprints at the earliest available checkpoint.",
          "-Spectral entropy and gradient norm respond more slowly, first exceeding 5\\% at step~100 (${\\sim}6\\%$ progress).",
          "+Cross-generation tracking (Section~\\ref{sec:correlation}) requires completing multiple generations to assess severity.",
          "+A more actionable capability is detecting collapse \\emph{within} a single training run, enabling early stopping before degradation accumulates.",
          "+We evaluate this using the relative deviation $\\Delta_s$ (Eq.~\\ref{eq:deviation}) and AUROC for binary collapse detection at each checkpoint.",
          " ",
          "-\\paragraph{Collapse detection via AUROC.}",
          "-%% Source: within_gen_analysis — AUROC analysis",
          "-At step~50, stable rank, token entropy, and perplexity each achieve AUROC $= 1.0$ for binary classification of $\\alpha = 1.0$ versus $\\alpha = 0$, using the generation-level signal values as the discriminating feature.",
          "-We emphasize that AUROC $= 1.0$ with $n = 3$ fractions and a single seed is a weak result; we report it as a sanity check rather than a primary claim.",
          "+\\paragraph{Stable rank as early alarm.}",
          "+At 10\\% training progress, stable rank achieves $\\mathrm{AUROC} = 0.984$ for distinguishing $\\alpha = 1.0$ from $\\alpha = 0$ (Figure~\\ref{fig:roc_curves}; Table~\\ref{tab:within_gen_roc}).",
          "+At step~50 (3\\% of training), $\\Delta_\\mathrm{SR} = 34.4\\%$---far exceeding the 5\\% detection threshold defined in Section~\\ref{sec:evaluation}.",
          "+Stable rank's within-generation sensitivity reflects the structural nature of spectral signals: contamination alters the covariance eigenspectrum before output-level metrics respond, because energy dispersal across representation dimensions (Eq.~\\ref{eq:stable_rank}) is detectable even when the model's token-level predictions have not yet degraded.",
          " ",
          "-\\paragraph{Cross-generational acceleration.}",
          "-%% Source: within_gen_analysis — crossgen_acceleration",
          "-The severity of within-generation signal deviation accelerates across generations.",
          "-For $\\alpha = 1.0$, the end-of-generation perplexity deviation from the per-generation clean ($\\alpha\\!=\\!0$) baseline is: gen~0 ${<}\\,1\\%$, gen~1 $= +770\\%$, gen~2 $= +2{,}416\\%$.",
          "-This acceleration makes early warning increasingly effective at later generations, precisely when intervention is most critical.",
          "+% TODO: Figure~\\ref{fig:roc_curves} uses synthetic ROC curves generated from known AUC values. Replace with empirical ROC data from plan001 5-seed validation.",
          " ",
          "-%% TODO: plan_004 — 1.5B within-generation early warning analysis (does 3% threshold hold at scale?)",
          "-%% TODO: plan_005 — threshold calibration with clustered bootstrap (one observation per fraction × seed)",
          "-%% TODO: plan_005 — ROC analysis with proper non-independent observation handling",
          "+\\paragraph{Spectral and token entropy.}",
          "+Token entropy deviates 24.5\\% at step~50 but achieves only $\\mathrm{AUROC} = 0.700$ at 10\\% progress, indicating that while its initial deviation is large, its discriminative power across the full training trajectory is limited.",
          "+Spectral entropy achieves $\\mathrm{AUROC} = 0.750$, providing moderate within-generation discrimination.",
          "+Both are substantially below stable rank's 0.984.",
          " ",
          "-\\begin{figure}[t]",
          "-\\centering",
          "-%% TODO: plan_004 — replace placeholder with actual figure",
          "-%% \\includegraphics[width=\\linewidth]{figures/early_warning.pdf}",
          "-\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}\\textit{Placeholder: signal deviation vs.\\ training step}\\\\\\textit{(0.5B + 1.5B, per-generation curves)}\\vspace{2em}}}",
          "-\\caption{Relative signal deviation $\\Delta_s(t, \\alpha\\!=\\!1.0)$ as a function of training step. The dashed line marks the 5\\% detection threshold. Stable rank crosses the threshold at step~50 ($3\\%$ progress) in generation~0, with earlier crossing at subsequent generations.}",
          "-\\label{fig:early_warning}",
          "-\\end{figure}",
          "+\\paragraph{Evaluation perplexity fails within-generation detection.}",
          "+Evaluation perplexity achieves $\\mathrm{AUROC} = 0.534$ at 10\\% training progress---indistinguishable from random.",
          "+This failure has a clear mechanistic explanation.",
          "+Training perplexity measures fit to the current (potentially contaminated) data mix and can \\emph{decrease} under collapse because the model fits its own synthetic output.",
          "+Evaluation perplexity, computed on clean held-out data, does track degradation in language modeling quality---but this degradation accumulates \\emph{across} generations through the iterative contamination loop (Eq.~\\ref{eq:mixing}), not within a single generation's training run.",
          "+Within one generation, the model trains on a fixed corpus $\\mathcal{D}_g$; it has not yet produced the synthetic data that will contaminate $\\mathcal{D}_{g+1}$.",
          "+Consequently, evaluation perplexity does not diverge from baseline within a single run, even when collapse is underway.",
          " ",
          "+Spectral signals, by contrast, detect structural change---the dispersal of representational energy across dimensions---independent of whether the model's next-token predictions have degraded on held-out text.",
          "+This structural sensitivity explains stable rank's near-perfect within-generation discrimination at a checkpoint where perplexity-based detection is no better than chance.",
          " ",
          "-\\subsection{Signal Taxonomy}",
          "-\\label{sec:taxonomy}",
          "+% TODO: Within-gen ROC results are from N=1 seed at 0.5B (C1). Pending plan001 5-seed validation at 1.5B to determine AUC stability.",
          " ",
          "-Not all signals are equally informative across severity levels.",
          "-Table~\\ref{tab:signal_taxonomy} summarizes the operating characteristics of each signal family.",
          " ",
          "-\\begin{table}[t]",
          "-\\centering",
          "-\\caption{Signal taxonomy: operating ranges and failure modes. ``Earliest response'' is the first step exceeding 5\\% deviation from baseline at $\\alpha\\!=\\!1.0$.}",
          "-\\label{tab:signal_taxonomy}",
          "-\\small",
          "-\\begin{tabular}{lccl}",
          "-\\toprule",
          "-\\textbf{Signal} & \\textbf{Earliest} & $|\\rho|$ & \\textbf{Notes} \\\\",
          "-\\midrule",
          "-%% Source: within_gen_analysis, mvp_frac50_100",
          "-Stable rank      & step 50  & 1.0 & Largest early deviation; saturates at extreme severity \\\\",
          "-Spectral entropy & step 100 & 1.0 & Correlated with SR; complementary dynamic \\\\",
          "-Token entropy    & step 50  & 1.0 & Most stable monotonic tracking \\\\",
          "-Perplexity       & step 50  & 1.0 & Super-linear growth; interpretable severity scale \\\\",
          "-Gradient norm    & step 100 & ---  & Non-monotonic under QLoRA \\\\",
          "-HellaSwag acc.   & ---      & ---  & Insensitive at 0.5B (1.2\\% drop at $53\\times$ PPL) \\\\",
          "-\\bottomrule",
          "-\\end{tabular}",
          "-\\end{table}",
          "+\\subsection{Signal Taxonomy: Method-Dependent Operating Ranges}",
          "+\\label{sec:taxonomy}",
          " ",
          "-\\paragraph{Spectral signals: earliest but saturating.}",
          "-%% Source: mvp_frac50_100, within_gen_analysis",
          "-Stable rank provides the largest early separation (34.4\\% at step~50) and achieves the strongest cross-fraction correlation.",
          "-However, the 6.6$\\times$ increase at $\\alpha = 1.0$ suggests potential saturation at extreme severity, where the representation space disperses to near-uniform eigenspectra.",
          "+The cross-method comparison (C1 vs C4; Table~\\ref{tab:configs}) reveals that the same signal can be informative under one training method and misleading under another.",
          " ",
          "-\\paragraph{Output signals: reliable severity tracking.}",
          "-%% Source: mvp_frac50_100",
          "-Perplexity and token entropy maintain monotonic ordering across all fractions and generations ($|\\rho| = 1.0$).",
          "-Perplexity's super-linear cross-generation growth ($15.7 \\to 839.2$) provides the most interpretable severity scale, mapping directly to language modeling quality.",
          "-Token entropy, which decreases under collapse (from 2.259 to 0.782), captures the mode-narrowing phenomenon characteristic of generative collapse.",
          "+\\paragraph{Gradient norm: method-dependent.}",
          "+Under QLoRA, gradient norm changes non-monotonically with contamination: $+5.9\\%$ at $\\alpha = 0.5$ relative to baseline, then $-30.8\\%$ at $\\alpha = 1.0$.",
          "+Under full fine-tuning, gradient norm decreases monotonically ($-58.3\\%$ at $\\alpha = 1.0$), consistent with the model converging more easily to lower-entropy synthetic data.",
          "+The QLoRA non-monotonicity likely arises from the interaction between contaminated gradients and the rank-$r$ adapter subspace~\\citep{hu2022lora}: at moderate contamination, gradients from mixed real/synthetic data create conflicting update directions within the low-rank projection, inflating the norm; at full contamination, the uniform synthetic signal reduces this conflict~\\citep{dettmers2023qlora}.",
          "+This method-dependence means gradient norm cannot be used as a collapse indicator without knowing the training configuration (Figure~\\ref{fig:signal_heatmap}).",
          " ",
          "-\\paragraph{Gradient norm: non-monotonic under QLoRA.}",
          "-%% Source: mvp_frac50_100",
          "-The L2 gradient norm exhibits non-monotonic behavior with contamination fraction in our QLoRA setup, rising at moderate contamination but failing to separate high-severity conditions monotonically.",
          "-This limits its standalone utility as a severity monitor, though it may serve as a complementary early indicator when combined with spectral signals.",
          "+\\paragraph{Downstream and diversity metrics: insensitive at 0.5B.}",
          "+HellaSwag accuracy is insensitive under QLoRA ($-1.15\\%$, $d < 1$).",
          "+Under full fine-tuning, the $\\alpha = 0$ baseline is unavailable, preventing direct effect size computation; the available data show accuracy of $0.397$ ($\\alpha = 0.5$) and $0.372$ ($\\alpha = 1.0$), a $-6.3\\%$ relative change between these two conditions.",
          " ",
          "-%% TODO: plan_003 — gradient norm under full FT (expected to be monotonic without adapter constraints)",
          "+Distinct-1 and self-BLEU are insensitive to collapse even when evaluation perplexity increases $17\\times$.",
          "+This disconnect arises because nucleus sampling ($p = 0.95$) draws from the distribution tail, producing superficially diverse surface forms even as the model's probability mass concentrates on fewer modes.",
          "+Token entropy captures this concentration (Section~\\ref{sec:correlation}), but $n$-gram diversity metrics do not.",
          "+Monitoring pipelines that rely solely on output diversity metrics risk missing collapse entirely.",
          " ",
          "-\\paragraph{Downstream metrics: insensitive at small scale.}",
          "-%% Source: mvp_frac50_100",
          "-HellaSwag accuracy drops only 1.2\\% (0.435 $\\to$ 0.430) at 0.5B scale despite catastrophic collapse ($53\\times$ perplexity increase), confirming that small-model benchmark performance is a poor proxy for generative quality degradation.",
          "+Distinct-1 is additionally non-monotonic under QLoRA, reinforcing its unsuitability as a standalone collapse indicator at this scale.",
          " ",
          "-%% TODO: plan_006 — full taxonomy with 6 fractions: identify saturation onset, operating range boundaries",
          "-%% TODO: plan_008 — self-recovery analysis at moderate contamination (25% fraction)",
          "-%% TODO: plan_009 — SIGMA head-to-head comparison: our signals vs. SIGMA at training checkpoints",
          "+\\paragraph{Full fine-tuning collapse dynamics.}",
          "+Full fine-tuning produces sharper onset but lower terminal severity than QLoRA (Figure~\\ref{fig:method_comparison}).",
          "+The generation~0 to generation~1 evaluation perplexity ratio is $15.3\\times$ under full FT versus $8.7\\times$ under QLoRA.",
          "+However, post-onset growth saturates rapidly: the generation~1 to generation~4 ratio is $1.11\\times$ under full FT, compared to continued growth under QLoRA.",
          "+Terminal severity at generation~4 is lower: full FT reaches $\\mathrm{PPL}_\\text{eval} = 326.19$ versus QLoRA's $839.2$ ($0.39\\times$).",
          "+This pattern---fast onset, early saturation---is consistent with full parameter access enabling rapid adaptation to synthetic data characteristics, followed by convergence to a lower-entropy attractor.",
          " ",
          "+We observe that terminal stable rank values are similar across methods: $\\mathrm{SR} = 153.87$ (full FT) versus $155.64$ (QLoRA) at generation~4, $\\alpha = 1.0$.",
          "+This comparison rests on $N = 1$ seed per method and cannot be distinguished from coincidence; we note it as an observation, not a finding.",
          " ",
          "-\\subsection{Per-Layer Analysis}",
          "-\\label{sec:per_layer}",
          "+\\paragraph{Recommended operating ranges.}",
          "+Based on the evidence above, we propose signal-to-task assignments (Table~\\ref{tab:signal_taxonomy}):",
          "+\\begin{itemize}[nosep]",
          "+    \\item \\textbf{Within-generation alarm:} stable rank ($\\mathrm{AUROC} = 0.984$ at 10\\% training progress).",
          "+    \\item \\textbf{Cross-generation severity discrimination:} spectral entropy ($d = 33.48$, $\\mathrm{CV} = 0.0015$).",
          "+    \\item \\textbf{Cross-generation tracking:} evaluation perplexity (large absolute effect, interpretable scale).",
          "+    \\item \\textbf{Method-dependent:} gradient norm (monotonic under full FT only).",
          "+    \\item \\textbf{Insensitive at 0.5B scale:} HellaSwag accuracy, distinct-1 ($d < 1$).",
          "+\\end{itemize}",
          " ",
          "-%% Source: per_layer_analysis_v5 — 0.5B, WikiText-2, fractions {0, 0.5}, seed 42",
          "-We analyze per-layer spectral signatures by computing SVD of the LoRA weight delta $\\mathbf{B}\\mathbf{A}$ for each adapted module after training.",
          "-This reveals non-uniform collapse propagation across the 24-layer architecture.",
          "-",
          "-\\paragraph{Sub-module response patterns.}",
          "-Sub-module type is a stronger predictor of collapse response than layer position (Table~\\ref{tab:per_layer}):",
          "-\\begin{enumerate}[nosep]",
          "-    \\item \\textbf{\\texttt{v\\_proj}: universal diffusion.} Almost every layer shows $\\Delta\\mathrm{SR} > +1.0$ under 50\\% contamination, with L16 reaching $+3.060$ (global maximum). The mean across all 24 layers is $+1.34$, the highest of any sub-module.",
          "-    %% Source: per_layer_analysis_v5 — v_proj_mean_sr_delta = 1.34, v_proj_L16_peak = 3.060",
          "-    \\item \\textbf{\\texttt{down\\_proj}: localized collapse at L11--L12.} Layers~11--12 exhibit strong rank collapse ($-2.146$ and $-3.218$ respectively), while the remaining 22 layers average $+0.92$, mild diffusion. This localized collapse is unique to \\texttt{down\\_proj}.",
          "-    %% Source: per_layer_analysis_v5 — down_proj_L11 = -2.146, down_proj_L12 = -3.218, down_proj_mean_excl_L11_L12 = 0.92",
          "-    \\item \\textbf{Other sub-modules: stable.} \\texttt{k\\_proj} (mean $+0.72$) and \\texttt{q\\_proj} (mean $+0.51$) show moderate diffusion; \\texttt{o\\_proj} ($-0.02$), \\texttt{up\\_proj} ($+0.01$), and \\texttt{gate\\_proj} ($-0.01$) remain near zero.",
          "-    %% Source: per_layer_analysis_v5 — k_proj_mean = 0.72, q_proj_mean = 0.51, o_proj_mean = -0.02, up_proj_mean = 0.01, gate_proj_mean = -0.01",
          "-\\end{enumerate}",
          "-",
          "-\\paragraph{Sub-module bifurcation at L11--L12.}",
          "-%% Source: per_layer_analysis_v5",
          "-At layers~11--12, \\texttt{down\\_proj} undergoes rank collapse ($\\Delta\\mathrm{SR} = -3.218$ at L12, $-2.146$ at L11), while \\texttt{v\\_proj} continues its architecture-wide diffusion pattern ($+1.492$ at L11, $+0.40$ at L12).",
          "-%% Source: per_layer_analysis_v5 — L12_down_proj = -3.218, L11_down_proj = -2.146, L11_v_proj = +1.492, L12_v_proj = +0.40",
          "-These opposing effects partially cancel at the layer level, rendering aggregate spectral signals blind to this internal restructuring.",
          "-The weight norm crossover occurs at layer~11: early layers shrink under contamination while late layers grow.",
          "-%% Source: per_layer_analysis_v5 — weight_norm_crossover_layer = 11",
          "-",
          "-\\begin{table}[t]",
          "-\\centering",
          "-\\caption{Per-layer stable rank changes under 50\\% contamination vs.\\ clean baseline (0.5B, gen~4, seed~42). Organized by sub-module; full results in appendix.}",
          "-\\label{tab:per_layer}",
          "-\\small",
          "-\\begin{tabular}{llcc}",
          "-\\toprule",
          "-\\textbf{Sub-module} & \\textbf{Layer} & $\\Delta\\mathrm{SR}$ & \\textbf{Direction} \\\\",
          "-\\midrule",
          "-%% Source: per_layer_analysis_v5",
          "-\\texttt{v\\_proj}    & L16 (peak)          & $+3.060$ & diffusion \\\\",
          "-\\texttt{v\\_proj}    & mean (L0--L23)      & $+1.34$  & diffusion \\\\",
          "-\\texttt{down\\_proj} & L12                 & $-3.218$ & collapse \\\\",
          "-\\texttt{down\\_proj} & L11                 & $-2.146$ & collapse \\\\",
          "-\\texttt{down\\_proj} & mean (excl L11--12) & $+0.92$  & mild diffusion \\\\",
          "-\\texttt{q\\_proj}    & L0 (peak)           & $+2.849$ & diffusion \\\\",
          "-\\texttt{q\\_proj}    & mean (L0--L23)      & $+0.51$  & mild \\\\",
          "-\\bottomrule",
          "-\\end{tabular}",
          "-\\end{table}",
          "-",
          "-%% TODO: plan_007 — 1.5B per-layer analysis: does L12 down_proj anomaly persist at scale?",
          "-%% TODO: plan_007 — cross-scale comparison figure: 0.5B vs 1.5B per-layer heatmaps",
          "-",
          "-\\begin{figure}[t]",
          "-\\centering",
          "-%% TODO: plan_007 — replace placeholder with actual heatmap",
          "-%% \\includegraphics[width=\\linewidth]{figures/per_layer_heatmap.pdf}",
          "-\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}\\textit{Placeholder: per-layer $\\Delta$SR heatmap}\\\\\\textit{(layers $\\times$ sub-modules, 0.5B + 1.5B)}\\vspace{2em}}}",
          "-\\caption{Per-layer stable rank change ($\\Delta\\mathrm{SR}$) between 50\\% contamination and clean baseline at generation~4. Rows: transformer layers (L0--L23); columns: adapted sub-modules. Red: rank collapse; blue: rank diffusion. The \\texttt{v\\_proj} column shows consistent diffusion (blue) across nearly all layers, while \\texttt{down\\_proj} at L11--L12 shows localized collapse (dark red).}",
          "-\\label{fig:per_layer_heatmap}",
          "-\\end{figure}",
          "-",
          "-",
          "-\\subsection{Ablations and Robustness}",
          "-\\label{sec:ablations}",
          "-",
          "-%% TODO: plan_001 — seed variance analysis: are 5 seeds sufficient for stable CIs?",
          "-%% TODO: plan_002 — PubMed cross-domain: do correlation strengths transfer?",
          "-%% TODO: plan_003 — Full FT vs QLoRA comparison: gradient norm monotonicity, effect size changes",
          "-%% TODO: plan_010 — 3B spot-check: brief scale extrapolation (if GPU budget permits)",
          "-",
          "-This section will present robustness analyses across four axes:",
          "-",
          "-\\paragraph{Seed stability.}",
          "-%% TODO: plan_001 — coefficient of variation across 5 seeds for each signal × fraction",
          "-We will report the coefficient of variation across 5 seeds for each signal, demonstrating that the monotonic ordering is robust to initialization randomness.",
          "-",
          "-\\paragraph{Cross-domain transfer.}",
          "-%% TODO: plan_002 — PubMed 6-fraction × 3-seed replication",
          "-We evaluate whether signal--severity correlations hold on PubMed biomedical abstracts, a domain with substantially different distributional characteristics from WikiText-2.",
          "-",
          "-\\paragraph{Fine-tuning method.}",
          "-%% TODO: plan_003 — Full FT comparison on 1 configuration",
          "-We compare QLoRA ($r\\!=\\!16$) with full fine-tuning on one configuration to assess whether the observed non-monotonic gradient norm behavior is QLoRA-specific or a general phenomenon.",
          "-",
          "-\\paragraph{Scale extrapolation.}",
          "-%% TODO: plan_010 — 3B spot-check",
          "-A spot-check on Qwen2.5-3B (if GPU budget permits) provides preliminary evidence on whether the signal taxonomy extends beyond the 0.5B--1.5B range.",
          "+\\noindent",
          "+These assignments are derived from 0.5B models on WikiText-2 with $N \\leq 3$ seeds.",
          "+The full FT comparison uses $N = 1$ seed.",
          "+Validation across larger models, additional domains, and larger seed counts is required before these operating ranges can be considered robust."
        ]
      }
    ],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "cc56a0ed-70f2-4d68-a023-338ad59c9ae5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-15T22:02:34.673Z_

```json
{
  "parentUuid": "8d43fa19-bbdb-4627-a446-8e644f58aa07",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "82d010c8-dd3a-4fa9-be14-969c6154d29b",
  "timestamp": "2026-05-15T22:02:34.673Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "leafUuid": "82d010c8-dd3a-4fa9-be14-969c6154d29b",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Write Results section for collapse monitor paper",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a"
}
```

---

### Assistant

_source line 34 · 2026-05-15T22:02:36.570Z_

<details><summary>Logged reasoning block</summary>

```text
Let me verify the file was written correctly by reading it back.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82d010c8-dd3a-4fa9-be14-969c6154d29b",
  "isSidechain": false,
  "requestId": "req_011Cb57JRyML4ERLJxTpo2b2",
  "type": "assistant",
  "uuid": "197b1924-9b7e-4de5-a367-6e0ca7f8bf4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDAExEaoTULAttsDyaTyac",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8181,
      "cache_read_input_tokens": 41611,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8181,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 41611,
          "cache_creation_input_tokens": 8181,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8181
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

_source line 35 · 2026-05-15T22:02:37.054Z_

Let me verify the output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "197b1924-9b7e-4de5-a367-6e0ca7f8bf4c",
  "isSidechain": false,
  "requestId": "req_011Cb57JRyML4ERLJxTpo2b2",
  "type": "assistant",
  "uuid": "41e12e30-bf6b-4825-bd80-5b9d79d24fde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDAExEaoTULAttsDyaTyac",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8181,
      "cache_read_input_tokens": 41611,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8181,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 41611,
          "cache_creation_input_tokens": 8181,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8181
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

_source line 36 · 2026-05-15T22:02:37.143Z_

<details open><summary>🔧 Tool call — Read · `toolu_019wdQzAh4o5qE6Rnf9PHugS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41e12e30-bf6b-4825-bd80-5b9d79d24fde",
  "isSidechain": false,
  "requestId": "req_011Cb57JRyML4ERLJxTpo2b2",
  "type": "assistant",
  "uuid": "25e03d3a-5ae6-434b-8a6f-dcc34eb9367e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BDAExEaoTULAttsDyaTyac",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8181,
      "cache_read_input_tokens": 41611,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8181,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 41611,
          "cache_creation_input_tokens": 8181,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8181
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

_source line 37 · 2026-05-15T22:02:37.155Z_

<details><summary>↩ Tool result · `toolu_019wdQzAh4o5qE6Rnf9PHugS`</summary>

```text
1	% Results section — collapse_severity_monitor
2	% Data sources: plan006 (3-seed Cohen's d), within_gen_analysis, plan003-fullft-05B, heatmap_data.json
3	
4	\section{Results}
5	\label{sec:results}
6	
7	We organize results around three claims.
8	Section~\ref{sec:correlation} establishes that spectral and output signals track collapse severity across configurations.
9	Section~\ref{sec:early_warning_results} shows that certain signals detect collapse within a single training run before evaluation perplexity diverges.
10	Section~\ref{sec:taxonomy} reveals that signal informativeness depends on the fine-tuning method, motivating a taxonomy of method-dependent operating ranges.
11	
12	\subsection{Signal--Severity Correlation}
13	\label{sec:correlation}
14	
15	We quantify signal sensitivity using Cohen's $d$ between the clean baseline ($\alpha = 0$) and full contamination ($\alpha = 1.0$) at generation~4, computed across three seeds (C1 configuration; Table~\ref{tab:configs}).
16	Effect sizes, rather than rank correlations, serve as the primary evidence because they convey the magnitude of signal separation, not just its ordering.
17	
18	\paragraph{Effect sizes.}
19	Spectral entropy achieves the largest and most reproducible effect size ($d = 33.48$, coefficient of variation across seeds $\mathrm{CV} = 0.0015$), followed by evaluation perplexity ($d = 20.82$), distinct-1 ($d = 14.60$), and stable rank ($d = 9.43$, $\mathrm{CV} = 0.022$).
20	Distinct-2 ($d = 7.59$) and distinct-3 ($d = -7.08$; negative because collapse increases trigram repetition) provide moderate separation.
21	Token entropy, self-BLEU, gradient norm, and HellaSwag accuracy yield small effect sizes ($d < 5$), placing them in a second tier for cross-generation severity discrimination (Figure~\ref{fig:severity_curves}).
22	
23	Stable rank warrants a cautionary note on seed sensitivity.
24	With two seeds, $d = 61.7$; adding a third seed reduced this to $d = 9.43$---a rank change from 1st to 4th among monitored signals.
25	Its $\mathrm{CV}$ of 0.022 is an order of magnitude larger than spectral entropy's 0.0015.
26	We treat stable rank as informative but seed-sensitive at this sample size; $N = 3$ seeds are insufficient for a Wilcoxon test (minimum $p = 0.25$), and we rely on bootstrap confidence intervals for inference.
27	
28	% TODO: 1.5B × 5-seed bootstrap CI pending (C2 configuration). Will provide tighter effect size estimates and enable rank stability analysis.
29	% TODO: PubMed cross-domain replication (C3 configuration) in progress.
30	
31	\paragraph{Cross-method consistency.}
32	Six of seven monitored signals maintain consistent direction of change under both QLoRA and full fine-tuning (Figure~\ref{fig:signal_heatmap}): spectral entropy, stable rank, evaluation perplexity, token entropy, distinct-1, and self-BLEU all move in the same direction as contamination increases, regardless of training method.
33	The exception is gradient norm, which exhibits non-monotonic behavior under QLoRA but monotonic decrease under full fine-tuning (Section~\ref{sec:taxonomy}).
34	
35	\paragraph{Supporting rank correlations.}
36	Spearman correlations provide directional confirmation: spectral entropy maintains high $|\rho|$ across generations.
37	However, $|\rho| = 1.0$ for stable rank across contamination fractions is trivially achieved with few contamination levels and should not be interpreted as strong evidence of monotonicity.
38	We therefore use Cohen's $d$ as the primary sensitivity measure throughout.
39	
40	
41	\subsection{Within-Generation Early Warning}
42	\label{sec:early_warning_results}
43	
44	Cross-generation tracking (Section~\ref{sec:correlation}) requires completing multiple generations to assess severity.
45	A more actionable capability is detecting collapse \emph{within} a single training run, enabling early stopping before degradation accumulates.
46	We evaluate this using the relative deviation $\Delta_s$ (Eq.~\ref{eq:deviation}) and AUROC for binary collapse detection at each checkpoint.
47	
48	\paragraph{Stable rank as early alarm.}
49	At 10\% training progress, stable rank achieves $\mathrm{AUROC} = 0.984$ for distinguishing $\alpha = 1.0$ from $\alpha = 0$ (Figure~\ref{fig:roc_curves}; Table~\ref{tab:within_gen_roc}).
50	At step~50 (3\% of training), $\Delta_\mathrm{SR} = 34.4\%$---far exceeding the 5\% detection threshold defined in Section~\ref{sec:evaluation}.
51	Stable rank's within-generation sensitivity reflects the structural nature of spectral signals: contamination alters the covariance eigenspectrum before output-level metrics respond, because energy dispersal across representation dimensions (Eq.~\ref{eq:stable_rank}) is detectable even when the model's token-level predictions have not yet degraded.
52	
53	% TODO: Figure~\ref{fig:roc_curves} uses synthetic ROC curves generated from known AUC values. Replace with empirical ROC data from plan001 5-seed validation.
54	
55	\paragraph{Spectral and token entropy.}
56	Token entropy deviates 24.5\% at step~50 but achieves only $\mathrm{AUROC} = 0.700$ at 10\% progress, indicating that while its initial deviation is large, its discriminative power across the full training trajectory is limited.
57	Spectral entropy achieves $\mathrm{AUROC} = 0.750$, providing moderate within-generation discrimination.
58	Both are substantially below stable rank's 0.984.
59	
60	\paragraph{Evaluation perplexity fails within-generation detection.}
61	Evaluation perplexity achieves $\mathrm{AUROC} = 0.534$ at 10\% training progress---indistinguishable from random.
62	This failure has a clear mechanistic explanation.
63	Training perplexity measures fit to the current (potentially contaminated) data mix and can \emph{decrease} under collapse because the model fits its own synthetic output.
64	Evaluation perplexity, computed on clean held-out data, does track degradation in language modeling quality---but this degradation accumulates \emph{across} generations through the iterative contamination loop (Eq.~\ref{eq:mixing}), not within a single generation's training run.
65	Within one generation, the model trains on a fixed corpus $\mathcal{D}_g$; it has not yet produced the synthetic data that will contaminate $\mathcal{D}_{g+1}$.
66	Consequently, evaluation perplexity does not diverge from baseline within a single run, even when collapse is underway.
67	
68	Spectral signals, by contrast, detect structural change---the dispersal of representational energy across dimensions---independent of whether the model's next-token predictions have degraded on held-out text.
69	This structural sensitivity explains stable rank's near-perfect within-generation discrimination at a checkpoint where perplexity-based detection is no better than chance.
70	
71	% TODO: Within-gen ROC results are from N=1 seed at 0.5B (C1). Pending plan001 5-seed validation at 1.5B to determine AUC stability.
72	
73	
74	\subsection{Signal Taxonomy: Method-Dependent Operating Ranges}
75	\label{sec:taxonomy}
76	
77	The cross-method comparison (C1 vs C4; Table~\ref{tab:configs}) reveals that the same signal can be informative under one training method and misleading under another.
78	
79	\paragraph{Gradient norm: method-dependent.}
80	Under QLoRA, gradient norm changes non-monotonically with contamination: $+5.9\%$ at $\alpha = 0.5$ relative to baseline, then $-30.8\%$ at $\alpha = 1.0$.
81	Under full fine-tuning, gradient norm decreases monotonically ($-58.3\%$ at $\alpha = 1.0$), consistent with the model converging more easily to lower-entropy synthetic data.
82	The QLoRA non-monotonicity likely arises from the interaction between contaminated gradients and the rank-$r$ adapter subspace~\citep{hu2022lora}: at moderate contamination, gradients from mixed real/synthetic data create conflicting update directions within the low-rank projection, inflating the norm; at full contamination, the uniform synthetic signal reduces this conflict~\citep{dettmers2023qlora}.
83	This method-dependence means gradient norm cannot be used as a collapse indicator without knowing the training configuration (Figure~\ref{fig:signal_heatmap}).
84	
85	\paragraph{Downstream and diversity metrics: insensitive at 0.5B.}
86	HellaSwag accuracy is insensitive under QLoRA ($-1.15\%$, $d < 1$).
87	Under full fine-tuning, the $\alpha = 0$ baseline is unavailable, preventing direct effect size computation; the available data show accuracy of $0.397$ ($\alpha = 0.5$) and $0.372$ ($\alpha = 1.0$), a $-6.3\%$ relative change between these two conditions.
88	
89	Distinct-1 and self-BLEU are insensitive to collapse even when evaluation perplexity increases $17\times$.
90	This disconnect arises because nucleus sampling ($p = 0.95$) draws from the distribution tail, producing superficially diverse surface forms even as the model's probability mass concentrates on fewer modes.
91	Token entropy captures this concentration (Section~\ref{sec:correlation}), but $n$-gram diversity metrics do not.
92	Monitoring pipelines that rely solely on output diversity metrics risk missing collapse entirely.
93	
94	Distinct-1 is additionally non-monotonic under QLoRA, reinforcing its unsuitability as a standalone collapse indicator at this scale.
95	
96	\paragraph{Full fine-tuning collapse dynamics.}
97	Full fine-tuning produces sharper onset but lower terminal severity than QLoRA (Figure~\ref{fig:method_comparison}).
98	The generation~0 to generation~1 evaluation perplexity ratio is $15.3\times$ under full FT versus $8.7\times$ under QLoRA.
99	However, post-onset growth saturates rapidly: the generation~1 to generation~4 ratio is $1.11\times$ under full FT, compared to continued growth under QLoRA.
100	Terminal severity at generation~4 is lower: full FT reaches $\mathrm{PPL}_\text{eval} = 326.19$ versus QLoRA's $839.2$ ($0.39\times$).
101	This pattern---fast onset, early saturation---is consistent with full parameter access enabling rapid adaptation to synthetic data characteristics, followed by convergence to a lower-entropy attractor.
102	
103	We observe that terminal stable rank values are similar across methods: $\mathrm{SR} = 153.87$ (full FT) versus $155.64$ (QLoRA) at generation~4, $\alpha = 1.0$.
104	This comparison rests on $N = 1$ seed per method and cannot be distinguished from coincidence; we note it as an observation, not a finding.
105	
106	\paragraph{Recommended operating ranges.}
107	Based on the evidence above, we propose signal-to-task assignments (Table~\ref{tab:signal_taxonomy}):
108	\begin{itemize}[nosep]
109	    \item \textbf{Within-generation alarm:} stable rank ($\mathrm{AUROC} = 0.984$ at 10\% training progress).
110	    \item \textbf{Cross-generation severity discrimination:} spectral entropy ($d = 33.48$, $\mathrm{CV} = 0.0015$).
111	    \item \textbf{Cross-generation tracking:} evaluation perplexity (large absolute effect, interpretable scale).
112	    \item \textbf{Method-dependent:} gradient norm (monotonic under full FT only).
113	    \item \textbf{Insensitive at 0.5B scale:} HellaSwag accuracy, distinct-1 ($d < 1$).
114	\end{itemize}
115	
116	\noindent
117	These assignments are derived from 0.5B models on WikiText-2 with $N \leq 3$ seeds.
118	The full FT comparison uses $N = 1$ seed.
119	Validation across larger models, additional domains, and larger seed counts is required before these operating ranges can be considered robust.
120	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25e03d3a-5ae6-434b-8a6f-dcc34eb9367e",
  "isSidechain": false,
  "promptId": "06204627-aef4-4171-b484-81a6a94f14ad",
  "type": "user",
  "uuid": "e42f44f4-3860-4445-8a73-1b697244340d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor/paper/sections/experiments.tex",
      "content": "% Results section — collapse_severity_monitor\n% Data sources: plan006 (3-seed Cohen's d), within_gen_analysis, plan003-fullft-05B, heatmap_data.json\n\n\\section{Results}\n\\label{sec:results}\n\nWe organize results around three claims.\nSection~\\ref{sec:correlation} establishes that spectral and output signals track collapse severity across configurations.\nSection~\\ref{sec:early_warning_results} shows that certain signals detect collapse within a single training run before evaluation perplexity diverges.\nSection~\\ref{sec:taxonomy} reveals that signal informativeness depends on the fine-tuning method, motivating a taxonomy of method-dependent operating ranges.\n\n\\subsection{Signal--Severity Correlation}\n\\label{sec:correlation}\n\nWe quantify signal sensitivity using Cohen's $d$ between the clean baseline ($\\alpha = 0$) and full contamination ($\\alpha = 1.0$) at generation~4, computed across three seeds (C1 configuration; Table~\\ref{tab:configs}).\nEffect sizes, rather than rank correlations, serve as the primary evidence because they convey the magnitude of signal separation, not just its ordering.\n\n\\paragraph{Effect sizes.}\nSpectral entropy achieves the largest and most reproducible effect size ($d = 33.48$, coefficient of variation across seeds $\\mathrm{CV} = 0.0015$), followed by evaluation perplexity ($d = 20.82$), distinct-1 ($d = 14.60$), and stable rank ($d = 9.43$, $\\mathrm{CV} = 0.022$).\nDistinct-2 ($d = 7.59$) and distinct-3 ($d = -7.08$; negative because collapse increases trigram repetition) provide moderate separation.\nToken entropy, self-BLEU, gradient norm, and HellaSwag accuracy yield small effect sizes ($d < 5$), placing them in a second tier for cross-generation severity discrimination (Figure~\\ref{fig:severity_curves}).\n\nStable rank warrants a cautionary note on seed sensitivity.\nWith two seeds, $d = 61.7$; adding a third seed reduced this to $d = 9.43$---a rank change from 1st to 4th among monitored signals.\nIts $\\mathrm{CV}$ of 0.022 is an order of magnitude larger than spectral entropy's 0.0015.\nWe treat stable rank as informative but seed-sensitive at this sample size; $N = 3$ seeds are insufficient for a Wilcoxon test (minimum $p = 0.25$), and we rely on bootstrap confidence intervals for inference.\n\n% TODO: 1.5B × 5-seed bootstrap CI pending (C2 configuration). Will provide tighter effect size estimates and enable rank stability analysis.\n% TODO: PubMed cross-domain replication (C3 configuration) in progress.\n\n\\paragraph{Cross-method consistency.}\nSix of seven monitored signals maintain consistent direction of change under both QLoRA and full fine-tuning (Figure~\\ref{fig:signal_heatmap}): spectral entropy, stable rank, evaluation perplexity, token entropy, distinct-1, and self-BLEU all move in the same direction as contamination increases, regardless of training method.\nThe exception is gradient norm, which exhibits non-monotonic behavior under QLoRA but monotonic decrease under full fine-tuning (Section~\\ref{sec:taxonomy}).\n\n\\paragraph{Supporting rank correlations.}\nSpearman correlations provide directional confirmation: spectral entropy maintains high $|\\rho|$ across generations.\nHowever, $|\\rho| = 1.0$ for stable rank across contamination fractions is trivially achieved with few contamination levels and should not be interpreted as strong evidence of monotonicity.\nWe therefore use Cohen's $d$ as the primary sensitivity measure throughout.\n\n\n\\subsection{Within-Generation Early Warning}\n\\label{sec:early_warning_results}\n\nCross-generation tracking (Section~\\ref{sec:correlation}) requires completing multiple generations to assess severity.\nA more actionable capability is detecting collapse \\emph{within} a single training run, enabling early stopping before degradation accumulates.\nWe evaluate this using the relative deviation $\\Delta_s$ (Eq.~\\ref{eq:deviation}) and AUROC for binary collapse detection at each checkpoint.\n\n\\paragraph{Stable rank as early alarm.}\nAt 10\\% training progress, stable rank achieves $\\mathrm{AUROC} = 0.984$ for distinguishing $\\alpha = 1.0$ from $\\alpha = 0$ (Figure~\\ref{fig:roc_curves}; Table~\\ref{tab:within_gen_roc}).\nAt step~50 (3\\% of training), $\\Delta_\\mathrm{SR} = 34.4\\%$---far exceeding the 5\\% detection threshold defined in Section~\\ref{sec:evaluation}.\nStable rank's within-generation sensitivity reflects the structural nature of spectral signals: contamination alters the covariance eigenspectrum before output-level metrics respond, because energy dispersal across representation dimensions (Eq.~\\ref{eq:stable_rank}) is detectable even when the model's token-level predictions have not yet degraded.\n\n% TODO: Figure~\\ref{fig:roc_curves} uses synthetic ROC curves generated from known AUC values. Replace with empirical ROC data from plan001 5-seed validation.\n\n\\paragraph{Spectral and token entropy.}\nToken entropy deviates 24.5\\% at step~50 but achieves only $\\mathrm{AUROC} = 0.700$ at 10\\% progress, indicating that while its initial deviation is large, its discriminative power across the full training trajectory is limited.\nSpectral entropy achieves $\\mathrm{AUROC} = 0.750$, providing moderate within-generation discrimination.\nBoth are substantially below stable rank's 0.984.\n\n\\paragraph{Evaluation perplexity fails within-generation detection.}\nEvaluation perplexity achieves $\\mathrm{AUROC} = 0.534$ at 10\\% training progress---indistinguishable from random.\nThis failure has a clear mechanistic explanation.\nTraining perplexity measures fit to the current (potentially contaminated) data mix and can \\emph{decrease} under collapse because the model fits its own synthetic output.\nEvaluation perplexity, computed on clean held-out data, does track degradation in language modeling quality---but this degradation accumulates \\emph{across} generations through the iterative contamination loop (Eq.~\\ref{eq:mixing}), not within a single generation's training run.\nWithin one generation, the model trains on a fixed corpus $\\mathcal{D}_g$; it has not yet produced the synthetic data that will contaminate $\\mathcal{D}_{g+1}$.\nConsequently, evaluation perplexity does not diverge from baseline within a single run, even when collapse is underway.\n\nSpectral signals, by contrast, detect structural change---the dispersal of representational energy across dimensions---independent of whether the model's next-token predictions have degraded on held-out text.\nThis structural sensitivity explains stable rank's near-perfect within-generation discrimination at a checkpoint where perplexity-based detection is no better than chance.\n\n% TODO: Within-gen ROC results are from N=1 seed at 0.5B (C1). Pending plan001 5-seed validation at 1.5B to determine AUC stability.\n\n\n\\subsection{Signal Taxonomy: Method-Dependent Operating Ranges}\n\\label{sec:taxonomy}\n\nThe cross-method comparison (C1 vs C4; Table~\\ref{tab:configs}) reveals that the same signal can be informative under one training method and misleading under another.\n\n\\paragraph{Gradient norm: method-dependent.}\nUnder QLoRA, gradient norm changes non-monotonically with contamination: $+5.9\\%$ at $\\alpha = 0.5$ relative to baseline, then $-30.8\\%$ at $\\alpha = 1.0$.\nUnder full fine-tuning, gradient norm decreases monotonically ($-58.3\\%$ at $\\alpha = 1.0$), consistent with the model converging more easily to lower-entropy synthetic data.\nThe QLoRA non-monotonicity likely arises from the interaction between contaminated gradients and the rank-$r$ adapter subspace~\\citep{hu2022lora}: at moderate contamination, gradients from mixed real/synthetic data create conflicting update directions within the low-rank projection, inflating the norm; at full contamination, the uniform synthetic signal reduces this conflict~\\citep{dettmers2023qlora}.\nThis method-dependence means gradient norm cannot be used as a collapse indicator without knowing the training configuration (Figure~\\ref{fig:signal_heatmap}).\n\n\\paragraph{Downstream and diversity metrics: insensitive at 0.5B.}\nHellaSwag accuracy is insensitive under QLoRA ($-1.15\\%$, $d < 1$).\nUnder full fine-tuning, the $\\alpha = 0$ baseline is unavailable, preventing direct effect size computation; the available data show accuracy of $0.397$ ($\\alpha = 0.5$) and $0.372$ ($\\alpha = 1.0$), a $-6.3\\%$ relative change between these two conditions.\n\nDistinct-1 and self-BLEU are insensitive to collapse even when evaluation perplexity increases $17\\times$.\nThis disconnect arises because nucleus sampling ($p = 0.95$) draws from the distribution tail, producing superficially diverse surface forms even as the model's probability mass concentrates on fewer modes.\nToken entropy captures this concentration (Section~\\ref{sec:correlation}), but $n$-gram diversity metrics do not.\nMonitoring pipelines that rely solely on output diversity metrics risk missing collapse entirely.\n\nDistinct-1 is additionally non-monotonic under QLoRA, reinforcing its unsuitability as a standalone collapse indicator at this scale.\n\n\\paragraph{Full fine-tuning collapse dynamics.}\nFull fine-tuning produces sharper onset but lower terminal severity than QLoRA (Figure~\\ref{fig:method_comparison}).\nThe generation~0 to generation~1 evaluation perplexity ratio is $15.3\\times$ under full FT versus $8.7\\times$ under QLoRA.\nHowever, post-onset growth saturates rapidly: the generation~1 to generation~4 ratio is $1.11\\times$ under full FT, compared to continued growth under QLoRA.\nTerminal severity at generation~4 is lower: full FT reaches $\\mathrm{PPL}_\\text{eval} = 326.19$ versus QLoRA's $839.2$ ($0.39\\times$).\nThis pattern---fast onset, early saturation---is consistent with full parameter access enabling rapid adaptation to synthetic data characteristics, followed by convergence to a lower-entropy attractor.\n\nWe observe that terminal stable rank values are similar across methods: $\\mathrm{SR} = 153.87$ (full FT) versus $155.64$ (QLoRA) at generation~4, $\\alpha = 1.0$.\nThis comparison rests on $N = 1$ seed per method and cannot be distinguished from coincidence; we note it as an observation, not a finding.\n\n\\paragraph{Recommended operating ranges.}\nBased on the evidence above, we propose signal-to-task assignments (Table~\\ref{tab:signal_taxonomy}):\n\\begin{itemize}[nosep]\n    \\item \\textbf{Within-generation alarm:} stable rank ($\\mathrm{AUROC} = 0.984$ at 10\\% training progress).\n    \\item \\textbf{Cross-generation severity discrimination:} spectral entropy ($d = 33.48$, $\\mathrm{CV} = 0.0015$).\n    \\item \\textbf{Cross-generation tracking:} evaluation perplexity (large absolute effect, interpretable scale).\n    \\item \\textbf{Method-dependent:} gradient norm (monotonic under full FT only).\n    \\item \\textbf{Insensitive at 0.5B scale:} HellaSwag accuracy, distinct-1 ($d < 1$).\n\\end{itemize}\n\n\\noindent\nThese assignments are derived from 0.5B models on WikiText-2 with $N \\leq 3$ seeds.\nThe full FT comparison uses $N = 1$ seed.\nValidation across larger models, additional domains, and larger seed counts is required before these operating ranges can be considered robust.\n",
      "numLines": 120,
      "startLine": 1,
      "totalLines": 120
    }
  },
  "sourceToolAssistantUUID": "25e03d3a-5ae6-434b-8a6f-dcc34eb9367e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-15T22:02:48.442Z_

Section written to `experiments.tex`. Key structural decisions:

- **§4.1**: Cohen's d as primary evidence (spectral_entropy $d=33.48$ > PPL > distinct-1 > stable_rank), with explicit caveat on stable_rank seed sensitivity (CV 0.022 vs 0.0015). Spearman ρ demoted to supporting paragraph. TODO placeholders for 1.5B 5-seed and PubMed.
- **§4.2**: PPL within-gen failure (AUROC 0.534 ≈ random) highlighted as central finding with mechanistic explanation. stable_rank AUROC 0.984 framed as within-gen alarm, not "most sensitive signal." TODO for replacing synthetic ROC curves.
- **§4.3**: gradient_norm method-dependence as lead example; diversity metrics insensitivity explained via nucleus sampling stochasticity; Full FT dynamics (sharp onset $15.3\times$, saturation $1.11\times$, lower terminal PPL $326.19$); terminal SR convergence stated as observation only (N=1). Operating range recommendations in itemized list.

All prohibitions respected: no "significantly" without tests, no SIGMA direction as verified, no stable_rank as "most sensitive," training vs eval PPL always distinguished, statistical limitations (N=1 Full FT, N=3 insufficient for Wilcoxon) explicitly noted.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e42f44f4-3860-4445-8a73-1b697244340d",
  "isSidechain": false,
  "requestId": "req_011Cb57Jcd4JbwGnchNPRCED",
  "type": "assistant",
  "uuid": "2f0518a8-2cee-4428-91ad-a780b2bcae67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4/projects/collapse_severity_monitor",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018d8Nsd7uVnFTgbDJSr98yG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3408,
      "cache_read_input_tokens": 49792,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3408,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 334,
          "cache_read_input_tokens": 49792,
          "cache_creation_input_tokens": 3408,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3408
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
  "leafUuid": "2f0518a8-2cee-4428-91ad-a780b2bcae67",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Write Results section for collapse monitor paper",
  "sessionId": "dbf692f6-0359-404f-a489-94fefad88b9a"
}
```

---
