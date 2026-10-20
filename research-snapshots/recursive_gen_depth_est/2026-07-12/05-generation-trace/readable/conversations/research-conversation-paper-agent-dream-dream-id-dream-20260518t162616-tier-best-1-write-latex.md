# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162616 tier=best 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/0499f6b9-3e8b-4fbf-b60c-304da272439c.jsonl`
- **Structured JSON:** [`6e8eb3813685da2d9715.json`](../../sessions/6e/6e8eb3813685da2d9715.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T16:42:16.054Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T16:42:16.054Z",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162616 tier=best 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table\n7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：best档叙事：14B Qwen2.5-14B FP16 完整验证 depth signal 在主流规模上的持续性， 消除\"small model only\"质疑。理论section从 Shumailov tail erosion + Dohmatob contraction rate 推导出 EDD 上界=4±1，与三模型实证 EDD=4 精确吻合，将 Atlas 从 empirical observation 升级为 theoretically grounded framework。Binoculars/Fast-DetectGPT ordinal baseline 接近 chance， 确认现有 binary detector 不具备 ordinal 能力。Bootstrap CIs 紧致（±1-2pp），三模型 cross-seed max Δ<3pp。 论文定位 \"task formalization + theoretical grounding + systematic empirical atlas + practical framework\" 获审稿人认可，projected_reviewer_avg 3.7-4.0。\n\n- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/paper_framing.md`（先 Read 此文件）\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-18T16:42:16.059Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T16:42:16.059Z",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c"
}
```

---

## Round 1

30 recorded events

### User

_source line 3 · 2026-05-18T16:42:16.079Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162616 tier=best 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完
6. 你必须在论文中为 experiment_data.json 中的**每个**实验设计对应的 section/table
7. narrative_guidance 是你的写作方向指引，不要在论文正文中引用或复述此指引

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：best档叙事：14B Qwen2.5-14B FP16 完整验证 depth signal 在主流规模上的持续性， 消除"small model only"质疑。理论section从 Shumailov tail erosion + Dohmatob contraction rate 推导出 EDD 上界=4±1，与三模型实证 EDD=4 精确吻合，将 Atlas 从 empirical observation 升级为 theoretically grounded framework。Binoculars/Fast-DetectGPT ordinal baseline 接近 chance， 确认现有 binary detector 不具备 ordinal 能力。Bootstrap CIs 紧致（±1-2pp），三模型 cross-seed max Δ<3pp。 论文定位 "task formalization + theoretical grounding + systematic empirical atlas + practical framework" 获审稿人认可，projected_reviewer_avg 3.7-4.0。

- paper_framing.md（完整版）：`/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/paper_framing.md`（先 Read 此文件）

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c9727216-6650-4282-92f3-6408303632c9",
  "type": "user",
  "uuid": "757b464f-f052-45f3-b4bd-42b9aba50fbc",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T16:42:16.078Z_

```json
{
  "parentUuid": "757b464f-f052-45f3-b4bd-42b9aba50fbc",
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
  "uuid": "a529ab6f-c3d1-45aa-a9e5-b8f157a5f946",
  "timestamp": "2026-05-18T16:42:16.078Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T16:42:16.078Z_

```json
{
  "parentUuid": "a529ab6f-c3d1-45aa-a9e5-b8f157a5f946",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3d9657f1-9581-471c-b66e-ae1cbbe34133",
  "timestamp": "2026-05-18T16:42:16.078Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
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
  "aiTitle": "Generate ordinal depth estimation paper with theory",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c"
}
```

---

### Assistant

_source line 7 · 2026-05-18T16:42:18.753Z_

Let me start by reading the input files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d9657f1-9581-471c-b66e-ae1cbbe34133",
  "isSidechain": false,
  "requestId": "req_011CbANJVYvE9vQPSAN1KgQn",
  "type": "assistant",
  "uuid": "47d0b365-0ac4-4364-a695-014959497a64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pq8DoiaxPbuH6wzZEWn8fd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12839,
      "cache_read_input_tokens": 11841,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 203,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12839
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

_source line 8 · 2026-05-18T16:42:19.382Z_

<details open><summary>🔧 Tool call — Read · `toolu_019V6XHGkCSPgFQz2krLL55y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47d0b365-0ac4-4364-a695-014959497a64",
  "isSidechain": false,
  "requestId": "req_011CbANJVYvE9vQPSAN1KgQn",
  "type": "assistant",
  "uuid": "743098e6-f980-4999-b9ff-742283e2f496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pq8DoiaxPbuH6wzZEWn8fd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12839,
      "cache_read_input_tokens": 11841,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 203,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12839
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

_source line 9 · 2026-05-18T16:42:19.703Z_

<details><summary>↩ Tool result · `toolu_019V6XHGkCSPgFQz2krLL55y`</summary>

```text
1	[
2	  {
3	    "name": "14B clean FP16 scale validation",
4	    "description": "Qwen2.5-14B FP16 + LoRA on 96GB RTX PRO 6000，无量化干扰。 完整 d0-d3 nucleus 递归链 + 19 特征提取 + RF/LR 分类。 验证 depth signal 在 14B 主流规模上是否与 1B 量级一致。\n",
5	    "results": {
6	      "rf_4class_acc": 0.79,
7	      "rf_4class_ci": [
8	        0.778,
9	        0.802
10	      ],
11	      "lr_4class_acc": 0.76,
12	      "d0v1_auc": 0.991,
13	      "d1v2_auc": 0.87,
14	      "d1v3_auc": 0.975,
15	      "d2v3_auc": 0.82,
16	      "rf_3class_acc": 0.74,
17	      "rf_3class_ci": [
18	        0.722,
19	        0.758
20	      ],
21	      "top_features": [
22	        "p90_ppl",
23	        "var_surprisal",
24	        "p75_ppl",
25	        "mean_surprisal"
26	      ],
27	      "feature_top4_overlap_with_1b": 4,
28	      "per_class_recall_d0": 0.98,
29	      "per_class_recall_d1": 0.84,
30	      "per_class_recall_d2": 0.62,
31	      "per_class_recall_d3": 0.72,
32	      "finetune_loss_d0": 2.35,
33	      "finetune_loss_d1": 1.58,
34	      "finetune_loss_d2": 1.15
35	    },
36	    "tables": [
37	      "Table 2: Scale robustness — Qwen2.5-14B vs 1B models (4-class acc, d1v2 AUC, top-4 features)"
38	    ],
39	    "figures": [],
40	    "analysis": "14B 结果彻底消除 \"small model only\" 质疑。关键论证：(1) 4class_acc=79% 在 1B 三模型 range [69.6, 85.4] 内，(2) d1v2_auc=0.87 与 1B 均值一致，(3) top-4 feature 完全重合（4/4）， (4) 无量化干扰（FP16 clean run vs 之前 7B QLoRA 的矛盾结果）。这支持 Claim 1 的 scale robustness 子句，并为 Atlas/EDD 的跨规模泛化提供直接证据。审稿人无法再以 \"only small models tested\" 降分。\n\n\nShumailov tail erosion 是递归生成的基本属性，不依赖模型规模——每次递归 fine-tune 都使输出分布的尾部进一步收缩 （高 perplexity token 概率下降，低 perplexity token 概率上升）。14B 模型容量更大意味着 d0 输出分布更接近训练数据（更宽尾），但递归过程同样驱动尾部收敛。因此 p90_ppl 和 var_surprisal 仍然是 top-4 特征（overlap=4/4）。绝对准确率 ~79% 处于 1B 三模型均值（78.3%）附近， 因为 Qwen2.5 架构的 RoPE + GQA 与 GPT-2/Pythia/OLMo 的 absolute PE + MHA 不同， but feature space 捕获的是输出分布统计属性而非架构细节。d1v2_auc=0.87 处于 [0.82, 0.92] 范围中段， 与 OLMo nucleus (0.867) 和 Pythia nucleus (0.861) 高度一致，支持\"depth signal 是 递归生成的普遍属性\"论点。14B 的 finetune loss 下降曲线（2.35→1.58→1.15）比 1B 更平缓， 因为大模型有更多 residual capacity 抵抗 catastrophic shift，但不足以阻止尾部收敛。\n"
41	  },
42	  {
43	    "name": "Wild-data calibration (C4/FineWeb/RedPajama)",
44	    "description": "从 C4/FineWeb/RedPajama 各抽取 10K 子集，用 Pythia-1.4B reference model 提取 19 特征， 用 3×3 训练好的 RF 分类器做 depth 预测 + 分布分析。验证 controlled setting 训练的 depth estimator 在 wild web-crawl 数据上的行为。\n",
45	    "results": {
46	      "c4_d0_pct": 78.5,
47	      "c4_d1_pct": 19.8,
48	      "c4_d2_pct": 1.2,
49	      "c4_d3_pct": 0.5,
50	      "c4_fpr": 21.5,
51	      "fineweb_d0_pct": 82.0,
52	      "fineweb_d1_pct": 16.8,
53	      "fineweb_d2_pct": 0.8,
54	      "fineweb_d3_pct": 0.4,
55	      "fineweb_fpr": 18.0,
56	      "redpajama_d0_pct": 85.0,
57	      "redpajama_d1_pct": 13.5,
58	      "redpajama_d2_pct": 1.0,
59	      "redpajama_d3_pct": 0.5,
60	      "redpajama_fpr": 15.0,
61	      "cross_model_consistency_d0_agreement": 0.92,
62	      "misclassified_content_type": "template/SEO/boilerplate"
63	    },
64	    "tables": [
65	      "Table A3: Wild-data depth distribution across C4/FineWeb/RedPajama (3 reference models)",
66	      "Table A4: Cross-model agreement on wild data depth predictions"
67	    ],
68	    "figures": [],
69	    "analysis": "Wild-data 结果有双重叙事价值：(1) 正面——depth estimator 在 editorial text (WikiText) 上 FPR≈0%，证明不会误判高质量人类文本；(2) 发现——web-crawl FPR ~15-22% 揭示了 template/SEO 内容与递归生成文本在特征空间中的 overlap，暗示 depth estimation 可兼做 web-crawl 质量分层工具。Limitations 需写明 \"controlled→wild domain shift 存在， FPR 对 web-crawl 质量高度敏感\"。\n\n\n已有 wild data 实验（wild_data_calibration_001~005, wild_data_features_001）建立了基线： WikiText FPR≈0%, C4 FPR≈20-34%, FineWeb FPR≈17-19%, OpenWebText FPR≈1-3%。 FPR 的主要来源是 web-crawl 中的 template/SEO/boilerplate 内容——这类文本天然具有 高重复率和低多样性（high rep_4gram, high p90_ppl），在特征空间中落入 \"degraded\" 区域。 这不是模型错误而是反映了一个真实发现：低质量 web 内容与递归生成文本共享统计特征。 RedPajama FPR 略低于 C4 因为其数据清洗 pipeline 更严格（已过滤部分 template 内容）。 cross-model consistency 高（~92%）因为三个 RF 分类器都依赖同一组 tail statistics， 而 template 内容在所有 reference model 下都产生异常的 perplexity 分布。 best 档下这些结果被写入 \"ecological validity\" section，作为 depth estimator 对 web-crawl 质量梯度的敏感性的正面发现。\n"
70	  },
71	  {
72	    "name": "Existing detector ordinal baseline (Binoculars + Fast-DetectGPT)",
73	    "description": "将 Binoculars 和 Fast-DetectGPT 的连续分数校准为 ordinal depth bin， 在 3×3 已有数据上评估 4-class ordinal depth estimation 性能。 两种校准方式：(a) 等分位 binning, (b) optimal threshold search (oracle)。\n",
74	    "results": {
75	      "binoculars_4class_acc_quantile": 0.32,
76	      "binoculars_4class_acc_oracle": 0.38,
77	      "binoculars_d1v2_auc": 0.56,
78	      "binoculars_d2v3_auc": 0.52,
79	      "fastdetectgpt_4class_acc_quantile": 0.3,
80	      "fastdetectgpt_4class_acc_oracle": 0.36,
81	      "fastdetectgpt_d1v2_auc": 0.54,
82	      "fastdetectgpt_d2v3_auc": 0.51,
83	      "combined_best_4class_acc": 0.4,
84	      "chance_baseline": 0.25,
85	      "rf_19feat_reference": 0.783
86	    },
87	    "tables": [
88	      "Table 3: Ordinal baseline comparison — Binary detectors vs feature-based methods"
89	    ],
90	    "figures": [],
91	    "analysis": "Binoculars/Fast-DetectGPT 的 ordinal failure 是论文最重要的 baseline 之一。 它直接支撑 \"ordinal depth estimation is a new task requiring new methods\" 的论点。 审稿人可能问 \"为什么不直接用 existing detector scores?\" → 这个实验回答： 因为 binary scores 在 d1+ 上 saturate，不编码 depth gradient。 RF 19-feature 方法的 ~78% vs binary detector 的 ~35% 形成 43pp gap， 强力论证 feature-based ordinal estimation 的必要性。 写法：不是 \"binary detectors are bad\"，而是 \"ordinal depth estimation requires features that track progressive degradation, which binary scores do not provide\"。\n\n\nBinoculars 和 Fast-DetectGPT 都是为 binary real/synthetic detection 设计的。 它们的连续分数反映 \"text 有多像 model output\" 的单维度信号，而非 ordinal depth gradient。 关键问题：binary detector score 与 depth 不是单调关系——d1 和 d3 的 binary score 可能接近 （都是 \"synthetic\"），但 d1 和 d3 在 tail statistics 上差异显著。Binoculars 使用 两个 LM 的 cross-perplexity ratio，主要捕获 d0 vs d1+ 的 boundary（d0v1 AUC 可能 ~0.85+）， 但对 d1/d2/d3 的区分接近 chance。Fast-DetectGPT 类似——其 perturbation-based score 在 d1+ 样本上趋于 plateau。oracle threshold search 能比 quantile binning 多 ~6pp 因为可以利用非均匀 depth 分布，但 ceiling 仍在 40% 左右（接近 [25, 45] range 上段）。 d1v2 AUC 0.54-0.56 勉强高于 chance (0.50)，证实 binary detector 的连续分数 不编码 ordinal depth 信息。这是论文的关键 negative baseline——\"existing detectors cannot estimate ordinal depth\" 的直接实证支撑。\n"
92	  },
93	  {
94	    "name": "Table 1 bootstrap CIs",
95	    "description": "对 3×3 矩阵所有 9 cells 的 5-fold CV 结果计算 bootstrap 95% confidence intervals。 纯 CPU 分析任务，从已有 fold-level 结果 resample。\n",
96	    "results": {
97	      "mean_ci_width_pp": 1.8,
98	      "max_ci_width_pp": 2.5,
99	      "min_ci_width_pp": 1.2,
100	      "ci_non_overlap_key_comparisons": true,
101	      "pythia_nucleus_ci": [
102	        0.769,
103	        0.794
104	      ],
105	      "pythia_temp09_ci": [
106	        0.749,
107	        0.776
108	      ],
109	      "pythia_topk50_ci": [
110	        0.682,
111	        0.711
112	      ],
113	      "olmo_nucleus_ci": [
114	        0.776,
115	        0.802
116	      ],
117	      "olmo_temp09_ci": [
118	        0.808,
119	        0.835
120	      ],
121	      "olmo_topk50_ci": [
122	        0.728,
123	        0.756
124	      ],
125	      "gpt2xl_nucleus_ci": [
126	        0.826,
127	        0.852
128	      ],
129	      "gpt2xl_temp09_ci": [
130	        0.841,
131	        0.867
132	      ],
133	      "gpt2xl_topk50_ci": [
134	        0.743,
135	        0.77
136	      ]
137	    },
138	    "tables": [
139	      "Table 1: 3×3 accuracy matrix with bootstrap 95% CIs"
140	    ],
141	    "figures": [],
142	    "analysis": "Bootstrap CIs 是 reviewer 硬性要求（Dream D002）。紧致的 CIs（mean ~1.8pp） 确保所有定量 claim 有统计基础。关键：9/9 cells 的 lower CI bound 均 >50%（chance×2）， 支持 \"depth signal is robust across all model-strategy combinations\" claim。 CI non-overlap 在 strategy 比较中支持三档分类（nucleus vs temp09 vs topk50）， 在 model 比较中显示 GPT-2 XL consistently strongest。\n\n\nBootstrap CIs 从已有 5-fold CV accuracies 计算，结果高度确定（非随机实验）。 每个 cell 有 n≈20000 样本（5000/depth × 4 depths），5-fold CV 提供 5 个独立 accuracy 估计。 Bootstrap resample 这 5 个点会得到 ±1-2.5pp 的 CI width，这与已有 cell-level CIs 一致 （如 Pythia nucleus [0.769, 0.794] = 2.5pp width, GPT-2 XL temp09 [0.843, 0.865] = 2.2pp width）。 CI width 主要由 fold 间方差驱动——topk50 cells 方差略大（因为 signal 弱导致 fold 间波动更大）， 但所有 cells 的 CI 都不跨越 chance (25%)。关键比较：temp09 vs nucleus 的 CI 在 GPT-2 XL 和 OLMo 上不重叠（temp09 显著优于 nucleus），支持 \"temperature enhances signal\" 结论； topk50 vs 其他两种策略的 CI 不重叠（topk50 显著弱），支持三档策略分类。\n"
143	  },
144	  {
145	    "name": "Theoretical analysis (model collapse → EDD upper bound)",
146	    "description": "理论 section 三部分：(1) tail erosion mechanism 解释 p90_ppl/var_surprisal 主导地位 via Shumailov et al. 2024, (2) EDD upper bound 推导 from Dohmatob 2024 contraction rates, (3) strategy-dependent convergence rate 解释 temp09 trajectory reversal。 产出: paper Theory section 草稿（1.5 pages）。\n",
147	    "results": {
148	      "edd_upper_bound_derived": 5,
149	      "edd_predicted_range": [
150	        3,
151	        5
152	      ],
153	      "edd_empirical_match": "EDD=4 across 3 models, within predicted [3,5]",
154	      "tail_erosion_rate_predicted": "p90_ppl decreases ~15-25% per generation depth",
155	      "tail_erosion_rate_empirical": "p90_ppl median decreases 18-22% per depth (observed)",
156	      "contraction_rate_alpha": 0.72,
157	      "fixed_point_convergence_depth": 5.2,
158	      "strategy_convergence_ratio_temp_vs_nucleus": 1.35,
159	      "verifiable_predictions_count": 3
160	    },
161	    "tables": [
162	      "Table 4: Theoretical predictions vs empirical observations"
163	    ],
164	    "figures": [],
165	    "analysis": "理论 section 是 best 档区别于 median/worst 的核心。它将 Atlas 从 \"empirical observation\" 升级为 \"theoretically grounded framework\"，直接回应 \"just an empirical study\" 质疑。 三条 verifiable predictions 给审稿人提供可验证的 falsifiable claims， 这是 empirical paper 通常缺少的。EDD 上界推导从 Dohmatob contraction rate 出发， 经由 classifier noise floor 得到闭式解，与三模型实证 EDD=4 吻合。 temp09 accelerated convergence 的理论解释（均匀 logit scaling vs 截断）将 empirical d1v2 反转 finding 嵌入 principled framework。 审稿人评价：\"theory section provides testable predictions that go beyond post-hoc rationalization\"——这是 best 档 4.0 accept 的关键加分项。\n\n\n理论推导基于两条已发表的理论： (1) Shumailov et al. (Nature 2024) 证明递归训练导致 \"model collapse\"，机制是尾部分布的 progressive erosion——每次递归使 rare token 概率衰减，common token 概率增长。 p90_ppl 精确捕获尾部行为（90th percentile 对 tail erosion 最敏感），var_surprisal 捕获整体分布宽度收窄。这解释了为什么这两个特征在 9/9 settings 中稳定占据 top-2。 (2) Dohmatob (2024) 给出了递归生成过程中分布收缩的定量 contraction rate α<1。 在 1B 规模模型上，α≈0.72（从 finetune loss 衰减曲线 2.27→1.65→1.23 反推）。 EDD 上界 = ⌈log(ε_noise) / log(α)⌉ 其中 ε_noise 是分类器噪声下限。 取 ε_noise=0.05（对应 AUC=0.75 threshold），得 EDD ≤ ⌈log(0.05)/log(0.72)⌉ = ⌈9.1⌉/2 ≈ 5。 实证 EDD=4 落在 predicted [3,5] 内。Temperature 的均匀 logit scaling（vs nucleus 的截断） 加速收敛（ratio≈1.35×），解释了 temp09 depth N ≈ nucleus depth N+1 的 empirical observation。 best 档下，三条 verifiable predictions 都与实验数据吻合： (a) EDD ∈ [3,5] ✓, (b) p90_ppl 衰减率 15-25%/depth ✓, (c) temp convergence ratio >1 ✓。\n"
166	  },
167	  {
168	    "name": "API model recursive chains (GPT-4o-mini)",
169	    "description": "两种方式：(a) GPT-4o-mini fine-tuning API 递归链（需 OpenAI key）， (b) Prompted recursive chain (rewrite/continue prompts, 无需 fine-tune)。 验证 depth signal 在商用 API 模型中是否存在。\n",
170	    "results": {
171	      "finetuned_chain_4class_acc": 0.58,
172	      "finetuned_chain_d1v2_auc": 0.72,
173	      "finetuned_chain_d0v1_auc": 0.93,
174	      "prompted_chain_4class_acc": 0.45,
175	      "prompted_chain_d1v2_auc": 0.61,
176	      "prompted_chain_d0v1_auc": 0.78,
177	      "top_features_finetuned": [
178	        "p90_ppl",
179	        "var_surprisal",
180	        "mean_ppl",
181	        "p75_ppl"
182	      ],
183	      "top_features_prompted": [
184	        "var_surprisal",
185	        "p90_ppl",
186	        "surprisal_range",
187	        "mean_surprisal"
188	      ],
189	      "feature_overlap_with_base_models": 3
190	    },
191	    "tables": [
192	      "Table A5: API model depth estimation (fine-tuned chain vs prompted chain vs base model baseline)"
193	    ],
194	    "figures": [],
195	    "analysis": "API model 实验是 best 档的 \"nice-to-have\" 而非 critical path。主要价值： (1) 扩展 generalization story 到商用模型生态，(2) 与 instruct model finding (47.4%) 形成一致叙事——RLHF regularizes but does not eliminate depth signal， (3) prompted chain 的弱信号 (45%) 揭示 generation mode dependence， 与 plan_016 prompted generation (69.5%) 的 fine-tuned chain 对比， 说明 fine-tuning vs prompting 是影响 depth signal 的关键因素之一。\n\n\nAPI 模型经过 RLHF/RLAIF 对齐训练，输出分布已被正则化——tail 被显著压缩， output diversity 受限于 safety/helpfulness objectives。这与 plan_021 instruct model (47.4%) 的 finding 一致：RLHF regularizes depth signal。 Fine-tuning API chain (~58%) 优于 prompted chain (~45%) 因为 fine-tuning 产生的 distributional shift 更接近我们的 benchmark 设置（LoRA fine-tune → generation → repeat）， 而 prompted chain 的 \"recursive generation\" 是通过 prompt engineering 模拟的， degradation pattern 不同（prompt-mediated vs parameter-level shift）。 Fine-tuned chain 的 top features 与 base model 一致（overlap≈3/4）， 因为 tail erosion 机制仍然存在，只是被 RLHF baseline regularization 削弱。 Prompted chain 的 feature profile 不同（surprisal_range 上升），因为 prompt engineering 引入了额外的 style/content constraints 影响 surprisal 分布。 best 档下，fine-tuned chain 58% 结果被写入 Appendix 作为 \"API model generalization\" evidence，prompted chain 45% 进 Discussion 作为 \"generation mode affects signal strength\" 的佐证。两者都 >chance (25%)，支持 \"depth signal is a general phenomenon of iterative generation, modulated by RLHF and generation mode\"。\n"
196	  },
197	  {
198	    "name": "DCOL component ablation (cancelled)",
199	    "description": "DCOL v6 RoBERTa-large 失败（test acc 64.5% vs RF baseline 78.2%, -13.7pp）， 前置条件 plan_004 未满足，此实验取消。\n",
200	    "results": {
201	      "status": "CANCELLED",
202	      "reason": "DCOL v6 failed (plan_004 conclusion: negative), prerequisite unmet",
203	      "negative_analysis_contribution": "DCOL v1-v6 全部失败的 failure mode 分析写入 negative analysis section（半页）。 核心结论：contrastive ordinal learning 在文本深度估计中面临固有困难—— adjacent depth 的 embedding space overlap 过大（d2 embeddings 与 d1/d3 的 cosine similarity >0.95），contrastive loss 无法在此 regime 下学习有效 margins。 这反过来支持 \"feature-based methods > end-to-end\" 的结论。\n"
204	    },
205	    "tables": [
206	      "Table A6: End-to-end vs feature-based method comparison (negative results)"
207	    ],
208	    "figures": [],
209	    "analysis": "DCOL 取消是 D010/D011 contingency plan 的执行。在 best 档下， 这不是一个 gap 而是一个 strength：negative analysis section 展示了 对 alternative approaches 的系统性探索，审稿人认可这是 thorough methodology 的标志。半页 negative analysis 覆盖 v1-v6 的 failure modes （embedding collapse, OOM, catastrophic forgetting, 超参违规, NaN 梯度, overfitting）， 结论 \"contrastive ordinal learning requires sufficient inter-class separability in embedding space, which adjacent recursive depths do not provide\" 是一个 standalone negative finding。\n\n\nDCOL 取消不影响 best 档。论文已转型为 \"task formalization + systematic empirical study\"， DCOL failure 反而加强叙事：(1) end-to-end 方法在此任务上的固有困难佐证了 feature engineering 的价值，(2) 与 DeBERTa baseline (58.3%) 和 RoBERTa baseline (59.5%) 形成一致 pattern——neural end-to-end 方法在 ordinal depth estimation 上 系统性低于 feature-based 方法，(3) negative analysis section 展示 research maturity， 审稿人通常对诚实报告失败尝试评价正面。\n"
210	  },
211	  {
212	    "name": "Theoretical section (what_if)",
213	    "description": "假设性理论 section——如果成功完成 plan_023 的全部内容， 对论文整体评分的预期影响。\n",
214	    "results": {
215	      "reviewer_score_delta": "+0.3 to +0.5",
216	      "addresses_concern": "'no algorithmic contribution' → 'theoretical grounding + verifiable predictions'",
217	      "key_equations": 2,
218	      "key_theorems": 1,
219	      "page_count": 1.5,
220	      "new_references": 4
221	    },
222	    "tables": [],
223	    "figures": [],
224	    "analysis": "理论 section 是 best 档能否达到 4.0 的 swing factor。 没有它，论文是 high-quality empirical study → 3.5。 有了它且 predictions 吻合，论文是 \"theoretically grounded new task formalization with systematic empirical validation\" → 3.8-4.0。 风险：如果理论推导过于 hand-wavy（如 contraction rate 的精确值依赖 未知的 model-specific constants），审稿人可能认为是 \"overfitting theory to data\"。 缓解：明确报告 theoretical range [3,5] 而非点预测， 并在 Discussion 中列出理论假设的 limitations。\n\n理论 section 的边际贡献是将论文从 \"comprehensive empirical study\" 升级为 \"empirically grounded + theoretically motivated framework\"。 在 EMNLP 评审标准中，\"theoretical analysis that makes testable predictions validated by experiments\" 通常带来 +0.3~0.5 的评分提升。 具体机制：(1) EDD 上界推导给出了一个 novel formal result（虽然简短）， (2) verifiable predictions 展示了理论的 predictive power 而非 post-hoc fitting， (3) Shumailov/Dohmatob 连接将本文嵌入 model collapse 理论框架， 增强 \"new mission for NLP\" 的 venue fit。 best 档下，审稿人评价从 \"solid empirical study (3.5)\" 升级为 \"empirical study with theoretical insight (3.8-4.0)\"。\n"
225	  }
226	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "743098e6-f980-4999-b9ff-742283e2f496",
  "isSidechain": false,
  "promptId": "c9727216-6650-4282-92f3-6408303632c9",
  "type": "user",
  "uuid": "c2c0ba9c-f234-4876-9b41-1b4db54b0915",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"14B clean FP16 scale validation\",\n    \"description\": \"Qwen2.5-14B FP16 + LoRA on 96GB RTX PRO 6000，无量化干扰。 完整 d0-d3 nucleus 递归链 + 19 特征提取 + RF/LR 分类。 验证 depth signal 在 14B 主流规模上是否与 1B 量级一致。\\n\",\n    \"results\": {\n      \"rf_4class_acc\": 0.79,\n      \"rf_4class_ci\": [\n        0.778,\n        0.802\n      ],\n      \"lr_4class_acc\": 0.76,\n      \"d0v1_auc\": 0.991,\n      \"d1v2_auc\": 0.87,\n      \"d1v3_auc\": 0.975,\n      \"d2v3_auc\": 0.82,\n      \"rf_3class_acc\": 0.74,\n      \"rf_3class_ci\": [\n        0.722,\n        0.758\n      ],\n      \"top_features\": [\n        \"p90_ppl\",\n        \"var_surprisal\",\n        \"p75_ppl\",\n        \"mean_surprisal\"\n      ],\n      \"feature_top4_overlap_with_1b\": 4,\n      \"per_class_recall_d0\": 0.98,\n      \"per_class_recall_d1\": 0.84,\n      \"per_class_recall_d2\": 0.62,\n      \"per_class_recall_d3\": 0.72,\n      \"finetune_loss_d0\": 2.35,\n      \"finetune_loss_d1\": 1.58,\n      \"finetune_loss_d2\": 1.15\n    },\n    \"tables\": [\n      \"Table 2: Scale robustness — Qwen2.5-14B vs 1B models (4-class acc, d1v2 AUC, top-4 features)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"14B 结果彻底消除 \\\"small model only\\\" 质疑。关键论证：(1) 4class_acc=79% 在 1B 三模型 range [69.6, 85.4] 内，(2) d1v2_auc=0.87 与 1B 均值一致，(3) top-4 feature 完全重合（4/4）， (4) 无量化干扰（FP16 clean run vs 之前 7B QLoRA 的矛盾结果）。这支持 Claim 1 的 scale robustness 子句，并为 Atlas/EDD 的跨规模泛化提供直接证据。审稿人无法再以 \\\"only small models tested\\\" 降分。\\n\\n\\nShumailov tail erosion 是递归生成的基本属性，不依赖模型规模——每次递归 fine-tune 都使输出分布的尾部进一步收缩 （高 perplexity token 概率下降，低 perplexity token 概率上升）。14B 模型容量更大意味着 d0 输出分布更接近训练数据（更宽尾），但递归过程同样驱动尾部收敛。因此 p90_ppl 和 var_surprisal 仍然是 top-4 特征（overlap=4/4）。绝对准确率 ~79% 处于 1B 三模型均值（78.3%）附近， 因为 Qwen2.5 架构的 RoPE + GQA 与 GPT-2/Pythia/OLMo 的 absolute PE + MHA 不同， but feature space 捕获的是输出分布统计属性而非架构细节。d1v2_auc=0.87 处于 [0.82, 0.92] 范围中段， 与 OLMo nucleus (0.867) 和 Pythia nucleus (0.861) 高度一致，支持\\\"depth signal 是 递归生成的普遍属性\\\"论点。14B 的 finetune loss 下降曲线（2.35→1.58→1.15）比 1B 更平缓， 因为大模型有更多 residual capacity 抵抗 catastrophic shift，但不足以阻止尾部收敛。\\n\"\n  },\n  {\n    \"name\": \"Wild-data calibration (C4/FineWeb/RedPajama)\",\n    \"description\": \"从 C4/FineWeb/RedPajama 各抽取 10K 子集，用 Pythia-1.4B reference model 提取 19 特征， 用 3×3 训练好的 RF 分类器做 depth 预测 + 分布分析。验证 controlled setting 训练的 depth estimator 在 wild web-crawl 数据上的行为。\\n\",\n    \"results\": {\n      \"c4_d0_pct\": 78.5,\n      \"c4_d1_pct\": 19.8,\n      \"c4_d2_pct\": 1.2,\n      \"c4_d3_pct\": 0.5,\n      \"c4_fpr\": 21.5,\n      \"fineweb_d0_pct\": 82.0,\n      \"fineweb_d1_pct\": 16.8,\n      \"fineweb_d2_pct\": 0.8,\n      \"fineweb_d3_pct\": 0.4,\n      \"fineweb_fpr\": 18.0,\n      \"redpajama_d0_pct\": 85.0,\n      \"redpajama_d1_pct\": 13.5,\n      \"redpajama_d2_pct\": 1.0,\n      \"redpajama_d3_pct\": 0.5,\n      \"redpajama_fpr\": 15.0,\n      \"cross_model_consistency_d0_agreement\": 0.92,\n      \"misclassified_content_type\": \"template/SEO/boilerplate\"\n    },\n    \"tables\": [\n      \"Table A3: Wild-data depth distribution across C4/FineWeb/RedPajama (3 reference models)\",\n      \"Table A4: Cross-model agreement on wild data depth predictions\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Wild-data 结果有双重叙事价值：(1) 正面——depth estimator 在 editorial text (WikiText) 上 FPR≈0%，证明不会误判高质量人类文本；(2) 发现——web-crawl FPR ~15-22% 揭示了 template/SEO 内容与递归生成文本在特征空间中的 overlap，暗示 depth estimation 可兼做 web-crawl 质量分层工具。Limitations 需写明 \\\"controlled→wild domain shift 存在， FPR 对 web-crawl 质量高度敏感\\\"。\\n\\n\\n已有 wild data 实验（wild_data_calibration_001~005, wild_data_features_001）建立了基线： WikiText FPR≈0%, C4 FPR≈20-34%, FineWeb FPR≈17-19%, OpenWebText FPR≈1-3%。 FPR 的主要来源是 web-crawl 中的 template/SEO/boilerplate 内容——这类文本天然具有 高重复率和低多样性（high rep_4gram, high p90_ppl），在特征空间中落入 \\\"degraded\\\" 区域。 这不是模型错误而是反映了一个真实发现：低质量 web 内容与递归生成文本共享统计特征。 RedPajama FPR 略低于 C4 因为其数据清洗 pipeline 更严格（已过滤部分 template 内容）。 cross-model consistency 高（~92%）因为三个 RF 分类器都依赖同一组 tail statistics， 而 template 内容在所有 reference model 下都产生异常的 perplexity 分布。 best 档下这些结果被写入 \\\"ecological validity\\\" section，作为 depth estimator 对 web-crawl 质量梯度的敏感性的正面发现。\\n\"\n  },\n  {\n    \"name\": \"Existing detector ordinal baseline (Binoculars + Fast-DetectGPT)\",\n    \"description\": \"将 Binoculars 和 Fast-DetectGPT 的连续分数校准为 ordinal depth bin， 在 3×3 已有数据上评估 4-class ordinal depth estimation 性能。 两种校准方式：(a) 等分位 binning, (b) optimal threshold search (oracle)。\\n\",\n    \"results\": {\n      \"binoculars_4class_acc_quantile\": 0.32,\n      \"binoculars_4class_acc_oracle\": 0.38,\n      \"binoculars_d1v2_auc\": 0.56,\n      \"binoculars_d2v3_auc\": 0.52,\n      \"fastdetectgpt_4class_acc_quantile\": 0.3,\n      \"fastdetectgpt_4class_acc_oracle\": 0.36,\n      \"fastdetectgpt_d1v2_auc\": 0.54,\n      \"fastdetectgpt_d2v3_auc\": 0.51,\n      \"combined_best_4class_acc\": 0.4,\n      \"chance_baseline\": 0.25,\n      \"rf_19feat_reference\": 0.783\n    },\n    \"tables\": [\n      \"Table 3: Ordinal baseline comparison — Binary detectors vs feature-based methods\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Binoculars/Fast-DetectGPT 的 ordinal failure 是论文最重要的 baseline 之一。 它直接支撑 \\\"ordinal depth estimation is a new task requiring new methods\\\" 的论点。 审稿人可能问 \\\"为什么不直接用 existing detector scores?\\\" → 这个实验回答： 因为 binary scores 在 d1+ 上 saturate，不编码 depth gradient。 RF 19-feature 方法的 ~78% vs binary detector 的 ~35% 形成 43pp gap， 强力论证 feature-based ordinal estimation 的必要性。 写法：不是 \\\"binary detectors are bad\\\"，而是 \\\"ordinal depth estimation requires features that track progressive degradation, which binary scores do not provide\\\"。\\n\\n\\nBinoculars 和 Fast-DetectGPT 都是为 binary real/synthetic detection 设计的。 它们的连续分数反映 \\\"text 有多像 model output\\\" 的单维度信号，而非 ordinal depth gradient。 关键问题：binary detector score 与 depth 不是单调关系——d1 和 d3 的 binary score 可能接近 （都是 \\\"synthetic\\\"），但 d1 和 d3 在 tail statistics 上差异显著。Binoculars 使用 两个 LM 的 cross-perplexity ratio，主要捕获 d0 vs d1+ 的 boundary（d0v1 AUC 可能 ~0.85+）， 但对 d1/d2/d3 的区分接近 chance。Fast-DetectGPT 类似——其 perturbation-based score 在 d1+ 样本上趋于 plateau。oracle threshold search 能比 quantile binning 多 ~6pp 因为可以利用非均匀 depth 分布，但 ceiling 仍在 40% 左右（接近 [25, 45] range 上段）。 d1v2 AUC 0.54-0.56 勉强高于 chance (0.50)，证实 binary detector 的连续分数 不编码 ordinal depth 信息。这是论文的关键 negative baseline——\\\"existing detectors cannot estimate ordinal depth\\\" 的直接实证支撑。\\n\"\n  },\n  {\n    \"name\": \"Table 1 bootstrap CIs\",\n    \"description\": \"对 3×3 矩阵所有 9 cells 的 5-fold CV 结果计算 bootstrap 95% confidence intervals。 纯 CPU 分析任务，从已有 fold-level 结果 resample。\\n\",\n    \"results\": {\n      \"mean_ci_width_pp\": 1.8,\n      \"max_ci_width_pp\": 2.5,\n      \"min_ci_width_pp\": 1.2,\n      \"ci_non_overlap_key_comparisons\": true,\n      \"pythia_nucleus_ci\": [\n        0.769,\n        0.794\n      ],\n      \"pythia_temp09_ci\": [\n        0.749,\n        0.776\n      ],\n      \"pythia_topk50_ci\": [\n        0.682,\n        0.711\n      ],\n      \"olmo_nucleus_ci\": [\n        0.776,\n        0.802\n      ],\n      \"olmo_temp09_ci\": [\n        0.808,\n        0.835\n      ],\n      \"olmo_topk50_ci\": [\n        0.728,\n        0.756\n      ],\n      \"gpt2xl_nucleus_ci\": [\n        0.826,\n        0.852\n      ],\n      \"gpt2xl_temp09_ci\": [\n        0.841,\n        0.867\n      ],\n      \"gpt2xl_topk50_ci\": [\n        0.743,\n        0.77\n      ]\n    },\n    \"tables\": [\n      \"Table 1: 3×3 accuracy matrix with bootstrap 95% CIs\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"Bootstrap CIs 是 reviewer 硬性要求（Dream D002）。紧致的 CIs（mean ~1.8pp） 确保所有定量 claim 有统计基础。关键：9/9 cells 的 lower CI bound 均 >50%（chance×2）， 支持 \\\"depth signal is robust across all model-strategy combinations\\\" claim。 CI non-overlap 在 strategy 比较中支持三档分类（nucleus vs temp09 vs topk50）， 在 model 比较中显示 GPT-2 XL consistently strongest。\\n\\n\\nBootstrap CIs 从已有 5-fold CV accuracies 计算，结果高度确定（非随机实验）。 每个 cell 有 n≈20000 样本（5000/depth × 4 depths），5-fold CV 提供 5 个独立 accuracy 估计。 Bootstrap resample 这 5 个点会得到 ±1-2.5pp 的 CI width，这与已有 cell-level CIs 一致 （如 Pythia nucleus [0.769, 0.794] = 2.5pp width, GPT-2 XL temp09 [0.843, 0.865] = 2.2pp width）。 CI width 主要由 fold 间方差驱动——topk50 cells 方差略大（因为 signal 弱导致 fold 间波动更大）， 但所有 cells 的 CI 都不跨越 chance (25%)。关键比较：temp09 vs nucleus 的 CI 在 GPT-2 XL 和 OLMo 上不重叠（temp09 显著优于 nucleus），支持 \\\"temperature enhances signal\\\" 结论； topk50 vs 其他两种策略的 CI 不重叠（topk50 显著弱），支持三档策略分类。\\n\"\n  },\n  {\n    \"name\": \"Theoretical analysis (model collapse → EDD upper bound)\",\n    \"description\": \"理论 section 三部分：(1) tail erosion mechanism 解释 p90_ppl/var_surprisal 主导地位 via Shumailov et al. 2024, (2) EDD upper bound 推导 from Dohmatob 2024 contraction rates, (3) strategy-dependent convergence rate 解释 temp09 trajectory reversal。 产出: paper Theory section 草稿（1.5 pages）。\\n\",\n    \"results\": {\n      \"edd_upper_bound_derived\": 5,\n      \"edd_predicted_range\": [\n        3,\n        5\n      ],\n      \"edd_empirical_match\": \"EDD=4 across 3 models, within predicted [3,5]\",\n      \"tail_erosion_rate_predicted\": \"p90_ppl decreases ~15-25% per generation depth\",\n      \"tail_erosion_rate_empirical\": \"p90_ppl median decreases 18-22% per depth (observed)\",\n      \"contraction_rate_alpha\": 0.72,\n      \"fixed_point_convergence_depth\": 5.2,\n      \"strategy_convergence_ratio_temp_vs_nucleus\": 1.35,\n      \"verifiable_predictions_count\": 3\n    },\n    \"tables\": [\n      \"Table 4: Theoretical predictions vs empirical observations\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"理论 section 是 best 档区别于 median/worst 的核心。它将 Atlas 从 \\\"empirical observation\\\" 升级为 \\\"theoretically grounded framework\\\"，直接回应 \\\"just an empirical study\\\" 质疑。 三条 verifiable predictions 给审稿人提供可验证的 falsifiable claims， 这是 empirical paper 通常缺少的。EDD 上界推导从 Dohmatob contraction rate 出发， 经由 classifier noise floor 得到闭式解，与三模型实证 EDD=4 吻合。 temp09 accelerated convergence 的理论解释（均匀 logit scaling vs 截断）将 empirical d1v2 反转 finding 嵌入 principled framework。 审稿人评价：\\\"theory section provides testable predictions that go beyond post-hoc rationalization\\\"——这是 best 档 4.0 accept 的关键加分项。\\n\\n\\n理论推导基于两条已发表的理论： (1) Shumailov et al. (Nature 2024) 证明递归训练导致 \\\"model collapse\\\"，机制是尾部分布的 progressive erosion——每次递归使 rare token 概率衰减，common token 概率增长。 p90_ppl 精确捕获尾部行为（90th percentile 对 tail erosion 最敏感），var_surprisal 捕获整体分布宽度收窄。这解释了为什么这两个特征在 9/9 settings 中稳定占据 top-2。 (2) Dohmatob (2024) 给出了递归生成过程中分布收缩的定量 contraction rate α<1。 在 1B 规模模型上，α≈0.72（从 finetune loss 衰减曲线 2.27→1.65→1.23 反推）。 EDD 上界 = ⌈log(ε_noise) / log(α)⌉ 其中 ε_noise 是分类器噪声下限。 取 ε_noise=0.05（对应 AUC=0.75 threshold），得 EDD ≤ ⌈log(0.05)/log(0.72)⌉ = ⌈9.1⌉/2 ≈ 5。 实证 EDD=4 落在 predicted [3,5] 内。Temperature 的均匀 logit scaling（vs nucleus 的截断） 加速收敛（ratio≈1.35×），解释了 temp09 depth N ≈ nucleus depth N+1 的 empirical observation。 best 档下，三条 verifiable predictions 都与实验数据吻合： (a) EDD ∈ [3,5] ✓, (b) p90_ppl 衰减率 15-25%/depth ✓, (c) temp convergence ratio >1 ✓。\\n\"\n  },\n  {\n    \"name\": \"API model recursive chains (GPT-4o-mini)\",\n    \"description\": \"两种方式：(a) GPT-4o-mini fine-tuning API 递归链（需 OpenAI key）， (b) Prompted recursive chain (rewrite/continue prompts, 无需 fine-tune)。 验证 depth signal 在商用 API 模型中是否存在。\\n\",\n    \"results\": {\n      \"finetuned_chain_4class_acc\": 0.58,\n      \"finetuned_chain_d1v2_auc\": 0.72,\n      \"finetuned_chain_d0v1_auc\": 0.93,\n      \"prompted_chain_4class_acc\": 0.45,\n      \"prompted_chain_d1v2_auc\": 0.61,\n      \"prompted_chain_d0v1_auc\": 0.78,\n      \"top_features_finetuned\": [\n        \"p90_ppl\",\n        \"var_surprisal\",\n        \"mean_ppl\",\n        \"p75_ppl\"\n      ],\n      \"top_features_prompted\": [\n        \"var_surprisal\",\n        \"p90_ppl\",\n        \"surprisal_range\",\n        \"mean_surprisal\"\n      ],\n      \"feature_overlap_with_base_models\": 3\n    },\n    \"tables\": [\n      \"Table A5: API model depth estimation (fine-tuned chain vs prompted chain vs base model baseline)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"API model 实验是 best 档的 \\\"nice-to-have\\\" 而非 critical path。主要价值： (1) 扩展 generalization story 到商用模型生态，(2) 与 instruct model finding (47.4%) 形成一致叙事——RLHF regularizes but does not eliminate depth signal， (3) prompted chain 的弱信号 (45%) 揭示 generation mode dependence， 与 plan_016 prompted generation (69.5%) 的 fine-tuned chain 对比， 说明 fine-tuning vs prompting 是影响 depth signal 的关键因素之一。\\n\\n\\nAPI 模型经过 RLHF/RLAIF 对齐训练，输出分布已被正则化——tail 被显著压缩， output diversity 受限于 safety/helpfulness objectives。这与 plan_021 instruct model (47.4%) 的 finding 一致：RLHF regularizes depth signal。 Fine-tuning API chain (~58%) 优于 prompted chain (~45%) 因为 fine-tuning 产生的 distributional shift 更接近我们的 benchmark 设置（LoRA fine-tune → generation → repeat）， 而 prompted chain 的 \\\"recursive generation\\\" 是通过 prompt engineering 模拟的， degradation pattern 不同（prompt-mediated vs parameter-level shift）。 Fine-tuned chain 的 top features 与 base model 一致（overlap≈3/4）， 因为 tail erosion 机制仍然存在，只是被 RLHF baseline regularization 削弱。 Prompted chain 的 feature profile 不同（surprisal_range 上升），因为 prompt engineering 引入了额外的 style/content constraints 影响 surprisal 分布。 best 档下，fine-tuned chain 58% 结果被写入 Appendix 作为 \\\"API model generalization\\\" evidence，prompted chain 45% 进 Discussion 作为 \\\"generation mode affects signal strength\\\" 的佐证。两者都 >chance (25%)，支持 \\\"depth signal is a general phenomenon of iterative generation, modulated by RLHF and generation mode\\\"。\\n\"\n  },\n  {\n    \"name\": \"DCOL component ablation (cancelled)\",\n    \"description\": \"DCOL v6 RoBERTa-large 失败（test acc 64.5% vs RF baseline 78.2%, -13.7pp）， 前置条件 plan_004 未满足，此实验取消。\\n\",\n    \"results\": {\n      \"status\": \"CANCELLED\",\n      \"reason\": \"DCOL v6 failed (plan_004 conclusion: negative), prerequisite unmet\",\n      \"negative_analysis_contribution\": \"DCOL v1-v6 全部失败的 failure mode 分析写入 negative analysis section（半页）。 核心结论：contrastive ordinal learning 在文本深度估计中面临固有困难—— adjacent depth 的 embedding space overlap 过大（d2 embeddings 与 d1/d3 的 cosine similarity >0.95），contrastive loss 无法在此 regime 下学习有效 margins。 这反过来支持 \\\"feature-based methods > end-to-end\\\" 的结论。\\n\"\n    },\n    \"tables\": [\n      \"Table A6: End-to-end vs feature-based method comparison (negative results)\"\n    ],\n    \"figures\": [],\n    \"analysis\": \"DCOL 取消是 D010/D011 contingency plan 的执行。在 best 档下， 这不是一个 gap 而是一个 strength：negative analysis section 展示了 对 alternative approaches 的系统性探索，审稿人认可这是 thorough methodology 的标志。半页 negative analysis 覆盖 v1-v6 的 failure modes （embedding collapse, OOM, catastrophic forgetting, 超参违规, NaN 梯度, overfitting）， 结论 \\\"contrastive ordinal learning requires sufficient inter-class separability in embedding space, which adjacent recursive depths do not provide\\\" 是一个 standalone negative finding。\\n\\n\\nDCOL 取消不影响 best 档。论文已转型为 \\\"task formalization + systematic empirical study\\\"， DCOL failure 反而加强叙事：(1) end-to-end 方法在此任务上的固有困难佐证了 feature engineering 的价值，(2) 与 DeBERTa baseline (58.3%) 和 RoBERTa baseline (59.5%) 形成一致 pattern——neural end-to-end 方法在 ordinal depth estimation 上 系统性低于 feature-based 方法，(3) negative analysis section 展示 research maturity， 审稿人通常对诚实报告失败尝试评价正面。\\n\"\n  },\n  {\n    \"name\": \"Theoretical section (what_if)\",\n    \"description\": \"假设性理论 section——如果成功完成 plan_023 的全部内容， 对论文整体评分的预期影响。\\n\",\n    \"results\": {\n      \"reviewer_score_delta\": \"+0.3 to +0.5\",\n      \"addresses_concern\": \"'no algorithmic contribution' → 'theoretical grounding + verifiable predictions'\",\n      \"key_equations\": 2,\n      \"key_theorems\": 1,\n      \"page_count\": 1.5,\n      \"new_references\": 4\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"理论 section 是 best 档能否达到 4.0 的 swing factor。 没有它，论文是 high-quality empirical study → 3.5。 有了它且 predictions 吻合，论文是 \\\"theoretically grounded new task formalization with systematic empirical validation\\\" → 3.8-4.0。 风险：如果理论推导过于 hand-wavy（如 contraction rate 的精确值依赖 未知的 model-specific constants），审稿人可能认为是 \\\"overfitting theory to data\\\"。 缓解：明确报告 theoretical range [3,5] 而非点预测， 并在 Discussion 中列出理论假设的 limitations。\\n\\n理论 section 的边际贡献是将论文从 \\\"comprehensive empirical study\\\" 升级为 \\\"empirically grounded + theoretically motivated framework\\\"。 在 EMNLP 评审标准中，\\\"theoretical analysis that makes testable predictions validated by experiments\\\" 通常带来 +0.3~0.5 的评分提升。 具体机制：(1) EDD 上界推导给出了一个 novel formal result（虽然简短）， (2) verifiable predictions 展示了理论的 predictive power 而非 post-hoc fitting， (3) Shumailov/Dohmatob 连接将本文嵌入 model collapse 理论框架， 增强 \\\"new mission for NLP\\\" 的 venue fit。 best 档下，审稿人评价从 \\\"solid empirical study (3.5)\\\" 升级为 \\\"empirical study with theoretical insight (3.8-4.0)\\\"。\\n\"\n  }\n]",
      "numLines": 226,
      "startLine": 1,
      "totalLines": 226
    }
  },
  "sourceToolAssistantUUID": "743098e6-f980-4999-b9ff-742283e2f496",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T16:42:19.915Z_

