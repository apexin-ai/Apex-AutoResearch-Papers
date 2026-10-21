# cron hook mvp probe untrained 20260515T232259 607419

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 2
- **Tool calls:** 30
- **Original source:** `logs/chats/archive/cron_hook_mvp_probe_untrained_20260515T232259_607419.jsonl`
- **Structured JSON:** [`ebdcefdb2cd45ecffe35.json`](../../sessions/eb/ebdcefdb2cd45ecffe35.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-15T20:13:06.667566+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #4。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 westd-19183 的 `cuda:0` 和 `cuda:1`，无其他分配
- Registry 有重复条目：`d021_instruction_ablation` / `lg_instruction_ablation` 和 `d021_output_head_analysis` / `lg_output_head_analysis` 是同一实验的重复注册，提交时用 `d021_*` 前缀的，`lg_*` 前缀的作废
- Untrained model 的 `from_config()` 没用固定 seed，但 checkpoint 已持久化到磁盘，不要重新生成
- 分析 Worker 不得覆盖 registry 的 `spec` 字段（已有教训）
- transformers 版本差异（4.40.1 vs 4.57.6）：trained/untrained 用同版本提取，对比有效，但复现需注意

### 2. 🖥️ 基础设施快照
- 服务器：**westd-19183**，2×RTX PRO 6000
- 代码目录：`/root/vla-ssd`（git repo）
- 数据/模型/结果：`/root/autodl-tmp/vla-ssd/`（数据盘）
  - 模型：`checkpoints/{openvla-7b, openvla-7b-untrained, dinov2-large}/`
  - LIBERO-10 特征：`features/{trained, untrained, dinov2}/`（每个 ~52GB）
  - LIBERO-Goal 特征：`features/{trained_libero_goal, untrained_libero_goal, dinov2_libero_goal}/`
  - 结果：`results/` 下各子目录
- Python：`/root/miniconda3/bin/python`，conda base 环境，**不是 venv**
- 激活命令：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 活跃 Worker（4 个 running）：
  - `worker_ssh_instruction-ablation` — D021 Exp-1 instruction ablation 实验
  - `worker_ssh_output-head-analysis` — D021 Exp-2 output head 分析
  - `worker_ssh_pca1024-goal-classification` — 可能是遗留任务（D018/D019 时期）
  - `worker_ssh_exp1-pca-linear-perlayer` — 可能是遗留任务
- 无活跃 cron（reconcile 返回 0）

### 3. 📊 当前状态
**刚完成**：D021 framing pivot 到 "Architecture Trumps Training"。6 轮实验（temporal distance / action prediction / action-delta / goal classification / PCA-linear / RSA）× 2 benchmark（LIBERO-10 + LIBERO-Goal）一致结论：VLA >> DINO（架构效应），trained ≈ untrained（训练无显著表征变化）。

**正在进行**：D021 的两个验证实验已派 Worker，registry 状态仍为 PREPARING：
1. **Instruction Ablation**（d021_instruction_ablation）：去掉 instruction → RSA 应 collapse → 证明 architecture pathway。PASS: ρ 显著低于 0.48
2. **Output Head Analysis**（d021_output_head_analysis）：trained vs untrained 权重差集中在 output mapping → 解释 "representations unchanged but behavior improved"

**等待中**：
- 4 个 Worker 回调（上述 2 个 D021 + 2 个可能遗留的 Worker）
- Reviewer 独立评估 D021 framing（已提交审查）
- 两个验证实验 positive → complete_mvp() → 进入 research/writing 阶段

**Registry 统计**：33 experiments total — 18 success / 5 negative / 0 failed / 6 killed / 4 preparing

### 4. 📋 待办（条件触发式）
- D021 instruction ablation Worker 回调 → RSA ρ collapse 到显著低于 0.48 → 更新 registry DONE(success)，汇报 Director
- D021 instruction ablation ρ 仍 ≈ 0.48 → FAIL，视觉 state 本身提供 action structure，architecture pathway 证据不够直接 → 产出 Framing 调整提案
- D021 output head analysis Worker 回调 → output head norm ratio >> LLM deep layer mean (>3x) → success → 汇报
- **两个 D021 验证都 positive** → `complete_mvp()` → 立即进 research/writing 阶段 → 派 paper-plan Worker → 争取 May 16 启动论文写作
- **任一 D021 验证 negative** → 不动 paper，先产出 Framing 调整提案给 Director，备选 Option A (redundancy) 可兜底
- 遗留 Worker（pca1024-goal-classification / exp1-pca-linear-perlayer）回调 → 检查是否产出有用结果，若已过时则忽略并清理

### 5. 🎯 战略上下文
**核心结论链**：D014(MVP-2判死: action prediction G2 FAIL) → D015(pivot LIBERO-Goal) → D019(goal classification 方法论失败) → D020(RSA G1+G3 PASS, G2 FAIL) → D021(framing pivot "Architecture Trumps Training")

**论文 story**：VLA 的 instruction conditioning 来自架构设计（multi-modal fusion pathway），不是 LLM fine-tuning。与 Grant 2026 互补：他们发现 behavioral level 的 "encoded but not used" paradox，我们在 representation level 发现 "not even encoded differently"。

**CoRL 2026 时间线**：Abstract DDL May 26 (11天)，Paper DDL May 29 (14天)。验证实验应在 May 15-16 完成，May 16 确认 framing，May 16-17 启动 Paper Agent。时间极紧。

**易错点**：
- 不要把 LIBERO-10 结果和 LIBERO-Goal 结果混为一谈——LIBERO-10 是 in-distribution（trained checkpoint 就是在这上面 fine-tuned 的），LIBERO-Goal 是 OOD
- Untrained VLA 不是"没有 vision"——它保留了完整的 SigLIP vision encoder（0.80B），只有 LLM（6.74B）是 random init
- RSA 的 Δρ=0.003 不是"接近显著"，是远低于 0.08 threshold——不要试图用更好的超参数救回来
- Goal classification 100% vs 100% 是 probe capacity 饱和（MLP+4096+10 classes），不是 bug，已用 PCA+linear 验证仍无差异
- `lg_*` 前缀的 PREPARING 实验是 `d021_*` 的重复，别重复提交

## 项目硬约束 (memory.md 节选)

## 技术约束

- Untrained model: from_config() 重新初始化 LLM（6.74B random），保留 SigLIP（0.80B）
- D017: 统一用 LIBERO-10 fine-tuned checkpoint（LIBERO-Goal 是 OOD 测试）
- Token 聚合：Primary = last pre-action token
- 存储：根分区 ~30GB，大文件在 /root/autodl-tmp/vla-ssd/
- transformers 版本差异（4.40.1 vs 4.57.6），trained/untrained 同版本，对比有效
- **分析 Worker 不得覆盖 spec 字段**

## 可查的历史
前 11 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:mvp_probe_untrained",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-15T20:13:17.236217+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-15T20:13:17.236646+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T20:13:24.065069+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "vla-ssd",
  "filters": "{'status': 'PREPARING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "vla-ssd",
    "filters": "{'status': 'PREPARING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T20:13:24.516948+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"d021_output_head_analysis\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:11:17.179Z\", \"updated_at\": \"2026-05-15T20:11:17.180Z\", \"hypothesis\": \"D021 Exp-2: Output Head Analysis. Compare trained vs untrained VLA weight differences per layer (Frobenius norm ratio). PASS: output head norm ratio >> LLM deep layer mean (>3x), confirming shallow adaptation. FAIL: differences uniformly distributed.\"}, \"d021_instruction_ablation\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:11:15.503Z\", \"updated_at\": \"2026-05-15T20:11:15.503Z\", \"hypothesis\": \"D021 Exp-1: Instruction Ablation on untrained VLA. Replace instruction tokens with empty string, extract LIBERO-Goal features, run RSA. If architecture pathway provides action-relevant structure, RSA should collapse from ρ≈0.48 to significantly lower. PASS: ρ significantly below 0.48; FAIL: ρ still ≈ 0.48.\"}, \"lg_output_head_analysis\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:08:58.398Z\", \"updated_at\": \"2026-05-15T20:08:58.398Z\", \"hypothesis\": \"D021 Exp-2: Output Head Analysis. Compare trained vs untrained VLA weight differences across layers. If training does \\\"shallow adaptation\\\", output head weight diff >> middle layer weight diff. Explains \\\"representations unchanged but behavior improved\\\".\"}, \"lg_instruction_ablation\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:08:57.146Z\", \"updated_at\": \"2026-05-15T20:08:57.146Z\", \"hypothesis\": \"D021 Exp-1: Instruction Ablation. Extract LIBERO-Goal features with empty instruction (trained + untrained VLA), then run RSA. If instruction pathway is the source of action-relevant structure, RSA should collapse from ρ≈0.49 to <0.15. PASS: ρ<0.15; PARTIAL: 0.15<ρ<0.30; FAIL: ρ≥0.30.\"}}, \"count\": 4, \"total\": 4, \"baseline\": null}, \"error\": n
…[truncated 51 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 451
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T20:13:24.517422+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "vla-ssd",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "vla-ssd",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T20:13:24.971345+00:00_

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
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T20:13:24.971741+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1853}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 454
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T20:13:25.624973+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 653
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T20:13:25.625413+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "vla-ssd",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "vla-ssd",
    "status": "running"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T20:13:25.776616+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_ssh_pca1024-goal-classification_20260515T191620\", \"task_type\": \"ssh:pca1024-goal-classification\", \"project\": \"vla-ssd\", \"status\": \"running\", \"started_at\": \"2026-05-15T19:16:21.020556+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_ssh_exp1-pca-linear-perlayer_20260515T192115\", \"task_type\": \"ssh:exp1-pca-linear-perlayer\", \"project\": \"vla-ssd\", \"status\": \"running\", \"started_at\": \"2026-05-15T19:21:15.867214+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_ssh_instruction-ablation_20260515T200929\", \"task_type\": \"ssh:instruction-ablation\", \"project\": \"vla-ssd\", \"status\": \"running\", \"started_at\": \"2026-05-15T20:09:29.170631+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_ssh_output-head-analysis_20260515T200957\", \"task_type\": \"ssh:output-head-analysis\", \"project\": \"vla-ssd\", \"status\": \"running\", \"started_at\": \"2026-05-15T20:09:57.870247+00:00\", \"ended_at\": null}], \"count\": 4}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T20:13:26.078138+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "report.md"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T20:13:26.080130+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **lg_rsa_analysis** (negative): D019/D020: RSA on LIBERO-Goal features. Same-scene/different-goal cross-goal RSA: representation RDM vs action RDM correlation. Gates (D020): G1 trained best-layer RSA ρ > 0.15; G2 Δρ(trained-untrained) > 0.08 with bootstrap 95% CI excluding 0; G3 trained ρ > DINO ρ (any positive margin).\\n- **lg_shuffled_token_control** (killed): Control: token-shuffled goal classification on trained VLA features. Shuffling token order destroys positional/sequential info. NOTE: uses bare task name prompt (not formatted prompt like main pipeline) — results not directly comparable.\\n- **lg_pca1024_linear_pertimestep** (negative): D018 Exp-2: PCA-1024 + Linear Probe per-timestep (10 bins). Tests whether trained VLA shows stronger goal encoding than untrained at early timesteps (visual ambiguity highest). Success: t=0 bin Δ(trained-untrained) > 15pp.\\n\\n## 趋势\\n成功 18 / 负向 5 / 失败 0 / 共 29\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-19183: 无 GPU 信息\\n\\n## 告警\\n- mvp2_action_probe: 已被终止 — unknown\\n- lg_extract_trained_r2: 已被终止 — unknown\\n- lg_extract_untrained_r2: 已被终止 — unknown\\n- lg_extract_trained_r1: 已被终止 — unknown\\n- lg_extract_untrained_r1: 已被终止 — unknown\\n- lg_shuffled_token_control: 已被终止 — unknown\\n\", \"total_chars\": 1319, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T20:13:26.080505+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T20:13:26.181720+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\", \"content\": \"# vla-ssd — Research Dashboard\\n\\n> 最后更新: 2026-05-15 20:09 UTC | 更新原因: D021: Framing pivot to \\\"Architecture Trumps Training\\\", instruction ablation + output head analysis launched\\n\\n## 核心方向\\n\\n**\\\"Architecture Trumps Training\\\"**（D021）: VLA 的 instruction conditioning 来自架构设计（multi-modal fusion），不是 LLM fine-tuning。5 轮 probing × 2 benchmark 一致：trained ≈ untrained >> DINO。\\n\\n与 Grant 2026 互补：behavioral (\\\"encoded but not used\\\") → representational (\\\"not even encoded differently\\\")。\\n\\n## 当前进展\\n\\n- **阶段**: Framing pivot（D021）→ 验证实验中\\n- **MVP 核心发现**: G1+G3 PASS / G2 FAIL 模式跨所有方法论一致\\n  - Temporal distance: Δρ=0.043（vision-dominated）\\n  - Action prediction: ΔR²=0.067, DINO ≈ trained\\n  - Goal classification: trained 100% = untrained 100%\\n  - RSA: Δρ=0.003, trained ρ=0.49 vs untrained ρ=0.48\\n- **架构效应确认**: VLA >> DINO 在所有度量上稳定（G3 consistently PASS）\\n- **Layer stability**: trained 31/33 层有效 vs untrained ~15/33（secondary finding）\\n\\n## 近期任务\\n\\n- [ ] **[P0] Instruction ablation**（GPU 0）: 去掉 instruction → RSA 应 collapse → 证明 architecture pathway\\n- [ ] **[P1] Output head analysis**（GPU 1/CPU）: trained vs untrained 权重差异集中在 output mapping\\n- [ ] Reviewer 独立评估 D021 framing（已提交）\\n- [ ] 两个验证实验 positive → complete_mvp() → 进入 research/writing 阶段\\n- [ ] Registry 清理（已派单）\\n\\n## 时间线（CoRL 2026）\\n\\n| 里程碑 | 日期 | 剩余天数 |\\n|--------|------|---------|\\n| Abstract DDL | May 26 | 11 |\\n| Paper DDL | May 29 | 14 |\\n| 验证实验完成 | May 15-16 | 0-1 |\\n| Framing 确认 | May 16 | 1 |\\n| complete_mvp → research | May 16 | 1 |\\n| Paper Agent 启动 | May 16-17 | 1-2 |\\n\\n## GPU 预算\\n\\nwestd-19183: 2×RTX PRO 6000 | 当前 2/2 占用（instruction ablation + output head）\\n\\n## 关键风险\\n\\n1. **[中] Instruction ablation 不 collapse** — 如果去掉 instruction 后 RSA 仍高，说明 visual state 本身就提供 action structure → architecture pathway 证据不
…[truncated 1699 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T20:13:48.907748+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__get_worker_status",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__get_worker_status",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T20:13:48.958644+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T20:13:53.475112+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_ssh_instruction-ablation_20260515T200929",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_ssh_instruction-ablation_20260515T200929",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T20:13:53.977306+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_ssh_instruction-ablation_20260515T200929\", \"status\": \"running\", \"task_type\": \"ssh:instruction-ablation\", \"project\": \"vla-ssd\", \"started_at\": \"2026-05-15T20:09:29.170631+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ssh_execute\", \"ssh_execute\", \"ssh_execute\", \"ssh_read_only\", \"ssh_read_only\"], \"last_text\": \"提取正在运行，首个任务有 7027 steps。CUDA warmup 后速度应提升。等几分钟再检查。\", \"turn_count\": 15}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T20:13:54.479999+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_ssh_output-head-analysis_20260515T200957",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_ssh_output-head-analysis_20260515T200957",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T20:13:54.982127+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_ssh_output-head-analysis_20260515T200957\", \"status\": \"running\", \"task_type\": \"ssh:output-head-analysis\", \"project\": \"vla-ssd\", \"started_at\": \"2026-05-15T20:09:57.870247+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ssh_execute\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_execute\", \"ssh_execute\"], \"last_text\": \"进程活跃 (1039% CPU, ~6.5GB RSS, 运行 ~2 分钟)。继续等待。\", \"turn_count\": 34}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T20:13:54.982485+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_ssh_pca1024-goal-classification_20260515T191620",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_ssh_pca1024-goal-classification_20260515T191620",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T20:13:55.434256+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_ssh_pca1024-goal-classification_20260515T191620\", \"status\": \"running\", \"task_type\": \"ssh:pca1024-goal-classification\", \"project\": \"vla-ssd\", \"started_at\": \"2026-05-15T19:16:21.020556+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\"], \"last_text\": \"Layer 13 has been running for an unusually long time. Let me verify the process.\", \"turn_count\": 37}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 451
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T20:13:55.485089+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_ssh_exp1-pca-linear-perlayer_20260515T192115",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_ssh_exp1-pca-linear-perlayer_20260515T192115",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T20:13:55.535766+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_ssh_exp1-pca-linear-perlayer_20260515T192115\", \"status\": \"running\", \"task_type\": \"ssh:exp1-pca-linear-perlayer\", \"project\": \"vla-ssd\", \"started_at\": \"2026-05-15T19:21:15.867214+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\"], \"last_text\": \"Layer 15 done (acc=1.0000). Halfway through trained_vla (15/33). Still 100%. ~17 more layers. Let me check less frequently now — every ~5 minutes.\", \"turn_count\": 29}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T20:14:21.227694+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "project": "vla-ssd",
  "text": "[资源] GPU 分配 2/2 (westd-19183 cuda:0,1) | Worker 池 4 (GPU 2 / CPU 2)\n\n**Loop #4 Session Start 状态汇报**\n\nD021 \"Architecture Trumps Training\" 两个验证实验 Worker 均活跃：\n\n1. **Instruction Ablation** (d021_instruction_ablation, GPU 0): Turn 15, 正在提取 no-instruction 特征（7027 steps）。预计特征提取 ~30-60 min → 然后 RSA 分析 ~10 min → 回调。\n2. **Output Head Analysis** (d021_output_head_analysis, GPU 1→CPU): Turn 34, 权重差异分析进行中（1039% CPU, 6.5GB RSS）。预计 ~10-20 min 完成。\n\n两个遗留 Worker（D018/D019 时期）仍在跑：\n- pca1024-goal-classification: 可能卡在 Layer 13，不在关键路径\n- exp1-pca-linear-perlayer: 15/33 层，100% accuracy everywhere（再次确认探针饱和，不改变 D021 结论）\n\n**等待中**: 两个 D021 验证 Worker 回调 → 结果决定是否 complete_mvp() 进入论文阶段。CoRL Paper DDL 还剩 14 天。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "project": "vla-ssd",
    "text": "[资源] GPU 分配 2/2 (westd-19183 cuda:0,1) | Worker 池 4 (GPU 2 / CPU 2)\n\n**Loop #4 Session Start 状态汇报**\n\nD021 \"Architecture Trumps Training\" 两个验证实验 Worker 均活跃：\n\n1. **Instruction Ablation** (d021_instruction_ablation, GPU 0): Turn 15, 正在提取 no-instruction 特征（7027 steps）。预计特征提取 ~30-60 min → 然后 RSA 分析 ~10 min → 回调。\n2. **Output Head Analysis** (d021_output_head_analysis, GPU 1→CPU): Turn 34, 权重差异分析进行中（1039% CPU, 6.5GB RSS）。预计 ~10-20 min 完成。\n\n两个遗留 Worker（D018/D019 时期）仍在跑：\n- pca1024-goal-classification: 可能卡在 Layer 13，不在关键路径\n- exp1-pca-linear-perlayer: 15/33 层，100% accuracy everywhere（再次确认探针饱和，不改变 D021 结论）\n\n**等待中**: 两个 D021 验证 Worker 回调 → 结果决定是否 complete_mvp() 进入论文阶段。CoRL Paper DDL 还剩 14 天。"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T20:14:25.053141+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 3825
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T20:14:36.729171+00:00_

Session-start 初始化完成。4 个 Worker 活跃（2 个 D021 验证 + 2 个遗留），已向 Director 汇报。等待 Worker 回调。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:mvp_probe_untrained"
}
```

</details>

---

## Round 2

36 recorded events

### User

_source line 29 · 2026-05-15T23:21:23.242917+00:00_

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
  "session": "cron:hook:mvp_probe_untrained",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T23:21:32.002208+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__read_experiment_plan_with_status,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_worker_status",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__read_experiment_plan_with_status,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_worker_status",
    "max_results": "8"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T23:21:32.052991+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T23:21:34.822354+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "vla-ssd",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "vla-ssd",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T23:21:35.324085+00:00_

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
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T23:21:35.876800+00:00_

Error: result (69,948 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-89bf97d0/69c351dc-d840-4ceb-a075-4f18238e191b/tool-results/mcp-agent-ml-research-read_registry-1778887295334.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-89bf97d0/69c351dc-d840-4ceb-a075-4f18238e191b/tool-results/mcp-agent-ml-research-read_registry-1778887295334.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1054
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T23:21:35.877283+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 553
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T23:21:35.877616+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "report.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "report.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T23:21:36.332192+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- lg_output_head_analysis: D021 Exp-2: Output Head Analysis. Compare trained vs untrained VLA weight differences across layers. If training does \\\"shallow adaptation\\\", output head weight diff >> middle layer weight diff. Explains \\\"representations unchanged but behavior improved\\\".（排队等待 GPU）\\n- lg_instruction_ablation: D021 Exp-1: Instruction Ablation. Extract LIBERO-Goal features with empty instruction (trained + untrained VLA), then run RSA. If instruction pathway is the source of action-relevant structure, RSA should collapse from ρ≈0.49 to <0.15. PASS: ρ<0.15; PARTIAL: 0.15<ρ<0.30; FAIL: ρ≥0.30.（排队等待 GPU）\\n\\n## 近期结论\\n- **p0_bootstrap_ci_training_effect** (success): P0: Bootstrap CI on training effect (image_mean aggregation). Trained RSA=0.5014 vs untrained RSA=0.4847, Δ=+0.017. Task-level resampling bootstrap 95% CI. If CI excludes 0 → Claim 3 needs minor adjustment (\\\"minimal but detectable\\\"). If CI includes 0 → Claim 3 \\\"invariance\\\" holds.\\n- **p0_image_mean_rsa_verify** (success): P0 CRITICAL: Verify Claim 2 (LLM degrades action alignment 0.615→0.488) is not an aggregation artifact. SigLIP uses mean pooling, VLA used last_preaction. Re-run RSA with image_mean feature key for trained with-inst and untrained with-inst. If image_mean RSA ≈ 0.61 → Claim 2 is artifact. If ≈ 0.49 → Claim 2 holds.\\n- **plan_003_perlayer_degradation** (success): D028 plan_003: Per-layer RSA degradation curve. Track RSA from SigLIP+projector output (L0=0.615) through LLM layers 1-32 (~0.48). If monotonic decrease → LLM progressively degrades action alignment. If non-monotonic → some layers partially recover. Supports Claim 2 (LLM degrades action-relevant structure).\\n\\n## 趋势\\n成功 23 / 负向 7 / 失败 0 / 共 36\\n\\n## 下一步\\n
…[truncated 419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T23:21:36.332706+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T23:21:37.035365+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\", \"content\": \"# vla-ssd — Research Dashboard\\n\\n> 最后更新: 2026-05-15 22:29 UTC | 更新原因: D028: complete_mvp 完成，进入 research 阶段。paper_framing.md + experiment_plan.yaml 已写，Dream 已提交\\n\\n## 核心方向\\n\\n**\\\"Vision Encoder Dominance: The Architectural Source of Action-Relevant Representations in VLAs\\\"**（D028 确定）\\n\\n三个 Core Claims（详见 paper_framing.md）：\\n1. Action-relevant 表征源自 frozen SigLIP vision encoder（RSA 0.615 >> VLA 0.488 >> DINO 0.388）\\n2. LLM processing 降低 action alignment（degrader, 非 passthrough）\\n3. Training 和 instruction 均不改变表征结构（2×2 matrix 收敛）\\n\\n## 当前进展\\n\\n- **阶段**: Research — post-MVP kickoff 完成，Dream 模拟中\\n- **MVP 结果**: 原假设（training 注入知识）系统性否定 → pivot 到 Vision Encoder Dominance\\n- **P0 实验全部完成**: 7 probing methods × 2 benchmarks + SigLIP-only RSA smoking gun + instruction ablation + 2×2 matrix + output head analysis\\n- **P1 待做**: per-layer RSA degradation curve（CPU）、random instruction control（2h GPU）\\n- **Dream**: `dream_20260515T222933` pending，等回调后决定是否调整 framing/plan\\n\\n## 近期任务\\n\\n- [ ] 等 Dream 完成 → 分析审稿报告 → 决定是否调整 framing/plan\\n- [ ] Dream 通过后批准 P1 实验（per-layer degradation curve + random instruction control）\\n- [ ] 启动 Paper Agent（Full Draft 模式，CoRL 2026）\\n- [ ] P1 实验结果补入论文\\n\\n## 时间线（CoRL 2026）\\n\\n| 里程碑 | 日期 | 剩余天数 |\\n|--------|------|---------|\\n| Abstract DDL | May 26 | 11 |\\n| Paper DDL | May 29 | 14 |\\n| Dream 完成 | May 15-16 | 0-1 |\\n| P1 实验完成 | May 16-17 | 1-2 |\\n| Paper Agent Full Draft | May 17-20 | 2-5 |\\n| Review + Iteration | May 20-28 | 5-13 |\\n\\n## GPU 预算\\n\\nwestd-19183: 2×RTX PRO 6000 | 当前 0/2 占用（等 Dream 结果后派 P1 实验）\\nP0 已用 ~13h GPU | P1 需 ~2h GPU + CPU | P2 需 ~4h（时间允许）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D030 | 2026-05-15 | D030: Dream 三档均低于 acceptance（best borderline rejec | d027_siglip_only_rsa, mvp2_action_trained, mvp2_action_
…[truncated 1387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 702
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T23:21:37.086097+00:00_

called mcp__agent-ml-research__load_project_config

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config</summary>

```json
{
  "project_name": "vla-ssd",
  "section": "execution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__load_project_config",
  "tool_args": {
    "project_name": "vla-ssd",
    "section": "execution"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T23:21:37.186943+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"vla-ssd\", \"section\": \"execution\", \"config\": {\"execution\": {\"gpu_ids\": [\"cuda:0\", \"cuda:1\"], \"project_path\": \"/root/vla-ssd\", \"servers\": [\"westd-19183\"]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T23:21:37.237541+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "vla-ssd",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "vla-ssd",
    "status": "running"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T23:21:37.338406+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_analysis_no_inst_image_mean_rsa_20260515T231839\", \"task_type\": \"analysis:no_inst_image_mean_rsa\", \"project\": \"vla-ssd\", \"status\": \"running\", \"started_at\": \"2026-05-15T23:18:40.030443+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_code_plan_008_prep_20260515T231944\", \"task_type\": \"code:plan_008_prep\", \"project\": \"vla-ssd\", \"status\": \"running\", \"started_at\": \"2026-05-15T23:19:44.427860+00:00\", \"ended_at\": null}], \"count\": 2}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T23:21:44.114993+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-89bf97d0/69c351dc-d840-4ceb-a075-4f18238e191b/tool-results/mcp-agent-ml-research-read_registry-1778887295334.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor e in exps:\n    eid = e.get('exp_id','?')\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','')\n    hypothesis = e.get('hypothesis','')[:80] if e.get('hypothesis') else ''\n    print(f'{eid} | {status} | {conclusion} | {hypothesis}')\n\"",
  "description": "Parse registry experiments summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-89bf97d0/69c351dc-d840-4ceb-a075-4f18238e191b/tool-results/mcp-agent-ml-research-read_registry-1778887295334.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor e in exps:\n    eid = e.get('exp_id','?')\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','')\n    hypothesis = e.get('hypothesis','')[:80] if e.get('hypothesis') else ''\n    print(f'{eid} | {status} | {conclusion} | {hypothesis}')\n\"",
    "description": "Parse registry experiments summary"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T23:21:44.517976+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    eid = e.get('exp_id','?')
          ^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T23:21:44.919839+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T23:21:44.920302+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-3/proje…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T23:21:44.920566+00:00_

called mcp__agent-ml-research__read_experiment_plan_with_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_experiment_plan_with_status</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_experiment_plan_with_status",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T23:21:44.920794+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-3/proje…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_experiment_plan_with_status",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T23:21:49.888025+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-89bf97d0/69c351dc-d840-4ceb-a075-4f18238e191b/tool-results/mcp-agent-ml-research-read_registry-1778887295334.txt') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint(type(exps))\nif isinstance(exps, dict):\n    for eid, e in exps.items():\n        status = e.get('status','?')\n        conclusion = e.get('conclusion','')\n        hypothesis = (e.get('hypothesis','') or '')[:80]\n        print(f'{eid} | {status} | {conclusion} | {hypothesis}')\nelif isinstance(exps, list):\n    print(exps[0])\n\"",
  "description": "Parse registry with correct structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nwith open('/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-89bf97d0/69c351dc-d840-4ceb-a075-4f18238e191b/tool-results/mcp-agent-ml-research-read_registry-1778887295334.txt') as f:\n    data = json.loads(f.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint(type(exps))\nif isinstance(exps, dict):\n    for eid, e in exps.items():\n        status = e.get('status','?')\n        conclusion = e.get('conclusion','')\n        hypothesis = (e.get('hypothesis','') or '')[:80]\n        print(f'{eid} | {status} | {conclusion} | {hypothesis}')\nelif isinstance(exps, list):\n    print(exps[0])\n\"",
    "description": "Parse registry with correct structure"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T23:21:49.989496+00:00_

&lt;class 'dict'>
p0_bootstrap_ci_training_effect | DONE | success | P0: Bootstrap CI on training effect (image_mean aggregation). Trained RSA=0.5014
p0_image_mean_rsa_verify | DONE | success | P0 CRITICAL: Verify Claim 2 (LLM degrades action alignment 0.615→0.488) is not a
plan_003_perlayer_degradation | DONE | success | D028 plan_003: Per-layer RSA degradation curve. Track RSA from SigLIP+projector 
lg_output_head_analysis | QUEUED | killed | D021 Exp-2: Output Head Analysis. Compare trained vs untrained VLA weight differ
lg_instruction_ablation | QUEUED | killed | D021 Exp-1: Instruction Ablation. Extract LIBERO-Goal features with empty instru
d027_siglip_only_rsa | DONE | success | D027 Exp-1 (SMOKING GUN): Extract SigLIP+projector output features (LLM input em
d027_trained_no_inst_rsa | DONE | success | D027 Exp-2: Extract trained VLA features with empty instruction on LIBERO-Goal, 
d021_instruction_ablation | DONE | negative | D021 Exp-1 (HARD GATE): Instruction Ablation on untrained VLA. Replace instructi
d021_output_head_analysis | DONE | negative | D021 Exp-2: Output Head Analysis. Compare trained vs untrained VLA weight differ
lg_rsa_analysis | DONE | negative | D019/D020: RSA on LIBERO-Goal features. Same-scene/different-goal cross-goal RSA
lg_shuffled_token_control | DONE | killed | Control: token-shuffled goal classification on trained VLA features. Shuffling t
lg_pca1024_linear_pertimestep | DONE | negative | D018 Exp-2: PCA-1024 + Linear Probe per-timestep (10 bins). Tests whether traine
lg_gc_trained_frame0 | DONE | success | Frame-0-only goal classification on trained VLA features (33 layers). Tests inst
lg_gc_untrained | DONE | negative | Goal classification probe on untrained VLA LIBERO-Goal features (33 layers). Bas
lg_gc_dino | DONE | success | DINO-V2 LIBERO-Goal goal classification probe (Sanity-GC gate). DINO acc must be
lg_dino_extract | DONE | success | DINO-V2 LIBERO-Goal feature extraction — vision-only baseline for Goal Classific
lg_gc_trai
…[truncated 1900 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-15T23:21:52.854548+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T23:21:53.409340+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/memory.md\", \"content\": \"# VLA-SSD Project Memory\\n\\n## SMOKING GUN 确认：SigLIP+Projector RSA = 0.6153（2026-05-15）\\n\\n**d027_siglip_only_rsa 结果**: SigLIP+projector 直接输出（不过 LLM）的 RSA = 0.6153 [95% CI: 0.5257, 0.6954]。\\n\\n**关键发现：LLM 降低 action alignment（不是 passthrough）**：\\n- SigLIP+projector: **0.6153**\\n- Full VLA（任何条件）: ~0.48-0.49\\n- DINO: 0.388\\n\\nLLM 不仅没增强 action-relevant structure，反而将 RSA 从 0.615 降到 ~0.488（约 20% 下降）。这比 \\\"passthrough\\\" 更强——是 \\\"degradation\\\"。\\n\\n**机制解释**: SigLIP image-text 预训练产生的 visual features 天然具有强 action-relevant 结构。Projector 保持这一结构（cos_sim=1.0 frozen）。LLM 的高维 token mixing 稀释了这种结构（trained 和 untrained LLM 稀释程度一致）。\\n\\n## Per-Layer Degradation Curve 发现（2026-05-15）\\n\\n**plan_003_perlayer_degradation 结果**：降解非单调，集中在 embedding interface。\\n\\n**关键机制洞察**：\\n- Proj→L1 是最大 single-step drop（0.13–0.25，~20–40%），token embedding 是 degradation bottleneck\\n- L0（embedding layer）是异常值：trained 模型 RSA≈0，结构从 L1 才开始恢复\\n- 中间层有 partial recovery（non-monotonic），LLM 不是 \\\"progressive degrader\\\"\\n- **no-inst trained 独特模式**：唯一呈 L1→L30 持续上升的条件（peak at L30），training 在无 instruction 时让 LLM 逐层积累 action 信号。其余 3 个条件均 non-monotonic\\n- 总降解幅度 ~0.13：best LLM layer 仍比 projector 低 ~0.127\\n\\n**对 Claim 2 措辞影响**：应从 \\\"LLM degrades action alignment\\\" 精炼为 \\\"LLM's token embedding interface introduces primary degradation; subsequent layers partially but incompletely recover\\\"。这个 nuance 对 discussion section 很重要——说明 LLM 不是纯粹有害，而是 \\\"lossy interface + partial recovery\\\"。\\n\\n## 完整 2×2 Matrix + SigLIP-only（2026-05-15）\\n\\n| 条件 | RSA | 备注 |\\n|------|-----|------|\\n| **SigLIP+Projector (no LLM)** | **0.6153** | smoking gun |\\n| Trained with-inst | 0.4876 | L9 peak |\\n| Trained no-inst | 0.489 | L30 peak |\\n| Untrained with-inst | 0.4846 | L12 peak |\\n| Untrained no-inst | 0.4802 | — |\\n| DINO | 0.388 | — |\\n\\n**结论**: 所有 4 个 full
…[truncated 2393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 554
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-15T23:21:53.409883+00:00_

called mcp__agent-ml-research__read_experiment_plan_with_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_experiment_plan_with_status</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_experiment_plan_with_status",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-15T23:21:53.861970+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": [{\"id\": \"plan_001\", \"claim\": 1, \"description\": \"SigLIP+Projector RSA vs Full VLA vs DINO — 证明 action-relevant 结构源自 frozen vision encoder\", \"priority\": \"P0\", \"gpu_budget_hours\": 1, \"deps\": [], \"registry_id\": \"d027_siglip_only_rsa\", \"status\": \"DONE\", \"result\": \"RSA=0.615 >> VLA 0.488 >> DINO 0.388\", \"conclusion\": \"success\", \"metrics\": {\"siglip_projector_rsa\": 0.6153, \"bootstrap_95_ci\": [0.5257, 0.6954], \"comparison\": {\"siglip_projector\": 0.6153, \"trained_with_inst\": 0.4876, \"untrained_with_inst\": 0.4846, \"untrained_no_inst\": 0.4802, \"trained_no_inst\": 0.489, \"dino\": 0.388}, \"llm_degradation\": \"LLM reduces RSA from 0.615 (projector output) to ~0.488 (LLM hidden states)\", \"gate_judgment\": \"PASS — SigLIP+projector RSA=0.6153 >> 0.45-0.50 threshold. Vision encoder is the source of action-relevant structure. LLM is not passthrough but actually degrades action alignment.\"}}, {\"id\": \"plan_002\", \"claim\": 1, \"description\": \"DINO baseline RSA — standalone vision model 参照\", \"priority\": \"P0\", \"gpu_budget_hours\": 0.5, \"deps\": [], \"registry_id\": \"dinov2_baseline\", \"status\": \"DONE\", \"result\": \"RSA=0.388\", \"conclusion\": \"success\", \"metrics\": {\"temporal_distance_rho\": 0.833, \"temporal_distance_rho_pooled\": 0.833, \"per_task_rho_mean\": 0.9008, \"per_task_rho_range\": [0.41, 0.68], \"per_task_n_pairs\": 500, \"R2\": 0.687, \"MAE\": 0.127, \"feature_dim\": 1024, \"num_layers\": 1, \"probe_type\": \"mlp_adam_early_stopping\", \"training_time_seconds\": 7.5, \"note\": \"pooled ρ=0.833 inflated by cross-task variance; per-task mean ρ=0.9008 is correct comparison baseline (updated per D005/D006)\", \"subtask_macro_auc\": 0.9717, \"subtask_auc_per_predicate\": {\"subtask_0\": 0.9694, \"subtask_1\": 0.9739}, \"subtask_labels\": \"auto-extracted from MuJoCo state transitions (2 subtasks per task)\", \"subtask_probe_type\": \"sklearn_lo
…[truncated 6588 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_experiment_plan_with_status",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-15T23:21:54.063439+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "paper_framing.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "paper_framing.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-15T23:21:54.114495+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md\", \"content\": \"# Paper Framing — vla-ssd\\n\\n## Target Venue\\n- Primary: CoRL 2026\\n- Deadline: Abstract May 26, Paper May 29\\n- Format: 8 pages + references\\n\\n## Core Claims (3 条)\\n\\n1. **Vision Encoder Dominance**: VLA 中 action-relevant 表征结构由 frozen vision encoder（SigLIP）决定。SigLIP+projector 的 RSA 与 action structure 的相关性（ρ=0.615）远高于完整 VLA（ρ≈0.501, image_mean 聚合）和 standalone vision model（DINOv2 ρ=0.388）。\\n2. **LLM Degrades Action Alignment**: LLM 的 token embedding interface 引入主要降解（Proj→L1 drop 20-40%），后续层部分恢复但净降解 ~18% 持续存在（SigLIP 0.615 → VLA 0.501，用相同 mean pooling 聚合）。这一模式在 trained/untrained、with/without instruction 四种条件下一致。Per-layer curve 显示非单调降解（非简单递减），LLM self-attention 部分恢复 action-relevant 结构但无法完全弥补 interface loss。\\n3. **Training and Instruction Invariance**: VLA task-specific fine-tuning 和 instruction input 均不显著改变 LLM hidden state 中的 action-relevant 表征结构。image_mean 聚合下 training Δ=0.021，95% CI=[−0.031, +0.064]，p=0.20；last_preaction 下 Δ=0.008，95% CI=[−0.040, +0.056]，p=0.37。两个 CI 均包含 0。2×2 matrix（training × instruction）四格收敛于 0.48-0.50。\\n\\n## Paper 主数值基准（image_mean 聚合，公平对比）\\n\\n| Model / Condition | RSA (image_mean) | Notes |\\n|---|---|---|\\n| **SigLIP+Projector** | **0.615** | Smoking gun, LLM input |\\n| VLA trained with-inst | 0.501 | Peak L23 |\\n| VLA untrained with-inst | 0.485 | Peak L23 |\\n| VLA trained no-inst | — | Pending image_mean recompute |\\n| VLA untrained no-inst | — | Pending image_mean recompute |\\n| DINO-V2 | 0.388 | Vision-only baseline |\\n\\nlast_preaction 数值（trained 0.488, untrained 0.485）放 supplementary 作为 robustness check。\\n\\n## Story Spine\\n\\n- **Problem**: VLAs 通过 fine-tuning LLM on robot data 实现 impressive performance，但 action-relevant 表征从何而来？业界隐性假设 fine-tuning 注入 new representational knowledge，但无系统性验证。\\n- **Existing approaches & gaps**: Grant et al. 2026 从 behavioral level 发
…[truncated 3814 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-15T23:21:58.884186+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_analysis_no_inst_image_mean_rsa_20260515T231839",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_analysis_no_inst_image_mean_rsa_20260515T231839",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-15T23:21:59.235796+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_no_inst_image_mean_rsa_20260515T231839\", \"status\": \"running\", \"task_type\": \"analysis:no_inst_image_mean_rsa\", \"project\": \"vla-ssd\", \"started_at\": \"2026-05-15T23:18:40.030443+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ssh_execute\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_execute\", \"ssh_execute\"], \"last_text\": \"Still running (1m31s, 115% CPU). Let me check again shortly.\", \"turn_count\": 32}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 351
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-15T23:21:59.687848+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_code_plan_008_prep_20260515T231944",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_code_plan_008_prep_20260515T231944",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-15T23:22:00.089776+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_code_plan_008_prep_20260515T231944\", \"status\": \"running\", \"task_type\": \"code:plan_008_prep\", \"project\": \"vla-ssd\", \"started_at\": \"2026-05-15T23:19:44.427860+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\", \"ssh_read_only\"], \"last_text\": \"Let me check file sizes for timing estimation, and the extract_one_task function I missed (it was truncated).\", \"turn_count\": 17}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-15T23:22:00.193128+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__check_job_status",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__check_job_status",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-15T23:22:00.193647+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_probe_untrained",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-15T23:22:59.605602+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：**cuda:0, cuda:1** on westd-19183。绝对不用其他 GPU 编号
- 服务器 **westd-19183 无外网**：所有 HF/AutoProcessor 操作必须 `local_files_only=True`，禁止 `from_pretrained()` 不带此参数
- 大文件必须放 `/root/autodl-tmp/vla-ssd/`，根分区 ~30GB
- Untrained model = `from_config()` 重新初始化 LLM（6.74B random），**保留 SigLIP（0.80B frozen）**——不是全随机
- 分析 Worker **不得覆盖 registry spec 字段**（只能补充，不能改已有的 command/server 等）
- Paper 主文数值用 **image_mean 聚合**（SigLIP 0.615 vs VLA 0.501），last_preaction 放 supplementary
- Dream `dream_20260515T222933` pending——**等 Dream 回调再决定是否调 framing/plan**，不要提前改 paper_framing.md

### 2. 🖥️ 基础设施快照
- 服务器：**westd-19183**，2×RTX PRO 6000，工作目录 `/root/vla-ssd`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 激活命令：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型 checkpoint：`/root/autodl-tmp/vla-ssd/` 下（trained/untrained OpenVLA）
- 已提取特征：`/root/autodl-tmp/vla-ssd/results/` 下各子目录（rsa/, features/ 等）
- Per-layer curve 数据：`/root/autodl-tmp/vla-ssd/results/rsa/perlayer_degradation_curve.json`
- W&B：项目配置中查 wandb section
- 活跃进程：当前 0 个 GPU 训练进程（P0 全完成，P1 plan_003 已完成）
- Cron：reconcile 返回 0 个活跃 cron（全部已清理）

### 3. 📊 当前状态
**刚完成**：P0 全部 DONE + P1 plan_003 (per-layer degradation) DONE + p0_bootstrap_ci + p0_image_mean_rsa_verify。D028 确认 pivot 到 "Vision Encoder Dominance" framing。

**正在跑的 2 个 Worker**：
1. `worker_analysis_no_inst_image_mean_rsa_20260515T231839`（turn 32）— 计算 no-inst 条件的 image_mean RSA，补全 paper_framing.md 中 "Pending image_mean recompute" 的两格（trained no-inst / untrained no-inst）
2. `worker_code_plan_008_prep_20260515T231944`（turn 17）— 准备 plan_008 random instruction control 代码（P1，排除 trivial separability 攻击面 D024）

**等待中**：
- Dream `dream_20260515T222933` 回调 → 审稿模拟结果 → 决定是否调 framing
- 两个 Worker 回调
- Director 尚未批准 P1 实验 GPU 分配（plan_008 代码就绪后需 GPU 跑）

**Registry 总结**：36 实验，23 success / 7 negative / 0 failed / 6 killed。所有 P0 证据链完整。

### 4. 📋 待办（条件触发式）
- Dream 回调到达 → 读审稿报告 → 如果 borderline/accept 则保持 framing 推进写作；如果 reject 则产 Framing 调整提案给 Director
- `worker_analysis_no_inst_image_mean_rsa` 完成 → 更新 paper_framing.md 中 no-inst image_mean 数值 → 更新 registry → 刷新 report.md
- `worker_code_plan_008_prep` 完成 → 向 Director 请求批准 plan_008 GPU 提交（cuda:0 或 cuda:1，~2h）→ 批准后 submit_training_job
- plan_008 完成 → 更新 registry → 如果 PASS 则 Claim 3 random instruction control 证据到位 → 启动 Paper Agent Full Draft
- Paper Agent 启动前 → 确认 Dream 已分析 + 所有 P0/P1 证据在 registry → spawn paper writing workers
- plan_009 (CKA verification, P2, CPU-only) 和 plan_010 (LIBERO-Spatial, P2, 4h GPU) → 时间允许才做，不 blocking paper

### 5. 🎯 战略上下文
**核心结论链**：MVP-1 temporal distance → G2 FAIL → 多轮 pivot → D028 SigLIP-only smoking gun PASS → "Vision Encoder Dominance" framing 锁定。三个 Core Claims 全有 P0 证据支撑。

**D030 关键判断**：Dream 三档均低于 acceptance（best = borderline reject）。这意味着 framing 可能需要调整，或者 Dream 本身对这种 analysis paper 评估偏保守。**等 Dream 回调后仔细读报告再判断**，不要看到 "borderline reject" 就恐慌 pivot。

**最容易判断错的事**：
- paper_framing.md 中 no-inst 两格标 "Pending image_mean recompute"——Worker 正在算，**不要**用 last_preaction 数值填充主文
- D030 说 Dream 低于 acceptance，但这是模拟审稿，不是真实审稿。CoRL 是 robotics venue，对 analysis/understanding paper 可能比 Dream 更友好
- Claim 2 措辞已从 "LLM degrades" 精炼为 "token embedding interface introduces primary degradation, subsequent layers partially recover"（memory.md），paper 写作时用精炼版
- 6 个 killed 实验（mvp2_action_probe, lg_extract 系列, lg_shuffled_token_control）是早期被淘汰的路线，不需要关注

**时间线**：Abstract DDL May 26（11天），Paper DDL May 29（14天）。P1 完成预计 May 16-17，Paper Full Draft May 17-20，留 ~8 天 review iteration。节奏紧但可行。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:mvp_probe_untrained"
}
```

</details>

---
