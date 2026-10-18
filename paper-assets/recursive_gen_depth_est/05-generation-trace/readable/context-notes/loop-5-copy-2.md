# agent / loop_5.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`527c088395bed010fb1c.json`](../../sessions/52/527c088395bed010fb1c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-15T05:22:13+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：gpu-6000pro-2 cuda:0 和 cuda:1，禁止使用其他卡
- 服务器环境是 conda（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），不是 venv，不要创建 .venv
- 模型路径必须在 `/root/autodl-tmp/models/` 下，数据/checkpoint 在 `/root/autodl-tmp/recursive_gen_depth_est/`
- DCOL 的 margin_lr 不能超过 1e-4（1e-3 导致 v1 embedding collapse，已验证）
- OLMo 用 `olmo-1b-hf` 目录，不是 `olmo-1b`

### 2. 🖥️ 基础设施快照
- 服务器：gpu-6000pro-2，2× RTX PRO 6000 Blackwell 98GB
- 工作目录：`/root/autodl-tmp/recursive_gen_depth_est`
- Python：`/root/miniconda3/bin/python`，conda base 环境
- 模型路径：`/root/autodl-tmp/models/{gpt2-xl, olmo-1b-hf, pythia-1.4b, deberta-v3-large}`
- HF cache：未特别设置（AutoDL 需设 `HF_HOME=/root/autodl-tmp/.hf_cache`）
- 活跃进程：dcol_deberta_003 (PID 241769, cuda:1, tmux session)
- Cron：dcol_deberta_003 监控中（reconcile 确认 still running）

### 3. 📊 当前状态
**刚发生**：gpt2xl_topk50_001 进程正常退出，cron 已转 ANALYZING。我派了 Worker (`worker_analysis_gpt2xl_topk50_001_20260515T021757`) 去服务器读取结果，但 Worker 发现 pipeline 只完成了生成步骤，分类可能没跑完（Worker 第 14 轮仍在 ssh_read_only 探查中）。**这个 Worker 的回调必须处理**——结果可能需要手动补跑分类步骤。

**Registry 状态**：
- `gpt2xl_topk50_001` — ANALYZING，等 Worker 回调确认指标（或确认需要补跑分类）
- `dcol_deberta_003` — RUNNING on cuda:1 (PID 241769)，DCOL v3 retry #2（v1 collapse, v2 OOM）
- `olmo_temp09_002` — PREPARING/killed（无需处理，已取消）

**活跃 Worker**（4 个 running）：
1. `worker_analysis_gpt2xl_topk50_001` — 分析实验结果，可能发现分类未完成
2. `worker_ssh_zeroshot_baseline_dryrun` — zero-shot baseline 准备
3. `worker_code_dcol_v4_fix_and_submit` — DCOL v4 代码修复
4. `worker_fix_matrix_analysis_warnings` — 矩阵分析代码 warning 修复

**资源问题**：cuda:0 空闲（gpt2xl_topk50_001 完成后释放），需要立即铺任务。

### 4. 📋 待办（条件触发式）
- `worker_analysis_gpt2xl_topk50_001` 回调 → 如果分类指标完整：update_registry(conclusion/metrics) + update report.md + 向 Director 汇报 3×3 矩阵 9/9 完成 + 反思实验计划 + 文献联动
- `worker_analysis_gpt2xl_topk50_001` 回调 → 如果分类未完成：派新 Worker 在 cuda:0 补跑分类步骤（`python src/classify_features.py` 等）
- cuda:0 空闲 → 3×3 完成后，下一个 GPU 任务应该是 plan_011（depth extension to 5 generations，P1，无 DCOL 依赖）或 plan_008（DeBERTa end-to-end）
- `dcol_deberta_003` 完成回调 → 分析 DCOL v3 结果，判断 DCOL vs RF 提升是否 ≥5pp（<5pp 则 Atlas/EDD 为 primary，DCOL 为 secondary）
- `worker_code_dcol_v4_fix_and_submit` 完成 → 审查 DCOL v4 代码，但 v3 结果出来前不要提交 v4
- 3×3 矩阵 9/9 完成后 → 更新 Atlas v1 数据（加入 gpt2xl_topk50 数据点），重算 monotonicity/EDD/cross-model 指标

### 5. 🎯 战略上下文
- **D001**: MVP PASS，递归深度可区分（Pythia 78.2%）
- **D002**: Dream 审稿 Best=3.0/Median=3.0/Worst=2.5，Atlas/EDD 为 primary contribution，DCOL 为 secondary
- **D004**: 跨策略泛化 claim 从 "strategy-agnostic" 降级为 "strategy-dependent"——top-k 信号衰减显著（Pythia -8.6pp），连续策略（nucleus/temp）接近
- **D006**: 解码策略影响是模型依赖的——Pythia temp09 降 1.9pp，但 GPT-2 XL temp09 反而升 2.1pp
- **D007**: Feature importance top set (p90_ppl, var_surprisal, mean_surprisal, p75_ppl) 跨模型稳定，但 ranking 因模型而异
- **3×3 矩阵趋势**: GPT-2 XL 信号最强（85.4% best），OLMo 中等，Pythia 最弱。Top-k 一致性地削弱信号（所有模型都降）
- **易错点 1**: OLMo cron 有 false failure 先例（子进程 PID 退出被误判），看到 OLMo 实验 "failed" 先验证
- **易错点 2**: gpt2xl_topk50_001 的分析 Worker 报告 pipeline 可能只完成了生成步骤——不要假设分类已跑完，必须确认 results/ 目录有完整输出
- **易错点 3**: DCOL 已失败两次（v1 collapse, v2 OOM 僵尸），v3 在跑——如果 v3 也失败，需要向 Director 提 pivot 方案而不是无限重试


---
