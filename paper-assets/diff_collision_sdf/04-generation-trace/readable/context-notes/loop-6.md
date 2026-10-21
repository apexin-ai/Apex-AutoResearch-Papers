# director / loop_6.md

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`64e23302acba92fc03b7.json`](../../sessions/64/64e23302acba92fc03b7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-26T23:08:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-35807 cuda:0-3，westd-45947 cuda:0-1，共 6 卡，不得越界
- λ=0.1 placeholder 区域（claim3.tex 2处 + discussion.tex 1处 + abstract 尾句）在 eval 结果出来前**不要改**
- A3 CAR 已确认用 77.1%（post-m024fix），不要回退到 74.5%
- Eval 必须用 rotation-fixed eval_safelibero.py（`[::-1, ::-1]` 存在），seed=7，200 episodes
- 主文严格 8 页（当前恰好 8 页），任何新增内容必须等量压缩

### 2. 🖥️ 基础设施快照
- **westd-35807**: connect.westd.seetacloud.com, conda env = `libero`, 代码 /root/colliforce-vla
- **westd-45947**: connect.westd.seetacloud.com, conda env = `base`, 代码 /root/colliforce-vla
- Eval 命令模板已保存：`artifacts/eval_prep_l01_high.md`（λ=0.1 s0/s1/s2 + LoRA s2 全覆盖）
- Checkpoints: `/root/autodl-tmp/checkpoints/` 下各子目录
- 活跃进程（6个）：
  - westd-35807 cuda:0: eval_spatial_sdf_s0_l005_30k (PID 373135, ~23:40 UTC完成)
  - westd-35807 cuda:1: train_pi05_a1_obj_s0_l01_high (PID 271266, ~17:00 UTC 5/27)
  - westd-35807 cuda:2: train_pi05_a1_obj_s1_l01_high (PID 274407, ~17:45 UTC 5/27)
  - westd-35807 cuda:3: train_spatial_bowl_lora_control_s0 (PID 341425, ~06:10 UTC 5/28)
  - westd-45947 cuda:0: train_pi05_lora_baseline_s2 (PID 78558, ~20:15 UTC 5/27)
  - westd-45947 cuda:1: train_pi05_a1_obj_s2_l01_high (PID 425058, ~08:40 UTC 5/28)

### 3. 📊 当前状态
本轮完成了大量论文打磨：
- Claim 强度升级 6 项（illusory / counterproductive / demos sufficient / tradeoff dissolves / metric property / Pi0+A1 paradox）
- Em-dash 全部清零，appendix 阈值敏感度表填充，A3 CAR 更新为 77.1%
- Reviewer coherence 复查通过，tone 一致，无旧措辞残留
- 编译 0 errors，14 pages（8 main + 1 ref + 5 appendix）

RUNNING 实验 6 个（见上），全部是训练或 eval，无 PREPARING。
等待：spatial_bowl eval 回调（~1h），后续 λ=0.1 s0/s1 训练完成回调是关键路径。

### 4. 📋 待办
- eval_spatial_sdf_s0_l005_30k 完成 → 分析 CAR/TSR，判断跨场景泛化；结果写入 report，不急入论文（spatial_bowl 不在关键路径）
- λ=0.1 s0 训练完成（~17:00 UTC 5/27）→ 立即启动 eval（命令在 artifacts/eval_prep_l01_high.md）
- λ=0.1 s1 训练完成（~17:45 UTC 5/27）→ 同上
- 2-seed eval 结果出齐（~5/27 20:00 UTC）→ **A/B/C 场景判定**：均值≤57% → B，57-60% → C，≥60% → A。判定后立即 patch claim3 placeholder + discussion + abstract 尾句
- LoRA s2 训练完成（~20:15 UTC 5/27）→ eval → 3v3 统计确认 low-λ 结论
- λ=0.1 s2 完成（~08:40 UTC 5/28）→ 3-seed 验证，若时间紧可降级为 footnote
- **DDL: 5/28 12:00 UTC**，距 s0/s1 eval 出结果约 23h 修论文窗口

### 5. 🎯 战略上下文
- 论文核心：VLA safety evaluation 系统性缺陷。3 个 claim：fake safety (illusory) / EE-only counterproductive / demos sufficient
- Claim 1+2 证据链完整已定稿。**Claim 3 是唯一 pending**：low-λ 已确认 SDF 无效，λ=0.1 决定最终叙事（A=dose-response / B=全域 negative / C=灰区）
- **A/B/C 判定阈值**（D033 Reviewer 统计分析）：零分布 mean=54.5%, std=2.17%（5 个无效 SDF 测量值）。λ=0.1 作为独立检验对象，不纳入零分布
- **硬约束检查**：λ=0.1 eval 必须检查 TSR≥35% + frozen_ee=0%，任一不满足则 CAR 数字无效（历史上 Pi0+λ=0.1 产生过 action collapse）
- 易错点：不要把 spatial_bowl 结果混入 object_pudding 的统计比较；spatial_bowl baseline CAR=13%（vs object_pudding 27%），scale 完全不同
- paper_framing.md 已更新到最新状态，是所有决策的 ground truth


---
