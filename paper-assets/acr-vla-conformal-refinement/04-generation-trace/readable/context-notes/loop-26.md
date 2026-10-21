# director / loop_26.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_26.md`
- **Structured JSON:** [`dae6e0b1bba989f86c98.json`](../../sessions/da/dae6e0b1bba989f86c98.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 26
reason: max_messages
updated: '2026-05-28T16:07:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 分配白名单以 `get_project_status` 的 gpu_ids 为准，当前 3/4 服务器不可达，仅 bjb1-18228 有 1× RTX 4090
- Figure 2 (fig1_pipeline.pdf) 中 d² 应为 d₂（下标 2 = K=2 pairwise distance，非平方）——Reviewer WARNING 未修复，提交前/camera-ready 必须改
- CoRL 2026 DDL 2026-05-28 20:00 BJ 已过，后续工作为 camera-ready 或等审稿结果
- Paper 真源在本地 `projects/acr-vla-conformal-refinement/docs/paper/`，训练代码在远程 `/root/acr-vla-conformal-refinement`

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (connect.bjb1.seetacloud.com): 可达，1× RTX 4090，工作目录 `/root/acr-vla-conformal-refinement`
- **bjb1-32546 / bjb2-28827 / cqa1-32758**: 全部不可达（AutoDL 实例可能关机或端口变更），已通知用户检查控制台，未收到回复
- 论文目录: `/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/`
- 活跃进程: 无（0 RUNNING 实验，Agent 已 idle 16h）

### 3. 📊 当前状态
- **论文已编译通过**：8 页正文 + refs + appendix，零 critical warning，所有 5 个 figure 就位
- **Table 1 K-matched 重构完成**：VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive 三列，4/4 suites harmful 叙事
- **Table 3 Pi05 完成**：4/4 suites degradation-only
- **Figure 2 PaperBanana 重画完成**但有 d²→d₂ 符号未修（severity: warning）
- **Registry**: 0 RUNNING，177 排队实验（supplementary tau-sweep/bonus seeds），1415 已完成
- **等待中**: 用户回复服务器状态；无活跃 Worker/Cron 回调

### 4. 📋 待办
- 用户确认服务器恢复 → 更新 SSH 配置 → 派 Agent 在恢复的 GPU 上跑 supplementary 实验（tau-sweep、bonus seeds）
- 用户确认已提交 CoRL → 切换到等审稿模式，准备 rebuttal 素材
- 如未提交 → 确认是否需要晚提交/换 venue，修复 d₂ 符号后再提交
- camera-ready 阶段 → 修复 Figure 2 d²→d₂ + 补充 supplementary 实验数据

### 5. 🎯 战略上下文
- **核心 narrative**: CRM always-on 在 4/4 suites 有害（SmolVLA -1.3~-14.8pp, Pi05 全降），Adaptive gating 全面恢复 → "Knowing When Not to Correct"
- **三条 claim**: MC1=CRM always-on 有害+Adaptive 恢复, MC2=Trigger rate↔Δ 单调正相关, MC3=Cross-VLA 泛化 (SmolVLA 0.4B + π0.5 3.6B)
- **Title 已锁定** (D184): "Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models"
- **易错点**: 3 台服务器不可达不代表数据丢失——实验结果已在 registry 中，仅影响新实验派发；不要因服务器问题 panic 改论文内容
- **决策链关键节点**: D177 Table 1 K-matched 重构 → D178 Long -14.8pp 最强证据 → D179 Title 锁定 → D183 移除 OpenVLA Contribution 4 → D184 提交确认


---
