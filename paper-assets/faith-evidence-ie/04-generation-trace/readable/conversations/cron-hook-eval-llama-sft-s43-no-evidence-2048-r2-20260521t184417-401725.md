# cron hook eval llama sft s43 no evidence 2048 r2 20260521T184417 401725

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 3
- **Tool calls:** 15
- **Original source:** `logs/chats/archive/cron_hook_eval_llama_sft_s43_no_evidence_2048_r2_20260521T184417_401725.jsonl`
- **Structured JSON:** [`aefb5333c3dabf6f6826.json`](../../sessions/ae/aefb5333c3dabf6f6826.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-21T02:40:30.835940+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: eval_llama_sft_s43_no_evidence_2048_r2
- project: faith-evidence-ie
- server: rtx5090-4x
- log_path: ~/runs/faith-evidence-ie/eval_llama_sft_s43_no_evidence_2048_r2.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-21T02:40:44.825589+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__fetch_wandb_metrics",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__fetch_wandb_metrics",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-21T02:40:44.876464+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T02:40:48.851780+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
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

### Tool call

_source line 5 · 2026-05-21T02:40:49.304483+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T02:40:49.808098+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
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

_source line 7 · 2026-05-21T02:40:50.312345+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T02:40:50.414693+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
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

_source line 9 · 2026-05-21T02:40:50.579415+00:00_

Error: result (515,044 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie--claude-sessions-agent-15ab4311/31a63d90-c6fd-457b-9d4d-f23cebe36cb6/tool-results/mcp-agent-ml-research-read_registry-1779331250518.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie--claude-sessions-agent-15ab4311/31a63d90-c6fd-457b-9d4d-f23cebe36cb6/tool-results/mcp-agent-ml-research-read_registry-1779331250518.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1727
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T02:40:57.731147+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 2, \"results\": [{\"exp_id\": \"eval_llama_sft_s44_with_evidence_2048\", \"success\": true, \"actions\": [\"Job still running (pid=64023)\"]}, {\"exp_id\": \"eval_llama_sft_s43_with_evidence_2048\", \"success\": true, \"actions\": [\"Job still running (pid=64391)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 8426
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T02:40:57.782946+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-21T02:40:30Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 268 个实验 — ANALYZING 1, DONE 264, RUNNING 3\\n**DONE 分布**: failed 57, killed 33, negative 18, success 156\\n\\n### GPU 占用\\n- **分配**: 4 张 — rtx5090-4x:cuda:0, rtx5090-4x:cuda:1, rtx5090-4x:cuda:2, rtx5090-4x:cuda:3\\n- **实际运行**: 3 张 — rtx5090-4x:cuda:0(plan017_14b_rsft_eval), rtx5090-4x:cuda:3(eval_llama_sft_s44_with_evidence_2048), rtx5090-4x:cuda:2(eval_llama_sft_s43_with_evidence_2048)\\n- **空闲（分配了没跑）**: rtx5090-4x:cuda:1\\n\\n### 💾 磁盘余量\\n- **rtx5090-4x**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/usr/bin/nvidia-smi`: 815G/879G 可用（已用 3%）\\n- **bjb2-12179**:\\n  - `/autodl-pub`: 8.6T/14T 可用（已用 39%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `plan017_14b_rsft_eval` | rtx5090-4x | cuda:0 | 53413 | `—` |\\n| `eval_llama_sft_s44_with_evidence_2048` | rtx5090-4x | cuda:3 | 64023 | `/tmp/eval_llama_sft_s44_with_evidence_2048.log` |\\n| `eval_llama_sft_s43_with_evidence_2048` | rtx5090-4x | cuda:2 | 64391 | `…eige/eval_outputs/eval_llama_sft_s43_with_evidence_2048.log` |\\n\\n### 📌 最近完成 (top 5)\\n- `eval_llama_sft_s42_with_evidence_2048` [success] — 2026-05-21T00:42:33\\n- `plan017_14b_rsft_no_evidence_eval` [success] — 2026-05-21T00:41:38\\n- `eval_llama_sft_s43_no_evidence_2048` [failed] — 2026-05-20T22:29:07 — EXIT_CODE=124 (timeout — exceeded timeout_hours)\\n- `eval_llama_sft_s42_no_evidence_2048` [success] — 2026-05-20T21:16:45\\n- `plan017_14b_rsft_generate_r4` [success] — 2026-05-20T21:13:54\\n\\n### 🔴 最近失败原因 (top 3)\\n- `eval_llama_sft_s43_no_evidence_2048`: EXIT_CODE=124 (timeout — exceeded timeout
…[truncated 6724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 7974
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T02:40:57.783694+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-20 07:31 UTC | 更新原因: 服务器迁移: westd-37389 (4×RTX PRO 6000 96GB), 数据完好从 bjb2 迁移中\\n\\n## 核心方向\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\n- **服务器迁移中**: bjb2-12179 → westd-37389 (4× RTX PRO 6000, 96GB VRAM/卡, 350GB disk)\\n- **数据状况**: bjb2 上全部完好（adapters + 14B gen 62% + eval results），迁移中\\n- **D130**: LLaMA 全系列 ign_f1 审计完成，论文数据正确\\n\\n| Scale | SFT ign_f1 (seeds) | RSFT ign_f1 (seeds) | Δ | Variance compression |\\n|-------|---------------------|----------------------|---|---------------------|\\n| 1.7B | 0.4464 (3) | 0.5119 (3) | +6.55pp | **31×** (2.79→0.09pp) |\\n| 4B | 0.4358 (3) | 0.4482 (3, A) / 0.5152 (1, B) | +1.24/+4.18pp | **7.5×** (3.80→0.51pp) |\\n| 8B | 0.5019 (3) | 0.5433 (3) | +4.14pp | **7.4×** (3.72→0.50pp) |\\n| 14B | 0.5507 (1) | 🔄 gen 62% done, resume pending | — | — |\\n| LLaMA-8B | 0.5384 (1) | 0.5654 (3) ±0.64pp | +2.70pp | TBD (需 SFT 3-seed) |\\n\\n## 投稿目标\\n- **EMNLP 2026 Main** (ARR July cycle, **~56 天**)\\n\\n## 服务器迁移计划\\n1. 🔄 rsync bjb2 → westd-37389 (~207G, ~30-60min)\\n2. 🔄 ML 依赖安装（并行）\\n3. 📋 rsft_generate 脚本加 resume 机制（M019）\\n4. 📋 迁移完成后 4 GPU 并行恢复实验\\n\\n## 迁移后实验计划（96GB/卡，14B 单卡可跑）\\n| GPU | 实验 | 预计时长 |\\n|-----|------|---------|\\n| cuda:0 | 14B RSFT gen resume (1155 docs remaining) | ~4-5h |\\n| cuda:1 | LLaMA SFT s43 retrain + eval | ~3h |\\n| cuda:2 | LLaMA SFT s44 retrain + eval | ~3h |\\n| cuda:3 | eval_llama_sft_s42_no_evidence_std (~30min) → 其他 | ~30min+ |\\n\\n## 近期任务\\n- [x] D129-D130: LLaMA metrics 审计 + 修正\\n- [x] 新服务器注册 + SSH 配置\\n- [ ] 数据迁移 bjb2 → westd-37389\\n- [ ] ML 依赖安装\\n- [ ] rsft_generate 脚本加 res
…[truncated 1786 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 7471
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T02:40:57.884635+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 7469
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T02:41:03.020408+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'eval_llama_sft_s43_no_evidence_2048_r2'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'eval_llama_sft_s43_no_evidence_2048_r2'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T02:41:03.976648+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'eval_llama_sft_s43_no_evidence_2048'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'eval_llama_sft_s43_no_evidence_2048'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T02:41:04.480432+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9697}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1460
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T02:41:04.480911+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'eval_llama_sft_s42_no_evidence_2048'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'eval_llama_sft_s42_no_evidence_2048'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T02:41:05.425723+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1915}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1449
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T02:41:05.426224+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'eval_llama_sft_s44_no_evidence_2048'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'eval_llama_sft_s44_no_evidence_2048'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T02:41:05.978793+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'eval_llama_sft_s42_with_evidence_2048'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'eval_llama_sft_s42_with_evidence_2048'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T02:41:06.280844+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0285}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1799
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T02:41:07.336643+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9765}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1910
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T02:41:08.343798+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0207}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2365
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T02:41:13.143471+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
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

