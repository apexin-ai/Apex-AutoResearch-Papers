# agent / loop_2.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`66d0c03a697b27d7c401.json`](../../sessions/66/66d0c03a697b27d7c401.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: idle_timeout
updated: '2026-05-14T01:58:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: 只能用 westd-39279 的 cuda:0 和 cuda:1，submit 前必须 `get_project_resource_usage` 或查 config 确认
- **C001**: 所有 plan001/plan013 系列实验统一使用 `data/train_500_seed42.jsonl`，禁止用 `proofwriter_fol_500.jsonl`
- **C002**: 所有训练命令必须以 `export CUDA_VISIBLE_DEVICES=N &&` 开头（非 inline 赋值），提交后 `nvidia-smi` 验证只占目标 GPU。2026-05-14 因 inline 赋值导致双 GPU 溢出事故（plan013-r1 + plan001-s43 同时失败）
- **C003**: 训练必须设 `log_completions=False` + `save_total_limit=1`，output_dir 放 `/root/autodl-tmp/outputs/`。250GB 系统盘已被 TRL completions parquet 撑满过一次
- **submit_training_job 命令格式**: 必须用 `bash -c "export CUDA_VISIBLE_DEVICES=N && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py ..."`，tmux 默认 sh 不识别 source

### 2. 🖥️ 基础设施快照
- **服务器**: westd-39279，2× RTX PRO 6000 Blackwell 94GB VRAM
- **工作目录**: `/root/solver-trace-ablation/`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **CUDA**: 12.8, PyTorch 2.10.0+cu128
- **模型**: Qwen3-4B，通过 ModelScope 下载，路径 `/root/solver-trace-ablation/models/Qwen3-4B`（7.6GB）
- **训练数据**: `/root/solver-trace-ablation/data/train_500_seed42.jsonl`（500 条 FOLIO FOL）
- **eval 数据**: `/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl`（100 条）
- **Outputs**: `/root/autodl-tmp/outputs/` 下按 `plan001_exec_only_s42/` 等命名
- **Solvers**: Prover9 (源码编译), SWI-Prolog 8.4.2, Z3 4.16.0.0
- **活跃进程**: 
  - plan001-exec-only-s43-r4: PID 136339, cuda:1, tmux session
  - plan013-random-reward-s42-r4: PID 136261, cuda:0, tmux session
- **活跃 Cron**: reconcile 返回 0（可能是 cron 未正确注册，需要手动 check_job_status 确认两个 RUNNING 实验状态）

### 3. 📊 当前状态
两个实验正在运行（r4 = 第 4 次尝试，之前因磁盘满/OOM/配置错误连续失败）：
- **plan001-exec-only-s43-r4** (cuda:1): exec-only baseline seed=43, 500 步。这是 3-seed baseline 的第 2 个 seed（seed=42 已成功完成，last100 prove_rate=0.865）
- **plan013-random-reward-s42-r4** (cuda:0): random reward baseline, 500 步。用随机值替代 ISR，隔离 ISR-specific signal vs multi-objective regularization。Dream 审稿认定此实验为必修 (M2/W7)

**Worker 池 = 0**（两个实验提交后 Worker 已退出，等 cron 回调）。

**已完成的关键实验**:
- plan001-exec-only-s42-r2: SUCCESS — exec-only 500 步 seed=42, last100 prove_rate=0.865, ISR=0.8612
- plan005-sta-low-s42: NEGATIVE — STA weight=0.1, last100 prove_rate=0.7725 (低于 exec-only 0.865), 但 ISR/PR ratio=0.298 说明 STA 维持了结构分离
- plan003-eval-exec-only-r5: SUCCESS — held-out eval 确认 exec-only ISR 提升是 organic 的 (proved_only_ISR=0.6423)
- sta-phase1-exec-sta-r5: NEGATIVE — 50/50 权重是 penalty effect，prove_rate 退化到 0.10

**等待中**: 两个 RUNNING 实验的 cron 完成回调。无 pending Director 决策。

### 4. 📋 待办（条件触发式）
- **plan001-exec-only-s43-r4 完成 → last100 prove_rate ≥ 0.80**: 确认 exec-only baseline 跨 seed 可复现 → 标记 plan001 第 2 seed done → 开始 seed=44 (第 3 seed) 或进入 plan002
- **plan001-exec-only-s43-r4 完成 → prove_rate < 0.60**: 调查是否 seed-specific 问题，与 seed=42 对比 windowed 趋势
- **plan013-random-reward-s42-r4 完成 → ISR 分析**: random reward 模式下 `isr_mean` 字段恒 = 0（随机值在 `random_reward` 字段）。对比 plan001 exec-only 的 prove_rate 趋势：若 random 组 prove_rate ≈ exec-only → multi-objective regularization 本身不影响训练 → ISR 的 specific signal 成立；若 random 组 prove_rate 显著低于 exec-only → 任何 penalty 都有 regularization 效果
- **两个实验都完成后**: 更新 report.md + memory.md → 向 Director 汇报（带 [资源] 行）→ 建议下一批：plan002 (exec+STA 500 步最优权重), plan_006 (Prolog), plan_014 (downstream validation)
- **plan005 NEGATIVE 的 Framing 提案**: 已在 registry notes 中记录分析，但尚未正式向 Director 提交 red-section Framing 调整提案。plan005 的 negative 结论需要走 Framing 流程——但 notes 中的"结构性发现"(ISR/PR ratio=0.298 稳定分离) 可能支持一个 "STA as monitoring metric + low-weight bonus" 的新 narrative，而非纯 negative

### 5. 🎯 战略上下文
**项目核心**: STA (Solver Trace Ablation) 用 component necessity testing (LOO ablation) 从 solver execution trace 派生 intensional structural reward (ISR)，用于 GRPO 训练 neurosymbolic formalizer。

**Decision chain 关键节点**:
- D003: binary ISR (fast_isr_fol) 无效 → 改 continuous ISR (full STA)
- D005/D007: exec-only checkpoint 的 ISR 提升是 organic 的，不是 hacking → 50/50 权重是 penalty effect
- D008: Dream 审稿 best 4/6 Borderline Reject → 5 个结构性弱点需修
- D009: 添加 C001/C002 约束防止 confound 和 GPU 溢出

**论文 story 已转向**: "STA detects reward hacking" → "STA as principled structural metric + proper integration (low weight/curriculum)"。plan005 negative 证实 STA weight=0.1 仍然拉低 prove_rate（0.7725 vs 0.865），但 ISR/PR ratio=0.298 维持结构分离——下一步需找到不牺牲 prove_rate 的集成方式。

**易错点**:
1. **plan013 isr_mean 字段是陷阱**: random_reward 模式下 `sta_reward`=0 → `isr_mean`=0，真正的随机值在 `random_reward` 字段。分析时看 prove_rate 趋势和 `random_reward` 字段，不看 `isr_mean`
2. **cron 可能没注册**: reconcile 返回 0，但两个实验 RUNNING。下一个 session 应立即 `check_job_status` 确认进程存活，必要时手动注册 cron
3. **磁盘空间**: 之前清理释放了 171GB，但两个新实验又在跑。train_grpo.py 已设 `log_completions=False` 但仍需监控
4. **DDL 2026-05-25**: 剩 11 天。必修实验还有 plan002 (exec+STA 最优权重 3 seed), plan_006 (Prolog 3 seed), plan_014 (downstream validation)。至少需要 ~15 GPU·h，时间紧张但可行
5. **plan005 的 Framing 提案还没正式提**: negative conclusion 按规则应该产出 Framing 调整提案向 Director 汇报，但上一个 session 可能因 reset 中断未完成此步骤


---
