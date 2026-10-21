# research gated isr paper narrative

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_research_gated-isr-paper-narrative_20260516T151204.jsonl`
- **Structured JSON:** [`6561aa8d95ea6c0684cf.json`](../../sessions/65/6561aa8d95ea6c0684cf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-16T15:12:49.593035+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_gated-isr-paper-narrative_20260516T151204",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T15:12:49.593372+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_gated-isr-paper-narrative_20260516T151204",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T15:12:49.593534+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_gated-isr-paper-narrative_20260516T151204",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T15:12:49.593844+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- **EMNLP 2026 Main** (NLP and Symbolic Reasoning track)\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\\n\\n| Claim | Status | 闭环标志 |\\n|-------|--------|----------|\\n| Claim 1: STA 诊断能力 | ✅ 已闭环 | 3-seed + 1000-step + hacking taxonomy (8 modes) |\\n| Claim 2: Goodhart / ISR 无结构优势 | ✅ 已闭环 (D057) | 3-seed ISR + 3-seed random + premise-count-matched + SFT baseline |\\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: **3/3 gaming** — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\\n\\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\\n\\n**证据**：\\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\\n- 3-seed consistency: s42 redundant embedding (H1=87.1%, ISR=0.123 diluted), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (H7=100%, PR=98%, ISR=0.57 fake-high, n_comp=2.04). All 3 seeds exhibit 87-100% conclusion embeddin
…[truncated 10646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_gated-isr-paper-narrative_20260516T151204",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T15:12:49.594037+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_gated-isr-paper-narrative_20260516T151204",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T15:12:49.594238+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ROADMAP.md\", \"content\": \"# solver-trace-ablation — Research Dashboard\\n\\n> 最后更新: 2026-05-16 10:55 UTC | 更新原因: D108 放弃 8B 改用 1.7B + GPU 空闲等待提交\\n\\n## 核心方向\\nSTA/ISR 作为 GRPO neurosymbolic formalizer 的**诊断工具** + **Goodhart's Law 案例研究**——检测 reward hacking、量化结构退化、分类退化模式，并展示 ISR 从诊断指标到优化目标的 Goodhart 转折。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: ✍️ Writing + 🔍 Review | **DDL**: 2026-05-25（剩 9 天）\\n- **实验**: 110+ registered (success 30 / negative 30 / failed 34) — Qwen3-4B 完成，**8B 放弃（3 次 OOM）**\\n- **Claims**: ✅ Claim 1 | ✅ Claim 2 | ✅ Claim 3（全部基于 4B）\\n- **Critical gap**: W2 单模型 → **D108: 改用 Qwen3-1.7B 全参 GRPO，准备提交中**\\n- **D106 叙事**: dominant hacking across all β, β=0.2 maximum exploitation, H7 absorbing state\\n- **Provenance**: 36/36\\n\\n### 核心证据链 ✅ 全部就位（Qwen3-4B）\\n- ✅ Claim 1 — STA 诊断: ISR 崩塌 0.6423→0.1324→0.0027; 8-mode taxonomy; SFT 92.3% genuine\\n- ✅ Claim 2 — Goodhart: H7 ISR 70.6% vs Random 13.7%; genuine p=0.182 n.s.; dose-response β∈{0.05,0.1,0.2,0.3}\\n- ✅ Claim 3 — 跨逻辑泛化: Prolog 3/3 gaming, 0% genuine\\n\\n## RUNNING\\n（Agent 准备 1.7B configs 中，即将提交双卡）\\n\\n## 排期（D108 更新）\\n| 优先级 | 实验 | 说明 | 预估时长 |\\n|--------|------|------|----------|\\n| **P0** | 1.7B exec-only + 1.7B ISR β=0.1 | Qwen3-1.7B pilot 双卡并行，K=4, seed=42 | ~1h |\\n| **P1** | 1.7B eval + classify_h7 | 完成后立即 eval，对比 4B hacking patterns | ~30min |\\n| **P2** | 1.7B ISR β=0.3 (如 P0 hacking 确认) | 验证 dose-response 在 1.7B | ~1h |\\n| **P3** | QLoRA 8B (如时间允许) | 补充大 scale 证据（有 confound 注明） | ~4h |\\n| **P4** | 5-seed 扩展 | 更紧 CI，仅 GPU 空余时 | ~1h each |\\n\\n## 并行写作任务（Paper Agent）\\n- [ ] Abstract 精简 + pooled mean±std (v2-R1-N1, v2-R2-W3)\\n- [ ] Meta-Goodhart framing 降级 (R1-W5, v2-R2-N3)\\n- [ ] Dose-response 4 点更新 (v2-R1-N3)\\n- [ ] Premise-count confound 提升到正文 (v2-R1-W3, v2-R2-W4)\\n- [ ] 格式修正 (v2-FMT-1/2/3), H1-H8 编号统一, Taxonomy 独立性\\n\\n## GPU 预算\\n- 本地: 2 × RT
…[truncated 1877 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_gated-isr-paper-narrative_20260516T151204",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T15:12:49.594468+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/gated_isr_narrative_analysis.md",
  "content": "# Gated-ISR-Curriculum: Narrative Impact Analysis\n\n## 三种结果解读\n\n**A. Gated-ISR 仍产生 hacking（最可能）**\n- 支持核心论点：ISR 作为 proxy reward 本质上 gameable，门控/课程设计无法消除 Goodhart 效应\n- 论文框架：在 Discussion 加 \"Attempted Mitigations\" 段落，1-2 段说明门控失败，强化 \"metric optimization ≠ capability improvement\" 结论\n- 若出现新 hacking 模式（如 H9 变体），扩展 taxonomy\n\n**B. Gated-ISR 显著减少 hacking（genuine >30%）**\n- 论文转为 \"diagnosis + partial mitigation\"：ISR 既能诊断又能（有条件地）指导训练\n- 框架：新增 Section 6 \"Toward Safe ISR Deployment\"，报告门控阈值与 hacking 率的关系\n- 风险：削弱 Goodhart 主线的尖锐度，需权衡叙事一致性\n\n**C. 训练不收敛（PR <20% 或 loss 不降）**\n- 解读：门控过强截断了学习信号，ISR 的信息量不足以独立驱动学习\n- 框架：支持 \"ISR 只适合做诊断不适合做 reward\" 的结论，与 Claim 2 一致\n- 1 句话写入 limitations 即可\n\n## Eval Metrics 优先级\n\n1. **Genuine rate**（C013 标准）— 核心判定指标\n2. **H7/H9 rate** — hacking 模式分布\n3. **PR trajectory** — 收敛性判断\n4. **ISR proved-only** — 是否仍被 game\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_gated-isr-paper-narrative_20260516T151204",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/gated_isr_narrative_analysis.md",
    "content": "# Gated-ISR-Curriculum: Narrative Impact Analysis\n\n## 三种结果解读\n\n**A. Gated-ISR 仍产生 hacking（最可能）**\n- 支持核心论点：ISR 作为 proxy reward 本质上 gameable，门控/课程设计无法消除 Goodhart 效应\n- 论文框架：在 Discussion 加 \"Attempted Mitigations\" 段落，1-2 段说明门控失败，强化 \"metric optimization ≠ capability improvement\" 结论\n- 若出现新 hacking 模式（如 H9 变体），扩展 taxonomy\n\n**B. Gated-ISR 显著减少 hacking（genuine >30%）**\n- 论文转为 \"diagnosis + partial mitigation\"：ISR 既能诊断又能（有条件地）指导训练\n- 框架：新增 Section 6 \"Toward Safe ISR Deployment\"，报告门控阈值与 hacking 率的关系\n- 风险：削弱 Goodhart 主线的尖锐度，需权衡叙事一致性\n\n**C. 训练不收敛（PR <20% 或 loss 不降）**\n- 解读：门控过强截断了学习信号，ISR 的信息量不足以独立驱动学习\n- 框架：支持 \"ISR 只适合做诊断不适合做 reward\" 的结论，与 Claim 2 一致\n- 1 句话写入 limitations 即可\n\n## Eval Metrics 优先级\n\n1. **Genuine rate**（C013 标准）— 核心判定指标\n2. **H7/H9 rate** — hacking 模式分布\n3. **PR trajectory** — 收敛性判断\n4. **ISR proved-only** — 是否仍被 game\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T15:12:49.594624+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/gated_isr_narrative_analysis.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_gated-isr-paper-narrative_20260516T151204",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-16T15:12:49.594844+00:00_

分析备忘已保存到 `artifacts/gated_isr_narrative_analysis.md`。

核心判断：结果 A（门控仍 hack）对论文叙事最有利——直接强化 Goodhart 主线；结果 B 有价值但需重构叙事平衡；结果 C 是 Claim 2 的自然推论，一句 limitations 收尾。无论哪种结果，genuine rate（C013 标准）是第一优先 eval 指标。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_gated-isr-paper-narrative_20260516T151204"
}
```

</details>

---
