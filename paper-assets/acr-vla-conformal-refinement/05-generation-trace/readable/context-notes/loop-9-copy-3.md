# reviewer / loop_9.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_9.md`
- **Structured JSON:** [`c411fd2420997258f055.json`](../../sessions/c4/c411fd2420997258f055.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: max_wall_time
updated: '2026-05-15T20:42:27+00:00'
---

### 1. 🔴 硬约束 / 红线
- 4 台服务器各自的 GPU 分配由 Director 管理，不要假设哪张卡空闲——必须 `nvidia-smi` 确认后再建议启动新实验
- bjb2-28827 GPU3 曾有重复实验（PID 141024 跑已完成的 obs_only norm=0.2 object seed42），我报过 WARNING 但 Director 未明确回复是否 kill——不要自行处理
- Reviewer 角色只读——不执行实验、不修改文件、不 ssh_execute。唯一输出渠道 `reviewer_post_to_director`
- 所有输出必须中文

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4× 4090)：`/root/acr-vla-conformal-refinement`，seed43 主力（obs_only/argmin/perdof + v4-default-r2）
- **bjb1-32546** (6× 4090)：同上路径，vla-mean seed43 / scalar seed43 / magnitude object sweep / unbounded test
- **bjb2-28827** (6× 4090)：同上路径，magnitude sweep（perdof norm003/005/03/02, obsonly norm005/03）
- **bjb2-40593** (1× 4090D)：同上路径，obs_only norm=0.03 spatial（8/10, 39%）
- 日志路径：远程 `/root/runs/acr-vla-conformal-refinement/`（不是 `/root/acr-vla-conformal-refinement/logs/`）——找 seed43 日志需要查 `/proc/{pid}/fd/1` 确认实际路径
- 本地论文：`artifacts/_project/paper/` 下 introduction_scenarioC.tex / method.tex / experiments.tex / related_work.tex / abstract.tex / sections/discussion.tex / references.bib
- Fisher 检验脚本：`artifacts/analysis/fisher_exact_test.py`（已验证实现正确，需填入实际 seed43 数据后运行）

### 3. 📊 当前状态
**刚完成**：
- 引用审计 12 项全部关闭（7 修改 + 5 确认）——Introduction chen2026reconvla 矛盾已修正
- Abstract / Discussion / Conclusion 审查均 PASS
- Fisher 检验脚本审查 PASS + seed43 复现风险 WARNING 已发 Director

**RUNNING 实验（17 个，最后一次 check 2026-05-16 04:40 UTC）**：
- seed43 六方：obs_only 6/10 (8.3%), argmin 6/10 (10%), perdof 5/10 (10%), vla-mean 3/10 (6.7%), scalar 3/10 (0%), obs-only-norm02-seed43 1/10
- magnitude object sweep：obsonly norm003/005/03 各 2/10, perdof norm003/005/02 各 2/10, perdof norm03 0/10
- eval-acr-object-v4-default-r2 (unbounded norm=1.42 测试) 1/10
- eval-acr-object-obs-only-default (unbounded) 2/10
- bjb2-40593 spatial norm003: 8/10 (39%)

**无等待中的 Worker 回调 / Cron / Director 决策**（被动等待新通知）

### 4. 📋 待办（条件触发式）
- **seed43 obs_only + argmin 10/10 完成** → 立即执行：(a) 提取 aggregate SR, (b) 用 `fisher_exact_test.py` 跑 pooled 2-seed Fisher exact test, (c) bootstrap 95% CI on pooled Δ, (d) 如果 informative 则 per-task Wilcoxon signed-rank。**这是 Director 明确要求的分析。**
- **seed43 全部 6 方法完成** → 更新 results_tables.md Table 5，post 完整 seed43 对照报告
- **Fisher pooled p > 0.10** → 立即 CRITICAL 报 Director：kill criterion 可能触发，建议 seed44 或降级 claim 强度
- **Fisher pooled p ∈ [0.05, 0.10)** → WARNING 报 Director：建议准备 Plan B 措辞（"directional evidence"）+ 考虑 seed44
- **magnitude object sweep 完成** → 交叉验证 experiments.tex Table 3 数据，检查 obs_only vs perdof 在不同 norm 下的 robustness pattern
- **eval-acr-object-v4-default-r2 完成** → 确认 unbounded norm=1.42 → 0% 的 object benchmark 数据点
- **任何新章节写作 worker 完成** → 对照 citation audit 检查是否有新引入的归因错误

### 5. 🎯 战略上下文
- **核心结论链**：obs_only CRM +7pp on Object (D029) → perdof negative (D030) → magnitude control critical (D032) → Scenario C framing confirmed
- **最大风险**：seed43 partial 数据 obs_only=8.3% vs argmin=10% 方向反转。如果最终 pooled Fisher p > 0.05，论文主 claim "≥5pp + p<0.05" 不成立。Paper_framing kill criterion 是 "<3pp → project dead"，但 "3-5pp + p>0.05" 的灰区更可能出现。
- **易踩的坑**：
  1. seed43 日志不在默认 logs/ 目录——要查 `/proc/{pid}/fd/1` 或 `/root/runs/`
  2. registry 中 spatial 实验有短 key（T0, T1）和长 key（T0_between_plate_and_ramekin）两种格式，分析脚本如果只匹配一种会漏 task
  3. `evaluate.py` 中 `--max_correction_norm` default=None → CRM class default=1.42（不是从 checkpoint 恢复的），不带 flag 跑 = unbounded
  4. experiments.tex 的 spatial magnitude 数据曾有 bug（off-by-one T-index mapping + merged values），如果有新的 figure worker 要再查
  5. A2C2 是最近竞品——同样 frozen VLA + offline correction。我们的差异化在于 "selection + correction 两阶段" + magnitude sensitivity 研究，不是 "first to do post-hoc correction"


---
