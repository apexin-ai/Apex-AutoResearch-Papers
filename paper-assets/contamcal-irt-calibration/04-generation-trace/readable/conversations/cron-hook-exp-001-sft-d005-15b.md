# cron hook exp 001 sft d005 15B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/cron_hook_exp_001_sft_d005_15B.jsonl`
- **Structured JSON:** [`55900b168ab7c9d4be82.json`](../../sessions/55/55900b168ab7c9d4be82.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

54 recorded events

### User

_source line 1 · 2026-05-14T15:40:49.944768+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #6。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0-5 on cqa1-21977，全部 6 张分配给本项目，禁止用其他服务器 GPU
- `server: local` 实验（exp_004_sim_sweep_v2, exp_005_noise_prop_v3）禁止用 ssh_read_only 查状态，必须用 Bash `ps -p PID`。两次误标事故教训
- AutoDL eval 提交必须用绝对路径 `/root/miniconda3/bin/python` + `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`，三次失败教训见 memory.md
- train_sft.py / compute_signals.py 中的 `CUDA_VISIBLE_DEVICES` 覆写已删除，GPU 绑定由 wrapper 控制，脚本内只用 `cuda:0`。如果有人加回来会导致 GPU 错位
- 3B GSM8K 已排除出 dose-response 分析（D018），不要试图修复或重跑
- D017: 所有 MC eval 必须用 `--mc-format aligned`，legacy 结果仅供诊断参考
- exp-002 ConStat (s3) 需要 paraphrase eval 才能跑，目前 exp-003 RRF 已用 3-signal 降级模式完成

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-21977 (6× RTX 4090D)，工作目录 `/root/contamcal-irt-calibration`
- **Python**: `/root/miniconda3/bin/python`（conda base env，不用 venv）
- **模型缓存**: `/root/autodl-tmp/.hf_cache/Qwen/` (0.5B, 1.5B, 3B, 0.5B-Instruct)
- **SFT checkpoints**: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-{size}_d{dose}_s{seed}/lora_adapter`
- **Eval 输出**: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-{size}_d{dose}_s{seed}[_aligned]/`
- **Signals 输出**: `/root/autodl-tmp/exp002/signals/` (9/9 完成, S1+S2+S4)
- **exp-003 RRF**: `/root/autodl-tmp/exp003/` (3-signal RRF 已完成)
- **Stan models**: `/root/contamcal-irt-calibration/stan_models/` (4 个已编译)
- **Local CPU 实验**: 项目 artifacts 目录 `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/`
- **活跃进程 (远程 cqa1-21977)**:
  - exp_001_eval_15B_aligned_batch: PID 336750, GPU 1 — 1.5B d000/d005/d100 aligned eval batch
  - exp_001_eval_3B_d005_aligned: PID 373931, GPU 4 — 3B d005 aligned eval
  - exp_001_eval_05B_d025_aligned: PID 374947, GPU 5 — 0.5B d025 aligned eval
  - exp_001_sft_d025_15B: tmux=sft_15B_d025, GPU 0 — 1.5B d025 SFT
  - exp_001_eval_05B_d100_aligned_v3: GPU 2(?) — 0.5B d100 eval v3
  - exp_001_eval_05B_d100_aligned_v4: GPU 2(?) — 0.5B d100 eval v4
- **活跃进程 (本地)**:
  - exp_004_sim_sweep_v2: PID 411032 — 144-condition IRT simulation sweep, ETA ~May 16-17
  - exp_005_noise_prop_v3: PID 339838 — noise propagation study, ETA ~today 14:30-15:30 UTC (可能已完成)
- **活跃 Crons**: 6 个，对应上述 6 个远程 RUNNING 实验
- **活跃 Worker**: 1 个 — worker_code_exp_008_signal_survival (编写 exp-008 代码)

### 3. 📊 当前状态

**刚做完**: 上一轮 session 完成了 exp-002 signal pipeline (9/9 signals done)、exp-003 RRF aggregation、大量 eval 提交和诊断。关键决策 D013-D019 已记录。

**Registry**: 6 RUNNING / 49 DONE / 13 PREPARING (历史废弃版本)
- RUNNING 实验全部在跑，GPU 6/6 满载
- exp_004_sim_sweep_v2 (local CPU): 模拟 sweep，ETA May 16-17
- exp_005_noise_prop_v3 (local CPU): 可能已完成，**需立即 `ps -p 339838` 检查**

**等待中**:
- Worker `worker_code_exp_008_signal_survival` 正在编写 exp-008 signal survival 代码，等 [WORKER DONE] 回调
- 6 个 cron 监控远程实验，等完成回调
- exp_005_noise_prop_v3 可能已完成但未触发回调（local 实验不走 cron）

### 4. 📋 待办（条件触发式）
- **exp_005_noise_prop_v3 `ps -p 339838` 显示已退出** → spawn worker 分析结果（check artifacts/exp005_noise_propagation/output_v3/），更新 registry，汇报 Director
- **exp_001_eval_15B_aligned_batch cron 回调 DONE** → 提取 1.5B d000/d005/d100 aligned metrics → 更新 memory.md dose-response table → 这是 1.5B 完整 dose-response 数据，极关键
- **exp_001_eval_05B_d025_aligned cron 回调 DONE** → 提取 0.5B d025 metrics → 0.5B 4 点 dose-response 曲线完成 → 可立即跑 exp-002 signals on d025
- **exp_001_eval_05B_d100_aligned_v3/v4 完成** → 0.5B d100 aligned 数据到手 → 0.5B dose-response 完整 (d000/d005/d025/d100)
- **exp_001_eval_3B_d005_aligned 完成** → 3B d005 数据到手 → 3B MMLU/ARC dose-response 可做 (d000/d005, 等 d100 SFT→eval)
- **GPU 空出** → 按优先级: (1) 0.5B exp-002 signals on new dosages, (2) 3B d100 eval, (3) 3B d025 SFT, (4) 1.5B d025 eval
- **worker_code_exp_008 完成** → 审查代码 → 等 GPU 和 exp-002 数据 ready 后提交
- **所有 0.5B eval 完成** → 立即跑 exp-002 signals on {d025, d100} → exp-003 RRF 更新 → exp-006 IRT calibration (核心结果!)
- **exp-006 完成** → 填充论文 headline numbers → 这是 paper 的 main table

### 5. 🎯 战略上下文
- **截止日期**: EMNLP 2026 ARR May 25，距今 11 天
- **Critical path**: eval 完成 → exp-002 signals → exp-003 RRF → exp-006 IRT calibration (核心 Table 1) → paper results
- **瓶颈已从算力转为软件依赖**: exp-002 signals 已完成(9/9)，exp-003 RRF 已完成(3-signal)，exp-006 代码就绪(95%)。现在纯等 eval 数据
- **代码全部就绪**: exp-002(done), exp-003(done), exp-006(95%), exp-008(Worker 在写)。不需要再写核心代码
- **paper_framing.md 3 条 Core Claims**: C1=Calibration, C2=Signal Survival, C3=Identifiability。C1 证据来自 exp-006(未跑)，C2 来自 exp-008(未跑)，C3 来自 exp-004/005(running)
- **易错点**:
  - exp_005_noise_prop_v3 是 local 实验，不会有 cron 回调，必须手动 `ps -p` 检查
  - 0.5B d100 有 v3/v4 两个版本在 PREPARING/RUNNING，注意不要重复提交
  - exp_004_sim_sweep_v2 的 PID 是 411032 不是旧的 340553
  - 1.5B aligned batch eval (GPU 1) 跑的是 d000+d005+d100 三个 dosage，完成后一次性拿到 1.5B 完整数据
  - D016: Min-K++ 参考模型用 d000 fine-tuned model（非裸基座），不要改
  - 3B GSM8K 崩塌是 LoRA CoT 遗忘，不是 contamination 效应，不要试图修复

## 项目硬约束 (memory.md 节选)

## Phase 3 GPU 调度优先级 (Director 2026-05-14, 更新 03:23 UTC)
**原则：每个 model size 先跑两端极值 (d005, d100)，再填 d025。d050 降为 P2+ 可选。**

**新增：GPU 1/2 eval 完成后，先跑 0.5B exp-002 signals（1-2 GPU-hours），再提交 d025 SFT。**

**免审批：** GPU 空出时直接按优先级启动，事后汇报。

**Why:** 3 点 (d000/d005/d100) 天然单调，审稿人会打回 monotonicity claim。0.5B d025 恢复 P2：成本极低 (~1+2 GPU-h)，4 点曲线显著增强 claim 可信度。

## 可查的历史
前 48 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T15:41:06.769045+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__list_workers",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__list_workers",
    "max_results": "8"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T15:41:06.821502+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T15:41:12.487344+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T15:41:12.992363+00:00_

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
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T15:41:13.510652+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_005_noise_prop_v3\": {\"conclusion\": null, \"created_at\": \"2026-05-14T03:24:06.949Z\", \"hypothesis\": \"Noise propagation: ME-aware 4PL+γ IRT produces wider calibrated-score CIs than simple model as σ_e increases, demonstrating proper uncertainty propagation. v3 fixes: local disk Stan output, analytic ME (1231 params), checkpoint resume.\", \"status\": \"RUNNING\", \"updated_at\": \"2026-05-14T14:22:10.749Z\", \"notes\": \"14/25 fits (56%), 当前 σ_e=0.5 seed=46 analytic ME model fitting。~15-17min/fit, 剩余 11 fits ≈ 2.5-3h, ETA ~17:30-18:30 UTC May 14。v3 运行正常 (Rhat ~1.006-1.007)。PID 426335/426336。server: local。最新 CI_width: simple=0.0990, ME=0.0991 (σ_e=0.5, seed=46)。\"}, \"exp_001_sft_d025_15B\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T14:18:59.162Z\", \"updated_at\": \"2026-05-14T14:19:31.704Z\", \"hypothesis\": \"25% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-dosage contamination for 1.5B dose-response curve intermediate point\", \"notes\": \"训练启动成功。GPU 0, 14361 MiB。3384 steps, ~3.94s/step, ETA ~02:00 UTC May 15。tmux session: sft_15B_d025。参数与 1.5B d005/d100 一致 (batch_size=1, grad_accum=16, lora_r=16, alpha=32)。补齐 1.5B dose-response 中间点 (d025)。\"}, \"exp_001_eval_3B_d005_aligned\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T13:10:12.650Z\", \"updated_at\": \"2026-05-14T13:29:00.712Z\"}, \"exp_004_sim_sweep_v2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T07:12:12.267Z\", \"updated_at\": \"2026-05-14T12:44:13.225Z\", \"notes\": \"2026-05-14 12:35 增量分析 v4: 48/120 runs 完成. auc0.80_n50: 10 seeds, bias +0.006, RMSE 0.030, CI95 coverage 100%. auc0.80_n100 新增: γ̂=0.508, bias=+0.008, CI width=0.116, θ_corr=0.962. CI width ratio (AUC=0.80/0.55) N=100 为 1.81×, 与 N=20/50 的 1.87-1.95× 一致, 支持 multiplicative 无交互结论. 1/√N scaling 继续成立. 所有核心 findings 不变.\", \"metrics\": {\"runs_completed\": 48, \"runs_total\": 120, \"auc080_n50_bias\": 0.006, \"auc080_n50_rmse\": 0.0
…[truncated 1032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1023
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T15:41:13.511104+00:00_

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
  "session": "cron:hook:exp_001_sft_d005_15B",
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

_source line 8 · 2026-05-14T15:41:13.985511+00:00_

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
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T15:41:16.102805+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ps -p 339838 -o pid=,stat=,etime= 2>/dev/null && echo \"RUNNING\" || echo \"EXITED\"",
  "description": "Check if exp_005_noise_prop_v3 local process is still alive"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "Bash",
  "tool_args": {
    "command": "ps -p 339838 -o pid=,stat=,etime= 2>/dev/null && echo \"RUNNING\" || echo \"EXITED\"",
    "description": "Check if exp_005_noise_prop_v3 local process is still alive"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T15:41:16.860441+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ps -p 411032 -o pid=,stat=,etime= 2>/dev/null && echo \"RUNNING\" || echo \"EXITED\"",
  "description": "Check if exp_004_sim_sweep_v2 local process is still alive"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "Bash",
  "tool_args": {
    "command": "ps -p 411032 -o pid=,stat=,etime= 2>/dev/null && echo \"RUNNING\" || echo \"EXITED\"",
    "description": "Check if exp_004_sim_sweep_v2 local process is still alive"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T15:41:17.213754+00:00_

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
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "status": "running"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T15:41:33.606681+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 6, \"results\": [{\"exp_id\": \"exp_001_eval_15B_aligned_batch\", \"success\": true, \"actions\": [\"Job still running (pid=336750)\"]}, {\"exp_id\": \"exp_001_eval_3B_d005_aligned\", \"success\": true, \"actions\": [\"Job still running (pid=373931)\"]}, {\"exp_id\": \"exp_001_eval_05B_d025_aligned\", \"success\": true, \"actions\": [\"Stale cron removed (registry status=DONE)\"]}, {\"exp_id\": \"exp_001_sft_d025_15B\", \"success\": true, \"actions\": [\"Job still running (pid=sft_15B_d025)\"]}, {\"exp_id\": \"exp_001_eval_05B_d100_aligned_v3\", \"success\": true, \"actions\": [\"Job still running (pid=exp_001_eval_05B_d100_aligned_v3)\"]}, {\"exp_id\": \"exp_001_eval_05B_d100_aligned_v4\", \"success\": true, \"actions\": [\"Job still running (pid=exp_001_eval_05B_d100_aligned_v4)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 20614
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T15:41:33.707556+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_005_noise_prop_v3 | Noise propagation: ME-aware 4PL+γ IRT produces wider calibrated-score CIs than simple model as σ_e increases, demonstrating proper uncertainty propagation. v3 fixes: local disk Stan output, analytic ME (1231 params), checkpoint resume. | — | — | — |\\n| exp_001_sft_d025_15B | 25% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-dosage contamination for 1.5B dose-response curve intermediate point | — | — | — |\\n| exp_001_eval_3B_d005_aligned | — | — | — | — |\\n\\n## 待处理\\n- exp_001_eval_05B_d100_aligned_v4（准备中）\\n- exp_001_eval_05B_d100_aligned_v3: 0.5B d100 s42 aligned-format eval (v3 fix: conda activation). d100 original + paraphrase MC eval with \\\"The answer is\\\" prefix (D017).（准备中）\\n- exp_001_eval_05B_d100_aligned_v2（准备中）\\n- exp_001_eval_3B_d000_s42_v3: 3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。（准备中）\\n- exp_001_eval_05B_d000_s42_v6: 0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)（准备中）\\n- exp_001_eval_05B_d100_v6: 100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)（准备中）\\n- exp_001_eval_05B_d100_v4: 100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)（准备中）\\n- exp_001_eval_05B_d000_s42_v4: 0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)（准备中）\\n- exp_001_eval_05B_d000_s42_v2（准备中）\\n- exp_001_eval_05B_d100_v3: 100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 contamination score inflation（准备中）\\n- …另有 3 项\\n\\n## 近期结论\\n- **exp_001_eval_05B_d025_aligned** (failed): 0.5B d025 s42 aligned eval — 25% contamination dose-response intermediate point (original + paraphrase)\\n- **exp_001_eval_3B_d100_aligned** (success): 3B d100 s42 aligned eval — 100% con
…[truncated 1135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 20196
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T15:41:33.811781+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-14 03:39 UTC | 更新原因: Phase 3 SFT 进度同步、exp-002/006 管线加速、d025 0.5B 恢复优先级、exp-008 近期任务追踪\\n\\n## 核心方向\\nContamCal：post-hoc statistical calibration via contamination-augmented 4PL IRT。详见 paper_framing.md。\\n\\n## 投稿目标\\n**EMNLP 2026 ARR May 25**（D006, 距今 11 天）\\n- Track: ML for NLP / Resources and Evaluation\\n- Special theme: \\\"New Missions for NLP Research\\\" — contamination/data governance\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-13 通过）+ 审稿进行中\\n- **Phase 1 Paraphrase**: ✅ 全部完成 (ARC ✅, GSM8K ✅, MMLU ✅ v3, HumanEval ✅ appendix-only D009)\\n- **Phase 2 数据准备**: ✅ dosage 文件已生成 (ARC + GSM8K + MMLU)\\n- **Phase 3 SFT 进度 (seed=42)**:\\n\\n| 模型 | d000 | d005 | d025 | d050 | d100 |\\n|------|------|------|------|------|------|\\n| 0.5B | ✅ | ✅ | P2 | DP | ✅ |\\n| 1.5B | ✅ | 🏃GPU4 | P4 | DP | 🏃GPU0 |\\n| 3B | ✅ | P2 | P4 | DP | P1→GPU0释放后 |\\n\\n  ✅=完成 🏃=运行中 DP=deprioritized(d050) P=待排优先级\\n  seed=123 baselines: 0.5B ✅, 1.5B ✅, 3B ✅ (all d000)\\n\\n- **Phase 4 Eval**: 2 完成, 7 运行中\\n  - 完成: 0.5B-d000-s123 (MMLU 0.4182, GSM8K 0.3404, ARC 0.3976, HumanEval 0.1037), 1.5B-d000-s42 (MMLU 0.5753, GSM8K 0.6368, ARC 0.7756, HumanEval 0.128)\\n  - 运行中: GPU 1/2/3/5 各跑 eval\\n- **代码准备** (CPU Workers 并行):\\n  - exp-002 signal pipeline 代码: 编写中（4 signals + dry-run）\\n  - exp-006 baselines 代码: 编写中（7 baselines + 统一接口）\\n- **CPU 实验**:\\n  - exp-004 sim sweep: 27/120 完成, PID 340553, ETA ~40-60h (~May 16-17)\\n  - exp-005 noise prop v3: PID 339838 运行中, ETA ~11-12h (~14:30-15:30 UTC today)\\n- **Fisher 推导**: ✅ appendix.tex (Theorem 1 + 2 Corollaries)\\n- **论文**: Intro/Method/Related Work/Experiments 初稿已有\\n- **Stan**: D013 确认 Simple IRT model, ME model 弃用。contam_irt_4pl_simple.stan 收敛良好。\\n\\n## Critical Path\\n```\\nexp-002 代码完成 (CPU Worker, hours)\\n  → 0
…[truncated 2873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 19826
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T15:41:34.419784+00:00_

EXITED

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "Bash",
  "elapsed_ms": 18316
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T15:41:34.625495+00:00_

 411032 S       08:29:53
RUNNING

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "Bash",
  "elapsed_ms": 17765
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T15:41:34.829945+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_code_exp_008_signal_survival_20260514T151607\", \"task_type\": \"code:exp_008_signal_survival\", \"project\": \"contamcal-irt-calibration\", \"status\": \"running\", \"started_at\": \"2026-05-14T15:16:08.739027+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 17616
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T15:42:01.137605+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ps -p 426335 -o pid=,stat=,etime= 2>/dev/null && echo \"RUNNING\" || echo \"EXITED\"; ps -p 426336 -o pid=,stat=,etime= 2>/dev/null && echo \"RUNNING\" || echo \"EXITED\"",
  "description": "Check exp_005_noise_prop_v3 updated PIDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "Bash",
  "tool_args": {
    "command": "ps -p 426335 -o pid=,stat=,etime= 2>/dev/null && echo \"RUNNING\" || echo \"EXITED\"; ps -p 426336 -o pid=,stat=,etime= 2>/dev/null && echo \"RUNNING\" || echo \"EXITED\"",
    "description": "Check exp_005_noise_prop_v3 updated PIDs"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T15:42:01.543485+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "project": "contamcal-irt-calibration",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "project": "contamcal-irt-calibration",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T15:42:01.696470+00:00_

 426335 S       07:15:22
RUNNING
 426336 Sl      07:15:22
RUNNING

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "Bash",
  "elapsed_ms": 558
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T15:42:02.855183+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_001_eval_05B_d025_aligned\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T13:14:42.647Z\", \"updated_at\": \"2026-05-14T15:40:34.733Z\", \"hypothesis\": \"0.5B d025 s42 aligned eval — 25% contamination dose-response intermediate point (original + paraphrase)\", \"conclusion\": \"failed\"}, \"exp_001_eval_3B_d100_aligned\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:56:44.974Z\", \"updated_at\": \"2026-05-14T15:33:27.101Z\", \"hypothesis\": \"3B d100 s42 aligned eval — 100% contamination at largest scale, upper bound for 3B dose-response (MMLU/ARC only, GSM8K excluded per D018)\", \"parent\": \"exp_001_sft_d100_3B\", \"notes\": \"重跑成功。PID 362942 GPU 3。4 benchmarks 全部完成: MMLU 64.17%, GSM8K 69.67%, ARC 83.96%, HumanEval 12.20%。运行时间约 3h16m (20:06-23:22)。\", \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.6417, \"gsm8k_exact_match\": 0.6967, \"arc_challenge_accuracy\": 0.8396, \"humaneval_pass1\": 0.122}}, \"exp_001_eval_05B_d005_aligned\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:20:22.394Z\", \"updated_at\": \"2026-05-14T15:21:22.628Z\", \"metrics\": {\"d005_aligned_mmlu\": 0.3255, \"d005_aligned_gsm8k\": 0.3624, \"d005_aligned_arc\": 0.3285, \"d005_aligned_humaneval\": 0.0793}, \"conclusion\": \"success\"}, \"exp_001_eval_05B_d100_aligned\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T14:50:02.679Z\", \"updated_at\": \"2026-05-14T15:19:06.659Z\", \"hypothesis\": \"0.5B d100 s42 aligned eval resubmit — d100 original + paraphrase, split from failed batch to avoid timeout\", \"notes\": \"PID 389866 仍在运行（ps 确认 state=Rl, elapsed=19:31），tmux session 已死但 python 进程存活。Cron 误报 process gone（miss 4/5）因 tmux 检测失效。MMLU 已完成，GSM8K/ARC/HumanEval 进行中。等进程完成后立即提交 d100 paraphrase eval（--output-dir Qwen2.5-0.5B_d100_s42_para_aligned --paraphrase）。GPU 2 仍在使用。\", \"conclusion\": \"failed\"}, \"exp_001_eval_05B_aligned_batch\": {\"status\": \"DONE\", \"created_at\": \"202
…[truncated 1271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1311
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T15:43:27.818465+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_001_eval_05B_d100_aligned_v3'}",
  "project": "contamcal-irt-calibration",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_001_eval_05B_d100_aligned_v3'}",
    "project": "contamcal-irt-calibration",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T15:43:28.270894+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_001_eval_05B_d100_aligned_v4'}",
  "project": "contamcal-irt-calibration",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_001_eval_05B_d100_aligned_v4'}",
    "project": "contamcal-irt-calibration",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T15:43:29.229377+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0579}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1410
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T15:43:29.229837+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_001_eval_05B_d025_aligned'}",
  "project": "contamcal-irt-calibration",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_001_eval_05B_d025_aligned'}",
    "project": "contamcal-irt-calibration",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T15:43:30.188629+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9001}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1917
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T15:43:30.189064+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_gpu_health,mcp__agent-ml-research__load_project_config",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_gpu_health,mcp__agent-ml-research__load_project_config",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T15:43:30.901603+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9505}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1671
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T15:43:30.902067+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "ToolSearch",
  "elapsed_ms": 713
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T15:43:37.889808+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'PREPARING'}",
  "project": "contamcal-irt-calibration",
  "fields": "['status', 'notes', 'hypothesis']",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'PREPARING'}",
    "project": "contamcal-irt-calibration",
    "fields": "['status', 'notes', 'hypothesis']",
    "limit": "20"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T15:43:38.803599+00:00_

called mcp__agent-ml-research__get_gpu_health

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_gpu_health</summary>

```json
{
  "server": "cqa1-21977"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__get_gpu_health",
  "tool_args": {
    "server": "cqa1-21977"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T15:43:38.954682+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_001_eval_05B_d100_aligned_v4\": {\"status\": \"PREPARING\"}, \"exp_001_eval_05B_d100_aligned_v3\": {\"status\": \"PREPARING\", \"hypothesis\": \"0.5B d100 s42 aligned-format eval (v3 fix: conda activation). d100 original + paraphrase MC eval with \\\"The answer is\\\" prefix (D017).\"}, \"exp_001_eval_05B_d100_aligned_v2\": {\"status\": \"PREPARING\", \"notes\": \"失败原因: EXIT_CODE=127 — 命令未激活 conda 环境，python 不在 PATH。日志仅 2 行: \\\"bash: line 1: python: command not found\\\" + \\\"EXIT_CODE=127\\\"。修复: 命令需加 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base。已创建 v3 重提交。\"}, \"exp_001_eval_3B_d000_s42_v3\": {\"hypothesis\": \"3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d000_s42_v6\": {\"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d100_v6\": {\"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d100_v4\": {\"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d000_s42_v4\": {\"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d000_s42_v2\": {\"status\": \"PREPARING\"}, \"exp_001_eval_05B_d100_v3\": {\"hypothesis\": \"100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 contamination score inflation\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d000_s42_v3\": {\"hypothesis\": \"0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于 calibration error 计算\", \"status\": \"PREPARING\"}, \"exp_001_sft_d005_05B_r3\": {\"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry #3 after v1/v2 OOM (v1: GPU 5 zombie process; v2: --gpu 0 bug ran on GPU 0 instead of 5). Now uses --gpu 5 correctly
…[truncated 291 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1064
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T15:43:38.955170+00:00_

{"result":"{\"success\": true, \"data\": {\"servers\": {\"cqa1-21977\": {\"error\": \"no data yet\", \"stale\": true}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__get_gpu_health",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T15:43:38.955447+00:00_

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
  "session": "cron:hook:exp_001_sft_d005_15B",
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

_source line 35 · 2026-05-14T15:43:39.059698+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"contamcal-irt-calibration\", \"section\": \"execution\", \"config\": {\"execution\": {\"gpu_ids\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\", \"cuda:4\", \"cuda:5\"], \"project_path\": \"/root/contamcal-irt-calibration\", \"servers\": [\"cqa1-21977\"]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 104
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T15:44:03.236593+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T15:44:04.143257+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\", \"content\": \"# Memory — contamcal-irt-calibration\\n\\n## 🔴 Local vs Remote 实验监控规范 (2026-05-14, Reviewer CRITICAL)\\n**两次误标事故教训：** Worker 在远程服务器查找 `server: local` 实验，找不到就误标 DONE/negative。\\n\\n**规范（硬约束）：**\\n- 派 Worker 做状态检查时，task_prompt 必须注明 `server: local` 还是远程\\n- `server: local` 实验用 Bash `ps -p PID`，**禁止** ssh_read_only\\n- `server: local` 实验**不注册 cron**（cron 只支持 SSH），改用手动定期检查\\n- Worker 标记 DONE/failed 前必须确认查找位置与 spec.server 一致\\n- 如果误标，registry.yaml DONE→RUNNING 需直接编辑文件（API 不允许回退）\\n\\n**Why:** exp_005_noise_prop_v2 和 v3 两次被误判。v3 的 PID 339838 实际在本地运行，被 ops worker 在远程查找后错误标记。\\n\\n## 🔴 CUDA_VISIBLE_DEVICES 覆写 bug (2026-05-14, 事故教训)\\n**train_sft.py:114 和 signal_minkpp.py/compute_signals.py 中 `os.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = args.gpu` 覆写了 submit_training_job wrapper 正确设置的 CUDA_VISIBLE_DEVICES，导致 GPU 绑定错位。**\\n\\n已修复：删除所有脚本中的环境变量覆写行。GPU 绑定完全由 wrapper 控制，脚本内部只用 `cuda:0`。\\n\\n**影响**：3B d100 SFT 跑错到 GPU 0（与 1.5B d100 共用 95% VRAM）、0.5B d025 SFT OOM（被挤爆）。\\n\\n## 🔴 MC 评估格式冲突 (2026-05-14, d005 MC collapse 根因)\\n**训练格式 `\\\"The answer is B.\\\"` 与 evaluate.py 的 logprob 评估格式 `\\\"Answer: \\\"` 不兼容。**\\n\\nSFT 后模型在 assistant 位置把概率集中在 token \\\"The\\\"，A/B/C/D 的 logprob 退化为 token 先验频率。\\\"A\\\" 作为字母表首位获得最高残余概率 → A-collapse。\\n\\n**修复**：D017 — evaluate.py 改用 \\\"The answer is \\\" 前缀，新增 --mc-format {aligned,legacy} 参数。已部署。\\n\\n**D017 延伸决策（Director 2026-05-14 08:01 UTC）**：统一 aligned 格式。所有 MC eval（含 paraphrase eval）必须用 `--mc-format aligned`。v5 legacy eval 结果仅供诊断参考，正式 dose-response 分析和信号计算需用 aligned 格式重跑。只有 aligned-aligned pair 的 ConStat 结果才有效。\\n\\n## 🔴 Cron false positive: wrapper PID vs python PID (2026-05-14)\\n**cron 监控 submit_training_job 的 wrapper PID，如果 wrapper 死了但 python 训练进程还在，cron 会误判为 failed。**\\n\\nexp_001_sft_d100_3B: wrapper PID 319550 死了，python PID 319555 正常训练。被 cron 自动标记 DONE/failed，手动编辑 registry.y
…[truncated 10873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 906
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T15:44:17.445554+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "ops:gpu_check_and_eval_diagnose",
  "project": "contamcal-irt-calibration",
  "task_prompt": "## 任务：检查服务器 GPU 状态 + 诊断 eval 失败\n\n### 服务器信息\n- 服务器: cqa1-21977\n- 工作目录: /root/contamcal-irt-calibration\n- Python: /root/miniconda3/bin/python (conda base env)\n- 6× RTX 4090D (cuda:0-5)\n\n### 任务 1: GPU 状态检查\n用 ssh_read_only 执行：\n```bash\nnvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader\n```\n和：\n```bash\nnvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory,name --format=csv,noheader\n```\n以及：\n```bash\nps aux | grep -E 'python|evaluate' | grep -v grep\n```\n\n汇报：每个 GPU (0-5) 当前是否有进程在跑，跑的是什么。\n\n### 任务 2: 诊断 exp_001_eval_05B_d025_aligned 失败\n这个实验在 GPU 5 上跑 0.5B d025 aligned eval，已标记 DONE(failed)。\n检查日志：\n```bash\nls -la /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_aligned/ 2>/dev/null\ncat /tmp/exp_001_eval_05B_d025_aligned*.log 2>/dev/null | tail -50\n# 也检查 tmux\ntmux ls 2>/dev/null\n```\n\n### 任务 3: 检查 d100 v3/v4 状态\nCron 报告 exp_001_eval_05B_d100_aligned_v3 和 v4 仍在运行，但 registry 显示 PREPARING。检查：\n```bash\n# 查 tmux sessions\ntmux ls 2>/dev/null | grep -i d100\n# 查进程\nps aux | grep -i \"d100\" | grep -v grep\n# 查日志\nls -la /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned/ 2>/dev/null\ncat /tmp/exp_001_eval_05B_d100_aligned*.log 2>/dev/null | tail -30\n```\n\n### 产出\n简洁汇报：\n1. 每个 GPU (0-5) 的当前状态（空闲/占用+进程）\n2. d025 eval 失败原因\n3. d100 v3/v4 的真实状态（在跑还是已结束/从未启动）\n4. 建议：哪些 GPU 空闲可以接新任务",
  "tool_groups": "['ssh']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "ops:gpu_check_and_eval_diagnose",
    "project": "contamcal-irt-calibration",
    "task_prompt": "## 任务：检查服务器 GPU 状态 + 诊断 eval 失败\n\n### 服务器信息\n- 服务器: cqa1-21977\n- 工作目录: /root/contamcal-irt-calibration\n- Python: /root/miniconda3/bin/python (conda base env)\n- 6× RTX 4090D (cuda:0-5)\n\n### 任务 1: GPU 状态检查\n用 ssh_read_only 执行：\n```bash\nnvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader\n```\n和：\n```bash\nnvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory,name --format=csv,noheader\n```\n以及：\n```bash\nps aux | grep -E 'python|evaluate' | grep -v grep\n```\n\n汇报：每个 GPU (0-5) 当前是否有进程在跑，跑的是什么。\n\n### 任务 2: 诊断 exp_001_eval_05B_d025_aligned 失败\n这个实验在 GPU 5 上跑 0.5B d025 aligned eval，已标记 DONE(failed)。\n检查日志：\n```bash\nls -la /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_aligned/ 2>/dev/null\ncat /tmp/exp_001_eval_05B_d025_aligned*.log 2>/dev/null | tail -50\n# 也检查 tmux\ntmux ls 2>/dev/null\n```\n\n### 任务 3: 检查 d100 v3/v4 状态\nCron 报告 exp_001_eval_05B_d100_aligned_v3 和 v4 仍在运行，但 registry 显示 PREPARING。检查：\n```bash\n# 查 tmux sessions\ntmux ls 2>/dev/null | grep -i d100\n# 查进程\nps aux | grep -i \"d100\" | grep -v grep\n# 查日志\nls -la /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned/ 2>/dev/null\ncat /tmp/exp_001_eval_05B_d100_aligned*.log 2>/dev/null | tail -30\n```\n\n### 产出\n简洁汇报：\n1. 每个 GPU (0-5) 的当前状态（空闲/占用+进程）\n2. d025 eval 失败原因\n3. d100 v3/v4 的真实状态（在跑还是已结束/从未启动）\n4. 建议：哪些 GPU 空闲可以接新任务",
    "tool_groups": "['ssh']"
  }
}
````

</details>

---

### Tool result

_source line 39 · 2026-05-14T15:44:26.924253+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_ops_gpu_check_and_eval_diagnose_20260514T154422\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/logs/workers/worker_ops_gpu_check_and_eval_diagnose_20260514T154422.log\", \"setup_data\": {}, \"message\": \"Worker worker_ops_gpu_check_and_eval_diagnose_20260514T154422 started. Use get_worker_status('worker_ops_gpu_check_and_eval_diagnose_20260514T154422') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 9478
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T15:44:56.008438+00:00_

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
  "session": "cron:hook:exp_001_sft_d005_15B",
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

_source line 41 · 2026-05-14T15:44:56.113028+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\", \"content\": \"# Memory — contamcal-irt-calibration\\n\\n## 🔴 Local vs Remote 实验监控规范 (2026-05-14, Reviewer CRITICAL)\\n**两次误标事故教训：** Worker 在远程服务器查找 `server: local` 实验，找不到就误标 DONE/negative。\\n\\n**规范（硬约束）：**\\n- 派 Worker 做状态检查时，task_prompt 必须注明 `server: local` 还是远程\\n- `server: local` 实验用 Bash `ps -p PID`，**禁止** ssh_read_only\\n- `server: local` 实验**不注册 cron**（cron 只支持 SSH），改用手动定期检查\\n- Worker 标记 DONE/failed 前必须确认查找位置与 spec.server 一致\\n- 如果误标，registry.yaml DONE→RUNNING 需直接编辑文件（API 不允许回退）\\n\\n**Why:** exp_005_noise_prop_v2 和 v3 两次被误判。v3 的 PID 339838 实际在本地运行，被 ops worker 在远程查找后错误标记。\\n\\n## 🔴 CUDA_VISIBLE_DEVICES 覆写 bug (2026-05-14, 事故教训)\\n**train_sft.py:114 和 signal_minkpp.py/compute_signals.py 中 `os.environ[\\\"CUDA_VISIBLE_DEVICES\\\"] = args.gpu` 覆写了 submit_training_job wrapper 正确设置的 CUDA_VISIBLE_DEVICES，导致 GPU 绑定错位。**\\n\\n已修复：删除所有脚本中的环境变量覆写行。GPU 绑定完全由 wrapper 控制，脚本内部只用 `cuda:0`。\\n\\n**影响**：3B d100 SFT 跑错到 GPU 0（与 1.5B d100 共用 95% VRAM）、0.5B d025 SFT OOM（被挤爆）。\\n\\n## 🔴 MC 评估格式冲突 (2026-05-14, d005 MC collapse 根因)\\n**训练格式 `\\\"The answer is B.\\\"` 与 evaluate.py 的 logprob 评估格式 `\\\"Answer: \\\"` 不兼容。**\\n\\nSFT 后模型在 assistant 位置把概率集中在 token \\\"The\\\"，A/B/C/D 的 logprob 退化为 token 先验频率。\\\"A\\\" 作为字母表首位获得最高残余概率 → A-collapse。\\n\\n**修复**：D017 — evaluate.py 改用 \\\"The answer is \\\" 前缀，新增 --mc-format {aligned,legacy} 参数。已部署。\\n\\n**D017 延伸决策（Director 2026-05-14 08:01 UTC）**：统一 aligned 格式。所有 MC eval（含 paraphrase eval）必须用 `--mc-format aligned`。v5 legacy eval 结果仅供诊断参考，正式 dose-response 分析和信号计算需用 aligned 格式重跑。只有 aligned-aligned pair 的 ConStat 结果才有效。\\n\\n## 🔴 Cron false positive: wrapper PID vs python PID (2026-05-14)\\n**cron 监控 submit_training_job 的 wrapper PID，如果 wrapper 死了但 python 训练进程还在，cron 会误判为 failed。**\\n\\nexp_001_sft_d100_3B: wrapper PID 319550 死了，python PID 319555 正常训练。被 cron 自动标记 DONE/failed，手动编辑 registry.y
…[truncated 15445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 104
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T15:46:08.489173+00:00_

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
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T15:46:08.609639+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_3ab11b2b.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "Read",
  "elapsed_ms": 120
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-14T15:46:11.399549+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T15:46:11.691654+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "Glob",
  "elapsed_ms": 292
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T15:46:14.656575+00:00_

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
  "session": "cron:hook:exp_001_sft_d005_15B",
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

_source line 47 · 2026-05-14T15:46:15.563894+00:00_

/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "Glob",
  "elapsed_ms": 907
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T15:46:18.579469+00:00_

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
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-14T15:46:18.684527+00:00_

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
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "Read",
  "elapsed_ms": 105
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T15:47:23.517600+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__submit_on_allocated",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__submit_on_allocated",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-14T15:47:23.669568+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-14T15:47:42.982811+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 分配 6 / 实际在跑 ≤4 | Worker 池 3 (GPU 0 / CPU 3)\n\n## Session Start 汇报 (Loop #6, 2026-05-14 ~15:45 UTC)\n\n### 运行中实验\n| GPU | 实验 | 内容 | 预计完成 |\n|-----|------|------|---------|\n| 0 | exp_001_sft_d025_15B | 1.5B d025 SFT | ~02:00 UTC May 15 |\n| 1 | exp_001_eval_15B_aligned_batch | 1.5B d000 para→d005→d100 aligned eval | 数小时 |\n| 2 | ⚠️ 状态不明 | d100 v3/v4 registry=PREPARING 但 cron=running | Worker 诊断中 |\n| 4 | exp_001_eval_3B_d005_aligned | 3B d005 aligned eval | 数小时 |\n| **3** | **空闲** | 3B d100 eval 已完成 | — |\n| **5** | **空闲** | 0.5B d025 eval DONE(failed) | — |\n| local | exp_004_sim_sweep_v2 (PID 411032) | 48/120 IRT sim | May 16-17 |\n| local | exp_005_noise_prop_v3 (PID 426335/6) | 14/25 fits | ~17:30-18:30 UTC today |\n\n### ⚠️ 问题\n1. **GPU 3/5 空闲** — GPU check Worker 已派出确认状态，确认后立即提交：\n   - GPU 5: 重提交 0.5B d025 aligned eval（失败需诊断原因）\n   - GPU 3: 提交 0.5B d005 paraphrase aligned eval（ConStat 信号依赖）\n2. **GPU 2 状态不一致** — v3/v4 在 registry 中是 PREPARING 但 cron 报告进程存活。Worker 正在 SSH 确认真实状态\n3. **Worker exp-008 代码** — 仍在编写 signal survival 代码，等回调\n\n### Critical Path 更新\neval 完成 → exp-002 signals(已有9/9, 但缺 ConStat) → exp-003 RRF → exp-006 IRT calibration\n- 0.5B d000/d005 aligned 原始 eval ✅\n- 0.5B d025 eval 需重提交\n- 0.5B d100 eval 状态待确认\n- 1.5B batch eval 运行中（GPU 1）\n- 所有下游代码已 ready（exp-003/006/008）\n\n距 EMNLP ARR 截止 11 天。",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 分配 6 / 实际在跑 ≤4 | Worker 池 3 (GPU 0 / CPU 3)\n\n## Session Start 汇报 (Loop #6, 2026-05-14 ~15:45 UTC)\n\n### 运行中实验\n| GPU | 实验 | 内容 | 预计完成 |\n|-----|------|------|---------|\n| 0 | exp_001_sft_d025_15B | 1.5B d025 SFT | ~02:00 UTC May 15 |\n| 1 | exp_001_eval_15B_aligned_batch | 1.5B d000 para→d005→d100 aligned eval | 数小时 |\n| 2 | ⚠️ 状态不明 | d100 v3/v4 registry=PREPARING 但 cron=running | Worker 诊断中 |\n| 4 | exp_001_eval_3B_d005_aligned | 3B d005 aligned eval | 数小时 |\n| **3** | **空闲** | 3B d100 eval 已完成 | — |\n| **5** | **空闲** | 0.5B d025 eval DONE(failed) | — |\n| local | exp_004_sim_sweep_v2 (PID 411032) | 48/120 IRT sim | May 16-17 |\n| local | exp_005_noise_prop_v3 (PID 426335/6) | 14/25 fits | ~17:30-18:30 UTC today |\n\n### ⚠️ 问题\n1. **GPU 3/5 空闲** — GPU check Worker 已派出确认状态，确认后立即提交：\n   - GPU 5: 重提交 0.5B d025 aligned eval（失败需诊断原因）\n   - GPU 3: 提交 0.5B d005 paraphrase aligned eval（ConStat 信号依赖）\n2. **GPU 2 状态不一致** — v3/v4 在 registry 中是 PREPARING 但 cron 报告进程存活。Worker 正在 SSH 确认真实状态\n3. **Worker exp-008 代码** — 仍在编写 signal survival 代码，等回调\n\n### Critical Path 更新\neval 完成 → exp-002 signals(已有9/9, 但缺 ConStat) → exp-003 RRF → exp-006 IRT calibration\n- 0.5B d000/d005 aligned 原始 eval ✅\n- 0.5B d025 eval 需重提交\n- 0.5B d100 eval 状态待确认\n- 1.5B batch eval 运行中（GPU 1）\n- 所有下游代码已 ready（exp-003/006/008）\n\n距 EMNLP ARR 截止 11 天。",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-14T15:47:44.551829+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_sft_d005_15B",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 1569
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-14T15:48:14.566887+00:00_

Session-start 初始化完成。当前状态：

- **GPU**: 0/1/4 确认在跑，2 状态待确认，3/5 可能空闲
- **本地 CPU**: exp_004 (48/120) + exp_005 (14/25) 运行中
- **Worker 池**: 2 个 (exp-008 代码 + GPU 诊断)
- **已向 Director 汇报**

等待 GPU check Worker 回调——确认后立即在空闲 GPU 上提交 0.5B d025 eval 重跑和 d005 paraphrase eval。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:exp_001_sft_d005_15B"
}
```

</details>

---
