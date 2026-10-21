# reviewer / loop_15.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_15.md`
- **Structured JSON:** [`f17a9c23e8a412cc480e.json`](../../sessions/f1/f17a9c23e8a412cc480e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-16T02:12:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- CWM 8B 训练已确认严重过拟合（eval_loss best at step 400, 之后单调上升到 0.521）。**禁止从 ckpt-400 以外的 checkpoint resume 训练**。Director 已下令终止 v6。
- 8B s42 val-best 已从 ckpt-1000 切换到 **ckpt-3600**（resume sweep 发现，val=90.28%）。论文主表用 ckpt-3600，**不要再用 ckpt-1000 数字**。
- 论文 ICC=0.191 / DEFF=3.97 是 **function-level**。新出的 repo-level ICC=0.3146 / DEFF=114.4 是不同层级，**不可混用**。
- per-mutation P/R 分析中 4B 对比基线用了错误的 ckpt-600（应为 val-best ckpt-4600）。**已向 Director 报告，等待修正前不要引用 4B per-mutation 对比数据**。

### 2. 🖥️ 基础设施快照
- 服务器：`seetacloud-westd-4x5090`（root）+ `home-1x5090`（sonny，当前离线）
- 工作目录（远程）：`/home/sonny/exec-sim-repair-verifier`
- Python：`/root/miniconda3/bin/python3`（conda base）
- 模型：`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
- CLS checkpoints：`/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/`（ckpt-600 起），seed123 backup `/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000/`
- CWM checkpoints：`/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-400`（唯一有效 ckpt）
- Eval 输出：`/root/autodl-tmp/eval_results/`
- 论文源码（本地）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/`
- 活跃进程（截至 handoff）：
  - PID 443221: CWM 8B v3 eval, cuda:3, ~57% (5632/9784)
  - PID 446873: CLS 8B ckpt-3600 test v2, cuda:2
  - PID 448100: CWM 8B eval shard2 (idx 7680-9784), cuda:1
  - PID 447483/447490: CLS 8B seed123 ckpt-3000 mutation, cuda:0

### 3. 📊 当前状态
本轮审查了 7 个 worker 完成通知：
- **已解决 CRITICAL**：GPU 2 上 CWM 训练孤儿进程（PID 442200, ckpt-6100 resume）已被杀死
- **已解决**：GPU 0/1 上错误标记为 "ghost" 的 CLS ckpt-1000 eval 已清理
- **已完成分析**：ckpt-3600 mutation breakdown（boundary_removal 46.9%）、8B block correlation（ICC=0.3146）、per-mutation P/R（8B 有效，4B 用错 ckpt）
- **RUNNING 实验**：cwm8b-ckpt400-test-eval-v3 (cuda:3)、cwm8b-ckpt400-test-eval-shard2 (cuda:1)、cls8b-s42-resume-ckpt3600-test-v2 (cuda:2)、cls8b-seed123-ckpt3000-mutation (cuda:0)
- **paper worker 失败**：`worker_paper_full-consistency-review` status=failed，未产出结果。论文数字我已人工交叉验证过 experiments.tex 主要指标，与 registry 一致。

### 4. 📋 待办（条件触发式）
- CWM 8B v3 eval 完成（~9h ETA）→ **立即核实 overall accuracy + unparseable rate**，与 4B CWM (58.04%, 53.7% unparse) 对比，锁定 8B-8B gap。这是论文 Table 4 最后一个 TBD。
- cls8b-seed123-ckpt3000-mutation 完成 → 与 s42 ckpt-3600 的 boundary_removal 46.9% 对比，确认是否跨 seed 一致。
- cls8b-s42-resume-ckpt3600-test-v2 完成 → 验证 accuracy 是否复现 84.48%（v1 结果）。如有差异 > 0.5pp，标 WARNING。
- CWM shard2 完成 → 确认与 v3 主进程结果的一致性和覆盖完整性（index overlap / gap）。
- 4B per-mutation P/R 用 ckpt-4600 重跑后 → 审查 boundary_removal 是否保持 fail bias 趋势（与 8B pass bias 对比）。
- 论文章节提交审查 → 按 §5 章节写作对抗审查模式执行。

### 5. 🎯 战略上下文
- **核心 story**：CLS vs CWM gap 是 complexity-dependent。function-level ≈1pp，repo-level ≈25pp。CWM 在 repo-level 崩溃（53-67% unparseable，parseable-only 42-43% < random）。
- **DDL**：EMNLP 2026 ARR May 25，剩 9 天。Paper Agent 已在写 full draft。
- **最大风险**：CWM 8B eval 是 Table 4 最后缺口。如果 CWM 8B 在 repo-level 显著好于 4B（>65%），则 "generation bottleneck not capacity" 的 claim 会被削弱——需要调整 narrative。如果 CWM 8B ≈ 4B（~58-60%），则完美支持 story。
- **易错点**：
  1. 不要把 function-level ICC (0.191) 和 repo-level ICC (0.3146) 混用
  2. ckpt-3600 是 s42 resume 的 val-best，不是原始训练的——checkpoint 目录是 `checkpoints_repo_cls_8b_s42_resume/` 不是 `checkpoints_repo_cls_8b_conda/`
  3. 4B-4B gap (25.59pp) 目前是 single seed，论文 Limitations 已诚实披露
  4. CWM eval shard2 从 idx 7680 开始，v3 从头跑——如果 v3 跑过 7680 会有重叠，合并时需 dedup


---