### Tool call

_source line 25 · 2026-05-21T02:41:13.546532+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
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

### Tool result

_source line 26 · 2026-05-21T02:41:14.151162+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_llama_sft_s43_no_evidence_2048_r2\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:29:26.346Z\", \"updated_at\": \"2026-05-21T02:40:23.445Z\", \"hypothesis\": \"方法论一致性重跑：s43 SFT no-evi 2048 eval。上次在 237/247 batch 超时(4h timeout)。timeout 改为 6h。与 s42/s44 2048 matched comparison，验证截断伪影 vs 真实 evidence dependency。\", \"parent\": \"eval_llama_sft_s43_no_evidence_2048\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T22:29:44.205Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=1 python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 2048 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_no_evidence_2048\\\"\", \"finished_at\": \"2026-05-21T02:40:19.948Z\", \"training_hours\": 4.18}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=1 python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 2048 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_no_evidence_2048\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"58417\", \"log_path\": \"~/runs/faith-evidence-ie/eval_llama_sft_s43_no_evidence_2048_r2.log\", \"submitted_at\": \"2026-05-20T22:29:47.154Z\", \"submitted_via\": \"submit_training_job\", \"b
…[truncated 396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1007
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T02:41:15.158572+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_llama_sft_s43_with_evidence_2048\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:47:46.702Z\", \"updated_at\": \"2026-05-21T00:48:13.215Z\", \"hypothesis\": \"matched@2048 methodology: s43 SFT with-evidence eval at max_new_tokens=2048. 配对 s43 no-evi@2048 计算 matched evidence tax。\", \"parent\": \"llama_sft_s43_train_eval_r3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -m freige.eval.inference --model_path /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --split dev --seed 42\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Meta-Llama-3.1-8B + s43 SFT adapter (with-evidence)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/sft_output_llama_3_1_8b_s43\", \"eval_data\": \"docred dev\", \"pid\": 64391, \"gpu\": \"cuda:2\", \"log_path\": \"/root/autodl-tmp/freige/eval_outputs/eval_llama_sft_s43_with_evidence_2048.log\"}}, \"eval_llama_sft_s44_with_evidence_2048\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:46:47.679Z\", \"updated_at\": \"2026-05-21T00:47:16.734Z\", \"hypothesis\": \"matched@2048 methodology: s44 SFT with-evidence eval at max_new_tokens=2048. 配对 s44 no-evi@2048 (ign_f1=0.4373) 计算 matched evidence tax。s42 control 显示 with-evi@1024→2048 delta=+2.65pp，证明 matched budget 必要。\", \"parent\": \"llama_sft_s44_train_eval_r3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -m freige.eval.inference --model_path /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b_s44 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/eva
…[truncated 1961 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1612
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T02:41:24.036156+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'status': 'DONE'}",
  "fields": "['status', 'conclusion', 'metrics', 'hypothesis', 'parent']",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'status': 'DONE'}",
    "fields": "['status', 'conclusion', 'metrics', 'hypothesis', 'parent']",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T02:41:25.247900+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_llama_sft_s42_with_evidence_2048\": {\"status\": \"DONE\", \"hypothesis\": \"方法论 control: LLaMA SFT s42 with-evidence eval at max_new_tokens=2048. 原 1024 版 ign_f1=0.5384. 预期 delta<1pp, 证明 with-evi 对 token budget 不敏感, 从而验证 no-evi@2048 vs with-evi@1024 的 tax 计算方法论合理。\", \"parent\": \"llama_sft_s42\", \"metrics\": {\"ign_f1\": 0.5649, \"f1\": 0.5767, \"format_ok\": 976, \"format_ok_rate\": 0.9909, \"truncated\": 147, \"predictions\": 20302, \"evi_f1\": 0.803, \"edcr\": 0.6428, \"inference_time_seconds\": 10491.7}, \"conclusion\": \"success\"}, \"plan017_14b_rsft_no_evidence_eval\": {\"status\": \"DONE\", \"hypothesis\": \"14B RSFT no-evidence eval. Measures evidence tax at 14B scale. Based on smaller scales, expect RSFT to compress evidence tax variance. SFT 14B ign_f1=0.5507.\", \"parent\": \"plan017_14b_rsft_train\", \"metrics\": {\"ign_f1\": 0.5432, \"f1\": 0.5536, \"ign_precision\": 0.5193, \"ign_recall\": 0.5693, \"precision\": 0.5414, \"recall\": 0.5664, \"evi_f1\": 0, \"edcr\": 0, \"format_ok\": 953, \"format_ok_rate\": 0.9675, \"n_total\": 985, \"n_predictions\": 15333, \"n_truncated\": 106, \"tp\": 6882, \"pred_count\": 12711, \"gold_count\": 12151, \"inference_time_seconds\": 9427.5}, \"conclusion\": \"success\"}, \"eval_llama_sft_s43_no_evidence_2048\": {\"status\": \"DONE\", \"hypothesis\": \"方法论一致性：s43 SFT no-evi 用 max_new_tokens=2048 重跑。原 1024 版 truncation=38.4%, ign_f1=0.3391。与 s42/s44 2048 版 matched comparison，验证截断伪影 vs 真实退化。seed=42（标准 eval seed）。\", \"parent\": \"eval_llama_sft_s43_no_evidence_r2\", \"conclusion\": \"failed\"}, \"eval_llama_sft_s42_no_evidence_2048\": {\"status\": \"DONE\", \"hypothesis\": \"方法论一致性：s42 SFT no-evi 用 max_new_tokens=2048 重跑，与 s44 2048 版 matched comparison。原 1024 版 s42 format_ok=88.7% (874/985)，fair tax=+1.35pp。2048 版验证截断对 s42 的影响程度，确保 3-seed evidence tax 在相同条件下比较。\", \"parent\": \"eval_llama_sft_s42_no_evidence_std_r2\", \"metrics\": {\"ign_f1\": 0.521, \"
