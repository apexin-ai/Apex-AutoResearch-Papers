# cron hook plan017 14b rsft generate r3 20260521T072130 627632

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 3
- **Tool calls:** 14
- **Original source:** `logs/chats/archive/cron_hook_plan017_14b_rsft_generate_r3_20260521T072130_627632.jsonl`
- **Structured JSON:** [`345ad50e6366e2546982.json`](../../sessions/34/345ad50e6366e2546982.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-20T15:17:24.046560+00:00_

[CRON] 实验进程异常退出（失败），需要你诊断原因。
详情: Process exited without valid W&B metrics

- exp_id: plan017_14b_rsft_generate_r3
- project: faith-evidence-ie
- server: rtx5090-4x
- log_path: ~/runs/faith-evidence-ie/plan017_14b_rsft_generate_r3.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-20T15:17:45.525039+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_worker_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_worker_status",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-20T15:17:45.575872+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T15:17:50.096818+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "limit": "0",
  "fields": "['*']",
  "filters": "{'exp_id': 'plan017_14b_rsft_generate_r3'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "limit": "0",
    "fields": "['*']",
    "filters": "{'exp_id': 'plan017_14b_rsft_generate_r3'}"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T15:17:50.604058+00:00_

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
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T15:17:51.207573+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1014}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1110
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T15:17:51.258317+00:00_

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
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
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

_source line 8 · 2026-05-20T15:17:51.761974+00:00_

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
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T15:17:51.762412+00:00_

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
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
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