<details><summary>↩ Tool result · `toolu_01HKUCFHxmM9JtvEvax4CLfQ`</summary>

```text
1	# Paper Framing — recursive_gen_depth_est
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25, 2026)
5	- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)
6	- EMNLP 2026 special theme "New Missions for NLP Research" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit
7	
8	## Core Claims (3 条 + Discussion implication)
9	
10	1. **Ordinal depth estimation is feasible, accurate, and robust across scales and generation modes**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features from reference-model perplexity distributions. On our 3-model × 3-strategy benchmark (1–1.5B), Random Forest classifiers on 19 statistical features achieve 70–85% four-class accuracy (chance=25%), with the best configuration (GPT-2 XL, temp τ=0.9) reaching 85.4%. Feature-based methods (RF, CORAL, DivEye) consistently outperform single-feature baselines across all settings. **Scale robustness**: Clean FP16 13B experiment (Qwen2.5-14B, no quantization) confirms depth signal persists at mainstream model scale, addressing the "small model only" concern from prior 7B QLoRA experiments. **Ecological validity**: Prompted generation experiment (topic-seeded text, not BOS-only unconditional) confirms depth signal is not an artifact of unnatural generation mode.
11	
12	2. **Depth Degradation Atlas — systematic characterization of recursive collapse** (PRIMARY): We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) perplexity tail statistics (p90_ppl) and surprisal variance (var_surprisal) as the dominant depth signal family — consistently occupying the top-4 features across all models and strategies, though their relative ranking is model-dependent, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable, and (d) **strategy-dependent feature trajectory reversal** — temperature sampling causes the depth-1→depth-2 feature boundary to invert relative to nucleus/top-k (cross-strategy LOO d1v2 AUC as low as 0.13), demonstrating that decoding strategy fundamentally shapes the degradation trajectory rather than merely attenuating it, and (e) **accelerated convergence mechanism** — root cause analysis confirms a genuine structural distributional shift: temperature's uniform logit scaling (vs nucleus/top-k truncation) accelerates convergence to the attractor distribution, so temp09 depth N features ≈ nucleus/topk50 depth N+1 (GPT-2 XL temp09 d1 p90_ppl median=92.2, falls into nucleus/topk50 d2 range 65–92). This is not a simple scale artifact fixable by normalization — z-score normalization improves overall LR cross-strategy accuracy (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), and does **not** improve tree-based classifiers (RF Δ<0.02pp) — confirming a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation methods could recover the d1/d2 boundary remains open. This atlas spans 3 model families × 3 decoding strategies, with scale consistency confirmed at 14B.
13	
14	3. **Cross-strategy depth estimation via two-stage pipeline + strategy-invariant signal discovery**: Naive cross-strategy transfer degrades to 59.1% with d1v2 boundary inversion. We propose a two-stage solution: (a) strategy identification classifier (57.8% — strategies share more feature space than expected), then (b) strategy-conditioned depth classifiers. The pipeline improves cross-strategy accuracy by **+11.5pp** on average (59.1% → 70.5%), with per-model results: GPT-2 XL 73.0%, OLMo 69.4%, Pythia 69.3%. Oracle ceiling at 78.3%. **Caveat**: improvement is consistent across models but absolute accuracy varies (2/3 models individually below 70%); paper must claim "+11.5pp improvement" rather than "≥70% universal recovery". The surprising finding: even with imperfect strategy routing, the pipeline works because depth signal has a **strategy-invariant core** (~60% accuracy floor) plus a strategy-specific component. This reframes cross-strategy transfer from "broken" to "substantially improved with clear ceiling for future work".
15	
16	4. **[Discussion — Practical Implication]** Depth-graduated curation as alternative to binary filtering: predicted depth provides a finer-grained quality proxy than binary real/synthetic labels, enabling graduated weighting strategies. Conceptual argument supported by depth-accuracy correlation in 3×3 matrix data; full experimental validation deferred to future work (D012).
17	
18	## Story Spine
19	
20	- **Problem**: Web-scraped training corpora increasingly contain multi-generational synthetic content from uncontrolled model→data→model feedback loops. Existing detectors answer "is this synthetic?" but not "how many recursive cycles has this undergone?" — a critical distinction since 1st-gen synthetic data can improve training while deeply recursive text drives distribution collapse.
21	
22	- **Existing approaches & gaps**: Binary detectors (LOKI, DivEye, Binoculars) classify real vs. synthetic but discard ordinal depth information. EditLens estimates single-pass AI editing extent but not recursive depth. Model collapse studies (Drayson et al. EMNLP 2025; Shumailov et al. Nature 2024) characterize degradation patterns but assume depth is known a priori — no method estimates depth from text alone.
23	
24	- **Our framing**: We formalize ordinal generation depth estimation as a new task, construct a multi-generational benchmark spanning 1B–14B models across 3 decoding strategies and 4 depths, and provide the first **Depth Degradation Atlas** — a systematic empirical map of how text statistical properties evolve across recursive depths, models, and strategies. The Atlas reveals (a) perplexity tail statistics as universal depth markers across all settings, (b) model-dependent strategy interaction effects with an identified root cause, and (c) the Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable. We show that feature-based classifiers achieve 70–85% four-class accuracy, and propose a two-stage strategy-aware pipeline that solves the cross-strategy deployment challenge. The depth signal persists under prompted generation (not just BOS-seeded), confirming ecological relevance.
25	
26	- **Headline result template**: "On our multi-generational benchmark spanning model scales from 1B to 14B and 3 decoding strategies, feature-based ordinal depth estimation achieves 70–85% accuracy (chance=25%), with perplexity tail statistics (p90_ppl, var_surprisal) consistently among the top-4 features across all settings. The depth signal persists under prompted (topic-seeded) generation and at 14B scale without quantization. The Depth Degradation Atlas reveals that effective discriminable depth extends to depth 3 in 7/9 settings (T=0.75). We identify strategy-dependent feature trajectory reversal and propose a two-stage pipeline that restores near within-strategy accuracy for cross-strategy deployment."
27	- **Note**: 4-class (depth 0-3) is the confirmed setting. 6-class (depth 0-5) completed via plan_011.
28	
29	## DCOL Status — Contingency Activated (D010/D011, 2026-05-15)
30	
31	DCOL v1–v5 全部失败（embedding collapse / OOM / catastrophic forgetting / 超参违规 / NaN 梯度爆炸）。
32	
33	- **Claim 2 (Atlas/EDD) 升为 PRIMARY contribution**
34	- **Claim 1**: Feature-based methods (RF/CORAL/DivEye) 作为 depth estimation 方法，不依赖 DCOL
35	- **DCOL v6 (RoBERTa-large)**: 非阻塞尝试。成功 → Section 5 bonus；失败 → negative analysis section（"contrastive ordinal learning 在文本深度估计的固有局限"）
36	- **Paper type**: Task formalization + systematic empirical study + practical framework（非 method paper）
37	- Atlas + EDD + feature universality + model-strategy interaction = 充分支撑 EMNLP "New Missions" track
38	
39	## Venue Fit Risks
40	
41	- **"Just an empirical study" risk**: Primary risk now that DCOL is demoted. Mitigation: (a) task formalization is a genuine contribution — no prior work estimates ordinal depth from text alone; (b) Atlas + EDD are novel analytical tools, not just tables; (c) feature universality finding (p90_ppl/var_surprisal top-4 across 9 settings) is a scientific claim with practical implications; (d) model-strategy interaction effects are a new finding; (e) **cross-strategy two-stage pipeline (Claim 3)** is a concrete practical contribution, not just analysis. EMNLP "New Missions" track explicitly values problem formalization.
42	- **Controlled vs wild gap**: Mitigation: prompted generation experiment validates signal under realistic generation conditions (topic-seeded, not BOS-only). Honest scoping — controlled setting is primary, prompted generation bridges toward ecological validity.
43	- **"No novel method" concern**: Mitigation: (a) RF/CORAL are tools, not the contribution; (b) the two-stage cross-strategy pipeline IS a novel practical method for strategy-aware depth estimation; (c) 13B clean experiment shows method scales without modification. Analogous to benchmark/analysis papers at top venues (e.g., HELM, MMLU).
44	- **"Small model only" concern**: Eliminated by clean 13B FP16 experiment. Prior 7B QLoRA results were contradictory due to quantization artifacts; 13B clean run provides definitive scale evidence.
45	
46	## Dream-Derived Requirements (D002, 2026-05-14)
47	
48	三档(best 3.0 / median 3.0 / worst 2.5)一致指出的结构性必修项：
49	
50	### 论文写作硬约束
51	1. **DCOL loss 描述** — 若 v6 成功：Eq.1 必须包含 attractive + repulsive 双项（N-pair formulation）。若 v6 失败：negative analysis section 描述失败模式和根因分析，无需完整 loss 公式
52	2. **至少4张图** — (a) AUC decay curve across depth pairs w/ EDD threshold line (b) feature trajectory panel (top-5 features × depth, stratified by model) (c) confusion matrix heatmap (d) Atlas feature×depth heatmap grid。"Atlas without maps is a contradiction"
53	3. **Bibliography 25+ references** — 必须覆盖: watermarking (Kirchenbauer ICML 2023), model collapse theory (Alemohammad ICLR 2024, Dohmatob 2024, Gerstgrasser 2024), data curation (DSIR, QuRating), multi-source attribution (Uchendu 2020), binary detectors (Binoculars Hans ICML 2024, Fast-DetectGPT Bao 2024), decoding strategy effects (Garces Arias COLING 2025, Holtzman ICLR 2020)
54	4. **Surprisal reference model** — 必须明确指定 reference model、说明 cross-model LOO 时如何处理、讨论 circularity
55	
56	### 指标报告硬约束
57	5. **d1-d5 only accuracy** — 作为 companion metric 报告，隔离 ordinal depth estimation 与 binary human-vs-machine detection
58	6. **EDD threshold sensitivity** — 报告 AUC threshold 在 0.65/0.70/0.75/0.80 四档下的 EDD 值
59	7. **k-NN inference 完整规格** — k 值、distance metric、sensitivity analysis
60	
61	### Framing 方向
62	8. **Atlas/EDD 为 primary contribution** — DCOL 定位为 "one strong method within the framework"，不作为 co-primary。三档审稿均认为 DCOL 是 incremental adaptation of CLOC。与 DCOL Contingency 一致。
63	9. **"First systematic empirical map" 需限定** — Shumailov/Drayson 已有 characterization, 我们的新颖性在 ordinal estimation lens + EDD formalization + multi-model multi-strategy coverage
64	
65	### Cross-Strategy 反转硬约束 (D015, Reviewer 降级条件)
66	10. **三档策略分类** — 论文不得将 nucleus 和 temperature 归为同一类 "soft sampling"。必须采用三档：nucleus（baseline 稳定）、temperature（信号增强但存在 d1v2 方向反转风险）、topk（信号衰减但方向一致）。D004 的 "soft sampling" 分组已被反转数据推翻。
67	11. **Discussion 必须含 per-strategy d1v2 AUC 表** — 包含 0.13/0.25 反转值 + **已确认的机制**：temperature 均匀缩放 logit（非截断）加速模型收敛到 attractor 分布（genuine structural distributional shift），temp09 depth N ≈ nucleus/topk50 depth N+1。z-score 标准化提升整体 LR 跨策略 acc（25%→61%）但**不恢复** pairwise d1v2 AUC（GPT-2 XL 0.50→0.24, OLMo 0.50→0.19），证实这是结构性几何偏移而非可校正的尺度差异。
68	12. **Limitations 必须写明跨策略部署约束** — "跨策略部署时需先验知道目标策略类型，否则 d1/d2 预测可能反转。"不可仅将反转作为正面发现消化。
69	
70	## Anticipated Reviewer Concerns
71	
72	1. "EDD might be very low (depth 2-3), making the task trivial beyond shallow depths" → Report EDD transparently; argue even low EDD is scientifically valuable (determines the boundary) and practically sufficient (shallow vs deep is the actionable distinction for curation). Data: 7/9 settings EDD≥3 at T=0.75. **Depth extension bootstrap (D027)**: 三模型 d3v4 AUC 聚集在 0.75 附近 (Pythia 0.784 p=0.001 ✅, OLMo 0.765 p=0.091 ⚠️, GPT-2 XL 0.750 p=0.505 ❌)，仅 Pythia 统计显著。**禁止**写 "three models all achieve statistically significant EDD=4"。正确措辞："d3v4 AUC consistently clusters near the 0.75 threshold (0.750–0.784) across all three models, while d4v5 AUC uniformly falls below 0.70 (0.681–0.694)"——强调方向一致性 + 完整报告 CI 和 p-values。D024 连续衰减曲线叙事被 bootstrap 数据强力支持。
73	2. "Why ordinal and not just binary?" → d0v1 AUC=0.998 vs d1v2=0.861 vs d2v3=0.801 — ordinal structure captures monotonically decreasing but still significant discrimination at all adjacent pairs
74	3. "Generalization to unseen models/strategies?" → Cross-model LOO: mean 66.4% (holdout Pythia 62.4%, OLMo 69.2%, GPT-2 XL 67.6%) — all >chance but depth_0 recall >98% inflates headline. **Must report per-class recall** (depth_2 recall as low as 26.8%). Cross-strategy LOO: mean 59.1% (51.5–69.4%), topk50 holdout consistently worst. **temp09 holdout shows d1v2 AUC reversal** (GPT-2 XL 0.13, OLMo 0.25) — root cause confirmed as genuine structural distributional shift (temperature accelerates convergence to attractor distribution). Z-score normalization improves overall LR acc (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), confirming a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation could recover d1v2 AUC remains open. Discuss as "strategy shapes degradation trajectory" finding — temp09 cross-strategy d1v2 generalization remains an open problem (D013/D015/D021).
75	4. "No novel method — just RF on features" → (a) Contribution is task formalization + Atlas + EDD + systematic findings, not just method; (b) the two-stage cross-strategy pipeline (Claim 3) IS a novel practical method that solves the deployment challenge; (c) 13B clean experiment confirms the approach scales without modification. Analogous to benchmark papers (HELM, MMLU). Feature universality across 9+ settings is itself a finding.
76	5. "d0 confound inflates headline metrics" → Report d1-only accuracy alongside full accuracy; 3-class (d1/d2/d3) results already show 59–82% accuracy
77	6. "EDD threshold is arbitrary" → Sensitivity analysis at 0.65/0.70/0.75/0.80 completed (Dream D002)
78	7. "No figures for Atlas" → Minimum 4 figures (Dream D002)
79	8. "Bibliography too thin" → 25+ refs covering all relevant subfields (Dream D002)
80	9. "Model-strategy interaction is just noise" → Three-tier pattern confirmed: nucleus=stable baseline, temperature=enhances signal but reverses d1v2 feature boundary in cross-strategy transfer, topk=attenuates signal but preserves direction (D015). Garces Arias (COLING 2025) independently confirms model-dependent strategy effects.
81	10. "Cross-strategy deployment is unreliable" → **Now addressed by Claim 3**: Two-stage pipeline (strategy identification → strategy-conditioned depth classification) provides a practical solution. Strategy classifier achieves 57.8% accuracy on 19 features (below the expected >90%), indicating strategy distributions are less separable than anticipated. A two-stage pipeline (oracle strategy identification + strategy-conditioned depth classification) recovers 11.5pp over naive LOO, though practical deployment still requires either strategy metadata or improved routing. The root cause (temperature's accelerated convergence) is identified and the mechanism explained.
82	11. "Signal is an artifact of unconditional BOS-seeded generation" → Prompted generation experiment (plan_016) tests depth signal under topic-seeded generation. If signal persists → validates ecological relevance; if not → important finding about generation mode dependence (written as limitation).
83	12. "Only tested on small models (1–1.5B)" → Clean 13B FP16 experiment (Qwen2.5-14B, plan_017) confirms scale robustness without quantization confounds. Prior 7B QLoRA results were contradictory — now superseded by clean experiment.
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00859b38-9186-4742-8ee9-8b3ecdac49f1",
  "isSidechain": false,
  "promptId": "c9727216-6650-4282-92f3-6408303632c9",
  "type": "user",
  "uuid": "d80bea7e-a288-4490-8c94-d73d23b471b3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/paper_framing.md",
      "content": "# Paper Framing — recursive_gen_depth_est\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25, 2026)\n- Backup: AAAI 2027 (abstract July 25, full paper August 1, 2026)\n- EMNLP 2026 special theme \"New Missions for NLP Research\" explicitly calls for work on data contamination, synthetic data feedback loops, and data governance — direct venue fit\n\n## Core Claims (3 条 + Discussion implication)\n\n1. **Ordinal depth estimation is feasible, accurate, and robust across scales and generation modes**: Given text alone, recursive generation depth (d ∈ {0,1,2,...,K}) can be estimated with high accuracy using statistical features from reference-model perplexity distributions. On our 3-model × 3-strategy benchmark (1–1.5B), Random Forest classifiers on 19 statistical features achieve 70–85% four-class accuracy (chance=25%), with the best configuration (GPT-2 XL, temp τ=0.9) reaching 85.4%. Feature-based methods (RF, CORAL, DivEye) consistently outperform single-feature baselines across all settings. **Scale robustness**: Clean FP16 13B experiment (Qwen2.5-14B, no quantization) confirms depth signal persists at mainstream model scale, addressing the \"small model only\" concern from prior 7B QLoRA experiments. **Ecological validity**: Prompted generation experiment (topic-seeded text, not BOS-only unconditional) confirms depth signal is not an artifact of unnatural generation mode.\n\n2. **Depth Degradation Atlas — systematic characterization of recursive collapse** (PRIMARY): We provide the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, revealing (a) perplexity tail statistics (p90_ppl) and surprisal variance (var_surprisal) as the dominant depth signal family — consistently occupying the top-4 features across all models and strategies, though their relative ranking is model-dependent, (b) non-uniform inter-depth distances (depth 0→1 gap >> depth 2→3 gap), (c) an Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable, and (d) **strategy-dependent feature trajectory reversal** — temperature sampling causes the depth-1→depth-2 feature boundary to invert relative to nucleus/top-k (cross-strategy LOO d1v2 AUC as low as 0.13), demonstrating that decoding strategy fundamentally shapes the degradation trajectory rather than merely attenuating it, and (e) **accelerated convergence mechanism** — root cause analysis confirms a genuine structural distributional shift: temperature's uniform logit scaling (vs nucleus/top-k truncation) accelerates convergence to the attractor distribution, so temp09 depth N features ≈ nucleus/topk50 depth N+1 (GPT-2 XL temp09 d1 p90_ppl median=92.2, falls into nucleus/topk50 d2 range 65–92). This is not a simple scale artifact fixable by normalization — z-score normalization improves overall LR cross-strategy accuracy (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), and does **not** improve tree-based classifiers (RF Δ<0.02pp) — confirming a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation methods could recover the d1/d2 boundary remains open. This atlas spans 3 model families × 3 decoding strategies, with scale consistency confirmed at 14B.\n\n3. **Cross-strategy depth estimation via two-stage pipeline + strategy-invariant signal discovery**: Naive cross-strategy transfer degrades to 59.1% with d1v2 boundary inversion. We propose a two-stage solution: (a) strategy identification classifier (57.8% — strategies share more feature space than expected), then (b) strategy-conditioned depth classifiers. The pipeline improves cross-strategy accuracy by **+11.5pp** on average (59.1% → 70.5%), with per-model results: GPT-2 XL 73.0%, OLMo 69.4%, Pythia 69.3%. Oracle ceiling at 78.3%. **Caveat**: improvement is consistent across models but absolute accuracy varies (2/3 models individually below 70%); paper must claim \"+11.5pp improvement\" rather than \"≥70% universal recovery\". The surprising finding: even with imperfect strategy routing, the pipeline works because depth signal has a **strategy-invariant core** (~60% accuracy floor) plus a strategy-specific component. This reframes cross-strategy transfer from \"broken\" to \"substantially improved with clear ceiling for future work\".\n\n4. **[Discussion — Practical Implication]** Depth-graduated curation as alternative to binary filtering: predicted depth provides a finer-grained quality proxy than binary real/synthetic labels, enabling graduated weighting strategies. Conceptual argument supported by depth-accuracy correlation in 3×3 matrix data; full experimental validation deferred to future work (D012).\n\n## Story Spine\n\n- **Problem**: Web-scraped training corpora increasingly contain multi-generational synthetic content from uncontrolled model→data→model feedback loops. Existing detectors answer \"is this synthetic?\" but not \"how many recursive cycles has this undergone?\" — a critical distinction since 1st-gen synthetic data can improve training while deeply recursive text drives distribution collapse.\n\n- **Existing approaches & gaps**: Binary detectors (LOKI, DivEye, Binoculars) classify real vs. synthetic but discard ordinal depth information. EditLens estimates single-pass AI editing extent but not recursive depth. Model collapse studies (Drayson et al. EMNLP 2025; Shumailov et al. Nature 2024) characterize degradation patterns but assume depth is known a priori — no method estimates depth from text alone.\n\n- **Our framing**: We formalize ordinal generation depth estimation as a new task, construct a multi-generational benchmark spanning 1B–14B models across 3 decoding strategies and 4 depths, and provide the first **Depth Degradation Atlas** — a systematic empirical map of how text statistical properties evolve across recursive depths, models, and strategies. The Atlas reveals (a) perplexity tail statistics as universal depth markers across all settings, (b) model-dependent strategy interaction effects with an identified root cause, and (c) the Effective Discriminable Depth (EDD) boundary beyond which adjacent depths become indistinguishable. We show that feature-based classifiers achieve 70–85% four-class accuracy, and propose a two-stage strategy-aware pipeline that solves the cross-strategy deployment challenge. The depth signal persists under prompted generation (not just BOS-seeded), confirming ecological relevance.\n\n- **Headline result template**: \"On our multi-generational benchmark spanning model scales from 1B to 14B and 3 decoding strategies, feature-based ordinal depth estimation achieves 70–85% accuracy (chance=25%), with perplexity tail statistics (p90_ppl, var_surprisal) consistently among the top-4 features across all settings. The depth signal persists under prompted (topic-seeded) generation and at 14B scale without quantization. The Depth Degradation Atlas reveals that effective discriminable depth extends to depth 3 in 7/9 settings (T=0.75). We identify strategy-dependent feature trajectory reversal and propose a two-stage pipeline that restores near within-strategy accuracy for cross-strategy deployment.\"\n- **Note**: 4-class (depth 0-3) is the confirmed setting. 6-class (depth 0-5) completed via plan_011.\n\n## DCOL Status — Contingency Activated (D010/D011, 2026-05-15)\n\nDCOL v1–v5 全部失败（embedding collapse / OOM / catastrophic forgetting / 超参违规 / NaN 梯度爆炸）。\n\n- **Claim 2 (Atlas/EDD) 升为 PRIMARY contribution**\n- **Claim 1**: Feature-based methods (RF/CORAL/DivEye) 作为 depth estimation 方法，不依赖 DCOL\n- **DCOL v6 (RoBERTa-large)**: 非阻塞尝试。成功 → Section 5 bonus；失败 → negative analysis section（\"contrastive ordinal learning 在文本深度估计的固有局限\"）\n- **Paper type**: Task formalization + systematic empirical study + practical framework（非 method paper）\n- Atlas + EDD + feature universality + model-strategy interaction = 充分支撑 EMNLP \"New Missions\" track\n\n## Venue Fit Risks\n\n- **\"Just an empirical study\" risk**: Primary risk now that DCOL is demoted. Mitigation: (a) task formalization is a genuine contribution — no prior work estimates ordinal depth from text alone; (b) Atlas + EDD are novel analytical tools, not just tables; (c) feature universality finding (p90_ppl/var_surprisal top-4 across 9 settings) is a scientific claim with practical implications; (d) model-strategy interaction effects are a new finding; (e) **cross-strategy two-stage pipeline (Claim 3)** is a concrete practical contribution, not just analysis. EMNLP \"New Missions\" track explicitly values problem formalization.\n- **Controlled vs wild gap**: Mitigation: prompted generation experiment validates signal under realistic generation conditions (topic-seeded, not BOS-only). Honest scoping — controlled setting is primary, prompted generation bridges toward ecological validity.\n- **\"No novel method\" concern**: Mitigation: (a) RF/CORAL are tools, not the contribution; (b) the two-stage cross-strategy pipeline IS a novel practical method for strategy-aware depth estimation; (c) 13B clean experiment shows method scales without modification. Analogous to benchmark/analysis papers at top venues (e.g., HELM, MMLU).\n- **\"Small model only\" concern**: Eliminated by clean 13B FP16 experiment. Prior 7B QLoRA results were contradictory due to quantization artifacts; 13B clean run provides definitive scale evidence.\n\n## Dream-Derived Requirements (D002, 2026-05-14)\n\n三档(best 3.0 / median 3.0 / worst 2.5)一致指出的结构性必修项：\n\n### 论文写作硬约束\n1. **DCOL loss 描述** — 若 v6 成功：Eq.1 必须包含 attractive + repulsive 双项（N-pair formulation）。若 v6 失败：negative analysis section 描述失败模式和根因分析，无需完整 loss 公式\n2. **至少4张图** — (a) AUC decay curve across depth pairs w/ EDD threshold line (b) feature trajectory panel (top-5 features × depth, stratified by model) (c) confusion matrix heatmap (d) Atlas feature×depth heatmap grid。\"Atlas without maps is a contradiction\"\n3. **Bibliography 25+ references** — 必须覆盖: watermarking (Kirchenbauer ICML 2023), model collapse theory (Alemohammad ICLR 2024, Dohmatob 2024, Gerstgrasser 2024), data curation (DSIR, QuRating), multi-source attribution (Uchendu 2020), binary detectors (Binoculars Hans ICML 2024, Fast-DetectGPT Bao 2024), decoding strategy effects (Garces Arias COLING 2025, Holtzman ICLR 2020)\n4. **Surprisal reference model** — 必须明确指定 reference model、说明 cross-model LOO 时如何处理、讨论 circularity\n\n### 指标报告硬约束\n5. **d1-d5 only accuracy** — 作为 companion metric 报告，隔离 ordinal depth estimation 与 binary human-vs-machine detection\n6. **EDD threshold sensitivity** — 报告 AUC threshold 在 0.65/0.70/0.75/0.80 四档下的 EDD 值\n7. **k-NN inference 完整规格** — k 值、distance metric、sensitivity analysis\n\n### Framing 方向\n8. **Atlas/EDD 为 primary contribution** — DCOL 定位为 \"one strong method within the framework\"，不作为 co-primary。三档审稿均认为 DCOL 是 incremental adaptation of CLOC。与 DCOL Contingency 一致。\n9. **\"First systematic empirical map\" 需限定** — Shumailov/Drayson 已有 characterization, 我们的新颖性在 ordinal estimation lens + EDD formalization + multi-model multi-strategy coverage\n\n### Cross-Strategy 反转硬约束 (D015, Reviewer 降级条件)\n10. **三档策略分类** — 论文不得将 nucleus 和 temperature 归为同一类 \"soft sampling\"。必须采用三档：nucleus（baseline 稳定）、temperature（信号增强但存在 d1v2 方向反转风险）、topk（信号衰减但方向一致）。D004 的 \"soft sampling\" 分组已被反转数据推翻。\n11. **Discussion 必须含 per-strategy d1v2 AUC 表** — 包含 0.13/0.25 反转值 + **已确认的机制**：temperature 均匀缩放 logit（非截断）加速模型收敛到 attractor 分布（genuine structural distributional shift），temp09 depth N ≈ nucleus/topk50 depth N+1。z-score 标准化提升整体 LR 跨策略 acc（25%→61%）但**不恢复** pairwise d1v2 AUC（GPT-2 XL 0.50→0.24, OLMo 0.50→0.19），证实这是结构性几何偏移而非可校正的尺度差异。\n12. **Limitations 必须写明跨策略部署约束** — \"跨策略部署时需先验知道目标策略类型，否则 d1/d2 预测可能反转。\"不可仅将反转作为正面发现消化。\n\n## Anticipated Reviewer Concerns\n\n1. \"EDD might be very low (depth 2-3), making the task trivial beyond shallow depths\" → Report EDD transparently; argue even low EDD is scientifically valuable (determines the boundary) and practically sufficient (shallow vs deep is the actionable distinction for curation). Data: 7/9 settings EDD≥3 at T=0.75. **Depth extension bootstrap (D027)**: 三模型 d3v4 AUC 聚集在 0.75 附近 (Pythia 0.784 p=0.001 ✅, OLMo 0.765 p=0.091 ⚠️, GPT-2 XL 0.750 p=0.505 ❌)，仅 Pythia 统计显著。**禁止**写 \"three models all achieve statistically significant EDD=4\"。正确措辞：\"d3v4 AUC consistently clusters near the 0.75 threshold (0.750–0.784) across all three models, while d4v5 AUC uniformly falls below 0.70 (0.681–0.694)\"——强调方向一致性 + 完整报告 CI 和 p-values。D024 连续衰减曲线叙事被 bootstrap 数据强力支持。\n2. \"Why ordinal and not just binary?\" → d0v1 AUC=0.998 vs d1v2=0.861 vs d2v3=0.801 — ordinal structure captures monotonically decreasing but still significant discrimination at all adjacent pairs\n3. \"Generalization to unseen models/strategies?\" → Cross-model LOO: mean 66.4% (holdout Pythia 62.4%, OLMo 69.2%, GPT-2 XL 67.6%) — all >chance but depth_0 recall >98% inflates headline. **Must report per-class recall** (depth_2 recall as low as 26.8%). Cross-strategy LOO: mean 59.1% (51.5–69.4%), topk50 holdout consistently worst. **temp09 holdout shows d1v2 AUC reversal** (GPT-2 XL 0.13, OLMo 0.25) — root cause confirmed as genuine structural distributional shift (temperature accelerates convergence to attractor distribution). Z-score normalization improves overall LR acc (25%→61%) but does **not** recover pairwise d1v2 AUC (GPT-2 XL 0.50→0.24, OLMo 0.50→0.19), confirming a distributional shift that simple feature normalization cannot resolve; whether more sophisticated domain adaptation could recover d1v2 AUC remains open. Discuss as \"strategy shapes degradation trajectory\" finding — temp09 cross-strategy d1v2 generalization remains an open problem (D013/D015/D021).\n4. \"No novel method — just RF on features\" → (a) Contribution is task formalization + Atlas + EDD + systematic findings, not just method; (b) the two-stage cross-strategy pipeline (Claim 3) IS a novel practical method that solves the deployment challenge; (c) 13B clean experiment confirms the approach scales without modification. Analogous to benchmark papers (HELM, MMLU). Feature universality across 9+ settings is itself a finding.\n5. \"d0 confound inflates headline metrics\" → Report d1-only accuracy alongside full accuracy; 3-class (d1/d2/d3) results already show 59–82% accuracy\n6. \"EDD threshold is arbitrary\" → Sensitivity analysis at 0.65/0.70/0.75/0.80 completed (Dream D002)\n7. \"No figures for Atlas\" → Minimum 4 figures (Dream D002)\n8. \"Bibliography too thin\" → 25+ refs covering all relevant subfields (Dream D002)\n9. \"Model-strategy interaction is just noise\" → Three-tier pattern confirmed: nucleus=stable baseline, temperature=enhances signal but reverses d1v2 feature boundary in cross-strategy transfer, topk=attenuates signal but preserves direction (D015). Garces Arias (COLING 2025) independently confirms model-dependent strategy effects.\n10. \"Cross-strategy deployment is unreliable\" → **Now addressed by Claim 3**: Two-stage pipeline (strategy identification → strategy-conditioned depth classification) provides a practical solution. Strategy classifier achieves 57.8% accuracy on 19 features (below the expected >90%), indicating strategy distributions are less separable than anticipated. A two-stage pipeline (oracle strategy identification + strategy-conditioned depth classification) recovers 11.5pp over naive LOO, though practical deployment still requires either strategy metadata or improved routing. The root cause (temperature's accelerated convergence) is identified and the mechanism explained.\n11. \"Signal is an artifact of unconditional BOS-seeded generation\" → Prompted generation experiment (plan_016) tests depth signal under topic-seeded generation. If signal persists → validates ecological relevance; if not → important finding about generation mode dependence (written as limitation).\n12. \"Only tested on small models (1–1.5B)\" → Clean 13B FP16 experiment (Qwen2.5-14B, plan_017) confirms scale robustness without quantization confounds. Prior 7B QLoRA results were contradictory — now superseded by clean experiment.\n",
      "numLines": 84,
      "startLine": 1,
      "totalLines": 84
    }
  },
  "sourceToolAssistantUUID": "00859b38-9186-4742-8ee9-8b3ecdac49f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T16:42:19.902Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HKUCFHxmM9JtvEvax4CLfQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2c0ba9c-f234-4876-9b41-1b4db54b0915",
  "isSidechain": false,
  "requestId": "req_011CbANJVYvE9vQPSAN1KgQn",
  "type": "assistant",
  "uuid": "00859b38-9186-4742-8ee9-8b3ecdac49f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pq8DoiaxPbuH6wzZEWn8fd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12839,
      "cache_read_input_tokens": 11841,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 203,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12839
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162616 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_dept…",
  "leafUuid": "d80bea7e-a288-4490-8c94-d73d23b471b3",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate ordinal depth estimation paper with theory",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c"
}
```

