# director / loop_5.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`d5a9c795831c7825af90.json`](../../sessions/d5/d5a9c795831c7825af90.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-12T22:16:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- seetacloud-westd-4x5090 有 cgroup 360GB RAM 限制，**禁止并行训练**（v3+v4 两次 OOM 确认，D028）。只能单 GPU 训练，其余 3 块空闲是结构性的
- home-1x5090 只有 62GB RAM，同样只能跑单实验
- repo-level CWM 已迭代 9 次、CLS 迭代 4 次，历史上多次出现 Worker 并行提交导致进程泄漏互杀（D031），CWM 提交必须单 Worker 串行
- seetacloud 根分区只有 ~30GB，模型/cache 必须放数据盘，CLS v3 就是磁盘满被 SIGKILL 的

### 2. 🖥️ 基础设施快照
- **seetacloud-westd-4x5090**: connect.westd.seetacloud.com [root], 代码路径 /home/sonny/exec-sim-repair-verifier
- **home-1x5090**: implicit5638.xyfu.me [sonny], 代码路径 /home/sonny/exec-sim-repair-verifier
- **westd-48478**: connect.westd.seetacloud.com [sonny]（备用，当前未用）
- 活跃进程：
  - repo-level-cwm-v9: seetacloud cuda:2, PID 95806, cron 已注册（120s 间隔），预计 ~20h
  - repo-level-cls-v4: home cuda:0, 刚提交/启动中，预计 ~12h
- 模型：Qwen3-4B LoRA（两个实验都是）
- 镜像：aml-train（conda 环境，不是 venv）

### 3. 📊 当前状态
Director session 6（本轮）主要做了：
1. 批准 Agent Session 5 reset（idle 180min）
2. 收到 Agent Session 5 启动报告：修正 registry（CLS v2/v3 → failed），确认 CWM v9 在跑、CLS v4 提交中
3. 派 Agent 等待期任务：准备 repo-level eval + paired bootstrap 脚本
4. 更新 ROADMAP（v7→v9, CLS-home→v4）
5. 批准 Agent + Director 双 reset（两边都已收敛，下一个行动点是训练完成 10-17h 后）

Registry: CWM v9 RUNNING, CLS v4 RUNNING/PREPARING。其余 45 个实验全 DONE（30 success, 3 negative, 12 failed）。

### 4. 📋 待办
- CLS v4 训练完成 → 立即跑 eval 脚本（不等 CWM v9）→ 记录 repo-level CLS metrics
- CWM v9 训练完成 → 立即跑 eval → paired bootstrap CLS vs CWM → Go/No-Go (D008)
- Go/No-Go 结果：
  - F1 diff ≥ 3pp + p<0.05 → 全力推进 EMNLP Main，派 Paper Agent patch repo-level 结果
  - F1 diff 1-3pp → 加 seeds 或数据量巩固
  - F1 diff < 1pp → Kill Claim 1 (complexity-dependent advantage)，pivot to Plan B
- Paper Agent 在 Step 2（图表+模板），等 repo-level 数据后进 Step 3-5

### 5. 🎯 战略上下文
- **核心论文 story**: execution simulation 可以从 generation 重构为 classification，函数级等价（TOST p=0.007），但 repo-level 复杂度下 CLS 应该优于 CWM → complexity-dependent advantage。4B 函数级 gap=1.25pp (p=0.025)，8B gap=2.43pp (p=0.007) 已支持 scaling 趋势
- **repo-level 是决胜战场**：如果 repo-level 不出 ≥3pp gap，Claim 1 站不住，论文降级为 equivalence analysis 而非 method paper
- **投稿目标**: ARR May 25（~13 天），时间线：训练 ~20h + eval 3h + Paper Agent ~2d = ~4-5d 可完成
- **易踩的坑**：
  - CWM 训练极其脆弱（已失败 8 次），常见问题：eval_steps/save_steps 不对齐、compute_loss OOM（需 pop labels before model forward）、tmux kill、磁盘满。CWM v9 已修复这些，但如果再失败需要认真诊断根因而不是简单重试
  - seetacloud 3 块空闲 GPU 不能用于训练（cgroup），不要浪费时间尝试并行
  - experiment_plan.yaml 中 per-test-precision-recall/block-corr-empirical/per-test-majority-voting 显示 "planned" 但实际已在 ROADMAP 中标记完成，是 plan 维护遗留问题


---