_source line 10 · 2026-05-20T15:18:06.908443+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 4, \"results\": [{\"exp_id\": \"migration_bjb2_to_westd\", \"success\": true, \"actions\": [\"Job still running (pid=6660)\"]}, {\"exp_id\": \"eval_llama_sft_s43_no_evidence\", \"success\": true, \"actions\": [\"Job still running (pid=27322)\"]}, {\"exp_id\": \"eval_llama_sft_s44_no_evidence\", \"success\": true, \"actions\": [\"Job still running (pid=29983)\"]}, {\"exp_id\": \"eval_llama_rsft_s44_no_evidence\", \"success\": true, \"actions\": [\"Job still running (pid=30188)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 16304
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T15:18:06.968785+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-20T15:17:30Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 255 个实验 — DONE 251, RUNNING 4\\n**DONE 分布**: failed 56, killed 32, negative 18, success 145\\n\\n### GPU 占用\\n- **分配**: 4 张 — rtx5090-4x:cuda:0, rtx5090-4x:cuda:1, rtx5090-4x:cuda:2, rtx5090-4x:cuda:3\\n- **实际运行**: 3 张 — rtx5090-4x:cuda:1(eval_llama_sft_s43_no_evidence), rtx5090-4x:cuda:2(eval_llama_sft_s44_no_evidence), rtx5090-4x:cuda:3(eval_llama_rsft_s44_no_evidence)\\n- **空闲（分配了没跑）**: rtx5090-4x:cuda:0\\n\\n### 💾 磁盘余量\\n- **rtx5090-4x**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/usr/bin/nvidia-smi`: 814G/879G 可用（已用 3%）\\n- **bjb2-12179**:\\n  - `/autodl-pub`: 8.8T/14T 可用（已用 38%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `migration_bjb2_to_westd` | rtx5090-4x | ? | ? | `—` |\\n| `eval_llama_sft_s43_no_evidence` | rtx5090-4x | cuda:1 | 27322 | `~/runs/faith-evidence-ie/eval_llama_sft_s43_no_evidence.log` |\\n| `eval_llama_sft_s44_no_evidence` | rtx5090-4x | cuda:2 | 29983 | `—` |\\n| `eval_llama_rsft_s44_no_evidence` | rtx5090-4x | cuda:3 | 30188 | `—` |\\n\\n### 📌 最近完成 (top 5)\\n- `plan017_14b_rsft_generate_r3` [failed] — 2026-05-20T15:17:19 — EXIT_CODE=143 (SIGTERM — graceful kill)\\n- `eval_llama_sft_s42_no_evidence_std_r2` [success] — 2026-05-20T14:39:28\\n- `llama_sft_s44_train_eval_r3` [success] — 2026-05-20T14:38:21\\n- `d112_rsft_s44_ced_score` [success] — 2026-05-20T14:36:56 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `d112_rsft_s44_generate` [success] — 2026-05-20T14:36:52\\n\\n### 🔴 最近失败原因 (top 3)\\n- `plan017_14b_rsft_generate_r3`: EXIT_CODE=143 (SIGTERM — gracef
…[truncated 6528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 15710
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T15:18:07.028778+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-20 07:31 UTC | 更新原因: 服务器迁移: westd-37389 (4×RTX PRO 6000 96GB), 数据完好从 bjb2 迁移中\\n\\n## 核心方向\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\n- **服务器迁移中**: bjb2-12179 → westd-37389 (4× RTX PRO 6000, 96GB VRAM/卡, 350GB disk)\\n- **数据状况**: bjb2 上全部完好（adapters + 14B gen 62% + eval results），迁移中\\n- **D130**: LLaMA 全系列 ign_f1 审计完成，论文数据正确\\n\\n| Scale | SFT ign_f1 (seeds) | RSFT ign_f1 (seeds) | Δ | Variance compression |\\n|-------|---------------------|----------------------|---|---------------------|\\n| 1.7B | 0.4464 (3) | 0.5119 (3) | +6.55pp | **31×** (2.79→0.09pp) |\\n| 4B | 0.4358 (3) | 0.4482 (3, A) / 0.5152 (1, B) | +1.24/+4.18pp | **7.5×** (3.80→0.51pp) |\\n| 8B | 0.5019 (3) | 0.5433 (3) | +4.14pp | **7.4×** (3.72→0.50pp) |\\n| 14B | 0.5507 (1) | 🔄 gen 62% done, resume pending | — | — |\\n| LLaMA-8B | 0.5384 (1) | 0.5654 (3) ±0.64pp | +2.70pp | TBD (需 SFT 3-seed) |\\n\\n## 投稿目标\\n- **EMNLP 2026 Main** (ARR July cycle, **~56 天**)\\n\\n## 服务器迁移计划\\n1. 🔄 rsync bjb2 → westd-37389 (~207G, ~30-60min)\\n2. 🔄 ML 依赖安装（并行）\\n3. 📋 rsft_generate 脚本加 resume 机制（M019）\\n4. 📋 迁移完成后 4 GPU 并行恢复实验\\n\\n## 迁移后实验计划（96GB/卡，14B 单卡可跑）\\n| GPU | 实验 | 预计时长 |\\n|-----|------|---------|\\n| cuda:0 | 14B RSFT gen resume (1155 docs remaining) | ~4-5h |\\n| cuda:1 | LLaMA SFT s43 retrain + eval | ~3h |\\n| cuda:2 | LLaMA SFT s44 retrain + eval | ~3h |\\n| cuda:3 | eval_llama_sft_s42_no_evidence_std (~30min) → 其他 | ~30min+ |\\n\\n## 近期任务\\n- [x] D129-D130: LLaMA metrics 审计 + 修正\\n- [x] 新服务器注册 + SSH 配置\\n- [ ] 数据迁移 bjb2 → westd-37389\\n- [ ] ML 依赖安装\\n- [ ] rsft_generate 脚本加 res
…[truncated 1687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 15266
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T15:18:07.369526+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_analysis_s42-no-evi-format-issue_20260520T151608\", \"task_type\": \"analysis:s42-no-evi-format-issue\", \"project\": \"faith-evidence-ie\", \"status\": \"running\", \"started_at\": \"2026-05-20T15:16:08.866295+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 15607
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T15:18:17.397187+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "limit": "5",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "limit": "5",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T15:18:18.204306+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/on-experiment-failed.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/on-experiment-failed.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T15:18:18.456582+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan017_14b_rsft_generate_r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:35:00.799Z\", \"updated_at\": \"2026-05-20T15:17:19.864Z\", \"hypothesis\": \"14B RSFT 生成 resume (r3: 修正 adapter 路径指向 checkpoint-144)。从 doc 1873 继续生成剩余 1155 docs。r2 因 --sft_adapter 指向顶层目录而非 checkpoint-144 子目录失败。\", \"parent\": \"plan017_14b_rsft_generate_r2\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-20T11:35:20.944Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/rsft_generations_14b --num_generations 8 --resume\\\"\", \"finished_at\": \"2026-05-20T15:17:06.480Z\", \"training_hours\": 3.7}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/rsft_generations_14b --num_generations 8 --resume\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:0\"], \"pid\": \"17644\", \"log_path\": \"~/runs/faith-evidence-ie/plan017_14b_rsft_generate_r3.log\", \"submitted_at\": \"2026-05-20T11:35:24.818Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13307.5, \"gpu_hours\": 3.7}, \"pid\": \"17644\", \"log_path\": \"~/runs/faith-evidence-ie/plan017_14b_rsft_generate_r3.log\"
…[truncated 8315 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1059
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T15:18:18.457127+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/agent_80a9cb72.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T15:18:28.365523+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/on-experiment-failed.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/on-experiment-failed.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T15:18:28.416482+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T15:18:31.487431+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/on-experiment-failed*",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/on-experiment-failed*",
    "path": "/home/ubuntu"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T15:18:31.839309+00:00_

/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "Glob",
  "elapsed_ms": 351
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T15:18:34.866247+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T15:18:34.918798+00:00_

1	---
2	name: on-experiment-failed
3	description: 实验失败后的自动诊断工作流——查日志分析原因、更新 registry、通知 Director。[CRON] 实验失败消息到达时使用。
4	scope: global
5	tags:
6	- workflow
7	- diagnosis
8	- cron-hook
9	tools:
10	- read_registry
11	- tail_training_logs
12	- update_registry
13	- append_idea
14	- feishu_send_result_card
15	- spawn_worker
16	- check_job_status
17	version: 4
18	heavy: true
19	roles:
20	- agent
21	---
22	
23	# 实验失败诊断工作流
24	
25	## 触发方式
26	由 cron hook 自动触发：进程退出且 W&B 无数据 / W&B state=failed/crashed / NaN 检测到。
27	
28	## 步骤
29	
30	### Step 0: 读取项目上下文（诊断前必须执行）
31	先读文档，再看日志——否则诊断方向可能完全错误：
32	
33	- `read_project_file("memory.md")` — **最重要**：查是否有相同失败模式的历史记录和已知修复方案
34	- Worker 通过 `list_repo_tree` + `read_repo_file` 按需从代码仓库读取训练脚本结构
35	
36	读完后检查：
37	- memory.md 里有没有"此类实验曾失败，原因是 X"的记录？→ 直接按已知方案诊断，跳过 Step 2 通用流程
38	- 代码仓库中的训练入口和参数格式是否与本次实验配置匹配？（Worker 可用 `list_repo_tree` + `read_repo_file` 查看）
39	
40	### Step 1: 了解失败背景
41	- read_registry(exp_id) — 查看状态、conclusion、notes、metrics、log_path
42	
43	### Step 2: 浅层日志诊断
44	有 log_path 时：tail_training_logs(server, **绝对路径**, lines=80)
45	- 寻找：OOM、CUDA error、NaN、assertion error、数据加载错误、Python Traceback
46	- 没找到 → 增加行数再查
47	
48	### Step 2.5: 深查（满足以下任一条件时 spawn_worker）
49	- 运行时长 < 5 分钟（初始化阶段崩溃）
50	- tail 日志中未见明确 Traceback 或错误行
51	- 同类实验连续失败 ≥ 2 次
52	
53	```python
54	spawn_worker(
55	    task_type="diagnose:{exp_id}",
56	    task_prompt="""SSH 到服务器 {server}，诊断实验 {exp_id} 的失败原因。
57	
58	项目路径：{project_path}（绝对路径）
59	日志路径：{log_path}（可能为空）
60	
61	执行步骤（按顺序，有结论就停）：
62	
63	1. 如果有日志路径：
64	   - 先看结尾 50 行（找 Traceback / Error / CUDA OOM）
65	   - 没找到明确错误：再看开头 100 行（初始化崩溃在这里）
66	   - 日志文件不存在：说明任务启动即失败，跳到步骤 2
67	
68	2. 日志无错误或无日志时，检查基础设施：
69	   - 入口文件是否存在
70	   - 激活环境并验证 import
71	   - 检查 configs/ 目录
72	
73	3. 检查磁盘/内存（OOM 类）
74	
75	最后输出一行 JSON：
76	{"root_cause":"<引用具体报错行>","error_type":"infrastructure|hyperparameter|resource|data","fix_steps":["步骤1","步骤2"],"can_auto_fix":true}""",
77	    tool_groups=["ssh"],
78	)
79	```
80	
81	Worker 返回后，以其结论作为 Step 3 的诊断依据。
82	
83	### 
…[truncated 1766 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T15:18:46.477641+00:00_

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
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
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

_source line 25 · 2026-05-20T15:18:46.629064+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# faith-evidence-ie Memory\\n\\n## 服务器架构（2026-05-20 更新）\\n\\n- **主服务器 westd-37389**: 4× RTX PRO 6000 Blackwell, 98GB VRAM/卡, 350GB 数据盘 (46% used, 190GB free)\\n  - SSH: `rtx5090-4x` (connect.westd.seetacloud.com:37389)\\n  - 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128, transformers 5.8.1, flash-attn 2.8.3\\n- **数据源 bjb2-12179**: 全部 208G 数据完好，rsync 迁移仍在后台运行\\n  - SSH: `bjb2-12179` (connect.bjb2.seetacloud.com:12179)\\n- **废弃 bjb1-49673**: AutoDL 重启导致数据清空，已关停\\n\\n## GPU 分配教训（2026-05-20）\\n\\nLLaMA SFT 脚本里有 `export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`，会覆盖 submit_training_job 注入的 CUDA_VISIBLE_DEVICES。**必须通过 `GPU=X` 环境变量传物理 GPU 编号**，不能依赖框架注入。\\n\\n## LLaMA 完整统计（2026-05-20 更新）\\n\\n### SFT 3-seed\\n| Seed | ign_f1 | rel_f1 | edcr |\\n|------|--------|--------|------|\\n| s42 | 0.5384 | 0.5514 | — |\\n| s43 | 0.5142 | 0.5308 | 0.5866 |\\n| s44 | 0.4802 | 0.4902 | 0.6579 |\\n| **Mean** | **0.5109** | — | — |\\n| **Std** | **0.0238** | — | — |\\n\\ns44 异常低（较 s42 低 5.8pp），拉大了 SFT 方差。这恰好强化了 RSFT variance compression 的价值。\\n\\n### RSFT 3-seed (k=1)\\n| Seed | ign_f1 | rel_f1 | edcr |\\n|------|--------|--------|------|\\n| s42 | 0.5714 | 0.5839 | 0.5799 |\\n| s43 | 0.5662 | 0.5780 | 0.5783 |\\n| s44 | 0.5587 | 0.5706 | 0.5829 |\\n| **Mean** | **0.5654** | — | — |\\n| **Std** | **0.0052** | — | — |\\n\\n### 跨方法对比\\n- **SFT→RSFT Δ**: +5.45pp\\n- **方差压缩**: 4.58× (0.0238→0.0052)\\n- RSFT 在最弱 SFT seed (s44) 上仍显著提升：0.4802→0.5587 (+7.85pp)\\n\\n### Evidence Tax (LLaMA)\\n\\n**RSFT (已完成 2/3 seed)**:\\n- s42: no-evi 0.5526, with-evi 0.5714, tax=-1.88pp (evidence helps)\\n- s43: no-evi 0.5546, with-evi 0.5662, tax=-1.16pp (evidence helps)\\n- s44: 🔄 running\\n- mean (2-seed): -1.52pp\\n\\n**SFT (已完成 1/3 seed)**:\\n- s42: no-evi 0.5219, with-evi 0.5384, tax=-1.65pp (evidence helps!)\\n- s43/s44: 🔄 running\\n\
…[truncated 500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T15:18:54.885504+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__feishu_send_result_card",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__feishu_send_result_card",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T15:18:54.936647+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T15:19:13.161037+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "diagnose:plan017_14b_rsft_generate_r3",
  "project": "faith-evidence-ie",
  "task_prompt": "SSH 到服务器 rtx5090-4x，诊断实验 plan017_14b_rsft_generate_r3 的失败原因。\n\n**背景**：\n- 14B RSFT 生成任务（从 doc 1873 resume 生成剩余 1155 docs）\n- 服务器: rtx5090-4x, GPU: cuda:0\n- 运行了 ~3.7 小时后被 SIGTERM (exit code 143) 杀死\n- 这是第 3 次重试（r1 adapter 路径错, r2 adapter 路径指向顶层目录而非 checkpoint-144）\n- 命令: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/rsft_generations_14b --num_generations 8 --resume`\n- 日志路径: ~/runs/faith-evidence-ie/plan017_14b_rsft_generate_r3.log\n\n**诊断步骤（按顺序，有结论就停）**：\n\n1. 看日志结尾 100 行，找 Traceback / Error / OOM / CUDA error / 最后处理到哪个 doc\n2. 看日志开头 50 行，确认启动正常、resume 从正确位置开始\n3. 检查系统层面：\n   - `dmesg | tail -50` 看有无 OOM killer\n   - `journalctl --since \"4 hours ago\" | grep -i \"kill\\|oom\\|sigterm\" | tail -20`\n   - 检查 tmux session 是否还在：`tmux ls`\n   - 检查磁盘空间：`df -h /root/autodl-tmp`\n4. 检查输出目录状态：\n   - `ls -la /root/autodl-tmp/rsft_generations_14b/` 看已生成了多少文件\n   - 确认 resume 是否有进展（对比 r2 结束时的文件数）\n5. 检查是否有其他进程抢了 GPU 0：`nvidia-smi`\n\n**输出格式**（最终结论用这个 JSON）：\n```json\n{\"root_cause\":\"<引用具体证据>\",\"error_type\":\"infrastructure|hyperparameter|resource|data\",\"fix_steps\":[\"步骤1\",\"步骤2\"],\"can_auto_fix\":true/false,\"progress\":\"已生成到 doc X / 总 3028\"}\n```",
  "tool_groups": "['ssh']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "diagnose:plan017_14b_rsft_generate_r3",
    "project": "faith-evidence-ie",
    "task_prompt": "SSH 到服务器 rtx5090-4x，诊断实验 plan017_14b_rsft_generate_r3 的失败原因。\n\n**背景**：\n- 14B RSFT 生成任务（从 doc 1873 resume 生成剩余 1155 docs）\n- 服务器: rtx5090-4x, GPU: cuda:0\n- 运行了 ~3.7 小时后被 SIGTERM (exit code 143) 杀死\n- 这是第 3 次重试（r1 adapter 路径错, r2 adapter 路径指向顶层目录而非 checkpoint-144）\n- 命令: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 python -m freige.training.rsft_generate --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --output_dir /root/autodl-tmp/rsft_generations_14b --num_generations 8 --resume`\n- 日志路径: ~/runs/faith-evidence-ie/plan017_14b_rsft_generate_r3.log\n\n**诊断步骤（按顺序，有结论就停）**：\n\n1. 看日志结尾 100 行，找 Traceback / Error / OOM / CUDA error / 最后处理到哪个 doc\n2. 看日志开头 50 行，确认启动正常、resume 从正确位置开始\n3. 检查系统层面：\n   - `dmesg | tail -50` 看有无 OOM killer\n   - `journalctl --since \"4 hours ago\" | grep -i \"kill\\|oom\\|sigterm\" | tail -20`\n   - 检查 tmux session 是否还在：`tmux ls`\n   - 检查磁盘空间：`df -h /root/autodl-tmp`\n4. 检查输出目录状态：\n   - `ls -la /root/autodl-tmp/rsft_generations_14b/` 看已生成了多少文件\n   - 确认 resume 是否有进展（对比 r2 结束时的文件数）\n5. 检查是否有其他进程抢了 GPU 0：`nvidia-smi`\n\n**输出格式**（最终结论用这个 JSON）：\n```json\n{\"root_cause\":\"<引用具体证据>\",\"error_type\":\"infrastructure|hyperparameter|resource|data\",\"fix_steps\":[\"步骤1\",\"步骤2\"],\"can_auto_fix\":true/false,\"progress\":\"已生成到 doc X / 总 3028\"}\n```",
    "tool_groups": "['ssh']"
  }
}
````

</details>

---

### Tool result

_source line 29 · 2026-05-20T15:19:16.666542+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_diagnose_plan017_14b_rsft_generate_r3_20260520T151914\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/logs/workers/worker_diagnose_plan017_14b_rsft_generate_r3_20260520T151914.log\", \"setup_data\": {}, \"message\": \"Worker worker_diagnose_plan017_14b_rsft_generate_r3_20260520T151914 started. Use get_worker_status('worker_diagnose_plan017_14b_rsft_generate_r3_20260520T151914') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 3505
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-20T15:19:22.630175+00:00_

诊断 Worker 已派出 (`worker_diagnose_plan017_14b_rsft_generate_r3_20260520T151914`)，等待回调。

当前状态：
- cuda:0 空闲（plan017_14b_rsft_generate_r3 失败）
- cuda:1/2/3 在跑 LLaMA no-evidence eval（3 个）
- 1 个 Worker 在分析 s42-no-evi 格式问题
- 1 个 Worker 在诊断本次失败

Worker 返回后我会更新 registry 并汇报 Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:plan017_14b_rsft_generate_r3"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 31 · 2026-05-20T15:19:22.649478+00:00_

[CRON] 实验进程异常退出（失败），需要你诊断原因。
详情: Process exited without valid W&B metrics

- exp_id: plan017_14b_rsft_generate_r3
- project: faith-evidence-ie
- server: rtx5090-4x
- log_path: ~/runs/faith-evidence-ie/plan017_14b_rsft_generate_r3.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "source": "cron:hook"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-20T15:19:35.155350+00:00_

已收到重复的 CRON 回调。诊断 Worker `worker_diagnose_plan017_14b_rsft_generate_r3_20260520T151914` 已在运行中，等待其返回结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:plan017_14b_rsft_generate_r3"
}
```

</details>

---

## Round 3

2 recorded events

### User

_source line 33 · 2026-05-21T07:20:36.347179+00:00_

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
  "session": "cron:hook:plan017_14b_rsft_generate_r3",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-21T07:21:30.434412+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单: rtx5090-4x 的 cuda:0, cuda:1, cuda:2, cuda:3（4 张全分配给本项目）
- LLaMA SFT 脚本用 `GPU=X` 环境变量传物理 GPU 编号，不能依赖框架注入的 CUDA_VISIBLE_DEVICES（脚本内部会覆盖）
- 14B 模型路径: `/root/autodl-tmp/models/Qwen/Qwen3-14B`，SFT adapter: `/root/autodl-tmp/sft_output_14b/checkpoint-144`（必须指向 checkpoint-144 子目录，不是顶层）
- bjb2-12179 数据盘只读迁移源，不要在上面跑新实验
- evidence tax 测量必须用同一模型 + `--no_evidence` flag，不能对比独立训练的 no-evidence 模型（Reviewer 指出的方法论问题）

### 2. 🖥️ 基础设施快照
- **主服务器 rtx5090-4x** (connect.westd.seetacloud.com:37389): 4× RTX PRO 6000 Blackwell, 98GB VRAM/卡, ~190GB 可用磁盘
  - 工作目录: `/root/autodl-tmp/freige`
  - Python: `/root/miniconda3/bin/python` (conda base, Python 3.12, PyTorch 2.8.0+cu128, transformers 5.8.1, flash-attn 2.8.3)
  - 模型: `/root/autodl-tmp/models/` (Qwen3-14B, Qwen3-4B, Meta-Llama-3.1-8B)
  - 数据: `/root/autodl-tmp/data/docred`
  - HF cache: `/root/autodl-tmp/.hf_cache`
- **数据源 bjb2-12179**: 208G 完好，迁移 rsync 仍在后台 (migration_bjb2_to_westd, PID 6660)
- 活跃 cron: migration_bjb2_to_westd, eval_llama_sft_s43_no_evidence (PID 27322, cuda:1), eval_llama_sft_s44_no_evidence (PID 29983, cuda:2), eval_llama_rsft_s44_no_evidence (PID 30188, cuda:3)

### 3. 📊 当前状态
- **刚发生**: `plan017_14b_rsft_generate_r3` 在 cuda:0 上跑了 3.7h 后被 SIGTERM (143) 杀死。已派诊断 Worker (`worker_diagnose_plan017_14b_rsft_generate_r3_20260520T151914`) 去查日志和系统状态，**Worker 尚未返回**。
- **RUNNING 实验** (3 个 eval + 1 个 migration):
  - `eval_llama_sft_s43_no_evidence` (cuda:1) — LLaMA SFT s43 no-evidence eval，补齐 evidence tax 3-seed
  - `eval_llama_sft_s44_no_evidence` (cuda:2) — LLaMA SFT s44 no-evidence eval
  - `eval_llama_rsft_s44_no_evidence` (cuda:3) — LLaMA RSFT s44 no-evidence eval，最后 1 个 RSFT evidence tax seed
  - `migration_bjb2_to_westd` — 数据迁移，后台 rsync
- **另有 1 个运行中 Worker**: `worker_analysis_s42-no-evi-format-issue` (从上个 session 遗留，可能已完成但状态未更新)
- **cuda:0 当前空闲**，等诊断 Worker 返回后决定是否重试 14B gen r4
- 尚未向 Director 汇报本次失败（等诊断结论）

### 4. 📋 待办（条件触发式）
- 诊断 Worker 返回 → 根据 root_cause 决定：infrastructure/resource 类可自动修复重试 r4；否则汇报 Director 决策。更新 registry notes，发飞书结果卡片
- eval_llama_sft_s43_no_evidence 完成 → 记录 ign_f1，计算 SFT s43 evidence tax (对比 with-evi 0.5142)，更新 memory.md
- eval_llama_sft_s44_no_evidence 完成 → 记录 ign_f1，计算 SFT s44 evidence tax (对比 with-evi 0.4802)
- eval_llama_rsft_s44_no_evidence 完成 → 记录 ign_f1，计算 RSFT s44 evidence tax (对比 with-evi 0.5587)。**3 个 RSFT seed 全部完成后**计算 RSFT evidence tax mean±std
- **3 个 eval 全部完成** → 汇总 LLaMA 全系列 evidence tax 表格（SFT 3-seed + RSFT 3-seed），汇报 Director，更新论文数据
- 14B gen 恢复后 → CED scoring → RSFT train → eval，填 ROADMAP 中 14B 行
- migration 完成 → 确认数据完整性，关闭 bjb2 实例

### 5. 🎯 战略上下文
- **投稿目标**: EMNLP 2026 Main (ARR July, ~56 天)
- **核心 story**: FREIGE — 3 contributions: (1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression
- **D133**: LLaMA 升级为 co-primary evidence（不再只是 cross-family 验证点）
- **D131**: 3 contributions 从独立小文章统一为一条叙事主线
- **关键数据缺口**: 14B RSFT (gen 62% done, 被 SIGTERM 中断) 和 LLaMA evidence tax (3 个 eval 正在跑)
- **易踩坑**:
  - SIGTERM 可能是 OOM killer、tmux 被杀、或磁盘满导致——等诊断 Worker 结论再行动，不要盲目重试
  - 14B gen 是 CPU+GPU 混合负载（生成 + 写文件），磁盘满会导致静默失败
  - `worker_analysis_s42-no-evi-format-issue` 可能是僵尸 Worker，新 session 检查其状态
  - LLaMA evidence tax 数据：s42 SFT no-evi ign_f1=0.5219（已完成），RSFT s42=0.5526, s43=0.5546（已完成），注意这些是 ign_f1 不是 rel_f1
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:plan017_14b_rsft_generate_r3"
}
```

</details>

---