---

### Assistant

_source line 14 · 2026-05-18T16:42:36.465Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of both the experiment data and paper framing. Let me also check the output directory.

Let me now write the full LaTeX paper. I need to:

1. Create a comprehensive paper with Abstract, Introduction, Related Work, Method, Theory, Experiments (covering ALL experiments from experiment_data.json), and Conclusion
2. Use data from experiment_data.json for all quantitative claims
3. Follow the narrative guidance about 14B validation, theoretical grounding, ordinal baseline comparison, etc.

Let me organize the experiments into sections:
- Table 1: 3×3 accuracy matrix with bootstrap CIs (from "Table 1 bootstrap CIs")


- Table 2: Scale robustness — 14B vs 1B (from "14B clean FP16 scale validation")
- Table 3: Ordinal baseline comparison (from "Existing detector ordinal baseline")
- Table 4: Theoretical predictions vs empirical (from "Theoretical analysis")
- Table A3/A4: Wild-data calibration (from "Wild-data calibration")
- Table A5: API model depth estimation (from "API model recursive chains")
- Table A6: End-to-end vs feature-based (from "DCOL component ablation (cancelled)")

Now I'll draft the paper.

I'm structuring this as a standard article with abstract, introduction, related work, and task formalization for ordinal depth estimation. The core sections will cover the theoretical analysis of tail erosion and EDD bounds, then present the experimental results starting with the 3×3 Atlas table with confidence intervals, followed by scale robustness findings, baseline comparisons, and theoretical validation. I'll include the cross-strategy pipeline results, then discuss wild-data calibration, API model generalization, the negative DCOL results, and limitations before concluding. The appendix will contain the additional tables.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d80bea7e-a288-4490-8c94-d73d23b471b3",
  "isSidechain": false,
  "requestId": "req_011CbANJnKj7ZMMgA3Nawk1r",
  "type": "assistant",
  "uuid": "0a249c90-1fb6-479c-a462-7487bbbe6452",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PC8sgcQzAE9P8nxKNqAmBn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13512,
      "cache_read_input_tokens": 24680,
      "output_tokens": 656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13512,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 656,
          "cache_read_input_tokens": 24680,
          "cache_creation_input_tokens": 13512,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13512
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

