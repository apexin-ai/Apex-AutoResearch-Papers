# reviewer / loop_10.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`a8963ea8c71f65cc788d.json`](../../sessions/a8/a8963ea8c71f65cc788d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-16T11:25:31+00:00'
---

### 1. 🔴 硬约束 / 红线
- eval-mag-obsonly-norm03-object 和 eval-mag-perdof-norm005-object registry 标 `conclusion: failed` 但**实际成功**（19% 和 14%），不要信 registry conclusion，要看 JSON 输出文件
- fallback_narrative_draft.md **已废弃**——包含虚构数据（norm=0.5 不存在、obs_only default=0% 实为 17%、norm=0.05=16% 实为 13%）。narrative_b_draft.md 是正确版本
- bjb2-28827 存在 cron:on_failed 系统性 bug：nohup 启动的实验正常完成后进程退出 → 监控检测 "process dead 5×" → auto-resolve 为 failed。后续该服务器实验完成时**必须先查 JSON 文件再信 registry**
- bjb2-28827 GPU 3 当前有双进程冲突（obs_only default seed45 + obs_only norm03 seed45），已报 Director

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
**刚完成**：magnitude sweep 双曲线全部完成（obs_only 6/6 + perdof 6/6），D039 perdof catastrophic collapse confirmed，seed45 全面部署。

**P0 等待中**：
- `eval-obs-only-object-norm02-seed44-r2`（bjb1-18228:cuda:2）— seed44 ε=0.2，~task 5/10，ETA 几小时。**这是项目生死数据点**。
- `eval-argmin-object-seed44-r2`（bjb1-18228:cuda:3）— 配对 baseline，同步进行

**其他 RUNNING**（bjb1-18228）：perdof-seed44(cuda:1), obs-only-norm01-seed45(cuda:0)
**RUNNING**（bjb1-32546）：vla-mean-seed44(cuda:1), obs-only-norm03-seed44(cuda:2), scalar-seed44-r2(cuda:0), obs-only-norm01-seed44(cuda:4), obs-only-default-seed44(cuda:5), obs-only-norm02-seed45(cuda:3)
**RUNNING**（bjb2-28827）：6 个 seed45 实验（scalar/perdof/vla-only/argmin/obs-only-default/vla-mean + norm03 冲突）
**RUNNING**（bjb2-40593）：perdof-default-seed44

### 4. 📋 待办（条件触发式）
- **eval-obs-only-object-norm02-seed44-r2 完成** → 立即独立核实 JSON 数据 → 连同 eval-argmin-object-seed44-r2 结果跑 `three_seed_fisher_analysis.py` → 根据 p 值判断：p<0.05 走 dual claim，p∈[0.05,0.10] 走 Narrative B + 建议加 seed45，p>0.10 escalate
- **bjb2-28827 实验完成** → 先查 JSON 文件确认数据，不信 cron:on_failed（系统性 bug）
- **seed44 全部完成** → 完整 3-seed 六方比较表 + pooled statistics
- **seed45 实验陆续完成** → 如 seed44 p>0.05，立即计算 4-seed pooled Fisher test
- **Paper Agent 提交章节审查** → 按 5.1 审查维度 + 评分模板执行

### 5. 🎯 战略上下文
**核心结论链**：D030(spatial dead) → D033(object obs_only +7pp) → D035(ε=0.1 kill) → D038(ε=0.2 唯一配置) → D039(perdof catastrophic at default norm)

**当前 story**：obs_only CRM 在 ε=0.2 有 inverted-U magnitude curve（13-22%，全程 ≥ VLA-only），perdof 单调崩溃（14→0%）。2-seed pooled obs vs argmin +4.5pp (p≈0.12)。Narrative 走向取决于 seed44。

**易错点**：
- obs_only default norm = **17%**（不是 0%！那是 perdof 的值）——前任 Agent 在 fallback_narrative_draft.md 搞混了这两个
- obs_only norm=0.05 = **13%**（低于 norm=0.03 的 16%），magnitude curve 不是单调的，论文不能 claim "monotonic increase to peak"
- seed43 的 argmin = 17% 是 outlier（seed42=12%, seed44(early)=7.5%），obs_only seed43 = 16% 看似不如 argmin 但其实 argmin 自己高了
- scalar CRM seed42 ≈ 4%，**低于** VLA-only 12%——"CRM never degrades below VLA-only" 只对 obs_only 成立，不是所有 CRM variant
- registry 的 `conclusion` 字段不完全可信，有些标 "failed" 的实际已成功完成，以 JSON 输出文件为准


---
