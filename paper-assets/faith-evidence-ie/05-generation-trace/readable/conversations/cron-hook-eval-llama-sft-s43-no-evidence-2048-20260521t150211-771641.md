# cron hook eval llama sft s43 no evidence 2048 20260521T150211 771641

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 66
- **Recorded user turns:** 2
- **Tool calls:** 31
- **Original source:** `logs/chats/archive/cron_hook_eval_llama_sft_s43_no_evidence_2048_20260521T150211_771641.jsonl`
- **Structured JSON:** [`cd19d65bf96d64c0708d.json`](../../sessions/cd/cd19d65bf96d64c0708d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

64 recorded events

### User

_source line 1 · 2026-05-20T22:26:56.967779+00:00_

[CRON] 实验进程异常退出（失败），需要你诊断原因。
详情: Process exited without valid W&B metrics

- exp_id: eval_llama_sft_s43_no_evidence_2048
- project: faith-evidence-ie
- server: rtx5090-4x
- log_path: ~/runs/faith-evidence-ie/eval_llama_sft_s43_no_evidence_2048.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-20T22:27:08.720586+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-20T22:27:08.721201+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T22:27:11.737573+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T22:27:11.738020+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T22:27:12.240223+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
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

_source line 7 · 2026-05-20T22:27:12.441587+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T22:27:13.098410+00:00_

Error: result (170,660 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie--claude-sessions-agent-364ab4f0/3b0992b5-7dfe-4635-a7dd-de6d749111dd/tool-results/mcp-agent-ml-research-read_registry-1779316033060.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie--claude-sessions-agent-364ab4f0/3b0992b5-7dfe-4635-a7dd-de6d749111dd/tool-results/mcp-agent-ml-research-read_registry-1779316033060.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1360
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T22:27:13.200543+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 1462
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T22:27:13.201479+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-20T22:26:54Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 265 个实验 — DONE 262, RUNNING 3\\n**DONE 分布**: failed 57, killed 33, negative 18, success 154\\n\\n### GPU 占用\\n- **分配**: 4 张 — rtx5090-4x:cuda:0, rtx5090-4x:cuda:1, rtx5090-4x:cuda:2, rtx5090-4x:cuda:3\\n- **实际运行**: 3 张 — rtx5090-4x:cuda:0(plan017_14b_rsft_eval), rtx5090-4x:cuda:2(plan017_14b_rsft_no_evidence_eval), rtx5090-4x:cuda:3(eval_llama_sft_s42_with_evidence_2048)\\n- **空闲（分配了没跑）**: rtx5090-4x:cuda:1\\n\\n### 💾 磁盘余量\\n- **rtx5090-4x**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/usr/bin/nvidia-smi`: 815G/879G 可用（已用 3%）\\n- **bjb2-12179**:\\n  - `/autodl-pub`: 8.6T/14T 可用（已用 39%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `plan017_14b_rsft_eval` | rtx5090-4x | cuda:0 | 53413 | `—` |\\n| `plan017_14b_rsft_no_evidence_eval` | rtx5090-4x | cuda:2 | 55039 | `—` |\\n| `eval_llama_sft_s42_with_evidence_2048` | rtx5090-4x | cuda:3 | 55468 | `…faith-evidence-ie/eval_llama_sft_s42_with_evidence_2048.log` |\\n\\n### 📌 最近完成 (top 5)\\n- `eval_llama_sft_s43_no_evidence_2048` [failed] — 2026-05-20T22:26:50 — EXIT_CODE=124 (timeout — exceeded timeout_hours)\\n- `eval_llama_sft_s42_no_evidence_2048` [success] — 2026-05-20T21:16:45\\n- `plan017_14b_rsft_generate_r4` [success] — 2026-05-20T21:13:54\\n- `eval_llama_sft_s43_no_evidence_r2` [success] — 2026-05-20T21:13:36\\n- `eval_llama_sft_s44_no_evidence_2048` [success] — 2026-05-20T21:13:33\\n\\n### 🔴 最近失败原因 (top 3)\\n- `eval_llama_sft_s43_no_evidence_2048`: EXIT_CODE=124 (timeout — exceeded timeout_hours)\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026
…[truncated 6610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 961
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T22:27:13.202082+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-20 07:31 UTC | 更新原因: 服务器迁移: westd-37389 (4×RTX PRO 6000 96GB), 数据完好从 bjb2 迁移中\\n\\n## 核心方向\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\n- **服务器迁移中**: bjb2-12179 → westd-37389 (4× RTX PRO 6000, 96GB VRAM/卡, 350GB disk)\\n- **数据状况**: bjb2 上全部完好（adapters + 14B gen 62% + eval results），迁移中\\n- **D130**: LLaMA 全系列 ign_f1 审计完成，论文数据正确\\n\\n| Scale | SFT ign_f1 (seeds) | RSFT ign_f1 (seeds) | Δ | Variance compression |\\n|-------|---------------------|----------------------|---|---------------------|\\n| 1.7B | 0.4464 (3) | 0.5119 (3) | +6.55pp | **31×** (2.79→0.09pp) |\\n| 4B | 0.4358 (3) | 0.4482 (3, A) / 0.5152 (1, B) | +1.24/+4.18pp | **7.5×** (3.80→0.51pp) |\\n| 8B | 0.5019 (3) | 0.5433 (3) | +4.14pp | **7.4×** (3.72→0.50pp) |\\n| 14B | 0.5507 (1) | 🔄 gen 62% done, resume pending | — | — |\\n| LLaMA-8B | 0.5384 (1) | 0.5654 (3) ±0.64pp | +2.70pp | TBD (需 SFT 3-seed) |\\n\\n## 投稿目标\\n- **EMNLP 2026 Main** (ARR July cycle, **~56 天**)\\n\\n## 服务器迁移计划\\n1. 🔄 rsync bjb2 → westd-37389 (~207G, ~30-60min)\\n2. 🔄 ML 依赖安装（并行）\\n3. 📋 rsft_generate 脚本加 resume 机制（M019）\\n4. 📋 迁移完成后 4 GPU 并行恢复实验\\n\\n## 迁移后实验计划（96GB/卡，14B 单卡可跑）\\n| GPU | 实验 | 预计时长 |\\n|-----|------|---------|\\n| cuda:0 | 14B RSFT gen resume (1155 docs remaining) | ~4-5h |\\n| cuda:1 | LLaMA SFT s43 retrain + eval | ~3h |\\n| cuda:2 | LLaMA SFT s44 retrain + eval | ~3h |\\n| cuda:3 | eval_llama_sft_s42_no_evidence_std (~30min) → 其他 | ~30min+ |\\n\\n## 近期任务\\n- [x] D129-D130: LLaMA metrics 审计 + 修正\\n- [x] 新服务器注册 + SSH 配置\\n- [ ] 数据迁移 bjb2 → westd-37389\\n- [ ] ML 依赖安装\\n- [ ] rsft_generate 脚本加 res
…[truncated 1793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 760
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T22:27:23.052375+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
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

_source line 13 · 2026-05-20T22:27:23.959469+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8434}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 907
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T22:27:24.010255+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/on-experiment-failed.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T22:27:24.161797+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/agent_364ab4f0.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T22:27:24.212622+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T22:27:24.263965+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/agent_364ab4f0.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T22:27:28.723747+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'status': 'DONE', 'conclusion': 'failed'}",
  "fields": "['*']",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'status': 'DONE', 'conclusion': 'failed'}",
    "fields": "['*']",
    "limit": "5"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T22:27:29.277060+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
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

_source line 20 · 2026-05-20T22:27:29.681036+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_llama_sft_s43_no_evidence_2048\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:26:07.605Z\", \"updated_at\": \"2026-05-20T22:26:50.504Z\", \"hypothesis\": \"方法论一致性：s43 SFT no-evi 用 max_new_tokens=2048 重跑。原 1024 版 truncation=38.4%, ign_f1=0.3391。与 s42/s44 2048 版 matched comparison，验证截断伪影 vs 真实退化。seed=42（标准 eval seed）。\", \"parent\": \"eval_llama_sft_s43_no_evidence_r2\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T18:26:28.196Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=1 python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 2048 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_no_evidence_2048\\\"\", \"finished_at\": \"2026-05-20T22:26:45.629Z\", \"training_hours\": 4.0}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=1 python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 2048 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_no_evidence_2048\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"45587\", \"log_path\": \"~/runs/faith-evidence-ie/eval_llama_sft_s43_no_evidence_2048.log\", \"submitted_at\": \"2026-05-20T18:26:31.570Z\", \"submitted_via\": \"submit_training_job\", \"ba
…[truncated 8890 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 957
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T22:27:29.681583+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "Glob",
  "elapsed_ms": 404
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T22:27:29.782383+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T22:27:29.833078+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T22:27:33.663165+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
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

_source line 25 · 2026-05-20T22:27:34.017434+00:00_

/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "Glob",
  "elapsed_ms": 354
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T22:27:34.268956+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation*",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation*",
    "path": "/home/ubuntu"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T22:27:34.571432+00:00_

/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "Glob",
  "elapsed_ms": 302
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T22:27:37.233285+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/on-experiment-failed.skill.md"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T22:27:37.233835+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T22:27:37.284554+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T22:27:37.285144+00:00_

1	---
2	name: resource-saturation
3	description: "当你准备向 Director 汇报前、收到 cron/worker 回调、审批通过准备开跑、怀疑 Worker 池不够饱和时,立即使用本 skill。四部分:A) GPU 分配率(分配了没跑=失职) B) GPU 效率 C) 非 GPU 任务并行(Worker 池<2=失职) D) 汇报必须带 [资源] 行。"
4	always: false
5	roles:
6	  - director
7	  - agent
8	---
9	
10	# 资源饱和度自检（硬约束）
11	
12	## A. GPU 分配率检查
13	
14	调 `get_project_resource_usage(project)` 看:
15	- 已分配给本项目的 GPU 总数和具体卡号
16	- 实际在跑任务的 GPU 数和具体卡号（交叉 registry RUNNING + nvidia-smi 进程）
17	- 分配了但没跑的 GPU 清单 ⚠️
18	
19	任何"分配了但没跑"的 GPU = 失职。必须立即:
20	- 派 Worker 铺 dry-run / 下一批实验代码准备
21	- 铺 ablation（从 experiment-matrix 空白格子里挑）
22	- 确实无实验可铺 → 向 Director 汇报"暂无可铺实验"+ 建议下一步方向(扩 ablation 维度 / 加 baseline / 加 benchmark)。**不要建议归还 GPU**——项目级 GPU 归还只在归档时由 `archive_project` 自动触发, 不是 Director 中途的动作
23	
24	**单实验不占多卡**: 分配 4 卡但实验只用 1 卡 → 另 3 卡必须并行跑其他实验,不能空占。
25	
26	## B. GPU 效率检查
27	
28	调 `get_gpu_health(server)`:
29	- 空闲 GPU（util < 10% 持续 > 5 min）→ 立即铺任务
30	- 低利用率（util < 50% 持续 > 15 min）→ spawn_worker 诊断（batch / IO / 同步）
31	- OOM 风险（显存 > 90% 持续 10 min）→ 主动降 batch / 调优
32	
33	## C. 非 GPU 任务并行
34	
35	GPU 在跑 ≠ 你空闲。以下 CPU / 网络任务**必须**派独立 Worker 并行:
36	- 下一批实验的数据集下载 / 预处理 / fingerprint
37	- 下一批实验的代码准备 / dry-run / 环境配置
38	- 论文文献调研 / related work 检索
39	- 已完成实验的 log 深度分析 / metric 聚合
40	- 论文章节起草
41	- 代码 review / refactor
42	
43	**硬约束**: 任一时刻 Worker 池 < 2 个 = 失职（除非真的全部下游阻塞在等 GPU,这时应当向 Director 申请扩 GPU）。
44	
45	## D. 汇报格式
46	
47	向 Director 汇报时开头必须带资源声明行:
48	
49	    [资源] GPU 分配 N / 实际在跑 M | Worker 池 K (其中 GPU 任务 A / CPU 任务 B)
50	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T22:28:02.400044+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "memory.md"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T22:28:03.709469+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# faith-evidence-ie Memory\\n\\n## 服务器架构（2026-05-20 更新）\\n\\n- **主服务器 westd-37389**: 4× RTX PRO 6000 Blackwell, 98GB VRAM/卡, 350GB 数据盘 (46% used, 190GB free)\\n  - SSH: `rtx5090-4x` (connect.westd.seetacloud.com:37389)\\n  - 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128, transformers 5.8.1, flash-attn 2.8.3\\n- **数据源 bjb2-12179**: 全部 208G 数据完好，rsync 迁移主体完成，SFT adapter 补传中\\n  - SSH: `bjb2-12179` (connect.bjb2.seetacloud.com:12179)\\n- **废弃 bjb1-49673**: AutoDL 重启导致数据清空，已关停\\n\\n## GPU 分配教训（2026-05-20）\\n\\nLLaMA SFT 脚本里有 `export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`，会覆盖 submit_training_job 注入的 CUDA_VISIBLE_DEVICES。**必须通过 `GPU=X` 环境变量传物理 GPU 编号**，不能依赖框架注入。\\n\\n## submit_training_job timeout 教训（2026-05-20）\\n\\nLLaMA 8B no-evidence eval 需要 ~2h+。默认 timeout=7200s (2h) 不够，导致 eval_llama_sft_s43_no_evidence 在 244/247 batch (99%) 时被 kill (EXIT_CODE=124)。**所有 LLaMA eval 的 timeout 至少设 14400s (4h)**。\\n\\n## LLaMA 完整统计（2026-05-20 更新）\\n\\n### SFT 3-seed\\n| Seed | ign_f1 | rel_f1 | edcr |\\n|------|--------|--------|------|\\n| s42 | 0.5384 | 0.5514 | — |\\n| s43 | 0.5142 | 0.5308 | 0.5866 |\\n| s44 | 0.4802 | 0.4902 | 0.6579 |\\n| **Mean** | **0.5109** | — | — |\\n| **Std** | **0.0238** | — | — |\\n\\ns44 异常低（较 s42 低 5.8pp），拉大了 SFT 方差。这恰好强化了 RSFT variance compression 的价值。\\n\\n### RSFT 3-seed (k=1)\\n| Seed | ign_f1 | rel_f1 | edcr |\\n|------|--------|--------|------|\\n| s42 | 0.5714 | 0.5839 | 0.5799 |\\n| s43 | 0.5662 | 0.5780 | 0.5783 |\\n| s44 | 0.5587 | 0.5706 | 0.5829 |\\n| **Mean** | **0.5654** | — | — |\\n| **Std** | **0.0052** | — | — |\\n\\n### 跨方法对比\\n- **SFT→RSFT Δ**: +5.45pp\\n- **方差压缩**: 4.58× (0.0238→0.0052)\\n- RSFT 在最弱 SFT seed (s44) 上仍显著提升：0.4802→0.5587 (+7.85pp)\\n\\n### Evidence Tax (LLaMA) — D134 决策：用 fair comparison 报告\\n\\n**RSFT 3-seed（完整）**：\\n- s42: no-evi 0.5526, with-ev
…[truncated 2414 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1309
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T22:28:03.810689+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__tail_training_logs,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__list_workers",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__tail_training_logs,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__list_workers",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T22:28:03.811202+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T22:28:24.064561+00:00_

called mcp__agent-ml-research__tail_training_logs

<details open><summary>🔧 Tool call — mcp__agent-ml-research__tail_training_logs</summary>

```json
{
  "server": "rtx5090-4x",
  "exp_id": "eval_llama_sft_s43_no_evidence_2048",
  "project": "faith-evidence-ie",
  "n": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__tail_training_logs",
  "tool_args": {
    "server": "rtx5090-4x",
    "exp_id": "eval_llama_sft_s43_no_evidence_2048",
    "project": "faith-evidence-ie",
    "n": "80"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T22:28:24.517366+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T22:28:24.920108+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
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

_source line 39 · 2026-05-20T22:28:25.122712+00:00_

{"result":"{\"success\": true, \"data\": {\"lines\": [\"2026-05-21 02:26:34,475 INFO Detected adapter at /root/autodl-tmp/sft_output_llama_3_1_8b_s43, base: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\", \"2026-05-21 02:26:34,475 WARNING --sft_adapter not set but --base_model is non-default (/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B); assuming base is already merged.\", \"2026-05-21 02:26:34,475 INFO Loading tokenizer: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\", \"2026-05-21 02:26:35,268 INFO Loading model: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\", \"[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\", \"\\rLoading weights:   0%|          | 0/291 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/291 [00:00<00:50,  5.74it/s]\\rLoading weights:   1%|          | 2/291 [00:00<00:47,  6.04it/s]\\rLoading weights:   5%|▍         | 14/291 [00:00<00:06, 41.71it/s]\\rLoading weights:   9%|▉         | 27/291 [00:00<00:03, 68.38it/s]\\rLoading weights:  12%|█▏        | 35/291 [00:00<00:04, 63.83it/s]\\rLoading weights:  20%|█▉        | 58/291 [00:00<00:02, 106.24it/s]\\rLoading weights:  24%|██▍       | 70/291 [00:00<00:02, 104.92it/s]\\rLoading weights:  29%|██▉       | 85/291 [00:01<00:01, 113.45it/s]\\rLoading weights:  33%|███▎      | 97/291 [00:01<00:01, 108.08it/s]\\rLoading weights:  37%|███▋      | 109/291 [00:01<00:01, 105.38it/s]\\rLoading weights:  42%|████▏     | 122/291 [00:01<00:01, 109.34it/s]\\rLoading weights:  48%|████▊     | 140/291 [00:01<00:01, 120.03it/s]\\rLoading weights:  53%|█████▎    | 154/291 [00:01<00:01, 124.34it/s]\\rLoading weights:  57%|█████▋    | 167/291 [00:01<00:01, 120.42it/s]\\rLoading weights:  62%|██████▏   | 180/291 [00:01<00:00, 117.59it/s]\\rLoading weights:  66%|██████▌   | 192/291 [00:01<00:00, 109.54it/s]\\rLoading weights:  70%|███████   | 204/291 [00:02<00:00, 109.72it/s]\\rLoading weights:  76%|███████▌  | 220/291 [00:02<00:00, 121.49it/s]\\rLoading weights:  80%
…[truncated 6561 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__tail_training_logs",
  "elapsed_ms": 1058
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T22:28:26.541653+00:00_

{"result":"{\"success\": true, \"data\": {\"allocated_gpus\": [{\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:0\"}, {\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:1\"}, {\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:2\"}, {\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:3\"}], \"actually_running_gpus\": [{\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:0\", \"exp_id\": \"plan017_14b_rsft_eval\"}, {\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"plan017_14b_rsft_no_evidence_eval\"}, {\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:3\", \"exp_id\": \"eval_llama_sft_s42_with_evidence_2048\"}], \"allocated_but_idle\": [{\"server\": \"rtx5090-4x\", \"gpu_id\": \"cuda:1\", \"idle_min\": null, \"util_pct\": null}], \"registered_but_hw_idle\": [], \"unregistered_but_hw_active\": [], \"running_experiments\": [{\"exp_id\": \"plan017_14b_rsft_eval\", \"gpus\": [\"cuda:0\"], \"util_avg\": null}, {\"exp_id\": \"plan017_14b_rsft_no_evidence_eval\", \"gpus\": [\"cuda:2\"], \"util_avg\": null}, {\"exp_id\": \"eval_llama_sft_s42_with_evidence_2048\", \"gpus\": [\"cuda:3\"], \"util_avg\": null}], \"worker_pool\": {\"total\": 0, \"gpu_tasks\": 0, \"cpu_tasks\": 0, \"details\": []}, \"summary\": \"分配 4 张, 实际跑 3 张 ⚠️ | Worker 0 (GPU 0 / CPU 0)\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "elapsed_ms": 2024
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-20T22:28:26.696902+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 1776
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T22:28:52.935093+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_llama_sft_s43_no_evidence_2048",
  "field": "notes",
  "value": "失败原因: timeout_hours=4h 不足，推理完成 237/247 batches (96%) 时被 kill (EXIT_CODE=124)。末段 ~70s/batch，差约 12min。s43 生成更长输出（原 1024 版 truncation=38.4%），2048 版每 batch 耗时远超 s42/s44。| 已有成果: 无（未完成无输出文件）| 建议: 以 timeout_hours=6 重跑 (r2)",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_llama_sft_s43_no_evidence_2048",
    "field": "notes",
    "value": "失败原因: timeout_hours=4h 不足，推理完成 237/247 batches (96%) 时被 kill (EXIT_CODE=124)。末段 ~70s/batch，差约 12min。s43 生成更长输出（原 1024 版 truncation=38.4%），2048 版每 batch 耗时远超 s42/s44。| 已有成果: 无（未完成无输出文件）| 建议: 以 timeout_hours=6 重跑 (r2)",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T22:28:53.890415+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_on_allocated,mcp__agent-ml-research__feishu_send_result_card,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_on_allocated,mcp__agent-ml-research__feishu_send_result_card,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T22:28:54.343581+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_llama_sft_s43_no_evidence_2048\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:26:07.605Z\", \"updated_at\": \"2026-05-20T22:28:53.700Z\", \"hypothesis\": \"方法论一致性：s43 SFT no-evi 用 max_new_tokens=2048 重跑。原 1024 版 truncation=38.4%, ign_f1=0.3391。与 s42/s44 2048 版 matched comparison，验证截断伪影 vs 真实退化。seed=42（标准 eval seed）。\", \"parent\": \"eval_llama_sft_s43_no_evidence_r2\", \"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"rtx5090-4x\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T18:26:28.196Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=1 python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 2048 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_no_evidence_2048\\\"\", \"finished_at\": \"2026-05-20T22:26:45.629Z\", \"training_hours\": 4.0}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=1 python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 2048 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_no_evidence_2048\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"45587\", \"log_path\": \"~/runs/faith-evidence-ie/eval_llama_sft_s43_no_evidence_2048.log\", \"submitted_at\": \"2026-05-20T18:26:31.570Z\", \"submitted_via\": \"submit_training_j
…[truncated 787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1408
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T22:28:54.344180+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "ToolSearch",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-20T22:29:11.321964+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__allocate_and_submit",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__allocate_and_submit",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-20T22:29:11.372779+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T22:29:25.570395+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_llama_sft_s43_no_evidence_2048_r2",
  "field": "hypothesis",
  "value": "方法论一致性：s43 SFT no-evi 用 max_new_tokens=2048 重跑 (r2: timeout 4h→6h)。原 1024 版 truncation=38.4%, ign_f1=0.3391。与 s42/s44 2048 版 matched comparison，验证截断伪影 vs 真实退化。seed=42（标准 eval seed）。",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_llama_sft_s43_no_evidence_2048_r2",
    "field": "hypothesis",
    "value": "方法论一致性：s43 SFT no-evi 用 max_new_tokens=2048 重跑 (r2: timeout 4h→6h)。原 1024 版 truncation=38.4%, ign_f1=0.3391。与 s42/s44 2048 版 matched comparison，验证截断伪影 vs 真实退化。seed=42（标准 eval seed）。",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T22:29:26.424221+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_llama_sft_s43_no_evidence_2048_r2",
  "field": "parent",
  "value": "eval_llama_sft_s43_no_evidence_2048",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_llama_sft_s43_no_evidence_2048_r2",
    "field": "parent",
    "value": "eval_llama_sft_s43_no_evidence_2048",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T22:29:26.980360+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_llama_sft_s43_no_evidence_2048_r2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:29:26.346Z\", \"updated_at\": \"2026-05-20T22:29:26.346Z\", \"hypothesis\": \"方法论一致性：s43 SFT no-evi 用 max_new_tokens=2048 重跑 (r2: timeout 4h→6h)。原 1024 版 truncation=38.4%, ign_f1=0.3391。与 s42/s44 2048 版 matched comparison，验证截断伪影 vs 真实退化。seed=42（标准 eval seed）。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3817}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1409
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-20T22:29:28.396385+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_llama_sft_s43_no_evidence_2048_r2\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:29:26.346Z\", \"updated_at\": \"2026-05-20T22:29:27.807Z\", \"hypothesis\": \"方法论一致性：s43 SFT no-evi 用 max_new_tokens=2048 重跑 (r2: timeout 4h→6h)。原 1024 版 truncation=38.4%, ign_f1=0.3391。与 s42/s44 2048 版 matched comparison，验证截断伪影 vs 真实退化。seed=42（标准 eval seed）。\", \"parent\": \"eval_llama_sft_s43_no_evidence_2048\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3739}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1972
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-20T22:29:34.793418+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_llama_sft_s43_no_evidence_2048_r2",
  "field": "status",
  "value": "QUEUED",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_llama_sft_s43_no_evidence_2048_r2",
    "field": "status",
    "value": "QUEUED",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-20T22:29:37.457605+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_llama_sft_s43_no_evidence_2048_r2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:29:26.346Z\", \"updated_at\": \"2026-05-20T22:29:35.703Z\", \"hypothesis\": \"方法论一致性：s43 SFT no-evi 用 max_new_tokens=2048 重跑 (r2: timeout 4h→6h)。原 1024 版 truncation=38.4%, ign_f1=0.3391。与 s42/s44 2048 版 matched comparison，验证截断伪影 vs 真实退化。seed=42（标准 eval seed）。\", \"parent\": \"eval_llama_sft_s43_no_evidence_2048\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.6744}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2664
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-20T22:29:42.485594+00:00_

called mcp__agent-ml-research__allocate_and_submit

<details open><summary>🔧 Tool call — mcp__agent-ml-research__allocate_and_submit</summary>

```json
{
  "exp_id": "eval_llama_sft_s43_no_evidence_2048_r2",
  "server": "rtx5090-4x",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=1 python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 2048 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_no_evidence_2048\"",
  "gpu_ids": "['cuda:1']",
  "timeout_hours": "6",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__allocate_and_submit",
  "tool_args": {
    "exp_id": "eval_llama_sft_s43_no_evidence_2048_r2",
    "server": "rtx5090-4x",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=1 python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 2048 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_no_evidence_2048\"",
    "gpu_ids": "['cuda:1']",
    "timeout_hours": "6",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-20T22:29:52.593397+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_llama_sft_s43_no_evidence_2048_r2\", \"status\": \"RUNNING\", \"server\": \"rtx5090-4x\", \"gpu_ids\": [\"cuda:1\"], \"pid\": \"58417\", \"log_file\": \"~/runs/faith-evidence-ie/eval_llama_sft_s43_no_evidence_2048_r2.log\", \"account\": \"root\", \"tmux_session\": \"eval_llama_sft_s43_no_evidence_2048_r2\", \"cuda_visible_devices\": \"1\", \"cron_registered\": true, \"code_synced\": false}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.71}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__allocate_and_submit",
  "elapsed_ms": 10107
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-20T22:30:15.328812+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-20T22:30:15.380792+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# faith-evidence-ie Memory\\n\\n## 服务器架构（2026-05-20 更新）\\n\\n- **主服务器 westd-37389**: 4× RTX PRO 6000 Blackwell, 98GB VRAM/卡, 350GB 数据盘 (46% used, 190GB free)\\n  - SSH: `rtx5090-4x` (connect.westd.seetacloud.com:37389)\\n  - 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128, transformers 5.8.1, flash-attn 2.8.3\\n- **数据源 bjb2-12179**: 全部 208G 数据完好，rsync 迁移主体完成，SFT adapter 补传中\\n  - SSH: `bjb2-12179` (connect.bjb2.seetacloud.com:12179)\\n- **废弃 bjb1-49673**: AutoDL 重启导致数据清空，已关停\\n\\n## GPU 分配教训（2026-05-20）\\n\\nLLaMA SFT 脚本里有 `export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`，会覆盖 submit_training_job 注入的 CUDA_VISIBLE_DEVICES。**必须通过 `GPU=X` 环境变量传物理 GPU 编号**，不能依赖框架注入。\\n\\n## submit_training_job timeout 教训（2026-05-20）\\n\\nLLaMA 8B no-evidence eval 需要 ~2h+。默认 timeout=7200s (2h) 不够，导致 eval_llama_sft_s43_no_evidence 在 244/247 batch (99%) 时被 kill (EXIT_CODE=124)。**所有 LLaMA eval 的 timeout 至少设 14400s (4h)**。\\n\\n## LLaMA 完整统计（2026-05-20 更新）\\n\\n### SFT 3-seed\\n| Seed | ign_f1 | rel_f1 | edcr |\\n|------|--------|--------|------|\\n| s42 | 0.5384 | 0.5514 | — |\\n| s43 | 0.5142 | 0.5308 | 0.5866 |\\n| s44 | 0.4802 | 0.4902 | 0.6579 |\\n| **Mean** | **0.5109** | — | — |\\n| **Std** | **0.0238** | — | — |\\n\\ns44 异常低（较 s42 低 5.8pp），拉大了 SFT 方差。这恰好强化了 RSFT variance compression 的价值。\\n\\n### RSFT 3-seed (k=1)\\n| Seed | ign_f1 | rel_f1 | edcr |\\n|------|--------|--------|------|\\n| s42 | 0.5714 | 0.5839 | 0.5799 |\\n| s43 | 0.5662 | 0.5780 | 0.5783 |\\n| s44 | 0.5587 | 0.5706 | 0.5829 |\\n| **Mean** | **0.5654** | — | — |\\n| **Std** | **0.0052** | — | — |\\n\\n### 跨方法对比\\n- **SFT→RSFT Δ**: +5.45pp\\n- **方差压缩**: 4.58× (0.0238→0.0052)\\n- RSFT 在最弱 SFT seed (s44) 上仍显著提升：0.4802→0.5587 (+7.85pp)\\n\\n### Evidence Tax (LLaMA) — D134 决策：用 fair comparison 报告\\n\\n**RSFT 3-seed（完整）**：\\n- s42: no-evi 0.5526, with-ev
…[truncated 2414 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-20T22:30:45.945773+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "content": "# faith-evidence-ie Memory\n\n## 服务器架构（2026-05-20 更新）\n\n- **主服务器 westd-37389**: 4× RTX PRO 6000 Blackwell, 98GB VRAM/卡, 350GB 数据盘 (46% used, 190GB free)\n  - SSH: `rtx5090-4x` (connect.westd.seetacloud.com:37389)\n  - 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128, transformers 5.8.1, flash-attn 2.8.3\n- **数据源 bjb2-12179**: 全部 208G 数据完好，rsync 迁移主体完成，SFT adapter 补传中\n  - SSH: `bjb2-12179` (connect.bjb2.seetacloud.com:12179)\n- **废弃 bjb1-49673**: AutoDL 重启导致数据清空，已关停\n\n## GPU 分配教训（2026-05-20）\n\nLLaMA SFT 脚本里有 `export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`，会覆盖 submit_training_job 注入的 CUDA_VISIBLE_DEVICES。**必须通过 `GPU=X` 环境变量传物理 GPU 编号**，不能依赖框架注入。\n\n## submit_training_job timeout 教训（2026-05-20 更新）\n\nLLaMA 8B no-evidence eval timeout 参考：\n- **max_new_tokens=1024**: ~2h+，至少 14400s (4h)\n- **max_new_tokens=2048 + 高截断 seed (s43)**: ~4.5h+，4h 仍不够（237/247, 96%，末段 ~70s/batch）。**至少 21600s (6h)**。s43 原 1024 版 truncation=38.4%，2048 版生成更长输出导致每 batch 耗时远超 s42/s44\n\n## LLaMA 完整统计（2026-05-20 更新）\n\n### SFT 3-seed\n| Seed | ign_f1 | rel_f1 | edcr |\n|------|--------|--------|------|\n| s42 | 0.5384 | 0.5514 | — |\n| s43 | 0.5142 | 0.5308 | 0.5866 |\n| s44 | 0.4802 | 0.4902 | 0.6579 |\n| **Mean** | **0.5109** | — | — |\n| **Std** | **0.0238** | — | — |\n\ns44 异常低（较 s42 低 5.8pp），拉大了 SFT 方差。这恰好强化了 RSFT variance compression 的价值。\n\n### RSFT 3-seed (k=1)\n| Seed | ign_f1 | rel_f1 | edcr |\n|------|--------|--------|------|\n| s42 | 0.5714 | 0.5839 | 0.5799 |\n| s43 | 0.5662 | 0.5780 | 0.5783 |\n| s44 | 0.5587 | 0.5706 | 0.5829 |\n| **Mean** | **0.5654** | — | — |\n| **Std** | **0.0052** | — | — |\n\n### 跨方法对比\n- **SFT→RSFT Δ**: +5.45pp\n- **方差压缩**: 4.58× (0.0238→0.0052)\n- RSFT 在最弱 SFT seed (s44) 上仍显著提升：0.4802→0.5587 (+7.85pp)\n\n### Evidence Tax (LLaMA) — D134 决策：用 fair comparison 报告\n\n**RSFT 3-seed（完整）**：\n- s42: no-evi 0.5526, with-evi 0.5714, tax=-1.88pp (evidence helps)\n- s43: no-evi 0.5546, with-evi 0.5662, tax=-1.16pp (evidence helps)\n- s44: no-evi 0.5550, with-evi 0.5587, tax=-0.37pp (evidence helps, 微弱)\n- **Mean: -1.14pp ± 0.76pp**（3-seed 一致负向 = evidence 对 RSFT 有帮助）\n- RSFT format compliance: 984/985 (99.9%)，fair comparison ≈ full set\n\n**SFT s44 no-evi 截断异常**：ign_f1=0.3326, truncation 41.7% (411/985)。正在跑 2048 版验证截断 vs 真实退化。\n\n**SFT（1024 版，已完成 2/3 seed）**：\n- s42: raw tax=-1.65pp（不公平），**fair tax=+1.35pp**（evidence 有害）\n- s44: raw tax=-14.76pp, **fair tax=-12.62pp**（evidence 极度有帮助，但截断率异常高）\n- s43: 🔄 running\n\n**2048 版验证实验（进行中）**：\n- eval_llama_sft_s42_no_evidence_2048 (cuda:3) — 方法论一致性\n- eval_llama_sft_s44_no_evidence_2048 (cuda:2) — 截断伪影 vs 真实退化诊断\n\n**Reviewer control 需求**：如果 2048 版结果显著不同于 1024 → 需要 with-evi@2048 control（证明 with-evi 对 token limit 不敏感）。如果差异 <1pp → 不需要。\n\n## 🚨 Evidence Tax 方法论（D134 决策）\n\n**论文报告标准**：用 fair comparison（format-OK 子集），不修 parser。与 1.7B D083 方法论一致。\n\n**Fair comparison 脚本**：`/root/autodl-tmp/freige/scripts/analysis/fair_evidence_tax.py`，已用 s42 数据验证通过。\n\n**RSFT 压缩 evidence tax 方差**（Director insight）：SFT evidence tax swing 14pp（+1.35 到 -12.62），RSFT swing 1.5pp（-0.38 到 -1.88）。RSFT 不仅压缩 RE 方差，还让 evidence 的角色变得可预测。SFT 下 evidence 效果是 seed lottery，RSFT 下一致有帮助。\n\n## RSFT inference 架构（2026-05-20 确认）\n\nRSFT 是 nested LoRA：inference.py 先 merge SFT adapter 到 base model，再加载 RSFT adapter。**eval 时必须传 `--sft_adapter` 参数**，否则代码报错。\n\n## 14B Pipeline 状态（2026-05-20 更新）\n\n- Generation: r4 完成, 24216 candidates from 3027 docs\n- **CED Scoring 完成** (plan017_14b_ced_scoring)：\n  - 输出: `/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl` (3015 条, 9.1MB)\n  - Selected F1=0.730, CED=0.690, Combined=0.768\n  - vs 4B: F1 +5.4pp (0.676→0.730), CED +1.4pp (0.676→0.690)\n  - 14B 候选质量显著优于 4B，验证 scaling 假设\n- 下一步: RSFT training on 14B scored data\n\n## Qwen3-8B RSFT Evidence Tax 确认（2026-05-20）\n\n- no-evi ign_f1 = 0.5336, with-evi ign_f1 = 0.5414\n- D127 tax = -0.78pp（evidence helps，微弱）\n- 与 LLaMA RSFT (-1.14pp) 方向一致，跨家族均为负\n\n## Reviewer 发现（2026-05-20）\n\n- SFT evidence tax 方法论不一致：应该用同一模型加 `--no_evidence` flag，而非对比独立训练的 no-evidence 模型\n- LLaMA eval configs 的 base_model 指向 Qwen3-4B（不影响结果，model_path 正确）\n\n## 竞品实验参考\n\n（待填充——首次进入新方向时从 literature_map 提取）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "memory.md",
    "content": "# faith-evidence-ie Memory\n\n## 服务器架构（2026-05-20 更新）\n\n- **主服务器 westd-37389**: 4× RTX PRO 6000 Blackwell, 98GB VRAM/卡, 350GB 数据盘 (46% used, 190GB free)\n  - SSH: `rtx5090-4x` (connect.westd.seetacloud.com:37389)\n  - 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128, transformers 5.8.1, flash-attn 2.8.3\n- **数据源 bjb2-12179**: 全部 208G 数据完好，rsync 迁移主体完成，SFT adapter 补传中\n  - SSH: `bjb2-12179` (connect.bjb2.seetacloud.com:12179)\n- **废弃 bjb1-49673**: AutoDL 重启导致数据清空，已关停\n\n## GPU 分配教训（2026-05-20）\n\nLLaMA SFT 脚本里有 `export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`，会覆盖 submit_training_job 注入的 CUDA_VISIBLE_DEVICES。**必须通过 `GPU=X` 环境变量传物理 GPU 编号**，不能依赖框架注入。\n\n## submit_training_job timeout 教训（2026-05-20 更新）\n\nLLaMA 8B no-evidence eval timeout 参考：\n- **max_new_tokens=1024**: ~2h+，至少 14400s (4h)\n- **max_new_tokens=2048 + 高截断 seed (s43)**: ~4.5h+，4h 仍不够（237/247, 96%，末段 ~70s/batch）。**至少 21600s (6h)**。s43 原 1024 版 truncation=38.4%，2048 版生成更长输出导致每 batch 耗时远超 s42/s44\n\n## LLaMA 完整统计（2026-05-20 更新）\n\n### SFT 3-seed\n| Seed | ign_f1 | rel_f1 | edcr |\n|------|--------|--------|------|\n| s42 | 0.5384 | 0.5514 | — |\n| s43 | 0.5142 | 0.5308 | 0.5866 |\n| s44 | 0.4802 | 0.4902 | 0.6579 |\n| **Mean** | **0.5109** | — | — |\n| **Std** | **0.0238** | — | — |\n\ns44 异常低（较 s42 低 5.8pp），拉大了 SFT 方差。这恰好强化了 RSFT variance compression 的价值。\n\n### RSFT 3-seed (k=1)\n| Seed | ign_f1 | rel_f1 | edcr |\n|------|--------|--------|------|\n| s42 | 0.5714 | 0.5839 | 0.5799 |\n| s43 | 0.5662 | 0.5780 | 0.5783 |\n| s44 | 0.5587 | 0.5706 | 0.5829 |\n| **Mean** | **0.5654** | — | — |\n| **Std** | **0.0052** | — | — |\n\n### 跨方法对比\n- **SFT→RSFT Δ**: +5.45pp\n- **方差压缩**: 4.58× (0.0238→0.0052)\n- RSFT 在最弱 SFT seed (s44) 上仍显著提升：0.4802→0.5587 (+7.85pp)\n\n### Evidence Tax (LLaMA) — D134 决策：用 fair comparison 报告\n\n**RSFT 3-seed（完整）**：\n- s42: no-evi 0.5526, with-evi 0.5714, tax=-1.88pp (evidence helps)\n- s43: no-evi 0.5546, with-evi 0.5662, tax=-1.16pp (evidence helps)\n- s44: no-evi 0.5550, with-evi 0.5587, tax=-0.37pp (evidence helps, 微弱)\n- **Mean: -1.14pp ± 0.76pp**（3-seed 一致负向 = evidence 对 RSFT 有帮助）\n- RSFT format compliance: 984/985 (99.9%)，fair comparison ≈ full set\n\n**SFT s44 no-evi 截断异常**：ign_f1=0.3326, truncation 41.7% (411/985)。正在跑 2048 版验证截断 vs 真实退化。\n\n**SFT（1024 版，已完成 2/3 seed）**：\n- s42: raw tax=-1.65pp（不公平），**fair tax=+1.35pp**（evidence 有害）\n- s44: raw tax=-14.76pp, **fair tax=-12.62pp**（evidence 极度有帮助，但截断率异常高）\n- s43: 🔄 running\n\n**2048 版验证实验（进行中）**：\n- eval_llama_sft_s42_no_evidence_2048 (cuda:3) — 方法论一致性\n- eval_llama_sft_s44_no_evidence_2048 (cuda:2) — 截断伪影 vs 真实退化诊断\n\n**Reviewer control 需求**：如果 2048 版结果显著不同于 1024 → 需要 with-evi@2048 control（证明 with-evi 对 token limit 不敏感）。如果差异 <1pp → 不需要。\n\n## 🚨 Evidence Tax 方法论（D134 决策）\n\n**论文报告标准**：用 fair comparison（format-OK 子集），不修 parser。与 1.7B D083 方法论一致。\n\n**Fair comparison 脚本**：`/root/autodl-tmp/freige/scripts/analysis/fair_evidence_tax.py`，已用 s42 数据验证通过。\n\n**RSFT 压缩 evidence tax 方差**（Director insight）：SFT evidence tax swing 14pp（+1.35 到 -12.62），RSFT swing 1.5pp（-0.38 到 -1.88）。RSFT 不仅压缩 RE 方差，还让 evidence 的角色变得可预测。SFT 下 evidence 效果是 seed lottery，RSFT 下一致有帮助。\n\n## RSFT inference 架构（2026-05-20 确认）\n\nRSFT 是 nested LoRA：inference.py 先 merge SFT adapter 到 base model，再加载 RSFT adapter。**eval 时必须传 `--sft_adapter` 参数**，否则代码报错。\n\n## 14B Pipeline 状态（2026-05-20 更新）\n\n- Generation: r4 完成, 24216 candidates from 3027 docs\n- **CED Scoring 完成** (plan017_14b_ced_scoring)：\n  - 输出: `/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl` (3015 条, 9.1MB)\n  - Selected F1=0.730, CED=0.690, Combined=0.768\n  - vs 4B: F1 +5.4pp (0.676→0.730), CED +1.4pp (0.676→0.690)\n  - 14B 候选质量显著优于 4B，验证 scaling 假设\n- 下一步: RSFT training on 14B scored data\n\n## Qwen3-8B RSFT Evidence Tax 确认（2026-05-20）\n\n- no-evi ign_f1 = 0.5336, with-evi ign_f1 = 0.5414\n- D127 tax = -0.78pp（evidence helps，微弱）\n- 与 LLaMA RSFT (-1.14pp) 方向一致，跨家族均为负\n\n## Reviewer 发现（2026-05-20）\n\n- SFT evidence tax 方法论不一致：应该用同一模型加 `--no_evidence` flag，而非对比独立训练的 no-evidence 模型\n- LLaMA eval configs 的 base_model 指向 Qwen3-4B（不影响结果，model_path 正确）\n\n## 竞品实验参考\n\n（待填充——首次进入新方向时从 literature_map 提取）\n"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-20T22:30:46.249679+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 303
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-20T22:30:49.271428+00:00_

called mcp__agent-ml-research__feishu_send_result_card

<details open><summary>🔧 Tool call — mcp__agent-ml-research__feishu_send_result_card</summary>

```json
{
  "exp_id": "eval_llama_sft_s43_no_evidence_2048",
  "conclusion": "failed",
  "key_metrics": "{}",
  "baseline_comparison": "Timeout (EXIT_CODE=124): 237/247 batches (96%) 完成后被 kill。4h timeout 不足以覆盖 s43@2048 的长输出生成。已以 timeout_hours=6 重提交 r2 到 cuda:1。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__feishu_send_result_card",
  "tool_args": {
    "exp_id": "eval_llama_sft_s43_no_evidence_2048",
    "conclusion": "failed",
    "key_metrics": "{}",
    "baseline_comparison": "Timeout (EXIT_CODE=124): 237/247 batches (96%) 完成后被 kill。4h timeout 不足以覆盖 s43@2048 的长输出生成。已以 timeout_hours=6 重提交 r2 到 cuda:1。"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-20T22:30:55.404918+00:00_

{"result":"{\"success\": true, \"data\": {\"message_id\": \"om_x100b6fd72f03c4a8c27bb00ae13cbce\", \"chat_id\": \"oc_84537e1e2f9ef71a90742c2db859c6f2\", \"msg_type\": \"interactive\", \"next_required_steps\": \"飞书卡片已发出。请立即完成剩余步骤（不可跳过）： (1) 如有跨实验价值的教训/约定 → save_project_file(file='memory.md', ...) 追加一行； (2) move_idea — 将实验从 IN_PROGRESS 移到对应区块。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__feishu_send_result_card",
  "elapsed_ms": 6133
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-20T22:30:55.505860+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 4/4 | Worker 0 (GPU 0 / CPU 0) | 磁盘: rtx5090-4x 815G/879G (3%)\n\n**eval_llama_sft_s43_no_evidence_2048 失败 — timeout 自动修复**\n\n失败原因：EXIT_CODE=124，timeout_hours=4 不足。推理到 237/247 batch (96%)，末段 ~70s/batch，差约 12min。s43 因高截断率（原 1024 版 38.4%）在 2048 版生成更长输出，耗时远超 s42/s44。\n\n已处理：\n- 以 timeout_hours=6 重提交 `eval_llama_sft_s43_no_evidence_2048_r2` 到 cuda:1，已 RUNNING (pid=58417)\n- registry 已更新，memory.md timeout 教训已补充 2048 版参考\n\n当前 4 GPU 全满：\n- cuda:0: plan017_14b_rsft_eval\n- cuda:1: eval_llama_sft_s43_no_evidence_2048_r2（刚提交）\n- cuda:2: plan017_14b_rsft_no_evidence_eval\n- cuda:3: eval_llama_sft_s42_with_evidence_2048",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 4/4 | Worker 0 (GPU 0 / CPU 0) | 磁盘: rtx5090-4x 815G/879G (3%)\n\n**eval_llama_sft_s43_no_evidence_2048 失败 — timeout 自动修复**\n\n失败原因：EXIT_CODE=124，timeout_hours=4 不足。推理到 237/247 batch (96%)，末段 ~70s/batch，差约 12min。s43 因高截断率（原 1024 版 38.4%）在 2048 版生成更长输出，耗时远超 s42/s44。\n\n已处理：\n- 以 timeout_hours=6 重提交 `eval_llama_sft_s43_no_evidence_2048_r2` 到 cuda:1，已 RUNNING (pid=58417)\n- registry 已更新，memory.md timeout 教训已补充 2048 版参考\n\n当前 4 GPU 全满：\n- cuda:0: plan017_14b_rsft_eval\n- cuda:1: eval_llama_sft_s43_no_evidence_2048_r2（刚提交）\n- cuda:2: plan017_14b_rsft_no_evidence_eval\n- cuda:3: eval_llama_sft_s42_with_evidence_2048",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-20T22:30:56.662454+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_84537e1e2f9ef71a90742c2db859c6f2:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 1156
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-20T22:31:02.512427+00:00_

诊断和修复完成：

- **根因**：`eval_llama_sft_s43_no_evidence_2048` 超时 (EXIT_CODE=124)，4h timeout 不够。到 237/247 batch (96%) 被 kill，差约 12min。s43 高截断率导致 2048 版生成更长输出，末段 ~70s/batch。
- **已修复**：以 timeout_hours=6 重提交 `eval_llama_sft_s43_no_evidence_2048_r2` 到 cuda:1，已 RUNNING (pid=58417)。
- **更新**：registry notes、memory.md timeout 教训、飞书卡片已发、Director 已汇报。
- **当前 4 GPU 全满**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 65 · 2026-05-21T15:01:27.052659+00:00_

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
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 66 · 2026-05-21T15:02:11.769719+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：rtx5090-4x 的 cuda:0/1/2/3，不得用其他设备
- LLaMA SFT 脚本用 `GPU=X` 传物理 GPU 编号，不能依赖框架注入的 CUDA_VISIBLE_DEVICES（脚本内部会覆盖）
- RSFT eval 必须传 `--sft_adapter` 参数（nested LoRA 架构，不传会报错）
- Evidence tax 论文报告标准：用 fair comparison（format-OK 子集），不修 parser（D134 决策）
- LLaMA eval timeout：1024 版至少 4h，2048 版（尤其 s43 高截断 seed）至少 6h
- 14B 模型 SFT adapter 路径是 `sft_output_14b/checkpoint-144`（不是顶层目录）

### 2. 🖥️ 基础设施快照
- **服务器**: rtx5090-4x (connect.westd.seetacloud.com:37389), 4×RTX PRO 6000 98GB
- **工作目录**: /root/autodl-tmp/freige
- **Python**: conda base, /root/miniconda3/bin/python, Python 3.12, PyTorch 2.8.0+cu128
- **模型路径**: /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B, /root/autodl-tmp/models/Qwen/Qwen3-14B
- **SFT adapters**: sft_output_llama_3_1_8b (s42), sft_output_llama_3_1_8b_s43, sft_output_llama_3_1_8b_s44
- **数据**: /root/autodl-tmp/data/docred (dev.json: 998 docs, 12275 triples)
- **14B RSFT scored data**: /root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl (3015 条)
- **Fair tax 脚本**: /root/autodl-tmp/freige/scripts/analysis/fair_evidence_tax.py
- **磁盘**: 815G/879G 可用 (3% used)
- **活跃进程**:
  - plan017_14b_rsft_eval (cuda:0, PID 53413)
  - eval_llama_sft_s43_no_evidence_2048_r2 (cuda:1, PID 58417, tmux=eval_llama_sft_s43_no_evidence_2048_r2)
  - plan017_14b_rsft_no_evidence_eval (cuda:2, PID 55039)
  - eval_llama_sft_s42_with_evidence_2048 (cuda:3, PID 55468)

### 3. 📊 当前状态
刚处理 eval_llama_sft_s43_no_evidence_2048 的 timeout 失败（EXIT_CODE=124, 237/247 batch, 96%）。已以 timeout_hours=6 重提交为 r2 到 cuda:1。4 GPU 全满，Director 已汇报。

RUNNING 实验：
- **plan017_14b_rsft_eval** (cuda:0): 14B RSFT eval on DocRED dev，期望超越 SFT 0.5507 baseline
- **eval_llama_sft_s43_no_evidence_2048_r2** (cuda:1): s43 SFT no-evi 2048 版重跑，补齐 3-seed evidence tax
- **plan017_14b_rsft_no_evidence_eval** (cuda:2): 14B RSFT no-evidence eval，测 14B scale evidence tax
- **eval_llama_sft_s42_with_evidence_2048** (cuda:3): s42 with-evi@2048 control，验证 with-evi 对 token limit 不敏感

等待：4 个实验的 cron 完成回调。无 Worker 在跑。

### 4. 📋 待办
- plan017_14b_rsft_eval 完成 → 与 SFT 0.5507 对比，填 scaling table 14B 行 RSFT 列；success 则 14B scaling story 完整
- plan017_14b_rsft_no_evidence_eval 完成 → 计算 14B evidence tax，与 8B/4B/1.7B 对比 tax 趋势
- eval_llama_sft_s43_no_evidence_2048_r2 完成 → 跑 fair_evidence_tax.py 算 s43 fair tax；3-seed SFT evidence tax 完整后与 RSFT 3-seed (-1.14pp±0.76pp) 对比方差
- eval_llama_sft_s42_with_evidence_2048 完成 → 与 s42@1024 (ign_f1=0.5384) 对比：delta<1pp 则 with-evi 对 token limit 不敏感（方法论合理），delta>1pp 则需要调整 evidence tax 计算
- 所有 LLaMA evidence tax 实验完成 → 汇总 SFT vs RSFT evidence tax swing 对比，更新论文 Table

### 5. 🎯 战略上下文
- **核心方向**: FREIGE — LLM-based evidence-grounded DocRE，3 贡献：RSFT+NLI 有效性、Decoupling spectrum、Scale-dependent evidence tax + variance compression
- **投稿目标**: EMNLP 2026 Main (ARR July, ~56 天)
- **Scaling table** (核心论据): 1.7B/4B/8B/LLaMA-8B 已完成，14B RSFT eval 是最后一行
- **D136 关键发现**: LLaMA SFT evidence tax wildly seed-dependent（s42 +1.35pp vs s44 -12.62pp），而 RSFT 一致 -1.14pp±0.76pp。这是 variance compression 最强证据之一
- **易错点**:
  - s42 的 eval 结果是 ign_f1=0.5384（不是 0.5514，后者是 rel_f1）
  - LLaMA RSFT s42 ign_f1=0.5714（不是 0.5839=rel_f1），D129 已修正
  - 4B RSFT 有两版数据（A 版 k=3 vs B 版 k=1），论文用 B 版 (0.5152)
  - SFT evidence tax 的 "fair comparison" 只看 format-OK 子集，不是全集
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval_llama_sft_s43_no_evidence_2048"
}
```

</details>

---
