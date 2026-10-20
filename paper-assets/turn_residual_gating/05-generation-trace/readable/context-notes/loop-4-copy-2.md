# reviewer / loop_4.md

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_4.md`
- **Structured JSON:** [`b2a48f87bfbde3109783.json`](../../sessions/b2/b2a48f87bfbde3109783.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_wall_time
updated: '2026-05-22T22:49:52+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 `westd-20861:cuda:0`（单卡）。已发生 1 次 GPU 资源冲突导致 SS s42 OOM（gradient_conflict_analysis.py 占 70GB 挤爆训练），Director 标记 CRITICAL。**任何 GPU 密集任务必须等 GPU 空闲再启动**。
- DDL 是 **ARR May 2026-05-25**（不是之前误记的 August 03）。剩余 ~60h。
- SS s42 已中断 2 次（OOM + SSH 断连），第 3 次用 tmux 启动。**所有长时间训练必须 tmux/nohup + 日志重定向**。
- config.py 默认值与 v7 实际值有 4 处不同（lambda_gar=2→1, init_bias=2→1.5, gate_lr_multiplier=1→10, gar_target=0.3→0.5），所有训练脚本必须显式传这 4 个参数。

### 2. 🖥️ 基础设施快照
- 服务器：`westd-20861`，工作目录 `/root/turn_residual_gating`
- Python：`/root/miniconda3/bin/python3.12`（conda base 环境，不用 venv）
- 模型：`/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct`
- 数据：`/root/turn_residual_gating/data/ultrachat_8k`（训练），`data/ultrachat_eval_heldout.json`（eval）
- 活跃进程：SS s42 resume v3（PID 33402，tmux session `ss_s42_v3`，日志 `runs/d048_ss_s42_resume_v3.log`，从 epoch_0 恢复跑 epoch 1-2）
- D048 队列脚本：`scripts/d048_queue_runner.sh`（截断至 8 项：SS eval → AR N=50 → SS s123/s456 → Base s123/s456 → TG s123/s456）
- 论文本地：`/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/`，13 页 0 errors
- 数字更新脚本：本地 `scripts/update_paper_numbers.py`（dry-run 默认，`--apply` 才写入）

### 3. 📊 当前状态
**刚完成**：Round 3 审稿报告全部 13 项写作修复（GAR→Goal Accessibility Ratio、causal→diagnostic、页数压缩至 8 页、Appendix D 6 图表、loss table failure mechanism 列等）。queue_runner 截断至 72h 内可完成的 8 项。论文编译通过（13 页 0 error）。

**RUNNING**：`d048_ss_s42`（resume v3，epoch 1-2，预计 ~20:00 UTC 完成）

**等待中**：
- SS s42 训练完成 → on_complete hook 触发 → 需审查结果
- SS s42 eval + AR N=50 existing eval（queue_runner 排队中，SS 训练完即启动）
- 后续 SS s123/s456 + Base/TG multi-seed 串行执行

### 4. 📋 待办（条件触发式）
- SS s42 训练完成（cron:on_complete）→ 审查 epoch_1/epoch_2 checkpoint 完整性 + loss 曲线正常性 + GPU 是否释放
- SS s42 eval 完成 → 核实 AR N=50 bootstrap CI 与 Table 1 mid_turns 定义一致（必须用 `curve[2:]` = turns 3-T）
- AR N=50 existing 完成 → 核实 5 条件 AR GAR 与 registry 已有 N=5 数据方向一致
- SS s123/s456 完成 → 计算 3-seed mean±std，检查 CoV（>50% 则 SS 降级为 unstable）
- Base/TG multi-seed 完成 → 核实 TG≈Base≈LO 结论在 seed variance 下仍成立
- 所有 multi-seed 完成 → `update_paper_numbers.py --dry-run` 先看差异，确认后 `--apply`
- 论文数字更新后 → 最终编译 + 页数检查（必须 ≤8 页主文）+ 交叉核对 Abstract/Intro/Conclusion 一致性
- **异常**：任何训练中断 → 检查 GPU 是否有竞争进程（nvidia-smi），确认 tmux 存活

### 5. 🎯 战略上下文
- **核心结论**：ThreadGate 的 auxiliary GAR loss 在 TF 下有效（GAR 0.50）但 AR 下完全失效（GAR 0.016），~20-33× gap。根因是 exposure bias（text distribution shift），不是梯度冲突（PCGrad 排除）。SS 是唯一有效 training-time mitigation（gap 31×→1.57×）。论文 framing 从 "method paper" 转为 "diagnostic/negative result paper"。
- **DDL 紧张**：72h 内需完成 SS 3-seed + AR N=50 + Base/TG multi-seed + 论文数字更新。buffer 仅 ~4h。
- **易错点 1**：GAR 全称是 "Goal **Accessibility** Ratio"（Dongre 原文），不是 "Attention"——已全文替换，但如果有新增文本务必用正确名称。
- **易错点 2**：mid_turns = `avg_gar[2:]`（0-indexed）= turns 3-T（1-indexed），不是 "turns 2-T"。bootstrap CI 和 eval 脚本已统一为 `curve[2:]`。
- **易错点 3**：LO/UG/PCGrad 仍为单种子（被 DDL triage 砍掉）。如果 Round 4 reviewer 追问，这是已知 gap，Limitations 段已覆盖。
- **关键决策链**：D048（multi-seed 修复计划）→ D049（Round 3 action matrix，不降级 SS claim）。paper_framing.md 是论文 narrative 权威来源。


---