…[truncated 12395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1211
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T02:41:44.549446+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "analysis:eval_llama_sft_s43_no_evidence_2048_r2",
  "project": "faith-evidence-ie",
  "task_prompt": "## 任务\n分析实验 `eval_llama_sft_s43_no_evidence_2048_r2` 的结果，提取所有关键 metrics。\n\n## 服务器信息\n- Server: rtx5090-4x\n- Log path: ~/runs/faith-evidence-ie/eval_llama_sft_s43_no_evidence_2048_r2.log\n- Output dir: /root/autodl-tmp/eval_results/eval_llama_sft_s43_no_evidence_2048\n\n## 需要提取的 metrics\n1. ign_f1, f1, ign_precision, ign_recall\n2. format_ok_rate, n_format_ok, n_documents\n3. n_truncated, truncation_rate\n4. n_predictions\n5. evi_f1 (应该是 0 因为 no_evidence)\n6. inference_time_seconds\n7. 任何其他可用的 eval metrics\n\n## 步骤\n1. SSH 到 rtx5090-4x 读取 log 文件最后 100 行（尾部通常有汇总）\n2. 检查 output_dir 下的 eval_results.json 或类似结果文件\n3. 如果有 fair comparison 子集分析（fair_tax_pp），也提取\n\n## 对比上下文（供参考）\n- s42 no-evi@2048: ign_f1=0.5210, format_ok=0.8873, truncated=201\n- s44 no-evi@2048: ign_f1=0.4373, format_ok=0.9919, truncated=246\n- s42 with-evi@2048: ign_f1=0.5649\n\n## 输出格式\n列出所有提取到的 metrics 值（精确数值），加上你对数据质量的判断。",
  "tool_groups": "['ssh']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analysis:eval_llama_sft_s43_no_evidence_2048_r2",
    "project": "faith-evidence-ie",
    "task_prompt": "## 任务\n分析实验 `eval_llama_sft_s43_no_evidence_2048_r2` 的结果，提取所有关键 metrics。\n\n## 服务器信息\n- Server: rtx5090-4x\n- Log path: ~/runs/faith-evidence-ie/eval_llama_sft_s43_no_evidence_2048_r2.log\n- Output dir: /root/autodl-tmp/eval_results/eval_llama_sft_s43_no_evidence_2048\n\n## 需要提取的 metrics\n1. ign_f1, f1, ign_precision, ign_recall\n2. format_ok_rate, n_format_ok, n_documents\n3. n_truncated, truncation_rate\n4. n_predictions\n5. evi_f1 (应该是 0 因为 no_evidence)\n6. inference_time_seconds\n7. 任何其他可用的 eval metrics\n\n## 步骤\n1. SSH 到 rtx5090-4x 读取 log 文件最后 100 行（尾部通常有汇总）\n2. 检查 output_dir 下的 eval_results.json 或类似结果文件\n3. 如果有 fair comparison 子集分析（fair_tax_pp），也提取\n\n## 对比上下文（供参考）\n- s42 no-evi@2048: ign_f1=0.5210, format_ok=0.8873, truncated=201\n- s44 no-evi@2048: ign_f1=0.4373, format_ok=0.9919, truncated=246\n- s42 with-evi@2048: ign_f1=0.5649\n\n## 输出格式\n列出所有提取到的 metrics 值（精确数值），加上你对数据质量的判断。",
    "tool_groups": "['ssh']"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T02:41:48.293745+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_eval_llama_sft_s43_no_evidence_2048_r2_20260521T024145\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/logs/workers/worker_analysis_eval_llama_sft_s43_no_evidence_2048_r2_20260521T024145.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_eval_llama_sft_s43_no_evidence_2048_r2_20260521T024145 started. Use get_worker_status('worker_analysis_eval_llama_sft_s43_no_evidence_2048_r2_20260521T024145') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 3744
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-21T02:42:06.161225+00:00_

Worker 已派发读取 rtx5090-4x 上的实验结果。等待回调后完成 on-experiment-done 流程（更新 registry → report.md → 汇报 Director）。

当前状态：
- `eval_llama_sft_s43_no_evidence_2048_r2`: ANALYZING → Worker 提取 metrics 中
- cuda:1 已空闲（该实验刚完成释放）
- 3 个实验仍在跑：plan017_14b_rsft_eval (cuda:0), eval_llama_sft_s43_with_evidence_2048 (cuda:2), eval_llama_sft_s44_with_evidence_2048 (cuda:3)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 33 · 2026-05-21T02:42:06.170712+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: eval_llama_sft_s43_no_evidence_2048_r2
- project: faith-evidence-ie
- server: rtx5090-4x
- log_path: ~/runs/faith-evidence-ie/eval_llama_sft_s43_no_evidence_2048_r2.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "source": "cron:hook"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-21T02:42:14.575873+00:00_

已在处理中——上一轮已派 Worker `worker_analysis_eval_llama_sft_s43_no_evidence_2048_r2` 读取日志和提取 metrics，等待回调。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2"
}
```

</details>

---

## Round 3

2 recorded events

### User

_source line 35 · 2026-05-21T18:43:27.990325+00:00_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-21T18:44:17.399944+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx5090-4x 的 cuda:0, cuda:1, cuda:2, cuda:3（共 4 张）。bjb2-12179 不可用
- eval 实验用 `--no-quantize`，batch_size=1（with-evidence）或 batch_size=4（no-evidence）
- evidence tax 计算必须用 matched@2048 methodology（D137 决策）：no-evi@2048 vs with-evi@2048，同 token budget 下对比
- LLaMA SFT s42 的 ground truth ign_f1=0.5384（D130 审计确认，非 0.5514 那个是 rel_f1）
- LLaMA RSFT s42 ign_f1=0.5714（D129 修正，非 0.5839 那个是 rel_f1）
- submit_training_job 命令必须自带 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`

