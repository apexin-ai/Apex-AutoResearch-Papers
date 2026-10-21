# analysis negative results insight

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_analysis_negative-results-insight_20260524T183247.jsonl`
- **Structured JSON:** [`f84bcd0dbaddfff6700b.json`](../../sessions/f8/f84bcd0dbaddfff6700b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

27 recorded events

### Tool call

_source line 1 · 2026-05-24T18:37:45.289490+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T18:37:45.289851+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T18:37:45.290048+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'conclusion': 'negative'}",
  "fields": "['*']",
  "project": "event-gated-adaptive-horizon",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'conclusion': 'negative'}",
    "fields": "['*']",
    "project": "event-gated-adaptive-horizon",
    "limit": "0"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-24T18:37:45.290190+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-24T18:37:45.290681+00:00_

Error: result (98,699 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/a16e8b93-bce8-4579-82f0-52ee2e183f79/tool-results/mcp-agent-ml-research-read_registry-1779647587226.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/a16e8b93-bce8-4579-82f0-52ee2e183f79/tool-results/mcp-agent-ml-research-read_registry-1779647587226.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T18:37:45.290921+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/memory.md\", \"content\": \"# Memory — event-gated-adaptive-horizon\\n\\n## 基线定义（2026-05-24 确认）\\n- **NVE 计算用 step-matched single-seed s1 baseline**（exp_001 seed=1），不是 4-seed mean\\n- exp_001 s1 baseline ve_ratio 随 step 变化：0.331@45K, 0.7007@85K, 0.683@115K, 0.656@105K\\n- methodology.tex 说 single-seed s1，appendix.tex:268 已统一为 single-seed s1\\n- 之前用 4-seed mean (0.683) 做的 backfill NVE 全部错误，已回滚标记 \\\"backfill_error, see M027\\\"\\n\\n## Walker trained seeds 实际清单（2026-05-24 审计）\\n- 5 个唯一 seed，不是 6 个\\n- s1: exp_008d_subsample_on_h8 = exp_009e（同一个 seed=1 run，不要双算）\\n- s2: exp_009b_008d_walker_s2 (seed=2)\\n- s3: exp_008d_civo_trigger_s3 (seed=3)\\n- s4: exp_008d_civo_trigger_s4 (seed=4)\\n- s5: exp_059_walker_trained_s5 (seed=5)\\n\\n## exp_059 (Walker s5) 分类（2026-05-24）\\n- NVE peak: 4.72× @85K（step-matched s1 baseline 0.7007）\\n- NVE final: 1.22× @105K（baseline 0.656）\\n- 分类: onset_collapse（Collapse†）\\n- 原因: NVE 自修正（4.72→1.22×）但 eval=95.8（baseline 913 的 10.5%），策略不可逆损伤\\n- 与 s1 collapse (9.0%) 和 s4 (6.9%) 同一水平\\n- s2 是唯一真正 self-correction 的 seed（eval 268 = 29.4% baseline）\\n\\n## Onset/Outcome 统计（2026-05-24）\\n- Onset: 7/7 locomotion trained seeds（5 Walker + 2 Cheetah）\\n- Outcome: 6/7 collapse, 1/7 self-correction (s2 only)\\n- Frozen: 0/5 onset\\n\\n## AUROC 处理原则（2026-05-24 Director 决策）\\n- AUROC=0.953 基于原始 4-seed 验证集（008d/009b/008f/009c），不因 s5 重算\\n- s5 不在验证集内，加入是 post-hoc 改测试集\\n- IQM/mean/intervention table 分母/detector TPR-FPR 同理不变\\n- n=29→30 和 26/29→27/30 是确定性更新（s5 正确分类为 CIVO-positive）\\n\\n## 竞品实验参考\\n（待补充）\\n\", \"total_chars\": 1433, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T18:37:45.291095+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/negative_results_taxonomy.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/negative_results_taxonomy.md"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T18:37:45.291299+00:00_

1	# Negative Results 分类清单
2	
3	总计：**35** 个 negative 实验
4	
5	## 分类总览
6	
7	| 类别 | 数量 | 占比 | 代表实验 |
8	|------|------|------|----------|
9	| TCN 跨环境/剂量失败 | 10 | 28.6% | exp_030a (Cheetah σ=0.2), exp_031 (PickCube σ=0.2) |
10	| SGS 干预失败 | 5 | 14.3% | exp_016e (reward-head SGS), exp_018_s2 (full-SGS seed 2) |
11	| Dual-critic / Wide-critic 跨环境失败 | 5 | 14.3% | exp_034 (Cheetah dual-critic), exp_038 (Walker s2 non-CIVO collapse) |
12	| dt>1 本身退化 | 5 | 14.3% | exp_007 (fixed dt=4), exp_008f_s4 (no-dt-emb control) |
13	| CIVO 复现/表征（诊断性 negative） | 4 | 11.4% | exp_009e (CIVO collapse confirmed), exp_008e_v3_s3 (stochastic collapse) |
14	| Event-gate 机制失败 | 3 | 8.6% | exp_005 (v4 collapse @85K) |
15	| RAVE 干预失败 | 2 | 5.7% | exp_028 (ceiling=2.0), exp_028_ceil15 (ceiling=1.5) |
16	| Frozen dt_emb 失败 | 1 | 2.9% | exp_015b (gradient starvation) |
17	
18	---
19	
20	## 详细分组
21	
22	### 类别 1：TCN 跨环境/剂量失败（10 个）
23	
24	TCN (Temporal Conditioning Noise) 在 Walker σ=0.2 上成功，但在其他环境或剂量下普遍失败。
25	
26	| exp_id | hypothesis | 环境 | 关键指标 | 简要结论 |
27	|--------|-----------|------|----------|----------|
28	| exp_027_tcn_walker_s0 | TCN σ=0.5 抑制 CIVO | Walker | eval peak 240@35K, oscillatory; eval_105K=95.5 | σ=0.5 过量：NVE 一度自修正但后续震荡性 CIVO，eval 大幅波动 |
29	| exp_027_tcn_walker_s1 | TCN σ=0.5 seed 1 复现 | Walker | eval peak 364.9@75K, last10 mean 233.1 | σ=0.5 跨 seed 不稳定，eval 振幅大（94.6–364.9），不可靠 |
30	| exp_029b_tcn_walker_s2_sigma02 | TCN σ=0.2 seed 2 方差表征 | Walker | eval peak 177.67@55K, CIVO onset @65K | s0=91% s1=45% s2=collapsed。σ=0.2 在 Walker 上高方差，2/4 seeds 仍崩溃 |
31	| exp_029c_tcn_walker_s0_sigma01 | σ=0.1 最低有效剂量测试 | Walker | eval peak 490.7@165K, final 328.3 | σ=0.1 未阻止 CIVO（NVE 曾 breach），但最终 eval 尚可；剂量不足以可靠抑制 |
32	| exp_029d_tcn_walker_s3_sigma02 | TCN σ=0.2 seed 3 统计补充 | Walker | eval peak 349.6@95K, CIVO onset @105K sudden blowup | 健康→突然崩溃（NVE 0.67@95K→3.0@105K），TCN σ=0.2 无法防止晚期 CIVO |
33	| exp_030a_tcn_cheetah_s0_sigma02 | TCN σ=0.2 跨环境验证 (Cheetah) | Cheetah | eval 299.5@35K→31.9@55K, NVE 1.903@5
…[truncated 8636 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T18:37:45.291488+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/a16e8b93-bce8-4579-82f0-52ee2e183f79/tool-results/mcp-agent-ml-research-read_registry-1779647587226.txt",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/a16e8b93-bce8-4579-82f0-52ee2e183f79/tool-results/mcp-agent-ml-research-read_registry-1779647587226.txt",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T18:37:45.291619+00:00_

File content (42580 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T18:37:45.291741+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "event-gated-adaptive-horizon",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T18:37:45.292575+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_framing.md\", \"content\": \"# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL\\n\\n## Title Candidates\\n\\n1. **\\\"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination\\\"**\\n2. ~~**\\\"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination\\\"**~~ (deprecated — \\\"delusional critic\\\" conflicts with Lu et al. 2018)\\n3. **\\\"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3\\\"** ← preferred after D037 terminology decision\\n4. **\\\"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination\\\"**\\n\\n**⚠️ D037 术语决定**: \\\"delusional critic\\\" → **\\\"conditioning-induced value overestimation\\\"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换：\\\"delusional critic\\\" → \\\"conditioning-induced value overestimation\\\"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。\\n\\n**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 \\\"known failure class 的 specific instance\\\" 升级为 \\\"dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability\\\"**。TAWM 是强化 novelty 的最关键参考文献。\\n\\n## Venue\\n\\n**ICML 2026** — Deadline: 2026-05-29\\n\\n## Narrative Positioning\\n\\nThis is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*\\n\\nThe contribution is a **strongly supported causal chain** from mechanism to failure 
…[truncated 45788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T18:37:45.292813+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/a16e8b93-bce8-4579-82f0-52ee2e183f79/tool-results/mcp-agent-ml-research-read_registry-1779647587226.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result if isinstance(result, list) else result.get('experiments', result.get('data', []))\nprint(f'Total negative experiments: {len(exps)}')\nprint()\nfor e in exps:\n    eid = e.get('exp_id', 'unknown')\n    hyp = e.get('hypothesis', '')[:100]\n    conc = e.get('conclusion_detail', e.get('conclusion', ''))[:80]\n    tags = e.get('tags', [])\n    print(f'--- {eid} ---')\n    print(f'  hypothesis: {hyp}')\n    print(f'  conclusion_detail: {conc}')\n    print(f'  tags: {tags}')\n    print()\n\" 2>/dev/null || echo \"PARSE_ERROR\"\n",
  "description": "Parse registry JSON to extract experiment summaries",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/a16e8b93-bce8-4579-82f0-52ee2e183f79/tool-results/mcp-agent-ml-research-read_registry-1779647587226.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result if isinstance(result, list) else result.get('experiments', result.get('data', []))\nprint(f'Total negative experiments: {len(exps)}')\nprint()\nfor e in exps:\n    eid = e.get('exp_id', 'unknown')\n    hyp = e.get('hypothesis', '')[:100]\n    conc = e.get('conclusion_detail', e.get('conclusion', ''))[:80]\n    tags = e.get('tags', [])\n    print(f'--- {eid} ---')\n    print(f'  hypothesis: {hyp}')\n    print(f'  conclusion_detail: {conc}')\n    print(f'  tags: {tags}')\n    print()\n\" 2>/dev/null || echo \"PARSE_ERROR\"\n",
    "description": "Parse registry JSON to extract experiment summaries",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T18:37:45.292990+00:00_

Total negative experiments: 4

PARSE_ERROR

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T18:37:45.293143+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{}",
  "fields": "['exp_id', 'conclusion', 'hypothesis', 'tags']",
  "project": "event-gated-adaptive-horizon",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{}",
    "fields": "['exp_id', 'conclusion', 'hypothesis', 'tags']",
    "project": "event-gated-adaptive-horizon",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T18:37:45.293619+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_063_rssm_fidelity\": {\"hypothesis\": \"RSSM 在 dt=2 transitions 上的 observation/reward reconstruction loss 显著高于 dt=1，量化 fidelity gap 作为 trained dt_emb 导致 delusional critic 的机械性基础。从 exp_001 (baseline) 和 exp_008d (collapsed) 的已有 checkpoint 提取，对比 dt=1 vs dt=2 prediction quality。\"}, \"exp_051_stackcube_frozen_dt_emb_s0\": {\"hypothesis\": \"Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_ratio 3.27@32.5K) to establish trained-vs-frozen causal evidence in manipulation tasks. If frozen prevents CIVO → extends Walker/Cheetah frozen finding to manipulation; if not → domain-specific factors override dt_emb mechanism.\", \"conclusion\": \"negative\"}, \"exp_049_stackcube_civo_trigger_s0\": {\"hypothesis\": \"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion 推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack）。如果触发 → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\", \"conclusion\": \"success\"}, \"exp_061_cartpole_civo_trigger\": {\"hypothesis\": \"Trained dt_emb (d=32) + subsample ON + H=8 + dt=2 imagination 在 Cartpole Swingup 上触发 CIVO（NVE > 1.5x），验证 CIVO 是否跨 locomotion 子类环境泛化（Walker/Cheetah 已确认，Cartpole 是第三个 DMC locomotion 环境）。与 exp_062 配对形成因果对比。\"}, \"exp_057\": {\"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker seed=2, n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3 验证稳健性。\", \"conclusion\": \"success\"}, \"exp_062_cartpole_control\": {\"hypothesis\": \"dt_embed_dim=0 + subsample ON + H=8 在 Cartpole Swingup 上不触发 CIVO（NVE < 1.5x），因果控制实验验证移除 dt_emb 是否阻止 CIVO 在第三个环境中泛化。与 exp_061 配对形成因果对比。\"}, \"exp_060_cartpole_baseline\": {\"hypothesis\": \"Cartpole Swingup (DMC) baseline dt=1 建立 v/e ratio 校准基线，用于 CIVO 诊断阈值在第三个 DMC 环境的验证。预期 NVE 保持在 1.0x 附近，无 CIVO 现象。\"}, \"exp_008d_civo_trigger_s4\": {\"conclusion\": \"success\", \"hypothesis\": \"Walker Walk C
…[truncated 37845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T18:37:45.293865+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_051_stackcube_frozen_dt_emb_s0'}",
  "fields": "['*']",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_051_stackcube_frozen_dt_emb_s0'}",
    "fields": "['*']",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T18:37:45.294015+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4857}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T18:37:45.294144+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_025_obs_sgs_walker_s1'}",
  "fields": "['*']",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_025_obs_sgs_walker_s1'}",
    "fields": "['*']",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T18:37:45.294298+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4472}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T18:37:45.294440+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_026_obs_sgs_cheetah_s0'}",
  "fields": "['*']",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_026_obs_sgs_cheetah_s0'}",
    "fields": "['*']",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T18:37:45.294568+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4564}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-24T18:37:45.294783+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/negative_results_insights.md",
  "content": "# Negative Results → ICML Insights Analysis\n\n**目标**: 从 35 个 negative 实验中提取可转化为论文 positive contribution 的 insight，服务于核心 narrative: CIVO 是 dt_emb-driven 的 locomotion-specific 现象，且在所有干预层级上都难以可靠缓解。\n\n---\n\n## 结构化清单\n\n### 高 Insight 价值（证伪本身是重要发现）\n\n| exp_id | Hypothesis（被证伪） | Insight | 价值 | 论文 Framing 建议 |\n|--------|----------------------|---------|------|-------------------|\n| exp_016e | Reward-head SGS 阻断 CIVO 梯度通路 | Reward head 贡献 38-49% 梯度但阻断它是 **no-op**（reward loss 对 dt_emb.weight 梯度=0）。**梯度量级与因果重要性完全脱耦** | 高 | Section 3 核心发现。\"Gradient Magnitude ≠ Causal Importance\" 作为独立 observation，对 multi-head MBRL 系统有方法论启示。Reviewer 易 resonate——违反直觉且可验证 |\n| exp_018v2 + exp_018_s2 | Full-SGS（阻断所有 decoder→dt_emb 梯度）消除 CIVO | Full SGS 0/3 seeds（含 2 环境）。CIVO 仅被延迟 ~30K 步后仍爆发。**Backward-pass 是错误的干预层级**——forward-pass representational damage 不可逆 | 高 | Intervention Hierarchy Table 的 L1 行。Frame: \"Even blocking all non-KL gradient pathways (reducing dt_emb gradient by >95%) only delays onset, proving the vulnerability resides in the forward pass\" |\n| exp_026_obs_sgs_cheetah (s0+s1) | 阻断 obs-decoder→dt_emb 梯度消除 Cheetah CIVO | **补偿放大**：阻断 obs-decoder 后 NVE 从 untreated 8.3× 恶化到 21.9-30.2×（2.6-3.6× 放大）。阻断一条通路导致剩余通路 co-adaptation 加剧 | 高 | Section 3/Discussion 作为 \"compensatory amplification\" 现象。对 multi-head architecture 干预设计有普适警示：局部干预可能比不干预更糟 |\n| exp_030c (TCN σ=1.0 Cheetah) | 高剂量 TCN 噪声可抑制 Cheetah CIVO | **\"Impossible dose\"**：σ=1.0 完全抑制 CIVO（NVE≤0.30），但 eval 从 peak 372(116% baseline!)→47(15%)。CIVO prevention threshold > noise tolerance threshold，**不存在 Goldilocks zone**。关键：初始学习不受影响（35K=116% baseline），是渐进累积性 policy erosion | 高 | Section 3.6 最有力单点。Frame: \"The effective dose exceeds the tolerable dose — CIVO prevention requires noise levels that progressively erode policy quality through cumulative actor gradient interference, even while value calibration remains normal\" |\n| exp_034 + exp_034_dual_critic_cheetah | Dual-critic pessimism（Double Q）防止 Cheetah CIVO | **v1≈v2**（ρ>0.999）：两个 critic 共享 world model imagined features → 收敛到相同函数。Per-sample pessimism 仅为独立 critic 理论值 3-4%。**Pessimism 机制在 pure-imagination MBRL 中失效** | 高 | Section 3 / R9 回应的核心。Frame: \"Standard Double Q assumes critic independence; in imagination-based training where both critics consume identical world-model features, this assumption breaks — critics correlate to ρ>0.999, rendering min-based pessimism a near-identity operation\" |\n| exp_038_dual_critic_walker_s2 | Dual-critic 防止所有 collapse | CIVO 被完全阻止（NVE≤0.3）但 eval 仍 354→99.6 崩溃。**Non-CIVO collapse（Pathway B）**：actor entropy 急升(-3.59→-0.45)，与 CIVO 的 entropy 下降相反。Trained dt_emb 创造**多条脆弱性路径** | 高 | C6 partially falsified 的关键证据。Frame: \"Eliminating CIVO (Pathway A) reveals a second vulnerability — trained dt-embedding destabilizes the actor through a distinct mechanism (eval-driven entropy increase) that architectural interventions do not address\" |\n| exp_008e_v3_s2 | dt=1 imagination 防止 collapse（C6） | dt=1 imagination + trained dt_emb：1/2 seeds 崩溃（715→137），崩溃动力学与 CIVO 定性不同（eval-driven vs value-driven）。**Trained dt_emb 通过 forward pass 创造不依赖 imagination dt 的脆弱性** | 高 | C6 核心，2-3 句 + 对比表。Frame: \"Restricting imagination to dt=1 eliminates the value overestimation feedback loop (Pathway A) but not the eval-driven instability (Pathway B), demonstrating that trained dt-embedding creates vulnerability through the forward pass itself, not solely through multi-step imagination\" |\n\n### 中 Insight 价值（边界条件或设计约束）\n\n| exp_id | Hypothesis（被证伪） | Insight | 价值 | 论文 Framing 建议 |\n|--------|----------------------|---------|------|-------------------|\n| exp_030a/030b/031/031b (TCN cross-env) | TCN 跨环境泛化 | Effective dose scales with CIVO severity; tolerable dose does not。Walker σ=0.2 成功但 Cheetah/PickCube σ=0.2-0.5 全部失败。**不存在 universal effective dose** | 中 | Section 3.6 \"dose-environment dependency\" observation。支撑 TCN = diagnostic probe not deployable mitigation 的定位 |\n| exp_027_s0/s1 + exp_029b/029d (TCN seed variance) | TCN σ=0.2 在 Walker 上 robust | Walker σ=0.2: 2/4 seeds 成功，2/4 完全失败（NVE>2.0）。**Seed 效应 > dose 效应**。TCN 作为 all-or-nothing gate 运作，无中间态 | 中 | 1-2 句 observation + appendix 详细分析。\"Binary protection\" 特性表明 CIVO onset 有 phase transition 性质——一旦突破临界点不可逆转 |\n| exp_028/028_ceil15 (RAVE) | Value capping 防止 CIVO | **EMA anchor 自身被污染**：CIVO 早期 imagined values 已偏高，EMA 跟踪这些值 → ceiling 无效。CIVO 根因不在 value 数值大小，而在 **value 的结构性偏差** | 中 | Intervention Hierarchy L2 行。Frame: \"Output-level value capping fails because the anchor itself is corrupted by the same overestimation it aims to constrain — a bootstrap failure analogous to the CIVO mechanism itself\" |\n| exp_006/007/008c/008f_s4/009c (dt>1 degradation) | 解决 CIVO 后 dt>1 可行 | 即使完全消除 CIVO，dt>1 仍带来 40-70% 性能损失（RSSM compounding error）。**CIVO 只是 dt>1 问题的一个维度** | 中 | Discussion/Limitation。Frame: \"Even a hypothetical perfect CIVO solution would leave 40-70% performance degradation from RSSM compounding error — temporal abstraction in imagination requires fundamentally better multi-step prediction, not just overestimation control\" |\n| exp_015b (frozen dt_emb) | 冻结 dt_emb 避免 CIVO | **Gradient starvation**：冻结 dt_emb 导致 actor_loss→0、entropy 异常低。dt_emb 梯度流对正常学习必要——**不能通过冻结触发参数来规避** | 中 | Section 3 简短提及。Frame: \"The very parameter that triggers CIVO is also essential for learning — freezing it trades overestimation for starvation, confirming that the vulnerability is architecturally entangled\" |\n| exp_037_wide_critic_cheetah | Capacity alone（宽 critic）抑制 Cheetah CIVO | NVE 从 baseline 70.64 降至 3.6（但仍远超 1.5 阈值），eval 146（baseline 31%）。**Capacity alone 提供部分 recovery 但不能 prevent** | 中 | 2×2 mechanism factorial 的一格。与 dual-critic 对比支撑 \"min+capacity 协同\" 发现 |\n| exp_036_dual_critic_pickcube | Dual-critic 跨 manipulation 泛化 | NVE 终值 0.2（\"prevented\"）但 eval 极低（27.7），gate 锁死 dt=2。**功能性失败**：CIVO 指标好但实际性能不可接受 | 中 | Scope limitation discussion。PickCube 任务动态与 locomotion 根本不同——gate/subsample 配置本身对 manipulation 有害（vanilla baseline 58.6 → 加配置后 26.6），非 CIVO 导致 |\n| exp_003/004/005 (event-gate v2-v4) | Learned gate 实现 adaptive horizon | Gate 的 dt>1 选择**内在地**引入 CIVO，且 gate 无法学会规避。**这一失败催生了整个 CIVO 研究方向** | 中 | Introduction 叙事起点。Frame: \"Our initial attempt at learned temporal abstraction consistently degraded performance. Diagnosing this failure led to the identification of CIVO as the root mechanism\" |\n| exp_051_stackcube_frozen | Frozen dt_emb 在 manipulation 防止 CIVO | Frozen dt_emb 在 Walker/Cheetah（locomotion）有效但 StackCube（manipulation）失败。**Locomotion 与 manipulation 的 CIVO 机制存在差异** | 中 | Scope boundary 讨论。支撑 \"locomotion-specific\" 论文 scope 限定 |\n\n### 低 Insight 价值（纯统计补充或已被取代）\n\n| exp_id | Hypothesis（被证伪） | Insight | 价值 | 论文 Framing 建议 |\n|--------|----------------------|---------|------|-------------------|\n| exp_009e (008d s1 延长) | CIVO collapse 复现 | 确认 CIVO collapse，诊断性 negative | 低 | 仅作为 multi-seed 数据点计入统计表 |\n| exp_009b (008d s2) | CIVO onset 跨 seed 复现 | NVE>1.5 但 self-corrected（268 eval）。Transient vs sustained 的 early evidence | 低 | 已被更完整的 multi-seed 分析取代，作为 C2 4/4 separation 的一个数据点 |\n| exp_008e_v3_s3 | C6 第三 seed 验证 | 又一个 collapse seed，加强统计但无新机制 | 低 | 仅计入 collapse rate（现 3/4），不需独立讨论 |\n| exp_008f_s4 | No-dt-emb 控制组 seed 4 | eval 306.5（baseline 33%），无 CIVO（NVE 0.58）。预期内的性能代价 | 低 | 仅作为 no-dt-emb 控制的第 N 个数据点 |\n| exp_009c (008f s2) | No-dt-emb 控制 seed 2 | NVE 1.14@105K（borderline），比 seed 1 更高。Protection \"不 robust\" 的早期 signal | 低 | 已被 008f 系列多 seed 数据取代 |\n| exp_008c | Subsample OFF + dt=2 imag 可行 | eval 仅 baseline 39%。Compounding error 是瓶颈 | 低 | 被 C5 discussion 吸收，不需独立列出 |\n| exp_025_obs_sgs_walker_s2 | Obs-decoder-only SGS 抑制 CIVO | CIVO 部分抑制但 eval 仅 7-10% baseline。obs-decoder SGS 摧毁性能 | 低 | 被 C7 的 1/6 统计和 universal value collapse 发现吸收 |\n| exp_029c (σ=0.1) | σ=0.1 是最低有效剂量 | NVE breach 但最终 eval 尚可（328）。剂量不足 | 低 | dose-response 曲线的一个数据点 |\n| exp_027_tcn_walker_s0 (σ=0.5) | TCN σ=0.5 抑制 CIVO | NVE peak 4.0, oscillatory CIVO。σ=0.5 在 Walker 过量 | 低 | dose-response 的 overdose 端参考 |\n| exp_027_tcn_walker_s1 (σ=0.5 s1) | TCN σ=0.5 seed 1 复现 | NVE 1.64, oscillatory。与 s0 一致：σ=0.5 过量 | 低 | 同上 |\n\n---\n\n## Coherent Story: Intervention Hierarchy 与多层失败叙事\n\n### 核心 Narrative\n\n35 个 negative 实验组合构成了一个 **escalating intervention failure** 的完整叙事，从最轻量（gradient manipulation）到最重量（architecture redesign），系统性证明 CIVO 在所有干预层级上的抗性：\n\n```\n干预层级           方法               成功率      关键失败机制\n─────────────────────────────────────────────────────────────\nL1 Gradient        Reward SGS         0/2        No-op (梯度≠因果)\n                   Full SGS           0/3        Forward-pass damage 不可逆\n                   Obs-decoder SGS    1/6        补偿放大 + critic 校准损坏\nL2 Output          RAVE               0/2        EMA anchor 自身被污染\nL3 Representation  TCN                2/8        Dose-env dependency, 无 Goldilocks zone\nL4 Architecture    Dual-critic        3/5*       v1≈v2 (pessimism 失效),\n                                                 non-CIVO collapse (Pathway B)\n─────────────────────────────────────────────────────────────\nControl            dt_emb removal     5/5        不是干预——移除了 feature\n```\n\n*Walker 2/3 CIVO prevented + 1 non-CIVO collapse; Cheetah 0/1; PickCube 功能性失败\n\n### 这个 Hierarchy 为什么构成 Positive Contribution\n\n1. **节约社区资源**：7+ 方法 × 3 层级 × 3 环境的系统性 negative evidence，阻止后续研究者重复探索这些 dead ends\n2. **揭示 CIVO 的本质**：不是 gradient 问题（SGS 失败）、不是 value magnitude 问题（RAVE 失败）、不是 critic independence 问题（v1≈v2），而是 **forward-pass representational entanglement**\n3. **方法论启示**：\n   - \"梯度量级 ≠ 因果重要性\" 对所有 multi-head MBRL 系统的 debugging 有普适价值\n   - \"补偿放大\" 对 partial intervention 设计的警示\n   - \"impossible dose\" 证明某些 failure mode 不能通过 tuning 解决\n\n### 三条辅助 Narrative\n\n**A. Multi-Pathway Vulnerability（多路径脆弱性）**\n- exp_008e_v3_s2 + exp_038 共同证明：trained dt_emb 通过至少两条路径创造脆弱性\n  - Pathway A (CIVO): value overestimation → actor exploitation → entropy ↓ → collapse\n  - Pathway B (IRD): eval-driven destabilization → entropy ↑ → policy randomization\n- dt=1 imagination 消除 Pathway A 但不消除 B\n- Dual-critic 消除 CIVO 但不消除 non-CIVO collapse\n- **论文价值**: 即使\"解决\" CIVO，trained dt_emb 仍不安全\n\n**B. Environment Severity Boundary（环境严重度边界）**\n- Walker（NVE 1.5-5×）: TCN 2/4, dual-critic 2/3 有效\n- Cheetah（NVE 8-70×）: TCN 0/3, dual-critic 0/1, σ=1.0 impossible dose\n- PickCube: 任务动态本质不同，gate 配置本身有害\n- **论文价值**: 所有干预方法都有 CIVO severity ceiling，强化 \"根本解决需要架构革新\" 的结论\n\n**C. Origin Story（研究方向转向）**\n- exp_003→004→005 (event-gate v2-v4) 的连续失败催生了 CIVO 研究方向\n- 从 \"如何让 temporal abstraction work\" 到 \"为什么 temporal abstraction fails\"\n- **论文价值**: Introduction 叙事起点，展示研究动机的自然性\n\n---\n\n## 论文各 Section 对应的 Negative Results 使用建议\n\n| Section | 使用的 Negative Results | 功能 |\n|---------|------------------------|------|\n| Introduction | exp_003-005 (event-gate 失败) | 研究动机：试图做 temporal abstraction 但反复失败，转向诊断 why |\n| Section 3.1-3.2 (CIVO 诊断) | exp_009e/009b (CIVO 复现) | 作为 multi-seed 数据点确认 CIVO 可复现性和随机性 |\n| Section 3.3 (Gradient analysis) | exp_016e (reward SGS no-op) | \"梯度 ≠ 因果\" 核心发现 |\n| Section 3.4 (SGS 系列) | exp_018v2/018_s2/021/025/026 | Intervention Hierarchy L1 全面否定；补偿放大 |\n| Section 3.5 (RAVE) | exp_028/028_ceil15 | L2 否定；anchor 污染机制 |\n| Section 3.6 (TCN) | exp_027-031b 全系列 | L3 部分否定；impossible dose；dose-env dependency |\n| Section 3.7 (Dual-critic) | exp_034/036/037/038 | L4 部分否定；v1≈v2；non-CIVO collapse |\n| Section 4 (C6 multi-pathway) | exp_008e_v3_s2/s3 + exp_038 | 多路径脆弱性证据 |\n| Discussion (dt>1 limitation) | exp_006/007/008c/008f_s4 | 即使解决 CIVO，dt>1 仍有 40-70% 性能损失 |\n| Discussion (scope) | exp_051 (StackCube frozen 失败) + exp_036 (PickCube) | Locomotion-specific scope boundary |\n| Discussion (frozen dt_emb) | exp_015b | 不能冻结触发参数——architecturally entangled |\n\n---\n\n## 总结\n\n35 个 negative 实验中：\n- **7 个高 insight**：构成 Intervention Hierarchy + Multi-Pathway Vulnerability 两大核心贡献\n- **10 个中 insight**：提供边界条件、scope limitation、design constraint\n- **10+ 个低 insight**：作为统计数据点计入，不需独立讨论\n\n最重要的 framing 策略：这些 negative results **不是 limitation**，而是论文的 **primary contribution**。一篇 diagnostic paper 的价值恰恰在于系统性地证明某个问题有多难解决，以及为什么难。Intervention Hierarchy（7 methods × 3 levels × 3 environments）是同类工作中最全面的 CIVO 干预评估，其 negative nature 本身就是强贡献。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/negative_results_insights.md",
    "content": "# Negative Results → ICML Insights Analysis\n\n**目标**: 从 35 个 negative 实验中提取可转化为论文 positive contribution 的 insight，服务于核心 narrative: CIVO 是 dt_emb-driven 的 locomotion-specific 现象，且在所有干预层级上都难以可靠缓解。\n\n---\n\n## 结构化清单\n\n### 高 Insight 价值（证伪本身是重要发现）\n\n| exp_id | Hypothesis（被证伪） | Insight | 价值 | 论文 Framing 建议 |\n|--------|----------------------|---------|------|-------------------|\n| exp_016e | Reward-head SGS 阻断 CIVO 梯度通路 | Reward head 贡献 38-49% 梯度但阻断它是 **no-op**（reward loss 对 dt_emb.weight 梯度=0）。**梯度量级与因果重要性完全脱耦** | 高 | Section 3 核心发现。\"Gradient Magnitude ≠ Causal Importance\" 作为独立 observation，对 multi-head MBRL 系统有方法论启示。Reviewer 易 resonate——违反直觉且可验证 |\n| exp_018v2 + exp_018_s2 | Full-SGS（阻断所有 decoder→dt_emb 梯度）消除 CIVO | Full SGS 0/3 seeds（含 2 环境）。CIVO 仅被延迟 ~30K 步后仍爆发。**Backward-pass 是错误的干预层级**——forward-pass representational damage 不可逆 | 高 | Intervention Hierarchy Table 的 L1 行。Frame: \"Even blocking all non-KL gradient pathways (reducing dt_emb gradient by >95%) only delays onset, proving the vulnerability resides in the forward pass\" |\n| exp_026_obs_sgs_cheetah (s0+s1) | 阻断 obs-decoder→dt_emb 梯度消除 Cheetah CIVO | **补偿放大**：阻断 obs-decoder 后 NVE 从 untreated 8.3× 恶化到 21.9-30.2×（2.6-3.6× 放大）。阻断一条通路导致剩余通路 co-adaptation 加剧 | 高 | Section 3/Discussion 作为 \"compensatory amplification\" 现象。对 multi-head architecture 干预设计有普适警示：局部干预可能比不干预更糟 |\n| exp_030c (TCN σ=1.0 Cheetah) | 高剂量 TCN 噪声可抑制 Cheetah CIVO | **\"Impossible dose\"**：σ=1.0 完全抑制 CIVO（NVE≤0.30），但 eval 从 peak 372(116% baseline!)→47(15%)。CIVO prevention threshold > noise tolerance threshold，**不存在 Goldilocks zone**。关键：初始学习不受影响（35K=116% baseline），是渐进累积性 policy erosion | 高 | Section 3.6 最有力单点。Frame: \"The effective dose exceeds the tolerable dose — CIVO prevention requires noise levels that progressively erode policy quality through cumulative actor gradient interference, even while value calibration remains normal\" |\n| exp_034 + exp_034_dual_critic_cheetah | Dual-critic pessimism（Double Q）防止 Cheetah CIVO | **v1≈v2**（ρ>0.999）：两个 critic 共享 world model imagined features → 收敛到相同函数。Per-sample pessimism 仅为独立 critic 理论值 3-4%。**Pessimism 机制在 pure-imagination MBRL 中失效** | 高 | Section 3 / R9 回应的核心。Frame: \"Standard Double Q assumes critic independence; in imagination-based training where both critics consume identical world-model features, this assumption breaks — critics correlate to ρ>0.999, rendering min-based pessimism a near-identity operation\" |\n| exp_038_dual_critic_walker_s2 | Dual-critic 防止所有 collapse | CIVO 被完全阻止（NVE≤0.3）但 eval 仍 354→99.6 崩溃。**Non-CIVO collapse（Pathway B）**：actor entropy 急升(-3.59→-0.45)，与 CIVO 的 entropy 下降相反。Trained dt_emb 创造**多条脆弱性路径** | 高 | C6 partially falsified 的关键证据。Frame: \"Eliminating CIVO (Pathway A) reveals a second vulnerability — trained dt-embedding destabilizes the actor through a distinct mechanism (eval-driven entropy increase) that architectural interventions do not address\" |\n| exp_008e_v3_s2 | dt=1 imagination 防止 collapse（C6） | dt=1 imagination + trained dt_emb：1/2 seeds 崩溃（715→137），崩溃动力学与 CIVO 定性不同（eval-driven vs value-driven）。**Trained dt_emb 通过 forward pass 创造不依赖 imagination dt 的脆弱性** | 高 | C6 核心，2-3 句 + 对比表。Frame: \"Restricting imagination to dt=1 eliminates the value overestimation feedback loop (Pathway A) but not the eval-driven instability (Pathway B), demonstrating that trained dt-embedding creates vulnerability through the forward pass itself, not solely through multi-step imagination\" |\n\n### 中 Insight 价值（边界条件或设计约束）\n\n| exp_id | Hypothesis（被证伪） | Insight | 价值 | 论文 Framing 建议 |\n|--------|----------------------|---------|------|-------------------|\n| exp_030a/030b/031/031b (TCN cross-env) | TCN 跨环境泛化 | Effective dose scales with CIVO severity; tolerable dose does not。Walker σ=0.2 成功但 Cheetah/PickCube σ=0.2-0.5 全部失败。**不存在 universal effective dose** | 中 | Section 3.6 \"dose-environment dependency\" observation。支撑 TCN = diagnostic probe not deployable mitigation 的定位 |\n| exp_027_s0/s1 + exp_029b/029d (TCN seed variance) | TCN σ=0.2 在 Walker 上 robust | Walker σ=0.2: 2/4 seeds 成功，2/4 完全失败（NVE>2.0）。**Seed 效应 > dose 效应**。TCN 作为 all-or-nothing gate 运作，无中间态 | 中 | 1-2 句 observation + appendix 详细分析。\"Binary protection\" 特性表明 CIVO onset 有 phase transition 性质——一旦突破临界点不可逆转 |\n| exp_028/028_ceil15 (RAVE) | Value capping 防止 CIVO | **EMA anchor 自身被污染**：CIVO 早期 imagined values 已偏高，EMA 跟踪这些值 → ceiling 无效。CIVO 根因不在 value 数值大小，而在 **value 的结构性偏差** | 中 | Intervention Hierarchy L2 行。Frame: \"Output-level value capping fails because the anchor itself is corrupted by the same overestimation it aims to constrain — a bootstrap failure analogous to the CIVO mechanism itself\" |\n| exp_006/007/008c/008f_s4/009c (dt>1 degradation) | 解决 CIVO 后 dt>1 可行 | 即使完全消除 CIVO，dt>1 仍带来 40-70% 性能损失（RSSM compounding error）。**CIVO 只是 dt>1 问题的一个维度** | 中 | Discussion/Limitation。Frame: \"Even a hypothetical perfect CIVO solution would leave 40-70% performance degradation from RSSM compounding error — temporal abstraction in imagination requires fundamentally better multi-step prediction, not just overestimation control\" |\n| exp_015b (frozen dt_emb) | 冻结 dt_emb 避免 CIVO | **Gradient starvation**：冻结 dt_emb 导致 actor_loss→0、entropy 异常低。dt_emb 梯度流对正常学习必要——**不能通过冻结触发参数来规避** | 中 | Section 3 简短提及。Frame: \"The very parameter that triggers CIVO is also essential for learning — freezing it trades overestimation for starvation, confirming that the vulnerability is architecturally entangled\" |\n| exp_037_wide_critic_cheetah | Capacity alone（宽 critic）抑制 Cheetah CIVO | NVE 从 baseline 70.64 降至 3.6（但仍远超 1.5 阈值），eval 146（baseline 31%）。**Capacity alone 提供部分 recovery 但不能 prevent** | 中 | 2×2 mechanism factorial 的一格。与 dual-critic 对比支撑 \"min+capacity 协同\" 发现 |\n| exp_036_dual_critic_pickcube | Dual-critic 跨 manipulation 泛化 | NVE 终值 0.2（\"prevented\"）但 eval 极低（27.7），gate 锁死 dt=2。**功能性失败**：CIVO 指标好但实际性能不可接受 | 中 | Scope limitation discussion。PickCube 任务动态与 locomotion 根本不同——gate/subsample 配置本身对 manipulation 有害（vanilla baseline 58.6 → 加配置后 26.6），非 CIVO 导致 |\n| exp_003/004/005 (event-gate v2-v4) | Learned gate 实现 adaptive horizon | Gate 的 dt>1 选择**内在地**引入 CIVO，且 gate 无法学会规避。**这一失败催生了整个 CIVO 研究方向** | 中 | Introduction 叙事起点。Frame: \"Our initial attempt at learned temporal abstraction consistently degraded performance. Diagnosing this failure led to the identification of CIVO as the root mechanism\" |\n| exp_051_stackcube_frozen | Frozen dt_emb 在 manipulation 防止 CIVO | Frozen dt_emb 在 Walker/Cheetah（locomotion）有效但 StackCube（manipulation）失败。**Locomotion 与 manipulation 的 CIVO 机制存在差异** | 中 | Scope boundary 讨论。支撑 \"locomotion-specific\" 论文 scope 限定 |\n\n### 低 Insight 价值（纯统计补充或已被取代）\n\n| exp_id | Hypothesis（被证伪） | Insight | 价值 | 论文 Framing 建议 |\n|--------|----------------------|---------|------|-------------------|\n| exp_009e (008d s1 延长) | CIVO collapse 复现 | 确认 CIVO collapse，诊断性 negative | 低 | 仅作为 multi-seed 数据点计入统计表 |\n| exp_009b (008d s2) | CIVO onset 跨 seed 复现 | NVE>1.5 但 self-corrected（268 eval）。Transient vs sustained 的 early evidence | 低 | 已被更完整的 multi-seed 分析取代，作为 C2 4/4 separation 的一个数据点 |\n| exp_008e_v3_s3 | C6 第三 seed 验证 | 又一个 collapse seed，加强统计但无新机制 | 低 | 仅计入 collapse rate（现 3/4），不需独立讨论 |\n| exp_008f_s4 | No-dt-emb 控制组 seed 4 | eval 306.5（baseline 33%），无 CIVO（NVE 0.58）。预期内的性能代价 | 低 | 仅作为 no-dt-emb 控制的第 N 个数据点 |\n| exp_009c (008f s2) | No-dt-emb 控制 seed 2 | NVE 1.14@105K（borderline），比 seed 1 更高。Protection \"不 robust\" 的早期 signal | 低 | 已被 008f 系列多 seed 数据取代 |\n| exp_008c | Subsample OFF + dt=2 imag 可行 | eval 仅 baseline 39%。Compounding error 是瓶颈 | 低 | 被 C5 discussion 吸收，不需独立列出 |\n| exp_025_obs_sgs_walker_s2 | Obs-decoder-only SGS 抑制 CIVO | CIVO 部分抑制但 eval 仅 7-10% baseline。obs-decoder SGS 摧毁性能 | 低 | 被 C7 的 1/6 统计和 universal value collapse 发现吸收 |\n| exp_029c (σ=0.1) | σ=0.1 是最低有效剂量 | NVE breach 但最终 eval 尚可（328）。剂量不足 | 低 | dose-response 曲线的一个数据点 |\n| exp_027_tcn_walker_s0 (σ=0.5) | TCN σ=0.5 抑制 CIVO | NVE peak 4.0, oscillatory CIVO。σ=0.5 在 Walker 过量 | 低 | dose-response 的 overdose 端参考 |\n| exp_027_tcn_walker_s1 (σ=0.5 s1) | TCN σ=0.5 seed 1 复现 | NVE 1.64, oscillatory。与 s0 一致：σ=0.5 过量 | 低 | 同上 |\n\n---\n\n## Coherent Story: Intervention Hierarchy 与多层失败叙事\n\n### 核心 Narrative\n\n35 个 negative 实验组合构成了一个 **escalating intervention failure** 的完整叙事，从最轻量（gradient manipulation）到最重量（architecture redesign），系统性证明 CIVO 在所有干预层级上的抗性：\n\n```\n干预层级           方法               成功率      关键失败机制\n─────────────────────────────────────────────────────────────\nL1 Gradient        Reward SGS         0/2        No-op (梯度≠因果)\n                   Full SGS           0/3        Forward-pass damage 不可逆\n                   Obs-decoder SGS    1/6        补偿放大 + critic 校准损坏\nL2 Output          RAVE               0/2        EMA anchor 自身被污染\nL3 Representation  TCN                2/8        Dose-env dependency, 无 Goldilocks zone\nL4 Architecture    Dual-critic        3/5*       v1≈v2 (pessimism 失效),\n                                                 non-CIVO collapse (Pathway B)\n─────────────────────────────────────────────────────────────\nControl            dt_emb removal     5/5        不是干预——移除了 feature\n```\n\n*Walker 2/3 CIVO prevented + 1 non-CIVO collapse; Cheetah 0/1; PickCube 功能性失败\n\n### 这个 Hierarchy 为什么构成 Positive Contribution\n\n1. **节约社区资源**：7+ 方法 × 3 层级 × 3 环境的系统性 negative evidence，阻止后续研究者重复探索这些 dead ends\n2. **揭示 CIVO 的本质**：不是 gradient 问题（SGS 失败）、不是 value magnitude 问题（RAVE 失败）、不是 critic independence 问题（v1≈v2），而是 **forward-pass representational entanglement**\n3. **方法论启示**：\n   - \"梯度量级 ≠ 因果重要性\" 对所有 multi-head MBRL 系统的 debugging 有普适价值\n   - \"补偿放大\" 对 partial intervention 设计的警示\n   - \"impossible dose\" 证明某些 failure mode 不能通过 tuning 解决\n\n### 三条辅助 Narrative\n\n**A. Multi-Pathway Vulnerability（多路径脆弱性）**\n- exp_008e_v3_s2 + exp_038 共同证明：trained dt_emb 通过至少两条路径创造脆弱性\n  - Pathway A (CIVO): value overestimation → actor exploitation → entropy ↓ → collapse\n  - Pathway B (IRD): eval-driven destabilization → entropy ↑ → policy randomization\n- dt=1 imagination 消除 Pathway A 但不消除 B\n- Dual-critic 消除 CIVO 但不消除 non-CIVO collapse\n- **论文价值**: 即使\"解决\" CIVO，trained dt_emb 仍不安全\n\n**B. Environment Severity Boundary（环境严重度边界）**\n- Walker（NVE 1.5-5×）: TCN 2/4, dual-critic 2/3 有效\n- Cheetah（NVE 8-70×）: TCN 0/3, dual-critic 0/1, σ=1.0 impossible dose\n- PickCube: 任务动态本质不同，gate 配置本身有害\n- **论文价值**: 所有干预方法都有 CIVO severity ceiling，强化 \"根本解决需要架构革新\" 的结论\n\n**C. Origin Story（研究方向转向）**\n- exp_003→004→005 (event-gate v2-v4) 的连续失败催生了 CIVO 研究方向\n- 从 \"如何让 temporal abstraction work\" 到 \"为什么 temporal abstraction fails\"\n- **论文价值**: Introduction 叙事起点，展示研究动机的自然性\n\n---\n\n## 论文各 Section 对应的 Negative Results 使用建议\n\n| Section | 使用的 Negative Results | 功能 |\n|---------|------------------------|------|\n| Introduction | exp_003-005 (event-gate 失败) | 研究动机：试图做 temporal abstraction 但反复失败，转向诊断 why |\n| Section 3.1-3.2 (CIVO 诊断) | exp_009e/009b (CIVO 复现) | 作为 multi-seed 数据点确认 CIVO 可复现性和随机性 |\n| Section 3.3 (Gradient analysis) | exp_016e (reward SGS no-op) | \"梯度 ≠ 因果\" 核心发现 |\n| Section 3.4 (SGS 系列) | exp_018v2/018_s2/021/025/026 | Intervention Hierarchy L1 全面否定；补偿放大 |\n| Section 3.5 (RAVE) | exp_028/028_ceil15 | L2 否定；anchor 污染机制 |\n| Section 3.6 (TCN) | exp_027-031b 全系列 | L3 部分否定；impossible dose；dose-env dependency |\n| Section 3.7 (Dual-critic) | exp_034/036/037/038 | L4 部分否定；v1≈v2；non-CIVO collapse |\n| Section 4 (C6 multi-pathway) | exp_008e_v3_s2/s3 + exp_038 | 多路径脆弱性证据 |\n| Discussion (dt>1 limitation) | exp_006/007/008c/008f_s4 | 即使解决 CIVO，dt>1 仍有 40-70% 性能损失 |\n| Discussion (scope) | exp_051 (StackCube frozen 失败) + exp_036 (PickCube) | Locomotion-specific scope boundary |\n| Discussion (frozen dt_emb) | exp_015b | 不能冻结触发参数——architecturally entangled |\n\n---\n\n## 总结\n\n35 个 negative 实验中：\n- **7 个高 insight**：构成 Intervention Hierarchy + Multi-Pathway Vulnerability 两大核心贡献\n- **10 个中 insight**：提供边界条件、scope limitation、design constraint\n- **10+ 个低 insight**：作为统计数据点计入，不需独立讨论\n\n最重要的 framing 策略：这些 negative results **不是 limitation**，而是论文的 **primary contribution**。一篇 diagnostic paper 的价值恰恰在于系统性地证明某个问题有多难解决，以及为什么难。Intervention Hierarchy（7 methods × 3 levels × 3 environments）是同类工作中最全面的 CIVO 干预评估，其 negative nature 本身就是强贡献。\n"
  }
}
````

</details>

---

### Tool result

_source line 24 · 2026-05-24T18:37:45.295133+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/negative_results_insights.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T18:37:45.295282+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "negative_results_insights",
  "type": "report",
  "description": "35个negative实验的insight提取与ICML论文framing分析：7高/10中/10+低insight，Intervention Hierarchy + Multi-Pathway Vulnerability两大核心贡献定位",
  "project": "event-gated-adaptive-horizon",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/negative_results_insights.md",
  "tags": "['negative_results', 'paper_framing', 'icml', 'intervention_hierarchy']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "negative_results_insights",
    "type": "report",
    "description": "35个negative实验的insight提取与ICML论文framing分析：7高/10中/10+低insight，Intervention Hierarchy + Multi-Pathway Vulnerability两大核心贡献定位",
    "project": "event-gated-adaptive-horizon",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/negative_results_insights.md",
    "tags": "['negative_results', 'paper_framing', 'icml', 'intervention_hierarchy']"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-24T18:37:45.295443+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260524_48b590\", \"name\": \"negative_results_insights\", \"type\": \"report\", \"description\": \"35个negative实验的insight提取与ICML论文framing分析：7高/10中/10+低insight，Intervention Hierarchy + Multi-Pathway Vulnerability两大核心贡献定位\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/report/negative_results_insights.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-24T18:37:30.618583+00:00\", \"tags\": [\"negative_results\", \"paper_framing\", \"icml\", \"intervention_hierarchy\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_negative-results-insight_20260524T183247",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-24T18:37:45.295626+00:00_

产出已写入 `artifacts/negative_results_insights.md` 并注册。核心结论：

**7 个高 insight negative results** 构成论文两大 positive contribution：

1. **Intervention Hierarchy**（SGS/RAVE/TCN/dual-critic 系统性失败）— 证明 CIVO 在所有三个干预层级（gradient/output/representation）都难以可靠缓解，揭示根因是 forward-pass representational entanglement 而非 gradient 或 value magnitude 问题

2. **Multi-Pathway Vulnerability**（exp_008e_v3_s2 + exp_038）— trained dt_emb 通过至少两条路径创造脆弱性（CIVO = value-driven + IRD = eval-driven），消除一条不能保障安全

最有力的单点发现：
- **exp_016e**: 梯度量级 ≠ 因果重要性（reward head 49% 梯度但因果无关）
- **exp_030c**: Cheetah "impossible dose"（CIVO prevention threshold > noise tolerance threshold）
- **exp_034**: v1≈v2（pure-imagination MBRL 中 pessimism 机制失效，ρ>0.999）
- **exp_026**: 补偿放大（阻断一条通路导致 2.6-3.6× 恶化）

这些 negative results 不是 limitation，而是 diagnostic paper 的 primary contribution——系统性证明问题有多难解决。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_negative-results-insight_20260524T183247"
}
```

</details>

---
