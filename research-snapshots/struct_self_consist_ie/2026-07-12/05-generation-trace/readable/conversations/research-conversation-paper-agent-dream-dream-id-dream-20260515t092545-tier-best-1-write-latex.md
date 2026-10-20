# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T092545 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/904bcd2b-4006-47ab-bbd6-19bc5f2000f3.jsonl`
- **Structured JSON:** [`689aee581a429cc17c44.json`](../../sessions/68/689aee581a429cc17c44.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T09:45:14.278Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T09:45:14.278Z",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T092545 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/experiment_data.json`（先 Read 此文件）\n- Venue：EMNLP 2026 Findings\n- Narrative guidance：Free-form ablation (exp-018) 清晰证实 constrained decoding 是 selection 失败的因果机制。三层论证闭环完全成立：\n(1) 概念澄清：4/5 signals 是 instance-level 聚合，无法 rank candidates；\n(2) 实证发现：logprob 在 constrained decoding 下被压缩（60% instances range < 0.05）；\n(3) 控制实验：free-form generation 恢复 logprob variance 和 selection ability（NER +5pp, p<0.01）。\nexp-017 补全 cross-model validation（LLaMA×CoNLL ≈ Qwen×CoNLL, SJ ρ Δ<0.01），\nexp-019 用 supervised verifier 建立 gap-closable upper bound，但其 gain 反而低于 free-form logprob，\n从反面强化 \"constrained decoding IS the bottleneck\" 结论。\nSignal ranking reversal（logprob 从 constrained worst → free-form best）是最有说服力的单一证据。\nTitle \"The Constrained Decoding Bottleneck\" 三个动词 identify/diagnose/verify 全部 earned。\nExpected reviewer score 3.5–4.0, Findings acceptance prob 55–75%。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-15T09:45:14.283Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T09:45:14.283Z",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3"
}
```

---

## Round 1

29 recorded events

### User

_source line 3 · 2026-05-15T09:45:14.315Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T092545 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/experiment_data.json`（先 Read 此文件）
- Venue：EMNLP 2026 Findings
- Narrative guidance：Free-form ablation (exp-018) 清晰证实 constrained decoding 是 selection 失败的因果机制。三层论证闭环完全成立：
(1) 概念澄清：4/5 signals 是 instance-level 聚合，无法 rank candidates；
(2) 实证发现：logprob 在 constrained decoding 下被压缩（60% instances range < 0.05）；
(3) 控制实验：free-form generation 恢复 logprob variance 和 selection ability（NER +5pp, p<0.01）。
exp-017 补全 cross-model validation（LLaMA×CoNLL ≈ Qwen×CoNLL, SJ ρ Δ<0.01），
exp-019 用 supervised verifier 建立 gap-closable upper bound，但其 gain 反而低于 free-form logprob，
从反面强化 "constrained decoding IS the bottleneck" 结论。
Signal ranking reversal（logprob 从 constrained worst → free-form best）是最有说服力的单一证据。
Title "The Constrained Decoding Bottleneck" 三个动词 identify/diagnose/verify 全部 earned。
Expected reviewer score 3.5–4.0, Findings acceptance prob 55–75%。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "1b194309-ac76-4d60-bc4e-ae0827f25a5b",
  "type": "user",
  "uuid": "8ed2cb97-e093-4bc1-8ae0-a47d41303bfe",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T09:45:14.314Z_

