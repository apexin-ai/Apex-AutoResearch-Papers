# agent / loop_29.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_29.md`
- **Structured JSON:** [`a5a4e8c4f329967b812b.json`](../../sessions/a5/a5a4e8c4f329967b812b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 29
reason: idle_timeout
updated: '2026-05-28T16:09:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: 仅 bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5, cqa1-32758:cuda:0-5（共 22 卡）。其他服务器/卡号禁止使用
- **westd 服务器数据有毒**: D175 确认 westd-49937 LIBERO assets 版本与其他服务器不同（HF 下载 vs 预装），westd 产出的 eval 数据**不可用于论文 Table**
- **Pi05 unified checkpoint 必须传 `--obs_dim 2048 --unified_obs_dim 2088`**: checkpoint 路径 `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt`，缺参数会 shape mismatch 报错（已踩过两次）
- **CoRL DDL 2026-05-28 20:00 BJ**: D184 锁定，20:00 后数据冻结。论文 title 已锁: "Knowing When Not to Correct: Adaptive Test-Time Refinement for Frozen VLAs"
- **perdof 消融不可与 Table 1 对比**: D176 确认 perdof 训练条件与主表不同，不能放同表

### 2. 🖥️ 基础设施快照
- **服务器 × 4**: bjb1-18228 (4卡), bjb1-32546 (6卡), bjb2-28827 (6卡), cqa1-32758 (6卡)
- **工作目录**: `/root/acr-vla-conformal-refinement`（所有服务器统一路径）
- **账号**: root
- **SmolVLA CRM checkpoint**: `/root/autodl-tmp/checkpoints/crm_smolvla_unified_4suite/crm_best.pt`（obs_dim=960）
- **Pi05 CRM checkpoint**: `/root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt`（obs_dim=2048, unified_obs_dim=2088）
- **活跃进程**: 无。0 RUNNING 实验, 0 active crons, 0 running workers
- **GPU 状态**: 全部 22 卡空闲（report.md 确认）

### 3. 📊 当前状态
- **论文就绪待提交**: 编译通过, 8页正文 + 6页(refs 2 + appendix 4), 零 critical warning
- **Registry**: 1229 实验总计 — 768 success / 96 negative / 130 failed。**0 RUNNING / 0 PREPARING / 0 QUEUED / 0 PENDING / 0 ALLOCATED**。所有实验管线已清空
- **Table 1 (SmolVLA K-matched)**: 4/4 suites 完整, CRM always-on 4/4 有害 (Long -14.8pp 最强), Adaptive 全面恢复
- **Table 3 (Pi05)**: 4/4 suites degradation-only 完整 (Long 94.0→77.0, Δ=-17.0pp)
- **等待中**: 用户确认 title + CoRL 提交决定（contingency: 18:00 BJ 默认提交）。无 Worker/Cron 回调待处理
- **report.md 列 eval-supp-obj-adapt-tau025-s43 为运行中**, 但 registry 无 RUNNING 实验——可能已完成但 report 未刷新

### 4. 📋 待办（条件触发式）
- 用户/Director 确认提交 → 执行 CoRL 提交流程（submit_paper_to_review 或用户手动提交）
- 18:00 BJ 无用户响应 → 按 D184 contingency 默认提交
- 若 DDL 前还有时间 + GPU 空闲 → 可继续跑 supplementary seeds（Pi05 CRM always-on long s43/s44, tau-sweep 补充点），但**不影响主表**
- 任何 backfill cron 回调到达 → update_registry + 刷新 report.md（仅 supplementary/camera-ready 用途）
- Reviewer claim 强度审查完成 → 如有修改建议需在 DDL 前处理

### 5. 🎯 战略上下文
- **核心 narrative**: CRM correction 是双刃剑——无条件应用 4/4 suites 有害; Adaptive gating 正确决定"何时不修正"是核心贡献。Analysis-first paper, method 是分析洞察的产物
- **3 个 Claims**: MC1=CRM always-on 4/4 有害+Adaptive 恢复, MC2=trigger rate↔Δ 单调正相关, MC3=跨 VLA 泛化 (SmolVLA 0.4B + Pi05 3.6B)
- **决策链关键节点**: D170(K-matched重构) → D177(Table 1 3列) → D178(Long最强证据) → D179(Title锁定) → D184(提交确认)
- **易错点**: ① 不要混淆旧 K=10 数据和新 K=2 K-matched 数据——Table 1 只用 D170 之后的数据 ② Pi05 Table 只有 degradation-only 两列（VLA-only + CRM always-on），没有 Adaptive 列 ③ Long suite 是论文最有力证据 (-14.8pp)，任何叙事调整不能弱化这个数据点 ④ OpenVLA-OFT 已放弃(D124)，不要尝试恢复


---
