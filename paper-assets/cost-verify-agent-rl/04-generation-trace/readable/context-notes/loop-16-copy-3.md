# reviewer / loop_16.md

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_16.md`
- **Structured JSON:** [`c9baf83d088bfb23fe1e.json`](../../sessions/c9/c9baf83d088bfb23fe1e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: max_wall_time
updated: '2026-05-21T01:42:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-47453 白名单: cuda:0,1,2,3；bjb1-17606 白名单: cuda:0,1
- FSDP checkpoint (CPUOffload) 不能跨服务器加载——world_size mismatch + device mismatch 双重问题，已失败 3 次（bjb1 1次, westd 2次）。Seed 3 eval v2 的 fix 是跳过 optimizer state 加载
- exp029_seed3_v2 的 EXIT_CODE=129 是 W&B teardown BrokenPipeError 误报，训练实际完成 15/15 步，conclusion 已改为 success。不要被 on_failed hook 误导

### 2. 🖥️ 基础设施快照
- **westd-47453**: `/root/cost-verify-agent-rl`（代码）, `/root/autodl-tmp/`（checkpoints/数据）, conda base (`/root/miniconda3/bin/python`)
- **bjb1-17606**: 同结构，`/root/cost-verify-agent-rl` + `/root/autodl-tmp/`
- Seed 3 checkpoint: `/root/autodl-tmp/checkpoints/exp029-seed3/global_step_15/` (westd)
- ScienceWorld SFT: `/root/autodl-tmp/checkpoints/scienceworld_sft/huggingface` (bjb1+westd)
- W&B: entity `xiaoyucorynne-`, project `cost-verify-agent-rl`
- 活跃进程 (westd):
  - Cell C v3: PID 88226 (tmux), TaskRunner PID 94753, cuda:2,3, ~45GB/卡
  - Seed 3 OOD v2: PID ~536907 (TaskRunner), cuda:0,1, ~4.7GB/卡, W&B run `gqr6ux4z`
- bjb1: 全部空闲

### 3. 📊 当前状态
**刚做完**: 诊断 Seed 3 OOD eval FSDP 失败根因（optimizer state CPU/CUDA mismatch），Agent 提交了 fix（跳过 optimizer loading）并启动 v2 eval。
**正在运行**:
- `exp029_seed3_ood_v2` (RUNNING) — Seed 3 step15 on 134 OOD tasks, westd cuda:0,1, 启动 08:40 UTC, 预计 30-60min
- `scienceworld_grpo_cell_c_v3` (RUNNING) — ScienceWorld episode-level GRPO, westd cuda:2,3, 2/15 步完成, 严重减速(step2 耗 3h46min), ETA ~24-32h
**等待中**:
- Seed 3 OOD v2 结果回调 → 审查数据 + 论文 Table 1 更新建议
- Director 对 seed 间差异分析的反馈（已报告 12.5pp in-dist 差异统计不显著）

### 4. 📋 待办
- Seed 3 OOD v2 完成且成功 → 核实 OOD 数字, 与 Seed 1 (23.88%) 对比, 建议 Table 1 报告格式 (mean+range vs 分行)
- Seed 3 OOD v2 再次失败 → 报告 Director，建议方案3（手动合并 FSDP shards 为 HuggingFace 格式）
- Cell C v3 完成 step 5+ → 检查 ScienceWorld episode-level 是否真的避免 collapse（核心 cross-env 数据点）
- Cell C v3 日志停滞 >3h + GPU 0% → 可能 JVM crash，需要 kill 检查
- 论文 W6 修复待确认: ScienceWorld 结果应在 Limitations 中注明 single-seed/single-run

### 5. 🎯 战略上下文
- **核心论点**: step-independent GRPO 因 M1(信息丢失) + M2(符号误归因) 双机制失败; episode-level GRPO 是 minimum viable fix
- **论文状态**: R5 审查 8/10, 编译通过, ~8页正文, EMNLP 2026 target
- **Seed 3 OOD 是论文最后关键数据点**: multi-seed robustness evidence, 目前只有 Seed 1 的 23.88%
- **Cell C v3 (ScienceWorld episode-level) 是 nice-to-have**: 即使失败也不阻塞投稿（Cell A collapse 已够证明 cross-env），但成功会大幅强化 story
- **易错点**:
  - exp029_seed3_v2 registry 里 failure_reason 仍写着 EXIT_CODE=129，但 conclusion 是 success——不要被 failure_reason 字段误导
  - Cell C v3 的 0% GPU util 可能是正常的（ScienceWorld JVM 交互是 CPU 密集型），不要误判为 stall——用 `ls -la log` 检查文件修改时间，而非 GPU util
  - 32-task in-dist eval set 的 binomial SE ≈ 8.4pp，任何 <15pp 的 seed 间差异都不显著


---
