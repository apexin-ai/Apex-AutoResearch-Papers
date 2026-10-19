# reviewer / loop_7.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`e0f5e58541cd515c4f44.json`](../../sessions/e0/e0f5e58541cd515c4f44.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-05-15T09:53:16+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-18228 四个 GPU 分配：cuda:0=obsonly-norm03-r2, cuda:1=scalar-r2, cuda:2=seed43, cuda:3=obs-only-r3。**不要根据 ROADMAP 表格判断 GPU 分配**——ROADMAP 之前四个 GPU 全写反了，以 registry + nvidia-smi 为准。
- bjb2-40593 只有 1 张 RTX 4090 D（cuda:0）。该卡已出过 3 次双进程冲突（ghost PID 211962、obsonly-norm03 误杀、norm-0p3-r3 重复部署）。部署前**必须** nvidia-smi 确认 GPU 空闲。
- 命名歧义陷阱：**norm03 = 0.3，norm003 = 0.03**。已因此导致误杀事故（worker 把 0.3 当 0.03 的重复）。核实时看 `--max_correction_norm` 实际值，不信实验名。
- bjb1-18228 上所有 restart 实验都有 output_file bug：`--output_file` 指向 log 路径，完成时 JSON 覆盖 log。已有 .bak 备份（scalar-r2, obs-only-r3, small-r2），但 seed43 和 norm03-r2 没有 .bak。

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4× RTX 4090): conda base, `/root/miniconda3/bin/python`, 项目 `/root/acr-vla-conformal-refinement`, logs `/root/runs/acr-vla-conformal-refinement/`
- **bjb1-32546** (6× RTX 4090): conda base, 项目 `/root/acr-vla-conformal-refinement`, logs 分两处——旧的在 `项目/logs/`，新的在 `/root/runs/acr-vla-conformal-refinement/`
- **bjb2-28827** (6× RTX 4090): conda base, logs `/root/runs/acr-vla-conformal-refinement/`
- **bjb2-40593** (1× RTX 4090 D): conda base, logs `~/runs/acr-vla-conformal-refinement/`
- 模型：SmolVLA `/root/autodl-tmp/models/smolvla_libero/`；CRM checkpoints `/root/autodl-tmp/checkpoints/crm_v3_norm/{perdof,obs_only,scalar_unc}/crm_best.pt`
- HF cache: `/root/autodl-tmp/.hf_cache`（所有服务器）
- 本地 workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/`
- 活跃进程（截至 ~10:00 UTC）：
  - bjb1-18228: PID 325264 (norm03-r2, cuda:0), PID 311886 (scalar-r2, cuda:1), PID 341873 wrapper (seed43, cuda:2), PID 312425 (obs-only-r3, cuda:3)
  - bjb1-32546: 6 个 eval 进程（reconvla/perdof/obs-only/scalar/obs-only-norm02/vla-mean on cuda:0-5）
  - bjb2-28827: 6 个 magnitude sweep 进程
  - bjb2-40593: PID 227434 (obsonly-norm003-b2, cuda:0)

### 3. 📊 当前状态
刚完成全服务器紧急状态快照并上报 Director。关键进展：

**已完成（DONE）**：
- eval-argmin-only-spatial-r2: argmin 10-task = **34%**
- eval-acr-spatial-v4-small-r2: perdof 10-task = **35%** (+1pp vs argmin，kill criterion triggered)

**即将完成（~30min）**：
- eval-acr-spatial-v4-obs-only-r3 (cuda:3): T6=90%, T7=0%, T8=20%, T9 进行中。投影 35-36%。

**RUNNING（16 个）**：
- bjb1-18228: 4 个（norm03-r2 3/10, scalar-r2 T7进行, seed43 1/10, obs-only-r3 T9进行）
- bjb1-32546: 6 个 object eval（均 3-5/10 tasks）— **obs_only 16% 领先 argmin 8% (+8pp)**
- bjb2-28827: 6 个 magnitude sweep（均 4-5/10 tasks）
- bjb2-40593: 1 个 obsonly-norm003-b2（2/10 tasks）

**等待中**：
- obs-only-r3 cron:on_complete → 最终 spatial obs_only 10-task 结果
- Director 最终 framing 裁决（等 spatial 完成 + object 更多数据）

### 4. 📋 待办（条件触发式）
- obs-only-r3 完成 → 核实 10-task SR，上报最终 spatial 四方对比表（argmin 34% / perdof 35% / obs_only ?% / scalar 待完成）
- scalar-r2 完成 → 合并 parent (T0-T2: 17/30) + restart (T3-T9)，更新四方表
- object eval 达到 7+ tasks → 重新做 Fisher exact test，判断 obs_only vs argmin 是否统计显著
- obs_only object 5-task avg 维持 ≥ argmin+5pp → 支持 Scenario C（论文转向 "learned correction" story）
- obs_only object 回落到 argmin ±3pp → Scenario 4（项目 dead），立即上报
- seed43 完成 → 对比 seed42 obs_only 结果，评估种子稳定性（如果差异 >5pp → [severity: warning] 结论不稳）
- 任何新部署到 bjb1-18228 cuda:0/cuda:2 → 检查 GPU 是否有遗留进程

### 5. 🎯 战略上下文
**核心结论链**：D018(归一化修复) → D019(magnitude control 关键) → D022/D023(砍到单 Claim) → D025(52.5% 数据作废) → D027(perdof=argmin=42.9% on spatial, per-DOF claim dead)

**项目现状**：per-DOF conformal 的核心卖点在 spatial 上已死（perdof 35% ≈ argmin 34%）。项目存活完全依赖 **obs_only CRM correction 在 object benchmark 上的表现**（当前 5 tasks: 16% vs argmin 8%, +8pp）。Scenario C 是唯一可行论文方向："observation-conditioned learned correction significantly improves VLA robustness"，per-DOF 降级为 negative result / ablation。

**最容易判断错的事**：
1. **不要把 magnitude sweep partial results 当最终结论** — 多数只有 4-5/10 tasks，且 T0/T1 是最容易的 tasks，会严重高估 SR。spatial 10-task 完整结果（perdof 35%）比 7-task partial（42.9%）低了 8pp。
2. **不要把 obs_only spatial ~35% 当作失败** — spatial 上所有方法都在 34±2pp，CRM 确实没用；但 object 上 obs_only 16% vs argmin 8% 的 gap 是真的。两个 benchmark 的结论可能不同。
3. **命名混乱是本项目最大运维风险** — norm03 vs norm003，r2 vs r3 vs b2，不同 log 路径。核实任何实验前先看 `--max_correction_norm` 和 `--seed` 实际参数值。


---
