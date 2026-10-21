# cron hook sta phase1 exec sta r2 20260514T053424 355033

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 2
- **Tool calls:** 28
- **Original source:** `logs/chats/archive/cron_hook_sta-phase1-exec-sta-r2_20260514T053424_355033.jsonl`
- **Structured JSON:** [`6e9b3cd8ed478875b066.json`](../../sessions/6e/6e9b3cd8ed478875b066.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

37 recorded events

### User

_source line 1 · 2026-05-14T02:11:08.160915+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #3。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**只能用 westd-39279 的 cuda:0 和 cuda:1**（config `gpu_ids`）
- **C001**: 所有 plan001/plan013 实验统一用 `train_500_seed42.jsonl`，不是 `proofwriter_fol_500.jsonl`
- **C002**: 每次 submit_training_job 后必须 `nvidia-smi` 验证只占目标 GPU（plan013 GPU overflow 事故教训）
- **C003**: 训练必须 `log_completions=False` + `save_total_limit=1`，output_dir 放 `/root/autodl-tmp/outputs/`（250GB 系统盘被 completions parquet 撑满过）
- submit_training_job command 格式：`bash -c "export CUDA_VISIBLE_DEVICES=N && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 ..."`。**必须 export**，inline 赋值子进程看不到
- plan013 random_reward 模式下 `isr_mean` 字段恒为 0（`sta_reward=0`），随机值在 `random_reward` 字段。分析时忽略 isr_mean
- **旧凸组合公式已废弃**（D010）：r = α·r_exec + β·r_exec·ISR, α+β=1 → ISR<1 永远是 penalty。新公式 r = r_exec · (1 + β·ISR)

### 2. 🖥️ 基础设施快照
- **服务器**: westd-39279，2× RTX PRO 6000 Blackwell 94GB
- **工作目录**: `/root/solver-trace-ablation/`
- **Python**: `/root/miniconda3/bin/python`（conda base，不是 venv）
- **激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **CUDA**: 12.8, PyTorch 2.10.0+cu128, 镜像 aml-train
- **模型**: Qwen3-4B（ModelScope 下载，7.6GB）
- **数据**: `data/train_500_seed42.jsonl`（500条 FOLIO FOL），`data/proofwriter_fol_100.jsonl`（100条 eval）
- **Outputs**: `/root/autodl-tmp/outputs/` (checkpoints + reward_log)
- **Solvers**: Prover9 (LADR 源码编译), SWI-Prolog 8.4.2, Z3 4.16.0.0
- **活跃进程**:
  - plan013-random-reward-s42-r4: PID 136261, cuda:0, tmux session 有 cron 监控
  - plan001-exec-only-s43-r4: PID 136339, cuda:1, tmux session 有 cron 监控
- **Prolog STA**: 代码就绪（`src/sta/prolog_reward.py`），dry-run 通过，plan006 可直接启动

### 3. 📊 当前状态
**刚完成**: 处理了 plan001-exec-only-s43-r3 和 plan013-random-reward-s42-r3 的磁盘满崩溃（清理 171GB），修复 `log_completions=False`，重新提交为 r4。

**RUNNING 实验**:
- `plan001-exec-only-s43-r4` (cuda:1): exec-only seed=43 第二个种子复现，预期 ~70min
- `plan013-random-reward-s42-r4` (cuda:0): random reward baseline，隔离 ISR-specific signal vs 多目标正则化

**RUNNING Workers**:
- `worker_research_plan014-downstream-design`: 调研下游验证任务设计（打破 ISR circularity）
- `worker_code_plan002-additive-bonus-reward`: 编写新 additive bonus reward 代码（r = r_exec · (1 + β·ISR)）

**已完成关键实验**:
- plan001-exec-only-s42-r2: **SUCCESS**, last100 prove_rate=0.865, ISR=0.8612（exec-only baseline 锚定）
- plan005-sta-low-s42: **NEGATIVE**, last100 prove_rate=0.7725 (vs exec-only 0.865 ↓)，ISR/PR=0.298。确认凸组合公式是 penalty → 触发 D010 公式转向
- plan003-eval-exec-only-r5: **SUCCESS**, held-out proved_only_isr=0.6423，确认 ISR organic 提升

### 4. 📋 待办（条件触发式）
- plan001-exec-only-s43-r4 cron 回调 → 分析 metrics，与 s42 (prove_rate=0.865) 对比 → 一致则 exec-only baseline 2-seed 锚定完成
- plan013-random-reward-s42-r4 cron 回调 → 分析 prove_rate + random_reward 字段，与 plan001 对比 → 若 prove_rate ≈ exec-only 则 "ISR-specific > random" claim 成立，若 prove_rate ↓ 则多目标正则化本身就有 penalty effect
- worker_code_plan002-additive-bonus-reward 完成 → review 代码 → 提交 plan002 (additive bonus β=0.3) 到 cuda:0（等 plan013 完成后）
- worker_research_plan014-downstream-design 完成 → 整合调研结果 → 设计 plan014 downstream validation 实验
- plan001 + plan013 都完成后 → 两张 GPU 空闲 → 立即启动 plan002 (additive bonus, cuda:0) + plan001 seed=44 第三个种子 (cuda:1)
- 3-seed exec-only baseline 完成后 → 启动 plan006 Prolog（代码已就绪）

### 5. 🎯 战略上下文
**项目核心结论链**:
- D003: binary ISR 无效 → 必须用 continuous ISR
- D007/D008: exec-only ISR 提升是 organic 的，50/50 STA 是 penalty effect (Interpretation B confirmed)
- D010: 凸组合公式废弃 → additive bonus r = r_exec · (1 + β·ISR)
- D011: Narrative A+C 批准 — STA as diagnostic metric 为主线

**论文 story**: "STA detects hacking" 已降级为观察性表述 → 转为 "STA as principled structural metric + proper integration (additive bonus)"。plan002 是验证新 story 的关键实验。

**DDL**: 2026-05-25（剩 11 天）

**易错点**:
- 不要用旧凸组合公式提交 plan002，必须用 additive bonus（Worker 正在写代码）
- plan013 分析时不要看 `isr_mean`（恒为 0），要看 `random_reward` 字段
- exec-only baseline 目前只有 1 个成功种子 (s42)，s43 正在跑，s44 还没开始 → 3-seed 尚未完成
- Dream 审稿指出 5 个结构性弱点：(1) related work 不足 (2) RIP framing 过度 (3) ISR circularity (4) single-seed (5) ISR sparsity。plan013 解决 #3 partial，plan014 解决 #3 full，3-seed 解决 #4
- `reward_log.jsonl` 多轮 run 会追加到同一文件 → 分析时必须按 timestamp 过滤或使用独立 output_dir

## 项目硬约束 (memory.md 节选)

## 环境信息 (2026-05-13)

### westd-39279 服务器
- **GPU**: 2× RTX PRO 6000 Blackwell, 94GB VRAM 每张
- **CUDA**: 12.8, PyTorch 2.10.0+cu128
- **镜像**: aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **ML 栈**: transformers/trl/vllm/accelerate 全部预装
- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2, Z3 4.16.0.0
- **模型**: Qwen3-4B 已下载（7.6GB，通过 ModelScope）
- **代码路径**: `/root/solver-trace-ablation/`
- **磁盘**: 系统盘 250GB，大文件（outputs/checkpoints）必须放 `/root/autodl-tmp/`

### 决策记录
- Qwen3-4B 用 ModelScope 下载（HuggingFace 直连可能慢）
- Prover9 从 LADR 源码编译（apt 无包）
- 94GB VRAM 单卡跑 Qwen3-4B 完全无压力

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
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T02:11:20.211933+00:00_

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
  "session": "cron:hook:sta-phase1-exec-sta-r2",
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

_source line 3 · 2026-05-14T02:11:20.212851+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T02:11:23.532965+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "solver-trace-ablation",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "solver-trace-ablation",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T02:11:23.533429+00:00_

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
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T02:11:24.037220+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan005-sta-low-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:20:47.812Z\", \"updated_at\": \"2026-05-14T01:55:26.234Z\", \"spec\": {\"model_name\": \"Qwen3-4B\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:55:02.341Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:55:06.559440+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan005_sta_low_s42/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan005_sta_low_s42/reward_log.jsonl\", \"completed_at\": \"2026-05-13T23:59:25.396Z\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 71, \"parse_rate\": 1, \"overall_prove_rate\": 0.5657, \"overall_isr\": 0.1682, \"last50_prove_rate\": 0.77, \"last50_isr\": 0.2559, \"last100_prove_rate\": 0.7725, \"last100_isr\": 0.2299, \"last100_loss\": 0.022752, \"overall_loss\": 0.017296, \"last100_isr_pr_ratio\": 0.298, \"last100_isr_lt_pr_count\": \"99/100\", \"first_rolling10_pr_ge_0.8\": 178, \"first_rolling10_pr_ge_0.9\": 439, \"max_rolling10_pr\": 0.9375, \"max_rolling10_isr\": 0.3282, \"windowed\": {\"1-50\": {\"pr\": 0.1775, \"isr\": 0.0906}, \"51-100\": {\"pr\": 0.1775, \"isr\": 0.0835}, \"101-200\": {\"pr\": 0.5062, \"isr\": 0.1463}, \"201-300\": {\"pr\": 0.6713, \"isr\": 0.1791}, \"301-400\": {\"pr\": 0.7013, \"isr\": 0.1984}, \"401-500\": {\"pr\": 0.7725, \"isr\": 0.2299}}}, \"notes\": \"conclusion=negative 基于 prove_rate 下降（last100 0.7725 vs exec-only 0.865）。但结构性发现：ISR/PR ratio=0.298，99/100 步 ISR &lt; PR，说明 STA=0.1 维持了 ISR 与 PR 的持续分离——模型未通过 hacking prove_rate 绕过 STA penalty。此观察支持论文 \\\"STA 抑制 reward hacking\\\" claim：即使低权重 STA 也能保持结构性约束（ISR 不跟随 PR 虚高），代价是 prove_rate 有一定下降。windowed ISR/PR: 1-50 (0.51), 51-100 (0.47), 101-200 (0.29), 201-300 (0.27), 301-400 (0.28), 401-500 (0.30) — 分
…[truncated 36019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T02:11:24.541924+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "solver-trace-ablation",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "solver-trace-ablation",
    "status": "running"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T02:11:24.592580+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "report.md"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T02:11:26.803187+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 2, \"results\": [{\"exp_id\": \"plan001-exec-only-s43-r4\", \"success\": true, \"actions\": [\"Job still running (pid=136339)\"]}, {\"exp_id\": \"plan013-random-reward-s42-r4\", \"success\": true, \"actions\": [\"Job still running (pid=136261)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 3269
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T02:11:26.854940+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_research_plan014-downstream-design_20260514T020422\", \"task_type\": \"research:plan014-downstream-design\", \"project\": \"solver-trace-ablation\", \"status\": \"running\", \"started_at\": \"2026-05-14T02:04:22.385071+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 2313
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T02:11:26.855505+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan001-exec-only-s43-r4 | — | — | — | — |\\n| plan013-random-reward-s42-r4 | — | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **plan001-exec-only-s43-r3** (failed): —\\n- **plan013-random-reward-s42-r3** (failed): —\\n- **plan001-exec-only-s43-r2** (failed): —\\n\\n## 趋势\\n成功 5 / 负向 4 / 失败 14 / 共 23\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39279: 无 GPU 信息\\n\\n## 告警\\n- sta-phase1-exec-only: 训练失败 — unknown\\n- sta-phase1-exec-sta: 训练失败 — unknown\\n- sta-phase1-exec-only-r2: 训练失败 — unknown\\n- sta-phase1-exec-sta-r2: 训练失败 — unknown\\n- sta-phase1-exec-only-r3: 训练失败 — unknown\\n- sta-phase1-exec-sta-r3: 训练失败 — unknown\\n- plan001-exec-only-s42: 训练失败 — unknown\\n- plan001-exec-only-s42-r3: 训练失败 — unknown\\n- plan001-exec-only-s43: 训练失败 — unknown\\n- plan013-random-reward-s42: 训练失败 — unknown\\n- plan013-random-reward-s42-r2: 训练失败 — unknown\\n- plan001-exec-only-s43-r2: 训练失败 — unknown\\n- plan013-random-reward-s42-r3: 训练失败 — unknown\\n- plan001-exec-only-s43-r3: 训练失败 — unknown\\n\", \"total_chars\": 1088, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 2262
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T02:11:35.489495+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "solver-trace-ablation",
  "status": "done",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "solver-trace-ablation",
    "status": "done",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T02:11:35.541941+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_ops_check-training-progress_20260514T020044\", \"task_type\": \"ops:check-training-progress\", \"project\": \"solver-trace-ablation\", \"status\": \"done\", \"started_at\": \"2026-05-14T02:00:44.846543+00:00\", \"ended_at\": \"2026-05-14T02:01:41.887305+00:00\"}, {\"worker_id\": \"worker_ops_prepare-seed44-config_20260514T020104\", \"task_type\": \"ops:prepare-seed44-config\", \"project\": \"solver-trace-ablation\", \"status\": \"done\", \"started_at\": \"2026-05-14T02:01:05.148187+00:00\", \"ended_at\": \"2026-05-14T02:04:05.721788+00:00\"}, {\"worker_id\": \"worker_research_plan005-negative-literature_20260514T020402\", \"task_type\": \"research:plan005-negative-literature\", \"project\": \"solver-trace-ablation\", \"status\": \"done\", \"started_at\": \"2026-05-14T02:04:02.303013+00:00\", \"ended_at\": \"2026-05-14T02:09:20.376492+00:00\"}, {\"worker_id\": \"worker_code_plan002-additive-bonus_20260514T020603\", \"task_type\": \"code:plan002-additive-bonus\", \"project\": \"solver-trace-ablation\", \"status\": \"done\", \"started_at\": \"2026-05-14T02:06:03.570145+00:00\", \"ended_at\": \"2026-05-14T02:08:41.425234+00:00\"}, {\"worker_id\": \"worker_code_plan002-additive-bonus-reward_20260514T020631\", \"task_type\": \"code:plan002-additive-bonus-reward\", \"project\": \"solver-trace-ablation\", \"status\": \"done\", \"started_at\": \"2026-05-14T02:06:31.350787+00:00\", \"ended_at\": \"2026-05-14T02:10:06.049909+00:00\"}], \"count\": 5}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T02:11:35.592625+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T02:11:35.643531+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ROADMAP.md\", \"content\": \"# solver-trace-ablation — Research Dashboard\\n\\n> 最后更新: 2026-05-13 23:09 UTC | 更新原因: Dream 完成 + plan_003 消歧确认 penalty effect + plan_001 3次失败紧急处理\\n\\n## 核心方向\\nSTA（Solver Trace Ablation）：基于 mutation testing 的 component necessity testing，为 neurosymbolic formalizer 的 GRPO 训练提供 intensional structural reward。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 通过，消歧实验完成，Dream 审稿指导重构中）\\n- **基础设施**: westd-39279 × 2 RTX PRO 6000 96GB\\n- **消歧结论 (D008)**: plan_003 held-out eval 确认 exec-only checkpoint ISR=0.6423（proved-only），高于 GT 0.56。**Interpretation B confirmed**: 50/50 STA reward 是 penalty effect，非 hacking detection。\\n- **Dream 结果**: dream_20260513T215750 done — best 4/6 Borderline Reject, median 3/6 Weak Reject\\n- **Dream 跨档一致问题**: (1) related work 6→25+ (2) RIP framing 过度 (3) ISR circularity (4) single-seed secondary (5) ISR sparsity/\\\"dense+automatic\\\" 不成立\\n- **论文 story 转向**: \\\"STA detects hacking\\\" → \\\"STA as principled structural metric + proper integration\\\"\\n- **⚠️ plan_001 连续 3 次 failed**: exec-only baseline 500步尚未成功运行，Agent 正在诊断\\n- **plan_005 RUNNING**: STA weight=0.1 训练进行中（cuda:1）\\n\\n## 实验计划摘要（详见 experiment_plan.yaml）\\n**既有 P0**:\\n- plan_001: exec-only 500步 3seed baseline — **3次failed，紧急修复中**\\n- plan_002: exec+STA 500步 3seed — 待 plan_005 确定最优权重\\n- plan_003: held-out eval — ✅ done, 消歧完成\\n- plan_005: weight ablation — RUNNING (sta_weight=0.1)\\n\\n**Dream 新增实验需求**:\\n- **random reward baseline** (NEW): random structural penalty 替代 ISR → 隔离 ISR specific signal vs multi-objective regularization. ~1 GPU·h. **Dream M2/W7 必修**\\n- **downstream validation** (NEW): 高 ISR formalizations 用于下游逻辑推理任务 → 打破 ISR circularity. **Dream M2/W4 必修**\\n- **3-seed for secondary**: 至少 Prolog (plan_006) + top weight config 需 3 seed. ~6 GPU·h\\n- **curriculum ablation**: linear ramp vs sigmoid c
…[truncated 2523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T02:11:47.997131+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T02:11:48.047904+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T02:11:51.813874+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_code_plan002-additive-bonus-reward_20260514T020631"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_code_plan002-additive-bonus-reward_20260514T020631"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T02:11:52.269469+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_code_plan002-additive-bonus-reward_20260514T020631\", \"status\": \"done\", \"task_type\": \"code:plan002-additive-bonus-reward\", \"project\": \"solver-trace-ablation\", \"started_at\": \"2026-05-14T02:06:31.350787+00:00\", \"ended_at\": \"2026-05-14T02:10:06.049909+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"全部就绪。代码和配置已到位，汇总：\\n\\n**`scripts/train_grpo.py` 已有改动：**\\n- `make_reward_fn` 签名新增 `beta: float = 0.3`\\n- `additive_bonus` 分支实现 `r = r_exec * (1 + β·ISR)` (line 187-195)\\n- `--beta` CLI 参数 (line 312-313)\\n- `--reward_mode` choices 包含 `additive_bonus`\\n- `beta` 传入 `make_reward_fn` (line 384)\\n- `save_total_limit=1` (C003 合规)\\n\\n**`configs/grpo_additive_bonus.yaml`：**\\n- `reward_mode: additive_bonus`, `beta: 0.3`\\n- `data_path: data/train_500_seed42.jsonl` (C001 合规)\\n- `output_dir: /root/autodl-tmp/outputs/plan002_additive_beta03_s42` (已修正)\\n- `no_wandb: true`, `seed: 42`\\n\\n**Dry-run 验证通过：** 语法检查 OK，`--help` 确认 `--beta` 和 `additive_bonus` 模式均被识别。\"}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 455
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T02:11:52.271664+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_code_plan002-additive-bonus_20260514T020603"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_code_plan002-additive-bonus_20260514T020603"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T02:11:53.226060+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_code_plan002-additive-bonus_20260514T020603\", \"status\": \"done\", \"task_type\": \"code:plan002-additive-bonus\", \"project\": \"solver-trace-ablation\", \"started_at\": \"2026-05-14T02:06:03.570145+00:00\", \"ended_at\": \"2026-05-14T02:08:41.425234+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"全部修改已验证通过。总结：\\n\\n**`scripts/train_grpo.py` 修改：**\\n- **L148**: `make_reward_fn` 签名增加 `beta: float = 0.3` 参数\\n- **L187-195**: 新增 `additive_bonus` 模式 — `r = r_exec * (1 + beta * ISR)`，调用 `_full_fn` 时 `sta_weight=1.0` 确保 ISR 被计算\\n- **L302**: `--reward_mode` choices 增加 `\\\"additive_bonus\\\"`\\n- **L312-313**: 新增 `--beta` CLI 参数（默认 0.3）\\n- **L384**: `main()` 中传递 `beta` 到 `make_reward_fn`\\n- `save_total_limit` 从 2 改为 1（C003）\\n\\n**新建 `configs/grpo_additive_bonus.yaml`：**\\n- `reward_mode: additive_bonus`, `beta: 0.3`\\n- `data_path: data/train_500_seed42.jsonl`（C001）\\n- `output_dir: /root/autodl-tmp/outputs/grpo_additive_bonus_b03`\\n- 其他参数与 plan005 一致（500 steps, K=8, lr=1e-6）\\n- `no_wandb: true`\\n\\nDry-run `--help` 通过，argparse 正确识别所有新参数。GPU 空出后可直接提交。\"}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T02:11:53.276674+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_ops_prepare-seed44-config_20260514T020104"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_ops_prepare-seed44-config_20260514T020104"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T02:11:53.628417+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_ops_prepare-seed44-config_20260514T020104\", \"status\": \"done\", \"task_type\": \"ops:prepare-seed44-config\", \"project\": \"solver-trace-ablation\", \"started_at\": \"2026-05-14T02:01:05.148187+00:00\", \"ended_at\": \"2026-05-14T02:04:05.721788+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"**seed=44 就绪，状态: READY**\\n\\n已完成的检查:\\n- Config 文件 ✅ — exec_only 模式，Qwen3-4B\\n- 数据文件 `train_500_seed42.jsonl` ✅ — 符合 C001\\n- 磁盘 112GB 可用 ✅ — s43 占 30GB，s44 同量级后仍余 ~82GB\\n- Import 测试通过 ✅\\n- 输出目录 `plan001_exec_only_s44` 已创建 ✅\\n- `log_completions=False` ✅ — completions parquet 已禁用\\n- `CUDA_VISIBLE_DEVICES` 用 `export` 设置 ✅ — 符合 C002\\n\\n**唯一 flag**: `save_total_limit=2`（C003 要求 1），但与当前跑的 s43 一致，且磁盘充足，不阻塞。\\n\\n报告已保存到 `artifacts/seed44_readiness.md`，含完整提交命令（含 nohup 版本）。等 s43 跑完释放 cuda:1 即可提交。\"}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 351
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T02:11:53.731006+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_research_plan005-negative-literature_20260514T020402"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_research_plan005-negative-literature_20260514T020402"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T02:11:53.781654+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_research_plan005-negative-literature_20260514T020402\", \"status\": \"done\", \"task_type\": \"research:plan005-negative-literature\", \"project\": \"solver-trace-ablation\", \"started_at\": \"2026-05-14T02:04:02.303013+00:00\", \"ended_at\": \"2026-05-14T02:09:20.376492+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"完成。\\n\\n**调研报告** → `artifacts/plan005_negative_literature.md`\\n**文献地图** → `literature_map.yaml` 新增 5 篇论文（reward-shaping category）\\n\\n### 核心结论\\n\\nplan005 的 NEGATIVE 结果（ISR 降低 prove_rate）是 multi-objective RL 中已知的 **auxiliary reward degradation** 现象，5 篇论文从不同角度确认：\\n\\n1. **Gao et al. (2024)** — process reward 在 RL 训练中可能**比 success-only reward 更差**\\n2. **Ye et al. (2025, PROF)** — 朴素混合 PRM+ORM 导致退化，需 consistency filtering\\n3. **Moskovitz et al. (2023, ICLR 2024)** — 固定权重线性组合存在过度优化阈值\\n4. **Skalse et al. (2022, NeurIPS)** — 理论证明：任何非常数 proxy reward 都可能降低 true reward\\n5. **Rezaei et al. (2026, PROGRS)** — 无条件 process reward 会放大失败模式，需 outcome-conditioned centering\\n\\n**推荐改进方向**：Bonus-only + Outcome-conditioned ISR（仅对 prove 成功的样本施加正向 ISR bonus），实施复杂度低且同时解决 hackability 和 gradient corruption 问题。\\n\\nSources:\\n- [Gao et al. - On Designing Effective RL Reward](https://arxiv.org/abs/2410.15115)\\n- [Ye et al. - Beyond Correctness (PROF)](https://arxiv.org/abs/2509.03403)\\n- [Moskovitz et al. - Confronting Reward Model Overoptimization](https://arxiv.org/abs/2310.04373)\\n- [Skalse et al. - Defining and Characterizing Reward Hacking](https://arxiv.org/abs/2209.13085)\\n- [Rezaei et al. - PROGRS](https://arxiv.org/abs/2604.02341)\"}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T02:12:19.597983+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/skills/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T02:12:19.598646+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_e94af266.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T02:12:22.923897+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T02:12:22.975022+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T02:12:25.339845+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation*",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation*",
    "path": "/home/ubuntu/agent-ml-research"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T02:12:25.491074+00:00_

/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T02:12:27.704729+00:00_

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
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T02:12:27.755777+00:00_

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
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T02:13:08.474664+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "ops:verify-plan002-code-integrity",
  "project": "solver-trace-ablation",
  "task_prompt": "## 任务：验证 plan002 additive bonus 代码完整性\n\n**背景**：上一轮有两个 Worker 同时修改了服务器上的 `scripts/train_grpo.py` 和创建了 `configs/grpo_additive_bonus.yaml`，可能产生冲突。需要验证代码是正确的。\n\n**服务器**: westd-39279\n**代码路径**: `/root/solver-trace-ablation/`\n**激活环境**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n\n### 验证清单\n\n1. **SSH 读取 `scripts/train_grpo.py`**，检查：\n   - `make_reward_fn` 函数签名包含 `beta: float = 0.3`\n   - 存在 `additive_bonus` 分支，实现 `r = r_exec * (1 + beta * ISR)`\n   - `--reward_mode` choices 包含 `\"additive_bonus\"`\n   - `--beta` CLI 参数存在（默认 0.3）\n   - `beta` 传入 `make_reward_fn`\n   - `save_total_limit=1`（C003 约束）\n   - 没有语法错误、没有重复代码块\n\n2. **SSH 读取 `configs/grpo_additive_bonus.yaml`**，检查：\n   - `reward_mode: additive_bonus`\n   - `beta: 0.3`\n   - `data_path: data/train_500_seed42.jsonl`（C001 约束）\n   - `output_dir` 在 `/root/autodl-tmp/outputs/` 下\n   - `log_completions: false` 或等效设置\n   - `save_total_limit: 1`（C003）\n\n3. **额外检查**：\n   - `save_total_limit` 在 `configs/grpo_exec_only.yaml` 中也应为 1（seed44 Worker 发现是 2）\n   - 如果不是 1，修改为 1\n\n4. **Dry-run 验证**：\n   ```bash\n   cd /root/solver-trace-ablation\n   python3 scripts/train_grpo.py --help 2>&1 | grep -E \"reward_mode|beta\"\n   python3 -c \"import scripts.train_grpo\" 2>&1 || python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --num_steps 1 --dry_run 2>&1 | head -20\n   ```\n\n5. **检查磁盘空间**：`df -h /root/autodl-tmp/`\n\n### 产出\n在回复中汇报：\n- 代码是否一致/有冲突\n- save_total_limit 是否已修正\n- dry-run 是否通过\n- 磁盘空间状况\n",
  "tool_groups": "['ssh']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "ops:verify-plan002-code-integrity",
    "project": "solver-trace-ablation",
    "task_prompt": "## 任务：验证 plan002 additive bonus 代码完整性\n\n**背景**：上一轮有两个 Worker 同时修改了服务器上的 `scripts/train_grpo.py` 和创建了 `configs/grpo_additive_bonus.yaml`，可能产生冲突。需要验证代码是正确的。\n\n**服务器**: westd-39279\n**代码路径**: `/root/solver-trace-ablation/`\n**激活环境**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n\n### 验证清单\n\n1. **SSH 读取 `scripts/train_grpo.py`**，检查：\n   - `make_reward_fn` 函数签名包含 `beta: float = 0.3`\n   - 存在 `additive_bonus` 分支，实现 `r = r_exec * (1 + beta * ISR)`\n   - `--reward_mode` choices 包含 `\"additive_bonus\"`\n   - `--beta` CLI 参数存在（默认 0.3）\n   - `beta` 传入 `make_reward_fn`\n   - `save_total_limit=1`（C003 约束）\n   - 没有语法错误、没有重复代码块\n\n2. **SSH 读取 `configs/grpo_additive_bonus.yaml`**，检查：\n   - `reward_mode: additive_bonus`\n   - `beta: 0.3`\n   - `data_path: data/train_500_seed42.jsonl`（C001 约束）\n   - `output_dir` 在 `/root/autodl-tmp/outputs/` 下\n   - `log_completions: false` 或等效设置\n   - `save_total_limit: 1`（C003）\n\n3. **额外检查**：\n   - `save_total_limit` 在 `configs/grpo_exec_only.yaml` 中也应为 1（seed44 Worker 发现是 2）\n   - 如果不是 1，修改为 1\n\n4. **Dry-run 验证**：\n   ```bash\n   cd /root/solver-trace-ablation\n   python3 scripts/train_grpo.py --help 2>&1 | grep -E \"reward_mode|beta\"\n   python3 -c \"import scripts.train_grpo\" 2>&1 || python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --num_steps 1 --dry_run 2>&1 | head -20\n   ```\n\n5. **检查磁盘空间**：`df -h /root/autodl-tmp/`\n\n### 产出\n在回复中汇报：\n- 代码是否一致/有冲突\n- save_total_limit 是否已修正\n- dry-run 是否通过\n- 磁盘空间状况\n",
    "tool_groups": "['ssh']"
  }
}
````

</details>

---

### Tool result

_source line 35 · 2026-05-14T02:13:27.014888+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_ops_verify-plan002-code-integrity_20260514T021308\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_ops_verify-plan002-code-integrity_20260514T021308.log\", \"setup_data\": {}, \"message\": \"Worker worker_ops_verify-plan002-code-integrity_20260514T021308 started. Use get_worker_status('worker_ops_verify-plan002-code-integrity_20260514T021308') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 18540
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T02:13:27.366676+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "research:related-work-expansion",
  "project": "solver-trace-ablation",
  "task_prompt": "## 任务：Related Work 文献扩充\n\n**背景**：Dream 审稿指出我们的 related work 只有 ~6 篇引用，远低于顶会标准（需要 25+）。项目研究方向是 STA（Solver Trace Ablation）——一种基于 mutation testing 的 component necessity testing，为 neurosymbolic formalizer 的 GRPO 训练提供 intensional structural reward。\n\n**论文 story**: \"STA as principled structural metric for evaluating formalization quality + proper integration via additive bonus reward\"\n\n### 需要覆盖的 Related Work 类别\n\n1. **Neurosymbolic reasoning / autoformalization** (核心领域)\n   - LLM 自动形式化（NL→FOL, NL→Lean, NL→Isabelle）\n   - 神经符号推理系统（NeSy）\n   - 搜索关键词: autoformalization, neural theorem proving, neurosymbolic reasoning, LLM formalization\n\n2. **Process reward / structural reward in RL**\n   - PRM (Process Reward Models)\n   - ORM vs PRM 对比\n   - Multi-objective RL reward design\n   - 搜索关键词: process reward model, reward shaping LLM, multi-objective RLHF\n\n3. **Mutation testing / software testing → ML 的迁移**\n   - Mutation testing 传统方法\n   - Mutation testing 在 ML / formal verification 中的应用\n   - 搜索关键词: mutation testing formal verification, mutation analysis program correctness\n\n4. **Reward hacking / overoptimization**\n   - RLHF reward hacking\n   - Goodhart's law in RL\n   - 搜索关键词: reward hacking RLHF, reward overoptimization, Goodhart's law RL\n\n5. **GRPO / reinforcement learning for reasoning**\n   - DeepSeek GRPO\n   - RL for mathematical/logical reasoning\n   - 搜索关键词: GRPO reasoning, reinforcement learning mathematical reasoning, RL code generation\n\n### 产出要求\n\n把找到的论文整理成以下格式，写入 `artifacts/related_work_survey.md`：\n\n```markdown\n## Category: [类别名]\n\n### [Paper Title] (Year, Venue)\n- **Authors**: ...\n- **Key contribution**: 1-2 句\n- **与我们的关系**: 我们的工作如何 differ/extend\n- **BibTeX key 建议**: [简短 key]\n- **arXiv/DOI**: [链接]\n```\n\n目标: 每个类别至少 5 篇论文，总计 25-30 篇。优先选 2023-2026 的论文。确保每篇论文都是真实存在的（通过 WebSearch 验证 arXiv ID）。\n",
  "tool_groups": "['knowledge']",
  "tools": "['WebSearch']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "research:related-work-expansion",
    "project": "solver-trace-ablation",
    "task_prompt": "## 任务：Related Work 文献扩充\n\n**背景**：Dream 审稿指出我们的 related work 只有 ~6 篇引用，远低于顶会标准（需要 25+）。项目研究方向是 STA（Solver Trace Ablation）——一种基于 mutation testing 的 component necessity testing，为 neurosymbolic formalizer 的 GRPO 训练提供 intensional structural reward。\n\n**论文 story**: \"STA as principled structural metric for evaluating formalization quality + proper integration via additive bonus reward\"\n\n### 需要覆盖的 Related Work 类别\n\n1. **Neurosymbolic reasoning / autoformalization** (核心领域)\n   - LLM 自动形式化（NL→FOL, NL→Lean, NL→Isabelle）\n   - 神经符号推理系统（NeSy）\n   - 搜索关键词: autoformalization, neural theorem proving, neurosymbolic reasoning, LLM formalization\n\n2. **Process reward / structural reward in RL**\n   - PRM (Process Reward Models)\n   - ORM vs PRM 对比\n   - Multi-objective RL reward design\n   - 搜索关键词: process reward model, reward shaping LLM, multi-objective RLHF\n\n3. **Mutation testing / software testing → ML 的迁移**\n   - Mutation testing 传统方法\n   - Mutation testing 在 ML / formal verification 中的应用\n   - 搜索关键词: mutation testing formal verification, mutation analysis program correctness\n\n4. **Reward hacking / overoptimization**\n   - RLHF reward hacking\n   - Goodhart's law in RL\n   - 搜索关键词: reward hacking RLHF, reward overoptimization, Goodhart's law RL\n\n5. **GRPO / reinforcement learning for reasoning**\n   - DeepSeek GRPO\n   - RL for mathematical/logical reasoning\n   - 搜索关键词: GRPO reasoning, reinforcement learning mathematical reasoning, RL code generation\n\n### 产出要求\n\n把找到的论文整理成以下格式，写入 `artifacts/related_work_survey.md`：\n\n```markdown\n## Category: [类别名]\n\n### [Paper Title] (Year, Venue)\n- **Authors**: ...\n- **Key contribution**: 1-2 句\n- **与我们的关系**: 我们的工作如何 differ/extend\n- **BibTeX key 建议**: [简短 key]\n- **arXiv/DOI**: [链接]\n```\n\n目标: 每个类别至少 5 篇论文，总计 25-30 篇。优先选 2023-2026 的论文。确保每篇论文都是真实存在的（通过 WebSearch 验证 arXiv ID）。\n",
    "tool_groups": "['knowledge']",
    "tools": "['WebSearch']"
  }
}
````

