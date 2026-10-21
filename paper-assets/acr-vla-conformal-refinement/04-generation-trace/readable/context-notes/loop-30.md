# agent / loop_30.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_30.md`
- **Structured JSON:** [`acb6558b56d5884eb63e.json`](../../sessions/ac/acb6558b56d5884eb63e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 30
reason: idle_timeout
updated: '2026-05-29T08:21:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- CoRL 2026 DDL **2026-05-28 20:00 北京时间**（已过/当天）
- GPU 白名单 22 张：bjb1-18228(4), bjb1-32546(6), bjb2-28827(6), cqa1-32758(6)
- westd-49937 数据系统性偏低 4-5pp（LIBERO assets 版本差异），**不可混入 Table 1/2 主表**
- Table 1 已锁定 K-matched 3 列结构（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），不可擅自改列结构
- Pi05 Object CRM 数据不入 Table 2 主表，放 Supplement（D171）

### 2. 🖥️ 基础设施快照
- **cqa1-32758**: `/root/acr-vla-conformal-refinement`, conda base `/root/miniconda3` — **连接失败**（端口不可达）
- **bjb2-28827**: 同结构 — **连接失败**
- **bjb1-32546**: 同结构 — **连接失败**
- **bjb1-18228**: 配置 4 卡但实测仅 1 卡可用 — 连接状态未确认
- CRM checkpoint: `cqa1:/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`
- 所有服务器可能因 AutoDL 实例重启导致端口变更，需用户去控制台查新端口

### 3. 📊 当前状态
**刚做完**: Session #30 初始化（read_registry + reconcile_crons + report.md + ROADMAP），向 Director 汇报了状态。

**实际状态与 handoff 不一致**: Handoff 说 7 个 RUNNING，但 registry 显示 **0 RUNNING**。report.md 明确记录"2026-05-28 用户指令全面停机"，全部实验已 kill/cancel。0 个活跃 Worker，0 个活跃 Cron。

**论文状态**: 就绪（编译通过，8 页正文 + 6 页附录，零 critical warning）。Table 1 K-matched 重构 + 叙事 4/4 升级均完成。ROADMAP 记录等待用户确认 title + CoRL 提交决定。

### 4. 📋 待办（条件触发式）
- Director 回复提交指令 → 执行最终提交流程（submit_paper_to_review 或按 Director 指示操作）
- 用户更新服务器端口 → 更新 SSH config → 恢复服务器连接 → 可恢复补充实验
- Director 要求提交前检查 → 派 Worker 做最终 claim 强度审查 / 编译验证
- 任何新实验需求 → 先确认服务器可达性，再提交

### 5. 🎯 战略上下文
- **核心叙事（D170/D178）**: "CRM always-on 在 4/4 suites 有害（Object -4.7pp, Goal -3.7pp, Spatial -1.3pp, Long -14.8pp），adaptive gating 全面恢复"——这是论文最强证据
- **Claim 策略**: MC1=4/4 harmful + recovery, MC2=trigger rate↔Δ 正相关（tau-sweep）, MC3=cross-VLA 泛化（SmolVLA 0.4B + π0.5 3.6B）
- **易错点**: 项目处于"全面停机 + 论文就绪"状态，不要假设任何实验还在跑。服务器全部不可达，不要尝试 SSH 操作除非用户更新了端口。metrics 格式混用小数/百分比（0.61 vs 58.5），比较时必须统一
- **D184**: 用户已授权按核心 claim 定 title，contingency 18:00 BJ 默认提交
- 成功率：768 success / 96 negative / 130 failed / 共 1229 实验


---
