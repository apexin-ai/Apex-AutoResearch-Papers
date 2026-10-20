# analysis eval sft baseline noquant

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_analysis_eval_sft_baseline_noquant_20260515T194310.jsonl`
- **Structured JSON:** [`859f329351229a3421f9.json`](../../sessions/85/859f329351229a3421f9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

27 recorded events

### Tool call

_source line 1 · 2026-05-15T19:44:21.805216+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T19:44:21.806093+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T19:44:21.806443+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -50 ~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -50 ~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T19:44:21.806656+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -la /root/autodl-tmp/eval_results/sft_baseline_noquant/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -la /root/autodl-tmp/eval_results/sft_baseline_noquant/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T19:44:21.806992+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 02:38:49,421 INFO Detected adapter at /root/autodl-tmp/sft_output, base: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-16 02:38:49,421 INFO Loading tokenizer: /root/autodl-tmp/models/Qwen3-4B\\n2026-05-16 02:38:49,790 INFO Loading model: /root/autodl-tmp/models/Qwen3-4B\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-16 02:38:50,039 INFO We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards:  33%|███▎      | 1/3 [00:00<00:01,  1.23it/s]\\rLoading checkpoint shards:  67%|██████▋   | 2/3 [00:01<00:00,  1.22it/s]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:01<00:00,  1.81it/s]\\n2026-05-16 02:38:51,732 INFO Loading LoRA adapter: /root/autodl-tmp/sft_output\\n2026-05-16 02:38:54,777 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-16 02:38:55,128 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-16 02:38:55,334 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/62 [00:00<?, ?it/s]The following generation flags are not valid and may be ignored: ['temperature', 'top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\n\\rInference:   2%|▏         | 1/62 [00:57<58:07, 57.17s/it]\\rInference:   3%|▎         | 2/62 [01:54<57:00, 57.01s/it]\\rInference:   5%|▍         | 3/62 [02:54<57:31, 58.49s/it]\\rInference:   6%|▋         | 4/62 [03:51<56:00, 57.94s/it]\\rInference:   8%|▊         | 5/62 [04:51<55:47, 58.73s/it]\\rInference:  10%|▉         | 6/62 [05:51<55:05, 59.02s/it]\\rInference:  11%|█▏        | 7/62 [06:50<54:03, 58.97s/it]\\rInference:  13%|█▎        | 8/62 [07:47<52:46, 58.63s/it]\\rInference:  15%|█▍        | 9/62 
…[truncated 4160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T19:44:21.807293+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 7080\\ndrwxr-xr-x  2 root root      62 May 16 03:40 .\\ndrwxr-xr-x 28 root root    4096 May 16 03:33 ..\\n-rw-r--r--  1 root root    1491 May 16 03:40 metrics.json\\n-rw-r--r--  1 root root 7238660 May 16 03:40 predictions.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T19:44:21.807529+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'eval_sft_baseline_noquant'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'eval_sft_baseline_noquant'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T19:44:21.807727+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4303}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T19:44:21.807931+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "cat /root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "cat /root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T19:44:21.808123+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T19:44:21.808411+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"precision\\\": 0.4197541476833147,\\n  \\\"recall\\\": 0.4018599292239322,\\n  \\\"f1\\\": 0.4106121762529432,\\n  \\\"ign_precision\\\": 0.4197541476833147,\\n  \\\"ign_recall\\\": 0.4018599292239322,\\n  \\\"ign_f1\\\": 0.4106121762529432,\\n  \\\"tp\\\": 4883,\\n  \\\"pred_count\\\": 11633,\\n  \\\"gold_count\\\": 12151,\\n  \\\"evi_precision\\\": 0.80046358895113,\\n  \\\"evi_recall\\\": 0.8021680216802168,\\n  \\\"evi_f1\\\": 0.8013148989654839,\\n  \\\"n_evaluated\\\": 16647,\\n  \\\"edcr\\\": 0.7038730884664857,\\n  \\\"n_distractor_citations\\\": 19700,\\n  \\\"n_total_citations\\\": 27988,\\n  \\\"evi_joint_precision\\\": 0.3185128596893303,\\n  \\\"evi_joint_recall\\\": 0.3246975754114532,\\n  \\\"evi_f1_joint\\\": 0.32157548334018926,\\n  \\\"evi_tp\\\": 6254,\\n  \\\"evi_pred_total\\\": 19635,\\n  \\\"evi_gold_total\\\": 19261,\\n  \\\"format_compliance_rate\\\": 0.9979695431472081,\\n  \\\"field_compliance_rate\\\": 0.7065989847715736,\\n  \\\"evidence_format_rate\\\": 0.7065989847715736,\\n  \\\"n_total\\\": 985,\\n  \\\"n_parseable\\\": 983,\\n  \\\"n_field_complete\\\": 696,\\n  \\\"n_evidence_valid\\\": 696,\\n  \\\"n_documents\\\": 985,\\n  \\\"n_predictions\\\": 16774,\\n  \\\"n_truncated\\\": 288,\\n  \\\"n_format_ok\\\": 983,\\n  \\\"format_ok_rate\\\": 0.9979695431472081,\\n  \\\"inference_time_seconds\\\": 3677.9,\\n  \\\"config\\\": {\\n    \\\"model_path\\\": \\\"/root/autodl-tmp/sft_output\\\",\\n    \\\"base_model\\\": \\\"/root/autodl-tmp/models/Qwen3-4B\\\",\\n    \\\"sft_adapter\\\": null,\\n    \\\"data_path\\\": \\\"/root/autodl-tmp/data/docred\\\",\\n    \\\"output_dir\\\": \\\"/root/autodl-tmp/eval_results/sft_baseline_noquant\\\",\\n    \\\"batch_size\\\": 16,\\n    \\\"max_new_tokens\\\": 1024,\\n    \\\"split\\\": \\\"dev\\\",\\n    \\\"seed\\\": 42,\\n    \\\"no_evidence\\\": false,\\n    \\\"quantize\\\": false\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, 
…[truncated 61 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T19:44:21.810421+00:00_

Error: result (178,897 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/9631602c-9850-4f12-9a7b-8884326a6894/tool-results/mcp-agent-ml-research-read_registry-1778874212064.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/9631602c-9850-4f12-9a7b-8884326a6894/tool-results/mcp-agent-ml-research-read_registry-1778874212064.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T19:44:21.810757+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/9631602c-9850-4f12-9a7b-8884326a6894/tool-results/mcp-agent-ml-research-read_registry-1778874212064.txt | python3 -c \"import sys,json; d=json.loads(json.loads(sys.stdin.read())['result']); exps=d['data']['experiments']; matches=[k for k in exps if 'noquant' in k.lower() or 'sft_baseline' in k.lower()]; print(json.dumps({k:exps[k] for k in matches}, indent=2))\" 2>/dev/null | head -100",
  "description": "Search registry for sft_baseline experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/9631602c-9850-4f12-9a7b-8884326a6894/tool-results/mcp-agent-ml-research-read_registry-1778874212064.txt | python3 -c \"import sys,json; d=json.loads(json.loads(sys.stdin.read())['result']); exps=d['data']['experiments']; matches=[k for k in exps if 'noquant' in k.lower() or 'sft_baseline' in k.lower()]; print(json.dumps({k:exps[k] for k in matches}, indent=2))\" 2>/dev/null | head -100",
    "description": "Search registry for sft_baseline experiments"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T19:44:21.811033+00:00_

{
  "eval_sft_baseline_noquant": {
    "status": "ANALYZING",
    "retry_count": 0,
    "created_at": "2026-05-15T18:38:33.128Z",
    "updated_at": "2026-05-15T19:41:54.901Z",
    "spec": {
      "command": "python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --no-quantize",
      "server": "rtx5090-4x",
      "gpu": [
        "cuda:1"
      ],
      "pid": "237912",
      "log_path": "~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log",
      "submitted_at": "2026-05-15T18:38:45.042Z",
      "submitted_via": "submit_training_job",
      "backend": "tmux",
      "account": "root",
      "data_path": "/root/autodl-tmp/data/docred",
      "data_count": 985,
      "model_name": "Qwen3-4B (SFT baseline, no-quantize)",
      "seed": 42,
      "checkpoint_source": "/root/autodl-tmp/sft_output",
      "eval_data": "docred dev (985 docs)"
    },
    "reproduce": {
      "finished_at": "2026-05-15T19:41:54.062Z"
    },
    "extra": {
      "hook_events": [
        {
          "event": "on_complete",
          "action": "agent",
          "ts": "2026-05-15T19:41:59.716746+00:00"
        }
      ]
    }
  },
  "mvp2_eval_sft_baseline": {
    "status": "DONE",
    "retry_count": 1,
    "created_at": "2026-05-14T21:47:41.356Z",
    "updated_at": "2026-05-15T13:27:26.236Z",
    "hypothesis": "SFT baseline eval using identical eval protocol as GRPO evals (eval_lr5e6_ckpt20.sh). Required for MVP-2 core comparison: CED_Evi-F1 \u2212 SFT_Evi-F1 \u2265 2pp. Prior SFT eval (r3) used different eval path; this ensures apple-to-apple comparison.",
    "parent": "mvp2_sft_warmup",
    "server": "rtx5090-4x",
    "gpu": "cuda:3",
    "account": "root",
    "reproduce": {
      "server": "rtx5090-4x",
      "gpu": "cuda:3",
      "started_at": "2026-05-14T21:4
…[truncated 2062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T19:44:21.811306+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "report.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "report.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T19:44:21.811620+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-15T19:41:58Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 75 个实验 — ALLOCATED 1, ANALYZING 2, DONE 66, PREPARING 2, QUEUED 1, RUNNING 3\\n**DONE 分布**: failed 12, killed 14, negative 8, success 32\\n\\n### GPU 占用\\n- **分配**: 4 张 — rtx5090-4x:cuda:0, rtx5090-4x:cuda:1, rtx5090-4x:cuda:2, rtx5090-4x:cuda:3\\n- **实际运行**: 3 张 — rtx5090-4x:cuda:3(plan_008_rsft_topk3), rtx5090-4x:cuda:0(plan_001_flat_nli_seed43), rtx5090-4x:cuda:2(plan_012_dpo_ced_1ep)\\n- **空闲（分配了没跑）**: rtx5090-4x:cuda:1\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `plan_008_rsft_topk3` | rtx5090-4x | cuda:3 | 234489 | `~/runs/faith-evidence-ie/plan_008_rsft_topk3.log` |\\n| `plan_001_flat_nli_seed43` | rtx5090-4x | cuda:0 | 236774 | `~/runs/faith-evidence-ie/plan_001_flat_nli_seed43.log` |\\n| `plan_012_dpo_ced_1ep` | rtx5090-4x | cuda:2 | 244627 | `~/runs/faith-evidence-ie/plan_012_dpo_ced_1ep.log` |\\n\\n### 📌 最近完成 (top 5)\\n- `plan_009_flatnli_reward_eval` [failed] — 2026-05-15T19:39:02\\n- `eval_plan_012_dpo_ced_ckpt400` [failed] — 2026-05-15T19:37:31\\n- `plan_009_forgetting_figure` [success] — 2026-05-15T18:57:17\\n- `eval_plan_014_sft_no_evidence` [success] — 2026-05-15T18:42:46\\n- `plan_014_sft_no_evidence` [success] — 2026-05-15T18:42:28\\n\\n### 🔴 最近失败原因 (top 3)\\n- `plan_009_flatnli_reward_eval`: _(no failure_reason — pre-2026-04-24 entry)_\\n- `eval_plan_012_dpo_ced_ckpt400`: _(no failure_reason — pre-2026-04-24 entry)_\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan_012_dpo_ced_1ep | DPO+CED 1 epoch retraining: plan_01
…[truncated 2748 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T19:44:21.811943+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_baseline_noquant",
  "field": "metrics",
  "value": "{'rel_f1': 0.4106, 'rel_precision': 0.4198, 'rel_recall': 0.4019, 'evi_f1': 0.8013, 'evi_precision': 0.8005, 'evi_recall': 0.8022, 'evi_f1_joint': 0.3216, 'edcr': 0.7039, 'format_ok_rate': 0.998, 'field_compliance_rate': 0.7066, 'n_predictions': 16774, 'n_truncated': 288, 'n_documents': 985, 'inference_time_seconds': 3677.9}",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_baseline_noquant",
    "field": "metrics",
    "value": "{'rel_f1': 0.4106, 'rel_precision': 0.4198, 'rel_recall': 0.4019, 'evi_f1': 0.8013, 'evi_precision': 0.8005, 'evi_recall': 0.8022, 'evi_f1_joint': 0.3216, 'edcr': 0.7039, 'format_ok_rate': 0.998, 'field_compliance_rate': 0.7066, 'n_predictions': 16774, 'n_truncated': 288, 'n_documents': 985, 'inference_time_seconds': 3677.9}",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T19:44:21.812258+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_baseline_noquant\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:38:33.128Z\", \"updated_at\": \"2026-05-15T19:43:52.669Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --no-quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"237912\", \"log_path\": \"~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log\", \"submitted_at\": \"2026-05-15T18:38:45.042Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B (SFT baseline, no-quantize)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"docred dev (985 docs)\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:41:54.062Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:41:59.716746+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4106, \"rel_precision\": 0.4198, \"rel_recall\": 0.4019, \"evi_f1\": 0.8013, \"evi_precision\": 0.8005, \"evi_recall\": 0.8022, \"evi_f1_joint\": 0.3216, \"edcr\": 0.7039, \"format_ok_rate\": 0.998, \"field_compliance_rate\": 0.7066, \"n_predictions\": 16774, \"n_truncated\": 288, \"n_documents\": 985, \"inference_time_seconds\": 3677.9}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.716}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T19:44:21.812485+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_baseline_noquant",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_baseline_noquant",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T19:44:21.812754+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_baseline_noquant\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:38:33.128Z\", \"updated_at\": \"2026-05-15T19:43:53.576Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --no-quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"237912\", \"log_path\": \"~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log\", \"submitted_at\": \"2026-05-15T18:38:45.042Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B (SFT baseline, no-quantize)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"docred dev (985 docs)\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:41:54.062Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:41:59.716746+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4106, \"rel_precision\": 0.4198, \"rel_recall\": 0.4019, \"evi_f1\": 0.8013, \"evi_precision\": 0.8005, \"evi_recall\": 0.8022, \"evi_f1_joint\": 0.3216, \"edcr\": 0.7039, \"format_ok_rate\": 0.998, \"field_compliance_rate\": 0.7066, \"n_predictions\": 16774, \"n_truncated\": 288, \"n_documents\": 985, \"inference_time_seconds\": 3677.9}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5443}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T19:44:21.812987+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_baseline_noquant",
  "field": "conclusion",
  "value": "success",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_baseline_noquant",
    "field": "conclusion",
    "value": "success",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T19:44:21.813248+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_baseline_noquant\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:38:33.128Z\", \"updated_at\": \"2026-05-15T19:43:57.618Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --no-quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"237912\", \"log_path\": \"~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log\", \"submitted_at\": \"2026-05-15T18:38:45.042Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B (SFT baseline, no-quantize)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"docred dev (985 docs)\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:41:54.062Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:41:59.716746+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4106, \"rel_precision\": 0.4198, \"rel_recall\": 0.4019, \"evi_f1\": 0.8013, \"evi_precision\": 0.8005, \"evi_recall\": 0.8022, \"evi_f1_joint\": 0.3216, \"edcr\": 0.7039, \"format_ok_rate\": 0.998, \"field_compliance_rate\": 0.7066, \"n_predictions\": 16774, \"n_truncated\": 288, \"n_documents\": 985, \"inference_time_seconds\": 3677.9}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5273}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T19:44:21.813478+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_baseline_noquant",
  "field": "status",
  "value": "DONE",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_baseline_noquant",
    "field": "status",
    "value": "DONE",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T19:44:21.813771+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_baseline_noquant\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:38:33.128Z\", \"updated_at\": \"2026-05-15T19:44:01.274Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --no-quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"237912\", \"log_path\": \"~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log\", \"submitted_at\": \"2026-05-15T18:38:45.042Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B (SFT baseline, no-quantize)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"docred dev (985 docs)\", \"wall_clock_seconds\": 3916.2, \"gpu_hours\": 1.09}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:41:54.062Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:41:59.716746+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4106, \"rel_precision\": 0.4198, \"rel_recall\": 0.4019, \"evi_f1\": 0.8013, \"evi_precision\": 0.8005, \"evi_recall\": 0.8022, \"evi_f1_joint\": 0.3216, \"edcr\": 0.7039, \"format_ok_rate\": 0.998, \"field_compliance_rate\": 0.7066, \"n_predictions\": 16774, \"n_truncated\": 288, \"n_documents\": 985, \"inference_time_seconds\": 3677.9}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:44:01.274Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9835}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T19:44:21.814021+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_sft_baseline_noquant",
  "field": "notes",
  "value": "[2026-05-16] 无量化 SFT baseline eval 完成。rel_f1=0.4106 vs 量化版 0.4057 (+0.49pp), evi_f1=0.8013 vs 0.7979 (+0.34pp)。差异 <1pp，确认量化 confound 不显著（D058 排除）。所有基于量化 baseline 的对比结论仍然成立。无量化版推理时间 3678s vs 量化版 6139s（快 40%，因无量化用满 GPU 内存）。",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_sft_baseline_noquant",
    "field": "notes",
    "value": "[2026-05-16] 无量化 SFT baseline eval 完成。rel_f1=0.4106 vs 量化版 0.4057 (+0.49pp), evi_f1=0.8013 vs 0.7979 (+0.34pp)。差异 <1pp，确认量化 confound 不显著（D058 排除）。所有基于量化 baseline 的对比结论仍然成立。无量化版推理时间 3678s vs 量化版 6139s（快 40%，因无量化用满 GPU 内存）。",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T19:44:21.814340+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_sft_baseline_noquant\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:38:33.128Z\", \"updated_at\": \"2026-05-15T19:44:09.250Z\", \"spec\": {\"command\": \"python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output --base_model /root/autodl-tmp/models/Qwen3-4B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 42 --output_dir /root/autodl-tmp/eval_results/sft_baseline_noquant --no-quantize\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"237912\", \"log_path\": \"~/runs/faith-evidence-ie/eval_sft_baseline_noquant.log\", \"submitted_at\": \"2026-05-15T18:38:45.042Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 985, \"model_name\": \"Qwen3-4B (SFT baseline, no-quantize)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output\", \"eval_data\": \"docred dev (985 docs)\", \"wall_clock_seconds\": 3916.2, \"gpu_hours\": 1.09}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:41:54.062Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:41:59.716746+00:00\"}]}, \"metrics\": {\"rel_f1\": 0.4106, \"rel_precision\": 0.4198, \"rel_recall\": 0.4019, \"evi_f1\": 0.8013, \"evi_precision\": 0.8005, \"evi_recall\": 0.8022, \"evi_f1_joint\": 0.3216, \"edcr\": 0.7039, \"format_ok_rate\": 0.998, \"field_compliance_rate\": 0.7066, \"n_predictions\": 16774, \"n_truncated\": 288, \"n_documents\": 985, \"inference_time_seconds\": 3677.9}, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/sft_baseline_noquant/metrics.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:44:01.274Z\", \"notes\": \"[2026-05-16] 无量化 SFT baseline eval 完成。rel_f1=0.4106 vs 量化版 0.4057 (+0.49pp), evi_f1=0.8013 vs 0.7979 (+0.34pp)。差异 <
…[truncated 175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-15T19:44:21.814650+00:00_

Registry 已更新。总结：

## eval_sft_baseline_noquant 结果

| 指标 | 无量化 | 量化 | Δ |
|------|--------|------|---|
| **rel_f1** | **0.4106** | 0.4057 | **+0.49pp** |
| rel_precision | 0.4198 | — | — |
| rel_recall | 0.4019 | — | — |
| **evi_f1** | **0.8013** | 0.7979 | **+0.34pp** |
| evi_f1_joint | 0.3216 | 0.3117 | +0.99pp |
| edcr | 0.7039 | 0.7118 | -0.79pp |
| format_ok | 99.8% | 99.8% | = |
| truncated | 288/985 | 367/985 | −79 |
| inference_time | 3678s | 6139s | **−40%** |

**结论：量化 confound 不显著。** rel_f1 差异仅 +0.49pp（远低于 2pp 阈值），evi_f1 差异 +0.34pp。D058 担忧可以排除，之前所有基于量化 baseline (rel_f1=0.4057) 的对比结论仍然成立。

无量化 baseline 的 rel_f1=0.4106 对 RSFT/GRPO 的增益稍有压缩：
- RSFT CED: 0.4596 vs 0.4106 = **+4.90pp**（之前 vs 量化是 +5.39pp）
- RSFT flat-NLI: 0.4539 vs 0.4106 = **+4.33pp**
- bf16 GRPO ckpt-100: 0.4549 vs 0.4106 = **+4.43pp**

增益仍然显著（>4pp），方法有效性不受影响。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_eval_sft_baseline_noquant_20260515T194310"
}
```

</details>

---
