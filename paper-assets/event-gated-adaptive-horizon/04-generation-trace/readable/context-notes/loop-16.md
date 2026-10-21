# director / loop_16.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_16.md`
- **Structured JSON:** [`f23fac1cbac03c4fdabb.json`](../../sessions/f2/f23fac1cbac03c4fdabb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_messages
updated: '2026-05-29T04:33:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-51268 的 cuda:0（cuda:1 物理不可用，已多次确认）
- D171 数据锁定：所有已有实验数据和论文数值冻结，禁止修改。新环境实验不受此限
- D177：Humanoid 实验已放弃（baseline NVE=12.2×，generic bootstrap overestimation），不要再跑 humanoid_008d_s0
- 论文正文严格 ≤8 页（用户要求，非 ICLR 官方限制）
- Figure 3 刚完成学术风格重构（低饱和度 muted palette + 加粗 + serif），用户已确认，不要回退样式

### 2. 🖥️ 基础设施快照
- 服务器：westd-51268 (connect.westd.seetacloud.com)，root 用户
- 工作目录：/root/autodl-tmp/event-gated-adaptive-horizon
- GPU：1× RTX PRO 6000（cuda:0），cuda:1 不可用
- 预置镜像 aml-train，conda 环境（/root/miniconda3/bin/python）
- 论文目录：本地 projects/event-gated-adaptive-horizon/docs/paper/
- 活跃进程：exp_quadruped_baseline_s0_r2 应为 PREPARING 状态（EGL 修复已应用 MUJOCO_EGL_DEVICE_ID=0）
- Cron：humanoid_baseline 完成回调已触发（实验 DONE）

### 3. 📊 当前状态
**刚做完**：
- 用户 4 项论文修改全部完成（摘要去数字、删 Broader Impact、Conclusion 扩充/Limitation 精简、正文压到 8 页）
- Figure 3 学术风格重构（低饱和度配色 + 加粗线条/边框/字体 + 数值标注 + baseline 参考线）已更新到正文
- 全文破折号去除（~40 处）、段落末行 orphan word 修复、Keywords 行修复
- cross_seed_summary.md 完成（9 组配置 × 多 seed，CIVO 计数已按 NVE≥2.0 校准为论文一致）

**Registry 状态**：
- exp_humanoid_baseline_s0: DONE (NVE=12.2×, 无学习, D177 放弃)
- exp_quadruped_baseline_s0_r2: PREPARING → 这是下一个要跑的实验
- exp_humanoid_008d_s0: PENDING → 已取消（D177）
- exp_quadruped_008d_s0: PENDING → 等 quadruped baseline 完成后串行

**Agent session 正在 RESET 中**（RESET_BOTH 已批准）

### 4. 📋 待办
- Agent RESET 完成 → 立即指令：跳过 humanoid_008d，直接启动 quadruped_baseline_s0_r2 on cuda:0
- quadruped_baseline_s0 完成 → 检查 eval_return 是否有意义行为 + NVE 是否 <2.0。如果 baseline 正常 → 启动 quadruped_008d_s0
- quadruped_008d_s0 完成 → 判定 CIVO 是否复现。复现 → scope expansion 1/1 成功（6→6.5/10）；不复现 → 重新评估 scope expansion 计划
- 用户可能继续提论文排版修改 → 响应优先级高于实验（用户说过"太慢了"）

### 5. 🎯 战略上下文
- **投稿目标**：ICLR 2027（~10月 DDL），从 CoRL 转来（D176）
- **核心 claim**：DreamerV3 trained dt_embedding 驱动 CIVO，frozen/removed dt_emb 可阻止
- **论文状态**：42 页（8 页正文 + refs + 34 页 appendix），Reviewer 评分 5→6/10，所有 Reviewer 改进已完成
- **scope expansion 现状**：Humanoid 失败（D177），全部押注 Quadruped。如果 Quadruped 也失败（baseline NVE>2.0），需要考虑 Hopper（plan_040）或接受当前 Walker+Cheetah+Cartpole 三环境结果
- **易错点**：
  - 不要把 Humanoid 的 generic bootstrap overestimation 误判为 CIVO
  - Quadruped baseline 如果 NVE 也偏高，先检查是否训练步数不够再下结论
  - 论文修改用户有两人（吴俊豪 + 周雪阳），周雪阳偏排版/视觉风格，吴俊豪偏内容/结构
  - Figure 3 的绘图脚本在 artifacts/figures/paper/fig2_nve_trajectory.py，但论文引用路径是 docs/paper/figures/fig1_nve_trajectory.pdf（名字不同）


---
