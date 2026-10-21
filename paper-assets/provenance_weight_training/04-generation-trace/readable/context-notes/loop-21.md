# agent / loop_21.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_21.md`
- **Structured JSON:** [`85b236351c9891e2fddb.json`](../../sessions/85/85b236351c9891e2fddb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: idle_timeout
updated: '2026-05-25T09:33:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 `cuda:0/1/2/3` on `westd-41312`，其他设备号/服务器禁用
- 投稿目标：**EMNLP 2026 ARR May 25**（今天是 DDL）——论文已在 Round 13 审稿循环中，score 3.0 (Findings)
- `submit_training_job` 不支持 shell builtin（`source`/`conda activate` 全不行），用绝对路径 `/root/miniconda3/bin/python`
- eval 数据路径：`data/human/eval_holdout.jsonl`（NOT `data/eval_holdout.jsonl`）
- output_dir：`/root/autodl-tmp/output/models/`（NOT `/root/autodl-tmp/provenance_weight_training/output/models/`）
- eval 用 bfloat16（不是 float16），float16 在 wiki 大数据量下溢出 NaN
- 提交实验前必须 `df -h` 预检 `/root/autodl-tmp`（250GB，曾因 checkpoint 占满导致 4 实验同时崩溃），所有实验加 `--save_total_limit 2`
- 15 个 PREPARING 状态实验是历史残留（stale），不要尝试恢复或提交它们

### 2. 🖥️ 基础设施快照
- **服务器**：westd-41312，4× RTX PRO 6000 96GB
- **工作目录**：`/root/provenance_weight_training`
- **Python**：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- **激活**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **HF cache**：`/root/autodl-tmp/.hf_cache`
- **模型 checkpoint 目录**：`/root/autodl-tmp/output/models/`
- **数据**：`/root/provenance_weight_training/data/` (scored_data.jsonl, human/, synthetic/)
- **W&B**：项目内已配置，但部分实验未开 W&B（cron 会误判 failed，需 tail_training_logs 二次确认）
- **活跃进程**：无。0 RUNNING，0 cron，0 Worker。4 GPU 全部空闲待命

### 3. 📊 当前状态
**DDL 当天。** 论文处于 Round 13 审稿响应阶段，score 3.0 (Findings)。

**已完成的关键突破**：
- N=5 seeds 统计显著性：Δ=-0.023±0.006, p=0.0012, p_BH=0.011 < 0.05 ✓（解决了 Round 13 核心瓶颈 "N=3 BH 不显著"）
- Figure CRITICAL 修复（Fig 2 + Fig 4）已通过 Reviewer 审查 (05-24 04:58 UTC)
- D&R 阈值扫描全部完成：q>0.3 (17.25) / q>0.5 (17.291) / q>0.7 (17.32)，均显著优于 Uniform (17.694)
- Random-subset baseline done：holdout_ppl=17.694（= Uniform），确认 D&R 优势来自 multi-epoch exposure

**待完成（ROADMAP 未勾选）**：
- 论文更新 N=5 统计量 — Paper Agent 已派单但未见完成回调
- OOD eval (OWT/Wiki) adaptive seeds — Worker 状态不明（无 running worker）
- ρ=0.6 p 值标注 "uncorrected" / secondary analysis

**Registry 总览**：269 实验，254 DONE (175 success / 14 negative / 42 failed / 23 killed)，15 PREPARING (stale)，0 RUNNING

### 4. 📋 待办（条件触发式）
- Paper Agent N=5 更新回调到达 → 检查论文 results.tex 是否已更新统计量 + abstract 是否 ≤200 words → 如未完成则重新派 Worker
- Director 要求提交论文 → 确认所有 ROADMAP 未勾选项完成状态，汇报遗留项
- Director 分配新实验（如 OOD eval / ρ=0.6 标注） → 提交到 4 空闲 GPU
- 收到 Round 14 审稿意见 → 加载 rebuttal skill，分析 reviewer comments

### 5. 🎯 战略上下文
**核心结论链**：
- D115: 论文转为 analysis paper — "When, why, and how does detect-and-reweight work?"
- 贡献排序：(1) Epoch confound >95% (2) Detector requirements: calibration+discrimination (3) Mechanism decomposition: minimum intervention > maximization (4) Adaptive b* tool
- D130: Round 13 响应策略 = 补 N=5 seeds + random-subset baseline（两者均已完成）
- D129: α_eff 定义从 binary indicator 改为 continuous (1-q_i)

**审稿历史**：R8: 2.5 → R9: 3.0 → R10: 3.0 → R12: 3.0 → R13: 3.0 — 持续在 Findings 线上

**易错点**：
- cron 误判：无 W&B 的实验被 cron auto-resolve 为 failed，必须 tail_training_logs 验证真实结论（已发生 2 次：permuted_score_control_seed42, contamination_20_tau07_seed42）
- 15 个 PREPARING 实验是 stale 的，不要当作待提交任务
- ρ=0.3 是 transition zone（adaptive 中性），ρ=0.2 是 negative → 论文 scope 限制为 ρ≥0.4
- tau07_seed 和 adaptive_seed 的 n_min 可能不一致（memory.md 有详细说明），严格一致用 adaptive_fix_seed 系列
- Random-subset baseline holdout_ppl=17.694 恰好等于 Uniform，但 OOD 指标 (owt=18.349, wiki=15.317) 与 Uniform 不同，汇报时注意区分


---
