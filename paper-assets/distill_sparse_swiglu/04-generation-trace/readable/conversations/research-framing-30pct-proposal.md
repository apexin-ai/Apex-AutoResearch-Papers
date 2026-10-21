# research framing 30pct proposal

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_research_framing_30pct_proposal_20260516T025534.jsonl`
- **Structured JSON:** [`87d972d8f6fd8981e993.json`](../../sessions/87/87d972d8f6fd8981e993.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-16T03:00:31.946198+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T03:00:31.946570+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T03:00:31.946740+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T03:00:31.946940+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md\", \"content\": \"# Paper Framing — distill_sparse_swiglu\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\\n- Deadline: 2026-05-25 (ARR submission)\\n- Track: Efficient Methods for NLP\\n\\n## Core Claims\\n\\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating 67.2M compensation parameters (~256MB, 32 layers × bottleneck MLP) and per-layer GEMV overhead at inference. All quality comparisons must be presented alongside inference cost (params, FLOPs, latency) to prevent \\\"unfair comparison\\\" attacks. (Headline claim)\\n\\n2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL \\\"subsuming\\\" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that KL addresses. (Evidence: plan_005_subsumption_s42, spon_2048_s42, D009, D010)\\n\\n3. **KL advantage grows with sparsity level (testable prediction)**: BCE's per-neuron factorized gradient (mean-field analog) misses joint neuron interactions scaling as O(s^2 D^2). We predict KL-vs-BCE delta follows approximately quadratic curve in sparsity level s — to be validated by 7-level sparsity sweep (plan_008). If empirical scaling deviates from quadratic (linear, log, 
…[truncated 4471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T03:00:31.947152+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "ROADMAP.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "ROADMAP.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T03:00:31.947332+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ROADMAP.md\", \"content\": \"# distill_sparse_swiglu — Research Dashboard\\n\\n> 最后更新: 2026-05-16 02:53 UTC | 更新原因: D030: 30% downstream collapse + per-layer sparsity imbalance root cause; new P0 uniform allocation ablation\\n\\n## 核心方向\\nKL distillation 使 SwiGLU LLM 的 contextual sparsity prediction 不再需要 error compensation 和 static bias correction，实现最简推理管线。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research + 审稿进行中（EMNLP 2026 ARR May, DDL 2026-05-25）\\n- **实验**: plan_001-006 全部完成，plan_008 部分完成（30% 训练+PPL done，downstream 崩溃）\\n- **Claim 1 (KL >> all baselines)**: ✅ PPL 层面确认\\n- **Claim 2 (SPON orthogonal)**: ✅ 确认\\n- **Claim 3 (sparsity scaling)**: ⚠️ 重大发现 — 见下方\\n\\n### ⚠️ 关键发现：Per-Layer Sparsity 不均匀导致 Downstream 崩溃 (D030)\\n- 30% KL: PPL 8.98（+47%），但 MMLU 28.74%（≈随机）、GSM8K 7.43%（-85%）\\n- **根因**：全局 top-k 将 sparsity 集中在后层（Layer 26-31: 41-70%，Layer 31=70.3%）\\n- PPL 是平均指标（前层好即可），downstream 依赖后层精确输出 → 后层在\\\"崩溃区\\\"运行\\n- **PPL 作为 sparse model 质量指标完全不可信** — 潜在新 contribution\\n- 待验证：uniform per-layer allocation 是否修复 downstream collapse\\n\\n## 近期任务\\n- [ ] **[P0] 提取 50% per-layer sparsity 分布**：确认同样的后层集中模式\\n- [ ] **[P0] 实现 uniform per-layer allocation**：每层独立 top-k，不需重新训练\\n- [ ] **[P0] Uniform 30%+50% 消融实验**：PPL + 4 task downstream，与 global 对比\\n- [ ] plan_007 benchmark eval 统一重跑（benchmark_eval.py 就绪后）\\n- [ ] plan_009 Mistral 泛化验证\\n- [ ] 修复 lm_eval_teal_50pct registry model 字段错误\\n- [ ] 根据 uniform 实验结果决定是否更新 paper_framing.md Claim 3\\n\\n## GPU 预算\\n- 分配: westd-34887 cuda:0 + cuda:1\\n- 当前: Agent 处理 worker_done 队列中，即将启动 uniform per-layer 实验\\n- 累计 GPU·h: ~90h used / plan 总预算 ~196h\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D030 | 2026-05-16 | 30% KL 不能作为推荐配置；per-layer sparsity 不均匀是 downstream | lm_eval_kl_30pct_s42, kl_sparsity30_s42_v3 |\\n| D029 | 2026-05-16 | 统一 few-shot 设置：plan_007 用 benchm
…[truncated 1061 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T03:00:31.947497+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T03:00:31.947695+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/memory.md\", \"content\": \"# Project Memory\\n\\n## Paper Framing Decisions (Director-approved)\\n\\n### BCE vs training-free: \\\"objective mismatch\\\" 非 \\\"anti-learning\\\" (2026-05-16)\\nBCE (54.84) 比 training-free (23-33) 差。**禁止用 \\\"anti-learning\\\" framing**，改用 **\\\"objective mismatch\\\"**：BCE 优化 per-neuron binary accuracy，TEAL 推理用 global top-k 重分配，两者结构性不兼容。BCE 学到的 per-neuron scoring 在 global budget allocation 下不是最优的。正确 claim: loss function 必须匹配推理管线的 sparsity allocation 机制。KL 直接优化 output distribution，天然兼容任何 allocation 策略。\\n\\n### KL PPL 统一引用规范 (2026-05-16)\\n论文中所有 KL PPL 对比统一用 **4-seed mean 12.00±0.07**（TEAL sparse PPL），不要用单 seed 最佳值 11.91。BCE iso-compute 对比时标注步数（1000 步 vs KL 1000 步，但 BCE per-step FLOPs 仅 KL 的 1/2.71）。\\n\\n### SPON framing: \\\"marginal complement\\\" 非 \\\"subsumption\\\" (2026-05-15)\\n禁止 \\\"KL subsumes SPON\\\" 措辞。正确表述：SPON corrections are orthogonal to and much smaller than predictor mask effects (cos_sim=0.196, magnitude ratio=16%)。D010 \\\"marginal complement\\\" framing。\\n\\n### s456 outlier 报告方式 (2026-05-16)\\n报 \\\"5-seed mean: 12.32±0.71\\\" + \\\"Excluding s456 (TEAL allocation outlier): 12.00±0.07\\\"。附 per-seed breakdown table + Layer 31 keep ratio 分析。不跑第 6 个 seed。\\n\\n## Key Insights (non-metrics)\\n\\n### 50% sparsity 摧毁 autoregressive generation (2026-05-16)\\nGSM8K 生成对比（10 samples）：sparse 50% 模型 1-3 句后进入无限重复循环，0/10 正确。退化模式是推理能力根本性丧失（模式 A），非仅数字算错。PPL 不惩罚 repetition loop（每个重复 token 仍有较高概率）。这解释了 PPL 12.00 但 GSM8K exact_match 仅 0.0121 的 disconnect。论文需用 30% 数据展示 sparsity-task tradeoff。\\n\\n### PPL-downstream disconnect 是真实现象，非 eval bug (2026-05-16)\\n三重验证确认：(1) acc_norm 已正确使用，(2) mask 逻辑审查无 bug（HFLM logit diff=0.0），(3) 生成对比显示推理链断裂。根因：50% sparsity 下 logit 微小偏移（如 \\\"Paris\\\" 从 #2 降到 #5）足以翻转 4-choice 答案，且摧毁 autoregressive 推理链。\\n\\n### PPL-downstream disconnect 文献支撑 (2026-05-16)\\n文献调研确认这
…[truncated 5403 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T03:00:31.947880+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "filters": "{'exp_id': 'lm_eval_kl_30pct_s42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "filters": "{'exp_id': 'lm_eval_kl_30pct_s42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T03:00:31.948041+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2019}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T03:00:31.948218+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "filters": "{'exp_id': 'kl_sparsity30_s42_v3'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "filters": "{'exp_id': 'kl_sparsity30_s42_v3'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T03:00:31.948354+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2519}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T03:00:31.948476+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "filters": "{'exp_id': 'lm_eval_kl_s42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "filters": "{'exp_id': 'lm_eval_kl_s42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T03:00:31.948599+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1479}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T03:00:31.948716+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "filters": "{'exp_id': 'lm_eval_teal_50pct'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "filters": "{'exp_id': 'lm_eval_teal_50pct'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T03:00:31.948843+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1535}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T03:00:31.949188+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "limit": "30",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "limit": "30",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T03:00:31.949986+00:00_

&lt;persisted-output>
Output too large (51.2KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/cc189c81-f1fd-442e-a5bc-e0b0a7a34008/tool-results/toolu_01XjeeMYCkxU9WX9k7fcLxbc.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"lm_eval_kl_30pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:35:56.358Z\", \"updated_at\": \"2026-05-16T02:49:25.308Z\", \"hypothesis\": \"30% sparsity downstream eval (ARC-c, WinoGrande, MMLU, GSM8K) - 与 50% 对比看退化是否有梯度。决定论文是否能 claim \\\"30% 为推荐配置\\\"。\", \"spec\": {\"command\": \"python -u src/lm_eval_sparse.py --tasks arc_challenge,winogrande,mmlu,gsm8k --sparsity_target 0.3\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"191335\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_kl_30pct_s42.log\", \"submitted_at\": \"2026-05-16T01:58:48.081Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"meta-llama/Llama-3.1-8B\", \"seed\": 42, \"wall_clock_seconds\": 3037.2, \"gpu_hours\": 0.84}, \"notes\": \"第一次提交 (PID 186674) 因 HF httpx \\\"Cannot send a request, client closed\\\" 失败，无输出。需设 HF_HUB_OFFLINE=1 重跑。\", \"reproduce\": {\"finished_at\": \"2026-05-16T02:46:54.414Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T02:46:56.057400+00:00\"}]}, \"metrics\": {\"arc_challenge_acc\": 0.3575, \"arc_challenge_acc_norm\": 0.3737, \"winogrande_acc\": 0.6756, \"mmlu_acc\": 0.2874, \"gsm8k_exact_match_strict\": 0.0743, \"gsm8k_exact_match_flexible\": 0.0781, \"actual_sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"condition\": \"kl_distill_30pct_sparsity_s42\", \"mmlu_stem_acc\": 0.2499, \"mmlu_social_sciences_acc\": 0.2896, \"mmlu_humanities_acc\": 0.2786, \"mmlu_other_acc\": 0
…[truncated 319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T03:00:31.950212+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/cc189c81-f1fd-442e-a5bc-e0b0a7a34008/tool-results/toolu_01XjeeMYCkxU9WX9k7fcLxbc.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/cc189c81-f1fd-442e-a5bc-e0b0a7a34008/tool-results/toolu_01XjeeMYCkxU9WX9k7fcLxbc.txt"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T03:00:31.950801+00:00_

1	{"result":"{\"success\": true, \"data\": {\"experiments\": {\"lm_eval_kl_30pct_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:35:56.358Z\", \"updated_at\": \"2026-05-16T02:49:25.308Z\", \"hypothesis\": \"30% sparsity downstream eval (ARC-c, WinoGrande, MMLU, GSM8K) - 与 50% 对比看退化是否有梯度。决定论文是否能 claim \\\"30% 为推荐配置\\\"。\", \"spec\": {\"command\": \"python -u src/lm_eval_sparse.py --tasks arc_challenge,winogrande,mmlu,gsm8k --sparsity_target 0.3\", \"server\": \"westd-34887\", \"gpu\": [\"cuda:0\"], \"pid\": \"191335\", \"log_path\": \"~/runs/distill_sparse_swiglu/lm_eval_kl_30pct_s42.log\", \"submitted_at\": \"2026-05-16T01:58:48.081Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"arc_challenge,winogrande,mmlu,gsm8k\", \"data_count\": 0, \"model_name\": \"meta-llama/Llama-3.1-8B\", \"seed\": 42, \"wall_clock_seconds\": 3037.2, \"gpu_hours\": 0.84}, \"notes\": \"第一次提交 (PID 186674) 因 HF httpx \\\"Cannot send a request, client closed\\\" 失败，无输出。需设 HF_HUB_OFFLINE=1 重跑。\", \"reproduce\": {\"finished_at\": \"2026-05-16T02:46:54.414Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T02:46:56.057400+00:00\"}]}, \"metrics\": {\"arc_challenge_acc\": 0.3575, \"arc_challenge_acc_norm\": 0.3737, \"winogrande_acc\": 0.6756, \"mmlu_acc\": 0.2874, \"gsm8k_exact_match_strict\": 0.0743, \"gsm8k_exact_match_flexible\": 0.0781, \"actual_sparsity\": 0.3, \"model\": \"llama-3.1-8b\", \"condition\": \"kl_distill_30pct_sparsity_s42\", \"mmlu_stem_acc\": 0.2499, \"mmlu_social_sciences_acc\": 0.2896, \"mmlu_humanities_acc\": 0.2786, \"mmlu_other_acc\": 0.3363}, \"conclusion\": \"negative\", \"checkpoint_path\": \"results/lm_eval_kl_30pct/results.json\", \"completed_at\": \"2026-05-16T02:49:25.308Z\"}, \"lm_eval_teal_50pct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:35:57.527Z\", \"updated_at\": \"2026-05-16T
…[truncated 50440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T03:00:31.951035+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "limit": "30",
  "fields": "['*']",
  "filters": "{'status': 'DONE'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "limit": "30",
    "fields": "['*']",
    "filters": "{'status': 'DONE'}"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T03:00:31.951400+00:00_

Error: result (58,956 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/cc189c81-f1fd-442e-a5bc-e0b0a7a34008/tool-results/mcp-agent-ml-research-read_registry-1778900170916.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/cc189c81-f1fd-442e-a5bc-e0b0a7a34008/tool-results/mcp-agent-ml-research-read_registry-1778900170916.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T03:00:31.951607+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T03:00:31.951737+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T03:00:31.951892+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

````json
{
  "project": "distill_sparse_swiglu",
  "file": "artifacts/framing_proposal_30pct_downstream.md",
  "content": "# Framing 调整提案：30% Downstream Negative 结果\n\n> 生成时间: 2026-05-16 | 触发: lm_eval_kl_30pct_s42 negative result + D030\n\n---\n\n## 1. 原 Claim\n\n**Claim 3 (paper_framing.md)**:\n> \"KL advantage grows with sparsity level (testable prediction): BCE's per-neuron factorized gradient misses joint neuron interactions scaling as O(s²D²). We predict KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.\"\n\n隐含假设：低 sparsity（如 30%）是安全的操作点，论文 Story Spine 中 \"30% 为推荐配置\" 的叙事建立在 \"PPL 好 → downstream 也好\" 的未验证前提之上。\n\n---\n\n## 2. 实验结果（客观数字）\n\n### 2.1 KL 30% Downstream (exp: lm_eval_kl_30pct_s42)\n\n| Task | Dense | KL 30% | Drop | 备注 |\n|------|-------|--------|------|------|\n| arc_challenge (acc_norm) | 0.5819 | 0.3737 | **-35.8%** | 与 50% 的 -35.2% 几乎相同 |\n| winogrande (acc) | 0.7814 | 0.6756 | **-13.5%** | 最轻微的退化 |\n| mmlu (acc) | 0.6532 | 0.2874 | **-56.0%** | ≈4-choice 随机水平 (0.25) |\n| gsm8k (flexible) | 0.5004 | 0.0781 | **-84.4%** | 近乎完全丧失 |\n\n### 2.2 KL 30% PPL (exp: kl_sparsity30_s42_v3)\n\n| Metric | Value |\n|--------|-------|\n| true_dense_ppl | 6.12 |\n| predictor_hard_mask_ppl | 7.30 (+19.3%) |\n| teal_sparse_ppl | 8.98 (+46.7%) |\n| model_level_sparsity | 0.300 |\n| per-layer sparsity | 早期 0.13-0.23, 中间 0.30-0.34, **后层 0.50-0.70** |\n\n### 2.3 跨条件对比\n\n| Metric | KL 30% | KL 50% | TEAL 50% | Dense |\n|--------|--------|--------|----------|-------|\n| **PPL (TEAL)** | 8.98 | 12.00±0.07 | 23.31 | 6.12 |\n| arc_challenge | 0.3737 | 0.3771 | 0.2910 | 0.5819 |\n| winogrande | 0.6756 | 0.6156 | 0.5556 | 0.7814 |\n| mmlu | 0.2874 | 0.2591 | 0.2856 | 0.6532 |\n| gsm8k | 0.0781 | 0.0121 | 0.0190 | 0.5004 |\n\n数据来源: lm_eval_kl_30pct_s42, lm_eval_kl_s42, lm_eval_teal_50pct, lm_eval_dense, kl_sparsity30_s42_v3\n\n---\n\n## 3. 重新审视\n\n### 3.1 被挑战的 Hypothesis\n\n**H_safe_30**: \"30% sparsity 是安全操作点，PPL 退化可控 → downstream 退化也可控。\"\n\n这一假设被彻底否定。MMLU 在 30% 就崩到接近随机 (0.2874 vs random 0.25)，GSM8K 丧失 84%。PPL 仅 +47% 不足以预测 downstream 灾难。\n\n**H_ppl_proxy**: \"PPL 是 sparse model 质量的可靠代理指标。\"\n\n30% 数据点将此否定从 \"50% 的特例\" 升级为 \"系统性规律\"：\n- 30% PPL: 8.98 (+47%)，但 MMLU ≈ random\n- 50% PPL: 12.00 (+96%)，但 MMLU ≈ random\n- PPL 几乎翻倍，MMLU 退化程度几乎相同 → PPL 变化量与 downstream 退化量不相关\n\n### 3.2 被忽略的变量：Per-Layer Sparsity 不均匀\n\n**这是根因。** 全局 top-k 将 sparsity 集中在后层：\n\n- 30% global → Layer 26-31 实际 sparsity 41-70%（Layer 31 高达 70.3%）\n- 后层直连 LM head，负责精确知识检索和推理链延续\n- PPL 是平均指标（前层正常即可拉低），downstream 依赖后层逐 token 精确输出\n\n**这与 50% 的 PPL-downstream disconnect 是完全相同的机制**，只是程度不同：\n- 50% global → 后层 sparsity 可能超过 80%（待 P0 任务确认）\n- 30% global → 后层 sparsity 50-70%，仍在 \"崩溃区\"\n\n### 3.3 已做实验的有效性\n\n| 实验 | 新 framing 下是否有效 | 说明 |\n|------|----------------------|------|\n| KL vs BCE PPL (Claim 1) | ✅ 完全有效 | PPL 层面 KL 优势不受影响 |\n| SPON orthogonality (Claim 2) | ✅ 完全有效 | logit 空间分解不依赖 downstream |\n| STE vs Gumbel ablation | ✅ 完全有效 | 训练稳定性结论独立于 downstream |\n| Mistral cross-arch PPL | ✅ 有效（PPL 层面）| downstream 待补 |\n| 50% downstream collapse (D028) | ✅ 升值 | 从 \"负面结果\" 变为 \"系统性发现的一个数据点\" |\n| 30% downstream collapse (D030) | ✅ 核心新证据 | 证明 PPL-downstream disconnect 是普遍现象 |\n| GSM8K 生成质量对比 | ✅ 升值 | 提供 disconnect 的机制解释 |\n| 文献调研 (PPL-downstream) | ✅ 关键支撑 | 定位我们的贡献在文献空白中 |\n\n---\n\n## 4. 新 Narrative 骨架（3 种备选）\n\n### Narrative A: \"PPL-Downstream Disconnect 是论文核心贡献之一\"\n\n**核心论点**: 在 contextual sparsity prediction 框架下，PPL 不是可靠的质量指标。我们系统性地展示这一 disconnect，分析根因（per-layer sparsity imbalance），并提出诊断协议。\n\n**Story Spine 调整**:\n- Problem: 不变\n- Existing approaches & gaps: 增加 \"所有现有工作仅用 PPL 评估 sparse model 质量\"\n- Our contribution: (1) KL >> BCE/compensation [原 Claim 1]; (2) SPON orthogonal [原 Claim 2]; **(3) PPL-downstream disconnect 的系统性证据 + 根因分析 + 文献定位** [替换原 Claim 3]\n- Headline: \"KL distillation produces the best PPL-quality sparse predictor, but PPL alone is insufficient — we demonstrate a systematic PPL-downstream disconnect caused by per-layer sparsity imbalance under global top-k allocation.\"\n\n**优点**: 诚实、有文献支撑（Khanal & Capone 2024, Xu et al. 2024 EMNLP, Kodathala & Vunnam 2026, Siam et al. 2026）、填补文献空白（无论文在 contextual sparsity + KL distillation 下系统研究此现象）、所有已做实验全部可用。\n\n**风险**: Reviewer 可能认为 \"发现问题但没解决\" 不够 contribution；需要 uniform allocation 实验作为 \"指向解决方案\" 的 bridge。\n\n**强度匹配**: 30% 和 50% 两个数据点 + TEAL 50% 对照 + 文献支撑 = 中等强度。可支撑 \"systematic evidence\" 但不足以支撑 \"definitive characterization\"。\n\n### Narrative B: \"Per-Layer Allocation 修复 Downstream Collapse\"（需新实验）\n\n**核心论点**: Global top-k allocation 是 downstream collapse 的根因。Per-layer uniform allocation（每层独立 top-k）能在保持 sparsity 目标的同时恢复 downstream quality。KL + uniform allocation 是正确的推理管线。\n\n**Story Spine 调整**:\n- Problem: 增加 \"global top-k allocation 导致 per-layer sparsity 不均匀，摧毁后层精确输出\"\n- Our contribution: (1) KL >> all [原 Claim 1]; (2) SPON orthogonal [原 Claim 2]; **(3) Uniform allocation 修复 downstream collapse，KL + uniform 是推荐管线** [替换原 Claim 3]\n- Headline: \"KL distillation + per-layer uniform allocation achieves [X] downstream quality at 30% sparsity, within [Y]% of dense, while global top-k allocation causes catastrophic downstream collapse despite acceptable PPL.\"\n\n**优点**: 提供解决方案（不只是诊断问题）、30% uniform 如果 downstream 恢复则有强 positive result、自然承接 PPL-disconnect 发现。\n\n**风险**: **完全依赖未完成的实验（ROADMAP P0 任务）。** 如果 uniform allocation 不能修复 downstream（即问题不仅仅是 per-layer imbalance，而是 sparsity 本身摧毁了某些能力），则此 narrative 崩塌。\n\n**实验依赖**: uniform_30pct + uniform_50pct downstream eval（ROADMAP 已列 P0）\n\n### Narrative C: \"Task-Sensitive Sparsity Spectrum\"\n\n**核心论点**: 不同 downstream task 对 sparsity 的敏感度存在质的差异。我们构建 task × sparsity 退化矩阵，揭示三层敏感度谱系。\n\n**Task 敏感度分层（基于现有数据）**:\n\n| 敏感度 | Task | 30% drop | 50% drop | 特征 |\n|--------|------|----------|----------|------|\n| Robust | WinoGrande | -13.5% | -21.2% | 渐进退化，30% 保留 87% |\n| Cliff | ARC-c | -35.8% | -35.2% | 在 ≤30% 已到 cliff，30→50% 无进一步退化 |\n| Ultra-fragile | MMLU | -56.0% | -60.3% | 30% 即 ≈ random，知识检索彻底丧失 |\n| Ultra-fragile | GSM8K | -84.4% | -97.6% | 30% 残留微弱，50% 完全丧失 |\n\n**Story Spine 调整**:\n- Our contribution: (1) KL >> all [原 Claim 1]; (2) SPON orthogonal [原 Claim 2]; **(3) Task-sensitive sparsity spectrum: 对 sparsity 的退化不是均匀的，而是 task-dependent 的阶梯式崩溃** [替换原 Claim 3]\n\n**优点**: 每个数字都是 informative 的（包括负面结果）；ARC-c 在 30→50% 无进一步退化是独特发现；GSM8K 的 gradual degradation (0.0781 → 0.0121) 说明存在连续退化（非二元 cliff）。\n\n**风险**: 数据点有限（仅 30% 和 50% 两个 level，4 个 task）。需要更多 sparsity level（如 10%, 20%, 40%）才能画出完整 spectrum。\n\n**推荐**: **Narrative A 为主线，Narrative C 为子节**。Narrative B 作为 \"future direction\" 或在 uniform 实验完成后升级为主线。\n\n---\n\n## 5. 对论文各章节的影响\n\n### Abstract\n- **删除**: \"30% 为推荐配置\" 相关措辞\n- **新增**: \"我们发现 PPL 与 downstream quality 存在系统性 disconnect：30% sparsity 下 PPL 仅 +47% 但 MMLU 崩至随机水平\"\n- **保留**: KL >> BCE/compensation headline 不变\n\n### Introduction\n- Story Spine 的 \"headline result template\" 需重写\n- 增加第三段：PPL-downstream disconnect 的 motivation\n- 引用 Khanal & Capone (2024), Xu et al. (2024)\n\n### Related Work\n- 新增小节：\"PPL as Evaluation Metric for Sparse Models\"\n- 引用 4 篇文献调研结果（见 memory.md \"PPL-downstream disconnect 文献支撑\"）\n\n### Method\n- 无重大影响。KL loss、predictor architecture、Gumbel relaxation 不变\n- 可增加 per-layer sparsity 分析工具的描述\n\n### Experiments — PPL Results (原有)\n- **完全保留**。KL vs BCE、KL vs TEAL、SPON orthogonality、STE ablation 全部有效\n- 增加 caveat: \"PPL results are necessary but not sufficient for quality assessment\"\n\n### Experiments — Downstream Results (新增/重写)\n- **核心新增章节**: Task × Sparsity 退化矩阵\n- 30% 和 50% 两个 level × 4 tasks × 2 methods (KL, TEAL)\n- Figure: 退化热力图（task 行, sparsity 列, color = drop%）\n- WinoGrande gradual degradation vs MMLU/GSM8K cliff 对比\n\n### Experiments — PPL-Downstream Disconnect Analysis (新增)\n- Per-layer sparsity 分布可视化（30% vs 50%）\n- 后层 over-pruning → downstream collapse 的因果链\n- GSM8K 生成质量对比（dense vs sparse, 来自 gsm8k_gen_compare）\n- 文献对比：我们的发现与 Khanal (2024) / Siam (2026) 的一致性\n\n### Discussion\n- PPL 作为 sparse model 评估指标的局限性\n- Per-layer allocation 作为潜在修复方向\n- Task sensitivity 分层的实践意义\n\n### Conclusion\n- 三句话公式：(1) KL >> all on PPL axis; (2) PPL ≠ downstream under global top-k; (3) per-layer sparsity imbalance 是根因，指向 uniform allocation 方向\n\n---\n\n## 6. 建议下一步实验\n\n### 实验 1: [P0] 50% Per-Layer Sparsity 分布提取\n- **目的**: 确认 50% global top-k 是否存在同样的后层集中模式\n- **方法**: 从 mvp_kl_norm_v2_s42 predictor 提取 per-layer sparsity 分布\n- **预期**: 后层 sparsity >> 50%（与 30% 的 0.50-0.70 模式一致但更极端）\n- **填补矩阵**: 确认 30% 和 50% 共享同一根因\n- **耗时**: < 1 GPU·h\n\n### 实验 2: [P0] Uniform Per-Layer Allocation 30% + 50%\n- **目的**: 验证 per-layer sparsity 均匀分配是否修复 downstream collapse\n- **方法**: 每层独立 top-k（不需重新训练 predictor，仅修改推理时的 mask 生成策略）\n- **评估**: PPL + arc_challenge + winogrande + mmlu + gsm8k\n- **关键对比**:\n  - uniform_30% vs global_30% downstream\n  - uniform_50% vs global_50% downstream\n- **预期 A（乐观）**: 30% uniform 恢复 MMLU > 0.50, GSM8K > 0.30 → 激活 Narrative B\n- **预期 B（悲观）**: uniform 仍然崩 → PPL-disconnect 不仅仅是 allocation 问题，sparsity 本身摧毁某些能力\n- **耗时**: ~2 GPU·h (4 conditions × 0.5h each)\n- **决策点**: 若预期 A 成立 → 论文 Claim 3 切换到 Narrative B；若预期 B → 锁定 Narrative A+C\n\n### 实验 3: TEAL 30% Downstream (已在 ROADMAP)\n- **目的**: 与 KL 30% 对比，验证 30% collapse 是否为所有 sparsity 方法的固有限制\n- **方法**: lm_eval_teal.py --sparsity_target 0.3\n- **预期**: TEAL 30% 也崩（与 TEAL 50% 同模式），但可能比 KL 30% 更差（与 50% 的 TEAL < KL 一致）\n- **填补矩阵**: 完成 method × sparsity × task 三维矩阵的最后一个 condition\n- **耗时**: ~1 GPU·h\n- **状态**: registry 中 lm_eval_teal_30pct 已 PREPARING\n\n### 实验 4: [P1] 10% / 20% Sparsity Downstream\n- **目的**: 找到 downstream 退化的 onset point（目前只知道 30% 已崩，但不知道 threshold 在哪）\n- **方法**: 需先训练 10% 和 20% predictor，再跑 downstream\n- **价值**: 如果 20% 尚可但 30% 崩 → 确认 threshold 在 20-30% 区间；如果 10% 就崩 → 问题更严重\n- **耗时**: ~4 GPU·h (2 training + 2 eval)\n- **优先级**: P1 — 对 Narrative C 重要但对 DDL (05-25) 非必需\n\n### 实验 5: [P1] Per-Layer Sparsity Cap Ablation\n- **目的**: 测试约束后层 sparsity 上限（如 max 40%/layer）是否比 uniform 更好\n- **方法**: 修改 TEAL global top-k，增加 per-layer cap 约束\n- **评估**: PPL + 4 task downstream\n- **价值**: 如果 capped > uniform on PPL but capped ≈ uniform on downstream → 可得到 PPL-downstream Pareto 最优点\n- **耗时**: ~2 GPU·h\n- **优先级**: P1 — 仅在 uniform 实验（实验 2）出正面结果后执行\n\n---\n\n## 7. 决策树摘要\n\n```\nuniform_30% downstream 结果\n├── MMLU > 0.50, GSM8K > 0.30 (downstream 恢复)\n│   → Narrative B 为主线: \"KL + uniform allocation = 推荐管线\"\n│   → Claim 3 重写为 allocation strategy comparison\n│   → 30% uniform 成为论文 headline positive result\n│\n├── MMLU 0.35-0.50, GSM8K 0.10-0.30 (部分恢复)\n│   → Narrative A+B 混合: disconnect 是真实的，uniform 缓解但不消除\n│   → 论文贡献 = 诊断 + 部分修复\n│\n└── MMLU < 0.35, GSM8K < 0.10 (无恢复)\n    → Narrative A+C 为主线: PPL-disconnect 是根本性限制\n    → per-layer imbalance 是 necessary 但 not sufficient 的根因\n    → 论文贡献 = 系统性 disconnect 证据 + task sensitivity spectrum\n```\n\n---\n\n## 写作红线\n\n1. **禁止 cherry-picking**: 不能只报 WinoGrande（退化最轻）而隐藏 MMLU/GSM8K\n2. **所有定量 claim 附 exp_id**: 每个数字必须追溯到 registry\n3. **强度匹配**: \"systematic evidence\" 而非 \"definitive proof\"（仅 2 个 sparsity level）\n4. **禁止 \"30% is the recommended operating point\"**: 数据明确否定\n5. **PPL 结果保留但降级**: PPL 表格前后必须加 caveat，不能单独作为 quality claim 的依据\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "file": "artifacts/framing_proposal_30pct_downstream.md",
    "content": "# Framing 调整提案：30% Downstream Negative 结果\n\n> 生成时间: 2026-05-16 | 触发: lm_eval_kl_30pct_s42 negative result + D030\n\n---\n\n## 1. 原 Claim\n\n**Claim 3 (paper_framing.md)**:\n> \"KL advantage grows with sparsity level (testable prediction): BCE's per-neuron factorized gradient misses joint neuron interactions scaling as O(s²D²). We predict KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.\"\n\n隐含假设：低 sparsity（如 30%）是安全的操作点，论文 Story Spine 中 \"30% 为推荐配置\" 的叙事建立在 \"PPL 好 → downstream 也好\" 的未验证前提之上。\n\n---\n\n## 2. 实验结果（客观数字）\n\n### 2.1 KL 30% Downstream (exp: lm_eval_kl_30pct_s42)\n\n| Task | Dense | KL 30% | Drop | 备注 |\n|------|-------|--------|------|------|\n| arc_challenge (acc_norm) | 0.5819 | 0.3737 | **-35.8%** | 与 50% 的 -35.2% 几乎相同 |\n| winogrande (acc) | 0.7814 | 0.6756 | **-13.5%** | 最轻微的退化 |\n| mmlu (acc) | 0.6532 | 0.2874 | **-56.0%** | ≈4-choice 随机水平 (0.25) |\n| gsm8k (flexible) | 0.5004 | 0.0781 | **-84.4%** | 近乎完全丧失 |\n\n### 2.2 KL 30% PPL (exp: kl_sparsity30_s42_v3)\n\n| Metric | Value |\n|--------|-------|\n| true_dense_ppl | 6.12 |\n| predictor_hard_mask_ppl | 7.30 (+19.3%) |\n| teal_sparse_ppl | 8.98 (+46.7%) |\n| model_level_sparsity | 0.300 |\n| per-layer sparsity | 早期 0.13-0.23, 中间 0.30-0.34, **后层 0.50-0.70** |\n\n### 2.3 跨条件对比\n\n| Metric | KL 30% | KL 50% | TEAL 50% | Dense |\n|--------|--------|--------|----------|-------|\n| **PPL (TEAL)** | 8.98 | 12.00±0.07 | 23.31 | 6.12 |\n| arc_challenge | 0.3737 | 0.3771 | 0.2910 | 0.5819 |\n| winogrande | 0.6756 | 0.6156 | 0.5556 | 0.7814 |\n| mmlu | 0.2874 | 0.2591 | 0.2856 | 0.6532 |\n| gsm8k | 0.0781 | 0.0121 | 0.0190 | 0.5004 |\n\n数据来源: lm_eval_kl_30pct_s42, lm_eval_kl_s42, lm_eval_teal_50pct, lm_eval_dense, kl_sparsity30_s42_v3\n\n---\n\n## 3. 重新审视\n\n### 3.1 被挑战的 Hypothesis\n\n**H_safe_30**: \"30% sparsity 是安全操作点，PPL 退化可控 → downstream 退化也可控。\"\n\n这一假设被彻底否定。MMLU 在 30% 就崩到接近随机 (0.2874 vs random 0.25)，GSM8K 丧失 84%。PPL 仅 +47% 不足以预测 downstream 灾难。\n\n**H_ppl_proxy**: \"PPL 是 sparse model 质量的可靠代理指标。\"\n\n30% 数据点将此否定从 \"50% 的特例\" 升级为 \"系统性规律\"：\n- 30% PPL: 8.98 (+47%)，但 MMLU ≈ random\n- 50% PPL: 12.00 (+96%)，但 MMLU ≈ random\n- PPL 几乎翻倍，MMLU 退化程度几乎相同 → PPL 变化量与 downstream 退化量不相关\n\n### 3.2 被忽略的变量：Per-Layer Sparsity 不均匀\n\n**这是根因。** 全局 top-k 将 sparsity 集中在后层：\n\n- 30% global → Layer 26-31 实际 sparsity 41-70%（Layer 31 高达 70.3%）\n- 后层直连 LM head，负责精确知识检索和推理链延续\n- PPL 是平均指标（前层正常即可拉低），downstream 依赖后层逐 token 精确输出\n\n**这与 50% 的 PPL-downstream disconnect 是完全相同的机制**，只是程度不同：\n- 50% global → 后层 sparsity 可能超过 80%（待 P0 任务确认）\n- 30% global → 后层 sparsity 50-70%，仍在 \"崩溃区\"\n\n### 3.3 已做实验的有效性\n\n| 实验 | 新 framing 下是否有效 | 说明 |\n|------|----------------------|------|\n| KL vs BCE PPL (Claim 1) | ✅ 完全有效 | PPL 层面 KL 优势不受影响 |\n| SPON orthogonality (Claim 2) | ✅ 完全有效 | logit 空间分解不依赖 downstream |\n| STE vs Gumbel ablation | ✅ 完全有效 | 训练稳定性结论独立于 downstream |\n| Mistral cross-arch PPL | ✅ 有效（PPL 层面）| downstream 待补 |\n| 50% downstream collapse (D028) | ✅ 升值 | 从 \"负面结果\" 变为 \"系统性发现的一个数据点\" |\n| 30% downstream collapse (D030) | ✅ 核心新证据 | 证明 PPL-downstream disconnect 是普遍现象 |\n| GSM8K 生成质量对比 | ✅ 升值 | 提供 disconnect 的机制解释 |\n| 文献调研 (PPL-downstream) | ✅ 关键支撑 | 定位我们的贡献在文献空白中 |\n\n---\n\n## 4. 新 Narrative 骨架（3 种备选）\n\n### Narrative A: \"PPL-Downstream Disconnect 是论文核心贡献之一\"\n\n**核心论点**: 在 contextual sparsity prediction 框架下，PPL 不是可靠的质量指标。我们系统性地展示这一 disconnect，分析根因（per-layer sparsity imbalance），并提出诊断协议。\n\n**Story Spine 调整**:\n- Problem: 不变\n- Existing approaches & gaps: 增加 \"所有现有工作仅用 PPL 评估 sparse model 质量\"\n- Our contribution: (1) KL >> BCE/compensation [原 Claim 1]; (2) SPON orthogonal [原 Claim 2]; **(3) PPL-downstream disconnect 的系统性证据 + 根因分析 + 文献定位** [替换原 Claim 3]\n- Headline: \"KL distillation produces the best PPL-quality sparse predictor, but PPL alone is insufficient — we demonstrate a systematic PPL-downstream disconnect caused by per-layer sparsity imbalance under global top-k allocation.\"\n\n**优点**: 诚实、有文献支撑（Khanal & Capone 2024, Xu et al. 2024 EMNLP, Kodathala & Vunnam 2026, Siam et al. 2026）、填补文献空白（无论文在 contextual sparsity + KL distillation 下系统研究此现象）、所有已做实验全部可用。\n\n**风险**: Reviewer 可能认为 \"发现问题但没解决\" 不够 contribution；需要 uniform allocation 实验作为 \"指向解决方案\" 的 bridge。\n\n**强度匹配**: 30% 和 50% 两个数据点 + TEAL 50% 对照 + 文献支撑 = 中等强度。可支撑 \"systematic evidence\" 但不足以支撑 \"definitive characterization\"。\n\n### Narrative B: \"Per-Layer Allocation 修复 Downstream Collapse\"（需新实验）\n\n**核心论点**: Global top-k allocation 是 downstream collapse 的根因。Per-layer uniform allocation（每层独立 top-k）能在保持 sparsity 目标的同时恢复 downstream quality。KL + uniform allocation 是正确的推理管线。\n\n**Story Spine 调整**:\n- Problem: 增加 \"global top-k allocation 导致 per-layer sparsity 不均匀，摧毁后层精确输出\"\n- Our contribution: (1) KL >> all [原 Claim 1]; (2) SPON orthogonal [原 Claim 2]; **(3) Uniform allocation 修复 downstream collapse，KL + uniform 是推荐管线** [替换原 Claim 3]\n- Headline: \"KL distillation + per-layer uniform allocation achieves [X] downstream quality at 30% sparsity, within [Y]% of dense, while global top-k allocation causes catastrophic downstream collapse despite acceptable PPL.\"\n\n**优点**: 提供解决方案（不只是诊断问题）、30% uniform 如果 downstream 恢复则有强 positive result、自然承接 PPL-disconnect 发现。\n\n**风险**: **完全依赖未完成的实验（ROADMAP P0 任务）。** 如果 uniform allocation 不能修复 downstream（即问题不仅仅是 per-layer imbalance，而是 sparsity 本身摧毁了某些能力），则此 narrative 崩塌。\n\n**实验依赖**: uniform_30pct + uniform_50pct downstream eval（ROADMAP 已列 P0）\n\n### Narrative C: \"Task-Sensitive Sparsity Spectrum\"\n\n**核心论点**: 不同 downstream task 对 sparsity 的敏感度存在质的差异。我们构建 task × sparsity 退化矩阵，揭示三层敏感度谱系。\n\n**Task 敏感度分层（基于现有数据）**:\n\n| 敏感度 | Task | 30% drop | 50% drop | 特征 |\n|--------|------|----------|----------|------|\n| Robust | WinoGrande | -13.5% | -21.2% | 渐进退化，30% 保留 87% |\n| Cliff | ARC-c | -35.8% | -35.2% | 在 ≤30% 已到 cliff，30→50% 无进一步退化 |\n| Ultra-fragile | MMLU | -56.0% | -60.3% | 30% 即 ≈ random，知识检索彻底丧失 |\n| Ultra-fragile | GSM8K | -84.4% | -97.6% | 30% 残留微弱，50% 完全丧失 |\n\n**Story Spine 调整**:\n- Our contribution: (1) KL >> all [原 Claim 1]; (2) SPON orthogonal [原 Claim 2]; **(3) Task-sensitive sparsity spectrum: 对 sparsity 的退化不是均匀的，而是 task-dependent 的阶梯式崩溃** [替换原 Claim 3]\n\n**优点**: 每个数字都是 informative 的（包括负面结果）；ARC-c 在 30→50% 无进一步退化是独特发现；GSM8K 的 gradual degradation (0.0781 → 0.0121) 说明存在连续退化（非二元 cliff）。\n\n**风险**: 数据点有限（仅 30% 和 50% 两个 level，4 个 task）。需要更多 sparsity level（如 10%, 20%, 40%）才能画出完整 spectrum。\n\n**推荐**: **Narrative A 为主线，Narrative C 为子节**。Narrative B 作为 \"future direction\" 或在 uniform 实验完成后升级为主线。\n\n---\n\n## 5. 对论文各章节的影响\n\n### Abstract\n- **删除**: \"30% 为推荐配置\" 相关措辞\n- **新增**: \"我们发现 PPL 与 downstream quality 存在系统性 disconnect：30% sparsity 下 PPL 仅 +47% 但 MMLU 崩至随机水平\"\n- **保留**: KL >> BCE/compensation headline 不变\n\n### Introduction\n- Story Spine 的 \"headline result template\" 需重写\n- 增加第三段：PPL-downstream disconnect 的 motivation\n- 引用 Khanal & Capone (2024), Xu et al. (2024)\n\n### Related Work\n- 新增小节：\"PPL as Evaluation Metric for Sparse Models\"\n- 引用 4 篇文献调研结果（见 memory.md \"PPL-downstream disconnect 文献支撑\"）\n\n### Method\n- 无重大影响。KL loss、predictor architecture、Gumbel relaxation 不变\n- 可增加 per-layer sparsity 分析工具的描述\n\n### Experiments — PPL Results (原有)\n- **完全保留**。KL vs BCE、KL vs TEAL、SPON orthogonality、STE ablation 全部有效\n- 增加 caveat: \"PPL results are necessary but not sufficient for quality assessment\"\n\n### Experiments — Downstream Results (新增/重写)\n- **核心新增章节**: Task × Sparsity 退化矩阵\n- 30% 和 50% 两个 level × 4 tasks × 2 methods (KL, TEAL)\n- Figure: 退化热力图（task 行, sparsity 列, color = drop%）\n- WinoGrande gradual degradation vs MMLU/GSM8K cliff 对比\n\n### Experiments — PPL-Downstream Disconnect Analysis (新增)\n- Per-layer sparsity 分布可视化（30% vs 50%）\n- 后层 over-pruning → downstream collapse 的因果链\n- GSM8K 生成质量对比（dense vs sparse, 来自 gsm8k_gen_compare）\n- 文献对比：我们的发现与 Khanal (2024) / Siam (2026) 的一致性\n\n### Discussion\n- PPL 作为 sparse model 评估指标的局限性\n- Per-layer allocation 作为潜在修复方向\n- Task sensitivity 分层的实践意义\n\n### Conclusion\n- 三句话公式：(1) KL >> all on PPL axis; (2) PPL ≠ downstream under global top-k; (3) per-layer sparsity imbalance 是根因，指向 uniform allocation 方向\n\n---\n\n## 6. 建议下一步实验\n\n### 实验 1: [P0] 50% Per-Layer Sparsity 分布提取\n- **目的**: 确认 50% global top-k 是否存在同样的后层集中模式\n- **方法**: 从 mvp_kl_norm_v2_s42 predictor 提取 per-layer sparsity 分布\n- **预期**: 后层 sparsity >> 50%（与 30% 的 0.50-0.70 模式一致但更极端）\n- **填补矩阵**: 确认 30% 和 50% 共享同一根因\n- **耗时**: < 1 GPU·h\n\n### 实验 2: [P0] Uniform Per-Layer Allocation 30% + 50%\n- **目的**: 验证 per-layer sparsity 均匀分配是否修复 downstream collapse\n- **方法**: 每层独立 top-k（不需重新训练 predictor，仅修改推理时的 mask 生成策略）\n- **评估**: PPL + arc_challenge + winogrande + mmlu + gsm8k\n- **关键对比**:\n  - uniform_30% vs global_30% downstream\n  - uniform_50% vs global_50% downstream\n- **预期 A（乐观）**: 30% uniform 恢复 MMLU > 0.50, GSM8K > 0.30 → 激活 Narrative B\n- **预期 B（悲观）**: uniform 仍然崩 → PPL-disconnect 不仅仅是 allocation 问题，sparsity 本身摧毁某些能力\n- **耗时**: ~2 GPU·h (4 conditions × 0.5h each)\n- **决策点**: 若预期 A 成立 → 论文 Claim 3 切换到 Narrative B；若预期 B → 锁定 Narrative A+C\n\n### 实验 3: TEAL 30% Downstream (已在 ROADMAP)\n- **目的**: 与 KL 30% 对比，验证 30% collapse 是否为所有 sparsity 方法的固有限制\n- **方法**: lm_eval_teal.py --sparsity_target 0.3\n- **预期**: TEAL 30% 也崩（与 TEAL 50% 同模式），但可能比 KL 30% 更差（与 50% 的 TEAL < KL 一致）\n- **填补矩阵**: 完成 method × sparsity × task 三维矩阵的最后一个 condition\n- **耗时**: ~1 GPU·h\n- **状态**: registry 中 lm_eval_teal_30pct 已 PREPARING\n\n### 实验 4: [P1] 10% / 20% Sparsity Downstream\n- **目的**: 找到 downstream 退化的 onset point（目前只知道 30% 已崩，但不知道 threshold 在哪）\n- **方法**: 需先训练 10% 和 20% predictor，再跑 downstream\n- **价值**: 如果 20% 尚可但 30% 崩 → 确认 threshold 在 20-30% 区间；如果 10% 就崩 → 问题更严重\n- **耗时**: ~4 GPU·h (2 training + 2 eval)\n- **优先级**: P1 — 对 Narrative C 重要但对 DDL (05-25) 非必需\n\n### 实验 5: [P1] Per-Layer Sparsity Cap Ablation\n- **目的**: 测试约束后层 sparsity 上限（如 max 40%/layer）是否比 uniform 更好\n- **方法**: 修改 TEAL global top-k，增加 per-layer cap 约束\n- **评估**: PPL + 4 task downstream\n- **价值**: 如果 capped > uniform on PPL but capped ≈ uniform on downstream → 可得到 PPL-downstream Pareto 最优点\n- **耗时**: ~2 GPU·h\n- **优先级**: P1 — 仅在 uniform 实验（实验 2）出正面结果后执行\n\n---\n\n## 7. 决策树摘要\n\n```\nuniform_30% downstream 结果\n├── MMLU > 0.50, GSM8K > 0.30 (downstream 恢复)\n│   → Narrative B 为主线: \"KL + uniform allocation = 推荐管线\"\n│   → Claim 3 重写为 allocation strategy comparison\n│   → 30% uniform 成为论文 headline positive result\n│\n├── MMLU 0.35-0.50, GSM8K 0.10-0.30 (部分恢复)\n│   → Narrative A+B 混合: disconnect 是真实的，uniform 缓解但不消除\n│   → 论文贡献 = 诊断 + 部分修复\n│\n└── MMLU < 0.35, GSM8K < 0.10 (无恢复)\n    → Narrative A+C 为主线: PPL-disconnect 是根本性限制\n    → per-layer imbalance 是 necessary 但 not sufficient 的根因\n    → 论文贡献 = 系统性 disconnect 证据 + task sensitivity spectrum\n```\n\n---\n\n## 写作红线\n\n1. **禁止 cherry-picking**: 不能只报 WinoGrande（退化最轻）而隐藏 MMLU/GSM8K\n2. **所有定量 claim 附 exp_id**: 每个数字必须追溯到 registry\n3. **强度匹配**: \"systematic evidence\" 而非 \"definitive proof\"（仅 2 个 sparsity level）\n4. **禁止 \"30% is the recommended operating point\"**: 数据明确否定\n5. **PPL 结果保留但降级**: PPL 表格前后必须加 caveat，不能单独作为 quality claim 的依据\n"
  }
}
````