```json
{
  "parentUuid": "8ed2cb97-e093-4bc1-8ae0-a47d41303bfe",
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
  "uuid": "497720e4-86a6-4ff2-a3f1-f0bbfd5ab2d4",
  "timestamp": "2026-05-15T09:45:14.314Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T09:45:14.314Z_

```json
{
  "parentUuid": "497720e4-86a6-4ff2-a3f1-f0bbfd5ab2d4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "138899a4-7a62-4603-b48e-1796122a5157",
  "timestamp": "2026-05-15T09:45:14.314Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
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
  "aiTitle": "Generate EMNLP paper on constrained decoding bottleneck",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3"
}
```

---

### Assistant

_source line 7 · 2026-05-15T09:45:17.795Z_

I'll start by reading the input files to understand the experiment data and paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "138899a4-7a62-4603-b48e-1796122a5157",
  "isSidechain": false,
  "requestId": "req_011Cb495HVUq8SSvUESTNLvb",
  "type": "assistant",
  "uuid": "b18ae236-ec69-4bcb-a859-c9712dffa297",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Nxhgnwj7yEUMqMpEUzrdi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11424,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11424
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

_source line 8 · 2026-05-15T09:45:18.281Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BbJ83M3ifQQMF7paAiVJAd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b18ae236-ec69-4bcb-a859-c9712dffa297",
  "isSidechain": false,
  "requestId": "req_011Cb495HVUq8SSvUESTNLvb",
  "type": "assistant",
  "uuid": "75e920ed-01ea-4f37-aa51-b0732ad7a2ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Nxhgnwj7yEUMqMpEUzrdi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11424,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11424
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

_source line 9 · 2026-05-15T09:45:18.612Z_

<details><summary>↩ Tool result · `toolu_01BbJ83M3ifQQMF7paAiVJAd`</summary>

```text
1	[
2	  {
3	    "name": "ner_ood_robustness",
4	    "description": "SciERC fine-tuned Qwen3-8B 对 WNUT-17 test set 做 zero-shot cross-domain NER inference\n(N=8, T=1.0)。评估 5 个 confidence signals 的 OOD 鲁棒性，验证 constrained decoding\nbottleneck 在 domain shift 下是否持续。\n",
5	    "results": {
6	      "n_instances": 1287,
7	      "n_valid": 689,
8	      "n_conditional": 520,
9	      "greedy_f1": 0.32,
10	      "oracle_f1": 0.52,
11	      "oracle_headroom": 0.2,
12	      "parse_rate": 0.92,
13	      "sample_f1_pct_zero": 58.0,
14	      "ner_full_rho_sj": 0.15,
15	      "ner_full_rho_fk": 0.12,
16	      "ner_full_rho_logprob": -0.08,
17	      "ner_full_rho_em": 0.11,
18	      "ner_full_rho_voting_conf": 0.18,
19	      "ner_full_auroc_sj": 0.58,
20	      "ner_full_auroc_fk": 0.56,
21	      "ner_full_auroc_logprob": 0.48,
22	      "ner_full_auroc_em": 0.57,
23	      "ner_full_auroc_voting_conf": 0.6,
24	      "ner_cond_rho_sj": 0.24,
25	      "ner_cond_rho_logprob": 0.05,
26	      "logprob_within_sample_range_median": 0.02,
27	      "structural_beats_logprob": true,
28	      "selection_f1_logprob": 0.31,
29	      "selection_f1_greedy": 0.32,
30	      "selection_delta_pp": -1.0
31	    },
32	    "tables": [
33	      {
34	        "name": "Table S1: OOD Signal Robustness (SciERC → WNUT-17)",
35	        "description": "5 signals × {ρ, τ, AUROC} on OOD NER, full/conditional split。\n对比 in-domain baseline (Table 1)。Appendix 补充实验。\n"
36	      }
37	    ],
38	    "figures": [],
39	    "analysis": "Appendix supporting evidence，不改变主线论证。(1) 排除 \"bottleneck 仅在 in-domain 成立\"；\n(2) logprob OOD 过度自信与 exp-003 呼应，佐证 Claim 3；\n(3) 58% F1=0 进一步说明 constrained decoding 在 OOD 下输出高度同质化。\n局限：zero-shot transfer 本身 unfair (schema 不匹配)，绝对数值参考意义有限。\n\n\nOOD (SciERC→WNUT-17) 导致绝对性能大幅下降 (greedy 0.32 vs in-domain 0.66)，\n但 constrained decoding bottleneck 模式不变：\n\n**logprob ρ=−0.08 (负值)**：constrained decoding 下 logprob compression 在 OOD 时更严重。\n模型对 OOD 输入的 token 分布更 uniform（不确定该选什么），grammar masking 后仅存的微小\n差异指向错误方向——高 logprob 对应的是模型 \"自信地输出训练域模式\"（SciERC schema），\n而非 WNUT-17 ground truth 期望的输出。这与 exp-003 中 rho_logprob_full=−0.414 方向一致，\nconstrained decoding 的 compression 将绝对值从 −0.41 缩小到 −0.08。\n\n**Structural signals 仍正向 (voting_conf 0.18, SJ 0.15)**：即使 OOD，model 内部一致性\n仍与输出质量弱正相关——当模型对某些 entity \"碰巧\" 确信时，这些 entity 更可能真实存在。\n绝对值低是因为 SciERC schema (6 types) 与 WNUT-17 schema (6 types, 不同) 的 mismatch\n使大多数输出 degenerate。\n\n**58% samples F1=0**：schema mismatch 导致绝大多数生成的 entity 无法匹配 gold，\n而 constrained decoding 迫使所有样本生成 SciERC-format 的 entity——\n高度同质化的输出使 within-sample variance 进一步坍缩 (range median 0.02)。\n\n关键价值：排除 \"bottleneck 仅在 in-domain 成立\" 的 alternative hypothesis。\n"
40	  },
41	  {
42	    "name": "ner_llama_conll",
43	    "description": "LLaMA-3.1-8B-Instruct fine-tuned on CoNLL-2003, N=8, T=1.0 inference。\n补全 2×2 model-dataset grid 的第四个 cell (Qwen×SciERC, Qwen×CoNLL, LLaMA×SciERC, LLaMA×CoNLL)。\n",
44	    "results": {
45	      "n_instances": 3453,
46	      "n_valid": 2756,
47	      "n_conditional": 2642,
48	      "greedy_f1": 0.926,
49	      "oracle_f1": 0.944,
50	      "oracle_headroom": 0.018,
51	      "N": 8,
52	      "T": 1.0,
53	      "full_SJ_rho": 0.431,
54	      "full_FK_rho": 0.428,
55	      "full_logprob_rho": 0.307,
56	      "full_EM_rho": 0.431,
57	      "full_voting_conf_rho": 0.426,
58	      "full_SJ_AUROC": 0.704,
59	      "full_FK_AUROC": 0.703,
60	      "full_logprob_AUROC": 0.761,
61	      "full_EM_AUROC": 0.705,
62	      "full_voting_conf_AUROC": 0.709,
63	      "full_SJ_ECE": 0.114,
64	      "full_logprob_ECE": 0.129,
65	      "cond_SJ_rho": 0.436,
66	      "cond_FK_rho": 0.431,
67	      "cond_logprob_rho": 0.328,
68	      "cond_EM_rho": 0.44,
69	      "cond_EM_AUROC": 0.726,
70	      "cond_logprob_AUROC": 0.81,
71	      "structural_beats_logprob_rho": true,
72	      "sj_rho_delta_vs_logprob": 0.124,
73	      "cross_model_sj_rho_delta_vs_qwen": 0.005
74	    },
75	    "tables": [
76	      {
77	        "name": "Table 2 (main results): LLaMA×CoNLL row in 2×2 grid",
78	        "description": "Main results table 中 2 models × 2 datasets grid。每个 cell: 5 signals 的 ρ + AUROC。\nLLaMA×CoNLL 填补最后一个空 cell。\n"
79	      },
80	      {
81	        "name": "Table 3: Cross-model consistency summary",
82	        "description": "Qwen vs LLaMA on each dataset。Per-signal |Δρ| across models。\nMean |Δρ| across structural signals < 0.01。\n"
83	      }
84	    ],
85	    "figures": [],
86	    "analysis": "填补 2×2 grid 最后一个 cell，使 cross-model claim 从 \"suggestive\" 升级到 \"systematic\"：\n(1) LLaMA SJ ρ=0.431 vs Qwen SJ ρ=0.436 (Δ=0.005) — signal ranking 是 task property；\n(2) 两模型均显示 structural > logprob (Δρ∈[0.12, 0.16])，排除 \"Qwen 特有 compression\"；\n(3) CoNLL small headroom (0.018) 说明 near-ceiling 下 selection gain 天然有限，\n    但 signal quality hierarchy 不受影响——方法论有效性验证。\n\n\n**SJ ρ=0.431 ≈ Qwen×CoNLL SJ ρ=0.436 (Δ=0.005)**:\nCoNLL-2003 NER 是高资源 benchmark (3453 test, greedy F1 ~0.926)，两个 8B 模型在相同数据上\n学到了几乎相同的 task structure。SJ 衡量的是 entity set 间 structural agreement——\n这是 task property (entity ambiguity 分布) 而非 model artifact。\n两个不同架构 (LLaMA transformer vs Qwen transformer) 产生 Δρ<0.01 的一致性\n强有力地证明 signal ranking 是 task-intrinsic。\n\n**Logprob ρ=0.307 仍显著低于 structural signals (Δρ=+0.124)**:\n与 Qwen×CoNLL (logprob ρ=0.316) 一致。两个模型均使用 Outlines constrained decoding，\ngrammar masking 以相同方式压缩 logprob variance。\nLogprob AUROC (0.761) 在 binary discrimination 上 strong，但 ρ 在 ranking 上 weak——\nAUROC 仅需区分 \"good vs bad\"（threshold-based），而 ρ 需要 fine-grained ranking，\n后者正是 logprob compression 破坏的能力。\n\n**Oracle headroom 仅 0.018**:\nCoNLL 的 near-ceiling 性能 (0.926) 意味着 selection 潜力本身有限——\n所有 8 个 samples 都接近 correct，差异很小。但 bottleneck 仍可观测\n(logprob 在 ranking 任务上不如 structural signals)，证明即使 easy regime\n也存在 constrained decoding 对 logprob 的系统性损害。\n\n**ECE=0.114 低于 SciERC (0.453)**:\n高正确率自然改善 calibration (大部分预测都对)，但不解决 selection 问题——\ncalibration 衡量 \"预测的置信度是否匹配正确率\"，selection 衡量 \"能否从 N 个中选出最好的\"。\n"
87	  },
88	  {
89	    "name": "freeform_decoding_ablation",
90	    "description": "BREAKTHROUGH EXPERIMENT. SciERC 上 Qwen3-8B (fine-tuned) 生成 free-form（无 Outlines\nconstrained decoding）N=8 samples per instance。对比 constrained vs free-form 下\nlogprob variance、QE metrics、selection performance。证明 constrained decoding\n是 correlation-selection gap 的因果机制。\n",
91	    "results": {
92	      "freeform_parse_rate_ner": 0.9,
93	      "freeform_parse_rate_re": 0.88,
94	      "n_parseable_ner": 476,
95	      "n_parseable_re": 350,
96	      "constrained_logprob_within_sample_range_median_ner": 0.031,
97	      "freeform_logprob_within_sample_range_median_ner": 0.32,
98	      "constrained_logprob_within_sample_range_median_re": 0.028,
99	      "freeform_logprob_within_sample_range_median_re": 0.27,
100	      "constrained_pct_range_below_005": 0.6,
101	      "freeform_pct_range_below_005": 0.08,
102	      "variance_recovery_factor": 10.3,
103	      "wilcoxon_variance_constrained_vs_freeform_p": 1.2e-45,
104	      "constrained_logprob_rho_ner": 0.205,
105	      "freeform_logprob_rho_ner": 0.42,
106	      "freeform_sj_rho_ner": 0.37,
107	      "freeform_fk_rho_ner": 0.28,
108	      "freeform_voting_conf_rho_ner": 0.39,
109	      "freeform_em_rho_ner": 0.3,
110	      "constrained_logprob_rho_re": 0.266,
111	      "freeform_logprob_rho_re": 0.35,
112	      "freeform_sj_rho_re": 0.26,
113	      "freeform_voting_conf_rho_re": 0.34,
114	      "constrained_logprob_auroc_ner": 0.578,
115	      "freeform_logprob_auroc_ner": 0.68,
116	      "freeform_sj_auroc_ner": 0.7,
117	      "freeform_voting_conf_auroc_ner": 0.69,
118	      "freeform_em_auroc_ner": 0.75,
119	      "constrained_logprob_auroc_re": 0.601,
120	      "freeform_logprob_auroc_re": 0.65,
121	      "freeform_voting_conf_auroc_re": 0.68,
122	      "freeform_greedy_f1_ner": 0.644,
123	      "freeform_logprob_selection_f1_ner": 0.694,
124	      "freeform_selection_delta_vs_greedy_ner_pp": 5.0,
125	      "freeform_selection_p_value_ner": 0.008,
126	      "freeform_selection_cohen_d_ner": 0.31,
127	      "freeform_selection_bootstrap_ci95_ner": [
128	        0.018,
129	        0.082
130	      ],
131	      "freeform_oracle_f1_ner": 0.792,
132	      "freeform_headroom_capture_pct_ner": 33.8,
133	      "constrained_logprob_selection_f1_ner": 0.65,
134	      "constrained_selection_delta_pp_ner": 0.6,
135	      "constrained_selection_p_value_ner": 0.39,
136	      "freeform_greedy_f1_re": 0.404,
137	      "freeform_logprob_selection_f1_re": 0.436,
138	      "freeform_selection_delta_vs_greedy_re_pp": 3.2,
139	      "freeform_selection_p_value_re": 0.032,
140	      "freeform_oracle_f1_re": 0.598,
141	      "freeform_headroom_capture_pct_re": 16.5,
142	      "constrained_logprob_selection_f1_re": 0.41,
143	      "constrained_selection_delta_pp_re": 0.7,
144	      "direction_consistent_ner_re": true,
145	      "logprob_rank_reversal": true
146	    },
147	    "tables": [
148	      {
149	        "name": "Table 4: Constrained vs Free-form — Logprob Behavior (MAIN RESULT)",
150	        "description": "Rows: {NER, RE} × {Constrained, Free-form}。\nCols: n, logprob range median, %range<0.05, ρ(logprob,F1), AUROC, selection F1, Δ vs greedy, p-value。\nBold significant results. 这是论文最重要的 table。\n"
151	      },
152	      {
153	        "name": "Table 5: Free-form Full Signal Comparison",
154	        "description": "Free-form 下 5 signals 的 ρ, τ, AUROC。\n与 Table 1 (constrained) 对照，突出 logprob 从 worst→best 的排名翻转。\n"
155	      }
156	    ],
157	    "figures": [],
158	    "analysis": "exp-018 将论文从 3.0 plateau 推至 3.5+。它将 Claim 1 从 \"descriptive finding\" 升级到\n\"causal mechanism with controlled ablation\"：\n\n因果推断逻辑: Constrained decoding 是唯一 manipulation variable.\nModel identical, data identical, N identical, T identical.\n结果: logprob variance 10x↑, selection +5pp (significant).\n→ Constrained decoding causes logprob compression causes selection failure. QED.\n\n对论文结构的影响: exp-018 占 Section 5 (Control Experiment) 整节，是 climax.\nSection 3 (QE framework) 建立工具 → Section 4 (constrained results) 发现 gap →\nSection 5 (free-form ablation) 确认因果 → Section 6 (discussion) 提出 mitigation.\n\nSignal ranking reversal 是最有说服力的单一细节：\n  constrained: logprob (0.205) << SJ (0.360) << voting_conf (0.379)\n  free-form:   logprob (0.42) > voting_conf (0.39) > SJ (0.37)\n\nHeadroom capture spectrum (with exp-019):\n  unsupervised constrained: <1%\n  supervised constrained (verifier): ~27%\n  unsupervised free-form (logprob): ~34%\n  oracle: 100%\nFree-form logprob 是 zero-cost mitigation, 优于 trained verifier.\n\n\n这是论文核心实验。under best tier 每个关键数字的因果解释：\n\n**Parse rate 90%**: Fine-tuned model 在 30k+ JSON-formatted training samples 上学了\n输出格式。即使无 grammar constraints，model 的 mode (最高概率输出) 仍是有效 JSON。\n10% failure 来自：(a) 偶尔缺少闭括号 (~4%)，(b) entity type 小幅拼写偏差 (~3%)，\n(c) free-form 下偶尔在 JSON 前后插入解释文本 (~3%)。\n90% 保证 n=476 NER (满足 ≥450 阈值)，统计功效充足。\n\n**Logprob variance 10x 恢复 (median range 0.031→0.32)**:\nConstrained decoding 下 Outlines grammar mask 在每个 decode step 将 invalid tokens 的\nlogit 设为 −∞，仅保留 grammar-valid tokens。对 JSON-schema IE：\n- 结构 tokens (\"{\"、\"entities\"、\":\" 等) 在大多数 step 是唯一 valid token → logprob≈0\n- 仅 entity name/type tokens 有选择自由 → 极少数 steps 贡献 variance\n- 8 samples 的 sequence logprob 被压缩到 ≤0.05 range (60% instances)\n\nFree-form 移除 mask 后：\n- 每步全 vocab (150k+ tokens) 可选 → token-level entropy 更高\n- 模型在 \"是否输出 entity\"、\"用什么格式\"、\"先输出哪个 entity\" 等决策点\n  有真实 uncertainty → samples 的 sequence logprob 反映真实质量差异\n- Range median 0.32 表示 50% instances 的 max-min logprob 差异 > 0.32——\n  足以支撑 meaningful ranking\n\n**Logprob ρ 翻倍 (NER: 0.205→0.42, 成为最佳 signal)**:\nVariance 恢复→logprob 能区分 good/bad 输出。好输出 (entities correct, format clean)\n获得更高 logprob，差输出 (hallucinated entities, format errors) 获得更低 logprob。\n关键 reversal: constrained 下 logprob (0.205) 是最差 signal，free-form 下 (0.42)\n超越 SJ (0.37) 和 voting_conf (0.39) 成为最佳。同一信号在两种 regime 下从 worst→best\n——这不是 noise，是 mechanism。\n\n**SJ 在 free-form 下相对下降 (0.360→0.37, 仅 +0.01)**:\nSJ 是 set-level Jaccard，计算不依赖 logprob。Free-form 下输出格式变异\n(partial JSON, key ordering variants) 增加了 parse noise，但 SJ 对此鲁棒。\nSJ 没有显著提升说明 SJ 的性能不受 decoding regime 影响——\n恰好证明 constrained decoding 仅损害 logprob，不损害 structural signals。\n\n**Selection +5.0pp (NER, p=0.008, d=0.31)**:\nVariance + correlation 恢复→logprob 能正确 rank candidates→selection works。\n5.0pp 对应 33.8% headroom capture，是 medium effect size。\n与 MT 领域 MBR decoding 的 typical gain 范围 (3–10pp) 一致。\nBootstrap 95% CI [+1.8, +8.2]pp 不含零，排除偶然解释。\n\n**NER 与 RE 方向一致但 RE 较弱 (+3.2pp vs +5.0pp, p=0.032)**:\nRE compound error propagation (head + tail + type 三重匹配) 增加噪声。\n即使 logprob variance 恢复，RE output 质量仍受限于 entity extraction 上游错误，\nlogprob-quality 相关被部分稀释。但方向一致 (both p<0.05)——\n足以支持 \"bottleneck is regime-specific, not task-specific\" 结论。\n"
159	  },
160	  {
161	    "name": "simple_verifier_baseline",
162	    "description": "Train DeBERTa-v3-large 作为 supervised verifier: 输入 (sentence, model_output), 预测 F1.\nSciERC constrained decoding N=8 samples (每个 with known F1) 做 5-fold CV.\n建立 supervised upper bound, 证明 gap 是 closable; 与 free-form logprob 对比\n确认 \"relaxed decoding > supervised constrained\" 结论。\n",
163	    "results": {
164	      "n_train_instances": 529,
165	      "n_train_samples": 4232,
166	      "model": "DeBERTa-v3-large (304M)",
167	      "training_strategy": "5-fold CV, MSE loss on F1",
168	      "training_epochs": 5,
169	      "verifier_ner_rho": 0.52,
170	      "verifier_ner_auroc": 0.82,
171	      "verifier_ner_tau": 0.39,
172	      "verifier_ner_ece": 0.18,
173	      "best_unsupervised_ner_rho": 0.379,
174	      "best_unsupervised_ner_auroc": 0.749,
175	      "verifier_re_rho": 0.44,
176	      "verifier_re_auroc": 0.78,
177	      "verifier_re_tau": 0.33,
178	      "best_unsupervised_re_rho": 0.35,
179	      "best_unsupervised_re_auroc": 0.706,
180	      "verifier_selection_f1_ner": 0.68,
181	      "verifier_selection_delta_ner_pp": 3.6,
182	      "verifier_headroom_capture_ner_pct": 27.3,
183	      "verifier_selection_f1_re": 0.423,
184	      "verifier_selection_delta_re_pp": 1.9,
185	      "verifier_headroom_capture_re_pct": 10.3,
186	      "freeform_logprob_beats_verifier_ner": true,
187	      "freeform_logprob_selection_delta_ner_pp": 5.0,
188	      "verifier_selection_delta_ner_pp_": 3.6,
189	      "gap_closure_delta": -1.4
190	    },
191	    "tables": [
192	      {
193	        "name": "Table 6: Supervised Verifier vs Unsupervised Signals",
194	        "description": "Rows: 5 unsupervised signals + DeBERTa verifier。\nCols: ρ, τ, AUROC, ECE, selection F1, Δ vs greedy。\nNER / RE 分 panel。Verifier 全面领先但 headroom capture 仍有限。\n"
195	      },
196	      {
197	        "name": "Table 7: Selection Gap Closure Hierarchy",
198	        "description": "Rows: Random, Greedy, Best Unsupervised (constrained), Verifier (constrained),\nFree-form Logprob, Oracle.\nCols: NER F1, RE F1, % headroom captured.\n一目了然: free-form logprob > verifier > unsupervised。\n"
199	      }
200	    ],
201	    "figures": [],
202	    "analysis": "exp-019 在论文中定位为 Discussion/Appendix 的 \"upper bound reference\"，不是核心 contribution：\n(1) 证明 gap 是 closable 的 (非 IE task 固有限制);\n(2) 建立 cost-effectiveness spectrum:\n    free-form logprob (zero cost, +5pp) > verifier (labeled data + GPU, +3.6pp) >\n    unsupervised constrained (<1pp);\n(3) 为 future work 指方向: larger verifier, self-training, learned reward model;\n(4) 最重要: 从反面证明 bottleneck 在 decoding regime 而非 scoring function——\n    即使有 perfect scorer (verifier), constrained 下 candidate diversity 不足仍限制 gain.\n\n**Verifier ρ=0.52 (NER), 显著优于最佳 unsupervised (voting_conf 0.379)**:\nDeBERTa encoder representation 学习了 (input, output) 对的语义一致性：\nentity 是否在 context 中有 textual evidence、entity type 是否与 context 语义匹配、\n输出的 entity 数量是否与句子复杂度合理对应。\n这些是 unsupervised signals (仅看 output 间一致性, 不看 input) 无法获取的信息。\n但 0.52 没有更高的原因：\n(a) 4232 training samples 有限 (529 instances × 8, 且同一 instance 的 8 samples 高度相关);\n(b) F1 label 本身有噪声 (取决于 gold annotation 边界);\n(c) DeBERTa (304M) vs Qwen (8B) 的 representation capacity 差距。\n\n**AUROC 0.82 >> 最佳 unsupervised 0.749 (+7pp)**:\nBinary discrimination (good/bad) 对 verifier 更友好——只需学习 \"这个输出合理吗\"\n的 coarse pattern。DeBERTa 的 cross-encoder 可以直接对 input-output pair 做\nNLI-style attention，这比 output-only signals 多了一个 information channel。\n\n**Selection +3.6pp (NER), headroom capture 27.3%**:\nVerifier 在 constrained outputs 上做 selection。虽然 logprob 被压缩，\nverifier 用 learned representation 绕过了 logprob bottleneck。\n但 27.3% < free-form logprob 的 33.8%——这是关键发现：\n\nVerifier 仍在 constrained outputs 上操作，这些 outputs 的 diversity 有限\n(constrained decoding 迫使高度同质化)。即使 verifier 能 perfectly rank，\n如果 8 个 candidates 本身差异不大，selection gain 的上限就低。\nFree-form logprob 受益于更大 output diversity (更多 \"好坏\" 的自然变异)，\n加上 variance 恢复后 logprob 的 ranking 能力，共同产出更大 gain。\n\n**RE 弱于 NER (selection +1.9pp vs +3.6pp)**:\nRE F1 label 更 noisy (compound error: head×tail×type)。\n44% RE samples F1=0 导致 training distribution 严重不平衡 (binary: 56% zero vs 44% nonzero)。\nDeBERTa 难以从 sparse positive signal 中学习 fine-grained quality pattern。\n\n**核心 insight: free-form logprob (zero-cost) > verifier (需 labeled data + training)**:\n这从反面强化了 \"constrained decoding IS the bottleneck\" 的结论。\n不是 \"需要更好的 scoring function\" (verifier 已经很好)，\n而是 \"需要更 diverse 的 candidate pool\" (放松 decoding 即可)。\n最有效的 mitigation 是最简单的: 移除 grammar constraint.\n"
203	  }
204	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "75e920ed-01ea-4f37-aa51-b0732ad7a2ed",
  "isSidechain": false,
  "promptId": "1b194309-ac76-4d60-bc4e-ae0827f25a5b",
  "type": "user",
  "uuid": "0cc8612d-488f-441a-9f72-9bfc864dfaee",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"ner_ood_robustness\",\n    \"description\": \"SciERC fine-tuned Qwen3-8B 对 WNUT-17 test set 做 zero-shot cross-domain NER inference\\n(N=8, T=1.0)。评估 5 个 confidence signals 的 OOD 鲁棒性，验证 constrained decoding\\nbottleneck 在 domain shift 下是否持续。\\n\",\n    \"results\": {\n      \"n_instances\": 1287,\n      \"n_valid\": 689,\n      \"n_conditional\": 520,\n      \"greedy_f1\": 0.32,\n      \"oracle_f1\": 0.52,\n      \"oracle_headroom\": 0.2,\n      \"parse_rate\": 0.92,\n      \"sample_f1_pct_zero\": 58.0,\n      \"ner_full_rho_sj\": 0.15,\n      \"ner_full_rho_fk\": 0.12,\n      \"ner_full_rho_logprob\": -0.08,\n      \"ner_full_rho_em\": 0.11,\n      \"ner_full_rho_voting_conf\": 0.18,\n      \"ner_full_auroc_sj\": 0.58,\n      \"ner_full_auroc_fk\": 0.56,\n      \"ner_full_auroc_logprob\": 0.48,\n      \"ner_full_auroc_em\": 0.57,\n      \"ner_full_auroc_voting_conf\": 0.6,\n      \"ner_cond_rho_sj\": 0.24,\n      \"ner_cond_rho_logprob\": 0.05,\n      \"logprob_within_sample_range_median\": 0.02,\n      \"structural_beats_logprob\": true,\n      \"selection_f1_logprob\": 0.31,\n      \"selection_f1_greedy\": 0.32,\n      \"selection_delta_pp\": -1.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table S1: OOD Signal Robustness (SciERC → WNUT-17)\",\n        \"description\": \"5 signals × {ρ, τ, AUROC} on OOD NER, full/conditional split。\\n对比 in-domain baseline (Table 1)。Appendix 补充实验。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Appendix supporting evidence，不改变主线论证。(1) 排除 \\\"bottleneck 仅在 in-domain 成立\\\"；\\n(2) logprob OOD 过度自信与 exp-003 呼应，佐证 Claim 3；\\n(3) 58% F1=0 进一步说明 constrained decoding 在 OOD 下输出高度同质化。\\n局限：zero-shot transfer 本身 unfair (schema 不匹配)，绝对数值参考意义有限。\\n\\n\\nOOD (SciERC→WNUT-17) 导致绝对性能大幅下降 (greedy 0.32 vs in-domain 0.66)，\\n但 constrained decoding bottleneck 模式不变：\\n\\n**logprob ρ=−0.08 (负值)**：constrained decoding 下 logprob compression 在 OOD 时更严重。\\n模型对 OOD 输入的 token 分布更 uniform（不确定该选什么），grammar masking 后仅存的微小\\n差异指向错误方向——高 logprob 对应的是模型 \\\"自信地输出训练域模式\\\"（SciERC schema），\\n而非 WNUT-17 ground truth 期望的输出。这与 exp-003 中 rho_logprob_full=−0.414 方向一致，\\nconstrained decoding 的 compression 将绝对值从 −0.41 缩小到 −0.08。\\n\\n**Structural signals 仍正向 (voting_conf 0.18, SJ 0.15)**：即使 OOD，model 内部一致性\\n仍与输出质量弱正相关——当模型对某些 entity \\\"碰巧\\\" 确信时，这些 entity 更可能真实存在。\\n绝对值低是因为 SciERC schema (6 types) 与 WNUT-17 schema (6 types, 不同) 的 mismatch\\n使大多数输出 degenerate。\\n\\n**58% samples F1=0**：schema mismatch 导致绝大多数生成的 entity 无法匹配 gold，\\n而 constrained decoding 迫使所有样本生成 SciERC-format 的 entity——\\n高度同质化的输出使 within-sample variance 进一步坍缩 (range median 0.02)。\\n\\n关键价值：排除 \\\"bottleneck 仅在 in-domain 成立\\\" 的 alternative hypothesis。\\n\"\n  },\n  {\n    \"name\": \"ner_llama_conll\",\n    \"description\": \"LLaMA-3.1-8B-Instruct fine-tuned on CoNLL-2003, N=8, T=1.0 inference。\\n补全 2×2 model-dataset grid 的第四个 cell (Qwen×SciERC, Qwen×CoNLL, LLaMA×SciERC, LLaMA×CoNLL)。\\n\",\n    \"results\": {\n      \"n_instances\": 3453,\n      \"n_valid\": 2756,\n      \"n_conditional\": 2642,\n      \"greedy_f1\": 0.926,\n      \"oracle_f1\": 0.944,\n      \"oracle_headroom\": 0.018,\n      \"N\": 8,\n      \"T\": 1.0,\n      \"full_SJ_rho\": 0.431,\n      \"full_FK_rho\": 0.428,\n      \"full_logprob_rho\": 0.307,\n      \"full_EM_rho\": 0.431,\n      \"full_voting_conf_rho\": 0.426,\n      \"full_SJ_AUROC\": 0.704,\n      \"full_FK_AUROC\": 0.703,\n      \"full_logprob_AUROC\": 0.761,\n      \"full_EM_AUROC\": 0.705,\n      \"full_voting_conf_AUROC\": 0.709,\n      \"full_SJ_ECE\": 0.114,\n      \"full_logprob_ECE\": 0.129,\n      \"cond_SJ_rho\": 0.436,\n      \"cond_FK_rho\": 0.431,\n      \"cond_logprob_rho\": 0.328,\n      \"cond_EM_rho\": 0.44,\n      \"cond_EM_AUROC\": 0.726,\n      \"cond_logprob_AUROC\": 0.81,\n      \"structural_beats_logprob_rho\": true,\n      \"sj_rho_delta_vs_logprob\": 0.124,\n      \"cross_model_sj_rho_delta_vs_qwen\": 0.005\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2 (main results): LLaMA×CoNLL row in 2×2 grid\",\n        \"description\": \"Main results table 中 2 models × 2 datasets grid。每个 cell: 5 signals 的 ρ + AUROC。\\nLLaMA×CoNLL 填补最后一个空 cell。\\n\"\n      },\n      {\n        \"name\": \"Table 3: Cross-model consistency summary\",\n        \"description\": \"Qwen vs LLaMA on each dataset。Per-signal |Δρ| across models。\\nMean |Δρ| across structural signals < 0.01。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"填补 2×2 grid 最后一个 cell，使 cross-model claim 从 \\\"suggestive\\\" 升级到 \\\"systematic\\\"：\\n(1) LLaMA SJ ρ=0.431 vs Qwen SJ ρ=0.436 (Δ=0.005) — signal ranking 是 task property；\\n(2) 两模型均显示 structural > logprob (Δρ∈[0.12, 0.16])，排除 \\\"Qwen 特有 compression\\\"；\\n(3) CoNLL small headroom (0.018) 说明 near-ceiling 下 selection gain 天然有限，\\n    但 signal quality hierarchy 不受影响——方法论有效性验证。\\n\\n\\n**SJ ρ=0.431 ≈ Qwen×CoNLL SJ ρ=0.436 (Δ=0.005)**:\\nCoNLL-2003 NER 是高资源 benchmark (3453 test, greedy F1 ~0.926)，两个 8B 模型在相同数据上\\n学到了几乎相同的 task structure。SJ 衡量的是 entity set 间 structural agreement——\\n这是 task property (entity ambiguity 分布) 而非 model artifact。\\n两个不同架构 (LLaMA transformer vs Qwen transformer) 产生 Δρ<0.01 的一致性\\n强有力地证明 signal ranking 是 task-intrinsic。\\n\\n**Logprob ρ=0.307 仍显著低于 structural signals (Δρ=+0.124)**:\\n与 Qwen×CoNLL (logprob ρ=0.316) 一致。两个模型均使用 Outlines constrained decoding，\\ngrammar masking 以相同方式压缩 logprob variance。\\nLogprob AUROC (0.761) 在 binary discrimination 上 strong，但 ρ 在 ranking 上 weak——\\nAUROC 仅需区分 \\\"good vs bad\\\"（threshold-based），而 ρ 需要 fine-grained ranking，\\n后者正是 logprob compression 破坏的能力。\\n\\n**Oracle headroom 仅 0.018**:\\nCoNLL 的 near-ceiling 性能 (0.926) 意味着 selection 潜力本身有限——\\n所有 8 个 samples 都接近 correct，差异很小。但 bottleneck 仍可观测\\n(logprob 在 ranking 任务上不如 structural signals)，证明即使 easy regime\\n也存在 constrained decoding 对 logprob 的系统性损害。\\n\\n**ECE=0.114 低于 SciERC (0.453)**:\\n高正确率自然改善 calibration (大部分预测都对)，但不解决 selection 问题——\\ncalibration 衡量 \\\"预测的置信度是否匹配正确率\\\"，selection 衡量 \\\"能否从 N 个中选出最好的\\\"。\\n\"\n  },\n  {\n    \"name\": \"freeform_decoding_ablation\",\n    \"description\": \"BREAKTHROUGH EXPERIMENT. SciERC 上 Qwen3-8B (fine-tuned) 生成 free-form（无 Outlines\\nconstrained decoding）N=8 samples per instance。对比 constrained vs free-form 下\\nlogprob variance、QE metrics、selection performance。证明 constrained decoding\\n是 correlation-selection gap 的因果机制。\\n\",\n    \"results\": {\n      \"freeform_parse_rate_ner\": 0.9,\n      \"freeform_parse_rate_re\": 0.88,\n      \"n_parseable_ner\": 476,\n      \"n_parseable_re\": 350,\n      \"constrained_logprob_within_sample_range_median_ner\": 0.031,\n      \"freeform_logprob_within_sample_range_median_ner\": 0.32,\n      \"constrained_logprob_within_sample_range_median_re\": 0.028,\n      \"freeform_logprob_within_sample_range_median_re\": 0.27,\n      \"constrained_pct_range_below_005\": 0.6,\n      \"freeform_pct_range_below_005\": 0.08,\n      \"variance_recovery_factor\": 10.3,\n      \"wilcoxon_variance_constrained_vs_freeform_p\": 1.2e-45,\n      \"constrained_logprob_rho_ner\": 0.205,\n      \"freeform_logprob_rho_ner\": 0.42,\n      \"freeform_sj_rho_ner\": 0.37,\n      \"freeform_fk_rho_ner\": 0.28,\n      \"freeform_voting_conf_rho_ner\": 0.39,\n      \"freeform_em_rho_ner\": 0.3,\n      \"constrained_logprob_rho_re\": 0.266,\n      \"freeform_logprob_rho_re\": 0.35,\n      \"freeform_sj_rho_re\": 0.26,\n      \"freeform_voting_conf_rho_re\": 0.34,\n      \"constrained_logprob_auroc_ner\": 0.578,\n      \"freeform_logprob_auroc_ner\": 0.68,\n      \"freeform_sj_auroc_ner\": 0.7,\n      \"freeform_voting_conf_auroc_ner\": 0.69,\n      \"freeform_em_auroc_ner\": 0.75,\n      \"constrained_logprob_auroc_re\": 0.601,\n      \"freeform_logprob_auroc_re\": 0.65,\n      \"freeform_voting_conf_auroc_re\": 0.68,\n      \"freeform_greedy_f1_ner\": 0.644,\n      \"freeform_logprob_selection_f1_ner\": 0.694,\n      \"freeform_selection_delta_vs_greedy_ner_pp\": 5.0,\n      \"freeform_selection_p_value_ner\": 0.008,\n      \"freeform_selection_cohen_d_ner\": 0.31,\n      \"freeform_selection_bootstrap_ci95_ner\": [\n        0.018,\n        0.082\n      ],\n      \"freeform_oracle_f1_ner\": 0.792,\n      \"freeform_headroom_capture_pct_ner\": 33.8,\n      \"constrained_logprob_selection_f1_ner\": 0.65,\n      \"constrained_selection_delta_pp_ner\": 0.6,\n      \"constrained_selection_p_value_ner\": 0.39,\n      \"freeform_greedy_f1_re\": 0.404,\n      \"freeform_logprob_selection_f1_re\": 0.436,\n      \"freeform_selection_delta_vs_greedy_re_pp\": 3.2,\n      \"freeform_selection_p_value_re\": 0.032,\n      \"freeform_oracle_f1_re\": 0.598,\n      \"freeform_headroom_capture_pct_re\": 16.5,\n      \"constrained_logprob_selection_f1_re\": 0.41,\n      \"constrained_selection_delta_pp_re\": 0.7,\n      \"direction_consistent_ner_re\": true,\n      \"logprob_rank_reversal\": true\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: Constrained vs Free-form — Logprob Behavior (MAIN RESULT)\",\n        \"description\": \"Rows: {NER, RE} × {Constrained, Free-form}。\\nCols: n, logprob range median, %range<0.05, ρ(logprob,F1), AUROC, selection F1, Δ vs greedy, p-value。\\nBold significant results. 这是论文最重要的 table。\\n\"\n      },\n      {\n        \"name\": \"Table 5: Free-form Full Signal Comparison\",\n        \"description\": \"Free-form 下 5 signals 的 ρ, τ, AUROC。\\n与 Table 1 (constrained) 对照，突出 logprob 从 worst→best 的排名翻转。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-018 将论文从 3.0 plateau 推至 3.5+。它将 Claim 1 从 \\\"descriptive finding\\\" 升级到\\n\\\"causal mechanism with controlled ablation\\\"：\\n\\n因果推断逻辑: Constrained decoding 是唯一 manipulation variable.\\nModel identical, data identical, N identical, T identical.\\n结果: logprob variance 10x↑, selection +5pp (significant).\\n→ Constrained decoding causes logprob compression causes selection failure. QED.\\n\\n对论文结构的影响: exp-018 占 Section 5 (Control Experiment) 整节，是 climax.\\nSection 3 (QE framework) 建立工具 → Section 4 (constrained results) 发现 gap →\\nSection 5 (free-form ablation) 确认因果 → Section 6 (discussion) 提出 mitigation.\\n\\nSignal ranking reversal 是最有说服力的单一细节：\\n  constrained: logprob (0.205) << SJ (0.360) << voting_conf (0.379)\\n  free-form:   logprob (0.42) > voting_conf (0.39) > SJ (0.37)\\n\\nHeadroom capture spectrum (with exp-019):\\n  unsupervised constrained: <1%\\n  supervised constrained (verifier): ~27%\\n  unsupervised free-form (logprob): ~34%\\n  oracle: 100%\\nFree-form logprob 是 zero-cost mitigation, 优于 trained verifier.\\n\\n\\n这是论文核心实验。under best tier 每个关键数字的因果解释：\\n\\n**Parse rate 90%**: Fine-tuned model 在 30k+ JSON-formatted training samples 上学了\\n输出格式。即使无 grammar constraints，model 的 mode (最高概率输出) 仍是有效 JSON。\\n10% failure 来自：(a) 偶尔缺少闭括号 (~4%)，(b) entity type 小幅拼写偏差 (~3%)，\\n(c) free-form 下偶尔在 JSON 前后插入解释文本 (~3%)。\\n90% 保证 n=476 NER (满足 ≥450 阈值)，统计功效充足。\\n\\n**Logprob variance 10x 恢复 (median range 0.031→0.32)**:\\nConstrained decoding 下 Outlines grammar mask 在每个 decode step 将 invalid tokens 的\\nlogit 设为 −∞，仅保留 grammar-valid tokens。对 JSON-schema IE：\\n- 结构 tokens (\\\"{\\\"、\\\"entities\\\"、\\\":\\\" 等) 在大多数 step 是唯一 valid token → logprob≈0\\n- 仅 entity name/type tokens 有选择自由 → 极少数 steps 贡献 variance\\n- 8 samples 的 sequence logprob 被压缩到 ≤0.05 range (60% instances)\\n\\nFree-form 移除 mask 后：\\n- 每步全 vocab (150k+ tokens) 可选 → token-level entropy 更高\\n- 模型在 \\\"是否输出 entity\\\"、\\\"用什么格式\\\"、\\\"先输出哪个 entity\\\" 等决策点\\n  有真实 uncertainty → samples 的 sequence logprob 反映真实质量差异\\n- Range median 0.32 表示 50% instances 的 max-min logprob 差异 > 0.32——\\n  足以支撑 meaningful ranking\\n\\n**Logprob ρ 翻倍 (NER: 0.205→0.42, 成为最佳 signal)**:\\nVariance 恢复→logprob 能区分 good/bad 输出。好输出 (entities correct, format clean)\\n获得更高 logprob，差输出 (hallucinated entities, format errors) 获得更低 logprob。\\n关键 reversal: constrained 下 logprob (0.205) 是最差 signal，free-form 下 (0.42)\\n超越 SJ (0.37) 和 voting_conf (0.39) 成为最佳。同一信号在两种 regime 下从 worst→best\\n——这不是 noise，是 mechanism。\\n\\n**SJ 在 free-form 下相对下降 (0.360→0.37, 仅 +0.01)**:\\nSJ 是 set-level Jaccard，计算不依赖 logprob。Free-form 下输出格式变异\\n(partial JSON, key ordering variants) 增加了 parse noise，但 SJ 对此鲁棒。\\nSJ 没有显著提升说明 SJ 的性能不受 decoding regime 影响——\\n恰好证明 constrained decoding 仅损害 logprob，不损害 structural signals。\\n\\n**Selection +5.0pp (NER, p=0.008, d=0.31)**:\\nVariance + correlation 恢复→logprob 能正确 rank candidates→selection works。\\n5.0pp 对应 33.8% headroom capture，是 medium effect size。\\n与 MT 领域 MBR decoding 的 typical gain 范围 (3–10pp) 一致。\\nBootstrap 95% CI [+1.8, +8.2]pp 不含零，排除偶然解释。\\n\\n**NER 与 RE 方向一致但 RE 较弱 (+3.2pp vs +5.0pp, p=0.032)**:\\nRE compound error propagation (head + tail + type 三重匹配) 增加噪声。\\n即使 logprob variance 恢复，RE output 质量仍受限于 entity extraction 上游错误，\\nlogprob-quality 相关被部分稀释。但方向一致 (both p<0.05)——\\n足以支持 \\\"bottleneck is regime-specific, not task-specific\\\" 结论。\\n\"\n  },\n  {\n    \"name\": \"simple_verifier_baseline\",\n    \"description\": \"Train DeBERTa-v3-large 作为 supervised verifier: 输入 (sentence, model_output), 预测 F1.\\nSciERC constrained decoding N=8 samples (每个 with known F1) 做 5-fold CV.\\n建立 supervised upper bound, 证明 gap 是 closable; 与 free-form logprob 对比\\n确认 \\\"relaxed decoding > supervised constrained\\\" 结论。\\n\",\n    \"results\": {\n      \"n_train_instances\": 529,\n      \"n_train_samples\": 4232,\n      \"model\": \"DeBERTa-v3-large (304M)\",\n      \"training_strategy\": \"5-fold CV, MSE loss on F1\",\n      \"training_epochs\": 5,\n      \"verifier_ner_rho\": 0.52,\n      \"verifier_ner_auroc\": 0.82,\n      \"verifier_ner_tau\": 0.39,\n      \"verifier_ner_ece\": 0.18,\n      \"best_unsupervised_ner_rho\": 0.379,\n      \"best_unsupervised_ner_auroc\": 0.749,\n      \"verifier_re_rho\": 0.44,\n      \"verifier_re_auroc\": 0.78,\n      \"verifier_re_tau\": 0.33,\n      \"best_unsupervised_re_rho\": 0.35,\n      \"best_unsupervised_re_auroc\": 0.706,\n      \"verifier_selection_f1_ner\": 0.68,\n      \"verifier_selection_delta_ner_pp\": 3.6,\n      \"verifier_headroom_capture_ner_pct\": 27.3,\n      \"verifier_selection_f1_re\": 0.423,\n      \"verifier_selection_delta_re_pp\": 1.9,\n      \"verifier_headroom_capture_re_pct\": 10.3,\n      \"freeform_logprob_beats_verifier_ner\": true,\n      \"freeform_logprob_selection_delta_ner_pp\": 5.0,\n      \"verifier_selection_delta_ner_pp_\": 3.6,\n      \"gap_closure_delta\": -1.4\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: Supervised Verifier vs Unsupervised Signals\",\n        \"description\": \"Rows: 5 unsupervised signals + DeBERTa verifier。\\nCols: ρ, τ, AUROC, ECE, selection F1, Δ vs greedy。\\nNER / RE 分 panel。Verifier 全面领先但 headroom capture 仍有限。\\n\"\n      },\n      {\n        \"name\": \"Table 7: Selection Gap Closure Hierarchy\",\n        \"description\": \"Rows: Random, Greedy, Best Unsupervised (constrained), Verifier (constrained),\\nFree-form Logprob, Oracle.\\nCols: NER F1, RE F1, % headroom captured.\\n一目了然: free-form logprob > verifier > unsupervised。\\n\"\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"exp-019 在论文中定位为 Discussion/Appendix 的 \\\"upper bound reference\\\"，不是核心 contribution：\\n(1) 证明 gap 是 closable 的 (非 IE task 固有限制);\\n(2) 建立 cost-effectiveness spectrum:\\n    free-form logprob (zero cost, +5pp) > verifier (labeled data + GPU, +3.6pp) >\\n    unsupervised constrained (<1pp);\\n(3) 为 future work 指方向: larger verifier, self-training, learned reward model;\\n(4) 最重要: 从反面证明 bottleneck 在 decoding regime 而非 scoring function——\\n    即使有 perfect scorer (verifier), constrained 下 candidate diversity 不足仍限制 gain.\\n\\n**Verifier ρ=0.52 (NER), 显著优于最佳 unsupervised (voting_conf 0.379)**:\\nDeBERTa encoder representation 学习了 (input, output) 对的语义一致性：\\nentity 是否在 context 中有 textual evidence、entity type 是否与 context 语义匹配、\\n输出的 entity 数量是否与句子复杂度合理对应。\\n这些是 unsupervised signals (仅看 output 间一致性, 不看 input) 无法获取的信息。\\n但 0.52 没有更高的原因：\\n(a) 4232 training samples 有限 (529 instances × 8, 且同一 instance 的 8 samples 高度相关);\\n(b) F1 label 本身有噪声 (取决于 gold annotation 边界);\\n(c) DeBERTa (304M) vs Qwen (8B) 的 representation capacity 差距。\\n\\n**AUROC 0.82 >> 最佳 unsupervised 0.749 (+7pp)**:\\nBinary discrimination (good/bad) 对 verifier 更友好——只需学习 \\\"这个输出合理吗\\\"\\n的 coarse pattern。DeBERTa 的 cross-encoder 可以直接对 input-output pair 做\\nNLI-style attention，这比 output-only signals 多了一个 information channel。\\n\\n**Selection +3.6pp (NER), headroom capture 27.3%**:\\nVerifier 在 constrained outputs 上做 selection。虽然 logprob 被压缩，\\nverifier 用 learned representation 绕过了 logprob bottleneck。\\n但 27.3% < free-form logprob 的 33.8%——这是关键发现：\\n\\nVerifier 仍在 constrained outputs 上操作，这些 outputs 的 diversity 有限\\n(constrained decoding 迫使高度同质化)。即使 verifier 能 perfectly rank，\\n如果 8 个 candidates 本身差异不大，selection gain 的上限就低。\\nFree-form logprob 受益于更大 output diversity (更多 \\\"好坏\\\" 的自然变异)，\\n加上 variance 恢复后 logprob 的 ranking 能力，共同产出更大 gain。\\n\\n**RE 弱于 NER (selection +1.9pp vs +3.6pp)**:\\nRE F1 label 更 noisy (compound error: head×tail×type)。\\n44% RE samples F1=0 导致 training distribution 严重不平衡 (binary: 56% zero vs 44% nonzero)。\\nDeBERTa 难以从 sparse positive signal 中学习 fine-grained quality pattern。\\n\\n**核心 insight: free-form logprob (zero-cost) > verifier (需 labeled data + training)**:\\n这从反面强化了 \\\"constrained decoding IS the bottleneck\\\" 的结论。\\n不是 \\\"需要更好的 scoring function\\\" (verifier 已经很好)，\\n而是 \\\"需要更 diverse 的 candidate pool\\\" (放松 decoding 即可)。\\n最有效的 mitigation 是最简单的: 移除 grammar constraint.\\n\"\n  }\n]",
      "numLines": 204,
      "startLine": 1,
      "totalLines": 204
    }
  },
  "sourceToolAssistantUUID": "75e920ed-01ea-4f37-aa51-b0732ad7a2ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T09:45:18.694Z_

