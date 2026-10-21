# reviewer / loop_12.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_12.md`
- **Structured JSON:** [`8505325102d54b9bf760.json`](../../sessions/85/8505325102d54b9bf760.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-15T12:22:35+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd GPU 白名单：cuda:0/1/2/3。home GPU：cuda:0。跨项目越界立即 critical。
- CWM 8B 训练在 cuda:2（repo-level-cwm-8b-conda-v4），CLS 8B s42 resume 在 cuda:1。**不可 kill 这两个进程**——它们是论文核心数据。
- 论文主表数字必须用 **val-selected checkpoint**（D088 决策），不是 test-best。
- CLS 4B seed123 val-best ckpt-800 test=75.33% 是**已知 artifact**（论文 L165 标注），**不可纳入均值计算或区间下界**。所有正常 repo-level gap 在 24.8-26.5pp。
- "below chance level (50%)" 用于 parseable-only CWM accuracy (42-43%)，**不要改成 "below majority baseline (73%)"**——后者弱化论点。

### 2. 🖥️ 基础设施快照
- **westd**: seetacloud-westd-4x5090, root@westd, 工作目录 `/home/sonny/exec-sim-repair-verifier`
  - conda: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
  - 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-{4B,8B}/`
  - Checkpoints: `/root/autodl-tmp/checkpoints_repo_cls_*` 和 `/root/autodl-tmp/checkpoints_repo_cwm_*`
  - 数据: `/home/sonny/exec-sim-repair-verifier/data/swebench_full` (70748 train)
  - 活跃进程: CWM 8B (PID 266816, cuda:2, ~60%), CLS 8B s42 resume (PID 295789, cuda:1, ~61%)
  - cuda:0 和 cuda:3 空闲
- **home**: home-1x5090, sonny@home, 同工作目录。SSH 不稳定（最近 5 次超时），cuda:0 名义分配但实际不可用。
- **本地 workspace**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/`
  - 论文: `docs/paper/*.tex`
  - Registry/decisions/roadmap: 项目根目录下

### 3. 📊 当前状态
**刚完成**：Action Matrix v1 + v2 独立审查（Report #19 和 #20），已 post 给 Director。核心发现：16-26pp 区间下界来自 artifact [critical]，below chance 改动弱化论文 [warning]，LoRA rank 消融仅函数级留攻击面 [warning]。

**RUNNING 实验**：
- `repo-level-cwm-8b-conda-v4`: CWM 8B 训练，step ~4013/6633 (60.5%), ETA May 16 ~11:00 UTC
- `repo-level-cls-8b-s42-resume`: CLS 8B s42 full training，step ~4041/6633 (60.9%), ETA May 16 ~06:00 UTC

**ANALYZING**: `cls8b-seed123-ckpt200-test-eval` (accuracy=72.55%, seed123 test curve 最后补点, ckpt-200)

**等待中**: Director 对 Report #19/#20 的回应（16-26pp 是否改回 25.59pp，LoRA rank 实验设计确认）

### 4. 📋 待办（条件触发式）
- CWM 8B 训练完成（cron 回调）→ 核实 GPU 边界（cuda:2）→ 等 test eval 提交 → 核实 8B-8B gap 数字 → 如 unparseable >40% 则确认 formulation bottleneck narrative
- CLS 8B s42 resume 完成 → 核实 → 等 extended val sweep 提交 → 检查 val-test reversal 是否持续
- LoRA rank 消融实验提交（Director 批准后）→ 核实在 cuda:0 跑 + 只用函数级数据 → 结果出来后验证 CWM accuracy vs rank 单调性
- Relaxed matching 分析完成 → 核实 overall CWM accuracy 上界 → 确认 format compliance collapse 仍是主因
- Paper 修订提交审查 → 执行章节审查模式 B（特别关注：seq_length paragraph L163 是否更新了 ablation 结果 82.83%、数字与 registry 一致性、claim 降级幅度）

### 5. 🎯 战略上下文
- **核心结论链**: D007（函数级 CLS≈CWM null result）→ D016（repo-level 训练批准）→ D088（val-selected checkpoint 为主指标）→ D093（multi-seed gap 锁定 25.99pp mean）→ D094（seq_length confound 排除，97% gap 来自 formulation）
- **论文 DDL**: EMNLP 2026 ARR May 25（10 天）
- **最容易判断错的事**：
  1. seed123 4B test=75.33% 看起来像 gap 缩小的证据，实际是 ckpt-800 选择 artifact。**绝对不要把它当正常数据点**。
  2. CWM 8B 日志文件名和 registry exp_id 不一致（日志实际是 `repo-level-cwm-8b-conda-v2.log`），不要因为文件名困惑就误判实验状态。
  3. 论文 experiments.tex L163 的 seq_length paragraph 当前已有 ablation 结果（82.83%），但 Action Matrix 讨论中这个更新可能被遗漏——审查时务必核对此段是否仍写 "in progress"。
  4. Report #19/#20 的 critical finding（16-26pp 不可用）可能被 Director 采纳也可能被驳回。如果 Director 坚持 16-26pp，需要追问数据依据。
- **已发 19 份审查报告**（#1-#18 在前一轮 context，#19-#20 在本轮）。编号从 #21 继续。


---
