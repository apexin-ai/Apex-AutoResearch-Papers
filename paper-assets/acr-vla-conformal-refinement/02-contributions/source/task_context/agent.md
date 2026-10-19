---
loop: 30
reason: idle_timeout
updated: '2026-05-29T13:30:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 22 张，分布在 bjb1-18228, bjb1-32546, bjb2-28827, cqa1-32758
- westd-49937 数据系统性偏低 4-5pp（D174/D175），该服务器结果不可用于论文
- Table 1 只用 K-matched 3 列（VLA-only K=1 / K=2 CRM always-on / K=2 Adaptive），禁止混 K 对比
- perdof 数据因训练条件差异不可用于论文对比（D176）
- crm-always-on-long-s45 是 bonus seed，不进入主 Table 1 统计（主统计用 s42/s43/s44）
- Title 已锁定(D179): "Knowing When Not to Correct: Adaptive Test-Time Correction via Conformal Prediction for Vision-Language-Action Models"
- CoRL 2026 DDL **2026-05-28 20:00 北京时间**（已过或即将到达）

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 可达，1×RTX 4090 空闲，工作目录 /root/autodl-tmp/acr-vla-conformal-refinement
- **bjb1-32546**: ❌ 连接失败（port 32546 不可达，AutoDL 实例可能已关机/端口变更）
- **bjb2-28827**: ❌ 连接失败（port 28827 不可达）
- **cqa1-32758**: ❌ 连接失败（port 32758 不可达）
- CRM checkpoint: /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt（各服务器同路径）
- 活跃进程：无（0 RUNNING 实验，0 活跃 Worker，0 活跃 Cron）

### 3. 📊 当前状态
项目完全空闲。所有实验已 kill/cancel（2026-05-28 用户指令全面停机）。论文就绪：编译通过，8+6 页，零 critical warning。Table 1 K-matched 重构 ✅，Table 3 Pi05 ✅，叙事一致性 ✅。

Registry: 0 RUNNING / 0 PREPARING。总计 1230 实验（成功 768 / 负向 97 / 失败 130）。

已向 Director 发送 Session #30 启动汇报，等待 Director/用户确认提交决定。无待处理 Worker 回调或 Cron。

### 4. 📋 待办
- Director 回复提交决定 → 执行论文提交流程（submit_paper_to_review）
- 用户要求重新连接服务器（端口变更后）→ 更新 SSH config → 重新探测环境
- 如需补充实验（camera-ready 阶段）→ 先确认服务器可达性 → 恢复 cron 监控 → 重新提交
- DDL 已过且未提交 → 等 Director 指示下一步（转投其他会议 / camera-ready 准备）

### 5. 🎯 战略上下文
- **核心结论**: CRM always-on 在 4/4 suites 有害（Long 最严重 -14.8pp），Adaptive conformal gating 全面恢复。这是论文最强 claim（MC1）
- **数据已锁定**: SmolVLA 4 suites × 3 seeds 齐全。Long: VLA-only 58.0±1.5, CRM-always-on 43.2±2.3, Adaptive 57.7±1.5
- **Table 2 (Pi05)**: 4/4 suites degradation-only（VLA-only + CRM-always-on 两列），Long 94.0→77.0 Δ=-17.0pp
- **Claim 策略**: MC1=4/4 harmful + recovery, MC2=trigger rate↔Δ 单调正相关, MC3=cross-VLA 泛化
- **易错点**: 3/4 服务器不可达，如需重新操作必须先让用户去 AutoDL 控制台查新端口。不要反复重试连接