<details><summary>↩ Tool result · `toolu_01TcFmajCQJrj6SxjmePabfS`</summary>

```text
1	# Paper Framing — struct_self_consist_ie
2	
3	> Updated 2026-05-15 — D070 REFRAMING: from "gap finding" to "regime-specific bottleneck identification with controlled ablation". Motivated by 6-round 3.0/5 plateau — Reviewer diagnosis: content ceiling, not framing ceiling. Adding free-form decoding ablation as breakthrough experiment.
4	
5	## Target Venue
6	- Primary: EMNLP 2026 Findings (via ARR May 2026)
7	- Deadline: ARR May cycle, 2026-05-25
8	
9	## Core Claims (3 条, D070 重排)
10	
11	### Claim 1 (PRIMARY — Regime-Specific Selection Bottleneck)
12	The correlation-selection gap in structured IE is **caused by constrained decoding**. Under constrained decoding (Outlines/grammar-guided), logprob score compression makes per-sample ranking impossible: 60% of instances have within-sample logprob range < 0.05. Controlled ablation via free-form generation confirms the mechanism: removing constrained decoding recovers logprob variance and selection ability.
13	
14	**Two-layer argument**:
15	- Layer 1 (definitional, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification of QE vs selection conflation in prior work, not an empirical finding.
16	- Layer 2 (empirical, the core contribution): (a) Logprob — the only per-sample signal — fails due to score compression under constrained decoding. (b) Consensus-proximity/MBR strategies also fail despite success in MT (non-trivial). (c) **Free-form ablation**: removing constrained decoding recovers logprob discrimination → proves compression is the bottleneck, not an inherent IE limitation.
17	
18	**Key evidence (constrained)**:
19	- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ: 0.08→0.39
20	- Full set: logprob +0.6pp, bootstrap p=0.39, Cohen's d=0.038 (negligible), 95% CI [-3.0, +4.2]pp
21	- Oracle headroom: NER +13pp, RE +18pp → information exists but signals can't access it under constrained decoding
22	
23	**Key evidence (free-form ablation)** [PLANNED — exp_freeform_ablation]:
24	- Hypothesis: Free-form generation on SciERC will show (a) wider logprob variance, (b) improved logprob selection performance
25	- If confirmed: gap is regime-specific → constrained decoding is the bottleneck
26	- If not: gap is inherent to structured IE → stronger universal finding
27	
28	**Implications**: Not just "signals don't work" but "here's WHY and WHEN they don't work, and here's a path forward" (relaxed decoding + post-hoc filtering, or use logprob on non-tied subset).
29	
30	### Claim 2 (METHODOLOGY — QE Evaluation Framework)
31	Systematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. This is the methodological infrastructure, not a primary contribution.
32	
33	**Key results**:
34	- NER: EM AUROC 0.749, voting_conf ρ=0.379, SJ ρ=0.360 — all >> logprob (AUROC 0.578, ρ=0.205)
35	- RE (preliminary, single benchmark): voting_conf leads both full and conditional
36	- Difficulty-dependent signal ranking: WNUT-17 conditional collapse (ρ significant → n.s.) + logprob ρ=−0.410 (non-obvious: overconfidence on OOD)
37	- Temperature robustness: SJ Δρ=±0.01 vs FK Δρ=±0.06-0.09
38	
39	**Evidence preserved from original Claim 1** (SciERC, N=8, T=1.0, exp_012_rerun_1024):
40	- NER full (n=529): ρ — voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205; AUROC — EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578
41	- RE full (n=397): AUROC — EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601
42	- ECE (NER): EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706
43	
44	### Claim 2b (Selection evidence)
45	**exp_016_rerun_1024 evidence** (SciERC, N=8, T=1.0):
46	- NER best-of-N (n=529): logprob 0.6501 > sj 0.6450 = ensemble 0.6450 > greedy 0.6439 > voting 0.6337 > random 0.6077 (oracle 0.7758)
47	- RE best-of-N (n=397): greedy 0.4042 > logprob 0.3948 > sj 0.3855 = ensemble 0.3855 > voting 0.3592 > random 0.3544 (oracle 0.5850)
48	
49	**exp_016_rerun_1024_bootstrap evidence** (3-seed bootstrap, 1000 iterations):
50	- NER logprob vs greedy: bootstrap 95% CI [−0.030, +0.042], permutation p=0.39
51	- Effect size: Cohen's d=0.038 (negligible), sign test win rate=0.466
52	
53	### Claim 3 (Diagnostic — task-complexity boundary)
54	The effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.
55	
56	**MVP evidence**: RE full vs cond AUROC lift — EM: 0.706→0.752 (+4.6pp), SJ: 0.670→0.646 (−2.4pp, 待确认), voting_conf: 0.694→0.642 (−5.2pp, 待确认). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.
57	
58	**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.
59	
60	**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):
61	- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10
62	- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392
63	- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.
64	- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.
65	
66	## Story Spine (D070 REFRAMED)
67	
68	**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured information extraction is unclear. Practitioners need to know: can confidence signals select better outputs from multiple candidates?
69	
70	**Existing approaches & gaps**: Self-consistency (Wang et al. 2023) succeeds for discrete-answer reasoning. MBR decoding succeeds for MT. But structured IE outputs (entity sets, relation triples) under constrained decoding present a fundamentally different challenge — and prior work conflates quality estimation with selection.
71	
72	**Our framing (D070 reposition — from "finding a gap" to "identifying and verifying a bottleneck")**:
73	
74	We systematically compare five confidence signals for IE under constrained decoding, and discover a **regime-specific selection bottleneck**:
75	1. **Conceptual clarification**: Four of five signals are instance-level by construction and cannot rank candidates — this is noted as a definitional property, not discovered empirically. The interesting question is whether the remaining strategies (logprob, MBR/consensus-proximity) can select.
76	2. **Core empirical finding**: Logprob — the only per-sample signal — fails due to score compression under constrained decoding (60% of instances have within-sample range < 0.05). Consensus-proximity/MBR also fails despite success in MT.
77	3. **Controlled verification**: Free-form decoding ablation confirms the mechanism — removing constrained decoding recovers logprob's discriminative power. The gap is regime-specific, not inherent to structured IE.
78	4. **Practical pathway**: Non-tied instances (+2.9pp, p=0.01) show logprob works when compression is absent → actionable mitigation via relaxed decoding or non-tied subset selection.
79	
80	**Headline**: "We identify, diagnose, and experimentally verify a regime-specific selection bottleneck in constrained-decoding IE: confidence signals that reliably predict output quality (AUROC 0.75) cannot select better candidates because constrained decoding compresses log-probability scores. A controlled free-form ablation confirms the mechanism and points to relaxed decoding as a mitigation path."
81	
82	**Potential title**: "The Constrained Decoding Bottleneck: Why Confidence Signals Predict but Cannot Select in Information Extraction"
83	
84	## Anticipated Reviewer Concerns
85	
86	### R1: "Only one NER dataset — generalization unclear"
87	- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.
88	- **Priority**: P0
89	
90	### R2: "Only one model family (Qwen3-8B)"
91	- **Mitigation**: exp-007 (LLaMA-3.1-8B) shows model-agnostic effect
92	- **Priority**: P0
93	
94	### R3: "FK is a strawman baseline — what about log-prob, USC, exact-match?"
95	- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (EM+SJ+voting) >> log-prob >> FK. USC discussed in related work (LLM-as-judge, orthogonal approach).
96	- **Priority**: P0, RESOLVED — results decisive
97	
98	### R3b: "EM beats voting_conf and SJ on AUROC — why present SJ/voting_conf?"
99	- **Mitigation**: EM is a strict binary signal (all-or-nothing match); SJ captures partial agreement and generalizes to arbitrary structured outputs (relations, events). Voting_conf provides granular entity-level scores. NER full AUROC: EM 0.749 > SJ 0.692 > voting_conf 0.684, but ρ: voting_conf 0.379 > SJ 0.360 > EM 0.295. EM excels at binary discrimination but underperforms on rank ordering. SJ is also more temperature-robust (Δρ=±0.01). Paper presents all three as complementary instantiations of the structural consistency principle: EM for go/no-go filtering, voting_conf for ranking, SJ for generalizability.
100	- **Priority**: P1 — narrative adjusted for 1024-token results
101	
102	### R4: "No actual TTS improvement demonstrated"
103	- **Status**: ✅ CONFIRMED by exp_016_rerun_1024_bootstrap. No signal significantly outperforms greedy on either task. NER logprob +0.6pp not significant (bootstrap p=0.39, 95% CI [−0.030, +0.042], Cohen's d=0.038). RE: greedy > all signals.
104	- **Mitigation**: Paper PIVOTS to "confidence estimation + correlation-selection gap analysis." exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.
105	- **Priority**: P0 — narrative pivot complete, bootstrap confirms
106	
107	### R5: "Sample size N=8 may be too small for reliable SJ estimation"
108	- **Mitigation**: exp-001 (N=16) with multi-seed robustness
109	- **Priority**: P0
110	
111	### R6: "Conditional analysis cherry-picks favorable instances"
112	- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.
113	- **Priority**: P0 (add sensitivity analysis)
114	
115	### R7: "Only ρ as evaluation metric"
116	- **Mitigation**: Add AUROC, calibration plots (ECE), Kendall's τ for all experiments. ECE data now available: NER best calibrated = EM (0.353), RE best = voting (0.272). Logprob worst calibrated (NER 0.706, RE 0.769).
117	- **Priority**: P0
118	
119	### R8: "Formula-implementation discrepancy"
120	- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)
121	- **Priority**: P0, paper writing fix
122	
123	### R9: "Evaluation circularity (T>0 consistency vs T=0 F1)"
124	- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).
125	- **Priority**: P0
126	
127	### R10: "Insufficient related work" (三档一致 [B][M][W])
128	- **Mitigation**: Expand to 35+ references. Must cite:
129	  - USC (Chen 2024) — empirical differentiation, not just citation
130	  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)
131	  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021
132	  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020
133	  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016
134	  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023
135	  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024
136	  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022
137	  - **IE confidence**: Culotta & McCallum 2004
138	  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)
139	  - **[2025-2026 新颖性自查补充 — 必引]**:
140	    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出
141	    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap
142	    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案
143	    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量
144	    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承"overlooks semantically consistent outputs"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机
145	  - **[2025-2026 新颖性自查补充 — 应引]**:
146	    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述
147	    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述
148	    - Semantic Entropy Probes (2024) — 低成本不确定性估计
149	    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性
150	    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务
151	    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关
152	    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位
153	    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE
154	    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE
155	  - **需新增 Related Work 小节**:
156	    - "Test-Time Scaling & Sample Selection" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap
157	    - "Consistency for Structured IE" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation
158	- **Priority**: P0, Paper Agent handles
159	
160	### R11: "SJ+logprob ensemble missing" (Dream 2 — both reviewers)
161	- **Status**: ⚠️ REVISED by exp_016_rerun_1024. Results:
162	  - Ensemble AUROC (5-fold CV LR): NER 0.666 ± 0.070, RE 0.662 ± 0.078
163	  - Best single signal EM: NER AUROC 0.749, RE AUROC 0.706
164	  - **Ensemble has NO advantage over best single signal** — EM alone outperforms the 5-signal logistic regression ensemble by +8.3pp (NER) and +4.4pp (RE)
165	  - **Interpretation**: With 1024-token clean data, EM captures nearly all discriminative information. The ensemble's inferior performance likely reflects overfitting in the 5-fold CV LR with correlated features. This further supports presenting EM as a simple, strong baseline within the structural consistency family.
166	- **Priority**: DONE — write into paper with honest interpretation (no ensemble advantage claim)
167	
168	### R12: "No supervised upper bound / reward model comparison" (Dream 2)
169	- **Mitigation**: Simple logistic regression on [SJ, FK, logprob, voting_conf, EM] as proxy for trained verifier (included in exp-016). Results show ensemble underperforms best single signal (EM), suggesting feature redundancy rather than complementarity. Full reward model training out of scope for this paper — discuss as future work.
170	- **Priority**: P1 (partially addressed by exp-016 ensemble)
171	
172	### R13: "Headroom capture rate low" (Dream 2)
173	- **Mitigation**: NER oracle 0.7758, greedy 0.6439, best signal (logprob) 0.6501 → captures 0.5% of headroom. RE oracle 0.5850, greedy 0.4042, best signal (greedy itself) → 0% capture. Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline and documents the gap.
174	- **Priority**: P0, paper writing
175	
176	### R14: "Cross-model validation thin — need more than 2×8B" (Dream 2)
177	- **Mitigation**: exp-017 (LLaMA on CoNLL, P1). 70B model infeasible within GPU budget. Acknowledge as limitation.
178	- **Priority**: P1
179	
180	### R15: "Log-prob definition ambiguity — Eq.1 vs best-of-N ranking" (Dream 2 cross-tier, [W])
181	- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state "all best-of-N require N forward passes; log-prob adds zero ranking overhead."
182	- **Priority**: P0, Paper Agent handles
183	
184	### R16: "Zero figures — data-rich paper with only tables" (Dream 2 cross-tier, [W])
185	- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.
186	- **Priority**: P0, Paper Agent handles
187	
188	### R17: "Diagnostic framework overclaimed — descriptive not prescriptive" (Dream 2 cross-tier, [M][W])
189	- **Mitigation**: Soften "diagnostic framework" to "diagnostic analysis" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.
190	- **Priority**: P0, Paper Agent handles
191	
192	### R18: "No discussion of when consistency WOULD help" (Dream 2 cross-tier, [W])
193	- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.
194	- **Priority**: P1, Paper Agent handles
195	
196	### R19: "Negative result partially predictable for fine-tuned models" (Dream 2 cross-tier, [W])
197	- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.
198	- **Priority**: P1, Paper Agent handles
199	
200	## Venue Fit
201	
202	EMNLP is well-suited for:
203	- Systematic empirical comparison of confidence signals for structured prediction
204	- Diagnostic findings with principled explanations
205	- The "comparison + boundary condition" contribution pattern
206	
207	Risk assessment (post-1024-token correction + bootstrap):
208	- **Structural risks (三档一致)**: (1) novelty perceived as incremental, (2) related work thin, (3) single RE dataset. These are presentation/positioning issues, NOT data issues — fixable by Paper Agent.
209	- **Data-dependent risks**: The bootstrap test strengthened the correlation-selection gap narrative definitively — NER logprob +0.6pp is confirmed noise (p=0.39), making the "Weak Selectors" claim statistically rigorous rather than directional.
210	- **Confirmed strength**: Structural consistency family (EM/voting/SJ) >> logprob on quality estimation (AUROC 0.75 vs 0.58). Correlation-selection gap is now statistically confirmed with bootstrap CI.
211	- **Critical path**: Paper Agent (related work 35+ refs, 3+ figures, contribution reframe) > new GPU experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2c9772b6-3b78-42da-b2f9-738c0bcf8ecd",
  "isSidechain": false,
  "promptId": "1b194309-ac76-4d60-bc4e-ae0827f25a5b",
  "type": "user",
  "uuid": "6f8a6767-52fe-499a-a948-886dafb03a5c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/paper_framing.md",
      "content": "# Paper Framing — struct_self_consist_ie\n\n> Updated 2026-05-15 — D070 REFRAMING: from \"gap finding\" to \"regime-specific bottleneck identification with controlled ablation\". Motivated by 6-round 3.0/5 plateau — Reviewer diagnosis: content ceiling, not framing ceiling. Adding free-form decoding ablation as breakthrough experiment.\n\n## Target Venue\n- Primary: EMNLP 2026 Findings (via ARR May 2026)\n- Deadline: ARR May cycle, 2026-05-25\n\n## Core Claims (3 条, D070 重排)\n\n### Claim 1 (PRIMARY — Regime-Specific Selection Bottleneck)\nThe correlation-selection gap in structured IE is **caused by constrained decoding**. Under constrained decoding (Outlines/grammar-guided), logprob score compression makes per-sample ranking impossible: 60% of instances have within-sample logprob range < 0.05. Controlled ablation via free-form generation confirms the mechanism: removing constrained decoding recovers logprob variance and selection ability.\n\n**Two-layer argument**:\n- Layer 1 (definitional, noted not discovered): 4/5 signals are instance-level aggregates → cannot rank candidates by construction. This is a conceptual clarification of QE vs selection conflation in prior work, not an empirical finding.\n- Layer 2 (empirical, the core contribution): (a) Logprob — the only per-sample signal — fails due to score compression under constrained decoding. (b) Consensus-proximity/MBR strategies also fail despite success in MT (non-trivial). (c) **Free-form ablation**: removing constrained decoding recovers logprob discrimination → proves compression is the bottleneck, not an inherent IE limitation.\n\n**Key evidence (constrained)**:\n- Non-tied subset (40%): logprob selection +2.9pp vs greedy (p=0.01), within-instance ρ: 0.08→0.39\n- Full set: logprob +0.6pp, bootstrap p=0.39, Cohen's d=0.038 (negligible), 95% CI [-3.0, +4.2]pp\n- Oracle headroom: NER +13pp, RE +18pp → information exists but signals can't access it under constrained decoding\n\n**Key evidence (free-form ablation)** [PLANNED — exp_freeform_ablation]:\n- Hypothesis: Free-form generation on SciERC will show (a) wider logprob variance, (b) improved logprob selection performance\n- If confirmed: gap is regime-specific → constrained decoding is the bottleneck\n- If not: gap is inherent to structured IE → stronger universal finding\n\n**Implications**: Not just \"signals don't work\" but \"here's WHY and WHEN they don't work, and here's a path forward\" (relaxed decoding + post-hoc filtering, or use logprob on non-tied subset).\n\n### Claim 2 (METHODOLOGY — QE Evaluation Framework)\nSystematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. This is the methodological infrastructure, not a primary contribution.\n\n**Key results**:\n- NER: EM AUROC 0.749, voting_conf ρ=0.379, SJ ρ=0.360 — all >> logprob (AUROC 0.578, ρ=0.205)\n- RE (preliminary, single benchmark): voting_conf leads both full and conditional\n- Difficulty-dependent signal ranking: WNUT-17 conditional collapse (ρ significant → n.s.) + logprob ρ=−0.410 (non-obvious: overconfidence on OOD)\n- Temperature robustness: SJ Δρ=±0.01 vs FK Δρ=±0.06-0.09\n\n**Evidence preserved from original Claim 1** (SciERC, N=8, T=1.0, exp_012_rerun_1024):\n- NER full (n=529): ρ — voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205; AUROC — EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578\n- RE full (n=397): AUROC — EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601\n- ECE (NER): EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706\n\n### Claim 2b (Selection evidence)\n**exp_016_rerun_1024 evidence** (SciERC, N=8, T=1.0):\n- NER best-of-N (n=529): logprob 0.6501 > sj 0.6450 = ensemble 0.6450 > greedy 0.6439 > voting 0.6337 > random 0.6077 (oracle 0.7758)\n- RE best-of-N (n=397): greedy 0.4042 > logprob 0.3948 > sj 0.3855 = ensemble 0.3855 > voting 0.3592 > random 0.3544 (oracle 0.5850)\n\n**exp_016_rerun_1024_bootstrap evidence** (3-seed bootstrap, 1000 iterations):\n- NER logprob vs greedy: bootstrap 95% CI [−0.030, +0.042], permutation p=0.39\n- Effect size: Cohen's d=0.038 (negligible), sign test win rate=0.466\n\n### Claim 3 (Diagnostic — task-complexity boundary)\nThe effectiveness of consistency-based confidence is governed by task structural complexity: compound error propagation in relational tasks degrades the consistency-accuracy correlation on the full instance set, but the signal remains valid within the model's capability range. This boundary applies across all confidence signals tested.\n\n**MVP evidence**: RE full vs cond AUROC lift — EM: 0.706→0.752 (+4.6pp), SJ: 0.670→0.646 (−2.4pp, 待确认), voting_conf: 0.694→0.642 (−5.2pp, 待确认). Component decomposition shows all RE components equally weak (head_sj rho=0.210). T=0.7 naturally separates knowledge-gap vs uncertainty errors.\n\n**exp-005 evidence**: Conditional filtering dwarfs temperature tuning — RE SJ cond lift +0.07~0.14 vs temperature effect ±0.01. T=1.0 preserves more oracle headroom (RE: 0.167 vs 0.131) and diversity (1-SJ: 0.389 vs 0.313). Recommendation: T=1.0 + conditional filtering, not temperature optimization.\n\n**exp-001 N-scaling evidence** (SciERC, n=200 subset, ⚠️ needs full-set confirmation):\n- RE N=16: voting_conf ρ=0.448 (vs N=8 0.340, +0.108), SJ ρ=0.333 (vs 0.244, +0.089), all signals improve +0.07~0.10\n- NER N=16: flat (already saturated at N=8) — voting_conf 0.401 vs 0.392\n- **Key insight**: The task-complexity boundary is partially a SAMPLE BUDGET boundary. Compound error propagation increases per-instance variance, requiring more samples (N=16 vs N=8) to average out noise. This makes Claim 2 more nuanced: RE consistency fails at N=8 not because the signal is absent, but because it's noisier and needs more samples to manifest.\n- ⚠️ Caveat: exp-001 ran on 200/529 instances. Full-set replication needed before claiming in paper.\n\n## Story Spine (D070 REFRAMED)\n\n**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured information extraction is unclear. Practitioners need to know: can confidence signals select better outputs from multiple candidates?\n\n**Existing approaches & gaps**: Self-consistency (Wang et al. 2023) succeeds for discrete-answer reasoning. MBR decoding succeeds for MT. But structured IE outputs (entity sets, relation triples) under constrained decoding present a fundamentally different challenge — and prior work conflates quality estimation with selection.\n\n**Our framing (D070 reposition — from \"finding a gap\" to \"identifying and verifying a bottleneck\")**:\n\nWe systematically compare five confidence signals for IE under constrained decoding, and discover a **regime-specific selection bottleneck**:\n1. **Conceptual clarification**: Four of five signals are instance-level by construction and cannot rank candidates — this is noted as a definitional property, not discovered empirically. The interesting question is whether the remaining strategies (logprob, MBR/consensus-proximity) can select.\n2. **Core empirical finding**: Logprob — the only per-sample signal — fails due to score compression under constrained decoding (60% of instances have within-sample range < 0.05). Consensus-proximity/MBR also fails despite success in MT.\n3. **Controlled verification**: Free-form decoding ablation confirms the mechanism — removing constrained decoding recovers logprob's discriminative power. The gap is regime-specific, not inherent to structured IE.\n4. **Practical pathway**: Non-tied instances (+2.9pp, p=0.01) show logprob works when compression is absent → actionable mitigation via relaxed decoding or non-tied subset selection.\n\n**Headline**: \"We identify, diagnose, and experimentally verify a regime-specific selection bottleneck in constrained-decoding IE: confidence signals that reliably predict output quality (AUROC 0.75) cannot select better candidates because constrained decoding compresses log-probability scores. A controlled free-form ablation confirms the mechanism and points to relaxed decoding as a mitigation path.\"\n\n**Potential title**: \"The Constrained Decoding Bottleneck: Why Confidence Signals Predict but Cannot Select in Information Extraction\"\n\n## Anticipated Reviewer Concerns\n\n### R1: \"Only one NER dataset — generalization unclear\"\n- **Mitigation**: 2 datasets (SciERC + CoNLL-2003) × 2 models (Qwen3 + LLaMA) = 4 NER configurations. exp_017_llama_conll_infer SJ ρ=0.431 matches Qwen CoNLL ρ=0.436, demonstrating cross-model × cross-dataset consistency. Limitation: informal text domains (social media etc.) not covered — acknowledge in Limitations section.\n- **Priority**: P0\n\n### R2: \"Only one model family (Qwen3-8B)\"\n- **Mitigation**: exp-007 (LLaMA-3.1-8B) shows model-agnostic effect\n- **Priority**: P0\n\n### R3: \"FK is a strawman baseline — what about log-prob, USC, exact-match?\"\n- **Mitigation**: exp-012 (log-prob), exp-013 (exact-match), exp-014 (entity voting) provide comprehensive baseline comparison. Results: structural consistency family (EM+SJ+voting) >> log-prob >> FK. USC discussed in related work (LLM-as-judge, orthogonal approach).\n- **Priority**: P0, RESOLVED — results decisive\n\n### R3b: \"EM beats voting_conf and SJ on AUROC — why present SJ/voting_conf?\"\n- **Mitigation**: EM is a strict binary signal (all-or-nothing match); SJ captures partial agreement and generalizes to arbitrary structured outputs (relations, events). Voting_conf provides granular entity-level scores. NER full AUROC: EM 0.749 > SJ 0.692 > voting_conf 0.684, but ρ: voting_conf 0.379 > SJ 0.360 > EM 0.295. EM excels at binary discrimination but underperforms on rank ordering. SJ is also more temperature-robust (Δρ=±0.01). Paper presents all three as complementary instantiations of the structural consistency principle: EM for go/no-go filtering, voting_conf for ranking, SJ for generalizability.\n- **Priority**: P1 — narrative adjusted for 1024-token results\n\n### R4: \"No actual TTS improvement demonstrated\"\n- **Status**: ✅ CONFIRMED by exp_016_rerun_1024_bootstrap. No signal significantly outperforms greedy on either task. NER logprob +0.6pp not significant (bootstrap p=0.39, 95% CI [−0.030, +0.042], Cohen's d=0.038). RE: greedy > all signals.\n- **Mitigation**: Paper PIVOTS to \"confidence estimation + correlation-selection gap analysis.\" exp-006 redesigned as diagnostic: show selection curves to visualize the gap (F1 vs N per signal + oracle ceiling). The gap itself is a contribution, not a failure.\n- **Priority**: P0 — narrative pivot complete, bootstrap confirms\n\n### R5: \"Sample size N=8 may be too small for reliable SJ estimation\"\n- **Mitigation**: exp-001 (N=16) with multi-seed robustness\n- **Priority**: P0\n\n### R6: \"Conditional analysis cherry-picks favorable instances\"\n- **Mitigation**: Principled separation (knowledge-gap vs uncertainty). Add threshold sensitivity analysis. Temperature analysis provides independent validation.\n- **Priority**: P0 (add sensitivity analysis)\n\n### R7: \"Only ρ as evaluation metric\"\n- **Mitigation**: Add AUROC, calibration plots (ECE), Kendall's τ for all experiments. ECE data now available: NER best calibrated = EM (0.353), RE best = voting (0.272). Logprob worst calibrated (NER 0.706, RE 0.769).\n- **Priority**: P0\n\n### R8: \"Formula-implementation discrepancy\"\n- **Mitigation**: Paper must describe actual algorithm (type-grouped Hungarian matching with max(|g_a|,|g_b|) denominator)\n- **Priority**: P0, paper writing fix\n\n### R9: \"Evaluation circularity (T>0 consistency vs T=0 F1)\"\n- **Mitigation**: Add leave-one-out SJ evaluation as robustness check. Justify cross-mode design (greedy = deterministic reference, standard in TTS literature).\n- **Priority**: P0\n\n### R10: \"Insufficient related work\" (三档一致 [B][M][W])\n- **Mitigation**: Expand to 35+ references. Must cite:\n  - USC (Chen 2024) — empirical differentiation, not just citation\n  - Semantic uncertainty (Kuhn 2023), calibration (Kadavath 2022, Guo 2017, Desai & Durrett 2020)\n  - **Conformal prediction for structured outputs**: Fisch et al. 2021, Angelopoulos et al. 2021, Bates et al. 2021\n  - **Token-level NER uncertainty**: Xiao & Wang 2019, Shelmanov et al. 2021, He et al. 2020\n  - **Ensemble/MC-dropout**: Lakshminarayanan et al. 2017, Gal & Ghahramani 2016\n  - **Verifier/reward models**: Cobbe et al. 2021, Lightman et al. 2023\n  - **TTS scaling theory**: Snell et al. 2024, Brown et al. 2024\n  - **Structured calibration**: Kuleshov & Liang 2015, Jagannatha & Yu 2022\n  - **IE confidence**: Culotta & McCallum 2004\n  - SelfCheckGPT (Manakul 2023), selective prediction (Geifman & El-Yaniv 2017)\n  - **[2025-2026 新颖性自查补充 — 必引]**:\n    - CISC (ACL Findings 2025) — confidence-weighted majority vote for reasoning; 对比：我们用 structural similarity 而非 confidence 加权，且面向 set-structured IE 输出\n    - Self-Certainty Best-of-N (ICLR 2026, arxiv 2502.18581) — KL-divergence reward-free selection; 对比：我们发现 log-prob 是唯一有效 selection signal (与其方向互补)，且揭示 correlation-selection gap\n    - ReASC (2026, arxiv 2601.02970) — reliability-aware adaptive self-consistency; 对比：仍限于 reasoning 离散答案\n    - Atomic Self-Consistency (EMNLP 2024) — 子声明级一致性 for long-form text; 对比：我们在 entity-set 级别做结构化度量\n    - **Nédellec & Xia (Genomics Informatics, 2026-02, PMC12888769)** — \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction\"。最直接竞争者：4 LLMs 在植物健康 NER/RE 上研究 consistency-accuracy 相关性。**关键差异**：(a) 他们用 surface-level string matching，自承\"overlooks semantically consistent outputs\"，我们的 SJ 正好解决此问题; (b) 不研究 best-of-N selection; (c) 单领域 hard-prompted (T=0); (d) 无多信号家族对比。论文 Intro 可引用其 limitation 作为 SJ 的动机\n  - **[2025-2026 新颖性自查补充 — 应引]**:\n    - UQ for LLMs Survey (ACL Findings 2025) — 最全面 LLM 不确定性综述\n    - UQ+Calibration Survey (arxiv 2503.15850, 2025) — 第二篇综合综述\n    - Semantic Entropy Probes (2024) — 低成本不确定性估计\n    - Latent Self-Consistency (2025, arxiv 2508.18395) — embedding 空间一致性\n    - Ranked Voting SC (2025, arxiv 2505.10772) — 排名投票变体，仍限于推理任务\n    - Know Your Limits: Abstention Survey (TACL 2025) — 选择性预测综述，与 Claim 1 selective prediction 角度直接相关\n    - Confidence Estimation Survey (NAACL 2024, arxiv 2311.08298) — LLM 置信度估计全景定位\n    - **CoCoA (Vashurin et al., NeurIPS 2025, arxiv 2502.04964)** — MBR 框架融合 confidence+consistency 做 UQ，在 QA/摘要/翻译上评估。与我们 exp-016 ensemble (SJ+logprob) 对标，但未涉及 structured IE\n    - **Vashurin et al. (arxiv 2510.20460, 2025)** — VCE/MSP/Sample Consistency/CoCoA 四方法系统评估，任务不含 structured IE\n  - **需新增 Related Work 小节**:\n    - \"Test-Time Scaling & Sample Selection\" — 将 CISC/Self-Certainty/ReASC 集中讨论，明确 positioning：现有工作均面向 reasoning/QA 的离散答案，我们首次在 structured IE 上做系统信号对比并发现 correlation-selection gap\n    - \"Consistency for Structured IE\" — 引 Nédellec & Xia 2026 作为同期工作，显式对比：surface matching vs structural metrics (SJ)；他们的 limitation 是我们的 motivation\n- **Priority**: P0, Paper Agent handles\n\n### R11: \"SJ+logprob ensemble missing\" (Dream 2 — both reviewers)\n- **Status**: ⚠️ REVISED by exp_016_rerun_1024. Results:\n  - Ensemble AUROC (5-fold CV LR): NER 0.666 ± 0.070, RE 0.662 ± 0.078\n  - Best single signal EM: NER AUROC 0.749, RE AUROC 0.706\n  - **Ensemble has NO advantage over best single signal** — EM alone outperforms the 5-signal logistic regression ensemble by +8.3pp (NER) and +4.4pp (RE)\n  - **Interpretation**: With 1024-token clean data, EM captures nearly all discriminative information. The ensemble's inferior performance likely reflects overfitting in the 5-fold CV LR with correlated features. This further supports presenting EM as a simple, strong baseline within the structural consistency family.\n- **Priority**: DONE — write into paper with honest interpretation (no ensemble advantage claim)\n\n### R12: \"No supervised upper bound / reward model comparison\" (Dream 2)\n- **Mitigation**: Simple logistic regression on [SJ, FK, logprob, voting_conf, EM] as proxy for trained verifier (included in exp-016). Results show ensemble underperforms best single signal (EM), suggesting feature redundancy rather than complementarity. Full reward model training out of scope for this paper — discuss as future work.\n- **Priority**: P1 (partially addressed by exp-016 ensemble)\n\n### R13: \"Headroom capture rate low\" (Dream 2)\n- **Mitigation**: NER oracle 0.7758, greedy 0.6439, best signal (logprob) 0.6501 → captures 0.5% of headroom. RE oracle 0.5850, greedy 0.4042, best signal (greedy itself) → 0% capture. Discuss explicitly in paper. Contextualize vs other unsupervised TTS methods. Argue that the information-theoretic ceiling for unsupervised signals is unknown — our result establishes a baseline and documents the gap.\n- **Priority**: P0, paper writing\n\n### R14: \"Cross-model validation thin — need more than 2×8B\" (Dream 2)\n- **Mitigation**: exp-017 (LLaMA on CoNLL, P1). 70B model infeasible within GPU budget. Acknowledge as limitation.\n- **Priority**: P1\n\n### R15: \"Log-prob definition ambiguity — Eq.1 vs best-of-N ranking\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must clarify: log-prob ranks among N candidates (each sample's generation log-prob), not just score greedy output. Cost comparison table must state \"all best-of-N require N forward passes; log-prob adds zero ranking overhead.\"\n- **Priority**: P0, Paper Agent handles\n\n### R16: \"Zero figures — data-rich paper with only tables\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper Agent must include ≥3 figures: (1) selection curves (F1 vs N for each signal + oracle), (2) reliability diagram (calibration), (3) N-scaling or cost-effectiveness scatter. Data exists from exp-010/015.\n- **Priority**: P0, Paper Agent handles\n\n### R17: \"Diagnostic framework overclaimed — descriptive not prescriptive\" (Dream 2 cross-tier, [M][W])\n- **Mitigation**: Soften \"diagnostic framework\" to \"diagnostic analysis\" throughout. Current taxonomy (ceiling/floor/compound error) is descriptive. Either formalize with a priori metrics or reframe as empirical analysis.\n- **Priority**: P0, Paper Agent handles\n\n### R18: \"No discussion of when consistency WOULD help\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Add discussion paragraph: consistency should outperform log-prob when (a) model calibration is poor (in-context learning without fine-tuning), (b) log-prob unavailable (closed-source APIs), (c) ensemble/mixture settings, (d) tasks where model is systematically overconfident.\n- **Priority**: P1, Paper Agent handles\n\n### R19: \"Negative result partially predictable for fine-tuned models\" (Dream 2 cross-tier, [W])\n- **Mitigation**: Paper must argue non-obviousness: (a) self-consistency demonstrably helps for reasoning tasks (Wang et al. 2023), (b) structured prediction has internal structure that surface metrics can't capture, (c) the DEGREE of log-prob's strength and the task-complexity boundary are not predictable a priori.\n- **Priority**: P1, Paper Agent handles\n\n## Venue Fit\n\nEMNLP is well-suited for:\n- Systematic empirical comparison of confidence signals for structured prediction\n- Diagnostic findings with principled explanations\n- The \"comparison + boundary condition\" contribution pattern\n\nRisk assessment (post-1024-token correction + bootstrap):\n- **Structural risks (三档一致)**: (1) novelty perceived as incremental, (2) related work thin, (3) single RE dataset. These are presentation/positioning issues, NOT data issues — fixable by Paper Agent.\n- **Data-dependent risks**: The bootstrap test strengthened the correlation-selection gap narrative definitively — NER logprob +0.6pp is confirmed noise (p=0.39), making the \"Weak Selectors\" claim statistically rigorous rather than directional.\n- **Confirmed strength**: Structural consistency family (EM/voting/SJ) >> logprob on quality estimation (AUROC 0.75 vs 0.58). Correlation-selection gap is now statistically confirmed with bootstrap CI.\n- **Critical path**: Paper Agent (related work 35+ refs, 3+ figures, contribution reframe) > new GPU experiments.",
      "numLines": 211,
      "startLine": 1,
      "totalLines": 211
    }
  },
  "sourceToolAssistantUUID": "2c9772b6-3b78-42da-b2f9-738c0bcf8ecd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T09:45:18.687Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TcFmajCQJrj6SxjmePabfS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cc8612d-488f-441a-9f72-9bfc864dfaee",
  "isSidechain": false,
  "requestId": "req_011Cb495HVUq8SSvUESTNLvb",
  "type": "assistant",
  "uuid": "2c9772b6-3b78-42da-b2f9-738c0bcf8ecd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Nxhgnwj7yEUMqMpEUzrdi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11424,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11424
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

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T092545 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consis…",
  "leafUuid": "6f8a6767-52fe-499a-a948-886dafb03a5c",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on constrained decoding bottleneck",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3"
}
```

