# agent / loop_5.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`80775e32371b3cf9d099.json`](../../sessions/80/80775e32371b3cf9d099.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-14T22:10:15+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb2-40593:cuda:0, bjb1-18228:cuda:0/1/2/3，共 5 张，禁止用其他卡
- submit_training_job 命令必须自带环境激活：`source /root/miniconda3/bin/activate && ...`（bjb2 用 conda，不要假设 .venv）
- bjb2-40593 是 AutoDL 实例，大文件必须放 `/root/autodl-tmp/`，根分区只有 ~30GB
- CRM 训练必须传 `--norm_stats` 参数（D018 教训：未归一化导致 1500x scale 差异，所有 v3 实验依赖此修复）
- ACR-VLA 早期信号低于 baseline（23-26% vs 30%），**不要**在完整 spatial 四路对比表出来前修改 paper framing

### 2. 🖥️ 基础设施快照
- **bjb2-40593**（1× RTX 4090 D）：工作目录 `/root/acr-vla-conformal-refinement`，Python `/root/miniconda3/bin/python`，conda base 环境
  - CRM checkpoints: `/root/autodl-tmp/checkpoints/crm_v3/`（per_dof / scalar_unc / obs_only 三个子目录）
  - CRM cache: `/root/autodl-tmp/crm_cache/`
  - norm_stats: `/root/autodl-tmp/checkpoints/crm_v3/norm_stats.pt`
  - eval 结果: `/root/autodl-tmp/eval_results/`
  - 活跃进程：eval-vla-mean-spatial (PID 143106, tmux, cuda:0)
- **bjb1-18228**（4× RTX 4090）：同样工作目录 `/root/acr-vla-conformal-refinement`
  - 活跃进程：eval-acr-spatial-v3 (PID 197057, cuda:0), eval-acr-object-v3 (PID 197803, cuda:3), eval-argmin-only-spatial (PID 231421, cuda:1), eval-tiny-correction-spatial (PID 232815, cuda:2)
- **W&B**: entity/project 从 project config 读取
- **Cron**: 5 个活跃 cron 分别监控上述 5 个 eval

### 3. 📊 当前状态
**刚做完**：收到 crm-train-v3-obs-only（CRM obs_only v3 归一化修复版）cron 回调，已派 Worker `worker_analysis_crm-train-v3-obs-only_20260514T182913` 分析训练日志 + W&B 指标。**Worker 尚未回调**，registry 仍为 ANALYZING。

**前序 CRM v3 训练结果**（已完成）：per-DOF val_loss=0.009, scalar_unc=0.008, obs_only(v2)=0.018。v3 obs_only 是否因归一化修复而改善是关键问题。

**RUNNING (5)**：
- eval-vla-mean-spatial — 隔离多采样平均贡献（bjb2）
- eval-acr-spatial-v3 — ACR-VLA 核心方法 spatial eval（bjb1:0）
- eval-acr-object-v3 — ACR-VLA object eval（bjb1:3）
- eval-argmin-only-spatial — argmin-only ablation spatial（bjb1:1）
- eval-tiny-correction-spatial — tiny correction ablation spatial（bjb1:2）

**PREPARING (12)**：precompute-v2/v3/v4 shards、eval-spatial-v4-full、eval-object-v6-full、eval-reconvla-spatial-v1 等

**等待中**：Worker analysis 回调 → 更新 registry + 详细汇报 Director

### 4. 📋 待办
- Worker `analysis:crm-train-v3-obs-only` 回调 → 读 conclusion，若 success 则更新 report.md + 对标 experiment matrix；若 negative 则按 red-section 产 Framing 提案
- eval-vla-mean-spatial cron 回调 → spawn worker 分析 VLA-mean baseline 成功率，这是四路对比的关键一路
- eval-acr-spatial-v3 cron 回调 → **最关键数据点**：ACR-VLA 完整 spatial 成功率，决定核心 claim 是否成立（vs baseline 30%）
- eval-acr-object-v3 cron 回调 → object benchmark 数据点（baseline 13%）
- eval-argmin-only-spatial + eval-tiny-correction-spatial 回调 → ablation 数据点
- 5 路 eval 全部完成 → 汇总四路对比表 → 若 ACR-VLA < baseline 确认，需要 framing 调整（D017 已发现 CRM correction 拖累现象）
- Director 若批准 framing 调整 → 读 framing-reaudit skill 做全文 re-audit

### 5. 🎯 战略上下文
- **投稿目标**: ICLR 2027（Sep-Oct 2026 DDL），CoRL 已放弃（D011）
- **核心 claim**: per-DOF conformal statistics enable dimension-selective action correction
- **最大风险**: D017 已确认 CRM correction 全面拖累 baseline（ACR 23-26% vs baseline 30%），SampleConsensus 反而领先（42.9%）。当前 5 路 eval 是归一化修复（D018）后的重跑，如果 ACR-VLA 仍低于 baseline，核心 claim 可能需要 pivot
- **D018 修复链**: CRM 输入未归一化（1500x scale 差异）→ 重训 v3 CRM（per_dof/scalar_unc/obs_only）→ 重跑所有 eval。当前 obs_only 训练刚完成，分析 Worker 在跑
- **易错点**：(1) 不要混淆 v2 和 v3 的 metrics，v3 才是归一化修复后的版本；(2) 四路对比必须等**全部完成**再下结论，不要用 2/10 tasks 的早期信号做决策；(3) SampleConsensus 不是 ReconVLA（D014 已纠正命名）；(4) correction degradation 文献调研已完成（art_20260514_d21dd2），correction clipping/gating 是备选补救方向


---
