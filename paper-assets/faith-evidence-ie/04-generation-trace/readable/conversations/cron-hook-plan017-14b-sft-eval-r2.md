# cron hook plan017 14b sft eval r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 40
- **Recorded user turns:** 1
- **Tool calls:** 19
- **Original source:** `logs/chats/cron_hook_plan017_14b_sft_eval_r2.jsonl`
- **Structured JSON:** [`6ff668ee8d4e1a649f48.json`](../../sessions/6f/6ff668ee8d4e1a649f48.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

40 recorded events

### User

_source line 1 · 2026-05-19T13:53:41.265460+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: plan017_14b_sft_eval_r2
- project: faith-evidence-ie
- server: rtx5090-4x

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-19T13:53:57.823440+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__read_experiment_plan_with_status",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__read_experiment_plan_with_status",
    "max_results": "8"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-19T13:53:57.875169+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T13:54:02.965048+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "fields": "['*']",
  "filters": "{'exp_id': 'plan017_14b_sft_eval_r2'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "fields": "['*']",
    "filters": "{'exp_id': 'plan017_14b_sft_eval_r2'}"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T13:54:03.317012+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "limit": "20"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T13:54:03.819588+00:00_

called mcp__agent-ml-research__reconcile_crons

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons</summary>

```json
Arguments not recorded in this source.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T13:54:04.172894+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9889}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1207
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T13:54:04.173378+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "report.md"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T13:54:04.173645+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T13:54:04.959846+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan019_8b_rsft_no_evidence_eval_r2\": {\"status\": \"ALLOCATED\", \"created_at\": \"2026-05-19T13:44:38.870Z\", \"updated_at\": \"2026-05-19T13:53:45.324Z\", \"hypothesis\": \"8B RSFT no-evidence eval r2: 移除 evidence 输出后测量 8B RSFT 的 evidence tax。8B RSFT with-evidence mean ign_f1=0.5414 (s42=0.5376, s44=0.5451)。若 no-evidence ign_f1 > with-evidence，证实 evidence 生成对 8B RE 的性能代价；与 1.7B/4B/14B evidence tax 配合构建跨尺度 scaling curve (Claim 3)。修正 r1 的 cuda:2 冲突问题，改用 cuda:0。\", \"parent\": \"plan019_8b_rsft_no_evidence_eval\"}, \"plan017_14b_sft_eval_r2\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-19T08:51:48.518Z\", \"updated_at\": \"2026-05-19T13:53:33.563Z\", \"hypothesis\": \"D076 eval for 14B SFT baseline (bf16, --no-quantize). 修正 r1 的 D076 违规（r1 用了 int8 量化）。14B 是第 4 个 scale 档，SFT baseline 用于计算 RSFT 增益和 evidence tax。预期 ign_f1 高于 8B SFT mean (0.4866)。\", \"parent\": \"plan017_14b_sft\"}, \"d112_rsft_no_evidence_eval_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:41:03.808Z\", \"updated_at\": \"2026-05-19T13:45:20.995Z\", \"hypothesis\": \"4B RSFT no-evidence eval (D112 bf16 SFT s44 base): 移除 evidence 输出后测量 4B RSFT 的 evidence tax。对比 with-evidence 的 canonical 4B RSFT ign_f1，验证 evidence 生成对 4B RE 性能的代价。与 1.7B/8B/14B no-evidence eval 配合构建跨尺度 evidence tax scaling curve (Claim 3)。\", \"parent\": \"d112_rsft_s44_eval_bf16\", \"conclusion\": \"failed\"}, \"plan019_8b_rsft_no_evidence_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:12:23.195Z\", \"updated_at\": \"2026-05-19T13:44:36.625Z\", \"hypothesis\": \"8B RSFT no-evidence eval: 移除 evidence 输出后测量 8B RSFT 的 evidence tax。8B RSFT with-evidence mean ign_f1=0.5414 (s42=0.5376, s44=0.5451)。若 no-evidence ign_f1 > with-evidence，证实 evidence 生成对 8B RE 的性能代价；与 1.7B/4B/14B evidence tax 配合构建跨尺度 scaling curve (Claim 3)。\", \"parent\": \"plan019_8b_rsft_s44_eval\", \"conclusion\": \"killed\"}, \"d112_rsft_no_evidence_eval\": {\"status\": \"D
…[truncated 8060 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1642
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T13:54:10.351185+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 2, \"results\": [{\"exp_id\": \"plan019_1_7b_rsft_no_evidence_eval\", \"success\": true, \"actions\": [\"Job still running (pid=679713)\"]}, {\"exp_id\": \"plan019_8b_sft_s43\", \"success\": true, \"actions\": [\"Job still running (pid=683937)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 6531
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T13:54:10.402337+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/report.md\", \"content\": \"# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| d112_rsft_s44_eval_bf16 | D112 step 4 bf16: D076 eval for RSFT trained on SFT s44 base with CED k=1 scored data (bf16 LoRA). 修正原 d112_rsft_s44_eval 的 QLoRA confound。预期 ign_f1 > 0.4734 (SFT s44 baseline)。 | — | — | — |\\n| plan019_8b_sft_s43 | 8B SFT seed=43: 补齐第 3 seed 改善 '1.7B RSFT surpasses 8B SFT' claim 统计力（当前 p≈0.20，瓶颈在 8B SFT 仅 2 seeds）。Reviewer 建议，对应 plan_019 Claim 3。 | — | — | — |\\n| plan019_1_7b_rsft_no_evidence_eval | 1.7B RSFT s42 no-evidence eval: 测量 evidence tax。移除 evidence 输出后，模型可以将全部容量用于关系预测，预期 ign_f1 高于 with-evidence 的 0.5122，验证 evidence 输出对 RE 性能的代价。 | — | — | — |\\n\\n## 待处理\\n- plan019_8b_rsft_no_evidence_eval_r2: 8B RSFT no-evidence eval r2: 移除 evidence 输出后测量 8B RSFT 的 evidence tax。8B RSFT with-evidence mean ign_f1=0.5414 (s42=0.5376, s44=0.5451)。若 no-evidence ign_f1 > with-evidence，证实 evidence 生成对 8B RE 的性能代价；与 1.7B/4B/14B evidence tax 配合构建跨尺度 scaling curve (Claim 3)。修正 r1 的 cuda:2 冲突问题，改用 cuda:0。（已分配 ? GPU:?，等待提交）\\n\\n## 近期结论\\n- **d112_rsft_no_evidence_eval_r2** (failed): 4B RSFT no-evidence eval (D112 bf16 SFT s44 base): 移除 evidence 输出后测量 4B RSFT 的 evidence tax。对比 with-evidence 的 canonical 4B RSFT ign_f1，验证 evidence 生成对 4B RE 性能的代价。与 1.7B/8B/14B no-evidence eval 配合构建跨尺度 evidence tax scaling curve (Claim 3)。 ← 基于 d112_rsft_s44_eval_bf16\\n- **plan019_8b_rsft_no_evidence_eval** (killed): 8B RSFT no-evidence eval: 移除 evidence 输出后测量 8B RSFT 的 evidence tax。8B RSFT with-evidence mean ign_f1=0.5414 (s42=0.5376, s44=0.5451)。若 no-evidence ign_f1 > with-evidence，证实 evidence 生成对 8B RE 的性能代价；与 1.7B/4B/14B evidence tax 配合构建跨尺度 scaling curve (Claim 3)。 ← 基于 plan019_8b_rsft_s44_eval\\n- **d112_rsft_no_evidence_eval** (failed): 4B RSFT no-evidence
…[truncated 4812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 6228
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T13:54:10.403027+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成\\n\\n## 核心方向\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\n- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）\\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）\\n- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）\\n- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）\\n- **关键数值汇总**:\\n\\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\\n|-------|-------------------|--------------------|----------|---------|----------|\\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |\\n| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |\\n\\n- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)\\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\\n\\n## 投稿目标\\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\\n\\n## 实验路线（3 层优先级）\\n\\n### Tier 1 — Main 必要条件\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅
…[truncated 3461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 6229
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T13:54:19.149943+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'status': 'ANALYZING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'status': 'ANALYZING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T13:54:20.660817+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan017_14b_sft_eval_r2\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T08:51:48.518Z\", \"updated_at\": \"2026-05-19T13:53:33.563Z\", \"hypothesis\": \"D076 eval for 14B SFT baseline (bf16, --no-quantize). 修正 r1 的 D076 违规（r1 用了 int8 量化）。14B 是第 4 个 scale 档，SFT baseline 用于计算 RSFT 增益和 evidence tax。预期 ign_f1 高于 8B SFT mean (0.4866)。\", \"parent\": \"plan017_14b_sft\", \"spec\": {\"command\": \"bash scripts/14b/eval_14b_sft.sh\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"pid\": 633106, \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": 998, \"model_name\": \"Qwen3-14B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_14b/\", \"eval_data\": \"/root/autodl-tmp/data/docred/dev.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T13:53:32.084Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T13:53:40.349959+00:00\"}]}}}, \"count\": 1, \"total\": 1, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.042}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1510
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T13:54:21.265781+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__compute_coverage_matrix",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__compute_coverage_matrix",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T13:54:21.266320+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T13:54:21.668617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T13:54:21.719842+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/agent_3078f375.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T13:54:37.413539+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_on_allocated,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__get_project_resource_usage",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_on_allocated,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__get_project_resource_usage",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T13:54:37.413919+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T13:54:37.765569+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "faith-evidence-ie",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "faith-evidence-ie",
    "status": "running"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-19T13:54:37.866460+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_research_find_4b_rsft_s42_canonical_20260519T135415\", \"task_type\": \"research:find_4b_rsft_s42_canonical\", \"project\": \"faith-evidence-ie\", \"status\": \"running\", \"started_at\": \"2026-05-19T13:54:15.710594+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T13:54:49.928361+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'plan019_8b_rsft_no_evidence_eval_r2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'plan019_8b_rsft_no_evidence_eval_r2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T13:54:50.430988+00:00_

called mcp__agent-ml-research__get_project_resource_usage

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_project_resource_usage</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T13:55:09.559452+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2362}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 19631
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T13:55:09.560008+00:00_

{"result":"{\"success\": true, \"data\": {\"allocated_gpus\": [{\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:0\"}, {\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:1\"}, {\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:2\"}, {\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:3\"}], \"actually_running_gpus\": [{\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:3\", \"exp_id\": \"plan019_1_7b_rsft_no_evidence_eval\"}, {\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:3\", \"exp_id\": \"plan019_8b_sft_s43\"}, {\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"d112_rsft_s44_eval_bf16\"}], \"allocated_but_idle\": [{\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:0\", \"idle_min\": null, \"util_pct\": null}, {\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:1\", \"idle_min\": null, \"util_pct\": null}], \"registered_but_hw_idle\": [], \"unregistered_but_hw_active\": [], \"running_experiments\": [{\"exp_id\": \"plan019_1_7b_rsft_no_evidence_eval\", \"gpus\": [\"cuda:3\"], \"util_avg\": null}, {\"exp_id\": \"plan019_8b_sft_s43\", \"gpus\": [\"cuda:3\"], \"util_avg\": null}, {\"exp_id\": \"d112_rsft_s44_eval_bf16\", \"gpus\": [\"cuda:2\"], \"util_avg\": null}], \"worker_pool\": {\"total\": 1, \"gpu_tasks\": 0, \"cpu_tasks\": 1, \"details\": [{\"worker_id\": \"worker_research_find_4b_rsft_s42_canonical_20260519T135415\", \"task\": \"research:find_4b_rsft_s42_canonical\"}]}, \"summary\": \"分配 4 张, 实际跑 3 张 ⚠️ | Worker 1 (GPU 0 / CPU 1)\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "elapsed_ms": 19129
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T13:55:09.861736+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "analysis:plan017_14b_sft_eval_r2",
  "project": "faith-evidence-ie",
  "task_prompt": "## 任务：分析 14B SFT eval 结果\n\n实验 `plan017_14b_sft_eval_r2` 已完成（进程正常退出），需要提取 eval metrics。\n\n### 背景\n- 实验：14B SFT baseline eval (bf16, --no-quantize)，修正 r1 的 D076 违规（r1 用了 int8 量化）\n- 服务器：rtx5090-4x\n- 命令：`bash scripts/14b/eval_14b_sft.sh`\n- GPU：cuda:1\n- checkpoint_source: /root/autodl-tmp/sft_output_14b/\n- eval_data: /root/autodl-tmp/data/docred/dev.json\n- 14B 是第 4 个 scale 档，SFT baseline 用于计算 RSFT 增益和 evidence tax\n- 预期 ign_f1 高于 8B SFT mean (0.4866)\n\n### 你需要做的\n1. SSH 到 rtx5090-4x，找到 eval 输出日志。可能的位置：\n   - 标准输出重定向的日志文件（检查 /root/autodl-tmp/ 或项目目录下的 logs/ 目录）\n   - tmux session 的输出\n   - 检查 `ls -lt /root/autodl-tmp/sft_output_14b/` 看有没有 eval 结果文件\n   - 检查 `/root/autodl-tmp/faith-evidence-ie/` 或类似项目目录下的日志\n   - 用 `find /root/autodl-tmp/ -name \"*14b*eval*\" -o -name \"*metrics*\" -mmin -120 2>/dev/null | head -20` 搜索近期文件\n   - 检查 tmux: `tmux ls` 然后 `tmux capture-pane -t &lt;session> -p -S -500`\n\n2. 提取关键 metrics：\n   - ign_f1, ign_precision, ign_recall（最重要）\n   - f1, precision, recall\n   - format_compliance_rate\n   - n_truncated\n   - inference_time_seconds\n   - 如果有 evidence 相关指标也提取：evi_precision, evi_recall, evi_f1, edcr\n\n3. 找到 checkpoint_path 和 log_path 的确切位置\n\n4. 将所有提取的 metrics 用 `update_registry` 写入：\n   ```\n   update_registry(exp_id=\"plan017_14b_sft_eval_r2\", field=\"metrics\", value={...}, project=\"faith-evidence-ie\")\n   ```\n\n5. 判断 conclusion：\n   - 如果 ign_f1 > 0.4866（8B SFT mean），说明 14B 确实比 8B 强 → conclusion = \"success\"\n   - 如果 ign_f1 ≤ 0.4866，说明 14B 没有如预期提升 → conclusion = \"negative\"\n   \n6. 设置 conclusion：\n   ```\n   update_registry(exp_id=\"plan017_14b_sft_eval_r2\", field=\"conclusion\", value=\"success\"或\"negative\", project=\"faith-evidence-ie\")\n   ```\n\n7. 设置 checkpoint_path 和 log_path：\n   ```\n   update_registry(exp_id=\"plan017_14b_sft_eval_r2\", field=\"spec\", value={\"checkpoint_path\": \"...\", \"log_path\": \"...\"}, project=\"faith-evidence-ie\", spec={\"checkpoint_path\": \"...\", \"log_path\": \"...\"})\n   ```\n\n### 对比参考\n- 14B SFT no-evidence eval (plan017_14b_sft_no_evidence_eval_r2): ign_f1=0.551\n- 8B SFT mean: 0.4866 (s42=0.5128, s44=0.4604)\n- 4B SFT mean: 0.4358\n- 1.7B SFT mean: 0.4464\n\n### 重要\n- 只用 ssh_read_only 读取日志和结果，不要用 ssh_execute\n- 完成后确保 registry 中 metrics、conclusion、checkpoint_path、log_path 都已更新",
  "tool_groups": "['ssh', 'registry']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analysis:plan017_14b_sft_eval_r2",
    "project": "faith-evidence-ie",
    "task_prompt": "## 任务：分析 14B SFT eval 结果\n\n实验 `plan017_14b_sft_eval_r2` 已完成（进程正常退出），需要提取 eval metrics。\n\n### 背景\n- 实验：14B SFT baseline eval (bf16, --no-quantize)，修正 r1 的 D076 违规（r1 用了 int8 量化）\n- 服务器：rtx5090-4x\n- 命令：`bash scripts/14b/eval_14b_sft.sh`\n- GPU：cuda:1\n- checkpoint_source: /root/autodl-tmp/sft_output_14b/\n- eval_data: /root/autodl-tmp/data/docred/dev.json\n- 14B 是第 4 个 scale 档，SFT baseline 用于计算 RSFT 增益和 evidence tax\n- 预期 ign_f1 高于 8B SFT mean (0.4866)\n\n### 你需要做的\n1. SSH 到 rtx5090-4x，找到 eval 输出日志。可能的位置：\n   - 标准输出重定向的日志文件（检查 /root/autodl-tmp/ 或项目目录下的 logs/ 目录）\n   - tmux session 的输出\n   - 检查 `ls -lt /root/autodl-tmp/sft_output_14b/` 看有没有 eval 结果文件\n   - 检查 `/root/autodl-tmp/faith-evidence-ie/` 或类似项目目录下的日志\n   - 用 `find /root/autodl-tmp/ -name \"*14b*eval*\" -o -name \"*metrics*\" -mmin -120 2>/dev/null | head -20` 搜索近期文件\n   - 检查 tmux: `tmux ls` 然后 `tmux capture-pane -t &lt;session> -p -S -500`\n\n2. 提取关键 metrics：\n   - ign_f1, ign_precision, ign_recall（最重要）\n   - f1, precision, recall\n   - format_compliance_rate\n   - n_truncated\n   - inference_time_seconds\n   - 如果有 evidence 相关指标也提取：evi_precision, evi_recall, evi_f1, edcr\n\n3. 找到 checkpoint_path 和 log_path 的确切位置\n\n4. 将所有提取的 metrics 用 `update_registry` 写入：\n   ```\n   update_registry(exp_id=\"plan017_14b_sft_eval_r2\", field=\"metrics\", value={...}, project=\"faith-evidence-ie\")\n   ```\n\n5. 判断 conclusion：\n   - 如果 ign_f1 > 0.4866（8B SFT mean），说明 14B 确实比 8B 强 → conclusion = \"success\"\n   - 如果 ign_f1 ≤ 0.4866，说明 14B 没有如预期提升 → conclusion = \"negative\"\n   \n6. 设置 conclusion：\n   ```\n   update_registry(exp_id=\"plan017_14b_sft_eval_r2\", field=\"conclusion\", value=\"success\"或\"negative\", project=\"faith-evidence-ie\")\n   ```\n\n7. 设置 checkpoint_path 和 log_path：\n   ```\n   update_registry(exp_id=\"plan017_14b_sft_eval_r2\", field=\"spec\", value={\"checkpoint_path\": \"...\", \"log_path\": \"...\"}, project=\"faith-evidence-ie\", spec={\"checkpoint_path\": \"...\", \"log_path\": \"...\"})\n   ```\n\n### 对比参考\n- 14B SFT no-evidence eval (plan017_14b_sft_no_evidence_eval_r2): ign_f1=0.551\n- 8B SFT mean: 0.4866 (s42=0.5128, s44=0.4604)\n- 4B SFT mean: 0.4358\n- 1.7B SFT mean: 0.4464\n\n### 重要\n- 只用 ssh_read_only 读取日志和结果，不要用 ssh_execute\n- 完成后确保 registry 中 metrics、conclusion、checkpoint_path、log_path 都已更新",
    "tool_groups": "['ssh', 'registry']"
  }
}
````