_source line 15 · 2026-05-18T16:42:36.466Z_

Now let me check the output directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a249c90-1fb6-479c-a462-7487bbbe6452",
  "isSidechain": false,
  "requestId": "req_011CbANJnKj7ZMMgA3Nawk1r",
  "type": "assistant",
  "uuid": "ff6625d6-c611-47f0-a435-76003e9c5a64",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PC8sgcQzAE9P8nxKNqAmBn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13512,
      "cache_read_input_tokens": 24680,
      "output_tokens": 656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13512,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 656,
          "cache_read_input_tokens": 24680,
          "cache_creation_input_tokens": 13512,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13512
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

_source line 16 · 2026-05-18T16:42:36.747Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01N7gugFpCpJbpLHqzdW1rTC`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/",
  "description": "List output directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff6625d6-c611-47f0-a435-76003e9c5a64",
  "isSidechain": false,
  "requestId": "req_011CbANJnKj7ZMMgA3Nawk1r",
  "type": "assistant",
  "uuid": "b559a764-7a04-42fd-b493-101cbc558bd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PC8sgcQzAE9P8nxKNqAmBn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13512,
      "cache_read_input_tokens": 24680,
      "output_tokens": 656,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13512,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 656,
          "cache_read_input_tokens": 24680,
          "cache_creation_input_tokens": 13512,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13512
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

_source line 17 · 2026-05-18T16:42:36.926Z_

<details><summary>↩ Tool result · `toolu_01N7gugFpCpJbpLHqzdW1rTC`</summary>

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
  "parentUuid": "b559a764-7a04-42fd-b493-101cbc558bd1",
  "isSidechain": false,
  "promptId": "c9727216-6650-4282-92f3-6408303632c9",
  "type": "user",
  "uuid": "b4b2233f-153d-4ce3-9375-64160647c12f",
  "toolUseResult": {
    "stdout": "experiment_data.json\nimagined_experiments.yaml\npaper_framing.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "b559a764-7a04-42fd-b493-101cbc558bd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-18T16:42:49.530Z_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists. Now let me write the full LaTeX paper.

I need to carefully incorporate ALL experiments:
1. "14B clean FP16 scale validation" → Table 2
2. "Wild-data calibration (C4/FineWeb/RedPajama)" → Table in appendix (A3, A4)
3. "Existing detector ordinal baseline (Binoculars + Fast-DetectGPT)" → Table 3
4. "Table 1 bootstrap CIs" → Table 1


5. "Theoretical analysis (model collapse → EDD upper bound)" → Table 4
6. "API model recursive chains (GPT-4o-mini)" → Table A5 in appendix
7. "DCOL component ablation (cancelled)" → Table A6, negative analysis

I'll structure this following the paper_framing.md narrative, making sure to incorporate the key metrics: the 3×3 matrix with bootstrap confidence intervals, the 14B model's performance at 0.79 accuracy and 0.87 AUC with perfect top-4 overlap, and the Binoculars baseline at 0.32 accuracy for comparison.

Now I'm reviewing the empirical results across different detection methods and datasets. The RF model achieves 0.783 accuracy as my reference point, while the theoretical EDD upper bound sits at 5 with empirical performance hitting 4. I'm also tracking the contraction rate at 0.72 and examining how false positive rates vary across different pretraining corpora—C4 at 21.5%, FineWeb at 18.0%, and RedPajama at 15.0%. For the API models, I see finetuned approaches reaching 58% while prompted methods plateau around 45%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4b2233f-153d-4ce3-9375-64160647c12f",
  "isSidechain": false,
  "requestId": "req_011CbANL2cz1EAG4aHFzXCmD",
  "type": "assistant",
  "uuid": "ba4cbe6a-87f7-454d-96f7-3c342a0f601f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013kXKDEnGfG1xNvj7p9tpEQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 38192,
      "output_tokens": 13664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13664,
          "cache_read_input_tokens": 38192,
          "cache_creation_input_tokens": 683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 683
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

_source line 19 · 2026-05-18T16:42:49.556Z_

Writing the full LaTeX paper now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba4cbe6a-87f7-454d-96f7-3c342a0f601f",
  "isSidechain": false,
  "requestId": "req_011CbANL2cz1EAG4aHFzXCmD",
  "type": "assistant",
  "uuid": "c031414a-7e51-44de-9e94-0e7a19f3fff3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013kXKDEnGfG1xNvj7p9tpEQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 38192,
      "output_tokens": 13664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13664,
          "cache_read_input_tokens": 38192,
          "cache_creation_input_tokens": 683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 683
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

_source line 20 · 2026-05-18T16:46:57.571Z_

<details open><summary>🔧 Tool call — Write · `toolu_014CQ1BEBzmd2YsnyUAvgEBf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/paper.tex",
  "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{enumitem}\n\n\\newcommand{\\edd}{\\textsc{EDD}}\n\\newcommand{\\atlas}{\\textsc{Atlas}}\n\n\\title{Depth Degradation Atlas: Ordinal Estimation of Recursive Generation Depth from Text}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWeb-scraped training corpora increasingly contain multi-generational synthetic content produced by uncontrolled model-data-model feedback loops. Existing detectors classify text as real or synthetic but discard ordinal depth information, a critical distinction since first-generation synthetic data can improve training while deeply recursive text drives distribution collapse. We formalize \\emph{ordinal generation depth estimation} as a new task: given text alone, predict how many recursive generation cycles it has undergone. We construct a multi-generational benchmark spanning three model families (GPT-2 XL, OLMo-1B, Pythia-1.4B), three decoding strategies (nucleus, temperature, top-$k$), and four depth levels (d0--d3), and provide the first \\emph{Depth Degradation Atlas}, a systematic empirical map of how text statistical properties evolve across recursive depths. Random Forest classifiers on 19 statistical features achieve 70--85\\% four-class accuracy (chance = 25\\%), with bootstrap 95\\% confidence intervals of $\\pm$1--2.5 percentage points. The depth signal persists at 14B scale (Qwen2.5-14B FP16, 79\\% accuracy) with identical top-4 features (4/4 overlap), eliminating the ``small model only'' concern. We derive a theoretical upper bound on Effective Discriminable Depth (\\edd) from model collapse contraction rates, predicting \\edd{} $\\in [3,5]$, which matches the empirical \\edd{} = 4 observed across all three model families. Existing binary detectors (Binoculars, Fast-DetectGPT) achieve only 30--38\\% when repurposed for ordinal estimation (near chance), confirming that ordinal depth estimation requires dedicated methods. A two-stage strategy-aware pipeline recovers +11.5 percentage points over naive cross-strategy transfer, addressing the deployment challenge.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nLarge language models (LLMs) are increasingly used to generate training data for subsequent model generations, creating recursive feedback loops where synthetic text is consumed, learned from, and regenerated. Recent work has shown that such iterative retraining leads to progressive distribution collapse: output distributions lose tail diversity, rare tokens disappear, and text quality degrades monotonically with recursion depth \\citep{shumailov2024model,alemohammad2024selfconsuming,dohmatob2024tale}. Understanding \\emph{how deeply recursive} a piece of text is has direct practical implications for data curation, since shallow-generation synthetic data may be beneficial while deeply recursive text actively harms model training \\citep{gerstgrasser2024model}.\n\nExisting approaches to synthetic text detection frame the problem as binary classification: real versus machine-generated \\citep{hans2024binoculars,bao2024fastdetectgpt,liang2024monitoring}. This binary framing discards critical ordinal information. A text classified as ``synthetic'' could be first-generation output (potentially useful for training augmentation) or fifth-generation output (likely degraded beyond utility). Model collapse studies characterize degradation patterns but assume depth is known a priori \\citep{drayson2025investigatinggeneralizabilitygenerationdegradation,shumailov2024model}. No prior method estimates recursive generation depth from text alone.\n\nWe formalize \\emph{ordinal generation depth estimation} as a new task. Given a text passage and a reference language model, the goal is to predict the number of recursive fine-tune-and-generate cycles the text has undergone. This framing captures the monotonic degradation structure that binary detection ignores and provides a finer-grained quality signal for data curation pipelines.\n\nOur central empirical finding is that recursive generation depth leaves detectable statistical signatures in text, primarily in perplexity tail statistics. Across all nine model-strategy combinations in our benchmark, the 90th percentile of per-token perplexity (\\texttt{p90\\_ppl}) and surprisal variance (\\texttt{var\\_surprisal}) consistently rank among the top-4 discriminative features. This universality is not coincidental: we connect it to the tail erosion mechanism formalized by \\citet{shumailov2024model}, where each recursive cycle compresses the output distribution's tails. We derive a theoretical upper bound on the Effective Discriminable Depth (\\edd) from the contraction rate framework of \\citet{dohmatob2024tale}, obtaining $\\edd \\leq 5$, which agrees with the empirical observation of $\\edd = 4$ across three model families.\n\nOur contributions are:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Task formalization.} We define ordinal generation depth estimation as a new problem and construct a systematic benchmark spanning 3 model families $\\times$ 3 decoding strategies $\\times$ 4 depths, with scale validation at 14B parameters.\n    \\item \\textbf{Depth Degradation Atlas.} We provide the first systematic empirical characterization of how text statistical properties evolve across recursive depths, revealing (a) perplexity tail statistics as universal depth markers, (b) non-uniform inter-depth distances, (c) the \\edd{} boundary, and (d) strategy-dependent feature trajectory reversal with an identified causal mechanism.\n    \\item \\textbf{Theoretical grounding.} We derive an \\edd{} upper bound from model collapse theory that produces three verifiable predictions, all confirmed by our experiments: $\\edd \\in [3,5]$, per-depth \\texttt{p90\\_ppl} decay of 15--25\\%, and temperature-to-nucleus convergence ratio $> 1$.\n    \\item \\textbf{Practical framework.} We demonstrate that feature-based classifiers achieve 70--85\\% four-class accuracy, that existing binary detectors fail at ordinal estimation (30--38\\%), and that a two-stage strategy-aware pipeline improves cross-strategy transfer by +11.5pp.\n\\end{itemize}\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Model collapse and recursive generation.}\n\\citet{shumailov2024model} demonstrate that iterative training on model-generated data causes progressive loss of distributional tail mass, termed model collapse. \\citet{alemohammad2024selfconsuming} and \\citet{dohmatob2024tale} provide theoretical frameworks quantifying the contraction rate of output distributions under recursive self-consumption. \\citet{gerstgrasser2024model} extend these results to multi-generational settings with partial synthetic data mixing. \\citet{drayson2025investigatinggeneralizabilitygenerationdegradation} investigate cross-model generalization of degradation patterns. These studies characterize \\emph{what happens} during recursive generation but assume depth is known. Our work addresses the inverse problem: estimating depth from text alone, and connects the observed feature universality to the tail erosion mechanism.\n\n\\paragraph{Machine-generated text detection.}\nBinary detectors span statistical methods \\citep{hans2024binoculars,bao2024fastdetectgpt,mitchell2023detectgpt}, watermarking approaches \\citep{kirchenbauer2023watermark}, and learned classifiers \\citep{liang2024monitoring}. \\citet{uchendu2020authorship} frame multi-source attribution as identifying which model generated a text but do not consider recursion depth. \\citet{garcesarias2025decoding} show that decoding strategy significantly affects detector performance, a finding our strategy-dependent results corroborate and extend to the ordinal setting. EditLens \\citep{wang2024editlens} estimates the extent of single-pass AI editing but does not address recursive multi-generational depth.\n\n\\paragraph{Data curation and quality estimation.}\nData selection methods such as DSIR \\citep{xie2023dsir} and QuRating \\citep{wettig2024qurating} score data quality along continuous dimensions but do not model recursive generation depth. Our depth estimates could complement these approaches by providing an orthogonal quality axis.\n\n\\paragraph{Decoding strategies and output distributions.}\n\\citet{holtzman2020curious} introduce nucleus sampling and characterize the degeneration problem in open-ended generation. The interaction between decoding strategy and downstream text properties is well-documented \\citep{garcesarias2025decoding}, but its effect on recursive depth estimation has not been studied. Our Atlas reveals that this interaction is not merely quantitative (signal attenuation) but qualitative (feature trajectory reversal under temperature sampling).\n\n% ============================================================\n% 3. TASK FORMALIZATION\n% ============================================================\n\\section{Task Formalization}\n\n\\paragraph{Problem definition.}\nLet $\\mathcal{M}_0$ denote a pre-trained language model and $\\mathcal{D}_0$ a corpus of human-written text. A \\emph{recursive generation chain} of depth $K$ is defined by the iteration: for $k = 0, 1, \\ldots, K-1$, fine-tune $\\mathcal{M}_k$ on $\\mathcal{D}_k$ to obtain $\\mathcal{M}_{k+1}$, then sample from $\\mathcal{M}_{k+1}$ to produce $\\mathcal{D}_{k+1}$. We assign depth label $d = 0$ to human-written text $\\mathcal{D}_0$ and depth $d = k$ to text in $\\mathcal{D}_k$.\n\nGiven a text passage $x$ and access to a reference language model $\\mathcal{M}_{\\mathrm{ref}}$, ordinal generation depth estimation is the task of predicting $\\hat{d}(x) \\in \\{0, 1, \\ldots, K\\}$.\n\n\\paragraph{Feature extraction.}\nWe extract 19 statistical features from the per-token log-probability distribution computed by $\\mathcal{M}_{\\mathrm{ref}}$. These features span four families: (1) perplexity statistics (mean, median, p75, p90, p95, variance of per-token perplexity), (2) surprisal statistics (mean, variance, skewness, kurtosis, range of per-token surprisal), (3) repetition indicators (2/3/4-gram repetition rates), and (4) diversity metrics (type-token ratio, hapax ratio, entropy of token distribution, mean sentence length). For the 3-model benchmark, each model serves as its own reference model in within-model evaluations; in cross-model experiments, Pythia-1.4B serves as the default reference model.\n\n\\paragraph{Reference model and circularity.}\nUsing the generating model as its own reference creates a potential circularity concern: the reference model ``recognizes'' its own output distribution. We address this through cross-model leave-one-out (LOO) evaluation, where the reference model is never the generating model. Cross-model LOO accuracy (mean 66.4\\%) confirms that depth signal is not purely an artifact of model self-recognition, though within-model accuracy is higher (mean 78.3\\%), indicating that model-specific distributional knowledge contributes to but is not necessary for depth estimation.\n\n\\paragraph{Effective Discriminable Depth (\\edd).}\nWe define the \\edd{} at threshold $T$ as the maximum depth $d^*$ such that adjacent-depth pairwise AUC exceeds $T$ for all pairs up to $d^*$:\n\\begin{equation}\n    \\edd(T) = \\max \\{ d^* : \\mathrm{AUC}(d_i, d_{i+1}) \\geq T, \\; \\forall \\, i < d^* \\}.\n\\end{equation}\n\\edd{} quantifies the practical horizon of ordinal depth estimation: beyond \\edd, adjacent depths become statistically indistinguishable with current features.\n\n% ============================================================\n% 4. THEORETICAL ANALYSIS\n% ============================================================\n\\section{Theoretical Analysis}\n\nWe ground the empirical Atlas in model collapse theory, deriving three verifiable predictions that connect distributional contraction to depth estimation feasibility.\n\n\\subsection{Tail Erosion and Feature Dominance}\n\n\\citet{shumailov2024model} prove that recursive fine-tuning progressively erodes the tails of the output distribution: high-perplexity tokens lose probability mass while low-perplexity tokens gain mass at each recursive step. This tail erosion mechanism directly explains why perplexity tail statistics (\\texttt{p90\\_ppl}, \\texttt{var\\_surprisal}) dominate the feature ranking across all model-strategy combinations. Central tendency measures (mean perplexity) are less sensitive because the bulk of the distribution shifts slowly relative to the tails.\n\n\\textbf{Prediction 1.} Per-depth \\texttt{p90\\_ppl} should decrease by 15--25\\% per generation depth, reflecting the exponential tail compression. \\emph{Observed}: median \\texttt{p90\\_ppl} decreases 18--22\\% per depth across all three models (Section~\\ref{sec:results}).\n\n\\subsection{\\edd{} Upper Bound from Contraction Rates}\n\n\\citet{dohmatob2024tale} formalize recursive generation as a contractive mapping on distributional space with contraction rate $\\alpha < 1$. The output distribution at depth $k$ satisfies $\\|P_k - P_\\infty\\| \\leq C \\cdot \\alpha^k$, where $P_\\infty$ is the fixed-point distribution.\n\nA classifier can distinguish depth $k$ from depth $k+1$ only if the distributional distance exceeds the classifier's noise floor $\\epsilon$. This yields:\n\\begin{equation}\n    \\edd \\leq \\left\\lceil \\frac{\\log \\epsilon}{\\log \\alpha} \\right\\rceil.\n\\end{equation}\n\nFrom the empirical fine-tuning loss decay across depths (2.27 $\\to$ 1.65 $\\to$ 1.23 for 1B models), we estimate $\\alpha \\approx 0.72$. Setting $\\epsilon = 0.05$ (corresponding to an AUC threshold of 0.75), we obtain $\\edd \\leq \\lceil \\log(0.05) / \\log(0.72) \\rceil = 5$.\n\n\\textbf{Prediction 2.} $\\edd \\in [3, 5]$. \\emph{Observed}: $\\edd = 4$ across all three model families at threshold $T = 0.75$ (d3v4 AUC clusters near 0.75; d4v5 AUC uniformly falls below 0.70).\n\n\\subsection{Strategy-Dependent Convergence}\n\nTemperature sampling applies uniform scaling to logits, while nucleus and top-$k$ sampling truncate the distribution. Uniform scaling accelerates convergence to the fixed-point distribution because it amplifies the contraction at every point in the distribution simultaneously, rather than selectively truncating. We formalize this as a multiplicative factor on the effective contraction rate:\n\\[\n    \\alpha_{\\mathrm{temp}} = \\alpha \\cdot \\gamma, \\quad \\gamma \\approx 1.35 \\quad (\\text{estimated from empirical loss curves}).\n\\]\n\nThis predicts that temperature-sampled text at depth $N$ should exhibit feature statistics similar to nucleus-sampled text at depth $N+1$.\n\n\\textbf{Prediction 3.} Temperature-to-nucleus convergence ratio $> 1$. \\emph{Observed}: ratio $\\approx 1.35$; GPT-2 XL temp09 d1 \\texttt{p90\\_ppl} median = 92.2, which falls within the nucleus/top-$k$ d2 range of 65--92.\n\n% ============================================================\n% 5. EXPERIMENTAL SETUP\n% ============================================================\n\\section{Experimental Setup}\n\n\\paragraph{Benchmark construction.}\nWe construct recursive generation chains for three 1--1.5B parameter models: GPT-2 XL (1.5B), Pythia-1.4B, and OLMo-1B. For each model, we fine-tune with LoRA on the previous depth's generated text and sample the next depth using three decoding strategies: nucleus sampling ($p = 0.95$), temperature sampling ($\\tau = 0.9$), and top-$k$ sampling ($k = 50$). This produces $3 \\times 3 = 9$ independent chains, each spanning depths d0--d3, yielding $9 \\times 4 \\times 5000 = 180{,}000$ text passages.\n\n\\paragraph{Scale validation.}\nWe additionally construct a Qwen2.5-14B chain using FP16 precision (no quantization) with LoRA fine-tuning on a 96GB RTX PRO 6000 GPU, spanning depths d0--d3 with nucleus sampling, to validate that depth signal persists at mainstream model scale.\n\n\\paragraph{Classifiers.}\nWe evaluate Random Forest (RF, 100 trees) and Logistic Regression (LR) as representative non-parametric and linear classifiers. All results use 5-fold cross-validation with bootstrap 95\\% confidence intervals computed from fold-level estimates (1000 resamples).\n\n\\paragraph{Baselines.}\nWe calibrate Binoculars \\citep{hans2024binoculars} and Fast-DetectGPT \\citep{bao2024fastdetectgpt} continuous scores for ordinal depth estimation using (a) equal-quantile binning and (b) oracle threshold optimization. The chance baseline for 4-class classification is 25\\%.\n\n% ============================================================\n% 6. RESULTS\n% ============================================================\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Depth Degradation Atlas: The 3$\\times$3 Benchmark}\n\nTable~\\ref{tab:atlas} presents the core Atlas results. RF classifiers achieve 70--85\\% four-class accuracy across all nine model-strategy combinations, with GPT-2 XL under temperature sampling reaching the highest accuracy of 85.4\\%. Bootstrap 95\\% CIs are tight (mean width 1.8pp, max 2.5pp), and all lower bounds exceed 68\\%, well above chance (25\\%).\n\nThree patterns emerge. First, \\texttt{p90\\_ppl} and \\texttt{var\\_surprisal} rank among the top-4 features in all nine settings, confirming the universality of tail-based depth markers. Second, inter-depth discrimination decreases monotonically: d0v1 AUC $\\approx$ 0.99, d1v2 AUC $\\approx$ 0.86, d2v3 AUC $\\approx$ 0.80. Third, decoding strategies produce a three-tier pattern: temperature enhances signal (mean accuracy 82.6\\%), nucleus provides a stable baseline (mean 79.0\\%), and top-$k$ attenuates signal (mean 73.2\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{Depth Degradation Atlas: 4-class RF accuracy (\\%) with bootstrap 95\\% CIs across 3 models $\\times$ 3 decoding strategies. All results use 5-fold CV on 19 statistical features. Chance = 25\\%.}\n\\label{tab:atlas}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Nucleus} & \\textbf{Temp ($\\tau$=0.9)} & \\textbf{Top-$k$ ($k$=50)} \\\\\n\\midrule\n\\textbf{Pythia-1.4B} & 78.2 \\scriptsize{[76.9, 79.4]} & 76.3 \\scriptsize{[74.9, 77.6]} & 69.7 \\scriptsize{[68.2, 71.1]} \\\\\n\\textbf{OLMo-1B}     & 78.9 \\scriptsize{[77.6, 80.2]} & 82.2 \\scriptsize{[80.8, 83.5]} & 74.2 \\scriptsize{[72.8, 75.6]} \\\\\n\\textbf{GPT-2 XL}    & 83.9 \\scriptsize{[82.6, 85.2]} & 85.4 \\scriptsize{[84.1, 86.7]} & 75.7 \\scriptsize{[74.3, 77.0]} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Scale Robustness at 14B}\n\nTable~\\ref{tab:14b} presents results for Qwen2.5-14B under clean FP16 conditions (no quantization). The 14B model achieves 79\\% four-class accuracy [77.8, 80.2], falling within the range of the three 1B-scale models (69.7--85.4\\%). The adjacent-depth AUC profile mirrors the 1B pattern: d0v1 = 0.991, d1v2 = 0.87, d2v3 = 0.82. The top-4 features are identical to the 1B models (overlap = 4/4): \\texttt{p90\\_ppl}, \\texttt{var\\_surprisal}, \\texttt{p75\\_ppl}, and \\texttt{mean\\_surprisal}. Per-class recall follows the expected depth-dependent pattern: d0 = 98\\%, d1 = 84\\%, d2 = 62\\%, d3 = 72\\%.\n\nThese results confirm that the depth signal and feature universality are not limited to small models. The fine-tuning loss trajectory at 14B (2.35 $\\to$ 1.58 $\\to$ 1.15) is flatter than at 1B, consistent with larger residual capacity resisting catastrophic distributional shift, but insufficient to prevent tail erosion.\n\n\\begin{table}[t]\n\\centering\n\\caption{Scale robustness: Qwen2.5-14B FP16 vs 1B-scale models. Feature overlap refers to concordance of top-4 ranked features with the 1B-model consensus.}\n\\label{tab:14b}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{4-class Acc} & \\textbf{d1v2 AUC} & \\textbf{d2v3 AUC} & \\textbf{Top-4 Overlap} \\\\\n\\midrule\nPythia-1.4B (nucleus) & 78.2 & 0.86 & 0.80 & --- \\\\\nOLMo-1B (nucleus)     & 78.9 & 0.87 & 0.81 & --- \\\\\nGPT-2 XL (nucleus)    & 83.9 & 0.92 & 0.84 & --- \\\\\n\\midrule\nQwen2.5-14B (nucleus) & 79.0 & 0.87 & 0.82 & 4/4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Binary Detectors Fail at Ordinal Estimation}\n\nTable~\\ref{tab:baseline} compares existing binary detectors repurposed for ordinal depth estimation against our feature-based approach. Both Binoculars and Fast-DetectGPT perform near chance on the ordinal task. Even with oracle threshold optimization (which uses test-set depth distribution information), the best binary detector achieves only 38\\%, compared to 78.3\\% for the RF 19-feature classifier. The d1v2 AUC values (0.54--0.56) are barely above chance (0.50), confirming that binary detector scores do not encode ordinal depth gradients. A score combination (Binoculars + Fast-DetectGPT features) reaches 40\\%, still 38pp below the feature-based method.\n\nBinary detectors are designed to capture a single boundary (real vs.\\ synthetic). Their continuous scores saturate beyond d0: d1, d2, and d3 texts all register as ``synthetic'' with similar confidence, erasing the ordinal structure that tail statistics preserve.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ordinal baseline comparison: binary detectors calibrated for 4-class depth estimation vs.\\ feature-based methods. Quantile: equal-quantile binning; Oracle: optimal threshold search using test-set distribution.}\n\\label{tab:baseline}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{4-class Acc} & \\textbf{d1v2 AUC} & \\textbf{d2v3 AUC} \\\\\n\\midrule\nChance & 25.0 & 0.50 & 0.50 \\\\\nBinoculars (quantile)   & 32.0 & 0.56 & 0.52 \\\\\nBinoculars (oracle)     & 38.0 & 0.56 & 0.52 \\\\\nFast-DetectGPT (quantile) & 30.0 & 0.54 & 0.51 \\\\\nFast-DetectGPT (oracle) & 36.0 & 0.54 & 0.51 \\\\\nCombined (oracle)       & 40.0 & --- & --- \\\\\n\\midrule\nRF 19-feature           & \\textbf{78.3} & \\textbf{0.86} & \\textbf{0.80} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Theoretical Predictions vs.\\ Empirical Results}\n\nTable~\\ref{tab:theory} summarizes the three theoretical predictions and their empirical verification. All three predictions fall within the theoretically derived ranges, supporting the connection between model collapse contraction theory and the practical feasibility of depth estimation.\n\nThe agreement between the predicted \\edd{} range of [3, 5] and the observed \\edd{} = 4 provides more than post-hoc confirmation: it establishes a principled basis for understanding why ordinal depth estimation works at shallow depths but faces fundamental limits. As recursive generation contracts the output distribution toward a fixed point, the remaining inter-depth distributional distance eventually falls below any classifier's discrimination threshold.\n\n\\begin{table}[t]\n\\centering\n\\caption{Theoretical predictions derived from model collapse contraction theory vs.\\ empirical observations. $\\alpha = 0.72$ is estimated from fine-tuning loss decay curves.}\n\\label{tab:theory}\n\\small\n\\begin{tabular}{p{4.5cm}cc}\n\\toprule\n\\textbf{Prediction} & \\textbf{Theoretical} & \\textbf{Empirical} \\\\\n\\midrule\n\\edd{} range & [3, 5] & 4 (all 3 models) \\\\\n\\texttt{p90\\_ppl} decay / depth & 15--25\\% & 18--22\\% \\\\\nTemp/nucleus convergence ratio & $> 1$ & $\\approx 1.35$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Strategy Transfer and Two-Stage Pipeline}\n\nNaive cross-strategy leave-one-out transfer yields 59.1\\% mean accuracy, with temperature holdout exhibiting d1v2 AUC reversal (GPT-2 XL: 0.13, OLMo: 0.25). This reversal is not noise: Section~4.3 explains the causal mechanism (temperature's uniform logit scaling accelerates convergence, so temp09 depth $N$ features approximate nucleus depth $N+1$).\n\nThe two-stage pipeline first identifies the decoding strategy (57.8\\% accuracy on the same 19 features), then routes to strategy-conditioned depth classifiers. This improves mean cross-strategy accuracy from 59.1\\% to 70.5\\% (+11.5pp). Per-model results: GPT-2 XL 73.0\\%, OLMo 69.4\\%, Pythia 69.3\\%. The oracle ceiling (perfect strategy identification) is 78.3\\%.\n\n\\paragraph{Strategy-dependent d1v2 AUC.}\nWe report per-strategy cross-strategy d1v2 AUC for transparency. When temperature is the holdout strategy, d1v2 AUC drops to 0.13--0.25, reflecting the structural distributional shift identified in Section~4.3. Z-score normalization improves overall LR cross-strategy accuracy from 25\\% to 61\\% but does not recover pairwise d1v2 AUC (GPT-2 XL: 0.50 $\\to$ 0.24; OLMo: 0.50 $\\to$ 0.19), confirming that simple feature normalization cannot resolve a geometric distributional shift.\n\n% ============================================================\n% 7. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Wild-data ecological validity.}\nTo assess behavior on uncurated web text, we apply depth estimators trained on our controlled benchmark to 10K-sample subsets of C4, FineWeb, and RedPajama. The depth distribution is dominated by d0 predictions (78--85\\%), with false positive rates (non-d0 predictions on human-written web text) of 21.5\\% (C4), 18.0\\% (FineWeb), and 15.0\\% (RedPajama). Cross-model agreement on d0 predictions is high (92\\%). Inspection of misclassified samples reveals that template, SEO, and boilerplate content shares statistical features with recursively generated text (high $n$-gram repetition, low surprisal variance). FPR correlates inversely with the strictness of the source corpus's cleaning pipeline (RedPajama $<$ FineWeb $<$ C4). This suggests that depth estimation features capture a general text quality gradient, with template-heavy web content occupying a similar feature-space region as shallow recursive generation. Full results appear in Appendix Tables~\\ref{tab:wild} and~\\ref{tab:wild_agreement}.\n\n\\paragraph{API model generalization.}\nFine-tuned GPT-4o-mini recursive chains achieve 58\\% four-class accuracy with d0v1 AUC = 0.93 and d1v2 AUC = 0.72. Prompted (non-fine-tuned) recursive chains yield 45\\% accuracy. Both exceed chance (25\\%), indicating that depth signal persists in RLHF-aligned commercial models, though attenuated. The feature profile of fine-tuned chains overlaps 3/4 top features with base models (\\texttt{p90\\_ppl}, \\texttt{var\\_surprisal}, \\texttt{mean\\_ppl}), while prompted chains show a shifted profile (\\texttt{surprisal\\_range} replaces \\texttt{p75\\_ppl}), reflecting the additional constraints imposed by prompt engineering on the generation process. Full results appear in Appendix Table~\\ref{tab:api}.\n\n\\paragraph{Negative results: end-to-end learning.}\nWe systematically explored contrastive ordinal learning (DCOL) using RoBERTa-large embeddings across six architecture variants (v1--v6). All variants failed to outperform feature-based methods, with the best achieving 64.5\\% accuracy versus 78.2\\% for the RF baseline. Failure modes included embedding collapse (adjacent-depth cosine similarity $> 0.95$), catastrophic forgetting, and gradient instability. The consistent underperformance of neural end-to-end approaches (DeBERTa: 58.3\\%, RoBERTa: 59.5\\%, DCOL best: 64.5\\%) compared to feature-based methods (RF: 78.3\\%, LR: 76.0\\%) suggests that explicit statistical features capture depth-relevant distributional properties more effectively than learned representations when inter-class boundaries in embedding space are narrow. Full analysis appears in Appendix Table~\\ref{tab:dcol}.\n\n\\paragraph{Depth-graduated curation.}\nPredicted depth provides a finer-grained quality proxy than binary real/synthetic labels. Rather than filtering all synthetic content, curation pipelines could weight training samples inversely to predicted depth, retaining beneficial shallow-generation data while downweighting deeply recursive text. The monotonic relationship between depth and classifier accuracy in our 3$\\times$3 matrix supports this graduated approach, though full experimental validation of downstream training effects is left to future work.\n\n% ============================================================\n% 8. LIMITATIONS\n% ============================================================\n\\section{Limitations}\n\n\\textbf{Controlled vs.\\ wild domain shift.} Our benchmark uses LoRA fine-tuning chains under controlled conditions. Real-world recursive generation involves heterogeneous models, varying data mixtures, and unknown generation parameters. While wild-data calibration (Section~7) and prompted generation experiments provide evidence of ecological validity, the controlled-to-wild generalization gap remains only partially characterized.\n\n\\textbf{Cross-strategy deployment.} Cross-strategy deployment requires knowledge of the target decoding strategy. Without strategy metadata, d1/d2 predictions may be inverted when the unknown strategy is temperature-based, due to the structural distributional shift identified in Section~4.3. The two-stage pipeline mitigates this partially (+11.5pp), but strategy classification accuracy (57.8\\%) remains a bottleneck. Whether more sophisticated domain adaptation methods can fully resolve the temperature-induced d1v2 boundary reversal remains an open problem.\n\n\\textbf{\\edd{} statistical significance.} While d3v4 AUC consistently clusters near the 0.75 threshold across all three models (0.750--0.784), only Pythia achieves statistical significance ($p = 0.001$); OLMo is marginal ($p = 0.091$) and GPT-2 XL is not significant ($p = 0.505$). D4v5 AUC uniformly falls below 0.70 (0.681--0.694). We report \\edd{} = 4 based on directional consistency rather than universal statistical significance.\n\n\\textbf{Reference model dependency.} Feature extraction requires access to a reference language model. Cross-model LOO accuracy (66.4\\%) is lower than within-model accuracy (78.3\\%), indicating partial reference model dependence. The choice of reference model affects absolute accuracy but not the qualitative patterns (feature ranking, strategy effects, \\edd{}).\n\n% ============================================================\n% 9. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe formalized ordinal generation depth estimation as a new task, addressing the gap between binary synthetic text detection and the reality of multi-generational recursive content in web-scraped corpora. Our Depth Degradation Atlas provides the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, spanning three model families, three decoding strategies, and scales from 1B to 14B parameters. The theoretical connection to model collapse contraction rates grounds the Atlas in distributional theory and produces verifiable predictions that match our observations. Feature-based classifiers achieve 70--85\\% four-class accuracy, existing binary detectors fail at ordinal estimation (30--38\\%), and a two-stage strategy-aware pipeline addresses the cross-strategy deployment challenge. We release our benchmark and code to support future work on recursive depth estimation and depth-aware data curation.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Alemohammad et~al.(2024)]{alemohammad2024selfconsuming}\nS.~Alemohammad, J.~Casco-Rodriguez, L.~Luzi, A.~I. Ahmed, D.~Abedi, R.~Baraniuk, et~al.\n\\newblock Self-consuming generative models go {MAD}.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Bao et~al.(2024)]{bao2024fastdetectgpt}\nG.~Bao, Y.~Zhao, Z.~Teng, L.~Yang, and M.~Zhang.\n\\newblock Fast-{DetectGPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024tale}\nE.~Dohmatob, P.~Feng, and Q.~Yang.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock \\emph{arXiv preprint arXiv:2402.07043}, 2024.\n\n\\bibitem[Drayson et~al.(2025)]{drayson2025investigatinggeneralizabilitygenerationdegradation}\nN.~Drayson, Y.~Du, and A.~Sherborne.\n\\newblock Investigating the generalizability of generation degradation.\n\\newblock In \\emph{EMNLP}, 2025.\n\n\\bibitem[Garc{\\'e}s~Arias et~al.(2025)]{garcesarias2025decoding}\nL.~Garc{\\'e}s~Arias, S.~Mille, and L.~Padro.\n\\newblock On the impact of decoding strategies on the detectability of machine-generated text.\n\\newblock In \\emph{COLING}, 2025.\n\n\\bibitem[Gerstgrasser et~al.(2024)]{gerstgrasser2024model}\nM.~Gerstgrasser, R.~Schaeffer, A.~Dey, R.~Rafailov, H.~Sleiman, J.~Hughes, T.~Korbak, R.~Agarwal, D.~Levine, et~al.\n\\newblock Is model collapse inevitable? {Breaking} the curse of recursion by accumulating real and synthetic data.\n\\newblock \\emph{arXiv preprint arXiv:2404.01413}, 2024.\n\n\\bibitem[Hans et~al.(2024)]{hans2024binoculars}\nA.~Hans, A.~Schwarzschild, V.~Cherepanova, H.~Kazemi, A.~Saha, M.~Goldblum, J.~Geiping, and T.~Goldstein.\n\\newblock Spotting {LLMs} with {Binoculars}: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Holtzman et~al.(2020)]{holtzman2020curious}\nA.~Holtzman, J.~Buys, L.~Du, M.~Forbes, and Y.~Choi.\n\\newblock The curious case of neural text degeneration.\n\\newblock In \\emph{ICLR}, 2020.\n\n\\bibitem[Kirchenbauer et~al.(2023)]{kirchenbauer2023watermark}\nJ.~Kirchenbauer, J.~Geiping, Y.~Wen, J.~Katz, I.~Miers, and T.~Goldstein.\n\\newblock A watermark for large language models.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Liang et~al.(2024)]{liang2024monitoring}\nW.~Liang, M.~Yuksekgonul, Y.~Mao, E.~Wu, and J.~Zou.\n\\newblock {GPT} detectors are biased against non-native {English} writers.\n\\newblock In \\emph{Patterns}, 4(7), 2024.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nE.~Mitchell, Y.~Lee, A.~Khazatsky, C.~D. Manning, and C.~Finn.\n\\newblock {DetectGPT}: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024model}\nI.~Shumailov, Z.~Shumaylov, Y.~Zhao, N.~Papernot, R.~Anderson, and Y.~Gal.\n\\newblock {AI} models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 631:755--759, 2024.\n\n\\bibitem[Uchendu et~al.(2020)]{uchendu2020authorship}\nA.~Uchendu, T.~Le, K.~Shu, and D.~Lee.\n\\newblock Authorship attribution for neural text generation.\n\\newblock In \\emph{EMNLP}, 2020.\n\n\\bibitem[Wang et~al.(2024)]{wang2024editlens}\nM.~Wang, Z.~Wang, B.~Li, and J.~Chen.\n\\newblock {EditLens}: Evaluating and predicting editing on {AI}-generated texts.\n\\newblock \\emph{arXiv preprint arXiv:2404.17435}, 2024.\n\n\\bibitem[Wettig et~al.(2024)]{wettig2024qurating}\nA.~Wettig, A.~Gao, Z.~Zhong, and D.~Chen.\n\\newblock {QuRating}: Selecting high-quality data for training language models.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Xie et~al.(2023)]{xie2023dsir}\nS.~M. Xie, S.~Santurkar, T.~Ma, and P.~Liang.\n\\newblock Data selection for language models via importance resampling.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\bibitem[Radford et~al.(2019)]{radford2019gpt2}\nA.~Radford, J.~Wu, R.~Child, D.~Luan, D.~Amodei, and I.~Sutskever.\n\\newblock Language models are unsupervised multitask learners.\n\\newblock \\emph{OpenAI Technical Report}, 2019.\n\n\\bibitem[Biderman et~al.(2023)]{biderman2023pythia}\nS.~Biderman, H.~Schoelkopf, Q.~Anthony, H.~Bradley, K.~O'Brien, E.~Hallahan, M.~A. Khan, S.~Purohit, U.~S. Prashanth, E.~Raff, et~al.\n\\newblock {Pythia}: A suite for analyzing large language models across training and scaling.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Groeneveld et~al.(2024)]{groeneveld2024olmo}\nD.~Groeneveld, I.~Beltagy, P.~Walsh, A.~Bhagia, R.~Kinney, O.~Tafjord, A.~Jha, H.~Ivison, I.~Magnusson, Y.~Wang, et~al.\n\\newblock {OLMo}: Accelerating the science of language models.\n\\newblock In \\emph{ACL}, 2024.\n\n\\bibitem[Hu et~al.(2022)]{hu2022lora}\nE.~J. Hu, Y.~Shen, P.~Wallis, Z.~Allen-Zhu, Y.~Li, S.~Wang, L.~Wang, and W.~Chen.\n\\newblock {LoRA}: Low-rank adaptation of large language models.\n\\newblock In \\emph{ICLR}, 2022.\n\n\\bibitem[Breiman(2001)]{breiman2001randomforests}\nL.~Breiman.\n\\newblock Random forests.\n\\newblock \\emph{Machine Learning}, 45(1):5--32, 2001.\n\n\\bibitem[Yang et~al.(2024)]{yang2024qwen2}\nA.~Yang, B.~Yang, B.~Hui, B.~Zheng, B.~Yu, C.~Zhou, et~al.\n\\newblock {Qwen2} technical report.\n\\newblock \\emph{arXiv preprint arXiv:2407.10671}, 2024.\n\n\\bibitem[Cao et~al.(2020)]{cao2020coral}\nW.~Cao, V.~Mirjalili, and S.~Raschka.\n\\newblock Rank consistent ordinal regression for neural networks with application to age estimation.\n\\newblock \\emph{Pattern Recognition Letters}, 140:325--331, 2020.\n\n\\bibitem[Liang et~al.(2023)]{liang2023helm}\nP.~Liang, R.~Bommasani, T.~Lee, D.~Tsipras, D.~Soylu, M.~Yasunaga, Y.~Zhang, D.~Narayanan, et~al.\n\\newblock Holistic evaluation of language models.\n\\newblock \\emph{TMLR}, 2023.\n\n\\bibitem[Hendrycks et~al.(2021)]{hendrycks2021mmlu}\nD.~Hendrycks, C.~Burns, S.~Basart, A.~Zou, M.~Mazeika, D.~Song, and J.~Steinhardt.\n\\newblock Measuring massive multitask language understanding.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Achiam et~al.(2023)]{achiam2023gpt4}\nJ.~Achiam, S.~Adler, S.~Agarwal, L.~Ahmad, I.~Akkaya, F.~L.~Aleman, et~al.\n\\newblock {GPT-4} technical report.\n\\newblock \\emph{arXiv preprint arXiv:2303.08774}, 2023.\n\n\\end{thebibliography}\n\n% ============================================================\n% APPENDIX\n% ============================================================\n\\appendix\n\n\\section{Wild-Data Calibration}\n\\label{app:wild}\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth distribution predictions on wild web-crawl data (10K samples each, Pythia-1.4B reference model). FPR = percentage of samples predicted as non-d0.}\n\\label{tab:wild}\n\\small\n\\begin{tabular}{lcccc|c}\n\\toprule\n\\textbf{Corpus} & \\textbf{d0 (\\%)} & \\textbf{d1 (\\%)} & \\textbf{d2 (\\%)} & \\textbf{d3 (\\%)} & \\textbf{FPR (\\%)} \\\\\n\\midrule\nC4         & 78.5 & 19.8 & 1.2 & 0.5 & 21.5 \\\\\nFineWeb    & 82.0 & 16.8 & 0.8 & 0.4 & 18.0 \\\\\nRedPajama  & 85.0 & 13.5 & 1.0 & 0.5 & 15.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-model agreement on wild-data d0 predictions across three reference models.}\n\\label{tab:wild_agreement}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nd0 agreement (3 models) & 92\\% \\\\\nPrimary misclassification type & template/SEO/boilerplate \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFPR inversely correlates with corpus cleaning strictness: RedPajama (most filtered) $<$ FineWeb $<$ C4. Misclassified samples are predominantly template-heavy, SEO-optimized, or boilerplate content, whose low lexical diversity and high repetition rates place them in the same feature-space region as shallow recursive generation output.\n\n\\section{API Model Depth Estimation}\n\\label{app:api}\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth estimation on GPT-4o-mini recursive chains. Fine-tuned: LoRA fine-tuning API chain. Prompted: iterative rewrite prompting without fine-tuning.}\n\\label{tab:api}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Chain Type} & \\textbf{4-class Acc} & \\textbf{d0v1 AUC} & \\textbf{d1v2 AUC} \\\\\n\\midrule\nFine-tuned chain & 58.0 & 0.93 & 0.72 \\\\\nPrompted chain   & 45.0 & 0.78 & 0.61 \\\\\n\\midrule\nBase model RF (reference) & 78.3 & 0.99 & 0.86 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFine-tuned chain top features: \\texttt{p90\\_ppl}, \\texttt{var\\_surprisal}, \\texttt{mean\\_ppl}, \\texttt{p75\\_ppl} (3/4 overlap with base models). Prompted chain top features: \\texttt{var\\_surprisal}, \\texttt{p90\\_ppl}, \\texttt{surprisal\\_range}, \\texttt{mean\\_surprisal} (shifted profile reflecting prompt-mediated constraints). Both settings exceed chance (25\\%), confirming that RLHF regularization attenuates but does not eliminate depth signal.\n\n\\section{End-to-End vs.\\ Feature-Based Methods}\n\\label{app:dcol}\n\n\\begin{table}[h]\n\\centering\n\\caption{Comparison of end-to-end neural methods vs.\\ feature-based classifiers. DCOL v1--v6 explored contrastive ordinal learning with RoBERTa-large embeddings; all variants underperformed feature-based baselines.}\n\\label{tab:dcol}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{4-class Acc (\\%)} & \\textbf{Category} \\\\\n\\midrule\nDeBERTa (fine-tuned)     & 58.3 & End-to-end \\\\\nRoBERTa (fine-tuned)     & 59.5 & End-to-end \\\\\nDCOL v6 (best variant)   & 64.5 & End-to-end \\\\\n\\midrule\nLR (19 features)         & 76.0 & Feature-based \\\\\nRF (19 features)         & \\textbf{78.3} & Feature-based \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe systematic underperformance of end-to-end methods is attributable to the narrow inter-class boundaries in embedding space. Adjacent recursive depths produce text with cosine similarity exceeding 0.95 in RoBERTa-large embedding space, leaving insufficient margin for contrastive learning to establish discriminative boundaries. Feature-based methods circumvent this by operating on hand-crafted statistics (tail perplexity, surprisal variance) that amplify the distributional differences that embedding-space distances compress. DCOL v1--v6 failure modes included: embedding collapse (v1--v2), out-of-memory (v3), catastrophic forgetting (v4), NaN gradients (v5), and overfitting to depth 0 (v6). This negative result suggests that ordinal depth estimation in text is fundamentally better suited to explicit statistical features than to end-to-end representation learning, at least with current transformer-based text encoders.\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c031414a-7e51-44de-9e94-0e7a19f3fff3",
  "isSidechain": false,
  "requestId": "req_011CbANL2cz1EAG4aHFzXCmD",
  "type": "assistant",
  "uuid": "1a980e3e-86b9-4de6-b3fd-05b351a051ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013kXKDEnGfG1xNvj7p9tpEQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 38192,
      "output_tokens": 13664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 683,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13664,
          "cache_read_input_tokens": 38192,
          "cache_creation_input_tokens": 683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 683
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

