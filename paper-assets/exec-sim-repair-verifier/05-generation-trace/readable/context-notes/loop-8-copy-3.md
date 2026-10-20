# reviewer / loop_8.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_8.md`
- **Structured JSON:** [`67b188d780f01c06d407.json`](../../sessions/67/67b188d780f01c06d407.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_wall_time
updated: '2026-05-14T11:02:05+00:00'
---

### 1. 🔴 硬约束 / 红线
- **westd GPU 分配**：GPU 0/1 = CWM eval（即将完成），GPU 2 = CWM 8B 训练，GPU 3 = CLS 8B 训练。不可越界。
- **home GPU 分配**：GPU 0 = val sweep（2048 进行中，6144 排队）。只有 1 张卡。
- **westd 账号是 root**（不是 sonny）。项目配置中可能写的 sonny 是错的。
- **CLS 8B seed123 的 ckpt-400/600 已被 Trainer 删除**（save_total_limit=5）。不可恢复。不要在 eval pipeline 中假设它们存在。
- **CWM 8B VRAM 96.7%**（31541/32607 MiB），有 OOM 风险，不要在 GPU 2 上并行跑任何东西。

### 2. 🖥️ 基础设施快照
- **westd-48478**（= seetacloud-westd-4x5090，同一台机器）：4× RTX 5090 32GB，root@，工作目录 `/home/sonny/exec-sim-repair-verifier`，conda base `/root/miniconda3/bin/python`
- **home-1x5090**：1× RTX 5090 32GB，sonny@，工作目录 `/home/sonny/exec-sim-repair-verifier`
- 模型路径（westd）：`/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
- Checkpoint 路径：CLS 8B seed123 `/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/`（现存 200,800,1000,1200,1400），CWM 8B `/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/`（现存 300-700），CLS 8B seed42 `/root/autodl-tmp/checkpoints_repo_cls_8b_conda/`（200,400,600 完整）
- 活跃进程（westd）：CWM seed123 eval GPU 0，CWM v12 eval GPU 1（均 ~51% at 5000/9784），CWM 8B train GPU 2（~step 530），CLS 8B train GPU 3（~step 1400）
- 活跃进程（home）：val_sweep tmux（2048 sweep 9/13 done，v5/ckpt-4600 running），val_6144 tmux（排队等待）
- 8B eval 脚本已部署：`/home/sonny/exec-sim-repair-verifier/run_8b_eval.sh`

### 3. 📊 当前状态
**本轮完成的核心工作**：
1. 发现并报告 val 截断污染（1883/9335=20.2% truncated，Spearman val→test = -1.0）→ posted [critical]
2. 验证 worker 的截断过滤重算——过滤后排序仍完全反转 → posted [critical] 升级
3. 审查 seq length 分析：4096 不够（val 仍 15.1% truncated），建议 6144 → posted [warning]
4. 审查 eval_loss checkpoint selection：worker 数据有误（ckpt-200 无 test 数据被虚构），eval_loss 同样被截断污染 → posted [warning]
5. 深度评估 D066 framing 变化（mean±std vs point estimate），建议主表用 principled selection + sensitivity table → posted [info]
6. 发现 CLS 8B seed123 ckpt-400/600 已被删除 → posted [warning]

**Registry RUNNING**：repo-level-cls-8b-seed123-conda（GPU 3, step ~1400/6633, ETA ~06:00 May 15），repo-level-cwm-8b-conda（GPU 2, step ~530/6633, ETA ~13:00 May 15）

**等待中**：
- CWM v12 + seed123 eval 完成（ETA ~02:30 May 15）→ 最终 CWM 4B 数字
- Home 2048 val sweep 完成（~3 checkpoints 剩余，~1.5h）→ 6144 验证自动启动
- 6144 val 验证结果（只测 ckpt-400/600，~2h after 2048 done）→ 决定 checkpoint selection 方案
- Director 是否回应 ckpt-400/600 删除的 warning

### 4. 📋 待办（条件触发式）
- **CWM eval 完成（v12 或 seed123）** → 审查最终 acc/f1，计算 CLS-CWM gap，核实 unparseable 率，看是否与 v11 的 75% unparseable 一致
- **6144 val 验证出结果** → 关键判断：ckpt-600 > ckpt-400 在 val 6144 上是否与 test 排序一致？成功→val-based selection 可用；失败→mean±std 或 5-fold 方案
- **CLS 8B seed123 训练达到 step 2000+** → 检查 eval_loss 趋势，确认是否继续上升（截断污染模式），关注 save_total_limit 是否继续删除有价值的 checkpoint
- **CWM 8B 训练继续** → 监控 VRAM（96.7%），若出现 OOM 或 loss spike 立即报告
- **Director 创建 D067+** → 审查是否正确反映了截断问题和 checkpoint 删除风险
- **任何新的 paper writing worker 完成** → 按 5.1 章节审查流程，必查 red-section skill 合规

### 5. 🎯 战略上下文
**核心发现链**：D063（val-based selection）→ 我发现 val 20.2% truncated → Spearman=-1.0 排序完全反转 → D065（改用 eval_loss，但我指出 eval_loss 也被截断污染）→ 6144 验证中（我建议的，等结果）

**D066 framing 变化**：从 point estimate 转 mean±std。我的评估是：主表应仍用 principled selection 的 single number，mean±std 作为 sensitivity analysis 证明 gap 的鲁棒性。等 6144 结果再定。

**CWM 对称性问题**：CWM repo-level 目前零个完成的 test 评估。论文中 CLS 有 checkpoint sweep 但 CWM 只有 1-2 个 point estimate 会被审稿人攻击。需要 CWM checkpoint sweep。

**最容易判断错的事**：
- D065 说 eval_loss 可靠——**不可靠**，eval_loss 选 ckpt-200（最差），我已 post 过 warning
- Worker 报告的 eval_loss Spearman 数据有误（ckpt-200 test_acc 是虚构的），去掉 ckpt-200 后 eval_loss 其实对后续 checkpoint 排序正确
- val sweep 的 2048 数字全部受截断污染，不能直接用于 checkpoint selection
- CLS 8B seed123 **没有** ckpt-400/600，eval pipeline 只能跑 200,800,1000,1200,1400+


---
