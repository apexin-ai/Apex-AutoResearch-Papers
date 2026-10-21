# cron hook exp 001 eval 3B instruct aligned para 20260516T145240 839196

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 2
- **Tool calls:** 27
- **Original source:** `logs/chats/archive/cron_hook_exp_001_eval_3B_instruct_aligned_para_20260516T145240_839196.jsonl`
- **Structured JSON:** [`42750276679a6b4e2032.json`](../../sessions/42/42750276679a6b4e2032.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-16T10:28:50.091676+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: exp_001_eval_3B_instruct_aligned_para
- project: contamcal-irt-calibration
- server: cqa1-21977
- log_path: /root/runs/contamcal-irt-calibration/exp_001_eval_3B_instruct_aligned_para.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-16T10:29:03.586366+00:00_

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
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
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

_source line 3 · 2026-05-16T10:29:03.586957+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T10:29:08.194500+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T10:29:08.194936+00:00_

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
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T10:29:08.797800+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "report.md"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T10:29:08.898525+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T10:29:09.055382+00:00_

Error: result (337,662 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-9f9278f8/38f91620-8716-4ff5-9a4a-642bce4b18f2/tool-results/mcp-agent-ml-research-read_registry-1778927348996.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-9f9278f8/38f91620-8716-4ff5-9a4a-642bce4b18f2/tool-results/mcp-agent-ml-research-read_registry-1778927348996.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 860
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T10:29:18.101691+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 4, \"results\": [{\"exp_id\": \"exp_002_signals_05B_s123_v2\", \"success\": true, \"actions\": [\"Job still running (pid=exp002_05B_s123_v2)\"]}, {\"exp_id\": \"exp_002_signals_15B_s123_batch\", \"success\": true, \"actions\": [\"Job still running (pid=691872)\"]}, {\"exp_id\": \"exp_002_signals_3B_d100_a32_s42\", \"success\": true, \"actions\": [\"Job still running (pid=724022)\"]}, {\"exp_id\": \"exp_002_signals_15B_d100_s123_cuda2\", \"success\": true, \"actions\": [\"Job still running (pid=746777)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 9906
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T10:29:18.154409+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-16T10:28:48Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 211 个实验 — ANALYZING 1, DONE 185, PREPARING 21, RUNNING 4\\n**DONE 分布**: failed 44, killed 10, negative 3, success 128\\n\\n### GPU 占用\\n- **分配**: 6 张 — cqa1-21977:cuda:0, cqa1-21977:cuda:1, cqa1-21977:cuda:2, cqa1-21977:cuda:3, cqa1-21977:cuda:4, cqa1-21977:cuda:5\\n- **实际运行**: 4 张 — cqa1-21977:cuda:5(exp_002_signals_05B_s123_v2), cqa1-21977:cuda:0(exp_002_signals_15B_s123_batch), cqa1-21977:cuda:1(exp_002_signals_3B_d100_a32_s42), cqa1-21977:cuda:2(exp_002_signals_15B_d100_s123_cuda2)\\n- **空闲（分配了没跑）**: cqa1-21977:cuda:3, cqa1-21977:cuda:4\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `exp_002_signals_05B_s123_v2` | cqa1-21977 | cuda:5 | ? | `/root/autodl-tmp/exp002/signals/signals_05B_s123_v2.log` |\\n| `exp_002_signals_15B_s123_batch` | cqa1-21977 | cuda:0 | 691872 | `…ontamcal-irt-calibration/exp_002_signals_15B_s123_batch.log` |\\n| `exp_002_signals_3B_d100_a32_s42` | cqa1-21977 | cuda:1 | 724022 | `…ntamcal-irt-calibration/exp_002_signals_3B_d100_a32_s42.log` |\\n| `exp_002_signals_15B_d100_s123_cuda2` | cqa1-21977 | cuda:2 | 746777 | `…ontamcal-irt-calibration/exp002/run_15B_d100_s123_cuda2.log` |\\n\\n### 📌 最近完成 (top 5)\\n- `exp_002_signals_3B_d000_a32_s42` [success] — 2026-05-16T10:23:58\\n- `exp_002_signals_3B_d005_a32_s42` [success] — 2026-05-16T10:11:52 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n- `exp_006_pooled_irt_05b_15b_arc_2pl` [negative] — 2026-05-16T09:21:36\\n- `exp_006_pooled_irt_05b_15b` [success] — 2026-05-16T09:16:12\\n- `exp006_pooled_rrf_irt_05b_15b` [success] — 2026-05-16T09:08:42\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover
…[truncated 3973 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 9356
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T10:29:18.155120+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-16 10:26 UTC | 更新原因: Reviewer critical: 修正d005 false failure + D108措辞降级为domain heterogeneity evidence + GPU状态同步\\n\\n## 核心方向\\nContamCal：contamination-augmented IRT with per-benchmark γ_k → domain heterogeneity evidence (Simpson's paradox, D108)。详见 paper_framing.md。\\n\\n## 投稿目标\\n**EMNLP 2026 ARR May 25**（距今 9 天）\\n\\n## 当前进展\\n- **阶段**: Research (MVP 2026-05-13 通过) + 审稿进行中\\n- **D108 发现**: MMLU 57 subjects → 8 cognitive domains，aggregate γ≈0 masks domain heterogeneity (5 domains significant, γ range: -0.55 to +1.34)。PPP=0 in 4/5 domains → claim 基于 pattern/ranking，非绝对值。N=24 重跑确认前为\\\"evidence of heterogeneity\\\"\\n- **3B s42 signals**: d000 ✅ d005 ✅ d025 ✅ d100 🔄(cuda:1, ~35min)。d100 完成后全齐 → RRF\\n- **0.5B s123**: 全部完成 ✅\\n- **1.5B s123**: d025 running (cuda:0), d100 running (cuda:2)。完成后全量 RRF (N≥16+)\\n- **Scope expansion (D106)**: Llama 代码+模型就绪 | RL observational 3B-Instruct eval running (cuda:3) | 7B 待云GPU\\n\\n## GPU 实时占用 (6× RTX 4090D, cqa1-21977)\\n| GPU | 任务 | 预计完成 |\\n|-----|------|---------|\\n| cuda:0 | signals_15B_s123_batch (d025) | ~2h |\\n| cuda:1 | signals_3B_d100_a32_s42 | ~35min |\\n| cuda:2 | signals_15B_d100_s123 | ~3h |\\n| cuda:3 | eval_3B_instruct_aligned_para (P0-C) | ~1h |\\n| cuda:4 | **待分配 → Llama-3.2-3B d000 SFT** | 指令已发 |\\n| cuda:5 | signals_05B_s123_v2 (d100) | ~2.5h |\\n\\n## Critical Path (EMNLP T-9)\\n```\\n[Now]     cuda:1 d100 ~35min → 3B s42 全齐 → RRF 聚合 (CPU)\\n          cuda:4 → Llama-3.2-3B d000 SFT 启动\\n          cuda:3 3B-Instruct eval ~1h → 0.5B/1.5B-Instruct eval\\n[Day 1]   pooled IRT (N≥16+) — 论文核心 γ 数字\\n          MMLU domain gamma N=24 (含 3B) — 确认 heterogeneity 是否 scale-dependent\\n          Llama d000 SFT + eval\\n[Day 2]   Llama d005/d025/d100 SFT + eval + signals\\n          scale-st
…[truncated 2160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 9256
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T10:29:30.159151+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": "{'exp_id': 'exp_001_eval_3B_instruct_aligned_para'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "filters": "{'exp_id': 'exp_001_eval_3B_instruct_aligned_para'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T10:29:30.712545+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.502}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 553
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T10:29:37.669503+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"instruct_aligned_para\\|instruct.*aligned.*para\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml | head -20",
  "description": "Search registry for instruct_aligned_para experiment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"instruct_aligned_para\\|instruct.*aligned.*para\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml | head -20",
    "description": "Search registry for instruct_aligned_para experiment"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-16T10:29:37.820789+00:00_

7766:  exp_001_eval_3B_instruct_aligned_para:
7777:      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_3B_instruct_aligned_para.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T10:29:41.792824+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml",
  "offset": "7765",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/registry.yaml",
    "offset": "7765",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T10:29:41.843438+00:00_

7765	    checkpoint_path: /root/autodl-tmp/exp006/results_mmlu_domain_gamma/
7766	  exp_001_eval_3B_instruct_aligned_para:
7767	    status: ANALYZING
7768	    retry_count: 0
7769	    created_at: '2026-05-16T07:54:58.792Z'
7770	    updated_at: '2026-05-16T10:28:46.207Z'
7771	    spec:
7772	      command: bash /root/contamcal-irt-calibration/scripts/run_instruct_3b_eval.sh
7773	      server: cqa1-21977
7774	      gpu:
7775	      - cuda:3
7776	      pid: '730671'
7777	      log_path: ~/runs/contamcal-irt-calibration/exp_001_eval_3B_instruct_aligned_para.log
7778	      submitted_at: '2026-05-16T07:54:58.299Z'
7779	      submitted_via: submit_training_job
7780	      backend: tmux
7781	      account: root
7782	      data_path: /root/autodl-tmp/exp001/paraphrases/
7783	      data_count: 0
7784	      model_name: Qwen/Qwen2.5-3B-Instruct
7785	      seed: null
7786	      checkpoint_source: huggingface
7787	      eval_data: mmlu,gsm8k,arc_challenge,humaneval (aligned + para_aligned)
7788	    hypothesis: 'Qwen2.5-3B-Instruct (RL post-trained) eval. P0-C RL observational:
7789	      verify signal patterns after RLHF. No training, inference only. Aligned + para_aligned
7790	      on 4 benchmarks.'
7791	    reproduce:
7792	      finished_at: '2026-05-16T10:28:45.392Z'
7793	    extra:
7794	      hook_events:
7795	      - event: on_complete
7796	        action: agent
7797	        ts: '2026-05-16T10:28:49.480069+00:00'
7798	  exp006_pooled_rrf_irt_05b_15b:
7799	    status: DONE
7800	    retry_count: 0
7801	    created_at: '2026-05-16T09:02:32.472Z'
7802	    updated_at: '2026-05-16T09:08:42.567Z'
7803	    spec:
7804	      command: python3 run_pooled_rrf_irt.py --scales 0.5B 1.5B --benchmarks gsm8k
7805	        arc_challenge --model-type 4pl_gamma
7806	      server: cqa1-21977
7807	      gpu:
7808	      - cuda:0
7809	      pid: '738279'
7810	      log_path: /root/runs/contamcal-irt-calibration/exp006_pooled_rrf_irt_05b_15b_v2.log
7811	      submitted_at: '2026-05-16T09:02:31.986Z'
7812
…[truncated 91 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-16T10:29:52.129062+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T10:29:52.129485+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-16T10:30:28.099555+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "analysis:exp_001_eval_3B_instruct_aligned_para",
  "project": "contamcal-irt-calibration",
  "task_prompt": "## 任务：分析 exp_001_eval_3B_instruct_aligned_para 实验结果\n\n### 背景\n这是一个 eval-only 实验，用 Qwen2.5-3B-Instruct（HuggingFace 原始权重，RL post-trained）在 4 个 benchmark 的 aligned + para_aligned 版本上做推理评估。\n\n**假设**: 验证 RLHF 后的 Instruct 模型是否仍然表现出 contamination signal patterns（aligned vs para_aligned 的性能差异）。这是 P0-C \"RL observational\" 验证。\n\n**服务器**: cqa1-21977\n**日志路径**: /root/runs/contamcal-irt-calibration/exp_001_eval_3B_instruct_aligned_para.log\n**评估数据**: mmlu, gsm8k, arc_challenge, humaneval (aligned + para_aligned)\n**模型**: Qwen/Qwen2.5-3B-Instruct\n\n### 你需要做的\n\n1. **读取日志文件**：SSH 到 cqa1-21977 读取完整日志（或至少最后 200 行），找到各 benchmark 的 accuracy 指标\n2. **查 W&B 指标**：用 fetch_wandb_metrics 查这个 run 的指标（项目名可能是 contamcal-irt-calibration 或类似）\n3. **分析 contamination signals**：\n   - 每个 benchmark 的 aligned accuracy vs para_aligned accuracy\n   - 计算 gap = aligned - para_aligned（正值 = contamination signal 存在）\n   - 与已有的 base model（非 Instruct）结果对比（如果日志中有参考）\n4. **判断 conclusion**：\n   - 如果 Instruct 模型仍显示显著 gap（大部分 benchmark 有 >2pp 差异）→ success（RL 不消除 contamination signals）\n   - 如果 gap 消失或大幅缩小 → 也是 success（重要发现：RL 可能抑制 contamination 信号）\n   - 只有代码报错/数据异常才是 failed\n\n### 输出格式\n请在最终输出中明确写出：\n```\nCONCLUSION: success/negative/failed\nMETRICS:\n  mmlu_aligned: X.XX\n  mmlu_para: X.XX\n  mmlu_gap: X.XX\n  gsm8k_aligned: X.XX\n  gsm8k_para: X.XX\n  gsm8k_gap: X.XX\n  arc_aligned: X.XX\n  arc_para: X.XX\n  arc_gap: X.XX\n  humaneval_aligned: X.XX (if available)\n  humaneval_para: X.XX (if available)\n  humaneval_gap: X.XX (if available)\nSUMMARY: 一句话总结发现\nCHECKPOINT_PATH: 结果文件路径（如有输出 JSON/CSV）\n```\n",
  "tool_groups": "['ssh', 'wandb']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analysis:exp_001_eval_3B_instruct_aligned_para",
    "project": "contamcal-irt-calibration",
    "task_prompt": "## 任务：分析 exp_001_eval_3B_instruct_aligned_para 实验结果\n\n### 背景\n这是一个 eval-only 实验，用 Qwen2.5-3B-Instruct（HuggingFace 原始权重，RL post-trained）在 4 个 benchmark 的 aligned + para_aligned 版本上做推理评估。\n\n**假设**: 验证 RLHF 后的 Instruct 模型是否仍然表现出 contamination signal patterns（aligned vs para_aligned 的性能差异）。这是 P0-C \"RL observational\" 验证。\n\n**服务器**: cqa1-21977\n**日志路径**: /root/runs/contamcal-irt-calibration/exp_001_eval_3B_instruct_aligned_para.log\n**评估数据**: mmlu, gsm8k, arc_challenge, humaneval (aligned + para_aligned)\n**模型**: Qwen/Qwen2.5-3B-Instruct\n\n### 你需要做的\n\n1. **读取日志文件**：SSH 到 cqa1-21977 读取完整日志（或至少最后 200 行），找到各 benchmark 的 accuracy 指标\n2. **查 W&B 指标**：用 fetch_wandb_metrics 查这个 run 的指标（项目名可能是 contamcal-irt-calibration 或类似）\n3. **分析 contamination signals**：\n   - 每个 benchmark 的 aligned accuracy vs para_aligned accuracy\n   - 计算 gap = aligned - para_aligned（正值 = contamination signal 存在）\n   - 与已有的 base model（非 Instruct）结果对比（如果日志中有参考）\n4. **判断 conclusion**：\n   - 如果 Instruct 模型仍显示显著 gap（大部分 benchmark 有 >2pp 差异）→ success（RL 不消除 contamination signals）\n   - 如果 gap 消失或大幅缩小 → 也是 success（重要发现：RL 可能抑制 contamination 信号）\n   - 只有代码报错/数据异常才是 failed\n\n### 输出格式\n请在最终输出中明确写出：\n```\nCONCLUSION: success/negative/failed\nMETRICS:\n  mmlu_aligned: X.XX\n  mmlu_para: X.XX\n  mmlu_gap: X.XX\n  gsm8k_aligned: X.XX\n  gsm8k_para: X.XX\n  gsm8k_gap: X.XX\n  arc_aligned: X.XX\n  arc_para: X.XX\n  arc_gap: X.XX\n  humaneval_aligned: X.XX (if available)\n  humaneval_para: X.XX (if available)\n  humaneval_gap: X.XX (if available)\nSUMMARY: 一句话总结发现\nCHECKPOINT_PATH: 结果文件路径（如有输出 JSON/CSV）\n```\n",
    "tool_groups": "['ssh', 'wandb']"
  }
}
````

</details>

---

### Tool result

_source line 21 · 2026-05-16T10:30:31.118140+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_exp_001_eval_3B_instruct_aligned_para_20260516T103028\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/logs/workers/worker_analysis_exp_001_eval_3B_instruct_aligned_para_20260516T103028.log\", \"setup_data\": {}, \"message\": \"Worker worker_analysis_exp_001_eval_3B_instruct_aligned_para_20260516T103028 started. Use get_worker_status('worker_analysis_exp_001_eval_3B_instruct_aligned_para_20260516T103028') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 3018
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T10:30:56.680744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/skills/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-16T10:30:56.732003+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_9f9278f8.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T10:31:00.847553+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T10:31:00.948297+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-16T10:31:08.609474+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/skills/**/resource*",
  "path": "/home/ubuntu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/skills/**/resource*",
    "path": "/home/ubuntu"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-16T10:31:09.212549+00:00_

/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "Glob",
  "elapsed_ms": 603
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-16T10:31:12.582257+00:00_

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
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-16T10:31:12.633590+00:00_

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
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T10:31:29.277485+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": "{'status': 'PREPARING'}",
  "fields": "['exp_id', 'hypothesis', 'status']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "filters": "{'status': 'PREPARING'}",
    "fields": "['exp_id', 'hypothesis', 'status']"
  }
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-16T10:48:50.547154+00:00_

Worker 已派发分析结果。让我读 resource-saturation skill 然后向 Director 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para"
}
```

</details>

---

## Round 2

26 recorded events

### User

_source line 32 · 2026-05-16T14:50:52.555477+00:00_

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
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T14:51:02.180535+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__load_project_config",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__load_project_config",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T14:51:02.180881+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T14:51:05.593923+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-16T14:51:06.045740+00:00_

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
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T14:51:06.547793+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "report.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "report.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T14:51:07.054955+00:00_

Error: result (362,519 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-9f9278f8/bec0cc24-be03-4a77-ae6c-413e5dfada58/tool-results/mcp-agent-ml-research-read_registry-1778943066668.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-9f9278f8/bec0cc24-be03-4a77-ae6c-413e5dfada58/tool-results/mcp-agent-ml-research-read_registry-1778943066668.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1461
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T14:51:07.055461+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T14:51:07.557456+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "status": "running"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T14:51:07.909198+00:00_

called mcp__agent-ml-research__load_project_config

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config</summary>

```json
{
  "project_name": "contamcal-irt-calibration",
  "section": "execution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__load_project_config",
  "tool_args": {
    "project_name": "contamcal-irt-calibration",
    "section": "execution"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T14:51:09.566489+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 1, \"results\": [{\"exp_id\": \"exp_001_eval_15B_instruct\", \"success\": true, \"actions\": [\"Job still running (pid=782625)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 3520
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-16T14:51:09.567104+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_001_eval_05B_instruct | — | — | — | — |\\n| exp_006_pooled_irt_rrf_n25_v2 | — | — | — | — |\\n| exp_006_mmlu_domain_gamma_n24_v4 | — | — | — | — |\\n\\n## 待处理\\n- signals_05B_s123_batch（准备中）\\n- exp006_pooled_rrf_irt_05b_15b_v2（准备中）\\n- exp_001_eval_3B_d000_s42_a32_aligned: 3B d000 s42 alpha=32 aligned eval. Uses D076-retrained checkpoint (lr=5e-5). 0% contamination baseline for s42 IRT pool. Prerequisite for para_aligned eval and signals.（准备中）\\n- exp_001_sft_3B_d000_v4（准备中）\\n- exp_001_sft_3B_d000_s42（准备中）\\n- exp_001_eval_3B_d005_s123（准备中）\\n- exp_001_eval_3B_d025_s123（准备中）\\n- exp_001_eval_3B_d005_s42_aligned_v2（准备中）\\n- exp_001_sft_15B_d025_s123（准备中）\\n- exp006-gsm8k-d024-delta（准备中）\\n- …另有 11 项\\n\\n## 近期结论\\n- **exp_001_eval_llama32_3B_d000_s42** (killed): —\\n- **exp_003_rrf_full_n25_latest** (success): —\\n- **signals_05B_s123_v2** (success): —\\n\\n## 趋势\\n成功 142 / 负向 4 / 失败 49 / 共 206\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-21977: 无 GPU 信息\\n\\n## 告警\\n- exp_001_eval_05B_d000_s42: 训练失败 — unknown\\n- exp_001_eval_05B_d100: 训练失败 — unknown\\n- exp_001_eval_05B_d100_v2: 训练失败 — unknown\\n- exp_001_eval_15B_d000_s42: 训练失败 — unknown\\n- exp_001_sft_100pct_05B: 训练失败 — unknown\\n- exp_001_sft_d005_05B: 已被终止 — unknown\\n- exp_001_sft_d005_05B_v2: 训练失败 — unknown\\n- exp_001_sft_d100_15B: 训练失败 — unknown\\n- exp_004_sim_sweep: 训练失败 — unknown\\n- exp_005_noise_prop: 训练失败 — unknown\\n- exp_005_noise_prop_v2: 训练失败 — unknown\\n- exp_005_noise_prop_v3: 训练失败 — unknown\\n- exp_001_sft_d025_05B: 训练失败 — unknown\\n- exp_001_sft_d025_05B_v2: 训练失败 — unknown\\n- exp_004_sim_sweep_v2: 训练失败 — unknown\\n- exp_001_eval_05B_aligned_batch: 训练失
…[truncated 2181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 3019
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T14:51:09.618830+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-16 10:26 UTC | 更新原因: Reviewer critical: 修正d005 false failure + D108措辞降级为domain heterogeneity evidence + GPU状态同步\\n\\n## 核心方向\\nContamCal：contamination-augmented IRT with per-benchmark γ_k → domain heterogeneity evidence (Simpson's paradox, D108)。详见 paper_framing.md。\\n\\n## 投稿目标\\n**EMNLP 2026 ARR May 25**（距今 9 天）\\n\\n## 当前进展\\n- **阶段**: Research (MVP 2026-05-13 通过) + 审稿进行中\\n- **D108 发现**: MMLU 57 subjects → 8 cognitive domains，aggregate γ≈0 masks domain heterogeneity (5 domains significant, γ range: -0.55 to +1.34)。PPP=0 in 4/5 domains → claim 基于 pattern/ranking，非绝对值。N=24 重跑确认前为\\\"evidence of heterogeneity\\\"\\n- **3B s42 signals**: d000 ✅ d005 ✅ d025 ✅ d100 🔄(cuda:1, ~35min)。d100 完成后全齐 → RRF\\n- **0.5B s123**: 全部完成 ✅\\n- **1.5B s123**: d025 running (cuda:0), d100 running (cuda:2)。完成后全量 RRF (N≥16+)\\n- **Scope expansion (D106)**: Llama 代码+模型就绪 | RL observational 3B-Instruct eval running (cuda:3) | 7B 待云GPU\\n\\n## GPU 实时占用 (6× RTX 4090D, cqa1-21977)\\n| GPU | 任务 | 预计完成 |\\n|-----|------|---------|\\n| cuda:0 | signals_15B_s123_batch (d025) | ~2h |\\n| cuda:1 | signals_3B_d100_a32_s42 | ~35min |\\n| cuda:2 | signals_15B_d100_s123 | ~3h |\\n| cuda:3 | eval_3B_instruct_aligned_para (P0-C) | ~1h |\\n| cuda:4 | **待分配 → Llama-3.2-3B d000 SFT** | 指令已发 |\\n| cuda:5 | signals_05B_s123_v2 (d100) | ~2.5h |\\n\\n## Critical Path (EMNLP T-9)\\n```\\n[Now]     cuda:1 d100 ~35min → 3B s42 全齐 → RRF 聚合 (CPU)\\n          cuda:4 → Llama-3.2-3B d000 SFT 启动\\n          cuda:3 3B-Instruct eval ~1h → 0.5B/1.5B-Instruct eval\\n[Day 1]   pooled IRT (N≥16+) — 论文核心 γ 数字\\n          MMLU domain gamma N=24 (含 3B) — 确认 heterogeneity 是否 scale-dependent\\n          Llama d000 SFT + eval\\n[Day 2]   Llama d005/d025/d100 SFT + eval + signals\\n          scale-st
…[truncated 2192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 2563
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-16T14:51:09.719831+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 2162
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T14:51:09.720364+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"contamcal-irt-calibration\", \"section\": \"execution\", \"config\": {\"execution\": {\"gpu_ids\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\", \"cuda:4\", \"cuda:5\"], \"project_path\": \"/root/contamcal-irt-calibration\", \"servers\": [\"cqa1-21977\"]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 1811
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T14:51:16.241953+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['exp_id', 'status', 'hypothesis', 'spec']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['exp_id', 'status', 'hypothesis', 'spec']"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T14:51:17.096283+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_001_eval_05B_instruct\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python3 /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/models/Qwen/Qwen2.5-0.5B-Instruct-hf --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct/ --mc-format aligned --instruct --benchmarks mmlu gsm8k humaneval\", \"server\": \"cqa1-21977\", \"data_path\": \"mmlu+gsm8k+humaneval\", \"data_count\": 0, \"model_name\": \"Qwen2.5-0.5B-Instruct\", \"seed\": 42, \"eval_data\": \"mmlu gsm8k humaneval\", \"hypothesis\": \"0.5B-Instruct baseline eval (RL observational claim). Generation-based MCQ with chat template.\"}}, \"exp_006_pooled_irt_rrf_n25_v2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python3 /root/contamcal-irt-calibration/exp006/run_pooled_rrf_irt.py --exposure-file /root/autodl-tmp/exp003/rrf_full_n_latest/exposure_scores.json --output-dir /root/autodl-tmp/exp006/pooled_irt_rrf_n25_v2 --model-type 4pl_gamma --benchmarks mmlu gsm8k arc_challenge --chains 4 --warmup 1000 --samples 1000\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp003/rrf_full_n_latest/exposure_scores.json\", \"data_count\": 25, \"model_name\": \"4pl_gamma_pooled\", \"seed\": 42}}, \"exp_006_mmlu_domain_gamma_n24_v4\": {\"status\": \"RUNNING\", \"spec\": {\"hypothesis\": \"D108 v4: rerun 4 MMLU domains with correct N=24 script\", \"plan_id\": \"D108\", \"type\": \"analysis\", \"parent\": \"exp_006_mmlu_domain_gamma_n24\", \"model_name\": \"2PL+gamma (Stan)\", \"seed\": \"Stan default (4 chains)\", \"data_path\": \"/root/autodl-tmp/exp003/rrf_all_scales/exposure_scores.json\", \"data_count\": \"24 respondents x 4 MMLU domains\", \"command\": \"python run_mmlu_domain_gamma_n24.py --domains Humanities Social_Sciences Business_Law Other --output-dir /root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24/\", \"server\": \"cqa1-21977\", \"gpu\": \"CPU\", \
…[truncated 1063 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 854
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T14:51:17.147063+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": "{'status': 'PREPARING'}",
  "fields": "['exp_id', 'status', 'hypothesis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "filters": "{'status': 'PREPARING'}",
    "fields": "['exp_id', 'status', 'hypothesis']"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T14:51:17.950501+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"signals_05B_s123_batch\": {\"status\": \"PREPARING\"}, \"exp006_pooled_rrf_irt_05b_15b_v2\": {\"status\": \"PREPARING\"}, \"exp_001_eval_3B_d000_s42_a32_aligned\": {\"status\": \"PREPARING\", \"hypothesis\": \"3B d000 s42 alpha=32 aligned eval. Uses D076-retrained checkpoint (lr=5e-5). 0% contamination baseline for s42 IRT pool. Prerequisite for para_aligned eval and signals.\"}, \"exp_001_sft_3B_d000_v4\": {\"status\": \"PREPARING\"}, \"exp_001_sft_3B_d000_s42\": {\"status\": \"PREPARING\"}, \"exp_001_eval_3B_d005_s123\": {\"status\": \"PREPARING\"}, \"exp_001_eval_3B_d025_s123\": {\"status\": \"PREPARING\"}, \"exp_001_eval_3B_d005_s42_aligned_v2\": {\"status\": \"PREPARING\"}, \"exp_001_sft_15B_d025_s123\": {\"status\": \"PREPARING\"}, \"exp006-gsm8k-d024-delta\": {\"status\": \"PREPARING\"}, \"exp_006_irt_05B_v2\": {\"status\": \"PREPARING\", \"hypothesis\": \"Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 items + ADVI robustness check. Fixes v1 issues: aligned-only, signal-derived exposure, --max-items.\"}, \"exp_001_eval_05B_d100_aligned_v2\": {\"status\": \"PREPARING\"}, \"exp_001_eval_05B_d000_s42_v6\": {\"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d100_v6\": {\"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d100_v4\": {\"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d000_s42_v4\": {\"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d000_s42_v2\": {\"status\": \"PREPARING\"}, \"exp_001_eval_05B_d100_v3\": {\"hypothesis\": \"100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 contamination score inflation\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d
…[truncated 591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 803
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T14:51:17.951050+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T14:51:18.051934+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\", \"content\": \"# Pipeline Readiness Report — RRF Aggregation + IRT Fitting\\n**Date**: 2026-05-16  \\n**Server**: cqa1-21977\\n\\n---\\n\\n## 1. RRF Aggregation Code (exp003) — READY\\n\\n`/root/contamcal-irt-calibration/exp003/rrf_aggregation.py`\\n\\n- **Signal selection**: `SIGNAL_KEYS = [\\\"s1_embedding\\\", \\\"s2_minkpp\\\", \\\"s4_selfcritique\\\"]` — s3_constat correctly excluded per D098\\n- **Input**: `/root/autodl-tmp/exp002/signals/`\\n- **ALPHA16_BLOCKLIST** in place — skips all 5 deprecated alpha=16 3B dirs\\n- **Output**: configurable `--output-dir`, supports `--generate-exposure` for IRT-ready format\\n- **Known issue**: exposure_scores.json has 25 entries (2 duplicates from _a32_s42 vs _s42_a32 naming). Worker cleaning up.\\n\\n---\\n\\n## 2. Signals Data Matrix\\n\\n### 2.1 Complete (s1+s2+s4 × mmlu+gsm8k+arc_challenge)\\n\\n| # | Directory | Notes |\\n|---|-----------|-------|\\n| 1 | Qwen2.5-0.5B_d000_s42 | All 3 benchmarks MERGED |\\n| 2 | Qwen2.5-0.5B_d005_s42 | All 3 benchmarks MERGED |\\n| 3 | Qwen2.5-0.5B_d025_s42 | All 3 benchmarks MERGED |\\n| 4 | Qwen2.5-0.5B_d100_s42 | All 3 benchmarks MERGED |\\n| 5 | Qwen2.5-1.5B_d000_s42 | All 3 benchmarks MERGED |\\n| 6 | Qwen2.5-1.5B_d005_s42 | All 3 benchmarks MERGED |\\n| 7 | Qwen2.5-1.5B_d025_s42 | All 3 benchmarks MERGED |\\n| 8 | Qwen2.5-1.5B_d100_s42 | All 3 benchmarks MERGED |\\n| 9 | Qwen2.5-3B_d025_v3_s42 | s1+s2+s4 all 3 benchmarks |\\n| 10 | Qwen2.5-3B_d005_s123 | All 3 benchmarks MERGED |\\n| 11 | Qwen2.5-3B_d025_s123 | gsm8k/arc MERGED; mmlu s1+s2+s4 present |\\n| 12 | Qwen2.5-3B_d005_a32_s42 | All 3 benchmarks MERGED |\\n| 13 | Qwen2.5-3B_d000_a32_s42 | All 3 benchmarks (confirmed 2026-05-16) |\\n| 14 | Qwen2.5-3B_d100_a32_s42 | All 3 benchmarks (confirmed 2026-05-16 ~10:47) |\\n\\n**Total complete: 14 model dirs (3B s42 alpha=32 全齐: d0
…[truncated 4502 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T14:51:22.670677+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__poll_cron",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__poll_cron",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T14:51:22.821765+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T14:51:26.684260+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__list_workers",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__list_workers",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T14:51:26.885275+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-16T14:52:40.837490+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0-5（cqa1-21977），6 卡全分配给本项目，无跨项目共享
- 3B 实验必须用 alpha=32（alpha=16 已 blocklist，RRF 代码 ALPHA16_BLOCKLIST 自动跳过 5 个 deprecated 目录）
- MMLU domain gamma claim 已降级为 "domain heterogeneity evidence"（D108），禁止用 "significant gamma" 措辞——PPP=0 in 4/5 domains，只能基于 pattern/ranking claim
- D110: scale-stratified IRT 已判定 negative（N=6-8 per scale 不够），不要再尝试
- D112: Medical domain PPP=1.0 model misfit，已排除；D114: domain gamma claim scoped to STEM-only
- submit_training_job 的 command 必须自带环境激活（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），不要假设 .venv 存在
- s3_constat 信号已按 D098 排除，SIGNAL_KEYS = [s1_embedding, s2_minkpp, s4_selfcritique]

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-21977，6× RTX 4090D
- **工作目录**: `/root/contamcal-irt-calibration`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境）
- **模型路径**: `/root/autodl-tmp/models/Qwen/` 下有 0.5B/1.5B/3B base+instruct；Llama-3.2-3B 在 `/root/autodl-tmp/models/`
- **数据/产出**: `/root/autodl-tmp/exp001/`(eval), `/root/autodl-tmp/exp002/signals/`(signals), `/root/autodl-tmp/exp003/`(RRF), `/root/autodl-tmp/exp006/`(IRT)
- **HF cache**: `/root/autodl-tmp/.hf_cache`
- **Stan models**: `/root/contamcal-irt-calibration/stan_models/`（5 个已编译）
- **活跃进程**:
  - PID 782625 — exp_001_eval_15B_instruct (cuda:5, cron 监控中)
  - PID 789935 — exp_006_mmlu_domain_gamma_n24_v4 (CPU, D108 N=24 rerun)
  - exp_001_eval_05B_instruct (cuda:2, registry RUNNING, 无 PID 记录)
  - exp_006_pooled_irt_rrf_n25_v2 (CPU, pooled IRT N=25)
- **Worker 池**: 0 running（全部已完成/回调处理完毕）

### 3. 📊 当前状态
**刚做完**: 本 session 刚启动，执行了 session-start 初始化（reconcile crons + registry 同步）。上一轮 session 完成了：D108 MMLU domain gamma 初步分析（Simpson's paradox confirmed）、sim_sweep_v7 Claim 3 identifiability 验证、scope expansion D106 批准（Llama 跨族）、3B s42 全 4 dosage signals 完成、pooled IRT N=23 完成。

**RUNNING (4)**:
1. `exp_001_eval_15B_instruct` — 1.5B-Instruct eval (cuda:5, PID 782625, cron active)
2. `exp_001_eval_05B_instruct` — 0.5B-Instruct eval (cuda:2)
3. `exp_006_mmlu_domain_gamma_n24_v4` — D108 N=24 rerun for 4 non-STEM domains (CPU)
4. `exp_006_pooled_irt_rrf_n25_v2` — Pooled 4PL+γ IRT with N=25 (CPU)

**PREPARING (21)**: 大量 legacy 实验堆积（早期失败的 v2-v6 重试），实际有意义的待做项见第 4 节。

**等待中**:
- 无活跃 Worker
- 1 个 cron 监控 exp_001_eval_15B_instruct
- GPU 分配表（来自 memory.md 快照，可能已过时——下一个 session 需 SSH 验证）: cuda:0(1.5B s123 signals), cuda:1(0.5B d100_s123), cuda:2(1.5B d100_s123 或 0.5B-Instruct eval), cuda:3(3B-Instruct eval v2), cuda:4(Llama d000 SFT), cuda:5(1.5B-Instruct eval)

### 4. 📋 待办（条件触发式）
- **exp_001_eval_15B_instruct cron 回调到达** → 检查 MMLU/GSM8K/ARC/HumanEval 指标 → update_registry → 若 MMLU≥0.65+HumanEval≥0.50 则启动 0.5B-Instruct eval（已预批准）
- **cuda:3 释放（3B-Instruct eval v2 完成）** → 启动 1.5B-Instruct eval（Director 预批准）
- **cuda:0 释放（1.5B s123 batch 完成）** → 启动 3B d000_s123 signals（Director 预批准，N 扩展关键路径）
- **exp_006_mmlu_domain_gamma_n24_v4 完成** → 分析 4 non-STEM domains γ → 确认 heterogeneity 是否 scale-dependent → 汇报 Director → 更新 paper_framing.md D108 措辞
- **exp_006_pooled_irt_rrf_n25_v2 完成** → 核心论文 γ 数字确定 → update_registry + report.md
- **1.5B s123 全部完成** → 全量 RRF re-run (N≥27+) → 最终 pooled IRT
- **Llama d000 SFT 完成 (cuda:4)** → eval + signals → 跨模型族验证（D106 scope expansion）
- **7B 云 GPU A100-80G 批准** → 启动 7B 实验（已向 Manager 申请，pending）

### 5. 🎯 战略上下文
**投稿目标**: EMNLP 2026 ARR May 25（距今 9 天）。Day 3-5 需 full draft，Day 7-9 提交。

**核心结论链**:
- **D109**: Aggregate pooled IRT (N=23, 2PL+γ) confirms 3 benchmarks all positive γ → contamination upward bias
- **D108**: MMLU aggregate γ≈0 masks domain heterogeneity (Simpson's paradox)。但 PPP=0 in 4/5 domains → claim 只能基于 pattern/ranking，非绝对值。N=24 v4 正在 rerun 验证
- **D107**: Claim 3 (identifiability) GO，sim_sweep 11/12 条件充分
- **D106**: Scope expansion 批准——Llama-3.2-3B + RL observational (Instruct) + MMLU domain
- **D110**: Scale-stratified IRT NEGATIVE（N 太小）——不再追
- **D114**: Domain gamma claim scoped to STEM-only

**易错点**:
1. GPU 实际状态可能与 memory.md 快照不同（上个 session 结束后有进程可能已完成）——**第一件事 SSH 验证 nvidia-smi**
2. 不要把 GC4-par 和 GC4-seq 直接对比；不要把 alpha=16 和 alpha=32 的 3B 结果混用
3. PREPARING 里 21 个实验大部分是早期失败的 v2-v6 zombie entries，不要试图 revive 它们——关注 ROADMAP 近期任务列表
4. GSM8K γ≈0 是因为 0.5B/1.5B dose-response flat，3B 不 flat（scale-dependent）——论文要区分说明
5. Instruct eval 必须用 --instruct 模式 + chat_template，否则 MMLU 0.509 HumanEval 0.000（D113 教训）
6. ARC IRT PPP 结构性低（N:items = 1:146），N≥16 后仍可能 marginal——论文需 caveat
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:exp_001_eval_3B_instruct_aligned_para"
}
```

</details>

---