</details>

---

### Tool result

_source line 29 · 2026-05-19T13:55:13.031722+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_plan017_14b_sft_eval_r2_20260519T135510\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/logs/workers/worker_analysis_plan017_14b_sft_eval_r2_20260519T135510.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_plan017_14b_sft_eval_r2_20260519T135510 started. Use get_worker_status('worker_analysis_plan017_14b_sft_eval_r2_20260519T135510') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 3169
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-19T13:55:45.188162+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'plan019_8b_rsft_no_evidence_eval'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'plan019_8b_rsft_no_evidence_eval'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T13:55:45.691969+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'status': 'ALLOCATED'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'status': 'ALLOCATED'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T13:55:45.945402+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.745}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 757
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T13:55:46.751588+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7772}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1059
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-19T13:56:20.988534+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T13:56:21.692419+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T13:56:21.894098+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan019_8b_rsft_no_evidence_eval_r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:44:38.870Z\", \"updated_at\": \"2026-05-19T13:54:52.747Z\", \"hypothesis\": \"8B RSFT no-evidence eval r2: 移除 evidence 输出后测量 8B RSFT 的 evidence tax。8B RSFT with-evidence mean ign_f1=0.5414 (s42=0.5376, s44=0.5451)。若 no-evidence ign_f1 > with-evidence，证实 evidence 生成对 8B RE 的性能代价；与 1.7B/4B/14B evidence tax 配合构建跨尺度 scaling curve (Claim 3)。修正 r1 的 cuda:2 冲突问题，改用 cuda:0。\", \"parent\": \"plan019_8b_rsft_no_evidence_eval\", \"plan_id\": \"plan_019\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && GPU=0 bash scripts/seed_expansion/eval_8b_rsft_no_evidence.sh\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"698772\", \"log_path\": \"~/runs/faith-evidence-ie/plan019_8b_rsft_no_evidence_eval_r2.log\", \"submitted_at\": \"2026-05-19T13:54:48.828Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"698772\", \"log_path\": \"~/runs/faith-evidence-ie/plan019_8b_rsft_no_evidence_eval_r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && GPU=0 bash scripts/seed_expansion/eval_8b_rsft_no_evidence.sh\\\"\"}}, \"d112_rsft_s44_eval_bf16\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:04:19.692Z\", \"updated_at\": \"2026-05-19T13:16:48.504Z\", \"hypothesis\": \"D112 step 4 bf16: D076 eval for RSFT trained on SFT s44 base with CED k=1 scored data (bf16 LoRA). 修正原 d112_rsft_s44_eval 的 QLoRA confound。预期 ign_f1 > 0.4734 (SFT s44 baseline)。\", \"parent\": \"d112_rsft_s44_train_bf16\", \"spec\": {\"command\": \"bash /root/autodl-tmp/freige/scripts/d112/eval_d112_rsft_bf16.sh\", \"server\": \"rtx5090-4x\", \"g
…[truncated 1396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 905
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-19T13:56:21.894846+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# Project Memory\\n\\n## RSFT 方差压缩效应 (2026-05-19)\\n\\n**发现**: RSFT 在所有尺度显著压缩跨 seed 方差，且压缩倍数随模型容量递减：\\n\\n| Scale | SFT std | RSFT std | 压缩倍数 | SFT n | RSFT n |\\n|-------|---------|----------|---------|-------|--------|\\n| 1.7B | 2.79pp | 0.09pp | **31x** | 3 | 3 |\\n| 4B | 3.80pp | 0.51pp | **7.5x** | 3 | 3 |\\n| 8B | 2.62pp | 0.53pp | **5x** | 2 | 2 |\\n\\n**解释**: RSFT 的 CED 筛选过程相当于对训练数据施加 quality filter，减少了因随机种子导致的训练轨迹分歧。小模型更容易受数据噪声影响，所以压缩效应最强(31x)。大模型本身已较稳定(SFT std 较低)，RSFT 仍能进一步压缩(5x)。\\n\\n**论文意义**: 这是 RSFT 独立于 ign_f1 提升的第二个贡献维度——训练稳定性。可作为 Claim 1 的补充叙事：\\\"RSFT not only improves performance but dramatically stabilizes training outcomes across random seeds.\\\"\\n\\n**注意**: 1.7B RSFT 所有 3 seeds 使用 Method A（s42 SFT base + s42 CED data，仅变 RSFT seed），压缩效应测量的是 RSFT 训练过程本身的稳定性，不含 SFT base 变异。8B RSFT 使用相同方法（s42 SFT base），但仅 2 seeds。\\n\\n## plan_021: Deep Error Analysis — RSFT vs SFT (2026-05-19)\\n\\n**Files**: `scripts/analysis/deep_error_analysis.py` → `scripts/analysis/results/`\\n\\n**Models compared** (all dev set, seed 42 eval):\\n- 4B SFT: `d111_4b_sft_s42_reeval` (ign_f1=0.397)\\n- 4B RSFT: `rsft_s43_dev_eval_preds` (train seed 43, ign_f1=0.451) — NOTE: s42 predictions unavailable, used s43 model\\n- 8B SFT: `qwen3_8b_sft_eval` (ign_f1=0.505)\\n- 8B RSFT: `d102_8b_k1_s42` (ign_f1=0.538)\\n\\n### Key Findings\\n\\n**Per-Relation F1 (171 unique relations in predictions)**:\\n- 4B largest gains: original network (+0.32, gold=38), award received (+0.16, gold=66), cast member (+0.14, gold=225), performer (+0.13, gold=320)\\n- 4B largest losses: chairperson (-0.16, gold=21), screenwriter (-0.09, gold=35), genre (-0.09, gold=14)\\n- Pattern: RSFT helps most on mid-frequency entertainment/media relations where SFT under-performs. Losses concentrated on low-frequency relations (gold < 40).\\n- 8B gains are mor
…[truncated 7306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 202
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-19T13:56:54.503415+00:00_

called mcp__agent-ml-research__read_experiment_plan_with_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_experiment_plan_with_status</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_experiment_plan_with_status",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T13:56:55.663040+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": [{\"id\": \"plan_001\", \"claim\": 2, \"description\": \"CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选 RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py 用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。\", \"priority\": \"P0\", \"gpu_budget_hours\": 20, \"deps\": [], \"registry_id\": \"eval_flat_nli_seed45\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.455052, \"ign_f1\": 0.446181, \"evi_f1\": 0.815399, \"edcr\": 0.652133, \"evi_f1_joint\": 0.355612}}, {\"id\": \"plan_002\", \"claim\": 1, \"description\": \"Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set 上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。\", \"priority\": \"P0\", \"gpu_budget_hours\": 4, \"deps\": [\"plan_001\"], \"registry_id\": \"plan_002_test_rsft_s44\", \"status\": \"DONE\", \"conclusion\": \"success\"}, {\"id\": \"plan_003\", \"claim\": 4, \"description\": \"EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing 方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。\", \"priority\": \"P0\", \"gpu_budget_hours\": 2, \"deps\": [\"plan_001\"], \"registry_id\": \"plan_003_edcr_diagnostic\", \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"methods_evaluated\": 15, \"edcr_vs_rel_f1_spearman\": -0.9648, \"edcr_vs_rel_f1_pvalue\": 0.0001, \"edcr_vs_evi_f1_spearman\": 0.0022, \"edcr_vs_evi_f1_pvalue\": 0.9941, \"edcr_range\": \"0.63-0.99\", \"unique_diagnostic_value\": \"identifies pathological models (GRPO QLoRA) with high evi_f1 but catastrophically low rel_f1\"}}, {\"id\": \"plan_004\", \"claim\": 1, \"description\": \"DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large) 的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。\", \"priority\": \"P0\", \"gpu_budget_hours\": 8, \"deps\": [], \"registry_id\": \"plan_004_dreeam_baseline\", \"status\": \"DONE\", 
…[truncated 15308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_sft_eval_r2",
  "tool": "mcp__agent-ml-research__read_experiment_plan_with_status",
  "elapsed_ms": 1159
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-19T13:58:41.628609+00:00_

当前状态清晰了。让我总结：

**GPU 状态：**
- cuda:0: `plan019_8b_rsft_no_evidence_eval_r2` (RUNNING, 已被自动提交)
- cuda:1: **空闲** — 14B eval 刚完成
- cuda:2: `d112_rsft_s44_eval_bf16` (RUNNING)
- cuda:3: `plan019_1_7b_rsft_no_evidence_eval` + `plan019_8b_sft_s43` (RUNNING)

**Worker 池：** 2 (research:find_4b_rsft_s42_canonical + analysis:plan017_14b_sft_eval_r2)

已派 Worker 分析 `plan017_14b_sft_eval_r2` 的 eval 结果（SSH 读日志提取 metrics）。等待 Worker 回调后：
1. 更新 registry（metrics + conclusion）
2. 更新 report.md
3. 向 Director 汇报 14B SFT baseline 结果
4. 提议 cuda:1 下一步任务（14B RSFT 候选生成是 Tier 2 最高优先级）

cuda:1 空闲是当前瓶颈，Worker 回调后立即处理。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:plan017_14b_sft_eval_r2"
}
```

</details>

---
