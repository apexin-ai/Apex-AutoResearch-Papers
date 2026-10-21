# cron hook mvp controlb trained 20260516T023241 656735

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 2
- **Tool calls:** 27
- **Original source:** `logs/chats/archive/cron_hook_mvp_controlb_trained_20260516T023241_656735.jsonl`
- **Structured JSON:** [`7d61421d85fb97b2f53c.json`](../../sessions/7d/7d61421d85fb97b2f53c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-15T23:27:35.160325+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #5。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**cuda:0, cuda:1** on westd-19183（config.execution.gpu_ids）。其他 GPU 编号一律 push back Director
- **服务器无外网**：所有 HF 操作必须 `local_files_only=True`，不能在线下载模型/tokenizer
- Untrained model = `from_config()` 重新初始化 LLM（6.74B random），保留 SigLIP（0.80B frozen）。不要搞混 pretrained vs fine-tuned 对比
- Token 聚合：主文用 **image_mean**（公平对比），last_preaction 放 supplementary。paper_framing.md 已统一此口径
- **分析 Worker 不得覆盖 spec 字段**（registry 里的 command/server/gpu 等 provenance 信息）
- Dream `dream_20260515T222933` 还在 pending——**Dream 结果出来前不要启动 Paper Agent**，先分析审稿模拟报告

### 2. 🖥️ 基础设施快照
- **服务器**: westd-19183（2×RTX PRO 6000）
- **工作目录**: `/root/vla-ssd/`（代码），`/root/autodl-tmp/vla-ssd/`（大文件：features、results、checkpoints）
- **Python**: conda base，`/root/miniconda3/bin/python`。激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **镜像**: aml-train（先 `detect_image` 确认）
- **已提取 features 路径**: `/root/autodl-tmp/vla-ssd/features/`（trained/untrained × with-inst/no-inst × DINO，所有 P0 features 已就绪）
- **RSA 结果路径**: `/root/autodl-tmp/vla-ssd/results/rsa/`（perlayer_degradation_curve.json 等）
- **活跃进程**: 无 GPU 训练在跑（0/2 GPU 占用）。当前 3 个 Worker 都是 CPU 分析/代码准备任务
- **Cron**: reconcile 结果 0 个活跃 cron

### 3. 📊 当前状态
**刚做完**: P0 全部完成（7 probing × 2 benchmarks + SigLIP smoking gun + instruction ablation + 2×2 matrix + output head + bootstrap CI + image_mean verification + per-layer degradation）。paper_framing.md 和 experiment_plan.yaml 已写好，Dream 已提交。

**Registry 摘要**:
- PREPARING: `p0_functional_action_probe`, `p0_functional_action_delta_probe`（功能验证实验，等 Worker 结果确认是否需要 GPU）
- QUEUED/killed: `lg_output_head_analysis`, `lg_instruction_ablation`（旧版实验，已被新版替代，不需要重跑）
- DONE: 36 个实验（23 success / 7 negative / 6 killed）
- planned: plan_008（random instruction control，P1），plan_009（CKA，P2），plan_010（LIBERO-Spatial，P2）

**3 个 Running Workers**:
1. `worker_analysis_no_inst_image_mean_rsa_20260515T231839`（turn 33）— 计算 trained no-inst 和 untrained no-inst 的 image_mean RSA，填 paper_framing.md 表格空格
2. `worker_code_plan_008_prep_20260515T231944`（turn 10）— 准备 plan_008 random instruction control 的代码+dry-run
3. `worker_ssh_p0-functional-action-probe_20260515T232234`（turn 18）— P0 功能验证：在已有 features 上跑 action prediction probe，确认 probe 设计 sound

**等待中**:
- Dream `dream_20260515T222933` 回调 → 分析审稿模拟 → 决定是否调 framing
- 3 个 Worker 完成回调

### 4. 📋 待办（条件触发式）
- **Dream 回调到达** → 读 dream report → 如果 borderline-reject 以上则继续当前 framing；如果 reject 则产 Framing 调整提案给 Director
- **Worker no_inst_image_mean_rsa 完成** → 拿到 trained no-inst / untrained no-inst 的 image_mean RSA → 更新 paper_framing.md 表格 + registry
- **Worker plan_008_prep 完成** → 代码就绪 → 等 Director 批准 P1 实验后提交 plan_008（random instruction control，~2h GPU）
- **Worker p0-functional-action-probe 完成** → 确认 action probe 设计 sound → 更新 p0_functional_action_probe / p0_functional_action_delta_probe registry
- **Director 批准 P1** → 提交 plan_008（GPU，cuda:0）。plan_003 已完成，plan_009（CKA）是 CPU-only 可随时跑
- **所有 P1 完成 + Dream 通过** → 启动 Paper Agent（Full Draft 模式，CoRL 2026）

### 5. 🎯 战略上下文
**核心结论链**: MVP temporal distance FAIL (D007) → action prediction 也 FAIL (D022: Δρ=0.003) → 6 轮 probing 全部 trained≈untrained → D021 pivot Option B "Architecture Trumps Training" → instruction ablation FAIL 否证 Option B → D027 pivot 到 Option A2 "Vision Encoder Dominance" → **SigLIP smoking gun PASS (0.615 >> 0.488)** → 当前 framing 锁定。

**最容易判断错的事**:
1. **不要混淆 last_preaction 和 image_mean 数值**。主文用 image_mean（SigLIP 0.615 vs VLA 0.501），last_preaction（0.488）放 supplementary。paper_framing.md 已明确
2. **Dream 报告 D030 说三档均低于 acceptance**（best = borderline reject）。这不意味着放弃——Dream 是模拟，实际论文质量取决于写作和实验补充。但 Director 可能基于 Dream 结果调整策略
3. **lg_output_head_analysis / lg_instruction_ablation 是 QUEUED+killed 的旧实验**，已被 d021_ 版本替代。不要重新提交
4. **Per-layer degradation 是非单调的**——不要在论文中写 "progressive degradation"，正确说法是 "embedding interface bottleneck + partial recovery"
5. **CoRL DDL**: Abstract May 26（11天），Paper May 29（14天）。时间紧但充裕——P0 全完成，P1 只需 ~2h GPU，主要工作量在论文写作

## 项目硬约束 (memory.md 节选)

## 技术约束

- Untrained model: from_config() 重新初始化 LLM（6.74B random），保留 SigLIP（0.80B）
- D017: 统一用 LIBERO-10 fine-tuned checkpoint（LIBERO-Goal 是 OOD 测试）
- Token 聚合：Primary = last pre-action token
- 存储：根分区 ~30GB，大文件在 /root/autodl-tmp/vla-ssd/
- **分析 Worker 不得覆盖 spec 字段**
- **服务器无外网**：AutoProcessor/HF 操作必须 `local_files_only=True`
- **Instruction ablation bug**: `if args.task_instruction:` 对空字符串返回 False，已修复

## 可查的历史
前 22 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:mvp_controlb_trained",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-15T23:27:47.957647+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
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

_source line 3 · 2026-05-15T23:27:47.958090+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T23:27:51.069007+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "vla-ssd",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "vla-ssd",
    "limit": "0"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T23:27:51.521513+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T23:27:51.522810+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"p0_functional_action_delta_probe\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-15T23:21:52.667Z\", \"updated_at\": \"2026-05-15T23:22:00.278Z\", \"hypothesis\": \"P0 BLOCKING Functional Validation: Action-delta prediction (Δa = a_{t+1}-a_t) on SigLIP+projector output features. Removes autocorrelation. Compare with LLM best (L14, R²=0.059) and DINO (R²=0.060). Also tests image_mean aggregation.\"}, \"p0_functional_action_probe\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-15T23:21:52.011Z\", \"updated_at\": \"2026-05-15T23:21:58.413Z\", \"hypothesis\": \"P0 BLOCKING Functional Validation: Action prediction probe on SigLIP+projector output features. If projector R² ≥ LLM best layer (0.683) → smoking gun functional validation. If < LLM but > DINO (0.676) → partial. If ≤ DINO → degradation claim needs reeval. Also tests image_mean aggregation from LLM hidden states.\"}, \"p0_bootstrap_ci_training_effect\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T22:44:40.511Z\", \"updated_at\": \"2026-05-15T22:49:25.162Z\", \"hypothesis\": \"P0: Bootstrap CI on training effect (image_mean aggregation). Trained RSA=0.5014 vs untrained RSA=0.4847, Δ=+0.017. Task-level resampling bootstrap 95% CI. If CI excludes 0 → Claim 3 needs minor adjustment (\\\"minimal but detectable\\\"). If CI includes 0 → Claim 3 \\\"invariance\\\" holds.\", \"metrics\": {\"image_mean\": {\"delta\": 0.0206, \"ci_95\": [-0.0314, 0.0638], \"p_value\": 0.2, \"significant\": false}, \"last_preaction\": {\"delta\": 0.0076, \"ci_95\": [-0.0395, 0.0558], \"p_value\": 0.37, \"significant\": false}, \"n_bootstrap\": 10000, \"n_tasks\": 10, \"conclusion\": \"Both CIs include 0. Training effect not significant under task-level bootstrap. Claim 3 invariance holds.\", \"result_path\": \"/root/autodl-tmp/vla-ssd/results/rsa/bootstrap_training_effect.json\"}, \"conclusion\": \"success\"}, \"p0_image_mean_rsa_verify\": {\"status\": \"
…[truncated 31781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 453
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T23:27:51.974699+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T23:27:51.975084+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "report.md"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T23:27:51.975324+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T23:27:52.126165+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- lg_output_head_analysis: D021 Exp-2: Output Head Analysis. Compare trained vs untrained VLA weight differences across layers. If training does \\\"shallow adaptation\\\", output head weight diff >> middle layer weight diff. Explains \\\"representations unchanged but behavior improved\\\".（排队等待 GPU）\\n- lg_instruction_ablation: D021 Exp-1: Instruction Ablation. Extract LIBERO-Goal features with empty instruction (trained + untrained VLA), then run RSA. If instruction pathway is the source of action-relevant structure, RSA should collapse from ρ≈0.49 to <0.15. PASS: ρ<0.15; PARTIAL: 0.15<ρ<0.30; FAIL: ρ≥0.30.（排队等待 GPU）\\n- p0_functional_action_delta_probe（准备中）\\n- p0_functional_action_probe（准备中）\\n\\n## 近期结论\\n- **p0_bootstrap_ci_training_effect** (success): P0: Bootstrap CI on training effect (image_mean aggregation). Trained RSA=0.5014 vs untrained RSA=0.4847, Δ=+0.017. Task-level resampling bootstrap 95% CI. If CI excludes 0 → Claim 3 needs minor adjustment (\\\"minimal but detectable\\\"). If CI includes 0 → Claim 3 \\\"invariance\\\" holds.\\n- **p0_image_mean_rsa_verify** (success): P0 CRITICAL: Verify Claim 2 (LLM degrades action alignment 0.615→0.488) is not an aggregation artifact. SigLIP uses mean pooling, VLA used last_preaction. Re-run RSA with image_mean feature key for trained with-inst and untrained with-inst. If image_mean RSA ≈ 0.61 → Claim 2 is artifact. If ≈ 0.49 → Claim 2 holds.\\n- **plan_003_perlayer_degradation** (success): D028 plan_003: Per-layer RSA degradation curve. Track RSA from SigLIP+projector output (L0=0.615) through LLM layers 1-32 (~0.48). If monotonic decrease → LLM progressively degrades action alignment. If non-monotonic → some layers partially recover. Supports Claim 2 (LLM degrades acti
…[truncated 497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 151
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T23:27:52.126706+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\", \"content\": \"# vla-ssd — Research Dashboard\\n\\n> 最后更新: 2026-05-15 22:29 UTC | 更新原因: D028: complete_mvp 完成，进入 research 阶段。paper_framing.md + experiment_plan.yaml 已写，Dream 已提交\\n\\n## 核心方向\\n\\n**\\\"Vision Encoder Dominance: The Architectural Source of Action-Relevant Representations in VLAs\\\"**（D028 确定）\\n\\n三个 Core Claims（详见 paper_framing.md）：\\n1. Action-relevant 表征源自 frozen SigLIP vision encoder（RSA 0.615 >> VLA 0.488 >> DINO 0.388）\\n2. LLM processing 降低 action alignment（degrader, 非 passthrough）\\n3. Training 和 instruction 均不改变表征结构（2×2 matrix 收敛）\\n\\n## 当前进展\\n\\n- **阶段**: Research — post-MVP kickoff 完成，Dream 模拟中\\n- **MVP 结果**: 原假设（training 注入知识）系统性否定 → pivot 到 Vision Encoder Dominance\\n- **P0 实验全部完成**: 7 probing methods × 2 benchmarks + SigLIP-only RSA smoking gun + instruction ablation + 2×2 matrix + output head analysis\\n- **P1 待做**: per-layer RSA degradation curve（CPU）、random instruction control（2h GPU）\\n- **Dream**: `dream_20260515T222933` pending，等回调后决定是否调整 framing/plan\\n\\n## 近期任务\\n\\n- [ ] 等 Dream 完成 → 分析审稿报告 → 决定是否调整 framing/plan\\n- [ ] Dream 通过后批准 P1 实验（per-layer degradation curve + random instruction control）\\n- [ ] 启动 Paper Agent（Full Draft 模式，CoRL 2026）\\n- [ ] P1 实验结果补入论文\\n\\n## 时间线（CoRL 2026）\\n\\n| 里程碑 | 日期 | 剩余天数 |\\n|--------|------|---------|\\n| Abstract DDL | May 26 | 11 |\\n| Paper DDL | May 29 | 14 |\\n| Dream 完成 | May 15-16 | 0-1 |\\n| P1 实验完成 | May 16-17 | 1-2 |\\n| Paper Agent Full Draft | May 17-20 | 2-5 |\\n| Review + Iteration | May 20-28 | 5-13 |\\n\\n## GPU 预算\\n\\nwestd-19183: 2×RTX PRO 6000 | 当前 0/2 占用（等 Dream 结果后派 P1 实验）\\nP0 已用 ~13h GPU | P1 需 ~2h GPU + CPU | P2 需 ~4h（时间允许）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D030 | 2026-05-15 | D030: Dream 三档均低于 acceptance（best borderline rejec | d027_siglip_only_rsa, mvp2_action_trained, mvp2_action_
…[truncated 1387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T23:28:11.721027+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__update_registry",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__update_registry",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T23:28:11.771582+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T23:28:14.683099+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "vla-ssd",
  "status": "running",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "vla-ssd",
    "status": "running",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T23:28:14.934526+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_analysis_no_inst_image_mean_rsa_20260515T231839\", \"task_type\": \"analysis:no_inst_image_mean_rsa\", \"project\": \"vla-ssd\", \"status\": \"running\", \"started_at\": \"2026-05-15T23:18:40.030443+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_code_plan_008_prep_20260515T231944\", \"task_type\": \"code:plan_008_prep\", \"project\": \"vla-ssd\", \"status\": \"running\", \"started_at\": \"2026-05-15T23:19:44.427860+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_ssh_p0-functional-action-probe_20260515T232234\", \"task_type\": \"ssh:p0-functional-action-probe\", \"project\": \"vla-ssd\", \"status\": \"running\", \"started_at\": \"2026-05-15T23:22:34.210139+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_ssh_p0-functional-action-delta-probe_20260515T232553\", \"task_type\": \"ssh:p0-functional-action-delta-probe\", \"project\": \"vla-ssd\", \"status\": \"running\", \"started_at\": \"2026-05-15T23:25:54.005321+00:00\", \"ended_at\": null}], \"count\": 4}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T23:28:14.985191+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
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

_source line 17 · 2026-05-15T23:28:15.036756+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"vla-ssd\", \"section\": \"execution\", \"config\": {\"execution\": {\"gpu_ids\": [\"cuda:0\", \"cuda:1\"], \"project_path\": \"/root/vla-ssd\", \"servers\": [\"westd-19183\"]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T23:28:25.703308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/skills/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T23:28:25.704055+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/.claude/sessions/agent_17452cf3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T23:28:28.529994+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T23:28:28.580558+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T23:28:32.647615+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T23:28:32.698221+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T23:28:54.826614+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 分配 2 / 实际跑 0（等 Dream 回调后派 P1） | Worker 池 4 (GPU 0 / CPU 4)\n\n**Session #5 启动，状态同步完成。**\n\n当前活跃 Worker（4 个 CPU 任务）：\n1. `worker_analysis_no_inst_image_mean_rsa` — 计算 trained/untrained no-inst image_mean RSA，填 paper_framing 表格\n2. `worker_code_plan_008_prep` — plan_008 random instruction control 代码 + dry-run\n3. `worker_ssh_p0-functional-action-probe` — P0 功能验证：action prediction probe on SigLIP+projector features\n4. `worker_ssh_p0-functional-action-delta-probe` — P0 功能验证：action-delta probe\n\n等待中：\n- **Dream `dream_20260515T222933`** 回调未到。Dream 结果决定是否调 framing 和启动 Paper Agent\n- 4 个 Worker 完成回调\n\nGPU 空闲原因：P1 实验（plan_008 random instruction control, ~2h GPU）等 Dream 通过后提交。plan_009 (CKA) 是 P2 CPU-only，如 Director 批准可现在跑。\n\n无阻塞项，等回调中。",
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 分配 2 / 实际跑 0（等 Dream 回调后派 P1） | Worker 池 4 (GPU 0 / CPU 4)\n\n**Session #5 启动，状态同步完成。**\n\n当前活跃 Worker（4 个 CPU 任务）：\n1. `worker_analysis_no_inst_image_mean_rsa` — 计算 trained/untrained no-inst image_mean RSA，填 paper_framing 表格\n2. `worker_code_plan_008_prep` — plan_008 random instruction control 代码 + dry-run\n3. `worker_ssh_p0-functional-action-probe` — P0 功能验证：action prediction probe on SigLIP+projector features\n4. `worker_ssh_p0-functional-action-delta-probe` — P0 功能验证：action-delta probe\n\n等待中：\n- **Dream `dream_20260515T222933`** 回调未到。Dream 结果决定是否调 framing 和启动 Paper Agent\n- 4 个 Worker 完成回调\n\nGPU 空闲原因：P1 实验（plan_008 random instruction control, ~2h GPU）等 Dream 通过后提交。plan_009 (CKA) 是 P2 CPU-only，如 Director 批准可现在跑。\n\n无阻塞项，等回调中。",
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T23:28:58.648145+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 3821
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T23:29:03.777279+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T23:29:03.879202+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T23:29:15.070652+00:00_

Session #5 初始化完成。

**当前状态**：
- 4 个 CPU Worker 在跑（RSA 分析 / plan_008 代码 / action probe / delta probe）
- Dream `dream_20260515T222933` 待回调
- GPU 0/2 占用（等 Dream 通过后提交 P1）
- Director 已收到状态汇报

等待 Worker 完成回调和 Dream 结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:mvp_controlb_trained"
}
```

</details>

---

## Round 2

30 recorded events

### User

_source line 29 · 2026-05-16T02:30:58.771027+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T02:31:09.409729+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
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

_source line 31 · 2026-05-16T02:31:09.410182+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T02:31:12.829675+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
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

_source line 33 · 2026-05-16T02:31:12.830071+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T02:31:13.384277+00:00_

Error: result (82,979 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-17452cf3/6f9660bb-47ce-4218-8558-0adb532f7ed4/tool-results/mcp-agent-ml-research-read_registry-1778898673317.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-17452cf3/6f9660bb-47ce-4218-8558-0adb532f7ed4/tool-results/mcp-agent-ml-research-read_registry-1778898673317.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 554
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-16T02:31:13.838290+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 1008
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-16T02:31:13.889024+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
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

_source line 37 · 2026-05-16T02:31:14.291058+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **unified_action_probe** (success): Unified hyperparameter action probe (50ep/patience5/seed42) across all vision encoders on LIBERO-Goal. Resolves cross-experiment R² incomparability caused by differing probe configs. Tests geometric-functional dissociation: does VL pretraining RSA advantage translate to R² advantage?\\n- **plan_012_clip_vit_control** (success): —\\n  [rsa_clip_results](/api/workspace-files/projects/vla-ssd/artifacts/plan_012_clip_vit_control/data/rsa_clip_results.txt) | [action_probe_clip_results](/api/workspace-files/projects/vla-ssd/artifacts/plan_012_clip_vit_control/data/action_probe_clip_summary.txt) | [unified_action_probe_results](/api/workspace-files/projects/vla-ssd/artifacts/plan_012_clip_vit_control/data/unified_action_probe.py)\\n- **lg_instruction_ablation** (killed): D021 Exp-1: Instruction Ablation. Extract LIBERO-Goal features with empty instruction (trained + untrained VLA), then run RSA. If instruction pathway is the source of action-relevant structure, RSA should collapse from ρ≈0.49 to <0.15. PASS: ρ<0.15; PARTIAL: 0.15<ρ<0.30; FAIL: ρ≥0.30.\\n\\n## 趋势\\n成功 31 / 负向 7 / 失败 0 / 共 46\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-19183: 无 GPU 信息\\n\\n## 告警\\n- mvp2_action_probe: 已被终止 — unknown\\n- lg_extract_trained_r2: 已被终止 — unknown\\n- lg_extract_untrained_r2: 已被终止 — unknown\\n- lg_extract_trained_r1: 已被终止 — unknown\\n- lg_extract_untrained_r1: 已被终止 — unknown\\n- lg_shuffled_token_control: 已被终止 — unknown\\n- lg_instruction_ablation: 已被终止 — unknown\\n- lg_output_head_analysis: 已被终止 — unknown\\n\", \"total_chars\": 1621, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T02:31:14.291481+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-16T02:31:14.793184+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\", \"content\": \"# vla-ssd — Research Dashboard\\n\\n> 最后更新: 2026-05-16 00:14 UTC | 更新原因: Sync with D033/D034, CKA results, plan_008 running, updated Claims\\n\\n## 核心方向\\nVLA 中 action-relevant 表征的来源与 LLM 的 redistribution 机制。三层发现：(1) Vision encoder 是 action info 的通用源头，VL pretraining 赋予 geometric alignment 而非额外 predictive content；(2) LLM 降解分布式 image token 几何结构（RSA）但保留全局结构（CKA），通过训练依赖的 attention 将信号 concentrate 到 readout token；(3) Training 教会 routing（readout concentration），而非 creating new knowledge（distributed structure invariant）。详见 paper_framing.md。\\n\\n## 当前阶段\\n**Research phase, post-D034**。三条 Claim 完整成型，所有 P0 实验完成。等待：(1) untrained vs trained last_preaction bootstrap CI（已派 Agent）；(2) plan_008 random instruction control（RUNNING）。两者完成后 re-dream 验证新 framing，达标则启动 Paper Agent。\\n\\n## 已完成核心实验\\n- ✅ plan_001-007: RSA 组件分解 + 2×2 matrix + per-layer curve + instruction ablation\\n- ✅ plan_011: Functional action probe — Proj R²=0.706 > LLM img_mean 0.683 (p=0.001); readout 0.731 > Proj (p=0.001)\\n- ✅ plan_009: CKA verification — ordering reversal vs RSA (partial). RSA-CKA dissociation 成为新 finding\\n- ✅ D033: DINO R²=0.712 ≈ Projector 0.706 (p=0.22) — geometric-functional dissociation\\n- ✅ D034: Untrained readout R²=0.686 < projector 0.706 — redistribution is training-dependent\\n- ✅ Aggregation robustness: image_mean RSA 0.501 vs SigLIP 0.615, gap=0.114\\n- ✅ Bootstrap CI: training effect on image_mean CI includes 0, distributed structure invariant\\n\\n## 近期任务\\n- [ ] Untrained vs trained last_preaction bootstrap CI（Agent 已派，分钟级）\\n- [ ] plan_008 random instruction control 结果分析（RUNNING，等完成）\\n- [ ] Re-dream with updated framing（上述两项完成后立即触发）\\n- [ ] Paper Agent Full Draft（re-dream 达标后启动）\\n- [ ] plan_012 CLIP-ViT control（P1，Paper Agent 启动后并行）\\n\\n## GPU 预算\\nwestd-19183: 2× GPU（plan_008 占用中）\\n剩余预算: ~7 GPU·h\\n\\n## 关键里程碑\\n| 日期 | 事件 |\\n|
…[truncated 1853 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 501
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T02:31:14.793577+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "memory.md"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T02:31:15.245327+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/memory.md\", \"content\": \"# VLA-SSD Project Memory\\n\\n## ⚠️ 统一超参 Action Probe 修正（2026-05-16，替代之前不一致的结果）\\n\\n**之前 CLIP probe 用了 100ep/patience10，原始 probe 用 50ep/patience5，导致 R² 不可比（同一 DINO 数据出现 0.712 和 0.814）。已用统一超参重跑全部 vision encoder。**\\n\\n统一超参 (50ep/patience5/lr1e-3/hidden256/seed42, MLP input→256→7, predict a_{t+1}):\\n\\n| Model | mean_R² | overall_R² | vs Projector |\\n|-------|---------|-----------|-------------|\\n| VLA last_preaction L19 | **0.671** | 0.723 | +0.041, p=0.002 |\\n| DINO cls | 0.634 | 0.701 | ≈ (p=0.557) |\\n| SigLIP projector | 0.630 | 0.699 | — |\\n| VLA image_mean L19 | 0.599 | 0.677 | -0.031, p<0.001 |\\n| CLIP cls | 0.587 | 0.660 | -0.043, p<0.001 |\\n\\n**Geometric-Functional Dissociation（修正版，更极端）：**\\n\\n| Model | RSA (geometry) | R² (function) | 方向 |\\n|-------|---------------|---------------|------|\\n| CLIP | 0.557 (高) | 0.587 (最低) | **反向** |\\n| DINO | 0.388 (低) | 0.634 (高) | **反向** |\\n| Projector | 0.615 (最高) | 0.630 (≈DINO) | 持平 |\\n\\n**修正后结论**：\\n- VL pretraining (CLIP) 给了更高 geometric alignment (RSA=0.557>>0.388)，但 predictive capacity 反而更低 (R²=0.587<0.634)\\n- Geometry 和 function 是可分离的两个维度——这是比\\\"VL adds geometry not content\\\"更强的 finding\\n- Projector fine-tuning 恢复到 DINO 级别的 functional capacity (0.630≈0.634)\\n- Redistribution 确认：last_preaction > all (p=0.002)\\n\\n**论文影响**：Claim 1 不能说\\\"VL pretraining is better\\\"，而是\\\"VL pretraining reorganizes representations geometrically without improving—and potentially reducing—functional prediction capacity\\\"\\n\\n## CLIP ViT-L/14 RSA 确认 VL Pretraining 通用性（2026-05-16，plan_012 = success）\\n\\n**CLIP RSA=0.557，确认 action-relevant structure 是 VL pretraining 的通用产物，非 SigLIP 独有。**\\n\\n| Model | Peak RSA | CI95 |\\n|-------|---------|------|\\n| SigLIP + projector | 0.615 | [0.526, 0.695] |\\n| CLIP ViT-L/14 | 0.557 | [0.442, 0.660] |\\n| SigLIP only (LLM hidde
…[truncated 3722 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 451
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-16T02:31:15.245857+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
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

_source line 43 · 2026-05-16T02:31:15.397469+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_ssh_patch-mean-probe_20260516T022703\", \"task_type\": \"ssh:patch-mean-probe\", \"project\": \"vla-ssd\", \"status\": \"running\", \"started_at\": \"2026-05-16T02:27:04.067388+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-16T02:31:15.397897+00:00_

called mcp__agent-ml-research__load_project_config

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config</summary>

```json
{
  "project_name": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__load_project_config",
  "tool_args": {
    "project_name": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-16T02:31:15.450115+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"vla-ssd\", \"config\": {\"execution\": {\"gpu_ids\": [\"cuda:0\", \"cuda:1\"], \"project_path\": \"/root/vla-ssd\", \"servers\": [\"westd-19183\"]}, \"feishu\": {\"chat_id\": \"oc_a1d032cbe70bdd2058438e67e0d57613\", \"operational_chat_id\": \"oc_9e9aef1687e6abd097aa0edaf0551ee3\", \"submission_chat_id\": \"oc_554a5023cde4d603635cf97e6ab8151a\"}, \"project\": {\"created_at\": \"2026-05-15T04:32:26.871Z\", \"description\": \"VLA-SSD: Do VLAs Know Which Demonstrations Are Good? Self-Referential Quality Scoring from Pretrained Representations\", \"name\": \"vla-ssd\", \"phase\": \"research\", \"source_idea_id\": \"idea_004\"}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-16T02:31:19.418065+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
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

_source line 47 · 2026-05-16T02:31:19.469827+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-16T02:31:31.791135+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-17452cf3/6f9660bb-47ce-4218-8558-0adb532f7ed4/tool-results/mcp-agent-ml-research-read_registry-1778898673317.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor e in exps:\n    eid = e.get('exp_id','?')\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','')\n    hyp = e.get('hypothesis','')[:80] if e.get('hypothesis') else ''\n    print(f'{eid} | {status} | {conclusion} | {hyp}')\n\"",
  "description": "Parse registry experiments summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-17452cf3/6f9660bb-47ce-4218-8558-0adb532f7ed4/tool-results/mcp-agent-ml-research-read_registry-1778898673317.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor e in exps:\n    eid = e.get('exp_id','?')\n    status = e.get('status','?')\n    conclusion = e.get('conclusion','')\n    hyp = e.get('hypothesis','')[:80] if e.get('hypothesis') else ''\n    print(f'{eid} | {status} | {conclusion} | {hyp}')\n\"",
    "description": "Parse registry experiments summary"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-16T02:31:32.353389+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Bash",
  "elapsed_ms": 562
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-16T02:31:32.554628+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
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

_source line 51 · 2026-05-16T02:31:32.555087+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-3/proje…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-16T02:31:37.777016+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-17452cf3/6f9660bb-47ce-4218-8558-0adb532f7ed4/tool-results/mcp-agent-ml-research-read_registry-1778898673317.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Check structure\nif isinstance(exps, dict):\n    for eid, e in exps.items():\n        status = e.get('status','?') if isinstance(e, dict) else '?'\n        conclusion = e.get('conclusion','') if isinstance(e, dict) else ''\n        print(f'{eid} | {status} | {conclusion}')\nelif isinstance(exps, list):\n    print(type(exps[0]))\n    print(exps[0][:200] if isinstance(exps[0], str) else str(exps[0])[:200])\n\"",
  "description": "Parse registry structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-17452cf3/6f9660bb-47ce-4218-8558-0adb532f7ed4/tool-results/mcp-agent-ml-research-read_registry-1778898673317.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# Check structure\nif isinstance(exps, dict):\n    for eid, e in exps.items():\n        status = e.get('status','?') if isinstance(e, dict) else '?'\n        conclusion = e.get('conclusion','') if isinstance(e, dict) else ''\n        print(f'{eid} | {status} | {conclusion}')\nelif isinstance(exps, list):\n    print(type(exps[0]))\n    print(exps[0][:200] if isinstance(exps[0], str) else str(exps[0])[:200])\n\"",
    "description": "Parse registry structure"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-16T02:31:37.877978+00:00_

unified_action_probe | DONE | success
plan_012_clip_vit_control | DONE | success
lg_instruction_ablation | DONE | killed
lg_output_head_analysis | DONE | killed
plan_008_random_inst_control | DONE | success
untrained_last_preaction_probe | DONE | success
plan_009_cka_verification | DONE | success
p0_functional_probe_v2 | DONE | success
p0_functional_action_probe | DONE | success
p0_functional_action_delta_probe | DONE | success
p0_bootstrap_ci_training_effect | DONE | success
p0_image_mean_rsa_verify | DONE | success
plan_003_perlayer_degradation | DONE | success
d027_siglip_only_rsa | DONE | success
d027_trained_no_inst_rsa | DONE | success
d021_instruction_ablation | DONE | negative
d021_output_head_analysis | DONE | negative
lg_rsa_analysis | DONE | negative
lg_shuffled_token_control | DONE | killed
lg_pca1024_linear_pertimestep | DONE | negative
lg_gc_trained_frame0 | DONE | success
lg_gc_untrained | DONE | negative
lg_gc_dino | DONE | success
lg_dino_extract | DONE | success
lg_gc_trained | DONE | success
lg_extract_untrained | DONE | success
lg_extract_trained | DONE | success
mvp2_action_probe | DONE | killed
lg_extract_untrained_r2 | DONE | killed
lg_extract_trained_r2 | DONE | killed
lg_extract_untrained_r1 | DONE | killed
lg_extract_trained_r1 | DONE | killed
mvp2_delta_dino | DONE | success
mvp2_delta_untrained | DONE | success
mvp2_delta_trained | DONE | success
mvp2_action_dino | DONE | success
mvp2_action_untrained | DONE | success
mvp2_action_trained | DONE | success
dinov2_baseline | DONE | success
mvp_controlb_untrained | DONE | success
mvp_controlb_trained | DONE | success
mvp_001 | DONE | negative
mvp_probe_untrained | DONE | success
mvp_probe_trained | DONE | negative
openvla-untrained-extract | DONE | success
openvla-trained-extract | DONE | success

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-16T02:31:41.949072+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "paper_framing.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "paper_framing.md",
    "max_chars": "6000"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-16T02:31:42.754014+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/paper_framing.md\", \"content\": \"# Paper Framing — vla-ssd\\n\\n## Target Venue\\n- Primary: CoRL 2026\\n- Deadline: Abstract May 26, Paper May 29\\n- Format: 8 pages + references\\n\\n## Core Claims (3 条)\\n\\n1. **Vision Encoder Dominance + Geometric-Functional Dissociation**: VLA 中 action-relevant 表征结构由 frozen vision encoder 决定。RSA geometric alignment: SigLIP (0.615) > CLIP (0.557) >> DINO (0.388)——VL pretrained encoders 显著优于 vision-only。但 functional capacity (R²) 方向相反: DINO (0.634) ≈ Projector (0.630) > CLIP (0.587)。**Geometric alignment 和 predictive capacity 是可分离的独立维度**。VL pretraining 提供 geometric alignment（表征结构匹配 action 空间），不增加甚至略降低 functional capacity。\\n2. **LLM Redistributes Action-Relevant Structure (Training-Dependent)**: LLM 降解 distributed image token 的 **geometric alignment**（RSA: 0.615→0.501）和 functional capacity（R²: 0.630→0.599, p<0.001），但 global structure 保留（CKA 单调上升）。**训练后** LLM 学会将 action 信号 concentrate 到 readout token（trained R²=0.671 > projector 0.630, p=0.002），但 **untrained LLM 做不到**（untrained readout best=0.686 < projector）。Readout concentration 是 learned behavior，不是架构固有属性。\\n3. **Training: Routing Without Creating**: VLA fine-tuning 不改变 distributed representation structure（image_mean RSA: trained 0.501 ≈ untrained 0.485, bootstrap CI includes 0, p=0.20），但提升 readout concentration（trained last_preaction 0.731 >> untrained 0.686，Δ=0.045, bootstrap CI=[0.032, 0.058], p<0.0001）。Instruction input 对两者均无影响。综合解读：**Training 的贡献是学习信息路由（routing），而非注入新的 action knowledge（creating）**。\\n\\n## Paper 主数值基准（image_mean 聚合，公平对比）\\n\\n| Model / Condition | RSA (image_mean) | Notes |\\n|---|---|---|\\n| **SigLIP+Projector** | **0.615** | Smoking gun, LLM input |\\n| VLA trained with-inst | 0.501 | Peak L23 |\\n| VLA untrained with-inst | 0.485 | Peak L23 |\\n| VLA trained no-inst | 0.501 | Peak L23, identical to with-inst |\\n| VLA untrained no-
…[truncated 4474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 804
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-16T02:31:42.906031+00:00_

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
  "session": "cron:hook:mvp_controlb_trained",
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

_source line 57 · 2026-05-16T02:31:42.906447+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:mvp_controlb_trained",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-16T02:32:41.655045+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 `cuda:0` 和 `cuda:1`（westd-19183）
- 服务器 **无外网**：所有 HF/AutoProcessor 操作必须 `local_files_only=True`，不能 pip install / git clone
- westd 是 **SeetaCloud**（非 AutoDL），不适用 `network_turbo` / ModelScope 等 AutoDL 方案
- 统一 action probe 超参已锁定：50ep/patience5/lr1e-3/hidden256/seed42, MLP input→256→7, predict a_{t+1}。任何新 probe 必须用此配置，否则 R² 不可比（之前 CLIP 100ep 导致虚高 0.814 vs 真实 0.587 的事故）
- 论文数值只能来自 registry，不能凭记忆编造
- CoRL Abstract DDL = 5/26，Paper DDL = 5/29，**不允许讨论降级 venue**

### 2. 🖥️ 基础设施快照
- **服务器**：westd-19183，工作目录 `/root/vla-ssd`
- **Python**：`/root/miniconda3/bin/python`（conda base env，不是 venv）
- **模型 checkpoint**：`/root/autodl-tmp/vla-ssd/`（大文件存储）
- **W&B**：项目中无 W&B 训练（全部是离线 probe/RSA 分析脚本）
- **HF cache**：服务器无网，模型已预下载到本地
- **活跃进程**：无 RUNNING 实验，0 active crons
- **活跃 Worker**：`worker_ssh_patch-mean-probe_20260516T022703`（status=running，任务 ssh:patch-mean-probe）——可能正在修补 image_mean probe 相关代码，接手后检查其完成状态

### 3. 📊 当前状态
**所有 45 个实验均 DONE**（31 success / 7 negative / 7 killed）。无 RUNNING/PREPARING 实验，0 active crons。

刚完成的关键里程碑：
- `unified_action_probe`（success）：统一超参重跑所有 vision encoder，修正了之前 CLIP R² 虚高问题。发现 geometric-functional dissociation 比预期更极端
- `plan_012_clip_vit_control`（success）：CLIP ViT-L/14 RSA=0.557 确认 VL pretraining 通用性
- `plan_008_random_inst_control`（success）：四种 instruction 条件 RSA 完全收敛，instruction content invariance 证据闭合
- `plan_009_cka_verification`（success）：CKA 部分验证 RSA，发现指标依赖性

**paper_framing.md 三条 Claim 已定稿**，所有 P0 实验证据链完整。

等待中：
- 1 个 running worker（patch-mean-probe）未回调
- ROADMAP 说"re-dream + Paper Agent Full Draft"是下一步，D035 决策已批准并行启动

### 4. 📋 待办（条件触发式）
- `worker_ssh_patch-mean-probe` 回调完成 → 检查产出，更新 registry/report.md
- 上述 worker 完成 → 立即启动 Paper Agent Full Draft（D035 已批准，不需要额外审批）
- Paper Agent 启动 → 按 paper_framing.md 三条 Claim + Story Spine 写作，同时可并行 plan_010 LIBERO-Spatial（P2 优先级）
- 如需 re-dream → dream 验证新 framing 是否达 acceptance threshold（D030 记录上次 dream 结果为 borderline reject）
- Paper 写作中发现数值空缺 → 查 registry 补充，不要编造

### 5. 🎯 战略上下文
**核心结论链**：D027 Instruction Ablation FAIL → Option A2 锁定 → D028 SigLIP smoking gun PASS → D029 聚合伪影排除 → D031 Redistribution framing → D032 Option A 确认 → D033 Geometric-Functional Dissociation → D034 Training-Dependent Redistribution → D036 统一超参修正（dissociation 更极端）

**三条 Claim 总结**：
1. Vision encoder 是 action info 源头，但 geometric alignment (RSA) 与 predictive capacity (R²) **方向相反**——VL pretraining 给几何不给功能
2. LLM 降解分布式表征但通过 training-dependent attention 将信号 concentrate 到 readout token
3. Training = routing（readout concentration），not creating（distributed structure invariant）

**最容易判断错的事**：
- **不要混淆两组 probe 数据**：5-model 对比用 `unified_action_probe` 数字；trained/untrained 对比用 `p0_functional_probe_v2` 数字。两组绝对值不同（超参/数据处理差异），但组内排序一致
- **聚合口径依赖**：image_mean 下 Projector > LLM；last_preaction 下 LLM > Projector。主文用 image_mean（公平），last_preaction 放 supplementary。必须在论文中讨论
- **D030 dream 结果是 borderline reject**——re-dream 时注意新 framing（geometric-functional dissociation）是否足够提升 novelty score
- **CLIP R² < DINO 是反直觉但真实的**——统一超参后确认，不要怀疑数据
- Projector vs trained CKA gap 被压缩（RSA 下显著，CKA 下 ≈），论文措辞不能说 projector "dominance" 是 metric-independent 的
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:mvp_controlb_trained"
}
```

</details>

---
