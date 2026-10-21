# director / loop_13.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_13.md`
- **Structured JSON:** [`f5dd55967a9ab1ef139a.json`](../../sessions/f5/f5dd55967a9ab1ef139a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_messages
updated: '2026-05-27T12:14:22+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-19183 的 cuda:0 和 cuda:1（已通知 Manager 回收但未确认，卡还挂项目名下）
- 论文已提交就绪，DDL 5/29，**禁止对论文做任何非用户要求的改动**——Abstract 微调已是最后一次
- 项目处于审稿阶段，review_chat_id: `oc_554a5023cde4d603635cf97e6ab8151a`
- 107 个 success 实验已全部完成，Reviewer 已确认无值得跑的新实验——不要启动新实验线

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183 (connect.westd.seetacloud.com)，工作目录 /root/vla-ssd
- 最新 PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/submission_package/main.pdf`（5/27 06:54 编译）
- 提交包目录：`artifacts/submission_package/`
- 活跃进程：无。Agent/Reviewer/Worker 全部空闲，0 个实验在跑
- GPU：2 张分配（cuda:0 + cuda:1），利用率 0%，已催 Manager 回收 3 次未确认

### 3. 📊 当前状态
- 刚完成：Abstract 微调（加入 NLP controls 证据点），Discussion prescriptive 改动因页面溢出放弃
- 刚处理：用户周雪阳要求发 PDF，已上传最新版本
- 等待中：(1) 用户确认谁来提交 OpenReview + 什么时候提交（已催两次）；(2) Manager 确认 GPU 回收（已催三次）
- Registry：156 个实验，145 完成（109 success），11 个低优先级待处理（不影响论文）
- Reviewer 刚批准 RESET_BOTH，本 handoff 后 Director 也会重置

### 4. 📋 待办
- 用户回复提交计划 → 配合准备提交材料 / 发给 co-author
- 用户持续不回复且距 DDL < 24h → 再发紧急催促，建议 co-author 代提交
- Manager 回复 GPU 回收 → 确认完成
- Manager 持续不回复 → 升级处理
- 如果用户要求对论文做最后修改 → 派 Paper Agent 执行，改完重编译验证字体

### 5. 🎯 战略上下文
- 中稿率估计 53-58%，瓶颈是 venue fit（analysis paper at robotics venue），非实验可解决
- Reviewer 逐项评估过四个进攻方向（未挖掘 insight / visualization / seed 稳定性 / robustness），均无实质性 ROI
- 写作层面也评估过（Intro hook / contribution / Discussion / Abstract），仅 Abstract 微调有净收益且已执行
- 易错点：不要因为中稿率不高就启动新实验线——107 个实验的统计基础已足够坚实（15 seeds, bootstrap CI, permutation test, 3 NLP controls），问题在 paper type 不在证据量
- 关键决策链：从 method paper 路线转为 systematic analysis 路线（有完整的 Method→Analysis 切换论证）
- 用户周雪阳刚要过 PDF 说明在关注，但提交操作仍未确认——这是唯一阻塞项


---
