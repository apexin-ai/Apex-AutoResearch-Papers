# research route b design

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_research_route_b_design_20260519T104143.jsonl`
- **Structured JSON:** [`31cb8a0435f106dad933.json`](../../sessions/31/31cb8a0435f106dad933.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-19T10:45:06.718292+00:00_

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
  "session": "worker_research_route_b_design_20260519T104143",
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

_source line 2 · 2026-05-19T10:45:06.718893+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T10:45:06.719561+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "turn_residual_gating",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T10:45:06.720219+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper_framing.md\", \"content\": \"# Paper Framing: ThreadGate\\n\\n> 定位: **Solution paper**. Dongre et al. (2605.12922) 已独立诊断 GAR 衰减问题，ThreadGate 是首个架构级干预方案。\\n> 目标会议: EMNLP 2026, ARR August cycle, deadline 2026-08-03 (~10.5 weeks)\\n> 最后更新: 2026-05-19 (D014/D015 negative findings 纳入)\\n\\n---\\n\\n## 1. Title Candidates\\n\\n- **T1**: ThreadGate: Recovering Goal Attention in Multi-Turn Dialogue via Learnable Residual Gating\\n- **T2**: Per-Layer Residual Gates for Goal Attention Recovery in Multi-Turn LLM Conversations\\n- **T3**: ThreadGate: Restoring Goal Awareness in Multi-Turn Dialogue Through Turn-Conditioned Residual Gating\\n\\n推荐 T1: 简洁，包含方法名、核心机制(residual gating)、目标(goal attention recovery)。\\n\\n---\\n\\n## 2. Story Arc\\n\\nMulti-turn dialogue performance in LLMs degrades as conversations grow longer, a phenomenon recently quantified by Dongre et al. (2026) through the Goal Attention Ratio (GAR), which drops 27-48% over 50 turns. Our independent Phase 1 measurement on Qwen2.5-7B confirms severe decay at 70.8% over 10 turns (the larger magnitude reflects a broader goal token definition that includes the first user query; see Section 7 for definition comparison). Their mechanistic analysis reveals a striking paradox: while attention to goal-specifying tokens steadily diminishes, the goal information itself persists in the residual stream (probe AUC up to 0.98). This means the model retains the knowledge of what it should do, but its attention mechanism progressively fails to access it. We propose ThreadGate, a lightweight per-layer gating module inserted on frozen LLM residual connections, conditioned on turn boundary signals. Each layer learns an independent scalar gate g controlling the residual contribution as x + g·f(x), allowing the model to selectively modulate information flow at layers most relevant to goal encoding.
…[truncated 7269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T10:45:06.720470+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "turn_residual_gating",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T10:45:06.720678+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/memory.md\", \"content\": \"# Memory — turn_residual_gating\\n\\n## GAR Loss 模式演化教训\\n\\n### maximize 模式的结构性缺陷（v3/v3b/v5 验证）\\n- maximize (L_GAR = -mean(GAR)) 无界，驱动 gate 趋向恒等（gate→1 = 全通过 = 最大 GAR）\\n- v3b (λ=10, 500步): gate_std=0.087 但 L_GAR 已饱和 -0.96\\n- v5 (λ=1.0, 2400步): gate_std 从 0.034 降至 0.022，gate_mean 从 0.81 升至 0.965，确认长训练下分化完全消失\\n- 结论：maximize 只在短训练+大λ下产生暂态分化，不可用于正式训练\\n\\n### smooth_saturation 也失败（v6 验证）\\n- 公式: -target * tanh(GAR / target)，有界但仍单调奖励 GAR↑\\n- v6 step 100: gate_std=0.037↓ gate_mean=0.874↑，与 maximize 同轨迹\\n- 结论：**所有单调奖励 GAR↑ 的 loss 都会导致恒等退化**，不管有界无界\\n\\n### hinge_target 的梯度消失问题\\n- hinge_target (F.relu(target - mean_GAR)) 在 GAR 达标后梯度=0\\n- v1/v2 的 cumulative/pairwise 也有类似退化平衡点问题\\n- 不适合作为持续训练信号\\n\\n### MSE + gate_div：首个结构性不同的设计（v7 验证通过）\\n- MSE = (mean_GAR - target)²：双向，GAR > target 也受惩罚\\n- gate_div = F.relu(min_std - gate_std)：直接强制层间分化\\n- v7 dry-run: gate_std 0.034→0.088（5 步），L_GAR 为正（0.23），total loss 始终正\\n- v7 gs87: GAR 突破 0.05 阈值（从 0.016→0.066），呈加速趋势\\n- gate_div 按需启动（std<0.05 触发）、达标停止（std>0.05 归零）\\n- **v7 最终结果 (3 epoch)**：gate_std 全程稳定 0.049-0.054，L3/L4 持续最低（0.789/0.801），GAR 收敛到 target 附近（L_GAR≈0.001），NTP 正常收敛 0.896。Identity collapse 被阻止\\n\\n## v7 Eval 关键发现（2026-05-19, D014）\\n\\n### GAR 过拟合：训练 0.48 vs 推理 0.016（30x 断层）\\n- 逐行对比 gar.py（训练）vs eval_phase2_gar.py（推理）：goal tokens、query positions、GAR 公式、forward pass 方式全部一致，不是 measurement bug\\n- 根因：模型在 ultrachat 训练数据上学到 GAR≈0.5，但 attention pattern 不泛化到 eval 数据\\n- 推论：GAR 作为训练信号存在泛化性根本问题\\n\\n### Gate turn conditioning 方向反转（D014 确认）\\n- Gate dynamic range 显示：早期 turn（goal attention 高）→ gate 值低（0.75-0.86，强抑制）；晚期 turn（goal attention 低）→ gate 值高（0.93-0.98，近乎恒等）\\n- 预期是晚期 turn 更强干预来恢复 goal attention，实际相反\\n- Reviewer 分析：这是 NTP-GAR 损失竞争的结构性后果，不是调 conditioning 方向能修的\\n- 结论：ThreadGate 正面 story 不成立（D014）\\n\\n### Eval baseline confound\\n- Phase1 baseline 用 BASE 模型
…[truncated 1918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T10:45:06.720852+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "ROADMAP.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "turn_residual_gating",
    "file": "ROADMAP.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T10:45:06.721033+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md\", \"content\": \"# turn_residual_gating — Research Dashboard\\n\\n> 最后更新: 2026-05-19 10:06 UTC | 更新原因: UG 完成 + LoRA-only 47.5% 进度更新\\n\\n> 核心方向详见 paper_framing.md\\n\\n## 核心方向\\nThreadGate: 冻结 LLM 残差连接上插入 turn-boundary-conditioned gating，修复多轮对话 GAR 衰减。\\n\\n**目标 venue**: EMNLP 2026（ARR August cycle, deadline 2026-08-03, ~10 weeks）\\n\\n## 当前进展\\n- **阶段**: MVP 验证 — 三路消融最后一组（LoRA-only）训练中，完成后四路 eval 做最终判定\\n- **Phase 1**: GAR 衰减 70.8% 确认 ✅\\n- **Phase 2 v7 (TG)**: 训练成功但推理 GAR recovery 仅 +0.35pp/+0.72pp（远低于 3pp 门槛）\\n- **Phase 2 UG**: 训练完成 ✅，per-layer independent gates without turn conditioning\\n- **Phase 2 LoRA-only**: 训练中 ~47.5%（预计 ~3h 后完成）\\n- **v7 关键 negative findings (D014/D015)**:\\n  - 反向 turn conditioning: 27/28 层 gate 在后续 turns 趋向 identity\\n  - GAR 过拟合: 训练 0.48 vs 推理 0.016（30x 断层，confirmed non-bug）\\n  - NTP-GAR 梯度竞争: GAR 收敛后 NTP 接管，推 gate→identity\\n- **v1-v6 全部 negative/failed**: 单调 GAR 奖励结构性失败\\n\\n## 两路策略 (D017)\\n\\n**路线 A: Gating 有效（two-stage decoupled training）**\\n- 前提: LoRA-only < TG（gating 有非零贡献）\\n- Stage 1: gate-only + GAR loss → Stage 2: freeze gate + LoRA NTP\\n- 成功概率 ~20-30%，ceiling 高（main track）\\n- GPU: 15-21h 额外\\n\\n**路线 B: Negative result + mechanistic insight**\\n- 前提: LoRA-only ≈ TG（gating 贡献为零）\\n- Story: 首次系统性 residual gating 干预 + 完整失败机制分析\\n- 竞争力: Findings ~70% / main track 需跨模型验证\\n- GPU: 6-12h 额外（跨模型）\\n\\n**Gate keeper**: LoRA-only eval 结果决定路线。A 失败无缝转 B。\\n\\n## 三路消融 (D012)\\n| 实验 | 隔离目标 | 状态 |\\n|------|---------|------|\\n| TG v7 | 完整方法 | DONE (training success, inference weak) |\\n| UG s42 | turn conditioning 增量 | DONE (success) ✅ |\\n| LoRA-only s42 | gating 机制增量 | RUNNING (~47.5%, ~3h remaining) |\\n\\n## 近期任务\\n- [ ] LoRA-only 训练完成（~3h）\\n- [ ] 四路 eval on standard_conversations（Base/TG/UG/LoRA-only + gate-profile）\\n- [ ] 基于 LoRA-only 结果决策：路线 A（two-stage）或路线 B（negative result paper）
…[truncated 1614 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T10:45:06.721220+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "decisions.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "turn_residual_gating",
    "file": "decisions.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T10:45:06.721506+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/decisions.yaml\", \"content\": \"_next_id: 18\\ndecisions:\\n- id: D001\\n  date: 2026-05-18 04:48 UTC\\n  summary: MVP Phase 2 中间场景处置：条件1通过+条件2失败 = partial pass\\n  rationale: 如果 ThreadGate GAR recovery 显著优于 Uniform Gate（验证 Cesaro 理论预测）但下游任务无改善，说明核心机制成立但\\n    GAR explanation ceiling 有限。处置：视为 partial pass 进入 research，但 framing 必须从\\\"提升多轮性能的方法\\\"转向\\\"理论验证+首个\\n    principled 干预框架\\\"，实用价值作为 secondary contribution。如果连条件1都不满足则仍为 kill。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-18 04:59 UTC\\n  summary: MVP 使用残差缩放公式 x + g·f(x) 代替 IDEA_BRIEF 插值公式\\n  rationale: IDEA_BRIEF 的插值公式 g·x + (1-g)·f(x) 无法通过任何 g 值恢复正常模型行为 x+f(x)，导致初始化困难。改用\\n    x + g·f(x)（g=1 为正常，g→0 为跳过层），保证模型可从正常状态开始学习。核心对比（turn-conditional vs uniform）不受公式影响——两种公式下\\n    uniform gating 都无法选择性修改特定位置的 GAR。理论对齐留到 research 阶段。\\n  related_experiments: []\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-18 06:05 UTC\\n  summary: Phase 2 增加归一化 GAR 作为诊断指标，pass 标准仍基于 raw GAR\\n  rationale: Reviewer 发现 Phase 1 的 70.8% raw GAR 衰减大部分由序列增长稀释驱动，归一化后结构性下降仅 ~21%。normalized\\n    GAR 能区分\\\"稀释补偿\\\"vs\\\"结构性修复\\\"，直接影响论文 Cesaro 理论 story 的可信度。但 raw GAR 衰减是功能上真实有害的，方法即使只补偿稀释也有实用价值，因此\\n    MVP pass 标准不变。\\n  related_experiments:\\n  - exp_id: phase1_gar_diag\\n    role: evidence\\n    result: GAR衰减70.8%但归一化后仅~21%\\n  depends_on: []\\n- id: D004\\n  date: 2026-05-18 13:37 UTC\\n  summary: Kill v3, run v3b (λ=10, gate_lr=10x, init_bias=0.0) as GAR-driven gating的最终验证。500步内gate无分化则GAR→gate梯度路径判定失败。\\n  rationale: v1/v2/v3 三个版本全部无法驱动gate学习选择性干预：v1 epsilon过高(L_GAR=0)，v2 hinge退化平衡点，v3\\n    maximize模式梯度太弱(gate冻结在0.876±0.001)。根因一致：GAR→attention→hidden→gate间接梯度路径太弱。v3b同时最大化三个信号强度维度(λ=10,\\n    gate_lr=10x, init_bias=0.0给sigmoid最大梯度区间)，如果仍然失败则排除\\\"信号不够强\\\"的解释，确认是梯度路径结构性问题。\\n  related_experiments:\\n  - exp_id: phase2_tg_s42_v1\\n    role: evidence\\n    result: L_G
…[truncated 9957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T10:45:06.721693+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "report.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "turn_residual_gating",
    "file": "report.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T10:45:06.721866+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/report.md\", \"content\": \"# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| phase2_lora_only_s42 | LoRA-only baseline (gate 固定 1.0，无 gating 机制) 在相同 MSE+NTP loss 下 GAR 应低于 ThreadGate (v7)。如果 LoRA-only 也能训到 GAR~0.5，则 gating 机制贡献为零，paper story 不成立。关键对比：LoRA-only 的 GAR 收敛值 vs v7 的 0.48。 | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **phase2_ug_s42** (success): Uniform gating baseline: per-layer independent gates without turn conditioning (content-dependent only), to isolate whether ThreadGate's turn-conditioned gating provides benefit over content-only residual scaling. Same training setup as v7 but with gate-type=uniform. ← 基于 phase1_gar_diag\\n- **phase2_tg_s42_v7** (success): MSE 双向 loss (mean_GAR - target)² + gate diversity 正则 F.relu(min_std - gate_std) 从结构上解决恒等退化：MSE 在 GAR > target 时反向惩罚（不再单调推高），gate_div 直接强制层间分化。预期：gate_std 稳定 >0.05 + GAR 收敛到 target=0.5 附近 + NTP 正常收敛。 ← 基于 phase2_tg_s42_v6\\n  [v7_mse_target_gate_diversity_code](/api/workspace-files/projects/turn_residual_gating/artifacts/phase2_tg_s42_v7/intermediate/v7_mse_target_gate_diversity_code.txt) | [v7_training_dynamics_csv](/api/workspace-files/projects/turn_residual_gating/artifacts/phase2_tg_s42_v7/data/v7_training_dynamics_pointer.txt)\\n- **phase2_tg_s42_v6** (negative): smooth_saturation loss (-target*tanh(GAR/target), target=0.5) 提供有界但持续的 GAR 梯度，避免 maximize 的恒等退化（gate→1）和 hinge_target 的梯度消失（GAR达标后梯度=0）。预期：gate_std>0.05 的层间分化 + GAR 稳态在 0.3-0.5 + NTP loss 正常收敛 + 总 loss 为正。 ← 基于 phase2_tg_s42_v5\\n\\n## 趋势\\n成功 4 / 负向 4 / 失败 1 / 共 10\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-20861: 无 GPU 信息\\n\\n## 告警\\n- phase2_tg_s42_v2: 已被终止 — unknown\\n- phase2_tg_s42_v4: 训练失败 — unknown\\n\", \"total_chars\": 1716, \"truncated\": false}, \"error\": nu
…[truncated 23 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T10:45:06.722065+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/ 2>/dev/null || echo \"directory empty or doesn't exist\"",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/ 2>/dev/null || echo \"directory empty or doesn't exist\"",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T10:45:06.722209+00:00_

_project
manifest.yaml
paper
phase2_tg_s42_v7
src

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T10:45:06.722335+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "turn_residual_gating",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "turn_residual_gating",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T10:45:06.722759+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/literature_map.yaml\", \"content\": \"categories:\\n  layer_importance:\\n    description: \\\"Layer-wise importance analysis, redundancy, and pruning in transformers\\\"\\n    papers:\\n      - title: \\\"The Unreasonable Ineffectiveness of the Deeper Layers\\\"\\n        authors: \\\"Gromov et al.\\\"\\n        venue: \\\"ICLR 2025\\\"\\n        year: 2024\\n        url: \\\"https://arxiv.org/abs/2403.17887\\\"\\n        role: foundation\\n        relevance: \\\"发现 LLM 深层高度冗余，可删除近半层而性能不降；浅层对知识存储至关重要\\\"\\n        abstract: \\\"Studies knowledge storage via layer pruning. Finds minimal performance degradation until up to half of layers are removed.\\\"\\n\\n      - title: \\\"ShortGPT: Layers in Large Language Models are More Redundant Than You Expect\\\"\\n        authors: \\\"Men et al.\\\"\\n        venue: \\\"arXiv 2024\\\"\\n        year: 2024\\n        url: \\\"https://arxiv.org/abs/2403.03853\\\"\\n        role: foundation\\n        relevance: \\\"提出 Block Influence (BI) 度量各层重要性，发现许多层高度相似且功能冗余\\\"\\n        abstract: \\\"Defines Block Influence (BI) metric to gauge layer significance. Discovers many LLM layers exhibit high similarity.\\\"\\n\\n      - title: \\\"The Curse of Depth in Large Language Models\\\"\\n        authors: \\\"Sun et al.\\\"\\n        venue: \\\"NeurIPS 2025\\\"\\n        year: 2025\\n        url: \\\"https://arxiv.org/abs/2502.05795\\\"\\n        role: foundation\\n        relevance: \\\"Pre-LN 导致深层梯度趋近恒等映射。解释 ThreadGate 中 late layers gate 接近 1.0\\\"\\n        abstract: \\\"Pre-Layer Normalization causes output variance to grow exponentially with depth.\\\"\\n\\n      - title: \\\"Reassessing Layer Pruning in LLMs: New Insights and Methods\\\"\\n        authors: \\\"Anonymous\\\"\\n        venue: \\\"arXiv 2024\\\"\\n        year: 2024\\n        url: \\\"https://arxiv.org/abs/2411.15558\\\"\\n        role
…[truncated 18040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T10:45:06.723018+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/route_b_design.md",
  "content": "# Route B: Negative Result / Analysis Paper 实验设计\n\n> 前提条件: LoRA-only eval 确认 gating 贡献为零（LoRA-only ≈ TG），或路线 A two-stage 失败后无缝转入\n> 基于: paper_framing.md NF1-NF4, decisions D014-D017, memory.md v7 eval 发现\n> 最后更新: 2026-05-19\n\n---\n\n## 1. 论文定位选项\n\n### Option A: \"Why Residual Gating Fails to Recover Goal Attention in Multi-Turn Dialogue\"\n\n- **定位**: 对 Dongre et al. (2605.12922) 诊断的首个系统性架构干预尝试 + 完整失败机制分析\n- **核心贡献**: not \"what works\" but \"why the most principled approach doesn't work and what this tells us about the problem's hardness\"\n- **叙事线**: Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98) → 自然推论: 在 residual connection 上施加 gate 即可恢复 attention → ThreadGate 是这一推论的最直接实现 → 它的失败揭示了 NTP-GAR 梯度冲突和 attention pattern 泛化性这两个更深层的障碍\n- **强点**: ThreadGate 的设计动机直接来自 Dongre 的 residual probe evidence，不是 ad hoc 尝试；失败机制（NF1-NF3）有完整量化；对所有基于 attention steering 的方法有警示意义\n- **弱点**: 只有一种干预方法族（residual gating），审稿人可能质疑\"你只试了一种方法\"\n- **缓解**: UG/LoRA-only 消融 + Dongre 自己的 goal re-injection 也失败 = 两种独立干预路线均失败\n- **竞争力**: Findings ~70%，加跨模型验证有冲 main 的可能\n\n### Option B: \"The Training-Inference Generalization Gap in Attention Steering\"\n\n- **定位**: 发现并量化 GAR 作为训练信号的泛化性根本问题\n- **核心贡献**: 30x training-inference GAR gap + 机制分析（NTP-GAR 梯度冲突导致 attention pattern 过拟合）\n- **叙事线**: GAR 在训练中可被有效优化（0.02→0.48）→ 但训练学到的 attention pattern 不泛化到新对话（推理 GAR=0.016）→ 根因是 NTP loss 主导使 gate 学到反向 turn conditioning → 这意味着所有基于辅助 attention loss 的方法都面临相同泛化障碍\n- **强点**: 泛化性问题对所有 attention steering 方法都有意义（不只是 residual gating）；30x gap 是一个 striking 数字\n- **弱点**: 需要更多方法（不只 ThreadGate/UG）验证泛化性问题的普遍性；claim 的 scope 大于证据\n- **缓解**: Dongre 的 goal re-injection 失败可作为间接 evidence；Base model 在 ultrachat 上 GAR≈eval GAR 排除数据分布解释\n- **竞争力**: 如果泛化性 claim 立得住 → main track 潜力更高；但需要更强的实验支撑\n\n### Option C: \"A Comprehensive Analysis of Goal Attention Recovery Mechanisms\"\n\n- **定位**: 系统性比较多种 GAR 恢复策略的 survey/analysis paper\n- **额外工作量**: 需实现 2-3 种额外干预方法（positional bias calibration, attention re-weighting, periodic goal re-injection with proper training），每种 ~10-15h GPU，时间预算不允许\n- **竞争力**: 如果做全了很强，但 EMNLP deadline 前完不成\n- **结论**: 不推荐，除非路线 A/B 审稿人要求 major revision 时再扩展\n\n### 推荐: Option A 为主，Option B 作为 framing 的一部分\n\nOption A 的 scope 更聚焦、证据更充分、写作负担更小。Option B 的泛化性洞察作为 Discussion section 的核心论点融入，而非作为独立 paper 的中心 claim（避免 overclaim）。\n\n---\n\n## 2. 核心消融实验（四路 eval）\n\n### 实验设计\n\n四个条件在同一组 standard_conversations.json（base model 生成，5 组 × 10 轮）上评估，消除文本 confound（NF4 修正）。\n\n| 条件 | 隔离目标 | GAR-ours | GAR-Dongre | nGAR | Gate profile | 状态 |\n|------|----------|----------|-----------|------|-------------|------|\n| Base (无训练) | 自然衰减 baseline | ~0.01 (ultrachat 已验证) | 待跑 | 待跑 | N/A | ✅ ultrachat 已跑，standard_conv 待统一 eval |\n| TG v7 | 完整 ThreadGate | 0.016 (旧 eval) | 待重跑 | 待重跑 | 已有（D014 数据） | 待 standard_conv 统一 eval |\n| UG | turn conditioning 增量 | 待跑 | 待跑 | 待跑 | 待跑 | ✅ 训练完成，eval 待做 |\n| LoRA-only | gating 机制增量 | 待跑 | 待跑 | 待跑 | N/A (gate≡1.0) | 训练中 ~47.5% |\n\n### 关键对比\n\n1. **TG vs LoRA-only**: gating 机制是否有非零贡献（D012 核心问题）\n2. **TG vs UG**: turn conditioning 是否有增量（如果两者 ≈，则 turn conditioning 无效）\n3. **LoRA-only vs Base**: LoRA 微调本身是否改善/恶化 GAR\n4. **所有条件 vs Base**: 任何训练干预是否改善推理时 GAR\n\n### 预期结果（negative result 假设下）\n\n- TG ≈ UG ≈ LoRA-only >> Base（LoRA 微调略改善 GAR，但 gating 无增量贡献）\n- 或 TG ≈ UG ≈ LoRA-only ≈ Base（所有干预在推理时均无效）\n- 任一结果都支撑 \"residual gating 对推理时 GAR 无显著影响\" 的 negative conclusion\n\n---\n\n## 3. 机制分析实验\n\n### 3.1 NTP-GAR 梯度冲突量化\n\n- **目的**: 量化 NTP loss 和 GAR loss 在 gate 参数上的梯度方向和幅度，为 NF1（反向 turn conditioning）提供机制解释\n- **方法**: 在 v7 最终 checkpoint 上，取 10 个 ultrachat 样本做 single-step forward：\n  1. 分别计算 ∇_gate(L_NTP) 和 ∇_gate(L_GAR)（28 层 × 每层 gate bias 参数）\n  2. 逐层计算 cosine similarity: cos(∇_NTP, ∇_GAR)\n  3. 计算梯度幅度比: ||∇_NTP|| / ||∇_GAR||\n- **预期**: \n  - cosine < 0（两个梯度方向冲突），尤其在 GAR 已收敛的 late training 阶段\n  - ||∇_NTP|| >> ||∇_GAR||（NTP 梯度幅度远大于 GAR），解释为什么 NTP 主导了 gate 学习方向\n  - 不同 turn position 的冲突程度不同：早期 turn（短序列）冲突小，晚期 turn（长序列）NTP 梯度放大，冲突加剧\n- **与 NF1 关系**: 如果晚期 turn 的 NTP 梯度推 gate→1.0 最强烈，直接解释为什么 gates 在晚期 turn 变为 passive（NF1 核心发现）\n- **GPU 时间**: ~10min（10 次 forward+backward，无需训练）\n- **代码**: 修改 train_threadgate.py，关闭 optimizer step，分别 backward 两个 loss 记录梯度\n\n### 3.2 Gate Profile 深入分析\n\n已有数据的深度挖掘，无需新实验，纯分析工作。\n\n#### 3.2.1 Turn-by-turn gate 值变化（已有 D014 数据）\n- 完整 28 层 × 10 turn 的 gate heatmap\n- 标注 NF1 发现：27/28 层 diff (turn1 - turn21) < 0\n- 识别异常层（唯一 diff > 0 的层是哪一层？是否与 Dongre goal-encoding 层有关？）\n\n#### 3.2.2 Layer-wise gate 与 Dongre goal-encoding layers 对比\n- Dongre 报告 Qwen-2.5-7B goal encoding 从 L5 开始（probe AUC 陡升）\n- 训练时 L3/L4 为最低 gate（与 L4/L5 onset 位置 coincides，C4 suggestive）\n- 推理时 L14/L23 动态范围最大（与训练不一致）\n- 分析：为什么训练-推理的 critical layer 不同？是否与 NTP 梯度在不同层的相对强度有关？\n\n#### 3.2.3 UG vs TG gate profile 对比\n- 如果 UG 也产生相似的 per-layer 分化模式（L3/L4 最低）→ 分化是 GAR loss 驱动的，与 turn conditioning 无关\n- 如果 UG 分化模式不同 → turn conditioning 确实影响了哪些层被抑制（即使方向错误）\n- 已有线索（ROADMAP.md）：UG 训练也产生与 TG 相同的 per-layer 分化模式\n\n### 3.3 Attention Pattern 可视化\n\n- **目的**: 直观展示训练前后 attention 在 goal tokens 上的实际分布，让读者\"看到\"问题\n- **方法**: \n  1. 取 3 个 standard_conversations 样本\n  2. 对 Base / TG / UG / LoRA-only 四个条件提取 attention weights（全层全头）\n  3. 对每个条件：绘制 goal tokens 上的平均 attention heatmap（x 轴 = 层，y 轴 = turn）\n  4. 对比 TG 训练时（ultrachat 数据）vs 推理时（standard_conv 数据）的 attention pattern → 可视化 30x 过拟合\n- **预期**: \n  - Base: 明确的 turn-wise attention 衰减\n  - TG/UG/LoRA-only: 与 Base 差异极小（GAR 改善不泛化）\n  - TG 训练时: goal tokens attention 显著增强（GAR=0.48 的视觉对应）\n- **GPU 时间**: ~20min（四个模型各 forward 一次，提取 attention weights）\n- **图表**: 1 个 4×1 subfigure（四个条件的 attention heatmap）+ 1 个训练 vs 推理对比图\n\n### 3.4 GAR 泛化性分析\n\n- **已有**: 训练 GAR=0.48 vs 推理 GAR=0.016（NF2，30x 断层，confirmed non-bug by D015）\n- **已有**: Base model GAR on ultrachat ≈ GAR on eval data（~0.01），排除数据分布假设\n- **新增 per-layer GAR breakdown**:\n  - 目的：哪些层的 GAR 过拟合最严重？是否与 gate 分化最大的层相关？\n  - 方法：分别在训练数据和 eval 数据上计算逐层 GAR，绘制 per-layer GAR ratio (train/eval)\n  - 预期：所有层都过拟合，但 L3/L4（gate 分化最大层）可能过拟合更严重或更轻微 — 任一结果都有分析价值\n- **新增 training trajectory GAR 泛化曲线**:\n  - 目的：GAR 过拟合是渐进的还是突发的？与三阶段训练动力学（plateau → phase transition → convergence）的哪个阶段对应？\n  - 方法：在训练过程的 5 个 checkpoint（gs50, gs100, gs150, gs200, gs400）上分别计算 eval GAR\n  - 预期：训练 GAR 在 gs75-144 急升（phase transition），eval GAR 是否同步上升？如果不同步 → 过拟合在 phase transition 阶段即开始\n- **GPU 时间**: ~30min（5 个 checkpoint × 1 次 eval forward）\n\n### 3.5 训练动力学三阶段分析（已有数据，需可视化）\n\nv7 训练呈现清晰的三阶段动力学（memory.md 记录），这是 paper 的亮点之一：\n\n1. **Plateau (gs0-75)**: GAR ≈ 0.02，gate 在初始状态附近微调\n2. **Phase transition (gs75-144)**: GAR 从 0.02 急升至 0.48，gate profile 快速分化\n3. **Convergence (gs144+)**: GAR 稳定在 target=0.5 附近，gate_std plateau 在 0.05+\n\n- **可视化**: 训练 GAR + gate_mean + gate_std + L_NTP + L_GAR 的五合一 training dynamics 图\n- **叙事价值**: 说明 MSE 双向 loss 确实能驱动 gate 学到有意义的结构，问题不在训练而在泛化\n- **数据来源**: v7_training_dynamics_csv（已有 artifact）\n\n---\n\n## 4. 跨模型验证（Llama-3.1-8B-Instruct）\n\n跨模型验证是 Route B 从 Findings 冲 main track 的关键加分项（D017）。\n\n### 4.1 Phase 1 复现：GAR 衰减诊断\n\n- **目的**: 在第二个模型上确认 GAR 衰减现象（Dongre 已在 12 个模型上验证，但我们需要自己的数据来做完整对比）\n- **方法**: 用 Phase 1 GAR 诊断脚本在 Llama-3.1-8B-Instruct 上跑\n- **预期**: 同样观察到 GAR 衰减（Dongre 在 Llama-3.1-8B 上报告 27-48% 衰减范围）\n- **代码适配**: turn_utils.py 已支持 Llama chat template（D015 后完成）\n- **模型路径**: /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/（ModelScope 通道，已有 tokenizer，权重 ~16GB 需下载）\n- **GPU 时间**: ~30min\n- **磁盘**: 需先清理 Qwen cache 腾出空间（当前 15G/30G 可用，Llama 权重 ~16GB）\n\n### 4.2 ThreadGate v7 训练\n\n- **目的**: 在 Llama 上复现 ThreadGate 的 negative finding\n- **方法**: 用与 Qwen v7 相同的设置（MSE+gate_div, λ_gar=1.0, λ_div=1.0, 3 epoch）\n- **预期**: \n  - 训练 GAR 同样可被优化到 ~0.5（MSE loss 有效性是模型无关的）\n  - 推理 GAR 同样过拟合（如果确认 → NF2 普遍性加强）\n  - Turn conditioning 同样反向（如果确认 → NF1 是 NTP-GAR 竞争的结构性后果，不是 Qwen 特有的）\n- **代码适配**: threadgate.py 自动读取 hidden_dim (4096 for Llama vs 3584 for Qwen) / num_layers (32 for Llama vs 28 for Qwen)\n- **GPU 时间**: ~6h（Llama-3.1-8B 比 Qwen-2.5-7B 稍大）\n\n### 4.3 消融（可选，视时间预算）\n\n- 如果时间允许：在 Llama 上也跑 UG + LoRA-only 消融\n- 如果时间不允许：只做 TG + Base 对比，消融数据仅在 Qwen 上报告\n- GPU 时间（如做）: UG ~6h + LoRA-only ~6h\n\n### 4.4 跨模型 gate profile 对比\n\n- 如果 Llama 上也出现类似的 per-layer 分化模式（某些浅层 gate 最低）→ 更强的普遍性 evidence\n- 如果 Llama 的 critical layer 不同（如 L2 最低，对应 Dongre 报告 Llama goal-encoding onset 在 L2）→ 说明 gate 确实学到了模型特异的 goal-encoding 结构，但仍然无法泛化到推理\n- 两种结果都有分析价值\n\n---\n\n## 5. 与 Dongre et al. (2605.12922) 的关系\n\n### 互补定位\n\n| 维度 | Dongre et al. | 本文 |\n|------|---------------|------|\n| 核心问题 | \"发生了什么\" + \"为什么\" | \"怎么干预\" + \"为什么干预失败\" |\n| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认（Qwen 70.8% raw, 21% normalized），我们的测量定义更宽（含 first user query） |\n| 机制分析 | residual probe AUC=0.98（goal info 持续存在） | NTP-GAR 梯度冲突 + 30x 泛化 gap + turn conditioning 反转 |\n| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |\n| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |\n\n### 共同推论\n\n两种独立干预路线（prompt-level goal re-injection + architecture-level residual gating）均失败，共同指向：\n\n1. 简单的 attention steering 不足以对抗 NTP 的优化压力\n2. 需要更深层的架构改变（如 decoupled goal-processing pathway，或 inference-time attention intervention 绕过训练泛化问题）\n\n### 我们的独特增量\n\nDongre 诊断了问题，但没有解释为什么干预难以成功。我们量化了三个具体障碍：\n1. **NTP-GAR 梯度冲突**（NF1 + 3.1 实验）: NTP loss 在 gate 参数上的梯度方向与 GAR loss 相反\n2. **Attention pattern 不泛化**（NF2 + 3.4 实验）: 训练中学到的 attention redistribution 不迁移到新对话\n3. **Gate 干预强度不足**（NF3）: 推理时 gate 仅 2-7% attenuation，远不足以改变 attention pattern\n\n---\n\n## 6. 论文结构草案（Option A framing）\n\n1. **Abstract** (150-250 words): 问题（GAR 衰减）→ 动机（Dongre residual probe → residual gating 是自然方案）→ 方法（ThreadGate）→ 核心发现（三个失败机制）→ 意义\n2. **Introduction** (5 段): 多轮对话退化 → Dongre 诊断 + residual stream 持续性 → ThreadGate 设计动机 → 三个 negative findings 概述 → 贡献列表\n3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering\n4. **Background**: GAR 定义（cite Dongre）+ residual stream persistence 证据\n5. **Method**: ThreadGate 架构 + MSE+gate_div loss + 训练设置\n6. **Experiments**: 四路消融 + 跨模型验证 + 训练动力学\n7. **Analysis**: NTP-GAR 梯度冲突 + GAR 泛化性分析 + gate profile 深入分析 + attention 可视化\n8. **Discussion**: 为什么 residual gating 不够 + 对 attention steering 方法的启示 + 潜在解决方向\n9. **Conclusion**: negative result 总结 + 对社区的建议\n\n### 贡献列表（草案）\n\n1. 首个基于 residual stream persistence 证据设计的架构级 GAR 恢复干预（ThreadGate），及其完整失败分析\n2. 发现并量化 NTP-GAR 梯度冲突导致 turn conditioning 反向学习的机制\n3. 量化 GAR 训练信号的泛化性问题（30x training-inference gap），对所有基于辅助 attention loss 的方法有警示意义\n4. 四路消融 + 跨模型验证的完整实验设计，为后续研究提供 baseline 和诊断工具\n\n---\n\n## 7. 实验时间表\n\n| 实验 | GPU 时间 | 依赖 | 预计完成 |\n|------|----------|------|----------|\n| LoRA-only 训练完成 | ~3h (剩余) | 无 | D+0 (2026-05-19) |\n| 四路 eval on standard_conv (Qwen) | ~1h | LoRA-only 完成 | D+0 |\n| 梯度冲突分析 (3.1) | ~10min | v7 checkpoint | D+0 |\n| Attention 可视化 (3.3) | ~20min | 四路 checkpoint | D+0 |\n| GAR 泛化曲线 — 5 checkpoints (3.4) | ~30min | v7 中间 checkpoints | D+1 |\n| 训练动力学可视化 (3.5) | ~0 (纯绘图) | v7_training_dynamics_csv | D+0 |\n| Gate profile 深入分析 (3.2) | ~0 (纯分析) | 四路 eval 数据 | D+1 |\n| Llama 模型下载 | ~30min (网络) | 磁盘清理 | D+1 |\n| Phase 1 GAR 诊断 (Llama) | ~30min | Llama 模型下载 | D+1 |\n| TG v7 训练 (Llama) | ~6h | Llama 模型下载 | D+2 |\n| Llama eval + gate profile | ~1h | Llama TG 完成 | D+2 |\n| [可选] Llama UG + LoRA-only | ~12h | Llama TG eval | D+3-4 |\n\n**总 GPU 时间**: ~12h（核心）+ ~12h（可选 Llama 消融）\n**写作启动**: D+2（Qwen 全部数据就绪后可开始 Method/Background/Related Work）\n**完整初稿**: D+7-10（假设跨模型验证顺利）\n\n---\n\n## 8. 风险与应急\n\n| 风险 | 概率 | 影响 | 应急 |\n|------|------|------|------|\n| LoRA-only 意外优于 TG（gating 有负面贡献） | 低 | 叙事调整：gating 不仅无效还有害（更强的 negative finding） | 额外分析 why gating hurts |\n| Llama 上 GAR 衰减模式与 Qwen 显著不同 | 中 | 跨模型 claim 弱化 | 聚焦 Qwen 深度分析，Llama 作为补充 |\n| Llama 上 ThreadGate 意外成功 | 极低 | 整个 negative framing 需要重写 | 转回 Route A，Qwen 失败 + Llama 成功本身是更有趣的故事 |\n| 磁盘空间不足以同时存 Qwen + Llama checkpoints | 中 | Llama 实验延迟 | 先完成 Qwen 所有分析，删除中间 checkpoints，再下载 Llama |\n| 审稿人认为\"只测了 residual gating 一种方法，negative result 太窄\" | 高 | reject 风险 | Discussion 中系统性分析为什么其他方法（attention re-weighting, positional bias）也面临类似障碍；cite Dongre goal re-injection 失败 |\n| 梯度冲突分析结果不显著（cosine ≈ 0 而非 < 0） | 中 | NF1 的机制解释弱化 | 转为 \"orthogonal gradients = GAR loss 无法有效引导 gate\" 的叙事（NTP 不一定反对，但 GAR 信号太弱被淹没） |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/route_b_design.md",
    "content": "# Route B: Negative Result / Analysis Paper 实验设计\n\n> 前提条件: LoRA-only eval 确认 gating 贡献为零（LoRA-only ≈ TG），或路线 A two-stage 失败后无缝转入\n> 基于: paper_framing.md NF1-NF4, decisions D014-D017, memory.md v7 eval 发现\n> 最后更新: 2026-05-19\n\n---\n\n## 1. 论文定位选项\n\n### Option A: \"Why Residual Gating Fails to Recover Goal Attention in Multi-Turn Dialogue\"\n\n- **定位**: 对 Dongre et al. (2605.12922) 诊断的首个系统性架构干预尝试 + 完整失败机制分析\n- **核心贡献**: not \"what works\" but \"why the most principled approach doesn't work and what this tells us about the problem's hardness\"\n- **叙事线**: Dongre 发现 goal info 在 residual stream 持续存在 (probe AUC=0.98) → 自然推论: 在 residual connection 上施加 gate 即可恢复 attention → ThreadGate 是这一推论的最直接实现 → 它的失败揭示了 NTP-GAR 梯度冲突和 attention pattern 泛化性这两个更深层的障碍\n- **强点**: ThreadGate 的设计动机直接来自 Dongre 的 residual probe evidence，不是 ad hoc 尝试；失败机制（NF1-NF3）有完整量化；对所有基于 attention steering 的方法有警示意义\n- **弱点**: 只有一种干预方法族（residual gating），审稿人可能质疑\"你只试了一种方法\"\n- **缓解**: UG/LoRA-only 消融 + Dongre 自己的 goal re-injection 也失败 = 两种独立干预路线均失败\n- **竞争力**: Findings ~70%，加跨模型验证有冲 main 的可能\n\n### Option B: \"The Training-Inference Generalization Gap in Attention Steering\"\n\n- **定位**: 发现并量化 GAR 作为训练信号的泛化性根本问题\n- **核心贡献**: 30x training-inference GAR gap + 机制分析（NTP-GAR 梯度冲突导致 attention pattern 过拟合）\n- **叙事线**: GAR 在训练中可被有效优化（0.02→0.48）→ 但训练学到的 attention pattern 不泛化到新对话（推理 GAR=0.016）→ 根因是 NTP loss 主导使 gate 学到反向 turn conditioning → 这意味着所有基于辅助 attention loss 的方法都面临相同泛化障碍\n- **强点**: 泛化性问题对所有 attention steering 方法都有意义（不只是 residual gating）；30x gap 是一个 striking 数字\n- **弱点**: 需要更多方法（不只 ThreadGate/UG）验证泛化性问题的普遍性；claim 的 scope 大于证据\n- **缓解**: Dongre 的 goal re-injection 失败可作为间接 evidence；Base model 在 ultrachat 上 GAR≈eval GAR 排除数据分布解释\n- **竞争力**: 如果泛化性 claim 立得住 → main track 潜力更高；但需要更强的实验支撑\n\n### Option C: \"A Comprehensive Analysis of Goal Attention Recovery Mechanisms\"\n\n- **定位**: 系统性比较多种 GAR 恢复策略的 survey/analysis paper\n- **额外工作量**: 需实现 2-3 种额外干预方法（positional bias calibration, attention re-weighting, periodic goal re-injection with proper training），每种 ~10-15h GPU，时间预算不允许\n- **竞争力**: 如果做全了很强，但 EMNLP deadline 前完不成\n- **结论**: 不推荐，除非路线 A/B 审稿人要求 major revision 时再扩展\n\n### 推荐: Option A 为主，Option B 作为 framing 的一部分\n\nOption A 的 scope 更聚焦、证据更充分、写作负担更小。Option B 的泛化性洞察作为 Discussion section 的核心论点融入，而非作为独立 paper 的中心 claim（避免 overclaim）。\n\n---\n\n## 2. 核心消融实验（四路 eval）\n\n### 实验设计\n\n四个条件在同一组 standard_conversations.json（base model 生成，5 组 × 10 轮）上评估，消除文本 confound（NF4 修正）。\n\n| 条件 | 隔离目标 | GAR-ours | GAR-Dongre | nGAR | Gate profile | 状态 |\n|------|----------|----------|-----------|------|-------------|------|\n| Base (无训练) | 自然衰减 baseline | ~0.01 (ultrachat 已验证) | 待跑 | 待跑 | N/A | ✅ ultrachat 已跑，standard_conv 待统一 eval |\n| TG v7 | 完整 ThreadGate | 0.016 (旧 eval) | 待重跑 | 待重跑 | 已有（D014 数据） | 待 standard_conv 统一 eval |\n| UG | turn conditioning 增量 | 待跑 | 待跑 | 待跑 | 待跑 | ✅ 训练完成，eval 待做 |\n| LoRA-only | gating 机制增量 | 待跑 | 待跑 | 待跑 | N/A (gate≡1.0) | 训练中 ~47.5% |\n\n### 关键对比\n\n1. **TG vs LoRA-only**: gating 机制是否有非零贡献（D012 核心问题）\n2. **TG vs UG**: turn conditioning 是否有增量（如果两者 ≈，则 turn conditioning 无效）\n3. **LoRA-only vs Base**: LoRA 微调本身是否改善/恶化 GAR\n4. **所有条件 vs Base**: 任何训练干预是否改善推理时 GAR\n\n### 预期结果（negative result 假设下）\n\n- TG ≈ UG ≈ LoRA-only >> Base（LoRA 微调略改善 GAR，但 gating 无增量贡献）\n- 或 TG ≈ UG ≈ LoRA-only ≈ Base（所有干预在推理时均无效）\n- 任一结果都支撑 \"residual gating 对推理时 GAR 无显著影响\" 的 negative conclusion\n\n---\n\n## 3. 机制分析实验\n\n### 3.1 NTP-GAR 梯度冲突量化\n\n- **目的**: 量化 NTP loss 和 GAR loss 在 gate 参数上的梯度方向和幅度，为 NF1（反向 turn conditioning）提供机制解释\n- **方法**: 在 v7 最终 checkpoint 上，取 10 个 ultrachat 样本做 single-step forward：\n  1. 分别计算 ∇_gate(L_NTP) 和 ∇_gate(L_GAR)（28 层 × 每层 gate bias 参数）\n  2. 逐层计算 cosine similarity: cos(∇_NTP, ∇_GAR)\n  3. 计算梯度幅度比: ||∇_NTP|| / ||∇_GAR||\n- **预期**: \n  - cosine < 0（两个梯度方向冲突），尤其在 GAR 已收敛的 late training 阶段\n  - ||∇_NTP|| >> ||∇_GAR||（NTP 梯度幅度远大于 GAR），解释为什么 NTP 主导了 gate 学习方向\n  - 不同 turn position 的冲突程度不同：早期 turn（短序列）冲突小，晚期 turn（长序列）NTP 梯度放大，冲突加剧\n- **与 NF1 关系**: 如果晚期 turn 的 NTP 梯度推 gate→1.0 最强烈，直接解释为什么 gates 在晚期 turn 变为 passive（NF1 核心发现）\n- **GPU 时间**: ~10min（10 次 forward+backward，无需训练）\n- **代码**: 修改 train_threadgate.py，关闭 optimizer step，分别 backward 两个 loss 记录梯度\n\n### 3.2 Gate Profile 深入分析\n\n已有数据的深度挖掘，无需新实验，纯分析工作。\n\n#### 3.2.1 Turn-by-turn gate 值变化（已有 D014 数据）\n- 完整 28 层 × 10 turn 的 gate heatmap\n- 标注 NF1 发现：27/28 层 diff (turn1 - turn21) < 0\n- 识别异常层（唯一 diff > 0 的层是哪一层？是否与 Dongre goal-encoding 层有关？）\n\n#### 3.2.2 Layer-wise gate 与 Dongre goal-encoding layers 对比\n- Dongre 报告 Qwen-2.5-7B goal encoding 从 L5 开始（probe AUC 陡升）\n- 训练时 L3/L4 为最低 gate（与 L4/L5 onset 位置 coincides，C4 suggestive）\n- 推理时 L14/L23 动态范围最大（与训练不一致）\n- 分析：为什么训练-推理的 critical layer 不同？是否与 NTP 梯度在不同层的相对强度有关？\n\n#### 3.2.3 UG vs TG gate profile 对比\n- 如果 UG 也产生相似的 per-layer 分化模式（L3/L4 最低）→ 分化是 GAR loss 驱动的，与 turn conditioning 无关\n- 如果 UG 分化模式不同 → turn conditioning 确实影响了哪些层被抑制（即使方向错误）\n- 已有线索（ROADMAP.md）：UG 训练也产生与 TG 相同的 per-layer 分化模式\n\n### 3.3 Attention Pattern 可视化\n\n- **目的**: 直观展示训练前后 attention 在 goal tokens 上的实际分布，让读者\"看到\"问题\n- **方法**: \n  1. 取 3 个 standard_conversations 样本\n  2. 对 Base / TG / UG / LoRA-only 四个条件提取 attention weights（全层全头）\n  3. 对每个条件：绘制 goal tokens 上的平均 attention heatmap（x 轴 = 层，y 轴 = turn）\n  4. 对比 TG 训练时（ultrachat 数据）vs 推理时（standard_conv 数据）的 attention pattern → 可视化 30x 过拟合\n- **预期**: \n  - Base: 明确的 turn-wise attention 衰减\n  - TG/UG/LoRA-only: 与 Base 差异极小（GAR 改善不泛化）\n  - TG 训练时: goal tokens attention 显著增强（GAR=0.48 的视觉对应）\n- **GPU 时间**: ~20min（四个模型各 forward 一次，提取 attention weights）\n- **图表**: 1 个 4×1 subfigure（四个条件的 attention heatmap）+ 1 个训练 vs 推理对比图\n\n### 3.4 GAR 泛化性分析\n\n- **已有**: 训练 GAR=0.48 vs 推理 GAR=0.016（NF2，30x 断层，confirmed non-bug by D015）\n- **已有**: Base model GAR on ultrachat ≈ GAR on eval data（~0.01），排除数据分布假设\n- **新增 per-layer GAR breakdown**:\n  - 目的：哪些层的 GAR 过拟合最严重？是否与 gate 分化最大的层相关？\n  - 方法：分别在训练数据和 eval 数据上计算逐层 GAR，绘制 per-layer GAR ratio (train/eval)\n  - 预期：所有层都过拟合，但 L3/L4（gate 分化最大层）可能过拟合更严重或更轻微 — 任一结果都有分析价值\n- **新增 training trajectory GAR 泛化曲线**:\n  - 目的：GAR 过拟合是渐进的还是突发的？与三阶段训练动力学（plateau → phase transition → convergence）的哪个阶段对应？\n  - 方法：在训练过程的 5 个 checkpoint（gs50, gs100, gs150, gs200, gs400）上分别计算 eval GAR\n  - 预期：训练 GAR 在 gs75-144 急升（phase transition），eval GAR 是否同步上升？如果不同步 → 过拟合在 phase transition 阶段即开始\n- **GPU 时间**: ~30min（5 个 checkpoint × 1 次 eval forward）\n\n### 3.5 训练动力学三阶段分析（已有数据，需可视化）\n\nv7 训练呈现清晰的三阶段动力学（memory.md 记录），这是 paper 的亮点之一：\n\n1. **Plateau (gs0-75)**: GAR ≈ 0.02，gate 在初始状态附近微调\n2. **Phase transition (gs75-144)**: GAR 从 0.02 急升至 0.48，gate profile 快速分化\n3. **Convergence (gs144+)**: GAR 稳定在 target=0.5 附近，gate_std plateau 在 0.05+\n\n- **可视化**: 训练 GAR + gate_mean + gate_std + L_NTP + L_GAR 的五合一 training dynamics 图\n- **叙事价值**: 说明 MSE 双向 loss 确实能驱动 gate 学到有意义的结构，问题不在训练而在泛化\n- **数据来源**: v7_training_dynamics_csv（已有 artifact）\n\n---\n\n## 4. 跨模型验证（Llama-3.1-8B-Instruct）\n\n跨模型验证是 Route B 从 Findings 冲 main track 的关键加分项（D017）。\n\n### 4.1 Phase 1 复现：GAR 衰减诊断\n\n- **目的**: 在第二个模型上确认 GAR 衰减现象（Dongre 已在 12 个模型上验证，但我们需要自己的数据来做完整对比）\n- **方法**: 用 Phase 1 GAR 诊断脚本在 Llama-3.1-8B-Instruct 上跑\n- **预期**: 同样观察到 GAR 衰减（Dongre 在 Llama-3.1-8B 上报告 27-48% 衰减范围）\n- **代码适配**: turn_utils.py 已支持 Llama chat template（D015 后完成）\n- **模型路径**: /root/.cache/modelscope/hub/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/（ModelScope 通道，已有 tokenizer，权重 ~16GB 需下载）\n- **GPU 时间**: ~30min\n- **磁盘**: 需先清理 Qwen cache 腾出空间（当前 15G/30G 可用，Llama 权重 ~16GB）\n\n### 4.2 ThreadGate v7 训练\n\n- **目的**: 在 Llama 上复现 ThreadGate 的 negative finding\n- **方法**: 用与 Qwen v7 相同的设置（MSE+gate_div, λ_gar=1.0, λ_div=1.0, 3 epoch）\n- **预期**: \n  - 训练 GAR 同样可被优化到 ~0.5（MSE loss 有效性是模型无关的）\n  - 推理 GAR 同样过拟合（如果确认 → NF2 普遍性加强）\n  - Turn conditioning 同样反向（如果确认 → NF1 是 NTP-GAR 竞争的结构性后果，不是 Qwen 特有的）\n- **代码适配**: threadgate.py 自动读取 hidden_dim (4096 for Llama vs 3584 for Qwen) / num_layers (32 for Llama vs 28 for Qwen)\n- **GPU 时间**: ~6h（Llama-3.1-8B 比 Qwen-2.5-7B 稍大）\n\n### 4.3 消融（可选，视时间预算）\n\n- 如果时间允许：在 Llama 上也跑 UG + LoRA-only 消融\n- 如果时间不允许：只做 TG + Base 对比，消融数据仅在 Qwen 上报告\n- GPU 时间（如做）: UG ~6h + LoRA-only ~6h\n\n### 4.4 跨模型 gate profile 对比\n\n- 如果 Llama 上也出现类似的 per-layer 分化模式（某些浅层 gate 最低）→ 更强的普遍性 evidence\n- 如果 Llama 的 critical layer 不同（如 L2 最低，对应 Dongre 报告 Llama goal-encoding onset 在 L2）→ 说明 gate 确实学到了模型特异的 goal-encoding 结构，但仍然无法泛化到推理\n- 两种结果都有分析价值\n\n---\n\n## 5. 与 Dongre et al. (2605.12922) 的关系\n\n### 互补定位\n\n| 维度 | Dongre et al. | 本文 |\n|------|---------------|------|\n| 核心问题 | \"发生了什么\" + \"为什么\" | \"怎么干预\" + \"为什么干预失败\" |\n| GAR 衰减 | 定义 GAR，12 模型量化衰减 | 独立确认（Qwen 70.8% raw, 21% normalized），我们的测量定义更宽（含 first user query） |\n| 机制分析 | residual probe AUC=0.98（goal info 持续存在） | NTP-GAR 梯度冲突 + 30x 泛化 gap + turn conditioning 反转 |\n| 干预尝试 | goal re-injection (Appendix H, 失败) | ThreadGate residual gating (失败) + UG/LoRA-only 消融 |\n| 结论 | attention 通道关闭但 residual stream 保留 goal info | 即使在 residual stream 上施加 principled gating，NTP 梯度压制使 gate 无法学到正确的 turn-selective 干预 |\n\n### 共同推论\n\n两种独立干预路线（prompt-level goal re-injection + architecture-level residual gating）均失败，共同指向：\n\n1. 简单的 attention steering 不足以对抗 NTP 的优化压力\n2. 需要更深层的架构改变（如 decoupled goal-processing pathway，或 inference-time attention intervention 绕过训练泛化问题）\n\n### 我们的独特增量\n\nDongre 诊断了问题，但没有解释为什么干预难以成功。我们量化了三个具体障碍：\n1. **NTP-GAR 梯度冲突**（NF1 + 3.1 实验）: NTP loss 在 gate 参数上的梯度方向与 GAR loss 相反\n2. **Attention pattern 不泛化**（NF2 + 3.4 实验）: 训练中学到的 attention redistribution 不迁移到新对话\n3. **Gate 干预强度不足**（NF3）: 推理时 gate 仅 2-7% attenuation，远不足以改变 attention pattern\n\n---\n\n## 6. 论文结构草案（Option A framing）\n\n1. **Abstract** (150-250 words): 问题（GAR 衰减）→ 动机（Dongre residual probe → residual gating 是自然方案）→ 方法（ThreadGate）→ 核心发现（三个失败机制）→ 意义\n2. **Introduction** (5 段): 多轮对话退化 → Dongre 诊断 + residual stream 持续性 → ThreadGate 设计动机 → 三个 negative findings 概述 → 贡献列表\n3. **Related Work**: multi-turn degradation / residual gating & adaptive depth / attention steering\n4. **Background**: GAR 定义（cite Dongre）+ residual stream persistence 证据\n5. **Method**: ThreadGate 架构 + MSE+gate_div loss + 训练设置\n6. **Experiments**: 四路消融 + 跨模型验证 + 训练动力学\n7. **Analysis**: NTP-GAR 梯度冲突 + GAR 泛化性分析 + gate profile 深入分析 + attention 可视化\n8. **Discussion**: 为什么 residual gating 不够 + 对 attention steering 方法的启示 + 潜在解决方向\n9. **Conclusion**: negative result 总结 + 对社区的建议\n\n### 贡献列表（草案）\n\n1. 首个基于 residual stream persistence 证据设计的架构级 GAR 恢复干预（ThreadGate），及其完整失败分析\n2. 发现并量化 NTP-GAR 梯度冲突导致 turn conditioning 反向学习的机制\n3. 量化 GAR 训练信号的泛化性问题（30x training-inference gap），对所有基于辅助 attention loss 的方法有警示意义\n4. 四路消融 + 跨模型验证的完整实验设计，为后续研究提供 baseline 和诊断工具\n\n---\n\n## 7. 实验时间表\n\n| 实验 | GPU 时间 | 依赖 | 预计完成 |\n|------|----------|------|----------|\n| LoRA-only 训练完成 | ~3h (剩余) | 无 | D+0 (2026-05-19) |\n| 四路 eval on standard_conv (Qwen) | ~1h | LoRA-only 完成 | D+0 |\n| 梯度冲突分析 (3.1) | ~10min | v7 checkpoint | D+0 |\n| Attention 可视化 (3.3) | ~20min | 四路 checkpoint | D+0 |\n| GAR 泛化曲线 — 5 checkpoints (3.4) | ~30min | v7 中间 checkpoints | D+1 |\n| 训练动力学可视化 (3.5) | ~0 (纯绘图) | v7_training_dynamics_csv | D+0 |\n| Gate profile 深入分析 (3.2) | ~0 (纯分析) | 四路 eval 数据 | D+1 |\n| Llama 模型下载 | ~30min (网络) | 磁盘清理 | D+1 |\n| Phase 1 GAR 诊断 (Llama) | ~30min | Llama 模型下载 | D+1 |\n| TG v7 训练 (Llama) | ~6h | Llama 模型下载 | D+2 |\n| Llama eval + gate profile | ~1h | Llama TG 完成 | D+2 |\n| [可选] Llama UG + LoRA-only | ~12h | Llama TG eval | D+3-4 |\n\n**总 GPU 时间**: ~12h（核心）+ ~12h（可选 Llama 消融）\n**写作启动**: D+2（Qwen 全部数据就绪后可开始 Method/Background/Related Work）\n**完整初稿**: D+7-10（假设跨模型验证顺利）\n\n---\n\n## 8. 风险与应急\n\n| 风险 | 概率 | 影响 | 应急 |\n|------|------|------|------|\n| LoRA-only 意外优于 TG（gating 有负面贡献） | 低 | 叙事调整：gating 不仅无效还有害（更强的 negative finding） | 额外分析 why gating hurts |\n| Llama 上 GAR 衰减模式与 Qwen 显著不同 | 中 | 跨模型 claim 弱化 | 聚焦 Qwen 深度分析，Llama 作为补充 |\n| Llama 上 ThreadGate 意外成功 | 极低 | 整个 negative framing 需要重写 | 转回 Route A，Qwen 失败 + Llama 成功本身是更有趣的故事 |\n| 磁盘空间不足以同时存 Qwen + Llama checkpoints | 中 | Llama 实验延迟 | 先完成 Qwen 所有分析，删除中间 checkpoints，再下载 Llama |\n| 审稿人认为\"只测了 residual gating 一种方法，negative result 太窄\" | 高 | reject 风险 | Discussion 中系统性分析为什么其他方法（attention re-weighting, positional bias）也面临类似障碍；cite Dongre goal re-injection 失败 |\n| 梯度冲突分析结果不显著（cosine ≈ 0 而非 < 0） | 中 | NF1 的机制解释弱化 | 转为 \"orthogonal gradients = GAR loss 无法有效引导 gate\" 的叙事（NTP 不一定反对，但 GAR 信号太弱被淹没） |\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T10:45:06.723452+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/route_b_design.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_route_b_design_20260519T104143",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-19T10:45:06.723652+00:00_

文件已写入 `artifacts/route_b_design.md`。

内容覆盖：
- 三个论文定位选项（推荐 Option A 为主 + B 融入 Discussion）
- 四路消融 eval 设计及预期结果
- 五个机制分析实验（梯度冲突量化、gate profile 深入、attention 可视化、GAR 泛化曲线、训练动力学三阶段）
- Llama-3.1-8B 跨模型验证（Phase 1 + TG 训练 + 可选消融）
- 与 Dongre et al. 的精确互补定位和独特增量
- 论文结构草案 + 贡献列表
- 时间表（核心 ~12h GPU，D+0 到 D+2 完成 Qwen 全部数据）
- 六项风险评估及应急方案

所有实验设计均基于 paper_framing.md 的 NF1-NF4 和 C1-C6 状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_route_b_design_20260519T104143"
}
```

</details>

---
