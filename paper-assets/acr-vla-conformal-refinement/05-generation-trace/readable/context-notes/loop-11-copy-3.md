# reviewer / loop_11.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`20b7d1097413f58d0a6a.json`](../../sessions/20/20b7d1097413f58d0a6a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-16T15:33:56+00:00'
---

### 1. 🔴 硬约束 / 红线
- registry `conclusion` 字段不可信——bjb2-28827 有系统性 cron:on_failed bug（nohup 进程正常退出→监控误判→auto-resolve 为 failed），bjb1-18228 有 SIGHUP(129) 假阳性。**所有实验完成后必须先查 JSON 输出文件再信 registry**
- eval-argmin-object-seed44-r2 registry 仍标 conclusion="failed"，**实际 13% 成功完成**（JSON 已验证）。勿重跑
- fallback_narrative_draft.md **已废弃**——包含虚构数据。narrative_b_draft.md 是正确版本
- eval-obs-only-object-norm03-seed45 被 SIGTERM 杀死（cuda:3 双进程冲突），需重部署。registry 标 DONE/failed 是正确的（确实没跑完）
- VLA-only seed45 用了 n_rollouts=20（200 rollouts），其他所有实验用 n_rollouts=10（100 rollouts）。统计对比需注意分母差异

### 2. 🖥️ 基础设施快照
- **服务器**：bjb1-18228(4×4090) / bjb1-32546(6×4090) / bjb2-28827(6×4090) / bjb2-40593(1×4090)
- **工作目录**：`/root/acr-vla-conformal-refinement`（所有服务器）
- **Python**：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **CRM checkpoints**：`/root/autodl-tmp/checkpoints/crm_v3_norm/{obs_only,perdof,scalar_unc}/crm_best.pt`
- **SmolVLA**：`/root/autodl-tmp/models/smolvla_libero/`
- **HF cache**：`/root/autodl-tmp/.hf_cache`（需 HF_HUB_OFFLINE=1）
- **日志**：tmux logs `~/runs/acr-vla-conformal-refinement/`，eval JSON `logs/eval_object_*.json`
- **本地 workspace**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/`

### 3. 📊 当前状态
**刚完成**：P0 3-seed 配对数据全部到手（D040），已提交完整 Fisher 分析和 ROADMAP 审查。

**3-seed FINAL**：obs_only ε=0.2 pooled 18% (54/300) vs argmin 14% (42/300)，**+4pp, one-sided p≈0.091**。

**RUNNING（17 个）**：
- bjb1-18228：perdof-seed44(cuda:1), obs-only-norm01-seed45(cuda:0)，cuda:2/3 可能已释放（r4 killed + argmin 完成）
- bjb1-32546(6 GPU)：vla-mean-seed44, obs-only-norm03-seed44, scalar-seed44-r2, obs-only-norm01-seed44, obs-only-default-seed44, **obs-only-norm02-seed45**(cuda:3，4-seed tiebreaker)
- bjb2-28827(5 active)：scalar-seed45, perdof-norm02-seed45, vla-mean-seed45, obs-only-default-seed45, **argmin-seed45**(cuda:5，4-seed tiebreaker)
- bjb2-40593：perdof-default-seed44

**等待**：seed45 obs_only-norm02 + argmin 完成 → 4-seed pooled Fisher → 最终 narrative 决策

### 4. 📋 待办（条件触发式）
- **obs-only-norm02-seed45 + argmin-seed45 完成** → 独立核实 JSON → 4-seed pooled Fisher test → p<0.05 走 Narrative A，p≥0.05 走 Narrative B
- **4-seed power 预估**：seed45 需 gap≥+6pp 才能推 4-seed p<0.05（如 obs≥20%, argmin≤14%），大概率仍 p>0.05，Narrative B 应作为主线准备
- **bjb2-28827 实验完成** → 先查 JSON，不信 cron:on_failed
- **norm03-seed45 重部署** → bjb1-18228 cuda:2 或 cuda:3 释放后可部署
- **Paper Agent 提交章节审查** → 按 5.1 审查维度 + 评分模板执行
- **seed44 其他 norm 实验完成**（bjb1-32546 上 norm01/norm03/default）→ 可构建 multi-seed magnitude curve with error bars

### 5. 🎯 战略上下文
**核心决策链**：D030(spatial dead) → D033(object obs_only +7pp) → D035(ε=0.1 kill) → D038(ε=0.2 唯一配置) → D039(perdof catastrophic) → D040(3-seed p=0.091)

**当前 story**：obs_only CRM 在 object benchmark 上 pooled +4pp over argmin (p=0.091)，magnitude curve 全程安全（13-22%≥argmin 12%）；perdof 崩溃（14→0%）。CoRL DDL: abstract ~May 26, full ~Jun 2。

**易错点**：
- seed42 obs_only=22% 是高 outlier（seed43/44 都是 16%），pooled mean=18% 被 seed42 拉高。论文不能 claim "22% peak" 而不标注这是单 seed 最优
- seed43 argmin=17% 是 argmin 的高 outlier（seed42=12%, seed44=13%），导致 seed43 obs<argmin(-1pp)
- obs_only norm=0.05=13%（低于 norm=0.03 的 16%），magnitude curve 不是 monotonic inverted-U
- scalar CRM seed42≈4%，**低于** VLA-only 12%——"CRM never degrades" 只对 obs_only 成立
- magnitude_curve.pdf 已修复 collapse region 标注（改为 "per-DOF collapse region"），数据全部验证正确
- **4-seed p<0.05 不是大概率事件**——Narrative B（mechanism insight + robustness）应作为主要准备方向


---