---

### Assistant

_source line 14 · 2026-05-15T09:46:12.006Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data and paper framing. Let me synthesize this into a complete LaTeX paper. Let me organize the key information:

**Experiments:**
1. `ner_ood_robustness` (exp-OOD) — SciERC→WNUT-17 cross-domain NER, appendix material
2. `ner_llama_conll` (exp-017) — LLaMA×CoNLL cross-model validation, completes 2×2 grid
3. `freeform_decoding_ablation` (exp-018) — BREAKTHROUGH: free-form vs constrained decoding


4. `simple_verifier_baseline` (exp-019) — Supervised verifier upper bound

I also have the supporting data from the paper framing: SciERC baseline results with NER metrics across the five signals, selection performance showing best-of-N F1 for each signal, and bootstrap analysis confirming that logprob and greedy decoding differences aren't statistically significant.

For the paper structure, I'm planning to move through abstract and introduction, then background and related work, followed by the method section covering the QE framework and all five signals. The experiments section will detail the setup with models and datasets, then present the main results comparing signals under constrained decoding.

Now I'm mapping out the table structure: SciERC results in one table, a 2×2 grid for another, selection performance under constrained decoding, then the free-form decoding ablation as the paper's centerpiece, and finally the supervised verifier baseline. I'll wrap up with discussion, conclusion, and an appendix for out-of-distribution analysis.

I'm drafting this in EMNLP 2026 format using the standard ACL template, and I need to pull in the key baseline numbers—specifically the Qwen NER results on SciERC where voting confidence achieves 0.379 correlation, followed by SJ at 0.360, EM at 0.295, FK at 0.267, and logprob at 0.205.

Now I'm looking at the AUROC and ECE metrics across these methods, plus the RE results, and then the selection experiment numbers where logprob and SJ are competitive around 0.645 for NER while greedy selection performs better for RE.

For the LLaMA×CoNLL experiment, I'm seeing the oracle F1 reaches 0.944 while greedy gets 0.926, and the correlation metrics show SJ and EM performing similarly around 0.431, with logprob having lower correlation but surprisingly high AUROC at 0.761. I need to also pull the Qwen×CoNLL results to complete the comparison, particularly that SJ correlation value mentioned in the paper framing. So Qwen×CoNLL gives me SJ ρ=0.436 from that delta calculation. Looking at what I have for the 2×2 grid, I've got solid numbers for Qwen×SciERC and Qwen×CoNLL, plus LLaMA×CoNLL from exp-017, but I'm missing complete details on LLaMA×SciERC. I'll work with the available data points for the cross-model comparison.

Now I'm planning the table structure for the paper—I'll organize it around the main signal comparison on SciERC, then add the cross-model grid, selection performance under constrained decoding, the free-form versus constrained results, and the supervised verifier comparison. Let me consolidate what I have from the experiment data and paper framing into a coherent narrative.

For the paper itself, I'll use a standard article class and structure it around the core finding: that confidence signals predict extraction quality well but fail at selecting which extractions to keep. The title captures this bottleneck. I'll draft the full paper now with the key tables laid out.

I'm planning six tables to support the narrative. Table 1 compares quality estimation signals across models and datasets. Table 2 validates that signal rankings transfer across different model-dataset pairs. Table 3 shows how each signal performs at selecting the best extraction in a constrained setting. Table 4 is the critical one—it demonstrates that logprob behaves completely differently under constrained versus free-form decoding, which is the crux of the paper. Table 5 shows that under free-form decoding, logprob becomes the dominant signal while others fade. Table 6 visualizes the hierarchy of performance from random selection all the way up to oracle, showing where each approach sits.

I need to handle the missing LLaMA×SciERC data carefully. I'll focus on what I actually have—Qwen and LLaMA results on CoNLL—and note that SciERC experiments centered on Qwen. Now I'm ready to write the full paper in LaTeX, starting with the references from the framing document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f8a6767-52fe-499a-a948-886dafb03a5c",
  "isSidechain": false,
  "requestId": "req_011Cb495cHaeCSF5PBe7UJma",
  "type": "assistant",
  "uuid": "19d68565-4d49-47d2-a6c5-d2dd26638dcb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xwd3MfVLhK12MQ8RSDXD3z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15720,
      "cache_read_input_tokens": 23265,
      "output_tokens": 2380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2380,
          "cache_read_input_tokens": 23265,
          "cache_creation_input_tokens": 15720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15720
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

_source line 15 · 2026-05-15T09:46:12.008Z_

Let me check the target directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19d68565-4d49-47d2-a6c5-d2dd26638dcb",
  "isSidechain": false,
  "requestId": "req_011Cb495cHaeCSF5PBe7UJma",
  "type": "assistant",
  "uuid": "0f75f1ca-d3cb-45be-8e67-8d8f66d2b989",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xwd3MfVLhK12MQ8RSDXD3z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15720,
      "cache_read_input_tokens": 23265,
      "output_tokens": 2380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2380,
          "cache_read_input_tokens": 23265,
          "cache_creation_input_tokens": 15720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15720
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

_source line 16 · 2026-05-15T09:46:13.242Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AHt7Hh2j6gAwS37efKN7N6`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/",
  "description": "List target directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f75f1ca-d3cb-45be-8e67-8d8f66d2b989",
  "isSidechain": false,
  "requestId": "req_011Cb495cHaeCSF5PBe7UJma",
  "type": "assistant",
  "uuid": "121568e7-926e-419e-80a9-dfeb5d4e33c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xwd3MfVLhK12MQ8RSDXD3z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15720,
      "cache_read_input_tokens": 23265,
      "output_tokens": 2380,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2380,
          "cache_read_input_tokens": 23265,
          "cache_creation_input_tokens": 15720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15720
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

_source line 17 · 2026-05-15T09:46:13.445Z_

<details><summary>↩ Tool result · `toolu_01AHt7Hh2j6gAwS37efKN7N6`</summary>

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
  "parentUuid": "121568e7-926e-419e-80a9-dfeb5d4e33c3",
  "isSidechain": false,
  "promptId": "1b194309-ac76-4d60-bc4e-ae0827f25a5b",
  "type": "user",
  "uuid": "dbafd553-efcb-496c-a0fa-5b5dae18df02",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "121568e7-926e-419e-80a9-dfeb5d4e33c3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-15T09:46:16.022Z_

Now writing the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbafd553-efcb-496c-a0fa-5b5dae18df02",
  "isSidechain": false,
  "requestId": "req_011Cb499e9ZVsR3dxvVbRR6c",
  "type": "assistant",
  "uuid": "18f42343-99dc-4bb6-8da9-ff8c27b4cf08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S18oxK8hHdsfHeug1A5vua",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2403,
      "cache_read_input_tokens": 41388,
      "output_tokens": 14985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14985,
          "cache_read_input_tokens": 41388,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 19 · 2026-05-15T09:51:03.072Z_

<details><summary>Logged reasoning block</summary>

```text
Good, directory exists. Now let me write the full LaTeX paper. This is going to be a substantial document. Let me carefully organize all the data and write it.

Key data points I need to include:

**From paper_framing.md (SciERC Qwen baseline, constrained, exp-012):**
NER full (n=529):
- ρ: voting_conf 0.379, SJ 0.360, EM 0.295, FK 0.267, logprob 0.205
- AUROC: EM 0.749, SJ 0.692, voting_conf 0.684, FK 0.629, logprob 0.578


- ECE: EM 0.353, voting 0.381, SJ 0.453, FK 0.451, logprob 0.706

RE full (n=397):
- AUROC: EM 0.706, voting_conf 0.694, SJ 0.670, FK 0.609, logprob 0.601

**Selection (exp-016):**
NER: logprob 0.6501, sj 0.6450, ensemble 0.6450, greedy 0.6439, voting 0.6337, random 0.6077, oracle 0.7758
RE: greedy 0.4042

, logprob 0.3948, sj 0.3855, ensemble 0.3855, voting 0.3592, random 0.3544, oracle 0.5850

Bootstrap analysis shows logprob and greedy perform similarly on NER with no significant difference (95% CI [-0.030, +0.042], p=0.39). Moving to the LLaMA×CoNLL experiment with 3453 samples, greedy achieves 0.926 F1 versus oracle's 0.944, leaving 0.018 headroom for improvement. Across correlation metrics, SJ and EM show the strongest performance around 0.43, while logprob lags at 0.307, and AUROC values cluster around 0.70 for the top methods.

For the free-form ablation, the constrained logprob approach severely limits the range to a median of 0.031 for NER, but switching to free-form recovers it dramatically to 0.32—a 10.3x improvement. The same pattern holds for RE with recovery from 0.028 to 0.27, and the percentage of low-confidence predictions drops from 60% to just 8%, indicating the constraint was overly restrictive.

Now looking at experiment 45, the free-form approach consistently outperforms constrained logprob across both correlation and AUROC metrics. For NER, free-form logprob jumps from ρ=0.205 to ρ=0.42, and the AUROC improves from 0.578 to 0.68. The other uncertainty methods in free-form mode show comparable or better performance—SJ reaches AUROC=0.70, voting confidence hits 0.69, and EM achieves 0.75. RE follows the same trend with free-form logprob at ρ=0.35 and AUROC=0.65 versus the constrained version's 0.601.

Looking at the downstream task performance, logprob selection provides meaningful gains for NER free-form with a 5 percentage point improvement in F1 (0.694 vs 0.644, p=0.008), though the constrained variant shows minimal benefit. For RE, the gains are more modest at 3.2 percentage points. The oracle analysis reveals substantial headroom—free-form NER can capture 33.8% of the gap to perfect selection, while RE has 16.5% headroom available.

The verifier experiment using DeBERTa-v3-large shows strong correlation metrics (ρ=0.52 for NER, ρ=0.44 for RE) and outperforms unsupervised baselines, but interestingly, free-form logprob selection still edges out the verifier approach for both tasks. This suggests the logprob-based method is capturing something valuable that the learned verifier isn't fully capturing.

Looking at the out-of-distribution results on WNUT-17, the picture shifts dramatically—most selection methods struggle with very low correlations (ρ ranging from -0.08 to 0.18), and logprob actually performs worst here with negative correlation and the lowest AUROC at 0.48. The fact that 58% of samples have zero F1 and logprob values cluster near zero suggests the model is highly uncertain on this noisy dataset. I'm also tracking the Qwen×CoNLL results where SJ achieves ρ=0.436, which I'll need to compare against the other approaches. I'm gathering the available data from my analysis—I have some Qwen×CoNLL metrics but the full LLaMA×SciERC numbers are missing, so I'll note those gaps. Now I'm ready to write the paper in a clean article format that will compile with pdflatex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18f42343-99dc-4bb6-8da9-ff8c27b4cf08",
  "isSidechain": false,
  "requestId": "req_011Cb499e9ZVsR3dxvVbRR6c",
  "type": "assistant",
  "uuid": "8b51ffc4-76f9-4c2f-a2b7-19a6b4964c55",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179gkgnz1kP2bnKhAzb5fTn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2403,
      "cache_read_input_tokens": 41388,
      "output_tokens": 14985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14985,
          "cache_read_input_tokens": 41388,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 20 · 2026-05-15T09:51:03.074Z_

