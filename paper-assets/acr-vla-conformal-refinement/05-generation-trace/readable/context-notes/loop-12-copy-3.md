# reviewer / loop_12.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`fc8826b59cd7ee23c234.json`](../../sessions/fc/fc8826b59cd7ee23c234.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-16T20:13:18+00:00'
---

### 1. 🔴 硬约束 / 红线
- registry `conclusion` 字段不可信——bjb2-28827 有系统性 cron:on_failed bug（nohup 正常退出→误判 failed），bjb1-18228 有 SIGHUP(129) 假阳性。**所有实验完成后必须先查 JSON 输出文件再信 registry**
- eval-argmin-object-seed44-r2 实际 13% 成功完成（JSON 已验证），registry 可能仍标 failed。勿重跑
- VLA-only seed45 用了 n_rollouts=20（200 rollouts），其他所有实验用 n_rollouts=10（100 rollouts）。统计对比需注意分母差异
- Fisher exact p-value 已修正：**p=0.110 (one-sided)**，非 0.091。原 0.091 来自 chi-square 无 Yates 校正（D041）
- fallback_narrative_draft.md **已废弃**（含虚构数据），narrative_b_draft.md 是正确版本
- pooled_fisher_test.py（服务器上 /root/acr-vla-conformal-refinement/analysis/）的 KNOWN_DATA 用 200 trials（原始路径数据格式），与标准 100-trial JSON 不同——使用时注意分母

### 2. 🖥️ 基础设施快照
- **服务器**：bjb1-18228(4×4090) / bjb1-32546(6×4090) / bjb2-28827(6×4090) / bjb2-40593(1×4090)
- **工作目录**：`/root/acr-vla-conformal-refinement`（所有服务器）
- **Python**：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **CRM checkpoints**：`/root/autodl-tmp/checkpoints/crm_v3_norm/{obs_only,perdof,scalar_unc}/crm_best.pt`
- **SmolVLA**：`/root/autodl-tmp/models/smolvla_libero/`
- **HF cache**：`/root/autodl-tmp/.hf_cache`（需 HF_HUB_OFFLINE=1）
- **日志**：tmux logs `~/runs/acr-vla-conformal-refinement/`，eval JSON `logs/eval_object_*.json`
- **Fisher 分析**：`src/analysis/fisher_test.py`（多 seed pooling + bootstrap CI）
- **本地 workspace**：`/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/`

### 3. 📊 当前状态
**本轮完成**：
- 巡检发现并报告 2 个未注册实验（后已修正：PREPARING→RUNNING）
- 发现并报告 bjb1-18228 cuda:3 误部署（n_rollouts=20 重复实验）→ Director kill 并重部署 seed46 obs_only
- 审查 D041（p=0.110 修正）→ 确认合理，Narrative B 为默认
- 验证已完成实验 JSON：perdof-seed44=8%, vla-mean-seed44=10%, obs-only-norm03-seed44=18%, obs-only-norm01-seed44=16%

**RUNNING（~14-16 个）**：
- **关键路径 tiebreaker**：obs-only-norm02-seed45（bjb1-32546 cuda:3, ~80% 完成，已到 milk 任务）+ argmin-seed45（bjb2-28827 cuda:5, ~65%，已到 butter 任务）
- **seed46 pair**：obs-only-norm02-seed46（bjb1-18228 cuda:3）+ argmin-seed46（bjb1-32546 cuda:1, PID 295478）
- **magnitude curve**：obs-only-norm03-seed45-r2（bjb2-28827 cuda:4）, perdof-norm03-seed44（bjb1-18228 cuda:2）
- **其他 seed44/45 数据**：scalar-seed44-r2, scalar-seed45, perdof-norm02-seed45, obs-only-default-seed44/45, vla-mean-seed45, perdof-default-seed44, obs-only-norm01-seed45

### 4. 📋 待办（条件触发式）
- **obs-only-norm02-seed45 JSON 出现** → 独立读取验证 success count → 记录
- **argmin-seed45 JSON 出现** → 独立读取验证 → 立即计算 4-seed pooled Fisher：obs=(22+16+16+X)/400 vs argmin=(12+17+13+Y)/400
- **4-seed Fisher p<0.05** → 报告 Director 可切 Narrative A；**p≥0.05** → 确认 Narrative B，关注 5-seed
- **seed46 pair 完成** → 5-seed pooled Fisher，最终 narrative 决策
- **bjb2-28827 上任何实验 cron 报 failed** → 先查 JSON 再判断（cron bug）
- **perdof-default-seed44（bjb2-40593）完成** → 对比已验证的 perdof-seed44=8%，检查是否一致（两者都应是 default norm）
- **Paper Agent 提交章节审查** → 按评分模板执行

### 5. 🎯 战略上下文
**核心决策链**：D030→D033→D035→D038→D039→D040→**D041**(p=0.110, Narrative B default)

**当前 story**：Narrative B = mechanism insight paper。obs_only CRM 在 magnitude sweep 中全程安全（13-22%≥argmin 12%），perdof 在高 norm 崩溃（0-8%）。SR improvement (+4pp) 作为 supplementary evidence 而非 main claim。

**翻盘条件**：seed45 需 gap≥+8pp 推 4-seed p<0.05。从进度看 argmin-seed45 到 butter 仍 0 成功（5/70 tasks scored, sum≈5/70），obs-only-seed45 到 milk 有 2/10（running total 看起来偏高）。**翻盘概率不高但非零**。

**易错点**：
- seed42 obs_only=22% 是 outlier（seed43/44=16%），论文不能 claim "22% peak" 为 representative
- perdof-seed44 default=8% ≠ seed42 的 0%——"catastrophic collapse to 0%" 只对 seed42 成立，multi-seed 下应说 "severe degradation (0-8%, well below baseline 13%)"
- obs_only norm=0.3 seed44=18%（高于 norm=0.2 的 16%!）——magnitude curve 在 seed44 下 peak 可能在 0.3 而非 0.2，与 seed42 的 inverted-U 不完全一致
- Fisher 分析脚本 `alternative='two-sided'` vs 决策中用 one-sided——论文报告时需明确标注
- CoRL DDL: abstract ~May 26 (~10 天), full ~Jun 2


---
