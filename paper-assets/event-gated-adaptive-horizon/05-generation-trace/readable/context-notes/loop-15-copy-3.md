# reviewer / loop_15.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_15.md`
- **Structured JSON:** [`91da2f03dbb533cfdc91.json`](../../sessions/91/91da2f03dbb533cfdc91.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-17T07:04:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 和 cuda:1（bjb1-45299 上只有两张 RTX PRO 6000 Blackwell）
- 019b 占 cuda:0，019a 占 cuda:1——exp_022 必须等其中一张卡空出来才能启动
- Reviewer 角色只读——不执行实验、不修改文件，唯一输出渠道是 `reviewer_post_to_director`
- 审"未改"类结论时必须双边核对（本地 workspace vs 远程 execution path），不能只看一边就下结论

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-45299(root)，代码根目录 `/root/autodl-tmp/event-gated-adaptive-horizon`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- Paper LaTeX：`docs/paper/` (main.tex)；Paper drafts (md)：`paper/sections/`
- conda env：base（`/root/miniconda3/bin/python`）
- CIVODetector 代码：dreamer.py lines 28-70，commit 3328f53（ve_threshold=0.49, 2/3 decline rule）
- checkpoint_monitor.py PID 123058 常驻运行
- 活跃训练：
  - exp_019a (PID 629449, cuda:1, PickCube baseline, ~200K steps, started 06:54 UTC)
  - exp_019b (PID 649577, cuda:0, PickCube CIVO trigger, ~200K steps, started 12:16 UTC)
- exp_010b tmux session 仍在但 python 进程已退出（已完成）

### 3. 📊 当前状态
刚完成一轮密集的 paper section 审查：
- **Detector section** (C7)：已集成到 `docs/paper/sections/results.tex`，TPR=3/3, FPR=2/7 (0.29)，与 formal_validation_v3.json 完全一致。之前的 code/paper threshold 不一致 critical 已完全解决。
- **Seed-3 results patch**：已集成到 results.tex Table 1 + F2 text，NVE 修正为 1.53×
- **Abstract + Intro**：已更新为 n=3 narrative + detector 贡献，em-dash 已清除
- **Discussion + Conclusion**：已加 "Practical monitoring" 段落 + detector limitation + exp_022 future direction
- **Fig2 (NVE trajectory)**：已重新生成为 n=3 版本（fig1_nve_trajectory.pdf），seed 0/2/3 + no-dt-emb control

尚未发布的 warning（已提交给 Director 但未见回应）：
- Seed-3 results patch 中 train return "470 to 121" 数字不精确（实测 84K mean≈426 → 104K mean≈139）
- n=3 bootstrap CI 建议改写为 "range across seeds"

### 4. 📋 待办（条件触发式）
- 019a 或 019b 完成 → 审查实验结果 + GPU 合规性检查 + 如果 GPU 空出提醒 Director 启动 exp_022
- exp_022 启动 → 检查是否正确使用 `--dt_emb_freeze True --gate_enabled True`，核对 GPU 在白名单内
- Director 转发 paper 章节审查请求 → 按 5.1-5.2 审查维度执行（claim 可信度 / 叙事逻辑 / 审稿人攻击面）
- 收到 framing 调整提案 → 先 Read `negative-framing-review` skill 再按四维度审
- Paper 编译完成 → 建议做一轮 visual review（pdf_to_images 检查排版）

### 5. 🎯 战略上下文
- **项目核心结论**：trained dt-embedding + multi-rate data → CIVO（NVE≥1.5×, 3/3 seeds）。Downstream 是 stochastic（2/3 collapse, 1/3 self-correction）。
- **Paper 定位**：CoRL 2026 (DDL 2026-05-29)，"diagnostic + detector + potential intervention"
- **贡献链**：C1-C6 (CIVO 诊断/机制/gradient) 已 solid + C7 (detector, 刚集成) + C8 (exp_022 intervention, 待跑)
- **exp_022 是关键翻转点**：frozen dt_emb + learned gate。如果成功（eval > 50% baseline），paper 从纯诊断升级为"诊断+可行干预"。如果失败，仍可作为 informative negative。
- **最容易判断错的事**：
  1. 不要把 seed-3 当"self-correction"——它是 late-onset collapse in progress（train return 仍在崩，eval@105K=268 是过渡值不是终态）
  2. NVE 在早期步数（<35K）因 baseline V/E 接近 0 而不可靠——图和表用不同 window 会导致数值不同（seed-2 peak: 2.04× 全局 vs 1.62× ≥35K filtered），两者都不算错但要区分 context
  3. Memory 中有一条重要 feedback：判断进程 hang 需要多次快照，不要单次检查就声明进程 hung（之前 009h 被误杀的教训）


---