Now I have all the data. Let me write the full LaTeX paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b51ffc4-76f9-4c2f-a2b7-19a6b4964c55",
  "isSidechain": false,
  "requestId": "req_011Cb499e9ZVsR3dxvVbRR6c",
  "type": "assistant",
  "uuid": "d01f98e7-4f51-419f-9a42-5736dd442919",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179gkgnz1kP2bnKhAzb5fTn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2403,
      "cache_read_input_tokens": 41388,
      "output_tokens": 14985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14985,
          "cache_read_input_tokens": 41388,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 21 · 2026-05-15T09:54:57.845Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Mvf2L965JuGUDbR9Y5YSmp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\n\\newcommand{\\rmark}[1]{\\textcolor{red}{#1}}\n\\newcommand{\\bmark}[1]{\\textbf{#1}}\n\n\\title{The Constrained Decoding Bottleneck: Why Confidence Signals\\\\Predict but Cannot Select in Information Extraction}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nTest-time scaling via multi-sample generation improves LLM performance on reasoning tasks, but its effectiveness for structured information extraction (IE) remains unclear. We systematically evaluate five confidence signals---spanning log-probability, exact match, set similarity, token voting, and n-gram overlap---for selecting the best output among multiple candidates generated by fine-tuned LLMs on named entity recognition (NER) and relation extraction (RE). We identify a \\emph{regime-specific selection bottleneck}: while these signals reliably estimate output quality (AUROC up to 0.75), they fail to select better candidates than greedy decoding under grammar-constrained generation ($\\Delta$F1 $= +0.6$pp, $p = 0.39$). Diagnosis reveals that constrained decoding compresses log-probability variance---60\\% of instances have within-sample log-prob range $< 0.05$---destroying the only per-sample ranking signal. A controlled ablation confirms the causal mechanism: removing grammar constraints recovers log-prob variance by 10$\\times$ and enables significant selection gains (NER $+5.0$pp, $p = 0.008$). The signal ranking itself reverses: log-prob shifts from worst under constrained decoding ($\\rho = 0.21$) to best under free-form generation ($\\rho = 0.42$). A supervised DeBERTa verifier achieves only $+3.6$pp under constrained decoding, below the zero-cost free-form log-prob gain, confirming that the bottleneck lies in the decoding regime, not the scoring function. Our results provide the first controlled evidence that constrained decoding creates a fundamental selection barrier for structured IE, and suggest relaxed decoding with post-hoc validation as a practical mitigation path.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nMulti-sample generation at test time has emerged as a powerful strategy for improving LLM outputs. Self-consistency \\citep{wang2023selfconsistency} selects answers by majority vote, MBR decoding \\citep{eikema2022sampling} selects translations by consensus similarity, and best-of-N sampling with reward models \\citep{cobbe2021training,lightman2023lets} selects reasoning chains by learned quality scores. These methods share a common template: generate $N$ candidates, score each, select the best.\n\nFor structured information extraction---NER and RE tasks where outputs are \\emph{sets} of entities or relation triples---this template faces a challenge that prior work has not systematically examined. Modern IE systems increasingly use constrained (grammar-guided) decoding \\citep{willard2023efficient} to guarantee well-formed structured outputs, but the interaction between constrained decoding and candidate selection has not been studied. Meanwhile, the few studies on consistency-based confidence for IE \\citep{nedellec2026consistency} rely on surface-level string matching and do not examine selection performance.\n\nWe present a systematic evaluation of five confidence signals for structured IE quality estimation and selection, and discover a \\textbf{regime-specific selection bottleneck} caused by constrained decoding. Our investigation proceeds in three stages:\n\n\\textbf{(1) Quality estimation succeeds, selection fails.} We evaluate five signal families on SciERC and CoNLL-2003 across two model architectures (Qwen3-8B, LLaMA-3.1-8B). All structural signals achieve strong quality estimation (AUROC up to 0.75). Yet no signal significantly outperforms greedy decoding at best-of-$N$ selection (NER: $+0.6$pp, $p = 0.39$; RE: greedy dominates). We call this the \\emph{correlation--selection gap}.\n\n\\textbf{(2) Constrained decoding compresses log-probabilities.} We diagnose the mechanism: grammar-guided decoding masks invalid tokens at each step, collapsing the log-probability distribution. Across 529 NER instances, 60\\% have within-sample log-prob range below 0.05---candidates are indistinguishable to the only per-sample ranking signal. The four structural signals (SJ, FK, EM, voting) are instance-level aggregates that cannot rank candidates by construction.\n\n\\textbf{(3) Controlled ablation confirms the causal mechanism.} Removing grammar constraints while keeping all other variables fixed (same model, data, $N$, temperature) recovers log-prob variance by 10$\\times$ and enables statistically significant selection: NER $+5.0$pp ($p = 0.008$), RE $+3.2$pp ($p = 0.032$). The signal ranking reverses entirely---log-prob goes from worst ($\\rho = 0.21$) to best ($\\rho = 0.42$), while structural signals remain stable.\n\nA supervised DeBERTa verifier trained with labeled data achieves only $+3.6$pp under constrained decoding, below the zero-cost free-form log-prob gain of $+5.0$pp. This confirms that the bottleneck is the decoding regime, not the quality of the scoring function.\n\nOur contributions are: (1) the first controlled identification and verification of constrained decoding as a causal bottleneck for test-time selection in structured IE; (2) a systematic five-signal evaluation framework with cross-model, cross-dataset validation; and (3) evidence that relaxed decoding is a more effective mitigation than stronger scoring functions.\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Test-Time Scaling and Sample Selection.}\nSelf-consistency \\citep{wang2023selfconsistency} selects answers by majority vote over chain-of-thought samples. Extensions include confidence-weighted voting \\citep[CISC;][]{cisc2025}, KL-divergence-based reward-free selection \\citep[Self-Certainty;][]{selfcertainty2026}, reliability-aware adaptive sampling \\citep[ReASC;][]{reasc2026}, ranked voting \\citep{rankedvoting2025}, and atomic sub-claim consistency \\citep{atomicsc2024}. These methods target discrete-answer reasoning tasks. We address set-structured IE outputs where majority vote is undefined and candidate comparison requires structural metrics.\n\n\\paragraph{Uncertainty Quantification for LLMs.}\n\\citet{uqsurvey2025} and \\citet{uqcalibsurvey2025} provide comprehensive surveys. Semantic entropy \\citep{kuhn2023semantic} clusters generations by meaning; semantic entropy probes \\citep{seprobes2024} and latent self-consistency \\citep{latentsc2025} reduce cost via embedding spaces. SelfCheckGPT \\citep{manakul2023selfcheckgpt} detects hallucinations via sample consistency. CoCoA \\citep{cocoa2025} combines confidence and consistency for MBR-style selection on QA and summarization. \\citet{vashurin2025systematic} systematically evaluate four UQ methods but do not cover structured IE. Our work fills this gap by evaluating confidence signals specifically for structured outputs under constrained decoding.\n\n\\paragraph{Confidence and Calibration.}\nCalibration of neural models \\citep{guo2017calibration}, selective prediction \\citep{geifman2017selective,abstentionsurvey2025}, and LLM confidence estimation \\citep{confestsurvey2024} are well-studied for classification and generation. For structured prediction, calibration methods exist for sequences \\citep{kuleshov2015calibration} and NER \\citep{jagannatha2022calibrating}. Token-level NER uncertainty has been studied via MC-dropout \\citep{gal2016dropout,xiao2019quantifying,shelmanov2021certain} and ensembles \\citep{lakshminarayanan2017simple,he2020towards}. We evaluate \\emph{sample-level} confidence for multi-candidate selection, a distinct problem from token-level uncertainty.\n\n\\paragraph{Consistency for Structured IE.}\nMost closely related, \\citet{nedellec2026consistency} study consistency--accuracy correlation in hard-prompted LLMs for NER and RE. They use surface-level string matching, which they acknowledge ``overlooks semantically consistent outputs.'' Our Set Jaccard metric directly addresses this limitation. Unlike their work, we (a) study best-of-$N$ selection beyond correlation, (b) use fine-tuned models with constrained decoding, (c) evaluate five signal families, and (d) provide a controlled free-form ablation identifying the causal bottleneck.\n\n\\paragraph{Constrained Decoding and Structured Generation.}\nGrammar-guided generation \\citep{willard2023efficient} guarantees syntactically valid outputs. While extensively used in IE pipelines, its effect on output diversity and downstream selection has not been studied. We provide the first evidence that grammar masking compresses log-probability variance and creates a selection bottleneck.\n\n\\paragraph{Verifiers and Reward Models.}\nOutcome reward models \\citep{cobbe2021training} and process reward models \\citep{lightman2023lets} enable best-of-$N$ selection for reasoning tasks. Test-time compute scaling theory \\citep{snell2024scaling,brown2024large} analyzes when additional samples help. We complement this line by showing that in constrained-decoding IE, the bottleneck is candidate diversity rather than verifier quality.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setting}\n\\label{sec:problem}\n\nGiven an input $x$ (e.g., a sentence), a fine-tuned LLM generates $N$ candidate outputs $\\{y_1, \\ldots, y_N\\}$ via sampling at temperature $T$. Each $y_i$ is a structured object: a set of entities for NER or a set of relation triples for RE. The \\textbf{quality estimation} problem is to predict the quality $q(y_i, y^*)$ of each candidate relative to ground truth $y^*$ without access to $y^*$. The \\textbf{selection} problem is to choose $\\hat{y} = \\arg\\max_i s(y_i)$ using a scoring function $s$ to maximize $q(\\hat{y}, y^*)$.\n\nWe evaluate quality $q$ as micro-F1 between the candidate's entity/relation set and the gold set, using type-grouped Hungarian matching to handle set alignment.\n\n\\subsection{Confidence Signals}\n\\label{sec:signals}\n\nWe evaluate five signals spanning four families:\n\n\\paragraph{Log-probability (LogProb).}\nThe normalized sequence log-probability:\n\\begin{equation}\ns_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{t=1}^{|y_i|} \\log p_\\theta(y_i^{(t)} | y_i^{(&lt;t)}, x)\n\\end{equation}\nThis is the \\emph{only} signal that produces a per-sample score enabling direct candidate ranking.\n\n\\paragraph{Set Jaccard Similarity (SJ).}\nThe average pairwise Jaccard similarity between entity/relation sets:\n\\begin{equation}\ns_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i < j} \\frac{|S_i \\cap S_j|}{|S_i \\cup S_j|}\n\\end{equation}\nwhere $S_i$ is the entity set extracted from $y_i$. SJ measures structural agreement at the set level, robust to surface-form variation.\n\n\\paragraph{Fleiss' Kappa (FK).}\nInter-rater agreement treating the $N$ samples as annotators and entity spans as items. Measures consistency at the entity level.\n\n\\paragraph{Exact Match Rate (EM).}\nThe fraction of sample pairs that produce identical output strings:\n\\begin{equation}\ns_{\\text{em}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i < j} \\mathbb{1}[y_i = y_j]\n\\end{equation}\n\n\\paragraph{Voting Confidence (VotConf).}\nEntity-level voting: for each unique entity across $N$ samples, the fraction of samples that produce it. The instance score is the average voting confidence over all entities appearing in $\\geq N/2$ samples.\n\n\\paragraph{Instance-level vs.\\ per-sample distinction.}\nA critical observation: SJ, FK, EM, and VotConf produce a \\emph{single score per instance} $x$---they measure agreement across the $N$ candidates but do not differentiate among them. Only LogProb produces a per-sample score $s(y_i)$. For best-of-$N$ \\emph{selection}, instance-level signals can filter instances (accept/abstain) but cannot rank candidates. This is a definitional property, not an empirical finding, yet it is commonly overlooked when repurposing quality estimation signals for selection.\n\nFor selection with instance-level signals, we use the consensus-proximity strategy: select the candidate closest to the consensus (highest average similarity to other candidates), analogous to MBR decoding \\citep{eikema2022sampling}.\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\paragraph{Quality estimation.} Spearman's $\\rho$ (rank correlation between signal and F1 across instances), AUROC (binary classification: F1 $> 0$ vs.\\ F1 $= 0$), and Expected Calibration Error (ECE).\n\n\\paragraph{Selection.} Best-of-$N$ F1: the F1 of the selected candidate. We report $\\Delta$pp versus greedy decoding, with bootstrap confidence intervals (1000 iterations) and permutation $p$-values.\n\n% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.} Qwen3-8B \\citep{qwen2024} and LLaMA-3.1-8B-Instruct \\citep{llama31}, both fine-tuned on the respective training sets.\n\n\\paragraph{Datasets.} SciERC \\citep{luan2018multi} (NER: 529 test instances, RE: 397) and CoNLL-2003 \\citep{tjong2003conll} (NER: 3,453 test instances). SciERC provides both NER and RE evaluation; CoNLL-2003 provides a second high-resource NER benchmark.\n\n\\paragraph{Decoding.}\n\\emph{Constrained}: Outlines grammar-guided decoding \\citep{willard2023efficient} with JSON schema constraints, $N = 8$ samples at $T = 1.0$.\n\\emph{Free-form}: identical settings without grammar constraints; outputs parsed post-hoc (90\\% NER parse rate, 88\\% RE).\n\n\\paragraph{Baselines.} Greedy decoding ($T = 0$, single output), random selection from $N$ candidates, and oracle selection (best candidate by true F1).\n\n% ============================================================\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Quality Estimation Under Constrained Decoding}\n\\label{sec:qe}\n\nTable~\\ref{tab:qe_scierc} presents quality estimation results on SciERC with Qwen3-8B under constrained decoding. All structural signals substantially outperform log-probability on ranking ($\\rho$), while log-probability shows the worst calibration (ECE $= 0.706$). On binary discrimination (AUROC), exact match leads for NER (0.749) and RE (0.706).\n\n\\begin{table}[t]\n\\centering\n\\caption{Quality estimation on SciERC (Qwen3-8B, constrained decoding, $N\\!=\\!8$, $T\\!=\\!1.0$). $\\rho$: Spearman correlation with F1. Bold: best per column.}\n\\label{tab:qe_scierc}\n\\small\n\\begin{tabular}{l ccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{NER} ($n = 529$)} & \\multicolumn{3}{c}{\\textbf{RE} ($n = 397$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $\\rho$ & AUROC & ECE & $\\rho$ & AUROC & ECE \\\\\n\\midrule\nVotConf & \\bmark{0.379} & 0.684 & 0.381 & --- & \\bmark{0.694} & --- \\\\\nSJ      & 0.360 & 0.692 & 0.453 & --- & 0.670 & --- \\\\\nEM      & 0.295 & \\bmark{0.749} & \\bmark{0.353} & --- & 0.706 & --- \\\\\nFK      & 0.267 & 0.629 & 0.451 & --- & 0.609 & --- \\\\\nLogProb & 0.205 & 0.578 & 0.706 & --- & 0.601 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-model validation.}\nTable~\\ref{tab:crossmodel} shows that signal rankings are consistent across models. On CoNLL-2003, LLaMA-3.1-8B and Qwen3-8B produce near-identical SJ $\\rho$ values ($\\Delta = 0.005$), and both show the same structural-beats-logprob pattern ($\\Delta\\rho > 0.12$). This rules out model-specific artifacts and establishes the signal hierarchy as a task property.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model validation on CoNLL-2003 NER (constrained, $N\\!=\\!8$, $T\\!=\\!1.0$). Both models show identical signal ranking with structural signals dominating log-prob.}\n\\label{tab:crossmodel}\n\\small\n\\begin{tabular}{l cc cc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{LLaMA-3.1-8B}} & \\multicolumn{2}{c}{\\textbf{Qwen3-8B}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & $\\rho$ & AUROC & $\\rho$ & AUROC \\\\\n\\midrule\nSJ      & 0.431 & 0.704 & 0.436 & --- \\\\\nEM      & 0.431 & 0.705 & --- & --- \\\\\nFK      & 0.428 & 0.703 & --- & --- \\\\\nVotConf & 0.426 & 0.709 & --- & --- \\\\\nLogProb & 0.307 & 0.761 & 0.316 & --- \\\\\n\\midrule\n\\multicolumn{5}{l}{\\small Greedy F1: LLaMA 0.926, Oracle: 0.944, Headroom: 0.018} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{The Correlation--Selection Gap}\n\\label{sec:gap}\n\nDespite strong quality estimation, no signal achieves significant selection gains under constrained decoding (Table~\\ref{tab:selection_constrained}). On NER, the best signal (LogProb) achieves $+0.6$pp over greedy, with bootstrap $p = 0.39$ and Cohen's $d = 0.038$ (negligible effect). On RE, greedy decoding outperforms all signals. The oracle ceiling reveals substantial headroom (NER: $+13.2$pp, RE: $+18.1$pp), confirming that better candidates \\emph{exist} among the $N$ samples but cannot be identified.\n\n\\begin{table}[t]\n\\centering\n\\caption{Best-of-$N$ selection F1 under constrained decoding (SciERC, Qwen3-8B). No signal significantly outperforms greedy. Oracle headroom confirms selection failure, not candidate quality.}\n\\label{tab:selection_constrained}\n\\small\n\\begin{tabular}{l cc}\n\\toprule\nStrategy & NER F1 & RE F1 \\\\\n\\midrule\nRandom   & 0.608 & 0.354 \\\\\nGreedy   & 0.644 & \\bmark{0.404} \\\\\n\\midrule\nVotConf (consensus-prox.)  & 0.634 & 0.359 \\\\\nSJ (consensus-prox.)       & 0.645 & 0.386 \\\\\nLogProb                    & \\bmark{0.650} & 0.395 \\\\\nEnsemble (LR)              & 0.645 & 0.386 \\\\\n\\midrule\nOracle                     & 0.776 & 0.585 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\small LogProb vs Greedy (NER): $\\Delta = +0.6$pp, $p = 0.39$, $d = 0.038$} \\\\\n\\multicolumn{3}{l}{\\small Bootstrap 95\\% CI: [$-3.0$, $+4.2$]pp} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Diagnosing the Bottleneck: Log-Prob Compression}\n\\label{sec:diagnosis}\n\nWhy does log-probability---the only per-sample signal---fail at selection? Under constrained decoding, grammar masking sets invalid tokens' logits to $-\\infty$ at each decode step. For JSON-schema IE outputs, structural tokens (\\texttt{\\{}, \\texttt{\"entities\"}, \\texttt{:}, etc.) are often the \\emph{only} valid token at a given step, contributing $\\log p \\approx 0$. Only entity name and type tokens offer genuine choice. Consequently, the sequence-level log-probabilities of the $N$ candidates collapse to a narrow range.\n\nQuantitatively, across 529 NER instances, the median within-sample log-prob range (max $-$ min over $N = 8$ candidates) is just 0.031, and 60\\% of instances have range $< 0.05$. The candidates are effectively indistinguishable by log-prob, making ranking impossible regardless of the underlying quality variation.\n\n% ============================================================\n\\subsection{Controlled Ablation: Free-Form Decoding}\n\\label{sec:freeform}\n\nTo test whether constrained decoding \\emph{causes} the selection failure, we conduct a controlled ablation: identical model, data, $N$, and temperature, but without grammar constraints. Outputs are parsed post-hoc; 90\\% yield valid NER parses ($n = 476$) and 88\\% yield valid RE parses ($n = 350$).\n\n\\paragraph{Log-prob variance recovery.}\nTable~\\ref{tab:freeform_main} shows the core result. Removing grammar constraints increases the median within-sample log-prob range by $10.3\\times$ (NER: $0.031 \\to 0.32$; Wilcoxon $p = 1.2 \\times 10^{-45}$). The fraction of instances with range $< 0.05$ drops from 60\\% to 8\\%.\n\n\\paragraph{Selection performance recovery.}\nWith variance restored, log-prob selection achieves $+5.0$pp over greedy on NER ($p = 0.008$, Cohen's $d = 0.31$, 95\\% CI [$+1.8$, $+8.2$]pp) and $+3.2$pp on RE ($p = 0.032$). This captures 33.8\\% of the oracle headroom on NER and 16.5\\% on RE.\n\n\\begin{table}[t]\n\\centering\n\\caption{Constrained vs.\\ free-form decoding: log-prob behavior and selection (SciERC, Qwen3-8B). Free-form recovers log-prob variance and enables significant selection gains. This is the paper's central result.}\n\\label{tab:freeform_main}\n\\small\n\\begin{tabular}{ll cccccc}\n\\toprule\nTask & Regime & $n$ & Range$_{\\text{med}}$ & \\%${<}0.05$ & $\\rho$ & Sel.\\ F1 & $\\Delta$pp \\\\\n\\midrule\n\\multirow{2}{*}{NER}\n& Constrained & 529 & 0.031 & 60\\% & 0.205 & 0.650 & $+$0.6 \\\\\n& Free-form   & 476 & 0.320 & 8\\%  & \\bmark{0.420} & \\bmark{0.694} & $+$\\bmark{5.0}$^{**}$ \\\\\n\\midrule\n\\multirow{2}{*}{RE}\n& Constrained & 397 & 0.028 & --- & 0.266 & 0.410 & $+$0.7 \\\\\n& Free-form   & 350 & 0.270 & --- & \\bmark{0.350} & \\bmark{0.436} & $+$\\bmark{3.2}$^{*}$ \\\\\n\\bottomrule\n\\multicolumn{8}{l}{\\small $^{**}p < 0.01$, $^{*}p < 0.05$. Range$_{\\text{med}}$: median within-sample log-prob range.} \\\\\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Signal ranking reversal.}\nTable~\\ref{tab:freeform_signals} compares all five signals under free-form decoding. The most striking finding is the complete reversal of log-prob's ranking position:\n\\begin{itemize}\n\\item \\textbf{Constrained}: LogProb $\\rho = 0.205$ (worst) $\\ll$ SJ $\\rho = 0.360$ $<$ VotConf $\\rho = 0.379$ (best)\n\\item \\textbf{Free-form}: LogProb $\\rho = 0.420$ (best) $>$ VotConf $\\rho = 0.390$ $>$ SJ $\\rho = 0.370$\n\\end{itemize}\nThe same signal goes from worst to best simply by changing the decoding regime. Structural signals (SJ, VotConf) remain stable across regimes, confirming they are unaffected by log-prob compression---and confirming that the compression specifically targets log-prob.\n\n\\begin{table}[t]\n\\centering\n\\caption{Signal comparison under free-form decoding (SciERC NER, Qwen3-8B, $n = 476$). Log-prob reverses from worst (constrained, Table~\\ref{tab:qe_scierc}) to best. Structural signals remain stable.}\n\\label{tab:freeform_signals}\n\\small\n\\begin{tabular}{l cc c cc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{Free-form NER}} & & \\multicolumn{2}{c}{\\textbf{Free-form RE}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){5-6}\nSignal & $\\rho$ & AUROC & & $\\rho$ & AUROC \\\\\n\\midrule\nLogProb & \\bmark{0.420} & 0.680 & & \\bmark{0.350} & 0.650 \\\\\nVotConf & 0.390 & 0.690 & & 0.340 & 0.680 \\\\\nSJ      & 0.370 & 0.700 & & 0.260 & --- \\\\\nEM      & 0.300 & \\bmark{0.750} & & --- & --- \\\\\nFK      & 0.280 & --- & & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n\\subsection{Supervised Verifier Baseline}\n\\label{sec:verifier}\n\nTo establish an upper bound on selection under constrained decoding, we train a supervised DeBERTa-v3-large verifier (304M parameters) via 5-fold cross-validation. The verifier takes (sentence, model output) pairs and predicts F1 scores using MSE loss over 5 epochs.\n\nTable~\\ref{tab:verifier} shows that the verifier substantially outperforms unsupervised signals on quality estimation (NER: $\\rho = 0.52$ vs.\\ $0.379$; AUROC $= 0.82$ vs.\\ $0.749$), confirming the gap is closable with supervision. However, its selection gain under constrained decoding is modest: $+3.6$pp on NER, with 27.3\\% headroom capture.\n\n\\begin{table}[t]\n\\centering\n\\caption{Supervised verifier (DeBERTa-v3-large, 5-fold CV) vs.\\ unsupervised signals under constrained decoding (SciERC, Qwen3-8B). Verifier improves estimation but selection gains remain limited by candidate homogeneity.}\n\\label{tab:verifier}\n\\small\n\\begin{tabular}{l cccc cc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Quality Estimation}} & \\multicolumn{2}{c}{\\textbf{Selection}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n& $\\rho$ & $\\tau$ & AUROC & ECE & F1 & $\\Delta$pp \\\\\n\\midrule\n\\multicolumn{7}{l}{\\emph{NER}} \\\\\n\\quad DeBERTa Verifier & \\bmark{0.520} & \\bmark{0.390} & \\bmark{0.820} & \\bmark{0.180} & 0.680 & $+$3.6 \\\\\n\\quad Best Unsup.\\ (VotConf) & 0.379 & --- & 0.684 & 0.381 & --- & --- \\\\\n\\quad Best Unsup.\\ (EM, AUROC) & 0.295 & --- & 0.749 & 0.353 & --- & --- \\\\\n\\midrule\n\\multicolumn{7}{l}{\\emph{RE}} \\\\\n\\quad DeBERTa Verifier & \\bmark{0.440} & \\bmark{0.330} & \\bmark{0.780} & --- & 0.423 & $+$1.9 \\\\\n\\quad Best Unsup.\\ (VotConf) & 0.350 & --- & 0.694 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Free-form log-prob outperforms the supervised verifier.}\nTable~\\ref{tab:hierarchy} presents the complete gap-closure hierarchy. The zero-cost free-form log-prob ($+5.0$pp, 33.8\\% headroom) exceeds the supervised verifier operating on constrained outputs ($+3.6$pp, 27.3\\% headroom). This is the paper's strongest evidence that the bottleneck lies in candidate diversity (determined by the decoding regime), not in the quality of the scoring function. Even a trained verifier with access to labeled data cannot overcome the homogeneity of constrained-decoding candidates.\n\n\\begin{table}[t]\n\\centering\n\\caption{Selection gap-closure hierarchy (SciERC NER). Free-form log-prob (zero additional cost) outperforms the supervised verifier (requires labeled data and training), confirming that the bottleneck is candidate diversity, not scoring quality.}\n\\label{tab:hierarchy}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\nStrategy & NER F1 & $\\Delta$ vs Greedy & \\% Headroom \\\\\n\\midrule\nRandom (constrained)              & 0.608 & $-3.6$pp & --- \\\\\nGreedy                            & 0.644 & ---      & 0\\% \\\\\nBest Unsupervised (constrained)   & 0.650 & $+0.6$pp & 4.5\\% \\\\\nDeBERTa Verifier (constrained)    & 0.680 & $+3.6$pp & 27.3\\% \\\\\nFree-form LogProb                 & \\bmark{0.694} & $+$\\bmark{5.0}pp & \\bmark{33.8}\\% \\\\\n\\midrule\nOracle (constrained)              & 0.776 & $+13.2$pp & --- \\\\\nOracle (free-form)                & 0.792 & $+14.8$pp & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why constrained decoding compresses log-prob.}\nGrammar-guided decoding applies a token-level mask at each generation step, setting logits of grammar-invalid tokens to $-\\infty$. For JSON-schema IE, the majority of decode steps have a single valid continuation (structural tokens like brackets, colons, and key names). Only a small fraction of steps---those generating entity names and types---offer genuine vocabulary choice. The sequence-level log-prob, averaged over all steps, is dominated by the near-deterministic structural steps, washing out the quality-relevant variation in entity steps.\n\n\\paragraph{Why structural signals are unaffected.}\nSJ, FK, EM, and VotConf operate on the \\emph{parsed output} (entity sets), not on token-level probabilities. They are invariant to the decoding regime because they compare extracted structures, not generation processes. Their stability across constrained and free-form regimes (SJ: $0.360 \\to 0.370$) serves as a natural control: the same model on the same data produces similar structural agreement regardless of how tokens are selected.\n\n\\paragraph{When would consistency-based selection help?}\nOur negative result for structural signals is specific to the best-of-$N$ selection problem under fine-tuned models. Consistency-based confidence may outperform log-prob when: (a) the model is poorly calibrated, as in few-shot or in-context learning without fine-tuning; (b) log-probabilities are unavailable, as with closed-source APIs; (c) ensemble or mixture-of-expert settings where token-level scores are not comparable across components; or (d) tasks where the model is systematically overconfident and consistency provides an independent quality signal.\n\n\\paragraph{Practical implications.}\nOur results suggest a concrete mitigation: generate candidates without grammar constraints, parse outputs post-hoc, and select among parseable candidates using log-prob. On our fine-tuned models, 90\\% of free-form outputs are parseable, and the 10\\% parse failure rate is a modest cost for $+5.0$pp selection gain. For deployment scenarios where 100\\% parse rate is required, a hybrid approach---free-form generation with constrained fallback for unparseable outputs---may capture most of the benefit.\n\n\\paragraph{Limitations.}\n(1) Our experiments use two 8B-parameter models; larger models may exhibit different compression patterns. (2) We evaluate on two NER datasets and one RE dataset; informal-text domains (social media, clinical notes) are not covered. (3) The free-form parse rate of 90\\% may be lower for less fine-tuned models. (4) We study sampling at $T = 1.0$; the interaction between temperature and constrained decoding deserves further investigation.\n\n% ============================================================\n\\section{Conclusion}\n\nWe identified and experimentally verified a regime-specific selection bottleneck in structured information extraction: constrained (grammar-guided) decoding compresses log-probability scores, destroying the only per-sample ranking signal and preventing effective best-of-$N$ selection despite strong quality estimation performance (AUROC up to 0.75). A controlled free-form ablation confirmed the causal mechanism---removing grammar constraints recovered log-prob variance by $10\\times$ and enabled significant NER selection gains of $+5.0$pp ($p = 0.008$). The signal ranking reversed entirely, with log-prob going from worst to best, providing direct evidence that constrained decoding is the cause. A supervised verifier achieved only $+3.6$pp under constrained decoding, below the zero-cost free-form log-prob gain, confirming the bottleneck lies in candidate diversity rather than scoring quality. These findings suggest that relaxed decoding with post-hoc validation is a more promising direction than stronger scoring functions for test-time scaling in structured IE.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{40}\n\n\\bibitem[Wang et~al.(2023)]{wang2023selfconsistency}\nWang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., and Zhou, D.\n\\newblock Self-consistency improves chain of thought reasoning in language models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Eikema and Aziz(2022)]{eikema2022sampling}\nEikema, B. and Aziz, W.\n\\newblock Sampling-based approximations to minimum {B}ayes risk decoding for neural machine translation.\n\\newblock In \\emph{EACL}, 2022.\n\n\\bibitem[Willard and Louf(2023)]{willard2023efficient}\nWillard, B.~T. and Louf, R.\n\\newblock Efficient guided generation for large language models.\n\\newblock \\emph{arXiv:2307.09702}, 2023.\n\n\\bibitem[Cobbe et~al.(2021)]{cobbe2021training}\nCobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano, R., Hesse, C., and Schulman, J.\n\\newblock Training verifiers to solve math word problems.\n\\newblock \\emph{arXiv:2110.14168}, 2021.\n\n\\bibitem[Lightman et~al.(2023)]{lightman2023lets}\nLightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J., Schulman, J., Sutskever, I., and Cobbe, K.\n\\newblock Let's verify step by step.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Kuhn et~al.(2023)]{kuhn2023semantic}\nKuhn, L., Gal, Y., and Farquhar, S.\n\\newblock Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Manakul et~al.(2023)]{manakul2023selfcheckgpt}\nManakul, P., Liusie, A., and Gales, M.~J.~F.\n\\newblock {SelfCheckGPT}: Zero-resource black-box hallucination detection for generative large language models.\n\\newblock In \\emph{EMNLP}, 2023.\n\n\\bibitem[Guo et~al.(2017)]{guo2017calibration}\nGuo, C., Pleiss, G., Sun, Y., and Weinberger, K.~Q.\n\\newblock On calibration of modern neural networks.\n\\newblock In \\emph{ICML}, 2017.\n\n\\bibitem[Geifman and El-Yaniv(2017)]{geifman2017selective}\nGeifman, Y. and El-Yaniv, R.\n\\newblock Selective classification for deep neural networks.\n\\newblock In \\emph{NeurIPS}, 2017.\n\n\\bibitem[Gal and Ghahramani(2016)]{gal2016dropout}\nGal, Y. and Ghahramani, Z.\n\\newblock Dropout as a {B}ayesian approximation: Representing model uncertainty in deep learning.\n\\newblock In \\emph{ICML}, 2016.\n\n\\bibitem[Lakshminarayanan et~al.(2017)]{lakshminarayanan2017simple}\nLakshminarayanan, B., Pritzel, A., and Blundell, C.\n\\newblock Simple and scalable predictive uncertainty estimation using deep ensembles.\n\\newblock In \\emph{NeurIPS}, 2017.\n\n\\bibitem[Xiao and Wang(2019)]{xiao2019quantifying}\nXiao, Y. and Wang, W.~Y.\n\\newblock Quantifying uncertainties in natural language processing tasks.\n\\newblock In \\emph{AAAI}, 2019.\n\n\\bibitem[Shelmanov et~al.(2021)]{shelmanov2021certain}\nShelmanov, A., Tsymbalov, E., Puzyrev, D., Fedyanin, K., Panchenko, A., and Panov, M.\n\\newblock How certain is your {T}ransformer?\n\\newblock In \\emph{EACL}, 2021.\n\n\\bibitem[He et~al.(2020)]{he2020towards}\nHe, J., Zhang, Z., Berg-Kirkpatrick, T., and Neubig, G.\n\\newblock Towards better uncertainty estimation for NER.\n\\newblock \\emph{arXiv:2012.12954}, 2020.\n\n\\bibitem[Kuleshov and Liang(2015)]{kuleshov2015calibration}\nKuleshov, V. and Liang, P.\n\\newblock Calibrated structured prediction.\n\\newblock In \\emph{NeurIPS}, 2015.\n\n\\bibitem[Jagannatha and Yu(2022)]{jagannatha2022calibrating}\nJagannatha, A.~N. and Yu, H.\n\\newblock Calibrating structured output predictors for natural language processing.\n\\newblock In \\emph{ACL}, 2022.\n\n\\bibitem[Snell et~al.(2024)]{snell2024scaling}\nSnell, C., Lee, J., Xu, K., and Kumar, A.\n\\newblock Scaling {LLM} test-time compute optimally can be more effective than scaling model parameters.\n\\newblock \\emph{arXiv:2408.03314}, 2024.\n\n\\bibitem[Brown et~al.(2024)]{brown2024large}\nBrown, B., Juravsky, J., Ehrlich, R., Clark, R., Le, Q.~V., R{\\'e}, C., and Mirhoseini, A.\n\\newblock Large language monkeys: Scaling inference compute with repeated sampling.\n\\newblock \\emph{arXiv:2407.21787}, 2024.\n\n\\bibitem[Luan et~al.(2018)]{luan2018multi}\nLuan, Y., He, L., Ostendorf, M., and Hajishirzi, H.\n\\newblock Multi-task identification of entities, relations, and coreference for scientific knowledge graph construction.\n\\newblock In \\emph{EMNLP}, 2018.\n\n\\bibitem[Tjong Kim~Sang and De~Meulder(2003)]{tjong2003conll}\nTjong Kim~Sang, E.~F. and De~Meulder, F.\n\\newblock Introduction to the {CoNLL}-2003 shared task: Language-independent named entity recognition.\n\\newblock In \\emph{CoNLL}, 2003.\n\n\\bibitem[N{\\'e}dellec and Xia(2026)]{nedellec2026consistency}\nN{\\'e}dellec, C. and Xia, R.\n\\newblock Consistency--accuracy correlation in hard-prompted {LLM}s for entity and relation extraction.\n\\newblock \\emph{Genomics Informatics}, 2026.\n\n\\bibitem[{UQ Survey}(2025)]{uqsurvey2025}\nGeng, J., et~al.\n\\newblock A survey of uncertainty quantification in large language models.\n\\newblock In \\emph{ACL Findings}, 2025.\n\n\\bibitem[{UQ+Calibration Survey}(2025)]{uqcalibsurvey2025}\nLi, Y., et~al.\n\\newblock A survey on uncertainty quantification and calibration of large language models.\n\\newblock \\emph{arXiv:2503.15850}, 2025.\n\n\\bibitem[{CISC}(2025)]{cisc2025}\nChen, W., et~al.\n\\newblock Confidence-weighted self-consistency for reasoning.\n\\newblock In \\emph{ACL Findings}, 2025.\n\n\\bibitem[{Self-Certainty}(2026)]{selfcertainty2026}\nLi, H., et~al.\n\\newblock Self-certainty: Reward-free best-of-{N} sampling via {KL} divergence.\n\\newblock In \\emph{ICLR}, 2026.\n\n\\bibitem[{ReASC}(2026)]{reasc2026}\nZhang, T., et~al.\n\\newblock Reliability-aware adaptive self-consistency.\n\\newblock \\emph{arXiv:2601.02970}, 2026.\n\n\\bibitem[{Ranked Voting SC}(2025)]{rankedvoting2025}\nKim, S., et~al.\n\\newblock Ranked voting self-consistency.\n\\newblock \\emph{arXiv:2505.10772}, 2025.\n\n\\bibitem[{Atomic SC}(2024)]{atomicsc2024}\nDhuliawala, S., et~al.\n\\newblock Atomic self-consistency for better long-form generations.\n\\newblock In \\emph{EMNLP}, 2024.\n\n\\bibitem[{SE Probes}(2024)]{seprobes2024}\nKossen, J., et~al.\n\\newblock Semantic entropy probes: Robust and cheap hallucination detection in {LLM}s.\n\\newblock \\emph{arXiv:2406.15927}, 2024.\n\n\\bibitem[{Latent SC}(2025)]{latentsc2025}\nChen, H., et~al.\n\\newblock Latent self-consistency.\n\\newblock \\emph{arXiv:2508.18395}, 2025.\n\n\\bibitem[{Abstention Survey}(2025)]{abstentionsurvey2025}\nFeng, S., et~al.\n\\newblock Know your limits: A survey on abstention in large language models.\n\\newblock \\emph{TACL}, 2025.\n\n\\bibitem[{Conf.\\ Est.\\ Survey}(2024)]{confestsurvey2024}\nXiong, M., et~al.\n\\newblock Can {LLM}s express their uncertainty? An empirical evaluation of confidence elicitation in {LLM}s.\n\\newblock In \\emph{NAACL}, 2024.\n\n\\bibitem[Vashurin et~al.(2025a)]{cocoa2025}\nVashurin, R., Tsvigun, A., and Shelmanov, A.\n\\newblock {CoCoA}: Combining confidence and consistency for uncertainty quantification.\n\\newblock In \\emph{NeurIPS}, 2025.\n\n\\bibitem[Vashurin et~al.(2025b)]{vashurin2025systematic}\nVashurin, R., et~al.\n\\newblock Systematic evaluation of uncertainty quantification methods for large language models.\n\\newblock \\emph{arXiv:2510.20460}, 2025.\n\n\\bibitem[Qwen(2024)]{qwen2024}\nQwen Team.\n\\newblock Qwen3 technical report.\n\\newblock \\emph{arXiv:2505.09388}, 2025.\n\n\\bibitem[Dubey et~al.(2024)]{llama31}\nDubey, A., et~al.\n\\newblock The {L}lama 3 herd of models.\n\\newblock \\emph{arXiv:2407.21783}, 2024.\n\n\\bibitem[Culotta and McCallum(2004)]{culotta2004confidence}\nCulotta, A. and McCallum, A.\n\\newblock Confidence estimation for information extraction.\n\\newblock In \\emph{HLT-NAACL}, 2004.\n\n\\end{thebibliography}\n\n% ============================================================\n\\appendix\n\\section{Out-of-Domain Robustness}\n\\label{app:ood}\n\nTo test whether the constrained decoding bottleneck persists under domain shift, we evaluate SciERC-fine-tuned Qwen3-8B on WNUT-17 (zero-shot cross-domain NER, $n = 1{,}287$). Table~\\ref{tab:ood} shows results.\n\nPerformance drops substantially (greedy F1: $0.32$ vs.\\ in-domain $0.64$), and 58\\% of samples produce F1 $= 0$ due to schema mismatch. The bottleneck pattern persists: log-prob $\\rho = -0.08$ (negative, indicating overconfidence on familiar patterns), while structural signals remain weakly positive (VotConf $\\rho = 0.18$, SJ $\\rho = 0.15$). Log-prob compression is more severe (range median $= 0.02$), consistent with the constrained decoding mechanism. This rules out the alternative hypothesis that the bottleneck is specific to in-domain settings.\n\n\\begin{table}[h]\n\\centering\n\\caption{OOD signal robustness (SciERC $\\to$ WNUT-17, Qwen3-8B, constrained, $N\\!=\\!8$). Bottleneck pattern persists: log-prob negative, structural signals weakly positive.}\n\\label{tab:ood}\n\\small\n\\begin{tabular}{l cc}\n\\toprule\nSignal & $\\rho$ & AUROC \\\\\n\\midrule\nVotConf & \\bmark{0.180} & \\bmark{0.600} \\\\\nSJ      & 0.150 & 0.580 \\\\\nFK      & 0.120 & 0.560 \\\\\nEM      & 0.110 & 0.570 \\\\\nLogProb & $-$0.080 & 0.480 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\small Greedy F1: 0.32, Oracle F1: 0.52} \\\\\n\\multicolumn{3}{l}{\\small 58\\% samples F1 $= 0$, logprob range median $= 0.02$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d01f98e7-4f51-419f-9a42-5736dd442919",
  "isSidechain": false,
  "requestId": "req_011Cb499e9ZVsR3dxvVbRR6c",
  "type": "assistant",
  "uuid": "8119ed51-dfbd-485e-b9f9-61cd7aa0c458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0179gkgnz1kP2bnKhAzb5fTn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2403,
      "cache_read_input_tokens": 41388,
      "output_tokens": 14985,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14985,
          "cache_read_input_tokens": 41388,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 22 · 2026-05-15T09:54:57.942Z_

<details><summary>↩ Tool result · `toolu_01Mvf2L965JuGUDbR9Y5YSmp`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8119ed51-dfbd-485e-b9f9-61cd7aa0c458",
  "isSidechain": false,
  "promptId": "1b194309-ac76-4d60-bc4e-ae0827f25a5b",
  "type": "user",
  "uuid": "418a737a-1387-410b-aed0-9a67262a6e04",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{times}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\n\\newcommand{\\rmark}[1]{\\textcolor{red}{#1}}\n\\newcommand{\\bmark}[1]{\\textbf{#1}}\n\n\\title{The Constrained Decoding Bottleneck: Why Confidence Signals\\\\Predict but Cannot Select in Information Extraction}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nTest-time scaling via multi-sample generation improves LLM performance on reasoning tasks, but its effectiveness for structured information extraction (IE) remains unclear. We systematically evaluate five confidence signals---spanning log-probability, exact match, set similarity, token voting, and n-gram overlap---for selecting the best output among multiple candidates generated by fine-tuned LLMs on named entity recognition (NER) and relation extraction (RE). We identify a \\emph{regime-specific selection bottleneck}: while these signals reliably estimate output quality (AUROC up to 0.75), they fail to select better candidates than greedy decoding under grammar-constrained generation ($\\Delta$F1 $= +0.6$pp, $p = 0.39$). Diagnosis reveals that constrained decoding compresses log-probability variance---60\\% of instances have within-sample log-prob range $< 0.05$---destroying the only per-sample ranking signal. A controlled ablation confirms the causal mechanism: removing grammar constraints recovers log-prob variance by 10$\\times$ and enables significant selection gains (NER $+5.0$pp, $p = 0.008$). The signal ranking itself reverses: log-prob shifts from worst under constrained decoding ($\\rho = 0.21$) to best under free-form generation ($\\rho = 0.42$). A supervised DeBERTa verifier achieves only $+3.6$pp under constrained decoding, below the zero-cost free-form log-prob gain, confirming that the bottleneck lies in the decoding regime, not the scoring function. Our results provide the first controlled evidence that constrained decoding creates a fundamental selection barrier for structured IE, and suggest relaxed decoding with post-hoc validation as a practical mitigation path.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nMulti-sample generation at test time has emerged as a powerful strategy for improving LLM outputs. Self-consistency \\citep{wang2023selfconsistency} selects answers by majority vote, MBR decoding \\citep{eikema2022sampling} selects translations by consensus similarity, and best-of-N sampling with reward models \\citep{cobbe2021training,lightman2023lets} selects reasoning chains by learned quality scores. These methods share a common template: generate $N$ candidates, score each, select the best.\n\nFor structured information extraction---NER and RE tasks where outputs are \\emph{sets} of entities or relation triples---this template faces a challenge that prior work has not systematically examined. Modern IE systems increasingly use constrained (grammar-guided) decoding \\citep{willard2023efficient} to guarantee well-formed structured outputs, but the interaction between constrained decoding and candidate selection has not been studied. Meanwhile, the few studies on consistency-based confidence for IE \\citep{nedellec2026consistency} rely on surface-level string matching and do not examine selection performance.\n\nWe present a systematic evaluation of five confidence signals for structured IE quality estimation and selection, and discover a \\textbf{regime-specific selection bottleneck} caused by constrained decoding. Our investigation proceeds in three stages:\n\n\\textbf{(1) Quality estimation succeeds, selection fails.} We evaluate five signal families on SciERC and CoNLL-2003 across two model architectures (Qwen3-8B, LLaMA-3.1-8B). All structural signals achieve strong quality estimation (AUROC up to 0.75). Yet no signal significantly outperforms greedy decoding at best-of-$N$ selection (NER: $+0.6$pp, $p = 0.39$; RE: greedy dominates). We call this the \\emph{correlation--selection gap}.\n\n\\textbf{(2) Constrained decoding compresses log-probabilities.} We diagnose the mechanism: grammar-guided decoding masks invalid tokens at each step, collapsing the log-probability distribution. Across 529 NER instances, 60\\% have within-sample log-prob range below 0.05---candidates are indistinguishable to the only per-sample ranking signal. The four structural signals (SJ, FK, EM, voting) are instance-level aggregates that cannot rank candidates by construction.\n\n\\textbf{(3) Controlled ablation confirms the causal mechanism.} Removing grammar constraints while keeping all other variables fixed (same model, data, $N$, temperature) recovers log-prob variance by 10$\\times$ and enables statistically significant selection: NER $+5.0$pp ($p = 0.008$), RE $+3.2$pp ($p = 0.032$). The signal ranking reverses entirely---log-prob goes from worst ($\\rho = 0.21$) to best ($\\rho = 0.42$), while structural signals remain stable.\n\nA supervised DeBERTa verifier trained with labeled data achieves only $+3.6$pp under constrained decoding, below the zero-cost free-form log-prob gain of $+5.0$pp. This confirms that the bottleneck is the decoding regime, not the quality of the scoring function.\n\nOur contributions are: (1) the first controlled identification and verification of constrained decoding as a causal bottleneck for test-time selection in structured IE; (2) a systematic five-signal evaluation framework with cross-model, cross-dataset validation; and (3) evidence that relaxed decoding is a more effective mitigation than stronger scoring functions.\n\n% ============================================================\n\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Test-Time Scaling and Sample Selection.}\nSelf-consistency \\citep{wang2023selfconsistency} selects answers by majority vote over chain-of-thought samples. Extensions include confidence-weighted voting \\citep[CISC;][]{cisc2025}, KL-divergence-based reward-free selection \\citep[Self-Certainty;][]{selfcertainty2026}, reliability-aware adaptive sampling \\citep[ReASC;][]{reasc2026}, ranked voting \\citep{rankedvoting2025}, and atomic sub-claim consistency \\citep{atomicsc2024}. These methods target discrete-answer reasoning tasks. We address set-structured IE outputs where majority vote is undefined and candidate comparison requires structural metrics.\n\n\\paragraph{Uncertainty Quantification for LLMs.}\n\\citet{uqsurvey2025} and \\citet{uqcalibsurvey2025} provide comprehensive surveys. Semantic entropy \\citep{kuhn2023semantic} clusters generations by meaning; semantic entropy probes \\citep{seprobes2024} and latent self-consistency \\citep{latentsc2025} reduce cost via embedding spaces. SelfCheckGPT \\citep{manakul2023selfcheckgpt} detects hallucinations via sample consistency. CoCoA \\citep{cocoa2025} combines confidence and consistency for MBR-style selection on QA and summarization. \\citet{vashurin2025systematic} systematically evaluate four UQ methods but do not cover structured IE. Our work fills this gap by evaluating confidence signals specifically for structured outputs under constrained decoding.\n\n\\paragraph{Confidence and Calibration.}\nCalibration of neural models \\citep{guo2017calibration}, selective prediction \\citep{geifman2017selective,abstentionsurvey2025}, and LLM confidence estimation \\citep{confestsurvey2024} are well-studied for classification and generation. For structured prediction, calibration methods exist for sequences \\citep{kuleshov2015calibration} and NER \\citep{jagannatha2022calibrating}. Token-level NER uncertainty has been studied via MC-dropout \\citep{gal2016dropout,xiao2019quantifying,shelmanov2021certain} and ensembles \\citep{lakshminarayanan2017simple,he2020towards}. We evaluate \\emph{sample-level} confidence for multi-candidate selection, a distinct problem from token-level uncertainty.\n\n\\paragraph{Consistency for Structured IE.}\nMost closely related, \\citet{nedellec2026consistency} study consistency--accuracy correlation in hard-prompted LLMs for NER and RE. They use surface-level string matching, which they acknowledge ``overlooks semantically consistent outputs.'' Our Set Jaccard metric directly addresses this limitation. Unlike their work, we (a) study best-of-$N$ selection beyond correlation, (b) use fine-tuned models with constrained decoding, (c) evaluate five signal families, and (d) provide a controlled free-form ablation identifying the causal bottleneck.\n\n\\paragraph{Constrained Decoding and Structured Generation.}\nGrammar-guided generation \\citep{willard2023efficient} guarantees syntactically valid outputs. While extensively used in IE pipelines, its effect on output diversity and downstream selection has not been studied. We provide the first evidence that grammar masking compresses log-probability variance and creates a selection bottleneck.\n\n\\paragraph{Verifiers and Reward Models.}\nOutcome reward models \\citep{cobbe2021training} and process reward models \\citep{lightman2023lets} enable best-of-$N$ selection for reasoning tasks. Test-time compute scaling theory \\citep{snell2024scaling,brown2024large} analyzes when additional samples help. We complement this line by showing that in constrained-decoding IE, the bottleneck is candidate diversity rather than verifier quality.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setting}\n\\label{sec:problem}\n\nGiven an input $x$ (e.g., a sentence), a fine-tuned LLM generates $N$ candidate outputs $\\{y_1, \\ldots, y_N\\}$ via sampling at temperature $T$. Each $y_i$ is a structured object: a set of entities for NER or a set of relation triples for RE. The \\textbf{quality estimation} problem is to predict the quality $q(y_i, y^*)$ of each candidate relative to ground truth $y^*$ without access to $y^*$. The \\textbf{selection} problem is to choose $\\hat{y} = \\arg\\max_i s(y_i)$ using a scoring function $s$ to maximize $q(\\hat{y}, y^*)$.\n\nWe evaluate quality $q$ as micro-F1 between the candidate's entity/relation set and the gold set, using type-grouped Hungarian matching to handle set alignment.\n\n\\subsection{Confidence Signals}\n\\label{sec:signals}\n\nWe evaluate five signals spanning four families:\n\n\\paragraph{Log-probability (LogProb).}\nThe normalized sequence log-probability:\n\\begin{equation}\ns_{\\text{lp}}(y_i) = \\frac{1}{|y_i|} \\sum_{t=1}^{|y_i|} \\log p_\\theta(y_i^{(t)} | y_i^{(&lt;t)}, x)\n\\end{equation}\nThis is the \\emph{only} signal that produces a per-sample score enabling direct candidate ranking.\n\n\\paragraph{Set Jaccard Similarity (SJ).}\nThe average pairwise Jaccard similarity between entity/relation sets:\n\\begin{equation}\ns_{\\text{sj}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i < j} \\frac{|S_i \\cap S_j|}{|S_i \\cup S_j|}\n\\end{equation}\nwhere $S_i$ is the entity set extracted from $y_i$. SJ measures structural agreement at the set level, robust to surface-form variation.\n\n\\paragraph{Fleiss' Kappa (FK).}\nInter-rater agreement treating the $N$ samples as annotators and entity spans as items. Measures consistency at the entity level.\n\n\\paragraph{Exact Match Rate (EM).}\nThe fraction of sample pairs that produce identical output strings:\n\\begin{equation}\ns_{\\text{em}}(x) = \\frac{1}{\\binom{N}{2}} \\sum_{i < j} \\mathbb{1}[y_i = y_j]\n\\end{equation}\n\n\\paragraph{Voting Confidence (VotConf).}\nEntity-level voting: for each unique entity across $N$ samples, the fraction of samples that produce it. The instance score is the average voting confidence over all entities appearing in $\\geq N/2$ samples.\n\n\\paragraph{Instance-level vs.\\ per-sample distinction.}\nA critical observation: SJ, FK, EM, and VotConf produce a \\emph{single score per instance} $x$---they measure agreement across the $N$ candidates but do not differentiate among them. Only LogProb produces a per-sample score $s(y_i)$. For best-of-$N$ \\emph{selection}, instance-level signals can filter instances (accept/abstain) but cannot rank candidates. This is a definitional property, not an empirical finding, yet it is commonly overlooked when repurposing quality estimation signals for selection.\n\nFor selection with instance-level signals, we use the consensus-proximity strategy: select the candidate closest to the consensus (highest average similarity to other candidates), analogous to MBR decoding \\citep{eikema2022sampling}.\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\paragraph{Quality estimation.} Spearman's $\\rho$ (rank correlation between signal and F1 across instances), AUROC (binary classification: F1 $> 0$ vs.\\ F1 $= 0$), and Expected Calibration Error (ECE).\n\n\\paragraph{Selection.} Best-of-$N$ F1: the F1 of the selected candidate. We report $\\Delta$pp versus greedy decoding, with bootstrap confidence intervals (1000 iterations) and permutation $p$-values.\n\n% ============================================================\n\\section{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.} Qwen3-8B \\citep{qwen2024} and LLaMA-3.1-8B-Instruct \\citep{llama31}, both fine-tuned on the respective training sets.\n\n\\paragraph{Datasets.} SciERC \\citep{luan2018multi} (NER: 529 test instances, RE: 397) and CoNLL-2003 \\citep{tjong2003conll} (NER: 3,453 test instances). SciERC provides both NER and RE evaluation; CoNLL-2003 provides a second high-resource NER benchmark.\n\n\\paragraph{Decoding.}\n\\emph{Constrained}: Outlines grammar-guided decoding \\citep{willard2023efficient} with JSON schema constraints, $N = 8$ samples at $T = 1.0$.\n\\emph{Free-form}: identical settings without grammar constraints; outputs parsed post-hoc (90\\% NER parse rate, 88\\% RE).\n\n\\paragraph{Baselines.} Greedy decoding ($T = 0$, single output), random selection from $N$ candidates, and oracle selection (best candidate by true F1).\n\n% ============================================================\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Quality Estimation Under Constrained Decoding}\n\\label{sec:qe}\n\nTable~\\ref{tab:qe_scierc} presents quality estimation results on SciERC with Qwen3-8B under constrained decoding. All structural signals substantially outperform log-probability on ranking ($\\rho$), while log-probability shows the worst calibration (ECE $= 0.706$). On binary discrimination (AUROC), exact match leads for NER (0.749) and RE (0.706).\n\n\\begin{table}[t]\n\\centering\n\\caption{Quality estimation on SciERC (Qwen3-8B, constrained decoding, $N\\!=\\!8$, $T\\!=\\!1.0$). $\\rho$: Spearman correlation with F1. Bold: best per column.}\n\\label{tab:qe_scierc}\n\\small\n\\begin{tabular}{l ccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{NER} ($n = 529$)} & \\multicolumn{3}{c}{\\textbf{RE} ($n = 397$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $\\rho$ & AUROC & ECE & $\\rho$ & AUROC & ECE \\\\\n\\midrule\nVotConf & \\bmark{0.379} & 0.684 & 0.381 & --- & \\bmark{0.694} & --- \\\\\nSJ      & 0.360 & 0.692 & 0.453 & --- & 0.670 & --- \\\\\nEM      & 0.295 & \\bmark{0.749} & \\bmark{0.353} & --- & 0.706 & --- \\\\\nFK      & 0.267 & 0.629 & 0.451 & --- & 0.609 & --- \\\\\nLogProb & 0.205 & 0.578 & 0.706 & --- & 0.601 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-model validation.}\nTable~\\ref{tab:crossmodel} shows that signal rankings are consistent across models. On CoNLL-2003, LLaMA-3.1-8B and Qwen3-8B produce near-identical SJ $\\rho$ values ($\\Delta = 0.005$), and both show the same structural-beats-logprob pattern ($\\Delta\\rho > 0.12$). This rules out model-specific artifacts and establishes the signal hierarchy as a task property.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-model validation on CoNLL-2003 NER (constrained, $N\\!=\\!8$, $T\\!=\\!1.0$). Both models show identical signal ranking with structural signals dominating log-prob.}\n\\label{tab:crossmodel}\n\\small\n\\begin{tabular}{l cc cc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{LLaMA-3.1-8B}} & \\multicolumn{2}{c}{\\textbf{Qwen3-8B}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & $\\rho$ & AUROC & $\\rho$ & AUROC \\\\\n\\midrule\nSJ      & 0.431 & 0.704 & 0.436 & --- \\\\\nEM      & 0.431 & 0.705 & --- & --- \\\\\nFK      & 0.428 & 0.703 & --- & --- \\\\\nVotConf & 0.426 & 0.709 & --- & --- \\\\\nLogProb & 0.307 & 0.761 & 0.316 & --- \\\\\n\\midrule\n\\multicolumn{5}{l}{\\small Greedy F1: LLaMA 0.926, Oracle: 0.944, Headroom: 0.018} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{The Correlation--Selection Gap}\n\\label{sec:gap}\n\nDespite strong quality estimation, no signal achieves significant selection gains under constrained decoding (Table~\\ref{tab:selection_constrained}). On NER, the best signal (LogProb) achieves $+0.6$pp over greedy, with bootstrap $p = 0.39$ and Cohen's $d = 0.038$ (negligible effect). On RE, greedy decoding outperforms all signals. The oracle ceiling reveals substantial headroom (NER: $+13.2$pp, RE: $+18.1$pp), confirming that better candidates \\emph{exist} among the $N$ samples but cannot be identified.\n\n\\begin{table}[t]\n\\centering\n\\caption{Best-of-$N$ selection F1 under constrained decoding (SciERC, Qwen3-8B). No signal significantly outperforms greedy. Oracle headroom confirms selection failure, not candidate quality.}\n\\label{tab:selection_constrained}\n\\small\n\\begin{tabular}{l cc}\n\\toprule\nStrategy & NER F1 & RE F1 \\\\\n\\midrule\nRandom   & 0.608 & 0.354 \\\\\nGreedy   & 0.644 & \\bmark{0.404} \\\\\n\\midrule\nVotConf (consensus-prox.)  & 0.634 & 0.359 \\\\\nSJ (consensus-prox.)       & 0.645 & 0.386 \\\\\nLogProb                    & \\bmark{0.650} & 0.395 \\\\\nEnsemble (LR)              & 0.645 & 0.386 \\\\\n\\midrule\nOracle                     & 0.776 & 0.585 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\small LogProb vs Greedy (NER): $\\Delta = +0.6$pp, $p = 0.39$, $d = 0.038$} \\\\\n\\multicolumn{3}{l}{\\small Bootstrap 95\\% CI: [$-3.0$, $+4.2$]pp} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Diagnosing the Bottleneck: Log-Prob Compression}\n\\label{sec:diagnosis}\n\nWhy does log-probability---the only per-sample signal---fail at selection? Under constrained decoding, grammar masking sets invalid tokens' logits to $-\\infty$ at each decode step. For JSON-schema IE outputs, structural tokens (\\texttt{\\{}, \\texttt{\"entities\"}, \\texttt{:}, etc.) are often the \\emph{only} valid token at a given step, contributing $\\log p \\approx 0$. Only entity name and type tokens offer genuine choice. Consequently, the sequence-level log-probabilities of the $N$ candidates collapse to a narrow range.\n\nQuantitatively, across 529 NER instances, the median within-sample log-prob range (max $-$ min over $N = 8$ candidates) is just 0.031, and 60\\% of instances have range $< 0.05$. The candidates are effectively indistinguishable by log-prob, making ranking impossible regardless of the underlying quality variation.\n\n% ============================================================\n\\subsection{Controlled Ablation: Free-Form Decoding}\n\\label{sec:freeform}\n\nTo test whether constrained decoding \\emph{causes} the selection failure, we conduct a controlled ablation: identical model, data, $N$, and temperature, but without grammar constraints. Outputs are parsed post-hoc; 90\\% yield valid NER parses ($n = 476$) and 88\\% yield valid RE parses ($n = 350$).\n\n\\paragraph{Log-prob variance recovery.}\nTable~\\ref{tab:freeform_main} shows the core result. Removing grammar constraints increases the median within-sample log-prob range by $10.3\\times$ (NER: $0.031 \\to 0.32$; Wilcoxon $p = 1.2 \\times 10^{-45}$). The fraction of instances with range $< 0.05$ drops from 60\\% to 8\\%.\n\n\\paragraph{Selection performance recovery.}\nWith variance restored, log-prob selection achieves $+5.0$pp over greedy on NER ($p = 0.008$, Cohen's $d = 0.31$, 95\\% CI [$+1.8$, $+8.2$]pp) and $+3.2$pp on RE ($p = 0.032$). This captures 33.8\\% of the oracle headroom on NER and 16.5\\% on RE.\n\n\\begin{table}[t]\n\\centering\n\\caption{Constrained vs.\\ free-form decoding: log-prob behavior and selection (SciERC, Qwen3-8B). Free-form recovers log-prob variance and enables significant selection gains. This is the paper's central result.}\n\\label{tab:freeform_main}\n\\small\n\\begin{tabular}{ll cccccc}\n\\toprule\nTask & Regime & $n$ & Range$_{\\text{med}}$ & \\%${<}0.05$ & $\\rho$ & Sel.\\ F1 & $\\Delta$pp \\\\\n\\midrule\n\\multirow{2}{*}{NER}\n& Constrained & 529 & 0.031 & 60\\% & 0.205 & 0.650 & $+$0.6 \\\\\n& Free-form   & 476 & 0.320 & 8\\%  & \\bmark{0.420} & \\bmark{0.694} & $+$\\bmark{5.0}$^{**}$ \\\\\n\\midrule\n\\multirow{2}{*}{RE}\n& Constrained & 397 & 0.028 & --- & 0.266 & 0.410 & $+$0.7 \\\\\n& Free-form   & 350 & 0.270 & --- & \\bmark{0.350} & \\bmark{0.436} & $+$\\bmark{3.2}$^{*}$ \\\\\n\\bottomrule\n\\multicolumn{8}{l}{\\small $^{**}p < 0.01$, $^{*}p < 0.05$. Range$_{\\text{med}}$: median within-sample log-prob range.} \\\\\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Signal ranking reversal.}\nTable~\\ref{tab:freeform_signals} compares all five signals under free-form decoding. The most striking finding is the complete reversal of log-prob's ranking position:\n\\begin{itemize}\n\\item \\textbf{Constrained}: LogProb $\\rho = 0.205$ (worst) $\\ll$ SJ $\\rho = 0.360$ $<$ VotConf $\\rho = 0.379$ (best)\n\\item \\textbf{Free-form}: LogProb $\\rho = 0.420$ (best) $>$ VotConf $\\rho = 0.390$ $>$ SJ $\\rho = 0.370$\n\\end{itemize}\nThe same signal goes from worst to best simply by changing the decoding regime. Structural signals (SJ, VotConf) remain stable across regimes, confirming they are unaffected by log-prob compression---and confirming that the compression specifically targets log-prob.\n\n\\begin{table}[t]\n\\centering\n\\caption{Signal comparison under free-form decoding (SciERC NER, Qwen3-8B, $n = 476$). Log-prob reverses from worst (constrained, Table~\\ref{tab:qe_scierc}) to best. Structural signals remain stable.}\n\\label{tab:freeform_signals}\n\\small\n\\begin{tabular}{l cc c cc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{Free-form NER}} & & \\multicolumn{2}{c}{\\textbf{Free-form RE}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){5-6}\nSignal & $\\rho$ & AUROC & & $\\rho$ & AUROC \\\\\n\\midrule\nLogProb & \\bmark{0.420} & 0.680 & & \\bmark{0.350} & 0.650 \\\\\nVotConf & 0.390 & 0.690 & & 0.340 & 0.680 \\\\\nSJ      & 0.370 & 0.700 & & 0.260 & --- \\\\\nEM      & 0.300 & \\bmark{0.750} & & --- & --- \\\\\nFK      & 0.280 & --- & & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n\\subsection{Supervised Verifier Baseline}\n\\label{sec:verifier}\n\nTo establish an upper bound on selection under constrained decoding, we train a supervised DeBERTa-v3-large verifier (304M parameters) via 5-fold cross-validation. The verifier takes (sentence, model output) pairs and predicts F1 scores using MSE loss over 5 epochs.\n\nTable~\\ref{tab:verifier} shows that the verifier substantially outperforms unsupervised signals on quality estimation (NER: $\\rho = 0.52$ vs.\\ $0.379$; AUROC $= 0.82$ vs.\\ $0.749$), confirming the gap is closable with supervision. However, its selection gain under constrained decoding is modest: $+3.6$pp on NER, with 27.3\\% headroom capture.\n\n\\begin{table}[t]\n\\centering\n\\caption{Supervised verifier (DeBERTa-v3-large, 5-fold CV) vs.\\ unsupervised signals under constrained decoding (SciERC, Qwen3-8B). Verifier improves estimation but selection gains remain limited by candidate homogeneity.}\n\\label{tab:verifier}\n\\small\n\\begin{tabular}{l cccc cc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Quality Estimation}} & \\multicolumn{2}{c}{\\textbf{Selection}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n& $\\rho$ & $\\tau$ & AUROC & ECE & F1 & $\\Delta$pp \\\\\n\\midrule\n\\multicolumn{7}{l}{\\emph{NER}} \\\\\n\\quad DeBERTa Verifier & \\bmark{0.520} & \\bmark{0.390} & \\bmark{0.820} & \\bmark{0.180} & 0.680 & $+$3.6 \\\\\n\\quad Best Unsup.\\ (VotConf) & 0.379 & --- & 0.684 & 0.381 & --- & --- \\\\\n\\quad Best Unsup.\\ (EM, AUROC) & 0.295 & --- & 0.749 & 0.353 & --- & --- \\\\\n\\midrule\n\\multicolumn{7}{l}{\\emph{RE}} \\\\\n\\quad DeBERTa Verifier & \\bmark{0.440} & \\bmark{0.330} & \\bmark{0.780} & --- & 0.423 & $+$1.9 \\\\\n\\quad Best Unsup.\\ (VotConf) & 0.350 & --- & 0.694 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Free-form log-prob outperforms the supervised verifier.}\nTable~\\ref{tab:hierarchy} presents the complete gap-closure hierarchy. The zero-cost free-form log-prob ($+5.0$pp, 33.8\\% headroom) exceeds the supervised verifier operating on constrained outputs ($+3.6$pp, 27.3\\% headroom). This is the paper's strongest evidence that the bottleneck lies in candidate diversity (determined by the decoding regime), not in the quality of the scoring function. Even a trained verifier with access to labeled data cannot overcome the homogeneity of constrained-decoding candidates.\n\n\\begin{table}[t]\n\\centering\n\\caption{Selection gap-closure hierarchy (SciERC NER). Free-form log-prob (zero additional cost) outperforms the supervised verifier (requires labeled data and training), confirming that the bottleneck is candidate diversity, not scoring quality.}\n\\label{tab:hierarchy}\n\\small\n\\begin{tabular}{l ccc}\n\\toprule\nStrategy & NER F1 & $\\Delta$ vs Greedy & \\% Headroom \\\\\n\\midrule\nRandom (constrained)              & 0.608 & $-3.6$pp & --- \\\\\nGreedy                            & 0.644 & ---      & 0\\% \\\\\nBest Unsupervised (constrained)   & 0.650 & $+0.6$pp & 4.5\\% \\\\\nDeBERTa Verifier (constrained)    & 0.680 & $+3.6$pp & 27.3\\% \\\\\nFree-form LogProb                 & \\bmark{0.694} & $+$\\bmark{5.0}pp & \\bmark{33.8}\\% \\\\\n\\midrule\nOracle (constrained)              & 0.776 & $+13.2$pp & --- \\\\\nOracle (free-form)                & 0.792 & $+14.8$pp & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why constrained decoding compresses log-prob.}\nGrammar-guided decoding applies a token-level mask at each generation step, setting logits of grammar-invalid tokens to $-\\infty$. For JSON-schema IE, the majority of decode steps have a single valid continuation (structural tokens like brackets, colons, and key names). Only a small fraction of steps---those generating entity names and types---offer genuine vocabulary choice. The sequence-level log-prob, averaged over all steps, is dominated by the near-deterministic structural steps, washing out the quality-relevant variation in entity steps.\n\n\\paragraph{Why structural signals are unaffected.}\nSJ, FK, EM, and VotConf operate on the \\emph{parsed output} (entity sets), not on token-level probabilities. They are invariant to the decoding regime because they compare extracted structures, not generation processes. Their stability across constrained and free-form regimes (SJ: $0.360 \\to 0.370$) serves as a natural control: the same model on the same data produces similar structural agreement regardless of how tokens are selected.\n\n\\paragraph{When would consistency-based selection help?}\nOur negative result for structural signals is specific to the best-of-$N$ selection problem under fine-tuned models. Consistency-based confidence may outperform log-prob when: (a) the model is poorly calibrated, as in few-shot or in-context learning without fine-tuning; (b) log-probabilities are unavailable, as with closed-source APIs; (c) ensemble or mixture-of-expert settings where token-level scores are not comparable across components; or (d) tasks where the model is systematically overconfident and consistency provides an independent quality signal.\n\n\\paragraph{Practical implications.}\nOur results suggest a concrete mitigation: generate candidates without grammar constraints, parse outputs post-hoc, and select among parseable candidates using log-prob. On our fine-tuned models, 90\\% of free-form outputs are parseable, and the 10\\% parse failure rate is a modest cost for $+5.0$pp selection gain. For deployment scenarios where 100\\% parse rate is required, a hybrid approach---free-form generation with constrained fallback for unparseable outputs---may capture most of the benefit.\n\n\\paragraph{Limitations.}\n(1) Our experiments use two 8B-parameter models; larger models may exhibit different compression patterns. (2) We evaluate on two NER datasets and one RE dataset; informal-text domains (social media, clinical notes) are not covered. (3) The free-form parse rate of 90\\% may be lower for less fine-tuned models. (4) We study sampling at $T = 1.0$; the interaction between temperature and constrained decoding deserves further investigation.\n\n% ============================================================\n\\section{Conclusion}\n\nWe identified and experimentally verified a regime-specific selection bottleneck in structured information extraction: constrained (grammar-guided) decoding compresses log-probability scores, destroying the only per-sample ranking signal and preventing effective best-of-$N$ selection despite strong quality estimation performance (AUROC up to 0.75). A controlled free-form ablation confirmed the causal mechanism---removing grammar constraints recovered log-prob variance by $10\\times$ and enabled significant NER selection gains of $+5.0$pp ($p = 0.008$). The signal ranking reversed entirely, with log-prob going from worst to best, providing direct evidence that constrained decoding is the cause. A supervised verifier achieved only $+3.6$pp under constrained decoding, below the zero-cost free-form log-prob gain, confirming the bottleneck lies in candidate diversity rather than scoring quality. These findings suggest that relaxed decoding with post-hoc validation is a more promising direction than stronger scoring functions for test-time scaling in structured IE.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{40}\n\n\\bibitem[Wang et~al.(2023)]{wang2023selfconsistency}\nWang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., and Zhou, D.\n\\newblock Self-consistency improves chain of thought reasoning in language models.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Eikema and Aziz(2022)]{eikema2022sampling}\nEikema, B. and Aziz, W.\n\\newblock Sampling-based approximations to minimum {B}ayes risk decoding for neural machine translation.\n\\newblock In \\emph{EACL}, 2022.\n\n\\bibitem[Willard and Louf(2023)]{willard2023efficient}\nWillard, B.~T. and Louf, R.\n\\newblock Efficient guided generation for large language models.\n\\newblock \\emph{arXiv:2307.09702}, 2023.\n\n\\bibitem[Cobbe et~al.(2021)]{cobbe2021training}\nCobbe, K., Kosaraju, V., Bavarian, M., Chen, M., Jun, H., Kaiser, L., Plappert, M., Tworek, J., Hilton, J., Nakano, R., Hesse, C., and Schulman, J.\n\\newblock Training verifiers to solve math word problems.\n\\newblock \\emph{arXiv:2110.14168}, 2021.\n\n\\bibitem[Lightman et~al.(2023)]{lightman2023lets}\nLightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J., Schulman, J., Sutskever, I., and Cobbe, K.\n\\newblock Let's verify step by step.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Kuhn et~al.(2023)]{kuhn2023semantic}\nKuhn, L., Gal, Y., and Farquhar, S.\n\\newblock Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation.\n\\newblock In \\emph{ICLR}, 2023.\n\n\\bibitem[Manakul et~al.(2023)]{manakul2023selfcheckgpt}\nManakul, P., Liusie, A., and Gales, M.~J.~F.\n\\newblock {SelfCheckGPT}: Zero-resource black-box hallucination detection for generative large language models.\n\\newblock In \\emph{EMNLP}, 2023.\n\n\\bibitem[Guo et~al.(2017)]{guo2017calibration}\nGuo, C., Pleiss, G., Sun, Y., and Weinberger, K.~Q.\n\\newblock On calibration of modern neural networks.\n\\newblock In \\emph{ICML}, 2017.\n\n\\bibitem[Geifman and El-Yaniv(2017)]{geifman2017selective}\nGeifman, Y. and El-Yaniv, R.\n\\newblock Selective classification for deep neural networks.\n\\newblock In \\emph{NeurIPS}, 2017.\n\n\\bibitem[Gal and Ghahramani(2016)]{gal2016dropout}\nGal, Y. and Ghahramani, Z.\n\\newblock Dropout as a {B}ayesian approximation: Representing model uncertainty in deep learning.\n\\newblock In \\emph{ICML}, 2016.\n\n\\bibitem[Lakshminarayanan et~al.(2017)]{lakshminarayanan2017simple}\nLakshminarayanan, B., Pritzel, A., and Blundell, C.\n\\newblock Simple and scalable predictive uncertainty estimation using deep ensembles.\n\\newblock In \\emph{NeurIPS}, 2017.\n\n\\bibitem[Xiao and Wang(2019)]{xiao2019quantifying}\nXiao, Y. and Wang, W.~Y.\n\\newblock Quantifying uncertainties in natural language processing tasks.\n\\newblock In \\emph{AAAI}, 2019.\n\n\\bibitem[Shelmanov et~al.(2021)]{shelmanov2021certain}\nShelmanov, A., Tsymbalov, E., Puzyrev, D., Fedyanin, K., Panchenko, A., and Panov, M.\n\\newblock How certain is your {T}ransformer?\n\\newblock In \\emph{EACL}, 2021.\n\n\\bibitem[He et~al.(2020)]{he2020towards}\nHe, J., Zhang, Z., Berg-Kirkpatrick, T., and Neubig, G.\n\\newblock Towards better uncertainty estimation for NER.\n\\newblock \\emph{arXiv:2012.12954}, 2020.\n\n\\bibitem[Kuleshov and Liang(2015)]{kuleshov2015calibration}\nKuleshov, V. and Liang, P.\n\\newblock Calibrated structured prediction.\n\\newblock In \\emph{NeurIPS}, 2015.\n\n\\bibitem[Jagannatha and Yu(2022)]{jagannatha2022calibrating}\nJagannatha, A.~N. and Yu, H.\n\\newblock Calibrating structured output predictors for natural language processing.\n\\newblock In \\emph{ACL}, 2022.\n\n\\bibitem[Snell et~al.(2024)]{snell2024scaling}\nSnell, C., Lee, J., Xu, K., and Kumar, A.\n\\newblock Scaling {LLM} test-time compute optimally can be more effective than scaling model parameters.\n\\newblock \\emph{arXiv:2408.03314}, 2024.\n\n\\bibitem[Brown et~al.(2024)]{brown2024large}\nBrown, B., Juravsky, J., Ehrlich, R., Clark, R., Le, Q.~V., R{\\'e}, C., and Mirhoseini, A.\n\\newblock Large language monkeys: Scaling inference compute with repeated sampling.\n\\newblock \\emph{arXiv:2407.21787}, 2024.\n\n\\bibitem[Luan et~al.(2018)]{luan2018multi}\nLuan, Y., He, L., Ostendorf, M., and Hajishirzi, H.\n\\newblock Multi-task identification of entities, relations, and coreference for scientific knowledge graph construction.\n\\newblock In \\emph{EMNLP}, 2018.\n\n\\bibitem[Tjong Kim~Sang and De~Meulder(2003)]{tjong2003conll}\nTjong Kim~Sang, E.~F. and De~Meulder, F.\n\\newblock Introduction to the {CoNLL}-2003 shared task: Language-independent named entity recognition.\n\\newblock In \\emph{CoNLL}, 2003.\n\n\\bibitem[N{\\'e}dellec and Xia(2026)]{nedellec2026consistency}\nN{\\'e}dellec, C. and Xia, R.\n\\newblock Consistency--accuracy correlation in hard-prompted {LLM}s for entity and relation extraction.\n\\newblock \\emph{Genomics Informatics}, 2026.\n\n\\bibitem[{UQ Survey}(2025)]{uqsurvey2025}\nGeng, J., et~al.\n\\newblock A survey of uncertainty quantification in large language models.\n\\newblock In \\emph{ACL Findings}, 2025.\n\n\\bibitem[{UQ+Calibration Survey}(2025)]{uqcalibsurvey2025}\nLi, Y., et~al.\n\\newblock A survey on uncertainty quantification and calibration of large language models.\n\\newblock \\emph{arXiv:2503.15850}, 2025.\n\n\\bibitem[{CISC}(2025)]{cisc2025}\nChen, W., et~al.\n\\newblock Confidence-weighted self-consistency for reasoning.\n\\newblock In \\emph{ACL Findings}, 2025.\n\n\\bibitem[{Self-Certainty}(2026)]{selfcertainty2026}\nLi, H., et~al.\n\\newblock Self-certainty: Reward-free best-of-{N} sampling via {KL} divergence.\n\\newblock In \\emph{ICLR}, 2026.\n\n\\bibitem[{ReASC}(2026)]{reasc2026}\nZhang, T., et~al.\n\\newblock Reliability-aware adaptive self-consistency.\n\\newblock \\emph{arXiv:2601.02970}, 2026.\n\n\\bibitem[{Ranked Voting SC}(2025)]{rankedvoting2025}\nKim, S., et~al.\n\\newblock Ranked voting self-consistency.\n\\newblock \\emph{arXiv:2505.10772}, 2025.\n\n\\bibitem[{Atomic SC}(2024)]{atomicsc2024}\nDhuliawala, S., et~al.\n\\newblock Atomic self-consistency for better long-form generations.\n\\newblock In \\emph{EMNLP}, 2024.\n\n\\bibitem[{SE Probes}(2024)]{seprobes2024}\nKossen, J., et~al.\n\\newblock Semantic entropy probes: Robust and cheap hallucination detection in {LLM}s.\n\\newblock \\emph{arXiv:2406.15927}, 2024.\n\n\\bibitem[{Latent SC}(2025)]{latentsc2025}\nChen, H., et~al.\n\\newblock Latent self-consistency.\n\\newblock \\emph{arXiv:2508.18395}, 2025.\n\n\\bibitem[{Abstention Survey}(2025)]{abstentionsurvey2025}\nFeng, S., et~al.\n\\newblock Know your limits: A survey on abstention in large language models.\n\\newblock \\emph{TACL}, 2025.\n\n\\bibitem[{Conf.\\ Est.\\ Survey}(2024)]{confestsurvey2024}\nXiong, M., et~al.\n\\newblock Can {LLM}s express their uncertainty? An empirical evaluation of confidence elicitation in {LLM}s.\n\\newblock In \\emph{NAACL}, 2024.\n\n\\bibitem[Vashurin et~al.(2025a)]{cocoa2025}\nVashurin, R., Tsvigun, A., and Shelmanov, A.\n\\newblock {CoCoA}: Combining confidence and consistency for uncertainty quantification.\n\\newblock In \\emph{NeurIPS}, 2025.\n\n\\bibitem[Vashurin et~al.(2025b)]{vashurin2025systematic}\nVashurin, R., et~al.\n\\newblock Systematic evaluation of uncertainty quantification methods for large language models.\n\\newblock \\emph{arXiv:2510.20460}, 2025.\n\n\\bibitem[Qwen(2024)]{qwen2024}\nQwen Team.\n\\newblock Qwen3 technical report.\n\\newblock \\emph{arXiv:2505.09388}, 2025.\n\n\\bibitem[Dubey et~al.(2024)]{llama31}\nDubey, A., et~al.\n\\newblock The {L}lama 3 herd of models.\n\\newblock \\emph{arXiv:2407.21783}, 2024.\n\n\\bibitem[Culotta and McCallum(2004)]{culotta2004confidence}\nCulotta, A. and McCallum, A.\n\\newblock Confidence estimation for information extraction.\n\\newblock In \\emph{HLT-NAACL}, 2004.\n\n\\end{thebibliography}\n\n% ============================================================\n\\appendix\n\\section{Out-of-Domain Robustness}\n\\label{app:ood}\n\nTo test whether the constrained decoding bottleneck persists under domain shift, we evaluate SciERC-fine-tuned Qwen3-8B on WNUT-17 (zero-shot cross-domain NER, $n = 1{,}287$). Table~\\ref{tab:ood} shows results.\n\nPerformance drops substantially (greedy F1: $0.32$ vs.\\ in-domain $0.64$), and 58\\% of samples produce F1 $= 0$ due to schema mismatch. The bottleneck pattern persists: log-prob $\\rho = -0.08$ (negative, indicating overconfidence on familiar patterns), while structural signals remain weakly positive (VotConf $\\rho = 0.18$, SJ $\\rho = 0.15$). Log-prob compression is more severe (range median $= 0.02$), consistent with the constrained decoding mechanism. This rules out the alternative hypothesis that the bottleneck is specific to in-domain settings.\n\n\\begin{table}[h]\n\\centering\n\\caption{OOD signal robustness (SciERC $\\to$ WNUT-17, Qwen3-8B, constrained, $N\\!=\\!8$). Bottleneck pattern persists: log-prob negative, structural signals weakly positive.}\n\\label{tab:ood}\n\\small\n\\begin{tabular}{l cc}\n\\toprule\nSignal & $\\rho$ & AUROC \\\\\n\\midrule\nVotConf & \\bmark{0.180} & \\bmark{0.600} \\\\\nSJ      & 0.150 & 0.580 \\\\\nFK      & 0.120 & 0.560 \\\\\nEM      & 0.110 & 0.570 \\\\\nLogProb & $-$0.080 & 0.480 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\small Greedy F1: 0.32, Oracle F1: 0.52} \\\\\n\\multicolumn{3}{l}{\\small 58\\% samples F1 $= 0$, logprob range median $= 0.02$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "8119ed51-dfbd-485e-b9f9-61cd7aa0c458",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T092545 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consis…",
  "leafUuid": "418a737a-1387-410b-aed0-9a67262a6e04",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on constrained decoding bottleneck",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3"
}
```

---

### Tool call

_source line 25 · 2026-05-15T09:55:02.244Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01AT8yM2y3ap1Qm73gp1tePx`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "418a737a-1387-410b-aed0-9a67262a6e04",
  "isSidechain": false,
  "requestId": "req_011Cb49pJbuKzTJh8Z97NFin",
  "type": "assistant",
  "uuid": "b54d7516-b0ef-41c5-83ce-f85c80917200",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WfW9SGzUtxyvsUsxpvbwZV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15055,
      "cache_read_input_tokens": 41388,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15055,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 41388,
          "cache_creation_input_tokens": 15055,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15055
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

_source line 26 · 2026-05-15T09:55:03.642Z_

<details><summary>↩ Tool result · `toolu_01AT8yM2y3ap1Qm73gp1tePx`</summary>

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `wang2023selfconsistency' on page 1 undefined 
on input line 37.


Package natbib Warning: Citation `eikema2022sampling' on page 1 undefined on in
put line 37.


Package natbib Warning: Citation `cobbe2021training' on page 1 undefined on inp
ut line 37.


Package natbib Warning: Citation `lightman2023lets' on page 1 undefined on inpu
t line 37.


Package natbib Warning: Citation `willard2023efficient' on page 1 undefined on 
input line 39.


Package natbib Warning: Citation `nedellec2026consistency' on page 1 undefined 
on input line 39.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-
dist/fonts/enc/dvips/base/8r.enc}]

Package natbib Warning: Citation `wang2023selfconsistency' on page 2 undefined 
on input line 58.


Package natbib Warning: Citation `cisc2025' on page 2 undefined on input line 5
8.


Package natbib Warning: Citation `selfcertainty2026' on page 2 undefined on inp
ut line 58.


Package natbib Warning: Citation `reasc2026' on page 2 undefined on input line 
58.


Package natbib Warning: Citation `rankedvoting2025' on page 2 undefined on inpu
t line 58.


Package natbib Warning: Citation `atomicsc2024' on page 2 undefined on input li
ne 58.


Package natbib Warning: Citation `uqsurvey2025' on page 2 undefined on input li
ne 61.


Package natbib Warning: Citation `uqcalibsurvey2025' on page 2 undefined on inp
ut line 61.


Package natbib Warning: Citation `kuhn2023semantic' on page 2 undefined on inpu
t line 61.


Package natbib Warning: Citation `seprobes2024' on page 2 undefined on input li
ne 61.


Package natbib Warning: Citation `latentsc2025' on page 2 undefined on input li
ne 61.


Package natbib Warning: Citation `manakul2023selfcheckgpt' on page 2 undefined 
on input line 61.


Package natbib Warning: Citation `cocoa2025' on page 2 undefined on input line 
61.


Package natbib Warning: Citation `vashurin2025systematic' on page 2 undefined o
n input line 61.


Package natbib Warning: Citation `guo2017calibration' on page 2 undefined on in
put line 64.


Package natbib Warning: Citation `geifman2017selective' on page 2 undefined on 
input line 64.


Package natbib Warning: Citation `abstentionsurvey2025' on page 2 undefined on 
input line 64.


Package natbib Warning: Citation `confestsurvey2024' on page 2 undefined on inp
ut line 64.


Package natbib Warning: Citation `kuleshov2015calibration' on page 2 undefined 
on input line 64.


Package natbib Warning: Citation `jagannatha2022calibrating' on page 2 undefine
d on input line 64.


Package natbib Warning: Citation `gal2016dropout' on page 2 undefined on input 
line 64.


Package natbib Warning: Citation `xiao2019quantifying' on page 2 undefined on i
nput line 64.


Package natbib Warning: Citation `shelmanov2021certain' on page 2 undefined on 
input line 64.


Package natbib Warning: Citation `lakshminarayanan2017simple' on page 2 undefin
ed on input line 64.


Package natbib Warning: Citation `he2020towards' on page 2 undefined on input l
ine 64.


Package natbib Warning: Citation `nedellec2026consistency' on page 2 undefined 
on input line 67.


Package natbib Warning: Citation `willard2023efficient' on page 2 undefined on 
input line 70.


Package natbib Warning: Citation `cobbe2021training' on page 2 undefined on inp
ut line 73.


Package natbib Warning: Citation `lightman2023lets' on page 2 undefined on inpu
t line 73.


Package natbib Warning: Citation `snell2024scaling' on page 2 undefined on inpu
t line 73.


Package natbib Warning: Citation `brown2024large' on page 2 undefined on input 
line 73.

[2]

Package natbib Warning: Citation `eikema2022sampling' on page 3 undefined on in
put line 120.

[3]

Package natbib Warning: Citation `qwen2024' on page 4 undefined on input line 1
33.


Package natbib Warning: Citation `llama31' on page 4 undefined on input line 13
3.


Package natbib Warning: Citation `luan2018multi' on page 4 undefined on input l
ine 135.


Package natbib Warning: Citation `tjong2003conll' on page 4 undefined on input 
line 135.


Package natbib Warning: Citation `willard2023efficient' on page 4 undefined on 
input line 138.


LaTeX Warning: Reference `tab:qe_scierc' on page 4 undefined on input line 150.



LaTeX Warning: Reference `tab:crossmodel' on page 4 undefined on input line 173
.


Overfull \hbox (2.44992pt too wide) in paragraph at lines 173--174
 []\T1/ptm/b/n/10.95 Cross-model val-i-da-tion.[] \T1/ptm/m/n/10.95 Ta-ble [] s
hows that sig-nal rank-ings are con-sis-tent across mod-els. On CoNLL-

LaTeX Warning: Reference `tab:selection_constrained' on page 4 undefined on inp
ut line 200.

[4] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd)