_source line 21 · 2026-05-18T16:46:57.612Z_

<details><summary>↩ Tool result · `toolu_014CQ1BEBzmd2YsnyUAvgEBf`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a980e3e-86b9-4de6-b3fd-05b351a051ab",
  "isSidechain": false,
  "promptId": "c9727216-6650-4282-92f3-6408303632c9",
  "type": "user",
  "uuid": "df0b5705-cb6b-47ec-a013-e2043b1c07da",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/paper.tex",
    "content": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb,amsfonts}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage[margin=2.5cm]{geometry}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{enumitem}\n\n\\newcommand{\\edd}{\\textsc{EDD}}\n\\newcommand{\\atlas}{\\textsc{Atlas}}\n\n\\title{Depth Degradation Atlas: Ordinal Estimation of Recursive Generation Depth from Text}\n\n\\author{Anonymous}\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n% ABSTRACT\n% ============================================================\n\\begin{abstract}\nWeb-scraped training corpora increasingly contain multi-generational synthetic content produced by uncontrolled model-data-model feedback loops. Existing detectors classify text as real or synthetic but discard ordinal depth information, a critical distinction since first-generation synthetic data can improve training while deeply recursive text drives distribution collapse. We formalize \\emph{ordinal generation depth estimation} as a new task: given text alone, predict how many recursive generation cycles it has undergone. We construct a multi-generational benchmark spanning three model families (GPT-2 XL, OLMo-1B, Pythia-1.4B), three decoding strategies (nucleus, temperature, top-$k$), and four depth levels (d0--d3), and provide the first \\emph{Depth Degradation Atlas}, a systematic empirical map of how text statistical properties evolve across recursive depths. Random Forest classifiers on 19 statistical features achieve 70--85\\% four-class accuracy (chance = 25\\%), with bootstrap 95\\% confidence intervals of $\\pm$1--2.5 percentage points. The depth signal persists at 14B scale (Qwen2.5-14B FP16, 79\\% accuracy) with identical top-4 features (4/4 overlap), eliminating the ``small model only'' concern. We derive a theoretical upper bound on Effective Discriminable Depth (\\edd) from model collapse contraction rates, predicting \\edd{} $\\in [3,5]$, which matches the empirical \\edd{} = 4 observed across all three model families. Existing binary detectors (Binoculars, Fast-DetectGPT) achieve only 30--38\\% when repurposed for ordinal estimation (near chance), confirming that ordinal depth estimation requires dedicated methods. A two-stage strategy-aware pipeline recovers +11.5 percentage points over naive cross-strategy transfer, addressing the deployment challenge.\n\\end{abstract}\n\n% ============================================================\n% 1. INTRODUCTION\n% ============================================================\n\\section{Introduction}\n\nLarge language models (LLMs) are increasingly used to generate training data for subsequent model generations, creating recursive feedback loops where synthetic text is consumed, learned from, and regenerated. Recent work has shown that such iterative retraining leads to progressive distribution collapse: output distributions lose tail diversity, rare tokens disappear, and text quality degrades monotonically with recursion depth \\citep{shumailov2024model,alemohammad2024selfconsuming,dohmatob2024tale}. Understanding \\emph{how deeply recursive} a piece of text is has direct practical implications for data curation, since shallow-generation synthetic data may be beneficial while deeply recursive text actively harms model training \\citep{gerstgrasser2024model}.\n\nExisting approaches to synthetic text detection frame the problem as binary classification: real versus machine-generated \\citep{hans2024binoculars,bao2024fastdetectgpt,liang2024monitoring}. This binary framing discards critical ordinal information. A text classified as ``synthetic'' could be first-generation output (potentially useful for training augmentation) or fifth-generation output (likely degraded beyond utility). Model collapse studies characterize degradation patterns but assume depth is known a priori \\citep{drayson2025investigatinggeneralizabilitygenerationdegradation,shumailov2024model}. No prior method estimates recursive generation depth from text alone.\n\nWe formalize \\emph{ordinal generation depth estimation} as a new task. Given a text passage and a reference language model, the goal is to predict the number of recursive fine-tune-and-generate cycles the text has undergone. This framing captures the monotonic degradation structure that binary detection ignores and provides a finer-grained quality signal for data curation pipelines.\n\nOur central empirical finding is that recursive generation depth leaves detectable statistical signatures in text, primarily in perplexity tail statistics. Across all nine model-strategy combinations in our benchmark, the 90th percentile of per-token perplexity (\\texttt{p90\\_ppl}) and surprisal variance (\\texttt{var\\_surprisal}) consistently rank among the top-4 discriminative features. This universality is not coincidental: we connect it to the tail erosion mechanism formalized by \\citet{shumailov2024model}, where each recursive cycle compresses the output distribution's tails. We derive a theoretical upper bound on the Effective Discriminable Depth (\\edd) from the contraction rate framework of \\citet{dohmatob2024tale}, obtaining $\\edd \\leq 5$, which agrees with the empirical observation of $\\edd = 4$ across three model families.\n\nOur contributions are:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Task formalization.} We define ordinal generation depth estimation as a new problem and construct a systematic benchmark spanning 3 model families $\\times$ 3 decoding strategies $\\times$ 4 depths, with scale validation at 14B parameters.\n    \\item \\textbf{Depth Degradation Atlas.} We provide the first systematic empirical characterization of how text statistical properties evolve across recursive depths, revealing (a) perplexity tail statistics as universal depth markers, (b) non-uniform inter-depth distances, (c) the \\edd{} boundary, and (d) strategy-dependent feature trajectory reversal with an identified causal mechanism.\n    \\item \\textbf{Theoretical grounding.} We derive an \\edd{} upper bound from model collapse theory that produces three verifiable predictions, all confirmed by our experiments: $\\edd \\in [3,5]$, per-depth \\texttt{p90\\_ppl} decay of 15--25\\%, and temperature-to-nucleus convergence ratio $> 1$.\n    \\item \\textbf{Practical framework.} We demonstrate that feature-based classifiers achieve 70--85\\% four-class accuracy, that existing binary detectors fail at ordinal estimation (30--38\\%), and that a two-stage strategy-aware pipeline improves cross-strategy transfer by +11.5pp.\n\\end{itemize}\n\n% ============================================================\n% 2. RELATED WORK\n% ============================================================\n\\section{Related Work}\n\n\\paragraph{Model collapse and recursive generation.}\n\\citet{shumailov2024model} demonstrate that iterative training on model-generated data causes progressive loss of distributional tail mass, termed model collapse. \\citet{alemohammad2024selfconsuming} and \\citet{dohmatob2024tale} provide theoretical frameworks quantifying the contraction rate of output distributions under recursive self-consumption. \\citet{gerstgrasser2024model} extend these results to multi-generational settings with partial synthetic data mixing. \\citet{drayson2025investigatinggeneralizabilitygenerationdegradation} investigate cross-model generalization of degradation patterns. These studies characterize \\emph{what happens} during recursive generation but assume depth is known. Our work addresses the inverse problem: estimating depth from text alone, and connects the observed feature universality to the tail erosion mechanism.\n\n\\paragraph{Machine-generated text detection.}\nBinary detectors span statistical methods \\citep{hans2024binoculars,bao2024fastdetectgpt,mitchell2023detectgpt}, watermarking approaches \\citep{kirchenbauer2023watermark}, and learned classifiers \\citep{liang2024monitoring}. \\citet{uchendu2020authorship} frame multi-source attribution as identifying which model generated a text but do not consider recursion depth. \\citet{garcesarias2025decoding} show that decoding strategy significantly affects detector performance, a finding our strategy-dependent results corroborate and extend to the ordinal setting. EditLens \\citep{wang2024editlens} estimates the extent of single-pass AI editing but does not address recursive multi-generational depth.\n\n\\paragraph{Data curation and quality estimation.}\nData selection methods such as DSIR \\citep{xie2023dsir} and QuRating \\citep{wettig2024qurating} score data quality along continuous dimensions but do not model recursive generation depth. Our depth estimates could complement these approaches by providing an orthogonal quality axis.\n\n\\paragraph{Decoding strategies and output distributions.}\n\\citet{holtzman2020curious} introduce nucleus sampling and characterize the degeneration problem in open-ended generation. The interaction between decoding strategy and downstream text properties is well-documented \\citep{garcesarias2025decoding}, but its effect on recursive depth estimation has not been studied. Our Atlas reveals that this interaction is not merely quantitative (signal attenuation) but qualitative (feature trajectory reversal under temperature sampling).\n\n% ============================================================\n% 3. TASK FORMALIZATION\n% ============================================================\n\\section{Task Formalization}\n\n\\paragraph{Problem definition.}\nLet $\\mathcal{M}_0$ denote a pre-trained language model and $\\mathcal{D}_0$ a corpus of human-written text. A \\emph{recursive generation chain} of depth $K$ is defined by the iteration: for $k = 0, 1, \\ldots, K-1$, fine-tune $\\mathcal{M}_k$ on $\\mathcal{D}_k$ to obtain $\\mathcal{M}_{k+1}$, then sample from $\\mathcal{M}_{k+1}$ to produce $\\mathcal{D}_{k+1}$. We assign depth label $d = 0$ to human-written text $\\mathcal{D}_0$ and depth $d = k$ to text in $\\mathcal{D}_k$.\n\nGiven a text passage $x$ and access to a reference language model $\\mathcal{M}_{\\mathrm{ref}}$, ordinal generation depth estimation is the task of predicting $\\hat{d}(x) \\in \\{0, 1, \\ldots, K\\}$.\n\n\\paragraph{Feature extraction.}\nWe extract 19 statistical features from the per-token log-probability distribution computed by $\\mathcal{M}_{\\mathrm{ref}}$. These features span four families: (1) perplexity statistics (mean, median, p75, p90, p95, variance of per-token perplexity), (2) surprisal statistics (mean, variance, skewness, kurtosis, range of per-token surprisal), (3) repetition indicators (2/3/4-gram repetition rates), and (4) diversity metrics (type-token ratio, hapax ratio, entropy of token distribution, mean sentence length). For the 3-model benchmark, each model serves as its own reference model in within-model evaluations; in cross-model experiments, Pythia-1.4B serves as the default reference model.\n\n\\paragraph{Reference model and circularity.}\nUsing the generating model as its own reference creates a potential circularity concern: the reference model ``recognizes'' its own output distribution. We address this through cross-model leave-one-out (LOO) evaluation, where the reference model is never the generating model. Cross-model LOO accuracy (mean 66.4\\%) confirms that depth signal is not purely an artifact of model self-recognition, though within-model accuracy is higher (mean 78.3\\%), indicating that model-specific distributional knowledge contributes to but is not necessary for depth estimation.\n\n\\paragraph{Effective Discriminable Depth (\\edd).}\nWe define the \\edd{} at threshold $T$ as the maximum depth $d^*$ such that adjacent-depth pairwise AUC exceeds $T$ for all pairs up to $d^*$:\n\\begin{equation}\n    \\edd(T) = \\max \\{ d^* : \\mathrm{AUC}(d_i, d_{i+1}) \\geq T, \\; \\forall \\, i < d^* \\}.\n\\end{equation}\n\\edd{} quantifies the practical horizon of ordinal depth estimation: beyond \\edd, adjacent depths become statistically indistinguishable with current features.\n\n% ============================================================\n% 4. THEORETICAL ANALYSIS\n% ============================================================\n\\section{Theoretical Analysis}\n\nWe ground the empirical Atlas in model collapse theory, deriving three verifiable predictions that connect distributional contraction to depth estimation feasibility.\n\n\\subsection{Tail Erosion and Feature Dominance}\n\n\\citet{shumailov2024model} prove that recursive fine-tuning progressively erodes the tails of the output distribution: high-perplexity tokens lose probability mass while low-perplexity tokens gain mass at each recursive step. This tail erosion mechanism directly explains why perplexity tail statistics (\\texttt{p90\\_ppl}, \\texttt{var\\_surprisal}) dominate the feature ranking across all model-strategy combinations. Central tendency measures (mean perplexity) are less sensitive because the bulk of the distribution shifts slowly relative to the tails.\n\n\\textbf{Prediction 1.} Per-depth \\texttt{p90\\_ppl} should decrease by 15--25\\% per generation depth, reflecting the exponential tail compression. \\emph{Observed}: median \\texttt{p90\\_ppl} decreases 18--22\\% per depth across all three models (Section~\\ref{sec:results}).\n\n\\subsection{\\edd{} Upper Bound from Contraction Rates}\n\n\\citet{dohmatob2024tale} formalize recursive generation as a contractive mapping on distributional space with contraction rate $\\alpha < 1$. The output distribution at depth $k$ satisfies $\\|P_k - P_\\infty\\| \\leq C \\cdot \\alpha^k$, where $P_\\infty$ is the fixed-point distribution.\n\nA classifier can distinguish depth $k$ from depth $k+1$ only if the distributional distance exceeds the classifier's noise floor $\\epsilon$. This yields:\n\\begin{equation}\n    \\edd \\leq \\left\\lceil \\frac{\\log \\epsilon}{\\log \\alpha} \\right\\rceil.\n\\end{equation}\n\nFrom the empirical fine-tuning loss decay across depths (2.27 $\\to$ 1.65 $\\to$ 1.23 for 1B models), we estimate $\\alpha \\approx 0.72$. Setting $\\epsilon = 0.05$ (corresponding to an AUC threshold of 0.75), we obtain $\\edd \\leq \\lceil \\log(0.05) / \\log(0.72) \\rceil = 5$.\n\n\\textbf{Prediction 2.} $\\edd \\in [3, 5]$. \\emph{Observed}: $\\edd = 4$ across all three model families at threshold $T = 0.75$ (d3v4 AUC clusters near 0.75; d4v5 AUC uniformly falls below 0.70).\n\n\\subsection{Strategy-Dependent Convergence}\n\nTemperature sampling applies uniform scaling to logits, while nucleus and top-$k$ sampling truncate the distribution. Uniform scaling accelerates convergence to the fixed-point distribution because it amplifies the contraction at every point in the distribution simultaneously, rather than selectively truncating. We formalize this as a multiplicative factor on the effective contraction rate:\n\\[\n    \\alpha_{\\mathrm{temp}} = \\alpha \\cdot \\gamma, \\quad \\gamma \\approx 1.35 \\quad (\\text{estimated from empirical loss curves}).\n\\]\n\nThis predicts that temperature-sampled text at depth $N$ should exhibit feature statistics similar to nucleus-sampled text at depth $N+1$.\n\n\\textbf{Prediction 3.} Temperature-to-nucleus convergence ratio $> 1$. \\emph{Observed}: ratio $\\approx 1.35$; GPT-2 XL temp09 d1 \\texttt{p90\\_ppl} median = 92.2, which falls within the nucleus/top-$k$ d2 range of 65--92.\n\n% ============================================================\n% 5. EXPERIMENTAL SETUP\n% ============================================================\n\\section{Experimental Setup}\n\n\\paragraph{Benchmark construction.}\nWe construct recursive generation chains for three 1--1.5B parameter models: GPT-2 XL (1.5B), Pythia-1.4B, and OLMo-1B. For each model, we fine-tune with LoRA on the previous depth's generated text and sample the next depth using three decoding strategies: nucleus sampling ($p = 0.95$), temperature sampling ($\\tau = 0.9$), and top-$k$ sampling ($k = 50$). This produces $3 \\times 3 = 9$ independent chains, each spanning depths d0--d3, yielding $9 \\times 4 \\times 5000 = 180{,}000$ text passages.\n\n\\paragraph{Scale validation.}\nWe additionally construct a Qwen2.5-14B chain using FP16 precision (no quantization) with LoRA fine-tuning on a 96GB RTX PRO 6000 GPU, spanning depths d0--d3 with nucleus sampling, to validate that depth signal persists at mainstream model scale.\n\n\\paragraph{Classifiers.}\nWe evaluate Random Forest (RF, 100 trees) and Logistic Regression (LR) as representative non-parametric and linear classifiers. All results use 5-fold cross-validation with bootstrap 95\\% confidence intervals computed from fold-level estimates (1000 resamples).\n\n\\paragraph{Baselines.}\nWe calibrate Binoculars \\citep{hans2024binoculars} and Fast-DetectGPT \\citep{bao2024fastdetectgpt} continuous scores for ordinal depth estimation using (a) equal-quantile binning and (b) oracle threshold optimization. The chance baseline for 4-class classification is 25\\%.\n\n% ============================================================\n% 6. RESULTS\n% ============================================================\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Depth Degradation Atlas: The 3$\\times$3 Benchmark}\n\nTable~\\ref{tab:atlas} presents the core Atlas results. RF classifiers achieve 70--85\\% four-class accuracy across all nine model-strategy combinations, with GPT-2 XL under temperature sampling reaching the highest accuracy of 85.4\\%. Bootstrap 95\\% CIs are tight (mean width 1.8pp, max 2.5pp), and all lower bounds exceed 68\\%, well above chance (25\\%).\n\nThree patterns emerge. First, \\texttt{p90\\_ppl} and \\texttt{var\\_surprisal} rank among the top-4 features in all nine settings, confirming the universality of tail-based depth markers. Second, inter-depth discrimination decreases monotonically: d0v1 AUC $\\approx$ 0.99, d1v2 AUC $\\approx$ 0.86, d2v3 AUC $\\approx$ 0.80. Third, decoding strategies produce a three-tier pattern: temperature enhances signal (mean accuracy 82.6\\%), nucleus provides a stable baseline (mean 79.0\\%), and top-$k$ attenuates signal (mean 73.2\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{Depth Degradation Atlas: 4-class RF accuracy (\\%) with bootstrap 95\\% CIs across 3 models $\\times$ 3 decoding strategies. All results use 5-fold CV on 19 statistical features. Chance = 25\\%.}\n\\label{tab:atlas}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Nucleus} & \\textbf{Temp ($\\tau$=0.9)} & \\textbf{Top-$k$ ($k$=50)} \\\\\n\\midrule\n\\textbf{Pythia-1.4B} & 78.2 \\scriptsize{[76.9, 79.4]} & 76.3 \\scriptsize{[74.9, 77.6]} & 69.7 \\scriptsize{[68.2, 71.1]} \\\\\n\\textbf{OLMo-1B}     & 78.9 \\scriptsize{[77.6, 80.2]} & 82.2 \\scriptsize{[80.8, 83.5]} & 74.2 \\scriptsize{[72.8, 75.6]} \\\\\n\\textbf{GPT-2 XL}    & 83.9 \\scriptsize{[82.6, 85.2]} & 85.4 \\scriptsize{[84.1, 86.7]} & 75.7 \\scriptsize{[74.3, 77.0]} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Scale Robustness at 14B}\n\nTable~\\ref{tab:14b} presents results for Qwen2.5-14B under clean FP16 conditions (no quantization). The 14B model achieves 79\\% four-class accuracy [77.8, 80.2], falling within the range of the three 1B-scale models (69.7--85.4\\%). The adjacent-depth AUC profile mirrors the 1B pattern: d0v1 = 0.991, d1v2 = 0.87, d2v3 = 0.82. The top-4 features are identical to the 1B models (overlap = 4/4): \\texttt{p90\\_ppl}, \\texttt{var\\_surprisal}, \\texttt{p75\\_ppl}, and \\texttt{mean\\_surprisal}. Per-class recall follows the expected depth-dependent pattern: d0 = 98\\%, d1 = 84\\%, d2 = 62\\%, d3 = 72\\%.\n\nThese results confirm that the depth signal and feature universality are not limited to small models. The fine-tuning loss trajectory at 14B (2.35 $\\to$ 1.58 $\\to$ 1.15) is flatter than at 1B, consistent with larger residual capacity resisting catastrophic distributional shift, but insufficient to prevent tail erosion.\n\n\\begin{table}[t]\n\\centering\n\\caption{Scale robustness: Qwen2.5-14B FP16 vs 1B-scale models. Feature overlap refers to concordance of top-4 ranked features with the 1B-model consensus.}\n\\label{tab:14b}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{4-class Acc} & \\textbf{d1v2 AUC} & \\textbf{d2v3 AUC} & \\textbf{Top-4 Overlap} \\\\\n\\midrule\nPythia-1.4B (nucleus) & 78.2 & 0.86 & 0.80 & --- \\\\\nOLMo-1B (nucleus)     & 78.9 & 0.87 & 0.81 & --- \\\\\nGPT-2 XL (nucleus)    & 83.9 & 0.92 & 0.84 & --- \\\\\n\\midrule\nQwen2.5-14B (nucleus) & 79.0 & 0.87 & 0.82 & 4/4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Binary Detectors Fail at Ordinal Estimation}\n\nTable~\\ref{tab:baseline} compares existing binary detectors repurposed for ordinal depth estimation against our feature-based approach. Both Binoculars and Fast-DetectGPT perform near chance on the ordinal task. Even with oracle threshold optimization (which uses test-set depth distribution information), the best binary detector achieves only 38\\%, compared to 78.3\\% for the RF 19-feature classifier. The d1v2 AUC values (0.54--0.56) are barely above chance (0.50), confirming that binary detector scores do not encode ordinal depth gradients. A score combination (Binoculars + Fast-DetectGPT features) reaches 40\\%, still 38pp below the feature-based method.\n\nBinary detectors are designed to capture a single boundary (real vs.\\ synthetic). Their continuous scores saturate beyond d0: d1, d2, and d3 texts all register as ``synthetic'' with similar confidence, erasing the ordinal structure that tail statistics preserve.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ordinal baseline comparison: binary detectors calibrated for 4-class depth estimation vs.\\ feature-based methods. Quantile: equal-quantile binning; Oracle: optimal threshold search using test-set distribution.}\n\\label{tab:baseline}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{4-class Acc} & \\textbf{d1v2 AUC} & \\textbf{d2v3 AUC} \\\\\n\\midrule\nChance & 25.0 & 0.50 & 0.50 \\\\\nBinoculars (quantile)   & 32.0 & 0.56 & 0.52 \\\\\nBinoculars (oracle)     & 38.0 & 0.56 & 0.52 \\\\\nFast-DetectGPT (quantile) & 30.0 & 0.54 & 0.51 \\\\\nFast-DetectGPT (oracle) & 36.0 & 0.54 & 0.51 \\\\\nCombined (oracle)       & 40.0 & --- & --- \\\\\n\\midrule\nRF 19-feature           & \\textbf{78.3} & \\textbf{0.86} & \\textbf{0.80} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Theoretical Predictions vs.\\ Empirical Results}\n\nTable~\\ref{tab:theory} summarizes the three theoretical predictions and their empirical verification. All three predictions fall within the theoretically derived ranges, supporting the connection between model collapse contraction theory and the practical feasibility of depth estimation.\n\nThe agreement between the predicted \\edd{} range of [3, 5] and the observed \\edd{} = 4 provides more than post-hoc confirmation: it establishes a principled basis for understanding why ordinal depth estimation works at shallow depths but faces fundamental limits. As recursive generation contracts the output distribution toward a fixed point, the remaining inter-depth distributional distance eventually falls below any classifier's discrimination threshold.\n\n\\begin{table}[t]\n\\centering\n\\caption{Theoretical predictions derived from model collapse contraction theory vs.\\ empirical observations. $\\alpha = 0.72$ is estimated from fine-tuning loss decay curves.}\n\\label{tab:theory}\n\\small\n\\begin{tabular}{p{4.5cm}cc}\n\\toprule\n\\textbf{Prediction} & \\textbf{Theoretical} & \\textbf{Empirical} \\\\\n\\midrule\n\\edd{} range & [3, 5] & 4 (all 3 models) \\\\\n\\texttt{p90\\_ppl} decay / depth & 15--25\\% & 18--22\\% \\\\\nTemp/nucleus convergence ratio & $> 1$ & $\\approx 1.35$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Cross-Strategy Transfer and Two-Stage Pipeline}\n\nNaive cross-strategy leave-one-out transfer yields 59.1\\% mean accuracy, with temperature holdout exhibiting d1v2 AUC reversal (GPT-2 XL: 0.13, OLMo: 0.25). This reversal is not noise: Section~4.3 explains the causal mechanism (temperature's uniform logit scaling accelerates convergence, so temp09 depth $N$ features approximate nucleus depth $N+1$).\n\nThe two-stage pipeline first identifies the decoding strategy (57.8\\% accuracy on the same 19 features), then routes to strategy-conditioned depth classifiers. This improves mean cross-strategy accuracy from 59.1\\% to 70.5\\% (+11.5pp). Per-model results: GPT-2 XL 73.0\\%, OLMo 69.4\\%, Pythia 69.3\\%. The oracle ceiling (perfect strategy identification) is 78.3\\%.\n\n\\paragraph{Strategy-dependent d1v2 AUC.}\nWe report per-strategy cross-strategy d1v2 AUC for transparency. When temperature is the holdout strategy, d1v2 AUC drops to 0.13--0.25, reflecting the structural distributional shift identified in Section~4.3. Z-score normalization improves overall LR cross-strategy accuracy from 25\\% to 61\\% but does not recover pairwise d1v2 AUC (GPT-2 XL: 0.50 $\\to$ 0.24; OLMo: 0.50 $\\to$ 0.19), confirming that simple feature normalization cannot resolve a geometric distributional shift.\n\n% ============================================================\n% 7. DISCUSSION\n% ============================================================\n\\section{Discussion}\n\n\\paragraph{Wild-data ecological validity.}\nTo assess behavior on uncurated web text, we apply depth estimators trained on our controlled benchmark to 10K-sample subsets of C4, FineWeb, and RedPajama. The depth distribution is dominated by d0 predictions (78--85\\%), with false positive rates (non-d0 predictions on human-written web text) of 21.5\\% (C4), 18.0\\% (FineWeb), and 15.0\\% (RedPajama). Cross-model agreement on d0 predictions is high (92\\%). Inspection of misclassified samples reveals that template, SEO, and boilerplate content shares statistical features with recursively generated text (high $n$-gram repetition, low surprisal variance). FPR correlates inversely with the strictness of the source corpus's cleaning pipeline (RedPajama $<$ FineWeb $<$ C4). This suggests that depth estimation features capture a general text quality gradient, with template-heavy web content occupying a similar feature-space region as shallow recursive generation. Full results appear in Appendix Tables~\\ref{tab:wild} and~\\ref{tab:wild_agreement}.\n\n\\paragraph{API model generalization.}\nFine-tuned GPT-4o-mini recursive chains achieve 58\\% four-class accuracy with d0v1 AUC = 0.93 and d1v2 AUC = 0.72. Prompted (non-fine-tuned) recursive chains yield 45\\% accuracy. Both exceed chance (25\\%), indicating that depth signal persists in RLHF-aligned commercial models, though attenuated. The feature profile of fine-tuned chains overlaps 3/4 top features with base models (\\texttt{p90\\_ppl}, \\texttt{var\\_surprisal}, \\texttt{mean\\_ppl}), while prompted chains show a shifted profile (\\texttt{surprisal\\_range} replaces \\texttt{p75\\_ppl}), reflecting the additional constraints imposed by prompt engineering on the generation process. Full results appear in Appendix Table~\\ref{tab:api}.\n\n\\paragraph{Negative results: end-to-end learning.}\nWe systematically explored contrastive ordinal learning (DCOL) using RoBERTa-large embeddings across six architecture variants (v1--v6). All variants failed to outperform feature-based methods, with the best achieving 64.5\\% accuracy versus 78.2\\% for the RF baseline. Failure modes included embedding collapse (adjacent-depth cosine similarity $> 0.95$), catastrophic forgetting, and gradient instability. The consistent underperformance of neural end-to-end approaches (DeBERTa: 58.3\\%, RoBERTa: 59.5\\%, DCOL best: 64.5\\%) compared to feature-based methods (RF: 78.3\\%, LR: 76.0\\%) suggests that explicit statistical features capture depth-relevant distributional properties more effectively than learned representations when inter-class boundaries in embedding space are narrow. Full analysis appears in Appendix Table~\\ref{tab:dcol}.\n\n\\paragraph{Depth-graduated curation.}\nPredicted depth provides a finer-grained quality proxy than binary real/synthetic labels. Rather than filtering all synthetic content, curation pipelines could weight training samples inversely to predicted depth, retaining beneficial shallow-generation data while downweighting deeply recursive text. The monotonic relationship between depth and classifier accuracy in our 3$\\times$3 matrix supports this graduated approach, though full experimental validation of downstream training effects is left to future work.\n\n% ============================================================\n% 8. LIMITATIONS\n% ============================================================\n\\section{Limitations}\n\n\\textbf{Controlled vs.\\ wild domain shift.} Our benchmark uses LoRA fine-tuning chains under controlled conditions. Real-world recursive generation involves heterogeneous models, varying data mixtures, and unknown generation parameters. While wild-data calibration (Section~7) and prompted generation experiments provide evidence of ecological validity, the controlled-to-wild generalization gap remains only partially characterized.\n\n\\textbf{Cross-strategy deployment.} Cross-strategy deployment requires knowledge of the target decoding strategy. Without strategy metadata, d1/d2 predictions may be inverted when the unknown strategy is temperature-based, due to the structural distributional shift identified in Section~4.3. The two-stage pipeline mitigates this partially (+11.5pp), but strategy classification accuracy (57.8\\%) remains a bottleneck. Whether more sophisticated domain adaptation methods can fully resolve the temperature-induced d1v2 boundary reversal remains an open problem.\n\n\\textbf{\\edd{} statistical significance.} While d3v4 AUC consistently clusters near the 0.75 threshold across all three models (0.750--0.784), only Pythia achieves statistical significance ($p = 0.001$); OLMo is marginal ($p = 0.091$) and GPT-2 XL is not significant ($p = 0.505$). D4v5 AUC uniformly falls below 0.70 (0.681--0.694). We report \\edd{} = 4 based on directional consistency rather than universal statistical significance.\n\n\\textbf{Reference model dependency.} Feature extraction requires access to a reference language model. Cross-model LOO accuracy (66.4\\%) is lower than within-model accuracy (78.3\\%), indicating partial reference model dependence. The choice of reference model affects absolute accuracy but not the qualitative patterns (feature ranking, strategy effects, \\edd{}).\n\n% ============================================================\n% 9. CONCLUSION\n% ============================================================\n\\section{Conclusion}\n\nWe formalized ordinal generation depth estimation as a new task, addressing the gap between binary synthetic text detection and the reality of multi-generational recursive content in web-scraped corpora. Our Depth Degradation Atlas provides the first systematic empirical characterization of how text statistical properties evolve across recursive generation depths, spanning three model families, three decoding strategies, and scales from 1B to 14B parameters. The theoretical connection to model collapse contraction rates grounds the Atlas in distributional theory and produces verifiable predictions that match our observations. Feature-based classifiers achieve 70--85\\% four-class accuracy, existing binary detectors fail at ordinal estimation (30--38\\%), and a two-stage strategy-aware pipeline addresses the cross-strategy deployment challenge. We release our benchmark and code to support future work on recursive depth estimation and depth-aware data curation.\n\n% ============================================================\n% REFERENCES\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{30}\n\n\\bibitem[Alemohammad et~al.(2024)]{alemohammad2024selfconsuming}\nS.~Alemohammad, J.~Casco-Rodriguez, L.~Luzi, A.~I. Ahmed, D.~Abedi, R.~Baraniuk, et~al.\n\\newblock Self-consuming generative models go {MAD}.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Bao et~al.(2024)]{bao2024fastdetectgpt}\nG.~Bao, Y.~Zhao, Z.~Teng, L.~Yang, and M.~Zhang.\n\\newblock Fast-{DetectGPT}: Efficient zero-shot detection of machine-generated text via conditional probability curvature.\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Dohmatob et~al.(2024)]{dohmatob2024tale}\nE.~Dohmatob, P.~Feng, and Q.~Yang.\n\\newblock A tale of tails: Model collapse as a change of scaling laws.\n\\newblock \\emph{arXiv preprint arXiv:2402.07043}, 2024.\n\n\\bibitem[Drayson et~al.(2025)]{drayson2025investigatinggeneralizabilitygenerationdegradation}\nN.~Drayson, Y.~Du, and A.~Sherborne.\n\\newblock Investigating the generalizability of generation degradation.\n\\newblock In \\emph{EMNLP}, 2025.\n\n\\bibitem[Garc{\\'e}s~Arias et~al.(2025)]{garcesarias2025decoding}\nL.~Garc{\\'e}s~Arias, S.~Mille, and L.~Padro.\n\\newblock On the impact of decoding strategies on the detectability of machine-generated text.\n\\newblock In \\emph{COLING}, 2025.\n\n\\bibitem[Gerstgrasser et~al.(2024)]{gerstgrasser2024model}\nM.~Gerstgrasser, R.~Schaeffer, A.~Dey, R.~Rafailov, H.~Sleiman, J.~Hughes, T.~Korbak, R.~Agarwal, D.~Levine, et~al.\n\\newblock Is model collapse inevitable? {Breaking} the curse of recursion by accumulating real and synthetic data.\n\\newblock \\emph{arXiv preprint arXiv:2404.01413}, 2024.\n\n\\bibitem[Hans et~al.(2024)]{hans2024binoculars}\nA.~Hans, A.~Schwarzschild, V.~Cherepanova, H.~Kazemi, A.~Saha, M.~Goldblum, J.~Geiping, and T.~Goldstein.\n\\newblock Spotting {LLMs} with {Binoculars}: Zero-shot detection of machine-generated text.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Holtzman et~al.(2020)]{holtzman2020curious}\nA.~Holtzman, J.~Buys, L.~Du, M.~Forbes, and Y.~Choi.\n\\newblock The curious case of neural text degeneration.\n\\newblock In \\emph{ICLR}, 2020.\n\n\\bibitem[Kirchenbauer et~al.(2023)]{kirchenbauer2023watermark}\nJ.~Kirchenbauer, J.~Geiping, Y.~Wen, J.~Katz, I.~Miers, and T.~Goldstein.\n\\newblock A watermark for large language models.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Liang et~al.(2024)]{liang2024monitoring}\nW.~Liang, M.~Yuksekgonul, Y.~Mao, E.~Wu, and J.~Zou.\n\\newblock {GPT} detectors are biased against non-native {English} writers.\n\\newblock In \\emph{Patterns}, 4(7), 2024.\n\n\\bibitem[Mitchell et~al.(2023)]{mitchell2023detectgpt}\nE.~Mitchell, Y.~Lee, A.~Khazatsky, C.~D. Manning, and C.~Finn.\n\\newblock {DetectGPT}: Zero-shot machine-generated text detection using probability curvature.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Shumailov et~al.(2024)]{shumailov2024model}\nI.~Shumailov, Z.~Shumaylov, Y.~Zhao, N.~Papernot, R.~Anderson, and Y.~Gal.\n\\newblock {AI} models collapse when trained on recursively generated data.\n\\newblock \\emph{Nature}, 631:755--759, 2024.\n\n\\bibitem[Uchendu et~al.(2020)]{uchendu2020authorship}\nA.~Uchendu, T.~Le, K.~Shu, and D.~Lee.\n\\newblock Authorship attribution for neural text generation.\n\\newblock In \\emph{EMNLP}, 2020.\n\n\\bibitem[Wang et~al.(2024)]{wang2024editlens}\nM.~Wang, Z.~Wang, B.~Li, and J.~Chen.\n\\newblock {EditLens}: Evaluating and predicting editing on {AI}-generated texts.\n\\newblock \\emph{arXiv preprint arXiv:2404.17435}, 2024.\n\n\\bibitem[Wettig et~al.(2024)]{wettig2024qurating}\nA.~Wettig, A.~Gao, Z.~Zhong, and D.~Chen.\n\\newblock {QuRating}: Selecting high-quality data for training language models.\n\\newblock In \\emph{ICML}, 2024.\n\n\\bibitem[Xie et~al.(2023)]{xie2023dsir}\nS.~M. Xie, S.~Santurkar, T.~Ma, and P.~Liang.\n\\newblock Data selection for language models via importance resampling.\n\\newblock In \\emph{NeurIPS}, 2023.\n\n\\bibitem[Radford et~al.(2019)]{radford2019gpt2}\nA.~Radford, J.~Wu, R.~Child, D.~Luan, D.~Amodei, and I.~Sutskever.\n\\newblock Language models are unsupervised multitask learners.\n\\newblock \\emph{OpenAI Technical Report}, 2019.\n\n\\bibitem[Biderman et~al.(2023)]{biderman2023pythia}\nS.~Biderman, H.~Schoelkopf, Q.~Anthony, H.~Bradley, K.~O'Brien, E.~Hallahan, M.~A. Khan, S.~Purohit, U.~S. Prashanth, E.~Raff, et~al.\n\\newblock {Pythia}: A suite for analyzing large language models across training and scaling.\n\\newblock In \\emph{ICML}, 2023.\n\n\\bibitem[Groeneveld et~al.(2024)]{groeneveld2024olmo}\nD.~Groeneveld, I.~Beltagy, P.~Walsh, A.~Bhagia, R.~Kinney, O.~Tafjord, A.~Jha, H.~Ivison, I.~Magnusson, Y.~Wang, et~al.\n\\newblock {OLMo}: Accelerating the science of language models.\n\\newblock In \\emph{ACL}, 2024.\n\n\\bibitem[Hu et~al.(2022)]{hu2022lora}\nE.~J. Hu, Y.~Shen, P.~Wallis, Z.~Allen-Zhu, Y.~Li, S.~Wang, L.~Wang, and W.~Chen.\n\\newblock {LoRA}: Low-rank adaptation of large language models.\n\\newblock In \\emph{ICLR}, 2022.\n\n\\bibitem[Breiman(2001)]{breiman2001randomforests}\nL.~Breiman.\n\\newblock Random forests.\n\\newblock \\emph{Machine Learning}, 45(1):5--32, 2001.\n\n\\bibitem[Yang et~al.(2024)]{yang2024qwen2}\nA.~Yang, B.~Yang, B.~Hui, B.~Zheng, B.~Yu, C.~Zhou, et~al.\n\\newblock {Qwen2} technical report.\n\\newblock \\emph{arXiv preprint arXiv:2407.10671}, 2024.\n\n\\bibitem[Cao et~al.(2020)]{cao2020coral}\nW.~Cao, V.~Mirjalili, and S.~Raschka.\n\\newblock Rank consistent ordinal regression for neural networks with application to age estimation.\n\\newblock \\emph{Pattern Recognition Letters}, 140:325--331, 2020.\n\n\\bibitem[Liang et~al.(2023)]{liang2023helm}\nP.~Liang, R.~Bommasani, T.~Lee, D.~Tsipras, D.~Soylu, M.~Yasunaga, Y.~Zhang, D.~Narayanan, et~al.\n\\newblock Holistic evaluation of language models.\n\\newblock \\emph{TMLR}, 2023.\n\n\\bibitem[Hendrycks et~al.(2021)]{hendrycks2021mmlu}\nD.~Hendrycks, C.~Burns, S.~Basart, A.~Zou, M.~Mazeika, D.~Song, and J.~Steinhardt.\n\\newblock Measuring massive multitask language understanding.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Achiam et~al.(2023)]{achiam2023gpt4}\nJ.~Achiam, S.~Adler, S.~Agarwal, L.~Ahmad, I.~Akkaya, F.~L.~Aleman, et~al.\n\\newblock {GPT-4} technical report.\n\\newblock \\emph{arXiv preprint arXiv:2303.08774}, 2023.\n\n\\end{thebibliography}\n\n% ============================================================\n% APPENDIX\n% ============================================================\n\\appendix\n\n\\section{Wild-Data Calibration}\n\\label{app:wild}\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth distribution predictions on wild web-crawl data (10K samples each, Pythia-1.4B reference model). FPR = percentage of samples predicted as non-d0.}\n\\label{tab:wild}\n\\small\n\\begin{tabular}{lcccc|c}\n\\toprule\n\\textbf{Corpus} & \\textbf{d0 (\\%)} & \\textbf{d1 (\\%)} & \\textbf{d2 (\\%)} & \\textbf{d3 (\\%)} & \\textbf{FPR (\\%)} \\\\\n\\midrule\nC4         & 78.5 & 19.8 & 1.2 & 0.5 & 21.5 \\\\\nFineWeb    & 82.0 & 16.8 & 0.8 & 0.4 & 18.0 \\\\\nRedPajama  & 85.0 & 13.5 & 1.0 & 0.5 & 15.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-model agreement on wild-data d0 predictions across three reference models.}\n\\label{tab:wild_agreement}\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{Metric} & \\textbf{Value} \\\\\n\\midrule\nd0 agreement (3 models) & 92\\% \\\\\nPrimary misclassification type & template/SEO/boilerplate \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFPR inversely correlates with corpus cleaning strictness: RedPajama (most filtered) $<$ FineWeb $<$ C4. Misclassified samples are predominantly template-heavy, SEO-optimized, or boilerplate content, whose low lexical diversity and high repetition rates place them in the same feature-space region as shallow recursive generation output.\n\n\\section{API Model Depth Estimation}\n\\label{app:api}\n\n\\begin{table}[h]\n\\centering\n\\caption{Depth estimation on GPT-4o-mini recursive chains. Fine-tuned: LoRA fine-tuning API chain. Prompted: iterative rewrite prompting without fine-tuning.}\n\\label{tab:api}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Chain Type} & \\textbf{4-class Acc} & \\textbf{d0v1 AUC} & \\textbf{d1v2 AUC} \\\\\n\\midrule\nFine-tuned chain & 58.0 & 0.93 & 0.72 \\\\\nPrompted chain   & 45.0 & 0.78 & 0.61 \\\\\n\\midrule\nBase model RF (reference) & 78.3 & 0.99 & 0.86 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFine-tuned chain top features: \\texttt{p90\\_ppl}, \\texttt{var\\_surprisal}, \\texttt{mean\\_ppl}, \\texttt{p75\\_ppl} (3/4 overlap with base models). Prompted chain top features: \\texttt{var\\_surprisal}, \\texttt{p90\\_ppl}, \\texttt{surprisal\\_range}, \\texttt{mean\\_surprisal} (shifted profile reflecting prompt-mediated constraints). Both settings exceed chance (25\\%), confirming that RLHF regularization attenuates but does not eliminate depth signal.\n\n\\section{End-to-End vs.\\ Feature-Based Methods}\n\\label{app:dcol}\n\n\\begin{table}[h]\n\\centering\n\\caption{Comparison of end-to-end neural methods vs.\\ feature-based classifiers. DCOL v1--v6 explored contrastive ordinal learning with RoBERTa-large embeddings; all variants underperformed feature-based baselines.}\n\\label{tab:dcol}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{4-class Acc (\\%)} & \\textbf{Category} \\\\\n\\midrule\nDeBERTa (fine-tuned)     & 58.3 & End-to-end \\\\\nRoBERTa (fine-tuned)     & 59.5 & End-to-end \\\\\nDCOL v6 (best variant)   & 64.5 & End-to-end \\\\\n\\midrule\nLR (19 features)         & 76.0 & Feature-based \\\\\nRF (19 features)         & \\textbf{78.3} & Feature-based \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe systematic underperformance of end-to-end methods is attributable to the narrow inter-class boundaries in embedding space. Adjacent recursive depths produce text with cosine similarity exceeding 0.95 in RoBERTa-large embedding space, leaving insufficient margin for contrastive learning to establish discriminative boundaries. Feature-based methods circumvent this by operating on hand-crafted statistics (tail perplexity, surprisal variance) that amplify the distributional differences that embedding-space distances compress. DCOL v1--v6 failure modes included: embedding collapse (v1--v2), out-of-memory (v3), catastrophic forgetting (v4), NaN gradients (v5), and overfitting to depth 0 (v6). This negative result suggests that ordinal depth estimation in text is fundamentally better suited to explicit statistical features than to end-to-end representation learning, at least with current transformer-based text encoders.\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "1a980e3e-86b9-4de6-b3fd-05b351a051ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162616 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_dept…",
  "leafUuid": "df0b5705-cb6b-47ec-a013-e2043b1c07da",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate ordinal depth estimation paper with theory",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c"
}
```

---

### Tool call

_source line 24 · 2026-05-18T16:47:01.569Z_

<details open><summary>🔧 Tool call — Bash · `toolu_013AtqKeruKprMzHfqXnWHqr`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for cross-references",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df0b5705-cb6b-47ec-a013-e2043b1c07da",
  "isSidechain": false,
  "requestId": "req_011CbANfFqkVT7pVSiMM3gQk",
  "type": "assistant",
  "uuid": "6efd15e2-fc88-4dd5-b865-a1caa729ed44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198w35spNyYSyZ74edFDCss",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13731,
      "cache_read_input_tokens": 38875,
      "output_tokens": 172,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13731,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 172,
          "cache_read_input_tokens": 38875,
          "cache_creation_input_tokens": 13731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13731
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

_source line 25 · 2026-05-18T16:47:07.491Z_

<details><summary>↩ Tool result · `toolu_013AtqKeruKprMzHfqXnWHqr`</summary>

```text
&lt;persisted-output>
Output too large (38.8KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est/0499f6b9-3e8b-4fbf-b60c-304da272439c/tool-results/btng49t4g.txt

Preview (first 2KB):
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
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6efd15e2-fc88-4dd5-b865-a1caa729ed44",
  "isSidechain": false,
  "promptId": "c9727216-6650-4282-92f3-6408303632c9",
  "type": "user",
  "uuid": "da57c981-8b9e-484a-818c-dad1235e0eaf",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption.sty\n(/usr/share/texlive/texmf-dist/tex/latex/caption/caption3.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/caption/subcaption.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `shumailov2024model' on page 1 undefined on in\nput line 39.\n\n\nPackage natbib Warning: Citation `alemohammad2024selfconsuming' on page 1 undef\nined on input line 39.\n\n\nPackage natbib Warning: Citation `dohmatob2024tale' on page 1 undefined on inpu\nt line 39.\n\n\nPackage natbib Warning: Citation `gerstgrasser2024model' on page 1 undefined on\n input line 39.\n\n\nPackage natbib Warning: Citation `hans2024binoculars' on page 1 undefined on in\nput line 41.\n\n\nPackage natbib Warning: Citation `bao2024fastdetectgpt' on page 1 undefined on \ninput line 41.\n\n\nPackage natbib Warning: Citation `liang2024monitoring' on page 1 undefined on i\nnput line 41.\n\n\nPackage natbib Warning: Citation `drayson2025investigatinggeneralizabilitygener\nationdegradation' on page 1 undefined on input line 41.\n\n\nPackage natbib Warning: Citation `shumailov2024model' on page 1 undefined on in\nput line 41.\n\n\nPackage natbib Warning: Citation `shumailov2024model' on page 1 undefined on in\nput line 45.\n\n\nPackage natbib Warning: Citation `dohmatob2024tale' on page 1 undefined on inpu\nt line 45.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nPackage natbib Warning: Citation `shumailov2024model' on page 2 undefined on in\nput line 61.\n\n\nPackage natbib Warning: Citation `alemohammad2024selfconsuming' on page 2 undef\nined on input line 61.\n\n\nPackage natbib Warning: Citation `dohmatob2024tale' on page 2 undefined on inpu\nt line 61.\n\n\nPackage natbib Warning: Citation `gerstgrasser2024model' on page 2 undefined on\n input line 61.\n\n\nPackage natbib Warning: Citation `drayson2025investigatinggeneralizabilitygener\nationdegradation' on page 2 undefined on input line 61.\n\n\nPackage natbib Warning: Citation `hans2024binoculars' on page 2 undefined on in\nput line 64.\n\n\nPackage natbib Warning: Citation `bao2024fastdetectgpt' on page 2 undefined on \ninput line 64.\n\n\nPackage natbib Warning: Citation `mitchell2023detectgpt' on page 2 undefined on\n input line 64.\n\n\nPackage natbib Warning: Citation `kirchenbauer2023watermark' on page 2 undefine\nd on input line 64.\n\n\nPackage natbib Warning: Citation `liang2024monitoring' on page 2 undefined on i\nnput line 64.\n\n\nPackage natbib Warning: Citation `uchendu2020authorship' on page 2 undefined on\n input line 64.\n\n\nPackage natbib Warning: Citation `garcesarias2025decoding' on page 2 undefined \non input line 64.\n\n\nPackage natbib Warning: Citation `wang2024editlens' on page 2 undefined on inpu\nt line 64.\n\n\nPackage natbib Warning: Citation `xie2023dsir' on page 2 undefined on input lin\ne 67.\n\n\nPackage natbib Warning: Citation `wettig2024qurating' on page 2 undefined on in\nput line 67.\n\n\nPackage natbib Warning: Citation `holtzman2020curious' on page 2 undefined on i\nnput line 70.\n\n\nPackage natbib Warning: Citation `garcesarias2025decoding' on page 2 undefined \non input line 70.\n\n[2]\n\nPackage natbib Warning: Citation `shumailov2024model' on page 3 undefined on in\nput line 104.\n\n\nLaTeX Warning: Reference `sec:results' on page 3 undefined on input line 106.\n\n\nPackage natbib Warning: Citation `dohmatob2024tale' on page 3 undefined on inpu\nt line 110.\n\n[3]\n\nPackage natbib Warning: Citation `hans2024binoculars' on page 4 undefined on in\nput line 147.\n\n\nPackage natbib Warning: Citation `bao2024fastdetectgpt' on page 4 undefined on \ninput line 147.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 155.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `\\times' on input line 155.\n\n\nPackage hyperref Warning: Token not allowed in a PDF string (Unicode):\n(hyperref)                removing `math shift' on input line 155.\n\n\nLaTeX Warning: Reference `tab:atlas' on page 4 undefined on input line 157.\n\n[4]\n\nLaTeX Warning: Reference `tab:14b' on page 5 undefined on input line 179.\n\n\nLaTeX Warning: Reference `tab:baseline' on page 5 undefined on input line 203.\n\n[5]\n\nLaTeX Warning: Reference `tab:theory' on page 6 undefined on input line 230.\n\n\nUnderfull \\hbox (badness 10000) in paragraph at lines 245--245\n[]\\T1/cmr/m/n/10 Temp/nucleus con-ver-gence\n[6]\n\nLaTeX Warning: Reference `tab:wild' on page 7 undefined on input line 265.\n\n\nLaTeX Warning: Reference `tab:wild_agreement' on page 7 undefined on input line\n 265.\n\n\nLaTeX Warning: Reference `tab:api' on page 7 undefined on input line 268.\n\n\nLaTeX Warning: Reference `tab:dcol' on page 7 undefined on input line 271.\n\n[7] [8] [9]\n\nLaTeX Warning: `h' float specifier changed to `ht'.\n\n[10]\n\nPackage natbib Warning: There were undefined citations.\n\n[11] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information) &lt;/home/ubuntu/.texlive2025\n/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1000.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecrm0800\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecrm0800\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm0800.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecrm.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.06445pt)\nFont metrics written on ecrm0800.tfm.\nOutput written on ecrm0800.600gf (256 characters, 41732 bytes).\nTranscript written on ecrm0800.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive20\n25/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0800.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecxc1200\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecxc1200\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecxc1200.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecxc.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excsc.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excspl.mf\n Ok [25] [26] [27] [28] [29] [30] [31] [158])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170] [171]\n[172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182] [183]\n[184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.11108pt)\nFont metrics written on ecxc1200.tfm.\nOutput written on ecxc1200.600gf (256 characters, 60096 bytes).\nTranscript written on ecxc1200.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecxc1200.600pk: successfully generated.\n &lt;/home/ubuntu/.texlive\n2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecxc1200.600pk> &lt;/home/ubuntu/.texli\nve2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ecxc1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ecxc1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecxc1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ecxc.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excsc.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excspl.mf\n Ok [25] [26] [27] [28] [29] [30] [31] [158])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170] [171]\n[172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182] [183]\n[184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.0996pt)\nFont metrics written on ecxc1095.tfm.\nOutput written on ecxc1095.600gf (256 characters, 55196 bytes).\nTranscript written on ecxc1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecxc1095.600pk: successfully generated.\n &lt;/home/ubuntu/.tex\nlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecxc1095.600pk> &lt;/home/ubuntu/.t\nexlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 eccc1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input eccc1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/eccc1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/eccc.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excsc.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excspl.mf\n Ok [25] [26] [27] [28] [29] [30] [31] [158])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170] [171]\n[172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182] [183]\n[184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txpseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/txaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excligtb.mf\n Ok) ) ) )\n(some charht values had to be adjusted by as much as 0.0856pt)\nFont metrics written on eccc1095.tfm.\nOutput written on eccc1095.600gf (256 characters, 56408 bytes).\nTranscript written on eccc1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/eccc1095.600pk: successfully generated.\n &lt;/home/ubuntu/\n.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/eccc1095.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ectt1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ectt1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ectt1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ectt.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exmligtb.mf\n Ok) ) ) )\nFont metrics written on ectt1095.tfm.\nOutput written on ectt1095.600gf (256 characters, 47796 bytes).\nTranscript written on ectt1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk: successfully generated.\n &lt;/home/ubunt\nu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk> &lt;/home/ubu\nntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti1095.600pk> &lt;/home/u\nbuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095.600pk> &lt;/home\n/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm1095.600pk> &lt;/ho\nme/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1440.600pk>\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 eccc1000\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input eccc1000\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/eccc1000.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/eccc.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/excsc.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est/0499f6b9-3e8b-4fbf-b60c-304da272439c/tool-results/btng49t4g.txt",
    "persistedOutputSize": 39778
  },
  "sourceToolAssistantUUID": "6efd15e2-fc88-4dd5-b865-a1caa729ed44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162616 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_dept…",
  "leafUuid": "da57c981-8b9e-484a-818c-dad1235e0eaf",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate ordinal depth estimation paper with theory",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c"
}
```

---

### Tool call

_source line 28 · 2026-05-18T16:47:12.002Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RiSaMQpoXuqnsGQv3xXR2B`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/paper.pdf && tail -5 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est/0499f6b9-3e8b-4fbf-b60c-304da272439c/tool-results/btng49t4g.txt",
  "description": "Verify PDF exists and check compilation end"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da57c981-8b9e-484a-818c-dad1235e0eaf",
  "isSidechain": false,
  "requestId": "req_011CbANfyci7QEVBCQjcNBTy",
  "type": "assistant",
  "uuid": "8bbf354b-1d26-4ba2-b893-011a97115769",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6XnZUTMrsu9HpCvVtDyj6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 52606,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1193,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 213,
          "cache_read_input_tokens": 52606,
          "cache_creation_input_tokens": 1193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1193
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

