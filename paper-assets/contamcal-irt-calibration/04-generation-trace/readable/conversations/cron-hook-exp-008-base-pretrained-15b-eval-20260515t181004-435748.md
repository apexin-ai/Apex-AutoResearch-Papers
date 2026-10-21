# cron hook exp 008 base pretrained 15B eval 20260515T181004 435748

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 2
- **Tool calls:** 22
- **Original source:** `logs/chats/archive/cron_hook_exp_008_base_pretrained_15B_eval_20260515T181004_435748.jsonl`
- **Structured JSON:** [`330750caf75ba4856aef.json`](../../sessions/33/330750caf75ba4856aef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-15T15:01:28.952601+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #11。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0-5 全在 cqa1-21977，禁止用其他服务器或超出范围的 GPU
- 0.5B MMLU/ARC 已被排除出 IRT pooling（D045，position bias A=46%）——任何涉及 pooled IRT 的实验不要纳入这两个 benchmark 的 0.5B 数据
- d000 模型不含 GSM8K/HumanEval 格式数据（D044 format confound）——d000 在这两个 benchmark 上的 drop 不能归因于 contamination，是 format 问题
- exp_008 base pretrained eval 已连续失败 2 次（0.5B 版本 PID 卡死 + 无 sentinel），1.5B 版本刚完成是第一次成功——如果后续 base eval 再失败，优先检查 evaluate.py 对 base model 的兼容性
- submit_training_job 命令必须自带环境激活（如 `source /root/miniconda3/bin/activate && python ...`），不要假设 .venv 存在

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977，工作目录 /root/contamcal-irt-calibration
- Python：/root/miniconda3/bin/python（aml-train 镜像，conda base 环境）
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 活跃 GPU 进程：
  - cuda:0 — exp_001_sft_15B_d025_s123_v2 (PID 549516, log /tmp/sft_15B_d025_s123_v2.log)
  - cuda:1 — exp_001_sft_15B_d005_s123_v2 (PID 549858, log /tmp/sft_15B_d005_s123_v2.log)
  - cuda:3 — exp_001_eval_3B_d000_s123_aligned (PID 551219, log /tmp/eval_3B_d000_s123_aligned.log)
  - cuda:5 — exp_001_eval_3B_d005_s42_aligned (PID 551290, log /tmp/eval_3B_d005_s42_aligned.log)
  - cuda:2, cuda:4 — **空闲**
- CPU 进程：exp_004_sim_sweep_extreme_gamma (PID 528993，不在 registry 中，可能是 stale cron)
- Cron：2 个活跃（exp_004_sim_sweep_extreme_gamma + exp_008_base_pretrained_15B_eval_v2 残留 miss 2/5）

### 3. 📊 当前状态
刚收到 exp_008_base_pretrained_15B_eval 的 CRON 完成回调（Qwen2.5-1.5B base pretrained eval，进程正常退出，W&B 可用）。已派 Worker `worker_analyze_exp_008_base_pretrained_15B_eval_20260515T115311` 去 SSH 分析结果（读日志、提取 metrics、更新 registry）。**Worker 尚未回调**。

已向 Director 汇报：(1) exp_008 正在分析 (2) cuda:2/cuda:4 空闲，建议 exp_008_instruct_rl_proxy 和 exp_001_eval_05B_d000_s42_v6 填坑。**Director 尚未回复**。

RUNNING 4 个：
- exp_001_sft_15B_d025_s123_v2 (cuda:0) — 1.5B 25% dosage seed=123 SFT
- exp_001_sft_15B_d005_s123_v2 (cuda:1) — 1.5B 5% dosage seed=123 SFT
- exp_001_eval_3B_d000_s123_aligned (cuda:3) — 3B 0% dosage seed=123 aligned eval
- exp_001_eval_3B_d005_s42_aligned (cuda:5) — 3B 5% dosage seed=42 aligned eval

PREPARING 18 个，最优先：exp_008_instruct_rl_proxy、exp_001_eval_15B_d025_s123、exp_001_eval_15B_d005_s123

### 4. 📋 待办
- Worker analyze exp_008 回调 → 执行 on-experiment-done 全流程：更新 registry DONE + 刷新 report.md + 与 1.5B d000 对比量化 SFT tax + 文献联动 + 反思实验计划 + 向 Director 发完整分析报告
- Director 回复空闲 GPU 分配决策 → 立即提交审批通过的实验到 cuda:2/cuda:4
- cuda:0 SFT d025 完成 → 提交 exp_001_eval_15B_d025_s123 eval
- cuda:1 SFT d005 完成 → 提交 exp_001_eval_15B_d005_s123 eval
- cuda:3/5 eval 完成 → on-experiment-done，释放 GPU 给下一批 3B 实验
- seed=123 全部完成 → N≥16 multi-seed pooled IRT 重跑，检查 coverage collapse 是否改善（ROADMAP critical path）

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 ARR May 25（距今 10 天）
- **核心 pivot（D038）**：论文 framing 已从 "calibration method" 转为 "detection/diagnostic tool"——gamma 捕获 contamination signal 但校准不一定改善，故事是 "发现 benchmark-dependent effects" 而非 "修好 calibration"
- **Coverage collapse（D042 最高优先级）**：20-33% coverage 即使 oracle，PPP 极值，4PL+γ additive 模型可能 misspecified。根因调查路径：(a) multi-seed pooling 增加 N (b) exp-004 sweep coverage (c) 更灵活 IRT 结构
- **Gamma 语义（D043）**：d000 counterfactual 使 gamma 捕获 SFT_tax + contamination，不能纯当 contamination indicator
- **3-regime comparison（exp_008 系列）**：base → SFT(d000) → Instruct(SFT+RL)，目的是分离 SFT 效应和 RL 效应。1.5B base 刚完成，0.5B base 失败 2 次
- **易踩坑**：(1) 0.5B d000 s42 eval 已失败 5 个版本（v1-v5），根因可能是 evaluate.py 的 GPU 处理 bug，v6 还在 PREPARING (2) exp_004_sim_sweep 也失败了 v1-v5，v_extreme_gamma 在跑但不在 registry (3) reconcile 会报 stale cron，不在 registry 的直接忽略

## 项目硬约束 (memory.md 节选)

## GPU 当前占用

| GPU | PID | 任务 | 状态 |
|-----|-----|------|------|
| 0 | 566224 | 1.5B d005 s123 aligned eval | 运行中 |
| 1 | 566311 | 1.5B d025 s123 aligned eval | 运行中 |
| 2 | 555936 | **3B d005 s123 SFT** | 运行中 |
| 3 | 551219 | 3B d000 s123 aligned eval (re-run, non-v2 ckpt) | 运行中 |
| 4 | 556016 | **3B d025 s123 SFT** | 运行中 |
| 5 | 551290 | 3B d005 s42 aligned eval | 运行中 |

---

## 可查的历史
前 76 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-15T15:01:41.752964+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
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

_source line 3 · 2026-05-15T15:01:41.803621+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T15:01:45.382732+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T15:01:45.886745+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T15:01:46.342046+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
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

_source line 7 · 2026-05-15T15:01:46.499466+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T15:01:47.406677+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_002_signals_3B\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:46:52.925Z\", \"updated_at\": \"2026-05-15T15:01:04.042Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && python run_batch.py --model-size 3B --gpu 0 --only d000 d005 d025 d100\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"576030\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_3B.log\", \"submitted_at\": \"2026-05-15T14:46:52.136Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-3B\", \"data_path\": \"/root/contamcal-irt-calibration/exp002/\", \"data_count\": \"12 tasks (4 dosages x 3 benchmarks)\", \"seed\": \"N/A (signal computation)\", \"signals\": [\"embedding\", \"minkpp\", \"selfcritique\"], \"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"dosages\": [\"d000\", \"d005\", \"d025\", \"d100\"], \"note\": \"ConStat not enabled - 3B eval_results paths have _aligned/_v2 suffixes\"}}, \"exp_001_eval_3B_d000_s42_para_aligned\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:20.059Z\", \"updated_at\": \"2026-05-15T14:52:55.775Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-15T14:51:39.151Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d00
…[truncated 13072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 2023
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T15:02:05.690710+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 8, \"results\": [{\"exp_id\": \"exp_004_sim_sweep_extreme_gamma\", \"success\": true, \"actions\": [\"Job still running (pid=528993)\"]}, {\"exp_id\": \"exp_001_sft_3B_d005_s123\", \"success\": true, \"actions\": [\"Job still running (pid=555931)\"]}, {\"exp_id\": \"exp_001_eval_15B_d005_s123_v2\", \"success\": true, \"actions\": [\"Job still running (pid=566224)\"]}, {\"exp_id\": \"exp_001_eval_15B_d025_s123_v2\", \"success\": true, \"actions\": [\"Job still running (pid=566311)\"]}, {\"exp_id\": \"exp_001_eval_3B_d025_s123_aligned\", \"success\": true, \"actions\": [\"Job still running (pid=576730)\"]}, {\"exp_id\": \"exp_001_eval_3B_d100_s42_para_aligned\", \"success\": true, \"actions\": [\"Job still running (pid=576820)\"]}, {\"exp_id\": \"exp_001_eval_3B_d000_s42_para_aligned\", \"success\": true, \"actions\": [\"Job still running (pid=576973)\"]}, {\"exp_id\": \"exp_002_signals_3B\", \"success\": true, \"actions\": [\"Skipped (created 69s ago < interval 120s)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 19803
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T15:02:05.741711+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_002_signals_3B | — | — | — | — |\\n| exp_001_eval_3B_d000_s42_para_aligned | — | — | — | — |\\n| exp_001_eval_3B_d100_s42_para_aligned | — | — | — | — |\\n\\n## 待处理\\n- exp_001_eval_3B_d005_s123（准备中）\\n- exp_001_eval_3B_d025_s123（准备中）\\n- exp_001_eval_3B_d005_s42_aligned_v2（准备中）\\n- exp_001_sft_15B_d025_s123（准备中）\\n- exp_008_instruct_rl_proxy: RL proxy experiment (D021 Problem 3): Use Qwen2.5-0.5B-Instruct (SFT+RL post-trained) as RL regime data point. 3-regime comparison: base (pretrained) → d000 (SFT) → Instruct (SFT+RL). Compute all 4 signals on Instruct model, observe signal value changes across training regimes. No additional training needed.\\\"（准备中）\\n- exp_003_mmlu_item_aligned_gap（准备中）\\n- exp006-gsm8k-d024-delta（准备中）\\n- exp_006_irt_05B_v2: Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 items + ADVI robustness check. Fixes v1 issues: aligned-only, signal-derived exposure, --max-items.（准备中）\\n- exp_001_eval_05B_d100_aligned_v2（准备中）\\n- exp_001_eval_05B_d000_s42_v6: 0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)（准备中）\\n- …另有 8 项\\n\\n## 近期结论\\n- **exp_001_sft_3B_d025_s123** (success): —\\n- **exp_001_eval_3B_d000_s123_aligned** (success): —\\n- **exp_001_eval_3B_d005_s42_aligned** (success): —\\n\\n## 趋势\\n成功 93 / 负向 2 / 失败 32 / 共 130\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-21977: 无 GPU 信息\\n\\n## 告警\\n- exp_001_eval_05B_d000_s42: 训练失败 — unknown\\n- exp_001_eval_05B_d100: 训练失败 — unknown\\n- exp_001_eval_05B_d100_v2: 训练失败 — unknown\\n- exp_001_eval_15B_d000_s42: 训练失败 — unknown\\n- exp_001_sft_100pct_05B: 训练失败 — unknown\\n- exp_001_sft_d005_05B: 已被终止 — unknown\\n- exp_001_sft_d005_
…[truncated 1372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 19399
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T15:02:05.742477+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-15 10:50 UTC | 更新原因: 1.5B d005+d025 s123 SFT 完成，registry 更新 DONE，需提交 eval\\n\\n## 核心方向\\nContamCal：post-hoc statistical calibration via contamination-augmented 4PL IRT。详见 paper_framing.md。\\n\\n## 投稿目标\\n**EMNLP 2026 ARR May 25**（D006, 距今 10 天）\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-13 通过）+ 审稿进行中\\n- **D036 关键发现**: ARC gamma 负方向 confirmed（3 条独立证据链）→ framing 调整为 benchmark-dependent effects\\n- **Coverage collapse**: 20-33% 即使 oracle，PPP 极值 → 模型可能错误指定，调查中\\n- **跨种子方差**: 0.5B d100 ARC 7.25pp（s42 vs s123）→ multi-seed pooling 必要条件\\n- **Scale story**: 3B d100 ARC=84% vs 0.5B d100=29-37%，scale 显著缓解 contamination forgetting\\n\\n**SFT 进度 (seed=42)**:\\n\\n| 模型 | d000 | d005 | d025 | d100 |\\n|------|------|------|------|------|\\n| 0.5B | ✅ | ✅ | ❌(2x fail) | ✅ |\\n| 1.5B | ✅ | ✅ | ✅ | ✅ |\\n| 3B | ✅(v2) | P2 | P4 | 🏃(v2) |\\n\\n**SFT 进度 (seed=123)**:\\n\\n| 模型 | d000 | d005 | d025 | d100 |\\n|------|------|------|------|------|\\n| 0.5B | ✅ | 🏃(GPU 1) | — | ✅(eval done) |\\n| 1.5B | ✅ | ✅ | ✅ | 🏃(GPU 2) |\\n| 3B | 🏃(v2, GPU 5) | — | — | — |\\n\\n**Signal (exp-002)**: 0.5B ✅ | 1.5B ✅ (12/12 PASS) | 3B 未开始\\n**CPU**: exp-004 v3 ~45% | exp-005 v4 ~92%\\n\\n## ⚠️ Critical Issues (D036)\\n1. **Coverage collapse 20-33%** — PPP=1.0(ARC)/0.0(GSM8K)，4PL+γ additive 模型可能不够。调查路径：(a) N↑ via multi-seed (b) exp-004 at matching N (c) 更灵活 IRT 结构\\n2. **Oracle vs RRF 比较混淆** — N_models 15 vs 8，需匹配 N=8 重跑 oracle\\n3. **GSM8K oracle 诊断 FAIL** — rhat=1.012/ESS=345，需 warmup=2000/samples=2000\\n4. **train_sft.py --gpu 死代码** — args.gpu 解析但未用，需修复\\n\\n## Critical Path\\n```\\n🔴 Coverage collapse 调查 ← 最高优先级\\n  → exp-004 sweep coverage 数据（45% done）\\n  → seed=123 完成后 N≥16 pooled IRT 重跑 → 检查 coverage 是否改善\\n  → 如果 N↑ 仍不够 → 考虑 model misspecification fix\\n\\n并行
…[truncated 2077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 19243
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T15:02:55.387998+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__send_progress",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__send_progress",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T15:02:55.388480+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T15:03:00.930455+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": "{'status': 'DONE'}",
  "limit": "15",
  "fields": "['status', 'conclusion', 'metrics', 'updated_at', 'spec']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "filters": "{'status': 'DONE'}",
    "limit": "15",
    "fields": "['status', 'conclusion', 'metrics', 'updated_at', 'spec']"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T15:03:01.214539+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
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

_source line 16 · 2026-05-15T15:03:01.943258+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_001_sft_3B_d025_s123\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:48:17.888Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir Qwen2.5-3B_d025_s123 --seed 123 --lr 5e-5 --lora-alpha 16 --lora-r 16 --batch-size 2 --grad-accum 8\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": 556016, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d025_s123.log\", \"submitted_at\": \"2026-05-15T11:58:33.067Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"gpu_id\": \"cuda:4\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter/\", \"wall_clock_seconds\": 10087.1, \"gpu_hours\": 2.8}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1401, \"final_token_accuracy\": 0.734, \"total_steps\": 3384}}, \"exp_001_eval_3B_d000_s123_aligned\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:36:58.735Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d000_s123/lora_adapter --output-dir Qwen2.5-3B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 551219, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"exp_001_sft_3B_d000_s123\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"parent\": \"exp_001_sft_3B_d000_s12
…[truncated 13413 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1012
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T15:03:02.044189+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_analysis_run-pooled-4bench-irt-v2_20260515T132925\", \"task_type\": \"analysis:run-pooled-4bench-irt-v2\", \"project\": \"contamcal-irt-calibration\", \"status\": \"running\", \"started_at\": \"2026-05-15T13:29:25.377721+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_investigate_lora-alpha-bug_20260515T150214\", \"task_type\": \"investigate:lora-alpha-bug\", \"project\": \"contamcal-irt-calibration\", \"status\": \"running\", \"started_at\": \"2026-05-15T15:02:15.075057+00:00\", \"ended_at\": null}], \"count\": 2}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 829
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T15:04:08.449781+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__update_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__update_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T15:04:08.450269+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T15:04:09.762663+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T15:04:09.815002+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_9576f59f.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T15:04:13.435716+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
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

_source line 23 · 2026-05-15T15:04:13.486498+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T15:04:20.594155+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
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

_source line 25 · 2026-05-15T15:04:21.350947+00:00_

/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "Glob",
  "elapsed_ms": 756
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T15:04:26.777037+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T15:04:26.777924+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T15:05:10.608546+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 分配 6 / 实际跑 6 | Worker 池 2 (GPU 0 / CPU 2)\n\n**Session #11 启动状态汇报**\n\n**GPU 占用（6/6 全满）：**\n| GPU | 实验 | 类型 | 关键进度 |\n|-----|------|------|----------|\n| 0 | exp_001_eval_15B_d005_s123_v2 | 1.5B d005 s123 aligned eval | ⚡ N≥16 pooled IRT 前置 |\n| 1 | exp_001_eval_15B_d025_s123_v2 | 1.5B d025 s123 aligned eval | ⚡ N≥16 pooled IRT 前置 |\n| 2 | exp_001_sft_3B_d005_s123 | 3B d005 s123 SFT 训练 | 3B 矩阵填充 |\n| 3 | exp_001_eval_3B_d025_s123_aligned + exp_002_signals_3B | 3B eval + 信号计算 | 共享 GPU |\n| 4 | exp_001_eval_3B_d100_s42_para_aligned | 3B d100 s42 para eval | exp_002 S1 前置 |\n| 5 | exp_001_eval_3B_d000_s42_para_aligned | 3B d000 s42 para eval | exp_002 S1 前置 |\n\n**Worker 池（2 个 CPU 任务）：**\n1. `worker_analysis_run-pooled-4bench-irt-v2` — 4-benchmark pooled IRT 分析（已跑 ~1.5h）\n2. `worker_investigate_lora-alpha-bug` — LoRA alpha bug 调查（刚启动）\n\n**Critical path：**\n- cuda:0/1 的 1.5B d005/d025 s123 eval 是 N≥16 multi-seed pooled IRT 的**最后前置**。完成后即可重跑 pooled IRT 检查 coverage collapse 是否改善\n- cuda:2 的 3B d005 s123 SFT 完成后 → 提交 3B d005 s123 aligned eval\n- cuda:3/4/5 的 3B eval 完成后 → 释放给下一批（exp_008_instruct_rl_proxy、0.5B 补测等）\n\n**距 EMNLP ARR May 25 = 10 天。** 等 cron 回调推进。",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 分配 6 / 实际跑 6 | Worker 池 2 (GPU 0 / CPU 2)\n\n**Session #11 启动状态汇报**\n\n**GPU 占用（6/6 全满）：**\n| GPU | 实验 | 类型 | 关键进度 |\n|-----|------|------|----------|\n| 0 | exp_001_eval_15B_d005_s123_v2 | 1.5B d005 s123 aligned eval | ⚡ N≥16 pooled IRT 前置 |\n| 1 | exp_001_eval_15B_d025_s123_v2 | 1.5B d025 s123 aligned eval | ⚡ N≥16 pooled IRT 前置 |\n| 2 | exp_001_sft_3B_d005_s123 | 3B d005 s123 SFT 训练 | 3B 矩阵填充 |\n| 3 | exp_001_eval_3B_d025_s123_aligned + exp_002_signals_3B | 3B eval + 信号计算 | 共享 GPU |\n| 4 | exp_001_eval_3B_d100_s42_para_aligned | 3B d100 s42 para eval | exp_002 S1 前置 |\n| 5 | exp_001_eval_3B_d000_s42_para_aligned | 3B d000 s42 para eval | exp_002 S1 前置 |\n\n**Worker 池（2 个 CPU 任务）：**\n1. `worker_analysis_run-pooled-4bench-irt-v2` — 4-benchmark pooled IRT 分析（已跑 ~1.5h）\n2. `worker_investigate_lora-alpha-bug` — LoRA alpha bug 调查（刚启动）\n\n**Critical path：**\n- cuda:0/1 的 1.5B d005/d025 s123 eval 是 N≥16 multi-seed pooled IRT 的**最后前置**。完成后即可重跑 pooled IRT 检查 coverage collapse 是否改善\n- cuda:2 的 3B d005 s123 SFT 完成后 → 提交 3B d005 s123 aligned eval\n- cuda:3/4/5 的 3B eval 完成后 → 释放给下一批（exp_008_instruct_rl_proxy、0.5B 补测等）\n\n**距 EMNLP ARR May 25 = 10 天。** 等 cron 回调推进。",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T15:05:14.331669+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 3723
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-15T15:05:34.118251+00:00_

Session #11 初始化完成。

**当前态势：**
- 6/6 GPU 全满运行，2 个 CPU Worker 活跃
- Critical path：cuda:0/1 的 1.5B eval 完成 → 触发 N≥16 pooled IRT（coverage collapse 根因调查）
- 已向 Director 汇报启动状态

**注意事项：**
- Registry 有 1.5B eval 的 v1/v2 重复条目（同 PID），cron 回调时需注意去重
- cuda:3 共享了 eval + signals 两个进程，可能影响性能但不会 OOM（信号计算较轻量）

等待 cron/worker 回调推进。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval"
}
```

</details>

---

## Round 2

18 recorded events

### User

_source line 31 · 2026-05-15T18:08:15.113772+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T18:08:24.629236+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
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

_source line 33 · 2026-05-15T18:08:24.680232+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T18:08:27.865677+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
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

_source line 35 · 2026-05-15T18:08:27.966427+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T18:08:28.802781+00:00_

Error: result (262,077 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-9576f59f/096ddfdd-0516-4ac6-bbad-602d15169073/tool-results/mcp-agent-ml-research-read_registry-1778868508664.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-9576f59f/096ddfdd-0516-4ac6-bbad-602d15169073/tool-results/mcp-agent-ml-research-read_registry-1778868508664.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 937
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T18:08:28.903691+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
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

### Tool call

_source line 38 · 2026-05-15T18:08:29.306263+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T18:08:29.707572+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
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

### Tool call

_source line 40 · 2026-05-15T18:08:30.963451+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
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

_source line 41 · 2026-05-15T18:08:34.678867+00:00_

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
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
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

_source line 42 · 2026-05-15T18:08:43.968401+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 7, \"results\": [{\"exp_id\": \"exp_004_sim_sweep_extreme_gamma\", \"success\": true, \"actions\": [\"Job still running (pid=528993)\"]}, {\"exp_id\": \"exp_001_eval_3B_d005_s123_aligned\", \"success\": true, \"actions\": [\"Job still running (pid=580693)\"]}, {\"exp_id\": \"exp_001_sft_d025_3B_v3\", \"success\": true, \"actions\": [\"Job still running (pid=589763)\"]}, {\"exp_id\": \"exp_001_sft_3B_d100_s123_a32_v2\", \"success\": true, \"actions\": [\"Job still running (pid=594489)\"]}, {\"exp_id\": \"exp_001_sft_3B_d100_s42_a32_v2\", \"success\": true, \"actions\": [\"Job still running (pid=593740)\"]}, {\"exp_id\": \"exp_001_sft_3B_d000_v3\", \"success\": true, \"actions\": [\"Job still running (pid=597174)\"]}, {\"exp_id\": \"exp_001_sft_3B_d100_s42_a32\", \"success\": true, \"actions\": [\"Job still running (pid=593745)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 16001
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T18:08:43.969161+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-15T18:07:02Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 167 个实验 — ANALYZING 1, DONE 140, PREPARING 20, RUNNING 6\\n**DONE 分布**: failed 34, killed 4, negative 2, success 100\\n\\n### GPU 占用\\n- **分配**: 6 张 — cqa1-21977:cuda:0, cqa1-21977:cuda:1, cqa1-21977:cuda:2, cqa1-21977:cuda:3, cqa1-21977:cuda:4, cqa1-21977:cuda:5\\n- **实际运行**: 4 张 — cqa1-21977:cuda:2(exp_001_eval_3B_d005_s123_aligned), cqa1-21977:cuda:4(exp_001_sft_3B_d000_v3), cqa1-21977:cuda:1(exp_001_sft_3B_d100_s42_a32_v2), cqa1-21977:cuda:0(exp_001_sft_3B_d100_s123_a32_v2)\\n- **空闲（分配了没跑）**: cqa1-21977:cuda:3, cqa1-21977:cuda:5\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `exp_001_eval_3B_d005_s123_aligned` | cqa1-21977 | cuda:2 | 580693 | `…amcal-irt-calibration/exp_001_eval_3B_d005_s123_aligned.log` |\\n| `exp_001_sft_3B_d000_v3` | cqa1-21977 | cuda:4 | 597174 | `~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_v3.log` |\\n| `exp_001_sft_d025_3B_v3` | cqa1-21977 | ? | 589763 | `—` |\\n| `exp_001_sft_3B_d100_s42_a32_v2` | cqa1-21977 | cuda:1 | 593740 | `…ontamcal-irt-calibration/exp_001_sft_3B_d100_s42_a32_v2.log` |\\n| `exp_001_sft_3B_d100_s123_a32_v2` | cqa1-21977 | cuda:0 | 594489 | `…ntamcal-irt-calibration/exp_001_sft_3B_d100_s123_a32_v2.log` |\\n| `exp_004_sim_sweep_v6` | local | ? | ? | `—` |\\n\\n### 📌 最近完成 (top 5)\\n- `exp_001_sft_3B_d100_s42_a32` [failed] — 2026-05-15T18:00:32\\n- `exp_002_signals_3B_v2` [killed] — 2026-05-15T17:56:45\\n- `exp_005_noise_prop_v4` [negative] — 2026-05-15T17:56:14\\n- `exp_001_eval_3B_d005_s123_para_aligned` [success] — 2026-05-15T16:56:44\\n- `exp_001_eval_3B_d025_s123_para_aligned` [success] — 2026-05-15T16:56:42\\n\\n### 🔴 最近失败原因 
…[truncated 4759 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 15065
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T18:08:44.020660+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-15 10:50 UTC | 更新原因: 1.5B d005+d025 s123 SFT 完成，registry 更新 DONE，需提交 eval\\n\\n## 核心方向\\nContamCal：post-hoc statistical calibration via contamination-augmented 4PL IRT。详见 paper_framing.md。\\n\\n## 投稿目标\\n**EMNLP 2026 ARR May 25**（D006, 距今 10 天）\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-13 通过）+ 审稿进行中\\n- **D036 关键发现**: ARC gamma 负方向 confirmed（3 条独立证据链）→ framing 调整为 benchmark-dependent effects\\n- **Coverage collapse**: 20-33% 即使 oracle，PPP 极值 → 模型可能错误指定，调查中\\n- **跨种子方差**: 0.5B d100 ARC 7.25pp（s42 vs s123）→ multi-seed pooling 必要条件\\n- **Scale story**: 3B d100 ARC=84% vs 0.5B d100=29-37%，scale 显著缓解 contamination forgetting\\n\\n**SFT 进度 (seed=42)**:\\n\\n| 模型 | d000 | d005 | d025 | d100 |\\n|------|------|------|------|------|\\n| 0.5B | ✅ | ✅ | ❌(2x fail) | ✅ |\\n| 1.5B | ✅ | ✅ | ✅ | ✅ |\\n| 3B | ✅(v2) | P2 | P4 | 🏃(v2) |\\n\\n**SFT 进度 (seed=123)**:\\n\\n| 模型 | d000 | d005 | d025 | d100 |\\n|------|------|------|------|------|\\n| 0.5B | ✅ | 🏃(GPU 1) | — | ✅(eval done) |\\n| 1.5B | ✅ | ✅ | ✅ | 🏃(GPU 2) |\\n| 3B | 🏃(v2, GPU 5) | — | — | — |\\n\\n**Signal (exp-002)**: 0.5B ✅ | 1.5B ✅ (12/12 PASS) | 3B 未开始\\n**CPU**: exp-004 v3 ~45% | exp-005 v4 ~92%\\n\\n## ⚠️ Critical Issues (D036)\\n1. **Coverage collapse 20-33%** — PPP=1.0(ARC)/0.0(GSM8K)，4PL+γ additive 模型可能不够。调查路径：(a) N↑ via multi-seed (b) exp-004 at matching N (c) 更灵活 IRT 结构\\n2. **Oracle vs RRF 比较混淆** — N_models 15 vs 8，需匹配 N=8 重跑 oracle\\n3. **GSM8K oracle 诊断 FAIL** — rhat=1.012/ESS=345，需 warmup=2000/samples=2000\\n4. **train_sft.py --gpu 死代码** — args.gpu 解析但未用，需修复\\n\\n## Critical Path\\n```\\n🔴 Coverage collapse 调查 ← 最高优先级\\n  → exp-004 sweep coverage 数据（45% done）\\n  → seed=123 完成后 N≥16 pooled IRT 重跑 → 检查 coverage 是否改善\\n  → 如果 N↑ 仍不够 → 考虑 model misspecification fix\\n\\n并行
…[truncated 2039 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 14714
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T18:08:44.021413+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/memory.md\", \"content\": \"# 项目关键发现与决策记录\\n\\n## ⚡ exp-004 核心结论：Coverage collapse = Model misspecification（2026-05-15）\\n\\nSimulation sweep（66/80 seeds）证明：DGP=模型时 CI95 coverage 90-100%（即使 γ=4.0）。真实数据 coverage 仅 20-33%。\\n→ **coverage collapse 不是 γ 值大导致，而是 additive 4PL+γ 模型与真实 contamination 机制的 misspecification。**\\n这支持 \\\"benchmark-dependent effects\\\" framing，coverage collapse 可作为 model misspecification 的诊断证据。\\n\\n## 1.5B 跨种子一致性（2026-05-15）\\n\\nd025 cross-seed (s42 vs s123, aligned): MMLU Δ=0.21pp, GSM8K Δ=0.15pp, ARC Δ=1.11pp, HumanEval Δ=2.44pp。\\nd005 cross-seed: MMLU Δ=0.17pp, GSM8K Δ=0.00pp, ARC Δ=1.20pp, HumanEval Δ=0.00pp。\\nMC benchmarks 跨种子方差极小（<1.2pp），支持 multi-seed pooling 的统计可行性。\\n**1.5B 双种子矩阵全部就绪**（4 dosage × 2 seeds × 4 benchmarks = 32 数据点）。\\n\\n**对比 0.5B**：0.5B d100 ARC 跨种子方差 7.25pp（ROADMAP 记录），1.5B 显著更稳定——scale up 降低种子敏感性。\\n\\n## D055 Alpha 重跑状态（2026-05-15）\\n\\n**3 个 SFT 全部在跑**：\\n- d025_s42 → 🏃 cuda:5 (exp_001_sft_d025_3B_v3, PID 589763)\\n- d100_s42 → 🏃 cuda:1 (exp_001_sft_3B_d100_s42_a32, PID 593745, 7h+)\\n- d100_s123 → 🏃 cuda:0 (exp_001_sft_3B_d100_s123_a32_v2, PID 594494)\\n\\n**d000_v3 排队**：等 cuda:2/3 eval 完成后提交。\\n\\n**不需重跑**（已 alpha=32）：d000_s123, d005_s42, d005_s123, d025_s123\\n**弃用 d000_v2**（alpha=16），改用原始 d000（alpha=32）\\n\\n## exp-005 确认完成（2026-05-15）\\n\\nv4: 25/25 fits, all converged, conclusion=negative。ME CI width 对 sigma_e 完全不敏感（0.0997–0.1000）。\\nDirector 决策：降级为 appendix robustness check。\\n\\n## Alpha 实际分布（checkpoint 验证结果）\\n\\n| Checkpoint | alpha | seed | D055 处理 |\\n|---|---|---|---|\\n| d000_s123 | **32** ✅ | 123 | 保留 |\\n| d000_s42 | **32** ✅ | 42 | 保留 |\\n| d000_v2_s42 | 16 | 42 | **弃用** |\\n| d005_s123 | **32** ✅ | 123 | 保留 |\\n| d005_s42 | **32** ✅ | 42 | 保留 |\\n| d025_s123 | **32** ✅ | 123 | 保留 |\\n| d025_s42 | 16 ⚠️ | 42 | **重跑中** |\\n| d100_s123 | 16 ⚠️ | 123 | **重跑中** |\\n|
…[truncated 1233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 14313
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T18:08:44.021836+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"contamcal-irt-calibration\", \"section\": \"execution\", \"config\": {\"execution\": {\"gpu_ids\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\", \"cuda:4\", \"cuda:5\"], \"project_path\": \"/root/contamcal-irt-calibration\", \"servers\": [\"cqa1-21977\"]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 13058
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T18:08:44.122463+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 9443
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-15T18:10:04.433657+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 服务器只有 **cqa1-21977**，GPU 白名单 **cuda:0–5**（6× RTX 4090D）
- LoRA **alpha=32** 是全项目标准（D050/D055）。d000_v2 checkpoint（alpha=16）已弃用，禁止引用
- 3B d025_s42 / d100_s42 / d100_s123 的旧 alpha=16 SFT 结果**不可用于论文**，必须等 v3/a32 版本完成
- exp_001_sft_3B_d100_s42_a32（PID 593745）在 cron 中显示 running 但 registry 标记 failed——下一个 session **必须先诊断这个矛盾**，可能是僵尸进程占 GPU
- 投稿目标 **EMNLP 2026 ARR May 25**，距今 10 天

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-21977 | 工作目录 `/root/contamcal-irt-calibration` | 数据盘 `/root/autodl-tmp/`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- **激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型缓存**: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-{0.5B,1.5B,3B}`
- **SFT checkpoints**: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-{SIZE}_{DOSE}_{SEED}/lora_adapter`
- **Eval 结果**: `/root/autodl-tmp/exp001/eval_results/`
- **W&B**: 未在 config 中看到专门配置，需要 Worker 确认
- **活跃进程**:
  - PID 594489 — exp_001_sft_3B_d100_s123_a32_v2 (cuda:0)
  - PID 593740 — exp_001_sft_3B_d100_s42_a32_v2 (cuda:1)
  - PID 580693 — exp_001_eval_3B_d005_s123_aligned (cuda:2)
  - PID 597174 — exp_001_sft_3B_d000_v3 (cuda:4)
  - PID 589763 — exp_001_sft_d025_3B_v3 (cuda:5)
  - PID 593745 — exp_001_sft_3B_d100_s42_a32 (⚠️ 见红线，registry=failed 但 cron=running)
  - PID 528993 — exp_004_sim_sweep_extreme_gamma (CPU, simulation)
- **空闲 GPU**: cuda:3（确认空闲），cuda:5 可能被 d025_v3 占用（report 显示 "?" 但 memory.md 说 cuda:5）

### 3. 📊 当前状态
**刚做完**: D055 alpha=32 重跑批次提交（3 个 3B SFT），d000_v3 已提交 cuda:4。exp_005_noise_prop_v4 完成（negative，降级 appendix）。exp_002_signals_3B_v2 被 kill（D057 GPU 冲突）。

**Registry 概览**: 167 实验 — RUNNING 6, ANALYZING 1, PREPARING 20, DONE 140（success 100, failed 34, negative 2, killed 4）

**RUNNING GPU 实验**:
| Exp | GPU | 说明 |
|-----|-----|------|
| exp_001_sft_3B_d100_s123_a32_v2 | cuda:0 | D055 alpha=32 重跑 |
| exp_001_sft_3B_d100_s42_a32_v2 | cuda:1 | D055 alpha=32 重跑 |
| exp_001_eval_3B_d005_s123_aligned | cuda:2 | 3B d005 s123 aligned eval |
| exp_001_sft_3B_d000_v3 | cuda:4 | 3B d000 s42 alpha=32 baseline |
| exp_001_sft_d025_3B_v3 | cuda:5 | D055 alpha=32 重跑 |

**CPU**: exp_004_sim_sweep_extreme_gamma（simulation，验证 extreme γ 下 coverage）

**等待中**: 0 个 Worker 在跑。无 pending Director 决策。20 个 PREPARING 实验排队。

### 4. 📋 待办（条件触发式）
- **exp_001_sft_3B_d100_s42_a32 状态矛盾** → 立即 SSH 检查 PID 593745 存活状态；如已死则确认 registry failed + 清理 cron；如活着则更新 registry 为 RUNNING
- **任一 3B SFT（d025_v3 / d100_s42_v2 / d100_s123_v2 / d000_v3）完成** → spawn worker 提交对应 eval（aligned + para_aligned 两轮），命令模板见 memory.md
- **exp_001_eval_3B_d005_s123_aligned 完成** → 接着提交 para_aligned eval（同 checkpoint，加 --paraphrase-dir）
- **d025_v3 eval 完成** → 提交 exp_001_sft_3B_d025_s42_a32 的排队 eval
- **所有 3B alpha=32 SFT+eval 完成** → spawn worker 跑 exp_002_signals_3B_v3（信号计算），然后 multi-seed pooled IRT（exp_006）检查 coverage 是否改善
- **exp_004_sim_sweep_extreme_gamma 完成** → 分析 extreme γ 下 coverage，更新 D056 结论
- **GPU 空出** → 优先级：(1) exp_001_sft_3B_d025_s42_a32 (2) exp_001_sft_3B_d100_s123_a32 (3) exp_008_instruct_rl_proxy (4) 15B experiments
- **Worker 池 = 0 → 失职** → 立即 spawn ≥2 个 Worker 做非 GPU 任务（代码审查、文献联动、paper 准备）

### 5. 🎯 战略上下文
**核心 story**: ContamCal — post-hoc IRT calibration for contamination detection. 4PL+γ additive model 在真实数据上 coverage collapse（20-33%），已确认为 model misspecification（D056），framing 调整为 "benchmark-dependent contamination effects"。

**决策链**:
- D056: Coverage collapse = model misspecification（不是 γ 值问题）
- D055: 3B 只需重跑 3 个 SFT（d025_s42, d100_s42, d100_s123），其余已 alpha=32
- D053: 废弃联合/Stratified IRT，论文只引用 per-benchmark 独立 IRT
- D052: Gamma 方向不稳定，不 pivot，等更多数据

**易错点**:
1. **不要混用 alpha=16 和 alpha=32 的 checkpoint 做对比**——memory.md 有完整表格，每次引用 checkpoint 前核对
2. **d000 有两个 checkpoint**: 原版（alpha=32，保留）和 v2（alpha=16，弃用）。eval 必须用原版
3. **Oracle vs RRF 比较需匹配 N=8**——当前 oracle N=15，RRF N=8，直接对比不公平
4. **GSM8K oracle 拟合需要 warmup=2000/samples=2000**——默认参数 rhat 不合格
5. **exp_004 sim sweep 和真实 IRT 的 N_models 不同**——sim 用固定 N，真实数据 N 随 benchmark 变化
6. **距 EMNLP ARR 只有 10 天**——所有非 critical path 任务（如 15B 扩展、新 benchmark）都应降优先级，聚焦 3B alpha=32 完整矩阵 + pooled IRT + paper 写作
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:exp_008_base_pretrained_15B_eval"
}
```

</details>

---
