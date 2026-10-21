# agent / loop_25.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_25.md`
- **Structured JSON:** [`f1757db60243c0090ed6.json`](../../sessions/f1/f1757db60243c0090ed6.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 25
reason: idle_timeout
updated: '2026-05-23T21:23:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-32546 GPU 白名单：cuda:0-5；bjb2-28827 GPU 白名单：cuda:0-5；bjb1-18228：cuda:0-3（π0.5 precompute 专用）
- bjb2-40593 磁盘满，excluded，不得在上面启动任何实验
- n_action_steps 必须统一为 1（Object suite 之前有 n_action_steps=50 的实验 SR~51.8% 不可比，已记录为 M063 教训）
- 所有 Object suite 实验结果必须与 VLA-only wrapper 3-seed baseline 对比（正在收集中），不得用旧 baseline
- bjb2-28827 上有 3 个进程未注册（cuda:0 Object Adaptive CRM s42, cuda:1 Object Reconvla K=10 s42, cuda:2 Goal CRM norm=0.05 s42），ROADMAP 已标注 ⚠️，需尽快补注册

### 2. 🖥️ 基础设施快照
- **bjb1-32546** (6×4090)：工作目录 /root/acr-vla-conformal-refinement，Python 路径需 SSH 探查确认（aml-train 镜像用 conda）
- **bjb2-28827** (6×4090)：工作目录 /root/acr-vla-conformal-refinement，同上
- **bjb1-18228** (4×4090)：π0.5 precompute 2048D（object/spatial/goal/long），剩余 26-32h
- 代码仓库：本地 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/
- 活跃 cron 监控（reconcile 确认 11 个）：
  - bjb1-32546: eval-supp-crm-norm02-spatial-s42-r2 (pid=664402), eval-supp-adapt-tau015-spatial-s42-r2 (pid=664686), eval-supp-adapt-tau025-spatial-s42-r2 (pid=665520), eval-supp-adapt-tau035-spatial-s42-r2 (pid=667018), eval-supp-obj-crm005-s42-r2 (pid=669419)
  - bjb2-28827: eval-supp-obj-adapt-s42-r2 (pid=522259), eval-supp-obj-reconvla-s42 (pid=523238), eval-supp-goal-crm005-s42 (pid=524322), eval-object-vla-only-wrapper-s42-r2 (pid=519749), eval-object-vla-only-wrapper-s43-r2 (pid=520493), eval-object-vla-only-wrapper-s44-r2 (pid=521785)

### 3. 📊 当前状态
- 刚收到 `eval-supp-obj-adapt-s42` 失败回调（"Process exited without valid W&B metrics"），已将 registry 更新为 DONE/killed
- 已派 Worker `worker_diagnose_eval-supp-obj-adapt-s42_20260523T044926` 去 bjb2-28827 读日志诊断失败原因，**尚未收到回调**
- r2 版本 (pid=522259) 仍在运行，cron 监控正常
- 11 个实验全部 RUNNING，覆盖：
  - **P0 threshold sweep**：tau=0.15/0.25/0.35 Spatial s42（bjb1-32546）
  - **P0 gating 隔离**：CRM norm=0.2 always-on Spatial s42（bjb1-32546）
  - **P0 Object VLA-only 3-seed baseline**：s42/s43/s44（bjb2-28827）
  - **P1 Object cross-suite**：Adaptive s42, Reconvla s42, CRM norm=0.05 s42（bjb2-28827 + bjb1-32546）
  - **P1 Goal**：CRM norm=0.05 s42（bjb2-28827）
- 尚未向 Director 汇报本次失败（等 Worker 诊断结果后一并汇报）
- Registry 总量：624 实验（成功 364 / 负向 49 / 失败 82）

### 4. 📋 待办（条件触发式）
- Worker 诊断回调到达 → 更新 registry failure_reason → 确认 r2 正常运行 → 向 Director 简要汇报（不需要特别处理，r2 已在跑）
- threshold sweep (tau=0.15/0.25/0.35) 任一完成 → 收集 SR → 与 tau=0.074855 (81.0%) 对比 → 绘 Pareto 曲线 → 确定最优 tau
- CRM norm=0.2 always-on 完成 → 对比 Adaptive 81.0% vs always-on → 量化 gating 机制贡献
- Object VLA-only wrapper 3-seed 全部完成 → 计算 mean±std → 作为 Object suite 所有方法对比的 baseline
- threshold sweep 完成释放 GPU → 立即部署 Spatial multi-seed (s43/s44) Adaptive + CRM norm=0.05 + Reconvla（P0 任务）
- Object cross-suite 实验完成 → 与 Object VLA-only baseline 对比 → 验证跨 suite 泛化
- 所有 P0 实验完成 → 开始写 Experiments section + 生成 main results table

### 5. 🎯 战略上下文
- **投稿目标 CoRL 2026，DDL 2026-05-29，剩余 ≤6 天**
- 核心方法：ACR-VLA = CRM（Conformal Refinement Module）+ Adaptive K，method paper 定位
- 已确认核心结果（单 seed）：Spatial suite Adaptive CRM 81.0% vs VLA-only 78.5%（+2.5pp），但 200 trials 上 +2.5pp ≈ 0.86σ，**multi-seed 是 P0 优先级**
- π0.5 baseline 饱和（94-99%），仅适合 no-harm 验证，不是主要对比对象
- D128 确认 CRM 问题是 overcorrection magnitude（非方向错误），这是方法改进的关键 insight
- **易踩的坑**：
  - bjb2-28827 有 3 个未注册进程（M064/M065），不要误杀它们——它们是有效实验，只是 registry 缺条目
  - Worker 两次假报部署成功（M065 教训），收到 Worker "已部署" 回调后必须用 cron/ps 验证进程确实在跑
  - 4-suite CRM 训练 (bjb1-32546 cuda:3, epoch ~38/50) registry 路径不匹配，需修复但不紧急


---