### 2. 🖥️ 基础设施快照
- **服务器**: rtx5090-4x（4× RTX 5090），工作目录 `/root/autodl-tmp/freige`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **模型路径**:
  - 基座: `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B`, `/root/autodl-tmp/models/Qwen/Qwen3-14B`
  - SFT adapters: `/root/autodl-tmp/sft_output_llama_3_1_8b_s42`, `_s43`, `_s44`
  - RSFT adapters: `/root/autodl-tmp/rsft_output_llama_*`
  - 14B SFT: `/root/autodl-tmp/sft_output_14b/checkpoint-144`, RSFT: `/root/autodl-tmp/rsft_output_14b`
- **数据**: `/root/autodl-tmp/data/docred`（dev.json 985 docs, 12275 gold triples）
- **Eval 结果**: `/root/autodl-tmp/eval_results/`
- **活跃进程**:
  - `plan017_14b_rsft_eval` PID 53413, cuda:0（14B RSFT eval）
  - `eval_llama_sft_s44_with_evidence_2048` PID 64023, cuda:3
  - `eval_llama_sft_s43_with_evidence_2048` PID 64391, cuda:2

### 3. 📊 当前状态
**刚收到 `eval_llama_sft_s43_no_evidence_2048_r2` 完成回调，已派 Worker 提取 metrics 但 Worker 尚未返回。** 这是 s43 no-evi@2048 的超时重跑（上次在 237/247 batch 超时，本次 timeout 改为 6h，跑了 4.18h 完成）。

