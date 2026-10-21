# research evidence chain audit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_research_evidence-chain-audit_20260514T055852.jsonl`
- **Structured JSON:** [`1c43973c9bb3ff8111da.json`](../../sessions/1c/1c43973c9bb3ff8111da.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-14T06:01:34.897452+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-chain-audit_20260514T055852",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T06:01:34.897842+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-chain-audit_20260514T055852",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T06:01:34.898037+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "filters": "{'status': 'DONE'}",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-chain-audit_20260514T055852",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "filters": "{'status': 'DONE'}",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T06:01:34.898175+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-chain-audit_20260514T055852",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T06:01:34.898795+00:00_

&lt;persisted-output>
Output too large (51KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/ec8bb1db-21fb-4df7-b14b-bdfed532b410/tool-results/toolu_01FB2Dvjgyj8wStaW96xyy2T.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan017-additive-random-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:11:14.694Z\", \"updated_at\": \"2026-05-14T05:33:25.603Z\", \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。\", \"parent\": \"plan013-random-reward-s42-r4\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random)\", \"plan_id\": \"plan017\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"beta\": 0.3}, \"pid\": \"207116\", \"log_path\": \"~/runs/solver-trace-ablation/plan017-additive-random-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 
…[truncated 316 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-chain-audit_20260514T055852",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T06:01:34.899089+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — 诊断/分析论文)\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**:\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\\n- Hacking taxonomy: 5 distinct modes identified and quantified (plan012 `hacking_characterization_report.md` + plan017 D027)\\n\\n### Claim 2: GRPO Saturation Mechanism\\nExec-only GRPO exhibits a saturation failure mode: when prove_rate → 1.0, reward_std → 0 and loss → 0, training effectively stalls. Any reward component introducing variance (ISR, random noise) prevents saturation but does not prevent hacking — it redirects hacking into different structural failure modes.\\n\\n**证据**:\\n- plan001 exec-only: PR saturation → loss=0 → learning stops (D014)\\n- plan013 random reward: PR=1.0 (prevents saturation) but 100% P→P tautological collapse (D018)\\n- plan002 additive ISR β=0.3: PR=18%, ISR=0
…[truncated 8215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-chain-audit_20260514T055852",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T06:01:34.899290+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/ec8bb1db-21fb-4df7-b14b-bdfed532b410/tool-results/toolu_01FB2Dvjgyj8wStaW96xyy2T.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-chain-audit_20260514T055852",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/ec8bb1db-21fb-4df7-b14b-bdfed532b410/tool-results/toolu_01FB2Dvjgyj8wStaW96xyy2T.txt"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T06:01:34.899933+00:00_

1	{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan017-additive-random-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:11:14.694Z\", \"updated_at\": \"2026-05-14T05:33:25.603Z\", \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。\", \"parent\": \"plan013-random-reward-s42-r4\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random)\", \"plan_id\": \"plan017\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"beta\": 0.3}, \"pid\": \"207116\", \"log_path\": \"~/runs/solver-trace-ablation/plan017-additive-random-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"finished_at\": \"2026-05-14T05:17:13.920Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:17:18.376399+00:00\"}]}, \"conclusion\": \"negative\"
…[truncated 50231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-chain-audit_20260514T055852",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T06:01:34.900490+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "evidence_audit",
  "type": "report",
  "description": "论文 Table 1 数据审计 + 3 claims 证据覆盖度分析",
  "project": "solver-trace-ablation",
  "content_filename": "evidence_audit.md",
  "content": "# Evidence Audit — solver-trace-ablation\nGenerated: 2026-05-14\n\n---\n\n## 1. Table 1: Six-Condition Comparison (Registry-Verified)\n\nAll metrics sourced from `eval_sta.py full STA` on `proofwriter_fol_100.jsonl` unless noted.\n\n| # | Condition | exp_id | Reward Formula | eval PR | eval ISR | proved_only_ISR | n_components | Degeneration Mode |\n|---|-----------|--------|----------------|---------|----------|-----------------|--------------|-------------------|\n| 1 | Exec-only s42 | `plan001-exec-only-s42-r2` | r_exec | 93% | 0.1232 | 0.1324 | **6.58 ⚠️** | Genuine (only healthy seed) |\n| 2 | Exec-only s43 | `plan001-exec-only-s43-r4` | r_exec | **14% ⚠️** | 0.000 | 0.000 | **N/A ⚠️** | Length explosion (87% hit max_tokens) |\n| 3 | Exec-only s44 | `plan001-exec-only-s44` | r_exec | 98% | 0.5700 | 0.5816 | 2.04 | Tautological (94/100 = 2-component) |\n| 4 | Random reward | `plan013-random-reward-s42-r4` | 0.9·r_exec + 0.1·random | 100% | 0.5350 | 0.5350 | **2.04 ⚠️** | Tautological (100% P→P) |\n| 5 | Additive ISR β=0.3 | `plan002-additive-b03-s42` | r_exec·(1+0.3·ISR) | 18% | 0.0257 | 0.1427 | **10.67 ⚠️** | Repetitive cycling / format collapse |\n| 6 | Additive random β=0.3 | `plan017-additive-random-s42` | r_exec·(1+0.3·random) | 48% | 0.0453 | 0.0943 | 9.60 | Complexity-without-utility |\n\n### Discrepancies & Missing Data\n\n#### ❌ plan001-s43 eval PR: 14% not 13%\n- Registry: `eval_sampling_prove_rate=0.14`, `eval_sampling_n_proved=14` → **14%**\n- Task description and notes both say \"13%\" — **错误，应为 14%**\n- 论文必须使用 14%\n\n#### ⚠️ plan001-s43 eval method 不一致\n- s43 使用 `eval_sampling` (do_sample=True, temperature=0.7)\n- 其他 5 组全部使用 `eval_sta.py full STA` (deterministic)\n- **论文中必须标注 s43 的评估方法差异，或用 eval_sta.py 重新评估 s43 以保持一致性**\n\n#### ⚠️ n_components 数据追溯\n| Condition | In Registry? | Source |\n|-----------|-------------|--------|\n| plan001-s42 (6.58) | ❌ 不在 registry metrics 中 | 需追溯来源（可能是独立 eval 脚本输出或 artifact） |\n| plan001-s43 (N/A) | ❌ 无评估数据 | s43 未做 component count 评估 |\n| plan001-s44 (2.04) | ✅ `eval_component_count_mean=2.04` | Registry |\n| plan013 (2.04) | ❌ 仅在 eval_note 中提及 | 需补入 registry metrics 或标注来源 |\n| plan002 (10.67) | ❌ 不在 registry 中 | 需追溯来源 |\n| plan017 (9.60) | ✅ `eval_component_count_mean=9.6` | Registry |\n\n**结论：6 组实验中仅 2 组 (s44, plan017) 的 component count 在 registry 中有记录。plan001-s42、plan013、plan002 的 component count 需要补充来源或重新评估。**\n\n#### ⚠️ plan002 eval metrics 存储位置异常\n- plan002 的 eval 指标存储在 registry 顶层字段（`eval_prove_rate`, `eval_mean_isr` 等），而非 `metrics` dict 内\n- `metrics` dict 内仅有训练日志指标\n- 不影响数值正确性，但建议统一存储格式\n\n---\n\n## 2. 证据覆盖审计：3 Claims\n\n### Claim 1: ISR as Reward Hacking Diagnostic\n\n**状态：✅ 证据充分（1 处需补充）**\n\n| 证据点 | 支撑实验 | Registry 可追溯 | 状态 |\n|--------|---------|----------------|------|\n| ISR 崩塌轨迹：0.6423 → 0.1324 | plan003 (100步) + plan001-s42 (500步) | ✅ proved_only_isr 均在 registry | 完整 |\n| Base model ISR anchor | sta-phase0-baseline | ✅ mean_isr=0.0641 | 完整 |\n| 3-seed 分化（genuine/explosion/tautological） | plan001-s42-r2, s43-r4, s44 | ✅ eval metrics 均在 | 完整 |\n| Hacking taxonomy (5 modes) | plan012 artifact + plan017 D027 | ❌ plan012 不是 registry 实验 | **需标注 artifact 来源** |\n| Component count 辅助诊断 | 见 Table 1 | ⚠️ 3/6 组缺 registry 来源 | 需补充 |\n\n**Gap**: plan001-s43 需用 eval_sta.py 重新评估（当前是 sampling eval），否则论文 Table 1 中 s43 的评估方法与其他 5 组不一致。\n\n### Claim 2: GRPO Saturation Mechanism\n\n**状态：✅ 证据充分**\n\n| 证据点 | 支撑实验 | Registry 可追溯 | 状态 |\n|--------|---------|----------------|------|\n| Exec-only PR→1.0, loss→0 | plan001-s44: train_last100_loss=0.000419 | ✅ | 完整 |\n| Random reward prevents saturation but tautological | plan013-r4: eval_prove_rate=1.0 | ✅ | 完整 |\n| ISR bonus PR=18% (最差) | plan002: eval_prove_rate=0.18 | ✅ | 完整 |\n| Random bonus PR=48% > ISR 18% | plan017: eval_prove_rate=0.48 | ✅ | 完整 |\n| Convex combination = penalty | plan005: last100_prove_rate=0.7725 | ✅ | 完整 |\n| ISR actively misleading (not just noisy) | plan002 vs plan017 对比 | ✅ 两组 eval 均在 | 完整 |\n\n**写作约束提醒（D027）**：\n- plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同\n- 纯净对比仅限 plan002 vs plan017（唯一变量：ISR vs random）\n- 禁止将 plan013 vs plan017 简化为 \"additive vs convex\"\n\n### Claim 3: Cross-Logic Generality\n\n**状态：❌ 无证据**\n\n- plan006 (Prolog GRPO) 未启动，无任何实验数据\n- 如 DDL 前无法完成 → 降级为 Future Work\n- 论文可用 \"STA protocol is solver-agnostic by design\" 作为理论论证，但无实证支撑\n\n---\n\n## 3. 辅助实验证据\n\n| 实验 | exp_id | 结论 | 论文用途 |\n|------|--------|------|---------|\n| Base model baseline | `sta-phase0-baseline` | PR=12%, ISR=0.064 | ISR 起点锚定 |\n| 100-step eval | `plan003-eval-exec-only-r5` | PR=32%, proved_ISR=0.642 | ISR 崩塌前的高点 |\n| Convex combination | `plan005-sta-low-s42` | PR=77%, ISR/PR ratio=0.30 | ISR penalty 效应 |\n| Downstream NLI | `plan014-downstream-nli-s42` | ρ=-0.049, not significant | ISR capability boundary (Limitation) |\n| GT ISR baseline | `sta-gt-isr-baseline` | GT ISR=0.559, PR=18% | Ground truth 参照 |\n\n---\n\n## 4. 待完成实验能填补的 Gap\n\n| 实验 | 预期贡献 |\n|------|---------|\n| **plan002-b01** (additive ISR β=0.1) | ISR-as-reward 在更低 β 下是否仍然 harmful；如 PR 仍低 → 强化 \"ISR misleading\" 结论 |\n| **plan016** (extended 1000+ steps) | 解答 reviewer Q5 \"500 steps too short\"；验证 hacking 是否在更长训练后加剧 |\n| **plan006** (Prolog GRPO) | Claim 3 唯一实证来源；无此实验则 Claim 3 删除或降级 |\n| **plan001-s43 重新评估** | 用 eval_sta.py full STA 重新评估 s43 checkpoint，统一评估方法 |\n\n---\n\n## 5. 论文写作可立即启动的章节\n\n以下章节的证据已完整，不依赖任何未完成实验：\n\n1. **Introduction + Problem Statement** — 基于 plan001 3-seed 分化 + ISR 崩塌轨迹\n2. **Method (STA/ISR 定义)** — 纯方法论，不依赖实验\n3. **Results §4.1: ISR Diagnostic** (Claim 1 核心) — plan003 + plan001-s42 ISR 轨迹，3-seed 分化\n4. **Results §4.2: GRPO Saturation** (Claim 2) — plan001/plan002/plan013/plan017 完整\n5. **Results §4.3: Hacking Taxonomy** — 5 modes 均已在 DONE 实验中观测到\n6. **Discussion: ISR Capability Boundary** — plan014 negative result\n7. **Related Work** — literature_map.yaml 29 refs\n\n**暂缓章节**：\n- §4.4 Cross-Logic Generality → 等 plan006 或直接写成 Future Work\n- §4.X Extended Training → 等 plan016\n\n---\n\n## 6. 行动建议（按优先级）\n\n1. **[紧急]** 用 eval_sta.py 重新评估 plan001-s43-r4 checkpoint，统一评估方法 + 获取 component count\n2. **[紧急]** 追溯 plan001-s42 和 plan002 的 component count 来源，补入 registry\n3. **[紧急]** 修正所有引用 \"s43 PR=13%\" 的地方为 **14%**（registry metric: 0.14）\n4. **[重要]** 补充 plan013 的 component count 到 registry metrics\n5. **[重要]** 统一 plan002 的 eval metrics 存储位置到 metrics dict 内\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_evidence-chain-audit_20260514T055852",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "evidence_audit",
    "type": "report",
    "description": "论文 Table 1 数据审计 + 3 claims 证据覆盖度分析",
    "project": "solver-trace-ablation",
    "content_filename": "evidence_audit.md",
    "content": "# Evidence Audit — solver-trace-ablation\nGenerated: 2026-05-14\n\n---\n\n## 1. Table 1: Six-Condition Comparison (Registry-Verified)\n\nAll metrics sourced from `eval_sta.py full STA` on `proofwriter_fol_100.jsonl` unless noted.\n\n| # | Condition | exp_id | Reward Formula | eval PR | eval ISR | proved_only_ISR | n_components | Degeneration Mode |\n|---|-----------|--------|----------------|---------|----------|-----------------|--------------|-------------------|\n| 1 | Exec-only s42 | `plan001-exec-only-s42-r2` | r_exec | 93% | 0.1232 | 0.1324 | **6.58 ⚠️** | Genuine (only healthy seed) |\n| 2 | Exec-only s43 | `plan001-exec-only-s43-r4` | r_exec | **14% ⚠️** | 0.000 | 0.000 | **N/A ⚠️** | Length explosion (87% hit max_tokens) |\n| 3 | Exec-only s44 | `plan001-exec-only-s44` | r_exec | 98% | 0.5700 | 0.5816 | 2.04 | Tautological (94/100 = 2-component) |\n| 4 | Random reward | `plan013-random-reward-s42-r4` | 0.9·r_exec + 0.1·random | 100% | 0.5350 | 0.5350 | **2.04 ⚠️** | Tautological (100% P→P) |\n| 5 | Additive ISR β=0.3 | `plan002-additive-b03-s42` | r_exec·(1+0.3·ISR) | 18% | 0.0257 | 0.1427 | **10.67 ⚠️** | Repetitive cycling / format collapse |\n| 6 | Additive random β=0.3 | `plan017-additive-random-s42` | r_exec·(1+0.3·random) | 48% | 0.0453 | 0.0943 | 9.60 | Complexity-without-utility |\n\n### Discrepancies & Missing Data\n\n#### ❌ plan001-s43 eval PR: 14% not 13%\n- Registry: `eval_sampling_prove_rate=0.14`, `eval_sampling_n_proved=14` → **14%**\n- Task description and notes both say \"13%\" — **错误，应为 14%**\n- 论文必须使用 14%\n\n#### ⚠️ plan001-s43 eval method 不一致\n- s43 使用 `eval_sampling` (do_sample=True, temperature=0.7)\n- 其他 5 组全部使用 `eval_sta.py full STA` (deterministic)\n- **论文中必须标注 s43 的评估方法差异，或用 eval_sta.py 重新评估 s43 以保持一致性**\n\n#### ⚠️ n_components 数据追溯\n| Condition | In Registry? | Source |\n|-----------|-------------|--------|\n| plan001-s42 (6.58) | ❌ 不在 registry metrics 中 | 需追溯来源（可能是独立 eval 脚本输出或 artifact） |\n| plan001-s43 (N/A) | ❌ 无评估数据 | s43 未做 component count 评估 |\n| plan001-s44 (2.04) | ✅ `eval_component_count_mean=2.04` | Registry |\n| plan013 (2.04) | ❌ 仅在 eval_note 中提及 | 需补入 registry metrics 或标注来源 |\n| plan002 (10.67) | ❌ 不在 registry 中 | 需追溯来源 |\n| plan017 (9.60) | ✅ `eval_component_count_mean=9.6` | Registry |\n\n**结论：6 组实验中仅 2 组 (s44, plan017) 的 component count 在 registry 中有记录。plan001-s42、plan013、plan002 的 component count 需要补充来源或重新评估。**\n\n#### ⚠️ plan002 eval metrics 存储位置异常\n- plan002 的 eval 指标存储在 registry 顶层字段（`eval_prove_rate`, `eval_mean_isr` 等），而非 `metrics` dict 内\n- `metrics` dict 内仅有训练日志指标\n- 不影响数值正确性，但建议统一存储格式\n\n---\n\n## 2. 证据覆盖审计：3 Claims\n\n### Claim 1: ISR as Reward Hacking Diagnostic\n\n**状态：✅ 证据充分（1 处需补充）**\n\n| 证据点 | 支撑实验 | Registry 可追溯 | 状态 |\n|--------|---------|----------------|------|\n| ISR 崩塌轨迹：0.6423 → 0.1324 | plan003 (100步) + plan001-s42 (500步) | ✅ proved_only_isr 均在 registry | 完整 |\n| Base model ISR anchor | sta-phase0-baseline | ✅ mean_isr=0.0641 | 完整 |\n| 3-seed 分化（genuine/explosion/tautological） | plan001-s42-r2, s43-r4, s44 | ✅ eval metrics 均在 | 完整 |\n| Hacking taxonomy (5 modes) | plan012 artifact + plan017 D027 | ❌ plan012 不是 registry 实验 | **需标注 artifact 来源** |\n| Component count 辅助诊断 | 见 Table 1 | ⚠️ 3/6 组缺 registry 来源 | 需补充 |\n\n**Gap**: plan001-s43 需用 eval_sta.py 重新评估（当前是 sampling eval），否则论文 Table 1 中 s43 的评估方法与其他 5 组不一致。\n\n### Claim 2: GRPO Saturation Mechanism\n\n**状态：✅ 证据充分**\n\n| 证据点 | 支撑实验 | Registry 可追溯 | 状态 |\n|--------|---------|----------------|------|\n| Exec-only PR→1.0, loss→0 | plan001-s44: train_last100_loss=0.000419 | ✅ | 完整 |\n| Random reward prevents saturation but tautological | plan013-r4: eval_prove_rate=1.0 | ✅ | 完整 |\n| ISR bonus PR=18% (最差) | plan002: eval_prove_rate=0.18 | ✅ | 完整 |\n| Random bonus PR=48% > ISR 18% | plan017: eval_prove_rate=0.48 | ✅ | 完整 |\n| Convex combination = penalty | plan005: last100_prove_rate=0.7725 | ✅ | 完整 |\n| ISR actively misleading (not just noisy) | plan002 vs plan017 对比 | ✅ 两组 eval 均在 | 完整 |\n\n**写作约束提醒（D027）**：\n- plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同\n- 纯净对比仅限 plan002 vs plan017（唯一变量：ISR vs random）\n- 禁止将 plan013 vs plan017 简化为 \"additive vs convex\"\n\n### Claim 3: Cross-Logic Generality\n\n**状态：❌ 无证据**\n\n- plan006 (Prolog GRPO) 未启动，无任何实验数据\n- 如 DDL 前无法完成 → 降级为 Future Work\n- 论文可用 \"STA protocol is solver-agnostic by design\" 作为理论论证，但无实证支撑\n\n---\n\n## 3. 辅助实验证据\n\n| 实验 | exp_id | 结论 | 论文用途 |\n|------|--------|------|---------|\n| Base model baseline | `sta-phase0-baseline` | PR=12%, ISR=0.064 | ISR 起点锚定 |\n| 100-step eval | `plan003-eval-exec-only-r5` | PR=32%, proved_ISR=0.642 | ISR 崩塌前的高点 |\n| Convex combination | `plan005-sta-low-s42` | PR=77%, ISR/PR ratio=0.30 | ISR penalty 效应 |\n| Downstream NLI | `plan014-downstream-nli-s42` | ρ=-0.049, not significant | ISR capability boundary (Limitation) |\n| GT ISR baseline | `sta-gt-isr-baseline` | GT ISR=0.559, PR=18% | Ground truth 参照 |\n\n---\n\n## 4. 待完成实验能填补的 Gap\n\n| 实验 | 预期贡献 |\n|------|---------|\n| **plan002-b01** (additive ISR β=0.1) | ISR-as-reward 在更低 β 下是否仍然 harmful；如 PR 仍低 → 强化 \"ISR misleading\" 结论 |\n| **plan016** (extended 1000+ steps) | 解答 reviewer Q5 \"500 steps too short\"；验证 hacking 是否在更长训练后加剧 |\n| **plan006** (Prolog GRPO) | Claim 3 唯一实证来源；无此实验则 Claim 3 删除或降级 |\n| **plan001-s43 重新评估** | 用 eval_sta.py full STA 重新评估 s43 checkpoint，统一评估方法 |\n\n---\n\n## 5. 论文写作可立即启动的章节\n\n以下章节的证据已完整，不依赖任何未完成实验：\n\n1. **Introduction + Problem Statement** — 基于 plan001 3-seed 分化 + ISR 崩塌轨迹\n2. **Method (STA/ISR 定义)** — 纯方法论，不依赖实验\n3. **Results §4.1: ISR Diagnostic** (Claim 1 核心) — plan003 + plan001-s42 ISR 轨迹，3-seed 分化\n4. **Results §4.2: GRPO Saturation** (Claim 2) — plan001/plan002/plan013/plan017 完整\n5. **Results §4.3: Hacking Taxonomy** — 5 modes 均已在 DONE 实验中观测到\n6. **Discussion: ISR Capability Boundary** — plan014 negative result\n7. **Related Work** — literature_map.yaml 29 refs\n\n**暂缓章节**：\n- §4.4 Cross-Logic Generality → 等 plan006 或直接写成 Future Work\n- §4.X Extended Training → 等 plan016\n\n---\n\n## 6. 行动建议（按优先级）\n\n1. **[紧急]** 用 eval_sta.py 重新评估 plan001-s43-r4 checkpoint，统一评估方法 + 获取 component count\n2. **[紧急]** 追溯 plan001-s42 和 plan002 的 component count 来源，补入 registry\n3. **[紧急]** 修正所有引用 \"s43 PR=13%\" 的地方为 **14%**（registry metric: 0.14）\n4. **[重要]** 补充 plan013 的 component count 到 registry metrics\n5. **[重要]** 统一 plan002 的 eval metrics 存储位置到 metrics dict 内\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T06:01:34.900773+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_6b5acb\", \"name\": \"evidence_audit\", \"type\": \"report\", \"description\": \"论文 Table 1 数据审计 + 3 claims 证据覆盖度分析\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/report/evidence_audit.md\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T06:01:24.805724+00:00\", \"tags\": []}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_evidence-chain-audit_20260514T055852",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-14T06:01:34.900979+00:00_

产出已写入 `artifacts/_project/report/evidence_audit.md`。核心发现：

**Table 1 数据问题（3 个需立即处理）：**

1. **plan001-s43 PR 应为 14% 而非 13%** — registry 记录 `eval_sampling_n_proved=14`，所有引用 "13%" 的地方需修正
2. **plan001-s43 评估方法不一致** — s43 用 `eval_sampling` (temperature=0.7)，其他 5 组全用 `eval_sta.py full STA`。论文 Table 1 需统一，建议对 s43 checkpoint 重跑 eval_sta.py
3. **3/6 组缺少 component count 的 registry 来源** — plan001-s42 (6.58)、plan013 (2.04)、plan002 (10.67) 的 n_components 不在 registry 中，需追溯来源或重新评估后补入

**证据覆盖度：**
- Claim 1 (ISR 诊断): ✅ 充分，1 处需补充 (s43 评估方法统一)
- Claim 2 (GRPO 饱和): ✅ 充分，5 组实验全部可追溯
- Claim 3 (跨逻辑泛化): ❌ 无证据，plan006 未启动

**可立即启动写作的章节**：Introduction、Method、Results §4.1-4.3、Discussion (ISR boundary)、Related Work。仅 §4.4 Cross-Logic 和 Extended Training 依赖未完成实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_evidence-chain-audit_20260514T055852"
}
```

</details>

---