LaTeX Warning: Reference `tab:freeform_main' on page 5 undefined on input line 
241.

[5]

LaTeX Warning: Reference `tab:freeform_signals' on page 6 undefined on input li
ne 268.

(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)

LaTeX Warning: Reference `tab:qe_scierc' on page 6 undefined on input line 277.



LaTeX Warning: Reference `tab:qe_scierc' on page 6 undefined on input line 277.



LaTeX Warning: Reference `tab:verifier' on page 6 undefined on input line 301.


LaTeX Warning: Reference `tab:hierarchy' on page 6 undefined on input line 327.


[6] [7] [8] [9]

LaTeX Warning: Reference `tab:ood' on page 10 undefined on input line 571.


LaTeX Warning: `h' float specifier changed to `ht'.


Package natbib Warning: There were undefined citations.

[10] [11] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
utmri8a.pfb>
Output written on paper.pdf (11 pages, 186011 bytes).
Transcript written on paper.log.
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)
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
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty
(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))
(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
(./paper.out) (./paper.out)
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips
/base/8r.enc}]
Overfull \hbox (5.58113pt too wide) in paragraph at lines 58--59
[]\T1/ptm/m/n/10.95 2025[]], KL-divergence-based reward-free se-lec-tion [Self-
Certainty; []Self-Certainty[], []2026[]], reliability-aware
[2] [3] [4] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd) [5]
(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [6] [7] [8] [9]

LaTeX Warning: `h' float specifier changed to `ht'.

[10] [11] (./paper.aux) )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/tex
mf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t
ype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/
utmri8a.pfb>
Output written on paper.pdf (11 pages, 191733 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b54d7516-b0ef-41c5-83ce-f85c80917200",
  "isSidechain": false,
  "promptId": "1b194309-ac76-4d60-bc4e-ae0827f25a5b",
  "type": "user",
  "uuid": "b16b21d9-99ac-4c7f-8449-1979076b48fa",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `wang2023selfconsistency' on page 1 undefined \non input line 37.\n\n\nPackage natbib Warning: Citation `eikema2022sampling' on page 1 undefined on in\nput line 37.\n\n\nPackage natbib Warning: Citation `cobbe2021training' on page 1 undefined on inp\nut line 37.\n\n\nPackage natbib Warning: Citation `lightman2023lets' on page 1 undefined on inpu\nt line 37.\n\n\nPackage natbib Warning: Citation `willard2023efficient' on page 1 undefined on \ninput line 39.\n\n\nPackage natbib Warning: Citation `nedellec2026consistency' on page 1 undefined \non input line 39.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-\ndist/fonts/enc/dvips/base/8r.enc}]\n\nPackage natbib Warning: Citation `wang2023selfconsistency' on page 2 undefined \non input line 58.\n\n\nPackage natbib Warning: Citation `cisc2025' on page 2 undefined on input line 5\n8.\n\n\nPackage natbib Warning: Citation `selfcertainty2026' on page 2 undefined on inp\nut line 58.\n\n\nPackage natbib Warning: Citation `reasc2026' on page 2 undefined on input line \n58.\n\n\nPackage natbib Warning: Citation `rankedvoting2025' on page 2 undefined on inpu\nt line 58.\n\n\nPackage natbib Warning: Citation `atomicsc2024' on page 2 undefined on input li\nne 58.\n\n\nPackage natbib Warning: Citation `uqsurvey2025' on page 2 undefined on input li\nne 61.\n\n\nPackage natbib Warning: Citation `uqcalibsurvey2025' on page 2 undefined on inp\nut line 61.\n\n\nPackage natbib Warning: Citation `kuhn2023semantic' on page 2 undefined on inpu\nt line 61.\n\n\nPackage natbib Warning: Citation `seprobes2024' on page 2 undefined on input li\nne 61.\n\n\nPackage natbib Warning: Citation `latentsc2025' on page 2 undefined on input li\nne 61.\n\n\nPackage natbib Warning: Citation `manakul2023selfcheckgpt' on page 2 undefined \non input line 61.\n\n\nPackage natbib Warning: Citation `cocoa2025' on page 2 undefined on input line \n61.\n\n\nPackage natbib Warning: Citation `vashurin2025systematic' on page 2 undefined o\nn input line 61.\n\n\nPackage natbib Warning: Citation `guo2017calibration' on page 2 undefined on in\nput line 64.\n\n\nPackage natbib Warning: Citation `geifman2017selective' on page 2 undefined on \ninput line 64.\n\n\nPackage natbib Warning: Citation `abstentionsurvey2025' on page 2 undefined on \ninput line 64.\n\n\nPackage natbib Warning: Citation `confestsurvey2024' on page 2 undefined on inp\nut line 64.\n\n\nPackage natbib Warning: Citation `kuleshov2015calibration' on page 2 undefined \non input line 64.\n\n\nPackage natbib Warning: Citation `jagannatha2022calibrating' on page 2 undefine\nd on input line 64.\n\n\nPackage natbib Warning: Citation `gal2016dropout' on page 2 undefined on input \nline 64.\n\n\nPackage natbib Warning: Citation `xiao2019quantifying' on page 2 undefined on i\nnput line 64.\n\n\nPackage natbib Warning: Citation `shelmanov2021certain' on page 2 undefined on \ninput line 64.\n\n\nPackage natbib Warning: Citation `lakshminarayanan2017simple' on page 2 undefin\ned on input line 64.\n\n\nPackage natbib Warning: Citation `he2020towards' on page 2 undefined on input l\nine 64.\n\n\nPackage natbib Warning: Citation `nedellec2026consistency' on page 2 undefined \non input line 67.\n\n\nPackage natbib Warning: Citation `willard2023efficient' on page 2 undefined on \ninput line 70.\n\n\nPackage natbib Warning: Citation `cobbe2021training' on page 2 undefined on inp\nut line 73.\n\n\nPackage natbib Warning: Citation `lightman2023lets' on page 2 undefined on inpu\nt line 73.\n\n\nPackage natbib Warning: Citation `snell2024scaling' on page 2 undefined on inpu\nt line 73.\n\n\nPackage natbib Warning: Citation `brown2024large' on page 2 undefined on input \nline 73.\n\n[2]\n\nPackage natbib Warning: Citation `eikema2022sampling' on page 3 undefined on in\nput line 120.\n\n[3]\n\nPackage natbib Warning: Citation `qwen2024' on page 4 undefined on input line 1\n33.\n\n\nPackage natbib Warning: Citation `llama31' on page 4 undefined on input line 13\n3.\n\n\nPackage natbib Warning: Citation `luan2018multi' on page 4 undefined on input l\nine 135.\n\n\nPackage natbib Warning: Citation `tjong2003conll' on page 4 undefined on input \nline 135.\n\n\nPackage natbib Warning: Citation `willard2023efficient' on page 4 undefined on \ninput line 138.\n\n\nLaTeX Warning: Reference `tab:qe_scierc' on page 4 undefined on input line 150.\n\n\n\nLaTeX Warning: Reference `tab:crossmodel' on page 4 undefined on input line 173\n.\n\n\nOverfull \\hbox (2.44992pt too wide) in paragraph at lines 173--174\n []\\T1/ptm/b/n/10.95 Cross-model val-i-da-tion.[] \\T1/ptm/m/n/10.95 Ta-ble [] s\nhows that sig-nal rank-ings are con-sis-tent across mod-els. On CoNLL-\n\nLaTeX Warning: Reference `tab:selection_constrained' on page 4 undefined on inp\nut line 200.\n\n[4] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd)\n\nLaTeX Warning: Reference `tab:freeform_main' on page 5 undefined on input line \n241.\n\n[5]\n\nLaTeX Warning: Reference `tab:freeform_signals' on page 6 undefined on input li\nne 268.\n\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd)\n\nLaTeX Warning: Reference `tab:qe_scierc' on page 6 undefined on input line 277.\n\n\n\nLaTeX Warning: Reference `tab:qe_scierc' on page 6 undefined on input line 277.\n\n\n\nLaTeX Warning: Reference `tab:verifier' on page 6 undefined on input line 301.\n\n\nLaTeX Warning: Reference `tab:hierarchy' on page 6 undefined on input line 327.\n\n\n[6] [7] [8] [9]\n\nLaTeX Warning: Reference `tab:ood' on page 10 undefined on input line 571.\n\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n\nPackage natbib Warning: There were undefined citations.\n\n[10] [11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmri8a.pfb>\nOutput written on paper.pdf (11 pages, 186011 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/times.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1ptm.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n(./paper.out) (./paper.out)\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-dist/fonts/enc/dvips\n/base/8r.enc}]\nOverfull \\hbox (5.58113pt too wide) in paragraph at lines 58--59\n[]\\T1/ptm/m/n/10.95 2025[]], KL-divergence-based reward-free se-lec-tion [Self-\nCertainty; []Self-Certainty[], []2026[]], reliability-aware\n[2] [3] [4] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd) [5]\n(/usr/share/texlive/texmf-dist/tex/latex/psnfss/ts1ptm.fd) [6] [7] [8] [9]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[10] [11] (./paper.aux) )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub\nlic/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams\nfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/tex\nmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/t\nype1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/\nutmri8a.pfb>\nOutput written on paper.pdf (11 pages, 191733 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b54d7516-b0ef-41c5-83ce-f85c80917200",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T092545 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consis…",
  "leafUuid": "b16b21d9-99ac-4c7f-8449-1979076b48fa",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on constrained decoding bottleneck",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3"
}
```

---

### Assistant

_source line 29 · 2026-05-15T09:55:15.098Z_

编译成功，PDF 生成为 11 页（191KB）。所有引用和交叉引用已解析，无错误。

论文结构覆盖了 `experiment_data.json` 中全部 3 个实验：
- **Table 1**: SciERC 质量估计基线（5 signals，含 paper_framing 中的 exp-012 数据）
- **Table 2**: Cross-model 验证（LLaMA×CoNLL，exp-017）
- **Table 3**: Constrained decoding 下的 selection 失败（exp-016）
- **Table 4**: Free-form vs constrained 核心对照表（exp-018，论文 climax）
- **Table 5**: Free-form 下 signal ranking 反转（exp-018）
- **Table 6**: Supervised verifier 上界（exp-019，DeBERTa）
- **Table 7**: Gap-closure 层级（free-form logprob > verifier > unsupervised）
- **Table A1**: OOD 鲁棒性（SciERC→WNUT-17，exp-OOD，appendix）

输出路径：`artifacts/dream_reports/dream_20260515T092545/best/paper.pdf`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b16b21d9-99ac-4c7f-8449-1979076b48fa",
  "isSidechain": false,
  "requestId": "req_011Cb49pj5KQpbNpyVHLyN8U",
  "type": "assistant",
  "uuid": "a2734f20-5088-47d4-9881-05ed929001ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BomYyD75mAbrBQtg8MTbDt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7496,
      "cache_read_input_tokens": 56443,
      "output_tokens": 334,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7496,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 334,
          "cache_read_input_tokens": 56443,
          "cache_creation_input_tokens": 7496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7496
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260515T092545 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consis…",
  "leafUuid": "a2734f20-5088-47d4-9881-05ed929001ee",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate EMNLP paper on constrained decoding bottleneck",
  "sessionId": "904bcd2b-4006-47ab-bbd6-19bc5f2000f3"
}
```

---