**RUNNING (3)**:
| exp_id | GPU | 说明 |
|--------|-----|------|
| plan017_14b_rsft_eval | cuda:0 | 14B RSFT eval，补齐 scaling table 第 4 行 |
| eval_llama_sft_s43_with_evidence_2048 | cuda:2 | s43 with-evi@2048，配对 s43 no-evi 算 matched tax |
| eval_llama_sft_s44_with_evidence_2048 | cuda:3 | s44 with-evi@2048，配对 s44 no-evi 算 matched tax |

**ANALYZING (1)**:
- `eval_llama_sft_s43_no_evidence_2048_r2` (cuda:1 已释放) — Worker `worker_analysis_eval_llama_sft_s43_no_evidence_2048_r2_20260521T024145` 正在读 log 提取 metrics

**等待中**: 3 个 cron 回调（上述 3 个 RUNNING 实验）+ 1 个 Worker 回调

### 4. 📋 待办（条件触发式）
- Worker 分析回调到达 → 用 metrics 更新 registry（status=DONE, conclusion, metrics）→ cuda:1 空出可接新实验
- `eval_llama_sft_s43_with_evidence_2048` 完成 → 提取 metrics → 计算 s43 matched evidence tax = with-evi@2048 - no-evi@2048
- `eval_llama_sft_s44_with_evidence_2048` 完成 → 同上算 s44 matched tax
- **三组 matched tax 全到齐**（s42/s43/s44）→ 计算 SFT 3-seed matched evidence tax mean±std → 对比 RSFT 3-seed tax (-1.14pp±0) → 更新 D137 → 汇报 Director
- `plan017_14b_rsft_eval` 完成 → 提取 ign_f1 → 对比 14B SFT baseline (0.5507) → 补齐 scaling table 第 4 行 RSFT 列 → 如果 RSFT>SFT，计算 14B evidence tax 并与小尺度对比
- cuda:1 空出 → 检查是否有待跑实验可以立即填上（如 14B no-evidence eval 或其他矩阵格子）

