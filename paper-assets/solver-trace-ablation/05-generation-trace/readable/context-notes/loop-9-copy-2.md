# agent / loop_9.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_9.md`
- **Structured JSON:** [`4cd3aebfc818be84592e.json`](../../sessions/4c/4cd3aebfc818be84592e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 9
reason: idle_timeout
updated: '2026-05-14T23:44:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：**仅 westd-39279:cuda:0 和 cuda:1**，submit_training_job 命令必须 `bash -c "export CUDA_VISIBLE_DEVICES=N && ..."`（C002）
- 训练数据统一：所有 FOL 实验必须用 `train_500_seed42.jsonl`（C001），不能用 proofwriter_fol_500.jsonl
- **磁盘 96% (240G/250G)**：output_dir 放 `/root/autodl-tmp/outputs/`，eval 后立即清理 checkpoint，`log_completions=False` + `save_total_limit=1`（C003）
- ISR 报告禁令：不可报 raw 3-seed mean ISR（被膨胀值污染）；不可报 genuine-only 2.4x（D051 作废，premise-count-matched 1.06x 才是定论）
- plan013 vs plan017 公式结构不同，论文不可简化为 "additive vs convex" 对照（D027）
- Prolog STA s44 = query-as-fact gaming（Reviewer override），不是 genuine。strict classifier Genuine=100% 不可信，必须交叉验证 n_necessary

### 2. 🖥️ 基础设施快照
- **服务器**: westd-39279，代码 `/root/solver-trace-ablation/`
- **Python/conda**: `/root/miniconda3/bin/python`，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（不是 venv）
- **GPU**: 2× RTX PRO 6000 Blackwell 96GB，CUDA 12.8，PyTorch 2.10.0+cu128
- **模型**: Qwen3-4B（ModelScope 下载），路径见代码 config
- **数据盘**: `/root/autodl-tmp/`（250GB，当前 96% 满）
- **Solvers**: Prover9 (LADR 编译), SWI-Prolog 8.4.2 (`/usr/bin/swipl`), Z3 4.16.0.0
- **活跃进程**: exp1-isr-b03-s44-r2 训练中（PID 10597, cuda:0, cron 监控中）
- **活跃 Workers**: 3 个
  - `worker_fix_paper-compilation-p0p1_20260514T232349`（修论文编译，turn 7）
  - `worker_fix_paper-figures-r2_20260514T232946`（修论文图表，turn 9）
  - `worker_eval_b03-isr-s43-random-s43_20260514T234153`（eval β=0.3 ISR-s43 + random-s43，turn 20，刚开始跑 eval）

### 3. 📊 当前状态
项目处于**论文写作阶段 + 补充实验收尾**。DDL: 2026-05-25（剩 11 天）。

Registry: 56 DONE / 1 RUNNING / 1 PENDING。三条 Claim 全部闭环（D056-D059）。

**正在进行**：
- exp1-isr-b03-s44-r2 在 cuda:0 训练中（β=0.3 ISR seed44 重试），cron 自动监控
- exp1-random-b03-s44 等待审批（PENDING）
- 3 个 Worker 分别处理：论文 LaTeX 编译错误、图表修复、β=0.3 checkpoint eval
- writing_plan.yaml 已 Director 审批（2026-05-14），Method + Experiments 章节 Worker 已启动

**等待中**：
- 3 个 Worker 回调（paper-compilation / paper-figures / eval-b03）
- exp1-isr-b03-s44-r2 训练完成 cron 回调
- exp1-random-b03-s44 审批

### 4. 📋 待办（条件触发式）
- Worker eval-b03 回调 → 用 eval 结果更新 registry metrics → 补充 paper β=0.3 dosage 数据行
- exp1-isr-b03-s44-r2 cron 回调 → spawn eval worker → 结果入 registry
- exp1-random-b03-s44 审批通过 → submit_on_allocated 提交到 cuda:1
- Worker paper-compilation 回调 → 检查 PDF 编译成功 → 如有问题再派 fix worker
- Worker paper-figures 回调 → 验证图表渲染 → register_artifact
- 所有 β=0.3 3-seed eval 完成 → 汇总到 paper_framing.md β dosage 表 → 汇报 Director
- 论文初稿完成 → submit_paper_to_review
- **磁盘告急**：训练/eval 完成后必须 spawn worker 清理 `/root/autodl-tmp/outputs/` 旧 checkpoint

### 5. 🎯 战略上下文
**核心结论链**：STA/ISR 是诊断工具（Claim 1 ✅），ISR-as-reward 全剂量失败——低剂量 meta-Goodhart + 高剂量 classic Goodhart（Claim 2 ✅ D057），跨 Prolog 3/3 seeds gaming 0% genuine（Claim 3 ✅ D059）。论文 story = Goodhart 诊断分析论文，不是"ISR 改善推理"论文。

**exp1 系列是补充实验**：β=0.3 的 ISR 和 random 3-seed 对照，补全论文 β dosage 表格（β=0.1 已有 3-seed，β=0.3 之前只有单 seed）。

**最易判断错的事**：
1. 看到高 ISR 数字不要以为是 genuine——检查 n_necessary 分布和 H7 分类
2. 磁盘 96% 满，任何大规模训练/eval 前先确认空间
3. 论文 framing 已经从"ISR improves reasoning"转向"ISR as diagnostic + Goodhart case study"（D010 转向），不要回退到旧 narrative
4. Hacking taxonomy 是 7 种（含第 7 种 query-as-fact），不是 6 种
5. SFT baseline 零 hacking 是关键对照——Goodhart 是 RL-reward-specific


---