_source line 29 · 2026-05-18T16:47:12.067Z_

<details><summary>↩ Tool result · `toolu_01RiSaMQpoXuqnsGQv3xXR2B`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 260925 May 18 16:47 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/paper.pdf
ve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf
-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/
fonts/type1/public/amsfonts/cm/cmsy8.pfb>
Output written on paper.pdf (11 pages, 260925 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8bbf354b-1d26-4ba2-b893-011a97115769",
  "isSidechain": false,
  "promptId": "c9727216-6650-4282-92f3-6408303632c9",
  "type": "user",
  "uuid": "6d3e949f-a056-4290-9cce-569247e750ca",
  "toolUseResult": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu 260925 May 18 16:47 /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best/paper.pdf\nve/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf\n-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/\nfonts/type1/public/amsfonts/cm/cmsy8.pfb>\nOutput written on paper.pdf (11 pages, 260925 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "8bbf354b-1d26-4ba2-b893-011a97115769",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-18T16:47:23.472Z_

PDF 编译成功（11 页，261KB）。

论文已写入 `best/paper.tex` 并编译为 `best/paper.pdf`。覆盖了 experiment_data.json 中全部 7 个实验：

| 实验 | 论文位置 |
|------|----------|
| Table 1 bootstrap CIs (3×3 矩阵) | Table 1, Section 6.1 |
| 14B FP16 scale validation | Table 2, Section 6.2 |
| Binoculars/Fast-DetectGPT ordinal baseline | Table 3, Section 6.3 |
| Theoretical analysis (EDD upper bound) | Table 4, Section 4 + Section 6.4 |
| Cross-strategy pipeline | Section 6.5 |
| Wild-data calibration | Appendix A, Tables A3--A4, Discussion |
| API model (GPT-4o-mini) | Appendix B, Table A5, Discussion |
| DCOL negative results | Appendix C, Table A6, Discussion |

理论 section 从 Shumailov tail erosion + Dohmatob contraction rate 推导 EDD 上界 = 5，与实证 EDD = 4 吻合，提出 3 条可验证预测。所有定量 claim 均来自 experiment_data.json，无编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d3e949f-a056-4290-9cce-569247e750ca",
  "isSidechain": false,
  "requestId": "req_011CbANgK7EAbXJrqxD3mRHJ",
  "type": "assistant",
  "uuid": "5bf99e90-c1c1-4987-8231-bc81a3c8a645",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/dream_reports/dream_20260518T162616/best",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YVA55aMtbjyHmBCA2FnBsA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 428,
      "cache_read_input_tokens": 53799,
      "output_tokens": 368,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 428,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 368,
          "cache_read_input_tokens": 53799,
          "cache_creation_input_tokens": 428,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 428
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
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260518T162616 tier=best 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_dept…",
  "leafUuid": "5bf99e90-c1c1-4987-8231-bc81a3c8a645",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate ordinal depth estimation paper with theory",
  "sessionId": "0499f6b9-3e8b-4fbf-b60c-304da272439c"
}
```

---
