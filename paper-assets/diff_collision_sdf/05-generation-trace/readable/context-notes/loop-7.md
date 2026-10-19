# director / loop_7.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`b61509e0db2436c8ac00.json`](../../sessions/b6/b61509e0db2436c8ac00.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-27T09:18:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-35807 cuda:0-3，westd-45947 cuda:0-1。严禁在白名单外启动实验
- λ=0.1 eval 必须用 dfCAR + EE displacement 验证，不能用 raw CAR（违反 Claim 1 metric contamination 发现）
- 30K eval 冻结判定必须用修复后脚本（M044/M045 教训：旧 displacement 字段恒 <0.001m 是 bug）
- D035 Scenario B 标记 provisional（D036），30K s0/s1 eval 是 definitive 裁判，不要在 30K 前锁定叙事
- CoRL 2026 DDL: 5/28 12:00 UTC（北京时间 20:00）

### 2. 🖥️ 基础设施快照
- 服务器 1: westd-35807 (connect.westd.seetacloud.com)，4×GPU，`/root/colliforce-vla`
- 服务器 2: westd-45947 (connect.westd.seetacloud.com)，2×GPU，`/root/colliforce-vla`
- 镜像: aml-train（conda 环境，`/root/miniconda3/bin/python`）
- 活跃训练:
  - westd-35807 cuda:1: λ=0.1 s0 30K（~17:00 UTC 5/27 完成）
  - westd-35807 cuda:2: λ=0.1 s1 30K（~17:45 UTC 5/27 完成）
  - westd-35807 cuda:3: spatial_bowl LoRA control s0（~06:10 UTC 5/28）
  - westd-45947 cuda:0: LoRA baseline s2 resume（~20:15 UTC 5/27）
  - westd-45947 cuda:1: λ=0.1 s2（~08:40 UTC 5/28）
- westd-35807 cuda:0: 可能空闲（spatial_bowl SDF eval 应已完成 ~06:30 UTC 5/27）
- Agent 正在处理 worker 回调：eval_s0_30k 和 diagnose_train_pi05_a1_obj_s0_l01_high

### 3. 📊 当前状态
- **阶段**: Research + 审稿进行中 + 论文写作并行（CoRL 2026，全 8 章节已完成）
- **核心悬念**: λ=0.1 30K eval → A/B/C 场景判定。D035 判 Scenario B（全域 negative），D036 标 provisional（22K 跳变至 60.5%）
- **RUNNING 实验**:
  - `eval_pi05_a1_30k_s0_l01_high` — λ=0.1 s0 30K eval（最高优先级，Agent 正在处理回调）
  - `train_pi05_lora_baseline_s2_resume` — LoRA baseline s2 恢复训练（从 22K→30K）
  - `train_spatial_bowl_lora_control_s0` — 跨场景 LoRA 对照组
- **PENDING**: reeval_lora_s0_30k_v2（LoRA s0 重评）、eval_pi05_a1_best_s0_l005（best checkpoint eval）
- **等待中**: Agent 正处理两个 worker:done 回调（eval 结果 + 诊断结果），处理完后应启动 s1 eval 并汇报 s0 30K λ=0.1 结果

### 4. 📋 待办（条件触发式）
- λ=0.1 s0 30K eval 结果到位 → 对照 D033 阈值判定（≤57% = B，57-60% = C，≥60% = A-）。如 B：开始 Scenario B narrative patch（`abc_scenario_patches.md`已准备）
- λ=0.1 s1 30K eval 完成（~17:45 UTC）→ 2-seed 均值最终确认场景，patch claim3 + discussion + abstract placeholder
- LoRA baseline s2 训练完成（~20:15 UTC）→ eval → 3v3 统计对比（s0=56.5%, s1=52.5%, s2=?）
- 场景确定 → 通知 Paper Agent patch 论文 → 最终编译
- Figure 1 teaser 仍为 placeholder，DDL 前需设计
- spatial_bowl LoRA ctrl eval（5/28 ~06:10 UTC）→ 跨场景归因对比
- λ=0.1 s2（5/28 ~08:40 UTC）→ 第三 seed 可能赶不上 DDL，2-seed 兜底

### 5. 🎯 战略上下文
- **核心发现**: SDF collision auxiliary loss 在低 λ（0.005/0.01）下完全 redundant（= LoRA-only），CAR 提升 +29pp 全部来自 LoRA fine-tuning 对 collision-free demo 的模仿学习
- **决策链**: D025（SDF redundant 初判）→ D026（provisional，等 λ=0.1）→ D032（低 λ 确认 redundant）→ D033（量化阈值）→ D035（Scenario B 双 seed 20K 确认）→ D036（provisional，22K 异常跳变）
- **论文定位**: Analysis/diagnostic paper——Claim 1: fake safety metric contamination；Claim 2: LoRA fine-tuning 产生真实避碰；Claim 3: SDF geometric supervision 冗余（dose-response 分析）
- **易踩坑**:
  - 不要把 D035 当最终结论——D036 已标 provisional，必须等 30K eval
  - 不要用旧 eval 数据（M044/M045 导致大量历史数据无效，只信 rotation-fixed reeval 数据）
  - Phase 2 λ=0 结论（D029）也是 provisional（D031），不要在论文中过度引用
  - 论文主文已压缩至 7pp，改动需注意不超 8pp 限制


---
