# director / loop_2.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_2.md`
- **Structured JSON:** [`1ad83d432ec206700479.json`](../../sessions/1a/1ad83d432ec206700479.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_messages
updated: '2026-05-13T22:45:43+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 分配由 `get_project_status` 的 gpu_ids 决定，当前两台服务器 bjb2-40593 和 bjb1-18228，不要在未分配的卡上跑实验
- CRM 训练已完成（crm-train-v1 假失败，val_loss=0.009046），registry 需更新为 DONE/success——不要重新训练
- ReconVLA (arXiv:2604.16677) 是 conformal prediction 方法（CQR + argmin selection），不是 "scalar Euclidean distance selection"。论文中所有对 ReconVLA 的描述必须准确，之前 4 个 .tex 文件有错误描述，Paper Agent 已知悉但暂未全部修改
- baseline 已重命名为 SampleConsensus（原来错误地叫 ReconVLA baseline）

### 2. 🖥️ 基础设施快照
- 服务器 1：bjb2-40593 (connect.bjb2.seetacloud.com) [root]，工作目录 /root/acr-vla-conformal-refinement
- 服务器 2：bjb1-18228 (connect.bjb1.seetacloud.com) [root]，工作目录 /root/acr-vla-conformal-refinement
- CRM checkpoint：/root/autodl-tmp/checkpoints/crm/crm_best.pt（bjb2 上）
- 审稿 C 群：oc_416d453a45869a9406db62186b1e3ef7

### 3. 📊 当前状态
**刚完成的关键决策**：
- Reviewer 确认 Agent 对 ReconVLA 的深度分析完全准确，三个差异化论点（per-DOF vs scalar / correction vs selection / online vs offline calibration）全部成立
- Reviewer 确认 crm-train-v1 假失败，CRM 可直接用于 eval pipeline
- Paper Agent 已修正 experiments.tex 中虚假的 augmentation 描述（删除不存在的 camera viewpoint shifts）
- 已向 Agent 发出综合指令（CRM registry 更新 + Reviewer 补充风险点），在 reset 后的新 session 中处理

**Registry 状态**：
- RUNNING: eval-reconvla-spatial-v2, eval-object-v4-full, eval-spatial-v5-full
- PREPARING: precompute-v4-shard0/1/2, precompute-v3-shard0/1/2, eval-reconvla-spatial-v1, eval-spatial-v4-full, precompute-v2-shard1/2
- 已审批待执行：K=3 precompute（CRM 完成后 cuda:1 启动，完成后串 K=20）

### 4. 📋 待办
- Agent reset 完成 → 确认新 session 收到 CRM 假失败更新 + Reviewer 补充风险指令
- eval-object-v4-full 完成 → 若整体 <20% 成功率，需调整 Object benchmark claim 策略（Reviewer 风险点 4b）
- eval-spatial-v5-full 完成 → 对比 CRM correction vs SampleConsensus selection，验证 "better-than-best-sample" claim
- 差异化分析报告完成 → 规划 ReconVLA Medium baseline 实现（CQR + argmin selection，Reviewer 认为必须实现否则审稿人必问）
- K=3/K=20 precompute 完成 → 汇报 claim 强度分析

### 5. 🎯 战略上下文
**核心 story**：ACR-VLA 将 conformal prediction 从决策工具（selection）提升为 correction conditioning signal（per-DOF CP features → learned correction → online adaptation），vs ReconVLA 的（scalar CQR → selection → offline calibration）。

**Reviewer 补充的三个风险**（已发给 Agent 但 reset 前可能未处理）：
1. ReconVLA 有双模块（action + failure detection），ACR-VLA 只有 correction → 论文需定位 scope 为互补关系
2. SmolVLA 在 Object 上 baseline 可能极弱（Task 1 = 0%） → 可能需要只在 Spatial 上报主实验
3. ReconVLA Medium baseline（CQR + argmin）必须实现，否则审稿人必问

**易错点**：
- 不要把 crm-train-v1 当成失败重新训练——已确认是假失败
- Paper Agent 知道 ReconVLA 描述有误但暂未全部修改，等 Agent 差异化分析完成 + Director 下一步指令后再统一改
- 决策链参考 decisions.yaml（14 条记录）


---
