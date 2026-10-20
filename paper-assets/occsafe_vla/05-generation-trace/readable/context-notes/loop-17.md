# director / loop_17.md

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_17.md`
- **Structured JSON:** [`05538472e15e2c4e1e17.json`](../../sessions/05/05538472e15e2c4e1e17.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_messages
updated: '2026-05-29T03:33:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 分配需通过 `get_project_status` 确认 `gpu_ids` 白名单，不得使用白名单外的 GPU
- AutoDL 服务器有 cgroup v2 GPU 限制问题，用户需要从 AutoDL 控制台重启服务器才能解决
- Figure 1 用户已明确拒绝 PaperBanana 重绘方案（`fig1_architecture_pb.py`），**不要再用 PaperBanana 重画 Figure 1**。当前使用 `fig1_architecture.py` 的回退版本
- BN eval mode 实验（RD2-W4）需要 `--occ_bn_eval True` 参数**重新训练**，不是 eval-time 切换——occ_head 的 BN 层在 eval 时不加载

### 2. 🖥️ 基础设施快照
- 论文目录：`/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/`
- 图表脚本：`figures/fig1_architecture.py`（当前使用）、`fig_car_factorial_combined.py`（Fig2）、`plot_gradient_v2_combined.py`（Fig3）
- 实验服务器：AutoDL（cgroup v2 问题待用户重启）
- 项目知识文件：`projects/occsafe_vla/` 下 ROADMAP.md / paper_framing.md / experiment_plan.yaml / report.md / decisions.yaml / constraints.yaml / mistakes.yaml
- 审稿阶段已启动，review_chat_id: `oc_faa96524df7d6444f5c8cbc48d5a616b`

### 3. 📊 当前状态
刚完成 Figure 1 回退到旧版 + 增量美化，重新编译论文 PDF 并上传飞书（`occsafe_vla_20260529_033203.pdf`）。等待用户游承松确认 Figure 1 是否满意。

审稿修复进度：17 个 issue 中 12 个已 resolved，5 个 open。D079 叙事重构已完成，Reviewer 给出 WARNING（Cell 4 数据同步 + permutation 排序问题已处理）。

GPU 实验全部 blocked：AutoDL 服务器 cgroup v2 限制，等用户重启。待跑：
- RD2-W4: BN eval mode training (`--occ_bn_eval True`, ~13h)
- RD3-W3: λ₀=0.001 sweep (~13h)
- RD3-W3: λ₀=0.1 sweep (~13h)
- 两个实验可能已完成：`random_occ_v2_s0_r4` 和 `full_occ_bn_v2_s2_r5`（预计 ~13:00 UTC May 29）

### 4. 📋 待办
- 用户确认 Figure 1 满意 → 继续处理剩余 5 个 open review issues
- 用户确认 Figure 1 不满意 → 在 `fig1_architecture.py` 基础上按反馈微调（不用 PaperBanana）
- AutoDL 服务器重启完成 → 立即派 Agent 启动 RD2-W4 + RD3-W3 三组实验并行
- `random_occ_v2_s0_r4` / `full_occ_bn_v2_s2_r5` 完成回调 → 分析结果，更新论文数据（η² claim、Cell 4 n=3→n=4 同步）
- 新实验结果出来 → 更新 results.tex 中的 permutation p-values 和 effect sizes

### 5. 🎯 战略上下文
- 目标：SafeRL Workshop @ RSS 2025 投稿
- 核心结论：2×2 factorial design（gradient flow ON/OFF × BN/LN）揭示 auxiliary OCC task 对 VLA 安全性的影响
- 关键发现：seed-dependent outcomes + overtraining 是 MVP 阶段主要发现；permutation ANOVA 现在是 primary 统计方法
- 易错点：(1) 不要把 `fig1_architecture_pb` 系列文件当作当前版本——用户明确拒绝了 (2) Cell 4 数据 n=3→n=4 同步是 deliberate defer（D075/D078），不要急着改 (3) η² 的 claim 需要等 N=15 数据确认后再更新 abstract 中的 TODO
- 用户对图表审美非常敏感，游承松已三次对 Figure 1 提意见——后续修改务必保守增量，不要大改


---
