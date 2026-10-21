# agent / loop_3.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`26c56aab10aae2d790fe.json`](../../sessions/26/26c56aab10aae2d790fe.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: idle_timeout
updated: '2026-05-12T17:20:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 `gpu_ids: [cuda:0, cuda:1, cuda:2, cuda:3]`，全在 seetacloud-westd-4x5090 上。home-1x5090 的 cuda:0 也可用但需单独确认
- seetacloud-westd-4x5090 系统 RAM 不足以同时跑两个 repo-level 训练（70k 样本 × max_seq_length=4096）。repo-level CLS 和 CWM **必须串行**，不可同时加载两个 70k 数据集——v3 已因此被 OOM killer SIGKILL
- `submit_training_job` 的命令必须自带环境激活（`source /root/miniconda3/bin/activate && python ...`），seetacloud 用 conda 不是 venv
- repo-level 脚本有 `sample_weight` KeyError 历史——v2 因此失败，v3/v4 修复了 WeightedDataCollator 但需确认 Worker 的修复是否生效
- ARR May 25 deadline = 13 天，repo-level 是关键路径，不能再拖

### 2. 🖥️ 基础设施快照
- **seetacloud-westd-4x5090**: 4× RTX 5090, root@seetacloud-westd-4x5090, 工作目录 `/home/sonny/exec-sim-repair-verifier`（注意：项目 path 是 sonny 但 seetacloud account 是 root）
- **home-1x5090**: 1× RTX 5090, sonny@home-1x5090, 同上工作目录
- **westd-48478**: sonny@westd-48478（用途不明，近期无实验在此跑）
- Python: seetacloud 用 `/root/miniconda3/bin/python`（conda base env）; home 需探测
- 模型: Qwen3-4B LoRA 微调（函数级 checkpoint 已就绪，repo-level checkpoint 尚无——v3 在 step 188/6633 就被杀了）
- 8B 模型: cls8b/cwm8b 3-seed 全部完成（在 seetacloud + home 上跑过）
- W&B: 项目有 wandb 集成（fetch_wandb_metrics 可用）
- 活跃进程: **无**（v3 CLS PID 69782 已被 OOM SIGKILL，CWM 同时被杀）
- 活跃 Cron: **无**（reconcile 返回 0）
- 活跃 Worker: 2 个 running —— `worker_ops_repo-level-v3-recovery`（修复 OOM 问题）+ `worker_paper_figure_fig1_reformulation`（画 Figure 1）

### 3. 📊 当前状态
**刚做完**: repo-level-cls-v3 和 repo-level-cwm-v3 同时被系统 OOM SIGKILL，已派 recovery Worker 诊断和修复。之前完成了 matched-seed error overlap 分析（Oracle ensemble 90.63%）和 4B CLS vs CWM paired bootstrap（gap=1.25pp, p=0.025）。

**Registry 全景** (35 实验):
- **PREPARING**: repo-level-cls-v4, repo-level-cls-home, repo-level-cwm-v2, repo-level-cls-v2（后两个标记 failed 但状态是 PREPARING，是 v2 的遗留残骸）
- **RUNNING**: 无
- **DONE success**: 27 个（函数级 CLS/CWM 5-seed、8B 3-seed、traj-level、LLM-judge、oracle 分析等全部完成）
- **DONE negative**: 3 个（cwm-baseline 函数级 null、per-test-majority-voting 无效、p2p-regression-rate ~1%）
- **DONE failed**: 5 个（repo-level-cls/cwm v1/v3、trace-then-judge）

**等待中**:
- Worker `repo-level-v3-recovery`: 正在修复 OOM 问题，预期产出是可串行运行的 repo-level 训练方案
- Worker `fig1_reformulation`: 正在画论文 Figure 1
- 无 Director 待决策事项（D027 recovery 方案已定：清理磁盘 + save_steps=50 + 串行）

### 4. 📋 待办（条件触发式）
- **v3-recovery Worker 完成** → 确认修复方案 → 先提交 repo-level-cls-v4 到 seetacloud cuda:2（或可用 GPU），**等 CLS 完成后再提交 CWM**（串行，不可并行）
- **repo-level CLS 训练完成（~15h）** → spawn eval Worker → 再提交 repo-level CWM 训练
- **repo-level CLS+CWM 都完成** → paired bootstrap 统计检验 → 按 D008 Go/No-Go 判定：≥3pp 全力 EMNLP Main，1-3pp 加 seeds，<1pp Kill C1 转 Plan B
- **fig1 Worker 完成** → 注册 artifact，检查质量
- **4 块 GPU 全空闲** → 可在 cuda:0/1 上跑 repo-level-cls-home 或投机启动 8B repo-level（D026 已提过但未执行）。但需先确认 RAM 够
- **repo-level 也 null** → 触发 red-section，产出 Framing 调整提案（Plan B: 收缩到 Findings/workshop，C3 Oracle + 两个 null + efficiency 叙事）

### 5. 🎯 战略上下文
**核心结论链**: 函数级 CLS≈CWM（null, gap<0.5pp）→ 8B scaling 放大 gap 到 2.43pp → repo-level 是 **决胜战场**——如果 repo-level CLS 显著优于 CWM，paper 立住 "complexity-dependent advantage" 叙事投 EMNLP Main；如果也 null，退守 Plan B。

**关键决策**:
- D008: Repo-level Go/No-Go 阈值已定（≥3pp/1-3pp/<1pp）
- D027: v3 OOM 恢复——串行训练是唯一安全路径
- Paper framing 3 pillars: Pillar 1（complexity-dependent）等 repo-level，Pillar 2（equivalence）和 Pillar 3（oracle frontier）已完备

**易错点**:
1. **不要同时在 seetacloud 上跑两个 repo-level 训练**——系统 RAM 会 OOM，这已经发生过两次（v1 和 v3）
2. 8B gap 数字：3-seed 修正值是 **2.26pp**（不是之前 2-seed 的 2.42pp），但 ROADMAP 里写的是 2.43pp（accuracy 口径 vs fail_f1 口径不同）——论文引用时注意口径一致
3. repo-level-cls-v2 和 repo-level-cwm-v2 的 PREPARING+failed 状态是残留，不要试图恢复它们，用 v4 系列
4. home-1x5090 只有 1 块 GPU，且 account 是 sonny 不是 root
5. Paper Agent writing_plan.yaml 还在等审批，但 Worker 已经在画 fig1——确认 writing plan 审批状态后再大规模铺写作 Worker


---