</details>

---

### Assistant

_source line 37 · 2026-05-14T02:31:08.369413+00:00_

Worker 池当前只有 1 个（plan014），违反 ≥2 硬约束。两个 plan002 code Worker 可能对同一文件有冲突写入，需要验证。同时需要补充 CPU Worker。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:sta-phase1-exec-sta-r2"
}
```

</details>

---

## Round 2

22 recorded events

### User

_source line 38 · 2026-05-14T05:32:38.456464+00:00_

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
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T05:33:04.156781+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/",
  "description": "List project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/",
    "description": "List project directory"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T05:33:05.447625+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
artifacts
checkpoints
constraints.lock
constraints.yaml
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
literature_map.yaml
logs
memory.md
paper_framing.md
registry.lock
registry.yaml
report.md
study_status.lock
task_context

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Bash",
  "elapsed_ms": 1290
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T05:33:05.750545+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ -name \"registry.yaml\" -o -name \"report.md\" -o -name \"ROADMAP.md\" -o -name \"memory.md\" -o -name \"experiment_plan.yaml\" -o -name \"paper_framing.md\" 2>/dev/null",
  "description": "Find key project files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ -name \"registry.yaml\" -o -name \"report.md\" -o -name \"ROADMAP.md\" -o -name \"memory.md\" -o -name \"experiment_plan.yaml\" -o -name \"paper_framing.md\" 2>/dev/null",
    "description": "Find key project files"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T05:33:05.803197+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ROADMAP.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T05:33:08.417213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/registry.yaml"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T05:33:08.871311+00:00_

1	baseline: null
2	experiments:
3	  sta-phase0-baseline:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-13T17:51:48.853Z'
7	    updated_at: '2026-05-13T18:10:40.982Z'
8	    spec:
9	      hypothesis: 锚定 base Qwen3-4B 的 ISR baseline，后续判断 GRPO 训练是否导致 ISR 下降（reward hacking）
10	      model_name: Qwen3-4B
11	      data_path: /root/solver-trace-ablation/data/proofwriter_fol_100.jsonl
12	      data_count: 100
13	      server: westd-39279
14	      data_source: tasksource/folio
15	      command: CUDA_VISIBLE_DEVICES=0 python3 scripts/phase0_baseline.py --model_path
16	        models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output outputs/phase0_baseline.json
17	      seed: 0
18	      checkpoint_path: N/A (inference only)
19	      log_path: /root/solver-trace-ablation/outputs/phase0_baseline.json
20	      notes: conclusion=success 但语义是 baseline_anchored（registry 不支持自定义 conclusion）。此实验是
21	        baseline 锚定，非传统 success/failure。ISR 盲区：premise-conclusion 重复的 trivial formalization
22	        可能获高 ISR，论文 Discussion 需讨论。
23	    log_path: /tmp/phase0_baseline.log
24	    checkpoint_path: /root/solver-trace-ablation/outputs/phase0_baseline.json
25	    metrics:
26	      mean_isr: 0.0641
27	      isr_std: 0.1983
28	      median_isr: 0
29	      isr_range:
30	      - 0
31	      - 0.889
32	      prove_rate: 0.12
33	      proved_count: 12
34	      total_samples: 100
35	      xor_affected_samples: 34
36	      effective_prove_rate_no_xor: 0.182
37	      avg_time_per_sample_s: 3.4
38	      total_runtime_s: 336
39	      isr_by_answer:
40	        'true':
41	          n: 34
42	          proved: 9
43	          prove_rate: 0.265
44	          mean_isr: 0.1345
45	        'false':
46	          n: 25
47	          proved: 1
48	          prove_rate: 0.04
49	          mean_isr: 0.024
50	        unknown:
51	          n: 41
52	          proved: 2
53	          prove_rate: 0.049
54	          mean_isr: 0.0302
55	    conclusion: success
56	    completed_at: '2026-05-13T18:04:56
…[truncated 57890 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T05:33:08.922060+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/report.md"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T05:33:09.323756+00:00_

1	# Handover — 2026-05-14
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| plan002-additive-b01-s42 | — | — | — | — |
9	
10	## 待处理
11	- plan016-extended-1000-s42: Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence? 1000步观察 PR 和 ISR 在更长 horizon 的行为。s43(14%)/s44(98% tautological) 在 500 步均失败，延长训练是否能改善？（已分配 westd-39279 GPU:cuda:1，等待提交）
12	
13	## 近期结论
14	- **plan017-additive-random-s42** (negative): Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。 ← 基于 plan013-random-reward-s42-r4
15	  [eval_sta_plan017_additive_random_s42](/api/workspace-files/projects/solver-trace-ablation/artifacts/plan017-additive-random-s42/data/eval_sta_plan017_additive_random_s42.txt)
16	- **plan001-exec-only-s44** (negative): Exec-only seed=44 第3 seed: 解决 s42(93% eval PR) vs s43(13% eval PR) 的跨 seed 不稳定问题，3-seed mean±std 是论文必需。
17	  [eval_sta_plan001_exec_only_s44](/api/workspace-files/projects/solver-trace-ablation/artifacts/plan001-exec-only-s44/data/eval_sta_plan001_exec_only_s44.json)
18	- **plan014-downstream-nli-s42** (negative): Downstream NLI validation: 高ISR formalization 应在独立推理任务上表现更好(entailment accuracy)，Spearman ρ(ISR, accuracy) > 0.1 验证 ISR 作为 quality proxy 的实用价值。同时用 Z3 cross-solver agreement 验证 formalization 鲁棒性。
19	
20	## 趋势
21	成功 6 / 负向 9 / 失败 14 / 共 29
22	
23	## 下一步
24	（无活跃 idea，请通过 ideas.md 添加）
25	
26	## 资源状态
27	westd-39279: 无 GPU 信息
28	
29	## 告警
30	- sta-phase1-exec-only: 训练失败 — unknown
31	- sta-phase1-exec-sta: 训练失败 — unknown
32	- sta-phase1-exec-only-r2: 训练失败 — unknown
33	- sta-phase1-exec-sta-r2: 训练失败 — unknown
34	- sta-phase1-exec-only-r3: 训练失败 — unknown
35	- sta-phase1-exec-sta-r3: 训练失败 — unknown
36	- plan001-exec-only-s42: 训练失败 — unknown
37	- plan001-exec-only-s4
…[truncated 306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T05:33:09.725958+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T05:33:09.726418+00:00_

1	# solver-trace-ablation — Research Dashboard
2	
3	> 最后更新: 2026-05-14 05:32 UTC | 更新原因: 修正 Reviewer CRITICAL: s42 ISR=0.123 非 0.64、s44 PR=98% 非 14%、加数据精度注释、反映 pending 实验实际状态
4	
5	## 核心方向
6	STA（Solver Trace Ablation）：基于 component necessity testing 的 ISR 指标，作为 GRPO neurosymbolic formalizer 的**诊断工具**——检测 reward hacking、量化结构退化、区分不同退化模式。详见 paper_framing.md。
7	
8	**Framing 转向 (D020)**：ISR-as-reward 路线全面失败。论文转向**诊断/分析贡献**：
9	1. STA/ISR 检测 exec-only GRPO 的 reward hacking（ISR 崩塌轨迹）
10	2. GRPO saturation 机制（PR→1.0 时 loss→0 停止学习）
11	3. Hacking 策略分类学（conclusion embedding / P→P tautology / repetitive cycling / repetitive premise）
12	4. ISR 能力边界：syntactic necessity ≠ semantic faithfulness (D021)
13	
14	## 当前进展
15	- **阶段**: Research + 审稿进行中 | **DDL**: 2026-05-25（剩 11 天）
16	- **GPU**: 2 × RTX PRO 6000 96GB
17	
18	### 核心证据链
19	| 证据 | 状态 | 关键数据 |
20	|------|------|----------|
21	| ISR 崩塌轨迹 | ✅ | 100步 checkpoint (plan003): PR=32%, ISR=0.6423 → 500步 s42 (plan001): PR=93%, ISR=**0.1324** |
22	| 3-seed exec-only | ✅ | s42: PR=93%/ISR=0.123 (conclusion embedding); s43: PR=13%/ISR=0 (repetition collapse); s44: PR=**98%**/ISR=**0.57** (**tautological collapse**, n_comp=2.04, ISR 假高) |
23	| GRPO 饱和 confound | ✅ | random reward PR > exec-only PR, loss→0 mechanism (D014) |
24	| Hacking taxonomy | ✅ | 4 种模式已标注: `hacking_characterization_report.md` (plan012 done) |
25	| ISR 能力边界 | ✅ | ρ(ISR, NLI)=-0.049 n.s., ISR ≠ semantic quality (D021) |
26	| Additive ISR β=0.3 | ✅ negative | PR=18%, ISR=0.1427, repetitive cycling (D020) |
27	| Additive random 对照 | ⏳ | plan017 训练完成 (PR=0.574, ISR=0.110), eval_sta 进行中 (cuda:1) |
28	| Additive ISR β=0.1 | ⏳ | plan002-b01-s42: registered, 待提交 cuda:0 |
29	| Extended 1000-step | ⏳ | plan016: registered, 待 cuda:1 空出后提交 |
30	| Prolog 第二逻辑类型 | ❓ | plan006: 未启动, 需 readiness check |
31	
32	**⚠️ 数据精度注意**：s42 的 ISR=0.123 是 500-step held-out eval（plan001-s42-r2），ISR=0.6423 是 100-step checkpoint eval（plan003）。s44 的 PR=98% 是 tautological fake high（n_comp=2.04），不可与 s42 的 93
…[truncated 2607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T05:33:09.776905+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T05:33:09.828400+00:00_

1	# solver-trace-ablation — Memory
2	
3	## 环境信息 (2026-05-13)
4	
5	### westd-39279 服务器
6	- **GPU**: 2× RTX PRO 6000 Blackwell, 94GB VRAM 每张
7	- **CUDA**: 12.8, PyTorch 2.10.0+cu128
8	- **镜像**: aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
9	- **ML 栈**: transformers/trl/vllm/accelerate 全部预装
10	- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2, Z3 4.16.0.0
11	- **模型**: Qwen3-4B 已下载（7.6GB，通过 ModelScope）
12	- **代码路径**: `/root/solver-trace-ablation/`
13	- **磁盘**: 系统盘 250GB，大文件（outputs/checkpoints）必须放 `/root/autodl-tmp/`
14	
15	### 决策记录
16	- Qwen3-4B 用 ModelScope 下载（HuggingFace 直连可能慢）
17	- Prover9 从 LADR 源码编译（apt 无包）
18	- 94GB VRAM 单卡跑 Qwen3-4B 完全无压力
19	
20	## 数据 (2026-05-13)
21	
22	### 数据源变更：ProofWriter → FOLIO
23	- ProofWriter 原始数据无 FOL 列，改用 `tasksource/folio`（1204 条人工标注 FOL）
24	- Phase 0 子集 100 条，训练子集 500 条
25	- 34% 数据含 XOR (⊕) 符号，已在 `_normalize_fol()` 中修复展开
26	
27	### 数据约束 (2026-05-14, D009)
28	- **C001**: 所有 plan001/plan013 实验统一使用 `train_500_seed42.jsonl`，不再用 `proofwriter_fol_500.jsonl`（消除数据差异 confound）
29	
30	## Phase 0 关键发现 (2026-05-13)
31	
32	### Base Model ISR Baseline (sta-phase0-baseline)
33	- **Prove rate**: 12% overall, 18.2% excluding XOR-affected samples
34	- **Mean ISR**: 0.064 (very low — base model formalizations mostly unprovable)
35	- **ISR 区分度**: proved 样本 ISR 0.125–0.889
36	
37	### Ground-Truth ISR Baseline (sta-gt-isr-baseline)
38	- **GT prove rate**: 18% (limited by Prover9 only proving entailment; true=50%, false=4%, unknown=0%)
39	- **GT mean ISR**: 0.5588 (median 0.6125, range 0.14–1.00)
40	- **MVP Pass #2 验证**: GT ISR 0.559 > 0.5 ✅，好的 formalization ISR 高
41	- **Model vs GT gap**: ISR 0.064 vs 0.559 = 8.7x 差距，STA 有强区分力
42	
43	### Prover9 局限性
44	- Prover9 只能证明 entailment（conclusion 从 premises 推出）
45	- `false` 和 `unknown` 类问题几乎无法证明（false 4%, unknown 0%）
46	- Phase 1 训练中 reward 信号主要来自 `true` 类样本
47	
48	### ISR 已知盲区
49	- premise-conclusion 重复的 trivial formalization 可能获高 ISR
50	- 需在论文 Discussio
…[truncated 6351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T05:33:15.455848+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/experiment_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T05:33:15.908421+00:00_

1	experiments:
2	- id: plan_001
3	  claim: 1
4	  description: FOL single-logic GRPO, execution-only reward (500 steps, K=8, 3 seeds)
5	    — baseline for STA comparison
6	  priority: P0
7	  gpu_budget_hours: 3
8	  deps: []
9	  registry_id: plan001-exec-only-s43-r4
10	- id: plan_002
11	  claim: 1
12	  description: 'FOL single-logic GRPO, additive ISR bonus: r = r_exec · (1 + β·ISR),
13	    β∈{0.1, 0.3, 0.5}. 先跑 β=0.3 单 seed 验证方向，成功再 3-seed。旧凸组合公式 (α·r_exec + β·r_exec·ISR,
14	    α+β=1) 已废弃——ISR<1 时永远是 penalty (plan005 confirmed)。 新公式确保 ISR 只能 bonus 不能 penalty。'
15	  priority: P0
16	  gpu_budget_hours: 4
17	  deps: []
18	  registry_id: plan002-additive-b03-s42
19	- id: plan_003
20	  claim: 1
21	  description: 'FOL held-out evaluation: compare plan_001 vs plan_002 checkpoints
22	    on test set using identical full STA metrics (prove_rate, ISR, ISR/PR ratio, hacking
23	    taxonomy annotation)'
24	  priority: P0
25	  gpu_budget_hours: 1
26	  deps:
27	  - plan_001
28	  - plan_002
29	  registry_id: plan003-eval-exec-only-r5
30	- id: plan_004
31	  claim: 1
32	  description: 'STA O(1) vs O(N) ablation: rerun exec+STA with fast_isr_fol to confirm
33	    O(1) ineffectiveness at scale (500 steps, 1 seed) — negative result documentation'
34	  priority: P0
35	  gpu_budget_hours: 1
36	  deps: []
37	- id: plan_005
38	  claim: 1
39	  description: 'STA reward weight ablation: test α/β ratios (0.3/0.7, 0.5/0.5, 0.7/0.3)
40	    + sigmoid curriculum vs fixed — isolate optimal STA integration'
41	  priority: P0
42	  gpu_budget_hours: 4
43	  deps: []
44	  registry_id: plan005-sta-low-s42
45	- id: plan_006
46	  claim: 2
47	  description: 'Prolog single-logic GRPO: exec-only vs exec+STA (500 steps, K=8, 3
48	    seeds) — second logic type validation. Dream M3: must have 3 seeds for cross-logic
49	    claim.'
50	  priority: P1
51	  gpu_budget_hours: 6
52	  deps: []
53	  notes: Requires Prolog STA instantiation (rule ablation). SWI-Prolog already installed.
54	    Upgraded from 1→3 seeds pe
…[truncated 3824 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T05:33:15.959086+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T05:33:16.010339+00:00_

1	_next_id: 25
2	decisions:
3	- id: D001
4	  date: 2026-05-13 17:34 UTC
5	  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性
6	  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological
7	    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass
8	    标准：ISR gap >20pp + accuracy 降幅 <5pp。
9	  related_experiments: []
10	  depends_on: []
11	- id: D002
12	  date: 2026-05-13 17:37 UTC
13	  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria
14	  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察
15	    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL
16	    压力下无止境调整。
17	  related_experiments: []
18	  depends_on:
19	  - D001
20	- id: D003
21	  date: 2026-05-13 20:50 UTC
22	  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑
23	  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B
24	    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889
25	    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8
26	    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。
27	  related_experiments:
28	  - exp_id: sta-phase1-exec-only-r4
29	    role: evidence
30	    result: prove_rate 12%→15%, ISR ~0.15, minimal learning
31	  - exp_id: sta-phase1-exec-sta-r4
32	    role: evidence
33	    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号
34	  depends_on:
35	  - D002
36	- id: D004
37	  date: 2026-05-13 21:59 UTC
38	  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重
39	    + bonus 模式实验
40	  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给
41	    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteria 未触发（差
42	    5pp 非 15pp，权重未调整），但核心假设受挑战。需立即验证：(1) sta_weight=0.1 降低惩罚 (2) ISR-as-bonus 模式 r=exec×(1+α×ISR)
43	    避免惩罚。
44	  relate
…[truncated 18608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T05:33:26.310228+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T05:33:26.863149+00:00_

1	# Paper Framing — solver-trace-ablation
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)
5	- Fallback: EMNLP 2026 Findings
6	- Deadline: ARR May 25, 2026
7	
8	## Core Claims (4 条 — D020 诊断/分析论文定位)
9	
10	### Claim 1: ISR as Hacking Diagnostic
11	Intensional Structural Reward (ISR), derived from component necessity testing (leave-one-out ablation on solver proof components), detects reward hacking in GRPO-trained neurosymbolic formalizers that prove_rate alone cannot reveal. ISR collapses from 0.6423 (early training, 100 steps) → 0.1324 (converged, 500 steps) while prove_rate rises from 0.32 → 0.93 — quantifying structural degradation invisible to execution-only metrics.
12	
13	**证据**:
14	- plan003 (100步 checkpoint): proved_only_ISR=0.6423, PR=0.32 — 结构完好
15	- plan001-s42 (500步 checkpoint): proved_only_ISR=0.1324, median_ISR=0.0, PR=0.93 — 高 PR 但结构崩塌
16	- 3-seed exec-only 全景：s42 conclusion embedding (ISR≈0), s43 repetition collapse, s44 tautological collapse (n_comp=2.04, ISR=0.57 假高)
17	- 跨 seed 一致性：2/3 seeds 退化，单 seed 结果不可信
18	
19	### Claim 2: GRPO Saturation Mechanism
20	Exec-only GRPO exhibits a saturation failure mode: when prove_rate → 1.0, reward_std → 0, loss → 0, gradient signal vanishes and training stalls. Any reward component introducing variance (ISR, random noise) prevents saturation but does not prevent hacking — creating a confound in reward comparisons.
21	
22	**证据**:
23	- plan001 exec-only: PR=0.865-0.966, loss→0 at saturation (D014)
24	- plan013 random reward: PR=0.966 > exec-only PR=0.865 — random noise 防饱和但产生 tautological hacking
25	- plan002 additive ISR: PR=18% — ISR 信号过强抑制 prove 行为（与 random 对比说明 ISR 内容影响训练动态）
26	- plan017 additive random (待 eval): matched control 隔离 ISR signal vs pure variance regularization
27	
28	### Claim 3: Hacking Taxonomy
29	Different reward formulations induce distinct, characteristic hacking strategies in GRPO-trained formalizers. This taxonomy enables targeted diagnosis:
30	1. **Co
…[truncated 2318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T05:33:26.863502+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/constraints.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/constraints.yaml"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T05:33:26.913917+00:00_

1	_next_id: 6
2	constraints:
3	- id: C001
4	  added: 2026-05-13 23:57 UTC
5	  summary: 所有实验统一使用 data/train_500_seed42.jsonl 作为训练数据，禁止使用 proofwriter_fol_500.jsonl
6	    或其他数据文件
7	  scope: all
8	  reason: 'Reviewer CRITICAL: plan001-s43 使用了不同数据文件导致多 seed 对比 confound。多 seed 实验必须控制数据变量，seed
9	    仅控制模型初始化和训练随机性。'
10	- id: C002
11	  added: 2026-05-14 00:01 UTC
12	  summary: 提交训练任务前必须用 export CUDA_VISIBLE_DEVICES=N 显式设置 GPU，禁止 inline 赋值（bash -c
13	    VAR=X cmd），提交后验证 nvidia-smi 确认只占用分配的 GPU
14	  scope: all
15	  reason: plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43 OOM
16	    死亡。这是第二次 GPU 冲突事故。
17	- id: C003
18	  added: 2026-05-14 01:40 UTC
19	  summary: 训练配置必须设置 save_total_limit=1 且禁用/限制 completions parquet 保存，防止磁盘耗尽
20	  scope: all
21	  reason: plan013-r3 和 plan001-s43-r3 因磁盘 250G/250G 满导致 step 23/28 崩溃。根因：TRL 每实验保存
22	    3 份模型权重（~48GB）+ completions parquet（~2.5GB）。
23	- id: C004
24	  added: 2026-05-14 02:36 UTC
25	  summary: 跨 seed/跨 run 的 ISR 对比必须使用 eval_sta.py 统一评估，禁止引用训练日志 ISR 做跨 run 对比（不同 run
26	    可能使用不同版本的 ISR 计算代码）
27	  scope: all
28	  reason: Reviewer 核实发现 plan001-s42-r2 训练日志 ISR 使用 binary _fast_fn，plan001-s43-r4
29	    使用 full STA _full_fn，同一指标名下计算方法不同导致不可比。论文中所有 ISR 数据必须来自 eval_sta.py 统一评估。
30	- id: C005
31	  added: 2026-05-14 04:01 UTC
32	  summary: 所有 worker（含 fix/ops 类）启动任何 Python 进程前必须显式设置 CUDA_VISIBLE_DEVICES，禁止裸跑
33	  scope: worker
34	  reason: fix worker 未设 CUDA_VISIBLE_DEVICES 导致测试进程泄漏到 cuda:1（plan017 训练卡），占用 8638
35	    MiB 显存。2026-05-14 事故。
36	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sta-phase1-exec-sta-r2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-14T05:34:24.343494+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单: westd-39279 的 cuda:0 和 cuda:1（2 × RTX PRO 6000 96GB）。禁止用其他 GPU
- C001: 所有训练统一用 `data/train_500_seed42.jsonl`，禁止 `proofwriter_fol_500.jsonl`
- C002: 命令必须 `export CUDA_VISIBLE_DEVICES=N`，禁止 inline 赋值（`CUDA_VISIBLE_DEVICES=0 python`）
- C003: `save_total_limit=1` + 禁用 completions parquet，output 放 `/root/autodl-tmp/outputs/`
- C004: 跨 run ISR 对比只能用 `eval_sta.py` full STA，禁止引用训练日志 ISR
- C005: 任何 Worker（含 fix/ops）跑 Python 前必须显式设 CUDA_VISIBLE_DEVICES
- ISR-as-reward 路线已全面失败（D020），论文已转向诊断/分析贡献，**不要再尝试任何 ISR reward 方案**

### 2. 🖥️ 基础设施快照
- **服务器**: westd-39279，2× RTX PRO 6000 Blackwell 96GB，CUDA 12.8，PyTorch 2.10.0+cu128
- **环境**: aml-train 镜像，conda base（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）。**无 .venv**
- **代码**: `/root/solver-trace-ablation/`
- **模型**: `/root/autodl-tmp/models/Qwen3-4B`（7.6GB，ModelScope 下载）
- **输出**: `/root/autodl-tmp/outputs/`（系统盘 250GB 有限，大文件必须放这里）
- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2, Z3 4.16.0.0
- **eval 数据**: `/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl`（100题 held-out eval）
- **训练数据**: `/root/solver-trace-ablation/data/train_500_seed42.jsonl`（500题）
- **活跃进程**: plan002-additive-b01-s42（PID 262261, cuda:0, tmux session）
- **plan016**: ALLOCATED 状态待提交（cuda:1），等 cuda:1 空出

### 3. 📊 当前状态
**RUNNING**: plan002-additive-b01-s42（additive ISR β=0.1, cuda:0）— 这是 β=0.3 负面后的最后一次尝试，若也 negative → additive bonus 路线彻底关闭

**ALLOCATED 待提交**: plan016-extended-1000-s42（exec-only 1000步 extended training, cuda:1）— 等 cuda:1 空出后提交

**刚完成但未汇报 Director 的关键结果**:
- plan017-additive-random-s42: **negative**。Eval PR=0.48, ISR=0.0453, proved_only_ISR=0.0943。33% 已证明样本 ISR=0（n_necessary=0，结论不依赖任何前提）。与 plan013 不同的 failure mode：additive random 防止了 2-component 坍缩但模型转向生成多前提但无用的 formalization。Variance regularization 不足以产生 genuine proofs
- plan001-exec-only-s44: **negative**。TAUTOLOGICAL COLLAPSE 确认。eval PR=98% 但 94% 样本仅 2 components（premise=conclusion tautology），与 plan013 random reward 完全一致。3-seed 结果：s42=genuine, s43=degraded(PR=13%), s44=tautological(PR=98% fake)

**所有 29 个实验**: 6 success / 9 negative / 14 failed

### 4. 📋 待办（条件触发式）
- plan002-b01-s42 cron 回调到达 → spawn worker 跑 eval_sta.py on checkpoint → 若 negative → additive bonus 路线彻底关闭，论文纯诊断，向 Director 汇报 Kill Criteria #4 触发
- plan002-b01-s42 完成且 cuda:0 空出 → 提交 plan016-extended-1000-s42 到 cuda:1（或 cuda:0，看哪个先空）
- plan016 完成 → eval_sta.py 分析 1000步是否出现不同的退化轨迹
- 上述全部完成 → plan006 Prolog GRPO 是下一个大实验（D024 已批准，3 seeds，6 GPU·h），验证 hacking 现象跨 logic type 泛化。Prolog STA 代码已就绪，dry-run 已通过
- 论文 paper_framing.md 已重写（D023），但尚未开始实际 LaTeX 写作

### 5. 🎯 战略上下文
**核心结论**: ISR-as-reward 全面失败（D020），论文已 pivot 为**诊断/分析贡献**：
1. ISR 检测 reward hacking（ISR 崩塌轨迹 0.64→0.13）
2. GRPO saturation 机制（PR→1.0 时 loss→0 停止学习）
3. Hacking 策略分类学（4 种模式：conclusion embedding / P→P tautology / repetitive cycling / length-exploiting tautology）
4. ISR 能力边界（syntactic necessity ≠ semantic faithfulness）

**最容易判断错的事**:
1. **s44 的 ISR=0.57 看起来不错但是 fake** — 它来自 2-component tautology（P⊢P），与 GT ISR 0.559 接近纯属巧合。n_components 必须一起看
2. **训练日志 ISR 不可用于跨 run 对比** — 不同 run 用了不同版本的 ISR 计算（_fast_fn vs _full_fn），只有 eval_sta.py 输出可信
3. **plan013 random reward ISR=0.535 也是 fake** — 100% P→P tautology，ISR=0.5 是 2-component 机械值（D018 推翻了 D017）
4. **DDL 5月25日剩 11 天**，plan006 Prolog 是论文能进 Main vs 降级 Findings 的关键（D024）——不要拖延
5. **exec-only s42 是唯一产生 genuine proofs 的 seed**（mean_components=6.58），其他 seed 和 reward 方案全部退化。这是论文的核心数据点
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:sta-phase1-exec-sta-r2"
}
```

</details>

---