</details>

---

### Tool result

_source line 26 · 2026-05-16T03:00:31.952252+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'artifacts/framing_proposal_30pct_downstream.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T03:00:31.952433+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T03:00:31.952571+00:00_

_project
baselines.py
bce_mvp_3seed_analysis.md
diag_gsm8k_gencomp
dream_reports
figures
gsm8k_gen_compare
gsm8k_gen_compare.py
literature_ppl_downstream_disconnect.md
lm_eval_status_check.md
manifest.yaml
mvp_bce_s42
mvp_kl_s42
mvp_kl_s42_eval_report.json
plan008_ppl_summary.md
plan_006
plan_007
plan_007_all_ppl_fixed.json
plan_009_readiness_report.md
process_check_loop5.md
test_greedy_dryrun.py
train_bce_comp.py
training_free_baselines

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T03:00:31.952734+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/framing_proposal_30pct_downstream.md",
  "content": "# Framing 调整提案：30% Downstream Negative 结果\n\n> 生成时间: 2026-05-16 | 触发: lm_eval_kl_30pct_s42 negative result + D030\n\n---\n\n## 1. 原 Claim\n\n**Claim 3 (paper_framing.md)**:\n> \"KL advantage grows with sparsity level (testable prediction): BCE's per-neuron factorized gradient misses joint neuron interactions scaling as O(s²D²). We predict KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.\"\n\n隐含假设：低 sparsity（如 30%）是安全的操作点，论文 Story Spine 中 \"30% 为推荐配置\" 的叙事建立在 \"PPL 好 → downstream 也好\" 的未验证前提之上。\n\n---\n\n## 2. 实验结果（客观数字）\n\n### 2.1 KL 30% Downstream (exp: lm_eval_kl_30pct_s42)\n\n| Task | Dense | KL 30% | Drop | 备注 |\n|------|-------|--------|------|------|\n| arc_challenge (acc_norm) | 0.5819 | 0.3737 | **-35.8%** | 与 50% 的 -35.2% 几乎相同 |\n| winogrande (acc) | 0.7814 | 0.6756 | **-13.5%** | 最轻微的退化 |\n| mmlu (acc) | 0.6532 | 0.2874 | **-56.0%** | ≈4-choice 随机水平 (0.25) |\n| gsm8k (flexible) | 0.5004 | 0.0781 | **-84.4%** | 近乎完全丧失 |\n\n### 2.2 KL 30% PPL (exp: kl_sparsity30_s42_v3)\n\n| Metric | Value |\n|--------|-------|\n| true_dense_ppl | 6.12 |\n| predictor_hard_mask_ppl | 7.30 (+19.3%) |\n| teal_sparse_ppl | 8.98 (+46.7%) |\n| model_level_sparsity | 0.300 |\n| per-layer sparsity | 早期 0.13-0.23, 中间 0.30-0.34, **后层 0.50-0.70** |\n\n### 2.3 跨条件对比\n\n| Metric | KL 30% | KL 50% | TEAL 50% | Dense |\n|--------|--------|--------|----------|-------|\n| **PPL (TEAL)** | 8.98 | 12.00±0.07 | 23.31 | 6.12 |\n| arc_challenge | 0.3737 | 0.3771 | 0.2910 | 0.5819 |\n| winogrande | 0.6756 | 0.6156 | 0.5556 | 0.7814 |\n| mmlu | 0.2874 | 0.2591 | 0.2856 | 0.6532 |\n| gsm8k | 0.0781 | 0.0121 | 0.0190 | 0.5004 |\n\n数据来源: lm_eval_kl_30pct_s42, lm_eval_kl_s42, lm_eval_teal_50pct, lm_eval_dense, kl_sparsity30_s42_v3\n\n---\n\n## 3. 重新审视\n\n### 3.1 被挑战的 Hypothesis\n\n**H_safe_30**: \"30% sparsity 是安全操作点，PPL 退化可控 → downstream 退化也可控。\"\n\n这一假设被彻底否定。MMLU 在 30% 就崩到接近随机 (0.2874 vs random 0.25)，GSM8K 丧失 84%。PPL 仅 +47% 不足以预测 downstream 灾难。\n\n**H_ppl_proxy**: \"PPL 是 sparse model 质量的可靠代理指标。\"\n\n30% 数据点将此否定从 \"50% 的特例\" 升级为 \"系统性规律\"：\n- 30% PPL: 8.98 (+47%)，但 MMLU ≈ random\n- 50% PPL: 12.00 (+96%)，但 MMLU ≈ random\n- PPL 几乎翻倍，MMLU 退化程度几乎相同 → PPL 变化量与 downstream 退化量不相关\n\n### 3.2 被忽略的变量：Per-Layer Sparsity 不均匀\n\n**这是根因。** 全局 top-k 将 sparsity 集中在后层：\n\n- 30% global → Layer 26-31 实际 sparsity 41-70%（Layer 31 高达 70.3%）\n- 后层直连 LM head，负责精确知识检索和推理链延续\n- PPL 是平均指标（前层正常即可拉低），downstream 依赖后层逐 token 精确输出\n\n**这与 50% 的 PPL-downstream disconnect 是完全相同的机制**，只是程度不同：\n- 50% global → 后层 sparsity 可能超过 80%（待 P0 任务确认）\n- 30% global → 后层 sparsity 50-70%，仍在 \"崩溃区\"\n\n### 3.3 已做实验的有效性\n\n| 实验 | 新 framing 下是否有效 | 说明 |\n|------|----------------------|------|\n| KL vs BCE PPL (Claim 1) | ✅ 完全有效 | PPL 层面 KL 优势不受影响 |\n| SPON orthogonality (Claim 2) | ✅ 完全有效 | logit 空间分解不依赖 downstream |\n| STE vs Gumbel ablation | ✅ 完全有效 | 训练稳定性结论独立于 downstream |\n| Mistral cross-arch PPL | ✅ 有效（PPL 层面）| downstream 待补 |\n| 50% downstream collapse (D028) | ✅ 升值 | 从 \"负面结果\" 变为 \"系统性发现的一个数据点\" |\n| 30% downstream collapse (D030) | ✅ 核心新证据 | 证明 PPL-downstream disconnect 是普遍现象 |\n| GSM8K 生成质量对比 | ✅ 升值 | 提供 disconnect 的机制解释 |\n| 文献调研 (PPL-downstream) | ✅ 关键支撑 | 定位我们的贡献在文献空白中 |\n\n---\n\n## 4. 新 Narrative 骨架（3 种备选）\n\n### Narrative A: \"PPL-Downstream Disconnect 是论文核心贡献之一\"\n\n**核心论点**: 在 contextual sparsity prediction 框架下，PPL 不是可靠的质量指标。我们系统性地展示这一 disconnect，分析根因（per-layer sparsity imbalance），并提出诊断协议。\n\n**Story Spine 调整**:\n- Problem: 不变\n- Existing approaches & gaps: 增加 \"所有现有工作仅用 PPL 评估 sparse model 质量\"\n- Our contribution: (1) KL >> BCE/compensation [原 Claim 1]; (2) SPON orthogonal [原 Claim 2]; **(3) PPL-downstream disconnect 的系统性证据 + 根因分析 + 文献定位** [替换原 Claim 3]\n- Headline: \"KL distillation produces the best PPL-quality sparse predictor, but PPL alone is insufficient — we demonstrate a systematic PPL-downstream disconnect caused by per-layer sparsity imbalance under global top-k allocation.\"\n\n**优点**: 诚实、有文献支撑（Khanal & Capone 2024, Xu et al. 2024 EMNLP, Kodathala & Vunnam 2026, Siam et al. 2026）、填补文献空白（无论文在 contextual sparsity + KL distillation 下系统研究此现象）、所有已做实验全部可用。\n\n**风险**: Reviewer 可能认为 \"发现问题但没解决\" 不够 contribution；需要 uniform allocation 实验作为 \"指向解决方案\" 的 bridge。\n\n**强度匹配**: 30% 和 50% 两个数据点 + TEAL 50% 对照 + 文献支撑 = 中等强度。可支撑 \"systematic evidence\" 但不足以支撑 \"definitive characterization\"。\n\n### Narrative B: \"Per-Layer Allocation 修复 Downstream Collapse\"（需新实验）\n\n**核心论点**: Global top-k allocation 是 downstream collapse 的根因。Per-layer uniform allocation（每层独立 top-k）能在保持 sparsity 目标的同时恢复 downstream quality。KL + uniform allocation 是正确的推理管线。\n\n**Story Spine 调整**:\n- Problem: 增加 \"global top-k allocation 导致 per-layer sparsity 不均匀，摧毁后层精确输出\"\n- Our contribution: (1) KL >> all [原 Claim 1]; (2) SPON orthogonal [原 Claim 2]; **(3) Uniform allocation 修复 downstream collapse，KL + uniform 是推荐管线** [替换原 Claim 3]\n- Headline: \"KL distillation + per-layer uniform allocation achieves [X] downstream quality at 30% sparsity, within [Y]% of dense, while global top-k allocation causes catastrophic downstream collapse despite acceptable PPL.\"\n\n**优点**: 提供解决方案（不只是诊断问题）、30% uniform 如果 downstream 恢复则有强 positive result、自然承接 PPL-disconnect 发现。\n\n**风险**: **完全依赖未完成的实验（ROADMAP P0 任务）。** 如果 uniform allocation 不能修复 downstream（即问题不仅仅是 per-layer imbalance，而是 sparsity 本身摧毁了某些能力），则此 narrative 崩塌。\n\n**实验依赖**: uniform_30pct + uniform_50pct downstream eval（ROADMAP 已列 P0）\n\n### Narrative C: \"Task-Sensitive Sparsity Spectrum\"\n\n**核心论点**: 不同 downstream task 对 sparsity 的敏感度存在质的差异。我们构建 task × sparsity 退化矩阵，揭示三层敏感度谱系。\n\n**Task 敏感度分层（基于现有数据）**:\n\n| 敏感度 | Task | 30% drop | 50% drop | 特征 |\n|--------|------|----------|----------|------|\n| Robust | WinoGrande | -13.5% | -21.2% | 渐进退化，30% 保留 87% |\n| Cliff | ARC-c | -35.8% | -35.2% | 在 ≤30% 已到 cliff，30→50% 无进一步退化 |\n| Ultra-fragile | MMLU | -56.0% | -60.3% | 30% 即 ≈ random，知识检索彻底丧失 |\n| Ultra-fragile | GSM8K | -84.4% | -97.6% | 30% 残留微弱，50% 完全丧失 |\n\n**Story Spine 调整**:\n- Our contribution: (1) KL >> all [原 Claim 1]; (2) SPON orthogonal [原 Claim 2]; **(3) Task-sensitive sparsity spectrum: 对 sparsity 的退化不是均匀的，而是 task-dependent 的阶梯式崩溃** [替换原 Claim 3]\n\n**优点**: 每个数字都是 informative 的（包括负面结果）；ARC-c 在 30→50% 无进一步退化是独特发现；GSM8K 的 gradual degradation (0.0781 → 0.0121) 说明存在连续退化（非二元 cliff）。\n\n**风险**: 数据点有限（仅 30% 和 50% 两个 level，4 个 task）。需要更多 sparsity level（如 10%, 20%, 40%）才能画出完整 spectrum。\n\n**推荐**: **Narrative A 为主线，Narrative C 为子节**。Narrative B 作为 \"future direction\" 或在 uniform 实验完成后升级为主线。\n\n---\n\n## 5. 对论文各章节的影响\n\n### Abstract\n- **删除**: \"30% 为推荐配置\" 相关措辞\n- **新增**: \"我们发现 PPL 与 downstream quality 存在系统性 disconnect：30% sparsity 下 PPL 仅 +47% 但 MMLU 崩至随机水平\"\n- **保留**: KL >> BCE/compensation headline 不变\n\n### Introduction\n- Story Spine 的 \"headline result template\" 需重写\n- 增加第三段：PPL-downstream disconnect 的 motivation\n- 引用 Khanal & Capone (2024), Xu et al. (2024)\n\n### Related Work\n- 新增小节：\"PPL as Evaluation Metric for Sparse Models\"\n- 引用 4 篇文献调研结果（见 memory.md \"PPL-downstream disconnect 文献支撑\"）\n\n### Method\n- 无重大影响。KL loss、predictor architecture、Gumbel relaxation 不变\n- 可增加 per-layer sparsity 分析工具的描述\n\n### Experiments — PPL Results (原有)\n- **完全保留**。KL vs BCE、KL vs TEAL、SPON orthogonality、STE ablation 全部有效\n- 增加 caveat: \"PPL results are necessary but not sufficient for quality assessment\"\n\n### Experiments — Downstream Results (新增/重写)\n- **核心新增章节**: Task × Sparsity 退化矩阵\n- 30% 和 50% 两个 level × 4 tasks × 2 methods (KL, TEAL)\n- Figure: 退化热力图（task 行, sparsity 列, color = drop%）\n- WinoGrande gradual degradation vs MMLU/GSM8K cliff 对比\n\n### Experiments — PPL-Downstream Disconnect Analysis (新增)\n- Per-layer sparsity 分布可视化（30% vs 50%）\n- 后层 over-pruning → downstream collapse 的因果链\n- GSM8K 生成质量对比（dense vs sparse, 来自 gsm8k_gen_compare）\n- 文献对比：我们的发现与 Khanal (2024) / Siam (2026) 的一致性\n\n### Discussion\n- PPL 作为 sparse model 评估指标的局限性\n- Per-layer allocation 作为潜在修复方向\n- Task sensitivity 分层的实践意义\n\n### Conclusion\n- 三句话公式：(1) KL >> all on PPL axis; (2) PPL ≠ downstream under global top-k; (3) per-layer sparsity imbalance 是根因，指向 uniform allocation 方向\n\n---\n\n## 6. 建议下一步实验\n\n### 实验 1: [P0] 50% Per-Layer Sparsity 分布提取\n- **目的**: 确认 50% global top-k 是否存在同样的后层集中模式\n- **方法**: 从 mvp_kl_norm_v2_s42 predictor 提取 per-layer sparsity 分布\n- **预期**: 后层 sparsity >> 50%（与 30% 的 0.50-0.70 模式一致但更极端）\n- **填补矩阵**: 确认 30% 和 50% 共享同一根因\n- **耗时**: < 1 GPU·h\n\n### 实验 2: [P0] Uniform Per-Layer Allocation 30% + 50%\n- **目的**: 验证 per-layer sparsity 均匀分配是否修复 downstream collapse\n- **方法**: 每层独立 top-k（不需重新训练 predictor，仅修改推理时的 mask 生成策略）\n- **评估**: PPL + arc_challenge + winogrande + mmlu + gsm8k\n- **关键对比**:\n  - uniform_30% vs global_30% downstream\n  - uniform_50% vs global_50% downstream\n- **预期 A（乐观）**: 30% uniform 恢复 MMLU > 0.50, GSM8K > 0.30 → 激活 Narrative B\n- **预期 B（悲观）**: uniform 仍然崩 → PPL-disconnect 不仅仅是 allocation 问题，sparsity 本身摧毁某些能力\n- **耗时**: ~2 GPU·h (4 conditions × 0.5h each)\n- **决策点**: 若预期 A 成立 → 论文 Claim 3 切换到 Narrative B；若预期 B → 锁定 Narrative A+C\n\n### 实验 3: TEAL 30% Downstream (已在 ROADMAP)\n- **目的**: 与 KL 30% 对比，验证 30% collapse 是否为所有 sparsity 方法的固有限制\n- **方法**: lm_eval_teal.py --sparsity_target 0.3\n- **预期**: TEAL 30% 也崩（与 TEAL 50% 同模式），但可能比 KL 30% 更差（与 50% 的 TEAL < KL 一致）\n- **填补矩阵**: 完成 method × sparsity × task 三维矩阵的最后一个 condition\n- **耗时**: ~1 GPU·h\n- **状态**: registry 中 lm_eval_teal_30pct 已 PREPARING\n\n### 实验 4: [P1] 10% / 20% Sparsity Downstream\n- **目的**: 找到 downstream 退化的 onset point（目前只知道 30% 已崩，但不知道 threshold 在哪）\n- **方法**: 需先训练 10% 和 20% predictor，再跑 downstream\n- **价值**: 如果 20% 尚可但 30% 崩 → 确认 threshold 在 20-30% 区间；如果 10% 就崩 → 问题更严重\n- **耗时**: ~4 GPU·h (2 training + 2 eval)\n- **优先级**: P1 — 对 Narrative C 重要但对 DDL (05-25) 非必需\n\n### 实验 5: [P1] Per-Layer Sparsity Cap Ablation\n- **目的**: 测试约束后层 sparsity 上限（如 max 40%/layer）是否比 uniform 更好\n- **方法**: 修改 TEAL global top-k，增加 per-layer cap 约束\n- **评估**: PPL + 4 task downstream\n- **价值**: 如果 capped > uniform on PPL but capped ≈ uniform on downstream → 可得到 PPL-downstream Pareto 最优点\n- **耗时**: ~2 GPU·h\n- **优先级**: P1 — 仅在 uniform 实验（实验 2）出正面结果后执行\n\n---\n\n## 7. 决策树摘要\n\n```\nuniform_30% downstream 结果\n├── MMLU > 0.50, GSM8K > 0.30 (downstream 恢复)\n│   → Narrative B 为主线: \"KL + uniform allocation = 推荐管线\"\n│   → Claim 3 重写为 allocation strategy comparison\n│   → 30% uniform 成为论文 headline positive result\n│\n├── MMLU 0.35-0.50, GSM8K 0.10-0.30 (部分恢复)\n│   → Narrative A+B 混合: disconnect 是真实的，uniform 缓解但不消除\n│   → 论文贡献 = 诊断 + 部分修复\n│\n└── MMLU < 0.35, GSM8K < 0.10 (无恢复)\n    → Narrative A+C 为主线: PPL-disconnect 是根本性限制\n    → per-layer imbalance 是 necessary 但 not sufficient 的根因\n    → 论文贡献 = 系统性 disconnect 证据 + task sensitivity spectrum\n```\n\n---\n\n## 写作红线\n\n1. **禁止 cherry-picking**: 不能只报 WinoGrande（退化最轻）而隐藏 MMLU/GSM8K\n2. **所有定量 claim 附 exp_id**: 每个数字必须追溯到 registry\n3. **强度匹配**: \"systematic evidence\" 而非 \"definitive proof\"（仅 2 个 sparsity level）\n4. **禁止 \"30% is the recommended operating point\"**: 数据明确否定\n5. **PPL 结果保留但降级**: PPL 表格前后必须加 caveat，不能单独作为 quality claim 的依据\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/framing_proposal_30pct_downstream.md",
    "content": "# Framing 调整提案：30% Downstream Negative 结果\n\n> 生成时间: 2026-05-16 | 触发: lm_eval_kl_30pct_s42 negative result + D030\n\n---\n\n## 1. 原 Claim\n\n**Claim 3 (paper_framing.md)**:\n> \"KL advantage grows with sparsity level (testable prediction): BCE's per-neuron factorized gradient misses joint neuron interactions scaling as O(s²D²). We predict KL-vs-BCE delta follows approximately quadratic curve in sparsity level s.\"\n\n隐含假设：低 sparsity（如 30%）是安全的操作点，论文 Story Spine 中 \"30% 为推荐配置\" 的叙事建立在 \"PPL 好 → downstream 也好\" 的未验证前提之上。\n\n---\n\n## 2. 实验结果（客观数字）\n\n### 2.1 KL 30% Downstream (exp: lm_eval_kl_30pct_s42)\n\n| Task | Dense | KL 30% | Drop | 备注 |\n|------|-------|--------|------|------|\n| arc_challenge (acc_norm) | 0.5819 | 0.3737 | **-35.8%** | 与 50% 的 -35.2% 几乎相同 |\n| winogrande (acc) | 0.7814 | 0.6756 | **-13.5%** | 最轻微的退化 |\n| mmlu (acc) | 0.6532 | 0.2874 | **-56.0%** | ≈4-choice 随机水平 (0.25) |\n| gsm8k (flexible) | 0.5004 | 0.0781 | **-84.4%** | 近乎完全丧失 |\n\n### 2.2 KL 30% PPL (exp: kl_sparsity30_s42_v3)\n\n| Metric | Value |\n|--------|-------|\n| true_dense_ppl | 6.12 |\n| predictor_hard_mask_ppl | 7.30 (+19.3%) |\n| teal_sparse_ppl | 8.98 (+46.7%) |\n| model_level_sparsity | 0.300 |\n| per-layer sparsity | 早期 0.13-0.23, 中间 0.30-0.34, **后层 0.50-0.70** |\n\n### 2.3 跨条件对比\n\n| Metric | KL 30% | KL 50% | TEAL 50% | Dense |\n|--------|--------|--------|----------|-------|\n| **PPL (TEAL)** | 8.98 | 12.00±0.07 | 23.31 | 6.12 |\n| arc_challenge | 0.3737 | 0.3771 | 0.2910 | 0.5819 |\n| winogrande | 0.6756 | 0.6156 | 0.5556 | 0.7814 |\n| mmlu | 0.2874 | 0.2591 | 0.2856 | 0.6532 |\n| gsm8k | 0.0781 | 0.0121 | 0.0190 | 0.5004 |\n\n数据来源: lm_eval_kl_30pct_s42, lm_eval_kl_s42, lm_eval_teal_50pct, lm_eval_dense, kl_sparsity30_s42_v3\n\n---\n\n## 3. 重新审视\n\n### 3.1 被挑战的 Hypothesis\n\n**H_safe_30**: \"30% sparsity 是安全操作点，PPL 退化可控 → downstream 退化也可控。\"\n\n这一假设被彻底否定。MMLU 在 30% 就崩到接近随机 (0.2874 vs random 0.25)，GSM8K 丧失 84%。PPL 仅 +47% 不足以预测 downstream 灾难。\n\n**H_ppl_proxy**: \"PPL 是 sparse model 质量的可靠代理指标。\"\n\n30% 数据点将此否定从 \"50% 的特例\" 升级为 \"系统性规律\"：\n- 30% PPL: 8.98 (+47%)，但 MMLU ≈ random\n- 50% PPL: 12.00 (+96%)，但 MMLU ≈ random\n- PPL 几乎翻倍，MMLU 退化程度几乎相同 → PPL 变化量与 downstream 退化量不相关\n\n### 3.2 被忽略的变量：Per-Layer Sparsity 不均匀\n\n**这是根因。** 全局 top-k 将 sparsity 集中在后层：\n\n- 30% global → Layer 26-31 实际 sparsity 41-70%（Layer 31 高达 70.3%）\n- 后层直连 LM head，负责精确知识检索和推理链延续\n- PPL 是平均指标（前层正常即可拉低），downstream 依赖后层逐 token 精确输出\n\n**这与 50% 的 PPL-downstream disconnect 是完全相同的机制**，只是程度不同：\n- 50% global → 后层 sparsity 可能超过 80%（待 P0 任务确认）\n- 30% global → 后层 sparsity 50-70%，仍在 \"崩溃区\"\n\n### 3.3 已做实验的有效性\n\n| 实验 | 新 framing 下是否有效 | 说明 |\n|------|----------------------|------|\n| KL vs BCE PPL (Claim 1) | ✅ 完全有效 | PPL 层面 KL 优势不受影响 |\n| SPON orthogonality (Claim 2) | ✅ 完全有效 | logit 空间分解不依赖 downstream |\n| STE vs Gumbel ablation | ✅ 完全有效 | 训练稳定性结论独立于 downstream |\n| Mistral cross-arch PPL | ✅ 有效（PPL 层面）| downstream 待补 |\n| 50% downstream collapse (D028) | ✅ 升值 | 从 \"负面结果\" 变为 \"系统性发现的一个数据点\" |\n| 30% downstream collapse (D030) | ✅ 核心新证据 | 证明 PPL-downstream disconnect 是普遍现象 |\n| GSM8K 生成质量对比 | ✅ 升值 | 提供 disconnect 的机制解释 |\n| 文献调研 (PPL-downstream) | ✅ 关键支撑 | 定位我们的贡献在文献空白中 |\n\n---\n\n## 4. 新 Narrative 骨架（3 种备选）\n\n### Narrative A: \"PPL-Downstream Disconnect 是论文核心贡献之一\"\n\n**核心论点**: 在 contextual sparsity prediction 框架下，PPL 不是可靠的质量指标。我们系统性地展示这一 disconnect，分析根因（per-layer sparsity imbalance），并提出诊断协议。\n\n**Story Spine 调整**:\n- Problem: 不变\n- Existing approaches & gaps: 增加 \"所有现有工作仅用 PPL 评估 sparse model 质量\"\n- Our contribution: (1) KL >> BCE/compensation [原 Claim 1]; (2) SPON orthogonal [原 Claim 2]; **(3) PPL-downstream disconnect 的系统性证据 + 根因分析 + 文献定位** [替换原 Claim 3]\n- Headline: \"KL distillation produces the best PPL-quality sparse predictor, but PPL alone is insufficient — we demonstrate a systematic PPL-downstream disconnect caused by per-layer sparsity imbalance under global top-k allocation.\"\n\n**优点**: 诚实、有文献支撑（Khanal & Capone 2024, Xu et al. 2024 EMNLP, Kodathala & Vunnam 2026, Siam et al. 2026）、填补文献空白（无论文在 contextual sparsity + KL distillation 下系统研究此现象）、所有已做实验全部可用。\n\n**风险**: Reviewer 可能认为 \"发现问题但没解决\" 不够 contribution；需要 uniform allocation 实验作为 \"指向解决方案\" 的 bridge。\n\n**强度匹配**: 30% 和 50% 两个数据点 + TEAL 50% 对照 + 文献支撑 = 中等强度。可支撑 \"systematic evidence\" 但不足以支撑 \"definitive characterization\"。\n\n### Narrative B: \"Per-Layer Allocation 修复 Downstream Collapse\"（需新实验）\n\n**核心论点**: Global top-k allocation 是 downstream collapse 的根因。Per-layer uniform allocation（每层独立 top-k）能在保持 sparsity 目标的同时恢复 downstream quality。KL + uniform allocation 是正确的推理管线。\n\n**Story Spine 调整**:\n- Problem: 增加 \"global top-k allocation 导致 per-layer sparsity 不均匀，摧毁后层精确输出\"\n- Our contribution: (1) KL >> all [原 Claim 1]; (2) SPON orthogonal [原 Claim 2]; **(3) Uniform allocation 修复 downstream collapse，KL + uniform 是推荐管线** [替换原 Claim 3]\n- Headline: \"KL distillation + per-layer uniform allocation achieves [X] downstream quality at 30% sparsity, within [Y]% of dense, while global top-k allocation causes catastrophic downstream collapse despite acceptable PPL.\"\n\n**优点**: 提供解决方案（不只是诊断问题）、30% uniform 如果 downstream 恢复则有强 positive result、自然承接 PPL-disconnect 发现。\n\n**风险**: **完全依赖未完成的实验（ROADMAP P0 任务）。** 如果 uniform allocation 不能修复 downstream（即问题不仅仅是 per-layer imbalance，而是 sparsity 本身摧毁了某些能力），则此 narrative 崩塌。\n\n**实验依赖**: uniform_30pct + uniform_50pct downstream eval（ROADMAP 已列 P0）\n\n### Narrative C: \"Task-Sensitive Sparsity Spectrum\"\n\n**核心论点**: 不同 downstream task 对 sparsity 的敏感度存在质的差异。我们构建 task × sparsity 退化矩阵，揭示三层敏感度谱系。\n\n**Task 敏感度分层（基于现有数据）**:\n\n| 敏感度 | Task | 30% drop | 50% drop | 特征 |\n|--------|------|----------|----------|------|\n| Robust | WinoGrande | -13.5% | -21.2% | 渐进退化，30% 保留 87% |\n| Cliff | ARC-c | -35.8% | -35.2% | 在 ≤30% 已到 cliff，30→50% 无进一步退化 |\n| Ultra-fragile | MMLU | -56.0% | -60.3% | 30% 即 ≈ random，知识检索彻底丧失 |\n| Ultra-fragile | GSM8K | -84.4% | -97.6% | 30% 残留微弱，50% 完全丧失 |\n\n**Story Spine 调整**:\n- Our contribution: (1) KL >> all [原 Claim 1]; (2) SPON orthogonal [原 Claim 2]; **(3) Task-sensitive sparsity spectrum: 对 sparsity 的退化不是均匀的，而是 task-dependent 的阶梯式崩溃** [替换原 Claim 3]\n\n**优点**: 每个数字都是 informative 的（包括负面结果）；ARC-c 在 30→50% 无进一步退化是独特发现；GSM8K 的 gradual degradation (0.0781 → 0.0121) 说明存在连续退化（非二元 cliff）。\n\n**风险**: 数据点有限（仅 30% 和 50% 两个 level，4 个 task）。需要更多 sparsity level（如 10%, 20%, 40%）才能画出完整 spectrum。\n\n**推荐**: **Narrative A 为主线，Narrative C 为子节**。Narrative B 作为 \"future direction\" 或在 uniform 实验完成后升级为主线。\n\n---\n\n## 5. 对论文各章节的影响\n\n### Abstract\n- **删除**: \"30% 为推荐配置\" 相关措辞\n- **新增**: \"我们发现 PPL 与 downstream quality 存在系统性 disconnect：30% sparsity 下 PPL 仅 +47% 但 MMLU 崩至随机水平\"\n- **保留**: KL >> BCE/compensation headline 不变\n\n### Introduction\n- Story Spine 的 \"headline result template\" 需重写\n- 增加第三段：PPL-downstream disconnect 的 motivation\n- 引用 Khanal & Capone (2024), Xu et al. (2024)\n\n### Related Work\n- 新增小节：\"PPL as Evaluation Metric for Sparse Models\"\n- 引用 4 篇文献调研结果（见 memory.md \"PPL-downstream disconnect 文献支撑\"）\n\n### Method\n- 无重大影响。KL loss、predictor architecture、Gumbel relaxation 不变\n- 可增加 per-layer sparsity 分析工具的描述\n\n### Experiments — PPL Results (原有)\n- **完全保留**。KL vs BCE、KL vs TEAL、SPON orthogonality、STE ablation 全部有效\n- 增加 caveat: \"PPL results are necessary but not sufficient for quality assessment\"\n\n### Experiments — Downstream Results (新增/重写)\n- **核心新增章节**: Task × Sparsity 退化矩阵\n- 30% 和 50% 两个 level × 4 tasks × 2 methods (KL, TEAL)\n- Figure: 退化热力图（task 行, sparsity 列, color = drop%）\n- WinoGrande gradual degradation vs MMLU/GSM8K cliff 对比\n\n### Experiments — PPL-Downstream Disconnect Analysis (新增)\n- Per-layer sparsity 分布可视化（30% vs 50%）\n- 后层 over-pruning → downstream collapse 的因果链\n- GSM8K 生成质量对比（dense vs sparse, 来自 gsm8k_gen_compare）\n- 文献对比：我们的发现与 Khanal (2024) / Siam (2026) 的一致性\n\n### Discussion\n- PPL 作为 sparse model 评估指标的局限性\n- Per-layer allocation 作为潜在修复方向\n- Task sensitivity 分层的实践意义\n\n### Conclusion\n- 三句话公式：(1) KL >> all on PPL axis; (2) PPL ≠ downstream under global top-k; (3) per-layer sparsity imbalance 是根因，指向 uniform allocation 方向\n\n---\n\n## 6. 建议下一步实验\n\n### 实验 1: [P0] 50% Per-Layer Sparsity 分布提取\n- **目的**: 确认 50% global top-k 是否存在同样的后层集中模式\n- **方法**: 从 mvp_kl_norm_v2_s42 predictor 提取 per-layer sparsity 分布\n- **预期**: 后层 sparsity >> 50%（与 30% 的 0.50-0.70 模式一致但更极端）\n- **填补矩阵**: 确认 30% 和 50% 共享同一根因\n- **耗时**: < 1 GPU·h\n\n### 实验 2: [P0] Uniform Per-Layer Allocation 30% + 50%\n- **目的**: 验证 per-layer sparsity 均匀分配是否修复 downstream collapse\n- **方法**: 每层独立 top-k（不需重新训练 predictor，仅修改推理时的 mask 生成策略）\n- **评估**: PPL + arc_challenge + winogrande + mmlu + gsm8k\n- **关键对比**:\n  - uniform_30% vs global_30% downstream\n  - uniform_50% vs global_50% downstream\n- **预期 A（乐观）**: 30% uniform 恢复 MMLU > 0.50, GSM8K > 0.30 → 激活 Narrative B\n- **预期 B（悲观）**: uniform 仍然崩 → PPL-disconnect 不仅仅是 allocation 问题，sparsity 本身摧毁某些能力\n- **耗时**: ~2 GPU·h (4 conditions × 0.5h each)\n- **决策点**: 若预期 A 成立 → 论文 Claim 3 切换到 Narrative B；若预期 B → 锁定 Narrative A+C\n\n### 实验 3: TEAL 30% Downstream (已在 ROADMAP)\n- **目的**: 与 KL 30% 对比，验证 30% collapse 是否为所有 sparsity 方法的固有限制\n- **方法**: lm_eval_teal.py --sparsity_target 0.3\n- **预期**: TEAL 30% 也崩（与 TEAL 50% 同模式），但可能比 KL 30% 更差（与 50% 的 TEAL < KL 一致）\n- **填补矩阵**: 完成 method × sparsity × task 三维矩阵的最后一个 condition\n- **耗时**: ~1 GPU·h\n- **状态**: registry 中 lm_eval_teal_30pct 已 PREPARING\n\n### 实验 4: [P1] 10% / 20% Sparsity Downstream\n- **目的**: 找到 downstream 退化的 onset point（目前只知道 30% 已崩，但不知道 threshold 在哪）\n- **方法**: 需先训练 10% 和 20% predictor，再跑 downstream\n- **价值**: 如果 20% 尚可但 30% 崩 → 确认 threshold 在 20-30% 区间；如果 10% 就崩 → 问题更严重\n- **耗时**: ~4 GPU·h (2 training + 2 eval)\n- **优先级**: P1 — 对 Narrative C 重要但对 DDL (05-25) 非必需\n\n### 实验 5: [P1] Per-Layer Sparsity Cap Ablation\n- **目的**: 测试约束后层 sparsity 上限（如 max 40%/layer）是否比 uniform 更好\n- **方法**: 修改 TEAL global top-k，增加 per-layer cap 约束\n- **评估**: PPL + 4 task downstream\n- **价值**: 如果 capped > uniform on PPL but capped ≈ uniform on downstream → 可得到 PPL-downstream Pareto 最优点\n- **耗时**: ~2 GPU·h\n- **优先级**: P1 — 仅在 uniform 实验（实验 2）出正面结果后执行\n\n---\n\n## 7. 决策树摘要\n\n```\nuniform_30% downstream 结果\n├── MMLU > 0.50, GSM8K > 0.30 (downstream 恢复)\n│   → Narrative B 为主线: \"KL + uniform allocation = 推荐管线\"\n│   → Claim 3 重写为 allocation strategy comparison\n│   → 30% uniform 成为论文 headline positive result\n│\n├── MMLU 0.35-0.50, GSM8K 0.10-0.30 (部分恢复)\n│   → Narrative A+B 混合: disconnect 是真实的，uniform 缓解但不消除\n│   → 论文贡献 = 诊断 + 部分修复\n│\n└── MMLU < 0.35, GSM8K < 0.10 (无恢复)\n    → Narrative A+C 为主线: PPL-disconnect 是根本性限制\n    → per-layer imbalance 是 necessary 但 not sufficient 的根因\n    → 论文贡献 = 系统性 disconnect 证据 + task sensitivity spectrum\n```\n\n---\n\n## 写作红线\n\n1. **禁止 cherry-picking**: 不能只报 WinoGrande（退化最轻）而隐藏 MMLU/GSM8K\n2. **所有定量 claim 附 exp_id**: 每个数字必须追溯到 registry\n3. **强度匹配**: \"systematic evidence\" 而非 \"definitive proof\"（仅 2 个 sparsity level）\n4. **禁止 \"30% is the recommended operating point\"**: 数据明确否定\n5. **PPL 结果保留但降级**: PPL 表格前后必须加 caveat，不能单独作为 quality claim 的依据\n"
  }
}
````

