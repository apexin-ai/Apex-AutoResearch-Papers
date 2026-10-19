# agent / loop_13.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`8b08524115f465c9efe6.json`](../../sessions/8b/8b08524115f465c9efe6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-16T04:50:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格执行：bjb2-40593:cuda:0, bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5（共 17 张）
- submit_training_job 命令必须用 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 MUJOCO_GL=egl python -u ..."` — tmux 用 sh 不是 bash，缺 conda activate 必 EXIT_CODE=127
- seed=44 实验已经历 r1（127 失败）→ r2（被我误杀）→ r3（当前在跑）。不要再杀 -r3
- Negative 结果不得默默跑下一个实验——必须先产出 Framing 提案给 Director
- D037 已解除 D036 hold：零纠正确认为 CRM 效果弱非代码 bug

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4×4090): 工作目录 `/root/acr-vla-conformal-refinement`, conda base `/root/miniconda3`
- **bjb1-32546** (6×4090): 同上路径，account=root
- **bjb2-28827** (6×4090): 同上路径，account=root
- **bjb2-40593** (1×4090D): 同上路径，account=root
- 模型 checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/{obs_only,perdof,scalar}/crm_best.pt`
- HF cache: `/root/autodl-tmp/.hf_cache`
- 产出目录: 各服务器 `logs/` 下 JSON 结果文件

### 3. 📊 当前状态
**刚完成**: 诊断 seed=44 三组实验 EXIT_CODE=127（缺 conda activate），已用正确命令重新提交 -r3/-r2。已向 Director 汇报。

**RUNNING（17 个实验占满 17 GPU）**:
- **Seed=43 组**: eval-perdof-object-seed43 (bjb1-18228:1), eval-vla-mean-object-seed43 (bjb1-32546:1), eval-scalar-object-seed43 (bjb1-32546:2), eval-obs-only-object-norm02-seed43-r2 (bjb1-32546:3)
- **Seed=44 组（刚重提交）**: eval-argmin-object-seed44-r3 (bjb1-18228:3), eval-obs-only-object-norm02-seed44-r3 (bjb1-18228:2), eval-vla-only-object-seed44-r2 (bjb2-40593:0)
- **Object magnitude sweep**: eval-mag-obsonly-norm03-object, eval-mag-obsonly-norm005-object, eval-mag-obsonly-norm003-object, eval-mag-perdof-norm02-object, eval-mag-perdof-norm005-object, eval-mag-perdof-norm003-object, eval-mag-perdof-norm03-object-r3, eval-mag-perdof-norm02-seed43-object-r3
- **默认配置**: eval-acr-object-v4-default-r2 (bjb1-18228:0), eval-acr-object-obs-only-default (bjb1-32546:4)

**等待**: 所有实验的 cron 完成回调。无 Worker 在跑。无待处理 Director 决策。

### 4. 📋 待办
- Seed=44 三方实验完成 → 与 seed=42/43 做 pooled Fisher exact test + bootstrap CI，汇报 Director 统计显著性结论
- Seed=43 六方全部完成（目前 4/6 partial） → 同上 Fisher test，若 p<0.05 claim 成立，p=0.05-0.10 需 seed=44 补强，p>0.10 调整 claim
- Object magnitude sweep 完成 → 生成 norm sensitivity curve（fig3 数据），更新 ROADMAP
- 任何实验 conclusion=negative → 按 red-section 规范产出 Framing 提案，**不动 paper**
- Figure 生成（fig1 WIP, fig2/fig3 pending）→ 数据就绪后 spawn Worker 画图
- 全部数据就绪 → 更新 Paper Results section + Abstract 最终版

### 5. 🎯 战略上下文
- **核心结论**: obs_only CRM 是唯一存活路径。Per-DOF conformal claim 已死。Story: sample-then-correct > sample-then-select, obs features > conformal features (honest negative)
- **投稿目标**: CoRL 2026, abstract DDL ~May 26, full paper DDL ~Jun 2。剩 11 天
- **关键数字**: Object obs_only 0.2 = 22% (+10pp over argmin 12%) = PROJECT HIGH (seed=42)。Spatial 全 CRM dead (argmin 34%, obs_only 35%, +1pp)
- **D035 危机**: pooled seed42+43 Δ=1pp, p=0.89 — 统计不显著。D037 解除 hold 后部署 seed=44 补强。如果 3-seed pooled 仍不显著，需要调整 claim scope（可能从 "statistically significant" 退到 "consistent trend"）
- **易踩的坑**: (1) submit 命令忘记 conda activate → EXIT_CODE=127 (2) 前一 session 可能已提交 -r2 重试，新 session 不要盲目再提交导致 duplicate session 错误 (3) seed=43 obs_only partial 8.3% 远低于 seed=42 的 19%，但剩余 tasks 在 seed=42 中 SR 较高，不要过早下负向结论


---