### 5. 🎯 战略上下文
- **核心 story**: FREIGE 三大贡献 — (1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。D131 统一叙事主线
- **当前阶段**: matched@2048 evidence tax 方法论重跑（D137 决策），同时 14B RSFT 最后一行 scaling table
- **已知 LLaMA SFT evidence tax 极其 seed-dependent**（D136）：s42 fair_tax=+1.2pp, s44 fair_tax=-4.18pp。这正是 matched@2048 要解决的——用统一 token budget 消除截断伪影
- **s42 matched@2048 control 已完成**：with-evi@1024 ign_f1=0.5384 → with-evi@2048 ign_f1=0.5649（+2.65pp），证明 with-evi 也受 token budget 影响，matched comparison 是必要的
- **LLaMA RSFT 3-seed evidence tax**: 已完成，-1.14pp±0（极度稳定），是 variance compression story 的关键证据
- **Scaling table**: 1.7B/4B/8B 完成，14B 最后一行 RSFT eval 在跑
- **投稿目标**: EMNLP 2026 Main (ARR July cycle, ~56 天)
- **易错点**: (1) 不要把 rel_f1 和 ign_f1 搞混（D129/D130 教训）(2) evidence tax 必须用 matched@2048 不能用旧的 fair comparison (3) s43 no-evi 之前超时过一次，这次是 r2 重跑成功
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048_r2"
}
```

</details>

---