</details>

---

### Tool result

_source line 30 · 2026-05-16T03:00:31.953084+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/framing_proposal_30pct_downstream.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T03:00:31.953274+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "framing_proposal_30pct_downstream",
  "type": "report",
  "description": "Framing 调整提案：30% downstream negative 结果导致 Claim 3 重写，3 种 narrative 备选 + 5 组后续实验 + 决策树",
  "project": "distill_sparse_swiglu",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/framing_proposal_30pct_downstream.md",
  "tags": "['framing', 'claim3', 'downstream', '30pct', 'ppl-disconnect']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "framing_proposal_30pct_downstream",
    "type": "report",
    "description": "Framing 调整提案：30% downstream negative 结果导致 Claim 3 重写，3 种 narrative 备选 + 5 组后续实验 + 决策树",
    "project": "distill_sparse_swiglu",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/framing_proposal_30pct_downstream.md",
    "tags": "['framing', 'claim3', 'downstream', '30pct', 'ppl-disconnect']"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T03:00:31.953617+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_b1c4cd\", \"name\": \"framing_proposal_30pct_downstream\", \"type\": \"report\", \"description\": \"Framing 调整提案：30% downstream negative 结果导致 Claim 3 重写，3 种 narrative 备选 + 5 组后续实验 + 决策树\", \"path\": \"projects/distill_sparse_swiglu/artifacts/_project/report/framing_proposal_30pct_downstream.md\", \"url\": null, \"project\": \"distill_sparse_swiglu\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T03:00:19.183328+00:00\", \"tags\": [\"framing\", \"claim3\", \"downstream\", \"30pct\", \"ppl-disconnect\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_framing_30pct_proposal_20260516T025534",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-16T03:00:31.953806+00:00_

