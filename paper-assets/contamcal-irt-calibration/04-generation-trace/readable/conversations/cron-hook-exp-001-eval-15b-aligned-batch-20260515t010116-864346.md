# cron hook exp 001 eval 15B aligned batch 20260515T010116 864346

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 62
- **Recorded user turns:** 2
- **Tool calls:** 29
- **Original source:** `logs/chats/archive/cron_hook_exp_001_eval_15B_aligned_batch_20260515T010116_864346.jsonl`
- **Structured JSON:** [`63906e7587d1555da13c.json`](../../sessions/63/63906e7587d1555da13c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

36 recorded events

### User

_source line 1 · 2026-05-14T21:50:00.253392+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #7。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0-5 on cqa1-21977，全部分配给本项目，不可用其他服务器/卡
- submit_training_job 命令必须自带环境激活（`source /root/miniconda3/bin/activate && ...`），不假设 .venv
- GPU 编号脚本内始终从 0 开始（框架自动注入 CUDA_VISIBLE_DEVICES）
- MC eval 格式统一用 aligned（D017 "The answer is" 前缀），不要用 legacy 格式
- Min-K++ 参考模型必须用 0% dosage fine-tuned model（D016），不是裸基座
- exp-006 IRT：MMLU 必须子采样 1000 items（D023），GSM8K/ARC 直接 NUTS
- 距 EMNLP ARR May 25 截稿仅 11 天

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，account: root，6× RTX 4090D
- 工作目录：/root/contamcal-irt-calibration
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型路径：/root/autodl-tmp/exp001/ 下按 model/dosage 组织（Qwen2.5-0.5B/1.5B/3B）
- eval 结果：/root/autodl-tmp/exp001/eval_results/ 下按 model 组织
- Stan 代码：项目 repo 内 stan/ 目录
- 活跃进程（截至 18:43 UTC）：
  - cuda:2: exp002-signal-d025-05B (PID 422128)
  - cuda:3: exp_006_irt_05B_gsm8k (PID 418705, Stan NUTS CPU 为主)
  - cuda:4: exp_001_eval_15B_d025_aligned (PID 420905)
  - cuda:5: exp_001_sft_3B_d000_v2 (PID 405515) + exp_001_eval_05B_d025_aligned_v2 (PID 406017)
  - local CPU: exp_004_sim_sweep_v2 (PID 559605) + exp_005_noise_prop_v3 (PID 559666)
  - cuda:0, cuda:1: 空闲（需立即填充）

### 3. 📊 当前状态
收到 exp_001_eval_15B_aligned_batch CRON 回调（进程正常退出，ANALYZING）。已派两个 Worker：
1. **worker_analyze_exp_001_eval_15B_aligned_batch_20260514T184520**：SSH 分析完整 eval 结果（d000/d005/d100 × orig+para × 4 benchmarks）
2. **worker_gpu-check_idle-fill_20260514T184645**：检查实际 GPU 状态，确认 cuda:0/1 空闲

两个 Worker 均未返回（MCP 断连前已 spawn）。**下一个 session 必须先检查这两个 Worker 的状态/产出**，若已完成则处理结果，若丢失则重新 spawn。

Registry 已知 d000 aligned 部分 metrics：MMLU=58.53%, GSM8K=65.43%, ARC=77.22%, HumanEval=12.80%。完整 d005/d100 + paraphrase 数据待 Worker 提取。

未向 Director 汇报此次 CRON 回调（Worker 结果未返回即断连）。

### 4. 📋 待办
- Worker 分析结果返回 → 整理完整 metrics 表 → update_registry(conclusion=success/negative) → 更新 report.md → 向 Director 汇报（带 [资源] 行）
- Worker GPU 检查返回 → 确认 cuda:0/1 空闲 → 从 QUEUED/PREPARING 中选实验填充（优先 exp_001_sft_d100_3B_v2 QUEUED）
- Worker 丢失（MCP 断连导致） → 重新 spawn 相同任务
- exp_001_eval_15B_aligned_batch 若 success → 检查 experiment-matrix 覆盖率，1.5B scale dose-response 数据点补齐情况
- exp_001_eval_15B_aligned_batch 若 d005 paraphrase gap 显著 → 强化 C1 claim（low-dose detectable），加速 3B 同类 eval
- cuda:0/1 确认空闲 → 3B d100 SFT（P1 优先）+ exp_001_sft_d100_3B_v2（QUEUED）或 3B eval 系列
- exp_006_irt_05B_gsm8k 完成 → 验证 NUTS 在 GSM8K 上可行性（D023/D024 关键路径）
- CPU 实验 exp-004/005 完成 → 更新 registry + 检查断点续跑进度

### 5. 🎯 战略上下文
- **核心方向**：ContamCal = post-hoc statistical calibration via contamination-augmented 4PL IRT。Paper framing 见 paper_framing.md
- **C2 重构（D022）**："method-specific, scale-dependent signal effectiveness"，exp-008 v4 PASS，Min-K++ 反向效应是新发现
- **D023 关键瓶颈**：Stan NUTS 对 MMLU 56K params 不可行，分层策略已定（GSM8K/ARC 直接 NUTS + MMLU 子采样 1000 + ADVI fallback）。exp_006_irt_05B_gsm8k 正在验证 GSM8K NUTS 可行性——这是 critical path
- **D024**：GSM8K 作负对照、N_models=4 不可行需跨 scale 池化、MC benchmark 限制
- **SFT 矩阵**：0.5B 大部分完成，1.5B 正在补 d025/eval，3B 最缺（d000 v2 在重训，d100 未开始）
- **易错点**：
  - 不要混淆 legacy eval 和 aligned eval 的 metrics（aligned 用 D017 前缀，数值通常略高）
  - 3B 模型 GSM8K 崩塌是 LoRA SFT CoT 遗忘（D018），已排除出 dose-response 分析
  - d005 存在 position bias confound（D019），分析时注意区分真 contamination signal 和 format artifact
  - "scale-dependent" claim 目前仅有 0.5B 证据，1.5B/3B 数据是补齐关键——本次 1.5B batch eval 结果直接影响此 claim 可信度

## 可查的历史
前 56 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T21:50:27.841566+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_registry,reconcile_crons,read_project_file,read_roadmap",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_registry,reconcile_crons,read_project_file,read_roadmap",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T21:50:27.892362+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T21:50:31.554491+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "registry read experiment",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "registry read experiment",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T21:50:31.755735+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "ToolSearch",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T21:50:35.740810+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__list_available_gpus",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__get_project_resource_usage,mcp__agent-ml-research__list_available_gpus",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T21:50:35.844645+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "ToolSearch",
  "elapsed_ms": 103
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T21:50:40.392553+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T21:50:42.726151+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_005_noise_prop_v3\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T03:24:06.949Z\", \"hypothesis\": \"Noise propagation: ME-aware 4PL+γ IRT produces wider calibrated-score CIs than simple model as σ_e increases, demonstrating proper uncertainty propagation. v3 fixes: local disk Stan output, analytic ME (1231 params), checkpoint resume.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T21:50:34.523Z\", \"notes\": \"PID 559666 crashed (~10h ago). 22/25 fits completed. Restarting as v4.\"}, \"exp_004_sim_sweep_v2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T07:12:12.267Z\", \"updated_at\": \"2026-05-14T21:50:24.085Z\", \"notes\": \"重启 with --parallel 2 --chains-parallel 2, PID=599560, 53/120 runs 已完成 (6 conditions done/partial), 剩余 67 runs across 8 conditions. 脚本已改造支持 --parallel N 和 --chains-parallel N. 2核机器, 并行度有限.\", \"metrics\": {\"runs_completed\": 48, \"runs_total\": 120, \"auc080_n50_bias\": 0.006, \"auc080_n50_rmse\": 0.03, \"auc080_n50_ci95_coverage\": 1, \"auc080_n100_gamma_hat\": 0.508, \"auc080_n100_bias\": 0.008, \"auc080_n100_ci_width\": 0.116, \"auc080_n100_theta_corr\": 0.962, \"ci_width_ratio_n100\": 1.81, \"core_findings_stable\": true}, \"conclusion\": \"failed\"}, \"exp_001_eval_05B_d100_s123_aligned\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T21:31:14.591Z\", \"updated_at\": \"2026-05-14T21:31:39.554Z\", \"parent\": \"exp_001_sft_05B_d100_s123\", \"hypothesis\": \"0.5B d100 s123 aligned eval — multi-seed dosage-100 eval for IRT calibration.\"}, \"exp_001_sft_05B_d100_s123\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:17:25.569Z\", \"updated_at\": \"2026-05-14T21:30:33.304Z\", \"conclusion\": \"success\"}, \"exp_001_sft_d100_3B_v2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T18:25:23.780Z\", \"updated_at\": \"2026-05-14T21:13:03.187Z\", \"hypothesis\": \"3B d100 SFT v2 with D020 conservative params (lr=5e-5, alpha=16, 
…[truncated 45811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2333
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T21:50:47.812590+00:00_

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T21:50:48.215825+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 403
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T21:50:51.757946+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "report.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "report.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T21:50:51.911000+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_001_eval_05B_d100_s123_aligned | 0.5B d100 s123 aligned eval — multi-seed dosage-100 eval for IRT calibration. | — | — | — |\\n| exp_001_sft_d100_3B_v2 | 3B d100 SFT v2 with D020 conservative params (lr=5e-5, alpha=16, r=16) to prevent CoT catastrophic forgetting. seed=42. | — | — | — |\\n| exp002-signals-1p5B | — | — | — | — |\\n\\n## 待处理\\n- exp_003_mmlu_item_aligned_gap（准备中）\\n- exp006-gsm8k-d024-delta（准备中）\\n- exp_006_irt_05B_v2: Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 items + ADVI robustness check. Fixes v1 issues: aligned-only, signal-derived exposure, --max-items.（准备中）\\n- exp_008_instruct_rl_proxy: RL proxy experiment (D021 Problem 3): Use Qwen2.5-0.5B-Instruct (SFT+RL post-trained) as RL regime data point. 3-regime comparison: base (pretrained) → d000 (SFT) → Instruct (SFT+RL). Compute all 4 signals on Instruct model, observe signal value changes across training regimes. No additional training needed.\\\"（准备中）\\n- exp_001_eval_05B_d100_aligned_v2（准备中）\\n- exp_001_eval_3B_d000_s42_v3: 3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。（准备中）\\n- exp_001_eval_05B_d000_s42_v6: 0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)（准备中）\\n- exp_001_eval_05B_d100_v6: 100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)（准备中）\\n- exp_001_eval_05B_d100_v4: 100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)（准备中）\\n- exp_001_eval_05B_d000_s42_v4: 0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)（准备中）\\n- …另有 5 项\\n\\n## 近期结论\\n- **exp_004_sim_sweep_v2** (failed): —\\n- **exp_005_noise_prop_v3** (failed): Noise propagation: ME-aware 4PL+γ IRT produces wider calibrated-score CIs than simple model 
…[truncated 1316 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 153
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T21:50:54.884557+00:00_

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T21:50:55.082774+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-14 20:54 UTC | 更新原因: Reviewer #24: 更正 1.5B d025 eval 非卡死(HumanEval阶段), 更新 SFT 进度百分比, 1.5B d025 SFT 完成\\n\\n## 核心方向\\nContamCal：post-hoc statistical calibration via contamination-augmented 4PL IRT。详见 paper_framing.md。\\n\\n## 投稿目标\\n**EMNLP 2026 ARR May 25**（D006, 距今 11 天）\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-13 通过）+ 审稿进行中\\n- **P0 delta exposure fix**: ✅\\n- **D028**: exp_006_pooled_gsm8k_v1 INVALID（混合曝光尺度）\\n- **ARC 0.5B**: gamma=-1.87，负方向，支持 scale-dependent framing\\n- **新约束**: pooled IRT 仅在所有 scale 有同源 signal-derived exposure 时有效\\n- **关键发现**: 0.5B 污染导致退化（MMLU -16.5pp），1.5B 近乎免疫（<1pp），完美支撑 scale-dependent narrative\\n\\n**SFT 进度 (seed=42)**:\\n\\n| 模型 | d000 | d005 | d025 | d100 |\\n|------|------|------|------|------|\\n| 0.5B | ✅ | ✅ | ❌(2x fail) | ✅ |\\n| 1.5B | ✅ | ✅ | ✅ | ✅ |\\n| 3B | ✅(v2) | P2 | P4 | 🏃(v2, 51%, ~2.4h) |\\n\\n**SFT 进度 (seed=123)**:\\n\\n| 模型 | d000 | d005 | d025 | d100 |\\n|------|------|------|------|------|\\n| 0.5B | ✅(v1) | — | — | 🏃(GPU 1, 42%, ~41min) |\\n| 1.5B | ✅(v1) | — | — | 🏃(GPU 2, 10%, ~3.8h) |\\n| 3B | 🏃(v2, GPU 5, 11%) | — | — | — |\\n\\n**Eval 进度 (aligned)**:\\n\\n| 模型 | d000 | d005 | d025 | d100 |\\n|------|------|------|------|------|\\n| 0.5B | ✅ | ✅ | — | ✅(v4) |\\n| 1.5B | ✅ | ✅ | 🏃(GPU4, HumanEval阶段, ~12min) | ✅ |\\n| 3B | ⚠️v2 eval待安排 | P2 | — | ✅(para done) |\\n\\n**Signal (exp-002)**: 0.5B ✅ | 1.5B 🏃(GPU 0, 5/12 tasks, ~3-4h) | 3B 未开始\\n**CPU**: exp-004 v2 48/120 (40%) | exp-005 v3 14/25 (56%)\\n\\n## Critical Path\\n```\\n✅ P0 fix → ✅ cross-scale pooling 代码\\n→ 修复 compute_ground_truth + D018 死代码 (Agent 队列中)\\n  → 等 1.5B signals 完成 (~3-4h) → 0.5B+1.5B pooled IRT\\n    → Paper Table 1\\n\\n并行: seed=123 SFT 🏃(全部启动, 0.5B ~41min / 1.5B ~3.8h / 3B ~ongoing)\\n并行: 3B d000 v2 eval
…[truncated 2352 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 198
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T21:50:58.082493+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T21:50:58.384097+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_exp_arc_perbench_nuts_20260514T201612\", \"task_type\": \"exp:arc_perbench_nuts\", \"project\": \"contamcal-irt-calibration\", \"status\": \"done\", \"started_at\": \"2026-05-14T20:16:13.640083+00:00\", \"ended_at\": \"2026-05-14T20:18:43.270954+00:00\"}, {\"worker_id\": \"worker_analysis_mmlu_item_aligned_gap_20260514T201711\", \"task_type\": \"analysis:mmlu_item_aligned_gap\", \"project\": \"contamcal-irt-calibration\", \"status\": \"done\", \"started_at\": \"2026-05-14T20:17:12.129627+00:00\", \"ended_at\": \"2026-05-14T20:19:13.532792+00:00\"}, {\"worker_id\": \"worker_ops_gpu_status_d026_20260514T201815\", \"task_type\": \"ops:gpu_status_d026\", \"project\": \"contamcal-irt-calibration\", \"status\": \"done\", \"started_at\": \"2026-05-14T20:18:15.620542+00:00\", \"ended_at\": \"2026-05-14T20:20:13.862516+00:00\"}, {\"worker_id\": \"worker_gpu_sft_05B_d100_s123_gpu1_20260514T201947\", \"task_type\": \"gpu:sft_05B_d100_s123_gpu1\", \"project\": \"contamcal-irt-calibration\", \"status\": \"done\", \"started_at\": \"2026-05-14T20:19:48.089985+00:00\", \"ended_at\": \"2026-05-14T20:20:32.214265+00:00\"}, {\"worker_id\": \"worker_gpu_sft_15B_d100_s123_gpu2_20260514T201959\", \"task_type\": \"gpu:sft_15B_d100_s123_gpu2\", \"project\": \"contamcal-irt-calibration\", \"status\": \"done\", \"started_at\": \"2026-05-14T20:19:59.778477+00:00\", \"ended_at\": \"2026-05-14T20:21:34.064515+00:00\"}, {\"worker_id\": \"worker_gpu_sft_3B_d000_s123_gpu5_20260514T202009\", \"task_type\": \"gpu:sft_3B_d000_s123_gpu5\", \"project\": \"contamcal-irt-calibration\", \"status\": \"done\", \"started_at\": \"2026-05-14T20:20:10.431865+00:00\", \"ended_at\": \"2026-05-14T20:24:45.198769+00:00\"}, {\"worker_id\": \"worker_code_d018_exclusion_signal_homogeneity_20260514T204013\", \"task_type\": \"code:d018_exclusion_signal_homogeneity\", \"project\": \"contamcal-irt-calibration\", \"status\": \"done\", \"starte
…[truncated 3975 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 301
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T21:51:01.964324+00:00_

called mcp__agent-ml-research__list_available_gpus

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_available_gpus</summary>

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__list_available_gpus",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T21:51:04.026019+00:00_

{"result":"{\"success\": true, \"data\": {\"gpus\": [{\"id\": \"cuda:0\", \"name\": \"NVIDIA GeForce RTX 4090 D\", \"memory_used_mb\": 11875, \"memory_total_mb\": 24564, \"utilization_pct\": 61, \"temperature_c\": 47, \"config_available\": true}, {\"id\": \"cuda:1\", \"name\": \"NVIDIA GeForce RTX 4090 D\", \"memory_used_mb\": 3695, \"memory_total_mb\": 24564, \"utilization_pct\": 39, \"temperature_c\": 37, \"config_available\": true}, {\"id\": \"cuda:2\", \"name\": \"NVIDIA GeForce RTX 4090 D\", \"memory_used_mb\": 14723, \"memory_total_mb\": 24564, \"utilization_pct\": 21, \"temperature_c\": 46, \"config_available\": true}, {\"id\": \"cuda:3\", \"name\": \"NVIDIA GeForce RTX 4090 D\", \"memory_used_mb\": 13341, \"memory_total_mb\": 24564, \"utilization_pct\": 65, \"temperature_c\": 55, \"config_available\": true}, {\"id\": \"cuda:4\", \"name\": \"NVIDIA GeForce RTX 4090 D\", \"memory_used_mb\": 8985, \"memory_total_mb\": 24564, \"utilization_pct\": 68, \"temperature_c\": 56, \"config_available\": true}, {\"id\": \"cuda:5\", \"name\": \"NVIDIA GeForce RTX 4090 D\", \"memory_used_mb\": 17327, \"memory_total_mb\": 24564, \"utilization_pct\": 23, \"temperature_c\": 52, \"config_available\": true}], \"server\": \"cqa1-21977\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__list_available_gpus",
  "elapsed_ms": 2061
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T21:52:48.176522+00:00_

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T21:52:48.377893+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_4e44a59a.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T21:52:51.590588+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T21:52:52.201831+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "Glob",
  "elapsed_ms": 611
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T21:52:55.130195+00:00_

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
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

_source line 25 · 2026-05-14T21:52:58.674956+00:00_

/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "Glob",
  "elapsed_ms": 3544
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T21:53:01.702708+00:00_

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T21:53:01.854003+00:00_

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T21:53:07.076911+00:00_

called mcp__agent-ml-research__get_project_resource_usage

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_project_resource_usage</summary>

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T21:53:09.605391+00:00_

{"result":"{\"success\": true, \"data\": {\"allocated_gpus\": [{\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:0\"}, {\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:1\"}, {\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:2\"}, {\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:3\"}, {\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\"}, {\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:5\"}], \"actually_running_gpus\": [{\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:3\", \"exp_id\": \"exp_001_sft_d100_3B_v2\"}, {\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:2\", \"exp_id\": \"exp_001_sft_15B_d100_s123\"}, {\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:5\", \"exp_id\": \"exp_001_sft_3B_d000_s123\"}, {\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"exp_id\": \"exp_001_eval_3B_d000_v2_aligned\"}, {\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:1\", \"exp_id\": \"exp_001_eval_05B_d100_s123_aligned\"}], \"allocated_but_idle\": [{\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:0\", \"idle_min\": null}], \"running_experiments\": [{\"exp_id\": \"exp_001_sft_d100_3B_v2\", \"gpus\": [\"cuda:3\"], \"util_avg\": null}, {\"exp_id\": \"exp_001_sft_15B_d100_s123\", \"gpus\": [\"cuda:2\"], \"util_avg\": null}, {\"exp_id\": \"exp_001_sft_3B_d000_s123\", \"gpus\": [\"cuda:5\"], \"util_avg\": null}, {\"exp_id\": \"exp_001_eval_3B_d000_v2_aligned\", \"gpus\": [\"cuda:4\"], \"util_avg\": null}, {\"exp_id\": \"exp_001_eval_05B_d100_s123_aligned\", \"gpus\": [\"cuda:1\"], \"util_avg\": null}], \"worker_pool\": {\"total\": 3, \"gpu_tasks\": 1, \"cpu_tasks\": 2, \"details\": [{\"worker_id\": \"worker_ops_cpu_exp005_v4_restart_20260514T215110\", \"task\": \"ops:cpu_exp005_v4_restart\"}, {\"worker_id\": \"worker_ops_cpu_exp004_v3_restart_20260514T215133\", \"task\": \"ops:cpu_exp004_v3_restart\"}, {\"worker_id\": \"worker_ops_gpu_monitor_and_submit_queue_20260514T215157\", \"task\": \"ops:gpu_monitor_and_submit_queue\"}]}, \"summary\": \"分配 6 张, 实际跑 5 张 ⚠️ | Worker 3 (GPU 1 / CPU 2)\"}, \"err
…[truncated 31 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__get_project_resource_usage",
  "elapsed_ms": 2528
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T21:53:55.408481+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_004_sim_sweep_v2",
  "field": "status",
  "value": "DONE",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_004_sim_sweep_v2",
    "field": "status",
    "value": "DONE",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T21:54:04.276199+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_004_sim_sweep_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:12:12.267Z\", \"updated_at\": \"2026-05-14T21:53:59.879Z\", \"spec\": {\"command\": \"python run_sweep.py subset --parallel 2 --chains-parallel 2\", \"server\": \"local\", \"pid\": 599560, \"data_path\": \"synthetic\", \"data_count\": 120, \"model_name\": \"4PL+gamma IRT\", \"seed\": 42, \"log_path\": \"/tmp/exp004_sweep_restart_v2.log\", \"parent\": \"exp_004_sim_sweep\", \"hypothesis\": \"4PL+γ IRT parameter recovery sweep: 12 conditions (4 AUC × 3 N_models) × 10 seeds. v2 restart with parallel=2, chains_parallel=2.\"}, \"notes\": \"PID 599560 crashed (~10h ago). 53/120 runs completed (27 from v1 + 26 from v2). Restarting as v3 with parallelization.\", \"metrics\": {\"runs_completed\": 48, \"runs_total\": 120, \"auc080_n50_bias\": 0.006, \"auc080_n50_rmse\": 0.03, \"auc080_n50_ci95_coverage\": 1, \"auc080_n100_gamma_hat\": 0.508, \"auc080_n100_bias\": 0.008, \"auc080_n100_ci_width\": 0.116, \"auc080_n100_theta_corr\": 0.962, \"ci_width_ratio_n100\": 1.81, \"core_findings_stable\": true}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T21:50:42.987Z\"}, \"hint\": \"💡 建议将故障原因写入 memory.md（如何避免再犯）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 8.752}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 8867
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T21:54:41.548292+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

````json
{
  "text": "[资源] GPU 分配 6 / 实际跑 5+1(untracked) | Worker 池 3 (GPU 1 / CPU 2)\n\n## 综合状态汇报（Loop #7 session-start）\n\n### 1. 关键发现：1.5B eval batch (exp_001_eval_15B_aligned_batch) ✅\n\nMC benchmarks 在 1.5B 尺度上**完全无法检测污染**（d000 vs d100 差异 <1pp）：\n- MMLU: 58.53% → 59.33% (+0.8pp)\n- GSM8K: 65.43% → 64.97% (-0.5pp)\n- ARC: 77.22% → 76.88% (-0.3pp)\n- HumanEval: 12.8% → 30.49% (**+17.69pp**，强 dose-response)\n\n对比 0.5B（d100 导致 MMLU -16.5pp 退化），**scale-dependent narrative 得到完美验证**：小模型退化、大模型免疫、生成式任务始终敏感。\n\nParaphrase gap 不能干净区分污染（1.5B para 有时高于 orig），这限制了简单 gap 方法的可行性，进一步支撑 IRT calibration 的必要性。\n\n### 2. IRT NUTS 验证进展\n\n- **GSM8K** (exp_006_irt_05B_gsm8k): joint fit 收敛 ✅，Rhat=1.008, ESS=956, 0 divergences。gamma=0.35 CI [-0.65, 1.4]\n- **ARC** (exp_006_irt_05B_arc): gamma=-1.21 CI [-2.53, 0.12]\n- 两者 CI 均包含 0 → **单 scale N=4 模型不足以显著检测 gamma**，验证了 D024/D025 的判断：必须跨 scale 池化\n\nDelta exposure fix (P0) 已生效：signal scores 现在单调递增 [0, 0.016, 0.065, 0.197]\n\n### 3. GPU 实况\n\n| GPU | 实验 | 状态 |\n|-----|------|------|\n| cuda:0 | exp002-signals-1p5B（untracked，11.9GB/61%util） | 🏃 |\n| cuda:1 | exp_001_eval_05B_d100_s123_aligned | 🏃 |\n| cuda:2 | exp_001_sft_15B_d100_s123 | 🏃 |\n| cuda:3 | exp_001_sft_d100_3B_v2 | 🏃 |\n| cuda:4 | exp_001_eval_3B_d000_v2_aligned | 🏃 |\n| cuda:5 | exp_001_sft_3B_d000_s123 | 🏃 |\n\nCPU: exp-004 v3 重启中 | exp-005 v4 重启中 | GPU monitor worker 运行中\n\n### 4. Critical Path\n\n```\n1.5B signals 完成 (cuda:0, ~2-3h remaining)\n  → 0.5B+1.5B pooled IRT (exp_006_irt_05B_v2)\n    → Paper Table 1\n\n并行：3B d000 v2 eval (cuda:4) → 验证 D020 GSM8K 恢复\n并行：seed=123 SFT (cuda:1/2/5) → 多种子方差估计\n并行：3B d100 v2 SFT (cuda:3) → 3B 矩阵最后一块\n```\n\n### 5. 建议\n\n1. **等 1.5B signals 完成后立即启动 pooled IRT** — 这是 Paper Table 1 的直接依赖\n2. **3B d000 v2 eval 完成后** — 若 GSM8K >= 50% (D020 目标)，3B 回归正常矩阵；若仍崩塌则 3B GSM8K 永久排除\n3. **截稿前 11 天** — SFT 矩阵 seed=42 接近完整（缺 0.5B d025 v3 已完成 SFT 但未跑 aligned eval），seed=123 正在补齐",
  "project": "contamcal-irt-calibration"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 分配 6 / 实际跑 5+1(untracked) | Worker 池 3 (GPU 1 / CPU 2)\n\n## 综合状态汇报（Loop #7 session-start）\n\n### 1. 关键发现：1.5B eval batch (exp_001_eval_15B_aligned_batch) ✅\n\nMC benchmarks 在 1.5B 尺度上**完全无法检测污染**（d000 vs d100 差异 <1pp）：\n- MMLU: 58.53% → 59.33% (+0.8pp)\n- GSM8K: 65.43% → 64.97% (-0.5pp)\n- ARC: 77.22% → 76.88% (-0.3pp)\n- HumanEval: 12.8% → 30.49% (**+17.69pp**，强 dose-response)\n\n对比 0.5B（d100 导致 MMLU -16.5pp 退化），**scale-dependent narrative 得到完美验证**：小模型退化、大模型免疫、生成式任务始终敏感。\n\nParaphrase gap 不能干净区分污染（1.5B para 有时高于 orig），这限制了简单 gap 方法的可行性，进一步支撑 IRT calibration 的必要性。\n\n### 2. IRT NUTS 验证进展\n\n- **GSM8K** (exp_006_irt_05B_gsm8k): joint fit 收敛 ✅，Rhat=1.008, ESS=956, 0 divergences。gamma=0.35 CI [-0.65, 1.4]\n- **ARC** (exp_006_irt_05B_arc): gamma=-1.21 CI [-2.53, 0.12]\n- 两者 CI 均包含 0 → **单 scale N=4 模型不足以显著检测 gamma**，验证了 D024/D025 的判断：必须跨 scale 池化\n\nDelta exposure fix (P0) 已生效：signal scores 现在单调递增 [0, 0.016, 0.065, 0.197]\n\n### 3. GPU 实况\n\n| GPU | 实验 | 状态 |\n|-----|------|------|\n| cuda:0 | exp002-signals-1p5B（untracked，11.9GB/61%util） | 🏃 |\n| cuda:1 | exp_001_eval_05B_d100_s123_aligned | 🏃 |\n| cuda:2 | exp_001_sft_15B_d100_s123 | 🏃 |\n| cuda:3 | exp_001_sft_d100_3B_v2 | 🏃 |\n| cuda:4 | exp_001_eval_3B_d000_v2_aligned | 🏃 |\n| cuda:5 | exp_001_sft_3B_d000_s123 | 🏃 |\n\nCPU: exp-004 v3 重启中 | exp-005 v4 重启中 | GPU monitor worker 运行中\n\n### 4. Critical Path\n\n```\n1.5B signals 完成 (cuda:0, ~2-3h remaining)\n  → 0.5B+1.5B pooled IRT (exp_006_irt_05B_v2)\n    → Paper Table 1\n\n并行：3B d000 v2 eval (cuda:4) → 验证 D020 GSM8K 恢复\n并行：seed=123 SFT (cuda:1/2/5) → 多种子方差估计\n并行：3B d100 v2 SFT (cuda:3) → 3B 矩阵最后一块\n```\n\n### 5. 建议\n\n1. **等 1.5B signals 完成后立即启动 pooled IRT** — 这是 Paper Table 1 的直接依赖\n2. **3B d000 v2 eval 完成后** — 若 GSM8K >= 50% (D020 目标)，3B 回归正常矩阵；若仍崩塌则 3B GSM8K 永久排除\n3. **截稿前 11 天** — SFT 矩阵 seed=42 接近完整（缺 0.5B d025 v3 已完成 SFT 但未跑 aligned eval），seed=123 正在补齐",
    "project": "contamcal-irt-calibration"
  }
}
````

</details>

---

### Tool result

_source line 33 · 2026-05-14T21:55:04.280518+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 22732
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T21:55:29.290264+00:00_

called mcp__agent-ml-research__read_experiment_plan_with_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_experiment_plan_with_status</summary>

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_experiment_plan_with_status",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T21:55:32.294916+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": [{\"id\": \"exp-001\", \"name\": \"controlled_sft_injection\", \"claim\": 1, \"description\": \"SFT contamination injection on Qwen2.5-0.5B/1.5B/3B at 5 dosage levels (0%, 5%, 25%, 50%, 100% benchmark items as paraphrases in SFT data). Produces ground-truth contaminated/clean model pairs. 15 SFT runs total (3 models × 5 dosages), parallelized across GPUs. 3 seeds per condition for key metrics (mean ± std). Paraphrase generation: use strong open LLM (Qwen2.5-72B-Instruct or equivalent) with controlled semantic similarity — following methodology of \\\"Rethinking Benchmark and Contamination\\\" (arXiv 2023). Target: high semantic similarity (cosine >0.85) but low lexical overlap (BLEU <0.3) to evade n-gram decontamination while preserving contamination effect. Quality validation: automated similarity metrics + human spot-check on 50 random pairs per benchmark.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 50, \"deps\": [], \"benchmarks\": [\"MMLU\", \"GSM8K\", \"ARC-Challenge\", \"HumanEval\"], \"models\": [\"Qwen2.5-0.5B\", \"Qwen2.5-1.5B\", \"Qwen2.5-3B\"], \"seeds\": 3, \"registry_id\": \"exp_001_sft_d100_15B_v2\", \"status\": \"DONE\", \"conclusion\": \"success\"}, {\"id\": \"exp-002\", \"name\": \"stage1_signal_pipeline\", \"claim\": 2, \"description\": \"Compute 4 detection signals on all contaminated + clean models from exp-001: (a) embedding-based semantic retrieval (FAISS + sentence-transformers), (b) Min-K%++ membership inference, (c) ConStat performance gap (original vs paraphrased items), (d) Self-Critique entropy collapse. Output: per-model-item exposure scores for each signal.\\n\", \"priority\": \"P0\", \"gpu_budget_hours\": 20, \"deps\": [\"exp-001\"], \"status\": \"planned\"}, {\"id\": \"exp-003\", \"name\": \"rrf_aggregation_ablation\", \"claim\": 2, \"description\": \"RRF fusion of 4 signals into composite per-item exposure score. Ablations: (a) RRF vs equal-weight rank averaging, (b) si
…[truncated 8044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_experiment_plan_with_status",
  "elapsed_ms": 3004
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-14T21:56:57.935935+00:00_

Session-start 初始化完成。状态总结：

**RUNNING (6 GPU + 1 CPU):**
- cuda:0: exp002-signals-1p5B (1.5B 信号计算，critical path)
- cuda:1: exp_001_eval_05B_d100_s123_aligned
- cuda:2: exp_001_sft_15B_d100_s123
- cuda:3: exp_001_sft_d100_3B_v2 (预计 ~1.5h 完成)
- cuda:4: exp_001_eval_3B_d000_v2_aligned (D020 GSM8K 恢复验证)
- cuda:5: exp_001_sft_3B_d000_s123

**Worker 池 = 3** (满足 >=2 约束): GPU monitor + 2× CPU experiment restarts

**已完成的关键动作:**
1. Registry 修正: exp_004_sim_sweep_v2 RUNNING→DONE
2. Director 汇报: 1.5B eval batch 发现（MC <1pp，HumanEval +17.69pp）+ IRT NUTS 验证 + GPU 全满 + critical path 分析
3. 6/6 GPU 无空闲

**Critical path:** 1.5B signals (cuda:0, ~2-3h) → pooled IRT (exp_006_irt_05B_v2) → Paper Table 1

等待回调：Worker 完成通知 / CRON 实验完成 / Director 回复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch"
}
```

</details>

---

## Round 2

26 recorded events

### User

_source line 37 · 2026-05-15T00:59:02.467784+00:00_

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T00:59:19.349646+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__list_workers",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__list_workers",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T00:59:19.400410+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T00:59:23.239062+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T00:59:23.794643+00:00_

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T00:59:24.202644+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "report.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "file": "report.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T00:59:24.706480+00:00_

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T00:59:25.214484+00:00_

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__load_project_config",
  "tool_args": {
    "project_name": "contamcal-irt-calibration",
    "section": "execution"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T00:59:25.519544+00:00_

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
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

_source line 46 · 2026-05-15T00:59:26.340594+00:00_

Error: result (172,641 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-4e44a59a/99fc9dfe-0914-4f3c-ad92-48f244daef10/tool-results/mcp-agent-ml-research-read_registry-1778806766117.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-4e44a59a/99fc9dfe-0914-4f3c-ad92-48f244daef10/tool-results/mcp-agent-ml-research-read_registry-1778806766117.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-4e44a59a/99fc9dfe-0914-4f3c-ad92-48f244daef10/tool-results/mcp-agent-ml-research-read_registry-1778806766117.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 3101
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T00:59:46.348910+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 4, \"results\": [{\"exp_id\": \"exp_001_sft_d025_3B_v2\", \"success\": true, \"actions\": [\"Job still running (pid=466755)\"]}, {\"exp_id\": \"exp_001_sft_3B_d100_s123\", \"success\": true, \"actions\": [\"Job still running (pid=471296)\"]}, {\"exp_id\": \"exp_001_eval_15B_d100_s123_aligned\", \"success\": true, \"actions\": [\"Job still running (pid=473954)\"]}, {\"exp_id\": \"exp_001_eval_05B_d005_s123_aligned\", \"success\": true, \"actions\": [\"Job still running (pid=475651)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 22554
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T00:59:46.349595+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_001_eval_05B_d005_s123_aligned | — | — | — | — |\\n| exp_001_eval_15B_d100_s123_aligned | 1.5B d100 seed=123 aligned eval for N=16 multi-seed IRT pooling. | — | — | — |\\n| exp_004_sim_sweep_v4 | 4PL+γ IRT parameter recovery sweep v4: resume of v3 (crashed due to /tmp tmpfs full from cmdstanpy MCMC temp files). Fixed: TMPDIR=/home/ubuntu/tmp_cmdstan, --resume mode strips failed seeds and re-runs them. 57/120 done, 63 remaining across 8 conditions. | — | — | — |\\n\\n## 待处理\\n- exp_003_mmlu_item_aligned_gap（准备中）\\n- exp006-gsm8k-d024-delta（准备中）\\n- exp_006_irt_05B_v2: Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 items + ADVI robustness check. Fixes v1 issues: aligned-only, signal-derived exposure, --max-items.（准备中）\\n- exp_008_instruct_rl_proxy: RL proxy experiment (D021 Problem 3): Use Qwen2.5-0.5B-Instruct (SFT+RL post-trained) as RL regime data point. 3-regime comparison: base (pretrained) → d000 (SFT) → Instruct (SFT+RL). Compute all 4 signals on Instruct model, observe signal value changes across training regimes. No additional training needed.\\\"（准备中）\\n- exp_001_eval_05B_d100_aligned_v2（准备中）\\n- exp_001_eval_3B_d000_s42_v3: 3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。（准备中）\\n- exp_001_eval_05B_d000_s42_v6: 0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)（准备中）\\n- exp_001_eval_05B_d100_v6: 100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)（准备中）\\n- exp_001_eval_05B_d100_v4: 100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)（准备中）\\n- exp_001_eval_05B_d000_s42_v4: 0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)（准备中）\\n- …另有 5 项\\n\\n## 近期结论\\n- **exp_001_eval_3B_d100_v2_para_al
…[truncated 1715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 22146
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T00:59:46.452829+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-15 00:05 UTC | 更新原因: D036: ARC negative gamma confirmed, coverage collapse 20-33%, 跨种子方差 7pp, 优先级重排\\n\\n## 核心方向\\nContamCal：post-hoc statistical calibration via contamination-augmented 4PL IRT。详见 paper_framing.md。\\n\\n## 投稿目标\\n**EMNLP 2026 ARR May 25**（D006, 距今 10 天）\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-13 通过）+ 审稿进行中\\n- **D036 关键发现**: ARC gamma 负方向 confirmed（3 条独立证据链）→ framing 调整为 benchmark-dependent effects\\n- **Coverage collapse**: 20-33% 即使 oracle，PPP 极值 → 模型可能错误指定，调查中\\n- **跨种子方差**: 0.5B d100 ARC 7.25pp（s42 vs s123）→ multi-seed pooling 必要条件\\n- **Scale story**: 3B d100 ARC=84% vs 0.5B d100=29-37%，scale 显著缓解 contamination forgetting\\n\\n**SFT 进度 (seed=42)**:\\n\\n| 模型 | d000 | d005 | d025 | d100 |\\n|------|------|------|------|------|\\n| 0.5B | ✅ | ✅ | ❌(2x fail) | ✅ |\\n| 1.5B | ✅ | ✅ | ✅ | ✅ |\\n| 3B | ✅(v2) | P2 | P4 | 🏃(v2) |\\n\\n**SFT 进度 (seed=123)**:\\n\\n| 模型 | d000 | d005 | d025 | d100 |\\n|------|------|------|------|------|\\n| 0.5B | ✅ | 🏃(GPU 1) | — | ✅(eval done) |\\n| 1.5B | ✅ | — | — | 🏃(GPU 2) |\\n| 3B | 🏃(v2, GPU 5) | — | — | — |\\n\\n**Signal (exp-002)**: 0.5B ✅ | 1.5B ✅ (12/12 PASS) | 3B 未开始\\n**CPU**: exp-004 v3 ~45% | exp-005 v4 ~92%\\n\\n## ⚠️ Critical Issues (D036)\\n1. **Coverage collapse 20-33%** — PPP=1.0(ARC)/0.0(GSM8K)，4PL+γ additive 模型可能不够。调查路径：(a) N↑ via multi-seed (b) exp-004 at matching N (c) 更灵活 IRT 结构\\n2. **Oracle vs RRF 比较混淆** — N_models 15 vs 8，需匹配 N=8 重跑 oracle\\n3. **GSM8K oracle 诊断 FAIL** — rhat=1.012/ESS=345，需 warmup=2000/samples=2000\\n4. **train_sft.py --gpu 死代码** — args.gpu 解析但未用，需修复\\n\\n## Critical Path\\n```\\n🔴 Coverage collapse 调查 ← 最高优先级\\n  → exp-004 sweep coverage 数据（45% done）\\n  → seed=123 完成后 N≥16 pooled IRT 重跑 → 检查 coverage 是否改善\\n  → 如果 N↑ 仍不够 → 考虑 model mi
…[truncated 2158 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 21746
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T00:59:46.503529+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"contamcal-irt-calibration\", \"section\": \"execution\", \"config\": {\"execution\": {\"gpu_ids\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\", \"cuda:4\", \"cuda:5\"], \"project_path\": \"/root/contamcal-irt-calibration\", \"servers\": [\"cqa1-21977\"]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 21289
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T00:59:46.759785+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_diag_mcmc-progress-check_20260515T005659\", \"task_type\": \"diag:mcmc-progress-check\", \"project\": \"contamcal-irt-calibration\", \"status\": \"running\", \"started_at\": \"2026-05-15T00:57:00.089493+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_ops_prep-instruct-eval_20260515T005714\", \"task_type\": \"ops:prep-instruct-eval\", \"project\": \"contamcal-irt-calibration\", \"status\": \"running\", \"started_at\": \"2026-05-15T00:57:15.053877+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_code_pooled-irt-n16-script_20260515T005717\", \"task_type\": \"code:pooled-irt-n16-script\", \"project\": \"contamcal-irt-calibration\", \"status\": \"running\", \"started_at\": \"2026-05-15T00:57:18.461614+00:00\", \"ended_at\": null}], \"count\": 3}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 21240
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-15T00:59:52.189929+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['exp_id', 'status', 'hypothesis', 'spec']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['exp_id', 'status', 'hypothesis', 'spec']"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T00:59:53.145489+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": "{'status': 'PREPARING'}",
  "fields": "['exp_id', 'status', 'hypothesis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "filters": "{'status': 'PREPARING'}",
    "fields": "['exp_id', 'status', 'hypothesis']"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T00:59:53.804785+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_001_eval_05B_d005_s123_aligned\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_05B_d005_s123\", \"hypothesis\": \"0.5B d005 seed=123 aligned eval for seed=123 signal computation pipeline.\", \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\"}}, \"exp_001_eval_15B_d100_s123_aligned\": {\"status\": \"RUNNING\", \"hypothesis\": \"1.5B d100 seed=123 aligned eval for N=16 multi-seed IRT pooling.\", \"spec\": {\"command\": \"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned\", \"data_count\": 4, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_sou
…[truncated 6984 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1614
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T00:59:53.805258+00:00_

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
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

_source line 56 · 2026-05-15T00:59:55.168183+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_003_mmlu_item_aligned_gap\": {\"status\": \"PREPARING\"}, \"exp006-gsm8k-d024-delta\": {\"status\": \"PREPARING\"}, \"exp_006_irt_05B_v2\": {\"status\": \"PREPARING\", \"hypothesis\": \"Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 items + ADVI robustness check. Fixes v1 issues: aligned-only, signal-derived exposure, --max-items.\"}, \"exp_008_instruct_rl_proxy\": {\"status\": \"PREPARING\", \"hypothesis\": \"RL proxy experiment (D021 Problem 3): Use Qwen2.5-0.5B-Instruct (SFT+RL post-trained) as RL regime data point. 3-regime comparison: base (pretrained) → d000 (SFT) → Instruct (SFT+RL). Compute all 4 signals on Instruct model, observe signal value changes across training regimes. No additional training needed.\\\"\"}, \"exp_001_eval_05B_d100_aligned_v2\": {\"status\": \"PREPARING\"}, \"exp_001_eval_3B_d000_s42_v3\": {\"hypothesis\": \"3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d000_s42_v6\": {\"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d100_v6\": {\"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d100_v4\": {\"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d000_s42_v4\": {\"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d000_s42_v2\": {\"status\": \"PREPARING\"}, \"exp_001_eval_05B_d100_v3\": {\"hypothesis\": \"100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 contamination score inflation\", \"status\": \"PREPARING\"}, \"exp_001_eval_05B_d000_s42_v3\": {\"hypothesis\": \"0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于 calibration error 计算\", \"status\": \"PREPA
…[truncated 443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2022
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-15T00:59:55.270585+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\", \"content\": \"# Memory — contamcal-irt-calibration\\n\\n## 关键经验\\n\\n### P0: Delta Exposure Fix (2026-05-14)\\n- **问题**: per-benchmark IRT 用 exp-002 raw signal scores 做 exposure，d000 baseline≈0.613，所有模型看起来都 high exposure → Stan 无法区分 clean vs contaminated → Rhat=1.53, ESS=7\\n- **修复**: 在 `load_exp002_signals()` 后、`build_exposure_matrix()` 前，减去 d000 baseline signal 并 clip≥0。修复后 per-benchmark Rhat=1.0096, ESS=522, 0 divergences\\n- **代码位置**: `run_exp006.py` line 195-201\\n- **教训**: 任何 signal-derived exposure 都必须 baseline-subtract，否则 IRT gamma 不可识别\\n\\n### RRF Per-Model Mean 不可用作 Exposure (2026-05-14, 审计确认)\\n- **问题**: `load_exp002_signals()` 返回 `float(rrf.mean())`——per-item RRF 对全部 item 取 mean。d005 只有 5% item 被污染，mean 被 95% clean items 稀释。delta 后基本是噪声。\\n- **症状**: RRF fusion exposure 非单调（ARC 0.5B: d005(0.181) > d025(0.171)；GSM8K 0.5B: d025(0.209) > d100(0.192)）\\n- **S1 Embedding 单独是完美单调的**: 0.5946 → 0.6212 → 0.6932 → 0.8998，Spearman vs oracle = 1.0\\n- **S2/S4 噪声破坏单调性**: RRF fusion 后 Spearman vs oracle 降到 0.7\\n- **代码层面**: `build_exposure_matrix()` 中 `tau=ones`，exposure matrix 退化为 rank-1，丢失 item-level 信息\\n- **结论**: per-model exposure 应用 S1-only 或 oracle dosage。RRF 应用作 per-item tau（未来方向）\\n\\n### train_sft.py --gpu 不设 CUDA_VISIBLE_DEVICES (2026-05-14)\\n- **问题**: `train_sft.py` 解析 `--gpu` 参数但从未设置 `CUDA_VISIBLE_DEVICES` 或 `device_map`，进程默认跑到 GPU 0\\n- **症状**: `exp_001_sft_d025_3B` 注册 GPU 3 RUNNING 但 nvidia-smi 显示 GPU 3 空转\\n- **修复**: 提交命令前缀 `CUDA_VISIBLE_DEVICES=3`\\n- **教训**: 所有 train_sft.py 提交必须显式设 `CUDA_VISIBLE_DEVICES=N`，不能依赖 `--gpu` 参数\\n\\n### 结果收集 Worker 禁止模糊路径搜索 (2026-05-15, D036 事故)\\n- **问题**: Worker 收集 eval 结果时，v2 输出目录为空（eval 仍在跑），Worker 用 `ls -d *3B*d100*` 模糊搜索，找到 v1 结果目录并误报为 v2 metrics\\n- **连锁反应**: v2 误标 DONE → PID 461879 被认为重复进程 → kill → 输出目录被删 → 需重跑 v3\\n- **教训**: 结果收集 Worker 的 task prompt 必须指定精确输出目录路径。
…[truncated 4818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1465
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-15T00:59:59.516606+00:00_

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
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

_source line 59 · 2026-05-15T00:59:59.567327+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-15T01:00:02.247264+00:00_

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
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
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

_source line 61 · 2026-05-15T01:00:02.299499+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-15T01:01:16.857491+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0-5（cqa1-21977），全部已分配本项目，无需申请
- `train_sft.py --gpu` 是死代码，**必须用 `CUDA_VISIBLE_DEVICES=N` 前缀**，否则进程跑到 GPU 0
- 3B d000 GSM8K=12% 是 LoRA 超参损伤（D018），**必须从所有 IRT 分析中排除**
- Pooled IRT 禁止混用 signal-derived exposure 和 oracle dosage（D026），必须同源
- Per-model exposure 只用 S1-only 或 oracle，**RRF per-model mean 已废弃**（D034）
- 所有 eval 命令前缀必须带 `source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- seed=123 超参必须与同 scale seed=42 一致（0.5B/1.5B: lr=2e-4,alpha=32; 3B: lr=5e-5,alpha=16）
- 结果收集 Worker 必须指定精确路径，**禁止模糊 glob 搜索**（D036 事故教训）

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-21977, 6× RTX 4090D
- **工作目录**: `/root/contamcal-irt-calibration`
- **Python**: `/root/miniconda3/bin/python`（conda base env，不用 venv）
- **模型缓存**: `/root/autodl-tmp/.hf_cache`
- **SFT checkpoints**: `/root/autodl-tmp/exp001/checkpoints/`
- **Eval 结果**: `/root/autodl-tmp/exp001/eval_results/`
- **Signal 数据**: `/root/autodl-tmp/exp002/signals/`
- **IRT 结果**: `/root/autodl-tmp/exp006/`
- **Sim sweep 结果**: `~/projects/contamcal-irt-calibration/artifacts/simulation_sweep/results/`
- **活跃 GPU 进程**:
  - GPU 1: exp_001_eval_05B_d005_s123_aligned (PID 475651)
  - GPU 2: exp_001_eval_15B_d100_s123_aligned (PID 473954)
  - GPU 3: exp_001_sft_d025_3B_v2 (PID 466755, tmux=exp_001_sft_d025_3B_v2)
  - GPU 4: exp_001_eval_3B_d000_v2_para_aligned_v2 (tmux=同名)
  - GPU 5: exp_001_sft_3B_d100_s123 (PID 471296, tmux=同名)
- **CPU 进程**:
  - exp_004_sim_sweep_v4 (PID 652931, tmux=exp_004_sim_sweep_v4, TMPDIR=/home/ubuntu/tmp_cmdstan)
  - exp006-oracle-gsm8k-extended (CPU MCMC)
  - exp006-pooled-s1only-gsm8k (CPU MCMC)
  - exp006-pooled-s1only-arc (CPU MCMC)
- **Cron 监控**: 4 个活跃 cron (exp_001_sft_d025_3B_v2, exp_001_sft_3B_d100_s123, exp_001_eval_15B_d100_s123_aligned, exp_001_eval_05B_d005_s123_aligned)

### 3. 📊 当前状态
**刚完成**: D036 分析——ARC negative gamma confirmed（3 条独立证据链），coverage collapse 20-33%，跨种子方差 7.25pp。Framing 调整为 benchmark-dependent effects。

**正在进行**:
- 9 个实验 RUNNING（5 GPU + 4 CPU），详见上方
- 3 个 Worker running:
  - `worker_diag_mcmc-progress-check`: 检查 CPU MCMC 进度
  - `worker_ops_prep-instruct-eval`: 准备 exp_008 Instruct RL proxy eval
  - `worker_code_pooled-irt-n16-script`: 编写 N≥16 pooled IRT 脚本（multi-seed 完成后使用）
- GPU 0 当前空闲（无实验分配）

**等待中**:
- 4 个 cron 回调（SFT/eval 完成后触发）
- Worker 回调（3 个 running worker）
- seed=123 全部完成后 → N≥16 pooled IRT 是 critical path

### 4. 📋 待办（条件触发式）
- exp_001_sft_d025_3B_v2 cron 回调(GPU 3 SFT 完成) → spawn worker eval 3B d025 aligned + para_aligned
- exp_001_sft_3B_d100_s123 cron 回调(GPU 5 SFT 完成) → spawn worker eval 3B d100 s123 aligned + para_aligned
- exp_001_eval_15B_d100_s123_aligned 完成 → 跑 signal computation → 加入 pooled IRT 候选池
- exp_001_eval_05B_d005_s123_aligned 完成 → 跑 signal computation → 加入 pooled IRT 候选池
- worker_code_pooled-irt-n16-script 完成 → 审查脚本，等 seed=123 eval 全部完成后提交 N≥16 pooled IRT
- worker_ops_prep-instruct-eval 完成 → 审查方案，GPU 0 空闲可立即提交 exp_008
- CPU MCMC 完成(oracle-gsm8k-extended / s1only-gsm8k / s1only-arc) → 分析收敛性(rhat<1.01,ESS>1000)，更新 registry，汇报 Director
- exp_004_sim_sweep_v4 完成(57/120→120/120) → 分析 parameter recovery 覆盖率，与 real-data coverage collapse 对比
- 所有 seed=123 eval+signal 完成 → 跑 N≥16 pooled IRT → 检查 coverage 是否从 20-33% 改善 → 如果仍低则 model misspecification 路径
- GPU 0 空闲 → 优先提交 exp_008_instruct_rl_proxy（Instruct 模型无需训练，直接 eval）

### 5. 🎯 战略上下文
**投稿目标**: EMNLP 2026 ARR May 25（距今 10 天）。

**核心 story**: ContamCal 是 post-hoc statistical calibration via contamination-augmented 4PL+γ IRT。关键发现：contamination effects 是 benchmark-dependent 和 scale-dependent 的（D036 framing 调整后）。ARC gamma 为负（小模型遗忘>记忆），GSM8K gamma 为正但 CI 包含 0（N 不够）。

**Critical path**: coverage collapse 根因调查。当前 4PL+γ 覆盖率只有 20-33%（即使 oracle exposure），PPP 极值(1.0/0.0)暗示模型可能错误指定。两条调查路径：(a) N↑ via multi-seed pooling（正在做），(b) exp-004 simulation sweep 在匹配 N 下的覆盖率基准（45% done）。

**易错点**:
- 不要把 oracle baseline（N=15 models）和 RRF baseline（N=8 models）直接比较——N_models 不同
- exp-004 simulation sweep 用 TMPDIR=/home/ubuntu/tmp_cmdstan，不是 /tmp（/tmp 是 tmpfs 会满）
- 15 个 PREPARING 实验大部分是历史遗留（多次 fail 后重建的版本），不要盲目重提交——先看是否已被更高版本号替代
- S3 ConStat 信号已弃用（D030），论文只报告 3-signal（S1+S2+S4）
- Paraphrase gap 分析必须用 delta-of-deltas（减去 d000 baseline gap），raw gap 包含 paraphrase inherent difficulty difference

**决策链**: D027(pooled GSM8K invalid) → D028(mixed scales) → D029(paraphrase gap不可用) → D030(弃用ConStat) → D031(exposure同源性) → D032(首次pooled结果) → D033(审计6问题) → D034(S1-only) → D035(oracle baseline) → D036(ARC negative gamma + coverage collapse + 跨种子方差)
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:exp_001_eval_15B_aligned_batch"
}
```

</details>

---
