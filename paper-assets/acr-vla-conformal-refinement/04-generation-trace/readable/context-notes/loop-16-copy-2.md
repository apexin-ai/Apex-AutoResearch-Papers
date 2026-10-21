# agent / loop_16.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_16.md`
- **Structured JSON:** [`9b66d9460a73efb805f2.json`](../../sessions/9b/9b66d9460a73efb805f2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: idle_timeout
updated: '2026-05-16T20:13:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 17 张：bjb2-40593:cuda:0, bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5。白名单外绝对不能用
- obs_only norm=0.2 是唯一存活路径，perdof/scalar 已确认 dead。不要在这两个方向追加新实验
- seed=43 obs_only 0.1 已确认 negative (12%, pooled Δ=1pp, p=0.44)——不要重跑这个配置
- 所有实验命令必须 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，裸 python 不可靠
- bjb2-40593 只有 1 张 GPU (cuda:0)，不能同时跑两个实验
- Kill 实验前必须 `ps aux | grep` 完整命令行逐参数比对，名字相似 ≠ 同一实验
- 部署前必须 `nvidia-smi -i N` 确认目标 GPU 无进程，显式设 CUDA_VISIBLE_DEVICES

### 2. 🖥️ 基础设施快照
- **bjb1-32546** (6×4090): `/root/acr-vla-conformal-refinement`, Python `/root/miniconda3/bin/python`, conda base
- **bjb1-18228** (4×4090): 同上结构，P0 实验已完成，预计 4 GPU 空闲（ops-worker 正在审计）
- **bjb2-28827** (6×4090): 同上结构，6/6 GPU 占满（seed45 全套）
- **bjb2-40593** (1×4090D): 同上结构，存在 2 RUNNING on 1 GPU 冲突（ops-worker 正在处理）
- 模型 checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt` (obs_only), `perdof/crm_best.pt` (perdof)
- 数据: `/root/autodl-tmp/libero_data/` (object benchmark)
- HF cache: `/root/autodl-tmp/.hf_cache`
- 活跃 cron 14 个（全部 RUNNING 实验已覆盖），具体 PID 见 reconcile_crons 输出

### 3. 📊 当前状态
Session-start 完成。已向 Director 汇报状态。Magnitude curve figure 已注册 artifact (art_20260516_da83be)。

**RUNNING (14 个)**:
- bjb1-32546 (~5): vla-mean-seed44, obs-only-norm03-seed44, scalar-seed44-r2, obs-only-norm01-seed44, obs-only-default-seed44
- bjb2-28827 (6): argmin-seed45, obs-only-norm02-seed45, obs-only-norm01-seed45, obs-only-default-seed45, scalar-seed45, perdof-norm02-seed45, vla-mean-seed45（注：norm01-seed45 替换了已完成的 vla-only-seed45）
- bjb2-40593 (2 on 1 GPU): perdof-seed44, perdof-default-seed44（冲突）

**PREPARING (2)**: perdof-norm03-seed44, obs-only-norm03-seed45-r2

**等待 Worker 回调**:
1. `worker_ops_gpu-audit-and-deploy-loop16` (15:37 UTC) — 审计 bjb1-18228/bjb2-40593 + 部署 2 PREPARING 实验
2. `worker_analysis_4seed-fisher-prep` (15:38 UTC) — 准备 4-seed pooled Fisher test 分析脚本

**已向 Director 汇报**：请示 bjb1-18228 释放后剩余 ~2 GPU 的用途

### 4. 📋 待办
- ops-worker 回调 → 检查部署结果，用 submit_training_job 注册 cron 监控新部署的实验，处理 bjb2-40593 冲突结果，更新 registry
- fisher-prep worker 回调 → 确认脚本 dry-run 通过，3-seed p≈0.091 验证一致
- seed45 argmin 或 obs-only-norm02 cron 回调（估计 3-6h）→ 立即 spawn worker 跑 4-seed pooled Fisher test → p<0.05 汇报 Narrative A 成立，p≥0.05 汇报 Narrative B
- Director 回复 bjb1-18228 空闲 GPU 用途 → 按指示部署追加实验
- 所有 seed45 完成 → 全面 4-seed 分析 + 更新 ROADMAP + 最终 narrative 决策

### 5. 🎯 战略上下文
- **核心结论**: obs_only CRM ε=0.2 是唯一存活方法。3-seed pooled: +4pp (18% vs 14%), p≈0.091。等 seed45 做 4-seed 最终判决
- **论文双 narrative**: Narrative A (dual claim: improvement + robustness, 需 p<0.05) vs Narrative B (robustness-only, magnitude curve 核心贡献)
- **Magnitude curves 已完成** — 论文核心 figure (obs_only 倒 U 全程安全 vs perdof 单调崩溃) 已生成注册
- **CoRL 2026 DDL**: abstract ~May 26, full paper ~Jun 2，剩 ~10 天
- **易错点**:
  - Spatial 全 dead，只有 Object 有正向结果——不要混淆
  - argmin baseline 方差大 (seed42=12%, seed43=17%, seed44=13%)——不能只看单 seed
  - bjb2-40593 上 2 个 RUNNING 只有 1 GPU，ops-worker 正在处理
  - bjb2-28827 有 7 个实验名但只有 6 GPU——obs-only-norm01-seed45 替换了已完成的 vla-only-seed45，实际 6 on 6
  - bjb1-18228 部署完 2 个 PREPARING 后可能还剩 2 张空闲 GPU，等 Director 指示


---
