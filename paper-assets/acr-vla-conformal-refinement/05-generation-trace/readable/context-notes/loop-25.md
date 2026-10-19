# director / loop_25.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_25.md`
- **Structured JSON:** [`aaa52d14ded24317225a.json`](../../sessions/aa/aaa52d14ded24317225a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 25
reason: max_messages
updated: '2026-05-28T06:05:24+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-18228(4卡), bjb1-32546(6卡), bjb2-28827(6卡), cqa1-32758(6卡)，共 22 张。严禁用白名单外 GPU
- westd-49937 数据系统性偏低 4-5pp（D175），该服务器数据不可用于论文
- Table 2 Pi05 全部为 single-seed s42，不得混用 3-seed mean 或其他 seed
- Table 1 SmolVLA 用 matched-seed 统计（D172），CRM checkpoint 是 3suite（不含 Long）
- Long suite 是 CRM OOD（CRM 只训练了 Object/Spatial/Goal），论文必须标注
- DDL: CoRL 2026，2026-05-28 20:00 北京时间（今天）

### 2. 🖥️ 基础设施快照
- 4 台服务器全部 AutoDL，代码路径 `/root/acr-vla-conformal-refinement`
- bjb1-18228: 4×GPU，跑 Pi05 precompute 任务
- bjb1-32546: 6×GPU，跑 Pi05 CRM always-on seeds + K-sweep + random selection baseline
- bjb2-28827: 6×GPU，跑 τ-sweep + supp seeds + Long VLA-only
- cqa1-32758: 6×GPU，跑 τ=0.15 Object 3-seed + supp seeds；cuda:5 保留给 pi05-crm-always-on-long-s42（已完成 SR=77.0%）
- CRM checkpoint: `crm_smolvla_3suite_v1`（3 suites, 30 tasks, ~88K samples）
- 4suite checkpoint 存在（`crm_unified_4suite`）但主实验未使用

### 3. 📊 当前状态
**刚完成**：
- Pi05 Long CRM always-on 结果确认（77.0%），Table 2 四行完整
- Pi05 Long VLA-only baseline 修正为 s42 matched（94.0%, Δ=-17.0pp）
- Paper Agent 完成全文 -18.0→-17.0 级联修正 + 跨服务器配对注释
- 22 张 GPU 全部在跑，Agent 按 P0→P3 优先级部署 184 个 pending 实验中的首批

**运行中实验**（~29 个，含首批 backfill 的 10 个新部署）：
- Pi05 CRM always-on bonus seeds (bjb1-32546)
- τ=0.15 Object 3-seed sweep (cqa1)
- τ=0.45 Spatial, supp seeds (bjb2)
- K-sweep K=20 obs-only, random selection baseline (bjb1-32546)
- 完成后自动 backfill 下一批

**等待中**：
- 用户确认 title（D179: "Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models"）+ CoRL 提交决定——**已催 3 次，用户尚未明确回复**
- Paper Agent 跨服务器注释 patch 已完成
- Reviewer 刚 reset，需要新 session

### 4. 📋 待办
- 用户回复确认 title + CoRL 提交 → 立即进入最终提交流程（submit_paper_to_review 或直接提交）
- 用户说"提交" → 检查论文最终版编译 + 附录 + supplementary 完整性 → 提交
- 实验 cron 回调（backfill 实验完成）→ Agent 自动部署下一批，不需要逐个审批
- 如果 backfill 实验产出论文可用数据 → 评估是否值得 last-minute 加入 supplementary

### 5. 🎯 战略上下文
- **核心结论**：CRM always-on 在 4/4 suites 有害（SmolVLA + Pi05 跨模型一致），Adaptive conformal gating 恢复性能。Long 退化最严重（SmolVLA -14.8pp, Pi05 -17.0pp）因为 CRM 对 Long 是 OOD
- **论文 narrative**（D170/D177/D178）："CRM 修正是双刃剑，gating 正确决定何时不干预"
- **MC1**: 4/4 suites 跨模型有害；**MC2**: trigger_rate ↔ Δ 单调正相关；**MC3**: SmolVLA 0.4B + Pi05 3.6B 泛化
- **Table 1**: K-matched 3 列（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），SmolVLA 4 suites × 3 seeds
- **Table 2**: Pi05 degradation-only 2 列（VLA-only / CRM always-on），4 suites，single-seed s42
- **易错点**：Pi05 数据全是 single-seed，论文中标了 "preliminary single-seed" caveat；分析报告中 Goal baseline 有幽灵数字 97.8%（不对应任何实验），不要引用分析报告的 auto-populated baseline
- **决策链关键节点**：D172(matched-seed) → D175(westd偏差) → D177(K-matched Table 1) → D178(4/4 harmful) → D181(Table 2 degradation-only) → D182(Pi05 Long -17.0pp)


---
