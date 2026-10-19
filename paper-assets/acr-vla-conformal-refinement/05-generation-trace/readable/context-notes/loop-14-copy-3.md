# reviewer / loop_14.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`a0169fc1bc0209e6d6b0.json`](../../sessions/a0/a0169fc1bc0209e6d6b0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-17T06:43:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-32546 上 eval-acr-object-v4-obs-only tmux session 的日志（`/root/runs/acr-vla-conformal-refinement/eval-acr-object-v4-obs-only.log`）是 obs_only ε=0.1 = 19% 的唯一权威数据源，但该实验未注册到 registry（registry 中 eval-object-v8-full = 13% 是旧版 CRM，不是当前论文使用的数据）
- seed42 是系统性 outlier（obs_only 所有 norm 都偏高 3-6pp）。任何基于 seed42 单 seed 的 claim 都需要多 seed 验证才能定论
- eval-obs-only-object-seed43 (norm=0.1) = 12%，低于同 seed 的 argmin=17%。seed43 是 obs_only 的最差 seed + argmin 的最好 seed

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-18228 / bjb1-32546 / bjb2-28827 / bjb2-40593，account=root
- 代码根：`/root/acr-vla-conformal-refinement`
- Python：`/root/miniconda3/bin/python`（需 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- CRM checkpoints：`/root/autodl-tmp/checkpoints/crm_v3_norm/{obs_only,perdof,scalar_unc}/crm_best.pt`
- HF cache：`/root/autodl-tmp/.hf_cache`（HF_HUB_OFFLINE=1）
- SmolVLA：`/root/autodl-tmp/models/smolvla_libero/`
- 无 W&B — 所有评估均为离线 JSON 输出
- 空闲 GPU（截至 06:40 UTC）：bjb1-18228 cuda:2,3 / bjb1-32546 cuda:4 / bjb2-28827 cuda:2

### 3. 📊 当前状态
**刚完成**：
1. 论文 Experiments section 审查 → 发现 Table 3 per-task 数据 3/4 列有误（CRITICAL，已提供修正数据）
2. eval-direct-correction-r3 审查：14% > VLA-only 12%，但 +2pp 不显著 → Claim 1 需软化
3. eval-perdof-object-norm03-seed44 = 4% PASS（与 seed42 完全一致）
4. 多 seed variance 系统性分析：obs_only vs Argmin pooled p≈0.075（不显著），obs_only vs VLA-only p<0.01（显著）→ 建议 Director 将 primary contribution 锚定于 mechanism insight 而非 absolute SR

**RUNNING 实验**（16 个）：
- bjb1-32546: eval-argmin-object-seed46/47, eval-perdof-norm01-seed45, eval-perdof-norm03-seed45-r2, eval-obs-only-norm02-seed47
- bjb1-18228: eval-perdof-norm01-seed44, eval-perdof-norm03-seed44(已完成待收), eval-obs-only-norm01-seed45, eval-obs-only-norm02-seed46(已完成待收)
- bjb2-28827: eval-perdof-norm02-seed44/seed45, eval-scalar-seed45, eval-obs-only-default-seed45, eval-obs-only-norm03-seed45-r2
- bjb2-40593: eval-perdof-default-seed44

**等待中**：Director 对 claim 强度调整建议的决策回复

### 4. 📋 待办（条件触发式）
- eval-obs-only-object-norm02-seed47 完成 → 更新 6-seed 统计，按决策树判断 Claim 1 最终措辞
- 论文 Table 3 修正 worker 提交 → 审查新数据是否与 JSON 原始文件一致
- Direct correction 结果被写入论文 → 审查措辞是否如实报告 14%（非 ≤12%），是否避免 "CRM 独立无效" 过强声称
- 任何新 paper section 提交审查 → 先检查 Table 1/Table 3 自洽性（之前已证明 worker 会抄错数据）
- eval-vla-mean-object-seed45 registry status 仍为 ANALYZING → 提醒 Agent 补刷 status 为 DONE

### 5. 🎯 战略上下文
**核心结论链**：
- obs_only vs VLA-only: +6pp, p<0.01 ✓（稳）
- obs_only vs Argmin: +3.5pp, p≈0.075（不显著，seed43 反向）
- obs_only vs perdof magnitude robustness: 跨所有 seed 一致（最强证据）
- perdof progressive collapse: ε=0.3 → 4%, default → 0%（完美复现）
- Direct correction: 14%（边际正向，不显著）

**下一个"我"最容易判断错的事**：
1. 不要信 registry 中 eval-object-v8-full = 13% 是当前论文的 obs_only ε=0.1 数据——那是旧 CRM。真正的 19% 来自 eval-acr-object-v4-obs-only（只有 tmux log，未注册）
2. 不要因为 5-seed mean = 17% > Argmin 13.5% 就说"显著"——pooled Fisher p=0.075 不过阈值
3. Narrative B 最强点是 mechanism insight (robustness vs collapse)，不是绝对 SR improvement。如果 Agent 试图用 "+10pp" (seed42-only) 做 headline claim，必须打回
4. Paper worker 有从 report/registry 等二手源抄录数据的毛病（Table 3 事件），审查任何数据表时必须与 JSON 原始文件交叉验证


---