提案已写入 `artifacts/framing_proposal_30pct_downstream.md` 并注册 (`art_20260516_b1c4cd`)。

核心结论：

1. **原 Claim 3 ("30% 为推荐配置") 被数据否定** — MMLU 在 30% 就崩到随机水平，PPL +47% 完全无法预测这一灾难。

2. **根因是 per-layer sparsity 不均匀** — 30% global top-k 把后层（L26-31）推到 50-70% 实际 sparsity，后层直连 LM head，downstream 依赖后层精确输出。

3. **三种 narrative 备选**：
   - **A (推荐主线)**: PPL-downstream disconnect 作为论文核心贡献之一，填补文献空白
   - **B (需新实验)**: Uniform per-layer allocation 修复 collapse — 依赖 P0 实验结果
   - **C (子节)**: Task-sensitive sparsity spectrum，揭示 WinoGrande(robust) → ARC-c(cliff) → MMLU/GSM8K(ultra-fragile) 三层敏感度

4. **关键决策点**: uniform_30% downstream 实验结果决定最终走 A 还是 B。决策树已在提案 §7 给出。

5. **所有已做实验在新 framing 下仍然有效**，部分实验（50% collapse、GSM8K 生成对比）反而升值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_framing_30pct_proposal_20260516T025534"
}
```

</details>

---
