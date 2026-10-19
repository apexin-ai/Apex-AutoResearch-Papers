# cron hook eval adaptive k spatial p25 seed43 20260521T025225 868468

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 2
- **Tool calls:** 13
- **Original source:** `logs/chats/archive/cron_hook_eval-adaptive-k-spatial-p25-seed43_20260521T025225_868468.jsonl`
- **Structured JSON:** [`b4a1c53ffba10076e859.json`](../../sessions/b4/b4a1c53ffba10076e859.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-20T10:47:42.396142+00:00_

[CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。
详情: Process exited cleanly, W&B data available

- exp_id: eval-adaptive-k-spatial-p25-seed43
- project: acr-vla-conformal-refinement
- server: bjb1-32546
- log_path: ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p25-seed43.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "source": "cron:hook"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-20T10:47:55.741183+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__save_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__fetch_wandb_metrics,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__save_project_file",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-20T10:47:55.793430+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T10:47:58.659491+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T10:47:59.162885+00:00_

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
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T10:47:59.617457+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "report.md"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T10:48:00.169175+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T10:48:00.320150+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "status": "running"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T10:48:01.487762+00:00_

Error: result (663,703 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-d057c409/9e21a2d4-3e84-4792-bd34-7c6fc082a80e/tool-results/mcp-agent-ml-research-read_registry-1779274081410.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-d057c409/9e21a2d4-3e84-4792-bd34-7c6fc082a80e/tool-results/mcp-agent-ml-research-read_registry-1779274081410.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-d057c409/9e21a2d4-3e84-4792-bd34-7c6fc082a80e/tool-results/mcp-agent-ml-research-read_registry-1779274081410.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2828
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T10:49:05.358484+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 4, \"results\": [{\"exp_id\": \"eval-adaptive-k-spatial-p50-seed42\", \"success\": true, \"actions\": [\"Job still running (pid=681823)\"]}, {\"exp_id\": \"eval-crm-object-k20-seed44\", \"success\": true, \"actions\": [\"Sentinel EXIT_CODE=0 → Registry → ANALYZING\", \"Cron deleted\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=278354)\"]}, {\"exp_id\": \"eval-obs-only-object-norm003-seed44\", \"success\": true, \"actions\": [\"Job still running (pid=279014)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 66195
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T10:49:05.424069+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-obs-only-object-norm003-seed44 | CRM obs_only ε=0.03 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε. | — | — | — |\\n\\n## 待处理\\n- eval-argmin-object-seed48（准备中）\\n- eval-obs-only-object-norm02-seed43-r3（准备中）\\n- …另有 42 项\\n\\n## 近期结论\\n- **eval-obs-only-object-norm005-seed44** (success): CRM obs_only ε=0.05 on Object seed44. Low-norm multi-seed supplement (plan_500): strengthens Figure 2 error bars at small ε.\\n\\n## 趋势\\n成功 224 / 负向 32 / 失败 47 / 共 388\\nsuccess_rate: 12 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 无 GPU 信息\\nbjb1-32546: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-28827: 空闲 cuda:0, cuda:1, cuda:2, cuda:3, cuda:4, cuda:5\\nbjb2-40593: 无 GPU 信息\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- precompute-v2-shard0: 已被终止 — unknown\\n- precompute-v2-shard1: 已被终止 — unknown\\n- precompute-v2-shard2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- precompute-v3-shard0: 已被终止 — unknown\\n- precompute-v3-shard1: 已被终止 — unknown\\n- precompute-v3-shard2: 已被终止 — unknown\\n- eval-spatial-v4-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5-full: 已被终止 — unknown\\n- crm-train-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v2: 已被终止 — unknown\\n- eval-acr-spatial-v1: 已被终止 — unknown\\n- crm-train-a3-obs-only: 已被终止 — unknown\\n- eval-acr-vla-spatial-v1: 已被终止 — unknown\\n- eval-spatial-v6-full: 已被终止 — unknown
…[truncated 5098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 65806
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T10:49:05.439482+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-20 06:17 UTC | 更新原因: Fix Long OOD data to match D081, update RUNNING section per Reviewer observation\\n\\n> 详见 paper_framing.md（D077: Adaptive K 升级为核心贡献）\\n\\n## 核心方向\\n**Adaptive inference-time compute for frozen VLAs** — K=2 L2 distance 作为不确定性信号，自适应决定每步推理次数。CRM correction>selection 分析作为支撑。\\n\\n## 投稿目标\\n**CoRL 2026** DDL **2026-05-29**。剩余 ~9 天。\\n\\n## D077 方向转换（用户硬要求）\\n- Adaptive K = 论文**核心贡献**（方法）\\n- K=10 分析降为 supporting evidence\\n\\n## 信号候选 (CLOSED)\\n| 信号 | ρ vs K10_var | 结论 |\\n|------|-------------|------|\\n| **K=2 L2 distance** | **0.9979** | **✅ GO — 唯一可用信号** |\\n| CRM correction magnitude | 0.1523 | ❌ NO-GO (D079) |\\n| FMVD | 0.0825 | ❌ NO-GO |\\n\\n## Adaptive K Sweep (Object) — 12/12 DONE ✅\\n| 阈值 | seeds | SR (mean) | avg_K | fast_path% | vs K=10 |\\n|------|-------|-----------|-------|-----------|---------|\\n| P90 | 3/3 ✅ | 13.3% | ~2.6 | ~93% | 74% |\\n| P75 | 3/3 ✅ | 13.7% | ~3.1 | ~87% | 79% |\\n| **P50** | **3/3 ✅** | **15.3%** | **~3.8** | **~77%** | **~91%** |\\n| P25 | 3/3 ✅ | 14.3% | ~4.8 | ~65% | ~85% |\\n\\n**P50 = Pareto 最优 (D078)**。\\n\\n## RUNNING 实验\\n- bjb2-40593: Spatial Adaptive K P50 seed42 (rollout 中)\\n- bjb1-18228: Long VLA-only seed54, Long CRM seed53, Spatial VLA-only seed53\\n- bjb1-32546: Long CRM seed54, Spatial VLA-only seed54\\n- 更多部署中（Agent 处理综合指令）\\n\\n## 待部署\\n1. **Spatial Adaptive K P50 seed43, seed44**\\n2. **Random Selection baseline seed42, seed44** (plan_600)\\n3. **CRM Object K=10 norm02 seed42** (Table 1 n=6→n=7)\\n4. **fig3_kvalue 重新生成**\\n\\n## 论文 CRITICAL 待解决\\n1. **evaluate.py 推理模式确认** — Agent P0\\n2. **Spatial CRM K=10 n=8 溯源** — registry 只有 n=7, Agent 调查中\\n3. **OOD Long/Goal 数据全量更新** — Paper Agent 处理中\\n4. **P25 n=3 更新** — Paper Agent 处理中\\n\\n## 核心实验结果 (LOCKED,
…[truncated 2536 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 65270
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T10:49:05.820058+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_mass-deploy_multi-seed-supplement_20260520T104205\", \"task_type\": \"mass-deploy:multi-seed-supplement\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-20T10:42:05.434737+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 65499
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T10:49:16.318450+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-d057c409/9e21a2d4-3e84-4792-bd34-7c6fc082a80e/tool-results/mcp-agent-ml-research-read_registry-1779274081410.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nreg = json.loads(data['result'])\nexps = reg['data']['experiments']\ntargets = ['eval-adaptive-k-spatial-p25-seed43', 'eval-crm-object-k20-seed44']\nfor t in targets:\n    if t in exps:\n        print(f'=== {t} ===')\n        print(json.dumps(exps[t], indent=2, default=str))\n    else:\n        print(f'{t}: NOT FOUND')\n\"\n",
  "description": "Extract target experiments from registry dump"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-d057c409/9e21a2d4-3e84-4792-bd34-7c6fc082a80e/tool-results/mcp-agent-ml-research-read_registry-1779274081410.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nreg = json.loads(data['result'])\nexps = reg['data']['experiments']\ntargets = ['eval-adaptive-k-spatial-p25-seed43', 'eval-crm-object-k20-seed44']\nfor t in targets:\n    if t in exps:\n        print(f'=== {t} ===')\n        print(json.dumps(exps[t], indent=2, default=str))\n    else:\n        print(f'{t}: NOT FOUND')\n\"\n",
    "description": "Extract target experiments from registry dump"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T10:49:17.105920+00:00_

=== eval-adaptive-k-spatial-p25-seed43 ===
{
  "status": "ANALYZING",
  "retry_count": 0,
  "created_at": "2026-05-20T08:19:55.884Z",
  "updated_at": "2026-05-20T10:47:33.917Z",
  "hypothesis": "Adaptive K with \u03c4=P25 (0.054959, Object-calibrated) on LIBERO-Spatial seed43. Second seed for cross-benchmark P25 threshold sweep.",
  "spec": {
    "command": "bash -c \"... python -u src/evaluate.py --mode adaptive_k --adaptive_threshold 0.054959 --k_full 10 --benchmark spatial --seed 43 ...\"",
    "server": "bjb1-32546",
    "gpu": [
      "cuda:2"
    ],
    "pid": "314014",
    "log_path": "~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p25-seed43.log",
    "submitted_at": "2026-05-20T08:21:10.027Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "data_path": "LIBERO-Spatial",
    "data_count": "100 (10 tasks x 10 rollouts)",
    "model_name": "SmolVLA + CRM obs_only (adaptive_k P25)",
    "seed": 43,
    "checkpoint_source": "/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt",
    "eval_data": "LIBERO-Spatial (10 tasks x 10 rollouts)",
    "checkpoint_path": "N/A (eval only)"
  },
  "reproduce": {
    "finished_at": "2026-05-20T10:47:32.130Z"
  },
  "extra": {
    "hook_events": [
      {
        "event": "on_complete",
        "action": "agent",
        "ts": "2026-05-20T10:47:45.581311+00:00"
      }
    ]
  }
}
=== eval-crm-object-k20-seed44 ===
{
  "status": "RUNNING",
  "retry_count": 0,
  "created_at": "2026-05-20T08:47:49.745Z",
  "updated_at": "2026-05-20T10:32:59.666Z",
  "hypothesis": "CRM obs_only K=20 on Object seed44. K-value sweep third seed (plan_601): tests K=20 vs K=10 compute tradeoff.",
  "spec": {
    "command": "bash -c \"... python -u src/evaluate.py --mode crm_obs_only --benchmark object --seed 44 --n_rollouts 10 --K 20 --max_correction_norm 0.2 ...\"",
    "server": "bjb2-28827",
    "gpu": [
      "cuda:3"
    ],
    "pid": "278078",
    "log_path": "~/runs/acr-vla-co
…[truncated 534 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "Bash",
  "elapsed_ms": 787
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T10:49:57.558467+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "analyze:eval-adaptive-k-spatial-p25-seed43",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：分析实验 eval-adaptive-k-spatial-p25-seed43 的结果\n\n### 背景\n这是 Adaptive K 方法在 LIBERO-Spatial benchmark 上用 P25 阈值 (τ=0.054959) 的第二个 seed (seed43) 评估实验。Adaptive K 是论文的核心贡献——用 K=2 L2 distance 作为不确定性信号，自适应决定每步推理次数。\n\nObject benchmark 上 P25 的结果：SR 14.3%, avg_K ~4.8, fast_path ~65%, vs K=10 ~85%。\n\n### 实验信息\n- server: bjb1-32546\n- log_path: ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p25-seed43.log\n- 模式: adaptive_k, threshold=0.054959, k_full=10, benchmark=spatial, seed=43\n\n### 你要做的\n1. SSH 到 bjb1-32546，用 ssh_read_only 读取完整 log 文件\n2. 提取以下关键指标：\n   - Overall success rate (SR%)\n   - Per-task success rates (每个 task 的成功率)\n   - Average K (平均推理次数)\n   - Fast path percentage (K=1 的比例)\n   - 与 K=10 baseline 的对比（如果 log 中有）\n   - 总 rollout 数和任何错误/警告\n3. 如果 log 里有 W&B run ID，也记录下来\n4. 检查是否有任何异常（如 NaN、crash、incomplete rollouts）\n\n### 产出\n用 update_registry 更新实验：\n- 如果成功完成所有 rollout：status=DONE, conclusion=success, metrics={sr, avg_k, fast_path_pct, per_task_sr}\n- 如果有问题：status=DONE, conclusion=failed, 并说明原因\n\n最后输出一段简洁的分析摘要，包含所有提取的指标。\n",
  "tool_groups": "['ssh', 'registry']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analyze:eval-adaptive-k-spatial-p25-seed43",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：分析实验 eval-adaptive-k-spatial-p25-seed43 的结果\n\n### 背景\n这是 Adaptive K 方法在 LIBERO-Spatial benchmark 上用 P25 阈值 (τ=0.054959) 的第二个 seed (seed43) 评估实验。Adaptive K 是论文的核心贡献——用 K=2 L2 distance 作为不确定性信号，自适应决定每步推理次数。\n\nObject benchmark 上 P25 的结果：SR 14.3%, avg_K ~4.8, fast_path ~65%, vs K=10 ~85%。\n\n### 实验信息\n- server: bjb1-32546\n- log_path: ~/runs/acr-vla-conformal-refinement/eval-adaptive-k-spatial-p25-seed43.log\n- 模式: adaptive_k, threshold=0.054959, k_full=10, benchmark=spatial, seed=43\n\n### 你要做的\n1. SSH 到 bjb1-32546，用 ssh_read_only 读取完整 log 文件\n2. 提取以下关键指标：\n   - Overall success rate (SR%)\n   - Per-task success rates (每个 task 的成功率)\n   - Average K (平均推理次数)\n   - Fast path percentage (K=1 的比例)\n   - 与 K=10 baseline 的对比（如果 log 中有）\n   - 总 rollout 数和任何错误/警告\n3. 如果 log 里有 W&B run ID，也记录下来\n4. 检查是否有任何异常（如 NaN、crash、incomplete rollouts）\n\n### 产出\n用 update_registry 更新实验：\n- 如果成功完成所有 rollout：status=DONE, conclusion=success, metrics={sr, avg_k, fast_path_pct, per_task_sr}\n- 如果有问题：status=DONE, conclusion=failed, 并说明原因\n\n最后输出一段简洁的分析摘要，包含所有提取的指标。\n",
    "tool_groups": "['ssh', 'registry']"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T10:50:02.943227+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "analyze:eval-crm-object-k20-seed44",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：分析实验 eval-crm-object-k20-seed44 的结果\n\n### 背景\n这是 CRM obs_only K=20 在 LIBERO-Object benchmark 上的第三个 seed (seed44) 评估实验。属于 K-value sweep (plan_601)，测试 K=20 vs K=10 的 compute tradeoff。\n\n已知 Object CRM K=10 (norm02) 的结果：16.8%±1.8% (n=6)。\n\n### 实验信息\n- server: bjb2-28827\n- log_path: ~/runs/acr-vla-conformal-refinement/eval-crm-object-k20-seed44.log\n- 模式: crm_obs_only, benchmark=object, seed=44, K=20, max_correction_norm=0.2\n\n### 你要做的\n1. SSH 到 bjb2-28827，用 ssh_read_only 读取完整 log 文件\n2. 提取以下关键指标：\n   - Overall success rate (SR%)\n   - Per-task success rates\n   - 总 rollout 数和任何错误/警告\n3. 如果 log 里有 W&B run ID，也记录下来\n4. 检查是否有任何异常（如 NaN、crash、incomplete rollouts）\n\n### 产出\n用 update_registry 更新实验：\n- 如果成功完成所有 rollout：status=DONE, conclusion=success, metrics={sr, per_task_sr}\n- 如果有问题：status=DONE, conclusion=failed, 并说明原因\n\n最后输出一段简洁的分析摘要，包含所有提取的指标。\n",
  "tool_groups": "['ssh', 'registry']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "analyze:eval-crm-object-k20-seed44",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：分析实验 eval-crm-object-k20-seed44 的结果\n\n### 背景\n这是 CRM obs_only K=20 在 LIBERO-Object benchmark 上的第三个 seed (seed44) 评估实验。属于 K-value sweep (plan_601)，测试 K=20 vs K=10 的 compute tradeoff。\n\n已知 Object CRM K=10 (norm02) 的结果：16.8%±1.8% (n=6)。\n\n### 实验信息\n- server: bjb2-28827\n- log_path: ~/runs/acr-vla-conformal-refinement/eval-crm-object-k20-seed44.log\n- 模式: crm_obs_only, benchmark=object, seed=44, K=20, max_correction_norm=0.2\n\n### 你要做的\n1. SSH 到 bjb2-28827，用 ssh_read_only 读取完整 log 文件\n2. 提取以下关键指标：\n   - Overall success rate (SR%)\n   - Per-task success rates\n   - 总 rollout 数和任何错误/警告\n3. 如果 log 里有 W&B run ID，也记录下来\n4. 检查是否有任何异常（如 NaN、crash、incomplete rollouts）\n\n### 产出\n用 update_registry 更新实验：\n- 如果成功完成所有 rollout：status=DONE, conclusion=success, metrics={sr, per_task_sr}\n- 如果有问题：status=DONE, conclusion=failed, 并说明原因\n\n最后输出一段简洁的分析摘要，包含所有提取的指标。\n",
    "tool_groups": "['ssh', 'registry']"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T10:50:03.840596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T10:50:04.239905+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analyze_eval-adaptive-k-spatial-p25-seed43_20260520T105000\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-adaptive-k-spatial-p25-seed43_20260520T105000.log\", \"setup_data\": {}, \"message\": \"Worker worker_analyze_eval-adaptive-k-spatial-p25-seed43_20260520T105000 started. Use get_worker_status('worker_analyze_eval-adaptive-k-spatial-p25-seed43_20260520T105000') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 6681
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T10:50:08.706697+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analyze_eval-crm-object-k20-seed44_20260520T105005\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_analyze_eval-crm-object-k20-seed44_20260520T105005.log\", \"setup_data\": {}, \"message\": \"Worker worker_analyze_eval-crm-object-k20-seed44_20260520T105005 started. Use get_worker_status('worker_analyze_eval-crm-object-k20-seed44_20260520T105005') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 5763
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T10:50:08.766996+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_d057c409.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "Read",
  "elapsed_ms": 4926
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T10:50:11.985251+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T10:50:12.170121+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "Glob",
  "elapsed_ms": 184
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T10:50:14.694003+00:00_

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
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
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

_source line 25 · 2026-05-20T10:50:16.269560+00:00_

/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "Glob",
  "elapsed_ms": 1575
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T10:50:23.257343+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T10:50:23.309501+00:00_

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
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-20T10:50:41.984805+00:00_

已派 2 个分析 Worker。等待回调后更新 registry 并汇报 Director。

当前状态概览：
- **cron 回调**：`eval-adaptive-k-spatial-p25-seed43` (ANALYZING) — Spatial P25 seed43
- **reconcile 发现**：`eval-crm-object-k20-seed44` (ANALYZING) — Object K=20 seed44
- **仍在运行**：`eval-adaptive-k-spatial-p50-seed42`、`eval-obs-only-object-norm005-seed43`、`eval-obs-only-object-norm003-seed44`
- **Worker 池**：2 个分析 Worker + 1 个 mass-deploy Worker = 3 running

等待 Worker 回调处理结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43"
}
```

</details>

---

## Round 2

2 recorded events

### User

_source line 29 · 2026-05-21T02:51:36.709449+00:00_

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
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43",
  "source": "system:ralph_loop"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-21T02:52:25.866606+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单必须查 `get_project_status` 的 `execution.gpu_ids`，ROADMAP 说 17× RTX 4090 across 4 servers 但具体分配动态变化
- Object CRM K=10 Table 1 已锁定 norm02-only n=6 (16.8±1.8%)，D084 决定 seed42 (SR=20%) 不纳入——不要把新的 Object CRM 结果随意加入 Table 1
- Spatial CRM K=10 已修正为 clean n=8 (34.4±1.5%)，D083——不要用旧数据
- Long OOD 已降级 cautious wording (D081, MW-U p=0.061 n.s.)——不要写 significant
- evaluate.py 确认使用 batched inference (D082)——延迟表和效率声明需基于此
- P50 是 Pareto 最优 (D078)，论文核心配置——P25/P75/P90 是 sweep 支撑数据，不是主推

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: Long VLA-only seed54, Long CRM seed53, Spatial VLA-only seed53 运行中
- **bjb1-32546**: 6× RTX 4090, 工作目录 `/root/autodl-tmp/acr-vla-conformal-refinement/`, Python: conda base `/root/miniconda3/bin/python`, CRM checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt`
- **bjb2-28827**: 6× RTX 4090, 同上路径结构; eval-obs-only-object-norm005-seed43 (pid=278354), eval-obs-only-object-norm003-seed44 (pid=279014) 运行中
- **bjb2-40593**: Spatial Adaptive K P50 seed42 运行中 (rollout)
- W&B: 项目配置里有 entity/project，Worker 用 fetch_wandb_metrics 查询
- 活跃 Worker: `worker_mass-deploy_multi-seed-supplement_20260520T104205` (running，大批量部署)

### 3. 📊 当前状态
**刚发生的**：收到 cron 回调 `eval-adaptive-k-spatial-p25-seed43` (ANALYZING)，同时 reconcile 发现 `eval-crm-object-k20-seed44` 也完成 (EXIT_CODE=0 → ANALYZING)。已派出两个分析 Worker：
- `worker_analyze_eval-adaptive-k-spatial-p25-seed43_20260520T105000` — 读 bjb1-32546 日志提取 SR/avg_K/fast_path
- `worker_analyze_eval-crm-object-k20-seed44_20260520T105005` — 读 bjb2-28827 日志提取 SR

**等待中的回调**：
- 上述两个分析 Worker 完成 → 需要更新 registry → 汇报 Director
- eval-adaptive-k-spatial-p50-seed42 (bjb2-40593) — Spatial P50 核心实验，最重要
- eval-obs-only-object-norm005-seed43 (bjb2-28827) — 低 norm 补充 seed
- eval-obs-only-object-norm003-seed44 (bjb2-28827) — 低 norm 补充 seed
- mass-deploy Worker 可能还在部署更多实验

**RUNNING 实验** (reconcile 确认)：eval-adaptive-k-spatial-p50-seed42, eval-obs-only-object-norm005-seed43, eval-obs-only-object-norm003-seed44, 以及 bjb1-18228 上的 Long/Spatial 系列

### 4. 📋 待办
- 两个分析 Worker 回调到达 → 读结果，update_registry(status=DONE)，汇报 Director（带 [资源] 行）
- eval-adaptive-k-spatial-p25-seed43 结果出来后 → 与 Object P25 (14.3%) 对比，更新 Spatial Adaptive K sweep 表格
- eval-crm-object-k20-seed44 结果出来后 → 与 K=10 baseline (16.8%) 对比，判断 K=20 是否有额外收益
- Spatial Adaptive K P50 seed42 完成 → **最关键**，这是核心配置跨 benchmark 验证的第一个 seed
- ROADMAP 待部署：Spatial Adaptive K P50 seed43/44、Random Selection baseline seed42/44 (plan_600)、CRM Object norm02 seed42 补充 — 确认 mass-deploy Worker 是否已覆盖
- fig3_kvalue 重新生成 — 待 K-value sweep 数据齐全后派 Worker

### 5. 🎯 战略上下文
- **CoRL 2026 DDL = 2026-05-29，剩 ~9 天**
- 论文核心贡献 = Adaptive K (D077 用户硬要求)，K=10 分析降为 supporting evidence
- 信号已锁定 K=2 L2 distance (ρ=0.9979, D076)，CRM magnitude 和 FMVD 都 NO-GO
- Object Adaptive K sweep 12/12 全部完成，P50 = Pareto 最优 (15.3%, avg_K ~3.8, ~77% fast path, ~91% of K=10)
- **Spatial Adaptive K 是当前最重要的缺口** — 需要跨 benchmark 验证核心方法
- 决策链：D075(FMVD NO-GO) → D076(K=2 L2 GO) → D077(Adaptive K 升核心) → D078(P50 Pareto) → D079(CRM mag NO-GO) → D080(Table 1 norm02) → D081(Long OOD cautious) → D082(batched inference) → D083(Spatial CRM n=8) → D084(seed42 不入 Table 1)
- **易错点**：不要混淆 Object-calibrated threshold (τ=0.054959 for P25) 和 Spatial 的实际表现——阈值是从 Object 标定的，跨 benchmark 泛化性正是要验证的
- **易错点**：report.md 告警列表很长但大多是历史 killed/failed 实验，不要被干扰，关注 RUNNING 和 ANALYZING 的
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:eval-adaptive-k-spatial-p25-seed43"
}
```

</details>

---
